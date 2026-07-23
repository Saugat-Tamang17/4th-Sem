package main

type FIFO struct {
	capacity int
	frames   []int        //holds the current state of frames
	pageMap  map[int]bool // fast lookup to check if the process are inside ther frames
}

func NewFIFO(capacity int) *FIFO {
	return &FIFO{
		capacity: capacity,
		frames:   make([]int, 0, capacity),
		pageMap:  make(map[int]bool),
	}
}

func (f *FIFO) Access(page int) bool {
	//this is the condition of the page hit //
	if f.pageMap[page] {
		return true
	}

	if len(f.frames) == f.capacity {
		victim := f.frames[0]
		f.frames = f.frames[1:]
		delete(f.pageMap, victim)
	}
}
