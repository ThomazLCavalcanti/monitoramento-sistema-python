# 🖥️ Monitoramento de Sistema via Terminal

Este projeto é um script em Python para monitorar em tempo real o uso de recursos do sistema diretamente pelo terminal (CLI).

## 🔧 Funcionalidades

- Monitoramento da utilização de **CPU**, **memória RAM**, **disco** e **rede**.
- Exibição das informações em formato de tabela, atualizadas periodicamente.
- Interface leve, prática e sem dependência gráfica.

## ▶️ Como executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/monitoramento-sistema-python.git
cd monitoramento-sistema-python
```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
```bash
python3 -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute o script:
```bash
python monitoramento.py
```

## 📦 Requisitos

- Python 3.8+
- `psutil` e `tabulate` (listados em `requirements.txt`)

## 📄 Licença

Este projeto está licenciado sob a licença MIT.
