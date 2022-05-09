const express = require("express");
const Unblocker = require("unblocker");
const app = express();
const unblocker = Unblocker({});

app.use(unblocker);
app.get("/", (req, res) =>
  res.redirect("/proxy/https://kproxy.com")
);

const port = process.env.PORT || 3000;
app.listen(port).on("upgrade", unblocker.onUpgrade);

console.log(`unblocker app live at http://${port}-rishitv9-rishitv9-f02ximqlr56.ws-us44.gitpod.io/`);
