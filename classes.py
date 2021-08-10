# class Kettle(object):

#     def __init__(self, make, price):
#         self.make = make
#         self.price = price
#         self.on = False


# kenwood = Kettle("Kenwood", 8.99)
# print(kenwood.make)
# print(kenwood.price)

# kenwood.price = 12.75
# print(kenwood.price)

# hamilton = Kettle("Hamilton", 14.55)

# print(f"Models: {kenwood.make} = {kenwood.price}, {hamilton.make} = {hamilton.price}")
# print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))


# squeres = [value**2 for value in range(1,11)]
# print(squeres)

# listas = []
# for i in range(1, 1000001):
#     listas.append(i)

# print(sum(listas))

# listas = [value**3 for value in range(1,11)]
# print(listas)

# listas = [i ** 3 for i in range(11)]

# print(listas)


###################################################################


# class Restaurant:
#     def __init__(self, name, type):
#         self.name = name
#         self.type = type
#         self.number_served = 0


#     def describe_restaurant(self):
#         print(f'''Restaurant name: {self.name}\nRestaurant type: {self.type}''')


#     def open_restaurant(self):
#         print(f'{self.name.title()} is now open, welcome!')


#     def set_number_served(self, number):
#         self.number_served = self.number_served + number
#         print(f"New serving number is {self.number_served}")


# restoranas = Restaurant('Valgykla', 'Basic')

# # restoranas.describe_restaurant()

# # restoranas.open_restaurant()

# print(restoranas.number_served)
# restoranas.number_served = 5
# print(restoranas.number_served)
# restoranas.set_number_served(7)
# print(restoranas.number_served)


##########################################################################


class User:
    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.balance = 0
        self.login_attempts = 0

    
    def describe_user(self):
        print(f"""Information about user:
Name: {self.name}
Age: {self.age}
Gender: {self.gender}
Height: {self.height}""")


    def greet_user(self):
        print(f"Greetings {self.name}")

    
    def show_balance(self):
        print(f'{self.name} has {self.balance} in his account.')


    def increment_login_attempts(self):
        self.login_attempts += 1


    def reset_login_attempts(self):
        self.login_attempts = 0


vartotojas = User('Bill', 20, 'Male', 1.86)
vartotojas2 = User('Joe', 25, 'Male', 1.75)
vartotojas3 = User('Ana', 28, 'Female', 1.70)

# # print(vartotojas.name)
# # vartotojas2.describe_user()
# # vartotojas2.show_balance()
# # vartotojas2.balance = 423
# # vartotojas2.show_balance()

# vartotojas.increment_login_attempts()
# vartotojas.increment_login_attempts()
# vartotojas.increment_login_attempts()
# print(vartotojas.login_attempts)
# vartotojas.reset_login_attempts()
# print(vartotojas.login_attempts)


# class IceCreamStand(Restaurant):
#     def __init__(self, name, type):
#         super().__init__(name, type)
#         self.flavors = ['Strawberry', 'Vanilla', 'Chocolate', 'Caramel']


#     def show_flavors(self):
#         print(f'In our restaurant we have these kind of flavours:')
#         for i in self.flavors:
#             print(f'[+]{i}')


# ledaine = IceCreamStand('IceMania', 'Ledaine')

# ledaine.describe_restaurant()
# print()
# ledaine.show_flavors()\


class Privileges():
    def __init__(self):
        self.privileges = ['Can ban user', 'Can delete post', 'Can add post', 'Can access database']


    def show_privileges(self):
        print('Admin has these privileges:')
        for i in self.privileges:
            print(f'[+]{i}')


class Admin(User):
    def __init__(self, name, age, gender, height):
        super().__init__(name, age, gender, height)
        self.privileges = Privileges()


   
adminas = Admin('Adolf', 55, 'Male', 'Nevermind')

adminas.describe_user()
adminas.privileges.show_privileges()
