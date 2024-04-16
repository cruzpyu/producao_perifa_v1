image Anitta normal = "images/anitta/anitta seria.png"
image Anitta feliz = "images/anitta/anitta feliz.png"
image Anitta triste = "images/anitta/anitta triste.png"
image Anitta assustada = "images/anitta/anitta assustada.png"


image lake = 'images/scenes/lagoa.jpg'
image encruzilhada = 'images/scenes/encruzilhada.jpg'
image clareira = 'images/scenes/clareira.jpg'
image chave = 'images/scenes/golden-key.jpg'
image floresta escura = 'images/scenes/floresta-noite.jpg'
image cabin = 'images/scenes/cabin.jpg'
image inside cabin = 'images/scenes/inside-cabin.jpg'
image diary = 'images/scenes/diary.jpg'

image transparency = Movie(channel='movie', play='images/libras.webm', mask='images/libras_mask.webm')

image fire:
    "images/fogo/fogo 1.png"
    0.15
    "images/fogo/fogo 2.png"
    0.15
    "images/fogo/fogo 3.png"
    0.15
    "images/fogo/fogo 4.png"
    0.15
    "images/fogo/fogo 5.png"
    0.15
    repeat 

image cat: 
    'images/gato.png'
    2.0
    'images/gato-blink.png'
    0.3
    repeat


define a = Character(name="Anitta")

label start:
    play music "audio/music/disse-adeus.mp3" fadein 1.0
    
    scene black

    show encruzilhada:
        zoom 2.0
        xalign 0.5
        yalign 0.5

    show transparency with dissolve
    # $ renpy.movie_cutscene('images/teste.webm')

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

label left_path:

    hide Anitta

    scene forest_left 

    show lake

    "Você decide seguir o caminho da esquerda e encontra um lago tranquilo."

    show Anitta feliz:
        xalign 0.5
        yalign 0.61

    a "Que belo lago! Estou feliz por termos vindo por este caminho."

    return

label right_path:
    hide Anitta
    scene forest_right
    show clareira with dissolve
    "Você escolhe o caminho da direita e se depara com uma clareira."

    show Anitta triste: 
        xalign 0.5
        yalign 0.61
    a "Oh, esta clareira parece um pouco sombria. Deveríamos ter escolhido o outro caminho."

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

label investigate_lake:
    scene lake_view
    
    show chave:
        zoom 1.7
        xalign 0.5
        yalign 0.5

    "Ao se aproximar do lago, você encontra uma chave brilhante no fundo da água."

    show Anitta feliz:
        xalign 0.5
        yalign 0.61

    a "Uau, uma chave! Talvez ela abra alguma coisa importante na floresta."

    return

label continue_exploring:
    scene dark_forest
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

label enter_cabin:
    scene cabin_door

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

label search_cabin:
    scene cabin_interior
    show diary:
        zoom 1.9
        xalign 0.5
        yalign 0.5
    "Enquanto procuram por pistas, vocês encontram um diário que revela que a floresta está amaldiçoada e que quem a explora nunca mais sai."

    show Anitta assustada: 
        zoom 2.0
        xalign 0.5
        yalign 0.7
    a "Oh não, nós estamos presos aqui na floresta amaldiçoada!"




