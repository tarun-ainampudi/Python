function getLinks(xhrRes) {
    var parser = new DOMParser();
    var doc1 = parser.parseFromString(xhrRes, "text/html");
    var doc = doc1.getElementById("main");
    var li = doc.getElementsByTagName("a");
    var newList = [];
    for (var i = 0; i < li.length; i++) {
        if (li[i].className === "" && li[i].title === "" && li[i].rel === "bookmark" && li[i].children.length === 0) { newList.push(li[i]); }
    }
    //console.log(newList);
    for (var i = 0; i < newList.length; i++) {
        console.log(newList[i].href + " --- " + newList[i].innerHTML);
    }
    return newList;
}

function getDocument(url){
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url, false);
    xhr.send(null);
    return xhr.response;
}

var links = {};
for(var i = 1 ; i <= 464 ; i++ ){
    var gd = getDocument("https://naasongs.com.co/page/" + i);
    var extractedLinks = getLinks(gd);
    links[i] = extractedLinks;
}
