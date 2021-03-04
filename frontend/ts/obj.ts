var objectName = {
    key1: "value1",
    key2: "value2",
    key3: function() {
        console.log("function body")
    },
    key4: ["content1", "content2"]
}


interface IPerson {
    id: number,
    name: string
    sayHi: () => string
}

let customer: IPerson = {
    id: 1,
    name: "cat",
    sayHi: () => "Hi, beauty!"
}



