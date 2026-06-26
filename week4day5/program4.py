h = float(input("Height(cm): "))
w = float(input("Weight(kg): "))

bsa = ((h * w) / 3600) ** 0.5

print("BSA =", round(bsa, 2))