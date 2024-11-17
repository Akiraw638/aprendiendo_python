    #funcion para encriptar cadenas de texto:
    #inputValue --> cadena de entrada
    #keys --------> diccionario clave:valor
    #token -------> carácter que señala el inicio - fin de cada caracter encriptado

def encrypt(inputValue, keys, token):
    # Inicializamos una cadena para almacenar el resultado encriptado
    encrypted_text = ""
    
    # Recorremos cada carácter en inputValue
    
    for char in inputValue:
        # Damos mensage error si algun carácter de token coincide con alguno de la cadena inputValue:
        if char in token:
            print("Error: no es posible encriptar la cadena, verifique los parámetros de entrada.")
            exit()
        # Si el carácter está en keys, lo encriptamos con el token y el valor de keys
        elif char in keys:
            encrypted_text += token + str(keys[char]) + token
        else:
            # Si no está en keys, añadimos el carácter sin encriptar
            encrypted_text += char
            
    return encrypted_text


#encrypted_text = encrypt ("Hola que tal#",{"a": 1, "e": 2, "U": 3},"#")

#print(encrypted_text)

def decrypt(inputValue, keys, token):
    # Inicializamos cadena para almacenar el resultado desencriptado
    decrypted_text = ""
    
    # Invertimos el diccionario de claves para que el valor numérico apunte a la letra original
    reversed_keys = {v: k for k, v in keys.items()}
    
    i = 0
    while i < len(inputValue):
        # Verificamos si el carácter actual es el token de inicio
        if inputValue[i] == token:
            # Buscamos el número encriptado entre los tokens
            j = i + 1
            while j < len(inputValue) and inputValue[j] != token:
                j += 1
            
            # Extraemos el número y lo convertimos si está en el formato correcto
            if j < len(inputValue):
                encrypted_num = inputValue[i + 1:j]
                if encrypted_num.isdigit():
                    num = int(encrypted_num)
                    # Reemplazamos el número con la letra correspondiente
                    if num in reversed_keys:
                        decrypted_text += reversed_keys[num]
                # Movemos el índice después del segundo token
                i = j
        else:
            # Agregamos cualquier carácter no encriptado directamente al texto desencriptado
            decrypted_text += inputValue[i]
        
        i += 1
    
    return decrypted_text

decrypted_text = decrypt("M+0+s +3+m+0+gos son G+8+NI+4+L+8+S.", {"i":0,"E":8,"a":3,"A":4},"+")

print(decrypted_text)
print("modificado")
