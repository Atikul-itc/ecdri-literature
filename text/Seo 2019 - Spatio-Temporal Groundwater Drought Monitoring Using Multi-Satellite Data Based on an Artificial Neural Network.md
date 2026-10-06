**_water_** 





# _Article_ **Spatio-Temporal Groundwater Drought Monitoring Using Multi-Satellite Data Based on an Artificial Neural Network** 

**Jae Young Seo and Sang-Il Lee *** 

Department of Civil and Environmental Engineering, Dongguk University, Seoul 04620, Korea; dabbi2011@naver.com 

***** Correspondence: islee@dongguk.edu; Tel.: +82-2260-3353 

��������� Received: 31 July 2019; Accepted: 17 September 2019; Published: 19 September 2019 **�������** 

**Abstract:** Drought is a complex phenomenon caused by lack of precipitation that affects water resources and human society. Groundwater drought is difficult to assess due to its complexity and the lack of spatio-temporal groundwater observations. In this study, we present an approach to evaluate groundwater drought based on relatively high spatial resolution groundwater storage change data. We developed an artificial neural network (ANN) that employed satellite data (Gravity Recovery and Climate Experiment (GRACE) and Tropical Rainfall Measuring Mission (TRMM)) as well as Global Land Data Assimilation System (GLDAS) models. The Standardized Groundwater Level Index (SGI) was calculated by normalizing ANN-predicted groundwater storage changes from 2003 to 2015 across South Korea. The ANN-predicted 25 km groundwater storage changes correlated well with both the in situ and the water balance equation (WBE)-estimated groundwater storage changes, with mean correlation coefficients of 0.87 and 0.64, respectively. The Standardized Precipitation–Evapotranspiration Index (SPEI), having an accumulation time of 1–6 months, and the Palmer Drought Severity Index (PDSI) were used to validate the SGI. The results showed that the SGI had a pattern similar to that of SPEI-1 and SPEI-2 (1- and 2-month accumulation periods, respectively), and PDSI. However, the SGI performance fluctuated slightly due to its relatively short study period (13 years) as compared to SPEI and PDSI (more than 30 years). The SGI, which was developed using a new approach in this study, captured the characteristics of groundwater drought, thus presenting a framework for the assessment of these characteristics. 

**Keywords:** groundwater drought; groundwater storage changes; ANN; GRACE; TRMM; GLDAS; SGI 

## **1. Introduction** 

Accelerated global warming, resulting in drought and floods, has significant impacts on the hydrological environment on a global scale. The Korean Peninsula has recently experienced an increase in annual precipitation; however, the number of days of precipitation has decreased, and there has been a serious local drought phenomenon. Moreover, droughts continue to occur and have caused environmental and socio-economic losses. In recent years (2014–2015), the Central and Kangwon Provinces have suffered severe droughts that have affected not only surface water (e.g., reservoirs, lakes), but also groundwater. The groundwater level in Jeju Island was found to be much lower than normal due to drought during these years. Damage caused due to groundwater drought is not restricted to domestic water, but also includes agriculture and industry. Therefore, research related to the understanding and prediction of groundwater drought is increasingly important. 

A new drought indicator, the Standardized Groundwater Level Index (SGI), was developed by Bloomfield et al. [1]. With respect to understanding groundwater drought, this index is similar 

_Water_ **2019** , _11_ , 1953; doi:10.3390/w11091953 

www.mdpi.com/journal/water 

2 of 19 

_Water_ **2019** , _11_ , 1953 

to the traditional drought index, the Standardized Precipitation Index (SPI). Unlike precipitation, groundwater fluctuation is a continuous variable for which data do not need to be accumulated for a certain time period, and for which normalization using a gamma distribution like the SPI calculation is not necessary. Therefore, it is possible to quantitatively evaluate the fluctuation in groundwater during a drought period by appropriately normalizing the groundwater time series data measured by ground observation. 

Recently, there have been efforts to use the new groundwater drought index, SGI [2–4], for groundwater drought analysis in South Korea. Also, the National Drought Information-Analysis Center in Korea has provided a monthly SGI map from 2009 [5]. Groundwater storage changes data are generally obtained through in situ measurements and can be acquired from the National Groundwater Monitoring Network (NGMN) in South Korea. However, it is difficult to represent the spatial distribution of groundwater storage changes using point-based in situ measurements [6]. Previous studies used the only in situ groundwater data for SGI calculation; therefore, alternative approaches for such problems are needed. 

With the launch of the Gravity Recovery and Climate Experiment (GRACE) satellites, remote sensing approaches have been established as a powerful tool to observe spatio-temporal groundwater storage changes [7]. Previous studies have evaluated groundwater storage changes in many areas using GRACE satellites based on the water balance method [8–10]. Seo and Lee [11] estimated and evaluated groundwater storage changes across South Korea using GRACE satellites, based on the water balance method. Thomas et al. [6] also determined groundwater drought indicators for California Valley using GRACE-based water balance approaches, and Houborg et al. [12] determined groundwater drought indicators via hydrologic model simulations in the U.S. 

However, monitoring groundwater drought at a local or regional scale using GRACE data with a coarse spatial resolution (∼100 km) is difficult [13–16]. In addition, the hydrological variables available in those studies were insufficient to apply the water balance method. Global GRACE-based calculation of groundwater drought indices could provide useful information for droughts, but more high-resolution groundwater data are required to identify spatially detailed drought conditions. Recently, many machine learning approaches have been developed to overcome these difficulties [15–18]. The artificial neural network (ANN) is one such machine learning technique used extensively in the prediction of groundwater level changes/terrestrial water storage changes based on GRACE satellites data [15,16]. ANN models can explore empirical relationships between input and output variables through iterative training with input variables. Moreover, they are widely used for statistical downscaling of satellite data. 

The objective of this study is to estimate SGI using ANN-predicted groundwater storage changes through satellite data and Global Land Data Assimilation System (GLDAS) land surface models data for monitoring groundwater droughts in South Korea. The specific objectives of this study are to: (1) predict groundwater storage changes based on GRACE terrestrial water storage changes data, Tropical Rainfall Measuring Mission (TRMM) precipitation data, and GLDAS average temperature and soil moisture changes data using ANN models; (2) validate the ANN-predicted values using in situ data; (3) estimate SGI by normalizing groundwater storage changes for a given period; and (4) evaluate SGI through comparison with a multi-time-scale Standardized Precipitation–Evapotranspiration Index (SPEI), one of the meteorological drought index, and Palmer Drought Severity Index (PDSI), one of the hydrological drought indices. 

## **2. Study Area and Data** 

## _2.1. Study Area_ 

South Korea is located in East Asia (32.5<sup>◦</sup> N–40.0<sup>◦</sup> N and 124.5<sup>◦</sup> E–130.0<sup>◦</sup> E), and approximately 70% of its area is mountainous terrain (Figure 1a). The mean annual precipitation in the study area is 1307.7 mm (most of the annual precipitation occurs in summer and monsoon seasons), and the mean annual temperature is about 12.5<sup>◦</sup> C. South Korea is comprised of eight hydrogeologic 

3 of 19 

_Water_ **2019** , _11_ , 1953 

units (unconsolidated sediments, porous volcanic rock, semi-consolidated clastic sedimentary rock, non-porous volcanic rock, intrusive igneous rock, clastic sedimentary rock, limestone, and metamorphic rock), depending upon the geological period and the type of rocks (Figure 1b; [19]). The annual groundwater recharge in South Korea is 18.2 billion m<sup>3</sup> , with approximately 14% contributed by annual precipitation [19]. Groundwater usage accounts for 11% of the total annual water consumption with maximum usage during the dry season [20]. 



**Figure 1.** Locations of study area; ( **a** ) administrative district map; ( **b** ) digital elevation model (DEM); ( **c** ) geological map; ( **d** ) national groundwater monitoring network. 

## _2.2. Data Used_ 

## 2.2.1. GRACE Satellite 

Gridded GRACE products (Level-2) that were post-processed using spherical harmonic solutions were utilized to derive the Terrestrial Water Storage Anomaly (TWSA) for the study area. The GRACE gridded TWSA products (1<sup>◦</sup> × 1<sup>◦</sup> ) from spherical harmonics were provided by the Center for Space Research (CSR) at the University of Texas, the Jet Propulsion Laboratory (JPL), and the German Research Center for Geoscience (GFZ). In this study, we used the latest CSR data (Release number 5, RL05; [21]) from January 2003 to December 2015 (Table 1). CSR RL05 data were truncated at the maximum degree and order of 60 to reduce the error from spherical harmonic coefficients [22,23]. Also, the high-frequency noise of the GRACE spherical harmonic products was reduced by using a 300 km Gaussian filter for smoothing. Signal amplitudes were restored by gain factors computed by the Community Land Model (CLM) version 4 TWSA time series output, and the GRACE RL05 TWSA products were processed by multiplication with factors. The computed TWSA products were then 

4 of 19 

_Water_ **2019** , _11_ , 1953 

converted into Terrestrial Water Storage Changes (TWSC) for the _i_ th month by calculating TWSAs with respect to time (Equations (1) and (2)). 





**Table 1.** Information of data used in this study. 

|**Product**|**Dataset**|**Source**|**Resolu**<br>**Spatial**|**tion**<br>**Temporal**|**Reference**|
|---|---|---|---|---|---|
|GRACE RL05|TWSC|Satellite|1.0<sup>◦</sup>×1.0<sup>◦</sup>|Monthly|http://grace.jpl.nasa.gov/|
|TMPA3B43|Precipitation (P)|Satellite|0.25<sup>◦</sup>×0.25<sup>◦</sup>|Monthly|http://mirador.gsfc.nasa.gov/|
|GLDAS_ NOAH025_M|Soil moisture (∆SMS)<br>Average temperature (T)|Reanalysis|0.25<sup>◦</sup>×0.25<sup>◦</sup>|Monthly|http://ldas.gsfc.nasa.gov/|
|NGMN|Groundwater level|Gauges|-|Monthly|http://gims.go.kr/|



## 2.2.2. TRMM Satellite 

The TRMM is a joint mission between National Aeronautics and Space Administration (NASA) and the Japan Aerospace Exploration Agency (JAXA) to monitor the spatio-temporal precipitation variations in tropical regions. NASA’s Goddard Earth Sciences Data and Information Services Center (GES DISC) developed the TRMM Multi-satellite Precipitation Analysis (TMPA) products. Particularly, the TMPA3B42 and TMPA3B43 products provide precipitation data by merging multi-satellite (SSMI, SSMIS, MHS, AMSU-B, and AMSR E) precipitation data and global observed precipitation data (Global Precipitation Climatology Project; GPCP; [24]). TMPA3B42 and 3B43 precipitation data for the Korean Peninsula has been validated in previous studies [25,26]. We applied TMPA3B43 (ver. 7) monthly precipitation data, at 0.25<sup>◦</sup> spatial resolution (Table 1). 

## 2.2.3. GLDAS Model Data 

GLDAS has been developed by integrating satellite- and ground-based measurements using four land surface models: Common Land Model (CLM), Mosaic, Noah, and Variable Infiltration Capacity (VIC). GLDAS provides three-hourly and monthly datasets with 0.25<sup>◦</sup> and 1.0<sup>◦</sup> spatial resolutions, using data assimilation techniques. In this study, we used the version 1 GLDAS 0.25-degree products (GLDAS_NOAH025_M; Table 1) to obtain soil moisture changes (∆SMS) and average temperature (T). The data were obtained from the GES DISC. GLDAS_NOAH025_M has four layers of soil moisture by depth (layer 1: 0–0.1 m; layer 2: 0.1–0.4 m; layer 3: 0.4–1.0 m, and layer 4: 1.0–2.0 m), and we used the integrated soil moisture data for these four layers [27]. 

## 2.2.4. Well Data (National Groundwater Monitoring Network) 

Since 1995, NGMN has been operated in South Korea by the Ministry of Land, Infrastructure, and Transport (MOLIT) and Korea Water Resources Corporation [28], which obtains groundwater data, monitors groundwater fluctuations, and manages basic hydrogeological data. A total of 386 stations had been installed as of 2015. Among the 386 stations, 166 stations have two monitoring wells, one for shallow groundwater in alluvial aquifers and the other for deep groundwater in bedrock aquifers [28], whereas the other stations have only the latter. In this study, groundwater level data from 200 stations were used considering the continuity of data and the study period (2003–2015; Figure 1c; Table 1). Groundwater level data were converted to groundwater storage changes (∆GWS) in terms of equivalent water height by multiplying groundwater level changes (∆ _W_ ) and the specific yield ( _Ys_ ). This relationship is shown in Equation (3). 

5 of 19 

_Water_ **2019** , _11_ , 1953 

∆GWS = ∆ _W_ × _Y_ s (3) 

The geological characteristics of groundwater in alluvial aquifers in South Korea studied by the US Geological Survey (USGS) and Korea Rural Community (KRC) are composed of porous aquifers such as clay, silt, sand, gravel, and boulders (Figure 1b). The USGS and KRC reported average specific yields of 0.202 and 0.143, respectively [29]. Previous case studies regarding South Korea have found that the specific yield ranges from 0.02 to 0.42 in alluvial aquifers of Donghae City [30]; from 0.06 to 0.27 in 34 alluvial aquifers in South Korea [31], and from 0.009 to 0.031 in Jeju Island [32]. In this study, we used a specific yield of 0.20, which is the mean of the values of specific yields over various locations. 

## **3. Methodology** 

SGI, which is calculated based on the method proposed by Bloomfield and Marchant [1], is a new index for the standardization of groundwater time series data and characterization of groundwater drought. We calculated SGI using the space-borne data presented in Section 2. A flow chart for calculating SGI in this study is shown in Figure 2. The process consists of two parts: (1) predicting downscaled groundwater storage changes using GRACE satellites data and determining 25 km satellite-based hydrological variables through the ANN approach, and (2) developing SGI by standardizing the predicted groundwater storage changes. 



**Figure 2.** Process flow of the research. 

## _3.1. Water Balance Equation-Estimated Groundwater Storage Changes_ 

The water balance equation (WBE) can be used to describe the flow of water in and out of system. A system can be one of several hydrological domains, such as a column of areas or a drainage basin. Determination of WBE is difficult, and calculating closing water balance is complicated due to uncertainties of measurements of water balance components [33]. 

GRACE satellites provide an unprecedented opportunity to capture the variability of TWSC. Generally, the GRACE-based TWSC data comprises vertically integrated water storages of all columns 

6 of 19 

_Water_ **2019** , _11_ , 1953 

of a region, which represents the sum of soil moisture, groundwater, surface water, snow, and ice (Equation (4); [7–11,34–36]). Vegetation effects (canopy, wetland, etc.) are ignored, because these effects are small compared to other water storage changes. Groundwater storage changes are often disaggregate from GRACE from TWSC by subtracting changes of snow water, reservoir storage, and soil moisture (Equation (5)). Seo and Lee [11] estimated groundwater storage variations in South Korea based on TWSC observed by GRACE time-varying gravity data, soil moisture and snow water equivalent from the GLDAS land surface models data, and surface water from the reservoir data. They combined these in a WBE for estimating groundwater storage changes (∆GWS, Equation (5)). 





where, GWS is groundwater storage, TWSC is terrestrial water storage changes, RESS is surface water (reservoir water storage; Figure 1b), SMS is soil moisture storage, and SWE is snow water equivalent [7]. However, GRACE TWSC data has relatively large spatial resolution and inherent uncertainty, and TWSC in WBE causes larger noise [11]. Also, TWSC, ∆SMS, and ∆RESS have similar uncertainties compared to ∆SWE from uncertainty analysis [11]. The WBE-estimated ∆GWS results extended from Seo and Lee [11] are used to compare the ∆GWS results of this study. 

## _3.2. Prediction of Downscaled Groundwater Storage Changes_ 

The most common and standard learning algorithm for ANN models is the back-propagation algorithm. The backpropagation algorithm includes two steps: feedforward and weight update. In the feedforward step, vectors of the hidden layer are computed as an activation function using the dot product value of the input vectors and each connection weight. The computational process is shown in Equation (6), and the output value is computed through the hidden layer when input data is entered for each node on the input layer. 



where, _xi_ is the _i_ th node value of the previous layer, _y j_ is the _j_ th node value of the current layer, _b j_ is the bias of the _j_ th node of the current layer, _wji_ is the connection weight of _xi_ and _yj_ , and _m_ is the number of nodes of the previous layer, _f_ is the transfer function of the hidden layer and the output layer. In this study, we use the transfer function as the log-sigmoid function which is the most frequently used. 

In the weight update step, the error ( _E_ ) is the difference between the predicted value ( _yk_ ) and target value ( _tk_ ) calculated in the feedforward step. The error is used to calculate each of the connection weights on the vectors of neurons in the preceding layer. The mean squared error (MSE) method is used for error estimation (Equation (7)). 



Figure 2 (Prediction of downscaled ∆GWS part) shows the process flow of this research. ANN machine learning approaches were used to predict 25 km groundwater storage changes data. In order to develop a prediction model, GRACE products with 1.0<sup>◦</sup> spatial resolution were replaced with four 0.25<sup>◦</sup> pixels with the same value. Then, three variables, precipitation (P) of TRMM, average temperature (T), and soil moisture (SMS) of GLDAS, were extracted for each pixel. A total of 24,180 samples (155 pixels × 156 months), were gathered for South Korea, which were used to develop the ANN models. We developed multilayer perceptron (MLP) ANN models such that they learn functional mapping and predict monthly ∆GWS. The models consisted of one input layer, one hidden layer, and one output layer. Inputs to the MLP models consisted of monthly P, T, ∆SMS, and TWSC. 

7 of 19 

_Water_ **2019** , _11_ , 1953 

The target data were the in situ point data resampled to the 25 km grid simply with inverse distance weighting (IDW) interpolation in the ArcGIS tool, commonly used for the resampling of gridded data. Groundwater point data do not give appropriate representative 25 km resolution, because the densities of the measurement networks are sparse. Therefore, we tried to do grid-to-grid training. 

In this study, the Levenberg–Marquardt algorithm [37], which is commonly used for training, was applied to the back-propagation algorithm in the ANN model. The number of epochs for the training was set at 1000, and the variables of the input layer were entered before proceeding with the training. We defined an early stop criterion; the training is stopped if the error gradient reaches a minimum, or when the error goal in the training set is met. Also, early stopping of the training the ANN model was enforced before overfitting is occurred, such that the training dataset can reduce overfitting and improve the generalization of neural networks [38]. In addition, the number of nodes in the hidden layer was calculated by changing from one to ten nodes. The lead time (time delay) of the input layer variables for the prediction were varied from 1 to 3 months. Figure 3a shows the structure of the ANN model used in this study, where _m_ refers to the time series leading time based on time _t_ , and Ψ refers to the log-sigma function. Figure 3b shows the procedure of ∆GWS prediction using the ANN and is divided into sections of input data construction, learning process, trial error, verification process, and prediction process. The time series was divided into training, validation, and test periods, set to be 60% (Training; January 2003–October 2010), 20% (Validation; November 2010–May 2013), and 20% (Test; June 2013–December 2015) of the total period (January 2003–December 2015), respectively. 

8 of 19 

_Water_ **2019** , _11_ , 1953 



**Figure 3.** ( **a** ) Structure of the artificial neural network (ANN) model used for groundwater storage changes (∆GWS) predictions; ( **b** ) ANN model flow. 

## _3.3. Standardized Groundwater Drought Index (SGI)_ 

The SGI was developed using the predicted 25 km groundwater storage changes data derived from the satellites data through the ANN machine learning approach. SGI was calculated through normalization using the predicted groundwater storage values at each pixel during the test period (2014–2015) using Equation (8). Normalized SGI can express the status of observed groundwater storage values [1]. The SGI identifies areas that are drier (represented below 0) or wetter (represented by 1) than their usual condition. For groundwater drought, the USGS arbitrarily defined drought intensity according to SGI using percentile of groundwater level [2]. At the National Drought Mitigation Centre (NDMC), a monthly groundwater level of 25% or more is classified as normal conditions, 11–25% is classified as moderately dry, 6–10% is consider to be severely dry, and 5% is extremely dry. In this study, we suggested the criteria for the SGI using percentile of groundwater storage changes, such that SGI ≤−1.5 corresponded to exceptional drought, −1.5 < SGI ≤−1.2 was denoted as extreme drought, −1.2 < SGI ≤−0.9 corresponded to severe drought, −0.9 < SGI ≤−0.6 was moderate 

9 of 19 

_Water_ **2019** , _11_ , 1953 

drought, −0.6 < SGI ≤−0.3 was seen as abnormally dry conditions, and SGI > −0.3 as corresponded to normal/no drought. 



This study aimed to develop and validate SGI, using meteorological and hydrological reference data based on space borne data. The relationships and the time series patterns between SGI and the multi-timescale SPEI were analyzed for meteorological drought. 

## **4. Results and Discussion** 

## _4.1. ANN-Predicted Groundwater Storage Changes_ 

Based on the input variables, 1000 epochs and 100 iterations of the back-propagation algorithm were trained by varying the number of nodes in the hidden layer; the results provided the most accurate predictions when the lead time was two months and when there were four nodes in the hidden layer. Figure 4 shows the monthly time series of 25 km ANN-predicted ∆GWS, in situ ∆GWS, and WBE-estimated ∆GWS corresponding to precipitation at 56 stations during the study period. The two vertical dotted lines mark the division of the training, validation, and test periods. Both the 25 km predicted ∆GWS and the WBE-estimated ∆GWS show a similar temporal pattern to that of in situ ∆GWS. Groundwater storage changes with changing precipitation are generally low in the dry season and high in the wet season. However, WBE-estimated ∆GWS tends to be overestimated when compared to in situ ∆GWS, as discussed by Seo and Lee [11]. It might have uncertainties for the following reasons: (1) model error due to water balance components in the equation; (2) measurement uncertainties of three different product (GRACE satellite, GLDAS models, and ground measurements); (3) low spatial resolution and inherent uncertainties of GRACE; and (4) errors made in the process of integrating each product. It should also be noted that the spatial scales are quite different for the three types of ∆GWS data: in situ ∆GWS was measured at point locations, while the ANN-predicted ∆GWS and WBE-estimated ∆GWS data were observed over 25 km × 25 km and 1<sup>◦</sup> × 1<sup>◦</sup> grids, respectively. Table 3 lists the values for the root mean square error (RMSE; Equation (9)), the correlation coefficient ( _r_ ; Equation (10)), and the index of agreement (IOA; Equation (11)) for these calculated data. This enables statistical comparison between predicted or estimated ∆GWS and in situ ∆GWS. 



where, _N_ is the number of data, _X_ is predicted/estimated ∆GWS, _X_ is mean of _X_ , _Y_ is in situ ∆GWS, and _Y_ is mean of _Y_ . 

10 of 19 

_Water_ **2019** , _11_ , 1953 



**Figure 4.** Time series of ∆GWS (ANN-predicted, in situ, and water balance equation (WBE)-estimated) with monthly precipitation. 

Comparison between the in situ and ANN-predicted ∆GWS data resulted in mean RMSE of 22.50 mm/month, mean _r_ of 0.87, and mean IOA of 0.93 in the total period (January 2003–December 2015) across South Korea (Table 2). The ANN-predicted ∆GWS produced in this study also showed relatively low RMSE and high _r_ and IOA compared to the WBE-estimated ∆GWS extended from Seo and Lee [11] (resulting in mean RMSE of 49.18 mm/month, mean _r_ of 0.64, and mean IOA of 0.77; Table 2). Particularly, test results (June 2013–December 2015) that have no effect on training and provide an independent measure of network performance during and after training indicated that the ANN-predicted ∆GWS produced using the proposed approach was closely related to the in situ ∆GWS. 

**Table 2.** Performance (root mean square error (RMSE), correlation coefficient; _r_ , and index of agreement (IOA)) of groundwater storage changes results compared to in situ data. 

|**Period**|**Statistic**|**ANN-Predicted ∆GWS**|**WBE-Estimated ∆GWS [11] ***|
|---|---|---|---|
|Training<br>(Januar 2003–October 2010)|RMSE (mm/month)<br>_r_(-)|20.55<br>0.91|49.95<br>0.64|
|y|IOA (-)|0.95|0.78|
|Validation|RMSE (mm/month)|22.39|53.40|
|(November 2010–Ma 2013)|_r_(-)|0.89|0.66|
|y|IOA (-)|0.94|0.77|
|Test|RMSE (mm/month)|27.59|41.93|
|(June 2013–December 2015)|_r_(-)|0.67|0.60|
||IOA (-)|0.81|0.71|
|Total|RMSE (mm/month)|22.50|49.18|
|(Januar 2003–December 2015)|_r_(-)|0.87|0.64|
|y|IOA (-)|0.93|0.77|



* Time period was extended to include 2013–2015 ∆GWS data. 

Figure 5 shows the spatial distribution of monthly ∆GWS for January and August in 2014 during the test period. Although the four spatial patterns generally have similar results, the WBE-estimated ∆GWS did not express information regarding the changes in groundwater storage in some areas due to its low spatial resolution. The ANN-predicted ∆GWS and in situ ∆GWS showed spatial patterns similar to those of the WBE-estimated ∆GWS. Visual comparison of the spatial and temporal variation patterns among the groundwater storage changes confirmed that the ANN-predicted ∆GWS showed good visual agreement overall with in situ ∆GWS. 

11 of 19 

_Water_ **2019** , _11_ , 1953 



**Figure 5.** Spatial distribution of monthly ∆GWS in January and August in 2014. 

We examined the correlations between the ANN-predicted ∆GWS and interpolated in situ ∆GWS. The spatial distributions of RMSE and correlation coefficients ( _r_ ) between the ANN-predicted ∆GWS and in situ ∆GWS over the test period (June 2013–December 2015) are presented in Figure 6. It should be noted that low RMSE (blue color in Figure 6a) and positive correlation (blue color in Figure 6b) appear in most areas. 



**Figure 6.** Spatial distribution of ( **a** ) RMSE and ( **b** ) correlation coefficient between ANN-predicted ∆GWS and interpolated in situ ∆GWS during the test period (June 2013-December 2015). 

Some coastal regions in the eastern and southern areas show higher RMSE (red color in Figure 6a) and lower _r_ (green color in Figure 6b) than other regions in those areas. Unlike other areas, the satellite information for coastal regions shows uncertainties due to tidal effects. Also, in situ data for these regions are sparse, possibly resulting in a higher error and lower correlation coefficients. This is due to data leakage in the network or overfitting to the training data. 

Sensitivity was analyzed for the validation of the ANN model. Sensitivity or the importance of input and output variables in nonlinear function models, such as ANN models, can be measured using connection weights. The conventional method used for measuring sensitivity can calculate the relative importance of input variables by dividing the connection weights between the hidden ( _wij_ ) and output 

12 of 19 

_Water_ **2019** , _11_ , 1953 

layers ( _wjk_ ) for each input variable [39]. The relative importance ( _Zi_ ) was calculated using Equations (12)–(14). 







Figure 7 shows the relative importance of the four input variables (terrestrial water storage changes (TWSC), precipitation (P), soil moisture changes (∆SMS), and average temperature (T)). The results based on South Korea show that P had the highest importance at 0.29, followed by T at 0.24, ∆SMS at 0.26, and TWSC at 0.21, indicating that their importance was similar (Figure 7a). Figure 7b shows the relative importance of four variables for each administrative district (Figure 1a). In most areas, the contribution of P and ∆SMS (0.261–0.277 and 0.259–0.282, respectively) are relatively greater than those of TWSC and T (0.219–0.239 and 0.208–0.245, respectively). Moreover, as precipitation and soil moisture are closely related to groundwater seasonality, they reflect groundwater storage changes. However, as these values are similar, these results show that all four input variables have a significant effect on ∆GWS predictions. 



**Figure 7.** Relative importance of input variables; ( **a** ) for entire country; ( **b** ) for representative administrative district. 

13 of 19 

_Water_ **2019** , _11_ , 1953 

## _4.2. Monitoring of Groundwater Drought_ 

Figure 8 presents the spatial distribution of the SGI results, calculated from Equation (8) using the ANN-predicted ∆GWS in the study area during 2015, where non-drought periods (SGI > −0.3), are shown in bluish colors, and drought periods (SGI ≤−0.3) are shown in shades ranging from yellow to red, with increasing drought intensity. 



**Figure 8.** Spatial distribution of SGI using multi-satellite data with ANN (2015). 

As seen in Figure 8, detailed groundwater drought data with a spatial resolution of 25 km can be identified. In particular, groundwater droughts during the dry seasons (January/October–December) of 2015 are clearly expressed by the SGI records for agricultural areas (south-western/-eastern). In addition, SGI showed drought patterns in most regions because of the low precipitation (see Figure 4) during the rainy season (July–August) that year compared to other years. Moreover, there was a severe drought in the entire area, particularly in the southern region, at the end of year. 

Lee et al. [2] estimated the SGI using the NGMN level data of 167 stations in South Korea, and then calculated the area weighted average of SGI using the Thiessen Polygon based on each groundwater station. In situ groundwater level-based SGI has a limited ability in providing representative values, because there are some areas where the densities of the networks are sparse. As for the SGI proposed in this study, we have the ability to better characterize groundwater drought. Multi-satellite data with ANN-based results can provide spatio-temporal groundwater information and can be a useful tool for spatio-temporal groundwater drought monitoring. 

## _4.3. Comparison with Meteorological Drought_ 

The SGI was validated using the SPEI with various accumulation periods (1-, 2-, 3-, and 6-months) one of the meteorological drought indices, and the PDSI one of the hydrological drought indices. In this work, we chose the monthly SPEI based on FAO-56 Penman–Monteith potential evapotranspiration data over global land areas with a spatial resolution of 0.5<sup>◦</sup> × 0.5<sup>◦</sup> ([40]; https://spei.csic.es/database.html) and PDSI over entire globe with a spatial resolution of 0.5<sup>◦</sup> × 0.5<sup>◦</sup> [41,42] for comparison with the 

14 of 19 

_Water_ **2019** , _11_ , 1953 

dimensionless SGI drought index. Figure 9 shows the time series of the calculated SGI, SPEI for the accumulation periods (1–6 months), and PDSI along with the monthly precipitation. Results showed that the temporal trends and patterns of the drought and no drought conditions were similar (i.e., decreasing from 2008 to 2009; see red box in Figure 9). The SPEI became smoother and less noisy as precipitation and evapotranspiration accumulation periods increased. Also, PDSI had smoother variation, and drought duration was longer compared to SPEI and SGI. However, the SGI generally shows greater variation than SPEI and PDSI because as the latter were calculated over a long time period (more than 30 years) by fitting the probability distribution of the data, while the SGI was simply standardized without considering the data distribution, over a relatively short period of time (2003–2015). 



**Figure 9.** Time series of Standardized Precipitation−Evapotranspiration Index (SPEI)-1, -2, -3, -6, Palmer Drought Severity Index (PDSI), Standardized Groundwater Level Index (SGI), and monthly precipitation. 

15 of 19 

_Water_ **2019** , _11_ , 1953 

Since groundwater drought propagation is driven by precipitation deficits and evapotranspiration associated with elevated temperatures, SGI and other indices results have lag time. To explore drought propagation, we evaluated cross-correlations between the SPEI, PDSI, and SGI to quantify the lag time for SPEI-1, -2, -3, and -6 month periods and PDSI, as shown in Figure 10. Here, the strongest cross-correlation is marked by a star. The 1- and 2-lag month cross-correlation between SPEI and SGI was relatively high. One the other hand, 25-lagged month PDSI shows high cross-correlation with SGI. PDSI was calculated by precipitation, temperature, and soil moisture [43]. SPEI based on precipitation and potential evapotranspiration, combines the sensitivity of PDSI to changes in evaporation, caused by temperature changes. This indicates that antecedent precipitation, evapotranspiration, and soil moisture had a large impact on groundwater storage changes within these months. This has already been discussed in previous studies [1,2]. 



**Figure 10.** Cross-correlation between SPEI–SGI with lag time; ( **a** ) SPEI-1–SGI; ( **b** ) SPEI-2–SGI; ( **c** ) SPEI-3–SGI; ( **d** ) SPEI-6–SGI; ( **e** ) PDSI-SGI. 

The cross-correlations between SGI, multiscale SPEI-associated accumulation periods, and PDSI with lag time for each administrative district are shown in Table 3. The SGI presents relatively good cross-correlation with SPEI-1 among the different timescales. Also, the SGI presents relatively good cross-correlation with PDSI; however, the lag time is longer than SPEI. Table 3 also lists the values of the maximum correlation coefficients between SGI and other drought indices (SPEI and PDSI), and lag time between SGI and other indices. The maximum cross-correlation between SGI and SPEI is in the range of 0.39–0.58, with the highest coefficient being 0.50 (SPEI-2 with a lag time of 1 month). Also, the maximum cross-correlation between SGI and PDSI is in the range of 0.12–0.48, with the highest coefficient being 0.40 (PDSI with a lag time of 19 month). These results imply that the antecedent meteorological and hydrological drought indices data could provide predictive information for the groundwater drought prediction. However, there is a difference in terms of drought intensity and duration between SGI and other indices. This is because the two drought indices have different characteristics. SPEI and PDSI is based on precipitation, evapotranspiration and soil moisture, and SGI is based on underground characteristics (percolation and infiltration caused by precipitation, and geological variables). 

16 of 19 

_Water_ **2019** , _11_ , 1953 

**Table 3.** Maximum cross-correlation (lag month) between SGI and other drought indices (SPEI and PDSI) during the study period. 

|**Administrative District**|**SPEI-1**|**SPEI-2**|**SPEI-3**|**SPEI-6**|**PDSI**|
|---|---|---|---|---|---|
|Seoul|0.47 (0)|0.48 (1)|0.47 (2)|0.46 (5)|0.48 (19)|
|Gyeonggi-do|0.44 (0)|0.47 (35)|0.47 (36)|0.46 (5)|0.46 (19)|
|Kangwon-do|0.43 (0)|0.50 (1)|0.50 (2)|0.44 (5)|0.36 (47)|
|Chuncheong-do|0.43 (0)|0.48 (0)|0.45 (1)|0.45 (4)|0.33 (35)|
|Jeolla-do|0.45 (0)|0.43 (0)|0.39 (24)|0.42 (5)|0.12 (65)|
|Gyeongsang-do|0.44 (−1)|0.47 (0)|0.46 (1)|0.43 (−9)|0.33 (36)|
|Total area|0.58 (−1)|0.55 (19)|0.50 (1)|0.48 (5)|0.38 (25)|



## **5. Conclusions** 

Recently, groundwater droughts have become increasingly recognized around the world. The standardized groundwater level index (SGI) has not been widely used due to the associated limitations of spatio-temporal observation. A new groundwater drought index estimation method using satellite data and an artificial neural network (ANN) model, which involved the detection of spatio-temporal groundwater drought conditions considering relatively high spatial resolution, was proposed in this study. 

In this study, GRACE terrestrial water storage changes, TRMM precipitation, GLDAS average temperature, and soil moisture changes data were applied in the ANN model to predict groundwater storage changes. The predicted downscaled groundwater storage changes were found to have high correlations with both the in situ and WBE-estimated groundwater storage changes, as reported in a previous study [11]. The ANN-predicted groundwater storage changes had lower RMSE and higher correlation than the WBE-estimated results when compared to in situ groundwater storage changes. However, there would be uncertainty due to grid-to-grid training through resampling of in situ data, and this may cause overfitting or leakage in the ANN model. This problem needs improvement through future research. 

This study proposed a SGI developed using a new downscaled groundwater storage changes prediction method. SGI was evaluated for the traditional meteorological drought index using SPEI as accumulation periods and the hydrological drought index PDSI. SGI and SPEI detected drought conditions during the dry season and, in particular, SGI was correlated with the SPEI-1 and with PDSI. These drought indices showed a relatively good correlation; however, the duration and the severity of these drought indices differed by situation. Therefore, drought analysis needs to be complemented with various drought indices. 

It can be concluded that the SGI results in this study showed good performance to reflect the spatio-temporal drought events. In addition, SGI is expected to contribute to the determination of appropriate measures according to the drought conditions and the corresponding risk. Improvement, however, is still needed for SGI developed in this study to be effectively applied to real-world practice such as reservoir management or irrigation. While changes in soil moisture by irrigation can affect groundwater recharge [44,45], the current SGI may miss the short-term variation in groundwater storages due to the relatively coarse temporal resolution of the GRACE data (monthly). Further research needs to be carried out in that regard. 

To dramatically improve the precision of GRACE mission, GRACE-FO (Follow-On), which is the next generation of GRACE satellites, was launched in May 2018. Also, GRACE-2 is scheduled to be launched. These satellites are expected to generate continuous hydrological data with remarkable accuracy. We believe that the results of this study can provide a useful framework to analyze groundwater droughts in watersheds better and to improve our society’s ability to cope with climate change. 

17 of 19 

_Water_ **2019** , _11_ , 1953 

**Author Contributions:** J.Y.S. led manuscript writing and conducted the research under the guidance of S.-I.L. S.-I.L. contributed to preparation of the manuscript through review and comments. 

**Funding:** This subject is supported by Korea Environment Industry & Technology Institute (KEITI) through Water Management Research Program, funded by Korea Ministry of Environment (MOE; 79623), and also supported by Basic Science Research Program through the National Research Foundation of Korea (NRF) funded by the ministry grant (NRF-2018R1D1A1A09083120). 

**Acknowledgments:** The Authors are grateful to anonymous reviewers for their constructive comments and suggestion. 

**Conflicts of Interest:** The authors declare no conflict of interest. 

## **References** 

1. Bloomfield, J.P.; Marchant, B.P. Analysis of groundwater drought building on the standardised precipitation index approach. _Hydrol. Earth Syst. Sci._ **2013** , _17_ , 4769–4787. [CrossRef] 

2. Lee, J.; Kang, S.; Jeong, J.; Chun, G. Development of groundwater level monitoring and forecasting technique for drought analysis (1)—Groundwater drought monitoring using standardized groundwater level index (SGI). _J. Korea Water Resour. Assoc._ **2018** , _51_ , 1011–1020. (In Korean) [CrossRef] 

3. Song, S.-H. Assessment of drought effects on groundwater system in rural area using Standardized Groundwater Level Index (SGI). _J. Soil Groundw. Environ._ **2018** , _23_ , 1–9. (In Korean) [CrossRef] 

4. Lee, J.M.; Park, J.H.; Chung, E.; Woo, N.C. Assessment of groundwater drought in the Mangyeong river basin, Korea. _Sustainability_ **2018** , _10_ , 831. [CrossRef] 

5. National Groundwater Information-Analysis Center. 2019. Available online: www.drought.go.kr/ (accessed on 31 July 2019). 

6. Thomas, B.F.; Famiglietti, J.S.; Landerer, F.W.; Wiese, D.N.; Molotch, N.P.; Argus, D.F. GRACE groundwater drought index: Evaluation of California Central Valley groundwater drought. _Remote Sens. Environ._ **2017** , _198_ , 384–392. [CrossRef] 

7. Rodell, M.; Velicogna, I.; Famiglietti, J.S. Satellite-based estimates of groundwater depletion in India. _Nature_ **2009** , _460_ , 999–1002. [CrossRef] 

8. Famiglietti, J.S.; Lo, M.; Ho, S.L.; Bethune, J.; Anderson, K.J.; Syed, T.H.; Swenson, S.C.; de Linage, C.R.; Rodell, M. Satellites measure recent rates of groundwater depletion in California’s Central Valley. _Geophys. Res. Lett._ **2011** , _38_ , L03403. [CrossRef] 

9. Scanlon, B.R.; Longuevergne, L.; Long, D. Ground referencing GRACE satellite estimates of groundwater storage changes in the California Central Valley, USA. _Water Resour. Res._ **2012** , _48_ , W04520. [CrossRef] 

10. Scanlon, B.R.; Faunt, C.C.; Longuevergne, L.; Reedy, R.C.; Alley, W.M.; McGuire, V.L.; McMahon, P.B. Groundwater depletion and sustainability of irrigation in the US High Plains and Central Valley. _Proc. Natl. Acad. Sci. USA_ **2012** , _109_ , 9320–9325. [CrossRef] 

11. Seo, J.Y.; Lee, S.-I. Integration of GRACE, ground observation, and land-surface models for groundwater storage variations in South Korea. _Int. J. Remote Sens._ **2016** , _37_ , 5786–5801. [CrossRef] 

12. Houborg, R.; Rodell, M.; Li, B.; Reichle, R.; Zitchik, B.F. Drought indicators based on model-assimilated Gravity Recovery and Climate Experiment (GRACE) terrestrial water storage observations. _Water Resour. Res._ **2012** , _48_ . [CrossRef] 

13. Rodell, M. _Satellite Gravimetry Applied to Drought Monitoring, Remote Sensing of Drought: Innovative Monitoring Approaches_ ; NASA Publications: Washington, DC, USA, 2012; Volume 218. 

14. Petropoulos, G.P.; Islam, T. _Remote Sensing of Hydrometeorological Hazards_ ; CRC Press: Boca Raton, FL, USA, 2018. 

15. Long, D.; Shen, Y.; Sun, A.; Hong, Y.; Longuevergne, L.; Yang, Y.; Li, B.; Chen, L. Drought and flood monitoring for a large karst plateau in Southwest China using extended GRACE data. _Remote Sens. Environ._ **2014** , _155_ , 145–160. [CrossRef] 

16. Sun, A. Predicting groundwater level changes using GRACE data. _Water Resour. Res._ **2013** , _49_ , 1–13. [CrossRef] 

17. Park, S.; Park, S.; Im, J.; Rhee, J.; Shin, J.; Park, J.D. Downscaling GLDAS Soil moisture data in East Asia through fusion of multi-sensors by optimizing modified regression trees. _Water_ **2017** , _9_ , 332. [CrossRef] 

18 of 19 

_Water_ **2019** , _11_ , 1953 

18. Seyoum, W.M.; Kwon, D.; Milewski, A.M. Downscaling GRACE TWSA data into high-resolution groundwater level anomaly using machine learning-based models in a glacial aquifer system. _Remote Sens._ **2019** , _11_ , 824. [CrossRef] 

19. GIMS. 2019. Available online: http://gims.go.kr/ (accessed on 31 July 2019). 

20. Lee, J.-Y.; Kwon, K.D. Current status of groundwater monitoring networks in Korea. _Water_ **2016** , _8_ , 168. [CrossRef] 

21. Swenson, S.C. _GRACE Monthly Land Water Mass Grids NETCDF RELEASE 5.0_ . Ver. 5.0 PO.DAAC. CA, USA. 2012. Available online: http://dxdoi.org/10.5067/TELND-NC005 (accessed on 1 December 2018). 

22. Landerer, F.W.; Swenson, S.C. Accuracy of scaled GRACE terrestrial water storage estimates. _Water Resour. Res._ **2012** , _48_ , W04531. [CrossRef] 

23. Swenson, S.C.; Wahr, J. Post-processing removal of correlated errors in GRACE data. _Geophys. Res. Lett._ **2006** , _33_ , L08402. [CrossRef] 

24. Huffman, G.J.; Adler, R.F.; Bolvin, D.T.; Gu, G.J.; Nelkin, E.J.; Bowman, K.P.; Hong, Y.; Stoker, E.F.; Wolff, D.B. The TRMM Multisatellite Precipitation Analysis (TMPA): Quasi-global, multi-year, combined-sensor precipitation estimates at fine scales. _J. Hydrometeorol._ **2007** , _8_ , 28–55. [CrossRef] 

25. Kim, J.P.; Jung, I.W.; Park, K.W.; Yoon, S.K.; Lee, D. Hydrological Utility and Uncertainty of Multi-Satellite Precipitation Products in the Mountainous Region of South Korea. _Remote Sens._ **2016** , _8_ , 608. [CrossRef] 

26. Seo, J.Y.; Lee, S.-I. Total discharge estimation in the Korean Peninsula using multi-satellite products. _Water_ **2017** , _9_ , 532. [CrossRef] 

27. Rodell, M.; Houser, P.R.; Jambor, U.; Gottschalck, J.; Mitchell, K.; Meng, C.-J.; Arsenault, K.; Cosgrove, B.; Radakovich, J.; Bosilovich, M.; et al. The Global Land Data Assimilation System. _Bull. Am. Meteorol. Soc._ **2004** , _85_ , 381–394. [CrossRef] 

28. Kim, N.J.; Cho, M.J.; Woo, N.C. Developing a national groundwater monitoring network in Korea. _Hydrogeol. J._ **1995** , _3_ , 89–94. [CrossRef] 

29. Korea Institute of Geoscience and Mineral Resources. Groundwater quality management and purification plan. In _Report of Korea Ministry of Environment_ ; Korea Institute of Geoscience and Mineral Resources: Daejeon, Korea, 2001. (In Korean) 

30. Kim, K. Study on the Conjugate Water Use between the Surface- and Groundwater in the Jeoncheon Basin. Master’s Thesis, Yonsei University, Seoul, Korea, 1997. (In Korean). 

31. Kim, G. Estimation of specific yield using rainfall and groundwater levels at shallow groundwater monitoring sites. _J. Korea Geo-Environ. Soc._ **2010** , _11_ , 57–67. (In Korean) 

32. Kim, N.W.; Kim, Y.J.; Chung, I.-M. Development of analyzing model of groundwater table fluctuation (1): Theory of model. _KSCE J. Civ. Eng._ **2013** , _33_ , 2277–2284. [CrossRef] 

33. Sridhar, V.; Wedin, D.A. Hydrological behavior of Grasslands of the Sandhills: Water and Energy Balance Assessment from Measurements, Treatments and Modeling. _Ecohydrology_ **2009** , _2_ , 195–212. [CrossRef] 

34. GRACE Tellus. 2019. Available online: http://grace.jpl.nasa.gov/groundwater (accessed on 31 July 2019). 

35. Long, D.; Chen, X.; Scanlon, B.R.; Wada, Y.; Hong, Y.; Singh, V.P.; Chen, Y.; Wang, C.; Han, Z.; Yang, W. Have GRACE satellites overestimated groundwater depletion in the Northwest India Aquifer? _Sci. Rep._ **2016** , _6_ , 24398. [CrossRef] [PubMed] 

36. Rahaman, M.M.; Thakur, B.; Kalra, A.; Ahmad, S. Modeling of GRACE-derived groundwater information in the Colorado River Basin. _Hydrology_ **2019** , _6_ , 19. [CrossRef] 

37. Hao, Y.; Wilamowski, B.M. _Levenberg-Marquardt Training, Industrial Electronics Handbook, Intelligent Systems_ , 2nd ed.; 12-1-12-15; CRC Press: Boca Raton, FL, USA, 2011. 

38. Demuth, H.; Bale, M.; Hagan, M. _Neural Network ToolboxTM User’s Guide_ ; TheMathWorks Inc.: Natick, MA, USA, 2008. 

39. Garson, G.D. Interpreting neural network connection weights. _AI Expert_ **1991** , _6_ , 47–51. 

40. Vicente-Serrano, S.M.; Beguería, S.; López-Moreno, J.I. A multi-scalar drought index sensitive to global warming: The Standardized Precipitation Evapotranspiration Index—SPEI. _J. Clim._ **2010** , _23_ , 1696–1718. [CrossRef] 

41. Van der Schrier, G.; Barichivich, J.; Briffa, K.R.; Jones, P.D. A scPDSI-based global data set of dry and wet spells for 1901–2009. _J. Geophys. Res. Atmos._ **2013** , _118_ , 4025–4048. [CrossRef] 

19 of 19 

_Water_ **2019** , _11_ , 1953 

42. Osborn, T.J.; Barichivich, J.; Harris, I.; van der Schrier, G.; Jones, P.D. Monitoring global drought using the self-calibrating Palmer Drought Severity Index [in “State of the Climate in 2016”]. _Bull. Am. Meteorol. Soc._ **2017** , _98_ , S32–S33. [CrossRef] 

43. Sehgal, V.; Sridhar, V.; Tyagi, A. Stratified drought analysis using a stochastic ensemble of simulated and insitu soil moisture observations. _J. Hydrol._ **2017** , _545_ , 226–250. [CrossRef] 

44. Sridhar, V. Tracking the influence of irrigation on land surface fluxes and boundary layer climatology. _J. Contemp. Water Res. Educ._ **2013** , _152_ , 79–93. [CrossRef] 

45. Jaksa, W.T.A.; Sridhar, V. Effect of irrigation in simulating long-term evapotranspiration climatology in a human-dominated river basin system. _Agric. For. Meteorol._ **2015** , _200_ , 109–118. [CrossRef] 



- © 2019 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (http://creativecommons.org/licenses/by/4.0/). 

