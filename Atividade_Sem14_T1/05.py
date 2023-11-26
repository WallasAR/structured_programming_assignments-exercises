# 5. Foram anotados nomes, idades e alturas de 30 alunos. Faça um programa que determine quais alunos com mais de 13 anos possuem altura inferior à média de altura dos alunos. Considerar a altura arredondando para duas casas decimais.

# Function that calculates the average height of the students
def averageHeight(students):
    totalHeight = 0

    # Calculating the total height of all students
    for student in students:
        totalHeight += student[2]
    # Calculating the average height
    avgHeight = totalHeight / len(students)

    # Returning the rounded average height
    return round(avgHeight, 2)  

# Collects students' information
def getInfoStudents():
    students = []

    # Adding information for each student (name, age, height)
    for i in range(30):
        name = input(f"Nome do aluno {i + 1}: ")
        age = int(input(f"Idade do(a) aluno(a) {name}: "))
        height = float(input(f"Altura do(a) aluno(a) {name}: "))
        # Appending the student's information
        students.append((name, age, height))  

    # Returning the list of students
    return students  

# Check students over 13 years old with height below average
def ElegibleStudents(students, avg):
    eligible_students = []

    # Checking for students above 13 years old and with height below average
    for student in students:
        if student[1] > 13 and student[2] < avg:
            eligible_students.append(student)  # Appending eligible students

    return eligible_students  # Returning the list of eligible students

# Main Function
def main():
    # Getting students' information
    students = getInfoStudents()  

    # Calculating the average height
    avg = averageHeight(students)  

    # Finding eligible students
    eligible_students = ElegibleStudents(students, avg)  
    
    print("MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA")
    if eligible_students:
        # Displaying information for eligible students
        for student in eligible_students:
            print(f"Nome: {student[0]}, Idade: {student[1]}, Altura: {student[2]:.2f}")
    else:
        print("Não há alunos com mais de 13 anos e altura inferior à média.")

# Identify function main for execute
if __name__ == "__main__":
    main()
