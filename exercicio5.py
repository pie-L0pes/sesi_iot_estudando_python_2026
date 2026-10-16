b = int(input("Escreva um ano:"))

if b % 4 == 0 & b % 400 == 0 & b % 100 == 0:
    print("O ano", b, "é bissexto")
else:
    print("O ano", b, "não é bissexto")