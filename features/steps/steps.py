from behave import given, when, then
import re
import random
import logging

# Configuración del logger
logging.basicConfig(filename="features/steps/steps.log", level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger("steps")


# Función para convertir palabras numéricas a números
def convertir_palabra_a_numero(palabra):
    try:
        return float(palabra)
    except ValueError:
        numeros = {
            "cero": 0, "un": 1, "uno": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
            "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
            "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
            "diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinte": 20,
            "treinta": 30, "cuarenta": 40, "cincuenta": 50, "sesenta": 60, "setenta": 70,
            "ochenta": 80, "noventa": 90, "media": 0.5, "one":1, "two":2, "three":3, "four":4, "five":5,
            "six":6, "seven":7, "eight":8, "nine":9, "ten":10, "eleven":11, "twelve":12,
            "thirteen":13, "fourteen":14, "fifteen":15, "sixteen":16, "seventeen":17, "eighteen":18,
            "nineteen":19, "twenty":20, "thirty":30, "forty":40, "fifty":50, "sixty":60, "seventy":70,
            "eighty":80, "ninety":90, "half an hour":0.5
        }
        return numeros.get(palabra.lower(), 0)

# Función para formatear el tiempo en un formato legible
def format_time(time_description):
    new_time = time_description.strip('"').lower()
    new_time = new_time.replace(' y ', ' ') 
    new_time = new_time.replace(' and ', ' ') 
    new_time = new_time.replace(' a ', ' ') 
    new_time = new_time.replace(', ', ' ') 
    new_time = new_time.strip()
    return new_time

@given('que he comido {cukes} pepinos')
def step_given_eaten_cukes(context, cukes):
    try:
        # Intentar convertir la cadena a un número decimal
        try:
            cukes_float = float (cukes) # Todo se considera como un número decimal (incluso si es entero)
        except ValueError:
            raise ValueError(f"Se esperaba una cadena numérica, pero se obtuvo: {cukes}") # Si ocurre este error, se salta al except externo
        
        # Verificar si el número es válido
        if cukes_float < 0.0 or cukes_float > 10000.0:
            raise ValueError(f"Se esperaba un número válido (entre 0 y 10000), pero se obtuvo: {cukes}")
        context.belly.comer (cukes_float)
        context.error = None
    except Exception as e:
        context.error = e

@when('espero un tiempo aleatorio entre {min_time} y {max_time}')
def step_when_wait_random_interval_time(context, min_time, max_time):
    random.seed(40) # Semilla para que las pruebas no sean indeterministas

    # Función para convertir una descripción de tiempo a horas
    def convertir_a_horas(time_description):
        try: 
            pattern = re.compile(r'(?:(-?\w+(?:\.\w+)?)\s*(?:hour|hora)?s?)?\s*(?:(-?\w+(?:\.\w+)?)\s*(?:minute|minuto)?s?)?\s*(?:(-?\w+(?:\.\w+)?)\s*(?:second|segundo)?s?)?')
            
            time_description = format_time(time_description) # Formatear la descripción del tiempo

            match = pattern.match(time_description)
            if not match:
                raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")

            hours_word = match.group(1) or "0"
            minutes_word = match.group(2) or "0"
            seconds_word = match.group(3) or "0"

            hours = convertir_palabra_a_numero(hours_word)
            minutes = convertir_palabra_a_numero(minutes_word)
            seconds = convertir_palabra_a_numero(seconds_word)
            
            # Convertir todo a horas
            return hours + (minutes / 60) + (seconds / 3600)
        except Exception as e:
            raise e

    # Convertir los tiempos mínimo y máximo a horas (se asume que primero va el mínimo y luego el máximo)
    try:
        min_time_in_hours = convertir_a_horas(min_time)
        max_time_in_hours = convertir_a_horas(max_time)

        if min_time_in_hours < 0 or max_time_in_hours < 0:
            raise ValueError("Los tiempos no pueden ser negativos.")
        if min_time_in_hours > max_time_in_hours:
            raise ValueError("El tiempo mínimo no puede ser mayor que el tiempo máximo.")

        random_hours = random.uniform(min_time_in_hours, max_time_in_hours)
        logger.info(f"Se generó un tiempo aleatorio de {random_hours} horas.")
        context.belly.esperar(random_hours)
        context.error = None

    except Exception as e:
        context.error = e
        logger.error(f"Error capturado: {str(context.error)}")


@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):   
    try: 
        time_description = format_time(time_description) # Formatear la descripción del tiempo
        logger.info(f"{time_description}")

        if time_description == 'media hora' or time_description == 'half an hour':
            total_time_in_hours = 0.5
        else:
            pattern = re.compile(r'(?:(-?\w+(?:\.\w+)?)\s*(?:hours?|horas?))?\s*(media|half)?\s*(?:(-?\w+(?:\.\w+)?)\s*(?:minutes?|minutos?))?\s*(?:(-?\w+(?:\.\w+)?)\s*(?:seconds?|segundos?))?') # Solo se aceptaran half an hour (ya está arriba) y "n" hours and a half
            match = pattern.match(time_description)

            if match:
                hours_word = match.group(1) or "0"
                logger.info(f"{hours_word}")
                half_hour_word = match.group(2) or "0"
                minutes_word = match.group(3) or "0"
                seconds_word = match.group(4) or "0" 

                hours = convertir_palabra_a_numero(hours_word)
                logger.info(f"{hours}")
                if half_hour_word in ["media", "half"]:
                    hours += 0.5
                minutes = convertir_palabra_a_numero(minutes_word)
                seconds = convertir_palabra_a_numero(seconds_word) 

                if hours < 0 or minutes < 0 or seconds < 0:
                    raise ValueError("Los tiempos no pueden ser negativos.")

                total_time_in_hours = hours + (minutes / 60) + (seconds / 3600) #
            else:
                raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")

        context.belly.esperar(total_time_in_hours)
        context.error = None

    except Exception as e:
        context.error = e


@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."

@then('debería recibir un error con el mensaje "{error_message}"')
def step_then_should_receive_error(context, error_message):
    # Este paso no debería ejecutarse si el error fue lanzado correctamente
    if context.error is None:
        raise AssertionError("El sistema no lanzó el error esperado.")
    else:
        assert str(context.error) == error_message, f"Se esperaba el error: {error_message}, pero se obtuvo: {str(context.error)}"

@then('debería haber comido {cukes} pepinos')
def step_then_eaten_cukes (context, cukes):
    assert float(context.belly.pepinos_comidos) == float(cukes)