# -*- coding: utf-8 -*-

from pyspark import SparkContext
import sys


def main(filename):
    with SparkContext() as sc:
        sc.setLogLevel("ERROR")
        dato = sc.textFile(filename)
        palabras_rdd = dato.map(lambda x: len(x.split()))
        print (palabras_rdd.collect())
        print ('Resultados------------------')
        print ('conteo de palabras', palabras_rdd.sum())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 {0} <file>".format(sys.argv[0]))
    else:
        main(sys.argv[1])
