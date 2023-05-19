# Cocktail Attack

This pipeline aims to find repositioned drug combinations effective and selective against cancer cell using network perspectives.

A detailed scheme of the workflow can be found at pipeline_scheme.png. It is recommended to follow the scheme while going through this tutorial.

## 1. Constructing Biogrid interactomes.

To construct a Biogrid interactome use biogrid_parser.py and human (9606) Biogrid database available here: https://downloads.thebiogrid.org/BioGRID/Release-Archive/BIOGRID-4.4.221/. This way you'll obtail a Biogrid generic interectome. Use this generic interactome and an Expression Atlas file (https://www.ebi.ac.uk/gxa/home) to obtain tissue/cell-line specific interactomes using EMBL_interactomes.py, by specifing the column number of the expression file you are interested in. The bash script take_all_interactomes.sh allows you to construct all the interactomes available for a given expression file.

## 2. Constructing STRING interactomes.

To construct a generic interactome with STRING interactions over 400/700/900 cut off, use filter_togenint_400_700_900.sh over human (9606) STRING database available at https://string-db.org/cgi/download. Then, translate the protein names to gene names IDs by using string_gene_translate.py. To use the generic interactome to construct tissue-specific or cell-sepecific interactomes, continue the steps described in the prior point.

## 3. Generating a list of down-regulating drugs from DrugBank database.

Use XML_drugbank_parser.py with DrugBank .xml file to obtain a list of drugs-targets with their mechanism of action, their approval state, etc. Use this file as input for drug_combiner.py with as long with a file specifing the actions to be included (present in ./Cocktail) and with "1" as number of drugs per cocktail to create the "co1" file, a list of down-regulating drugs with their corresponding targets.

## 4. Select the 50 most relevant drugs for an specific cancer using IVI.

Taking an interactome from a cancer cell line and another one for its corresponding tissue, use ivi.R on each of them to obtain the IVI values of their proteins. Use both files and the "co1" file (from previous step) as input of ivi_targeting.py to obtain the differential of IVI values corresponding to each drug. Sort this file acording to this differential (sort -rnk 3) and take the 50 first drugs (head -50) to get the 50 most influencial drugs for this cancer according to IVI.

## 5. Create al the cocktails possible of size n for an specific cancer.

Use drug_combiner again with as before but this time change the "drug per cocktail" input parametre for n (the desired cocktail size) and also using a fourth input: the top 50 drugs filtered with IVI. This give us a "coN" file, a list of all possible combinations of size N of these drugs, and their targets.

## 6. [OPTIONAL] Process the "coN" file to make the following step faster.

If time is not an issue you can skip to the following step. This step consist in taking advantage that a lot of cocktails have the same set of targets to make the posterior network attack redundancies-aware and therefore faster.

Use the pair of healthy and cancer interactomes and the "co1" files as input for wich_targets_hit.py to obtain a list of wich target, from all the drugs, arre included in this pair of networks. Use the unprocessed "coN" and this previous list as input for cocktail_filtering_by_hit.py. This give us the same list of cocktails but only including the hitting targets. Next, use cockail_target_sort.py to sort the targets of each cocktail alphabetically. Lastly, use cocktail_sorter.sh to sort the cocktails for their targets, putting together those that have exactly the same set of targets. This allows that, in the next step, when we calculate the topological values of the attack, whenever we find that the next cocktail have the same set of targets, we don't repeat the process. This reduces the computing times significantly.

## 7. Attack the networks with the list of cocktails.

Take the pair of interactomes, the "coN" file (optimiced or not) and run rtargeting.R to obtain the values of the topological values analiced. rchunk_targeting_teide.sh allows you to pararelize the run in different cores of your machine, making the procces faster if needed.
