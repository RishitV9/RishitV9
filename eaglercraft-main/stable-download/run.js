var http = require('http')
var fs = require('fs')
var index = fs.readFileSync('Offline_Download_Version.html')

const port = 8000;

http.createServer((req, res) => {
    res.writeHead(200, {'Content-Type': 'text/html'})
    res.end(index);
}).listen(port)
