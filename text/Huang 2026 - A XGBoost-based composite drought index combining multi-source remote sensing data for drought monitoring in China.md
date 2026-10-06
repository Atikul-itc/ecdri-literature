Journal of Hydrology: Regional Studies 66 (2026) 103623 



Contents lists available at ScienceDirect 

# Journal of Hydrology: Regional Studies 

journal homepage: www.elsevier.com/locate/ejrh 



A XGBoost-based composite drought index combining multi-source remote sensing data for drought monitoring in China Xing Huang<sup>a,b</sup> , Xianghu Li<sup>a,c,d,*</sup> , Yani Song<sup>a,b</sup> , Zhenhe Lv<sup>a,b</sup> , Ligang Xu<sup>a,c</sup> , Dan Zhang<sup>a,c</sup> 



a _State Key Laboratory of Lake and Watershed Science for Water Security, Nanjing Institute of Geography and Limnology, Chinese Academy of Sciences, Nanjing 211135, China_ 

b _University of Chinese Academy of Sciences, Beijing 100049, China_ 

c _Poyang Lake Wetland Observation and Research Station, Nanjing Institute of Geography and Limnology, Chinese Academy of Sciences, Jiujiang 332899, China_ 

d _Lushan Floodplain Lake Wetland Observation and Research Station, Jiujiang 332899, China_ 

A R T I C L E I N F O A B S T R A C T 

_Keywords: Study region:_ China. Composite drought index _Study focus:_ The composite drought index (CDI) is crucial for monitoring and evaluating drought, XGBoost which can overcome the limitations of single indicators and provide a more comprehensive Multi-source remote sensing depiction of drought evolution. This study integrated multi-source data based on the XGBoost to Drought monitoring China construct a monthly-scale CDI at the national scale and analyzed the spatiotemporal patterns of drought in China from 2001 to 2020. 

_New hydrological insights for the region:_ The CDI showed stable performance across contrasting climatic and land-surface conditions and was able to reflect both meteorological drought signals and soil moisture stress. In representative drought events, it provided a more coherent depiction of drought evolution than single-source indices. At the national scale, the CDI revealed marked spatiotemporal heterogeneity of drought in China: drought was generally most severe in autumn, with the highest severity (1.67) and the longest duration (3.44 months), whereas spring showed the lowest drought severity (1.17). Spatially, Inner Mongolia (IM) and Northeast China (NEC) emerged as the main drought-prone regions, with persistently high severity in IM (1.57–1.99). These findings indicate that integrating multi-source drought signals within a machine-learning framework can improve national-scale drought monitoring in China and provide a stronger basis for region-specific drought-risk assessment and early warning. 

## **1. Introduction** 

Drought is a typical natural hazard with significant substantial impacts, which exerts a profound impact on agricultural production and water resource management by reducing soil moisture, constraining water supply, and suppressing vegetation growth (Yao et al., 2018; Gebrechorkos et al., 2025). In recent decades, global warming has led to a significant increase in the frequency of extreme hydroclimatic events. According to “The human cost of disasters: An overview of the last 20 years (2000–2019)” released by the United 

* Correspondence to: Nanjing Institute of Geography and Limnology, Chinese Academy of Sciences, 299 Chuangzhan Road, Nanjing 211135, China. 

_E-mail address:_ xhli@niglas.ac.cn (X. Li). 

https://doi.org/10.1016/j.ejrh.2026.103623 Received 31 October 2025; Received in revised form 4 June 2026; Accepted 5 June 2026 Available online 9 June 2026 

2214-5818/© 2026 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY-NC license ( http://creativecommons.org/licenses/by-nc/4.0/ ). 

_Journal of Hydrology: Regional Studies 66 (2026) 103623_ 

_X. Huang et al.                                                                                                                                                                                                         Journal of Hydrology: Regional Studies_ 

Nations Office for Disaster Risk Reduction (UNDRR), the number of climate-related disasters has increased by 83% compared with 1980–1999 and has continued to increase in recent decades (United Nations Office for Disaster Risk Reduction UNDRR, Centre for Research on the Epidemiology of Disasters CRED, 2020). The Intergovernmental Panel on Climate Change (IPCC) Sixth Assessment Report (AR6 WG1) also states that the frequency and intensity of heat waves and drought events have significantly increased in the past few decades, and this trend will continue to intensify under global warming scenarios (IPCC et al., 2023). In China, the occurrence of extreme drought events has significantly increased in many regions since the early 21st century (Wen and Chen, 2023). Analyses based on high-resolution multi-index datasets further indicate the expansion of drought-affected areas, faster recurrence rates, and escalating severity nationwide in China, especially in the agricultural areas of North China, Northeast China, and Northwest China (Zhang et al., 2025). Therefore, timely and accurate monitoring of drought conditions is essential for early warning and risk management of water resources and agricultural production (van Ginkel and Biradar, 2021). 

In general, drought can be classified into meteorological drought, hydrological drought, agricultural drought, and socio-economic drought based on water shortage conditions (Ding et al., 2021). To quantify the characteristics of drought, multiple types of drought indicators have been developed, and they can be roughly divided into two categories according to data sources and application contexts: ground-station-based drought indices and remote sensing-based drought indices. Among ground-based drought indices, the Standardized Precipitation Index (SPI) (McKee et al., 1993), the Palmer Drought Severity Index (PDSI) (Palmer, 1965), and the Standardized Precipitation-Evapotranspiration Index (SPEI) (Vicente-Serrano et al., 2010) are commonly used to reflect the state of meteorological drought. Although these indices can effectively reflect the drought conditions in specific locations, they are limited by the sparse or uneven distribution of stations and may not fully characterize the detailed spatial pattern of regional-scale drought (Pei et al., 2023). On the other hand, satellite-based remote sensing enables continuous and large-scale environmental observations, providing a promising technological approach for regional scale drought monitoring (Feng et al., 2023). Researchers have developed various remote sensing indices to monitor meteorological or agricultural droughts based on different remote sensing data, including the Normalized Difference Vegetation Index (NDVI) (Rouse et al., 1974), the Vegetation Health Index (VHI) (Kogan, 1997), and the Temperature-Vegetation Drought Index (TVDI) (Sandholt et al., 2002). Due to their wide coverage and continuous data availability, remote sensing indices are essential for analyzing the spatial characteristics of droughts (Zhao et al., 2022). 

However, indices based on single stations or single remote-sensing features usually depend mainly on one or two variables and therefore focus only on specific types of drought processes. With the shift in drought monitoring from “single-dimension identification” to “multi-process and integrated evaluation”, composite or multi-variable indicators have received increasing attention. Composite drought indicators achieve a more comprehensive characterization of drought processes by integrating multiple sources of data and fusing multidimensional drought signals. For example, the Multivariate Standardized Drought Index (MSDI) based on variables such as precipitation and soil moisture proposed by Hao and AghaKouchak (2014) performed better in identifying drought occurrence, duration, and spatial coverage. The short-term and long-term composite drought index developed by the National Drought Mitigation Center (NDMC) of the United States integrated SPI, SPEI, soil moisture, vegetation status, and snow-water equivalent, and provided weekly regional drought assessments. In the Middle East and North Africa, government departments and academic institutions have jointly established a monthly Composite Drought Indicator which considered precipitation, vegetation condition, soil moisture, and evapotranspiration to improve services for agricultural drought warning and ecological drought response (Bergaoui et al., 2024). However, many existing composite drought indices rely heavily on statistical methods such as principal component analysis, multiple linear regression, or copula-based formulations. Due to the nonlinear characteristics of drought development, these methods may be difficult to fully capture the complex interactions of multiple factors (Zhang et al., 2023; Kim et al., 2020; Wei et al., 2023). 

In recent years, machine learning has been broadly used in drought monitoring for its ability to capture nonlinear relationships and achieve robust predictive performance in diverse scenarios. Methods such as decision trees (e.g., Classification and Regression Tree, CART), generalized linear models (GLM), artificial neural networks (e.g., Backpropagation Artificial Neural Network, BP-ANN), Random Forests (RF), Convolutional Neural Networks (CNN), and gradient-boosting methods (e.g., Extreme Gradient Boosting, XGBoost) have shown promising performance in drought monitoring and prediction (Li et al., 2023; Tugrul, Hinis, 2025; Sundararajan ˘ et al., 2021; Oyounalsoud et al., 2024). For example, Liu et al. (2020) proposed an integrated agricultural drought index based on neural networks, which indicated that machine learning can strengthen the fusion of multi-source indicators and enhance drought characterization in agricultural systems. Xiao et al. (2024) developed a hybrid CNN–RF framework for agricultural drought monitoring using multi-source data, showing that convolution-based feature extraction can help reproduce the temporal and spatial patterns of drought more accurately. In parallel, machine learning has increasingly been used to reconstruct and downscale GRACE-derived terrestrial water storage and groundwater anomalies, highlighting that machine learning can also recover hydrologically meaningful drought signals from coarse-resolution Earth observation data (Sun et al., 2021; Shilengwe et al., 2024). Among existing machine-learning approaches, XGBoost has shown consistently strong potential for drought monitoring and forecasting because it can capture nonlinear relationships among multiple hydroclimatic and land-surface variables while remaining computationally efficient and relatively interpretable. Existing studies provide converging evidence for this advantage. For example, Zhang et al. (2019) developed a XGBoost-based drought forecasting framework using multiple meteorological variables in Shaanxi Province and showed that accounting for nonlinear and lagged effects improved SPEI prediction across 1–6 month lead times. Similarly, Zubair et al. (2025) proposed a hybrid modeling framework that integrated MODIS-derived indicators, showing that XGBoost can effectively learn from heterogeneous and multi-scale drought-related signals. In addition, Li et al. (2025) applied XGBoost to predict hydrological drought in the Huaihe River Basin using different feature sets, and demonstrating its suitability for drought problems in which dominant controls vary across both space and time. 

China is one of the regions most frequently affected by drought. Owing to its diverse climate regimes, complex topography, heterogeneous land cover, and strong monsoon influence, drought in China exhibits pronounced spatiotemporal heterogeneity, which 

2 

_Journal of Hydrology: Regional Studies 66 (2026) 103623_ 

_X. Huang et al._ 

poses a major challenge for effective monitoring (Peel et al., 2007; Zhao et al., 2017). Previous national-scale studies have advanced the understanding of drought in China from the perspectives of historical evolution, regional characteristics, and data support (Zou et al., 2005; Xia et al., 2018; Zhang et al., 2023). However, operational drought monitoring still relies largely on single meteorological indices, such as SPI, SPEI, and PDSI, which are less able to represent the coupled responses of water availability, energy conditions, vegetation activity, and soil moisture. Although multisource remote sensing and machine-learning approaches have been increasingly applied in drought research, many existing studies in China remain focused on specific regions or particular monitoring settings. A national-scale machine-learning framework that integrates multi-source remote sensing information into a unified composite drought index for China’s diverse climate and land-surface conditions remains limited. Therefore, it is necessary to develop a national-scale drought monitoring framework that integrates station-based drought information with multi-source remote sensing variables and is capable of capturing the complex relationships among climatic and land-surface factors across China. 

Against this background, this study developed a XGBoost-based composite drought index for China using multi-source remote sensing and reanalysis data. The objectives and main novelties of this study are as follows: (1) to develop a monthly composite drought index (CDI) for China by integrating 11 drought-related variables within an XGBoost framework and to evaluate its applicability across diverse regions with contrasting climatic and land-surface conditions; (2) to examine whether the CDI can reflect not only meteorological drought signals but also soil moisture stress, through comparisons with SPI− 1, SSI− 1 and analyses of typical drought events; (3) to characterize the spatiotemporal heterogeneity of drought in China during 2001–2020 based on the CDI, with particular attention to seasonal contrasts and regional drought-risk patterns. 

The results can provide key scientific support for formulating drought mitigation and disaster risk reduction policies, ensuring food and ecological security, and improving national water resources management strategies. 

## **2. Materials and methods** 

## _2.1. Study area_ 

China’s terrain slopes downward from west to east, forming three topographic steps. The highest topographic step is the Qinghai–Tibet Plateau, where elevations commonly exceed 4000 m above sea level. The second step consists mainly of inland plateaus, basins, and uplands, whereas the third step is dominated by eastern plains and coastal lowlands. This pronounced relief creates a highly heterogeneous land surface composed of mountains, plateaus, basins, deserts, plains, lake basins, and river valleys (Wang et al., 2020). 

Consistent with its diverse topography, China also exhibits strong climatic heterogeneity. According to the Koppen climate clas-¨ sification system, the country includes several climate types, such as tropical (Af, Am), subtropical (Cfa, Cwa), temperate (Dwa, Dwb), arid and semi-arid (BWh, BSk), and alpine (ET, EF) climate types, with distinct regional contrasts (Beck et al., 2023). This climatic 



**Fig. 1.** Geographic location of the seven natural sub-regions of China. 

3 

_Journal of Hydrology: Regional Studies 66 (2026) 103623_ 

_X. Huang et al.                                                                                                                                                                                                         Journal of Hydrology: Regional Studies_ 

pattern produces a pronounced precipitation gradient, with generally drier conditions in the west and wetter conditions in the east. For example, Northwest China is dominated by arid and semi-arid environments, and much of the region receives less than 200 mm of mean annual precipitation, whereas southeastern China is comparatively humid, with annual precipitation commonly reaching 1500–2000 mm. In addition, under the influence of the East Asian Summer Monsoon, precipitation is strongly concentrated in the rainy season. From May to September, approximately 40%–50% of the annual precipitation falls in South China, whereas about 60%– 70% falls in North China (Guo et al., 2020; Katzenberger and Levermann, 2024). 

To account for the large spatial heterogeneity of climate and land-surface conditions across China, this study divided China into seven sub-regions based on the regionalization scheme of Zhao (1983) and further considering climatic differences among regions, namely Central–South China (CSC), Inner Mongolia (IM), North China (NC), Northeast China (NEC), Northwest China (NWC), South China (SC), and Qinghai–Tibet Plateau (QTP) (Fig. 1). 

## _2.1.1. Data sources_ 

In this study, remote sensing and reanalysis datasets were integrated to construct the composite drought index (CDI). The datasets covered the period from 2001 to 2020 and included seven primary categories: surface temperature, evapotranspiration, precipitation, vegetation, soil moisture, elevation, and land cover. Detailed information on the datasets, including spatial resolution, temporal resolution, and source, is provided in Table 1. 

As this study aimed to develop the CDI at a monthly time scale, 1-month Standardized Precipitation–Evapotranspiration Index (SPEI− 1) was selected as the target variable for the XGBoost model. SPEI was adopted as the training target because it is a standardized meteorological drought index based on the climatic water balance and therefore provides a physically interpretable reference for drought conditions. Compared with precipitation-only indices, SPEI incorporates atmospheric evaporative demand and is thus more suitable for representing moisture deficits under varying thermal conditions (Vicente-Serrano et al., 2010; Beguería et al., 2014). The target data were obtained from the HSPEI dataset (https://doi.org/10.57760/sciencedb.ecodb.00090), a high-resolution monthly drought dataset for mainland China from 2001 to 2022, in which SPEI was calculated following the original formulation proposed by Vicente-Serrano et al. (2010) and then spatialized to 1-km grids using a random forest regression framework (Xia et al., 2024). The source study reported good agreement between HSPEI and station-based SPEI in both cross-validation and site-level comparisons, which indicates that this dataset is suitable for representing the spatial heterogeneity of meteorological drought across China at the monthly scale. In this study, SPEI− 1 served as the monthly meteorological reference for model training, while the predictor variables provided complementary information on drought-related conditions from multiple perspectives, including climatic water and energy conditions, vegetation status, soil moisture, and land-surface characteristics. Accordingly, the resulting CDI should be interpreted as a monthly-scale, hybrid, multi-source composite drought index trained using SPEI− 1 as the target variable. 

## _2.1.2. Predictor selection, feature importance analysis, and multicollinearity assessment_ 

To construct the composite drought index (CDI), 11 predictor variables were selected, including the Precipitation Condition Index (PCI), Vegetation Condition Index (VCI), Temperature Condition Index (TCI), Normalized Difference Vegetation Index (NDVI), Leaf Area Index (LAI), SIFCI (Solar-Induced Chlorophyll Fluorescence Condition Index), Soil Moisture Condition Index (SMCI), Crop Water Stress Index (CWSI), Temperature Vegetation Dryness Index (TVDI), z-score-normalized Digital Elevation Model (NDEMZ), and Land Cover (LC). The predictor set was designed to capture the main processes involved in drought development across the atmosphere–soil–vegetation continuum. Specifically, PCI was used to characterize precipitation deficits, SMCI to reflect soil water limitation, 

**Table 1** 

Dataset information and sources. 

|Variable type|Variable|Dataset|Spatial<br>resolution|Temporal<br>resolution|Source|
|---|---|---|---|---|---|
|Land Surface Temperature|LST|MOD11C3v061|0.05<sup>◦</sup>|1-month|https://lpdaac.usgs.gov/products/mod11c3v061/|
|Evapotranspiration|PET|ERA5-Land monthly|0.1<sup>◦</sup>|1-month|https://cds.climate.copernicus.eu/|
||ET|averaged data from 1950<br>to present|0.1<sup>◦</sup>|1-month||
|Precipitation|Precipitation|CHIRPSv3.0|0.05<sup>◦</sup>|1-month|https://data.chc.ucsb.edu/products/CHIRPS/v3.<br>0/|
|Vegetation|NDVI|MODIS/006/MOD13Q1|250 m|16-day|https://developers.google.com/earth-engine/<br>datasets/catalog/MODIS_061_MOD13Q1/|
||LAI|GLASS|0.05<sup>◦</sup>|8. day|https://glass.hku.hk/|
||SIF|GOSIF|0.05<sup>◦</sup>|1-month|https://globalecology.unh.edu/data/GOSIF.html|
|Soil Moisture|Soil|NASA/GLDAS/V021/|0.25<sup>◦</sup>|3-hour|https://developers.google.com/earth-engine/|
||Moisture|NOAH/G025/T3H|||datasets/catalog/NASA_GLDAS_V021_NOAH_<br>G025_T3H|
|Land Cover Type|Land Cover|MODIS/006/MCD12Q1|500 m|1-year|https://developers.google.com/earth-engine/<br>datasets/catalog/MODIS_061_MCD12Q1/|
|Elevation|DEM|USGS/SRTMGL1_003|30 m|—|https://developers.google.com/earth-engine/<br>datasets/catalog/USGS_SRTMGL1_003/|
|Standardized Precipitation<br>Evapotranspiration<br>Index|SPEI|HSPEI|1000 m|1-month|https://www.scidb.cn/en/detail?<br>dataSetId=968592537239420928|



4 

_Journal of Hydrology: Regional Studies 66 (2026) 103623_ 

TCI, CWSI, and TVDI to capture thermal stress and land-surface dryness, NDVI, VCI, LAI, and SIFCI to describe vegetation greenness, relative stress, canopy structure, and photosynthetic activity, respectively, with LC and NDEMZ to account for spatial heterogeneity associated with land cover and topographic settings (Ji and Peters, 2003; Kogan, 1995; Jackson et al., 1981; Sandholt et al., 2002; Wang et al., 2023; Xiao et al., 2023; Sang et al., 2024). This design is consistent with the view that drought is a multivariate process and is more reliably characterized when hydroclimatic, vegetation-related, and environmental controls are considered together rather than separately. 

To assess the relative role of each predictor in the fitted XGBoost models, we conducted a feature importance analysis based on the gain metric. Gain-based importance represents the relative contribution of each predictor to model split gains, providing a basis for comparing the model-based contributions of different drought-related predictors across sub-regions. The results showed regional differences in feature importance, with SMCI showing the highest importance in CSC (26.88%) and SC (34.05%), TCI in IM (26.73%), NEC (22.12%), NWC (24.20%), and QTP (39.91%), and PCI in NC (22.66%), while the remaining predictors generally importance values ranged from about 4–10% across subregions. The high importance of SMCI in CSC and SC may indicate that, in humid and vegetation-rich southern regions, drought stress is strongly expressed through soil water limitation after precipitation deficits develop. This pattern may be related to the ability of soil moisture to integrate the combined effects of precipitation shortage, evapotranspiration, and land-surface water storage, and can therefore capture the persistence of drought conditions. The relatively large contribution of PCI in NC suggests that direct precipitation deficits remain an important signal of drought variability in this monsooninfluenced agricultural region. In IM, NEC, NWC, and especially QTP, the high importance of TCI may indicate that thermal conditions are closely related to drought variability in northern, northwestern, and high-elevation regions. In relatively dry or cold environments, temperature anomalies can affect evaporative demand, surface energy balance, vegetation activity, and water availability associated with snow and frozen ground. This mechanism is particularly relevant to the QTP, where the high elevation and cold climatic background climate may increase the sensitivity of drought processes to land-surface temperature and energy availability. These results suggest that the selected predictors provided complementary, rather than redundant, information for CDI construction. 

To examine whether multicollinearity among predictors affected model stability, a Pearson correlation analysis and a reducedpredictor model comparison were conducted. DEM and LC were excluded from the correlation analysis because DEM is static and LC is categorical. The Pearson correlation analysis (Fig. 2) showed that most predictor pairs had weak to moderate correlations. The strongest correlation was observed between NDVI and LAI (r = 0.87), indicating partial overlap between vegetation greenness and canopy-structure information. In contrast, the correlations among other vegetation-related predictors were lower, such as those between VCI and SIFCI (r = 0.38), NDVI and VCI (r = 0.26), and LAI and VCI (r = 0.13). The thermal-stress-related variables also showed relatively weak pairwise correlations, with Pearson r values of 0.26 between CWSI and TVDI, − 0.25 between TVDI and TCI, and − 0.14 between CWSI and TCI. These results suggest that the main potential redundancy was concentrated in the NDVI–LAI pair. Within this 



**Fig. 2.** Pearson correlation matrix among the predictors used in the XGBoost model. The coefficients were calculated using spatiotemporally matched monthly raster samples from 2001 to 2020. The * indicates that the correlation coefficient (r) has a P-value less than 0.01. 

5 

_Journal of Hydrology: Regional Studies 66 (2026) 103623_ 

_X. Huang et al.                                                                                                                                                                                                         Journal of Hydrology: Regional Studies_ 

pair, LAI showed slightly higher, or at least comparable, gain-based importance than NDVI across most sub-regions. Therefore, LAI was retained as the representative variable from this correlated pair, and a reduced-predictor model excluding NDVI was constructed for comparison with the model using the full predictor set. Compared with the full-predictor model, the NDVI-excluded model showed slightly lower validation-set performance, with a relative EVS decrease of 0.19%–1.24% and relative increases in RMSE and MAE of 0.29%–2.58% and 0.08%–2.54%, respectively. These results suggest that the identified predictor correlation had only a limited influence on model stability. Considering the small but consistent performance advantage of the full-predictor model and the spatial variation in gain-based feature importance indicating complementary contributions rather than simple redundancy, the full set of 11 predictors was retained for CDI construction. 

## _2.1.3. Data processing_ 

The subsequent data processing was mainly carried out using ArcGIS 10.8, PyCharm, and the GEE cloud platform (https:// earthengine.google.com/). Before model construction, all raster datasets were projected to the WGS84 geographic coordinate system (EPSG:4326). Coarser-resolution datasets were resampled to 0.05<sup>◦</sup> using the nearest-neighbor method, and all raster datasets were then aligned to the same grid using a reprojection-based grid-matching procedure. Invalid values were removed, and missing values were filled using nearest-neighbour interpolation based on the Euclidean Distance Transform (EDT). TCI and SIFCI were calculated from LST and SIF data, respectively. NDVI images affected by significant cloud cover were discarded, and monthly mean composites were generated; these monthly NDVI composites were then used to calculate VCI and the TVDI. To reduce the influence of outliers, the minimum and maximum values used in the calculations of VCI, TCI, TVDI, and SIFCI were defined as the 5th and 95th percentiles, respectively. The LAI and Soil Moisture (SM) datasets were also aggregated to monthly means. In addition, the SMCI was calculated from monthly SM data and the digital elevation model (DEM) was z-score normalized. 

To evaluate the ability of the CDI to reflect meteorological drought conditions and soil moisture stress, correlation analyses were conducted between the CDI and two additional drought indicators, namely the 1-month Standardized Precipitation Index (SPI− 1) and 

**Table 2** 

Variables and formula. 

|Variable|Formula|Notes|Reference|
|---|---|---|---|
|Precipitation Condition<br>Index (PCI)|_PCI_ =<br>precip−precipmin<br>precipmax −precipmin|precipminand precipmaxare the minimum and<br>maximum precipitation in the same month over<br>multiple years, respectively; smaller PCI indicates<br>drier conditions.|(Rhee et al., 2010; Wang<br>et al., 2019)|
|Temperature Condition<br>Index (TCI)|_TCI_ =<br>_LST_max −_LST_<br>_LST_max −_LST_min<br>× 100|_LST_maxand_LST_minare the maximum and minimum<br>values of LST; lower TCI implies stronger drought<br>stress.|(Kogan, 1995; Wan et al.,<br>2004; Zhao et al., 2021)|
|Vegetation Condition<br>Index (VCI)|_VCI_ =<br>_NDVI_−_NDVI_min<br>_NDVI_max −_NDVI_min<br>× 100|_NDVI_minand_NDVI_maxare the minimum and<br>maximum values of NDVI, respectively; lower VCI<br>indicates more severe drought.|(Kogan, 1995; Quiring and<br>Ganesh, 2010; Liang et al.,<br>2017; Cao et al., 2022)|
|Soil Moisture Condition<br>Index (SMCI)|_SMCI_ =<br>_SM_−_SM_min<br>_SM_max −_SM_min<br>×100|_SM_minand_SM_maxare the minimum and maximum<br>values of SM, respectively; lower SMCI indicates<br>drier soil.|(Cao et al., 2022; Zhang<br>and Jia, 2013; Inocˆencio<br>et al., 2020)|
|Crop Water Stress Index<br>(CWSI)|_CWSI_ =1 −<br>_ET_<br>_PET_|_ET_and PET are the actual evapotranspiration and the<br>potential evapotranspiration, respectively; larger<br>CWSI indicates stronger crop water stress.|(Jackson et al., 1981; Bai<br>et al., 2017; Ma et al.,<br>2021)|
|Temperature Vegetation|TVDI<br>_T_−_T_min|T: land-surface temperature (LST); Tminand_T_maxare|(Bai et al., 2017; Liu and|
|Dryness Index<br>(TVDI)|=<br>_T_max−_T_min<br>_T_max = _a_1·_N_DVI + _b_1<br>_T_min =_a_2·_N_DVI +_b_2|the wet edge and the dry edge, respectively;_a_1,_b_1,<br>_a_2,_b_2: regression coefficients.|Yue, 2018; Zhao et al.,<br>2021)|
|Solar-Induced|_SIFCI_<br>_SIF_−SIFmin|SIFmin_and_SIFmaxare the minimum and maximum|Same calculation form as|
|Chlorophyll<br>Fluorescence<br>Condition Index<br>(SIFCI)|=<br>SIFmax −SIFmin|values of SIF, respectively; smaller values indicate<br>stronger potential drought stress.|VCI (Kogan, 1995; Quiring<br>and Ganesh, 2010; Liang<br>et al., 2017; Cao et al.,<br>2022)|
|z-score-<br>normalizedDigital<br>Elevation Model<br>(NDEMz)|_NDEMZ_ =<br>_DEM_−μDEM<br>σDEM|μDEMandσDEMare mean and standard deviation<br>within the computation domain.<br>i|z-score normalization|
|Standardized<br>Precipitation Index<br>(SPI)|_q_ =<br>_m_<br>_n_<sup>~~，~~</sup><sup>_G_(</sup><sup>_x_) =</sup><br>∫_x_<br>0<br>1<br>_β_<sup>_γ_</sup>Γ(_γ_)<sup>_~~t~~γ_−1</sup><sup>_e_−</sup><sup>_t/βdt_， </sup><br>_H_(_x_) = _q_ + (1−_q_)_G_(_x_),<br>_If H_(_x_) ≤0_._5，_T_=<br>−2ln_H_(_x_)<br>√<br>_, S_= −1<br>_If H_(_x_)_>_0_._5，_T_=<br>−2ln(1−_H_(_x_))<br>√<br>_, S_=1<br>SPI = _S_[_T_ −<br>_c_0+_c_1_T_+_c_2_T_<sup>2</sup><br>1+_d_1_T_+_d_2_T_<sup>2 </sup>+_d_3_T_<sup>3</sup><sup>~~]~~</sup>|cumulative precipitation was fitted using the Gamma<br>distribution (parameters_β_and_γ_obtained via<br>maximum likelihood estimation), with zero-<br>precipitation correction to derive the cumulative<br>probability_H_(_x_); SPI was then calculated using the<br>standard normal quantile<br>function;_c_0、_c_1、_c_2、_d_1、_d_2、_d_3are constants.|National Standard GB/T<br>20481–2017 (China)|
|Standardized Soil<br>Moisture Index (SSI)|<br>_SSI_y_,_m =<br>_SMy,m_−μ_m_<br>σ_m_|_SSI_y_,_mis the monthly soil moisture in year y and<br>month_m_, and_μm _and_σm _are the multi-year mean and<br>standard deviation of soil moisture for the<br>corresponding calendar month.|Xu et al., (2018);<br>Palagiri and Pal, (2024)|



6 

_Journal of Hydrology: Regional Studies 66 (2026) 103623_ 

the 1-month Standardized Soil Moisture Index (SSI− 1). SPI− 1 was used to assess whether the CDI could reflect short-term meteorological drought conditions, whereas SSI− 1 was used to examine whether the CDI could also reflect soil moisture stress (World Meteorological Organization et al., 2012; Hoylman et al., 2024). 

SPI− 1 was calculated using 75 years of precipitation datasets from January 1950 to December 2024, which were derived from the ERA5-Land monthly averaged data (https://cds.climate.copernicus.eu/). SSI− 1 was calculated from the GLDAS-Noah 0.25<sup>◦</sup> 3-hourly soil moisture product (https://developers.google.com/earth-engine/datasets/catalog/NASA_GLDAS_V021_NOAH_G025_T3H) for 2001–2020, corresponding to the study period. The 3-hourly soil moisture data were first aggregated to monthly values, and SSI− 1 was then derived from the monthly soil moisture series. The equations used for SPI− 1 and SSI− 1 are provided in Table 2. 

## _2.2. Methods_ 

The methodology used in this study is summarized in Fig. 3 and is as follows: (1) multi-source drought-related datasets were collected and preprocessed through projection harmonization, pixel alignment, missing-value filling, and monthly aggregation. (2) the processed datasets were organized into target, predictor, and validation variables for CDI construction and evaluation. (3) the monthly-scale CDI was constructed by training an XGBoost model using the target variable and predictor variables. (4) the trained model was evaluated using an independent validation set to assess model performance. (5) the resulting CDI was further compared with independent drought indicators to evaluate its consistency with meteorological and soil-moisture-related drought signals. (6) Finally, the validated CDI was applied to generate drought monitoring results and analyze the spatiotemporal evolution of drought in China. 

## _2.2.1. XGBoost model construction_ 

The XGBoost algorithm, proposed by Chen and Guestrin (2016), is a boosting-based ensemble learning algorithm that iteratively adds weak learners to minimize a regularized objective. It extends gradient boosting decision trees (GBDT) by optimizing a second-order Taylor approximation of the loss and by introducing explicit regularization on tree complexity, which improves both model fitting ability and generalization ability. The specific formulation is provided as follows (Han et al., 2019; Li, Zhu, 2020; Li et al., 2023): 



**Fig. 3.** Schematic workflow of the monthly-scale CDI construction, validation, and application. 

7 

_X. Huang et al.                                                                                                                                                                                                         Journal of Hydrology: Regional Studies 66 (2026) 103623_ 

Given a training set D = {( _x_ 1 _, y_ 1) _,_ ( _x_ 2 _, y_ 2) _,_ … _,_ ( _xn, yn_ )} _, xi_ ∈ _X_ ⊆ _R_<sup>_m_</sup> _, yi_ ∈ _Y_ ⊆ _R_ (with X as the input space and Y as the output space), XGBoost can be expressed as： 



Where ̂ y _i_ denotes the predicted value of the trained model, _fk_ represents the _k_ -th sub-model (i.e., the _k_ -th regression tree) in the ensemble model, and _xi_ is the feature data of the _i_ -th input sample. The optimization objective of the XGBoost algorithm includes a loss function and a regularization term, with the final optimization objective defined as： 



Where L( _t_ ) is the objective function at the _t_ -th iteration； _yi_ is the class label of the original sample；̂y _i_ ( _t_ − 1) represents the predicted value of the model during t− 1 model iterations of the sample； _ft_ ( _xi_ ) represents the predicted value of the model during the tth model iteration of the sample; and H( _ft_ ) is the regularization term of the objective function. The Taylor expansion of Eq. (2) yields： 



Where _gi_ represents the first-order gradient of the sample _xi_ ; _hi_ represents the second-order gradient of the sample _xi_ ; ω _j_ is the output value of the _j_ -th node；T is the total number of leaf nodes in the tree; λ and γ are coefficients of the regularization term, used to suppress model overfitting；and _Ij_ is the subset of samples in the _j_ -th leaf node. The training process of the XGBoost model solves Eq. (3) to find the optimal ω<sup>∗</sup> _j_<sup>and the corresponding optimal solution of the</sup> objective function: 



Eq. (5) was used to evaluate the quality of a tree structure, the lower the value, the better the tree structure. Therefore, when the nodes in the tree were split, Eq. (6) was obtained as follows: 



Gain = _Lleft_ + _Lright_ − _Lfather_ (6) 

If the gain value is greater than zero, the node splitting continues; otherwise, the node splitting stops. 

To construct the XGBoost model, PCI, TCI, VCI, NDVI, LAI, SIFCI, SMCI, CWSI, TVDI, NDEMZ, and LC were used as predictor variables, with SPEI− 1 as the target variable. The modeling process was implemented using the XGBRegressor from the xgboost package (version 2.1.4) in Python, and the procedures were as follows: 

- (1) The processed data were divided into seven sub-regional datasets. The spatiotemporal features of each pixel were converted into one-dimensional feature vectors and matched with the target variable (SPEI− 1). Each dataset was randomly split into training (80%) and validation (20%) subsets to assess out-of-sample performance. A hold-out validation strategy, in which the training subset was used for model fitting and the validation subset was used for hyperparameter tuning and performance evaluation, was applied within each sub-region. This strategy was adopted because the XGBoost models were constructed separately for the seven sub-regions to account for broad climatic and land-surface heterogeneity, and the 80/20 training–validation split provided a transparent and consistent way to assess the predictive performance of each sub-regional model. 

- (2) The XGBoost regression model was tuned by focusing on several key hyperparameters, including the number of boosting rounds (n_estimators), learning rate (eta), maximum tree depth (max_depth), column subsampling ratio per tree (colsample_bytree), and minimum child weight (min_child_weight). These hyperparameters were tuned sequentially based on validation-set performance, and early stopping with a patience of 50 rounds was used to reduce overfitting. Given the relatively small learning rate (eta = 0.01), a wider range of boosting rounds was evaluated during tuning. When the number of boosting rounds reached 1200, validation MAE and RMSE showed only marginal improvement; therefore, 1200 was retained as the final setting. The remaining hyperparameters were tuned using the same validation-based procedure: the subsample was set to 1 (ψ=1), indicating that all training samples were used in each boosting round; and L2 regularization was applied with λ= 1 to penalize large leaf weights by applying a squared penalty. The remaining hyperparameters were tuned based on the model performance as follows: the maximum tree depth _d_ max= 16, the learning rate η= 0.01, the column subsample ratio _rcol_ = 0.5, and the minimum leaf node weight _C_ min= 2. 

- (3) Model predictive performance was quantified through root mean squared error (RMSE), mean absolute error (MAE), and explained variance score (EVS). The formulas for these three metrics are as follows: 

8 

_X. Huang et al.                                                                                                                                                                                                         Journal of Hydrology: Regional Studies 66 (2026) 103623_ 

|RMSE=<br>1<br>_n_<br>∑<br>_n_<br>_i_=1<br>(_yi_−̂ _yi_)<sup>2</sup><br>√|(7)|
|---|---|
|MAE=<br>1<br>_n_<br>∑_n_<br>_i_=1<sup>|</sup><sup>_yi_ −̂</sup> <sup>_yi_|</sup>|(8)|
|EVS=1−<br>∑_n_<br>_i_=1<sup>(</sup><sup>_yi_ −̂</sup> <sup>_y_</sup>_i_<sup>)</sup><br>2<br>~~∑~~_n_<br>_i_=1<sup>(</sup><sup>_yi_ −</sup><br>_~~y~~_)<br>2|(9)|



Where _yi_ denotes the observed value, ̂ _yi_ the predicted value, and _~~y~~_ the observational mean. When the predictions are perfectly consistent with the observations, EVS is close to 1, while RMSE and MAE decrease asymptotically to zero as the accuracy increases. 

## _2.2.2. Drought classification_ 

Considering the marked climatic heterogeneity among the seven sub-regions, both CDI and SPEI− 1 were fitted separately for each sub-region with both normal and log-normal distributions, and the better-fitting distribution was selected according to the Kolmogorov–Smirnov (KS) statistic. The corresponding KS statistics and selected distributions are summarized in Table 3. Based on the threshold percentile method used in the United States Drought Monitor (Svoboda et al., 2002), and to facilitate clearer interpretation and more consistent comparison across sub-regions while still capturing the main gradient from normal conditions to increasing drought severity. Appropriate adjustments were made to define drought thresholds at the 30th, 15th, and 5th percentiles of the fitted distribution. These percentiles correspond to drought grades of D0 (no drought), D1 (mild drought), and D2 (severe drought), respectively, and details are shown in Table 4. 

## _2.2.3. Evaluation of CDI and run-theory-drought detection_ 

In this study, the applicability of the CDI in drought monitoring was evaluated by comparing the classification performance between the CDI and SPI− 1 in four metrics (recall, accuracy, precision, and F1-score) for drought classification. Recall reflects the ability of an index to detect actual drought events (the proportion of actual drought events that are correctly identified). Accuracy measures the overall correctness of the classification (the proportion of correct predictions among all events). Precision represents the proportion of actual drought events among all drought predictions. The F1-score is defined as the harmonic mean of precision and recall, enabling a balanced evaluation of these two metrics. 

In this study, a drought event was defined as an event in which CDI remains below the D0 threshold for at least three consecutive months based on run theory (Abu Arra and S¸is¸man, 2023). The characteristics of drought were then extracted from the CDI, including severity (cumulative deviation from normal), intensity (average severity per unit time), duration (event length), and frequency (event count). 

## **3. Results** 

## _3.1. XGBoost model performance_ 

The model performance across the seven sub-regions in the training and validation sets is shown in Figs. 4 and 5. The correlations between CDI and SPEI− 1 were highly significant (p _<_ 0.01) in all sub-regions. The EVS ranged from 0.63 to 0.89 in the training sets and from 0.54 to 0.82 in the validation sets, indicating that the model reproduced the monthly variations in SPEI− 1 reasonably well at the regional scale. 

Clear regional differences in model performance were observed. IM, NC, and NEC showed comparatively higher predictive performance. IM achieved the highest EVS in both the training (0.89) and validation (0.82) sets, with RMSE values of 0.31 and 0.39 and MAE values of 0.23 and 0.29, respectively. NEC followed closely, with EVS values of 0.88 and 0.81 in the training and validation sets, respectively, together with RMSE values of 0.33 and 0.40 and MAE values of 0.24 and 0.30. NC showed a similar pattern, with EVS values of 0.85 and 0.75, RMSE values of 0.35 and 0.45, and MAE values of 0.26 and 0.35 in the training and validation sets, respectively. This pattern suggests that the selected predictors were more closely aligned with SPEI− 1 in these sub-regions, resulting in 

**Table 3** 

KS statistics and selected distributions of CDI and SPEI− 1 in the seven sub-regions. 

|Sub-region|CDI|||SPEI−1|||
|---|---|---|---|---|---|---|
||Normal (KS)|Log-normal (KS)|Selected distribution|Normal (KS)|Log-normal (KS)|Selected distribution|
|CSC|0.0097|0.0536|Normal|0.0239|0.0526|Normal|
|IM|0.0265|0.0235|Log-normal|0.0267|0.0408|Normal|
|NC|0.0207|0.0395|Normal|0.0269|0.0526|Normal|
|NEC|0.0128|0.0323|Normal|0.0263|0.0458|Normal|
|NWC|0.0433|0.012|Log-normal|0.0428|0.0294|Log-normal|
|SC|0.0065|0.0496|Normal|0.0246|0.0595|Normal|
|QTP|0.0075|0.0468|Normal|0.0136|0.0533|Normal|



9 

_Journal of Hydrology: Regional Studies 66 (2026) 103623_ 

**Table 4** 

Drought grades for CDI and SPEI− 1 in different sub-regions. 

|Sub-region|CDI|||SPEI−1|||
|---|---|---|---|---|---|---|
||D0|D1|D2|D0|D1|D2|
|CSC|≥−0.361|−0.687~−0.361|_<_−0.687|≥−0.486|−0.935~−0.486|_<_−0.935|
|IM|≥−0.547|−0.890~−0.547|_<_−0.890|≥−0.530|−1.000~−0.530|_<_−1.000|
|NC|≥−0.422|−0.808~−0.422|_<_−0.808|≥−0.503|−0.969~−0.503|_<_−0.969|
|NEC|≥−0.423|−0.831~−0.423|_<_−0.831|≥−0.492|−0.966~−0.492|_<_−0.966|
|NWC|≥−0.439|−0.697~−0.439|_<_−0.697|≥−0.593|−0.926~−0.593|_<_−0.926|
|SC|≥−0.376|−0.714~−0.376|_<_−0.714|≥−0.484|−0.927~−0.484|_<_−0.927|
|QTP|≥−0.367|−0.658~−0.367|_<_−0.658|≥−0.494|−0.909~−0.494|_<_−0.909|





**Fig. 4.** Scatter density plot of simulated CDI versus observed SPEI− 1 for training-set performance of the XGBoost model across seven sub-regions of China. (a). CSC; (b). IM; (c). NC; (d). NEC; (e). NWC; (f). SC; (g). QTP. The color density indicates the concentration of training samples and is used to assess the model fitting performance within the calibration dataset. Note: “**” indicates P _<_ 0.01 (two-tailed). 

better CDI performance. By contrast, QTP showed the lowest EVS, with values of 0.63 in the training set and 0.54 in the validation set, together with RMSE values of 0.49 and 0.55 and MAE values of 0.39 and 0.44, respectively. This weaker performance may be related to the strong topographic heterogeneity and more complex land-surface conditions in the plateau region, which can reduce the stability of the relationship between predictors and the target variable. The feature-importance results further supported this interpretation. TCI showed the highest gain-based importance in QTP, accounting for 39.91% of the total importance, whereas vegetation-related predictors, including LAI, NDVI, VCI, and SIFCI, each contributed less than 6%. This pattern suggests that the QTP model relied more strongly on thermal conditions, whereas vegetation-related predictors were less influential. In cold and high-altitude environments, vegetation indices may be less sensitive to drought during non-growing or snow-affected periods. Meanwhile, thermal predictors, such as TCI and TVDI, may not be directly interpretable as drought-stress signals in QTP, because land-surface temperature can also be affected by elevation, slope aspect, snow/ice cover, surface heterogeneity, and freeze–thaw processes. CSC, NWC, and SC exhibited intermediate performance, with validation EVS values of 0.60, 0.64, and 0.62, respectively, accompanied by RMSE values of 0.55, 0.50, and 0.54 and MAE values of 0.44, 0.39, and 0.43. The lower performance in CSC and SC, both located in humid monsoon regions, may be attributable to the greater complexity of moisture transfer and land-surface responses under monsoonal climatic conditions. In these areas, short-term precipitation anomalies do not always translate directly into synchronous soil-moisture and vegetation responses, because antecedent water storage and lagged land-surface feedback can buffer or delay drought development. As a result, the CDI may show weaker correspondence with SPEI− 1 than in the northern water-limited regions, thereby contributing to the relatively lower CDI–SPEI correlations observed in CSC and SC. Overall, these results suggest that, although CDI performance varied among subregions, the index remained broadly effective across contrasting environments, with regional differences mainly reflecting variations in hydroclimatic settings and land-surface processes. 

Subsequently, the CDI and SPEI− 1 were classified into drought grades (D0–D2) based on predefined thresholds, and the consistency between drought grades was evaluated for each sub-region. The consistency rates ranged from 74.50% to 83.88%, with an 

10 

_Journal of Hydrology: Regional Studies 66 (2026) 103623_ 



**Fig. 5.** Scatter density plot of simulated CDI versus observed SPEI− 1 for validation-set performance of the XGBoost model across seven sub-regions of China. (a). CSC; (b). IM; (c). NC; (d). NEC; (e). NWC; (f). SC; (g). QTP. The color density indicates the concentration of validation samples and is used to assess the out-of-sample agreement between CDI and SPEI− 1. Note: “**” indicates P _<_ 0.01 (two-tailed). 

average of 79.7%. The highest consistency rates were found in IM (83.88%) and NEC (83.65%), followed by NC (82.08%) and SC (80.50%), whereas lower values were observed in CSC (76.57%), NWC (76.69%), and QTP (74.50%). These results indicate that the CDI was able to reproduce the broad distribution of SPEI− 1-based drought categories in most sub-regions. The relatively lower agreement in several regions also suggests that threshold-based drought classification was more sensitive to regional differences than the continuous-value fitting results alone. Therefore, the grade-grade consistency results should be interpreted as evidence of generally good categorical agreement rather than exact equivalence between CDI and SPEI− 1 in all sub-regions. 



**Fig. 6.** Correlation between CDI and SPI− 1 in different sub-regions. (a). CSC; (b). IM; (c). NC; (d). NEC; (e). NWC; (f). SC; (g). QTP. The R and P values shown in each panel indicate the correlation strength and statistical significance between the two variables. The fitted regression line and correlation coefficient indicate the degree to which the CDI reflects short-term meteorological drought variability. 

11 

_Journal of Hydrology: Regional Studies 66 (2026) 103623_ 

_X. Huang et al.                                                                                                                                                                                                         Journal of Hydrology: Regional Studies_ 

To further test whether the CDI captured information beyond that contained in SPEI− 1, an additional experiment was conducted. Specifically, using SSI− 1 as the response variable, two linear regression models were compared for each sub-region: a baseline model using only SPEI− 1 as the predictor and an extended model using both SPEI− 1 and CDI as predictors. The results showed that the inclusion of CDI consistently improved model performance across all seven sub-regions. RMSE and MAE decreased by 0.057–0.165 and 0.059–0.153, respectively, whereas EVS and R² increased by 0.090–0.233 and 0.098–0.241, respectively. These results suggest that, although the CDI was developed using SPEI− 1 as the training target, it was not merely a statistical replica of SPEI− 1, but contained additional information beyond that captured by SPEI− 1 alone. 

## _3.2. Comparative evaluation of CDI, SPI_ − _1, and SSI_ − _1 for drought_ 

The correlations of CDI with SPI− 1 and SSI− 1 were calculated to evaluate the ability of CDI in representing meteorological drought and soil-moisture drought, respectively, and the results are shown in Figs. 6 and 7. The results showed that CDI was significantly and positively correlated with both SPI− 1 and SSI− 1 in all seven sub-regions (p _<_ 0.01), although the strength of the relationships varied across regions. For SPI− 1, the correlation coefficients ranged from 0.36 to 0.81, with the highest values observed in NEC (R = 0.81) and IM (R = 0.76), followed by NWC (R = 0.61) and NC (R = 0.54), whereas weaker correlations were found in QTP (R = 0.45), CSC (R = 0.37), and SC (R = 0.36). In contrast, the correlations between CDI and SSI− 1 ranged from 0.42 to 0.70, with the highest values occurring in SC (R = 0.70) and CSC (R = 0.65), followed by IM (R = 0.62), NC (R = 0.60), NEC (R = 0.58), NWC (R = 0.48), and QTP (R = 0.42). These results reveal a clear regional contrast. In the northern and relatively water-limited regions, especially NEC and NWC, CDI showed stronger agreement with SPI− 1 than with SSI− 1, suggesting that drought variability in these regions was more directly controlled by short-term meteorological forcing. By contrast, in the southern humid regions, particularly SC and CSC, CDI was more strongly correlated with SSI− 1 than with SPI− 1, and the regression slopes were also close to 1, indicating a closer correspondence between CDI and soil-moisture variability. This pattern may occur because drought development in southern China is influenced not only by precipitation deficits, but also by evapotranspiration, antecedent moisture storage, and vegetation-related surface responses. Therefore, precipitation anomalies alone may not fully capture the actual drought conditions. In QTP, CDI showed relatively weak correlations with both SPI− 1 and SSI− 1, which may reflect the influence of complex terrain, cold-region processes, and stronger spatial heterogeneity. 

CDI, SPI− 1, and SSI− 1 were then classified into drought grades, and their consistency was evaluated using accuracy, precision, recall, and F1-score. The results are presented in Tables 5 and 6. Overall, CDI showed broad agreement with both SPI− 1 and SSI− 1 across the seven sub-regions, although its agreement with SPI− 1 was generally slightly higher than that with SSI− 1. The slightly closer correspondence with SPI− 1 may be related, at least in part, to the fact that the CDI was developed using SPEI− 1 as the training target, which is more closely related to meteorological drought conditions. 

For the comparison between CDI and SPI− 1, accuracy ranged from 67.19% to 74.64%, precision from 49.36% to 59.65%, recall from 49.23% to 59.30%, and F1-score from 49.29% to 59.46%. Among the seven sub-regions, NEC showed the highest overall 



**Fig. 7.** Correlation between CDI and SSI− 1 in different sub-regions. (a). CSC; (b). IM; (c). NC; (d). NEC; (e). NWC; (f). SC; (g). QTP. The R and P values shown in each panel indicate the correlation strength and statistical significance between the two variables. The fitted regression line and correlation coefficient indicate the degree to which the CDI reflects soil-moisture-related drought variability. 

12 

_X. Huang et al.                                                                                                                                                                                                         Journal of Hydrology: Regional Studies 66 (2026) 103623_ 

**Table 5** 

Accuracy, precision, recall, and F1-Score of CDI and SPI− 1 in drought classification. 

|Subregion|Accuracy (%)|Precision (%)|Recall (%)|F1-Score (%)|
|---|---|---|---|---|
|CSC|70.54|53.54|53.66|53.59|
|IM|73.05|55.54|56.75|56.08|
|NC|72.23|56.66|55.72|56.12|
|NEC|74.64|59.65|59.30|59.46|
|NWC|68.21|49.75|50.05|49.88|
|SC|72.33|56.45|55.87|56.15|
|QTP|67.19|49.36|49.23|49.29|



**Table 6** 

Accuracy, precision, recall, and F1-Score of CDI and SSI− 1 in drought classification. 

|Subregion|Accuracy (%)|Precision (%)|Recall (%)|F1-Score (%)|
|---|---|---|---|---|
|CSC|71.24|53.43|52.78|53.00|
|IM|71.41|52.82|52.41|52.60|
|NC|67.21|51.91|51.38|51.63|
|NEC|68.17|53.44|53.72|53.54|
|NWC|63.49|45.47|45.69|45.54|
|SC|71.89|54.70|54.30|54.43|
|QTP|63.93|45.08|44.13|44.52|



consistency, while NC and SC also exhibited relatively higher precision, recall, and F1-score values. This pattern indicates that drought conditions in these regions was more directly controlled by short-term precipitation deficits, which are more explicitly represented by SPI− 1. 

For the comparison between CDI and SSI− 1, accuracy ranged from 63.49% to 71.89%, precision from 45.08% to 54.70%, recall from 44.13% to 54.30%, and F1-score from 44.52% to 54.43%. SC showed the highest overall agreement, with an accuracy of 71.89%, precision of 54.70%, recall of 54.30%, and F1-score of 54.43%, suggesting that soil-moisture anomalies in this humid region were more closely linked to rainfall deficits and atmospheric evaporative demand. By contrast, lower values were found in NWC and QTP. In NWC, accuracy, precision, recall, and F1-score were 63.49%, 45.47%, 45.69%, and 45.54%, respectively, while the corresponding values in QTP were 63.93%, 45.08%, 44.13%, and 44.52%. In these two regions, soil-moisture conditions are influenced by additional controls beyond monthly meteorological anomalies. In NWC, strong evaporative demand and snowmelt-related or runoff-related water supply can weaken the correspondence between SSI− 1 and CDI. In QTP, freeze–thaw processes, permafrost, and complex terrain alter soil-water storage and dynamics, making the soil-moisture signal less directly comparable with CDI at the monthly scale. These results suggest that the CDI was able to reproduce drought-classification patterns that were broadly consistent with both SPI− 1 and SSI− 1, while maintaining slightly closer agreement with SPI− 1 in most sub-regions. 

To further evaluate the ability of the CDI to capture the temporal evolution of drought in China, monthly time series of CDI, SPI− 1, and SSI− 1 were compared across the seven sub-regions from January 2001 to December 2020 (Fig. 8). The results showed that all three indices exhibited frequent fluctuations, and the CDI generally followed the temporal variations of both SPI− 1 and SSI− 1 in most regions. In particular, the major peaks and troughs were broadly consistent during the onset, development, and recovery stages of drought events, indicating that the CDI could reflect both meteorological drought signals and soil moisture variations. 

## _3.3. Capability of CDI for typical drought events_ 

In this section, drought events in China from 2001 to 2020 were identified based on run theory and then compared with official annual drought records issued by the Ministry of Water Resources of China and related literature, to evaluate the ability of the CDI in drought event identification. The typical drought events and their characteristics were listed in Table 7. The reported drought event descriptions used for comparison were mainly based on Liu et al. (2024), who provided an event-oriented inventory of extreme meteorological drought events over China during 1951–2022. The typical drought events in the southeastern Tibetan Plateau during 2009–2010 were additionally confirmed by the study of Ma et al. (2017). The results showed that the CDI successfully identified many typical drought events across the seven sub-regions in a manner broadly consistent with the official records and related literature. 

Accurately monitoring the spatiotemporal evolution of drought events is critical for water resource management and early disaster detection. Different drought indices exhibit notable differences in sensitivity and accuracy when capturing the development of drought. In this study, two typical cases were selected to compare the ability of CDI, SPI− 1 and SSI− 1 to reproduce the spatial development of drought: the autumn-winter consecutive drought in Southern China in 2007 (a typical drought in humid regions) and the spring-summer drought in Northeastern China in 2017 (a typical drought in semi-humid regions). 

Figs. 9 and 10 present the spatiotemporal development of the autumn-winter drought in Southern China in 2007 and the springsummer drought in Northeastern China in 2017, as represented by CDI, SPI− 1, and SSI− 1. According to disaster records, from October to December 2007, large parts of Jiangnan, South China, southeastern Southwest China, and parts of North China and Northwest China were affected by persistent drought, with the event reaching its peak intensity in November. After late December, the drought 

13 

_Journal of Hydrology: Regional Studies 66 (2026) 103623_ 



**Fig. 8.** Monthly time series curves of CDI, SPI− 1, and SSI− 1 in seven sub-regions of China (2001–2020). (a). CSC; (b). IM; (c). NC; (d). NEC; (e). NWC; (f). SC; (g). QTP. The orange-shaded area marks drought periods noted in Liu et al. (2024). 

gradually weakened and was largely relieved in January 2008 following lower temperatures and increased rainfall. For the 2017 event, mild drought first developed in central Inner Mongolia and parts of Jilin in March. From April to early May, drought conditions intensified in Hebei, Inner Mongolia, Heilongjiang, Liaoning, and Jilin under reduced precipitation and rising temperatures. In late May, drought in much of Jilin was alleviated by rainfall, and in June the drought weakened further in Heilongjiang and Hebei, whereas it persisted in Inner Mongolia and Liaoning because of insufficient precipitation. 

The results showed that all three indices captured the overall evolution of the two drought events, including their development, peak, and subsequent alleviation. However, differences were observed in the spatial details and temporal transitions of the drought patterns depicted by the three indices. For the autumn-winter drought in Southern China in 2007, the CDI, SPI− 1, and SSI− 1 all reproduced the marked intensification in November and the subsequent weakening after late December. Compared with SPI− 1 and SSI− 1, the CDI showed a more spatially continuous drought signal over Southern China during the onset stage in October, and it also captured more residual drought patches during December and January. This pattern suggests that the CDI was able to describe the gradual emergence and recession of drought conditions in greater spatial detail, whereas SPI− 1 and SSI− 1 mainly captured the regional-scale evolution of the event. 

A similar pattern was observed for the spring–summer drought in Northeastern China in 2017. The CDI, SPI− 1, and SSI− 1 all identified the main drought-affected areas in North China and Northeast China and captured the overall intensification from March to May. At the same time, the CDI showed a clearer distinction between the core drought area and the surrounding transitional zones, especially during April and May when the event expanded rapidly. In June, the CDI also depicted the partial relief in some affected regions while preserving drought persistence in Inner Mongolia and Liaoning. By comparison, SPI− 1 and SSI− 1 still reflected the main drought pattern, but their spatial transitions were relatively less detailed in some months. These differences indicate that the CDI did 

14 

_Journal of Hydrology: Regional Studies 66 (2026) 103623_ 

_X. Huang et al._ 

**Table 7** 

Typical drought events in China identified by CDI and their characteristics. 

|Sub-<br>region|Start–end period|Duration|Drought<br>severity|Drought<br>intensity|Average drought<br>Area (%)|Record of typical drought events|
|---|---|---|---|---|---|---|
|CSC|2001–03–2001–10|7 months|2.78|0.40|40.72|The spring-autumn drought in the North area of the<br>Yangtze River Basin in 2001|
||2003–06–2004–01|7 months|2.66|0.38|38.95|The summer–winter consecutive drought in Jiangnan<br>and South China, 2003–2004|
||2007–10–2008–01|3 months|1.61|0.54|54.79|The autumn–winter drought over southern China in 2007|
||2019–08–2020–01|5 months|2.50|0.50|50.99|The summer-autumn drought in the middle and lower<br>reaches of the Yangtze River in 2019|
|IM|2011–03–2011–11|8 months|2.98|0.37|38.21|The spring–autumn consecutive drought in Inner<br>Mongolia, 2011|
|NC|2002–01–2002–12|11<br>months|5.47|0.50|50.68|The spring-summer-autumn drought in North China and<br>the Huanghuai Region, 2002|
||2010–10–2011–02|4 months|2.79|0.70|70.63|The autumn–winter consecutive drought in North China,<br>2010–2011|
|NEC|2007–06–2007–12|6 months|4.39|0.73|74.13|The summer–autumn consecutive drought in Northeast<br>China, 2007|
||2017–03–2017–08|5 months|2.78|0.56|56.56|The spring–summer drought in Northeast China, 2017|
||2018–11–2019–05|6 months|4.63|0.77|78.10|The spring drought in Northeast China, 2019|
|SC|2004–09–2005–02|5 months|3.09|0.62|62.72|The autumn–winter consecutive drought in southern<br>South China, 2004–2005|
||2018–04–2018–08|4 months|1.13|0.28|29.13|The spring–summer drought over southern China, 2018|
|NWC|2008–05–2008–08|3 months|1.87|0.62|63.37|The spring-summer drought in Northwest China, Inner<br>Mongolia, and Shanxi Province in 2008|
|QTP|2009–9–2010–03|6 months|2.01|0.34|33.52|The autumn–spring extreme drought in the southeastern<br>Tibetan Plateau, 2009–2010|



not substitute for SPI− 1 or SSI− 1; rather, it complemented them by offering a more spatially nuanced description of drought evolution. Overall, the CDI, SPI− 1, and SSI− 1 were generally consistent in reflecting the two drought events, while the CDI appeared to provide a relatively more refined depiction of drought evolution under complex surface and climatic conditions. SPI− 1 is effective for characterizing short-term meteorological drought, whereas SSI− 1 provides valuable information on soil moisture-related drought conditions. By integrating meteorological, soil-moisture, vegetation, and temperature-related information, the CDI better captured differences in the temporal evolution and spatial expression of different drought-related responses. In these two cases, this advantage was mainly expressed in a more coherent identification of drought onset, a more continuous representation of drought persistence, and a smoother depiction of partial recovery. Therefore, compared with the traditional single-source indices, the CDI provided a more detailed portrayal of drought spatiotemporal evolution in these representative events, while the three indices remained broadly consistent in capturing the overall drought development. 

## _3.4. Spatiotemporal characteristics of drought in China revealed by CDI_ 

Drought characteristics, such as severity, intensity, duration, and frequency, were calculated from CDI for different sub-regions during 2001–2020 (Table 8). The spatial distribution results of these indicators in the four seasons are presented in Figs. 9–12. The results showed that drought characteristics exhibited a significant seasonal and regional variations in China (Figs. 13− 14). 

Across the seven sub-regions, drought severity displayed clear seasonal differences. Mean severity was highest in autumn (1.67), followed by winter (1.53) and summer (1.38), whereas spring had the lowest value (1.17). Regionally, NEC showed the widest seasonal range in severity (1.49–2.70), with the annual maximum occurring in winter (2.70), while IM maintained relatively high severity from spring to autumn (1.57–1.99). By contrast, NWC remained comparatively low in all four seasons (0.81–1.19). The strong winter severity in NEC likely reflects the combined effects of cold-season water storage and delayed release, because snow accumulation and frozen-soil processes can temporarily lock water in the land surface and postpone its effective availability to later periods. Earlier snowmelt may further reduce the snowmelt contribution to late-spring runoff, thereby aggravating seasonal moisture deficits rather than alleviating them. In IM, the relatively high severity from spring to autumn is more likely driven by the hydroclimatic setting of the arid- to semi-arid transition zone, where precipitation is limited, strongly seasonal, and insufficient to offset cumulative moisture loss once dry conditions develop. 

Drought intensity showed a pattern similar to that of drought severity, with higher mean values in autumn and winter (both 0.40) and lower values in spring and summer (0.32–0.34). IM recorded the highest average intensity in spring and autumn (0.43 and 0.46, respectively), whereas NEC had the highest values in summer and winter (0.43 and 0.59, respectively). This indicates that drought in these two regions became more intense once established. In IM, stronger intensity may result from rapid soil-water depletion under limited rainfall supply and high atmospheric demand during the warm season, which allows moisture stress to accumulate quickly over grassland- and cropland-dominated areas. In NEC, the high summer–winter intensity suggests that once moisture deficits emerge, they are amplified by seasonal carry-over effects rather than remaining confined to a single short-lived event. More broadly, stronger responses of grassland and cultivated vegetation to cumulative and lagged drought help explain why the CDI intensity signal was particularly sharp in northern transitional regions. For drought duration, spring had the shortest mean duration (2.63 months), 

15 

_Journal of Hydrology: Regional Studies 66 (2026) 103623_ 



**Fig. 9.** Spatiotemporal distribution of drought conditions represented by the CDI, SPI− 1, and SSI− 1 for the 2007 autumn-winter drought in Southern China. 

whereas autumn had the longest (3.44 months), followed by winter (3.19 months) and summer (3.09 months). IM showed the longest drought duration in spring (3.29 months), while NEC became the dominant long-duration region from summer onward and maintained prolonged events into winter (3.83–4.01 months). This seasonal shift suggests that drought persistence was controlled by different mechanisms in different regions. In IM, prolonged events from spring to autumn were likely shaped by progressive moisture exhaustion under limited precipitation replenishment, so once initiated, drought was not easily terminated. In NEC, the persistence from summer to winter points more strongly to delayed hydrological adjustment, because cold-season storage and thaw-related release can extend the effects of water deficit across seasons. Meanwhile, the generally longer propagation time of drought in northern China provided a process-based explanation for why long-duration events were concentrated in IM and NEC. 

Drought frequency showed a seasonal pattern broadly consistent with that of drought duration, with the highest mean frequency in autumn (2.08 times), followed by winter (1.80 times) and summer (1.59 times), whereas spring had the lowest value (1.26 times). NEC had the highest drought frequency in summer and winter (at 2.32 times and 1.99 times, respectively), while IM was also prominent in spring (1.50 times); in autumn, the highest frequency occurred in QTP (3.34 times). The recurrence of drought in IM and NEC indicates that these regions were repeatedly plagued by water shortages. In IM, repeated occurrence was likely promoted by unstable precipitation supply and repeated re-intensification of water stress under semi-arid climatic conditions. In NEC, higher frequency in summer 

16 

_Journal of Hydrology: Regional Studies 66 (2026) 103623_ 

_X. Huang et al.                                                                                                                                                                                                         Journal of Hydrology: Regional Studies_ 



**Fig. 10.** Spatiotemporal distribution of drought conditions represented by the CDI, SPI− 1 and SSI− 1 for the 2017 spring-summer drought event in Northeastern China. 

and winter suggests that drought development was facilitated by seasonal propagation, meaning that an initial deficit could continue evolving instead of being fully alleviated by subsequent climate conditions. 

## **4. Discussion** 

This study developed a composite drought index (CDI) for China by integrating multiple drought-related variables within an XGBoost framework and evaluated its applicability across seven sub-regions. Compared with traditional single-indicator drought indices and linear composite approaches, the CDI showed stable performance in drought identification, drought grade classification, and the tracking of drought development. For example, Dai et al. (2023) modified the TVDI for agricultural drought monitoring in Northeast China, which significantly improved dry/wet boundary fitting compared with the traditional TVDI (R² increased from 0.37 to 0.90–0.53–0.91). However, although improved versions of TVDI have been shown to enhance agricultural drought monitoring, the single temperature-vegetation channel still had difficulty simultaneously and robustly representing complex land-surface conditions, topographic differences, and multiple drought-related stresses. By jointly incorporating energy-related indicators, evapotranspiration-related variables, and soil-moisture-related indices, including CWSI, SMCI, and TCI, in addition to TVDI, the CDI 

17 

_X. Huang et al.                                                                                                                                                                                                         Journal of Hydrology: Regional Studies 66 (2026) 103623_ 

**Table 8** 

Statistics of drought characteristics in different sub-regions. 

|Sub-region|Season|Drought<br>severity|Drought<br>intensity|Drought duration (months)|Drought frequency (times)|
|---|---|---|---|---|---|
|CSC|Spring|1.07|0.27|2.37|1.18|
||Summer|1.74|0.42|3.53|2.13|
||Autumn|1.57|0.35|3.33|1.79|
||Winter|1.28|0.35|2.95|1.59|
|IM|Spring|1.57|0.43|3.29|1.50|
||Summer|1.25|0.34|2.88|1.75|
||Autumn|1.99|0.46|3.36|1.52|
||Winter|1.36|0.38|2.69|1.39|
|NC|Spring|1.41|0.42|2.81|1.47|
||Summer|1.22|0.33|2.68|1.14|
||Autumn|1.89|0.51|3.49|2.60|
||Winter|1.35|0.38|3.00|1.52|
|NEC|Spring|1.49|0.32|2.97|1.05|
||Summer|1.85|0.43|3.83|2.32|
||Autumn|1.97|0.43|3.31|1.28|
||Winter|2.70|0.59|4.01|1.99|
|NWC|Spring|1.07|0.30|2.88|1.76|
||Summer|0.81|0.21|2.67|1.35|
||Autumn|0.99|0.25|3.15|1.54|
||Winter|1.19|0.30|3.36|1.98|
|SC|Spring|0.71|0.22|1.73|0.72|
||Summer|1.29|0.28|2.76|1.05|
||Autumn|1.55|0.39|3.45|2.52|
||Winter|1.72|0.48|3.35|2.33|
|QTP|Spring|0.89|0.25|2.36|1.15|
||Summer|1.53|0.34|3.29|1.38|
||Autumn|1.72|0.41|3.97|3.34|
||Winter|1.09|0.30|2.97|1.81|



**Note:** Values represent the seasonal mean drought severity, intensity, duration, and frequency derived from drought events identified using run theory in each sub-region during 2001–2020. 

improved model fitting over complex land surfaces, as indicated by relatively high EVS values obtained in both the training and validation sets, reaching 0.63–0.89 and 0.54–0.82, respectively (Figs. 4 and 5). In addition, Faiz et al. (2025) found that the correlation between a comprehensive drought index and soil moisture and crop water demand can be enhanced by integrating potential evapotranspiration (PET), actual evapotranspiration (ET), and radiation components. Therefore, the CDI incorporated energy indicators (TVDI/CWSI) and soil moisture indicators (SMCI) while retaining the physical constraints centered on evapotranspiration (ET, PET), which may help improve the accuracy of identifying typical drought events. For example, during the spring–summer drought event in northeastern China in 2017, the CDI showed a better spatiotemporal response to the evolution of the persistent drought from March to June than SPI− 1 (Fig. 10). At the national scale in China, Zhao et al. (2024) developed an Ecological Comprehensive Drought Index (ECDI) by integrating precipitation, evapotranspiration, and soil moisture within a three-dimensional copula framework, highlighting the value of multi-source constraints in composite drought assessment, with more than 90% of grid cells showing RMSE values below 0.1. However, the performance of the copula-based approach remained dependent on the selection of marginal distributions and was sensitive to model specification. In comparison, the CDI developed in this study provided a more flexible framework for integrating multiple drought-related predictors by using gradient-boosted trees to capture nonlinear relationships and feature interaction. It also achieved a drought-classification consistency rate of 74.50%–83.88% against SPEI− 1, indicating classification consistency across regions. 

Previous studies have shown that XGBoost has shown robust and efficient performance under conditions of multi-factor coupling. For example, Li et al. (2023) developed a drought monitoring model for Southwest China using multi-source remote sensing and station observations, and reported that the drought grades predicted by XGBoost were more than 85% consistency with SPEI− 1 records from 144 stations. Similarly, Xu et al. (2024) compared the performance of XGBoost, Random Forest, LSTM, and BPNN for agricultural drought prediction in the Dabie Mountains region and found that XGBoost and Random Forest outperformed LSTM and BPNN in terms of R², RMSE, and MAE. Building on these findings, this study further extended the XGBoost-based framework from regional or watershed-scale applications to the national scale in China. The resulting CDI achieved a drought-classification consistency rate of 67.19%–74.64% against SPI− 1, indicating good scalability and stable classification performance across regions. In addition, the CDI effectively captured the evolution of typical drought events. During the autumn–winter drought in southern China in 2007, as reported by Zou et al. (2008), the CDI more clearly identified the early expansion of drought and its residual effects than SPI− 1. Likewise, during the 2017 spring–summer drought in Northeast China, the CDI detected a mild drought signal in March, which intensified in April and gradually eased in June. This temporal evolution was consistent with previous reports by Zeng et al. (2019) and Wang et al., (2019). 

Furthermore, the CDI revealed clear spatiotemporal patterns of drought across China during 2001–2020. At the national scale, drought occurred most frequently in summer and autumn and was often accompanied by pronounced compound heat–drought characteristics. This pattern agrees with the report by Yu and Zhai (2020), which utilized daily data from 1961 to 2018 and 

18 

_X. Huang et al._ 

_Journal of Hydrology: Regional Studies 66 (2026) 103623_ 



**Fig. 11.** Spatial distribution characteristics of average drought severity during 2001–2020. (a) Spring; (b) Summer; (c) Autumn; (d) Winter. Higher values indicate stronger cumulative drought severity during identified drought events. 

documented that compound heat–drought events across China were more frequent and persistent during the warm season (May–October). As shown in the results of this study, autumn droughts were particularly frequent and long-lasting in the middle and lower reaches of the Yangtze River and in the regions to their north. Several major drought episodes have also been documented in this broader region, as supported by previous studies, including the winter–spring drought of 2011, the summer drought of 2013, and the autumn drought of 2019 (Jin et al., 2013; Yuan et al., 2016; Liu et al., 2021), as well as multiple compound heat-drought processes (Zhang et al., 2014). The regions extending from eastern IM to eastern NEC and NC showed high drought severity and frequency in most periods. Among them, the summer drought frequency in NEC and autumn drought in NC (especially in Hebei Province) were more prominent, consistent with both the northern summer drought mechanism revealed by Yang et al. (2024) from the perspective of atmospheric circulation and the MCI-based drought-event identification results for NC by Cai et al. (2021). In NC, spring and summer droughts exhibited characteristics of in-phase interannual variations, and S-EOF and teleconnection analysis linked this variation signal to the height anomalies of Lake Baikal and the spring NAO (Hu et al., 2022). In Southwest China, droughts were often persistent and sometimes spanned from the cold season into early spring, with a high frequency and long duration. Barriopedro et al. (2012) and Lan and Yan (2024) also reported similar results for drought characteristics and causes in Yunnan Province during 1961–2020. In the Qinghai-Tibet Plateau, CDI revealed that spring droughts were generally mild while winter droughts were more severe. This finding was consistent with Feng et al. (2020), who used SPEI data from 1970 to 2017 and reported significant humidification in spring and an increase in the frequency of severe winter drought. Overall, the CDI effectively identified high-risk drought seasons in China over the past 20 years and performed well in capturing compound heat–drought events, particularly with high sensitivity to severe autumn drought. 

Although the XGBoost-based CDI effectively captured the spatiotemporal patterns of drought and the evolution of typical drought events across China, several limitations should still be acknowledged. First, the current CDI should be regarded as a semi-dependent, multi-source composite drought index developed within a meteorological drought framework of SPEI− 1, rather than as a fully 

19 

_X. Huang et al.                                                                                                                                                                                                         Journal of Hydrology: Regional Studies 66 (2026) 103623_ 



**Fig. 12.** Spatial distribution characteristics of average drought intensity during 2001–2020. (a). Spring; (b). Summer; (c). Autumn; (d). Winter. Higher values indicate greater average drought severity per unit duration. 

independent drought indicator. While comparisons with SPI− 1, SSI− 1, and typical drought events suggest that the CDI captures complementary information related to soil moisture stress and evapotranspiration-related water stress, it remains constrained by the SPEI− 1 reference adopted during model training. Because SPEI− 1 was used as the training target and the predictors were matched at the monthly scale, the current CDI was specifically designed for monthly drought monitoring. It should therefore not be directly interpreted as a multi-scale CDI. Extending the CDI to longer timescales, such as 3-month or 12-month CDI, would require scalespecific target variables, such as SPEI− 3 or SPEI− 12, corresponding temporal aggregation or reformulation of predictors, and separate model training and validation. Therefore, considering both its target-dependence and temporal-scale constraints, the current CDI is more suitable for monthly operational drought monitoring as an integrated screening and early-warning tool for tracking regional drought evolution, rather than as a complete replacement for independent agricultural or hydrological drought indicators. For research applications, it provides a useful framework for evaluating the added value of multi-source remote sensing information in monthly drought characterization, but further development with independent drought targets and scale-specific model training is needed before it can be regarded as a fully independent and multi-scale drought benchmark. Second, a fixed hold-out validation strategy was used instead of k-fold cross-validation because the main purpose was to evaluate the predictive performance of the CDI within each sub-regional modeling domain, rather than to test its transferability to completely unseen spatial domains. Under this objective, the fixed 80/20 training–validation split strategy provides a useful assessment of within-region model performance and is unlikely to affect the main interpretation that the CDI can reproduce regional drought variability under the current modeling framework. However, because drought-related variables may show spatial and temporal autocorrelation, holdout validation may provide a relatively optimistic estimate of model generalization. Third, like other tree-ensemble regression models, XGBoost may show bias in tail-value, with predictions tending to shrink toward the central range of the target distribution (Belitz and Stackelberg, 2021). For CDI, this limitation mainly concerns the lower tail of SPEI− 1, where more negative values indicate more severe drought. For the lowest 5% of SPEI− 1 samples, the CDI was generally less negative than SPEI− 1, with CDI values being 0.30–0.63 higher than SPEI− 1 

20 

_Journal of Hydrology: Regional Studies 66 (2026) 103623_ 

_X. Huang et al.                                                                                                                                                                                                         Journal of Hydrology: Regional Studies_ 



**Fig. 13.** Spatial distribution characteristics of average drought duration during 2001–2020. (a). Spring; (b). Summer; (c). Autumn; (d). Winter. Higher values indicate longer persistence of identified drought events. 

on average across the seven sub-regions, indicating that severe drought intensity was partly smoothed toward less extreme values. In addition, because XGBoost does not explicitly model temporal dependence, its ability to represent drought persistence and evolution remains limited, as also noted in previous XGBoost-based drought studies (Felsche and Ludwig, 2021). Fourth, the gain-based importance results in Section 2.1.2 should be interpreted as model-based predictive contributions rather than as evidence that individual predictors independently have causal effects on drought development or the CDI variation. Although the reduced-predictor model comparison showed that the identified NDVI–LAI correlation had only limited influence on model stability and did not materially affect the subsequent CDI-based drought assessment, the multicollinearity assessment in this study should still be interpreted as a diagnostic analysis rather than a complete test of predictor independence. Because the Pearson correlation mainly evaluates pairwise linear associations, it may not fully capture nonlinear dependence or higher-order interactions among predictors representing similar drought-related processes, such as vegetation-related variables (NDVI, VCI, LAI, and SIFCI). In tree-based models such as XGBoost, these process-related predictors may partly share predictive information even when their pairwise Pearson correlations are not consistently high. Therefore, the gain-based importance of an individual predictor should be interpreted as its contribution within the full predictor set rather than as a fully independent contribution. Future studies could also combine tree-ensemble methods with sequence models, such as LSTM or Transformer-based models, to better capture drought seasonality, persistence, and lagged responses, thereby improving the representation of extreme drought events. In addition, recent studies have suggested that incorporating GRACE/GRACE-FO terrestrial water storage (TWS) data into hydrological and land-surface models can improve drought monitoring by capturing both surface and subsurface water deficits (Tapley et al., 2019; Soltani et al., 2021). Building on this, future work could integrate GRACE-based groundwater information, GLDAS runoff variables, higher-resolution remote-sensing products (e.g., LAI and soil moisture with 30 m resolution), and station observations to provide a more comprehensive and spatially refined feature set for CDI construction Such efforts would also support the development of a multi-source drought early-warning framework at seasonal, semiannual, and annual timescales for long-term drought risk management. 

21 

_X. Huang et al._ 

_Journal of Hydrology: Regional Studies 66 (2026) 103623_ 



**Fig. 14.** Spatial distribution characteristics of average drought frequency during 2001–2020. (a). Spring; (b). Summer; (c). Autumn; (d). Winter. Higher values indicate more frequent drought occurrence during the study period. 

## **5. Conclusions** 

This study developed a composite drought index (CDI) for China by integrating 11 variables, including PCI, TCI, VCI, NDVI, LAI, SIFCI, SMCI, CWSI, TVDI, NDEMZ, and LC, within an XGBoost framework, and evaluated its applicability under different climatic and land-surface conditions. Based on the CDI, the spatiotemporal characteristics of drought in China from 2001 to 2020 were identified and analyzed. The main conclusions are as follows: 

- (1) The CDI showed stable and generally strong performance, with validation-set EVS ranging from 0.54 to 0.82 across the seven sub-regions. Although the model performance varied among regions, the CDI remained effective even in topographically complex areas such as the Qinghai–Tibet Plateau. 

- (2) As a semi-dependent composite drought index trained using SPEI− 1 as the target variable, the CDI effectively reflected meteorological drought signals and captured information related to soil-moisture stress. The CDI was significantly and positively correlated with both SPI− 1 (R = 0.36–0.81) and SSI− 1 (R = 0.42–0.70). Compared with individual drought indicators, such as SPI− 1 and SSI− 1, the CDI integrated multi-source information and better captured differences in the temporal evolution and spatial expression of meteorological, soil-moisture, vegetation, and thermal-related drought responses, thereby providing a more coherent representation of drought onset, persistence, and recovery in representative events. 

- (3) Drought in China exhibited significant spatiotemporal heterogeneity during 2001–2020. At the seasonal scale, drought was generally more severe and persistent in autumn, with the highest severity (1.67) and longest duration (3.44 months), whereas spring drought was relatively mild, with a severity of 1.17 and a duration of 2.63 months. At the regional scale, IM had the highest drought risk in China, with seasonal average severity ranging from 1.25 to 1.99. NEC experienced the longest drought duration (ranging from 2.97 to 4.01 months), especially in winter, when prolonged drought duration was associated with the 

22 

_Journal of Hydrology: Regional Studies 66 (2026) 103623_ 

_X. Huang et al.                                                                                                                                                                                                         Journal of Hydrology: Regional Studies_ 

highest drought severity (2.70). In contrast, the drought risks were lower in NWC, SC and QTP, with maximum seasonal average severity of less than 1.19, 1.72 and 1.72, respectively. 

## **Declaration of Competing Interest** 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

## **Acknowledgements** 

This work was jointly funded by the Basic Research Program of Jiangsu (Grant No. BK20242106), the Jiangxi Science and Technology Program Project (Grant No. 20252ABF010001 and 20244BCF61001), the Ganpo Excellent Talent Support Program of Jiangxi–Training Program for Academic and Technical Leaders in Major Disciplines (Grant No. 20232BCJ22011), and the Project of Jiujiang Science and Technology Bureau (Grant No. 2025_000773). 

## **Data availability** 

Data will be made available on request. 

## **References** 

Abu Arra, A., S¸is¸man, E., 2023. Characteristics of Hydrological and Meteorological Drought Based on Intensity-Duration-Frequency (IDF) Curves. Water 15 (17), 3142. https://doi.org/10.3390/w15173142. 

Bai, J.-j, Yu, Y., Di, L., 2017. Comparison between TVDI and CWSI for drought monitoring in the Guanzhong Plain. China J. Integr. Agric. 16, 389–397. https://doi. org/10.1016/S2095-3119（15）61302-8. 

- Barriopedro, D., Gouveia, C.M., Trigo, R.M., Wang, L., 2012. The 2009/10 drought in China: Possible causes and impacts on vegetation. J. Hydrometeorol. 13, 1251–1267. https://doi.org/10.1175/JHM-D-11-074.1. 

- Beck, H.E., McVicar, T.R., Vergopolan, N., Berg, A., Lutsko, N.J., Dufour, A., Zeng, Z., Jiang, X., van Dijk, A.I.J.M., Miralles, D.G., 2023. High-resolution (1 km) Koppen¨ –Geiger maps for 1901–2099 based on constrained CMIP6 projections. Sci. Data 10, 724. https://doi.org/10.1038/s41597-023-02549-6. 

- Beguería, S., Vicente-Serrano, S.M., Reig, F., Latorre, B., 2014. Standardized precipitation evapotranspiration index (SPEI) revisited: parameter fitting, evapotranspiration models, tools, datasets and drought monitoring. Int. J. Climatol. 34 (10), 3001–3023. https://doi.org/10.1002/joc.3887. 

- Belitz, K., Stackelberg, P.E., 2021. Evaluation of six methods for correcting bias in estimates from ensemble tree machine-learning regression models. Environ. Model. Softw. 139, 105006. https://doi.org/10.1016/j.envsoft.2021.105006. 

- Bergaoui, K., Belhaj Fraj, M., Fragaszy, S., Ghanim, A., Hamadin, O., Al-Karablieh, E., Al-Bakri, J., Fakih, M., Fayad, A., Comair, F., Yessef, M., Ben Mansour, H., Belgrissi, H., Arsenault, K., Peters-Lidard, C., Kumar, S., Hazra, A., Nie, W., Hayes, M., Svoboda, M., McDonnell, R., 2024. Development of a composite drought indicator for operational drought monitoring in the MENA region. Sci. Rep. 14, 5414. https://doi.org/10.1038/s41598-024-55626-0. 

- Cai, X., Zhang, W., Fang, X., Zhang, Q., Zhang, C., Chen, D., Cheng, C., Fan, W., Yu, Y., 2021. Identification of regional drought processes in North China using MCI analysis. Land 10, 1390. https://doi.org/10.3390/land10121390. 

- Cao, M., Chen, M., Liu, J., Liu, Y., 2022. Assessing the performance of satellite soil moisture on agricultural drought monitoring in the North China Plain. Agric. Water Manag. 263, 107450. https://doi.org/10.1016/j.agwat.2021.107450. 

- Chen, T., Guestrin, C., 2016. XGBoost: A scalable tree boosting system. Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD ’16). Association for Computing Machinery, pp. 785–794. https://doi.org/10.1145/2939672.2939785. 

- Dai, R., Chen, S., Cao, Y., Zhang, Y., Xu, X., 2023. A modified temperature–vegetation dryness index (mTVDI) for agricultural drought assessment based on MODIS data: A case study in Northeast China. Remote. Sens. 15 (7), 1915. https://doi.org/10.3390/rs15071915. 

- Ding, Y., Gong, X., Xing, Z., Cai, H., Zhou, Z., Zhang, D., Sun, P., Shi, H., 2021. Attribution of meteorological, hydrological and agricultural drought propagation in different climatic regions of China. Agric. Water Manag. 255, 106996. https://doi.org/10.1016/j.agwat.2021.106996. 

- Faiz, M.A., Zhang, L., Liu, D., Ma, N., Li, M., Zhou, Z., Baig, F., Li, T., Cui, S., 2025. Revisiting the composite drought index for improving drought monitoring. J. Hydrol. 652, 132707. https://doi.org/10.1016/j.jhydrol.2025.132707. 

- Felsche, E., Ludwig, R., 2021. Applying machine learning for drought prediction in a perfect model framework using data from a large ensemble of climate simulations. Nat. Hazards Earth Syst. Sci. 21, 3679–3691. https://doi.org/10.5194/nhess-21-3679-2021. 

- Feng, A., Chen, Y., He, X., Liu, P., 2023. Drought monitoring from Fengyun satellite series: A comparative analysis with meteorological-drought composite index (MCI). Remote. Sens. 15 (22), 5410. https://doi.org/10.3390/rs15225410. 

- Feng, W., Lu, H., Yao, T., et al., 2020. Drought characteristics and its elevation dependence in the Qinghai–Tibet Plateau during the last half-century. Sci. Rep. 10, 14323. https://doi.org/10.1038/s41598-020-71295-1. 

- Gebrechorkos, S.H., et al., 2025. Warming accelerates global drought severity. Nature, advance online publication. https://doi.org/10.1038/s41586-025-09047-2. Guo, B., Zhang, J., Meng, X., et al., 2020. Long-term spatio-temporal precipitation variations in China with precipitation surface interpolated by ANUSPLIN. Sci. Rep. 10, 81. https://doi.org/10.1038/s41598-019-57078-3. 

- Han, Y.X., Wu, J.P., Zhai, B.N., Pan, Y.X., Huang, G.M., Wu, L.F., Zeng, W.Z., 2019. Coupling a bat algorithm with XGBoost to estimate reference evapotranspiration in the arid and semiarid regions of China. Adv. Meteorol. 2019, 9575782. https://doi.org/10.1155/2019/9575782. 

- Hao, Z., AghaKouchak, A., 2014. A nonparametric multivariate multi-index drought monitoring framework. J. Hydrometeorol. 15 (1), 89–101. https://doi.org/ 10.1175/JHM-D-12-0160.1. 

- Hoylman, Z.H., Holden, Z., Bocinsky, R.K., Ketchum, D., Swanson, A., Jencso, K., 2024. Optimizing drought assessment for soil moisture deficits. Water Resour. Res. 60 (6), e2023WR036087. https://doi.org/10.1029/2023WR036087. 

- Hu, Y., Li, P., Sun, C., Li, J., 2022. In-phase variations of spring and summer droughts over Northeast China. J. Clim. 35 (21), 3579–3596. https://doi.org/10.1175/ JCLI-D-22-0052.1. 

- Inocˆencio, T., de, M., Ribeiro Neto, A., Souza, A.G.S.S., 2020. Soil moisture obtained through remote sensing to assess drought events. Rev. Bras. Eng. Agr. íC. Ambient. 24 (9), 575–580. https://doi.org/10.1590/1807-1929/agriambi.v24n9p575-580. 

IPCC, 2023. Summary for Policymakers. In: Masson-Delmotte, V., Zhai, P., Pirani, A., et al. (Eds.), , Climate Change 2021: The Physical Science Basis. Contribution of Working Group I to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change. Cambridge Univ. Press, Cambridge, United Kingdom and New York, NY, USA, pp. 3–32. https://doi.org/10.1017/9781009157896.001. Jackson, R.D., Idso, S.B., Reginato, R.J., Pinter Jr, P.J., 1981. Canopy temperature as a crop water stress indicator. Water Resour. Res. 17 (4), 1133–1138. https://doi. org/10.1029/WR017i004p01133. 

23 

_X. Huang et al.                                                                                                                                                                                                         Journal of Hydrology: Regional Studies 66 (2026) 103623_ 

- Ji, L., Peters, A.J., 2003. Assessing vegetation response to drought in the northern Great Plains using vegetation and drought indices. Remote. Sens. Environ. 87, 85–98. https://doi.org/10.1016/S0034-4257(03)00174-3. 

- Jin, D., Lin, H., Li, Y., 2013. The extreme drought event during winter–spring of 2011 in the middle and lower reaches of the Yangtze River, China. J. Clim. 26 (20), 8210–8225. https://doi.org/10.1175/JCLI-D-12-00652.1. 

- Katzenberger, A., Levermann, A., 2024. Consistent increase in East Asian summer monsoon rainfall and its variability under climate change over China in CMIP6. Earth Syst. Dyn. 15 (4), 1137–1151. https://doi.org/10.5194/esd-15-1137-2024. 

- Kim, S.W., Jung, D., Choung, Y.-J., 2020. Development of a multiple linear regression model for meteorological drought index estimation based on Landsat satellite imagery. Water 12 (12), 3393. https://doi.org/10.3390/w12123393. 

- Kogan, F.N., 1995. Application of vegetation index and brightness temperature for drought detection. Adv. Space Res. 15 (11), 91–100. https://doi.org/10.1016/ 0273-1177(95)00079-T. 

- Kogan, F.N., 1997. Global drought watch from space. Bull. Am. Meteorol. Soc. 78 (4), 621–636. https://doi.org/10.1175/1520-0477(1997)078 _<_ 0621:GDWFS _>_ 2.0. CO;2. 

- Lan, T., Yan, X., 2024. Analysis of drought characteristics and causes in Yunnan Province in the last 60 years (1961–2020). J. Hydrometeorol. 25 (1), 177–190. https://doi.org/10.1175/JHM-D-23-0092.1. 

- Li, H., Zhu, Y., 2020. XGBoost algorithm optimization based on gradient distribution harmonized strategy. J. Comput. Appl. 40 (6), 1633–1637. https://doi.org/ 10.11772/j.issn.1001-9081.2019101878. 

- Li, M., Yao, Y., Feng, Z., Ou, M., 2025. Hydrological drought prediction and its influencing features analysis based on a machine learning model. Nat. Hazards Earth Syst. Sci. 25, 4299–4316. https://doi.org/10.5194/nhess-25-4299-2025. 

- Li, X., Jia, H., Wang, L., 2023. Remote sensing monitoring of drought in Southwest China using random forest and eXtreme gradient boosting methods. Remote. Sens. 15 (19), 4840. https://doi.org/10.3390/rs15194840. 

- Liang, L., Sun, Q., Luo, X., Wang, J., Zhang, L., Deng, M., Di, L., Liu, Z., 2017. Long-term spatial and temporal variations of vegetative drought based on vegetation condition index in China. Ecosphere 8 (8), e01919. https://doi.org/10.1002/ecs2.1919. 

- Liu, X., Zhu, X., Zhang, Q., Yang, T., Pan, Y., Sun, P., 2020. A remote sensing and artificial neural network-based integrated agricultural drought index: Index development and applications. Catena 186, 104394. https://doi.org/10.1016/j.catena.2019.104394. 

- Liu, Y., Yue, H., 2018. The temperature vegetation dryness index (TVDI) based on bi-parabolic NDVI-Ts space and gradient-based structural similarity (GSSIM) for long-term drought assessment across Shaanxi Province, China (2000–2016). Remote. Sens. 10 (6), 959. https://doi.org/10.3390/rs10060959. 

- Liu, Z., Zhou, W., Wang, X., 2024. Extreme meteorological drought events over China (1951–2022): Migration pattern, diversity of temperature extremes, and decadal variations. Adv. Atmos. Sci. 41 (12), 2313–2336. https://doi.org/10.1007/s00376-024-4004-2. 

- Ma, S., Zhou, T., Ang´elil, O., Zhang, W., Shiogama, H., Zheng, B., 2017. Increased chances of drought in the southeastern periphery of the Tibetan Plateau induced by anthropogenic warming. J. Clim. 30 (16), 6543–6560. https://doi.org/10.1175/JCLI-D-16-0636.1. 

- Ma, Z.-C., Sun, P., Zhang, Q., Hu, Y.-Q., Jiang, W., 2021. Characterization and evaluation of MODIS-derived crop water stress index (CWSI) for monitoring drought from 2001 to 2017 over Inner Mongolia. Sustainability 13 (2), 916. https://doi.org/10.3390/su13020916. 

McKee, T.B., Doesken, N.J., Kleist, J., 1993. The relationship of drought frequency and duration to time scales. Proceedings of the Eighth Conference on Applied Climatology. American Meteorological Society, pp. 179–184. Oyounalsoud, M.S., Yilmaz, A.G., Abdallah, M., Abdeljaber, A., 2024. Drought prediction using artificial intelligence models based on climate data and soil moisture. Sci. Rep. 14, 19700. https://doi.org/10.1038/s41598-024-70406-6. 

- Palagiri, H., Pal, M., 2024. Agricultural drought risk assessment in Southern Plateau and Hills using multi threshold run theory. Results Eng. 22, 102022. https://doi. org/10.1016/j.rineng.2024.102022. 

Palmer, W.C., 1965. Meteorological drought (Research Paper No. 45). U. S. Weather. Bur. Wash. DC. 

- Peel, M.C., Finlayson, B.L., McMahon, T.A., 2007. Updated world map of the Koppen¨ –Geiger climate classification. Hydrol. Earth Syst. Sci. 11 (5), 1633–1644. https://doi.org/10.5194/hess-11-1633-2007. 

- Pei, Z., Fan, Y., Wu, B., 2023. Drought monitoring of spring maize in the Songnen Plain using multi-source remote sensing data. Atmosphere 14 (11), 1614. https:// doi.org/10.3390/atmos14111614. 

- Quiring, S.M., Ganesh, S., 2010. Evaluating the utility of the vegetation condition index (VCI) for monitoring meteorological drought in Texas. Agric. For. Meteorol. 150 (3), 330–339. https://doi.org/10.1016/j.agrformet.2009.11.015. 

- Rhee, J., Im, J., Carbone, G.J., 2010. Monitoring agricultural drought for arid and humid regions using multi-sensor remote sensing data. Remote. Sens. Environ. 114 (12), 2875–2887. https://doi.org/10.1016/j.rse.2010.07.005. 

Rouse, J.W., Haas, R.H., Schell, J.A., Deering, D.W., 1974. Monitoring vegetation systems in the Great Plains with ERTS. In: Third ERTS-1 Symposium, NASA SP-351, 

1. NASA, Washington, DC, pp. 309–317. 

Sandholt, I., Rasmussen, K., Andersen, J., 2002. A simple interpretation of the surface temperature/vegetation index space for assessment of surface moisture status. Remote. Sens. Environ. 79 (2–3), 213–224. https://doi.org/10.1016/S0034-4257(01)00274-7. 

- Sang, Y., Tian, F., Jin, H., Cai, Z., Feng, L., Dou, Y., Eklundh, L., 2024. Assessing topographic effects on forest responses to drought with multiple seasonal metrics from Sentinel-2. Int. J. Appl. Earth Obs. Geoinf. 128, 103789. https://doi.org/10.1016/j.jag.2024.103789. 

- Shilengwe, C., Banda, K., Nyambe, I., 2024. Machine learning downscaling of GRACE/GRACE-FO data to capture spatial-temporal drought effects on groundwater storage at a local scale under data-scarcity. Environ. Syst. Res. 13, 38. https://doi.org/10.1186/s40068-024-00368-1. 

- Soltani, S.S., Ataie-Ashtiani, B., Simmons, C.T., 2021. Review of assimilating GRACE terrestrial water storage data into hydrological models: Advances, challenges and opportunities. Earth-Sci. Rev. 213, 103487. https://doi.org/10.1016/j.earscirev.2020.103487. 

- Sun, A.Y., Scanlon, B.R., Save, H., Rateb, A., 2021. Reconstruction of GRACE total water storage through automated machine learning. Water Resour. Res. 57 (2), e2020WR028666. https://doi.org/10.1029/2020WR028666. 

Sundararajan, K., Garg, L., Srinivasan, K., Bashir, A.K., Kaliappan, J., et al., 2021. A contemporary review on drought modeling using machine learning approaches. Comput. Model. Eng. Sci. 128 (2), 447–487. https://doi.org/10.32604/cmes.2021.015528. 

- Svoboda, M., LeComte, D., Hayes, M., Heim, R., Gleason, K., Angel, J., Rippey, B., Tinker, R., Palecki, M., Stooksbury, D., Miskus, D., Stephens, S., 2002. The drought monitor. Bull. Am. Meteorol. Soc. 83 (8), 1181–1190. https://doi.org/10.1175/1520-0477-83.8.1181. 

- Tapley, B.D., Watkins, M.M., Flechtner, F., et al., 2019. Contributions of GRACE to understanding climate change. Nat. Clim. Change 9 (5), 358–369. https://doi.org/ 10.1038/s41558-019-0456-2. 

Tugrul, T., Hinis, M.A., 2025. Improvement of drought forecasting by means of various machine learning algorithms and wavelet transformation. Acta Geophys. 73, ˘ 855–874. https://doi.org/10.1007/s11600-024-01399-z. 

United Nations Office for Disaster Risk Reduction (UNDRR), Centre for Research on the Epidemiology of Disasters (CRED), 2020. The human cost of disasters: An overview of the last 20 years (2000–2019) [Report]. UNDRR, Geneva. 

van Ginkel, M., Biradar, C., 2021. Drought early warning in agri-food systems. Climate 9 (9), 134. https://doi.org/10.3390/cli9090134. 

Vicente-Serrano, S.M., Beguería, S., Lopez-Moreno, J.I., 2010. A multiscalar drought index sensitive to global warming: The standardized precipitation ´ evapotranspiration index. J. Clim. 23 (7), 1696–1718. https://doi.org/10.1175/2009JCLI2909.1. 

Wan, Z., Wang, P., Li, X., 2004. Using MODIS land surface temperature and normalized difference vegetation index products for monitoring drought in the Southern Great Plains, USA. Int. J. Remote. Sens. 25, 61–72. https://doi.org/10.1080/0143116031000115328. 

Wang, K., Li, T., Wei, J., 2019. Exploring drought conditions in the Three River Headwaters Region from 2002 to 2011 using multiple drought indices. Water 11 (2), 190. https://doi.org/10.3390/w11020190. 

Wang, N., Cheng, W.M., Wang, B.X., Liu, Q.Y., Zhou, C.H., 2020. Geomorphological regionalization theory system and division methodology of China. J. Geogr. Sci. 30, 212–232. https://doi.org/10.1007/s11442-020-1724-9. 

24 

_X. Huang et al.                                                                                                                                                                                                         Journal of Hydrology: Regional Studies 66 (2026) 103623_ 

Wang, S., Yuan, X., Wu, R., 2019. Attribution of the persistent spring–summer hot and dry extremes over Northeast China in 2017. Bull. Am. Meteorol. Soc. 100 (1), S85–S89. https://doi.org/10.1175/BAMS-D-18-0120.1. 

Wang, X., Blanken, P.D., Wood, J.D., Nouvellon, Y., Thaler, P., Gay, F., Kasemsap, P., Chidthaisong, A., Petchprayoon, P., Chayawat, C., Xiao, J., Li, X., 2023. Solarinduced chlorophyll fluorescence detects photosynthesis variations and drought effects in tropical rubber plantation and natural deciduous forests. Agric. For. Meteorol. 339, 109591. https://doi.org/10.1016/j.agrformet.2023.109591. 

- Wei, H., Liu, X., Hua, W., Zhang, W., Ji, C., Han, S., 2023. Copula-based joint drought index using precipitation, NDVI, and runoff and its application in the Yangtze River Basin, China. Remote. Sens. 15 (18), 4484. https://doi.org/10.3390/rs15184484. 

- Wen, Q., Chen, H., 2023. Changes in drought characteristics over China during 1961–2019. Front. Earth Sci. 11, 1138795. https://doi.org/10.3389/ feart.2023.1138795. 

World Meteorological Organization, 2012. In: Svoboda, M., Hayes, M., Wood, D. (Eds.), Standardized Precipitation Index User Guide. World Meteorological Organization, Geneva. WMO-No. 1090. 

- Xia, H.M., Sha, Y.T., Zhao, X.Y., Jiao, W.Z., Song, H.Q., Yang, J., Zhao, W., Qin, Y.C., 2024. HSPEI: A 1-km spatial resolution SPEI dataset across Chinese mainland from 2001 to 2022. Geosci. Data J. 11 (4), 479–494. https://doi.org/10.1002/gdj3.276. 

- Xia, L., Zhao, F., Mao, K., Yuan, Z., Zuo, Z., Xu, T., 2018. SPI-Based Analyses of Drought Changes over the Past 60 Years in China’s Major Crop-Growing Areas. Remote. Sens. 10 (2), 171. https://doi.org/10.3390/rs10020171. 

- Xiao, C., Zaehle, S., Yang, H., Wigneron, J.-P., Schmullius, C., Bastos, A., 2023. Land cover and management effects on ecosystem resistance to drought stress. Earth Syst. Dynam 14, 1211–1237. https://doi.org/10.5194/esd-14-1211-2023. 

- Xiao, X., Ming, W., Luo, X., Yang, L., Li, M., Yang, P., Ji, X., Li, Y., 2024. Leveraging multisource data for accurate agricultural drought monitoring: A hybrid deep learning model. Agric. Water Manag. 293, 108692. https://doi.org/10.1016/j.agwat.2024.108692. 

- Xu, L., Ning, S., Xu, X., Wang, S., Chen, L., Long, R., Zhang, S., Zhou, Y., Zhang, M., Thapa, B.R., 2024. Comparative analysis of machine learning models and explainable AI for agriculture drought prediction: A case study of the Ta-pieh mountains. Agric. Water Manag. 306, 109176. https://doi.org/10.1016/j. agwat.2024.109176. 

- Xu, Y., Wang, L., Ross, K.W., Liu, C., Berry, K., 2018. Standardized soil moisture index for drought monitoring based on soil moisture active passive observations and 36 years of North American Land Data Assimilation System data: A case study in the southeast United States. Remote. Sens. 10 (2), 301. https://doi.org/10.3390/ rs10020301. 

- Yang, J., Zhang, Q., Wang, P., Yue, P., Li, Y., Liang, Z., Liu, X., 2024. Characteristics of summer drought circulation and synergistic effects in the Northern DroughtProne Belt of China. Front. Environ. Sci. 12, 1464917. https://doi.org/10.3389/fenvs.2024.1464917. 

- Yao, N., Li, Y., Lei, T., Peng, L., 2018. Drought evolution, severity and trends in mainland China over 1961–2013, 616–617 Sci. Total. Environ. 73–89. https://doi.org/ 10.1016/j.scitotenv.2017.10.327. 

- Yu, R., Zhai, P., 2020. More frequent and widespread persistent compound drought and heat event observed in China. Sci. Rep. 10, 14576. https://doi.org/10.1038/ s41598-020-71312-3. 

- Yuan, W., Cai, W., Chen, Y., Liu, S., Dong, W., Zhang, H., Yu, G., Chen, Z., He, H., Guo, W., Liu, D., Liu, S., Xiang, W., Xie, Z., Zhao, Z., Zhou, G., 2016. Severe summer heatwave and drought strongly reduced carbon uptake in southern China in 2013. Sci. Rep. 6, 18813. https://doi.org/10.1038/srep18813. 

- Zeng, D., Yuan, X., Roundy, J.K., 2019. Effect of teleconnected land–atmosphere coupling on Northeast China persistent drought in spring–summer of 2017. J. Clim. 32 (21), 7403–7420. https://doi.org/10.1175/JCLI-D-19-0175.1. 

- Zhang, A., Jia, G., 2013. Monitoring meteorological drought in semiarid regions using multi-sensor microwave remote sensing data. Remote. Sens. Environ. 134, 12–23. https://doi.org/10.1016/j.rse.2013.02.023. 

- Zhang, Q., Miao, C., Su, J., Gou, J., Hu, J., Zhao, X., Xu, Y., 2025. A new high-resolution multi-drought-index dataset for mainland China. Earth Syst. Sci. Data 17, 837–853. https://doi.org/10.5194/essd-17-837-2025. 

- Zhang, R., Jin, F.-F., Turner, A.G., 2014. Increasing autumn drought over southern China associated with a southeastward extension of the summertime western North Pacific subtropical high. Geophys. Res. Lett. 41 (10), 4020–4026. https://doi.org/10.1002/2014GL060130. 

- Zhang, R., Chen, Z.-Y., Xu, L.-J., Ou, C.-Q., 2019. Meteorological drought forecasting based on a statistical model with machine learning techniques in Shaanxi province, China. Sci. Total. Environ. 665, 338–346. https://doi.org/10.1016/j.scitotenv.2019.01.431. 

- Zhang, R., Bento, V.A., Qi, J., Xu, F., Wu, J., Qiu, J., Li, J., Shui, W., Wang, Q., 2023. The first high spatial resolution multi-scale daily SPI and SPEI raster dataset for drought monitoring and evaluating over China from 1979 to 2018. Big Earth Data 7 (3), 860–885. https://doi.org/10.1080/20964471.2022.2148331. 

- Zhang, W., Du, P.J., Guo, S.C., Lin, C., Zheng, H.R., Fu, P.J., 2023. Enhanced remote sensing ecological index and ecological environment evaluation in arid area. Natl. Remote. Sens. Bull. 27 (2), 299–317. https://doi.org/10.11834/jrs.20221527 (in Chinese). 

- Zhao, Q., Zhang, X., Li, C., Xu, Y., Fei, J., 2024. Compound ecological drought assessment of China using a copula-based drought index. Ecol. Indic. 164, 112141. https://doi.org/10.1016/j.ecolind.2024.112141. 

- Zhao, S., Cong, D., He, K., Yang, H., Qin, Z., 2017. Spatial-temporal variation of drought in China from 1982 to 2010 based on a modified Temperature Vegetation Drought Index (mTVDI). Sci. Rep. 7, 17473. https://doi.org/10.1038/s41598-017-17810-3. 

- Zhao, S.Q., 1983. A new scheme for comprehensive physical regionalization in China. Acta Geogr. Sin. 38 (1), 1–10. https://doi.org/10.11821/xb198301001. 

Zhao, X., Xia, H., Pan, L., Song, H., Niu, W., Wang, R., Li, R., Bian, X., Guo, Y., Qin, Y., 2021. Drought monitoring over Yellow River Basin from 2003 to 2019 using reconstructed MODIS land surface temperature in Google Earth Engine. Remote. Sens. 13 (18), 3748. https://doi.org/10.3390/rs13183748. 

Zhao, Y., Zhang, J., Bai, Y., Zhang, S., Yang, S., Henchiri, M., Seka, A.M., Nanzad, L., 2022. Drought monitoring and performance evaluation based on machine learning fusion of multi-source remote sensing drought factors. Remote. Sens. 14 (24), 6398. https://doi.org/10.3390/rs14246398. 

- Zou, X., Zhai, P., Zhang, Q., 2005. Variations in droughts over China: 1951–2003. Geophys. Res. Lett. 32 (4), L04707. https://doi.org/10.1029/2004GL021853. 

Zou, X.K., Chen, Y., Liu, Q.F., Sun, J.M., 2008. Overview of the climate in China in 2007. Meteorol. Mon. 34 (4), 118–123 (in Chinese). 

Zubair, M., Zafar, Z., Yao, S., Guo, Z., Nadeem, A.A., Fahd, S., 2025. Agricultural drought forecasting using remote sensing: A hybrid modeling framework by integrating wavelet transformation and machine learning techniques. Agric. Water Manag. 321, 109922. https://doi.org/10.1016/j.agwat.2025.109922. 

25 

