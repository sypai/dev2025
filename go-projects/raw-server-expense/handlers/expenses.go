package handlers

import (
	"basic-expense-tracker/models"
	"basic-expense-tracker/store"
	"encoding/json"
	"fmt"
	"net/http"
)

type ExpenseHandler struct {
	DB *store.ExpenseDB
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
	w.Header().Set("Content-Type", "application/json")

	err := json.NewEncoder(w).Encode(h.DB.Expenses)
	if err != nil {
		http.Error(w, "Failed to encode expenses", http.StatusInternalServerError)
		return
	}
}

// /POST expenses
func (h *ExpenseHandler) HandlePOSTExpense(w http.ResponseWriter, r *http.Request) {
	var expense models.Expense

	// Decode JSON request body into Expense struct
	err := json.NewDecoder(r.Body).Decode(&expense)
	if err != nil {
		http.Error(w, "Invalid request body", http.StatusBadRequest)
		return
	}

	// Assign a new ID and append to DB
	expense.ID = h.DB.NextID
	h.DB.NextID++
	h.DB.Expenses = append(h.DB.Expenses, expense)

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(expense)
}
