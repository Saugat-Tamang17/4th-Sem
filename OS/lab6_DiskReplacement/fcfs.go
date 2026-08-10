package main

import (
	"fmt"
	"strings"
)

func FCFSdisk(queue []int, head int) {
	totalHeadMovement := 0
	currentHead := head

	header := fmt.Sprintf("%-12s | %-12s | %-20s | %-18s", "From Track", "To Track", "Movement Calculation", "Head Movement")
	divider := strings.Repeat("-", len(header))
}

func main() {
	queue := []int{176, 79, 34, 60, 92, 11, 41, 114}
	initialHead := 50
	FCFSdisk(queue, initialHead)
}
