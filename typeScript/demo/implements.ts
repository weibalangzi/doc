
/**
 * 实现（implements）是面向对象中的一个重要概念。
 * 一般来讲，一个类只能继承自另一个类，
 * 有时候不同类之间可以有一些共有的特性，
 * 这时候就可以把特性提取成接口（interfaces），
 * 用 implements 关键字来实现。
 * 这个特性大大提高了面向对象的灵活性
 */

interface Alarm {
    alert();
}

class Door {
}

class SecurityDoor extends Door implements Alarm {
    alert() {
        console.log('SecurityDoor alert');
    }
}

class Car implements Alarm {
    alert() {
        console.log('Car alert');
    }
}

// 还可以实现多个接口
// class Car implements Alarm, Light{}


// 接口继承接口
interface Alarm {
    alert();
}

interface LightableAlarm extends Alarm {
    lightOn();
    lightOff();
}


// 接口继承类
class Point {
    x: number;
    y: number;
}

interface Point3d extends Point {
    z: number;
}

let point3d: Point3d = {x: 1, y: 2, z: 3};