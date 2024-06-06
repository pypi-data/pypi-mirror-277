import requests
import cv2

url = "http://localhost:8000/predict"

files = {'files': open('../data/test/test/035_43-14-ROOT1-2023-08-08_pvd_OD01_f6h1_03-Fish Eye Corrected.png', 'rb')}
data = {'model_name': 'test'}

response = requests.post(url, files=files, data=data)

# The .json() method returns the JSON response as a Python dictionary
parse_respons = response.json()

print(parse_respons)
