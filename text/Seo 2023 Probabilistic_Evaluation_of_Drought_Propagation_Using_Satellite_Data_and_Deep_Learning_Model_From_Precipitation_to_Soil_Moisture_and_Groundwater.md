6048 

IEEE JOURNAL OF SELECTED TOPICS IN APPLIED EARTH OBSERVATIONS AND REMOTE SENSING, VOL. 16, 2023 

## Probabilistic Evaluation of Drought Propagation Using Satellite Data and Deep Learning Model: From Precipitation to Soil Moisture and Groundwater 

Jae Young Seo and Sang-II Lee 

**_Abstract_ — The frequency of drought events has increased with climate change, making it vital to monitor and predict the response to drought. In particular, the relationship among meteorological, agricultural, and groundwater droughts needs to be characterized under different drought conditions. In this study, a probabilistic framework was developed for analyzing the spatio-temporal propagation of droughts and applied to South Korea. Three drought indices were calculated using satellite data and a deep learning model to determine the spatial and temporal extents of drought. The average propagation times were calculated. The time from meteorological to agricultural drought (MD-to-AD) was 2.83 months, and that from meteorological to groundwater drought (MD-to-GD) was 4.34 months. Next, the joint distribution among three drought types based on the best-fit copula functions was constructed. The conditional probabilities of drought occurrence were calculated on temporal and spatial scales. For instance, the probabilities of MD-to-GD propagation under light, moderate, severe, and extreme meteorological drought conditions were 38%, 43%, 48%, and 53%, respectively. The propagated drought occurrence probability was confirmed to be the highest under extreme antecedent drought conditions. The results of this study provide insight into the spatiotemporal drought propagation process from a probabilistic viewpoint. The use of satellite data and a deep learning model is expected to increase the efficiency of drought management practices such as vulnerability assessment and early warning system development.** 

**_Index Terms_ —Deep learning, groundwater drought, probability, propagation, satellite.** 

### I. INTRODUCTION 

ROUGHT is often caused by meteorological conditions **D** changes, such as a deficiency of precipitation or high temperature-related evaporation [1], [2], which results in water cycle imbalance and repeated water shortages. It significantly affects various domains, such as water resources, the environment, agriculture, and ecology [3]. On a broad and frequent scale, due to accelerating climate change, drought can lead to serious disasters [4]. 

# **D** 

A prolonged lack of precipitation and high temperatures can cause meteorological drought, which may lead to agricultural 

Manuscript received 6 March 2023; revised 1 May 2023; accepted 25 June 2023. Date of publication 29 June 2023; date of current version 11 July 2023. This work was supported by the National Research Foundation of Korea grant funded by the Korean government (MSIT) (NRF-2022R1C1C2004417 and NRF-2021R1A2C2011193). _(Corresponding author: Sang-II Lee.)_ 

The authors are with the Department of Civil and Environmental Engineering, Dongguk University, Seoul 04620, South Korea (e-mail: dabbi2011@naver.com; islee@dongguk.edu). 

Digital Object Identifier 10.1109/JSTARS.2023.3290685 

drought because low soil moisture affects vegetation growth [5]. Subsequently, a reduction in the available amount of water in streams and soils may result in groundwater drought [6]. 

Drought propagation is the mechanism whereby droughts occur successively along the hydrological cycle. It refers primarily to the temporal movement and spatial expansion of droughts from meteorological to agricultural and groundwater conditions [5], [7], [8], [9]. Monitoring and predicting the propagation of groundwater droughts have become increasingly important because of the increasing demand for groundwater. Generally, groundwater drought occurs as a consequence of precipitation deficits (meteorological drought) and soil moisture dryness (agricultural drought) along the vertical profile of terrestrial water storage. However, groundwater drought has not attracted extensiveresearchattention,becauseofitscomplexcharacteristics. Moreover, the data available for previous studies on groundwater drought were insufficient, and the modeling covered only small areas [6], [10], [11]. Bloomfield and Marchant [12] proposed a standardized groundwater index (SGI) that allows groundwater drought to be easily monitored, facilitating relevant studies. Accordingly,theanalysisandevaluationofgroundwaterdrought became feasible considering the temporal and spatial correspondences according to various types of drought occurrences. 

Drought analysis mainly involves the use of calculated index data from point-based meteohydrological observations to analyze drought conditions, duration, severity, and frequency. However, it is difficult to use such point-based monitoring data in spatio-temporal drought analysis, and there are uncertainties when the spatial drought distribution is obtained using interpolation [13], [14]. Drought status from various perspectives (meteorological, agricultural, and groundwater droughts) can be determined using satellite data with space-time continuity, even at locations without observation points [13], [14]. In recent years, drought analyses based on satellite data have been conducted. For example, researchers have analyzed meteorological drought using precipitation observation satellites [e.g., tropical rainfall measuring mission (TRMM) and global precipitation measurement(GPM)] [15], [16], [17];agriculturaldroughtusing soil moisture, evapotranspiration, and vegetation indices from Landsat, the moderate resolution imaging spectrometer, the advanced microwave scanning radiometer 2, and soil moisture active passive [18], [19], [20]; and groundwater drought using terrestrial water storage changes measured by gravity recovery and climate experiment (GRACE) satellites [21], [22], [23]. 

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4.0/ 

6049 

SEO AND LEE: PROBABILISTIC EVALUATION OF DROUGHT PROPAGATION USING SATELLITE DATA AND DEEP LEARNING MODEL 

Several studies have focused on developing methodologies for more accurately monitoring and predicting spatio-temporal changes in groundwater storage using geostatistical or machine/deep learning models to overcome the relatively low resolution of GRACE [24], [25], [26], [27], [28]. Seo and Lee [25] used an artificial neural network model to analyze changes in groundwater storage. They estimated the gridded SGI in South Korea from 2003 to 2015 based on groundwater storage estimations and compared SGI with meteorological drought indices. In another study, Seo and Lee [26] developed and validated satellite-based deep learning models for predicting groundwater storage changes by considering meteorological, vegetation, and hydrological factors in South Korea from 2003 to 2019. 

Most previous studies on the relationships between different typesofdroughtindiceshavefocusedoncorrelationcoefficients, autocorrelation coefficients, and cross wavelets [29], [30], [31], [32], [33]. Barker et al. [30] investigated relationship between meteorological and hydrological droughts at various temporal scales using correlation analysis and confirmed a correlation between droughts. Bhardwaj et al. [32] estimated the propagation time, development, and recovery rate from meteorological to hydrological droughts in India and found that seasonality and baseflow indices significantly affected drought propagation. Li et al. [33] constructed a framework of droughts (meteorological and hydrological) propagation time analysis based on cross wavelet and random forest algorithm and found that the seasonal dynamics of drought propagation were considerably affected by human activity. 

However, the analysis of the correlation between drought indices could not clearly explain their relationship with drought propagation. Thus, it is essential to develop a procedure for the probabilistic analysis of drought propagation. Fang et al. [34] analyzed vegetation vulnerability under meteorological drought conditions using probabilistic framework. Shin et al. [35] constructed a forecasting framework of hydrological drought based on Bayesian networks that consider drought propagation relationships. Wang et al. [36] examined three types of probabilistic propagation relationship between meteorological and hydrological droughts. Although these methods provide insights into drought propagation, studies on the probabilistic propagation analysis of spatio-temporal groundwater droughts under various preceding conditions are lacking. 

In this study, meteorological, agricultural, and groundwater droughts were characterized using a probabilistic approach based on satellite data and a deep learning model to analyze drought propagation relationships. The specific objectives were to 1) estimate groundwater storage changes using a satellitebased deep learning model, 2) analyze three drought types using multisatellite data, 3) estimate the propagation time between droughts, and 4) determine drought propagation probabilities using the best-fit copula function. 

### II. STUDY AREA AND DATA 

### _A. Study Area_ 

Of the 117 mid-watersheds in South Korea, 110 watersheds were investigated in this study [Fig. 1(a)]. Three watersheds near 



Fig. 1. Study area. (a) Mid-watersheds and major rivers. (b) Groundwater observation wells and DEM. 

the border of North Korea and four watersheds on Jeju Island were excluded [grayed in Fig. 1(a)]. South Korea experiences substantial seasonal temperature and precipitation variations owing to its monsoon climate characteristics (cold and dry climate in December–February and hot and wet climate in June– August), with approximately 70% of the annual precipitation occurring during summer. The annual average precipitation and temperature from 1912 to 2017 were 1237.4 mm and 13.2 °C, respectively [37]. In the past 30 years, the temperature and precipitation have increased by approximately 1.4 °C and 124 mm, respectively, compared with those in the early 20th century (1912–1941), and the variability during this period was high [37]. 

More than 65% of the land area consists of forests and mountainous terrain, particularly in the eastern and southern areas [corresponding to high values in the digital elevation model (DEM); Fig. 1(b)]. The persistence of long-term drought increases the risk of forest fires due to high water stress and dryness of the air and forests. 

### _B. Data_ 

_1) Remote Sensing Data:_ Table I presents the remote sensing data used to estimate groundwater storage changes and calculate various drought indices. The 3B43V7 monthly precipitation data from TRMM jointly developed by the National Aeronautics and Space Administration (NASA) and the Japan Aerospace Exploration Agency (JAXA) were used. The data were acquired from the Goddard Earth Sciences Data and Information Service Center (GES DISC). TRMM 3B43 data were combined with observations from the Global Precipitation Climatology Center (GPCC), 3B42 data (3-h precipitation data of TRMM), and gridded data produced by the Climate Prediction Center of the National Oceanic and Atmospheric Administration (NOAA). The 3B43 data had a spatial resolution of 0.25° for the regions from 50°S to 50°N and 180°W to 180°E. 

Landsat 5 and Landsat 8 satellite data with a 30 m spatial resolution were used to monitor various inland covers [modified normalized difference water index (MNDWI) and normalized 

6050 

IEEE JOURNAL OF SELECTED TOPICS IN APPLIED EARTH OBSERVATIONS AND REMOTE SENSING, VOL. 16, 2023 

TABLE I 

DETAILS OF THE REMOTE SENSING DATASET USED IN THIS STUDY 



difference vegetation index (NDVI)]. A total of 2652 images including South Korea were obtained from the USGS Earth Explorer [38] from January 2003 to February 2013 (Landsat 5) and from March 2013 to December 2019 (Landsat 8). Radiometric and atmospheric corrections were calibrated using the Fast Line-of-sight Atmospheric Analysis of Spectral Hypercubes (FLAASH) algorithm. For missing data, images were averaged to produce monthly MNDWI and NDVI values, and the images were resampled using the nearest-neighbor average. 

Global Land Data Assimilation System (GLDAS) provides meteorological and hydrological data on the land surface. Owing to the high accuracy of the land surface model, these data are widely used for analyses of climate change, the water cycle, and weather forecasting. In this study, the Noah product (GLDAS_Noah025_M) from GLDAS 2.1 version with a monthly spatial resolution of 0.25° was used, which included the average temperature and four soil moisture layers (0–10, 10–40, 40–100, and 100–200 cm). 

Terrestrial water storage anomaly (TWSA) was estimated using GRACE and GRACE-follow-on (GRACE-FO) of the Center for Space Research (CSR) RL06 mascon data with a 0.25° spatial resolution. Compared with the previous GRACE spherical harmonic-based processing method, the mass concentration (mascon) processing method was corrected to account for the Earth’s ellipsoidal shape. This better preserves the improved signals and low leakage errors compared with other products [39], [40]. Because data were missing between GRACE and GRACE-FO for 14 months, temporal gaps were filled using cubic spline interpolation [26]. 

_2) Groundwater Observation Data:_ The basic data observed in the National Groundwater Observation Monitoring Network (NGMN) in South Korea include the monthly groundwater level, groundwater temperature, and electrical conductivity of the groundwater. Fig. 1(b) represents the groundwater observation wells used in this study. A total of 166 stations with observational data (considering the study period: January 2003 to December 2019) were selected among the total groundwater 

stations. The groundwater observation wells of the NGMN were subjected to alluvial and bedrock aquifer measurements accordingtothedepthoftheaquifer,andthebedrockandalluvial layers were simultaneously observed at 95 of the 166 selected stations. Changes in the water cycle and groundwater storage were generally more strongly correlated in the alluvial layer than in the deep bedrock layer. Therefore, alluvial layer data were used for the observation stations with both bedrock and alluvial aquifer observation wells. For each watershed, the groundwater level data obtained were transformed into groundwater storage changes via multiplication by the specific yield values. Specific yield was estimated using a detailed soil texture classification map from the National Institute of Agricultural Sciences and the Korean Rural Development Administration (RDA), along with range values based on the soil texture, as reported by Johnson [41] and Loheide II et al. [42]. 

### III. METHODOLOGY 

### _A. Satellite-Based Deep Learning for Groundwater Storage Changes_ 

The procedure of the groundwater prediction framework using the satellite-based deep learning model is illustrated in Fig. 2 (Step 1). The deep learning model used for this analysis was a convolutional neural network–long short-term memory (CNN–LSTM) model based on multisatellite data from 2003 to 2019,whichwasdevelopedbySeoandLee [26] forSouthKorea. The satellite-based predictor variables included the precipitation, temperature, NDVI, MNDWI, soil moisture content, and TWSA, and the response variable was the groundwater storage changes (GWSC). The prediction model was trained using the Adam optimizer with a rectified linear unit (ReLU) activation function to minimize the loss function (mean squared error). The hyper-parameters (lag time, number of epochs, nodes, filters, hidden layers, and batch size) were tuned to achieve optimal performance using Bayesian optimization. 

### _B. Drought Index Calculation_ 

_1) Meteorological Drought Index:_ The standardized precipitation index (SPI) can express meteorological drought conditions using the probability distribution of precipitation [43]. Cumulative precipitation data for various time scales (1–24 months) were fitted to the gamma distribution (1), after which they were converted into a normal distribution. 



In (1), _x_ represents the accumulated precipitation ( _x >_ 0), _α_ is a shape parameter, and _β_ is a scale parameter. The mean of the normalized probability distribution model was 0, allowing comparisons of the drought time series and severity among the regions. Table II presents the classification of drought conditions basedontheSPI.TheSPIforeachmid-watershedwascalculated by converting 0.25° precipitation data from the TRMM satellite according to the weight of the area in this study. Because the frequency of drought events decreases as the time scale of drought increases, the analysis of drought events with longer time scales 

6051 

SEO AND LEE: PROBABILISTIC EVALUATION OF DROUGHT PROPAGATION USING SATELLITE DATA AND DEEP LEARNING MODEL 



Fig. 2. Proposed framework in this study. 

TABLE II 

DROUGHT CONDITIONS FOR THE SPI, SSMI, AND SGI 







may not provide significant statistical results. Therefore, this study analyzed meteorological drought on a one-month time scale to identify the number of propagated drought events. 

_2) Agricultural Drought Index:_ The persistence of meteorological drought results in agriculture-related soil moisture deficiencies and increases moisture stress during vegetation growth. The standardized soil moisture index (SSMI) is an agricultural drought indicator that has been validated in previous studies [44], [45] and can express soil moisture deficit condition. We integrated four layers of soil moisture data from GLDAS Noah_025_M at 0.25° and used them to calculate the SSMI. The mean and standard deviation of the multiyear soil moisture values for each grid in each calendar month were obtained by computing the grid-by-grid term series. The SSMI was calculated as follows: 



where _SMi,j_ represents the soil moisture for month _i_ and year _j_ , and _μi_ and _σi_ is the mean and standard deviation of the _SMi_ across all years, respectively. The gridded SSMI was converted into the SSMI for each mid-watershed. The SSMI drought conditions were identical to those for the SPI (Table II). 

_3) Groundwater Drought Index:_ Bloomfield and Marchant [12] proposed an SGI for the characterization of groundwater drought and analyzed groundwater drought by comparing the SGI and SPI of 14 groundwater observation stations using major aquifers in the United Kingdom. In contrast to precipitation data, groundwater data vary continuously and do not require accumulation during a specific period. As the monthly groundwater level or storage changes exhibit various data ranges and distributions for each station, it is difficult to fit the monthly probability distribution using a standard distribution and parameter estimation. In this study, the probability distribution of monthly GWSC predicted from the satellite-based deep learning model was estimated using kernel density estimation (KDE), which is a nonparametric estimation method. When _xi_ is GWSC predictions, the probability density function for random variable _X_ can be obtained using the KDE as follows [46]: 



where _n_ is the number of data points, _K_ is the kernel function, and _h_ is the bandwidth, which is a smoothing parameter. Commonly used kernel functions include the normal, box, triangle, 

6052 

IEEE JOURNAL OF SELECTED TOPICS IN APPLIED EARTH OBSERVATIONS AND REMOTE SENSING, VOL. 16, 2023 

#### TABLE III 

COPULA FUNCTIONS USED IN THIS STUDY 





Fig. 3. Schematic of drought propagation. 

and Epanechnikov functions. In this study, a normal function was used and the bandwidth was set as 0.8. 

The cumulative distribution function (CDF) of the kernel distribution can be projected onto the inverse of the normal distribution to calculate the SGI. Table II presents the drought condition classifications based on the SGI. 

- _C. Drought Identification and Propagation_ 

The propagation time was estimated by comparing the peak differences among meteorological, agricultural, and groundwater droughts using the SPI, SSMI, and SGI (Fig. 3). It is necessary to analyze the linkage between droughts considering the 

temporal order of meteorological, agricultural, and groundwater droughts before calculating the propagation time. In this study, we used the temporal overlapping approach proposed by Liu et al. [9]. 

First,thethresholdwassetas _−_ 0.5(lightconditionofdrought; Table II) to capture the onset of the drought event. It was considered that a drought started if the index value was _< −_ 0.5 formorethanconsecutivetwomonthsandthatthedroughtended if the index value was _>_ 0 for two or more consecutive months. 

After the onset and end times of the three types of drought events were identified, the drought onset/end times and overlap time were used to investigate the presence of propagation links between meteorological drought to agricultural drought (MDto-AD), meteorological drought to groundwater drought (MDto-GD), and agricultural drought to groundwater drought (ADto-GD). If the temporal overlap of MD-to-AD, MD-to-GD, and AD-to-GD exceeds 0, droughts were considered to be linked [9], as defined by the following criteria: 





where _D_ ( _tMDO, tMDE_ ), _D_ ( _tADO, tADE_ ), and _D_ ( _tGDO, tGDE_ ) are the durations between the onset time ( _tMDO_ ) and end time ( _tMDE_ ) of meteorological drought events, the onset time ( _tADO_ ) and end time ( _tADE_ ) of agricultural drought events, 

6053 

SEO AND LEE: PROBABILISTIC EVALUATION OF DROUGHT PROPAGATION USING SATELLITE DATA AND DEEP LEARNING MODEL 



Fig. 4. (a) Time series of GWSC: CNN-LSTM versus in situ. The vertical dotted line divides the periods for training and test. (b) Performance of the CNN-LSTM model for the test period. 

and the onset time ( _tGDO_ ) and end time ( _tGDE_ ) of groundwater drought events, respectively. 



### _D. Conditional Probability Based on Copula Function_ 

The copula function was established by Sklar [47], and Archimedean and Elliptical families in copula were developed by Joe [48] and Nelsen [49]. Copula functions can couple more than two variables to identify the dependencies between them, particularly the relationship with the maximum or minimum point of the joint distribution [50], [51]. They can be used to analyze the dependencies between variables regardless of limitations on the marginal distributions. In this study, the copula function was used to analyze the occurrence probability of agricultural and groundwater droughts under meteorological drought conditions and that of groundwater drought under agricultural drought conditions (Step 3 in Fig. 2). 

According to Sklar [47], the joint distribution of antecedent and propagated droughts can be expressed as follows: 



where _FX,Y_ ( _x, y_ ) is the joint distributions, _C_ () is a copula function, and _FX_ ( _x_ ) and _FY_ ( _y_ ) are the CDFs of the marginal distributions. In the case of the propagation process from meteorological drought to agricultural or groundwater drought, _X_ is the SPI and _Y_ is the SSMI or SGI. For propagation from agricultural to groundwater drought, _X_ is the SSMI and _Y_ is the SGI. The marginal distributions of the SPI, SSMI, and SGI were set as the normal distribution because the drought indices had to follow the normal distribution in the calculation process. 

Nelsen [49] proposed five copulas (Gumbel, Clayton, Frank, Gaussian, and Student’s _t_ ) for probability distributions from 

Fig. 5. Time series and color maps of the monthly SPI, SSMI, and SGI. 

the Archimedean and Elliptical families, as shown in Table III. In this study, the parameter ( _θ_ ) of each copula function were calculatedusingthemaximumlikelihoodestimation.Thecopula that best captured the relationship between the drought indices was determined using the Akaike information criterion (AIC) and Bayesian information criterion (BIC). 

The framework produces a series of occurrence probabilities for drought propagation from diverse meteorological and agricultural drought conditions. Higher occurrence probabilities under drought conditions imply higher degrees of soil moisture and groundwater drought vulnerability. 

The conditional probability of droughts under preceding drought conditions can be derived using (8) and (9), given the joint probability distribution of the SPI, SSMI, and SGI [i.e., (7)] [34]. 



6054 

IEEE JOURNAL OF SELECTED TOPICS IN APPLIED EARTH OBSERVATIONS AND REMOTE SENSING, VOL. 16, 2023 



Fig. 6. Spatial distributions of the SPI, SSMI, and SGI from September 2008 to February 2009. 



Fig. 7. Average propagation time and the number of temporally overlapped drought events in each watershed for MD-to-AD, MD-to-GD, and AD-to-GD. 

The probabilities of drought propagation from a meteorological drought condition (light, moderate, severe, or extreme) to an agricultural or groundwater drought state (SSMI, SGI _< −_ 0.5) and from an agricultural drought condition to a groundwater drought state (SGI _< −_ 0.5) can be calculated using (8) and (9). 

### IV. RESULTS AND DISCUSSIONS 

### _A. Spatio-Temporal Distribution of Drought Indices_ 

The spatio-temporal characteristics of groundwater drought were analyzed using the GWSC predictions based on data from 

multiple satellites and a deep learning model (CNN-LSTM) through hyper-parameter optimization. Fig. 4(a) shows a comparison of the _in situ_ and deep learning model time series [training period (60%): January 2003 to February 2013; test period (40%): March 2013 to December 2019] results. To assess theaccuracyofthemodel,thetestresultswereexaminedinterms of the correlation coefficient ( _r_ ) and root mean square error (RMSE) between the _in situ_ and predicted GWSCs. Fig. 4(b) shows scatterplots showing the correlation. The _r_ and RMSE of the CNN-LSTM model-predicted GWSC and _in situ_ GWSC were 0.72 and 42.92 mm/month, respectively. The performance 

6055 

SEO AND LEE: PROBABILISTIC EVALUATION OF DROUGHT PROPAGATION USING SATELLITE DATA AND DEEP LEARNING MODEL 



Fig. 8. Determination of propagation times from temporally overlapped drought events in (a) Hyeongsan River Watershed (2008) and (b) Han River-Goyang watershed (2014). 

of the prediction model exhibited a significant positive correlation and small error. 

Fig. 5 shows the time series and color maps of the SPI (from the TRMM precipitation data), SSMI (from the GLDAS soil moisture data), and SGI (from the GWSC results based on multisatellite data and the deep learning model) across South Korea during the study period. The black line corresponds to the time series of the SPI, SSMI, and SGI, and the yellow to red bars indicate the drought conditions. The results revealed that meteorological, agricultural, and groundwater droughts occurred frequently during the study period. Droughts existed in the study area in 2008, 2012, 2014, 2015, and 2017 with severe or extreme conditions. 

As previously reported [12], [23], [30], the SPI, SSMI, and SGI are closely related but have differences. Severe or extreme meteorological and groundwater droughts occurred in 2008, whereas agricultural droughts were moderate. In addition, extreme meteorological and agricultural droughts occurred from 2017 to 2019, whereas groundwater droughts during this period were light or relatively insignificant. On the other hand, only groundwater drought showed a significantly more severe condition contrary to SPI or SSMI in 2004 and 2011. The occurrence of groundwater drought in the absence of meteorological or agricultural drought may be caused by the long propagation time due to the shortage of cumulative precipitation or the soil moisture depletion. Otherwise, groundwater drought could be attributable to anthropogenic factors such as groundwater extraction. 

Fig. 6 shows the spatial distributions of the SPI, SSMI, and SGI values for the period from September 2008 to February 2009, where the drought periods (SPI, SSMI, SGI _≤−_ 0.5) are 

exhibited varying in colors from yellow to dark red, in order of becoming worse drought condition. The southern region experienced severe or extreme meteorological drought in September 2008, and some severe droughts continued in November and December before recovery from the droughts in February 2009. Agricultural drought expanded throughout the central part of the region following the onset of severe or extreme drought conditions in the southern part in October 2008. In most areas, drought peaked in January 2009, and progressive recovery occurred in February. Groundwater droughts, which began in September 2008, were most severe in October and exhibited complete recovery in February, similar to meteorological droughts. 

The influence of agricultural droughts continued even after recovery from meteorological drought, whereas groundwater droughts tended to terminate immediately after recovery from meteorological drought. This may have been due to a reduction in the amount of groundwater pumping and the recovery of groundwater storage with the improvement of meteorological drought conditions. 

### _B. Analysis of Propagation Time Between Drought Events_ 

The overlapped drought events among meteorological, agricultural, and groundwater droughts were identified according to their temporal overlap using (4)–(6). The propagation time was calculated as the peak time difference between temporally overlapped drought events. The propagation times for MD-to-AD, MD-to-GD, and AD-to-GD were estimated for the temporally overlapped drought events. 

The propagation times and the number of overlapped drought events are shown in Fig. 7. The propagation time in the study 

6056 

IEEE JOURNAL OF SELECTED TOPICS IN APPLIED EARTH OBSERVATIONS AND REMOTE SENSING, VOL. 16, 2023 

area ranged from 1 to 8 months, and there was a lag time between meteorological, agricultural, and groundwater droughts. The average propagation time and the number of overlapped drought events for MD-to-AD, MD-to-GD, and AD-to-GD were 2.83, 4.34, and 4.54 months and 11.47, 11.86, and 12.32, respectively. 

For most watersheds, the time required for MD-to-GD propagation was longer than that for MD-to-AD propagation. The longest propagation time (MD-to-GD) was observed in the southern and northwestern areas, and the shortest propagation time (MD-to-AD) was observed in the northern and southcentral areas, which have mountainous terrain and near-natural conditions. The average propagation time of MD-to-AD was shorter than the average propagation time of MD-to-GD. This is attributed to be due to the hydrological processes in the vertical profile of terrestrial water storage. The number of MD-to-GD overlapped events exceeded the number of MD-to-AD overlapped events. This implies that groundwater droughts caused by human activity not only nature processes tend to affect meteorological conditions more rapidly than agricultural droughts, as mentioned in the previous section. 

The AD-to-GD average propagation time was longer than the MD-to-AD and MD-to-GD average propagation times. This is attributed to the fact that the MD-to-GD and AD-to-GD spatial distributions were relatively similar, whereas the AD-to-GD propagation time was longer in some central watersheds. In addition, the difference in peak time was larger than those for MD-to-AD and MD-to-GD because of the longer duration of agricultural drought compared with groundwater drought. The large number of AD-to-GD overlapped events indicated that agricultural and groundwater droughts were closely related. 

Fig. 8 shows time series of drought indices for two midwatersheds having temporally overlapped drought events. For the 2008 drought event [Fig. 8(a)] of the Hyeongsan River Watershed, the peaks of SSMI and SGI occurred 7 months after the peak of SPI at the same time. For the 2014 drought events of the Han River-Goyang watershed [Fig. 8(b)], the peak of the meteorological drought was observed 3 months before the peak of the agricultural drought and 8 months before the peak of the groundwater drought. In addition, there is a propagation time of 5 months between SSMI and SGI. As shown in Figs. 6 and 8(a), the agricultural drought in the Hyungsan River Watershed continued even after the groundwater drought ended. In the 2008 drought event, the duration of agricultural drought was significantly longer. 

### _C. Best-Fit Copula Function for Joint Distribution of Drought Indices_ 

The copula function was used to probabilistically quantify the monthly propagation of drought. The best-fit copulas were selected for each watershed according to the AIC and BIC goodness-of-fit test results (Fig. 9). 

Fig. 9(a) shows the number of selected copulas for each watershed for the five copula functions. The average AIC and BIC values for the 110 watersheds are shown in Fig. 9(b) and (c), respectively. The Frank copula function exhibited the smallest AIC and BIC values for describing the joint distribution between 



Fig. 9. Comparison of five copulas for different drought propagation types. (a) Histogram of the selected copula functions. Boxplots of (b) AIC and (c) BIC values. 

the SPI and SSMI (i.e., MD-to-AD). The Gaussian function showed the best-fit between SPI and SGI (MD-to-GD), and the Clayton function showed the best-fit between SSMI and SGI (AD-to-GD). Table IV presents the statistics of the best-fit copulas for the different drought propagation types. 

### _D. Conditional Probability of Drought Propagation_ 

The probabilities of drought propagation were calculated using the joint distribution with the best-fit copula function [(8) and 

6057 

SEO AND LEE: PROBABILISTIC EVALUATION OF DROUGHT PROPAGATION USING SATELLITE DATA AND DEEP LEARNING MODEL 

TABLE IV 

MEAN _±_ STANDARD DEVIATION OF THE AIC AND BIC VALUES FOR THE BEST-FIT COPULAS IN 110 WATERSHEDS 







(9)] under the four drought conditions (light, moderate, severe, and extreme), as shown in Table II. 

Fig. 10 shows the CDFs of the drought indices under different preceding conditions. The curves indicate that the probability of drought propagation was the highest when the preceding conditions were extreme (SPI, SSMI _< −_ 2.0). The SSMI conditions hardly affected SGI, compared with SPI-to-SSMI and SPI-to-SGI [Fig. 10(c)]. 

Table V presentstheaverageprobabilitiesofMD-to-AD,MDto-GD, and AD-to-GD propagation under various preceding drought conditions. The probability of MD-to-AD propagation ranged from 3% to 66% depending on the SPI value. MD-toGD propagation had a 6%–53% probability. Under agricultural drought conditions, the probability of groundwater drought occurrence was 6%–42%, which was lower than those of the other types of drought propagation. 

Although the number of AD-to-GD overlapped drought events was large, as shown in Fig. 7, the effects of the preceding conditions on the groundwater occurrence probability were less significant than those for MD-to-AD and MD-to-GD. This is considered to be because there are not often groundwater drought events that are worse than the severe condition in South Korea. In addition, drought analysis generally requires more than 30 years of data, and there was a lack of data for drought analysis from the study period (2003–2019). If continuous data are available, long-term probabilistic drought frequency analysis can be performed using the proposed methodology. 

Figs. 11–13 show drought occurrence probabilities given various preceding conditions on a spatial scale. Such information is useful for identifying the vulnerability and risk of each watershed. The probability of propagated drought occurrence is anticipated to increase as preceding drought conditions deteriorate. 

Thelikelihoodofagriculturaldroughtwashighinthesouthern part of the country, where agriculture was the dominant land use type (Fig. 11). The groundwater drought vulnerability under meteorological drought conditions was high in the western part and in a specific eastern watershed (Fig. 12). 

Generally, groundwater droughts occur less frequently than agricultural droughts as the meteorological conditions improve, because of reduced pumping and the consequent recovery of groundwater levels. Regarding the AD-to-GD propagation with respect to the preceding drought conditions, the probability of groundwater drought occurrence was lower than that of MD-toGD propagation throughout the region; however, the western and southern edges were prone to groundwater drought. In particular, Seoul (the capital of South Korea where groundwater 



Fig.10. ConditionalCDFofdroughtindicesunderdifferentprecedingdrought conditions. (a) MD-to-AD, (b) MD-to-GD, (c) AD-to-GD. 

use accounts for 6.2% of the national total) exhibited a high risk of agricultural droughts propagating into groundwater droughts (Fig. 13). 

Overall, the probability of agricultural and groundwater droughts increases as the preceding drought conditions get worsen. Quantification of conditional probabilities on a spatiotemporal scale, which was achieved by multisatellite data and a deep learning model in this study, can be useful for assessing vulnerability to drought and for efficient drought management. 

### _E. Discussions_ 

This study analyzed the propagation process from meteorological to agricultural and groundwater droughts, focusing 

6058 

IEEE JOURNAL OF SELECTED TOPICS IN APPLIED EARTH OBSERVATIONS AND REMOTE SENSING, VOL. 16, 2023 

TABLE V 

DROUGHT PROPAGATION PROBABILITY FOR VARIOUS PRECEDING DROUGHT CONDITIONS 





Fig. 11. Spatial distributions of the probability of agricultural drought under different meteorological (SPI) conditions. 



Fig. 12. Spatial distributions of the probability of groundwater drought under different meteorological (SPI) conditions. 

on the identification of drought type, propagation time, and conditional probability of drought occurrence. The conditional probability was calculated using the copula function, which has the advantage of describing complex dependencies between variables relatively easily. 

In other works studied the drought propagation in South Korea, the analysis was performed using traditional drought indices or copula functions: They include the bivariate frequency analysis using SPI and copula functions [52], the correlation analysis between SPI, Standardized Precipitation Evapotranspiration Index (SPEI), and Standardized Runoff Index (SRI) to estimate the future probability of drought propagation using climate change scenarios [53], the prediction of Palmer Hydrological Drought Index (PHDI) using SPI and Bayesian network [35], and the forecasting of SRI based on machine learning models [54]. These studies focused on drought analysis at point scales (weather stations) or in parts of watersheds and did not consider the groundwater drought. The novelty of this study 

is to analyze the spatio-temporal groundwater drought across South Korea using satellite data and a deep learning model, and to estimate the likelihood of propagation from meteorological or agricultural to groundwater droughts using a probabilistic approach. 

Although our approach can predict monthly groundwater storage changes and monitor spatio-temporal groundwater droughts, there is a need to improve the accuracy of the results due to the low spatial resolution of satellite data and cloud cover problems (especially Landsat). While the study covers a relatively large area including 110 mid-watersheds for a long period of time (from 2003 to 2019), the resolution of the GRACE and GRACEFO data only allows the estimation of groundwater storage changes with a spatial resolution of 0.25°. In future studies, the use of satellite data such as soil moisture or temperature, which have a higher spatial resolution and cover a longer period, as suggested in [55] and [56], may improve the accuracy of the analysis. 

6059 

SEO AND LEE: PROBABILISTIC EVALUATION OF DROUGHT PROPAGATION USING SATELLITE DATA AND DEEP LEARNING MODEL 



Fig. 13. Spatial distributions of the probability of groundwater drought under different agricultural (SSMI) conditions. 

different watersheds, indicating that the information provided by the tool presented herein can be useful for drought-related tasks such as vulnerability or risk assessment for drought management. 

In this study, we performed the probabilistic evaluation of drought propagation. Meteorological, agricultural, and groundwater droughts were identified via the corresponding indices calculated using multisatellite data and a deep learning model. The copula function was adopted to calculate the conditional probabilities of drought propagation from one state to another. The proposed probabilistic method along with the deep learning model using satellite data is useful for responding to large-scale droughts. Further research is needed to address the climate change effects and investigate the role of human activities on drought propagation. 

### ACKNOWLEDGMENT 

The authors would like to thank the anonymous reviewers whose suggestions and comments helped improve this article. 

### REFERENCES 

- [1] D. A. Wilhite and M. H. Glantz, “Understanding the drought phenomenon: The role of definitions,” _Water Int._ , vol. 10, no. 3, pp. 111–120, Jan. 1985, doi: 10.1080/02508068508686328. 

- [2] K. E. Trenberth, G. W. Branstator, and P. A. Arkin, “Origins of the 1988 North American drought,” _Science_ , vol. 242, no. 4886, pp. 1640–1645, Dec. 1988, doi: 10.1126/science.242.4886.1640. 

### V. CONCLUSION 

Meteorological drought can be understood as scarcity of precipitation; however, agricultural and groundwater droughts are complex phenomena caused by various natural and anthropogenic factors. For determining the relationships among these drought types, conventional temporal correlation analyses face limitations. 

To identify meteorological, agricultural, and groundwater droughts, drought indices (SPI, SSMI, and SGI) were calculated for 110 watersheds in South Korea using multiple satellite datasets and a deep learning model. The gridded precipitation data from the TRMM satellite were used for the SPI calculation, whereas the SSMI was calculated using soil moisture data from the GLDAS output. The SGI was calculated using a deep learning model (CNN-LSTM) with meteorological (precipitation and temperature), agricultural (MNDWI and NDVI), and hydrological (soil moisture content and TWSA) data obtained from multiple satellites (TRMM, GLDAS, Landsat, GRACE, and GRACE-FO). 

The average propagation times for MD-to-AD, MD-to-GD, and AD-to-GD were 2.83, 4.34, and 4.54 months, respectively. The occurrence probabilities for the different types of droughts under various preceding drought conditions were calculated; for instance, the occurrence probabilities of agricultural drought under different preceding SPI conditions (MD-to-AD) were 44%, 53%, 60%, and 66%, respectively. For MD-to-GD, the conditional probabilities were reduced to 38%, 43%, 48%, and 53%, respectively. Meanwhile, AD-to-GD propagation had lower probabilities of 36%, 39%, 40%, and 42%, respectively. In addition, the propagation times and probabilities for MD-to-AD, MD-to-GD, and AD-to-GD exhibited various change patterns in 

- [3] D. A. Wilhite, M. D. Svoboda, and M. J. Hayes, “Understanding the complex impacts of drought: A key to enhancing drought mitigation and preparedness,” _Water Resour. Manage._ , vol. 21, pp. 763–774, Jan. 2007, doi: 10.1007/s11269-006-9076-5. 

- [4] F. K. S˝onmez, A. U.<sup>˝</sup> K˝om˝usc˝u, A. Erkan, and E. Turgu, “An analysis of spatial and temporal dimension of drought vulnerability in Turkey using the standardized precipitation index,” _Natural Hazards_ , vol. 35, pp. 243–264, Jun. 2005, doi: 10.1007/s11069-004-5704-7. 

- [5] A.F. Van Loon, “Hydrological drought explained,” _WIREs Water_ , vol. 2, no. 4, pp. 359–392, Apr. 2015, doi: 10.1002/wat2.1085. 

- [6] H. A. J. Van Lanen and E. Peters, “Definition, effects and assessment of groundwaterdroughts,”in _DroughtandDroughtManagementinEurope_ ,J. V.VogtandF.Somma,Eds.,Norwell,MA,USA:Kluwer,2000,pp. 49–61. 

- [7] S. Joseph, A. K. Sahai, and B. N. Goswami, “Eastward propagating MJO during boreal summer and Indian monsoon droughts,” _Climate Dyn._ , vol. 32, pp. 1139–1153, Apr. 2008, doi: 10.1007/s00382-008-0412-8. 

- [8] W. Wang, M. W. Ertsen, M. D. Svoboda, and M. Hafeez, “Propagation of drought: From meteorological drought to agricultural and hydrological drought,” _Adv. Meteorol._ , vol. 2016, Mar. 2016, Art. no. 6547209, doi: 10.1155/2016/6547209. 

- [9] Y. Liu et al., “Understanding the spatiotemporal links between meteorological and hydrological droughts from a three-dimensional perspective,” _J. Geophys. Res. Atmos._ , vol. 124, no. 6, pp. 3090–3109, Feb. 2019, doi: 10.1029/2018JD028947. 

- [10] E. Peters, H. A. J. van Lanen, P. J. J. F. Torfs, and G. Bier, “Drought in groundwater-drought distribution and performance indicators,” _J. Hydrol._ , vol. 306, no. 1–4, pp. 302–317, May 2005, doi: 10.1016/j.jhydrol.2004.09.014. 

- [11] S. Shahid and M. K. Hazarika, “Groundwater drought in the northwestern districts of Bangladesh,” _Water Resour. Manage._ , vol. 24, pp. 1989–2006, Nov. 2009, doi: 10.1007/s11269-009-9534-y. 

- [12] J. P. Bloomfield and B. P. Marchant, “Analysis of groundwater drought building on the standardised precipitation index approach,” _Hydrol. Earth Syst. Sci._ , vol. 17, pp. 4769–4787, Dec. 2013, doi: 10.5194/hess-17-4769-2013. 

- [13] A. AghaKouchak et al., “Remote sensing of drought: Progress, challenges and opportunities,” _Rev. Geophys._ , vol. 53, no. 2, pp. 452–480, Jun. 2015, doi: 10.1002/2014RG000456. 

- [14] H. West, N. Quinn, and M. Horswell, “Remote sensing of drought monitoring & impact assessment: Progress, past challenges and future opportunities,” _Remote Sens. Environ._ , vol. 232, Jul. 2019, Art. no. 111291, doi: 10.1016/j.rse.2019.111291. 

6060 

IEEE JOURNAL OF SELECTED TOPICS IN APPLIED EARTH OBSERVATIONS AND REMOTE SENSING, VOL. 16, 2023 

- [15] A. K. Sahoo, J. Sheffield, M. Pam, and E. F. Wood, “Evaluation of the tropical rainfall measuring mission multi-satellite precipitation analysis (TMPA) for assessment of large scale meteorological drought,” _Remote Sens. Environ._ , vol. 159, pp. 181–193, Jan. 2015, doi: 10.1016/j.rse.2014.11.032. 

- [16] L. Yu, G. Leng, and A. Python, “A comprehensive validation for GPM IMERG precipitation products to detect extremes and drought over mainland China,” _Weather Climate Extremes_ , vol. 36, Jun. 2022, Art. no. 100458, doi: 10.1016/j.wace.2022.100458. 

- [17] M. R. Alizadeh and M. R. Nikoo, “A fusion-based methodology for meteorological drought estimation using remote sensing data,” _Remote Sens. Environ._ , vol. 211, pp. 229–247, Jun. 2018, doi: 10.1016/j.rse.2018.04.001. 

- [18] X. Bai, P. Wang, H. Wang, and Y. Xie, “An up-scaled vegetation temperature condition index retrieved from Landsat data with trend surface analysis,” _IEEE J. Sel. Topics Appl. Earth Observ. Remote Sens._ , vol. 10, no. 8, pp. 3537–3546, Aug. 2017, doi: 10.1109/JSTARS.2017.2698444. 

- [19] I. E. Mladenova, J. D. Bolten, W. Crow, N. Sazib, and C. Reynolds, “Agricultural drought monitoring via the assimilation of SMAP soil moisture retrievals into a global soil water balance model,” _Front. Big Data_ , vol. 3, no. 10, pp. 1–16, Apr. 2020, doi: 10.3389/fdata.2020.00010. 

- [20] C. F. Chen, N. T. Son, C. R. Chen, S. H. Chiang, L. Y. Chang, and M. Valdez, “Drought monitoring in cultivated areas of Central America using multi-temporal MODIS data,” _Geomatics, Natural Hazards Risk_ , vol. 8, no. 2, pp. 402–417, Aug. 2016, doi: 10.1080/19475705.2016.1222313. 

- [21] M. Zhao, A. Geruo, I. Velicogna, and J. S. Kimball, “Satellite observations of regional drought severity in the continental United States using GRACE-based terrestrial water storage changes,” _J. Climate_ , vol. 30, no. 16, pp. 6297–6308, Aug. 2017, doi: 10.1175/JCLI-D-16-0458.1. 

- [22] B. F. Thomas et al., “GRACE groundwater drought index: Evaluation of California central valley groundwater drought,” _Remote Sens. Environ._ , vol. 198, pp. 384–392, Sep. 2017, doi: 10.1016/j.rse.2017.06.026. 

- [23] J. Y. Seo and S.-I. Lee, “Spatio-temporal groundwater drought monitoring using multi-satellite data based on an artificial neural network,” _Water_ , vol. 11, no. 9, Sep. 2019, Art. no. 1953, doi: 10.3390/w11091953. 

- [24] B. D. Vishwakarma, J. Zhang, and N. Sneeuw, “Downscaling GRACE totalwater storagechange using partial least squaresregression,” _Sci.Data_ , vol. 8, no. 95, pp. 1–13, Mar. 2021, doi: 10.1038/s41597-021-00862-6. 

- [25] J. Y. Seo and S.-I. Lee, “Spatio-temporal groundwater drought monitoring using multi-satellite data based on an artificial neural network,” _Water_ , vol. 11, Sep. 2019, Art. no. 1953, doi: 10.3390/w11091953. 

- [26] J. Y. Seo and S.-I. Lee, “Predicting changes in spatiotemporal groundwater storage through the integration of multi-satellite data and deep learning models,” _IEEE Access_ , vol. 9, pp. 157571–157583, 2021, doi: 10.1109/ACCESS.2021.3130306. 

- [27] A. Arshad, A. Mirchi, M. Samimi, and B. Ahmad, “Combining downscaled-GRACE data with SWAT to improve the estimation of groundwater storage and depletion variations in the Irrigated Indus Basin (IIB),” _Sci. Total Environ._ , vol. 838, no. 2, Sep. 2022, Art. no. 156044, doi: 10.1016/j.scitotenv.2022.156044. 

- [28] V. Agarwal et al., “Machine learning based downscaling of GRACE-estimated groundwater in central valley, California,” _Sci. Total Environ._ , vol. 20, no. 865, Mar. 2023, Art. no. 161138, doi: 10.1016/j.scitotenv.2022.161138. 

- [29] A. F. Van Loon and H. A. J. Van Lanen, “A process-based typology of hydrological drought,” _Hydrol. Earth Syst. Sci._ , vol. 16, pp. 1915–1946, Jul. 2012, doi: 10.5194/hess-16-1915-2012. 

- [30] L. J. Barker, J. Hannaford, A. Chiverton, and C. Svensson, “From meteorological to hydrological drought using standardised indicators,” _Hydrol. Earth Syst. Sci._ , vol. 20, no. 6, pp. 2483–2505, Jun. 2016, doi: 10.5194/hess-20-2483-2016. 

- [31] S. Huang, P. Li, Q. Huang, G. Leng, B. Hou, and L. Ma, “The propagation from meteorological to hydrological drought and its potential influence factors,” _J. Hydrol._ , vol. 547, pp. 184–195, Apr. 2017, doi 10.1016/j.jhydrol.2017.01.041. 

- [32] K. Bhardwaj, D. Shah, S. Aadhar, and V. Mishra, “Propagation of meteorological to hydrological droughts in India,” _J. Geophys. Res. Atmos._ , vol. 125, Oct. 2020, Art. no. e2020JD033455, doi: 10.1029/2020JD033455. 

- [33] Z. Li et al., “Clarifying the propagation dynamics from meteorological to hydrological drought induced by climate change and direct human activities,” _J. Hydrometeorol._ , vol. 22, no. 9, pp. 2359–2378, Sep. 2021, doi: 10.1175/JHM-D-21-0033.1. 

- [34] W. Fang et al., “Probabilistic assessment of remote sensing-based terrestrial vegetation vulnerability to drought stress of the Loess Plateau in China,” _Remote Sens. Environ._ , vol. 232, Oct. 2019, Art. no. 111290, doi: 10.1016/j.rse.2019.111290. 

- [35] J. Y. Shin, H.-H. Kwon, J.-H. Lee, and T.-W. Kim, “Probabilistic long-term hydrological drought forecast using Bayesian networks and drought propagation,” _Meteorological Appl._ , vol. 27, no. 1, Jan. 2020, Art. no. e1827, doi: 10.1002/met.1827. 

- [36] J. Wang, W. Wang, H. Cheng, H. Wang, and Y. Zhu, “Propagation from meteorological to hydrological drought and its influencing factors in the Huaihe River Basin,” _Water_ , vol. 13, Jul. 2021, Art. no. 1985, doi: 10.3390/w13141985. 

- [37] Y. J. Bae, H. J. Lee, B. W. Jung, and H.-C. Jung, “Korean climate change assessment report 2020-Climate impact and adaptation,” Minister of Environment, Republic of Korea, 11-1480000-001692-01, Jul. 2020. 

- [38] USGS Earth Explorer. Accessed: Feb. 3, 2023. [Online]. Available: https: //earthexplorer.usgs.gov 

- [39] H. Save, S. Bettadpur, and B. D. Tapley, “High resolution CSR GRACE RL05 mascons,” _J. Geophys. Res. Solid Earth_ , vol. 121, no. 10, pp. 7547–7569, Sep. 2016, doi: 10.1002/2016JB013007. 

- [40] H. Save. CSR GRACE and GRACE-FO RL06 Mascon Solutions v02. Accessed: Feb. 3, 2023. [Online]. Available: 10.15781/cgq9-nh24 

- [41] A. I. Johnson, Specific yield-compilation of specific yields for various materials, U.S. Government Printing Office, 1662-D, 1967, doi: 10.3133/wsp1662D. 

- [42] S. P. Loheide II, J. J. Butler Jr, and S. M. Gorelick, “Estimation of groundwaterconsumptionbyphreatophytesusingdiurnalwatertablefluctuations: A saturated-unsaturated flow assessment,” _Water Resour. Res._ , vol. 41, no. 7, Jul. 2005, Art. no. W07030, doi: 10.1029/2005WR003942. 

- [43] T. B. McKee, J. Nolan, and J. Kleist, “The relationship of drought frequency and duration to time scales,” in _Proc. 8th Conf. Appl. Climatol._ , 1993, pp. 179–183. 

- [44] M. H. Afshar, B. Bult, E. Duzenli, M. Amjad, and M. T. Yilmaz, “Global spatiotemporal consistency between meteorological and soil moisture drought indices,” _Agricultural Forest Meteorol._ , vol. 316, Apr. 2022, Art. no. 108848, doi: 10.1016/j.agrformet.2022.108848. 

- [45] J. Martínez-Fernández, A. González-Zamora, N. Sánchez, A. Gumuzzio, and C. M. Herrero-Jiménez, “Satellite soil moisture for agricultural drought monitoring: Assessment of the SMOS derived soil water deficit index,” _Remote Sens. Environ._ , vol. 177, pp. 277–286, May 2016, doi: 10.1016/j.rse.2016.02.064. 

- [46] B. W. Silverman, “Density estimation for statistics and data analysis,” in _Monographs On Statistical and Applied Probability_ , D. R. Cox, D. V. Hinkley, N. Keiding, N. Reid, D. B. Rubin, and B. W. Silverman, Eds., London, U.K.: Chapman & Hall, 1986, pp. 1–186. 

- [47] M. Sklar, “Fonctions de répartition à n dimensions et leurs marges,” _Pub. de l’Institut Statistique de l’Université de Paris_ , vol. 8, pp. 229–231, 1959. 

- [48] H. Joe, “Multivariate models and dependence concept,” in _Monographs On Statistical and Applied Probability_ , D. R. Cox, V. Isham, N. Keiding, N. Reid, and H. Tong, Eds., London, U.K.: Chapman & Hall, 1997, pp. 1–424. 

- [49] R. B. Nelsen, _An Introduction to Copulas_ . New York, NY, USA: Springer. 

- [50] M. Dehghani, B. Saghafian, and M. Zargar, “Probabilistic hydrological drought index forecasting based on meteorological drought index using Archimedean copulas,” _Hydrol. Res._ , vol. 50, no. 5, pp. 1230–12250, Oct. 2019, doi: 10.2166/nh.2019.051. 

- [51] S. Zhu et al., “Multidimensional response evaluation of remote-sensing vegetation change to drought stress in the three-river headwaters, China,” _IEEE J. Sel. Topics Appl. Earth Observ. Remote Sens._ , vol. 13, pp. 6249–6259, 2020, doi: 10.1109/JSTARS.2020.3027347. 

- [52] M. Jehanzaib, J. Yoo, H.-H. Kwon, and T.-W. Kim, “Reassessing the frequency and severity of meteorological drought considering nonstationarity and copula-based bivariate probability,” _J. Hydrol._ , vol. 603, no. part B, 2021, Art. no. 126948, doi: 10.1016/j.jhydrol.2021.126948. 

- [53] M. Jehanzaib, M. N. Sattar, J.-H. Lee, and T.-W. Kim, “Investigating effect of climate change on drought propagation from meteorological to hydrological drought using multi-model ensemble projections,” _Stochastic Environ. Res. Risk Assessment_ , vol. 34, pp. 7–21, 2020, doi: 10.1007/s00477-019-01760-5. 

- [54] M. Jehanzaib, M. B. Idrees, D. Kim, and T.-W. Kim, “Comprehensive evaluation of machine learning techniques for hydrological drought forecasting,” _J. Irrigation Drainage Eng._ , vol. 147, no. 7, 2021, Art. no. 04021022, doi: 10.1061/(ASCE)IR.1943-4774.0001575. 

- [55] Y. Zhang et al., “Generation of global 1-km daily soil moisture product from 2000 to 2020 using ensemble learning,” _Earth Syst. Sci. Data_ , vol. 15, no. 5, pp. 2055–2079, 2023, doi: 10.5194/essd-2022-348. 

- [56] P. Yu et al., “Global spatiotemporally continuous MODIS land surface temperature dataset,” _Sci. Data_ , vol. 9, no. 143, pp. 1–15, 2022, doi: 10.1038/s41597-022-01214-8. 

6061 

SEO AND LEE: PROBABILISTIC EVALUATION OF DROUGHT PROPAGATION USING SATELLITE DATA AND DEEP LEARNING MODEL 



**Jae Young Seo** received the B.S. and Ph.D. degrees in civil and environmental engineering from Dongguk University, Seoul, South Korea, in 2013 and 2019, respectively. 

She is currently a Postdoctoral Research Associate and Lecturer with Dongguk University. Her research interests include hydrological monitoring and prediction based on satellite remote sensing, GIS, and machine learning/deep learning. 

**Sang-II Lee** received the B.S. and M.S. degrees in mechanical engineering from Seoul National University, Seoul, South Korea, in 1982 and 1984, respectively, and the Ph.D. degree in civil and environmental engineering from Stanford University, Stanford, CA, USA, in 1991. 

Since 1995, he has been a Professor of Civil and Environmental Engineering, Dongguk University, Seoul, South Korea. Since 2014, he has been the Director of Center for Ecology and Environment. His primary areas of research include hydroenvironmental assessment using remote sensing techniques, groundwater hydrology, and conjunctive use of surface and subsurface water. 

Dr. Lee served as a Guest Editor for _Remote Sensing_ (ISSN: 2072-4292) for a special issue on Using Satellite Images for Drought Monitoring. 

