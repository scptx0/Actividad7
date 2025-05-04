# language: es

Característica: Comportamiento del Estómago
  @spanish
  Escenario: Comer muchos pepinos y gruñir
    Dado que he comido 42 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  @spanish
  Escenario: Comer pocos pepinos y no gruñir
    Dado que he comido 10 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  @spanish
  Escenario: Comer muchos pepinos y esperar menos de una hora
    Dado que he comido 50 pepinos
    Cuando espero media hora
    Entonces mi estómago no debería gruñir

  @spanish
  Escenario: Comer pepinos y esperar en minutos
    Dado que he comido 30 pepinos
    Cuando espero 90 minutos
    Entonces mi estómago debería gruñir

  @spanish
  Escenario: Comer pepinos y esperar en diferentes formatos
    Dado que he comido 25 pepinos
    Cuando espero "dos horas y treinta minutos"
    Entonces mi estómago debería gruñir

  @spanish
  Escenario: Comer pepinos y esperar en minutos y segundos
    Dado que he comido 35 pepinos
    Cuando espero "1 hora y 30 minutos y 45 segundos"
    Entonces mi estómago debería gruñir

  @spanish
  Escenario: Comer una cantidad fraccionaria de pepinos
    Dado que he comido 0.5 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  @spanish
  Escenario: Comer una cantidad negativa de pepinos
    Dado que he comido -4 pepinos
    Entonces debería recibir un error con el mensaje "Se esperaba un número válido (entre 0 y 10000), pero se obtuvo: -4"

  @spanish
  Escenario: Comer una cantidad inválida de pepinos
    Dado que he comido hola pepinos 
    Entonces debería recibir un error con el mensaje "Se esperaba una cadena numérica, pero se obtuvo: hola"

  @spanish
  Escenario: Comer una cantidad negativa decimal de pepinos
    Dado que he comido -2.5 pepinos
    Entonces debería recibir un error con el mensaje "Se esperaba un número válido (entre 0 y 10000), pero se obtuvo: -2.5"

  @spanish
  Escenario: Comer pepinos y esperar un tiempo aleatorio
    Dado que he comido 25 pepinos
    Cuando espero un tiempo aleatorio entre 1 y 3 horas
    Entonces mi estómago debería gruñir

  @spanish
  Escenario: Comer una cantidad muy grande de pepinos
    Dado que he comido 101 pepinos
    Cuando espero 5 horas
    Entonces mi estómago debería gruñir

  @spanish
  Escenario: Comer 1000 pepinos y esperar 10 horas
    Dado que he comido 1000 pepinos
    Cuando espero 10 horas
    Entonces mi estómago debería gruñir

  @spanish
  Escenario: Manejar tiempos complejos
    Dado que he comido 50 pepinos
    Cuando espero "1 hora, 30 minutos y 45 segundos"
    Entonces mi estómago debería gruñir

  @spanish
  Escenario: Manejar tiempos complejos
    Dado que he comido 30 pepinos
    Cuando espero "4 horas     5 minutos"
    Entonces mi estómago debería gruñir

  @spanish
  Escenario: Manejar tiempos complejos
    Dado que he comido 5 pepinos
    Cuando espero "     2 minutos y 5 segundos"
    Entonces mi estómago no debería gruñir

  @spanish
  Escenario: Comer pepinos y esperar un tiempo aleatorio (intervalo inválido)
    Dado que he comido 5 pepinos
    Cuando espero un tiempo aleatorio entre -1 y 4 horas
    Entonces debería recibir un error con el mensaje "Los tiempos no pueden ser negativos."

  @spanish
  Escenario: Comer pepinos y esperar un tiempo aleatorio (intervalo inválido)
    Dado que he comido 5 pepinos
    Cuando espero un tiempo aleatorio entre 6 y 4 horas
    Entonces debería recibir un error con el mensaje "El tiempo mínimo no puede ser mayor que el tiempo máximo."
  
  @spanish
  Escenario: Comer pepinos y esperar un tiempo inválido
    Dado que he comido 5 pepinos
    Cuando espero -5 horas
    Entonces debería recibir un error con el mensaje "Los tiempos no pueden ser negativos."

  @english
  Escenario: Esperar usando horas en inglés
    Dado que he comido 20 pepinos
    Cuando espero "two hours and thirty minutes"
    Entonces mi estómago debería gruñir

  @english
  Escenario: Comer pepinos y esperar en minutos y segundos en ingles
    Dado que he comido 35 pepinos
    Cuando espero "1 hour 30 minutes and 45 seconds"
    Entonces mi estómago debería gruñir

  @english
  Escenario: Comer pepinos y esperar media hora en inglés
    Dado que he comido 35 pepinos
    Cuando espero "half an hour"
    Entonces mi estómago no debería gruñir

  @english
  Escenario: Comer pepinos y esperar 1 hora y media en inglés
    Dado que he comido 2 pepinos
    Cuando espero "one hour and a half"
    Entonces mi estómago no debería gruñir

  @ejercicio8
  Escenario: Comer muchos pepinos y esperar el tiempo suficiente
    Dado que he comido 15 pepinos 
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  @ejercicio9 
  Escenario: Comer suficientes pepinos y esperar el tiempo adecuado
    # Issue relacionado: https://github.com/scptx0/Actividad7/issues/1
    Dado que he comido 20 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  @ejercicio9
  Escenario: Comer pocos pepinos y no esperar suficiente tiempo
    # Issue relacionado: https://github.com/scptx0/Actividad7/issues/1
    Dado que he comido 5 pepinos
    Cuando espero 1 hora
    Entonces mi estómago no debería gruñir

  @ejercicio10
  Escenario: Saber cuántos pepinos he comido
    Dado que he comido 15 pepinos
    Entonces debería haber comido 15 pepinos