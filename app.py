from flask import Flask, jsonify, request 
#request htttp
#jsonnify para kson
#flask es la envoltura

app= Flask(__name__) #inicializar una apliacion de tipo flask

#url= 'http://localhost:5000' #necesito url
@app.route('/')
def home(): #ruta principla
    return jsonify({"mensaje":"Bienvenido a mi microservicio!"})

@app.route('/api/sumar',methods=['POST']) #endpoint lugares donde van a llegar los clientes
def sumar(): 
        data= request.get_json() ##trasnforma la perticion que tengo y trasnforma ajson
        a=data.get('a')
        b=data.get('b')
        
        if a is None or b is None:
             return jsonify({'error':'Parametros ay b son requeridos'}),400 # errror de cliente 400, error en el servidor 500 , 200 errror exitoso
        return jsonify({'resultado':a+b})

@app.route('/api/info',methods=['GET']) 
def info():
     return({
          'nombre': 'Microservicio Clase 1 Tratamiento de DAtos',
          'version':'1.0.0'
          
     })
if __name__ =='__main__': #Ejecuta mi apliacion cuando yo llame el script
    app.run(debug=True, host='0.0.0.0', port =5000) #cuando ejecutes corre el app, que app la app de flask, host local 0.0.0.0 puerto 8080

