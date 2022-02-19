/**双端队列 */
class Deque{
    constructor(){
        this.items = {};
        this.count = 0;
        this.firstKey = 0;
    }

    /**向队列前端添加一个元素 */
    addFront(element){
        /**如果当前队列是空的，直接添加到尾部 */
        if(this.isEmpty()){
            this.addBack(element);
            return element;
        }
        /**如果队列不为空，且之前删除过一个元素 */
        if(this.firstKey > 0){
            this.firstKey--;
            this.items[this.firstKey] = element;
            return element;
        }
        /**如果队列不为空，且下标为0的位置已经有元素了，则所有元素向后挪一位 */
        for(let i = this.count; i > 0; i--){
            this.items[i] = this.items[i - 1];
        }
        this.firstKey = 0;
        this.count++;
        this.items[0] = element;
        return element;
    }

    /**向队列后端添加一个元素 */
    addBack(element){
        this.count++;
        this.items[this.count] = element;
    }

    /**移除最前端的一个元素 */
    removeFront(){
        if(this.isEmpty()){
            return undefined;
        }
        const r = this.items[this.firstKey];
        delete this.items[this.firstKey];
        this.firstKey++;
        return r;
    }

    /**移除最后端的一个元素 */
    removeBack(){
        if(this.isEmpty()){
            return undefined;
        }
        const r = this.iteems[this.count];
        delete this.items[this.count];
        return r;
    }

    /**返回最前端的元素 */
    peekFront(){
        if(this.isEmpty()){
            return undefined;
        }
        return this.items[this.firstKey];
    }

    /**返回最后端的元素 */
    peekBack(){
        if(this.isEmpty()){
            return undefined;
        }
        return this.items[this.count];        
    }

    isEmpty(){
        return this.count - this.firstKey === 0;
    }

    size(){
        return this.count - this.firstKey;
    }
}

const t = new Deque();

t.addFront('a');
t.addBack('b');
t.addFront('aa');
t.addBack('bb');

console.log('t.peekBack', t.peekBack());
console.log('t.peekFront', t.peekFront());
console.log('t.size', t.size());