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
async function downloadFiles() {
    for (let i = 0; i < lecture_topics.topics.length; i++) {
        if (ref_links[i]) {
            let k = 0;
            for (let fileUrl of ref_links[i]) {
                if (!fileUrl) continue;

                try {
                    const response = await fetch(fileUrl, { credentials: "include" });

                    let filename = null;

                    // 1. Try from Content-Disposition
                    const disposition = response.headers.get("Content-Disposition");
                    if (disposition && disposition.includes("filename=")) {
                        const match = disposition.match(/filename="?([^"]+)"?/);
                        if (match) {
                            filename = match[1];
                        }
                    }

                    // 2. Fallback: from URL
                    if (!filename) {
                        let urlPart = fileUrl.split("/").pop().split("?")[0];
                        if (urlPart && urlPart.includes(".")) {
                            filename = urlPart;
                        }
                    }

                    // 3. Fallback: from MIME type
                    if (!filename) {
                        const mime = response.headers.get("Content-Type");
                        let ext = "bin"; // default
                        if (mime) {
                            if (mime.includes("pdf")) ext = "pdf";
                            else if (mime.includes("msword")) ext = "doc";
                            else if (mime.includes("officedocument.wordprocessingml")) ext = "docx";
                            else if (mime.includes("presentation")) ext = "pptx";
                            else if (mime.includes("spreadsheet")) ext = "xlsx";
                            else if (mime.includes("zip")) ext = "zip";
                            else if (mime.includes("image/jpeg")) ext = "jpg";
                            else if (mime.includes("image/png")) ext = "png";
                        }
                        filename = `file.${ext}`;
                    }

                    // 4. Add your lecture topic name + index
                    const topicName = lecture_topics.topics[i] || "unknown";
                    const finalName = `${topicName}[${k}].${filename.split(".").pop()}`;
                    k++;

                    // 5. Download
                    const blob = await response.blob();
                    const url = URL.createObjectURL(blob);
                    const link = document.createElement("a");
                    link.href = url;
                    link.download = finalName;
                    link.click();
                    URL.revokeObjectURL(url);

                    console.log("Downloaded:", finalName);
                } catch (error) {
                    console.error("Error fetching file:", fileUrl, error);
                }
            }
        }
    }
}

// Call the function
downloadFiles();
