# Paradoja de Monty Hall

Estos son scripts que simulan la paradoja de **Monty Hall**.

El problema de Monty Hall es un problema matemático de probabilidad basado en el
concurso televisivo estadounidense Trato hecho (Let's Make a Deal). El problema
fue bautizado con el nombre del presentador de dicho concurso: Monty Hall.

El concursante debe elegir una puerta entre tres (todas cerradas); el premio
consiste en llevarse lo que se encuentra detrás de la elegida. Se sabe con certeza
que tras una de ellas se oculta un automóvil, y tras las otras dos hay cabras. Una
vez que el concursante haya elegido una puerta y comunicado su elección a los
presentes, el presentador, que sabe lo que hay detrás de cada puerta, abrirá una de
las otras dos en la que haya una cabra. A continuación, le da la opción al concursante
de cambiar, si lo desea, de puerta (tiene dos opciones). ¿Debe el concursante mantener
su elección original o escoger la otra puerta? ¿Hay alguna diferencia?

Esa pregunta generó un intenso debate. Como la respuesta correcta parece contradecir la
intuición, es aparentemente una paradoja.

*["Tomado de Wikipedia".](https://es.wikipedia.org/wiki/Problema_de_Monty_Hall)*

## Modo de uso

Las simulaciones se realizaron en los lenguajes **Python** y **Dart**, básicamente son el
mismo programa hecho con ambos lenguajes. Para poder usarlo y obtener los resultados deseados
solo debe cambiar el valor de la variable **decision** de la siguiente manera:

* Si desea que se tome una desición **random** (cambiar o no cambiar de puerta)
  "descomente" la línea de código `decision = desea_cambiar()` en Python o
  `String decision = deseaCambiar(decisiones);` en Dart y comente la siguiente
  línea.
* Si desea que la desición siempre sea "si" mantenga la linea `decision = "si"` en Python
  o `String decision = "si";` en Dart tal como está.
* Si desea que la decisión siempre sea "no", cambia dicha línea por ese valor.

Diviértete haciendo las pruebas o modificando el código. :D