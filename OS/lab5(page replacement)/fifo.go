package main

import "fmt"

func fifo(pages []int, capacity int) int {
	frames := make([]int, 0, capacity)
	queue := make([]int, 0, capacity)
	pagefaults := 0

	//printing the headers ( top part ) //
	header := fmt.Sprintf("%-16s |", "Reference String")
	for i := 1; i <= capacity; i++ {
		header += fmt.Sprintf(" Frame %d |", i)
	}
}
