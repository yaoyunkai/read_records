// name 会被提升
console.log(name); // undefined
var name = 'Matt';

// // age 不会被提升
// console.log(age); // ReferenceError：age 没有定义
// let age = 26;


for (var i = 0; i < 5; i ++) {
    setTimeout(() => console.log(i), 0);
}
