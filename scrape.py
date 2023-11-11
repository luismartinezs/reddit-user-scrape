import os
import praw
import json
from dotenv import load_dotenv

load_dotenv()

# Fill these in with your details
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
user_agent = 'script by /u/yourusername'
username = 'saito200'
password = os.getenv("REDDIT_PASSWORD")

# Authenticate to Reddit
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent,
                     username=username,
                     password=password)

# Function to get all posts and comments by a user
def get_user_activity(reddit_user):
    activity = {
        'posts': [],
        'comments': []
    }
    for submission in reddit_user.submissions.new(limit=None):
        activity['posts'].append({
            'title': submission.title,
            'selftext': submission.selftext,
            'created': submission.created,
            'url': submission.url
        })
    for comment in reddit_user.comments.new(limit=None):
        activity['comments'].append({
            'body': comment.body,
            'created': comment.created,
            'permalink': comment.permalink
        })
    return activity

# Get your activity
my_activity = get_user_activity(reddit.redditor(username))

# Write to a file
filename = 'my_reddit_activity.json'
with open(filename, 'w') as f:
    json.dump(my_activity, f, indent=4)

print(f'All posts and comments have been saved to {filename}')
