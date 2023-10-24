import re

def obtener_frases(texto):
    patron = r'[.!?]+\s*'
    frases = re.split(patron, texto)

    frases = [frase.replace('¿', '').replace('¡', '').strip() for frase in frases if frase.strip()]

    return frases

texto = "Este es un texto largo con muchas frases. ¡Este es un texto con un signo de exclamación! ¿Este es un texto con un signo de interrogación?"

frases = obtener_frases(texto)
print(frases)



