class Animal {
    name = 'animal'

    constructor(name) {
        this.speed = 0;
        this.name = name;
    }

    run(speed) {
        this.speed = speed;
        console.log(`${this.name} runs with speed ${this.speed}.`);
    }

    stop() {
        this.speed = 0;
        console.log(`${this.name} stands still.`);
    }
}


// 继承类的 constructor 必须调用 super(...)，并且 (!) 一定要在使用 this 之前调用。
// 类字段和类方法 初始化的顺序
class Rabbit extends Animal {
    name = 'rabbit'

    constructor(name, earLength) {
        super(name);
        this.earLength = earLength;
    }

    hide() {
        console.log(`${this.name} hides!`);
    }

    stop() {
        super.stop(); // 调用父类的 stop
        this.hide(); // 然后 hide
    }

}
