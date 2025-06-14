package handlers

import (
	"basic-expense-tracker/store"
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

}

// /POST expenses
func (h *ExpenseHandler) HandlePOSTExpense(w http.ResponseWriter, r *http.Request) {

}
