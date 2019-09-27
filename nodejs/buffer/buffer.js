
// 指定默认编码格式
const buf1 = Buffer.from('hahahahha', 'utf8');

console.log(buf1); // <Buffer 68 61 68 61 68 61 68 68 61>

// 编码后转为字符串
console.log(buf1.toString()); // hahahahha
console.log(buf1.toString('utf8')); // hahahahha
console.log(buf1.toString('ascii')); // hahahahha
console.log(buf1.toString('base64')); // aGFoYWhhaGhh
console.log(buf1.toString('hex')); // 686168616861686861

console.log('=============')
// 创建buff类
const buf2 = Buffer.alloc(10); // 默认被0填充
console.log(buf2); // <Buffer 00 00 00 00 00 00 00 00 00 00>
const buf3 = Buffer.alloc(10, 1); // 长度10，内容都为1
console.log(buf3); // <Buffer 01 01 01 01 01 01 01 01 01 01>
const buf4 = Buffer.from([1, 2, 3]);
console.log(buf4); // <Buffer 01 02 03>


/**写入缓冲区 */
console.log('===========写入缓存区=============');
const buf5 = Buffer.alloc(10);
buf5.write('hello');
console.log(buf5); // <Buffer 68 65 6c 6c 6f 00 00 00 00 00>
buf5.write('how are you today')
// 如果写入的长度大于规定的长度, 则只会写入一部分
console.log(buf5); // <Buffer 68 6f 77 20 61 72 65 20 79 6f>

/**读取缓存区 */
console.log('==========读取缓存区===========');
console.log(buf5.toString()) // how are yo

/**将buffer转为json对象 */
console.log('========转为json对象==========')
const buf6 = Buffer.from([1, 2, 3, 4]) 
console.log(buf6) // <Buffer 01 02 03 04>
console.log(buf6.toJSON()) // { type: 'Buffer', data: [ 1, 2, 3, 4 ] }
console.log(typeof buf6.toJSON()) // object