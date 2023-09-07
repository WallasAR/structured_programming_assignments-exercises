# 02. Escreva um programa que leia a idade de uma pessoa expressa em anos, meses e dias e mostra na tela a idade dessa pessoa expressa apenas em dias. Considerar sempre os anos com 365 dias e os messes com 30 dias.

# Processing
def onlyDays(y, m, d):
    # variable "calc" save the result of equation
    calc = (y*365) + (m*30) + d
    return calc

# main function 
def main():
    # variables "year, month, days" receives inputs and all are converted to int type
    year = int(input())
    month = int(input())
    days = int(input())
    # variable "result" receives the result of the function "onlyDays"
    result = onlyDays(year, month, days)
    #output
    print(result)

if __name__ == '__main__':
    main()