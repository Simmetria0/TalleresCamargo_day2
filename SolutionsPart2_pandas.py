#PART 2

1) Solution:
desc = reviews.description

or

desc = reviews["description"]

desc is a pandas Series object, with an index matching the reviews DataFrame. In general, when we select a single column from a DataFrame, we'll get a Series.


2) Solution

first_description = reviews.description.iloc[0]

Note that while this is the preferred way to obtain the entry in the DataFrame, many other options will return a valid result, such as reviews.description.loc[0], reviews.description[0], and more!

3) Solution:

first_descriptions = reviews.description.iloc[:10]

Note that many other options will return a valid result, such as desc.head(10) and reviews.loc[:9, "description"].


4) Solution:

cols = ['country', 'province', 'region_1', 'region_2']
indices = [0, 1, 10, 100]
df = reviews.loc[indices, cols]


5) Solution:

italian_wines = reviews[reviews.country == 'Italy']


6) Solution:

top_oceania_wines = reviews.loc[
    (reviews.country.isin(['Australia', 'New Zealand']))
    & (reviews.points >= 95)


7) Solution:
median_points = reviews.points.median()


8) Solution:
countries = reviews.country.unique()


9) Solution:
reviews_per_country = reviews.country.value_counts()

10) Solution:
centered_price = reviews.price - reviews.price.mean()


11) Solution:
bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']


12) Solution:
n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])


Solution:
def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(stars, axis='columns')





