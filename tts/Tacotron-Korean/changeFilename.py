import os

# 주어진 디렉토리에 있는 항목들의 이름을 담고 있는 리스트를 반환합니다.
# 리스트는 임의의 순서대로 나열됩니다.
# file_path = 'C:\\Users\\multicampus\\Desktop\\2학기 ssafy\\2차 프로젝트\\4주차\\새 폴더\\tts'
# file_names = os.listdir(file_path)
# print(file_names)


# i = 0
# for name in file_names:
#     src = os.path.join(file_path, name)
#     dst = str(i) + '.wav'
#     dst = os.path.join(file_path, dst)
#     os.rename(src, dst)
#     i += 1


# yuki
file_path = 'C:\\Users\\multicampus\\Desktop\\2학기 ssafy\\2차 프로젝트\\4주차\\s03p23c206\\tts\\Tacotron-Korean\\datasets\\yuki\\audio'
file_names = os.listdir(file_path)

for name in file_names:
    src = os.path.join(file_path, name)
    tmp = name
    idx_left = tmp.index('(')
    idx_right = tmp.index(')')
    save_tmp = int(tmp[idx_left+1:idx_right])-1

    dst = str(save_tmp) + '.m4a'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)