import findspark
findspark.init()
import pyspark as ps
from pyspark import SparkContext, SparkConf

def read_rdf_file(file,jar_home):
    conf = SparkConf().set("spark.jars", jar_home)
    sc = SparkContext( conf=conf)
    sansa_rdf_io = sc._jvm.net.sansa_stack.rdf.spark.io.package  #The package to be used  
    spark_session_scala = sc._jvm.org.apache.spark.sql.SparkSession.builder().master("local").config("spark.serializer", "org.apache.spark.serializer.KryoSerializer").config("spark.sql.legacy.allowUntypedScalaUDF", "true").appName("SansaTEST").getOrCreate()
   
    ret_rdf = sansa_rdf_io.RDFReader(spark_session_scala).rdf(file)  
    return ret_rdf
        
def print_triples(ret,size):
    arr = ret.take(size)
    idx = 0
    for i in arr:
        idx = idx+1
        print(idx,"->",i.toString())

def print_count(ret):
    print("Count = ", ret.count())        
    
