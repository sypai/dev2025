package main

import (
	"log"
	"net/http"

	"basic-expense-tracker/handlers"
	"basic-expense-tracker/store"
)

// With what little I knew, I was thinking we'll
// create a global variable and that'll be used across the project

// var expenseDB store.ExpenseDB

// func init() {
// 	expenseDB := store.GetDB()
// 	// But how do my handlers use this
// }

// Instead we use what is called - Dependency Injection
// "we pass what is needed"
// Like passing the DB to our Handler

func main() {
	db := store.GetDB() // we have here is a pointer to our singleton instance of type ExpenseDB

	handle := handlers.ExpenseHandler{DB: db}
	http.HandleFunc("/", handle.HandleRoot)
	http.HandleFunc("/expenses", handle.HandleExpenses)

	port := ":8080"
	log.Printf("Server is running on http://localhost%s\n", port)
	err := http.ListenAndServe(port, nil)
	if err != nil {
		log.Fatal(err)
	}
}
