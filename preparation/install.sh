#!/bin/bash
# Installation script for required libraries
# ISU 03/21
sudo apt install python3.8 python3-pip python3-tk
pip install numpy pandas seaborn jupyter
echo "export PATH=\$PATH:$HOME/.local/bin/" >> ~/.bashrc
echo "export DISPLAY=localhost:0.0" >> ~/.bashrc
source ~/.bashrc
