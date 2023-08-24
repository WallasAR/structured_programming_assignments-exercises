# Desafio: O ano 3000

print("Em que ano você nasceu?")
personyear = int(input(">> "))

print("Em que ano você quer saber sua idade?")
definedyear = int(input(">> "))

newyear = definedyear - personyear 

if(definedyear > personyear):
    print("Em {} você terá {} anos!" .format(definedyear,newyear))
else:
    print("A sua resposta não fez sentido. Não sou um programa tão tolo!")