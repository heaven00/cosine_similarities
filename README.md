How this works
==============

We are going to implement a simple and yet effective model called Vector Space Model (VSM).

In this model what we basically do is project the sentences, in this case tweets, in an n-dimensional space and see the angle between them and then we take the cosine of it. This value is called a cosine similarity, the value varies between 0,1. Thus the vectors near 0 (cos 90)are less similar to vectors near 1 (cos 0).

Implementation
--------------

We are using scikit's TfidfVectorizer to project the tweets as vectors and calculating the cosine similarities between these vectors and storing in a file.
This is in no way highly computatinal efficient, so bear with this old but useful code.

How To use
==========

You need to set this up a little bit first.

1. In "*config.py*" file you need to add your required twitter keys so that the program can access the twitter streaming api.

2. Under "*stream.py*" you can choose between two functions, either search for a query #hashtag or get stream of an user.   



After you are done with step 1 and 2. Run,

        python run.py
        
this will execute a program that will collect tweets from the the streaming API every 9 seconds, you can change time interval in "*run.py*" to anything you like.

This will output a csv file called "*tweet_cosine_similarities.csv*" that will contain the tweets gathered and their cosine similarities.


Requirements
------------
1. TwitterAPI
2. Pandas
3. sklearn