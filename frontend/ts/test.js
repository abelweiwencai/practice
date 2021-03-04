var hello = "hello world";
console.log(hello);
var Site = /** @class */ (function () {
    function Site() {
    }
    Site.prototype.name = function () {
        console.log("Roob");
    };
    return Site;
}());
var objSite = new Site();
objSite.name();
var Cat = /** @class */ (function () {
    function Cat() {
    }
    Cat.prototype.cute = function () {
        console.log('cute cat');
    };
    return Cat;
}());
var objCat = new Cat();
objCat.cute();
var objAny = new Site();
console.log({ objAny: objAny });
objAny.name();
objAny = new Cat();
console.log(objAny);
objAny.cute;
var varNum = 1;
var vatString = "i am a string";
var varBoolean = true;
var varArrayNum = [1];
var varArrayStr = ['123'];
var varArrayBoolean = [true, false];
// 使用泛型数组
var arrNum = [1];
var arrStr = ['a'];
var arrBoolean = [true, false, true];
var tup = [1, '1'];
var Color;
(function (Color) {
    Color[Color["Red"] = 0] = "Red";
    Color[Color["Blue"] = 1] = "Blue";
    Color[Color["Green"] = 2] = "Green";
})(Color || (Color = {}));
var c = Color.Red;
