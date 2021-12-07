#!/usr/bin/env python3

import requests

filename = 'test.pdf'
container = 'attachments'

# Data
endpoint = 'azure logic app url'
payload = {
    "to": 'change@me.com',
    "subject": 'Testing in progress',
    "body": "This is email body of test email!",
    "file_name": filename,
    "file_path": f'/{container}/{filename}',
}

# HTTP POST request
resp = requests.post(endpoint, json=payload)

print('response', resp.status_code)
