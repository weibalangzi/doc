declare function greeter(person: string): string;
declare enum Direction {
    left = 0,
    right = 1,
    top = 2,
    bottom = 3
}
declare const enum Direction2 {
    left = 1,
    right = 2,
    top = 3,
    bottom = 4
}
interface User {
    name: string;
    age?: number;
    readonly gender: string;
}
declare const getUser: (user: User) => string;
declare const userName: string;
declare const sayhi: <T>(txt: T) => void;
