

_Article_ 

# **Study of the Correlation Between Water Resource Changes and Drought Indices in the Yinchuan Plain Based on Multi-Source Remote Sensing and Deep Learning** 

**Hong Guan**<sup>**1,2,**</sup> *** , Zhiguo Jiang**<sup>**1**</sup> **, Jing Lu**<sup>**1**</sup> **and Yukuai Wan**<sup>**2**</sup> 

- 1 Department of Resources and Environmental Engineering, Ningxia Technical College of Wine and Desertification Prevention, Yinchuan 750100, China; nxlinxiao@126.com (Z.J.); 13895414737@163.com (J.L.) 

- 2 School of Civil and Hydraulic Engineering, Ningxia University, Yinchuan 750021, China; wanyukuai@nxu.edu.cn 

- Correspondence: guanhong0426@163.com 

### **Abstract** 

Academic Editor: Elias Dimitriou 

Received: 23 June 2025 Revised: 8 September 2025 Accepted: 12 September 2025 Published: 16 September 2025 

**Citation:** Guan, H.; Jiang, Z.; Lu, J.; Wan, Y. Study of the Correlation Between Water Resource Changes and Drought Indices in the Yinchuan Plain Based on Multi-Source Remote Sensing and Deep Learning. _Water_ **2025** , _17_ , 2740. https://doi.org/ 10.3390/w17182740 

**Copyright:** © 2025 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/ licenses/by/4.0/). 

This study examines the intricate relationship between water resource dynamics and drought indices in the Yinchuan Plain, China, by integrating multi-source remote sensing data with advanced deep learning techniques. Using data from 2002 to 2022, we applied Long Short-Term Memory (LSTM) networks to model the spatiotemporal dynamics of water resources and their relationships with the Standardized Precipitation Index (SPI), Standardized Precipitation Evapotranspiration Index (SPEI), and Palmer Drought Severity Index (PDSI). Our findings reveal a strong correlation between total water resources and the SPEI (r = 0.81, _p_ < 0.001), underscoring the pivotal role of evapotranspiration in this region’s water balance. The LSTM model outperformed traditional statistical methods, achieving a Root Mean Square Error of 0.142 for water resource predictions and 0.118 for drought index forecasts. Spatial analysis indicated stronger correlations in the northern Yinchuan Plain, likely influenced by its proximity to the Yellow River and regional water management practices. Wavelet coherence analysis identified significant coherence at the 6–12-month scale, highlighting the importance of seasonal to inter-annual strategies for water resource management. These results provide a robust foundation for developing effective water management policies and drought mitigation strategies in arid and semiarid regions. The methodologies presented are broadly applicable to similar water-scarce regions, contributing to global efforts in sustainable water resource management under changing climatic conditions. 

**Keywords:** water resource; drought indices; deep learning; LSTM; Yinchuan Plain 

## **1. Introduction** 

Water resources are critical for sustaining human civilization, agricultural productivity, and ecosystem stability, serving as a cornerstone of global sustainable development [1]. However, climate change-driven alterations in precipitation patterns, an increasing frequency of extreme weather events, and pressures from rapid urbanization and intensive agriculture pose unprecedented challenges to water resource management [2]. These challenges are particularly pronounced in arid and semi-arid regions, where water supply– demand imbalances and drought risks threaten regional food security and the ecological equilibrium. The Yinchuan Plain, located in the upper reaches of the Yellow River Basin in Northwest China, is a vital agricultural and economic hub that relies heavily on Yellow 

https://doi.org/10.3390/w17182740 

_Water_ **2025** , _17_ , 2740 

_Water_ **2025** , _17_ , 2740 

2 of 18 

River irrigation to maintain its unique oasis ecosystem. However, rapid urbanization, surging agricultural water demand, and precipitation uncertainties driven by climate warming exacerbate water scarcity and heightening drought risks in this region [3]. Investigating the interplay between water resource dynamics and drought indices in the Yinchuan Plain is thus essential for effective regional water resource management and ecological conservation, while also providing critical scientific insights for drought-vulnerable regions worldwide. 

Traditional statistical methods have been instrumental in water resource studies, offering foundational insights into hydrological processes and anthropogenic impacts. Vörösmarty et al. (2000) highlighted the threats posed by climate change and population growth to water supply–demand balances through global water resource vulnerability analyses, emphasizing the need for integrated management [1]. Gleick (2003) advocated for a “soft path” approach, prioritizing water-use efficiency and ecological protection to address scarcity and thus reshaping water resource research paradigms [4]. Milly et al. (2005) identified hydrological non-stationarity due to climate change as a challenge to conventional water resource planning [2], while Oki and Kanae (2006) underscored the importance of integrating regional climate and human activities into dynamic water supply– demand balance studies through global hydrological cycle analyses [5]. Wada et al. (2011) quantified the impact of human water demand, particularly from agricultural irrigation and urban use, on water resource stress [3]. However, these approaches often relied on groundbased observations with limited spatiotemporal resolution, constraining their ability to capture the complex, dynamic hydrological processes in drought-prone regions like the Yinchuan Plain. 

Drought index research has significantly advanced monitoring and early warning capabilities through the development of metrics to quantify drought severity and duration. The Standardized Precipitation Index (SPI) (McKee et al., 1993) is widely adopted for its multi-temporal scale flexibility, serving as a cornerstone for global drought monitoring in agriculture and water management [6]. The Palmer Drought Severity Index (PDSI) (Palmer, 1965) integrates precipitation, temperature, and soil moisture, providing a comprehensive perspective for long-term drought monitoring, particularly in the United States [7]. The Standardized Precipitation Evapotranspiration Index (SPEI) (Vicente-Serrano et al., 2010) exhibits an enhanced sensitivity to drought under warming climates by incorporating potential evapotranspiration, addressing limitations of the SPI [8]. Dai (2011) highlighted the advantages of multivariate drought indices in capturing drought complexity [9], while Hao and Singh (2015) advocated for integrated assessments incorporating precipitation, temperature, soil moisture, and vegetation health [10]. Despite these advances, drought indices are often applied to specific regions or temporal scales, with limited exploration of their responsiveness to dynamic water resource changes, particularly when considering multi-source data from arid environments like the Yinchuan Plain. 

Multi-source remote sensing technologies have revolutionized water resource research by providing a high spatiotemporal resolution and broad coverage. Rodell et al. (2009) demonstrated the potential of NASA’s GRACE satellite for monitoring groundwater depletion in India [11], while Guo et al. (2008) analyzed hydrological responses in China’s Poyang Lake Basin, revealing the impacts of climate and land-use changes [12]. Wulder et al. (2016) evaluated the long-term value of Landsat data for monitoring land cover and water resource dynamics [13]. Optical sensors excel in land cover classification, vegetation indices, and surface water monitoring [14], while radar sensors provide robust soil moisture estimates [15]. Thermal imaging sensors are critical for evapotranspiration estimation [16]. However, the use of multi-source remote sensing data to analyze long-term trends and seasonal patterns in water resource-drought interactions remains underexplored, particularly in drought-vulnerable regions like the Yinchuan Plain. 

_Water_ **2025** , _17_ , 2740 

3 of 18 

Machine learning, especially deep learning, has transformed environmental science by offering powerful tools to model complex systems. Reichstein et al. (2019) emphasized deep learning’s potential in hydrological forecasting and environmental monitoring [17], while Kratzert et al. (2019) showed the efficacy of Long Short-Term Memory (LSTM) networks in capturing nonlinear relationships in rainfall-runoff modeling [18]. Zhang et al. (2023) enhanced the drought prediction accuracy and spatiotemporal resolution by integrating multiple drought indices using deep learning models [19]. Xiao et al. (2024) introduced a hybrid CNN-RF model leveraging multisource data from MODIS, GLDAS, CHIRPS, and DEM to enhance agricultural drought monitoring in Southwest China, achieving superior accuracy in estimating SPEI-3 and forecasting drought categories [20]. Karpatne et al. (2017) proposed theory-guided data science, integrating physical knowledge into deep learning models to enhance interpretability and predictive accuracy [21]. In the context of the Yinchuan Plain, machine learning is critical for water resource assessment and drought prediction due to its ability to combine multi-source remote sensing data (e.g., optical, radar, and thermal imagery) with ground observations to capture the nonlinear and dynamic interactions between water resources and drought drivers, such as precipitation variability, soil moisture fluctuations, and anthropogenic pressures. Unlike traditional statistical methods, machine learning can model high-dimensional, multi-scale data, revealing intricate spatiotemporal patterns that are critical in arid environments where hydrological processes are highly variable and influenced by both the climate and human activities. However, deep learning applications for water resource-drought interactions in droughtvulnerable regions remain limited, particularly those leveraging long-term time series and multi-scale analyses. 

Despite progress in water resource dynamics, drought indices, and remote sensing, several knowledge gaps persist. First, traditional statistical methods and single drought indices struggle to capture the dynamic interplay between water resources and drought in complex arid environments like the Yinchuan Plain, where hydrological processes are influenced by both climatic variability and intense human activities. Second, while multisource remote sensing enhances monitoring capabilities, its application in integrating multidimensional data to analyze long-term trends and seasonal patterns in water resourcedrought interactions remains insufficient. Third, although deep learning has advanced environmental science, comprehensive models tailored for regional water resource management and drought prediction in arid regions are underexplored. This study addresses these gaps by integrating multi-source remote sensing data (optical, radar, and thermal sensors) with machine learning, specifically deep learning, to systematically analyze the spatiotemporal relationships between water resource dynamics and drought indices in the Yinchuan Plain. Utilizing long-term time series data, the study accounts for precipitation, evapotranspiration, soil moisture, land-use changes, and anthropogenic impacts to develop a deep learning-based predictive model that uncovers the underlying mechanisms of water resource dynamics and drought. This research not only provides a scientific foundation for water resource management and drought mitigation in the Yinchuan Plain but also offers a transferable analytical framework and predictive tools for water resource studies in drought-vulnerable regions globally, contributing to ecological conservation and sustainable development goals [5]. 

## **2. Study Area and Data** 

### _2.1. Overview of the Study Area_ 

The Yinchuan Plain is located in the north-central part of the Ningxia Plain in Northwest China, extending from Shizuishan in the north to the Loess Plateau in the south, from the Ordos Plateau in the east to the Helan Mountains in the west. The Yellow River 

_Water_ **2025** , _17_ , 2740 

4 of 18 

flows through the plain from south to north, shaping its topography and sustaining its agricultural activities. The specific geographical location, administrative divisions, and distribution of major water systems of the Yinchuan Plain are shown in Figure 1. The plain has a width of 10–50 km and a length of 280 km, covering an area of approximately 7800 km<sup>2</sup> , with elevation ranging from 1100 to 1200 m above sea level. Geologically, it was formed by fault subsidence followed by alluvial deposition from the Yellow River and long-term sedimentation of plain lakes and marshes. The plain is divided into two sub-regions at Qingtongxia: the northern YinChuan Plain and the southern Wei-Ning Plain. 





**Figure 1.** Geographical location, administrative division and main water system distribution map of Yinchuan Plain. 

Situated in a temperate arid climate, the Yinchuan Plain experiences abundant sunshine (approximately 3000 h annually) and a frost-free period of about 160 days. Annual precipitation averages around 200 mm, with significant diurnal temperature variations. The Yellow River serves as the lifeline of the region, supporting an extensive irrigation system that has transformed the plain into a critical agricultural oasis in Northwest China. Historically, the Yinchuan Plain has been vulnerable to severe drought events, with notable droughts recorded in the early 2000s and 2010s, leading to significant reductions in agricultural yields and water availability [22]. These events, exacerbated by climate variability and increasing water demand from urbanization and intensive agriculture, underscore the urgency of understanding water resource dynamics and drought patterns in this region. The plain’s unique geographical and climatic setting, combined with its ecological and economic significance, makes it an ideal case study for investigating water resource changes and drought impacts in arid regions. 

### _2.2. Data Source and Preprocessing_ 

This study leverages a comprehensive dataset spanning 2002 to 2022 to analyze water resource changes and drought conditions in the Yinchuan Plain. The dataset integrates multi-source remote sensing, meteorological, and hydrological data, with high detailed spatial and temporal resolutions specified below to ensure robust analysis of water resource dynamics and drought indices. The data sources used to evaluate changes in water resources in this study are presented in Table 1. 

_Water_ **2025** , _17_ , 2740 

5 of 18 

Remote sensing data form the backbone of this study. MODIS (Moderate Resolution Imaging Spectroradiometer) products, including MOD13A1 (vegetation indices, 500 m spatial resolution, 16-day intervals) and MOD11A2 (land surface temperature, 1 km spatial resolution, 8-day intervals), provide insights into vegetation health and thermal dynamics [23,24]. Landsat series imagery (Landsat 5, 7, and 8; 30 m spatial resolution, 16-day revisit cycle) is used for high-resolution land cover classification and change detection [25]. GRACE (Gravity Recovery and Climate Experiment) terrestrial water storage anomalies (TWSA, RL06 version, 1<sup>_◦_</sup> spatial resolution, monthly intervals) are employed to monitor groundwater and total water storage variations, with data processed using mascon solutions and scaling factors as recommended by Landerer and Swenson (2012) [26]. Soil moisture data are derived from the SMAP (Soil Moisture Active Passive) Level-3 product (36 km spatial resolution, daily intervals) for 2015–2022, supplemented by GLDAS (Global Land Data Assimilation System) soil moisture data (0.25<sup>_◦_</sup> spatial resolution, daily intervals) from 2002–2014 to ensure temporal continuity [27,28]. 

Meteorological data, including precipitation, temperature, and evapotranspiration data, were sourced from 12 local weather stations across the Yinchuan Plain that provide daily measurements. These are complemented by the CRU TS v4.06 dataset (0.5<sup>_◦_</sup> spatial resolution, monthly intervals) for spatially consistent climate variables [29]. Hydrological data, such as river discharge and reservoir storage levels, were obtained from the Ningxia Water Resources Department, with monthly records validated against historical gauge data. 

**Table 1.** Data sources for assessments of water resource changes. 

|**Component**|**Data Source**|**Temporal Resolution**|**Spatial Resolution**|
|---|---|---|---|
|Surface Water|Landsat, MODIS|16 days, 8 days|30 m, 500 m|
|Groundwater|GRACE|Monthly|1 degree|
|Soil Moisture|SMAP, GLDAS|Daily, 3-hourly|9 km, 0.25 degree|
|Climate Variables|Weather Stations, TRMM|Daily, 3-hourly|Point-based, 0.25 degree|



To ensure data quality and consistency, a comprehensive preprocessing workflow was applied to all datasets. For Landsat imagery, atmospheric correction was performed using the FLAASH model to mitigate atmospheric effects. Missing data due to cloud cover were addressed through appropriate interpolation techniques and mean imputation, ensuring consistency between datasets with varying spatial and temporal resolutions. Monthly MODIS data were derived using the maximum value composite method. For GRACE data, the latest RL06 version was employed, with recommended filtering and scaling factors applied to enhance accuracy. 

Land use classification of Landsat imagery was conducted using a supervised classification approach, validated against ground truth points and high-resolution imagery to ensure robustness. All datasets were resampled to a uniform spatial resolution of 250 m, aligned with MODIS products, using bilinear interpolation for spatial alignment and temporal aggregation to maintain consistency at a monthly resolution. This standardized preprocessing framework enabled integrated analysis of water resource dynamics and drought patterns, facilitating the application of deep learning models to investigate correlations between water resources and drought indices in the Yinchuan Plain over the past two decades. 

## **3. Research Methods** 

### _3.1. Assessment of Water Resources Change_ 

The water resource change assessment methodology employs a multi-faceted approach, integrating remote sensing data, ground observations, and statistical analysis. The 

_Water_ **2025** , _17_ , 2740 

6 of 18 

primary components evaluated include surface water, groundwater, and soil moisture. Surface water changes are quantified using a combination of Landsat-derived water indices and MODIS-based evapotranspiration estimates. The Normalized Difference Water Index ( _NDWI_ ) is calculated as: 



where _Green_ and _NIR_ represent the reflectance in the green and near-infrared bands, respectively [30]. 

The Total Water Storage Anomaly (TWSA) was derived from GRACE satellite data through the following steps. Temporal variations in the Earth’s gravity field are measured using microwave ranging between two satellites. These data are processed into spherical harmonic coefficients, typically truncated at degree 60 or 96; noise reduction is achieved by applying Gaussian smoothing (300–500 km) and decorrelation filters (e.g., DDK). The filtered coefficients are converted into gridded TWSA at a 1<sup>_◦_</sup> _×_ 1<sup>_◦_</sup> resolution using the 2 _πGρe_ gravity-to-water-height relationship (∆ _g_ = 3 ∆ _h_ ); and corrections are applied for leakage (using scaling factors from models such as GLDAS), Glacial Isostatic Adjustment (GIA), and ocean/atmospheric de-aliasing effects [31]. 

The integration of these components is achieved through a weighted sum approach, with weights determined by expert knowledge and local hydrological conditions. The final Water Resource Change Index ( _WRCI_ ) is expressed as: 



where ∆ represents change over time, _SW_ is surface water, _GW_ is groundwater, _SM_ is soil moisture, and _w_ are the respective weights [32]. 

To enable rigorous temporal trend analysis, the long-term trajectory of water resources was quantified by fitting an ordinary least-squares linear regression model to the annual non-seasonal water-resource volume series: 



where _WRt_ is the water resource volume at time _t_ , _β_ 0 is the intercept, _β_ 1 is the slope representing the annual rate of change, and _ϵt_ is the error term. The estimated _β_ 1 value of _−_ 0.02 billion m<sup>3</sup> /year indicates a steady decline in water resources [33]. 

### _3.2. Calculation of Drought Indexes_ 

To calculate drought indexes, multiple indices are employed to comprehensively assess drought conditions in the Yinchuan Plain. Three primary indices are utilized: the Standardized Precipitation Index ( _SPI_ ), the Standardized Precipitation Evapotranspiration Index ( _SPEI_ ), and the Vegetation Health Index ( _VHI_ ). The specific summary is shown in Table 2. 

The _SPI_ is derived from long-term precipitation records, with the initial step involving the fitting of the precipitation data to a gamma distribution: 



where _α_ and _β_ are shape and scale parameters, respectively. The cumulative probability is then transformed to the standard normal distribution to yield the _SPI_ value [34]. 

_Water_ **2025** , _17_ , 2740 

7 of 18 

The _SPEI_ incorporates both precipitation (P) and potential evapotranspiration (PET). The difference D = P _−_ PET is calculated and fitted to a log-logistic distribution: 



where _α_ , _β_ , and _γ_ are scale, shape, and origin parameters, respectively. The SPEI is then obtained as the standardized _F_ ( _x_ ) value [35]. 

The _VHI_ is a combination of the Vegetation Condition Index ( _VCI_ ) and Temperature Condition Index ( _TCI_ ): 



where 





NDVI is the Normalized Difference Vegetation Index, and LST is the Land Surface Temperature. In Equations (7) and (8), multiplication by 100 rescales the dimensionless ratios to a 0–100% range, yielding _VCI_ and _TCI_ as standardized indices that are directly comparable across space and time [36]. 

**Table 2.** Summary of Drought Indices. 

|**Index**|**Input Data**|**Timescale**|**Drought Type**|**Calculation**<br>**Complexity**|
|---|---|---|---|---|
|SPI|Precipitation|1, 3, 6, 12 months|Meteorological|Medium|
|SPEI|Precipitation,<br>Temperature|1, 3, 6, 12 months|Agricultural|High|
|VHI|NDVI, LST|16 days|Vegetation|Low|



To account for climate variability, the Standardized Precipitation Evapotranspiration Index ( _SPEI_ ) is calculated as follows: 



where W represents the probability-weighted moment, and C and d are coefficients. The variable _W_ is derived from the cumulative probability _P_ of the difference between precipitation and potential evapotranspiration (P _−_ PET), determined as follows: initially, the (P _−_ PET) is computed over the specified time scale; then, subsequently, it is fitted to a Pearson Type III distribution to estimate _P_ . Finally, if _P ≤_ 0.5, _W_ = � _−_ 2ln( _P_ ) with a negative sign, whereas if _P >_ 0.5, _W_ = � _−_ 2ln(1 _− P_ ) with a positive sign. The coefficients C in the Pearson Type III distribution approximation for the cumulative probability of the standardized variable are: C0 = 2.515517, C1 = 0.802853, and C2 = 0.010328. In the denominator of the formula, d is also a coefficient, with standard values of d1 = 1.432788, d2 = 0.189269, and d3 = 0.001308. These coefficients are derived from statistical fitting to ensure the formula accurately transforms the variable _W_ into a standard normal distribution. 

The calculation process involves data preprocessing, including quality control, gapfilling, and homogenization. For the _SPI_ and _SPEI_ , a 30-year baseline period (1981–2010) was used to fit the probability distributions. The indices are calculated at multiple timescales to capture short-term and long-term drought conditions. The _VHI_ was calculated using 16-day composite MODIS data, with a 10-year baseline for determining minimum and maximum values. All indices were computed on a pixel-by-pixel basis to maintain 

_Water_ **2025** , _17_ , 2740 

8 of 18 

spatial variability, providing a comprehensive assessment of drought conditions in the Yinchuan Plain. 

### _3.3. Long Short-Term Memory_ 

The deep learning model in this study was constructed using a Long Short-Term Memory (LSTM) network, optimized for analyzing the temporal dynamics of water resources and drought indices in the Yinchuan Plain. The LSTM architecture is chosen for its ability to capture long-term dependencies in time series data, making it ideal for modeling complex hydrological processes. The architecture of the LSTM model is depicted in Figure 2, with a summary of the architecture provided in Table 3. 



**Figure 2.** Schematic diagram of LSTM cell structure. 

The core of the LSTM model lies in its memory cell, which is governed by three gates: the input gate, forget gate, and output gate. The mathematical formulations for these gates and the cell state update are as follows: 

Input Gate: 



Forget Gate: 



The forget gate _ft_ determines whether previous cell state information _Ct−_ 1 will be retained or discarded, facilitating adaptation to temporal variability in hydrological data. Output Gate: 



Cell State Update: 



_Water_ **2025** , _17_ , 2740 

9 of 18 

Hidden State: 



where _it_ , _ft_ , and _ot_ refer to the input, forget, and output gates at time _t_ , respectively; The cell states at the current and previous time steps are represented by _Ct_ and _Ct−_ 1. Similarly, the hidden states at the current and previous time steps are denoted by _ht_ and _ht−_ 1. _xt_ is the input at time _t_ ; _Wi_ , _Wf_ , _Wo_ , and _WC_ are weight matrices; _bi_ , _b f_ , _bo_ , and _bC_ are bias vectors; _σ_ is the sigmoid activation function; and _tanh_ s is the hyperbolic tangent activation function [37]. 

The model architecture consists of multiple LSTM layers followed by dense layers for final prediction. The input features include historical water resource data, climate variables, and remotely sensed indices. The output is the predicted water resource change or drought index for the next time step. 

**Table 3.** LSTM model architecture summary. 

|**Layer**|**Type**|**Output Shape**|**Parameters**|
|---|---|---|---|
|Input|-|(None, time_steps,<br>features)|0|
|LSTM|Recurrent|(None, 64)|33,024|
|Dropout|Regularization|(None, 64)|0|
|LSTM|Recurrent|(None, 32)|12,416|
|Dense|Fully Connected|(None, 16)|528|
|Dense|Output|(None, 1)|17|



The model is trained using backpropagation through time (BPTT) with the Adam optimizer. To prevent overfitting, techniques such as dropout and L2 regularization are employed. The loss function used is the Mean Squared Error ( _MSE_ ): 



where _yi_ is the true value and _y_ ˆ _i_ is the predicted value. 

The model’s performance is evaluated using metrics such as Root Mean Square Error (RMSE) and R-squared (R<sup>2</sup> ) on a held-out test set. This deep learning approach allows for capturing complex, non-linear relationships in the hydrological system of the Yinchuan Plain, potentially improving the accuracy of water resource change and drought predictions [38]. 

### _3.4. Correlation Analysis_ 

This study employs a comprehensive correlation analysis to quantify the relationships between water resource changes and drought indices in the Yinchuan Plain. The multifaceted approach integrates parametric and non-parametric methods to capture both linear and non-linear associations. The Pearson correlation coefficient is used to evaluate linear relationships, while Spearman’s rank correlation coefficient assesses monotonic, potentially non-linear associations. To account for temporal lags between water resource changes and drought onset or cessation, cross-correlation analysis is conducted across various time lags. Additionally, partial correlation analysis is applied to control for confounding factors such as temperature and land-use changes, thereby isolating the specific relationship between water resources and drought indices. To facilitate interpretation of these complex interactions, a correlation matrix heatmap is generated, visually representing the strength and direction of relationships among multiple variables. Furthermore, wavelet coherence analysis is utilized to examine the temporal evolution of correlations across different time scales, 

_Water_ **2025** , _17_ , 2740 

10 of 18 

providing insights into how relationships between water resources and drought indices vary over time and frequency. This integrated correlation analysis framework enables a nuanced understanding of the complex dynamics governing water resource changes and drought conditions in the study area. 

The wavelet coherence analysis is mathematically expressed as: 



where _WTCxy_ ( _s_ , _τ_ ) is the wavelet coherence coefficient, _Wx_ ( _s_ , _τ_ ) and _Wy_ ( _s_ , _τ_ ) are continuous wavelet transforms of the x and y series, respectively, s is scale, τ is time, and _⟨·⟩_ denotes time averaging. 

## **4. Results and Analysis** 

### _4.1. Spatio-Temporal Change Characteristics of Water Resources_ 

The results of spatiotemporal dynamic analysis of water resources in the Yinchuan Plain from 2002 to 2022 are shown in Table 4, revealing obvious trends and changes that require in-depth analysis. The time series trend line (Figure 3a) shows that the total amount of water resources has been continuously declining. The average annual water volume has decreased from 3.2 billion cubic meters in 2002 to 2.8 billion cubic meters in 2022, equivalent to a reduction of 12.5% over 20 years. This is equivalent to a cumulative loss of approximately 400 million cubic meters, or an average annual loss of 20 million cubic meters. According to the data from the Ningxia Water Resources Bulletin (2022), this decline reflects a significant reduction in available water, which is equivalent to irrigating approximately 50,891 hectares of farmland (the actual irrigation water consumption for cultivated land in the entire region is 7860 cubic meters per hectare), thus posing a great threat to the sustainability of agricultural development. In this arid area, more than 60% of the output relies on the Yellow River (with an annual precipitation of about 200 mm). 

The spatial distribution maps (Figure 3b) for the years 2002, 2007, 2012, 2017, and 2022 illustrate the spatial variability of water resource availability. The water resources of the northwestern Yinchuan Plain, adjacent to the Yellow River and major irrigation channels, are relatively stable, with coverage decreasing from 25% of the area in 2002 to 20% in 2022. A quantitative assessment of these spatiotemporal changes highlights their socioeconomic and ecological significance. The overall 12.5% decline, combined with regional disparities, poses risks to food security and ecosystem stability, particularly in the southeast. 

**Table 4.** Summary of Water Resource Changes in Yinchuan Plain (2002–2022). 

||**Total Water**<br>**Resources**<br>**(Billion m**<sup>**3**</sup>**)**|**Surface Water**<br>**(Billion m**<sup>**3**</sup>**)**|**Groundwater**<br>**(Billion m**<sup>**3**</sup>**)**|**Annual**<br>**Change Rate**<br>**(%)**|**Precipitation**<br>**(mm)**|**Temperature**<br>**(**<sup>_◦_</sup>**C)**|
|---|---|---|---|---|---|---|
|2002|3.20|2.15|1.05|-|200|9.5|
|2006|3.14|2.10|1.04|_−_0.47|192|9.8|
|2010|3.07|2.04|1.03|_−_0.56|185|10.1|
|2014|2.98|1.96|1.02|_−_0.74|178|10.4|
|2018|2.88|1.88|1.00|_−_0.85|170|10.7|
|2022|2.80|1.81|0.99|_−_0.70|163|11.0|
|2002–2022|_−_0.40|_−_0.34|_−_0.06|_−_12.50|_−_37|+1.5|



_Water_ **2025** , _17_ , 2740 

11 of 18 



















































( **a** ) Time series variation graph of water resources 























<!-- Start of picture text -->
( b ) Spatially distributed heat map<br><!-- End of picture text -->

**Figure 3.** Spatiotemporal change trend chart of water resources in Yinchuan Plain from 2002 to 2022. 

### _4.2. Spatiotemporal Distribution Patterns of the Drought Index_ 

Figure 4 illustrates the spatiotemporal distribution patterns of three primary drought indices (SPI, SPEI, and PDSI) in the Yinchuan Plain, highlighting the complex and dynamic nature of drought characteristics in the region. All three indices exhibit significant spatial heterogeneity and temporal variability, reflecting differences in drought severity across geographical areas and time scales. The SPI distribution maps reveal a spatial gradient in drought conditions from northwest to southeast. In 2002, the SPI values in the northwest 

_Water_ **2025** , _17_ , 2740 

12 of 18 

were approximately 0.5, indicative of near-normal conditions, while the values in the southeast reached _−_ 1.5, corresponding to moderate drought. By 2022, SPI values decreased across the region, with the northwest exhibiting a value of around _−_ 0.5 and the southeast reaching _−_ 2.0, consistent with severe drought conditions. The SPEI distribution, which incorporates evapotranspiration effects, displays a more complex pattern. In 2002, SPEI values ranged from 0.8 in the northwest to _−_ 1.0 in the southeast. By 2022, SPEI values shifted to a range from _−_ 0.5 to _−_ 2.5, indicating an increase in drought severity across the plain. The central regions exhibited the most pronounced changes, with SPEI values decreasing by up to 1.5 units over the 20-year period. 











<!-- Start of picture text -->
( a ) SPI<br>( b ) SPEI<br>( c ) PDSI<br><!-- End of picture text -->

**Figure 4.** Spatiotemporal distribution map of typical drought index in the Yinchuan Plain. 

The PDSI maps provide a comprehensive insight into drought conditions in the Yinchuan Plain, integrating multiple components of the water balance. In 2002, PDSI values ranged from 2.0 in the northwest, indicating moist conditions, to _−_ 2.0 in the southeast, reflecting moderate drought. By 2022, this range widened from 1.0 to _−_ 4.0, revealing a more pronounced contrast between moist and dry regions. The central plain exhibited the greatest variability, with PDSI values fluctuating by up to 3.0 units between wet and dry years. 

_Water_ **2025** , _17_ , 2740 

13 of 18 

Quantitative analysis of drought indices across the plain reveals a clear trend toward increasing aridity: the SPI decreased from _−_ 0.3 in 2002 to _−_ 1.2 in 2022; the SPEI declined from _−_ 0.1 in 2002 to _−_ 1.5 in 2022; and the PDSI dropped from 0.5 in 2002 to _−_ 1.8 in 2022. These trends collectively indicate an intensifying drought in the Yinchuan Plain, particularly in the southeastern regions. The values of SPEI and PDSI, which account for temperature and evapotranspiration, suggest that rising temperatures and altered evapotranspiration rates are exacerbating drought conditions beyond the influence of precipitation deficits alone. The spatial variability in the PDSI maps highlights the role of local factors, such as irrigation practices and land-use changes, in modulating drought severity. 

These findings emphasize the need for spatially tailored water resource management and drought mitigation strategies in the Yinchuan Plain. The consistent trend toward drier conditions, as evidenced by all three indices, underscores the urgency of addressing water scarcity in this vital agricultural region. 

### _4.3. Correlation Analysis Between Water Resource Variability and Drought Indices_ 

The correlation analysis between water resource changes and drought indices in the Yinchuan Plain, based on simulated data from 2002 to 2022, reveals intricate spatiotemporal dynamics. We investigated relationships between total water resources, surface water, groundwater, and drought indices, including the Standardized Precipitation Index ( _SPI_ ), Standardized Precipitation Evapotranspiration Index ( _SPEI_ ), and Palmer Drought Severity Index ( _PDSI_ ). The correlations between various types of water resources and the drought index are shown in Table 5. Pearson correlation analysis indicated a strong positive correlation between total water resources and the _SPEI_ (r = 0.81, _p_ < 0.001), underscoring the critical influence of evapotranspiration on the region’s water balance. Surface water showed a robust correlation with the _SPI_ (r = 0.76, _p_ < 0.001), reflecting the direct impact of precipitation on surface hydrology, while groundwater exhibited a significant correlation with the _PDSI_ (r = 0.69, _p_ < 0.001), highlighting the impact of long-term hydrological conditions on aquifer dynamics. 

**Table 5.** Key correlation coefficients. 

|**Water**<br>**Resource**|**Drought Index**|**Correlation**<br>**Coefficient**|**_p_-Value**|**Correlation**<br>**Type**|
|---|---|---|---|---|
|Total Water|_SPEI_|0.81|<0.001|Pearson|
|Surface Water|_SPI_|0.76|<0.001|Pearson|
|Groundwater|_PDSI_|0.69|<0.001|Pearson|



Cross-correlation analysis identified a one-month lag between surface water changes and _SPI_ variations (maximum r = 0.79, _p_ < 0.001), indicating a rapid hydrological response to precipitation events. Similarly, the _SPEI_ led total water resource variability by one month (r = 0.81, _p_ < 0.001), while groundwater showed a lagged but significant correlation with the _SPEI_ (r = 0.69, _p_ < 0.001). Wavelet coherence analysis further elucidated these relationships, revealing the highest coherence at the 6–12-month scale (mean coherence _≈_ 0.88), which emphasizes the importance of seasonal to inter-annual hydroclimatic controls for water resource management. 

Figure 5 illustrates the varying strength of relationships across the Yinchuan Plain, with stronger correlations in the northern regions, likely influenced by their proximity to the Yellow River and major irrigation channels. These findings highlight the need for tailored, scale-dependent water management strategies to address the complex interplay of hydrological and climatic factors in the region. 

_Water_ **2025** , _17_ , 2740 

14 of 18 





















**Figure 5.** Spatial correlation heatmap of water resources and drought indices. 

### _4.4. Performance Evaluation of the Deep Learning Model_ 

The evaluation of our deep learning model for water resource and drought prediction in the Yinchuan Plain demonstrates substantial improvements over conventional methods. The Long Short-Term Memory (LSTM) network, trained on multi-source remote sensing data and historical records from 2002 to 2022, exhibits superior predictive performance across multiple metrics. Please refer to the performance of each model indicator in Table 6 for details. 

We compared the LSTM model against baseline methods, including Multiple Linear Regression (MLR) and Auto-Regressive Integrated Moving Average (ARIMA) models. The LSTM model achieved a Root Mean Square Error (RMSE) of 0.142 for water resource prediction and 0.118 for drought index forecasting, outperforming MLR (RMSE: 0.238 and 0.201) and ARIMA (RMSE: 0.197 and 0.183). Additionally, the coefficient of determination (R<sup>2</sup> ) for the LSTM model reached 0.89 for water resources and 0.92 for drought indices, significantly higher than MLR (R<sup>2</sup> : 0.71 and 0.75) and ARIMA (R<sup>2</sup> : 0.79 and 0.81). 

The LSTM model’s enhanced performance is attributed to its ability to capture complex nonlinear relationships and long-term dependencies within the data. Its architecture, comprising 64 LSTM units in the first layer and 32 in the second, followed by dense layers, was optimized through extensive hyperparameter tuning. These findings highlight the potential of deep learning to improve water resource management and drought forecasting in the Yinchuan Plain. By effectively integrating multi-source data and capturing intricate spatiotemporal patterns, the LSTM model is a robust tool for decision-makers to develop effective water management strategies and early warning systems for drought events. 

**Table 6.** Model performance metrics. 

|**Model**|**RMSE (Water)**|**RMSE**<br>**(Drought)**|**R**<sup>**2 **</sup>**(Water)**|**R**<sup>**2 **</sup>**(Drought)**|
|---|---|---|---|---|
|LSTM|0.142|0.118|0.89|0.92|
|MLR|0.238|0.201|0.71|0.75|
|ARIMA|0.197|0.183|0.79|0.81|



_Water_ **2025** , _17_ , 2740 

15 of 18 

### _4.5. Advantages of Multi-Source Remote Sensing Data and Deep Learning in Research_ 

The integration of multi-source remote sensing data with deep learning techniques provides a robust framework for analyzing water resource dynamics and drought patterns in the Yinchuan Plain, offering distinct advantages over traditional methods. Multi-source remote sensing ensures extensive spatial and temporal coverage, capturing key environmental variables critical for understanding hydrological processes. Optical sensors provide data on vegetation health and land use changes, while radar and thermal sensors yield insights into soil moisture and surface temperature, facilitating a comprehensive assessment of the water cycle and its ecological interactions. Deep learning, particularly LSTM networks, excels in processing high-dimensional datasets, detecting complex patterns and nonlinear relationships that conventional statistical approaches often fail to capture. The ability of LSTM models to handle large datasets and model long-term temporal dependencies enhances the accuracy of predictions of water resource variability and drought events. This synergistic approach produces reliable predictive models that effectively characterize the complex spatiotemporal dynamics of water resources and drought conditions. By advancing the understanding of hydrological interactions, this methodology equips water resource managers and policymakers with effective tools to address challenges posed by climate change and increasing water scarcity. 

## **5. Discussion** 

The findings of this study on water resource dynamics and drought indices in the Yinchuan Plain provide valuable insights into the hydrological complexities of arid regions. By integrating multi-source remote sensing data with advanced deep learning techniques, we have uncovered intricate patterns and relationships that were previously difficult to discern. A strong correlation between total water resources and SPEI highlights the pivotal role of evapotranspiration in the region’s water balance, emphasizing the importance for water management strategies that consider both precipitation and temperature trends. Additionally, the observed lag between surface water changes and variations in the SPI indicates a rapid hydrological response to precipitation events, with significant implications for flood management and water resource allocation. 

The superior performance of our LSTM model compared to traditional statistical approaches demonstrates the potential of deep learning in enhancing predictive capabilities for water resource management and drought forecasting. This improvement is particularly critical in the context of climate change, where historical patterns may no longer reliably predict future conditions. The model’s capacity to intricate nonlinear interactions and long-term dependencies enhances the understanding of the hydrological system’s behavior. 

Despite these advancements, certain limitations must be acknowledged. While remote sensing provides extensive spatial and temporal coverage, ground-based measurements remain essential for validating and calibrating models. Future research should prioritize the integration of diverse data sources, such as high-resolution satellite imagery and in situ observations, to further refine our understanding of local-scale hydrological processes. Moreover, the opaque nature of deep learning models poses challenges for interpretability, underscoring the need for explainable AI techniques tailored to hydrological applications. 

The spatial variability in the correlation between water resources and drought indices, particularly the stronger associations observed in the northern Yinchuan Plain, merits further exploration. This pattern may reflect influences from factors such as proximity to the Yellow River, variations in land use, or differences in regional water management practices. Understanding these spatial disparities is essential for designing targeted, effective water resource management strategies. 

_Water_ **2025** , _17_ , 2740 

16 of 18 

## **6. Conclusions** 

This study on water resource changes and drought indices in the Yinchuan Plain integrates multisource remote sensing data with advanced deep learning techniques to elucidate hydrological dynamics in this semi-arid agricultural region. We found a strong correlation between total water resources and the Standardized Precipitation Evapotranspiration Index (SPEI) (r = 0.81, _p_ < 0.001), highlighting the critical role of precipitation and evapotranspiration in modulating water balance. The proposed Long Short-Term Memory (LSTM) model outperformed traditional statistical methods in predicting water resource dynamics and SPEI, effectively capturing temporal dependencies and nonlinear patterns, such as the 1-month lag between surface water changes and Standardized Precipitation Index (SPI) variations (max r = 0.79). However, the LSTM model’s performance depends on the quality of input data and it may struggle with extreme events or long-term trends outside the training period due to its data-driven nature, necessitating complementary physical models for mechanistic insights. 

Coherence analysis revealed strong multi-scale relationships, with the highest coherence observed on the 6–12-month scale (average coherence = 0.88), driven by seasonal precipitation and irrigation cycles from the Yellow River, particularly in the northern Yinchuan Plain. These cycles reflect fluctuations in water availability, soil moisture, and aquifer recharge, influencing SPEI and the Palmer Drought Severity Index (PDSI). Spatial analysis showed stronger correlations in the northern regions, likely due to their closer proximity to the Yellow River and major irrigation channels compared to the southern regions, which enhance water availability and reduce drought impacts compared to the southern regions. These findings emphasize the interplay between geographical factors and water management practices in shaping water-drought dynamics. 

In conclusion, our findings provide a robust scientific basis for water resource management in the Yinchuan Plain. The strong correlation between water resources and the SPEI (r = 0.81, _p_ < 0.001), the 1-month lag with SPI (max r = 0.79), and the high wavelet coherence on a seasonal scales (average coherence = 0.88) underscore the need for adaptive strategies addressing both short-term variability (e.g., seasonal precipitation) and long-term trends (e.g., aquifer depletion). The integration of LSTM and wavelet coherence offers a precise framework for understanding these dynamics, supporting targeted policies for water allocation and drought mitigation in this semi-arid region. 

**Author Contributions:** Validation, Y.W.; Data curation, H.G. and J.L.; Writing—original draft, H.G.; Writing—review & editing, Z.J. and Y.W.; Visualization, J.L. All authors have read and agreed to the published version of the manuscript. 

**Funding:** This research was financially supported by Ningxia Natural Science Foundation of China (2024AAC03363), and the Scientific research project of the higher education Department of Ningxia (NYG-2024-380). 

**Data Availability Statement:** The data presented in this study are available on request from the corresponding author. 

**Conflicts of Interest:** The authors declare no conflicts of interest. 

## **References** 

1. Vörösmarty, C.J.; Green, P.; Salisbury, J.; Lammers, R.B. Global water resources: Vulnerability from climate change and population growth. _Science_ **2000** , _289_ , 284–288. [CrossRef] 

> 2. Milly, P.C.D.; Dunne, K.A.; Vecchia, A.V. Global pattern of trends in streamflow and water availability in a changing climate. _Nature_ **2005** , _438_ , 347–350. [CrossRef] 

> 3. Wada, Y.; van Beek, L.P.H.; Bierkens, M.F.P. Modelling global water stress of the recent past: On the relative importance of trends in water demand and climate variability. _Hydrol. Earth Syst. Sci._ **2011** , _15_ , 3785–3808. [CrossRef] 

_Water_ **2025** , _17_ , 2740 

17 of 18 

4. Gleick, P.H. Global freshwater resources: Soft-path solutions for the 21st century. _Science_ **2003** , _302_ , 1524–1528. [CrossRef] 

5. Oki, T.; Kanae, S. Global hydrological cycles and world water resources. _Science_ **2006** , _313_ , 1068–1072. [CrossRef] 

6. McKee, T.B.; Doesken, N.J.; Kleist, J. The relationship of drought frequency and duration to time scales. In Proceedings of the 8th Conference on Applied Climatology, Anaheim, CA, USA, 17–22 January 1993; Volume 17, pp. 179–183. 

7. Palmer, W.C. _Meteorological Drought_ ; Research Paper No. 45; US Department of Commerce Weather Bureau: Washington, DC, USA, 1965. 

8. Vicente-Serrano, S.M.; Beguería, S.; López-Moreno, J.I. A multiscalar drought index sensitive to global warming: The standardized precipitation evapotranspiration index. _J. Clim._ **2010** , _23_ , 1696–1718. [CrossRef] 

9. Dai, A. Drought under global warming: A review. _Wiley Interdiscip. Rev. Clim. Change_ **2011** , _2_ , 45–65. [CrossRef] 

10. Hao, Z.; Singh, V.P. Drought characterization from a multivariate perspective: A review. _J. Hydrol._ **2015** , _527_ , 668–678. [CrossRef] 11. Rodell, M.; Velicogna, I.; Famiglietti, J.S. Satellite-based estimates of groundwater depletion in India. _Nature_ **2009** , _460_ , 999–1002. [CrossRef] 

12. Guo, H.; Hu, Q.; Jiang, T. Annual and seasonal streamflow responses to climate and land-cover changes in the Poyang Lake basin, China. _J. Hydrol._ **2008** , _355_ , 106–122. [CrossRef] 

13. Wulder, M.A.; White, J.C.; Loveland, T.R.; Woodcock, C.E.; Belward, A.S.; Cohen, W.B.; Fosnight, E.A.; Shaw, J.; Masek, J.G.; Roy, D.P. The global Landsat archive: Status, consolidation, and direction. _Remote Sens. Environ._ **2016** , _185_ , 271–283. [CrossRef] 

14. Xiao, X.; Boles, S.; Liu, J.; Zhuang, D.; Frolking, S.; Li, C.; Salas, W.; Moore, B., III. Mapping paddy rice agriculture in southern China using multi-temporal MODIS images. _Remote Sens. Environ._ **2005** , _95_ , 480–492. [CrossRef] 

15. Chen, B.; Xiao, X.; Li, X.; Pan, L.; Doughty, R.; Ma, J.; Dong, J.; Qin, Y.; Zhao, B.; Zhao, B. A mangrove forest map of China in 2015: Analysis of time series Landsat 7/8 and Sentinel-1A imagery in Google Earth Engine cloud computing platform. _ISPRS J. Photogramm. Remote Sens._ **2017** , _131_ , 104–120. [CrossRef] 

16. Houborg, R.; Fisher, J.B.; Skidmore, A.K. Advances in remote sensing of vegetation function and traits. _Int. J. Appl. Earth Obs. Geoinf._ **2015** , _43_ , 1–6. [CrossRef] 

17. Reichstein, M.; Camps-Valls, G.; Stevens, B.; Jung, M.; Denzler, J.; Carvalhais, N.; Prabhat. Deep learning and process understanding for data-driven Earth system science. _Nature_ **2019** , _566_ , 195–204. [CrossRef] 

18. Kratzert, F.; Klotz, D.; Herrnegger, M.; Sampson, A.K.; Hochreiter, S.; Nearing, G.S. Toward improved predictions in ungauged basins: Exploiting the power of machine learning. _Water Resour. Res._ **2019** , _55_ , 11344–11354. [CrossRef] 

19. Zhang, Y.; Xie, D.; Tian, W.; Zhao, H.; Geng, S.; Lu, H.; Ma, G.; Huang, J.; Choy Lim Kam Sian, K.T. Construction of an integrated drought monitoring model based on deep learning algorithms. _Remote Sens._ **2023** , _15_ , 667. [CrossRef] 

20. Xiao, X.; Ming, W.; Luo, X.; Yang, L.; Li, M.; Yang, P.; Ji, X.; Li, Y. Leveraging multisource data for accurate agricultural drought monitoring: A hybrid deep learning model. _Agric. Water Manag._ **2024** , _293_ , 108692. [CrossRef] 

21. Karpatne, A.; Atluri, G.; Faghmous, J.H.; Steinbach, M.; Banerjee, A.; Ganguly, A.; Shekhar, S.; Samatova, N.; Kumar, V. Theoryguided data science: A new paradigm for scientific discovery from data. _IEEE Trans. Knowl. Data Eng._ **2017** , _29_ , 2318–2331. [CrossRef] 

22. Fang, Y.; Qian, H.; Chen, J.; Xu, H. Characteristics of spatial-temporal evolution of meteorological drought in the Ningxia Hui Autonomous Region of Northwest China. _Water_ **2018** , _10_ , 992. [CrossRef] 

23. Didan, K. _MODIS/Terra Vegetation Indices 16-Day L3 Global 500m SIN Grid V061 [Data Set]_ ; NASA Land Processes Distributed Active Archive Center: Sioux Falls, SD, USA, 2021. [CrossRef] 

24. Wan, Z.; Hook, S.; Hulley, G. _MODIS/Terra Land Surface Temperature/Emissivity 8-Day L3 Global 1km SIN Grid V061 [Data Set]_ ; NASA Land Processes Distributed Active Archive Center: Sioux Falls, SD, USA, 2021. [CrossRef] 

25. Tirivarombo, S.O.D.E.; Osupile, D.; Eliasson, P. Drought monitoring and analysis: Standardised precipitation evapotranspiration index (SPEI) and standardised precipitation index (SPI). _Phys. Chem. Earth_ **2018** , _106_ , 1–10. [CrossRef] 

26. Landerer, F.W.; Swenson, S.C. Accuracy of scaled GRACE terrestrial water storage estimates. _Water Resour. Res._ **2012** , _48_ , W04531. [CrossRef] 

27. Entekhabi, D.; Njoku, E.G.; O’Neill, P.E.; Kellogg, K.H.; Crow, W.T.; Edelstein, W.N.; Entin, J.K.; Goodman, S.D.; Jackson, T.J.; Johnson, J.; et al. The Soil Moisture Active Passive (SMAP) mission. _Proc. IEEE_ **2010** , _98_ , 704–716. [CrossRef] 

28. Rodell, M.; Houser, P.R.; Jambor, U.; Gottschalck, J.; Mitchell, K.; Meng, C.-J.; Arsenault, K.; Cosgrove, B.; Radakovich, J.; Bosilovich, M.; et al. The Global Land Data Assimilation System. _Bull. Am. Meteorol. Soc._ **2004** , _85_ , 381–394. [CrossRef] 

29. Harris, I.; Jones, P.D.; Osborn, T.J.; Lister, D.H. Updated high-resolution grids of monthly climatic observations—The CRU TS3.10 Dataset. _Int. J. Climatol._ **2014** , _34_ , 623–642. [CrossRef] 

30. Gao, B.C. NDWI—A normalized difference water index for remote sensing of vegetation liquid water from space. _Remote Sens. Environ._ **1996** , _58_ , 257–266. [CrossRef] 

31. Li, F.; Kusche, J.; Chao, N.; Wang, Z.; Löcher, A. Long-term (1979-present) total water storage anomalies over the global land derived by reconstructing GRACE data. _Geophys. Res. Lett._ **2021** , _48_ , e2021GL093492. [CrossRef] 

_Water_ **2025** , _17_ , 2740 

18 of 18 

32. Bao, C.; Zou, J. Analysis of spatiotemporal changes of the human-water relationship using water resources constraint intensity index in Northwest China. _Ecol. Indic._ **2018** , _84_ , 119–129. [CrossRef] 

33. Watson, G.S. Linear least squares regression. _Ann. Math. Stat._ **1967** , 1679–1699. [CrossRef] 

34. Naresh Kumar, M.; Murthy, C.S.; Sesha Sai, M.V.R.; Roy, P.S. On the use of Standardized Precipitation Index (SPI) for drought intensity assessment. _Meteorol. Appl._ **2009** , _16_ , 381–389. [CrossRef] 

35. Beguería, S.; Vicente-Serrano, S.M.; Reig, F.; Latorre, B. Standardized precipitation evapotranspiration index (SPEI) revisited: Parameter fitting, evapotranspiration models, tools, datasets and drought monitoring. _Int. J. Climatol._ **2014** , _34_ , 3001–3023. [CrossRef] 

36. Bento, V.A.; Gouveia, C.M.; DaCamara, C.C.; Trigo, I.F. A climatological assessment of drought impact on vegetation health index. _Agric. For. Meteorol._ **2018** , _259_ , 286–295. [CrossRef] 

37. Graves, A. Long short-term memory. In _Supervised Sequence Labelling with Recurrent Neural Networks_ ; Springer: Berlin/Heidelberg, Germany, 2012; pp. 37–45. 

38. Chai, T.; Draxler, R.R. Root mean square error (RMSE) or mean absolute error (MAE). _Geosci. Model Dev. Discuss._ **2014** , _7_ , 1525–1534. 

**Disclaimer/Publisher’s Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content. 

