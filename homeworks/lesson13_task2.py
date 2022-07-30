def discount(a):
    def make_discount(b):
        return b - b * a/100

    return make_discount


discount_10 = discount(10)
discount_5 = discount(5)

print(discount_10(100))
print(discount_5(100))
