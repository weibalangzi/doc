

/**
 * 字符串字面量类型
 * 字符串字面量类型用来约束取值只能是某几个字符串中的一个
 */

type MyName = 'hehe' | 'haha' | 'heihei'

let isMe: MyName;

isMe = 'hehe';

// 取值早已被约束
isMe = 'aaa'; // error