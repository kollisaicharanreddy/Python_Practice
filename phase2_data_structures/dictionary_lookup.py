contacts = {
    "Charan": "8888888888",
    "Raju": "9999999999",
    "Ujwal": "7777777777"
}
name = input()
phone = contacts.get(name, "Contact not found")
print(phone)