# create some data for the pie chart
year <- c(2008,2009,2010,2011,2012)
accidents <- c(20873,19542,21243,22387,21056)
colors <- c("red", "blue", "green", "purple", "orange")
slice_labels <- paste(year, round(accidents/sum(accidents)*100, 1), "%", sep = " ")

# create the pie chart with customizations
pie(populations, 
    labels = slice_labels, 
    col = colors,
    main = "Accidents occured in the year 2008 to 2012",
    clockwise = TRUE,
    density = 900,
    border = "white")

