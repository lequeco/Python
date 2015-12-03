shopping_list = ["banana", "laranja", "maca"]

stock = {
    "banana": 6,
    "maca": 0,
    "laranja": 32,
    "pera": 15
}
    
prices = {
    "banana": 4,
    "maca": 2,
    "laranja": 1.5,
    "pera": 3
}

# Escreva seu codigo abaixo!
 
def compute_bill(food):
    total = 0
    for key in food:
        if stock[key] > 0:
            total = total + prices[key]
            stock[key] = stock[key] - 1
    return total
            