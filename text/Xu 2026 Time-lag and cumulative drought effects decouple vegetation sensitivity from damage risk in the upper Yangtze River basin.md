Ecological Indicators 185 (2026) 114739 



Contents lists available at ScienceDirect 

# Ecological Indicators 

journal homepage: www.elsevier.com/locate/ecolind 



## Time-lag and cumulative drought effects decouple vegetation sensitivity from damage risk in the upper Yangtze River basin 



Xiaoxiang Xu<sup>a,b</sup> , Quanzhi Yuan<sup>a,b,*</sup> , Pan Zhao<sup>a,b</sup> , Luping Jia<sup>a,b</sup> , Ping Ren<sup>a,c</sup> 

a _Institute of Geography and Resources Science, Sichuan Normal University, Chengdu 610101, China_ 

b _Sustainable Development Research Center of Resource and Environment of Western Sichuan, Sichuan Normal University, Chengdu 610101, China_ c _Key Lab of Land Resources Evaluation and Monitoring in Southwest, Ministry of Education, Sichuan Normal University, Chengdu 610066, China_ 

|A R T I C L E I N F O|A B S T R A C T|
|---|---|
|_Keywords:_<br>Drought<br>Vegetation<br>Copula-Bayesian framework<br>Upper Yangtze River basin|Increasingly frequent drought events posed significant threats to vegetation stability in the ecologically sensitive<br>upper Yangtze River basin. This study systematically analyzed vegetation response characteristics to drought<br>based on NDVI and multi-scale SPEI data from 1990 to 2022, and developed an integrated drought sensitivity<br>index that incorporated both response magnitude and temporal scales, and quantified vegetation loss risks under<br>varying drought intensities using a Copula-Bayes framework. The results showed that: (1) Vegetation responses<br>to drought exhibited marked spatial and temporal heterogeneity, with cumulative effects dominating across the<br>basin and average response periods ranging from 5 to 8 months. (2) Drought sensitivity demonstrated a bimodal<br>pattern, with higher sensitivity observed at both the arid and humid ends of the moisture gradient, while some<br>humid regions,particularly forest and grassland areas also showed unexpectedly high sensitivity. (3) Under<br>drought scenarios, the likelihood of slight vegetation loss is relatively high, while severe loss remains low overall.<br>The risk of loss differs markedly across regions and vegetation types, and drought sensitivity does not fully align<br>with actual loss probability. Moreover, this study offers methodological and conceptual insights for future<br>research on vegetation–climate interactions, drought risk assessment, and ecosystem resilience under changing<br>climate conditions.Our findings reveal the nonlinear responses of ecosystems to extreme drought and provide a<br>quantitative framework for assessing vegetation sensitivity and loss risk under extreme drought conditions in<br>regions with atypical drought characteristics.|



### **1. Introduction** 

Drought is a natural disaster triggered by prolonged water scarcity and uneven spatiotemporal water distribution. As one of the most frequent and destructive global hazards, it features high frequency, long persistence, and broad spatial coverage (Mishra and Singh, 2010; Wilhite and Glantz, 1985). Meteorological drought, the precursor to agricultural and hydrological droughts, has complex ecological impacts. It can lead to direct consequences such as forest fires and crop reduction, or it can indirectly affect the stability of terrestrial ecosystems by altering vegetation dynamics (Weng et al., 2023; Stahl et al., 2016). The increasing severity of droughts has become a major environmental stressor for terrestrial ecosystems. 

Vegetation is a core component of terrestrial ecosystems, and serves a vital function in energy exchange, carbon cycling, and water regulation (Ming et al., 2025; Chen et al., 2023). In the face of drought stress, 

vegetation survives by closing stomata, decreasing photosynthetic rate, and accumulating antioxidants (Bashir et al., 2021; Zhang et al., 2024), but persistent drought suppresses metabolic activities and ultimately leads to vegetation death (Itam et al., 2020). Studies have shown that large-scale vegetation die-off not only weakens the carbon sink capacity of ecosystems, but also reduces surface evapotranspiration and lowers local air humidity, which reduces precipitation, increases surface temperatures, and further exacerbates drought conditions (Feldman et al., 2023; Duveiller et al., 2018; Bright et al., 2017). As global warming and precipitation patterns change, the interactions between vegetation and drought will also become more complex (Ji et al., 2024; Wang et al., 2025b). 

Understanding the response mechanisms and feedback processes of vegetation to drought is key to comprehending their coupled relationship. Temporal effects are a key feature of these vegetation-drought interactions, primarily manifesting as the Lag Effect of Drought (LED) 

* Corresponding author. 

_E-mail address:_ yuanqz@sicnu.edu.cn (Q. Yuan). 

https://doi.org/10.1016/j.ecolind.2026.114739 

Received 6 September 2025; Received in revised form 23 February 2026; Accepted 26 February 2026 

Available online 6 March 2026 

1470-160X/© 2026 The Author(s). Published by Elsevier Ltd. This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/ ). 

_Ecological Indicators 185 (2026) 114739_ 

_X. Xu et al._ 

and the Cumulative Effect of Drought (CED) (Dikshit et al., 2021; Zhou et al., 2022a). These two effects indicate that the response of vegetation to drought is not instantaneous but instead possesses distinct temporal and cumulative characteristics (Sun et al., 2016; Vilonen et al., 2022). The concept of LED was first introduced by McDowell et al. (2008), whose core idea is that vegetation cannot recover immediately after a drought has ended. Especially after a high-intensity drought, the recovery process can last for months or even years. The magnitude of LED is primarily influenced by vegetation type, drought severity, and local environmental conditions (Bevacqua et al., 2024). In contrast, the Cumulative Effect of Drought (CED), introduced by Vicente-Serrano et al. (2013), underscores the compounding impacts of repeated or prolonged drought events. Rather than isolated responses, CED reflects the progressive degradation of vegetation resilience over time. This deterioration is mainly attributed to persistent water deficits that cause lasting damage to soil properties and plant physiological functions—for example, soil structure deterioration, reduced microbial activity, and impairment of root systems (Porcel and Ruiz-Lozano, 2004; Itter et al., 2019). 

Despite substantial progress in understanding vegetation–drought interactions, important gaps remain. First, most existing studies emphasize drought responses in arid and semi-arid ecosystems (Jha et al., 2019; Deng et al., 2020), while the sensitivity and response mechanisms of vegetation in semi-humid and humid regions are still insufficiently explored across full moisture gradients. Second, drought temporal effects are often examined separately (Zhou et al., 2022b; Zhang and Zhang, 2019), with lag effects (LED) and cumulative effects (CED) rarely integrated into a unified sensitivity framework that jointly considers response magnitude and response timescale. Third, vegetation sensitivity assessments are not consistently connected to probabilistic vegetation loss risk under varying drought intensities; moreover, drought indices optimized by temporal scaling are seldom incorporated into copula-based risk quantification. Consequently, several critical questions remain insufficiently addressed: (1) What are the scaledependent differences and spatial patterns of vegetation responses to drought over time (particularly lag effects and cumulative effects) across distinct moisture gradients? (2) How do these temporal effects collectively shape the spatial distribution of regional vegetation drought sensitivity? (3) How does the risk of vegetation loss under mild, moderate, and severe drought scenarios change when drought indices optimized by temporal scaling are incorporated into probabilistic models? 

The upper Yangtze River Basin (UYRB) is a pivotal ecological barrier and water-conservation region in China, characterized by strong monsoon seasonality and pronounced hydroclimatic gradients. In recent decades, drought hazards in the basin have become increasingly frequent and complex, involving multiple drought types with distinct onset features and driving mechanisms(Wang et al., 2026). These intensifying droughts have been accompanied by high-impact extreme events, including the record-breaking compound hot–dry episode in Southwest China, particularly in the Sichuan–Chongqing region, during the summer of 2006, and the unprecedented summer–autumn drought in 2022, widely recognized as the most severe in the Yangtze Basin since 1961 (Wu et al., 2023). Observations and assessments indicate that these events caused substantial water-storage deficits and heightened ecohydrological stress, underscoring the escalating risks to regional ecosystems and associated ecosystem services (Duan et al., 2024). Against this backdrop, it is crucial to move beyond “synchronous” drought–vegetation matching and systematically quantify vegetation drought response mechanisms across temporally relevant scales (including lag and cumulative processes), and then translate these response diagnostics into scenario-based probabilities of vegetation loss to identify ecologically fragile and high-risk areas and inform climateadaptive ecosystem management in the UYRB. 

Therefore, this study aims to achieve the following specific objectives: (1) To characterize the spatiotemporal patterns of drought timelag and cumulative effects on vegetation. (2) To assess the drought 

sensitivity of major vegetation types along key hydroclimatic gradients. (3) To quantify the probability of drought-induced vegetation loss under different drought intensities to assess vegetation vulnerability. The results will support ecosystem conservation and climate-adaptive management in the basin. 

### **2. Materials and methods** 

### _2.1. Research area_ 

The upper Yangtze River Basin is located in southwestern China, spanning from 90<sup>◦</sup> 32′ E to 111<sup>◦</sup> 27′ E longitude and 24<sup>◦</sup> 27′ N to 35<sup>◦</sup> 45′ N latitude (Fig. 1). The region encompasses the first and second tiers of China's topographic ladder and features a complex topography comprising diverse geomorphological units, such as plateaus, mountains, arid-hot valleys, and large intermontane basins (Wang et al., 2013). Except for the headwater region, which is characterized by a highland mountain climate, most of the basin experiences a subtropical monsoon climate. Both temperature and precipitation exhibit significant spatial heterogeneity, showing a general decreasing gradient from the southeast to the northwest (Yang and Xing, 2022). It can be classified into four distinct moisture zones based on the aridity index. This climatic gradient strongly influences land cover distribution: arable land and forests are predominantly concentrated in the humid and semihumid zones, whereas shrublands and grasslands are mainly distributed in the semi-arid and arid zones of the western part of the basin **(** Qu et al., 2018 **)** . 

### _2.2. Data sources_ 

### _2.2.1. Ancillary data_ 

Table 1 shows all data types and sources. To ensure temporal consistency and comparability across different datasets, the period from 1990 to 2022 was uniformly selected as the study timeframe. The Normalized Difference Vegetation Index (NDVI) were obtained from the third-generation Global Inventory Modeling and Mapping Studies (GIMMS 3G+), with an original spatial resolution of 1/12<sup>◦</sup> and a temporal resolution of 15 days (Pinzon et al., 2023). It were aggregated to a monthly scale using the Maximum Value Composite (MVC) method and subsequently resampled to a uniform 5 km resolution via cubic convolution interpolation. Meteorological data included a 1 km resolution monthly mean precipitation dataset (1901–2024) and a monthly potential evapotranspiration (PET) dataset (1901–2024) for China. The PET dataset was derived using the Hargreaves potential evapotranspiration equation (Peng, 2020). For consistency with the study period, we extracted and used the 1990–2022 subset from both products in all analyses. The aridity index (AI) dataset was calculated based on the widely adopted United Nations Environment Programme (UNEP) definition, expressed as the ratio of multi-year mean annual precipitation to multi-year mean annual potential evapotranspiration. According to the AI values, the study area was classified into four climate humidity zones (Yao et al., 2023): humid (AI _>_ 0.65), semi-humid (0.5 _<_ AI ≤0.65), semi-arid (0.2 _<_ AI ≤0.5), and arid (AI _<_ 0.2). All meteorological and AI data were resampled to a 5 km spatial resolution using the bilinear interpolation method. To focus on long-term vegetation dynamics, land use data (1990–2022) were processed by retaining only pixels where land cover type remained unchanged throughout the study period. The spatial resolution was aggregated from 30 m to 5 km using a majority filter. 

### _2.2.2. Meteorological data and SPEI calculation_ 

Although the global SPEI database offers long-term drought monitoring data, its coarse spatial resolution limits its applicability for regional-scale assessments. Therefore, this study recalculated the Standardized Precipitation Evapotranspiration Index (SPEI) at a higher resolution. Following the methodology of Vicente-Serrano et al. (2010), the 

2 

_X. Xu et al.                                                                                                                                                                                                                                       Ecological Indicators 185 (2026) 114739_ 



**Fig. 1.** Study Area. 

**Table 1** 

Data types and sources. 

|Data|Spatial<br>resolution|Temporal<br>resolution|Data Sources|
|---|---|---|---|
|NDVI data<br>(1982–2022)|1/12<sup>◦</sup>×1/<br>12<sup>◦</sup>|15 day|NASA<br>(https://daac.ornl.<br>gov/VEGETATI<br>ON/guides)<br>Resource and<br>Environment|
|Land use data<br>(1990–2022)|30 m× 30<br>m|year|Science and Data<br>Center<br>(http://www.resdc.<br>cn)|
|Aridity Index data<br>(1901–2024)|1 km×1<br>km|Year|TPDC (https://data.<br>tpdc.ac.cn/zh-h<br>ans/data)|
|Precipitation data<br>(1901–2024)|1 km×1<br>km|month|TPDC (https://data.<br>tpdc.ac.cn/zh-h<br>ans/data)|
|PotentialEvapotranspiration<br>(1901-2024)|1 km×1<br>km|month|TPDC (https://data.<br>tpdc.ac.cn/zh-h<br>ans/data)|
||||Chinese Academy|
|DEM data|30 m|Year|of Sciences (htt<br>p://www.gscloud.<br>cn)|



SPEI was calculated using the gma package in Python. The calculation formulas are as follows: 

Monthly precipitation ( _Pt_ ) and potential evapotranspiration ( _PETt_ ) were first used to derive the monthly climatic water balance: _Dt_ = _Pt_ − _PETt_ (1) 

To characterize drought conditions at multiple temporal scales, the accumulated water balance at timescale _k_ (months) was computed as: 



For each timescale _k_ , the series _D_<sup>(</sup><sup>_k_)</sup> was fitted with a three-parameter log-logistic probability distribution, and the cumulative probability was obtained as _Fk_ ( _D_<sup>(</sup> _t_<sup>_k_)</sup> ). The SPEI was then derived by transforming this cumulative probability into a standard normal variate: _SPEI_<sup>(</sup> _t_<sup>_k_)</sup> = Φ<sup>−1(</sup> _Fk_ ( _D_<sup>(</sup> _t_<sup>_k_)</sup> ) ) (3) 

where _Φ_<sup>−1</sup> ( _._ )denotes the inverse cumulative distribution function of the standard normal distribution. The above procedure yields monthly SPEI at 12 timescales (1–12 months). A normal standardization procedure was applied to ensure comparability across time scales, and all meteorological variables and derived SPEI products were resampled to a final spatial resolution of 5 km. Drought intensity was classified based on commonly adopted SPEI thresholds (Vicente-Serrano et al., 2010): Mild drought (− 1.0 _<_ SPEI _<_ − 0.5); Moderate drought (− 1.5 _<_ SPEI ≤− 1.0); Severe drought (− 2.0 _<_ SPEI ≤− 1.5); Extreme drought (SPEI ≤− 2.0). 

3 

_Ecological Indicators 185 (2026) 114739_ 

_X. Xu et al._ 

The SPEI can reflect drought intensity at different time scales. 

### _2.3. Methodology_ 

### _2.3.1. Calculation of lag and accumulative effects_ 

To assess drought lag effects, Pearson correlation coefficients were computed between monthly NDVI and 1-month SPEI values from preceding i months _(1_ ≤ _i_ ≤ _12)_ at each pixel, with a significance threshold of 0.05. 







Here, _NDVIt_ represents the NDVI value in month _t_ , and _SPEI_<sup>(</sup> _t_ −<sup>1)</sup> _τ_<sup>de-</sup> notes the 1-month SPEI value occurring _τ_ months prior to _NDVIt_ . The term _Corr_ ( _NDVItSPEI_<sup>(</sup> _t_ −<sup>1)</sup> _τ_ ) refers to the Pearson correlation coefficient between NDVI and the SPEI at a lag of _τ_ months, while _rlag_ ( _τ_ ) denotes the set of 12 lagged correlation coefficients calculated for each pixel at lag times _τ_ = _1, …,12_ . The parameter _τ_<sup>*</sup> represents the optimal lag time scale, defined as the lag at which the absolute value of _rlag_ ( _τ_ ) reaches its maximum. Accordingly, _Tlag_ represents the optimal lagged response time, and _Rlag_ represents the maximum correlation coefficient corresponding to the optimal lag time scale. For example, if the NDVI in October has the strongest correlation with the 1-month SPEI in May, then the optimal lag time _Tlag_ is four months. 

To assess drought cumulative effects, SPEI values accumulated over 1–12 months (replacing 1-month SPEI) were correlated with NDVI using Pearson's method at each pixel ( _p_ = 0.05). 



_k_<sup>*</sup> = argmax| _racc_ ( _k_ ) | _, k_ ∈{1 _,_ 2 _,_ 3 _..._ 12} (8) 



Here, _SPEI_<sup>(</sup> _t_<sup>_k_)</sup> denotes the k-month SPEI in month _t_ , calculated from the climatic water balance accumulated over the preceding k months. The term _Corr_ ( _NDVIt, SPEI_<sup>(</sup> _t_<sup>_k_)</sup> ) refers to the Pearson correlation coefficient between the NDVI in month t and the k-month SPEI. The variable _k_ represents the SPEI time scale and ranges from 1 to 12 months. _Tacc_ denotes the optimal cumulative response time, and _Racc_ is the maximum correlation coefficient corresponding to that optimal cumulative scale. For example, if the NDVI in October exhibits the strongest correlation with the 5-month SPEI, the optimal cumulative time _Tacc_ is determined to be 5 months. 

### _2.3.2. Drought sensitivity of different vegetation types_ 

The sensitivity of vegetation to drought can be characterized along two dimensions: response magnitude ( _Racc_ and _Rlag_ ) or response timing ( _Tacc_ and _Tlag_ ). Highly drought-sensitive vegetation types typically exhibit lower _T_ acc and _T_ lag values, indicating faster responses to preceding drought events and greater sensitivity to short-term water stress. Moreover, previous studies have also shown that the magnitude and duration of vegetation responses to both recent and long-term droughts are often correlated (Peng et al., 2019). Based on the concepts of cumulative and lagged effects, a composite index was developed to quantify the drought sensitivity across different vegetation types (Xu et al., 2021). 



cumulative time ( _NTacc_ ), normalized lag time ( _NTlag_ ), cumulative effect correlation ( _Racc_ ), and lag effect correlation ( _Rlag_ ). All four indicators were standardized by the minimum-maximum scaling method. The Jenks natural breaks method was adopted to classify the drought sensitivity index (DS) into five categories, reflecting natural groupings inherent in the data. This approach allows for a more objective and representative identification of regions with varying sensitivity levels. DS was categorized into five sensitivity levels: very low (0–0.15), low (0.15–0.3), medium (0.3–0.6), high (0.6–0.8), and very high sensitivity (0.8–1). 

### _2.3.3. Copula_ – _bayes method for calculating vegetation loss probability_ 

The Copula function is a multivariate joint distribution function that links marginal distributions through a function defined on the [0,1] interval. Any multivariate cumulative distribution function can be decomposed into its corresponding marginal distributions and an appropriate Copula function. This approach has been widely applied in meteorology and hydrology, and is increasingly being used in vegetation damage risk assessment. Based on this method, we developed a probabilistic framework to assess vegetation damage risk under different drought scenarios, incorporating both lag and cumulative effects of water stress. 



Here we have previously determined the response time under cumulative and time-lag effects ( _p <_ 0.05), and _SPEIR_ denotes the cumulative or lagged drought value corresponding to the identified optimal time scale. _FSPEIR,NDVI_ stands for the joint distribution function of SPEI and NDVI, and C() stands for the Copula function of the optimal fit on each pixel of the present study, and _FSPEIR_ denotes the marginal distribution function of SPEI, and _FNDVI_ denotes the marginal distribution function of NDVI. Six common Copula functions (Gaussian, Clayton, Frank, Gumbel, Student-t, Joe) were chosen to construct the joint distribution of SPEI and NDVI. For model selection, the Kolmogorov–Smirnov (K–S) test was first applied to evaluate the goodness-of-fit of each Copula model. Then, Root Mean Square Error (RMSE), Akaike Information Criterion (AIC), and Bayesian Information Criterion (BIC) were used for further comparison and model optimization. Regarding marginal distributions, Generalized Extreme Value (GEV), Normal (NORM), Gamma (GAM), and Log-Normal (LOGN) distributions were used to fit the NDVI time series. Given that SPEI is derived from a standardized distribution, the Normal distribution was selected to fit the SPEI series. Final marginal distributions were selected based on K–S test results and the minimum RMSE criterion. The selected Copula functions were then combined with Bayes'conditional probability formula to estimate vegetation loss probability under four levels of drought stress. The vegetation loss was categorized into three levels of severity: slight, moderate, and severe loss. Previous studies have shown that determining vegetation loss based on percentile thresholds is more accurate than using _Z_ -scores, and using NDVI percentiles rather than absolute values is a widely adopted way to define vegetation stress or loss across heterogeneous regions and vegetation types (Han et al., 2023; Wang et al., 2022). This study focuses on NDVI values below the 40th, 30th and 10th percentiles. These thresholds(40th, 30th, 10th)represent a reasonable and widely used severity ladder (mild–moderate–tail extreme) that is both ecologically meaningful and statistically estimable at the pixel scale (Fig. S1). The conditional probability formula applied in this study is as follows: 





Drought sensitivity (DS) is quantified through normalized 

4 

_Ecological Indicators 185 (2026) 114739_ 

_X. Xu et al.                                                                                                                                                                                                                                       Ecological Indicators_ 

### **3. Results** 

**Table 2** 

**.** Maximum Cumulative Response Time of Different Vegetation Types. 

### _3.1. Cumulative effects of drought on vegetation_ 

The result showed 65.4% of the vegetation-covered regions within the basin displayed a statistically significant correlation ( _p < 0.05_ ), indicating a widespread cumulative drought effect (Fig.2a). Specifically, 48.1% of the areas in the basin showed significant positive correlations, and such areas were mainly concentrated in the east and southeast, especially in the Sichuan Basin and Guizhou Plateau, where the correlation coefficients usually fell within the range of 0.2 to 0.5. In contrast, areas exhibiting a significant negative correlation, indicative of droughtinduced stress, covered approximately 17.3% of the basin. These were primarily distributed in the Hengduan Mountains and Liangshan Canyon regions, with strong negative correlations ranging from − 0.3 to − 0.5. From a temporal perspective, the optimal cumulative timescales varied considerably across the study area (Fig.2b). Short-term cumulative effects (1–4 months) were dominant in 42.4% of the basin, primarily in the Hengduan Mountains, Hanzhong Basin, and Yunnan Plateau. Conversely, long-term cumulative effects (10–12 months) were observed in 40.5% of the area, mainly in the Sichuan Basin. Among these, 12-month timescale had the largest spatial extent, covering nearly 30% of the total vegetated area. 

The average cumulative responses duration of the major vegetation categories to drought exhibited an increasing trend along the moisture gradient,indicating that under more favorable moisture conditions, vegetation required a longer accumulation period before responding to drought. Meanwhile, from arid to semi-humid regions, cropland, forest, and shrubland within different ecological zones showed pronounced gradient variations in their drought response characteristics (Fig.2c-2f). This gradient was reflected in two key aspects: the correlation coefficient between vegetation and cumulative drought showed a declining trend, while the cumulative response time increased accordingly. Additionally, it was observed that higher correlation coefficients were 

|Vegetation<br>types|Arid|Semi-<br>arid|sub-<br>humid|Humid|Whole<br>region|
|---|---|---|---|---|---|
|Cropland|4.2±<br>2.3|4.8±<br>2.8|7.2± 3.9|9.1±<br>3.6|8.1±3.8|
|Forest|3.9±<br>2.1|5.7±<br>3.6|6.1± 4.2|8.2±<br>2.4|6.8±4.4|
|Shrub|4.1±<br>2.3|5.0±<br>3.2|6.6± 3.1|8.3±<br>2.4|6.3±4.2|
|G|5.2±|5.4±|55±41|5.6±|53±41|
|rass|3.8|4.1|. .|3.5|..|
|l|4.3±|5.9±||7.6±||
|Tota|2.9|3.8|6.4± 4.1|4.3|6.8±4.2|



often associated with shorter cumulative response times, suggesting that strong vegetation responses to drought were often accompanied by rapid feedback processes. From the perspective of vegetation types (Table 2), grassland showed the most sensitive and rapid reaction to cumulative drought, the mean response time being 5.3 ± 4.1 months.This was followed by shrubland at 6.8 ± 4.2 months, while cropland showed the slowest response, with an average time of 8.1 ± 3.8 months. Across different bioclimatic zones, vegetation in arid areas responded most quickly to cumulative drought, with an average response time of 4.3 ± 2.9 months; arid-zone forests, in particular, responded within just 3.9 ± 2.1 months on average. Notably, in grassland ecosystems within semihumid and humid regions, the response time to cumulative drought remained short, generally around 5 months, despite the relatively moist climatic background. In contrast, cropland responses in semi-humid and humid areas were the slowest, with average response times of approximately 7 months and 9 months, respectively. 



**Fig. 2.** Vegetation response to cumulative drought effects: (a) response time (months), (b) maximum correlation coefficient (c)Cumulative drought response gradient of Cropland ( _d_ )Cumulative drought response gradient of Forst ( _e_ )Cumulative drought response gradient of Shrub (f)Cumulative drought response gradient of grass. Error bars and dots indicate one standard deviation and mean values, respectively. 

5 

_Ecological Indicators 185 (2026) 114739_ 



**Fig. 3.** Vegetation response to lag drought effects: (a) response time (months), (b) maximum correlation coefficient( _c_ )Lagged drought response gradient of Cropland ( _d_ )Lagged drought response gradient of Forest( _e_ )Lagged drought response gradient of Shrub( _f_ )Lagged drought response gradient of Grass.Error bars and dots indicate one standard deviation and mean values, respectively. 

### _3.2. Lag effects of drought on vegetation_ 

Compared to the cumulative effects, the lag effects of drought on vegetation within the study basin were spatially less extensive and characterized by shorter response times(Fig. 3). As shown in Fig. 3a, a significant lag correlation ( _p < 0.05_ ) was observed in approximately 28.4% of the study area. The correlation was predominantly positive, signifying that antecedent drought conditions exerted a delayed promotional effect on subsequent vegetation growth, possibly due to factors like enhanced radiation. These regions were mainly distributed in the Sichuan hilly, the central mountain gorge area of western Yunnan, and the mountainous gorge zone of the Dalou Mountains, with the average maximum lag correlation coefficient being approximately 0.15. From a temporal perspective, vegetation across the basin generally exhibited short lag responses to drought, with optimal lag times concentrated within 1–3 months(Fig.3b). These short-term response regions made up 49.8% of the significantly affected regions and with their distribution focusing mainly on the central Sichuan Basin and its surrounding hilly areas, and the Yunnan Plateau. In contrast, areas with longer lag times 

**Table 3** 

Maximum Lag Response Time of Different Vegetation Types. 

|Vegetation<br>types|Arid|Semi-<br>arid|sub-<br>humid|Humid|Whole<br>region|
|---|---|---|---|---|---|
|Cropland|2.6±<br>1.1|2.3±<br>1.2|2.2± 1.3|4.2±<br>2.2|3.5±3.1|
|Forest|2.7±<br>1.3|3.9±<br>2.1|3.5± 2.3|5.1±<br>2.5|4.7±3.6|
|Shrub|2.6±<br>1.0|2.7±<br>1.3|3.4± 2.5|5.3±<br>2.8|4.1±3.6|
|Grass|4.4±<br>2.9|4.9±<br>2.9|4.6± 2.6|4.1±<br>2.5|4.6±3.7|
|Total|4.3±<br>3.8|4.3±<br>3.7|3.5± 3.6|4.8±<br>3.4|4.5±3.6|



(9–12 months) were relatively limited, comprising only 15.7% of the basin, and were primarily found in ecological transition zones such as the northwestern Sichuan Plateau broad-valley region and the Dalou Mountain gorge region. Notably, along the Tanggula Mountains to the Tongtian River Basin, where large elevation gradients and fragmented terrain support a mosaic of vegetation types the lag response times were highly variable. 

Distinct response patterns were observed for lag effects compared to cumulative effects. Table 3 presented that as water availability increased from arid to humid zones, the average lag time for vegetation response remained relatively consistent and short, at approximately 4 months. An exception was the semi-humid region, where vegetation responded slightly faster, with an average lag time of around 3 months. Regarding vegetation categories, forests (4.7 ± 3.6 months), grasslands (4.6 ± 3.7 months), and shrublands (4.1 ± 3.6 months) had similar lag response times, whereas croplands responded significantly faster, with a lag time of 3.5 ± 3.1 months. Vegetation responses also varied significantly across different bioclimatic zones (Fig.3c-3f). In arid, semi-arid, and semi-humid regions, croplands showed lag times of approximately 2 months, which increased to 4 months in humid regions. Forests and shrublands also exhibited a short response time and high response intensity in arid zones, whereas arid zones in humid regions demonstrated a relatively delayed response to drought. Conversely, the response pattern of grasslands showed little variation across the moisture gradient. However, the response time in humid areas was shorter and the response intensity was higher compared to other zones. 

### _3.3. Drought sensitivity of vegetation_ 

Within the upper Yangtze River Basin, the drought sensitivity of vegetation exhibited significant spatial heterogeneity, with clear gradations observed across different ecological and geographical units. As depicted in Fig. 4a, areas of extremely high sensitivity and high sensitivity were mainly concentrated in the Hengduan Mountains, Qionglai 

6 

_Ecological Indicators 185 (2026) 114739_ 

_X. Xu et al._ 



**Fig. 4.** Spatial Variation and Proportion of Vegetation Sensitivity to Drought. 

Mountains, and the alpine gorge regions of the Liangshan area. In contrast, the Tongtianhe region of the Tibetan Plateau showed relatively low drought sensitivity. An analysis of sensitivity across bioclimatic zones revealed a general decreasing trend from drier to wetter regions. That is, vegetation systems in arid areas tended to exhibit higher overall sensitivity, while those in humid zones showed relatively lower sensitivity. Specifically, Fig. 4b shows that the proportion of high-sensitivity areas reached 37% and 34% in arid and semi-arid zones, respectively. This proportion dropped to 26% in semi-humid zones and 24% in humid zones. In terms of mean sensitivity values, arid zones averaged 0.54 and semi-arid zones 0.56, whereas semi-humid and humid zones averaged 0.43 and 0.47, respectively. This pattern confirms a general decline in sensitivity from arid to semi-humid areas. It is noteworthy, however, that highly sensitive vegetation responses to drought could also occur in humid regions. 

Among the major vegetation types(fig.4c), a substantial proportion of each type was classified as highly sensitive, with all exceeding 20%. Shrub exhibited the highest proportion of high-sensitivity areas (30%), followed by grasslands (28%). Croplands showed the lowest proportion, at approximately 21%. Further analysis of mean drought sensitivity across vegetation types, as illustrated in Fig. 5, indicates that cropland, forest, shrubland, and grassland all displayed a common pattern across the moisture gradient: sensitivity increased as moisture availability decreased. That is, as the environment transitioned from semi-humid to arid zones, the mean drought sensitivity of all vegetation types increased accordingly. Notably, the mean sensitivity of forests was higher in humid areas (0.48) than in semi-humid areas (0.41). Furthermore, grasslands in humid regions showed an even higher mean sensitivity (0.55), surpassing that of grasslands in arid zones (0.52). This finding further demonstrates that, in addition to arid zones, vegetation in some humid regions can also exhibit high sensitivity to drought. 

under four drought scenarios, the results showed that as the severity of drought increased, the probability and range of vegetation damage also increased.For slight vegetation damage, the probability of occurrence under mild drought conditions was generally between 34% and 52%, and this ranged from 37% to 59% under moderate drought. Under severe and extreme drought scenarios, the damage probability increased rapidly to over 80% in several regions, including the low mountains and hills of eastern Sichuan, the broad valleys of central Sichuan, the Qinling and Daba Mountains in the north, the Miaoling Mountains in the southeast, and the Jiangyuan Plateau in the northwest. For moderate vegetation damage, the probability was notably higher only under extreme drought, whereas under mild, moderate, and severe drought, the occurrence probability remained mostly between 30% and 40%. The risk of severe vegetation damage was relatively low across the basin. The average trigger probability was approximately 6.5% under mild drought and only rose to about 19.1% under extreme drought. Overall, vegetation in the southwestern part of the basin, including the Hengduan Mountains and the Yunnan Plateau, had a lower probability of damage across all severity levels and drought scenarios. In contrast, vegetation in eastern Sichuan Basin and northwestern Qinghai-Tibet Plateau was more likely to experience higher damage probabilities when facing drought stress. 

Given that slight vegetation damage was the most prevalent response to drought stress, this damage level was selected for a more detailed risk analysis across different vegetation types and ecological zones (Fig.7). Forests and shrubs in environments with either significant or minimal water deficit exhibited high sensitivity to drought. Grassland sensitivity to drought intensified along the humidity gradient from wet to dry zones.with the damage probability gradually increasing, indicating a clear gradient of increasing risk in water-limited areas. 

### **4. Discussion** 

_3.4. Vegetation damage risk under drought stress considering temporal effects_ 

Fig. 6 showed the conditional probability of vegetation damage 

### _4.1. Vegetation response to drought considering temporal effects_ 

At the basin scale, our results indicate that vegetation responses to 

7 

_Ecological Indicators 185 (2026) 114739_ 

_X. Xu et al._ 



**Fig. 5.** Sensitivity Gradient Patterns of Four Vegetation Types. 

drought are dominated by cumulative effects. As water availability increases, the average cumulative response time of vegetation to drought shows a clear increasing gradient from arid–semi-arid regions toward humid regions. Similarly, previous studies in the Yellow River Basin have reported that the cumulative impact of drought on vegetation generally intensifies from arid to semi-humid zones (Zhan et al., 2022). Overall, the spatial variation in vegetation response time to drought (including both cumulative and lag times) is largely controlled by the combined effects of climatic water availability, topographic conditions, and soil water-holding capacity. 

In arid regions, vegetation is chronically water-limited, so even mild drought can rapidly deplete the limited soil moisture and trigger immediate physiological responses such as stomatal closure. Consequently, within the NDVI–SPEI framework used in this study, the time required to accumulate a “drought signal” sufficient to induce detectable NDVI changes is relatively short. After drought termination, slow recovery of soil moisture constrains the ability of vegetation to buffer or delay its response, leading to relatively short average lag times as well. In contrast, in humid regions such as the Sichuan Basin, higher soil water buffering capacity allows vegetation to withstand short-term drought by drawing on stored soil moisture; a much longer period of drought accumulation (about 6–12 months) is required to exceed this buffering threshold and cause a marked decline in NDVI. Post-drought recovery in these regions also relies on the gradual replenishment of soil moisture, and the re-establishment of water balance in deep-rooted forest ecosystems in particular, thereby resulting in longer lag times. Moreover, the impact of drought on vegetation in the upper Yangtze River Basin 

varies considerably among vegetation types, with distinct response strategies across functional groups. In general, the mean response time to prolonged drought increases in the order: grassland (5.3 months), shrubland (6.3 months), forest (6.8 months), and cropland (8.1 months). This pattern is likely related to differences in root system architecture, water acquisition strategies, and the degree of human intervention. In arid regions, vegetation typically evolves a suite of strategies to cope with water scarcity by reducing water demand and responding rapidly to drought. These strategies include adjusting cell division and differentiation at root tips, modifying root morphology to enhance water uptake, and downregulating enzyme activity to reduce respiration and slow photosynthesis, thereby lowering overall water requirements (Peguero-Pina et al., 2020; Osakabe et al., 2014). Although croplands are also dominated by shallow-rooted species, their response to drought is often more delayed, likely because agricultural practices—especially irrigation—substantially modulate the immediate effects of meteorological drought(Chen et al., 2025). In particular, in arid and semi-arid regions, irrigated croplands rely on external water sources such as groundwater and reservoirs, which can significantly postpone the onset of drought stress at the vegetation level (Volo et al., 2014). 

### _4.2. Vegetation sensitivity to drought_ 

The IPCC's Fifth Assessment Report defines “sensitivity” as how much a system can handle or struggle against the harmful impacts of climate change, such as shifts in weather patterns and severe weather events (IPCC, 2014). Generally, Vegetation exhibiting stronger drought 

8 

_X. Xu et al.                                                                                                                                                                                                                                       Ecological Indicators 185 (2026) 114739_ 



**Fig. 6.** Vegetation Vulnerability Probabilities under Different Drought Scenarios. 

correlation and quicker reaction times is considered to have a more direct and coupled response, thus indicating greater drought sensitivity. However, some regions exhibit an inconsistency between correlation strength and response time, which may result from multiple factors, including ecological adaptation strategies, hydrological conditions, soil characteristics, and human interventions. This inconsistency limits the effectiveness of single-indicator assessments for regional drought sensitivity (Xu et al., 2021;Yuan et al., 2024). Therefore, this study adopted a dual perspective of cumulative and lag effects to develop a composite sensitivity index that integrates both response amplitude and timescale, providing a more holistic assessment of vegetation drought sensitivity.The research revealed significant spatial heterogeneity in vegetation drought sensitivity, which was constrained by both 

hydroclimatic conditions and vegetation functional composition. From arid to semi-humid zones, vegetation sensitivity to drought showed a decreasing trend. As available water resources increase, the coupling between vegetation and drought weakens; however, moisture-rich humid areas maintained a relatively high sensitivity. Previous studies have likewise emphasized that, although droughts are generally less likely to occur in humid regions, vegetation in these areas tends to exhibit a more pronounced response when drought does occur.(Su et al., 2024; Li et al., 2024). From the perspective of vegetation types, forest ecosystems maintained high sensitivity to drought regardless of climatic moisture conditions. According to the study by Anderegg (2015), the phenomenon of hydraulic imbalance in forest plants not only occurred in typical arid zones but also was prevalent in moist regions with 

9 

_Ecological Indicators 185 (2026) 114739_ 

_X. Xu et al.                                                                                                                                                                                                                                       Ecological Indicators_ 



**Fig. 7.** Gradient pattern of the probability of mild loss occurrence for four vegetation types. 

sufficient water availability. We hypothesize that the pronounced drought sensitivity of vegetation in humid regions, particularly forests, can be primarily explained by two mechanisms.First, forest communities that have developed under long-term conditions of relatively ample water availability often exhibit functional trait syndromes that prioritize growth rather than drought resistance. Such communities typically maintain relatively high stomatal conductance, larger leaf area, and elevated transpiration rates in order to fully exploit abundant water and light and thereby maximize productivity (Grossiord et al., 2020). However, this also implies that once drought occurs, water loss can be greatly amplified. Under ongoing climate warming, increases in vapor pressure deficit (VPD) and air temperature further enhance atmospheric water demand, making these historically water-rich systems more prone to approaching critical thresholds of water stress and thus leading to shorter response times once drought sets in. Second, global warming increases the atmospheric water-holding capacity and potential evapotranspiration, so that a given level of precipitation variability is more readily translated into more extreme anomalies in soil moisture and atmospheric drought. An increasing number of studies have shown that rapid transitions between drought and extreme precipitation (precipitation or hydrological “whiplash”) have become significantly more frequent worldwide, with this enhancement in hydroclimate volatility being particularly pronounced at subseasonal timescales, characterized by rapid switching between extremely dry and extremely wet conditions (Tan et al., 2023; Swain et al., 2025). Such high-frequency, largeamplitude dry–wet alternations disrupt the long-term adaptation of humid-region vegetation to relatively stable moisture regimes and can cause rapid shifts in vegetation growth conditions. 

### _4.3. Decoupling between vegetation drought sensitivity and damage risk_ 

The findings indicated that vegetation in highly sensitive regions 

(the Hengduan Mountains) exhibits a relatively low probability of loss, while vegetation in some moderately and lowly sensitive regions (the Eastern Sichuan Basin, the Guizhou Plateau) shows a significantly higher probability of loss. This reveals a certain “decoupling” phenomenon between drought sensitivity indicators and actual loss risk. Similar decoupling has been reported at the tree and stand scales: several studies have indicated that trees approaching death often exhibit reduced growth sensitivity and resilience to water fluctuations, rather than being more “sensitive” to climatic anomalies (DeSoto et al., 2020; Herrero et al., 2023). Long-term chronic stress and hydraulic damage can weaken their plastic response capacity to climate fluctuations, leading to a state of “low apparent sensitivity but high mortality risk.” This is somewhat consistent with the characteristics of some “low sensitivity–high risk” regions identified in this study. 

In the Hengduan Mountains, the coexistence of high drought sensitivity and low loss probability may be jointly attributed to the regional forest characteristics and complex hydrothermal conditions. On the one hand, the region is dominated by evergreen broad-leaved and coniferous forests, distributed along a distinct altitudinal gradient. Evergreen coniferous forests typically exhibit strong cold and drought tolerance, deep root systems, and conservative water‑carbon utilization strategies, which enhance their stress resistance (Mathias and Thomas, 2021). On the other hand, the Hengduan Mountains are characterized by fragmented terrain and significant topographic relief. Processes such as orographic precipitation, cloud condensation, and valley circulation form multi-scale “microclimatic refuges” locally, which can buffer largescale drought extremes to a certain extent (Hu et al., 2025). Consequently, in this region, NDVI shows a strong coupling with SPEI variations (reflected by high DS index values), while canopy greenness rarely falls into the low percentile range indicating “damage,” resulting in a relatively low probability of vegetation loss.In contrast, the DS values of forests in the Eastern Sichuan Basin and Guizhou Plateau are generally 

10 

_Ecological Indicators 185 (2026) 114739_ 

_X. Xu et al._ 

not prominent, yet their vegetation loss probability exceeds 65% under various drought scenarios, presenting a typical “low sensitivity–high risk” pattern. Existing climate and ecological studies have indicated that these regions are hotspots for compound “drought–heatwaves” and high vapor pressure deficit (VPD) in Southwest China (Wang et al., 2025a). Compound drought–heat events often synergistically exacerbate hydraulic imbalance, carbon starvation, and leaf scorching, leading to significantly greater vegetation damage than expected under single drought scenarios (Xu et al., 2024). Meanwhile, some forests in Southwest China have exhibited a phenomenon of “greening but declining resilience”: despite an overall trend of increasing greenness, the ecosystem's buffering capacity against disturbances and recovery ability have weakened (Jiang et al., 2021). Against this backdrop, even if the intensity of meteorological drought (described by SPEI) is not extreme, the superimposition of high temperature and high VPD may still trigger a substantial decline in NDVI and a high probability of damage. 

It should also be noted that the decoupling phenomenon of “high sensitivity–low loss” and “low sensitivity–high loss” may partly stem from the mathematical and statistical properties of the optimal Copulas themselves, in addition to differences in regional ecological adaptability and compound climatic events such as drought–heatwaves. The DS index is based on the linear correlation and response time between NDVI and SPEI, primarily characterizing the overall coupling intensity; in contrast, the Copula model directly influences the quantitative results of loss probability through its tail dependence structure，where “tail dependence” refers to the degree of deviation between the probability of two variables simultaneously being in extreme states and their overall correlation. Shown as Fig. S2, in regions such as the Eastern Sichuan Basin and Guizhou Plateau, the optimal models are more inclined toward lower tail-dependent Copulas (Clayton Copula), indicating that when SPEI is extremely low, the probability of joint extreme events—where NDVI simultaneously falls into low percentiles—is significantly amplified. In highly sensitive regions like the Hengduan Mountains, the optimal Copulas are mostly approximately symmetric types (Frank, Gaussian Copulas) with weak left-tail dependence. This implies that while NDVI and SPEI fluctuate synergistically in most cases, the probability of their “simultaneous occurrence of extreme low values” is limited. Consequently, these regions exhibit significant responsiveness (high DS values) but relatively few severe loss events, show the “high sensitivity–low loss” pattern. 

### _4.4. Limitations and future perspectives_ 

This study proposes a framework for assessing the drought sensitivity and risk of regional vegetation, but several uncertainties remain. First, vegetation status and productivity were characterized solely using NDVI, which is known to saturate under dense canopies and may be less capable of separating structural changes from physiological regulation during drought, potentially limiting the detection of subtle stress signals (Zhou et al., 2022b). Second, drought conditions were represented by SPEI, which is primarily a meteorological drought index derived from climatic water balance; it may not fully capture root-zone soil moisture deficits and associated ecological drought processes that directly constrain plant water availability, thereby partly underestimating or misrepresenting the actual water stress experienced by vegetation. In addition, several key driving factors and processes have not yet been explicitly incorporated into the analysis.With respect to the mechanisms underlying the spatial patterns of drought sensitivity and loss probability, the present study is mainly based on qualitative analysis, and quantitative attribution remains limited; future studies should employ more advanced models and methods to further elucidate these processes. 

Future research could integrate the multi-source remote sensing indicators (such as the Enhanced Vegetation Index (EVI), Leaf Area Index (LAI), Solar-Induced Chlorophyll Fluorescence (SIF), Gross Primary Productivity (GPP)), high-resolution land cover and biomass data, and 

ground observations (Xu et al., 2023; Lai et al., 2025). Combining multivariate statistics and machine learning methods such as random forests, the contributions of different climatic, topographic, vegetation, and human activity factors can be quantified. Furthermore, coupling this framework with ecosystem or hydro-ecological models to explicitly consider compound drought-heat events and human activity intensity will enhance the scientific support for drought risk early warning and ecological management. 

### **5. Conclusions** 

This study sets against the backdrop of intensifying global drought and increasing ecosystem vulnerability, focuses on the upper Yangtze River Basin to construct a drought sensitivity analysis framework incorporating temporal effects. In addition, the Copula-Bayes approach is employed to quantitatively assess the probability of vegetation damage under drought conditions. 

Drought impacts on vegetation are dominated by cumulative effects, with lag effects playing a secondary role. The duration of vegetation response is closely linked to water availability: ecosystems in arid regions tend to respond more rapidly and over shorter periods, whereas those in humid regions show markedly prolonged responses. 

Sensitivity also differs among vegetation types. Grasslands and shrublands generally exhibit the highest drought sensitivity, while croplands respond more slowly and weakly. High-sensitivity zones occur not only in arid and semi-arid areas but also in humid mountainous and plateau regions. 

the Copula–Bayes framework effectively characterizes the joint probability structure between drought conditions and vegetation loss. The probability and spatial extent of vegetation damage increase systematically with drought severity, yet the basin-wide probability of severe vegetation loss remains relatively low even under extreme drought, suggesting a certain degree of ecosystem resilience. 

Clear spatial gradients and asymmetric responses emerge across different eco-geographical zones. Drought sensitivity is not always positively correlated with actual vegetation loss risk, some highsensitivity areas maintain relatively low damage probabilities. 

In summary, this study systematically characterizes the temporal responses, sensitivity mechanisms, and damage risk features of vegetation under drought from multiple dimensions, providing both methodological foundations and decision-making support for ecological security assessments in the upper Yangtze Basin and similar ecological regions. Future research should further integrate multi-source remote sensing, diverse meteorological variables, and human activity data to advance ecosystem risk modeling from static indicators to dynamic simulations. 

### **CRediT authorship contribution statement** 

**Xiaoxiang Xu:** Writing – original draft, Visualization, Methodology, Investigation, Conceptualization. **Quanzhi Yuan:** Writing – review & editing, Supervision, Methodology, Conceptualization. **Pan Zhao:** Formal analysis, Data curation. **Luping Jia:** Formal analysis. **Ping Ren:** Project administration, Funding acquisition. 

### **Declaration of competing interest** 

The authors declare the following financial interests/personal relationships which may be considered as potential competing interests: No reports was provided by no. No reports a relationship with no that includes:. No has patent no pending to no. The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. If there are other authors, they declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

11 

_Ecological Indicators 185 (2026) 114739_ 

_X. Xu et al._ 

### **Acknowledgements** 

This study was supported by the Projects of National Natural Science Foundation of China, grant number (No. 41930651) and the Sichuan Science and Technology Program (No. 2023NSFSC1979). 

### **Appendix A. Supplementary data** 

Supplementary data to this article can be found online at https://doi. org/10.1016/j.ecolind.2026.114739. 

### **Data availability** 

Data will be made available on request. 

### **References** 

- Anderegg, W.R., 2015. Spatial and temporal variation in plant hydraulic traits and their relevance for climate change impacts on vegetation. New Phytol. 205, 1008–1014. https://doi.org/10.1111/nph.12907. 

- Bashir, S.S., Hussain, A., Hussain, S.J., Wani, O.A., Nabi, S.Z., Dar, N.A., Baloch, F.S., Mansoor, S., 2021. Plant drought stress tolerance: understanding its physiological, biochemical and molecular mechanisms. Biotechnol. Biotechnol. Equip. 35, 1912–1925. https://doi.org/10.1080/13102818.2021.2020161. 

- Bevacqua, E., Rakovec, O., Schumacher, D.L., Kumar, R., Thober, S., Samaniego, L., Seneviratne, S.I., Zscheischler, J., 2024. Direct and lagged climate change effects intensified the 2022 European drought. Nat. Geosci. 17, 1100–1107. https://doi. org/10.1038/s41561-024-01559-2. 

- Bright, R.M., Davin, E., O'Halloran, T., Pongratz, J., Zhao, K., Cescatti, A., 2017. Local temperature response to land cover and management change driven by non-radiative processes. Nat. Clim. Chang. 7, 296–302. https://doi.org/10.1038/nclimate3250. 

- Chen, J., Shao, Z., Deng, X., Huang, X., Dang, C., 2023. Vegetation as the catalyst for water circulation on global terrestrial ecosystem. Sci. Total Environ. 895, 165071. https://doi.org/10.1016/j.scitotenv.2023.165071. 

- Chen, Y., Wang, Y., Wu, C., Jardim, A.M.R.F., Fang, M., Yao, L., Liu, G., Xu, Q., Chen, L., Tang, X., 2025. Drought-induced stress on rainfed and irrigated agriculture: Insights from multi-source satellite-derived ecological indicators. Agric. Water Manag. 307, 109249. https://doi.org/10.1016/j.agwat.2024.109249. 

- Deng, H., Yin, Y., Han, X., 2020. Vulnerability of vegetation activities to drought in Central Asia. Environ. Res. Lett. 15, 084005. https://doi.org/10.1088/1748-9326/ ab93fa. 

- DeSoto, L., Cailleret, M., Sterck, F., Jansen, S., Kramer, K., Robert, E.M., Aakala, T., Amoroso, M.M., Bigler, C., Camarero, J.J., Cufar, K., 2020. Low growth resilience to<sup>ˇ</sup> drought is related to future mortality risk in trees. Nat. Commun. 11, 545. https:// doi.org/10.1038/s41467-020-14300-5. 

- Dikshit, A., Pradhan, B., Alamri, A.M., 2021. Long lead time drought forecasting using lagged climate variables and a stacked long short-term memory model. Sci. Total Environ. 755, 142638. https://doi.org/10.1016/j.scitotenv.2020.142638. 

- Duan, A., Zhong, Y., Xu, G., Yang, K., Tian, B., Wu, Y., 2024. Quantifying the 2022 extreme drought in the Yangtze River basin using GRACE-FO. J. Hydrol. 630, 130680. https://doi.org/10.1016/j.jhydrol.2024.130680. 

- Duveiller, G., Hooker, J., Cescatti, A., 2018. The mark of vegetation change on earth's surface energy balance. Nat. Commun. 9, 679. https://doi.org/10.1038/s41467017-02810-8. 

- Feldman, A.F., Short Gianotti, D.J., Dong, J., Trigo, I.F., Salvucci, G.D., Entekhabi, D., 2023. Tropical surface temperature response to vegetation cover changes and the role of drylands. Glob. Change Biol. 29, 110–125. https://doi.org/10.1111/ gcb.16455. 

- Grossiord, C., Buckley, T.N., Cernusak, L.A., Novick, K.A., Poulter, B., Siegwolf, R.T., Sperry, J.S., McDowell, N.G., 2020. Plant responses to rising vapor pressure deficit. New Phytol. 226, 1550–1566. https://doi.org/10.1111/nph.16485. 

- Han, W., Guan, J., Zheng, J., Liu, Y., Ju, X., Liu, L., Li, J., Mao, X., Li, C., 2023. 

   - Probabilistic assessment of drought stress vulnerability in grasslands of Xinjiang. China. Front. Plant Sci. 14, 1143863. https://doi.org/10.3389/fpls.2023.1143863. 

- Herrero, A., Gonz´alez-Gascuena, R., Gonz˜ ´alez-Díaz, P., Ruiz-Benito, P., Andivia, E., 2023. Reduced growth sensitivity to water availability as potential indicator of droughtinduced tree mortality risk in a Mediterranean _Pinus sylvestris_ L. forest. Front. For. Glob. Change 6, 1249246. https://doi.org/10.3389/ffgc.2023.1249246. 

- Hu, Z., Liang, X., Bian, C., Min, X., Yue, Z., Ran, Y., 2025. Future precipitation projections and model evaluation in the Hengduan Mountains based on CMIP6. J. Environ. Manage. 382, 125378. https://doi.org/10.1016/j.jenvman.2025.125378. 

- Intergovernmental Panel on Climate Change (IPCC), 2014. Climate change 2014: Synthesis report. https://www.ipcc.ch/report/ar5/syr/. 

- Itam, M., Mega, R., Tadano, S., Abdelrahman, M., Matsunaga, S., Yamasaki, Y., Akashi, K., Tsujimoto, H., 2020. Metabolic and physiological responses to progressive drought stress in bread wheat. Sci. Rep. 10, 17189. https://doi.org/ 10.1038/s41598-020-74303-6. 

- Itter, M.S., D'Orangeville, L., Dawson, A., Kneeshaw, D., Duchesne, L., Finley, A.O., 2019. Boreal tree growth exhibits decadal-scale ecological memory to drought and insect defoliation, but no negative response to their interaction. J. Ecol. 107, 1288–1301. https://doi.org/10.1111/1365-2745.13087. 

- Jha, S., Das, J., Sharma, A., Hazra, B., Goyal, M.K., 2019. Probabilistic evaluation of vegetation drought likelihood and its implications to resilience across India. Glob. Planet. Change 176, 23–35. https://doi.org/10.1016/j.gloplacha.2019.01.014. 

- Ji, Y., Zeng, S., Yang, L., Wan, H., Xia, J., 2024. Global eight drought types: spatiotemporal characteristics and vegetation response. J. Environ. Manage. 359, 121069. https://doi.org/10.1016/j.jenvman.2024.121069. 

- Jiang, H., Song, L., Li, Y., Ma, M., Fan, L., 2021. Monitoring the reduced resilience of forests in Southwest China using long-term remote sensing data. Remote Sens. 14, 32. https://doi.org/10.3390/rs14010032. 

- Lai, Y., Tang, H., Zhan, C., Hong, S., Ran, Q., 2025. Evaluating the cumulative and timelag effects of vegetation response to drought in the Lancang-Mekong River basin. Ecol. Indic. 178, 114113. https://doi.org/10.1016/j.ecolind.2025.114113. 

- Li, D., An, L., Zhong, S., Shen, L., Wu, S., 2024. Declining coupling between vegetation and drought over the past three decades. Glob. Change Biol. 30, e17141. https://doi. org/10.1111/gcb.17141. 

- Mathias, J.M., Thomas, R.B., 2021. Global tree intrinsic water use efficiency is enhanced by increased atmospheric CO₂ and modulated by climate and plant functional types. Proc. Natl. Acad. Sci. U. S. A. 118, e2014286118. https://doi.org/10.1073/ pnas.2014286118. 

- McDowell, N., Pockman, W.T., Allen, C.D., Breshears, D.D., Cobb, N., Kolb, T., Plaut, J., Sperry, J., West, A., Williams, D.G., Yepez, E.A., 2008. Mechanisms of plant survival and mortality during drought: why do some plants survive while others succumb to drought? New Phytol. 178, 719–739. https://doi.org/10.1111/j.14698137.2008.02436.x. 

- Ming, W., Xu, T., Xiao, J., Liu, S., Xu, Z., Lin, J., 2025. Responses and shifting drivers of ecosystem carbon fluxes under drought conditions. Ecol. Indic. 179, 114283. https://doi.org/10.1016/j.ecolind.2025.114283. 

- Mishra, A.K., Singh, V.P., 2010. A review of drought concepts. J. Hydrol. 391, 202–216. https://doi.org/10.1016/j.jhydrol.2010.07.012. 

- Osakabe, Y., Osakabe, K., Shinozaki, K., Tran, L.-S.P., 2014. Response of plants to water stress. Front. Plant Sci. 5, 86. https://doi.org/10.3389/fpls.2014.00086. 

- Peguero-Pina, J.J., Vilagrosa, A., Alonso-Forn, D., Ferrio, J.P., Sancho-Knapik, D., GilPelegrín, E., 2020. Living in drylands: functional adaptations of trees and shrubs to cope with high temperatures and water scarcity. Forests 11, 1028. https://doi.org/ 10.3390/f11101028. 

- Peng, J., Wu, C., Zhang, X., Wang, X., Gonsamo, A., 2019. Satellite detection of cumulative and lagged effects of drought on autumn leaf senescence over the northern hemisphere. Glob. Change Biol. 25, 2174–2188. https://doi.org/10.1111/ gcb.14627. 

- Peng, S., 2020. 1-km monthly precipitation dataset for China (1901–2024). National Tibetan Plateau / Third Pole Environment Data Center. https://doi.org/10.5281/ zenodo.3114194. 

- Pinzon, J.E., Pak, E.W., Tucker, C.J., Bhatt, U.S., Frost, G.V., Macander, M.J., 2023. Global vegetation greenness (NDVI) from AVHRR GIMMS-3G+, 1981–2022. ORNL DAAC. https://doi.org/10.3334/ORNLDAAC/2187. 

- Porcel, R., Ruiz-Lozano, J.M., 2004. Arbuscular mycorrhizal influence on leaf water potential, solute accumulation, and oxidative stress in soybean plants subjected to drought stress. J. Exp. Bot. 55, 1743–1750. https://doi.org/10.1093/jxb/erh188. 

- Qu, S., Wang, L., Lin, A., Zhu, H., Yuan, M., 2018. What drives the vegetation restoration in Yangtze River basin, China: climate change or anthropogenic factors? Ecol. Indic. 90, 438–450. https://doi.org/10.1016/j.ecolind.2018.03.029. 

- Stahl, K., Kohn, I., Blauhut, V., Urquijo, J., De Stefano, L., Acacio, V., Dias, S., Stagge, J. ´ H., Tallaksen, L.M., Kampragou, E., Van Loon, A.F., Barker, L.J., Melsen, L.A., Bifulco, C., Musolino, D., De Carli, A., Massarutto, A., Assimacopoulos, D., Van Lanen, H.A.J., 2016. Impacts of European drought events: insights from an international database of text-based reports. Nat. Hazards Earth Syst. Sci. 16, 801–819. https://doi.org/10.5194/nhess-16-801-2016. 

- Su, J., Fan, L., Yuan, Z., Wang, Z., Wang, Z., 2024. Quantifying the drought sensitivity of grassland under different climate zones in Northwest China. Sci. Total Environ. 910, 168688. https://doi.org/10.1016/j.scitotenv.2023.168688. 

- Sun, B., Zhao, H., Wang, X., 2016. Effects of drought on net primary productivity: roles of temperature, drought intensity, and duration. Chin. Geogr. Sci. 26, 270–282. https://doi.org/10.1007/s11769-016-0804-3. 

- Swain, D.L., Prein, A.F., Abatzoglou, J.T., Albano, C.M., Brunner, M., Diffenbaugh, N.S., Singh, D., Skinner, C.B., Touma, D., 2025. Hydroclimate volatility on a warming earth. Nat. Rev. Earth Environ. 6, 35–50. https://doi.org/10.1038/s43017-02400624-z. 

- Tan, X., Wu, X., Huang, Z., Fu, J., Tan, X., Deng, S., Liu, Y., Gan, T.Y., Liu, B., 2023. Increasing global precipitation whiplash due to anthropogenic greenhouse gas emissions. Nat. Commun. 14, 2796. https://doi.org/10.1038/s41467-023-38510-9. 

- Vicente-Serrano, S.M., Beguería, S., Lopez-Moreno, J.I., 2010. A multiscalar drought ´ index sensitive to global warming: the standardized precipitation evapotranspiration index. J. Climate 23, 1696–1718. https://doi.org/10.1175/2009JCLI2909.1. 

- Vicente-Serrano, S.M., Gouveia, C., Camarero, J.J., Beguería, S., Trigo, R., Lopez- ´ Moreno, J.I., Azorín-Molina, C., Pasho, E., Lorenzo-Lacruz, J., Revuelto, J., Mor´anTejeda, E., 2013. Response of vegetation to drought time-scales across global land biomes. Proc. Natl. Acad. Sci. U. S. A. 110, 52–57. https://doi.org/10.1073/ pnas.1207068110. 

- Vilonen, L., Ross, M., Smith, M.D., 2022. What happens after drought ends: synthesizing terms and definitions. New Phytol. 235, 420–431. https://doi.org/10.1111/ nph.18137. 

- Volo, T.J., Vivoni, E.R., Martin, C.A., Earl, S., Ruddell, B.L., 2014. Modelling soil moisture, water partitioning, and plant water stress under irrigated conditions in desert urban areas. Ecohydrology 7, 1297–1313. https://doi.org/10.1002/eco.1457. 

12 

_Ecological Indicators 185 (2026) 114739_ 

_X. Xu et al._ 

- Wang, C., Yang, P., Xia, J., Huang, H., Chen, L., Sun, K., 2026. Drought onsets and their driving factors for multiple drought types in the Yangtze River basin. Climate Dynam. 64, 5. https://doi.org/10.1007/s00382-025-07953-9. 

- Wang, M., Wang, Y., Liu, X., Hou, W., Wang, J., Li, S., Zhao, L., Hu, Z., 2025b. Vapor pressure deficit dominates vegetation productivity during compound drought and heatwave events in China's arid and semi-arid regions: evidence from multiple vegetation parameters. Ecol. Inform. 88, 103144. https://doi.org/10.1016/j. ecoinf.2025.103144. 

- Wang, P., Zheng, H., Liu, S., 2013. Geomorphic constraints on middle Yangtze River reversal in eastern Sichuan Basin, China. J. Asian Earth Sci. 69, 70–85. https://doi. org/10.1016/j.jseaes.2012.09.018. 

- Wang, S., Li, R., Wu, Y., Zhao, S., 2022. Effects of multi-temporal scale drought on vegetation dynamics in Inner Mongolia from 1982 to 2015, China. Ecol. Indic. 136, 108666. https://doi.org/10.1016/j.ecolind.2022.108666. 

- Wang, Z., Chen, W., Piao, J., Cai, Q., Chen, S., Xue, X., Ma, T., 2025a. Synergistic effects of high atmospheric and soil dryness on record-breaking decreases in vegetation productivity over Southwest China in 2023. npj Clim. Atmos. Sci. 8, 6. https://doi. org/10.1038/s41612-025-00895-3. 

- Weng, Z., Niu, J., Guan, H., Kang, S., 2023. Three-dimensional linkage between meteorological drought and vegetation drought across China. Sci. Total Environ. 859, 160300. https://doi.org/10.1016/j.scitotenv.2022.160300. 

- Wilhite, D.A., Glantz, M.H., 1985. Understanding the drought phenomenon: the role of definitions. Water Int. 10, 111–120. https://doi.org/10.1080/02508068508686328. 

- Wu, X., Yang, Y., Jiang, D., 2023. Dramatic increase in the probability of 2006-like compound dry and hot events over Southwest China under future global warming. Weather Clim. Extrem. 41, 100592. https://doi.org/10.1016/j.wace.2023.100592. 

- Xu, H.J., Wang, X.P., Zhao, C.Y., 2021. Drought sensitivity of vegetation photosynthesis along the aridity gradient in northern China. Int. J. Appl. Earth Obs. Geoinf. 102, 102418. https://doi.org/10.1016/j.jag.2021.102418. 

- Xu, S., Wang, Y., Liu, Y., Li, J., Qian, K., Yang, X., Ma, X., 2023. Evaluating the cumulative and time-lag effects of vegetation response to drought in Central Asia under changing environments. J. Hydrol. 627, 130455. https://doi.org/10.1016/j. jhydrol.2023.130455. 

- Xu, W., Yuan, W., Wu, D., Zhang, Y., Shen, R., Xia, X., Ciais, P., Liu, J., 2024. Impacts of record-breaking compound heatwave and drought events in 2022 China on vegetation growth. Agric. For. Meteorol. 344, 109799. https://doi.org/10.1016/j. agrformet.2023.109799. 

- Yang, R., Xing, B., 2022. Spatio-temporal variability in hydroclimate over the upper Yangtze River basin, China. Atmosphere 13, 317. https://doi.org/10.3390/ atmos13020317. 

- Yao, L., Lu, J., Jiang, H., Liu, T., Qin, J., Zhou, C., 2023. Satellite-derived aridity index reveals China's drying in recent two decades. iScience 26, 106185. https://doi.org/ 10.1016/j.isci.2023.106185. 

- Yuan, B., Guo, S., Zhang, X., Mu, H., Cao, S., Xia, Z., Pan, X., Du, P., 2024. Quantifying the drought sensitivity of vegetation types in northern China from 1982 to 2022. Agric. For. Meteorol. 359, 110293. https://doi.org/10.1016/j. agrformet.2024.110293. 

- Zhan, C., Liang, C., Zhao, L., Jiang, S., Niu, K., Zhang, Y., 2022. Drought-related cumulative and time-lag effects on vegetation dynamics across the Yellow River Basin, China. Ecol. Indic. 143, 109409. https://doi.org/10.1016/j. ecolind.2022.109409. 

- Zhang, R.-Q., Xiong, Q., Wu, L., Wang, P., Kong, J.-Y., Shi, X., Sun, Z.-Y., 2024. Water supply following drought: effects on drought legacy and resilience in a tropical forest – a case study in Xishuangbanna. China. Ecol. Inform. 79, 102422. https://doi.org/ 10.1016/j.ecoinf.2023.102422. 

- Zhang, X., Zhang, B., 2019. The responses of natural vegetation dynamics to drought during the growing season across China. J. Hydrol. 574, 706–714. https://doi.org/ 10.1016/j.jhydrol.2019.04.084. 

- Zhou, R., Liu, Y., Cui, M., Lu, J., Shi, H., Ren, H., Zhang, W., Wen, Z., 2022a. Global assessment of cumulative and time-lag effects of drought on land surface phenology. GISci. Remote Sens. 59, 1918–1937. https://doi.org/10.1080/ 15481603.2022.2143661. 

- Zhou, Z., Liu, S., Ding, Y., Fu, Q., Wang, Y., Cai, H., Shi, H., 2022b. Assessing the responses of vegetation to meteorological drought and its influencing factors with partial wavelet coherence analysis. J. Environ. Manage. 311, 114879. https://doi. org/10.1016/j.jenvman.2022.114879. 

13 

