sudo apt update
yes | sudo apt upgrade
yes | sudo apt install ffmpeg sox cmake git virtualenv libfreetype6-dev gcc
yes | sudo apt-get install python3-dev libxml2-dev libxmlsec1-dev

git clone https://github.com/AssemblyAI-Examples/intro-to-espnet.git
cd intro-to-espnet
virtualenv venv -p /usr/bin/python3.6
source venv/bin/activate
pip install soundfile
pip install torch
pip install parallel-wavegan==0.5.3
pip install pyopenjtalk==0.1.5
pip install ctc-segmentation
pip install espnet-model-zoo
pip install kenlm
