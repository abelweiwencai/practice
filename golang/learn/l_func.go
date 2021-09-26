package main

import (
	"errors"
	"fmt"
)

type Person struct {
	Name string
	Age  int
}

func Func1(i interface{}) int {
	return 1
}

func Func2(i interface{}) interface{} {
	return i
}

func main() {

	p := Person{
		Name: "name",
		Age:  18,
	}
	r1 := Func1(p)

	fmt.Printf("%#v\n", r1)

	var r2 Person

	r2 = Func2(p).(Person)
	fmt.Printf("%#v", r2)

	err := errors.New("fuxx")
	fmt.Printf("err: %v\n", err)
	// mm := fmt.Sprintf("%s", err)
	mm1 := err.Error()
	fmt.Printf("mm1 = %v\n", mm1)

}
