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
				inFrames = true
				break
			}
		}
		var action string
		if inFrames {
			action = "hit"
		} else {
			pageFaults++
			if len(frames) < capacity {
				frames = append(frames, page)
				action = fmt.Sprintf("page %dLoaded", page)
			} else {
				lruIndex := 0
				minTime := LastUsed[frames[0]] //starting with first frame's timestamppp
				for i := 1; i < len(frames); i++ {
					f := frames[i]
					if LastUsed[f] < minTime {
						minTime = LastUsed[f]
						lruIndex = i
					}
				}
				evicted := frames[lruIndex]
				frames[lruIndex] = page
				action = fmt.Sprintf("Evicted %d -> Loaded %d", evicted, page)
			}
		}
		LastUsed[page] = timeStep
		row := fmt.Sprintf("%-16d |", page)
		for i := 0; i < capacity; i++ {
			if i < len(frames) {
				row += fmt.Sprintf(" %-7d |", frames[i])
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
	lru(referenceString, capacity)
}
