lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Adicione sua funcao abaixo!
def average(numbers):
    total = sum(numbers)
    resultado = float(total) / len(numbers)
    return resultado
    
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    
    return (0.1 * homework) + (0.3 * quizzes) + (0.6 * tests)
    
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
        
score = get_average(lloyd)
get_letter_grade(score)

    
def get_class_average(students):
    results = []
    for student in students:
        result = get_average(student)
        results.append(result)
    return average(results)
    
   
students = [lloyd, alice, tyler] #crio uma lista contendo os 3 dicionários
print get_class_average(students) #printo o resultado das médias dos 3 dicionários da função avarage
for student in students: #percorro a lista com os 3 dicionários
    print get_letter_grade(get_average(student)) #imprimo o resultado em letas "A" "B" "C" "D" ou "E" dos três dicionários