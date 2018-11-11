import cgi
import datetime
import json


form = cgi.FieldStorage()
answer = form.getfirst("answer", "не задано")
date_now = datetime.datetime.now()
if answer == "a1":

    out_date = json.dumps({"date now": str(date_now),
                           "Year now": str(date_now.year),
                           "Month now": str(date_now.month),
                           "Day now": str(date_now.day)
                           }, separators=(',', ':'), sort_keys=True, indent=4)
elif answer == "a2":
    out_date = json.dumps({"date now": str(date_now),
                           "Hour now": str(date_now.hour),
                           "Minute now": str(date_now.minute)
                           }, separators=(',', ':'), sort_keys=True, indent=4, default=str)
else:
    out_date = json.dumps({"response": "Error"
                           }, separators=(',', ':'), sort_keys=True, indent=4)




print("Content-type: application/json\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>Вывод json dump: {}</p>".format(out_date))

print("""</body>
        </html>""")