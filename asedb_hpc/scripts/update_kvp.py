import numpy as np
from ase.db import connect

dbname = '../../surfaces.db' # Be careful here. Always double-check if your connect to the desired database
dbid = int(np.loadtxt('dbid'))

db = connect(dbname)

# update queued kvp in the db
db.update(dbid,queued=True,started=False,converged=False)
