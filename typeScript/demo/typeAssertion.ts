
/**
 * 类型断言
 * 类型断言（Type Assertion）可以用来手动指定一个值的类型
 * 语法： <类型>值 或者 值 as 类型
 */

 let data: string | number;

 // error 当 TypeScript 不确定一个联合类型的变量到底是哪个类型的时候，我们只能访问此联合类型的所有类型里共有的属性或方法
 if(data.length > 0){
     alert(data)
 }

 // 使用类型断言，将当前变量断言成被允许的类型
 if((<string>data).length > 0){
     alert(data)
 }

 // error 原本定义的data的联合类型里面并没有array
 if((<array>data).length > 0){
     alert(data)
 }