import urllib.request
import json
import webbrowser
import os
print("░░██╗██████╗░░░░░░░░░░░░░░░░░░░░")
print("░░██║██╔══██╗░░░░░░░░░░░░░░░░░░░")
print("░░██║██████╔╝░░█ █▄░█ █▀▀ █▀█░░░")
print("░░██║██╔═══╝░░░█ █░▀█ █▀░ █▄█░░░")
print("░░██║██║░IP address information░")
print("░░╚═╝╚═╝░░░░░░░░░░░░░░░░░░░░░░░░")
print("================================")
getIP = input("[+] Enter IP : ")
url = "https://ipinfo.io/" + getIP + "/json"

try:
    getInfo = urllib.request.urlopen( url )

except:
    print( "\n[!] - IP not found! - [!]\n" )

infoList = json.load(getInfo)

def whoisIPinfo(ip):

    try:

        myComand = "whois " + getIP
        whoisInfo = os.popen( myComand ).read()
        return whoisInfo

    except:

        return "\n [!] Error [!] \n"
        
     
print( "-" * 60 )

print( "IP :", infoList["ip"] )
print( "City :", infoList["city"] )
print( "Region :", infoList["region"] )
print( "Country :", infoList["country"] )
print( "Hostname :", infoList["hostname"] )
print( "Organization :", infoList["org"] )
print( "Postal :", infoList["postal"] )
print( "Time zone :", infoList["timezone"] )
print( "Location :", infoList["loc"] )
print( "-" * 60)    
print( "API :", url )
print( "-" * 60) 
ourl = input("Open API link? (y/n) : ")
if ourl == ('y'):
    webbrowser.open(url)
elif ourl != ('y'):
    print("Okay...")