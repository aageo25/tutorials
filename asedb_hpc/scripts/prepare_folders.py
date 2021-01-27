import os
import shutil
from ase.db import connect
 
db = connect(dbname)
 
prevdir = os.getcwd()

# here quer can be anything
query = 'queued=False'

for row in db.select(query):
    dir = str(row.id)
    # create the subfolders
    try:
        os.mkdir(dir)
    except FileExistsError:
        print(f'Keeping folder {dir}')
    else:
        print(f'Creating folder {dir}')
    os.chdir(dir)
    # make a symbolic link for your sbatch submission file
    try:
        os.symlink('../run.sh', 'run.sh')
    except:
        pass
    # write a file with the row id
    with open('db_id', 'w') as out:
        out.write(dir)
    os.chdir(prevdir)
