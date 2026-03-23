import requests

git_username = str(input("Enter your GitHub username: "))

url = "https://api.github.com/users/" + git_username + "/events"
print(url)

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

else:
    print("Erro:", response.status_code)

def count_pushes():
    count = 0
    for i in data:

        if i ["type"] == "PushEvent" and i ["repo"]["name"]:
            count += 1
    return count


def repos_created():
    count = 0
    for i in data:

        if i["type"] == "CreateEvent" and i["repo"]["name"]:
            count += 1
    return count
print(git_username + " pushed to " +str(count_pushes()) + " repositories")
print(git_username + " created " +str(repos_created()) + " repositories")