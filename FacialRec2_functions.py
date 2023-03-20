from pathlib import Path
import requests
from requests.auth import HTTPBasicAuth
import json
import sys
from compreface import CompreFace
from compreface.service import RecognitionService
from compreface.collections import FaceCollection
from compreface.collections.face_collections import Subjects
from FacialRec2_GUI import *
try: 
    import cPickle as pickle
except ImportError:
    import pickle

my_env = pickle.load(open('my_env.pkl', 'rb'))

DOMAIN: str = my_env[0]
PORT: str = my_env[1]
API_KEY: str = my_env[2]

compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(API_KEY)

face_collection: FaceCollection = recognition.get_face_collection()

subjects: Subjects = recognition.get_subjects()

#Define Funtions:

#Define function to call api and search pictures
def facial_rec(file,person,matchs):
    '''Check input file to find any face matches'''
    api_url = '{}:{}/api/v1/recognition/recognize'.format(DOMAIN,PORT)
    headers = {'x-api-key':API_KEY} 
    files = {'file': open(file, 'rb')}
    try:
        response=requests.post(api_url, headers=headers, files=files, auth=None)
        content = response.json()
        decoded_content = content.get('result')
        for result in decoded_content:
            subjects = result['subjects']
            subject = subjects[0]
            similarity = subject['similarity']
            subject = subject['subject']
            if subject == person:
                if similarity > 0.91:
                    matchs.append(str(file))
                    print("Match Found: {} Subject:{} Similarity:{:.2f}%".format(file, subject, (similarity*100)))
                else:
                    print("Partial Match Found: {} Subject:{} Similarity:{:.2f}%".format(file, subject, (similarity*100)))
            else:
                print("No Match: {} ".format(file))
                          
    except:
        print("No Face found")
    return(matchs)

#Define function to list subjects
def facial_rec_query():
    '''List available subjects'''
    api_url = '{}:{}/api/v1/recognition/subjects/'.format(DOMAIN,PORT)
    headers = {'Content-Type':'application/json',
               'x-api-key': API_KEY
    }
    response=requests.get(api_url, headers=headers)
    content = response.json()
    subjects = content.get('subjects')
    return(subjects)

#Define function to add picture to subject 
def facial_rec_add(subject):
    '''Add new picture to subject'''
    file_path = filedialog.askopenfilename()
    response = face_collection.add(image_path=file_path, subject=subject)
    print(response)
    try: 
        id = response['image_id']
        result = 'Image added to subject {}'.format(subject)
    except:
        result = 'Image add failed - please try again'
    return(result)







