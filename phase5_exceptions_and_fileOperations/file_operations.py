with open("users.txt", "w") as file:
    file.writelines(["Charan\n", "Ujwal\n", "Sharma\n"])
with open("users.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())