class Mobile:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def Mob_Category(self):
        if self.price >=60000:
            return "Premium Category"
        elif self.price >=25000 and self.price<60000:
            return "Mid - range category"
        else:
            return "Budget"

    def Display(self):
        print(f"{self.brand:<10} {self.model:<15} {self.price:<12} {self.Mob_Category()}")

class Store:
    def __init__(self,name):
        self.name = name
        self.mobiles =[]


    def Add_mobiles(self,brand,model,price):
        mobile = Mobile(brand,model,price)
        self.mobiles.append(mobile)
        print(f"Mobile added successfully: {brand} {model}")

    def display(self):
        print(f"========== {self.name} =========")
        print(f"{'Brand':<10} {'Model':<15} {'Price':<12} {'Category'}")
        for mob in self.mobiles:
            mob.Display()

store = Store("Arnav mobile store")
store.Add_mobiles("Apple","Iphone 17 pro",95000)
store.Add_mobiles("samsung","F23",35000)
store.Add_mobiles("Mototrola","g57 power",19000)

store.display()


# Output
'''Mobile added successfully: Apple Iphone 17 pro
Mobile added successfully: samsung F23
Mobile added successfully: Mototrola g57 power
========== Arnav mobile store =========
Brand      Model           Price        Category
Apple      Iphone 17 pro   95000        Premium Category
samsung    F23             35000        Mid - range category
Mototrola  g57 power       19000        Budget'''
