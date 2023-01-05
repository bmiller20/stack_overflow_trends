# stack_overflow_trends
This Project is to practice how to safely delete data in a large dataset with many null data points


# Project Overview #
The project i sto put together several statisical analyses about the community to educate your client about the potential hiring marker for their company

# Steps #

### Explore Data ###

We are going to start with some EDA. That way we can start looking at the data fields and see what is there and more importantley what is not

*todo*
* Import 'developer_dataset.csv'
* Print Column Names
* Run the count of data in each row
* Find teh average, min max, the number of null points


### Delete Highly Missing Data ###
The rule for this project is that we can delete rows with 60% or more of its data missing

*todo*
* Find the Percentage of Missing data in each column
* Remove columns with lots of missing data


### Analyze Developers By Country ###

We are going to start looking about how many developers are in each country in the dataset

*todo*
* Determine Missing Datafor each country 
* Create a Bar Chart for Employment and Devtype mising data
* Delete the subsets of data using listwise deletion


### Analyze the Distribution of employment and developer types by Country ###

Break it down into a list of 
- Front End
- Back End
- Full Stack
- Mobile Development
- Administration Roles

*todo*
- Create a Series of Barcharts describing the breakdown of each developer role for each country


### Investigate Developer Undergrad Majors ###

*todo* 
- Take a look at the distrubtion of majors each year
- Use NOCB to fil in the gaps for missing data
- Analyze the distribution for each year for each major.

### Examinne the relationship between Years of Experience and Compensation ###

- Create a new dataframe with the Year, YearsCodePro, ConvertedComp columns
- Create a box plot for YearsCoded and one for Converted Comp
- Use Multiple Imputation to fill in missing data. 
- Then create a boxplot with Converted comp and years coded