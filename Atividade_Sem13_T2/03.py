# 3. Escreva um programa que ler a nota de 50 alunos. Mostre uma lista apenas com os índices dos alunos que tem nota maior ou igual a 6 (seis).

# Function to analyze student grades and identify approved students
def analysis():
    # Create an empty list to store student grades
    studList = []
    # Create an empty list to store indices of approved students
    approvedStud = []

    # Iterate through a loop 50 times to input 50 grades
    for elem in range(50):
        # Input a grade as a floating-point number
        note = float(input(f"Digite a nota do {elem + 1}º aluno: "))
        # Append the grade to the list of student grades
        studList.append(note)
        # Check if the grade is greater than or equal to 6 (considered as passing)
        if note >= 6:
            # Append the index of the approved student to the list
            approvedStud.append(elem)
    # Return the list of indices of approved students
    return approvedStud

# Main function
def main():
    # Call the analysis function to get the list of approved students' indices
    approved = analysis()
     # Call the analysis function to get the list of approved students' indices
    print(f"Índices dos alunos aprovados: {approved}")
# Identify function main for execute
if __name__ == "__main__":
    main()