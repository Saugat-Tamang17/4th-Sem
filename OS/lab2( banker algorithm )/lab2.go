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

	// Input Available Vector
	fmt.Println("\nEnter the Available Resources:")
	for i := 0; i < m; i++ {
		fmt.Scan(&available[i])
	}

	// Calculate Need Matrix
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			need[i][j] = max[i][j] - allocation[i][j]
		}
	}

	// Print Need Matrix
	fmt.Println("\nNeed Matrix:")
	for i := 0; i < n; i++ {
		fmt.Printf("P%d: ", i)
		for j := 0; j < m; j++ {
			fmt.Printf("%d ", need[i][j])
		}
		fmt.Println()
	}

	work := make([]int, m)
	copy(work, available)
}
