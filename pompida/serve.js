// import dependencies:
const fs = require("fs");
const https = require("http");
const port = 8080;
const headers = { "content-type": "html" };


// startup:
console.log(`[*] STARTING AT PORT: ${port}....`);
const server = https.createServer(function (req, res) {
    res.writeHead(200, headers);
    fs.readFile("unbocked.html", "utf-8", (error, data) => {
        if (!error) {
            return res.end(data);
        }
    })
}
).listen(port);

console.log(`[*] Server live at http://localhost:${port} (use gitpod link for usage)`);
