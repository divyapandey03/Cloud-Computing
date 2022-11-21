# Movie Recommendation with MLlib:
Recommender System is an information filtering tool that seeks to predict which product a user will like, and based on that, recommends a few products to the users. For example, Amazon can recommend new shopping items to buy, Netflix can recommend new movies to watch, and Google can recommend news that a user might be interested in. The two widely used approaches for building a recommender system are content-based filtering (CBF) and collaborative filtering (CF).


![stars-movies-1200x670-1](https://user-images.githubusercontent.com/23255126/202930904-6437addf-d22c-43ef-9d99-aa914c7e14b8.jpg)


## Design:

We use Collaborative filtering which is commonly used for recommender systems. These techniques aim to fill in the missing entries of a user-item association matrix, in our case, the user-movie rating matrix. MLlib currently supports model-based collaborative filtering, in which users and products are described by a small set of latent factors that can be used to predict missing entries. In particular, we implement the alternating least squares (ALS) algorithm to learn these latent factors.



<img width="268" alt="k8" src="https://user-images.githubusercontent.com/23255126/202931363-6c7c5859-7cf9-404b-89fb-5b35fe316474.png">


For example, if the user ‘A’ likes ‘Batman Begins’, ‘Justice League’ and ‘The Avengers’ while the user ‘B’ likes ‘Batman Begins’, ‘Justice League’ and ‘Thor’ then they have similar interests because we know that these movies belong to the super-hero genre. So, there is a high probability that the user ‘A’ would like ‘Thor’ and the user ‘B’ would like The Avengers’.

<img width="525" alt="k6" src="https://user-images.githubusercontent.com/23255126/202931069-44e833ea-7a47-4f34-98e6-d7b30f39a9c2.png">
