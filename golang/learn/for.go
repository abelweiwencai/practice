package main

import "fmt"

func main() {
	sum := 0
	for i := 0; i < 10; i++ {
		sum += i
	}
	fmt.Println(sum)

	s := 0
	for i := 0; i < 10 ; i ++ {
		s += i
		fmt.Println(s)
	}
}
// semicolons 分号