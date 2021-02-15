import pyspark as ps
from pyspark import SparkContext, SparkConf

#conf = SparkConf().setAppName("SANSA TESTING")
#sc = SparkContext(conf = conf)

conf = SparkConf().set("spark.jars", "/myjars/spark-kafka-source-0.2.0-SNAPSHOT.jar, /myjars/SANSA_all_dep_NO_spark.jar")
sc = SparkContext( conf=conf)

test1 = sc._jvm.com.ippontech.Hello

def add10(num):
	print(num+10)
