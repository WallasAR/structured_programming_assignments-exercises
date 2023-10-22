# 02. Modifique a canção dos programadores do exercício anterior para incluir o refrão: Tecle “Ctrl+F5”. Termine a canção com “Vamos fazer mais um café!”.
# 99 bugs no software, pegue um deles e conserte...
# Tecle “Ctrl+F5”
# ...
# 250 bugs no software, pegue um deles e conserte...
# Tecle “Ctrl+F5”
# Vamos fazer mais um café!

# Creation of the function "cantion" for data processing
def cantion():
    # Repetition structure that follows a range between 99 and 250, showing this range on the screen
    for num in range(99, 251):
        # Data output
        print(f'{num} bugs no software, pegue um deles e conserte...\nTecle "Ctrl+F5"')
    # Shows a final text on the screen after the repeating structure
    print("Vamos fazer mais um café!")
# Creating the main function
def main():
    # Function call "cantion"
    cantion()
# Identify function main for execute
if __name__ == "__main__":
    main()