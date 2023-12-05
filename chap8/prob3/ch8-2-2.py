text_file = open("write_it.txt", "w")
print("input your string...")
while (1):
    str = input(">> ")
    if (str == "Q"):
        print("Write process has been finished\n\n\n\n")
        break
    text_file.write(str)
    text_file.write("\n")
text_file.close()
print("Your inputs are below..")
text_file = open("write_it.txt", "r")
for line in text_file:
    print(line, sep='\n', end='')
