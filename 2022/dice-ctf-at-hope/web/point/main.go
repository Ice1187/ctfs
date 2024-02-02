package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"strings"
)

type importantStuff struct {
	Whatpoint string `json:"what_point"`
}

func main() {
	flag, err := os.ReadFile("flag.txt")
	if err != nil {
		panic(err)
	}

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		switch r.Method {
		case http.MethodGet:
			fmt.Fprint(w, "Hello, world")
			return
		case http.MethodPost:
			body, err := io.ReadAll(r.Body)
			if err != nil {
				fmt.Fprintf(w, "Post went wrong")
				return
			}

			if strings.Contains(string(body), "what_point") || strings.Contains(string(body), "\\") {
				fmt.Fprintf(w, "Filter")
				return
			}

			var whatpoint importantStuff
			fmt.Fprintf(w, "Body: %s\n", body)
			err = json.Unmarshal(body, &whatpoint)
			if err != nil {
				fmt.Fprintf(w, "Unmarshal went wrong")
				return
			}
			fmt.Fprintf(w, "input: %v\n", whatpoint.Whatpoint)

			if whatpoint.Whatpoint == "that_point" {
				fmt.Fprintf(w, "Congrats! Here is the flag: %s", flag)
				return
			} else {
				fmt.Fprintf(w, "Not correct\n")
				return
			}
		default:
			fmt.Fprint(w, "Method not allowed")
			return
		}
	})

	log.Fatal(http.ListenAndServe(":8081", nil))

}
