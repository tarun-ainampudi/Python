//better remove the time stamp in the ajax request with url examinations/processDigitalAssignmentUpload
//or
//change the last_date variable acording to the date and time of the last upload

//run it console in digital assignment upload page

//you can correct mcode in the download button href link

//mcode will either be the title if it is lab or someother i.e : Experiment-6

//if title is Digital Assessment-1 then mCode will be DA01

//if title is Event-1 then mCode will be AST01

var myform = document.getElementById("daUpload");
var ofd = new FormData(myform);
ofd.delete("authorizedID");

var fd = new FormData();

fd.append("authorizedID", document.getElementById("authorizedID").value);

const [fileHandle] = await window.showOpenFilePicker();
const file = await fileHandle.getFile();
fd.append("studDaUpload", file);

for (const [key, value] of ofd.entries()) {
	fd.append(key, value);
}

var classId = document.querySelector("#fixedTableContainer > table > tbody > tr.fixedContent.tableContent > td:nth-child(5)").innerText;
fd.append(csrfName, csrfValue);
fd.append("classId", classId);

for (const [key, value] of fd.entries()) {
	console.log(`${key}:`, value);
}

var mode = prompt("Enter mCode:") 
fd.append("mCode", mode);
console.log("mCode:", fd.get("mCode"));

var daUploadFlag = true;
var path = 'C:\\fakepath\\' + file.name; // Simulating the file path as it would appear in a file input
console.log("studDaUpload:", path);
var uploadedFile = path;
if (uploadedFile == '') {
	swal("Kindly upload the file", "", "warning");
	daUploadFlag = false;
}
if (uploadedFile != '') {
	var checkimg = uploadedFile.toLowerCase();

	if (!checkimg.match(/(\.pdf|\.xls|\.xlsx|\.doc|\.docx)$/)) { // validation of file extension using regular expression before file upload
		document.getElementById("studDaUpload").focus();
		swal("File type should be pdf,xls,xlsx,doc,docx", "", "warning");
		daUploadFlag = false;
	}
	if (uploadedFile != '' && file.size > 4194304)  // validation according to file size
	{
		swal("File size (Max. upto 4MB)", "", "warning");
		daUploadFlag = false;
	}
}
console.log("daUploadFlag:", daUploadFlag);


var last_date = "14-Mar-2025 22:09:23";
$.blockUI({

		message: '<img src="assets/img/482.GIF"> loading... Just a moment...'
	});

var authorizedID = document.getElementById("authorizedID").value;
var now = new Date(last_date);
params = "authorizedID=" + authorizedID + "&x="
	+ now.toUTCString() + "&classId=" + classId + "&mode="
	+ mode + "&" + csrfName + "=" + csrfValue;

$.ajax({
	url: "examinations/processDigitalAssignmentUpload",
	type: "POST",
	data: params,

	success: function (response) {
		$.unblockUI();
		$("#main-section").html(response);

	}

});


if (daUploadFlag == true) {

	$.blockUI({
		message: '<img src="assets/img/482.GIF"> loading... Just a moment...'
	});
	$.ajax({
		url: "examinations/doDAssignmentUploadMethod",
		type: "POST",
		data: fd,
		cache: false,
		processData: false,
		contentType: false,
		success: function (response) {
			$.unblockUI();
			$("#main-section").html(response);
		}

	});
}