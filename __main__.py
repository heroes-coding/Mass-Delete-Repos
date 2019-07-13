import requests, sys

unwanted_substring = sys.argv[1]
github_token = sys.argv[2]
headers = {'Authorization': 'token {}'.format(github_token)}

forked = []
page_num = 0

while True:
    print("Getting repos {}-{}".format(page_num*100, (page_num+1)*100-1))
    repo_data = requests.get("https://api.github.com/user/repos?per_page=100&page={}".format(page_num),headers=headers)
    page_of_repos =  repo_data.json()
    print("Got {} repos".format(len(page_of_repos)))
    forked.extend([repo["full_name"] for repo in page_of_repos if repo['fork'] and not repo["full_name"] in forked])
    if len(page_of_repos) == 0 or len(page_of_repos) < 100:
        break
    page_num += 1


to_delete = []
print("Checking for unwanted repos with a parent that has {} as part of its name...".format(unwanted_substring))
for repo_name in forked:
    detailed_repo = requests.get("https://api.github.com/repos/{}".format(repo_name), headers=headers).json()
    if unwanted_substring in detailed_repo["parent"]["full_name"]:
        to_delete.append(repo_name)

print("Are you sure you want to delete the following repos?\n\n{}\n".format( "\n".join(to_delete)))
command = input('Type in [y] plus [Enter] for yes, or anything else for no:\n')

if not command == "y":
    print("you typed '{}', bye bye!".format(command))
    sys.exit(0)

print("Deleting unwanted repos...")
for repo in to_delete:
    url = "https://api.github.com/repos/{}".format(to_delete)
    response = requests.delete(url,headers=headers)
    print(response.status_code,repo['url'])

