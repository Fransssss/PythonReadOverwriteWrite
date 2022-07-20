# author: Fransiskus Agapa
# read overwrite and write to a file

print("\n== File Menu ==")
print("1. Read file")
print("2. Overwrite file")
print("3. Write file")
print("E. Exit")
choice = input("choice: ")

while choice != 'e' and choice != 'E':
    if choice == '1':
        print("\n[ Read file ]")
        try:
            with open("joke.txt", 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print("\n[ File is not found ]")
    elif choice == '2':
        print("\n[ Overwrite file ]")
        try:
            overwrite_text = input("Input new text: ")
            with open("joke.txt", 'w') as file:
                file.write(overwrite_text)
                print("[ File has been overwritten ]")
        except FileNotFoundError:
            print("[ File is not found ]")
    elif choice == '3':
        print("\n[ Write file ]")
        add_text = input("Input text: ")
        try:
            with open("joke.txt", 'a') as file:
                file.write(add_text)
                print("[ File has been updated ]")
        except FileNotFoundError:
            print("[ File is not found ]")
    else:
        print("\n[ Invalid choice ]")

    print("\n== File Menu ==")
    print("1. Read file")
    print("2. Overwrite file")
    print("3. Write file")
    print("E. Exit")
    choice = input("choice: ")


if choice == 'e' or choice == 'E':
    print("\n== Exit Program ==")

# What is fast, loud and crunchy? A rocket chip.
# How does the ocean say hi? It waves!