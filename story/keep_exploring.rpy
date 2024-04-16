label keep_exploring:

    hide floresta escura
    show cabin with dissolve: 
        zoom 1.5
        xalign 0.5
        yalign 0.5

    "Enquanto avança mais um pouco, você encontra uma antiga cabana escondida entre as árvores."

    show Anitta normal:
        xalign 0.5
        yalign 0.65

    a "O que uma cabana está fazendo aqui? Deveríamos entrar e investigar?"

    hide Anitta

    menu:
        "Sim, vamos ver o que tem dentro.":
            jump enter_cabin
        "Não, é melhor voltarmos para a encruzilhada.":
            jump start
