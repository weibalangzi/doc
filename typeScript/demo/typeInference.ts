/**类型推论 */
let word = 123123; // 未明确定义word类型，但是赋值后，会根据当前值推论出类型

// error
word = 'aaaaa'; // 此时word已经被推论类型为Number，故而赋值为字符串时会报错