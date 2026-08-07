package main
func opr(pages[]int,capacity[]){
	frames := make([]int, 0, capacity)
	pageFaults := 0
	header := fmt.Sprintf("%-16s |", "Reference String")
	for i := 1; i <= capacity; i++ {
		header += fmt.Sprintf(" Frame %d |", i)
	}
	header += " Action Taken"
	fmt.Println(header)
	fmt.Println(strings.Repeat("-", len(header)+25))
	for i, page := range pages {
		inFrames := false
		for _, f := range frames {
			if f == page {
				inFrames = true
				break
			}
		}var action string

		if inFrames {
			action = "Hit"
		} else {
			pageFaults++
			if len(frames) < capacity {
				frames = append(frames, page)
				action = fmt.Sprintf("Page %d Loaded", page)}
}


//opr stands for optimal page replacement//
func main(){
	referenceString := []int{7, 0, 1, 2, 0, 3, 0, 4, 2, 3}
	capacity :=3
	opr(referenceString,capacity)
}