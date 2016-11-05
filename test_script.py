import contextlib
import json
import httplib
import urllib2
import requests


server_url = 'http://127.0.0.1:5000/'


def test_server():
    return urllib2.urlopen(server_url + 'test').read()


#Added methods
def upload_file_test(filename, username):
    files = {'file': open(filename, 'rb')}

    payload = {'username': username}
    response = requests.post(server_url+'upload', files=files, data=payload)

    print response.content

def retrieve_file(unic_id):
    payload = {'unic_id': unic_id}

    response = requests.get(server_url+'retrieve', data=payload)

    #IF YOU WANT TO WRITE IT TO A FILE
    #f = open('ttt.zip','w')
    #f.write(response.content)
    return response

def get_listing():
    response = requests.get(server_url+'listing')

    return response.content

def unzip(unic_id):
    payload = {'unic_id': unic_id}

    response = requests.get(server_url + 'unzip', data=payload)

    #If YOU WANT TO WRITE IT TO A FILE
    print response.content
    #data = json.loads(response)[0]
    #data_format = json.loads(response.content)[1]
    f = open('ttt.jpg','w')
    f.write(response.content)

    return 1
if __name__ == '__main__':
    print test_server()

    upload_file_test('cat.jpg', 'igor')
    #print retrieve_file('NLJ72UP73')
    print get_listing()

    print unzip('74GWKPAD9K')