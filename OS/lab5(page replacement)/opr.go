package main

import (
	"fmt"
	"strings"
)

func opr(pages []int, capacity int) {
	frames := make([]int, 0, capacity)
	pageFaults := 0

	// Print Header
	header := fmt.Sprintf("%-16s |", "Reference String")
	for i := 1; i <= capacity; i++ {
		header += fmt.Sprintf(" Frame %d |", i)
	}
	header += " Action Taken"
	fmt.Println(header)
	fmt.Println(strings.Repeat("-", len(header)+25))

	// Process each page
	for i, page := range pages {
		inFrames := false
		for _, f := range frames {
			if f == page {
				inFrames = true
				break
			}
		}

		var action string

		if inFrames {
			action = "Hit"
		} else {
			pageFaults++
			if len(frames) < capacity {
				frames = append(frames, page)
				action = fmt.Sprintf("Page %d Loaded", page)
			} else {
				// Find the frame page that will NOT be used for the longest time in the future
				replaceIdx := -1
				farthestUse := -1

				for idx, f := range frames {
					nextUse := -1

					// Look ahead in the remaining reference string
					for j := i + 1; j < len(pages); j++ {
						if pages[j] == f {
							nextUse = j
							break
						}
					}

					// If a page is never referenced again, it is the best candidate to evict immediately
					if nextUse == -1 {
						replaceIdx = idx
						break
					}

					// Otherwise, select the page whose next reference is farthest in the future
					if nextUse > farthestUse {
						farthestUse = nextUse
						replaceIdx = idx
					}
				}

				evicted := frames[replaceIdx]
				frames[replaceIdx] = page
				action = fmt.Sprintf("Evicted %d -> Loaded %d", evicted, page)
			}
		}

		// Print frame contents and current action
		row := fmt.Sprintf("%-16d |", page)
		for k := 0; k < capacity; k++ {
			if k < len(frames) {
				row += fmt.Sprintf(" %-7d |", frames[k])
			} else {
				row += fmt.Sprintf(" %-7s |", "-") // Empty frame slot
			}
		}
		row += " " + action
		fmt.Println(row)
	}

	fmt.Println(strings.Repeat("-", len(header)+25))
	fmt.Printf("Total Page Faults: %d\n", pageFaults)
}

func main() {
	referenceString := []int{7, 0, 1, 2, 0, 3, 0, 4, 2, 3}
	capacity := 3

	opr(referenceString, capacity)
}
