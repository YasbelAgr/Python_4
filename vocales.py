import vocales
def contar_vocales(frase):
    vocales="aeiou"
    contador=0
    for letra in frase.lower():
        if letra in vocales:
            contador+=1
    return contador
        
frase =input ("introduce una frase")
print(f"la frase tiene {contar_vocales(frase)} vocales")
