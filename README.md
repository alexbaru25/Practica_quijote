# Practica_quijote
Este proyecto contiene dos funciones: una función que selecciona aleatoriamente líneas de un archivo y las escribe en otro archivo de salida, y una función que cuenta el número total de palabras en un archivo utilizando PySpark.
Función porcentaje

La función porcentaje es una función Python que toma tres argumentos: el nombre del archivo de entrada, el nombre del archivo de salida y un número de ratio. La función abre el archivo de entrada, selecciona aleatoriamente líneas según el ratio proporcionado y las escribe en el archivo de salida. El objetivo de esta función es obtener un subconjunto aleatorio de las líneas del archivo de entrada.
La función 04_word_count_map.py es una función PySpark que cuenta el número total de palabras en un archivo. La función utiliza SparkContext para crear un RDD a partir del archivo de entrada y luego utiliza la función map para contar el número de palabras en cada línea. El resultado es una lista con el número de palabras en cada línea, y la función muestra la suma total de palabras en el archivo.

Por otra parte, los archivos .txt salvo quijote.txt son los resultados el ejecutar las funciones mencionadas anteriormente.
