# TECHNICAL CHALLENGE

## The Challenge

We want to build a reference map on a website and understand which will be the most viewed by users when browsing.

For this we will make a crawler to help us get this information. Then, with the data obtained, we will train a model against historical data.

A crawler is a tool that allows us to enter a link and obtain information about it, for example, if the link is active or not.

In the case of this exercise, this software will allow us to evaluate the HTML response, parse it and obtain the links that are referenced within it.

In addition, this crawler will re-execute this procedure for each link it finds after this process, putting together a map like the following:

![picture 1](images/854731ea7f96e0a8c518ddd5f3c5e5ce7077b277a76d97dbedf0420461bb99da.png)  

Our challenge will be to count the number of references (“appearences”) that we find of a link from other sources.

In the example case, the link https://www.google.com/doodles/ it has 2 "appearences", while https://google.com/ has 0 "appearences" (since no other page is referencing it).

Understanding that the growth of this process is exponential (and potentially infinite), at the beginning of the process will be defined a maximum degree of depth N, which we can reach. 

That is, we will stop the process when reaching the referenced link more than N steps after the initial link.

### First Part: Generation of Features

In the first instance, the objective is to build a project that has the ability to crawl the different links from a base set and persist, for each link, **how many different references (appearences)** of external pages were found. 

The maximum level, N, of depth of the crawler is defined at the beginning of the process:

![picture 2](images/dab11824e73f82c0df9dd00063da1d86cbddf49374235969b7007b85bd3c7b01.png)  

In addition, this information can be enriched for each link with the information that it deems necessary to store.

Once the map is finished, for each link of the base set it is required to build a vector with at least 10 numerical characteristics based on said map, using the enrichment information previously obtained.

An example of a characteristic is "the number of characters in the link." 

These characteristics should only depend on information that can be obtained from the link -to be able to dynamically load them later-.

This vector must be saved in a new storage instance (table, document, file, etc):

![picture 3](images/63819b93d826e3fd065f676bf3d33de0569b815e77a9606e1fa01212209359c4.png)  

Each of these vectors must be persisted in the type of persistence that the user defines -unless it is forced by the conditions of the exercise-.

Finally, a REST API will be built such that it uses the defined storage and allows **obtaining the vector of features associated with a link**:

- If the link is in the database, answer the precalculated vector.
- If the link is not found in the database, the values corresponding to the vector must be calculated, inserted into the database and then returned. This vector will not have the number of external references calculated.

## My Achievements

I build the crawler using [Scrapy]('https://docs.scrapy.org/en/latest/index.html'), this crawler can be access in [meli_challenge/meli_challenge/spiders/extract_links.py](./meli_challenge/meli_challenge/spiders/extract_links.py)

I build the transformation using Scrapy Item Pipelines, more details can be access [here]('https://docs.scrapy.org/en/latest/topics/item-pipeline.html').

Scrapy Item Pipeline source code can be access at [meli_challenge/pipelines.py](./meli_challenge/meli_challenge/pipelines.py).

Item Pipeline will analyse all the scrapped links and count the appearences.

I don't build the REST API yet, but I created a Jupyter Notebook to created Vectors.

The Jupyter Notebook can be access at [vector-analytics.ipynb](./vector-analytics.ipynb).

### TO-DO List

- Build the challenge REST API.