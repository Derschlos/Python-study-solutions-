dictonary = {}
recursions = 0

def list_gen(mini, maxi):
    """fills the dictonary by generating the numbers then splits them
    with str spliting, sqauring the digit and adding them up in the storage""" 
    maxi += 1
    for number in range(mini ,maxi):
        storage = 0
        r = str(number)
        for digit in r:
            digit = int(digit)
            storage = storage + (digit**2)
        dictonary[number] = storage
    return

def check(num):
    """checks if a number is in the premade dict and then either generates it
    by calling list_gen or returns it from the dict immediately"""  
    if num not in dictonary:
        list_gen(num-1, num +10)
    result_at_num = dictonary[num]
    return result_at_num

def happy_num(amount):
    """generates a list of (amount * happy numbers) called happy"""
    happy = [1]
    potential_happy = 2

    def recursion(num):
        """runs recurevely until it finds a 1 (returning True)
        or goes to 5 recursions(returning False)""" 
        global recursions
        if num == 1:
            recursions = 0
            return True
        elif recursions == 5:
            recursions = 0
            return False
        recursions +=1
        return recursion(check(num))

    while len(happy) is not amount:
        u = recursion(potential_happy)
        if u == True:
            happy.append(potential_happy)
        potential_happy += 1
    return happy

#pregenerates a list up to (9**2 + 9**2);adjust as you wish
list_gen(1, 162)
#prints the first 50 happy numbers; adjust as necessary
print(happy_num(50))
