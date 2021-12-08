import subprocess

veriler = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
profiles = [i.split(":")[1][1:-1] for i in veriler if "All User Profile" in i]

for i in profiles:    
    try:
        sonuc = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        sonuc = [b.split(":")[1][1:-1] for b in sonuc if "Key Cont" in b]
        
        try:
            print("Wifi Ağı: {:<30} sifre:  {:<}".format(i, sonuc[0]))
        
        except IndexError:
            print("Wifi Ağı: {:<30} sifre:  {:<}".format(i, ""))
    except subprocess.CalledProcessError:
        print("Wifi Ağı: {:<30} sifre:  {:<}".format(i, "Kodlama Hatası"))
