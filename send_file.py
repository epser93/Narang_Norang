import os
import requests

# 음성파일 가져오기
current_path = os.getcwd()
file_list = os.listdir(current_path+'\\file')
file_list.sort(key=lambda x : len(x))

# 대사 가져오기
fairytale_id = 6
model_id = 1
scenario_url = "https://j3c206.p.ssafy.io/api/books/scenario/{}/".format(fairytale_id)

header = {"Authorization" : "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6Ilx1YWU0MFx1YzcyMFx1YWUzMCIsImV4cCI6MTYwMjE0NTcxMiwiZW1haWwiOiIiLCJvcmlnX2lhdCI6MTYwMjA1OTMxMn0.hA4RaJdYGk0d6VbpWiV5C-LBWyUU9TExQY5IfM4OhsU"}

response = requests.get(url=scenario_url, headers=header).json()

for i in range(len(response)):
    # print(i+163, end=" ")
    print(response[i]['content'])

print(len(response))
for i in range(len(file_list)):
    print(file_list[i])
# url = "https://j3c206.p.ssafy.io/api/books/voice_storage"

# for i in range(len(response)):
#     print('{}\\file\\{}'.format(current_path, file_list[i]))
#     files = open('{}\\file\\{}'.format(current_path, file_list[i]), 'rb')
#     upload = {'file': files}
#     file_send_url = "{}/{}/{}/{}/".format(url, fairytale_id, response[i]['id'], model_id)
#     requests.post(file_send_url, files=upload, headers=header)