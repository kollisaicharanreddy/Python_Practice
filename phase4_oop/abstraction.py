from abc import ABC, abstractmethod

class DataRepository(ABC):
    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def delete(self, id):
        pass

class SQLRepository(DataRepository):
    def save(self, data):
        print(f"Saved the data: {data}")

    def delete(self, id):
        print(f"Deleted the data by id: {id}")

sql = SQLRepository()
sql.save("User Profile")
sql.delete(101)