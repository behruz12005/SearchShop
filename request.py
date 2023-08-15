import requests

# API URL
api_url = 'http://127.0.0.1:8000/api/'

# Faylni yuborish uchun fayl nomi va manzil
file_path = 'categories.csv'

# Faylni yuborish uchun POST so'rovi tuzamiz
files = {'file': open(file_path, 'rb')}
data = {'username': 'behruz', 'password': 'behruz2005'}  # To'g'ri parolni kiriting

response = requests.post(api_url, files=files, data=data)

# Javobni tekshirish
if response.status_code == 201:
    print('Fayl muvaffaqiyatli yuborildi va saqlandi.')
    print('Javob:', response.json())
else:
    print('Xatolik yuz berdi. Javob kodi:', response.status_code)
    print('Xatolik ma\'lumotlari:', response.text)
