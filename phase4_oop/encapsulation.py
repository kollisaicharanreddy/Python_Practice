class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def check_password(self, input_password):
        if self.__password == input_password:
            return True
        return False

user1 = UserAccount("charan", "12345678")
print(user1.check_password("12345678"))
user2 = UserAccount("cherry", "89674809")
print(user2.check_password("wrongpass"))