label left_path:

    hide Anitta

    show lake

    "Você decide seguir o caminho da esquerda e encontra um lago tranquilo."

    show Anitta feliz:
        xalign 0.5
        yalign 0.61

    a "Que belo lago! Estou feliz por termos vindo por este caminho."

    return

label right_path:
    hide Anitta
    show clareira with dissolve
    "Você escolhe o caminho da direita e se depara com uma clareira."

    show Anitta triste: 
        xalign 0.5
        yalign 0.61
    a "Oh, esta clareira parece um pouco sombria. Deveríamos ter escolhido o outro caminho."
