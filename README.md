# emValidator
Validate Suspicious Email Addreses using EmailRep.io's API

Simple script for use when doing a Brute Force attck on SSH.  Simply run the script with the required arguments and run.  Will output a successful logon to a file so you don't have to run the script again if you misplace the correct credentials.

*To get a free/paid api key, go to https://emailrep.io/key*

### Install/Setup ###
Grab the git repo:
`git clone https://github.com/jeffvader84/emValidator`

Install the required python packages:
`pip install -r requirements.txt`

If you purchase an api key, you can add it to the variable api_key on line 121 of the script. If you add the api key to that variable, you can omit adding the `-a` and pasting in your api key every time you run the script.

If you have a free api key, the above method to hardcode the key into the script will also work.

### Examples ###
To use run:
`python3 emValidator.py -e <email> -a <api key> -o <file.csv> -j <file.json> -v`

If you need any additional help run the following command:
`python3 emValidator.py -h`
