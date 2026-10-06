Agricultural Water Management 325 (2026) 110128 



Contents lists available at ScienceDirect 

# Agricultural Water Management 

journal homepage: www.elsevier.com/locate/agwat 



## Initial soil moisture conditions dominate variation in event-scale propagation time from meteorological to agricultural drought 



Zhengguang Xu<sup>a,b</sup> , Bo Jiang<sup>a</sup> , Xiao Guo<sup>c,*</sup> , Zhiyong Wu<sup>d</sup> , Siqi Fan<sup>e</sup> 

a _School of Water Conservancy, North China University of Water Resources and Electric Power, Zhengzhou 450046, China_ 

b _Henan Provincial Key Laboratory of Hydrosphere and Watershed Water Security, North China University of Water Resources and Electric Power, Zhengzhou 450046, China_ 

c _Hydrological Bureau, Yellow River Conservancy Commission, Zhengzhou 450004, China_ 

d _College of Hydrology and Water Resources, Hohai University, Nanjing 210098, China_ 

e _River and Reservoir Management Service Center of Liaoning Province (Hydrology Bureau of Liaoning Province), Shenyang 110003, China_ 

|A R T I C L E I N F O|A B S T R A C T|
|---|---|
|Handling Editor - Rodney Thompson<br>|Agricultural drought, typically triggered by meteorological drought, poses a significant threat to crop production<br>and regional water resources. Understanding the propagation from meteorological to agricultural drought is|
|_Keywords:_<br>|therefore crucial for improving drought early warning and agricultural water management. In this study, we|
|Drought propagation<br>Meteorological drought<br>Agricultural drought<br>Propagation time<br>XGBoost algorithm<br>Yellow River Basin|investigated event-scale drought propagation in the Yellow River Basin using the Standardized Precipitation<br>Evapotranspiration Index and Standardized Soil Moisture Index to characterize meteorological and agricultural<br>droughts, respectively. Variations in drought characteristics (duration and intensity) across the entire drought<br>event and during its development, persistence, and recovery stages were analyzed based on matched drought<br>events. We further identified the dominant drivers and constructed predictive models of propagation time using<br>the eXtreme Gradient Boosting (XGBoost) algorithm. The results indicate that agricultural droughts occur less<br>frequently and with lower intensity but persist longer than meteorological droughts. Approximately 49.5 % of<br>meteorological droughts propagate into agricultural droughts, with the one-to-one propagation type being<br>dominant. Lengthening of duration and attenuation of intensity were observed during drought propagation<br>across different drought stages. Initial soil moisture conditions emerged as the dominant driver of event-scale<br>propagation time, followed by the timing of meteorological drought occurrence and its development duration.<br>Based on the identified dominant influencing factors, a propagation time prediction model was constructed for<br>each subregion using the XGBoost algorithm, enabling reliable prediction of propagation time. These findings<br>underscore the critical role of initial soil moisture in regulating drought propagation, offering valuable insights<br>for the development of agricultural drought early warning systems and the optimization of irrigation scheduling.|



### **1. Introduction** 

Drought is one of the most devastating natural hazards, exerting widespread and long-lasting impacts on water supply, crop yields, and ecosystems (Mondal et al., 2023; Wu et al., 2025; Zhou et al., 2021). In recent decades, the frequency and severity of drought events have increased across many regions worldwide, largely due to the combined effects of natural climate variability and intensified human activities (Yuan et al., 2023; Zhao et al., 2022). This growing trend has made drought a critical challenge for water resource management. Accordingly, improving our understanding of drought occurrence and underlying mechanisms is essential for enhancing early warning systems and 

developing effective mitigation strategies. 

Droughts are generally classified into meteorological, agricultural, hydrological, and socio-economic types, each representing different aspects of the hydrological cycle and its interaction with human activities (Barker et al., 2016; Bevacqua et al., 2021; Li et al., 2020). Meteorological drought is characterized by a prolonged period of below-average precipitation relative to historical norms and often serves as the initial trigger for other drought types. Agricultural drought occurs when soil moisture becomes insufficient to support crop growth, reducing agricultural productivity. Hydrological drought refers to declines in surface and subsurface water supplies, including reduced river flows, lower reservoir levels, and depleted groundwater reserves. 

* Corresponding author. 

_E-mail address:_ gx_hwswj@163.com (X. Guo). 

https://doi.org/10.1016/j.agwat.2026.110128 

Received 21 August 2025; Received in revised form 19 December 2025; Accepted 4 January 2026 

Available online 23 January 2026 

0378-3774/© 2026 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY-NC license ( http://creativecommons.org/licenses/bync/4.0/ ). 

_Agricultural Water Management 325 (2026) 110128_ 

_Z. Xu et al._ 

Socio-economic drought arises when water shortages create a significant imbalance between supply and demand, disrupting economic activities and affecting community well-being (Ding et al., 2021a; Gevaert et al., 2018; Li et al., 2018). Drought propagation refers to the transition from an initial precipitation deficit (meteorological drought) through various components of the hydrological cycle, ultimately leading to other forms of drought, such as agricultural and hydrological droughts (Apurv et al., 2017; Das et al., 2022; Fang et al., 2020). Therefore, understanding the propagation process is essential, as it reveals the relationships between meteorological drought and the subsequent agricultural and hydrological droughts. This understanding is crucial for developing early-warning systems and adaptive management strategies to mitigate the adverse effects of agricultural and hydrological droughts (Das et al., 2022; Ding et al., 2021a; Ho et al., 2021; Wang et al., 2023b). 

Propagation time is a key parameter for assessing drought propagation, as it represents the lag between the initial atmospheric conditions and the eventual soil moisture deficits that affect crop growth and the water availability deficit that impacts water withdrawal (Bhardwaj et al., 2020; Chen et al., 2020; Li et al., 2022b; Wu et al., 2021b). Numerous studies have attempted to characterize propagation time through correlation analysis (e.g., Barker et al., 2016; Ding et al., 2021a; Xu et al., 2021a). In this approach, the correlation between agricultural (or hydrological) drought indicators at a single timescale and meteorological drought indicators at different timescales is calculated. The time scale at which the meteorological drought indicator exhibits the highest correlation with the agricultural (or hydrological) drought indicator is then considered the propagation time (Barker et al., 2016; Fang et al., 2020). The rationale behind using correlation analysis lies in its ability to reveal the statistical relationship between meteorological variables (e.g., precipitation, temperature) and hydrological responses (e.g., soil moisture, streamflow). This approach has provided valuable insights into drought propagation times across different climatic and geographic regions (Ding et al., 2021a; Gevaert et al., 2018). However, significant limitations exist when using a correlation-based approach to assess drought propagation (Gupta and Karthikeyan, 2024; Ho et al., 2021). One of the most critical drawbacks is that the propagation time from meteorological to agricultural and hydrological droughts varies temporally across different drought events, whereas the correlation-based approach, which often produces a single propagation time, cannot effectively capture this variability (Bhardwaj et al., 2020; Brunner and Chartier-Rescan, 2024; Li et al., 2018; Sattar et al., 2019). Moreover, the entire time series of drought indices includes both drought and non-drought periods, which may introduce uncertainties in the estimation of propagation time (Li et al., 2022b; Raposo et al., 2023; Zhang et al., 2023, 2022). 

Given these limitations, determining propagation time based on identified drought events rather than directly using drought indices is more appropriate (Chen et al., 2024; Das et al., 2022). Some studies have attempted to investigate drought propagation at the event level (e.g., Bevacqua et al., 2021; Bhardwaj et al., 2020; Ho et al., 2021; Sattar et al., 2019; Wang et al., 2023b). In this case, propagation time is estimated as the time lag between the onset (or peak) of meteorological drought events and the subsequent hydrological or agricultural drought events, typically identified by matching different types of drought events (Das et al., 2022; Raposo et al., 2023; Zhang et al., 2022). Additionally, variations in drought properties (e.g., drought duration and intensity) during propagation can also be analyzed using this method (Li et al., 2018; Zhou et al., 2021). Propagation time is a dynamic parameter attributed to each propagated drought event. However, the factors that govern propagation time at the event level remain largely unexplored. Moreover, to the best of our knowledge, few studies have explored the possibility of predicting propagation time using the primary factors influencing drought propagation, which is critically important in the context of climate change and the increasing demand for drought early warning systems. Another limitation of previous event-level studies is the insufficient attention paid to the evolution of drought characteristics 

across different stages. Most of these studies have primarily focused on variations in drought properties over the entire event, often overlooking the distinctions between the development and recovery stages. This may lead to an incomplete understanding of the full life cycle of drought propagation. 

In response to the limitations identified in existing research, this study aims to investigate the propagation from meteorological drought to agricultural drought at the event scale. Specifically, it focuses on variations in drought characteristics (duration and intensity) across different drought stages during propagation, as well as on the quantification of propagation time and the identification of its key influencing factors. The primary objectives of this study are to: (1) identify the main propagation types from meteorological to agricultural drought at the event scale; (2) investigate whether variations in drought characteristics during propagation differ across drought stages; and (3) identify the dominant factors influencing propagation time and develop a predictive model for propagation time using these identified factors. The results of this study are expected to enhance knowledge on drought propagation and contribute to the development of more accurate drought forecasting models. 

### **2. Materials and methods** 

### _2.1. Study area_ 

The Yellow River Basin (YRB) is the second-longest river basin in China, covering approximately 765,000 km² and stretching about 5464 km in length. It traverses nine provinces and autonomous regions, including Qinghai, Sichuan, Gansu, Ningxia, Inner Mongolia, Shaanxi, Shanxi, Henan, and Shandong. The basin exhibits pronounced spatial heterogeneity in topography, climate, and land use. As the cradle of Chinese civilization and a key economic and agricultural region, the YRB plays a vital role in ensuring national water security and food production. However, the YRB is also among the most water-stressed regions in China, frequently experiencing meteorological and agricultural droughts due to uneven precipitation distribution (Huang et al., 2025). These conditions make the basin a critical and representative area for studying drought propagation. To comprehensively analyze spatial differences in drought propagation, the YRB was divided into eight secondary sub-basins, as illustrated in Fig. 1. Both annual precipitation and temperature vary significantly across the sub-basins. Regions III and IV receive the least precipitation, with an annual average of less than 300 mm. In contrast, the annual precipitation in Regions I, II, and V is around 400 mm, while Regions VI, VII, and VIII experience the highest precipitation, exceeding 500 mm. The average annual temperature gradually increases from Region I to Region VIII, ranging from –1.0<sup>◦</sup> C to 14.3<sup>◦</sup> C (Li et al., 2024a). 

### _2.2. Datasets_ 

Precipitation, soil moisture, and potential evapotranspiration data for the period 1980–2024 were obtained from ERA5-Land (https://cds. climate.copernicus.eu/) (Munoz-Sabater et al., 2021˜ ), which is the land component of the fifth-generation reanalysis product from the European Centre for Medium-Range Weather Forecasts (ECMWF). ERA5-Land provides data at a spatial resolution of 0.1<sup>◦</sup> × 0.1<sup>◦</sup> and a temporal resolution of 1 h. Its high spatial and temporal resolution allows for more accurate characterization of land surface dynamics and extreme events such as droughts at both regional and global scales (Hirschi et al., 2025; Mei et al., 2025). All hourly data were aggregated to a daily resolution for subsequent analysis. Following previous studies, the volumetric water content of the 0–100 cm soil layer was used to represent root-zone soil moisture (Hirschi et al., 2025; Hong et al., 2024; Wu et al., 2024; Zhang et al., 2024), as this depth is closely associated with crop growth (Ding et al., 2021a). It was calculated as a depth-weighted average of the volumetric water content across three ERA5-Land layers (0–7, 7–28, and 

2 

_Agricultural Water Management 325 (2026) 110128_ 

_Z. Xu et al.                                                                                                                                                                                                                                       Agricultural Water Management_ 



**Fig. 1.** The location of the Yellow River Basin (YRB) and its eight sub-regions. 

28–100 cm). This approach provides a more realistic representation of integrated root-zone water storage by accounting for the relative contributions of different soil layers to plant-available moisture (Fan et al., 2022). The weighted formula is expressed as follows: 



where _SM_ 0− 100 denotes the root-zone soil moisture obtained from the weighted average, and _SM_ 0− 7, _SM_ 7− 28, and _SM_ 28− 100 represent the ERA5-Land soil moisture at depths of 0–7 cm, 7–28 cm, and 28–100 cm, respectively. The weighting coefficients were determined according to the thickness of each layer relative to the total 0–100 cm depth. 

The Normalized Difference Vegetation Index (NDVI) data were obtained from the National Earth System Science Data Center, National Science & Technology Infrastructure of China (http://www.geodata.cn), with a spatial resolution of 8 km and a monthly temporal resolution. The NDVI data were resampled to a spatial resolution of 0.10<sup>◦</sup> to ensure consistency with the other datasets used in this study. 

### _2.3. Methods_ 

### _2.3.1. Standardized drought indices_ 

In this study, the SPEI (Vicente-Serrano et al., 2010) and SSMI (Hao and AghaKouchak, 2013) were used to characterize meteorological and agricultural drought, respectively. The calculation procedure for the SPEI follows a process similar to that of the standardized precipitation index (SPI) and is summarized as follows: (1) determining the accumulation of water deficit D over different time scales, where the water deficit is the difference between precipitation and potential evapotranspiration; (2) fitting the water deficit series to an appropriate probability distribution function. To avoid assumptions about the parametric distribution and reduce the computational burden of fitting parameter distributions, the GPP (Gringorten plotting position) algorithm (Gringorten, 1963) is employed in this study to calculate the cumulative probability of the water deficit (Eq. (2)). The GPP algorithm has been widely applied in previous drought studies (e.g., Ho et al., 2021; Wang et al., 2023a; Wu et al., 2021a); (3) converting the cumulative probability into a standard variable using a standardized normal distribution via an equal probability transformation, which represents the SPEI. 



where _F_ is the cumulative probability, _i_ is the rank, and _n_ is the sample size. 

The SSMI, calculated from soil moisture series, follows the same calculation procedure as the SPEI. To estimate drought propagation time at a finer temporal resolution, the method proposed by Xu et al. (2023b) 

was used to compute daily updated SPEI and SSMI, using 30-day cumulative units with a 1-day sliding window. The 30-day time scale adopted in this study is comparable to the one-month accumulation period widely used in previous studies for drought event identification (e.g., Das et al., 2022; Xiong et al., 2025), ensuring methodological consistency and facilitating comparison with existing research. Moreover, compared with longer accumulation periods, the 30-day SSMI and SPEI can capture a larger number of drought events (Vicente-Serrano et al., 2010; Wu et al., 2021b; Xu et al., 2025a), thereby providing a richer sample set for the XGBoost algorithm used to identify the factors influencing propagation time. Specifically, for each day, the 30-day accumulated water deficit and soil moisture were first calculated. Then, the cumulative probabilities of the accumulated water deficit and soil moisture for each specific day from 1980 to 2024 were computed using Eq. (2). Finally, these cumulative probabilities were transformed into standard normal distributions to obtain the daily-updated SPEI and SSMI. A more detailed calculation procedure can be found in Xu et al. (2023b). 

### _2.3.2. Identification of drought events_ 

The widely used run theory was applied to identify meteorological and agricultural drought events based on a threshold value of − 0.5. In drought research, there is a broad consensus that standardized drought index values below − 0.5 indicate the onset of drought, and this threshold has been widely used in event-based drought propagation studies (e.g., Lin et al., 2023a; Lin et al., 2023b; Liu et al., 2023; Xu et al., 2025a; Zhou et al., 2021). In this study, drought events were identified 

**Table 1** 

Thresholds and temporal windows used for drought event identification and matching. 

|Component|Parameter|Threshold<br>Value|Description|
|---|---|---|---|
|Drought<br>identification|Drought<br>threshold|−0.50|Widely adopted threshold for<br>identifying drought onset using<br>SPEI or SSMI<br>l|
||Minimum<br>duration|20 days|To include flash drought events|
||Event<br>pooling|5 days|Merge two consecutive drought<br>events if their interval is≤5<br>days|
|Event<br>matching|Lead<br>window|−10 days|Allows agricultural drought to<br>start up to 10 days before<br>meteorological drought onset<br>(criterion 1, with time overlap)|
||Lag window|10 days|Allows agricultural drought to<br>start up to 10 days after<br>meteorological drought end<br>(criterion 2, without time<br>overlap)|



3 

_Agricultural Water Management 325 (2026) 110128_ 

_Z. Xu et al._ 

using a minimum duration threshold of 20 days (Table 1). This criterion is slightly different from previous drought propagation studies based on daily updated indices, which commonly used 30 days as the minimum duration (Ho et al., 2021; Xu et al., 2023b). The shorter 20-day threshold was adopted in this study to account for flash droughts (Yuan et al., 2023). Additionally, two consecutive drought events were merged into a single event if their interval was less than 5 days, following the recommendations of Tallaksen et al. (1997) and Fleig et al. (2006), as well as subsequent studies (Lin et al., 2023b; Tu et al., 2019; Xu et al., 2023b). Drought duration was defined as the number of consecutive days with SPEI or SSMI values below − 0.50, while drought intensity was defined as the average SPEI or SSMI value during the drought event. 

Moreover, meteorological and agricultural drought events were categorized into development, persistence, and recovery stages by refining the method proposed by Xu et al. (2023a). This classification allows for a more detailed assessment of changes in drought characteristics throughout different stages of drought propagation. Specifically, the drought development duration (DDD) refers to the period from the onset of a drought event to the first occurrence of its maximum intensity (MI). In some cases, such as Drought Event 2 in Fig. 2, the maximum intensity may occur multiple times. Therefore, the drought persistence duration (DPD) is defined as the time interval between the first and last occurrences of the maximum intensity. The drought recovery duration (DRD) is defined as the period from the last maximum intensity to the first day after the event when the SPEI or SSMI value rises above − 0.5. Correspondingly, the drought development intensity (DDI), persistence intensity (DPI), and recovery intensity (DRI) are defined as the average SPEI or SSMI values during the development, persistence, and recovery stages of a drought event, respectively. The drought development speed (DDS) refers to the rate of variation in SPEI or SSMI during the drought development stage, defined as the ratio of the difference between the SPEI or SSMI values at maximum intensity and at the onset of drought to the development duration. The drought recovery speed (DRS) refers to the rate of variation in SPEI or SSMI during the drought recovery stage, defined as the ratio of the difference between the SPEI or SSMI values on the last day of drought recovery and at maximum intensity to the recovery duration. However, the maximum intensity may occur only once in some drought events, such as Drought Event 1 in Fig. 2. In such cases, the DPD and DPI are considered to be 0. 

### _2.3.3. Matching of agricultural and meteorological drought events_ 

In this study, agricultural and meteorological drought events were matched if they satisfied one of the following two criteria: (1) the two types of drought events overlap in time, with the onset of the agricultural drought event occurring no more than 10 days before the start of the meteorological drought event; (2) there is no temporal overlap between the two types of drought events, but the start of the agricultural drought event occurs within 10 days after the end of the meteorological drought event (Table 1). Flash droughts, characterized by their rapid onset, are typically identified by a sudden and sharp decline in soil 

moisture within just a few days. Usually driven by abnormally high temperatures and significant precipitation deficits, they can serve as the initial phase of traditional long-term droughts (Yuan et al., 2023). Since soil moisture is also a key indicator of agricultural drought, flash droughts may cause agricultural drought to emerge earlier than those associated with conventional, slower-developing droughts. Additionally, previous studies have found that meteorological droughts may not always precede other drought types (Ho et al., 2021). Therefore, we assumed that agricultural drought events are matched with meteorological drought events if the former occurs within 10 days before the latter (criterion (1)), which is similar to the approach of Bevacqua et al. (2021), although several previous studies have assumed that meteorological droughts precede other drought types (Chen et al., 2024). 

ased on the matched drought events, the propagation from meteorological to agricultural drought was classified into four categories according to the number of meteorological and agricultural drought events involved within the defined matching window (Chen et al., 2024; Wu et al., 2022). As illustrated in Fig. A1 of the Supplementary Material, the one-to-one type refers to cases where a single meteorological drought (MD1) and one agricultural drought (AD1) occur within the matching window. The one-to-many type occurs when a single meteorological drought (MD2) triggers multiple agricultural drought events (AD2 and AD3) within the window. The many-to-one type represents situations where several consecutive meteorological droughts (MD3 and MD4) jointly lead to a single, prolonged agricultural drought (AD4). Finally, the many-to-many type reflects a more complex relationship, where multiple meteorological droughts (MD5 and MD6) and multiple agricultural droughts (AD5 and AD6) partially overlap within the defined matching window; AD5 overlaps with both MD5 and MD6, whereas AD6 primarily corresponds to MD6. 

### _2.3.4. Drought propagation characteristics_ 

Drought propagation characteristics, including propagation time (PT), propagation rate (PR), drought intensity propagation index (DIPI), and drought duration propagation index (DDPI), can be calculated based on the matched drought events. The propagation time is defined as the time interval between the onset of the meteorological drought and the onset of the corresponding agricultural drought (Sattar et al., 2019). For the one-to-one type, the propagation time is the interval between the onset of the meteorological drought and the agricultural drought. For the one-to-many type, it is calculated using the onset of the meteorological drought and the onset of the first agricultural drought. For the many-to-one type, it is calculated using the earliest meteorological drought and the agricultural drought. For the many-to-many type, it is calculated using the first meteorological drought and the first agricultural drought. The average propagation time for each grid is then calculated as the mean propagation time of all matched drought events. 





**Fig. 2.** Schematic diagram of drought stage classification. DDD, DPD, and DRD denote drought development, persistence, and recovery durations, respectively; MI indicates maximum intensity. 

4 

_Agricultural Water Management 325 (2026) 110128_ 

_Z. Xu et al.                                                                                                                                                                                                                                       Agricultural Water Management_ 

Where _n_ denotes the number of matched drought events, and _Adst,i_ and _Mdst,i_ represent the start times for the _i_ -th matched agricultural and meteorological drought events, respectively. 

Drought propagation rate is a significant index for characterizing the sensitivity of agricultural drought events to meteorological drought events (Xu et al., 2023b) and can be calculated as follows: 



Where _Nm_ and _Nt_ represent the number of matched and total meteorological drought events, respectively. 

The drought intensity propagation index and the drought duration propagation index were calculated to quantitatively characterize changes in drought intensity and duration during the propagation process (Chen et al., 2024; Li et al., 2022a). The DIPI and DDPI are defined as the ratio of the mean intensity of all matched meteorological droughts to that of agricultural droughts, and the ratio of the mean duration of all matched meteorological droughts to that of agricultural droughts, respectively, and are calculated as follows: 





Where Ii and Ij represent the intensity of matched meteorological and agricultural drought events, respectively; Di and Dj represent the duration of matched meteorological and agricultural drought events, respectively; and nm and na represent the number of matched meteorological and agricultural drought events, respectively. In addition to the DIPI and DDPI for the entire drought events, DIPI and DDPI were also estimated for the development, persistence, and recovery stages. 

_2.3.5. Identification of potential factors influencing drought propagation time_ 

In this study, the eXtreme Gradient Boosting (XGBoost) algorithm was employed to quantify the relative importance of potential factors influencing drought propagation time, thereby identifying the dominant drivers. XGBoost was chosen because it has been successfully applied in recent drought-related studies to identify key influencing factors and model complex nonlinear relationships (Qian et al., 2025; Xu et al., 2025b; You et al., 2025). Developed by Chen and Guestrin (2016), XGBoost is particularly notable for its capability to evaluate feature importance, which is essential for improving model interpretability. By quantifying the contributions of individual features to predictive performance, XGBoost facilitates the identification of key drivers influencing the predictive target. Specifically, relative importance is determined by calculating the loss reduction (gain) contributed by each feature during node splitting in decision tree construction. By default, the XGBoost algorithm uses feature gain as the importance score, aggregating each feature's gain across all trees, averaging, and normalizing these values to obtain relative importance scores. These importance scores intuitively represent each feature's impact on the model's predictive outcomes. In this study, the relative importance of factors influencing drought propagation time was assessed using Python's xgboost package through the feature_importance() function. 

This study evaluated the influence of seven potential factors on drought propagation time. The first factor is the initial soil moisture condition (IC), represented by the SSMI value on the start date of the matched meteorological drought event. Based on this definition, a 

higher initial condition value indicates wetter soil conditions at the onset of a meteorological drought, which may be associated with a longer propagation time. The second and third factors correspond to two of the three key meteorological drought development characteristics: drought development duration and drought development intensity. Drought development speed was excluded from this evaluation, as it somewhat overlaps with drought development duration. A longer meteorological drought development duration indicates slower drought progression, during which gradual soil moisture depletion may postpone the onset of agricultural drought in response to meteorological drought. Drought development intensity reflects the extent of precipitation deficit. Lower values indicate more severe meteorological droughts, which are more likely to trigger agricultural droughts. The fourth factor is the day of the year (DOY) on which the meteorological drought occurs, representing the number of days accumulated from January 1 of that year. The speed of the hydrological cycle varies throughout the year. A faster hydrological cycle accelerates soil moisture responses to meteorological anomalies, potentially shortening the propagation time from meteorological to agricultural drought. Additionally, three anomaly percentage variables were selected, namely precipitation anomaly percentage (Pre_AP) and temperature anomaly percentage (Tem_AP) during the meteorological drought development stage, and NDVI anomaly percentage (NDVI_AP) for the month in which the meteorological drought occurred. These variables were included to evaluate the influence of meteorological conditions and vegetation status on drought propagation time. To increase the sample size of matched drought events, events in the target grid i and its nearest four grids were included when applying the XGBoost algorithm to identify the dominant factor influencing drought propagation time in grid i. The relative importance of each potential factor for grid i was estimated only if at least 50 drought events were matched in these five grids. 

Based on the identified key factors influencing drought propagation time, a predictive model was developed for each subregion using the XGBoost algorithm. When drought events are randomly divided into training and validation sets, temporal dependencies and spatial autocorrelation among events may cause information leakage. To minimize this issue and evaluate the model’s generalization capability across heterogeneous environments, a leave-one-region-out cross-validation strategy was adopted. Specifically, based on the subregional division of the YRB, in each iteration, drought events from one entire subregion were used as the validation set, while events from the remaining seven subregions were combined to form the training set. For instance, in the first iteration, all grid-scale drought events within Region I were used for validation, and data from Regions II–VIII were used for training. In the second iteration, drought events from Region II served as the validation set, and those from Regions I and III–VIII were used for training. This procedure was repeated until each of the eight subregions had been used once as the validation set. This region-based cross-validation design ensures that the model is tested on independent spatial domains, providing a more rigorous and realistic assessment of its predictive performance. Each model uses the dominant influencing factors as predictors and propagation time as the predictand. The root-meansquare error (RMSE) and correlation coefficient (CC) are used to evaluate the performance of the predictive model: 





Where _Prei_ and _Obsi_ represent the predicted and observed drought propagation time, respectively; _Pre_ and _Obs_ represent the mean values of 

5 

_Agricultural Water Management 325 (2026) 110128_ 

_Z. Xu et al._ 

predicted and observed drought propagation time, respectively; and _n_ represents the sample size. 

### **3. Results** 

### _3.1. Matched agricultural and meteorological drought events_ 

The identification and matching results of agricultural and meteorological drought events are presented in Fig. 3. Compared to meteorological drought, agricultural drought events occur less frequently, with average occurrence frequencies of 82.6 for meteorological drought and 38.8 for agricultural drought across the YRB. Spatially, the frequency of agricultural drought events is significantly more heterogeneous than that of meteorological drought events. Specifically, the frequency of agricultural drought events in Regions I and II (54.0 and 51.8 on average) is higher than in other regions, whereas Region IV has the lowest frequency, averaging 28.4. As shown in Fig. 3(c), the average propagation rate of meteorological drought events in the YRB is 49.5 %, indicating that approximately half of the meteorological drought events transition into agricultural drought events. The spatial distribution of the propagation rate generally corresponds to the frequency of agricultural drought events, meaning regions with more agricultural drought events tend to have higher propagation rates. Specifically, the 

average propagation rate in Regions III and IV is approximately 37.0 %, which is lower than that in other subregions, where it ranges from 45.9 % to 57.7 % on average. 

We further identified the dominant propagation type from meteorological to agricultural drought events. As shown in Fig. 4, the matched meteorological and agricultural drought events predominantly exhibit a one-to-one relationship, accounting for 67.0 % of all propagation types. This is followed by the many-to-one type, with an average proportion of 31.9 %, while the one-to-many and many-to-many types are negligible. The percentage of the one-to-one type in Region I (77.9 %) is the highest among all subregions, followed by Regions II and VIII, with average values of 75.5 % and 72.8 %, respectively. The percentage in the remaining subregions ranges from 58.5 % in Region VII to 65.6 % in Region VI. In contrast, the percentage of the many-to-one type in Regions I, II, and VIII is lower than in the other subregions, especially in Region I, where it averages approximately 19.5 %. However, this type accounts for over 30.0 % in the remaining five subregions. 

### _3.2. Variations in drought characteristics during drought propagation_ 

Variations in drought characteristics during propagation were further examined. Fig. 5 presents the spatial distribution of the average total duration, development duration, persistence duration, and 



**Fig. 3.** Spatial distribution of the occurrence frequency of meteorological and agricultural droughts, as well as the drought propagation rate. 

6 

_Agricultural Water Management 325 (2026) 110128_ 

_Z. Xu et al._ 



**Fig. 4.** Spatial distribution of the percentage of each drought propagation type from meteorological to agricultural drought events. 

recovery duration for the matched meteorological and agricultural drought events. The average meteorological drought duration in the YRB is 51.1 days, significantly shorter than the agricultural drought duration, which averages 145.3 days. Similarly, the development, persistence, and recovery durations of meteorological droughts are all shorter than those of agricultural droughts. Moreover, the drought development duration is consistently longer than the persistence and recovery durations for both meteorological and agricultural drought events. In contrast, the recovery duration is longer than the persistence duration, indicating that drought recovery generally takes longer than the persistence stage but is still shorter than the development stage. In terms of spatial distribution, the total duration, development duration, persistence duration, and recovery duration of agricultural drought events exhibit greater spatial heterogeneity than those of meteorological drought events. These four duration-related characteristics of agricultural droughts are shortest in Regions I and II. For example, the average agricultural drought development durations in Regions I and II are 34.9 and 46.2 days, respectively, whereas in Regions III to VIII, they range from 58.9 days (Region VI) to 92.5 days (Region IV). 

Moreover, the spatial distribution of drought duration propagation indices is presented in Fig. 6 (a1-d1). The DDPI exceeds 1.00 in nearly all grids, accounting for 99.7 %, 98.2 %, 94.3 %, and 98.2 % of the total grids during the entire drought stage, and the development, persistence, and recovery stages, respectively. The average DDPI for these four stages is 2.86, 3.14, 3.10, and 2.42, respectively, indicating that agricultural drought durations are, on average, more than twice as long as the corresponding meteorological drought durations. Spatially, higher DDPI values are mainly observed in areas with longer agricultural drought durations. Accordingly, the average DDPI values in Region I for the entire drought stage, development stage, persistence stage, and recovery stage are 1.82, 1.74, 1.68, and 2.03, respectively, which are substantially lower than those in other regions, particularly compared to Regions III and IV. 

The agricultural drought intensity for the entire drought stage, development stage, persistence stage, and recovery stage is weaker than the corresponding meteorological drought intensity (Fig. 6 and Fig. 7). For instance, the average meteorological and agricultural drought intensities for the entire drought stage in the YRB are − 1.24 and − 0.97, 

respectively. The persistence intensity of both meteorological and agricultural droughts is more severe than the development intensity, which in turn is slightly more severe than the recovery intensity. For example, the average intensities during the development, persistence, and recovery stages of agricultural drought events are –0.90, –1.25, and –0.86, respectively (Fig. 7). The average DIPI values for the entire drought stage, development stage, persistence stage, and recovery stage are 0.78, 0.78, 0.84 and 0.85, respectively (Fig. 6). The spatial heterogeneity of agricultural drought intensity is slightly greater than that of meteorological drought intensity. Specifically, the intensity of agricultural drought events in Regions I and II during the entire drought stage, as well as during the development, persistence, and recovery stages, is more severe than in other regions. Consequently, the DIPI values in Regions I and II are higher than those in other regions, suggesting that drought intensity diminishes less significantly in these regions during drought propagation. However, drought intensity diminishes more significantly in Region III during drought propagation, with average DIPI values ranging from 0.74 to 0.81. Similar to the findings of Li et al. (2022a), there was a negative correlation between DDPI and DIPI, implying that the longer the drought duration extends, the more pronounced the weakening of drought intensity during propagation. 

The drought development speed represents the rate of decrease in the drought index value from the onset to the peak of the drought, while the recovery speed indicates the rate of increase in the drought index value from the peak to the end of the drought. The spatial distribution of drought development speed and recovery speed for the matched meteorological and agricultural droughts is presented in Fig. 8. The change in the drought index during the development stage is slower than during the recovery stage, suggesting that drought recovery is typically faster, likely due to intense precipitation events in the recovery stage (Yang et al., 2017). Moreover, both the development and recovery speeds of meteorological droughts are significantly faster than those of agricultural droughts. For example, the drought recovery speeds for meteorological and agricultural drought events are 0.14 and 0.04, respectively, possibly due to the longer recovery duration of agricultural droughts. Spatially, the recovery speed of meteorological droughts in the middle and lower YRB (Regions V to VIII) is slightly faster than in other regions. For example, the average recovery speed for meteorological droughts is 

7 

_Agricultural Water Management 325 (2026) 110128_ 

_Z. Xu et al.                                                                                                                                                                                                                                       Agricultural Water Management_ 



**Fig. 5.** Spatial distribution of average drought duration, development duration, persistence duration, and recovery duration (from top to bottom) for the matched meteorological (a1–d1) and agricultural drought events (a2–d2). 

0.15 in Region V, compared to 0.12 in Region I. 

### _3.3. Drought propagation time and its driving factors_ 

### _3.3.1. Propagation time from meteorological to agricultural drought events_ 

Fig. 9 presents the average propagation time from meteorological to agricultural drought events for each grid. On average, agricultural drought events lag meteorological drought events by 18.1 days in the YRB. Spatially, the average propagation time in the northwestern YRB and Region VIII is slightly lower than in other regions, while that in the central YRB is slightly higher. Nevertheless, the overall differences among the eight sub-regions are relatively small, with average values ranging from 15.3 days in Region VIII to 19.9 days in Region VI. This spatial pattern is similar to the results of Zhang et al. (2021a), although 

the estimated propagation times in the two studies differ significantly due to variations in the drought propagation time calculation method, drought indices, datasets, and other factors. Several previous studies have also found that the estimated propagation time varies depending on the methods used, such as run theory, correlation analysis, and others (Bevacqua et al., 2021; Das et al., 2022; Wu et al., 2021b; Zhang et al., 2023). Moreover, the propagation time estimated in this study is shorter than that of Zhang et al. (2021a), which aligns with Wu et al. (2021b) and Bevacqua et al. (2021). 

### _3.3.2. Main factors affecting drought propagation time_ 

Before identifying the main factors influencing drought propagation time using the XGBoost algorithm, a correlation analysis was performed to assess the relationship between drought propagation time and each 

8 

_Agricultural Water Management 325 (2026) 110128_ 

_Z. Xu et al._ 



**Fig. 6.** Spatial distributions of drought duration (left) and intensity (right) propagation indices for the entire drought stage, as well as the development, persistence, and recovery stages (from top to bottom). 

potential factor across four typical grids (Fig. 1). As shown in Fig. 10, the correlation between drought propagation time and initial soil moisture conditions vary significantly across grids (Fig. 10 (a1)-(a4)). For example, the correlation coefficient between initial soil moisture conditions and propagation time is 0.53 for the typical Grid 1 (Fig. 10 (a1)), whereas it is 0.79 for the typical Grid 2 (Fig. 10 (a2)). These differences are also observed in the other factors. The correlation coefficient between initial soil moisture conditions and propagation time is higher than that of the other factors. In typical Grids 1 and 2, the correlation coefficient between drought development duration and propagation time is the second strongest, following that of initial soil moisture conditions. In contrast, in typical Grid 3, the day of the year when meteorological drought occurs shows the second-highest correlation with propagation time, also after initial soil moisture conditions. These 

findings highlight that initial soil moisture conditions are the primary driver of drought propagation time across the basin, whereas the influence of other factors exhibits notable spatial variability. Moreover, it should be noted that a positive correlation coefficient between initial soil moisture conditions and propagation time was found across the four typical grids. This suggests that higher soil moisture at the onset of meteorological drought tends to prolong the agricultural drought's response. Although the overall correlation between the occurrence time of meteorological drought and propagation time is weak in some grids, certain locations, such as typical Grid 1 (Fig. 10 (d1)), exhibit longer propagation times during winter compared to other seasons. This suggests that the occurrence time of meteorological drought may be a factor influencing drought propagation time in some regions, and simple correlation analysis may not always effectively identify its impact. 

9 

_Agricultural Water Management 325 (2026) 110128_ 

_Z. Xu et al.                                                                                                                                                                                                                                       Agricultural Water Management_ 



**Fig. 7.** Spatial distribution of average drought intensity, development intensity, persistence intensity, and recovery intensity (from top to bottom) for the matched meteorological (a1–d1) and agricultural drought events (a2–d2). 

However, the correlation coefficients between propagation time and precipitation anomaly percentage (Fig. 10 (e1)-(e4)), temperature anomaly percentage (Fig. 10 (f1)-(f4)), and NDVI anomaly percentage (Fig. 10 (g1)-(g4)) were substantially lower. Moreover, both positive and negative correlations were observed for all variables except temperature anomaly percentage, suggesting that their effects on propagation time may be more complex or relatively weak. 

Fig. 11 shows the spatial distribution of the relative importance of seven potential factors on propagation time. Initial soil moisture conditions play a dominant role in determining the propagation time from meteorological to agricultural drought, with an average relative importance of 0.32. This is followed by the day of the year when meteorological drought occurs and drought development duration, with average relative importance values of 0.27 and 0.18, respectively. The 

relative importance of temperature anomaly percentage during the meteorological drought development stage is 0.10, which is higher than that of the other three potential influencing factors. Spatially, the relative importance of initial soil moisture conditions gradually increases from the upper reaches of the YRB (Regions I to IV) to the middle and lower reaches (Regions V to VIII). The average value in Region I (0.16) is lower than that in the other subregions, ranging from 0.25 in Region II to 0.43 in Region VIII. In contrast, the relative importance of the day of the year when meteorological drought occurs generally decreases from Regions I to VIII. The average relative importance of this factor is highest in Region I (0.46) and lowest in Region VII (0.17). The regional differences in the average relative importance of drought development duration and temperature anomaly percentage are relatively small across the eight subregions, ranging from 0.13 (Region III) to 0.27 

10 

_Agricultural Water Management 325 (2026) 110128_ 



**Fig. 8.** Spatial distribution of the average drought development speed and recovery speed for the matched meteorological (a1–b1) and agricultural drought events (a2–b2). 



**Fig. 9.** Average propagation time from meteorological to agricultural drought events. 

(Region VII) for development duration, and from 0.04 (Region I) to 0.13 (Region II) for temperature anomaly percentage. 

To further explore the underlying reasons for the results in Fig. 11, propagation time was grouped by initial soil moisture conditions, meteorological drought development duration, month of meteorological drought occurrence, and temperature anomaly percentage (Fig. 12). For better comparison, only the results for the entire YRB and four of its eight sub-regions are presented in Fig. 12, while the results for the other sub-regions are provided in Fig. A2 in the Supplementary Material. A 

significant positive correlation between initial soil moisture conditions and propagation time was observed (Fig. 12 (a)), indicating that higher soil moisture at the onset of meteorological drought tends to result in a longer propagation time from meteorological to agricultural drought. Similarly, a positive correlation was also found between drought development duration and propagation time (Fig. 12 (b)), suggesting that propagation time generally increases with the meteorological drought development duration. However, the correlation between development duration and propagation time is weaker than that 

11 

_Agricultural Water Management 325 (2026) 110128_ 



**Fig. 10.** Scatterplot of propagation time versus potential influencing factors (from top to bottom) across four typical grids (from left to right, corresponding to Grid 1 to Grid 4) (* denotes the correlation coefficient between propagation time and the evaluated potential influencing factor at the 0.05 significance level). N denotes the number of samples. 

12 

_Agricultural Water Management 325 (2026) 110128_ 

_Z. Xu et al.                                                                                                                                                                                                                                       Agricultural Water Management_ 



**Fig. 11.** Relative importance of each potential factor on drought propagation time. Only grids with a sufficient number of matched drought events, as defined by the predefined criteria, are colored. 

between initial soil moisture conditions and propagation time, which is consistent with the results based on relative importance derived from the XGBoost method. As shown in Fig. 12 (c), clear seasonal variations in propagation time are observed. Specifically, propagation time from June to September is significantly shorter than in the winter months. These results indicate a nonlinear relationship between drought propagation time and the timing of meteorological drought onset. This nonlinear pattern is effectively captured by the XGBoost method, which may explain why the timing of meteorological drought occurrence is identified as one of the main factors influencing propagation time. The relationship between propagation time and temperature anomaly percentage is less pronounced than that of the three factors discussed above (Fig. 12 (d)). However, in several sub-regions, the overall propagation time under positive temperature anomalies is slightly shorter than that under negative temperature anomalies, which may be attributed to higher temperatures enhancing evapotranspiration and thereby accelerating soil moisture depletion. 

_3.3.3. Performance of the predictive model for drought propagation time_ 

According to the results in Section 3.3.2, we established a predictive model for drought propagation time in each subregion using the XGBoost algorithm, with initial soil moisture conditions, meteorological drought development duration, timing of meteorological drought occurrence, and temperature anomaly percentage as predictor variables. As shown in Table 2 and Fig. 13, the CC between the predicted and observed propagation time during the training period ranges from 0.86 to 0.89, with an average of 0.87. The RMSE varies from 8.6 days in Region III to 10.0 days in Region VI. During the validation period, model performance shows a slight decline but remains highly accurate, with CC values ranging from 0.77 to 0.84 and RMSE values from 8.6 to 13.6 days, indicating that the predictive models exhibit strong robustness and generalization capability. The models perform significantly better in Regions VII and VIII than in other regions. As shown in Fig. 13, most points are clustered near the 1:1 line, with the fitted slope of the linear regression ranging from 0.82 in Region II to 1.18 in Region III. A possible reason for the relatively poorer performance in predicting longer propagation times is the limited number of samples with longer 

13 

_Agricultural Water Management 325 (2026) 110128_ 

_Z. Xu et al._ 



**Fig. 12.** Box plots of propagation time across the YRB and four representative sub-regions (Regions I, III, V, and VII), grouped by initial soil moisture conditions, drought development duration, month of drought occurrence, and temperature anomaly percentage. Note that outliers have been excluded to facilitate clearer comparison. 

propagation times, indicating that the models may not have been sufficiently trained to accurately predict these cases. 

### **4. Discussion** 

In this study, the propagation time from meteorological to 

agricultural droughts was investigated using an event-based approach, rather than traditional correlation analysis based directly on standardized drought indices. The event-based method, which relies on matched drought events with causal relationships, has the advantage of determining the propagation time for each pair of events (Chen et al., 2024). This is essential, as drought propagation characteristics can vary over 

14 

_Agricultural Water Management 325 (2026) 110128_ 

_Z. Xu et al.                                                                                                                                                                                                                                       Agricultural Water Management_ 

**Table 2** 

Performance of the propagation time prediction model during the training and validation periods. CC denotes the correlation coefficient, and RMSE refers to the root mean square error. 

|Subregions|Training period||Validation period||
|---|---|---|---|---|
||RMSE (days)|CC|RMSE (days)|CC|
|Region I|9.0|0.87|13.6|0.77|
|Region II|9.2|0.88|11.3|0.77|
|Region III|8.6|0.89|13.6|0.78|
|Region IV|9.4|0.87|11.2|0.81|
|Region V|9.3|0.87|11.7|0.81|
|Region VI|10.0|0.86|10.1|0.82|
|Region VII|9.4|0.87|9.6|0.84|
|Region VIII|9.2|0.87|8.6|0.83|



time under changing environments (Xu et al., 2025b; Zhang et al., 2022). Compared to previous research, the novelty of this study lies in two key aspects: (1) An event-based approach was developed to identify drought propagation time, accompanied by a novel stage-based analysis of drought characteristics during propagation. This method enables a detailed examination of the variation in drought characteristics throughout the entire drought event, as well as during the development, persistence, and recovery stages, thereby revealing intra-event heterogeneity across different stages. (2) The dominant drivers of propagation time were identified at the drought event scale, and a predictive model was developed by integrating multiple influencing factors using the XGBoost method. To the best of our knowledge, this is the first attempt to forecast drought propagation time using machine learning at the event level. 

### _4.1. Variations in drought characteristics_ 

Our results indicate that agricultural droughts occur less frequently than meteorological droughts, which suggests that meteorological 

droughts do not always lead to other drought types, as many meteorological droughts may be attenuated by the catchment (Bevacqua et al., 2021; Brunner and Chartier-Rescan, 2024; Chen et al., 2020). Moreover, some agricultural droughts are not caused by meteorological droughts, meaning that precipitation deficit is not the only driving factor for agricultural droughts; other factors, such as increased evaporation, may also influence the occurrence of agricultural droughts (Li et al., 2018). Similar findings were also reported by Brunner and Chartier-Rescan (2024), who observed that streamflow droughts occur twice as often as precipitation droughts, as deficits originating in the atmosphere are amplified by land surface processes. The one-to-one type is the dominant propagation pattern from meteorological to agricultural drought, which is consistent with several previous studies on drought propagation at the event level. However, the proportion of the one-to-one type relative to other types may vary depending on the drought types and the method used for event matching. For example, Chen et al. (2024) found that the one-to-one type accounted for 86.7 % of the total paired meteorological and hydrological drought events, while Wang et al. (2023c) reported that it accounted for 55.6 % of the total paired meteorological and ecological drought events. 

Agricultural droughts typically persist longer than meteorological droughts during the entire drought event as well as the development, persistence, and recovery stages. The lengthening of drought duration during propagation has been documented in several previous studies (Bevacqua et al., 2021; Chen et al., 2020; Raposo et al., 2023). Moreover, we found that both the development speed and recovery speed of agricultural drought events are lower than those of meteorological drought events. These results highlight that the recovery of agricultural and hydrological droughts does not always coincide with that of meteorological droughts and may lag behind, indicating a more complex and varied recovery process for these two drought types (Xu et al., 2023a; Yang et al., 2017). The agricultural drought intensity during the entire drought stage, as well as the development, persistence, and recovery stages, is weaker than the corresponding meteorological drought 



**Fig. 13.** Density scatter plot of predicted versus observed drought propagation times during the validation period across the eight subregions. N denotes the number of propagation time samples. Slop refers to the slope of the linear fit. 

15 

_Agricultural Water Management 325 (2026) 110128_ 

_Z. Xu et al._ 

intensity. The attenuation characteristic of drought propagation within hydrological systems highlights that agricultural and hydrological droughts are typically less intense than the originating meteorological droughts, primarily due to the buffering capacity of soil moisture and groundwater storage (Raposo et al., 2023; Zhang et al., 2022). 

The spatial patterns of agricultural drought characteristics are different from those of meteorological drought. In fact, the spatial distribution of agricultural drought characteristics exhibits weak correlations with meteorological drought characteristics (Fig. A3), indicating that catchment attributes play an important role in modulating drought propagation. This finding is consistent with Bevacqua et al. (2021), who reported that hydrological drought characteristics cannot be fully explained by meteorological droughts. However, the spatial distribution of agricultural drought characteristics is closely related to soil moisture memory, which integrates the combined influences of soil properties, vegetation conditions, and climatic factors. Specifically, agricultural drought frequency is negatively correlated with soil moisture memory, whereas drought duration and intensity exhibit positive correlations. This pattern indicates that in regions with stronger soil moisture memory, soils can retain water for longer periods, thereby reducing drought occurrence frequency but leading to longer and more persistent droughts once dryness develops. In contrast, areas with weaker soil moisture memory respond more rapidly to meteorological fluctuations, resulting in more frequent yet shorter agricultural drought events (Xu et al., 2021b). 

### _4.2. Drought propagation time_ 

The event-based method adopted in this study determines a propagation time for each pair of matched drought events, providing physically interpretable results that better capture the dynamic linkage between meteorological and agricultural droughts. It also more effectively reflects the influence of initial soil moisture conditions and meteorological drought characteristics on propagation behavior. However, the propagation times estimated in this study are generally shorter than those reported in previous research using correlation analysis. For example, Zhang et al. (2021a) found that the propagation time from meteorological to agricultural drought in the YRB ranged from 2 to 9 months, while Dai et al. (2022) reported a range of 2–8 months for the Wei River Basin, the largest tributary of the Yellow River. These findings are consistent with the results of Wu et al. (2021b) and Bevacqua et al. (2021), who also reported that propagation times derived using run theory tend to be shorter than those obtained through correlation analysis. Wu et al. (2021b) further recommended the use of the run theory method, as it provides more conservative and event-oriented information that is valuable for drought prevention and mitigation. This difference arises because the event-based run theory can capture the direct physical response of soil moisture to meteorological deficits. In contrast, correlation analysis infers propagation time statistically by identifying the time scale of the meteorological drought index (SPI or SPEI) that shows the highest correlation with the agricultural drought index. As this method considers both dry and wet sequences, the resulting propagation time is influenced by wet periods and by the smoothing of meteorological conditions over longer accumulation periods. This may cause the estimated propagation time to be ambiguous in interpretation and to not fully reflect the actual propagation from meteorological to agricultural drought, but rather the response of hydrological processes (e.g., soil moisture) to meteorological processes (e. g., precipitation) (Ho et al., 2021; Li et al., 2022a; Wu et al., 2021b). In addition, unlike most previous studies that calculated drought indices using monthly data, which naturally yielded propagation times at a monthly resolution, this study estimated propagation time based on daily updated SSMI and SPEI data. This finer temporal resolution enables a more precise estimation of propagation time and may partly explain why the values obtained in this study are lower than those reported in previous research. Finally, because the event-matching criteria 

allow agricultural droughts to start slightly before meteorological droughts, negative propagation times are possible and may partially explain why the overall propagation times obtained in this study are shorter than those reported in previous studies. However, since only a small proportion (7.2 %) of matched events exhibited negative propagation times, their influence on the overall results is negligible. 

Initial soil moisture conditions, the timing of meteorological drought occurrence, and the development duration of meteorological droughts play key roles in determining the propagation time from meteorological to agricultural drought events across the entire YRB and its eight subregions. Initial soil moisture reflects the available water in the soil at the onset of a meteorological drought. Owing to the buffering effect of soil moisture, higher initial soil moisture, compared with lower initial soil moisture, can delay soil moisture depletion under precipitation deficits and postpone the time at which soil moisture falls below the agricultural drought threshold, resulting in a longer delay between agricultural and meteorological droughts (Li et al., 2022b; Xu et al., 2023b). Therefore, initial soil moisture conditions emerge as a key determinant of drought propagation time (Bakke et al., 2020; Gupta and Karthikeyan, 2024; Zhang et al., 2022, 2021b). The hydrological cycle exhibits distinct seasonal characteristics, which significantly influence the seasonal variations in drought propagation time (Ding et al., 2021b; Li et al., 2018). Precipitation and temperature exhibit pronounced seasonal synchrony in the YRB, with significantly higher values from June to September compared to other months (Li et al., 2024b). This leads to a faster hydrological cycle and reduced soil moisture persistence during this period. Consequently, the propagation time is generally shorter in these months than in the rest of the year. Drought development duration represents the time from the onset of meteorological drought to its peak intensity. A longer drought development duration indicates slower meteorological drought intensification, which could lead to a slower response of agricultural drought to meteorological drought, resulting in a longer drought propagation time. In addition to the three factors mentioned above, temperature during the development stage of meteorological drought also plays an important role in influencing drought propagation time. You et al. (2025) also demonstrated the critical role of temperature in the propagation from meteorological to agricultural drought. The underlying mechanism may be that rising temperatures enhance potential evapotranspiration, resulting in rapid soil moisture depletion (Wu et al., 2024) and thereby accelerating the propagation from meteorological to agricultural drought. The regional differences in average propagation time are relatively small. Spatial correlation analysis indicates that propagation time is only weakly correlated with most hydrometeorological factors, with meteorological drought duration exhibiting the strongest correlation (Fig. A3). This may be attributed to our finding that the development duration of meteorological drought exerts a significant influence on propagation time at the grid scale. 

Based on these findings, the identified dominant factors were incorporated into an XGBoost-based predictive model for each subregion, which yielded reliable predictions of drought propagation time. To validate the reliability of the XGBoost-based predictive model, we further employed Random Forest and Multiple Linear Regression to build predictive models for propagation time, using the same leave-oneregion-out cross-validation strategy as applied for the XGBoost model. As shown in Table 3, both the XGBoost- and Random Forest-based models consistently outperformed the Multiple Linear Regression–based model, indicating that machine learning approaches can more effectively capture the nonlinear relationships between predictors and the target variable and achieve better model performance. Although the Random Forest model outperformed the XGBoost model during the training period, its accuracy declined noticeably in the validation period, and in most subregions, it was lower than that of the XGBoost model. This suggests that the XGBoost approach offers stronger spatial transferability and generalization capability, providing more robust performance for spatially heterogeneous basins. Considering that the ultimate goal of establishing the predictive models is to forecast 

16 

_Z. Xu et al.                                                                                                                                                                                                                                       Agricultural Water Management_ 

_Agricultural Water Management 325 (2026) 110128_ 

**Table 3** 

Comparison of the performance of Random Forest– and Multiple Linear Regression–based predictive models for drought propagation time. 

|Subregions|Random Forest||||Multiple Linear Re|gression|||
|---|---|---|---|---|---|---|---|---|
||Training<br>period||Validation<br>period||Training<br>period||Validation<br>period||
||RMSE (days)|CC|RMSE (days)|CC|RMSE (days)|CC|RMSE (days)|CC|
|Region I|7.5|0.91|14.2|0.75|13.7|0.66|17.2|0.61|
|Region II|7.7|0.92|11.6|0.76|14.4|0.66|14.2|0.57|
|Region III|7.3|0.92|13.7|0.77|14.0|0.65|16.4|0.61|
|Region IV|7.8|0.91|11.0|0.81|14.4|0.64|13.8|0.68|
|Region V|7.7|0.91|11.8|0.81|14.3|0.64|15.0|0.65|
|Region VI|7.8|0.92|10.7|0.81|15.1|0.62|12.2|0.71|
|Region VII|7.8|0.91|9.5|0.84|14.5|0.64|12.7|0.70|
|Region VIII|7.8|0.91|8.9|0.82|14.4|0.64|12.0|0.64|



propagation time, the XGBoost-based model is therefore considered more suitable for this application. 

### _4.3. Advantages and uncertainties_ 

The quantification of drought propagation time in this study enables the prediction of agricultural drought occurrence based on meteorological drought conditions. Once a meteorological drought is detected, the estimated propagation time provides an early indication of when an agricultural drought is likely to occur. Furthermore, the key factors identified as influencing propagation time, such as initial soil moisture, can be incorporated into agricultural drought forecasting models, potentially enhancing the accuracy and reliability of predictions. It is important to note that soil moisture dynamics derived from the ERA5Land product are driven solely by meteorological forcing and land surface processes, without explicit representation of anthropogenic interventions such as irrigation, groundwater pumping, or reservoir regulation. Thus, the drought propagation analyzed in this study represents the linkage between meteorological and agricultural droughts in the absence of human intervention, providing insights into how meteorological anomalies are transmitted to root-zone soil moisture. Understanding drought propagation behavior in the absence of human intervention remains essential because it provides a valuable scientific foundation for guiding irrigation management by identifying when and where supplemental irrigation may be required to mitigate the impacts of drought on crops. Specifically, by quantifying the propagation time from meteorological to agricultural drought, the results can be used to estimate the potential onset time of agricultural drought following the detection of meteorological drought. This enables water managers to schedule irrigation proactively in anticipation of soil moisture deficits, thereby improving the timeliness and efficiency of irrigation responses. Moreover, regions with shorter propagation times, where agricultural drought tends to develop more rapidly following meteorological drought, can be identified as more vulnerable areas in which irrigation should be prioritized during dry spells. By allocating water resources more efficiently in these areas, water-use efficiency can be improved and drought risk effectively reduced. Given that our results confirm that initial soil moisture is a key driver of propagation time, measures that enhance soil water retention can therefore directly help slow down the propagation from meteorological to agricultural drought. In practice, enhancing soil water retention through agronomic measures (e.g., improving soil structure or increasing organic matter) may increase the buffering capacity of the root zone (You et al., 2025), thereby lengthening the propagation time and providing a wider operational window for irrigation scheduling. 

Given that the matching criteria directly affect the matched drought events, it is important to evaluate whether the selected 10-day window influences the results. To assess the sensitivity of the temporal window used for drought event matching, we varied the windows defined in criteria (1) and (2) and analyzed their effects on the propagation rate. 

For criterion (1), which allows agricultural droughts to occur slightly earlier than meteorological droughts, the lead window was iteratively adjusted from − 60 to 0 days at 5-day intervals (Fig. A4 (a)). For criterion (2), which links agricultural droughts starting after the end of meteorological droughts, the lag window was varied from 0 to 60 days at the same interval (Fig. A4 (b)). The results indicate that for criterion (1), the propagation rate increases slightly as the onset of agricultural droughts occurs further ahead of meteorological droughts, whereas for criterion (2), the propagation rate also increases with a longer lag between the two drought types. Nevertheless, the variation in propagation rate across different window lengths is minor, indicating that the identified propagation behavior is largely insensitive to the selection of the matching window length. 

Although this study provides a comprehensive analysis of drought propagation from meteorological to agricultural drought at the event scale, several limitations remain. The data used in this study are mainly from ERA5-Land. Previous evaluations have demonstrated that the ERA5-Land soil moisture product has improved accuracy compared with earlier versions (Munoz-Sabater et al., 2021˜ ) and generally outperforms other widely used datasets such as GLDAS and GLEAM (Fan et al., 2022; Hong et al., 2024; Ling et al., 2021). Moreover, ERA5-Land has been extensively applied in regional and global drought studies (Hirschi et al., 2025; Li et al., 2022a; You et al., 2025), which supports its reliability. Nevertheless, uncertainties in reanalysis products remain inevitable, particularly due to model parameterizations. These uncertainties may influence the absolute values of drought characteristics, such as duration and intensity, and potential biases in soil moisture simulations could lead to over- or underestimation of agricultural drought severity in certain regions. However, as this study primarily focuses on event-scale propagation dynamics, the key findings, including the observed attenuation and lengthening patterns during propagation and the identification of initial soil moisture as the dominant driver, are less likely to be substantially affected. Furthermore, because drought events were identified using standardized indices rather than the absolute values of precipitation or soil moisture, systematic biases in the datasets are unlikely to affect the robustness of the conclusions. Importantly, You et al. (2025) likewise used ERA5-Land soil moisture data to investigate drought propagation and validated their results using multiple independent datasets. The consistency of their findings across different data sources provides additional evidence supporting the robustness of our results in this study. Future research should incorporate multiple datasets and ensemble modeling approaches to further evaluate the reliability of the results. 

The applicability of the proposed event-based framework was demonstrated in the YRB. However, the methodology is not inherently basin-specific, as it relies on widely available meteorological and soil moisture datasets, together with generic event-matching techniques and machine learning approaches. This suggests that the framework has strong potential for generalizability to basins with different climatic conditions and cropping systems, thereby offering a transferable tool for 

17 

_Agricultural Water Management 325 (2026) 110128_ 

_Z. Xu et al._ 

understanding and predicting drought propagation processes in diverse environments. Nevertheless, although the dominant factors influencing propagation time were identified using statistical and machine learning analyses, and their potential physical mechanisms were preliminarily examined, a comprehensive understanding of these mechanisms is still lacking and requires further in-depth investigation. Future research should therefore extend the application of this framework to other regions and drought types (e.g., hydrological or ecological droughts) to comprehensively assess its robustness and transferability. Furthermore, integrating physically based hydrological modeling and causal inference approaches could provide valuable insights into the mechanisms of drought propagation, thereby enhancing both the theoretical foundation and predictive capability of the framework. 

### **5. Conclusions** 

This study examined variations in drought characteristics during the propagation from meteorological to agricultural drought at the event level in the YRB. It also identified the factors influencing propagation time and developed a prediction model for propagation time using the XGBoost algorithm. Meteorological droughts occur more frequently than agricultural droughts. Approximately 49.5 % of meteorological drought events transition into agricultural drought events, with the majority of matched meteorological and agricultural drought events exhibiting a one-to-one relationship. Drought propagation exhibits a lengthening of duration and attenuation of intensity across different drought stages. On average, the duration of agricultural droughts is more than twice that of meteorological droughts, whereas the drought intensity propagation index ranges from 0.78 to 0.85. Moreover, the development and recovery speeds of meteorological droughts are faster than those of agricultural droughts. These patterns can be partly attributed to the buffering effects of antecedent soil moisture, which constrain the transition from meteorological to agricultural drought and moderate the intensity of agricultural drought responses. The average propagation time from meteorological to agricultural drought in the YRB is 18.1 days. Initial soil moisture conditions are the most dominant factor influencing event-scale propagation time, followed by the occurrence time of meteorological drought events and their development duration. A predictive model for drought propagation time, established using the XGBoost algorithm with the identified dominant factors as inputs, demonstrates reliable predictive performance. The findings deepen our understanding of drought propagation from meteorological to agricultural drought and provide a practical basis for developing early warning systems and optimizing agricultural water management strategies. 

### **CRediT authorship contribution statement** 

**Zhengguang Xu:** Writing – review & editing, Visualization, Methodology, Data curation. **Bo Jiang:** Writing – review & editing, Validation, Methodology. **Xiao Guo:** Writing – review & editing, Supervision, Validation, Methodology. **Zhiyong Wu:** Writing – review & editing. **Siqi Fan:** Writing – review & editing. 

### **Declaration of Competing Interest** 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

### **Acknowledgments** 

This work was supported by the National Natural Science Foundation of China (grant numbers 42401025, U2240225, 52579007). 

### **Appendix A. Supporting information** 

Supplementary data associated with this article can be found in the online version at doi:10.1016/j.agwat.2026.110128. 

### **Data availability** 

Data will be made available on request. 

### **References** 

- Apurv, T., Sivapalan, M., Cai, X., 2017. Understanding the role of climate characteristics in drought propagation. Water Resour. Res. 53, 9304–9329. https://doi.org/ 10.1002/2017WR021445. 

- Bakke, S.J., Ionita, M., Tallaksen, L.M., 2020. The 2018 northern European hydrological drought and its drivers in a historical perspective. Hydrol. Earth Syst. Sci. 24, 5621–5653. https://doi.org/10.5194/hess-24-5621-2020. 

- Barker, L.J., Hannaford, J., Chiverton, A., Svensson, C., 2016. From meteorological to hydrological drought using standardised indicators. Hydrol. Earth Syst. Sci. 20, 2483–2505. https://doi.org/10.5194/hess-20-2483-2016. 

- Bevacqua, A.G., Chaffe, P.L.B., Chagas, V.B.P., AghaKouchak, A., 2021. Spatial and temporal patterns of propagation from meteorological to hydrological droughts in Brazil. J. Hydrol. 603, 126902. https://doi.org/10.1016/j.jhydrol.2021.126902. 

- Bhardwaj, K., Shah, D., Aadhar, S., Mishra, V., 2020. Propagation of meteorological to hydrological droughts in india. J. Geophys. Res. Atmos. 125, e2020JD033455. https://doi.org/10.1029/2020JD033455. 

- Brunner, M.I., Chartier-Rescan, C., 2024. Drought spatial extent and dependence increase during drought propagation from the atmosphere to the hydrosphere. Geophys. Res. Lett. 51, e2023GL107918. https://doi.org/10.1029/2023GL107918. 

- Chen, J., Fan, Y., Zhang, Y., Peng, J., Zhang, J., Cao, C., 2024. Comprehensive propagation characteristics between paired meteorological and hydrological drought events: Insights from various underlying surfaces. Atmos. Res. 299, 107193. https:// doi.org/10.1016/j.atmosres.2023.107193. 

- Chen, N., Li, R., Zhang, X., Yang, C., Wang, X., Zeng, L., et al., 2020. Drought propagation in Northern China Plain: A comparative analysis of GLDAS and MERRA-2 datasets. J. Hydrol. 588, 125026. https://doi.org/10.1016/j.jhydrol.2020.125026. 

- Chen, T., Guestrin, C., 2016. XGBoost: a scalable tree boosting system. Proc. 22nd ACM SIGKDD Int. Conf. Knowl. Discov. Data Min. 785–794. https://doi.org/10.1145/ 2939672.2939785. 

- Dai, M., Huang, S., Huang, Q., Zheng, X., Su, X., Leng, G., et al., 2022. Propagation characteristics and mechanism from meteorological to agricultural drought in various seasons. J. Hydrol. 610, 127897. https://doi.org/10.1016/j. jhydrol.2022.127897. 

- Das, S., Das, J., Umamahesh, N.V., 2022. Investigating the propagation of droughts under the influence of large-scale climate indices in India. J. Hydrol. 610, 127900. https:// doi.org/10.1016/j.jhydrol.2022.127900. 

- Ding, Y., Xu, J., Wang, X., Cai, H., Zhou, Z., Sun, Y., Shi, H., 2021b. Propagation of meteorological to hydrological drought for different climate regions in China. J. Environ. Manag 283, 111980. https://doi.org/10.1016/j.jenvman.2021.111980. 

- Ding, Y., Gong, X., Xing, Z., Cai, H., Zhou, Z., Zhang, D., et al., 2021a. Attribution of meteorological, hydrological and agricultural drought propagation in different climatic regions of China. Agr. Water Manag. 255, 106996. https://doi.org/ 10.1016/j.agwat.2021.106996. 

- Fan, L., Xing, Z., Lannoy, G.D., Frappart, F., Peng, J., Zeng, J., et al., 2022. Evaluation of satellite and reanalysis estimates of surface and root-zone soil moisture in croplands of Jiangsu Province, China. Remote Sens. Environ. 282, 113283. https://doi.org/ 10.1016/j.rse.2022.113283. 

- Fang, W., Huang, S., Huang, Q., Huang, G., Wang, H., Leng, G., Wang, L., 2020. Identifying drought propagation by simultaneously considering linear and nonlinear dependence in the Wei River basin of the Loess Plateau, China. J. Hydrol. 591, 125287. https://doi.org/10.1016/j.jhydrol.2020.125287. 

- Fleig, A.K., Tallaksen, L.M., Hisdal, H., Demuth, S., 2006. A global evaluation of streamflow drought characteristics. Hydrol. Earth Syst. Sci. 10, 535–552. https:// doi.org/10.5194/hess-10-535-2006. 

- Gevaert, A.I., Veldkamp, T.I.E., Ward, P.J., 2018. The effect of climate type on timescales of drought propagation in an ensemble of global hydrological models. Hydrol. Earth Syst. Sci. 22, 4649–4665. https://doi.org/10.5194/hess-22-4649-2018. 

- Gringorten, I.I., 1963. A plotting rule for extreme probability paper. J. Geophys. Res. 68, 813–814. https://doi.org/10.1029/JZ068i003p00813. 

- Gupta, A., Karthikeyan, L., 2024. Role of initial conditions and meteorological drought in soil moisture drought propagation: an event-based causal analysis over South Asia. Earths Future 12, e2024EF004674. https://doi.org/10.1029/2024EF004674. 

- Hao, Z., AghaKouchak, A., 2013. Multivariate standardized drought index: a parametric multi-index model. Adv. Water Resour. 57, 12–18. https://doi.org/10.1016/j. advwatres.2013.03.009. 

- Hirschi, M., Stradiotti, P., Crezee, B., Dorigo, W., Seneviratne, S.I., 2025. Potential of long-term satellite observations and reanalysis products for characterising soil drying: trends and drought events. Hydrol. Earth Syst. Sci. 29, 397–425. https://doi. org/10.5194/hess-29-397-2025. 

- Ho, S., Tian, L., Disse, M., Tuo, Y., 2021. A new approach to quantify propagation time from meteorological to hydrological drought. J. Hydrol. 603, 127056. https://doi. org/10.1016/j.jhydrol.2021.127056. 

18 

_Agricultural Water Management 325 (2026) 110128_ 

_Z. Xu et al._ 

- Hong, X., Jia, S., Zhu, W., Song, Z., 2024. Evaluation of global seamless soil moisture products over China: A perspective of soil moisture sensitivity to precipitation. J. Hydrol. 641, 131789. https://doi.org/10.1016/j.jhydrol.2024.131789. 

- Huang, X., Yang, X., Wu, F., Zhang, J., 2025. Future propagation characteristics of meteorological drought to hydrological drought in the Yellow River basin. J. Hydrol. 649, 132443. https://doi.org/10.1016/j.jhydrol.2024.132443. 

- Li, J., Guo, Y., Wang, Y., Lu, S., Chen, X., 2018. Drought Propagation Patterns under Naturalized Condition Using Daily Hydrometeorological Data. Adv. Meteor. 2018, 2469156. https://doi.org/10.1155/2018/2469156. 

- Li, L., Peng, Q., Xu, J., Gu, X., Cai, H., 2024b. Widespread enhancement and slower occurrence of agricultural drought events in drylands of the Yellow River Basin. J. Hydrol. Reg. Stud. 52, 101692. https://doi.org/10.1016/j.ejrh.2024.101692. 

- Li, L., Peng, Q., Wang, M., Cao, Y., Gu, X., Cai, H., 2024a. Quantitative analysis of vegetation drought propagation process and uncertainty in the Yellow River Basin. Agr. Water Manag. 295, 108775. https://doi.org/10.1016/j.agwat.2024.108775. 

- Li, Q., Ye, A., Zhang, Y., Zhou, J., 2022a. The peer-to-peer type propagation from meteorological drought to soil moisture drought occurs in areas with strong landatmosphere interaction. Water Resour. Res. 58, e2022WR032846. https://doi.org/ 10.1029/2022WR032846. 

- Li, R., Chen, N., Zhang, X., Zeng, L., Wang, X., Tang, S., et al., 2020. Quantitative analysis of agricultural drought propagation process in the Yangtze River Basin by using cross wavelet analysis and spatial autocorrelation. Agr. For. Meteor. 280, 107809. https:// doi.org/10.1016/j.agrformet.2019.107809. 

- Li, Y., Huang, S., Wang, H., Zheng, X., Huang, Q., Deng, M., Peng, J., 2022b. Highresolution propagation time from meteorological to agricultural drought at multiple levels and spatiotemporal scales. Agr. Water Manag. 262, 107428. https://doi.org/ 10.1016/j.agwat.2021.107428. 

- Lin, H., Yu, Z., Chen, X., Gu, H., Ju, Q., Shen, T., 2023a. Spatial-temporal dynamics of meteorological and soil moisture drought on the Tibetan Plateau: Trend, response, and propagation process. J. Hydrol. 626, 130211. https://doi.org/10.1016/j. jhydrol.2023.130211. 

- Lin, Q., Wu, Z., Zhang, Y., Peng, T., Chang, W., Guo, J., 2023b. Propagation from meteorological to hydrological drought and its application to drought prediction in the Xijiang River basin, South China. J. Hydrol. 617, 128889. https://doi.org/ 10.1016/j.jhydrol.2022.128889. 

- Ling, X., Huang, Y., Guo, W., Wang, Y., Chen, C., Qiu, B., et al., 2021. Comprehensive evaluation of satellite-based and reanalysis soil moisture products using in situ observations over China. Hydrol. Earth Syst. Sci. 25, 4209–4229. https://doi.org/ 10.5194/hess-25-4209-2021. 

- Liu, Q., Yang, Y., Liang, L., Jun, H., Yan, D., Wang, X., et al., 2023. Thresholds for triggering the propagation of meteorological drought to hydrological drought in water-limited regions of China. Sci. Total Environ. 876, 162771. https://doi.org/ 10.1016/j.scitotenv.2023.162771. 

- Mei, L., Aru, H., Tong, S., Wang, Y., Guo, E., Zhang, T., et al., 2025. Study on the propagation processes and driving mechanisms of meteorological, hydrological, and agricultural droughts on the Mongolian Plateau. J. Hydrol. 660, 133511. https://doi. org/10.1016/j.jhydrol.2025.133511. 

- Mondal, S., K. Mishra, A., Leung, R., Cook, B., 2023. Global droughts connected by linkages between drought hubs. Nat. Commun. 14, 144. https://doi.org/10.1038/ s41467-022-35531-8. 

- Munoz-Sabater, J., Dutra, E., Agustí-Panareda, A., Albergel, C., Arduini, G., Balsamo, G., ˜ et al., 2021. ERA5-Land: a state-of-the-art global reanalysis dataset for land applications. Earth Syst. Sci. Data 13, 4349–4383. https://doi.org/10.5194/essd-134349-2021. 

- Qian, T., Su, X., Wu, H., Singh, V.P., Zhang, T., 2025. An agricultural drought early warning threshold model with considering copula combined with diminishing marginal benefit theory: A case study in the Yellow River basin. Agr. Water Manag. 316, 109582. https://doi.org/10.1016/j.agwat.2025.109582. 

- Raposo, Vd.M.B., Costa, V.A.F., Rodrigues, A.F., 2023. A review of recent developments on drought characterization, propagation, and influential factors. Sci. Total Environ. 898, 165550. https://doi.org/10.1016/j.scitotenv.2023.165550. 

- Sattar, M.N., Lee, J.-Y., Shin, J.-Y., Kim, T.-W., 2019. Probabilistic characteristics of drought propagation from meteorological to hydrological drought in South Korea. Water Resour. Manag 33, 2439–2452. https://doi.org/10.1007/s11269-019-022789. 

- Tallaksen, L.M., Madsen, H., Clausen, B., 1997. On the definition and modelling of streamflow drought duration and deficit volume. Hydrol. Sci. J. 42, 15–33. https:// doi.org/10.1080/02626669709492003. 

- Tu, X., Du, Y., Singh, V.P., Chen, X., Zhao, Y., Ma, M., et al., 2019. Bivariate Design of Hydrological Droughts and Their Alterations under a Changing Environment. J. Hydrol. Eng. 24, 04019015. https://doi.org/10.1061/(ASCE)HE.19435584.0001788. 

- Vicente-Serrano, S.M., Beguería, S., Lopez-Moreno, J.I., 2010. A Multiscalar Drought ´ Index Sensitive to Global Warming: The Standardized Precipitation Evapotranspiration Index. J. Clim. 23, 1696–1718. https://doi.org/10.1175/ 2009JCLI2909.1. 

- Wang, A., Tao, H., Ding, G., Zhang, B., Huang, J., Wu, Q., 2023a. Global cropland exposure to extreme compound drought heatwave events under future climate change. Weather Clim. Extrem. 40, 100559. https://doi.org/10.1016/j. wace.2023.100559. 

- Wang, T., Tu, X., Singh, V.P., Chen, X., Lin, K., Zhou, Z., Zhu, J., 2023b. A CMIP6-based framework for propagation from meteorological and hydrological droughts to socioeconomic drought. J. Hydrol. 623, 129782. https://doi.org/10.1016/j. jhydrol.2023.129782. 

- Wang, Y., Zhou, H., Huang, J., Yu, J., Yuan, Y., 2023c. A framework for identifying propagation from meteorological to ecological drought events. J. Hydrol. 625, 130142. https://doi.org/10.1016/j.jhydrol.2023.130142. 

- Wu, G., Chen, J., Shi, X., Kim, J.-S., Xia, J., Zhang, L., 2022. Impacts of global climate warming on meteorological and hydrological droughts and their propagations. Earths Future 10, e2021EF002542. https://doi.org/10.1029/2021EF002542. 

- Wu, H., Su, X., Singh, V.P., 2021a. Blended dry and hot events index for monitoring dryhot events over global land areas. Geophys. Res. Lett. 48, e2021GL096181. https:// doi.org/10.1029/2021GL096181. 

- Wu, H., Su, X., Singh, V.P., Niu, J., 2024. Predicting compound agricultural drought and hot events using a Cascade Modeling framework combining Bayesian Model Averaging ensemble with Vine Copula (CaMBMAViC). J. Hydrol. 642, 131901. https://doi.org/10.1016/j.jhydrol.2024.131901. 

- Wu, H., Su, X., Huang, S., Singh, V.P., Zhou, S., Tan, X., Hu, X., 2025. Decreasing dynamic predictability of global agricultural drought with warming climate. Nat. Clim. Chang 15, 411–419. https://doi.org/10.1038/s41558-025-02289-y. 

- Wu, J., Chen, X., Yao, H., Zhang, D., 2021b. Multi-timescale assessment of propagation thresholds from meteorological to hydrological drought. Sci. Total Environ. 765, 144232. https://doi.org/10.1016/j.scitotenv.2020.144232. 

- Xiong, H., Han, J., Yang, Y., 2025. Propagation from meteorological to hydrological drought: characteristics and influencing factors. Water Resour. Res. 61, e2024WR037765. https://doi.org/10.1029/2024WR037765. 

- Xu, D., Wang, M., Zhang, K., Zhang, Q., Wu, S., Fu, J., 2025a. Response mechanism of agricultural drought to meteorological drought in the Yellow River Basin. Agr. Water Manag. 318, 109732. https://doi.org/10.1016/j.agwat.2025.109732. 

- Xu, Y., Zhang, X., Hao, Z., Singh, V.P., Hao, F., 2021a. Characterization of agricultural drought propagation over China based on bivariate probabilistic quantification. J. Hydrol. 598, 126194. https://doi.org/10.1016/j.jhydrol.2021.126194. 

- Xu, Z., Wu, Z., He, H., Guo, X., Zhang, Y., 2021b. Comparison of soil moisture at different depths for drought monitoring based on improved soil moisture anomaly percentage index. Water Sci. Eng. 14, 171–183. https://doi.org/10.1016/j.wse.2021.08.008. 

- Xu, Z., Wu, Z., Shao, Q., He, H., Guo, X., 2023b. From meteorological to agricultural drought: propagation time and probabilistic linkages. J. Hydrol. Reg. Stud. 46, 101329. https://doi.org/10.1016/j.ejrh.2023.101329. 

- Xu, Z., Wu, Z., Guo, X., He, H., 2023a. Estimation of water required to recover from agricultural drought: Perspective from regression and probabilistic analysis methods. J. Hydrol. 617, 128888. https://doi.org/10.1016/j.jhydrol.2022.128888. 

- Xu, Z., Guo, X., Wu, Z., Li, G., 2025b. Spatiotemporal dynamic characteristics and influencing factors of propagation time from meteorological drought to agricultural drought. J. Hydrol. Reg. Stud. 62, 102806. https://doi.org/10.1016/j. ejrh.2025.102806. 

- Yang, Y., McVicar, T.R., Donohue, R.J., Zhang, Y., Roderick, M.L., Chiew, F.H.S., et al., 2017. Lags in hydrologic recovery following an extreme drought: Assessing the roles of climate and catchment characteristics. Water Resour. Res. 53, 4821–4837. https://doi.org/10.1002/2017WR020683. 

- You, Z., Sun, X., Sun, H., Chen, L., Lu, M., Xue, J., et al., 2025. Mechanisms of meteorological drought propagation to agricultural drought in China: insights from causality chain. npj Nat. Hazards 2, 24. https://doi.org/10.1038/s44304-02500073-8. 

- Yuan, X., Wang, Y., Ji, P., Wu, P., Sheffield, J., Otkin, J.A., 2023. A global transition to flash droughts under climate change. Science 380, 187–191. https://doi.org/ 10.1126/science.abn6301. 

- Zhang, H., Ding, J., Wang, Y., Zhou, D., Zhu, Q., 2021a. Investigation about the correlation and propagation among meteorological, agricultural and groundwater droughts over humid and arid/semi-arid basins in China. J. Hydrol. 603, 127007. https://doi.org/10.1016/j.jhydrol.2021.127007. 

- Zhang, K., Zhang, Q., Wang, G., Gu, X., Zhao, J., Feng, A., 2024. Spatiotemporal interactions between soil moisture and water availability across the Yellow River Basin, China. J. Hydrol. Reg. Stud. 54, 101874. https://doi.org/10.1016/j. ejrh.2024.101874. 

- Zhang, Q., Miao, C., Guo, X., Gou, J., Su, T., 2023. Human activities impact the propagation from meteorological to hydrological drought in the Yellow River Basin, China. J. Hydrol. 623, 129752. https://doi.org/10.1016/j.jhydrol.2023.129752. 

- Zhang, X., Hao, Z., Singh, V.P., Zhang, Y., Feng, S., Xu, Y., Hao, F., 2022. Drought propagation under global warming: Characteristics, approaches, processes, and controlling factors. Sci. Total Environ. 838, 156021. https://doi.org/10.1016/j. scitotenv.2022.156021. 

- Zhang, Y., Hao, Z., Feng, S., Zhang, X., Xu, Y., Hao, F., 2021b. Agricultural drought prediction in China based on drought propagation and large-scale drivers. Agr. Water Manag. 255, 107028. https://doi.org/10.1016/j.agwat.2021.107028. 

- Zhao, A., Xiang, K., Zhang, A., Zhang, X., 2022. Spatial-temporal evolution of meteorological and groundwater droughts and their relationship in the North China Plain. J. Hydrol. 610, 127903. https://doi.org/10.1016/j.jhydrol.2022.127903. 

- Zhou, Z., Shi, H., Fu, Q., Ding, Y., Li, T., Liu, S., 2021. Investigating the propagation from meteorological to hydrological drought by introducing the nonlinear dependence with directed information transfer index. Water Resour. Res. 57, e2021WR030028. https://doi.org/10.1029/2021WR030028. 

19 

