
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


## Output:


<img width="433" alt="l3" src="https://user-images.githubusercontent.com/23255126/208322136-4cfaa3fa-9c2f-44ce-aca4-464820362b58.png">
<img width="272" alt="l4" src="https://user-images.githubusercontent.com/23255126/208322137-385330e8-27c4-4026-9b10-6de263381e35.png">
<img width="389" alt="l5" src="https://user-images.githubusercontent.com/23255126/208322138-9dc438ed-fd31-4842-bac2-684c82bd7a28.png">
<img width="257" alt="l6" src="https://user-images.githubusercontent.com/23255126/208322139-cba54e5b-d97b-4238-8b39-cf66bee99429.png">
<img width="433" alt="l7" src="https://user-images.githubusercontent.com/23255126/208322140-53596c96-f98d-452e-9078-892ece1c86f8.png">
<img width="435" alt="l8" src="https://user-images.githubusercontent.com/23255126/208322141-c30b184b-2fbe-43ce-910b-2e1a5f83dacb.png">
<img width="422" alt="l9" src="https://user-images.githubusercontent.com/23255126/208322142-c2bfea54-b2e2-4e9b-9269-751a7d34ecbf.png">
<img width="502" alt="l10" src="https://user-images.githubusercontent.com/23255126/208322143-ad61cd19-dc10-4c12-bf87-78052342c937.png">
<img width="523" alt="l11" src="https://user-images.githubusercontent.com/23255126/208322144-623f4750-6996-46a5-bec9-a5e0fdf102f5.png">
<img width="509" alt="l12" src="https://user-images.githubusercontent.com/23255126/208322145-f20d1fd9-39d9-4330-a7cf-5d6bf313b256.png">
<img width="421" alt="l1" src="https://user-images.githubusercontent.com/23255126/208322147-3f57b686-2c2a-4e29-9cdc-c13676f677ec.png">
<img width="305" alt="l2" src="https://user-images.githubusercontent.com/23255126/208322148-f8f6141c-ce98-40fc-a0f1-0de341c97b8b.png">


