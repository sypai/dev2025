package handlers

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"net/http"
	"strconv"

	"basic-expense-tracker/models"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
)

type ExpenseHandler struct {
	DB     *sql.DB
	router http.Handler // internal router
}

func NewExpenseHandler(db *sql.DB) *ExpenseHandler {
	h := &ExpenseHandler{DB: db}

	r := chi.NewRouter()
	r.Use(middleware.Logger)
	r.Get("/", h.HandleRoot)

	r.Route("/expenses", func(r chi.Router) {
		r.Get("/", h.HandleGETExpenses)
		r.Post("/", h.HandlePOSTExpense)
		r.Get("/{id}", h.HandleGETExpenseByID)
		r.Delete("/{id}", h.HandleDELETEExpenseByID)
	})

	h.router = r
	return h
}

func (h *ExpenseHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	h.router.ServeHTTP(w, r) // delegate to chi
}

// root handler
func (h *ExpenseHandler) HandleRoot(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "welcome! track you expenses!")
}

func (h *ExpenseHandler) HandleExpenses(w http.ResponseWriter, r *http.Request) {
	switch r.Method {
	case http.MethodGet:
		h.HandleGETExpenses(w, r)
	case http.MethodPost:
		h.HandlePOSTExpense(w, r)
	default:
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
	}
}

// /GET expenses
func (h *ExpenseHandler) HandleGETExpenses(w http.ResponseWriter, r *http.Request) {
	rows, err := h.DB.Query(`SELECT id, amount, category, note, date FROM expenses`)
	if err != nil {
		http.Error(w, "query failed", http.StatusInternalServerError)
		return
	}
	defer rows.Close()

	var expenses []models.Expense
	for rows.Next() {
		var exp models.Expense
		if err := rows.Scan(&exp.ID, &exp.Amount, &exp.Category, &exp.Note, &exp.Date); err != nil {
			continue
		}
		expenses = append(expenses, exp)
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(expenses)
}

// /POST expenses
func (h *ExpenseHandler) HandlePOSTExpense(w http.ResponseWriter, r *http.Request) {
	var exp models.Expense
	if err := json.NewDecoder(r.Body).Decode(&exp); err != nil {
		http.Error(w, "invalid request", http.StatusBadRequest)
		return
	}

	res, err := h.DB.Exec(`INSERT INTO expenses (amount, category, note, date)
		VALUES (?, ?, ?, ?)`, exp.Amount, exp.Category, exp.Note, exp.Date)
	if err != nil {
		http.Error(w, "insert failed", http.StatusInternalServerError)
		return
	}

	id, _ := res.LastInsertId()
	exp.ID = int(id)

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(exp)
}

func (h *ExpenseHandler) HandleGETExpenseByID(w http.ResponseWriter, r *http.Request) {
	idStr := chi.URLParam(r, "id")

	id, err := strconv.Atoi(idStr)
	if err != nil {
		http.Error(w, "Invalid ID", http.StatusBadRequest)
		return
	}

	var expense models.Expense
	err = h.DB.QueryRow(`SELECT id, amount, category, note, date FROM expenses WHERE id = ?`, id).
		Scan(&expense.ID, &expense.Amount, &expense.Category, &expense.Note, &expense.Date)

	if err == sql.ErrNoRows {
		http.Error(w, "Expense not found", http.StatusNotFound)
		return
	} else if err != nil {
		http.Error(w, "Query error", http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(expense)
}

func (h *ExpenseHandler) HandleDELETEExpenseByID(w http.ResponseWriter, r *http.Request) {
	idStr := chi.URLParam(r, "id")

	id, err := strconv.Atoi(idStr)
	if err != nil {
		http.Error(w, "Invalid expense ID", http.StatusBadRequest)
		return
	}

	result, err := h.DB.Exec(`DELETE FROM expenses WHERE id = ?`, id)
	if err != nil {
		http.Error(w, "Failed to delete expense", http.StatusInternalServerError)
		return
	}

	rowsAffected, _ := result.RowsAffected()
	if rowsAffected == 0 {
		http.Error(w, "Expense not found", http.StatusNotFound)
		return
	}

	w.WriteHeader(http.StatusNoContent) // 204 No Content
}
