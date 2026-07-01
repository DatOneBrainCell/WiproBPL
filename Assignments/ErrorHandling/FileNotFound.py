try:
    with open("C:\\Users\\Admin\\Desktop\\23CS141\\txt\\SomethingAbout.txt", "r") as tx:
        content = tx.read().title()
        print(content)
except(FileNotFoundError):
    print("Cant find file")

'''O\P:
Cant find file
'''
