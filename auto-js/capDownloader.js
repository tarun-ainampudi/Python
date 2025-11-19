function downloadCap(base64_src, counter) {
  var a = document.createElement('a');
  a.href = base64_src;
  a.download = "captcha (" + counter + ").png";
  a.click();
}

async function captureAll(num) {
  for (let i = 0; i < num; i++) {
    const res = await fetch("get/new/captcha");
    const html = await res.text();
    const doc = new DOMParser().parseFromString(html, "text/html");
    const img = doc.querySelector("img");
    if (img){
        while(ca==1);
        ca=1;
        downloadCap(img.src, count++);
        ca=0;}
    await new Promise(r => setTimeout(r, 300)); // optional delay
  }
}

var num = 100;
var count = 1848;
var ca = 0
var per = 10*num/100;
for(let j = 0;j<10;j++){
    captureAll(per);
}