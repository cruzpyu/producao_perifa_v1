label start:
    play music "audio/music/disse-adeus.mp3" fadein 1.0
    
    scene black

    show encruzilhada:
        zoom 2.0
        xalign 0.5
        yalign 0.5

    show transparency with dissolve

    "Você está em uma encruzilhada na floresta."

    hide transparency 

    show Anitta normal:
        xalign 0.5
        yalign 0.67

    a "Olá! Eu sou a Anitta. Qual caminho você deseja seguir?"

    hide Anitta 

    menu first_menu:
        "Siga o caminho da esquerda.":
            jump left_path
        "Siga o caminho da direita.":
            jump right_path
        "Teste de animação":
            jump animation_test
        "Teste de vídeo":
            jump video_test
            
