package main

import (
	"fmt"
	"testpac"
	"time"
)

func main() {
	timeStr := time.Now().Format("20060102150405")
	fmt.Printf(timeStr)
	testpac.PprintTest2()
}
