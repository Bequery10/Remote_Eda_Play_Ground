# EDA Playground Automation

This open source program provides a seemingly remote interraction with edaplayground.com for thoese who don't want to open it manually through a browser.

## Requirements

Chrome version 70 or later

## Setup

Before you run, make sure:
   No other chrome session is open,
   Refer to the default variables or change them based on your needs in main.py between the lines 124 and 130 (make sure names are exactly as in edaplayground.com)

For the first time running, chrome browser will be visible so you can login with gmail only for the starter

## Use
   you can edit testbench.sv, design.sv, and hexfile.dat for memory if necessary 

1. Install python and pip if not installed

2. Create a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate

3. Install requirements
   ```sh
   pip install -r requirements.txt

4. Change the variables within the main function in main.py based on your system and needs

5. Run main.py
   ```sh
   python3 -u main.py
