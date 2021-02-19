import pyspark as ps
from pyspark import SparkContext, SparkConf
import findspark as fs
import sys

class Rdf:
    def __init__(self, sparkContext):
        # Initializes packages for different parts of SANSA RDF Layer
        # SparkContext
        self.sc = sparkContext
        # Rdf packages
        self.io = sparkContext._jvm.net.sansa_stack.rdf.spark.io.package
        self.mappings = sparkContext._jvm.net.sansa_stack.rdf.spark.mappings.package
        self.model = sparkContext._jvm.net.sansa_stack.rdf.spark.model.package
        self.ops = sparkContext._jvm.net.sansa_stack.rdf.spark.ops.package
        self.partition = sparkContext._jvm.net.sansa_stack.rdf.spark.partition.package
        self.qualityassessment = sparkContext._jvm.net.sansa_stack.rdf.spark.qualityassessment.package
        self.stats = sparkContext._jvm.net.sansa_stack.rdf.spark.stats.package
        self.packagesDict = {"io": self.io, "mappings": self.mappings, "model": self.model,
                         "ops": self.ops, "partition": self.partition, "qualityassesment": self.qualityassessment,
                         "stats": self.stats}
        # Lang
        langLib = sparkContext._jvm.org.apache.jena.riot.Lang
        self.lang = langLib.NTRIPLES
        # self.rdfReader = self.initializeRdfReader(spark)
        # self.triples = self.readAndReturnTripleObject(self.rdfReader, path)
           
    def initializeRdfReader(self, spark):
        # Initializes RDFReader object 
        try:
            rdfReader = self.io.RDFReader(spark)
            
            return rdfReader
        
        except Exception as exception:
             self.outputExceptionLog('initializeRdfReader', exception)
    
    def readTriples(self, rdfReader, path):
        # Reads and returns triples
        try:
            self.triples = rdfReader.rdf(path)
        
        except Exception as exception:
             self.outputExceptionLog('readTriples', exception)
    
    def count(self):
        # Counts the triples
        try:
            count = self.triples.count()
                         
            return count
        
        except Exception as exception:
             self.outputExceptionLog('count', exception)

    
    def getTriplesAsArray(self, size = 0):
        # Returns triples array with given size
        try:
            if size == 0:
                size = self.countTriples()
            
            triples = self.triples.take(size)
            
            return triples
        
        except Exception as exception:
             self.outputExceptionLog('getTriplesAsArray', exception)
             
    
    def printTriples(self, tripleArray):
        # Prints triples from the given tripleArray
        try:
            elementIndex = 1
            for val in tripleArray:
                print("\n" + str(elementIndex) + ". Element: " + val.toString())
                elementIndex += 1
                
        except Exception as exception:
             self.outputExceptionLog('printTriples', exception)
            
    def saveTriplesAsText(self, rdfObject, outputPath):
        # Saves triples as text
        try:
            rdfObject.saveAsTextFile(outputPath)
            
        except Exception as exception:
             self.outputExceptionLog('saveTriplesAsText', exception)
            
    def printRdfIOAttributes(self):
        # Prints rdf attributes of RDF/IO
        print("RDF IO Package methods: ")
        print(dir(self.io))
        
    def printTripleObjectAttributes(self):
        # Prints attributes of RDF Triple Object
        print("RDF Triple methods: ")
        print(dir(self.triples))
       
    def printAttributesOfGivenObject(self, obj):
        # Prints methods of given object
        print("Methods of the given object: ")
        print(dir(obj))
        
    def printRdfClassPackageList(self):
        # Prints packages of Rdf class
        print(self.packagesDict.keys())
        
    def outputExceptionLog(self, functionName, exception):
        # Prints the exception and function name which throws the exception
        print("--> " + functionName, exception)
        self.sc.stop()
