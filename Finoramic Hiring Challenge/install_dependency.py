import subprocess

error = []
def install(name):
    try:
        subprocess.call(['pip', 'install', name])
    except Exception as e:
        error.append(i)
        
with open('doc.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content] 

for i in content:
    install(i)

if len(error)==0:
    print("Success")
else:
    for i in error:
        print(i)
