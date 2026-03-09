# 📊 Analisador de Logs em Python

Projeto simples desenvolvido em **Python** para analisar arquivos de log e identificar padrões de acesso, como endereços IP que aparecem com maior frequência.

Esse tipo de ferramenta é muito utilizada em **segurança da informação, monitoramento de servidores e análise de tráfego de rede**.

---

## 📌 Objetivo do Projeto

O objetivo deste projeto é demonstrar como utilizar Python para:

* Ler arquivos de log
* Processar grandes volumes de texto
* Identificar padrões de acesso
* Contar ocorrências de endereços IP

Ferramentas desse tipo ajudam administradores de sistemas a detectar **comportamentos suspeitos em redes e servidores**.

---

## ⚙️ Tecnologias Utilizadas

* Python 3
* Manipulação de arquivos
* Estruturas de dados (`dicionários`)
* Processamento de strings

---

## 📂 Estrutura do Projeto

```
log-analyzer-python
│
├── log_analyzer.py
├── log.txt
└── README.md
```

---

## 💻 Código do Analisador

```
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
```

---

## ▶️ Como Executar

1. Clone o repositório

```
git clone https://github.com/SEU-USUARIO/log-analyzer-python.git
```

2. Entre na pasta do projeto

```
cd log-analyzer-python
```

3. Execute o programa

```
python log_analyzer.py
```

---

## 📊 Exemplo de Arquivo de Log

Exemplo de conteúdo do arquivo `log.txt`:

```
192.168.0.10 - acesso permitido
192.168.0.15 - acesso permitido
192.168.0.10 - acesso permitido
192.168.0.22 - acesso negado
192.168.0.10 - acesso permitido
```

---

## 📈 Exemplo de Resultado

```
192.168.0.10 -> 3 acessos
192.168.0.15 -> 1 acessos
192.168.0.22 -> 1 acessos
```

---

## 🔎 Aplicações Reais

Ferramentas de análise de logs são utilizadas para:

* Monitoramento de servidores
* Detecção de tentativas de invasão
* Auditoria de sistemas
* Análise de tráfego de rede
* Investigação em segurança digital

---

## 👨‍💻 Autor

*** Julio Cesar Alves de Oliveira ***

Estudante de tecnologia, redes de computadores e segurança da informação.

---

## 🚀 Melhorias Futuras

Algumas melhorias que podem ser implementadas:

* Identificar **IPs mais ativos**
* Detectar possíveis **ataques de força bruta**
* Exportar resultados para **CSV ou JSON**
* Criar gráficos de acesso
* Criar interface gráfica

---

## 📚 Aprendizados

Este projeto ajuda a praticar:

* leitura e processamento de arquivos
* manipulação de strings
* uso de dicionários em Python
* análise básica de dados

---

## ⚠️ Aviso

Este projeto foi desenvolvido para **fins educacionais**, com objetivo de estudo de programação e análise de dados.

---
