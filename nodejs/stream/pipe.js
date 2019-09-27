const fs = require('fs');
const zlib = require('zlib');

fs.createReadStream('output.txt')
    .pipe(zlib.createGzip())
    .pipe(fs.createWriteStream('output.txt.gz'))