
/**
 * 属性和方法
 * 使用 class 定义类，使用 constructor 定义构造函数
 * 通过 new 生成新实例的时候，会自动调用构造函数
 */
class Animal {
    name: string;
    constructor(name) {
        this.name = name;
    }
    sayHi() {
        return `My name is ${this.name}`;
    }
}

let a = new Animal('Jack');
console.log(a.sayHi()); // My name is Jack


 /**
  * 类的继承
  * 使用 extends 关键字实现继承，子类中使用 super 关键字来调用父类的构造函数和方法
  */
 class Cat extends Animal {
    constructor(name) {
        super(name); // 调用父类的 constructor(name)
        console.log(this.name);
    }
    sayHi() {
        return 'Meow, ' + super.sayHi(); // 调用父类的 sayHi()
    }
}

let c = new Cat('Tom'); // Tom
console.log(c.sayHi()); // Meow, My name is Tom


/**
 * 存取器
 * 使用 getter 和 setter 可以改变属性的赋值和读取行为
 */
class Animal2 {
    constructor(name) {
        this.name = name;
    }
    get name() {
        return 'Jack';
    }
    set name(value) {
        console.log('setter: ' + value);
    }
}

let d = new Animal('Kitty'); // setter: Kitty
d.name = 'Tom'; // setter: Tom
console.log(d.name); // Jack



/**
 * 静态方法
 * 使用 static 修饰符修饰的方法称为静态方法，它们不需要实例化，而是直接通过类来调用
 */
class Animal3 {
    name: string;
    constructor(name){
        this.name = name;
    }
    static isAnimal(a) {
        return a instanceof Animal3;
    }
}

let e = new Animal3('Jack');
Animal3.isAnimal(e); // true
e.isAnimal(e); // TypeError: a.isAnimal is not a function


class Person {
    static myName: string;
    public age: number;
    protected gender: string;
    private color: string;
}

let man = new Person();
console.log(man.myName); // error
console.log(man.age);
console.log(man.gender); // error  属性“gender”受保护，只能在类“Person”及其子类中访问
console.log(man.color); // error 属性“color”为私有属性，只能在类“Person”中访问



/**
 * 抽象类
 * abstract 用于定义抽象类和其中的抽象方法
 * 抽象类是不允许被实例化的
 * 抽象类中的抽象方法必须被子类实现
 */

// 抽象类是不允许被实例化的
abstract class Animal44 {
    public name;
    public constructor(name) {
        this.name = name;
    }
    public abstract sayHi();
}

let a4 = new Animal('Jack');

// index.ts(9,11): error TS2511: Cannot create an instance of the abstract class 'Animal'.


// 抽象类中的抽象方法必须被子类实现
abstract class Animal5 {
    public name;
    public constructor(name) {
        this.name = name;
    }
    public abstract sayHi();
}

class Cat5 extends Animal {
    public eat() {
        console.log(`${this.name} is eating.`);
    }
}

let cat5 = new Cat5('Tom');

// index.ts(9,7): error TS2515: Non-abstract class 'Cat' does not implement inherited abstract member 'sayHi' from class 'Animal'.


// 正确的使用方法
abstract class Animal6 {
    public name;
    public constructor(name) {
        this.name = name;
    }
    public abstract sayHi();
}

class Cat6 extends Animal {
    public sayHi6() {
        console.log(`Meow, My name is ${this.name}`);
    }
}

let cat6 = new Cat6('Tom');


// 类的类型
class Animal7 {
    name: string;
    constructor(name: string) {
        this.name = name;
    }
    sayHi(): string {
      return `My name is ${this.name}`;
    }
}

let a7: Animal7 = new Animal7('Jack');
console.log(a7.sayHi()); // My name is Jack