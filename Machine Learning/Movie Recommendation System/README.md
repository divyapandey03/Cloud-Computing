# Intruduction:
Recommender System is an information filtering tool that seeks to predict which product a user will like, and based on that, recommends a few products to the users. For example, Amazon can recommend new shopping items to buy, Netflix can recommend new movies to watch, and Google can recommend news that a user might be interested in. The two widely used approaches for building a recommender system are content-based filtering (CBF) and collaborative filtering (CF).


![stars-movies-1200x670-1](https://user-images.githubusercontent.com/23255126/202930904-6437addf-d22c-43ef-9d99-aa914c7e14b8.jpg)


## Design:

We use Collaborative filtering which is commonly used for recommender systems. These techniques aim to fill in the missing entries of a user-item association matrix, in our case, the user-movie rating matrix. MLlib currently supports model-based collaborative filtering, in which users and products are described by a small set of latent factors that can be used to predict missing entries. In particular, we implement the alternating least squares (ALS) algorithm to learn these latent factors.
<img width="691" alt="k7" src="https://user-images.githubusercontent.com/23255126/202931001-22b11e5c-fa28-4eeb-9a7f-35aa7ec27fbf.png">

