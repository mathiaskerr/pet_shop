def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, num):
    pet_shop["admin"]["pets_sold"] += num


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, breed):
    list = []
    x = 0
    for pets in pet_shop:
        if pet_shop["pets"][x]["breed"] == breed:
            list.append(breed)
            x += 1
    return list


def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet


def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)


def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)


def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customer, num):
    customer["cash"] -= num    

def get_customer_pet_count(customers):
    return len(customers['pets'])

def add_pet_to_customer(customer, new_pet):
    customer['pets'].append(new_pet)
