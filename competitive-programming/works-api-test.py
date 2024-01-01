#!/bin/python3

import math
import os
import random
import re
import sys
import json
import requests


#
# Complete the 'getUsernames' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER threshold as parameter.
# API URL: https://jsonmock.hackerrank.com/api/article_users?page=<pageNumber>
#
def getData():
    page = 1
    users = []
    next_page = True
    while next_page:
        url = f"https://jsonmock.hackerrank.com/api/article_users?page={page}"
        resp = requests.get(url)
        if resp.status_code != 200:
            return users
        data = resp.json()
        users.extend(data.get("data", []))
        total_page = data.get("total_pages", 0)
        page = page + 1
        next_page = page <= total_page
    return users

def getUsernames(threshold):
    data = getData()
    users = filter(lambda x: int(x['submission_count']) > threshold, data)
    result = [user.get("username", "") for user in users]
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    threshold = int(input().strip())

    result = getUsernames(threshold)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
