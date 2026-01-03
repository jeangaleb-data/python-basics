ladoA = float(input('Qual o comprimento do lado "A"? '))
ladoB = float(input('Qual o comprimento do lado "B"? '))

hipotenusa = (ladoA ** 2 + ladoB ** 2) ** 0.5

casas = int(input('Quantas casas decimais gostaria de ver? '))

print(f"O comprimento da hipotenusa é {hipotenusa:.{casas}f}")
