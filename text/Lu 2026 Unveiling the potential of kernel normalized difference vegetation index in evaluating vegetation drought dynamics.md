

# **Rapid #: -27622375** 

CROSS REF ID: **896753** 

## LENDER: **NVUSN (Roseman University of Health Science Library) :: Main Library** 

BORROWER: **IRU (New Mexico State University) :: Main Library** 

TYPE: Article CC:CCG JOURNAL TITLE: Remote sensing applications USER JOURNAL TITLE: Remote sensing applications : society and environment ARTICLE TITLE: Unveiling the potential of kernel Normalized Difference Vegetation Index in evaluating vegetation drought dynamics ARTICLE AUTHOR: Lu, Baiyu VOLUME: 44 ISSUE: MONTH: 12 YEAR: 2026 PAGES: 102281 ISSN: 2352-9385 OCLC #: Processed by RapidX: 10/5/2026 2:05:03 PM 

This material may be protected by copyright law (Title 17 U.S. Code) 

Remote Sensing Applications: Society and Environment 44 (2026) 102281 



Contents lists available at ScienceDirect 

## Remote Sensing Applications: Society and Environment 

journal homepage: www.elsevier.com/locate/rsase 



### Unveiling the potential of kernel normalized difference vegetation index in evaluating vegetation drought dynamics 

Baiyu Lu<sup>a</sup> , Yuhao Liang<sup>b,*</sup> , Maijin Lin<sup>c</sup> , Yungui Lu<sup>d</sup> , Donghui Lu<sup>e</sup> 

a _College of Geomatics and Geoinformation, Guilin University of Technology, Guilin, 541004, China_ b _College of Water Resources and Architectural Engineering, Northwest A & F University, Yangling, Shanxi, 712100, China_ c _College of Geology Engineering and Geomatics, Chang'an University, Xi'an, 710054, China_ d _School of Geosciences and Info-Physics, Central South University, Changsha, 410083, China_ e _Natural Resources Information Center of Guangxi Zhuang Autonomous Region, Nanning, 530022, China_ 

##### A R T I C L E I N F O 

A B S T R A C T 

_Keywords:_ Kernel Normalized difference vegetation index Vegetation condition indices Spatiotemporal variation Drought monitoring Southwest China 

Drought is a key factor that compromises the health of global terrestrial ecosystems, and vegetation indices are crucial parameters for accurately assessing vegetation drought conditions. This study constructed a new vegetation condition index (VCIk) based on the kernel Normalized Difference Vegetation Index (kNDVI). We compared VCIk with indices derived from the classic Normalized Difference Vegetation Index (VCIN) and the Enhanced Vegetation Index (VCIE) to verify its applicability and superiority for vegetation drought monitoring. Furthermore, we employed VCIk to assess the spatiotemporal patterns of seasonal vegetation drought in Southwest China. The results showed that: (1) VCIk was the optimal vegetation index for drought monitoring. Specifically, VCIk outperformed VCIN and VCIE across various assessments, including consistency for long-term drought monitoring, drought event monitoring accuracy, monitoring reliability in special drought period, and the sensitivity to the integrated drought stress. (2) From 2000 to 2020, seasonal vegetation drought across Southwest China showed an alleviating trend, with 50.96% of the area exhibiting significant alleviation (p _<_ 0.05). (3) Vegetation drought was more severe in spring and winter than in summer and autumn and exhibited strong persistence. Notably, seasonal vegetation droughts showed persistent characteristics, indicating that vegetation in Southwest China is susceptible to consecutive drought events. This study confirms the significant potential of kNDVI to supersede traditional vegetation indices (NDVI and EVI) for vegetation drought monitoring. These findings have important implications for improving drought monitoring accuracy and maintaining ecological stability. 

#### **1. Introduction** 

Drought stands out as one of the most complex natural disasters (Schwalm et al., 2017). According to the of the Global Climate 2023 report, global temperatures are on a steady rise, leading to a surge in extreme weather events, notably droughts, affecting millions and causing billions in economic losses. Under climate change, droughts are increasing in frequency, duration, severity, and spatial extent, posing a significant threat to ecosystem stability, agricultural production, food security, and economic development (Mishra and Singh, 2010). Consequently, developing objective and quantitative drought monitoring techniques and accurately assessing the 

* Corresponding author. 

_E-mail address:_ yhliang0221@nwafu.edu.cn (Y. Liang). 

https://doi.org/10.1016/j.rsase.2026.102281 Received 13 September 2025; Received in revised form 31 March 2026; Accepted 21 September 2026 Available online 22 September 2026 

2352-9385/© 2026 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies. 

_Remote Sensing Applications: Society and Environment 44 (2026) 102281_ 

_B. Lu et al.                                                                                                                                                                                                              Remote Sensing Applications: Society and Environment_ 

spatiotemporal variation of drought have emerged as pivotal challenges in contemporary drought research (Cui et al., 2024; Vicente-Serrano et al., 2020). 

Drought indices can be categorized into station monitoring and remote sensing monitoring indices based on monitoring methods. Station monitoring indices primarily utilize hydrological and meteorological data, such as runoff, precipitation, and temperature from in situ observation stations, for drought assessment. Commonly employed index is Standardized Precipitation Evapotranspiration Index (SPEI) (Vicente-Serrano et al., 2010). Although station monitoring provides high observation accuracy, it accurately characterizes drought conditions only proximal to the station, necessitating spatial interpolation methods for continuous drought monitoring across region (Li et al., 2020). However, the low density and uneven distribution of ground stations, coupled with the uncertainty of spatial interpolation methods, often result in insufficient accuracy, hindering the precise characterisation of drought's spatial patterns (Mendicino et al., 2008; Mirabbasi et al., 2013). With the advancements of remote sensing technology and increased satellite observations, data products with higher temporal resolution and finer spatial resolution have facilitated large-scale spatiotemporal continuous drought monitoring through remote sensing indices (Jiao et al., 2021). The Normalized Difference Vegetation Index (NDVI), an early index effectively portrays vegetation health by integrating red and near-infrared bands, commonly utilized in drought monitoring (Rouse et al., 1974). Nevertheless, NDVI is susceptible to atmospheric conditions and background effects of soil and canopy, with saturation issues in densely vegetated areas. To address these limitations, the Enhanced Vegetation Index (EVI) considers atmospheric interference and soil background reflectance, performing well in dense vegetation but still subject to saturation issues (Liu and Huete, 1995). Different traditional vegetation indices, the kernel Normalized Difference Vegetation Index (kNDVI) is a nonlinear index constructed employed kernel method theory and machine learning principles, maximizing spectral information usage and effectively mitigating saturation problems (Camps-Valls et al., 2021). It demonstrates superior stability and robustness compared to traditional vegetation indices under diverse environmental conditions (Wang et al., 2022b, 2023a). The Vegetation Condition Index (VCI), a standardized drought index, monitors relative changes in vegetation indices over time using historical vegetation index sequences (Kogan, 1995). It mitigates the impact of geographic location or environment variables (such as soil, vegetation, terrain, etc.) on drought monitoring, endorsed by the World Meteorological Organization State for regional and global drought monitoring (Wmo, 2009). 

VCI can be computed using various vegetation indices. Among these, NDVI stands out due to its long time series availability and ease of computation, making it the most prevalent choice for VCI calculations (Cao et al., 2022). Additionally, the EVI has also been utilized in VCI computation and has been demonstrated effectiveness in identifying vegetation drought severity (Senhorelo et al., 2023). Apart from its direct application in drought monitoring, VCI is considered a pivotal component in comprehensive drought indices (Lu et al., 2023). In light of the climate and drought characteristics in Southwest China, an Optimized Vegetation Drought Index (OVDI) was formulated using constrained optimization techniques, incorporating VCI alongside the Temperature Condition Index (TCI), Precipitation Condition Index (PCI), and Soil Moisture Condition Index (SMCI) (Hao et al., 2015). A comprehensive drought index was proposed by integrating VCI, PCI, TCI, and SMCI, with its applicability validated in the United States (Jiao et al., 2019). Despite the widespread adoption of VCI in previous research, the optimal vegetation index for VCI computation in vegetation drought monitoring remains ambiguous. A previous study revealed discrepancies in drought patterns between VCI derived from NDVI and EVI (Branco et al., 2019). Moreover, significant disparities in the consistency and accuracy of NDVI and EVI in vegetation drought monitoring were observed across various vegetation growth stages (Wang et al., 2023b). This underscores the need for a comprehensive analysis of the suitability of different vegetation indices and their derived VCI in vegetation drought monitoring applications. 

Southwest China is the largest continuous karst region in the world (Wang et al., 2021). Due to extensive rocky desertification and the unsustainable exploitation of ecological resources, the local ecological environment is fragile and sensitive, making Southwest China becoming the region with most frequent and serious of drought in China (Zhang et al., 2013). To combat karst rocky desertification, the Chinese government has initiated several ecological conservation initiatives, such as Natural Forest Protection Project and Rocky Desertification Control Project (Yan et al., 2022; Zhang et al., 2016). These efforts have substantially bolstered regional vegetation cover and enriched biodiversity within terrestrial ecosystems (Xu et al., 2023). However, some terrestrial vegetation ecosystems have deteriorated or even intensified, which cannot be ignored (Xu et al., 2023). Against this backdrop, the assessment of different vegetation indices for drought monitoring and the elucidation of spatiotemporal variations in drought across Southwest China hold significant scientific importance. 

Therefore, this study derived three VCIs from NDVI, EVI, and kNDVI respectively, and utilized them as proxies to evaluate the effectiveness of the vegetation indices for vegetation drought monitoring. Specifically, the Crop Water Stress Index (CWSI), SMCI and SPEI were employed to highlight the advantages of kNDVI in vegetation drought monitoring from multiple perspectives, including consistency for long-term drought monitoring, drought event monitoring accuracy, monitoring reliability in special drought period, and the sensitivity to the integrated drought stress. Additionally, VCI derived from kNDVI was employed to explore the spatiotemporal dynamics of seasonal vegetation drought in Southwest China. Overall, this study aims to answer the following questions: (1) Does the nonlinear vegetation index (kNDVI) exhibit superior monitoring capability compared to traditional vegetation indices for vegetation drought monitoring? (2) What are the spatiotemporal dynamic variation patterns of seasonal vegetation drought in ecologically vulnerable Southwest China? The findings provide valuable insights for precise vegetation drought monitoring and contribute to maintaining the stability of vulnerable ecosystem. 

2 

_Remote Sensing Applications: Society and Environment 44 (2026) 102281_ 

_B. Lu et al.                                                                                                                                                                                                              Remote Sensing Applications: Society and Environment_ 

#### **2. Materials and methods** 

#### _2.1. Study area_ 

The study area is located in the southwest region of China (20<sup>◦</sup> 54′N-34<sup>◦</sup> 19′N, 97<sup>◦</sup> 21′E− 112<sup>◦</sup> 04′E), encompasses the Guangxi, Yunnan, Guizhou, Sichuan, and Chongqing (Fig. 1). The study area exhibits significant seasonal variation, with precipitation during the wet season accounting for more than 85% of the total annual precipitation, while the dry season sees low precipitation and high evaporation rates (Wang et al., 2021). The elevation varies from − 20 to 6304 m, generally decreasing from west to east. Due to the interaction of unique topographical and monsoon climate factors, Southwest China has become an ecologically vulnerable area prone to frequent droughts, where vegetation growth is easily inhibited by drought conditions (Yan et al., 2023). 

#### _2.2. Data sources_ 

The monthly vegetation indices (NDVI, EVI, kNDVI) were derived from the MOD13A3 dataset, which has a spatial resolution of 1 km and covers the period from 2000 to 2020. It has been proven to accurately reflect vegetation dynamics (Liu et al., 2024). The vegetation indices were employed to construct different VCIs. The evapotranspiration (ET) and the potential evapotranspiration (PET) were obtained from the MOD16A2 product which has a temporal resolution of 8 day and a spatial resolution of 500 m. The MOD16 product have been demonstrated by previous studies to reveal the evapotranspiration in China (Zhang et al., 2009). We synthesized monthly ET and PET, and then resampled these data to a 1 km spatial resolution using the bilinear method to calculate the CWSI. To ensure data quality and scientific rigor, all MODIS products were preprocessed using the provided Quality Assurance (QA) bands to mask out pixels contaminated by clouds, snow, or high aerosol content. Small amounts of missing data in the 21-year time series were subsequently filled using linear temporal interpolation. These procedures ensured the continuity and reliability of the vegetation and evapotranspiration data used in our subsequent analysis. 

The monthly precipitation (Pre) and monthly PET data were obtained from the Third Pole Environment Data Center (TPDC). These data are produced by downscaling the CRU and WorldClim climate datasets, with a 1 km spatial resolution (Peng et al., 2019). In this study, the Pre and the PET data were employed to constructed the SPEI. 

The daily soil moisture dataset was provided by TPDC. It is constructed using machine learning modes based on the in-situ soil moisture observation data. The dataset includes soil moisture at ten layers (0~100 cm), having a spatial resolution of 1 km (Li et al., 2022). The mean synthesis method was utilized to obtain monthly averages of soil moisture in root zone (0~100 cm), and the SMCI was calculated based on this. 



**Fig. 1.** Overview of the study area: (a) geographical location; (b) elevation. Note: the elevation derived from the SRTM30+ Global 1-km Digital Elevation Model (DEM): Version 11: Land Surface. 

3 

_Remote Sensing Applications: Society and Environment 44 (2026) 102281_ 

_B. Lu et al.                                                                                                                                                                                                              Remote Sensing Applications: Society and Environment_ 

#### _2.3. Methodology_ 

In this study, the research process was divided into three parts, including the calculation of VCIs and drought indices (DIs), the validation and comparing of effectiveness of VCIk, and the assessment in dynamics of seasonal vegetation drought in Southwest China (Fig. 2). (i) Obtaining the VCIs and DIs datasets in Southwest China. Specifically, VCIN, VCIE, and VCIk were derived from NDVI, EVI, and kNDVI data obtained from MOD13A3, respectively. CWSI was calculated utilizing ET and PET data from MOD16A2. The threemonth-scale SPEI (SPEI-3) was computed based on Pre and PET from meteorological data. SMCI was calculated employing soil moisture data for the root zone (0~100 cm). (ii) The effectiveness of VCIk in vegetation drought monitoring was validated from multiple perspectives and compared with classical VCIs (VCIN and VCIE). Specifically, the evaluation included consistency for longterm drought monitoring, drought event monitoring accuracy, monitoring reliability in special drought period, and the sensitivity to the integrated drought stress. (iii) The VCIk was employed to assess seasonal vegetation drought in Southwest China, and the various analytical methods were utilized to analyze its spatiotemporal dynamics. 

#### _2.3.1. Vegetation condition indices and drought indices_ 

kNDVI is a recently developed nonlinear vegetation index, which is obtained by nonlinear generalization of NDVI by kernel method theory of machine learning (Camps-Valls et al., 2021). It is calculated as follows: 



Where σ represents the length-scale parameter that determines the distance between the near infrared band (NIR) and the red band (Red), and a reasonable choice is σ = 0.5 (NIR + Red) (Camps-Valls et al., 2021). Therefore, the calculation formula of kNDVI can be simplified as: 



**Fig. 2.** The methodological workflow of the research. 

4 

(2) 

_Remote Sensing Applications: Society and Environment 44 (2026) 102281_ 

_B. Lu et al.                                                                                                                                                                                                              Remote Sensing Applications: Society and Environment_ 

#### _kNDVI_ = tanh( _NDVI_<sup>2)</sup> 

The VCI is calculated based on the range of vegetation index values within the study period, providing a direct measure of vegetation drought (Branco et al., 2019). In this study, monthly VCIs were calculated based on NDVI, EVI and kNDVI respectively. The different DIs were employed to assess whether the novel nonlinear vegetation index (kNDVI) offers unique advantages over classical vegetation indices in vegetation drought monitoring. Specifically, CWSI, SMCI and SPEI-3 were selected as the drought indices. Among them, CWSI can reflect surface evaporation, SMCI depicts soil moisture deficit, and SPEI represents the difference between rainfall and potential evapotranspiration (Jackson et al., 1988; Vicente-Serrano et al., 2010; Zhang and Jia, 2013). The formulas for calculating the VCIs and drought indices are as follows. 

Where _VCIN_ , _VCIE_ and _VCIk_ represent the vegetation condition indices derived by NDVI, EVI and kNDVI respectively (see Table 1). _NDVIi,j_ , _EVIi,j_ and _kNDVIi,j_ denote the value of the respective vegetation indices in year _i_ and month _j_ . _NDVImin,j_ , _EVImin,j_ and _kNDVImin,j_ represent the minimum values of NDVI, EVI and kNDVI for month _j_ calculated across the period from 2000 to 2020. Similarly, _NDVImax, j_<sup>,</sup><sup>_EVI_</sup> _max,j_<sup>and</sup><sup>_kNDVI_</sup> _max,j_<sup>denote the maximum values for the corresponding month</sup><sup>_j_over the same multi-year period.</sup><sup>_ET_and</sup><sup>_PET_</sup> represent evapotranspiration and potential evapotranspiration, respectively. _SMi,j_ is the root-zone soil moisture in year _i_ and month _j_ , while _SMmin,j_ and _SMmax,j_ are its multi-year monthly extremes. According to the range, the VCIs and drought indices were classified into different drought grades (Table 2). 

#### _2.3.2. Consistency for long-term drought monitoring_ 

The Pearson correlation coefficient was employed to examine the long-term correlation between VCI and CWSI, SMCI, and SPEI-3, thereby evaluating the consistency of VCI in vegetation drought monitoring (Li et al., 2023). Specifically, VCI is considered consistent with the variation in DIs when it exhibits the expected correlations (negative correlation with CWSI, positive correlations with SMCI and SPEI-3). The calculation formula is as follows: 



Where _rxy_ represents the correlation coefficient between _x_ and _y_ , _n_ represents the total length from 2000 to 2020, _xi_ and _yi_ represent the value of x and y respectively in year _xi_ and _yi_ represent the mean values of x and y respectively from 2000 to 2020. The correlation between VCI and drought index was divided into insignificant correlation (P ≥ 0.05) and significant correlation (P _<_ 0.05). 

#### _2.3.3. Monitoring accuracy of drought event_ 

The number of drought events detected by VCI and drought indices was counted separately at the pixel scale. If a drought event is detected by VCI simultaneously with at least one of CWSI, SMCI, or SPEI-3, it is considered that the VCI accurately monitored this drought event (Cheng et al., 2023). The percentage of accurate detections out of the total number of drought events was regarded as the accuracy rate for drought monitoring utilizing VCI. The calculation formula is as follows: 



Where _ACC_ represents the accuracy rate of drought, _a_ represents the number of simultaneous droughts of VCIk with at least one of CWSI, SMCI and SPEI-3, _N_ represents the total length from 2000 to 2020. 

#### _2.3.4. Sensitivity to integrated drought stress_ 

To further evaluate the sensitivity of VCI to integrated drought stress, a multiple regression model was developed with VCIs (VCIN, VCIE, VCIk) and DIs (CWSI, SMCI, SPEI). The coefficient of determination (R<sup>2</sup> ) was employed to assess its overall explanatory power, which reflects the sensitivity of VCI to drought. The higher R<sup>2</sup> value indicates a stronger comprehensive sensitivity of VCI to drought 

**Table 1** 

The calculation formulas of VCIs and DIs. 

|Category|Index|Formula|
|---|---|---|
|Vegetation condition indices|VCIN<br>VCIE|_NDVIi,j_−_NDVImin,j_<br>_NDVImax,j_−_NDVImin,j _<sup>(3)</sup><br>_EVIi,j_−_EVImin,j_<br>_EVImax,j_−_EVImin,j _<sup>(4)</sup>|
||VCIk|_kNDVIi,j_−_kNDVImin,j_<br>(5)|
|||_kNDVImax,j_ −_kNDVImin,j _<br>|
|Drought indices|CWSI<br>SMCI|1−<br>_ET_<br>_PET_<sup>(6)</sup><br>_SMi,j_ −_SMmin,j_<br>_SMmax,j_−_SMmin,j _<sup>(7)</sup>|
||SPEI|Following (Vicente-Serrano et al., 2010)|



5 

_B. Lu et al.                                                                                                                                                                                                              Remote Sensing Applications: Society and Environment 44 (2026) 102281_ 

**Table 2** 

Drought categories of VCI, CWSI, SMCI and SPEI-3. 

|Drought categories|VCI|CWSI|SMCI|SPEI-3|
|---|---|---|---|---|
|No drought|0.4 ~ 1|0 ~ 0.4|0.4 ~ 1|_>_−0.5|
|Mild drought|0.3 ~ 0.4|0.4 ~ 0.6|0.3 ~ 0.4|−0.5 ~−1|
|Moderate drought|0.2 ~ 0.3|0.6 ~ 0.7|0.2 ~ 0.3|−1 ~−1.5|
|Severe drought|0.1 ~ 0.2|0.7 ~ 0.8|0.1 ~ 0.2|−1.5 ~−2|
|Extreme drought|0 ~ 0.1|0.8 ~ 1|0 ~ 0.1|_<_−2|



conditions, while a lower R<sup>2</sup> value suggests weaker sensitivity. The calculation formula is as follows: 



Where _N_ represents total length from 2000 to 2020, _yi_ represent the predicted value of VCI, _yi_ represents the true value of VCI, _~~y~~_ represents the average true value of VCI from 2000 to 2020. 

#### _2.3.5. Spatiotemporal dynamics of vegetation drought_ 

Firstly, we calculated the slope of variation in the seasonal VCIk utilizing Theil-Sen median trend analysis to assess the spatiotemporal trends of seasonal vegetation drought (Fan et al., 2023). Subsequently, the Mann-Kendall test was utilized to evaluate the significance of the trend, which we classified into significant (P _<_ 0.05) and insignificant (P ≥ 0.05). The slope is calculated as follows: 



Where _VCIj_ and _VCIi_ represent the value of seasonal VCIk in year _j_ and year _i_ respectively. _βVCI_ represents the slope of variation trend in VCIk. 

Finally, we employed the Hurst exponent (H) to quantify the persistence of the seasonal vegetation drought trends. An H value indicates an anti-persistent trend when 0 ≤ H _<_ 0.5, a random trend when H = 0.5, and a persistent trend when H _>_ 0.5. Accordingly, we classified the drought trend persistence based on the H value into distinct levels: persistence (0.5, 1]; stability (0.5); anti-persistence [0, 0.5). 

#### _2.3.6. Analysis of drought frequency and centroid migration_ 

The centroid migration model was utilized to determine the migration paths of seasonal vegetation drought, to analyze quantitatively the migration characteristics of drought from 2000 to 2020 (Xiang et al., 2022). 



Where _~~x~~_ and _~~y~~_ represent the longitude and latitude of the centroid of vegetation drought. _Mi_ indicates the degree of drought in the _i-th_ pixel. _Xi_ and _Yi_ represent the longitude and latitude of the _i-th_ pixel. 

The frequency of drought is a crucial indicator for drought management and early warning, and often employed to evaluate prolonged drought conditions (Li et al., 2024). The frequency of seasonal vegetation drought was calculated based on the number of drought events monitored by seasonal VCIk (Table 2), with the calculation formula as follows: 



Where _f_ represents the frequency of drought, _n_ represents the number of droughts from 2000 to 2020, and _N_ represents the total length from 2000 to 2020. 

6 

_Remote Sensing Applications: Society and Environment 44 (2026) 102281_ 

#### **3. Results** 

#### _3.1. Evaluation of the consistency for long-term drought monitoring_ 

To analyze the effectiveness of VCIs in vegetation drought monitoring, we compared the correlation coefficients between the VCIs and DIs (Fig. 3). Specifically, VCI was considered consistent with the drought indices when it was negatively correlated with CWSI and positively correlated with both SMCI and SPEI-3. The results demonstrate that VCIk maintains a superior level of spatial consistency compared to traditional indices across all drought dimensions. Specifically, VCIk achieves the most extensive regional coverage of consistent correlation with CWSI, SMCI, and SPEI-3, outperforming both VCIN and VCIE. This enhanced performance is further reflected in the mean correlation coefficients, where VCIk displays a tighter coupling with both meteorological and soil moisture stress indicators than other VCIs. Specifically, VCIk had the highest mean correlation coefficients with CWSI, SMCI, and SPEI-3 (− 0.32, 0.18, and 0.18). This was followed by VCIN (− 0.29, 0.18, and 0.16), while VCIE had the lowest coefficients (− 0.25, 0.13, and 0.14). 

To evaluate the effectiveness of each VCI, we calculated the proportion of the study area where each VCI showed a significant correlation (P _<_ 0.05) with the DIs (Table 3). The results indicated that VCIk yields the largest area of significant correlation with CWSI and SMCI, highlighting its increased sensitivity to crop water stress and soil moisture depletion. While VCIN shows a comparable spatial extent for meteorological drought (SPEI-3), VCIE generally exhibits the most limited capacity for capturing drought signals across the study area. These spatial patterns suggest that the nonlinear mapping of kNDVI provides a more comprehensive and reliable representation of vegetation stress in this complex landscape. 



**Fig. 3.** Spatial distribution of correlation coefficients between VCIs and DIs: (a) VCIN and CWSI; (b) VCIE and CWSI; (c) VCIk and CWSI; (e) VCIN and SMCI; (f) VCIE and SMCI; (g) VCIk and SMCI; (i) VCIN and SPEI-3; (j) VCIE and SPEI-3; (k) VCIk and SPEI-3; area percentage of correlation coefficients between VCIs and CWSI (d), SMCI (h), SPEI-3 (l). 

7 

_Remote Sensing Applications: Society and Environment 44 (2026) 102281_ 

**Table 3** 

The proportion of areas significantly correlated (P _<_ 0.05) between monthly VCIs and DIs. 

|Vegetation condition indices|Area proportion of si|ignificant correlation (%)||
|---|---|---|---|
||CWSI|SMCI|SPEI-3|
|VCIN|80.46|52.91|53.49|
|VCIE|75.14|37.56|38.62|
|VCIk|85.35|55.33|50.96|



#### _3.2. Verification of drought event monitoring accuracy_ 

The drought monitoring accuracies of the VCIs ranged primarily from 90% to 100% (Fig. 4). VCIk achieved the highest average accuracy (91.32%), followed by VCIN (91.19%), while VCIE had the lowest (90.03%). All VCIs showed similar spatial patterns of monitoring accuracy. Areas of high accuracy were concentrated mainly in the central part of Southwest China, with slightly lower accuracies observed in the southeast (Fig. 4ac). Overall, while the VCIs accurately identified drought events during the study period, but there are differences of performance in different VCI. Specifically, VCIk performed slightly better than VCIN, whereas VCIE performed the poorest. 

#### _3.3. Analyzing the monitoring reliability in special drought period_ 

We evaluated the performance of the VCIs during the frequent drought period (2009-2012) and the 2009/2010 drought event (Fig. 5). For the drought period, VCIk demonstrated a markedly higher degree of association with CWSI than both VCIN and VCIE, reflecting its superior ability to track long-term cumulative water deficits (Fig. 5a). Pixel-scale validation during the extreme event (December 2009 to April 2010) further confirms that the nonlinear index more effectively captures the rapid intensification of 



**Fig. 4.** The accuracy of vegetation drought monitoring: (a) VCIN; (b)VCIE; (c) VCIk; (d) area proportion of accuracy. 

8 

_B. Lu et al._ 



<!-- Start of picture text -->
Remote Sensing Applications: Society and Environment 44 (2026) 102281<br><!-- End of picture text -->



**Fig. 5.** The performance of VCIs during the frequent drought period: (a)Temporal variation of VCIs and CWSI; (b ~ d) the scatter density plot of CWSI with VCIN, VCIE, VCIk respectively in the drought event. 



**Fig. 6.** The sensitivity of VCIs to integrated drought stress: (˜ac) spatial Patterns of Sensitivity for VCIN, VCIE, VCIk respectively; (d ~ f) area percentage of sensitivity rank for VCIN, VCIE, VCIk respectively. 

9 

_Remote Sensing Applications: Society and Environment 44 (2026) 102281_ 

_B. Lu et al._ 

moisture stress across the landscape (Fig. 5b-d). Overall, VCIk consistently maintains a performance advantage over traditional linear indices during both prolonged drought cycles and localized extreme events, indicating its robust sensitivity to varying levels of vegetation water stress. 

#### _3.4. Assessing the sensitivity to the integrated drought stress_ 

The explanatory power of VCIk to the integrated drought stress was quantified from the R<sup>2</sup> of the multiple linear regression model at the pixel scale, with the higher explanatory power means that the VCIk is more sensitive to the drought situation (Fig. 6). 

We employed the R<sup>2</sup> from a pixel-scale multiple linear regression model to quantify the sensitivity of each VCI to the combined DIs. In this model, a higher R<sup>2</sup> value indicates greater VCI sensitivity to drought conditions (Fig. 6). Overall, the VCIk showed the strongest sensitivity to the integrated drought stress, followed by VCIN and VCIE. Specifically, the average value of the R<sup>2</sup> was 0.185 for VCIk, 0.133 for VCIN, and 0.097 for VCIE. Spatially, the high sensitivity areas primarily appeared in Guangxi, Yunnan, and eastern Sichuan, while the low sensitivity mainly distributed in the alpine areas of western Sichuan (Fig. 6ac). In terms of area proportion, VCIE had the highest low-sensitivity area (R<sup>2</sup> _<_ 0.1), accounting for 59.1%, while VCIN and VCIk only accounted for 41.92% and 40.58%, respectively (Fig. 6d-f). 

#### _3.5. The dynamic variation in seasonal vegetation drought_ 

The temporal variation of seasonal VCIk and the area proportion of drought were shown in Fig. 7. Among the seasons, VCIk experienced the highest increasing rate of 0.03 year<sup>−1</sup> in spring, with the highest proportion of drought appearing in 2000, accounting for 77.49% (Fig. 7a). VCIk in summer rose at a rate of 0.01 year<sup>−1</sup> , with the highest proportion of drought area being 56.85%, appearing in 2001 (Fig. 7b). The variation of VCIk was similar in autumn and winter, both increasing at a rate of 0.02 year<sup>−1</sup> . The most severe autumnal drought was recorded in 2002, affecting 63.37% of the area (Fig. 7c), while the most severe winter drought occurred in 2000, affecting 69.78% (Fig. 7d). Overall, Southwest China experienced severe drought from 2000 to 2011, and conditions improved from 2012 to 2020. 

Spatially, seasonal variations in vegetation drought exhibited significant spatial heterogeneity, with the rate of change in VCIk ranging from − 0.064 to 0.067 year<sup>−1</sup> (Fig. 8 ad). Among them, the area where VCIk showed an increasing trend was the highest in summer (92.85%), followed by autumn (90.95%) and winter (89.75%), and the lowest in spring, accounting for 76.34% (Fig. 8 e-h). In terms of the persistence of the variation, the area where VCIk displayed an increasing-persistent trend in the future was the highest in 



**Fig. 7.** The temporal variation and area proportion of seasonal vegetation drought: (a) spring; (b) summer; (c) autumn; (d) winter. 

10 

_Remote Sensing Applications: Society and Environment 44 (2026) 102281_ 



**Fig. 8.** The spatial variation of seasonal VCIk: (˜ad) variation slope of seasonal VCIk in spring, summer, autumn, winter respectively; (e ~ h) variation trends of VCIk in spring, summer, autumn, winter respectively; (i ~ l) future trend type of VCIk in spring, summer, autumn, winter respectively. 

winter (81.28%), followed by autumn (80.13%) and spring (71.97%), and the lowest in summer, accounting for 70.56% (Fig. 8 i-l). 

#### _3.6. The spatial patterns and migration of seasonal vegetation drought_ 

The spatial patterns of vegetation drought exhibited seasonal differences (Fig. 9). Overall, seasonal vegetation drought frequencies were primarily between 0.2 and 0.6 (Fig. 9 a). Among the seasons, drought frequency in spring was mainly between 0.2 and 0.6, with high-frequency events occurring predominantly in the northwestern part of Southwest China (Fig. 9b). Drought frequencies were lower in summer and autumn, ranging mainly from 0 to 0.4 (Fig. 9c and d). Winter had the highest drought frequency, which was largely between 0.4 and 0.6, with high-frequency events concentrated in northeastern Southwest China (Fig. 9 e). 

The centroid of drought was concentrated in the central part of study area, located between 103<sup>◦</sup> 27′58″E to 104<sup>◦</sup> 50′23″E and 26<sup>◦</sup> 59′24″N to 28<sup>◦</sup> 0′26″N (Fig. 10). The migration trajectories indicated that the Southwest region was at risk of droughts occurring in two consecutive seasons. Specifically, the centroid of vegetation drought followed similar trajectories in spring and summer, moving in a 'southwest-northwest-southeast' direction (Fig. 10a and b). The drought centroid in autumn and winter followed the same overall trajectory, first moving eastward, then to the northwest, and finally to the southwest (Fig. 10c and d). 

#### **4. Discussion** 

#### _4.1. Validation of different vegetation indices in drought_ 

Under climate change, drought events are expected to become more frequent, making the accurate characterization of drought conditions a central challenge in environmental monitoring (Sheffield and Wood, 2012). The large-scale and long-term vegetation condition information was provided satellite data, which has become an indispensable part of drought monitoring. Indeed, vegetation 

11 

_Remote Sensing Applications: Society and Environment 44 (2026) 102281_ 

_B. Lu et al._ 



**Fig. 9.** The seasonal vegetation drought frequency: (ae) research period, spring, summer, autumn, winter respectively; (f) area proportion of ˜ drought frequency. Note: RP represents the research period. 



**Fig. 10.** The centroid migration of seasonal drought: (ad) in spring, summer, autumn, winter respectively.˜ 

12 

_Remote Sensing Applications: Society and Environment 44 (2026) 102281_ 

_B. Lu et al._ 

status is a key component of many well-established DIs, such as the VCI, the Temperature-Vegetation Dryness Index (TVDI), and the Combined Drought Index (CDI) (Sandholt et al., 2002; Waseem et al., 2015). Therefore, it is crucial to identify which vegetation index most accurately reflects drought stress in vegetation. 

This study used the classic VCI as a proxy for vegetation condition to evaluate drought monitoring effectiveness. We compared VCIs derived from two classic and widely employed linear vegetation indices (NDVI and EVI) and a recently widely interested nonlinear vegetation index (kNDVI). The results consistently show that kNDVI is significantly more effective than NDVI and EVI in vegetation drought monitoring from any perspective. This indicates that kNDVI exhibits amazing potential for drought monitoring, which was not found in previous studies. One explanation for this is the rapid increase in vegetation cover in Southwest China due to extensive afforestation projects (Liu et al., 2022b; Yin et al., 2020). In such high-cover areas, both NDVI and EVI are known to be prone to signal saturation. Our stratified analysis further confirms this, showing that VCIk maintains the highest mean correlation across forests, croplands, and grasslands, with the performance gain being most prominent in forest regions (Fig. S1, Table S1). The mathematical foundation for this superiority lies in the RBF kernel utilized by kNDVI, which maps spectral reflectance into a high-dimensional feature space to capture high-order interactions between bands that linear indices overlook. This nonlinear mapping effectively linearizes the index's response to biophysical parameters, enabling kNDVI to effectively solve the problem of easy saturation and providing a stronger ability to deal with noise and complex phenology. On the other hand, kNDVI has been proved to be the best vegetation index to simulate the change of total primary productivity (GPP) in any kind of biological community (Camps-Valls et al., 2021; Zheng et al., 2023). This allows kNDVI to capture the impacts of drought on vegetation photosynthesis in a manner similar to GPP itself. This functional alignment is critical because GPP reflects physiological carbon fixation which responds to moisture stress through stomatal regulation before structural greenness changes occur. Consequently, kNDVI can detect early functional declines during drought more proactively than the structural proxy NDVI. The superior performance of VCIk is theoretically transferable to other high-biomass ecosystems like boreal regions where nonlinear mapping effectively addresses signal saturation. Conversely, this advantage may be less pronounced in arid environments with sparse vegetation where the relationship between reflectance and biophysical parameters remains relatively linear. 

The robustness of our findings is further supported by a series of sensitivity analyses and statistical tests provided in the Supplementary Material. The performance of VCIk remains remarkably stable across a wide range of the adjustment factor σ (Fig. S2–S4) and is not sensitive to the specific stringency of drought detection criteria (Fig. S5). Furthermore, pixel-level Wilcoxon signed-rank tests confirm that the improvements in monitoring accuracy achieved by VCIk over traditional linear indices are statistically significant across the study area (Fig. S6). 

#### _4.2. Spatiotemporal variation of vegetation drought in southwest China_ 

Southwest China is an important ecological protection area, and under the combined influence of climate and unique topography and geomorphology, vegetation growth status is easily affected by drought (Wang et al., 2021). We therefore constructed a VCI from the kNDVI, an index more sensitive to drought stress, to reveal the spatiotemporal characteristics of seasonal vegetation drought in this ecologically fragile region. The results indicated that, the areas where seasonal drought is still intensifying are primarily distributed in and around the major cities in Sichuan and Yunnan. This finding is consistent with previous research, confirming that these urbanized zones are also drought-prone areas (Li et al., 2019; Liu et al., 2024). The urban heat island effect likely exacerbates drought conditions by increasing air temperatures and the vapor pressure deficit, which in turn affects urban and peri-urban vegetation and its growing environment. Moreover, intensive human activities exert a potential influence. Changes in land cover type can aggravate asymmetries in precipitation patterns, contributing to water shortages during drought events (Huang et al., 2023; Liu et al., 2022a). Notably, seasonal vegetation drought showed a significant recovery trend, with VCIk values in summer, autumn, and winter exhibiting clear increase trends in over 50% of the study area. Meanwhile, the proportion of future VCIk transitioning from increase to decrease and continuing to decrease in these seasons is low, indicating that the drought situation will continue to ease. However, under climate warming, research based on the meteorological drought index tends to indicate that summer drought is gradually increasing, which differs from the results monitored by VCIk in summer (Tang et al., 2021). Notably, the principles underlying these monitoring methods differ significantly. The vegetation conditions were utilized for drought monitoring in VCI rather than climate conditions, to directly reflecting the extent of vegetation affected by drought (Wang et al., 2022a). Specifically, although higher temperatures can reduce soil moisture and trigger drought, abundant precipitation and solar radiation can promote vegetation growth in summer (Hu et al., 2008). Meanwhile, during the peak growing season (July to August), plant can access water from deeper soil to ensure normal growth (Liu et al., 2019). The recovery trend observed in summer further underscores the importance of soil moisture-vegetation coupling. In this period, although surface temperatures remain high, the developed root systems can tap into stable deep-layer soil moisture, acting as a hydrological buffer. Moreover, the superior sensitivity of VCIk allows it to reflect the maintenance of photosynthetic efficiency even during brief dry spells. Unlike structural indices that may fluctuate with minor surface moisture changes, the nonlinear mapping of kNDVI better captures the robust physiological resilience of established canopies in Southwest China, aligning more closely with the actual carbon sequestration rather than simple greenness variations. Furthermore, the drought-resistant plants such as, _Cinnamomum camphora_ , Michelia fulgens and Cephalomappa sinensis were widely planted during ecological restoration projects in Southwest China. These plants maintain a low leaf transpiration rate under drought conditions to avoid excessive water loss, allowing them to sustain stable leaf characteristics under drought stress (Liu et al., 2023). These phenomena result in significant differences between meteorological and vegetation drought. 

Different from other seasons, there are a certain proportion of regions in spring (March to May) showing a worsening trend of drought, with a higher proportion showing a continuous worsening trend compared to other seasons. Temperature and precipitation 

13 

_Remote Sensing Applications: Society and Environment 44 (2026) 102281_ 

_B. Lu et al.                                                                                                                                                                                                              Remote Sensing Applications: Society and Environment_ 

are key drivers causing vegetation drought in spring (Zhou et al., 2019). Influenced by the spring monsoon, the hydrothermal conditions in Southwest China change rapidly over a short period. Meanwhile, with the continuous warming of the climate, spring precipitation decreases, leading to frequent droughts in the spring before the rainy season (Cao et al., 2017; Liu et al., 2022c). During the spring green-up phase, vegetation exhibits heightened physiological sensitivity as leaf emergence and canopy development trigger a rapid increase in transpiration demand. However, because the spring monsoon has not yet delivered substantial rainfall, the shallow soil moisture dynamics are often insufficient to meet this surging water requirement. The mismatch between peak physiological demand and restricted root-zone soil water availability makes the spring season particularly vulnerable to intensifying drought stress. Therefore, future efforts must focus on developing site-specific spring drought mitigation plans, including enhancing water resource management and optimizing irrigation strategies to reduce negative impacts on vegetation. Finally, the historical migration paths of drought centroid in different seasons show that there is a similar migration characteristic in spring and summer (Fig. 10), suggesting the region is prone to persistent, sequential spring-summer droughts. Developing measures to avoid continuous drought events and reducing their impact on the fragile ecosystem in Southwest China are critical issues that require further study. 

The persistence of these sequential spring-summer droughts can be largely explained by hydrological climate memory. Initial soil moisture depletion in spring reduces surface evapotranspiration and latent heat flux, which can suppress local moisture recycling and sustain atmospheric dryness into the summer months, creating a self-reinforcing feedback loop. On the other hand, the widespread recovery observed in summer reflects the vegetation resilience inherent in the forest ecosystems of Southwest China. This resilience is supported by the physiological ability of plants to regulate gas exchange and tap into sub-surface water reservoirs, which mitigates the impact of prolonged dry spells. The superior performance of VCIk in these scenarios further demonstrates its ability to capture the threshold-crossing behaviors associated with vegetation recovery and resilience, providing a more nuanced characterization of drought duration and intensity than traditional indices. 

#### _4.3. Limitations and prospect_ 

Although the performance of NDVI, EVI, and kNDVI in drought monitoring was evaluated using multiple methods, several limitations remain. First, the spatial and temporal resolution of the satellite data may introduce uncertainties. All vegetation indices were derived from MODIS products at a 1 km resolution, which may lead to mixed-pixel issues in the rugged and fragmented terrain of Southwest China. Furthermore, while monthly data are effective for capturing seasonal trends, they may lack the precision required to monitor short-term drought impacts or rapid vegetation recovery dynamics, such as those associated with flash droughts. Second, the validation of VCIs relied on remote sensing-derived drought indices (CWSI, SMCI, and SPEI) rather than in-situ ground observations. The absence of ground-based validation, such as soil moisture sensors or direct plant physiological measurements, remains a limitation in verifying the absolute accuracy of the indices at the local scale. Future studies should aim to integrate multi-source data, including station-based observations and high-resolution UAV imagery, to enhance the robustness of the findings. 

Finally, while this study evaluated three representative indices, the applicability of other emerging indices and the potential for integrating VCIk with comprehensive indicators like the Palmer Drought Severity Index (PDSI) or the Vegetation Health Index (VHI) warrant further investigation (Zeng et al., 2022). Specifically, while PDSI excels in capturing long-term meteorological drought legacies and VHI incorporates surface temperature-related moisture stress, their fusion with the nonlinear kNDVI could provide a more multidimensional characterization of drought. Such cross-index synergy is essential to improve the comprehensiveness of drought monitoring frameworks. In addition, future attention should be directed toward decoupling the impacts of human activities from climate-driven drought signals to facilitate a more profound understanding of regional ecological dynamics. 

#### **5. Conclusions** 

In this study, a novel VCI (VCIk) based on kNDVI was proposed to validate its performance in drought monitoring and reveal the spatiotemporal variation of seasonal vegetation drought in Southwest China from 2000 to 2020. The results demonstrate that VCIk is significantly more effective than traditional VCIN and VCIE. Specifically, the consistency of VCIk with CWSI, SMCI, and SPEI-3 reached 93.61%, 87.43%, and 78.30%, respectively, which exceeded the performance of both linear indices. Furthermore, VCIk exhibited higher sensitivity to integrated drought stress with an R<sup>2</sup> of 0.185, compared to 0.133 for VCIN and 0.097 for VCIE. These findings indicate that the nonlinear mapping of kNDVI provides a more sensitive representation of vegetation stress across the diverse landscapes of Southwest China. 

From 2000 to 2020, seasonal vegetation drought generally exhibited an easing trend, with significant recovery (P _<_ 0.05) observed in 50.96% of the region while only 3.55% showed significant intensification. The seasonal VCIk increased at rates of 0.03 month<sup>−1</sup> in spring and 0.01 month<sup>−1</sup> in summer. However, the intensification of drought near major urban centers suggests that anthropogenic activities and the urban heat island effect may potentially exacerbate moisture stress in peri-urban environments. The observed seasonal disparities, particularly the higher frequency of drought in spring and winter, highlight critical periods of vulnerability for the regional ecosystem. Furthermore, the migration of the drought center of gravity displayed a similar southwest-northwest-southeast trend in both spring and summer, suggesting that the region is prone to persistent and sequential drought events. Overall, this study confirms the strong potential of kNDVI for ecological drought assessment and offers a more reliable tool for monitoring vegetation dynamics in heterogeneous environments. 

14 

_Remote Sensing Applications: Society and Environment 44 (2026) 102281_ 

_B. Lu et al.                                                                                                                                                                                                              Remote Sensing Applications: Society and Environment_ 

#### **CRediT authorship contribution statement** 

**Baiyu Lu:** Writing – review & editing, Writing – original draft, Visualization. **Yuhao Liang:** Writing – review & editing, Writing – original draft, Validation, Methodology, Funding acquisition. **Maijin Lin:** Software, Investigation. **Yungui Lu:** Validation, Supervision. **Donghui Lu:** Formal analysis. 

#### **Funding** 

The research leading to these results received funding from Guangxi Natural Science Foundation under Grant Agreement No 2025GXNSFAA069733. 

#### **Declaration of competing interest** 

The authors declare the following financial interests/personal relationships which may be considered as potential competing interests Yuhao Liang reports financial support was provided by Guangxi Natural Science Foundation. If there are other authors, they declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

#### **Acknowledgements** 

We would like to express our sincere gratitude to the research team "Wen Jie De Ma Zai Men" for their collaborative efforts and essential support throughout this study. Specifically, we acknowledge Haochen Yu, Yuwen Li, Yunyi Chen, Kun Huang, Jianming Li, Xianrui Li, Zejun Li, Senyao Luo, Qi Qiu and Jun Yan for their technical support. 

#### **Appendix A. Supplementary data** 

Supplementary data to this article can be found online at https://doi.org/10.1016/j.rsase.2026.102281. 

#### **Data availability** 

No datasets were generated or analysed during the current study. Data sets generated during the current study are available from the corresponding author on reasonable request. 

#### **References** 

- Branco, E.R.F., dos Santos, A.R., Pezzopane, J.E.M., dos Santo, A.B., Alexandre, R.S., Bernardes, V.P., da Silva, R.G., de Souza, K.B., Moura, M.M., 2019. Space-time analysis of vegetation trends and drought occurrence in domain area of tropical forest. J. Environ. Manag. 246, 384–396. 

Camps-Valls, G., Campos-Taberner, M., Moreno-Martínez, A., Walther, S., Duveiller, G., Cescatti, A., Mahecha, M.D., Munoz-Marí, J., García-Haro, F.J., Guanter, L., ˜ 

Jung, M., Gamon, J.A., Reichstein, M., Running, S.W., 2021. A unified vegetation index for quantifying the terrestrial biosphere. Sci. Adv. 7. Cao, J., Zhang, W.K., Tao, Y., 2017. Thermal configuration of the Bay of Bengal-Tibetan Plateau Region and the May precipitation anomaly in Yunnan. J. Clim. 30, 9303–9319. 

- Cao, S.P., Zhang, L.F., He, Y., Zhang, Y.L., Chen, Y., Yao, S., Yang, W., Sun, Q., 2022. Effects and contributions of meteorological drought on agricultural drought under different climatic zones and vegetation types in Northwest China. Sci. Total Environ. 821. 

- Cheng, Y.J., Zhang, K., Chao, L.J., Shi, W.Z., Feng, J., Li, Y.P., 2023. A comprehensive drought index based on remote sensing data and nested copulas for monitoring meteorological and agroecological droughts: a case study on the Qinghai-Tibet Plateau. Environ. Model. Softw. 161. 

- Cui, J., Chen, A., Huntingford, C., Piao, S., 2024. Integrating ecosystem water demands into drought monitoring and assessment under climate change. Nat. Water 2, 215–218. 

- Fan, M.T., Xu, J.H., Yu, W.Z., Chen, Y.N., Wang, M.H., Dai, W., Wang, Y.W., 2023. Recent Tianshan warming in relation to large-scale climate teleconnections. Sci. Total Environ. 856. 

- Hao, C., Zhang, J.H., Yao, F.M., 2015. Combination of multi-sensor remote sensing data for drought monitoring over Southwest China. Int. J. Appl. Earth Obs. Geoinf. 35, 270–283. 

- Hu, Z.M., Yu, G.R., Fu, Y.L., Sun, X.M., Li, Y.N., Shi, P.L., Wangw, Y.F., Zheng, Z.M., 2008. Effects of vegetation control on ecosystem water use efficiency within and among four grassland ecosystems in China. Glob. Change Biol. 14, 1609–1619. 

- Huang, S.Z., Gan, Y., Zhang, X., Chen, N.C., Wang, C., Gu, X.H., Ma, J.J., Niyogi, D., 2023. Urbanization amplified asymmetrical changes of rainfall and exacerbated drought: analysis over five urban agglomerations in the Yangtze River Basin, China. Earths Future 11. 

Jackson, R.D., Kustas, W.P., Choudhury, B.J., 1988. A reexamination of the crop water stress index. Irrig. Sci. 9, 309–317. 

- Jiao, W.Z., Wang, L.X., McCabe, M.F., 2021. Multi-sensor remote sensing for drought characterization: current status, opportunities and a roadmap for the future. Remote Sens. Environ. 256. 

- Jiao, W.Z., Wang, L.X., Novick, K.A., Chang, Q., 2019. A new station-enabled multi-sensor integrated index for drought monitoring. J. Hydrol. 574, 169–180. 

- Kogan, F.N., 1995. Droughts of the late 1980s in the United States as derived from NOAA polar-orbiting satellite data. Bull. Am. Meteorol. Soc. 76, 655–668. Li, K.W., Tong, Z.J., Liu, X.P., Zhang, J.Q., Tong, S.Q., 2020. Quantitative assessment and driving force analysis of vegetation drought risk to climate change: methodology and application in Northeast China. Agric. For. Meteorol. 282. 

- Li, Q.L., Shi, G.S., Shangguan, W., Nourani, V., Li, J.D., Li, L., Huang, F.N., Zhang, Y., Wang, C.Y., Wang, D.G., Qiu, J.X., Lu, X.J., Dai, Y.J., 2022. A 1 km daily soil moisture dataset over China using in situ measurement and machine learning. Earth Syst. Sci. Data 14, 5267–5286. 

- Li, X.Y., Li, Y., Chen, A.P., Gao, M.D., Slette, I.J., Piao, S.L., 2019. The impact of the 2009/2010 drought on vegetation growth and terrestrial carbon balance in Southwest China. Agric. For. Meteorol. 269, 239–248. 

15 

_B. Lu et al.                                                                                                                                                                                                              Remote Sensing Applications: Society and Environment 44 (2026) 102281_ 

- Li, Y., Zhang, W., Schwalm, C.R., Gentine, P., Smith, W.K., Ciais, P., Kimball, J.S., Gazol, A., Kannenberg, S.A., Chen, A.P., Piao, S.L., Liu, H.Y., Chen, D.L., Wu, X.C., 2023. Widespread spring phenology effects on drought recovery of Northern Hemisphere ecosystems. Nat. Clim. Change 13, 182-+. 

- Li, Z.W., Sun, F.B., Wang, H., Wang, T.T., Feng, Y., 2024. Detecting the interactions between vegetation greenness and drought globally. Atmos. Res. 304. 

- Liu, H.Q., Huete, A., 1995. A feedback based MODIFICATION OF the NDVI to MINIMIZE canopy background and atmospheric noise. IEEE Trans. Geosci. Remote Sens. 33, 457–465. 

- Liu, H.Y., Zou, L., Xia, J., Chen, T., Wang, F.Y., 2022a. Impact assessment of climate change and urbanization on the nonstationarity of extreme precipitation: a case study in an urban agglomeration in the middle reaches of the Yangtze river. Sustain. Cities Soc. 85. 

- Liu, J.C., Shen, L.C., Wang, Z.X., Duan, S.H., Wu, W., Peng, X.Y., Wu, C., Jiang, Y.J., 2019. Response of plants water uptake patterns to tunnels excavation based on stable isotopes in a karst trough valley. J. Hydrol. 571, 485–493. 

- Liu, S.H., Xue, L.Q., Xiao, Y., Yang, M.J., Liu, Y.H., Han, Q., Ma, J.T., 2024. Dynamic process of ecosystem water use efficiency and response to drought in the Yellow River Basin, China. Sci. Total Environ. 934. 

- Liu, Y., Ding, Z., Chen, Y.A., Yan, F.Q., Yu, P.J., Man, W.D., Liu, M.Y., Li, H., Tang, X.G., 2023. Restored vegetation is more resistant to extreme drought events than natural vegetation in Southwest China. Sci. Total Environ. 866. 

- Liu, Y.C., Li, Z., Chen, Y.N., Li, Y.P., Li, H.W., Xia, Q.Q., Kayumba, P.M., 2022b. Evaluation of consistency among three NDVI products applied to High Mountain Asia in 2000-2015. Remote Sens. Environ. 269. 

- Liu, Y.Y., Hu, Z.Z., Wu, R.G., Yuan, X., 2022c. Agricultural water MANAGEMENTAPPLIED ECOLOGY and environmental research. Adv. Atmos. Sci. 39, 1766–1776. Lu, X.-j., Li, Z.-b., Yan, H.-b., Liang, Y.-j., 2023. Spatiotemporal variations of drought and driving factors based on multiple remote sensing drought indices: a case study in karst areas of southwest China. J. Mt. Sci. 20, 3215–3232. 

- Mendicino, G., Senatore, A., Versace, P., 2008. A Groundwater Resource Index (GRI) for drought monitoring and forecasting in a mediterranean climate. J. Hydrol. 357, 282–302. 

- Mirabbasi, R., Anagnostou, E.N., Fakheri-Fard, A., Dinpashoh, Y., Eslamian, S., 2013. Analysis of meteorological drought in northwest Iran using the Joint Deficit Index. J. Hydrol. 492, 35–48. 

- Mishra, A.K., Singh, V.P., 2010. A review of drought concepts. J. Hydrol. 391, 204–216. 

- Peng, S.Z., Ding, Y.X., Liu, W.Z., Li, Z., 2019. 1 km monthly temperature and precipitation dataset for China from 1901 to 2017. Earth Syst. Sci. Data 11, 1931–1946. Rouse, J.W., Haas, R.H., Schell, J.A., Deering, D.W., 1974. Monitoring vegetation systems in the Great Plains with ERTS. NASA Spec. Publ, vol. 351, p. 309. 

Sandholt, I., Rasmussen, K., Andersen, J., 2002. A simple interpretation of the surface temperature/vegetation index space for assessment of surface moisture status. Remote Sens. Environ. 79, 213–224. 

- Schwalm, C.R., Anderegg, W.R.L., Michalak, A.M., Fisher, J.B., Biondi, F., Koch, G., Litvak, M., Ogle, K., Shaw, J.D., Wolf, A., 2017. Global patterns of drought recovery. Nature 548, 202–205. 

- Senhorelo, A.P., de Sousa, E.F., dos Santos, A.R., Ferrari, J.L., Peluzio, J.B.E., Zanetti, S.S., Carvalho, R.D.F., Camargo, C.B., de Souza, K.B., Moreira, T.R., Costa, G.A., Kunz, S.H., Dias, H.M., 2023. Application of the vegetation condition index in the diagnosis of spatiotemporal distribution of agricultural droughts: a case study concerning the state of Espirito Santo, Southeastern Brazil. Diversity 15. 

- Sheffield, J., Wood, E.F., 2012. Drought: past Problems and Future Scenarios. Routledge. 

- Tang, H., Wen, T., Shi, P., Qu, S.M., Zhao, L.L., Li, Q.F., 2021. Analysis of characteristics of hydrological and meteorological drought evolution in Southwest China. Water 13. 

Vicente-Serrano, S.M., Beguería, S., Lopez-Moreno, J.I., 2010. A multiscalar drought index sensitive to global warming: the standardized precipitation ´ evapotranspiration index. J. Clim. 23, 1696–1718. 

- Vicente-Serrano, S.M., Quiring, S.M., Pena-Gallardo, M., Yuan, S.S., Domínguez-Castro, F., 2020. A review of environmental droughts: increased risk under global ˜ warming? Earth Sci. Rev. 201. 

- Wang, F., Lai, H.X., Li, Y.B., Feng, K., Zhang, Z.Z., Tian, Q.Q., Zhu, X.M., Yang, H.B., 2022a. Dynamic variation of meteorological drought and its relationships with agricultural drought across China. Agric. Water Manag. 261. 

- Wang, M., Ding, Z., Wu, C.Y., Song, L.S., Ma, M.G., Yu, P.J., Lu, B.Q., Tang, X.G., 2021. Divergent responses of ecosystem water-use efficiency to extreme seasonal droughts in Southwest China. Sci. Total Environ. 760. 

- Wang, Q., Moreno-Martinez, A., Munoz-Mari, J., Campos-Taberner, M., Camps-Valls, G., 2023a. Estimation of vegetation traits with kernel NDVI. ISPRS J. Photogramm. Remote Sens. 195, 408–417. 

- Wang, X., Biederman, J.A., Knowles, J.F., Scott, R.L., Turner, A.J., Dannenberg, M.P., Kohler, P., Frankenberg, C., Litvak, M.E., Flerchinger, G.N., Law, B.E., Kwon, H., ¨ Reed, S.C., Parton, W.J., Barron-Gafford, G.A., Smith, W.K., 2022b. Satellite solar-induced chlorophyll fluorescence and near-infrared reflectance capture complementary aspects of dryland vegetation productivity dynamics. Remote Sens. Environ. 270. 

- Wang, Y.H., Wu, Y.F., Ji, L., Zhang, J.S., Meng, L.H., 2023b. Assessing the spatial-temporal pattern of Spring maize drought in Northeast China using an optimised remote sensing index. Remote Sens. 15. 

Waseem, M., Ajmal, M., Kim, T.W., 2015. Development of a new composite drought index for multivariate drought assessment. J. Hydrol. 527, 30–37. 

Wmo, 2009. Inter-Regional Workshop on Indices and Early Warning Systems for Drought. Lincoln Nebraska, pp. 8–11. 

Xiang, W., Tan, M., Yang, X., Li, X., 2022. The impact of cropland spatial shift on irrigation water use in China. Environ. Impact Assess. Rev. 97, 106904. 

Xu, X.J., Liu, J., Jiao, F.S., Zhang, K., Ye, X., Gong, H.B., Lin, N.A., Zou, C.X., 2023. Ecological engineering induced carbon sinks shifting from decreasing to increasing during 1981-2019 in China. Sci. Total Environ. 864. 

Yan, H.B., Zhou, G.Q., Lu, X.J., 2023. Surface soil moisture retrieval through combining LST-VI feature space with soil porosity. Int. J. Remote Sens. 44, 517–541. 

- Yan, K., Wang, W.F., Li, Y.H., Wang, X.F., Jin, J.X., Jiang, J., Yang, H.Q., Wang, L.J., 2022. Identifying priority conservation areas based on ecosystem services change driven by Natural Forest protection project in Qinghai province, China. J. Clean. Prod. 362. 

Yin, L., Dai, E.F., Zheng, D., Wang, Y.H., Ma, L., Tong, M., 2020. What drives the vegetation dynamics in the Hengduan Mountain region, southwest China: climate change or human activity? Ecol. Indic. 112. 

- Zeng, J.Y., Zhang, R.R., Qu, Y.P., Bentod, V.A., Zhou, T., Lin, Y.H., Wu, X.P., Qi, J.Y., Shui, W., Wang, Q.F., 2022. Improving the drought monitoring capability of VHI at the global scale via ensemble indices for various vegetation types from 2001 to 2018. Weather Clim. Extrem. 35, 14. 

- Zhang, A.Z., Jia, G.S., 2013. Monitoring meteorological drought in semiarid regions using multi-sensor microwave remote sensing data. Remote Sens. Environ. 134, 12–23. 

Zhang, J.Y., Dai, M.H., Wang, L.C., Su, W.C., 2016. Household livelihood change under the rocky desertification control project in karst areas, Southwest China. Land Use Policy 56, 8–15. 

- Zhang, M.J., He, J.Y., Wang, B.L., Wang, S.J., Li, S.S., Liu, W.L., Ma, X.N., 2013. Extreme drought changes in Southwest China from 1960 to 2009. J. Geogr. Sci. 23, 3–16. 

Zhang, Y.J., Xu, M., Chen, H., Adams, J., 2009. Global pattern of NPP to GPP ratio derived from MODIS data: effects of ecosystem type, geographical location and climate. Glob. Ecol. Biogeogr. 18, 280–290. 

- Zheng, Z.J., Schmid, B., Zeng, Y., Schuman, M.C., Zhao, D., Schaepman, M.E., Morsdorf, F., 2023. Remotely sensed functional diversity and its association with productivity in a subtropical forest. Remote Sens. Environ. 290. 

- Zhou, Y., Zhang, R., Wang, S.X., Wang, F.T., Qi, Y., 2019. Comparative analysis on responses of vegetation productivity relative to different drought monitor patterns in karst regions of southwestern China. Appl. Ecol. Environ. Res. 17, 85–105. 

16 

