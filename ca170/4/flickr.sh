#!/bin/sh

wget "https://api.flickr.com/services/feeds/photos_public.gne?format=json&tags=$img" > $HOME/flickr.html
