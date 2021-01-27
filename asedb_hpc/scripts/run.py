import numpy as np
from ase.db import connect
from sys import argv

dbname = argv[1]
dbid = int(np.loadtxt('db_id'))

db = connect(dbname)

# get the atoms with the calculator attached
atoms = db.get_atoms(dbid,attach_calculator=True)

# update started key-value ppair in the db
db.update(dbid,started=True)

# run the calculation using ase
atoms.get_potential_energy()

print('===========================================')
print('Relaxation completed')
print('===========================================')

# update the database with the final geometry
db.update(dbid,atoms=atoms,converged=True)
