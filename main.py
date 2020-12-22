import base64


content = 'sam is a good man'
print(base64.b64encode(content.encode()))