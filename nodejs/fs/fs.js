
/**
 * fs(文件系统)
 */

const fs = require('fs');

// 写入文件
fs.writeFile('test.html','<div>nihao</div>', err => {
    if(err) throw err
})

// 异步读取文件
fs.readFile('events.md', (err, data) => {
    if(err) throw err
    console.log(data) // buffer
    console.log(data.toString('utf8')) // 文本
})

// 同步读取文件
const data1 = fs.readFileSync('buffer.md', 'utf8');
console.log(data1)

// 以读取模式打开文件。如果文件不存在抛出异常
fs.open('./buffer.md', 'r', (err, data) => {
    if(err) throw err
    
    console.log(data)
})

// 读取文件相关属性
fs.stat('./buffer.md', (err, stats) => {
    if(err) throw err
    console.log(stats)
   // 检测文件类型
   console.log("是否为文件(isFile) ? " + stats.isFile());
   console.log("是否为目录(isDirectory) ? " + stats.isDirectory());    
})

// 删除文件
fs.unlink('./test.html', err => {
    if(err) throw err
    console.log('文件删除成功')
})