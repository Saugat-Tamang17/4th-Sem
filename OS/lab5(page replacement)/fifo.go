package main

import (
	"fmt"
	"strings"
)

func fifo(pages []int, capacity int) int {
	frames := make([]int, 0, capacity)
	queue := make([]int, 0, capacity)
	pagefaults := 0

	//printing the headers ( top part ) //
	header := fmt.Sprintf("%-16s |", "Reference String")
	for i := 1; i <= capacity; i++ {
		header += fmt.Sprintf(" Frame %d |", i)
	}

	header += "action taken"
	fmt.Println(header)
	fmt.Println(strings.Repeat("-", len(header)+25))

	//checking if the page is alreadyy in memory

	for _, page := range pages {
		inFrames := false
		for _, f := range frames {
			if f == page { //meaning that it is already inside the memory
				inFrames = true
				break
			}
		}
		var action string
		if inFrames {
			action = "Hit"
		} else {
			pagefaults++
			//if there is still free memory space
			if len(frames) < capacity {
				frames = append(frames, page)
				queue = append(queue, page)
				action = fmt.Sprintf("Page %d Loaded", page)
			}
		}

	}
}
