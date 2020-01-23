from __future__ import print_function

import sys
from operator import add

from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext


def loadFile(filename):
    return spark.read.load("data\\" + filename,
                           format="csv", sep=" ", inferSchema="false")


def joinFiles(file_1, file_2):
    return file_1.union(file_2)


def adjustData(self, parameter_list):
    pass


def defineSparkCongif():
    conf = SparkConf().setMaster("local")
    sc = SparkContext(conf=conf)


def defineSparkSession() -> SparkSession:
    return SparkSession\
        .builder\
        .appName("spark-test-semantix")\
        .getOrCreate()


if __name__ == "__main__":
    defineSparkCongif()
    spark = defineSparkSession()

    dataAug = loadFile('access_log_Aug95')
    dataJul = loadFile('access_log_Jul95')
    df = joinFiles(dataAug, dataJul)

    spark.stop()
