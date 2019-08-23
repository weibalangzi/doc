
/**
 * stream(流)
 */

const fs = require('fs');

// 异步读取文件
fs.readFile('events.md', (err, data) => {
    if(err) throw err
    console.log(data) // buffer
    console.log(data.toString('utf8')) // 文本
})

// 同步读取文件
const data1 = fs.readFileSync('buffer.md', 'utf8');
console.log(data1)