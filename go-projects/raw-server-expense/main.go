package main

import (
	"fmt"
	"log"
	"net/http"
)

// root handler
func rootHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "welcome! track you expenses!")
}

func main() {
	http.HandleFunc("/", rootHandler)

	port := ":8080"
	log.Printf("Server is running on http://localhost%s\n", port)
	err := http.ListenAndServe(port, nil)
	if err != nil {
		log.Fatal(err)
	}
}
