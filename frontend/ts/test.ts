const hello: string = "hello world"
console.log(hello)

class Site{
    name():void {
        console.log("Roob")
    }
}

const objSite = new Site()
objSite.name()


class Cat{
    cute(): void {
        console.log('cute cat')
    }
}
const objCat = new Cat()
objCat.cute()

let objAny: any = new Site()
console.log({objAny})
objAny.name()
objAny = new Cat()
console.log(objAny)
objAny.cute

const varNum: number = 1
const vatString: string = "i am a string"
const varBoolean: boolean = true
const varArrayNum: number[] = [1]
const varArrayStr: string[] = ['123']
const varArrayBoolean: boolean[] = [true, false]
// 使用泛型数组
const arrNum: Array<number> = [1]
const arrStr: Array<string> = ['a']
const arrBoolean: Array<boolean> = [true, false, true]

const tup: [number, string] = [1, '1']

enum Color { Red, Blue, Green }
let c: Color = Color.Red


let uname: string = 'weiwencai'
let varName: number
let varNameAny

function greet(hello: string):string {
    return hello
}

console.log(greet('hello world'))