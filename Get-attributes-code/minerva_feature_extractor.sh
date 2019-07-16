#!/bin/bash
#PBS -S /bin/bash
#PBS -N minerva_network_topology_analysis
#PBS -j oe
#PBS -o /data/dhoang/minerva_174plane_simple_output/GA_scratch_500026_simple_output
#PBS -l walltime=04:00:00
#PBS -A minervaG
#PBS -q amd32

#NOTE: This shell script still works fine on Wilson Cluster. 
#However, the Cluster uses a different kind of workload manager (SLURM). 
#Thus the comments above are likely irrelevant (but ommitting them still doesn't work). I didn't have 
#time to translate them all to SLURM so just leave it like that. More details about difference between 
#PBS and SLURM can be found here: https://wilsonweb.fnal.gov/slurm.shtml

echo "Job ${PBS_JOBNAME} submitted from ${PBS_O_HOST} started "`date`" jobid ${PBS_JOBID}"

cd /home/dhoang

export INPUT_PATH='/lfstev/e-938/aghosh12/minerva_multi/logs/GA_scratch_500031'
export OUTPUT_PATH='/data/dhoang/minerva_hadron_multiplicity'
export START_INDEX='1'
export END_INDEX='5000'
export MODE='minerva'

singularity exec -B /lfstev:/lfstev network_topology.simg python3 MINERvA_NOvA_network_analysis/get_simple_attributes.py ${INPUT_PATH} ${OUTPUT_PATH} ${START_INDEX} ${END_INDEX} ${MODE}

exit
