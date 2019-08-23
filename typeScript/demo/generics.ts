
/**
 * 泛型
 * 泛型（Generics）是指在定义函数、接口或类的时候，不预先指定具体的类型，而在使用的时候再指定类型的一种特性
 */

// example 输入类型和返回类型都是不确定的，这是一个缺陷
function test1(a: any, b: any): any {
    console.log(typeof a)
    console.log(typeof b)
}

// 使用泛型，在入参的时候确定类型
// 我也不知道我要什么，当那个东西出现的时候，我就知道我要什么了
function test2<T, S>(a: T, b: S): T {
    return a
}

/**约束泛型 */
interface IProps {
    length: number;
}

// 很显然，鬼知道a是个什么东西，鬼知道它有没有length
function test3<T>(a: T): Number {
    return a.length
}

// 如此，做一个约束，a必须是有长度length的东西;
function test4<T extends IProps>(a: T): number {
    return a.length
}


/**泛型接口 */
interface TProps<T> {
    age: T;
}

// 可以使用接口的方式来定义一个函数需要符合的形状
function test5(age: TProps<any>): TProps<any> {
    return age
}



/**泛型类 */
class GenericNumber<T> {
    zeroValue: T;
    add: (x: T, y: T) => T;
}

let myGenericNumber = new GenericNumber<number>();
myGenericNumber.zeroValue = 0;
myGenericNumber.add = function(x, y) { return x + y; };



/**泛型参数的默认类型 */
function createArray<T = string>(length: number, value: T): Array<T> {
    let result: T[] = [];
    for (let i = 0; i < length; i++) {
        result[i] = value;
    }
    return result;
}
