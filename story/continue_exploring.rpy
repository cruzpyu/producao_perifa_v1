label continue_exploring:
    show floresta escura: 
        zoom 3.0
        xalign 0.5
        yalign 0.5

    "Enquanto você continua a explorar, a floresta fica mais escura e densa."

    show Anitta triste: 
        yalign 0.6
        xalign 0.5

    a "Estou começando a ficar preocupada. Esta parte da floresta parece assustadora."

    hide Anitta triste

    menu:
        "Volte para a encruzilhada.":
            jump start
        "Continuar mais um pouco.":
            jump keep_exploring
