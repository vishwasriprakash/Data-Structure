# Get the input from the user and display
# 1. Search the Name 2. Search the Mark 3. Find the Number of name by marks (Above 80 or 90) using switch case:

dictionary = {}

a = int(input("How many keys and values want to enter?: "))

for i in range(a):
    key = input("Name: ")
    value = int(input("Mark: "))
    dictionary[key] = value

print(dictionary)
while True:

    print("\n---- Menu ----")
    print("1. Search the Name")
    print("2. Search the Mark")
    print("3. Find the Number of name by marks (Above 80 or 90)")
    print("4. Exit")

    choice = int(input("Your Choice: "))

    match choice:
        case 1:
            print("Find the Name")
            search_name = input("Name: ")
            print(dictionary.get(search_name)) # it only for keys not for values(key is only name)

            for name in dictionary:
                if name == search_name:
                    x = "Yes"
                    break
                else:
                    x = "No"

            print(x)
            print()

        case 2:
            print("Find the Mark")
            search_mark = int(input("Mark: "))
            #print(dictionary.get(search_mark)) # it only for keys not for values(key is only name,value is mark)

            found = False
            for key,value in dictionary.items():
                if value == int(search_mark):
                    print("Name: "+key)
                    found = True
                    break
            if not found:
                print("Name and Mark not found")

            print()

        case 3:
            print("Find the Number of name by marks (Above 80 or 90)")
            search_mark1 = int(input("Mark: "))
            print(dictionary.get(search_mark1))

            for key,value in dictionary.items():
                if value >= int(search_mark1):
                    print("Name: "+key+"\nMarks: "+str(value))

        case 4:
            print("Invalid Choice, Please try again!!")
            break
