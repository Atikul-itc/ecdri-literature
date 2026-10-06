Catena 209 (2022) 105804 



Contents lists available at ScienceDirect 

# Catena 

journal homepage: www.elsevier.com/locate/catena 



A novel comprehensive agricultural drought index reflecting time lag of soil moisture to meteorology: A case study in the Yangtze River basin, China 



## Qing Tian<sup>a</sup> , Jianzhong Lu<sup>a,b,*</sup> , Xiaoling Chen<sup>a,b</sup> 

a _State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University, Wuhan 430079, China_ b _Hubei Luojia Laboratory, Wuhan 430079, China_ 

|A R T I C L E I N F O|A B S T R A C T|
|---|---|
|_Keywords:_<br>|Soil moisture related agriculture drought usually lags behind meteorological factors. In order to address such a|
|Agricultural drought index<br>Soil moisture<br>Precipitation<br>Evapotranspiration<br>Time lag<br>Yangtze River basin|hysteresis, the time lag of soil moisture to meteorological factors were initially investigated based on remote<br>sensing products and meteorological observed data in Yangtze River basin. Soil moisture exhibited different lag<br>times to meteorological factors in different climate regions. There is one month lagged in the northwest of the<br>Yangtze River basin, while two months lagged in the middle and east. A novel Comprehensive Agricultural<br>Drought Index (CADI) was then constructed to reflect the feedback of time lag effects in drought assessment,<br>which comprehensively integrated the lagging times of soil moisture to precipitation and evapotranspiration. The<br>CADI was negatively correlated with Standardized Precipitation Index (SPI), Standard Precipitation Evapo-<br>transpiration Index (SPEI), Vegetation Health Index (VHI) and Reconnaissance Drought Index (RDI), among<br>which the SPEI-3 was most strongly correlated. Drought grades captured by CADI had significantly positive<br>correlations to SPI, SPEI, VHI and RDI captured with correlation coefficients between 0.5 and 0.7. Moreover, the<br>CADI was able to effectively monitor the annual and seasonal variations and spatial pattern of agricultural<br>drought, particularly better identify summer droughts, from which the crop phenology related agriculture<br>drought monitoring can benefit. The temporal variation trend of CADI also agreed to the crop drought-affected<br>area. Therefore, the proposed CADI is superior to characterize agricultural drought by eliminating temporally<br>asynchronous effects of meteorology and soil moisture on drought monitoring. It provides scientific support for<br>hazard assessment and mitigation of regional drought management.|



### **1. Introduction** 

As a hydroclimatic extreme phenomenon, drought occurs frequently and widespreadly, which has enormous impacts on economy, society and environment (Huang et al., 2021; Mishra and Singh, 2010). Most drought concepts are defined according to the application directions (Liu et al., 2020a; Mishra and Singh, 2010), in which drought can be classified into four types including meteorological drought, agricultural drought, hydrological drought and socioeconomic drought (AghaKouchak et al., 2015; Dracup et al., 1980; Dai, 2011; Heim, 2002; Mishra and Singh, 2010). The essential connotation of all types of drought is the phenomenon of water deficit caused by insufficient precipitation, and there are complex relationships between them (Liu, et al., 2016). In particular, the agricultural drought is regarded as a phenomenon of crop yield reduction due to insufficient soil moisture, which will constrain 

food production and lead to food security issues on a global scale (Mu et al., 2013). Therefore, it is of great significance to construct a robust agricultural drought index for understanding the evolution of agricultural drought, assessing agricultural drought risk and making decision. 

Drought indexes are commonly used to identify and monitor drought conditions, in order to quantitatively assess the intensity, duration and spatial extent of drought. So far there are nearly one hundred drought indexes developed for various applications (Heim 2002; Liu et al., 2016). For example, three most popularly used drought indexes, including Palmer Drought Severity Index (PDSI) (Palmer, 1965), Standardized Precipitation Index (SPI) (McKee et al., 1993), and Standardized Precipitation Evapotranspiration Index (SPEI) (Vicente-Serrano et al., 2010) based on one or more hydroclimatic factors, such as potential evapotranspiration and precipitation, were widely used in drought monitoring (Gupta and Jain, 2021; Liu and Sun, 2020; McCabe 

* Corresponding author at: State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University, Wuhan 430079, China. 

_E-mail address:_ lujzhong@whu.edu.cn (J. Lu). 

https://doi.org/10.1016/j.catena.2021.105804 

Received 9 July 2021; Received in revised form 10 October 2021; Accepted 11 October 2021 0341-8162/© 2021 Elsevier B.V. All rights reserved. 

_Catena 209 (2022) 105804_ 

_Q. Tian et al._ 

and Wolock, 2020; Salvador et al., 2021). However, the above drought indexes were designed for specific applications, which were challenged in agricultural drought assessment. In addition, the lagging response of vegetation to insufficient precipitation due to residual water in the soil (S´anchez et al., 2016) leads to agriculture drought temporally lagging to above indexes (Zhao et al., 2018). Therefore, traditional drought indexes were insufficient to monitor agriculture drought without concerning the time lag effects. 

To characterize agricultural drought, soil moisture data were commonly used in comprehensive drought assessment (Li et al., 2020; Liu et al., 2020c; Liu and Sun, 2020; Souza et al., 2020). Soil moisture is usually defined as the water contained in the unsaturated soil zone (Hillel, 1998). Although the water needed for agriculture is usually in the root zone, it has been confirmed that the information of surface soil moisture and root zone soil moisture are relevant, which reduces the uncertainty in the drought assessment process (Sanchez et al., 2016´ ). Moreover, the development of microwave remote sensing technology makes it possible to obtain global surface soil moisture data (AghaKouchak et al., 2015; Bolten et al., 2010; Yin et al., 2018). In recent years, many scholars have proposed multivariate comprehensive drought indexes integrated soil moisture data (Du et al., 2019; Hao and AghaKouchak, 2013; Huang et al., 2015; Kao and Govindaraju, 2010; S´anchez et al., 2016; Wang et al., 2018). Huang et al. (2015) constructed Integrated Drought Index (IDI) based on precipitation, runoff and soil moisture factors, and determined the weight of each factor through entropy weight method. Sanchez et al. (2016) ´ constructed Soil Moisture Agricultural Drought Index (SMADI) based on the inverse relationship between land surface temperature and vegetation conditions, and then considered the response of vegetation to soil moisture, in which soil moisture was set as a multiplier factor. However, there is a mutual feedback and response relationship between hydrological and meteorological factors, as well the correlations between factors have a time lag effect. The determination of the lag time between variables should be deeply investigated. 

In the context of climate change and land–atmosphere coupling, there are complex responses and feedbacks between soil moisture, precipitation and evapotranspiration (Seneviratne et al., 2010; Bojinski et al. 2014), which have important connections with changes in climate variability and extreme events, as well as ecosystem and agricultural (Lu et al., 2018; Lu et al., 2020; Zhang et al., 2019a). According to the principle of land–atmosphere coupling, precipitation–supplemented water must be at least equal to the evapotranspiration; otherwise, the insufficient precipitation–supplemented water will lead to the net effect of original soil moisture reduction (Seneviratne et al., 2010). The memory of soil moisture is a key aspect in land–atmosphere interactions, which may produce a potential time lag effect between soil moisture and climatic factors (Koster and Suarez, 2001; Wu and Dickinson, 2004). A period of atypical precipitation may have a positive anomalous effect on soil moisture, and evaporation or other processes may take several weeks or months to dissipate this anomaly, and similar time required to dissipate anomalies also exists for negative soil moisture anomalies—i. e., drought conditions (Wu and Dickinson, 2004). So far, several studies focused on estimating the lag time of different data through correlation coefficient, Bayesian model, cross wavelet transform or other methods (Grinsted et al., 2004; Liu et al., 2020b; Sattar and Kim, 2018; Zhao et al., 2020). Previous studies have also indicated that there are different temporal gaps between soil moisture and meteorological factors in different timescales (Jones and Brunsell, 2009; Wu and Dickinson, 2004). However, monthly scale of soil moisture related agriculture drought asynchronous to meteorology has not been revealed yet. Therefore, it is of great significance to construct an agricultural drought index concerning such an asynchronous effect of meteorological factors on soil moisture. This study attempts to understand the lag times of soil moisture to precipitation and evapotranspiration in agriculture drought assessment. 

In this study, the lag time of soil moisture to meteorological factors 

was first calculated by cross wavelet transform method, on which based a novel Comprehensive Agricultural Drought Index (CADI) was constructed to reflect such a time lag effect. And then the long-term CADI was calculated and compared with SPI, SPEI, VHI (Vegetation Health Index) and RDI (Reconnaissance Drought Index) in Yangtze River basin. In addition, the CADI drought grades threshold was proposed to assess different drought severities, which were verified by the temporal and spatial distribution of historical agricultural droughts. It provides a perspective to monitor and assess the global agricultural drought. 

### **2. Study area and data** 

### _2.1. The Yangtze River basin_ 

The Yangtze River is the longest river in China and the third longest river in world with a total length of about 6,380 km. The Yangtze River basin (24<sup>◦</sup> 30<sup>′</sup> N ~ 35<sup>◦</sup> 45<sup>′</sup> N, 90<sup>◦</sup> 33<sup>′</sup> E ~ 122<sup>◦</sup> 25<sup>′</sup> E) refers to the vast area through which the mainstream and tributaries of the Yangtze River flow, with a drainage area of 1.8 × 10<sup>6</sup> km<sup>2</sup> (Lu et al., 2019) (Fig. 1). It is divided into semi-arid, semi-humid and humid regions from northwest to southeast. The altitude ranges from − 142 m in the east to 7143 m in the west (Lu et al., 2019). The climatic conditions in the Yangtze River basin are complex, and the spatiotemporal distribution of precipitation and temperature are very uneven, with annual average precipitation is approximately 300–2400 mm from west to east of this basin and the average temperature is around 4–24<sup>◦</sup> C. Rainfall is concentrated in May, June and September, and summer drought is prone to occur in this basin from July to August. There are six main crop producing areas in the Yangtze River basin, all of which are China’s main commercial crop bases (Xu et al., 2019). Summer crops in the Yangtze River basin include early rice, cotton, and autumn crops include late rice, winter wheat, and rape. Therefore, it plays an important role in crop production and food security in China. 

### _2.2. Datasets_ 

Three types of data from satellite remote sensing, meteorological observation and statistical yearbook were collected (Table 1). The European Space Agency (ESA) Climate Change Initiative (CCI) released a multi-satellite composite product of global surface soil moisture, which has been widely used in agricultural drought monitoring worldwide (Bontempo et al., 2020; Carrao et al., 2016; Dorigo et al., 2017; Ma et al., ˜ 2021; Zhang et al., 2019b). The long time series products ESA CCI with high spatiotemporal resolution and strict quality control are constantly updating new data. We used in-situ observation soil moisture data to validate the applicability of CCI soil moisture products by Pearson Correlation Coefficient in the entire Yangtze River basin. As a result, the percentages of valid data for active, passive, and combined products are 90.83%, 70.83%, and 95.83%, respectively. The median R of ESA CCI’s active, passive, combined products correlated to in situ data are 0.47, 0.14, and 0.55, respectively, which means that the combined product provides the strongest correlation with the in situ data. Therefore, we chose the combined product in this study. The surface layer (0.5–5 cm) soil moisture with spatial resolution 0.25<sup>◦</sup> ×0.25<sup>◦</sup> can be daily acquired in ESA CCI datasets. The monthly averaged V04.7 version of combined soil moisture data was verified and calculated and there are 2,540 grid pixels in the Yangtze River basin during 1981–2018. 

Precipitation data was collected from the National Climate Center (NCC) of China Meteorological Administration (CMA), which was monthly 0.5<sup>◦</sup> ×0.5<sup>◦</sup> grid point datasets (V2.0), and interpolated into 0.25<sup>◦</sup> by the ArcGIS Kriging interpolation tool. The other seven types of meteorological data, including sunshine duration (h/day), average temperature (<sup>◦</sup> C), average maximum temperature (<sup>◦</sup> C), average minimum temperature (<sup>◦</sup> C), average wind speed (m/s), average vapor pressure (hPa), and average relative humidity (%), were also downloaded from CMA NCC to calculate the monthly average of Reference 

2 

_Catena 209 (2022) 105804_ 

_Q. Tian et al._ 



**Fig. 1.** Location, Subbasin, interested area of the Yangtze River basin. 

**Table 1** 

Datasets used in this study. 

|Date sources|Temporal resolution after processing|Spatial resolution after processing|Variable|Calculation index|Time span|
|---|---|---|---|---|---|
|ESA CCI V04.7|Monthly average|0.25<sup>◦</sup>×0.25<sup>◦</sup>|soil moisture|SMCI|1981.1–2018.12|
|CMA NCC|Monthly average|0.25<sup>◦</sup>×0.25<sup>◦</sup>|precipitation|PCI/SPI|1981.1–2018.12|
|CMA NCC|Monthly average|0.25<sup>◦</sup>×0.25<sup>◦</sup>|seven types of meteorological data|ET0/ECI/SPEI|1981.1–2018.12|
|AVHRR|Monthly|0.25<sup>◦</sup>×0.25<sup>◦</sup>|Vegetation Health Index|VHI|1981.9–2018.12|
|CNKI|Yearly|Province|drought-affected area of crops|–|1984–2018|



Note: PCI, ECI, SMCI are calculated by formula (3) and formula (4) in section 3.3 respectively. 

Crop Evapotranspiration (ET0). This study uses the Penman-Monteith (P-M) formula recommended by the Food and Agriculture Organization of the United Nations as the standard method for calculating ET0 (Allen and Pereira, 1998; Li et al., 2019) and verified it with in-situ evaporation data downloaded from CMA NCC. In order to keep consistence with soil moisture data in spatial resolution, the ET0 data was also interpolated into 0.25<sup>◦</sup> by the ArcGIS Kriging interpolation tool. The above precipitation, and ET0 data were not only used to estimate the lag time between them and soil moisture, but also used to construct CADI and calculate SPI and SPEI indexes during 1981 to 2018. 

The Vegetation Health Index obtained from the National Oceanic and Atmospheric Administration (NOAA) Center for Satellite Applications and Research (https://www.star.nesdis.noaa.gov/smcd/emb/v ci/VH/vh_ftp.php) was used to assist in verifying the effectiveness of CADI on drought monitoring, because it can indicate the vegetation status and was widely used for characterizing drought (Li et al., 2020; Liu and Kogan, 2010; Bento et al., 2018;). The VHI products in the end of month were selected and also resampled to 0.25<sup>◦</sup> during 1981 to 2018. The drought-affected areas of crop in five provinces (Sichuan, Chongqing, Hubei, Hunan, Jiangxi) and drought map were collected 



**Fig. 2.** Procedure of data processing and analysis. 

3 

_Catena 209 (2022) 105804_ 

_Q. Tian et al._ 

from China Rural Statistical Yearbook and China Meteorological Disaster Yearbook from 1984 to 2018 in China National Knowledge Infrastructure (CNKI) respectively, in order to verify the applicability of CADI in monitoring agricultural drought. Drought-affected area of crops refers to the sown area of crops in which the output of crops is reduced by _>_ 10% compared to the normal year due to drought during the year. 

### **3. Methodologies** 

A flowchart of the methodological procedure is presented in Fig. 2. Overall, this study contains three parts: calculation of lag time, calculation and comparison of CADI, CADI performance evaluation. Step 1 is to explore the interpretation rates of meteorological factors to soil moisture change, so as to support step 2 to calculate the lag times of soil moisture to meteorological factors. Step 3 is to calculate CADI based on the lag time, and step four is to compare CADI with SPI, SPEI, VHI and RDI. Steps 5, 6, and 7 are to explore the drought monitoring performance of CADI in the Yangtze River basin from the perspective of temporal, spatial, and agricultural drought. 

### _3.1. Generalized additive models_ 

Generalized additive models (GAM) is a non-parametric or semiparametric regression analysis method (Hastie and Tibshirani, 1986) that can simulate the relationship between the response variable and predictor variables (Huo et al., 2019; Underwood, 2009). This study used GAM to quantify the single-factor or mixed-factor interpretation rates of precipitation and evapotranspiration to soil moisture change. The model equation is as follows: 

_g_ ( _smi_ ) = _β_ 0 + _s_ ( _prei_ ) + _s_ ( _ET_ 0 _i_ ) + _ε_ (1) 

where _i_ is a site or grid point, _s_ is a smooth function for variables, _smi_ refers to the soil moisture (m<sup>3</sup> m<sup>−3</sup> ) at that point, _prei_ refers to the precipitation (mm) at that point, and _ET_ 0 _i_ refers to evapotranspiration (mm) at that point, _ε_ represents the residual error, and _β_ 0 represents the total average response. The GAM analysis was implemented in R language environment. The evaluation indicators including F-test p value, and variance interpretation rate were used. The smaller the value of the former indicator and the larger the value of the latter indicator, the better the model effect, indicating that the predictor variables contributes higher to the response variable. 

### _3.2. Cross wavelet transform_ 

The cross wavelet analysis developed by Friehe et al. (1993), is an effective tool for exploring the correlations between two correlated time series data. It is a new technique combined with the cross spectrum analysis and wavelet transform, and it can preferably examine the linkages between two time series in time–frequency domain (Grinsted et al., 2004; Li et al., 2020). The cross wavelet analysis was used to obtain the time lags of soil moisture-precipitation and soil moisture-ET0 in this study. 

The Cross Wavelet Transform (XWT) of the two time series _xn_ and _yn_ can be defined as _W_<sup>_XY_</sup> = _W_<sup>_X_</sup> _W_<sup>_Y_∗</sup> , where ∗ stands for their complex conjugation. ⃒⃒ _W_<sup>_XY_⃒⃒</sup> represents the cross wavelet energy. The larger value indicates that the two data series have a common high-energy region and are significantly correlated with each other. The complex argument _arg_ ( _W_<sup>_xy_</sup> ) can be regarded as the local relative phase between _xn_ and _yn_ in both time and frequency fields. The 5% confidence level against red noise is exhibited as a thick contour. The relative phase relationship is displayed as an arrow. The horizontal direction to the right indicates that the two signals are in the same phase, and the second variable has positive impact on the first variable in the common period; the downward direction indicates a difference by a quarter period, and the second variable is earlier than the first variable by a quarter period, and the lag 

time is equal to the common period multiplied by the phase relationship (Grinsted et al., 2004). The theoretical distribution of the cross wavelet power with their background power spectra _P_<sup>_X_</sup> _k_<sup>and</sup><sup>_PY_</sup> _k_<sup>was referred to</sup> Torrence and Compo (1998), which is expressed as follows: 



where _Zv_ ( _p_ ) denotes the confidence level associated with the probability _p_ of a probability distribution function which is defined by the square root of the product of two _χ_<sup>2</sup> distributions (Grinsted et al., 2004). 

### _3.3. CADI rationale_ 

Agricultural drought is regarded as a phenomenon of crop yield reduction due to insufficient soil moisture (Mu et al., 2013), so soil moisture is the direct factor in monitoring agricultural drought. According to energy balance and water balance, the magnitude of soil moisture highly depends on the previous precipitation and evapotranspiration (Seneviratne et al., 2010), that is, precipitation supplemented water must be at least equal to the evapotranspiration, otherwise, the insufficient precipitation supplemented water will lead to the net effect of original soil moisture reduction. In addition, the coupling response of soil moisture to precipitation and evapotranspiration has a potential lag time. Therefore, some of the most important natural parameters for monitoring agricultural drought are soil moisture, precipitation, evapotranspiration, and the lag time of soil moisture to previous precipitation and evapotranspiration. 

Based on the interaction and causality of the atmosphere, soil, hydrology, and crop drought, it is also necessary to consider temperature and wind when drought severity assessment. Since the ET0 reflects the comprehensive results of the influence of multiple factors such as sunshine, temperature, wind, and humidity, and ET0 is easy to obtain and it has a good correlation with in-situ evaporation data, the ET0 as a substitute variable was involved in constructing agricultural drought index in this study. In fact, precipitation and potential evapotranspiration have been widely used to construct drought indexes to monitor various types of droughts, such as the Aridity Index proposed by UNEP, RDI (Tsakiris et al., 2007), SPEI, and PDSI. 

Firstly, the precipitation and ET0 were combined to define a primary drought index to characterize basic climatic conditions. The specific definition formula of primary drought index was as follows: 



where, _Di_ represents the local climatic conditions. Larger _Di_ stands for more arid. _PCIj_ and _ECIk_ represent the relative values of precipitation and ET0 in the historical period (1981.1–2018.12), _Pj_ and _Ek_ are precipitation and ET0 in period _j_ and _k_ , respectively, _Pmax, Emax, Pmin, Emin_ refer to the maximum and minimum values of precipitation and ET0 in the study period. The precipitation and ET0 were normalized in above steps to eliminate the impact of different data magnitudes and facilitate the uniformity of drought standards. From the formula’s calculation, both PCI and ECI range from 0 and 1. Higher PCI means less precipitation, while smaller ECI means more ET0, which implies larger possibility of water evapotranspiration from land surface. 

Secondly, since the insufficiency of soil moisture directly causes the agricultural drought that result in crop yields reduction, soil moisture is the direct variable in constructing agricultural drought index. In this study, SMCI was defined as a multiplier factor, and the construction of the CADI was as follows: 

4 

_Catena 209 (2022) 105804_ 

_Q. Tian et al._ 



where SMCI (similar to PCI and ECI) is the relative value of soil moisture relative to the historical period, _SMi_ refer to the soil moisture in period _i_ , _SMmax, SMmin_ refer to the maximum and minimum values of soil moisture in the historical period of that place. SMCI normalizes soil moisture values from 1 (dry conditions) to 0 (wet conditions). SMCI acts as a multiplier factor, it will increase the _Dj_ value (dry conditions) or decrease it (normal or humid conditions). Finally, the results of CADI in Equation (4) were normalized between 0 and 1 to facilitate the selection of the drought threshold. 

The last and most important thing was the choice of the lag time of soil moisture to precipitation and ET0. The lag time of soil moisture to precipitation and ET0 are ( _i_ − _j_ ) and ( _i_ − _k_ ) respectively. According to the method of XWT in Section 3.2, the lag times between soil moisture and precipitation and ET0 can be explored to determine values of ( _i_ − _j_ ) and ( _i_ − _k_ ) . 

### _3.4. Traditional drought indexes_ 

Szalai et al. (2000) pointed out that SPI2-3 has a strong correlation with soil moisture, that is, it has a strong correlation with agricultural drought. Since SPEI not only considers the input of water sources on land, but also the output of water sources on land, it is theoretically more related to agricultural drought. Vicente-Serrano et al. (2012) compared the performance of SPI, SPEI and PDSI in global drought monitoring, and found that SPI and SPEI index are better than PDSI in monitoring agricultural drought, so the SPI and SPEI were chose firstly as reference indexes in this study. The VHI can indicate the vegetation status and was widely used for characterizing agricultural drought (Bento et al., 2018; Liu and Kogan, 2010) by characterizing the health of local vegetation using NDVI and thermal condition which was induced by precipitation and land surface temperature. Tsakiris et al. (2007) once pointed out that water deficit cannot be estimated only on the input (e.g. precipitation) but also on the output variable (water consumption), and they proposed the Reconnaissance Drought Index (RDI) using data of two determinants, precipitation and potential evapotranspiration. So, in this study, four drought indexes, SPI, SPEI, VHI and RDI were utilized to compare with CADI, in order to investigate its performance on drought monitoring. 

The SPI is calculated based on probability distributions of precipitation for particular monthly time scales. It is a meteorological index to normalize precipitation data and show how long a value is away from the mean. The time scaled SPI with 1-, 3- and 12- month was gained by fitting a gamma distribution. Similar to the SPI-1, 3, 12 calculation, the SPEI-1, 3, 12 were calculated by fitting a log-logistic probability density function to the specific frequency distribution of the series of the difference between precipitation and potential evapotranspiration. The shorter the time scale of SPI and SPEI (usually 1-, 3-, 6-, 9-, or 12month), the more the drought indexes’ value moves above and below zero, because the deviation from the mean precipitation of a certain month is expected to be greater than that of one year. The response of soil moisture to precipitation and evapotranspiration may be several months, Szalai et al. (2000) pointed out that SPI with 2- or 3- month scale have a strong correlation with soil moisture, which is used to measure agricultural drought. Therefore, the time scale of 1-, 3- month were chose in this study without 6-, 9- month scale. As for 12-month timescale, because agricultural drought has a hysteresis effect on insufficient precipitation, and we want to choose annual-scale SPI or SPEI to explore the relationship between it and agricultural drought. 

### **4. Results** 

### _4.1. Interpretation rate of meteorological factor to soil moisture change_ 

The interpretation rates of precipitation and ET0 to soil moisture change was calculated by GAM. Fig. 3 showed the single-factor and mixed-factor experimental results for 24 sites in the Yangtze River basin. In single-factor experiment, the predictor variables at almost all sites had a significant impact on soil moisture change at the P _<_ 0.001 significance level. It indicated that each predictor variable alone had a statistical significance. Therefore, GAM can well explain the relationship between multiple predictor variables impacts on the magnitude of soil moisture. Fig. 3(a) showed the interpretation rates of precipitation, ET0, and mixed-factor at each site, and precipitation had the highest interpretation rate, followed by ET0. In addition, the mixed-factor experiment enhanced the interpretation rate of the model. Fig. 3(b) counted the interpretation rates of mixed-factors experiment. At most sites, precipitation and ET0 had a relatively high interpretation rate for explaining soil moisture changes. Therefore, it is necessary to investigate the temporal synchronization between influencing factors and soil moisture, and to explore the early climatic conditions that affect soil moisture. 

### _4.2. Lag time of soil moisture to meteorological factor_ 

The cross wavelet energy spectrum obtained from XWT of soil moisture-precipitation and soil moisture-ET0 at Yunxian and Seda sites were showed in Fig. 4. The temporal relations of soil moistureprecipitation and soil moisture-ET0 had a common period of 8–16 months at Yunxian site (Fig. 4a, 4c), while 4–8 months at Seda site (Fig. 4b, 4d). The phase relationship arrows pointed to the upper right, right and lower right in most of time in the common period, hence, precipitation and ET0 had positive correlations on soil moisture, and they were about 1/8 or 7/8 of the common period earlier than the soil moisture. The lag time is equal to the common period multiplied by the phase relationship (Grinsted et al., 2004). In the period of 8–16 months at Yunxian site, the phase arrows pointed to the upper right and right in most of time, the time lag of 7/8 period was extracted, which implied that soil moisture had a time lag of 7 or 14 months on precipitation and ET0. Within one-year period in a short term, two months was selected as the lag time. In the period of 4–8 months at Seda site, the phase arrows pointed to the lower right and right in most of time, the time lag of 1/8 period was extracted, which implied soil moisture had a time lag of 0.5 or 1 month on precipitation and ET0. Overall, the soil moistureprecipitation and soil moisture-ET0 of the Yunxian site has a lag of 2 months. Seda sites have a lag of 0.5 or 1 month. 

Besides the Yunxian and Seda, the XWT was implemented on more meteorological stations to count the common periods and time lags. The spatial distribution of time lags was shown in Fig. 5. The lag times of soil moisture-precipitation and soil moisture-ET0 are analogous. The lagging time in the northwest arid area (approximately 1-month) is shorter than that in the relatively humid area (approximately 2-month) in the central and eastern Yangtze River basin. Several studies stated the same results that the temporal relationships had regional similarity and the time lag was different at different climate types and catchments (Gevaert et al., 2018; Li et al., 2020; Liu et al., 2020b). Therefore, the interested areas were selected in the semi-arid, semi-humid and humid regions respectively to demonstrate the CADI construction and application. 

### _4.3. Long term CADI in the Yangtze River basin_ 

The monthly CADI of the Yangtze River basin was calculated during 1981–2018 according to section 3.3. The time evolution of the monthly mean values of the input variables (Soil moisture, Precipitation, ET0) of CADI and CADI are shown in Fig. 6. All input variables in semi-arid region were smaller than that in humid region. Precipitation and ET0 

5 

_Catena 209 (2022) 105804_ 

_Q. Tian et al._ 



**Fig. 3.** The (a) single-factor and (b) mixed-factor interpretation rates of precipitation and ET0 to soil moisture change. 



**Fig. 4.** The cross wavelet energy spectrum of soil moisture-precipitation, soil moisture-ET0 at Yunxian site (a, c) and Seda site (b, d). 



**Fig. 5.** The spatial distribution of lag times of soil moisture-precipitation and soil moisture-ET0. 

showed obvious seasonality that they were high in summer and low in spring and winter. As well soil moisture varied seasonally in semi-arid and semi-humid regions, while breakpoints appeared in spring and winter, which may be attribute to the high latitude and soil freezing in plateau. This phenomenon didn’t occur in humid regions, and there was not obvious seasonality. Hence soil moisture using alone is insufficient to monitor drought completely. The ET0 was greater than precipitation in semi-arid areas, which is a major cause of drought. Precipitation and ET0 are similar in semi-humid region, while precipitation is greater than ET0 in most time in humid region. Therefore, whether it is a semi-arid, semi-humid or humid region, it is not sufficient to monitor drought using a variable alone. It is more reasonable to consider multiple variables 

comprehensively. Finally, the CADI also exhibited obvious seasonality and exhibits large fluctuations in all regions, from which drought identification and its grade division can benefit. Consequently, it is robust to monitor drought in different climatic regions using the proposed CADI. 

### _4.4. Correlation of CADI with traditional drought indexes_ 

In order to assess the performance of CADI, the Pearson correlations between monthly CADI and SPI-1, 3, 12, SPEI-1, 3, 12, VHI, and RDI were conducted in semi-arid, semi-humid, humid regions during 1981 to 2018 (Table 2). The correlation coefficient is between 0.1 and 0.51. 

6 

_Catena 209 (2022) 105804_ 

_Q. Tian et al._ 



**Fig. 6.** Comparison between monthly averaged CADI and input variables (soil moisture, precipitation and ET0) in (a) semi-arid, (b) semi-humid, and (c) humid region during 1981–2018. 

**Table 2** 

Pearson coefficient between monthly CADI and SPI-1, 3, 12, SPEI-1, 3, 12, VHI and RDI in semi-arid, semi-humid and humid regions during 1981 to 2018. 

|**R**|**CADI-**|**CADI-**|**CADI-**|**CADI-**|**CADI-**|**CADI-**|**CADI-**|**CADI-**|
|---|---|---|---|---|---|---|---|---|
||**SPI-1**|**SPI-3**|**SPI-12**|**SPEI-1**|**SPEI-3**|**SPEI-12**|**VHI**|**RDI**|
|Semi-arid|−0.2*|−0.39**|−0.46**|−0.17*|−0.44**|−0.51**|−0.51**|−0.26**|
|Semi-humid|−0.28**|−0.39**|−0.29**|−0.1*|−0.37**|−0.25*|−0.12*|−0.38**|
|Humid|−0.22*|−0.35**|−0.24*|−0.42**|−0.50**|−0.26**|−0.18*|−0.48**|



* p-value _<_ 0.05, ** p-value _<_ 0.01. 

CADI is negatively correlated with traditional drought indexes, because the larger the CADI was, the more arid, while the smaller the chosen indexes were, the more arid. Values denoted in red in Table 2 illustrated the most significant correlation between CADI and traditional drought index in different climate regions. Comprehensively considering the correlations in different climate regions, the CADI was significantly correlated to SPEI-3 in all regions. Therefore, the SPEI-3 was selected as a reference index to determine CADI drought threshold standard. 

As China Meteorological Disaster Yearbook records, there were little rainfall and three consecutive summer drought occurred from mid-July to mid-August in southern China during 2007 to 2009. Fig. 6 (c) also showed that it rained less than normal years in humid region. This summer drought covered the southern part of Guizhou province, Hunan province, and Jiangxi province in the Yangtze River basin. As well the drought-affected area of Hunan and Jiangxi provinces increased significantly in 2007 and 2009 which was shown in Fig. 11(d, e) in next section. In addition, since we selected three interest regions, we compared CADI and SPEI3 nine times to determine thresholds of the CADI drought grade division. 

Considering the start time, end time and severity of drought events, the CADI drought thresholds were set as: Normal: 0–0.025, Light: drought: 0.025–0.05, Moderate drought: 0.05–0.075, Heavy drought: 

0.075–0.125, Extreme drought: _>_ 0.125. Table 3 counted the occurrences of mild drought, moderate drought, heavy drought, extreme drought and total occurrences according to SPEI-3 (McKee et al., 1993) and CADI from 2007 to 2009. It should be noted that as long as drought index in a single month reached the threshold, it is regarded as a drought event. Table 3 showed that the occurrence number of each drought grade and the total number of drought occurrences are various in different climate regions. The meteorological drought and agricultural drought occurred closely depending on climate types. There were more meteorological droughts than agricultural droughts in all regions. The start and end of meteorological drought were not synchronous with agricultural drought, which may be due to the multiple factors of underlying surface including water conservation by soil. Therefore, the soil moisture involved index CADI pays more attentions to the identification of agricultural droughts. The soil has a certain function of water storage and reduces the frequency of agricultural droughts (Wu and Dickinson, 2004). Therefore, the advantage of CADI lies in the recognition of agricultural drought, not meteorological drought. 

Because of most crops growth and maturing in summer in the Yangtze River basin, it is important to further investigate the superiority of summer drought with proposed CADI in such a crop phenologyrelated region. Fig. 7 shows the time evolution of the CADI and SPEI-3 

7 

_Catena 209 (2022) 105804_ 

_Q. Tian et al._ 

**Table 3** 

Comparison of drought frequency of different drought grades captured by CADI and SPEI-3 during 2007–2009. 

||**Drought grade**|Light|Moderate|Heavy|Extreme|Total|
|---|---|---|---|---|---|---|
|**Semi-arid region**|**SPEI-3**|−1–0|−1.5–1|−2–1.5|≤-2||
||**Frequency**|6|5|3|0|14|
||**CADI**|0.025–0.05|0.05–0.075|0.075–0.125|_>_0.125||
||**Frequency**|4|4|1|0|9|
|**Semi-humid region**|**SPEI-3**|−1–0|−1.5–1|−2–1.5|≤-2||
||**Frequency**|12|4|3|1|20|
||**CADI**|0.025–0.05|0.05–0.075|0.075–0.125|_>_0.125||
||**Frequency**|10|4|4|0|18|
|**Humid region**|**SPEI-3**|−1–0|−1.5–1|−2–1.5|≤-2||
||**Frequency**|23|3|4|1|31|
||**CADI**|0.025–0.05|0.05–0.075|0.075–0.125|_>_0.125||
||**Frequency**|11|3|4|0|18|





**Fig. 7.** Comparison between monthly CADI and SPEI-3 in (a) semi-arid, (b) semi-humid region, and (c) humid region during 2007–2009. 

values from 2007 to 2009. Fig. 7(a, b, c) illustrate that both CADI and SPEI-3 in time series show an obvious seasonality. The black rectangle in Fig. 7(a, b, c) corresponds to the drought happened during July to August in 2007, 2008 and 2009. Compared with SPEI-3, CADI cannot only identify spring drought and winter drought, but also identify summer droughts more effectively, which is particularly important for the sowing and growth of early rice, cotton, late rice, winter wheat and rapeseed in summer and autumn in the Yangtze River basin. S´anchez et al. (2016) also stated that the traditional drought index is more effective in identifying winter and spring droughts, but summer and autumn droughts are more important for agricultural drought. Our proposed index in this study would be a good solution to this issue. 

In order to evaluate the consistency of CADI and traditional drought indexes in capturing drought grades, the CADI, SPEI, SPI, VHI and RDI were used to monitor droughts and classify drought to different grades based on the determined threshold respectively. The correlation coefficients of the drought grades were then calculated in the Yangtze 

River basin including 3 climate regions and 11 subbasins, which was shown in Fig. 8. In the case of confidence level P _<_ 0.05, the regionally averaged correlation coefficient ranged between 0.5 and 0.7, which shows significant correlations. Therefore, the construction of CADI and its threshold of drought severity division in this study performed well on drought monitoring in the Yangtze River basin. 

### _4.5. Drought monitoring based on CADI in Yangtze River basin_ 

In order to explore the performance of CADI in historical drought monitoring in the Yangtze River basin, the monthly CADI and SPEI-3 were compared in semi-arid, semi-humid, and humid regions during 1981 to 2018 (Fig. 9). The figure shows both CADI and SPEI-3 vary seasonally. The peak of CADI was corresponding to the valley of SPEI-3, at which the most severe drought happened. The sudden change of SPEI3 variation is in line with the characteristics of meteorological drought, while the relatively gentle change trend of CADI variation conforms to 

8 

_Catena 209 (2022) 105804_ 



**Fig. 8.** Pearson correlation coefficient (p _<_ 0.05) between CADI and traditional drought indexes for drought grades in Yangtze River basin. 



**Fig. 9.** Monthly drought grades comparison between CADI and SPEI-3 in (a) semi-arid region, (b) semi-humid region, and (c) humid region during 1981 to 2018. 

9 

_Catena 209 (2022) 105804_ 

_Q. Tian et al._ 

the characteristics of agricultural drought. A period of two consecutive months in which drought indexes reach the threshold of moderate and heavy drought is regarded as a drought event. Consequently, the moderated drought event counted to 10, 14, 11 determined by CADI, while 17, 16, 15 determined by SPEI-3 in semi-arid, semi-humid, and humid regions respectively. As well heavy drought event counted to 5, 9, 3 by CADI, while 9, 11, 5 determined by SPEI-3. The results showed agricultural drought events are less than meteorological drought events in spite of moderated drought and heavy drought. 

In order to comprehensively investigate the spatial characteristic of drought in the Yangtze River basin, the annual mean CADI map was derived during 1981 to 2018, as well as the CADI map in August 2016, and CADI map in spring, summer, autumn and winter in the year of 2016 (Fig. 10). According to the 2016 Statistical Yearbook, in August 2016, certain areas of the Yangtze River Basin experienced different levels of drought. Therefore, this study visualized the spatial distribution of CADI during this period. Fig. 10(a) shows that in the past 38 years, areas with more heavy droughts include the northeast of the Wujiang River basin, the Middle Yangtze River, and the northern and southern Poyang Lake basin, which is consistent with results of Chen et al. (2020). Li et al. (2019) also find that the midstream of the river were most prone to drought events. Fig. 10 (c-f) shows that the summer and autumn droughts in the Yangtze River basin in 2016 were more serious than winter and spring droughts, especially in the Jinsha River basin, Mintuo River basin, and Jialing River basin. The upper and middle reaches of the Yangtze River basin and the Poyang Lake basin have more heavy autumn droughts. In winter (Fig. 10 (c)), the missing data in the northwest of the Yangtze River basin may be due to soil freezing. Spatially continuous droughts occurred in the Mintuo River basin and Jialing River basin from the CADI map in August 2016 (Fig. 10 (b)). The drought conditions shown by CADI in the Yangtze River basin in 2016 are consistent with the meteorological drought recorded in the China Meteorological Disaster Yearbook. 

In order to verify the applicability of CADI in monitoring agricultural drought, the drought-affected area of crops were collect. Droughtaffected area of crops refers to the sown area of crops in which the output of crops is reduced by _>_ 10% compared to the normal year due to drought during the year. We analyzed the similar trend of crop droughtaffected area and CADI, that taking the province as a unit, with a time resolution of one year. To maintain spatiotemporal consistency, we used 

province vector boundaries for mask clipping in ArcGIS. Fig. 11 shows the temporal variation of the annual average of CADI value and the crops drought-affected area value of the five provinces or cities in the Yangtze River basin during 1984 to 2018. In recent years, the droughtaffected area in all provinces has been decreasing year by year, which may benefit from the help of drought-resistant measures. But in general, Fig. 11 shows that the annual average CADI of these five administrative regions has a similar trend to the crops drought-affected area value. Years with a larger drought-affected area value have a larger CADI value, which means drier. This trend also shows the feasibility of applying CADI drought index for agricultural drought in the Yangtze River basin. 

### **5. Discussion** 

### _5.1. Effects of time asynchrony between meteorology and soil moisture on drought assessment_ 

Soil moisture data were commonly used to construct agricultural drought index (Liu and Sun, 2020; Liu, et al., 2016; Ma et al., 2021; Martínez-Fernandez et al., 2015; S´ anchez et al., 2016; Souza et al., 2020; ´ Wang et al., 2018; Yin et al., 2018), which proved that it was more suitable for the drought index integrating soil moisture to identify agricultural drought than traditional meteorological drought indexes. This study revealed the time asynchrony between soil moisture and meteorological factors, which is the basis of CADI proposed. The precipitation and ET0 had good interpretation rates for soil moisture for different regions which exhibited various lag times. The lag timeintegrated multi-factor experiments by GAM analysis increased the interpretation rates from 27.8% to 32.4%, 53.2% to 53.8%, and 43% to 50%, respectively in three different climatic regions. Therefore, the time lag significantly affected on drought assessment when meteorology and soil moisture were simultaneously involved in drought index construction. The results were in accord with the research (Gevaert et al., 2018; Li et al., 2020; Liu et al., 2020b), which stated that the temporal relationship has regional similarity and the time lags vary in different climatic regions. 

Particularly in the Yangtze River basin, the CADI identified drought in this study generally agreed to previous studies (Chen et al., 2020; Huang et al., 2021; Li et al., 2020; Li et al., 2020; Xu et al., 2019; Zhu and 



**Fig. 10.** The spatial distribution pattern of CADI in the Yangtze River basin. (a) annual mean during 1981–2018, (b)august 2016, and (c) winter, (d) spring, (e) summer, and (f) autumn in 2016. 

10 

_Catena 209 (2022) 105804_ 

_Q. Tian et al._ 



**Fig. 11.** Comparisons between CADI and crop drought-affected area in (a) Sichuan Province, (b) Chongqing City, (c) Hubei Province, (d) Hunan Province, (e) Jiangxi Province during 1984 to 2018. 

Wang, 2001). The agricultural drought in the Yangtze River basin is characterized by summer drought in terms of temporal aspect, which is consistent with the drought characteristics of July to September 2007–2009. The drought coverage identified by the 38-year CADI average value was similar to results of Chen et al. (2020) and Li et al. (2019). 

From the perspective of different kinds of droughts, hysteresis effect of soil moisture to meteorology means meteorological drought may earlier than agricultural drought, which was supported by many studies (Aghelpour et al., 2021; Gevaert et al., 2018; Li et al., 2020; Li et al., 2014; Liu and Sun, 2020; Mahmud et al., 2021). Therefore, the meteorological drought index cannot be used directly for agricultural drought monitoring, which explained the differences between CADI-identified agricultural drought and SPEI-identified meteorological drought. However, CADI-identified drought region was consistent with the trend of drought-affected area of crops, so CADI was more suitable for monitoring agricultural drought. 

### _5.2. Implication for regional drought monitoring_ 

When the CADI construction, the ratio of precipitation to evapotranspiration was taken as the previous climatic conditions, which means that the water supplemented by precipitation must be at least equal to the evapotranspiration, otherwise it will lead to the net effect of original soil moisture reduction. Because of the memory function of soil moisture (Koster and Suarez, 2001; Wu and Dickinson, 2004), the lag response of vegetation to insufficient precipitation led to agriculture drought temporally lagging to meteorological drought (Zhao et al., 2018), which implied that we had to protect enough forest and luxuriant pasture to conserve water in the soil, so as to resistant long time insufficient precipitation. This study found that the time differences between soil moisture and meteorological factors was the available time to prevent drought during agricultural production. Therefore, the water storage of reservoirs and lakes in the wet season and the guarantee of irrigation for agricultural production are scientific measures to prevent agricultural drought. 

sufficient to reflect the real situation of agricultural drought. To reflect the feedback of time lag effects in drought monitoring, a novel Comprehensive Agricultural Drought Index (CADI) was constructed based on study of the time lag effects on soil moisture to meteorological factors in Yangtze River basin. The impacts of meteorological factors on soil moisture were investigated using GAM and cross wavelet transform methods. Soil moisture change was more dependent on variation in precipitation, and exhibited different lagging times to meteorological factors in different regions. There is one month lagged in the northwest of the Yangtze River basin, while two months lagged in middle and east of basin. Based on above these time lag effects, the monthly CADI was calculated during 1981 to 2018. The Pearson correlation analysis was conducted between CADI and SPI-1, 3, 12, SPEI-1, 3, 12, and VHI. The CADI was negatively correlated with these traditional drought indexes, among which the SPEI-3 was most strongly correlated to it with a maximum correlation coefficient of − 0.5. Referring to the drought grades division by SPEI-3, the drought grades thresholds were determined to CADI, which were applied in monitoring agricultural drought in the entire Yangtze River basin. The Pearson correlations of drought severity were calculated between CADI and SPI-1, 3, 12, SPEI-1, 3, 12, and VHI, and they all had strong positive correlations with the correlation coefficients between 0.5 and 0.7, which implied that the CADI was sensitive to capture the temporal variation and spatial pattern of agriculture drought. The CADI was investigated during the period of 2007–2009 when drought occurred significantly. From the perspective of drought capturing performance in seasonal scale, CADI has more advantages in monitoring summer drought in the Yangtze River basin, which is more significant for crop phenology related agricultural drought. By comparing the drought-affected area of crops and meteorological drought in the year of 2016, CADI has good applicability for agricultural drought in terms of temporal evolution and spatial distribution pattern in the Yangtze River basin. The drought index proposed in this study is more accurate in monitoring agricultural drought, which will be helpful for real-time agricultural drought monitoring and disaster management. 

### **6. Conclusions** 

In the context of climate change, soil moisture and meteorological factors have complex responses and feedback relationships. The drought index based on a single variable or synchronous variables is not 

### **Declaration of Competing Interest** 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

11 

_Catena 209 (2022) 105804_ 

_Q. Tian et al._ 

### **Acknowledgements** 

This work was funded by the National Key Research and Development Program (2018YFC1506506), the Frontier Project of Applied Foundation of Wuhan (2019020701011502), the Natural Science Foundation of Hubei Province (2019CFB736), Key Research and Development Program of Jiangxi Province (20201BBG71002), and the LIESMARS Special Research Funding. 

### **References** 

- AghaKouchak, A., Farahmand, A., Melton, F.S., Teixeira, J., Anderson, M.C., Wardlow, B. D., Hain, C.R., 2015. Remote sensing of drought: progress, challenges and opportunities. Rev. Geophys. 53 (2), 452–480. https://doi.org/10.1002/ 2014RG000456. 

- Aghelpour, P., Kisi, O., Varshavian, V., 2021. Multivariate drought forecasting in shortand long-term horizons using MSPI and data-driven approaches. J. Hydrol. Eng. 26, 040210064. https://doi.org/10.1061/(ASCE)HE.1943-5584.0002059. 

- Allen, R.G., Pereira, L.R.D., 1998. Crop evapotranspiration: guidelines for computing 

crop water requirement. United Nations Food and Agriculture Organization, Rome, Italy. 

- Bento, V.A., Gouveia, C.M., DaCamara, C.C., Trigo, I.F., 2018. A climatological assessment of drought impact on vegetation health index. Agric. For. Meteorol. 259, 286–295. https://doi.org/10.1016/j.agrformet.2018.05.014. 

- Bojinski, S., Verstraete, M., Peterson, T.C., Richter, C., Simmons, A., Zemp, M., 2014. The concept of essential climate variables in support of climate research, applications, and policy. Bull. Am. Meteorol. Soc. 95 (9), 1431–1443. https://doi.org/10.1175/ BAMS-D-13-00047.1. 

- Bolten, J.D., Crow, W.T., Zhan, X., Jackson, T.J., Reynolds, C.A., 2010. Evaluating the utility of remotely sensed soil moisture retrievals for operational agricultural drought monitoring. IEEE J. Sel. Top. Appl. Earth Obs. Remote Sens. 3 (1), 57–66. https://doi.org/10.1109/JSTARS.2009.2037163. 

- Bontempo, E., Dalagnol, R., Ponzoni, F., Valeriano, D., 2020. Adjustments to SIF Aid the interpretation of drought responses at the Caatinga of northeast Brazil. Remote Sens. 12 (19), 3264. https://doi.org/10.3390/rs12193264. 

- Carrao, H., Russo, S., Sepulcre-Canto, G., Barbosa, P., 2016. An empirical standardized ˜ soil moisture index for agricultural drought assessment from remotely sensed data. Int. J. Appl. Earth Observ. Geoinform. 48, 74–84. https://doi.org/10.1016/j. jag.2015.06.011. 

- Chen, S., Zhang, L., Zhang, Y., Guo, M., Liu, X., 2020. Evaluation of Tropical Rainfall Measuring Mission (TRMM) satellite precipitation products for drought monitoring over the middle and lower reaches of the Yangtze River Basin China. J. Geograph. Sci. 30 (1), 53–67. https://doi.org/10.1007/s11442-020-1714-y. 

- Dai, A., 2011. Drought under global warming: a review. Wiley Interdiscip. Rev. Clim. Change 2 (1), 45–65. https://doi.org/10.1002/wcc.81. 

- Dorigo, W., Wagner, W., Albergel, C., et al., 2017. ESA CCI soil moisture for improved earth system understanding: state-of-the art and future directions. Remote Sens. Environ. 203, 185–215. https://doi.org/10.1016/j.rse.2017.07.001. 

- Dracup, J.A., Lee, K.S., Paulson, E.G., 1980. On the definition of droughts. Water Resour. Res. 2 (16), 297–302. https://doi.org/10.1029/WR016i002p00297. 

- Du, J., Kimball, J.S., Velicogna, I., Zhao, M., Jones, L.A., Watts, J.D., Kim, Y., 2019. Multicomponent satellite assessment of drought severity in the contiguous United States from 2002 to 2017 using AMSR-E and AMSR2. Water Resour. Res. 55 (7), 5394–5412. https://doi.org/10.1029/2018WR024633. 

Friehe, C.A., Mayer, M.E., Hudgins, L., 1993. Wavelet transforms and atmopsheric turbulence. Phys. Rev. Lett. 71 (20), 3279–3282. https://doi.org/10.1103/ PhysRevLett.71.3279. 

- Gevaert, A.I., Veldkamp, T.I.E., Ward, P.J., 2018. The effect of climate type on timescales of drought propagation in an ensemble of global hydrological models. Hydrol. Earth Syst. Sci. 22 (9), 4649–4665. https://doi.org/10.5194/hess-22-4649-2018. 

Grinsted, A., Moore, J.C., Jevrejeva, S., 2004. Application of the cross wavelet transform and wavelet coherence to geophysical time series. Nonlinear Processes Geophys. 11 (5–6), 561–566. https://doi.org/10.5194/npg-11-561-2004. 

- Gupta, V., Jain, M.K., 2021. Unravelling the teleconnections between ENSO and dry/wet conditions over India using nonlinear Granger causality. Atmos. Res. 247, 105168 https://doi.org/10.1016/j.atmosres.2020.105168. 

- Hao, Z., AghaKouchak, A., 2013. Multivariate Standardized Drought Index: A parametric multi-index model. Adv. Water Resour. 57, 12–18. https://doi.org/10.1016/j. advwatres.2013.03.009. 

- Hastie, T., Tibshirani, R., 1986. Generalized Additive Models. Statist. Sci. 1 (3), 297–310. https://doi.org/10.1214/ss/1177013604. 

- Heim, R.R., 2002. A review of twentieth century drought indices used in the United States. Bull. Am. Meteorolog. Soc., 83 (8), 1149-1165. 

- Hillel, D., 1998. Environmental Soil Physics. Academic Press, San Diego. 771 pp. 

- Huang, L., Zhou, P., Cheng, L., Liu, Z., 2021. Dynamic drought recovery patterns over the Yangtze River Basin. CATENA 201, 105194. https://doi.org/10.1016/j. catena.2021.105194. 

Huang, S., Chang, J., Leng, G., Huang, Q., 2015. Integrated index for drought assessment based on variable fuzzy set theory: A case study in the Yellow River basin, China. J. Hydrol. 527, 608–618. https://doi.org/10.1016/j.jhydrol.2015.05.032. 

- Huo, S., He, Z., Ma, C., Zhang, H., Xi, B., Zhang, J., Li, X., Wu, F., Liu, H., 2019. Spatiotemporal impacts of meteorological and geographic factors on the availability of 

nitrogen and phosphorus to algae in Chinese lakes. J. Hydrol. 572, 380–387. https:// doi.org/10.1016/j.jhydrol.2019.03.010. 

Jones, A.R., Brunsell, N.A., 2009. A scaling analysis of soil moisture-precipitation interactions in a regional climate model. Theor. Appl. Climatol. 98 (3–4), 221–235. https://doi.org/10.1007/s00704-009-0109-x. 

- Kao, S., Govindaraju, R.S., 2010. A copula-based joint deficit index for droughts. J. Hydrol. 380 (1–2), 121–134. https://doi.org/10.1016/j.jhydrol.2009.10.029. 

- Koster, R.D., Suarez, M.J., 2001. Soil moisture memory in climate models. 

   - J. Hydrometeorol. 2 (6), 558–570. https://doi.org/10.1175/1525-7541(2001) 002 _<_ 0558:SMMICM _>_ 2.0.CO;2. 

- Li, R., Chen, N., Zhang, X., Zeng, L., Wang, X., Tang, S., Li, D., Niyogi, D., 2020. Quantitative analysis of agricultural drought propagation process in the Yangtze River Basin by using cross wavelet analysis and spatial autocorrelation. Agric. For. Meteorol. 280, 107809 https://doi.org/10.1016/j.agrformet.2019.107809. 

- Li, R., Tsunekawa, A., Tsubo, M., 2014. Index-based assessment of agricultural drought in a semi-arid region of Inner Mongolia. China. J. Arid Land 6 (1), 3–15. https://doi. org/10.1007/s40333-013-0193-8. 

- Li, X., Sha, J., Wang, Z., 2019. Comparison of drought indices in the analysis of spatial and temporal changes of climatic drought events in a basin. Environ. Sci. Pollut. Res. 26 (11), 10695–10707. https://doi.org/10.1007/s11356-019-04529-z. 

- Liu, L., Gudmundsson, L., Hauser, M., Qin, D., Li, S., Seneviratne, S.I., 2020a. Soil moisture dominates dryness stress on ecosystem production globally. Nat Commun 11 (1), 4892. https://doi.org/10.1038/s41467-020-18631-1. 

- Liu, M, Sun, A.Y., 2020. A physical agricultural drought index based on root zone water availability: model development and application. Geophys. Res. Lett., 47, e2020GL08855322, Doi: 10.1029/2020GL088553. 

- Liu, Q., Ma, X., Yan, S., Liang, L., Pan, J., Zhang, J., 2020b. Lag in hydrologic recovery following extreme meteorological drought events: implications for ecological water requirements. Water 12 (3), 837. https://doi.org/10.3390/w12030837. 

- Liu, W.T., Kogan, F., 2010. Monitoring Brazilian soybean production using NOAA/ AVHRR based vegetation condition indices. Int. J. Remote Sens. 23 (6), 1161–1179. https://doi.org/10.1080/01431160110076126. 

- Liu, X., Zhu, X., Pan, Y., Li, S., Liu, Y., Ma, Y., 2016. Agricultural drought monitoring: Progress, challenges, and prospects. J. Geog. Sci. 26 (6), 750–767. https://doi.org/ 10.1007/s11442-016-1297-9. 

- Liu, X., Zhu, X., Zhang, Q., Yang, T., Pan, Y., Sun, P., 2020c. A remote sensing and artificial neural network-based integrated agricultural drought index: Index development and applications. CATENA 186, 104394. https://doi.org/10.1016/j. catena.2019.104394. 

- Lu, J., Chen, X., Zhang, L., Sauvage, S., S´anchez-P´erez, J.M., 2018. Water balance assessment of an ungauged area in Poyang Lake watershed using a spatially distributed runoff coefficient model. J. Hydroinformatics 20 (5), 1009–1024. https://doi.org/10.2166/hydro.2018.017. 

- Lu, J., Liu, Z., Liu, W., Chen, X., Zhang, L., 2020. Assessment of CFSR and CMADS Weather Data for Capturing Extreme Hydrologic Events in the Fuhe River Basin of the Poyang Lake. J. Am. Water Resour. Assoc. 56 (5), 917–934. https://doi.org/ 10.1111/1752-1688.12866. 

- Lu, J., Zhang, L., Cui, X., Zhang, P., Chen, X., Sauvage, S., S´anchez-P´erez, J.M., 2019. Assessing the climate forecast system reanalysis weather data driven hydrological model for the Yangtze river basian in China. Appl. Ecol. Environ. Res. 17 (2), 3615–3632. https://doi.org/10.15666/aeer/1702_36153632. 

- Ma, S., Zhang, S., Wang, N., Huang, C., Wang, X., 2021. Prolonged duration and increased severity of agricultural droughts during 1978 to 2016 detected by ESA CCI SM in the humid Yunnan Province Southwest China. CATENA 198, 105036. https:// doi.org/10.1016/j.catena.2020.105036. 

- Martínez-Fern´andez, J., Gonzalez-Zamora, A., S´ anchez, N., Gumuzzio, A., 2015. A soil ´ water based index as a suitable agricultural drought indicator. J. Hydrol. 522, 265–273. https://doi.org/10.1016/j.jhydrol.2014.12.051. 

- Mahmud, T., et al., 2021. Drought dynamics of Northwestern Teesta Floodplain of Bangladesh: a remote sensing approach to ascertain the cause and effect. Environ. Monit. Assess. 193 (4), 218. https://doi.org/10.1007/s10661-021-09005-1. 

- McCabe, G.J., Wolock, D.M., 2020. Multi-year hydroclimatic droughts and pluvials across the conterminous United States. Int. J. Climatol. https://doi.org/10.1002/ joc.6925. 

- McKee, T.B., Doesken, N.J., Kleist, J., 1993. The relationship of drought frequency and duration to time scales. In: Proceedings of the 8th Conference on Applied 

   - Climatology, pp. 179–183. 

- Mishra, A.K., Singh, V.P., 2010. A review of drought concepts. J. Hydrol. 391 (1–2), 202–216. https://doi.org/10.1016/j.jhydrol.2010.07.012. 

- Mu, Q., Zhao, M., Kimball, J.S., McDowell, N.G., Running, S.W., 2013. A remotely sensed global terrestrial drought severity index. Bull. Am. Meteorol. Soc. 94 (1), 83–98. https://doi.org/10.1175/BAMS-D-11-00213.1. 

- Palmer, W., 1965. Meteorological drought, vol. 30. US Department of Commerce. Weather Bureau, Washington, DC. 

- Salvador, C., Nieto, R., Linares, C., Diaz, J., Alves, C.A., Gimeno, L., 2021. Drought effects on specific-cause mortality in Lisbon from 1983 to 2016: risks assessment by gender and age groups. Sci. Total Environ. 751, 142332 https://doi.org/10.1016/j. scitotenv.2020.142332. 

- S´anchez, N., Gonzalez-Zamora, ´ A., Piles, M., Martínez-Fern<sup>´</sup> ´andez, J., Roy, P.S., Thenkabail, P.S., 2016. A new Soil Moisture Agricultural Drought Index (SMADI) integrating MODIS and SMOS products: A case of study over the Iberian Peninsula. Remote Sensing 8 (4), 287. https://doi.org/10.3390/rs8040287. 

- Sattar, M.N., Kim, T., 2018. Probabilistic characteristics of lag time between meteorological and hydrological droughts using a Bayesian model. Terrestrial, Atmos. Oceanic Sci. 29 (6), 709–720. https://doi.org/10.3319/TAO.2018.07.01.01. 

12 

_Catena 209 (2022) 105804_ 

_Q. Tian et al._ 

- Seneviratne, S.I., Corti, T., Davin, E.L., Hirschi, M., Jaeger, E.B., Lehner, I., Orlowsky, B., Teuling, A.J., 2010. Investigating soil moisture–climate interactions in a changing climate: A review. Earth Sci. Rev. 99 (3–4), 125–161. https://doi.org/10.1016/j. earscirev.2010.02.004. 

- Souza, A.G.S.S., Ribeiro Neto, A., Souza, L.L.D., 2020. Soil moisture-based index for agricultural drought assessment: SMADI application in Pernambuco State-Brazil. Remote Sens. Environ. 252, 112124 https://doi.org/10.1016/j.rse.2020.112124. 

- Szalai, S., Szinell, C., Zoboki, J., 2000. Drought monitoring in Hungary. Early Warning 

   - Syst. Drought Pre-paredness Drought Manage. 57, 182–199. 

- Torrence, C., Compo, G.P., 1998. A Practical Guide to Wavelet Analysis. Bull. Am. Meteorol. Soc. 79 (1), 61–78. https://doi.org/10.2307/26215040. 

- Tsakiris, G., Pangalou, D., Vangelis, H., 2007. Regional Drought Assessment Based on the Reconnaissance Drought Index (RDI). Water Resour. Manage. https://doi.org/ 10.1007/s11269-006-9105-4. 

- Underwood, F.M., 2009. Describing long-term trends in precipitation using generalized additive models. J. Hydrol. 364 (3–4), 285–297. https://doi.org/10.1016/j. jhydrol.2008.11.003. 

- Vicente-Serrano, S.M., Begueria, S., Lopez-Moreno, J.I., 2010. A Multiscalar Drought Index Sensitive to Global Warming: The Standardized Precipitation Evapotranspiration Index. J. Clim. 23 (7), 1696–1718. https://doi.org/10.1175/ 2009JCLI2909.1. 

- Vicente-Serrano, S.M., Vicente-Serrano, S., Beguería, S., Lorenzo-Lacruz, J., Camarero, J. J., Lopez-Moreno, J.I., Azorin-Molina, C., Revuelto, J., Mor´ an-Tejeda, E., Sanchez- ´ Lorenzo, A., 2012. Performance of Drought Indices for Ecological, Agricultural, and Hydrological Applications. Earth Interact 16 (10), 1–27. https://doi.org/10.1175/ 2012EI000434.1. 

- Wang, S., Mo, X., Hu, S., Liu, S., Liu, Z., 2018. Assessment of droughts and wheat yield loss on the North China Plain with an aggregate drought index (ADI) approach. Ecol. Ind. 87, 107–116. https://doi.org/10.1016/j.ecolind.2017.12.047. 

- Wu, W., Dickinson, R.E., 2004. Time scales of layered soil moisture memory in the context of land-atmosphere interaction. J. Clim. 17 (14), 2752–2764. https://doi. org/10.1175/1520-0442(2004)017 _<_ 2752: TSOLSM _>_ 2.0.CO;2. 

- Xu, X., Hu, H., Tan, Y., Yang, G., Zhu, P., Jiang, B., 2019. Quantifying the impacts of climate variability and human interventions on crop production and food security in the Yangtze River Basin, China, 1990–2015. Sci. Total Environ. 665, 379–389. https://doi.org/10.1016/j.scitotenv.2019.02.118. 

- Yin, J., Zhan, X., Hain, C.R., Liu, J., Anderson, M.C., 2018. A method for objectively integrating soil moisture satellite observations and model simulations toward a blended drought index. Water Resour. Res. 54 (9), 6772–6791. https://doi.org/ 10.1029/2017WR021959. 

- Zhang, L., Chen, X., Lu, J., Fu, X., Zhang, Y., Liang, D., Xu, Q., 2019a. Precipitation projections using a spatiotemporally distributed method: a case study in the Poyang Lake watershed based on the MRI-CGCM3. Hydrol. Earth Syst. Sci. 23 (3), 1649–1666. https://doi.org/10.5194/hess-23-1649-2019. 

- Zhang, L., Liu, Y., Ren, L., Jiang, S., Yang, X., Yuan, F., Wang, M., Wei, L., 2019b. Drought monitoring and evaluation by ESA CCI soil moisture products over the Yellow River Basin. IEEE J. Sel. Top. Appl. Earth Obs. Remote Sens. 12 (9), 3376–3386. https://doi.org/10.1109/JSTARS.2019.2934732. 

- Zhao, A., Zhang, A., Cao, S., Liu, X., Liu, J., Cheng, D., 2018. Responses of vegetation productivity to multi-scale drought in Loess Plateau, China. CATENA 163, 165–171. https://doi.org/10.1016/j.catena.2017.12.016. 

- Zhao, J., Huang, S., Huang, Q., Wang, H., Leng, G., Fang, W., 2020. Time-lagged response of vegetation dynamics to climatic and teleconnection factors. CATENA 189, 104474. https://doi.org/10.1016/j.catena.2020.104474. 

- Zhu, J., Wang, S., 2001. 80a-oscillation of summer rainfall over the east part of China and East-Asian Summer Monsoon. Adv. Atmos. Sci. 18 (5), 1043–1051. 

13 

