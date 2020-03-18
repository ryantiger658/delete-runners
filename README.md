# Delete GitLab Runners
A quick script to delete GitLab runners that match a particular string

I was a dummy and had a runner registration loop causing me to have too many runners. The web interface is a pain to delete runners so I wrote a quick script to do it for me.

## To use

Update the variables for the name string, and your GitLab server

```
export GITLAB_TOKEN=YOUR_TOKEN_HERE
pip install -r requirements.txt
./delete_runners.py
```
