// import dependencies:
const Unblocker = require("unblocker");
const fs = require("fs");
const https = require("http");
// const readline = require('readline').createInterface({
//   input: process.stdin,
//   output: process.stdout
// });
const unblocker = Unblocker({});
// const { exec } = require('child_process');
// let port;
// let verbose = false;


// // initialization:
// readline.question('[*] RUN AT PORT: ', portnumber => {
//   port = portnumber;
//   readline.close();
// });

// readline.question('[*] Make a command for bash usage? (y/n): ', reply => {
//   if (reply === "y") {
//     exec('sudo ln -s /cmd.sh /usr/local/bin/proxy', (err, stdout, stderr) => {
//       if (err) {
//         console.error(err)
//       }
//     });
//   }
//   readline.close();
// });

// readline.question('[*] Activate verbose mode to provide info about every request made to your server? (y/n): ', reply => {
//   if (reply === "y") {
//     verbose = true;
//   }
//   readline.close();
// });


// startup:
console.log(`[*] STARTING AT PORT: 8080....`);
const server = https.createServer(function (req, res) {
    // print info about request/response:
    // if (verbose) {
    //   console.log(`REQUEST: ${req}: ${req.method} -> ${request.dir}`)
    // }

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
  .listen(8080);

server.on("upgrade", unblocker.onUpgrade);

console.log(`[*] Proxy Server live at http://localhost:8080/`);
