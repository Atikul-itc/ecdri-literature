

# **Rapid #: -27622117** 

CROSS REF ID: **896744** 

LENDER: **CS1 (Calif State Univ., San Marcos) :: Main Library** 

BORROWER: **IRU (New Mexico State University) :: Main Library** 

TYPE: Article CC:CCG JOURNAL TITLE: Remote sensing of environment USER JOURNAL TITLE: Remote sensing of environment. ARTICLE TITLE: The high spatial resolution Drought Response Index (HiDRI): An integrated framework for monitoring vegetation drought with remote sensing, deep learning, and spatiotemporal fusion ARTICLE AUTHOR: , Xu Zhenheng VOLUME: 312 ISSUE: MONTH: 10 YEAR: 2024 PAGES: 114324 ISSN: 0034-4257 OCLC #: 39148295 Processed by RapidX: 10/5/2026 12:27:41 PM 

This material may be protected by copyright law (Title 17 U.S. Code) 

Remote Sensing of Environment 312 (2024) 114324 



Contents lists available at ScienceDirect 

## Remote Sensing of Environment 

journal homepage: www.elsevier.com/locate/rse 



The high spatial resolution Drought Response Index (HiDRI): An integrated framework for monitoring vegetation drought with remote sensing, deep learning, and spatiotemporal fusion 



Zhenheng Xu , Hao Sun<sup>*</sup> , Tian Zhang , Huanyu Xu , Dan Wu , JinHua Gao 

_College of Geoscience and Surveying Engineering, China University of Mining and Technology-Beijing, Beijing 100083, China_ 

|A R T I C L E I N F O|A B S T R A C T|
|---|---|
|Edited by Jing M. Chen|Drought is a complex and extremely destructive natural disaster that seriously threatens the sustainable devel-<br>opment of human society and ecosystems. The integrated drought index with remote sensing offers an efficient|
|_Keywords:_<br>Integrated drought monitoring<br>Remote sensing<br>Spatiotemporal fusion<br>Deep learning<br>Field scale|i<br>approach for drought monitoring and assessment, and has become one of the main trends in drought monitoring<br>research. The existing integrated drought indices are generally used to monitor drought conditions at the na-<br>tional scale, with a spatial resolution of 500 m - 1 km. However, this resolution is still too coarse for farmland,<br>unable to capture the spatial heterogeneity of drought stress at a finer field scale (such as 30 m × 30 m), and<br>cannot meet the needs of field-scale drought monitoring such as refined agricultural water resources manage-<br>ment and drought loss assessment. Therefore, this paper proposes an integrated framework for monitoring<br>vegetation drought at the field scale, which integrates spatiotemporal fusion, deep learning, remote sensing, in-<br>situ stations, and biophysical information. First, the framework established a classification system of drought<br>factors based on the disaster system theory, including vegetation condition, drought-pregnant environment and<br>drought-inducing factors. Second, the dense time series of 30 m monthly vegetation conditions (greenness,<br>moisture, temperature) from 2001 to 2014 were generated based on spatiotemporal fusion. The monthly<br>anomalies were calculated and then integrated based on 3D Euclidean distance method to generate the 30 m<br>Vegetation Condition Anomaly Index (VCAI). Then, the drought-pregnant environment and drought-inducing<br>factors were integrated through deep learning to generate the 30 m Environmental Drought-Inducing Index<br>(EDII). Finally, the joint cumulative distribution was used to couple VCAI and EDII, and the 30 m High spatial<br>resolution Drought Response Index (HiDRI) was generated. Results showed that the comparative analysis of<br>HiDRI with in-situ Standardized Precipitation Evapotranspiration Index (SPEI), meteorological reanalysis data<br>and remote sensing soil moisture data performed well. The overall Pearson correlation coefficient between HiDRI<br>and in-situ SPEI was 0.601 (_p <_ 0.01). Meanwhile, HiDRI can effectively map 30 m × 30 m field-scale drought<br>spatial patterns in different climate zones, including heterogeneous spatial distribution and detailed texture<br>features. In addition, the generated results of spatiotemporal fusion and deep learning have been effectively<br>verified.|



### **1. Introduction** 

Drought is a complex and extremely destructive natural disaster. The complexity of drought is reflected in its multi-scale water-energy cycling process, and involves multiple characteristics of multiple objects such as vegetation, atmosphere, and soil (Hao and Singh, 2015; Vicente-Serrano et al., 2020). The destructiveness of drought is directly reflected in crop failure and water shortage, causing serious damage to the economy and 

ecology (Dai, 2011). With global climate change, the duration and impact of droughts are increasing (Naumann et al., 2021; Su et al., 2018), threatening the sustainable development of human society and ecosystems. Therefore, reliable drought monitoring is necessary and urgent. It can provide timely and effective information to help farmers or government departments take reasonable measures to reduce losses and risks caused by drought (Park et al., 2016; Rahmati et al., 2020). Traditional drought monitoring is mostly based on in-situ 

* Corresponding author at: College of Geoscience and Surveying Engineering, China University of Mining and Technology - Beijing, Ding No.11 Xueyuan Road, Haidian District, Beijing 100083, PR China. 

_E-mail address:_ sunhao@cumtb.edu.cn (H. Sun). 

https://doi.org/10.1016/j.rse.2024.114324 Received 3 February 2024; Received in revised form 26 June 2024; Accepted 20 July 2024 Available online 24 July 2024 

0034-4257/© 2024 Elsevier Inc. All rights are reserved, including those for text and data mining, AI training, and similar technologies. 

_Remote Sensing of Environment 312 (2024) 114324_ 

#### _Z. Xu et al._ 

meteorological data measured at ground stations to establish drought indices (Zhang et al., 2019), such as Palmer Drought Severity Index (PDSI) (Palmer, 1965), etc. However, the ground stations are sparsely and unevenly distributed in space, making it difficult to describe the detailed drought spatial characteristics (Feng et al., 2019; Hao et al., 2015). Remote sensing has the advantage of large-scale continuous earth observation, breaking through the limitations of traditional ground station monitoring in spatial description (Xu et al., 2020; Zhang and Jia, 2013). The relatively famous remote sensing-based drought indices include Normalized Difference Vegetation Index (NDVI) (Tucker, 1979), Temperature Condition Index (TCI) (F. N. Kogan, 1995a), Vegetation Health Index (VCI) (F. N. Kogan, 1995b), etc. However, these indices usually only reflect a certain aspect of the complex drought process and can not reflect the comprehensive characteristics of drought (Jiao et al., 2021a; Shen et al., 2019). 

As remote sensing technology matures, data suitable for drought monitoring is becoming more abundant (AghaKouchak et al., 2015). It is technically possible to use multi-source data to comprehensively monitor drought, and to integrate remote sensing into drought monitoring (West et al., 2019). Integrated drought monitoring refers to the consideration of vegetation status, soil moisture, precipitation, topography, land cover and other characteristics when drought occurs, and the integration of various remote sensing, in-situ stations and geospatial information data to conduct accurate and continuous large-scale drought monitoring. The most representative work is the Vegetation Drought Response Index (VegDRI) proposed by Brown et al. (2008). The VegDRI used data-driven technology to integrate vegetation status observed by remote sensing, meteorological data measured by ground stations, and biophysical information to achieve near-real-time drought monitoring with a spatial resolution of 1 km. The VegDRI can conduct effective drought monitoring at the national scale. It was initially used to assess the drought situation in the United States, and later localized to 

other countries, such as VegDRI-Canada (Tadesse et al., 2017). In order to more effectively monitor shorter-term drought and detect flash drought events, the Earth Resources Observation and Science (EROS) Center built the Quick Drought Response Index (QuickDRI) based on an analogous framework, with a spatial resolution of 1 km. Xu et al. (2023) improved the data-driven method in the QuickDRI, effectively improving the model accuracy and increasing the spatial resolution to 500 m. Since the publication of VegDRI, many integrated drought indices have been proposed. We summarized the representative integrated drought indices in the last 15 years, as shown in Table 1. 

The existing integrated drought indices are generally used to evaluate drought conditions at the national scale, with a spatial resolution of 500 m - 1 km. However, this resolution is still too coarse for farmland, as a single pixel may contain different vegetation types and land covers (Zhou et al., 2020). At the more refined field scale, the spatial heterogeneity of vegetation conditions and topographic environment is objective, which will lead to spatial variations of drought stress. The spatial resolution of the existing integrated drought indices still cannot meet the needs of drought monitoring at the field scale. The existing methods for drought assessment at the field scale still focus on a certain aspect of the drought process, such as vegetation temperature (Zhou et al., 2020), evapotranspiration (Yang et al., 2021), soil moisture (Abowarda et al., 2021; Vergopolan et al., 2020), phenological information (Gao et al., 2017), etc., and cannot comprehensively evaluate the drought conditions at the field scale. There is still a lack of a technical framework for integrated drought monitoring at the field scale. Effective integrated drought monitoring at the field scale will help refine agricultural water resources management, drought emergency management, and drought loss compensation. 

Therefore, this paper proposes an integrated framework for monitoring vegetation drought with fine spatial resolution at the field scale, named High spatial resolution Drought Response Index (HiDRI). The 

**Table 1** 

Summary of integrated drought indices for monitoring vegetation drought and their spatial resolution in the past 15 years. 

|Index|Abbreviation|Spatial<br>resolution|Study area|Drought factors|Reference(s)|
|---|---|---|---|---|---|
|Vegetation Drought<br>Response Index|VegDRI|1 km|United States|Vegetation greenness, Vegetation phenology, Biophysical data<br>(LULC, AWC, Irrigation, Ecoregion), In-situ meteorological data<br>(Precipitation, Temperature)|(Brown et al., 2008)|
|Scaled Drought Condition<br>Index|SDCI|1 km|United States|Vegetation greenness, LST, Precipitation|(Rhee et al., 2010)|
|Synthesized Drought Index|SDI|1 km|China|Vegetation greenness, LST, Precipitation|(Du et al., 2013)|
|Integrated Surface<br>Drought Index|ISDI|1 km|China|Vegetation greenness, Vegetation phenology, LST, Biophysical data<br>(LULC, AWC, Irrigation, Ecoregion, Elevation), In-situ<br>meteorological data (Precipitation, Temperature)|(Wu et al., 2013, 2015)|
|Optimized Vegetation<br>Drought Index|OVDI|1 km|China|Vegetation greenness, LST, Precipitation, Soil moisture|(Hao et al., 2015)|
|Vegetation Drought<br>Response Index for<br>Canada|VegDRI-<br>Canada|1 km|Canada|Vegetation greenness, Vegetation phenology, Biophysical data<br>(LULC, AWC, Irrigation, Ecoregion, Elevation), In-situ<br>meteorological data (Precipitation, Temperature)|(Tadesse et al., 2017)|
|Quick Drought Response<br>Index|QuickDRI|1 km|United States|Vegetation greenness, Vegetation phenology, Soil moisture,<br>Evapotranspiration, Biophysical data (LULC, AWC, Irrigation,<br>Ecoregion, Elevation), In-situ meteorological data (Precipitation,<br>Temperature)|(Earth Resources<br>Observation and Science<br>EROS Center, 2018)|
|Optimal Scaled Drought<br>Condition Index|OSDCI|0.05<sup>◦</sup>|Central Asia|Vegetation greenness, LST, Precipitation|(Guo et al., 2019)|
|Geographically<br>Independent Integrated<br>Drought Index|GIIDI|500 m|United States|Vegetation greenness, LST, Precipitation, Soil moisture|(Jiao et al., 2019)|
|Vector Projection Index of<br>Drought|VPID|500 m|United States<br>and East Asia|Vegetation greenness, LAI, LST, Precipitation, Soil moisture,<br>Evapotranspiration, Climate zone, In-situ meteorological data<br>(Precipitation, Temperature)|(Son et al., 2021)|
|Type Response-Aided<br>Drought Index|TRADI|500 m|United States|Vegetation greenness, LST, Precipitation, Soil moisture, LULC, In-<br>situ meteorological data (Precipitation, Temperature)|(Yin and Zhang, 2023)|
|Quick Drought Response<br>Index for China|QuickDRI-<br>China|500 m|China|Vegetation greenness, Vegetation phenology, Soil moisture,<br>Evapotranspiration, Biophysical data (LULC, AWC, Irrigation,<br>Ecoregion, Elevation), In-situ meteorological data (Precipitation,<br>Temperature)|(Xu et al., 2023)|



Note: LST, Land Surface Temperature; LULC, Land use/Land cover; AWC, Available Water Capacity, LAI: Leaf Area Index. 

2 

_Z. Xu et al._ 

_Remote Sensing of Environment 312 (2024) 114324_ 

technical features of the framework are as follows: 

- (1) The classification system of drought factors from the perspective of disaster system (Shi, 2019; Shi et al., 2020). According to the three elements of disaster-bearing body, disaster-pregnant environment and disaster-inducing factors in the disaster system theory (Gao et al., 2023), this integrated framework establishes a classification system of drought factors, including vegetation condition, drought-pregnant environment and drought-inducing factors. This has more practical theoretical significance than the usual classification system from the perspective of data types. Among them, vegetation condition includes vegetation greenness, moisture, temperature; drought-pregnant environment includes land cover, available water capacity, elevation, etc.; drought-inducing factors include precipitation, evapotranspiration, soil moisture. 

- (2) High spatial resolution Vegetation Condition Anomaly Index (VCAI) generation based on spatiotemporal fusion and Euclidean distance. Vegetation is the direct bearing body of drought and the monitoring target of this framework. Therefore, dense time series and fine spatial resolution surface vegetation conditions guarantee the reliability of drought monitoring. However, due to the long revisit period of high-resolution sensors and the frequent occurrence of atmospheric pollution such as cloud shadows, the available image data is limited, making it difficult to meet the requirements for dense time series for drought monitoring. Therefore, we introduced the spatiotemporal fusion technology Enhanced Spatial and Temporal Adaptive Reflectance Fusion Model (ESTARFM) (Zhu et al., 2010) in the framework to generate dense time series of surface reflectance and temperature data, and then retrieved high spatial resolution vegetation condition factors. Finally, the VCAI is generated through the threedimensional (3D) Euclidean distance method based on the vegetation conditions. 

- (3) High spatial resolution Environmental Drought-Inducing Index (EDII) generation based on deep learning. Drought-inducing factors and drought-pregnant environment are closely related. The framework integrates drought-causing factors and droughtpregnant environment by using the advanced deep learning method Entity Embedding Deep Neural Network (EEDNN) (Guo and Berkhahn, 2016) to generate high spatial resolution EDII. Deep learning has strong nonlinear learning capabilities (Yuan et al., 2020), and EEDNN has been proven to be suitable for heterogeneous drought feature fusion (Xu et al., 2023). 

- (4) Coupling strategy based on joint cumulative distribution. The multivariate cumulative distribution function Copula is used to couple VCAI and EDII to generate the final integrated drought index. VCAI and EDII are generated based on different strategies. The former mainly relies on physical methods, while the latter relies on data-driven methods. Copula can effectively couple the two strategies to maximize their respective advantages and comprehensively monitoring vegetation drought. 

- (5) The application and expansion of the integrated framework. This framework enables near-real-time drought monitoring, and in order to facilitate implementation in other regions of the world, we tried to select global public datasets. In addition, the highresolution reference images used in this study were the Landsat, and a 30 m integrated drought index was finally established. However, with the development of satellite sensors with higher spatial resolutions for surface reflectance and land surface temperature, this framework can also be used to guide the production of higher spatial resolutions of integrated drought indices in theory. 

### **2. Materials and methods** 

### _2.1. Study area_ 

The study area (Fig. 1) is the North China Plain (NCP), located at 32<sup>◦</sup> 10′ N - 40<sup>◦</sup> 38′ N, and 112<sup>◦</sup> 84′ E - 122<sup>◦</sup> 50′ E, with an area of approximately 400 thousand square kilometers (Wang et al., 2023). The NCP is one of the most densely populated regions in the world, with a total population of about 400 million people (Kang and Eltahir, 2018). It is also one of the important agricultural regions in China, producing wheat, corn, soybeans, peanuts, cotton, and various vegetables (Li and Lei, 2021). The NCP is a typical temperate monsoon climate zone. Climate change and the instability of the monsoon lead to frequent drought disasters (Mo et al., 2017), which seriously limits agricultural production and economic development. Refined drought monitoring is necessary. 

### _2.2. Data sets_ 

### _2.2.1. In-situ data_ 

The ground station data used in this study are temperature and precipitation data, which were used to calculate the data-driven dependent variable Standardized Precipitation Evapotranspiration Index (SPEI, 1-month scale) (Vicente-Serrano et al., 2010) and for comparative analysis of the constructed drought indices. The meteorological station data were from the Daily meteorological dataset of basic meteorological elements of China National Surface Weather Station dataset provided by the National Tibet Plateau Data Center (TPDC; http s://data.tpdc.ac.cn), which covers _>_ 2000 national stations in China from 1951 to 2014. This study used 159 effective national stations (Fig. 1) in the North China Plain region, with a time scale of 1985–2014 (30 years). Firstly, the monthly average temperature and monthly accumulated precipitation were calculated based on the daily meteorological data, and the months with _>_ 10 days of missing data in a single month were removed. Then, based on the monthly average temperature, the potential evapotranspiration was generated using the Thornthwaite method (Thornthwaite, 1948). Finally, the monthly SPEI were produced by the long time series of monthly potential evapotranspiration and accumulated precipitation. The calculation of SPEI used the R language package developed by Spanish National Research Council (CSIC) specifically for calculating SPEI. 

### _2.2.2. Vegetation condition data_ 

Vegetation is the direct bearing body of drought. When drought stress occurs, the vegetation condition will change significantly (Sun et al., 2023). In the study, vegetation condition factors include vegetation greenness, moisture and temperature. Vegetation greenness was represented by NDVI, vegetation moisture was represented by Normalized Difference Moisture Index (NDMI) (Jin and Sader, 2005), and vegetation temperature was approximated by LST (Sun et al., 2023). Then, the anomalies of the three were calculated respectively. 

_2.2.2.1. Surface reflectance data._ Surface reflectance products were used to calculate NDVI and NDMI. Two surface reflectance products were involved in the study, one was the Landsat 5 TM and Landsat 8 OLI products with a fine spatial resolution of 30 m, and the other was the MOD09GA Version 6.1 product with a coarse spatial resolution of 500 m. Both Landsat 5 TM and Landsat 8 OLI surface reflectance products have been atmospherically corrected. The former is produced by the Landsat Ecosystem Disturbance Adaptive Processing System (LEDAPS) algorithm (version 3.4.0) (Masek et al., 2006; Schmidt et al., 2013), with a time scale of 1984–2012; the latter is produced by the Land Surface Reflectance Code (LaSRC) (Version 1.5.0) (Vermote et al., 2016), with a time scale of 2013 to present. The reason why the Landsat 7 ETM+ reflectance product was not used is because of the gap pixels in the 

3 

_Z. Xu et al._ 

_Remote Sensing of Environment 312 (2024) 114324_ 



**Fig. 1.** The distribution of 159 national weather stations in the North China Plain and the land cover types in the study area. The climate zones of the North China Plain are divided based on the aridity index. 

images caused by the failure of the scan-line corrector (Chen et al., 2011). The image level of Landsat surface reflectance products used in the study were all Tier 1. A total of 27 Landsat scenes in Worldwide Reference System are covered in the North China Plain, these scenes are retrieved through Path and Row numbers. The clear sky data from 2001 to 2014 were selected (cloud cover = 0) for each Landsat scenes. The data from 2001 to 2012 used Landsat 5 TM, and the data from 2013 to 2014 used Landsat 8 OLI. The MOD09GA product, which is the data source for many MODIS land products, has been atmospheric corrected and provides global surface reflectance estimates from 2000 to the present (Vermote and Wolfe, 2015). In the study, the surface reflectance data of MOD09GA under clear sky conditions in the North China Plain area from 2001 to 2014 were selected. All the filtering and downloading steps were implemented based on Google Earth Engine (GEE) (Gorelick et al., 2017). 

_2.2.2.2. Land surface temperature data._ Land surface temperature data was used to approximately represent vegetation temperature and calculate vegetation temperature anomaly (Sun et al., 2023). The land surface temperature products involved in the study include Landsat 5 with a spatial resolution of 120 m, Landsat 8 with a spatial resolution of 100 m, and MOD11A1 product with a spatial resolution of 1 km. Landsat 5 and Landsat 8 surface temperature products are generated using the Landsat surface temperature algorithm (Version 1.3.0) (Cook et al., 2014). MOD11A1 provides global land surface temperature and emissivity estimates from 2000 to the present (Wan et al., 2015). In the study, the process of filtering and downloading the land surface temperature data under clear sky conditions was the same as that of the surface reflectance products. 

### _2.2.3. Drought-pregnant environment_ 

The drought-pregnant environment refers to the long-term stable environment formed by the inherent natural environment of the 

ecosystem and the changes caused by human activities to the natural environment (Gao et al., 2023). The drought-pregnant environment is an important factor in determining the drought resistance of an ecosystem (Roodposhti et al., 2017). The drought-pregnant environment factors used in the study include: Elevation, Land Cover, Irrigated Agriculture (IrrAg), Available Water Capacity (AWC), and Ecoregion. 

_2.2.3.1. Elevation._ Different elevations will directly affect the temperature of the vegetation growth environment, which may lead to changes in the growth phenology of the same type of vegetation. The elevation product used in the study was the Shuttle Radar Topography Mission (SRTM) Digital Elevation Data V003 (Farr et al., 2007), which is provided by the NASA Jet Propulsion Laboratory (JPL) with a spatial resolution of about 30 m. 

_2.2.3.2. Land cover._ Different land cover types represent different ecosystem environments, which may lead to differences in drought response states of vegetation. The land cover data used in the study was the annual China land cover dataset (CLCD), with a spatial resolution of 30 m. This dataset was based on _>_ 300,000 Landsat images from the GEE platform and was generated using a random forest classifier (Yang and Huang, 2021). 

_2.2.3.3. Irrigated agriculture._ Irrigated agricultural lands need to be distinguished from rainfed lands, as farmland systems with good irrigation are less susceptible to drought stress. IrrAg is the proportion of irrigated cropland to the all cropland, and represents the average level of farmland irrigation in a certain regional unit (Brown et al., 2008). In the study, the municipal administrative regions of China were used as the regional units for the IrrAg calculation. For a certain regional unit, the IrrAg was allocated to every pixel whose cover type is farmland, and non-farmland pixels were set to 0. The farmland area data comes from the provincial and municipal statistical bureaus (Anhui, Beijing, Hebei, 

4 

_Z. Xu et al._ 

_Remote Sensing of Environment 312 (2024) 114324_ 

Henan, Jiangsu, Shandong, Tianjin) in the North China Plain, and the land cover data is CLCD. Finally, the 30 m IrrAg maps from 2001 to 2014 were produced. 

_2.2.3.4. Available water capacity._ Available water capacity (AWC) represents the potential of soil to retain plant-available water, which will affect the sensitivity of vegetation to drought stress. The AWC data used in the study was SoilGrids250m (Hengl et al., 2017). This dataset is provided by International Soil Reference and Information Center (ISRIC) with a spatial resolution of 250 m. This dataset is based on the global compilation of soil ground observations and generates AWC up to the wilting point at different standard depths. AWC at a standard depth of 2 m was used in the study. 

_2.2.3.5. Ecoregion._ Ecoregions represent plant communities with different characteristics, and the RESOLVE Ecoregions dataset with global ecoregions (Dinerstein et al., 2017) was used in the study. 

_2.2.4. Drought-inducing factors_ 

Drought-inducing factors are the direct causes of drought, and the drought-inducing factors in the study include Standardized Precipitation Index (SPI), Evaporative Stress Index (ESI), and Soil Moisture Anomaly (SMA). 

_2.2.4.1. Standardized precipitation index._ SPI (McKee et al., 1993) is an effective indicator to characterize precipitation anomalies. In this study, the 1-month scale SPI from 2001 to 2014 were generated based on the fifth generation of European ReAnalysis (ERA5-land; https://cds.cli mate.copernicus.eu/) (Munoz˜ Sabater, 2019) total precipitation data. ERA5-land provides global land variables estimates with a spatial resolution of 0.1<sup>◦</sup> from 1950 to the present. The hourly data was used and aggregated (sum or average) to generate monthly data, the same for ESI and SMA. 

_2.2.4.2. Evaporative stress index._ ESI is used to describe temporal anomalies in evapotranspiration (Anderson et al., 2011), which can effectively reveal the stress of vegetation due to water shortage. ESI does not rely on precipitation data and is mainly based on land surface temperature from satellite observations to estimate water loss due to evapotranspiration. The monthly ESI were generated based on the ERA5-land potential evaporation and total evaporation data. 

_2.2.4.3. Soil moisture anomaly._ SMA represents the soil moisture deviation over a certain period from the historical average for the same time (Gao et al., 2016). In this study, the monthly SMA from 2001 to 2014 was calculated based on the summed soil moisture data from 0 to 100 cm (volumetric soil water layer 1/2/3) in the ERA5-land. 

### _2.2.5. Comparative analysis data_ 

_2.2.5.1. Meteorological reanalysis data._ In addition to using the in-situ SPEI for comparative analysis of HiDRI, the SPEIs calculated based on meteorological reanalysis data were also used for comparison (Peng et al., 2020; Pyarali et al., 2022). The 1-month scale SPEIs were calculated by the precipitation and potential evapotranspiration raster data of two widely used long time-series meteorological datasets such as the Climatic Research Unit gridded Time Series (CRU TS; https://crudata. uea.ac.uk/cru/data/hrg/) (Harris et al., 2020), and the TerraClimate (https://www.climatologylab.org/terraclimate.html) (Abatzoglou et al., 2018). The long time-series raster data obtained from these datasets are all from January 1985 to December 2014, a total of 30 years, which is the same as the time series of the in-situ SPEI in the study. 

_2.2.5.2. Remote sensing soil moisture data._ The European Space Agency Climate Change Initiative (ESA CCI; https://climate.esa.int) remote 

sensing soil moisture dataset (Dorigo et al., 2017; Gruber et al., 2019; Preimesberger et al., 2021) was used for comparative analysis of HiDRI in the study. This dataset provides soil moisture data from 1978 to 2022. Among them, the PASSIVE product from 2001 to 2014 was used. The daily data was first averaged monthly, and the monthly SMA was calculated. 

_2.2.5.3. Aridity index._ To compare the drought monitoring effect of HiDRI under different dryness of the climate (Jiao et al., 2021b; Zomer et al., 2008), the climate zones of the North China Plain were divided based on the aridity index (AI) (United Nations Environment Programme, 1997). The calculation formula of the AI is as follows: 

### <u>∑30i=1</u> PETPi i <u>( )</u> AI = 

### 30 

In the formula, _i_ represents the _ith_ year, _P_ represents the annual precipitation, and _PET_ represents the annual potential evapotranspiration. In the study, the CRU TS dataset from 1985 to 2014 was used to calculate the AI. It can be divided into different climate zones according to the AI values: 0 _._ 05 ≤ _AI <_ 0 _._ 2 is arid climate, 0 _._ 2 ≤ _AI <_ 0 _._ 5 is semiarid climate, 0 _._ 5 ≤ _AI <_ 0 _._ 65 is dry subhumid climate, and _AI_ ≥ 0 _._ 65 is humid climate. The climate zones included in the North China Plain are semi-arid, dry subhumid, and humid. 

### _2.3. Methodology_ 

The technical flowchart of this study is shown in Fig. 2. It is divided into three major parts: (a) The 30 m Vegetation Condition Anomaly Index (VCAI) was generated to characterize vegetation drought. (b) The 30 m Environmental Drought-Inducing Index (EDII) was generated to characterize environmental and meteorological drought. (c) The 30 m integrated drought index (HiDRI) was generated by coupling VCAI and EDII based on the joint cumulative distribution function. The specific steps are as follows: 

(1) Based on the Landsat Surface Reflectance product and the MOD09GA product, the spatiotemporal fusion was used to generate monthly 30 m spatial resolution surface reflectance data from 2001 to 2014. (2) Based on the Landsat LST product and the MOD11A1 product, the spatiotemporal fusion and the high-resolution urban thermal sharpener (HUTS) (Dominguez et al., 2011) were used to generate monthly 30 m spatial resolution LST from 2001 to 2014. (3) The vegetation condition anomalies were calculated by the monthly 30 m surface reflectance and LST. (4) Vegetation condition anomalies were integrated using the 3D Euclidean distance method to generate the 30 m VCAI. (5) The drought-pregnant environment and drought-inducing factors were calculated and processed. (6) Based on the advanced deep learning method EEDNN, the drought-pregnant environment and droughtinducing factors were data-driven to generate the 30 m EDII. (7) The joint cumulative distribution of EDII and VCAI was modeling by the copula function. (8) The 30 m HiDRI was generated based on the inverse normal of the joint cumulative distribution. 

### _2.3.1. Vegetation condition anomaly index_ 

_2.3.1.1. Spatiotemporal fusion._ Landsat satellites provide remote sensing images with fine spatial resolution. However, due to the long satellite revisit period (16 days) and the frequent occurrence of clouds, cloud shadows and other atmospheric pollution, many areas often do not have available clear sky data (Ju and Roy, 2008), making it impossible to support large-scale long-time-series of monthly fine spatial resolution drought monitoring. Spatiotemporal fusion of remote sensing data is an effective method to solve this problem. Spatiotemporal fusion refers to the fusion of low-temporal and fine-spatial resolution sensor data with high-temporal and coarse-spatial resolution sensor data, in order to 

5 

_Z. Xu et al._ 

_Remote Sensing of Environment 312 (2024) 114324_ 



**Fig. 2.** The technical flowchart for generating 30 m High spatial resolution Drought Response Index (HiDRI). ESTARFM, Enhanced Spatial and Temporal Adaptive Reflectance Fusion Model; HUTS, High-resolution Urban Thermal Sharpener; NDVI, Normalized Difference Vegetation Index; NDMI, Normalized Difference Moisture Index; LST, Land Surface Temperature; LULC, Land use and Land cover; IrrAg, Irrigated Agriculture; AWC, Available Water Capacity; SPI, Standardized Precipitation Index; ESI, Evaporative Stress Index; SMA, Soil Moisture Anomaly; SPEI, Standardized Precipitation Evapotranspiration Index. 

generate fine-spatial resolution remote sensing data with dense time series that meets the needs (Zhu et al., 2018). The spatiotemporal fusion algorithm used in this study was the ESTARFM proposed by Zhu et al. (2010). This algorithm is one of the most widely used spatiotemporal fusion algorithms and has demonstrated significant application efficacy in many downscaling studies of drought factors (Abowarda et al., 2021; Gao et al., 2015; Long et al., 2020; Ma et al., 2018; Zhou et al., 2020). 

ESTARFM needs to acquire two input image pairs of coarse and fine spatial resolution with the same date, and a coarse spatial resolution image for a specific time period or date used in the prediction. This algorithm predicts the fine spatial resolution image for a specific time period or date by searching for similar pixels, calculating similar pixel weights, and the conversion coefficients between coarse and fine spatial resolutions. In the study, monthly surface reflectance and LST data with 30 m spatial resolution from 2001 to 2014 were generated based on the ESTARFM algorithm. The specific generation processes are as follows. 

The generation process of 30 m surface reflectance: The fine spatial resolution input images were Landsat surface reflectance images under clear sky conditions. The clear-sky images were selected using the “cloud cover” band in the Landsat product, which provides an estimate of the percentage of cloud coverage in the entire image, determined by the C Function of Mask (CFMask) algorithm (Foga et al., 2017). The filter 

condition was set to cloud cover _<_ 0.5%. The coarse spatial resolution images were MOD09GA images under clear sky conditions. The reflectance data state QA band “state_1km” was used to select the MOD09GA clear sky data, and the pixels covered by clouds, cloud shadows and snow were removed. Firstly, the clear sky MOD09GA data with the same date and spatial range as the Landsat surface reflectance images were selected as the coarse spatial resolution images in the input image pairs. Then, the monthly average data of MOD09GA after cloud removal (a total of 168 months from 2001 to 2014) were calculated as the coarse spatial resolution images used in the prediction. 

The generation process of 30 m LST: The spatial resolutions of Landsat 5 and Landsat 8 land surface temperature products are 120 m and 100 m respectively. In order to obtain LST with 30 m spatial resolution as the input images for spatiotemporal fusion, the HUTS algorithm was used to downscale the 120/100 m LST product under clear sky conditions to 30 m. Based on the assumption of scale invariance, the HUTS algorithm established the polynomial relationship between NDVI, albedo and LST at 120/100 m spatial resolution, and then predicted the 30 m enhanced LST through NDVI and albedo at 30 m spatial resolution. Among them, the calculation of NDVI was based on the red band and near-infrared band of Landsat surface reflectance data under clear sky conditions (Tucker, 1979), and the calculation of albedo was based on 

6 

_Z. Xu et al._ 

_Remote Sensing of Environment 312 (2024) 114324_ 

the method proposed by Liang (2001). The coarse spatial resolution LST images were MOD11A1 data under clear sky conditions. The processing of MOD11A1 was similar to that of MOD09GA. Firstly, the clear sky MOD11A1 data with the same date and spatial range as the Landsat enhanced LST images were selected as the coarse spatial resolution images in the input image pairs. Then, the monthly average data of MOD11A1 after cloud removal were calculated as the coarse spatial resolution images used in the prediction. 

_2.3.1.2. Vegetation condition anomaly._ Based on the 30 m surface reflectance and LST data generated by spatiotemporal fusion, the anomalies of vegetation greenness, moisture and temperature in each month from 2001 to 2014 were calculated. The calculation formula is _VA_ = ( _VC_ − _VCμ_ ) _/VCσ_ . In the formula, _VA_ is the vegetation condition anomaly in a certain month, _VC_ is the vegetation condition (NDVI, NDMI, LST) at the same time, _VCμ_ is the average of the vegetation condition of that month from 2001 to 2014, and _VCσ_ is the standard deviation of the vegetation condition of that month from 2001 to 2014. 

_2.3.1.3. Three-dimensional (3D) Euclidean distance method._ The Euclidean distance can quantitatively characterize the correlation between variables and has practical physical significance. Therefore, it is widely used in geographical research including drought monitoring. Wei et al. (2020) established the Temperature Vegetation Precipitation Dryness Index by constructing a 3D space of precipitation, NDVI and LST. In this study, a 3D space was constructed based on the vegetation temperature anomaly (VTA), vegetation greenness anomaly (VGA) and vegetation moisture anomaly (VMA). The VCAI was calculated by the 3D Euclidean distance, and the formula is as follows: 

### VCAI = √(VTAmax − VTA)<sup>2</sup> + (VGA − VGAmin)<sup>2</sup> + (VMA − VMAmin)<sup>2</sup> 

Because the anomaly calculation is z-score, the vegetation condition anomalies are normally distributed, and most of the values are between − 3 and 3. Theoretically, the coordinate of the driest reference point in 3D space is (3,− 3,− 3), and the coordinate of the wettest reference point is (− 3,3,3). The driest point represents the highest vegetation temperature anomaly, and the lowest vegetation greenness and moisture anomalies. The VCAI at the driest point is 0, at the wettest point is 6√3. When the vegetation condition anomalies are all equal to 0, the VCAI is equal to 3√3, which corresponds to the middle value of the range. Therefore, the value range of VCAI is (0, 6√3), and the smaller the value, the drier it is. When VCAI is _<_ 3√3, it is considered that the vegetation may be under drought stress. 

### _2.3.2. Environmental drought-inducing index_ 

_2.3.2.1. Generation of drought factors dataset._ The drought-pregnant environment factors in each year and the drought-inducing factors in each month from 2001 to 2014 were processed and generated based on the corresponding original data. The drought factors with coarse spatial resolutions such as SPI, SMA, ESI, and AWC were resampled to 30 m using the bilinear method. 

Based on 159 effective meteorological stations in the North China Plain, the values of drought-pregnant environment and droughtinducing factors in each month from 2001 to 2014 were extracted at each station location. In order to reduce the random error that may be caused by a single pixel, the extracted value was the average value within a 3 × 3 pixel window centered on the pixel where the station is located. For land cover data, the majority of the land cover types within the 3 × 3 window was taken. All extracted values of a single station in a single month were taken as a sample, and each sample has 8 drought factor variables. Since the extracted values of some drought factors may be null in some months at some stations, the samples with null values were removed. Finally, 20,533 effective sample were obtained. 

_2.3.2.2. Entity embedding deep neural network._ The drought factors were integrated based on the advanced deep learning method EEDNN. It is a deep learning network specially designed to handle heterogeneous multi-source data, which is adapted to the heterogeneous characteristics of drought data (Xu et al., 2023). Because drought data usually contains a variety of continuous and categorical variables, it is a typical heterogeneous multi-source tabular data. The Embedding Layer included in EEDNN can effectively process categorical variables, which can densely compress categorical variables into continuous variables. Compared with traditional categorical variable coding (such as one-hot coding), this dense coding method reduces the dimension of categorical variables, effectively avoiding the dimension redundancy caused by traditional categorical variable coding. At the same time, it can also reveal the internal relationship between different categories of categorical variables, thus improving the speed and accuracy of model training (Guo and Berkhahn, 2016). The structure of EEDNN (Fig. 3) has strong expansibility and flexibility. Rather than a fixed network model, it is a network mode that can effectively handle heterogeneous tabular data. That is, the categorical variables are first densely encoded through the Embedding Layer, and then the dense coding results are connected with the continuous variables, and finally the multi-variable integration is carried out through multiple fully connected layers. Compared with convolutional layers and recurrent neural units, fully connected layers have higher flexibility and generalization ability when dealing with high-dimensional tabular drought data, making it easier to obtain satisfactory training results. 

_2.3.2.3. Hyperparameter tuning._ Hyperparameter tuning is an important step in data-driven models, which directly affects the accuracy of the developed model. In the study, the most important hyperparameters include: the output dimension of dense coding in the Embedding layer, the number of fully connected layers, the neurons number in the fully connected layers, and the regularization. The output dimension of the Embedding layer determines the complexity and effectiveness of categorical variable (LULC, ECO) coding. The neurons number in the fully connected layer determines the integration effect of the model on multiple variables. The regularization is to prevent the model from overfitting. The k-fold cross-validation and Bayesian optimization (Bergstra et al., 2013; Bergstra et al., 2011) were employed for hyperparameter tuning. For each hyperparameters combination, k-fold cross-validation refers to randomly dividing the samples of the training set into k parts according to the stations, and using k-1 of them for model training and the remaining 1 for validation. K-times training and validation are carried out in turn, and the average accuracy of k-times validation is taken as the final accuracy of the hyperparameters combination. In the study, k was set to 5. Then, the hyperparameters combination and its validation accuracy were passed to the Bayesian optimization, which will guide the efficient search of the next hyperparameters combination according to the existing combinations and accuracy, and finally determine the best hyperparameters combination (Table 2). In addition, the activation function used in EEDNN is ReLU( _x_ ) = _max_ (0 _, x_ ). And loss function is MSELoss, the formula is: 



where N is the batch size, _xi_ is the predicted value, _yi_ is the true value. 

### _2.3.3. Coupling to generate HiDRI_ 

_2.3.3.1. Main steps of coupling._ In the study, the EDII and VCAI were coupled based on the Copula function to obtain HiDRI. Copula is a multivariate Cumulative Distribution Function (CDF) that can model the marginal probability distribution of multiple random variables to obtain their joint distribution. The main steps of coupling EDII and VCAI to HiDRI are as follows: (1) According to the distribution of EDII and VCAI, 

7 

_Z. Xu et al._ 

_Remote Sensing of Environment 312 (2024) 114324_ 



**Fig. 3.** The structural diagram of Entity Embedding Deep Neural Network. 

**Table 2** 

EEDNN hyperparameters settings. 

|Hyperparameters|Settings|
|---|---|
|Number of fully connected layers|2|
|Number of neurons in fully connected layer 1|64|
|Number of neurons in fully connected layer 2|8|
|Output dimension of embedding layer LULC|4|
|Output dimension of embedding layer ECO|1|



environmental meteorological drought occurs and the vegetation condition is abnormal can it be more reliably determined that the vegetation is suffering from drought stress. 

In the study, the samples with _EDII <_ 0 and _VCAI <_ 3√3 were statistically analyzed and it was found that most of the coupled HiDRI values were less than − 0.5. Therefore, according to the actual physical meaning, when _HiDRI <_ − 0 _._ 5, it can be considered that the vegetation begins to be stressed by drought, and the smaller the value, the more severe the stress. 

Note: LULC, Land use/Land cover; ECO, Ecoregion. 

the marginal probability density function (PDF) was fitted respectively. Both fits used the Gamma distribution. (2) The CDFs were calculated based on the PDFs. (3) The CDFs were coupled by the Copula function to get the joint CDF. (4) The HiDRI was generated based on the inverse normal of the joint CDF. 

_2.3.3.2. Copula function._ Let EDII and VCAI be X and Y, and the marginal CDF are _u_ 1 = _E_ ( _x_ ) and _u_ 2 = _V_ ( _y_ ) respectively. The joint CDF is _H_ ( _x, y_ ) = _P_ ( _X_ ≤ _x, Y_ ≤ _y_ ). The Copula function _C_ ( _u_ 1 _, u_ 2) is defined as: 

H(x _,_ y) = C(E(x) _,_ V(y) ) = C(u1 _,_ u2) 

_x_ = _E_<sup>−1</sup> ( _u_ 1) _, y_ = _V_<sup>−1</sup> ( _u_ 2) 



Where the _E_<sup>−1</sup> and _V_<sup>−1</sup> are the inverse transform of the marginal CDF. 

Typical Copula functions include Clayton, Frank, Gumbel and Gaussian. The copula function ‘Frank’ was selected in this study based on likelihood method. The probability distribution function of Frank Copula is as follows: 



_2.3.3.3. Drought threshold of HiDRI._ Sometimes, environmental meteorological drought and vegetation condition anomalies may not be synchronized. On the one hand, when the EDII is _<_ 0, it means that environmental meteorological drought has begun, but due to the influence of vegetation type, groundwater and human activities, vegetation drought may be delayed or even not occur. On the other hand, when the VCAI monitors anomalies ( _VCAI <_ 3√3), it is not necessarily caused by drought stress. Some diseases, pests or heavy metal pollution may also cause vegetation condition anomalies. Therefore, only when 

### _2.3.4. Statistical metrics_ 

The main statistical metrics used in the study include the Pearson correlation coefficient R, the Root Mean Square Error (RMSE), the Mean Absolute Error (MAE), the average Bias and the Index of Agreement d. Among them, the RMSE is not only used for the accuracy evaluation, but also as the metrics of k-fold cross-validation. The calculation formulas of the metrics are as follows: 







where _k_ is the number of samples, _Si_ is the true reference value, and _Hi_ is the corresponding predicted value. 

8 

_Z. Xu et al._ 

_Remote Sensing of Environment 312 (2024) 114324_ 

### **3. Results** 

### _3.1. Performance of environmental drought-inducing index (EDII)_ 

Five independent unbiased accuracy evaluations were performed to verify the performance of EDII. For each evaluation, the training set for model development and the test set for accuracy evaluation were split randomly according to the stations, with 80% (127) of the stations used for training and 20% (32) of the stations used for evaluation. The results are shown in Fig. 4. EDII and in-situ SPEI show a strong correlation. The average correlation coefficient is 0.789, the maximum is 0.807 (Fig. 4d), and the minimum is 0.779 (Fig. 4e). The fitting lines of the data points are all close to the 1:1 reference line, the distributions of the data points are symmetrical, and the closer to the 1:1 reference line, the higher the point density. In addition, the indices of agreement are calculated, and the average value is 0.873. This shows a good agreement between EDII and in-situ SPEI, validating the accuracy of EDII predictions. 

To further evaluate the accuracy performance of EDII on time series, among the 32 stations in the test set of Fig. 4(a), the 6 evaluation stations were selected from the semi-arid, dry subhumid, and humid climate zone respectively (2 stations per zone) to compare the time series variation of EDII and in-situ SPEI. The time series ranges from January 2001 to December 2014, a total of 168 months. The selected evaluation station should have no _>_ 10 months of missing data, as some stations may lack data for certain months. For the months with missing data, the average value of the adjacent months was used as a replacement. Finally, the Station 53,697 ( _R_ = 0.73) and Station 54,715 ( _R_ = 0.70) in the semi- 

arid climate zone, the Station 54,846 ( _R_ = 0.78) and Station 57,093 ( _R_ = 0.84) in the dry subhumid climate zone, the Station 54,778 (R = 0.78) and Station58006 ( _R_ = 0.83) in the humid climate zone were selected. The spatial locations of the 6 evaluation stations are shown in Fig. 1, and the time series comparison is shown in Fig. 5. In most months, the time series variation of EDII at the 6 stations are consistent with that of in-situ SPEI, which shows that EDII can effectively capture the temporal variation and trend of drought. 

### _3.2. Performance of vegetation condition anomaly index (VCAI)_ 

The reliability of vegetation condition has an important impact on the accuracy of HiDRI. In order to confirm the spatiotemporal fusion effect of vegetation greenness, moisture and temperature, the ESTARFM spatiotemporal fusion results of NDVI, NDMI and LST within 3 km × 3 km around the Station 54,715 in the semi-arid climate, the Station 57,093 in the dry subhumid climate, and the Station 58,006 in the humid climate were further evaluated. In the study, the ESTARFM spatiotemporal fusion results were monthly average data. Therefore, the month in which there are two clear sky images in a single month around the station location was selected, and the average value image of the two clear sky images was taken as the true value image of NDVI, NDMI, and LST in that month, which was used as the reference data to evaluate the spatiotemporal fusion effect. Among them, the reference data of LST were the Landsat LST enhanced by HUTS. The evaluation month selected by the Station 54,715 was May 2005, the evaluation month selected by the Station 57,093 was June 2006, and the evaluation month 



**Fig. 4.** (a) - (e) are five independent unbiased accuracy evaluations of EDII. Each evaluation is based on the in-situ SPEI of 20% ground stations (random splits) that did not participate in the data-driven. EDII, Environmental Drought-Inducing Index; SPEI, Standardized Precipitation Evapotranspiration Index; R, Pearson correlation coefficient; RMSE, Root Mean Square Error; MAE, Mean Absolute Error. 

9 

_Z. Xu et al._ 

_Remote Sensing of Environment 312 (2024) 114324_ 



**Fig. 5.** Comparison of time series between EDII and the in-situ SPEI at stations in different climate zones. Station 53,697, 54,715 in the semi-arid climate zone, Station 54,846, 57,093 in the dry subhumid climate zone, Station 54,778, 58,006 in the humid climate zone. The distribution location of the stations is shown in Fig. 1. EDII, Environmental Drought-Inducing Index; SPEI, Standardized Precipitation Evapotranspiration Index; R: Pearson correlation coefficient. 

selected by the Station 58,006 was November 2013. The Landsat image dates corresponding to each month are shown in Table 3. 

The Station 54,715 and Station 57,093 can evaluate the spatiotemporal fusion effect of Landsat 5 (2001− 2012), while the Station 58,006 can evaluate the spatiotemporal fusion effect of Landsat 8 (2013–2014). At the same time, the vegetation coverage around these three stations in the evaluation months decreased sequentially (Fig. 6), with the Station 54,715 being the highest, the Station 58,006 s, and the Station 57,093 being the lowest. This can evaluate the spatiotemporal fusion effect under different vegetation coverage conditions. 

The spatiotemporal fusion results of NDVI are shown in Fig. 6. The overall accuracy evaluation metrics (R/RMSE) are 0.94/0.13 (Station 54,715), 0.98/0.06 (Station 57,093), and 0.98/0.09 (Station 58,006), respectively. The average index of agreement is 0.925. In terms of spatial distribution, ESTARFM NDVI was consistent with the true Landsat NDVI, and showed a significant spatial downscaling effect compared 

**Table 3** 

The date information of Landsat images used to evaluate the spatiotemporal fusion effect of vegetation conditions. 

|Station ID|Climate zone|Image date 1|Image date 2|
|---|---|---|---|
|Station 54,715|Semi-arid|2005.05.06|2005.05.22|
|Station 57,093|Dry subhumid|2006.06.10|2006.06.26|
|Station 58,006|Humid|2013.11.13|2013.11.29|



with MODIS image. In terms of spatial attributes, the color vision of ESTARFM NDVI was consistent with that of Landsat NDVI in the vegetation coverage areas, but there was an underestimation in the areas with no/low vegetation coverage. This is also reflected in the scatter plot. The scatter points with high NDVI values are closer to the 1:1 reference line, while the scatter points with NDVI _<_ 0.3 are relatively deviated. However, the impact of this underestimation on vegetation drought monitoring is very limited, because this study is more focused on the drought situation of vegetation, and the reliability of the fusion results of vegetation coverage areas is the key to the accuracy of drought monitoring. 

NDMI shows a similar spatiotemporal fusion effect with NDVI, as shown in Fig. 7. The overall accuracy evaluation metrics (R/RMSE) are 0.96/0.10 (Station 54,715), 0.96/0.05 (Station 57,093), 0.97/0.09 (Station 58,006) respectively. The average index of agreement is 0.931. ESTARFM NDMI was consistent with Landsat NDMI in spatial distribution. The spatiotemporal fusion effect of the vegetation coverage areas was better, and there was a little underestimation in the no/low vegetation coverage areas. 

The spatiotemporal fusion results of LST are shown in Fig. 8. The overall accuracy evaluation metrics (R/RMSE) are: 0.86/2.16 K (Station 54,715), 0.86/2.68 K (Station 57,093), and 0.88/1.51 K (Station 58,006). The average index of agreement is 0.658. Compared with the more stable signals of NDVI and NDMI, LST is more susceptible to the 

10 

_Z. Xu et al._ 

_Remote Sensing of Environment 312 (2024) 114324_ 



**Fig. 6.** The spatiotemporal fusion results of NDVI within 3 km × 3 km around the Station 54,715 in the semi-arid climate, the Station 57,093 in the dry subhumid climate, and the Station 58,006 in the humid climate. From left to right are MOD09GA monthly average NDVI (500 m), true Landsat NDVI (30 m) and spatiotemporal fusion ESTARFM NDVI (30 m). 

change of meteorological conditions, so there is greater uncertainty in spatiotemporal fusion. Although ESTARFM LST is not as accurate as NDVI and NDMI, it still achieved good results, and also showed similar characteristics with Landsat LST in spatial distribution. 

In general, the overall accuracy of the spatiotemporal fusion results of NDVI, NDMI and LST is high, and the spatial distribution of the spatiotemporal fusion results is consistent with that of the true Landsat data. This shows that the ESTARFM spatiotemporal fusion results can be used as a reliable input for the vegetation condition (30 m × 30 m) of HiDRI. 

At the same time, the vegetation greenness anomaly, moisture anomaly, temperature anomaly and the generated VCAI were further evaluated, as shown in Fig. 9. The lower the vegetation greenness anomaly, vegetation moisture anomaly, and VCAI, the drier it is. The higher the vegetation temperature anomaly, the drier it is. The three anomalies and the VCAI show rich texture details and similar spatial distribution, and the monitored dry and wet areas are consistent. This indicates that VCAI can effectively integrate the three anomalies and effectively characterize the spatial heterogeneity of vegetation condition anomalies at the field scale. 

### _3.3. Spatial patterns of HiDRI_ 

In order to explore the ability of HiDRI to characterize spatial details under different dryness of the climate, the spatial distribution patterns of HiDRI within the range of 3 km × 3 km near the Station 54,715 in the semi-arid climate, the Station 57,093 in the dry subhumid climate and 

the Station 58,006 in the humid climate are presented, as shown in Figs. 10, 11 and 12. Drought is considered to have occurred when _HiDRI <_ − 0 _._ 5, and the smaller the value, the drier it is. 

The HiDRI shows obvious spatial heterogeneity at the micro scale, which is particularly prominent among different land cover types (vegetation, bare land). At the same time, HiDRI shows rich texture details, including farmland textures and roads. 

To further analyze the monitoring effect of HiDRI on the evolution of drought, the spatial patterns of months with continuous drought in different climate zones are presented. For the Station 54,715 in the semiarid climate, HiDRI shows that a relief of the drought from July to August 2014. As a validation, the values of in-situ SPEI at the station from July to August were compared, and it was found that the in-situ SPEI increased from − 1.193 to − 0.625, indicating that the drought was indeed alleviated. A similar drought relief occurred from March to April 2006, and the in-situ SPEI increased from − 1.053 to − 0.497. For the Station 57,093 in the dry subhumid climate, HiDRI captured a drought event from September to November 2007 that first alleviated and then intensified. The in-situ SPEI first increased from − 1.250 (September) to − 0.156 (October) and then decreased to − 0.571 (November). For the Station 58,006 in the humid climate, the in-situ SPEI from November 2010 to January 2011 was − 1.398, − 0.886, and − 0.874, respectively. This is consistent with the monitoring of HiDRI, with drought was alleviated from November to December, and the drought condition in December were similar to that in January. The above shows that HiDRI can effectively monitor the changes of drought in different climate zones. 

11 

_Z. Xu et al._ 

_Remote Sensing of Environment 312 (2024) 114324_ 



**Fig. 7.** The spatiotemporal fusion results of NDMI within 3 km × 3 km around the Station 54,715 in the semi-arid climate, the Station 57,093 in the dry subhumid climate, and the Station 58,006 in the humid climate. From left to right are MOD09GA monthly average NDMI (500 m), true Landsat NDMI (30 m) and spatiotemporal fusion ESTARFM NDMI (30 m). 

Overall, HiDRI can effectively map the spatial patterns of drought at the 30 m × 30 m field scale, and can describe the heterogeneous spatial distribution and detailed texture characteristics of drought in different climate zones. 

### _3.4. Comparative analysis of HiDRI with in-situ SPEI_ 

The in-situ SPEI of all stations was used for the comparative analysis of HiDRI, with a total of 20,533 samples, and the results are shown in Fig. 13(a). HiDRI and In-situ SPEI show a strong correlation, with the overall Pearson correlation coefficient _R_ = 0.601 ( _p <_ 0.01). The fitting line of the data points is close to the 1:1 reference line. 

The performance of HiDRI on the spatial variation was further analyzed, the correlation coefficients between HiDRI and in-situ SPEI at all 159 stations were calculated, and 7 stations with _p >_ 0.01 were removed. Then, the correlation coefficients were spatially interpolated using the Empirical Bayesian Kriging method. The result is shown in Fig. 14. The correlation coefficients showed a continuous spatial variation, and there were no extremely prominent outliers. Most areas show a high correlation, with an average R of around 0.6, low-value area around 0.44, and the high-value area reaching around 0.76. 

For different climate zones, the correlations in the dry subhumid climate zone are similar to that in the humid climate zone, and the correlations in the semi-arid climate zone are overall slightly lower. The correlations have a clear boundary between the semi-arid climate zone and dry subhumid climate zone. The possible reason is that precipitation in the semi-arid climate zone is relatively low, and irrigation need to be 

used more regularly to make crops grow normally. The irrigation facilities are more complete, so crops are greatly affected by artificial irrigation. It is worth noting that there is a relatively high correlation in the northern part of the North China Plain (around Beijing) where the Yan Mountains and Taihang Mountains meet. This may be due to the special topography of the area. This area is located on the windward slope of the southeast monsoon in summer. The humid monsoon is blocked by the two mountain ranges and can easily cause heavy rainfall. At the same time, this area is on the leeward slope of dry northwest winds in winter, causing the Foehn effect. In addition, this area also has a strong heat island effect due to Beijing. These factors result in more extreme climatic conditions in this area compared to other parts of the North China Plain, making the vegetation system more susceptible to climate impacts. 

### _3.5. Comparative analysis of HiDRI with meteorological reanalysis data_ 

To further compare the performance of HiDRI, the 1-month SPEIs were calculated based on two widely used long-time series meteorological reanalysis data (CRU TS, TerraClimate). 

First, the overall comparative analysis results (no distinction between stations) are shown in Fig. 13(b-c). The SPEIs and HiDRI show a strong correlation, and the overall Pearson correlation coefficients are _R_ = 0.605 (p _<_ 0.01) and _R_ = 0.578 (p _<_ 0.01), respectively. Then, the correlation between HiDRI and the SPEIs were calculated at each station. The results are shown in Fig. 15 and Table 4. The correlation coefficients between HiDRI and the SPEIs are above 0.5 at most stations, and the average of correlation coefficients of all stations are around 0.6. 

12 

_Z. Xu et al._ 

_Remote Sensing of Environment 312 (2024) 114324_ 



**Fig. 8.** The spatiotemporal fusion results of LST within 3 km × 3 km around the Station 54,715 in the semi-arid climate, the Station 57,093 in the dry subhumid climate, and the Station 58,006 in the humid climate. From left to right are MOD11A1 monthly average LST (1 km), true Landsat LST enhanced by HUTS (30 m) and spatiotemporal fusion ESTARFM LST (30 m). 

For different climate zones, HiDRI shows good correlation with the SPEIs, and the performance of the semi-arid climate zone is slightly worse than that of others. 

### _3.6. Comparative analysis of HiDRI with remote sensing soil moisture data_ 

Different from the root zone soil moisture (0–100 cm) of the reanalysis data used in the framework, remote sensing soil moisture is the result of direct observation, which represents the surface soil moisture (0–5 cm) and can reflect the drought conditions on the surface to a certain extent. 

The comparative analysis results of HiDRI and the remote sensing soil moisture are shown in Fig. 16. The overall Pearson correlation coefficient R between HiDRI and CCI SMA is 0.351, indicating a good correlation. At the same time, the correlations at the typical stations in different climate zone also show a similar performance to the overall correlation. At the Station 57,093 in the dry subhumid climate even shows a strong correlation of _R_ = 0.517 (p _<_ 0.01). 

### **4. Discussion** 

### _4.1. Significance of the input factors_ 

The monthly input factors (drought-causing factors and vegetation condition anomalies) have a decisive impact on HiDRI. Therefore, the significance of monthly input factors to HiDRI is explored, which helps 

to understand the behavior of the model. The Pearson correlation coefficient is used to quantify the significance of each input factor, and the results are shown in Fig. 17. Since vegetation temperature anomaly (VTA) are negatively correlated with HiDRI, in order to facilitate comparison, the absolute value of the correlation coefficient between VTA and HiDRI was taken. The significance from high to low is: SPI, VTA, VMA, VGA, ESI, SMA. 

First, all input factors show strong correlations with HiDRI, indicating that HiDRI does effectively integrate various input factors and can comprehensively monitor vegetation drought based on multiple characteristics. Secondly, the contributions of drought-inducing factors and vegetation condition anomalies to HiDRI are similar. The average of the overall correlation coefficients of vegetation condition anomalies is 0.539, and that of drought-inducing factors is 0.548, which are very close. This demonstrates the effectiveness of the Copula-based coupling strategy in this framework, which can couple VCAI (reflecting vegetation condition anomalies) and EDII (reflecting drought-inducing factors) with equal contributions without unidirectional bias. Finally, the rationality of the significance of the input factors is analyzed. The SPI shows the highest correlation. According to drought theory, abnormal precipitation is the most direct and even decisive factor causing drought, because most droughts begin with a lack of precipitation. The VTA shows the second highest correlation, followed by the VMA and VGA. This is consistent with research on vegetation response to drought stress (Choat et al., 2018; Sun et al., 2023). When vegetation is stressed by drought, the first thing that occurs is the decrease in stomatal conductance, which leads to a decrease in the evaporative cooling capacity of 

13 

_Z. Xu et al._ 

_Remote Sensing of Environment 312 (2024) 114324_ 



**Fig. 9.** The vegetation condition anomaly within 3 km × 3 km around the Station 54,715 in the semi-arid climate, the Station 57,093 in the dry subhumid climate, and the Station 58,006 in the humid climate. From left to right are vegetation greenness anomaly, vegetation moisture anomaly, vegetation temperature anomaly and vegetation condition anomaly index (VCAI). 

the canopy and an increase in vegetation temperature. Then, as the evapotranspiration of the vegetation slowly proceeds, the water in the vegetation is continuously lost, which is reflected in the decrease in vegetation moisture. The lack of water affects the physiological activities of the vegetation, resulting in a reduction in vegetation greenness. 

### _4.2. The application and near real-time monitoring of HiDRI_ 

The operational application and near real-time drought monitoring of the framework are crucial. The framework can realize near real-time drought monitoring that is updated weekly, that is, monthly drought conditions including the previous week are released every week. For weekly HiDRI production, the input drought-inducing factors and vegetation condition anomalies are for the 30 days including the previous week. 

The drought-pregnant environment are annual data, they do not affect the near real-time of the framework. Moreover, land cover, irrigation, elevation, and available water capacity are relatively stable and have little inter-annual variation, so the data of the previous year can be used for weekly HiDRI production. However, it is still recommended to use corresponding years when developing model. The near real-time of the framework mainly depends on the production of drought-inducing factors and vegetation condition anomalies. The input data are shown in Table 5. The ERA5-land hourly data (precipitation, evaporation and soil moisture) is used to produce drought-inducing factors. This dataset 

contains data from 1950 to the present and is updated in near real-time. The MOD09GA and MOD11A1 used to produce vegetation condition anomalies are daily data updated in near real-time. Although spatiotemporal fusion relies on the Landsat data, its real-time characteristics mainly depends on the update frequency of MODDIS data. Because when performing spatiotemporal fusion, we only need to rely on near realtime MODIS data and the latest Landsat data to obtain near real-time high-resolution surface reflectance and LST estimates, thereby obtaining near real-time vegetation conditions. At the same time, combining Landsat 8 and Landsat 9, it is now possible to achieve 8-day revisit of the same area, which further ensures the accuracy of spatiotemporal fusion. 

Preparing long time-series benchmark datasets for calculating factor anomalies and developing models is complex, but in operational application, model development does not need to be done on a weekly basis. Only the month data including the previous week need to be produced every week, and HiDRI predictions can be derived based on the benchmark datasets and the developed models. The spatiotemporal fusion and resampling can use distributed and parallel operations to improve computing efficiency. Model development should include as many sample situations as possible, which will help improve the accuracy of HiDRI predictions. In this study, the drought factors were prepared based on the Gregorian calendar months, which actually represented the drought conditions in the last week of each calendar month in operational application. In the model development for operational application, the drought conditions in other weeks (52 weeks in a 

14 

_Z. Xu et al._ 



<!-- Start of picture text -->
Remote Sensing of Environment 312 (2024) 114324<br><!-- End of picture text -->



**Fig. 10.** The spatial patterns of HiDRI within 3 km × 3 km around the Station 54,715 in the semi-arid climate. 

year) should also be included. Of course, model development requires regular updates to ensure stable accuracy, and the update cycle depends on available labor costs. In addition, the input original datasets are also selected from publicly available data on a global scale as much as possible to facilitate the implementation of this framework in other parts of the world. 

### _4.3. Integrated drought monitoring by coupling physical methods and data_ 

### _driven_ 

In recent years, with the rapid development of machine learning and deep learning, the drought monitoring using data-driven has become a mainstream trend and has shown significant advantages (Jiao et al., 2021a; West et al., 2019). However, there are still some bottlenecks in the data-driven methods (Raissi et al., 2019; Seo et al., 2021): (1) In some regions, due to the limitations of terrain conditions or funding support, it is difficult to obtain the amount of sample data that meets the data-driven requirements. (2) The data-driven methods are often considered “black box”, which will reduce the user’s trust in them. (3) Due to the sensitivity of neural networks to data, some noise patterns may be learned, causing the noise to have a greater impact on the model. In order to solve these problems, one of the effective ways is to couple 

physical methods and data-driven. First, the physical laws can provide additional information to the neural network under given data conditions, thereby improving the accuracy of neural network. Secondly, it makes the data-driven method no longer a black box, which can improve user trust. Finally, the range of solutions of the neural network is limited by the laws, thereby reducing the interference caused by noise sensitivity. Some studies have begun to couple physical methods and datadriven methods for drought monitoring (Chen et al., 2022; Sun et al., 2022; Tyagi et al., 2022; Xie et al., 2021). Currently, there are two main ways: One is to couple physical methods outside the neural network, such as conditional data-driven based on the rules, and weighted combination of physical model results and data-driven results. The other is to couple physical methods inside the neural network (Seo et al., 2021), such as constraining loss function, constructing rule layers, etc. 

In this framework, we have also made beneficial attempts in this regard. First of all, the classification system of drought factors established based on disaster theory can guide the input of data-driven, making the input factors more meaningful. Secondly, the joint cumulative distribution is used to realize the coupling of VCAI and EDII, which can be considered as an effective way to couple physical methods and data-driven. Because VCAI is generated based on ESTARFM, HUTS and Euclidean distance, which has clear physical meaning, while EDII is 

15 

_Z. Xu et al._ 



<!-- Start of picture text -->
Remote Sensing of Environment 312 (2024) 114324<br><!-- End of picture text -->



**Fig. 11.** The spatial patterns of HiDRI within 3 km × 3 km around the Station 57,093 in the dry subhumid climate. 

generated based on deep learning. This coupling method helps to leverage the respective advantages of physical methods and data-driven. On the one hand, mature physical methods are fully applied; on the other hand, unclear nonlinear relationships are supplemented by datadriven, thus reflecting more comprehensive monitoring information. In the future, the coupling way of physical methods inside the neural networks will be further studied, as this way can make physical methods more deeply involved in data-driven processes. The outside and inside coupling of physical methods and data-driven will further enhance the capabilities of integrated drought monitoring. 

### **5. Conclusion** 

This paper proposes an integrated framework for monitoring vegetation drought at the field scale, and a 30 m × 30 m High spatial resolution Drought Response Index (HiDRI) was generated. Based on the disaster system theory, this framework established a classification system of drought factors, including vegetation condition, droughtpregnant environment and drought-inducing factors. The spatiotemporal fusion dominated by vegetation condition was conducted, and fine spatial resolution surface data of NDVI, NDMI, and LST were generated. Multivariate environmental drought-inducing information was 

integrated through deep learning. The performance of HiDRI was comprehensively compared with in-situ SPEI, meteorological reanalysis data, and remote sensing soil moisture data. Furthermore, the significance of the input factors and the application of the framework were fully discussed in this paper. The main conclusions of this paper are as follows: 

- (1) The comparative analysis of HiDRI with in-situ SPEI, meteorological reanalysis data, and remote sensing soil moisture data all perform well. The overall correlation coefficient (R) between HiDRI and the in-situ SPEI is 0.601, and also shows good correlation in spatial variation. The correlation coefficients between HiDRI and the SPEIs calculated by two meteorological reanalysis data (CRU TS, TerraClimate) are 0.605 and 0.578 respectively, and the correlation coefficient with remote sensing soil moisture (ESA CCI) anomaly is 0.351, which verifies the effectiveness of HiDRI from different aspects. 

- (2) HiDRI can effectively map the spatial patterns of drought at the 30 m × 30 m field scale, and can describe the heterogeneous spatial distribution and detailed texture characteristics of drought in different climate zones. 

16 



<!-- Start of picture text -->
Z. Xu et al.<br><!-- End of picture text -->



<!-- Start of picture text -->
Remote Sensing of Environment 312 (2024) 114324<br><!-- End of picture text -->



**Fig. 12.** The spatial patterns of HiDRI within 3 km × 3 km around the Station 58,006 in the humid climate. 



**Fig. 13.** Kernel density scatter plots of HiDRI with in-situ data and meteorological reanalysis data. Comparison of HiDRI with the in-situ SPEI (a), the SPEI calculated by CRU TS (b) and the SPEI calculated by TerraClimate (c). CRU TS: Climatic Research Unit gridded Time Series; R: Pearson correlation coefficient; n: Number of samples. 

17 

_Z. Xu et al._ 

_Remote Sensing of Environment 312 (2024) 114324_ 



**Fig. 14.** Spatial distribution of correlations between HiDRI and in-situ SPEI in the North China Plain. 



**Fig. 15.** Box plot of the correlation coefficients ( _p <_ 0.01) at the stations between HiDRI and the SPEIs. ALL refers to all stations, I is the stations in the semi-arid climate zone, II is the stations in the dry subhumid climate zone, and III is the stations in the humid climate zone. CRU TS, Climatic Research Unit gridded Time Series; R, Pearson correlation coefficient. 

**Table 4** 

The average of correlation coefficients at the stations between HiDRI and the SPEIs. 

|Data for SPEI|All|Semi-arid|Dry subhumid|Humid|
|---|---|---|---|---|
|calculation|stations|stations|stations|stations|
||||R||
|In-situ|0.615|0.594|0.632|0.628|
|CRU TS|0.619|0.589|0.624|0.651|
|TerraClimate|0.594|0.559|0.601|0.633|



- (3) Spatiotemporal fusion and deep learning are proven to be effective in generating field-scale high spatial resolution drought monitoring factors. At the same time, the joint cumulative distribution can effectively couple different aspects of drought information, which provides a way of coupling physical methods and data-driven. 

- (4) All input factors show good correlations with HiDRI, indicating that HiDRI effectively integrate various input factors and can comprehensively monitor vegetation drought based on multiple characteristics. 

Note: CRU TS, Climatic Research Unit gridded Time Series. 

This study achieved effective integrated monitoring of vegetation 

18 

_Z. Xu et al._ 

_Remote Sensing of Environment 312 (2024) 114324_ 



**Fig. 16.** Comparison of HiDRI and the CCI SMA at the station locations. (a) Overall kernel density scatter plot of HiDRI vs. CCI SMA. (b-e) Scatter plots of HiDRI vs. CCI SMA at the Station 54,715 (b), the Station 54,846 (c), the Station 57,093 (d) and the Station 58,006 (e). CCI, Climate Change Initiative (European Space Agency); SMA, Soil Moisture Anomaly; R: Pearson correlation coefficient; n: Number of samples. 



**Fig. 17.** Box plot of the correlation coefficients (p _<_ 0.01) at the stations between HiDRI and monthly input factors (left). Radar plot of overall correlation coefficients between HiDRI and monthly input factors (right). The correlation coefficient between HiDRI and VTA takes the absolute value. SPI, Standardized Precipitation Index; ESI, Evaporative Stress Index; SMA, Soil Moisture Anomaly; VTA, Vegetation Temperature Anomaly; VGA, Vegetation Greenness Anomaly; VMA, Vegetation Moisture Anomaly. 

drought at the field scale (30 m × 30 m), which is of great significance for refined water resources management and disaster loss assessment. In the future, with the development of earth observation satellite sensors with higher spatial resolution and the accumulation of public data, this framework can also be used to guide the production of the integrated drought index with higher spatial resolution in theory. 

Writing – review & editing. **Hao Sun:** Conceptualization, Formal analysis, Funding acquisition, Investigation, Methodology, Project administration, Resources, Supervision, Writing – original draft, Writing – review & editing. **Tian Zhang:** Data curation, Formal analysis. **Huanyu Xu:** Data curation, Formal analysis. **Dan Wu:** Data curation, Formal analysis. **JinHua Gao:** Data curation, Formal analysis. 

### **CRediT authorship contribution statement** 

### **Declaration of competing interest** 

**Zhenheng Xu:** Data curation, Formal analysis, Investigation, Methodology, Software, Validation, Visualization, Writing – original draft, 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence 

19 

_Z. Xu et al._ 

_Remote Sensing of Environment 312 (2024) 114324_ 

**Table 5** 

Overview of near real-time input data used to produce drought-inducing factors and vegetation condition anomalies. 

|Drought factor|Dataset|Band|Temporal<br>resolution|Time<br>range|
|---|---|---|---|---|
|Vegetation|MOD11A1|LST_Day_1km|Daily|2000 to|
|Temperature<br>Anomaly||l||Present|
|Vegetation|MOD09GA|sur_refl_b01,<br>l|Daily|2000 to|
|Greenness||sur_refl_b02||Present|
|Anomaly||l<br>l|||
|Vegetation||sur_refl_b02,<br>l|Daily||
|Moisture<br>Anomaly||l<br>sur_refl_b06|||
|Standardized|ERA5-|Total precipitation|Hourly|1950 to|
|Precipitation|Land|||present|
|Index|||||
|Evaporative||Total evaporation,|Hourly||
|Stress Index||Potential<br>evaporation|||
|Soil Moisture<br>Anomaly||Volumetric soil<br>water layer 1/2/3|Hourly||



the work reported in this paper. 

### **Data availability** 

Data will be made available on request. 

### **Acknowledgements** 

This work was supported by Beijing Natural Science Foundation (grant numbers 6222045) and Fundamental Research Funds for the Central Universities (grant numbers 2024JCCXDC03). 

### **References** 

- Abatzoglou, J.T., Dobrowski, S.Z., Parks, S.A., Hegewisch, K.C., 2018. TerraClimate, a high-resolution global dataset of monthly climate and climatic water balance from 1958–2015. Sci. Data 5, 170191. https://doi.org/10.1038/sdata.2017.191. 

- Abowarda, A.S., Bai, L., Zhang, C., Long, D., Li, X., Huang, Q., Sun, Z., 2021. Generating surface soil moisture at 30 m spatial resolution using both data fusion and machine learning toward better water resources management at the field scale. Remote Sens. Environ. 255, 112301 https://doi.org/10.1016/j.rse.2021.112301. 

- AghaKouchak, A., Farahmand, A., Melton, F.S., Teixeira, J., Anderson, M.C., Wardlow, B. D., Hain, C.R., 2015. Remote sensing of drought: Progress, challenges and opportunities. Rev. Geophys. 53, 452–480. https://doi.org/10.1002/ 2014RG000456. 

- Anderson, M.C., Hain, C., Wardlow, B., Pimstein, A., Mecikalski, J.R., Kustas, W.P., 2011. Evaluation of drought indices based on thermal remote sensing of evapotranspiration over the continental United States. J. Clim. 24, 2025–2044. https://doi.org/10.1175/2010JCLI3812.1. 

- Bergstra, J., Bardenet, R., Bengio, Y., K´egl, B., 2011. Algorithms for hyper-parameter optimization. In: Proceedings of the 24th International Conference on Neural Information Processing Systems, NIPS’11. Curran Associates Inc., Red Hook, NY, USA, pp. 2546–2554. 

- Bergstra, J., Yamins, D., Cox, D., 2013. Making a science of model search: 

   - Hyperparameter optimization in hundreds of dimensions for vision architectures. In: Proceedings of the 30th inteRnational Conference on Machine Learning Presented at the International Conference on Machine Learning. PMLR, pp. 115–123. 

- Brown, J.F., Wardlow, B.D., Tadesse, T., Hayes, M.J., Reed, B.C., 2008. The vegetation drought response index (VegDRI): a new integrated approach for monitoring drought stress in vegetation. GISci. Remote Sens. 45, 16–46. https://doi.org/10.2747/15481603.45.1.16. 

- Chen, J., Zhu, X., Vogelmann, J.E., Gao, F., Jin, S., 2011. A simple and effective method for filling gaps in Landsat ETM+ SLC-off images. Remote Sens. Environ. 115, 1053–1064. https://doi.org/10.1016/j.rse.2010.12.010. 

- Chen, H., Huang, J.J., Dash, S.S., Wei, Y., Li, H., 2022. A hybrid deep learning framework with physical process description for simulation of evapotranspiration. J. Hydrol. 606, 127422 https://doi.org/10.1016/j.jhydrol.2021.127422. 

- Choat, B., Brodribb, T.J., Brodersen, C.R., Duursma, R.A., Lopez, R., Medlyn, B.E., 2018.´ Triggers of tree mortality under drought. Nature 558, 531–539. https://doi.org/ 10.1038/s41586-018-0240-x. 

- Cook, M., Schott, J.R., Mandel, J., Raqueno, N., 2014. Development of an operational calibration methodology for the Landsat thermal data archive and initial testing of the atmospheric compensation component of a land surface temperature (LST) 

product from the archive. Remote Sens. 6, 11244–11266. https://doi.org/10.3390/ rs61111244. 

- Dai, A., 2011. Drought under global warming: a review. WIREs Clim. Change 2, 45–65. https://doi.org/10.1002/wcc.81. 

- Dinerstein, E., Olson, D., Joshi, A., Vynne, C., Burgess, N.D., Wikramanayake, E., Hahn, N., Palminteri, S., Hedao, P., Noss, R., Hansen, M., Locke, H., Ellis, E.C., Jones, B., Barber, C.V., Hayes, R., Kormos, C., Martin, V., Crist, E., Sechrest, W., Price, L., Baillie, J.E.M., Weeden, D., Suckling, K., Davis, C., Sizer, N., Moore, R., Thau, D., Birch, T., Potapov, P., Turubanova, S., Tyukavina, A., de Souza, N., Pintea, L., Brito, J.C., Llewellyn, O.A., Miller, A.G., Patzelt, A., Ghazanfar, S.A., Timberlake, J., Kloser,¨ H., Shennan-Farpon,´ Y., Kindt, R., Lillesø, J.-P.B., van Breugel, P., Graudal, L., Voge, M., Al-Shammari, K.F., Saleem, M., 2017. An ecoregion-based approach to protecting half the terrestrial realm. BioScience 67, 534–545. https://doi.org/10.1093/biosci/bix014. 

- Dominguez, A., Kleissl, J., Luvall, J.C., Rickman, D.L., 2011. High-resolution urban thermal sharpener (HUTS). Remote Sens. Environ. 115, 1772–1780. https://doi.org/ 10.1016/j.rse.2011.03.008. 

- Dorigo, W., Wagner, W., Albergel, C., Albrecht, F., Balsamo, G., Brocca, L., Chung, D., Ertl, M., Forkel, M., Gruber, A., Haas, E., Hamer, P.D., Hirschi, M., Ikonen, J., de Jeu, R., Kidd, R., Lahoz, W., Liu, Y.Y., Miralles, D., Mistelbauer, T., Nicolai-Shaw, N., Parinussa, R., Pratola, C., Reimer, C., van der Schalie, R., Seneviratne, S.I., Smolander, T., Lecomte, P., 2017. ESA CCI soil moisture for improved earth system understanding: state-of-the art and future directions. Remote Sens. Environ. Earth Observat. Essent. Climat. Variabl. 203, 185–215. https://doi.org/10.1016/j. rse.2017.07.001. 

- Du, L., Tian, Q., Yu, T., Meng, Q., Jancso, T., Udvardy, P., Huang, Y., 2013. A comprehensive drought monitoring method integrating MODIS and TRMM data. Int. J. Appl. Earth Obs. Geoinf. 23, 245–253. https://doi.org/10.1016/j. jag.2012.09.010. 

- Earth Resources Observation and Science (EROS) Center, 2018. Methods - QuickDRI. U. S. Geological Survey [WWW Document]. URL. https://www.usgs.gov/special-to pics/monitoring-vegetation-drought-stress/science/methods-quickdri (accessed 9.24.23). 

- Farr, T.G., Rosen, P.A., Caro, E., Crippen, R., Duren, R., Hensley, S., Kobrick, M., Paller, M., Rodriguez, E., Roth, L., Seal, D., Shaffer, S., Shimada, J., Umland, J., Werner, M., Oskin, M., Burbank, D., Alsdorf, D., 2007. The shuttle radar topography Mission. Rev. Geophys. 45 https://doi.org/10.1029/2005RG000183. 

- Feng, P., Wang, B., Liu, D.L., Yu, Q., 2019. Machine learning-based integration of remotely-sensed drought factors can improve the estimation of agricultural drought in south-eastern Australia. Agric. Syst. 173, 303–316. https://doi.org/10.1016/j. agsy.2019.03.015. 

- Foga, S., Scaramuzza, P.L., Guo, S., Zhu, Z., Dilley, R.D., Beckmann, T., Schmidt, G.L., Dwyer, J.L., Joseph Hughes, M., Laue, B., 2017. Cloud detection algorithm comparison and validation for operational Landsat data products. Remote Sens. Environ. 194, 379–390. https://doi.org/10.1016/j.rse.2017.03.026. 

- Gao, F., Hilker, T., Zhu, X., Anderson, M., Masek, J., Wang, P., Yang, Y., 2015. Fusing Landsat and MODIS data for vegetation monitoring. IEEE Geosci. Remote Sens. Magaz. 3, 47–60. https://doi.org/10.1109/MGRS.2015.2434351. 

- Gao, Y., Markkanen, T., Thum, T., Aurela, M., Lohila, A., Mammarella, I., K¨am¨ar¨ainen, M., Hagemann, S., Aalto, T., 2016. Assessing various drought indicators in representing summer drought in boreal forests in Finland. Hydrol. Earth Syst. Sci. 20, 175–191. https://doi.org/10.5194/hess-20-175-2016. 

- Gao, F., Anderson, M.C., Zhang, X., Yang, Z., Alfieri, J.G., Kustas, W.P., Mueller, R., Johnson, D.M., Prueger, J.H., 2017. Toward mapping crop progress at field scales through fusion of Landsat and MODIS imagery. Remote Sens. Environ. 188, 9–25. https://doi.org/10.1016/j.rse.2016.11.004. 

- Gao, C., Zhang, B., Shao, S., Hao, M., Zhang, Y., Xu, Y., Kuang, Y., Dong, L., Wang, Z., 2023. Risk assessment and zoning of flood disaster in Wuchengxiyu region, China. Urban Clim. 49, 101562 https://doi.org/10.1016/j.uclim.2023.101562. 

- Gorelick, N., Hancher, M., Dixon, M., Ilyushchenko, S., Thau, D., Moore, R., 2017. Google earth engine: planetary-scale geospatial analysis for everyone. Remote Sens. Environ. Big Remot. Sens. Data: Tools, Applicat. Experien. 202, 18–27. https://doi. org/10.1016/j.rse.2017.06.031. 

- Gruber, A., Scanlon, T., van der Schalie, R., Wagner, W., Dorigo, W., 2019. Evolution of the ESA CCI soil moisture climate data records and their underlying merging methodology. Earth Syst. Sci. Data 11, 717–739. https://doi.org/10.5194/essd-11- 

717-2019. 

- Guo, C., Berkhahn, F., 2016. Entity Embeddings of categorical variables (no. arXiv: 1604.06737). arXiv. https://doi.org/10.48550/arXiv.1604.06737. 

- Guo, H., Bao, A., Liu, T., Ndayisaba, F., Jiang, L., Zheng, G., Chen, T., De Maeyer, P., 2019. Determining variable weights for an optimal scaled drought condition index (OSDCI): evaluation in Central Asia. Remote Sens. Environ. 231, 111220 https://doi. org/10.1016/j.rse.2019.111220. 

- Hao, Z., Singh, V.P., 2015. Drought characterization from a multivariate perspective: a review. J. Hydrol. 527, 668–678. https://doi.org/10.1016/j.jhydrol.2015.05.031. 

- Hao, C., Zhang, J., Yao, F., 2015. Combination of multi-sensor remote sensing data for drought monitoring over Southwest China. Int. J. Appl. Earth Obs. Geoinf. 35, 270–283. https://doi.org/10.1016/j.jag.2014.09.011. 

- Harris, I., Osborn, T.J., Jones, P., Lister, D., 2020. Version 4 of the CRU TS monthly highresolution gridded multivariate climate dataset. Sci. Data 7, 109. https://doi.org/ 10.1038/s41597-020-0453-3. 

- Hengl, T., de Jesus, J.M., Heuvelink, G.B.M., Gonzalez, M.R., Kilibarda, M., Blagoti´c, A., Shangguan, W., Wright, M.N., Geng, X., Bauer-Marschallinger, B., Guevara, M.A., Vargas, R., MacMillan, R.A., Batjes, N.H., Leenaars, J.G.B., Ribeiro, E., Wheeler, I., Mantel, S., Kempen, B., 2017. SoilGrids250m: global gridded soil information based 

20 

_Z. Xu et al._ 

_Remote Sensing of Environment 312 (2024) 114324_ 

on machine learning. PLoS One 12, e0169748. https://doi.org/10.1371/journal. 

pone.0169748. 

- Jiao, W., Tian, C., Chang, Q., Novick, K.A., Wang, L., 2019. A new multi-sensor integrated index for drought monitoring. Agric. For. Meteorol. 268, 74–85. https:// doi.org/10.1016/j.agrformet.2019.01.008. 

- Jiao, W., Wang, L., McCabe, M.F., 2021a. Multi-sensor remote sensing for drought characterization: current status, opportunities and a roadmap for the future. Remote Sens. Environ. 256, 112313 https://doi.org/10.1016/j.rse.2021.112313. 

- Jiao, W., Wang, L., Smith, W.K., Chang, Q., Wang, H., D’Odorico, P., 2021b. Observed increasing water constraint on vegetation growth over the last three decades. Nat. Commun. 12, 3777. https://doi.org/10.1038/s41467-021-24016-9. 

- Jin, S., Sader, S.A., 2005. Comparison of time series tasseled cap wetness and the normalized difference moisture index in detecting forest disturbances. Remote Sens. Environ. 94, 364–372. https://doi.org/10.1016/j.rse.2004.10.012. 

- Ju, J., Roy, D.P., 2008. The availability of cloud-free Landsat ETM+ data over the conterminous United States and globally. Remote Sens. Environ. 112, 1196–1211. https://doi.org/10.1016/j.rse.2007.08.011. 

- Kang, S., Eltahir, E.A.B., 2018. North China plain threatened by deadly heatwaves due to climate change and irrigation. Nat. Commun. 9, 2894. https://doi.org/10.1038/ s41467-018-05252-y. 

- Kogan, F.N., 1995a. Application of vegetation index and brightness temperature for drought detection. In: Advances in Space Research, Natural Hazards: Monitoring and Assessment Using Remote Sensing Technique, 15, pp. 91–100. https://doi.org/ 10.1016/0273-1177(95)00079-T. 

- Kogan, F.N., 1995b. Droughts of the late 1980s in the United States as Derived from NOAA polar-orbiting satellite data. Bull. Am. Meteorol. Soc. 76, 655–668. https:// doi.org/10.1175/1520-0477(1995)076 _<_ 0655:DOTLIT _>_ 2.0.CO;2. 

- Li, J., Lei, H., 2021. Tracking the spatio-temporal change of planting area of winter wheat-summer maize cropping system in the North China plain during 2001–2018. Comput. Electron. Agric. 187, 106222 https://doi.org/10.1016/j. compag.2021.106222. 

- Liang, S., 2001. Narrowband to broadband conversions of land surface albedo I: algorithms. Remote Sens. Environ. 76, 213–238. https://doi.org/10.1016/S00344257(00)00205-4. 

- Long, D., Yan, L., Bai, L., Zhang, C., Li, X., Lei, H., Yang, H., Tian, F., Zeng, C., Meng, X., Shi, C., 2020. Generation of MODIS-like land surface temperatures under all-weather conditions based on a data fusion approach. Remote Sens. Environ. 246, 111863 https://doi.org/10.1016/j.rse.2020.111863. 

- Ma, Y., Liu, S., Song, L., Xu, Z., Liu, Y., Xu, T., Zhu, Z., 2018. Estimation of daily evapotranspiration and irrigation water efficiency at a Landsat-like scale for an arid irrigation area using multi-source remote sensing data. Remote Sens. Environ. 216, 715–734. https://doi.org/10.1016/j.rse.2018.07.019. 

- Masek, J.G., Vermote, E.F., Saleous, N.E., Wolfe, R., Hall, F.G., Huemmrich, K.F., Gao, F., Kutler, J., Lim, T.-K., 2006. A Landsat surface reflectance dataset for North America, 1990-2000. IEEE Geosci. Remote Sens. Lett. 3, 68–72. https://doi.org/10.1109/ LGRS.2005.857030. 

- McKee, T.B., Doesken, N.J., Kleist, J., 1993. The relationship of drought frequency and duration to time scales. In: Proceedings of the 8th Conference on Applied Climatology. Boston, MA, USA, Pp, pp. 179–183. 

- Mo, X.-G., Hu, S., Lin, Z.-H., Liu, S.-X., Xia, J., 2017. Impacts of climate change on agricultural water resources and adaptation on the North China plain. In: Advances in Climate Change Research, Including Special Topic on Climate Change and Water Resources, 8, pp. 93–98. https://doi.org/10.1016/j.accre.2017.05.007. 

- Munoz˜ Sabater, J., 2019. ERA5-Land Monthly Averaged Data From 1950 to Present. https://doi.org/10.24381/cds.68d2bb30. 

- Naumann, G., Cammalleri, C., Mentaschi, L., Feyen, L., 2021. Increased economic drought impacts in Europe with anthropogenic warming. Nat. Clim. Chang. 11, 485– +. https://doi.org/10.1038/s41558-021-01044-3. 

- Palmer, W.C., 1965. Meteorological Drought. U.S. Department of Commerce, Weather 

Bureau. 

- Park, S., Im, J., Jang, E., Rhee, J., 2016. Drought assessment and monitoring through blending of multi-sensor indices using machine learning approaches for different climate regions. Agric. For. Meteorol. 216, 157–169. https://doi.org/10.1016/j. agrformet.2015.10.011. 

- Peng, J., Dadson, S., Hirpa, F., Dyer, E., Lees, T., Miralles, D.G., Vicente-Serrano, S.M., Funk, C., 2020. A pan-African high-resolution drought index dataset. Earth Syst. Sci. Data 12, 753–769. https://doi.org/10.5194/essd-12-753-2020. 

- Preimesberger, W., Scanlon, T., Su, C.-H., Gruber, A., Dorigo, W., 2021. Homogenization of structural breaks in the global ESA CCI soil moisture multisatellite climate data record. IEEE Trans. Geosci. Remote Sens. 59, 2845–2862. https://doi.org/10.1109/ TGRS.2020.3012896. 

- Pyarali, K., Peng, J., Disse, M., Tuo, Y., 2022. Development and application of high resolution SPEI drought dataset for Central Asia. Sci. Data 9, 172. https://doi.org/ 10.1038/s41597-022-01279-5. 

- Rahmati, O., Falah, F., Dayal, K.S., Deo, R.C., Mohammadi, F., Biggs, T., Moghaddam, D. D., Naghibi, S.A., Bui, D.T., 2020. Machine learning approaches for spatial modeling of agricultural droughts in the south-east region of Queensland Australia. Sci. Total Environ. 699, 134230 https://doi.org/10.1016/j.scitotenv.2019.134230. 

- Raissi, M., Perdikaris, P., Karniadakis, G.E., 2019. Physics-informed neural networks: a deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations. J. Comput. Phys. 378, 686–707. https://doi. org/10.1016/j.jcp.2018.10.045. 

Rhee, J., Im, J., Carbone, G.J., 2010. Monitoring agricultural drought for arid and humid regions using multi-sensor remote sensing data. Remote Sens. Environ. 114, 2875–2887. https://doi.org/10.1016/j.rse.2010.07.005. 

Roodposhti, M.S., Safarrad, T., Shahabi, H., 2017. Drought sensitivity mapping using two 

one-class support vector machine algorithms. Atmos. Res. 193, 73–82. https://doi. org/10.1016/j.atmosres.2017.04.017. 

- Schmidt, G., Jenkerson, C.B., Masek, J., Vermote, E., Gao, F., 2013. Landsat Ecosystem Disturbance Adaptive Processing System (LEDAPS) Algorithm Description (No. 2013–1057), Open-File Report. U.S. Geological Survey. https://doi.org/10.3133/ ofr20131057. 

- Seo, S., Arik, S., Yoon, J., Zhang, X., Sohn, K., Pfister, T., 2021. Controlling neural networks with rule representations. In: Advances in Neural Information Processing Systems. Curran Associates, Inc., pp. 11196–11207 

- Shen, R., Huang, A., Li, B., Guo, J., 2019. Construction of a drought monitoring model using deep learning based on multi-source remote sensing data. Int. J. Appl. Earth Obs. Geoinf. 79, 48–57. https://doi.org/10.1016/j.jag.2019.03.006. 

- Shi, P., 2019. Hazards, disasters, and risks. In: Shi, P. (Ed.), Disaster Risk Science, IHDP/ Future Earth-Integrated Risk Governance Project Series. Springer, Singapore, pp. 1–48. https://doi.org/10.1007/978-981-13-6689-5_1. 

- Shi, P., Ye, T., Wang, Y., Zhou, T., Xu, W., Du, J., Wang, J., Li, N., Huang, C., Liu, L., Chen, B., Su, Y., Fang, W., Wang, M., Hu, X., Wu, J., He, C., Zhang, Q., Ye, Q., Jaeger, C., Okada, N., 2020. Disaster risk science: a geographical perspective and a research framework. Int. J. Disaster Risk Sci. 11, 426–440. https://doi.org/10.1007/ s13753-020-00296-5. 

- Son, B., Park, Sumin, Im, J., Park, Seohui, Ke, Y., Quackenbush, L.J., 2021. A new drought monitoring approach: vector projection analysis (VPA). Remote Sens. Environ. 252, 112145 https://doi.org/10.1016/j.rse.2020.112145. 

- Su, B., Huang, J., Fischer, T., Wang, Y., Kundzewicz, Z.W., Zhai, J., Sun, H., Wang, A., Zeng, X., Wang, G., Tao, H., Gemmer, M., Li, X., Jiang, T., 2018. Drought losses in China might double between the 1.5<sup>◦</sup> C and 2.0<sup>◦</sup> C warming. Proc. Natl. Acad. Sci. 115, 10600–10605. https://doi.org/10.1073/pnas.1802129115. 

- Sun, H., Zhang, X., Zhao, X., 2022. Series or parallel? An exploration in coupling physical model and machine learning method for disaggregating satellite microwave soil moisture. IEEE Trans. Geosci. Remote Sens. 60, 1–15. https://doi.org/10.1109/ TGRS.2022.3216343. 

- Sun, H., Xu, Z., Liu, H., 2023. An evaluation of the response of vegetation greenness, moisture, fluorescence, and temperature-based remote sensing indicators to drought stress. J. Hydrol. 130125 https://doi.org/10.1016/j.jhydrol.2023.130125. 

- Tadesse, T., Champagne, C., Wardlow, B.D., Hadwen, T.A., Brown, J.F., Demisse, G.B., Bayissa, Y.A., Davidson, A.M., 2017. Building the vegetation drought response index for Canada (VegDRI-Canada) to monitor agricultural drought: first results. GISci. Remote Sens. 54, 230–257. https://doi.org/10.1080/15481603.2017.1286728. 

- Thornthwaite, C.W., 1948. An approach toward a rational classification of climate. Geogr. Rev. 38, 55–94. https://doi.org/10.2307/210739. 

- Tucker, C.J., 1979. Red and photographic infrared linear combinations for monitoring vegetation. Remote Sens. Environ. 8, 127–150. https://doi.org/10.1016/0034-4257 (79)90013-0. 

- Tyagi, S., Zhang, X., Saraswat, D., Sahany, S., Mishra, S.K., Niyogi, D., 2022. Flash drought: review of concept, prediction and the potential for machine learning, deep learning methods. Earth’s Future 10. https://doi.org/10.1029/2022EF002723 e2022EF002723. 

- United Nations Environment Programme, 1997. World Atlas of Desertification: Second Edition. 

- Vergopolan, N., Chaney, N.W., Beck, H.E., Pan, M., Sheffield, J., Chan, S., Wood, E.F., 2020. Combining hyper-resolution land surface modeling with SMAP brightness temperatures to obtain 30-m soil moisture estimates. Remote Sens. Environ. 242, 111740 https://doi.org/10.1016/j.rse.2020.111740. 

- Vermote, E., Wolfe, R., 2015. MOD09GA MODIS/Terra Surface Reflectance Daily L2G Global 1kmand 500m SIN Grid V006. https://doi.org/10.5067/MODIS/ MOD09GA.006. 

- Vermote, E., Justice, C., Claverie, M., Franch, B., 2016. Preliminary analysis of the performance of the Landsat 8/OLI land surface reflectance product. Remote sensing of environment, Landsat 8. Sci. Res. 185, 46–56. https://doi.org/10.1016/j. rse.2016.04.008. 

- Vicente-Serrano, S.M., Begueria, S., Lopez-Moreno, J.I., 2010. A multiscalar drought index sensitive to global warming: the standardized precipitation evapotranspiration index. J. Clim. 23, 1696–1718. https://doi.org/10.1175/2009JCLI2909.1. 

- Vicente-Serrano, S.M., Quiring, S.M., Pena-Gallardo, M., Yuan, S., Domínguez-Castro, F.,˜ 2020. A review of environmental droughts: increased risk under global warming? Earth Sci. Rev. 201, 102953 https://doi.org/10.1016/j.earscirev.2019.102953. 

- Wan, Z., Hook, S., Hulley, G., 2015. MOD11A1 MODIS/Terra Land Surface Temperature/ Emissivity Daily L3 Global 1km SIN Grid V006. https://doi.org/10.5067/MODIS/ MOD11A1.006. 

- Wang, X., Lei, H., Li, J., Huo, Z., Zhang, Y., Qu, Y., 2023. Estimating evapotranspiration and yield of wheat and maize croplands through a remote sensing-based model. Agric. Water Manag. 282, 108294 https://doi.org/10.1016/j.agwat.2023.108294. 

- Wei, W., Pang, S., Wang, X., Zhou, L., Xie, B., Zhou, J., Li, C., 2020. Temperature vegetation precipitation dryness index (TVPDI)-based dryness-wetness monitoring in China. Remote Sens. Environ. 248, 111957 https://doi.org/10.1016/j. rse.2020.111957. 

- West, H., Quinn, N., Horswell, M., 2019. Remote sensing for drought monitoring & impact assessment: Progress, past challenges and future opportunities. Remote Sens. Environ. 232, 111291 https://doi.org/10.1016/j.rse.2019.111291. 

- Wu, J., Zhou, L., Liu, M., Zhang, J., Leng, S., Diao, C., 2013. Establishing and assessing the integrated surface drought index (ISDI) for agricultural drought monitoring in mid-eastern China. Int. J. Appl. Earth Obs. Geoinf. 23, 397–410. https://doi.org/ 10.1016/j.jag.2012.11.003. 

21 

_Z. Xu et al._ 

_Remote Sensing of Environment 312 (2024) 114324_ 

- Wu, J., Zhou, L., Mo, X., Zhou, H., Zhang, J., Jia, R., 2015. Drought monitoring and analysis in China based on the integrated surface drought index (ISDI). Int. J. Appl. Earth Obs. Geoinf. 41, 23–33. https://doi.org/10.1016/j.jag.2015.04.006. 

- Xie, K., Liu, P., Zhang, J., Han, D., Wang, G., Shen, C., 2021. Physics-guided deep learning for rainfall-runoff modeling by considering extreme events and monotonic relationships. J. Hydrol. 603, 127043 https://doi.org/10.1016/j. jhydrol.2021.127043. 

- Xu, L., Abbaszadeh, P., Moradkhani, H., Chen, N., Zhang, X., 2020. Continental drought monitoring using satellite soil moisture, data assimilation and an integrated drought index. Remote Sens. Environ. 250, 112028 https://doi.org/10.1016/j. rse.2020.112028. 

- Xu, Z., Sun, H., Zhang, T., Xu, H., Wu, D., Gao, J., 2023. Evaluating established deep learning methods in constructing integrated remote sensing drought index: a case study in China. Agric. Water Manag. 286, 108405 https://doi.org/10.1016/j. agwat.2023.108405. 

- Yang, J., Huang, X., 2021. The 30 m annual land cover dataset and its dynamics in China from 1990 to 2019. Earth Syst. Sci. Data 13, 3907–3925. https://doi.org/10.5194/ essd-13-3907-2021. 

- Yang, Y., Anderson, M.C., Gao, F., Wood, J.D., Gu, L., Hain, C., 2021. Studying droughtinduced forest mortality using high spatiotemporal resolution evapotranspiration data from thermal satellite imaging. Remote Sens. Environ. 265, 112640 https://doi. org/10.1016/j.rse.2021.112640. 

- Yin, G., Zhang, H., 2023. A new integrated index for drought stress monitoring based on decomposed vegetation response factors. J. Hydrol. 618, 129252 https://doi.org/ 10.1016/j.jhydrol.2023.129252. 

- Yuan, Q., Shen, H., Li, T., Li, Z., Li, S., Jiang, Y., Xu, H., Tan, W., Yang, Q., Wang, J., Gao, J., Zhang, L., 2020. Deep learning in environmental remote sensing: achievements and challenges. Remote Sens. Environ. 241, 111716 https://doi.org/ 10.1016/j.rse.2020.111716. 

- Zhang, A., Jia, G., 2013. Monitoring meteorological drought in semiarid regions using multi-sensor microwave remote sensing data. Remote Sens. Environ. 134, 12–23. https://doi.org/10.1016/j.rse.2013.02.023. 

- Zhang, A., Jia, G., Wang, H., 2019. Improving meteorological drought monitoring capability over tropical and subtropical water-limited ecosystems: evaluation and ensemble of the microwave integrated drought index. Environ. Res. Lett. 14, 044025 https://doi.org/10.1088/1748-9326/ab005e. 

- Zhou, X., Wang, P., Tansey, K., Zhang, S., Li, H., Wang, L., 2020. Developing a fused vegetation temperature condition index for drought monitoring at field scales using Sentinel-2 and MODIS imagery. Comput. Electron. Agric. 168, 105144 https://doi. org/10.1016/j.compag.2019.105144. 

- Zhu, X., Chen, J., Gao, F., Chen, X., Masek, J.G., 2010. An enhanced spatial and temporal adaptive reflectance fusion model for complex heterogeneous regions. Remote Sens. Environ. 114, 2610–2623. https://doi.org/10.1016/j.rse.2010.05.032. 

- Zhu, X., Cai, F., Tian, J., Williams, T.K.-A., 2018. Spatiotemporal fusion of multisource remote sensing data: literature survey, taxonomy, principles, applications, and future directions. Remote Sens. 10, 527. https://doi.org/10.3390/rs10040527. 

- Zomer, R.J., Trabucco, A., Bossio, D.A., Verchot, L.V., 2008. Climate change mitigation: a spatial analysis of global land suitability for clean development mechanism afforestation and reforestation. Agric. Ecosyst. Environ. 126, 67–80. https://doi.org/ 10.1016/j.agee.2008.01.014. 

22 

