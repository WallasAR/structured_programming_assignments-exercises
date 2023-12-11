# 05.Escreva um programa que lê matrícula, nome e duas notas de vários alunos e armazena tais notas em um dicionário, onde a chave é a matrícula do aluno. A entrada de dados deve terminar quando for lida uma string vazia como matrícula. Após o término da leitura dos dados de entrada, use uma função que retorna a média do aluno, dado sua matrícula. Mostre a média dos alunos até o programa ser finalizado com a leitura de uma matrícula vazia.

# Function to calculate average of a list of numbers
def average(notes):
    return sum(notes) / len(notes) if notes else 0  # Calculates the average if notes is not empty, otherwise returns 0

# Main function
def main():
    students = {}  # Dictionary to store student information

    # Loop to input student data
    while True:
        regist = input("Digite a matrícula do aluno (em branco para sair): ").strip()

        if regist == "":  # If input is blank, exit loop
            break
        
        name = input("Nome do aluno: ").strip()
        note1 = float(input("1ª nota: "))
        note2 = float(input("2ª nota: "))
        
        # Store student data in dictionary 'alunos' using student ID as key
        students[regist] = {'nome': name, 'notas': [note1, note2]}  

    # Loop to calculate and display average grades
    while True:
        selectedRegist = input().strip()  # Input desired student ID
        if selectedRegist == "":  # If input is blank, exit loop
            break
        
        if selectedRegist in students:  # If student ID exists in dictionary
            # Calculate average grade of the student using the 'average' function
            studAverage = average(students[selectedRegist]['notas'])  
            # Print student's name and their average grade with one decimal place
            print(f"{students[selectedRegist]['nome']}: {studAverage:.1f}")
        else:
             print("Matrícula não encontrada!")  # Display message if student ID is not found

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()

