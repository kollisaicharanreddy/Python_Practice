class NotificationService:
    def send_message(self, user, message="System Update"):
        return f"{user}: {message}"

notification1 = NotificationService()
print(notification1.send_message("Charan"))
print(notification1.send_message("Charan", "Default Update"))