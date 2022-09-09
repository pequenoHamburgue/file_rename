import os
path = 'C:\\your\\local\\path\\'
count = 1

list = os.listdir()
print(list)
print(os.system(f'cd {path}'))
print(os.listdir(f'{path}'))
# test in windows 10
print(os.system('echo %cd%'))
print(os.chdir(path))
print(os.system('echo %cd%'))

#test checkout files in folder
for file_name in os.listdir():
    source = path + file_name
    #print(source)
    print(file_name)

    destination = path + "video-exemple-" + str(count) + ".mp4"

    #test:
    #altern = str(f'teste_{count}.mp4')

    #os.rename(file_name, altern)
    os.rename(source, destination)
    count += 1

print('testando...')
result = os.listdir()
print(result)
