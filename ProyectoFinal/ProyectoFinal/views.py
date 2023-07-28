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
       "t�tulo": "La Sirenita",
       "director/ra": "Rob Marshall",
       "a�o": 2023,
       "g�nero": "aventuras",
       "sinopsis": "LA SIRENITA, la querida historia de Ariel, una sirena joven y apasionada con ansias de aventuras, est� protagonizada por la cantante y actriz Halle Bailey (CRECIDO) como Ariel; el ganador del premio Tony� Daveed Diggs (Hamilton, El expreso del miedo) como la voz de Sebasti�n; Jacob Tremblay (LUCA, La habitaci�n) como la voz de Flounder; Awkwafina (RAYA Y EL �LTIMO DRAG�N) como la voz de Scuttle; Jonah Hauer-King (A Dog's Way Home) como el Pr�ncipe Eric; Art Malik (HOMELAND) como Sir Grimsby; Noma Dumezweni (EL REGRESO DE MARY POPPINS) como la Reina Selina; con el ganador del Oscar� Javier Bardem (Sin lugar para los d�biles, Being the Ricardos) como el Rey Trit�n; y la dos veces nominada al Oscar� Melissa McCarthy (�PODR�S PERDONARME? , Damas en guerra) como �rsula. Ariel, la m�s joven de las hijas del rey Trit�n y la m�s rebelde, sue�a con conocer el mundo m�s all� del mar y, mientras visita la superficie, se enamora del distinguido pr�ncipe Eric. Aunque las sirenas tienen prohibido relacionarse con los humanos, Ariel debe seguir su coraz�n. Ella hace un trato con la malvada bruja del mar, �rsula, que le da la oportunidad de experimentar la vida sobre la tierra, pero que, en �ltima instancia, pone su vida y la corona de su padre en peligro.",
       "link": "https://www.cinemacenter.com.ar/img_movies/2627_img2.jpg",
       "comentario": "",
       "puntuaci�n": 3
    },
    {
        "t�tulo": "R�pidos y Furiosos X",
        "director/ra": "Louis Leterrier",
        "a�o": 2023,
        "g�nero": "acci�n",
        "sinopsis": "Comienza el final del camino. R�pidos y furiosos X, la d�cima pel�cula de la saga R�pidos y furiosos, es el cap�tulo final de una de las franquicias m�s populares y queridas del cine, ahora en su tercera d�cada y continuando con el mismo elenco y personajes que cuando comenz�. A trav�s de varias misiones y contra lo imposible, Dom Toretto (Vin Diesel) y su familia han sido m�s astutos y m�s r�pidos que todos los enemigos se le han cruzado en su camino. Ahora se enfrentan a su enemigo m�s letal: una amenaza aterradora que surge de las sombras del pasado que est� alimentado de una venganza sangrienta, y est� decidido a destruir a su familia y destruir todo, y a cualquier persona, A los que Dom ama. En R�pidos y furiosos: 5in control, de 2011, Dom y su equipo derrotaron al infame l�der de la droga brasile�a Hernan Reyes y destruyeron su imperio en un puente de Rio de Janeiro. Lo que no sab�an era que el hijo de Reyes, Dante (Jason Momoa, de Aquaman) presenci� todo y ha pasado 12 a�os creando un plan para que Dom pague el precio m�s alto. El plan de Dante llevar� a la familia de Dom de Los �ngeles a las catacumbas de Roma, de Brasil a Londres, y de Portugal a la Ant�rtida. Se forjaran nuevos aliados y resurgir�n viejos enemigos. Pero todo cambia cuando Dom descubre que su hijo de 8 a�os (Leo Abelo Perry, Black-ish) es el objetivo final de la venganza de Dante."
        "link": "https://www.cinemacenter.com.ar/img_movies/2672_img2.jpg",
        "comentario": "",
        "puntuaci�n": 6
    },
    {
        "t�tulo": "Guardianes de la Galaxia Vol. 3",
        "director/ra": "James Gunn",
        "a�o": 2023,
        "g�nero": "ciencia ficci�n",
        "sinopsis": "GUARDIANES DE LA GALAXIA VOLUMEN 3 contiene varias escenas con luces intermitentes que pueden afectar a los clientes susceptibles a padecer epilepsia fotosensible u otras fotosensibilidades."
        "link": "https://www.cinemacenter.com.ar/img_movies/2637_img2.jpg",
        "comentario": "",
        "puntuaci�n": 9
    },
    {
        "t�tulo": "La Extorsi�n",
        "director/ra": "Martino Zaidelis",
        "a�o": 2023,
        "g�nero": "drama",
        "sin�psis": "Alejandro es un experimentado piloto aeron�utico. Amante de su profesi�n, esconde un secreto: una condici�n m�dica que implicar�a su retiro inmediato. Los Servicios de Inteligencia lo descubren y muy pronto lo extorsionar�n exigi�ndole que transporte unas misteriosas valijas en la ruta Buenos Aires�Madrid sin hacer preguntas. Alerta por el enigm�tico cargamento que lleva, Alejandro se sumergir� en un universo de intriga y corrupci�n que lo pondr� en peligro a �l y a los que ama mientras intenta escapar con vida a cualquier precio.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2645_img2.jpg",
        "comentario": "",
        "puntuaci�n": 4
    },
    {
        "t�tulo": "Super Mario Bros",
        "director/ra": "Aaron Horvath, Michael Jenelic",
        "a�o": 2023,
        "g�nero": "animaci�n",
        "sin�psis": "Dirigida por by Aaron Horvath y Michael Jelenic (colaboradores en Los J�venes Titanes en acci�n, J�venes Titanes en acci�n: la pel�cula) de un guion de Matthew Fogel (La gran aventura LEGO 2, Minions: Nace un villano), la pel�cula es protagonizada por Chris Pratt como Mario, Anya Taylor-Joy como la Princesa Peach, Charlie Day como Luigi, Jack Black como Bowser, Keegan-Michael Key como Toad, Seth Rogen como Donkey Kong, Fred Armisen como Cranky Kong, Kevin Michael Richardson como Kamek y Sebastian Maniscalco como Spike.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2561_img2.jpg",
        "comentario": "",
        "puntuaci�n": 7
    },
    {
        "t�tulo": "Spiderman: Across the Spiderverse",
        "director/ra": "Joaquim Dos Santos, Kemp Powers, Justin K. Thompson",
        "a�o": 2023,
        "g�nero": "animaci�n",
        "sin�psis": "Miles Morales regresa para el siguiente cap�tulo de la saga Spider-Verse, ganadora de un Oscar�, una aventura �pica que transportar� al simp�tico Spider-Man de Brooklyn a tiempo completo a trav�s del Multiverso para unir fuerzas con Gwen Stacy y un nuevo equipo de Spider-People para enfrentarse a un villano m�s poderoso que cualquier cosa que hayan encontrado.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2615_img2.jpg",
        "comentario": "",
        "puntuaci�n": 10
    },
    {
        "t�tulo": "Transformers: El Despertar de las Bestias",
        "director/ra": "Steven Caple Jr.",
        "a�o": 2023,
        "g�nero": "ciencia ficci�n",
        "sinopsis": "Vuelven la acci�n y el espect�culo que han cautivado a los cin�filos de todo el mundo, #Transformers: El despertar de las bestias llevar� al p�blico a una aventura alrededor del mundo en los 90 con los Autobots en introducir� a una nueva generaci�n de Transformers, los Maximals, a la batalla existente en la tierra entre Autobots y Decepticons.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2607_img2.jpg",
        "comentario": "",
        "puntuaci�n": 5
    },
    {
        "t�tulo": "The Flash",
        "director/ra": "Andy Muschietti",
        "a�o": 2023,
        "g�nero": "ciencia ficci�n",
        "sinopsis": "Los mundos chocan en "Flash" cuando Barry usa sus superpoderes para viajar en el tiempo y cambiar los eventos del pasado. Pero cuando su intento de salvar a su familia altera el futuro sin darse cuenta, Barry queda atrapado en una realidad en la que el general Zod ha regresado, amenazando con la aniquilaci�n, y no hay superh�roes a los que recurrir. Es decir, a menos que Barry pueda sacar a un Batman muy diferente de su retiro y rescatar a un kryptoniano encarcelado... aunque no sea el que est� buscando. En �ltima instancia, para salvar el mundo en el que se encuentra y regresar al futuro que conoce, la �nica esperanza de Barry es escapar de �l para salvar su vida. Pero, �ser� suficiente hacer el �ltimo sacrificio para reiniciar el universo?",
        "link": "https://www.cinemacenter.com.ar/img_movies/2646_img2.jpg",
        "comentario": "",
        "puntuaci�n": 6
    },
    {
        "t�tulo": "Elemental",
        "director/ra": "Peter Sohn",
        "a�o": 2023,
        "g�nero": "animaci�n",
        "sinopsis": "Elemental, de Disney y Pixar, es un nuevo largometraje original ambientado en Elemental City, donde conviven habitantes de fuego, agua, tierra y aire. La protagonista de la historia es Ember, una joven fuerte, ingeniosa y con car�cter, cuya amistad con un chico divertido, sensible y tranquilo, llamado Wade, cambia su perspectiva sobre el mundo en el que viven.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2626_img2.jpg",
        "comentario": "",
        "puntuaci�n": 4
    },
    {
        "t�tulo": "Boogeyman: Tu Miedo Es Real",
        "director/ra": "Rob Savage",
        "a�o": 2023,
        "g�nero": "terror",
        "sinopsis": "BOOGEYMAN: TU MIEDO ES REAL es un cl�sico del cine de terror al estilo de �Poltergeist�, que asusta y muestra un costado m�s humano en igual medida, dice su director, Rob Savage. Recuerdo v�vidamente el terror que sent� al leer el cuento corto de King cuando era ni�o, y es esta sensaci�n de miedo infantil lo que quer�a inspirarle a las audiencias de todo el mundo. Esta pel�cula se realiz� en colaboraci�n con un equipo de creativos incre�blemente talentosos y est� anclada en las maravillosas y conmovedoras intepretaciones de nuestro extraordinario elenco que me ha asombrado, de verdad. Estamos orgullosos de esta pel�cula y estamos ansiosos por darles a todos una raz�n para temer a la oscuridad nuevamente el 1 de junio.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2655_img2.jpg",
        "comentario": "",
        "puntuaci�n": 5
    }
]
'''
directores = '/templates/directores.html'
generos = '/templates/generos.html'
direccion = '''
{
        "Rob Marshall": [
            {
                "t�tulo": "Piratas del Caribe: Navegando por Aguas Misteriosas",
                "a�o": 2011
            },
            {
                "titulo": "En El Bosque",
                "a�o": 2014
            },
            {
                "t�tulo": "El Regreso de Mary Popins",
                "a�o": 2018
            }
        ],
        "Louis Leterrier": [
            {
                "t�tulo": "El Increible Hulk",
                "a�o": 2008
            },
            {
                "t�tulo": "Furia de Titanes",
                "a�o": 2010
            }
        ],
        "James Gunn": [
            {
                "t�tulo": "Guardianes de la Galaxia",
                "a�o": 2014
            },
            {
                "t�tulo": "Guardianes de la Galaxia Vol. 2",
                "a�o": 2017
            },
            {
                "t�tulo": "The Suicide Squad",
                "a�o": 2021
            }
        ],
        "Martino Zaidelis": [
            {
                "t�tulo": "Re Loca",
                "a�o": 2018
            }
        ],
        "Aaron Horvath": [
            {
                "t�tulo": "Teen Titans Go",
                "a�o": 2018
            }
        ],
        "Steven Caple Jr.": [
            {
                "t�tulo": "Creed II",
                "a�o": 2018
            }
        ],
        "Andy Muschietti": [
            {
                "t�tulo": "Mama",
                "a�o": 2013
            },
            {
                "t�tulo": "IT",
                "a�o": 2017
            },
            {
                "t�tulo": "IT Cap�tulo Dos",
                "a�o": 2019
            }
        ],
        "Peter Sohn": [
            {
                "t�tulo": "El Buen Dinosaurio",
                "a�o": 2015
            }
        ]  
}
'''
posters = '''
{
    "La Sirenita": "https://www.cinemacenter.com.ar/img_movies/2627_img2.jpg",
    "R�pidos y Furiosos X": "https://www.cinemacenter.com.ar/img_movies/2672_img2.jpg",
    "Guardianes de la Galaxia Vol. 3": "https://www.cinemacenter.com.ar/img_movies/2637_img2.jpg",
    "La Extorsi�n": "https://www.cinemacenter.com.ar/img_movies/2645_img2.jpg",
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
    "R�pidos y Furiosos X": "Modificable",
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
    "ciencia ficci�n": "Alto",
    "acci�n": "Modificable",
    "aventuras": "Modificable",
    "terror": "Modificable",
    "animaci�n": "Bajo",
    "drama": "Modificable"
}
'''
usuarios = '''
[
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
        contrase�a = request.form['contrase�a']
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
        titulo1 = request.args.get('t�tulo')
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
        anio = request.form['a�o']
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
            "t�tulo": titulo,
            "director/ra": director,
            "a�o": anio,
            "g�nero": genero,
            "sinopsis": sinopsis,
            "link": link,
            "comentario": comentario,
            "puntuaci�n": puntuacion
        }
        peliculas.append(pelicula)
    for i in peliculas:
        director.append(i['director/ra'])
        genero.append(i['g�nero'])
    return render_template('agregacion.html', name = usuario(), pelicula = pelicula, director = director, genero = genero)
@app.route('/edicion/<pelicula>', methods = ['GET', 'POST'])
def edicion(pelicula):
    if usuario not in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        for i in peliculas:
            if i['t�tulo'] == pelicula:
                if request.form.get('titulo') != '':
                    i['t�tulo'] = request.form.get('titulo')
                if request.form.get('director') != '':
                    i['director/ra'] = request.form.get('director')
                if request.form.get('a�o') != '':
                    i['a�o'] = request.form.get('a�o')
                if request.form.get('genero') != '':
                    i['g�nero'] = request.form.get('genero')
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
                    i['puntuaci�n'] = request.form.get('puntuacion')
    return render_template('edicion.html', nombre = usuario(), pelicula = pelicula)
@app.route('/eliminacion/<pelicula>', methods=['GET', 'POST'])
def eliminacion(pelicula):
    if 'usuario' not in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        for i in peliculas:
            if i['t�tulo'] == pelicula:
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
            if request.form['genero'] == i['g�nero']:
                i['g�nero'] = request.form['nuevo_genero']
        return redirect(url_for('peliculas'))
    return render_template('modificacion_genero.html', nombre = usuario(), peliculas = peliculas)
@app.route('/directores')
def directores():
    return jsonify(directores)
@app.route('/g�neros')
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
