package main

import (
	"log"
	"net/http"

	"basic-expense-tracker/handlers"
	"basic-expense-tracker/store"
)

func main() {
	// we have here is a pointer to our singleton instance of type ExpenseDB
	db := store.GetDB()
	handler := handlers.NewExpenseHandler(db)

	server := &http.Server{
		Addr:    ":8080",
		Handler: handler, // 👈 ExpenseHandler is now the full HTTP app
	}

	log.Println(" Server running at http://localhost:8080")
	log.Fatal(server.ListenAndServe())
}
