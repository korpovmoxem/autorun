import base64


def authentication(key):
    credentials = {
        'Bitrix': 'aHR0cHM6Ly92YzRkay5iaXRyaXgyNC5ydS9yZXN0LzMxMS93a3EwYTBtdnN2Zm1vc2VvLw==',
        'Google': 'Yml0cml4MjQtZGF0YS1zdHVkaW8tMjI3OGM3YmZiMWE3Lmpzb24=',
        '1c@gk4dk.ru': 'Q1JZMWJtOEhqQlRoaHMwSmU1R20=',
        'Yandex': 'eTBfQWdBQUFBQVlBQkR1QUFvdmJRQUFBQURueE43OFZHcTlncnEwUWJHcUJPT3RvZW1palNmWjBRMA==',
        'Chat-bot': 'aHR0cHM6Ly92YzRkay5iaXRyaXgyNC5ydS9yZXN0LzMxMS81d2UyNzJ6YXRwamJkcXNsLw==',
    }
    return base64.b64decode(credentials[key]).decode('utf-8')
