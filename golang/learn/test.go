package main

import (
	"time"
	"fmt"
)

func main() {
	timeStr:=time.Now().Format("20060102150405")
	fmt.Printf(timeStr)
}