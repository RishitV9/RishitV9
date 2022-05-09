var http = require("http");
var Unblocker = require("unblocker");
const fs = require("fs")

var unblocker = Unblocker({});

var server = http.createServer(function (req, res) {
    unblocker(req, res, function (err) {
      var headers = { "content-type": "html" };

      if (err) {
        res.writeHead(500, headers);
        return res.end(err.stack || err);
      }

      else {
        res.writeHead(200, headers);
        fs.readFile("block.html", "utf-8", (error, data) => {
            if (!error) {
              return res.end(data);
            }
        })
      }
    });
  })
  .listen(8080);

server.on("upgrade", unblocker.onUpgrade);

console.log("proxy server live at http://8080-rishitv9-rishitv9-f02ximqlr56.ws-us44.gitpod.io/");
