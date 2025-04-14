producto = float(input("Introduce el precio del producto: "))
if producto < 100:
    print("Compra el producto")
elif producto >= 100 and producto <= 150:
    print("Holding")
else:
    print("Vende el producto")