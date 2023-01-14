from surprise import *


def print_recommendations():
    user_id = 'me'
    user_laptops = trainset.ur[trainset.to_inner_uid(user_id)]
    laptops_to_ignore = [laptop for (laptop, _) in user_laptops]
    top_n = 10
    algo = SVD()
    predicted_laptops = algo.get_top_n(top_n)
    print("Recommended laptops for user {}:".format(user_id))
    for laptop_id, rating in predicted_laptops:
        if laptop_id not in laptops_to_ignore:
            print("- Laptop ID: {}, predicted rating: {:.2f}".format(laptop_id, rating))
