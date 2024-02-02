<
  input id = "input" > < /input><button onclick="check()">check solve</button > < script > function check() {
        checkSolve(document.getElementById('input').value);
  }
async function checkSolve(n) {
      const o = JSON.parse('{\
          "0": "",\
          "48": "0",\
          "95": "_",\
          "107332": "log",\
          "107868": "map",\
          "3151786": "from",\
          "3267882": "join",\
          "3344077": "mark",\
          "3373707": "name",\
          "92960979": "angle",\
          "99463871": "hope{",\
          "109526418": "slice",\
          "400256961": "you got it!",\
          "757893007": "padStart",\
          "1207387375": "wrong flag :(",\
          "1811681647": "_sold!}",\
          "-1074417128": "[object Object]",\
          "-1523887726": "SHA-256",\
          "-989967315": "fromCharCode",\
          "-1106363674": "length",\
          "-1776922004": "toString",\
          "-1266514778": "frames",\
          "-1013175693": "onLine",\
          "-1439500848": "orientation",\
          "-1298776554": "encode",\
          "-1331913276": "digest",\
          "-891528531": "subtle"\
}');
      const e = String["fromCharCode"](+(148) - eval["toString"]()["length"]) + String["fromCharCode"]((window.frames["length"] !== -1) * 72) + String["fromCharCode"]((navigator["onLine"] + screen.orientation["angle"]) * 111) + String["fromCharCode"]((performance["mark"]({})["name"] === "[object Object]") * 101);
      const t = new TextEncoder()["encode"](e);
      const r = await crypto.subtle["digest"]("SHA-256", t);
      const a = Array["from"](new Uint8Array(r));
      const c = a["map"](function(n) {
                return n["toString"](16)["padStart"](2, "0");
            })["join"]("");
    const i = c["slice"](16);
    if (n === "hope{" + e + "_" + i + "_sold!}") {
              console['log']("you got it!");
          } else {
                    console['log']("wrong flag :(");
                }
} < /script>
