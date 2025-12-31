import pandas as pd
searches = ["rice", "indian", "lunch", "vegetarian"]

data = pd.read_csv("recipes.csv")
filtered_data = data[
    (data['name'].str.contains(searches[0], case=False)) &
    (data['cuisine'].str.contains(searches[1], case=False)) &
    (data['course'].str.contains(searches[2], case=False)) &
    (data['diet'].str.contains(searches[3], case=False)) &
    (~data['description'].str.contains('shrimp', case=False))
]

#print(filtered_data)