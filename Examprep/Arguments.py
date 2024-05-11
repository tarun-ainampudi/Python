def new_function(registration_number,name,branch="CSE",**courses):
    print(f"Registration Number : {registration_number}")
    print(f"Name : {name}")
    print(f"Branch : {branch}")
    for course,subject in courses.items():
        print(f"{course} : {subject}",end="  ")
new_function('23BCE9846',"Tarun",CSE="Python",MATHS="Calculus")