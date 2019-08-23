fs(文件系统)
===========
> Node.js 文件系统（fs 模块）模块中的方法均有异步和同步版本  

写入文件
--------
```javascript
fs.writeFile('test.html','<div>nihao</div>', err => {
    if(err) throw err
})
```
删除文件
--------
```javascript
fs.unlink('./test.html', err => {
    if(err) throw err
    console.log('文件删除成功')
})
```
读取文件
--------
```javascript
// 异步读取文件
fs.readFile('events.md', (err, data) => {
    if(err) throw err
    console.log(data) // buffer
    console.log(data.toString('utf8')) // 文本
})

// 同步读取文件
const data1 = fs.readFileSync('buffer.md', 'utf8');
console.log(data1)

// 读取文件相关属性
fs.stat('./buffer.md', (err, stats) => {
    if(err) throw err
    console.log(stats)
   // 检测文件类型
   console.log("是否为文件(isFile) ? " + stats.isFile());
   console.log("是否为目录(isDirectory) ? " + stats.isDirectory());    
})
```