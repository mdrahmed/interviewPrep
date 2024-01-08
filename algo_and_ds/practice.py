
def product(n):
    if n < 10:
        return n 
    products = 1
    while n > 0:
        modu = n %10
        n = n//10
        products *= modu
    return products

def isColorful(n):
    all_products = set()
    str_n = str(n)
    for i in range(1,len(str_n)):
        # 3245 0-2 1-3
        for j in range(0,len(str_n)-i+1):
            new_n = str_n[j:j+i]
            new_product = product(int(new_n))
            if new_product in all_products:
                return False
            all_products.add(new_product)
    return True

print(isColorful(3245))
print(isColorful(326))
