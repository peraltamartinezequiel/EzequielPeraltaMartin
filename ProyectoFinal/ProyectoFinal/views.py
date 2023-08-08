import math 
from flask import Flask, render_template, request, redirect, url_for, jsonify, session

app = Flask(__name__, template_folder="templates")
app.secret_key = "Ezequiel"

pelis = [
    {
        "titulo": "La Sirenita",
        "director": "Rob Marshall",
        "anio": "2023",
        "genero": "aventuras",
        "actores": "Halle Bailey, Jonah Hauer King, Melissa McCarthy.",
        "sinopsis": "Ariel, la mas joven de las hijas del rey Triton y la mas rebelde, suenia con conocer el mundo mas alla del mar y, mientras visita la superficie, se enamora del distinguido principe Eric. Aunque las sirenas tienen prohibido relacionarse con los humanos, Ariel debe seguir su corazon. Ella hace un trato con la malvada bruja del mar, Ursula, que le da la oportunidad de experimentar la vida sobre la tierra, pero que, en ultima instancia, pone su vida y la corona de su padre en peligro.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2627_img2.jpg",
        "comentario": "",
        "puntuacion": "3"
    },
    {
        "titulo": "Rapidos y Furiosos X",
        "director": "Louis Leterrier",
        "anio": "2023",
        "genero": "accion",
        "actores": "Vin Diesel, Jason Momoa, Michelle Rodriguez.",
        "sinopsis": "Comienza el final del camino. Rapidos y furiosos X, la decima pelicula de la saga Rapidos y furiosos, es el capitulo final de una de las franquicias mas populares y queridas del cine, ahora en su tercera decada y continuando con el mismo elenco y personajes que cuando comenzo. A traves de varias misiones y contra lo imposible, Dom Toretto (Vin Diesel) y su familia han sido mas astutos y mas rapidos que todos los enemigos se le han cruzado en su camino. Ahora se enfrentan a su enemigo mas letal: una amenaza aterradora que surge de las sombras del pasado que esta alimentado de una venganza sangrienta, y esta decidido a destruir a su familia y destruir todo, y a cualquier persona, A los que Dom ama. En Rapidos y furiosos: Sin control, de 2011, Dom y su equipo derrotaron al infame lider de la droga brasilenia Hernan Reyes y destruyeron su imperio en un puente de Rio de Janeiro. Lo que no sabian era que el hijo de Reyes, Dante (Jason Momoa, de Aquaman) presencio todo y ha pasado 12 anios creando un plan para que Dom pague el precio mas alto. El plan de Dante llevara a la familia de Dom de Los Angeles a las catacumbas de Roma, de Brasil a Londres, y de Portugal a la Antartida. Se forjaran nuevos aliados y resurgiran viejos enemigos. Pero todo cambia cuando Dom descubre que su hijo de 8 anios (Leo Abelo Perry, Black-ish) es el objetivo final de la venganza de Dante.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2672_img2.jpg",
        "comentario": "",
        "puntuacion": "6"
    },
    {
        "titulo": "Guardianes de la Galaxia 3",
        "director": "James Gunn",
        "anio": "2023",
        "genero": "ciencia ficcion",
        "actores": "Chris Pratt, Zoe Saldania, Will Pourter.",
        "sinopsis": "GUARDIANES DE LA GALAXIA VOLUMEN 3 contiene varias escenas con luces intermitentes que pueden afectar a los clientes susceptibles a padecer epilepsia fotosensible u otras fotosensibilidades.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2637_img2.jpg",
        "comentario": "",
        "puntuacion": "9"
    },
    {
        "titulo": "La Extorsion",
        "director": "Martino Zaidelis",
        "anio": "2023",
        "genero": "drama",
        "actores": "Guillermo Francella, Andrea Frigerio, Pablo Rago.",
        "sinopsis": "Alejandro es un experimentado piloto aeronautico. Amante de su profesion, esconde un secreto: una condicion medica que implicaria su retiro inmediato. Los Servicios de Inteligencia lo descubren y muy pronto lo extorsionaran exigiendole que transporte unas misteriosas valijas en la ruta Buenos Aires Madrid sin hacer preguntas. Alerta por el enigmatico cargamento que lleva, Alejandro se sumergira en un universo de intriga y corrupcion que lo pondra en peligro a el y a los que ama mientras intenta escapar con vida a cualquier precio.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2645_img2.jpg",
        "comentario": "",
        "puntuacion": "4"
    },
    {
        "titulo": "Super Mario Bros",
        "director": "Aaron Horvath, Michael Jenelic",
        "anio": "2023",
        "genero": "animacion",
        "actores": "Anya Taylor Joy, Chris Pratt, Charlie Day.",
        "sinopsis": "Dirigida por by Aaron Horvath y Michael Jelenic (colaboradores en Los Jovenes Titanes en accion, Jovenes Titanes en accion: la pelicula) de un guion de Matthew Fogel (La gran aventura LEGO 2, Minions: Nace un villano), la pelicula es protagonizada por Chris Pratt como Mario, Anya Taylor-Joy como la Princesa Peach, Charlie Day como Luigi, Jack Black como Bowser, Keegan-Michael Key como Toad, Seth Rogen como Donkey Kong, Fred Armisen como Cranky Kong, Kevin Michael Richardson como Kamek y Sebastian Maniscalco como Spike.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2561_img2.jpg",
        "comentario": "",
        "puntuacion": "7"
    },
    {
        "titulo": "Spiderman: Across the Spiderverse",
        "director": "Joaquim Dos Santos, Kemp Powers, Justin K. Thompson",
        "anio": "2023",
        "genero": "animacion",
        "actores": "Shameick Moore, Oscar Isaac, Hailee Steinfield.",
        "sinopsis": "Miles Morales regresa para el siguiente capitulo de la saga Spiderverse, ganadora de un Oscar, una aventura epica que transportara al simpatico Spiderman de Brooklyn a tiempo completo a traves del Multiverso para unir fuerzas con Gwen Stacy y un nuevo equipo de Spiderpeople para enfrentarse a un villano mas poderoso que cualquier cosa que hayan encontrado.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2615_img2.jpg",
        "comentario": "",
        "puntuacion": "10"
    },
    {
        "titulo": "Transformers: El Despertar de las Bestias",
        "director": "Steven Caple Jr.",
        "anio": "2023",
        "genero": "ciencia ficcion",
        "actores": "Peter Cullen, Ron Perlman, Anthony Ramos.",
        "sinopsis": "Vuelven la accion y el espectaculo que han cautivado a los cinefilos de todo el mundo, Transformers: El despertar de las bestias llevara al publico a una aventura alrededor del mundo en los 90 con los Autobots en introducira a una nueva generacion de Transformers, los Maximals, a la batalla existente en la tierra entre Autobots y Decepticons.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2607_img2.jpg",
        "comentario": "",
        "puntuacion": "5"
    },
    {
        "titulo": "The Flash",
        "director": "Andy Muschietti",
        "anio": "2023",
        "genero": "ciencia ficcion",
        "actores": "Ezra Miller, Michael Keaton, Sasha Calle.",
        "sinopsis": "Los mundos chocan en Flash cuando Barry usa sus superpoderes para viajar en el tiempo y cambiar los eventos del pasado. Pero cuando su intento de salvar a su familia altera el futuro sin darse cuenta, Barry queda atrapado en una realidad en la que el general Zod ha regresado, amenazando con la aniquilacion, y no hay superheroes a los que recurrir. Es decir, a menos que Barry pueda sacar a un Batman muy diferente de su retiro y rescatar a un kryptoniano encarcelado... aunque no sea el que esta buscando. En ultima instancia, para salvar el mundo en el que se encuentra y regresar al futuro que conoce, la unica esperanza de Barry es escapar de el para salvar su vida. Pero, sera suficiente hacer el ultimo sacrificio para reiniciar el universo?",
        "link": "https://www.cinemacenter.com.ar/img_movies/2646_img2.jpg",
        "comentario": "",
        "puntuacion": "6"
    },
    {
        "titulo": "Elemental",
        "director": "Peter Sohn",
        "anio": "2023",
        "genero": "animacion",
        "actores": "Leah Lewis, Mamoudou Athie, Catherine O'Hara.",
        "sinopsis": "Elemental, de Disney y Pixar, es un nuevo largometraje original ambientado en Elemental City, donde conviven habitantes de fuego, agua, tierra y aire. La protagonista de la historia es Ember, una joven fuerte, ingeniosa y con caracter, cuya amistad con un chico divertido, sensible y tranquilo, llamado Wade, cambia su perspectiva sobre el mundo en el que viven.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2626_img2.jpg",
        "comentario": "",
        "puntuacion": "4"
    },
    {
        "titulo": "Boogeyman: Tu Miedo Es Real",
        "director": "Rob Savage",
        "anio": "2023",
        "genero": "terror",
        "actores": "Sophie Thatcher, David Dastmalchian, Madison Hu.",
        "sinopsis": "BOOGEYMAN: TU MIEDO ES REAL es un clasico del cine de terror al estilo de Poltergeist, que asusta y muestra un costado mas humano en igual medida, dice su director, Rob Savage. Recuerdo vividamente el terror que senti al leer el cuento corto de King cuando era ninio, y es esta sensacion de miedo infantil lo que queria inspirarle a las audiencias de todo el mundo. Esta pelicula se realizo en colaboracion con un equipo de creativos increiblemente talentosos y esta anclada en las maravillosas y conmovedoras intepretaciones de nuestro extraordinario elenco que me ha asombrado, de verdad. Estamos orgullosos de esta pelicula y estamos ansiosos por darles a todos una razon para temer a la oscuridad nuevamente el 1 de junio.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2655_img2.jpg",
        "comentario": "",
        "puntuacion": "5"
    }
]
direccion = {
    "Rob Marshall": [
        {
            "titulo": "Piratas del Caribe: Navegando por Aguas Misteriosas",
            "anio": "2011"
        },
        {
            "titulo": "En El Bosque",
            "anio": "2014"
        },
        {
            "titulo": "El Regreso de Mary Popins",
            "anio": "2018"
        }
    ],
    "Louis Leterrier": [
        {
            "titulo": "El Increible Hulk",
            "anio": "2008"
        },
        {
            "titulo": "Furia de Titanes",
            "anio": "2010"
        }
    ],
    "James Gunn": [
        {
            "titulo": "Guardianes de la Galaxia",
            "anio": "2014"
        },
        {
            "titulo": "Guardianes de la Galaxia 2",
            "anio": "2017"
        },
        {
            "titulo": "The Suicide Squad",
            "anio": "2021"
        }
    ],
    "Martino Zaidelis": [
        {
            "titulo": "Re Loca",
            "anio": "2018"
        }
    ],
    "Aaron Horvath": [
        {
            "titulo": "Teen Titans Go",
            "anio": "2018"
        }
    ],
    "Steven Caple Jr.": [
        {
            "titulo": "Creed II",
            "anio": "2018"
        }
    ],
    "Andy Muschietti": [
        {
            "titulo": "Mama",
            "anio": "2013"
        },
        {
            "titulo": "IT",
            "anio": "2017"
        },
        {
            "titulo": "IT Capitulo Dos",
            "anio": "2019"
        }
    ],
    "Peter Sohn": [
        {
            "titulo": "El Buen Dinosaurio",
            "anio": "2015"
        }
    ]
}
posters = [
    {
        "titulo": "La Sirenita",
        "link": "https://www.cinemacenter.com.ar/img_movies/2627_img2.jpg"
    },
    {
        "titulo": "Rapidos y Furiosos X",
        "link": "https://www.cinemacenter.com.ar/img_movies/2672_img2.jpg"
    },
    {
        "titulo": "Guardianes de la Galaxia 3",
        "link": "https://www.cinemacenter.com.ar/img_movies/2637_img2.jpg"
    },
    {
        "titulo": "La Extorsion",
        "link": "https://www.cinemacenter.com.ar/img_movies/2645_img2.jpg"
    },
    {
        "titulo": "Super Mario Bros",
        "link": "https://www.cinemacenter.com.ar/img_movies/2561_img2.jpg"
    },
    {
        "titulo": "Spiderman: Across the Spiderverse",
        "link": "https://www.cinemacenter.com.ar/img_movies/2615_img2.jpg"
    },
    {
        "titulo": "Transformers: El Despertar de las Bestias", 
        "link": "https://www.cinemacenter.com.ar/img_movies/2607_img2.jpg"
    },
    {
        "titulo": "The Flash",
        "link": "https://www.cinemacenter.com.ar/img_movies/2646_img2.jpg"
    },
    {
        "titulo": "Elemental",
        "link": "https://www.cinemacenter.com.ar/img_movies/2626_img2.jpg"
    },
    {
        "titulo": "Boogeyman: Tu Miedo Es Real",
        "link": "https://www.cinemacenter.com.ar/img_movies/2655_img2.jpg"
    }
]
ABM_peliculas = [
    {
        "titulo": "La Sirenita",
        "ABM": "Bajo" 
    },
    {
        "titulo": "Rapidos y Furiosos X",
        "ABM": "Modificable" 
    },
    {
        "titulo": "Guardianes de la Galaxia 3",
        "ABM": "Alto" 
    },
    {
        "titulo": "La Extorsion",
        "ABM": "Bajo" 
    },
    {
        "titulo": "Super Mario Bros",
        "ABM": "Modificable" 
    },
    {
        "titulo": "Spiderman: Across the Spiderverse",
        "ABM": "Alto"
    },
    {
        "titulo": "Transformers: El Despertar de las Bestias",
        "ABM": "Modificable" 
    },
    {
        "titulo": "The Flash",
        "ABM": "Alto" 
    },
    {
        "titulo": "Elemental",
        "ABM": "Bajo" 
    },
    {
        "titulo": "Boogeyman: Tu Miedo Es Real",
        "ABM": "Bajo"
    }
]
ABM_directores = [
    {
        "director": "Rob Marshall",
        "ABM": "Bajo" 
    },
    {
        "director": "Louis Leterrier",
        "ABM": "Bajo" 
    },
    {
        "director": "James Gunn",
        "ABM": "Alto" 
    },
    {
        "director": "Martino Zaidelis",
        "ABM": "Modificable" 
    },
    {
        "director": "Aaron Horvath",
        "ABM": "Modificable" 
    },
    {
        "director": "Steven Caple Jr.",
        "ABM": "Modificable" 
    },
    {
        "director": "Andy Muschietti",
        "ABM": "Alto" 
    },
    {
        "director": "Peter Sohn",
        "ABM": "Modificable" 
    }
]
ABM_generos = [
    {
        "genero": "ciencia ficcion", 
        "ABM": "Alto" 
    },
    {
        "genero": "accion",
        "ABM": "Modificable" 
    },
    {
        "genero": "aventuras",
        "ABM": "Modificable" 
    },
    {
        "genero": "terror",
        "ABM": "Modificable" 
    },
    {
        "genero": "animacion",
        "ABM": "Bajo" 
    },
    {
        "genero": "drama",
        "ABM": "Modificable" 
    }
]
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
ABM_usuarios = [
    {
        "usuario": "Coco814151",
        "ABM": "Alto" 
    },
    {
        "usuario": "negrito55fotos",
        "ABM": "Alto" 
    },
    {
        "usuario": "mymartin",
        "ABM": "Modificable" 
    }
]
def usuario():
    if "user" in session:
        nombre = session["user"]
    else:
        nombre = ""
    return nombre
@app.route("/")
def index():
    contador = 0
    num_pagina = request.args.get("pagina", 1, type=int)
    por_pagina = 10
    inicio_indice = (num_pagina - 1) * por_pagina
    fin_indice = inicio_indice + por_pagina
    peliculas2 = list(pelis)
    if len(peliculas2) > 1:
        peliculas2.reverse()
    peliculas3 = peliculas2[inicio_indice:fin_indice]
    total_peliculas = len(pelis)
    total_paginas = math.ceil(total_peliculas/por_pagina)
    session["contador"] = session.get("contador", 0) + 1
    contador = session["contador"]
    return render_template("index.html", nombre = usuario(), peliculas = peliculas3, visitas = contador, total_peliculas = total_peliculas, total_paginas = total_paginas, pagina_recurrente = num_pagina)
@app.route("/ingreso")
def ingreso():
    return render_template("login.html", nombre = usuario())
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        for usuario in usuarios:
            if usuario["usuario"] == username and usuario["contrasenia"] == password:
                session["user"] = usuario["usuario"]
                return redirect(url_for("index"))
        return incorrecto()
@app.route("/peliculas")
def peliculas():
    return render_template("peliculas.html", nombre = usuario(), peliculas = pelis)
@app.route("/peliculas/<director>", methods = ["GET", "POST"])
def pelis_direccion(director):
    peliculas = []
    if request.method == "POST":
        for pelicula in pelis:
            if pelicula["director"] == director:
                peliculas.append(pelicula)
    return render_template("pelis_direccion.html", nombre = usuario(), peliculas = pelis, director = director)
@app.route("/imagenes")
def imagenes():
    num_pagina = request.args.get("pagina", 1, type=int)
    por_pagina = 10
    inicio_indice = (num_pagina - 1) * por_pagina
    fin_indice = inicio_indice + por_pagina
    peliculas = pelis[inicio_indice:fin_indice]
    total_peliculas = len(pelis)
    total_paginas = math.ceil(total_peliculas/por_pagina)
    return render_template("imagenes.html", nombre = usuario(), peliculas = peliculas, total_peliculas = total_peliculas, total_paginas = total_paginas, pagina_recurrente = num_pagina)
@app.route("/confirmacion_peliculas", methods=["GET", "POST"])
def confirmacion_peliculas():
    if request.method == "POST":
        titulo = request.form.get("Titulo")
        titulo = titulo.title()
        lista = []
        for pelicula in pelis:
            if titulo == pelicula["titulo"]:
                lista.append(pelicula["titulo"])
        if lista != "":
            titulo = ""
            for i in lista:
                titulo = i + titulo
            return redirect(url_for("buscador_peliculas", Titulo = titulo))
        return noEncontrado()
@app.route("/buscador_peliculas")
def buscador_peliculas():
    titulo1 = request.args.get("Titulo")
    if titulo1 == None:
        titulo1 = ""
    return render_template("buscador_peliculas.html", nombre = usuario(), peliculas = pelis, titulo1 = titulo1)
@app.route("/confirmacion_directores", methods=["GET", "POST"])
def confirmacion_directores():
    if request.method == "POST":
        directores = request.form.get("Directores")
        lista = []
        for pelicula in pelis:
            if directores in pelicula["director"]:
                lista.append(pelicula["director"])
        if lista != "":
            director = ","
            for i in lista:
                director = i + director
            return redirect(url_for("buscador_directores", Director = director))
        return noEncontrado()
@app.route("/buscador_directores")
def buscador_directores():
    director1 = request.args.get("Director")
    if director1 == None:
        director1 = ""
    return render_template("buscador_directores.html", nombre = usuario(), peliculas = pelis, director1 = director1)
@app.route("/confirmacion_actores", methods=["GET", "POST"])
def confirmacion_actores():
    if request.method == "POST":
        actores = request.form.get("Actores")
        lista = []
        for pelicula in pelis:
            if actores in pelicula["actores"]:
                lista.append(pelicula["actores"])
        if lista != "":
            actor = ","
            for i in lista:
                actor = i + actor
            return redirect(url_for("buscador_actores", Actor = actor))
        return noEncontrado()
@app.route("/buscador_actores")
def buscador_actores():
    actor1 = request.args.get("Actor")
    if actor1 == None:
        actor1 = ""
    return render_template("buscador_actores.html", nombre = usuario(), peliculas = pelis, actor1 = actor1)
@app.route("/agregacion", methods=["GET", "POST"])
def agregacion():
    lista_directores = []
    for i in pelis:
        if i["director"] not in lista_directores:
            lista_directores.append(i["director"])
    lista_generos = []
    for i in pelis:
        if i["genero"] not in lista_generos:
            lista_generos.append(i["genero"])
    if "user" not in session:
        return redirect(url_for("index"))
    if request.method == "POST":
        titulo = request.form["Titulo"]
        director1 = request.form["Director"]
        anio = request.form["Anio"]
        genero1 = request.form["Genero"]
        actores = request.form["Actores"]
        sinopsis = request.form["Sinopsis"]
        link = request.form["Link"]
        comentario = request.form["Comentario"]
        puntuacion = request.form["Puntuacion"]
        pelicula = {
            "titulo": titulo,
            "director": director1,
            "anio": anio,
            "genero": genero1,
            "actores": actores,
            "sinopsis": sinopsis,
            "link": link,
            "comentario": comentario,
            "puntuacion": puntuacion
        }
        pelis.append(pelicula)
        return redirect(url_for("peliculas"))
    return render_template("agregacion.html", nombre = usuario(), directores = lista_directores, generos = lista_generos)
@app.route("/edicion/<pelicula>", methods = ["GET", "POST"])
def edicion(pelicula):
    lista_directores = []
    for i in pelis:
        if i["director"] not in lista_directores:
            lista_directores.append(i["director"])
    lista_generos = []
    for i in pelis:
        if i["genero"] not in lista_generos:
            lista_generos.append(i["genero"])
    if "user" not in session:
        return redirect(url_for("index"))
    if request.method == "POST":
        for peli in pelis:
            if peli["titulo"] == pelicula:
                if request.form.get("Titulo") != "":
                    peli["titulo"] = request.form.get("Titulo")
                if request.form.get("Director") != "":
                    peli["director"] = request.form.get("Director")
                if request.form.get("Anio") != "":
                    peli["anio"] = request.form.get("Anio")
                if request.form.get("Genero") != "":
                    peli["genero"] = request.form.get("Genero")
                if request.form.get("Actores") != "":
                    peli["actores"] = request.form.get("Actores")
                if request.form.get("Sinopsis") != "":
                    peli["sinopsis"] = request.form.get("Sinopsis")
                if request.form.get("Link") != "":
                    peli["link"] = request.form.get("Link")
                if request.form.get("Cometario") != "":
                    opinion = request.form.get("Comentario")
                    comentario = peli["comentario"]
                    if type(opinion) == str:
                        comentario = comentario.split(",")
                    user = ",usuario"
                    nombre = usuario()
                    user = user + nombre
                    user = user + ":"
                    comentario.append(usuario)
                    comentario.append(opinion)
                    peli["comentario"] = comentario
                if request.form.get('Puntuacion') != '':
                    peli["puntuacion"] = request.form.get("Puntuacion")
        return redirect(url_for("peliculas"))
    return render_template("edicion.html", nombre = usuario(), pelicula = pelicula, directores = lista_directores, generos = lista_generos)
@app.route("/eliminacion/<pelicula>", methods=["GET", "POST"])
def eliminacion(pelicula):
    if "user" not in session:
        return redirect(url_for("index"))
    if request.method == "POST":
        for datos in pelis:
            if datos["titulo"] == pelicula:
                pelis.remove(datos)
        return redirect(url_for("peliculas"))
    return render_template("eliminacion.html", nombre = usuario(), pelicula = pelicula)
@app.route("/modificacion_director", methods=["GET", "POST"])
def modificacion_director():
    lista = []
    for i in pelis:
        if i["director"] not in lista:
            lista.append(i["director"])
    if "user" not in session:
        return redirect(url_for("index"))
    if request.method == "POST":
        for datos in pelis:
            if request.form["Director"] == datos["director"]:
                datos["director"] = request.form["nuevo_director"]
        return redirect(url_for("peliculas"))
    return render_template("modificacion_director.html", nombre=usuario(), peliculas = lista)
@app.route("/modificacion_genero", methods=["GET", "POST"])
def modificacion_genero():
    lista = []
    for i in pelis:
        if i["genero"] not in lista:
            lista.append(i["genero"])
    if "user" not in session:
        return redirect(url_for("index"))
    if request.method == "POST":
        for datos in pelis:
            if request.form["Genero"] == datos["genero"]:
                datos["genero"] = request.form["nuevo_genero"]
        return redirect(url_for("peliculas"))
    return render_template("modificacion_genero.html", nombre=usuario(), peliculas = lista)
@app.route("/directores")
def directores():
    lista = []
    for i in pelis:
        if i["director"] not in lista:
            lista.append(i["director"])
    return render_template("directores.html", nombre = usuario(), peliculas = lista)
@app.route("/generos")
def generos():
    lista = []
    for i in pelis:
        if i["genero"] not in lista:
            lista.append(i["genero"])
    return render_template("generos.html", nombre = usuario(), peliculas = lista)
@app.route("/direccion")
def devolucion_direccion():
    return jsonify(direccion)
@app.route("/posters")
def devolucion_posters():
    return jsonify(posters)
@app.route("/ABM_peliculas")
def devolucion_ABM_peliculas():
    return jsonify(ABM_peliculas)
@app.route("/ABM_directores")
def devolucion_ABM_directores():
    return jsonify(ABM_directores)
@app.route("/ABM_generos")
def devolucion_ABM_generos():
    return jsonify(ABM_generos)
@app.route("/usuarios")
def devolucion_usuarios():
    return jsonify(usuarios)
@app.route("/ABM_usuarios")
def devolucion_ABM_usuarios():
    return jsonify(ABM_usuarios)
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("ingreso"))
@app.errorhandler(400)
def incorrecto():
    return render_template("400.html"), 400
@app.errorhandler(404)
def noEncontrado():
    return render_template("404.html"), 404
@app.errorhandler(501)
def yaExistente():
    return render_template("501.html"), 501
if __name__ == "__main__":
    app.run(debug=True)
