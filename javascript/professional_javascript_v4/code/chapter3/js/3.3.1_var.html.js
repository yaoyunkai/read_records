// 不初始化的情况下，变量会保存一个特殊值 undefined
var message;
var message = "hi";

// function test() {
//     var s2 = "hello";
// }
// test();
// console.log(s2);


function test2() {
    s3 = "nihao";
}

test2();
console.log(s3);

function foo() {
    console.log(age);
    var age = 23;
}

foo();

function foo1() {
    var age1;
    console.log(age1);
    age1 = 23;
    alert('hello');
}

foo1();
