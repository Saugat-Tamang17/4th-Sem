package main

import (
	"fmt"
	"strings"
)

// Frame represents a memory frame in the Clock algorithm.
type Frame struct {
	Page     int
	UsageBit int
}

func clock(pages []int, capacity int) {
	frames := make([]Frame, 0, capacity)
	hand := 0
	pageFaults := 0

	// Build the dynamic header based on capacity
	header := fmt.Sprintf("%-16s |", "Reference String")
	for i := 0; i < capacity; i++ {
		header += fmt.Sprintf(" Frame %d |", i)
	}
	header += " Pointer | Action Taken"

	divider := strings.Repeat("-", len(header)+5)
	fmt.Println(header)
	fmt.Println(divider)

	// Process each page in the reference string
	for _, page := range pages {
		inFrames := false
		hitIndex := -1

		// Check if page is already loaded (Hit)
		for i, f := range frames {
			if f.Page == page {
				inFrames = true
				hitIndex = i
				break
			}
		}

		var action string

		if inFrames {
			// Page Hit: set usage bit to 1
			frames[hitIndex].UsageBit = 1
			action = "Hit"
		} else {
			// Page Fault
			pageFaults++

			if len(frames) < capacity {
				// Memory has free slots available
				frames = append(frames, Frame{Page: page, UsageBit: 1})
				action = fmt.Sprintf("Loaded page %d", page)
				hand = (hand + 1) % capacity
			} else {
				// Memory is full: run the Clock algorithm to find a victim
				for {
					if frames[hand].UsageBit == 1 {
						// Give second chance: clear usage bit and advance hand
						frames[hand].UsageBit = 0
						hand = (hand + 1) % capacity
					} else {
						// Found victim (UsageBit == 0)
						evicted := frames[hand].Page
						frames[hand] = Frame{Page: page, UsageBit: 1}
						action = fmt.Sprintf("Evicted %d -> Loaded %d", evicted, page)
						hand = (hand + 1) % capacity
						break
					}
				}
			}
		}

		// Print the formatted current state row
		row := fmt.Sprintf("%-16d |", page)
		for i := 0; i < capacity; i++ {
			if i < len(frames) {
				// Print frame content and its usage bit
				row += fmt.Sprintf(" %d(u=%d)   |", frames[i].Page, frames[i].UsageBit)
			} else {
				// Empty slot
				row += fmt.Sprintf(" %-7s |", "-")
			}
		}

		// Print clock hand position and the action taken
		row += fmt.Sprintf(" Hand: %d  | %s", hand, action)
		fmt.Println(row)
	}

	fmt.Println(divider)
	fmt.Printf("Total Page Faults: %d\n", pageFaults)
}

func main() {
	referenceString := []int{7, 0, 1, 2, 0, 3, 0, 4, 2, 3}
	capacity := 3
	clock(referenceString, capacity)
}
