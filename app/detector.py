from fer import FER

detector = FER(mtcnn=True)

def detectar_emocao(frame):
    resultados = detector.detect_emotions(frame)
    if resultados:
        face = resultados[0]
        emotions = face["emotions"]
        emocao_mais_forte = max(emotions, key=emotions.get)
        score = emotions[emocao_mais_forte]
        return emocao_mais_forte, score
    return None, None
