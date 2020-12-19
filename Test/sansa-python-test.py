#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 03:17:38 2020

@author: erce
"""
# Boiler plate stuff to start the module
import jpype
import jpype.imports
from jpype.types import *

def init_jvm(jvmpath=None):
    if jpype.isJVMStarted():
        print('Jpype is started.')
        return
    # Launch the JVM
    jpype.startJVM(classpath=['../sansa-rdf-spark_2.11-0.7.1.jar'])

init_jvm()

#package = jpype.JPackage("net.sansa_stack.rdf.spark.io.package")
#logging = jpype.JPackage("net")
#from net.sansa_stack.rdf.spark.streaming import FileReader
from net.sansa_stack.rdf.spark.io import package
#package()
#a = NTripleReader()
#a = FileReader()
#a = RDFDataSource()
#dataFrameWriter = jpype.JClass("net.sansa_stack.rdf.spark.io.package$RDFDataFrameWriter")


#obj = logging.Logging()
#print(obj)
#package.RDFReader()
#package.RDFWriter()
#package.NTripleReader()
#a = jpype.JClass("net.sansa_stack.rdf.spark.io.NTripleReader")
#aClass = a()