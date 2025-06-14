# 💸 Basic Expense Tracker API (in Go)

A simple in-memory REST API to **track your expenses** — built with pure Go.  
Perfect for learning how to build web servers, route handlers, and manage data using structs and pointers.

---

## 🚀 Features

- `GET /expenses` → List all expenses
- `POST /expenses` → Add a new expense
- In-memory store using slices and pointers
- Clean, idiomatic Go codebase

---

# 🔧 How to Run

```bash
go run main.go
```

Server will be available at:
📍 http://localhost:8080

### 🧪 Sample Requests

##### ➕ POST /expenses

```bash
curl -X POST http://localhost:8080/expenses \
 -H "Content-Type: application/json" \
 -d '{
"amount": 250.75,
"category": "Food",
"note": "Lunch with friends",
"date": "2025-06-12"
}'
```

##### 📄 GET /expenses

```bash
curl http://localhost:8080/expenses
```

---

🧠 Built With
Go (net/http, encoding/json)

---

📘 Learning Goals
This project is for you if you want to:

- Learn how to build an API server in Go

- Understand how pointers work across handlers

- Practice writing and structuring Go code cleanly
