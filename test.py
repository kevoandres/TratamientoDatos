import requests


def request_info():
    url= 'http://localhost:5000/api/info'
    response =requests.get(url)
    return response.json()
def request_sumar(a,b):
    url= 'http://localhost:5000/api/sumar'
    data={ ##parametros en forma de diccionario o enforma json
        'a':a,
        'b':b
    }
    response= requests.post(url,json=data)
    return response.json()

respuesta= request_sumar(5,10)
print(f"REsultado de sumar: {respuesta}")

