import cv2

from PIL import ImageFont, ImageDraw, Image
import cv2
import numpy as np

def mostrar_resultado(frame, emocao, score, resposta):

    # Converte o frame do OpenCV (BGR) para PIL (RGB)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(frame_rgb)

    # Crie objeto para desenhar
    draw = ImageDraw.Draw(pil_img)

    # Fonte TTF 
    fonte = ImageFont.truetype("arial.ttf", 24)  # ou "DejaVuSans.ttf", "Roboto-Regular.ttf"

    # Mensagem
    texto_emocao = f"{emocao} ({score:.2f})"
    draw.rectangle([(10, 10), (700, 120)], fill=(0, 0, 0, 128))
    draw.text((20, 20), texto_emocao, font=fonte, fill=(255, 255, 255))

    # Resposta com acento e dentro do limite

    linhas_resposta = dividir_texto(resposta, 60)  # limite de 60 caracteres por linha
    y = 60  # posição vertical inicial

    for linha in linhas_resposta:
        draw.text((20, y), linha, font=fonte, fill=(144, 238, 144))
        y += 30  # espaçamento entre linhas

    # Converta de volta para OpenCV e exiba
    frame_bgr = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    cv2.imshow("Assistente Emocional", frame_bgr)


def dividir_texto(texto, max_caracteres):
    palavras = texto.split()
    linhas = []
    atual = ""
    for palavra in palavras:
        if len(atual + " " + palavra) > max_caracteres:
            linhas.append(atual.strip())
            atual = palavra
        else:
            atual += " " + palavra
    if atual:
        linhas.append(atual.strip())
    return linhas
