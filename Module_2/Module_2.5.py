talents=float(input("Enter talents:\n"))
pounds=float(input("Enter pounds:\n"))
lots=float(input("Enter lots:\n"))
gram=(talents*20*32*13.3)+(pounds*32*13.3)+(lots*13.3)
kilograms=int(gram/1000)
grams=gram%1000
print(f'The weight in modern units:\n {kilograms} kilograms and {grams:.2f} grams')