package main

import (
	"fmt"  //for the formatting purpose
	"sort" // for sorting the process by arrival time //
)

type Process struct {
	ID             int
	ArrivalTime    int
	BurstTime      int
	CompletionTime int
	WaitingTime    int
	TurnAroundTime int
}

func main() {
	var numProcess int
	fmt.Println("Enter the Number of the processes you need:\n")
	_, err := fmt.Scanln(&numProcess)
	if err != nil {
		fmt.Println("\nInvalid input. Enter the +ve number")
		return
	}

	processes := make([]Process, numProcess) //makes a slice for required no. of process

	for i := 0; i < numProcess; i++ {
		pid := i + 1
		processes[i].ID = pid //assign the process with respective id

		fmt.Printf("\n--- Process P%d ---\n", pid)

		fmt.Print("Enter the Arrival time : ")
		fmt.Scanln(&processes[i].ArrivalTime)

		fmt.Print("Enter the Burst time : ")
		fmt.Scanln(&processes[i].BurstTime)
	}

	//sorting according to the arrival time //
	sort.Slice(processes, func(i, j int) bool {
		return processes[i].ArrivalTime < processes[j].ArrivalTime
	})

	currentTime := 0
	var totalTAT, totalWT float64
	for i := 0; i < numProcess; i++ {
		if currentTime < processes[i].ArrivalTime {
			currentTime = processes[i].ArrivalTime
		}

		processes[i].CompletionTime = currentTime + processes[i].BurstTime

		processes[i].TurnAroundTime = processes[i].CompletionTime - processes[i].ArrivalTime

		processes[i].WaitingTime = processes[i].TurnAroundTime - processes[i].BurstTime

		totalTAT += float64(processes[i].TurnAroundTime)
		totalWT += float64(processes[i].WaitingTime)

		currentTime = processes[i].CompletionTime

	}

	fmt.Println("\nPID\tArrival\tBurst\tComplete\tTurnaround\tWaiting")
	fmt.Println("-----------------------------------------------------------------")
	for _, p := range processes {
		fmt.Printf("P%d\t%d\t%d\t%d\t\t%d\t\t%d\n",
			p.ID, p.ArrivalTime, p.BurstTime, p.CompletionTime, p.TurnAroundTime, p.WaitingTime)
	}
	n := float64(numProcess)
	fmt.Println("\nAverage Waiting Time :", totalWT/n)
	fmt.Println("\nAverage Turn Around Time :", totalTAT/n)

}
