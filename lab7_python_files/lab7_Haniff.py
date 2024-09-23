""" Alisa Haniff
    Sept 23, 2024
    Python Files
 """   


#pipe the file with the .py file
fileUsers = open("users.txt", "r")    

print(f"\n-----------Example 2: Python limit to read files -------------\n")
#reads the first 10 characers
print(fileUsers.read(10))

print(f"\n-----------Example 1: Python files -------------\n")
#use loop to go through each line of the file
for eachline in fileUsers:
    print(eachline)
    

#alternative: print(fileusers.read())
#close file
fileUsers.close()

print(f"\n-----------Example 3: Python read files with 'with' and 'r'-------------\n")
with open("users.txt", "r") as fileUsers:
    lines_users = fileUsers.read()
    print(lines_users)
fileUsers.close()

#prints by index
print("\n")
with open("users.txt", "r") as fileUsers:
    eachlines = fileUsers.readlines()
    print(eachlines[2])
fileUsers.close()

    
print(f"\n-----------Example 4: Python read files with 'split-------------\n")
with open("users.txt","r") as fileUsers:
    eachlines = fileUsers.readlines()
    for line in eachlines:
        word = line.split()
        print(word[2])
        
print(f"\n-----------Example 5: Python read files and check for a specific item-------------\n")
def finduser(textfile, username):
    with open("users.txt","r") as fileUsers:
        eachline = fileUsers.readlines()
        usercounter = 0
        for line in eachline:
            word = line.split()
            for eachword in word:
                if eachword == "Bruce":
                    usercounter += 1
    return usercounter
user = "Diana"
usercount = finduser("users.txt", user)
print(f"There is {usercount} with the name {user}")

    
print(f"\n-----------Example6: Python write file-------------\n")
def userReport(totalCount, username):
    with open("writeResult.txt", "w") as writeUserResult:
        writeUserResult.write(f"There is {totalCount} with the name '{username}'")

userReport(usercount, user)

print(f"\n-----------Example6: Python append data-------------\n")

def addUser(newUser,city, age, userFilename):
    with open(userFilename, "a") as fileUsers:
        fileUsers.write(f"{newUser}, {city}, {age}")

newUsername= "Kate Spade"
city = "NYC"
age = "38"        
addUser(newUsername, city, age, "users.txt")

print(f"\n-----------Example 7: Python add error-------------\n")

def addUser(newUser,city, age, userFilename):
    try: 
        with open(userFilename, "a") as fileUsers:
            fileUsers.write(f"{newUser}, {city}, {age}")
    except IOError:
        print(f"Error! couldn't find file name {userFilename}")
        
newUsername= "Kate Spade"
city = "NYC"
age = "38"        
addUser(newUsername, city, age, "users.txt")