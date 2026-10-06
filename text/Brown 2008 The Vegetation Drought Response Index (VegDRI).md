**GIScience & Remote Sensing** 



**ISSN: 1548-1603 (Print) 1943-7226 (Online) Journal homepage: www.tandfonline.com/journals/tgrs20** 



# **The Vegetation Drought Response Index (VegDRI): A New Integrated Approach for Monitoring Drought Stress in Vegetation** 

**Jesslyn F. Brown, Brian D. Wardlow, Tsegaye Tadesse, Michael J. Hayes & Bradley C. Reed** 

**To cite this article:** Jesslyn F. Brown, Brian D. Wardlow, Tsegaye Tadesse, Michael J. Hayes & Bradley C. Reed (2008) The Vegetation Drought Response Index (VegDRI): A New Integrated Approach for Monitoring Drought Stress in Vegetation, GIScience & Remote Sensing, 45:1, 16-46, DOI: 10.2747/1548-1603.45.1.16 

**To link to this article:** <u>https://doi.org/10.2747/1548-1603.45.1.16</u> 











Published online: 15 May 2013. Submit your article to this journal Article views: 3655 View related articles 





Citing articles: 84 View citing articles 

Full Terms & Conditions of access and use can be found at https://www.tandfonline.com/action/journalInformation?journalCode=tgrs20 

## **The Vegetation Drought Response Index (VegDRI): A New Integrated Approach for Monitoring Drought Stress in Vegetation** 

### **Jesslyn F. Brown**<sup>**1**</sup> 

_SAIC, Contractor to U.S. Geological Survey (USGS), Earth Resources Observation and Science Center, 47914 252nd Street, Sioux Falls, South Dakota 57198-0001_ 

### **Brian D. Wardlow, Tsegaye Tadesse, and Michael J. Hayes** 

_National Drought Mitigation Center, School of Natural Resources, University of Nebraska-Lincoln, 811 Hardin Hall, 3310 Holdredge Street, P.O. Box 830988, Lincoln, Nebraska 68583-0988_ 

### **Bradley C. Reed** 

_U.S. Geological Survey, Flagstaff Field Center, 2255 N. Gemini Dr., Flagstaff, Arizona 86001_ 

**Abstract:** The development of new tools that provide timely, detailed-spatial-resolution drought information is essential for improving drought preparedness and response. This paper presents a new method for monitoring drought-induced vegetation stress called the Vegetation Drought Response Index (VegDRI). VegDRI integrates traditional climate-based drought indicators and satellite-derived vegetation index metrics with other biophysical information to produce a 1 km map of drought conditions that can be produced in near-real time. The initial VegDRI map results for a 2002 case study conducted across seven states in the north-central United States illustrates the utility of VegDRI for improved large-area drought monitoring. 

#### **INTRODUCTION** 

Droughts are normal, recurring climatic events that frequently trigger negative impacts on many sectors of society, including agriculture, energy, recreation, tourism, and transportation (Rosenberg, 1978; Wilhite, 2000). During the past century, virtually all regions of the United States have experienced several extended severe drought episodes, as well as many short-term droughts, resulting in considerable impacts and economic losses (Wilhite, 2000). In comparison to other natural hazards, droughts 

1 jfbrown@usgs.gov. Work performed under USGS contract 03CRCN0001. 

_GIScience & Remote Sensing_ , 2008, **45** , No. 1, p. 16–46. DOI: 10.2747/1548-1603.45.1.16 Copyright © 2008 by Bellwether Publishing, Ltd. All rights reserved. 

**16** 

**17** 

VEGETATION DROUGHT RESPONSE INDEX 

frequently have larger associated costs because of the serious economic, environmental, and social consequences that often result from prolonged and widespread drought events (Wilhite, 1997; NCDC, 2007). Cutter and Emrich (2005) found that droughts accounted for 8 percent of the total costs (that is, direct losses of crops and property) of all natural hazards in the United States from 1960 to 2003. Ross and Lott (2003) also pointed out that the 11 major droughts experienced in the United States between 1980 and 2003 caused the largest percentage (42 percent) of weather-related monetary losses during that period. In 1995, the Federal Emergency Management Agency (FEMA) reported that $6–8 billion in losses on average were caused by drought events in the United States each year, more than for any other weather-related disaster at that time (FEMA, 1995). As a result of the major impacts that result from drought events, the development of improved drought monitoring tools is vital for providing decision makers with accurate and timely information that is needed for effective drought planning, mitigation, and response activities (WGA, 2004). 

Drought monitoring is challenging because of the immense spatial and temporal variability exhibited by each drought event. The term drought also lacks a single technical definition because the characteristics that define a drought event may vary by both location and sector. Therefore, no single method can be used to adequately characterize and monitor drought. Monitoring techniques have to be adapted to capture the time-, location-, and sector-specific characteristics of drought. Improvements in drought monitoring techniques and products, such as higher spatial resolution and the timely delivery of information in a variety of accessible formats (for example, maps, descriptive text, and statistics), increase the value and relevancy of the information available to decision makers, and thereby enhance and support drought response and mitigation activities. A recent report by the United States Western Governors’ Association (WGA), describing the vision of a National Integrated Drought Information System (NIDIS), identified these types of improvements as a top priority for enhancing the nation’s drought monitoring capabilities (WGA, 2004). 

Over the past decade, significant progress has been made in drought monitoring worldwide. The accuracy and spatial precision of climate-based indicators have improved with technological advances in meteorological instrumentation and the expansion of weather station networks. This has improved both the spatial and temporal resolution of the climate data available for drought monitoring. However, climatebased monitoring approaches still have a restricted level of spatial precision for monitoring drought patterns because they use discrete, point-based meteorological measurements collected at weather station locations. As a result, climate-based monitoring tools characterize relatively broad-scale drought patterns and the level of accuracy and spatial detail in the information they provide depends on the density and geographic placement of stations across the landscape. Since the 1980s, many studies have capitalized on the synoptic, timely, and spatially continuous characteristics of remotely sensed data gathered by satellites to analyze and monitor vegetation conditions over large areas (Goward et al., 1985; Malingreau, 1986; Di et al., 1994; Goetz and Prince, 1996; Reed et al., 1996; Jakubauskas et al., 2002). Satellite-based observations have proven very useful for detecting vegetation condition anomalies (that is, apparent declines in vegetation health), but the specific cause or causes for the vegetation stress may not always be determined solely from the remotely sensed data. A number of natural (for example, drought, flooding, fire, pest infestation, and hail 

**18** 

BROWN ET AL. 

damage) and anthropogenic (for example, land cover/land use conversion) events can produce these anomalies (Kogan, 1990; 1997; Asner et al., 2000; Breshears et al., 2005; Domenikiotis et al., 2003; Franke and Menz, 2007; Goetz et al., 2006; Henebry and Ratcliffe, 2003; Peters et al., 2000; Wang et al., 2003). Thus, remote sensing data provides a means to monitor detailed spatial patterns of vegetation conditions, but it is often difficult to distinguish drought-related vegetation stress from vegetation changes caused by these other drivers without additional information. As a result, the integration of coarser-resolution climate data and higher-resolution, satellite-based vegetation observations provides an alternative approach to better monitor and characterize the spatial extent, intensity, and local variability of drought’s affect on vegetation conditions. 

The goal of this paper is to introduce a new drought monitoring methodology called the Vegetation Drought Response Index (VegDRI), which integrates historical climate data and satellite-based earth observations with other biophysical information (for example, land cover, land use, and soils) to produce a 1 km–resolution indicator of the geographic extent and intensity of drought stress on vegetation. This approach builds on the traditions from both the climate and remote sensing communities for drought monitoring and utilizes new data mining analysis techniques to identify historical climate-vegetation relationships related to the drought phenomenon. This paper provides a review of existing methods and data used for drought monitoring to support the scientific basis for the VegDRI methodology. We present the specific inputs and methods used for VegDRI and then show initial VegDRI results from a pilot study conducted over a seven-state region of the central United States (Fig. 1) for 2002. The pilot study and following discussion highlights the strengths of this index over more traditional drought indicators and illustrates the potential utility of this tool for improved drought monitoring. 

#### **BACKGROUND** 

#### **Monitoring with Climate-Based Drought Indices** 

Traditionally, climate and meteorological data have been the primary sources for drought information. Climate-based drought indices are often used to support drought planning decisions and to trigger mitigating actions in different parts of the world (Hayes, 2003; Keyantash and Dracup, 2002). These indices typically characterize the intensity of dryness as compared to the long-term average or normal condition and are usually calculated from one or more of the following variables: rainfall, temperature, snow pack, stream flow, soil water holding capacity, and other water supply indicators. As discussed earlier, climate-based indicators are traditionally calculated from point-based measurements collected at meteorological stations and climate data are not available in between stations. Statistical estimation methods such as kriging must be used to estimate the values of specific climate parameters between stations and obtain a continuous spatial coverage of general climate patterns. In addition, the weather stations within an observing network can be unevenly distributed and are often limited in number, particularly at higher elevations and in sparsely populated areas. This further limits the spatial accuracy and detail in the climate patterns that can extrapolated from station-based measurements. 

**19** 

VEGETATION DROUGHT RESPONSE INDEX 



**Fig. 1.** The seven-state study area in the north-central United States and the geographic locations of the 776 weather stations used for VegDRI model development. 

Two climate-based drought indices, the Standardized Precipitation Index (SPI) and the Palmer Drought Severity Index (PDSI), were selected for incorporation into VegDRI because they are among the most commonly used indicators for drought monitoring in the United States and are key indices analyzed during the construction of the widely accepted USDM (Svoboda et al., 2002). 

**Standardized Precipitation Index (SPI).** The SPI was designed to quantify the precipitation anomaly for a specified time period (for example, previous 1, 3, 5, or 12 months) for a location (for example, weather station) based on the long-term precipitation record over that specific time interval (McKee et al., 1995). The SPI is calculated by fitting the long-term record of precipitation over a specific time step to a probability distribution, which is then transformed into a gamma distribution so that the mean SPI for a specific location and time period is zero (Edwards and McKee, 1997). The SPI value is positive if the precipitation over a particular time period is greater than the historical mean precipitation and is negative if the precipitation is less than the historical mean precipitation. SPI provides the temporal flexibility to assess conditions over multiple time intervals, allowing the index to be used to monitor both shorter-term agricultural drought and longer-term hydrologic drought. 

**20** 

BROWN ET AL. 

**Palmer Drought Severity Index (PDSI).** The PDSI has been a very prominent climate-based drought index used in the United States (Keyantash and Dracup, 2002). The PDSI calculation is based on a simple supply-and-demand model of a water balance equation that builds on both the precipitation and temperature history for a location so that a calculated PDSI value represents a combination of the current conditions and previous PDSI values (Palmer, 1965). Several parameters are used in the PDSI calculation, including precipitation, temperature, and soil properties (that is, available water-holding capacity). The response of PDSI to an emerging drought event may lag by weeks or months compared to a quicker response index such as SPI (Hayes et al., 1999), but PDSI is a still useful indicator of longer-term drought conditions. 

A new self-calibrated PDSI was recently developed by Wells et al. (2004). In the self-calibrated PDSI, empirical constants and duration factors in the PDSI computation are dynamically calibrated to the local characteristics of each weather station. This adjustment was designed to keep the original intentions of Palmer’s (1965) drought index intact, while improving the spatial comparability of PDSI values and calibrating the index so that extreme dry and wet events would occur approximately two percent of the time at any location, as recommended in the literature (Guttman et al., 1992; Hayes et al., 1999). 

**U.S Drought Monitor (USDM).** The USDM (Svoboda et al., 2002) is a state-ofthe-art drought monitoring tool used in the United States. The USDM, operational since 1999, is developed using a hybrid approach that considers a number of variables such as short- and long-term climate-based drought indicators, hydrologic indices, and remote sensing information. The USDM map provides a general assessment of drought conditions (both agricultural and hydrologic) across the nation. The USDM map is updated weekly and has a spatial resolution at the approximate scale of a climate division (Svoboda et al., 2002). Climate divisions are an administrative construct of the National Oceanic and Atmospheric Administration (NOAA) that can vary in area from tens to hundreds of km<sup>2</sup> across the conterminous United States (Lackey et al., 2007). In all, there are 344 climate divisions. The spatial resolution of the USDM has been adequate for national- and state-level policy makers and the media, and it has been used as a trigger for federal drought relief programs (for example, USDA’s Livestock Assistance Grant Program in 2006; Svoboda et al., 2002). However, the coarse spatial resolution of the USDM limits its utility for drought response and mitigation at a more localized level, and the development of new, higher resolution tools that provide more localized monitoring across the country has been identified as a priority (WGA, 2004). 

#### **Satellite-Based Monitoring of Vegetation Conditions** 

Satellite observations provide a valuable source of timely, spatially continuous information for monitoring vegetation dynamics (for example, physiological stages) and conditions across large areas. In particular, time-series Advanced Very High Resolution Radiometer (AVHRR) normalized difference vegetation index (NDVI) data have been widely used to monitor vegetation at regional to global scales (Tucker et al., 1985; Malingreau, 1986; Townshend et al., 1987; Reed et al., 1994; Myneni et al., 1997; Jakabauskas, 2002; DeBeurs and Henebry, 2004) and have inherently 

**21** 

VEGETATION DROUGHT RESPONSE INDEX 

higher spatial resolution (ranging from 1 km<sup>2</sup> to 16 km<sup>2</sup> ) than traditional climatebased indicators such as the USDM. The NDVI (Rouse et al., 1974; Tucker, 1979) is a numerical transform of the visible red (red) and near infrared (NIR) spectral bands, which takes the form: 



NDVI represents a dimensionless, radiometric measure that capitalizes on the differential response of the incident visible red (absorbed by chlorophyll) and NIR (reflected by the spongy mesophyll layer of leaves) radiation with the vegetation canopy and has been found to be correlated with the relative abundance and condition of green vegetation (Asrar et al., 1989; Baret and Guyot, 1991). As a result, timeseries NDVI observations from AVHRR have proven useful for the quantification of seasonal events (Reed et al., 1994; Reed et al., 1996; Yang et al., 1998; Schwartz, 1992) and biophysical vegetation characteristics (for example, leaf area index and biomass) (Hoff et al., 1995; Sannier et al., 2002; Wang et al., 2005; Gonzalez-Alonso et al., 2006; Wessels et al., 2006), the classification of land cover types (Loveland et al., 1991, 1995, 2000; DeFries and Townshend, 1994; DeFries et al., 1998, Hansen et al., 2000), and the characterization of vegetation conditions (Reed et al., 1996; Yang et al., 1998; Jakubauskas et al., 2002). This large body of research has shown that time-series NDVI observations from AVHRR (and other instruments aboard global polar-orbiting satellites) provide the required information for monitoring vegetation patterns and conditions at 1 km<sup>2</sup> to 16 km<sup>2</sup> scales across large geographic areas. 

A strong relationship between climate- and satellite-derived vegetation indices (VIs) has been established (Di et al., 1994; Yang et al., 1998; Rundquist and Harrington, 2000; McVicar and Bierwirth, 2001; Ji and Peters, 2003), which indicates that VIs are an effective measure for monitoring climate-related changes in vegetation conditions. McVicar and Bierwirth (2001) found a strong correlation ( _r_<sup>2</sup> = 0.81) between accumulated rainfall and integrated NDVI and surface temperature in their investigation of AVHRR data for drought assessment. Yang et al. (1998) also found a significant positive correlation between time-integrated NDVI and summer and spring precipitation over the grasslands of the central United States. Significant correlations between monthly NDVI and SPI during the growing season were also reported by Ji and Peters (2003) in the central Great Plains. They found NDVI to be an effective indicator of “vegetation moisture condition” and found the relationship between NDVI and SPI to be the strongest in areas with low soil-water holding capacity. 

The utility of time-series VI derivative measurements (primarily from the 16 km<sup>2</sup> AVHRR Global Vegetation Index; Kidwell, 1990) for drought monitoring in the United States and internationally has been demonstrated since the early 1990s (Kogan, 1990; Kogan, 1995; Liu and Kogan, 1996; Hayes and Decker, 1996; Kogan, 1997; Unganai and Kogan, 1998). Most of this research was based on a transformation of the NDVI data to an indicator called the Vegetation Condition Index (VCI) (Kogan, 1990, 1997). The VCI and TCI (an index calculated from AVHRR thermal channel data) were found to have good correlation (ranging from 0.45 to 0.97) with a corn yield ratio (percent of 1986–1994 mean yield) at the district level in Zimbabwe, but the timing of the occurrence of the highest correlation varied by district (Unganai and Kogan, 1998). Similar to the NDVI, the VCI can also be sensitive to other envi- 

**22** 

BROWN ET AL. 

ronmental phenomena (for example, flooding, wildfire, pest infestation, hail, etc.), and this may result in an incorrect interpretation or identification of a drought-like signal. 

The value of multi-temporal, satellite-based VI observations for characterizing vegetation conditions and patterns is clear from this previous body of research, but identifying the specific cause(s) of significant anomalies in the dynamic vegetation patterns exhibited in the VI data is difficult without the use of additional ancillary information. A number of environmental factors (for example, flooding, hail, plant disease, pest infestation, fire, and human-induced land changes) can degrade vegetation conditions and produce a similar multi-temporal VI signal, as seen in areas experiencing drought stress (Asnar et al., 2000; Peters et al., 2000; Domenikiotis et al., 2003; Henebry and Ratcliffe, 2003; Wang et al., 2003; Breshears et al., 2005; Goetz et al., 2006; Franke and Menz, 2007). As a result, satellite VI data may decline, but without the integration of ancillary information such as climate data, there is uncertainty as to the specific cause(s) of the vegetation stress. Therefore, an effective drought monitoring approach should consider both climate- and satellite-based information, as well as other environmental parameters that may influence the effects of drought and its severity on vegetation, such as soil properties or land cover type. 

#### **Data Mining Techniques for Integrating Complex Environmental Information** 

Data mining techniques, which were originally developed in the machine learning community, are increasingly being used for variety of environmental applications (Bell, 1999; De’ath and Fabricus, 2000; Zhang et al., 2005; Wylie et al., 2007) and have shown considerable potential for drought monitoring (Harms et al., 2002; Tadesse et al., 2005). The term data mining refers to a set of analysis tools and techniques that incorporate methods from machine learning, pattern recognition, statistics, and visualization and are designed to identify complex patterns and relationships in large numbers of variables (Two Crows Corporation, 1999). This approach has several advantages over traditional analysis techniques, including the flexibility to handle a variety of data types (for example, nominal, interval, and ratio); the ability to handle data without a normal distribution (non-parametric) and hierarchical relationships among variables; efficient processing of large data volumes; and transparent, interpretable model outputs (De’ath and Fabricus, 2000). As a result, a data mining approach was appropriate for VegDRI given the complexities in measuring and monitoring drought discussed earlier, as well as the large number of variables and considerable volume of climate, satellite, and biophysical information analyzed in this approach. 

#### **DATA AND METHODS** 

#### **Overview of VegDRI Methodology** 

The VegDRI methodology represents a new approach to drought monitoring by integrating traditional climate-based drought index information and satellite-based NDVI measures of vegetation conditions with several biophysical characteristics. This index, by design, specifically targets the effects of drought on vegetation by 

**23** 

VEGETATION DROUGHT RESPONSE INDEX 

considering the general vegetation conditions as observed by satellite and the level of dryness experienced for a given location. Additional environmental characteristics are also represented in this approach given the different climate-vegetation response relationships that can occur for different land cover types, soil types, and land use practices. 

The VegDRI methodology consists of three primary steps. The first step was to process, summarize, and organize the data for the eight variables (Table 1) used in VegDRI into a database (Section 3.2). A 16-year historical record (1989–2005) of climate-based drought index and satellite-derived VI observations and information from four temporally static biophysical variables were included in the training database. For each variable, information was summarized for 776 weather station locations across the seven-state study area (Fig. 1), entered and sequentially ordered in the database, and then subdivided into three seasonal phases (Table 2) for model development. The second step was to generate an empirically derived model for each phase by applying a supervised classification and regression-tree (CART) analysis technique to information in the database (section 3.3). The third step was to apply the seasonal models to the geospatial data to produce a 1 km resolution VegDRI map for the study area (section 3.4). The VegDRI map contains seven categories of varying levels of drought-induced vegetation stress, based on the PDSI drought classification scheme (Palmer, 1965). The seasonal models were applied at a two-week time-step to the geospatial data to produce a map for each bi-week within their respective phase. 

#### **Climate Data Inputs for VegDRI** 

The SPI and self-calibrated PDSI were calculated from the National Agricultural Decision Support System (NADSS) (http://nadss.unl.edu/), which collects, processes, and formats historical climate data provided from the Applied Climate Information System (ACIS) (http://rcc-acis.org) (Hubbard et al., 2004). Rigorous quality control was used to remove any meteorological stations with any or all of the following characteristics: (1) an insufficient historical record (less than 30 years); (2) too many missing observations (greater than 10 percent of the station record missing); and (3) spurious PDSI or SPI results. A total of 776 meteorological stations were retained across the study area (Fig. 1) and a 17-year time series of SPI and self-calibrated PDSI values were calculated on a bi-weekly (14-day) time-step for these locations. 

**SPI Data** . Because the SPI has the inherent flexibility to be calculated over various time spans, an optimal SPI interval had to be selected for each seasonal phase. A single SPI interval was used in VegDRI rather than multiple intervals because there is some temporal overlap in the precipitation observations used in the different SPI calculations (for example, 4 weeks of the same precipitation data would be used for the 4- and 8-week SPI), which would result in a high degree of intercorrelation among the SPI data values calculated for a given date. Station-based SPI data were calculated for 14 time intervals ranging from 1 to 52 weeks, and each SPI was tested in separately in the seasonal VegDRI models to determine the specific SPI interval that provided the best predictive accuracy for each phase. Table 3 presents the results from this testing. A 52-week SPI was selected for the spring and summer models and a 40-week SPI for the fall model. 

**24** 

|Reference(s)|Edwards and McKee, 1997|Palmer, 1965; Wells et al.,|BR<br>2004|OW|N ET|AL.<br>Vogelmann et al., 2000|USDA, 1994|USDA, 1999|Omernik, 1987|
|---|---|---|---|---|---|---|---|---|---|
|ormat|at sites), 1 km<br>urface|at sites)||ter|ter|ter|ter|ter|ter|
|F|II (<br>er s|II (||ras|ras|ras|ras|ras|ras|
|ce|DSS<br>ASC<br>rast|DSS<br>ASC||DVI<br>1 km|DVI<br>1 km|and Cover<br><br>1 km|1 km|SS<br>1 km|gions<br>1 km|
|our|A|A||N|N|l L<br>ase|GO|NA|ore|
|S|/N|/N||R|R|na<br>b|S||c|
||ACIS|ACIS||AVHR|AVHR|Natio<br>Data|STAT|USDA|EPA E|
|Acronym|SPI|PDSI||PASG|SOSA|NLCD|AWC|IrrAg|ECO|
|ype|ate|ate||lite|lite|hysical|hysical|hysical|hysical|
|T|m|m||el|el|p|p|p|p|
||ation Index<br>Cli|rity Index (Self-<br>Cli||easonal Greenness<br>Sat|aly<br>Sat|Bio|Capacity<br>Bio|Bio|Bio|
||ipit|eve||e S|nom||ter|ure|s|
||rec|t S||rag|A||Wa|ult|ion|
|me|d P|ugh|)|Ave|son||ble|gric|Reg|
|na|dize|Dro|ted|of|Sea|ver|ila|A|cal|
|et|r|r|ra|t|f|Co|va|ed|i|
|Data s|Standa|Palme|calib|Percen|Start o|Land|Soil A|Irrigat|Ecolog|



**25** 

VEGETATION DROUGHT RESPONSE INDEX 

**Table 2.** Three seasonal modeling phases for VegDRI 

|Phase|Start date|End date|Phenological stage|
|---|---|---|---|
|Spring|39561|39615|Emergence, early growth|
|Summer|39616|39685|Maturity, peak growth|
|Fall|39686|39727|Senescence, harvest|



**Table 3.** Results (correlation coefficients) of the SPI Testing for the Three Seasonal VegDRI Models 

||Correlation coefficient|<br>Correlation coefficient<br>|Correlation coefficient|
|---|---|---|---|
|SPI used in the model|for Phase 1|for Phase 2|for Phase 3|
|1-week SPI|0.45|0.54|0.5|
|2-week SPI|0.47|0.56|0.51|
|4-week SPI|0.57|0.65|0.61|
|8-week SPI|0.64|0.74|0.72|
|12-week SPI|0.67|0.79|0.79|
|16-week SPI|0.7|0.82|0.81|
|20-week SPI|0.71|0.83|0.84|
|24-week SPI|0.72|0.84|0.86|
|28-week SPI|0.74|0.84|0.87|
|32-week SPI|0.76|0.85|0.88|
|36-week SPI|0.78|0.85|0.88|
|40-week SPI|0.79|0.85|0.89|
|44-week SPI|0.8|0.86|0.88|
|48-week SPI|0.81|0.86|0.88|
|52-week SPI|0.81|0.87|0.88|



**Self-Calibrated PDSI Data.** The PDSI indicates how the soil moisture compares with normal conditions and is calculated based on parameters including precipitation, temperature, and soil moisture conditions. This index provides a measure of the longterm intensity and duration of drought conditions derived from the precipitation and temperature anomalies and their combined effects on soil water availability to plants. In this study, self-calibrated PDSI historical records for each weather station in the study area were calculated across the 17-year period using the new self-calibrated PDSI algorithm developed by Wells et al. (2004). The PDSI data had a value range from –8.0 to +8.0, and served as the dependent variable in the VegDRI models. 

The PDSI was selected as the dependent variable for the VegDRI model for two primary reasons. First, unlike other climate-based drought indices (such as the SPI) that are solely based on precipitation observations, the PDSI accounts for the effect of both precipitation and temperature on drought conditions. Second, the PDSI scale has 

**26** 

BROWN ET AL. 

sufficient resolution to identify multiple levels of drought severity (for example, moderate, severe, and extreme). Lastly, the PDSI is well recognized and, as a result, the PDSI-like drought scale used for VegDRI is familiar to the drought research community. 

#### **Satellite Data Inputs** 

**Time-Series AVHRR NDVI Data.** A 17-year time series (1989–2005) of biweekly, composited 1 km AVHRR NDVI data (Eidenshink, 2006) was used to calculate the two vegetation-related metrics, percent average seasonal greenness (PASG) and start of season anomaly (SOSA) that were included in the VegDRI model. Prior to the calculation of these metrics, a weighted least squares regression technique (Swets et al., 1999) was applied to the NDVI time series to minimize noise and other artifacts (for example, clouds and variable illumination and viewing angles) that are commonly found in the 14-day NDVI composites (Los et al., 1994) and lead to non-vegetation–related changes in the NDVI data over the year. This smoothing technique enabled the non-vegetation related change in the NDVI data to be eliminated while maintaining a NDVI time series that tracks closely with the original NDVI data set and retains the vegetation’s seasonal responses over the 17-year period. 

**Percent of Average Seasonal Greenness (PASG).** PASG provides a measure of how the general vegetation conditions for a specific period during the growing season compare to historical average conditions for that same period over the 17-year AVHRR historical record. In order to calculate the PASG, the median start and end of the growing season (SOST and EOST) had to be determined at the pixel level in order to define the growing season length across which the PASG should be calculated. The median SOST and EOST day of year (DOY) were identified using a delayed or moving-window averaging technique (Reed et al., 1994). The next step was to calculate the seasonal greenness (SG) metric for each bi-weekly period of the growing season for all 17 years in the time series. SG represents the accumulated NDVI above a baseline (that is, latent or background NDVI) across the 14 days within a bi-weekly period. NDVI values (minus the latent NDVI) were integrated across the period on a daily interval based on NDVI values that were linearly interpolated between the observed NDVI in consecutive 14-day composites. Daily NDVI integration began on each pixel’s SOST DOY and an accumulated SG (or NDVI) was calculated at the end of the 14-day compositing period. Daily integration of the NDVI continued for the subsequent bi-weekly periods where the daily NDVI values were summed across the 14-day period and added to the accumulated NDVI from the prior periods for that year, which continued until the median EOST was reached for each pixel as shown in Equation 2: 



**27** 

VEGETATION DROUGHT RESPONSE INDEX 

where _P1, P2, P3, …Pn_ refer to the 14-day periods; _P1_ is the period for the median SOST and _Pn_ is the period for the median EOST. _NDVI_ is the observed value in the AVHRR composited data and _NDVIb_ is the latent (or baseline) NDVI value defined at the SOST for each pixel. For pixels with a median SOST later than the median EOST (for example, fallow cropland planted to winter wheat in the fall), the integration still started at the median SOST but continued past day 365 into the next year. Periodspecific SG values were calculated for each individual year, as well as the average, period-by-period SG over the 17-year record. 

PASG was then calculated by dividing the SG for a bi-weekly period by the historical mean SG for the same time period using Equation 3: 



where SGP _nYn_ refers to the SG for a bi-weekly period (P _n_ ) of a specific year ( _Yn_ ) and xSGP _n_ is the historical average SG ( _x)_ for the same bi-weekly period (P _n_ ). PASG values less than 100 percent occur when the accumulated SG for a period is less than the historical average, with extremely low PASG values indicative of poor vegetation conditions. PASG values greater than 100 percent occur when the accumulated SG is greater than the historical average and reflect vegetation conditions that are better than those typically found at that time. 

**Start of Season Anomaly (SOSA).** The SOSA metric represents the departure in the SOST for a specific year from the average historical SOST for a given pixel. The SOSA was calculated at the pixel level for each year in the time series using Equation 4: 



where SOSAi is the SOSA (in number of days) for year _i_ , SOST _i_ is the start of season DOY for year _I_ , and SOST _med_ is the median start of season DOY from 1989 to 2005. The SOSA was included in the VegDRI model to account for the different timings of emergence of various natural and agricultural vegetation types, as well as land cover change—all of which can influence seasonal vegetation performance (and thus PASG) recorded in the satellite observations. The SOSA allows a key distinction to be made between areas that have a comparable SOST to the historical median data and are experiencing low PASG values due to some form of stress versus areas that experience an unusually late SOST due to non-drought–related environmental factors (for example, cold or wet spring conditions) and/or management practices (for example, planting of a spring vs. summer crop), which would result in low PASG values that are unrelated to drought stress. 

#### **Biophysical Data** 

**National Land Cover Data (NLCD)** . A 1 km land cover map was generated from the U.S. Geological Survey’s (USGS) 30 m National Land Cover Dataset (NLCD) circa 1992 (Vogelmann et al., 2000).<sup>2</sup> The majority land cover class of the 30-m NLCD map contained within each 1 km AVHRR pixel footprint was calculated and assigned to each pixel in a 1 km land cover map. This variable was included in 

**28** 

BROWN ET AL. 

the VegDRI model to reflect the different seasonal NDVI signals and climate-vegetation responses that are exhibited by different land cover types (for example, deciduous vs. evergreen forest). 

Soil Available Water Capacity (AWC). Soil available water capacity (AWC) was extracted from the STATSGO soils database (item AW35S8M from the 1997 version) (USDA, 1994) for each STATSGO soil map unit over the study area and converted to a 1 km raster grid. The AWC variable was included in the VegDRI model because it represents the potential of the soil to hold moisture and make it available to plants, which in turn exerts control over vegetation growth (Churkina et al., 1999) and influences the sensitivity and response of vegetation to drought. 

**Irrigated Agriculture.** A 1 km irrigated agriculture map was derived using 1997 Census of Agriculture data (USDA, 1999) and the 1 km land cover map (the NLCD described above). The percentage of farmland under irrigation for each county in the study area was calculated by dividing the area of irrigated land in a county by the total farmland area reported in the USDA Census data. This percent irrigated value (ranging from 0 to 100 percent) was then assigned to all pixels within the county that were classified as either cropland or hay/pasture in the 1 km land cover map. The areas of the county with non-crop cover types were assigned a constant background value and assumed to contain no irrigation. The representation of irrigation in VegDRI is critical because rainfed vegetation has much greater sensitivity and response to drought than irrigated vegetation. 

**Ecoregions (ECO).** A 1 km ecoregion grid was generated from the Omernik Level III ecoregion data (Omernik, 1987). The study area comprised 21 ecoregions that divide the regional landscape into a series of geographic areas with similar ecosystems and environmental resources, which were identified using both abiotic (for example, climate, geology, hydrology, land use, and physiography) and biotic (for example, vegetation and wildlife) criteria (Omernik, 1995). Many environmental characteristics (for example, growing season length and plant species) exhibit considerable variability across the seven-state study area, which can influence the sensitivity of vegetation to drought. The ECO variable provided a geographic framework to help account for variability across the study area due to basic climatic conditions and the solar energy budget that varies with latitude, elevation, and time of year in the VegDRI models. 

#### **VegDRI Training Database Development** 

A training database of all the aforementioned climate, satellite, and biophysical data was assembled for the 776 weather station locations. The historical SPI and selfcalibrated PDSI data for each station were entered into the database and sequentially ordered. Summarized statistics had to be calculated for each station for all the variables that were in a raster, gridded format. For each variable, information from a 3 × 3 pixel window centered on each station location was considered and the average value from the window was calculated for continuous variables (for example, PASG, SOSA, 

> 2The NLCD 2001 (Homer et al., 2004) will be tested as a biophysical input variable in the planned expansion of the VegDRI models covering the western United States during 2008. 

**29** 

VEGETATION DROUGHT RESPONSE INDEX 

AWC, and percent irrigation) and the dominant (or majority) class for categorical variables (for example, NLCD and ecoregion). The historical time series of PASG data were sequentially ordered for each station in the same manner as the climate data. For the SOSA, a single value was used for each year. The other biophysical variables were considered static and their values remained constant across time in the database. As discussed earlier, the records in the database were also temporally subdivided into three seasonal subdivisions (Table 2) to accommodate the development of seasonal VegDRI models. 

#### **VegDRI Model Derivation** 

A commercial CART algorithm called Cubist (Quinlan, 1993; Rulequest, 2007) was used to analyze the historical data in the training database and generate the three seasonal, rule-based, piecewise linear regression VegDRI models. The rules and instances option available in Cubist were utilized for model development. The Cubist models are composed of an unordered set of rules, with each rule having the syntax, “if _x_ conditions are met then use the associated linear regression model.” The following rule provides an example of the rules generated by the Cubist algorithm for VegDRI: 

Rule 1: if: 52weekSPI <= 1.4 LandCover in {Grassland, Pasture/Hay, Row Crops} AWC <= 5.46 Percent_Irrigation <= 6 then: VegDRI = –4.9 + 1.48 (52weekSPI) + 3.2 (Percent_Irrigation) – 0.14 AWC. 

If the data associated with a case met the threshold criteria for the three continuous variables (that is, SPI, AWC, and Irrigated Agriculture) and were represented by one of the three land cover classes (that is, grassland, hay/pasture, and row crops) identified by Cubist, then a following multivariate linear regression equation was applied to calculate a VegDRI value. If two or more rules applied to a case, then the individual predictions from each regression equation were averaged to arrive at the final, predicted VegDRI value. In this study, the total number of 31, 26, and 29 rules were generated for the spring, summer, and fall phases, respectively. 

#### **VegDRI Model Implementation** 

The rules from the appropriate seasonal Cubist model were then applied to the gridded image input data (as listed in Table 1) for each bi-weekly period using MapCubist software developed at the USGS Center for Earth Resources Observation and Science (EROS) to produce the series of 1 km VegDRI maps across the 2002 growing season. For the SPI variable, which was acquired as point-based data from weather station locations, a 1 km raster image was generated for each bi-weekly period using an inverse distance weighting (IDW) interpolation method. During the implementation of the model to the image data, the values of all the input variables for each pixel were considered to determine which rule(s) applied and the 

**30** 

BROWN ET AL. 

corresponding linear regression equation(s) associated with the rule(s) was (were) applied to input data values to calculate the VegDRI value for each pixel across the study area. A total of 12 VegDRI maps spanning the May 2 to October 3, 2002 biweekly periods were produced. 

#### **RESULTS AND DISCUSSION** 

Several different methods were used in this study to evaluate the VegDRI results for the 2002 growing season in the central United States and illustrate the utility of this new approach for large-area drought monitoring. A cross-validation technique was used to quantitatively assess the predictive (or estimation) accuracy of the three seasonal VegDRI models. The spatial patterns in the VegDRI maps were then compared to the widely used USDM maps to illustrate the strengths of VegDRI. Lastly, a time-series of VegDRI maps were presented at the county level to demonstrate the local-scale monitoring capabilities of this tool. 

#### **Cross-Validation Using Holdout Method** 

A k-fold cross-validation (by year) approach (Kohavi, 1995) was used to determine the statistical accuracy of the three seasonal VegDRI models. The cross-validation results provide an indicator of the model stability and errors (Rulequest, 2007). By withholding years, the stability of each seasonal model’s predictive accuracy over the 17-year study period could be assessed. For the three seasons, model errors were also accumulated across multiple iterations to yield an average absolute error measure, which was also evaluated for each seasonal model. 

The cross-validation involves an iterative process. In each iteration (or fold), 16 years of data were used to train a seasonal VegDRI model that is subsequently tested on data for a single holdout year to determine its predictive accuracy. A different holdout year was selected as the test data set in each iteration until every year in the 17-year database was withheld for testing. Thus, a 17-fold cross-validation was performed for each seasonal model by replacing the test year at each iteration. 

At each iteration, the correlation coefficient ( _r_ ) and the average and relative errors of the VegDRI model were calculated and the mean (± 1 standard deviation) coefficient and error values across the 17 years were reported for the three seasonal models (Table 4). The average error measure, expressed in PDSI units (that is, the dependent variable) that range from –8.0 to +8.0, represents the average of the individual model error terms calculated for the each iteration or fold in the cross validation process. The relative error measure is the ratio of the average error term to the error magnitude that would result if the mean VegDRI value was always estimated by the model. 

The correlation coefficient values revealed that all three seasonal models had a relatively high predictive accuracy ( _r_ > 0.80). For the individual holdout year results, the _r_ values ranged from 0.79 (spring 1999) to 0.92 (fall 2004). The average and relative errors of the models were also relatively low for all three seasonal phases, ranging from 0.63 to 0.83 and 0.32 to 0.52, respectively. The VegDRI performance was relatively stable across the 17-year study period, with extremely low variability in the _r_ values (1 _r_ < 0.03) and both error measures (1 _r_ < 0.03). This stable multi-year 

**31** 

VEGETATION DROUGHT RESPONSE INDEX 

**Table 4.** Summary of k-fold Cross-validation Results for Three-Phase VegDRI Models Using Holdout Year for Testing<sup>a</sup> 

||Evaluation o<br>|n test data, mean ± sta<br>|ndard deviation<br>|
|---|---|---|---|
||Average |error| ±|Relative |error| ±|Correlation coefficient ±|
|Season|1 STD|1 STD|1 STD|
|Phase 1 (spring)|0.83 ± 0.05|0.49 ± 0.03|0.81 ± 0.02|
|Phase 2 (summer)|0.70 ± 0.01|0.40 ± 0.01|0.86 ± 0.01|
|Phase 3 (fall)|0.63 ± 0.05|0.36 ± 0.03|0.88 ± 0.01|



aThe table shows the mean of the average error, relative error, and correlation coefficient (± 1 standard deviation) for the three seasonal VegDRI models. 

response of VegDRI indicates that this index was relatively uninfluenced by interannual climate variability. However, subtle seasonal differences were found among the models, with the VegDRI consistently having higher _r_ values and lower average and relative errors during the summer and fall phases of the growing season. The slightly lower predictive accuracy of the spring VegDRI model may be influenced by the highly variable NDVI response that vegetation can exhibit in the early growing season from year to year as a result of the limited amount of green vegetation (for example, low NDVI values) that can be remotely sensed by satellite. A subtle change in vegetation conditions early in the year when there is low green biomass can result in greater fluctuations in the low NDVI values as compared to later in the growing season when slight changes in vegetation with higher biomass result in less change in the NDVI value between years. As a result, the VegDRI model results for the spring phase have more uncertainty compared to the other seasonal phases. 

#### **Regional Monitoring Capabilities: A Comparison of VegDRI and USDM for the 2002 Drought** 

A regional-scale comparison of the VegDRI and USDM maps for late July 2002 is provided to illustrate the large-area monitoring capabilities of VegDRI relative to the widely used USDM. The summer of 2002 was an ideal case study because belowaverage precipitation and abnormally high temperatures during the spring and summer months (April through August) resulted in pronounced drought conditions across much of the country (NCDC, 2003). By late July, more than 50 percent of the United States was experiencing “moderate” to “extreme” drought conditions (NCDC, 2003) and the geographic extent was significant, with all 50 states exhibiting some type of dryness (as shown in the USDM map; http://drought.unl.edu/dm/archive/2002/ drmon0723.htm). Drought conditions across the seven-state study area were particularly extreme, with several states (Colorado, Nebraska, and Wyoming) receiving total precipitation amounts in 2002 that ranked among the seven driest on record, dating back to 1895 (NCDC, 2003; USDA, 2003). 

**32** 

BROWN ET AL. 



**Fig. 2.** The VegDRI map (A) for July 25, 2002 and the USDM map (B) for July 23, 2002 over the seven-state study area. The Roman numerals (i.e., I, II, III, and IV) highlight areas for which local differences between VegDRI and USDM maps were further examined and discussed in the study. 

Figure 2 shows the VegDRI (A) and USDM (B) maps over the study area for July 25 and July 23, respectively. A visual examination of Figures 2A and 2B shows that the general spatial patterns and intensity of drought depicted in the two maps were 

**33** 

VEGETATION DROUGHT RESPONSE INDEX 

similar. This was particularly true over the most seriously affected drought areas across the states of Colorado and Wyoming, as well as the western parts of Kansas, Nebraska, and South Dakota and central and southeastern Montana. However, the improved 1 km spatial resolution of VegDRI is readily apparent, showing considerably higher detail at a local scale than in the USDM. The VegDRI map characterizes detailed drought patterns within individual counties, whereas the USDM portrays much broader scale patterns with multiple counties and often large portions of a state(s) assigned to the same drought category. Several local-scale differences in the drought patterns characterized in the VegDRI and USDM maps in Figure 2 illustrate the strengths of the 1-km VegDRI as a drought monitoring tool and also highlight some of the inherent differences between these two indicators. 

The first example occurs in north-central Montana (indicated by Roman numeral I in Fig. 2A). The VegDRI map shows generally normal conditions across this area while the USDM map has classified moderate, severe, and extreme conditions for the same location. This pronounced difference reflects the different nature of these two map products and provides an example of an instance when the patterns between the maps would not be expected to be the same. As discussed earlier, the USDM map is produced from a subjective assimilation of meteorological, hydrological, and numerous other indicators to determine the level of overall drought conditions across a region (Svoboda et al., 2002). As a result, the USDM reflects both agricultural and hydrological drought events. In contrast, the VegDRI represents a single aspect of drought stress on vegetation (that is, agricultural). In north-central Montana, the USDM classified this area in hydrological drought (indicated by the “W” label in Fig. 2B) but not experiencing agricultural drought, which would be consistent with the preponderance of normal vegetation condition shown on the VegDRI map. This difference can be attributed to a major early June storm that provided 2–6 inches of precipitation over this area, which allowed vegetation conditions to recover to normal conditions but did not ease the longer-term hydrological drought impacts that were occurring (LeComte, 2002). 

Western South Dakota and North Dakota represent a second example of interest, where the VegDRI map (indicated by the Roman numeral II in Fig. 2A) depicted more extreme drought stress on vegetation than in the USDM map (Fig. 2B). The spatial drought depictions in the VegDRI map for July 25 looked very similar to the patterns in the late July PDSI maps (NCDC, 2002), which suggests that drought patterns for these two areas were underemphasized in the USDM map. In addition, many specific drought impacts were being reported in western South Dakota, confirming the severe to extreme drought in that part of the state (Miller, 2002a, 2002b, 2002c, 2002d; Velder, 2002). These omissions and/or underestimates of drought in the USDM map were likely due to a lack of ground truth information for these areas in the USDM map development process. The creation of the USDM map depends on input from local and regional experts (for example, state climatologists), who describe dryness conditions and specific impacts for their areas. In 2002, expert feedback was not available for South and North Dakota (Svoboda, pers. commun.), which resulted in the USDM map under-representing the severity of drought for these locations. The drought depictions on the USDM map eventually evolved over the latter part of 2002 to represent the drought (D3, extreme drought) over western South Dakota and show some dryness over northern North Dakota (D0, abnormally dry) by 

**34** 

BROWN ET AL. 

January 2003 (as shown in the USDM for January 7, 2003; http://drought.unl.edu/dm/ archive/2003/drmon0107.htm). This example illustrates the valuable, objective information that VegDRI can provide, not only to decision makers, but also to USDM authors who can utilize the VegDRI as an additional indicator in the development of their maps. 

Another area that warrants examination is the western panhandle of Nebraska (indicated by the Roman numeral III in Fig. 2A), where the VegDRI tool indicates that drought impact on vegetation is more extreme than the conditions represented in the USDM. This is particularly true for the area stretching from northwest to northcentral Nebraska and appears to be an extension of the underestimation of drought conditions in the USDM map that was observed for western South Dakota. A prime example of VegDRI’s local-scale monitoring capabilities is also seen in southwest Nebraska, where the VegDRI map shows normal conditions over a two- to threecounty area while the USDM map has depicted extreme drought (D3). This area experienced heavy rainfall and a flash flood event (on July 6, 2002) (Nebraska Department of Roads, 2002) several weeks before the late July dates of the two maps; this allowed the vegetation conditions to recover from the early summer drought stress. This was reflected in the VegDRI map on July 25. This event was too localized for the USDM and could not be resolved at the map’s coarse, climate-division spatial resolution. This specific example shows how the VegDRI would be valuable for local-scale applications and interests and can provide complimentary information to the USDM maps. 

#### **Local-Scale VegDRI Results: An Example from Perkins County, South Dakota** 

A case study for Perkins County, South Dakota is also presented to further illustrate the improved spatial resolution and more localized drought monitoring capabilities that are provided by VegDRI. Although this example is limited to a specific county, the drought conditions and patterns characterized by VegDRI for this area were fairly representative of those depicted across the larger seven-state study area in 2002 and demonstrate the potential of this new tool to acquire county to sub-county drought information. Perkins County has an agriculturally based economy with a landscape dominated by a mosaic of grassland and cropland. In 2002, the county experienced severe to extreme drought conditions that resulted in significant agricultural losses. This was reflected by the county’s considerably lower wheat yields in 2002 (Fig. 3) (USDA, 2002) and the large percentage of crops that remained unharvested after the 2002 growing season due to drought-induced crop failures. USDA (2002) reported that less than 20 percent of the county’s three major crops (wheat, sorghum, and corn) were harvested in 2002. 

The development and intensification of drought conditions for the Perkins County area was also reflected in the large number of drought impacts (31 total) reported in the National Drought Mitigation Center’s (NDMC) Drought Impact Reporter (http://droughtreporter.unl.edu/, last accessed on August 28, 2007) from April 1 to October 30, 2002, for South Dakota. In addition, many drought impacts for western/northwestern South Dakota (for example, county drought disaster declarations, increased cattle sales, businesses closings and food drives in local communities, and the release of Conservation and Reserve Program lands for emergency grazing) 

**35** 

VEGETATION DROUGHT RESPONSE INDEX 



**36** 

BROWN ET AL. 



**Fig. 4.** Reported county wheat yields for Perkins County, South Dakota from 1989 through 2006 (USDA, 2002). In 2002, the extreme drought conditions led to substantial declines in yield compared to other years in this 18-year period. 

were documented in state and federal agency reports and by the media in the region (Miller, 2002a, 2002b, 2002c; Velder, 2002). 

The spatial patterns and temporal behavior of the time series of VegDRI maps for Perkins County and the surrounding area (Fig. 4) show the expansion and intensification of drought conditions in 2002. On May 16, the majority of Perkins County had normal conditions according to the VegDRI, with some grassland primarily in the southern part of the county showing moderate drought conditions. By June 13, a moderate drought signal had expanded across most of the county’s grassland and some cropland, with isolated areas of severe drought. Drought conditions continued to expand and intensify by July 11 and by the late-summer August 8 and September 5 dates, the majority of Perkins County was classified as experiencing severe to extreme drought in the VegDRI maps. The trend and relative changes in drought conditions depicted by VegDRI across the growing season had strong agreement with the observed drought conditions for weather stations located within or near Perkins County, as shown in Figure 5. The behavior of the VegDRI for the county’s two dominant land cover types—grassland (64 percent of county area) and cropland (27 percent of county area)—track well with the PDSI values calculated for the three local weather stations. From early May to mid July, the average VegDRI response for both cover types and the PDSI values for the three stations showed a gradual downtrend as the severity of the drought conditions across Perkins County intensified. By late July, the station-based PDSI values reached their minimum, ranging from approximately –2.0 (moderate to severe drought) at Bison to –4.0 (severe to extreme drought) at Glad Valley. The average VegDRI response from both cover types continued to gradually decline until reaching minimum VegDRI values of approximately 

**37** 

VEGETATION DROUGHT RESPONSE INDEX 



**Fig. 5.** Average VegDRI response calculated for grassland and small grains within Perkins County, South Dakota for 14-day periods in 2002 and the self-calibrated PSDI calculated at three weather stations located within and near the county. The time-series responses of VegDRI for both land cover types and the PDSI for all three stations are similar and reflect the intensification of drought conditions across the 2002 growing season. 

–4.0 (extreme drought). This increasing severity of drought conditions can be seen in the series of VegDRI maps from July 11 to September 5, when the total area with severe to extreme drought conditions substantially increased. Also, the VegDRI maps on August 8 and September 5 reflect the more severe drought conditions at Glad Valley (compared to Bison) that were shown in the observed PDSI values for both station locations. These results indicate that the VegDRI monitored similar drought conditions to those observed at weather station locations over this small case study area and depicted sub-county–level spatial variations in drought conditions. 

The improved geospatial drought information provided in the VegDRI maps could be used by agricultural producers, policy makers, and other stakeholders to make more informed decisions at the county to sub-county levels. Examples include sub-county drought declarations for financial assistance and emergency grazing of CRP lands, the identification of locations with poor and/or good rangeland and hay conditions for livestock grazing and feed purchases, and triggers for drought response mitigation and response activities. 

#### **CONCLUSIONS AND FUTURE RESEARCH DIRECTIONS** 

The VegDRI represents a new large-area drought monitoring approach that integrates climate data, satellite-based observations of vegetation, and other biophysical 

**38** 

BROWN ET AL. 

characteristics of the environment. The 1 km spatial resolution of the satellite observations enables monitoring drought events at a finer spatial scale than with traditional climate-based drought indicators. Climate data, when used in combinations with these observations, allows drought-affected areas of stressed vegetation to be discerned from stressed areas resulting from other environmental factors. This cannot be achieved by the traditional remote sensing-based approaches that rely solely on satellite VI information. 

The aim of VegDRI was to address the need for a tool that could map and monitor spatially detailed drought patterns across large geographic areas and provide localscale drought information required for more effective planning, mitigation, and response activities. The results from this study demonstrate that more spatially detailed drought patterns can be characterized and monitored in the 1 km VegDRI maps, compared to the commonly used USDM map. This provides more localized drought information, which is currently at a county to sub-county scale. In addition, VegDRI represents an objective and repeatable approach to drought monitoring that can be implemented in a near real-time fashion and geographically expanded to provide coverage across the United States. 

The intent of this pilot study was to present this new drought monitoring methodology and demonstrate the VegDRI’s capabilities over a limited seven-state region for a single drought year. This research should be viewed as an initial step in the evaluation and development of VegDRI. A limited number of qualitative and quantitative assessments of VegDRI were presented in this paper, which constitutes a stage 1 validation (as defined by Morisette et al., 2006) of this index where the accuracy of the results have been estimated from a limited number of observations from selected locations and times. A validation of VegDRI, like many other large-area drought and land cover monitoring products, is challenging because of the extensive ground truth data that is required to adequate assess the index’s performance across both space and time. A complete validation of VegDRI will require multi-year observations of vegetation characteristics (for example, green biomass, LAI, and turgidity) collected across the growing season for a considerable number of sample locations. Currently, few data sets with these characteristics exist, and most of them have only been collected over a limited number of sites and years. 

Plans are under way to perform a more comprehensive validation of the VegDRI using multiple sources of the “best available” information in an effort to better understand the accuracy and performance of this index for drought monitoring. A comprehensive spatial cross-validation of VegDRI is planned by partitioning the model training data in space for model calibration and testing. County-level USDA crop yield information will be compared with the VegDRI response over cropland for multiple years to determine if change in VegDRI is consistent with inter-annual crop production fluctuations. Multi-year, multi-seasonal clip plot data for several biophysical vegetation characteristics (for example, green LAI and biomass) will be also be compared to intra- and interannual VegDRI trends to determine the strength of their relationship. Time-series soil moisture observations from Mesonets will also be evaluated in relation to the VegDRI’s multi-temporal response. In addition, a network of scientific experts (for example, state climatologists, rangeland scientists, and USDM authors), policy makers, and agricultural producers has been established to provide periodic feedback on the accuracy of the VegDRI for their local area. Collectively, 

**39** 

VEGETATION DROUGHT RESPONSE INDEX 

this diverse set of information will be used to determine the accuracy of VegDRI and characterize the index’s strengths and weaknesses. This “convergence of evidence” evaluation approach will provide a more objective, quantifiable assessment approach for VegDRI until data sets become available for stage 2 and 3 validation (as defined by Morisette et al., 2006), which will require a standard set of measurements that can be collected over a widely distributed set of locations and time periods. 

Further research and development of the VegDRI is also being undertaken. The area of coverage for VegDRI is currently being expanded beyond the initial sevenstate study region and will cover the conterminous United States in several years. In addition, a process to produce near real-time VegDRI maps has been established to provide operational and timely information to users. New variables such as elevation and evapotranspiration will also be tested in VegDRI models. Alternative data mining algorithms and ensemble techniques are also being evaluated. Lastly, comparable time-series VI data sets from other current and future satellite-based sensors—such as the Moderate Resolution Imaging Spectroradiometer (MODIS), Medium Resolution Imaging Spectrometer (MERIS), and the planned Visible/Infrared Imager/Radiometer Suite (VIIRS)—will also be investigated to ensure the temporal continuity of operational VegDRI production in the future. 

#### **ACKNOWLEDGMENTS** 

The research performed by Jesslyn Brown was carried out under USGS contract 03CRCN0001. Support was also provided by the U.S. Department of Agriculture’s Federal Crop Insurance Corporation (FCIC) through the Risk Management Agency (RMA) under USDA partnership (02-IE-0831-0208) with the National Drought Mitigation Center, University of Nebraska-Lincoln, and the U.S. Geological Survey (USGS). The climate data used in this study were acquired from the High Plains Regional Climate Center (HPRCC) and the Department of Computer Science and Engineering’s National Agricultural Decision Support System (NADSS) at the University of Nebraska-Lincoln. The authors also wish to thank A. Haacke for her administrative support, D. Wood for her editorial suggestions, and the reviewers of the manuscript for their helpful suggestions. 

#### **REFERENCES** 

- Asner, G. P., Townsend, A. R., and B. H. Braswell, 2000, “Satellite Observation of El Niño Effects on Amazon Forest Phenology and Productivity,” _Geophysical Research Letters_ , 27(7):981–984. 

- Asrar, G., Myneni, R. B., and E. T. Kanemasu, 1989, “Estimation of Plant Canopy Attributes from Spectral Reflectance Measurements,” in _Theory and Applications of Optical Remote Sensing_ , Asrar, G. (Ed.), New York, NY: Wiley, 252–296. 

- Baret, F. and G. Guyot, 1991, “Potentials and Limits to Vegetation Indices for LAI and APAR Assessments,” _Remote Sensing of Environment_ , 35:161–173. 

- Bell, J. F., 1999, “Tree-Based Methods. The Use of Classification Trees to Predict Species Distributions,” in _Machine Learning Methods for Ecological Applications,_ Fielding, A. (Ed.), Norwell, MA: Kluwer Academic Publishers, 89–105. 

**40** 

BROWN ET AL. 

- Breshears, D. D., Cobb, N. S., Rich, P. M., Price, K. P., Allen, C. D., Balice, R. G., Romme, W. H., Kastens, J. H., Floyd, M. L., Belnap, J., Anderson, J. J., Myers, O. B., and C. W. Meyer, 2005, “Regional Vegetation Die-off in Response to Global-change-type Drought,” _Proceedings of the National Academy of Sciences of the United States of America_ , 102(42):5144–5148. 

- Churkina, G., Running, S. W., Schloss, A. L., and the participants of the Potsdam NPP model intercomparison, 1999, “Comparing Global Models of Terrestrial Net Primary Productivity (NPP): The Importance of Water Availability,” _Global Change Biology_ , 5(Suppl. 1):46–55. 

- Cutter, S. L. and C. Emrich, 2005, “Are Natural Hazards and Disaster Losses in the U.S. Increasing?,” _EOS,_ ( _Transactions of the American Geophysical Union_ ), 86(41):388–389. 

- De’ath, G. and K. E. Fabricius, 2000, “Classification and Regression Trees—a Powerful yet Simple Technique for Ecological Data Analysis,” _Ecology_ , 81(11):3178– 3192. 

- DeBeurs, K. M. and G. M. Henebry, 2004, “Land Surface Phenology, Climatic Variation, and Institutional Change: Analyzing Agricultural Land Cover Change in Kazakhstan,” _Remote Sensing of Environment_ , 89(4):497–509. 

- DeFries, R. S., Hansen, M. C., Townshend, J. R. G., and R. S. Sohlberg, 1998, “Global Land Cover Classifications at 8 km Spatial Resolution: The Use of Training Data Derived from Landsat Imagery in Decision Tree Classifiers,” _International Journal of Remote Sensing_ , 19:3141–3168. 

- DeFries, R. S. and J. R. G. Townshend, 1994, “NDVI-Derived Land Cover Classifications at a Global Scale,” _International Journal of Remote Sensing_ , 15:3567– 3586. 

- Di, L., Rundquist, D. C., and L. Han, 1994, “Modeling Relationships between NDVI and Precipitation during Vegetative Growth Cycle,” _International Journal of Remote Sensing_ , 15(10):2121–2136. 

- Domenikiotis, C., Loukas, A., and N. R. Dalezios, 2003, “The Use of NOAA/ AVHRR Satellite Data for Monitoring and Assessment of Forest Fires and Floods,” _Natural Hazards and Earth System Science,_ 3(1-2):115–128. 

- Edwards, D. C. and T. B. McKee, 1997, _Characteristics of 20th Century Drought in the United States at Multiple Time Scales_ , Ft. Collins, CO: Colorado State University, Climatology Report Number 97-2. 

- Eidenshink , J. C., 2006, “A 16-year Time Series of 1 km AVHRR Satellite Data of the Conterminous United States and Alaska,” _Photogrammetric Engineering & Remote Sensing_ , 72:1027–1035. 

- FEMA (Federal Emergency Management Agency), 1995, _National Mitigation Strategy—Partnerships for Building Safer Communities_ , Washington, DC: FEMA, 26 pp. 

- Franke, J. and G. Menz, 2007, “Multi-temporal Wheat Disease Detection by Multispectral Remote Sensing,” _Precision Agriculture_ , 8(3):161–172. 

- Goetz, S. J., Fiske, G. J., and A. G. Bunn, 2006, “Using Satellite Time-series Data Sets to Analyze Fire Disturbance and Forest Recovery across Canada,” _Remote Sensing of Environment_ , 101:352–365. 

- Goetz, S. J. and S. D. Prince, 1996, “Remote Sensing of Net Primary Production in Boreal Forest Stand,” _Agricultural and Forest Meteorology_ , 78:149–179. 

**41** 

VEGETATION DROUGHT RESPONSE INDEX 

- Gonzalez-Alonso, F., Merino-De-Miguel, S., Roldan-Zamarron, A., Garcia-Gigorro, S., and J. M. Cuevas, 2006, “Forest Biomass Estimation through NDVI Composites. The Role of Remotely Sensed Data to Assess Spanish Forests as Carbon Sinks,” _International Journal of Remote Sensing_ , 27(24):5409–5415. 

- Goward, S. N., Tucker, C. J., and D. G. Dye, 1985, “North American Vegetation Patterns Observed with the NOAA-7 Advanced Very High Resolution Radiometer,” _Vegetatio_ , 64:3–14. 

- Guttman, N. B., Wallis, J. R., and J. R. M. Hosking, 1992, “Spatial Comparability of the Palmer Drought Severity Index,” _Water Resources Bulletin_ , 28:1111–1119. 

- Hansen, M. C., DeFries, R. S., Townshend, J. R. G., and R. Sohlberg, 2000, “Global Land Cover Classification at 1 km Spatial Resolution Using a Classification Tree Approach,” _International Journal of Remote Sensing_ , 21(6-7):1331–1364. 

- Harms, S. K., Deogun, J., and T. Tadesse, 2002, “Discovering Sequential Rules with Constraints and Time Lags in Multiple Sequences,” in _Proceedings of the 2002 National Conference on Digital Government Research_ , Los Angeles, California, USA, May 2002, 235–241. 

- Hayes, M. J., 2003, “Drought Indices,” National Drought Mitigation Center, University of Nebraska-Lincoln [http://www.drought.unl.edu/whatis/indices.htm#spi], accessed September 9, 2007. 

- Hayes, M. J. and W. L. Decker, 1996, “Using NOAA AVHRR Data to Estimate Maize Production in the United States Corn Belt,” _International Journal of Remote Sensing_ , 17(16):3189–3200. 

- Hayes, M. J., Wilhite, D. A., Svoboda, M., and O. Vanyarkho, 1999, “Monitoring the 1996 Drought Using Standardized Precipitation Index,” _Bulletin of the American Meteorological Society_ , 80(3):429–438. 

- Henebry, G. M. and I. C. Ratcliffe, 2003, “Occurrence and Persistence of Hailstreaks in the Vegetated Land Surface,” in _Proceedings of the American Meteorological Society Annual Meeting_ , Long Beach, CA, February 2003. 

- Hoff, C., Bachelet, D., Rambal, S., Joffre, R., and B. Lacaze, 1995, “Simulating Leaf Area Index of Mediterranean Evergreen Oak Ecosystems: Comparison with Remotely Sensed Estimation,” in _Proceedings_ , IUFRO Meetings, Montpellier, France, 313–321. 

- Homer, C., Huang, C., Yang, L., Wylie, B., and M. Coan, 2004, “Development of a 2001 National Land-Cover Database for the United States,” _Photogrammetric Engineering and Remote Sensing_ , 70:829–840. 

- Hubbard, K. G., DeGaetano, A. T., and K. D. Robbins, 2004, “SERVICES: A Modern Applied Climate Information System,” _Bulletin of the American Meteorological Society_ , 85(6):811–812. 

- Jakubauskas, M. E., Peterson, D. L., Kastens, J. H., and D. R. Legates, 2002, “Time Series Remote Sensing of Landscape-Vegetation Interactions in the Southern Great Plains,” _Photogrammetric Engineering and Remote Sensing_ , 68:1021– 1030. 

- Ji, L. and A. J. Peters, 2003, “Assessing Vegetation Response to Drought in the Northern Great Plains Using Vegetation and Drought Indices,” _Remote Sensing of Environment_ , 87:85–98. 

**42** 

BROWN ET AL. 

- Keyantash, J. and J. A. Dracup, 2002, “The Quantification of Drought: An Evaluation of Drought Indices,” _Bulletin of the American Meteorological Society_ , 83:1167– 1180. 

- Kidwell, K. B., 1990, _Global Vegetation Index User’s Guide_ , Washington, DC: U.S. Department of Commerce, National Oceanic and Atmospheric Administration. 

- Kogan, F. N., 1990, “Remote Sensing of Weather Impacts on Vegetation in NonHomogeneous Areas,” _International Journal of Remote Sensing_ , 11(8):1405– 1419. 

- Kogan, F. N., 1995, “Droughts of the Late 1980s in the United States as Derived from NOAA Polar-Orbiting Satellite Data,” _Bulletin of the American Meteorological Society_ , 76(5):655–668. 

- Kogan, F. N., 1997, “Global Drought Watch from Space,” _Bulletin of the American Meteorological Society_ , 78(4):621–636. 

- Kohavi, R., 1995, “A Study of Cross-Validation and Bootstrap for Accuracy Estimation and Model Selection,” in _Proceedings of the 14th International Joint Conference on Artificial Intelligence_ , 1137–1143. 

- Lackey, M., Lott, N., Ross, T., Graumann, A., and J. Kobar, 2007, _NOAA’s National Climatic Data Center Products and Services Guide_ , Washington, DC: U.S. Department of Commerce, National Oceanic and Atmospheric Administration., January 2007 [http://www1.ncdc.noaa.gov/pub/data/inventories/COMPLETEGUIDE.pdf], accessed August 17, 2007. 

- LeComte, D. 2002, “National Drought Summary—June 11, 2002,” June 13, 2002 [http://drought.unl.edu/dm/archive/2002/drmon0611.htm], accessed August 1, 2007. 

- Liu, W. T., and F. N. Kogan, 1996, “Monitoring Regional Drought Using the Vegetation Condition Index,” _International Journal of Remote Sensing_ , 17(14):2761– 2782. 

- Los, S. O., Justice, C. O., and C. J. Tucker, 1994, “A Global 1 by 1 NDVI Data Set for Climate Studies Derived from the GIMMS Continental NDVI Data,” _International Journal of Remote Sensing_ , 15(17):3493–3518. 

- Loveland, T. R., Merchant, J. W., Ohlen, D. O., and J. F. Brown, 1991, “Development of a Land Cover Characteristics Data Base for the Conterminous U.S.,” _Photogrammetric Engineering & Remote Sensing_ , 57(11):1453–1463. 

- Loveland, T. R., Merchant, J. W., Reed, B. C., Brown, J. F., Ohlen, D. O., Olson, P., and J. Hutchinson, 1995, “Seasonal Land Cover Regions of the United States,” _Annals of the Association of American Geographers_ , 85:339–355. 

- Loveland, T. R., Reed, B. C., Brown, J. F., Ohlen, D. O., Zhu, Z., Yang, L., and J. W. Merchant, 2000, “Development of a Global Land Cover Characteristics Database and IGBP DISCover from 1 km AVHRR Data,” _International Journal of Remote Sensing_ , 21(6-7):1303–1330. 

- Malingreau, J. P., 1986, “Global Vegetation Dynamics: Satellite Observations Over Asia,” _International Journal of Remote Sensing_ , 7:1121–1146. 

- McKee, T. B., Doesken, N. J., and J. Kleist, 1995, “Drought Monitoring with Multiple Time Scales,” Preprints, _9th Conference on Applied Climatology_ , January 15–20, Dallas, Texas, 233–236. 

**43** 

VEGETATION DROUGHT RESPONSE INDEX 

- McVicar, T. R. and P. N. Bierwirth, 2001, “Rapidly Assessing the 1997 Drought in Papua New Guinea Using Composite AVHRR Imagery,” _International Journal of Remote Sensing_ , 22:2109–2128. 

- Miller, S., 2002a, “Study: Drought Costs Mount,” _Rapid City Journal_ , July 29, 2002 [http://www.rapidcityjournal.com/articles/2002/07/29/news02.prt], accessed August 22, 2007. 

- Miller, S., 2002b, “Drought Disaster Declared,” _Rapid City Journal_ , August 14, 2002 [http://www.rapidcityjournal.com/articles/2002/08/14/news02.prt], accessed August 23, 2007). 

- Miller, S., 2002c, “Drought Impacts Spread to Towns’ Main Streets,” _Rapid City Journal_ , August 26, 2002 [http://www.rapidcityjournal.com/articles/2002/08/26/ news02.prt], accessed August 23, 2007. 

- Miller, S., 2002d, “Drought Putting Crunch on Ranchers, Small-Town Businesses,” _Rapid City Journal_ , November 29, 2002 [http://www.rapidcityjournal.com/ articles/2002/11/29/front/top/news01.prt], accessed August 23, 2007. 

- Morisette, J. T., Baret, F., and S. Liang, 2006, “Special Issue on Global Land Product Validation,” _IEEE Transactions on Geoscience and Remote Sensing_ , 44(7):1695– 1697. 

- Myneni, R. B., Keeling, C. D., Tucker, C. J., Asrar, G., and R. R. Nemani, 1997, “Increased Plant Growth in the Northern High Latitudes from 1981 to 1991,” _Nature_ , 386:695–702. 

- NCDC (National Climatic Data Center), 2002, “Climate of 2002—July, U.S. Regional Drought Watch,” August 15, 2002 [http://www.ncdc.noaa.gov/oa/ climate/research/2002/jul/drought-regional-overview.html#CUS], accessed July 14, 2007. 

- NCDC (National Climatic Data Center), 2003, “Climate of 2002—Annual Review U.S. Drought,” January 23, 2003 [http://www.ncdc.noaa.gov/oa/climate/ research/2002/ann/drought-summary.html], accessed July 13, 2007. 

- NCDC (National Climatic Data Center), 2007, “Billion Dollar U.S. Weather Disasters” [http://lwf.ncdc.noaa.gov/oa/reports/billionz.html], accessed September 22, 2007. 

- Nebraska Department of Roads, 2002, “The Flood” [http://www.nebraskatransportation.org/closure/], accessed September 17, 2007. 

- Omernik, J. M., 1987, “Ecoregions of the Conterminous United States,” _Annals of the Association of American Geographers_ , 77(1):118–125. 

- Omernik, J. M., 1995, “Ecoregions: A Spatial Framework for Environmental Management,” in _Biological Assessment and Criteria: Tools for Water Resource Planning and Decision Making_ , Davis, W. and T. Simon (Eds.), Boca Raton, FL: Lewis Publishers, 49–62. 

- Quinlan, J. R., 1993, _C4.5 Programs for Machine Learning_ , San Mateo, CA: Morgan Kaufmann Publishers. 

- Palmer, W. C., 1965, _Meteorological Drought. Research Paper,_ No. 45, Washington, DC: U.S. Department of Commerce, Weather Bureau, 58 pp. 

- Peters, A. J., Griffin, S. C., Vina, A., and L. Ji, 2000, “Use of Remotely Sensed Data for Assessing Crop Hail Damage,” _Photogrammetric Engineering and Remote Sensing,_ 66(11):1349–1355. 

**44** 

BROWN ET AL. 

- Reed, B. C., Brown, J. F., VanderZee, D., Loveland, T. R., Merchant, J. W., and D. O. Ohlen, 1994, “Measuring Phenological Variability from Satellite Imagery,” _Journal of Vegetation Science_ , 5:703–714. 

- Reed, B. C., Loveland, T. R., and L. L. Tieszen, 1996, “An Approach for Using AVHRR Data to Monitor U.S. Great Plains Grasslands,” _Geocarto International_ , 11(3):13–22. 

- Rosenberg, N. J. (Ed.), 1978, _North American Droughts_ , Boulder, CO, Westview Press, 177 pp. 

- Ross, T., and N. Lott, 2003, _A Climatology of 1980–2003 Extreme Weather and Climate Events_ , Washington, DC: U.S. Department of Commerce, NOAA/NESDIS, National Climatic Data Center (NCDC), Technical Report 2003-01, 14 pp. 

- Rouse, J. W., Haas, R. H., Schell, J. A., Deering, D. W., and J. C. Harlan, 1974, _Monitoring the Vernal Advancement and Retrogradation (Greenwave Effect) of Natural Vegetation_ , Greenbelt, MD: NASA/GSFC Type II Final Report, 371 pp. 

- Rulequest, 2007, “An Overview of Cubist” [http://www.rulequest.com/cubistwin.html], accessed May 23, 2007. 

- Rundquist, B. C. and J. A. Harrington, Jr., 2000, “The Effects of Climatic Factors on Vegetation Dynamics of Tallgrass and Shortgrass Cover,” _GeoCarto International_ , 15(3):31–36. 

- Sannier, C. A. D., Taylor, J. C., and W. Du Plessis, 2002, “Real-Time Monitoring of Vegetation Biomass with NOAA-AVHRR in Etosha National Park, Namibia, for Fire Risk Assessment,” _International Journal of Remote Sensing_ . 23(1):71–89. 

- Schwartz, M. D., 1992, “Phenology and Springtime Surface Layer Change,” _Monthly Weather Review_ , 120:2570–2578. 

- Swets, D. L., Reed, B. C., Rowland, J. R., and S. E. Marko, 1999, “A Weighted LeastSquares Approach to Temporal Smoothing of NDVI,” in _Proceedings of the 1999 ASPRS Annual Conference, from Image to Information_ , Portland, Oregon, May 17–21, 1999 (CD-ROM, 1 disc). 

- Svoboda, M., LeComte, D., Hayes, M., Heim, R., Gleason, K., Angel, J., Rippey, B., Tinker, R., Palecki, M., Stooksbury, D., Miskus, D., and S. Stephens, 2002, “The Drought Monitor,” _Bulletin of the American Meteorological Society_ , 83(8):1181– 1190. 

- Tadesse, T., Brown, J. F., and M. J. Hayes, 2005, “A New Approach for Predicting Drought-Related Vegetation Stress: Integrating Satellite, Climate, and Biophysical Data Over the U.S. Central Plains,” _ISPRS Journal of Photogrammetry and Remote Sensing_ , 59(4):244–253. 

- Townshend, J. R. G., Justice, C. O., and V. Kalb, 1987, “Characterization and Classification of South American Land Cover Types Using Satellite Data,” _International Journal of Remote Sensing_ , 8:1189–1207. 

- Tucker, C. J., 1979, “Red and Photographic Infrared Linear Combinations for Monitoring Vegetation,” _Remote Sensing of Environment_ , 8:127–150. 

- Tucker, C. J., Townshend, J. R. G., and T. E. Goff, 1985, “African Land Cover Classification Using Satellite Data,” _Science_ , 9227(4685):369–375. 

- Two Crows Corporation, 1999, _Introduction to Data Mining and Knowledge Discovery_ , 3rd ed., Potomac, MD: Two Crows Corporation. 

**45** 

VEGETATION DROUGHT RESPONSE INDEX 

- Unganai, L. S. and F. N. Kogan, 1998, “Drought Monitoring and Corn Yield Estimation in Southern Africa from AVHRR Data,” _Remote Sensing of the Environment_ , 63:219–232. 

- USDA (U.S. Department of Agriculture), Natural Resource Conservation Service, 1994, _State Soil Geographic (STATSGO) Data Base: Data Use Information_ , Washington, DC: U.S. Soil Conservation Service, Miscellaneous Publication Number 1492, 113 pp. 

- USDA (U.S. Department of Agriculture), 1999, _1997 Census of Agriculture_ , Washington, DC: National Agricultural Statistics Service, Geographic Area Series 1A and 1B (CD-ROM). 

- USDA (U.S. Department of Agriculture), 2002, “USDA National Agricultural Statistics Service (NASS)—Quick Stats” [http://www.nass.usda.gov/QuickStats/ Create_County_All.jsp], accessed September 25, 2007. 

- USDA (U.S. Department of Agriculture), 2003, “Weekly Weather and Crop Bulletin, January 14, 2003,” [http://usda.mannlib.cornell.edu/usda/waob/weather_weekly/ /2000s/2003/weather_weekly-01-14-2003.pdf], accessed September 20, 2007. 

- Velder, T., 2002, “Food Drive Helps Ag Families,” _Rapid City Journal_ , September 22, 2002 [http://www.rapidcityjournal.com/articles/2002/09/22/news01.prt], accessed August 23, 2007. 

- Vogelmann, J. E., Howard, S. M., Yang, L., Larson, C. R., Wylie, B. K., and N. Van Driel, 2000, “Completion of the 1990s National Land Cover Dataset for the Coterminous United States from Landsat Thematic Mapper Data and Ancillary Data Sources,” _Photogrammetric Engineering & Remote Sensing_ , 67(6):650– 661. 

- Wang, Q., Adiku, S., Tenhunen, J., and A. Granier, 2005, “On the Relationship of NDVI with Leaf Area Index in a Deciduous Forest Site,” _Remote Sensing of Environment_ , 94(2):244–255. 

- Wang, Q., Watanabe, M., Hayashi, S., and S. Murakami, 2003, “Using NOAA AVHRR Data to Assess Flood Damage in China,” _Environmental Monitoring and Assessment_ , 82(2):119–148. 

- Wells, N., Goddard, S., and M. J. Hayes, 2004, “A Self-Calibrating Palmer Drought Severity Index,” _Journal of Climate_ , 17(12):2335–2351. 

- Wessels, K. J., Prince, S. D., Zambatis, N., MacFadyen, S., Frost, P. E., and D. Van Zyl, 2006, “Relationship between Herbaceous Biomass and 1-km<sup>2</sup> Advanced Very High Resolution Radiometer (AVHRR) NDVI in Kruger National Park, South Africa,” _International Journal of Remote Sensing,_ 27(5):951–973. 

- WGA (Western Governors’ Association), 2004, “Creating a Drought Early Warning System for the 21st Century: The National Integrated Drought Information System,” Western Governors’ Association, Denver, CO. 13 pp. [http:// www.westgov.org/wga/publicat/nidis.pdf], accessed August 20, 2007. 

- Wilhite, D. A., 1997, “Responding to Drought: Common Threads from the Past, Visions for the Future,” _Journal of the American Water Resources Association_ 33(5):951–959. 

- Wilhite, D. A., 2000, “Preparing for Drought: A Methodology,” in _Drought: A Global Assessment_ , Wilhite, D. A. (Ed.), London, UK: Routledge, Natural Hazards and Disaster Series, 2:89–104. 

**46** 

BROWN ET AL. 

- Wylie, B. K., Fosnight, E. A., Gilmanov, T. G., Frank, A. B., Morgan, J. A., Haferkamp, M. R., and T. P. Meyers, 2007, “Adaptive Data-Driven Models for Estimating Carbon Fluxes in the Northern Great Plains,” _Remote Sensing of Environment_ , 106:399–413. 

- Yang, L., Wylie, B. K., Tieszen, L. L., and B. C. Reed, 1998, “An Analysis of Relationships among Climate Forcing and Time-Integrated NDVI of Grasslands over the U.S. Northern and Central Great Plains,” _Remote Sensing of the Environment_ , 65:25–37. 

- Zhang, Y., Grant, R. F., Flanagan, L. B., Wang, S., and D. L. Verseghy, 2005, “Modeling CO2 and Energy Exchanges in a Northern Semiarid Grassland Using the Carbon and Nitrogen-Coupled Canadian Land Surface Scheme (C-Class),” _Ecological Modeling_ , 181:591–614. 

