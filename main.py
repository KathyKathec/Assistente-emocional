from app.camera import capturar_frame
from app.detector import detectar_emocao
from app.ia_resposta import gerar_resposta
from app.interface import mostrar_resultado

def main():
    print("Iniciando Assistente Emocional com Reconhecimento Facial")

    for frame in capturar_frame():
        emocao, score = detectar_emocao(frame)
        if emocao:
            resposta = gerar_resposta(emocao)
            mostrar_resultado(frame, emocao, score, resposta)

if __name__ == "__main__":
    main()
