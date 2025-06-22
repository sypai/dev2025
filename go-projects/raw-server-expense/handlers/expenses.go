package handlers

import (
	"basic-expense-tracker/models"
	"database/sql"
	"encoding/json"
	"errors"
	"net/http"
	"strconv"
	"strings"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
)

type ExpenseHandler struct {
	DB     *sql.DB
	router http.Handler
}

func NewExpenseHandler(db *sql.DB) *ExpenseHandler {
	h := &ExpenseHandler{DB: db}

	r := chi.NewRouter()
	r.Use(middleware.RequestID)
	r.Use(middleware.Logger)
	r.Use(middleware.Recoverer)
	r.Use(jsonContentType)

	r.Get("/", h.HandleRoot)

	r.Route("/expenses", func(r chi.Router) {
		r.Get("/", h.HandleGETExpenses)
		r.Post("/", h.HandlePOSTExpense)
		r.Get("/{id}", h.HandleGETExpenseByID)
		r.Put("/{id}", h.HandlePUTExpenseByID)
		r.Delete("/{id}", h.HandleDELETEExpenseByID)
	})

	h.router = r
	return h
}

func (h *ExpenseHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	h.router.ServeHTTP(w, r)
}

// --- Middleware to enforce JSON content type
func jsonContentType(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		next.ServeHTTP(w, r)
	})
}

// --- Root handler
func (h *ExpenseHandler) HandleRoot(w http.ResponseWriter, r *http.Request) {
	json.NewEncoder(w).Encode(map[string]string{"message": "📘 Welcome to the Expense Tracker API!"})
}

// --- GET /expenses with optional query filtering
func (h *ExpenseHandler) HandleGETExpenses(w http.ResponseWriter, r *http.Request) {
	category := strings.TrimSpace(r.URL.Query().Get("category"))

	var (
		rows *sql.Rows
		err  error
	)

	if category != "" {
		rows, err = h.DB.Query(`SELECT id, amount, category, note, date FROM expenses WHERE category = ?`, category)
	} else {
		rows, err = h.DB.Query(`SELECT id, amount, category, note, date FROM expenses`)
	}

	if err != nil {
		http.Error(w, "Query failed", http.StatusInternalServerError)
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

	json.NewEncoder(w).Encode(expenses)
}

// --- POST /expenses
func (h *ExpenseHandler) HandlePOSTExpense(w http.ResponseWriter, r *http.Request) {
	var exp models.Expense
	if err := json.NewDecoder(r.Body).Decode(&exp); err != nil {
		http.Error(w, "Invalid JSON body", http.StatusBadRequest)
		return
	}

	res, err := h.DB.Exec(`INSERT INTO expenses (amount, category, note, date) VALUES (?, ?, ?, ?)`,
		exp.Amount, exp.Category, exp.Note, exp.Date)
	if err != nil {
		http.Error(w, "Insert failed", http.StatusInternalServerError)
		return
	}

	id, _ := res.LastInsertId()
	exp.ID = int(id)

	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(exp)
}

// --- GET /expenses/{id}
func (h *ExpenseHandler) HandleGETExpenseByID(w http.ResponseWriter, r *http.Request) {
	id, err := parseID(chi.URLParam(r, "id"))
	if err != nil {
		http.Error(w, "Invalid ID", http.StatusBadRequest)
		return
	}

	var exp models.Expense
	err = h.DB.QueryRow(`SELECT id, amount, category, note, date FROM expenses WHERE id = ?`, id).
		Scan(&exp.ID, &exp.Amount, &exp.Category, &exp.Note, &exp.Date)

	if errors.Is(err, sql.ErrNoRows) {
		http.Error(w, "Expense not found", http.StatusNotFound)
		return
	} else if err != nil {
		http.Error(w, "Query error", http.StatusInternalServerError)
		return
	}

	json.NewEncoder(w).Encode(exp)
}

// --- PUT /expenses/{id}
func (h *ExpenseHandler) HandlePUTExpenseByID(w http.ResponseWriter, r *http.Request) {
	id, err := parseID(chi.URLParam(r, "id"))
	if err != nil {
		http.Error(w, "Invalid ID", http.StatusBadRequest)
		return
	}

	var exp models.Expense
	if err := json.NewDecoder(r.Body).Decode(&exp); err != nil {
		http.Error(w, "Invalid JSON body", http.StatusBadRequest)
		return
	}

	_, err = h.DB.Exec(`UPDATE expenses SET amount = ?, category = ?, note = ?, date = ? WHERE id = ?`,
		exp.Amount, exp.Category, exp.Note, exp.Date, id)
	if err != nil {
		http.Error(w, "Update failed", http.StatusInternalServerError)
		return
	}

	exp.ID = id
	json.NewEncoder(w).Encode(exp)
}

// --- DELETE /expenses/{id}
func (h *ExpenseHandler) HandleDELETEExpenseByID(w http.ResponseWriter, r *http.Request) {
	id, err := parseID(chi.URLParam(r, "id"))
	if err != nil {
		http.Error(w, "Invalid ID", http.StatusBadRequest)
		return
	}

	res, err := h.DB.Exec(`DELETE FROM expenses WHERE id = ?`, id)
	if err != nil {
		http.Error(w, "Delete failed", http.StatusInternalServerError)
		return
	}

	n, _ := res.RowsAffected()
	if n == 0 {
		http.Error(w, "Expense not found", http.StatusNotFound)
		return
	}

	w.WriteHeader(http.StatusNoContent)
}

// --- Utility: Parse string ID to int
func parseID(s string) (int, error) {
	return strconv.Atoi(s)
}
