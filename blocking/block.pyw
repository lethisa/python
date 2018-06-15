import time
from datetime import datetime as dt

hosts_path_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website = ["www.facebook.com", "facebook.com", "dub119.mail.live.com", "www.dub119.mail.live.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("working hours")
        with open(hosts_path_temp, "r+") as file:
            content = file.read()  
            for web in website:
                if web in content:
                    pass
                else:
                    file.write(redirect + "" + web)
    else:
        with open(hosts_path_temp, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(web in line for web in website):
                    file.write(line)
            file.truncate()
        print("free hours")
    time.sleep(5)

