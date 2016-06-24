# Import Library
library(sqldf)
library(ggmap)
library(ggplot2)
library(plotrix)

# Load data training
dftraining <- read.csv(file="./Kaggle/input/train.csv",head=TRUE,sep=",")
map <- readRDS("./Kaggle/input/map.rds")

# Select the Top 5 Crime excluding ("NON-CRIMINAL","OTHER OFFENSES") 
dfGroup <- sqldf('select Category,count(*) nro from dftraining where Category not in ("NON-CRIMINAL","OTHER OFFENSES") group by Category order by 2 desc')
dfMax <- dfGroup[1:5,]

# Pie Chart Number of Crime for Category
lbls <- paste(as.character(dfMax[, "Category"]), format(as.numeric(dfMax[, "nro"]),big.mark=","))
pie3D(as.numeric(dfMax[, "nro"]), labels = lbls, explode=0.1,main="Top 5 Crime")

# Custom Color for every Crime
vectorcolor <- c("red","green","cyan","blue","orange")
dfMax$colorz <- vectorcolor

# Convert data frame dfMax to vector
dfMax2 <- as.character(dfMax[, "Category"])

# Filter the top 5 Crime
dftrainingFilter <- subset(dftraining, Category %in% dfMax2)
dftrainingFilter <- dftrainingFilter[c(2,5,8,9)]


# Merge color custom and data training
dfFinale <- merge(x = dfMax, y = dftrainingFilter, by = "Category", all = TRUE)

# Create San Francisco Map
#map<-get_map(location="sanfrancisco",zoom=12,source="osm",color="bw")

# Plot point into Map
plot <- ggmap(map) + 
		labs(x = "Longitude",  y = "Latitude")+
		ggtitle("The Top 5 San Francisco Crime") +
			geom_point(data=dfFinale, aes(x=dfFinale$X, y=dfFinale$Y, color=dfFinale$Category), alpha=0.2) +
			scale_colour_manual(name="Crime" ,labels=dfMax2,values=vectorcolor)

# Save Map to local File 
ggsave("Top5Crimes.png", plot, width=14, height=10, units="in")
#dev.off()