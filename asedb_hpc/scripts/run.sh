#!/bin/bash -l
# The -l above is required to get the full environment with modules

#SBATCH -A snic####-##-##
#SBATCH --mail-type=ALL
#SBATCH -t 1-00:00:00

#SBATCH -J id_xx
#SBATCH -o dat.out

# number of nodes
#SBATCH -n 28

# NEEDED MODULES FOR THE CALCULATION
module purge
source ~/calcs/env/load_vasp_ase

# RUN THE PYTHON CODE
python ../run.py
