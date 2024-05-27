from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# leer el archivo de datos
archivoClubs = open("data/datos_clubs.txt", "r")
archivoJugadores = open("data/datos_jugadores.txt", "r")

# obtener las lineas del archivo
dataClubs = archivoClubs.readlines()
dataJugadores = archivoJugadores.readlines()

# cerrar archivo
archivoClubs.close
archivoJugadores.close

# se crea un objetos de tipo Club 
for c in dataClubs:
    nombreC, deporteC, fundacionC = c.strip().split(';')
    club = Club(nombre=nombreC, deporte=deporteC, fundacion=fundacionC)
    # se agregan los objetos a la sesion
    session.add(club)


# Se crean objeto de tipo Jugador
for j in dataJugadores:
    clubString, posicionJ, dorsalJ, nombreJ = j.strip().split(';')
    # para obtener el objeto tipo club y no el string
    club = session.query(Club).filter_by(nombre=clubString).one()

    jugador = Jugador(nombre=nombreJ, dorsal=dorsalJ, posicion=posicionJ, club=club)
    # se agregan los objetos a la sesion
    session.add(jugador)

# se confirma las transacciones
session.commit()
