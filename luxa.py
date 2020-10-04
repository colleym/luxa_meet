#!/usr/local/bin/python3

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

    # http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys, getopt
import json
import requests


# # change color via webhook
def change_light(webhookid,color):
    json_post={}
    json_post['userId'] = webhookid
    json_post['actionFields'] = {}
    json_post['actionFields']['color'] = color
    
    try:
        r = requests.post('https://api.luxafor.com/webhook/v1/actions/solid_color', json=json_post)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:],"k:c:h",["webhookid=","color=","help"])
    except getopt.GetoptError:
        print ('luxa.py -k <webhookid> -c <color>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print ('luxa.py -k <webhookid> -c <color>')
            sys.exit()
        elif opt in ("-k", "--webhookid"):
            webhookid = arg
        elif opt in ("-c", "--color"):
            color = arg
    # print ('WebhookID: ', webhookid)
    # print ('Color ', color)
    
    change_light(webhookid, color)

if __name__ == "__main__":
   main()