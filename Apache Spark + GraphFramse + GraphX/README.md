
# Introduction:


![download](https://user-images.githubusercontent.com/23255126/208321724-b5bb9de0-16b0-4f6a-a711-55bbf744bee0.png)

GraphFrames is a package for Apache Spark that provides a DataFrame-based API for working with graph data. It is designed to make it easy to perform graph analytics on large-scale data using Spark.

GraphX is another graph processing library for Apache Spark. It provides a set of high-level APIs for graph computation and can be used to perform tasks such as graph filtering, vertex and edge manipulation, and graph traversal. GraphX also includes a collection of pre-built graph algorithms and utilities for graph visualization.

 GraphFrames and GraphX are useful tools for working with graph data in Spark. However, GraphFrames is generally easier to use and more efficient, as it is built on top of the DataFrame API, which is more optimized for large-scale data processing.

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

**GraphFrame:**


<img width="421" alt="l1" src="https://user-images.githubusercontent.com/23255126/208322282-16f6ebcf-a355-4fa3-b679-cf71a8e0102f.png">
<img width="305" alt="l2" src="https://user-images.githubusercontent.com/23255126/208322283-ea3dbeb2-c617-4688-a67a-6663ba39353b.png">

**TriangleCount:**


<img width="433" alt="l3" src="https://user-images.githubusercontent.com/23255126/208322384-5d43a987-0ce2-4333-a3af-d8d743b4e098.png">


<img width="272" alt="l4" src="https://user-images.githubusercontent.com/23255126/208322390-bae79bf3-2386-4127-bf9c-965a3c8ea23c.png">

<img width="389" alt="l5" src="https://user-images.githubusercontent.com/23255126/208322391-3f0de915-0609-47cd-b3a9-a6107735eb25.png">

<img width="257" alt="l6" src="https://user-images.githubusercontent.com/23255126/208322397-1aaaac2a-b68b-4345-8d90-40a272a05595.png">

<img width="433" alt="l7" src="https://user-images.githubusercontent.com/23255126/208322401-77f58f07-8705-4b0c-9eb3-7618cd89b55d.png">

**PageRank:**

<img width="435" alt="l8" src="https://user-images.githubusercontent.com/23255126/208322445-d377a9b2-a44f-4a81-a596-364a0889f0d2.png">


<img width="422" alt="l9" src="https://user-images.githubusercontent.com/23255126/208322452-e5eac747-a986-46ca-855c-f1abe275137b.png">

**BFS:**


<img width="502" alt="l10" src="https://user-images.githubusercontent.com/23255126/208322515-4e5cd1a3-dc87-45ec-9d43-848fc667623a.png">

<img width="523" alt="l11" src="https://user-images.githubusercontent.com/23255126/208322517-b5721bc5-1f9f-46a0-8f30-8e0e335f9666.png">

<img width="509" alt="l12" src="https://user-images.githubusercontent.com/23255126/208322520-0f9b9f29-db7d-4b79-9276-88da4aff9b7f.png">

## Presentation Link:

- https://docs.google.com/presentation/d/1c6fvobNsz-KAFJ7mj4I5hVbbjDUebqDL/edit#slide=id.p18
