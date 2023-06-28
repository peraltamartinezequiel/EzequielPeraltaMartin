"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect, url_for
from ProyectoFinal import app
import json

peliculas = '''
{
    "pel�culas": [
        {
            "id": 0,
            "t�tulo": "La Sirenita",
            "director/ra": "Rob Marshall",
            "a�o": 2023,
            "g�nero": "aventuras",
            "sinopsis": "LA SIRENITA, la querida historia de Ariel, una sirena joven y apasionada con ansias de aventuras, est� protagonizada por la cantante y actriz Halle Bailey (CRECIDO) como Ariel; el ganador del premio Tony� Daveed Diggs (Hamilton, El expreso del miedo) como la voz de Sebasti�n; Jacob Tremblay (LUCA, La habitaci�n) como la voz de Flounder; Awkwafina (RAYA Y EL �LTIMO DRAG�N) como la voz de Scuttle; Jonah Hauer-King (A Dog's Way Home) como el Pr�ncipe Eric; Art Malik (HOMELAND) como Sir Grimsby; Noma Dumezweni (EL REGRESO DE MARY POPPINS) como la Reina Selina; con el ganador del Oscar� Javier Bardem (Sin lugar para los d�biles, Being the Ricardos) como el Rey Trit�n; y la dos veces nominada al Oscar� Melissa McCarthy (�PODR�S PERDONARME? , Damas en guerra) como �rsula. Ariel, la m�s joven de las hijas del rey Trit�n y la m�s rebelde, sue�a con conocer el mundo m�s all� del mar y, mientras visita la superficie, se enamora del distinguido pr�ncipe Eric. Aunque las sirenas tienen prohibido relacionarse con los humanos, Ariel debe seguir su coraz�n. Ella hace un trato con la malvada bruja del mar, �rsula, que le da la oportunidad de experimentar la vida sobre la tierra, pero que, en �ltima instancia, pone su vida y la corona de su padre en peligro.",
            "link": "https://www.cinemacenter.com.ar/img_movies/2627_img2.jpg"
        },
        {
            "id": 1,
            "t�tulo": "R�pidos y Furiosos X",
            "director/ra": "Louis Leterrier",
            "a�o": 2023,
            "g�nero": "acci�n",
            "sinopsis": "Comienza el final del camino. R�pidos y furiosos X, la d�cima pel�cula de la saga R�pidos y furiosos, es el cap�tulo final de una de las franquicias m�s populares y queridas del cine, ahora en su tercera d�cada y continuando con el mismo elenco y personajes que cuando comenz�. A trav�s de varias misiones y contra lo imposible, Dom Toretto (Vin Diesel) y su familia han sido m�s astutos y m�s r�pidos que todos los enemigos se le han cruzado en su camino. Ahora se enfrentan a su enemigo m�s letal: una amenaza aterradora que surge de las sombras del pasado que est� alimentado de una venganza sangrienta, y est� decidido a destruir a su familia y destruir todo, y a cualquier persona, A los que Dom ama. En R�pidos y furiosos: 5in control, de 2011, Dom y su equipo derrotaron al infame l�der de la droga brasile�a Hernan Reyes y destruyeron su imperio en un puente de Rio de Janeiro. Lo que no sab�an era que el hijo de Reyes, Dante (Jason Momoa, de Aquaman) presenci� todo y ha pasado 12 a�os creando un plan para que Dom pague el precio m�s alto. El plan de Dante llevar� a la familia de Dom de Los �ngeles a las catacumbas de Roma, de Brasil a Londres, y de Portugal a la Ant�rtida. Se forjaran nuevos aliados y resurgir�n viejos enemigos. Pero todo cambia cuando Dom descubre que su hijo de 8 a�os (Leo Abelo Perry, Black-ish) es el objetivo final de la venganza de Dante."
            "link": "https://www.cinemacenter.com.ar/img_movies/2672_img2.jpg"
        },
        {
            "id": 2,
            "t�tulo": "Guardianes de la Galaxia Vol. 3",
            "director/ra": "James Gunn",
            "a�o": 2023,
            "g�nero": "ciencia ficci�n",
            "sinopsis": "GUARDIANES DE LA GALAXIA VOLUMEN 3 contiene varias escenas con luces intermitentes que pueden afectar a los clientes susceptibles a padecer epilepsia fotosensible u otras fotosensibilidades."
            "link": "https://www.cinemacenter.com.ar/img_movies/2637_img2.jpg"
        },
        {
            "id": 3,
            "t�tulo": "La Extorsi�n",
            "director/ra": "Martino Zaidelis",
            "a�o": 2023,
            "g�nero": "drama",
            "sin�psis": "Alejandro es un experimentado piloto aeron�utico. Amante de su profesi�n, esconde un secreto: una condici�n m�dica que implicar�a su retiro inmediato. Los Servicios de Inteligencia lo descubren y muy pronto lo extorsionar�n exigi�ndole que transporte unas misteriosas valijas en la ruta Buenos Aires�Madrid sin hacer preguntas. Alerta por el enigm�tico cargamento que lleva, Alejandro se sumergir� en un universo de intriga y corrupci�n que lo pondr� en peligro a �l y a los que ama mientras intenta escapar con vida a cualquier precio.",
            "link": "https://www.cinemacenter.com.ar/img_movies/2645_img2.jpg"
        },
        {
            "id": 4,
            "t�tulo": "Super Mario Bros",
            "director/ra": "Aaron Horvath, Michael Jenelic",
            "a�o": 2023,
            "g�nero": "animaci�n",
            "sin�psis": "Dirigida por by Aaron Horvath y Michael Jelenic (colaboradores en Los J�venes Titanes en acci�n, J�venes Titanes en acci�n: la pel�cula) de un guion de Matthew Fogel (La gran aventura LEGO 2, Minions: Nace un villano), la pel�cula es protagonizada por Chris Pratt como Mario, Anya Taylor-Joy como la Princesa Peach, Charlie Day como Luigi, Jack Black como Bowser, Keegan-Michael Key como Toad, Seth Rogen como Donkey Kong, Fred Armisen como Cranky Kong, Kevin Michael Richardson como Kamek y Sebastian Maniscalco como Spike.",
            "link": "https://www.cinemacenter.com.ar/img_movies/2561_img2.jpg"
        },
        {
            "id": 5,
            "t�tulo": "Spiderman: Across the Spiderverse",
            "director/ra": "Joaquim Dos Santos, Kemp Powers, Justin K. Thompson",
            "a�o": 2023,
            "g�nero": "animaci�n",
            "sin�psis": "Miles Morales regresa para el siguiente cap�tulo de la saga Spider-Verse, ganadora de un Oscar�, una aventura �pica que transportar� al simp�tico Spider-Man de Brooklyn a tiempo completo a trav�s del Multiverso para unir fuerzas con Gwen Stacy y un nuevo equipo de Spider-People para enfrentarse a un villano m�s poderoso que cualquier cosa que hayan encontrado.",
            "link": "https://www.cinemacenter.com.ar/img_movies/2615_img2.jpg"
        },
        {
            "id": 6,
            "t�tulo": "Transformers: El Despertar de las Bestias",
            "director/ra": "Steven Caple Jr.",
            "a�o": 2023,
            "g�nero": "ciencia ficci�n",
            "sinopsis": "Vuelven la acci�n y el espect�culo que han cautivado a los cin�filos de todo el mundo, #Transformers: El despertar de las bestias llevar� al p�blico a una aventura alrededor del mundo en los 90 con los Autobots en introducir� a una nueva generaci�n de Transformers, los Maximals, a la batalla existente en la tierra entre Autobots y Decepticons.",
            "link": "https://www.cinemacenter.com.ar/img_movies/2607_img2.jpg"
        },
        {
            "id": 7,
            "t�tulo": "The Flash",
            "director/ra": "Andy Muschietti",
            "a�o": 2023,
            "g�nero": "ciencia ficci�n",
            "sinopsis": "Los mundos chocan en "Flash" cuando Barry usa sus superpoderes para viajar en el tiempo y cambiar los eventos del pasado. Pero cuando su intento de salvar a su familia altera el futuro sin darse cuenta, Barry queda atrapado en una realidad en la que el general Zod ha regresado, amenazando con la aniquilaci�n, y no hay superh�roes a los que recurrir. Es decir, a menos que Barry pueda sacar a un Batman muy diferente de su retiro y rescatar a un kryptoniano encarcelado... aunque no sea el que est� buscando. En �ltima instancia, para salvar el mundo en el que se encuentra y regresar al futuro que conoce, la �nica esperanza de Barry es escapar de �l para salvar su vida. Pero, �ser� suficiente hacer el �ltimo sacrificio para reiniciar el universo?",
            "link": "https://www.cinemacenter.com.ar/img_movies/2646_img2.jpg"
        },
        {
            "id": 8,
            "t�tulo": "Elemental",
            "director/ra": "Peter Sohn",
            "a�o": 2023,
            "g�nero": "animaci�n",
            "sinopsis": "Elemental, de Disney y Pixar, es un nuevo largometraje original ambientado en Elemental City, donde conviven habitantes de fuego, agua, tierra y aire. La protagonista de la historia es Ember, una joven fuerte, ingeniosa y con car�cter, cuya amistad con un chico divertido, sensible y tranquilo, llamado Wade, cambia su perspectiva sobre el mundo en el que viven.",
            "link": "https://www.cinemacenter.com.ar/img_movies/2626_img2.jpg"
        },
        {
            "id": 9,
            "t�tulo": "Boogeyman: Tu Miedo Es Real",
            "director/ra": "Rob Savage",
            "a�o": 2023,
            "g�nero": "terror",
            "sinopsis": "BOOGEYMAN: TU MIEDO ES REAL es un cl�sico del cine de terror al estilo de �Poltergeist�, que asusta y muestra un costado m�s humano en igual medida, dice su director, Rob Savage. Recuerdo v�vidamente el terror que sent� al leer el cuento corto de King cuando era ni�o, y es esta sensaci�n de miedo infantil lo que quer�a inspirarle a las audiencias de todo el mundo. Esta pel�cula se realiz� en colaboraci�n con un equipo de creativos incre�blemente talentosos y est� anclada en las maravillosas y conmovedoras intepretaciones de nuestro extraordinario elenco que me ha asombrado, de verdad. Estamos orgullosos de esta pel�cula y estamos ansiosos por darles a todos una raz�n para temer a la oscuridad nuevamente el 1 de junio.",
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
            "R�pidos y Furiosos X": "Louis Leterrier"
        },
        {
            "id": 12,
            "Guardianes de la Galaxia Vol. 3": "James Gunn"
        },
        {
            "id": 13,
            "La Extorsi�n": "Martino Zaidelis"
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
    "g�neros": [
        {
            "id": 20,
            "La Sirenita": "aventuras"
        },
        {
            "id": 21,
            "R�pidos y Furiosos X": "acci�n"
        },
        {
            "id": 22,
            "Guardianes de la Galaxia Vol. 3": "ciencia ficci�n"
        },
        {
            "id": 23,
            "La Extorsi�n": "drama"
        },
        {
            "id": 24,
            "Super Mario Bros": "animaci�n"
        },
        {
            "id": 25,
            "Spiderman: Across the Spiderverse": "animaci�n"
        },
        {
            "id": 26,
            "Transformers: El Despertar de las Bestias": "ciencia ficci�n"
        },
        {
            "id": 27,
            "The Flash": "ciencia ficci�n"
        },
        {
            "id": 28,
            "Elemental": "animaci�n"
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
    "pel�culas dirigidas por": [
        "Rob Marshall": [
            {
                "id": 30,
                "t�tulo": "Piratas del Caribe: Navegando por Aguas Misteriosas",
                "a�o": 2011
            },
            {
                "id": 31,
                "titulo": "En El Bosque",
                "a�o": 2014
            },
            {
                "id": 32,
                "t�tulo": "El Regreso de Mary Popins",
                "a�o": 2018
            }
        ],
        "Louis Leterrier": [
            {
                "id": 40,
                "t�tulo": "El Increible Hulk",
                "a�o": 2008
            },
            {
                "id": 41,
                "t�tulo": "Furia de Titanes",
                "a�o": 2010
            }
        ],
        "James Gunn": [
            {
                "id": 50,
                "t�tulo": "Guardianes de la Galaxia",
                "a�o": 2014
            },
            {
                "id": 51,
                "t�tulo": "Guardianes de la Galaxia Vol. 2",
                "a�o": 2017
            },
            {
                "id": 52,
                "t�tulo": "The Suicide Squad",
                "a�o": 2021
            }
        ],
        "Martino Zaidelis": [
            {
                "id": 60,
                "t�tulo": "Re Loca",
                "a�o": 2018
            }
        ],
        "Aaron Horvath": [
            {
                "id": 70,
                "t�tulo": "Teen Titans Go",
                "a�o": 2018
            }
        ],
        "Steven Caple Jr.": [
            {
                "id": 80,
                "t�tulo": "Creed II",
                "a�o": 2018
            }
        ],
        "Andy Muschietti": [
            {
                "id": 90,
                "t�tulo": "Mama",
                "a�o": 2013
            },
            {
                "id": 91,
                "t�tulo": "IT",
                "a�o": 2017
            },
            {
                "id": 92,
                "t�tulo": "IT Cap�tulo Dos",
                "a�o": 2019
            }
        ],
        "Peter Sohn": [
            {
                "id": 100,
                "t�tulo": "El Buen Dinosaurio",
                "a�o": 2015
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
            "R�pidos y Furiosos X": "https://www.cinemacenter.com.ar/img_movies/2672_img2.jpg"
        },
        {
            "id": 112,
            "Guardianes de la Galaxia Vol. 3": "https://www.cinemacenter.com.ar/img_movies/2637_img2.jpg"
        },
        {
            "id": 113,
            "La Extorsi�n": "https://www.cinemacenter.com.ar/img_movies/2645_img2.jpg"
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
            "R�pidos y Furiosos X": "Modificable"
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
            "contrase�a": "Ezequiel151plataforma"
        },
        {
            "usuario": "negrito55fotos",
            "contrase�a": "manchitas"
        },
        {
            "usuario": "mymartin",
            "contrase�a": "jvk967"
        }
    ]
}
'''
@app.route('/')
def index():
    usuario = request.args.get('usuario', usuarios)
    contrase�a = request.args.get('contrase�a', usuarios)
@app.route('/usuarios', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrase�a = request.form['contrase�a']
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('peliculas'))
    return render_template('index.html')

def index():
    return render_template('index.html')
@app.route('/pel�culas')
def peliculas():
    return render_template(peliculas)
@app.route('/directores')
def directores():
    return render_template(directores)
@app.route('/g�neros')
def generos():
    return render_template(generos)
@app.route('/pel�culas dirigidas por')
def peliculasDirigidasPor():
    return render_template(peliculasDirigidasPor)
@app.route('/ABM')
def ABM():
    return render_template(ABM)


app.run()
