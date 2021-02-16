import pyspark as ps
from pyspark import SparkContext, SparkConf
import findspark as fs
import sys

class Rdf:
    # Initialize packages for different parts of SANSA RDF Layer
    def __init__(self, spark, sc, path):
        # SparkContext
        self.sc = sc
        # Rdf packages
        self.io = sc._jvm.net.sansa_stack.rdf.spark.io.package
        self.mappings = sc._jvm.net.sansa_stack.rdf.spark.mappings.package
        self.model = sc._jvm.net.sansa_stack.rdf.spark.model.package
        self.ops = sc._jvm.net.sansa_stack.rdf.spark.ops.package
        self.partition = sc._jvm.net.sansa_stack.rdf.spark.partition.package
        self.qualityassessment = sc._jvm.net.sansa_stack.rdf.spark.qualityassessment.package
        self.stats = sc._jvm.net.sansa_stack.rdf.spark.stats.package
        self.packagesDict = {"io": self.io, "mappings": self.mappings, "model": self.model,
                         "ops": self.ops, "partition": self.partition, "qualityassesment": self.qualityassessment,
                         "stats": self.stats}
        # Hadoop url and file path
        #self.hadoopUrl = "hdfs://localhost:54310"
        #self.rdfHadoopPath = self.hadoopUrl + ("/user/erce/rdf.nt"  if hadoopPath == '' else hadoopPath)
        # Local file path
        #self.rdfLocalPath = ""
        # Lang
        langLib = sc._jvm.org.apache.jena.riot.Lang
        self.lang = langLib.NTRIPLES
        self.rdfReader = self.initializeRdfReader(spark)
        self.triples = self.readTriples(self.rdfReader, path)
        
    # Initialite RDFReader object    
    def initializeRdfReader(self, spark):
        # RDFReader
        try:
            rdfReader = self.io.RDFReader(spark)
            
            return rdfReader
        except Exception as exception:
             self.outputExceptionLog('initializeRdfReader', exception)
    
    # Read and return triples
    def readTriples(self, rdfReader, path):
        # Triples
        try:
            triples = rdfReader.rdf(path)
        
            return triples
        except Exception as exception:
             self.outputExceptionLog('readTriples', exception)
    
    # Count the triples 
    def countTriples(self):
        try:
            count = self.triples.count()
                         
            return count
        except Exception as exception:
             self.outputExceptionLog('countTriples', exception)
    
    # Return triples array with given size
    def getTriplesWithGivenSize(self, size):
        try:
            triples = self.triples.take(size)
            
            return triples
        except Exception as exception:
             self.outputExceptionLog('getTriplesWithGivenSize', exception)
             
    # Print triples from the given tripleArray
    def printTriples(self, tripleArray):
        try:
            elementIndex = 1
            for val in tripleArray:
                print("\n" + str(elementIndex) + ". Element: " + val.toString())
                elementIndex += 1
        except Exception as exception:
             self.outputExceptionLog('printTriples', exception)
            
    # Save triples as text
    def saveTriplesAsText(self, rdfObject, outputPath):
        try:
            rdfObject.saveAsTextFile(outputPath)
        except Exception as exception:
             self.outputExceptionLog('saveTriplesAsText', exception)
            
    # Prints rdf attributes of IO
    def printRdfIOAttributes(self):
        print("RDF IO Package methods: ")
        print(dir(self.io))
        
    # Prints attributes of RDF Triples Object
    def printRdfReaderAttributes(self):
        print("RDF Triples methods: ")
        print(dir(self.triples))
       
    # Print methods of given object
    def printMethodsOfGivenObject(self, obj):
        print("Methods of the given object: ")
        print(dir(obj))
        
    # Print packages of Rdf class
    def printRdfPackageList(self):
        print(self.packagesDict.keys())
        
    def outputExceptionLog(self, functionName, exception):
        print("--> " + functionName, exception)
        self.sc.stop()
