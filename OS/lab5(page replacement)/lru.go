package main

func lru(pages []int, capacity int) {
	frames := make([]int, 0, capacity)
	LastUsed := make(map[int]int)
	pageFaults := 0
}

func main() {
	referenceString := []int{7, 0, 1, 2, 0, 3, 0, 4, 2, 3}
	capacity := 3
	lru(referenceString, capacity)
}
