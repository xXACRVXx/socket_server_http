import socket 
import requests as Request
host , port = '0.0.0.0' , 8888

Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Server.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
Server.bind((host , port))
Server.listen(1)
print('servidor en el puerto',port)

while True:
    Conexion , address = Server.accept()
    Solicitud = Conexion.recv(1024).decode('utf-8')
    
    string_list = Solicitud.split(' ')
    print(string_list)
    method = string_list[0]
    Archivo_solicitado = string_list[1]
    #Archivo_solicitado = '/templates'+Archivo_solicitado
    print('Client request',Archivo_solicitado)

    Archivo = Archivo_solicitado.split('?')[0]
    Archivo = Archivo.lstrip('/')
    
    print(f'primer {Archivo} ')
    if(Archivo == ''):
        Archivo = 'templates/index.html'
    if(Archivo == 'login'):
        Archivo = 'templates/login.html'
    


    try:
        file = open(Archivo , 'rb')
        respuesta = file.read()
        file.close()

        header = 'HTTP/1.1 200 OK\n'

        if(Archivo.endswith('.jpg')):
            mimetype = 'image/jpg'
        elif(Archivo.endswith('.css')):
            mimetype = 'text/css'
        elif(Archivo.endswith('.pdf')):
            mimetype = 'application/pdf'
        elif(Archivo.endswith('.apk')):
            mimetype = 'application/pdf'
        else:
            mimetype = 'text/html'

        header += 'Content-Type: '+str(mimetype)+'\n\n'

    except Exception as e:
        print("-")
        header = 'HTTP/1.1 404 Not Found\n\n'
        respuesta = '<html><body>Error 404: File not found</body></html>'.encode('utf-8')

    respuesta_final = header.encode('utf-8')
    respuesta_final += respuesta
    Conexion.send(respuesta_final)
    Conexion.close()
