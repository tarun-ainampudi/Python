import datetime
def searchkeyword(keyword,dictionary):
    pass    
#There are two hostel blocks
#Each contain 2 floors ground and first
#Each floor contain 13 rooms
#6 are two bed 6 are four bed 1 is 8 bed or dorm
listofhostels={'MH-1':{'twobed':{'001':2,'002':2,'003':2,'004':2,'005':2,'006':2,'101':2,'102':2,'103':2,'104':2,'105':2,'106':2},
                       'fourbed':{'007':4,'008':4,'009':4,'010':4,'011':4,'012':4,'107':4,'108':4,'109':4,'110':4,'111':4,'112':4},
                       'dorm':{'013':8,'113':8}},
               'MH-2':{'twobed':{'001':2,'002':2,'003':2,'004':2,'005':2,'006':2,'101':2,'102':2,'103':2,'104':2,'105':2,'106':2},
                       'fourbed':{'007':4,'008':4,'009':4,'010':4,'011':4,'012':4,'107':4,'108':4,'109':4,'110':4,'111':4,'112':4},
                       'dorm':{'013':8,'113':8}},
              }
serialnumber=1
print("Available Rooms:")
for i,j in listofhostels.items():
    for k,l in j.items():
        print(f"{i} - {k.upper()} - {l}")
print("\nSelect one of the option below")
key=int(input("1)Registration of the new user\n2)Quit\nEnter the option:"))
while key==1:
    username=input("\nEnter the Username:").upper()
    if username.isalnum() and len(username)==9:
        name=input("Enter the Name:").upper()
        room_type=int(input('Enter the sharing of room(2/4/8):'))
        if room_type==2:
            room_type='twobed'
        elif room_type==4:
            room_type='fourbed'
        elif room_type==8:
            room_type='dorm'
        else:
            print('Invalid Input! - Try Again')
            key=1
            continue
        #Pending
        avilability='Checking'
        block="Not Alloted"
        room_number="Not Assigned"
        for i,j in listofhostels.items():
            for k,l in j.items():
                if k==room_type:
                    for m,n in l.items():
                         if n>=1:
                             room_number=m
                             listofhostels[i][k][m]-=1
                             break
                    block=i
                    print(f'Block Alloted : {block}')
                    print(f'Room Alloted : {room_number}')
                    avilability="It is available!"
                    print(avilability)
                    break
                else:
                    continue
            if avilability=="It is available!":
                break    
        #To Give the Room Number
        #Changing its value in the dictionary
        hostel_list=open('HostelList.txt','a+')
        dateandtime=datetime.datetime.now()
        hostel_list.write(f'{serialnumber} - {dateandtime.strftime("%d-%m-%Y")} - {username} - {name} - {block} - {room_number} - {room_type.upper()}\n')
        hostel_list.close()
        serialnumber+=1
        print("\nSelect one of the option below")
        key=int(input("1)Registration of the new user\n2)Quit\nEnter the option:"))
        continue
    else:
        print("Invalid Username!\nTry Again")
        key=1
while key==2:
    print("File Saved Sucessfully!")
    break

