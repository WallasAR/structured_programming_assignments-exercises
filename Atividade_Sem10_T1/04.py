# 04. Escreva um programa que gere a seguinte sequência:

# 10, 20, 30, 40, ..., 990, 1000.

# Considere a separação dos números por vírgula seguido de espaço em branco e o ponto no final da sequência.

# Creation of the function "showNums" for data processing
def showNums():
    # Initialization of variable "string" of type string
    string = ""
    # Repetition structure that cycles through a range between 0 and 1000, every 10 
    for show in range(10, 1000, 10):
        # "String" receives iterations of the counter variable "show"
        string += str(show) + ", "  
    # Variable "string" receives iteration of the last number of the structure, properly formatted
    string += "1000."
    return string 
# Creating the main function
def main():
    # The variable "result" receives the call to the "showNums" function
    result = showNums()
    # Shows the result of the variable "result" on the screen
    print(f"{result}")
# Identify function main for execute
if __name__ == "__main__":
    main()