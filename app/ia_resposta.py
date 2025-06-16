# -*- coding: utf-8 -*-

import os
import random

def gerar_resposta(emocao):
    respostas_mock = {
        "happy": [
            #"Que bueno verte feliz, Sigue asi ",
            #"Tu alegria es contagiosa. Es genial verte asi.",
            "Me encanta verte feliz. Que tu dia siga siendo maravilloso."
        ],
        "sad": [
            #"Esta bien sentirse asi... respira profundo.",
            #"Lamento que estes triste. Estoy aqui si necesitas desahogarte.",
            "Permitete sentir. Mañana es un nuevo dia y todo puede mejorar."
        ],
        "angry": [
            #"Trata de calmarte. Quieres hablar de eso? ",
            "Es normal sentir enojo. Respira hondo y trata de encontrar la calma.",
            #"Que te hizo enojar? Puedo ayudarte de alguna manera?"
        ],
        "neutral": [
            #"Estoy aqui si necesitas hablar. ",
            "Parece que estas bien. ¡Que tengas un gran dia!",
            #"Todo bien? Estoy cerca si necesitas algo."
        ],
        "surprise": [
            "Parece que algo te sorprendio, Cuentame... ",
            #"Vaya sorpresa... Espero que sea algo bueno",
            #"Una sorpresa, eh? Tengo curiosidad por saber que es!"
        ],
        "fear": [
            #"Esta todo bien, estoy contigo. ",
            "El miedo es natural. Recuerda tu fuerza y valentia.",
            #"No tienes que tener miedo. Estoy aqui para apoyarte."
        ],
        "disgust": [
            #"A veces necesitamos un descanso. Esta bien sentirse asi.",
            #"Siento que algo te molesto. No te preocupes, pasara.",
            "Esta bien no gustar de algo. Como puedo ayudarte a sentirte mejor?"
        ]
    }

    emocao_normalizada = emocao.lower()
    frases_disponibles = respostas_mock.get(emocao_normalizada, ["Como puedo ayudarte hoy?"])

    return random.choice(frases_disponibles)
