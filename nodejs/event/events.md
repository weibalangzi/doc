events模块
==========
> events只有一个对象，即eventEmitter，EventEmitter 的核心就是事件触发与事件监听器功能的封装  
> 大多数时候我们不会直接使用 EventEmitter，而是在对象中继承它。包括 fs、net、 http 在内的，只要是支持事件响应的核心模块都是 EventEmitter 的子类。  

事件触发、监听、传参
----------------------
```javascript
// 监听事件
eventEmitter.on('person_des', (options) => {
    console.log('optjions', options)
})

// 需要传递的对象
const options = {
    name: 'hehe',
    age: 18,
}

// 触发事件
eventEmitter.emit('person_des', options)
```
错误事件error
-------------
error事件是一个特殊的事件，遇到异常时会触发。
- 如果没有监听错误事件，则会退出程序
```javascript
/**触发error事件 */
eventEmitter.emit('error')


Error [ERR_UNHANDLED_ERROR]: Unhandled error.
    at EventEmitter.emit (events.js:178:17)
    at Object.<anonymous> (E:\hewei\nodejs\events.js:47:14)
    at Module._compile (internal/modules/cjs/loader.js:701:30)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:712:10)
    at Module.load (internal/modules/cjs/loader.js:600:32)
    at tryModuleLoad (internal/modules/cjs/loader.js:539:12)
    at Function.Module._load (internal/modules/cjs/loader.js:531:3)
    at Function.Module.runMain (internal/modules/cjs/loader.js:754:12)
    at startup (internal/bootstrap/node.js:283:19)
    at bootstrapNodeJSCore (internal/bootstrap/node.js:622:3)
```
- 监听错误事件，自己处理错误信息
```javascript
// 监听错误事件
eventEmitter.on('error', () => {
    console.log('报错了')
})

/**触发error事件 */
eventEmitter.emit('error')
```