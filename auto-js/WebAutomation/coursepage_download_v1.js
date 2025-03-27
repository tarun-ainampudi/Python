table = document.getElementsByClassName("table");
authorizedID = $("#authorizedIDX").val();
csrf = $('input[name="_csrf"]').val();

topicIndex = 8;
linkIndex = 9;
ref_links = { "links": [] };
lecture_topics = { "topics": [] };

data = table[2].getElementsByTagName("td");
nTimes = data.length;

while (topicIndex < nTimes && linkIndex < nTimes) {
    full_param = data[linkIndex].querySelector("a") ? data[linkIndex].querySelector("a").getAttribute("href") : null;
    req_param = full_param?.match(/'([^']+)'/)?.[1]; // Safe regex extraction
    file_url = req_param ? `https://vtop.vitap.ac.in/vtop/${req_param}?authorizedID=${authorizedID}&_csrf=${csrf}` : null;

    lecture_topics.topics.push(data[topicIndex] ? data[topicIndex].innerText : null);
    ref_links.links.push(file_url);

    topicIndex += 5;
    linkIndex += 5;
}

// Async function for downloading PDFs one by one
async function downloadPDFs() {
    for (let i = 0; i < ref_links.links.length; i++) {
        const pdfUrl = ref_links.links[i];
        const filename = lecture_topics.topics[i] ? lecture_topics.topics[i] + ".pdf" : "unknown.pdf";

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
    }
}

// Call the function after data is populated
downloadPDFs();

console.log(ref_links);
console.log(lecture_topics);
