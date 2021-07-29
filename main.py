import os 
import sys 
import time 
import colorama 
import pyfiglet 
from colorama import Fore 

os.system(' clear ')


def load_animation(): 
  
    load_str = "Loading DBROWSER."
    ls_len = len(load_str) 
    time.sleep(1)
    animation = "|/-\\|/-\|/-/"
    anicount = 0
      
    counttime = 0        
       
    i = 0                     
  
    while (counttime != 30): 
          

        time.sleep(0.075)  
                              
        load_str_list = list(load_str)  
 
        x = ord(load_str_list[i]) 
          
        y = 0                             

        if x != 32 and x != 46:              
            if x>90: 
                y = x-32
            else: 
                y = x + 32
            load_str_list[i]= chr(y) 
          
        res =''              
        for j in range(ls_len): 
            res = res + load_str_list[j] 
              
        sys.stdout.write("\r"+res + animation[anicount]) 
        sys.stdout.flush() 
  
        load_str = res 
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len 
        counttime = counttime + 1

    else: 
        os.system("clear") 
  
# Driver program 
if __name__ == '__main__':  
    load_animation() 

def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()

def screen_clear():
   if name == 'nt':
      _ = system('cls')

def CS(X):          # CS = clear sleep
   time.sleep(X)
   os.system("clear")


os.system(' clear ')

print(Fore.GREEN+"")
banner = pyfiglet.figlet_format("DBROW", font = "isometric1" )
print(banner)
print(Fore.RED+"                                           WelC0me to DBROW the hackers browser   ")
print("                                                                               V1.0")
print("--------------------------------------------------------------------------------------------")
time.sleep(0.1)
print("                                                                _____________________________")
print("proxychains                                                     | you should have it if you | ")
print("                                                                | have a linux system or are|")
print("                                                                | a hacker and programmer   |")
print("                                                                |---------------------------|")
A = str(input(" Do Y0U HAV3 PR0X3CHAINS ===>> "))

if 'yes' in A:
         print(" [!] okay continuing code [!] ")
         
elif 'no' in A:
          CS(2)
          print(banner)
          print(" [!] installing proxychains [!] ")
          os.system(' sudo apt-get install proxychains ')
          os.system(' wget https://dist.torproject.org/torbrowser/7.0.11/tor-browser-linux64-7.0.11_en-US.tar.xz ')
          os.system(' tar xvf tor-browser-linux64-7.0.11_en-US.tar.xz ')
          os.system(' ./configure && make​ ')
          os.system(' sudo make install ')
          restart_program()

elif 'No' in A:
          CS(2)
          print(banner)
          print(" [!] installing proxychains [!] ")
          os.system(' sudo apt-get install proxychains ')
          os.system(' wget https://dist.torproject.org/torbrowser/7.0.11/tor-browser-linux64-7.0.11_en-US.tar.xz ')
          os.system(' tar xvf tor-browser-linux64-7.0.11_en-US.tar.xz ')
          os.system(' ./configure && make​ ')
          os.system(' sudo make install ')
          restart_program()          

CS(2)
print(banner)
print(Fore.RED+"                                           WelC0me to DBROW the hackers browser   ")
print("                                                                               V1.0")
print(" [1] Just browse the net ")
print(" [2] go to my index for my website ") 
print(" [3] just browse google ")
print("--------------------------------------------------------------------------------------------")

# run.py = index 
# rung = run google 
# run1 = run duckduckgo 

N = str(input(" Options ===> "))


####### BROWSE DUCKDUCKGO ###########
if '1' == N:
    time.sleep(1)
    print(" [!] running Dark browser [!] ")
    time.sleep(3)
    Yn = str(input(" would you like to run proxys along side browsing Y/n? "))
    time.sleep(1)
    
    if 'n' in Yn:
        time.sleep(1)
        print(" alright then running browser ")
        CS(2)
        print(banner)
        os.system(' sudo service tor start && proxychains python3 run1.py ')
        print(" [!] Stopping tor service and breaking connections [!] ")
        os.system(' sudo service tor stop && clear ')
        sys.exit()

    if 'Y' == Yn:
        time.sleep(1)
        print(" [=] alright then running browser with proxychains and tor service ")
        CS(2)
        print(banner)
        os.system(' sudo service tor start && proxychains python3 run1.py') 
        print(" [!] Stopping tor service and breaking connections [!] ")
        os.system(' sudo service tor stop && clear ')
        sys.exit()   

##############################################
###########BROWSE GOOGLE 

elif '3' == N:
    time.sleep(1)
    Yn = str(input(" Would you like to use proxies Y/n? "))
    
    if 'Y' in Yn:
           CS(2)
           time.sleep(1)
           print(banner)
           print(" [=] alright then running browser [=] ")
           os.system(' sudo service tor start && proxychains python3 rung.py  ')
           print(" [!] Stopping tor service and breaking connections [!] ")
           os.system(' sudo service tor stop && clear ')
           sys.exit()

    if 'n' in Yn:
           CS(2)
           time.sleep(1)
           print(banner)    
           os.system(' sudo service tor start && proxychains python3 rung.py ')
           os.system(' clear ')
           print(" [!] Stopping tor service and breaking connections [!] ")
           os.system(' sudo service tor stop && clear ')
           sys.exit()

###################BROWSE MTY INDEX################ 
elif '2' == N:
      time.sleep(1)
      Yn = str(input(" Would you like to use proxies Y/n? "))
      print(" [!] running Dark browser [!] ")
      
      if 'Y' in Yn:
          CS(2)
          print(banner)
          print(" [=] alright then running script [=] ")
          time.sleep(1)
          os.system(' sudo service tor start && proxychains python3 run.py ')
          print(" [!] Stopping tor service and breaking connections [!] ")
          os.system(' sudo service tor stop && clear ')
          sys.exit()
      
      if 'n' == Yn:
          CS(2)
          print(" [=] alright then running script [=] ")
          print(banner)
          time.sleep(1)
          os.system(' python3 run.py ')
          print(" [!] Stopping tor service and breaking connections [!] ")
          os.system(' sudo service tor stop && clear ')
          sys.exit()