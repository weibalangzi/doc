
/**队列 */
class Queue{
    constructor(){
        this.count = 0;
        this.items = {};
        this.firstKey = 0; 
    }

    /**向队列尾部添加一个新元素 */
    unqueue(element){
        this.items[this.count] = element;
        this.count++;
    }

    /**移除队列第一项，并返回被移除的元素 */
    dequeue(){
        if(this.isEmpty){
            return undefined;
        }
        const r = this.items[this.firstKey];
        delete this.items[this.firstKey];
        this.firstKey++;
        return r;
    }

    /**返回当前队列的第一个元素 */
    peek(){
        if(this.isEmpty){
            return undefined;
        }
        return this.items[this.firstKey];
    }

    isEmpty(){
        return this.count - this.firstKey === 0;
    }

    size(){
        return this.count - this.firstKey;
    }

    clear(){
        this.items = {};
        this.count = 0;
        this.firstKey = 0;
    }
}

const t = new Queue();

t.unqueue('aAA');
t.unqueue('BAA');
t.unqueue('CAA');

console.log('t.peek()', t.peek());

t.dequeue();

console.log('t.peek()', t.peek());