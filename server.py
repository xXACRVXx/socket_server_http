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
    request = Conexion.recv(1024).decode('utf-8')
    
    string_list = request.split(' ')
    print(string_list)
    method = string_list[0]
    requesting_file = string_list[1]
    #requesting_file = '/templates'+requesting_file
    print('Client request',requesting_file)

    myfile = requesting_file.split('?')[0]
    myfile = myfile.lstrip('/')
    
    print(f'primer {myfile} ')
    if(myfile == ''):
        myfile = 'templates/index.html'
    if(myfile == 'login'):
        myfile = 'templates/login.html'
    


    try:
        file = open(myfile , 'rb')
        response = file.read()
        file.close()

        header = 'HTTP/1.1 200 OK\n'

        if(myfile.endswith('.jpg')):
            mimetype = 'image/jpg'
        elif(myfile.endswith('.css')):
            mimetype = 'text/css'
        elif(myfile.endswith('.pdf')):
            mimetype = 'application/pdf'
        elif(myfile.endswith('.apk')):
            mimetype = 'application/pdf'
        else:
            mimetype = 'text/html'

        header += 'Content-Type: '+str(mimetype)+'\n\n'

    except Exception as e:
        print("-")
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><body>Error 404: File not found</body></html>'.encode('utf-8')

    final_response = header.encode('utf-8')
    final_response += response
    Conexion.send(final_response)
    Conexion.close()
