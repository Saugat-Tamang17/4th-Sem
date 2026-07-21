package main

import "fmt"

func main() {
	var n, m int

	fmt.Print("Enter the number of processes: ")
	fmt.Scan(&n)

	fmt.Print("Enter the number of resource types: ")
	fmt.Scan(&m)

	// Allocate matrices
	allocation := make([][]int, n)
	max := make([][]int, n)
	need := make([][]int, n)
	available := make([]int, m)
}
