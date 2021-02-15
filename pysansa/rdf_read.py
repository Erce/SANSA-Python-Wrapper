import findspark
findspark.init()

import pyspark as ps
from pyspark import SparkContext, SparkConf

#conf = SparkConf().setAppName("SANSA TESTING")
#sc = SparkContext(conf = conf)



#ret_rdf = sansa_rdf_io_pack.RDFReader(spark_session_scala).rdf(file)

def read_rdf_file(file,jar_home):
    
    conf = SparkConf().set("spark.jars", jar_home)
    sc = SparkContext( conf=conf)

    print("Entered RDF Reader_____________________________________________")

    sansa_rdf_io = sc._jvm.net.sansa_stack.rdf.spark.io
    sansa_rdf_io_pack = sc._jvm.net.sansa_stack.rdf.spark.io.package

    spark_session_scala = sc._jvm.org.apache.spark.sql.SparkSession.builder().master("local").config("spark.serializer", "org.apache.spark.serializer.KryoSerializer").config("spark.sql.legacy.allowUntypedScalaUDF", "true").appName("SansaTEST").getOrCreate()

    lang_lib = sc._jvm.org.apache.jena.riot.Lang
    lang = lang_lib.NTRIPLES
    
    ret_rdf = sansa_rdf_io_pack.RDFReader(spark_session_scala).rdf(file)
    
    return ret_rdf
    #print(ret_rdf)
    #print(dir(ret_rdf))
    
    
    

def add10(num):
    print(num+10)
