package main

import (
	"fmt"
	"time"

	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/mysql"
)

type UserInfo struct {
	Id     uint
	Name   string
	Gender string
	Hobby  string
}

type Like struct {
	ID        int    `gorm: "primary_key"`
	Ip        string `gorm: "type:varchar(20);not null;index:ip_idx"`
	Ua        string `gorm: "type: varchar(20);not null;"`
	Title     string `grom: "type: varchar(512);not null;"`
	Hash      string `gorm: "type: varchar(128);not null;"`
	CreatedAt time.Time
}

func start() {
	db, err := gorm.Open("mysql", "abel:root@(127.0.0.1:3306)/learn?charset=utf8mb4&parseTime=True&loc=Local")
	if err != nil {
		panic(err)
	}
	defer db.Close()

	db.AutoMigrate(&UserInfo{})

	// u1 := UserInfo{1, "枯藤", "男", "篮球"}
	// u2 := UserInfo{2, "abel", "lady", "ping"}

	// 增 怎么批量新增
	// db.Create(u1)
	// db.Create(u2)

	// 查
	var u = UserInfo{}
	db.First(&u) // 查第一个？查列表怎么查?
	fmt.Printf("%#v\n", u)

	var uu = new(UserInfo)
	db.Find(&uu, "hobby=?", "ping") // 查列表
	fmt.Printf("%#v\n", uu)

	db.Close()
	fmt.Println("fux")
	return
}

func tryModel() {
	db, err := gorm.Open("mysql", "abel:123456@(127.0.0.1:3306)/learn?charset=utf8mb4&parseTime=True&loc=Local")
	if err != nil {
		panic(err)
	}
	defer db.Close()

	if !db.HasTable(&Like{}) {
		if err := db.CreateTable(&Like{}).Error; err != nil {
			panic(err)
		}
	}
	var l = Like{
		ID:        4,
		Ip:        "qwe",
		Ua:        "asdf",
		Title:     "i am title",
		Hash:      "asdfasdfa",
		CreatedAt: time.Now(),
	}
	var cnt int

	if err := db.Model(&Like{}).Where(&Like{ID: l.ID}).Count(&cnt).Error; err != nil {
		panic(err)
	}
	if cnt == 0 {
		if err := db.Create(&l).Error; err != nil {
			fmt.Println("插入失败")
			panic(err)
		}
		fmt.Println("插入数据成功")
	} else {
		fmt.Println("数据已经存在，不需要插入")
	}
	if err := db.Model(&Like{}).Where(&Like{ID: 1}).Update(&Like{Ip: "127.0.0.1"}).Error; err != nil {
		panic(err)
	}
	fmt.Println("跟新成功")

	var likes []Like
	if err := db.Find(&likes).Error; err != nil {
		fmt.Println("查询出错")
		panic(err)
	}
	fmt.Printf("%#v", likes)

}

func testPanic() {
	fmt.Println("start test panic")
	defer func() {
		fmt.Println("i am doing defer function ")
		if err := recover(); err != nil {
			fmt.Printf("get err msg: %#v", err)
		} else {
			fmt.Println("正常结束函数，执行defer\n")

		}
	}()
	fmt.Println("going to panic ")
	// panic(" fxx K panic ")

	fmt.Println("after panic ")
}

func testPanic2() {
	defer func() {
		fmt.Println("aaaaaa")
	}()
	fmt.Println("bbbbbb")
	fmt.Println("cccccc")
	// panic("hahahaha")
	fmt.Println("ddddd")
	defer func() {
		fmt.Println("eeeeeeee")
	}()
}
func main() {
	// start()
	// tryModel()
	testPanic()
	testPanic2()
}
