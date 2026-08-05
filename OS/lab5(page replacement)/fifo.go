package main

import (
	"fmt"
	"strings"
)

func fifo(pages []int, capacity int) int {
	frames := make([]int, 0, capacity)
	queue := make([]int, 0, capacity)
	pagefaults := 0

	// printing the headers (top part)
	header := fmt.Sprintf("%-16s |", "Reference String")
	for i := 1; i <= capacity; i++ {
		header += fmt.Sprintf(" Frame %d |", i)
	}
	header += "action taken"
	fmt.Println(header)
	fmt.Println(strings.Repeat("-", len(header)+25))

	for _, page := range pages {
		inFrames := false
		for _, f := range frames {
			if f == page {
				inFrames = true
				break
			}
		}

		action := "Hit"
		if !inFrames {
			pagefaults++
			if len(frames) < capacity {
				frames = append(frames, page)
				queue = append(queue, page)
				action = fmt.Sprintf("Page %d Loaded", page)
			} else {
				evicted := queue[0]
				queue = queue[1:]

				for idx, f := range frames {
					if f == evicted {
						frames[idx] = page
						break
					}
				}
				queue = append(queue, page)
				action = fmt.Sprintf("Evicted %d-> Loaded %d", evicted, page)
			}
		}

		row := fmt.Sprintf("%-16d|", page)
		for i := 0; i < capacity; i++ {
			if i < len(frames) {
				row += fmt.Sprintf("%-7d |", frames[i])
			} else {
				row += fmt.Sprintf("%-7s |", "-")
			}
		}
		row += action
		fmt.Println(row)
		fmt.Println(strings.Repeat("-", len(header)+25))
		fmt.Printf("Total Page Faults: %d\n", pagefaults)
	}

	return pagefaults
}

func main() {
	referenceString := []int{7, 0, 1, 2, 0, 3, 0, 4, 2, 3}
	capacity := 3

	fifo(referenceString, capacity)
}
