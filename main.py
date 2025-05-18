import requests

#Funcion para obtener el clima:

def obtener_clima():
    ciudad = entrada.get()
    api_key = "" #Generamos e ingresamos la api_key de Weatherapi.com aqui
    try: 
        respuesta = requests.get(f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={ciudad}&lang=es")
        clima = respuesta.json()

        if 'error' in clima:
            label_clima['text'] = f"Error:¨{clima['error']['message']}"
        else:
            label_clima['text'] = f"El clima en tu {ciudad} es de {clima['current']['temp_c'])°C con {clima['current']['condition'['text']'}"
    except:
        label_clima['text'] = "Error al obtener el clima"