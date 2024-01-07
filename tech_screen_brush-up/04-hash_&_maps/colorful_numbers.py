## Site: https://tutorialhorizon.com/algorithms/colorful-numbers/
### Very good site for competitive programming
# 3245
# 3 2 4 5 32 24 45 324 245

# 32
# 32%10 = 2
# 32/10 = 3
# 3%10 = 3
# 3/10 = 0
def product(n):
    if n < 10:
        return n
    product = 1
    while n > 0:
        modu = n%10
        n = n//10
        product *= modu
    return product
    
print(product(32))

def isColorful(a):
    num = str(a)
    length = len(num)
    product_set = set()
    # 324 
    # i = 1 2
    # j = 0-1,1-2 => 3-1 | 0-2, 1-3 => 3-2+1 = 2
    for i in range(1,length):
        for j in range(0, length-i+1):
            sub = num[j:j+i]
            #print(sub)
            products = product(int(sub))
            if products in product_set:
                return False
            else:
                product_set.add(products)
    return True

print(isColorful(3245))
