import shape = require("./IShape")

export class Triangle implements shape.IShape {
    public draw() {
        console.log("i am drawing triangle")
    }
}