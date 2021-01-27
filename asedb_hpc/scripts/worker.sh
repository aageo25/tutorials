#!/bin/bash                                                                    

# different ways to walk in the subfolders 
calc_id="$(find . -type d | sort -n |awk -F  "/" '{print $2}')"
#calc_id="$(cat list_id.txt)"
#calc_id="$(seq 1 9)"
#calc_id="3"
 
home_dir=$(pwd)

#Be careful here. Double-check if this is the database you want to connect.
db="../../surfaces.db" # A full path is preferred. 
 
for i in $calc_id ; do
    work_id=${i}
    cd $work_id
    echo ========
    echo $work_id
    echo ========
    # submit the calculation
    #sbatch --job-name=$work_id.surfaces run.sh > JobID ; more JobID
    # update the status in the database
    ase db $db id=$work_id -k queued=True
    # run a script in the subfolder
    python3 ../run.py $db
    cd $home_dir
done
