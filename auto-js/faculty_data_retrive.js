doc = document.getElementsByClassName("table");
tab1 = doc[1].getElementsByTagName("tr");
authorizedID = $('#authorizedIDX').val();
csrf = $('input[name="_csrf"]').val();
len = tab1.length;
const facultyData = [];

for (let i = 1; i < len; i++) {
    const cells = tab1[i].getElementsByTagName("td");
    const name = cells[0].innerText.trim();
    const designation = cells[1].innerText.trim();
    const school = cells[2].innerText.trim();
    const button = cells[3].querySelector("button");
    const employeeId = button ? button.id : null;

    var data = "_csrf=" + csrf + "&authorizedID=" + authorizedID + "&empId=" + employeeId;

    $.ajax({
        type: 'POST',
        url: 'hrms/EmployeeSearch1ForStudent',
        data: data,
        async: false,  // Asynchronous calls are generally preferred. Use async: true if possible.
        success: function(res) {
 res = new DOMParser().parseFromString(res, 'text/html');
            // Check if the response is HTML
            const doc2 = res.getElementsByTagName("td");
            var emailId = doc2[11] ? doc2[11].innerText.trim() : null;
            var cabin = doc2[13] ? doc2[13].innerText.trim() : null;
if (cabin){}else{cabin="Not Updated in VTOP";}
if (emailId){}else{emailId="Not Updated in VTOP";}
            // If emailId and cabin are valid, add to facultyData
            if (name && designation && school && employeeId && emailId && cabin) {
                facultyData.push({
                    Name: name,
                    Designation: designation,
                    School: school,
                    EmployeeId: employeeId,
                    EmailId: emailId,
                    Cabin: cabin
                });
            }
        },
        error: function(xhr, status, error) {
            console.error("AJAX request failed:", error);
        }
    });
}

console.log(facultyData);
