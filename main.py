from fasthtml.common import *
from pathlib import Path

hdrs = (
    Script(src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=default"),
)

app, rt = fast_app(hdrs=hdrs, static_path="my_website/data")

logo_large = Img(
                src="/logos/logo2.jpg",  # Replace with your logo URL
                alt="Logo",
                style="position: absolute; top: 20px; right: 20px; width: 200px;"
                )

logo_small = Img(
                src="/logos/logo2.jpg",  # Replace with your logo URL
                alt="Logo",
                style="position: absolute; top: 20px; right: 20px; width: 100px;"
                )
#app, rt = fast_app(hdrs=hdrs)
#css = Style(':root {--pico-font-size:90%,--pico-font-family: Pacifico, cursive;}')

#app, rt = fast_app(hdrs=(picolink, css))

@rt('/')
def get():
    return Div (
                P(H3("Bienvenue chez ServiKite, à votre service pour apprendre le kite")),
                P(A('Votre moniteur', href='/votre_moniteur')),
                P(A('Nos cours', href='/nos_cours')),
                P(A('Nos tarifs', href='/nous_tarifs')),
                P(A('Les spots', href='/spots')),
                P(A('Physique du kite', href='/physique')),
                P(A('Systèmes de sécurité sur un kite', href='/sécurité_kite')),
                P(A('Règles de sécurité', href='/sécurité_règles')),
                P(A('Assurance', href='/assurance')),
                P(A('Videos', href='/videos')),
                P(A('Photos', href='/photos')), 
                P(A('logos', href='/Logos')), 
                logo_large,
                style="padding-top: 10px;"
               )



#Div(
#            Img(
#                src="https://via.placeholder.com/100",  # Replace with your logo URL
#                alt="Logo",
#                style="position: absolute; top: 20px; right: 20px; width: 100px;"
#            ),
#            Div("Welcome to the page!", style="padding-top: 100px;")
#        )
                
@rt('/votre_moniteur')
def get():

    s1  = "Benjamin est ingénieur de formation, il dispose d'un monitorat de voile obtenu en 2001 \
            effectué pendant ses études. Il a fait quelques saisons, notamment à Dinard, Pornic, \
            Noirmoutier, Porto veccio et 2 saisons complètes à l'UCPA de Hyères en 2023 et 2024."
    s2 = "A partir de 2018, il se passione pour le kite. En mars 2024, il passe l'IKO niveau 1 \
             à Tarifa, pour enseigner le kite à l'internationale. Actuellement il est en formation moniteur \
             BPJEPS GADA (Glisses Aérotractée et Disciplines Associées) à Quiberon"
    
    s3 = "Pourquoi ServiKite ?, je vous laisse deviner...,)"
         #c'est par respect pour mon père qui avait une entreprise appelée Serviver"

    return (
            Title("A propos de nous"), 
            Div(
                H1('Votre moniteur'),
                P(s1),
                P(s2),
                P(s3),
                P(A('Sommaire', href='/')),
                logo_small,
                cls="container",
                style="padding-top: 10px;"
                  
                )

           )
    
@rt('/nos_cours')
def get():

    s1 ="Nos cours sont données en général sur une durée de 3h. En fonction des conditions météo, on choisit le meilleur spot.\
        Les cours sont formés de 1 à 4 stagiaires et peuvent etre dispensés en Francais, Anglais ou Allemand"
    
    return (
            Title("Nos cours"),
            Div(
                H1('Nos cours'),
                P(s1),
                P(A('Sommaire', href='/')),
                logo_small,
                cls="container",
                style="padding-top: 10px;"
                )
            )

@rt('/nous_tarifs')
def get():
    
    s1 = "Le prix est donnée par le calcul suivant: $$P = Ph * T/N $$"
    s2 = "avec P: le prix par personne, Ph = {120, 100}: le prix horaire en haute et basse saison \
         N le nombre de stagiaires (de 1 à 4) \
        Voici un tableau récapitulatif ci dessous:"
    html_table = """
                    <div class="center">
                <table>
                <thead>
                <tr>
                <th style="text-align: center;">Nombre de stagiaires</th>
                <th style="text-align: center;">Prix basse saison (&#8364)</th>
                <th style="text-align: center;">Prix haute saison (&#8364)</th>
                </tr>
                </thead>
                <tbody>
                <tr>
                <td style="text-align: center;">1</td>
                <td style="text-align: center;">300</td>
                <td style="text-align: center;">360</td>
                </tr>
                <tr>
                <td style="text-align: center;">2</td>
                <td style="text-align: center;">150</td>
                <td style="text-align: center;">180</td>
                </tr>
                <tr>
                <td style="text-align: center;">3</td>
                <td style="text-align: center;">100</td>
                <td style="text-align: center;">120</td>
                </tr>
                <tr>
                <td style="text-align: center;">4</td>
                <td style="text-align: center;">75</td>
                <td style="text-align: center;">90</td>
                </tr>
                </tbody>
                </table>
                </div>
                """
    return (
            Title("Nos tarifs"),
            Div(
                H1('Nos tarifs'),
                P(s1),
                P(s2),
                P(NotStr(html_table)),
                P(A('Sommaire', href='/')),
                logo_small,
                cls="container"
                )
            )

@rt('/spots')
def get():
    s1 ="Le spot est choisit en fonction des conditions météo, on choisira toujours un spot avec un vent on shore ou side on"
    
    return (
            Title("Les spots"),
            Div(
               H1('Les spots'),
               P(s1),
               P(A('Sommaire', href='/')),
               logo_small,
               cls="container"
               )
            )

@rt('/physique')
def get():
    s1 = "Le kitesurf est la combinaison d'un cerf volant et d'un engin qui glisse sur l'eau. \
          Une aile plongée dans un écoulement va générer une portance et une trainée.\
          La force globale est la somme de ces 2 forces  et détermine le comportement du kite."

    s2 = "Pour une vitesse et direction constante, le système rider + kite est à l'équilibre et \
          la somme des forces est nulle. Ainsi la tension dans les lignes qui provient de la force \
          globale générée par le kite s'équilibre avec l'action du rider (son poids et son crantage).\
         En fait ce jeu d'equilibre des forces entre un système dans l'air et un système dans l'eau est \
         à la base du tous les systèmes à voile (bateaux, planche à voile, kite et wing)."

    return (
            Title("Physique du kite"),
            Div(
                H1('Physique du kite'),
                P(s1),
                P(s2),
                P(A('Sommaire', href='/')),
                logo_small,
                cls="container"
                )
            )

@rt('/sécurité_kite')
def get():
    s1 = "En kite, à l'inverse de la planche à voile, le rider est toujours connecté à son aile.\
         Pour cela, il existe par ordre croissant d'urgence, 3 systèmes de sécurité."

    s2 = "Le premier, utilisé le plus fréquemment, est le laché de barre. En faisant ce geste, \
         la tension des lignes est transféré en totalité aux lignes avant du kite. Il perd ainsi\
         énormémment en puissance."

    s3 = "Si pour une raison x ou y, le kite est toujours tractant (vent très fort ou deathloop par exemple),\
          on peut actionner le quick release, ceci a pour effet de prendre la tension seulement sur une ligne: \
        la ligne de sécurité. Ainsi le kite se met en drapeau, il est toujours connecté au rider par la\
         seule ligne de sécurité (une des 2 lignes avant)."

    s4 = "En dernier recourt, on peut utiliser son leash d'aile, et se désolidariser de son matériel.\
        Ce geste est rarement effectué, mais il est utilisé lorsque il y a un danger important et qu'il \
         faut choisir entre sa vie ou son matériel...."
    
    return (
            Title("Systèmes de sécurité sur un kite"),
            Div(
                H1('Systèmes de sécurité sur un kite'),
                P(s1),
                P(s2),
                P(s3),
                P(s4),
                P(A('Sommaire', href='/')),
                logo_small,
                cls="container"
                )
            )

@rt('/sécurité_règles')
def get():
    s1 = "Un peu comme le parapente, la majorité des accidents ont lieu en phase \
        de décollage ou d'attérissage. En suivant les 5 règles \
        d'or suivantes, on limite fortement le risque d'un incident facheux:"
    
    html_code = """<ul>
        <li><p>règle numéro 1: avoir de l’espace</p></li>
        <li><p>règle numéro 2: avoir un vent régulier on shore ou side on,
        jamais offshore</p></li>
        <li><p>règle numéro 3: connaitre ses systèmes de sécurité et les
        pratiquer.</p></li>
        <li><p>règle numéro 4: bien connaitre la procédure de décollage et
        d’attérissage.</p></li>
        <li><p>règle numéro 5: rester humble et ne pas se surestimer</p></li>
    </ul>"""

    return (
            Title("Accidentologie"),
            Div(
                H1('Accidentologie'),
                P(s1),
                P(NotStr(html_code)),
                P(A('Sommaire', href='/')),
                logo_small,
                cls="container"
               )
            )
@rt('/assurance')
def get():
    s1 = "Pour suivre les cours il faut obligatoirement etre asssuré. Pour votre pratique personelle \
        il est vivement conseillé d'avoir une assurance RC à minima. Le plus simple est de prendre \
            une licence à la FFV, FFVL ou AFK"

    return (
            Title("Assurance"),
            Div(
                H1('Assurance'),
                P(s1),
                P(A('Sommaire', href='/')),
                logo_small,
                cls="container"
                )
            )
@rt('/videos')
def get():
    video_file_name = "/videos/pav_ben.mp4"

    return Titled(
            "Videos",
            Div(
                Figure(
                   Video(
                       Source(src=video_file_name ,type="video/mp4"),
                       controls=True,
                       width=1024,
                       height=768,
                        ),
                       Figcaption("Planche à voile presqu'ile de Giens, pointe de l'Esterelle, juin 2024")
                       ),
                P(A('Sommaire', href='/')),
                logo_small,
                cls="container",
                )
            
            )
@rt('/photos')
def get():
    
    return Titled(
        "Photos",
        Div(
            Style("""
                figure {
                    display: inline-block;
                    width: 300px; /* Set figure width */
                    margin: 0 auto;
                    text-align: center;
                }
                figcaption {
                    margin-top: 8px;
                    font-style: italic;
                    color: gray;
                }"""
                ),
            Figure(
                Img(src="/photos/calculatrice2.jpg", alt="Example image", style="width: 100%; height: auto;"),
                Figcaption("Ceci est une casio")
            ),
            P(A('Sommaire', href='/')),
            logo_small,
            cls="container",
        )
    )
 

@rt('/Logos')
def get():
    return Titled(
            "Logos",
            Div(
                Style("""
                    figure {
                        display: inline-block;
                        width: 300px; /* Set figure width */
                        margin: 0 auto;
                        text-align: center;
                    }
                    figcaption {
                        margin-top: 8px;
                        font-style: italic;
                        color: gray;
                    }"""
                    ),
                Figure(
                    Img(src="/logos/logo1.jpg", alt="Example image", style="width: 100%; height: auto;"),
                    Figcaption("Mon logo1")
                ),
                Figure(
                    Img(src="/logos/logo2.jpg", alt="Example image", style="width: 100%; height: auto;"),
                    Figcaption("Mon logo2")
                ),
                Figure(
                    Img(src="/logos/logo3.jpg", alt="Example image", style="width: 100%; height: auto;"),
                    Figcaption("Mon logo3")
                ),
                P(A('Sommaire', href='/')),
                cls="container",
            )
        )

serve()
