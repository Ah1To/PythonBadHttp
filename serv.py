from http.server import HTTPServer, CGIHTTPRequestHandler
#из модуля http.server импортирую HTTPServer и CGIHTTPRequestHandler для дальнейшего использования

#создаю переменые host и port и описываю их для создания сервера и слушателя на порт
host = 'localhost'
port = 8080
#создаю сервер с параметрами host и port и обработчиком событий CGIHTTPRequester
httpd = HTTPServer((host, port), CGIHTTPRequestHandler)
#Запускаю сервер
httpd.serve_forever()

#Ы задаче используется простой сервер и cgi скрипты в данном случае мой скрипт помещен в директорию cgi-bin, 
#CGIHTTPRequester по умолчанию "подхватывает" index.html в котром я поставил выбор на вывод информации, после чего запускается 
#скрипт в cgi-bin/form.py, который должет от выбора пользователя вывести в формате json либо время либо дату времени сейчас
#если выбор не коректный, то выводтся ошибка, 
