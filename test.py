from programa import es_primo  # Importamos la función es_primo

# Pruebas directas
print("Prueba de números primos:")
print(es_primo(2))  # Se espera True (es primo)
print(es_primo(3))  # Se espera True (es primo)
print(es_primo(5))  # Se espera True (es primo)
print(es_primo(7))  # Se espera True (es primo)

print("\nPrueba de números no primos:")
print(es_primo(4))  # Se espera False (no es primo)
print(es_primo(6))  # Se espera False (no es primo)
print(es_primo(8))  # Se espera False (no es primo)
print(es_primo(9))  # Se espera False (no es primo)

print("\nPrueba de números menores que 1:")
print(es_primo(0))  # Se espera False (no es primo)
print(es_primo(-1)) # Se espera False (no es primo)
print(es_primo(1))  # Se espera False (no es primo)
