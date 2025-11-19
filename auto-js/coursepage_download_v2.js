table = document.getElementsByClassName("table");
authorizedID = $("#authorizedIDX").val();
csrf = $('input[name="_csrf"]').val();

topicIndex = 8;
linkIndex = 9;
ref_links = {};
lecture_topics = { "topics": [] };

data = table[2].getElementsByTagName("td");
nTimes = data.length;
refIndex = 0;

while (topicIndex < nTimes && linkIndex < nTimes) {
   mul_links = [];
   data[linkIndex].querySelectorAll("a") ? mul_links=data[linkIndex].querySelectorAll("a"): null;
   links=[];
if (mul_links){for (let i of mul_links) {
    if (i.innerText.toLowerCase().includes("reference")&&i.innerText.toLowerCase().includes("material")) {
        full_param=i.getAttribute("href")?i.getAttribute("href") : null;
        req_param = full_param?.match(/'([^']+)'/)?.[1];
        file_url = req_param ? `https://vtop.vitap.ac.in/vtop/${req_param}?authorizedID=${authorizedID}&_csrf=${csrf}` : null;
        links.push(file_url);
    }
}}

ref_links[refIndex] = links;
refIndex+=1;
topic = data[topicIndex] ? data[topicIndex].innerText : null;
topic = topic.toLowerCase().replaceAll(",", "_").replaceAll("-","_").replaceAll(" ", "_").replaceAll("__", "_");
    lecture_topics.topics.push(topic);

    topicIndex += 5;
    linkIndex += 5;
}


async function downloadPDFs() {
    for (let i = 0; i < lecture_topics.topics.length; i++) {

        if (ref_links[i]){
            var k=0;
            for (let j of ref_links[i]) {
            const pdfUrl = j;
            const filename = lecture_topics.topics[i] ? lecture_topics.topics[i] +"["+k+"].pdf" : "unknown.pdf";
            k+=1;
            if (pdfUrl) {
                try {
                    const response = await fetch(pdfUrl);
                    const blob = await response.blob();
                    const link = document.createElement("a");
                    const url = URL.createObjectURL(blob);
                    link.href = url;
                    link.download = filename;
                    link.click();
                    URL.revokeObjectURL(url);
                    console.log("Downloaded:", filename);
                } catch (error) {
                    console.error("Error fetching PDF:", pdfUrl, error);
                }
            }
         
        }}
     
    }
}

// Call the function after data is populated
downloadPDFs();

//console.log(ref_links);
//console.log(lecture_topics);
