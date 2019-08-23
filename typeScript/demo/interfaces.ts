/**
 * 接口
 * typeScript中接口用于对类的一部分行为进行抽象，也用于对对象的形状进行描述 
 * */

 // 接口名称的首字母大写，最后以大写I开头
 interface IProps {
     name: String,
     age: Number,
 }

 // 在IProps中，name与age都是必须的，所以为空会报错
 let person: IProps = {} 

 // 只有两个字段值都存在且正确时才是ok的
 let person1: IProps = {
     name: 'hehe',
     age: 18
 }

 // 不能添加未定义的属性，不能多，不能少，不能错
let person2: IProps = {
    name: 'hehe',
    age: 18,
    happy: false, // error
}

/**
 * 可选属性
 * 如下，加个'?'就可以了，使用的时候没有happy这个属性，一样可以正常使用 
 * */
interface IProps2 {
    name: String,
    age: Number,
    happy?: Boolean,
}

/**
 * 任意属性
 * 想是多少就是多少，任意个属性
 * 一旦定义了任意属性，那么确定属性和可选属性的类型都必须是它的类型的子集
 * */
interface IProps3 {
    name: string,
    [PropName: string]: string, 
}

// 可以添加任意多个属性，但是属性的类型是有被限制为sting的
let person3: IProps3 = {
    name: 'hehe',
    happy: false, // error
}


// 所以对属性的类型也不做限制，这样可以任意属性，任意类型
interface IProps4 {
    name: string,
    [PropName: string]: any,
}

let person4: IProps4 = {
    name: 'hehe',
    happy: false,
}

/**只读属性 */
interface IProps5 {
    readonly name: string;
    age: Number;
}

let person5: IProps5 = {
    name: 'hehe',
    age: 18,
}

person5.age = 19;
// 只读的约束存在于第一次给对象赋值的时候，而不是第一次给只读属性赋值的时候
person5.name = 'haha'; // error


