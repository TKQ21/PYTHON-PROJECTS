import re
import json
import pickle

class customer:
    cusdict = {}   # key = customer id

    def __init__(self):
        self.id = ""
        self.name = ""
        self.age = 0
        self.email = ""
        self.mobile = ""
        self.address = ""
        self.profession = ""
        self.city = ""
        self.country = ""

    # ---------- VALIDATION ----------
    @staticmethod
    def validate_mobile(mobile):
        return re.fullmatch(r'^(\+91|91)?[6-9]\d{9}$', mobile)

    # ---------- ADD ----------
    def addcustomer(self):
        customer.cusdict[self.id] = self

    # ---------- SEARCH ----------
    def searchcustomer(self):
        if self.id in customer.cusdict:
            e = customer.cusdict[self.id]
            self.__dict__.update(e.__dict__)
            return True
        return False

    # ---------- DELETE ----------
    def deletecustomer(self):
        if self.id in customer.cusdict:
            del customer.cusdict[self.id]
            return True
        return False

    # ---------- MODIFY ----------
    def modifycustomer(self):
        if self.id in customer.cusdict:
            customer.cusdict[self.id] = self
            return True
        return False

    # ---------- DISPLAY ----------
    @staticmethod
    def showcustomer(cus):
        print(
            "ID:", cus.id,
            "| Name:", cus.name,
            "| Age:", cus.age,
            "| Email:", cus.email,
            "| Mobile:", cus.mobile,
            "| Address:", cus.address,
            "| Profession:", cus.profession,
            "| City:", cus.city,
            "| Country:", cus.country
        )

    # ---------- JSON SAVE / LOAD ----------
    @classmethod
    def save_json(cls):
        with open("customers.json", "w") as f:
            json.dump({k: v.__dict__ for k, v in cls.cusdict.items()}, f, indent=4)

    @classmethod
    def load_json(cls):
        try:
            with open("customers.json") as f:
                data = json.load(f)
                for k, v in data.items():
                    c = customer()
                    c.__dict__.update(v)
                    cls.cusdict[k] = c
        except FileNotFoundError:
            pass

    # ---------- PICKLE SAVE / LOAD ----------
    @classmethod
    def save_pickle(cls):
        with open("customers.pkl", "wb") as f:
            pickle.dump(cls.cusdict, f)

    @classmethod
    def load_pickle(cls):
        try:
            with open("customers.pkl", "rb") as f:
                cls.cusdict = pickle.load(f)
        except FileNotFoundError:
            pass


# ================= MENU =================
while True:
    print("""
1.ADD CUSTOMER
2.SEARCH CUSTOMER
3.DELETE CUSTOMER
4.MODIFY CUSTOMER
5.DISPLAY ALL
6.LOAD FROM JSON
7.SAVE TO JSON
8.LOAD FROM PICKLE
9.SAVE TO PICKLE
10.EXIT
""")

    choice = input("Enter choice: ")

    if choice == '1':
        cus = customer()
        cus.id = input("ID: ")

        if cus.id in customer.cusdict:
            print("Customer ID already exists")
            continue

        cus.name = input("Name: ")

        while True:
            try:
                cus.age = int(input("Age: "))
                break
            except ValueError:
                print("Age must be number")

        cus.email = input("Email: ")

        while True:
            mobile = input("Mobile: ")
            if customer.validate_mobile(mobile):
                cus.mobile = mobile[-10:]
                break
            else:
                print("Invalid mobile")

        cus.address = input("Address: ")
        cus.profession = input("Profession: ")
        cus.city = input("City: ")
        cus.country = input("Country: ")

        cus.addcustomer()
        print("Customer added")

    elif choice == '2':
        cus = customer()
        cus.id = input("Enter ID: ")
        if cus.searchcustomer():
            customer.showcustomer(cus)
        else:
            print("Customer not found")

    elif choice == '3':
        cus = customer()
        cus.id = input("Enter ID: ")
        print("Deleted" if cus.deletecustomer() else "Customer not found")

    elif choice == '4':
        cus = customer()
        cus.id = input("Enter ID: ")

        if cus.id not in customer.cusdict:
            print("Customer not found")
            continue

        cus.name = input("New Name: ")
        cus.age = int(input("New Age: "))
        cus.email = input("New Email:")
        cus.mobile = input("New Mobile:")
        cus.address = input("New Address:")
        cus.profession = input("New Profession:")
        cus.city = input("New City:")
        cus.country = input("New Country:")

        cus.modifycustomer()
        print("Customer updated")

    elif choice == '5':
        if not customer.cusdict:
            print("No customers")
        else:
            for e in customer.cusdict.values():
                customer.showcustomer(e)
                print("-" * 40)

    elif choice == '6':
        customer.load_json()
        print("Loaded from JSON")

    elif choice == '7':
        customer.save_json()
        print("Saved to JSON")

    elif choice == '8':
        customer.load_pickle()
        print("Loaded from PICKLE")

    elif choice == '9':
        customer.save_pickle()
        print("Saved to PICKLE")

    elif choice == '10':
        print("Bye 👋")
        break

    else:
        print("Invalid choice")