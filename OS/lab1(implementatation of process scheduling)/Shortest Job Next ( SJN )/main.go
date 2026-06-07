package main

import (
	"fmt"
	"sort"
)

type Process struct {
	ID             int
	ArrivalTime    int
	BurstTime      int
	CompletionTime int
	TurnAroundTime int
	WaitingTime    int
	IsCompleted    bool
}

func GetCredentials(numProcess int) []Process {
	processes := make([]Process, numProcess)
	for i := 0; i < numProcess; i++ {
		pid := i + 1
		processes[i].ID = pid
		fmt.Printf("\n--- Process P%d ---\n", pid)
		fmt.Print("Enter Arrival Time: ")
		fmt.Scanln(&processes[i].ArrivalTime)

		fmt.Print("Enter Burst Time: ")
		fmt.Scanln(&processes[i].BurstTime)
	}
	return processes
}

func main() {
	var numProcess int
	fmt.Println("Enter the number of the processes you will need :")
	_, err := fmt.Scanln(&numProcess)
	if err != nil || numProcess <= 0 {
		fmt.Println("Invalid Input . +ve number as the input is required.\n")
		return
	}
	processes := GetCredentials(numProcess)

	CurrentTime := 0
	CompletedCount := 0
	var totalWT, totalTAT float64

	for CompletedCount < numProcess {
		minIndex := -1  // first jpb
		minBurst := 1e9 // setting to hightest so that replacing will be easier
		for i := 0; i < numProcess; i++ {
			if processes[i].ArrivalTime <= CurrentTime && !processes[i].IsCompleted {
				if processes[i].BurstTime < int(minBurst) {
					minBurst = float64(processes[i].BurstTime)
					minIndex = i
				}
			}
		}

		//when no processes arrive and cpu is in the idle condition
		if minIndex == -1 {
			CurrentTime++
			continue
		}
		idx := minIndex
		processes[idx].CompletionTime = CurrentTime + processes[idx].BurstTime
		processes[idx].TurnAroundTime = processes[idx].CompletionTime - processes[idx].ArrivalTime
		processes[idx].WaitingTime = processes[idx].TurnAroundTime - processes[idx].BurstTime
		processes[idx].IsCompleted = true
		totalTAT += float64(processes[idx].TurnAroundTime)
		totalWT += float64(processes[idx].WaitingTime)

		// Advance currentTime to when this process finishes
		CurrentTime = processes[idx].CompletionTime
		CompletedCount++
	}
	sort.Slice(processes, func(i, j int) bool {
		return processes[i].ID < processes[j].ID
	})

	// 5. Output the results
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
