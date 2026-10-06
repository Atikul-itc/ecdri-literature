

# **Rapid #: -27621838** 

CROSS REF ID: **896739** 

LENDER: **CCH (California State University, Chico) :: Meriam Library** BORROWER: **IRU (New Mexico State University) :: Main Library** 

TYPE: Article CC:CCL JOURNAL TITLE: Catena USER JOURNAL TITLE: Catena. ARTICLE TITLE: A remote sensing and artificial neural network-based integrated agricultural drought index: Index development and applications ARTICLE AUTHOR: , Liu Xianfeng VOLUME: 186 ISSUE: MONTH: 3 YEAR: 2020 PAGES: 104394 ISSN: 0341-8162 OCLC #: 

Processed by RapidX: 10/5/2026 12:24:08 PM 

This material may be protected by copyright law (Title 17 U.S. Code) 

Catena 186 (2020) 104394 



Contents lists available at ScienceDirect 

## Catena 

journal homepage: www.elsevier.com/locate/catena 



### A remote sensing and artificial neural network-based integrated agricultural drought index: Index development and applications 



<!-- Start of picture text -->
T<br><!-- End of picture text -->

#### Xianfeng Liu<sup>a,b,⁎</sup> , Xiufang Zhu<sup>b,c</sup> , Qiang Zhang<sup>b,d</sup> , Tiantian Yang<sup>e</sup> , Yaozhong Pan<sup>c</sup> , Peng Sun<sup>f</sup> 

> a School of Geography and Tourism, Shaanxi Normal University, Xi’an 710119, China 

> b Key Laboratory of Environmental Change and Natural Disaster, Ministry of Education, Beijing Normal University, Beijing 100875, China 

> c Institute of Remote Sensing Science and Engineering, Faculty of Geographical Science, Beijing Normal University, Beijing 100875, China 

> d Academy of Disaster Reduction and Emergency Management, Faculty of Geographical Science, Beijing Normal University, Beijing 100875, China 

> e School of Civil Engineering and Environmental Science, the University of Oklahoma, Oklahoma, USA 

> f College of Territorial Resources and Tourism, Anhui Normal University, Anhui 241002, China 

|A R T I C L E I N F O|A B S T R A C T|
|---|---|
|Keywords:<br>|Reliable drought monitoring is critical for evaluating drought risk and reducing potential agricultural losses.|
|Agricultural drought<br>Drought index<br>Drought monitoring<br>Remote sensing data<br>Artificial neural network|However, many existing drought indices developed by a single indicator may not properly describe the complex<br>features of agricultural drought. Here, we propose a new drought index—the integrated agricultural drought<br>index (IDI), which describes the relationship between multiple variables and agricultural drought conditions.<br>The derivation of IDI is based on the remote sensing data and the back-propagation (BP) neural network, capable<br>of identifying the non-stationary relationship of drought conditions. Development of IDI involves the following<br>meteo-hydrological variables: precipitation, land surface temperature (LST), normalized difference vegetation<br>index (NDVI), soil water capacity, and elevation. The lagging effect of NDVI with respect to precipitation and<br>LST changes can also be captured by the proposed IDI. Our results indicate that the IDI based on a machine<br>learning method can relax the assumption used in many existing indices that the input and output data are<br>linearly correlated. Results also demonstrate that the IDI is close to SPI-3 and SPEI-3 in a case study of the North<br>China Plain (NCP). Moreover, we found the drought condition in the NCP area is highly correlated with 10 cm<br>depth soil moisture at 8 agrometeorological stations and the newly developed IDI can effectively monitor the<br>drought in terms of onset, duration, extent, and intensity of a drought episode. Additionally, the IDI provides<br>spatial information about root zone soil moisture that can facilitate agricultural drought monitoring. The pro-<br>posed framework of IDI can also be applied in other regions of the world for agriculture management.|



##### 1. Introduction 

Drought is the most costly and poorly understood natural disaster that imposes significant challenges for food security and water resources management (AghaKouchak, et al., 2015; Hao and Singh, 2015; Yang, 2017a,b; Zhang et al., 2015). Changing hydroclimatic and socioeconomic conditions have aggravated water scarcity over the past decades—particularly spatiotemporal alterations of precipitation regimes due to warming climate and ENSO events evidently alter spatiotemporal patterns of floods and droughts (Zhang et al., 2015; Zhang et al., 2013). Variability of droughts, floods, and precipitation have further changed agriculture sectors across the world, and food security has been drawing increasing attentions from academic communities in recent decades (Douglas, 2009; Zhang et al., 2012). 

Monitoring drought is critical for its mitigation and early warning. 

Generally, drought can be classified into four main categories: meteorological, agricultural, hydrological, and socioeconomic drought (Heim, 2002). For agricultural drought modeling, root zone soil moisture is important and relatively stable compared to the surface soil moisture because the latter is sensitive to other environment variables. Globally, a wide range of drought indices have been developed to characterize the onset, intensity, and spatial expansion of droughts from the perspective of meteorology, hydrology, and agriculture (Zhang et al., 2019), including the indices based on single variables, such as precipitation (McKee et al., 1993), runoff (Vicente-Serrano et al., 2011), soil water storage (Hao and AghaKouchak, 2013), satellite-based measures of vegetation growth, and land surface temperature (Kogan, 1995; Mu et al., 2013). However, agricultural drought is the nexus between meteorology, soil, and crop systems, termed as the soil-plantatmosphere continuum. Most of these above indices mainly reflect one 

> ⁎ Corresponding author at: School of Geography and Tourism, Shaanxi Normal University, Xi’an 710119, China. E-mail address: liuxianfeng7987@163.com (X. Liu). 

https://doi.org/10.1016/j.catena.2019.104394 Received 28 March 2019; Received in revised form 12 November 2019; Accepted 25 November 2019 Available online 07 December 2019 0341-8162/ © 2019 Elsevier B.V. All rights reserved. 

X. Liu, et al. 

_Catena 186 (2020) 104394_ 

specific aspect of drought and lack the ability to identify the complex features of agriculture drought. 

An individual drought indicator is generally not sufficient for characterizing complex drought conditions and impacts. Multiple drought-related variables and indices are required to capture different aspects of complicated drought conditions. To address these issues, several integrated drought indices have been developed recently to combine multiple drought-related variables and indices to improve drought characterizations (AghaKouchak, 2015; Brown et al., 2008; Hao and AghaKouchak, 2014; Rhee et al., 2010; Sun et al., 2017; Wu, 2013; Zhang and Jia, 2013). The foremost effort is the development of the U.S. Drought Monitor (USDM), which blends drought information from a variety of sources—including gauge measurements, remote sensing, land surface simulations, and inputs from local experts (Hao and Singh, 2015). Brown et al (2008) proposed a vegetation drought response index (VegDRI) by combining the meteorological drought indices, the vegetation index, and a digital elevation model. This index can provide near-real country scale drought information and has become a model for comprehensive drought monitoring indices. These integrated drought indices have significantly improved the capacity of drought monitoring and early warning. 

Going further, how to combine multiple variables and indices is important in developing integrated drought indices. Generally, the development of integrated drought indices can be grouped into three categories: linear combination (Rhee et al., 2010), copula-based method (Hao and AghaKouchak, 2014), and machine learning (Brown et al., 2008; Wu et al., 2013). Most of the current integrated drought indices are developed by the former two approaches, which may suffer from the linearity assumption with weights or parameters associated with different variables and indices (Hao and Singh, 2015). A potential drawback of using the copula-based method is that it is only comparable with other multivariate probabilities with the same sets of margins (Hao and Singh, 2015). Machine learning, such as an artificial neural network tool that has been widely used to derive remote sensing precipitation (Ashouri et al., 2015) and leaf area index (Zhu et al., 2013), has gained popularity in various types of studies because of its strong capability of extracting target information from a large amount of random, noisy data, and catering to the characteristics of physical processes, such as agricultural drought (Yang et al., 2017a,b). 

Notably, different drought-related variables are time asynchronous. For example, agricultural drought that is described by soil moisture could lag behind meteorological drought that is expressed by precipitation. Another concern in current studies is the neglect of the lagging effect of vegetation response to water deficit, which may not properly describe the underlying features. Therefore, the primary purposes of this study was to address the following two scientific issues: (1) development of an integrated agricultural drought index (IDI) incorporating time lag effects using a nonlinear artificial neural network based on multisource remote sensing data; (2) verification and assessment of applicability of the proposed IDI against in-situ soil moisture observation and typical drought episodes. This current study is designed to provide a new framework in drought monitoring and drought index for agricultural management and planning. 

##### 2. Study region and data 

Wen, 2002; Xu et al., 2005). Hence, an investigation on the development of a drought index and relevant application in drought monitoring in the NCP is of practical and theoretical merit. 

##### 2.2. Data 

Data analyzed in this study are in situ meteorological data, agrometeorological data, remotely sensed data, and biophysical data. Specifically, the meteorological data are mainly temperature, precipitation, relative humid, sunshine hour, and wind speed at a daily time scale obtained from 53 stations covering the period of 2003–2014. Locations of the meteorological stations can be found in Fig. 1. The meteorological data were obtained from the China Meteorological Information Center (http://cdc.cma.gov.cn). The in situ soil moisture observations with time step of 10 days were obtained at 16 agro-meteorological stations. The soil moisture data were provided by the China Meteorological Information Center (http://cdc.cma.gov.cn). This data record contains considerably detailed information on vegetation growth stage and soil moisture in different layers of soil profile depth. In this study, we selected the 10 cm-depth soil moisture data that is suitable for monitoring performance of agricultural drought indices. Data quality control was also carried out on the aforementioned datasets. In terms of the remotely sensed data, the monthly maximum Normalized Difference Vegetation Index (NDVI) time series products (MOD13A3) and an 8-day average value of composited Land Surface Temperature (LST) products (MYD11A2) with 1 km × 1 km from 2003 to 2014 were acquired from the U.S. Geological Survey (https://e4ftl01.cr.usgs.gov/ ). The 8-day composite LST data were aggregated into monthly data by calculating the average value of adjacent images to maintain the same temporal resolution as that of NDVI dataset. The NDVI and LST datasets were extracted with high quality pixels based on quality analysis and quality control files and reconstructed by a certain low-quality pixels by data interpolation algorithm (Li et al., 2015). The tropical rainfall measuring mission (TRMM) data product (3B43) with 0.25°×0.25° spatial resolution and monthly temporal scale during 2003–2014 were downloaded from the Goddard Earth Sciences Data and Information Services Center. The TRMM data over the study area is compared to the in situ observed precipitation (Liu, 2016). The TRMM data record was further resampled to 1 km × 1 km spatial resolution to match with the spatial resolutions of NDVI and LST datasets. Soil type data and digital elevation data (DEM) of study area was derived from the China Western Environment and Ecology Science Data Center (http://westdc.westgis. ac.cn). The final resolution of all input data for IDI product is 1 km × 1 km. 

##### 3. Methodology 

The process of developing IDI can be divided into three steps. First, we selected the variables related to agricultural drought conditions and identified the time lags response of vegetation to climate factors by using partial correlation analysis. Then, we constructed the structure of Back-propagation (BP) Neural Network. Finally, we trained the BP model with in situ soil moisture and validated IDI against with the remaining in situ soil moisture that are not involved in model development. The detail technical framework for development of the IDI can be found in Fig. 2. 

##### 2.1. Study region 

##### 3.1. Variables for development of IDI 

The North China Plain (NCP) (113°E-123°E, 32°N-43°N) is in northern China (Fig. 1). Due to its low-lying terrain and fertile soil, the NCP is the main supplier of agriculture products in China with cultivated land area accounting for 27.9% of the total arable land in China. However, the NCP has been hit by frequent droughts and the frequency of droughts in the study region is highest in comparison to other regions of China (Hu et al., 2010; Liu et al., 2015). As a result, frequent droughts have remarkable challenges for food security in China (Fu and 

Agricultural drought is a slow process that begins with precipitation deficits. It then leads to soil moisture deficits that lead to a higher land surface temperature than normal, and the vegetation growth will be influenced by this process eventually (Du et al., 2013). Thus, to develop the integrated agricultural drought index, we must comprehensively consider the overall effects of precipitation, soil, vegetation, and regional environment conditions, including precipitation anomaly 

2 

X. Liu, et al. 

_Catena 186 (2020) 104394_ 



Fig. 1. Locations of the study region and meteorological stations. 

(aPRE), LST anomaly (aLST), NDVI anomaly (aNDVI), available water content of soil (AWC), and elevation (DEM). It should be noted that the lagging effects of vegetation response to precipitation and the LST changes vary from one region to another. Thus, prior to the modeling scheme, we first quantified the time lags of vegetation in the NCP. The results showed that 0 and 1 month of time lag can be confirmed for vegetation responses to precipitation and LST (Fig. 3), indicating concurrent effect of precipitation and LST during the current and the former months on agricultural drought development. Therefore, the former month precipitation and LST were introduced to the input variables for the development of IDI, according to the aforementioned time lags of NDVI to PRE and LST. The anomaly calculation formula is as follow: 

¯ _Xa_ = _X_ i − _X σ_ 

month; _X_ i is the variables in a certain month; _X_<sup>¯</sup> is the mean value of variables in a certain period; and _σ_ is the standard deviation of variables in a certain period. The greater the value of _Xa_ , the more abnormalities in the variabilities of indices. 

It should be noted that the above multisource remote sensing data are scaled to a standardized drought parameter range of [0,1] in the proposed integrated drought index. Then, based on the 16 agro-meteorological stations in the study area, we extracted the monthly mean values within a boundary of 3 km × 3 km domain and used that as the final input dataset. In terms of output data, researchers usually regard soil moisture as the most appropriate indicator of agricultural droughts, causing increasing demand for detailed predictions of soil moisture (Sheffield and Wood, 2008; Zhao et al., 2016); therefore, we selected 10 cm soil moisture as the final dependent variable in the IDI model. 

where _Xa_ is the anomaly variables (aPRE, aLST, or aNDVI) in a certain 



Fig. 2. Technical framework for the development of IDI (AWC: available water content). 

3 

X. Liu, et al. 

_Catena 186 (2020) 104394_ 



Fig. 3. Spatial distribution of time lags of vegetation response to precipitation (a) and land surface temperature (b). 

##### 3.2. Structure of Back-propagation neural network 

Artificial neural network (ANN) enables building of linkages between different variables without presuming any null hypothesis (Yang et al., 2017a,b; Zhu et al., 2013). The BP neural network has been widely used and involves three layers: input layer, hidden layer, and output layer. Signals flow from the input layer to the hidden layer and finally to the output layer. The error in the output layer will be propagated backwards to the hidden and the input layers. The abovementioned iteration will stop when the final output conforms to the user-defined error tolerance threshold. In this study, we built a threelayer ANN model with the BP scheme. The number of neurons of input layer and output layer are seven (including the current and former month precipitation and LST anomaly, NDVI anomaly, AWC, DEM) and one, respectively (Fig. 4). The strategy of selecting the number of neurons in the hidden layer is not confirmative. More neurons in the hidden layer will result in more flexibility but potentially causes an over-fitting problem. The iteration was set to formulate a hidden layer with eleven neurons. 

hence precipitation, temperature, and vegetation conditions are subject to seasonal and interannual variability. Therefore, the integrated agricultural drought index was developed for each individual month. Given a certain month, the performance of the BP model was evaluated by subdividing the entire data series into three parts: 70% of the data series were taken as the training dataset, 15% as the validation dataset, and 15% the verification dataset. The BP model was trained until its performance reached the peak (Zhu et al., 2013). The test dataset provides an independent assessment of the performance of BP model in capturing the drought properties. The cost function is used in the BP model, which depicts the differences between the model and the target outputs. Based on the above-mentioned training strategy, independent training runs 10 times to optimize the initial values until the final prediction model was obtained with the highest robustness and optimal modelling performance. 

The aforementioned training practices helped to produce 12 BP models for development of the integrated agricultural drought for each individual month. A total of 144 images from the IDI-based drought monitoring products were obtained for each individual month across the NCP during 2003–2014 with 1 km × 1 km spatial resolution. 

##### 3.3. Training the BP model 

The NCP is climatically characterized by the East Asia monsoon and 



Fig. 4. Structure of the back-propagation Neural Network. 

##### 4. Results and discussions 

##### 4.1. Comparisons between IDI and PDSI, SPI, SPEI 

Comparisons of IDI against 3-month Standardized Precipitation Index (SPI), 3-month Standardized Precipitation-Evapotranspiration Index (SPEI), and Palmer Drought Severity Index (PDSI) were done at 53 stations across the NCP (Fig. 5). It can be observed from Fig. 5 that the average IDI is close to SPI-3 and SPEI-3 but is subject to a larger difference from PDSI, and this is particularly true for the difference between PDSI and IDI before 2011. PDSI tends to overestimate drought conditions due to the fact that PDSI is very sensitive to temperature variations (Sheffield et al., 2012). In addition, our previous study (Liu et al., 2018) also demonstrated that SPI and SPEI are superior to PDSI in monitoring agricultural drought across the NCP, and the correlation between crop yield and SPEI (SPI) is also higher than that for PDSI. The results portray that IDI is an effective indicator in reflecting the true drought conditions. IDI can also monitor drought conditions across 

4 

X. Liu, et al. 

_Catena 186 (2020) 104394_ 



Fig. 5. Comparisons of IDI against SPI-3, SPEI-3, and PDSI. 

widespread spatial area, which is superior over many existing drought indices based on in situ observations. The technical framework proposed in this current study can also be used in the development of drought monitoring models in other regions of the world. 

##### 4.2. Drought monitoring performance of IDI based on in situ soil moisture 

Soil moisture is an important agricultural drought monitoring indicator (Wang et al., 2015), thus we carried out a validation experiment for IDI using in situ soil moisture observation data that is exclusive in model development in space and time. From the spatial perspective, we extracted IDI series at 3 km × 3 km spatial resolution for each station during 2003–2014, and then we compared the IDI series against the in situ soil moisture series at each station across the NCP; from a temporal perspective, the values of IDI for each month was filtered out and the same procedure was done for the in situ soil moisture observation (Fig. 6). IDI and soil moisture are correlated across all stations considered in this study with the correlation coefficients between 0.52 and 0.73 (Fig. 6). The correlations between IDI and in situ soil moisture observation are statistically significant at 0.01 confidence level; and the correlation coefficients between IDI and soil moisture were higher during spring and summer than autumn and winter (Fig. 7). These analytical results indicate that the proposed IDI can capture the soil moisture variation during a drought condition. 

for a typical year with extreme drought conditions. Fig. 8 depicts that the proposed IDI can capture onset, duration, extent, and the end of the fast extreme drought that occurred over the NCP during the summer of 2014. Fig. 8 also illustrates that incipient drought occurred over most of the regions of NCP in June, and then drought-affected regions expanded rapidly across almost the entire NCP with increased drought intensity in July. In particular, drought intensity increased significantly in the central Henan province. Summer precipitation in 2014 in the Henan province was the lowest since 1960 and was accompanied by high temperatures (Fig. 9), which induced a sharp decrease in soil moisture and consequent occurrence of extreme agricultural drought in a wide spatial domain. This extreme drought episode lasted until August with different spatial pattern when compared to that of July with higher drought intensity in the Shandong province. However, relatively lower drought intensity can be found in the Henan province (Fig. 8). Abovementioned drought processes halted in September and were followed by wetting tendencies in southeastern Henan province in October. This temporal pattern of drought processes is consistent with the soil moisture variation (Becker-Reshef et al., 2010). The monitoring results in the rest of the months are also in agreement with the official government report of soil moisture in each province (http://www.agri.cn/ ). Our results suggested that the proposed IDI were able to accurately capture the whole process of a typical drought episode with comprehensive spatial information. 

##### 4.3. Drought monitoring performance evaluation of IDI for typical dry year 

##### 4.4. Limitations and challenges for application of IDI in drought monitoring 

In this study, drought monitoring performance of IDI was evaluated 

Aforementioned results showed the proposed IDI is a good indicator 



Fig. 6. Correlations between IDI and in situ soil moisture observations in 10 cm depth soil layer at 8 stations across the study region. The red solid line is linear fitting, and the double solid green line indicate significant at 95% confidence. 

5 

X. Liu, et al. 

_Catena 186 (2020) 104394_ 



Fig. 7. Correlations between IDI and in situ soil moisture observations for each individual month between 2003 and 2014. The red solid line is linear fitting, and the double solid green line indicate significant at 95% confidence. 

for agricultural drought monitoring. The comparison experiment of IDI against SPI, SPEI, and PDSI indicated that IDI has the advantages over others over the NCP areas of China. However, it should be noted that every method or technique always has its own strength and/or weakness. There remain some issues about potential application of IDI in agricultural drought monitoring practices. Firstly, we focus mainly on the development of the index, hence the time interval of the proposed IDI is one month, which means the current index cannot monitor drought events at a finer temporal scale less than 1 month; secondly, the newly proposed IDI in this study only involves hydrological and meteorological variables and hence IDI cannot differentiate the differences between impacts of droughts on different crops, such as winter wheat and summer maize, and related impacts of IDI-based droughts on crops during different growth stages of a certain specific crop. However, the sensitivity of crop yields to drought impacts are different during different growing periods of corps. Nevertheless, the IDI proposed in this study can still help to monitor agricultural drought conditions and allow decision makers to formulate alternative management policies to mitigate the impacts of agricultural droughts. Expectantly, it is believed that increasing temporal scales of the remotely sensed data, together with the incorporation of more input variables into an ANN model, can greatly help us improve the monitoring performance of IDI. In this case, ongoing work can be suggested as: (1) the remotely sensed data with higher temporal resolution such as 10-day or weekly can potentially improve the drought monitoring performance of IDI; (2) more information pertaining to crop growth as input variable for ANN can be expected to improve the drought monitoring performance of IDI. It should be noted that although agricultural irrigation plays an important role in the alleviation of agricultural drought, the irrigation information will reflect the soil moisture changes, which has already been incorporated in the presented development of the IDI. Therefore, irrigation will not affect the presented results; instead, it will influence the 

prediction of agricultural drought. 

##### 5. Conclusions 

In this study, we developed an integrated agricultural drought index based on multisource remote sensing data and a nonlinear machine learning method over the North China Plain. Multiple variables selected from the atmosphere, soil, and crop systems were involved in the integrated agricultural drought index, and the lagging effect of NDVI to LST and precipitation changes was also considered in the newly developed IDI. Therefore, the IDI developed in this current study fully manifests itself as the “integrated” feature by involving multisource data and physical processes within drought. The newly developed IDI based on a nonlinear machine learning method avoids the assumption of linearity between input and output variables, which was usually ignored in other indices. Moreover, the IDI is close to SPI-3 and SPEI-3 and can potentially discover the true drought conditions. Compared with the results from PDSI, the newly developed IDI is relatively stable, robust, and has less overestimation on the drought conditions. Therefore, the advantage of IDI over other standing drought indices is apparent. The newly-proposed IDI is highly correlated with 10 cm depth soil moisture at agro-meteorological stations across the NCP. The IDI can monitor soil moisture changes, which are critical in influencing factors for agricultural droughts, in both space and time. Therefore, we conclude that the newly developed IDI enables effective monitoring of the onset, duration, extent, and intensity for an agricultural drought episode. The IDI can provide a full picture about agricultural drought conditions, indicating significant potentials for root zone soil moisture and agricultural drought monitoring. Also, the technical framework proposed in this current study can be used in the development of agricultural drought monitoring models in other regions of the world. 

6 

X. Liu, et al. 



<!-- Start of picture text -->
Catena 186 (2020) 104394<br><!-- End of picture text -->



Fig. 8. Drought process captured by IDI over the NCP in 2014. 

##### Declaration of Competing Interest 

influence the work reported in this paper. 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to 



Fig. 9. Ranked historical July (a) precipitation and (b) temperature for Henan Province. 

7 

X. Liu, et al. 

_Catena 186 (2020) 104394_ 

##### Acknowledgments 

The authors would like to thank the United States Geological Survey for providing MODIS products and the Goddard Earth Sciences Data and Information Services Center for providing tropical rainfall measuring mission data product during 2003–2014. This work was supported by the National Natural Science Foundation of China (No. 41801333; 41771536; 41601023), the National Science Foundation for Distinguished Young Scholars of China (No. 51425903), the Fund for Creative Research Groups of National Natural Science Foundation of China (No. 41621061), and China Postdoctoral Science Foundation (2019M650859 and 2019T120142). 

##### References 

- AghaKouchak, A., et al., 2015. Remote sensing of drought: progress, challenges and opportunities. Rev. Geophys. 53 (2), 452–480. 

- AghaKouchak, A., 2015. A multivariate approach for persistence-based drought prediction: Application to the 2010–2011 East Africa drought. J. Hydrol. 526, 127–135. 

- Ashouri, H., et al., 2015. PERSIANN-CDR: Daily Precipitation Climate Data Record from Multisatellite Observations for Hydrological and Climate Studies. Bull. Am. Meteorol. Soc. 96 (1), 69–83. 

- Becker-Reshef, I., et al., 2010. Monitoring Global Croplands with Coarse Resolution Earth Observations: The Global Agriculture Monitoring (GLAM) Project. Remote Sensing 2 (6), 1589–1609. 

- Brown, J.F., Wardlow, B.D., Tadesse, T., Hayes, M.J., Reed, B.C., 2008. The Vegetation Drought Response Index (VegDRI): A New Integrated Approach for Monitoring Drought Stress in Vegetation. GISci. Rem. Sens. 45 (1), 16–46. 

- Douglas, I., 2009. Climate change, flooding and food security in south Asia. Food Security 1 (2), 127–136. 

- Du, L., et al., 2013. A comprehensive drought monitoring method integrating MODIS and TRMM data. Int. J. Appl. Earth Obs. Geoinf. 23, 245–253. 

- Fu, C., Wen, G., 2002. Several issues on aridification in the Northern China. Climate Environ. Res. 7 (1), 22–29. 

- Hao, Z., AghaKouchak, A., 2013. Multivariate Standardized Drought Index: A parametric multi-index model. Adv. Water Resour. 57, 12–18. 

- Hao, Z., AghaKouchak, A., 2014. A Nonparametric Multivariate Multi-Index Drought Monitoring Framework. J. Hydrometeorol. 15 (1), 89–101. 

- Hao, Z., Singh, V.P., 2015. Drought characterization from a multivariate perspective: A review. J. Hydrol. 527, 668–678. 

- Heim, R.R., 2002. A Review of Twentieth-Century Drought Indices Used in the United States. Bull. Am. Meteorol. Soc. 83 (8), 1149. 

- Hu, S., Mo, X., Lin, Z., Qiu, J., 2010. Emergy Assessment of a Wheat-Maize Rotation System with Different Water Assignments in the North China Plain. Environ. Manage. 46 (4), 643–657. 

- Kogan, F.N., 1995. Drought of the late 1980s in the United States as derived from NOAA Polar-orbiting satellite data. Bull. Am. Meteorol. Soc. 76 (5), 655–668. 

- Li, T., Zhu, X., Pan, Y., Liu, X., 2015. Study on NDVI Time-series reconstruction methods of China's HJ satellite imagery. Rem. Sens. Inform. 30 (1), 3–11. 

- Liu, X., et al., 2015. Investigation of the probability of concurrent drought events between the water source and destination regions of China's water diversion project. Geophys. Res. Lett. 42 (20), 8424–8431. 

- Liu, X., 2016. Modeling and application for agricultural drought monitoring and loss preassessment. Normal University, Beijing. 

- Liu, X., Zhu, X., Pan, Y., Bai, J., Li, S., 2018. Performance of different drought indices for agriculture drought in the North China Plain. J. Arid Land. 

- McKee, T.B., Doesken, N.J., Kleist, J., 1993. The relationship of drought frequency and duration to time scales. Eighth conference on applied climatogy. American meteorological society, Anaheim, CA. 

- Mu, Q., Zhao, M., Kimball, J.S., McDowell, N.G., Running, S.W., 2013. A Remotely Sensed Global Terrestrial Drought Severity Index. Bull. Am. Meteorol. Soc. 94 (1), 83–98. 

- Rhee, J., Im, J., Carbone, G.J., 2010. Monitoring agricultural drought for arid and humid regions using multi-sensor remote sensing data. Remote Sens. Environ. 114 (12), 2875–2887. 

- Sheffield, J., Wood, E.F., 2008. Global trends and variability in soil moisture and drought characteristics, 1950–2000, from observation-driven simulations of the terrestrial hydrologic cycle. J. Clim. 21 (3), 432–458. 

- Sheffield, J., Wood, E.F., Roderick, M.L., 2012. Little change in global drought over the past 60 years. Nature 491 (7424), 435–438. 

- Sun, P., Zhang, Q., Wen, Q., Singh, V.P., Shi, P., 2017. Multisource data based integrated agricultural drought monitoring in the Huai River basin, China. J. Geophys. Res.Atmosp. https://doi.org/10.1002/2017JD027186. 

- Vicente-Serrano, S.M., Beguería, S., López-Moreno, J.I., 2011. Comment on 

   - “Characteristics and trends in various forms of the palmer drought severity index (PDSI) during 1900–2008” by Aiguo Dai. J. Geophys. Res. 116 (D19). 

- Wang, H., Rogers, J.C., Munroe, D.K., 2015. Commonly Used Drought Indices as 

   - Indicators of Soil Moisture in China. J. Hydrometeorol. 16 (3), 1397–1408. 

- Wu, J., et al., 2013. Establishing and assessing the Integrated Surface Drought Index (ISDI) for agricultural drought monitoring in mid-eastern China. Int. J. Appl. Earth Obs. Geoinf. 23, 397–410. 

- Xu, G., Yang, X., Sun, X., 2005. Interdecadal and interannual variation characteristics of rainfall in North China and its relation with the northern hemisphere atmospheric circulations. Chin. J. Geophys. 48 (3), 511–518. 

- Yang, T., et al., 2017a. An Enhanced Artificial Neural Network with A Shuffled Complex Evolutionary Global Optimization with Principal Component Analysis. Infrom. Sci. https://doi.org/10.1016/j.ins.2017.08.003. 

- Yang, T., et al., 2017b. Developing reservoir monthly inflow forecasts using artificial intelligence and climate phenomenon information. Water Resour. Res. 

- Zhang, A., Jia, G., 2013. Monitoring meteorological drought in semiarid regions using multi-sensor microwave remote sensing data. Remote Sens. Environ. 134, 12–23. 

- Zhang, B., AghaKouchak, A., Yang, Y., Wei, J., Wang, G., 2019. A water-energy balance approach for multi-category drought assessment across globally diverse hydrological basins. Agric. For. Meteorol. 264, 247–265. 

- Zhang, Q., Gu, X., Singh, V.P., Kong, D., Chen, X., 2015. Spatiotemporal behavior of floods and droughts and their impacts on agriculture in China. Global Planet. Change 131, 63–72. 

- Zhang, Q., Li, J., Singh, V.P., Xiao, M., 2013. Spatio-temporal relations between temperature and precipitation regimes: Implications for temperature-induced changes in the hydrological cycle. Global Planet. Change 111, 57–76. 

- Zhang, Q., Sun, P., Singh, V.P., Chen, X., 2012. Spatial-temporal precipitation changes (1956–2000) and their implications for agriculture in China. Global Planet. Change 82–83, 86–95. 

- Zhao, J., Xu, J., Xie, X., Lu, H., 2016. Drought monitoring based on TIGGE and distributed hydrological model in Huaihe River Basin, China. Sci. Total Environ. 553, 358–365. 

- Zhu, Z., et al., 2013. Global Data Sets of Vegetation Leaf Area Index (LAI)3g and Fraction of Photosynthetically Active Radiation (FPAR)3g Derived from Global Inventory Modeling and Mapping Studies (GIMMS) Normalized Difference Vegetation Index (NDVI3g) for the Period 1981 to 2011. Rem. Sens. 5 (2), 927–948. 

8 

