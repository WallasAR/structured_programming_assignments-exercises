# 04. Escreva um programa que leia a data de nascimento do usuário, e informa qual o seu signo. Considere exatamente: Áries (21/03 a 19/04); Touro (20/04 a 20/05); Gêmeos (21/05 a 21/06); Câncer (22/06 a 22/07); Leão (23/07 a 22/08); Virgem (23/08 a 22/09); Libra (23/09 a 22/10); Escorpião (23/10 a 21/11); Sagitário (22/11 a 21/12); Capricórnio (22/12 a 19/01); Aquário (20/01 a 18/02); Peixes (19/02 a 20/03);

# Processing function
def sign(month, day):
    # Conditional structure that returns the sign corresponding to the given day and month
    if ((month == 3 and day >= 21) or (month == 4 and day <= 19)):
        return "Áries"
    elif ((month == 4 and day >= 20) or (month == 5 and day <= 20)):
        return "Touro"
    elif ((month == 5 and day >= 21) or (month == 6 and day <= 21)):
        return "Gêmeos"
    elif ((month == 6 and day >= 22) or (month == 7 and day <= 22)):
        return "Câncer"
    elif ((month == 7 and day >= 23) or (month == 8 and day <= 22)):
        return "Leão"
    elif ((month == 8 and day >= 23) or (month == 9 and day <= 22)):
        return "Virgem"
    elif ((month == 9 and day >= 23) or (month == 10 and day <= 22)):
        return "Libra"
    elif ((month == 10 and day >= 23) or (month == 11 and day <= 21)):
        return "Escorpião"
    elif ((month == 11 and day >= 22) or (month == 12 and day <= 21)):
        return "Sagitário"
    elif ((month == 12 and day >= 22) or (month == 1 and day <= 19)):
        return "Capricórnio"
    elif ((month == 1 and day >= 20) or (month == 2 and day <= 18)):
        return "Aquário"
    elif ((month == 2 and day >= 19) or (month == 3 and day <= 20)):
        return "Peixes"

# Main function
def main():
    # Variables "day, month" receives inputs and all are converted to int type
    day = int(input("Qual o dia do seu nascimento?\n "))
    month = int(input("Qual o mês em que você nasceu?\n"))
    # The variable "result" receives the function call "sign"
    result = sign(month, day)
    # Shows the values ​​of the variables "result" on the screen
    print(f"Seu signo é {result}")

# Identify function main for execute
if __name__ == "__main__":
    main()