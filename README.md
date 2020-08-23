# Smtp-Vrfy
* Smtp-Vrfy python 2.7 
## how to use 
* git clone https://github.com/jac11/Smtp-Vrfy.git
* chmod +x Smtp-Vrfy.py
* to check all  option open help menu by typing Smtp-Vrfy.py -h or --help
* follow the help menu to use option 
##  [ help menu overview ]
```
usage: Smtp-Vrfy.py [-h] [-t] [-u] [-w] [-p]

Example: ./Smtp-Vrfy.py -t 10.195.100.67 -w /usr/share/wordlists/rockyou.txt

optional arguments:
  -h, --help        show this help message and exit
  -t , --target     Target ip address or name
  -u , --user       for only one username
  -w , --wordlist   read from wordlist list same like rockyou.txt
  -p , --port       use specific port

```

### [Enumeration]

* Smtp-Vrfy  use for SMTP Enumeration VRFY SCAN
* the Smtp-Vrfy will create file have all users exists
* default ports  25-465-587 
* ./Smtp-Vrfy.py -t 10.195.100.67 -w /usr/share/wordlists/rockyou.txt
* specific port use option -p 
* ./Smtp-Vrfy.py -t 10.195.100.67 -w /usr/share/wordlists/rockyou.txt -p 2525
```
#-----------------------------------------------------------#
|                     SMTP-VRFY                             |
#-----------------------------------------------------------#

[*] host name     |................ 10.195.100.229
[*] user vrfy     |................ None
[*] users list    |................ /home/jac/Desktop/code/wordlist.txt
[*] ping host     |................ True
[*] host Status   |................ Online
[*] default ports |................ 25-465-587
============================================================
port scan start.......
=========================
##-port 25  is open
##-port 465  is closed
##-port 587  is closed
----------------------------------------
[*]##-Enumeration start in  port  25
----------------------------------------
[-] 10.195.100.229 .... 12345 ............[NOT Exists]
[-] 10.195.100.229 .... 123456789 ............[NOT Exists]
[-] 10.195.100.229 .... password ............[NOT Exists]
[+] 10.195.100.229 .... user ............[Exists]
[-] 10.195.100.229 .... iloveyou ............[NOT Exists]
[-] 10.195.100.229 .... princess ............[NOT Exists]
[-] 10.195.100.229 .... 1234567 ............[NOT Exists]
[-] 10.195.100.229 .... rockyou ............[NOT Exists]
[-] 10.195.100.229 .... 12345678 ............[NOT Exists]
[-] 10.195.100.229 .... abc123 ............[NOT Exists]
[+] 10.195.100.229 .... msfadmin ............[Exists]
[-] 10.195.100.229 .... nicol ............[NOT Exists]
[-] 10.195.100.229 .... daniel ............[NOT Exists]
[-] 10.195.100.229 .... babygirl ............[NOT Exists]
[+] 10.195.100.229 .... root ............[Exists]
[-] 10.195.100.229 .... ljguigfyu ............[NOT Exists]
[-] 10.195.100.229 .... \kljvkhfhyk ............[NOT Exists]
[-] 10.195.100.229 .... kjhgcyhjv\ ............[NOT Exists]
[-] 10.195.100.229 .... 545455 ............[NOT Exists]
[-] 10.195.100.229 .... 999 ............[NOT Exists]
[-] 10.195.100.229 .... 09990 ............[NOT Exists]

	*********END**OF**WORD**LIST*********


===============
Users Exists
====================
[*] user
[*] msfadmin
[*] root
 
```

### [for connect]
* administrator@jacstory.tech
* thank you 
