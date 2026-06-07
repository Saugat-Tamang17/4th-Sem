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
	CompletionTime int
	TurnAroundTime int
	WaitingTime    int
	InQueue        bool
}

func main() {
	var numProcess, quantum int
	fmt.Println("Enter the total number of the processes:")
	fmt.Scanln(&numProcess)
	processes := make([]Process, numProcess)

	for i := 0; i < numProcess; i++ {
		pid := i + 1
		processes[i].ID = pid
		fmt.Printf("\n--- Process P%d ---\n", pid)
		fmt.Println("Enter the Arrival Time :")
		fmt.Scanln(&processes[i].ArrivalTime)
		fmt.Println("Enter the Burst Time:")
		fmt.Scanln(&processes[i].BurstTime)
		processes[i].RemainingTime = processes[i].BurstTime
	}

	fmt.Println("\nEnter the Time Quantum :")
	fmt.Scanln(&quantum)

	sort.Slice(processes, func(i, j int) bool {
		return processes[i].ArrivalTime < processes[j].ArrivalTime
	})

	var readyQueue []int
	currentTime := 0
	completedCount := 0
	var totalTAT, totalWT float64

	for i := 0; i < numProcess; i++ {
		if processes[i].ArrivalTime == currentTime {
			readyQueue = append(readyQueue, i)
			processes[i].InQueue = true
		}
	}

	for completedCount < numProcess {
		if len(readyQueue) == 0 {
			currentTime++
			for i := 0; i < numProcess; i++ {
				if processes[i].ArrivalTime <= currentTime && processes[i].RemainingTime > 0 && !processes[i].InQueue {
					readyQueue = append(readyQueue, i)
					processes[i].InQueue = true
				}
			}
			continue
		}

		idx := readyQueue[0]
		readyQueue = readyQueue[1:]

		executionTime := quantum
		if processes[idx].RemainingTime < executionTime {
			executionTime = processes[idx].RemainingTime
		}

		currentTime += executionTime
		processes[idx].RemainingTime -= executionTime

		for i := 0; i < numProcess; i++ {
			if processes[i].ArrivalTime <= currentTime && processes[i].RemainingTime > 0 && !processes[i].InQueue {
				readyQueue = append(readyQueue, i)
				processes[i].InQueue = true
			}
		}

		if processes[idx].RemainingTime > 0 {
			readyQueue = append(readyQueue, idx)
		} else {
			completedCount++
			processes[idx].CompletionTime = currentTime
			processes[idx].TurnAroundTime = processes[idx].CompletionTime - processes[idx].ArrivalTime
			processes[idx].WaitingTime = processes[idx].TurnAroundTime - processes[idx].BurstTime

			totalTAT += float64(processes[idx].TurnAroundTime)
			totalWT += float64(processes[idx].WaitingTime)
		}
	}

	sort.Slice(processes, func(i, j int) bool {
		return processes[i].ID < processes[j].ID
	})

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
