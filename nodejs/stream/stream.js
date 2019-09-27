const fs = require('fs');

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


/**复制文件 */
const readStream = fs.createReadStream('./output.txt')
const writeStream = fs.createWriteStream('./output1.txt')
readStream.pipe(writeStream)