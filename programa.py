def es_primo(numero):
    # Casos para los números menores o iguales a 1
    if numero <= 1:
        return False
    
    # Verifica si el número es divisible por algún número entre 2 y la raíz cuadrada de 'numero'
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    
    # Si no se encontró ningún divisor, el número es primo
    return True

# Pide al usuario un número
numero_usuario = int(input("Introduce un número para verificar si es primo: "))

# Llama a la función y muestra el resultado
if es_primo(numero_usuario):
    print(f"El número {numero_usuario} es primo.")
else:
    print(f"El número {numero_usuario} no es primo.")

