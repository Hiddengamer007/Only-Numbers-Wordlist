print(" _   _                 _               _ _     _    ___  ___      _             ")
print("| \ | |               | |             | (_)   | |   |  \/  |     | |            ")
print("|  \| |_   _ _ __ ___ | |__   ___ _ __| |_ ___| |_  | .  . | __ _| | _____ _ __ ")
print("| . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | / __| __| | |\/| |/ _` | |/ / _ \ '__|")
print("| |\  | |_| | | | | | | |_) |  __/ |  | | \__ \ |_  | |  | | (_| |   <  __/ |   ")
print("\_| \_/\__,_|_| |_| |_|_.__/ \___|_|  |_|_|___/\__| \_|  |_/\__,_|_|\_\___|_|   ")
print("By Hiddengamer007")
print(" ")
print("Welcome to the Numberlist maker.")
print("Follow the instructions to generate a list with numbers")
print("Enter the highest number in the List")
print("For example, a 4 digit code has 10000 combinations, so the highest number is 10000")
numbers = input("Enter the highest number: ")
filename = input("Enter the Filename of the list: ")

intnumbers = int(numbers)

maxnum = intnumbers + 1

a = 0

f = open(filename+'.txt', 'w')
for i in range(1,maxnum):
    a += 1
    f.write(str(a)+'\n')
    print(a)