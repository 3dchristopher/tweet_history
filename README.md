# tweet_history
Makes use of the Tweepy Python package to retrieve the tweet histories of users found in .json tweet files, finding only those that contain specific keywords.
## Setup
In order to make use of the program, you must first generate Twitter API keys. Use this link to create a Twitter Application, and follow the instructions to create the four keys you need: [https://apps.twitter.com/](https://apps.twitter.com/)

Once you have your keys, rename the "config.txt" file to "config.py", and put each of the four keys in the variable lines within the "config.py" file.

`consumer_key = 'put your consumer key here'
consumer_secret = 'put your consumer secret key here'
access_token = 'put your access token here'
access_token_secret = 'put your access secret token here'`

## Compiling
**Important Note**: When this program runs, it will attempt to access **every** .json file in its directory. Make sure that you have only the .json files you wish to run the program on in the directory before starting.

**twitter_history.py** requires command line arguments in order to compile the program. The command takes the following arguments:

'python twitter_history.py --keywords=type,keywords,here --output=outputfilename'

If you want to search for multiple keywords, write each keyword with only a comma seperating them as shown above.

## Runtime
During the timespan that the program is actively pulling tweets, the command prompt will display the user the program is currently pulling tweets from, as well as the number of tweets found from said user once the check has been completed.

Due to request limitations by Twitter's API, the program will occasionally be denied access to tweets. When this happens, the following line will show up in the command prompt.

`Unable to pull user history, attempting to reconnect(1)`

If you see this line show up in the command prompt, **do not close the command window and attempt to retry the program.** The program will automatically retry to pull tweets every so often, until the requests are once again allowed by the Twitter API.

## Output
As the program is running, tweets will be written to the output file. If you specified an output file name in your command line, the output file will be named "<Insert Filename Here>.jsonl" If you have not chosen an output name, the standard output file will be called "tweet_history.jsonl".
A seperate file called "users.txt" will also be created, holding the Twitter screennames searched by the main program. This file can be used later to pull information from the same collection of Twitter users if desired.
