"""
Process the tweets.json file and get the tweets text in 1 file.
"""
def main():
    """
    Generate tweets.txt containing only text of tweet
    """
    tweets_text_file = open('tweets.txt', 'w+')
    # get the tweets in list form
    with open('tweets.json', 'r+') as tweets_data:
        for line in tweets_data:
            for item in line.split(','):
                if "text" in item:
                    tweet = item.replace('text', '')
                    tweet = tweet.strip("\"\":")
                    tweets_text_file.write(tweet)
                    tweets_text_file.write('\n')
                    break

if __name__ == "__main__":
    main()
