from CurlUtility import CurlUtility
import sys
import json
import argparse

parser = argparse.ArgumentParser(description='clones all the repo of my githubin local')
parser.add_argument('-u','--user', help='username', required=True)
parser.add_argument('-p','--passwd', help='password', required=True)
parser.add_argument('-s','--subdomain', help='subdomain', required=True)
args = parser.parse_args()

username = args.user
password = args.passwd
subdomain = args.subdomain

headers_dict = {'content-type': 'application/json','accept': 'application/json'}
auth_dict = {"user":username,"pass":password}
giturl = "https://%s.unfuddle.com/api/v1/repositories"%subdomain
print giturl

result = CurlUtility().curl(url=giturl,auth=auth_dict,headers= headers_dict)
all_repo_info = json.loads(result['content'])
repo_names = list()

for items in all_repo_info:
    repo_url = "https://%s:%s@%s.unfuddle.com/git/%s_%s/"%(username,password,subdomain,subdomain,items['abbreviation'])
    repo_names.append(repo_url)

with open("git_repo.txt",'w') as f:
    for items in repo_names:
        f.write(items+"\n")

