#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping
app = Flask(__name__)


# In[2]:


# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# In[3]:


@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)
if __name__ == "__main__":
   app.run()

