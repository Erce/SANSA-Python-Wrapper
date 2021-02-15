import findspark
findspark.init()

import pyspark as ps
from pyspark import SparkContext, SparkConf
import traceback
import os.path
from os import path
import subprocess
    
#sparkP = ps.sql.SparkSession.builder \
#    .master("local") \
#    .appName("PYTHON_SPARK_SESSION") \
#    .config("spark.some.config.option", "some-value") \
#    .config("spark.jars", "/home/alex/Desktop/TEST/scala/extend/target/spark-kafka-source-0.2.0-SNAPSHOT.jar, /home/alex/Desktop/SANSA4/SANSA-Stack/sansa-stack/sansa-stack-spark/target/SANSA_all_dep_NO_spark.jar") \
#    .getOrCreate()


#####################################################
##    Create a pyspark-session and load jar   #######
#####################################################
def create_spark_session(sansa_jar):    
    global conf 
    #conf = SparkConf().set("spark.jars", "/home/alex/Desktop/SANSA4/SANSA-Stack/sansa-stack/sansa-stack-spark/target/SANSA_all_dep_NO_spark.jar")
    
    #sparkP = ps.sql.SparkSession.builder.getOrCreate()
    print(sansa_jar)
    sparkP = ps.sql.SparkSession.builder \
        .master("local") \
            .appName("PYTHON_SPARK_SESSION") \
                .config("spark.some.config.option", "some-value") \
                    .config("spark.jars", sansa_jar) \
                        .getOrCreate()
   
    #conf = sparkP.conf  #.get("PYTHON_SPARK_SESSION")

    
    global sc 
    sc = SparkContext.getOrCreate() #SparkContext(conf = conf)

    conf = sc.getConf()
    
#####################################################
##     Construction of an Java array          #######
#####################################################
def toJStringArray(arr):
    jarr = sc._gateway.new_array(sc._jvm.java.lang.String, len(arr))
    for i in range(len(arr)):
        jarr[i] = arr[i]
    return jarr

###########################################################
## ML-ALGORITHM     Similaritypipeline - Batet-Call #######
###########################################################
def ml_similarity_batet(nt_file_in, result_folder_in):
    ml_similarity(nt_file_in, result_folder_in, "Batet")
    
###########################################################
## ML-ALGORITHM     Similaritypipeline - Simpson-Call #######
###########################################################
def ml_similarity_simpson(nt_file_in, result_folder_in):
    ml_similarity(nt_file_in, result_folder_in, "Simpson")
    
###########################################################
## ML-ALGORITHM     Similaritypipeline - Ochiai-Call #######
###########################################################
def ml_similarity_ochiai(nt_file_in, result_folder_in):
    ml_similarity(nt_file_in, result_folder_in, "Ochiai")
 
###########################################################
## ML-ALGORITHM     Similaritypipeline - Dice-Call #######
###########################################################
def ml_similarity_dice(nt_file_in, result_folder_in):
    ml_similarity(nt_file_in, result_folder_in, "Dice")

#############################################################
## ML-ALGORITHM     Similaritypipeline - Tversky-Call #######
#############################################################
def ml_similarity_tversky(nt_file_in, result_folder_in):
    ml_similarity(nt_file_in, result_folder_in, "Tversky")

#############################################################
## ML-ALGORITHM     Similaritypipeline - Jaccard-Call #######
#############################################################
def ml_similarity_jaccard(nt_file_in, result_folder_in):
    ml_similarity(nt_file_in, result_folder_in, "Jaccard")

#############################################################
## ML-ALGORITHM     Similaritypipeline - MinHash-Call #######
#############################################################
def ml_similarity_minhash(nt_file_in, result_folder_in):
    ml_similarity(nt_file_in, result_folder_in, "MinHash")


######################################################
## ML-ALGORITHM     Similaritypipeline ###############
######################################################
def ml_similarity(nt_file_in, result_folder_in, mode):
    print("-----------Starting Similaritypipeline - "+mode+" Algorithm--------")
    nt_file = nt_file_in
    result_folder = result_folder_in
    if nt_file[0:4] != "hdfs" and nt_file[0:4] != "file":
            nt_file = "file://" + nt_file
    if result_folder[0:4] != "hdfs" and result_folder[0:4] != "file":
            result_folder = "file://" + result_folder
    #No error in validation -> proceed with Algorithm
    if validate_arguments(nt_file,result_folder) == 0: 
        SimilarityPipeline = sc._jvm.net.sansa_stack.ml.spark.similarity.run.SimilarityPipeline
    
        java_arr = toJStringArray(['1','2','3'])
        java_arr[0] = nt_file
        java_arr[1] = result_folder
        java_arr[2] = mode # "Batet"
        
        try:
            SimilarityPipeline.main(java_arr)
            print("SUCCESS! Resultfiles generated in: " + result_folder_in)
        except Exception as e: 
            print(e)

####################################################################################
## Validation for Hadoop files and directories #####################################
####################################################################################
def hadoop_check(location):
    #### https://stackoverflow.com/questions/53111903/given-a-hdfs-path-how-do-i-know-if-it-is-a-folder-or-a-file-with-python ####
    filexistchk="/usr/local/hadoop-2.8.3/bin/hdfs dfs -test -e "+location+";echo $?"
    #echo $? will print the exit code of previously execited command
    
    filexistchk_output=subprocess.Popen(filexistchk,shell=True,stdout=subprocess.PIPE).communicate()
    filechk="/usr/local/hadoop-2.8.3/bin/hdfs dfs -test -d "+location+";echo $?"
    filechk_output=subprocess.Popen(filechk,shell=True,stdout=subprocess.PIPE).communicate()
    #Check if location exists
    if '1' not in str(filexistchk_output[0]):
        #check if its a directory
        if '1' not in str(filechk_output[0]):
            #print('The given URI is a directory: '+location)
            return "dir"
        else:
            #print('The given URI is a file: '+location)
            return "file"
    else:
        #print(location+ " does not exist.")
        return "not_exists"

####################################################################################
## Validation of input Parameters. accepts hdfs:// , file:// and local paths #######
####################################################################################
def validate_arguments (source_file_in, result_folder_in):
    error = 0
    source_file = source_file_in
    result_folder = result_folder_in
    source_type = source_file[0:4]
    result_type = result_folder[0:4]
    #does the string start with file:// ?
    if source_type == "file":
        source_file = source_file[7:]
    if result_type == "file":
        result_folder = result_folder[7:]
        
    if source_type != "hdfs":
        #File check
        file_exist = path.exists(source_file)
    else:
        #Hdfs check
        if hadoop_check(source_file) == "file":
            file_exist = True
        else:
            file_exist = False
    
    if result_type != "hdfs":
        #Directory check
        folder_exist = path.exists(result_folder)
    else:
        #Hdfs check
        if hadoop_check(result_folder) == "not_exists":
            folder_exist = False
        else:
            folder_exist = True
    
    if file_exist == False:
        print("ERROR: File does not exists: " + source_file)
        error = 1
    if folder_exist == True:
        print("ERROR: Result_directory already exists: " + result_folder)
        error = 1

    return error


#Spark Session in Python
#create_spark_session("/home/alex/Desktop/SANSA4/SANSA-Stack/sansa-stack/sansa-stack-spark/target/SANSA_all_dep_NO_spark.jar")

#Spark Session in Scala
#spark_session_scala = sc._jvm.org.apache.spark.sql.SparkSession.builder().master("local").config("spark.serializer", "org.apache.spark.serializer.KryoSerializer").config("spark.sql.legacy.allowUntypedScalaUDF", "true").appName("SansaSpark").getOrCreate()

#nt_file = "file:///home/alex/Desktop/SANSA4/SANSA-Stack/sansa-ml/sansa-ml-spark/src/main/resources/rdf.nt" 
#result_folder = "file:///home/alex/Desktop/SANSA4/SANSA-Stack/sansa-ml/sansa-ml-spark/src/main/resources/rdf_out_Batet_py24" 

#nt_file2 = "/home/alex/Desktop/SANSA4/SANSA-Stack/sansa-ml/sansa-ml-spark/src/main/resources/rdf.nt" 
#result_folder2 = "/home/alex/Desktop/SANSA4/SANSA-Stack/sansa-ml/sansa-ml-spark/src/main/resources/rdf_out_Batet_py25" 
#file = "hdfs://localhost:54310/user/hduser/rdf.nt"
#result_folder3 = "hdfs://localhost:54310/user/hduser"

#hdfs dfs -chown alex /user/hduser/

#          MinHash, Jaccard, Tversky, Braun Blanquet   , Dice, Ochiai, +Simpson, #MinHashJaccardStacked
#ml_similarity(nt_file, result_folder3 + "/output_10", "MinHash")
