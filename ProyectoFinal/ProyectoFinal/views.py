"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect, url_for, jsonify, session, math
from ProyectoFinal import app
import json

peliculas = '''
[
    {
       "título": "La Sirenita",
       "director/ra": "Rob Marshall",
       "año": 2023,
       "género": "aventuras",
       "sinopsis": "LA SIRENITA, la querida historia de Ariel, una sirena joven y apasionada con ansias de aventuras, está protagonizada por la cantante y actriz Halle Bailey (CRECIDO) como Ariel; el ganador del premio Tony® Daveed Diggs (Hamilton, El expreso del miedo) como la voz de Sebastián; Jacob Tremblay (LUCA, La habitación) como la voz de Flounder; Awkwafina (RAYA Y EL ÚLTIMO DRAGÓN) como la voz de Scuttle; Jonah Hauer-King (A Dog's Way Home) como el Príncipe Eric; Art Malik (HOMELAND) como Sir Grimsby; Noma Dumezweni (EL REGRESO DE MARY POPPINS) como la Reina Selina; con el ganador del Oscar® Javier Bardem (Sin lugar para los débiles, Being the Ricardos) como el Rey Tritón; y la dos veces nominada al Oscar® Melissa McCarthy (¿PODRÁS PERDONARME? , Damas en guerra) como Úrsula. Ariel, la más joven de las hijas del rey Tritón y la más rebelde, sueña con conocer el mundo más allá del mar y, mientras visita la superficie, se enamora del distinguido príncipe Eric. Aunque las sirenas tienen prohibido relacionarse con los humanos, Ariel debe seguir su corazón. Ella hace un trato con la malvada bruja del mar, Úrsula, que le da la oportunidad de experimentar la vida sobre la tierra, pero que, en última instancia, pone su vida y la corona de su padre en peligro.",
       "link": "https://www.cinemacenter.com.ar/img_movies/2627_img2.jpg",
       "comentario": "",
       "puntuación": 3
    },
    {
        "título": "Rápidos y Furiosos X",
        "director/ra": "Louis Leterrier",
        "año": 2023,
        "género": "acción",
        "sinopsis": "Comienza el final del camino. Rápidos y furiosos X, la décima película de la saga Rápidos y furiosos, es el capítulo final de una de las franquicias más populares y queridas del cine, ahora en su tercera década y continuando con el mismo elenco y personajes que cuando comenzó. A través de varias misiones y contra lo imposible, Dom Toretto (Vin Diesel) y su familia han sido más astutos y más rápidos que todos los enemigos se le han cruzado en su camino. Ahora se enfrentan a su enemigo más letal: una amenaza aterradora que surge de las sombras del pasado que está alimentado de una venganza sangrienta, y está decidido a destruir a su familia y destruir todo, y a cualquier persona, A los que Dom ama. En Rápidos y furiosos: 5in control, de 2011, Dom y su equipo derrotaron al infame líder de la droga brasileña Hernan Reyes y destruyeron su imperio en un puente de Rio de Janeiro. Lo que no sabían era que el hijo de Reyes, Dante (Jason Momoa, de Aquaman) presenció todo y ha pasado 12 años creando un plan para que Dom pague el precio más alto. El plan de Dante llevará a la familia de Dom de Los Ángeles a las catacumbas de Roma, de Brasil a Londres, y de Portugal a la Antártida. Se forjaran nuevos aliados y resurgirán viejos enemigos. Pero todo cambia cuando Dom descubre que su hijo de 8 años (Leo Abelo Perry, Black-ish) es el objetivo final de la venganza de Dante."
        "link": "https://www.cinemacenter.com.ar/img_movies/2672_img2.jpg",
        "comentario": "",
        "puntuación": 6
    },
    {
        "título": "Guardianes de la Galaxia Vol. 3",
        "director/ra": "James Gunn",
        "año": 2023,
        "género": "ciencia ficción",
        "sinopsis": "GUARDIANES DE LA GALAXIA VOLUMEN 3 contiene varias escenas con luces intermitentes que pueden afectar a los clientes susceptibles a padecer epilepsia fotosensible u otras fotosensibilidades."
        "link": "https://www.cinemacenter.com.ar/img_movies/2637_img2.jpg",
        "comentario": "",
        "puntuación": 9
    },
    {
        "título": "La Extorsión",
        "director/ra": "Martino Zaidelis",
        "año": 2023,
        "género": "drama",
        "sinópsis": "Alejandro es un experimentado piloto aeronáutico. Amante de su profesión, esconde un secreto: una condición médica que implicaría su retiro inmediato. Los Servicios de Inteligencia lo descubren y muy pronto lo extorsionarán exigiéndole que transporte unas misteriosas valijas en la ruta Buenos Aires–Madrid sin hacer preguntas. Alerta por el enigmático cargamento que lleva, Alejandro se sumergirá en un universo de intriga y corrupción que lo pondrá en peligro a él y a los que ama mientras intenta escapar con vida a cualquier precio.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2645_img2.jpg",
        "comentario": "",
        "puntuación": 4
    },
    {
        "título": "Super Mario Bros",
        "director/ra": "Aaron Horvath, Michael Jenelic",
        "año": 2023,
        "género": "animación",
        "sinópsis": "Dirigida por by Aaron Horvath y Michael Jelenic (colaboradores en Los Jóvenes Titanes en acción, Jóvenes Titanes en acción: la película) de un guion de Matthew Fogel (La gran aventura LEGO 2, Minions: Nace un villano), la película es protagonizada por Chris Pratt como Mario, Anya Taylor-Joy como la Princesa Peach, Charlie Day como Luigi, Jack Black como Bowser, Keegan-Michael Key como Toad, Seth Rogen como Donkey Kong, Fred Armisen como Cranky Kong, Kevin Michael Richardson como Kamek y Sebastian Maniscalco como Spike.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2561_img2.jpg",
        "comentario": "",
        "puntuación": 7
    },
    {
        "título": "Spiderman: Across the Spiderverse",
        "director/ra": "Joaquim Dos Santos, Kemp Powers, Justin K. Thompson",
        "año": 2023,
        "género": "animación",
        "sinópsis": "Miles Morales regresa para el siguiente capítulo de la saga Spider-Verse, ganadora de un Oscar®, una aventura épica que transportará al simpático Spider-Man de Brooklyn a tiempo completo a través del Multiverso para unir fuerzas con Gwen Stacy y un nuevo equipo de Spider-People para enfrentarse a un villano más poderoso que cualquier cosa que hayan encontrado.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2615_img2.jpg",
        "comentario": "",
        "puntuación": 10
    },
    {
        "título": "Transformers: El Despertar de las Bestias",
        "director/ra": "Steven Caple Jr.",
        "año": 2023,
        "género": "ciencia ficción",
        "sinopsis": "Vuelven la acción y el espectáculo que han cautivado a los cinéfilos de todo el mundo, #Transformers: El despertar de las bestias llevará al público a una aventura alrededor del mundo en los 90 con los Autobots en introducirá a una nueva generación de Transformers, los Maximals, a la batalla existente en la tierra entre Autobots y Decepticons.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2607_img2.jpg",
        "comentario": "",
        "puntuación": 5
    },
    {
        "título": "The Flash",
        "director/ra": "Andy Muschietti",
        "año": 2023,
        "género": "ciencia ficción",
        "sinopsis": "Los mundos chocan en "Flash" cuando Barry usa sus superpoderes para viajar en el tiempo y cambiar los eventos del pasado. Pero cuando su intento de salvar a su familia altera el futuro sin darse cuenta, Barry queda atrapado en una realidad en la que el general Zod ha regresado, amenazando con la aniquilación, y no hay superhéroes a los que recurrir. Es decir, a menos que Barry pueda sacar a un Batman muy diferente de su retiro y rescatar a un kryptoniano encarcelado... aunque no sea el que está buscando. En última instancia, para salvar el mundo en el que se encuentra y regresar al futuro que conoce, la única esperanza de Barry es escapar de él para salvar su vida. Pero, ¿será suficiente hacer el último sacrificio para reiniciar el universo?",
        "link": "https://www.cinemacenter.com.ar/img_movies/2646_img2.jpg",
        "comentario": "",
        "puntuación": 6
    },
    {
        "título": "Elemental",
        "director/ra": "Peter Sohn",
        "año": 2023,
        "género": "animación",
        "sinopsis": "Elemental, de Disney y Pixar, es un nuevo largometraje original ambientado en Elemental City, donde conviven habitantes de fuego, agua, tierra y aire. La protagonista de la historia es Ember, una joven fuerte, ingeniosa y con carácter, cuya amistad con un chico divertido, sensible y tranquilo, llamado Wade, cambia su perspectiva sobre el mundo en el que viven.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2626_img2.jpg",
        "comentario": "",
        "puntuación": 4
    },
    {
        "título": "Boogeyman: Tu Miedo Es Real",
        "director/ra": "Rob Savage",
        "año": 2023,
        "género": "terror",
        "sinopsis": "BOOGEYMAN: TU MIEDO ES REAL es un clásico del cine de terror al estilo de “Poltergeist”, que asusta y muestra un costado más humano en igual medida, dice su director, Rob Savage. Recuerdo vívidamente el terror que sentí al leer el cuento corto de King cuando era niño, y es esta sensación de miedo infantil lo que quería inspirarle a las audiencias de todo el mundo. Esta película se realizó en colaboración con un equipo de creativos increíblemente talentosos y está anclada en las maravillosas y conmovedoras intepretaciones de nuestro extraordinario elenco que me ha asombrado, de verdad. Estamos orgullosos de esta película y estamos ansiosos por darles a todos una razón para temer a la oscuridad nuevamente el 1 de junio.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2655_img2.jpg",
        "comentario": "",
        "puntuación": 5
    }
]
'''
directores = '/templates/directores.html'
generos = '/templates/generos.html'
direccion = '''
{
        "Rob Marshall": [
            {
                "título": "Piratas del Caribe: Navegando por Aguas Misteriosas",
                "año": 2011
            },
            {
                "titulo": "En El Bosque",
                "año": 2014
            },
            {
                "título": "El Regreso de Mary Popins",
                "año": 2018
            }
        ],
        "Louis Leterrier": [
            {
                "título": "El Increible Hulk",
                "año": 2008
            },
            {
                "título": "Furia de Titanes",
                "año": 2010
            }
        ],
        "James Gunn": [
            {
                "título": "Guardianes de la Galaxia",
                "año": 2014
            },
            {
                "título": "Guardianes de la Galaxia Vol. 2",
                "año": 2017
            },
            {
                "título": "The Suicide Squad",
                "año": 2021
            }
        ],
        "Martino Zaidelis": [
            {
                "título": "Re Loca",
                "año": 2018
            }
        ],
        "Aaron Horvath": [
            {
                "título": "Teen Titans Go",
                "año": 2018
            }
        ],
        "Steven Caple Jr.": [
            {
                "título": "Creed II",
                "año": 2018
            }
        ],
        "Andy Muschietti": [
            {
                "título": "Mama",
                "año": 2013
            },
            {
                "título": "IT",
                "año": 2017
            },
            {
                "título": "IT Capítulo Dos",
                "año": 2019
            }
        ],
        "Peter Sohn": [
            {
                "título": "El Buen Dinosaurio",
                "año": 2015
            }
        ]  
}
'''
posters = '''
{
    "La Sirenita": "https://www.cinemacenter.com.ar/img_movies/2627_img2.jpg",
    "Rápidos y Furiosos X": "https://www.cinemacenter.com.ar/img_movies/2672_img2.jpg",
    "Guardianes de la Galaxia Vol. 3": "https://www.cinemacenter.com.ar/img_movies/2637_img2.jpg",
    "La Extorsión": "https://www.cinemacenter.com.ar/img_movies/2645_img2.jpg",
    "Super Mario Bros": "https://www.cinemacenter.com.ar/img_movies/2561_img2.jpg",
    "Spiderman: Across the Spiderverse": "https://www.cinemacenter.com.ar/img_movies/2615_img2.jpg",
    "Transformers: El Despertar de las Bestias": "https://www.cinemacenter.com.ar/img_movies/2607_img2.jpg",
    "The Flash": "https://www.cinemacenter.com.ar/img_movies/2646_img2.jpg",
    "Elemental": "https://www.cinemacenter.com.ar/img_movies/2626_img2.jpg",
    "Boogeyman: Tu Miedo Es Real": "https://www.cinemacenter.com.ar/img_movies/2655_img2.jpg"
}
'''
ABM_peliculas = '''
{
    "La Sirenita": "Bajo",
    "Rápidos y Furiosos X": "Modificable",
    "Guardianes de la Galaxia Vol. 3": "Alto",
    "La Extorsion": "Bajo",
    "Super Mario Bros": "Modificable",
    "Spiderman: Across the Spiderverse": "Alto",
    "Transformers: El Despertar de las Bestias": "Modificable",
    "The Flash": "Alto",
    "Elemental": "Bajo",
    "Boogeyman: Tu Miedo Es Real": "Bajo"
}
'''
ABM_directores = '''
{
    "Rob Marshall": "Bajo",
    "Louis Leterrier": "Bajo",
    "James Gunn": "Alto",
    "Martino Zaidelis": "Modificable",
    "Aaron Horvath": "Modificable",
    "Steven Caple Jr.": "Modificable",
    "Andy Muschietti": "Alto",
    "Peter Sohn": "Modificable",
}
'''
ABM_generos = '''
{
    "ciencia ficción": "Alto",
    "acción": "Modificable",
    "aventuras": "Modificable",
    "terror": "Modificable",
    "animación": "Bajo",
    "drama": "Modificable"
}
'''
usuarios = '''
[
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
'''
ABM_usuarios = '''
{
    "Coco814151": "Alto",
    "negrito55fotos": "Alto",
    "mymartin": "Modificable"
}
'''
def usuario():
    if 'usuario' in session:
        nombre = session['usuario']
    else:
        nombre = ''
    return nombre
@app.route('/')
def index():
    contador = 0
    peliculas2 = peliculas
    peliculas2 = list(peliculas2)
    num_pagina = request.args.get('pagina', 1, type=int)
    por_pagina = 10
    inicio_indice = (num_pagina - 1) * por_pagina
    fin_indice = inicio_indice + fin_indice
    if len(peliculas2) > 1:
        peliculas2.reverse()
    peliculas3 = peliculas2[inicio_indice:fin_indice]
    total_peliculas = len(peliculas)
    total_paginas = math.ceil(total_peliculas/por_pagina)
    session['contador'] = session.get('contador', 0) + 1
    contador = session['contador']
    return render_template('index.html', nombre = usuario(), peliculas = peliculas3, visitas = contador, total_paginas = total_paginas, pagina_recurrente = num_pagina)
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/usuarios', methods=['GET', 'POST'])
def usuarios():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('/peliculas'))
    return render_template('login.html')
@app.route('/peliculas')
def peliculas():
    return render_template('peliculas.html')
@app.route('/peliculas/<director>', methods = ['GET', 'POST'])
def pelis_direccion(director):
    peliculas = []
    if request.method == 'POST':
        for i in peliculas:
            if i['director'] == director:
                peliculas.append('pelicula')
    return render_template('pelis_direccion.html', nombre = usuario(), director = director, peliculas = peliculas)
@app.route('/buscador', methods=['GET', 'POST'])
def buscador():
    if request.method == 'GET':
        return render_template('buscador.html')
    if request.method['buscador']:
        titulo1 = request.args.get('título')
        coco_plus = request.method(titulo1)
        data = jsonify(coco_plus)
        print(data)
        return render_template('buscador.html', i = data['i'])
    else:
        return render_template('buscador.html')
@app.route('/agregacion', methods=['GET', 'POST'])
def agregacion():
    if request.method == 'GET':
        return render_template('agregacion.html')
    if request.method['agregacion']:
        agregacion = 'S'
        titulo = request.form['titulo']
        director = request.form['director']
        anio = request.form['año']
        genero = request.form['genero']
        sinopsis = request.form['sinopsis']
        link = request.form['link']
        comentario = request.form['comentario']
        puntuacion = request.form['puntuacion']
        return redirect(url_for('agregacion'), titulo = titulo, director = director, anio = anio, genero = genero, sinopsis = sinopsis, link = link, comentario = comentario, puntuacion = puntuacion)
    director = []
    genero = []
    if 'usuario' not in session:
        return redirect(url_for('peliculas'))
    if agregacion == 'S':
        pelicula = {
            "título": titulo,
            "director/ra": director,
            "año": anio,
            "género": genero,
            "sinopsis": sinopsis,
            "link": link,
            "comentario": comentario,
            "puntuación": puntuacion
        }
        peliculas.append(pelicula)
    for i in peliculas:
        director.append(i['director/ra'])
        genero.append(i['género'])
    return render_template('agregacion.html', name = usuario(), pelicula = pelicula, director = director, genero = genero)
@app.route('/edicion/<pelicula>', methods = ['GET', 'POST'])
def edicion(pelicula):
    if usuario not in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        for i in peliculas:
            if i['título'] == pelicula:
                if request.form.get('titulo') != '':
                    i['título'] = request.form.get('titulo')
                if request.form.get('director') != '':
                    i['director/ra'] = request.form.get('director')
                if request.form.get('año') != '':
                    i['año'] = request.form.get('año')
                if request.form.get('genero') != '':
                    i['género'] = request.form.get('genero')
                if request.form.get('sinopsis') != '':
                    i['sinopsis'] = request.form.get('sinopsis')
                if request.form.get('link') != '':
                    i['link'] = request.form.get('link')
                if request.form.get('cometario') != '':
                    opinion = request.form.get('comentario')
                    comentario = i['comentario']
                    if type(opinion) == str:
                        comentario = comentario.split(',')
                    usuario = ',usuario'
                    nombre = usuario()
                    usuario = usuario + nombre
                    usuario = usuario + ':'
                    comentario.append(usuario)
                    comentario.append(opinion)
                    palabras = "".join(comentario)
                    i['comentario'] = palabras
                if request.form.get('puntuacion') != '':
                    i['puntuación'] = request.form.get('puntuacion')
    return render_template('edicion.html', nombre = usuario(), pelicula = pelicula)
@app.route('/eliminacion/<pelicula>', methods=['GET', 'POST'])
def eliminacion(pelicula):
    if 'usuario' not in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        for i in peliculas:
            if i['título'] == pelicula:
                peliculas.remove(i)
            return redirect(url_for('peliculas'))
    return render_template('eliminacion.html', nombre = usuario, pelicula = pelicula)
@app.route('modificacion_director', methods=['GET', 'POST'])
def modificacion_director():
    if usuario not in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        for i in peliculas:
            if request.form['director'] == i['director']:
                i['director'] = request.form['nuevo_director']
        return redirect(url_for('peliculas'))
    return render_template('modificacion_director.html', nombre = usuario(), peliculas = peliculas)
@app.route('modificacion_genero', methods=['GET', 'POST'])
def modificacion_genero():
    if usuario not in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        for i in peliculas:
            if request.form['genero'] == i['género']:
                i['género'] = request.form['nuevo_genero']
        return redirect(url_for('peliculas'))
    return render_template('modificacion_genero.html', nombre = usuario(), peliculas = peliculas)
@app.route('/directores')
def directores():
    return jsonify(directores)
@app.route('/géneros')
def generos():
    return jsonify(generos)
@app.route('/direccion')
def direccion():
    return jsonify(direccion)
@app.route('/posters')
def posters():
    return jsonify(posters)
@app.route('/ABM_peliculas')
def ABM_peliculas():
    return jsonify(ABM_peliculas)
@app.route('/ABM_directores')
def ABM_directores():
    return jsonify(ABM_directores)
@app.route('/ABM_generos')
def ABM_generos():
    return jsonify(ABM_generos)
@app.route('/ABM_usuarios')
def ABM_usuarios():
    return jsonify(ABM_usuarios)
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))
@app.errorhandler(404)
def noEncontrado():
    return render_template('404.html', 404)
@app.errorhandler(501)
def yaExistente():
    return render_template('501.html', 501)
app.run()
