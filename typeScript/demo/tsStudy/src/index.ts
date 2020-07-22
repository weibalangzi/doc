
function greeter(person: string){
    return 'hello' + person
}


enum Direction {
    left,
    right,
    top,
    bottom,
}

const enum Direction2 {
    left = 1,
    right,
    top,
    bottom,
}

interface User {
    name: string,
    age?: number,
    readonly gender: string,
}

const getUser = (user: User): string => {
    return user.name
}

const userName: string = getUser({name: 'hehe', age: 12, gender: 'man'})

const sayhi = <T>(txt: T): void => {
    console.log('txt', txt)
}

sayhi(123)
sayhi('djkfdfkd')


function getValue<T extends object, U extends keyof T>(item: T, key: U){
    return item[key]
}

const people:Record<string,any> = {
    name: 'chengfeng',
    age: 10
}