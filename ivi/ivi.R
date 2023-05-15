library(influential)

args <- commandArgs(trailingOnly= TRUE)

# Preparing the data
MyData <- read.table(args[1])       
	

# Reconstructing the graph
My_graph <- graph_from_data_frame(MyData)        

# Extracting the vertices

GraphVertices <- V(My_graph)

if (length(args) > 1) {
	GraphIndex <- c()
	hits <- scan(args[2], what="", sep="\n")
	for (vertex in V(My_graph)) {
		if (V(My_graph)[vertex]$name %in% hits) {
			GraphIndex = c(GraphIndex, vertex)
		}
	}
	GraphVertices <- GraphVertices[GraphIndex]
}

    



# Calculation of IVI
My.vertices.IVI <- ivi(graph = My_graph, vertices = GraphVertices, 
                       weights = unlist(MyData[3]), directed = FALSE, mode = "all",
                       loops = TRUE, d = 3, scaled = TRUE)

nodes <- names(My.vertices.IVI)

for (i in 1:length(My.vertices.IVI)) {
	cat(nodes[i])
	cat("\t")
	cat(My.vertices.IVI[i])
	cat("\n")
}

