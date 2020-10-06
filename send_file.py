import os
import requests

# 음성파일 가져오기
current_path = os.getcwd()
# file_list = os.listdir(current_path+'\\file')

# 대사 가져오기
fairytale_id = 1
model_id = 1
scenario_url = "https://j3c206.p.ssafy.io/api/books/scenario/{}/".format(fairytale_id)

header = {"Authorization" : "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6Ilx1YWU0MFx1YzcyMFx1YWUzMCIsImV4cCI6MTYwMjA1NTE4NSwiZW1haWwiOiIiLCJvcmlnX2lhdCI6MTYwMTk2ODc4NX0.4RWGyHvsV7lYtCWjBcqCUvmqm3GQG0Z-PCUpAzn-X8k"}

response = requests.get(url=scenario_url, headers=header).json()

for i in range(len(response)):
    print(response[i]['content'])


# url = "http://127.0.0.1:8000/api/books/voice_storage"

# for i in range(len(response)): 
#     files = open('{}\\file\\{}'.format(current_path, file_list[0]), 'rb')
#     upload = {'file': files}
#     file_send_url = "{}/{}/{}/{}/".format(url, fairytale_id, response[i]['id'], model_id)
#     requests.post(file_send_url, files=upload, headers=header)