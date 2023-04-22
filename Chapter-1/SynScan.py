from scapy.all import *

host="192.168.68.1"
ports = [25,80,53,443,445,8080,8443]

ans, unans = sr(IP(dst=host)/TCP(sport=33333,dport=ports,flags="S"),timeout=2,verbose=0)

s,r = ans[1]

print(s[TCP].dport,r[TCP].sport,r[TCP].flags)
