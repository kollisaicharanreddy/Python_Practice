def security_check(func):
    def wrapper():
        print("Checking user permissions... Access Granted!")
        func()
    return wrapper
@security_check
def delete_database():
    print("The database has been deleted")

delete_database()