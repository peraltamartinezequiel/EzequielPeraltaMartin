"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect, url_for
from ProyectoFinal import app
import json

peliculas = '''
{
    "películas": [
        {
            "id": 0,
            "título": "La Sirenita",
            "director/ra": "Rob Marshall",
            "año": 2023,
            "género": "aventuras",
            "sinopsis": "LA SIRENITA, la querida historia de Ariel, una sirena joven y apasionada con ansias de aventuras, está protagonizada por la cantante y actriz Halle Bailey (CRECIDO) como Ariel; el ganador del premio Tony® Daveed Diggs (Hamilton, El expreso del miedo) como la voz de Sebastián; Jacob Tremblay (LUCA, La habitación) como la voz de Flounder; Awkwafina (RAYA Y EL ÚLTIMO DRAGÓN) como la voz de Scuttle; Jonah Hauer-King (A Dog's Way Home) como el Príncipe Eric; Art Malik (HOMELAND) como Sir Grimsby; Noma Dumezweni (EL REGRESO DE MARY POPPINS) como la Reina Selina; con el ganador del Oscar® Javier Bardem (Sin lugar para los débiles, Being the Ricardos) como el Rey Tritón; y la dos veces nominada al Oscar® Melissa McCarthy (¿PODRÁS PERDONARME? , Damas en guerra) como Úrsula. Ariel, la más joven de las hijas del rey Tritón y la más rebelde, sueña con conocer el mundo más allá del mar y, mientras visita la superficie, se enamora del distinguido príncipe Eric. Aunque las sirenas tienen prohibido relacionarse con los humanos, Ariel debe seguir su corazón. Ella hace un trato con la malvada bruja del mar, Úrsula, que le da la oportunidad de experimentar la vida sobre la tierra, pero que, en última instancia, pone su vida y la corona de su padre en peligro.",
            "link": "https://www.cinemacenter.com.ar/img_movies/2627_img2.jpg"
        },
        {
            "id": 1,
            "título": "Rápidos y Furiosos X",
            "director/ra": "Louis Leterrier",
            "año": 2023,
            "género": "acción",
            "sinopsis": "Comienza el final del camino. Rápidos y furiosos X, la décima película de la saga Rápidos y furiosos, es el capítulo final de una de las franquicias más populares y queridas del cine, ahora en su tercera década y continuando con el mismo elenco y personajes que cuando comenzó. A través de varias misiones y contra lo imposible, Dom Toretto (Vin Diesel) y su familia han sido más astutos y más rápidos que todos los enemigos se le han cruzado en su camino. Ahora se enfrentan a su enemigo más letal: una amenaza aterradora que surge de las sombras del pasado que está alimentado de una venganza sangrienta, y está decidido a destruir a su familia y destruir todo, y a cualquier persona, A los que Dom ama. En Rápidos y furiosos: 5in control, de 2011, Dom y su equipo derrotaron al infame líder de la droga brasileña Hernan Reyes y destruyeron su imperio en un puente de Rio de Janeiro. Lo que no sabían era que el hijo de Reyes, Dante (Jason Momoa, de Aquaman) presenció todo y ha pasado 12 años creando un plan para que Dom pague el precio más alto. El plan de Dante llevará a la familia de Dom de Los Ángeles a las catacumbas de Roma, de Brasil a Londres, y de Portugal a la Antártida. Se forjaran nuevos aliados y resurgirán viejos enemigos. Pero todo cambia cuando Dom descubre que su hijo de 8 años (Leo Abelo Perry, Black-ish) es el objetivo final de la venganza de Dante."
            "link": "https://www.cinemacenter.com.ar/img_movies/2672_img2.jpg"
        },
        {
            "id": 2,
            "título": "Guardianes de la Galaxia Vol. 3",
            "director/ra": "James Gunn",
            "año": 2023,
            "género": "ciencia ficción",
            "sinopsis": "GUARDIANES DE LA GALAXIA VOLUMEN 3 contiene varias escenas con luces intermitentes que pueden afectar a los clientes susceptibles a padecer epilepsia fotosensible u otras fotosensibilidades."
            "link": "https://www.cinemacenter.com.ar/img_movies/2637_img2.jpg"
        },
        {
            "id": 3,
            "título": "La Extorsión",
            "director/ra": "Martino Zaidelis",
            "año": 2023,
            "género": "drama",
            "sinópsis": "Alejandro es un experimentado piloto aeronáutico. Amante de su profesión, esconde un secreto: una condición médica que implicaría su retiro inmediato. Los Servicios de Inteligencia lo descubren y muy pronto lo extorsionarán exigiéndole que transporte unas misteriosas valijas en la ruta Buenos Aires–Madrid sin hacer preguntas. Alerta por el enigmático cargamento que lleva, Alejandro se sumergirá en un universo de intriga y corrupción que lo pondrá en peligro a él y a los que ama mientras intenta escapar con vida a cualquier precio.",
            "link": "https://www.cinemacenter.com.ar/img_movies/2645_img2.jpg"
        },
        {
            "id": 4,
            "título": "Super Mario Bros",
            "director/ra": "Aaron Horvath, Michael Jenelic",
            "año": 2023,
            "género": "animación",
            "sinópsis": "Dirigida por by Aaron Horvath y Michael Jelenic (colaboradores en Los Jóvenes Titanes en acción, Jóvenes Titanes en acción: la película) de un guion de Matthew Fogel (La gran aventura LEGO 2, Minions: Nace un villano), la película es protagonizada por Chris Pratt como Mario, Anya Taylor-Joy como la Princesa Peach, Charlie Day como Luigi, Jack Black como Bowser, Keegan-Michael Key como Toad, Seth Rogen como Donkey Kong, Fred Armisen como Cranky Kong, Kevin Michael Richardson como Kamek y Sebastian Maniscalco como Spike.",
            "link": "https://www.cinemacenter.com.ar/img_movies/2561_img2.jpg"
        },
        {
            "id": 5,
            "título": "Spiderman: Across the Spiderverse",
            "director/ra": "Joaquim Dos Santos, Kemp Powers, Justin K. Thompson",
            "año": 2023,
            "género": "animación",
            "sinópsis": "Miles Morales regresa para el siguiente capítulo de la saga Spider-Verse, ganadora de un Oscar®, una aventura épica que transportará al simpático Spider-Man de Brooklyn a tiempo completo a través del Multiverso para unir fuerzas con Gwen Stacy y un nuevo equipo de Spider-People para enfrentarse a un villano más poderoso que cualquier cosa que hayan encontrado.",
            "link": "https://www.cinemacenter.com.ar/img_movies/2615_img2.jpg"
        },
        {
            "id": 6,
            "título": "Transformers: El Despertar de las Bestias",
            "director/ra": "Steven Caple Jr.",
            "año": 2023,
            "género": "ciencia ficción",
            "sinopsis": "Vuelven la acción y el espectáculo que han cautivado a los cinéfilos de todo el mundo, #Transformers: El despertar de las bestias llevará al público a una aventura alrededor del mundo en los 90 con los Autobots en introducirá a una nueva generación de Transformers, los Maximals, a la batalla existente en la tierra entre Autobots y Decepticons.",
            "link": "https://www.cinemacenter.com.ar/img_movies/2607_img2.jpg"
        },
        {
            "id": 7,
            "título": "The Flash",
            "director/ra": "Andy Muschietti",
            "año": 2023,
            "género": "ciencia ficción",
            "sinopsis": "Los mundos chocan en "Flash" cuando Barry usa sus superpoderes para viajar en el tiempo y cambiar los eventos del pasado. Pero cuando su intento de salvar a su familia altera el futuro sin darse cuenta, Barry queda atrapado en una realidad en la que el general Zod ha regresado, amenazando con la aniquilación, y no hay superhéroes a los que recurrir. Es decir, a menos que Barry pueda sacar a un Batman muy diferente de su retiro y rescatar a un kryptoniano encarcelado... aunque no sea el que está buscando. En última instancia, para salvar el mundo en el que se encuentra y regresar al futuro que conoce, la única esperanza de Barry es escapar de él para salvar su vida. Pero, ¿será suficiente hacer el último sacrificio para reiniciar el universo?",
            "link": "https://www.cinemacenter.com.ar/img_movies/2646_img2.jpg"
        },
        {
            "id": 8,
            "título": "Elemental",
            "director/ra": "Peter Sohn",
            "año": 2023,
            "género": "animación",
            "sinopsis": "Elemental, de Disney y Pixar, es un nuevo largometraje original ambientado en Elemental City, donde conviven habitantes de fuego, agua, tierra y aire. La protagonista de la historia es Ember, una joven fuerte, ingeniosa y con carácter, cuya amistad con un chico divertido, sensible y tranquilo, llamado Wade, cambia su perspectiva sobre el mundo en el que viven.",
            "link": "https://www.cinemacenter.com.ar/img_movies/2626_img2.jpg"
        },
        {
            "id": 9,
            "título": "Boogeyman: Tu Miedo Es Real",
            "director/ra": "Rob Savage",
            "año": 2023,
            "género": "terror",
            "sinopsis": "BOOGEYMAN: TU MIEDO ES REAL es un clásico del cine de terror al estilo de “Poltergeist”, que asusta y muestra un costado más humano en igual medida, dice su director, Rob Savage. Recuerdo vívidamente el terror que sentí al leer el cuento corto de King cuando era niño, y es esta sensación de miedo infantil lo que quería inspirarle a las audiencias de todo el mundo. Esta película se realizó en colaboración con un equipo de creativos increíblemente talentosos y está anclada en las maravillosas y conmovedoras intepretaciones de nuestro extraordinario elenco que me ha asombrado, de verdad. Estamos orgullosos de esta película y estamos ansiosos por darles a todos una razón para temer a la oscuridad nuevamente el 1 de junio.",
            "link": "https://www.cinemacenter.com.ar/img_movies/2655_img2.jpg"
        }
    ],
}
'''
directores = '''
{
    "directores": [
        {
            "id": 10,
            "La Sirenita": "Rob Marshall"
        },
        {
            "id": 11,
            "Rápidos y Furiosos X": "Louis Leterrier"
        },
        {
            "id": 12,
            "Guardianes de la Galaxia Vol. 3": "James Gunn"
        },
        {
            "id": 13,
            "La Extorsión": "Martino Zaidelis"
        },
        {
            "id": 14,
            "Super Mario Bros": "Aaron Horvath, Michael Jenelic"
        },
        {
            "id": 15,
            "Spiderman: Across the Spiderverse": "Joaquim Dos Santos, Kemp Powers, Justin K. Thompson"
        },
        {
            "id": 16,
            "Transformers: El Despertar de las Bestias": "Steven Caple Jr."
        },
        {
            "id": 17,
            "The Flash": "Andy Muschietti"
        },
        {
            "id": 18,
            "Elemental": "Peter Sohn"
        },
        {
            "id": 19,
            "Boogeyman: Tu Miedo Es Real": "Rob Savage"
        }
    ]
}
'''
generos = '''
{
    "géneros": [
        {
            "id": 20,
            "La Sirenita": "aventuras"
        },
        {
            "id": 21,
            "Rápidos y Furiosos X": "acción"
        },
        {
            "id": 22,
            "Guardianes de la Galaxia Vol. 3": "ciencia ficción"
        },
        {
            "id": 23,
            "La Extorsión": "drama"
        },
        {
            "id": 24,
            "Super Mario Bros": "animación"
        },
        {
            "id": 25,
            "Spiderman: Across the Spiderverse": "animación"
        },
        {
            "id": 26,
            "Transformers: El Despertar de las Bestias": "ciencia ficción"
        },
        {
            "id": 27,
            "The Flash": "ciencia ficción"
        },
        {
            "id": 28,
            "Elemental": "animación"
        },
        {
            "id": 29,
            "Boogeyman: Tu Miedo Es Real": "terror"
        }
    ]
}
'''
peliculasDirigidasPor = '''
{
    "películas dirigidas por": [
        "Rob Marshall": [
            {
                "id": 30,
                "título": "Piratas del Caribe: Navegando por Aguas Misteriosas",
                "año": 2011
            },
            {
                "id": 31,
                "titulo": "En El Bosque",
                "año": 2014
            },
            {
                "id": 32,
                "título": "El Regreso de Mary Popins",
                "año": 2018
            }
        ],
        "Louis Leterrier": [
            {
                "id": 40,
                "título": "El Increible Hulk",
                "año": 2008
            },
            {
                "id": 41,
                "título": "Furia de Titanes",
                "año": 2010
            }
        ],
        "James Gunn": [
            {
                "id": 50,
                "título": "Guardianes de la Galaxia",
                "año": 2014
            },
            {
                "id": 51,
                "título": "Guardianes de la Galaxia Vol. 2",
                "año": 2017
            },
            {
                "id": 52,
                "título": "The Suicide Squad",
                "año": 2021
            }
        ],
        "Martino Zaidelis": [
            {
                "id": 60,
                "título": "Re Loca",
                "año": 2018
            }
        ],
        "Aaron Horvath": [
            {
                "id": 70,
                "título": "Teen Titans Go",
                "año": 2018
            }
        ],
        "Steven Caple Jr.": [
            {
                "id": 80,
                "título": "Creed II",
                "año": 2018
            }
        ],
        "Andy Muschietti": [
            {
                "id": 90,
                "título": "Mama",
                "año": 2013
            },
            {
                "id": 91,
                "título": "IT",
                "año": 2017
            },
            {
                "id": 92,
                "título": "IT Capítulo Dos",
                "año": 2019
            }
        ],
        "Peter Sohn": [
            {
                "id": 100,
                "título": "El Buen Dinosaurio",
                "año": 2015
            }
        ]
    ]
}
'''
posters = '''
{
    "posters": [
        {
            "id": 110,
            "La Sirenita": "https://www.cinemacenter.com.ar/img_movies/2627_img2.jpg"
        },
        {
            "id": 111,
            "Rápidos y Furiosos X": "https://www.cinemacenter.com.ar/img_movies/2672_img2.jpg"
        },
        {
            "id": 112,
            "Guardianes de la Galaxia Vol. 3": "https://www.cinemacenter.com.ar/img_movies/2637_img2.jpg"
        },
        {
            "id": 113,
            "La Extorsión": "https://www.cinemacenter.com.ar/img_movies/2645_img2.jpg"
        },
        {
            "id": 114,
            "Super Mario Bros": "https://www.cinemacenter.com.ar/img_movies/2561_img2.jpg"
        },
        {
            "id": 115,
            "Spiderman: Across the Spiderverse": "https://www.cinemacenter.com.ar/img_movies/2615_img2.jpg"
        },
        {
            "id": 116,
            "Transformers: El Despertar de las Bestias": "https://www.cinemacenter.com.ar/img_movies/2607_img2.jpg"
        },
        {
            "id": 117,
            "The Flash": "https://www.cinemacenter.com.ar/img_movies/2646_img2.jpg"
        },
        {
            "id": 118,
            "Elemental": "https://www.cinemacenter.com.ar/img_movies/2626_img2.jpg"
        },
        {
            "id": 119,
            "Boogeyman: Tu Miedo Es Real": "https://www.cinemacenter.com.ar/img_movies/2655_img2.jpg"
        }
    ]
}
'''
ABM = '''
{
    "ABM": [
        {
            "id": 120;
            "La Sirenita": "Bajo"
        },
        {
            "id": 121;
            "Rápidos y Furiosos X": "Modificable"
        },
        {
            "id": 122,
            "Guardianes de la Galaxia Vol. 3": "Alto"
        },
        {
            "id": 123,
            "La Extorsion": "Bajo"
        },
        {
            "id": 124,
            "Super Mario Bros": "Modificable"
        },
        {
            "id": 125,
            "Spiderman: Across the Spiderverse": "Alto"
        },
        {
            "id": 126,
            "Transformers: El Despertar de las Bestias": "Modificable"
        },
        {
            "id": 127,
            "The Flash": "Alto"
        },
        {
            "id": 128,
            "Elemental": "Bajo"
        },
        {
            "id": 129,
            "Boogeyman: Tu Miedo Es Real": "Bajo"
        }
    ]
}
'''
usuarios = '''
{
    "usuarios": [
        {
            "usuario": "Coco814151",
            "contraseña": "Ezequiel151plataforma"
        },
        {
            "usuario": "negrito55fotos",
            "contraseña": "manchitas"
        },
        {
            "usuario": "mymartin",
            "contraseña": "jvk967"
        }
    ]
}
'''
@app.route('/')
def index():
    usuario = request.args.get('usuario', usuarios)
    contraseña = request.args.get('contraseña', usuarios)
@app.route('/usuarios', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('peliculas'))
    return render_template('index.html')

def index():
    return render_template('index.html')
@app.route('/películas')
def peliculas():
    return render_template(peliculas)
@app.route('/directores')
def directores():
    return render_template(directores)
@app.route('/géneros')
def generos():
    return render_template(generos)
@app.route('/películas dirigidas por')
def peliculasDirigidasPor():
    return render_template(peliculasDirigidasPor)
@app.route('/ABM')
def ABM():
    return render_template(ABM)


app.run()
