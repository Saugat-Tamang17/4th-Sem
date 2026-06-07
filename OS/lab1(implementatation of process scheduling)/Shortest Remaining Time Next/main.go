package main

import (
	"fmt"
	"sort"
)

type Process struct {
	ID             int
	ArrivalTime    int
	BurstTime      int
	RemainingTime  int // this is the crucial part of SRTN
	CompletionTime int
	TurnAroundTime int
	WaitingTime    int
}

func main() {
	var numProcess int
	fmt.Println("Enter the number of the Processes you will need:")
	_, err := fmt.Scanln(&numProcess)
	if err != nil || numProcess <= 0 {
		fmt.Println("Invalid input. Exiting.")
		return
	}

	processes := make([]Process, numProcess)
	for i := 0; i < numProcess; i++ {
		pid := i + 1
		processes[i].ID = pid
		fmt.Println("\n----Process P%d----\n", pid)
		fmt.Println("Enter the arrival time :")
		fmt.Scanln(&processes[i].ArrivalTime)
		fmt.Println("Enter the Burst time :")
		fmt.Scanln(&processes[i].BurstTime)

		//initially ,remaining time equals to the Burst Time
		processes[i].RemainingTime = processes[i].BurstTime
	}

	currentTime := 0
	completedCount := 0
	var totalTAT, totalWT float64

	for completedCount < numProcess {
		minIndex := -1
		minRemaining := 1e9
		for i := 0; i < numProcess; i++ {
			if processes[i].ArrivalTime <= currentTime && processes[i].RemainingTime > 0 {
				if float64(processes[i].RemainingTime) < minRemaining {
					minRemaining = float64(processes[i].RemainingTime)
					minIndex = i
				}
			}
			if minIndex == -1 {
				currentTime++
				continue
			}
			processes[i].RemainingTime--
		}

		if processes[minIndex].RemainingTime == 0 {
			completedCount++
			idx := minIndex
			processes[idx].CompletionTime = currentTime + 1 //
			processes[idx].TurnAroundTime = processes[idx].CompletionTime - processes[idx].ArrivalTime
			processes[idx].WaitingTime = processes[idx].TurnAroundTime - processes[idx].BurstTime

			totalTAT += float64(processes[idx].TurnAroundTime)
			totalWT += float64(processes[idx].WaitingTime)

		}
		currentTime++
	}
	sort.Slice(processes, func(i, j int) bool {
		return processes[i].ID < processes[j].ID
	})
	// 5. Output the results table
	fmt.Println("\nPID\tArrival\tBurst\tComplete\tTurnaround\tWaiting")
	fmt.Println("-----------------------------------------------------------------")
	for _, p := range processes {
		fmt.Printf("P%d\t%d\t%d\t%d\t\t%d\t\t%d\n",
			p.ID, p.ArrivalTime, p.BurstTime, p.CompletionTime, p.TurnAroundTime, p.WaitingTime)
	}

	n := float64(numProcess)
	fmt.Printf("\nAverage Turnaround Time: %.2f\n", totalTAT/n)
	fmt.Printf("Average Waiting Time: %.2f\n", totalWT/n)
}
