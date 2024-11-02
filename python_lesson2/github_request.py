import requests

url = "https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>12000"
headers = {"Accept" : "application/vnd.github.v3+json"}

r = requests.get(url, headers=headers)
print(f"status code : {r.status_code}")
response_dict = r.json()
print(response_dict.keys())

print(f"Total repos is: {response_dict['total_count']}")
print(f"The true result is : {not response_dict['incomplete_results']}")

repo_dict = response_dict['items']
print(f"The repos details are: {len(repo_dict)}")

repo_info = repo_dict[4]
print(f"\nKeys: {len(repo_info)}")

for key in sorted(repo_info.keys()):
    print(key)

print(f"The owner is : {repo_info['owner']['url']}")
     