package main

import "fmt"

func lru(pages []int, capacity int) {
	frames := make([]int, 0, capacity)
	LastUsed := make(map[int]int)
	pageFaults := 0

	header := fmt.Sprintf("%-16s |", "Reference String")
	for i := 0; i <= capacity; i++ {
		header += fmt.Sprintf("Frame %d |", i)
	}
	header += "action taken"
}

func main() {
	referenceString := []int{7, 0, 1, 2, 0, 3, 0, 4, 2, 3}
	capacity := 3
	lru(referenceString, capacity)
}
