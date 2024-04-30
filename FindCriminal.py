#   practice/3
#four suspects,each with three answers//
suspects={
    "A": ["C and I have seen each other many times before today", "B is guilty", "thief didnt know that the car belonged to him"],
    "B": ["D hasnt done this", "third word of D is a lie", "im innocent"],
    "C": ["i have not met A before this problem", "B is not guilty", "D cant drive"],
    "D": ["first word of D is a lie", "i cant drive", "A did this"]}
def check_statement(assertion): 
    if assertion == "C and I have seen each other many times before today" :
        return suspects["A"][0] == assertion
    elif assertion == "B is guilty" :
        return suspects["A"][1] == assertion
    elif assertion == "thief didnt know that the car belonged to him" :
        return suspects["A"][2] == assertion
    elif assertion == "D hasnt done this" :
        return suspects["B"][0] == assertion
    elif assertion == "third word of D is a lie" :
        return suspects["B"][1] == assertion
    elif assertion == "im innocent" :
        return suspects["B"][2] == assertion
    elif assertion == "i have not met A before this problem" :
        return suspects["C"][0] == assertion
    elif assertion == "B is not guilty" :
        return suspects["C"][1] == assertion
    elif assertion == "D cant drive" :
        return suspects["C"][2] == assertion
    elif assertion == "first word of D is a lie" :
        return suspects["D"][0] == assertion
    elif assertion == "i cant drive" :
        return suspects["D"][1] == assertion
    elif assertion == "A did this" :
        return suspects["D"][2] == assertion
    else:
        return False
def find_thief():
    for suspect,assertions in suspects.items():
        count = 0
        for assertion in assertions:
            if check_statement(assertion):
                count+= 1
        if count == len(assertions):
            return suspect
co=find_thief()
print(co) #criminal is?