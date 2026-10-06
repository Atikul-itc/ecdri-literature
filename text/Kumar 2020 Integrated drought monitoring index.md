



Available online at www.sciencedirect.com 

## ScienceDirect 

Advances in Space Research 67 (2021) 298–315 



www.elsevier.com/locate/asr 

# Integrated drought monitoring index: A tool to monitor agricultural drought by using time-series datasets of space-based earth observation satellites 

### K.C. Arun Kumar<sup>a,b</sup> , G.P. Obi Reddy<sup>a,⇑</sup> , P. Masilamani<sup>b</sup> , Satish Y. Turkar<sup>a</sup> , P. Sandeep<sup>a,b</sup> 

> a ICAR-National Bureau of Soil Survey and Land Use Planning, Amravati Road, Nagpur 440 033, India 

> b Department of Geography, Bharathidasan University, Tiruchirappalli, Tamil Nadu 620 024, India 

Received 28 January 2020; received in revised form 27 September 2020; accepted 2 October 2020 

Available online 16 October 2020 

##### Abstract 

In this study, integrated drought monitoring index (IDMI) was proposed as a tool to assess and monitor the spatio-temporal dynamics of agricultural drought during the northeast monsoon season for the period from 2000 to 2016 in Tamil Nadu state, south-eastern part of Indian peninsula. The IDMI is characterized as the principal component of precipitation condition index (PCI), soil moisture condition index (SMCI), temperature condition index (TCI), and vegetation condition index (VCI) derived from time-series satellite observations of climate hazards group infra-red precipitation with stations (CHIRPS), European space agency climate change initiative (ESA-CCI) and moderate resolution imaging spectroradiometer (MODIS). The study shows that in the year 2016, about 44.4 and 17.8% of Tamil Nadu state was under extreme and severe drought conditions, respectively. Sensitivity analysis of the study shows that PCI is the most influential parameter to IDMI, followed by VCI and TCI. The validation of IDMI with 3-month standardized precipitation index (SPI) by using Pearson correlation test shows a strong positive correlation between IDMI and 3-month SPI with correlation coefficient (r) value of 0.73 and 0.77 for the wet (2005) and dry year (2016), respectively. The study clearly demonstrates the potential of IDMI derived from time-series datasets of earth observation satellites as a tool in assessment and monitoring of spatio-temporal dynamics of agricultural drought. The proposed IDMI could be effectively used as a reliable tool to monitor agricultural drought and develop its mitigation strategies to minimise the adverse effects of drought on agriculture, water resources, and livelihoods of the people. � 2020 COSPAR. Published by Elsevier Ltd. All rights reserved. 

Keywords: Agricultural drought; Earth observation satellites; IDMI; MODIS; NDVI 

#### 1. Introduction 

Food and agriculture are vital for achieving Sustainable Development Goals (SDGs) to end the poverty, and hunger (SDG1 and SDG2) and tackle the climate change 

⇑ Corresponding author at: Division of Remote Sensing Applications, ICAR-National Bureau of Soil Survey and Land Use Planning, Amravati Road, Nagpur 440 033, India. 

E-mail address: GPO.Reddy@icar.gov.in (G.P.O. Reddy). 

(SDG11) by 2030 through maintain natural resource base (SDSN, 2013; FAO, 2016). Furthermore, to overcome the challenges like rising global population, global climate change, depletion of irrigation water, land degradation, it is necessary to increase the agricultural production, especially in rainfed arable land (M.C. Anderson et al., 2016; W. Anderson et al., 2016). Assessment of spatio-temporal dynamics of agricultural drought is of great interest as it has wide variability in time and space (Xue and Su, 2017) and has far-reaching impact on global food security and 

https://doi.org/10.1016/j.asr.2020.10.003 0273-1177/� 2020 COSPAR. Published by Elsevier Ltd. All rights reserved. 

K.C. Arun Kumar et al. 

Advances in Space Research 67 (2021) 298–315 

sustainable development (Hu et al., 2019; Kogan et al., 2019). Agricultural drought leads to decline in crop yields due to adverse weather conditions such as erratic rainfall pattern, the rise of global temperature (IPCC, 2018), and the associated decline of soil moisture content (Du et al., 2018). On the other side, the successful assessment and monitoring of agricultural drought requires frequent and internally consistent records of evidence on a range of biophysical variables (Kogan, 2001). Multi-variate analysis and geo-statistical methods commonly used in the assessment of spatio-temporal dynamics of regional droughts (Haining et al., 2010). The common approaches to depict the characteristics of agricultural drought are the region of influence approach (Zrinji and Burn, 1994), the entropy approach (Rajsekhar et al., 2012); the residuals method (Choquette, 1988) and the principal component analysis (PCA) method (Hazaymeh and Hassan, 2017). As agricultural drought generally begins with deficiencies in precipitation, then leads to deficiencies of soil moisture, higher land surface temperature, and at last, it adversely affects the vegetation growth. Therefore, the parameters derived from precipitation, soil and vegetation play a critical role to assess and monitor the agricultural drought. Traditional methods are not fully capable to assess and monitor the agricultural droughts (AghaKouchak and Nakhjiri, 2012) as they are limited in a region, often offers inaccurate measures, moreover, it is hard to get the near-real-time data to predict and quantify them (Easterling, 2013). 

In recent years, the time-series datasets derived from space-based earth observation satellites play a key role in assessment and monitoring of agricultural drought as they provide wide and temporal coverage (Muthumanickam et al., 2011; Reddy et al., 2020). Remote sensing and Geographic Information System (GIS) techniques have been broadly used as an ideal tool in order to assess agricultural drought risk over a large area (Belal et al., 2012; Du et al., 2013; Sa´nchez et al., 2018). Moreover, which helps to monitor the agricultural drought at distinct stages like before, during or after the event (AghaKouchak et al., 2015; Himanshu et al., 2015). By means of satellite remote sensing and GIS technologies, many authors monitored the impact of drought on agriculture in both time and space (Gebrehiwot et al., 2011; Zhang et al., 2017). Moderate resolution imaging spectroradiometer (MODIS) provides near real-time remote sensing datasets and its integration with GIS offers an enhanced agricultural drought assessment (Qian et al., 2016; Zambrano et al., 2016; Santos et al., 2017; Reddy et al., 2020). With modern technological advances in the field of remote sensing, the latest indices of time-series satellite data that are real-time have fully toppled the conventional agricultural drought indices (Elhag and Zhang, 2018). In addition, remote sensing has a tremendous ability to provide comprehensive coverage across a large region with a spatial resolution that varies from a few meters to a few kilometres (Himanshu et al., 2015). Among the indices derived from remote sensing, the normalized difference vegetation index (NDVI) 

(Tucker et al., 2001) is the most robust and widely used index with the capabilities of measuring terrestrial vegetation’s photosynthetic ability during the growing season (Karnieli et al., 2010; Son et al., 2012; Zhang et al., 2016; Okin et al., 2018). Agricultural drought has a relation with precipitation, NDVI, land surface temperature (LST), and soil moisture anomalies in different seasons and regions; however, in some cases, their relationship and correlation are not straight. Table 1 shows various drought indices derived from earth observation satellites and used in the assessment and monitoring of agricultural drought across the globe. 

PCA is a linear transformation that eliminates uncertainty by converting the original component space, enabling the display of drought details without correlation in a new component space (MaChado-MaChado et al., 2011). It was widely used in all forms of analysis since it is a simple, non-parametric method of extracting relevant data from complex datasets (Wold et al., 1987; Zabiri et al., 2007). In recent years, the PCA method (Rencher, 1998) was adopted in developing drought monitoring tools through the aggregation of several hydro-climatic variables into a single drought indicator as it can effectively hold the characteristics of datasets through a lower dimension with a simplified structure (Keyantash and Dracup, 2004; Martins et al., 2012; Liu et al., 2016; Bayissa et al., 2018). Martins et al. (2012) used the PCA approach to study the spatial variance of drought in Portugal by reducing the size and extracting structured data from a large number of time-series drought indices. Liu et al. (2016) used the PCA approach to identify the specific locations and sub-regions, taking into account the drought characteristics to provide a regional view of drought conditions across the Loess Plateau, China. Bayissa et al. (2018) developed a vigorous tool for drought monitoring with the PCA by integrating conventional climate and satellite-based drought indices to describe the severity and spatial distribution of Ethiopia’s historic drought events. Gocic and Trajkovic (2014) was used the PCA model to capture spatio-temporal drought patterns in Serbia by reducing dimensionality in a time-series of standardized precipitation index (SPI). These studies reported the temporal variation of agricultural drought as expressed in the PC scores obtained from the PCA and support the potential application of PCA approach in aggregating several input variables into a single aggregate drought index. The commonly used individual and many composite indices were not capable to monitor and assess the agricultural drought events. As rainfed agriculture is prone to seasonal variation of climate components, the integration of multiple climatic and agricultural drought variables derived from space-based earth observation satellite datasets provides a comprehensive view of drought conditions for its assessment and monitoring (Sepulcre-Canto et al., 2012). 

In India, the agriculture sector is one of the primary sources of livelihood for about 68% of the total population (Dutta et al., 2015), and it contributes about 17% of the 

299 

K.C. Arun Kumar et al. 

Advances in Space Research 67 (2021) 298–315 

Table 1 

Indices derived from earth observation satellites data products in drought assessment and monitoring. 

|Indices|Description|Mathematical expression|References|
|---|---|---|---|
|Vegetation in|dices|||
|NDVI|Normalized Difference<br>Vegetation Index|(q858 �q650)/(q858 + q650)|Tucker (1979) and Kogan (1991, 1995)|
|EVI|Enhanced Vegetation Index|2.5�(q858-q650)/(q858 + 6 �q650 �7/q469 + 1)|Huete et al. (2002) and Saleska et al.<br>(2007)|
|VCI<br>NIR and SW|Vegetation Condition Index<br>IR based indices|(NDVI �NDVImin)/(NDVImax �NDVImin)|Kogan (1995)|
|NDWI1240|Normalized Difference Water<br>Index|(q858 �q1240)/(q858 + q1240)|Gao (1996)|
|LSWI|Land Surface Water Index|(q858 �q1640)/(q858 + q1640)|Xiao et al. (2002)|
|SWISI|Shortwave Infrared Water<br>Stress Index|(q1640 �q850)/(q1640 + q850)|Fensholt and Sandholt (2003)|
|NDWI2130|Normalized Difference Water<br>Index|(q858 �q2130)/(q858 + q2130)|Chen et al. (2005)|
|NMDI|Normalized Multiband<br>Drought Index|(q860 �(q1640 �q2130))/(q860 + (q1640 �q2130))|Wang and Qu (2007)|
|Combined in|dices|||
|VTCI|Vegetation Temperature<br>Condition Index|NDVI, LST|Moran et al. (1994); Wan et al. (2004)|
|TVDI|Temperature Vegetation<br>Dryness Index|NDVI, LST|Sandholt et al. (2002)|
|SDCI|Scaled Drought Condition<br>Index|LST, NDVI, TRMM|Rhee et al. (2010)|
|NDDI|Normalized Difference<br>Drought Index|(NDVI �NDWI)/(NDVI + NDWI)|Gu et al. (2007)|
|ESI|Evaporative Stress Index|LAI, LST, MERRA, TRMM|M.C. Anderson et al. (2016) and W.<br>Anderson et al. (2016)|
|ISDI|Integrated Surface Drought<br>Index|NDVI, LST, ecological zoning, AWC, irrigation water<br>management distribution, DEM|Wu et al. (2015)|
|SDI|Synthesized Drought Index|NDVI, LST, TRMM|Du et al. (2013)|



Note: MODIS is a 36-band instrument (400–1400 nm) with spatial resolution varying from 250 m to 1 km on-board Terra and Aqua orbital platforms. `q` 469 = Blue; `q` 650 = Red; `q` 850 = NIR; `q` 858 = NIR; `q` 860 = NIR; `q` 1240 = SWIR; `q` 1640 = SWIR; `q` 2130 = SWIR. 

country’s gross domestic product (GDP) (Arjun, 2013). Indian agriculture mainly depends on south-west monsoons (June to September) (Kumar et al., 2013) and any changes in monsoon pattern adversely affect the crop conditions and overall economy of the nation (Udmale et al., 2014). There is a growing concern over increasing weather aberrations, and drought patterns with the increasing climate variability in the semi-arid regions of India (Vyas and Bhattacharya, 2020). The Intergovernmental Panel on Climate Change (IPCC) predicted the increase in frequency of droughts over the semi-arid regions of India (IPCC, 2013). The agriculture in Tamil Nadu state, however, vastly depends on northeast monsoon (October to December), which contributes about 60% of the total annual rainfall of the state (Priya and Manimannan, 2014). Any scarcity of rainfall during northeast monsoon results acute water shortage and severe agricultural drought in the state. The present study was aimed firstly to develop comprehensive integrated drought monitoring index (IDMI) as a new tool by using time-series datasets derived from space-based earth observation satellites and PCA, secondly to demonstrate and validate its robustness in monitoring of spatio-temporal patterns of agricultural drought in Tamil Nadu state of Indian Peninsula. 

#### 2. Materials and methods 

#### 2.1. Study area 

Tamil Nadu state in the Indian peninsula lies between 08� 00<sup>0</sup> and 13� 30<sup>0</sup> northern latitudes and 76� 00<sup>0</sup> and 80� 18<sup>0</sup> of eastern longitudes with an area of 13.00 million hectare (Mha) and occupies about 3.96% of the country’s total geographical area (TGA) (Fig. 1). The state is bounded by the Bay of Bengal on its east, Western Ghats on its west, Indian Ocean on its south, Andhra Pradesh state on north, and Karnataka state on its northwest. About 90% area of the state is under the semi-arid climatic condition except the narrow stretches along the coastal and Western Ghats regions. Tamil Nadu state is characterized by equatorial and tropical climates in inland region, whereas, coastal regions are marked with equatorial and maritime climates. The average temperature of the state ranges from 28 �C to 40 �C in the summer and 18 �C to 26 �C in the winter season. The southwest (June to September) and northeast (October to December) monsoon seasons are the state’s two main rainfall seasons. However, agriculture in Tamil Nadu is largely depends on northeast monsoon, it contributes about 60% of the state’s total annual rainfall 

300 

K.C. Arun Kumar et al. 

Advances in Space Research 67 (2021) 298–315 



Fig. 1. Location of the study area with rain-gauge stations. 

(Nathan, 1998; Selvaraj, 2009). The state’s cultivated area is 4.7 (Mha), which constitutes about 36% of the TGA, out of which the rainfed area occupies 2.55 Mha, which 

is about 54% of the cultivated area. Rice, maize, sorghum, pearl millet, finger millet, and pulses are the main food crops grown in the state. Cotton, sugarcane, oilseeds, coffee, 

301 

K.C. Arun Kumar et al. 

Advances in Space Research 67 (2021) 298–315 

tea, rubber, coconut, and chillies are among the cash crops. Bananas and mangoes are the major horticultural crops grown in the study area. 

#### 2.2. Datasets used 

In the present study, the daily rainfall data obtained for 208 rain-gauge stations from Tamil Nadu Public Works Department (PWD), Chennai was used for the period from 1987 to 2016. The analysis of rainfall trends shows that the erratic rainfall patterns are quite common during northeast monsoon during the year 2000 to 2016. The analysis of time-series rainfall data for the northeast monsoon season during the period from 2000 to 2016 shows that the year 2005 was wet and 2016 was dry year, respectively (Fig. 2). These two years were considered for the detailed study of spatio-temporal and intra-seasonal variability of agricultural drought in Tamil Nadu state. District wise crop area and yields for maize, pearl millet, and sorghum, which are the major rainfed crops during the northeast monsoon season in the state were obtained from the Directorate of Economics and Statistics (DES), Govt. of India (https://aps.dac.gov.in/) for the period from 2011 - 12 to 2015–16. 

The Climate Hazards Group Infra-Red Precipitation with Stations (CHIRPS) satellite monthly rainfall products (ver. 3.0) having one-month temporal resolution and spatial resolution of 0.05� � 0.05� were downloaded (https:// www.chc.ucsb.edu/data). It blends satellite estimates and gauge observations based on infrared Cold Cloud Duration (CCD) observations (Saha et al., 2011). The European Space Agency Climate Change Initiative (ESA-CCI) developed the soil moisture data (ver. 4.2), the same was download (https://www.esa-soilmoisture-cci.org/) for the northeast monsoon season during 2000 to 2016 and used as it provides statistically consistent soil moisture data at a spatial resolution of 0.25� � 0.25� (Dorigo et al., 2017). 

Time-series MODIS datasets used for the study were obtained for the northeast monsoon season during 2000 to 2016 from the Land Processes Distributed Active Center (http://lpdaac.usgs.gov/). High quality, consistent and well-calibrated 16-day interval MODIS NDVI products (MOD13Q1) of 250 m resolution were used to compute vegetation condition index (VCI). The MODIS 8-day LST data products (MOD11A2) at 1 km resolution were used for the northeast monsoon season during 2000 to 2016 to compute temperature condition index (TCI). 

#### 2.3. Computation of 3-month SPI 

SPI is an index of probability considers mainly precipitation for any given time scales, developed with historical data to monitor and assess the drought for any rainfall station. McKee et al. (1993, 1995) proposed the SPI as drought monitoring index to define drought intensities (Table 2). In the study, SPI was computed for the period from 1987 to 2016 at 3-month time-scale for 208 rainfall stations in the study area. Subsequently, 3-month SPI values were obtained at each rain-gauge station and the same were used to develop 3-month SPI rasters’ for the northeast monsoon season from the year 2000 to 2016 by using ordinary kriging interpolation technique in ArcGIS (ESRI, 2001). Positive SPI values are more than the normal precipitation, while unfavourable values are less than normal precipitation. The seven-category classification system of McKee et al. (1993, 1995) for the SPI namely extremely wet (>2.0), very wet (1.5–1.99), moderately wet (1.0– 1.49), near normal (�0.99 to 0.99), moderately dry (�1.00 to �1.49), severely dry (�1.5 to �1.99), and extremely dry (<-2.0) was followed to classify the SPI in the study. The analysis of 3-month SPI for the period from 2000 to 2016 shows that 2005 was wet and 2016 was dry year, respectively. The computed 3-month SPI was used to validate IDMI of wet (2005) and dry (2016) years to 



Fig. 2. Distribution of seasonal rainfall of northeast monsoon and departure from the seasonal mean rainfall during the period from 1987 to 2016. 

302 

K.C. Arun Kumar et al. 

Advances in Space Research 67 (2021) 298–315 

Table 2 

Drought indices used in this study and their data sources. 

|Drought indices|Data source|Mathematical expression|References|
|---|---|---|---|
|SPI|Rain-gauge|(Xij �Xi)/r|McKee et al. (1993, 1995)|
|PCI|CHIRPS|(CHIRPSi �CHIRPSmin)/(CHIRPSmax �CHIRPSmin)|Du et al. (2013)|
|SMCI|ESA-CCI SM|(SMmax �SMi)/(SMmax �SMmin)|Hao et al. (2015)|
|TCI|MOD 11 A2|(LSTmax �LSTi)/(LSTmax �LSTmin)|Kogan (1997)|
|VCI|MOD 13 Q1|(NDVIi �NDVImin)/(NDVImax �NDVImin)|Kogan (1995)|



Note: r is standard deviation for the i<sup>th</sup> station, Xij is the precipitation for the i<sup>th</sup> station and j<sup>th</sup> observation, Xi is the mean precipitation for the i<sup>th</sup> station. CHIRPSi, SMi, LSTi, NDVIi – monthly CHIRPS, SM, LST, NDVI for pixel current month of i. CHIRPSmin, SMmin,LSTmin, NDVImin � 17 years minimum CHIRPS, SM, LST, NDVI for the of pixels i<sup>th</sup> month. CHIRPSmax,SMmax, LSTmax, NDVImax � 17 years maximum CHIRPS, SM, LST, NDVI for the of pixels i<sup>th</sup> month, respectively. 

understand the intra-seasonal variability of drought intensity in Tamil Nadu state. 

2.4. Computation of scaled remote sensing drought indices 

The precipitation condition index (PCI) is an index relying on precipitation estimates (i.e., CHIRPS); Du et al. (2013) introduced it as a systematic variance of precipitation from its long-term mean to monitor precipitation deficits from the climate signal (Table 2). PCI also changes from 0 to 1, from severely undesirable to optimum, due to variations in precipitation. In case of meteorological drought with extremely low precipitation, the PCI is below or equivalent to 0, and at flooding conditions the PCI is close to 1. In the study, monthly PCI was computed for the northeast monsoon season from 2000 to 2016. Data of ESA-CCI for the period of northeast monsoon season were downscaled to 250 m by using ‘bi-linear interpolation technique’ in ArcGIS to get parity with the MODIS 250 m data products. Similarly, soil moisture condition index (SMCI) (Hao et al., 2015) was also used as one of the input parameters to assess and monitor the agricultural drought in the study area (Table 2). The values of SMCI vary from 0 to 1. The low values of SMCI imply the serious condition of drought. Under a drought process, the SMCI is close or equal to 0, and at wet conditions, the SMCI is close to 1. In the study, the monthly SMCI was computed for northeast monsoon season for the period from 2000 to 2016. LST data were derived from 8-day MODIS MOD11A2 data product with a spatial resolution of 1 km and were composed by maximum value composite (MVC) in a monthly format and same was used to compute TCI (Kogan, 1997) and estimate the thermal impact of drought (Table 2). The values of TCI vary from 0 to 1 and low values of TCI imply the serious condition of drought. Under a drought process, the TCI is close or equal to 0, and at wet conditions, the TCI is close to 1. In the study, monthly TCI for northeast monsoon season from the year 2000 to 2016 was computed. 

The Savitzky-Golay (Chen et al., 2004) filter was applied by using TIMESAT software (Jo¨nsson and Eklundh, 2002) to smoothen time-series MODIS MOD13Q1 16-day composites and these datasets were used to generate MVC to minimize further non-vegetation effects (Holben, 1986; 

Maisongrande et al., 2004; Tang et al., 2017). Kogan (1995) suggested VCI and shows how close the NDVI of the current month is to the minimum NDVI calculated from the long-term record (Table 2). VCI provides the information on the current status of vegetation as compared with the historical maximum and minimum (Kogan, 1997). VCI provides the deviation of each pixel from the historical NDVI values. VCI from 0 to 1 indicates an extremely unfavourable to optimal increase in vegetation consistency (Kogan, 1995). The vegetation condition is low in an extremely dry month and the VCI is near to or equivalent to 0. The VCI of 0.5 represents the state of healthy vegetation and at optimal conditions of vegetation, VCI is close to 1 (Jain et al., 2009). 

#### 2.5. Computation of IDMI using earth observation satellite datasets and PCA 

PCA is a mathematical technique for reducing the dimensionality of a dataset (Jackson, 1983). Due to numeric digital remote sensing images, this approach may reduce their dimensions. The bands are the initial variables of multi-band remote sensing images. In the present study, PCA (Storch and Zwiers, 1999) was used to develop IDMI to identify the spatial patterns of agricultural drought over Tamil Nadu state by integrating satellite-based input parameters that include CHIRPS rainfall, soil moisture, LST, and NDVI. The computation of the principal components involves constructing a square (p � p, where p is the number of input parameters) symmetric correlation coefficient matrix for each pixel. Accordingly, 4 � 4 correlation co-efficient matrix was developed by using the standardized time-series values of the four input parameters. This matrix was used to determine the eigenvectors that were ultimately used to transform the input variables into different orthogonal key components (PCs) (equivalent in this case to the number of input parameters-four). The eigenvectors are unit vectors that identify the relationship between the key components and the original information. The PCs are orthogonal vectors and the implementation of mathematical functions (Keyantash and Dracup, 2004) makes it more difficult to transform them into a single vector. The first component, or new axis called PC1, is defined by the direction of greatest variance in all input data. The second, PC2, 

303 

Advances in Space Research 67 (2021) 298–315 

###### K.C. Arun Kumar et al. 

is orthogonal to it and accounts for the maximum remaining variance not accounted by component 1. Each subsequent axis is defined in the same way. In the present study, the first principal component axis (PC1) was used to develop IDMI (Fig. 3) to satisfy the larger variability in input data. The process first computes the covariance matrix of S among all i input parameters. S is symmetric and of dimensions k � k, where k is the total number of input parameters. S is calculated by using the Eq. (1). 



where k1, k2 k3 and k4 are four input parameters represented by PCI, SMCI, TCI, and VCI, respectively; Pij is the brightness value of a pixel in row i and column j; n is the number of rows; m is the number of columns; `m` is mean of all pixel values in the given input parameters. 

The percent of variance in the total dataset was explained by each component i by using the Eq. (2). 



where (ki) represents diagonal elements of eigenvalues and k represents input parameter k1, k2, k3 and k4. 

IDMI is calculated by multiplying the eigenvector for that component by the vector of original pixel values in the input parameters by using the Eq. (3). 



where Pk is brightness value of input parameter k1, k2, k3 and k4; Ui is eigenvector element for component i in input parameter k1, k2, k3 and k4; and n is the number of input 



Fig. 3. Principal components score of IDMI. 

Table 3 

Classification schema for IDMI and their probability of occurrence. 

|IDMI|IDMI drought classes|Probability (%)|
|---|---|---|
|�2.0 and less|Extreme drought|2.3|
|�1.5 to �1.99|Severe drought|4.4|
|�1.0 to �1.49|Mild drought|9.2|
|�0.99 to 0.99|Normal|68.2|
|1.0 to 1.49|Mild wet|9.2|
|1.5 to 1.99|Very wet|4.4|
|2.0 and more|Extreme wet|2.3|



parameters. The classification schema of IDMI based the probability of occurance is shown in Table 3. 

#### 2.6. Validation of IDMI with 3-month SPI using Pearson correlation test 

Pearson correlation test was performed between indices such as dependent variable (i.e., IDMI) and the independent variable (i.e., 3-month SPI) to evaluate the robustness of IDMI derived from time-series remotely sensed data to monitor the drought over time and space. Since the relationship between remotely sensed drought indices and 3-month SPI varies over time (Ji and Peters, 2003), the Pearson correlation test for wet (2005) and dry (2016) years of northeast season was carried out. The mean IDMI values were extracted based on the location of the in-situ raingauge stations (i.e., Tehsils) by using Arc GIS. The Pearson correlation test was carried out between IDMI and 3- month SPI using the following mathematical equation. 



where Rxy is the correlation coefficient, n is the length of the time-series, and i is the number of the years from 2000 to 2016 (1–17). Whereas, xi and yi are the 3-month SPI and the IDMI in year i, respectively, and x and y are the mean 3-month SPI and the mean IDMI, respectively, from 2000 to 2016. Galarc¸a et al. (2010) and Figueiredo Filho and da Silva Ju´nior (2009) stated that the Pearson correlation coefficient (r) has values ranging from �1 to 1, where, values close to 1 (r = 1) represents a perfectly positive correlation and values close to �1 (r = �1) represents a perfectly negative correlation between two variables. Dancey and Reidy (2006) suggested that the Pearson correlation coefficient (r) be graded as r = 0.10 to 0.30 (weak), r = 0.40 to 0.60 (moderate), and r = 0.70 to1.0 (strong). 

#### 2.7. Validation of IDMI with crop areas and yields 

To validate the impact of drought assessed through IDMI, the percent area under extreme, severe and mild drought classes with respect to total geographical area of the district was computed for the dry (2016) year. For validation of crop area and yields with IDMI, the three 

304 

K.C. Arun Kumar et al. 

Advances in Space Research 67 (2021) 298–315 

important crops i.e., maize, pearl millet, and sorghum grown in the study area during the northeast monsoon season were selected and compiled the district wise data on crop area and yields for the period from 2011–12 to 2015–16. Further, crop wise mean area and mean yields were computed at district level for the same period. In order to obtain the crop area departure from mean for the year 2015–16, the deviation has been worked out based on the mean crop area and crop area of the year 2015–16 at district level for maize, pearl millet, and sorghum crops. Similarly, for the same period, the crop wise yields departure from the mean for the year 2015–16 for maize, pearl millet and sorghum crops were computed at district level. The percent departure of crop area and crop yields from mean for the dry (2016) year were computed and plotted against to the percent area under extreme, severe, and mild drought classes of IDMI to validate the robustness of IDMI in monitoring of agricultural drought and to know the impact of drought on crop area and yields. The detailed methodology followed in the study is shown in Fig. 4. 

conditions in the majority of the years. However, the extreme wet condition was noticed in the year 2005, followed by 2004 and 2006 (Fig. 5). The analysis shows a recurring dry condition continuously from 2000 to 2003. During this period, the near-normal condition (�0.99 to 0.99) was noticed in large parts of the study area. During the dry year 2016, around 45 Mha of the state was under extremely dry condition (<�2.0), more particularly in central and western parts as compared to the extreme southern and northern parts of the study area. During this period, the lowest 3-month SPI (�3.09) was observed at Chidambaram station in the eastern part of the study area. The analysis clearly exhibits the worst dry conditions of Tamil Nadu during the below normal rainfall more particularly in the year 2016. However, moderately wet to wet conditions were observed in the northeast monsoon season during the year 2005 followed by 2004 and 2006 with the highest 3-month SPI (1.62) was observed in the year 2005 at Tirupattur station in the northern part of the study area. 

#### 3.2. Monitoring of agricultural drought using IDMI 

#### 3. Results 

#### 3.1. Spatio-temporal variability of 3-month SPI 

The spatio-temporal analysis of seasonal 3-month SPI for the period from 2000 to 2016 shows that study area was experienced above near-normal (�0.99 to 0.99) dry 

IDMI illustrates the impact of precipitation, soil moisture, temperature, and vegetation on the intensity and spatial-temporal dynamics of agricultural drought. The analysis of seasonal IDMI shows a high variability from extreme drought (�2.0 and less) to no drought (2.0 and more) condition during the period from 2000 to 2016 



<!-- Start of picture text -->
Earth observation satellites data<br>ESA-CCI Soil<br>MOD13Q1 MOD11A2 moisture CHIRPS<br>Data Pre-processing<br>Savitsky- Downscale to  Monthly<br>Golay filter Monthly LST 250m resolution precipitation<br>Data Preparation<br>VCI TCI SMCI PCI<br>Validation<br>Principal Component<br>Analysis<br>in situ  Rainfall  Integrated Drought  Crop census<br>data Monitoring Index data<br>(IDMI)<br>Model validation  Crop area and yield<br>3-month SPI (Maize, Pearl millet<br>and analysis<br>and Sorghum)<br><!-- End of picture text -->

Fig. 4. Methodology followed in the study. 

305 

K.C. Arun Kumar et al. 

Advances in Space Research 67 (2021) 298–315 



<!-- Start of picture text -->
2000 2001 2002 2003<br>2004 2005 2006 2007<br>2008 2009 2010 2011<br>2012 2013 2014 2015<br>2016<br>SPI drought classes<br>-2.0 and less (Extremely dry) 1.0 to 1.49 (Moderately wet)<br>-1.5 to -1.99 (Severely dry) 1.5 to 1.99 (Very wet)<br>-1.0 to -1.49 (Moderately dry) 2.0 and more (Extremely wet)<br>-0.99 to 0.99 (Near normal)<br>0 150 300<br>km<br><!-- End of picture text -->

Fig. 5. Spatio-temporal dynamic of 3-month SPI during the period from 2000 to 2016 in Tamil Nadu. 

(Fig. 6). The analysis indicates that in the year 2016 the majority of the study area was under dry condition, followed by 2000, 2001, 2002, 2012, and 2013. During the year 

2000, extreme drought condition was experienced in the south-eastern part of the study area, whereas, in the year 2001 and 2002 similar drought condition was noticed in 

306 

K.C. Arun Kumar et al. 

Advances in Space Research 67 (2021) 298–315 



Fig. 6. Spatio-temporal dynamic of IDMI during the period from 2000 to 2016 in Tamil Nadu. 

307 

K.C. Arun Kumar et al. 

Advances in Space Research 67 (2021) 298–315 

the northern part of the study area. The extreme drought condition was witnessed over the northern and south western parts of the study area during the year 2012 and 2013. During the wet year (2005), except the southern tip of the state, about 10.1 and 6.0% of TGA of the state was under extreme and very wet conditions, respectively. However, in the dry (2016) year, it was clearly observed that the districts of Salem, Namakkal, Tiruchirappalli, Ramanathapuram, Kurur, and Thoothukudi were under extreme to severe drought category. Whereas, Dindigul, Thiruvarur southern parts of Erode, and eastern parts of Cuddalore were under moderate drought condition. In the year 2016, about 44.4 and 17.8% of TGA of the state was observed under extreme and severe drought conditions, respectively. However, the year 2005 to 2011 and 2015 were found as normal years. In the year 2016, the northeast monsoon was ended with a deficit rainfall of 62% (168 mm out of the normal rainfall of 440 mm), leaving several areas under drought in Tamil Nadu. Interestingly, it was observed that after the disastrous floods in Chennai and other parts of Tamil Nadu in the year 2015, the state was faced one of its worst droughts during the northeast monsoon season in the subsequent year 2016 (Fig. 7). 

3.3. Correlation of IDMI with 3-month SPI in wet and dry years 

The independent in-situ meteorological drought index, i.e. 3-month SPI was used to validate the results of IDMI. The Pearson correlation of IDMI with 3-month SPI for both the wet (2005) and dry (2016) years shows a strong positive relationship. The analysis shows a strong positive correlation between IDMI and 3-month SPI with a correlation coefficient (r) of 0.73 (Fig. 8a) during the wet (2005) year. The correlation of IDMI and 3-month SPI during the dry (2016) year shows a strong positive correlation with a correlation coefficient (r) of 0.77 (Fig. 8b). The 

Pearson correlation test clearly shows that IDMI found to be a robust drought index to assess the agricultural drought vulnerability in time and space. 

#### 4. Discussion 

#### 4.1. Intra-seasonal variability of IDMI and 3-month SPI in wet year 

To understand the intra-seasonal variability of drought intensity of Tamil Nadu, the spatio-temporal variability of 3-month SPI and IDMI for the wet year (2005) during the northeast monsoon season was analysed. The analysis shows that moderately wet to very wet conditions with mean seasonal 3-month SPI of 1.7 were observed. During the northeast monsoon season, the intra-seasonal analysis of 3-month SPI shows the relatively near-normal conditions in the month of November as compared to the wet to very wet conditions in the month of October (Fig. 9a and b). Whereas, in the month of December (Fig. 9c), near normal condition was observed in the majority of the study area except the northern part of the state, where the moderate wet condition was observed. In case of IDMI, though 2005 was the wet year, the moderate to severe drought conditions were observed in the month of October particularly in Kanyakumari, Tirunelveli, and Tuticorin districts in the southern part of the study area (Fig. 9d). Whereas, in the month of November (Fig. 9e), moderate drought condition was observed in major parts of the state more particularly in Kanyakumari, Tirunelveli, and Tuticorin districts of the study area. The analysis of IDMI for the month of December shows no drought conditions (Fig. 9f) this could be attributed to good rainfall received during the month of December. The analysis of intra-seasonal variability of 3- month SPI and IDMI during the wet years clearly indicates the spatio-temporal variability of dry or wet conditions and intensity of drought within the northeast monsoon season. 



<!-- Start of picture text -->
80.0 1600<br>Extreme drought Severe drought Mild drought Rainfall<br>70.0 1400<br>60.0 1200<br>50.0 1000<br>40.0 800<br>30.0 600<br>20.0 400<br>10.0 200<br>0.0 0<br>2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016<br>Rainfall ( in mm)<br>Drought affected area in Tamil Nadu ( in %)<br><!-- End of picture text -->

Fig. 7. Symbiotic relationship between the rainfall and IDMI during the northeast monsoon season (2000 to 2016). 308 

K.C. Arun Kumar et al. 

Advances in Space Research 67 (2021) 298–315 



Fig. 8. (a and b) Pearson correlation between the 3-month SPI v/s IDMI during the wet year (2005) and dry year (2016). 



Fig. 9. (a–f) Intra-seasonal variability of 3-month SPI and IDMI during the wet year (2005). 

4.2. Intra-seasonal variability of IDMI and 3-month SPI in dry year 

The intra-seasonal variability of 3-month SPI exhibits the spatial extent of dry condition during October, Novem- 

ber, and December months of the northeast monsoon in the dry year 2016 of the Tamil Nadu state. During the month of October (Fig. 10a), the extremely dry condition was confined mostly to northern and north-eastern parts of the study area. In the month of November (Fig. 10b), 

309 

K.C. Arun Kumar et al. 

Advances in Space Research 67 (2021) 298–315 

the districts of the northern and eastern parts of the state were experienced the extremely dry condition (�2.0 and less) and rest of the state was under the near-normal condition. However, in the month of December (Fig. 10c), the entire study area was under the near-normal condition except some parts of Krishnagiri and Erode districts. The intra-seasonal variability of IDMI shows that the drought phenomenon was extreme in the months of October and November, but it was subdued in the month of December. In the month of October (Fig. 10d), extreme drought (<�2.0) condition was observed in almost all the districts except in Madurai, Virudhunagar, and Kanchipuram districts. Similar conditions were also observed in the month of November except in Tirunelveli, and Tuticorin districts (Fig. 10e). Whereas, during the month of December (Fig. 10f) extreme drought (<�2.0) condition was observed in central and eastern parts of the study area and it was subdued in rest of the area of the state. The analysis clearly shows that in the year 2016, the distinct intra-seasonal variability of 3-month SPI and IDMI was observed, this could be attributed to the receipt of about 62.0% deficient rainfall as compared to the mean rainfall of northeast monsoon season of the study area. 

#### 4.3. Validation of IDMI with crop areas and yields 

The relationship between the crop areas, yields, and IDMI were investigated for dry year (2016) by considering the area under extreme, moderate, and mild drought classes. The analysis of district wise percent crop area departure from the mean of maize, pearl millet, and sorghum for the year 2015–16 shows that the highest negative departure from the mean area of maize was observed in Karur, Namakkal and Thiruvarur districts, pearl millet in Nagapattinam, Namakkal, and Thoothukudi districts and sorghum in Erode, Thiruvarur, and Thiruvallur districts. The percent crop area departure from the mean during the year (2016) with respect to the drought classes clearly shows that area under maize was far below the mean area in half of the districts expect in Madhurai, and Perambalur districts. In case of pearl millet, the percent crop area departure from the mean during the year (2016) shows that it was below the mean in majority of the districts, except in Cuddalore, Kanchipuram, and Theni districts. Similarly, in case of sorghum, more than half of the districts in the state shown the below normal crop area except in Krishnagiri, and Vellore districts 



Fig. 10. (a–f) Intra-seasonal variability of 3-month SPI and IDMI during the dry year (2016). 

310 

K.C. Arun Kumar et al. 

Advances in Space Research 67 (2021) 298–315 

(Fig. 11a). The analysis of district wise percent crop yield departure from the mean for the year (2016) with respect to the drought classes clearly shows that maize yields were far below the mean in almost all the districts where extreme and severe drought was occurred except in Villupuram district. The percent crop yield departure from the mean for pearl millet, and sorghum with respect to the drought classes also shows that the yields are far below the mean in almost all the districts where extreme and severe drought was occurred except in Madhurai, and Vullupuram districts. However, in case of sorghum almost all the districts in the state shown below normal yields (Fig. 11b). The validation of extreme, severe, and mild drought classes of IDMI clearly shows the impact of drought on crop area and more particularly on yields in the study area. The impact analysis of drought with respect to crop area and yields of maize, pearl millet, and sorghum clearly demonstrate the robustness of IDMI in monitoring of agricultural drought. 

#### 4.4. Sensitivity analysis 

Sensitivity analysis was carried out to determine how a different value of an independent variable (i.e., IDMI) influences particular dependent variables (i.e., PCI, SMCI, TCI and VCI) under a given set of assumptions. To identify the most influential parameter for the IDMI, the ‘linear interaction model’ was used in the study. This gives incorrect estimates of the standard errors and p-values and variables whose contribution is minimal can be deleted. Therefore, the sensitivity analysis finds all the risk factors of a scenario to be equivalent and attempts to sequentially classify the applicant subset of variables; therefore, most of these approaches concentrate on the main effects and neglect higher-order effects (variable interactions) (Fig. 12). When we considered a single parameter for sensitivity analysis, VCI shows more sensitive followed by TCI, considering the standard error. In combination of two, PCI:VCI is more sensitive followed by PCI:TCI. 



Fig. 11. (a and b) Relationships between crop areas, yields and IDMI drought classes during the dry year (2016). 

311 

K.C. Arun Kumar et al. 

Advances in Space Research 67 (2021) 298–315 



Fig. 12. Predicting parameters of IDMI by sensitivity analysis. 

Table 4 

Estimated coefficients and standard errors for different variable selection methods. 

|Factors|Estimated error|Standard error|IDMI|p-value|
|---|---|---|---|---|
|PCI|13.202|0.376|35.100|<2e�16***|
|SMCI|�5.341|0.513|�10.421|<2e�16***|
|TCI|3.274|0.214|15.303|<2e�16***|
|VCI|3.659|0.103|35.603|<2e�16***|
|PCI:SMCI|1.388|3.934|0.353|0.725|
|PCI:TCI|2.936|1.633|1.798|0.074*|
|SMCI:TCI|10.289|3.794|2.712|0.007**|
|PCI:VCI|�0.339|0.791|�0.429|0.669|
|SMCI:VCI|0.482|1.132|0.426|0.671|
|TCI:VCI|0.486|0.371|1.311|0.192|
|PCI:SMCI:TCI|�85.838|25.666|�3.344|0.001***|
|PCI:SMCI:VCI|�1.822|8.289|�0.220|0.826|
|PCI:TCI:VCI|�4.357|2.930|�1.487|0.139|
|SMCI:TCI:VCI|�18.891|6.443|�2.932|0.004**|
|PCI:SMCI:TCI:VCI|149.675|43.761|3.420|0.001***|



Significant codes: ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.1. 

However, in combination of three, PCI:TCI:VCI shows the most influencing parameters in assessment and monitoring of intensity of agricultural drought (Table 4). The sensitivity analysis distinguishes the most and least contributing parameters and their combinations in assessment and monitoring of intensity of the agricultural drought. 

#### 5. Conclusions 

The analysis of spatio-temporal variability of 3-month SPI for the dry year 2016 shows that moderate to extremely dry conditions (�2.0 and less) in the central part of the study area covers mainly in Kongu uplands and parts of the Cauvery delta region of the study area more particularly in the months of October and November. The analysis of IDMI for the period from 2000 to 2016 clearly shows moderate to extremely dry conditions during the dry year 2016, especially in central, northern and north-western parts of the state. However, in the year 2005, almost all 

the districts exhibit extremely wet to near-normal conditions due to high rainfall during the northeastern monsoon season. However, during the dry year (2016), IDMI shows about 44.4% of the state was witnessed extreme drought (�2.0 and less) and 17.2% experienced severe drought conditions (�1.5 to �1.99). Whereas, in the wet year 2005, about 10.06% of the state was under extreme wet (2.0 and more) condition due to high rainfall conditions. Analysis of intra-seasonal drought variability during the wet year (2005) in the northeastern season clearly shows the impact of rainfall through 3-month SPI on spatiotemporal dynamics of IDMI. This might be due to good rainfall received and its subsequent positive impact on vegetation. During the dry year (2016), the direct impact of rainfall exhibits through 3-month SPI on spatio-temporal dynamics of IDMI was observed particularly in the months of November and December. This could be attributed to low rainfall and its direct adverse impact on vegetation. The validation of IDMI with 3-month SPI by using 

312 

K.C. Arun Kumar et al. 

Advances in Space Research 67 (2021) 298–315 

Pearson correlation test shows a strong positive correlation coefficient (r) of 0.73 and 0.77 during the wet year (2005) and dry year (2016), respectively. The analysis of impact of drought on area and yields of maize, pearl millet, and sorghum during the dry year (2016) show the robustness of IDMI in monitoring of agricultural drought. Sensitivity analysis shows that, PCI is the most influencing parameter followed by VCI and TCI in assessment and monitoring of intensity of agricultural drought. The study clearly demonstrates the potential of proposed IDMI derived from time-series datasets of space-based earth observation satellites in assessment and monitoring of spatio-temporal variability of agricultural drought. The results obtained from the proposed IDMI are comprehensive and reliable to develop the agricultural drought mitigation measures and policies by the decision-makers to minimise the adverse effects of drought on agriculture, water resources and livelihoods of the people in the state. 

#### Declaration of Competing Interest 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

#### Acknowledgments 

The authors are thankful to NASA LPDAAC, ESA-CCI and CHC for providing time-series MODIS, soil moisture and precipitation datasets at free of cost for this research. The authors are thankful to the Director, ICAR-National Bureau of Soil Survey and Land Use Planning (NBSS&LUP), Nagpur for extending the facilities to carry out the work. The authors also thankful to Tamil Nadu Public Works Department (PWD), Chennai for providing the rainfall data. This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors. We sincerely thank anonymous reviewers whose constructive comments and suggestions greatly helped to improve the overall quality of manuscript. 

#### References 

- AghaKouchak, A., Farahmand, A., Melton, F.S., Teixeira, J., Anderson, M.C., Wardlow, B.D., Hain, C.R., 2015. Remote sensing of drought: progress, challenges and opportunities. Rev. Geophys. 53 (2), 452–480. 

- AghaKouchak, A., Nakhjiri, N., 2012. A near real-time satellite-based global drought climate data record. Environ. Res. Lett. 7 (4) 044037. 

- Anderson, M.C., Zolin, C.A., Sentelhas, P.C., Hain, C.R., Semmens, K., Yilmaz, M.T., Gao, F., Otkin, J.A., Tetrault, R., 2016a. The evaporative stress index as an indicator of agricultural drought in Brazil: an assessment based on crop yield impacts. Remote Sens. Environ. 174, 82–99. 

- Anderson, W., Johansen, C., Siddique, K.H., 2016b. Addressing the yield gap in rainfed crops: a review. Agron. Sustain. Dev. 36, 1–13. 

- Arjun, K.M., 2013. Indian agriculture-status, importance and role in Indian economy. Int. J. Agr. Food Sci. Tech. 4, 343–346. 

- Bayissa, Y.A., Tadesse, T., Svoboda, M., Wardlow, B., Poulsen, C., Swigart, J., Van Andel, S.J., 2018. Developing a satellite-based combined drought indicator to monitor agricultural drought: a case study for Ethiopia. Gisci. Remote Sens., 1–31 

- Belal, A.A., El-Ramady, H.R., Mohamed, E.S., Saleh, A.M., 2012. Drought risk assessment using remote sensing and GIS techniques. Arab. J. Geosci. 7 (1), 35–53. 

- Chen, D., Huang, J., Jackson, T.J., 2005. Vegetation water content estimation for corn and soybeans using spectral indices derived from MODIS near-and short-wave infrared bands. Remote Sens. Environ. 98, 225–236. 

- Chen, J., Jo¨nsson, P., Tamura, M., Gu, Z., Matsushita, B., Eklundh, L., 2004. A simple method for reconstructing a high-quality NDVI timeseries data set based on the Savitzky-Golay filter. Remote Sens. Environ. 91, 332–344. 

- Choquette, A.F., 1988. Regionalization of peak discharges for streams in Kentucky: U.S. Geological Survey Water-Resources Investigations Report 87-4209, 105 p. 

- Dancey, C., Reidy, J., 2006. Estatı´sticasemmatema´tica para psicologia: usando SPSS para Windows. Porto Alegre, 608p. 

- Dorigo, W.A. et al., 2017. ESA CCI Soil moisture for improved earth system understanding: state-of-the art and future directions. Remote Sens. Environ. 203, 185–215. 

- Du, L., Tian, Q., Yu, T., Meng, Q., Jancso, T., Udvardy, P., Huang, Y., 2013. A comprehensive drought monitoring method integrating MODIS and TRMM data. Int. J. Appl. Earth Obs. Geoinf. 23, 245– 253. 

- Du, T.L.T., Bui, D.D., Nguyen, M.D., Lee, H., 2018. Satellite-based, multi-indices for evaluation of agricultural droughts in a highly dynamic tropical catchment, Central Vietnam. Water. 10 (5), 659. 

- Dutta, D., Kundu, A., Patel, N.R., Saha, S.K., Siddiqui, A.R., 2015. Assessment of agricultural drought in Rajasthan (India) using remote sensing derived Vegetation Condition Index (VCI) and Standardized Precipitation Index (SPI). Egypt J. Remote Sens. Space Sci. 18 (1), 53– 63. 

- Easterling, D.R., 2013. Global data sets for analysis of climate extremes. In: AghaKouchak, A., Easterling, D., Hsu, K., Schubert, S., Sorooshian, S., (Eds.), Extremes in a Changing Climate. Water Science and Technology Library, 65. Springer, Dordrecht. 

- Elhag, K.M., Zhang, W., 2018. Monitoring and assessment of drought focused on its impact on sorghum yield over Sudan by using meteorological drought indices for the period 2001–2011. Remote Sens. 10 (8), 1231. 

- ESRI, 2001. Using ArcGIS Geostatistical Analyst. ESRI Press, Redlands, CA. 

- FAO, 2016. Food and Agriculture: Key to achieving the 2030 agenda for sustainable development. Food and Agriculture Organization of the United Nations, Rome, Italy. 

- Fensholt, R., Sandholt, I., 2003. Derivation of a shortwave infrared water stress index from MODIS near-and shortwave infrared data in a semiarid environment. Remote Sens. Environ. 87 (1), 111–121. 

- Figueiredo Filho, D.B., da Silva Ju´nior, J.A., 2009. Desvendandoos Miste´rios do Coeficiente de Correlac¸a˜o de Pearson (r). Revista Polı´tica Hoje 18 (1), 115–146. 

- Galarc¸a, S.P., Lima, C.S.M., Silveira, G., Rufato, A.R., 2010. Correlac¸a˜o de Pearson e ana´lise de trilhaidentificandovaria´veis para caracterizar porta-enxerto de Pyruscommunis L. Cieˆncia e Agrotecnologia. 34 (4), 860–869. 

- Gao, B.C., 1996. NDWI- A normalized difference water index for remote sensing of vegetation liquid water from space. Remote Sens. Environ. 58 (3), 257–266. 

- Gebrehiwot, T., Van der Veen, A., Maathuis, B., 2011. Spatial and temporal assessment of drought in the northern highlands of Ethiopia. Int. J. Appl. Earth Obs. Geoinf. 13 (3), 309–321. 

- Gocic, M., Trajkovic, S., 2014. Spatiotemporal characteristics of drought in Serbia. J. Hydrol. 510, 110–123. 

313 

K.C. Arun Kumar et al. 

Advances in Space Research 67 (2021) 298–315 

- Gu, Y., Brown, J.F., Verdin, J.P., Wardlow, B., 2007. A five-year analysis of MODIS NDVI and NDWI for grassland drought assessment over the central Great Plains of the United States. Geophys. Res. Lett. 34. 

- Haining, R.P., Kerry, R., Oliver, M.A., 2010. Geography, spatial data analysis, and geostatistics: an overview. Geogr. Anal. 42 (1), 7–31. 

- Hao, C., Zhang, J., Yao, F., 2015. Combination of multi-input remote sensing data for drought monitoring over Southwest China. Int. J. Appl. Earth Obs. Geoinf. 35, 270–283. 

- Hazaymeh, K., Hassan, Q.K., 2017. A remote sensing-based agricultural drought indicator and its implementation over a semi-arid region. Jordan. J. Arid Land. 9 (3), 319–330. 

- Himanshu, S.K., Singh, G., Kharola, N., 2015. Monitoring of drought using satellite data. Int. Res. J. Earth Sci. 3 (1), 66–72. 

- Holben, B.N., 1986. Characteristics of maximum-value composite images from temporal AVHRR data. Int. J. Remote Sens. 7, 1417–1434. 

- Hu, X., Ren, H., Tansey, K., Zheng, Y., Ghent, D., Liu, X., Yan, L., 2019. Agricultural drought monitoring using European Space Agency Sentinel 3A land surface temperature and normalized difference vegetation index imageries. Agr. Forest Meteorol. 279 107707. 

- Huete, A., Didan, K., Miura, T., Rodriguez, E.P., Gao, X., Ferreira, L.G., 2002. Overview of the radiometric and biophysical performance of the MODIS vegetation indices. Remote Sens. Environ. 83 (1–2), 19–213. 

- IPCC, 2013. Climate Change 2013. In: Stocker, T.F., et al. (Eds.), The Physical Science Basis. Cambridge University Press, 1535 pp. 

- IPCC, 2018. Summary for Policymakers. In: Global warming of 1.5�C. An IPCC Special Report on the impacts of global warming of 1.5�C above pre-industrial levels and related global greenhouse gas emission pathways, in the context of strengthening the global response to the threat of climate change, sustainable development, and efforts to eradicate poverty (Eds: Masson-Delmotte, et al.), World Meteorological Organization, Geneva, Switzerland, 32 pp. 

- Jackson, B.B., 1983. Multivariate Data Analysis: An Introduction, Irwin, Homewood, Illinois, USA. 

- Jain, S.K., Keshri, R., Goswami, A., Sarkar, A., Chaudhry, A., 2009. Identification of drought-vulnerable areas using NOAA AVHRR data. Int. J. Remote Sens. 30, 2653–2668. 

- Ji, L., Peters, A.J., 2003. Assessing vegetation response to drought in the northern Great Plains using vegetation and drought indices. Remote Sens. Environ. 87, 85–98. 

- Jo¨nsson, P., Eklundh, L., 2002. Seasonality extraction by function-fitting to time series of satellite sensor data. IEEE Trans. Geosci. Remote Sens. 40 (8), 1824–1832. 

- Karnieli, A., Agam, N., Pinker, R.T., Anderson, M., Imhoff, M.L., Gutman, G.G., Panov, N., Goldberg, A., 2010. Use of NDVI and land surface temperature for drought assessment: merits and limitations. J. Climate. 23, 618–633. 

- Keyantash, J.A., Dracup, J.A., 2004. An aggregate drought index: assessing drought severity based on fluctuations in the hydrologic cycle and surface water storage. Water Resour. Res. 40, W09304. 

- Kogan, F.N., 2001. Operational space technology for global vegetation assessment. Bull. Am. Meteorol. Soc. 82 (9), 1949–1964. 

- Kogan, F.N., 1991. Observations of the 1990 US drought from the NOAA-11 polar orbiting satellite. Drought Netw. News. 3, 7–11. 

- Kogan, F.N., 1995. Application of vegetation index and brightness temperature for drought detection. Adv. Space Res. 11, 91–100. 

- Kogan, F.N., 1997. Global drought watch from space. Bull. Am. Meteorol. Soc. 78, 621–636. 

- Kogan, F.N., Guo, W., Yang, W., 2019. Drought and food security prediction from NOAA new generation of operational satellites. Geomat. Nat. Haz. Risk. 10 (1), 651–666. 

- Kumar, K.N., Rajeevan, M., Pai, D.S., Srivastava, A.K., Preethi, B., 2013. On the observed variability of monsoon droughts over India. Weather Clim. Extrem. 1, 42–50. 

- Liu, Z.P., Wang, Y.Q., Shao, M.G., Jia, X.X., Li, X.L., 2016. Spatiotemporal analysis of multiscalar drought characteristics across the loess plateau of China. J. Hydrol. 534, 281–299. 

- MaChado-MaChado, E.A., Neeti, N., Eastman, J.R., Chen, H., 2011. Implications of space-time orientation for principal components 

   - analysis of earth observation image time series. Earth Sci. Inform. 4 (3), 117–124. 

- Maisongrande, P., Duchemin, B., Dedieu, G., 2004. VEGETATION/ SPOT: an operational mission for the Earth monitoring; presentation of new standard products. Int. J. Remote Sens. 25 (1), 9–14. 

- Martins, D.S., Raziei, T., Paulo, A.A., Pereira, L.S., 2012. Spatial and temporal variability of precipitation and drought in Portugal. Nat. Hazards Earth Syst. Sci. 12 (5), 1493–1501. 

- McKee, T.B., Doesken, N.J., Kleis,t J., 1995. Drought monitoring with multiple time scales. Proceedings of the XIth conference on Applied Climatology. B. Am. Meteorol. Soc., pp. 233–236. 

- McKee, T.B., Doesken, N.J., Kleist, J., 1993. The relationship of drought frequency and duration to time scales. In: Proceedings of the IXth Conference onApplied Climatology. B.Am. Meteorol. Soc., pp. 179–184. 

- Moran, M., Clarke, T., Inoue, Y., Vidal, A., 1994. Estimating crop water deficit using the relation between surface-air temperature and spectral vegetation index. Remote Sens. Environ. 49 (3), 246–263. 

- Muthumanickam, D., Kannan, P., Kumaraperumal, R., Natarajan, S., Sivasamy, R., Poongodi, C., 2011. Drought assessment and monitoring through remote sensing and GIS in western tracts of Tamil Nadu, India. Int. J. Remote Sens. 32 (18), 5157–5176. 

- Nathan, K.K., 1998. Droughts in Tamil Nadu: a qualitative and quantitative appraisal. Drought Netw. News 10 (3), 3–6. 

- Okin, G.S., Dong, C., Willis, K.S., Gillespie, T.W., MacDonald, G.M., 2018. The impact of drought on native Southern California Vegetation: remote sensing analysis using MODIS-derived time series. J. Geophys. Res-Biogeo. 123 (6), 1927–1939. 

- Priya, R.L., Manimannan, G., 2014. Rainfall fluctuation and region wise classification in Tamil Nadu: using geographical information system. IOSR J. M. 10 (5), 5–12. 

- Qian, X., Liang, L., Shen, Q., Sun, Q., Zhang, L., Liu, Z., Zhao, S., Qin, Z., 2016. Drought trends based on the VCI and its correlation with climate factors in the agricultural areas of China from 1982 to 2010. Environ. Monit. Assess. 188 (11), 639–652. 

- Rajsekhar, D., Mishra, A.K., Singh, V.P., 2012. Regionalization of drought characteristics using an entropy approach. J. Hydrol. Eng. 18 (7), 870–887. 

- Reddy, G.P.O., Kumar, N., Sahu, N., Srivastava, R., Singh, S.K., Naidu, L.G.K., Chary, G.R., Biradar, C.M., Gumma, M.K., Reddy, B.S., Kumar, J.N., 2020. Assessment of spatio-temporal vegetation dynamics in tropical arid ecosystem of India using MODIS time-series vegetation indices. Arab. J. Geosci. 13 (15), 1–13. 

- Rencher, A.C., 1998. Multivariate Statistical Inference and Applications. Wiley, New York. 

- Rhee, J., Im, J., Carbone, G.J., 2010. Monitoring agricultural drought for arid and humid regions using multi-sensor remote sensing data. Remote Sens. Environ. 114 (12), 2875–2887. 

- Saha, S. et al., 2011. The NCEP climate forecast system reanalysis. B. Am. Meteorol. Soc. 91 (8), 1015–1058. 

- Saleska, S.R., Didan, K., Huete, A.R., da Rocha, H.R., 2007. Amazon forests green-up during 2005 drought. Science. 318 (5850), 612. 

- Sa´nchez, N., Gonza´lez-Zamora, A<sup>´</sup> ., Martı´nez-Ferna´ndez, J., Piles, M., Pablos, M., 2018. Integrated remote sensing approach to global agricultural drought monitoring. Agr. Forest Meteorol. 259, 141–153. 

- Sandholt, I., Rasmussen, K., Andersen, J., 2002. A simple interpretation of the surface temperature/vegetation index space for assessment of surface moisture status. Remote Sens. Environ. 79, 213–224. 

- Santos, C.A.G., Brasil Neto, R.M., Passos, J.S.A., Silva, R.M., 2017. Drought assessment using a TRMM-derived standardized precipitation index for the upper Sa˜o Francisco River basin, Brazil. Environ. Monit. Assess. 189 (6), 250. 

- SDSN, 2013. Solutions for sustainable agriculture and food systems. In Technical Report for the Post-2015 Development Agenda; Sustainable Development Solutions Network: Paris, France; New York, NY, USA. 

- Selvaraj, K.N., 2009. Risk management strategies for drought-prone rice cultivation: a case study of Tamil Nadu, India. Asian. J. Agric. Dev. 6 (2), 1–29. 

314 

K.C. Arun Kumar et al. 

Advances in Space Research 67 (2021) 298–315 

- Sepulcre-Canto, G., Horion, S., Singleton, A., Carrao, H., Vogt, J., 2012. Development of a combined drought indicator to detect agricultural drought in Europe. Nat. Hazards Earth Syst. Sci. 12 (11), 3519–3531. 

- Son, N.T., Chen, C.F., Chen, C.R., Chang, L.Y., Minh, V.Q., 2012. Monitoring agricultural drought in the Lower Mekong Basin using MODIS NDVI and land surface temperature data. Int. J. Appl. Earth Obs. Geoinf. 18, 417–427. 

- Storch, H.V., Zwiers, F.W., 1999. Statistical Analysis in Climate Research. Cambridge University Press, Cambridge, UK. 

- Tang, Z., Ma, J., Peng, H., Wang, S., Wei, J., 2017. Spatiotemporal changes of vegetation and their responses to temperature and precipitation in upper Shiyang river basin. Adv. Space. Res. 60 (5), 969–979. 

- Tucker, C.J., 1979. Red and photographic infrared linear combinations for monitoring vegetation. Remote Sens. Environ. 8 (2), 127–150. 

- Tucker, C.J., Slayback, D.A., Pinzon, J.E., Los, S.O., Myneni, R.B., Taylor, M.G., 2001. Higher northern latitude normalized difference vegetation index and growing season trends from 1982 to 1999. Int. J. Biometeorol. 45 (4), 184–190. 

- Udmale, P., Ichikawa, Y., Manandhar, S., Ishidaira, H., Kiem, A.S., 2014. Farmer’s perception of drought impacts, local adaptation and administrative mitigation measures in Maharashtra State, India. Int. J. Disaster Risk Reduct. 10, 250–269. 

- Vyas, S.S., Bhattacharya, B.K., 2020. Agricultural drought early warning from geostationary meteorological satellites: concept and demonstration over semi-arid tract in India. Environ. Monit. Assess. 192, 311. 

- Wan, Z., Wang, P., Li, X., 2004. Using MODIS land surface temperature and normalized difference vegetation index products for monitoring drought in the southern Great Plains, USA. Int. J. Remote Sens. 25 (1), 61–72. 

- Wang, L., Qu, J.J., 2007. NMDI: A normalized multi-band drought index for monitoring soil and vegetation moisture with satellite remote sensing. Geophys. Res. Lett. 34 (20). 

- Wold, S., Esbensen, K., Geladi, P., 1987. Principal component analysis. Chemom. Intell. Lab. Syst. 2 (1–3), 37–52. 

- Wu, J., Zhou, L., Mo, X., Zhou, H., Zhang, J., Jia, R., 2015. Drought monitoring and analysis in China based on the Integrated Surface Drought Index (ISDI). Int. J. Appl. Earth Obs. Geoinf. 41, 23–33. 

- Xiao, X., Boles, S., Liu, J., Zhuang, D., Liu, M., 2002. Characterization of forest types in North eastern China, using multi-temporal SPOT-4 VEGETATION sensor data. Remote Sens. Environ. 82 (2–3), 335– 348. 

- Xue, J., Su, B., 2017. Significant remote sensing vegetation indices: A review of developments and applications. J. Sens., 1–17 

- Zabiri, H., Diep, T., Thao, T., 2007. A Principal component approach in diagnosing poor control loop performance. In: Proceedings of the world congress on engineering and computer science 2007, October 2426, 2007, San Francisco, USA. 

- Zambrano, F., Lillo-Saavedra, M., Verbist, K., Lagos, O., 2016. Sixteen years of agricultural drought assessment of the Bio-Bı´o Region in Chile using a 250 m resolution vegetation condition index (VCI). Remote Sens. 8 (6), 530. 

- Zhang, L., Xiao, J., Zhou, Y., Zheng, Y., Li, J., Xiao, H., 2016. Drought events and their effects on vegetation productivity in China. Ecosphere. 7 (12) e01591. 

- Zhang, Q., Kong, D., Singh, V.P., Shi, P., 2017. Response of vegetation to different time scales drought across China: spatiotemporal patterns, causes and implications. Glob. Planet. Chang. 152, 1–11. 

- Zrinji, Z., Burn, D.H., 1994. Flood frequency-analysis for ungauged sites using a region of influence approach. J. Hydrol. 153 (1–4), 1–21. 

315 

