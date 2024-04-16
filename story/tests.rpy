label animation_test:
    scene black

    show fire:
        xalign 7.0
        yalign 0.3
        zoom 1.0
        
    show cat:
        zoom 0.5
        xalign 0.98
        yalign 0.8

    "Teste de animação"

    return 

label video_test:

    a "SERÁ SE VAI"
    $ renpy.movie_cutscene('images/cavalete.webm')

    "ihhhhhhhhhh"

    return
