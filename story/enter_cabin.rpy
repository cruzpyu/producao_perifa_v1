label enter_cabin:
    show inside cabin: 
        zoom 2.15
        xalign 0.5
        yalign 0.5

    "Ao entrar na cabana, você encontra evidências de que alguém mora ali, mas não há ninguém à vista."

    show Anitta triste: 
        xalign 0.5
        yalign 0.61

    a "Isso é assustador. Será que devemos continuar investigando?"

    hide Anitta

    menu:
        "Sim, vamos procurar mais pistas.":
            jump search_cabin
        "Não, é melhor sairmos daqui.":
            jump start
