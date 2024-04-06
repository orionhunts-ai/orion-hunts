package main

import (
	"fmt"
	"log"
	"net/http"
	"sync"
)

// analyzeEvent simulates the analysis of an event for malicious intent.
func analyzeEvent(eventData string) {
	// Placeholder for actual analysis logic
	fmt.Println("Analyzing event:", eventData)
	// Example: Check eventData against known heuristics or patterns
}

func eventHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != "POST" {
		http.Error(w, "Only POST method is allowed", http.StatusMethodNotAllowed)
		return
	}

	// Simulating reading the event data (e.g., from the request body)
	var eventData string
	if err := r.ParseForm(); err == nil {
		eventData = r.FormValue("data")
	}

	// Use a goroutine for concurrent processing of the event
	go analyzeEvent(eventData)

	fmt.Fprintf(w, "Event received and being analyzed")
}

func main() {
	http.HandleFunc("/event", eventHandler)

	port := "8080" // Default port for Cloud Run
	log.Printf("Listening on port %s", port)
	log.Fatal(http.ListenAndServe(fmt.Sprintf(":%s", port), nil))
}
