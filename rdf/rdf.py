#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 6 18:12:29 2021

@author: erce

This class is a wrapper to use SANSA-Stack RDF layer functionalities
through Python.

It runs on SparkSession by importing SANSA-Stack jar with dependencies to
SparkContext then build a SparkSession with the SparkContext.

If Hadoop is installed in the system, it can be used to read and write data 
from/to Hadoop url. From the SANSA-Stack and our documentation, default
local Hadoop url is => hdfs://localhost:54310/user/[username]
| E.g: hdfs://localhost:54310/user/erce

"""
class Rdf:
    """    
    rdf.py
    ==============================================
    Python wrapper class for SANSA-Stack RDF Layer
    ==============================================
    """
    def __init__(self, sparkContext):
        """
        - Initializes packages for different parts of SANSA RDF Layer
        - Creates a dictionary with packages for easy access
        - Packages from this Rdf class can be used directly as in SANSA if
        needed. 
         | E.g.:
         | rdf.packagesDict["io"].RDFWriter(rdf.triples)
        
        Parameters
        ----------
        sparkContext
            A SparkContext object that includes SANSA-Stack jar with dependencies
            It is created as first step of our examples
        
        """
        # SparkContext
        self.sc = sparkContext
        # SANSA Rdf packages
        # SANSA Rdf IO package
        self.io = sparkContext._jvm.net.sansa_stack.rdf.spark.io.package
        # SANSA Rdf Mappings package
        self.mappings = sparkContext._jvm.net.sansa_stack.rdf.spark.mappings.package
        # SANSA Rdf Model package
        self.model = sparkContext._jvm.net.sansa_stack.rdf.spark.model.package
        # SANSA Rdf Ops package
        self.ops = sparkContext._jvm.net.sansa_stack.rdf.spark.ops.package
        # SANSA Rdf Partition package
        self.partition = sparkContext._jvm.net.sansa_stack.rdf.spark.partition.package
        # SANSA Rdf Qualityassessment package
        self.qualityassessment = sparkContext._jvm.net.sansa_stack.rdf.spark.qualityassessment.package
        # SANSA Rdf Stats package
        self.stats = sparkContext._jvm.net.sansa_stack.rdf.spark.stats.package
        # Put packages in a dictionary for easy access
        self.packagesDict = {"io": self.io,
                             "mappings": self.mappings,
                             "model": self.model,
                             "ops": self.ops,
                             "partition": self.partition,
                             "qualityassesment": self.qualityassessment,
                             "stats": self.stats}
        # Lang
        langLib = sparkContext._jvm.org.apache.jena.riot.Lang
        self.lang = langLib.NTRIPLES
           
    def initializeRdfReader(self, spark):
        """
        Initializes RDFReader class from SANSA RDF Layer to be used to read
        triples or for extended usage with deeper SANSA-Stack knowledge

        Parameters
        ----------
        spark : SparkSession
            SparkSession that was built with SANSA fat-jar and necessary
            configuration

        Returns
        -------
        rdfReader : RDFReader
            RDFReader object from SANSA RDF Layer

        """
        try:
            rdfReader = self.io.RDFReader(spark)
            
            return rdfReader
        
        except Exception as exception:
             self.outputExceptionLog('initializeRdfReader', exception)
    
    def readTriples(self, rdfReader, path):
        """
        Reads triples by using RDFReader class from SANSA RDF Layer

        Parameters
        ----------
        rdfReader : RDFReader
            RDFReader object from SANSA RDF Layer
        path : string
            Path to triple file in local machine or hadoop
             | E.g.:
             | file:///data/rdf.nt ===> Local machine
             | hdfs://localhost:54310/user/erce/rdf.nt ===> Hadoop
            
        """
        try:
            self.triples = rdfReader.rdf(path)
        
        except Exception as exception:
             self.outputExceptionLog('readTriples', exception)
    
    def count(self):
        """
        Counts the triples in the Rdf object by using count function from
        SANSA RDF Layer.

        Returns
        -------
        count : int
            Size of the triples that is read from the given file

        """
        try:
            count = self.triples.count()
                         
            return count
        
        except Exception as exception:
             self.outputExceptionLog('count', exception)

    
    def getTriples(self, size = 0):
        """
        Gets the triples array with the given size from the triples that
        is read from the given file. Uses "take" function from SANSA RDF
        Layer.

        Parameters
        ----------
        size : int, optional
            To return smaller array with given size or the whole array.
            The default is 0

        Returns
        -------
        triples : array
            Triples that is taken from the given file
        """
        try:
            if size == 0:
                size = self.count()
            
            triples = self.triples.take(size)
            
            return triples
        
        except Exception as exception:
             self.outputExceptionLog('getTriples', exception)
             
    
    def printTriples(self, tripleArray):
        """
        Prints triples as string with indexes from the given tripleArray.

        Parameters
        ----------
        tripleArray : array
            Triple array
        """
        try:
            elementIndex = 1
            for val in tripleArray:
                print("\n" + str(elementIndex) + ". Element: " + val.toString())
                elementIndex += 1
                
        except Exception as exception:
             self.outputExceptionLog('printTriples', exception)
            
    def saveAsTextFile(self, rdfObject, outputPath):
        """
        Save triples as text file in small partitions. Uses "saveAsTextFile"
        from SANSA RDF Layer.

        Parameters
        ----------
        rdfObject : RDF Triple Object
            Return object of SANSA RDF IO Package "rdf" function
        outputPath : string
            Output will be a directory with several text files
             | E.g.:
             | file:///output ===> Local machine
             | hdfs://localhost:54310/user/erce/output ===> Hadoop
        """
        try:
            rdfObject.saveAsTextFile(outputPath)
            
        except Exception as exception:
             self.outputExceptionLog('saveTriplesAsText', exception)
            
    def printRdfIOAttributes(self):
        """
        Prints attributes of RDF/IO to see which functions can be used from
        SANSA rdf/io Package.
        """
        print("RDF IO Package methods: ")
        print(dir(self.io))
        
    def printTripleObjectAttributes(self):
        """
        Prints attributes of RDF Triple Object. It can be used to see the
        usable functions. It is possible to use functions directly with 
        SANSA-Stack knowledge.
        """
        print("RDF Triple methods: ")
        print(dir(self.triples))
       
    def printAttributesOfGivenObject(self, obj):
        """
        Prints functions of the given object by using "dir" function in Python
         | E.g.:
         | rdf.printAttributesOfGivenObject(rdf.packagesDict["qualityassesment"])
        
        Parameters
        ----------
        obj : Object
            Any object to see the attributes and functions of it
        """
        print("Methods of the given object: ")
        print(dir(obj))
        
    def printRdfClassPackageList(self):
        """
        Prints the SANSA-Stack RDF Package list that is loaded to this python 
        wrapper.      
         | E.g.:
         | rdf.packagesDict["io"].RDFReader(spark)
        """
        print(self.packagesDict.keys())
        
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
