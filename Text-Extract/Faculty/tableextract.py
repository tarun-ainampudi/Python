from bs4 import BeautifulSoup

# Sample HTML
html_content = """
<table class="table" border="1">
														
														<tbody><tr style="text-align: center; border-style: solid;">
															<!-- <td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #afbadc;">Employee ID</td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #afbadc;">Name of the Faculty</td>															
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #afbadc;">Designation</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #afbadc;">School / Centre</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #afbadc;">Action</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> AASTHA MADONNA SATHE</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70531" onclick="getEmployeeIdNo(&quot;70531&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. AMRENDRA SINGH GILL</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70665" onclick="getEmployeeIdNo(&quot;70665&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Ms. ANINDITA ROY</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70682" onclick="getEmployeeIdNo(&quot;70682&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> ANURAG DE</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70557" onclick="getEmployeeIdNo(&quot;70557&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> A Phani Kumar</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70254" onclick="getEmployeeIdNo(&quot;70254&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Mr. ARIVARASAN A</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30047" onclick="getEmployeeIdNo(&quot;30047&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. ASHRAF PULIKKAMATH</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70594" onclick="getEmployeeIdNo(&quot;70594&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. BANDARU RAMA KRISHNA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70660" onclick="getEmployeeIdNo(&quot;70660&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. BEEBI NASEEBA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70390" onclick="getEmployeeIdNo(&quot;70390&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Mr. BENSHA C. SHAJI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70669" onclick="getEmployeeIdNo(&quot;70669&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. CHILUKAMARI RAJESH</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70645" onclick="getEmployeeIdNo(&quot;70645&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. CHIRUGURI SHYAM KUMAR</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Visiting Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="40009" onclick="getEmployeeIdNo(&quot;40009&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Mr. DINESH V</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30041" onclick="getEmployeeIdNo(&quot;30041&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. D. KOTHANDARAMAN</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70647" onclick="getEmployeeIdNo(&quot;70647&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. ABDUL RAFFIE NAIK</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70616" onclick="getEmployeeIdNo(&quot;70616&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. ABHISHEK YADAV</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70627" onclick="getEmployeeIdNo(&quot;70627&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.ALKA MUNJAL</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70584" onclick="getEmployeeIdNo(&quot;70584&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.AMRITA PURAKAYASTHA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70560" onclick="getEmployeeIdNo(&quot;70560&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. ANANTHU S HARI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70541" onclick="getEmployeeIdNo(&quot;70541&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. ANJITHA GOPI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70556" onclick="getEmployeeIdNo(&quot;70556&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. ANSHUL GOPAL</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70606" onclick="getEmployeeIdNo(&quot;70606&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR ANUPRIYA </td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70545" onclick="getEmployeeIdNo(&quot;70545&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR ASWATHY M</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70553" onclick="getEmployeeIdNo(&quot;70553&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.ATUL KUMAR</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70631" onclick="getEmployeeIdNo(&quot;70631&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Dr.Bikash Sharma</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20003" onclick="getEmployeeIdNo(&quot;20003&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.BOGGARAPU VASAVI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Research</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Mechanical Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70528" onclick="getEmployeeIdNo(&quot;70528&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. BUSHRA KHATOON</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70595" onclick="getEmployeeIdNo(&quot;70595&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. B.V.GOKULNATH</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70585" onclick="getEmployeeIdNo(&quot;70585&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. CHINTAKINDI BALARAM MURTHY</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70591" onclick="getEmployeeIdNo(&quot;70591&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. CHIRANJEEV KUMAR SHAHU</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70590" onclick="getEmployeeIdNo(&quot;70590&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.DEBOSMITA BISWAS</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70596" onclick="getEmployeeIdNo(&quot;70596&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. DEEPANRAMKUMAR P</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70608" onclick="getEmployeeIdNo(&quot;70608&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.DIBYENDU SEKHAR MANDAL</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70609" onclick="getEmployeeIdNo(&quot;70609&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. D. SANTHADEVI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70602" onclick="getEmployeeIdNo(&quot;70602&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. G D V SANTHOSH KUMAR</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70563" onclick="getEmployeeIdNo(&quot;70563&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. GOKULNATH M</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70554" onclick="getEmployeeIdNo(&quot;70554&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.G.SOMA SEKHAR</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70635" onclick="getEmployeeIdNo(&quot;70635&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.HABIBA KHATUN</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70615" onclick="getEmployeeIdNo(&quot;70615&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.HANUMANTHARAO BITRA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70564" onclick="getEmployeeIdNo(&quot;70564&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. HELEN SHARMILA A</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70607" onclick="getEmployeeIdNo(&quot;70607&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. IRAM</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70535" onclick="getEmployeeIdNo(&quot;70535&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. JABEEN YASMEEN</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70623" onclick="getEmployeeIdNo(&quot;70623&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. JEETHU V. DEVASIA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70633" onclick="getEmployeeIdNo(&quot;70633&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.KARTHICK V</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70598" onclick="getEmployeeIdNo(&quot;70598&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.KASHIF BEG</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70580" onclick="getEmployeeIdNo(&quot;70580&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR KAUSHIK N BHUYAN</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70558" onclick="getEmployeeIdNo(&quot;70558&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. KOTTU DURGA PRASAD</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70614" onclick="getEmployeeIdNo(&quot;70614&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR LELLA KRANTHI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70548" onclick="getEmployeeIdNo(&quot;70548&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. LINET THOMAS</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70578" onclick="getEmployeeIdNo(&quot;70578&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. MISHA </td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70539" onclick="getEmployeeIdNo(&quot;70539&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. MOHAN ALLAM</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70630" onclick="getEmployeeIdNo(&quot;70630&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.MOHIT KUMAR</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70562" onclick="getEmployeeIdNo(&quot;70562&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR MUTHU PRABHU S</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70542" onclick="getEmployeeIdNo(&quot;70542&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.NARESH SAMMETA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70592" onclick="getEmployeeIdNo(&quot;70592&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.NAVEEN KUMAR RANJAN</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70561" onclick="getEmployeeIdNo(&quot;70561&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. NEETHU P ANTONY</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70555" onclick="getEmployeeIdNo(&quot;70555&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.NIMAI SARKAR</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70593" onclick="getEmployeeIdNo(&quot;70593&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Dr Pradip Ramesh Patle</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70577" onclick="getEmployeeIdNo(&quot;70577&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.PRAGNYA PARIMITA CHAYANI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70622" onclick="getEmployeeIdNo(&quot;70622&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. PRAKASH S</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70613" onclick="getEmployeeIdNo(&quot;70613&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.PRASHANT PATEL</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70587" onclick="getEmployeeIdNo(&quot;70587&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. RAJASHREE NAIK</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70612" onclick="getEmployeeIdNo(&quot;70612&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. RAVI KUMAR BANDARU</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Senior</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70604" onclick="getEmployeeIdNo(&quot;70604&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.RITU VARGHESE</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70597" onclick="getEmployeeIdNo(&quot;70597&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.SAISTA TABSSUM</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70618" onclick="getEmployeeIdNo(&quot;70618&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.SANTANU NANDI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70534" onclick="getEmployeeIdNo(&quot;70534&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.SANZIOU BORO </td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70583" onclick="getEmployeeIdNo(&quot;70583&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.SATYENDRA SINGH CHAUHAN</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70629" onclick="getEmployeeIdNo(&quot;70629&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. SENTHAMIZHSELVI.A</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70620" onclick="getEmployeeIdNo(&quot;70620&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. SHAIKU SHAHIDA SAHEB</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70588" onclick="getEmployeeIdNo(&quot;70588&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. DR. S. KALYANI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70646" onclick="getEmployeeIdNo(&quot;70646&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.SONALI KAUSHIK </td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70589" onclick="getEmployeeIdNo(&quot;70589&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.SRTP SUGUNAKARA RAJU</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Visiting Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20002" onclick="getEmployeeIdNo(&quot;20002&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR S. S. SHANTHAKUMARI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70551" onclick="getEmployeeIdNo(&quot;70551&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.SUBHASIS PANDA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70626" onclick="getEmployeeIdNo(&quot;70626&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. SUHAIL AHMAD BHAT</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70586" onclick="getEmployeeIdNo(&quot;70586&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.SUMA KAMALESH GANDHIMATHI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70576" onclick="getEmployeeIdNo(&quot;70576&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.SUNIL KHOSLA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70565" onclick="getEmployeeIdNo(&quot;70565&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. SURESH DARA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70628" onclick="getEmployeeIdNo(&quot;70628&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.SURESH GARIMELLA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70637" onclick="getEmployeeIdNo(&quot;70637&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Dr.S V Kota Reddy</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Vice Chancellor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Mechanical Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70227" onclick="getEmployeeIdNo(&quot;70227&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR. TANMOY DAS</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70600" onclick="getEmployeeIdNo(&quot;70600&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.UMER MUSHTAQ LONE</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70636" onclick="getEmployeeIdNo(&quot;70636&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.VANACHARLA PUJITHA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70569" onclick="getEmployeeIdNo(&quot;70569&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> DR.VISALAKSHI ANNEPU</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70568" onclick="getEmployeeIdNo(&quot;70568&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. DWARASALA ADILAKSHMI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70672" onclick="getEmployeeIdNo(&quot;70672&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. FAROOQ AHMAD MIR</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70670" onclick="getEmployeeIdNo(&quot;70670&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> GAURAV SONIK </td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70611" onclick="getEmployeeIdNo(&quot;70611&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. GIRISH KUMAR MEKALA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70653" onclick="getEmployeeIdNo(&quot;70653&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> GOKUL YENDURI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70634" onclick="getEmployeeIdNo(&quot;70634&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Gopinath M</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70267" onclick="getEmployeeIdNo(&quot;70267&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Mr. GUNDIMEDA VENUGOPAL</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Visiting Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="40008" onclick="getEmployeeIdNo(&quot;40008&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. KAILASH CHANDRA MISHRA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70648" onclick="getEmployeeIdNo(&quot;70648&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. KALAPRAVEEN BAGADI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Senior</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70567" onclick="getEmployeeIdNo(&quot;70567&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Ms. KALYANI M</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30043" onclick="getEmployeeIdNo(&quot;30043&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. K. DEEPANJAN</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70582" onclick="getEmployeeIdNo(&quot;70582&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> KIRTIKA SAHU</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70536" onclick="getEmployeeIdNo(&quot;70536&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. KOSURI YELLARESWARARAO</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70656" onclick="getEmployeeIdNo(&quot;70656&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. KRITIKA BANSAL</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70673" onclick="getEmployeeIdNo(&quot;70673&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> KSHAMA PANDEY</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70537" onclick="getEmployeeIdNo(&quot;70537&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. K SRINIVAS</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70527" onclick="getEmployeeIdNo(&quot;70527&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Ms. LOGANATHAN PAVITHRA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70681" onclick="getEmployeeIdNo(&quot;70681&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. MANISHA CHOWDHURY</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70678" onclick="getEmployeeIdNo(&quot;70678&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Mr. MANOJ D</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30042" onclick="getEmployeeIdNo(&quot;30042&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. MO FAHEEM</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70658" onclick="getEmployeeIdNo(&quot;70658&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. MOUMITA SAHA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70659" onclick="getEmployeeIdNo(&quot;70659&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. M. RAMMOHAN</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Visiting Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="40007" onclick="getEmployeeIdNo(&quot;40007&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> MS ANJALI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70543" onclick="getEmployeeIdNo(&quot;70543&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Ms.Chafle Pratiksha Vasantrao</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70255" onclick="getEmployeeIdNo(&quot;70255&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Ms.Jyothisri Vadlamudi</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70260" onclick="getEmployeeIdNo(&quot;70260&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> MS. MALAVIKA GANTA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70566" onclick="getEmployeeIdNo(&quot;70566&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Ms.Mamatha Bandaru</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70257" onclick="getEmployeeIdNo(&quot;70257&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Ms.Pidaparthy Vijaya</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70258" onclick="getEmployeeIdNo(&quot;70258&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Ms.Sravani Sravanam</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70259" onclick="getEmployeeIdNo(&quot;70259&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. NARESH BABU MUDDHANGALA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70676" onclick="getEmployeeIdNo(&quot;70676&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> NAVANEETHAKRISHNAN K</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT Business School</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70603" onclick="getEmployeeIdNo(&quot;70603&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. NEELIMA ADAPA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70377" onclick="getEmployeeIdNo(&quot;70377&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Ms. NIDHI NAIR</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70668" onclick="getEmployeeIdNo(&quot;70668&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Ms. NIVETHA J</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30044" onclick="getEmployeeIdNo(&quot;30044&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. PEMA CHODEN BHUTIA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70654" onclick="getEmployeeIdNo(&quot;70654&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Ms. POSHAM UPPAMMA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70667" onclick="getEmployeeIdNo(&quot;70667&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Mr. PRADEEP B</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30040" onclick="getEmployeeIdNo(&quot;30040&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> PRANAV ANAND OJHA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70530" onclick="getEmployeeIdNo(&quot;70530&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. PREMKUMAR CHITHALURU</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70651" onclick="getEmployeeIdNo(&quot;70651&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. PRIYANKA SINGH</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70649" onclick="getEmployeeIdNo(&quot;70649&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.ABBARAPU ASHOK</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20017" onclick="getEmployeeIdNo(&quot;20017&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Abdul Kayom MD Khairuzzaman</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70447" onclick="getEmployeeIdNo(&quot;70447&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.ABHISHEK THOMMANDRU</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70339" onclick="getEmployeeIdNo(&quot;70339&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Aby Abraham</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70464" onclick="getEmployeeIdNo(&quot;70464&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Aditya Muppa</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="40003" onclick="getEmployeeIdNo(&quot;40003&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Afzal Hussain Shahid</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70310" onclick="getEmployeeIdNo(&quot;70310&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Agam Das Goswami</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70164" onclick="getEmployeeIdNo(&quot;70164&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Ajay Dagar</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70418" onclick="getEmployeeIdNo(&quot;70418&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. PROF.AJITH JUBILSON E</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70029" onclick="getEmployeeIdNo(&quot;70029&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof. Akhila</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30008" onclick="getEmployeeIdNo(&quot;30008&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Amar Wayal</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70491" onclick="getEmployeeIdNo(&quot;70491&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Ambuj Sharma</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Senior</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Mechanical Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70069" onclick="getEmployeeIdNo(&quot;70069&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Ameet Chavan</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70486" onclick="getEmployeeIdNo(&quot;70486&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Anamika Lata</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70477" onclick="getEmployeeIdNo(&quot;70477&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Anil Negi</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70156" onclick="getEmployeeIdNo(&quot;70156&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Anil Vitthalrao Turukmane</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70487" onclick="getEmployeeIdNo(&quot;70487&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Anindita Shome</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70370" onclick="getEmployeeIdNo(&quot;70370&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Ankita Swetaparna</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70353" onclick="getEmployeeIdNo(&quot;70353&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.ANKIT DUBEY</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20030" onclick="getEmployeeIdNo(&quot;20030&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Ann Mary George</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70463" onclick="getEmployeeIdNo(&quot;70463&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Anoop Kumar Mishra</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Senior</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70060" onclick="getEmployeeIdNo(&quot;70060&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Anupama A.P</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70430" onclick="getEmployeeIdNo(&quot;70430&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.APARAJITA MISHRA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20035" onclick="getEmployeeIdNo(&quot;20035&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.APSAL AHAMED K</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20020" onclick="getEmployeeIdNo(&quot;20020&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. Prof.Aravapalli Rama Satish</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70103" onclick="getEmployeeIdNo(&quot;70103&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Archana Tiwari</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70424" onclick="getEmployeeIdNo(&quot;70424&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Arenkala Kichu</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70212" onclick="getEmployeeIdNo(&quot;70212&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Arikumar K S </td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70470" onclick="getEmployeeIdNo(&quot;70470&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Arindam Dey</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70369" onclick="getEmployeeIdNo(&quot;70369&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Arpana Venu</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70408" onclick="getEmployeeIdNo(&quot;70408&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Arunkumar  Balakrishnan</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70503" onclick="getEmployeeIdNo(&quot;70503&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Arun Kumar Sinha</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70063" onclick="getEmployeeIdNo(&quot;70063&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Arunkumar Sivakumar</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70429" onclick="getEmployeeIdNo(&quot;70429&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Arun Kumar Yadav</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70441" onclick="getEmployeeIdNo(&quot;70441&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Ashish Gupta</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70443" onclick="getEmployeeIdNo(&quot;70443&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.ASHUTOSH PANDEY</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20018" onclick="getEmployeeIdNo(&quot;20018&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Asish Kumar Dalai</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70054" onclick="getEmployeeIdNo(&quot;70054&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Asraar Ahmed K A</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70472" onclick="getEmployeeIdNo(&quot;70472&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Aswathy R K</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70285" onclick="getEmployeeIdNo(&quot;70285&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof Athithyan M</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30004" onclick="getEmployeeIdNo(&quot;30004&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Atul Shankar Mani Tripathi</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70414" onclick="getEmployeeIdNo(&quot;70414&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Avadhesh Kumar</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70398" onclick="getEmployeeIdNo(&quot;70398&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Avin Tiwari</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70413" onclick="getEmployeeIdNo(&quot;70413&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof. Azees Maria John Francis</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70448" onclick="getEmployeeIdNo(&quot;70448&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.BANOTH VASU NAIK</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70335" onclick="getEmployeeIdNo(&quot;70335&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Bappadittya Roy</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70163" onclick="getEmployeeIdNo(&quot;70163&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Benarji Chakka</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70169" onclick="getEmployeeIdNo(&quot;70169&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. Prof.Bharathi V C</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70466" onclick="getEmployeeIdNo(&quot;70466&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Bharath Reddy Gudibandi </td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70446" onclick="getEmployeeIdNo(&quot;70446&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof. Bhavya</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30018" onclick="getEmployeeIdNo(&quot;30018&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Bibhab Bandhu Majumdar</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70454" onclick="getEmployeeIdNo(&quot;70454&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.BITRA JAYALAKSHMI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70336" onclick="getEmployeeIdNo(&quot;70336&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Bolem Sai Chandana</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70371" onclick="getEmployeeIdNo(&quot;70371&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Bommareddy Lokesh</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70479" onclick="getEmployeeIdNo(&quot;70479&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.BRIJENDRA KUMAR CHAURASIYA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20023" onclick="getEmployeeIdNo(&quot;20023&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Carlin Pouamou</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor (Junior)</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70095" onclick="getEmployeeIdNo(&quot;70095&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.CA Sudhir Shenoy</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="40001" onclick="getEmployeeIdNo(&quot;40001&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.CA Supriya Ballal</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="40002" onclick="getEmployeeIdNo(&quot;40002&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Chandan Kumar Pandey</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70155" onclick="getEmployeeIdNo(&quot;70155&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Chandan Kumar Thakur</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70153" onclick="getEmployeeIdNo(&quot;70153&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Chandan Nayak</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70396" onclick="getEmployeeIdNo(&quot;70396&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Chandan Vishwas</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70189" onclick="getEmployeeIdNo(&quot;70189&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.CHANDINI MUTTA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70345" onclick="getEmployeeIdNo(&quot;70345&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Chandu D S</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70196" onclick="getEmployeeIdNo(&quot;70196&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Ch Deepak</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Senior</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70059" onclick="getEmployeeIdNo(&quot;70059&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Chillu Naresh</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70492" onclick="getEmployeeIdNo(&quot;70492&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Chirra Venkata Ramireddy</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70459" onclick="getEmployeeIdNo(&quot;70459&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Chitti Amrita Gulshan</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70148" onclick="getEmployeeIdNo(&quot;70148&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.C Siva Kumar Reddy</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70382" onclick="getEmployeeIdNo(&quot;70382&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Dasaradha Ramarao</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70516" onclick="getEmployeeIdNo(&quot;70516&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Dasari Venkata Lakshmi</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70308" onclick="getEmployeeIdNo(&quot;70308&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Davala Ravi Kumar</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70357" onclick="getEmployeeIdNo(&quot;70357&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Debajit Goswami</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70058" onclick="getEmployeeIdNo(&quot;70058&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Debakanta Tripathy</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70373" onclick="getEmployeeIdNo(&quot;70373&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Debanjali Sarkar</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70489" onclick="getEmployeeIdNo(&quot;70489&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.DEBASISH MISHRA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20009" onclick="getEmployeeIdNo(&quot;20009&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Deepasikha Mishra</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70034" onclick="getEmployeeIdNo(&quot;70034&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Deepjoy Katuwal</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70201" onclick="getEmployeeIdNo(&quot;70201&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Deepthi Godavarthi</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70505" onclick="getEmployeeIdNo(&quot;70505&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.DEVANGAM BANGARU RAJESH</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20042" onclick="getEmployeeIdNo(&quot;20042&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Devarakonda Nagaraju</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70104" onclick="getEmployeeIdNo(&quot;70104&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.DHAWLATH G</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20022" onclick="getEmployeeIdNo(&quot;20022&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Dheeraj Kumar</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor (Junior)</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70379" onclick="getEmployeeIdNo(&quot;70379&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Dilip Kumar  Mohanty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Mechanical Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70016" onclick="getEmployeeIdNo(&quot;70016&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Divya Bora</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30032" onclick="getEmployeeIdNo(&quot;30032&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Divya Meena Sundaram</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70290" onclick="getEmployeeIdNo(&quot;70290&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.D Khasim Vali</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70462" onclick="getEmployeeIdNo(&quot;70462&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Dripta De Joarder</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70381" onclick="getEmployeeIdNo(&quot;70381&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Eswaraiah Rayachoti</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70391" onclick="getEmployeeIdNo(&quot;70391&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Ethnus Faculty-4</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30020" onclick="getEmployeeIdNo(&quot;30020&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Faizan Danish</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70460" onclick="getEmployeeIdNo(&quot;70460&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Francis P</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70405" onclick="getEmployeeIdNo(&quot;70405&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.GANDIKOTA NAGA CHANDRIKA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70346" onclick="getEmployeeIdNo(&quot;70346&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Ganesh Kotagiri</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70452" onclick="getEmployeeIdNo(&quot;70452&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.GANESH KUMAR M</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70332" onclick="getEmployeeIdNo(&quot;70332&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Ganesh Reddy Karri</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Senior</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70140" onclick="getEmployeeIdNo(&quot;70140&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Gauranga Mandal</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70351" onclick="getEmployeeIdNo(&quot;70351&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Gopikrishnan S</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70107" onclick="getEmployeeIdNo(&quot;70107&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.GUDLURU RAMA DEVI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20029" onclick="getEmployeeIdNo(&quot;20029&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.GULLINKALA RAMYA VENKATA TRIVENI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20041" onclick="getEmployeeIdNo(&quot;20041&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof Hariharan</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30003" onclick="getEmployeeIdNo(&quot;30003&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Hari Kishan Kondaveeti</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70071" onclick="getEmployeeIdNo(&quot;70071&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Hari Seetha</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70003" onclick="getEmployeeIdNo(&quot;70003&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof Harshavardhan</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30027" onclick="getEmployeeIdNo(&quot;30027&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. Prof.Hemant Kumar Reddy</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70493" onclick="getEmployeeIdNo(&quot;70493&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Hussain Ahmed Choudhury</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70309" onclick="getEmployeeIdNo(&quot;70309&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Hussain Syed</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70032" onclick="getEmployeeIdNo(&quot;70032&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Illa Ramakanth</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70440" onclick="getEmployeeIdNo(&quot;70440&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Jagadish Chandra Mudiganti</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70014" onclick="getEmployeeIdNo(&quot;70014&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Jayendra Kumar</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Senior</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70077" onclick="getEmployeeIdNo(&quot;70077&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof. Jesmitha</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30009" onclick="getEmployeeIdNo(&quot;30009&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.John Pradeep  Darsy</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70007" onclick="getEmployeeIdNo(&quot;70007&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Jonnadula Harikiran</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70110" onclick="getEmployeeIdNo(&quot;70110&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Joseph Alugula</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70511" onclick="getEmployeeIdNo(&quot;70511&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Kalyan Chakravarthi  Maddikera</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor (Senior)</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70011" onclick="getEmployeeIdNo(&quot;70011&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Kamalesh Kumar</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70419" onclick="getEmployeeIdNo(&quot;70419&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Karishma Bisht</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70490" onclick="getEmployeeIdNo(&quot;70490&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Karthika Natarajan</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70279" onclick="getEmployeeIdNo(&quot;70279&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.KASMITA DEVI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20013" onclick="getEmployeeIdNo(&quot;20013&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.KATURI SRILAKSHMI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20031" onclick="getEmployeeIdNo(&quot;20031&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Khadheer Pasha SK</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70012" onclick="getEmployeeIdNo(&quot;70012&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Khairnar Vikas Vishnu</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70193" onclick="getEmployeeIdNo(&quot;70193&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.KHOSE SHUBHAM BHAUSAHEB</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20019" onclick="getEmployeeIdNo(&quot;20019&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Kingshuk Sarkar</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70365" onclick="getEmployeeIdNo(&quot;70365&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Kirubakaran </td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30016" onclick="getEmployeeIdNo(&quot;30016&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> PROF.KISHOR. E</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Mechanical Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70574" onclick="getEmployeeIdNo(&quot;70574&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.KODALI RADHA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70333" onclick="getEmployeeIdNo(&quot;70333&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Kolluri Rajesh</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70476" onclick="getEmployeeIdNo(&quot;70476&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.KOMAL GOYAL</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20014" onclick="getEmployeeIdNo(&quot;20014&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Komanapalli Gurumurthy</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70180" onclick="getEmployeeIdNo(&quot;70180&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Komandla Mahipal Reddy</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70097" onclick="getEmployeeIdNo(&quot;70097&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Koteswararao Chitipireddi</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70278" onclick="getEmployeeIdNo(&quot;70278&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Kotnana Ganesh</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70385" onclick="getEmployeeIdNo(&quot;70385&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.KSHIRSAGAR SUNIL YADAV</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20006" onclick="getEmployeeIdNo(&quot;20006&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Kumar Debasis</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70151" onclick="getEmployeeIdNo(&quot;70151&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.KUNCHE VIJAYA LAKSHMI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20004" onclick="getEmployeeIdNo(&quot;20004&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Lakhan Dev Sharma</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70178" onclick="getEmployeeIdNo(&quot;70178&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Lakshmi Sowjanya Pali</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70112" onclick="getEmployeeIdNo(&quot;70112&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Lalitha Kumari Pappala</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70277" onclick="getEmployeeIdNo(&quot;70277&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.LINGUTLA VIJAY KUMAR</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20027" onclick="getEmployeeIdNo(&quot;20027&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Lisna PC</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70145" onclick="getEmployeeIdNo(&quot;70145&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Madhusmita Mohanty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70507" onclick="getEmployeeIdNo(&quot;70507&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Madhusudhana Rao N</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70005" onclick="getEmployeeIdNo(&quot;70005&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof. Mahesh</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30006" onclick="getEmployeeIdNo(&quot;30006&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Mahesh Miriyala</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70515" onclick="getEmployeeIdNo(&quot;70515&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Mahi S Thavarathu</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70368" onclick="getEmployeeIdNo(&quot;70368&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Manas Kumar Pal</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Mechanical Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70139" onclick="getEmployeeIdNo(&quot;70139&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Manikanta Ravindra Kumar Vakkalagadda</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Senior</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Mechanical Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70092" onclick="getEmployeeIdNo(&quot;70092&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Manisha Maity</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70198" onclick="getEmployeeIdNo(&quot;70198&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Manish Kumar Singh</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70478" onclick="getEmployeeIdNo(&quot;70478&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Manmadha Rao Banki</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70089" onclick="getEmployeeIdNo(&quot;70089&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof. Manoj</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30019" onclick="getEmployeeIdNo(&quot;30019&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Manoj Kumar Gupta</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Senior</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Mechanical Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70082" onclick="getEmployeeIdNo(&quot;70082&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Manoj Kumar Mishra</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70064" onclick="getEmployeeIdNo(&quot;70064&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Manomita Chakraborty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70296" onclick="getEmployeeIdNo(&quot;70296&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.MEDHA KUMARI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20015" onclick="getEmployeeIdNo(&quot;20015&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.MEDISETTY PADMA DEVI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70314" onclick="getEmployeeIdNo(&quot;70314&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.MIRIYALA NAVYA PRATYUSHA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20024" onclick="getEmployeeIdNo(&quot;20024&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.M. Krishnasamy</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70496" onclick="getEmployeeIdNo(&quot;70496&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.M. Muneeswaran</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70519" onclick="getEmployeeIdNo(&quot;70519&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.MOHAMMED ZUBAIR AHAMED</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20021" onclick="getEmployeeIdNo(&quot;20021&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Mohd Abdul Muqeet Maaz</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70499" onclick="getEmployeeIdNo(&quot;70499&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Monali Bordoloi </td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70294" onclick="getEmployeeIdNo(&quot;70294&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Moru Satyanarayana</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70485" onclick="getEmployeeIdNo(&quot;70485&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.M S Jagadeesh</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70403" onclick="getEmployeeIdNo(&quot;70403&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.M SNEHITHA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Registrar</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70338" onclick="getEmployeeIdNo(&quot;70338&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Mukkoti Maruthi Venkata Chalapathi</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70469" onclick="getEmployeeIdNo(&quot;70469&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.MUKKU PAVAN KUMAR</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70330" onclick="getEmployeeIdNo(&quot;70330&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof Musthaq</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30026" onclick="getEmployeeIdNo(&quot;30026&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Muthu Krishnammal</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70434" onclick="getEmployeeIdNo(&quot;70434&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.M. VIJAYA LAKSHMI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20012" onclick="getEmployeeIdNo(&quot;20012&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Nadiminti Nagamani</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70211" onclick="getEmployeeIdNo(&quot;70211&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. Prof.Naga Jagadesh Bommagani</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70436" onclick="getEmployeeIdNo(&quot;70436&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Naga Prasad.P</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70518" onclick="getEmployeeIdNo(&quot;70518&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Nagarjuna Neella</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70359" onclick="getEmployeeIdNo(&quot;70359&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Nagendra Panini Challa</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70397" onclick="getEmployeeIdNo(&quot;70397&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Nallamuthu S</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70410" onclick="getEmployeeIdNo(&quot;70410&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Nalluri Purnachand </td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Senior</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70027" onclick="getEmployeeIdNo(&quot;70027&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Nandam Ashok</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70130" onclick="getEmployeeIdNo(&quot;70130&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Nandha Kumar R</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Senior</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70079" onclick="getEmployeeIdNo(&quot;70079&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Nanduri Govinda Rao</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Mechanical Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70384" onclick="getEmployeeIdNo(&quot;70384&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Narendra Nath Dutta</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70467" onclick="getEmployeeIdNo(&quot;70467&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Naveen Kumar Cherupelly</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70409" onclick="getEmployeeIdNo(&quot;70409&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Neeraj Kumar Misra</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70442" onclick="getEmployeeIdNo(&quot;70442&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Neha Gupta</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70128" onclick="getEmployeeIdNo(&quot;70128&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Nihar Ranjan Pradhan</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70504" onclick="getEmployeeIdNo(&quot;70504&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Nusrat Begum</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70428" onclick="getEmployeeIdNo(&quot;70428&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Pandi Soundarya</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30021" onclick="getEmployeeIdNo(&quot;30021&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Pankaj Balakrishna Tambe</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Mechanical Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70009" onclick="getEmployeeIdNo(&quot;70009&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Paramasivam R</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70106" onclick="getEmployeeIdNo(&quot;70106&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.PARESH KUMAR PANIGRAHI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20007" onclick="getEmployeeIdNo(&quot;20007&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.PARNAB DAS</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20036" onclick="getEmployeeIdNo(&quot;20036&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.PATHIPATI LAKSHMI DURGA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20038" onclick="getEmployeeIdNo(&quot;20038&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Peeyush Singh</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70186" onclick="getEmployeeIdNo(&quot;70186&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.PENJARLA NAGA VENKATA NAVEEN KUMAR</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70334" onclick="getEmployeeIdNo(&quot;70334&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Perumandla Karunakar</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70439" onclick="getEmployeeIdNo(&quot;70439&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Phani Kumar Meduri</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70022" onclick="getEmployeeIdNo(&quot;70022&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Piu Kundu</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Research</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70449" onclick="getEmployeeIdNo(&quot;70449&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.POOJA VISHWAKARMA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20033" onclick="getEmployeeIdNo(&quot;20033&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof Poojitha L</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30005" onclick="getEmployeeIdNo(&quot;30005&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Ms. Prof.Pottumuthu Kanaka Himabindu</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor (Junior)</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70185" onclick="getEmployeeIdNo(&quot;70185&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Prabhakaran Thandapani</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70362" onclick="getEmployeeIdNo(&quot;70362&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Prabha Selvaraj</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70123" onclick="getEmployeeIdNo(&quot;70123&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Pradeep Reddy CH</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70008" onclick="getEmployeeIdNo(&quot;70008&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> PROF.PRADEEP SINGH</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Mechanical Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70573" onclick="getEmployeeIdNo(&quot;70573&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Pradosh Ranjan Sahoo</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70412" onclick="getEmployeeIdNo(&quot;70412&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Pragya Sen Gupta</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70086" onclick="getEmployeeIdNo(&quot;70086&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof Pranesh</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30015" onclick="getEmployeeIdNo(&quot;30015&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Prashanth Maroju</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70197" onclick="getEmployeeIdNo(&quot;70197&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Prashanth Ragam</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70438" onclick="getEmployeeIdNo(&quot;70438&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Pratheep Kumar</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70421" onclick="getEmployeeIdNo(&quot;70421&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Pratik Premadarshi Ray</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70191" onclick="getEmployeeIdNo(&quot;70191&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Praveen Maurya</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70425" onclick="getEmployeeIdNo(&quot;70425&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Priyanka Ghosh</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70342" onclick="getEmployeeIdNo(&quot;70342&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.P.S.Rama Sreekanth</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Mechanical Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70020" onclick="getEmployeeIdNo(&quot;70020&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Radha Mohan Pattanayak</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70475" onclick="getEmployeeIdNo(&quot;70475&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Rafael Ganzalez Macho</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70521" onclick="getEmployeeIdNo(&quot;70521&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Raghavi R K</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70194" onclick="getEmployeeIdNo(&quot;70194&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Rajarshi Sarkar</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70453" onclick="getEmployeeIdNo(&quot;70453&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Rajashekar Naraveni</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70395" onclick="getEmployeeIdNo(&quot;70395&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Rajeev Sharma</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70179" onclick="getEmployeeIdNo(&quot;70179&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Rajesh Chalasani</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70137" onclick="getEmployeeIdNo(&quot;70137&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Rajesh Duvvuru</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70388" onclick="getEmployeeIdNo(&quot;70388&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Rajesh Kandala NVPS</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70498" onclick="getEmployeeIdNo(&quot;70498&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof. Raj Kumar</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30007" onclick="getEmployeeIdNo(&quot;30007&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Rakhi N K</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70154" onclick="getEmployeeIdNo(&quot;70154&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Ramesh A</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70512" onclick="getEmployeeIdNo(&quot;70512&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Ramkumar D</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70488" onclick="getEmployeeIdNo(&quot;70488&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Ranjan Kumar</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70293" onclick="getEmployeeIdNo(&quot;70293&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Rasheda Parveen</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70062" onclick="getEmployeeIdNo(&quot;70062&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.RAVADA SIMHACHALAM</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70344" onclick="getEmployeeIdNo(&quot;70344&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Ravindra Dhuli</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70053" onclick="getEmployeeIdNo(&quot;70053&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Ravi Sankar Barpanda</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70066" onclick="getEmployeeIdNo(&quot;70066&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Reeja S R</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70306" onclick="getEmployeeIdNo(&quot;70306&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Renuprasad Hemkiran Patki</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70222" onclick="getEmployeeIdNo(&quot;70222&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Ritambhara Sharma</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70372" onclick="getEmployeeIdNo(&quot;70372&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> PROF.RITI NAIK</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70575" onclick="getEmployeeIdNo(&quot;70575&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Rohit Kumar Das</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70291" onclick="getEmployeeIdNo(&quot;70291&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Rohit Lorenzo</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70161" onclick="getEmployeeIdNo(&quot;70161&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Roopas Kiran  Sirugudu</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70031" onclick="getEmployeeIdNo(&quot;70031&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Sabeel M Basheer</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70159" onclick="getEmployeeIdNo(&quot;70159&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Sachil Sharma</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70427" onclick="getEmployeeIdNo(&quot;70427&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. Prof.Sachi Nandan Mohanty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70455" onclick="getEmployeeIdNo(&quot;70455&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Saladi Saritha</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70461" onclick="getEmployeeIdNo(&quot;70461&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Sambhudutta Nanda</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70514" onclick="getEmployeeIdNo(&quot;70514&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Sameeulla Khan Md</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Senior</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70061" onclick="getEmployeeIdNo(&quot;70061&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Samineni Peddakrishna</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70105" onclick="getEmployeeIdNo(&quot;70105&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SANA ABDULLA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20034" onclick="getEmployeeIdNo(&quot;20034&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Sandhya Sadanandan</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70509" onclick="getEmployeeIdNo(&quot;70509&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Sandipan Maiti</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70125" onclick="getEmployeeIdNo(&quot;70125&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof Sanjay S</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30025" onclick="getEmployeeIdNo(&quot;30025&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Sanjit Chakraborty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70411" onclick="getEmployeeIdNo(&quot;70411&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Sanket Mishra</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70217" onclick="getEmployeeIdNo(&quot;70217&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Santosh Kumar Sahu</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Mechanical Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70471" onclick="getEmployeeIdNo(&quot;70471&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Santunu Mandal</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70030" onclick="getEmployeeIdNo(&quot;70030&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Saroj Kumar Panigrahy</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Senior</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70051" onclick="getEmployeeIdNo(&quot;70051&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SAS CHY  Faculty-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70727" onclick="getEmployeeIdNo(&quot;70727&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SAS CHY  Faculty-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70728" onclick="getEmployeeIdNo(&quot;70728&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SAS CHY  Faculty-3</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70729" onclick="getEmployeeIdNo(&quot;70729&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SAS CHY  Faculty-4</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70730" onclick="getEmployeeIdNo(&quot;70730&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SAS CHY  Faculty-5</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70741" onclick="getEmployeeIdNo(&quot;70741&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SAS Dig Crs Faculty-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80021" onclick="getEmployeeIdNo(&quot;80021&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SAS Dig Crs Faculty-10</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80030" onclick="getEmployeeIdNo(&quot;80030&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SAS Dig Crs Faculty-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80022" onclick="getEmployeeIdNo(&quot;80022&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SAS Dig Crs Faculty-3</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80023" onclick="getEmployeeIdNo(&quot;80023&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SAS Dig Crs Faculty-4</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80024" onclick="getEmployeeIdNo(&quot;80024&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SAS Dig Crs Faculty-5</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80025" onclick="getEmployeeIdNo(&quot;80025&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SAS Dig Crs Faculty-6</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80026" onclick="getEmployeeIdNo(&quot;80026&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SAS Dig Crs Faculty-7</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80027" onclick="getEmployeeIdNo(&quot;80027&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SAS Dig Crs Faculty-8</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80028" onclick="getEmployeeIdNo(&quot;80028&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SAS Dig Crs Faculty-9</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80029" onclick="getEmployeeIdNo(&quot;80029&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.S.ASHA VARMA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70319" onclick="getEmployeeIdNo(&quot;70319&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SAS PHY  Faculty-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70722" onclick="getEmployeeIdNo(&quot;70722&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SAS PHY  Faculty-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70723" onclick="getEmployeeIdNo(&quot;70723&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SAS PHY  Faculty-3</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70724" onclick="getEmployeeIdNo(&quot;70724&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SAS PHY  Faculty-4</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70725" onclick="getEmployeeIdNo(&quot;70725&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SAS PHY  Faculty-5</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70726" onclick="getEmployeeIdNo(&quot;70726&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Satyanaryana Badeti</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70006" onclick="getEmployeeIdNo(&quot;70006&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Sayyed Faizan Ali</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70501" onclick="getEmployeeIdNo(&quot;70501&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SCOPE Dig Crs Faculty-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80001" onclick="getEmployeeIdNo(&quot;80001&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SCOPE Dig Crs Faculty-10</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80010" onclick="getEmployeeIdNo(&quot;80010&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SCOPE Dig Crs Faculty-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80002" onclick="getEmployeeIdNo(&quot;80002&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SCOPE Dig Crs Faculty-3</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80003" onclick="getEmployeeIdNo(&quot;80003&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SCOPE Dig Crs Faculty-4</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80004" onclick="getEmployeeIdNo(&quot;80004&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SCOPE Dig Crs Faculty-5</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80005" onclick="getEmployeeIdNo(&quot;80005&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SCOPE Dig Crs Faculty-6</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80006" onclick="getEmployeeIdNo(&quot;80006&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SCOPE Dig Crs Faculty-7</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80007" onclick="getEmployeeIdNo(&quot;80007&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SCOPE Dig Crs Faculty-8</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80008" onclick="getEmployeeIdNo(&quot;80008&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SCOPE Dig Crs Faculty-9</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80009" onclick="getEmployeeIdNo(&quot;80009&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SCOPE  Faculty-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor (Junior)</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70701" onclick="getEmployeeIdNo(&quot;70701&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SCOPE  Faculty-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor (Junior)</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70702" onclick="getEmployeeIdNo(&quot;70702&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SCOPE  Faculty-3</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor (Junior)</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70703" onclick="getEmployeeIdNo(&quot;70703&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SCOPE  Faculty-4</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor (Junior)</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70704" onclick="getEmployeeIdNo(&quot;70704&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SCOPE  Faculty-5</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor (Junior)</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70705" onclick="getEmployeeIdNo(&quot;70705&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SCOPE  Faculty-6</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70721" onclick="getEmployeeIdNo(&quot;70721&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Selvakumar Karuthapandi</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Senior</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70119" onclick="getEmployeeIdNo(&quot;70119&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Selva Kumar S</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70401" onclick="getEmployeeIdNo(&quot;70401&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SENSE Dig Crs Faculty-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80011" onclick="getEmployeeIdNo(&quot;80011&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SENSE Dig Crs Faculty-10</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80020" onclick="getEmployeeIdNo(&quot;80020&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SENSE Dig Crs Faculty-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80012" onclick="getEmployeeIdNo(&quot;80012&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SENSE Dig Crs Faculty-3</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80013" onclick="getEmployeeIdNo(&quot;80013&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SENSE Dig Crs Faculty-4</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80014" onclick="getEmployeeIdNo(&quot;80014&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SENSE Dig Crs Faculty-5</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80015" onclick="getEmployeeIdNo(&quot;80015&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SENSE Dig Crs Faculty-6</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80016" onclick="getEmployeeIdNo(&quot;80016&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SENSE Dig Crs Faculty-7</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80017" onclick="getEmployeeIdNo(&quot;80017&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SENSE Dig Crs Faculty-8</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80018" onclick="getEmployeeIdNo(&quot;80018&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SENSE Dig Crs Faculty-9</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80019" onclick="getEmployeeIdNo(&quot;80019&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Senthil K</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70400" onclick="getEmployeeIdNo(&quot;70400&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Senthil Murugan</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70276" onclick="getEmployeeIdNo(&quot;70276&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SHACHI SHAMBHAVI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70337" onclick="getEmployeeIdNo(&quot;70337&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Shaik Kareemulla</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70474" onclick="getEmployeeIdNo(&quot;70474&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SHAIK KHALEEL PASHA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Mechanical Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70349" onclick="getEmployeeIdNo(&quot;70349&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Shalini Thakur</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70118" onclick="getEmployeeIdNo(&quot;70118&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Sheela Jayachandran</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70280" onclick="getEmployeeIdNo(&quot;70280&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Sheik Noushad</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30035" onclick="getEmployeeIdNo(&quot;30035&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof Shekar</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30012" onclick="getEmployeeIdNo(&quot;30012&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SHUBHAM KUMAR TRIPATHI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20032" onclick="getEmployeeIdNo(&quot;20032&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SHUBHAM SINGH</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20028" onclick="getEmployeeIdNo(&quot;20028&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Shubhra Ghoshal</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70376" onclick="getEmployeeIdNo(&quot;70376&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Sibi Chakkaravarthy S</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Senior</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70084" onclick="getEmployeeIdNo(&quot;70084&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Siddique Ibrahim Peer Mohamed</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70399" onclick="getEmployeeIdNo(&quot;70399&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Sinuvasan R</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70116" onclick="getEmployeeIdNo(&quot;70116&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof Sivalingam</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30014" onclick="getEmployeeIdNo(&quot;30014&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Sivarama Krishna Pillutla</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70422" onclick="getEmployeeIdNo(&quot;70422&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Six Phrase Faculty-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30031" onclick="getEmployeeIdNo(&quot;30031&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Six Phrase Faculty-6</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30036" onclick="getEmployeeIdNo(&quot;30036&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Six Phrase Faculty-7</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30037" onclick="getEmployeeIdNo(&quot;30037&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Six Phrase Faculty-8</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30038" onclick="getEmployeeIdNo(&quot;30038&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Six Phrase Faculty-9</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30039" onclick="getEmployeeIdNo(&quot;30039&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SMEC Dig Crs Faculty-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Mechanical Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80061" onclick="getEmployeeIdNo(&quot;80061&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SMEC Dig Crs Faculty-10</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Mechanical Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80070" onclick="getEmployeeIdNo(&quot;80070&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SMEC Dig Crs Faculty-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Mechanical Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80062" onclick="getEmployeeIdNo(&quot;80062&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SMEC Dig Crs Faculty-3</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Mechanical Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80063" onclick="getEmployeeIdNo(&quot;80063&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SMEC Dig Crs Faculty-4</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Mechanical Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80064" onclick="getEmployeeIdNo(&quot;80064&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SMEC Dig Crs Faculty-5</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Mechanical Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80065" onclick="getEmployeeIdNo(&quot;80065&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SMEC Dig Crs Faculty-6</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Mechanical Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80066" onclick="getEmployeeIdNo(&quot;80066&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SMEC Dig Crs Faculty-7</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Mechanical Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80067" onclick="getEmployeeIdNo(&quot;80067&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SMEC Dig Crs Faculty-8</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Mechanical Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80068" onclick="getEmployeeIdNo(&quot;80068&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SMEC Dig Crs Faculty-9</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Mechanical Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80069" onclick="getEmployeeIdNo(&quot;80069&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SNEHALATA JENA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20016" onclick="getEmployeeIdNo(&quot;20016&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Somya Ranjan Sahoo</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70167" onclick="getEmployeeIdNo(&quot;70167&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SOUBHAGYA SANKAR BARPANDA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70023" onclick="getEmployeeIdNo(&quot;70023&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof Soumendra Chakravarthy</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30001" onclick="getEmployeeIdNo(&quot;30001&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Soumen Kundu</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70450" onclick="getEmployeeIdNo(&quot;70450&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Soumyakanta Prusty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70176" onclick="getEmployeeIdNo(&quot;70176&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.S Priyanka</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70415" onclick="getEmployeeIdNo(&quot;70415&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SRILATHA RAAVI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20025" onclick="getEmployeeIdNo(&quot;20025&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Srinivasa Reddy Konda</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70517" onclick="getEmployeeIdNo(&quot;70517&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Srinivas S</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Higher Academic Grade</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70004" onclick="getEmployeeIdNo(&quot;70004&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SRINU IRUGULA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20026" onclick="getEmployeeIdNo(&quot;20026&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.S.Sudhakar Ilango</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70087" onclick="getEmployeeIdNo(&quot;70087&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.S Sudheer Mangalampalli</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70393" onclick="getEmployeeIdNo(&quot;70393&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Subhasish Mahapatra</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70183" onclick="getEmployeeIdNo(&quot;70183&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SUBHASREE PANDA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70315" onclick="getEmployeeIdNo(&quot;70315&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Sucharitha Jackson</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70435" onclick="getEmployeeIdNo(&quot;70435&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Sudesh Manger</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70109" onclick="getEmployeeIdNo(&quot;70109&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Sudha Ellison Mathe</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Senior</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70078" onclick="getEmployeeIdNo(&quot;70078&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Sudhakar Matle</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70015" onclick="getEmployeeIdNo(&quot;70015&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof. Sudharshan</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30017" onclick="getEmployeeIdNo(&quot;30017&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SUDIPTA PRIYADARSHINI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20008" onclick="getEmployeeIdNo(&quot;20008&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.SUGUNAKAR MAMIDALA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70343" onclick="getEmployeeIdNo(&quot;70343&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Sukanta Nayak</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70305" onclick="getEmployeeIdNo(&quot;70305&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof Sumanth</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30013" onclick="getEmployeeIdNo(&quot;30013&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof Sumanth</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30011" onclick="getEmployeeIdNo(&quot;30011&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Sumathi D</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70122" onclick="getEmployeeIdNo(&quot;70122&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Sumesh E P</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70510" onclick="getEmployeeIdNo(&quot;70510&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Sunil Kumar Singh</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70135" onclick="getEmployeeIdNo(&quot;70135&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Sunkesula Moulana Abdul Kalam Azad</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70134" onclick="getEmployeeIdNo(&quot;70134&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Sunny Dayal Vanambathina</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Senior</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70090" onclick="getEmployeeIdNo(&quot;70090&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Surendra Reddy Vinta</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70482" onclick="getEmployeeIdNo(&quot;70482&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Suresh Jagannadham</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70358" onclick="getEmployeeIdNo(&quot;70358&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Suseela Vappangi</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70182" onclick="getEmployeeIdNo(&quot;70182&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Suyog Jhavar</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Mechanical Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70386" onclick="getEmployeeIdNo(&quot;70386&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Swati Shukla</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70513" onclick="getEmployeeIdNo(&quot;70513&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof. Syed</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30010" onclick="getEmployeeIdNo(&quot;30010&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Syed Khasim</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70457" onclick="getEmployeeIdNo(&quot;70457&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.TALAPAPHULA JAYANTH</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20040" onclick="getEmployeeIdNo(&quot;20040&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Tannishta Das gupta</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70083" onclick="getEmployeeIdNo(&quot;70083&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Tauseef Khan</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70522" onclick="getEmployeeIdNo(&quot;70522&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.THIRUMALESH NIZAMPATNAM</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70340" onclick="getEmployeeIdNo(&quot;70340&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.T Ramana</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70524" onclick="getEmployeeIdNo(&quot;70524&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Triveni Rajashekhar Mandlimath</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70420" onclick="getEmployeeIdNo(&quot;70420&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Tufan Ghosh</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70127" onclick="getEmployeeIdNo(&quot;70127&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Udit Narayana Kar </td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70281" onclick="getEmployeeIdNo(&quot;70281&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.UJJAWALA SINGH</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20005" onclick="getEmployeeIdNo(&quot;20005&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Umakanta Nanda</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Senior</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70055" onclick="getEmployeeIdNo(&quot;70055&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.UMESH UTTAMRAO SHINDE</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20010" onclick="getEmployeeIdNo(&quot;20010&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.U M Gopala Krishna</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70481" onclick="getEmployeeIdNo(&quot;70481&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Usha Seshadri</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70114" onclick="getEmployeeIdNo(&quot;70114&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VANA RAMBABU</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20037" onclick="getEmployeeIdNo(&quot;20037&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Varunkumar Merugu</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70431" onclick="getEmployeeIdNo(&quot;70431&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Vasili Bala Venkata Nagarjuna</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70508" onclick="getEmployeeIdNo(&quot;70508&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Vatambeti Ramesh</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70473" onclick="getEmployeeIdNo(&quot;70473&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.V Balasingh</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70361" onclick="getEmployeeIdNo(&quot;70361&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Vemula Ramakrishna Reddy</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70098" onclick="getEmployeeIdNo(&quot;70098&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Venkatarajam M</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70041" onclick="getEmployeeIdNo(&quot;70041&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Venkata Rajanikanth Machavaram</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70383" onclick="getEmployeeIdNo(&quot;70383&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Venkata Rajasekhar Nuthakki</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Senior</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70081" onclick="getEmployeeIdNo(&quot;70081&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Vikash Kumar Singh</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70202" onclick="getEmployeeIdNo(&quot;70202&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VIKASH KUMAR SINHA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20011" onclick="getEmployeeIdNo(&quot;20011&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Vikram </td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30022" onclick="getEmployeeIdNo(&quot;30022&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Vinod Kiran K</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70506" onclick="getEmployeeIdNo(&quot;70506&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof Vinu Raj</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30002" onclick="getEmployeeIdNo(&quot;30002&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Virendra Kumar Verma</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70445" onclick="getEmployeeIdNo(&quot;70445&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VISH Dig Crs Faculty-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80031" onclick="getEmployeeIdNo(&quot;80031&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VISH Dig Crs Faculty-10</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80040" onclick="getEmployeeIdNo(&quot;80040&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VISH Dig Crs Faculty-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80032" onclick="getEmployeeIdNo(&quot;80032&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VISH Dig Crs Faculty-3</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80033" onclick="getEmployeeIdNo(&quot;80033&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VISH Dig Crs Faculty-4</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80034" onclick="getEmployeeIdNo(&quot;80034&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VISH Dig Crs Faculty-5</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80035" onclick="getEmployeeIdNo(&quot;80035&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VISH Dig Crs Faculty-6</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80036" onclick="getEmployeeIdNo(&quot;80036&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VISH Dig Crs Faculty-7</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80037" onclick="getEmployeeIdNo(&quot;80037&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VISH Dig Crs Faculty-8</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80038" onclick="getEmployeeIdNo(&quot;80038&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VISH Dig Crs Faculty-9</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80039" onclick="getEmployeeIdNo(&quot;80039&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VISH  Faculty-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70745" onclick="getEmployeeIdNo(&quot;70745&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VISH  Faculty-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70746" onclick="getEmployeeIdNo(&quot;70746&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VISH  Faculty-3</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70747" onclick="getEmployeeIdNo(&quot;70747&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VISH  Faculty-4</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70748" onclick="getEmployeeIdNo(&quot;70748&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VISH  Faculty-5</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70749" onclick="getEmployeeIdNo(&quot;70749&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VSB Dig Crs Faculty-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80041" onclick="getEmployeeIdNo(&quot;80041&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VSB Dig Crs Faculty-10</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80050" onclick="getEmployeeIdNo(&quot;80050&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VSB Dig Crs Faculty-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80042" onclick="getEmployeeIdNo(&quot;80042&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VSB Dig Crs Faculty-3</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80043" onclick="getEmployeeIdNo(&quot;80043&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VSB Dig Crs Faculty-4</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80044" onclick="getEmployeeIdNo(&quot;80044&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VSB Dig Crs Faculty-5</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80045" onclick="getEmployeeIdNo(&quot;80045&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VSB Dig Crs Faculty-6</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80046" onclick="getEmployeeIdNo(&quot;80046&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VSB Dig Crs Faculty-7</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80047" onclick="getEmployeeIdNo(&quot;80047&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VSB Dig Crs Faculty-8</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80048" onclick="getEmployeeIdNo(&quot;80048&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VSB Dig Crs Faculty-9</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80049" onclick="getEmployeeIdNo(&quot;80049&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VSB  Faculty-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70742" onclick="getEmployeeIdNo(&quot;70742&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VSB  Faculty-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70743" onclick="getEmployeeIdNo(&quot;70743&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VSB  Faculty-3</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Business</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70744" onclick="getEmployeeIdNo(&quot;70744&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VSL Dig Crs Faculty-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80051" onclick="getEmployeeIdNo(&quot;80051&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VSL Dig Crs Faculty-10</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80060" onclick="getEmployeeIdNo(&quot;80060&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VSL Dig Crs Faculty-2</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80052" onclick="getEmployeeIdNo(&quot;80052&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VSL Dig Crs Faculty-3</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80053" onclick="getEmployeeIdNo(&quot;80053&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VSL Dig Crs Faculty-4</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80054" onclick="getEmployeeIdNo(&quot;80054&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VSL Dig Crs Faculty-5</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80055" onclick="getEmployeeIdNo(&quot;80055&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VSL Dig Crs Faculty-6</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80056" onclick="getEmployeeIdNo(&quot;80056&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VSL Dig Crs Faculty-7</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80057" onclick="getEmployeeIdNo(&quot;80057&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VSL Dig Crs Faculty-8</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80058" onclick="getEmployeeIdNo(&quot;80058&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.VSL Dig Crs Faculty-9</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="80059" onclick="getEmployeeIdNo(&quot;80059&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.V V Sreenivasu M</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70387" onclick="getEmployeeIdNo(&quot;70387&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Yada NanduKumar</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70192" onclick="getEmployeeIdNo(&quot;70192&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Yamarthi Narasimha Rao</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Professor Grade - 1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70465" onclick="getEmployeeIdNo(&quot;70465&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Yamini Durga</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30033" onclick="getEmployeeIdNo(&quot;30033&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Y.Mary Chandini</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Emeritus Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70456" onclick="getEmployeeIdNo(&quot;70456&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Y Mohamed Sirajudeen</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70389" onclick="getEmployeeIdNo(&quot;70389&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.YUVA RAJA BODU</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20039" onclick="getEmployeeIdNo(&quot;20039&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Prof.Y V Pavan Kumar</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Senior</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70049" onclick="getEmployeeIdNo(&quot;70049&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. RAJAN DEORAO LANJEKAR</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Mechanical Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70662" onclick="getEmployeeIdNo(&quot;70662&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> RAMA DEVI KALLURI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - T &amp; Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70246" onclick="getEmployeeIdNo(&quot;70246&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> RAMESH PRASAD PANDA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70538" onclick="getEmployeeIdNo(&quot;70538&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. SANE UMESH REDDY</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70674" onclick="getEmployeeIdNo(&quot;70674&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. SATPAL SINGH</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70661" onclick="getEmployeeIdNo(&quot;70661&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. SATRI VEERA KESALU</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70679" onclick="getEmployeeIdNo(&quot;70679&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. S.BHARATH BHUSHAN</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70655" onclick="getEmployeeIdNo(&quot;70655&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. SHAZIA SABIR</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70666" onclick="getEmployeeIdNo(&quot;70666&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. SHIRIN NARESH PATIL</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Mechanical Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70650" onclick="getEmployeeIdNo(&quot;70650&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> SHOBHIT KUMAR SRIVASTAVA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70552" onclick="getEmployeeIdNo(&quot;70552&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Shoubhik Bhattacharya</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Teaching Assitant's</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences &amp; Languages</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="20001" onclick="getEmployeeIdNo(&quot;20001&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Mr. SIDHANT GUPTA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70664" onclick="getEmployeeIdNo(&quot;70664&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. SK ASHADUL RAHAMAN</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70675" onclick="getEmployeeIdNo(&quot;70675&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. SOUMIK SARKAR</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70644" onclick="getEmployeeIdNo(&quot;70644&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. SRINIVAS ARUKONDA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70639" onclick="getEmployeeIdNo(&quot;70639&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. SUDHAKAR REDDY</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Visiting Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="40006" onclick="getEmployeeIdNo(&quot;40006&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> SUDHIR </td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">VIT-AP School of Law</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70547" onclick="getEmployeeIdNo(&quot;70547&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Ms. SUMATHI K</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30049" onclick="getEmployeeIdNo(&quot;30049&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Ms. SUPRIYA C</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30048" onclick="getEmployeeIdNo(&quot;30048&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. S V GOMATHI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70663" onclick="getEmployeeIdNo(&quot;70663&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. THATIPARTHY.BHARATH KUMAR</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70652" onclick="getEmployeeIdNo(&quot;70652&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Ms. T RAMA THULASI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70680" onclick="getEmployeeIdNo(&quot;70680&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. UDAYASRI KOMPALLI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Visiting Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="40005" onclick="getEmployeeIdNo(&quot;40005&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Velpula Vijaya Kumar</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70269" onclick="getEmployeeIdNo(&quot;70269&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. VENKATA BHIKSHAPATHI CHENAM</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70619" onclick="getEmployeeIdNo(&quot;70619&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"> Venkata Lakshmaiah Y</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor On Contract - Lab</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70271" onclick="getEmployeeIdNo(&quot;70271&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Ms. VIJAYAVALLI K</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30050" onclick="getEmployeeIdNo(&quot;30050&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. V LAKSHMI CHETANA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Visiting Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Advanced Sciences</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="40004" onclick="getEmployeeIdNo(&quot;40004&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Ms. VODDELLI SRILAKSHMI</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Sr. Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Computer Science &amp; Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70643" onclick="getEmployeeIdNo(&quot;70643&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. V VISHNU</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Assistant Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70677" onclick="getEmployeeIdNo(&quot;70677&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Ms. YAMUNA DURGA A</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Soft Skill Faculty</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Social Sciences and Humanities</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="30046" onclick="getEmployeeIdNo(&quot;30046&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>

														<tr style="text-align: center; border-style: solid;">
															<!-- <td th:text="${(e[0]==null)?'':e[0]}" style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;"></td> -->
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3;">Dr. YEPUGANTI KARUNA</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">Associate Professor Grade-1</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">School of Electronics Engineering</td>
															<td style="text-align: left; font-weight:bold; color: #000000; font-size:12px; background-color: #d4d3d3">
																<button type="button" class="btn btn-primary" value="select" id="70657" onclick="getEmployeeIdNo(&quot;70657&quot;);">
																<span class="glyphicon glyphicon-ok"></span> 
																</button>	
																									 
															</td>
														</tr>
													</tbody></table>
"""

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the table rows (tr elements)
rows = soup.find_all('tr')

# Loop through rows and extract the "Name of the Faculty"
faculty_names = []
for row in rows[1:]:  # Skip the header row
    columns = row.find_all('td')
    faculty_name = columns[0].get_text(strip=True)  # The first column contains the name
    faculty_names.append(faculty_name)

f=open("faculty-list.txt","w")


for name in faculty_names:
    f.write(name+"\n")

f.close()
