list_of_school_subjects = [
    "Artificial neural networks",           #0
    "Generative artificial intelligence",   #1
    "Machine learning",                     #2
    "Practical quantum computing",          #3
    "Deep learning"                         #4
]



print("Materias disponibles: ")


for index, subject in enumerate(list_of_school_subjects):
    print(f"{index + 1}. {subject}")
    


selcted_optios = input("\nEscribe los números de las materias que deseas llevar, separados por comas:")

selected_subjects = []

for option in selcted_optios.split(","):
    option = option.strip()
    
    if option.isdigit():
        index = int(option)-1
        
        if 0 <= index < len(list_of_school_subjects):
            subject = list_of_school_subjects[index]
            
            if subject not in selected_subjects:
                selected_subjects.append(subject)
            
            
print("\nMaterias seleccionadas:")

if selected_subjects:
    print(*selected_subjects, sep="\n")
else:
    print("No seleccionaste ninguna materia.")