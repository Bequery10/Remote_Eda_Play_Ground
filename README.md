# EDA Playground Automation

This project automates the process of transferring SystemVerilog code from your local machine to EDA Playground and running it there using Selenium.

## requirements

Chrome version 70 or later

## Setup

Before you run, make sure:
   No other chrome session is open,
   Refer to the default variables or change them based on your needs in main.py starting from line 98 (make sure names are exactly as in edaplayground.com)

For the first time running, chrome browser will be visible so you can login with gmail only for starter

1. Install python if not installed

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
