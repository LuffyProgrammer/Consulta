import requests
print(""""
▄▀ ▄▀▄ █▄░█ ▄▀▀ █░█ █░░ ▀█▀ ▄▀▄     ▀ █▀▄ 
█░ █░█ █░▀█ ░▀▄ █░█ █░▄ ░█░ █▀█     █ █░█ 
░▀ ░▀░ ▀░░▀ ▀▀░ ░▀░ ▀▀▀ ░▀░ ▀░▀     ▀ █▀░ 

""")
def consulta():
    ip = input("-> Digite o IP:")
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
    a24 = json['currency']
    a25 = json['currency_code']
    a26 = json['currency_symbol']
 
    print(f"\n-> IP:{a1}\n-> SUCESSO:{a2}\n-> TIPO DE IP:{a3}\n-> CONTINENTE:{a4}\n-> SIGLA DO CONTINENTE:{a5}\n-> PAÍS:{a6}\n-> CAPITAL DO PAÍS:{a9}\n-> DDI DO PAÍS:{a10}\n-> SIGLAS DOS PAÍSES VIZINHOS:{a11}\n-> REGIÃO:{a12}\n-> CIDADE:{a13}\n-> LATITUDE:{a14}\n-> LONGITUDE:{a15}\n-> ASN::{a16}\n-> ORG:{a17}\n-> ISP:{a18}\n-> FUSO HORARIO LOCAL:{a19}\n-> FUSO HORÁRIO DO PAIS:{a20}\n-> MOEDA DO PAÍS:{a24}\n-> SIGLA DA MOEDA LOCAL:{a25}\n-> SIMBOLO DA MOEDA:{a26}")
    
    con = int(input("-> Deseja fazer uma nova consulta?: \n1-S\n2-N\n"))
    if con == 1:
        consulta()
    else:
      print('-> Saindo...')
      exit()
consulta()
