#! usr/bin/python3

import os
import requests
import optparse

# simple live subDomins checker
# thanks for using it

barnner = '''
███████ ██    ██ ██████  ██████   ██████  ███    ███ ██ ███    ██      ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██████  
██      ██    ██ ██   ██ ██   ██ ██  ████ ████  ████ ██ ████   ██     ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ 
███████ ██    ██ ██████  ██   ██ ██ ██ ██ ██ ████ ██ ██ ██ ██  ██     ██      ███████ █████   ██      █████   █████   ██████  
     ██ ██    ██ ██   ██ ██   ██ ████  ██ ██  ██  ██ ██ ██  ██ ██     ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ 
███████  ██████  ██████  ██████   ██████  ██      ██ ██ ██   ████      ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██   ██'''

# Tacking args from the command line

parser = optparse.OptionParser()
parser.add_option('-f', '--filename', metavar="FILE", default=None, help='File containing urls or subDomins \"required\" :=)')
parser.add_option('-O', '--output', dest="Ofile",
                  help='outputfile  :=)')
parser.add_option('-t', '--tor', action='store_true', default=None, help='trafic over tor  :=)')
parser.add_option('-p', '--proxy', action='store_true', dest="proxy", help='TO make trafic from proxy :=)')
(options, args) = parser.parse_args()

# check if the filename been included
if options.filename == 0:
    parser.error(' please use -h/--help for help and more information')
    exit()
# make function for tor trafic

def get_tor_session():
    session = requests.session()

    session.proxies = {'http': 'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session

# make function for proxy trafic

def proxy():
    proxy_session = requests.session()
    proxy_session.proxies = {
        'https': options.proxy,
        'http': options.proxy
    }
    return proxy_session

# check status_code of requests and get more information with args "-v" verbose
# filename = options.filename From command line

def status_code(filename):
    poxy = proxy()
    session = get_tor_session()
    print(barnner)
    print('[+] checking subDomins')
    print("=" * 25)
    print("BUILD BY MOHAMED\n Ahmed Saad")
    print("=" * 25)
    ####################################################################################################################
    all_status_code = [{"status_code": 101, "message": "[+] 100 Continue"},
                       {"status_code": 102, "message": "[+] 102 Processing"},
                       {"status_code": 103, "message": "[+] 103 Early Hints"},
                       {"status_code": 200, "message": "[+] 200 successful"},
                       {"status_code": 201, "message": "[+] 201 Created"},
                       {"status_code": 202, "message": "[+] 202 Accepted"},
                       {"status_code": 203, "message": "[+] 203 Non-Authoritative Information"},
                       {"status_code": 204, "message": "[+] 204 No Content"},
                       {"status_code": 205, "message": "[+] 205 Reset Content"},
                       {"status_code": 206, "message": "[+] 206 Partial Content"},
                       {"status_code": 300, "message": "[+] 206 Partial Content"},
                       {"status_code": 301, "message": "[*] 301 Moved Permanently"},
                       {"status_code": 302, "message": "[*] 302 Found"},
                       {"status_code": 303, "message": "[*] 303 See Other"},
                       {"status_code": 304, "message": "[*] 304 Not Modified"},
                       {"status_code": 307, "message": "[*] 307 Temporary Redirect"},
                       {"status_code": 308, "message": "[*] 308 Permanent Redirect"},
                       {"status_code": 400, "message": "[-] 400 Bad Request"},
                       {"status_code": 401, "message": "[-] 401 Unauthorized"},
                       {"status_code": 402, "message": "[-] 402 Payment Required"},
                       {"status_code": 403, "message": "[-] 403 Forbidden"},
                       {"status_code": 414, "message": "[-] 405 Method Not Allowed"},
                       {"status_code": 405, "message": "[-] 404 Not Found"},
                       {"status_code": 406, "message": "[-] 405 Method Not Allowed"},
                       {"status_code": 407, "message": "[-] 407 Proxy Authentication Required"},
                       {"status_code": 408, "message": "[-] 408 Request Timeout"},
                       {"status_code": 409, "message": "[-] 409 Conflict"},
                       {"status_code": 410, "message": "[-] 410 Gone"},
                       {"status_code": 411, "message": "[-] 411 Length Required"},
                       {"status_code": 412, "message": "[-] 412 Precondition Failed"},
                       {"status_code": 413, "message": "[-] 413 Payload Too Large"},
                       {"status_code": 414, "message": "[-] 414 URI Too Long"},
                       {"status_code": 415, "message": "[-] 415 Unsupported Media Type"},
                       {"status_code": 416, "message": "[-] 416 Range Not Satisfiable"},
                       {"status_code": 417, "message": "[-] 417 Expectation Failed"},
                       {"status_code": 418, "message": "[-] 418 I\'m a teapot"},
                       {"status_code": 421, "message": "[-] 421 Misdirected Request"},
                       {"status_code": 422, "message": "[-] 422 Unprocessable Entity (WebDAV)"},
                       {"status_code": 423, "message": "[-] 423 Locked (WebDAV)"},
                       {"status_code": 424, "message": "[-] 424 Failed Dependency (WebDAV)"},
                       {"status_code": 425, "message": "[-] 425 Too Early"},
                       {"status_code": 426, "message": "[-] 426 Upgrade Required"},
                       {"status_code": 428, "message": "[-] 428 Precondition Required"},
                       {"status_code": 429, "message": "[-] 429 Too Many Requests"},
                       {"status_code": 431, "message": "[-] 431 Request Header Fields Too Large"},
                       {"status_code": 451, "message": "[-] 451 Unavailable For Legal Reasons"},
                       {"status_code": 500, "message": "[] 500 Internal Server Error"},
                       {"status_code": 501, "message": "[] 501 Not Implemented"},
                       {"status_code": 502, "message": "[] 502 Bad Gateway"},
                       {"status_code": 503, "message": "[] 503 Service Unavailable"},
                       {"status_code": 504, "message": "[] 504 Gateway Timeout"},
                       {"status_code": 505, "message": "[] 505 HTTP Version Not Supported"},
                       {"status_code": 506, "message": "[] 506 Variant Also Negotiates"},
                       {"status_code": 507, "message": "[] 507 Insufficient Storage (WebDAV)"},
                       {"status_code": 508, "message": "[] 508 Loop Detected (WebDAV)"},
                       {"status_code": 510, "message": "[] 510 Not Extended"},
                       {"status_code": 511, "message": "[] 511 Network Authentication Required"}]

    ########################################################################################################
# check if the filename exists
# else will exit
    if os.path.exists(filename):
        # after checking the file exists
        # now check if is empty
        if os.stat(filename).st_size == 0:
            print('File is empty exiting !!!!!')
            exit()
        urls = open(filename).read().splitlines()
        # open file and read the lines
        print(
            '[+] for more information about the status_code check the documentation : https://developer.mozilla.org/en-US/docs/Web/HTTP/Status\n')

        for url in urls:
            # the program will check if the user want to use proxy or tor
            # else will run directly
            if options.tor == True:

                test = session.get(url)
            elif options.proxy == True:

                test = poxy.get(url)

            else:
                test = requests.get(url)
            ###########################################################################################
            for i in all_status_code:
                if test.status_code == i["status_code"]:
                    print(i["message"], url)
                    if options.Ofile:
                    # out put the results in file "options.Ofile"
                        with open(options.Ofile, "a") as f:
                            f.write(i["message"] + url + "\n")




    # print error message if file is not exists and exit
    else:
        print('File, ', os.path.realpath(filename), 'does not exist.  Please try again.')
        exit()
    print("=" * 25)
    print("END Request")
    print("=" * 25)


if __name__ == '__main__':

    status_code(options.filename)

