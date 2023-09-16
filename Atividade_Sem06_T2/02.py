# 02. Nem sempre as transações financeiras resultam em números inteiros. Vamos usar o round() para resolver isso! Peça ao usuário para inserir uma quantidade de dinheiro. Em seguida, arredonde esse valor para o número inteiro mais próximo e imprima o resultado.

# Processing function
def roundNum(money):
    # returns the result of the number rounded without decimal places and then transformed into an integer type
    return int(round(money, 0))

def main():
    # The "money" variable receives input and is converted to float type
    money = float(input("Insira algum valor monetário: "))
    # The variable "result" receives the function call "roundNum", sending the necessary parameter and receiving the result
    result = roundNum(money)
    # Prints the result of the "result" variable on the screen
    print(f"O valor arredondado é de {result} coins")

# Identify function main for execute
if __name__ == "__main__":
    main()