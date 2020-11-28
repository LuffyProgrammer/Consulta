import requests
print(""""
#╔════•ೋೋ•════╗ 
# ▀ █▀▄ ▄▀▀─ █▀▀ ▄▀▄
# █ █─█ █─▀▌ █▀▀ █─█
# ▀ █▀─ ▀▀▀─ ▀▀▀ ─▀─
#┈┈┈╲┈┈┈┈╱
#┈┈┈╱     ▔▔╲
#┈┈┃┈▇┈┈▇┈┃
#╭╮┣━━━━━━┫╭╮
#┃┃┃┈┈┈┈┈┈┃┃┃
#╰╯┃┈┈┈┈┈┈┃╰╯
#┈┈╰┓┏━━┓┏╯
#┈┈┈╰╯┈┈╰╯
#CRIADOR:Luiz Eduardo
#╚════•ೋೋ•════╝
""")
def consulta():
    ip = input("➜ Digite o IP:")
    url = requests.get(f'http://ipwhois.app/json/{ip}')
    json = url.json()
    a1 = json['ip']
    a2 = json['success']
    a3 = json['type']
    a4 = json['continent']
    a5 = json['continent_code']
    a6 = json['country']
    a7 = json['country_code']
    a9 = json['country_capital']
    a10 = json['country_phone']
    a11 = json['country_neighbours']
    a12 = json['region']
    a13 = json['city']
    a14 = json['latitude']
    a15 = json['longitude']
    a16 = json['asn']
    a17 = json['org']
    a18 = json['isp']
    a19 = json['timezone']
    a20 = json['timezone_name']
    a21 = json['timezone_dstOffset']
    a22 = json['timezone_gmtOffset']
    a23 = json['timezone_gmt']
    a24 = json['currency']
    a25 = json['currency_code']
    a26 = json['currency_symbol']
    a27 = json['currency_rates']
    a28 = json['currency_plural']
    a29 = json['completed_requests']
 
    print(f"\n➜ Ip:{a1}")
    print(f"\n➜ Ip:{a2}")
    print(f"\n➜ Ip:{a3}")
    print(f"\n➜ Ip:{a4}")
    print(f"\n➜ Ip:{a5}")
    print(f"\n➜ Ip:{a6}")
    print(f"\n➜ Ip:{a7}")
    print(f"\n➜ Ip:{a9}")
    print(f"\n➜ Ip:{a10}")
    print(f"\n➜ Ip:{a11}")
    print(f"\n➜ Ip:{a12}")
    print(f"\n➜ Ip:{a13}")
    print(f"\n➜ Ip:{a14}")
    print(f"\n➜ Ip:{a15}")
    print(f"\n➜ Ip:{a16}")
    print(f"\n➜ Ip:{a17}")
    print(f"\n➜ Ip:{a18}")
    print(f"\n➜ Ip:{a19}")
    print(f"\n➜ Ip:{a20}")
    print(f"\n➜ Ip:{a21}")
    print(f"\n➜ Ip:{a22}")
    print(f"\n➜ Ip:{a23}")
    print(f"\n➜ Ip:{a24}")
    print(f"\n➜ Ip:{a25}")
    print(f"\n➜ Ip:{a26}")
    print(f"\n➜ Ip:{a27}")
    print(f"\n➜ Ip:{a28}")
    print(f"\n➜ Ip:{a29}")

    con = int(input("➜ Deseja fazer uma nova consulta?: \n1-S\n2-N\n"))
    if con == 1:
        consulta()
    else:
      print('➜ Saindo...')
      exit()
consulta()