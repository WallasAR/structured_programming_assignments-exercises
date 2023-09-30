# 03. Escreva um programa que leia 5 números inteiros e escreva o maior e o menor deles. Considere que todos os valores são diferentes. NÃO use as funções embutidas min() e max().

# Creation of the function "maximun" for data processing
def maximum(var1, var2, var3, var4, var5):
    # Conditional structures that check whether one number is greater than another number
    if (var1 > var2) and (var1 > var3) and (var1 > var4) and (var1 > var5):
        return var1
    if (var2 > var1) and (var2 > var3) and (var2 > var4) and (var2 > var5):
        return var2
    if (var3 > var1) and (var3 > var2) and (var3 > var4) and (var3 > var5):
        return var3
    if (var4 > var1) and (var4 > var2) and (var4 > var3) and (var4 > var5):
        return var4
    else:
        return var5

# Creation of the function "minimun" for data processing
def minimum(var1, var2, var3, var4, var5):
    # Conditional structures that check whether a number is smaller than another number
    if (var1 < var2) and (var1 < var3) and (var1 < var4) and (var1 < var5):
        return var1
    if (var2 < var1) and (var2 < var3) and (var2 < var4) and (var2 < var5):
        return var2
    if (var3 < var1) and (var3 < var2) and (var3 < var4) and (var3 < var5):
        return var3
    if (var4 < var1) and (var4 < var2) and (var4 < var3) and (var4 < var5):
        return var4
    else:
        return var5

# Creating the main function
def main():
    # Variables "num1, num2, num3, num4, num5" receive input and are converted to integer
    num1 = int(input("Informe o primeiro número inteiro: "))
    num2 = int(input("Informe o segundo número inteiro: "))
    num3 = int(input("Informe o terceiro número inteiro: "))
    num4 = int(input("Informe o quarto número inteiro: "))
    num5 = int(input("Informe o quinto número inteiro: "))
    # Variables "maxi" and "mini" receive the call of the functions "maximum" and "minimum" respectively, having the largest and smallest number as their value.
    maxi = maximum(num1, num2, num3, num4, num5)
    mini = minimum(num1, num2, num3, num4, num5)
    # Prints the value of the variables "maxi" and "mini" on the screen.
    print(f"O valor maximo corresponde a {maxi}\nE o valor minimo {mini}")

# Identify function main for execute
if __name__ == "__main__":
    main()