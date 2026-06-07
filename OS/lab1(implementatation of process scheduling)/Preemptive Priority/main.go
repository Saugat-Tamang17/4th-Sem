package main

import (
	"fmt"
	"sort"
)

type Process struct {
	ID             int
	ArrivalTime    int
	BurstTime      int
	RemainingTime  int
	Priority       int // Lower integer means higher priority
	CompletionTime int
	TurnaroundTime int
	WaitingTime    int
}

func main() {
	var numProcesses int

	// 1. Collect Input from User
	fmt.Print("Enter the total number of processes: ")
	_, err := fmt.Scanln(&numProcesses)
	if err != nil || numProcesses <= 0 {
		fmt.Println("Invalid input. Exiting.")
		return
	}

	processes := make([]Process, numProcesses)

	for i := 0; i < numProcesses; i++ {
		pid := i + 1
		processes[i].ID = pid
		fmt.Printf("\n--- Process P%d ---\n", pid)
		fmt.Print("Enter Arrival Time: ")
		fmt.Scanln(&processes[i].ArrivalTime)
		fmt.Print("Enter Burst Time: ")
		fmt.Scanln(&processes[i].BurstTime)
		fmt.Print("Enter Priority (Lower number = Higher Priority): ")
		fmt.Scanln(&processes[i].Priority)

		// Initialize remaining time to match the initial burst time
		processes[i].RemainingTime = processes[i].BurstTime
	}

	currentTime := 0
	completedCount := 0
	var totalTAT, totalWT float64

	// 2. Main Preemptive Priority Simulation Loop
	for completedCount < numProcesses {
		highestPriorityIdx := -1
		highestPriorityVal := int(1e9) // Using a large number since smaller integer = higher priority

		// Scan for the arrived process with the highest priority (lowest integer value)
		for i := 0; i < numProcesses; i++ {
			if processes[i].ArrivalTime <= currentTime && processes[i].RemainingTime > 0 {
				if processes[i].Priority < highestPriorityVal {
					highestPriorityVal = processes[i].Priority
					highestPriorityIdx = i
				}
			}
		}

		// CPU Idle check: if no process has arrived yet, advance the clock cleanly
		if highestPriorityIdx == -1 {
			currentTime++
			continue
		}

		// --- EXECUTION WINDOW ---
		// The chosen process takes exactly 1 unit of CPU time right now
		processes[highestPriorityIdx].RemainingTime--
		currentTime++ // The global timeline moves forward immediately by that 1 unit

		// Check if the process finished *after* that time unit passed
		if processes[highestPriorityIdx].RemainingTime == 0 {
			completedCount++

			idx := highestPriorityIdx
			// Since currentTime already jumped forward by 1, it naturally reflects the true completion point
			processes[idx].CompletionTime = currentTime
			processes[idx].TurnaroundTime = processes[idx].CompletionTime - processes[idx].ArrivalTime
			processes[idx].WaitingTime = processes[idx].TurnaroundTime - processes[idx].BurstTime

			totalTAT += float64(processes[idx].TurnaroundTime)
			totalWT += float64(processes[idx].WaitingTime)
		}
	}

	// 3. Sort back by ID for structured output printing
	sort.Slice(processes, func(i, j int) bool {
		return processes[i].ID < processes[j].ID
	})

	// 4. Print Results Table
	fmt.Println("\nPID\tArrival\tBurst\tPriority\tComplete\tTurnaround\tWaiting")
	fmt.Println("-------------------------------------------------------------------------")
	for _, p := range processes {
		fmt.Printf("P%d\t%d\t%d\t%d\t\t%d\t\t%d\t\t%d\n",
			p.ID, p.ArrivalTime, p.BurstTime, p.Priority, p.CompletionTime, p.TurnaroundTime, p.WaitingTime)
	}

	// 5. Display Averages
	n := float64(numProcesses)
	fmt.Printf("\nAverage Turnaround Time: %.2f\n", totalTAT/n)
	fmt.Printf("Average Waiting Time: %.2f\n", totalWT/n)
}
