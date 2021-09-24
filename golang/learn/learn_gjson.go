package main

import (
	"fmt"
	"sort"

	"github.com/tidwall/gjson"
)

const json = `{
	"name": {"first": "Tom", "last": "Anderson"},
	"age":37,
	"children": ["Sara","Alex","Jack"],
	"fav.movie": "Deer Hunter",
	"friends": [
	  {"first": "Dale", "last": "Murphy", "age": 44, "nets": ["ig", "fb", "tw"]},
	  {"first": "Roger", "last": "Craig", "age": 68, "nets": ["fb", "tw"]},
	  {"first": "Jane", "last": "Murphy", "age": 47, "nets": ["ig", "tw"]}
	]
  }`

func main() {
	value := gjson.Get(json, "friends.#(last==\"Murphy\")#|@reverse|0.first")
	println(value.String())
	var m = make(map[string]string)
	m["abc"] = "abc"
	fmt.Println(m["abc"])
	fmt.Println(len(m))
	delete(m, "abc")
	m["a"] = "a"
	a, ok := m["a"]
	fmt.Println(a, ok)
	_, ok1 := m["a"]
	fmt.Println(ok1)
	for k, v := range m {
		fmt.Println("k: ", k, "v: ", v)
	}
	for k, v := range m {
		fmt.Println(k, v)
	}
	var m1 = make(map[string]int)
	m1["abc"] = 1234
	delete(m1, "abc")
	k1, okm := m1["abc"]
	fmt.Println(k1, okm)
	m2 := map[string]int{
		"a": 1,
		"b": 2,
		"c": 3,
	}
	var keys []string
	for k := range m2 {
		keys = append(keys, k)
	}
	sort.Strings(keys)
	for idx, v := range keys {
		fmt.Println("idx", idx, "key", v, "value", m2[v])
	}
	fmt.Println(m2["a"])
	m3 := map[string]string{}
	fmt.Println(m3)
}
