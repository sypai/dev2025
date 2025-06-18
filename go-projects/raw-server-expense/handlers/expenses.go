package handlers

import (
	"basic-expense-tracker/models"
	"database/sql"
	"encoding/json"
	"fmt"
	"net/http"
)

type ExpenseHandler struct {
	DB *sql.DB
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
