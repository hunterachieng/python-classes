class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"We are the {self.restaurant_name} offering you {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now OPEN!")
        
restaurant = Restaurant("Mama's Heart","African")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2=Restaurant("La Paz","Italian")
restaurant3 = Restaurant("Fan Mian","Chinese")
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

class User:
    
    def __init__(self,first_name,last_name,email,phone_number,address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} of email:{self.email} , phone number {self.phone_number} and address {self.address}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

user = User("Veronicah","Njenga","njengaveronica@gmail.com","0723534563","200-Nairobi")
user.describe_user()
user.greet_user()
user2 =User("Mercelyine", "Ombongi","akoth@gmail.com","0789346234","300-Kisii")
user2.describe_user()
user2.greet_user()
    