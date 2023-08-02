import math
from flask import Flask, render_template, request, redirect, url_for, jsonify, session

app = Flask(__name__)
wsgi_app = app.wsgi_app

peliculas = [
    {
        "titulo": "La Sirenita",
        "director": "Rob Marshall",
        "anio": 2023,
        "genero": "aventuras",
        "sinopsis": "Ariel, la mas joven de las hijas del rey Triton y la mas rebelde, suenia con conocer el mundo mas alla del mar y, mientras visita la superficie, se enamora del distinguido principe Eric. Aunque las sirenas tienen prohibido relacionarse con los humanos, Ariel debe seguir su corazon. Ella hace un trato con la malvada bruja del mar, Ursula, que le da la oportunidad de experimentar la vida sobre la tierra, pero que, en ultima instancia, pone su vida y la corona de su padre en peligro.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2627_img2.jpg",
        "comentario": "",
        "puntuacion": 3
    },
    {
        "titulo": "Rapidos y Furiosos X",
        "director": "Louis Leterrier",
        "anio": 2023,
        "genero": "accion",
        "sinopsis": "Comienza el final del camino. Rapidos y furiosos X, la decima pelicula de la saga Rapidos y furiosos, es el capitulo final de una de las franquicias mas populares y queridas del cine, ahora en su tercera decada y continuando con el mismo elenco y personajes que cuando comenzo. A traves de varias misiones y contra lo imposible, Dom Toretto (Vin Diesel) y su familia han sido mas astutos y mas rapidos que todos los enemigos se le han cruzado en su camino. Ahora se enfrentan a su enemigo mas letal: una amenaza aterradora que surge de las sombras del pasado que esta alimentado de una venganza sangrienta, y esta decidido a destruir a su familia y destruir todo, y a cualquier persona, A los que Dom ama. En Rapidos y furiosos: Sin control, de 2011, Dom y su equipo derrotaron al infame lider de la droga brasilenia Hernan Reyes y destruyeron su imperio en un puente de Rio de Janeiro. Lo que no sabian era que el hijo de Reyes, Dante (Jason Momoa, de Aquaman) presencio todo y ha pasado 12 anios creando un plan para que Dom pague el precio mas alto. El plan de Dante llevara a la familia de Dom de Los Angeles a las catacumbas de Roma, de Brasil a Londres, y de Portugal a la Antartida. Se forjaran nuevos aliados y resurgiran viejos enemigos. Pero todo cambia cuando Dom descubre que su hijo de 8 anios (Leo Abelo Perry, Black-ish) es el objetivo final de la venganza de Dante.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2672_img2.jpg",
        "comentario": "",
        "puntuacion": 6
    },
    {
        "titulo": "Guardianes de la Galaxia 3",
        "director": "James Gunn",
        "anio": 2023,
        "genero": "ciencia ficcion",
        "sinopsis": "GUARDIANES DE LA GALAXIA VOLUMEN 3 contiene varias escenas con luces intermitentes que pueden afectar a los clientes susceptibles a padecer epilepsia fotosensible u otras fotosensibilidades.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2637_img2.jpg",
        "comentario": "",
        "puntuacion": 9
    },
    {
        "titulo": "La Extorsion",
        "director": "Martino Zaidelis",
        "anio": 2023,
        "genero": "drama",
        "sinopsis": "Alejandro es un experimentado piloto aeronautico. Amante de su profesion, esconde un secreto: una condicion medica que implicaria su retiro inmediato. Los Servicios de Inteligencia lo descubren y muy pronto lo extorsionaran exigiendole que transporte unas misteriosas valijas en la ruta Buenos Aires Madrid sin hacer preguntas. Alerta por el enigmatico cargamento que lleva, Alejandro se sumergira en un universo de intriga y corrupcion que lo pondra en peligro a el y a los que ama mientras intenta escapar con vida a cualquier precio.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2645_img2.jpg",
        "comentario": "",
        "puntuacion": 4
    },
    {
        "titulo": "Super Mario Bros",
        "director": "Aaron Horvath, Michael Jenelic",
        "anio": 2023,
        "genero": "animacion",
        "sinopsis": "Dirigida por by Aaron Horvath y Michael Jelenic (colaboradores en Los Jovenes Titanes en accion, Jovenes Titanes en accion: la pelicula) de un guion de Matthew Fogel (La gran aventura LEGO 2, Minions: Nace un villano), la pelicula es protagonizada por Chris Pratt como Mario, Anya Taylor-Joy como la Princesa Peach, Charlie Day como Luigi, Jack Black como Bowser, Keegan-Michael Key como Toad, Seth Rogen como Donkey Kong, Fred Armisen como Cranky Kong, Kevin Michael Richardson como Kamek y Sebastian Maniscalco como Spike.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2561_img2.jpg",
        "comentario": "",
        "puntuacion": 7
    },
    {
        "titulo": "Spiderman: Across the Spiderverse",
        "director": "Joaquim Dos Santos, Kemp Powers, Justin K. Thompson",
        "anio": 2023,
        "genero": "animacion",
        "sinopsis": "Miles Morales regresa para el siguiente capitulo de la saga Spiderverse, ganadora de un Oscar, una aventura epica que transportara al simpatico Spiderman de Brooklyn a tiempo completo a traves del Multiverso para unir fuerzas con Gwen Stacy y un nuevo equipo de Spiderpeople para enfrentarse a un villano mas poderoso que cualquier cosa que hayan encontrado.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2615_img2.jpg",
        "comentario": "",
        "puntuacion": 10
    },
    {
        "titulo": "Transformers: El Despertar de las Bestias",
        "director": "Steven Caple Jr.",
        "anio": 2023,
        "genero": "ciencia ficcion",
        "sinopsis": "Vuelven la accion y el espectaculo que han cautivado a los cinefilos de todo el mundo, Transformers: El despertar de las bestias llevara al publico a una aventura alrededor del mundo en los 90 con los Autobots en introducira a una nueva generacion de Transformers, los Maximals, a la batalla existente en la tierra entre Autobots y Decepticons.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2607_img2.jpg",
        "comentario": "",
        "puntuacion": 5
    },
    {
        "titulo": "The Flash",
        "director": "Andy Muschietti",
        "anio": 2023,
        "genero": "ciencia ficcion",
        "sinopsis": "Los mundos chocan en Flash cuando Barry usa sus superpoderes para viajar en el tiempo y cambiar los eventos del pasado. Pero cuando su intento de salvar a su familia altera el futuro sin darse cuenta, Barry queda atrapado en una realidad en la que el general Zod ha regresado, amenazando con la aniquilacion, y no hay superheroes a los que recurrir. Es decir, a menos que Barry pueda sacar a un Batman muy diferente de su retiro y rescatar a un kryptoniano encarcelado... aunque no sea el que esta buscando. En ultima instancia, para salvar el mundo en el que se encuentra y regresar al futuro que conoce, la unica esperanza de Barry es escapar de el para salvar su vida. Pero, sera suficiente hacer el ultimo sacrificio para reiniciar el universo?",
        "link": "https://www.cinemacenter.com.ar/img_movies/2646_img2.jpg",
        "comentario": "",
        "puntuacion": 6
    },
    {
        "titulo": "Elemental",
        "director": "Peter Sohn",
        "anio": 2023,
        "genero": "animacion",
        "sinopsis": "Elemental, de Disney y Pixar, es un nuevo largometraje original ambientado en Elemental City, donde conviven habitantes de fuego, agua, tierra y aire. La protagonista de la historia es Ember, una joven fuerte, ingeniosa y con caracter, cuya amistad con un chico divertido, sensible y tranquilo, llamado Wade, cambia su perspectiva sobre el mundo en el que viven.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2626_img2.jpg",
        "comentario": "",
        "puntuacion": 4
    },
    {
        "titulo": "Boogeyman: Tu Miedo Es Real",
        "director": "Rob Savage",
        "anio": 2023,
        "genero": "terror",
        "sinopsis": "BOOGEYMAN: TU MIEDO ES REAL es un clasico del cine de terror al estilo de Poltergeist, que asusta y muestra un costado mas humano en igual medida, dice su director, Rob Savage. Recuerdo vividamente el terror que senti al leer el cuento corto de King cuando era ninio, y es esta sensacion de miedo infantil lo que queria inspirarle a las audiencias de todo el mundo. Esta pelicula se realizo en colaboracion con un equipo de creativos increiblemente talentosos y esta anclada en las maravillosas y conmovedoras intepretaciones de nuestro extraordinario elenco que me ha asombrado, de verdad. Estamos orgullosos de esta pelicula y estamos ansiosos por darles a todos una razon para temer a la oscuridad nuevamente el 1 de junio.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2655_img2.jpg",
        "comentario": "",
        "puntuacion": 5
    }
]
direccion = {
    "Rob Marshall": [
        {
            "titulo": "Piratas del Caribe: Navegando por Aguas Misteriosas",
            "anio": 2011
        },
        {
            "titulo": "En El Bosque",
            "anio": 2014
        },
        {
            "titulo": "El Regreso de Mary Popins",
            "anio": 2018
        }
    ],
    "Louis Leterrier": [
        {
            "titulo": "El Increible Hulk",
            "anio": 2008
        },
        {
            "titulo": "Furia de Titanes",
            "anio": 2010
        }
    ],
    "James Gunn": [
        {
            "titulo": "Guardianes de la Galaxia",
            "anio": 2014
        },
        {
            "titulo": "Guardianes de la Galaxia 2",
            "anio": 2017
        },
        {
            "titulo": "The Suicide Squad",
            "anio": 2021
        }
    ],
    "Martino Zaidelis": [
        {
            "titulo": "Re Loca",
            "anio": 2018
        }
    ],
    "Aaron Horvath": [
        {
            "titulo": "Teen Titans Go",
            "anio": 2018
        }
    ],
    "Steven Caple Jr.": [
        {
            "titulo": "Creed II",
            "anio": 2018
        }
    ],
    "Andy Muschietti": [
        {
            "titulo": "Mama",
            "anio": 2013
        },
        {
            "titulo": "IT",
            "anio": 2017
        },
        {
            "titulo": "IT Capitulo Dos",
            "anio": 2019
        }
    ],
    "Peter Sohn": [
        {
            "titulo": "El Buen Dinosaurio",
            "anio": 2015
        }
    ]  
}
posters = {
    "La Sirenita": "https://www.cinemacenter.com.ar/img_movies/2627_img2.jpg",
    "Rapidos y Furiosos X": "https://www.cinemacenter.com.ar/img_movies/2672_img2.jpg",
    "Guardianes de la Galaxia 3": "https://www.cinemacenter.com.ar/img_movies/2637_img2.jpg",
    "La Extorsion": "https://www.cinemacenter.com.ar/img_movies/2645_img2.jpg",
    "Super Mario Bros": "https://www.cinemacenter.com.ar/img_movies/2561_img2.jpg",
    "Spiderman: Across the Spiderverse": "https://www.cinemacenter.com.ar/img_movies/2615_img2.jpg",
    "Transformers: El Despertar de las Bestias": "https://www.cinemacenter.com.ar/img_movies/2607_img2.jpg",
    "The Flash": "https://www.cinemacenter.com.ar/img_movies/2646_img2.jpg",
    "Elemental": "https://www.cinemacenter.com.ar/img_movies/2626_img2.jpg",
    "Boogeyman: Tu Miedo Es Real": "https://www.cinemacenter.com.ar/img_movies/2655_img2.jpg"
}

ABM_peliculas = {
    "La Sirenita": "Bajo",
    "Rapidos y Furiosos X": "Modificable",
    "Guardianes de la Galaxia 3": "Alto",
    "La Extorsion": "Bajo",
    "Super Mario Bros": "Modificable",
    "Spiderman: Across the Spiderverse": "Alto",
    "Transformers: El Despertar de las Bestias": "Modificable",
    "The Flash": "Alto",
    "Elemental": "Bajo",
    "Boogeyman: Tu Miedo Es Real": "Bajo"
}
ABM_directores = {
    "Rob Marshall": "Bajo",
    "Louis Leterrier": "Bajo",
    "James Gunn": "Alto",
    "Martino Zaidelis": "Modificable",
    "Aaron Horvath": "Modificable",
    "Steven Caple Jr.": "Modificable",
    "Andy Muschietti": "Alto",
    "Peter Sohn": "Modificable",
}
ABM_generos = {
    "ciencia ficciin": "Alto",
    "accion": "Modificable",
    "aventuras": "Modificable",
    "terror": "Modificable",
    "animacion": "Bajo",
    "drama": "Modificable"
}
usuarios = [
    {
        "usuario": "Coco814151",
        "contrasenia": "Ezequiel151plataforma"
    },
    {
        "usuario": "negrito55fotos",
        "contrasenia": "manchitas"
    },
    {
        "usuario": "mymartin",
        "contrasenia": "jvk967"
    }
]
ABM_usuarios = {
    "Coco814151": "Alto",
    "negrito55fotos": "Alto",
    "mymartin": "Modificable"
}
def usuario():
    return session.get("usuario", "")
@app.route("/")
def index():
    contador = 0
    peliculas2 = peliculas
    peliculas2 = list(peliculas2)
    num_pagina = request.args.get("pagina", 1, type=int)
    por_pagina = 10
    inicio_indice = (num_pagina - 1) * por_pagina
    fin_indice = inicio_indice + por_pagina 
    if len(peliculas2) > 1:
        peliculas2.reverse()
    peliculas3 = peliculas2[inicio_indice:fin_indice]
    total_peliculas = len(peliculas)
    total_paginas = math.ceil(total_peliculas/por_pagina)
    session["contador"] = session.get("contador", 0) + 1
    contador = session["contador"]
    return render_template("index.html", nombre = usuario(), peliculas = peliculas3, visitas = contador, total_paginas = total_paginas, pagina_recurrente = num_pagina)
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        contrasenia = request.form["contrasenia"]
        next = request.args.get("next", None)
        for i in usuarios:
            if i["usuario"] == usuario and i["contrasenia"] == contrasenia:
                session["usuario"] = usuario
                return redirect(next or url_for("index"))
        mensaje_error = "Usuario o contrasenia incorrecto."
        return render_template("login.html", nombre=usuario, mensaje_error=mensaje_error)
    return render_template("login.html", nombre=usuario)
@app.route("/peliculas")
def peliculas():
    return render_template("peliculas.html")
@app.route("/peliculas/<director>", methods = ["GET", "POST"])
def pelis_direccion(director):
    peliculas = []
    if request.method == "POST":
        for i in peliculas:
            if i["director"] == director:
                peliculas.append("pelicula")
    return render_template("pelis_direccion.html", nombre = usuario(), director = director, peliculas = peliculas)
@app.route("/buscador")
def buscador():
    titulo1 = request.args.get("titulo")
    resultados = []
    for pelicula in peliculas:
        if titulo1.lower() in pelicula["titulo"].lower():
            resultados.append(pelicula)
    return render_template("buscador.html", nombre=usuario(), resultados=resultados)
@app.route("/agregacion", methods=["GET", "POST"])
def agregacion():
    if request.method == "POST":
        titulo = request.form["Titulo"]
        director = request.form["Director"]
        anio = request.form["Anio"]
        genero = request.form["Genero"]
        sinopsis = request.form["Sinopsis"]
        link = request.form["Link"]
        comentario = request.form["Comentario"]
        puntuacion = request.form["Puntuacion"]
        pelicula = {
            "titulo": titulo,
            "director": director,
            "anio": anio,
            "genero": genero,
            "sinopsis": sinopsis,
            "link": link,
            "comentario": comentario,
            "puntuacion": puntuacion
        }
        peliculas.append(pelicula)
        return redirect(url_for("peliculas"))
    return render_template("agregacion.html")
@app.route("/edicion/<pelicula>", methods = ["GET", "POST"])
def edicion(pelicula):
    if usuario not in session:
        return redirect(url_for("index"))
    if request.method == 'POST':
        for i in peliculas:
            if i["titulo"] == pelicula:
                if request.form.get('Titulo') != '':
                    i["titulo"] = request.form.get("Titulo")
                if request.form.get('Director') != '':
                    i["director"] = request.form.get("Director")
                if request.form.get("Anio") != '':
                    i["anio"] = request.form.get("Anio")
                if request.form.get("Genero") != "":
                    i["genero"] = request.form.get("Genero")
                if request.form.get("Sinopsis") != "":
                    i["sinopsis"] = request.form.get("Sinopsis")
                if request.form.get("Link") != "":
                    i["link"] = request.form.get("Link")
                if request.form.get("Cometario") != "":
                    opinion = request.form.get("Comentario")
                    comentario = i["comentario"]
                    if type(opinion) == str:
                        comentario = comentario.split(",")
                    usuario = ",usuario"
                    nombre = usuario()
                    user = user + nombre
                    usuario = usuario + ":"
                    comentario.append(user)
                    comentario.append(opinion)
                    palabras = "".join(comentario)
                    i["comentario"] = palabras
                if request.form.get('Puntuacion') != '':
                    i["puntuacion"] = request.form.get("Puntuacion")
    return render_template("edicion.html", nombre = usuario(), pelicula = pelicula)
@app.route("/eliminacion/<pelicula>", methods=["GET", "POST"])
def eliminacion(pelicula):
    if "usuario" not in session:
        return redirect(url_for("index"))
    if request.method == "POST":
        for i in peliculas:
            if i["titulo"] == pelicula:
                peliculas.remove(i)
            return redirect(url_for("peliculas"))
    return render_template("eliminacion.html", nombre = usuario(), pelicula = pelicula)
@app.route("/modificacion_director", methods=["GET", "POST"])
def modificacion_director():
    if request.method == "POST":
        old_director = request.form["Director"]
        new_director = request.form["nuevo_director"]

        for pelicula in peliculas:
            if pelicula["director"] == old_director:
                pelicula["director"] = new_director

        return redirect(url_for("peliculas"))

    return render_template("modificacion_director.html", nombre=usuario(), peliculas=peliculas)
@app.route("/modificacion_genero", methods=["GET", "POST"])
def modificacion_genero():
    if request.method == "POST":
        old_genero = request.form["Genero"]
        new_genero = request.form["nuevo_genero"]
        for pelicula in peliculas:
            if pelicula["genero"] == old_genero:
                pelicula["genero"] = new_genero
        return redirect(url_for("peliculas"))
    return render_template("modificacion_genero.html", nombre=usuario(), peliculas=peliculas)
@app.route("/directores")
def directores():
    return render_template("directores.html", nombre = usuario(), peliculas = peliculas)
@app.route("/generos")
def generos():
    return render_template("generos.html", nombre = usuario(), peliculas = peliculas)
@app.route("/direccion")
def direccion():
    return jsonify(direccion)
@app.route("/posters")
def posters():
    return jsonify(posters)
@app.route("/ABM_peliculas")
def ABM_peliculas():
    return jsonify(ABM_peliculas)
@app.route("/ABM_directores")
def ABM_directores():
    return jsonify(ABM_directores)
@app.route("/ABM_generos")
def ABM_generos():
    return jsonify(ABM_generos)
@app.route("/ABM_usuarios")
def ABM_usuarios():
    return jsonify(ABM_usuarios)
@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login"))
@app.errorhandler(404)
def noEncontrado(e):
    return render_template("404.html"), 404
@app.errorhandler(501)
def yaExistente(e):
    return render_template("501.html"), 501
if __name__ == "__main__":
    app.run(debug=True)
