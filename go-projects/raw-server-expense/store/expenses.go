package store

import (
	"database/sql"
	"log"
	"sync"

	_ "modernc.org/sqlite" // registers driver
)

var (
	db   *sql.DB
	once sync.Once
)

// initDB initializes and returns a singleton instance of ExpenseDB

func initDB() *sql.DB {
	once.Do(func() {
		var err error
		db, err = sql.Open("sqlite", "/Users/sypai/Desktop/code/dev2025/go-projects/raw-server-expense/store/expenses.db")
		if err != nil {
			log.Fatalf("failed to open DB: %v", err)
		}

		createTable := `
		CREATE TABLE IF NOT EXISTS expenses (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			amount REAL,
			category TEXT,
			note TEXT,
			date TEXT
		);`

		if _, err := db.Exec(createTable); err != nil {
			log.Fatalf("failed to create table: %v", err)
		}
	})

	return db
}

// GetDB returns the singleton instance
func GetDB() *sql.DB {
	return initDB()
}
