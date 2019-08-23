
/**事件 */

var events = require('events');

// 创建eventEmitter对象
var eventEmitter = new events.EventEmitter();

// 创建事件处理程序
var eventHanlder = function connected(){
    console.log('连接成功');
    eventEmitter.emit('event_received');
}

// 绑定事件处理程序
eventEmitter.on('connection', eventHanlder);

// 绑定event_received事件
eventEmitter.on('event_received', function(){
    console.log('接收到event_received事件');
})

// 触发事件
// eventEmitter.emit('connection');




/**触发事件并传参 */

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

// 监听错误事件
eventEmitter.on('error', () => {
    console.log('报错了')
})

/**触发error事件 */
eventEmitter.emit('error')