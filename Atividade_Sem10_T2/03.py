# 03. Modifique a canção dos programadores novamente para aumentar os bugs de 7 em 7, iniciando em 99 e parando em 250 ou antes
# 99 bugs no software, pegue sete deles e conserte...
# Tecle “Ctrl+F5”
# 106 bugs no software, pegue sete deles e conserte...
# Tecle “Ctrl+F5”
# 113 bugs no software, pegue sete deles e conserte...
# Tecle “Ctrl+F5”
# ...
# Vamos fazer mais um café!

# Creation of the function "cantion" for data processing
def cantion():
    # Repetition structure that follows an interval between 99 and 250, going every seven, showing this interval on the screen
    for num in range(99, 250, 7):
        # Data output
        print(f'{num} bugs no software, pegue sete deles e conserte...\nTecle "Ctrl+F5"')
    # Shows a final text on the screen after the repeating structure
    print("Vamos fazer mais um café!")
# Creating the main function
def main():
    # Function call "cantion"
    cantion()
# Identify function main for execute
if __name__ == "__main__":
    main()