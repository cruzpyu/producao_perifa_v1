
label explore_more:
    "Você decide explorar mais a floresta."

    show Anitta normal:
        zoom 1
        xalign 0.5
        yalign 0.7

    a "Espere! Eu ouço algo vindo da direção do lago. Deveríamos investigar?"

    hide Anitta normal

    menu:
        "Sim, vamos verificar o que é.":
            jump investigate_lake
        "Não, é melhor continuarmos a explorar a floresta.":
            jump continue_exploring