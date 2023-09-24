# 05. Escreva um programa que leia três números e mostre na tela em ordem crescente.

# Processing function
def ascOrder(v1, v2, v3):
    # Variable "mini" receives the smallest number among the three numbers read
    mini = min(v1, v2, v3)
    # Variable "maxi" receives the largest number among the three numbers read
    maxi = max(v1, v2, v3)
    # Variable "mid" receives an operation in order to discover the number corresponding to the middle
    mid = v1 + v2 + v3 - mini - maxi
    return mini, mid, maxi

# Main function
def main():
     # Variables "var1, var2, var3" receives inputs and all are converted to int type
    var1 = int(input("Digite o primeiro número inteiro: "))
    var2 = int(input("Digite o segundo número inteiro: "))
    var3 = int(input("Digite o terceiro número inteiro: "))
    # The variables "mini, mid, maxi" receive a call to the function "ascOrder", giving the necessary parameters and receiving the respective results according to the return "return mini, mid, maxi"
    mini, mid, maxi = ascOrder(var1, var2, var3)
    # Shows the value of the variables "mini", "mid" and "maxi" on the screen
    print(f"Os números ordenados de forma crescente:\n{mini} - {mid} - {maxi}")

# Identify function main for execute
if __name__ == "__main__":
    main()