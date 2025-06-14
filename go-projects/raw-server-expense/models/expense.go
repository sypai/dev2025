package models

type Expense struct {
	ID       int     `json:"id"`
	Amount   float64 `json:"amount"`
	Category string  `json:"category"`
	Note     string  `json:"note"`
	Date     string  `json:"date"` // keep it string for now
}
