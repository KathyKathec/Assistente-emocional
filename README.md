# 🤖 Assistente Emocional com Reconhecimento Facial

Este é um projeto de assistente emocional que utiliza reconhecimento facial em tempo real para identificar emoções humanas e responder com mensagens empáticas em espanhol, promovendo bem-estar e apoio emocional.

## 🎯 Objetivo

Criar um sistema simples de inteligência artificial que reconheça expressões faciais capturadas pela webcam, classifique a emoção predominante e exiba uma resposta apropriada na tela.

## 🧰 Tecnologias e Ferramentas

- Python 3
- [OpenCV](https://opencv.org/) – Captura de vídeo e manipulação de imagens
- [FER](https://github.com/justinshenk/fer) – Detecção de emoções faciais
- [TensorFlow](https://www.tensorflow.org/) – Backend do FER
- [Pillow (PIL)](https://python-pillow.org/) – Desenho de textos e caixas sobre o vídeo
- Random – Geração aleatória de respostas personalizadas
- MoviePy – Dependência auxiliar
- .env – Configuração de ambiente

## 📁 Estrutura do Projeto

ASSISTENTE_EMOCIONAL/
│
├── app/
│ ├── camera.py # Captura de frames da webcam
│ ├── detector.py # Detecção de emoções usando FER
│ ├── ia_resposta.py # Geração de respostas baseadas na emoção
│ └── interface.py # Interface com visualização do resultado
│
├── main.py # Arquivo principal que integra os módulos
├── requerimentos.txt # Dependências do projeto
├── .env # Variáveis de ambiente
└── README.md # Documentação do projeto


## ▶️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/nome-do-repo.git
cd nome-do-repo

```
2. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

```
3. Instale as dependências:

```bash
pip install -r requerimentos.txt

```
4. Execute o programa:

```bash
python main.py

```
