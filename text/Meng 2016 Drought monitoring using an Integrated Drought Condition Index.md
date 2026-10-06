Nat Hazards (2016) 80:1135–1152 DOI 10.1007/s11069-015-2014-1 

<mark>ORIGINAL PAPER</mark> 



# Drought monitoring using an Integrated Drought Condition Index (IDCI) derived from multi-sensor remote sensing data 

Lingkui Meng<sup>1•</sup> Ting Dong<sup>1•</sup> Wen Zhang<sup>1</sup> 

Received: 14 January 2015 / Accepted: 10 October 2015 / Published online: 22 October 2015 � Springer Science+Business Media Dordrecht 2015 

Abstract Drought is a complex natural phenomenon. To effectively characterize the spatial extent and intensity of the phenomenon, multiple drought-related factors, such as precipitation, vegetation growth condition, and land surface temperature, should be considered comprehensively. However, the capability of each of these factors in drought monitoring varies with seasonal time. Thus, in formulating a drought index, different weights should be assigned to these factors at different time periods. This study proposes a novel remote sensing index, the Integrated Drought Condition Index (IDCI), for short-term drought monitoring. The index sets different weights for each month of the growing season into three components, i.e., precipitation, vegetation growth condition, and land surface temperature, based on the principle component analysis. To assess IDCI performance, the spatial drought conditions of the IDCI maps during the growing season in a typical dry year and individual month of August from 2003 to 2012 were compared with in situ drought indices in Northern China. Correlation analyses were performed between the IDCI and different timescale Standardized Precipitation Evapotranspiration Index values, and the year-to-year IDCI variations were compared with in situ drought indices. The results of the comparison and correlation analysis confirmed the effectiveness of IDCI in characterizing drought conditions and patterns. 

Keywords Drought � MODIS � TRMM precipitation � Principle component analysis � SPEI � Drought index � Drought index weighting 

> & Ting Dong dongt@whu.edu.cn Lingkui Meng lkmeng@whu.edu.cn 

> 1 School of Remote Sensing and Information Engineering, Wuhan University, 129 Luoyu Road, Wuhan 430079, China 

123 

Nat Hazards (2016) 80:1135–1152 

1136 

## 1 Introduction 

Drought is a complex natural hazard. A result of climatic fluctuations and variations, drought triggers negative economic, social, and environmental impacts (Tadesse et al. 2004). In 1995, the Federal Emergency Management Agency (FEMA) estimated that drought affected more people than any other weather-related disasters and the average annual damage in the USA has been estimated to be worth 6–8 billion dollars (FEMA 1995). Drought occurs frequently in China, resulting in considerable impacts and economic losses. The droughts in China have affected an average of 21 million ha annually over the last 50 years, or approximately 20 % of the total cropland area (Jiang et al. 2013). The State Flood Control and Drought Relief Headquarters (SFCDRH) and the Ministry of Water Resources of the Government of the People’s Republic of China have reported that droughts were responsible for direct economic losses amounting to RMB 120.6 billion in 2009 (SFCDRH 2011). 

Droughts are often classified into four general types: meteorological or climatological, agricultural, hydrological, and socioeconomic (American Meteorological Society 2013). Meteorological or climatological drought is an abnormal phenomenon of water shortages caused by precipitation deficit, which normally triggers the other three drought types (Zhang and Jia 2013). Recent observations have shown that climate change brought about by global warming causes the intensification and increased frequency of droughts, which result in escalated impacts (Dai 2011, 2013; Kogan et al. 2013). Therefore, a comprehensive study on drought monitoring and prediction is important to provide policymakers with accurate and timely information needed for early warning and mitigation. 

Drought monitoring worldwide has significantly progressed through various drought indices, such as the Palmer Drought Severity Index (PDSI) (Palmer 1965), Standardized Precipitation Index (SPI) (McKee et al. 1993), Standardized Precipitation Evapotranspiration Index (SPEI) (Vicente-Serrano et al. 2010a), and percentage of precipitation anomalies (Pa) (AQSIQ and SAC 2006; Zhou et al. 2012). These indices are typically calculated using station-based climate and meteorological data. The PDSI is established according to a simplified water balance model that considers long-term historical precipitation, mean temperature data, and the available water content information of soil. The calculation of the SPI is based on statistical probability derived from precipitation data. The main characteristic of the SPI is the flexibility in precipitation anomaly quantification for a specific time period (e.g., 1, 3, 6, 9, or 12 months) according to the long-term precipitation record for specific drought types (Guttman 1998, 1999). Mathematically, SPI values are based only on precipitation data, and it does not consider other variables that can influence droughts. The SPEI is an improved drought index, and it is based on both precipitation and potential evapotranspiration (PET) data. The procedure for calculating the SPEI is similar to that for the SPI, but SPEI considers the role of temperature and uses the difference between precipitation and PET as the input data (Begueria et al. 2014; Stagge et al. 2015; Vicente-Serrano et al. 2010a, b). The SPEI has been widely used in diverse studies because it has great promise as a drought index (Li et al. 2013; Sohn et al. 2013; Wang et al. 2015; Yu et al. 2014). SPEI considers the effect of reference evapotranspiration on drought severity and retains the simplicity multi-scalar nature of the SPI which allows for the identification of different drought types. The Pa is another simple indicator that measures precipitation anomaly compared with historical average for a specific period (Zhou et al. 2012). 

123 

Nat Hazards (2016) 80:1135–1152 

1137 

The use of station-based indices in the quantitative characterization of drought conditions around meteorological stations in different regions is advantageous. However, in areas with sparse weather stations or in places where available precipitation data are inconclusive, the spatial drought conditions may be estimated using spatial interpolation techniques (Rhee et al. 2010). As a result, detailed characterization and monitoring of the spatial pattern of drought conditions using traditional station-based tools depend on the density and spatial distribution of the stations. This situation highlights the capability of satellite-based remote sensing to quickly obtain a wide range of spatial details and evaluate the relevant information of the drought condition with continuous and accurate data that timely and spatial across large-scale areas (Keshavarz et al. 2014; Malingreau 1986; Son et al. 2012). 

The Moderate Resolution Imaging Spectroradiometer (MODIS) data are widely applied in establishing remote sensing drought index, owing to the rich spectral information (Caccamo et al. 2011; Gu et al. 2007; Park et al. 2004; Shahabfar et al. 2012; Son et al. 2012). The Normalized Difference Vegetation Index (NDVI) (Rouse et al. 1974) is widely used in estimating vegetation growth conditions and monitoring drought conditions (Boschetti et al. 2013; Carlson and Ripley 1997; Chen et al. 2004; Hmimina et al. 2013; Kogan 1990; Peters et al. 2002; Tadesse et al. 2005; Xiong et al. 2010). The NDVI fully utilizes the reflective and absorptive characteristics of plants in the near-infrared (NIR) and red channels of the electromagnetic spectrum, which can be obtained as (NIR - RED)/ (NIR ? RED). Kogan (1995) computed the Vegetation Condition Index (VCI) by linearly scaling the NDVI values from 0 to 1 for each pixel according to the absolute maximum and minimum values of the same period in the entire record. Compared with the NDVI, the VCI can measure the impact of weather on vegetation better (Gebrehiwot et al. 2011; Liu and Kogan 1996; Rhee et al. 2010). Surface temperature is also affected by drought, and as such, the Temperature Condition Index (TCI) was developed based on land surface temperature (LST). TCI is widely used in drought monitoring (Bayarjargal et al. 2006; Bhuiyan et al. 2006; Du et al. 2012; Ezzine et al. 2014; Kogan et al. 2012; Seiler et al. 2000). In addition, microwave remote sensing can be utilized in drought monitoring because this method works in all-weather working conditions (Du et al. 2012; Rhee et al. 2010). The Tropical Rainfall Measuring Mission (TRMM) was designed to measure precipitation at a 0.25� 9 0.25� resolution from space using various sensors, such as the highresolution radar, visible-infrared radiometer, and passive microwave radiometer. The precipitation products are widely used to monitor drought conditions effectively (Du et al. 2012; Ezzine et al. 2014; Feng et al. 2012; Keshavarz et al. 2014; Rhee et al. 2010; Zhang and Jia 2013). 

Considering the complexity of drought, multiple sources of drought-related factors such as precipitation, vegetation growth condition, and land surface temperature should be integrated to characterize the spatial extent and intensity of drought. Moreover, these factors share correlated information. All these aforementioned points render the principal component analysis (PCA) as capable of providing unique advantages in establishing a remote sensing drought index that considers precipitation, vegetation, and land surface temperature (Du et al. 2012). PCA is an orthogonal linear transformation that converts a set of observations of possibly correlated variables into a new coordinate system that can be represented without correlation (Baert et al. 2012; Lasaponara 2006; Liu et al. 2014; Vicente-Serrano et al. 2004; Xia et al. 2014). PCA is widely used in analyzing spatial drought patterns (Bonaccorso et al. 2003; Raziei et al. 2008; Santos et al. 2010; VicenteSerrano 2006). 

123 

Nat Hazards (2016) 80:1135–1152 

1138 

The capability of each of these drought-related factors including precipitation, vegetation, and land surface temperature in drought monitoring varies along seasonal time. Vegetation shows different sensitivities to water stress during different phenological phases. Thus, appropriate weights should be assigned to these factors in principal component analysis at different time periods. Based on the PCA method, this study aims to establish a new remote sensing index named Integrated Drought Condition Index (IDCI), which considers precipitation, vegetation growth condition, and land surface temperature comprehensively. In this index, these factors are weighed differently for each month of the growing season. 

## 2 Study area and data 

### 2.1 Study area 

The study area is situated in Northern China with a latitude of 33�54<sup>0</sup> –46�43<sup>0</sup> N and longitude of 107�54<sup>0</sup> –131�41<sup>0</sup> E (Fig. 1). The total area is 163.69 9 10<sup>4</sup> km<sup>2</sup> and covers 14 provinces, including Hebei, Shandong, Shanxi, and Liaoning. The major land cover categories of the region are grasslands, croplands, and mixed forest according to the 2012 MODIS land cover classifications data (MCD12Q1). In addition, this region is mainly located in the arid/semiarid area of the mid-temperate zone and in the humid/sub-humid area of the warm temperate zone based on the Chinese eco-geographical zoning map (Zheng and Li 2008). The East Asian monsoon climate produces uneven precipitation spatial distribution. Northern China suffers from frequent climate-related disasters, such as droughts and floods. 

### 2.2 Data 

### 2.2.1 In situ meteorological data 

The monthly precipitation and mean temperature data from 1961 to 2012 of all the available stations were acquired from China Meteorological Data Sharing Service System 



Fig. 1 Study area and the distribution of the meteorological stations 

123 

Nat Hazards (2016) 80:1135–1152 

1139 

(http://cdc.cma.gov.cn/). The meteorological data records were inspected rigorously. Only those meteorological stations with available long-term data from 1961 to 2012 were included. A total of 135 meteorological stations in the study area were selected (Fig. 1). The monthly precipitation and mean temperature for all the meteorological stations within each province were averaged to represent the regional drought condition. 

The Standardized Precipitation Evapotranspiration Index (SPEI) developed by VicenteSerrano et al. (2010a) can be flexibly designed to measure drought severity for a specific time period based on the long-term precipitation and PET record. In this study, PET was calculated based on the Thornthwaite equation (Thornthwaite 1948) which considers only monthly mean temperature data. Different timescales are useful for monitoring different drought types. Short SPEI timescales are mainly appropriate for analyzing soil water content and river discharge in headwater areas, while long SPEI timescales are related to variations in groundwater storage (Vicente-Serrano et al. 2010a). Given that the major interest of this study is short-term drought, the multi-scale SPEIs (1, 3, and 6 months) of 135 weather stations were calculated using the long-term monthly precipitation and mean temperature data from 1961 to 2012. 

The percentage of precipitation anomalies (Pa) is a simple indicator in measuring precipitation anomalies compared with the historical average for a specific period (Zhou et al. 2012). In this study, we calculated the Pa using the monthly precipitation data for the weather stations throughout the study area. 

### 2.2.2 Remote sensing data 

The Terra MODIS 8-day average value of composited LST products with 1 km resolution (MOD11A2, collection v005) from 2003 to 2012 and the monthly maximum value composited (MVC) MODIS NDVI time series products with 1 km resolution (MOD13A3, collection v005) from 2003 to 2012 in four tiles (h26v04, h26v05, h27v04, and h27v05) that covered the study area were obtained from the National Aeronautics and Space Administration (NASA) Land Processes Distributed Active Archive Center. The original NDVI and LST images were spliced and their projection system was converted from sinusoidal to an Albers conical equal area projection using the MODIS reprojection tool developed by NASA. 

The remotely sensed precipitation data used in this study were derived from the TRMM satellite that was launched in November 1997. The TRMM 3B43 dataset from 2003 to 2012 was obtained from the NASA Data and Information Services Center (http://mirador. gsfc.nasa.gov/). This dataset was presented as a monthly precipitation rate (mm/h) in a 0.25� 9 0.25� spatial resolution and covered the 50� south to 50� north global latitude band. To explore the optimal integrated drought index, accumulated 3- and 6-month TRMM data were calculated and the 1-, 3-, and 6-month TRMM data were tested, respectively, in the subsequent experiment. 

## 3 Methodology 

### 3.1 Remote sensing data processing 

The NDVI and LST datasets were MODIS monthly MVC and 8-day average value products, respectively. However, noises still existed because of cloud contamination and 

123 

Nat Hazards (2016) 80:1135–1152 

1140 

atmospheric variability. These cloud-contaminated pixels in the LST and NDVI products were masked out based on the quality control documents. Furthermore, to maintain a temporal resolution that is the same as that of the NDVI dataset, the 8-day LST was composited to monthly LST by calculating the average value weighting with the number of days belonging to each month after masking the fill and missing values (Rhee et al. 2010). 

All the remote sensing variable values, including the NDVI, LST, and 1- to 6-month accumulated TRMM precipitation data, were linearly scaled from 0 to 1 for each pixel based on the absolute maximum and minimum values of the same month in the entire record (2003–2012) to discriminate the weather and ecosystem components. The process adhered to that performed by Kogan (1995) for the VCI using the NDVI. Moreover, the scaled value was changed from 0 to 1 to correspond to the driest and wettest conditions. In addition, the scaled TRMM precipitation data were resampled to 1 km resolution using a bilinear interpolation method to ensure that spatial resolution is consistent with that of MODIS data. The formulas for each remote sensing drought indices are given in Table 1. 

### 3.2 Remote sensing drought-related factors and the principal component analysis method 

Since the relationship between different remotely sensed drought indices and SPEI varies over time, Pearson’s correlation analyses were performed on the remote sensing drought indices of each month from May to September and SPEI of different timescales from 2003 to 2012. These analyses were conducted to assess the capability of these drought-related factors in drought monitoring and further determine the appropriate weights. The remotely sensed index values at the weather station were extracted using the 3 km 9 3 km window method. The information from the 3 km 9 3 km pixel window that centered on each weather station location was extracted, and the average value of all pixels in the extraction window was calculated to represent the index value of the site location. 

The PCA method, a powerful tool for data analysis, was used to obtain the integrated information from the TCI, VCI, and scaled TRMM. The capability of different indices in monitoring drought showed considerable variations along seasonal time; thus, we weighted these indices differently over different time periods while performing PCA. The integrated drought condition indices with different weights were tested through Pearson’s correlation analyses. 

### 3.3 Evaluation of IDCI drought monitoring behavior using in situ drought observations 

An IDCI dataset that contains optimal weights during the growing season (May to September) from 2003 to 2012 was created based on the PCA method. The spatial changes in the IDCI maps were compared with the changes in the in situ drought indices in a typical 

Table 1 Remote sensing drought index formulas 

|Drought index|Formula|
|---|---|
|Scaled LST (modified TCI)|(LSTmax - LST)/(LSTmax - LSTmin)|
|Scaled NDVI (VCI)|(NDVI - NDVImin)/(NDVImax - NDVImin)|
|Scaled TRMM|(TRMM - TRMMmin)/(TRMMmax - TRMMmin)|



The scaled TRMM uses one of the 1-, 3-, and 6-month timescales 

123 

Nat Hazards (2016) 80:1135–1152 

1141 

dry year and individual month of August from 2003 to 2012 to assess the IDCI performance in monitoring short-term drought conditions. The spatial distributions of the areas that experienced drought were compared. 

Pearson’s correlation analyses were performed between the IDCI values and the 1-, 3-, and 6-month SPEI values during the growing season from 2003 to 2012. Additionally, regression analyses were performed between the IDCI and the in situ reference data from 2003 to 2012 to further evaluate the capability of regional drought condition monitoring. Analyses were performed in nine main provinces of the study area. Furthermore, the yearly IDCI variations were compared with the yearly variations in the in situ drought indices to evaluate the temporal drought monitoring capability of this index. The IDCI values from 2003 to 2012 at the weather stations were the average value of all pixels in the 3 km 9 3 km window which centered on the in situ site location. 

## 4 Results and discussion 

### 4.1 Correlations between drought-related factors and SPEIs 

The monthly correlation coefficients were calculated between the remotely sensed drought indices (TCI, VCI, and scaled TRMM) and the 1-, 3-, and 6-month SPEI (SPEIs) from 2003 to 2012 (Fig. 2). The correlation coefficient values varied among the different timescales and were statistically significant at the 0.01 significance level except for the VCI versus SPEI-1 in May and September (Fig. 2a). Notably, the scaled TRMM with various timescales showed high correlation coefficient values with the in situ drought index, followed by the TCI and VCI (Fig. 2). Overall, the scaled TRMM mostly produced the highest correlation coefficient values with in situ variables with the same timescales as that of the scaled TRMM. For example, the scaled TRMM1 (1-month TRMM data used) was best correlated with SPEI-1 (Fig. 2a), the scaled TRMM6 (6-month TRMM data used) was best correlated with SPEI-6 (Fig. 2c), and the scaled TRMM3 (3-month TRMM data used) was best correlated with SPEI-3 except in May (Fig. 2b). 

In addition, compared with that of the scaled TRMM and TCI, the correlations between the VCI and the SPEIs varied significantly among the different SPEI timescales and over the different time periods. The VCI appeared less sensitive to SPEI-1 than to SPEI-3 or SPEI-6 (Fig. 2a) because there is a time lag existed between the precipitation occurrence and the vegetation condition response. The VCI showed the highest correlation with the SPEIs in July because of the vegetation phenological phase in the study area (Fig. 2). 



Fig. 2 Correlations between the remote sensing drought indices and the in situ different timescales SPEI from May to September. The p value \0.01 except for columns with an asterisk (*). The descriptions of the drought indices are given in Table 1. SPEI-1, 1-month SPEI; SPEI-3, 3-month SPEI; SPEI-6, 6-month SPEI 

123 

Nat Hazards (2016) 80:1135–1152 

1142 

Table 2 Correlation coefficient r values between the integrated drought condition indices with different weights and the in situ different timescales SPEI from May to September 

|Index<br>Month|Weight|||r|||
|---|---|---|---|---|---|---|
||Scaled<br>TRMM<br>(a)|TCI (b)|VCI (c)|SPEI-1<br>(TRMM1<br>used)|SPEI-3<br>(TRMM3<br>used)|SPEI-6<br>(TRMM6<br>used)|
|IDCI<br>a. May (n = 1120)|1|1|1|0.14|0.25|0.25|
||2|0|1|0.20|0.27|0.26|
||2|1|0|0.64|0.59|0.62|
||3|1|1|0.30|0.30|0.28|
||4|0|1|0.45|0.33|0.29|
||4|1|0|0.64|0.59|0.63|
||4|3|1|0.45|0.33|0.29|
||5|3|2|0.25|0.29|0.27|
|b. June (n = 1168)|1|1|1|0.28|0.24|0.28|
||2|0|1|0.41|0.30|0.30|
||2|1|0|0.56|0.60|0.65|
||3|2|0|0.57|0.60|0.65|
||3|2|2|0.37|0.27|0.29|
||4|1|0|0.57|0.59|0.64|
||4|3|1|0.57|0.45|0.43|
||5|2|1|0.57|0.48|0.47|
|c. July (n = 1172)|1|1|1|0.55|0.44|0.42|
||2|1|1|0.64|0.52|0.53|
||3|1|2|0.61|0.47|0.49|
||3|2|2|0.61|0.48|0.49|
||4|1|3|0.59|0.47|0.47|
||4|3|1|0.64|0.57|0.61|
||5|1|2|0.64|0.55|0.56|
||5|2|1|0.64|0.57|0.62|
|d. August (n = 1230)|1|1|1|0.66|0.51|0.49|
||2|1|1|0.75|0.61|0.62|
||3|0|2|0.74|0.58|0.58|
||3|2|2|0.74|0.59|0.58|
||4|0|3|0.73|0.58|0.55|
||4|1|1|0.75|0.62|0.65|
||4|1|3|0.73|0.58|0.55|
||5|3|2|0.75|0.62|0.64|
|e. September (n = 1201)|1|1|1|0.53|0.47|0.52|
||2|0|1|0.60|0.68|0.64|
||2|1|1|0.60|0.68|0.63|
||3|0|2|0.58|0.64|0.62|
||3|1|2|0.58|0.64|0.61|
||4|0|1|0.67|0.68|0.64|



123 

Nat Hazards (2016) 80:1135–1152 

1143 

Table 2 continued 

|Index|Month|Weight|||r|||
|---|---|---|---|---|---|---|---|
|||Scaled<br>TRMM<br>(a)|TCI (b)|VCI (c)|SPEI-1<br>(TRMM1<br>used)|SPEI-3<br>(TRMM3<br>used)|SPEI-6<br>(TRMM6<br>used)|
|||4|1|3|0.57|0.63|0.60|
|||5|1|2|0.65|0.68|0.64|



In all the cases, the p value\0.01. The highest r values for each column at different time periods are shown in bold. The descriptions of the drought indices are presented in Table 1. SPEI-1, 1-month SPEI; SPEI-3, 3-month SPEI; SPEI-6, 6-month SPEI 



Fig. 3 Seasonal changes in drought detected by IDCI (using TRMM6) and SPEI-6 from May to September in 2009. SPEI-6, 6-month SPEI 

Additionally, compared with the VCI, the TCI demonstrated more correlation with both 3- and 6-month SPEI from May to June. This result indicates that the TCI can provide valuable drought information during that time period (Fig. 2b, c). 

Generally, the scaled TRMM showed a higher correlation with the in situ drought indices than the TCI and VCI, and the capability of the TCI and VCI in drought monitoring highly differed over different time periods. Therefore, appropriate weights were assigned to these indices in the PCA at different time periods. The original spectral feature space in the PCA procedure was composed of the scaled TRMM, TCI, and VCI, as shown in the following: 



where a, b, and c show the number of occurrences of these three indices in the original feature matrix and represent the weights of these three indices, respectively. The scaled TRMM used one of the 1-, 3-, and 6-month timescales. The covariance matrix and the 

123 

Nat Hazards (2016) 80:1135–1152 

1144 



Fig. 4 Seasonal variations of precipitation, mean temperature, and the percentage of precipitation anomalies (Pa) in nine provinces from May to September in 2009 

eigenvalues and eigenvectors of the covariance matrix were calculated. Subsequently, a series of new principal components was computed by multiplying the eigenvector of the covariance matrix for the original feature matrix. The Integrated Drought Condition Index was defined as the first principal component, by considering that the first principal component contained the most number of information from the original spectral feature space. 

To select the optimal IDCI weight over different time periods, Pearson’s correlation analyses were performed between the integrated drought condition indices and the 1-, 3-, and 6-month SPEI values for each month of the growing season (Table 2). All the correlations were statistically significant at the 0.01 significance level. The r values generally decreased as the VCI weight increased in May and June (Table 2a, b). By contrast, the integrated drought condition indices with larger VCI weight yielded higher r values with the in situ drought indices from July to September than that in May and June (Table 2c–e). Moreover, during the entire growing season, the integrated drought condition indices with appropriate weights were better correlated with the in situ variables than the indices with equal weights of 1, 1, and 1 for the scaled TRMM, TCI, and VCI, respectively (Table 2). Based on the relatively higher correlations between the IDCI with in situ drought indices over different time periods, the May to September optimal weights (a, b, c) for the scaled TRMM, TCI, and VCI of the IDCI were (4, 1, 0), (3, 2, 0), (5, 2, 1), (4, 1, 1), and (4, 0, 1), respectively (Table 2). Finally, an IDCI dataset with different weights was obtained during 

123 

Nat Hazards (2016) 80:1135–1152 

1145 



Fig. 5 Year-to-year maps of IDCI (using TRMM6) and SPEI-6 for August from 2003 to 2012. SPEI-6, 6-month SPEI 

the growing season (May to September) from 2003 to 2012. The appropriate weights for these factors can be adjusted flexibly for studies that involve areas with different biophysical characteristics depending on the ability of these factors in drought monitoring. 

### 4.2 Drought conditions monitored by IDCI 

The spatial distributions of IDCI (using TRMM6) from May to September 2009 (Fig. 3) and for August 2003–2012 (Fig. 5) were illustrated and compared with the 6-month SPEI to demonstrate its temporal and spatial effectiveness in drought assessment and monitoring in Northern China. To compare the IDCI map information with the in situ drought indices, the temporal distribution of the precipitation and mean temperature data for the nine main provinces were also obtained (Figs. 4, 6). 

Although local discrepancies between SPEI-6 and IDCI values were found, the two variables basically showed a similar spatial pattern. Based on the IDCI maps, the drought 

123 

Nat Hazards (2016) 80:1135–1152 

1146 



Fig. 6 Annual variation of the precipitation and mean temperature data in nine provinces for August from 2003 to 2012. SPEI-6, 6-month SPEI 

in Northeast part (Jilin and Liaoning) developed heavily from July to September 2009 (Fig. 3c–e). These situations are evidenced by the SPEI-6 values in those regions, which tend to be lower (Fig. 3c–e), indicating that precipitation deficiency and high temperature were affecting those areas (Fig. 4b, e). In June 2009, IDCI showed more severe drought conditions in northern Shaanxi because the average precipitation of the region was only 6.9 mm and the Pa value was -86 % (Figs. 3b, 4h). SPEI-6 showed a similar trend with lower values (Fig. 3b). Inner Mongolia was affected by serious drought conditions (Fig. 5c, g, i), because of the precipitation declining and high temperature in August of 2005, 2009, and 2011(Fig. 6g). SPEI-6 values in the corresponding time were low, which showed agreement with the IDCI pattern (Fig. 5c, g, i). Moreover, the SPEI-6 showed more severe conditions in Jilin in August 2004 as well as in northern Henan and Shandong in August 2012. The same severity and extent of the droughts were also detected through the IDCI maps (Figs. 5b, j). 

### 4.3 Correlation analysis and year-to-year comparisons 

The IDCI values were compared with the 1-, 3-, and 6-month SPEI values for each month of the growing season from 2003 to 2012 (Table 3). The results showed that the IDCI and SPEIs were highly correlated during the growing season, and all the correlations were statistically significant (p \ 0.005). The IDCI values for the nine main provinces (Heilongjiang, Jilin, Hebei, Shanxi, Liaoning, Shandong, Inner Mongolia, Shaanxi, and Henan) were also tested. The scatter plots between the monthly IDCI (using TRMM6) and the SPEI-6 for each province with weather stations are presented in Fig. 7. The IDCI agreed 

123 

Nat Hazards (2016) 80:1135–1152 

1147 

||SPEI-6|0.75|0.61|0.82|0.50|0.76|0.37|0.61|0.75|0.65|0.76||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|ber|SPEI-3|0.75|0.63|0.78|0.53|0.75|0.54|0.77|0.81|0.75|0.67||
|Septem|SPEI-1|0.72|0.63|0.85|0.74|0.79|0.79|0.61|0.69|0.74|0.69||
||SPEI-6|0.68|0.58|0.84|0.54|0.70|0.39|0.56|0.81|0.57|0.74||
||SPEI-3|0.65|0.60|0.79|0.46|0.70|0.40|0.62|0.81|0.59|0.69||
|August|SPEI-1|0.76|0.77|0.71|0.72|0.83|0.63|0.82|0.84|0.73|0.81||
||SPEI-6|0.68|0.66|0.83|0.60|0.56|0.41|0.61|0.78|0.60|0.77|nth SPEI|
||SPEI-3|0.59|0.60|0.79|0.56|0.60|0.40|0.47|0.70|0.57|0.79|EI-6, 6-mo|
|July|SPEI-1|0.65|0.69|0.69|0.62|0.60|0.69|0.60|0.86|0.68|0.63|SPEI; SP|
||SPEI-6|0.74|0.72|0.85|0.68|0.68|0.49|0.70|0.46|0.54|0.82|3, 3-month|
||SPEI-3|0.61|0.66|0.83|0.67|0.65|0.39|0.65|0.40|0.55|0.81|PEI; SPEI-|
|June|SPEI-1|0.57|0.55|0.75|0.65|0.71|0.56|0.78|0.43|0.63|0.79|-month S|
||SPEI-6|0.90|0.82|0.84|0.49|0.66|0.55|0.65|0.74|0.63|0.53|SPEI-1, 1|
||SPEI-3|0.82|0.76|0.82|0.55|0.68|0.51|0.63|0.70|0.48|0.56|ue\0.005.|
|May|SPEI-1|0.75|0.73|0.76|0.76|0.60|0.68|0.75|0.67|0.55|0.77|the p val|
|Year||2003|2004|2005|2006|2007|2008|2009|2010|2011|2012|he cases,|
|Index|r|IDCI||||||||||In all t|



123 

Nat Hazards (2016) 80:1135–1152 

1148 



Fig. 7 Scatter plots and correlation coefficient r values between the IDCI (using TRMM6) and SPEI-6 in nine provinces. SPEI-6, 6-month SPEI 

well with the SPEI-6 in different provinces during the growing season (Fig. 7), and all the correlations passed the p value \0.005 significance test. 

The yearly IDCI changes (using TRMM-6) in 18 representative meteorological sites were compared with that of the SPEI-6 for August (Fig. 8). These 18 representative meteorological sites, which are evenly distributed, can represent the three main land cover types (grasslands, croplands, and mixed forest) in the study region. There are some discrepancies between the IDCI and the SPEI-6. For example, the SPEI-6 slightly decreased from 2009 to 2010, whereas the IDCI increased in Yan’an (Fig. 8h). The SPEI-6 increased from 2007 to 2008 in Yiyuan, whereas the change in the IDCI had the opposite result (Fig. 8r). In most cases, the IDCI exhibited consistent variations with the in situ reference data at the regional scales, indicating that IDCI can be used to characterize drought conditions and patterns effectively. 

## 5 Conclusion 

This study established a new remote sensing index named Integrated Drought Condition Index (IDCI) using the PCA method. This synthesized drought index was found to be capable of integrating precipitation, vegetation growth condition, and land surface temperature with the monthly optimal weight during the growing season. 

123 

Nat Hazards (2016) 80:1135–1152 

1149 



Fig. 8 Year-to-year changes in the IDCI (using TRMM6) and SPEI-6 in August from 2003 to 2012. SPEI6, 6-month SPEI 

The regional drought monitoring capability of the IDCI was validated by comparing the seasonal changes and inter-annual variations in the IDCI maps and in the in situ reference data. The IDCI was found to be effective in characterizing drought conditions and patterns. The IDCI exhibited high correlations with the in situ SPEIs. The yearly IDCI variations agreed well with the in situ reference data variations. However, the efficiency of IDCI may 

123 

1150 

Nat Hazards (2016) 80:1135–1152 

be improved by taking into consideration the soil moisture factor because it is an important indicator of drought events. Therefore, in future research, the soil moisture data will become a component of the Integrated Drought Condition Index to provide more detailed drought condition information. 

Acknowledgments This work was funded by the National Key Technology Research and Development Program of the Ministry of Science and Technology of China (No. 2011BAH12B06-02) and the Scientific Research in the Public Interest of the Ministry of Water Resources of China (No. 201001046). The authors are thankful to the China Meteorological Data Sharing Service System for the provision of meteorological data. Thanks to Land Processes Distributed Active Archive Center for providing the MODIS satellite images and the NASA Data and Information Services Center for providing the TRMM satellite images. Moreover, the authors express gratitude to Beguerıa and Vicente-Serrano for providing the SPEI R Package, which is available at http://sac.csic.es/spei. We are grateful to the anonymous reviewers for their valuable comments and suggestions. 

## References 

American Meteorological Society (2013) An information statement of the American meteorological society on drought. https://www.ametsoc.org/policy/2013drought_amsstatement.html 

- AQSIQ (General Administration of Quality Supervision, Inspection and Quarantine of the People’s Republic of China), SAC (Standardization Administration of the People’s Republic of China) (2006) Classification of meteorological drought. In: Qiang Z, Xukai Z, Fengjin X (eds) State standardization of the People’s Republic of China, China Standards Publishing House, Beijing 

Baert A, Villez K, Steppe K (2012) Functional unfold principal component analysis for automatic plantbased stress detection in grapevine. Funct Plant Biol 39(6):519–530 

Bayarjargal Y, Karnieli A, Bayasgalan M, Khudulmur S, Gandush C, Tucker CJ (2006) A comparative study 

- of NOAA-AVHRR derived drought indices using change vector analysis. Remote Sens Environ 105(1):9–22 

Begueria S, Vicente-Serrano SM, Reig F, Latorre B (2014) Standardized precipitation evapotranspiration index (SPEI) revisited: parameter fitting, evapotranspiration models, tools, datasets and drought monitoring. Int J Climatol 34(10):3001–3023 

Bhuiyan C, Singh RP, Kogan FN (2006) Monitoring drought dynamics in the Aravalli region (India) using different indices based on ground and remote sensing data. Int J Appl Earth Obs Geoinf 8(4):289–302 Bonaccorso B, Bordi I, Cancelliere A, Rossi G, Sutera A (2003) Spatial variability of drought: an analysis of the SPI in Sicily. Water Resour Manage 17(4):273–296 

Boschetti M, Nutini F, Brivio PA, Bartholome E, Stroppiana D, Hoscilo A (2013) Identification of environmental anomaly hot spots in West Africa from time series of NDVI and rainfall. ISPRS J Photogramm Remote Sens 78:26–40 

Caccamo G, Chisholm LA, Bradstock RA, Puotinen ML (2011) Assessing the sensitivity of MODIS to monitor drought in high biomass ecosystems. Remote Sens Environ 115(10):2626–2639 

Carlson TN, Ripley DA (1997) On the relation between NDVI, fractional vegetation cover, and leaf area index. Remote Sens Environ 62(3):241–252 

Chen J, Jo¨nsson P, Tamura M, Gu Z, Matsushita B, Eklundh L (2004) A simple method for reconstructing a high-quality NDVI time-series data set based on the Savitzky-Golay filter. Remote Sens Environ 91(3):332–344 

Dai AG (2011) Drought under global warming: a review. Wiley Interdiscip Rev Clim Change 2(1):45–65 Dai AG (2013) Increasing drought under global warming in observations and models. Nat Clim Change 3(1):52–58 

Du L, Tian Q, Yu T, Meng Q, Jancso T, Udvardy P, Huang Y (2012) A comprehensive drought monitoring method integrating MODIS and TRMM data. Int J Appl Earth Obs Geoinf 23:245–253 

Ezzine H, Bouziane A, Ouazar D (2014) Seasonal comparisons of meteorological and agricultural drought 

indices in Morocco using open short time-series data. Int J Appl Earth Obs Geoinf 26:36–48 

Federal Emergency Management Agency (FEMA) (1995) National mitigation strategy—partnerships for 

building safer communities. FEMA, Washington, DC 

- Feng L, Hu CM, Chen XL (2012) Satellites capture the drought severity around China’s largest freshwater lake. IEEE J Sel Top Appl Earth Obs Remote Sens 5(4):1266–1271 

123 

Nat Hazards (2016) 80:1135–1152 

1151 

- Gebrehiwot T, van der Veen A, Maathuis B (2011) Spatial and temporal assessment of drought in the Northern highlands of Ethiopia. Int J Appl Earth Obs Geoinf 13(3):309–321 

- Gu Y, Brown JF, Verdin JP, Wardlow B (2007) A five-year analysis of MODIS NDVI and NDWI for grassland drought assessment over the central great plains of the United States. Geophys Res Lett 34(6):186–192 

- Guttman NB (1998) Comparing the palmer drought index and the standardized precipitation index. J Am Water Resour Assoc 34(1):113–121 

- Guttman NB (1999) Accepting the standardized precipitation index: a calculation algorithm. J Am Water Resour Assoc 35(2):311–322 

- Hmimina G, Dufrene E, Pontailler JY, Delpierre N, Aubinet M, Caquet B, de Grandcourt A, Burban B, Flechard C, Granier A, Gross P, Heinesch B, Longdoz B, Moureaux C, Ourcival JM, Rambal S, Saint Andre L, Soudani K (2013) Evaluation of the potential of MODIS satellite data to predict vegetation phenology in different biomes: an investigation using ground-based NDVI measurements. Remote Sens Environ 132:145–158 

- Jiang D, Fu JY, Zhuang DF, Xu XL (2013) Dynamic monitoring of drought using HJ-1 and MODIS time series data in northern China. Nat Hazards 68(2):337–350 

Keshavarz MR, Vazifedoust M, Alizadeh A (2014) Drought monitoring using a Soil Wetness Deficit Index (SWDI) derived from MODIS satellite data. Agric Water Manage 132:37–45 

Kogan FN (1990) Remote sensing of weather impacts on vegetation in non-homogeneous areas. Int J Remote Sens 11(8):1405–1419 Kogan FN (1995) Application of vegetation index and brightness temperature for drought detection. Adv Space Res 15(11):91–100 

Kogan F, Salazar L, Roytman L (2012) Forecasting crop production using satellite-based vegetation health indices in Kansas USA. Int J Remote Sens 33(9):2798–2814 

Kogan F, Adamenko T, Guo W (2013) Global and regional drought dynamics in the climate warming era. Remote Sens Lett 4(4):364–372 

Lasaponara R (2006) On the use of principal component analysis (PCA) for evaluating interannual vegetation anomalies from SPOT/VEGETATION NDVI temporal series. Ecol Model 194(4):429–434 

Li B, Liang Z, Yu Z, Acharya K (2013) Evaluation of drought and wetness episodes in a cold region (Northeast China) since 1898 with different drought indices. Nat Hazards 71(3):2063–2085 Liu W, Kogan F (1996) Monitoring regional drought using the vegetation condition index. Int J Remote Sens 17(14):2761–2782 

Liu WP, Holst J, Yu ZR (2014) Thresholds of landscape change: a new tool to manage green infrastructure and social-economic development. Landsc Ecol 29(4):729–743 Malingreau JP (1986) Global vegetation dynamics—satellite-observations over Asia. Int J Remote Sens 7(9):1121–1146 

McKee TB, Doesken NJ, Kleist J (1993) The relationship of drought frequency and duration to time scales. In: Proceedings of the 8th conference on applied climatology, vol. 17. pp 179–183 

Palmer WC (1965) Meteorological droughts. U.S. Department of Commerce Weather Bureau Research Paper 45 

Park S, Feddema JJ, Egbert SL (2004) Impacts of hydrologic soil properties on drought detection with MODIS thermal data. Remote Sens Environ 89(1):53–62 

Peters AJ, Walter-Shea EA, Ji L, Vina A, Hayes M, Svoboda MD (2002) Drought monitoring with NDVIbased standardized vegetation index. Photogramm Eng Remote Sens 68(1):71–75 

Raziei T, Bordi I, Pereira LS (2008) A precipitation-based regionalization for Western Iran and regional drought variability. Hydrol Earth Syst Sci 12(6):1309–1321 

Rhee J, Im J, Carbone GJ (2010) Monitoring agricultural drought for arid and humid regions using multisensor remote sensing data. Remote Sens Environ 114(12):2875–2887 

Rouse JW, Hass RH, Schell JA, Deering DW (1974) Monitoring vegetation systems in the great plains with ERTS. In: Proceedings of the 3rd earth resources technology satellite-1 symposium, NASA, Greenbelt, pp 309–317 

Santos JF, Pulido-Calvo I, Portela MM (2010). Spatial and temporal variability of droughts in Portugal. Water Resour Res 46(3):742–750 

Seiler RA, Kogan F, Wei G (2000) Monitoring weather impact and crop yield from NOAA AVHRR data in Argentina. Adv Space Res 26(7):1177–1185 

Shahabfar A, Ghulam A, Eitzinger J (2012) Drought monitoring in Iran using the perpendicular drought indices. Int J Appl Earth Obs Geoinf 18:119–127 

- Sohn SJ, Ahn JB, Tam CY (2013) Six month—lead downscaling prediction of winter to spring drought in South Korea based on a multimodel ensemble. Geophys Res Lett 40(3):579–583 

123 

1152 

Nat Hazards (2016) 80:1135–1152 

- Son NT, Chen CF, Chen CR, Chang LY, Minh VQ (2012) Monitoring agricultural drought in the Lower Mekong Basin using MODIS NDVI and land surface temperature data. Int J Appl Earth Obs Geoinf 18:417–427 

- Stagge JH, Tallaksen LM, Gudmundsson L, Van Loon AF, Stahl K (2015) Candidate distributions for climatological drought indices (SPI and SPEI). Int J Climatol. doi:10.1002/joc.4267 

- State Flood Control and Drought Relief Headquarters (SFCDRH) and Ministry of Water Resources of the Government of the People’s Republic of China (2011) Gazette of China’s flood and drought disasters in 2009, Gazette of the Ministry of Water Resources of the People’s Republic of China, vol 1. pp 14–30 

- Tadesse T, Wilhite DA, Harms SK, Hayes MJ, Goddard S (2004) Drought monitoring using data mining techniques: a case study for Nebraska USA. Nat Hazards 33(1):137–159 

- Tadesse T, Brown JF, Hayes MJ (2005) A new approach for predicting drought-related vegetation stress: integrating satellite, climate, and biophysical data over the US central plains. ISPRS J Photogramm Remote Sens 59(4):244–253 

- Thornthwaite CW (1948) An approach toward a rational classification of climate. Geogr Rev 38(1):55–94 

- Vicente Serrano SM, Gonza´lez-Hidalgo JC, Luis MD, Ravento´s J (2004) Drought patterns in the Mediterranean area: the Valencia region (eastern Spain). Clim Res 26(1):5–15 

- Vicente-Serrano SM (2006) Differences in spatial patterns of drought on different time scales: an analysis of the Iberian Peninsula. Water Resour Manage 20(1):37–60 

- Vicente-Serrano SM, Begueria S, Lopez-Moreno JI (2010a) A multiscalar drought index sensitive to global warming: the standardized precipitation evapotranspiration index. J Clim 23(7):1696–1718 

- Vicente-Serrano SM, Begueria S, Lopez-Moreno JI, Angulo M, El Kenawy A (2010b) A new global 0.5 degrees gridded dataset (1901–2006) of a multiscalar drought index: comparison with current drought index datasets based on the Palmer Drought Severity Index. J Hydrometeorol 11(4):1033–1043 

- Wang W, Zhu Y, Xu RG, Liu JT (2015) Drought severity change in China during 1961–2012 indicated by SPI and SPEI. Nat Hazards 75(3):2437–2451 

- Xia JS, Du PJ, He XY, Chanussot J (2014) Hyperspectral remote sensing image classification based on rotation forest. IEEE Geosci Remote Sens Lett 11(1):239–243 

- Xiong J, Wu BF, Yan NN, Zeng YA, Liu SF (2010) Estimation and validation of land surface evaporation using remote sensing and meteorological data in North China. IEEE J Sel Top Appl Earth Obs Remote Sens 3(3):337–344 

- Yu M, Li Q, Hayes MJ, Svoboda MD, Heim RR (2014) Are droughts becoming more frequent or severe in China based on the Standardized Precipitation Evapotranspiration Index: 1951–2010? Int J Climatol 34(3):545–558 

- Zhang AZ, Jia GS (2013) Monitoring meteorological drought in semiarid regions using multi-sensor microwave remote sensing data. Remote Sens Environ 134:12–23 

- Zheng D, Li B (2008) Study on eco-geographic regional systems of China. The Commercial Press, Beijing (in Chinese) 

- Zhou L, Zhang J, Wu JJ, Zhao L, Liu M, Lu AF, Wu ZT (2012) Comparison of remotely sensed and meteorological data-derived drought indices in mid-eastern China. Int J Remote Sens 33(6):1755–1779 

123 

**Reproduced with permission of the copyright owner. Further reproduction prohibited without permission.** 

