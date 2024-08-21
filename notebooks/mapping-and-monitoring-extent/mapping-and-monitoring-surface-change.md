# Mapping and Monitoring Surface Change - Damage to Buildings and Infrastructure
This is an illustrative class to showcase the work done by the World Bank DAta Lab team to estimate the damage undertaken to buildings and points of interest due to Gaza-Israel conflict. This damage assessment was created using satellite Interferometric Synthetic Aperture Radar (InSAR) imagery.

## Data
The baseline data used for this analysis is the following:

1. [ACLED](https://acleddata.com): The Armed Conflict Location & Event Data Project (ACLED) is a disaggregated data collection, analysis, and crisis mapping project. ACLED collects information on the dates, actors, locations, fatalities, and types of all reported political violence and protest events around the world. The raw data is available through a license obtained by the World Bank.

2. [WorldPop](https://www.worldpop.org): Estimated population density per grid-cell. The units are number of people per square kilometre based on country totals adjusted to match the corresponding official United Nations population estimates that have been prepared by the Population Division of the Department of Economic and Social Affairs of the United Nations Secretariat (2019 Revision of World Population Prospects).This data was produced in 2020.

3. [OpenStreetMap](https://wiki.openstreetmap.org/wiki/About_OpenStreetMap): This is a crowdsourced dataset used to identify Points of Interest within Gaza. There is research that suggests that the OSM data for Israel is better than Gaza. However, it is currently the most accessible dataset available to the team.

4. [Sentinel-1](https://sentinels.copernicus.eu/web/sentinel/missions/sentinel-1/overview): Satellite imagery forms the core of this analysis. These data are obtained once in two weeks to detect changes to building structures.

5. [Google Earth Engine](https://earthengine.google.com): The heights of the buildings were obtained from Google Earth Engine.

(damage-assessment-methodology)=

## Methodology

The WB Data Lab team developed a multi-step methodology, designed to reduce costs of conducting the analysis while maximizing certainty and frequency of results for damage inventories. Using freely available, bi-weekly satellite radar data, the team has been running a set of automated algorithms to identify significant “changes” to the underlying infrastructure – especially changes in the heights and shapes of features. 
```{caution}
This analysis is still experimental; it can result in false positives and negatives.
```
The damage assessment analysis relies on the similarity measure computed using SAR medium resolution and openly accessible [Sentinel-1](https://sentinels.copernicus.eu/web/sentinel/missions/sentinel-1/overview) and the employed methodology can be split into 3 steps:

### 1. Image similarity computation

This similarity measurement, namely interferometric coherence ranging from $[0,1]$, provides values of high similarity (usually higher than $0.6$) over structures that had not suffered almost any variation, as for example buildings or man-made structures, while exhibits lower values (usually lower than $0.4$) over forest and agricultural areas (especially on large time separation between the acquisition time of the satellite data) over water (usually lower than $0.3$) bodies already between consecutive acquisitions.

We have employed all the Copernicus [Sentinel-1](https://sentinels.copernicus.eu/web/sentinel/missions/sentinel-1/overview) data acquired over the Gaza strip, which consists in 3 satellite orbits, namely ascending orbit 87 and 160 and descending orbit 94. Then, all the similarity maps were calculated with respect to the first image available for each of the orbits acquired in September 2022. This produces time series measurements that will allow to use a statistical approach to determine changes using anomaly detection method. Each orbit has 12 days repeat pass, so new updated products can be added regularly every 12 days.

```{figure} ../images/damage-assessment-calendar.png
---
---
Calendar with Copernicus Sentinel-1 acquisition dates after the war started on past 7th October 2023 until 9th January 2023.
```

### 2. Change detection based on time series statistics

For the time series change detection, pre-war data from September 2022 until end September 2023 was computed to obtain statistics in non-war situation. These statistics are also used to classify the newer data acquired during the war period, October 2023 until the present time, with pixels for which had been detected a change (potentially attributable to war damage) using anomaly detection method with different thresholds (i.e. 3 sigma rule and 2.5 sigma rule).

The 3-sigmas rule considers as an anomaly those values that are lower than the average minus 3 times the standard deviation. In other words, anomalies are those values that are lower than 99.6% of the values in the pre-war context. Similarly, the 2.5-sigma rules consider anomalies those values that are lower than the average minus 2.5 standard deviations. The 3-sigma rule is more conservative while the 2.5 sigma rule can result in a higher number of false alarms. See example of this empirical rule below.

```{figure} ../images/damage-assessment-empirical-rule.jpg
---
scale: 50%
---
Illustration of the empirical rule
```

### 3. Infrastructural damage assessment using the change maps and the vector layers

For the final assessment of infrastructural damage, in roads, points of interest or buildings, the different layers are overlaid and computed whether each feature has been damage or not. For the different features their potential damage was computed as follows:

- In case of roads, the layer is split into 10 meters roads, and it is computed whether each of the segments had been damaged or not,

- In case of the points-of-interest (POI):

  - POIs have been attributed a buffer of 10-meter radius and are overlaid to the change map to detect whether they are likely damaged or not.

  - Area POIs have been overlaid with the change map to detect whether they are likely damaged or not.

- In case of buildings,

  - Using OpenStreetMap building layer, building polygons are overlaid with the change map and computed which is the percentage (in $[0,1]$ range) of their area which is likely damaged. OSM layers comes also with their possible landuse information.

  - Using Microsoft footprint layer, building polygons are overlaid with the change map and computed which is the percentage (in $[0,1]$ range) of their area which is likely damaged, but, unlike OSM, they do not come with landuse information.

## Limitations

```{important}
The following damage assessment maps are based on preliminary estimates and have not been verified through field survey or satellite imagery. They do not reflect the final estimations by the [World Bank](https://www.worldbank.org/en/country/westbankandgaza). The project team is currently working on procuring high resolution imagery to verify whether the buildings identified as damaged have collapsed or experienced impact.
```

```{caution}
Using OpenStreetMap (OSM) and Interferometric Synthetic Aperture Radar (InSAR) for estimating building damage has its strengths but also several limitations:

- **Incomplete Data:**
    - **Coverage Discrepancies:** OSM data might lack comprehensive coverage, especially in certain regions or areas with limited community input or verification. This can lead to incomplete or outdated information about buildings. For instance, {cite:t}`BITTNER201734` outlined the Israeli domination of OSM entries, whereas there are far fewer mappers in Palestine.
    - **Quality Variability:** Data quality can vary significantly as it relies on volunteer contributions. Accuracy in mapping may vary, leading to inconsistencies or errors in identifying buildings

- **Temporal Limitations:**
    - **Data Timeliness:** OSM data might not be up to date due to infrequent updates or changes in the landscape that haven't been reflected yet.
    - **InSAR Timing:** InSAR data might not capture the most recent changes or damages, especially in rapidly evolving situations where damage continues to occur after the data collection period.

- **Contextual Understanding:**
    - **Local Knowledge:** OSM data might lack contextual information crucial for assessing damages accurately, such as the original state of buildings or variations in construction materials.
    - **Verification Challenges:** Verifying damages solely based on remote sensing data might lack the on-ground verification necessary for a comprehensive understanding of the situation.

- **Conflict Data**
ACLED is a crowdsourced dataset and is highly likely that the numbers are underreported. ACLED keep changing their data based on local validation.
```

## References

```{bibliography}
:filter: docname in docnames
```
