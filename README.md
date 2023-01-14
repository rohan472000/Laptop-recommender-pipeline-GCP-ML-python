# Laptop-recommender-pipeline-GCP-ML-python
This is a project which takes data of purchased laptops as .csv files and using ML algorithm, it recommends the laptops.

In this project `surprise` lin=b is used, `surprise` is a Python scikit for building and analyzing recommender systems that deal with explicit rating data.

Surprise was designed with the following purposes in mind:
    Give users perfect control over their experiments.
    Alleviate the pain of Dataset handling.
    Provide various ready-to-use prediction algorithms 
    Make it easy to implement new algorithm ideas.
    Provide tools to evaluate, analyse and compare the algorithms' performance.
    The name SurPRISE (roughly :) ) stands for Simple Python RecommendatIon System Engine.
    
`GCP` services such as `storage` is used to store and retrieve data files. so, you must have a `GCP` account with required permissions.

`apache-airflow` is used to schedule the task at specified time interval.
