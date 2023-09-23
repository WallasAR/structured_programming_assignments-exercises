# 01. Escreva um programa que leia o nome e o estado civil de uma pessoa, considere apenas “1” para casado e “2” para solteiro. Se a pessoa for casada, leia, também, o nome do cônjuge. Mostre quantos caracteres no total existem no(s) nome(s) lido(s).

def maritstatus(num, name):
    if (num == 1):
        spouse = str(input()).strip()
        return len(spouse) + len(name)
    elif (num == 2):
        return len(name)
     
def main():
    name = str(input()).strip()
    status = int(input())

    namespouse = maritstatus(status, name)
    
    if maritstatus:
        print(f"{namespouse}")
    else:
        print(f"{name}") 

if __name__ == "__main__":
    main()