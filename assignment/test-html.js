const fs = require('fs');
console.log(fs.readFileSync('index.html', 'utf8').substring(0, 100));
