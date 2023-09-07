# 04. Escreva um programa que leia um valor inteiro e mostra na tela no valor booleano True caso o número lido seja maior que 100 ou False caso contrário.

# Processing
def verif(var):
    # return True or False
    return bool(var > 100)

# main function
def main():
    # variable "var" receives input and converts to type integer
    var = int(input())
    # variable "result" receives the result of the function "verif"
    result = verif(var)
    # output  
    print(result)
# identify function main for execute

if __name__ == "__main__":
    main()

# note: In run.codes the code has made with conndictional structure, this version is correct for what was proposed.