"""
Accept a list of tweets and generate a tweet_cosine_similarities.csv
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def find_relations(tweets, feature_extraction, tdm):
    """
    Go through all the tweets and create a map for each tweet and
    there cosine similarities
    """
    # a list of dictionaries containing list of related tweets and the
    # cosine value
    cosine_value_map = []
    for tweet in tweets:
        temp = {tweet:[]}
        query = feature_extraction.transform([tweet])
        cosine_similarities = linear_kernel(query, tdm).flatten()
        related_docs_indices = cosine_similarities.argsort()[:-5:-1]
        for index in related_docs_indices:
            temp[tweet].append((tweets[index], cosine_similarities[index]))
        cosine_value_map.append(temp)
    return cosine_value_map

def main():
    """
    Use the TfidfVectorizer function to form a TDM and prepare a
    cosine_similarities csv
    """
    tweets = list(open('tweets.txt', 'r+'))
    feature_extraction = TfidfVectorizer(analyzer="word")
    tdm = feature_extraction.fit_transform(tweets)
    relations = find_relations(tweets, feature_extraction, tdm)
    data = {'tweet_one':[], 'tweet_two':[], 'cosine_relation':[]}
    for item in relations:
        for key in item.keys():
            for processed_data in item[key]:
                if key != processed_data[0]:
                    data['tweet_one'].append(key)
                    data['tweet_two'].append(processed_data[0])
                    data['cosine_relation'].append(processed_data[1])
    pd.DataFrame(data).to_csv('tweet_cosine_similarities.csv', index=False)

if __name__ == "__main__":
    main()
