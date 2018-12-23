'''
Created on Dec 19, 2018

@author: LAC42787
'''
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate() 
sc = spark.sparkContext
myRdd = sc.parallelize([1,2,3,4])
print(myRdd.take(5))