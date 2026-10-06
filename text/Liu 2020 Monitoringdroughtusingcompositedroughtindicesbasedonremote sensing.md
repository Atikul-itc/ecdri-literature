

# **Rapid #: -27620948** 

CROSS REF ID: **896745** 

LENDER: **CLA (CSU Los Angeles) :: Main Library** 

BORROWER: **IRU (New Mexico State University) :: Main Library** 

TYPE: Article CC:CCL JOURNAL TITLE: Science of the total environment USER JOURNAL TITLE: Science of the total environment. ARTICLE TITLE: Monitoring drought using composite drought indices based on remote sensing ARTICLE AUTHOR: Liu, Liu Qi VOLUME: 711 ISSUE: MONTH: 4 YEAR: 2020 PAGES: 134585 ISSN: 0048-9697 OCLC #: 39284343 Processed by RapidX: 10/5/2026 12:25:13 PM This material may be protected by copyright law (Title 17 U.S. Code) 

Science of the Total Environment 711 (2020) 134585 



Contents lists available at ScienceDirect 

## Science of the Total Environment 

journal homepage: www.elsevier.com/locate/scitotenv 



### Monitoring drought using composite drought indices based on remote sensing 



#### Qi Liu<sup>a</sup> , Sha Zhang<sup>a</sup> , Hairu Zhang<sup>c</sup> , Yun Bai<sup>a,⇑</sup> , Jiahua Zhang<sup>a,b,⇑</sup> 

> a College of Computer Science and Technology, Excellent Research Center of Space Information and Earth Big Data, Qingdao University, Shandong, 266071, China 

> b University of Chinese Academy of Sciences, Beijing, 100049, China 

> c College of Business, Qingdao University, Shandong, 266071, China 

##### h i g h l i g h t s 

##### g r a p h i c a l a b s t r a c t 

- The multivariable linear regression was uses to establish composite drought indices. 

- Mediator and moderator variables were introduced to optimize the regression model. 

- MCDI-1 and MCDI-9 were good indicators for meteorological and agricultural drought. 



##### a r t i c l e i n f o 

##### a b s t r a c t 

Article history: Received 14 May 2019 Received in revised form 11 September 2019 Accepted 19 September 2019 Available online 22 November 2019 Ralf Ludwig 

Keywords: Drought Multivariable linear regression MCDIs SPEI Shandong Province 

Drought is one of the most frequent disasters occurring in North China and has a great influence on agriculture, ecology and economy. To monitor drought of typical dry areas in North China, Shandong Province, this paper proposed composite drought indices using multivariable linear regression (MCDIs) to integrate Tropical Rainfall Measuring Mission (TRMM) derived precipitation, Global Land Data Assimilation System Version 2.1 (GLDAS-2.1) derived soil moisture, Moderate Resolution Imaging Spectroradiometer (MODIS) derived land surface temperature (LST) and normalized difference vegetation index (NDVI) from 2013 to 2017 (March to September). Pearson correlation analyses were performed between single remote sensing drought indices and in-situ drought indices, standardized precipitation evapotranspiration index (SPEI), in different time scales to assess the capability of single indices over Shandong Province. The multivariable linear regression method was used to established MCDIs, and mediator and moderator variables were introduced to optimize the model. The correlation coefficients (r) between MCDIs and SPEIs was higher than that between each single index and SPEIs. Additionally, when we investigate the correlations of different MCDIs with both standardized precipitation index (SPI) and moisture index (MI), the highest r values with both 1-month SPI and MI were acquired by the MCDI based on 1-month SPEI (MCDI-1). This suggested MCDI-1 was suitable to monitor meteorological drought. Also, the comparison between MCDI based on 9-month SPEI (MCDI-9) and soil moisture showed MCDI-9 was a good indicator for agricultural drought. Therefore, multivariable linear regression and MCDIs were recommended to be an effective method and indices for monitoring drought across Shandong Province and similar areas. 

� 2019 Elsevier B.V. All rights reserved. 

> ⇑ Corresponding authors. 

> E-mail addresses: sealiuqi@163.com (Q. Liu), zhangsha@qdu.edu.cn (S. Zhang), zhanghairu165@163.com (H. Zhang), byron506@126.com (Y. Bai), zhangjh_radicas@163. com (J. Zhang). 

> https://doi.org/10.1016/j.scitotenv.2019.134585 

> 0048-9697/� 2019 Elsevier B.V. All rights reserved. 

Q. Liu et al. / Science of the Total Environment 711 (2020) 134585 

2 

###### 1. Introduction 

Drought, a natural phenomenon that occurs at multiple time scales and affects large areas and every part of the hydrological cycle, is a recurring extreme event causing great harm to agricultural production and society (Mishra and Singh, 2010; Wu et al., 2018; Liu et al.,2019). Owing to global warming, droughts have been occurring more frequently over expanding areas in recent years, especially in semi-arid regions of the northern hemisphere (Yao et al., 2018; Dai, 2013; Liu et al., 2015; Wagner et al., 1999). Droughts have been classified into meteorological, agricultural, hydrological, and socioeconomic droughts (Liu et al., 2018; Wilhite and Glantz, 1985). Shandong is one of the largest agricultural provinces in North China, and since the late 1990s, it has been increasingly influenced by drought (Zhou et al., 2017; Wang et al., 2017). The increase in the frequency and severity of drought have adversely affected water resources, agricultural production and economic development across Shandong Province (Wang et al., 2016; Zhang et al., 2016; Piao et al., 2010). 

Many in-situ drought indices can effectively monitor drought, such as moisture index (MI) (Thornthwaite et al., 1955), palmer drought severity index (PDSI) (Palmer, 1965), standardized precipitation index (SPI) (McKee et al., 1993), standardized precipitation evapotranspiration index (SPEI) (Vicente-Serrano et al., 2010) and so on. MI is widely used in the evaluation of climate dry and wet conditions (Willmott and Feddema, 1992). PDSI, as a milestone in meteorology, was successful in quantifying the severity of longterm droughts for a given location and time, but it was unsatisfactory for solving short-term problems and inconsistent comparisons between different climatological regions (Guttman, 1998; Zhao et al.,2017). To address these two problems, SPI and SPEI were developed. Their simple computation and good adaptability to various climates allowed them to be more widely applied in drought monitoring studies than PDSI (Guo et al., 2018). However, as a regional event, drought needs to be monitored not only on a site scale but also over space, and the levels of spatial detail of insitu drought indices are affected by the density and the distribution of the site network (Kogan 1997; Anderson et al., 2011; Hao et al., 2015). Remote sensing data can systematically and continuously provide information such as vegetation and water cycles, so remote sensing drought indices can overcome the shortcomings of in-situ drought indices and be applied to monitor drought in space (Xu et al., 2018). 

In recent years, a series of indices derived from remote sensing data have been used to detect drought events (AghaKouchak et al., 2015), and the Normalized Difference Vegetation Index (NDVI) (Rouse et al., 1974) is the most widely used remote sensing index. Referring to NDVI, some drought indicators have been developed, such as Anomaly Vegetation Index (AVI) (Weiying et al., 1994), the Vegetation Condition Index (VCI) (Kogan, 1990, 1995a, 1995b; Liu and Kogan, 1996). NDVI is also used in some models to estimate gross primary productivity (GPP) and the fraction of absorbed photosynthetically active radiation (FPAR) and so on (Bai et al.,2018; Dong et al., 2015). These vegetation index-based drought indices can reflect the reduction in leaf area and chloro- 

phyll of plants attacked by drought. Moreover, the land surface temperature (LST)-based temperature condition index (TCI), precipitation-based precipitation condition index (PCI) and soil moisture-based soil moisture condition index (SMCI) are also useful for monitoring the duration and impact of drought (Kogan, 1995a; Zhang and Jia, 2013; Rhee et al.2010). 

Due to the diversified causes of drought, many composite drought indices were developed to monitor drought conditions by combining single remote sensing drought indices, such as PCI, SMCI, VCI, TCI and so on. Table 1 summarizes several commonly composite drought indices (more than two variables). Rhee et al. (2010) designed a composite drought index, the scaled drought condition index (SDCI), through integrate VCI, PCI and TCI with different percentage to monitor agricultural drought in the North and South Carolina of the United State. The microwave integrated drought index (MIDI) was established by Zhang and Jia (2013), based on multi-sensor microwave indices TCI, PCI and SMCI, to detect short-term especially meteorological drought distribution in North China. In addition, many composite drought indices were proposed, such as the synthesized drought index (SDI) (Du et al., 2013), the optimized drought indices (ODIs) (Hao et al., 2015), the multivariate drought index (MDI) (Rajsekhar et al., 2015), the process-based accumulated drought index (PADI) (Zhang et al., 2017) and so on. These combined drought indices have achieved the results expected by researchers. 

However, the effectiveness of these indices with regard to drought monitoring are region-dependent, and many of these indices may not be sufficient to capture the role of single variables in the formation of drought. Therefore, we used the multivariable linear regression method and introduced mediator and moderator variables to build composite drought indices (MCDIs) by integrating precipitation, land surface temperature, soil moisture, and vegetation data to analyze the drought in Shandong. 

The main objectives of this study are: 1) to assess the capability of single remote sensing indices in monitoring drought; 2) to establish MCDIs on 1-, 3-, 6- and 9-month SPEI (MCDI-1, MCDI-3, MCDI-6 and MCDI-9) and compare the correlation coefficients between composite indices and SPEIs with that between single indices and SPEIs; 3) to verify the ability of MCDIs in monitoring meteorological drought and agricultural drought; 4) to investigate drought condition by MCDIs in Shandong Province over space and time. 

###### 2. Study area, data and methodology 

###### 2.1. Study area 

The study area, Shandong Province, is located in the east coast of China, covering the area 34�22<sup>0</sup> �38�23<sup>0</sup> N and 114�09<sup>0</sup> �122�43<sup>0</sup> E, with temperate monsoon climate and temperate maritime climate: short spring and autumn, long winter, and long summer with concentrated precipitation and heat. Fig. 1a shows forest, grassland, cropland and others account for 5%, 0.5%, 85% and 9.5% of study area respectively as estimated with land cover classifications 

Table 1 

Summary of several commonly composite drought indices. 

|Composite index|Data source|Method|Reference|
|---|---|---|---|
|SDCI|Precipitation, LST, NDVI, reflectance|empirical weights|(Rhee et al.2010)|
|MIDI|Precipitation, soil moisture, and LST|empirical weights|(Zhang and Jia, 2013)|
|SDI|Precipitation, LST and NDVI|Principal Component Analysis (PCA)|(Du et al., 2013)|
|MDI|Precipitation, runoff, evapotranspiration and soil moisture|Kernel PCA and kernel entropy component analysis (KECA)|(Rajsekhar et al., 2015)|
|OMDI/MVDI|Precipitation, soil moisture, LST and NDVI|empirical weights, PCA, and constrained optimization|(Hao et al., 2015)|
|PADI|Precipitation, soil moisture, NDVI|Evolution Process-based Multi-sensor Collaboration (EPMC)|(Zhang et al., 2017)|



Q. Liu et al. / Science of the Total Environment 711 (2020) 134585 

3 



Fig. 1. (a) Distribution of meteorological stations and landcover based on MODIS International Geosphere Biosphere Program (IGBP) land cover classification map of 2015 MCD12Q1, some land cover classes were aggregated into one category, (b) average annual precipitation of 2015, and (c) average annual temperature in 2015. 

derived from 2015 MODIS (the Moderate Resolution Imaging Spectroradiometer) data (MCD12Q1). 

Recently, Shandong has less precipitation and uneven distribution in time and space, and the frequent occurrence of drought has seriously restricted the agricultural production and economic development of Shandong (Wang and Chen, 1999; Ma et al., 2013). 

Thus, SPEI captures the main impact of increased temperatures on water demand (Vicente-Serrano et al., 2010). MI based on Penman–Monteith FAO 56 method (P-M) also was calculated (Allen et al., 1998). SPEI contains the information of evapotranspiration compared with SPI and is more flexible than MI in time scale. Thus, SPEI was used for regression analysis, and SPI and MI were used as comparisons. 

###### 2.2. Data and methodology 

###### 2.2.2. TRMM precipitation 

###### 2.2.1. In situ reference data and drought indices 

The 30 years of monthly precipitation, mean temperature, wind speed at 2 m, relative humidity, saturated vapor pressure, actual vapor pressure, sunshine duration and latitude data from 1988 to 2017 were obtained from China meteorological data service (http://data.cma.gov.cn) over the study area. There are 27 weather stations with no missing data in Shandong province. 

Referring to Standard Precipitation Index User Guide (2012), 1- month SPI reflects short-term conditions, its application can be related closely to meteorological types of drought; 3-month SPI gives an indication of soil moisture conditions as the growing season begins; 6-month SPI may also begin to be associated with anomalous stream flows and reservoir levels and 9-month SPI is usually a good indication that dryness is having a significant impact on agriculture. Thus, in this study, the most widely used in-situ drought indices SPI and SPEI were calculated at 1-, 3- ,6and 9-month time scales (noted as SPI-1, SPI-3, SPI-6, SPI-9, SPEI1, SPEI-3, SPEI-6 and SPEI-9, respectively) using the data above. SPI can be calculated using historical precipitation data at different time scales to monitor droughts with respect to different usable water resources (Mckee et al., 1993; Hayes et al., 1999). SPEI, an extension of SPI, is designed to take into account both precipitation and potential evapotranspiration (PET) in determining drought. 

TRMM satellite was launched in November 1997, and since then, the TRMM Multi-satellite Precipitation Analysis (TMPA) monthly gridded precipitation product was used to monitor precipitation variation and drought. The 3B43 dataset with 25 km � 25 km spatial resolution from 1998 to present, and weighting as precipitation rates (mm/h). The TRMM 3B43 monthly precipitation data (March-September) from 2013 to 2017 were obtained from National Aeronautics and Space Administration (NASA) Data and Information Services Center (DISC) (http://disc. sci.gsfc.nasa.gov/). In this study, the data were resampled to 1 km resolution and calculated monthly PCI, and the formula is as follows: 



where TRMMmax and TRMMmin refer to the historical maximum and minimum values at each desired time step over the study period, TRMMi represents the precipitation in i month. 

###### 2.2.3. GLDAS soil moisture 

The data set, Global Land Data Assimilation System Version 2.1 (GLDAS-2.1) Noah 0.25�3-hourly, simulated with the Noah Model 3.3 in Land Information System (LIS) Version 7, was used in this 

Q. Liu et al. / Science of the Total Environment 711 (2020) 134585 

4 

study. This dataset contains 36 land surface fields from January 2000 to present (https://giovanni.gsfc.nasa.gov/giovanni/). Soil moisture data from 2013 to 2017 during March to September was resampled to 1 km and used to calculate monthly SMCI. SMCI can be described as: 



where SMmax and SMmin are the historical maximum and minimum values at each desired time step over the study period, SMi is the soil moisture in i month. 

###### 2.2.4. MODIS LST and NDVI 

The MODIS LST and NDVI from 2013 to 2017 during March to September in each year were used to calculate monthly VCI and TCI. Both LST (8-day, MOD11A2, collection v006) and NDVI (16day, MOD13A2, collection v006) with 1 km resolution were obtained from NASA’s Earth Observing System Data and Information System (EOSDIS) (http://reverb.echo.nasa.gov). The formulas of TCI and VCI are as follow: 





where LST max(NDVImax) and LST min(NDVImin) are the historical maximum and minimum values at each desired time step over the study period, LST i and NDVIi represent the land surface temperature and normalized difference vegetation index in i month. 

###### 2.2.5. SMOS soil moisture 

In this study, the near real-time global SMOS Level-3 soil moisture products generated by the SMOS-BEC (http://cp34-bec.cmima. csic.es) were selected, which provides soil moisture data sets at various temporal resolutions: daily maps in both maps in both 

Icosahedral Snyder Equal Area grid projection with aperture 4, resolution 9 (ISEA 4H9) and Equal Area Scalable Earth vison 2 (EASE2) 25 km � 25 km, and 3-day, 9-day, monthly, and annual maps in EASE-2 25 km � 25 km. In this study the monthly soil moisture product with the EASE grid from 2013 to 2017 during March to September was used to verify the ability of MCDIs for monitoring vegetation drought. 

###### 2.2.6. The multivariable linear regression method 

Many problems that can be solved by nonlinear regressions and polynomial regressions can also be solved by multiple linear regression, and thus, multiple linear regression is widely used in many fields (Zheng, 2018). The multivariable linear regression refers to the influence of multiple factors on one result and has n independent variables and a dependent variable Y. The formula is approximated by: 



where e is a random experimental error, b0 is the constant,b1,���,bj are the coefficients of X1, X2,���, Xj. When the value of bj(j ¼ 1; 2; 3; ��� n) is greater than 0, the larger value of bj(j ¼ 1; 2; 3; ��� n), the higher degree of interpretation Xj (j ¼ 1; 2; 3; ��� n) to Y. In this study, SPEI-1, SPEI-3, SPEI-6 and SPEI-9 were Y, and X1,X2,���, Xj were PCI, SMCI, TCI and VCI, and the overall approach was illustrated in Fig. 2. 

Because PCI, TCI, SMCI, and VCI have various degrees of impacts on drought, when the regression is performed, there may be problems such as a failure of the significance test. In this regard, Variance Inflation Factor (VIF) test, mediator and moderator variables were introduced to optimize the regression model (Wen et al., 2005). 

The formula of VIF can be approximated by: 





Fig. 2. The flowchart of MCDIs establishment based on multivariable linear regression method. 

Q. Liu et al. / Science of the Total Environment 711 (2020) 134585 

5 

where Rj is the determination coefficient between Xj and the rest of independent variables in the process of regression. If VIF is less than 10, it indicates there is no multicollinearity between independent variables. 

Testing of mediator and moderator variables (Wen et al., 2005): 



where Y, X, M were dependent variable, independent variable and mediator variable, respectively. C1, C2 and C3 were constants. a1 ,a2, a3 and b were coefficients, and all of them need to pass the significance test. If a2 or b fails to pass the significance test, the Sobel test is required. Only when the p value of Sobel test is less than 0.05, it will be a significant mediator effect. For moderator variables, it is sufficient that coefficient of interaction term is significant. 

###### 3. Results and discussion 

3.1. Correlations between single remote sensing drought indices and in-situ drought indices 

The remotely sensed index values were extracted according to the in-situ meteorological station location during the chosen time period (Zhang and Jia, 2013). To assess the capability of single remote sensing indices in monitoring drought, the correlation coefficients (r) were calculated between each single remote sensing drought index and in-situ drought indices SPEIs over the study area (Table 2). 

Table 2 shows that the r between PCI and SPEI-1 was the highest (r = 0.69), which indicates PCI was the most sensitive in monitoring short-term drought compared with other single remote sensing indices, and the r decreased as the SPEI time scale increased. SMCI showed the highest r with SPEI-3 when compared with other single indices. This suggested that SMCI provided reliable but time-lagged information in monitoring meteorological and vegetation droughts. Similar to PCI, TCI had the highest r with SPEI-1 than other SPEIs, and the r decreased as the SPEI time scale increased. The r between VCI and SPEIs were lower than that between other single indices and SPEIs. And the r value between VCI and SPEI-9 showed higher than that between VCI and other SPEIs, which suggested that drought information reflected in VCI was lagged for a longer time than that in SMCI. 

###### 3.2. Establishment of composite drought indices by multivariable linear regression method 

Table 3 shows coefficients, significance, normalization coefficient and VIF of four single indices generated by multivariable linear regression method. All values of VIF less than 10, the maximum VIF value that frequently taken as an indication that multicollinearity may be unduly influencing the least squares estimates. In addition, most p-values of coefficients was less than 0.05, but, in results of regression on SPEI-1, the coefficients of SMCI and VCI did 

Table 2 

Correlation coefficients (r) values between single remote sensing drought indices and different time scales in-situ indices SPEI. All p-values were less than 0.01. n denotes the sample size. 

Table 3 

The Coeff (coefficient), p-values and N-Coeff (Normalization coefficient) of single remote sensing indices obtained by multivariable linear regression method. 

|||SPEI-1|SPEI-3|SPEI-6|SPEI-9|VIF|
|---|---|---|---|---|---|---|
|PCI|Coeff|1.695|0.575|0.431|0.206|1.191|
||p|0.000|0.000|0.000|0.049||
||N-Coeff||0.319|0.312|0.143||
|SMCI|Coeff|0.084|0.560|0.387|0.515|1.231|
||p|0.328|0.000|0.000|0.000||
||N-Coeff||0.311|0.280|0.358||
|TCI|Coeff|0.464|0.496|0.348|0.344|1.189|
||p|0.000|0.000|0.001|0.001||
||N-Coeff||0.275|0.252|0.239||
|VCI|Coeff|0.018|0.172|0.216|0.372|1.030|
||p|0.822|0.049|0.025|0.000||
||N-Coeff||0.095|0.156|0.260||
|Model|p|0.000|0.000|0.000|0.000||



not pass significance test. For drought, both SMCI and TCI can provide indispensable information. Thus, we introduced mediator or moderator variables to optimize this model. 

The occurrence of drought depends largely on precipitation and soil moisture, and precipitation can affect soil moisture. Therefore, we believed soil moisture was mediator variable, in other words, precipitation influences drought by changing soil moisture in some degree, and the test results of mediator variable are shown in Table 4. Additionally, land surface temperature has effects on the evaporation of soil moisture, and vegetation also has impacts on drought (Cheng and Huang, 2016; Liu, 2016). Test results of moderator variables TCI and VCI are displayed in Table 5, and significance test of interaction term coefficients showed TCI had significant moderator effect between PCI and SMCI. VCI had significant moderator effect between PCI and SPEI-1 but did not have it between PCI and SMCI and between SM and SPEI-1. The flowchart is shown in Fig. 2, and the equation of multivariable linear regression on SPEI-1 was represented by Eqs. (10) and (11). The role of SMCI can be expressed indirectly by PCI and TCI (Eq. (11)) in some way rather than being eliminated. Table 6 displays the reregression result on SPEI-1. All coefficients passed the significance test, and the VIF of all variables were less than 10, which suggested this model was reasonable. Negative values represent a negative correlation, and, in the study area, rain and heat over the same period and irrigation of crops caused coefficients of PT and V to be negative. 





where X was PCI, M was mediator variable SMCI,W 1 and W 2 were moderator variables TCI and VCI. 

Fig. 3 shows the regression standardized residual of SPEIs, and their residuals were in normal distribution. Based on Tables 3 and 6, MCDIs were established. Fig. 4 shows the comparisons of S (the highest r values between single drought indices and SPEIs) and C (the r values between the composite indices and SPEIs), and the difference between C and S ranges from 0.04 to 0.12. Each single index can only provide its own information, but composite indices can integrate the information provided by single indices 

Table 4 

p-value test of mediator variable SMCI in Eqs. (7), (8) and (9). 

||SPEI-1|SPEI-3|SPEI-6|SPEI-9|||SMCI|SPEI-1|
|---|---|---|---|---|---|---|---|---|
|PCI (n = 945)|0.69|0.39|0.28|0.21|Eq (7)|PCI||0.000(a1)|
|SMCI(n = 945)|0.31|0.40|0.28|0.30|Eq (8)|PCI|0.000(a2)||
|TCI(n = 945)|0.37|0.36|0.26|0.25|Eq (9)|PCI||0.000(a3)|
|VCI(n = 945)|0.11|0.16|0.15|0.20||SMCI||0.012(b)|



Q. Liu et al. / Science of the Total Environment 711 (2020) 134585 

6 

Table 5 

Testing of moderator variables TCI and VCI (p-value test of the interaction term). P: PCI; SM: SMCI; PT: the interaction term of PCI and TCI; PV: the interaction term of PCI and VCI and SMV: the interaction term of SMCI and VCI. 

||TCI|VCI||
|---|---|---|---|
||Between P and<br>SM|Between P and SM and<br>between P and SPEI-1|Between SM and<br>SPEI-1|
||PT|PV|SMV|
|SMCI|0.000|0.894||
|SPEI-1||0.004|0.191|



Table 6 

The result of multivariable linear regression on SPEI-1. Coeff: coefficient; N-Coeff: (Normalization coefficient); PT: the interaction term of PCI and TCI and PV: the interaction term of PCI and VCI. 

||PCI|TCI|PT|VCI|PV|Model|
|---|---|---|---|---|---|---|
|Coeff|1.728|0.713|�0.608|�0.233|0.683||
|p|0.000|0.000|0.003|0.037|0.001|0.000|
|N-Coeff|0.757|0.312|�0.266|�0.102|0.299||
|VIF|4.975|2.235|5.477|2.096|4.271||



together. And the performance of MCDIs was better than that of each single index, which indicated MCDIs had a stronger interpretation of drought and were more suitable for detecting the drought than single indices. 



Fig. 4. Comparisons between S and C. S: the highest r values between single drought indices and SPEIs; C: the r values between the composite indices and SPEIs. 

3.3. Comparisons of MCDIs with in-situ drought indices and soil moisture 

To verify the ability of MCDIs to monitor meteorological and agricultural drought, this study used the in-situ meteorological drought indices MI and SPIs and SMOS soil moisture data to compare with MCDIs. 



Fig. 3. Regression standardized residual and Normal P-P plot of multivariable linear regression on SPEI-1(a), SPEI-3(b), SPEI-6(c) and SPEI-9(d). 

Q. Liu et al. / Science of the Total Environment 711 (2020) 134585 

7 

Table 7 shows that MCDI-1 had the highest r with MI compared with other MCDIs and had the highest r with SPI-1 than other SPIs. Fig. 5 displays scatterplots of MCDI-1 and in-situ meteorological drought indices (MI and SPI-1). These indicated MCDI-1 was more suitable for monitoring short-term drought especially meteorological drought than other MCDIs. 

Fig. 6 displays the correlation coefficient maps of MCDI-1, MCDI-3, MCDI-6 and MCDI-9 with soil moisture. The r value between MCDI-1 and soil moisture was concentrated between 0.2 and 0.5 and the average r was 0.359, which was obviously lower than that between other MCDIs and soil moisture. It meant MCDI-1 was not suitable to detect agricultural drought. Fig. 6(b) and (c) show most of the r values were above 0.6, and the average r were 0.675 and 0.653, respectively. Fig. 6(d) shows the r value between MCDI-9 and soil moisture, and the r values are concentrated above 0.7, suggesting MCDI-9 was the most suitable to monitor agricultural drought compared with other MCDIs. In addition, the average r (0.740) of Fig. 6(d) was the highest. Overall, from Table 5, Figs. 5 and 6, MCDI-1 and MCDI-9 can be used to detect meteorological and agricultural drought. 

###### 3.4. Spatial distribution of drought monitored by MCDI 

Referring to the comparisons between MCDIs and in-situ drought indices and that between MCDIs and soil moisture, MCDI was divided into five levels: 0 � MCDI less than 0.1 (extreme drought), 0.1 � MCDI less than 0.2 (severe drought), 0.2 � MCDI le ss than 0.3 (moderate drought), 0.3 � MCDI less than 0.5 (slight drought) and 0.5 � MCDI (no drought). 

Fig. 7 shows the spatial distribution of drought monitored by MCDI-1 and MCDI-9 in the typical drought year (2014) from March to September. The spatial distribution of MCDI-1 showed a large regional drought occurred in both spring and summer, and the condition of drought was most severe in March, July and August. Extreme droughts occurred mainly in March, a month of frequent drought in Shandong. As the precipitation belt moved southeast, 

from April to May, the drought eased gradually. In summer of 2014, high temperatures and little rainfall, massive droughts occurred in the study area. In July, except for coast area, moderate and severe drought occurred in the remaining area; in August, moderate and severe droughts still occurred, but they transferred to the north of Shandong. Because of high temperature fading and supplement of precipitation, in September, the drought had disappeared. Additionally, in the early stages of drought (March to May), due to the water storage capacity of soil and vegetation, MCDI-9 showed a less degree of drought than MCDI-1. However, as the drought continued, the temperature rising, no effective precipitation and soil water evaporation and plant transpiration increasing caused the drought shown by MCDI-9 to be more serious than that exhibited by MCDI-1. 

###### 3.5. Discussions and limitations 

In this study, the performance of MCDIs in monitoring meteorological and vegetation drought of study area were very well, but some uncertainty and limitations have to be acknowledged about MCDIs. For example, the main vegetation type of the study area was the cropland, which caused the performance of MCDIs in other vegetation types have not been tested. For other vegetation types, such as grassland and forest, there are difference in soil moisture retention and transpiration compared with cropland. This may affect the role of mediation variable SMCI and moderator variables TCI and VCI in the regression. In addition, MCDIs were used to monitoring drought only at monthly scale. But the severity and spatial distribution of drought is constantly changing. This requires a smaller time scale, such as 8-day and 16-day. Also, MCDIs did not consider the information of evapotranspiration. 

Therefore, future work needs to be focused on larger study area including multiple vegetation types, more drought-related variables such as evaporation and transpiration, and reducing time scale. 

Table 7 

Comparison of MCDIs with MI and SPIs. n denotes the sample size. 

||MI (n = 630)|SPI-1(n = 945)|SPI-3(n = 945)|SPI-6(n = 945)|SPI-9(n = 945)|
|---|---|---|---|---|---|
|MCDI-1|0.690|0.708|0.392|0.299|0.207|
|MCDI-3|0.437|0.600|0.467|0.338|0.306|
|MCDI-6|0.348|0.602|0.472|0.344|0.316|
|MCDI-9|0.201|0.488|0.457|0.327|0.334|





Fig. 5. Scatterplot of MCDI-1 and in-situ meteorological drought indices (MI and SPI-1). 

Q. Liu et al. / Science of the Total Environment 711 (2020) 134585 

8 



Fig. 6. Maps of correlation coefficient between soil moisture and MCDI-1(a), MCDI-3 (b), MCDI-6(c) and MCDI-9 (d) over the study period. 

Q. Liu et al. / Science of the Total Environment 711 (2020) 134585 

9 



Fig. 7. Spatial distribution of drought monitored by MCDI-1 (a) and MCDI-9 (b) in the typical drought year (2014) from March to September. 

###### 4. Conclusions 

In this study, MCDIs were proposed to detect the spatial and temporal drought in Shandong by the multivariable linear regression during the growing season of major crops (MarchSeptember). Firstly, single remote sensing drought indices PCI, SMCI, TCI and VCI were compared with in-situ drought indices SPEI at multiple time scales to assess the ability of single drought indices in monitoring drought, and the results showed PCI had 

the highest r (r = 0.69) with SPEI-1, which suggested PCI provided more information than other single drought indices in monitoring drought. Secondly, we used the multivariable linear regression method to establish composite drought indices MCDIs. The correlation coefficients between composite indices and SPEIs was higher than that between each single index and SPEIs, and the improvement ranged from 0.04 to 0.12, which indicated MCDIs was more suitable to detect drought than single drought indices. Additionally, MCDI-1 has the highest r with MI and SPI-1, which indicated 

Q. Liu et al. / Science of the Total Environment 711 (2020) 134585 

10 

MCDI-1 was fit for monitoring meteorological drought. Compared with other MCDIs, MCDI-9 acquired the highest r with soil moisture, suggesting MCDI-9 was recognized as a good indicator for agricultural drought in study area. 

###### Declaration of Competing Interest 

There is no conflict of interest. 

###### Acknowledgement 

We thank editors and anonymous reviewers greatly improved the manuscript and Dr. Shahzad Ali for the grammatical editing of this paper. This work was funded by Key Basic Research Project of Shandong Natural Science Foundation of China (No. ZR2017ZB0422) and ‘‘Taishan Scholar” Project of Shandong Province, the National Key Research and Development Program of China (No. 2016YFD0300101), and the National Natural Science Foundation of China (No. 31571565, No. 3167158 5, No. 41901342). 

###### References 

AghaKouchak, A., Farahmand, A., Melton, F.S., Teixeira, J., Anderson, M.C., Wardlow, B.D., Hain, C.R., 2015. Remote sensing of drought: progress, challenges and opportunities. Geophys. Rev. https://doi.org/10.1002/2014RG000456. 

- Allen, R.G., Pereira, L.S., Raes, D., Smith, M., 1998. In: Crop EvapotranspirationGuidelines for Computing Crop Water Requirements-FAO Irrigation and Drainage Paper 56. FAO. https://doi.org/10.1016/j.eja.2010.12.00. 

- Anderson, M.C., Hain, C., Wardlow, B., Pimstein, A., Mecikalski, J.R., Kustas, W.P., 2011. Evaluation of drought indices based on thermal remote sensing of evapotranspiration over the continental United States. J. Clim. https://doi.org/ 10.1175/2010JCLI3812.1. 

- Bai, Y., Zhang, J., Zhang, S., Yao, F., Magliulo, V., 2018. A remote sensing-based twoleaf canopy conductance model: Global optimization and applications in modeling gross primary productivity and evapotranspiration of crops. Remote Sens. Environ. 215, 411–437. https://doi.org/10.1016/j.rse.2018.06.005. 

- Weiying, C., Qianguang, X., Yongwei, S., 1994. Application of the anomaly vegetation index to monitoring heavy drought in 1992. Remote Sens. Envrion. 

- Cheng, S., Huang, J., 2016. Enhanced soil moisture drying in transitional regions under a warming climate. J. Geophys. Res. [Atmos.] 121. https://doi.org/ 10.1002/2015JD024559. 

Dai, A., 2013. Increasing drought under global warming in observations and models. Clim. Chang Nat. https://doi.org/10.1038/nclimate1633. 

- Dong, T., Meng, J., Shang, J., Liu, J., Wu, B., 2015. Evaluation of chlorophyll-related vegetation indices using simulated Sentinel-2 data for estimation of crop fraction of absorbed photosynthetically active radiation. IEEE J. Sel. Top. Appl. Earth Obs. Remote Sens. 8, 4049–4059. https://doi.org/10.1109/JSTARS.2015.2400134. 

- Du, L., Tian, Q., Yu, T., Meng, Q., Jancso, T., Udvardy, P., Huang, Y., 2013. A comprehensive drought monitoring method integrating MODIS and TRMM data. J. Appl. Earth Obs. Geoinf. Int. https://doi.org/10.1016/j.jag.2012.09.010. 

- Guo, H., Bao, A., Liu, T., Jiapaer, G., Ndayisaba, F., Jiang, L., Kurban, A., De Maeyer, P., 2018. Spatial and temporal characteristics of droughts in Central Asia during 1966–2015. Sci. Total Environ. 624, 1523–1538. https://doi.org/10.1016/j. scitotenv.2017.12.120. 

- Guttman, N.B., 1998. Comparing the palmer drought index and the standardized precipitation index. J. Am. Water Resour. Assoc. https://doi.org/10.1111/j.17521688.1998.tb05964.x. 

Hao, C., Zhang, J., Yao, F., 2015. Combination of multi-sensor remote sensing data for drought monitoring over Southwest China. J. Appl. Earth Obs. Geoinf. Int. https://doi.org/10.1016/j.jag.2014.09.011. 

- Hayes, M.J., Svoboda, M.D., Wilhite, D.A., Vanyarkho, O., 1999. Monitoring the 1996 drought using the standardized precipitation index. Bull. Am. Meteorol. Soc. 80 (3), 429–438. 

Kogan, F.N., 1990. Remote sensing of weather impacts on vegetation in nonhomogeneous areas. J. Remote Sens. Int. https://doi.org/10.1080/ 01431169008955102. 

Kogan, F.N., 1995a. Application of vegetation index and brightness temperature for 

- drought detection. Sp. Res. Adv. https://doi.org/10.1016/0273-1177(95)00079-T. 

- Kogan, F.N., 1995b. Droughts of the late 1980s in the United States as derived from NOAA polar-orbiting satellite data. Bull. Am. Meteorol. Soc. https://doi.org/ 10.1175/1520-0477(1995)076<0655:DOTLIT>2.0.CO;2. 

- Kogan, F.N., 1997. Global drought watch from space. Bull. Am. Meteorol. Soc. https://doi.org/10.1175/1520-0477(1997)078<0621:GDWFS>2.0.CO;2. 

- Liu, Q., Zhang, G., Ali, S., Wang, X., Wang, G., Pan, Z., Zhang, J., 2019. SPI-based drought simulation and prediction using ARMA-GARCH model. Appl. Math. Comput. 355, 96–107. https://doi.org/10.1016/j.amc.2019.02.058. 

Liu, W.T., Kogan, F.N., 1996. Monitoring regional drought using the vegetation condition index. J. Remote Sens. Int. https://doi.org/10.1080/ 01431169608949106. 

Liu, X., Pan, Y., Zhu, X., Yang, T., Bai, J., Sun, Z., 2018. Drought evolution and its impact on the crop yield in the North China Plain. J. Hydrol. 564, 984–996. https://doi.org/10.1016/j.jhydrol.2018.07.077. 

- Liu, X., Zhu, X., Pan, Y., Zhao, A., Li, Y., 2015. Spatiotemporal changes of cold surges in Inner Mongolia between 1960 and 2012. J. Geogr. Sci. https://doi.org/10.1007/ s11442-015-1166-y. 

- Liu, Y., 2016. Impacts of vegetation on drought trends. Chin. J. Atmos. Sci. 40 (1), 142–156. https://doi.org/10.3878/j.issn.1006-9895.1508.15146 (in Chinese with English abstract). 

- Ma, J., Liu, B., Xia, J., 2013. Analysis of temporal and spatial characteristics of meteorological drought in Shandong Province based on the theory of Runs. Yellow River 35 (9) (in Chinese). 

- McKee, T.B., Doesken, N.J., Kleist, J., 1993. The relationship of drought frequency and duration of time scales. Eight conference on Apllied Climatology. Am. Meteorol. Soc., 179–186 

- Mishra, A.K., Singh, V.P., 2010. A review of drought concepts. J. Hydrol. https://doi. org/10.1016/j.jhydrol.2010.07.012. 

- Palmer, W.C. (1965). Meteorological drought. Research Paper No. 45.U.S. Department of Commerce Weather Bureau, Washington, D.C. 

- Piao, S., Ciais, P., Huang, Y., Shen, Z., Peng, S., Li, J., Zhou, L., Liu, H., Ma, Y., Ding, Y., Friedlingstein, P., Liu, C., Tan, K., Yu, Y., Zhang, T., Fang, J., 2010. The impacts of climate change on water resources and agriculture in China. Nature. https://doi. org/10.1038/nature09364. 

- Rajsekhar, D., Singh, V.P., Mishra, A.K., 2015. Multivariate drought index: an information theory based approach for integrated drought assessment. J. Hydrol. 526, 164–182. https://doi.org/10.1016/j.jhydrol.2014.11.031. 

- Rhee, J., Im, J., Carbone, G.J., 2010. Monitoring agricultural drought for arid and humid regions using multi-sensor remote sensing data. Environ. Remote Sens. https://doi.org/10.1016/j.rse.2010.07.005. 

- Rouse Jr., J., Haas, R., Schell, J., Deering, D., 1974. Monitoring vegetation systems in the great plains with ERTS. NASA Spec. Publ. 351, 309. 

- Svaboda, M., Hayes, M.,Woodm D., 2012. Wood Standard Precipitation Index User Guide. World Meteorological Organization. 10.1175/2007JCLI1348.1. 

- Thornthwaite, C.W., Mather, J. A., Thornthwaite, W., 1955. The water balance: Publications in Climatology, Laboratory of Climatology, vol. 8. 

- Vicente-Serrano, S., Beguería, S., López-Moreno, J.I., 2010. A multiscalar drought index sensitive to global warming: the standardized precipitation evapotranspiration index. J. Clim. 23, 1696–1718. https://doi.org/10.1175/ 2009JCLI2909.1. 

- Wagner, W., Lemoine, G., Rott, H., 1999. A method for estimating soil moisture from ERS Scatterometer and soil data. Environ. Remote Sens. https://doi.org/10.1016/ S0034-4257(99)00036-X. 

- Wang, H., Vicente-serrano, S.M., Tao, F., Zhang, X., Wang, P., Zhang, C., Chen, Y., Zhu, D., El Kenawy, A., 2016. Monitoring winter wheat drought threat in Northern China using multiple climate-based drought indices and soil moisture during 2000– 2013. For. Meteorol. Agric. https://doi.org/10.1016/j.agrformet.2016.06.004. 

- Wang, J., Chen, Y., 1999. Analyses of the main factors of drought in Shandong Province. Meteorol. Mon. 25 (11), 34–36 (in Chinese with English abstract). 

- Wang, Z., Li, J., Lai, C., Zeng, Z., Zhong, R., Chen, X., Zhou, X., Wang, M., 2017. Does drought in China show a significant decreasing trend from 1961 to 2009?. Total Environ. Sci. 579, 314–324. https://doi.org/10.1016/j.scitotenv.2016.11.098. 

- Wen, Z., Hau, K.T., Chang, L., 2005. A comparison of moderator and mediator and their applications. ACTA Psychol. Sin. 37 (2), 268–274 (in Chinese with English abstract). 

- Wilhite, D.A., Glantz, M.H., 1985. Understanding the drought phenomenon: the role of definitions. Water Int. https://doi.org/10.1080/02508068508686328. 

- Willmott, C.J., Feddema, J.J., 1992. A more rational climatic moisture index. Prof. Geogr. 44 (1), 84–88. https://doi.org/10.1111/j.0033-0124.1992.00084.x. 

- Wu, J., Liu, Z., Yao, H., Chen, X., Chen, X., Zheng, Y., He, Y., 2018. Impacts of reservoir operations on multi-scale correlations between hydrological drought and meteorological drought. J. Hydrol. https://doi.org/10.1016/j.jhydrol.2018.06.053. 

- Xu, P., Zhou,T.,Zhao,X.,Luo, H., Gao,S., Li, Z., Cao,L., 2018.Diverseresponsesofdifferent structured forest to drought in Southwest China through remotely sensed data. J. Appl. Earth Obs. Geoinf. Int. https://doi.org/10.1016/j.jag.2018.03.009. 

- Yao, N., Li, Y., Li, N., Yang, D., Ayantobo, O.O., 2018. Bias correction of precipitation data and its effects on aridity and drought assessment in China over 1961–2015. Sci. Total Environ. 639, 1015–1027. https://doi.org/10.1016/j. scitotenv.2018.05.243. 

- Zhang, A., Jia, G., 2013. Monitoring meteorological drought in semiarid regions using multi-sensor microwave remote sensing data. Environ. Remote Sens. https://doi.org/10.1016/j.rse.2013.02.023. 

- Zhang, J., Mu, Q., Huang, J., 2016. Assessing the remotely sensed drought severity index for agricultural drought monitoring and impact analysis in North China. Indic. Ecol. https://doi.org/10.1016/j.ecolind.2015.11.062. 

- Zhang, X., Chen, N., Li, J., Chen, Z., Niyogi, D., 2017. Multi-sensor integrated framework and index for agricultural drought monitoring. Environ. Remote Sens. https://doi.org/10.1016/j.rse.2016.10.045. 

- Zhao, H., Gao, G., An, W., Zou, X., Li, H., Hou, M., 2017. Timescale differences between SC-PDSI and SPEI for drought monitoring in China. Chem. Earth Phys. https://doi.org/10.1016/j.pce.2015.10.022. 

- Zheng, Q., 2018. Multiple linear regression analysis. Guide Sci. Educ. 2018 (10), 184 

- (in Chinese). 

- Zhou, L., Wu, J., Mo, X., Zhou, H., Diao, C., Wang, Q., Chen, Y., Zhang, F., 2017. Quantitative and detailed spatiotemporal patterns of drought in China during 2001–2013. Sci. Total Environ. 589, 136–145. https://doi.org/10.1016/j. scitotenv.2017.02.202. 

