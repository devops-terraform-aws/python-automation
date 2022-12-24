#!/usr/bin/env bash

# Make sure you are in the "AmazonAutomation" directory
cd AmazonAutomation

# install virtual environment
python -m venv .venv

# for Git Bash, run:
source .venv/bin/activate

# for PowerShell, run:
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
.venv\Scripts\activate


# for WSL or Linux, run:
source .venv/bin/activate

# to exit from virtual environment
deactivate
