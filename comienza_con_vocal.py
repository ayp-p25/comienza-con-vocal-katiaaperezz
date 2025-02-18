"""
Comienza con vocal
"""
#Declaraciones
vocal= 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú'
# Entradas
palabra = input("Escribe una palabra: ")

# Proceso
if palabra.startswith(vocal):
    resultado = "'" + palabra + "'" + " comienza con vocal"
else: 
    resultado = "'" + palabra + "'" + " no comienza con vocal"
# Salidas
print(resultado)
