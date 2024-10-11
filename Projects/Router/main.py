from requests import post

from form_data import form_data

res = post("http://192.168.1.1/cgi-bin/check_auth.json", data=form_data)

print(res.text)
