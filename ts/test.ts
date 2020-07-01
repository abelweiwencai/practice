var message:string = "hello World"
console.log(message)

class Site {
    name():void {
        console.log("i am in name")
    }
}

var obj = new Site()
obj.name()

var userName = 'my name is abel'
var score1:number = 12
console.log("username", userName)
console.log("score1", score1)

if (score1 > 10) {
    console.log("you score is higher than 10 point")
}

var grade:string = 'A'
if (grade == "a") {
    console.log("is A")
} else if (grade == "B") {
    console.log("you are sB")
} else {
    console.log("what is your grade")
}
switch(grade) {
    case "A": {
        console.log("you are A")
    }
    case "B": {
        console.log("you are B")
    }
    case "C": {
        console.log("you grade is C")
    }
}
var strB:string = "B"
var typeAny:any = "i am any type"
switch(grade) {
    case "A": {
        console.log('i am A')
    }
    case strB: {
        console.log("i am ", strB)
    }
    default: {
        console.log('did not catch the case and i am default')
    }
}
 for (var i:number = 0; i < 10; i++) {
    console.log("i am in for loop", i)
 }

 var typeArray = [1,2,3,4,5,6]
 for (var val in typeArray) {
     console.log("i am in for in loop:", val )
 }

 function firstFunction():string {
     let res:string = "i am the res value"
     console.log(res)
     return res
 }

var typeArray:number[] = [1,2,3,4]
var typeArrayStr:string[] = ['1', '2']

interface IPerson {
    firstName:string,
    lastName:string,
    sayHi: () => string
}

var customer:IPerson = {
    firstName: 'Tom',
    lastName: 'Hanks',
    sayHi: ():string => { return "Hi there"}
}
console.log("custom 对象：")
console.log(customer.firstName)
console.log(customer.lastName)
console.log(customer.sayHi())


class Person {

}

class Car {
    engin:string
    constructor(engin:string) {
        this.engin = engin
    }
    disp():void {
        console.log("发动机为：" + this.engin)
    }
}

var car = new Car("五菱引擎")
car.disp()