items = {
    "Python Course": ["python", "programming", "ai"],
    "Web Development": ["html", "css", "javascript"],
    "Machine Learning": ["python", "ai", "data"],
    "Cloud Computing": ["cloud", "aws", "devops"]
}

user_interests = input("Enter your interests separated by commas: ").lower().split(",")

user_interests = [i.strip() for i in user_interests]

recommendations = []

for item, tags in items.items():
    score = len(set(user_interests) & set(tags))
    recommendations.append((item, score))

recommendations.sort(key=lambda x: x[1], reverse=True)

print("\nRecommended Items:")
for item, score in recommendations:
    if score > 0:
        print(f"{item} (Match Score: {score})")