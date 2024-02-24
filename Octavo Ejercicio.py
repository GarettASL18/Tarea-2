# Elige un número de dos dígitos
numero = 18

# Extrae los dígitos individualmente
digito1 = numero // 10  # Divide por 10 para obtener el primer dígito
digito2 = numero % 10   # Obtiene el segundo dígito utilizando el módulo 10

# Suma los dígitos individualmente
suma_digitos = digito1 + digito2

# Muestra el resultado
print(f"El número es {numero}")
print(f"La suma de los dígitos es: {suma_digitos}")
