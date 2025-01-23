# README - Repeatability Analysis on a DJI Tello Drone

## Sobre o Projeto
Este projeto é uma aplicação para controlar o drone DJI Tello e visualizar a imagem da câmera em tempo real. Ele faz parte da monografia intitulada **"Repeatability Analysis on a DJI Tello Drone for Automation"**. O objetivo principal do projeto é analisar a repetibilidade dos movimentos do drone DJI Tello em cenários automatizados.

## Funcionalidades
- Controle do drone DJI Tello.
- Transmissão de vídeo em tempo real da câmera do drone.
- Interface acessível via navegador web.

## Instruções
1. **Ligue o Drone**: Certifique-se de que o drone DJI Tello esteja ligado.
2. **Conecte-se à Rede**: Conecte sua máquina (PC) à rede Wi-Fi gerada pelo drone DJI Tello.

## Instalação
1. **Clone o Repositório**:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_DIRETORIO>
   ```

2. **Instale as Dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Inicie a Aplicação**:
   ```bash
   python main.py
   ```

4. **Acesse o App**:
   Abra seu navegador e acesse: [http://127.0.0.1:5000/controllers](http://127.0.0.1:5000/controllers)

## Requisitos do Sistema
- **Python 3.7+**
- **Bibliotecas Necessárias**: Listadas no arquivo `requirements.txt`
- **Rede Wi-Fi**: Conexão direta com o drone DJI Tello

## Estrutura do Projeto
```
├── main.py                # Arquivo principal para execução do projeto
├── docs/                  # Arquicos de referências
├── requirements.txt       # Dependências do projeto
├── models/                # Arquicos de gerenciamento do drone 
├── controllers/           # Arquivos de controle rotas(server)
├── templates/             # Arquivos HTML para a interface web
└── static/                # Arquivos estáticos como CSS e JavaScript
```

## Contribuição
Contribuições para o projeto são bem-vindas. Sinta-se à vontade para abrir issues ou enviar pull requests.

## Autores
- **Autor**: Cleby Francisco da Silva
- **Orientador**: João Marcelo Xavier Natário Teixeira
- **Aux. Técnico**: Felipe Augusto da Silva Mendonça

---

**Nota**: Certifique-se de operar o drone DJI Tello em um ambiente seguro e adequado para evitar acidentes ou danos ao equipamento.

