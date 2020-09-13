# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop_dic):
    return pet_shop_dic["name"]

def get_total_cash(pet_shop_dic):
    return pet_shop_dic["admin"]["total_cash"]

def add_or_remove_cash(pet_shop_dic, amount):
    existing_cash = ["admin"][int"total_cash"]
    total_cash.add(amount)
    return(total_cash)
