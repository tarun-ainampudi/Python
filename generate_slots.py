subjects = {
    'OS,CSE2008': ['B2+TB2', 'A2+TA2', 'F2+TFF2', 'F2+TF2'],
    'SC,CSE2009': ['D2+TD2', 'C2+TCC2', 'C2+TC2'],
    'CN,CSE3003': ['D2+TDD2', 'B2+TB2', 'D2+TD2', 'C2+TCC2', 'C2+TC2'],
    'DAA,CSE3004': ['D2+TDD2', 'D2+TD2', 'F2+TFF2', 'F2+TF2', 'E2+TE2'],
    'French,FRL1001': ['G2', 'F2', 'C2'],
    'STS,STS3007': [
        'D2+TDD2', 'C2+TCC2', 'B2+TB2', 'D2+TD2', 'A2+TA2',
        'F2+TFF2', 'E2+TE2', 'G2+TG2', 'F2+TF2', 'C2+TC2'
    ],
    'AWS,CSE2025': ['A2+TA2','B2+TB2','C2+TC2','D2+TD2','E2+TE2','F2+TFF2', 'G2+TG2']
}

# subjects = {
#     'OS,CSE2008': ['F1+TF1', 'F1+TFF1', 'A1+TA1', 'B1+TB1'],
#     'SC,CSE2009': ['C1+TC1', 'D1+TD1', 'C1+TCC1'],
#     'CN,CSE3003': ['C1+TC1', 'D1+TD1', 'C1+TCC1', 'D1+TDD1', 'B1+TB1'],
#     'DAA,CSE3004': ['F1+TF1', 'E1+TE1', 'F1+TFF1', 'D1+TD1', 'D1+TDD1'],
#     'French,FRL1001': ['F1', 'C1', 'G1'],
#     'STS,STS3007': [
#         'C1+TC1', 'F1+TFF1', 'D1+TD1', 'C1+TCC1', 'G1+TG1',
#         'A1+TA1', 'E1+TE1', 'D1+TDD1', 'B1+TB1', 'F1+TF1'
#     ],
#     'AWS,CSE2025': ['A1+TA1','B1+TB1','C1+TC1','D1+TD1','E1+TE1','F1+TFF1', 'G1+TG1']
# }

clashable_slots = {"G1":"TC1+TF1","TG1":"TD1","G2":"TC2+TF2","TG2":"TD2"}

def prettyPrintD(slots, subjects):
    print("\n")
    for i in subjects:
        print(f"{i} , {', '.join(slots[i])}")
    print("\n")
    
def prettyPrintND(slots, subjects):
    print("\n")
    for i in subjects:
        print(f"{i} , {slots[i]}")
    print("\n")

def prettyPrintL(li, subjects):
    fs = {}
    for i in subjects:
        sl = []
        for j in li:
            sl.append(j[i])
        fs[i] = sl
    prettyPrintD(fs, subjects)

def vMatch(str1, str2):
    for i in str1.split("+"):
        if i in str2.split("+"):
            return True
    return False

def vExists(slot, slots):
    if any(key in slot for key in clashable_slots):
        #print(f"Before : {slot}")
        str1=""
        slot_split = slot.split("+")
        for i in slot_split:
            if i in clashable_slots:
                str1 += clashable_slots[i] + "+"
            else:
                str1 += i + "+"
        slot = str1.rstrip("+")
        #print(f"After : {slot}")
    for i in slots.values():
        if vMatch(slot, i):
            return True
    return False

pSlots = []

def generateSlots(subject_list, index, current_slots):
    if index == len(subject_list):
        pSlots.append(current_slots.copy())
        return

    subject = subject_list[index]
    for slot in subjects[subject]:
        if not vExists(slot, current_slots):
            current_slots[subject] = slot
            generateSlots(subject_list, index + 1, current_slots)
            del current_slots[subject]

# Start the recursive search
subject_list = list(subjects.keys())
generateSlots(subject_list, 0, {})

# Display the results
prettyPrintL(pSlots, subjects)
print(f"Total valid non-clashing combinations: {len(pSlots)}")

print(f"\nAfter 8 AM slots:")

slots_8am = ["TFF1","TGG1","TEE1","TCC1","TDD1"]
after_8_slots = []
for i in pSlots:
    #print(i.values())
    valid = True
    for j in i.values():
        for k in j.split("+"):
            #print(k in slots_8am)
            if k in slots_8am:
                valid = False
                break
    if valid:
        after_8_slots.append(i)        
        
prettyPrintL(after_8_slots, subjects)
print(f"Total valid non-clashing combinations after 8 AM: {len(after_8_slots)}")

print(f"\n Before 6 PM slots:")

slots_6pm = ["TFF2","TGG2","TEE2","TCC2","TDD2"]
before_6_slots = []
for i in pSlots:
    #print(i.values())
    valid = True
    for j in i.values():
        for k in j.split("+"):
            #print(k in slots_8am)
            if k in slots_6pm:
                valid = False
                break
    if valid:
        before_6_slots.append(i)        
        
if(len(before_6_slots) == 1):
    prettyPrintND(before_6_slots[0], subjects)
else:
    prettyPrintL(before_6_slots, subjects)
print(f"Total valid non-clashing combinations before 6 PM: {len(before_6_slots)}")