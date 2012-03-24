# BBandXplor
BBandXplor lets you explore and evaluate hundreds of highlighted neighborhoods within a city, using random Google Street View locations.
The goal is to build consensus (or crowdsource) subjective information about the neighborhoods.

For example, the Pittsburgh BBandXplor map explores the question: why were hundreds of areas cut out of ISPs' maps?
Viewers can vote on whether the exception is benign ( highways and parks ), concerning ( vacant houses ), or worth targeting ( areas with homes and businesses ).

The same program could be used to explore food deserts and find locations suitable for a farmers' market or community garden.

The server-side codebase is a Ruby on Rails app designed for hosting on Heroku.

## Setup

    git clone git://github.com/mapmeld/BBandXplor.git
    cd BBandXplor
    gem install bundle
    bundle

## Run the tests

    bundle exec rake

## Run the app and background worker

    gem install foreman
    foreman start

You can now open the app in your browser http://localhost:3000

## Running on Heroku

Running this on Heroku requires the following steps:

### Step 1: Create the app on the Heroku Cedar stack

    gem install heroku
    heroku apps:create YOUR_APP_NAME_HERE --stack cedar

We also need to configure it to run in production

    heroku config:add RACK_ENV=production

### Step 2: Add a MongoDB Addon

The MongoHQ or MongoLab Addons will give us a small free MongoDB instance for storing our documents.

    heroku addons:add mongohq:free

### Step 3: Deploy to Heroku

    git push heroku master
    heroku scale web=1 worker=1

### Step 4: Create geospatial index

Log into heroku.com and open the app's page
On the right, under the banner, select MongoHQ from Addons
On the MongoHQ page, select the sv_reports collection
On the row of tabs (Documents open by default) select Indexes
Click "Create a Geospatial Index". Set Location Field to "latlng" with Min -180 and Max 180
Click "Create Index" to enable searching reports by location

## License
Free BSD licensed

The server-side code is adapted from Jonathan Hoyt's PDF Archive example for using MongoDB with Heroku.
That license agreement is printed below:
---
Copyright (c) 2011 Jonathan Hoyt
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
