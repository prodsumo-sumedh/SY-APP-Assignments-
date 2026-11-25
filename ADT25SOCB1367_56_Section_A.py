class Toy:
    def __init__(self, toy_name, age_group, price):
        self.toy_name = toy_name
        self.age_group = age_group
        self.price = price

    def display_toy(self):
        print(f"Toy Name : {self.toy_name}")
        print(f"Age Group: {self.age_group}")
        print(f"Price: Rs. {self.price}")
        print("-" * 30)


class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.toys = []

    def add_toy(self, toy):
        self.toys.append(toy)
        print(f"{toy.toy_name} added successfully!")

    def display_all_toys(self):
        print("\n==================================")
        print(f"{self.store_name}")
        print("AVAILABLE TOYS")
        print("==================================")

        if not self.toys:
            print("No toys available in the store.")
        else:
            for toy in self.toys:
                toy.display_toy()


store_name = input("Enter Store Name: ")
store = Store(store_name)

while True:
    print("\n===== TOY STORE MANAGEMENT =====")
    print("1. Create Toy and Add to Store")
    print("2. Display All Toys")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        toy_name = input("Enter Toy Name: ")
        age_group = input("Enter Age Group: ")

        try:
            price = float(input("Enter Toy Price: "))

            if price < 0:
                print("Price cannot be negative.")
                continue

            toy = Toy(toy_name, age_group, price)
            store.add_toy(toy)

        except ValueError:
            print("Please enter a valid price.")

    elif choice == "2":
        store.display_all_toys()

    elif choice == "3":
        print("Thank you for visiting Toy Store!")
        break

    else:
        print("Invalid choice! Please try again.")
