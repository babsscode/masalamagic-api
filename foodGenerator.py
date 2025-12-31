import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import os

import numpy as np
from operator import itemgetter
from flask import jsonify

# get directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# construct the path to the CSV file
file_path = os.path.join(script_dir, 'Food_Recipe.csv')

def calc_cos_sim(df, phrase, filename='cosine_similarity.npz'):
    tfidf_vectorizer = TfidfVectorizer()

    # make all content into one
    df['content'] = (
            df['name'].fillna('') + ' ' +
            df['description'].fillna('') + ' ' +
            df['cuisine'].fillna('') + ' ' +
            df['course'].fillna('') + ' ' +
            df['diet'].fillna('') + ' ' +
            df['ingredients_name'].fillna('') + ' ' +
            df['instructions'].fillna('')
    )

    # fit & transform the dataframe content w/ tfidf vectorizer
    tfidf_matrix_df = tfidf_vectorizer.fit_transform(df['content'])

    # fit & transform the phrase w/ tfidf vectorizer
    tfidf_matrix_phrase = tfidf_vectorizer.transform([phrase])


    # find cosine similarity between foods and phrase
    cosine_sim = cosine_similarity(tfidf_matrix_df, tfidf_matrix_phrase)

    return cosine_sim.flatten()

def get_recs(phrase, offset):
    final_json = {}

    if phrase == "random":
        final_json = random_recs()
        return final_json
    # make data into data frame
    data = pd.read_csv(file_path)
    df = pd.DataFrame(data)

    cos_sim_list = calc_cos_sim(df, phrase)

    # sort in highest to lowest
    orig_pos, cos_sim_sorted = zip(*sorted(enumerate(cos_sim_list), key=lambda i: i[1], reverse=True))
    print(len(orig_pos))
    if offset < (len(orig_pos)):
        orig_pos = orig_pos[0:offset]
    else:
        orig_pos = orig_pos[0:(len(orig_pos) - 1)]

    #cos_sim_sorted = cos_sim_sorted[0:10:20]

    # get name corresponding to index from df
    for id, i in enumerate(orig_pos):
        nan_message = "data not available"
        food_json = {
            "id": id,
            "index": i,
            "description": df['description'].fillna(nan_message).iloc[i],
            "cuisine": df['cuisine'].fillna(nan_message).iloc[i],
            "course": df['course'].fillna(nan_message).iloc[i],
            "diet": df['diet'].fillna(nan_message).iloc[i],
            "ingredients": df['ingredients_name'].fillna(nan_message).iloc[i],
            "imageUrl": df['image_url'].fillna(nan_message).iloc[i],
            "websiteUrl": "https://www.youtube.com/results?search_query="+ df['name'].fillna(nan_message).iloc[i]
        }
        final_json[df['name'].fillna(nan_message).iloc[i]] = food_json
    return final_json

# with food name in json data values instead of as the key for website api purposes
def get_recs2(phrase, offset):
    final_json = {}

    if phrase == "random":
        final_json = random_recs2()
        return final_json
    # make data into data frame
    data = pd.read_csv(file_path)
    df = pd.DataFrame(data)

    cos_sim_list = calc_cos_sim(df, phrase)

    # sort in highest to lowest
    orig_pos, cos_sim_sorted = zip(*sorted(enumerate(cos_sim_list), key=lambda i: i[1], reverse=True))
    print(len(orig_pos))
    if offset < (len(orig_pos)):
        orig_pos = orig_pos[0:offset]
    else:
        orig_pos = orig_pos[0:(len(orig_pos) - 1)]

    #cos_sim_sorted = cos_sim_sorted[0:10:20]

    # get name corresponding to index from df
    for id, i in enumerate(orig_pos):
        nan_message = "data not available"
        food_json = {
            "id": id,
            "index": i,
            "foodName": df['name'].fillna(nan_message).iloc[i],
            "description": df['description'].fillna(nan_message).iloc[i],
            "cuisine": df['cuisine'].fillna(nan_message).iloc[i],
            "course": df['course'].fillna(nan_message).iloc[i],
            "diet": df['diet'].fillna(nan_message).iloc[i],
            "ingredients": df['ingredients_name'].fillna(nan_message).iloc[i],
            "imageUrl": df['image_url'].fillna(nan_message).iloc[i],
            "websiteUrl": "https://www.youtube.com/results?search_query="+ df['name'].fillna(nan_message).iloc[i]
        }
        final_json[df['name'].fillna(nan_message).iloc[i]] = food_json
    return final_json

def random_recs():
    # make data into data frame
    data = pd.read_csv(file_path)
    df = pd.DataFrame(data)

    random_nums = []
    for i in range(10):
        random_nums.append(random.randint(0, len(df)))
    random_nums = set(random_nums)

    final_json = {}
    # get name corresponding to index from df
    for id, i in enumerate(random_nums):
        nan_message = "data not available"
        food_json = {
            "id": id,
            "index": i,
            "description": df['description'].fillna(nan_message).iloc[i],
            "cuisine": df['cuisine'].fillna(nan_message).iloc[i],
            "course": df['course'].fillna(nan_message).iloc[i],
            "diet": df['diet'].fillna(nan_message).iloc[i],
            "ingredients": df['ingredients_name'].fillna(nan_message).iloc[i],
            "imageUrl": df['image_url'].fillna(nan_message).iloc[i],
            "websiteUrl": "https://www.youtube.com/results?search_query="+ df['name'].fillna(nan_message).iloc[i]
        }
        final_json[df['name'].fillna(nan_message).iloc[i]] = food_json
    return final_json

# with food name in json data values instead of as the key for website api purposes
def random_recs2():
    # make data into data frame
    data = pd.read_csv(file_path)
    df = pd.DataFrame(data)

    random_nums = []
    for i in range(10):
        random_nums.append(random.randint(0, len(df)))
    random_nums = set(random_nums)

    final_json = {}
    # get name corresponding to index from df
    for id, i in enumerate(random_nums):
        nan_message = "data not available"
        food_json = {
            "id": id,
            "index": i,
            "foodName": df['name'].fillna(nan_message).iloc[i],
            "description": df['description'].fillna(nan_message).iloc[i],
            "cuisine": df['cuisine'].fillna(nan_message).iloc[i],
            "course": df['course'].fillna(nan_message).iloc[i],
            "diet": df['diet'].fillna(nan_message).iloc[i],
            "ingredients": df['ingredients_name'].fillna(nan_message).iloc[i],
            "imageUrl": df['image_url'].fillna(nan_message).iloc[i],
            "websiteUrl": "https://www.youtube.com/results?search_query="+ df['name'].fillna(nan_message).iloc[i]
        }
        final_json[df['name'].fillna(nan_message).iloc[i]] = food_json
    return final_json

# Test with different inputs
user_input = {
    "cuisine": "south indian",
    "course": "lunch or main course",
    "diet": "vegetarian",
    "ingredients_name": "cheese, milk, tomato, potato, lemon",
    "prep_time_mins": " ",
    "cook_time_mins":" ",
    "description": "spicy medium savory",
}

#print(get_recs(input("I'm craving something... ")))
#print(random_recs())
