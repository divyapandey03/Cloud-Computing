
# Introduction:


![download](https://user-images.githubusercontent.com/23255126/208321724-b5bb9de0-16b0-4f6a-a711-55bbf744bee0.png)

GraphFrames is a package for Apache Spark that provides a DataFrame-based API for working with graph data. It is designed to make it easy to perform graph analytics on large-scale data using Spark.

GraphX is another graph processing library for Apache Spark. It provides a set of high-level APIs for graph computation and can be used to perform tasks such as graph filtering, vertex and edge manipulation, and graph traversal. GraphX also includes a collection of pre-built graph algorithms and utilities for graph visualization.

oth GraphFrames and GraphX are useful tools for working with graph data in Spark. However, GraphFrames is generally easier to use and more efficient, as it is built on top of the DataFrame API, which is more optimized for large-scale data processing.

<img width="249" alt="d3" src="https://user-images.githubusercontent.com/23255126/208321711-de315ff2-f1ef-4b2f-a838-186243a8ae0b.png">


<img width="240" alt="d2" src="https://user-images.githubusercontent.com/23255126/208321718-73cf9c6d-6d5d-4fa9-b7fd-3601e7f5157c.png">


<img width="247" alt="d1" src="https://user-images.githubusercontent.com/23255126/208321722-e700c330-aa13-45e9-8886-3d71d1a2254b.png">

# Installation Steps:

## Create the Vitual Machine on GCP and SSH into it:
<img width="461" alt="k1" src="https://user-images.githubusercontent.com/23255126/208321867-eb18befe-7479-4141-b9bb-9b6e225cef54.png">

## Install Java:

- sudo apt-get update
- sudo apt-get install openjdk-11-jdk


<img width="476" alt="g2" src="https://user-images.githubusercontent.com/23255126/208321906-7e458e9f-415f-4d44-bba3-9e27d538dbf1.png">

## Install Spark and Unpack it:


<img width="485" alt="g1" src="https://user-images.githubusercontent.com/23255126/208321934-021463a4-cd05-4ca7-9a60-c18881521df8.png">


## Create graphX directory and then prepare person.csv and relationship.csv file into graphX directory

- mkdir graphX


<img width="322" alt="g3" src="https://user-images.githubusercontent.com/23255126/208321953-95cb7b4e-e542-41d0-9d92-5acf27b5b6cd.png">

## Install Numpy Library: 
- sudo apt install python3-pip
- pip3 install numpy

## Prepare for the Code:
- graphX.py
Download Link:
https://github.com/divyapandey03/Cloud-Computing/blob/main/Apache%20Spark%20%2B%20GraphFramse%20%2B%20GraphX/graphX.py

## Download GraphFrames jar file:
   https://repos.spark-packages.org/graphframes/graphframes/0.8.2-spark3.1-s_2.12/graphframes-0.8.2-spark3.1-s_2.12.jar
   
## Submit PySpark Job:

- spark-submit --packages graphframes:graphframes:0.8.2-spark3.1-s_2.12 pyspark_graphX.py



