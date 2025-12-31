import pandas as pd
import json
import random
import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the CSV file
file_path = os.path.join(script_dir, 'Food_Recipe.csv')

def searchAlg(searchPhrase):
    data = pd.read_csv(file_path)

    searchPhrases = searchPhrase.split(" ")

    filtered_data = data

    for phrase in searchPhrases:
        filtered_data = filtered_data[filtered_data['description'].str.contains(phrase, case=False)]

    if "vegetarian" in searchPhrase.lower():
        filtered_data = filtered_data[~filtered_data['description'].str.contains('Non Vegetarian', case=False)]

    if len(filtered_data) > 25:
        filtered_data = filtered_data.head(25)

    filtered_data = filtered_data.fillna("data not available")

    recipes_dict = {}
    for idx, row in filtered_data.iterrows():
        recipes_dict[idx] = row.to_dict()

    recipes_json = json.dumps(recipes_dict, ensure_ascii=False, indent=4)

    print(recipes_json)

    return recipes_json

def randomAlg():
    data = pd.read_csv(file_path)

    random_nums = []

    while len(random_nums) < 10:
        random_num = random.randint(0, len(data) - 1)
        if random_num not in random_nums:
            random_nums.append(random_num)

    filtered_data = data.iloc[random_nums]

    recipes_dict = {}
    for idx, row in filtered_data.iterrows():
        recipes_dict[idx] = row.to_dict()

    # Convert dictionary to JSON string
    recipes_json = json.dumps(recipes_dict, ensure_ascii=False, indent=4)

    return recipes_json


"""inputSearchPhrase = input("Enter search phrases separated by space: ")
searchAlg(inputSearchPhrase)"""