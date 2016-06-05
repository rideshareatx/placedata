#!/usr/bin/env bash

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install -y --force-yes software-properties-common build-essential python-dev python-pip libgeos-dev
pip install --upgrade pip
pip install simplejson numpy scipy requests geocoder Shapely
