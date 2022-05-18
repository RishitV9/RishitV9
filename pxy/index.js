// import dependencies:
const Unblocker = require("unblocker");
const fs = require("fs");
const https = require("http");
const unblocker = Unblocker({});
const port = 8080;


// startup:
console.log(`[*] STARTING AT PORT: ${port}....`);
const server = https.createServer(function (req, res) {
    console.log()
    unblocker(req, res, function (err) {
      const headers = { "content-type": "html" };

      // send response
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
  .listen(port);

server.on("upgrade", unblocker.onUpgrade);

console.log(`[*] Proxy Server live at http://${port}-rishitv9-rishitv9-ldgqgowvow7.ws-us45.gitpod.io/`);
