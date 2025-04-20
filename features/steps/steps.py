from behave import given, when, then
import re

# Función para convertir palabras numéricas a números
def convertir_palabra_a_numero(palabra):
    try:
        return int(palabra)
    except ValueError:
        numeros = {
            "cero": 0, "un": 1, "uno": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
            "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
            "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
            "diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinte": 20,
            "treinta": 30, "cuarenta": 40, "cincuenta": 50, "sesenta": 60, "setenta": 70,
            "ochenta": 80, "noventa": 90, "media": 0.5
        }
        return numeros.get(palabra.lower(), 0)

@given('que he comido {cukes} pepinos')
def step_given_eaten_cukes(context, cukes):

    try:
        # Intentar convertir la cadena a un número decimal
        try:
            cukes_float = float (cukes) # Todo se considera como un número decimal (incluso si es entero)
        except ValueError:
            raise ValueError(f"Se esperaba un número válido, pero se obtuvo: {cukes}") # Si ocurre este error, se salta al except externo
        
        # Verificar si el número es negativo
        if cukes_float < 0:
            raise ValueError(f"Se esperaba un número positivo, pero se obtuvo: {cukes}")
        context.belly.comer (cukes_float)
        context.error = None
    except Exception as e:
        context.error = e

@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    time_description = time_description.strip('"').lower()
    time_description = time_description.replace('y', ' ')
    time_description = time_description.strip()

    if time_description == 'media hora':
        total_time_in_hours = 0.5
    else:
        pattern = re.compile(r'(?:(\w+)\s*horas?)?\s*(media)?\s*(?:(\w+)\s*minutos?)?\s*(?:(\w+)\s*segundos?)?') #
        match = pattern.match(time_description)

        if match:
            hours_word = match.group(1) or "0"
            half_hour_word = match.group(2) or "0" #
            minutes_word = match.group(3) or "0"
            seconds_word = match.group(4) or "0" #

            hours = convertir_palabra_a_numero(hours_word)
            if half_hour_word == "media":
                hours += 0.5
            minutes = convertir_palabra_a_numero(minutes_word)
            seconds_word = convertir_palabra_a_numero(seconds_word) #

            total_time_in_hours = hours + (minutes / 60) + (seconds_word / 3600) #
        else:
            raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")

    context.belly.esperar(total_time_in_hours)

@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."

@then('debería recibir un error con el mensaje "{mensaje_error}"')
def step_then_should_receive_error(context, mensaje_error):
    if context.error:
        # Verificar que el mensaje del error coincida con el esperado
        assert str(context.error) == mensaje_error, f"Se esperaba el mensaje de error '{mensaje_error}', pero se obtuvo '{str(context.error)}'."
    else:
        # Si no hay error, fallar la prueba
        assert False, "Se esperaba un error, pero no se obtuvo ninguno."