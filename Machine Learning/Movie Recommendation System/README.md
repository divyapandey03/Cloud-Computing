# Movie Recommendation with MLlib:
Recommender System is an information filtering tool that seeks to predict which product a user will like, and based on that, recommends a few products to the users. For example, Amazon can recommend new shopping items to buy, Netflix can recommend new movies to watch, and Google can recommend news that a user might be interested in. The two widely used approaches for building a recommender system are content-based filtering (CBF) and collaborative filtering (CF).


![stars-movies-1200x670-1](https://user-images.githubusercontent.com/23255126/202930904-6437addf-d22c-43ef-9d99-aa914c7e14b8.jpg)


## Design:

We use Collaborative filtering which is commonly used for recommender systems. These techniques aim to fill in the missing entries of a user-item association matrix, in our case, the user-movie rating matrix. MLlib currently supports model-based collaborative filtering, in which users and products are described by a small set of latent factors that can be used to predict missing entries. In particular, we implement the alternating least squares (ALS) algorithm to learn these latent factors.



<img width="268" alt="k8" src="https://user-images.githubusercontent.com/23255126/202931363-6c7c5859-7cf9-404b-89fb-5b35fe316474.png">


For example, if the user ‘A’ likes ‘Batman Begins’, ‘Justice League’ and ‘The Avengers’ while the user ‘B’ likes ‘Batman Begins’, ‘Justice League’ and ‘Thor’ then they have similar interests because we know that these movies belong to the super-hero genre. So, there is a high probability that the user ‘A’ would like ‘Thor’ and the user ‘B’ would like The Avengers’.

<img width="525" alt="k6" src="https://user-images.githubusercontent.com/23255126/202931069-44e833ea-7a47-4f34-98e6-d7b30f39a9c2.png">


## Implementation(Google Colab):
- Download movielens.ipynb
- https://colab.research.google.com/notebooks/intro.ipynb#recent=true
- Upload movies.csv,ratings.csv and tags.csv file
- Run All
- Download movielens.py file

![Screenshot (6)](https://user-images.githubusercontent.com/23255126/202949117-083b7be7-c9e0-46f0-ba89-ed0cc48ee164.png)

![Screenshot (4)](https://user-images.githubusercontent.com/23255126/202951992-21b381d1-cf02-47ba-b454-a211a63a36a7.png)





## Implementation(Google Cloud Dataproc):
- Create  Google cloud Dataproc Cluster


<img width="599" alt="k2" src="https://user-images.githubusercontent.com/23255126/202950034-58c190ef-b906-4a9f-af3d-e2d8c6aec19f.png">

- SSH into it
- Upload the movies.csv and ratings.csv file
- Upload movielens.py file
### Create the HDFS Directory:
   - hdfs dfs -mkdir hdfs:///movielens
   
### Copy the movies.csv and ratings.csv file into HDFS Directory:
  - hdfs dfs -put movies.csv hdfs:///movielens
  - hdfs dfs -put ratings.csv hdfs:///movielens
  
  ### Run:
        spark-submit movielens.py
        

<img width="508" alt="g9" src="https://user-images.githubusercontent.com/23255126/202950872-7194e51d-c1d9-4290-ad1f-a6a80f69cfce.png">


## Output:

### Google Colab:
<img width="643" alt="k1" src="https://user-images.githubusercontent.com/23255126/202951018-9990a33b-fee5-4ba2-8829-021a763f6d82.png">

<img width="599" alt="k2" src="https://user-images.githubusercontent.com/23255126/202951051-fc160bfb-a4d6-4728-b67a-0491b9ad0f58.png">

<img width="944" alt="k3" src="https://user-images.githubusercontent.com/23255126/202951071-1b2b985b-726b-44f4-8e7a-ef096714e494.png">

### Google Cloud DataProc:


<img width="217" alt="g6" src="https://user-images.githubusercontent.com/23255126/202951145-c24f8b83-6d43-47ed-9303-b02af1b304f6.png">



<img width="462" alt="g7" src="https://user-images.githubusercontent.com/23255126/202951153-be44e212-c33c-4030-8338-24c365b68b90.png">


<img width="435" alt="g8" src="https://user-images.githubusercontent.com/23255126/202951161-622441d0-dc42-4ac5-bd90-20c8826fc106.png">

## Presentation Link: 
https://docs.google.com/presentation/d/1yprDUy-fmjwhP5075syXjG0xq6HCSpFK/edit?usp=sharing&ouid=115854624782305611491&rtpof=true&sd=true
