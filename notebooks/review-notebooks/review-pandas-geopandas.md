# Pandas and Geopandas Review
In order to successfully complete this course, learners need a background in Data Analysis and Geospatial Analysis.
The code is designed to be completed using Python and its libraries Pandas, Geopandas and Rasterio, or similar. However, if you are 
an R or GIS user, you most likely will be able to complete the course as well. 

This section is organized in 3 parts:
- A list of resources to review data analysis skills
- A list of resources to review geospatial skills
- A final fictional case study to assess your abilities and reinforce them accordingly. In the next section we provide 
the solutions to the exam so you can autoevaluate your performance. 

## Data Science Skills
The following resources might be of your interest to grow your skills in the Data Analysis field.
- [Introduction to Computer Science and Programming in Python](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/?) 	
- [Python Excercises](https://www.w3schools.com/python/python_exercises.asp?)
- [Pandas Online Course](https://www.kaggle.com/learn/pandas?)
- [Data Science for Beginners](https://github.com.mcas.ms/microsoft/Data-Science-For-Beginners/tree/main?tab=readme-ov-file)

## Geospatial Analysis Skills
The following resources might be of your interest to grow your skills in Geospatial Analysis:
- [What is Geospatial Data?](https://www.ibm.com/think/topics/geospatial-data?)
- [Introduction to Geospatial Concepts](https://datacarpentry.github.io/organization-geospatial/index.html?)
- [Coordinate Systems and Projections](https://sites.dartmouth.edu/gis-geography/coordinate-systems-and-projections/?)
- [Python for Geographic Data Analysis](https://pythongis.org/index.html)
- [Rasterio Quick Start](https://rasterio.readthedocs.io/en/stable/quickstart.html)

## Case Study (Fictional)
>Last Monday, there was an earthquake in the city of San Juan, San Juan, Argentina, with a magnitude of 7.5 on the 
> moment magnitude scale. We need you to create a report answering the below questionnaire with the below data:
> - Epicenter's latitude and longitude: -31.553, -68.529
> - [Population's Raster from Worldpop](https://worldbankgroup.sharepoint.com/:i:/r/teams/DevelopmentDataPartnershipCommunity-WBGroup/Shared%20Documents/Projects/Data%20Lab/Alternative%20Data%20for%20Crisis/datasets_review_python/arg_ppp_2020_constrained.tif?csf=1&web=1&e=sZdHEi)
> - [Healthcare Facilities from HDX](https://worldbankgroup.sharepoint.com/:u:/r/teams/DevelopmentDataPartnershipCommunity-WBGroup/Shared%20Documents/Projects/Data%20Lab/Alternative%20Data%20for%20Crisis/datasets_review_python/health_care_facilities.zip?csf=1&web=1&e=kfv2TQ)
> - [H3 level 6 hexagons]()
You were requested to provide:
- The number of population on a buffer of 15 Km from the epicenter as an estimation of affected population.
- The number of healthcare facilities on a buffer of 15 Km from the epicenter as an estimation of affected healthcare 
facilities.
- An interactive map that shows the 15 Km buffer from the epicenter, the population by h3 level 6 hexagons and the 
healthcare facilities in the buffer. 