package main

type FIFO struct {
	capacity int
	frames   []int        //holds the current state of frames
	pageMap  map[int]bool // fast lookup to check if the process are inside ther frames
}
