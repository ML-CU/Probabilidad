# PROBABILIDAD - SIMULACIÓN PARA HALLAR EL "VALOR ESPERADO" - JUEGO DE LOS DADOS
# Diana y Jason juegan a los dados, si cae 6 o 7 Diana le paga a Jason 9 dolares, si cae 9 o 10 Jason le paga a Diana 9 pesos ¿Quién gana y quién pierde? ¿Cuanto gana o pierde Diana, o cuanto gana o pierde Jason?

# ¿Que es el valor esperado?
## cuanto vamos a optener en promedio en cada realización del experimento, en este caso nos damos cuenta de que el promedio se determina que por mas de que Diana quiera ganar, siempre va a peder, en promedio va a pagar mucho dinero Jason, esto es logico porque los numeros que salen mas en los dados es 6 y 7. 
## 

# JUEGO DEL DADO
## Respecto al juego del lanzamiento de un dado, tenemos el objetivo de realizar x simulaciones y detenerminar el valor esperado, para esto sumamos los valores obtenidos en cada lanzamiento y lo dividimos entre el numero de lanzamientos. Aqui podemos ver que el valor esperado no es un valor del dado (1,2,3,4,5 o 6), sino que nos da por ejemplo un numero decimal 3.9, esto no nos dice que al final vamos a tener el valor de 3.9, esto nos permite ver una distribución normal del comportamiento de los datos, podemos decir si realizamos una apuesta y si elegimos obtener 4,5 o 6 en 10 lanzamientos, no vamos a ganar mucho dinero, solo un poco, por que en los lanzamientos el comportamiento del dado en promedio es 3.9. En cambio si jugamos todo el dia (10000 lanzamientos) la tendencia(promedio) del valor esperado va hacia 3.5