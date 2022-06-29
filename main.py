import os
import shutil
import time
#n'oublier pas le anti slash a la fin de votre chemin d'accès
access_path = r"VOTRE CHEMIN D'ACCES"
list = os.listdir(access_path)

for x in list:
    date_creation = time.ctime(os.path.getmtime(access_path + x))
    date_decouper = date_creation.split()
    date_creation_obj = time.strptime(date_creation, '%a %b %d %H:%M:%S %Y')
    os.makedirs(access_path + date_decouper[4], exist_ok=True)
    os.makedirs(access_path + date_decouper[4] + '\\' + date_decouper[1], exist_ok=True)
    source = access_path + x
    destination = access_path + date_decouper[4] + '\\' + date_decouper[1]
    shutil.move(source, destination)