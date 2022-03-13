import re
import requests

count = 0

with open("pub.txt") as f:

    db = f.readlines()

for x in range(len(db)):

    link = db[x].strip()

    r = requests.get(link).text

    c = int("".join(re.findall('Участники <em class="pm_counter">(\d+)</em></a>',r)))

    print(f"{c} {link}")

    count += c

with open("count.txt","a") as f:

    f.writelines(f"Общее число участников {count}"+"\n")

print(f"Общее число участников {count}")