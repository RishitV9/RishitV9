var http = require("http");
var Unblocker = require("unblocker");
const fs = require("fs")

var unblocker = Unblocker({});

var server = http.createServer(function (req, res) {
    // first let unblocker try to handle the requests
    unblocker(req, res, function (err) {
      // this callback will be fired for any request that unblocker does not serve
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

// allow unblocker to proxy websockets
server.on("upgrade", unblocker.onUpgrade);

console.log("proxy server live at http://localhost:8080/");