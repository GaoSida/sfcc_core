library(ggplot2)
library(ggmap)
map <- 
    readRDS("./Kaggle/input/map.rds")

ggmap(map, extent='device', legend="topleft") +
geom_point(aes(x=X, y=Y, colour=Category), data=mapdata ) +  
ggtitle('Violent Crime in San Francisco')