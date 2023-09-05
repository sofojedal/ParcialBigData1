import datetime
from descargaHtml import descargahtml
from crearCsv import descargacsv


def obtenerFecha():
    
    fecha_actual = datetime.datetime.now()

    day = fecha_actual.day
    month = fecha_actual.strftime('%B').lower()
    year = fecha_actual.year

    return day, month, year


def contar_lineas(contenido):
    
    lineas = contenido.split('\n')
    return len(lineas)


def test_answer_1():
    
    contenido_html = descargahtml()
    
    # cadena1 = "martes, septiembre 05, 2023"
    # cadena2 = "05 de septiembre de 2023"
    day, month, year = obtenerFecha()
    
    # eltiempo
    cadena1 = "{} {}, {}".format(month, day, year)
    # publimetro
    cadena2 = "{} de {} de {}".format(day, month, year)
    
    assert cadena1 in contenido_html or cadena2 in contenido_html, "Ninguna de las cadenas se encontró en el contenido HTML"


def test_answer_2():
    
    contenido_csv = descargacsv()
    
    num_lineas_1 = contar_lineas(contenido_csv[0])
    num_lineas_2 = contar_lineas(contenido_csv[1])
    
    assert num_lineas_1 > 2 and num_lineas_2 > 2, "Los CSV tiene menos de tres líneas"
