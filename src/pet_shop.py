# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

#The function needs to return a list
#I need to grab the pets from the pet_shop
#I need to loop through them and find the 

def get_pets_by_breed(pet_shop, input_breed):
    found_pets = []
    pets = pet_shop["pets"]
    for pet in pets:
        if pet ["breed"]== input_breed:
            found_pets.append(pet)
    
    return found_pets