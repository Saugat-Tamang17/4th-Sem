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

	for i := 0; i < n; i++ {
		allocation[i] = make([]int, m)
		max[i] = make([]int, m)
		need[i] = make([]int, m)
	}

	// Input Allocation Matrix
	fmt.Println("\nEnter the Allocation Matrix:")
	for i := 0; i < n; i++ {
		fmt.Printf("P%d: ", i)
		for j := 0; j < m; j++ {
			fmt.Scan(&allocation[i][j])
		}
	}

	// Input Maximum resourcce needed Matrix
	fmt.Println("\nEnter the Maximum Matrix:")
	for i := 0; i < n; i++ {
		fmt.Printf("P%d: ", i)
		for j := 0; j < m; j++ {
			fmt.Scan(&max[i][j])
		}
	}
}
