package main

import (
	"fmt"
	"strings"
)

func lru(pages []int, capacity int) {
	frames := make([]int, 0, capacity)
	LastUsed := make(map[int]int)
	pageFaults := 0

	header := fmt.Sprintf("%-16s |", "Reference String")
	for i := 0; i <= capacity; i++ {
		header += fmt.Sprintf("Frame %d |", i)
	}
	header += "action taken"
	fmt.Println(header)
	fmt.Println(strings.Repeat("-", len(header)+25))

	//processing the each page ( from reference string)//
	for timeStep, page := range pages {
		inFrames := false
		for _, f := range frames {
			if f == page {
				inFrames == true
				break
			}
		}
		var action string
		if inFrames {
			action = "hit"
		} else {

		}
	}
}

func main() {
	referenceString := []int{7, 0, 1, 2, 0, 3, 0, 4, 2, 3}
	capacity := 3
	lru(referenceString, capacity)
}
