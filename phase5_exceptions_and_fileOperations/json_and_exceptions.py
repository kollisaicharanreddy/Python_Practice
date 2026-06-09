import json

database = {
    "username":"kscr",
    "password":"kscr1234",
    "database_name": "customers"
}

with open("db_credentials.json", "w") as file:
    json.dump(database, file, indent=4)

try:
    with open("missing_credentials.json", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The requested file does not exist")
finally:
    print("The execution is completed")