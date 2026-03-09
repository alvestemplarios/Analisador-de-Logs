arquivo = open("log.txt", "r")

linhas = arquivo.readlines()

contador = {}

for linha in linhas:
    ip = linha.split()[0]

    if ip in contador:
        contador[ip] += 1
    else:
        contador[ip] = 1

for ip, acessos in contador.items():
    print(ip, "->", acessos, "acessos")

arquivo.close()