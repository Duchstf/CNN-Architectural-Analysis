# CNN-Architectural-Analysis
Codes and data related to paper: 

## Files Summary
Each folder MINERvA-Vertex-Finding and MINERvA-Hadron-Multiplicity contains two sub-folders: Code and Data. There you can find the data and the analysis code that was used to produce the results in the paper. 

## Raw data source
For those who are interested in the raw prototxt files from MENNDL, from which the features are extracted from. If you have access to the Wilson Cluster at Fermilab, the file paths are the followings:

**Image files that the networks were trained on:** `/data/jhamer/minerva_imgs/hadmultkineimgs_127x94_me1Amc.hdf5`

**NOTE: Human Performance Benchmark for Hadron Mutliplicity problem in paper is evaluated on ramdomly drawn input images on the same data set.**

**MINERvA Vertex Finding Networks:**
- First Population: `/data/jhamer/minerva_networks/networks/`
- Second Population: `/lfstev/e-938/aghosh12/minerva_174plane/logs`

**MINERvA Hadron Multiplicity Networks:** `/lfstev/e-938/aghosh12/minerva_multi/logs`

**Singularity recipe to build an image:** [Link](https://github.com/Duchstf/CNN-Architectural-Analysis-SingularityImg)
