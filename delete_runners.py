#!/usr/bin/env python3

import requests
import os
import gitlab

# UPDATE THESE FOR YOUR CONFIGURATION
gitlab_url = 'https://gitlab.com'

token = os.environ['GITLAB_TOKEN']

kill_string = 'my-runner'

# LOGIC

gl = gitlab.Gitlab(gitlab_url, private_token=token)

runners = gl.runners.list()

print()
for runner in runners:
    print("Checking " + str(runner.id) + " - " + runner.description)
    if runner.description == kill_string:
        run = gl.runners.get(runner.id)
        run.delete()
        print("Deleted " + str(runner.id))
    else:
        print("Not Deleting " + str(runner.id) + " - " + runner.description)
    print()