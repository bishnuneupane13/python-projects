word = input("Enter some text: ")

with open("file.txt", "r") as file:
    bn = file.read().splitlines()
    for items in bn:
        if items in word:
            word = word.replace(items, "***")

    print("You entered:", word)

file.close()
