#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 22:45:51 2021

@author: erce

This class is a wrapper to use SANSA-Stack Query layer functionalities
through Python.

It runs on SparkSession by importing SANSA-Stack jar with dependencies to
SparkContext then build a SparkSession with the SparkContext.

If Hadoop is installed in the system, it can be used to read and write data 
from/to Hadoop url. From the SANSA-Stack and our documentation, default
local Hadoop url is => hdfs://localhost:54310/user/[username]
| E.g: hdfs://localhost:54310/user/erce

"""
class Query:
    """    
    query.py
    ==========================================
    Python wrapper class for SANSA Query Layer
    ==========================================
    """
    def __init__(self, sparkContext):
        """
        Initialize packages for different parts of SANSA Query Layer
        
        Parameters
        ----------
        sparkContext : SparkContext
            A SparkContext object which is created as first step of our examples

        """
        self.sc = sparkContext
        # SANSA Query package
        self.query = self.sc._jvm.net.sansa_stack.query.spark.query.package
        
    def setTriplesToSparqlifyExecutor(self, triples):
        """
        Chooses Sparqlify as default and returns the object

        Parameters
        ----------
        triples : RDF Triple object
            Triple object that is returned from SANSA RDF IO Package "rdf" 
            function

        """
        try:
            self.sparqlify = self.query.SparqlifySPARQLExecutorAsDefault(triples)
            
        except Exception as exception:
            self.outputExceptionLog("setTriplesToSparqlifyExecutor", exception)
        
    def runQueryOnSparqlify(self, query):
        """
        Runs the given sparql query on Sparqlify        

        Parameters
        ----------
        query : string
            Sparql query that fits to the triples

        Returns
        -------
        result : object
            Return from SANSA Query package "sparql" function

        """
        try:
            result = self.sparqlify.sparql(query)
            
            return result
        
        except Exception as exception:
            self.outputExceptionLog("runQueryOnSparqlify", exception)
        
    def createAndGetDataLakeObject(self, query):    
        """
        Creates and returns DataLake object        

        Parameters
        ----------
        query : string
            Sparql query that fits to the triples
            
        Returns
        -------
        DataLake object
            Object that returns from SANSA Query package "DataLake" class

        """
        try:
            self.dataLake = self.query.DataLake(self.spark)
        
            return self.dataLake
        except Exception as exception:
            self.outputExceptionLog("createAndGetDataLakeObject", exception)
        
    def runQueryWithDataLake(self, sparQLQuery, mappingsUrl, configUrl):
        """
        Runs query with DataLake         

        Parameters
        ----------
        sparQLQuery : string
        mappingsUrl : string
        configUrl : string

        Returns
        -------
        result : Object

        """
        try:
            result = self.dataLake.sparqlDL(sparQLQuery, mappingsUrl, configUrl)
            
            return result
        
        except Exception as exception:
            self.outputExceptionLog("runQueryWithDataLake", exception)
            
    def show(self, result):
        """
        Shows the data by using "show" function from SANSA Query package
        and print a table to the console.

        Parameters
        ----------
        result : Object
            The object that is returned from runQueryOnSparqlify function

        """       
        try:
            result.show()
        
        except Exception as exception:
            self.outputExceptionLog("show", exception)
        
    def convertToDataFrame(self, obj):
        """
        Converts object to DataFrame        

        Parameters
        ----------
        obj : Object
            Return object from runQueryOnSparqlify function

        Returns
        -------
        result : DataFrame
            A DataFrame object

        """
        try:
            result = obj.toDF()
            
            return result
        except Exception as exception:
            self.outputExceptionLog("convertToDataFrame", exception)
        
    def count(self, obj):
        """
        Counts DataFrame rows        

        Parameters
        ----------
        obj : DataFrame
            A DataFrame object that is converted from Sparqlify object

        Returns
        -------
        count : int
            Number of rows in the DataFrame

        """
        try:
            count = obj.count()
        
            return count
        
        except Exception as exception:
            self.outputExceptionLog("count", exception)
            
    def takeFromDataFrame(self, df, size = 0):
        """
        Takes rows depending on the given size from DataFrame       

        Parameters
        ----------
        df : DataFrame
            DataFrame object 
        size : int, optional
            Size of the taken rows from DataFrame with "take" function from 
            SANSA Query package. The default is 0.

        Returns
        -------
        result : array
            Array from rows that are taken from the DataFrame

        """
        try:
            if size == 0:
                size = self.count(df)
                
            result = df.take(size)
            
            return result
    
        except Exception as exception:
            self.outputExceptionLog("takeFromDataFrame", exception)
            
    def getRow(self, df, rowIndex):
        """
        Gets a row from the given DataFrame with the given row index 

        Parameters
        ----------
        df : DataFrame
            DataFrame object 
        rowIndex : int
            Index of any row that is wished to be returned

        Returns
        -------
        object
            A row object chosen from the given DataFrame

        """
        try:
            row = df[0]
            
            return row 
        
        except Exception as exception:
            self.outputExceptionLog("getRow", exception)
            
    def getColumn(self, row, columnIndex):
        """
        Gets a column from the given row        

        Parameters
        ----------
        row : array
            A row array that is taken from DataFrame
        columnIndex : int
            Column index in the range of the given row

        Returns
        -------
        string
            Chosen column from the given row

        """
        try:
            return row.values()[columnIndex]
            
        except Exception as exception:
            self.outputExceptionLog("getColumn", exception)

    def printDF(self, rowArray):   
        """
        Prints the DataFrame rows with indexes

        Parameters
        ----------
        rowArray : DataFrame
             Array that is taken with "take" function in 
             SANSA Query package. Return of "takeFromDataFrame" function in this
             wrapper

        """
        try:
            elementIndex = 1
            for val in rowArray:
                print("\n" + str(elementIndex) + ". Element: " + val.toString())
                elementIndex += 1
            
        except Exception as exception:
            self.outputExceptionLog("printDF", exception)
            
    def printAttributes(self, obj):
        """
        Prints functions of the given object by using "dir" function in Python     

        Parameters
        ----------
        obj : object
            Any object to see the attributes and functions of it

        """
        print(dir(obj))
    
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