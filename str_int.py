def cloth_sales(cloth_and_price):
    cloth = " "
    price = " "

    cloth_or_price = cloth_and_price.split()
    
    for i in cloth_or_price:
        if i.isalpha():
            cloth += i + " "
        else:
            price = i

    cloth = cloth.strip()

    return f"The {cloth} now goes for KES {price}"

cloth_label = "Official Suit 4500"

print(cloth_sales(cloth_label))

    



         

