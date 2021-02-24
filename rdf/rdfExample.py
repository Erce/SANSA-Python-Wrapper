#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 01:42:30 2021

@author: erce
"""
import pathlib
# Get the current path
currentPath = pathlib.Path().absolute()
import sys
sys.path.insert(0, str(currentPath) + '/..')
from pyspark import SparkContext, SparkConf
from pysansa.rdf.rdf import Rdf
import pathlib

# Get the current path
currentPath = pathlib.Path().absolute()
# Spark Session and Config
conf = SparkConf().set("spark.jars", str(currentPath) + "../../pysansa/myjars/SANSA_all_dep_NO_spark.jar")
sc = SparkContext(conf=conf)
# Spark object
spark = sc._jvm.org.apache.spark.sql.SparkSession.builder().master("local").config("spark.serializer", "org.apache.spark.serializer.KryoSerializer").config("spark.sql.legacy.allowUntypedScalaUDF", "true").appName("SansaRDF").getOrCreate()
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
# Print triples
rdf.printTriples(triples)
# Print attributes of RDF/IO
rdf.printRdfIOAttributes()
# Print triple object attribute
rdf.printTripleObjectAttributes()
# Print Rdf class packages
rdf.printRdfClassPackageList()

########################################################
# Example usage of different packages from Rdf class
# io package RDFReader
reader = rdf.packagesDict["io"].RDFReader(spark)
print("RDFReader class methods: ")
print(dir(reader))
########################################################
# Example usage of different packages from Rdf class
# io package RDFWriter
writer = rdf.packagesDict["io"].RDFWriter(rdf.triples)
print("RDFWriter class methods: ")
print(dir(writer))
########################################################
# Example usage of different packages from Rdf class
# io package RDFWriter
qualityassesment = rdf.packagesDict["qualityassesment"].QualityAssessmentOperations(rdf.triples)
print("QualityAssessmentOperations class methods: ")
print(dir(qualityassesment))
assesmentTriples = qualityassesment.assessAmountOfTriples()
print("Triples assesment: ", assesmentTriples)
assesmentCoverage = qualityassesment.assessCoverageDetail()
print("Coverage scope assesment: ", assesmentCoverage)
# Stop SparkContext to prevent overloading
sc.stop()