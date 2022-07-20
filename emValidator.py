import json, requests, os, argparse, sys
import pandas as pd
from time import sleep

# def functions - start

# ascii art banner
def ascii_banner():
    print('                                                                                                               dddddddd                                                                             ')
    print('                                         VVVVVVVV           VVVVVVVV               lllllll   iiii              d::::::d                          tttt                                               ')
    print('                                         V::::::V           V::::::V               l:::::l  i::::i             d::::::d                       ttt:::t                                               ')
    print('                                         V::::::V           V::::::V               l:::::l   iiii              d::::::d                       t:::::t                                               ')
    print('                                         V::::::V           V::::::V               l:::::l                     d:::::d                        t:::::t                                               ')
    print('    eeeeeeeeeeee       mmmmmmm    mmmmmmm V:::::V           V:::::Vaaaaaaaaaaaaa    l::::l iiiiiii     ddddddddd:::::d   aaaaaaaaaaaaa  ttttttt:::::ttttttt       ooooooooooo   rrrrr   rrrrrrrrr   ')
    print('  ee::::::::::::ee   mm:::::::m  m:::::::mmV:::::V         V:::::V a::::::::::::a   l::::l i:::::i   dd::::::::::::::d   a::::::::::::a t:::::::::::::::::t     oo:::::::::::oo r::::rrr:::::::::r  ')
    print(' e::::::eeeee:::::eem::::::::::mm::::::::::mV:::::V       V:::::V  aaaaaaaaa:::::a  l::::l  i::::i  d::::::::::::::::d   aaaaaaaaa:::::at:::::::::::::::::t    o:::::::::::::::or:::::::::::::::::r ')
    print('e::::::e     e:::::em::::::::::::::::::::::m V:::::V     V:::::V            a::::a  l::::l  i::::i d:::::::ddddd:::::d            a::::atttttt:::::::tttttt    o:::::ooooo:::::orr::::::rrrrr::::::r')
    print('e:::::::eeeee::::::em:::::mmm::::::mmm:::::m  V:::::V   V:::::V      aaaaaaa:::::a  l::::l  i::::i d::::::d    d:::::d     aaaaaaa:::::a      t:::::t          o::::o     o::::o r:::::r     r:::::r')
    print('e:::::::::::::::::e m::::m   m::::m   m::::m   V:::::V V:::::V     aa::::::::::::a  l::::l  i::::i d:::::d     d:::::d   aa::::::::::::a      t:::::t          o::::o     o::::o r:::::r     rrrrrrr')
    print('e::::::eeeeeeeeeee  m::::m   m::::m   m::::m    V:::::V:::::V     a::::aaaa::::::a  l::::l  i::::i d:::::d     d:::::d  a::::aaaa::::::a      t:::::t          o::::o     o::::o r:::::r            ')
    print('e:::::::e           m::::m   m::::m   m::::m     V:::::::::V     a::::a    a:::::a  l::::l  i::::i d:::::d     d:::::d a::::a    a:::::a      t:::::t    tttttto::::o     o::::o r:::::r            ')
    print('e::::::::e          m::::m   m::::m   m::::m      V:::::::V      a::::a    a:::::a l::::::li::::::id::::::ddddd::::::dda::::a    a:::::a      t::::::tttt:::::to:::::ooooo:::::o r:::::r            ')
    print(' e::::::::eeeeeeee  m::::m   m::::m   m::::m       V:::::V       a:::::aaaa::::::a l::::::li::::::i d:::::::::::::::::da:::::aaaa::::::a      tt::::::::::::::to:::::::::::::::o r:::::r            ')
    print('  ee:::::::::::::e  m::::m   m::::m   m::::m        V:::V         a::::::::::aa:::al::::::li::::::i  d:::::::::ddd::::d a::::::::::aa:::a       tt:::::::::::tt oo:::::::::::oo  r:::::r            ')
    print('    eeeeeeeeeeeeee  mmmmmm   mmmmmm   mmmmmm         VVV           aaaaaaaaaa  aaaalllllllliiiiiiii   ddddddddd   ddddd  aaaaaaaaaa  aaaa         ttttttttttt     ooooooooooo    rrrrrrr            ')
    print('\n')
    print(f'                                                                                  Version {version}                                                                                                ')
    print('                                                                   https://github.com/jeffvader84/emValidator                                                                                         ')
    print('                                                                       python3 emValidator.py -h for help                                                                                      ')
    print('\n')                                                                                                                                                                    

def clear_screen():
    # mac and linux
    if os.name == 'posix':
        c = os.system('clear')
    else:
        # windows
        c = os.system('cls')

def new_line():
    print('\n')

# setup arguments
def arguments():
    parser = argparse.ArgumentParser(description="Validate Suspicious Email Addreses using EmailRep.io's API")
    parser.add_argument('-e', '--email', dest='email', help='Target email address to validate')
    parser.add_argument('-o', '--output', dest='output', help='Name of csv file to save results in')
    parser.add_argument('-a', '--api', dest='apikey', help='(Free) API key for EmailRep')
    parser.add_argument('-j', '--json', dest='json', help='Save json API response to file')
    parser.add_argument('-v', '--verbose', dest='verbose', action='count', default=0, help='Prints additional information to the terminal')
    global args
    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        parser.exit()

def j_output():
    global json_file_name
    if args.json:
        json_file = open(args.json, 'w')
        json_file.write(text)
        json_file.close()
        json_file_name = args.json
    else:
        json_file = open(f'{email}.json', 'w')
        json_file.write(text)
        json_file.close()
        json_file_name = f'{email}.json'

def api_call():
    if not args.apikey:
        get = requests.get(checker, headers={'Key': api_key, 'User-Agent': 'My Script'})
    elif args.apikey:
        get = requests.get(checker, headers={'Key': args.apikey, 'User-Agent': 'My Script'})
    else:
        print('No api key given as argument or added to variable in script.')
        print('Exiting script...')
        sys.exit()
    return get

def status_code():
    # rate limit max is HTTP 429
    if s_code == 429:
        print('You reached the daily limit on this API key.')
        sys.exit()
    elif s_code == 400:
    # invalid email is HTTP 400
        print('You provided an invalid email address. Please verify and try again.')
        sys.exit()
    elif s_code == 200:
    # successful api call is HTTP 200
        print(sep)
        print(f'Validated email address: {email}')
        print(sep)

# check file extension type
def f_ext(file):
    filename, filext = os.path.splitext(file)
    return filext

# def functions - stop

# def var - start

version = '1.0'

# def var - stop

##############################################
##                                          ##
##             Start of Script              ##
##                                          ##
##############################################

clear_screen()
ascii_banner()
arguments()
sleep(2)

# add api key to this variable if using the same key every time
api_key = ''
url = 'https://emailrep.io/'
sep = '-' * 55

# var for email provided
email = args.email
# create url with email address
checker = url + email
# only 10 queries per day (250 per month)
queries = 10
# make api call
get = api_call()
# get the status code
s_code = get.status_code

# daily limit check using HTTP code
status_code()

# grab information from api response and save to variables
# grab json output
text = get.text
# grab current api limit counts
if args.apikey:
    daily_limit = get.headers['X-Rate-Limit-Daily-Remaining']
    monthly_limit = get.headers['X-Rate-Limit-Monthly-Remaining']

# save output to json file
j_output()

# open json file
with open(json_file_name) as jfile:
    json_data = json.load(jfile)

# create data from with pandas
df = pd.json_normalize(json_data)
df.set_index('email', inplace=True)

# write data frame to csv file
df.to_csv(args.output)

# remove json file if not wanted
if not args.json:
    os.remove(json_file_name)

# verbose output
if args.verbose:
    print(text)
    print(df)

# print current api usage
if args.apikey:
    print(sep)
    print(f'Daily usage left: {daily_limit}')
    print(f'Monthly usage left: {monthly_limit}')
    print(sep)

##############################################
##                                          ##
##              End of Script               ##
##                                          ##
##############################################
