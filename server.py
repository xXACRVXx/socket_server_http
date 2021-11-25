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
    archivo_solicitado = string_list[1]
    #archivo_solicitado = '/templates'+archivo_solicitado 
    
    print('Client request',archivo_solicitado)

    archivo = archivo_solicitado.split('?')[0]
    archivo = archivo.lstrip('/')
    
    print(f'primer {archivo} ')
    if(archivo == ''):
        archivo = 'templates/index.html'
    if(archivo == 'login'):
        archivo = 'templates/login.html'
    


    try:
        El_archivo = open(archivo , 'rb')
        respuesta = El_archivo.read()
        El_archivo.close()

        header = 'HTTP/1.1 200 OK\n'

        if(archivo.endswith('.jpg')):
            mimetype = 'image/jpg'
        elif(archivo.endswith('.css')):
            mimetype = 'text/css'
        elif(archivo.endswith('.pdf')):
            mimetype = 'application/pdf'
        elif(archivo.endswith('.apk')):
            mimetype = 'application/pdf'
        else:
            mimetype = 'text/html'

        header += 'Content-Type: '+str(mimetype)+'\n\n'

    except Exception as e:
        print("-")
        header = 'HTTP/1.1 404 Not Found\n\n'
        respuesta = '<html><body>Error 404: El_archivo not found</body></html>'.encode('utf-8')

    respuesta_final = header.encode('utf-8')
    respuesta_final += respuesta
    Conexion.send(respuesta_final)
    Conexion.close()
