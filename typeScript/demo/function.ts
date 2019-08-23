

/**函数的类型 */

// 声明式
// error
function test(name: string, age: number): string {
    return name + age;
}

// 表达式
const test1: (name: string, age: number) => string = function(name: string, age: number): string {
    return name + age;
}

// 使用接口
interface IFunc {
    (name: string, age: number): string;
}

// error
const test2: IFunc = function(name: string, age: number): string{
    return name + age
}

// 函数的可选参数
const test4: (name: string, age: number, gender?: string) => string = function(name: string, age: number, gender?: string): string{
    return name + age;
}

// 可选参数后面不允许再出现必须参数了
// error
const test5: (name: string, gender?: string, age: number) => string = function(name: string, gender?: string, age: number): string {
    return name + age;
}

/**函数的默认参数 */
// TypeScript 会将添加了默认值的参数识别为可选参数
function test6(name: string, gender?: string, age: number = 18): string {
    return age + name + gender
}

// 剩余参数
function test7(name: string, ...others: Array<any>): string{
    return name + others.join('-');
}

// 重载 没怎么看明白，准备参考一下其它资料