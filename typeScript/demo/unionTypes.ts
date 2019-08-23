/**联合类型 */
let some: String | Number | Boolean; // 即变量的类型可以为多种

/**
 * 访问联合类型的属性或方法 
 * 当 TypeScript 不确定一个联合类型的变量到底是哪个类型的时候，我们只能访问此联合类型的所有类型里共有的属性或方法
 * */
// error
console.log(some.length) // 因为some也有可能为Number或者Boolean，但是这两种类型是没有长度的

/**联合类型的变量在被赋值的时候，会根据类型推论的规则推断出一个类型 */
some = 'aaaaa';
console.log(some.length);

some = 1111;
console.log(some.length);// error


/**所以为定义类型的变量，其最后一次赋值时，所推论出的类型，及为该变量当前的类型 */