import requests

my_data = {"name": "Tarun", "email": "tarun@example.com"}
r = requests.post("https://www.w3schools.com/php/welcome.php", data=my_data)

f = open("myfile.html", "w+")
f.write(r.text)