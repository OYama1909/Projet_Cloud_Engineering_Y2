import base64

def decode_base64(data):
    """
    Décode une chaîne encodée en base64 et renvoie la chaîne décodée.
    :param data: chaîne encodée en base64 à décoder.
    :return: chaîne décodée.
    """
    # D'abord, assurez-vous que la chaîne est un type bytes
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Décoder la chaîne base64
    decoded_data = base64.b64decode(data)
    
    # Convertir les données décodées en chaîne UTF-8, si nécessaire
    try:
        return decoded_data.decode('utf-8')
    except UnicodeDecodeError:
        # Retourner les données brutes décodées si elles ne peuvent pas être converties en UTF-8
        return decoded_data

# Exemple d'utilisation
encoded_string = "SGVsbG8sIFdvcmxkIQ=="  # "Hello, World!" encodé en base64
decoded_string = decode_base64(encoded_string)
print("Chaîne décodée :", decoded_string)
