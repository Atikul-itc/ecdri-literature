

# **Rapid #: -27621837** 

CROSS REF ID: **896737** 

LENDER: **XFF (Western Washington University) :: Western Libraries** 

BORROWER: **IRU (New Mexico State University) :: Main Library** 

TYPE: Article CC:CCL JOURNAL TITLE: Geocarto international USER JOURNAL TITLE: Geocarto international. ARTICLE TITLE: A combined drought monitoring index based on multi-sensor remote sensing data and machine learning ARTICLE AUTHOR: Han, Hongzhu VOLUME: 36 ISSUE: 10 MONTH: YEAR: 2021 PAGES: 1161-1177 ISSN: 1010-6049 OCLC #: 54940097 Processed by RapidX: 10/5/2026 12:23:56 PM 

This material may be protected by copyright law (Title 17 U.S. Code) 

**Geocarto International** 



**ISSN: 1010-6049 (Print) 1752-0762 (Online) Journal homepage: www.tandfonline.com/journals/tgei20** 



## **A combined drought monitoring index based on multi-sensor remote sensing data and machine learning** 

#### **Hongzhu Han, Jianjun Bai, Jianwu Yan, Huiyu Yang & Gao Ma** 

**To cite this article:** Hongzhu Han, Jianjun Bai, Jianwu Yan, Huiyu Yang & Gao Ma (2021) A combined drought monitoring index based on multi-sensor remote sensing data and machine learning, Geocarto International, 36:10, 1161-1177, DOI: 10.1080/10106049.2019.1633423 

**To link to this article:** <u>https://doi.org/10.1080/10106049.2019.1633423</u> 













Published online: 27 Jun 2019. Submit your article to this journal Article views: 1192 View related articles View Crossmark data Citing articles: 41 View citing articles 



Full Terms & Conditions of access and use can be found at https://www.tandfonline.com/action/journalInformation?journalCode=tgei20 

GEOCARTO INTERNATIONAL 2021, VOL. 36, NO. 10, 1161–1177 https://doi.org/10.1080/10106049.2019.1633423 



### A combined drought monitoring index based on multisensor remote sensing data and machine learning 

##### Hongzhu Han<sup>a</sup> , Jianjun Bai<sup>a</sup> , Jianwu Yan<sup>a,b</sup> , Huiyu Yang<sup>a</sup> and Gao Ma<sup>c</sup> 

> aSchool of Geography and Tourism, Shaanxi Normal University, Xi’an, China; bNational Demonstration Center for Experimental Geography Education, Shaanxi Normal University, Xi’an, China;<sup>c</sup> China Academy of Space Technology-Xi’an, Xi’an, China 

###### ABSTRACT 

The occurrence of drought is related to complicated interactions between many factors, such as precipitation, temperature, evapotranspiration and vegetation. In this study, the relationships between drought and precipitation, temperature, vegetation and evapotranspiration were investigated with a random forest (RF), and a new combined drought monitoring index (CDMI) was constructed. The effectiveness of the CDMI in monitoring drought in Shaanxi Province was verified by the in situ 1 � 12-month standardized precipitation index (SPI); relative soil moisture (RSM) and four other commonly used remote sensing drought monitoring indices. The results show that CDMI is more correlated with the SPI and RSM than the four indices. Moreover, the spatial distributions of drought for the CDMI and RSM are similar. Therefore, the CDMI can be used to monitor droughts in Shaanxi Province, and machine learning can explore the relationships between various factors and establish a drought index without knowledge of the causal mechanisms of these factors. 

###### ARTICLE HISTORY 

Received 8 December 2018 Accepted 5 June 2019 

###### KEYWORDS 

Drought monitoring; MODIS; TRMM; random forest 

##### 1. Introduction 

Drought is considered the most complex but least understood of all natural disasters, affecting more people than any other disaster (Hagman et al. 1984; Hao et al. 2015; Zhang et al. 2017). Each year, droughts result in significant socio-economic losses and ecological damage around the world (Hao et al. 2014). Due to global climate change, the frequency and intensity of drought events in many places worldwide have changed (Mu et al. 2013; Cao et al. 2015; Agutu et al. 2017). Moreover, influenced by the increasing grain demand caused by world population growth, the global adverse effects of droughts have been further expanded. Thus, a system is needed to quantify, monitor and predict droughts (Mishra and Singh 2011; Rajsekhar et al. 2015). 

A drought is generally defined as a water shortage with reference to a specified need for water in a conceptual supply and demand relationship (Dracup et al. 1980). To help understand, describe, monitor and minimize drought, droughts are usually divided into 

> � 2019 Informa UK Limited, trading as Taylor & Francis Group 

CONTACT Jianjun Bai bjj@snnu.edu.cn 

1162 H. HAN ET AL. 

four types: meteorological drought, agricultural drought, hydrological drought and socioeconomic drought (Wilhite and Glantz 1985; Heim 2002; Hao and Singh 2015). Meteorological drought is caused by a lack of rainfall. The soil water content declines with an extended meteorological drought, leading to agricultural drought (Park et al. 2016). Hydrological drought occurs when stream, lake, groundwater or reservoir levels are significantly lower than normal; this type of drought will usually last for a certain period after the meteorological drought ends (Heim 2002; Hao and Singh 2015; Rajsekhar et al. 2015; Park et al. 2016). Socio-economic drought is associated with the supply and demand of some economic goods and possesses features of the other three (physically based) drought types (Wilhite and Glantz 1985; Hao and Singh 2015). 

Among the above four types of drought, agricultural drought is the main drought type that has catastrophic effects, such as crop failure or even famine; in serious cases, this type of drought poses a direct threat to the food supply, the means of production and lives of human beings. For this reason, agricultural droughts have attracted widespread attention worldwide. Moreover, agricultural droughts occur in the early stage of hydrological and socio-economic droughts; monitoring agricultural droughts involves taking measures to prevent droughts in advance and reduce the complexity and impacts of drought. Therefore, accurate and timely agricultural drought monitoring is essential to understand the progression and potential impact and to provide information to support drought mitigation decision-making (Tadesse et al. 2017). Shaanxi Province in China has always suffered from frequent droughts. According to historical records, droughts occur every 3 � 5 years in Shaanxi, and severe droughts occur approximately every 10 years. People say, ‘one small drought occurs every three years, a large drought strikes every ten years, and a hard time happens every thirty years’ (Shi 1994). Furthermore, challenged by socio-economic development, population growth, the increasing demands for production and domestic water, and the frequent occurrence of high temperatures and heat waves triggered by global warming and extreme weather, the present technologies still fail to eliminate severe drought in Shaanxi Province. Therefore, a study on agricultural drought monitoring in Shaanxi could provide the latest information about drought development and changes in drought-prone areas under the background of global climate change. With this information, decision-makers can make early drought control arrangements to reduce disaster losses. 

However, regardless of the type of drought, the interactions among the various influencing factors in the natural environment should be considered in drought monitoring. Generally, drought conditions are associated with multiple variables, which is especially true for agricultural drought. For instance, drought conditions can be aggravated by other climatic factors, such as high temperature and low relative humidity, and are related to water deficits from various sources (Wilhite and Glantz 1985; Wilhite 2005; Jiao et al. 2019). For this reason, any single drought indicator may not sufficiently characterize complicated drought conditions and its wide impact (Hao and Singh 2015). Therefore, blending various indices should be used to monitor droughts (Hayes et al. 2005; Mizzell 2008; Wardlow et al. 2012; Park et al. 2016). When using the blended drought index to monitor droughts, it is particularly important to choose an appropriate index integration method. At present, the commonly used index integration methods include water balance models (standardized precipitation evapotranspiration index: SPEI), linear combinations (scaled drought condition index: SDCI; the microwave-integrated drought index: MIDI), principal component analyses (synthesized drought index: SDI) and joint distributions (multivariate standardized drought index: MSDI) (Hao and Singh 2015). Among these integration methods, linear models are widely used to construct comprehensive drought indices 

GEOCARTO INTERNATIONAL 1163 

because they are easy to understand and simple to calculate. For example, the SDCI, which is used to monitor agricultural drought, was designed with different percentages of three indices: the temperature condition index (TCI), the vegetation condition index (VCI) and the precipitation condition index (PCI); SDCI ¼ (1/4)�scaled LSTþ(2/ 4)�scaled TRMMþ(1/4)�scaled NDVI (Rhee et al. 2010), where LST is the land surface temperature, TRMM is the Tropical Rainfall Measuring Mission rainfall data and NDVI is the normalized difference vegetation index. Similarly, by assigning different weights to each unique remote sensing index, the MIDI was developed based on multi-sensor microwave indices (soil moisture condition index (SMCI), TCI, SMCI and PCI); MIDI ¼ a�PCI þ b�SMCIþ(1-a-b)TCI (Zhang and Jia 2013). The grand mean index (GMI) is used for drought characterizations based on equal weights of the 6-month standardized precipitation index (SPI6), the total soil moisture percentiles (SMPs) and the 3- month standardized runoff index (SRI3); GMI¼(1/3)�SPI6þ(1/3)�SMPþ(1/3)�SRI3 (Mo and Lettenmaier 2014). In linear models for constructing drought indicators, the weights are set based on experience and the test results of the model; in more advanced adaptive weighting methods, such as machine learning methods, various factors can be synthesized for better drought monitoring. Furthermore, in the absence of a clear mechanism for drought caused by multifactor participation, the use of machine learning to mine the data helps us to mathematically understand the relationships between multiple factors. Moreover, the factors used to construct linear models are slightly different for different applications. For example, precipitation, temperature and vegetation are more important than other factors in monitoring the occurrence and development of agricultural droughts. In addition, evapotranspiration (ET) is closely related to drought conditions because it reflects energy and water exchanges among vegetation, soil and the atmosphere and considers the characteristics of soil moisture (Allen et al. 2011; Cooke et al. 2012; Park et al. 2016). Therefore, a drought model cannot ignore ET. Therefore, the purpose of this paper is to use machine learning and these four important factors to develop a new combined drought monitoring index (CDMI) for monitoring agricultural droughts and to conduct research on the effectiveness of indicators in Shaanxi Province, China (Table 1). 

##### 2. Study area and data 

###### 2.1. Study area 

The study area is Shaanxi Province: one of the inland provinces of China. Shaanxi, which is located between 105.48<sup>�</sup> �111.25<sup>�</sup> E and 31.7<sup>�</sup> �39.58<sup>�</sup> N (Figure 1), covers an area of 20.58 � 104 km<sup>2</sup> . Because of its large area and geographical location, Shaanxi has a diverse climate ranging from arid to subtropical humid. There are three distinct climate zones in Shaanxi: the warm/middle temperate semi-arid zone (north of approximately 37<sup>�</sup> N), the warm temperate semi-humid zone (near 33<sup>�</sup> N �37<sup>�</sup> N) and the north subtropical humid zone (south of approximately 33<sup>�</sup> N). Shaanxi has a high elevation in the north and south, while central Shaanxi has a relatively low elevation. The north and south regions of Shaanxi, with higher elevations, belong to a warm/middle temperate semi-arid climate and a north subtropical humid climate, respectively; the low-lying area in the centre belongs to a warm temperate semi-humid climate. Generally, the annual average temperature of Shaanxi is 11.6<sup>�</sup> C; the average precipitation is approximately 653 mm, which is mainly concentrated in 7 � 9 months, and the annual average evaporation is approximately 1608 mm. The uneven precipitation distribution and high annual evaporation have 

1164 H. HAN ET AL. 

Table 1. Summary of drought indices. 

|Drought index|Method|
|---|---|
|SPI<br>SPEI|k�<br>c0þc1kþc2k<sup>2</sup><br>1þd1kþd2k<sup>2</sup>þd3k<sup>3</sup><br>w�<br>c0þc1wþc2w<sup>2</sup><br>1þd1wþd2w<sup>2</sup>þd3w<sup>3</sup>|
|SDCI|(1/4)�scaled LST þ (2/4)�scaled TRMM þ (1/4)�scaled NDVI|
|MIDI|a�PCI þ b�SMCI þ (1-a-b)TCI|
|GMI|(1/3)�SPI6 þ (1/3)�SMP þ (1/3)�SRI3|
|TCI|(LSTmax-LST) / (LSTmax-LSTmin)|
|VCI|(NDVI-NDVImin) / (NDVImax-NDVImin)|
|PCI|(TRMM-TRMMmin) / (TRMMmax-TRMMmin)|
|SMCI|(SM�SMmin) / (SMmax�SMmin)|
|MSDI|It is based on standardization of the joint probability of the<br>accumulated precipitation and soil moisture.|
|SDI|It is based on a principal component analysis (PCA) of VCI, TCI<br>and PCI.|



k is calculated based on the precipitation probability distribution, w is calculated based on the climatic water balance (the difference between precipitation and reference evapotranspiration) probability distribution, and c0, c1, c2, d1, d2 and d3 are constants. 

made Shaanxi a drought-prone area. The major vegetation types in Shaanxi are grassland, cropland and deciduous broadleaf forests. Among these types, grassland is mainly located in the north, cropland is located in the centre and deciduous broadleaf forests are distributed in the south. The major cultivated agricultural crops are wheat and corn, and the farming practices follow a winter wheat and summer maize rotation. 

###### 2.2. Data 

###### 2.2.1. In situ reference data 

The SPI is the World Meteorological Organization (WMO)-ratified index for meteorological drought (Sheffield et al. 2014). Due to its simplicity, space-time comparability and rich time scale, the SPI is widely used for not only studying meteorological drought worldwide but also monitoring other types of drought and comparing various drought indices. Therefore, the SPI was used to evaluate the results of this paper. The 1970 to 2016 daily precipitation data from 34 meteorological stations in Shaanxi Province, which were obtained from the Chinese ground meteorological data daily data set (V3.0) downloaded from the China Meteorological Data website (http://cdc.cma.gov.cn/), were utilized to calculate the 1 � 12-month SPI. The SPI was calculated by using an SPI program provided by the National Drought Monitoring Center of the University of Nebraska–Lincoln (http://drought.unl.edu/MonitoringTools/DownloadableSPIProgram.aspx). 

Considerable studies have verified that soil moisture is an effective indicator for monitoring agricultural drought (Samaniego et al. 2013; AghaKouchak 2014; Paredes-Trejo and Barbosa 2017). Accurate knowledge of soil moisture is a key for characterizing agricultural droughts (Paredes-Trejo and Barbosa 2017). Soil moisture is often used as a measure of agricultural drought since it affects plant growth and productivity (Boken et al. 2005; Wilhite 2005; AghaKouchak et al. 2015). Therefore, the relative soil moisture (RSM) measured at the site was used as the reference index of agricultural drought to evaluate the reliability of the proposed CDMI. The 2001 to 2013 RSM levels of 26 sites in Shaanxi Province were measured 20 cm beneath the soil surface and were obtained from China’s crop growth and farmland soil moisture data set from the China Meteorological Data website. The RSM levels were used to evaluate the various indices. The January 2001 to 

GEOCARTO INTERNATIONAL 1165 



Figure 1. Study area. 

December 2013 monthly soil moisture data from 24 Shaanxi stations were obtained by averaging. 

###### 2.2.2. Remote sensing data 

The December 1999 launch of the Moderate Resolution Imaging Spectroradiometer (MODIS) sensor carried by the Terra satellite, the flagship satellite of NASA’s Earth Observing System (EOS) programme, ushered in a new era of multi-spectral and medium-/high-resolution observations of Earth. MODIS data sets, due to their moderate spectral and spatial resolutions and open access availability, are some of the most widely used data sets in earth science, environmental science and biophysics. In this study, Terra MODIS land surface temperature (LST), ET and surface reflectance data were used to calculate the remotely sensed regional drought factors. The 8-day LST with 1-km resolution (MOD11A2, collection v006), 8-day ET with 500-m resolution (MOD16A2, collection v006) and 8-day surface reflectance with 500-m resolution (MOD09A1, collection v006) were obtained from the Level-1 and Atmosphere Archive & Distribution System (LAADS) 

1166 H. HAN ET AL. 

Table 2. Remote sensing indices and their formulae (TRMM includes the 1-, 3-, 6-, 9-, and 12-month time scales). 

|Remote sensing index|Formula|
|---|---|
|NDVI|(qband2-qband1)/(qband2þqband1)|
|NDWI 5, 6 &7<br>NMDI|(qband2-qband5(or 6 or 7))/(qband2þqband5(or 6 or 7))<br>(qband2-(qband6-qband7)/(qband2þ(qband6-qband7)|
|NDDI 5, 6 &7|(NDVI-NDWI 5,6&7)/(NDVIþNDWI 5,6&7)|
|Scaled NDVI(or VCI)|(NDVI-NDVImin) /(NDVImax-NDVImin)|
|Scaled LST(or TCI)|(LSTmax-LST) /(LSTmax-LSTmin)|
|Scaled ET|(ET-ETmin) /(ETmax-ETmin)|
|Scaled TRMM(or PCI)|(TRMM-TRMMmin) /(TRMMmax-TRMMmin)|



Distributed Active Archive Center (DAAC) website (https://ladsweb.modaps.eosdis.nasa. gov/) for two tiles (h26v05 and h27v05) covering the study area. The sixteen-year period between 2001 and 2016 was used. By using MOD09A1 surface reflectance variables, the NDVI, the normalized difference water index (NDWI), the normalized difference moisture index (NDMI) and the normalized difference drought index (NDDI) were obtained (Table 2). The NDWI was calculated from shortwave-infrared (SWIR) bands 5, 6 and 7 (i.e. NDWI5, NDWI6, and NDWI7, respectively) in ENVI/IDL. All indices with a 500-m spatial resolution were converted into 1-km indices by using the ArcMap resampling tool, and the 8-day indices were averaged according to the number of days in the month to obtain the monthly data by using MATLAB. 

Data from the TRMM, which was launched in November 1997, are some of the most commonly used global precipitation remote sensing data. The 0.25<sup>�</sup> resolution TRMM 3B43 monthly rainfall data from 2000 to 2016 were obtained from the Goddard Earth Sciences Data and Information Services Center (GES DISC; http://mirador.gsfc.nasa.gov/). Data are provided as a precipitation rate with mm/hr and were converted into mm/ month. Considering the time lag between precipitation and agricultural droughts, the TRMM data were accumulated up to 12 months (1, 3, 6, 9 and 12 months) and tested. The literature suggests that TRMM rainfall measures have the potential to substitute for ground-based observations (Abbas et al. 2014). 

##### 3. Methods 

###### 3.1. Remote sensing indices 

The remote sensing indices used in this paper have different units. Therefore, to eliminate the effects of data units in the remote sensing index comparisons, all of the indices were standardized, after which all values ranged from 0 to 1. The remote sensing indices and their formulae are shown in Table 2. 

###### 3.2. Random forest (RF) 

Random forest (RF) models are based on classification and regression trees (CART) and produce numerous independent trees to reach a final decision (e.g. majority votes for classification and average for regression) through two randomization approaches to the selection of training samples and the selection of variables at each node of a tree (Breiman 2001; Liaw and Wiener 2002; Park et al. 2016). In an RF model, each variable is randomly permutated, and the relative importance of the model variables is determined by increase in classification error rate or the regression mean square error (MSE) using out-of-bag (OOB) data (Liaw and Wiener 2002; Park et al. 2016; Liu and Zhao 2017; Park et al. 2017). The setting of two parameters, namely, setting the number of variables in the 

GEOCARTO INTERNATIONAL 1167 

Table 3. Parameter settings for optimal random forests under different factor combinations. 

|||Scaled L|ST, Scaled ET, Scaled N|DVI and||
|---|---|---|---|---|---|
||Scaled TRMM1|Scaled TRMM3|Scaled TRMM6|Scaled TRMM9|Scaled TRMM12|
|mtry|3|2|1|1|1|
|ntree|150|52|625|460|85|



random subset at each node mtry and the number of trees in the forest ntree, in an RF model will affect the model’s accuracy. The RF model was implemented in R (http://www. r-project.org) with the randomForest package with the default settings, except for mtry and ntree. The RF model was run repeatedly with mtry¼1 … n, where n is the number of predictive factors or independent variables and ntree¼1000 until the best RF model was obtained; subsequently, the relative importance of the predictive factors (independent variables) in the optimal RF can be obtained. This relative importance was used as a factor coefficient to construct the linear model of the CDMI. The parameter settings of the best RF model for different factor combinations are shown in Table 3. 

##### 4. Results and discussion 

###### 4.1. Construction of the combined drought index 

As mentioned in the introduction, the four main factors involved in the occurrence, development and evolution of drought were selected to construct the combined drought indicators. These factors are the standardized forms of the NDVI, LST, ET and TRMM, which are denoted as Scaled NDVI, Scaled LST, Scaled ET and Scaled TRMM, respectively. Scaled TRMM mainly refers to the cumulative precipitation at 1, 3, 6, 9 and 12 months, which are denoted by Scaled TRMM1, Scaled TRMM3, Scaled TRMM6, Scaled TRMM9 and Scaled TRMM12, respectively. Subsequently, each was combined with Scaled NDVI, Scaled LST and Scaled ET to obtain the optimal cumulative precipitation scale for the combined drought index. The importance of each factor was obtained after inputting the five different combinations of Scaled NDVI, Scaled LST, Scaled ET and Scaled TRMM as independent variables and the RSM as the dependent variable into the RF model. Next, the importance of each factor was homogenized as a factor coefficient, and a linear model of the combined drought index was constructed. The five factor combinations and the weighted coefficients are listed in Table 4. 

###### 4.2. The combined drought monitoring index (CDMI) 

The importance coefficients of different factors were obtained through the RF model based on which the five combined drought indices were constructed. To determine the optimum combined index for drought monitoring, the correlations between each of the above-mentioned combined drought indices and the RSM measured at the site were analysed (Figure 2). 

Figure 2(a) shows the correlation coefficient between the combined drought index and the RSM measured at the 24 sites. It is obvious that the drought indices based on different factor combinations and the RSM are all significant (P<.01) positively correlated, and the correlation coefficient of the combined drought index calculated by Combination 3 and the RSM is the largest. From Table 3, the different factor combinations are used to choose different time scales for the precipitation factors. Therefore, the correlation coefficient of the combined drought index and RSM increases gradually along with the TRMM 

1168 H. HAN ET AL. 

Table 4. The combinations and coefficients of different factors. 

|Combination 1||Combination|2|Combination|3|Combination|4|Combination|5|
|---|---|---|---|---|---|---|---|---|---|
|Scaled LST|0.35|Scaled LST|0.32|Scaled LST|0.25|Scaled LST|0.27|Scaled LST|0.37|
|Scaled ET|0.13|Scaled ET|0.14|Scaled ET|0.21|Scaled ET|0.24|Scaled ET|0.25|
|Scaled NDVI|0.16|Scaled NDVI|0.16|Scaled NDVI|0.19|Scaled NDVI|0.17|Scaled NDVI|0.19|
|Scaled TRMM1|0.36|Scaled TRMM3|0.38|Scaled TRMM6|0.36|Scaled TRMM9|0.32|Scaled TRMM12|0.19|





Figure 2. (a) Correlation coefficient (R) of the combined drought index and the relative soil moisture (RSM); (b) a scatter plot of the CDMI and RSM. 

time scale until Scaled TRMM6 and gradually decreases after Scaled TRMM6, and the first decrease is the largest. The minimum correlation coefficient of the cumulative precipitation scale appears at Scaled TRMM12. In addition, according to the variation amplitude of the correlation coefficient between the combined drought index from different time scales and the RSM, the change is gentle when the correlation coefficient gradually increases along the cumulative precipitation time scale. After achieving the maximum correlation coefficient along the cumulative precipitation time scale, the correlation coefficient gradually decreases with the prolongation of cumulative precipitation time scale, and the first decrease is the largest. 

From the above analyses, the combined drought index constructed by precipitation, temperature, vegetation and evapotranspiration can effectively reflect the change in soil moisture and monitor the drought in the study area. Moreover, the comparison between the correlation coefficients of the different combined drought indices and the RSM shows that the combined drought index with 6 months of cumulative precipitation has the best performance in reflecting the drought conditions; therefore, this combined drought index is regarded as the CDMI. The model expression is as follows: 

CDMI ¼ 0:36 � Scaled TRMM6 þ 0:25 � Scaled LST þ 0:19 � Scaled NDVI 



Because the CDMI and SDCI have similar calculation formulae that belong to linear combinations of comprehensive drought monitoring indicators, the CDMI also be divided into six categories (Table 5). 

GEOCARTO INTERNATIONAL 1169 

Table 5. The CDMI categories. 

|Category|CDMI|SDCI|
|---|---|---|
|Exceptional drought|0.0�CDMI < 0.1|0.0�SDCI < 0.1|
|Extreme drought|0.1�CDMI < 0.2|0.1�SDCI < 0.2|
|Severe drought|0.2�CDMI < 0.3|0.2�SDCI < 0.3|
|Moderate drought|0.3�CDMI < 0.4|0.3�SDCI < 0.4|
|Abnormally dry|0.4�CDMI < 0.5|0.4�SDCI < 0.5|
|No drought|CDMI > 0.5|SDCI > 0.5|



###### 4.3. A time series correlation analysis of the CDMI and RSM 

To examine the correlation between the CDMI proposed in this paper and the stationbased time series measurements of the RSM, an intra- and inter-annual correlation analysis of CDMI and RSM was performed. 

From Figure 3(a), the correlation between the CDMI and RSM from 2001 to 2013 was significant (P<.01), the correlation coefficient r ranged from 0.33 to 0.78, and the average r was 0.59. In detail, from the yearly values of r, in 2002, the correlation coefficient is at a minimum, and in 2011, the correlation coefficient is at a maximum. The r values of the remaining years are less different and are approximately equal to the average. Therefore, according to the correlation analysis results shown in Figure 3(a), CDMI can reflect the changes in the RSM in different months of each year between 2001 and 2013. The correlation between the CDMI and RSM was significant from February to December, and the range of r was 0.15 � 0.55, with an average of 0.38 (Figure 3(b)). Thus, the CDMI can also reflect the inter-annual variation in the RSM for most months. 

The intra-annual or inter-annual correlation analyses both showed a significant correlation between CDMI and RSM, indicating that the CDMI can reflect temporal changes in the RSM. 

###### 4.4. Comparison of the spatial distributions of the CDMI and RSM 

From Section 4.3, we know that the time series of the CDMI and RSM are significantly correlated, and the CDMI can reflect the temporal changes in the RSM, but in space, will the distributions of CDMI and RSM be consistent? And if this consistency directly affects whether the spatial distribution of drought indicated by the CDMI is consistent with the actual drought distribution, can the CDMI demonstrate the spatial changes in the RSM? This paper attempts to solve this problem by comparing the spatial distribution of the RSM with the spatial distribution of drought monitored by the CDMI from January to December 2011 (Figure 4). It should be noted that in Figure 4, data are missing from some stations in certain months, and the total number of collected RSM levels is inconsistent across months. 

Despite the lack of enough measurement station and missing RSM data, there is an observed consistency in the spatial distributions of the RSM and the CDMI in Figure 4. As shown in Figure 4, the values of the CDMI and RSM have spatial agreement. Areas with large CDMI values have large RSM values; similarly, areas with small CDMI values have small RSM values. This finding indicates that the CDMI can accurately determine the spatial distribution of drought; thus, it can be used to monitor the spatial distribution of drought. 

1170 H. HAN ET AL. 



Figure 3. (a) Scatter plot of the intra-annual correlation analysis of the CDMI and RSM; (b) scatter plot of the interannual correlation analysis of the CDMI and RSM. 

By comparing the spatial distributions of the CDMI and the RSM, we confirmed that the CDMI can reflect the spatial distribution of drought. Thus, by taking advantage of the CDMI as a remote sensing drought monitoring index, we can not only analyse more details of the spatial distribution of droughts but also the temporal and spatial evolution. 

GEOCARTO INTERNATIONAL 1171 



Figure 3. Continued. 

As shown in the maps in Figure 4, the spatiotemporal evolution of drought in Shaanxi from January to June shows the formation of drought in nearly the whole province (CDMI < 0.5) and over time. The drought intensity gradually increased, and the 

1172 H. HAN ET AL. 



Figure 4. Spatial distributions of the CDMI and RSM in 2011. 

differences in regional drought began to appear. The most severe drought month in the province occurred in April (CDMI < 0.2 in most parts of the province), and the most obvious regional drought differences occurred in June (the CDMI < 0.2 in northern Shaanxi, the CDMI ranged from 0.1 to 0.3 in central Shaanxi and the CDMI ranged from 0.3 to 0.5 in southern Shaanxi). Subsequently, the drought began to ease in July, and the drought in the southern part of Shaanxi basically ended. The drought relief continued into November, and consequently, the province basically showed no drought in November. However, droughts started to emerge in the northern and southern parts of Shaanxi in December. From a seasonal perspective, the analysis of Shaanxi drought characteristics revealed that drought mainly occurs in winter, spring and early summer, and there is no drought in autumn, which is consistent with the seasonality of the drought distribution in Shaanxi (Shi 1994). 

###### 4.5. Comparison with other drought monitoring indices 

To further illustrate the applicability of the proposed CDMI in drought monitoring, the CDMI was compared with other drought indicators. Because most drought factors used 

GEOCARTO INTERNATIONAL 1173 

Table 6. Correlation coefficients (r) for remote sensing indices with the SPI and RSM (Notes:<sup>�</sup> indicates P>.05, and the bold values are the maximum value of each column). 

|Remote sensing<br>index|SPI1<br>(n¼6528)|SPI3<br>(n¼6528)|SPI6<br>(n¼6528)|SPI9<br>(n¼6528)|SPI12<br>(n¼6528)|RSM<br>(n¼2515)|
|---|---|---|---|---|---|---|
|NDVI|–0.06|–0.04<br>|–0.06|–0.03|�0.01<br>|–0.05|
|NDWI5|0.08|�–0.01|–0.06|–0.03|�–0.02|0.05|
|NDWI6|0.07|�–0.01|–0.06|–0.03|�–0.01|0.11|
|NDWI7|0.05|�–0.01|–0.05|–0.02|�0.01|0.16|
|NDDI5|�–0.01|�–0.01|�–0.01|�–0.01|�–0.02|0.04|
|NDDI6|�0|0.03|�0.02|�0|�0.01|�0|
|NDDI7|�–0.01|�–0.02|�–0.01|�–0.01|�–0.01|�0|
|NMDI|�0.01|–0.03|�–0.02|–0.03|–0.06|–0.26|
|LST|–0.13|–0.12|–0.13|–0.06|–0.03|–0.39|
|ET|0.11|0.07|0.06|�0.01|�0|0.30|
|TRMM6|0.12|0.25|0.32|0.22|0.21|0.49|
|Scaled NDVI (VCI)|–0.05|�–0.02|–0.04|�0|0.04|–0.05|
|Scaled LST (TCI)|0.14|0.13|0.14|0.08|0.04|0.35|
|Scaled ET|0.12|0.07|0.06|�0.02|�0.01|0.25|
|Scaled TRMM6|0.16|0.30|0.38|0.27|0.26|0.39|
|SDCI (TRMM6)|0.18|0.29|0.35|0.24|0.24|0.44|
|CDMI or CDI (TRMM6)|0.20|0.26|0.50|0.19|0.18|0.62|



to construct the CDMI are common monitoring indicators of meteorological drought and agricultural drought, in this paper, the CDMI was compared with meteorological and agricultural drought indices. The SPI is a widely used meteorological drought index that is not only used for comparing various newly proposed drought monitoring indices but also as one of the major factors for constructing other comprehensive drought monitoring indices or drought monitoring and prediction systems (Rhee et al. 2010; Zhou et al. 2013; Hao Z et al. 2014). Therefore, the SPI calculated by the measured precipitation data from meteorological stations, as a representative index of meteorological drought, was utilized to evaluate the suitability of other drought indices for monitoring meteorological drought. Because soil moisture is closely related to agricultural drought (Lambert et al. 2013; Long et al. 2013; Park et al. 2016), the measured RSM is often used to verify the performance of the agricultural drought monitoring index. The correlation analyses were conducted between the SPI, the RSM and the following indices: the CDMI, other commonly used drought monitoring indices (VCI, TCI, NDWI, NDDI and NMDI) and drought factors (ET and TRMM). The meteorological drought and agricultural drought monitoring performances of drought indices were compared. The SDCI (Rhee et al. 2010), a comprehensive agricultural drought monitoring index, was also used in the comparative study (Table 6). 

As shown in Table 6, the correlations between SPI1, SPI3, SPI6, SPI9 and SPI12 and the combined drought indices (e.g. the CDMI and SDCI) are generally higher than those of any of the single remote sensing drought indices, excluding Scaled TRMM6, and the range of correlation coefficients r is 0.12 � 0.50. The correlation coefficients between the proposed drought index and SPI1 and SPI6 are the largest among all of the remote sensing indices. This finding indicates that the CDMI is superior to other drought indices in reflecting short- and medium-term meteorological droughts. However, the performance is not as good as Scaled TRMM6 and the SDCI for long-term meteorological drought monitoring. The largest correlation coefficients were between Scaled TRMM6 and SPI9 and between the Scaled TRMM6 and SPI12, which may be because the influence of factors other than precipitation on meteorological drought is quite small during long-term meteorological droughts. The correlation between SDCI and SPI9 and between SDCI and SPI12 is larger than the correlation between CDMI and SPI9 and between CDMI and 

1174 H. HAN ET AL. 

SPI12, which may be because the weight of the SDCI is 0.5, which is much larger than the weight of the CDMI (0.36). 

According to the correlation analysis between the remote sensing indices and the relative soil moisture, the correlation coefficients between the CDMI and RSM and between the SDCI and RSM are generally higher than those between other remote sensing indices and the RSM, which indicates the advantages of combined drought indices in reflecting the RSM. Moreover, the correlation coefficient (r ¼ 0.62) of the CDMI and RSM is higher than that of the SDCI and RSM (r ¼ 0.44), which indicates that the CDMI is more effective than the SDCI. 

Although the correlations between other remote sensing indices and the RSM are not as large as the correlations of the CDMI and SDCI with the RSM, meaningful observations can still be made: (1) the NDDI, which is based on the NDVI, is not related to any of the SPIs nor the RSM, indicating that the NDDI is not suitable for monitoring droughts in the study area. (2) The drought indices NDVI, NDWI and NMDI are more correlated with the RSM than with the SPI, which is indicated by the significance test for r. This finding shows that the NDVI, NDWI and NMDI, which are based on the spectral reflectance of vegetation, are more suitable for monitoring agricultural droughts than other types of droughts. (3) The correlations between SPI1, SPI3, SPI6, SPI9, SPI12 and RSM and the LST, ET and TRMM, which are based on temperature and moisture levels, were tested. The correlations between the RSM and LST and the RSM and ET are slightly larger than the correlations between the RSM and each of SPI1, SPI3, SPI6, SPI9 and SPI12, and the correlation between the RSM and LST is generally higher than that between the RSM and ET. This finding indicates that the influences that LST and ET exert on agricultural drought are larger than those on meteorological drought. In addition, the effect of LST on drought, whether meteorological or agricultural, is greater than that of ET. The correlations between TRMM and each of SPI1, SPI3, SPI6, SPI9, SPI12 and RSM are larger than those of any single remote sensing drought index. Again, it has been suggested that precipitation is the main influence factor for drought. 

From the above analyses, the correlations between the proposed CDMI and each of SPI1, SPI3, SPI6, SPI9, SPI12 and the RSM are significant and are generally larger than those of other remote sensing drought indices. This finding indicates that the proposed CDMI, which was constructed with an RF method, can reflect both meteorological drought and agricultural drought. Moreover, the CDMI outperforms the SDCI, which indicates that the performance of the drought monitoring index is significantly improved by the introduction of the ET variable. In addition, the proposed CDMI is more suitable for monitoring agricultural drought because the correlation between it and the RSM is much larger than the correlation between it and the SPI. 

##### 5. Conclusions 

In this paper, the relative importance of four drought factors (precipitation, temperature, vegetation and evapotranspiration) was analysed by an RF model, and a combined drought index constructed based on these four factors was constructed after calculating the weight of each factor. Subsequently, the equation of the CDMI was established. The agricultural drought index CDMI was determined by analysing its correlation with RSM. Moreover, the spatial distribution of drought determined by the CDMI agrees with that of the RSM, and the temporal and spatial changes in drought in Shaanxi were analysed. The performances of the CDMI and other drought monitoring indices in monitoring meteorological drought and agricultural drought were analysed and compared. The 

GEOCARTO INTERNATIONAL 1175 

correlation coefficient between the CDMI and SPI1, SPI6 or RSM shows that the performance of the CDMI is better than those of other remote sensing indices and the comprehensive agricultural drought monitoring index SDCI. This finding shows that mapping and monitoring regional agricultural drought can be realized through the CDMI based on satellite remote sensing data when the measured data are incomplete. 

In summary, the method for constructing a combined drought index, under the condition that the mechanism of drought-induced interaction between drought-causing factors is not clear, is proposed in this paper, a machine learning-based RF model is used to assess the abilities of the indices to represent drought and a comprehensive multi-factor drought index is constructed. In addition, with Shaanxi as an example, the feasibility of the index is proven, and its drought monitoring effectiveness is superior to that of other common drought indices. 

##### Acknowledgement 

We are grateful to the anonymous reviewers for their valuable comments and recommendations, which greatly help us to improve the original version of the manuscript. 

##### Disclosure statement 

No potential conflict of interest was reported by the authors. 

##### Funding 

This work was supported by the National Natural Science Foundation of China [41171310, 41501093] and the Natural Science Basic Research Program of Shaanxi grant number [2016JM4016]. 

##### References 

- Abbas S, Nichol JE, Qamer FM, Xu J. 2014. Characterization of drought development through remote sensing: a case study in Central Yunnan, China. Remote Sens. 6(6):4998–5018. 

- AghaKouchak A. 2014. A baseline probabilistic drought forecasting framework using standardized soil moisture index: application to the 2012 United States drought. Hydrol Earth Syst Sci. 18(7): 2485–2492. 

- AghaKouchak A, Farahmand A, Melton FS, Teixeira J, Anderson MC, Wardlow BD, Hain CR. 2015. Remote sensing of drought: Progress, challenges and opportunities. Rev Geophys. 53(2): 452–480. 

- Agutu NO, Awange JL, Zerihun A, Ndehedehe CE, Kuhn M, Fukuda Y. 2017. Assessing multi-satellite remote sensing, reanalysis, and land surface models’ products in characterizing agricultural drought in East Africa. Remote Sens Environ. 194:287–302. 

- Allen R, Irmak A, Trezza R, Hendrickx JM, Bastiaanssen W, Kjaersgaard J. 2011. Satellite-based ET estimation in agriculture using SEBAL and METRIC. Hydrol Process. 25(26):4011–4027. 

- Boken VK, Cracknell AP, Heathcote RL, editors. 2005. Monitoring and predicting agricultural drought: a global study. Oxford: Oxford University Press. 

Breiman L. 2001. Random forests. Mach Learn. 45(1):5–32. 

- Cao Y, Nan Z, Cheng G. 2015. GRACE gravity satellite observations of terrestrial water storage changes for drought characterization in the arid land of northwestern China. Remote Sens. 7(1): 1021–1047. 

- Cooke WH, Mostovoy GV, Anantharaj VG, Jolly WM. 2012. Wildfire potential mapping over the state of Mississippi: a land surface modeling approach. GISci Remote Sens. 49(4):492–509. 

Dracup JA, Lee KS, Paulson EG. 1980. On the definition of droughts. Water Resour Res. 16(2):297–302. 

1176 H. HAN ET AL. 

Hagman G, Beer H, Bendz M, Wijkman A. 1984. Prevention better than cure. Report on human and environmental disasters in the Third World. Stockholm: Swedish Red Cross. 

Hao C, Zhang J, Yao F. 2015. Combination of multi-sensor remote sensing data for drought monitoring over Southwest China. Int J Appl Earth Obs Geoinf. 35:270–283. 

Hao Z, AghaKouchak A, Nakhjiri N, Farahmand A. 2014. Global integrated drought monitoring and prediction system. Scientific Data. 1:1–10. 

Hao Z, Singh VP. 2015. Drought characterization from a multivariate perspective: a review. J Hydrol. 527: 668–678. 

Hayes M, Svoboda M, Le Comte D, Redmond KT, Pasteris P. 2005. Drought monitoring: New tools for the 21st century. In: Wilhite DA. Drought and water crises: science, technology, and management issues. Abingdon: Taylor and Francis; p. 53–69. 

Heim RR. Jr 2002. A review of twentieth-century drought indices used in the United States. Bull Amer Meteor Soc. 83(8):1149–1165. 

Jiao W, Tian C, Chang Q, Novick KA, Wang L. 2019. A new multi-sensor integrated index for drought monitoring. Agric For Meteorol. 268:74–85. 

Lambert J, Drenou C, Denux J-P, Balent G, Cheret V. 2013. Monitoring forest decline through remote sensing time series analysis. GISci Remote Sens. 50(4):437–457. 

Liaw A, Wiener M. 2002. Classification and regression by randomForest. R News. 2(3):18–22. 

Liu Y, Zhao H. 2017. Variable importance-weighted random forests. Quant Biol. 5(4):338–351. 

Long JA, Lawrence RL, Greenwood MC, Marshall L, Miller PR. 2013. Object-oriented crop classifica- 

tion using multitemporal ETM þ SLC-off imagery and random forest. GISci Remote Sens. 50(4): 418–436. 

Mishra AK, Singh VP. 2011. Drought modeling–A review. J Hydrol. 403(1–2):157–175. 

Mizzell EHP. 2008. Improving drought detection in the Carolinas: evaluation of local, state, and federal 

drought indicators [Doctoral dissertation]. Columbia: University of South Carolina. 

Mo KC, Lettenmaier DP. 2014. Objective drought classification using multiple land surface models. J Hydrometeor. 15(3):990–1010. 

Mu Q, Zhao M, Kimball JS, McDowell NG, Running SW. 2013. A remotely sensed global terrestrial drought severity index. Bull Amer Meteor Soc. 94(1):83–98. 

- Paredes-Trejo F, Barbosa H. 2017. Evaluation of the SMOS-Derived Soil Water Deficit Index as Agricultural Drought Index in northeast of Brazil. Water. 9(6):377. 

Park S, Im J, Jang E, Rhee J. 2016. Drought assessment and monitoring through blending of multi-sensor indices using machine learning approaches for different climate regions. Agric For Meteorol. 216: 157–169. 

Park S, Im J, Park S, Rhee J. 2017. Drought monitoring using high resolution soil moisture through multi-sensor satellite data fusion over the Korean peninsula. Agric For Meteorol. 237:257–269. 

Rajsekhar D, Singh VP, Mishra AK. 2015. Multivariate drought index: an information theory based approach for integrated drought assessment. J Hydrol. 526:164–182. 

Rhee J, Im J, Carbone GJ. 2010. Monitoring agricultural drought for arid and humid regions using multisensor remote sensing data. Remote Sens Environ. 114(12):2875–2887. 

Samaniego L, Kumar R, Zink M. 2013. Implications of parameter uncertainty on soil moisture drought analysis in Germany. J Hydrometeor. 14(1):47–68. 

- Sheffield J, Wood EF, Chaney N, Guan K, Sadri S, Yuan X, Olang L, Amani A, Ali A, Demuth S, et al. 2014. A drought monitoring and forecasting system for sub-sahara African water resources and food security. Bull Amer Meteor Soc. 95(6):861–861. 

- Shi Y. 1994. Causes and temporal spatial distribution characteristics of drought disasters in Shaanxi. J Arid Land Res Environ. 8(3):51–57. 

- Tadesse T, Champagne C, Wardlow BD, Hadwen TA, Brown JF, Demisse GB, Bayissa YA, Davidson AM. 2017. Building the vegetation drought response index for Canada (VegDRI-Canada) to monitor agricultural drought: first results. GIsci Remote Sens. 54(2):230–257. 

- Wardlow BD, Anderson MC, Verdin JP. 2012. Remote sensing of drought: Innovative monitoring approaches. Boca Raton: CRC Press. 

- Wilhite DA. 2005. Drought and water crises: science, technology, and management issues. Vol. 86. 1st ed. Boca Raton: CRC Press. 

- Wilhite DA, Glantz MH. 1985. Understanding: the drought phenomenon: the role of definitions. Water Int. 10(3):111–120. 

- Zhang A, Jia G. 2013. Monitoring meteorological drought in semiarid regions using multi-sensor microwave remote sensing data. Remote Sens Environ. 134:12–23. 

GEOCARTO INTERNATIONAL 1177 

- Zhang L, Jiao W, Zhang H, Huang C, Tong Q. 2017. Studying drought phenomena in the Continental United States in 2011 and 2012 using various drought indices. Remote Sens Environ. 190:96–106. 

- Zhou L, Wu J, Zhang J, Leng S, Liu M, Zhang J, Zhao L, Zhang F, Shi Y. 2013. The integrated surface drought index (ISDI) as an indicator for agricultural drought monitoring: theory, validation, and application in Mid-Eastern China. IEEE J Sel Top Appl Earth Observations Remote Sensing. 6(3): 1254–1262. 

