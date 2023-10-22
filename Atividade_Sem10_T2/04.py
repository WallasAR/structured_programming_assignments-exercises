# 04. Modifique mais um vez a canção dos programadores, dessa vez, gerando a canção dos bons programadores, que resolvem 11 erros de cada vez e ao chegar a zero declaram que o software está estabilizado. Atenção para o exemplo a seguir, especialmente, os versos finais.
# 99 bugs no software, pegue onze deles e conserte...
# Tecle “Ctrl+F5”
# 88 bugs no software, pegue onze deles e conserte...
# Tecle “Ctrl+F5”
# 77 bugs no software, pegue onze deles e conserte...
# Tecle “Ctrl+F5”
# ...
# 11 bugs no software, pegue onze deles e conserte...
# Tecle “Ctrl+F5”
# Sem erros no software! Está estabilizado!

# Creation of the function "cantion" for data processing
def cantion():
    # Repetition structure that follows an interval between 99 and 250, going from eleven to eleven in decreasing fashion, showing this interval on the screen
    for num in range(99, 0, -11):
        # Data output
        print(f'{num} bugs no software, pegue onze deles e conserte...\nTecle "Ctrl+F5"')
    # Shows a final text on the screen after the repeating structure
    print("Sem erros no software! Está estabilizado!")
# Creating the main function
def main():
    # Function call "cantion"
    cantion()
# Identify function main for execute
if __name__ == "__main__":
    main()