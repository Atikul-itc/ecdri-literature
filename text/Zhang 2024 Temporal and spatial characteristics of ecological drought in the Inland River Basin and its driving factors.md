www.nature.com/scientificreports 



# **OPEN Temporal and spatial characteristics of ecological drought in the Inland River Basin and its driving factors** 

**Zezhong Zhang**<sup>**1**</sup> **, Jian Liu**<sup>**1**</sup> **, Kai Feng**<sup>**1**</sup> **, Fei Wang**<sup>**1**</sup> **, Hengzhi Guo**<sup>**1**</sup> **, Weijie Zhang**<sup>**2**</sup> **& Sinan Wang**<sup>**2**</sup> 

**Most of the previous studies only used the index of vegetation growth to characterize ecological drought. This study built a Standardized Ecological Water Deficit Index (SEWDI) , analysed its space–time evolution characteristics from the perspectives of time, space and spatio-temporal coupling, extractes feature variables by three-dimensional spatio-temporal clustering, analysed typical ecological drought events, the effect of teleconnection factors on ecological drought was investigated using cross wavelet analysis . The reliability of SEWDI was quantitatively evaluated by comparing the r values of Standardized Precipitation Index (SPI), Standardized Precipitation Evapotranspiration Index (SPEI), Standardized Soil Moisture Index (SSMI), self-calibrating Palmer Drought Severity Index (scPDSI), and SEWDI with Standardized Solar-induced Fluorescence (SSIF) at various scales in time.The results demonstrated that: (1) Ecological drought in the Inland River Basin showed a weakening trend from 1982 to 2015. Seasonal drought showed a wetting trend in the west and a drought trend in the east, and the wetting trend is most evident in spring. It may be related to the policy of returning farmland to forest in the eastern part of IRB in Inner Mongolia Autonomous Region. (2) Three-dimensional recognition method could extract more detailed characteristic variables of ecological drought events. A total of 133 ecological drought events occurred in the Inland River Basin during 1982–2015, and ecological drought events had a longer duration and intensity after the twenty-first century. (3) June 2005 to February 2007 was the most severe ecological drought event on record, which lasted for 21 months. The drought intensity was 44.65 × 10**<sup>**5**</sup> **month·km**<sup>**2**</sup> **, and the drought area was 23.79 × 10**<sup>**4**</sup> **km**<sup>**2**</sup> **. The event occurred in June 2005, intensified in September 2005, attenuated in June 2006, re-intensified in August 2006 and re-attenuated (extinction) in February 2007. The trend of drought migration spread to northeast (4) Among the teleconnecting factors, Among the teleconnection factors, ENSO has the most complex and greatest influence on ecological drought in the Inland River Basin. (5) In addition to having a high correlation with other drought indexs, the SEWDI can also more accurately reflect the effects of drought on vegetation. When ENSO events occur, IRB precipitation decreases significantly. However, the effect of soil moisture on vegetation is ignored in this study, which aims to provide ideas for calculating ecological drought index of small watershed. How to accurately calculate ecological water deficiency in different soil regions is the focus of future work.** 

**Keywords** Ecological drought, Three-dimensional spatiotemporal cluster recognition, Teleconnection factors, Inland River Basin 

Global warming intensifies the water cycle, leading to more extreme weather events. Meteorological drought caused by precipitation deficiency develops into agricultural drought caused by soil water deficit and hydrological drought caused by runoff deficit over time, resulting in reduce d water flow into wetlands and underground aquifers, which is highly likely to cause water deficit of vegetation dependent on precipitation and groundwater growth, and induce regional ecological drought<sup>1–3</sup> . The traditional classification of drought focuses on the 

> 1North China University of Water Resources and Electric Power, Zhengzhou 450046, China. 2Institute of Water Resources for Pastoral Area, China Institute of Water Resources and Hydropower Research, Hohhot 010018, China. 

>  email: fengk0121@163.com 

**Scientific Reports** |        (2024) 14:28900 

1 

| https://doi.org/10.1038/s41598-024-76988-5 

www.nature.com/scientificreports/ 

occurrence of drought events, and researches on meteorological drought and its driven hydrological, agricultural and socio-economic drought, paying little attention to ecological drought<sup>4–6</sup> . Compared with meteorological, hydrological and agricultural drought, ecological drought involves more factors, many of which are difficult to monitor and quantify, and are very complicated. The first clear definition of ecological drought was presented by the SNAPP Ecological Drought Working Group, which defined it as: Caused by natural climate change or human activities of periodic water supply shortage result in changes hydrologic meteorological conditions, which makes the vegetation under water stress and its living soil environment form a xerophytic environment, and then feedbacks into a comprehensive and complex process of other systems<sup>7</sup> . Ecological drought is defined as a periodic water supply deficiency that causes ecosystems to exceed a threshold of vulnerability, affects the normal function of ecosystem, and triggers feedback loops in natural and/or human systems. 

Park<sup>8</sup> believed that ecological drought should be monitored from the perspective of ecosystem, and terrestrial ecosystem and aquatic ecosystem should be evaluated separately. McEvoy<sup>9</sup> used the new ecological drought framework to analyze five catchment-scale drought plans in southwestern Montana, USA, to evaluate the ecological impact of drought. Kim<sup>10</sup> quantitatively assessed the water quality risk caused by ecological drought by applying non-parametric kernel density estimation and assuming the probability of river water quality exceeding the water quality target after extreme drought. Park<sup>8</sup> established an ecological drought index with double thresholds of river ecological discharge and very low discharge, assessed the possible ecological drought degree of typical fish in the Gamu River ecosystem, and proposed methods for monitoring and early warning of ecological drought. For dryland ecosystems, the assessment of ecological drought is still in its infancy. At present, vegetation index based on remote sensing is commonly used to characterize the drought situation of vegetation, such as temperature vegetation Drought Index (TVDI)<sup>11,12</sup> , Standardized Vegetation Difference Index (NDVI)<sup>13,14</sup> , improved Vegetation Index<sup>15,16</sup> , Vegetation Condition Index (VCI)<sup>17,18</sup> , Vegetation Water Supply Index (VSWI)<sup>13,19</sup> . Although these vegetation indices can indirectly reflect the influence of drought on vegetation and the water consumption of vegetation, they cannot directly reflect the dynamic changes in the water supply and demand balance of vegetation in the process of ecological drought. Under the background that human beings have great ability to regulate the water resources system, it is difficult to carry out effective drought management based on the actual situation of water provide and requirement balance. It is not conducive to drought warning and drought mitigation. 

The Inland River Basin(IRB) is the transition zone from the semi-arid region to the arid region. With its special geographical location, it belongs to the national ecological security pattern of "three zones and two screens" sand belt in the north, and its ecological functions are positioned as extremely important functional areas for wind prevention and sand fixing and biodiversity protection. It plays an important role in basin water resources allocation, biodiversity, carbon cycle and regional economic development<sup>20</sup> . Since the twenty-first century, the Inner Mongolia Autonomous Region has implemented the policy of returning farmland to forest in the eastern part of IRB. The increase of vegetation has brought huge water consumption, aggravated water shortage, and affected vegetation growth and development. However, the conventional SPI and SPEI only reflect the abnormal phenomenon of precipitation, and the vegetation index such as NDVI and TVDI is also affected by other factors (such as flood, wildfire, insect pests, hail and human activities, etc.). It is difficult to reflect the effective drought situation of vegetation only by meteorological factors or vegetation index. Therefore, it is very necessary to construct an ecological drought index that can reflect both meteorological and hydrological conditions and vegetation water consumption state based on the dynamic balance between supply and demand of ecological vegetation. 

Based on reference crop evaporation (ET0) and actual evapotranspiration (ETA), this study calculated the ecological water deficit of vegetation, thereby constructing the ecological drought index of inland river basin. The actual evapotranspiration was used instead of precipitation, which can better represent the recharge of all water resources (such as precipitation and groundwater) in the process of vegetation growth. It can more accurately calculate the water consumption of vegetation during normal growth.Mann-Kendall (MK) was used to analyze the change trends of ecological drought at various seasonal scales, and three-dimensional(3D) spatiotemporal clustering was used to extract characteristic variables to analyze typical ecological drought events. The cross-wavelet was introduced to analyze the relationship between teleconferences and ecological drought, and the research results are helpful to promote the research on the influence of ecological drought on grassland system and its mechanism. 

## **Materials and methods** 

### **Study area** 

The IRB is located at 40°33’–46°46’ north latitude and 105°12’–120°7' east longitude. It is mostly desert in the west, desert in the middle, and grassland and forest in the east, covering an area of about 311,600 km<sup>2</sup> . The climate is temperate continental monsoon climate, the annual average precipitation is 238.33 mm, mainly concentrated in July to August, accounting for 76% to 80% of the whole year, the annual average temperature is 2.5 °C, the annual average sunshine duration is 3100 to 3300 hours, the frost-free period is about 83 days, the annual average evaporation capacity is 877.62 mm, 3.7 times the precipitation. The annual average wind speed is 4.5m/s, and the maximum wind speed is 27.0m/s<sup>20</sup> . The overview of the IRB is shown in Fig. 1. It was drawn by ArcGIS 10.6.1 (https://desk top.arcgis.c om/zh-cn/des ktop/index. html). 

### **Data source** 

The meteorological data used in this article is from the National Cryosphere Desert Data Center  ( h t t p s : / / d a t a . t p d c . a c . c n ) , Land use classification data are from the annual China Land Cover Dataset (https://zenodo.org) and vegetation remote sensing data are from the Avhrr land normalized difference vegetation index  ( h t t p s : / / w w w . n c e i . n o a a . g o v ) and (https://globalecology.unh.edu/data/GOSIF.html). Table 1. provides data-specific information. 

**Scientific Reports** |        (2024) 14:28900 

2 

| https://doi.org/10.1038/s41598-024-76988-5 

www.nature.com/scientificreports/ 



**Fig. 1** . Study area. 

|**Data**|**Time scale**|**Resolution**|
|---|---|---|
|CLCD|1985, 1990–2019|30 m×30 m|
|DEM||1 km×1 km|
|NDVI|1981–2022|0.05°×0.05º|
|ETA|1982–2017|0.1°×0.1º|
|ET0|1901–2022|0.00833°×0.00833º|
|Precipitation & Temperature|1901–2022|1 km×1 km|
|Specific humidity & Downward shortwave radiation|1979–2018|0.1°×0.1º|
|0.05-degree product of solarinduced chlorophyll fluorescence|2000–2015|0.05°×0.05º|



**Table 1** . Information about datasets. 

In order to maintain spatiotemporal consistency of the data, the high-precision dataset was resampled to 1/12°× 1/12°using nearest neighbor interpolation, covering the period 1982–2015. The resample method in this paper is implemented by the terra package in R-4.4.1 programming language  ( h t t p s : / / c r a n . r - p r o j e c t . o r g / w e b / / p a c k a g e s / t e r r a / i n d e x . h t m l ) . 

To examine the relationship between ecological drought and monthly teleconnection factors between 1982 and 2015, this study selected partially representative monthly teleconnection factors<sup>21,22</sup> . Detailed information about the monthly teleconnection factors is shown in Table 2. 

### **Methods** 

_Standardized ecological water deficit index (SEWDI)_ 

SEWDI can identify the degree of water deficit in the sense of ecology, and can reflect not only the change of hydrometeorological conditions, but also the balance between consumption and demand of vegetation system<sup>23</sup> . The index takes the difference between ecological consumption water and ecological demand water as the ecological water deficit sequence, and the calculation methods are as follows: 

**Scientific Reports** |        (2024) 14:28900 

3 

| https://doi.org/10.1038/s41598-024-76988-5 

www.nature.com/scientificreports/ 

|**Teleconnection factor**|**Full names**|**Time scale**|
|---|---|---|
|AO|Arctic oscillation|1982–2015|
|ENSO|El Niño-Southern oscillation|1982–2015|
|PNA|Pacific North America index|1982–2015|
|SOI|Southern oscillation index|1982–2015|
|Sunspot|Sunspot|1982–2015|
|TPI|Trans polar index|1982–2015|



**Table 2** . Selected teleconnection factor information. 









where EWD means ecological water deficit, mm; EWC means ecological water consumption,mm; EWR means ecological water requirement,mm; ET0 represents refer to crop evapotranspiration; Kc is vegetation coefficient, Choudhury studied and obtained NDVI* replaceable crop coefficient<sup>24</sup> ; _NDV I max_ and _NDV I min_ are maximum and minimum values of NDVI for each year; η is approximately 1. 

The ecological water deficit sequence was treated with the inverse standardization similar to the SPI to obtain SEWDI, and the Standardized Ecological Water Deficit Index (SEWDI) was obtained to characterize the impact degree of drought on the ecosystem. The specific steps are as follows: (1) The ecological water deficit sequence _x1i_ was normalized to obtain a new sequence _x2i_ , which was replaced by 1 and 0 of 0.999 and 0.001 respectively in order to fit the distribution; (2) Three commonly used distributions, including Gamma distribution, loglogistic distribution and P-III distribution, were selected to fit _x2i_ and obtain the probability density equation _fx2i(t)_ . Akaike information criterion (AIC criterion) was used to select the optimal fitting distribution. (3) The probability density function of the optimal distribution function is integrated to obtain the corresponding cumulative distribution _Fx2i(t)_ ; (4) _Fx2i(t)_ was inversely normalized to obtain the standardized ecological water deficit index ( _SEWDI_ ). The expression is: 





_Mann–Kendall (MK) change point test_ 

With drought index sequence ( _x1_ , _x2_ ,..., _xn_ ), assuming no trend change in the series, construct the statistic: 



where _mp_ is the cumulative number of _xp_ > _xq_ (1 ≤ _q_ ≤ _p_ ,1 ≤ _p_ ≤ _n_ ). 

The _dk_ was standardized to get: 



where _UFk_ is the statistical parameter calculated along time series and follows the standard normal distribution; _E(dk)_ is the mathematical expectation of the statistic; _D(dk)_ is the variance of the statistic. 

Repeating the above calculation with the inverse time series, we get _UFk_ = - _UBk_ ( _k_ = _n_ , _n_ -1,...,1). _UFk_ and _UBk_ curves are plotted respectively, and the intersection point between the corresponding critical values is the mutation point if the significance level α = 0.05 is selected. MK change point test can be used to observe the year in which the time series changes, which is impossible for trend tests. 

**Scientific Reports** |        (2024) 14:28900 

4 

| https://doi.org/10.1038/s41598-024-76988-5 

www.nature.com/scientificreports/ 

_Mann–Kendall (M–K) trend test method_ 

Mann-Kendall (M-K) non-parametric statistical test method was used in this study to judge the significance of the change trend of ecological drought without samples being subject to a certain distribution and unaffected by outliers. The Z-value of time series trend was calculated to indicate the significance of a change in a time series trend.. When |z| is greater than 2.58, 1.96 and 1.64, respectively, the significance test of the change trend of time series was passed by _p_ = 0.01, _p_ = 0.05 and _p_ = 0.1. 

Suppose there is a time series X = x1,x2,…xn, divide each data in the series by the mean of the modified series to obtain a set of time series Xt, and then calculate the rank trend estimate β of the new time series: 



when β > 0, the time series showed an upward trend. When β < 0, the time series showed a downward trend. 

Assuming that the trend term of time series _Xt_ is linear _Tt_ , the corresponding stationary series _Yt_ can be obtained after removing _Tt_ of time series: 



The corresponding rank sequence of stationary sequence Yt was calculated, and the autocorrelation coefficient _ri_ was calculated 



where _Ri_ is the rank of _yi_ and _R_ is the mean of the rank. 

According to the autocorrelation coefficient _ri_ , the variance var(S) of the trend statistic S of the autocorrelation series can be obtained: 





The Z-value of the trend of time series was calculated to represent the significance of its change. When MMK statistics S > 0, S = 0, and S < 0, the expressions are as follows: 



_3D identification method of drought events_ 

Ecological drought event is essentially a spatio-temporal continuous 3D structure (longitude, latitude, and time)<sup>25</sup> . Based on raster data set, this study calculated a 3D matrix of ecological drought index (denoted as X) at the level of longitude-latitudinal time. The drought index of each grid point in the matrix X can be expressed as X(i, j, k), where i represents the longitude coordinate of the point, j represents the latitude coordinate of the point, and k represents the time coordinate of the point<sup>1,4</sup> . Based on the above 3D drought index grid matrix, 3D identification of drought events is carried out through the following steps: Consider the evolution of drought events as a cube of space-time (longitude, latitude, and time). This study extracted the 3D sequence of SEWDI4 to characterize ecological drought. The extraction process consists of two steps (Fig. 2) : First, the monthly dry patches are identified by clustering method; Secondly, t The overlap area of drought patches between two months was selected to construct the drought cube, and the overlap area was more than 1.6% of the total area.For each ecological drought event, four characteristic variables of drought event were extracted. In this study, used four drought characteristic variables: duration, effect area, intensity, and center of drought, analyzed the continuous spatiotemporal evolution characteristics of ecological drought event. It was drawn by MATLAB R2022b  ( h t t p s : / / w w 2 . m a t h w o r k s . c n / h e l p / m a t l a b / r e f / s l i c e . h t m l ) . 

#### _Cross wavelet method_ 

This study examined the relationships between teleconnecting factors and SEWDI by using the cross-wavelet, so as to explore the driving factors of SEWDI in the IRB. When two time series are added together, cross wavelets can reveal their common oscillation behavior<sup>26</sup> . Among them, In the high-energy region, cross wavelet energy spectrum (XWT) is often used to explain phase relationships between sequences, and it is common to use the cross wavelet energy cluster spectrum (WTC) to explain the phase relationship between two sequences in the low-energy region. 

**Scientific Reports** |        (2024) 14:28900 

5 

| https://doi.org/10.1038/s41598-024-76988-5 

www.nature.com/scientificreports/ 



**Fig. 2** . Schematic diagram of drought patch identification and time-path connection. It was drawn by  d r a w . i o ( h t t p s : / / a p p . d i a g r a m s . n e t / ) . 

_Pearson correlation analysis_ 

The correlation of two drought index and its significant level were analyzed based on Pearson correlation coefficient<sup>27</sup> : 



where _rxy_ is the correlation coefficient of _x_ and _y_ variables; _xi_ and _yi_ are the values of _x_ and _y_ in year i; _x_ , _y_ is the average of the two variables; n is the number of years. 

#### _Restraint line extraction_ 

The restraint line method provides a new way to explore the mechanism of driving factors’ influence on SEWDI<sup>28</sup> . In this study, quantile segmentation method is selected to extract restraint lines. According to the scatter plot between different variables, Divided the driving factors equally into 100 parts along the X-axis, and 100 columns are obtained. 99.9% quantile of each column was taken as boundary points, and 100 boundary points are obtained. The boundary points were fitted by the least square method, and the type with the largest fitting determination coefficient was taken as the fitting result of the restraint line from the four types of functions: straight line, quadratic function, logarithmic function and exponential function. Using R-4.4.1, the optimal restraint line was simulated according to the shape and goodness of fit of the scattered point cloud. 

## **Results** 

### **Characteristics of ecological drought time variation** 

The cumulative effect of ecological water deficit in different periods. In this study, the SEWDI of ecological drought zones in IRB at 1–24 months scale and the mean SEWDI of different scales each year were calculated, the Hovmoller chart was used to plot the temporal variation characteristics of ecological drought index at multiple scales (Fig. 3). Blue green indicates wet, that is, ecological drought is relatively stable, and yellow red indicates drought. As can be seen from Fig. 3, when the accumulation time is longer, the fluctuation frequency of SEWDI is lower, and when the accumulation time scale decreases, the fluctuation frequency of SEWDI increases. In different time scales, the low SEWDI value of IRB concentrated in 2000–2008, that is, the ecological drought was more serious, and SEWDI fluctuated greatly during 2000–2008, which was in the alternating stage of dry and wet, and entered the wet period after 2008. Several notable dry periods occurred in the IRB in 1985–1987, 2001–2002, and 2005–2007. The SEWDI in the IRB showed a trend of first decreasing in1982-1987, then increasing in1987–2000, then sharply decreasing in 2000–2008 and finally increasing in 2009–2015. This trend was consistent with the findings of Wang et al.<sup>29</sup> . The overall trend was upward, that is, the SEWDI showed a slowly wet trend and became wet after 2008. 

The change characteristics of ecological drought at various time scales in IRB were further analyzed, the mean SEWDI at each scale was calculated, and the annual SEWDI change characteristics of inland river basins from 1982 to 2015 were plotted, as shown in Fig. 4. The SEWDI of the IRB appeared a fluctuating upward trend at annual scale, and the change tendency rate of SEWDI was 0.00913/1a, indicating that the IRB showed wetting ( _R_<sup>_2_</sup> = 0.013). Seasonal SEWDI changes in IRB during 1982-2015 are shown in the Fig. 4. In spring, summer and autumn, SEWDI in the Inner Mongolia IRB presents an upward trend, and the linear trend rates are 0.01224/1a, 0.00749/1a and 0.000116/1a, namely, the slowly wetting, and the change trend is the largest in spring. During 1982–2015, SEWDI had significant changes in each season and drought events occurred in all seasons, rising and falling alternately, showing a fluctuating upward trend, that is, humidification. In the Inner Mongolia IRB, the winter SEWDI showed a fluctuating downward trend from 1982 to 2009, reached the maximum value in 2010 and continued to decline after that, and the linear tendency rate was − 0.00505/1a, that is, the trend of drought. The monthly SEWDI series of IRB showed a steady upward trend from 1982 to 2015, but it was not obvious, 

**Scientific Reports** |        (2024) 14:28900 

6 

| https://doi.org/10.1038/s41598-024-76988-5 

www.nature.com/scientificreports/ 



**Fig. 3** . Temporal changes of SEWDI in IRB from 1 to 24 months. It was drawn by Origin 2022  ( h t t p s : / / w w w . o r i g i n l a b . c o m / 2 0 2 2 ) . 



**Fig. 4** . SEWDI trends in the IRB during 1982–2015 at different time scales. The red areas are 95% confidence intervals. It was drawn by Origin 2022 (https://www.originlab.com/2022). 

and the linear trend rate was 0.0000091/1a. The fluctuation range was small from 1982 to 2005, reaching the minimum value in November 2005, and the fluctuation range was larger from 2005 to 2015, although drought events occurred from time to time. But the overall trend is stable. 

MK method was used to test the mutation of annual and seasonal SEWDI index sequences. The confidence α = 0.05 and the critical value was ±1.96. As shown in Fig. 5, it can be seen that SEWDI has mutation points within confidence intervals at all scales, among which the mutation years of spring were 1998 and 2013, summer were 1984, 1986, 1988, 2001, 2003 and 2011. Autumn were 1991, 1997 and 2012, winter were 2001, 2003, 2007 and 2012, and year scale are 1983, 1987, 1999 and 2011. 

### **Temporal and spatial evolution characteristics of ecological drought** 

On the whole, the spatial distribution characteristics of the ecological drought change trend of the IRB were quite different in four seasons (Fig. 6). The specific characteristics of each season were as follows: In spring, there were more areas with an insignificant decline trend, that is, the trend of drought, accounting for 91.97%. 

**Scientific Reports** |        (2024) 14:28900 

7 

| https://doi.org/10.1038/s41598-024-76988-5 

www.nature.com/scientificreports/ 



**Fig. 5** . MK change statistics curve for year and seasonal SEWDI series. It was drawn by MATLAB R2022b (https://ww2. mathworks.cn /matlabcentr al/fileexch ange/25531-mann-kendall-test). 

Zhengxiangbai Banner, Xianghuang Banner and East Wuzhumuqin showed a trend of drought. This is due to the gradual thawing of the ground in spring, facing strong evaporation, and the rapid warming in the southern part of IRB and strong evapotranspiration, so the trend of aridity is obvious<sup>30</sup> . In summer, the SEWDI of Inner Mongolia IRB mainly decreased, accounting for 81.44%, mainly concentrated in Alxa Left Banner and Xilin Hot City. This region is located at the edge of the East Asian monsoon region, and is affected by the monsoon and the west wind, so the climate change is quite significant<sup>31</sup> . The spatial distribution of SEWDI variation trend in autumn of Inner Mongolia IRB was roughly the same as that in summer, with 15.08% of the areas showed no significant dry trend, 75.89% of the areas showed no significant upward trend, and 9.03% of the areas showed significant upward trend, mainly concentrated in Damao Banner and Siziwang Banner. The spatial distribution 

**Scientific Reports** |        (2024) 14:28900 

8 

| https://doi.org/10.1038/s41598-024-76988-5 

www.nature.com/scientificreports/ 



**Fig. 6** . Spatial distribution characteristics of SEWDI trend (Z-value) at seasonal scale in the IRB. It was drawn by ArcGIS 10.6.1 (https://desk top.arcgis.c om/zh-cn/des ktop/index. html). 

|||||**Centroi**|**d**|||
|---|---|---|---|---|---|---|---|
|**No**|**Start time (year/month)**|**End time (year/month)**|**Duration (month)**|**Lon(°E)**|**Lat(°N)**|**Affected area(10**<sup>**4**</sup>**km**<sup>**2**</sup>**)**|**Severity (10**<sup>**5**</sup>**month·km**<sup>**2**</sup>**)**|
|90|2005/6|2007/2|21|114.86|37.88|23.79|44.65|
|74|2000/9|2002/3|19|111.79|36.47|22.28|31.74|
|13|1985/6|1986/12|19|113.41|37.22|23.67|30.90|
|96|2007/4|2008/5|14|114.95|37.72|22.79|25.84|
|23|1989/4|1990/6|15|114.56|37.60|21.95|18.67|
|112|2011/3|2012/5|15|112.54|36.59|22.44|17.66|
|2|1982/9|1983/9|13|113.11|36.81|22.62|16.47|
|78|2002/5|2003/2|10|115.41|37.46|22.53|14.25|
|73|2000/3|2001/1|11|116.79|38.61|13.75|10.27|
|105|2009/6|2010/1|8|111.65|36.30|19.01|9.51|



**Table 3** . Top ten ecological drought events according to the severity from 1982 to 2015. 

of SEWDI variation trend in the IRB in winter was very different from that in summer and autumn. In winter, more areas showed a dry trend, that is, the trend of drought, accounting for 71.90%, among which 2.67% showed a significant drought trend, this is the same conclusion as Wang et al and Zhang et al.<sup>29,32</sup> . Relatively few areas showed an upward trend, that is, the trend of humidification, accounting for 28.10%. Zhang et al. and Zheng et al. believed that global warming and the increase in vegetation coverage lead to the increase in actual evapotranspiration<sup>33,34</sup> , resulting in a sharp increase in water consumption by vegetation, thus aggravating ecological drought. 

### **Recognition results of ecological drought events and their dynamic evolution with 3D recognition** 

_Recognition results of ecological drought events_ 

Add the calculated SEWDI1 raster data to MATLAB R2022b. Based on the 3D identification, 133 ecological drought events were identified in the IRB from 1982 to 2015, accounting for 32.60% of the study period, among which 44 drought events lasted more than 3 months. The most serious in the first 10 games ecological drought events and specific feature variables were listed in Table 3 according to the order of drought severity, where the drought event number represents the sequence of 133 drought events. The table showed that the duration of these 10 drought events was longer than 8 months, among which the 90th ecological drought event occurred from June 2005 to February 2007 was the most serious, with drought intensity of 44.65 × 10<sup>5</sup> month·km<sup>2</sup> and drought area of 23.79 × 10<sup>4</sup> km<sup>2</sup> . The 74th (September 2000–March 2002) and 13th (June 1985–December 1986) drought event lasted 19 months, ranking second and third. The 105th ecological drought incident sustained for 

**Scientific Reports** |        (2024) 14:28900 

9 

| https://doi.org/10.1038/s41598-024-76988-5 

www.nature.com/scientificreports/ 

8 months from June 2009 to January 2010, with a drought intensity of 9.51 × 10<sup>5</sup> month·km<sup>2</sup> and a drought area of 19.01 × 10<sup>4</sup> km<sup>2</sup> . 

In order to directly express the month-to-month variation trend of the characteristic variables of drought events, this study took the most serious (90th) drought event as an example, Fig. 7 and 8 showed the 3D perspective view of the Change of time and space of drought events. As can be seen from the Fig. 7, the monthly variation trends of the 90th drought affected area and severity are basically consistent, showed an increased trend from June 2005 to January 2006, and to the Max in January 2006, which is 23.20 × 10<sup>4</sup> km<sup>2</sup> and 44.06 × 10<sup>4</sup> month·km<sup>2</sup> , respectively, and a downward trend in the following two months. From March 2006 to June 2006, the drought area and drought intensity were 22.63 × 10<sup>4</sup> km<sup>2</sup> and 31.15 × 10<sup>4</sup> month·km<sup>2</sup> , respectively. From July 2006 to February 2007, the drought area and drought intensity were 1.43 × 10<sup>4</sup> km<sup>2</sup> and 1.71 × 10<sup>4</sup> month·km<sup>2</sup> . 

_The most serious ecological drought event in time and space dynamic evolution_ 

In order to further demonstrate the advantages of 3D drought identification method in describing the spatiotemporal dynamic process of drought, a severe ecological drought event occurred in recent years was selected as an example to analyze its spatio-temporal dynamic evolution from the beginning to the end of the drought, and all grid SEWDI values in this period were accumulated, as shown in Figs. 9 and 10. The 90th event lasted 21 months from June 2005 to February 2007, had a drought intensity of 44.65 × 10<sup>5</sup> month·km<sup>2</sup> , ranking first among all event, with specific characteristics as follows: It began in June 2005, and the drought area was about 2.96 × 10<sup>4</sup> km<sup>2</sup> , covering the Back banner of Wulat, the Middle Banner of Wulat, Guyang County, Damao Banner and the west of Wuchuan County, accounting for 4.63% of the total area of the IRB. The starting point of drought was located in the south of the Middle Banner of Wulat, Inner Mongolia Autonomous Region. In July 2005, the drought area expanded rapidly to 1.37 × 10<sup>5</sup> km<sup>2</sup> , accounting for 21.45%, and the 90th center moved northeast to the north of Siziwang Banner, other areas had been affected by the drought except the Alxa League of the IRB, and Damao Banner and the northern part of Siziwang Banner suffered the most serious drought. From August 2005 to January 2006, the drought area and intensity increased continuously, reaching the maximum values of 2.32 × 10<sup>5</sup> km<sup>2</sup> and 4.40 × 10<sup>5</sup> month·km<sup>2</sup> in January 2006. The epicenter of the 90th event moved northeast to the east of Sunit Right Banner. In April 2006, the severity of the 90th continued to increase, and the affected area was 2.17 × 10<sup>5</sup> km<sup>2</sup> , mainly concentrated in the middle of the IRB. In January 2007, the 90th event effected area was slumped to 1.29 × 10<sup>4</sup> km<sup>2</sup> , the 90th weakened, and then it was lifted. The drought event started from 



**Fig. 7** . Time trend of characteristic variables of time and space changes of the 90th ecological drought. It was drawn by MATLAB R2022b (https://ww2. mathworks.cn /help/matlab /ref/slice. html). 

**Scientific Reports** |        (2024) 14:28900 

10 

| https://doi.org/10.1038/s41598-024-76988-5 

www.nature.com/scientificreports/ 



**Fig. 8** . Dynamic evolution of the 90th ecological drought. It was drawn by ArcGIS 10.6.1  ( h t t p s : / / d e s k t o p . a r c g i s . c o m / z h - c n / d e s k t o p / i n d e x . h t m l ) . 

the west of the IRB, expanded its impact area, reached its maximum in the middle of the study area, and finally disappeared in the east of the study area. This method can feel the change of drought more directly. 

### **The relationship between teleconnecting factors and ecological drought** 

AO, ENSO, PNA, SOI, Sunspot and TPI data were used to reveal the dynamic relationship between SEWDI and teleconnection factors. As shown in Fig. 11, AO showed a significant negative correlation with SEWDI during 2000–2005 and 2008–2012, ranging from 50 to 80 months and 6–12 months, respectively. ENSO and SEWDI showed negative correlation between 10–14 months and 16–32 months in 1992–1994 and 1996–1998, respectively, and positive correlation between 60–70 months, 16–26 months and 6–14 months in 1996–2015, 2004–2008 and 2006–2013. PNA and SEWDI showed a negative correlation between 10–16 months and 18–24 months in 2001-2002 and 2003-2006, and a positive correlation between 64–70 months in 1994–2007. There 

**Scientific Reports** |        (2024) 14:28900 

11 

| https://doi.org/10.1038/s41598-024-76988-5 

www.nature.com/scientificreports/ 



**Fig. 9** . Dynamic evolution of the most severe ecological drought event (the 90th event) from 1982 to 2015. It was drawn by ArcGIS 10.6.1 (https://desk top.arcgis.c om/zh-cn/des ktop/index. html). 



**Fig. 10** . 3D perspective 90th ecological drought event. It was drawn by Origin 2022  ( h t t p s : / / w w w . o r i g i n l a b . c o m / 2 0 2 2 ) . 

was a negative correlation between SOI and SEWDI for 60–80 months from 1995 to 2004. During the period 1982–2015, Sunspot and SEWDI have short intermittent resonance periods of 1–8 months. TPI and SEWDI showed a positive correlation between 60–80 months and 16–20 months in 1994–2006 and 2003–2009, and a negative correlation between 16 and 32 months in 1993–1997. In summary, the cross wavelet transform method can effectively identify the dynamic relationship between teleconferential factors and ecological drought. There is a significant correlation between teleconnecting factors and SEWDI, indicating that they are indispensable factors in the development of ecological drought in IRB. Overall, ENSO has the greatest impact on SEWDI. 

It was drawn by MATLAB R2022b  ( h t t p s : / / w w 2 . m a t h w o r k s . c n / h e l p / w a v e l e t / r e f / w c o h e r e n c e . h t m l ? s _ t i d = d o c _ t a ) . 

There was a negative correlation between AO and SEWDI for 32-50 months from 1985 to 1993 (Fig. 12). ENSO and SEWDI had a negative correlation of 16-32 months during 1988-1998, and a positive correlation of 70-80 months during 1996-2006. PNA and SEWDI have a short resting resonance period of 1-8 months. There was a positive correlation between SOI and SEWDI for 16-32 months from 1990 to 2000. There was a negative correlation between Sunspot and SEWDI for 16-50 months from 1985 to 1992. There was a negative correlation between TPI and SEWDI for 16-32 months from 1990 to 1998. 

It was drawn by MATLAB R2022b  ( h t t p s : / / w w 2 . m a t h w o r k s . c n / h e l p / w a v e l e t / r e f / w c o h e r e n c e . h t m l ? s _ t i d = d o c _ t a ) . 

**Scientific Reports** |        (2024) 14:28900 

12 

| https://doi.org/10.1038/s41598-024-76988-5 

www.nature.com/scientificreports/ 



**Fig. 11** . The cross wavelet transforms between the teleconnection factors and SEWDI. 



**Fig. 12** . The bivariate wavelet coherences between the teleconnection factors and SEWDI. 

## **Discussions** 

### **SEWDI assessment** 

This study selected SPI and SPEI to reflect the actual changes in meteorological elements, reflect the characteristics of the soil moisture change SSMI, scPDSI reflected a variety of water balance process, and this study constructed SEWDI. At different time scales, the reliability of SEWDI was quantitatively evaluated by comparing the r values of SPI, SPEI, SSMI, scPDSI, and SEWDI with SSIF. There are many indices to characterize vegetation growth, such as normalized vegetation index, net vegetation primary productivity, etc., but these indices can only represent the existing state of vegetation<sup>14,35,36</sup> , while Solar-induced Fluorescence<sup>37</sup> has the advantage of directly reflecting vegetation photosynthesis and related to the photosynthetic rate of vegetation directly<sup>38</sup> . When drought occurs, vegetation stomatal conductance decreases, photosynthesis efficiency decreases, and carbon 

**Scientific Reports** |        (2024) 14:28900 

13 

| https://doi.org/10.1038/s41598-024-76988-5 

www.nature.com/scientificreports/ 

sequestration capacity decreases. Therefore, taking SIF as vegetation index can more sensitively capture the effects of drought stress on vegetation growth. In order to reduce the impact of human activities in the process of vegetation change, referring to the research of Vicent-Serrano et al.<sup>39,40</sup> , SIF was standardized and transformed with a method similar to SPI to obtain SSIF, reflecting its multi-scale characteristics. 

The correlation coefficients between various drought index and SSIF at the scale of 1, 3, 6 and 12 months were shown in Fig 13. A positive correlation coefficient indicates that vegetation has a negative feedback to the drought process, that is, the greater the degree of drought, the worse the vegetation growth condition; while a greater correlation indicates that the drought process has a greater impact on vegetation. At each time scale, the r between the five drought index and SSIF were SEWDI>SPI> scPDSI> SSMI> SPEI from large to small, and the correlation coefficients increased with the increase of the time scale, indicating that vegetation was more sensitive to the drought index response over a long time scale. In addition, the correlation between SEWDI and other drought indexes is also high, reflecting the high credibility of SEWDI, which is convenient to combine with other standardized drought indexes to study the relationship between different types of drought, so it is a relatively ideal ecological drought assessment index. The correlation with SPI is the highest, because the IRB is located in the transition area between arid and semi-arid areas, with strong evapotranspiration capacity and scarce groundwater, and precipitation will directly affect the growth of vegetation<sup>41,42</sup> . 

The results showed that the probability of ecological drought gradually decreased after 2000, which may be related to the implementation of conservation policies such as returning grazing land to grassland in recent years. In order to curb grassland degradation since 2000, In the eastern of the IRB (Xilin Gol City), the Inner Mongolia Autonomous Region began to implement such policies as returning farmland to grassland, banning grazing, confining and transferring, strengthening grassland and benefiting grazing, and subsidizing and rewarding grassland ecological protection. 

It was drawn by R-4.4.1(https://cran .r-project.o rg/web/packa ges/corrplo t/vignettes/corrplot-intro.html). 

### **Restraint effect of driving factors on ecological water deficit** 

In order to clarify the influencing factors of drought, this study introduced the constraint line method to quantify and identify the heterogeneous constraints of different factors on drought intensity.As shown in Fig. 14, NDVI, 



**Fig. 13** . Pearson correlation coefficients representing the correlations between SPI, SPEI, SSMI, scPDSI, and SEWDI with SSIF. 

**Scientific Reports** |        (2024) 14:28900 

14 

| https://doi.org/10.1038/s41598-024-76988-5 

www.nature.com/scientificreports/ 

precipitation and temperature have a significant restraint effect on ecological water deficit<sup>43</sup> . The restraint line form between ecological water deficit and NDVI in IRB is convex wave type, indicating that with the increase of NDVI, the restraint effect on ecological water deficit is gradually enhanced, and the fitting degree _R_<sup>_2_</sup> of the restraint line exceeds 0.8 (0.95 in 1985, 0.86 in 1995, 0.94 in 2005, and 0.96 in 2015). The fitting effect is good. The restraint line between ecological water deficit and precipitation in IRB is convex wave type, which means that the restraint effect of precipitation increase on ecological water deficit is also gradually enhanced, and the fitting effect is better. The type of influence of specific humidity on ecological water deficit changed with time. In 1985, the restraint line shape of specific humidity and ecological water deficit was convex wave type, indicating that the restraint effect of specific humidity on ecological water deficit gradually increased with the increase of specific humidity, while in 1995, 2005 and 2015, the restraint form of specific humidity and ecological water deficit showed a weak convex wave type. When the solar radiation is small, the limiting effect on the ecological water deficit is weak, and with the increase of the solar radiation, the limiting effect on the ecological water deficit is enhanced. With the increase of temperature, the restraint effect of temperature on the maximum ecological water deficit is gradually weakened. 

Precipitation and temperature changes will directly affect vegetation transpiration and soil water evaporation<sup>44–46</sup> . When the precipitation supply is insufficient, the ecological water deficit will be higher than the average level of many years, and when the temperature continues to rise, the airflow will not condense into rain<sup>47,48</sup> , and it is easy to form a clear sky, while the increasing transparency of the atmosphere further weakens the reduction effect of clouds on solar radiation, causing the underlying surface temperature to rise, forming a vicious cycle, which will lead to ecological drought<sup>6,49</sup> . When NDVI changes<sup>50</sup> , for example, returning farmland to forest will increase the evapotranspiration of vegetation, resulting in an increase in ecological water deficit, which will also lead to ecological drought. The constraint line method can be used to quantify the impact degree of meteorological factors on ecological water shortage, which is conducive to understanding the relationship between influencing factors and ecological drought from the perspective of ecological mechanism, and deepening the understanding of drought impact mechanism. In this study, the constraint line method and cross wavelet analysis are used to achieve an accurate analysis of ecological drought driving factors. The correlation between teleconnecting factors and ecological drought can be analyzed by cross wavelet, and the causes of ecological drought can be revealed. In general, ENSO events are significantly related to drought<sup>52</sup> , but how to quantify the effects of teleconnecting factors on ecological drought is also a problem to be solved<sup>53,54</sup> . When ENSO events occur, they first affect the climate environment, and when the climate environment changes, vegetation will inevitably respond. 



**Fig. 14** . Restraint effect of driving factors on ecological water deficit in 1985, 1995, 2005 and 2015. It was drawn by R-4.4.1 (https: //cr a n.r-pro jec t.o rg/web/p ackages/ corrplot/ vignette s/cor rplot-intro.html). 

**Scientific Reports** |        (2024) 14:28900 

15 

| https://doi.org/10.1038/s41598-024-76988-5 

www.nature.com/scientificreports/ 

### **Uncertainty in the calculation of SEWDI** 

At present, the ecological drought index of the terrestrial system can be evaluated, or the vegetation index can be used to reflect the drought situation of vegetation, or the drought index can be constructed by combining various factors to represent the comprehensive drought<sup>11,14</sup> , but these indexes cannot directly reflect the role of vegetation in the water cycle of the ecosystem. Vegetation can not only reduce soil and water loss by trapping precipitation, but also regulate the regional hydrological cycle. When meteorological, hydrological factors and land vegetation change with time, the balance relationship between water demand and water consumption of vegetation will constantly change. By considering land surface hydrological factors and vegetation factors, and taking ecological water shortage as the entry point, this study constructs SEWDI by using a standardized transformation method similar to SPI. This index can reflect the multi-time scale characteristics of ecological drought and is convenient to combine with other standardized drought indexes to study the relationship between different types of drought. Therefore, it is an ideal ecological drought assessment index. 

Choudhury<sup>24</sup> believe that in vegetation, chlorophyll can absorb red light and leaf tissues reflect near-infrared light, while NDVI reflects the difference between the two adjacent bands in the spectrum of red and nearinfrared. The red band (TM Band3) is usually subtracted from the near-infrared band (TM Band4) and divided by the sum of reflections of the two bands. Groeneveld<sup>51</sup> converted NDVI into NDVI* and further improved the simulation effect of NDVI on actual evapotranspiration of vegetation by eliminating non-systematic changes. Therefore, this study used NDVI* to calculate the vegetation coefficient. However, the change of NDVI can not reflect the comprehensive response of vegetation to drought more accurately, and may overestimate the growth of vegetation. 

The calculation of SEWDI in this study still needs improvement. There were some uncertainties in using the product of vegetation coefficient Kc and potential evapotranspiration to characterize the ecological water requirement of vegetation. Due to the differences in rooting habits, xylem structure and stomatal conductance, water consumption rules and drought resistance of different types of vegetation, the ecological water deficit of different vegetation is somewhat different. The IRB has a large spatial span, a large difference in vegetation growth environment between the east and the west, and obvious spatial heterogeneity in the growth period. The division of the same growth period may cause errors in the estimation of ecological water requirements, while the central part of the basin is mostly desert steppe with single vegetation type, which has little impact on the calculation results. In addition, soil moisture, as an important water source in the process of vegetation growth, must be considered in ecological drought. In addition, soil water content is closely related to _ET0_ . When soil water is insufficient, evapotranspiration of vegetation will be restricted. In short, evapotranspiration, soil moisture and vegetation status are important indicators to reflect vegetation growth. In future work, we can further study how to couple these three indicators to make ecological drought monitoring more accurately. At the same time, the propagation of meteorological drought to ecological drought is also an important problem worth studying. 

### **Effects of climate change and human activities on ecological drought** 

Water and temperature are the two key factors affecting vegetation growth, which are directly related to the balance of supply and demand of the ecosystem, and temperature and water are the main factors affecting the demand side and the supply side, respectively. Qi et al. found that the Inner Mongolia Autonomous Region has become warmer and drier over the past six decades<sup>31</sup> . At the same time, the autonomous region has also implemented a series of ecological protection policies, such as the natural forest protection project and the "Three-North" shelterbelt policy implemented from 1991 to 2001, the establishment of nature reserves and biodiversity protection policies from 2005 to 2010, and the establishment of ecological function reserves in the lower reaches of Heihe River and the northern foot of Yinshan Mountain in 2015. These projects and policies had greatly increased the coverage area of vegetation in inland river basins, especially the project of returning farmland to forest and grassland ecological protection had played an important role, resulting in the increase of vegetation and greening. However, increasing temperature and decreasing moisture make vegetation stress more significant, which is one of the main reasons for the increase of ecological drought events in the twenty-first century. Regulators should do a better job of formulating policies to address climate change. 

## **Conclusions** 

In this study, SEWDI of the IRB was constructed based on ecological water deficit. Mann-Kendall trend test was used to analyze the temporal and spatial characteristics of ecological drought in the IRB. The ecological drought events and their characteristic variables were extracted from 1982 to 2015 by using 3D spatiotemporal clustering recognition method. The relationship between NDVI and climate factors and ecological water deficit was quantified by restraint line method. The results showed that: (1) The ecological drought in the IRB showed a weakening trend during 1982-2015, and the seasonal drought showed an upward trend in the west and a downward trend in the east, with the spring wetting trend being the most obvious. (2) More detailed characteristic variables of ecological drought events can be extracted based on 3D recognition method. A total of 133 drought events occurred in the IRB from 1982 to 2015, and the ecological drought events had a longer duration and intensity after the twenty-first century, among which the most serious ecological drought event occurred from June 2005 to February 2007, which lasted for 21 months. The drought intensity was 44.65 × 10<sup>5</sup> month·km<sup>2</sup> , and the drought area was 23.79 × 10<sup>4</sup> km<sup>2</sup> . The event occurred in June 2005, intensified in September 2005, attenuated in June 2006, re-intensified in August 2006 and re-attenuated (extinction) in February 2007, and the migration path of the drought center showed the characteristics of northeast propagation. (3)Among the teleconnecting factors, ENSO has the greatest effect on ecological drought in the IRB. (4) NDVI, precipitation and temperature are the most direct factors affecting ecological water deficit. The constraining effect of NDVI and precipitation on ecological water deficit is gradually enhanced with the increase of precipitation, the constraining effect 

**Scientific Reports** |        (2024) 14:28900 

16 

| https://doi.org/10.1038/s41598-024-76988-5 

www.nature.com/scientificreports/ 

of temperature on ecological water deficit is gradually enhanced with the increase of temperature, and the constraining effect of specific humidity and solar radiation on ecological water deficit is less. 

## **Data availability statement** 

Data available on request from the authors. The data that support the findings of this study are available from the corresponding author upon reasonable request. 

Received: 25 April 2024; Accepted: 18 October 2024 



## **References** 

1. Zhang, W. et al. Dynamic evolution and copula-based multivariable frequency analysis of meteorological drought considering the spatiotemporal variability in Northwestern China. _Water_ https://doi.org/10.3390/w15213861 (2023). 

2. Zhang, W. et al. Dynamic characteristics of meteorological drought and its impact on vegetation in an arid and semi-arid region. _Water_ https://doi.org/10.3390/w15223882 (2023). 

3. Zhang, Z. et al. Lag time and cumulative effects of climate factors on drought in North China Plain. _Water_ https://doi.org/10.3390/ w15193428 (2023). 

4. Jiang, T., Su, X., Zhang, G., Zhang, T. & Wu, H. Estimating propagation probability from meteorological to ecological droughts using a hybrid machine learning copula method. _Hydrol. Earth Syst. Sci._ **27** , 559–576. https://doi.org/10.5194/hess-27-559-2023 (2023). 

5. Tian, Q. et al. Copula-based comprehensive drought identification and evaluation over the Xijiang River Basin in South China. _Ecol. Indic._ **154** , 110503. https://doi.org/10.1016/j.ecolind.2023.110503 (2023). 

6. Wu, S.-W., Huang, H., Tsai, S.-F. & Lin, C.-Y. Identification of aeolian dust hotspots in the lower reaches of Zhuoshui river in Taiwan using environmental indicators. _Ecol. Ind._ **154** , 110864. https://doi.org/10.1016/j.ecolind.2023.110864 (2023). 

7. Ramirez, A. R. et al. Defining ecological drought for the twenty-first century. _Bull. Am. Meteor. Soc._ **98** , 2543–2550.  h t t p s : / / d o i . o r g / 1 0 . 1 1 7 5 / b a m s - d - 1 6 - 0 2 9 2 . 1 (2017). 

8. Park, S.-Y., Sur, C., Lee, J.-H. & Kim, J.-S. Ecological drought monitoring through fish habitat-based flow assessment in the Gam river basin of Korea. _Ecol. Indic._ **109** , 105830. https://doi.org/10.1016/j.ecolind.2019.105830 (2020). 

9. McEvoy, J. et al. Ecological drought: Accounting for the non-human impacts of water shortage in the upper missouri headwaters Basin, Montana, USA. _Resources_ https://doi.org/10.3390/resources7010014 (2018). 

10. Kim, J.-S., Jain, S., Lee, J.-H., Chen, H. & Park, S.-Y. Quantitative vulnerability assessment of water quality to extreme drought in a changing climate. _Ecol. Indic._ **103** , 688–697. https://doi.org/10.1016/j.ecolind.2019.04.052 (2019). 

11. Li, C. et al. Spatial and temporal variations of drought in Sichuan Province from 2001 to 2020 based on modified temperature vegetation dryness index (TVDI). _Ecol. Indic._ **139** , 108883. https://doi.org/10.1016/j.ecolind.2022.108883 (2022). 

12. Przeździecki, K., Zawadzki, J. J., Urbaniak, M., Ziemblińska, K. & Miatkowski, Z. Using temporal variability of land surface temperature and normalized vegetation index to estimate soil moisture condition on forest areas by means of remote sensing. _Ecol. Indic._ **148** , 110088. https://doi.org/10.1016/j.ecolind.2023.110088 (2023). 

13. Xu, Y. et al. Identification of ecologically sensitive zones affected by climate change and anthropogenic activities in Southwest China through a NDVI-based spatial-temporal model. _Ecol. Indic._ **158** , 111482. https://doi.org/10.1016/j.ecolind.2023.111482 (2024). 

14. Zhang, Y., Zhang, L., Wang, J., Dong, G. & Wei, Y. Quantitative analysis of NDVI driving factors based on the geographical detector model in the Chengdu-Chongqing region, China. _Ecol. Indic._ **155** , 110978. https://doi.org/10.1016/j.ecolind.2023.110978 (2023). 

15. Griffin-Nolan, R. J. et al. Shifts in plant functional composition following long-term drought in grasslands. _J. Ecol._ **107** , 2133–2148. https://doi.org/10.1111/1365-2745.13252 (2019). 

16. Chen, J., Yang, H., Jin, T. & Wu, K. Assessment of terrestrial ecosystem sensitivity to climate change in arid, semi-arid, sub-humid, and humid regions using EVI, LAI, and SIF products. _Ecol. Indic._ **158** , 111511 (2024). 

17. Zhong, S., Sun, Z. & Di, L. Characteristics of vegetation response to drought in the CONUS based on long-term remote sensing and meteorological data. _Ecol. Indic._ **127** , 107767. https://doi.org/10.1016/j.ecolind.2021.107767 (2021). 

18. Zou, L., Cao, S., Zhu, Z. & Sanchez-Azofeifa, A. Assessment of the response of tropical dry forests to El Niño southern oscillation. _Ecol. Indic._ **133** , 108390. https://doi.org/10.1016/j.ecolind.2021.108390 (2021). 

19. Sandeep, P., Obi Reddy, G. P., Jegankumar, R. & Arun Kumar, K. C. Monitoring of agricultural drought in semi-arid ecosystem of Peninsular India through indices derived from time-series CHIRPS and MODIS datasets. _Ecol. Indic._ **121** , 107033.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . e c o l i n d . 2 0 2 0 . 1 0 7 0 3 3 (2021). 

20. Li, W., Duan, L., Luo, Y., Liu, T. & Scharaw, B. Spatiotemporal characteristics of extreme precipitation regimes in the Eastern Inland River Basin of inner mongolian plateau, Chuna. _Water_ https://doi.org/10.3390/w10010035 (2018). 

21. Wang, H., Chen, Y., Pan, Y. & Li, W. Spatial and temporal variability of drought in the arid region of China and its relationships to teleconnection indices. _J. Hydrol._ **523** , 283–296. https://doi.org/10.1016/j.jhydrol.2015.01.055 (2015). 

22. Chen, S. & Zha, X. Effects of the ENSO on rainfall erosivity in the Fujian Province of southeast China. _Sci. Total Environ._ **621** , 1378–1388. https://doi.org/10.1016/j.scitotenv.2017.10.090 (2018). 

23. Jiang, T., Su, X., Zhang, G., Zhang, T. & Wu, H. https://doi.org/10.5194/hess-2022-78 

24. Choudhury, B. J., Ahmed, N. U., Idso, S. B., Reginato, R. J. & Daughtry, C. S. T. Relations between evaporation coefficients and vegetation indices studied by model simulations. _Remote Sens. Environ._ **50** , 1–17. https://doi.org/10.1016/0034-4257(94)90090-6 (1994). 

25. Liu, Y. et al. Understanding the spatiotemporal links between meteorological and hydrological droughts from a three-dimensional perspective. _J. Geophys. Res. Atmos._ **124** , 3090–3109. https://doi.org/10.1029/2018jd028947 (2019). 

26. Han, Z. et al. Propagation dynamics from meteorological to groundwater drought and their possible influence factors. _J. Hydrol._ **578** , 124102. https://doi.org/10.1016/j.jhydrol.2019.124102 (2019). 

27. Chen, Y. et al. Spatial-temporal dynamics of grassland net primary productivity and its driving mechanisms in Northern Shaanxi, China. _Agronomy_ https://doi.org/10.3390/agronomy13112684 (2023). 

28. Gao, Y. et al. Identifying the spatio-temporal pattern of drought characteristics and its constraint factors in the Yellow River Basin. _Ecol. Indic._ https://doi.org/10.1016/j.ecolind.2023.110753 (2023). 

29. Wang, S., Li, R., Wu, Y. & Zhao, S. Effects of multi-temporal scale drought on vegetation dynamics in Inner Mongolia from 1982 to 2015, China. _Ecol. Indic._ https://doi.org/10.1016/j.ecolind.2022.108666 (2022). 

30. Li, B., Chen, Y., Shi, X., Chen, Z. & Li, W. Temperature and precipitation changes in different environments in the arid region of northwest China. _Theor. Appl. Climatol._ **112** , 589–596. https://doi.org/10.1007/s00704-012-0753-4 (2013). 

31. Hu, Q. et al. Spatial analysis of climate change in Inner Mongolia during 1961–2012, China. _Appl. Geogr.phy_ **60** , 254–260.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . a p g e o g . 2 0 1 4 . 1 0 . 0 0 9 (2015). 

32. Zhang, W. et al. Temporal and spatial evolution of meteorological drought in inner Mongolia Inland River Basin and its driving factors. _Sustainability_ https://doi.org/10.3390/su16052212 (2024). 

**Scientific Reports** |        (2024) 14:28900 

17 

| https://doi.org/10.1038/s41598-024-76988-5 

www.nature.com/scientificreports/ 

33. Zhang, Z., Ju, W. & Zhou, Y. The effect of water stress on net primary productivity in northwest China. _Environ. Sci. Pollut. Res. Int._ **28** , 65885–65898. https://doi.org/10.1007/s11356-021-15314-2 (2021). 

34. Zheng, S. et al. The trend towards a warmer and wetter climate observed in arid and semi-arid areas of northwest China from 1959 to 2019. _Environ. Res. Commun._ https://doi.org/10.1088/2515-7620/ac39f7 (2021). 

35. Wang, F. et al. Spatial and temporal evolutions of terrestrial vegetation drought and the influence of atmospheric circulation factors across the Mainland China. _Ecol. Indic._ **158** , 111455. https://doi.org/10.1016/j.ecolind.2023.111455 (2024). 

36. Yu, D. et al. Spatiotemporal variation of net primary productivity and its response to drought in Inner Mongolian desert steppe. _Global Ecol. Conserv._ https://doi.org/10.1016/j.gecco.2021.e01991 (2022). 

37. Zhang, X. et al. Drought propagation under global warming: Characteristics, approaches, processes, and controlling factors. _Sci. Total Environ._ **838** , 156021. https://doi.org/10.1016/j.scitotenv.2022.156021 (2022). 

38. Mohammed, G. H. et al. Remote sensing of solar-induced chlorophyll fluorescence (SIF) in vegetation: 50 years of progress. _Remote Sens. Environ._ **231** , 111177. https://doi.org/10.1016/j.rse.2019.04.030 (2019). 

39. Vicente-Serrano, S. M. et al. Global assessment of the standardized evapotranspiration deficit index (SEDI) for drought analysis and monitoring. _J J. Climate._ **31** , 5371–5393. https://doi.org/10.1175/JCLI-D-17-0775.1 (2018). 

40. Zhang, J. et al. Solar-induced chlorophyll fluorescence captures photosynthetic phenology better than traditional vegetation indices. _ISPRS J. Photogramm. Remote Sens._ **203** , 183–198. https://doi.org/10.1016/j.isprsjprs.2023.07.021 (2023). 

41. Deng, Y., Wu, D., Wang, X. & Xie, Z. Responding time scales of vegetation production to extreme droughts over China. _Ecol. Indic._ https://doi.org/10.1016/j.ecolind.2022.108630 (2022). 

42. Bushra, N. et al. The relationship between the normalized difference vegetation index and drought indices in the South Central United States. _Nat. Hazards_ **96** , 791–808. https://doi.org/10.1007/s11069-019-03569-5 (2019). 

43. Wang, Q. et al. Assessing the impacts of drought on grassland net primary production at the global scale. _Sci. Rep._ **9** , 14041.  h t t p s : / / d o i . o r g / 1 0 . 1 0 3 8 / s 4 1 5 9 8 - 0 1 9 - 5 0 5 8 4 - 4 (2019). 

44. Li, M. et al. Drought reduces the effectiveness of ecological projects: Perspectives from the inter-annual variability of vegetation index. _Ecol. Indic._ **130** , 108158. https://doi.org/10.1016/j.ecolind.2021.108158 (2021). 

45. Ling, M., Guo, X., Shi, X. & Han, H. Temporal and spatial evolution of drought in Haihe River Basin from 1960 to 2020. _Ecol. Indic._ **138** , 108809. https://doi.org/10.1016/j.ecolind.2022.108809 (2022). 

46. Ni, X., Guo, W., Li, X. & Li, S. Heterogeneity of increases in net primary production under intensified human activity and climate variability on the loess plateau of China. _Remote Sens._ https://doi.org/10.3390/rs14194706 (2022). 

47. Ren, H. et al. Vegetation response to changes in climate across different climate zones in China. _Ecol. Indic._ **155** , 110932.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . e c o l i n d . 2 0 2 3 . 1 1 0 9 3 2 (2023). 

48. Wan, F., Zhang, F., Wang, Y., Peng, S. & Zheng, X. Study on the propagation law of meteorological drought to hydrological drought under variable time Scale: An example from the Yellow River Water Supply Area in Henan. _Ecol. Indic._ **154** , 110873.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . e c o l i n d . 2 0 2 3 . 1 1 0 8 7 3 (2023). 

49. Wang, D. et al. Drought resistance of vegetation and its change characteristics before and after the implementation of the grain for green program on the loess plateau, China. _Remote Sens._ https://doi.org/10.3390/rs14205142 (2022). 

50. Ren, Y., Zhang, F., Zhao, C. & Cheng, Z. Attribution of climate change and human activities to vegetation NDVI in Jilin Province, China during 1998–2020. _Ecol. Indic._ **153** , 110415. https://doi.org/10.1016/j.ecolind.2023.110415 (2023). 

51. Groeneveld, D. P., Baugh, W. M., Sanderson, J. S. & Cooper, D. J. Annual groundwater evapotranspiration mapped from single satellite scenes. _J. Hydrol._ **344** , 146–156. https://doi.org/10.1016/j.jhydrol.2007.07.002 (2007). 

52. Zhang, K., Xie, X., Zhu, B., Meng, S. & Yao, Y. Unexpected groundwater recovery with decreasing agricultural irrigation in the Yellow River Basin. _Agric. Water Manag._ **213** , 858–867. https://doi.org/10.1016/j.agwat.2018.12.009 (2019). 

53. Lin, M., Biswas, A. & Bennett, E. M. Spatio-temporal dynamics of groundwater storage changes in the Yellow River Basin. _J. Environ. Manag._ **235** , 84–95. https://doi.org/10.1016/j.jenvman.2019.01.016 (2019). 

54. Yin, L. et al. Interaction between groundwater and trees in an arid site: Potential impacts of climate variation and groundwater abstraction on trees. _J. Hydrol._ **528** , 435–448. https://doi.org/10.1016/j.jhydrol.2015.06.063 (2015). 

## **Author contributions** 

Conceptualization, Z.Z. and K.F.; data interpretation and methodology, J.L. and K.F.; validation, K.F.; F.W. and H.G.; software, W.Z. and S.W.; original draft preparation, J.L.; funding acquisition, K.F. and W.Z.; All authors have read and agreed to the published version of the manuscript. 

## **Declarations** 

## **Competing interests** 

The authors declare no competing interests. 

## **Additional information** 

**Correspondence** and requests for materials should be addressed to K.F. 

**Reprints and permissions information** is available at www.nature.com/reprints. 

**Publisher’s note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

**Open Access** This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit  h t t p : / / c r e a t i v e c o m m o n s . o r g / l i c e n s e s / b y - n c - n d / 4 . 0 / . 

#### © The Author(s) 2024 

**Scientific Reports** |        (2024) 14:28900 

18 

| https://doi.org/10.1038/s41598-024-76988-5 

