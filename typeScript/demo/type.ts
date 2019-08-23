

/**
 * 类型别名 
 * 类型别名用来给一个类型起个新名字
 * 类型别名常用于联合类型
 * */

type name1 = string;
type name2 = string;

type nameType = name1 | name2;

let myName: nameType;