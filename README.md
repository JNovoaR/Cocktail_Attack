# Cocktail Attack

This pipeline aims to find repositioned drug combinations effective and selective against cancer cell using network perspectives.

A detailed scheme of the workflow can be found at pipeline_scheme.html. It is recommended to follow the scheme while going through this tutorial.

## 1. Constructing Biogrid interactomes.

To construct a Biogrid interactome use biogrid_parser.py and human (9606) Biogrid database available here: https://downloads.thebiogrid.org/BioGRID/Release-Archive/BIOGRID-4.4.221/. This way you'll obtail a Biogrid generic interectome. Use this generic interactome and an Expression Atlas file (https://www.ebi.ac.uk/gxa/home) to obtain tissue/cell-line specific interactomes using EMBL_interactomes.py, by specifing the column number of the expression file you are interested in. The bash script take_all_interactomes.sh allows you to construct all the interactomes available for a given expression file.

