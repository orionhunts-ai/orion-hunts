package main

import (
	"encoding/json"
	"fmt"
	"math/rand"
	"os"
	"time"
)

type CyberSecurityEntry struct {
	TransID      int      `json:"transID"`
	Timestamp    string   `json:"timestamp"`
	IP           string   `json:"ip"`
	APTID        string   `json:"APTID"`
	Fingerprints []string `json:"fingerprints"`
}

func main() {
	numEntries := 10 // Change this to 200 for your actual dataset
	entries := make([]CyberSecurityEntry, numEntries)
	rand.Seed(time.Now().UnixNano())

	for i := 0; i < numEntries; i++ {
		entries[i] = CyberSecurityEntry{
			TransID:      i + 1,
			Timestamp:    time.Now().Add(time.Duration(i) * time.Minute).Format(time.RFC3339),
			IP:           fmt.Sprintf("192.168.1.%d", rand.Intn(255)),
			APTID:        fmt.Sprintf("APT%d", rand.Intn(30)+1),
			Fingerprints: []string{fmt.Sprintf("fingerprint%d", rand.Intn(3)+1)},
		}
	}

	file, err := os.Create("cybersecurity_data.json")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	encoder := json.NewEncoder(file)
	err = encoder.Encode(entries)
	if err != nil {
		panic(err)
	}
}
