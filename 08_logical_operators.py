#and
age = 25
have_a_pasport = True

# if age >= 18 and  have_a_pasport == True:
#     print('The person can enter the country')
# else:
#     print('The person cannot enter the country')
#or
# is_uchiha = False
# is_uzumaki = False

# if is_uchiha == True or is_uzumaki == True:
#     print('Puede entrar a la aldea de la hoja')
# else:
#     print('No puede entrar a la aldea ')

#not 
# is_destroyed = False

# if not is_destroyed :
#     print('La aldea esta destruida')
# else:
#     print('La aldea esta a salvo')

#short-circuit    
def verificar():
    print("Se ejecutó verificar()")
    return True

resultado = False and verificar()
print(resultado)

message = '''
Resultado:False

Nota que "Se ejecutó verificar()" nunca se imprime,
porque como el primer valor ya es False, 
Python no necesita evaluar la función.
'''
