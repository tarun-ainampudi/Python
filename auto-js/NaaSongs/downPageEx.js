var doc = document.getElementsByClassName("entry-content clearfix")[0];
var paragraphs = doc.getElementsByTagName("p");
var links = {};
for (var i = 0; i < paragraphs.length; i++) {
    if (paragraphs[i].getElementsByTagName("a").length > 0) {
        links[paragraphs[i].innerText.split("\n")[0]]={}
        for(var j = 0 ; j < paragraphs[i].getElementsByTagName("a").length ; j++){
            var Index = paragraphs[i].innerText.split("\n")[j+1] || paragraphs[i].getElementsByTagName("a")[j].innerText || "No Index";
            links[paragraphs[i].innerText.split("\n")[0]][Index]=paragraphs[i].getElementsByTagName("a")[j].href;
        }
    }
}
console.log(links);