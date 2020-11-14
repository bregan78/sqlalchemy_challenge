
# sql-challenge



##This repo contains the following:
1. Climate Analysis and Exploration
2. Climate App



* Climate Analysis and Exploration
	- Precipitation Analysis
		- Design a query to retrieve the date and prcp values from the last 12 months of precipitation data (from the most recent date in the database).
		- Load the query results into a Pandas DataFrame and set the index to the date column.
		- Sort the DataFrame values by date.
		- Use Pandas to print the summary statistics for the precipitation data.
	- Station Analysis
		- Design a query to calculate the total number of stations.
		- Design a query that lists all stations with their corresponding observation count in descending order.
		- Design a query to retrieve the last 12 months of temperature observation data (TOBS) for the most active station.
			-Plot the results as a histogram with bins=12.

* Climate App
	- Routes
		- /
			- List all routes that are available.
		- /api/v1.0/precipitation
			- Using the query from part 1 (most recent 12 months of precipitation data), convert the query results to a dictionary using date as the key and prcp as the value.
			- Return the JSON representation of your dictionary (note the specific format of your dictionary as required from above).
		- /api/v1.0/stations
			- Return a JSON list of stations from the dataset.
		- /api/v1.0/tobs
			- Query the dates and temperature observations of the most active station for the latest year of data.
			- Return a JSON list of temperature observations (TOBS) for that year
		- /api/v1.0/<start> and  /api/v1.0/<start>/<end>
			- Create a query that returns the minimum temperature, the average temperature, and the max temperature for a given start or start-end range
			- When given the start date only, calculate min, max, and avg for all dates greater than and equal to the start date
			- When given the start and the end date, calculate the min, avg, and max for dates between the start and end date inclusive
			- Return a JSONified dictionary of min, max, and avg temperatures
			
	
