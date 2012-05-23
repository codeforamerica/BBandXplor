# BBandXplor
BBandXplor lets you explore and evaluate hundreds of highlighted neighborhoods within a city, using random Google Street View locations.
The goal is to build consensus (or crowdsource) subjective information about the neighborhoods.

For example, the Pittsburgh BBandXplor map explores the question: why were hundreds of areas cut out of ISPs' maps?
Viewers can vote on whether the exception is benign ( highways and parks ), concerning ( vacant houses ), or worth targeting ( areas with homes and businesses ).

The same program could be used to explore food deserts and find locations suitable for a farmers' market or community garden.

The server-side codebase is a Ruby on Rails app designed for hosting on Heroku.

## Working with BroadbandMap.gov

###Shapefiles
* Scroll down on the [http://www.broadbandmap.gov/data-download Data Download] page until you see your state.  Click the download on the right column to download SHP shapefiles.
* The download is a zip archive containing at least three other zip archives. Open each of these to expose state-level data on wireless and terrestrial broadband.
* Search for a shapefile with the city or county limits from the Census TIGER maps

<strong>Viewing Shapefiles</strong>
* Install <a href="http://qgis.org">QGIS</a> to view and edit shapefiles.
* In QGIS, select Layer... Add Vector Layer.  For Dataset, choose your city or county limits. The system should automatically set the view to see the entire shape.
* Now select Layer... Add Vector Layer for one of your broadband shapefiles. These are usually wireless, terrestrial, and road-lining connections across the entire state.

<strong>Selecting Geodata</strong> - to save processing time, reduce the size of the file before running the Clip operation.
* On QGIS's picture menu bar, click the <strong>>><strong> to the right of a mouse cursor to see different options for mouse movement. Select the top middle, which shows selecting features by rectangle.
* Click and drag from one corner of the screen to the opposite end. Release to select only layers which overlap with your city or county.
* Now click Layer... Save selected as... and save as an Esri Shapefile with the name City_BBand_Select.
* Remove the statewide layer and use Layer... Add Vector Layer to add the City_BBand_Select layer.

<strong>Clipping Geodata</strong> - cut the boundaries of the area to your city or county boundaries
* Click Vector... Geoprocessing Tools... Clip to open the clip menu. Set Input Vector to City_BBand_Select and Clip Layer to the city or county limits.  Use Browse to select a name such as City_BBand_Clip as the name for the shapefile.
* Click OK and wait (up to several minutes) while the Clip operation runs.

<strong>Dividing into Polygons</strong>
* The output shapefile is a mix of different ISPs. From the Vector menu, select Data Management Tools > Split Vector Layer
* Select your clipped broadband layer as the Input Vector and DBANAME as the Unique ID Field.
* For output file, create a new folder and select it with the file tool. Click OK to create the layers.
* Add the shapefile layers to the map - they will have names such as City_BBand_Clip_DBANAME__ISP NAME.shp.

<strong>Saving as Google Earth KML</strong>
* You can right-click each layer in the QGIS menu and save it as a KML file, to view them in Google Earth

<strong>Extracting Holes</strong>
* Run the included findholes.py script to create KML and JavaScript files

<code>python findholes.py SOURCE_FILE.kml OUTPUT_NAME</code>

* OUTPUT_NAME.kml is a file you can open in Google Earth and other mapping applications

* OUTPUT_NAME.js is a script which adds coordinates of all of the holes to an array. Attach it to macon.erb or other template

<strong>Forking Manchester</strong>
Make these changes to manchester.erb

* Replace manchester.js with the URL of your generated JavaScript file.

* Change the config object

    var config = {
	    latitude: 42.992124,
	    longitude: -71.448266,
	    zoom: 13,
	    city: "Manchester",
	    latmin: 42.943387,
	    latmax: 43.023758,
	    lngmin: -71.49478,
	    lngmax: -71.379773
    };

Add your city to pdf_archive.rb. Using Honolulu as an example:

    get '/honolulu' do
      erb :honolulu
    end

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
