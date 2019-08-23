
/**数组类型 */

// 方式一
let arr1: number[];

// error
arr1.push('aaa'); // 如上，约束了只能为number类型

// 方式二
let arr2: Array<number>;

// 方式三
interface IArr{
    [index: number]: number
}

// error
let arr3: IArr = [1, 2, 3, '4'] // 于是报错了

// 正常情况下，数组里面最好可以添加任意类型
let arr4: any[];


/**类数组 */

// error
function test(){
    let arr5: any[] = arguments // 类数组并非数组。所以报错了。
}

// 常见的类数组都有自己的接口定义，如 IArguments, NodeList, HTMLCollection 等

// error
function test2(){
    let arr6: IArguments = arguments
}