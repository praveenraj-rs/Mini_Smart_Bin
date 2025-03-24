#!/bin/bash
# Bash Script to run the main script
which python3
cd /home/hexfuse/Mini_Smart_Bin/deployment
pwd
activate() {
. /home/hexfuse/venv/bin/activate
}
activate
which python3
python3 main.py

