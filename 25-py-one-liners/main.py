python -m http.server 8000

python -c "import random, string; password_length = 10; password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(password_length)); print(password)"

python -c "from datetime import date; birthdate = date(1990, 5, 15); age = (date.today() - birthdate).days // 365; print(age)"

python -c "celsius_temperature = 25; fahrenheit_temperature = celsius_temperature * 9/5 + 32; print(fahrenheit_temperature)"

python -c "import math; number = 5; factorial = math.factorial(number); print(factorial)"

python -c "import re; text = 'Contact us at email@example.com or support@example.com'; emails = re.findall(r'\S+@\S+', text); print(emails)"

python -c "import uuid; uuid_val = uuid.uuid4(); print(uuid_val)"

python -c "string = 'madam'; is_palindrome = string == string[::-1]; print(is_palindrome)"

#pip install qrcode
python3 -c "import qrcode; qr = qrcode.QRCode(version=1, box_size=10, border=5); qr.add_data('Hello, world\!'); qr.make(fit=True); qr_img = qr.make_image(); qr_img.save('qr_code.png')"

#pip install Pillow
python3 -c "from PIL import Image; image_path = 'image.jpg'; image = Image.open(image_path).convert('L'); image.save('grayscale.jpg')"

python -c "print('hello world'[::-1])"





