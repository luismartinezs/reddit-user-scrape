import json
from datetime import datetime

# Load the data from the JSON file
with open('my_reddit_activity.json', 'r') as f:
    data = json.load(f)

# Extract posts and comments, convert timestamps, and combine them
activities = [
    (datetime.fromtimestamp(item['created']), item['selftext'])
    for item in data['posts']
] + [
    (datetime.fromtimestamp(item['created']), item['body'])
    for item in data['comments']
]

# Sort by date
activities.sort()

# Write the combined activities to a new file with dates
with open('combined_activities_by_date.txt', 'w') as f:
    for date, text in activities:
        if text:
          f.write(f"{date.strftime('%Y-%m-%d')}\n{text}\n\n")

print('combined_activities_by_date.txt has been created with the combined selftext and body values ordered by date.')
