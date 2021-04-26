#!/bin/sh

img=$1

wget -q -O - "https://api.flickr.com/services/feeds/photos_public.gne?format=json&tags=$img" | grep "description" | tr -d '\\' | grep -o ' <p>.*</p>' > $HOME/flickr.html
