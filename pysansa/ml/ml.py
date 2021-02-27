"""
Created on Fri Feb 26 2021

@author: alex

This class is a wrapper to use SANSA-Stack ML layer functionalities
through Python.

It runs on SparkSession by importing SANSA-Stack jar with dependencies to
SparkContext then build a SparkSession with the SparkContext.

If Hadoop is installed in the system, it can be used to read and write data 
from/to Hadoop url. From the SANSA-Stack and our documentation, default
local Hadoop url is => hdfs://localhost:54310/user/[username]
| E.g: hdfs://localhost:54310/user/alex

"""

class ML:
    """    
    ml.py
    ==============================================
    Python wrapper class for SANSA-Stack ML Layer
    ==============================================
    """
        
    #####################################################
    ##    Create a pyspark-session and load jar   #######
    #####################################################
    def create_spark_session(self, sansa_jar):    
        """
        Creates a SparkSession and loads the jar into it.

        Parameters
        ----------
        sansa_jar : String
            Location of the Jar file, read dynamicaly by the __init__ method

        """
        import pyspark as ps
        from pyspark import SparkContext, SparkConf
        
        #Pyspark Session        
        self.sparkP = ps.sql.SparkSession.builder \
            .master("local") \
                .appName("PYTHON_SPARK_SESSION") \
                    .config("spark.sql.legacy.allowUntypedScalaUDF", "true") \
                        .config("spark.jars", sansa_jar) \
                            .getOrCreate()
        print(sansa_jar + " loaded!")    
        
        self.sc = SparkContext.getOrCreate() 
    
        self.conf = self.sc.getConf()

    def __init__(self):
        """
        - Initializes packages for different parts of SANSA ML Layer
        - Packages from this ML class can be used directly as in SANSA if
        needed.  
         | E.g.:
         | ML.packagesDict["SimilarityPipeline"].main(java_arr)
        
        """
        import pathlib
        # Get the current path
        currentPath = pathlib.Path().absolute()
        
        import sys
        sys.path.insert(0, str(currentPath) + '/..')

        self.create_spark_session(str(currentPath) + "../../pysansa/myjars/SANSA_all_dep_NO_spark.jar")    

        # SANSA ML SimilarityPipeline, you can also include all the other packages/algorithms this way
        self.SimilarityPipeline = self.sc._jvm.net.sansa_stack.ml.spark.similarity.run.SimilarityPipeline

    def toJStringArray(self, arr):
        """
        Converts the given Stringarray into an Java String Array, to be used as input Parameter.

        Parameters
        ----------
        arr : Array of Strings
            e.g. ['1','2','3']
        Returns
        -------
        jarr : java.lang.String[],
            java.lang.String[] Object

        """
        jarr = self.sc._gateway.new_array(self.sc._jvm.java.lang.String, len(arr))
        for i in range(len(arr)):
            jarr[i] = arr[i]
        return jarr
    
    def ml_similarity(self, nt_file_in, result_folder_in, mode):
        """
        Uses SANSA's ML Similarity Algorithm with a specific mode

        Parameters
        ----------
        nt_file_in : String
            Path to the nt file
        result_folder_in : String
            Path to the output folder, result will go here
            Please make sure the output directory does not exist yet!
        mode : String
            Algorithmmode
        
        """
        print("-----------Starting Similaritypipeline - "+mode+" Algorithm--------")
        nt_file = nt_file_in
        result_folder = result_folder_in
        if nt_file[0:4] != "hdfs" and nt_file[0:4] != "file":
                nt_file = "file://" + nt_file
        if result_folder[0:4] != "hdfs" and result_folder[0:4] != "file":
                result_folder = "file://" + result_folder
        #No error in validation -> proceed with Algorithm
        #if validate_arguments(nt_file,result_folder) == 0: 
        SimilarityPipeline = self.SimilarityPipeline
        
        java_arr = self.toJStringArray(['1','2','3'])
        java_arr[0] = nt_file
        java_arr[1] = result_folder
        java_arr[2] = mode # "Batet"
        
        try:
            SimilarityPipeline.main(java_arr)
            print("SUCCESS! Resultfiles generated in: " + result_folder_in)
            print("Make sure to use a new output_folder when you run another algorithm")
            print("______________________________________________________")
        except Exception as exception:
             self.outputExceptionLog('ml_similarity', exception)
            
    ###########################################################
    ## ML-ALGORITHM     Similaritypipeline - Batet-Call #######
    ###########################################################
    def ml_similarity_batet(self, nt_file_in, result_folder_in):
        """
        Uses SANSA's ML Similarity Algorithm with a specific mode

        Parameters
        ----------
        nt_file_in : String
            Path to the nt file
        result_folder_in : String
            Path to the output folder, result will go here
        mode : String
            Algorithmmode
        
        """
        self.ml_similarity(nt_file_in, result_folder_in, "Batet")
        
    ###########################################################
    ## ML-ALGORITHM     Similaritypipeline - Simpson-Call #######
    ###########################################################
    def ml_similarity_simpson(self, nt_file_in, result_folder_in):
        """
        Uses SANSA's ML Similarity Algorithm Simpson version

        Parameters
        ----------
        nt_file_in : String
            Path to the nt file
             | E.g.:
             | file:///data/rdf.nt ===> Local machine
             | hdfs://localhost:54310/user/alex/rdf.nt ===> Hadoop
        result_folder_in : String
            Path to the output folder, result will go here
             | E.g.:
             | file:///data/rdf_output  ===> Local machine
             | hdfs://localhost:54310/user/alex/rdf_output ===> Hadoop
        
        """
        self.ml_similarity(nt_file_in, result_folder_in, "Simpson")
        
    ###########################################################
    ## ML-ALGORITHM     Similaritypipeline - Ochiai-Call #######
    ###########################################################
    def ml_similarity_ochiai(self, nt_file_in, result_folder_in):
        """
        Uses SANSA's ML Similarity Algorithm Ochiai version

        Parameters
        ----------
        nt_file_in : String
            Path to the nt file
             | E.g.:
             | file:///data/rdf.nt ===> Local machine
             | hdfs://localhost:54310/user/alex/rdf.nt ===> Hadoop
        result_folder_in : String
            Path to the output folder, result will go here
             | E.g.:
             | file:///data/rdf_output  ===> Local machine
             | hdfs://localhost:54310/user/alex/rdf_output ===> Hadoop
        
        """
        self.ml_similarity(nt_file_in, result_folder_in, "Ochiai")
        
    ###########################################################
    ## ML-ALGORITHM     Similaritypipeline - Dice-Call #######
    ###########################################################
    def ml_similarity_dice(self, nt_file_in, result_folder_in):
        """
        Uses SANSA's ML Similarity Algorithm Dice version

        Parameters
        ----------
        nt_file_in : String
            Path to the nt file
             | E.g.:
             | file:///data/rdf.nt ===> Local machine
             | hdfs://localhost:54310/user/alex/rdf.nt ===> Hadoop
        result_folder_in : String
            Path to the output folder, result will go here
             | E.g.:
             | file:///data/rdf_output  ===> Local machine
             | hdfs://localhost:54310/user/alex/rdf_output ===> Hadoop
        
        """
        self.ml_similarity(nt_file_in, result_folder_in, "Dice")
    
    #############################################################
    ## ML-ALGORITHM     Similaritypipeline - Tversky-Call #######
    #############################################################
    def ml_similarity_tversky(self, nt_file_in, result_folder_in):
        """
        Uses SANSA's ML Similarity Algorithm Tversky version

        Parameters
        ----------
        nt_file_in : String
            Path to the nt file
             | E.g.:
             | file:///data/rdf.nt ===> Local machine
             | hdfs://localhost:54310/user/alex/rdf.nt ===> Hadoop
        result_folder_in : String
            Path to the output folder, result will go here
             | E.g.:
             | file:///data/rdf_output  ===> Local machine
             | hdfs://localhost:54310/user/alex/rdf_output ===> Hadoop
        
        """
        self.ml_similarity(nt_file_in, result_folder_in, "Tversky")
    
    #############################################################
    ## ML-ALGORITHM     Similaritypipeline - Jaccard-Call #######
    #############################################################
    def ml_similarity_jaccard(self, nt_file_in, result_folder_in):
        """
        Uses SANSA's ML Similarity Algorithm Jaccard version

        Parameters
        ----------
        nt_file_in : String
            Path to the nt file
             | E.g.:
             | file:///data/rdf.nt ===> Local machine
             | hdfs://localhost:54310/user/alex/rdf.nt ===> Hadoop
        result_folder_in : String
            Path to the output folder, result will go here
             | E.g.:
             | file:///data/rdf_output  ===> Local machine
             | hdfs://localhost:54310/user/alex/rdf_output ===> Hadoop
        
        """
        self.ml_similarity(nt_file_in, result_folder_in, "Jaccard")
    
    #############################################################
    ## ML-ALGORITHM     Similaritypipeline - MinHash-Call #######
    #############################################################
    def ml_similarity_minhash(self, nt_file_in, result_folder_in):
        """
        Uses SANSA's ML Similarity Algorithm MinHash version

        Parameters
        ----------
        nt_file_in : String
            Path to the nt file
             | E.g.:
             | file:///data/rdf.nt ===> Local machine
             | hdfs://localhost:54310/user/alex/rdf.nt ===> Hadoop
        result_folder_in : String
            Path to the output folder, result will go here
             | E.g.:
             | file:///data/rdf_output  ===> Local machine
             | hdfs://localhost:54310/user/alex/rdf_output ===> Hadoop
        
        """
        self.ml_similarity(nt_file_in, result_folder_in, "MinHash")
    
    ####################################################################################
    ## Validation for Hadoop files and directories #####################################
    ####################################################################################
    def hadoop_check(self, location):
        """
        Validates Hadoop paths, currently not in use but kept for debugging

        Parameters
        ----------
        location : String
            Path to the nt file or a folder
             | E.g.:
             | hdfs://localhost:54310/user/alex/rdf.nt ===> Hadoop
             | requires /usr/local/hadoop-2.8.3/bin/hdfs hardcoded currently, should be enhanced for further use
        Returns
        -------
        String : String,
            dir, file or not_exists
            
        """
        import subprocess
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
    def validate_arguments (self, source_file_in, result_folder_in):
        """
        Validates input Parameters for ML-Algorithms, Hadoop and local

        Parameters
        ----------
        source_file_in : String
            Path to the nt file
             | E.g.:
             | file:///data/rdf.nt ===> Local machine
             | hdfs://localhost:54310/user/alex/rdf.nt ===> Hadoop
        result_folder_in : String
            Path to the output folder, result will go here
             | E.g.:
             | file:///data/rdf_output  ===> Local machine
             | hdfs://localhost:54310/user/alex/rdf_output ===> Hadoop
        Returns
        -------
        error : Integer,
            0 for all fine, 1 for an error. Console output
            
        """
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
            file_exist = self.path.exists(source_file)
        else:
            #Hdfs check
            if self.hadoop_check(source_file) == "file":
                file_exist = True
            else:
                file_exist = False
        
        if result_type != "hdfs":
            #Directory check
            folder_exist = self.path.exists(result_folder)
        else:
            #Hdfs check
            if self.hadoop_check(result_folder) == "not_exists":
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
    
    def outputExceptionLog(self, functionName, exception):
            """
            Exception function to print the exception and the function that 
            throws the exception.
            Stops the SparkSession in case of failure as well if there are too many
            SparkSessions running, creating new SparkSession in examples will fail.
    
            Parameters
            ----------
            functionName : string
                Name of the function that throws the exception
            exception : Exception
                Exception object in Python
            """
            print("--> " + functionName, exception)
            self.sc.stop()

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

#Spark Session in Python, needs correct jar location!
#ml.create_spark_session("/home/alex/Desktop/SANSA4/SANSA-Stack/sansa-stack/sansa-stack-spark/target/SANSA_all_dep_NO_spark.jar")
