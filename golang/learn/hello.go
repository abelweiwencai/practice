/*
这是一个多行注释
我的连接文件
*/

// this is a single line comment

package main
import (
	"fmt"
	// "math"
	// "math/rand"
)

var i, j, k int = 1, 2, 3
func add(x, y int) int {
	return x + y
}

func swap(x, y string) (string, string) {
	return y, x
}

func test_for() (x int ,y int) {
	x = 10
	y = 20
	return
}

func main() {
	// fmt.Println("hello, world!")

	// var myName string = "weiwencia"

	// fmt.Println("my name is :" + myName)

	// var myAge, myWeight int = 30, 100
	// fmt.Println(myAge, myWeight)
	// fmt.Println(math.Pi)

	// fmt.Println(add(1, 3))
	// fmt.Println(swap("pre", "behind"))
	// sum := 1
	// for ; sum < 1000; {
	// 	sum += sum
	// 	fmt.Println(sum)
	// 	fmt.Println("随机数", rand.Intn(10))
	// }
	// a, b := test_for()
	// fmt.Println(a, b, math.Pi, rand.Intn(8))
	var c, python, java = true, false, "no!"
	l := 12
	fmt.Println(i, j, k, c, python, java, l)
}
