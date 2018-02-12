import os
import sys
import json
import time
import argparse
from tweepy import Cursor
from tweepy import error
from twitter_client import get_twitter_client
from retrying import retry

@retry(wait_exponential_multiplier=1000, wait_exponential_max=10000)
def tweet_pull(users,uCount,keywords,rcVal):
    count=0
    try:
        #fname = "user_timeline_{}.jsonl".format(users)
        for page in Cursor(client.user_timeline, screen_name=users, count=200).pages(16):
            for status in page:
                #print status
                #print status.split('."text":"')[1].split('","source')[0]
                hold=json.dumps(status._json)
                h=json.loads(hold)
                txt = ''.join((h["text"])).encode('utf-8').strip()
                #print txt
                for kw in keywords:
                    if kw in txt:
                        f.write(json.dumps(status._json)+"\n")
                        count=count+1 
        if count > 0:
            print("Found %d tweets with a keyword in them" % (count))
    except error.TweepError:
        print("Unable to pull user history, attempting to reconnect(%d)\n" % (rcVal))
        rcVal=rcVal+1
        raise
    return

def get_parser():
    parser = argparse.ArgumentParser(description="Tweet History Retriever")
    parser.add_argument("-k",
                        "--keywords",
                        dest="keywords",
                        help="Keywords to search for in tweets",
                        default='opiod')
    parser.add_argument("-o",
                        "--output",
                        dest="output",
                        help="Name of the output file",
                        default="tweet_history")
    return parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    filename = []
    keywords= args.keywords.split(',')
    for fn in os.listdir(os.getcwd()):
        if fn[-5:] == ".json":
            filename.append(fn.strip('\''))
    client = get_twitter_client()
    user = []
    with open("users.txt","r") as u:
        lns = u.readlines()
        for lines in lns:
            if not lines=='\n':
                user.append(lines.strip('\'').strip('\n'))
    for f in filename:
        #print f
        fcontent = file(f,"r")
        lines = fcontent.readlines()
        for line in lines:
            data=json.loads(line)
            user.append(data["user"]["screen_name"])
    user = list(set(user))
    #print user
    with open("users.txt","w") as uw:
        for users in user:
            uw.write("%s\n" % (users))
    uCount=1
    fname = args.output + ".jsonl"
    with open(fname, 'w') as f:
        for u in user:
            #try:
            print(str(uCount)+" of "+str(len(u))+"| Retrieving " + users + " history")
            rcVal=1
            tweet_pull(u, uCount, keywords, rcVal)
            #except error.TweepError:
            #    raise
            uCount=uCount+1