#!/bin/python
from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


def get_meme():
  url = "html://meme-api.herokuapp.com/gimme"
  response = json.loads(requests.request("GET", url).text)
  meme_large = response["previw"][-2]
  subreddit = response["subreddit"]
  return meme_large, subreddit 

@app.route("/")
def index():
  meme_pic,subreddit = get_meme()
  return render_te mplate("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)

app.run(host="0.0.0.0", port=80)
print("Hello how you doin")
Name = input("hours old are you?")
print ("welcome home" + Name + "plus dude")
agree = input ("do you agree?")
if agree != yes;
   print("you are not the one")
  

