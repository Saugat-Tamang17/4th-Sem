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

	// Input Maximum resource needed Matrix
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

	finish := make([]bool, n)
	safeSequence := []int{}SZ
	count := 0

	for count < n {
		found := false

		for i := 0; i < n; i++ {
			if finish[i] {
				continue
			}

			canExecute := true
			for j := 0; j < m; j++ {
				if need[i][j] > work[j] {
					canExecute = false
					break
				}
			}

			if canExecute {
				fmt.Printf("\nP%d executes.", i)

				for j := 0; j < m; j++ {
					work[j] += allocation[i][j]
				}

				fmt.Print("\nAvailable Resources: ")
				for j := 0; j < m; j++ {
					fmt.Printf("%d ", work[j])
				}
				fmt.Println()

				safeSequence = append(safeSequence, i)
				finish[i] = true
				count++
				found = true
			}
		}

		if !found {
			break
		}
	}

	if count == n {
		fmt.Println("\nSystem is in a SAFE state.")
		fmt.Print("Safe Sequence: ")

		for i := 0; i < len(safeSequence); i++ {
			if i == len(safeSequence)-1 {
				fmt.Printf("P%d\n", safeSequence[i])
			} else {
				fmt.Printf("P%d -> ", safeSequence[i])
			}
		}
	} else {
		fmt.Println("\nSystem is NOT in a SAFE state.")
	}
}
