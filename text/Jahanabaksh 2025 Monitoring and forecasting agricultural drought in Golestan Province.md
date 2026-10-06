



Available online at www.sciencedirect.com 

## ScienceDirect 

Advances in Space Research 77 (2026) 4222–4246 



www.elsevier.com/locate/asr 

# Monitoring and forecasting agricultural drought in Golestan Province, Iran (2001–2028): an integrated approach using remote sensing and machine learning 

Mahsa Jahanbakhsh, Mehdi Akhoondzadeh<sup>⁎</sup> 

Photogrammetry and Remote Sensing Department, School of Surveying and Geospatial Engineering, College of Engineering, University of Tehran, Tehran, Iran 

Received 15 July 2025; received in revised form 4 November 2025; accepted 27 November 2025 Available online 1 December 2025 

#### Abstract 

Agricultural drought poses a significant threat to food security in arid and semi-arid regions such as Golestan Province, Iran, where climate variability, groundwater depletion, and land use changes have exacerbated water stress. Traditional monitoring approaches often reliant on single-variable indices or sparse in-situ data fail to capture the complex and spatially heterogeneous nature of drought. This study develops an integrated framework for monitoring and forecasting agricultural drought using remote sensing and machine learning. The Vegetation Health Index (VHI), calculated from MODIS-derived NDVI and LST via the Vegetation Condition Index (VCI) and Temperature Condition Index (TCI), was used to track monthly drought patterns from 2001 to 2024. Supplementary hydroclimatic indicators, including the Standardized Precipitation Index (SPI) and the Evaporative Stress Index (ESI), were used to interpret precipitation deficits and evapotranspiration anomalies. Drought trends and severity were analyzed through VHI-based classification, linear trend mapping, and land cover cross-analysis using Sentinel-derived Dynamic World data. For forecasting, Random Forest (RF) and Extreme Gradient Boosting (XGBoost) regression models were trained on VHI (2001–2020) and validated over 2021–2024. XGBoost showed superior performance (R<sup>2</sup> = 0.83, RMSE = 0.065, MAE = 0.041) and was used to forecast 2028 drought conditions. Results indicate that severe and extreme drought will expand to over 13,000 km<sup>2</sup> (≈62 % of the province), with croplands and bare lands being the most vulnerable. This study demonstrates the effectiveness of integrating satellite data and machine learning for operational drought monitoring and prediction, offering valuable insights for early warning systems and climate-resilient agricultural planning. © 2025 COSPAR. Published by Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies. 

Keywords: Agricultural drought; XGBoost; Vegetation Health Index; Drought monitoring; Golestan Province 

### 1. Introduction 

Drought is a climatic phenomenon characterized by a prolonged and significant deficiency in precipitation over a wide geographic area, posing severe challenges to agriculture, ecosystems, natural resources, food and water secu- 

> ⁎ Corresponding author. E-mail address: makhonz@ut.ac.ir (M. Akhoondzadeh). 

rity, economic stability, and human health, to the extent that it may even result in loss of life (Behrang Manesh et al., 2019; Damavandi et al., 2016; Hu et al., 2020; Lu et al., 2019; Ogunrinde et al., 2020; Ray et al., 2014; Zhao et al., 2020). In recent years, the gradual warming of the Earth has led to the emergence of more frequent and intense drought events, causing substantial negative impacts on ecosystems and contributing to vegetation degradation (Behrang Manesh et al., 2019). Drought is 

https://doi.org/10.1016/j.asr.2025.11.113 

0273-1177/© 2025 COSPAR. Published by Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies. 

Advances in Space Research 77 (2026) 4222–4246 

##### M. Jahanbakhsh, M. Akhoondzadeh 

generally classified into four main types: meteorological, hydrological, agricultural, and socio-economic droughts (Hu et al., 2020; Ogunrinde et al., 2020). Agricultural drought occurs when soil moisture becomes insufficient for optimal plant growth, directly reducing agricultural productivity (Mannocchi et al., 2004). This form of drought is particularly critical for the economies of agrarian countries (Dutta et al., 2015). Continuous and efficient monitoring of agricultural drought is essential for maintaining agricultural output, as early warning systems can significantly reduce potential damages (Lu et al., 2019). Furthermore, such monitoring enables policymakers to take timely and effective actions and allocate financial resources appropriately. Compared to traditional methods, remote sensing (RS) provides an efficient means of observing land conditions and managing natural resources. Numerous RS-based indices have been proposed, developed, and applied for drought monitoring purposes (Zarei et al., 2013). According to the Food and Agriculture Organization (FAO), agriculture supports the livelihoods of over 15 million people in rural areas of Iran. Situated in the arid and semi-arid region of the Middle East, Iran exhibits a wide range of climatic conditions, from cold climates in the northwest to humid conditions in the north and south, and dry to semi-arid zones in the southeast and central regions (Zarei et al., 2013). Due to favorable climatic conditions, agricultural activities are more prominent in the northern, northwestern, and southwestern parts of the country. In a developing nation such as Iran, which aims to transition from an oil-dependent to a non-oil-based economy, agriculture plays a pivotal role in economic stability. Consequently, it is imperative for policymakers to adopt advanced technologies to safeguard agricultural resources from threats such as droughts, floods, and pests. Numerous studies have explored remote sensing-based methods for agricultural drought monitoring. For instance, Dutta et al. (2015) assessed drought conditions in Rajasthan using the Vegetation Condition Index (VCI) validated by ground data, while Kundu et al. (2016) combined precipitation anomalies with RS indicators for drought detection. Vaani and Porchelvan (2018) analyzed a 20year VCI time series in India, identifying persistent moderate to severe drought conditions. Similar findings were reported by Zagade et al. (2018), who observed a shift from moderate to extreme drought across an Indian watershed. In East Asia, Yoon et al. (2020) found that the Evaporative Stress Index (ESI) showed higher sensitivity to drought events in South Korea compared to other indices. Likewise, recent studies have highlighted the usefulness of long-term satellite-based precipitation datasets for capturing regional drought dynamics. For example, in the Sudano–Sahelian zone of Nigeria, a spatio-temporal analysis using CHIRPS rainfall data effectively revealed multi-decadal rainfall recovery trends and growing season shifts (Usman et al., 2018). Similarly, a study in Pakistan’s Tharparkar region integrated CHIRPS rainfall estimates with Normalized difference vegetation index (NDVI) to monitor drought vari- 

ability, emphasizing the critical link between precipitation patterns and vegetation productivity in arid environments (Usman and Nichol, 2020). Several researchers also examined long-term drought trends: Gu¨ner Bacanli (2017) applied the Standardized Precipitation Index (SPI) and Sen’s method in Turkey, Han et al. (2020) used slope analysis with RS indices, and Okal et al. (2020) integrated SPI and Standardized Precipitation Evapotranspiration Index (SPEI) with satellite data to map drought patterns in Kenya. A wide range of drought indices has been developed to facilitate the monitoring and assessment of different drought types, including meteorological, hydrological, and agricultural droughts. Among these, several indices are based on precipitation deficits, such as the Palmer Drought Severity Index (PDSI) (Palmer, 1965), the SPI (McKee et al., 1993), and the SPEI (Vicente-Serrano et al., 2010). Others rely on hydrological and soil moisture parameters, such as the Standardized Runoff Index (SRI) (Shukla and Wood, 2008a,b) and the Standardized Soil Moisture Index (SSMI) developed specifically for agricultural drought monitoring (Carra˜o et al., 2016). Despite their widespread application, most of these indices address only specific dimensions of drought such as rainfall anomaly (e.g., SPI, SPEI), soil moisture scarcity (e.g., SSMI), or runoff deficiency (e.g., SRI) and therefore fall short in capturing the multifaceted nature of drought events. Furthermore, indices derived solely from individual meteorological variables cannot comprehensively represent the spatial complexity and impact of agricultural droughts. Stationbased meteorological observations, although valuable, often fail to adequately reflect the spatial variability and extent of drought conditions across large areas. In this context, the integration of multi-source datasets enabled by RS technologies has emerged as a powerful tool for large-scale drought monitoring (Ghulam et al., 2007; Peters et al., 2002). RS not only facilitates spatially continuous observation but also allows for the synergistic analysis of multiple environmental variables. However, the characterization of agricultural drought, which is inherently influenced by diverse and uncertain factors such as crop type, disease outbreaks, soil conditions, and field management practices, presents a unique challenge. Consequently, univariate drought indices are often insufficient for accurately detecting, quantifying, and forecasting drought-related dynamics (Charusombat and Niyogi, 2011; Hao and AghaKouchak, 2014). To address these limitations, researchers have increasingly adopted bivariate analytical approaches a subset of multivariate analysis by integrating land surface temperature (LST) and vegetation condition indicators. Recent advances in RS have also improved the monitoring of LST and its relationship with vegetation and urban heat stress. For instance, MODIS-derived LST data were used to investigate urban heat island effects and temporal warming trends in Kano, Nigeria, illustrating the potential of satellite-based thermal indicators for evaluating surface temperature dynamics (Usman et al., 2025). One of the most widely used indices in this category is the Vegetation 

4223 

Advances in Space Research 77 (2026) 4222–4246 

##### M. Jahanbakhsh, M. Akhoondzadeh 

Health Index (VHI) (Kogan, 2002), which combines the VCI and the Temperature Condition Index (TCI) to provide a more comprehensive depiction of agricultural drought stress. Other notable bivariate indices include the LST/NDVI ratio (McVicar and Bierwirth, 2001) and SPEI (Vicente-Serrano et al., 2010). In Iran’s arid and semi-arid climate, numerous drought monitoring studies have been conducted at both national and regional levels using RS and meteorological data. Shamsipour et al. (2008) examined droughts in central plains using SPI and satellite imagery, while Zarei et al. (2013) assessed meteorological drought nationwide (2000–2005) using NOAA-AVHRR data. Damavandi et al. (2016) analyzed agricultural drought in Markazi Province via time-series satellite data, Tavazohi and Nadoushan (2018) evaluated drought in the Zayandeh-Rud Basin using SPI and RS indices. Heydari et al. (2018) forecasted drought using AVHRR vegetation indices from 1985 to 2008. Behrang Manesh et al. (2019) studied meteorological agricultural drought links across various Iranian climates. Golestan Province, situated in northeastern Iran along the southern coast of the Caspian Sea, holds strategic importance in the country’s agricultural sector due to its fertile soils, diverse landscapes, and relatively favorable climatic conditions. In recent years, however, the province has been increasingly affected by frequent and severe drought events, which have posed serious threats to agricultural productivity, water resources, and ecosystem stability. Although several studies have investigated meteorological droughts in the region using station-based precipitation data and standardized indices such as SPI and SPEI, these efforts have primarily focused on climatic trends and rainfall variability (Jahdi and Hanifepour, 2024; Pirnia et al., 2018). While useful, such univariate analyses often suffer from limited spatial representation and fall short in capturing the multidimensional nature of agricultural drought, which is influenced by complex interactions between vegetation condition, temperature stress, and land surface processes. Moreover, no research has specifically examined how land use and land cover (LULC) influence drought risk in Iran under varying climate change scenarios. Although the existing literature highlights the potential links between drought and climate change, key challenges persist. A primary issue is the lack of integrated studies that comprehensively analyze land use in relation to drought vulnerability. Most current research tends to evaluate either climate change or land use change in isolation, even though their interrelationship can have a substantial effect on drought dynamics. 

Despite Golestan’s critical role in Iran’s agricultural economy, comprehensive investigations that integrate multi-source and multi-index RS data for agricultural drought assessment remain scarce. Previous studies have primarily focused on meteorological droughts or relied on univariate indices such as the SPI and SPEI. While these indicators are valuable for detecting rainfall anomalies, they are insufficient to fully capture vegetation stress and surface thermal responses. Moreover, the influence of 

LULC on drought vulnerability has not been systematically examined in Iran or in most RS–ML drought studies worldwide, even though different land-cover classes (e.g., cropland, forest, rangeland) respond differently to moisture deficits. This represents a key knowledge gap in understanding the spatial heterogeneity of drought impacts. Another limitation in the existing literature is the lack of forward-looking, provincial-scale prediction frameworks. Most studies have focused on retrospective analyses of historical droughts, with only limited use of advanced machine learning models for near-future forecasting. The main objective of this study is therefore to develop and validate an integrated, cloud-based framework for long-term monitoring and near-term forecasting of agricultural drought in Golestan Province, northern Iran. Specifically, the study (1) analyzes drought dynamics from 2001 to 2024 using the VHI derived from MODIS NDVI and LST data, (2) forecasts agricultural drought conditions through 2028 using ensemble machine learning regression models, and (3) investigates the relationship between drought severity, precipitation variability, and dynamic LULC classes derived from the Sentinel-based Dynamic World dataset. This integrated approach advances previous research by explicitly linking LULC dynamics with drought vulnerability and by combining multi-sensor satellite observations with predictive modeling, thereby providing a novel and operational framework for early warning, agricultural planning, and drought risk management in data-scarce regions. 

### 2. Materials and study area 

### 2.1. Study area 

Golestan Province, located in northeastern Iran between latitudes 36°25′N to 38°8′N and longitudes 53°57′E to 56°22′E, covers an area of approximately 21,000 km<sup>2</sup> and is home to a population of around 1.86 million people (Fig. 1). It holds strategic significance in Iran’s agricultural landscape due to its fertile plains, diverse terrain, and climatic variability. The province encompasses a wide range of topographic features including the high Alborz Mountains in the south, salt marshes and coastal lowlands in the north, and loess hills in the west. Elevation across the province varies substantially, ranging from −26 m to 2,460 m in the north–south direction, and from −10 m to 1,110 m in the west east direction (Governorship, 2016).Climatic conditions in Golestan are notably heterogeneous. Based on 30-year meteorological records (1987–2017) from the Iran Meteorological Organization, annual precipitation ranges from 290 mm at Marze Artesh Station in the north to 600 mm at Shirinabad in the south over just 50 km, and from 460 mm in the west (Bandar Turkmen) to 370 mm in the east (Maraveh Tappeh) across a 200 km span. Average annual temperature ranges from 18.2 °C to 14.9 °C in the north–south direction, and from 

4224 

M. Jahanbakhsh, M. Akhoondzadeh 

Advances in Space Research 77 (2026) 4222–4246 



Fig. 1. Study area of Golestan Province, Iran, showing the topography and administrative boundaries. The two red dots indicate the representative sites selected for detailed hydroclimatic comparison: Site 1 located in cropland classified as Severe Drought in 2024, and Site 2 located in forest classified as No Drought in 2024. These sites were used in Section 3.5 for the analysis of SPI and ESI. 

18.2 °C to 18.0 °C west to east (Governorship, 2016). The province contains two major river systems: Gorgan Roud and Atrak Roud, both originating in Northern Khorasan Province. Gorgan Roud traverses over 250 km through the Gorgan Plain before discharging into the Caspian Sea, while Atrak Roud flows for more than 670 km, forming part of the border between Iran and Turkmenistan. Their average annual discharges are estimated at 1.08 × 10<sup>8</sup> m<sup>3</sup> /year and 4.7 × 10<sup>8</sup> m<sup>3</sup> /year, respectively. However, due to excessive agricultural extraction, Atrak Roud typically reaches the Caspian Sea only during flood events (Governorship, 2016). In terms of land use, approximately 42 % of the province is covered by rangelands, 35 % by agricultural land (including irrigated fields, rainfed farms, and orchards), and 22 % by forested areas, with the remaining 1 % comprising salt marshes, playas, and urban settlements (Governorship, 2016). Most of the population is concentrated in a narrow central corridor, with density sharply decreasing toward the north and east. Golestan has witnessed rapid population growth of 9.4 % since the 2011 census alongside substan- 

tial rural-to-urban migration, particularly toward Gorgan, the provincial capital. Water scarcity has become increasingly critical in the province. Groundwater, which serves as the main source for drinking and irrigation, is under significant stress due to overextraction. This has resulted in declining groundwater levels, saline water intrusion, reduced water quality, and land subsidence. In some northern areas, historical rainwater harvesting systems once vital for livestock and domestic use have become largely ineffective due to prolonged droughts and reduced rainfall (Jafari Shalamzari et al., 2016; Zehtabian et al., 2009). The situation is further complicated by fragmented water governance. While the Iran Meteorological Organization manages climate data, the Ministry of Energy oversees water supply, wastewater treatment, and hydropower, and the Forests, Range, and Watershed Management Organization is responsible for watershed conservation. The lack of integration across these institutions has hindered effective water and drought management in Golestan Province (Ardakanian, 2005; Madani, 2014). 

4225 

M. Jahanbakhsh, M. Akhoondzadeh 

Advances in Space Research 77 (2026) 4222–4246 

### 2.2. Data acquisition and preprocessing 

### 2.2.1. Vegetation and land surface temperature data 

In this study, agricultural drought conditions were assessed using indicators that simultaneously capture thermal stress and vegetation health. Surface temperature variability was characterized using the MOD11A2 Version 6.1 product (MODIS/Terra Land Surface Temperature and Emissivity (which provides daytime LST data at 1 km spatial resolution and an 8-day temporal interval. LST plays a key role in identifying drought-induced thermal anomalies and is essential for the derivation of TCI. To ensure spatial consistency with the LST data, the MOD13A2 Version 6.1 product (MODIS/Terra Vegetation Indices) was utilized to obtain the NDVI. Although MODIS offers vegetation indices at higher spatial resolutions (e.g., MOD13Q1 at 250 m), the 1 km resolution of MOD13A2 was preferred to maintain compatibility with the LST product and to avoid scale mismatches during index calculations. Both MODIS products were accessed and processed within the Google Earth Engine (GEE) cloud computing environment, covering the period from January 2001 to December 2024. Monthly median composites of LST and NDVI were generated to reduce the influence of noise and cloud contamination. Subsequently, the TCI was computed from monthly LST, and the VCI was derived from monthly NDVI. Finally, these two indices were integrated to calculate the VHI, which serves as a bivariate drought indicator reflecting both vegetation vigor and temperature-induced stress. 

### 2.2.2. Precipitation and evaporative stress data 

To complement the assessment of agricultural drought conditions based on the VHI, two additional hydroclimatic datasets were incorporated into the analysis. These variables were used to enhance the classification of drought and non-drought zones and to examine their correspondence with vegetation-based drought indicators across the study area. Daily precipitation estimates were acquired from the PERSIANN-CDR (Precipitation Estimation from Remotely Sensed Information using Artificial Neural Networks – Climate Data Record) dataset, which provides high-resolution (0.25°) global precipitation data since 1983. This dataset was developed using artificial neural networks applied to longwave infrared imagery from geostationary satellites and was bias corrected with monthly precipitation data from the Global Precipitation Climatology Project (GPCP) to improve accuracy for long-term climatic studies (Ashouri et al., 2015). In this study, daily data were aggregated into annual totals for the period 2001–2024 and subsequently used to calculate the SPI for evaluating meteorological drought conditions. In parallel, the ESI was utilized to identify short-term anomalies in evapotranspiration rates and surface moisture. This thermal-based index is produced by the NOAA Center for Satellite Applications and Research (STAR) in cooperation with the USDA-ARS Hydrology and RS Laboratory. The ESI cap- 

tures deviations in actual evapotranspiration (ET) derived from satellite-observed LST, which responds rapidly to changes in soil moisture content. Because of this sensitivity, the ESI is particularly effective in detecting flash drought events and crop water stress. ET estimates in the ESI framework are derived using an energy balance model, following the principles described by Anderson et al. (2007a, b). 

### 2.2.3. Land Use and Land Cover (LULC) data 

LULC data were obtained from the Dynamic World dataset (Version 1), a near real-time (NRT) global 10meter resolution product developed by Google and the World Resources Institute, based on Sentinel-2 Level-1C imagery and a deep learning classification model (Brown et al., 2022). The dataset provides per-pixel class probabilities and corresponding ‘‘Top 1” labels for nine LULC categories: water, trees, grass, flooded vegetation, crops, shrub & scrub, built area, bare ground, and snow & ice. To ensure temporal consistency and reduce noise caused by cloud cover, all available Dynamic World images for the summer season of 2024 (from June 1 to August 31) were retrieved and processed using mode compositing. In this approach, the most frequently occurring land cover class (i.e., the statistical mode of the ‘‘Top 1” labels) was calculated for each pixel over the three-month period. This composited LULC map was subsequently used to investigate spatial relationships between land cover patterns and drought conditions as measured by vegetation and thermal drought indices. All processing and image filtering were conducted using GEE, and only scenes with cloud cover below 35 % (based on Sentinel-2 metadata) were included to ensure data quality and spatial completeness. A summary of all datasets used in this study is provided in Table 1. 

### 3. Methodology 

A systematic and well-organized procedure was adopted in this study for data collection and processing, ensuring alignment with the research objectives. Each phase was deliberately designed to match the specific requirements of the analysis. An overview of the methodology is illustrated in the flow chart presented in Fig. 2. 

### 3.1. Monthly computation of multivariate agricultural drought indicator 

To capture the vegetation health component of agricultural drought, the NDVI was derived from the MODIS MOD13A2 Version 6.1 product. NDVI, a widely recognized indicator of photosynthetic activity and vegetation vigor, was computed using the standard equation (Huang et al., 2021): 



where BNIR and BRED represent the reflectance values in the near-infrared and red spectral bands, respectively. To 

4226 

M. Jahanbakhsh, M. Akhoondzadeh 

Advances in Space Research 77 (2026) 4222–4246 

Table 1 

Summary of datasets used in this study, including their sources, spatial and temporal resolutions. 

|Products|PERSIANN-CDR|NOAA Evaporative Stress Index (ESI)|MOD13A2 V6.1|MOD11A2 V6.1|Dynamic World V1|
|---|---|---|---|---|---|
|Bands Name|Precipitation|ESI_12wk|NDVI|LST|Label|
|Temporal Resolution|Daily|Weekly|16-day|8 days|2015-now|
|spatial Resolution(km)|27.83|4|1|1|0.01|





Fig. 2. The flowchart summarizes the key steps of data acquisition, preprocessing, and analysis. 

minimize the influence of transient noise such as atmospheric disturbances and cloud cover, the median value of all NDVI observations within each month was calculated, resulting in a single representative NDVI image per month. The VCI which normalizes NDVI values to reflect vegetation stress relative to historical conditions, was subsequently computed for each pixel using the following equation (Kogan, 1990): VCI NDVIi NDVImin NDVImax NDVImin 100 



where NDVI i is the monthly median NDVI value, and NDVI min and NDVI max denote the minimum and maximum NDVI values for each pixel, respectively. This index effectively quantifies vegetation anomalies linked to drought conditions. To incorporate thermal stress into the drought assessment, the MOD11A2 Version 6.1 product, which provides 8-day composites of LST, was employed. Like the NDVI processing, the median LST was calculated for each month to generate a single monthly 

LST image, thereby reducing the influence of outliers and noise. The TCI was derived from the monthly LST data using the following formula (Kogan, 1997): 

TCI LSTmax LSTi LSTmax LSTmin 100 



where LST i is the monthly median LST, and LSTmin and LST max represent the historical minimum and maximum LST values for each pixel. TCI provides a normalized measure of thermal anomalies, with higher TCI values indicating less thermal stress. To comprehensively assess agricultural drought by integrating both vegetation and thermal stress factors, the VHI was computed as a weighted combination of VCI and TCI (Kogan, 2002): VHI a VCI 1 a TCI 4 

where a is the weighting coefficient, commonly set to 0.5 to assign equal importance to vegetation and temperature conditions. This procedure was systematically applied across the entire study area for each month during the per- 

4227 

Advances in Space Research 77 (2026) 4222–4246 

##### M. Jahanbakhsh, M. Akhoondzadeh 

iod 2001 to 2024, resulting in a monthly time series of VCI, TCI, and VHI. These indices form the foundation for subsequent drought classification, temporal trend analysis, and forecasting processes described in the following sections. 

3.2. Temporal dynamics and classification of agricultural drought (2001–2024) 

### 3.2.1. Optimal accumulation period for VHI trend analysis & slop map 

To analyze the long-term evolution of agricultural drought, the study focused on the summer season (June– August), which represents the peak period of vegetation water stress in Golestan Province. For each year from 2001 to 2024, monthly VHI layers corresponding to June, July, and August were extracted and averaged on a pixel basis to generate a single summer composite VHI map per year. This temporal aggregation reduced short-term fluctuations and emphasized the interannual drought signal during the critical dry period. All annual VHI composites were organized into a multi-year stack, and a pixel-based linear trend analysis was performed to estimate the direction and magnitude of change in vegetation health over time. The regression slope for each pixel expresses the rate of VHI change, allowing spatial identification of improving or degrading drought conditions. Prior to trend estimation, non-valid and background pixels were masked to eliminate artifacts, and only pixels with sufficient valid observations were included in the analysis. The resulting slope map was generated at the same spatial resolution and projection as the original VHI dataset. 

### 3.2.2. Classification of agricultural drought severity based on VHI thresholds 

To facilitate interpretation and communication of drought severity, VHI values were classified into discrete drought severity classes. This classification followed widely accepted thresholds proposed by Kogan (2002) and further applied in monitoring drought (Gidey et al., 2018; Kloos et al., 2021; Serban and Maftei, 2025; Viet and Thuy, 2024).The thresholds and corresponding drought severity classes used in this study are summarized in Table 2. 

Using these thresholds, each summer VHI image was reclassified to produce annual drought severity maps for the entire study area. These classified maps enabled a spa- 

tial understanding of drought intensity and distribution trends over time. 

3.2.3. Spatio-temporal change detection of drought conditions (2001–2024) 

To assess how drought severity classes have changed over time, two complementary analyses were performed: 

In the first step, the temporal trend of each drought class’s spatial extent was calculated using linear regression. This analysis provided insight into whether the area covered by each drought class increased or decreased over the 24-year period. For instance, a negative trend in the ‘‘No Drought” class indicates an expansion of droughtaffected areas, while a positive trend in the ‘‘Severe Drought” class reflects increasing drought severity. In the second step, the area covered by each drought class was computed annually. These areas were then expressed as percentages of the total study area, allowing for consistent comparison across years. The percentage change in area for each drought class was also calculated over the full study period to quantitatively assess the long-term shifts in drought severity. This spatio-temporal analysis provides a critical basis for targeted drought mitigation and agricultural risk management strategies. 

### 3.3. Machine learning regression models for drought 

### prediction (2024–2028) 

In recent years, machine learning regression models such as Random Forest (RF) and Extreme Gradient Boosting (XGBoost) have gained remarkable attention in environmental and drought prediction studies owing to their ability to model complex nonlinear relationships, achieve high predictive accuracy, and reduce overfitting tendencies (Hussain et al., 2025; Piraei et al., 2024; Zeng et al., 2025). In this study, two complementary modeling approaches were developed to assess agricultural drought dynamics. These algorithms were not intended for direct performance comparison; rather, they are considered to represent two distinct predictive strategies. The RF algorithm, originally introduced by Breiman (2001), is an ensemble learning method in which multiple decision trees are constructed using bootstrapped subsets of both the training data and predictor variables. Final predictions are generated by aggregating the outputs of all trees, 

Table 2 

Agricultural drought severity classification based on VHI thresholds. 

|Drought Class|VHI Range|Severity descriptio n|
|---|---|---|
|Extreme Drought|0–10|Severe vegetation stress, crop failure likely|
|Severe Drought|Oct-20|High stress, significant crop damage|
|Moderate Drought|20–30|Visible stress, reduced crop yield|
|Light Drought|30–40|Slight stress, early warning stage|
|No Drought 1|40–60|Normal vegetation conditions|
|No Drought 2|60–100|Healthy vegetation, optimal growth|



4228 

Advances in Space Research 77 (2026) 4222–4246 

##### M. Jahanbakhsh, M. Akhoondzadeh 

thereby reducing model variance and enhancing generalization. In the present study, the RF model was trained using 100 trees. The XGBoost algorithm, proposed by Chen and Guestrin (2016), represents an advanced implementation of gradient boosting. Trees are sequentially built, with each subsequent tree designed to correct the residual errors of its predecessors. Regularization, shrinkage, and column subsampling are incorporated within XGBoost to enhance computational efficiency and mitigate overfitting. In this study, hyperparameters of the XGBoost model were optimized through a randomized search procedure, including the number of boosting trees (100–300), maximum tree depth (3–10), learning rate (0.01–0.1), subsampling ratio of training instances (0.7–0.9), and subsampling ratio of features per tree (0.7–0.9). Both RF and XGBoost models were trained and evaluated using the VHI time series to predict agricultural drought conditions across Golestan Province. The modeling workflow consisted of two main phases, validation and forecasting. In the validation phase, annual VHI maps from 2001 to 2020 were used to train each model, and the trained models were employed to predict VHI for 2021, 2022, 2023, and 2024. Model outputs were compared against the corresponding MODISderived VHI maps to assess predictive accuracy and temporal transferability. Three performance indicators were used for evaluation: the coefficient of determination (R<sup>2</sup> ), root mean square error (RMSE), and mean absolute error (MAE), providing complementary measures of model accuracy and bias. Following this validation, the model achieving the highest average R<sup>2</sup> and lowest RMSE and MAE values across the test years was selected as the optimal model for long-term forecasting. In the forecasting phase, this optimal model was retrained using the full 2001–2024 VHI dataset and then applied to predict VHI for the summer of 2028. The resulting 2028 VHI map represents a data-driven projection derived from historical patterns and learned dependencies within the vegetation health records. Although future uncertainties are unavoidable due to the absence of actual observations, the forecast provides a scientifically grounded outlook on potential drought severity under ongoing climatic and vegetation dynamics. To further interpret drought risk evolution, the predicted 2028 VHI map was reclassified into drought severity categories using the same thresholds as defined in Table 2. A comparative spatial analysis between 2024 and 2028 drought classes was subsequently performed to detect transitions indicating either intensification or alleviation of drought conditions. This forward-looking assessment provides valuable insights for proactive agricultural management, ecosystem monitoring, and drought risk mitigation planning across Golestan Province. 

3.4. Analysis of the relationship between LULC and drought severity classes 

To elucidate the interplay between land surface characteristics and agricultural drought dynamics, a comprehen- 

sive analysis was conducted to examine the relationship between LULC types and drought severity classes derived from the VHI. The analysis employed the Dynamic World Version 1 dataset, a high-resolution (10 m) near real-time land cover product generated from Sentinel-2 Level-1C imagery using a deep learning classification model (Brown et al., 2022). Recognizing the seasonal variability of land cover and the frequent presence of clouds in optical imagery, all available LULC maps for the summer of 2024 (June to August) were aggregated, and a per-pixel mode composite was computed. This approach ensured that the most frequent land cover label at each pixel was retained, resulting in a temporally stable and cloud-free 9-class LULC map that aligned temporally with the VHI drought analysis for the same period. Given the spatial resolution discrepancy between the LULC and VHI datasets, the LULC map was resampled to match the 1 km VHI grid using nearest-neighbor interpolation, preserving the categorical integrity of the land cover classes. Following spatial harmonization, two complementary analyses were performed. First, for each LULC class such as cropland, forest, shrubland, and urban the mean, standard deviation, maximum, and minimum values of VHI were calculated to assess vegetation health and drought sensitivity across land cover types. Second, a pixel-wise cross-tabulation was carried out to determine the distribution of VHI drought classes within each LULC category. This allowed quantifying the relative exposure of different land use types to varying levels of drought severity. By integrating continuous VHI metrics with categorical drought class distributions, this dual analytical approach offered a nuanced understanding of the spatial correlation between land use patterns and drought stress. 

3.5. Assessing the link between agricultural drought, precipitation, and evaporative stress 

To enhance understanding of the environmental controls on agricultural drought intensity across Golestan Province, this study examined the relationship between drought severity classes derived from VHI and two major hydrometeorological factors: precipitation and evaporative stress. Precipitation data were obtained from the PERSIANN-CDR dataset, which provides highresolution, bias-corrected daily rainfall estimates from satellite observations (Ashouri et al., 2015). These daily values were aggregated into annual precipitation totals for each year from 2001 to 2024 to analyze long-term rainfall variability across the study area. To investigate the influence of hydroclimatic conditions on different drought severity classes, two representative locations were selected, each situated within distinct drought and land cover zones based on the 2024 VHI classification. The first location was placed in an area experiencing severe drought within agricultural land, while the second represented an area with no drought located in forested land. These two contrasting sites, whose positions are shown in Fig. 1, were chosen to 

4229 

Advances in Space Research 77 (2026) 4222–4246 

##### M. Jahanbakhsh, M. Akhoondzadeh 

highlight the environmental gradients that influence drought severity across different ecosystems. 

At both sites, the SPI was calculated using the annual precipitation time series, following the formulation introduced by McKee et al. (1993): SPI Pi l r 5 

where Pi denotes the annual precipitation for i year, l and r represent the long-term mean and standard deviation of precipitation, respectively. The resulting SPI values were compared across the two sites to examine how rainfall deficits may have contributed to the emergence of distinct drought classes in 2024. 

In parallel, the ESI was also assessed at both locations to evaluate differences in surface moisture stress. The ESI, developed by Anderson et al. (2007a, b). Evapotranspiration and ESI values between two sites characterized by different VHI drought classes, the study highlights how precipitation anomalies and evapotranspiration stress jointly influence the spatial distribution of agricultural drought severity. This analysis underscores the importance of integrating multiple hydroclimatic indicators to better interpret and predict drought impacts across heterogeneous land systems. 

### 4. Results and discussion 

### 4.1. Spatiotemporal dynamics of agricultural drought indicator (2001–2024) 

Monthly time series of the VCI, TCI, and VHI were analyzed from 2001 to 2024 to assess the evolution of agricultural drought conditions across Golestan Province. Fig. 3 present the trends of these indices over time. As shown in Fig. 3, the VCI an indicator of vegetation greenness and moisture availability exhibits a generally decreasing trend in many regions, which signifies progressive 

vegetation stress and supports the presence of agricultural drought. Conversely, Fig. 3 shows an increasing trend in TCI values over time. An increasing trend in TCI would typically reflect intensifying drought. Although monthly VHI trends were not steep, to better capture interannual drought dynamics, the summer-season VHI (June–August) was extracted for each year, a noticeable decline was evident (Fig. 4). Interannual variability was also observed, with temporary improvements during relatively wet years (e.g., 2009, 2020), followed by sharp declines in dry years (e.g., 2010, 2021, 2006). A linear regression was applied to the 24-year summer VHI time series for each pixel to generate a slope map, revealing spatial trends in drought severity. Fig. 5 displays the resulting slope map. The interpretation of slope values is as follows: Slope = 0 represents a stable condition, indicating no significant change in drought severity. Slope > 0 denotes an increasing VHI trend, meaning improving vegetation health and reduction in drought severity. Slope < 0 indicates a declining VHI trend, corresponding to worsening drought conditions and vegetation stress. Fig. 5 visualizes these spatial dynamics across the province. Areas with positive slopes (shaded in red) signify regions where VHI has increased over time, highlighting areas where drought severity is decreasing. Conversely, negative slopes (blue to orange areas) mark locations with decreasing VHI, possibly due to land use shifts. This slope-based analysis provides a spatially explicit understanding of drought evolution and helps identify persistent hotspots of agricultural stress. Such information is essential for agricultural planning, drought risk mitigation, and the development of early warning systems in climate-sensitive regions. 

### 4.2. Drought severity classification and trends over time 

To provide a comprehensive understanding of drought evolution across Golestan Province, the VHI was catego- 



Fig. 3. Monthly Temporal trends of TCI, VCI, and VHI, showing seasonal and interannual variability over the study area. 

4230 

M. Jahanbakhsh, M. Akhoondzadeh 

Advances in Space Research 77 (2026) 4222–4246 



Fig. 4. Annual time trends of VHI show seasonal and interannual variability in the study area (2001–2024). 

rized into six standard drought severity classes using the thresholds proposed by Kogan (2002). Summer-season VHI classification maps from 2001 to 2024 (Fig. 6) were analyzed to track the spatial distribution and temporal changes in agricultural drought severity. Long-term trends between 2001 and 2023 demonstrate a general intensification of drought conditions. As shown in Table 3, the area under extreme drought increased from 179 km<sup>2</sup> in 2001 to 2,224 km<sup>2</sup> in 2023 an alarming growth of more than 1,100 %. Simultaneously, the No Drought 2 class declined from 183 km<sup>2</sup> to just 6 km<sup>2</sup> , a 96.7 % decrease. These findings reflect the broad-scale degradation of vegetation health and the expansion of drought-affected areas over two decades, culminating in a critical situation by 2023. However, the comparison between 2001 and 2024 presents a more nuanced narrative. In 2024, a notable reduction in extreme drought was observed, shrinking from 2,224 km<sup>2</sup> in 2023 to just 1 km<sup>2</sup> , suggesting a temporary recovery. Similarly, No Drought 2 increased from 6 km<sup>2</sup> in 2023 to 741 km<sup>2</sup> in 2024, indicating partial vegetation recovery and a possible response to improved climatic conditions. Despite this, the area under moderate and light drought remained high, suggesting that while conditions in 2024 were less severe compared to 2023, drought persists over much of the province. This short-term improvement in 2024 aligns with historical fluctuations observed over the study period. Although the overall trend is clearly increasing as confirmed by the slope map (Fig. 5) and the time ser- 

ies in Fig. 4 interannual anomalies have been present. For example, following the severe drought years of 2016 and 2017, a period of relative improvement occurred in 2019, characterized by a temporary increase in VHI values and reduced drought severity. However, this recovery was short-lived, as drought severity sharply intensified again in 2021, marking one of the worst years in the time series. These oscillations or drought anomaly patterns reflect the high climate variability and sensitivity of Golestan’s ecosystems to both regional weather shifts and global climatic influences. In summary the drought severity classification and trend analysis reveal a dual dynamic: (1) a longterm intensification of agricultural drought conditions across Golestan Province, evident in the expansion of severe and extreme drought classes and the contraction of no drought areas; and (2) noticeable short-term anomalies and episodic recoveries, such as those observed in 2019 and 2024, which briefly interrupted the overall deteriorating trend. Notably, Fig. 7 provides a valuable time-series visualization of drought class transitions, offering a class-wise breakdown of changes over the 24-year period. By tracking the spatial extent of each class annually, this figure not only illustrates the dominance of moderate and severe droughts in recent years but also quantifies the temporary regressions and improvements in specific drought categories. Such granular trend insights are critical for understanding drought trajectories and for informing region-specific mitigation, adaptation, and early-warning strategies. 

4231 

M. Jahanbakhsh, M. Akhoondzadeh 

Advances in Space Research 77 (2026) 4222–4246 



Fig. 5. Spatial distribution of the linear trend (slope) of the summer VHI across Golestan Province from 2001 to 2024. The slope values were derived from pixel-wise linear regression of summer (June–August) VHI time series. Positive slope values (red tones) indicate increasing VHI trends, corresponding to improving vegetation health and decreasing drought severity, whereas negative slope values (blue to orange tones) represent declining VHI trends, reflecting worsening vegetation health and intensifying drought conditions. Slope = 0 indicates stable conditions with no significant change in drought severity. 

4.3. Model validation: predicting drought with machine learning (2021–2024) 

To evaluate the capability of machine learning algorithms in forecasting agricultural drought severity, two ensemble regression models RF and XGBoost were employed. Both models were trained on historical VHI 

data spanning 2001–2020 and subsequently validated using independent MODIS-based VHI maps for 2021–2024, following a temporal validation scheme instead of a conventional random split. This strategy ensures that model performance is assessed in future, unseen periods, providing a realistic measure of their predictive skill. The objective of this analysis was not to perform a direct 

4232 

M. Jahanbakhsh, M. Akhoondzadeh 



<!-- Start of picture text -->
Advances in Space Research 77 (2026) 4222–4246<br><!-- End of picture text -->



Fig. 6. Spatiotemporal distribution of drought severity across the study area from 2001 to 2024, classified into five drought intensity levels based on the VHI. 

Table 3 

Changes in drought severity classes between 2001, 2023, and 2024 in Golestan Province. 

|Class|2001–2024||||2001–2023|||
|---|---|---|---|---|---|---|---|
||Area 2001 (km<sup>2</sup>)|Area 2024 (km<sup>2</sup>)|Change (km<sup>2 </sup>)|Change (%)|Area 2023 (km<sup>2</sup>)|Change (km<sup>2 </sup>)|Change (%)|
|Extreme Drought|179|1|−178|−99.44|2224|2045|1142.45|
|Severe Drought|10420|4197|−6223|−59.72|10420|0|0|
|Moderate Drought|5138|9105|3969|77.2|4633|−505|−9.82|
|Light Drought|3421|4513|1092|31.92|3274|−147|−4.29|
|No Drought 1|6203|7030|827|13.33|5030|−1173|−18.91|
|No Drought 2|183|741|558|304.91|6|−177|−96.72|



comparison between the two algorithms, but rather to illustrate two complementary approaches for drought prediction. The RF model was implemented with 100 trees, using standard hyperparameter settings to ensure robustness and interpretability. In contrast, the XGBoost model underwent hyperparameter optimization through Randomized Search, tuning five key parameters (learning_rate, max_depth, subsample, colsample_bytree, and n_estimators) to fully leverage its boosting-based learning and regularization strengths. As shown in Figs. 8 and 9, both 

models exhibited strong predictive performance, with high spatial consistency and relatively low errors across the study area. Quantitative evaluation metrics (Table 4) suggest that XGBoost slightly outperformed RF in most years, which may be attributed, at least in part, to the advantages conferred by the model optimization process. As presented in Figs. 8 and 9, both models demonstrated strong predictive performance with high spatial agreement and relatively low error levels across the study region. However, based on quantitative evaluation metrics (Table 4), XGBoost slightly 

4233 

M. Jahanbakhsh, M. Akhoondzadeh 

Advances in Space Research 77 (2026) 4222–4246 



Fig. 7. Temporal trends in the spatial extent of agricultural drought severity classes across Golestan Province (2001–2024). 

outperformed RF in most years. Specifically, the average R<sup>2</sup> across the four validation years was 0.85 for XGBoost compared to 0.83 for RF. Similarly, RMSE and MAE were marginally lower for XGBoost, with average values of RMSE ≈ 0.0601 and MAE ≈ 0.0385, compared to RMSE ≈ 0.0640 and MAE ≈ 0.0396 for RF. These differences, although relatively small, consistently favored XGBoost. Given this consistent yet modest edge in predictive accuracy, XGBoost was selected as the preferred model for drought forecasting in the subsequent analysis. Its superior performance highlights the model’s strong generalization capacity, ability to handle complex environmental interactions, and suitability for spatiotemporal drought prediction based on RS inputs. 

### 4.4. Forecasting future drought conditions in 2028 

Based on the validated performance of machine learning models in Section 4.3, the XGBoost model, which demonstrated superior accuracy, was selected to forecast agricultural drought conditions for the summer of 2028 across Golestan Province. The model was retrained using the 

complete historical dataset from 2001 to 2024, incorporating VHI. The resulting VHI prediction map for 2028 (Fig. 10) was then classified into six drought severity classes using the standard thresholds defined in Table 2. The spatial distribution of forecasted drought severity reveals a significant intensification of drought stress compared to 2024. As shown in Table 5, the area under Extreme Drought is projected to rise dramatically from 1 km<sup>2</sup> in 2024 to 3,126 km<sup>2</sup> in 2028, reflecting a staggering 3,125 km<sup>2</sup> increase (equivalent to +312,500 %). Similarly, Severe Drought is expected to expand from 4,197 km<sup>2</sup> to 10,046 km<sup>2</sup> , marking a 139.4 % increase. Together, these two most critical drought categories will likely cover more than 13,000 km<sup>2</sup> , or roughly 62 % of the province, by 2028. In contrast, the No Drought classes are projected to decline sharply. The No Drought 2 category completely disappears, while No Drought 1 shrinks from 7,030 km<sup>2</sup> in 2024 to just 3,943 km<sup>2</sup> in 2028, a 43.9 % decrease. Additionally, Moderate Drought areas decreased by 7.3 %, and Light Drought by 53.4 %, suggesting that milder drought conditions may transition into more severe forms over time. These findings point to a clear deterioration in 

4234 

M. Jahanbakhsh, M. Akhoondzadeh 

Advances in Space Research 77 (2026) 4222–4246 



Fig. 8. Random Forest regression model performance in predicting VHI: observed vs. predicted values for the years 2021–2024. 

vegetation health and intensification of agricultural drought soon. Spatially, the most affected zones are projected to be concentrated in central and northern agricultural lands, which are already highly vulnerable due to high evapotranspiration rates and groundwater extraction. The disappearance of the No Drought 2 class underscores the severity of the situation, suggesting that even the healthiest areas in 2024 may not remain immune to worsening drought stress. The projected shift toward more extreme drought conditions aligns with the long-term downward trend in summer VHI values and is consistent 

with the model’s learned relationship between past vegetation stress, climatic variables, and drought progression. To further illustrate this trend, Fig. 11 presents the temporal evolution of average VHI across the entire province for both the historical period (2001–2024) and the forecasted years (2025–2028). The blue line represents observed and predicted average VHI values, while the red dashed line indicates the fitted linear trend (slope = –0.0014 yr<sup>−1</sup> ). The negative slope confirms a persistent decline in vegetation health over time, signifying an overall intensification of drought severity toward 2028. Notably, the predicted 

4235 

M. Jahanbakhsh, M. Akhoondzadeh 

Advances in Space Research 77 (2026) 4222–4246 



Fig. 9. XGBoost regression model performance in predicting VHI: observed vs. predicted values for the years 2021–2024. 

Table 4 

Performance comparison of Random Forest (RF) and XGBoost (XGB) models in predicting Vegetation Health Index (VHI) during independent validation years (2021–2024). 

|Year|R<sup>2 </sup>(RF)|R<sup>2 </sup>(XGB)|RMSE (RF)|RMSE (XGB)|MAE (RF)|MAE (XGB)|
|---|---|---|---|---|---|---|
|2021|0.7491|0.7682|0.0797|0.0766|0.0515|0.0512|
|2022|0.8501|0.8665|0.0651|0.0614|0.0406|0.0400|
|2023|0.7856|0.8027|0.0756|0.0728|0.0478|0.0473|
|2024|0.9663|0.9769|0.0358|0.0296|0.0185|0.0156|
|Average|0.8377|0.8535|0.0640|0.0601|0.0396|0.0385|



4236 

M. Jahanbakhsh, M. Akhoondzadeh 

Advances in Space Research 77 (2026) 4222–4246 



Fig. 10. Forecasted agricultural drought map for 2028 in Golestan Province derived from the machine learning model using VHI. Drought classes range from Extreme Drought (black) to No Drought (green). 

Table 5 

Changes in different drought severity classes between 2024 and 2028 in Golestan Province. 

|Class|2024–2028||||
|---|---|---|---|---|
||Area 2028 (km<sup>2</sup>)|Area 2024 (km<sup>2</sup>)|Change (km<sup>2 </sup>)|Change (%)|
|Extreme Drought|3126|1|3215|312500|
|Severe Drought|10046|4197|5849|139.36|
|Moderate Drought|4243|9105|−4862|−53.39|
|Light Drought|4184|4513|−329|−7.29|
|No Drought 1|3943|7030|−3087|−43.91|
|No Drought 2|0|741|−741|−100|



VHI value for 2028 is the lowest in the entire 28-year sequence, reinforcing the spatial evidence of widespread drought expansion depicted in Fig. 10. However, it is important to note that while the forecast assumes continuity of current patterns and drivers, actual 2028 conditions may vary due to unpredictable climatic factors, land use changes, or policy interventions. 

### 4.5. Relationship between LULC and drought severity 

Understanding how LULC types of influence drought vulnerability is essential for targeted drought risk reduction and land management. In this study, we analyzed the spa- 

tial relationship between LULC classes and drought severity levels, as defined by the VHI for the summer of 2024. The LULC map was derived from the Dynamic World V1 dataset at 10-meter resolution (Fig. 12). Land cover categories included croplands, trees (forests), shrub and scrub, grass, flooded vegetation, built-up areas, bare ground, and water bodies. Statistical analysis of mean VHI values across LULC classes revealed notable differences in drought susceptibility (Table 6). The bare land class exhibited the lowest average VHI (0.24), indicating extremely poor vegetation conditions or absence of vegetation altogether. This was followed by croplands and built-up areas, both with a mean VHI of 0.32, highlighting their exposure 

4237 

M. Jahanbakhsh, M. Akhoondzadeh 

Advances in Space Research 77 (2026) 4222–4246 



Fig. 11. Annual time trends of VHI show seasonal and interannual variability in the study area (2001–2028). 

to significant drought stress. In contrast, forested areas (trees) showed the highest VHI mean (0.55) with low variability, reflecting stable vegetation health and lower drought exposure. Grasslands and flooded vegetation showed moderate VHI means (≈0.48), while shrublands had slightly lower values (mean = 0.36), indicating intermediate levels of stress. Further insights were obtained by examining the pixel-wise distribution of VHI-derived drought classes within each land cover type (Table 7). Croplands were the most drought-affected category, containing 928 pixels under Severe Drought and 3,134 under Moderate Drought, confirming their high sensitivity to agricultural drought. Bare lands, although largely devoid of vegetation, still showed presence in moderate and severe drought classes, likely due to their elevated surface temperatures and influence on thermal indices. In contrast, forest areas were mostly classified under No Drought 1 and 2, with only a single pixel identified under severe drought, underscoring their relative resilience. Shrublands exhibited a wide range of drought classes, spanning from light to moderate and no drought, reflecting diverse vegetation responses in these semi-natural ecosystems. These results underscore a clear association between land cover type and vulnerability to drought. Croplands and bare soils, being highly modified and ecologically exposed, are more susceptible to drought-induced stress. This has direct implications for drought preparedness and land management, suggesting the need for adaptive measures such as soil sta- 

bilization in bare areas, implementation of efficient irrigation and crop rotation in agricultural zones, and protection or expansion of vegetated buffers. Conversely, the resilience observed in forested landscapes points to their ecological value as natural drought buffers, supporting the case for afforestation and ecosystem restoration in vulnerable regions. Overall, integrating land use-drought interactions into early warning systems and land policy can significantly improve the effectiveness of mitigation strategies. 

4.6. Hydroclimatic drivers of drought severity: SPI and ESI analysis 

To better understand the environmental mechanisms contributing to drought severity across Golestan Province, this section investigates two key hydroclimatic indicators: the SPI and the ESI. These indicators were analyzed at two representative locations with contrasting drought conditions in 2024, one situated in a Severe Drought zone within cropland, and the other in a No Drought zone within forested land. As shown in Fig. 13, annual precipitation between 2001 and 2024 demonstrates considerable variability, with notable dry periods in 2006, 2010, 2021, and 2023. The SPI trends at both locations, presented in Figs. 14 and 15, reflect this variability. Both sites exhibit a long-term downward trend in SPI, indicating increasing precipitation deficits over time. However, this declining 

4238 

M. Jahanbakhsh, M. Akhoondzadeh 

Advances in Space Research 77 (2026) 4222–4246 



Fig. 12. Spatial distribution of land use and land cover types in 2024. 

Table 6 

Statistical analysis of VHI values across different LULC classes. 

|LULC Class|VHI Mean|VHI<br>Std|VHI<br>Max|VHI<br>Min|
|---|---|---|---|---|
|Water|0.37|0.12|0.66|0.15|
|Teres|0.55|0.06|0.65|0|
|Grass|0.48|0.08|0.61|0.27|
|Flooded Vegetation|0.48|0.02|0.51|0.45|
|Crops|0.32|0.1|0.68|0|
|Shrub & Scrub|0.36|0.08|0.59|0.17|
|Built|0.32|0.1|0.64|0.14|
|Bare|0.24|0.08|0.64|0|
|Snow & Ice|nan|nan|nan|nan|



trend is more pronounced in the cropland area, where SPI values dropped more sharply in recent years particularly in 2021 and 2023 corresponding to years of intense drought. In contrast, the forested site shows a similar but milder SPI decline, indicating less sensitivity to rainfall reduction, likely due to better canopy retention, soil moisture buffering, and microclimatic stability. Parallel to SPI, the ESI was analyzed to assess surface moisture stress. As shown in Figs. 16 and 17, the cropland site consistently recorded 

lower ESI values, especially during dry years, indicating higher evapotranspiration stress and reduced soil moisture availability. The forested area, by contrast, maintained relatively stable and higher ESI values, reflecting better moisture conditions and a more resilient hydrological regime. Importantly, the trends observed in both SPI and ESI are consistent with the drought classification trends from 2001 to 2024 discussed in Section 4.2. As shown previously, No Drought classes have declined, while moderate to severe drought classes have expanded, and this shift is reflected in the SPI and ESI behaviors at both analyzed sites. Although drought severity has increased provincewide, the rate of deterioration is faster in cropland zones, highlighting their higher vulnerability to both meteorological and surface-level stressors. These findings reinforce the importance of integrating both atmospheric (SPI) and surface (ESI) indicators into drought monitoring frameworks. The alignment between hydroclimatic trends and vegetation-based drought classification adds robustness to the interpretation and enhances early warning capabilities. Such integrated approaches are essential for effective drought preparedness and adaptation, especially in regions like Golestan with complex land use and climatic gradients. 

4239 

M. Jahanbakhsh, M. Akhoondzadeh 

Advances in Space Research 77 (2026) 4222–4246 

Table 7 

Pixel count of drought severity levels corresponding to different LULC types. 

|LULC Class|Extreme Drought|Severe Drought|Moderate Drought|Light Drought|No Drought 1|No Drought 2|
|---|---|---|---|---|---|---|
|Water|0|10|73|104|130|11|
|Teres|1|0|56|189|3649|670|
|Grass|0|1|4|43|199|3|
|Flooded Vegetation|0|0|2|5|10|0|
|Crops|0|928|3019|1993|1780|48|
|Shrub & Scrub|1|74|561|604|541|2|
|Built|0|50|211|214|193|4|
|Bare|4|3134|5179|1361|527|3|
|Snow & Ice|0|0|0|0|1|0|



### 4.7. Comparative analysis with previous studies 

The results of this study demonstrate strong alignment with an extensive body of global and regional literature, while simultaneously contributing novel perspectives on the interaction among climatic variability, land-use transformations, and agricultural drought evolution. The SPIand ESI-based drought evaluations presented here corroborate the global patterns reported by Dai (2013), who emphasized that warming-induced reductions in warmseason precipitation and increased evapotranspiration intensify drought occurrence and persistence. This consistency reinforces the broader understanding that climate change magnifies agricultural drought risks through simultaneous moisture deficits and atmospheric evaporative demand. Regionally, similar precipitation variability trends have been documented across Iran by Soltani et al. (2012) and Asakereh et al. (2023), affirming the heightened climatic instability observed in arid and semi-arid settings where rainfall fluctuations exert direct control over agricultural productivity. At a provincial scale, Roshan et al. (2024) investigated meteorological drought–groundwater interactions in Golestan Province using SPI and SPEI alongside multivariate regression and M5 tree-based models for SWI prediction. Their results identifying delayed groundwater responses to drought closely parallel our findings regarding precipitation decline, drought intensification, and rising agricultural water scarcity. Likewise, Ghorbani et al. (2024) linked SPI variability to treegrowth dynamics in the Hyrcanian forests, illustrating that amplified evapotranspiration driven by higher temperatures, increased wind speed, and greater sunshine duration combined with reduced precipitation has aggravated drought conditions, thereby supporting our results on SPI variability and agricultural drought stress. Advances in remote sensing and machine learning between 2023 and 2025 have substantially expanded drought prediction capability. Liu et al. (2024) introduced a machinelearning-constrained framework for hydrological drought risk projections across China, demonstrating the utility of hybrid modeling approaches in risk assessment. Complementary findings by Pande et al. (2024) confirmed the superior forecasting skills of ensemble ML algorithms for SPI- 

based drought prediction in semi-arid India. Furthermore, the Focal-TSMP deep-learning model developed by Shams Eddin and Gall (2023) strengthened agricultural drought classification by integrating regional climate simulations with vegetation indices. In Brazil, Gallear et al. (2025) demonstrated operational-scale agricultural drought forecasting using RF and GBM models with high nationalscale accuracy (R<sup>2</sup> ≈ 0.8), underscoring the effectiveness of ML-driven spatiotemporal drought early-warning systems. Notably, attention-based recurrent deep-learning architectures have recently excelled at capturing longrange dependency in climate–vegetation time series; however, their deployment remains constrained by substantial data and computational demands. In this regard, the drought assessment in India by Sharma et al. (2025) highlighted the operational appeal of tree-based ensembles, with XGBoost (84.80 % accuracy) and RF (82.98 %) offering high accuracy alongside enhanced interpretability and computational efficiency. Despite these methodological gains, critical challenges persist regarding model scalability, interpretability, and dynamic land-use integration. Deep-learning approaches remain largely limited to subregional domains and lack operational deployment pipelines in platforms like GEE. Addressing these gaps, the present study integrates VHI (VCI + TCI), SPI, ESI, and Dynamic World land-use products at 1-km spatial resolution while employing scalable RF and XGBoost algorithms validated through temporal hold-out testing (2021–2024). This configuration balances predictive rigor with operational feasibility, enabling regional drought forecasts through 2028. To our knowledge, this research represents the first comprehensive evaluation in Golestan Province that jointly examines agricultural drought dynamics in relation to land-use classes, precipitation variability, and moisture stress. Leveraging 2001–2024 drought time series, the model successfully predicts future drought trajectories, revealing strong associations between multivariate predictors and forecasted drought patterns. These outcomes complement studies such as Liu et al. (2025), which applied climate and land-use variables for long-term drought forecasts without a specific agricultural drought focus on this spatial and temporal scale. While Zhao and Dai (2017) emphasized uncertainty in global drought projections, the 

4240 

M. Jahanbakhsh, M. Akhoondzadeh 

Advances in Space Research 77 (2026) 4222–4246 



Fig. 13. Spatial distribution of annual precipitation in Golestan Province from 2001 to 2024. 

present localized and validated approach improves practical applicability for agricultural risk management and planning. Moreover, in contrast to studies in Iran that largely isolated climatic drivers (Soltani et al., 2012) or landuse change (Morid et al., 2006), this research bridges these dimensions to produce a holistic agricultural drought assessment for Golestan. Internationally, our methodology aligns with emerging integrated drought frameworks. For instance, the IADI approach by Senapati and Das (2025) utilized AHP-weighted vegetation and thermal indicators, while our data-driven fusion of VHI, SPI, and ESI extends 

predictive capability through 2028. Similarly, Senapati et al. (2025) linked farmer perceptions with satellite indices for agricultural drought impact assessment. Although field surveys were beyond the current scope, model accuracy (R<sup>2</sup> = 0.83; RMSE = 0.065) demonstrates robust performance. Vulnerability mapping frameworks by Senapati and Das (2024a, 2024b) also complement our spatial prioritization of land-use management strategies. Together, these studies and the present work advance integrative, satellite-enabled, forward-looking agricultural drought monitoring in semi-arid landscapes. Beyond comparative 

4241 

M. Jahanbakhsh, M. Akhoondzadeh 

Advances in Space Research 77 (2026) 4222–4246 



Fig. 14. Time series of the SPI from 2001 to 2024 for Golestan Province at a site located in a drought class with cropland land cover. Positive SPI values (blue bars) indicate above-normal precipitation and wet conditions, whereas negative SPI values red bars indicate below-normal precipitation and drought periods. 



Fig. 15. Time series of the SPI from 2001 to 2024 for Golestan Province at a site with forest land cover and no recorded drought conditions. Positive SPI values (blue bars) indicate above-normal precipitation and wet conditions, whereas negative SPI values red bars indicate below-normal precipitation and drought periods. 

analysis, the implications of this research are significant for both science and practice. Integrating multi-source remote sensing with ensemble ML delivers an effective platform for continuous drought monitoring and near-term prediction. Spatial delineation of drought-prone agricultural lands and bare surfaces underscores the necessity of adaptive irrigation management, strategic groundwater regulation, and ecological restoration. In contrast, the relative resilience of forested regions highlights the importance of conserving natural vegetation as a protective buffer against thermal and hydrological stress. Overall, this study advances drought science by linking regional satellite evidence with predictive analytics to develop an operational early- 

warning system. The findings provide not only scientific insight into agricultural drought mechanisms but also actionable guidance for policymakers, water managers, and agricultural planners seeking to enhance drought resilience and climate adaptation across Golestan Province and similar semi-arid environments. 

### 4.8. Implications and future considerations 

This study introduced an integrated and multivariate framework for monitoring and conceptually forecasting agricultural drought in Golestan Province, combining multi-source satellite observations with machine learning techniques. While the framework demonstrates significant potential for regional drought assessment, several directions for further improvement and refinement remain. Future research is encouraged to incorporate higher spatial resolution satellite imagery, such as Sentinel-2 or Landsat 9, to better capture the fine-scale spatial heterogeneity of drought impacts, particularly in fragmented agricultural and mixed-use landscapes. Although the current research primarily relied on remotely sensed data, the integration of in-situ observations such as soil moisture measurements, crop yield statistics, and meteorological station data would enhance calibration accuracy and provide stronger validation datasets. Such combined approaches would increase the reliability, operational applicability, and transferability of drought monitoring systems for decision-making purposes. It is also important to emphasize that the predictive component of this study was not intended to deliver deterministic forecasts. Instead, it aimed to explore a conceptual outlook of possible future drought conditions based on observed spatiotemporal trends and existing environmental dynamics. The RF and XGBoost models were applied as complementary analytical tools within the monitoring framework to evaluate their ability to reproduce shortterm variability and to demonstrate the potential of datadriven methods in early drought detection. Accordingly, the 2028 projection should be interpreted as a scenariobased hypothesis, not as an exact prediction. Reliable long-term forecasting would require more advanced temporal deep learning models such as Long Short-Term Memory (LSTM) and Gated Recurrent Unit (GRU) architectures that can explicitly learn sequential dependencies in multi-year datasets. However, these approaches require large training datasets and substantial computational resources, which remain a key limitation in many regional-scale applications. The present framework thus offers an innovative yet realistic foundation that links drought monitoring with preliminary predictive insight, supporting proactive drought management and adaptation planning. Beyond technical developments, the findings of this study carry clear implications for environmental management and policy. The multi-year spatiotemporal trend maps and drought classification results provide a scientific basis for prioritizing restoration programs, improving irrigation efficiency, and allocating water resources more effec- 

4242 

Advances in Space Research 77 (2026) 4222–4246 

M. Jahanbakhsh, M. Akhoondzadeh 



Fig. 16. Temporal profile of the ESI at a site located in a drought class with cropland land cover. Positive values (blue) indicate favorable moisture conditions, while negative values (red) denote periods of high evaporative stress and drought occurrence. 



Fig. 17. Temporal profile of the ESI at a site with forest land cover and no recorded drought conditions. Positive values (blue) indicate favorable moisture conditions, while negative values (red) denote periods of high evaporative stress and drought occurrence. 

tively. Identifying persistent drought-prone areas can help guide the distribution of agricultural subsidies, infrastructure investment, and land rehabilitation initiatives. Looking ahead, it is crucial to move beyond purely technical analyses and integrate scientific evidence into institutional coordination and governance frameworks. Effective drought mitigation requires translating geospatial intelligence into actionable policy, aligning the efforts of environmental agencies, agricultural ministries, and water authorities. Embedding satellite-based drought information and machine learning–driven analytics into decisionmaking systems will enable regional stakeholders to develop more proactive, sustainable, and equitable strategies for environmental protection and climate resilience. 

### 5. Conclusion 

This study developed an integrated framework combining multi-source RS data and machine learning models to monitor and forecast agricultural drought in Golestan Province, Iran, from 2001 to 2028. Long-term analyses of the VHI revealed a clear intensification of 

drought severity, particularly in cropland-dominated areas, although short-term fluctuations indicated partial recovery in certain years. The XGBoost model demonstrated strong predictive performance (R<sup>2</sup> = 0.85) and projected that by 2028, severe and extreme droughts could affect more than 60 % of the province. Results showed that croplands and bare soil are the most drought-sensitive land types, while forests exhibit higher ecological resilience. Declining precipitation (SPI) and increasing surface moisture stress (ESI) acted as parallel and reinforcing hydroclimatic drivers, jointly accelerating drought intensification across the region. The proposed framework provides a robust and transferable approach for regional drought monitoring, early warning, and adaptive agricultural planning. Future research should integrate higher-resolution satellite imagery, groundbased observations, and advanced temporal deep learning architectures to enhance predictive accuracy. Strengthening the linkage between geospatial analytics and policy implementation will be essential for developing climateresilient agricultural and water management strategies in semi-arid regions like Golestan Province. 

4243 

M. Jahanbakhsh, M. Akhoondzadeh 

Advances in Space Research 77 (2026) 4222–4246 

### Declaration of competing interest 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

### References 

- Anderson, M.C., Norman, J.M., Mecikalski, J.R., Otkin, J.A., Kustas, W. P., 2007a. A climatological study of evapotranspiration and moisture stress across the continental United States based on thermal remote sensing: 1. Model formulation. J. Geophys. Res. Atmos. 112. https:// doi.org/10.1029/2006JD007506. 

- Anderson, M.C., Norman, J.M., Mecikalski, J.R., Otkin, J.A., Kustas, W. P., 2007b. A climatological study of evapotranspiration and moisture stress across the continental United States based on thermal remote sensing: 2. Surface moisture climatology. J. Geophys. Res. Atmos. 112. https://doi.org/10.1029/2006JD007507. 

- Ardakanian, R., 2005. Overview of water management in Iran. In: Water Conservation, Reuse, and Recycling: Proceeding of an IranianAmerican workshop. The National Academies Press, Washington, DC, pp. 18–33. 

- Asakereh, H., Masoodian, S.A., Tarkarani, F., Zandkarimi, S., 2023. Decadal change of Iran’s precipitation regime. Pure Appl. Geophys. 180, 4275–4293. https://doi.org/10.1007/s00024-023-03376-x. 

- Ashouri, H., Lin Hsu, K., Sorooshian, S., Braithwaite, D., Knapp, K., Cecil, D., Nelson, B., Prat, O., 2015. Daily precipitation climate data record from multisatellite observations for hydrological and climate studies. Am. Meteorol. Soc. 69–84, In. https://doi.org/10.1175/BAMSD-13-00068.1. 

- Behrang Manesh, M., Khosravi, H., Heydari Alamdarloo, E., Saadi Alekasir, M., Gholami, A., Singh, V.P., 2019. Linkage of agricultural drought with meteorological drought in different climates of Iran. Theor. Appl. Climatol. 138, 1025–1033. https://doi.org/10.1007/ s00704-019-02878-w. 

- Breiman, L., 2001. Random forests. Mach. Learn. 45, 5–32. https://doi. org/10.1023/A:1010933404324. 

- Brown, C.F., Brumby, S.P., Guzder-Williams, B., Birch, T., Hyde, S.B., Mazzariello, J., Czerwinski, W., Pasquarella, V.J., Haertel, R., Ilyushchenko, S., 2022. Dynamic world, near real-time global 10 m land use land cover mapping. Sci. Data 9, 251. https://doi.org/10.1038/ s41597-022-01307-4. 

- Carra˜o, H., Russo, S., Sepulcre-Canto, G., Barbosa, P., 2016. An empirical standardized soil moisture index for agricultural drought assessment from remotely sensed data. Int. J. Appl. Earth Obs. Geoinf. 48, 74–84. https://doi.org/10.1016/j.jag.2015.06.011. 

- Charusombat, U., Niyogi, D., 2011. A hydroclimatological assessment of regional drought vulnerability: a case study of Indiana droughts. Earth Interact 15, 1–65. https://doi.org/10.1175/2011EI343.1. 

- Chen, T., Guestrin, C., 2016. Xgboost: a scalable tree boosting system. In: Proceedings of the 22nd acm sigkdd International Conference on Knowledge Discovery and Data Mining, pp. 785–794. https://doi.org/ 10.1145/2939672.293978. 

- Dai, A., 2013. Increasing drought under global warming in observations and models. Nat. Clim. Chang. 3, 52–58. https://doi.org/10.1038/ nclimate1633. 

- Damavandi, A.A., Rahimi, M., Yazdani, M.R., Noroozi, A.A., 2016. Spatial monitoring of agricultural drought through time series of NDVI and LST indices of MODIS data (Case study: Markazi Province). In: Scientific- Research Quarterly of Geographical Data (SEPEHR), pp. 115–126. https://doi.org/10.22131/sepehr.2016.23200. 

- Dutta, D., Kundu, A., Patel, N., Saha, S., Siddiqui, A., 2015. Assessment of agricultural drought in Rajasthan (India) using remote sensing derived Vegetation Condition Index (VCI) and Standardized Precipitation Index (SPI). Egypt. J. Remote Sens. Space Sci. 18, 53–63. https://doi.org/10.1016/j.ejrs.2015.03.006. 

- Gallear, J.W., Valadares Galdos, M., Zeri, M., Hartley, A., 2025. Evaluation of machine learning approaches for large-scale agricultural drought forecasts to improve monitoring and preparedness in Brazil. Nat. Hazards Earth Syst. Sci. 25, 1521–1541. https://doi.org/10.5194/ nhess-25-1521-2025. 

- Ghorbani, K., Mohammadi, J., Rezaei Ghaleh, L., 2024. Annual growth of Fagus orientalis is limited by spring drought conditions in Iran’s Golestan Province. J. For. Res. 35, 19. https://doi.org/10.1007/s11676023-01674-7. 

- Ghulam, A., Li, Z.-L., Qin, Q., Tong, Q., Wang, J., Kasimu, A., Zhu, L., 2007. A method for canopy water content estimation for highly vegetated surfaces-shortwave infrared perpendicular water stress index. Sci. China Ser. D: Earth Sci. 50, 1359–1368. https://doi.org/ 10.1007/s11430-007-0086-9. 

- Gidey, E., Dikinya, O., Sebego, R., Segosebe, E., Zenebe, A., 2018. Analysis of the long-term agricultural drought onset, cessation, duration, frequency, severity and spatial extent using Vegetation Health Index (VHI) in Raya and its environs, Northern Ethiopia. Environ. Syst. Res. 7, 1–18. https://doi.org/10.1186/s40068-018-0115-z. 

- Governorship, G.P. 2016. Golestan Province Governorship. Territorial Planning of Golestan Provine, Iran; Golestan Province. 

- Gu¨ner Bacanli, U<sup>¨</sup> ., 2017. Trend analysis of precipitation and drought in the A egean region, Turkey. Meteorol. Appl. 24, 239–249. https://doi. org/10.1002/met.1622. 

- Han, Y., Li, Z., Huang, C., Zhou, Y., Zong, S., Hao, T., Niu, H., Yao, H., 2020. Monitoring droughts in the Greater Changbai Mountains using multiple remote sensing-based drought indices. Remote Sens. (Basel) 12, 530. https://doi.org/10.3390/rs12030530. 

- Hao, Z., AghaKouchak, A., 2014. A nonparametric multivariate multiindex drought monitoring framework. J. Hydrometeorol. 15, 89–101. https://doi.org/10.1175/JHM-D-12-0160.1. 

- Heydari, H., Valadan Zoej, M., Maghsoudi, Y., Dehnavi, S., 2018. An investigation of drought prediction using various remote-sensing vegetation indices for different time spans. Int. J. Remote Sens. 39, 1871–1889. https://doi.org/10.1080/01431161.2017.1416696. 

- Hu, T., van Dijk, A.I., Renzullo, L.J., Xu, Z., He, J., Tian, S., Zhou, J., Li, H., 2020. On agricultural drought monitoring in Australia using Himawari-8 geostationary thermal infrared observations. Int. J. Appl. Earth Obs. Geoinf. 91. https://doi.org/10.1016/j.jag.2020.102153 102153. 

- Huang, S., Tang, L., Hupy, J.P., Wang, Y., Shao, G., 2021. A commentary review on the use of normalized difference vegetation index (NDVI) in the era of popular remote sensing. J. For. Res. 32, 1– 6. https://doi.org/10.1007/s11676-020-01155-1. 

- Hussain, A., Niaz, R., Al-Rezami, A., Mohamed Omer, A., Al-Duais, F. S., Almazah, M.M.A., 2025. Application of random forest for identification of an appropriate model for predicting meteorological drought. Adv. Meteorol. 2025. https://doi.org/10.1155/adme/7674140 7674140. 

- Jafari Shalamzari, M., Sheikh, V.B., Saadodin, A., Abedi Sarvestani, A., 2016. Public perception and acceptability toward domestic rainwater harvesting in Golestan, limits to up-scaling. Ecopersia 4, 1437–1454, 20.1001.1.23222700.2016.4.3.1.6. 

- Jahdi, R., Hanifepour, M., 2024. Analyzing the effects of meteorological drought on vegetation dynamics in the Golestan province. Geogr. Environ. Sustain. 14, 39–51. https://doi.org/10.22126/ GES.2024.10786.2762. 

- Kloos, S., Yuan, Y., Castelli, M., Menzel, A., 2021. Agricultural drought detection with MODIS based vegetation health indices in southeast Germany. Remote Sens. (Basel) 13, 3907. https://doi.org/10.3390/ rs13193907. 

- Kogan, F.N., 1990. Remote sensing of weather impacts on vegetation in non-homogeneous areas. Int. J. Remote Sens. 11, 1405–1419. https:// doi.org/10.1080/01431169008955102. 

- Kogan, F.N., 1997. Global drought watch from space. Bull. Am. Meteorol. Soc. 78, 621–636. https://doi.org/10.1175/1520-0477(1997) 078%3C0621:GDWFS%3E2.0.CO;2. 

4244 

Advances in Space Research 77 (2026) 4222–4246 

##### M. Jahanbakhsh, M. Akhoondzadeh 

- Kogan, F., 2002. World droughts in the new millennium from AVHRRbased vegetation health indices. Eos Trans. AGU 83, 557–563. https:// doi.org/10.1029/2002EO000382. 

- Kundu, A., Denis, D., Patel, N., Dutta, D., 2016. Spatial pattern of agricultural drought using noaa-avhrr derived vegetation indices. Remote Sens. Nat. Resour. Manag. Monit. 276. 

- Liu, J., Li, M., Li, R., Shalamzari, M.J., Ren, Y., Silakhori, E., 2025. Comprehensive assessment of drought susceptibility using predictive modeling, climate change projections, and land use dynamics for sustainable management. Land 14, 337. https://doi.org/ 10.3390/land14020337. 

- Liu, R., Yin, J., Slater, L., Kang, S., Yang, Y., Liu, P., Guo, J., Gu, X., Zhang, X., Volchak, A., 2024. Machine-learning-constrained projection of bivariate hydrological drought magnitudes and socioeconomic risks over China. Hydrol. Earth Syst. Sci. 28, 3305–3326. https://doi. org/10.5194/hess-28-3305-2024. 

- Lu, J., Carbone, G.J., Gao, P., 2019. Mapping the agricultural drought based on the long-term AVHRR NDVI and North American Regional Reanalysis (NARR) in the United States, 1981–2013. Appl. Geogr. 104, 10–20. https://doi.org/10.1016/j.apgeog.2019.01.005. 

- Madani, K., 2014. Water management in Iran: what is causing the looming crisis? J. Environ. Stud. Sci. 4, 315–328. https://doi.org/ 10.1007/s13412-014-0182-z. 

- Mannocchi, F., Todisco, F., Vergni, L., 2004. Agricultural drought: indices, definition and analysis. IAHS Publ. 286, 246–254. 

- McKee, T.B., Doesken, N.J., Kleist, J. 1993. The relationship of drought frequency and duration to time scales. In: Proceedings of the 8th Conference on Applied Climatology (pp. 179–183): California. 

- McVicar, T., Bierwirth, P., 2001. Rapidly assessing the 1997 drought in Papua New Guinea using composite AVHRR imagery. Int. J. Remote Sens. 22, 2109–2128. https://doi.org/10.1080/01431160120728. 

- Morid, S., Smakhtin, V., Moghaddasi, M., 2006. Comparison of seven meteorological indices for drought monitoring in Iran. Int. J. Climatol. 26, 971–985. https://doi.org/10.1002/joc.1264. 

- Ogunrinde, A.T., Olasehinde, D.A., Olotu, Y., 2020. Assessing the sensitivity of standardized precipitation evapotranspiration index to three potential evapotranspiration models in Nigeria. Sci. Afr. 8. https://doi.org/10.1016/j.sciaf.2020.e00431 e00431. 

- Okal, H.A., Ngetich, F.K., Okeyo, J.M., 2020. Spatio-temporal characterisation of droughts using selected indices in Upper Tana River watershed, Kenya. Sci. Afr. 7. https://doi.org/10.1016/j.sciaf.2020. e00275 e00275. 

- Palmer, W.C., 1965. Meteorological drought. US. Weather Bureau Res. Paper, 45, 1–58. 

- Pande, C.B., Sidek, L.M., Varade, A.M., Elkhrachy, I., Radwan, N., Tolche, A.D., Elbeltagi, A., 2024. Forecasting of meteorological drought using ensemble and machine learning models. Environ. Sci. Eur. 36, 160. https://doi.org/10.1186/s12302-024-00975-w. 

- Peters, A.J., Walter-Shea, E.A., Ji, L., Vina, A., Hayes, M., Svoboda, M. D., 2002. Drought monitoring with NDVI-based standardized vegetation index. Photogramm. Eng. Remote Sens. 68, 71–75. 

- Piraei, R., Niazkar, M., Gangi, F., Eryılmaz Tu¨rkkan, G., Afzali, S.H., 2024. Short-term drought forecast across two different climates using machine learning models. Hydrology 11, 163. https://doi.org/10.3390/ hydrology11100163. 

- Pirnia, A., Golshan, M., Bigonah, S., Solaimani, K., 2018. Investigating the drought characteristics of Tamar basin (upstream of Golestan Dam) using SPI and SPEI indices under current and future climate conditions. J. Ecohydrol. 5, 215–228. https://doi.org/10.22059/ ije.2018.239226.689. 

- Ray, S., Sesha Sai, M., Chattopadhyay, N., 2014. Agricultural drought assessment: operational approaches in India with special emphasis on 2012. In: High-Impact Weather Events Over the SAARC Region. Springer, pp. 349–364. 

- Roshan, A., Ghorbani, K., Salarijazi, M., Oskouei, E.A., 2024. Evaluation of meteorological drought effects on underground water level fluctuations using data mining methods (case study: semi-deep wells of 

   - Golestan province). Environ. Monit. Assess. 196, 236. https://doi.org/ 10.1007/s10661-024-12415-6. 

- Senapati, U., Das, T.K., 2024a. Delineation of potential alternative agriculture region using RS and AHP-based GIS techniques in the drought prone upper Dwarakeswer river basin, West Bengal, India. Ecol. Model. 490. https://doi.org/10.1016/j.ecolmodel.2024.110650 110650. 

- Senapati, U., Das, T.K., 2024b. Geospatial assessment of agricultural drought vulnerability using integrated three-dimensional model in the upper Dwarakeshwar river basin in West Bengal, India. Environ. Sci. Pollut. Res. 31, 54061–54088. https://doi.org/10.1007/s11356-02223663-9. 

- Senapati, U., Das, U., Das, T.K., 2025. Spatio-temporal Scenario and farmers’ perceptions of agricultural drought in the context of climate change in a drought–prone river basin of India. J. Indian Soc. Remote Sens. 1–19. https://doi.org/10.1007/s12524-025-02134-x. 

- Senapati, U., Das, T.K., 2025. Enhancing agricultural drought monitoring with the Integrated Agricultural Drought Index (IADI): a multi-source remote sensing approach. Adv. Space Res. https://doi.org/10.1016/j. asr.2025.04.021. 

- Serban, C., Maftei, C., 2025. Remote sensing evaluation of drought effects on crop yields across dobrogea, romania, using Vegetation Health Index (VHI). Agriculture 15, 668. https://doi.org/10.3390/ agriculture15070668. 

- Shams Eddin, M.H., Gall, J., 2023. Focal-TSMP: deep learning for vegetation health prediction and agricultural drought assessment from a regional climate simulation. Egusphere 2023, 1–50. https://doi.org/ 10.5194/egusphere-2023-2422. 

- Shamsipour, A.A., AlaviPanah, S.K., Mohammadi, H., Azizi, A., Khoshakhlagh, F., 2008. An analysis of drought events for central plains of Iran through an employment of NOAA-AVHRR data. Desert 13, 105–115. 

- Sharma, S.S., Mukherjee, J., Dell’Acqua, F., 2025. Leveraging sentinel-2 data and machine learning for drought detection in India: the process of ground truth construction and a case study. Remote Sens. (Basel) 17, 3159. 

- Shukla, S., Wood, A.W., 2008a. Use of a standardized runoff index for characterizing hydrologic drought. Geophys. Res. Lett. 35. https://doi. org/10.3390/rs17183159. 

- Shukla, S., Wood, A.W., 2008b. Use of a standardized runoff index for characterizing hydrologic drought. Geophys. Res. Lett. 35. https://doi. org/10.1029/2007GL032487. 

- Soltani, S., Saboohi, R., Yaghmaei, L., 2012. Rainfall and rainy days trend in Iran. Clim. Change 110, 187–213. https://doi.org/10.1007/ s10584-011-0146-1. 

- Tavazohi, E., Nadoushan, M.A., 2018. Assessment of drought in the Zayandehroud basin during 2000-2015 using NDDI and SPI indices. Fresenius Environ. Bull. 27, 2332–2340. 

- Usman, M., Nichol, J., 2020. A spatio-temporal analysis of rainfall and drought monitoring in the Tharparkar Region of Pakistan. Remote Sens 12, 580. https://doi.org/10.3390/rs12030580. 

- Usman, M., Nichol, J.E., Ibrahim, A.T., Buba, L.F., 2018. A spatiotemporal analysis of trends in rainfall from long term satellite rainfall products in the Sudano Sahelian zone of Nigeria. Agric. For. Meteorol. 260, 273–286. https://doi.org/10.1016/j. agrformet.2018.06.016. 

- Usman, M., Nichol, J.E., Abdallah, A.M., Bilal, M., 2025. Characterising the Urban Heat Island in a low-rise indigenous city using remote sensing. Urban Clim. 61. https://doi.org/10.1016/j.uclim.2025.102433 102433. 

- Vaani, N., Porchelvan, P., 2018. Monitoring of agricultural drought using fortnightly variation of vegetation condition index (VCI) for the state of Tamil Nadu, India. Int. Arch. Photogramm. Remote. Sens. Spat. Inf. Sci. 42, 159–164. https://doi.org/10.5194/isprs-archives-XLII-4W9-159-2018. 

- Vicente-Serrano, S.M., Beguerı´a, S., Lo´pez-Moreno, J.I., 2010. A multiscalar drought index sensitive to global warming: the standardized 

4245 

M. Jahanbakhsh, M. Akhoondzadeh 

Advances in Space Research 77 (2026) 4222–4246 

   - precipitation evapotranspiration index. J. Clim. 23, 1696–1718. https:// doi.org/10.1175/2009JCLI2909.1. 

- Viet, L.V., Thuy, T.T.T., 2024. Drought sensitivity analysis of meteorological and vegetation indices in Dak Nong, Vietnam. J. Water Clim. Chang. 15, 4968–4988. https://doi.org/10.2166/wcc.2024.661. 

- Yoon, D.-H., Nam, W.-H., Lee, H.-J., Hong, E.-M., Feng, S., Wardlow, B.D., Tadesse, T., Svoboda, M.D., Hayes, M.J., Kim, D.-E., 2020. Agricultural drought assessment in East Asia using satellite-based indices. Remote Sens. (Basel) 12, 444. https://doi.org/10.3390/ rs12030444. 

- Zagade, N., Kadam, A., Umrikar, B., Maggirwar, B., 2018. Remote sensing-based assessment of agricultural droughts in sub-watersheds of upper Bhima basin India. J Remote Sens Land 2, 105–111. https://doi. org/10.21523/gcj1.18020204. 

- Zarei, R., Sarajian, M., Bazgeer, S., 2013. Monitoring meteorological drought in Iran using remote sensing and drought indices. Desert 18, 89–97. 

- Zehtabian, G., Khosravi, H., Ghodsi, M., 2009. In: High demand in a land of water scarcity: Iran. Water and Sustainability in Arid Regions: Bridging the Gap between Physical and Social Sciences. Springer, pp. 75–86. https://doi.org/10.1007/978-90-481-2776-4_5. 

- Zeng, F., Gao, Q., Wu, L., Rao, Z., Wang, Z., Zhang, X., Yao, F., Sun, J., 2025. Modeling short-term drought for SPEI in mainland China using the XGBoost model. Atmos. 16, 419. https://doi.org/10.3390/ atmos16040419. 

- Zhao, C., Brissette, F., Chen, J., Martel, J.-L., 2020. Frequency change of future extreme summer meteorological and hydrological droughts over North America. J. Hydrol. 584. https://doi.org/10.1016/j.jhydrol.2019.124316 124316. 

- Zhao, T., Dai, A., 2017. Uncertainties in historical changes and future projections of drought. Part II: model-simulated historical and future drought changes. Clim. Change 144, 535–548. https://doi.org/10.1007/ s10584-016-1742-x. 

4246 

