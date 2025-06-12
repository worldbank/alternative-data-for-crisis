# Final Project
To wrap up the course, you will be presented with two recent crisis events from around the world. You will need to 
create an analysis of the immediate impact based on what you have learned during the course.

```{note} 
If you are interested in working on a different crisis event not listed here, discuss it with the instructor.
```

## Crisis Events
### Earthquake in Morocco
The 8th of February 2023, an earthquake struck Morocco's Al Haouz Province. Its epicenter was 73.4 km southwest of Marrakesh.
For this crisis, the client requested you the following deliverables:
- Earthquake intensity map by the lowest administrative level possible.
- Distribution of hospitals by the earthquake intensity that affected them. **Note**: Histogram of hospitals where 
the x-axis is the intensity of the earthquake affecting the hospital, and the y-axis is the number of hospitals.
- Distribution of people by the earthquake intensity that affected them. Idem above.
- Changes in the national conflict index across the years, use all available data. Detect whether there are significant changes in the 
conflict index after the earthquake in the areas most affected by the natural disaster. 
- Scatter plot where the x-axis is the average earthquake intensity and the y-label is the change in NTL. The change in 
NTL should be calculated as the average radiance during weekdays four weeks before the earthquake against the radiance 
in the week (weekdays) after the earthquake. The datapoints are the administrative level 3 boundaries.

### Flood in Bangladesh
On August 21, 2024, heavy rainfall, coupled with a surge of water released from a dam in India's Tripura, resulted in severe flooding that affected 73 upazilas (sub-districts) and 528 unions/municipalities across 11 districts in northeastern and southeastern Bangladesh. [Source](August_2024_Bangladesh_floods). 

At the Data Lab, we were able to collect the flood data from the 6th of November on. 

For this crisis event, the client requested you the following deliverables:
- An interactive map showing flooded areas at the pixel level.
- A map showing approximately flooded area at administrative level 3 boundary.
- Using NTL, calculate the radiance at administrative level 3 to try to detect changes after the flood.
- Calculate how many people got affected by the flood. Note: Ideally, for this step you would resample the population to the flood pixels.
- Create a map at administrative level 3 showing number of affected people by the flood. 
- Calculate how many hospitals and schools are in areas that are still flooded. Hint: You can vectorize the raster layer and intersect it with the pois layer.


## Guidelines on how to work on this assignment
The following section will give you some steps to follow to successfully accomplish the tasks:
1. Create a folder for saving all the data that you will be using in the analysis. It is a good idea to have a backup of
this data in the cloud.
2. Download the base maps for the region of interest. Explore what is available and try to find what is the lowest geography 
level you can find data for. 
3. Download the specific data for the crisis event you are analyzing.
4. Always remember to document where you downloaded the data from. If you try to do this at the end of the project, it
might be more difficult.
5. Create a GitHub repository for each crisis event. 
6. Work in branches. Create branches for incorporating new analysis to the repository. Once you are done, create a PR 
and merge the new branch to `main/develop`.
7. Once you merged to `main`, make sure that your changes were deployed correctly.

``` {note}
Do not upload datasets to GitHub. This tool is not meant for saving data.
```

## Deliverables
Your analysis is expected to be delivered as a link to a deployed web-book 2 weeks after the end of the course. 