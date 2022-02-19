
const items = Symbol('stackItems');

/**栈 */
class Stack{
    constructor(){
        this[items] = {};
        this.count = 0;
    }

    push(element){
        this[items][this.count] = element;
        this.count++;
    }

    pop(){
        if(this.isEmpty){
            return undefined;
        }
        const r = this[items][this.couunt];
        delete this[items][this.count];
        this.count--;
        return r;
    }

    size(){
        this.count;
    }

    isEmpty(){
        return this.count === 0;
    }
}

const s = new Stack();

s.push(1)

