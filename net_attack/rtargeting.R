#!/usr/bin/env Rscript
#This rtargeting.r is redundancies aware so is faster

library(igraph)


args <- commandArgs(trailingOnly= TRUE)


time_mode <- FALSE
deleted_args <- 0
for (i in 1:length(args)) {
	i = i - deleted_args
	if (substr(args[i], 1, 1) == "-") {
		if (grepl("t", args[i], fixed = TRUE)) {
			time_mode <- TRUE
		}
		args = args[-i]
		i = i-1
		deleted_args <- deleted_args + 1
	}
}

start_time = Sys.time()

if (length(args) <4) {
	all_cocktails <- TRUE
	first_cocktail <- 0
	last_cocktail <- 0
} else {
	all_cocktails <- FALSE
	first_cocktail <- strtoi(args[4])
	last_cocktail <- strtoi(args[5])
}



c_file <- file(args[3], open = "r")

#cocktails <- lapply(strsplit(readLines(c_file)," "), as.character)

original_healthy <- read.graph(args[1], format="ncol")
original_cancer <- read.graph(args[2], format="ncol")


if (time_mode) {
	net_readed = Sys.time()
	reading_time <- difftime(net_readed, start_time, units= "secs")
	cat("READING -> ", reading_time, "secs", "\n", file = stderr())
}


oh_l_vertices <- V(original_healthy)$name
oc_l_vertices <- V(original_cancer)$name

oh_vertices_count <- gorder(original_healthy)
oc_vertices_count <- gorder(original_cancer)

oh_density <- edge_density(original_healthy, loops= TRUE)
oc_density <- edge_density(original_cancer, loops= TRUE)

oh_APL <- mean_distance(original_healthy, directed= FALSE, unconnected= FALSE)
oc_APL <- mean_distance(original_cancer, directed= FALSE, unconnected= FALSE)

oh_NCC <- components(original_healthy)$no
oc_NCC <- components(original_cancer)$no

oh_SLCC <- max(components(original_healthy)$csize)
oc_SLCC <- max(components(original_cancer)$csize)

oh_CC_temp <- transitivity (original_healthy, type= "weighted", isolates= "zero")
oc_CC_temp <- transitivity (original_cancer, type= "weighted", isolates= "zero")
oh_CC_temp2 <- oh_CC_temp[!is.na(as.numeric(as.character(oh_CC_temp)))]
oc_CC_temp2 <- oc_CC_temp[!is.na(as.numeric(as.character(oc_CC_temp)))]
oh_CC <- mean(oh_CC_temp2[!is.infinite(oh_CC_temp2)])
oc_CC <- mean(oc_CC_temp2[!is.infinite(oc_CC_temp2)])

cat('Cocktail','Den_Heal_Ratio', 'Den_Cancer_Ratio','APL_Heal_Ratio','APL_Can_Ratio','NCC_Heal_Ratio','NCC_Can_Ratio','SLCC_Heal_Ratio','SLCC_Can_Ratio','Clust.Cof_Heal_Ratio','Clust.Cof_Can_Ratio', "\n", sep= "\t")

n<-0

previous_targets <- ""

c = unlist(lapply(strsplit(readLines(c_file, n=1),"\t"), as.character))
while (length(c) > 1) {
	if (time_mode) {start_cocktail = Sys.time()}
	if (all_cocktails || n %in% first_cocktail:last_cocktail) {
		disgregated_healthy <- original_healthy
		disgregated_cancer <- original_cancer
		drugs <- c[1]
		targets_string <- c[2]
		if (targets_string == previous_targets) {new_targets = FALSE} else {new_targets = TRUE}
		previous_targets <- targets_string
		targets_list <- strsplit(targets_string, " ")[[1]]
		if (new_targets) {
			for (target in targets_list) {
				if (target != drugs) {
					dh_l_vertices <- V(disgregated_healthy)$name
					dc_l_vertices <- V(disgregated_cancer)$name
					if (target %in%  dh_l_vertices) {
						disgregated_healthy <- delete_vertices(disgregated_healthy, c(target))
						}
					if (target %in%  dc_l_vertices) {
						disgregated_cancer <- delete_vertices(disgregated_cancer, c(target))
						}
					}
			}

			dh_l_vertices <- V(disgregated_healthy)$name
			dc_l_vertices <- V(disgregated_cancer)$name

			dh_vertices_count <- gorder(disgregated_healthy)
			dc_vertices_count <- gorder(disgregated_cancer)

			dh_density <- edge_density(disgregated_healthy, loops= TRUE)
			dc_density <- edge_density(disgregated_cancer, loops= TRUE)

			dh_APL <- mean_distance(disgregated_healthy, directed= FALSE, unconnected= FALSE)
			dc_APL <- mean_distance(disgregated_cancer, directed= FALSE, unconnected= FALSE)

			dh_NCC <- components(disgregated_healthy)$no
			dc_NCC <- components(disgregated_cancer)$no

			dh_SLCC <- max(components(disgregated_healthy)$csize)
			dc_SLCC <- max(components(disgregated_cancer)$csize)

			dh_CC_temp <- transitivity (disgregated_healthy, type= "weighted", isolates= "zero")
			dc_CC_temp <- transitivity (disgregated_cancer, type= "weighted", isolates= "zero")
			dh_CC_temp2 <- dh_CC_temp[!is.na(as.numeric(as.character(dh_CC_temp)))]
			dc_CC_temp2 <- dc_CC_temp[!is.na(as.numeric(as.character(dc_CC_temp)))]
			dh_CC <- mean(dh_CC_temp2[!is.infinite(dh_CC_temp2)])
			dc_CC <- mean(dc_CC_temp2[!is.infinite(dc_CC_temp2)])
			
			
			h_DEN_ratio <- round(oh_density/dh_density, 7)
			c_DEN_ratio <- round(oc_density/dc_density, 7)
			h_APL_ratio <- round(oh_APL/dh_APL, 7)
			c_APL_ratio <- round(oc_APL/dc_APL, 7)
			h_NCC_ratio <- round(oh_NCC/dh_NCC, 7)
			c_NCC_ratio <- round(oc_NCC/dc_NCC, 7)
			h_SLCC_ratio <- round(oh_SLCC/dh_SLCC, 7)
			c_SLCC_ratio <- round(oc_SLCC/dc_SLCC, 7)
			h_CLUST_ratio <- round(oh_CC/dh_CC, 7)
			c_CLUST_ratio <- round(oc_CC/dc_CC, 7)
		}
		row <- c(drugs, h_DEN_ratio, c_DEN_ratio, h_APL_ratio, c_APL_ratio, h_NCC_ratio, c_NCC_ratio, h_SLCC_ratio, c_SLCC_ratio, h_CLUST_ratio, c_CLUST_ratio)
		
		print = FALSE

		for (i in row) {
			if (i != row[1]) {
				if (i != 1) {
					print = TRUE
					}
				}
		}
		if (print) {
			cat(row, "\n", sep="\t")
		}
	 }
	 n<-n+1
	 if (time_mode) {
	 	finish_cocktail = Sys.time()
	 	cocktail_time <- difftime(finish_cocktail, start_cocktail, units="secs")
	 	cat("COCKTAIL n.", n, "-> ", cocktail_time, "secs", "\n", file = stderr())
	 } else {
	 	cat("Cocktail n.", n, "\n", file = stderr())
	 }
	 c = unlist(lapply(strsplit(readLines(c_file, n=1),"\t"), as.character))
}


end_time <- Sys.time()
total_time <- difftime(end_time, start_time, units="hours")
cat("TOTAL TIME -> ", total_time, "hours", "\n", file = stderr())



		
	




