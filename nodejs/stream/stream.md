Stream(数据流)
=================
> 当内存中无法一次装下需要处理的数据时，或者一边读取一边处理更加高效时，我们就需要用到数据流;       
> 所有的 Stream 对象都是 EventEmitter 的实例;

Stream对象常用事件：
- data==>当有数据读取时触发
- end==>没有数据读取时触发
- error==>读取产生错误时触发
- finish==>所有数据被写入底层系统时触发

读取数据、写入数据
------------------
```javascript
/**读取数据 */
const rs = fs.createReadStream('./stream.md');

rs.on('data', chunk=>{
    console.log('chunk', chunk)
})

rs.on('end', () => {
    console.log('读完了')
})

/**写入数据 */
const ws = fs.createWriteStream('./output.txt');

ws.write('哈哈哈哈', 'UTF8');
ws.end();
ws.on('finish', () => {
    console.log('写完了')
})
ws.on('error', () => {
    console.log('写错了')
})
```

管道流
--------
使用管道流复制文件
```javascript
/**复制文件 */
const readStream = fs.createReadStream('./output.txt')
const writeStream = fs.createWriteStream('./output1.txt')
readStream.pipe(writeStream)
```

链式流
----
使用链式流压缩文件
```javascript
const fs = require('fs');
const zlib = require('zlib');

fs.createReadStream('output.txt')
    .pipe(zlib.createGzip())
    .pipe(fs.createWriteStream('output.txt.gz'))
```
