#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 11:20:27 2021

@author: erce
"""
import pathlib
# Get the current path
currentPath = pathlib.Path().absolute()
import sys
sys.path.insert(0, str(currentPath) + '/..')
from pyspark import SparkContext, SparkConf
from pysansa.rdf.rdf import Rdf
from pysansa.query.query import Query
import pathlib

# Get the current path
currentPath = pathlib.Path().absolute()
# Spark Session and Config
conf = SparkConf().set("spark.jars", str(currentPath) + "../../pysansa/myjars/SANSA_all_dep_NO_spark.jar")
sc = SparkContext(conf=conf)
# Spark Object
spark = sc._jvm.org.apache.spark.sql.SparkSession.builder().master("local").config("spark.serializer", "org.apache.spark.serializer.KryoSerializer").config("spark.sql.legacy.allowUntypedScalaUDF", "true").appName("SansaRDF-Query").getOrCreate()
# Rdf object
rdf = Rdf(sc)
# Initialize Rdf Reader
rdfReader = rdf.initializeRdfReader(spark)
# Read triples from the given path
triples = rdf.readTriples(rdfReader, path = 'file:///' + str(currentPath) + '../../data/rdf.nt')
# Count triples from the object
size = rdf.count()
# Print size of triples
print("Size of triples: " + str(size))
# Get triples as array
triples = rdf.getTriples(30)
# Get triples from Rdf object
triples = rdf.triples
# Create Query object
query = Query(sc)
# Set and create Sparqlify executor object
query.setTriplesToSparqlifyExecutor(triples)
# An example query
query1 = "SELECT * WHERE {?s ?p ?o} LIMIT 106"
# Run the query and return the result object
result = query.runQueryOnSparqlify(query1)
# Print possible usable functions of the result object
query.printAttributes(result)
# Print the result to the console as a table
query.show(result)
# Convert the result to DataFrame
dfResult = query.convertToDataFrame(result)
# Convert to JSON 
json = result.toJSON()
# Print JSON
json.show()
# Get the first JSON element
first = json.first()
# Get the 5 first element from the JSON
taken = json.take(5)
# Get the first element from the JSON Array
taken[0]
# Print the JSON array
print(dir(taken))
# Get 10 rows from the DataFrame
dfResultArray = query.takeFromDataFrame(dfResult, 10)
# Print the row array that was taken from the DataFrame
query.printDF(dfResultArray)
# Get the first row of the DataFrame Array
firstRow = query.getRow(dfResultArray, 0)
# Get the first column of the first row
firstColumnOfFirstRow = query.getColumn(firstRow, 0)
# Get the third column of the first row
firstColumnOfFirstRow = query.getColumn(firstRow, 2)
# Get the fourth column of the first row
firstColumnOfFirstRow = query.getColumn(firstRow, 3)
# Get the second row of the DataFrame Array
secondRow = query.getRow(dfResultArray, 1)
# JSON of the second row
jsonOfSecondRow = secondRow.json()
# Print the JSON of the second row
print(jsonOfSecondRow)
# Print JSON Value
print(secondRow.jsonValue())
# Print Schema
print(secondRow.schema())
# Print pretty JSON
print(secondRow.prettyJson())
# Stop SparkContext to prevent overloading
sc.stop()
