//open grade history and run this in console
table = document.getElementsByClassName("customTable")[1];
contents = table.getElementsByClassName("tableContent");
contents_len = table.getElementsByClassName("tableContent").length;
var only_cont = [];
for (var i=0 ; i<contents_len ; i++){
	if(contents[i].id===''){only_cont.push(contents[i]);}
}

var courses = [];

for (var i=0 ; i<only_cont.length ; i++){

	course_code = only_cont[i].getElementsByTagName("td")[1].innerText || null;
	credits = parseInt(only_cont[i].getElementsByTagName("td")[4].innerText) || null
	grade = only_cont[i].getElementsByTagName("td")[5].innerText || null;
	result_declared = only_cont[i].getElementsByTagName("td")[7].innerText || null;

	course = {
	cc : course_code,
	credits : credits,
	grade : grade,
	result_declared : result_declared,
	}
	 courses.push(course);
}

function gpa(courses_list){
	var gpa_list =[];
	var numerator =[];
	var denominator = [];
	var str = "";

	grade_map =  {
		's':10,
		'a':9,
		'b':8,
		'c':7,
		'd':6,
		'e':5,
		'f':0,
		'p':0
	}

	var nIndex = 0;
	var dIndex = 0;

	for (var i=0 ; i<courses_list.length ; i++){

		grade_point = grade_map[courses_list[i].grade.toLowerCase()]
		numerator[nIndex] = (numerator[nIndex] || 0) + courses_list[i].credits*grade_point;
		if(courses_list[i].grade.toLowerCase() !== 'p'){
		denominator[dIndex] = (denominator[dIndex] || 0) + courses_list[i].credits;}

		if(i < courses_list.length - 1 && courses_list[i].result_declared !== courses_list[i+1].result_declared){nIndex=nIndex+1;dIndex=dIndex+1;}

	}
	nSum = 0;
	dSum = 0;

	for (var i=0 ; i<Math.min(numerator.length,denominator.length) ; i++){
		nSum = nSum + numerator[i];
		dSum = dSum + denominator[i];
		gpa = numerator[i] / denominator[i];
		gpa_list.push(parseFloat(gpa.toFixed(2)));
		//console.log("GPA[SEM "+(i+1)+"] : "+parseFloat(gpa.toFixed(2)));
		str=str+"GPA[SEM "+(i+1)+"] : "+parseFloat(gpa.toFixed(2))+"\n";
	}
	cgpa = nSum/dSum;
	//console.log("CGPA : "+parseFloat(cgpa.toFixed(2)));
	str=str+"CGPA : "+parseFloat(cgpa.toFixed(2))+"\n";
    console.log(str);
}
gpa(courses);