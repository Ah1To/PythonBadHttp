from http.server import HTTPServer, CGIHTTPRequestHandler
#из модуля http.server импортирую HTTPServer и CGIHTTPRequestHandler для дальнейшего использования

#создаю переменые host и port и описываю их для создания сервера и слушателя на порт
host = 'localhost'
port = 8080
#создаю сервер с параметрами host и port и обработчиком событий CGIHTTPRequester
httpd = HTTPServer((host, port), CGIHTTPRequestHandler)
#Запускаю сервер
httpd.serve_forever()
