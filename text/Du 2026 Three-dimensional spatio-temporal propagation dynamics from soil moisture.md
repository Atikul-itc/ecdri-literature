Journal of Hydrology: Regional Studies 67 (2026) 103786 



Contents lists available at ScienceDirect 

# Journal of Hydrology: Regional Studies 

journal homepage: www.elsevier.com/locate/ejrh 



Three-dimensional spatio-temporal propagation dynamics from soil moisture to vegetation droughts across different eco-geographical regions of China 



Yuxuan Du<sup>a</sup> , Tao Peng<sup>a,*</sup> , Vijay P. Singh<sup>b,c</sup> , Ji Liu<sup>a</sup> , Xiaohua Dong<sup>a</sup> , Qingxia Lin<sup>a</sup> , Jiali Guo<sup>a</sup> , Chao Song<sup>a</sup> , Dan Yu<sup>a</sup> , Gaoxu Wang<sup>d</sup> 

a _Hubei Provincial Key Laboratory of Construction and Management in Hydropower Engineering, and Engineering Research Center of Ecoenvironment in Three Gorges Reservoir Region, Ministry of Education, China Three Gorges University, Yichang 443002, China_ b _6848 Truxton Drive, Dallas, TX 75231, USA_ c _National Water & Energy Center, UAE University, Al Ain, UAE_ 

d _State Key Laboratory of Hydrology-Water Resources and Hydraulic Engineering, Nanjing Hydraulic Research Institute, Nanjing 210029, China_ 

A R T I C L E I N F O A B S T R A C T 

_Keywords: Study region:_ China. Soil moisture drought _Study focus:_ This study investigated the propagation from soil moisture drought (SD) to vegetation Vegetation drought drought (VD) across China during 1981–2020 using a three-dimensional (3-D) spatio-temporal Drought propagationThree-dimensional clustering clustering framework. SD and VD events were identified based on the Standardized Soil MoisChina ture Index (SSMI) and Standardized Vegetation Health Index (SVHI), respectively. A spatiotemporal matching algorithm was developed to pair SD and VD events, enabling a quantitative analysis of propagation characteristics (i.e., propagation time, rate, direction, distance, probability, and thresholds). The key contributors were identified using an integrated XGBoost-SHAP approach. _New hydrological insights for the region:_ This study identified 144 SD and 59 VD events, among which 24 were successfully matched as propagation events. The average propagation time from SD to VD was 3.76 months, exhibiting a distinct west-to-east gradient. The thresholds for triggering VD increased with drought severity, with SD duration thresholds ranging from 1 to 6 months across most regions. Regional contributors to drought propagation time varied across China: energy-related factors were primary in humid regions, precipitation (PRE) in arid zones, and temperature (TMP) and root-zone soil moisture (SMrz) in semi-arid areas. This study provides a comprehensive framework for understanding multi-dimensional drought propagation and offers scientific support for drought early warning and ecological risk management in China. 

## **1. Introduction** 

Drought, a natural hazard characterized by its high frequency, prolonged duration, and extensive spatial coverage (Wilhite and Glantz, 1985; Van Loon, 2015; Ault, 2020), represents one of the most widespread disasters affecting societies and terrestrial ecosystems (Dai, 2013; Cook et al., 2018; Das et al., 2022; Chen et al., 2025a). It typically originates from precipitation deficits, which can 

* Corresponding author. 

_E-mail address:_ pengtao306@163.com (T. Peng). 

https://doi.org/10.1016/j.ejrh.2026.103786 

Received 15 March 2026; Received in revised form 15 July 2026; Accepted 22 July 2026 

Available online 5 August 2026 

2214-5818/© 2026 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license ( http://creativecommons.org/licenses/by-nc-nd/4.0/ ). 

_Journal of Hydrology: Regional Studies 67 (2026) 103786_ 

_Y. Du et al.                                                                                                                                                                                                              Journal of Hydrology: Regional Studies_ 

subsequently trigger reductions in river flow and groundwater levels, diminished soil moisture (SM), decreased vegetation productivity, and inadequate water resources availability for use (Wilhite and Glantz, 1985; Mishra and Singh, 2010; Hua et al., 2019). Based on causative factors and impacts, droughts are typically categorized into four types: meteorological, hydrological, agricultural (or SM), and socioeconomic drought. These categories are not isolated but interlinked through the hydrological cycle, a process known as drought propagation (Peters et al., 2003; Van Loon et al., 2012). However, prevailing drought classification schemes predominantly adopt an anthropocentric perspective, emphasizing the impacts of reduced precipitation on water resource systems and water usage, while paying limited attention to ecosystem responses, particularly the mechanisms through which vegetation reacts to soil moisture drought (SD) (Crausbay et al., 2017). In recent decades, the intensification of global drought severity has mainly been attributed to the increased atmospheric evaporative demand (AED) rather than merely a reduction in precipitation (Gebrechorkos et al., 2025), ultimately leading to vegetation degradation as a result of intensified SM deficiency. Therefore, a deeper understanding of the propagation from SD to vegetation drought (VD) is essential for elucidating the response mechanism of vegetation to drought stress. This knowledge also provides a theoretical basis and practical guidance for vegetation management and sustainable ecosystem development (Vicente-Serrano et al., 2013; Seddon et al., 2016). 

Drought propagation, which refers to the process through which one type of drought evolves into another, plays a pivotal role in drought monitoring, impact assessment, and early warning systems (Fang et al., 2020; Warter et al., 2021). Consequently, it has become a major research focus in meteorology and hydrology (Apurv et al., 2017; Guo et al., 2020). For instance, Huang et al. (2017) identified seasonal patterns in propagation from meteorological to hydrological drought in the Wei River basin, China, while Feng et al. (2024b) illustrated convergence, prolongation, lag, and attenuation effects during the transition from meteorological to agricultural drought. These studies have collectively advanced the understanding of cross-system drought propagation and established methodological foundations for drought impact assessment. However, existing research has largely centered on the propagation from meteorological to hydrological, agricultural, or socio-economic drought (Van Loon, 2015), leaving the propagation processes within vegetation ecosystems relatively underexplored. Persistent drought conditions can lead to significant SM deficits, thereby suppressing vegetation productivity (Zhao et al., 2023a; Wang et al., 2025), underscoring a strong intrinsic linkage between SD and VD. Thus, clarifying this relationship is crucial for comprehensively understanding vegetation response to drought and for improving drought early warning. 

Previous studies on drought event identification and propagation have mainly followed two approaches: hydrological model simulation and statistical analysis (Han et al., 2019). The former employs physically-based models to represent hydrological processes and simulate the propagation from meteorological drought to other types (Van Lanen et al., 2013). For example, Wang et al. (2011) utilized coupled models to investigate the propagation mechanisms from meteorological to agricultural and hydrological droughts in central Illinois, USA. Although such models can reveal underlying propagation mechanisms, they require massive data support and parameter calibration, and their applicability to large-scale regions is limited by model structure and parameter uncertainties (Huang et al., 2017). In contrast, statistical methods are computationally efficient and widely used to identify drought events and examine propagation across drought types. Li et al. (2018), for instance, applied a threshold-based method to identify drought events and their characteristics, revealing the propagation patterns from meteorological to hydrological and agricultural droughts. Additionally, the integration of run theory with copula functions has provided valuable references for regional drought risk assessment (Ayantobo et al., 2019; Wang et al., 2020, 2022). However, most traditional methods focus primarily on either temporal or spatial dimensions of drought, with limited consideration of their spatio-temporal continuity, potentially leading to biased interpretations of large-scale drought propagation (Jiang et al., 2022b). 

In recent years, a three-dimensional (3-D) clustering method, proposed by Lloyd-Hughes (2012), has gained popularity as an effective approach for drought identification. Unlike low-dimensional analysis, this method simultaneously accounts for three dimensions: longitude, latitude, and time. Xu et al. (2015) proposed a 3-D clustering method that simultaneously considers temporal and spatial continuity to characterize drought events. Building on this approach, Zhu et al. (2024) identified ecological drought events across China and examined the migration and evolution, while Wang et al. (2024a) applied the same 3-D identification algorithm to detect meteorological and vegetation drought events in the Yellow River basin, China, delineating the evolution of representative events. Nevertheless, studies employing the 3-D clustering method have primarily focused on identifying drought characteristics within individual categories. In contrast, the application of this approach to investigate propagation mechanisms among different drought categories has received relatively less attention. This gap has somewhat hindered a holistic understanding of drought causation and overall propagation behavior (Jiang et al., 2022b; Wang et al., 2024a). 

China's vast territory and complex topography encompass diverse climatic zones, ranging from humid monsoon regions in the east to arid inland areas in the northwest, resulting in pronounced spatial heterogeneity in climatic conditions (Wang et al., 2023). These variations significantly affect the dynamics of SM. As a critical phase in the drought process, SD directly influences soil water storage and plant-available water (Van Loon, 2015; Ge et al., 2025). In contrast, VD is manifested through delayed physiological responses and degradation in vegetation health (Allen et al., 2010). Given the tight coupling between soil and vegetation systems, the propagation from SD to VD not only reflects drought progression but also has direct implications for ecosystem stability and agricultural productivity (Sawada, 2018; Liu et al., 2023). Therefore, investigating the propagation from SD to VD at the national scale in China is crucial for understanding drought mechanisms, improving early warning systems, and enhancing ecological resilience. 

This study aimed to identify SD and VD events across China and to establish matched pairs between them at the event-level. By quantitatively characterizing the temporal and spatial continuity as well as the dependencies linking these two drought types, we innovatively elucidated the spatio-temporal evolution patterns within drought propagation chains. The specific objectives were to: (1) identify SD and VD events using a 3-D framework; (2) integrate temporal and spatial matching methods to uncover the spatio-temporal propagation characteristics from SD to VD; (3) investigate the propagation probability and threshold from SD to VD; and (4) identify 

2 

_Journal of Hydrology: Regional Studies 67 (2026) 103786_ 

_Y. Du et al._ 

the key contributors of drought propagation. Overall, this study explored the spatio-temporal propagation between SD and VD, examined regional disparities and spatial heterogeneity, and aimed to provide a scientific basis for regional drought mitigation and ecological management strategies. 

## **2. Study area and datasets** 

## _2.1. Study area_ 

China is located in the east of the Eurasian continent (4<sup>◦</sup> –53.5<sup>◦</sup> N, 73.5<sup>◦</sup> –135<sup>◦</sup> E), spanning a vast territory of approximately 9.6 million km<sup>2</sup> . It exhibits a remarkable diversity of climate types, ranging from hot and humid in the southeast to cold and dry in the northwest. Precipitation is characterized by distinct seasonal and regional variations: generally higher in summer and lower in winter, with amounts gradually decreasing from the southeastern coast toward the northwestern interior (Wei et al., 2020). Topographically, the country is marked by higher elevations in the west and lower in the east, forming a three-step descending staircase. Nearly two-thirds of the nation’s territory is characterized by mountainous, plateau, and hilly terrain, whereas plains and basins comprise roughly one-third of the total land area (Wang et al., 2023). 

As proposed by Zheng (1999), China can be divided into nine eco-geographical regions based on terrain, vegetation, and climate (Fig. 1), including cold temperate humid (I), mid-temperate humid and sub-humid (II), warm-temperate humid and sub-humid (III), northern subtropical humid (IV), mid-subtropical humid (V), southern subtropical and tropical humid (VI), northern semi-arid (VII), northwestern arid (VIII), and the Qinghai-Tibet Plateau alpine (IX) regions. This regionalization framework highlights climatic conditions and inter-regional differences and supports ecological conservation and construction planning. It also provides a macro-regional framework for studying physical processes affecting climate, as well as for harmonizing environmental protection, resource utilization, and sustainable economic development (Zong et al., 2024). 

## _2.2. Datasets_ 

ERA5-Land SM reanalysis data were used as the primary SM dataset in this study. This dataset offers spatially continuous, long-term land surface information and has demonstrated relatively high accuracy compared with other remote sensing and reanalysis SM products (Munoz-Sabater et al., 2021; Zhang et al., 2021; Xing et al., 2023˜ ). It features a spatial resolution of 0.1<sup>◦</sup> × 0.1<sup>◦</sup> and covers the period from 1981 to 2020 (https://cds.climate.copernicus.eu). Specifically, SM data from the 0–7 cm were selected, as this surface soil layer responds rapidly to external forcing such as precipitation deficits, enhanced evapotranspiration, and rising temperature, thereby effectively capturing the onset and early development of SD (Seneviratne et al., 2010). To assess the robustness of the results derived from the ERA5-Land 0–7 cm surface SM, three additional SM datasets, namely GLDAS Noah (Rodell et al., 2004), GLEAM (Miralles et al., 2025), and SiTHv2 (Zhang et al., 2024), were introduced for comparative validation (see Supplementary Table 1 for details). In addition, 0–100 cm root-zone SM (RZSM) was calculated from the ERA5-Land multilayer SM data to serve as a supplementary comparison indicator. Following Deng et al. (2024), RZSM was calculated as the weighted average of ERA5-Land SM from the 0–7 cm, 7–28 cm, and 28–100 cm layers, with weights of 0.07, 0.21, and 0.72, respectively. 

The Vegetation Health Index (VHI) has been extensively used for drought monitoring, vegetation health assessment, and ecological response analyses at global and regional scales (Bento et al., 2018). In this study, an improved high-resolution VHI dataset developed by Zeng et al. (2023) was utilized. This dataset covers the period of 1981–2020 at a spatial resolution of 4 km, extending from 50<sup>◦</sup> S to 70<sup>◦</sup> N and 180<sup>◦</sup> W to 180<sup>◦</sup> E. This dataset is publicly available via the figshare repository (https://doi.org/10.6084/m9.figshare. 19811854.v5). The China Land Cover Dataset (CLCD), derived from Yang and Huang (2021), was adopted to represent land cover types across China. It classifies the country into nine categories (Fig. 1a), effectively capturing the structural characteristics of terrestrial ecosystems. Widely used in studies of land use change and ecological environment assessment, the CLCD is available at https://doi.org/10.5281/zenodo.4417810. The DEM data were acquired from the Geospatial Data Cloud of the Chinese Academy of 



**Fig. 1.** Land use (a), elevation (b), and eco-geographical regions in China. 

3 

_Journal of Hydrology: Regional Studies 67 (2026) 103786_ 

_Y. Du et al.                                                                                                                                                                                                              Journal of Hydrology: Regional Studies_ 

Sciences (http://www.gscloud.cn), providing reliable support for terrain-related analyses. 

For the attribution analysis based on the XGBoost and SHAP algorithms, the following datasets from 1981 to 2020 were employed in this study. Mean annual precipitation (PRE), mean annual temperature (TMP), and sunshine duration (SunD) were obtained from the Zenodo repository (https://zenodo.org/records/10963932). The CO2 data used in this study were obtained from the global atmospheric CO2 concentration dataset released by Cheng et al. (2022) (https://zenodo.org/records/5021361). Mean annual solar radiation (RAD) datasets were provided by the National Tibetan Plateau Data Center (http://data.tpdc.ac.cn) (Feng and Wang, 2021). Mean annual root-zone SM (SMrz) and mean annual vegetation transpiration (T_veg) datasets were accessed from the official GLEAM platform (https://doi.org/10.1038/s41597− 025–04610-y). The soil texture index, sand-to-silt ratio (SASI), was calculated based on 



**Fig. 2.** Framework of this study. 

4 

_Journal of Hydrology: Regional Studies 67 (2026) 103786_ 

_Y. Du et al.                                                                                                                                                                                                              Journal of Hydrology: Regional Studies_ 

the China soil characteristics dataset developed by Shangguan et al. (2013) (http://globalchange). The normalized difference vegetation index (NDVI) was derived from the MOD13A3 product (https://www.earthdata.nasa.gov/), and maximum root depth (MRD) data were obtained from https://wci.earth2observe.eu/thredds/catalog/usc/root-depth/catalog.html. All spatial datasets utilized in this study were uniformly resampled at a resolution of 0.1<sup>◦</sup> × 0.1<sup>◦</sup> using the bilinear interpolation method. 

## **3. Methods** 

Fig. 2 illustrates the overall technical workflow of this study. Standardized drought indices, based on SM and VHI, were constructed to characterize SD and VD, respectively. Drought events were identified using a 3-D clustering method, from which key characteristic variables (e.g., duration, severity, affected area, and orientation direction) were extracted. Subsequent spatio-temporal matching was applied to pair SD and VD events, thereby filtering out associated propagation processes. The matched events were then integrated and categorized to distinguish different types of propagation relationships. Following this, the propagation from SD to VD was quantitatively analyzed in both temporal and spatial dimensions, including propagation time, rate, direction, distance, probability, and thresholds, thereby systematically revealing its spatio-temporal evolution characteristics. Finally, XGBoost and SHAP approaches were employed to analyze the drought propagation process in order to identify the key contributors and underlying mechanisms. 

## _3.1. Drought indices_ 

In this study, SSMI and SVHI were adopted to represent SD and VD, respectively. The standardization procedure followed the methodology of the Standardized Precipitation Index (SPI) and was implemented in three steps. 

Step 1: Data preprocessing. For the original SM and VHI series _xi_ at each grid cell, a min-max normalization was applied to obtain the transformed series _yi_ : 



To avoid the influence of extreme values, the values of 0 and 1 in _yi_ were replaced with 0.001 and 0.999, respectively. Step 2: Probability distribution fitting. Three common distributions (i.e., Gamma, log-logistic, and Pearson Type III) were employed to fit the _yi_ series and obtain the probability density function (PDF). The optimal distribution was determined using the Akaike Information Criterion (AIC). 

Step 3: Standardized index calculation. The cumulative distribution function (CDF) was derived from the selected optimal distribution and then converted into the standardized drought index (SDI) via the inverse standard normal transformation, yielding the SSMI and SVHI: 





where _SDI_ denotes SSMI or SVHI, _yi_ is the preprocessed time series of SM and VHI data, and _fyi_ ( _u_ ) and _Fyi_ ( _t_ ) are the PDF and CDF of the selected optimal distribution, respectively. 

Following the drought classification framework introduced by McKee et al. (1993), the classification criteria for SDI (i.e., SSMI and SVHI) are presented in Table 1. 

## _3.2. Drought identification from a three-dimensional perspective_ 

## _3.2.1. Identification of drought events_ 

Drought events are typically characterized as continuous spatio-temporal entities; therefore, the 3-D clustering algorithm was utilized for the spatial detection and temporal connection of drought patches. 

Step 1: Spatial detection of drought patches. 

Each month, grid points with an SSMI (or SVHI) value below − 1 were regarded as drought-affected cells. Each cell in the monthly gridded dataset was encoded as 1 if affected by drought, and 0 otherwise. Drought patches were then delineated based on spatial continuity. Specifically, a 3 × 3 moving window was employed to scan the binary grid and identify adjacent drought cells (i.e., grid 

**Table 1** 

Drought classification criteria based on SDI. 

|Level|Classification|SDI|
|---|---|---|
|1|No drought|−0.5_<_SDI|
|2|Mild drought|−1.0_<_SDI≤−0.5|
|3|Moderate drought|−1.5_<_SDI≤−1.0|
|4|Severe drought|−2.0_<_SDI≤−1.5|
|5|Extreme drought|SDI≤−2.0|



5 

_Journal of Hydrology: Regional Studies 67 (2026) 103786_ 

_Y. Du et al.                                                                                                                                                                                                              Journal of Hydrology: Regional Studies_ 

cells with a value of 1). The 3 × 3 window corresponded to the eight-neighbor connectivity rule in raster data, which accounted for adjacent grids in the horizontal, vertical, and diagonal directions and thus effectively captured the spatially continuous distribution of drought patches. Spatially connected drought cells were merged into a single drought patch according to a pixel-adjacency rule, forming a spatial connectivity network for the initial identification of drought patches. To eliminate noise from small-scale anomalies or atypical drought signals, patches with an area smaller than a minimum area threshold (denoted as _H_ ) were excluded. The remaining patches that satisfied the spatial continuity criterion and the minimum area requirement were considered individual drought events for that month. 

Step 2: Temporal connection of drought patches. 

The temporal linkage between drought patches in consecutive months was identified by evaluating their overlapping areas. Assuming that month _i_ contains _N_ drought patches and month _i_ + 1 contains _M_ patches, if the overlapping area between any patch in _N_ and any patch in _M_ exceeds the minimum threshold _H_ , those patches are considered part of the same drought event. This matching procedure was repeated iteratively from the second month to the last month of the study period. As a result, each drought event was defined as a series of temporally continuous drought clusters. A detailed description of this 3-D drought identification method can be found in Andreadis et al. (2005) and Lloyd-Hughes (2012). 

## _3.2.2. Definition of drought characteristics_ 

- (1) Drought duration (DD) 

Traditionally, drought duration refers to the interval extending from the initial occurrence of a drought event to its end at a specific grid cell or location. In a 3-D context, however, a drought event typically consists of multiple drought patches and their constituent grid cells, each exhibiting specific initiation and termination times. Thus, the duration of a drought event was defined as the time interval between the earliest onset and the latest termination among all associated grid cells (Liu et al., 2019). A drought event can be defined as a set _P_ consisting of multiple drought patches and the corresponding drought-affected grid cells. 

_P_ = { _g_ 1 _, g_ 2 _, …, gn_ } (4) where _gi_ denotes the _i_ th drought-affected grid cell, and _n_ represents the total number of such cells within the drought event. Each grid cell _gi_ has a drought onset time _t_<sup>_start_</sup> _i_ and termination time _t_<sup>_end_</sup> _i_ . The drought duration can then be defined as follows: _DD_ = max _i_ ) − min _i_ ) + 1 (5) 1≤ _i_ ≤ _n_<sup>(</sup><sup>_tend_</sup> 1≤ _i_ ≤ _n_<sup>(</sup><sup>_tstart_</sup> where min ( _t_<sup>_start_</sup> _i_ ) represents the earliest onset time among all grid cells, and max ( _t_<sup>_end_</sup> _i_ ) denotes the latest termination time. (2) Drought severity (DS) Drought severity (km<sup>2</sup> ⋅month) quantifies the cumulative water deficits over the entire drought duration and across the affected area. It can be calculated as follows: _Nlat Nlon Nt DSn_ = ∑ ∑ ∑ _sn_ ( _i, j, k_ ) (6) _i j k s_ ( _i, j, k_ ) = | _SDI_ ( _i, j, k_ )| × _area_ ( _i, j, k_ ) × 1 _month_ (7) where _n_ is the total number of drought events, _i_ , _j_ , and _k_ denote the longitude, latitude, and temporal coordinates of the grid cell ( _i_ , _j_ , _k_ ) within drought event _n_ , and area ( _i_ , _j_ , _k_ ) represents the area of the corresponding grid cell. (3) Drought affected area (DA) Drought affected area (km<sup>2</sup> ) is defined as the maximum projected area of the 3-D drought continuum onto the horizontal coordinate plane, reflecting the cumulative area that experienced drought conditions in any given month. It can be expressed as follows: _DA_ = _area_ (1) ∪ _…area_ ( _k_ ) ∪ _…area_ ( _DD_ ) (8) where area ( _k_ ) represents the cumulative area exposed to drought event during month _k_ . (4) Drought centroid (DC) Drought centroid ( _Xi_ , _Yj_ ) represents the spatio-temporal center of a drought patch, indicating its central location in the 3-D space of latitude, longitude, and time. It can be computed as follows: _n_ <u>∑</u> _xiWi Xi_ = _i_ =1 _n_ (9) ∑ _Wi i_ =1 

6 

_Journal of Hydrology: Regional Studies 67 (2026) 103786_ 

_Y. Du et al._ 



where _Wi_ denotes the weight coefficient of the _i_ -th grid ( _i_ = 1, 2, …, _n_ ), and _xi_ and _yi_ represent the longitude and latitude of the _i_ - th grid, respectively. 

(5) Drought migration orientation (DO) 

Drought migration orientation describes the spatial dynamic evolution of a drought event. It was determined by comparing the mean location during the first half of the event duration with that during the second half. In this study, the direction angle was defined with true north as 0<sup>◦</sup> , increasing clockwise. The full range of 0<sup>◦</sup> –360<sup>◦</sup> was divided into eight directional sectors: the four cardinal directions (N, E, S, and W) and the four intercardinal directions (NE, SE, SW, and NW). Each sector spans 45<sup>◦</sup> , corresponding to a central angle of ±22.5<sup>◦</sup> around its axis. 

## _3.3. Matching SD and VD events at a spatio-temporal scale_ 

To investigate the spatio-temporal propagation characteristics between SD and VD events, this study employed a matching approach that links related SD and VD events across temporal and spatial scales (Liu et al., 2019; Zhu et al., 2019). The matching procedure consisted of the following four steps. 

Step 1: Sorting of drought events. 

Identified SD and VD events were sorted chronologically and arranged into an _m_ × _n_ matrix, where _m_ and _n_ denote the numbers of SD and VD events, respectively. Each cell in the matrix corresponds to a paired SD and VD event to be examined. 

Step 2: Determination of temporal overlap between SD and VD events. 

Temporal overlapping was a prerequisite for matching SD and VD events. The overlap duration (Overlaptime) was determined, based on the start and end times, as well as durations of drought events. If a temporal overlap existed, the corresponding matrix cell was assigned a value of 1; otherwise, it was assigned 0. The following criterion was applied to define temporal overlap: 



where _Xmn_ is a pair of SD and VD events, _SBT_ and _SET_ are the initiation and termination times of an SD event, respectively, _VBT_ and _VET_ are the beginning and the end of a VD event, respectively, and _D_SD_ and _D_VD_ denote the durations of SD and VD events, respectively. The parameter _α_ was defined as one-third of the duration of the shorter drought event and was used as the minimum temporal overlap threshold, allowing the event-matching criterion to adaptively vary with drought duration (Liu et al., 2019). This setting avoids imposing overly strict matching requirements on short-duration events while increasing the temporal association requirement for long-duration events, thereby reducing the risk of false matches caused by incidental temporal overlap (Wang et al., 2021; Feng et al., 2024a). 

Step 3: Assessment of spatial overlap between SD and VD events. 

SD and VD event pairs marked as 1 in the matrix from Step 2 were further evaluated for spatial overlap (Overlapspace). If the overlapping area between an SD and a VD event exceeded a predefined threshold _β_ , the pair was considered successfully matched, and the corresponding matrix cell remained as 1; otherwise, it was set to 0. The spatial overlap criterion was defined as follows: 



7 

_Journal of Hydrology: Regional Studies 67 (2026) 103786_ 

_Y. Du et al.                                                                                                                                                                                                              Journal of Hydrology: Regional Studies_ 

where _AS_ and _AV_ denote the affected areas of the SD and VD events, respectively. Parameter _β_ , used to quantify the spatial overlap between SD and VD, can be defined by an absolute, relative, or combined threshold. Following Liu et al. (2019), _β_ was set to the larger of two values: 50% of _H_ (i.e., _a_ = 50%) and 15% of the smaller affected area (i.e., _b_ = 15%). 

Step 4: Classification of successfully matched SD and VD events. 

After completing the previous steps, successfully matched pairs of SD and VD events were integrated and classified. The propagation from SD to VD was categorized into four types as follows. Type 1 (T1): A single valid code per row or column implies that one SD event triggers one VD event. Type 2 (T2): Multiple valid codes in one row suggest that one SD event induces several VD events across different regions. Type 3 (T3): Multiple valid codes within the same column indicate that multiple SD events jointly induce one VD event. Type 4 (T4): Valid codes spread across multiple rows and columns indicate that multiple SD events lead to several VD events. 

## _3.4. Drought propagation characteristics_ 

## _3.4.1. Propagation time and propagation rate_ 

- (1) Propagation time (PT) 

The PT from SD to VD was calculated on a grid-by-grid basis using the Pearson correlation coefficient (PCC) method (Ding et al., 2021; Wu et al., 2021; Zhang et al., 2022b; Wang et al., 2024c). Specifically, the correlation coefficients were computed between the 1-month scale SVHI (SVHI-1) and the multi-time scale SSMI- _n_ (where _n_ = 1, 2, 3, … 12). The time-scale corresponding to the maximum correlation coefficient was then defined as the PT (Wu et al., 2021; Zhang et al., 2022a; Liu et al., 2023; Li et al., 2025a,b). In this framework, SVHI-1 was employed to capture the monthly variation in vegetation drought, whereas the multi-timescale SSMI- _n_ was used to represent SM deficits accumulated over various antecedent periods. This approach enables the identification of the specific timescale at which VD responds most strongly to antecedent SM anomalies. 

(2) Propagation rate (PR) 

For each grid cell, all SD events and VD events occurring during the study period were first identified and then spatiotemporally matched. The PR for that grid cell was defined as the proportion of VD events triggered by SD relative to the total number of SD events at that grid cell. This can be expressed as: 



where _Nv-s_ denotes the number of SD events that trigger VD, and _Ns_ represents the total number of SD events. 

## _3.4.2. Propagation direction and distance_ 

To reveal the spatial patterns of drought propagation, the average centroid positions of SD and VD events were first identified, and the propagation direction and distance between paired drought event across different categories were subsequently derived. The propagation distance ( _L_ ) was used to quantify the actual surface distance between the centroids of SD and VD events. In this study, the Haversine formula was adopted to calculate the great-circle distance between the centroids of each pair of SD and VD events, with _L_ expressed in kilometers (km) (Chen et al., 2025b; Gu et al., 2026). The calculation formulas are defined as follows (Feng et al., 2024a): 



where _V_ and _S_ denote the centroids of VD and SD events, respectively. The _lon_ and _lat_ represent the longitude and latitude of these centroid locations, respectively, and _r_ is the radius of the Earth (approximately 6371 km). _θ_ and _L_ represent the propagation angle and propagation distance, respectively. The azimuth angle _θ_ can be classified into eight directional sectors, consistent with the categorization used for drought migration orientation. 

## _3.4.3. Probability and threshold of drought propagation_ 

The copula function, which links individual marginal distributions to construct multivariate distributions with uniform values ranging from 0 to 1, is widely used to assess multivariate drought probabilities (Genest et al., 2007; Hao and Singh, 2015; Salvadori and De Michele, 2015). Based on the SD-VD propagation event pairs identified using the spatio-temporal matching criteria, this study employed a copula function to calculate the conditional probability and threshold. The main steps involved are as follows. Step 1: Selection of marginal distribution. 

8 

_Journal of Hydrology: Regional Studies 67 (2026) 103786_ 

_Y. Du et al._ 

Typical probability distributions (e.g., log-normal, Gamma, and two-parameter Weibull) were employed to fit the marginal distributions of drought duration and severity for both SD and VD. The parameters were evaluated via the maximum likelihood method (MLM). The Kolmogorov-Smirnov (K-S) test and the root mean square error (RMSE) were employed to assess the goodness-of-fit. Spearman’s rank correlation was applied to compute correlations between duration (severity) of SD events and that of VD events. Step 2: Joint distribution model. 

Joint distribution models were developed using widely used copula families, specifically the Clayton, Frank, and Gumbel families. For a pair of random variables, _X_ and _Y_ , the copula is defined as: 



where _u_ and _v_ represent the marginal cumulative distribution functions (CDF) of _X_ and _Y_ , respectively, and _C_ refers to the copula function. The copula parameters were evaluated using the MLM, and the best-fitting joint distribution function was selected, based on RMSE. 

Step 3: Conditional probability. 

The conditional probability of _Y_ ≥ _v_ given _X_ ≥ _u_ can be expressed as: 



where _x_ ( _u_ ) and _y_ ( _v_ ) indicate the cumulative probabilities for _X_ ≤ _u_ and _Y_ ≤ _v_ , respectively, and _C_ ( _x_ ( _u_ ), _y_ ( _v_ )) denotes the joint cumulative probability of _X_ ≤ _u_ and _Y_ ≤ _v_ . 

Drought levels are typically divided into four classes (i.e., mild, moderate, severe, and extreme) based on the 30th, 50th, 70th, and 90th percentiles of drought severity (duration), respectively (Jiang et al., 2024). The probabilities of VD events at different drought levels were then calculated using Eqs. (20)–(21). The SD characteristic value corresponding to a probability exceeding 95% was identified as the threshold for triggering a VD event (Guo et al., 2020). 

## _3.5. XGBoost and SHAP_ 

An integrated modeling framework combining Extreme Gradient Boosting (XGBoost) and SHapley Additive exPlanations (SHAP) was applied to quantitatively identify the key contributors of drought propagation. XGBoost is a gradient-boosting ensemble algorithm based on decision trees, which incorporates regularization terms and an iterative weighted learning strategy. This design enhances computational efficiency and effectively mitigates overfitting (Chen and Guestrin, 2016; Sun et al., 2025). This algorithm can simultaneously handle continuous predictors, missing values, and outliers, and exhibits strong capability in capturing complex nonlinear relationships and interactive effects among variables (Abel et al., 2023). Consequently, XGBoost has been widely adopted in ecological and climate-related studies and is particularly suitable for identifying key predictors with drought evolution. 

Prior to model construction, all explanatory variables were initially screened for missing and infinite values. A Pearson correlation matrix was then calculated to identify pairs of highly correlated features using a threshold of |r| _>_ 0.8. Within each group of strongly correlated variables, only the one with a higher correlation with the target variable was retained to reduce multicollinearity and enhance model stability. Subsequently, the selected predictors were standardized to eliminate scale differences that could interfere with model training. The processed dataset was randomly split into a training set (80%) and a testing set (20%) under a fixed random seed. During training, hyperparameter tuning was performed for the XGBoost regression model. The optimal parameter configuration was selected based on overall performance and used to retrain the model, which was then evaluated on the independent testing set to assess its predictive capability. Model performance was quantified using the coefficient of determination (R<sup>2</sup> ), root mean square error (RMSE), and mean absolute error (MAE). Higher R<sup>2</sup> values and lower RMSE and MAE values indicate better fit and generalization performance. 

In the model interpretation stage, the SHAP method was employed to attribute the predictions of the XGBoost model. SHAP is a model-agnostic interpretability approach grounded in cooperative game theory. It quantifies the contribution of each explanatory variable to model outputs by computing its marginal effect across different feature combinations (Lundberg and Lee, 2017; Li et al., 2024a). In this study, a positive SHAP value indicates that a given feature increases the predicted drought propagation, whereas a negative value suggests a reducing effect. Global variable importance was ranked according to the mean absolute SHAP value, enabling the identification of key contributors in the drought propagation process (Wei et al., 2024). 

In this study, 11 representative environmental factors were selected as predictors to further investigate the key contributors of drought propagation. Among them, CO₂ was included as a key indicator of global change, indirectly influencing vegetation photosynthesis and water-use efficiency, while RAD directly regulates surface energy balance, thereby affecting SM dynamics and transpiration processes. SMrz and T_veg were chosen to characterize the intensity of land-atmosphere water exchange, both of which respond directly to drought conditions. Soil texture was represented by SASI, reflecting its role in water retention capacity, and MRD indicates the potential of vegetation to access deep SM. Collectively, these factors provide a comprehensive environmental context for drought propagation and establish a robust data foundation for identifying key contributors. 

9 

_Journal of Hydrology: Regional Studies 67 (2026) 103786_ 

_Y. Du et al.                                                                                                                                                                                                              Journal of Hydrology: Regional Studies_ 

## **4. Results** 

## _4.1. Identification of SD and VD events_ 

A total of 144 SD events and 59 VD events were recognized via the 3-D detection method. Fig. 3 illustrates the temporal variations in drought duration, severity, and affected area of SD and VD events. During the period 1981–2020, approximately 95.8% of SD events persisted from 1 to 6 months, 2.8% lasted from 7 to 9 months, and only 1.4% (2 out of 144 events) exceeded 10 months. On average, SD events occurred 3.6 times per year, with a mean duration of 2.1 months, a severity of 3.45 × 10⁶ km²⋅month, and an affected area of 9.56 × 10⁵ km². Notable SD events, such as those from October 1984 to May 1985, October 2005 to August 2006, and June 2007 to April 2008, were characterized by prolonged duration, high severity, and extensive affected areas. Among these, the event from October 2005 to August 2006 lasted 11 months, recorded the highest severity (23.46 × 10⁶ km²⋅month) and the largest affected area (22.61 × 10⁵ km²). In contrast, VD events were generally shorter in duration and less frequent, with 91.5% lasting 1–3 months. The average annual occurrence was 1.5, with a mean duration of 1.80 months, severity of 2.57 × 10⁶ km²⋅month, and affected area of 9.51 × 10⁵ km². Relatively severe VD events occurred from September 1989 to February 1990, June to December 1995, and June to December 2007. The event from June to December 2007 persisted for 7 months, with a mean severity of 9.51 × 10⁶ km²⋅month and affected area of 12.25 × 10⁵ km². Temporal variation analysis revealed an overall lag effect between SD and VD events. According to the Bulletin of Flood and Drought Disaster in China, during the summer and autumn of 2006, China experienced its most severe regional drought event since 1951. The drought affected over 20 provinces (autonomous regions and municipalities) across the country, with particularly severe impacts in Sichuan, Chongqing, Guizhou, Hubei, and Hunan. Precipitation in these areas was 50–90% below the historical average for the same period, resulting in a rapid decline in SM and subsequent severe damage to vegetation. Nationwide, approximately 20 million ha of crops were affected. 

Fig. 4 presents the spatial distributions of the average duration and severity of SD and VD. Results indicated generally consistent spatial patterns in both duration and severity between SD and VD. Areas with longer and more severe SD generally exhibited longer VD duration and greater severity. At the regional level, longer duration and greater severity of SD were observed in regions IV, V, and VI, and the western parts of region IX. In the southeastern areas of China, drought severity generally ranged between 2 × 10² km²⋅month and 3 × 10² km²⋅month. For VD, longer duration (2–4 months) was identified in northwestern China, primarily covering regions VIII and IX. Regions IV, V, and VI exhibited higher VD severity, which aligned spatially with the pattern of SD severity, though the values were generally lower than those of SD. Higher drought severity was mainly concentrated in the southeastern, North China, and Loess Plateau regions. Previous studies have reported two nationwide centers of high drought intensity, located in the Huanghuai region (e. g., central Henan and northern Anhui), the Jianghuai region (e.g., central Anhui and Jiangsu), and most of the Jianghan region (i.e., Hubei), as well as in southern South China, Yunnan, southeastern Sichuan, and western Guizhou (Gao et al., 2023). These areas correspond to regions IV, V, and VI of the present study. Moreover, to further validate the results derived from ERA5-Land SM data, comparative analyses based on multiple SM datasets (GLDAS Noah, GLEAM, and SiTHv2) and RZSM showed that the derived SD 



**Fig. 3.** Temporal variations in the duration-severity and duration-affected area relationships for SD and VD events. In each column, the width and color represent drought duration, while the height denotes severity or affected area. 

10 

_Journal of Hydrology: Regional Studies 67 (2026) 103786_ 

_Y. Du et al._ 



**Fig. 4.** Spatial distributions of duration and severity for SD and VD events. Boxplots summarize statistical features of duration and severity across the nine eco-geographical regions of China. 



**Fig. 5.** Severity (10<sup>6</sup> km<sup>2</sup> ⋅month), affected area (10<sup>5</sup> km<sup>2</sup> ), and event count for SD and VD events across migration orientations. 

11 

_Journal of Hydrology: Regional Studies 67 (2026) 103786_ 

characteristics exhibited generally consistent spatial patterns with those obtained from ERA5-Land 0–7 cm surface SM (Supplementary Figs. 1–4). 

## _4.2. Migration patterns of SD and VD events_ 

Fig. 5 displays the migration characteristics of severity, affected area, and duration for SD and VD events across different orientations. Between 1981 and 2020, 25 SD events in China migrated westward (i.e., NW, W, and SW). Among these, the westwardmigrating SD event from October 2005 to August 2006 recorded the highest severity (23.46 × 10<sup>6</sup> km²⋅month). Compared to other orientations, westward-migrating SD events exhibited the highest frequency (14 events), along with longer average duration (4.43 months), higher severity (7.84 × 10<sup>6</sup> km²⋅month), and larger affected area (13.50 × 10<sup>5</sup> km²). This indicated that SD events migrating westward in China were generally more severe, extensive, and prolonged than those migrating in other directions. 

For VD events during 1981–2020, the highest migration frequency was toward the southeast, with events lasting 2–3 months. However, VD events migrating westward (NW, W, and SW) showed longer average duration (4.17 months), higher severity (7.76 × 10<sup>6</sup> km²⋅month), and larger affected area (16.48 × 10<sup>5</sup> km²) compared to other orientations, which was consistent with the migration patterns of SD events. The southwestward-migrating VD event from June to December 1995 exhibited the maximum duration, severity, and affected area among all VD events. 

## _4.3. Matching characteristics of drought event pairs_ 

Fig. 6 presents the spatial distributions of average duration and severity for spatio-temporally matched SD and VD events. As an initial signal of drought propagation, SD exhibited pronounced regional patterns in both its duration (Fig. 6a) and severity (Fig. 6c). In high-value regions (I and II), SD lasted 3–6 months on average, with severity ranging from 0.5 × 10 ³ km²⋅month to 2 × 10 ³ km²⋅month. In contrast, the matched SD events in low-value regions (V, VI, and IX) were of shorter duration and mild severity. For matched propagation events, longer duration and greater severity of VD events were found in the western region of China and region V. 



**Fig. 6.** Spatial distributions of duration and severity for matched SD and VD events. Boxplots show statistical features of duration and severity across the nine eco-geographical regions of China. 

12 

_Journal of Hydrology: Regional Studies 67 (2026) 103786_ 

_Y. Du et al.                                                                                                                                                                                                              Journal of Hydrology: Regional Studies_ 

Fig. S5 shows the spatial distributions of the mean duration and severity of SD and VD events that did not establish spatio-temporal matching relationships. The mean duration of SD events was mainly concentrated between 1 and 3 months, with relatively high values observed only in localized areas of regions I, II, and IX. Their severity was generally low, mostly below 0.4 × 10 ³ km²⋅month, although localized high values occurred in region IX. For unmatched VD events, the duration was approximately 1–2 months, and the severity was mostly below 0.3 × 10 ³ km²⋅month, with relatively high values observed only in the transition zone from northwestern to northern areas. 

Compared with successfully matched SD-VD events, the unmatched events showed substantially weaker persistence and cumulative impacts. Successfully matched events usually represented typical propagation processes from SD to VD, with longer durations, higher severity, and stronger spatial continuity. In contrast, unmatched events were commonly characterized by short-term, low-intensity, and localized features. 

## _4.4. Drought propagation characteristics in China_ 

## _4.4.1. Temporal dimension_ 

Fig. 7 displays the spatial distributions of PT and PR from SD to VD across China. The PT exhibited a distinct spatial pattern, generally longer in the western and northern regions and shorter in the eastern and southern regions, highlighting obvious spatial heterogeneity among nine regions of China (Fig. 7a). Specifically, regions VII, VIII, and IX displayed longer PT, with average values of 3.95, 4.0, and 4.53 months, respectively, suggesting a substantial lag of VD behind SD in these areas. In contrast, regions II and IV showed shorter PT, averaging 2.99 and 2.68 months, indicating greater sensitivity of VD to SD. The boxplots in Fig. 7a further illustrate the statistical characteristics of PT within each region. For instance, region I had a median PT of 4 months with a relatively concentrated distribution, whereas region VII, despite an average PT of 3.95 months, exhibited strong internal variability, with the maximum value exceeding 8 months. 

Similarly, Fig. 7b exhibits considerable spatial heterogeneity in the distribution of PR from SD to VD. High PR values were mainly distributed in regions I, II, and VII, while low values were found in regions IV, V, and VI. A noticeable PR gradient was observed across region III. Boxplots in Fig. 7b visually demonstrate the pronounced differences in PR among the nine regions. Region I displayed the highest median PR, reflecting the strongest sensitivity of VD to SD in this area. In comparison, region V exhibited a lower median PR, suggesting a weaker propagation process from SD to VD. 

Integration of the results from Fig. 7 and Fig. 1a revealed notable differences in PT and PR across vegetation types. The average response time of forests located in humid regions I, V, and VI was 3.48 months, whereas croplands had the shortest response time (3.03 months), partly because irrigation and other human interventions mitigate soil moisture deficits and thus accelerate vegetation response to drought (Tian et al., 2025). Within region II, local forests had a longer response time (3.56 months) than had grasslands (3.13 months). Moreover, forests in regions I (3.63 months) and II (3.56 months) demonstrated longer response times than those in regions V (3.35 months) and VI (3.46 months). 

Furthermore, the highest average PR (0.48) was observed in forests of region I, locally reaching 0.6–0.8, indicating that nearly half of the SD events triggered VD on average. In contrast, forests in humid southern regions had lower PR values (0.2–0.3), suggesting a buffering effect of SM on drought propagation. In regions VII and VIII, grasslands showed an average PR of 0.26. Croplands generally showed a moderate PR (0.20); however, those in the more northern regions II (0.29) and III (0.23) had higher PR than those in the southern regions IV (0.11) and V (0.08). In region VIII, barren lands recorded a slightly higher average PR (0.28) than grasslands (0.27), while in region II, forests (0.31) showed a marginally higher PR than croplands (0.29). 

Table 2 summarizes the statistical characteristics of PT from SD to VD across China and its nine eco-geographical regions. At the national scale, the mean PT was 3.76 months, ranging from 1 to 11 months, with a standard deviation (Std.) of 1.87 months. Previous national-scale studies have also reported significant regional differences in PT among different drought types in China. For example, 



**Fig. 7.** Spatial distributions of PT and PR from SD to VD. Boxplots summarize statistical characteristics across the nine eco-geographical regions of China, while pie charts display the national-scale proportions of each PT and PR category. 

13 

_Y. Du et al.                                                                                                                                                                                                              Journal of Hydrology: Regional Studies 67 (2026) 103786_ 

**Table 2** 

Statistical characteristics of PT from SD to VD for China and its nine eco-geographical regions. 

|Region|Mean (month)|Min (month)|Max (month)|Std. (month)|
|---|---|---|---|---|
|I|3.61|1|8|0.91|
|II|2.99|1|9|1.46|
|III|3.34|1|10|1.67|
|IV|2.68|1|9|1.38|
|V|3.16|1|10|1.54|
|VI|3.48|1|10|1.50|
|VII|3.95|1|11|2.10|
|VIII|4.00|1|11|1.72|
|IX|4.53|1|11|2.08|
|China|3.76|1|11|1.87|



Geng et al. (2024) found that the PT from meteorological drought to agricultural drought was mainly concentrated within 1–10 months, with a national average of approximately 4.1 months, which is close to the mean PT of 3.76 months obtained in this study. 

Across the nine eco-geographical regions, PT from SD to VD showed clear spatial heterogeneity. Region IX had the longest mean PT (4.53 months), followed by regions VIII (4 months) and VII (3.95 months). In contrast, region IV had the shortest PT (only 2.68 months), while regions II and V also showed relatively short mean PT of 2.99 and 3.16 months, respectively. Overall, PT in arid, semiarid, and alpine regions was generally longer than that in humid and semi-humid regions. 

Previous studies have shown that vegetation responses to drought on the Qinghai-Tibet Plateau exhibit clear time-lag effects. Wei et al. (2023) reported an optimal lag time of approximately 3–6 months for VD responses on the Qinghai-Tibet Plateau, which is generally consistent with the mean PT of 4.53 months in region IX. Feng et al. (2024b) also found that the mean PT in Northwest China was approximately 6 months, with longer PT in plateau climate zones. Therefore, the longer PT observed in regions VII, VIII, and IX further indicate stronger lagged soil-vegetation water linkages under high-elevation, arid, and semi-arid conditions. In contrast, PT in humid and semi-humid regions were generally shorter, suggesting faster vegetation responses to SM anomalies where water availability is higher and SM recharge is more rapid (Geng et al., 2024). The shorter PT observed in regions IV, II, and V are consistent with rapid SM recharge and tighter soil-vegetation response linkages in humid and semi-humid regions. 



**Fig. 8.** Spatial distribution of the percentage of paired SD-VD events for different categories. Radar plots illustrate propagation direction and distance. 

14 

_Journal of Hydrology: Regional Studies 67 (2026) 103786_ 

_Y. Du et al.                                                                                                                                                                                                              Journal of Hydrology: Regional Studies_ 

## _4.4.2. Spatial dimension_ 

Fig. 8 illustrates the spatial distribution of the percentage of paired SD-VD events for different categories. Type 1 was mainly distributed in regions II, III, V, and VIII. Approximately 67% of type 1 events propagated laterally, with only two pairs moving northeast. The mean propagation distance was 1027 km, reaching a maximum of 2673 km. In the northeastern forest zones located in regions I and II, the average frequencies were 3.45% and 3.61%, respectively. By contrast, the humid southern forest areas situated in regions V and VI showed lower average frequencies of 3.02% and 2.97%, respectively, suggesting a distinct latitudinal gradient. In terms of croplands, the average frequency was 3.17%, with higher values observed in northern areas and lower values in southern areas. The highest frequency of 5.88% occurred in the barren areas of Northwest China, implying that under sparse vegetation, a single SD event was more likely to trigger a subsequent VD event. 

Type 2 was concentrated in the central and northeastern parts of China, showing a distribution pattern similar to type 1. A distinct spatial gradient was observed, with frequencies decreasing from west to east and north to south. Most events (85.71%) propagated northward, with a mean distance of 413 km and a maximum of 677 km, which was markedly shorter than type 1, reflecting more limited spatial influence. In terms of vegetation, frequencies averaged 4.63% in the northeastern croplands, ranged between 1.93% and 7.69% in southeastern coastal forests, and were relatively low in barren areas. 

Type 3 occurred across almost the entire study area, with high-frequency zones in region III, southwestern part of region VII, and eastern part of region VIII, where its occurrence was generally higher than that of other types. Most paired drought events moved laterally. The mean propagation distance was 1158 km, with a maximum of 2581 km. Notable differences in vegetation response were observed across land cover types. For example, the average frequency was 7.36% in forests and 7.92% in grasslands, but reached its highest levels in northern croplands ( _>_ 9%), with a peak of 10.16% recorded in region III. This indicates that croplands were more susceptible to this event type. 

Type 4 was distributed in regions I and II, as well as the southwestern part of region VII. In the junction area of Shaanxi, Gansu, and Qinghai Provinces, the frequency exceeded 9%, indicating localized clustering. About 75% of type 4 events propagated westward, with a mean distance of 774 km and a maximum of 1545 km. Regarding vegetation, frequencies were relatively high in northeastern forests and central grasslands, generally exceeding 6%. 

## _4.4.3. Probability and threshold of drought propagation_ 

Prior to estimating the conditional probabilities and propagation thresholds, the fitting performance of the marginal distributions of SD and VD characteristics, as well as their joint distribution models, was first evaluated. Based on the matched SD-VD event pairs, the Gamma, lognormal, and two-parameter Weibull distributions were applied to fit the duration and severity series of SD and VD, respectively. The K-S test and RMSE were then used to select the best-fitting marginal distribution functions. Due to space constraints, Fig. S6 presents the goodness-of-fit results of the marginal distributions at the national scale. Subsequently, three commonly used copula functions (i.e., Clayton, Frank, and Gumbel) were adopted to fit the bivariate probability distributions. As shown in Fig. S7, the Gumbel copula showed the best fitting performance at the national scale and was therefore selected to construct the joint distribution model of SD-VD characteristics for China as a whole. Fig. 9 presents the conditional probability that a given SD level (in terms of duration and severity) triggers different levels of VD across nine regions of China. Overall, as the SD level intensified, the conditional probability of triggering more severe VD increased significantly, demonstrating a strong hierarchical response relationship. 

As shown in Fig. 9a, under the given mild VD conditions, all nine regions exhibited relatively high probabilities. Regarding moderate drought, the conditional probability of moderate VD triggered by moderate SD was higher in regions IV (0.95) and IX (0.99), while region V showed a lower probability (0.69). For severe drought, the conditional probability of severe VD resulting from severe SD was the lowest in region VII (0.54), with the remaining regions exceeding 0.60. Notably, region I demonstrated a higher probability of triggering extreme VD under extreme SD conditions (0.83), whereas other regions had relatively low probabilities of extreme VD. 



**Fig. 9.** Conditional probabilities of different levels of VD triggered by varying SD conditions across the nine eco-geographical regions of China. For instance, SD1_VD1 denotes the conditional probability of mild SD triggering mild VD. The numeric suffixes 1, 2, 3, and 4 in both SD and VD labels correspond to mild, moderate, severe, and extreme drought, respectively. 

15 

_Journal of Hydrology: Regional Studies 67 (2026) 103786_ 

_Y. Du et al.                                                                                                                                                                                                              Journal of Hydrology: Regional Studies_ 

Furthermore, with longer SD duration, regions I, VIII, and IX were associated with a higher risk of elevated-level VD. 

In terms of severity (Fig. 9b), relatively higher risks of mild VD were observed in regions II, IV, and V, with the highest conditional probability for inducing mild VD found in region V (0.95). In contrast, the probabilities of severe and extreme VD were low in regions I, V, and IX. Specifically, region I exhibited the lowest conditional probability (0.27) for severe VD developing from severe SD, while region V had the lowest probability (0.04) for extreme VD. A comparison of propagation probabilities under different drought conditions revealed that regions II, V, and VI were more prone to VD. 

Fig. 10 presents the drought duration and severity thresholds at which SD triggered different levels of VD. With respect to duration (Fig. 10a), most regions were concentrated within 1–6 months, such as region III where the thresholds of SD_VD1, SD_VD2, and SD_VD3 were 1.46, 2.68, and 5.49 months, respectively. For region V, the SD_VD2 threshold reached 11.98 months, far exceeding other regions, indicating that moderate VD requires more prolonged SD stress. Similarly, in region IV, the SD_VD3 threshold reached 10.88 months, which was substantially higher than its lower-level thresholds, reflecting a pronounced difference in response across drought levels. 

In terms of severity (Fig. 10b), thresholds generally increased with drought level. In region VIII, the SD_VD4 value reached 21.28 × 10⁶ km²⋅month, the highest among all regions, while the SD_VD1 value was 5.28 × 10⁶ km²⋅month. Moreover, SD severity thresholds in region VIII for various VD levels were generally higher than those in other regions, indicating that more severe SD conditions were required to trigger VD, and that vegetation in this area exhibited stronger resistance to drought disturbance. In region IV, the SD_VD4 threshold (10.47 × 10⁶ km²⋅month) was far greater than that of SD_VD1 (0.59 × 10⁶ km²⋅month), showing a clear escalation threshold. In contrast, thresholds in regions I, II, and VII were generally lower, indicating more sensitive vegetation responses. In particular, thresholds for VD1 to VD3 in region I ranged only from 0.12 × 10⁶ km²⋅month to 2.14 × 10⁶ km²⋅month, suggesting weaker ecological resistance to drought disturbance. 

## _4.5. Key contributors to drought propagation time in China_ 

Fig. 11 presents the SHAP-based importance of environmental contributors to PT from SD to VD across the nine eco-geographical regions of China. The results indicated that PT was associated with multiple climatic and environmental factors, with their relative importance varying markedly among regions. 

SunD was an important contributor to PT in regions I, III, V, and IX, suggesting that solar radiation conditions were closely associated with PT. Region I, characterized by a cold-temperate humid climate with limited thermal conditions and a short growing season, showed that PT was primarily associated with SunD, PRE, and CO2. Longer SunD generally corresponded to negative SHAP values, indicating an association between increased SunD and shorter PT. This pattern may reflect the role of enhanced solar radiation in promoting vegetation photosynthesis and transpiration, which could increase vegetation sensitivity to SM deficits (Ma and Yuan, 2024; Wu et al., 2024). Conversely, higher PRE was mainly associated with positive SHAP values, suggesting that increased precipitation may replenish SM and enhance its buffering capacity against PT (Teutschbein et al., 2025). Elevated CO2 concentrations were predominantly linked with negative SHAP values, possibly because enhanced photosynthesis and biomass accumulation accelerate the transmission of SM deficits to vegetation, thereby shortening PT (Ainsworth and Long, 2005; Norby et al., 2005). 

In region III, which has a warm-temperate humid to semi-humid climate, SunD, PRE, and CO2 were important contributors to PT, indicating that PT was closely associated with energy input and water supply. Longer SunD was associated with shorter PT, potentially because enhanced radiation increased transpiration demand and SM depletion, allowing vegetation to respond more rapidly to SM deficits. The effect of PRE on PT showed nonlinearity, reflecting the complex interplay between precipitation replenishment and evapotranspiration demand. Region V, situated in the mid-subtropical humid zone, benefits from favorable hydrothermal conditions, relatively abundant PRE, and dense vegetation cover. SunD showed the highest model contribution, while CO2, TMP, and NDVI also contributed substantially. This suggests that, under sufficiently moist conditions, PT may be more strongly associated with energy availability and vegetation physiological status than with direct moisture limitation (Qin et al., 2023; Ren et al., 2023). Region IX, 



**Fig. 10.** Propagation thresholds for triggering different VD levels under various SD conditions across the nine eco-geographical regions of China. The gray blocks indicate no propagation from SD to the corresponding VD level at the 95% probability. 

16 

_Journal of Hydrology: Regional Studies 67 (2026) 103786_ 



**Fig. 11.** Key contributors to PT across the nine eco-geographical regions of China. 

located in the alpine Qinghai-Tibet Plateau, is characterized by high elevation, thin air, strong solar radiation, and limited thermal conditions (Yang et al., 2010; Kuang and Jiao, 2016; Gelsor et al., 2018). This region is also affected by freeze-thaw processes, snowmelt, and active-layer SM dynamics (Wang et al., 2015; Qin et al., 2017; Fu et al., 2022). SHAP results identified SunD, PRE, and RAD as important contributors to PT, consistent with the high sensitivity of alpine ecosystems to radiation, precipitation, and freeze-thaw hydrological processes (Li et al., 2024b). 

TMP was an important predictor of PT in regions II, IV, VI, and VII, although its association with PT and the underlying mechanisms appeared to vary across climate zones. In region II, PT prediction was substantially associated with TMP, PRE, and DEM. Thermal conditions can influence the growing season, soil thawing, and evapotranspiration intensity, whereas PRE may buffer PT by replenishing SM storage (Seneviratne et al., 2010; Zhang et al., 2020; Li et al., 2024b). Region IV lies in the transition zone between the Qinling-Daba Mountains and the Jianghan Plain, where mountains, hills, plains, and valleys form a highly heterogeneous landscape. TMP was closely associated with DEM and CO2 (Lan et al., 2022; Yao and Cui, 2022) and showed a high contribution to PT prediction, followed by NDVI, SMrz, and PRE. SHAP results showed that higher TMP values were generally associated with negative SHAP values in the relatively humid regions II and IV, indicating an association with shorter PT. This pattern may reflect enhanced transpiration and soil-vegetation water exchange under warmer conditions, which accelerates SM consumption and may facilitate the transition from SM deficits to vegetation water stress (Seneviratne et al., 2010; Zhang et al., 2020; Li et al., 2023). Region VI, characterized by a low-latitude hot and humid climate, was mainly associated with CO2, TMP, and SunD, whereas PRE had a lower relative importance. Under abundant precipitation and concurrent warm-wet conditions, SM may not be a long-term limiting factor, and PT may therefore be more closely associated with energy supply than with moisture availability (Yang et al., 2016). The high importance of CO2 in this region may reflect vegetation sensitivity to CO2 fertilization effects, stomatal regulation, and associated changes in water-use efficiency (Ainsworth and Long, 2005; Ainsworth and Rogers, 2007; McDermid et al., 2021). 

17 

_Journal of Hydrology: Regional Studies 67 (2026) 103786_ 

_Y. Du et al.                                                                                                                                                                                                              Journal of Hydrology: Regional Studies_ 

In contrast, the association between TMP and PT in region VII differed markedly from that in humid regions. Higher TMP values corresponded to positive SHAP values, indicating an association with longer PT. In humid regions with sufficient water availability, higher TMP may enhance vegetation transpiration and promote energy-water exchange, thereby accelerating the propagation from SD to VD and shortening PT (Li et al., 2023, 2025c; You et al., 2025). By contrast, vegetation in chronically water-limited drylands often adopts drought-adaptation strategies, such as reduced transpiration and improved water-use efficiency, which may decrease vegetation sensitivity to short-term SM fluctuations (Mohanta et al., 2024; Yao et al., 2025). Thus, although higher TMP may increase vegetation metabolic demand, conservative water-use and drought-tolerance strategies could delay vegetation responses to SM deficits, resulting in longer PT (Li et al., 2023; You et al., 2025). Region VIII is a typical arid region, where PRE contributed most to PT prediction, followed by CO2 and RAD. Higher PRE values were associated with positive SHAP values, indicating that increased PRE was related to longer PT. The scarcity and intermittency of PRE in arid regions govern SM recharge and may fundamentally constrain the rate at which vegetation responds to drought stress (Zhu et al., 2015). 

Overall, vegetation in tropical and subtropical humid regions receives abundant PRE and benefits from favorable hydrothermal conditions, making it less sensitive to variations in PRE. Consequently, drought propagation in these regions may be more closely associated with SunD, TMP, and CO2 (Hilker et al., 2014; Wang et al., 2022). In contrast, vegetation growth in arid regions of China is highly dependent on water availability (Sun et al., 2015; Zhao et al., 2023b; Liu et al., 2025), whereas semi-arid regions may be more sensitive to changes in TMP and SMrz (Bai et al., 2022; Jiang et al., 2022a; Wang et al., 2024b; Lan et al., 2025). 

## **5. Discussion** 

## _5.1. Advantages of the proposed method_ 

A strong driver-response relationship existed between SD and VD with respect to their occurrence and developmental mechanisms. Therefore, an in-depth investigation of the propagation process from SD to VD is crucial for accurately evaluating the ecological impacts of drought and improving prediction reliability (Zhu et al., 2019). The 3-D spatio-temporal clustering method applied in this study offered significant advantages in characterizing and analyzing this propagation process. 

First, compared with traditional one-dimensional or two-dimensional drought identification approaches, the 3-D spatio-temporal clustering algorithm provided a more comprehensive characterization of the dynamic evolution of drought events (Liu et al., 2019, 2021; Feng et al., 2021, 2024a; Jiang et al., 2022b). This method not only captured fundamental attributes, such as drought duration and severity, but also accurately extracted key spatio-temporal features, including the affected area and spatial dynamics patterns (Figs. 3–5). This capability enabled a deeper exploration of drought expansion, contraction, and migration. By retaining the information provided by conventional methods, while extending their analytical scope, the 3-D clustering approach significantly advanced our understanding of the spatio-temporal nature of drought events. 

Second, this study employed a spatio-temporal matching algorithm to accurately pair independently identified SD and VD events, thereby enabling effective extraction of drought propagation processes with strong spatio-temporal linkages (Xu et al., 2015; Jiang et al., 2022b). More importantly, both the matching procedure and its results provided spatial explanatory power for understanding the underlying propagation mechanisms (Fig. 6). The successfully matched drought event pairs visually captured the spatial correlations (i.e., propagation distance and direction) and occurrence frequencies (Fig. 8). These metrics provide indirect evidence of regional differences in vegetation sensitivity to SM deficits: higher matching frequencies and shorter propagation distances generally indicate greater sensitivity, reflecting more efficient drought signal transmission under comparable environmental conditions. 

Finally, building on the successfully matched drought event pairs, this study conducted a systematic quantitative analysis of the propagation process across both temporal and spatial dimensions. Temporally, PT and PR were quantified (Fig. 7); spatially, propagation direction and distance were measured (Fig. 8). Furthermore, by estimating propagation probability and threshold, triggering conditions of drought propagation were identified (Figs. 9–10). This integrated, multi-indicator analysis of spatio-temporal propagation constituted a core methodological strength of the study. It not only addressed the limitations of previous research that focused predominantly on single time lags or statistical correlations (Liu et al., 2019; Feng et al., 2024a), but also established a comprehensive framework for understanding drought propagation dynamics. 

## _5.2. Robustness of ERA5-Land SM data for drought characterization_ 

This study primarily identified SD characteristics based on 0–7 cm surface SM from ERA5-Land, aiming to characterize the spatiotemporal variation in soil water deficits. Given that the selection of SM datasets and soil layer depths may affect the identification of SD, we further conducted a series of robustness tests. Specifically, SD characteristics were derived from multiple alternative SM datasets, including GLDAS Noah, GLEAM, and SiTHv2, as well as RZSM of ERA5-Land. The resulting SD metrics were then compared with those obtained from the ERA5-Land surface SM product. 

The SD characteristics estimated from the multiple SM datasets exhibited strong spatial consistency, particularly in terms of drought duration and severity (Figs. S1–S3). Overall, the derived SD duration across datasets fell predominantly within the range of approximately 1.4–2.5 months. Specifically, the GLDAS Noah data showed that longer durations mainly occurred in southeastern China and localized areas of region IX. The GLEAM results similarly pointed to southeastern China as a region of prolonged drought. The SiTHv2 outputs revealed that extended durations were mainly concentrated in regions IX, V, and the transition zone between North China and Northwest China. Regarding SD severity, the multiple SM datasets exhibited broadly similar spatial distributions, with higher severity in southeastern China and lower severity in northern China. Areas of high severity were mainly concentrated in 

18 

_Journal of Hydrology: Regional Studies 67 (2026) 103786_ 

_Y. Du et al.                                                                                                                                                                                                              Journal of Hydrology: Regional Studies_ 

regions IV, V, and VI, whereas low-severity areas were primarily distributed in regions I, II, VII, and VIII, suggesting relatively weak cumulative drought effects in these latter regions. Collectively, the SD patterns derived from the GLDAS Noah, GLEAM, and SiTHv2 were generally consistent with those from ERA5-Land, thereby confirming the reliability and robustness of the ERA5-Land-based SD estimates. 

To further investigate the potential influence of soil layer depth on SD identification, root-zone SD characteristics were calculated using RZSM data (Fig. S4). The results showed that the drought duration and severity derived from RZSM exhibited spatial patterns similar to those obtained from surface SM (0–7 cm). Regions with longer root-zone SD duration were predominantly located in western China, especially the Tibetan Plateau and its surrounding areas. Meanwhile, areas with higher drought severity were mainly concentrated in regions IV, V, and VI and their adjacent areas, which are generally consistent with the high-severity areas identified from surface SD. These findings further indicated that ERA5-Land 0–7 cm surface SM can effectively capture the primary spatial differentiation characteristics of SD, supporting the rationality for using surface SM in SD identification and subsequent analyses in this study. 

It should be noted, however, that surface SM responds rapidly to precipitation inputs and evapotranspiration losses, thereby enabling it to effectively capture the onset of SD and its triggering effects on VD. Nevertheless, surface SM may not fully represent the buffering and lagged responses of deeper root-zone SM dynamics. Therefore, the present study mainly revealed the propagation characteristics from surface SD to VD, whereas the role of deeper root-zone SM in modulating this propagation process may not have been fully accounted for. Future research should integrate multilayer SM datasets to provide a more comprehensive understanding of the propagation from SD to VD. 

## _5.3. Selection of the minimum area threshold_ 

_H_ is a key parameter for identifying three-dimensional regional drought events. This study investigated the influence of this threshold on the identification results for both SD and VD events. As illustrated in Fig. 12, the number of extracted SD and VD events, along with the proportion of minor drought events, varied considerably under different thresholds (Feng et al., 2024a). With the area threshold set at 4.0% of the total study area, 207 SD events and 94 VD events were identified, of which minor events accounted for 67.15% and 60.64%, respectively. As the threshold increased, both the total number of identified drought events and the proportion of minor events decreased significantly. However, once the threshold exceeded 5.6%, the declining trend slowed noticeably and eventually stabilized, indicating that spatially scattered or short-duration localized minor drought events have been effectively filtered out (Jiang et al., 2022b; Feng et al., 2024a). 

In our analysis, setting _H_ to 5.8% allowed for the identification of major drought episodes, such as the severe drought in 2006 and the spring drought in 2008—each captured as a single, persistent multi-dimensional event. If _H_ is set too low (e.g., 4.0%), large-scale drought events may be fragmented into multiple sub-events, while introducing substantial spatially dispersed short-term noise, which can obscure the analysis of drought processes (Wen et al., 2020). Considering both the statistical behavior and the accurate identification of historical events, this study selected 5.8% of the total study area as _H_ . This choice ensured robust event identification and aligned with established methodological practices in the field (Li et al., 2020; Feng et al., 2021; Wang et al., 2023; Zhang et al., 2023). 

## _5.4. Uncertainties, limitations, and prospects_ 

This study considered several sources of uncertainty. First, the inherent uncertainties associated with VHI remote sensing products, combined with the differing spatial resolutions of the SM and the VHI datasets, introduced additional uncertainty during data resampling. Second, the determination of drought thresholds involved a degree of arbitrariness. Here, moderate to extreme drought events were identified using a threshold of − 1 for both the SSMI and SVHI, while mild droughts were excluded. Although this threshold setting aligns with previous studies (Liu et al., 2019; Feng et al., 2024a; Wang et al., 2024a), it omits numerous mild SD events that nonetheless affect vegetation ecosystems, especially in transitional or semi-arid regions. Therefore, this threshold may underestimate drought frequency and spatial continuity, reduce event samples for propagation analysis, and introduce uncertainty into drought assessment. Third, the application of the 3-D clustering method for identification and spatio-temporal matching of drought events relies on specific conditional constraint parameters (e.g., _H_ ). The choice of such thresholds often depends on the extent of the study area and the characteristics of the input data. Although the threshold selection procedure followed the established method (Liu et al., 2019; Feng et al., 2024a), the inherent uncertainty associated with thresholds was not fully eliminated (Fig. 12). Meanwhile, the strict spatio-temporal matching criteria limited the number of SD-VD matched pairs, potentially affecting the robustness of drought propagation statistics. Finally, uncertainty may also arise from the selection of copula functions (Guo et al., 2019; Wang et al., 2020). In this study, three widely used copulas (i.e., Clayton, Frank, and Gumbel) were chosen as candidates due to their common application in drought frequency analysis (Ayantobo et al., 2019; Chen et al., 2024; Jin et al., 2024). Nevertheless, we cannot exclude the possibility that other copula functions not considered here might better describe the dependence structure between drought variables. 

Although this study effectively identified SD and VD events using a 3-D spatio-temporal clustering method and analyzed their propagation characteristics, several limitations remain. First, this study primarily identified SD characteristics based on ERA5-Land 0–7 cm surface SM, with a focus on characterizing near-surface soil water deficits and their relationship with VD. Although the comparison results based on multiple SM datasets and RZSM indicate that the spatial patterns of SD derived in this study are relatively robust, surface SM still cannot fully represent deep soil water recharge, root-zone water storage, and vegetation water uptake from deeper soil layers (Fan et al., 2017; Zhang et al., 2019a; Meng and Sun, 2023). Therefore, future studies could further integrate information on multilayer SM, rooting depth, and land cover types to develop a comprehensive SD index that better reflects differences in 

19 

_Journal of Hydrology: Regional Studies 67 (2026) 103786_ 



**Fig. 12.** Rationality test of the minimum area threshold for identifying SD and VD events. 

vegetation root-zone water use (Wu et al., 2015; Mao et al., 2016). Second, while VHI served as the primary VD indicator in this study, its sensitivity to vegetation water status is limited. Subsequent research could incorporate remote sensing indices that directly reflect vegetation moisture conditions, such as solar-induced chlorophyll fluorescence (SIF) and the Land Surface Water Index (LSWI), and compare them with VHI to achieve more thorough and timely characterization of VD (Miao et al., 2018; Zhang et al., 2019b). Third, the analysis focused mainly on the spatio-temporal propagation between SD and VD, without delving deeply into the underlying biophysical and physiological mechanisms. For instance, how SD affects plant water uptake and stomatal conductance, ultimately leading to vegetation stress (Anderegg et al., 2012; Haghpanah et al., 2024), was not systematically examined using eco-physiological models (Müllers et al., 2022; Shao et al., 2023). Future studies could combine statistical approaches with process-based models to simulate water, energy, and carbon fluxes within the soil-vegetation continuum, thereby clarifying key controls on drought propagation (Fatichi et al., 2016; Novick et al., 2016). Notably, a bidirectional feedback exists between SD and VD: SD induces vegetation water stress, while vegetation affects SM recovery via transpiration and root water uptake (Seneviratne et al., 2010; Fatichi et al., 2016; Bassiouni et al., 2020). This study only focused on the one-way propagation from SD to VD, without quantifying the reverse effect of vegetation on SM. Future studies should further elucidate the bidirectional feedback mechanism by incorporating vegetation physiological processes (Fatichi et al., 2016; Zhou et al., 2025). Finally, this study did not account for the effects of human activities on vegetation status. In agricultural regions, interventions such as irrigation, tillage, and land-use changes can substantially alter vegetation growth and, in some cases, outweigh natural climatic drivers, increasing the nonlinearity and complexity of drought propagation (Pielke et al., 2011; Kumar et al., 2016; Lu et al., 2020). Therefore, future efforts should develop more integrated drought propagation models that systematically assess the interactions between climate variability and human activities, ultimately enhancing the explanatory and predictive capability for extreme drought events. 

## **6. Conclusions** 

This study systematically investigated the spatio-temporal propagation from SD to VD across China from 1981 to 2020. By applying a three-dimensional (3-D) clustering framework and a novel spatio-temporal matching algorithm, we identified and paired SD and VD events, and quantitatively analyzed their propagation characteristics and explored their statistical associations with environmental factors. The main conclusions are summarized as follows: 

The results revealed that the average propagation time from SD to VD was 3.76 months, exhibiting a distinct west-to-east gradient, with longer lags in the arid northwestern regions and shorter times in the humid southeast. Among the four identified propagation types, the convergence of multiple SD events into a single VD event (Type 3) was the most frequent and had the longest mean distance, highlighting the cumulative effects of sequential or simultaneous SM deficits on vegetation. 

The thresholds for triggering VD increased with drought severity. Across most regions, SD duration thresholds ranged from 1 to 6 months, with exceptions in regions IV and V where they exceeded 10 months. The SD severity thresholds corresponding to all VD levels in region VIII were generally higher than those in other regions. A comparative analysis of drought propagation probabilities across nine eco-geographical regions further revealed that VD was more prone to occurring in region II and southeastern parts of regions V and VI, highlighting marked spatial heterogeneity. 

The statistical associations between key contributors and PT exhibited pronounced regional heterogeneity. In humid regions, energy-related factors (SunD, TMP, and CO₂) showed the strongest associations with shorter PT, suggesting that atmospheric demand may regulate vegetation response under sufficient water supply. PRE was the primary contributor in arid regions, where water scarcity fundamentally constrains vegetation response, while TMP and SMrz were the key contributors in semi-arid areas. 

Overall, by employing a 3-D spatio-temporal identification framework, this study comprehensively revealed the patterns of SD and VD events and their propagation dynamics across diverse eco-geographical regions of China. Through quantitative assessments of spatio-temporal linkages, propagation thresholds, and regional contributors, this study provides a scientific basis for understanding vegetation vulnerability to water stress. These findings are of practical significance for strengthening regional water resource management and developing effective adaptation strategies to enhance ecosystem resilience under a warming climate. 

20 

_Journal of Hydrology: Regional Studies 67 (2026) 103786_ 

_Y. Du et al._ 

## **CRediT authorship contribution statement** 

**Yuxuan Du:** Writing – original draft, Methodology. **Tao Peng:** Writing – review & editing, Supervision. **Vijay P. Singh:** Writing – review & editing. **Ji Liu:** Project administration. **Xiaohua Dong:** Investigation. **Qingxia Lin:** Conceptualization. **Jiali Guo:** Data curation. **Chao Song:** Validation. **Dan Yu:** Formal analysis. **Gaoxu Wang:** Resources. 

## **Declaration of Competing Interest** 

The authors report no conflicts of interest. The authors alone are responsible for the content and writing of this article. 

## **Acknowledgment** 

This study was supported by the National Natural Science Foundation of China (No. 52179018, 52509024), Natural Science Foundation of Hubei Province of China (2024AFD212), and Hubei Provincial Key Laboratory of Construction and Management in Hydropower Engineering, Three Gorges University, China (2023KSD30). The authors are grateful to the editor and anonymous reviewers for their constructive comments and suggestions, which greatly improved the quality of this manuscript. 

## **Appendix A. Supporting information** 

Supplementary data associated with this article can be found in the online version at doi:10.1016/j.ejrh.2026.103786. 

## **Data availability** 

Data will be made available on request. 

## **References** 

- Abel, C., Abdi, A.M., Tagesson, T., Horion, S., Fensholt, R., 2023. Contrasting ecosystem vegetation response in global drylands under drying and wetting conditions. Glob. Change Biol. 29, 3954–3969. https://doi.org/10.1111/gcb.16745. 

- Ainsworth, E.A., Long, S.P., 2005. What have we learned from 15 years of free-air CO2 enrichment (FACE)? A meta-analytic review of the responses of photosynthesis, canopy properties and plant production to rising CO2. New Phytol. 165 (2), 351–372. https://doi.org/10.1111/j.1469-8137.2004.01224.x. 

- Ainsworth, E.A., Rogers, A., 2007. The response of photosynthesis and stomatal conductance to rising [CO2]: mechanisms and environmental interactions. Plant Cell Environ. 30 (3), 258–270. https://doi.org/10.1111/j.1365-3040.2007.01641.x. 

- Allen, C.D., Macalady, A.K., Chenchouni, H., Bachelet, D., McDowell, N., Vennetier, M., Kitzberger, T., Rigling, A., Breshears, D.D., Hogg, E.H.T., Gonzalez, P., Fensham, R., Zhang, Z., Castro, J., Demidova, N., Lim, J.-H., Allard, G., Running, S.W., Semerci, A., Cobb, N., 2010. A global overview of drought and heatinduced tree mortality reveals emerging climate change risks for forests. For. Ecol. Manag. 259 (4), 660–684. https://doi.org/10.1016/j.foreco.2009.09.001. 

- Anderegg, W.R.L., Berry, J.A., Smith, D.D., Sperry, J.S., Anderegg, L.D.L., Field, C.B., 2012. The roles of hydraulic and carbon stress in a widespread climate-induced forest die-off. Proc. Natl. Acad. Sci. U. S. A. 109 (1), 233–237. https://doi.org/10.1073/pnas.1107891109. 

- Andreadis, K.M., Clark, E.A., Wood, A.W., Hamlet, A.F., Lettenmaier, D.P., 2005. Twentieth-century drought in the conterminous United States. J. Hydrometeorol. 6 (6), 985–1001. https://doi.org/10.1175/JHM450.1. 

- Apurv, T., Sivapalan, M., Cai, X., 2017. Understanding the role of climate characteristics in drought propagation. Water Resour. Res. 53 (11), 9304–9329. https://doi. org/10.1002/2017WR021445. 

- Ault, T.R., 2020. On the essentials of drought in a changing climate. Science 368, 256–260. https://doi.org/10.1126/science.aaz5492. 

Ayantobo, O.O., Li, Y., Song, S., 2019. Copula-based trivariate drought frequency analysis approach in seven climatic sub-regions of mainland China over 1961–2013. Theor. Appl. Climatol. 137 (3), 2217–2237. https://doi.org/10.1007/s00704-018-2724-x. 

- Bai, H., Li, L., Wu, Y., Feng, G., Gong, Z., Sun, G., 2022. Identifying critical meteorological elements for vegetation coverage change in China. Front. Phys. 10, 834094. https://doi.org/10.3389/fphy.2022.834094. 

- Bassiouni, M., Good, S.P., Still, C.J., Higgins, C.W., 2020. Plant water uptake thresholds inferred from satellite soil moisture. Geophys. Res. Lett. 47 (7), e2020GL087077. https://doi.org/10.1029/2020GL087077. 

- Bento, V.A., Gouveia, C.M., DaCamara, C.C., Trigo, I.F., 2018. A climatological assessment of drought impact on vegetation health index. Agric. For. Meteorol. 259, 286–295. https://doi.org/10.1016/j.agrformet.2018.05.014. 

- Chen, L., Brun, P., Buri, P., Fatichi, S., Gessler, A., McCarthy, M.J., Pellicciotti, F., Stocker, B., Karger, D.N., 2025a. Global increase in the occurrence and impact of multiyear droughts. Science 387 (6731), 278–284. https://doi.org/10.1126/science.ado4245. 

- Chen, C., Peng, T., Singh, V.P., Wang, Y., Zhang, T., Dong, X., Lin, Q., Guo, J., Liu, J., Fan, T., Wang, G., 2024. Assessment of dynamic hydrological drought risk from a non-stationary perspective. Hydrol. Process. 38, e15267. https://doi.org/10.1002/hyp.15267. 

- Chen, Y., Wu, H., Xie, N., Liang, X., Jiang, L., Qiu, M., Li, Y., 2025b. STAT-LSTM: A multivariate spatiotemporal feature aggregation model for SPEI-based drought prediction. Earth Sci. Inform. 18, 289. https://doi.org/10.1007/s12145-025-01813-0. 

- Chen, T., Guestrin, C., 2016. XGBoost: a scalable tree boosting system. In: Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. Association for Computing Machinery, New York, NY, pp. 785–794. doi:10.1145/2939672.2939785. 

- Cheng, W., Dan, L., Deng, X., Feng, J., Wang, Y., Peng, J., Tian, J., Qi, W., Liu, Z., Zheng, X., Zhou, D., Jiang, S., Zhao, H., Wang, X., 2022. Global monthly gridded atmospheric carbon dioxide concentrations under the historical and future scenarios. Sci. Data 9 (1), 83. https://doi.org/10.1038/s41597-022-01196-7. 

- Cook, B.I., Mankin, J.S., Anchukaitis, K.J., 2018. Climate change and drought: From past to future. Curr. Clim. Change Rep. 4 (2), 164–179. https://doi.org/10.1007/ s40641-018-0093-2. 

Crausbay, S.D., Ramirez, A.R., Carter, S.L., Cross, M.S., Hall, K.R., Bathke, D.J., Betancourt, J.L., Colt, S., Cravens, A.E., Dalton, M.S., Dunham, J.B., Hay, L.E., Hayes, M.J., McEvoy, J., McNutt, C.A., Moritz, M.A., Nislow, K.H., Raheem, N., Sanford, T., 2017. Defining ecological drought for the twenty-first century. Bull. Am. Meteorol. Soc. 98 (12), 2543–2550. https://doi.org/10.1175/BAMS-D-16-0292.1. 

Dai, A., 2013. Increasing drought under global warming in observations and models. Nat. Clim. Change 3 (1), 52–58. https://doi.org/10.1038/nclimate1633. 

21 

_Journal of Hydrology: Regional Studies 67 (2026) 103786_ 

_Y. Du et al._ 

- Das, S., Das, J., Umamahesh, N.V., 2022. Investigating the propagation of droughts under the influence of large-scale climate indices in India. J. Hydrol. 610, 127900. https://doi.org/10.1016/j.jhydrol.2022.127900. 

- Deng, S., Tan, X., Tan, X., Wu, X., Huang, Z., Liu, Y., Liu, B., 2024. On the development and recovery of soil moisture deficit drought events. J. Hydrol. 632, 130920. https://doi.org/10.1016/j.jhydrol.2024.130920. 

- Ding, Y., Gong, X., Xing, Z., Cai, H., Zhou, Z., Zhang, D., Sun, P., Shi, H., 2021. Attribution of meteorological, hydrological and agricultural drought propagation in different climatic regions of China. Agric. Water Manag. 255, 106996. https://doi.org/10.1016/j.agwat.2021.106996. 

- Fan, Y., Miguez-Macho, G., Jobbagy, E.G., Jackson, R.B., Otero-Casal, C., 2017. Hydrologic regulation of plant rooting depth. Proc. Natl. Acad. Sci. U. S. A. 114 (40), ´ 10572–10577. https://doi.org/10.1073/pnas.1712381114. 

- Fang, W., Huang, S., Huang, Q., Huang, G., Wang, H., Leng, G., Wang, L., 2020. Identifying drought propagation by simultaneously considering linear and nonlinear dependence in the Wei River basin of the Loess Plateau, China. J. Hydrol. 591, 125287. https://doi.org/10.1016/j.jhydrol.2020.125287. 

- Fatichi, S., Pappas, C., Ivanov, V.Y., 2016. Modeling plant–water interactions: An ecohydrological overview from the cell to the global scale. Wiley Interdiscip. Rev. Water 3 (3), 327–368. https://doi.org/10.1002/wat2.1125. 

- Feng, K., Su, X., Singh, V.P., Ayantobo, O.O., Zhang, G., Wu, H., Zhang, Z., 2021. Dynamic evolution and frequency analysis of hydrological drought from a threedimensional perspective. J. Hydrol. 600, 126675. https://doi.org/10.1016/j.jhydrol.2021.126675. 

- Feng, F., Wang, K., 2021. Merging high-resolution satellite surface radiation data with meteorological sunshine duration observations over China from 1983 to 2017. Remote Sens. 13 (4), 602. https://doi.org/10.3390/rs13040602. 

- Feng, K., Wang, Y., Li, Y., Wang, F., Su, X., Zhang, Z., Wu, H., Zhang, G., Li, Y., Wang, X., 2024a. Three-dimensional perspective on the characterization of the spatiotemporal propagation from meteorological to agricultural drought. Agric. For. Meteorol. 353, 110048. https://doi.org/10.1016/j.agrformet.2024.110048. 

- Feng, K., Yuan, H., Wang, Y., Li, Y., Wang, X., Wang, F., Su, X., Zhang, Z., 2024b. Propagation dynamics from meteorological to agricultural drought in Northwestern China: key influencing factors. Agronomy 14 (9), 1987. https://doi.org/10.3390/agronomy14091987. 

- Fu, C., Hu, Z., Yang, Y., Deng, M., Yu, H., Lu, S., Wu, D., Fan, W., 2022. Responses of soil freeze–thaw processes to climate on the Tibetan Plateau from 1980 to 2016. Remote Sens. 14 (23), 5907. https://doi.org/10.3390/rs14235907. 

- Gao, G., Li, Y., Chen, Y.X., Feng, A.Q., 2023. The evolution characteristics of drought spatio-temporal law in China in the recent 30 years. China Flood Drought Manag. 33, 2023192. https://doi.org/10.16867/j.issn.1673-9264.2023192. 

- Ge, C., Sun, P., Yao, R., Zhang, Y., Shen, H., Yang, H., 2025. Drivers of ecological drought recovery: insights from meteorological and soil drought impact. J. Hydrol. 646, 132324. https://doi.org/10.1016/j.jhydrol.2024.132324. 

- Gebrechorkos, S.H., Sheffield, J., Vicente-Serrano, S.M., Funk, C., Miralles, D.G., Peng, J., Dyer, E., Talib, J., Beck, H.E., Singer, M.B., Dadson, S.J., 2025. Warming accelerates global drought severity. Nature 642, 628–635. https://doi.org/10.1038/s41586-025-09047-2. 

- Gelsor, N., Gelsor, N., Wangmo, T., Chen, Y.C., Frette, Ø., Stamnes, J.J., Hamre, B., 2018. Solar energy on the Tibetan Plateau: atmospheric influences. Sol. Energy 173, 984–992. https://doi.org/10.1016/j.solener.2018.08.024. 

- Genest, C., Favre, A.-C., B´eliveau, J., Jacques, C., 2007. Metaelliptical copulas and their use in frequency analysis of multivariate hydrological data. Water Resour. Res. 43 (9), W09401. https://doi.org/10.1029/2006WR005275. 

- Geng, G., Zhang, B., Gu, Q., He, Z., Zheng, R., 2024. Drought propagation characteristics across China: time, probability, and threshold. J. Hydrol. 631, 130805. https://doi.org/10.1016/j.jhydrol.2024.130805. 

- Gu, X., Li, Y., Zhang, Y., Hussain, A., Jamshidi, S., Gu, L., Wang, D., 2026. Evaluating the propagation process of meteorological, hydrological, and agricultural drought dynamics in the Yellow River Basin. Sci. Rep. 16, 14564. https://doi.org/10.1038/s41598-026-45050-x. 

- Guo, Y., Huang, S., Huang, Q., Wang, H., Wang, L., Fang, W., 2019. Copulas-based bivariate socioeconomic drought dynamic risk assessment in a changing environment. J. Hydrol. 575, 1052–1064. https://doi.org/10.1016/j.jhydrol.2019.06.010. 

- Guo, Y., Huang, S., Huang, Q., Leng, G., Fang, W., Wang, L., Wang, H., 2020. Propagation thresholds of meteorological drought for triggering hydrological drought at various levels. Sci. Total Environ. 712, 136502. https://doi.org/10.1016/j.scitotenv.2020.136502. 

- Haghpanah, M., Hashemipetroudi, S., Arzani, A., Araniti, F., 2024. Drought tolerance in plants: physiological and molecular responses. Plants 13 (21), 2962. https:// doi.org/10.3390/plants13212962. 

- Han, Z., Huang, S., Huang, Q., Leng, G., Wang, H., Bai, Q., Zhao, J., Ma, L., Wang, L., Du, M., 2019. Propagation dynamics from meteorological to groundwater drought and their possible influence factors. J. Hydrol. 578, 124102. https://doi.org/10.1016/j.jhydrol.2019.124102. 

- Hao, Z., Singh, V.P., 2015. Drought characterization from a multivariate perspective: a review. J. Hydrol. 527, 668–678. https://doi.org/10.1016/j. jhydrol.2015.05.031. 

- Hilker, T., Lyapustin, A.I., Tucker, C.J., Hall, F.G., Myneni, R.B., Wang, Y., Bi, J., Mendes de Moura, Y., Sellers, P.J., 2014. Vegetation dynamics and rainfall sensitivity of the Amazon. Proc. Natl. Acad. Sci. U. S. A. 111 (45), 16041–16046. https://doi.org/10.1073/pnas.1404870111. 

- Hua, L., Wang, H., Sui, H., Wardlow, B., Hayes, M.J., Wang, J., 2019. Mapping the spatial-temporal dynamics of vegetation response lag to drought in a semi-arid region. Remote Sens. 11 (16), 1873. https://doi.org/10.3390/rs11161873. 

- Huang, S., Li, P., Huang, Q., Leng, G., Hou, B., Ma, L., 2017. The propagation from meteorological to hydrological drought and its potential influence factors. J. Hydrol. 547, 184–195. https://doi.org/10.1016/j.jhydrol.2017.01.041. 

- Jiang, P., Ding, W., Yuan, Y., Ye, W., Mu, Y., 2022a. Interannual variability of vegetation sensitivity to climate in China. J. Environ. Manag. 301, 113768. https://doi. org/10.1016/j.jenvman.2021.113768. 

- Jiang, T., Su, X., Qu, Y., Singh, V.P., Zhang, T., Chu, J., Hu, X., 2024. Determining the response of ecological drought to meteorological and groundwater droughts in Northwest China using a spatio-temporal matching method. J. Hydrol. 633, 130753. https://doi.org/10.1016/j.jhydrol.2024.130753. 

- Jiang, T., Su, X., Singh, V.P., Zhang, G., 2022b. Spatio-temporal pattern of ecological droughts and their impacts on health of vegetation in Northwestern China. J. Environ. Manag. 305, 114356. https://doi.org/10.1016/j.jenvman.2021.114356. 

- Jin, L., Peng, T., Fan, T., Singh, V.P., Lin, Q., Dong, X., Liu, J., Guo, J., Yu, D., Wang, G., 2024. Modified drought propagation under a changing environment: a case study in the Dongting Lake basin, China. J. Hydr. Reg. Stud. 56, 101986. https://doi.org/10.1016/j.ejrh.2024.101986. 

- Kuang, X.X., Jiao, J.J., 2016. Review on climate change on the Tibetan Plateau during the last half century. J. Geophys. Res. Atmos. 121, 3979–4007. https://doi.org/ 10.1002/2015JD024728. 

- Kumar, R., Musuuza, J.L., Van Loon, A.F., Teuling, A.J., Barthel, R., Ten Broek, J., Mai, J., Samaniego, L., Attinger, S., 2016. Multiscale evaluation of the Standardized Precipitation Index as a groundwater drought indicator. Hydrol. Earth Syst. Sci. 20 (3), 1117–1131. https://doi.org/10.5194/hess-20-1117-2016. 

- Lan, X., Li, W., Tang, J., Shakoor, A., Zhao, F., Fan, J., 2022. Spatiotemporal variation of climate of different flanks and elevations of the Qinling–Daba mountains in China during 1969–2018. Sci. Rep. 12, 6952. https://doi.org/10.1038/s41598-022-10819-3. 

- Lan, X., Li, R., Wang, X., Zhou, T., Li, Y., Duo, J., Sun, J., 2025. Vegetation dynamics and sensitivity responds to climate change in the upstream of the Yellow River, China. Ecosyst. Health Sustain. 11, 0292. https://doi.org/10.34133/ehs.0292. 

- Li, Y., Deng, Q., Chang, J., Huang, Y., Zhang, H., Fan, J., Wu, H., 2025c. Nonlinear propagation of meteorological to hydrological drought: contrasting dynamics in humid and semi-arid regions. J. Hydrol. 657, 133012. https://doi.org/10.1016/j.jhydrol.2025.133012. 

- Li, T., Fu, B., Lü, Y., Du, C., Zhao, Z., Wang, F., Gao, G., Wu, X., 2024b. Soil freeze–thaw cycles affect spring phenology by changing phenological sensitivity in the Northern Hemisphere. Sci. Total Environ. 914, 169963. https://doi.org/10.1016/j.scitotenv.2024.169963. 

- Li, C., Fu, Y., Zhao, Q., Zhang, X., Ding, R., Hao, F., Yin, G., 2025a. Climatic driving mechanisms of the propagation from meteorological drought to agricultural and ecological droughts. J. Environ. Manag. 383, 125445. https://doi.org/10.1016/j.jenvman.2025.125445. 

- Li, J., Guo, Y., Wang, Y., Lu, S., Chen, X., 2018. Drought propagation patterns under naturalized condition using daily hydrometeorological data. Adv. Meteorol. 2018, 2469156. https://doi.org/10.1155/2018/2469156. 

- Li, M., Han, A., Tong, S., Wang, Y., Guo, E., Zhang, T., Yin, S., Bao, Y., 2025b. Study on the propagation processes and driving mechanisms of meteorological, hydrological, and agricultural droughts on the Mongolian Plateau. J. Hydrol., 133511 https://doi.org/10.1016/j.jhydrol.2025.133511. 

22 

- _Y. Du et al.                                                                                                                                                                                                              Journal of Hydrology: Regional Studies 67 (2026) 103786_ Li, W., Reichstein, M., O, S., May, C., Destouni, G., Migliavacca, M., Kraft, B., Weber, U., Orth, R., 2023. Contrasting drought propagation into the terrestrial water cycle between dry and wet regions. Earth’s Future 11 (7), e2022EF003441. https://doi.org/10.1029/2022EF003441. 

- Li, M., Sun, H., Huang, Y., Chen, H., 2024a. Shapley value: from cooperative game to explainable artificial intelligence. Auton. Intell. Syst. 4 (1), 2. https://doi.org/ 10.1007/s43684-023-00060-8. 

- Li, J., Wang, Z., Wu, X., Chen, J., Guo, S., Zhang, Z., 2020. A new framework for tracking flash drought events in space and time. Catena 194, 104763. https://doi.org/ 10.1016/j.catena.2020.104763. 

- Liu, Z., Lin, H., Li, H., Li, M., Zhou, P., Wang, Z., Niu, J., 2025. Response mechanisms of vegetation productivity to water variability in arid and semi-arid areas of China: a decoupling analysis of soil moisture and precipitation. Atmosphere 16 (8), 933. https://doi.org/10.3390/atmos16080933. 

- Liu, Y., Liu, Y., Wang, W., Zhou, H., 2021. Propagation of soil moisture droughts in a hotspot region: spatial pattern and temporal trajectory. J. Hydrol. 593, 125906. https://doi.org/10.1016/j.jhydrol.2020.125906. 

- Liu, Y., Shan, F., Yue, H., Wang, X., 2023. Characteristics of drought propagation and effects of water resources on vegetation in the karst area of Southwest China. Sci. Total Environ. 891, 164663. https://doi.org/10.1016/j.scitotenv.2023.164663. 

- Liu, Y., Zhu, Y., Ren, L., Singh, V.P., Yong, B., Jiang, S., Yuan, F., Yang, X., 2019. Understanding the spatiotemporal links between meteorological and hydrological droughts from a three-dimensional perspective. J. Geophys. Res. Atmos. 124 (6), 3090–3109. https://doi.org/10.1029/2018JD028947. 

- Lloyd-Hughes, B., 2012. A spatio-temporal structure-based approach to drought characterisation. Int. J. Climatol. 32 (3), 406–418. https://doi.org/10.1002/joc.2280. Lu, J., Carbone, G.J., Huang, X., Lackstrom, K., Gao, P., 2020. Mapping the sensitivity of agriculture to drought and estimating the effect of irrigation in the United States, 1950–2016. Agric. For. Meteorol. 292, 108124. https://doi.org/10.1016/j.agrformet.2020.108124. 

- Lundberg, S.M., Lee, S.-I., 2017. A unified approach to interpreting model predictions. Adv. Neural Inf. Process. Syst. 30. https://doi.org/10.48550/ arXiv.1705.07874. 

- Ma, F., Yuan, X., 2024. Vegetation greening and climate warming increased the propagation risk from meteorological drought to soil drought at subseasonal timescales. Geophys. Res. Lett. 51 (4), e2023GL107937. https://doi.org/10.1029/2023GL107937. 

- Mao, J., Ribes, A., Yan, B., Shi, X., Thornton, P.E., S´ef´erian, R., Ciais, P., Myneni, R.B., Douville, H., Piao, S., Zhu, Z., Dickinson, R.E., Dai, Y., Ricciuto, D.M., Jin, M., Hoffman, F.M., Wang, B., Huang, M., Lian, X., 2016. Human-induced greening of the northern extratropical land surface. Nat. Clim. Change 6 (10), 959–963. https://doi.org/10.1038/nclimate3056. 

- McDermid, S.S., Cook, B.I., De Kauwe, M.G., Mankin, J., Smerdon, J.E., Williams, A.P., Seager, R., Puma, M.J., Aleinov, I., Kelley, M., Nazarenko, L., 2021. Disentangling the regional climate impacts of competing vegetation responses to elevated atmospheric CO2. J. Geophys. Res. Atmos. 126 (5), e2020JD034108. https://doi.org/10.1029/2020JD034108. 

- McKee, T.B., Doesken, N.J., Kleist, J., 1993. The relationship of drought frequency and duration to time scales. In: Proceedings of the 8th Conference on Applied Climatology, 17–22 January 1993, Anaheim, CA, USA. American Meteorological Society, Boston, MA, pp. 179–184. 

- Meng, T., Sun, P., 2023. Variations of deep soil moisture under different vegetation restoration types in a watershed of the Loess Plateau, China. Sci. Rep. 13, 4957. https://doi.org/10.1038/s41598-023-32038-0. 

- Miao, G., Guan, K., Yang, X., Bernacchi, C.J., Berry, J.A., DeLucia, E.H., Wu, J., Moore, C.E., Meacham, K., Cai, Y., Peng, B., Kimm, H., Masters, M.D., 2018. Suninduced chlorophyll fluorescence, photosynthesis, and light use efficiency of a soybean field from seasonally continuous measurements. J. Geophys. Res. Biogeosci. 123 (2), 610–623. https://doi.org/10.1002/2017JG004180. 

- Miralles, D.G., Bonte, O., Koppa, A., Baez-Villanueva, O.M., Tronquo, E., Zhong, F., Beck, H.E., Hulsman, P., Dorigo, W., Verhoest, N.E.C., Haghdoost, S., 2025. GLEAM4: global land evaporation and soil moisture dataset at 0.1 resolution from 1980 to near present. Sci. Data 12 (1), 416. https://doi.org/10.1038/s41597025-04610-y. 

- Mishra, A.K., Singh, V.P., 2010. A review of drought concepts. J. Hydrol. 391 (1–2), 202–216. https://doi.org/10.1016/j.jhydrol.2010.07.012. 

- Mohanta, T.K., Mohanta, Y.K., Kaushik, P., Kumar, J., 2024. Physiology, genomics, and evolutionary aspects of desert plants. J. Adv. Res. 58, 63–78. https://doi.org/ 10.1016/j.jare.2023.04.019. 

- Müllers, Y., Postma, J.A., Poorter, H., van Dusschoten, D., 2022. Stomatal conductance tracks soil-to-leaf hydraulic conductance in faba bean and maize during soil drying. Plant Physiol. 190 (4), 2279–2294. https://doi.org/10.1093/plphys/kiac422. 

- Munoz-Sabater, J., Dutra, E., Agustí-Panareda, A., Albergel, C., Arduini, G., Balsamo, G., Boussetta, S., Choulga, M., Harrigan, S., Hersbach, H., Martens, B., ˜ Miralles, D.G., Piles, M., Rodríguez-Fernandez, N.J., Zsoter, E., Buontempo, C., Th´ ´epaut, J.-N., 2021. ERA5-Land: a state-of-the-art global reanalysis dataset for land applications. Earth Syst. Sci. Data 13, 4349–4383. https://doi.org/10.5194/essd-13-4349-2021. 

- Norby, R.J., DeLucia, E.H., Gielen, B., Calfapietra, C., Giardina, C.P., King, J.S., Ledford, J., McCarthy, H.R., Moore, D.J.P., Ceulemans, R., De Angelis, P., Finzi, A.C., Karnosky, D.F., Kubiske, M.E., Lukac, M., Pregitzer, K.S., Scarascia-Mugnozza, G.E., Schlesinger, W.H., Oren, R., 2005. Forest response to elevated CO2 is conserved across a broad range of productivity. Proc. Natl. Acad. Sci. U. S. A. 102 (50), 18052–18056. https://doi.org/10.1073/pnas.0509478102. 

- Novick, K.A., Ficklin, D.L., Stoy, P.C., Williams, C.A., Bohrer, G., Oishi, A.C., Papuga, S.A., Blanken, P.D., Noormets, A., Sulman, B.N., Scott, R.L., Wang, L., Phillips, R. P., 2016. The increasing importance of atmospheric demand for ecosystem water and carbon fluxes. Nat. Clim. Change 6 (11), 1023–1027. https://doi.org/ 10.1038/nclimate3114. 

- Peters, E., Torfs, P.J.J.F., van Lanen, H.A.J., Bier, G., 2003. Propagation of drought through groundwater—a new approach using linear reservoir theory. Hydrol. Process. 17 (15), 3023–3040. https://doi.org/10.1002/hyp.1274. 

- Pielke Sr., R.A., Pitman, A., Niyogi, D., Mahmood, R., McAlpine, C., Hossain, F., Klein Goldewijk, K.K., Nair, U., Betts, R., Fall, S., Reichstein, M., Kabat, P., de Noblet, N., 2011. Land use/land cover changes and climate: modeling analysis and observational evidence. Wiley Interdiscip. Rev. Clim. Change 2 (6), 828–850. https://doi.org/10.1002/wcc.144. 

- Qin, J., Ma, M., Shi, J., Ma, S., Wu, B., Su, X., 2023. The time-lag effect of climate factors on the forest enhanced vegetation index for subtropical humid areas in China. Int. J. Environ. Res. Public Health 20 (1), 799. https://doi.org/10.3390/ijerph20010799. 

- Qin, Y., Wu, T., Zhao, L., Wu, X., Li, R., Xie, C., Pang, Q., Hu, G., Qiao, Y., Zhao, G., Liu, G., Zhu, X., Hao, J., 2017. Numerical modeling of the active layer thickness and permafrost thermal state across the Qinghai-Tibetan Plateau. J. Geophys. Res. Atmos. 122, 11604–11620. https://doi.org/10.1002/2017JD026858. 

- Ren, H., Wen, Z., Liu, Y., Lin, Z., Han, P., Shi, H., Wang, Z., Su, T., 2023. Vegetation response to changes in climate across different climate zones in China. Ecol. Indic. 155, 110932. https://doi.org/10.1016/j.ecolind.2023.110932. 

- Rodell, M., Houser, P.R., Jambor, U., Gottschalck, J., Mitchell, K., Meng, C.-J., Arsenault, K., Cosgrove, B., Radakovich, J., Bosilovich, M., Entin, J.K., Walker, J.P., Lohmann, D., Toll, D., 2004. The Global Land Data Assimilation System. Bull. Am. Meteorol. Soc. 85, 381–394. https://doi.org/10.1175/BAMS-85-3-381. 

- Salvadori, G., De Michele, C., 2015. Multivariate real-time assessment of droughts via copula-based multi-site hazard trajectories and fans. J. Hydrol. 526, 101–115. https://doi.org/10.1016/j.jhydrol.2014.11.056. 

- Sawada, Y., 2018. Quantifying drought propagation from soil moisture to vegetation dynamics using a newly developed ecohydrological land reanalysis. Remote Sens. 10 (8), 1197. https://doi.org/10.3390/rs10081197. 

- Seddon, A.W.R., Macias-Fauria, M., Long, P.R., Benz, D., Willis, K.J., 2016. Sensitivity of global terrestrial ecosystems to climate variability. Nature 531 (7593), 229–232. https://doi.org/10.1038/nature16986. 

- Seneviratne, S.I., Corti, T., Davin, E.L., Hirschi, M., Jaeger, E.B., Lehner, I., Orlowsky, B., Teuling, A.J., 2010. Investigating soil moisture–climate interactions in a changing climate: a review. Earth-Sci. Rev. 99 (3–4), 125–161. https://doi.org/10.1016/j.earscirev.2010.02.004. 

- Shangguan, W., Dai, Y., Liu, B., Zhu, A., Duan, Q., Wu, L., Ji, D., Ye, A., Yuan, H., Zhang, Q., Chen, D., Chen, M., Chu, J., Dou, Y., Guo, J., Li, H., Li, J., Liang, L., Liang, X., Liu, H., Liu, S., Miao, C., Zhang, Y., 2013. A China data set of soil properties for land surface modeling. J. Adv. Model Earth Syst. 5 (2), 212–224. https://doi.org/10.1002/jame.20026. 

- Shao, X., Gao, X., Zeng, Y., Yang, M., Wang, Y., Zhao, X., 2023. Eco-physiological constraints of deep soil desiccation in semiarid tree plantations. Water Resour. Res. 59 (8), e2022WR034246. https://doi.org/10.1029/2022WR034246. 

- Sun, Y., Guan, Q., Zhang, Z., Zhang, J., Cui, Z., Pan, L., 2025. Ecosystem drought recovery and influencing factors in temperate China and the Qinghai–Tibet alpine region. Catena 260, 109417. https://doi.org/10.1016/j.catena.2025.109417. 

23 

_Y. Du et al.                                                                                                                                                                                                              Journal of Hydrology: Regional Studies 67 (2026) 103786_ 

Sun, W., Song, H., Yao, X., Ishidaira, H., Xu, Z., 2015. Changes in remotely sensed vegetation growth trend in the Heihe Basin of arid northwestern China. PLOS ONE 10 (8), e0135376. https://doi.org/10.1371/journal.pone.0135376. Teutschbein, C., Grabs, T., Giese, M., Todorovi´c, A., Barthel, R., 2025. Drought propagation in high-latitude catchments: insights from a 60-year analysis using standardized indices. Nat. Hazards Earth Syst. Sci. 25 (7), 2541–2564. https://doi.org/10.5194/nhess-25-2541-2025. Tian, Y., Zheng, H., Yan, M., Wu, L., 2025. Research on the response mechanism of vegetation to drought stress in the West Liao River Basin, China. Remote Sens. 17 (10), 1780. https://doi.org/10.3390/rs17101780. Van Lanen, H.A.J., Wanders, N., Tallaksen, L.M., van Loon, A.F., 2013. Hydrological drought across the world: impact of climate and physical catchment structure. Hydrol. Earth Syst. Sci. 17 (5), 1715–1732. https://doi.org/10.5194/hess-17-1715-2013. Van Loon, A.F., 2015. Hydrological drought explained. Wiley Interdiscip. Rev. Water 2 (4), 359–392. https://doi.org/10.1002/wat2.1085. Van Loon, A.F., Van Huijgevoort, M.H.J., Van Lanen, H.A.J., 2012. Evaluation of drought propagation in an ensemble mean of large-scale hydrological models. Hydrol. Earth Syst. Sci. 16 (11), 4057–4078. https://doi.org/10.5194/hess-16-4057-2012. Vicente-Serrano, S.M., Gouveia, C., Camarero, J.J., Beguería, S., Trigo, R., Lopez-Moreno, J.I., Azorín-Molina, C., Pasho, E., Lorenzo-Lacruz, J., Revuelto, J., Mor´ ´anTejeda, E., Sanchez-Lorenzo, A., 2013. Response of vegetation to drought time-scales across global land biomes. Proc. Natl. Acad. Sci. U. S. A. 110 (1), 52–57. https://doi.org/10.1073/pnas.1207068110. Wang, J., Bao, Z., Wang, G., Liu, C., Xie, M., Wang, B., Zhang, J., 2024b. The time lag effects and interaction among climate, soil moisture, and vegetation from in situ monitoring measurements across China. Remote Sens. 16 (12), 2063. https://doi.org/10.3390/rs16122063. Wang, Z., Chang, J., Wang, Y., Yang, Y., Guo, Y., Yang, G., He, B., 2024c. Temporal and spatial propagation characteristics of meteorological drought to hydrological drought and influencing factors. Atmos. Res. 299, 107212. https://doi.org/10.1016/j.atmosres.2023.107212. Wang, D., Hejazi, M., Cai, X., Valocchi, A.J., 2011. Climate change impact on meteorological, agricultural, and hydrological drought in central Illinois. Water Resour. Res. 47 (9). https://doi.org/10.1029/2010WR009845. Wang, F., Lai, H., Li, Y., Feng, K., Tian, Q., Guo, W., Zhang, W., Di, D., Yang, H., 2023. Dynamic variations of terrestrial ecological drought and propagation analysis with meteorological drought across the mainland China. Sci. Total Environ. 896, 165314. https://doi.org/10.1016/j.scitotenv.2023.165314. Wang, F., Lai, H., Wang, Z., Men, R., Li, Y., Jiang, Y., Feng, K., Tian, Q., Du, X., Qu, Y., 2024a. Dynamic relationships and propagation characteristics between meteorological drought and vegetation drought based on a three-dimensional identification algorithm. Glob. Planet. Change 240, 104535. https://doi.org/ 10.1016/j.gloplacha.2024.104535. Wang, Z., Wang, C., Liu, S., 2022. Elevated CO2 alleviates adverse effects of drought on plant water relations and photosynthesis: a global meta-analysis. J. Ecol. 110 (12), 2836–2849. https://doi.org/10.1111/1365-2745.13988. Wang, J., Wang, W., Cheng, H., Wang, H., Zhu, Y., 2021. Propagation from meteorological to hydrological drought and its influencing factors in the Huaihe River Basin. Water 13 (14), 1985. https://doi.org/10.3390/w13141985. Wang, F., Wang, Z., Yang, H., Di, D., Zhao, Y., Liang, Q., Hussain, Z., 2020. Comprehensive evaluation of hydrological drought and its relationships with meteorological drought in the Yellow River basin, China. J. Hydrol. 584, 124751. https://doi.org/10.1016/j.jhydrol.2020.124751. Wang, T., Zhang, J., Li, Z., Liu, Y., Chen, X., 2025. Roles of soil and atmospheric dryness on terrestrial vegetation productivity in China—which dominates at what thresholds. Earth’s Future 13 (3), e2024EF005469. https://doi.org/10.1029/2024EF005469. Wang, K., Zhang, L., Qiu, Y., Ji, L., Tian, F., Wang, C., Wang, Z., 2015. Snow effects on alpine vegetation in the Qinghai-Tibetan Plateau. Int. J. Digit. Earth 8 (1), 56–73. https://doi.org/10.1080/17538947.2013.848946. 

- Warter, M.M., Singer, M.B., Cuthbert, M.O., Roberts, D., Caylor, K.K., Sabathier, R., Stella, J., 2021. Drought onset and propagation into soil moisture and grassland vegetation responses during the 2012–2019 major drought in Southern California. Hydrol. Earth Syst. Sci. 25 (6), 3713–3729. https://doi.org/10.5194/hess-253713-2021. 

- Wei, P., Hao, S., Shi, Y., Anand, A., Wang, Y., Chu, M., Ning, Z., 2024. Combining Google traffic map with deep learning model to predict street-level traffic-related air pollutants in a complex urban environment. Environ. Int. 191, 108992. https://doi.org/10.1016/j.envint.2024.108992. 

- Wei, W., Liu, T., Zhou, L., Wang, J., Yan, P., Xie, B., Zhou, J., 2023. Drought-related spatiotemporal cumulative and time-lag effects on terrestrial vegetation across China. Remote Sens. 15 (18), 4362. https://doi.org/10.3390/rs15184362. 

- Wei, W., Pang, S., Wang, X., Zhou, L., Xie, B., Zhou, J., Li, C., 2020. Temperature vegetation precipitation dryness index (TVPDI)-based dryness-wetness monitoring in China. Remote Sens. Environ. 248, 111957. https://doi.org/10.1016/j.rse.2020.111957. 

- Wen, X., Tu, Y., Tan, Q., Li, W., Fang, G., Ding, Z., Wang, Z., 2020. Construction of 3D drought structures of meteorological drought events and their spatio-temporal evolution characteristics. J. Hydrol. 590, 125539. https://doi.org/10.1016/j.jhydrol.2020.125539. 

- Wilhite, D.A., Glantz, M.H., 1985. Understanding: the drought phenomenon: the role of definitions. Water Int. 10 (3), 111–120. https://doi.org/10.1080/ 02508068508686328. 

- Wu, J., Chen, X., Yao, H., Zhang, D., 2021. Multi-timescale assessment of propagation thresholds from meteorological to hydrological drought. Sci. Total Environ. 765, 144232. https://doi.org/10.1016/j.scitotenv.2020.144232. 

- Wu, S., Li, R., Bu, C., Zhu, C., Miao, C., Zhang, Y., Cui, J., Jiang, Y., Ding, X., 2024. Photoperiodic effect on growth, photosynthesis, mineral elements, and metabolome of tomato seedlings in a plant factory. Plants 13 (22), 3119. https://doi.org/10.3390/plants13223119. 

- Wu, D., Zhao, X., Liang, S., Zhou, T., Huang, K., Tang, B., Zhao, W., 2015. Time-lag effects of global vegetation responses to climate change. Glob. Change Biol. 21 (9), 3520–3531. https://doi.org/10.1111/gcb.12945. 

- Xing, Z., Li, X., Fan, L., Colliander, A., Frappart, F., de Rosnay, P., Fernandez-Moran, R., Liu, X., Wang, H., Zhao, L., Wigneron, J.-P., 2023. Assessment of 9 km SMAP soil moisture: evidence of narrowing the gap between satellite retrievals and model-based reanalysis. Remote Sens. Environ. 296, 113721. https://doi.org/ 10.1016/j.rse.2023.113721. 

- Xu, K., Yang, D., Yang, H., Li, Z., Qin, Y., Shen, Y., 2015. Spatio-temporal variation of drought in China during 1961–2012: a climatic perspective. J. Hydrol. 526, 253–264. https://doi.org/10.1016/j.jhydrol.2014.09.047. 

- Yang, Y., Guan, H., Batelaan, O., McVicar, T.R., Long, D., Piao, S., Liang, W., Liu, B., Jin, Z., Simmons, C.T., 2016. Contrasting responses of water use efficiency to drought across global terrestrial ecosystems. Sci. Rep. 6, 23284. https://doi.org/10.1038/srep23284. 

- Yang, K., He, J., Tang, W., Qin, J., Cheng, C.C.K., 2010. On downward shortwave and longwave radiations over high altitude regions: observation and modeling in the Tibetan Plateau. Agric. For. Meteorol. 150 (1), 38–46. https://doi.org/10.1016/j.agrformet.2009.08.004. 

- Yang, J., Huang, X., 2021. The 30 m annual land cover dataset and its dynamics in China from 1990 to 2019. Earth Syst. Sci. Data 13 (8), 3907–3925. https://doi.org/ 10.5194/essd-13-3907-2021. 

- Yao, Y., Cui, L., 2022. Vegetation dynamics in the Qinling–Daba mountains through climate warming with land-use policy. Forests 13 (9), 1361. https://doi.org/ 10.3390/f13091361. 

- Yao, K., Tu, C., Zhang, A., Zeng, Z., Yang, Y., 2025. Distinguishing drought resistance strategies and identifying indicator traits of Platycladus orientalis and Broussonetia papyrifera. Front. Plant Sci. 16, 1644756. https://doi.org/10.3389/fpls.2025.1644756. 

- You, Z., Sun, X., Sun, H., Chen, L., Lu, M., Xue, J., Ban, X., Yan, B., Tuo, Y., Qin, H., Zhang, L., Zhang, W., 2025. Mechanisms of meteorological drought propagation to agricultural drought in China: insights from causality chain. npj Nat. Hazards 2 (1), 24. https://doi.org/10.1038/s44304-025-00073-8. 

- Zeng, J., Zhou, T., Qu, Y., Bento, V.A., Qi, J., Xu, Y., Li, Y., Wang, Q., 2023. An improved global vegetation health index dataset in detecting vegetation drought. Sci. Data 10 (1), 338. https://doi.org/10.1038/s41597-023-02255-3. 

- Zhang, K., Chen, H., Ma, N., Shang, S., Wang, Y., Xu, Q., Zhu, G., 2024. A global dataset of terrestrial evapotranspiration and soil moisture dynamics from 1982 to 2020. Sci. Data 11, 445. https://doi.org/10.1038/s41597-024-03271-7. 

- Zhang, R., Li, L., Zhang, Y., Huang, F., Li, J., Liu, W., Mao, T., Xiong, Z., Shangguan, W., 2021. Assessment of agricultural drought using soil water deficit index based on ERA5-Land soil moisture data in four southern provinces of China. Agriculture 11, 411. https://doi.org/10.3390/agriculture11050411. 

- Zhang, D., Liu, X., Zhang, L., Zhang, Q., Gan, R., Li, X., 2020. Attribution of evapotranspiration changes in humid regions of China from 1982 to 2016. J. Geophys. Res. Atmos. 125 (13), e2020JD032404. https://doi.org/10.1029/2020JD032404. 

24 

_Y. Du et al.                                                                                                                                                                                                              Journal of Hydrology: Regional Studies 67 (2026) 103786_ 

- Zhang, Q., Miao, C., Gou, J., Wu, J., Jiao, W., Song, Y., Xu, D., 2022a. Spatio-temporal characteristics of meteorological to hydrological drought propagation under natural conditions in China. Weather Clim. Extrem. 38, 100505. https://doi.org/10.1016/j.wace.2022.100505. 

- Zhang, L., Qiao, N., Huang, C., Wang, S., 2019b. Monitoring drought effects on vegetation productivity using satellite solar-induced chlorophyll fluorescence. Remote Sens. 11 (4), 378. https://doi.org/10.3390/rs11040378. 

- Zhang, X., She, D., Xia, J., Zhang, L., Deng, C., Liu, Z., 2023. The changing characteristics of propagation time from meteorological drought to hydrological drought in the Yangtze River basin, China. Atmos. Res. 290, 106774. https://doi.org/10.1016/j.atmosres.2023.106774. 

- Zhang, T., Su, X., Zhang, G., Wu, H., Wang, G., Chu, J., 2022b. Evaluation of the impacts of human activities on propagation from meteorological drought to hydrological drought in the Weihe River Basin, China. Sci. Total Environ. 819, 153030. https://doi.org/10.1016/j.scitotenv.2022.153030. 

- Zhang, J., Wang, J., Chen, J., Song, H., Li, S., Zhao, Y., Tao, J., Liu, J., 2019a. Soil moisture determines horizontal and vertical root extension in the perennial grass Lolium perenne L. growing in Karst soil. Front. Plant Sci. 10, 629. https://doi.org/10.3389/fpls.2019.00629. 

- Zhao, F., Wang, X., Wu, Y., Sivakumar, B., Liu, S., 2023b. Enhanced dependence of China’s vegetation activity on soil moisture under drier climate conditions. J. Geophys. Res. Biogeosci. 128 (5), e2022JG007300. https://doi.org/10.1029/2022JG007300. 

- Zhao, D., Zhang, Z., Zhang, Y., 2023a. Soil moisture dominates the forest productivity decline during the 2022 China compound drought-heatwave event. Geophys. Res. Lett. 50 (17), e2023GL104539. https://doi.org/10.1029/2023GL104539. 

- Zheng, D., 1999. A study on the ecogeographic regional system of China. In: Proceedings of the FAO FRA2000 Global Ecological Zoning Workshop, Cambridge, UK. Zhou, Z., Xue, P., Zhou, X., Wang, T., Ding, Y., Zhao, Y., Chen, P., Wang, X., 2025. Assessing the soil moisture-vegetation mutual feedback relationship in different climatic regions of mainland China. Catena 249, 108684. https://doi.org/10.1016/j.catena.2024.108684. 

- Zhu, L., Gong, H., Dai, Z., Xu, T., Su, X., 2015. An integrated assessment of the impact of precipitation and groundwater on vegetation growth in arid and semiarid areas. Environ. Earth Sci. 74, 5009–5021. https://doi.org/10.1007/s12665-015-4513-5. 

- Zhu, Y., Jiang, S., Ren, L., Guo, J., Zhong, F., Du, S., Cui, H., He, M., Duan, Z., 2024. Three-dimensional ecological drought identification and evaluation method considering eco-physiological status of terrestrial ecosystems. Sci. Total Environ. 951, 175423. https://doi.org/10.1016/j.scitotenv.2024.175423. 

- Zhu, Y., Liu, Y., Wang, W., Singh, V.P., Ma, X., Yu, Z., 2019. Three dimensional characterization of meteorological and hydrological droughts and their probabilistic links. J. Hydrol. 578, 124016. https://doi.org/10.1016/j.jhydrol.2019.124016. 

- Zong, X., Liu, Y., Yin, Y., 2024. Identifying the dominant compound events and their impacts on vegetation growth in China. Weather Clim. Extrem. 45, 100715. https://doi.org/10.1016/j.wace.2024.100715. 

25 

