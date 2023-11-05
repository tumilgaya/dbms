import pymongo
from pymongo import MongoClient


class UserDataBase:     #making class for CRUD operations
    def __init__(self):
        self.client = MongoClient("localhost", 27017)   #define client MongoClient()
        self.db = self.client["userdata"]
        self.collection = self.db["users"]

    def createUser(self, name, age, salary):
        user = {
                "Name": name,
                "Age": age,
                "Salary": salary,
            }

        self.collection.insert_one(user)   #insertOne({"firstName": fname, "lastName": lname})
        print("Created user successfully!")

    
    def displayuser(self):
        users = self.collection.find()  
        if users:
            for i in users:
                self.displayUser(i)
        else:
            print("\nNo users in the database currently!")

    def displayUser(self,user):
        print(f'\nName: {user["Name"]},\t\tAge:{user["Age"]},\t\tSalary:{user["Salary"]}')
        print(f'')

    def update(self,name,age):
        temp = self.collection.find_one({"Name":name})

        if temp:
            print("fond")
            self.collection.update_one({"Name":name},{"$set":{"age":age}})
        else:
            print("NOTFOUND")
        
    def deleteUser(self,name):
        temp = self.collection.find_one({"Name":name})

        if temp:
            print("fond")
            self.collection.delete_one({"Name":name})

    def closeConnection(self):
        self.client.close()


def main():
    obj = UserDataBase()
    while(1):
        print("1 add")
        print("2 delete")
        print("3 display")
        print("4 update")

        no = int(input("ENter the choice : "))

        if no == 1:
            name =input("Enter name")
            age =int(input("Enter age"))
            salary =int(input("Enter salary"))
            obj.createUser(name,age,salary)
        
        elif no ==2:
            obj.deleteUser(name)
        elif no ==3:
            obj.displayuser()
        elif no ==4:
            obj.update(name,age)
        elif no ==5:
            break

main()

