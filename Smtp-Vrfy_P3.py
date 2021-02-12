#!/usr/bin/env python3


import socket 
import sys
import os
import argparse
import time 

W='\033[0m'     
R='\033[31m'    
Y="\033[1;33m" 
  
class SMTP_emn:
     
       def __init__(self): 
           global W
           global R   
           global Y    
           self.parser()
           self.main()
           
       def wordlist(self):
           try:
             self.path= os.path.abspath(self.args.wordlist)
             self.list= open(self.path)             
             self.line =self.list.readline() 
             with open('SMTP_'+self.args.target,'w') as file:
                  file = file.write("\n\n"+("="*15+"\n")+"Users Exists\n"+"="*20+"\n")
           except IOError :
                print ( " No such file or directory", self.path ) 
                exit()                                                               
       def ping_host(self):
              print ( )
              print ( "#-----------------------------------------------------------#")
              print ( Y+"|                     SMTP-VRFY                             |"+W)
              print ( "#-----------------------------------------------------------#")
              print ( )                                   
              print ( "[*] host name     |................" ,self.args.target)
              print ( "[*] user vrfy     |................" ,self.args.user ) 
              print ( "[*] users list    |................" ,self.args.wordlist)           
              print ( "[*] ping host     |................ True")
              response =  os.system("ping -c1 "+ "{}".format(self.args.target) + " > /dev/null 2>&1" ) 
              if response == 0 :
                  print ( "[*] host Status   |................ Online")  
                  print ( "[*] default ports |................ 25-465-587")
                  print (("="*60))
              else : 
                  print ( "[*] host Status   |................ Offline") 
                  print ( ("="*60)) 
                  exit() 
       def Check_port(self):
            try: 
               print ("port scan start......." )
               print ( Y+"="*25+W )
               PortList= [25,465,587]           
               for port in PortList:
                    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    sock.settimeout(3)
                    result = sock.connect_ex((self.args.target, port))                    
                    if result ==0:
                       print ( R+"##-port",port," is open"+W )
                       self.port= port
                    else:
                       print (  "##-port",port," is closed")
               if self.args.port:
                       self.port = self.args.port
                       print ( Y+"##-specific port",str(self.port)+W )    
               print ("-"*40 )      
            except Exception :
                     print ( "all default port are closed")
                     exit()                           
       def connect(self):
           try:
               self.socke_25 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
               self.socke_25.settimeout(5)            
               connect =  self.socke_25.connect((self.args.target ,int(self.port)))
           except Exception :
                     print ( "##-all default port are closed")
                     print ( "##-try -p to use specific port")
                     exit()                  
       def  socket_25(self): 
                     try:
                        data = self.socke_25.recv(1024)
                     except socket.timeout:
                         time.sleep(2)
                         print ( R+"Server "+W+Y+self.args.target+W+R+" Time out..."+W+'\n')
                         if os.path.exists('SMTP_'+self.args.target):
                            os.remove('SMTP_'+self.args.target)
                         exit()    
                     print ( Y+"[*]##-Enumeration start in  port "+W,R+str(self.port)+W )
                     print ("-"*40 )                      
                     if self.args.user:
                        self.socke_25.sendall('HELO '.encode() + self.args.target.encode()+ '\r\n'.encode())
                        redata =  self.socke_25.recv(1024)
                        self.socke_25.send('VRFY '.encode() + self.args.user.encode() +'\r\n'.encode())                                        
                        final= self.socke_25.recv(1024)                  
                        if "550".encode() in final :
                            print ( "[-]", self.args.target,"....",self.args.user ,"............[NOT Exists]")
                            exit() 	
                        elif "I'll try my best".encode()in final:
                             print ( Y+"[*]Target",self.args.target," Not vulnerable..."+W)
                             if os.path.exists('SMTP_'+self.args.target):
                                os.remove('SMTP_'+self.args.target)
                             exit()	
                        else:
                           if "252".encode() in final :
                              print ( R+"[+]", self.args.target,"....",self.args.user ,"............[Exists]"+W)
                              exit()
       def worldusers(self):
                try:  
                     if self.socke_25.recv(1024):
                        if self.args.wordlist: 
                           for self.line in self.list:  
                                self.socke_25.sendall('HELO '.encode()+'127.0.0.1 '.encode()+ '\r\n'.encode())
                                redata =  self.socke_25.recv(1024) 
                                time.sleep(1)                                                                        
                                self.socke_25.send('VRFY '.encode() + self.line.encode() )                                                       
                                final=  self.socke_25.recv(1024)
                                name=self.line.split()
                                name=''.join(name)
                                if "I'll try my best".encode()  in final:
                                    print ( Y+"[*]Target",self.args.target," Not vulnerable..."+W)
                                    if os.path.exists('SMTP_'+self.args.target):
                                       os.remove('SMTP_'+self.args.target)
                                    exit()
                                elif "550".encode() in final :       
                                    print ( "[-]", self.args.target,"....",name ,"............[NOT Exists]" )                       
                                else:
                                   if "252".encode() in final :
                                        with open('SMTP_'+self.args.target,'a') as self.append:
                                            self.append =self.append.write("[*] "+name+'\n')
                                        print ( R+"[+]", self.args.target,"....",name ,"............[Exists]"+W)
                                    
                           else:
                               print ( R+"\n\t*********END**OF**WORD**LIST*********" +W  )                                        
                               with open('SMTP_'+self.args.target,'r') as self.append:
                                            self.append =self.append.read()
                                            print ( self.append)
                                            exit() 
                except Exception:
                     self.connect()
                     self.worldusers()
                except KeyboardInterrupt:
                       print ( R+"***** Session is Terminated *****"+W)
                       exit()                               
      

       def parser(self):
       
           parser = argparse.ArgumentParser( description="Usage: <OPtion> <arguments> ")
           parser = argparse.ArgumentParser(description="Example: ./Smtp-Vrfy.py -t 10.195.100.67 -w /usr/share/wordlists/rockyou.txt ")
           parser.add_argument( '-t',"--target"   ,metavar='' , action=None  ,help ="Target ip address or name ")
           parser.add_argument( '-u',"--user"   ,metavar='' , action=None  ,help ="for only one username")
           parser.add_argument( '-w',"--wordlist"   ,metavar='' , action=None  ,help ="read from wordlist same like rockyou.txt ")
           parser.add_argument( '-p',"--port"   ,metavar='' , action=None  ,help ="use  specific port ",type=int)
           self.args = parser.parse_args()
           if len(sys.argv)!=1 and len(sys.argv) != 3:
               pass
           else:
               parser.print_help()
               exit()                                        
       def main(self): 
             if self.args.wordlist:
                  self.wordlist()       
             if self.args.target :
                  self.ping_host()
                  self.Check_port()
                  self.connect()
                  self.socket_25()
                  self.worldusers()
                             
if __name__=="__main__":
   SMTP_emn()
   
   
