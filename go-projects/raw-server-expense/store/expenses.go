package store

import (
	"basic-expense-tracker/models"
	"sync"
)

type ExpenseDB struct {
	Expenses []models.Expense
	NextID   int
}

var (
	db   *ExpenseDB
	once sync.Once
)

// initDB initializes and returns a singleton instance of ExpenseDB
func initDB() *ExpenseDB {
	once.Do(func() {
		db = &ExpenseDB{
			Expenses: []models.Expense{},
			NextID:   1,
		}
	})
	return db // return the memory address of the struct, aka a pointer to type ExpenseDB
}

// GetDB returns the singleton instance
func GetDB() *ExpenseDB {
	return initDB()
}
