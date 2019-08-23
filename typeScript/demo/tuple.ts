
/**
 * 元组
 * 元组起源于函数编程语言
 * 数组合并了相同类型的对象，而元组（Tuple）合并了不同类型的对象
 */

let arr: [number, string];

arr = [1, 'aaa'];

// 当直接对元组类型的变量进行初始化或者赋值的时候，需要提供所有元组类型中指定的项
arr = [1, 'aaa', 3]; // error

// 添加越界的元素时，它的类型会被限制为元组中每个类型的联合类型
arr.push('hahhaha');
arr.push(true);// error

