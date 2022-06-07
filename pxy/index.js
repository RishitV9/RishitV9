// import dependencies:
const Unblocker = require("unblocker");
const fs = require("fs");
const https = require("http");
const unblocker = Unblocker({});
const txtLog = new console.Console(fs.createWriteStream('logs.txt'));
const port = 8080;
const headers = { "content-type": "html" };

// ip address funstion:
const parseIp = (req) =>
    req.headers['x-forwarded-for']?.split(',').shift()
    || req.socket?.remoteAddress


// startup:
console.log(`[*] STARTING AT PORT: ${port}....`);
const server = https.createServer(function (req, res) {
    if (req.url === "/log/") {
      res.writeHead(200, headers);
      fs.readFile("logs.txt", "utf-8", (error, data) => {
        if (!error) {
          return res.end(data);
        }
      })
    }
    if (!(req.url.indexOf("/u7hhgw0lh2.herokuapp.com/socket.io/") > 0)) {
      txtLog.log("[*] GET -> REQUESTED: (", req.url, ") BY " + parseIp(req))
    }
    unblocker(req, res, function (err) {


      // send response
      if (err) {
        res.writeHead(500, headers);
        return res.end(err.stack || err);
      }

      else {
        txtLog.log("[*] INVALID URL, SENDING block.html...")
        res.writeHead(200, headers);
        fs.readFile("block.html", "utf-8", (error, data) => {
            if (!error) {
              return res.end(data);
            }
        })
      }
    });
  })
  .listen(port);

server.on("upgrade", unblocker.onUpgrade);

console.log(`[*] Proxy Server live at http://localhost:${port} (use gitpod link for usage)`);
