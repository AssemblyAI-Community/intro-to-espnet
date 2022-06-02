#!/bin/sh

echo "Upgrading packages"
yes | sudo apt update
yes | sudo apt upgrade

echo "Installing ffmpeg"
yes | sudo apt install ffmpeg

echo "Installing sox"
yes | sudo apt install sox

echo "Installing cmake"
yes | sudo apt-get install cmake

echo "Installing pyjopentalk"
yes | sudo apt-get install pyjopentalk==0.1.5

echo "Installing parallel_wavegan"
yes | sudo apt-get install parallel_wavegan==0.5.3

echo "Cloning project folder ESPNet"
git clone https://github.com/AssemblyAI-Examples/intro-to-espnet.git
cd intro-to-espnet

echo "Installing virtualenv"
yes | apt install virtualenv

echo "Creating virtualenv"
yes | virtualenv venv -p /usr/bin/python3.6
source venv/bin/activate
pip install -r requirements.txt

