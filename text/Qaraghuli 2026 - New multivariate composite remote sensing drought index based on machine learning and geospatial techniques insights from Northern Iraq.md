Journal of Hydrology: Regional Studies 64 (2026) 103211 



Contents lists available at ScienceDirect 

# Journal of Hydrology: Regional Studies 

journal homepage: www.elsevier.com/locate/ejrh 



New multivariate composite remote sensing drought index based on machine learning and geospatial techniques, insights from Northern Iraq 



Khalid Qaraghuli<sup>a,b</sup> , Mohamad Fared Murshed<sup>a,*</sup> , Md Azlin Md Said<sup>a</sup> , Ali Salem<sup>d,e,**</sup> , Ali Mokhtar<sup>c,*</sup> 

a _School of Civil Engineering, Universiti Sains Malaysia, 14300, Nibong Tebal, Pulau Pinang, Malaysia_ b _Al-Mussaib Technical Institute, Al-Furat Al-Awsat Technical University, 51006, Babil, Iraq_ c _Department of Agricultural Engineering, Faculty of Agriculture, Cairo University, Giza 12613, Egypt_ d _Civil Engineering Department, Faculty of Engineering, Minia University, Minia 61111, Egypt_ 

e _Structural Diagnostics and Analysis Research Group, Faculty of Engineering and Information Technology, University of P_ ´ _ecs, Boszorkany ut 2, H-_ ´ _7624 Pecs, Hungary_ 

### A R T I C L E I N F O 

A B S T R A C T 

_Keywords:_ Climate change Drought Remote sensing Random forest Machine learning 

_Study region:_ Northern Iraq, is widely known as the breadbasket of Iraq, famous for its cereal production. It is an arid to semi-arid region that frequently experiences significant droughts, impacting agriculture, water resources, and ecosystems. _Study focus:_ This study develops and evaluates five machine learning models (Random Forest (RF), Extreme Gradient Boosting (XGB), Support Vector Regression (SVR), Gradient Boosting Machine (GBM), and Artificial Neural Networks (ANN)) for predicting the Standardized Precipitation Evapotranspiration Index (SPEI) at 3-month (SPEI-03) and 6-month (SPEI-06) timescales across Iraq. The models were trained and tested with satellite-based and bias-corrected gridded data covering 2001–2023. Seventeen variables from meteorological, vegetation, soil, and topographic sources were used across four predictor scenarios. 

_New hydrological insights for the region:_ Results demonstrate that RF and XGB models consistently outperformed other models in estimating short-term (SPEI03) and medium-term (SPEI06) drought conditions, with R² up to 0.90 and NSE of 0.89. SHAP analysis revealed that precipitation is the dominant driver of short-term droughts, while temperature, vegetation indices, and soil moisture have greater influence on medium-term droughts. The proposed modeling framework improves the understanding of regional drought dynamics and offers a robust, data-driven tool to strengthen early warning systems and support drought risk management for local stakeholders. 

## **1. Introduction** 

Climate change intensifies extreme drought events by accelerating evapotranspiration, altering precipitation patterns, and 

* Corresponding authors. 

** Corresponding author at: Civil Engineering Department, Faculty of Engineering, Minia University, Minia 61111, Egypt. 

_E-mail addresses:_ khalid.qaraghuli@student.usm.my (K. Qaraghuli), cefaredmurshed@usm.my (M.F. Murshed), ceazlin@usm.my (M.A.M. Said), salem.ali@mik.pte.hu (A. Salem), ali.mokhtar@agr.cu.edu.eg (A. Mokhtar). 

https://doi.org/10.1016/j.ejrh.2026.103211 

Received 4 July 2025; Received in revised form 29 January 2026; Accepted 30 January 2026 

Available online 10 February 2026 

2214-5818/© 2026 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/ ). 

_Journal of Hydrology: Regional Studies 64 (2026) 103211_ 

_K. Qaraghuli et al._ 

increasing drought persistence, with recent assessments showing a 29 % rise since 2000 and projections warning of further intensification under high emissions scenarios (Rahman et al., 2025). These impacts are especially severe in arid and semi-arid regions like Iraq, where escalating water scarcity threatens national stability and food security. International organizations such as the FAO and UN WFP rank Iraq among the world’s most climate-vulnerable countries due to its exposure to heat waves, sandstorms, and prolonged droughts (Hashim et al., 2025; UN, 2023). This situation highlights the urgent need for localized, data-driven drought prediction tools tailored to Iraq’s unique climatic and geographic conditions. 

Drought monitoring often relies on station-based observations, but missing data and sparse networks hinder trend analysis and early warning systems, especially in vulnerable regions (Qaraghuli et al., 2024; Sa’adi et al., 2023). Remote sensing and gridded climate datasets help address these gaps by providing consistent, spatially continuous records of key indicators such as precipitation, temperature, and soil moisture (Casas et al., 2024; Newman et al., 2024). While common single-variable indices like SPI and VCI are useful, they do not fully capture drought’s complexity; multivariate indices integrating multiple variables provide a more comprehensive assessment but require careful selection and robust methodologies (Faiz et al., 2025; Xu et al., 2021). In parallel, drought forecasting can employ physical or conceptual hydrological models, which offer valuable process insights but are often data-intensive and complex for real-time use, whereas data-driven approaches require fewer inputs and have shown strong predictive capability across various drought contexts (Mokhtar et al., 2021). 

Recent advances in computer technology have positioned machine learning (ML) as a powerful approach for drought monitoring and prediction, integrating data from station observations, remote sensing, and gridded records to identify complex, non-linear relationships among multiple climatic variables (Mohammadi et al., 2025; Qaraghuli et al., 2024). While the predictive power of ML models is well established, their “black box” nature poses challenges for scientific research and operational drought monitoring, where understanding the drivers of drought is as important as prediction accuracy (Mardian et al., 2023). Feature importance analysis helps address this by quantifying each predictor’s contribution to the model output, revealing key environmental and climatic factors. Traditional global methods, such as Mean Decrease in Impurity, offer general rankings but do not explain individual predictions (Xue et al., 2024) **.** In contrast, SHapley Additive exPlanations (SHAP), based on cooperative game theory, provides consistent, mathematically grounded insights both globally and locally, making it a robust tool for interpreting ML-based drought models and an integral part of this study’s methodology (Xue et al., 2024; Yang et al., 2023). 

The transition from traditional univariate drought indices to multivariate and data-driven frameworks represents a significant advancement in drought monitoring (Prodhan et al., 2022). This integrated approach enhances the reliability of early warning systems, fostering more effective climate adaptation and mitigation strategies, particularly in vulnerable regions such as Nineveh and the broader Iraqi landscape. A wide range of machine learning models has been applied to drought prediction in recent years, each offering unique strengths depending on data structure and forecasting objectives. Support Vector Regression (SVR) has shown strong performance in short-term drought forecasting, with studies demonstrating its capacity to predict drought indices like the SPEI and SPI across multiple regions. Similarly, Artificial Neural Networks (ANN) have been widely applied due to their adaptability and robustness in modeling temporal and spatial drought dynamics, especially when lagged climatic variables are incorporated (Thai-Nghe, 2024; Poudel et al., 2024). Random Forest (RF) has also gained prominence for its high prediction accuracy and ability to handle large datasets with diverse predictors, ranging from meteorological to socio-economic factors (Mokhtar et al., 2021; Xu et al., 2024). Gradient Boosting Machines (GBM), with their ensemble learning structure, have proven effective in quantifying drought variability and identifying dominant influencing factors across large regions (Zhang et al., 2022). Extreme Gradient Boosting (XGB) has demonstrated good performance, particularly in integrating multi-source remote sensing and climatic data for both agricultural and hydrological drought forecasting (Li et al., 2024). 

While the SPEI is traditionally calculated using historical precipitation and temperature data, this diagnostic approach is limited to assessing current or past drought conditions. The primary motivation for this study is to move from diagnosis to prognosis by developing a predictive framework. The necessity for predicting SPEI via machine learning arises from several key challenges. Firstly, there is a critical need for drought forecasting to enable proactive planning and early warning systems. A well-trained predictive model can estimate future SPEI values, providing lead time for stakeholders to implement mitigation strategies. Secondly, many regions, including parts of Iraq, suffer from data scarcity, with sparse or incomplete ground-based meteorological station networks. This study investigates the extent to which readily available, spatially continuous remote sensing data (e.g., land surface temperature, soil moisture) can substitute for or augment traditional inputs to accurately predict drought conditions. Finally, by systematically evaluating models with different combinations of input variables, this research aims to identify the primary drivers of drought in the region, offering deeper insights into the physical processes governing drought evolution. 

The ultimate goal is to develop a reliable predictive tool that can support regional water resource management and agricultural planning by providing timely drought forecasts. Therefore, the specific objectives of this study are: (1) To develop and compare the performance of five state-of-the-art machine learning models for predicting SPEI at 3-month and 6-month timescales in Iraq. (2) To evaluate the predictive power of different variable groups—including meteorological, land surface, and topographic data through a series of structured scenarios. (3) To identify the optimal model and input combination that provides the highest accuracy for drought prediction, thereby establishing a foundation for an operational drought monitoring and forecasting system in the region. This research contributes to the expanding body of literature on drought modeling by developing and validating advanced machine learning approaches to estimate the SPEI across multiple timescales in the Nineveh governorate, Iraq. 

2 

_Journal of Hydrology: Regional Studies 64 (2026) 103211_ 

_K. Qaraghuli et al.                                                                                                                                                                                                     Journal of Hydrology: Regional Studies_ 

## **2. Materials and methods** 

## _2.1. Study area_ 

Iraq, located in the West Asia and North Africa (WANA) region, experiences an arid to semi-arid climate, as classified by the Koppen ¨ climate system. The country has four distinct climatic seasons: summer, autumn, winter, and spring. Approximately 90 % of annual rainfall occurs in winter and spring (Al-Ozeer et al., 2020; Salman et al., 2019). This study focuses on the Nineveh governorate, "breadbasket of Iraq", owing to its extensive rainfed cereal cultivation, particularly wheat and barley, situated in northwestern Iraq, covering an area of 32,308 km² between longitudes 41<sup>◦</sup> 25' to 44<sup>◦</sup> 15' E and latitudes 34<sup>◦</sup> 15' to 37<sup>◦</sup> 30' N. Fig. 1 illustrates the geographical boundaries and topography of the study area. 

Nineveh has a semi-arid climate with marked seasonal variation shaped by diverse terrain and regional circulation. The Koppen- ¨ Geiger classification places the governorate at the transition between Mediterranean (Csa) and Subtropical Steppe (Bsh) zones. The Csa zone features cold, wet winters and hot, dry summers, while the Bsh zone has moderately cold winters and extremely hot, arid summers (Al-Bazaz and Agha, 2023). Average January temperatures are around 7<sup>◦</sup> C, while peak summer temperatures reach up to 43<sup>◦</sup> C in July and August with low humidity. Annual rainfall averages 365 mm, mostly falling from November to April (Yahya and Seker, 2019). 

## _2.2. Datasets and methods_ 

Fig. 2 illustrates the workflow of this research, which is described in detail in the following sections. 

## _2.3. Datasets_ 

## _2.3.1. Station Data_ 

To support this research, monthly meteorological observations from seven stations across the Nineveh governorate, Iraq, covering the period from 1992 to 2013, have been used. The entire dataset was partitioned into two independent periods: a **training period from January 1992 to December 2006** and a **testing period from January 2006 to December 2013** . A detailed summary of the datasets is provided in Table 1. All datasets were resampled to a common spatial resolution of [e.g., 0.25<sup>◦</sup> ] using bilinear interpolation for spatial consistency and aggregated to a monthly temporal scale. The dataset comprises key climatic variables, including precipitation (Pre), maximum temperature (Tmax), minimum temperature (Tmin), mean temperature (Tmean), relative humidity (RH), wind speed (WS), and sunshine duration (Sun). These records were sourced from the Iraqi Meteorological Organization and Seismology (IMOS), the primary authority for climate and weather monitoring in Iraq. The geographical locations of the selected meteorological stations are shown in Fig. 1, with detailed descriptions, including their coordinates and altitudes, provided in Table 2. 



**Fig. 1.** Study area and the location of meteorological stations. 

3 

_Journal of Hydrology: Regional Studies 64 (2026) 103211_ 

_K. Qaraghuli et al.                                                                                                                                                                                                     Journal of Hydrology: Regional Studies_ 



**Fig. 2.** Workflow of the machine learning approach for drought estimation. 

## _2.3.2. Gridded Datasets_ 

TerraClimate is a high-resolution dataset providing monthly climate and water balance data for global terrestrial surfaces from 1958 to the present. With a spatial resolution of approximately 4 km (1/24th degree) and monthly temporal coverage, it supports ecological and hydrological studies requiring fine-scale, time-varying climate information (Al-Yaari et al., 2024). The dataset includes key variables such as precipitation accumulation and reference evapotranspiration, calculated using the Penman-Monteith method (Abubakar, 2024; Solaimani and Ahmadi, 2024). These features make TerraClimate a valuable resource for drought monitoring, water resource management, and climate change assessments (de Andrade et al., 2022). 

Monthly TerraClimate data in NetCDF format were obtained from its official repository. Values corresponding to the study area's meteorological stations were extracted and processed using ArcGIS 10.8 to ensure consistency with the research framework and objectives. Additionally, data for the entire study area were retrieved using Google Earth Engine (GEE), providing values for each point across the region. 

## _2.3.3. Remote Sensing Data_ 

Multiple remote sensing products from the Moderate Resolution Imaging Spectroradiometer (MODIS) and the United States Geological Survey (USGS) were utilized to obtain essential datasets for drought analysis and estimation. Specifically, the MODIS vegetation indices product (MOD13A3) and the land surface temperature (LST) product (MOD11A2), both with a spatial resolution of 

4 

_Journal of Hydrology: Regional Studies 64 (2026) 103211_ 

_K. Qaraghuli et al.                                                                                                                                                                                                     Journal of Hydrology: Regional Studies_ 

**Table 1** 

Summary of Datasets Used in This Study. 

|Category|Variable Name|Source Dataset|Purpose in Study|Temporal<br>Resolution|Spatial<br>Resolution|Data Source/<br>Link|
|---|---|---|---|---|---|---|
|**Meteorological**|Precipitation (P)|CHIRPS|SPEI Calculation&<br>Predictor|Monthly|0.05<sup>◦</sup>|IMOS|
||Max Temperature<br>(Tmax)|TerraClimate|PET Calculation&<br>Predictor|Monthly|1/24<sup>◦</sup>(~4 km)|IMOS|
||Min Temperature<br>(Tmin)|TerraClimate|PET Calculation&<br>Predictor|Monthly|1/24<sup>◦</sup>(~4 km)|IMOS|
||Wind Speed (Ws)|TerraClimate|Predictor|Monthly|1/24<sup>◦</sup>(~4 km)|IMOS|
|**Land Surface**|Land Surface Temp.<br>(LST)|MODIS<br>(MOD11C3)|Predictor|Monthly|0.05<sup>◦</sup>||
||Soil Moisture (SM)|GLDAS-Noah|Predictor|Monthly|0.25<sup>◦</sup>||
||NDVI|MODIS<br>(MOD13C2)|Predictor|Monthly|0.05<sup>◦</sup>||
|**Topographic**|Elevation (ELEV)|USGS DEM<br>(SRTM)|Static Predictor|Static|30 m (~1 km)||
||Slope (SLP)|Derived from DEM|Static Predictor|Static|30 m (~1 km)||
||Aspect (ASP)|Derived from DEM|Static Predictor|Static|30 m (~1 km)||



**Table 2** 

Description of meteorological stations. 

|**Station**|**WMO Code**|**Name**|**Latitude**|**Longitude**|**Altitude (m)**|
|---|---|---|---|---|---|
|Station1|40910|Al-Baaj|36<sup>◦</sup>02'|41<sup>◦</sup>48'|321|
|Station2|40619|Makhmour|35<sup>◦</sup>46'|43<sup>◦</sup>35'|270|
|Station3|40608|Mosul|36<sup>◦</sup>19'|43<sup>◦</sup>09'|223|
|Station4|40602|Rabiah|36<sup>◦</sup>48'|42<sup>◦</sup>06'|382|
|Station5|40604|Sinjar|36<sup>◦</sup>19'|41<sup>◦</sup>50'|465|
|Station6|40609|Tel-Abta|35<sup>◦</sup>55'|42<sup>◦</sup>24'|200|
|Station7|40603|Tel-Afar|36<sup>◦</sup>22'|42<sup>◦</sup>06'|273|



Note: WMO is the World Meteorological Organization 

1000 m, were employed to support the analysis and ensure alignment with the study objectives. Additionally, USGS offered highresolution topographic information, further enhancing the spatial analysis by providing critical elevation and terrain data essential for understanding drought dynamics. Table 3 below summarizes the remote sensing datasets used, including their key variables and resolutions. 

## _2.4. Methods_ 

## _2.4.1. Standardized Precipitation Evapotranspiration Index (SPEI)_ 

The SPEI is a widely recognized index for drought monitoring, particularly under climate change conditions, as it integrates both precipitation and temperature to provide a comprehensive assessment of drought severity and duration (Choudhury, 2024; Liu et al., 2024). It is calculated by determining the monthly water balance ( _Di_ ), defined as the difference between precipitation ( _Pi_ ) and potential evapotranspiration (PET) for each month ( _i_ ) (Oz et al., 2024<sup>¨</sup> ): 



In this study, SPEI values were computed for two timescales: three months (SPEI03) to capture short-term drought variability and six months (SPEI06) to reflect medium-term drought conditions. All indices were derived from bias-corrected TerraClimate data to ensure consistency with local climatological patterns. 

The calculation of SPEI involved the following steps: 

**Table 3** 

Summary of remote sensing datasets utilized in this study. 

|**Data / Sensor**|**Product**|**Variable**|**Spatial**|**Temporal**|**Coverage**|
|---|---|---|---|---|---|
||||**resolution**|**resolution**|**period**|
|MODIS|MOD11A2.061|LST|1000 m|8 days|2000-present|
|MODIS|MOD13A3.061|NDVI|1000 m|Monthly|2000-present|
|MODIS|MOD13A3.061|EVI|1000 m|Monthly|2000-present|
|USGS|SRTM 1 Arc-second|DEM|30 m|Static|2023|



5 

_K. Qaraghuli et al.                                                                                                                                                                                                     Journal of Hydrology: Regional Studies 64 (2026) 103211_ 

1. **Calculating PET:** Monthly PET was calculated using the Hargreaves equation, which requires only minimum and maximum temperature and is suitable for data-scarce regions [cite: Hargreaves and Samani, 1985]. _PET_ = _0.0023_ × _R_ ₐ × _(T_ ₘₑₐₙ + _17.8)_ × _(T_ ₘₐₓ _- T_ ₘᵢₙ _)_ ⁰⋅⁵ 

2. **Calculating Climatic Water Balance (D):** The monthly difference between precipitation (P) and PET was calculated: _D_ ᵢ = _P_ ᵢ _- PET_ ᵢ. 

3. **Aggregating Water Balance:** The D series was aggregated at 3-month and 6-month timescales. 

4. **Fitting to a Distribution:** The aggregated D series was fitted to a three-parameter log-logistic probability distribution to compute the cumulative probability of the water balance for each timescale. 

5. **Standardization:** The cumulative probability was transformed into a standard normal variable with a mean of zero and a standard deviation of one, resulting in the final unitless SPEI value." 

SPEI can be calculated over multiple accumulation periods, each representing different types and temporal dynamics of drought. In this study, SPEI-3 and SPEI-6 were selected because they effectively capture short- to medium-term moisture variability that is most relevant to agricultural drought monitoring and vegetation response. The 3-month scale (SPEI-3) reflects short-term soil moisture anomalies and meteorological water deficits that directly influence crop growth during sensitive phenological stages. The 6-month scale (SPEI-6) represents seasonal cumulative water balance conditions, integrating precipitation and evaporative demand over a longer period and thus capturing prolonged moisture stress that affects crop productivity and ecosystem functioning. Since the objective of this research is to develop a remote sensing–based multivariate drought index sensitive to agricultural impacts rather than long-term hydrological drought, these two time scales provide an optimal balance between responsiveness and stability, aligning with crop growth cycles and the temporal sensitivity of vegetation-based remote sensing indicators. 

Drought is a complex phenomenon influenced by multiple interacting climatic, vegetation, and topographic factors (Liu et al., 2020). To improve the accuracy and reliability of drought estimation, this study incorporated 17 predictor variables derived from three primary datasets: MODIS, USGS DEM, and bias-corrected TerraClimate. These variables capture key aspects of soil moisture, vegetation health, temperature conditions, precipitation, and terrain characteristics. The Standardized Precipitation Evapotranspiration Index (SPEI) at three-month and six-month timescales served as the response variables. 

All variables were preprocessed to ensure consistent spatial and temporal resolution (1000 m and monthly), using Google Earth Engine (GEE) and ArcGIS 10.8 for resampling, aggregation, and index derivation. Table 4 summarizes the full list of predictors, their descriptions, relevant derivation equations for indices, and their allocation across the four input scenarios (Sc01–Sc04) developed for model comparison. 

**Table 4** 

Description of the predictor variables. 

|**No.**|**Abbr.**|**Full name**|**Source**|**Description**|**Eq**|**uation**||**Sc01**|**Sc02**|**Sc03**|**Sc04**|
|---|---|---|---|---|---|---|---|---|---|---|---|
|1|SM|Soil Moisture|TerraClimate|Water retained in the soil|—|||✓||✓||
|2|SMCI|Soil Moisture Condition<br>Index|Derived from<br>TerraClimate|Soil moisture anomaly|=|_SM_−<br>_SM_max−|_SM_min<br>_SM_min|✓||✓|✓|
|3|LST|Land Surface Temperature|MODIS|Surface temperature,<br>heat stress indicator|—|||✓||✓||
|4|TCI|Temperature Condition<br>Index|Derived from<br>MODIS|Temperature anomaly<br>index|=|_LST_max <br>_LST_max −|−_LST_<br>_LST_min|✓||✓|✓|
|5|NDVI|Normalized Difference<br>Vegetation Index|MODIS|Vegetation greenness|—|||✓||✓||
|6|VCI|Vegetation Condition Index|Derived from<br>MODIS|Vegetation condition<br>anomaly|=|_NDVI_−_N_|_DVI_min|✓||✓||
|||||||_NDVI_max −|_NDVI_min|||||
|7|VHI|Vegetation Health Index|Derived from<br>MODIS|Combined vegetation<br>stress index|=|_αVCI_ +|_βTCI_|✓||✓|✓|
|8|EVI|Enhanced Vegetation Index|MODIS|Improved vegetation<br>index|—|||✓||✓|✓|
|9|PET|Potential<br>evapotranspiration|TerraClimate|Atmospheric demand for<br>moisture|—|||✓|✓||✓|
|10|Tmin|Minimum temperature|TerraClimate|Monthly minimum<br>temperature|—|||✓|✓|||
|11|Tmax|Maximum temperature|TerraClimate|Monthly maximum<br>temperature|—|||✓|✓|||
|12|Pre|Precipitation|TerraClimate|Total rainfall|—|||✓|✓|||
|13|PCI|Precipitation Condition<br>Index|Derived from<br>TerraClimate|Precipitation anomaly|=|_Pre_−<br>_Pre_max−|_Pre_min<br>_Pre_min|✓|✓||✓|
|14|RAI|Rainfall Anomaly Index|Derived from<br>TerraClimate|Rainfall deviation from<br>the mean|=|_Pre_−<br><br>_δ Pr_|_Premean_<br>_e_|✓|✓|||
|15|DEM|Digital Elevation Model|USGS|Elevation|—|||✓||✓||
|16|Sl|Slope of the terrain|Derived from DEM|Terrain steepness|—|||✓||||
|17|Rghn|Roughness of the terrain|Derived from DEM|Local terrain variability|=|_FSmean_−<br>_FS_max−|_FS_min<br>_FS_min|✓||||



Note: Sc01: Scenario 01, Sc02: Scenario 02, Sc03: Scenario 03, Sc03: Scenario 03 

6 

_Journal of Hydrology: Regional Studies 64 (2026) 103211_ 

## _2.4.2. Bias Correction of the Gridded Datasets_ 

To improve the accuracy of the gridded precipitation and PET datasets, Empirical Quantile Mapping (EQM) was used to align the cumulative distribution functions (CDFs) of the gridded data with observed station data, thereby minimizing systematic biases while preserving statistical properties. EQM corrects the distribution of modeled or remote sensing data to match the distribution of observed or reference data by mapping the quantiles of the target data to the corresponding quantiles of the reference data. The method is nonparametric and effectively corrects biases in the mean, variance, and shape of the distribution (Gudmundsson et al., 2012). Monthly PET was calculated at each station using observational data (1991–2013) along with recorded precipitation, which then served as the reference for bias-correcting TerraClimate records for 2001–2023, using the overlapping period (2001–2013) to derive correction factors. 

Bias correction was applied station by station, with quantile mapping adjusted for seasonal variation through monthly corrections and then extended to the entire study area. The EQM transformation is defined as: 

_xcorrected_ = _O_<sup>−1(</sup> _G_ ( _xgridded_ ) ) 

(2) 

where _x_ gridded is the raw gridded value, _G_ ( _x_ gridded) is its CDF, _O_<sup>−1</sup> is the inverse CDF of the observed data, and _x_ corrected is the resulting bias-corrected value. 

## _2.4.3. Machine Learning Models_ 

After data preparation, five machine learning models were developed to estimate drought conditions using SPEI03 and SPEI06 as target variables. This section outlines the development and implementation process of each model. 

## _2.4.4. Artificial Neural Network_ 

The Artificial Neural Network (ANN) model was developed in this study to estimate drought conditions using SPEI03 and SPEI06. The model was implemented using the _caret_ package in R, which facilitated the training process, while the _nnet_ package was used internally to fit the neural network. The _nnet_ package is particularly suited for regression tasks, making it ideal for this application. The ANN model followed a feedforward architecture with a single hidden layer. The predicted output is expressed as: 



where: 

- _H_ is the number of hidden neurons, 

- _αjk_ and _βj_ are connection weights, 

- _g_ (·)is the activation function (e.g., logistic), 

- _p_ is the number of predictors. 

The model parameters are estimated by minimizing the regularized mean squared error: 



where _λ_ is the weight decay parameter controlling model complexity. 

To optimize model performance, hyperparameter tuning was conducted using a grid search, testing hidden layer sizes of 5, 10, and 15, along with decay rates of 0.1 and 0.01. 

## _2.4.5. Random Forest_ 

The Random Forest (RF) model was implemented to estimate drought conditions using SPEI03 and SPEI06 as the target variables. The model was developed using the _randomForest_ and _caret_ packages in R, enabling efficient hyperparameter optimization and robust model evaluation. A grid search approach was employed to optimize the _mtry_ parameter, which determines the number of predictors randomly sampled at each split in the decision trees. Random Forest constructs an ensemble of _B_ regression trees. The prediction is the average of individual trees: 



where: 

- _Tb_ represents the _b_ -th decision tree, 

- Each tree is trained on a bootstrap sample, 

- At each split, a random subset of predictors of size _mtry_ is considered. 

7 

_Journal of Hydrology: Regional Studies 64 (2026) 103211_ 

_K. Qaraghuli et al.                                                                                                                                                                                                     Journal of Hydrology: Regional Studies_ 

RF reduces variance through averaging and improves generalization performance. 

The grid search evaluated values of (2, 4, 6, 8, 10), while the number of trees ( _ntree_ ) was fixed at 200, balancing computational efficiency with model complexity. 

## _2.4.6. Gradient Boosting Machine_ 

The Gradient Boosting Machine (GBM) model was implemented to estimate drought conditions using SPEI03 and SPEI06 as target variables. The model was developed using the _caret_ and _gbm3_ packages in R, facilitating training and hyperparameter optimization. A grid search approach was employed to optimize key parameters, including the number of trees (50, 100, 150), interaction depth (1, 3, 5), learning rate (0.01, 0.1), and minimum node size (10). A 5-fold cross-validation procedure was used to ensure robust model evaluation and minimize the risk of overfitting. Following hyperparameter selection, the final GBM model was trained using 70 % of the dataset and validated on the remaining 30 % test set to assess predictive performance. The observed and predicted values were exported as CSV files for further analysis. GBM builds an additive model sequentially: 



where: 

- _ht_ ( **x** )is the regression tree fitted to the residuals at iteration _t_ , 

- _ν_ is the learning rate, 

- _t_ = 1 _,_ … _, T_ denotes boosting iterations. 

The model minimizes a differentiable loss function, here the squared error: 



Thus, each tree corrects the errors of the previous ensemble. 

## _2.4.7. Extreme Gradient Boosting_ 

Extreme Gradient Boosting (XGB) was employed to estimate drought conditions using SPEI03 and SPEI06 as the target variables. The implementation leveraged the _caret_ and _xgboost_ packages in R, streamlining model training, hyperparameter tuning, and performance evaluation. To optimize computation and memory efficiency, _xgb.DMatrix_ objects were used to format training and test sets after data splitting, ensuring structured input for the XGB model. XGB is a machine learning algorithm realized by gradient lifting technology, it is an enhanced GBDT algorithm. Its base classifier is the Classification and Regression Tree (CART). XGB is a tree integration model combines multiple CART (Chen, 2016). The XGB model is built by adding trees iteratively. The predicted value of the i-th sample in the t-th iteration can be expressed as follows: 



The tree is added iteratively to minimize the objective function, which can be expressed as: 



where _oooooo_ is the loss function and _ΩΩ_ ( _fftt_ ) represents the model complexity. 

The model was trained using the squared error regression objective function ( _reg:squarederror_ ), which is well-suited for regression tasks as it minimizes the mean squared error between predicted and actual values. Hyperparameter tuning was conducted using crossvalidation with early stopping, exploring fixed values for key parameters, including a learning rate of 0.01, a maximum tree depth of 6, and subsampling and column sampling ratios of 0.8 each. These configurations were evaluated using 5-fold cross-validation over a maximum of 1000 boosting iterations, ensuring robust model assessment. Early stopping was employed to halt training if no improvement in validation error was observed over 10 consecutive rounds, effectively identifying the optimal number of boosting iterations. Following hyperparameter optimization, the final XGB model was trained using the optimal configuration and applied to the test dataset to generate predictions. The predicted and observed values were exported as CSV files for further analysis and model performance evaluation. 

## _2.4.8. Support Vector Regression_ 

Support Vector Regression (SVR) was applied to estimate drought conditions using the SPEI03 and SPEI06 as the target variables. The implementation utilized the _caret_ and _e1071_ packages in R, enabling efficient model evaluation and hyperparameter tuning. Two kernel functions were considered: the Radial Basis Function (RBF) kernel and the Linear kernel. 

SVR estimates a function: 

_f_ ( **x** ) = **w**<sup>⊤</sup> _ϕ_ ( **x** ) + _b_ 

8 

_Journal of Hydrology: Regional Studies 64 (2026) 103211_ 

_K. Qaraghuli et al.                                                                                                                                                                                                     Journal of Hydrology: Regional Studies_ 

where: 

- _ϕ_ ( **x** )maps inputs into a higher-dimensional feature space, 

- **w** and _b_ are model parameters. 

The optimization problem is: 



subject to: 



where: 

- _ε_ defines the insensitive loss margin, 

- _C_ is the regularization parameter, 

- _ξi, ξ_<sup>∗</sup> _i_<sup>are slack variables.</sup> 

For nonlinear modeling, the Radial Basis Function (RBF) kernel was applied: 

_K_ ( **x** _i,_ **x** _j_ ) = exp ( − _σ_ ∣∣ **x** _i_ − **x** _j_ ∣∣<sup>2</sup> ) 

Hyperparameter tuning was conducted using a grid search approach. For the RBF kernel, tuning included combinations of the regularization parameter _C_ (0.1, 1, 10) and the kernel-specific parameter σ (0.01, 0.05, 0.1). For the Linear kernel, tuning was applied solely to _C_ (0.1, 1, 10) since it does not require a kernel parameter. A 5-fold cross-validation procedure ensured rigorous model evaluation while minimizing overfitting. After training both models, their performance was compared, and the model yielding the lowest RMSE was selected for final predictions. The trained model was then applied to the test dataset, and the observed and predicted values were exported as CSV files for further analysis. 

To enhance reliability, a repeated 5-fold cross-validation procedure with three repetitions was employed, managed using the _trainControl()_ function in R, which specified the number of folds and repetitions, ensuring consistency and reliability in the evaluation. The dataset was partitioned into training (70 %) and testing (30 %) subsets, ensuring a structured evaluation process. After training, the model was applied to the test dataset, and predicted values were stored in CSV files for subsequent analysis. 

## _2.4.9. Performance Metrics for the model's evaluation_ 

Model performance was evaluated using four standard metrics: the coefficient of determination (R²), root mean square error (RMSE), mean absolute error (MAE), and Nash-Sutcliffe efficiency (NSE), which collectively assess both accuracy and consistency of the predictions. Table 5 details the evaluation metrics. Several performance indices, including, the mean absolute error (MAE) (Malik et al., 2020) and the root mean square error (RMSE) were used to evaluate the applied models (Behar et al., 2013; Gueymard, 2014). In this research, the Root Mean Square Error (RMSE) (Peng et al., 2005) serves as a measure of the standard sample variance between the predicted and observed values, emphasizing a greater tolerance for smaller errors compared to larger discrepancies. 

**Table 5** 

Details of the statistical evaluation metrics. 

|**Metric**|**Formula**|**Range**|**Best Score**|
|---|---|---|---|
|MAE|=<br>1<br>_n_<br>∑_n_<br>_i_=1 <sup>|</sup><sup>_Mi_ −</sup><sup>_Oi_|</sup>|(0,∞)|0|
|RMSE|=<br>1<br>_n_<br>∑_n_<br>_i_=1 <sup>(</sup><sup>_Mi_ −</sup><sup>_Oi_)2</sup><br>√|(0,∞)|0|
|NSE|=<br>1 −<br>∑_n_<br>_i_=1 <sup>(</sup><sup>_Mi_ −</sup><sup>_Oi_)2</sup><br>~~∑~~_n_<br>_i_=1<sup>(</sup><sup>_Mi_ −</sup><br>_O_)<sup>2</sup>|(-∞, 1)|1|
|R²|=<br>( ∑_n_<br>_i_=1 <sup>(</sup><sup>_Oi_ −</sup><br>_O_)(_Mi_−<br>_M_)<br>)2|(0, 1)|1|
||~~∑~~_n_<br>_i_=1 <sup>(</sup><sup>_Oi_ −</sup><br>_O_)<sup>2 </sup><sup>~~∑~~</sup><sup>_n_</sup><br>_i_=1 <sup>(</sup><sup>_Mi_ −</sup><br>_M_)<br>2|||



Note: Mi: the predicted value of the drought index (SPEI03 or SPEI06) generated by the machine learning model for sample **_i_** , **_Oi_** : the observed (reference) SPEI value for sample **_i_** , **_M_** : the mean of the predicted SPEI values, **_O_** : the mean of the observed SPEI values, **_n_** is the total number of samples used in model evaluation and **_i_** : the index of the sample, where **_i_** = **_1_** _,_ **_2_** _,_ … _,_ **_n_** . 

9 

_Journal of Hydrology: Regional Studies 64 (2026) 103211_ 

_K. Qaraghuli et al.                                                                                                                                                                                                     Journal of Hydrology: Regional Studies_ 

_2.4.9.1. Feature importance for drought estimation models._ To assess the contribution of predictor variables in drought modeling, SHapley Additive exPlanations (SHAP) was applied to the XGB model for both SPEI03 and SPEI06 across the study area. Recognizing that drought characteristics vary significantly with climate and topography, Iraq was partitioned into homogeneous drought regions rather than using an arbitrary geographical split. A K-means clustering algorithm was applied to long-term spatial data of mean annual precipitation, mean annual temperature, and elevation. This data-driven approach groups grid cells with similar climatological and topographical characteristics, ensuring that the subsequent drought analysis is performed over physically meaningful zones [Gocic and Trajkovic, (2013)]. Based on the analysis, the study area was divided into four regions: northeast (NE), northwest (NW), southeast (SE), and southwest (SW). This division enabled a more localized assessment of predictor impact, ensuring that regional variations in climate and environmental influences on drought dynamics were effectively captured. The application of SHAP provided a quantitative measure of each feature’s contribution to model predictions, enhancing interpretability while maintaining predictive accuracy. SHAP, grounded in cooperative game theory (Shapley, 1953), determines the relative contribution of each feature to the model’s prediction by computing Shapley values. These values provide a unified framework for interpreting machine learning outputs by quantifying the marginal impact of each predictor (Xue et al., 2024). The Shapley value for a given feature _m_ is defined as: 



where _ϕm_ ( _v_ ) represents the contribution of feature _m_ to the model prediction, _N_ is the set of all features, _S_ is a subset of _N_ , ( _v_ ( _S_ U { _m_ }) – _v_ ( _S_ )) denote the model outputs when feature _m_ is included and excluded, respectively, and the term | _S_ |!(| _N_ | − | _S_ | − 1 )! _/_ | _N_ |! represents the probability of different feature combinations occurring, ensuring that each feature’s contribution is fairly weighted across all possible subsets. The result obtained from this equation quantifies the marginal contribution of feature _m_ to the final model predictions by averaging its impact across all possible feature groupings. 

## **3. Results and discussion** 

## _3.1. Machine learning-based drought modelling_ 

The performance of the five machine learning models under the four input scenarios was evaluated on the independent test period (2001–2013). Table 6 and Figs. 3 and 4 present the evaluation metrics (R², RMSE, MAE, KGE) for SPEI-03 and SPEI-06 predictions. The analysis focuses on comparing model architectures and understanding the significance of different input data combinations. The meteorological Scenario 01 serves as a crucial benchmark, representing the model's ability to replicate the physical basis of SPEI. The key scientific insights are derived from comparing the performance of the land-surface Scenario 02, comprehensive Scenario 03, and parsimonious Scenario 04 scenarios against this baseline, which highlights the potential for drought prediction using alternative data sources and optimized input sets. 

Model performance was evaluated under four different predictor scenarios to assess the impact of feature selection on SPEI03 and SPEI06 estimation accuracy. Performance was assessed using R², RMSE, NSE, and MAE metrics. A comparative summary is provided in Table 6 and visualized in Fig. 3 and Fig. 4. 

**Table 6** 

Performance metrics of five machine learning models across four scenarios for estimating SPEI03 and SPEI06. 

|||**SPEI03**||||**SPEI06**||||
|---|---|---|---|---|---|---|---|---|---|
||**Model**|**R²**|**RMSE**|**NSE**|**MAE**|**R**<sup>**2**</sup>|**RMSE**|**NSE**|**MAE**|
|Scenario 01|ANN|0.4266|0.7545|0.3946|0.5999|0.4222|0.7523|0.4014|0.6033|
||RF|0.9003|0.3116|0.8903|**0.2022**|0.9067|0.2999|0.8980|**0.1971**|
||XGB|**0.9047**|**0.3044**|**0.8961**|0.2071|**0.9093**|**0.2989**|**0.8991**|0.2073|
||GBM|0.8543|0.3915|0.8369|0.2924|0.8657|0.3696|0.8529|0.2786|
||SVR|0.5615|0.7258|0.4031|0.5517|0.5212|0.7450|0.3713|0.5678|
|Scenario 02|ANN|0.2637|0.8431|0.2497|0.6760|0.2065|0.8763|0.1964|0.6948|
||RF|**0.8797**|**0.3284**|**0.8756**|**0.1786**|**0.8659**|**0.3479**|**0.8609**|**0.1876**|
||XGB|0.8494|0.3834|0.8371|0.2600|0.8308|0.4149|0.8106|0.2851|
||GBM|0.6999|0.5479|0.6803|0.4281|0.6565|0.5883|0.6302|0.4597|
||SVR|0.3007|0.8261|0.2783|0.6331|0.2258|0.9087|0.1196|0.6956|
|Scenario 03|ANN|0.3710|0.7770|0.3609|0.6214|0.4446|0.7332|0.4312|0.5886|
||RF|**0.7292**|**0.5048**|**0.7234**|**0.3485**|**0.7730**|**0.4626**|**0.7681**|**0.3158**|
||XGB|0.7220|0.5129|0.7157|0.3720|0.7639|0.4806|0.7505|0.3493|
||GBM|0.6168|0.6050|0.6108|0.4717|0.6765|0.5535|0.6712|0.4308|
||SVR|0.4632|0.7303|0.4270|0.5474|0.5086|0.7165|0.4320|0.5434|
|Scenario 04|ANN|0.4439|0.7274|0.4412|0.5753|0.4857|0.7009|0.4819|0.5652|
||RF|**0.8482**|**0.3783**|**0.8420**|**0.2373**|**0.8621**|**0.3598**|**0.8564**|**0.2296**|
||XGB|0.8436|0.3895|0.8345|0.2729|0.8592|0.3708|0.8496|0.2656|
||GBM|0.7253|0.5158|0.7167|0.4003|0.7410|0.4987|0.7322|0.3916|
||SVR|0.5576|0.6502|0.5528|0.4688|0.6075|0.6135|0.6013|0.4517|



Note: Bold font represents the best performance 

10 

_Journal of Hydrology: Regional Studies 64 (2026) 103211_ 



**Fig. 3.** Radar plot visualization comparing the performance of five machine learning models across four scenarios using SPEI03 as a response variable. 

Scenario 01 incorporated all seventeen predictors spanning meteorological, vegetation, soil, and topographic factors (Table 4). The results indicate that XGB and RF consistently outperformed the other models, effectively capturing complex, nonlinear relationships between drought predictors and SPEI values. For SPEI03, XGB achieved the highest accuracy (R² = 0.905, NSE = 0.896) and lowest error (RMSE = 0.304, MAE = 0.207), followed closely by RF. Similarly, for SPEI06, XGB attained R² = 0.909, NSE = 0.899, with the lowest RMSE (0.298). The strong performance of XGB and RF is attributed to their ensemble learning capabilities, which enable them to model complex interactions between multiple variables while effectively handling collinearity. This scenario serves as a baseline for comparing reduced predictor sets. In scenario 02, when limiting the input to six meteorological predictors, RF and XGB remained the most accurate models, demonstrating their ability to extract meaningful patterns from climate-related variables. For SPEI03, RF achieved the highest accuracy (R² = 0.880, NSE = 0.875, RMSE = 0.328), while for SPEI06, it maintained superior performance (R² = 0.866, NSE = 0.860, RMSE = 0.348) followed closely by XGB, reinforcing the robustness of ensemble models for drought estimation even with fewer features. In contrast, ANN, GBM, and SVR showed weaker performance, suggesting that these models are more sensitive to limited predictor sets. 

Scenario 03 focused exclusively on the soil and vegetation predictors. RF remained the best-performing model, achieving R² = 0.729, NSE = 0.723, and RMSE = 0.504 for SPEI03, with similar results for SPEI06. However, a noticeable decline in model accuracy was observed across all models compared to Scenario 1, indicating that meteorological variables play a crucial role in drought estimation. ANN and SVR performed the weakest, suggesting that these models struggle to effectively learn from soil-vegetation features alone, whereas RF demonstrated greater adaptability due to its ability to handle nonlinear interactions within the feature set. 

Scenario 04 utilized a selected set of six variables, strategically selected from each predictor category. RF and XGB continued to demonstrate strong predictive capability, with RF achieving R² = 0.848, NSE = 0.842 for SPEI03 and R² = 0.862, NSE = 0.856 for SPEI06. Although performance slightly declined compared to Sc01, both ensemble models maintained high accuracy, indicating effective generalization when using fewer but diverse features. 

In contrast, ANN, GBM, and SVR showed further reductions in accuracy, reinforcing their reliance on higher-dimensional input data for optimal performance. These findings confirm the consistent advantage of ensemble learning methods when employing a wellbalanced multivariate predictor set. 

11 

_Journal of Hydrology: Regional Studies 64 (2026) 103211_ 



**Fig. 4.** Radar plot visualization comparing the performance of five machine learning models across four scenarios using SPEI06 as a response variable. 

## _3.2. Comparative analysis of the applied models_ 

The comparative evaluation of machine learning models under varying predictor scenarios yields critical insights into the predictive importance of different variable groups and the performance strengths of individual algorithms. The analysis specifically highlights two key dimensions: the influence of predictor groupings on drought modelling accuracy, and the superiority of ensemble learning methods (particularly Random Forest (RF) and XGBoost (XGB)) in capturing drought dynamics. 

Scenario 01, which incorporated all seventeen predictors (including meteorological, vegetation, soil, and topographic variables) achieved the highest model performance for both SPEI03 and SPEI06. This comprehensive feature set enabled the models to capture the multifactorial nature of drought processes, where the interplay between short-term climatic anomalies and longer-term biophysical conditions governs both the spatial distribution and temporal evolution of drought. The integration of diverse input layers enhanced the models’ ability to simulate rapid-onset droughts as well as prolonged dry spells, offering a more holistic view of drought behavior. 

Interestingly, Scenario 02, which utilized only six meteorological predictors, also yielded strong predictive outcomes, nearly approaching the performance of the full-feature model. This finding underscores the dominant role of meteorological drivers in controlling drought variability. The implications are particularly significant in an operational context: meteorological data are typically more accessible, frequent, and reliable than vegetation or soil datasets. This positions Scenario 02 as a highly practical solution for real-time drought monitoring, particularly in data-scarce or resource-constrained regions. 

In contrast, Sc03 and Sc04, which relied exclusively on vegetation, soil, and topographic variables, exhibited marked declines in model accuracy. This outcome reflects the limited standalone predictive power of these groups. Vegetation indices, for example, typically respond to drought conditions rather than serve as early indicators, while topographic features are static and do not directly capture the dynamic climatic fluctuations relevant to drought onset. These findings suggest that non-meteorological indicators are most valuable when used in conjunction with core climatic variables, rather than as independent predictors. 

Across all scenarios, RF and XGB consistently outperformed the remaining models (GBM, SVR, and ANN), demonstrating exceptional adaptability to different input configurations and temporal scales. Their ensemble-based architecture enables them to model complex, nonlinear relationships among predictors while maintaining computational efficiency and resilience to overfitting. 

RF leverages bagging (bootstrap aggregation), where multiple decision trees are trained on random subsets of the data, and their predictions are averaged to reduce variance and improve generalization (Ali et al., 2025; Chen, 2025). This makes RF particularly robust in high-dimensional and noisy environments. In contrast, XGB applies gradient boosting, where trees are added sequentially to 

12 

_Journal of Hydrology: Regional Studies 64 (2026) 103211_ 

minimize the residual errors of prior trees. This iterative approach allows XGB to capture intricate interactions and fine-grained dependencies in the data. 

These structural advantages help explain why both models retained high accuracy even under reduced-input conditions such as Scenario 02. Their ability to extract meaningful patterns from limited data inputs demonstrates their strong generalization capability, 



**Fig. 5.** Spatial variability analysis of SPEI03 and SPEI06 estimations using XGB and RF under Scenario 1. Statistical maps display Q1, Median, Q3, and IQR. 

13 

_Journal of Hydrology: Regional Studies 64 (2026) 103211_ 

_K. Qaraghuli et al._ 

an essential trait for drought prediction in data-limited regions. 

The findings of this study are consistent with prior literature. Mokhtar et al. (2021) reported that RF and XGB outperformed deep learning models such as CNN and LSTM in similar drought modelling tasks. Likewise, Zamani et al. (2025) showed that XGB achieved the highest performance in predicting a multivariate drought index (Joint Deficit Index) derived from SPI and SRI using a copula-based 



**Fig. 6.** Spatial variability analysis of SPEI03 and SPEI06 estimations using XGB and RF under Scenario 02. Statistical maps display Q1, Median, Q3, and IQR. 

14 

_Journal of Hydrology: Regional Studies 64 (2026) 103211_ 

_K. Qaraghuli et al.                                                                                                                                                                                                     Journal of Hydrology: Regional Studies_ 

framework, reinforcing its robustness in hydrometeorological modelling. 

Overall, this analysis reaffirms that ensemble learning algorithms (particularly RF and XGB) are exceptionally well-suited for drought prediction. Their flexibility, resilience to limited input availability, and robustness across diverse predictor scenarios position 



**Fig. 7.** SHAP-based feature importance for SPEI03 across the four regions (NE, NW, SE, SW), horizontal bars represent the average absolute SHAP values. 

15 

_Journal of Hydrology: Regional Studies 64 (2026) 103211_ 

_K. Qaraghuli et al.                                                                                                                                                                                                     Journal of Hydrology: Regional Studies_ 

them as optimal candidates for both research-focused applications and operational early warning systems in drought-prone or datascarce environments. 

## _3.3. Spatial variability and model stability in drought estimation_ 

A spatial analysis of boxplot statistics (including the First Quartile (Q1), Median, Third Quartile (Q3), and Interquartile Range (IQR)) was performed to assess the performance and stability of the RF and XGB models in estimating short- and medium-term drought conditions, as represented by the SPEI03 and SPEI06 indices across the two best-performing scenarios. Model accuracy was evaluated using residuals, defined as the difference between observed and predicted SPEI values. Residuals closer to zero indicate higher accuracy, with negative values representing overestimations and positive values indicating underestimations. 

In Sc01, as shown in 

Fig. 5, for estimating SPEI03, both models demonstrate similar spatial performance at the Q1 (25th percentile), although RF shows slightly better accuracy in the central part of the study area, where residuals cluster around − 0.5. 

This suggests that RF is marginally more effective at reducing substantial underestimations in that region. Median residuals for both models are tightly concentrated between − 0.1 and 0.1, indicating minimal bias and overall balanced predictions. RF displays a slightly broader spatial extent of − 0.1 residuals, which reflects a consistent, mild tendency to overestimate. Despite this overestimation, the pattern remains stable, contributing to its spatial reliability. 

When considering Q3 (75th percentile), both models yield residuals predominantly in the 0.5–0.7 range. However, RF demonstrates a wider and more favorable spatial distribution, particularly in the eastern and western portions of the study area, suggesting improved capacity to handle moderate overestimations. Although both models exhibit similar IQR patterns, RF achieves a marginally smaller IQR in the eastern region, indicating reduced residual variability and greater consistency in its predictive performance. 

For SPEI06, the models again show comparable spatial behavior. Q1 residuals are generally between − 0.7 and − 0.5, with XGB performing slightly better in the northern areas by more effectively minimizing underestimations. Both models maintain Median residuals within the − 0.1–0.1 range, suggesting limited bias and balanced predictions. Nonetheless, RF covers a slightly broader spatial area with near-zero residuals, particularly in the central and northern regions, indicating more conservative and stable estimates. Similarly, for the Q3 level, residuals for both models remain within the 0.5–0.7 range. RF exhibits a slight advantage in the central and southern parts of the study area, where its broader distribution of moderate positive residuals suggests enhanced ability to manage overestimations and improved spatial robustness. IQR values for both models are nearly identical, reinforcing their comparable stability in predicting medium-term drought conditions. 

For Scenario 02, we observe different spatial patterns, as shown in Fig. 6, for SPEI03, at Q1, both models demonstrate good spatial performance; however, XGB shows a slight advantage, particularly in the northern parts of the study area, where it more effectively minimizes underestimations. The median residuals remain closely aligned for both models, with values concentrated between − 0.1 and 0.1, indicating minimal bias and balanced predictions across the region. In terms of Q3, XGB again outperforms RF, with residuals reaching around 0.4 in most parts of the study area, reflecting better management of moderate overestimations. The IQR values further support this trend, with XGB showing improved performance, especially across northern areas, suggesting lower variability and enhanced prediction reliability compared to RF. 

For SPEI06, at the Q1, XGB demonstrates superior performance across most areas of the study region, with a noticeable advantage in the western parts, where it more effectively reduces underestimations. The median residuals for both models are nearly identical, remaining within the − 0.1–0.1 range, which indicates low bias and generally balanced predictions. At Q3, XGB outperforms RF, particularly in the central and southern regions, where it handles moderate overestimations more effectively and displays greater spatial consistency. Regarding the IQR, XGB again shows better performance, especially in the northern areas, suggesting reduced variability and improved stability in medium-term drought prediction compared to RF. While Scenario 01 highlights the spatial stability and consistent performance of both models, with RF showing marginally better spatial characteristics, such as broader nearzero residual zones and reduced variability, Scenario 02 reveals a different spatial pattern. It emphasizes XGB’s ability to manage moderate overestimations and reduce residual variability, particularly in northern and western regions. 

Together, these scenarios underscore the sensitivity of model performance to spatial and temporal factors, suggesting that selecting between RF and XGB depends on the specific objectives and regional characteristics relevant to drought estimation. 

## _3.4. Feature importance analysis for drought estimation_ 

The SHAP-based feature importance analysis for SPEI03 highlights distinct regional variations in predictor influence, emphasizing the dominant factors shaping short-term drought conditions. Across all four regions, precipitation (Pre) consistently emerges as the most influential variable, reinforcing its fundamental role in controlling drought variability. However, the significance of other predictors varies spatially, reflecting differences in climatic and environmental conditions (Fig. 7). 

In the northeastern (NE) region, precipitation remains the dominant predictor, followed by RAI, DEM, and Tmax. The moderate SHAP importance of DEM suggests that elevation influences drought severity, likely by modulating precipitation distribution, runoff processes, and localized moisture retention. The presence of temperature-related factors (Tmax, TCI) alongside DEM further indicates that topography and thermal conditions interact to shape drought persistence, particularly by affecting evapotranspiration rates and atmospheric moisture dynamics. A similar pattern is observed in the northwestern (NW) region, where precipitation and RAI retain the highest influence, while LST and TCI also play a notable role. The relatively higher contribution of temperature-related indices in these two northern regions suggests that temperature stress intensifies short-term drought effects, primarily by enhancing 

16 

_Journal of Hydrology: Regional Studies 64 (2026) 103211_ 

evapotranspiration and reducing soil moisture availability. In the southeastern (SE) region, Tmax surpasses precipitation as the leading predictor, followed closely by LST and RAI. This suggests that temperature extremes exert a stronger influence on drought dynamics in this area, reinforcing the role of heat stress in driving moisture deficits. While vegetation-related indices such as VCI contribute to drought predictions, their influence is less pronounced than temperature and precipitation-driven indices. Meanwhile, PCI reflects precipitation variability, indicating that fluctuations in rainfall continue to shape drought conditions despite the dominance of 



**Fig. 8.** Violin plots illustrate the distribution of SHAP values for predictor variables in SPEI03 across the four regions. The width of each violin represents the density of SHAP values, showing the variability in feature importance across predictions. 

17 

_Journal of Hydrology: Regional Studies 64 (2026) 103211_ 

_K. Qaraghuli et al.                                                                                                                                                                                                     Journal of Hydrology: Regional Studies_ 

temperature-related factors. The southwestern (SW) region exhibits a balanced distribution of predictor influence, with Pre ranking highest, followed by Tmax, LST, and PCI. This highlights the combined effects of temperature and precipitation variability in shaping drought conditions. The moderate contribution of NDVI suggests that vegetation stress plays a role in moisture regulation, reflecting 



**Fig. 9.** SHAP-based feature importance for SPEI06 across the four regions (NE, NW, SE, SW), horizontal bars represent the average absolute SHAP values. 

18 

_Journal of Hydrology: Regional Studies 64 (2026) 103211_ 

_K. Qaraghuli et al.                                                                                                                                                                                                     Journal of Hydrology: Regional Studies_ 

ecosystem sensitivity to drought conditions. While RAI accounts for precipitation anomalies and contributes to drought variability, its influence remains secondary to direct precipitation indicators (Pre, PCI). Similarly, Tmin has a role in drought conditions but exerts a weaker effect compared to Tmax and LST, which more strongly influence evapotranspiration moisture depletion. 

The violin plot distributions (Fig. 8) further illustrate these regional differences. Precipitation consistently exhibits a strong and uniform influence across all regions, reinforcing its primary role in short-term drought prediction. However, temperature-related predictors (Tmax, LST, and TCI) show greater variability, particularly in the SE and NW regions, indicating that their influence on drought is more regionally dependent. RAI and DEM display broader distributions in some regions, suggesting that their impact on drought conditions is more variable and context dependent. 

The SHAP-based feature importance analysis for SPEI06 reveals distinct variations in predictor contributions across the four regions, reflecting the influence of medium-term drought drivers. While Pre remains a relevant predictor, its dominance is slightly reduced compared to SPEI03, suggesting that a broader set of factors influences longer-term drought conditions (Fig. 9). 

In the NE region, LST and NDVI emerge as the most influential predictors, followed by EVI, PCI, and VHI. The high ranking of temperature and vegetation indices underscores their role in prolonged moisture stress and evapotranspiration-driven drought conditions. The presence of Tmin and SM further highlights the combined effects of heat stress and declining subsurface moisture levels, reinforcing their influence in medium-term drought persistence. In the NW region, on the other hand, EVI and LST emerge as the most influential predictors, followed by NDVI, VHI, and PET. The strong presence of vegetation indices highlights the significant role of plant health in drought response, while the high importance of temperature-related variables suggests the influence of land surface heating and evapotranspiration-driven moisture loss. In the SE region, LST and EVI are the most influential predictors, followed by PCI, NDVI, and DEM. The high importance of temperature and vegetation indices suggests that surface heating and vegetation stress are primary drivers of drought persistence, reinforcing the impact of prolonged moisture deficits. The moderate ranking of Pre and PET indicates that while precipitation remains relevant, evaporative demand and surface energy fluxes play a greater role in controlling drought variability. 

Similarly, in the SW region, LST and EVI emerge as the most influential predictors, followed by NDVI, PCI, and DEM. The dominance of temperature and vegetation indices indicates that surface heating and vegetation health significantly influence drought conditions, highlighting the role of evapotranspiration and land-atmosphere interactions. The moderate ranking of PET and RAI suggests that cumulative moisture deficits, rather than immediate precipitation variability, play a larger role in shaping drought persistence. 

The violin plots for SPEI06 (Fig. 10) further illustrate these trends, revealing greater variability in the influence of temperature and vegetation indices compared to SPEI03, particularly in the SE and SW regions. 

This suggests that SPEI06 predictions are more influenced by long-term climatic patterns and environmental feedback mechanisms rather than immediate meteorological conditions. In contrast to SPEI03, where precipitation remained the dominant driver, the influence of land surface temperature, vegetation health, and soil moisture indicators increases over longer timescales. This shift reflects the delayed response of these factors to drought persistence, emphasizing the importance of monitoring long-term environmental interactions. 

Overall, the results highlight a clear shift in predictor importance from precipitation-driven short-term drought (SPEI03) to a more complex interaction of temperature, vegetation, and soil moisture in medium-term drought (SPEI06). These findings emphasize the need for regionally adaptive drought monitoring frameworks that account for shifting drought drivers over different timescales, improving both predictive accuracy and decision-making effectiveness. 

## **4. Conclusions** 

The key conclusions from the development and comparison of various Machine Learning models for drought estimation are as follows, the evaluation and comparison of machine learning models for drought estimation underscore the effectiveness of multivariate approaches in improving forecasting accuracy. Model performance varied across four predictor scenarios, depending on the nature and combination of input variables. XGB achieved the highest accuracy when utilizing all predictors (meteorological, vegetation, soil, and topographic), demonstrating the advantage of comprehensive environmental data, as evidenced in Scenario 1. In contrast, RF outperformed other models under more limited input conditions, confirming its robustness across Scenarios 2, 3, and 4. Reliance solely on meteorological variables provided satisfactory accuracy for drought forecasting, emphasizing the central role of climate-based inputs, as demonstrated in Scenario 2. Using only soil and vegetation variables resulted in the lowest predictive accuracy due to the absence of meteorological data, limiting the model’s capacity to capture drought variability, as shown in Scenario 3. Moderate performance was observed when topographic variables were excluded, highlighting the added value of integrating multiple environmental drivers, as illustrated in Scenario 4. Overall, both RF and XGB demonstrated strong effectiveness in drought prediction, with Random Forest proving most reliable under data-limited conditions and XGB excelling when a full set of predictors was available. These insights underscore the vital role of advanced machine learning techniques in capturing complex environmental interactions. Integrating diverse environmental variables within such models is essential for developing robust early warning systems and advancing climate resilience strategies. The analysis revealed notable regional variability in the drivers of drought across short-term (SPEI03) and medium-term (SPEI06) timescales. Precipitation consistently emerged as the primary factor influencing short-term drought variability, while temperature, vegetation health, and soil moisture became critical drivers of prolonged drought conditions. This highlights the crucial necessity for region-specific drought monitoring strategies that can adapt to changing climatic influences. In particular, the northeastern (NE) and northwestern (NW) regions exhibited strong contributions from precipitation and the Rainfall Anomaly Index (RAI), alongside significant effects from temperature-related variables such as Tmax, TCI, and LST. 

19 

_Journal of Hydrology: Regional Studies 64 (2026) 103211_ 

_K. Qaraghuli et al.                                                                                                                                                                                                     Journal of Hydrology: Regional Studies_ 



**Fig. 10.** Violin plots illustrate the distribution of SHAP values for predictor variables in SPEI06 across the four regions. The width of each violin represents the density of SHAP values, showing the variability in feature importance across predictions. 

Additionally, the influence of the Digital Elevation Model (DEM) in the NE region highlights how elevation shapes precipitation distribution and moisture retention, thereby modulating drought severity. Together, this evidence emphasizes the necessity for dynamic, multivariate drought assessment frameworks that integrate spatial and temporal complexities to improve the effectiveness and responsiveness of drought monitoring and management systems. For medium-term droughts (SPEI06), the analysis identified a clear transition from precipitation-dominated short-term droughts toward a complex interplay of temperature, vegetation indices (EVI, NDVI, VHI), and soil moisture as dominant factors sustaining drought persistence. Although precipitation remains relevant, its relative importance declines, particularly in the northern parts, reflecting the cumulative impact of prolonged moisture deficits. These dynamics highlight the significant role of land-atmosphere interactions (such as soil moisture depletion, vegetation stress, and 

20 

_Journal of Hydrology: Regional Studies 64 (2026) 103211_ 

_K. Qaraghuli et al.                                                                                                                                                                                                     Journal of Hydrology: Regional Studies_ 

evapotranspiration processes) in driving medium-term drought conditions beyond immediate precipitation anomalies. 

## **CRediT authorship contribution statement** 

**Khalid Qaraghuli:** Writing – original draft, Visualization, Software, Methodology, Conceptualization. **Mohamad Fared Murshed:** Writing – review & editing, Supervision. **Md Azlin Md Said:** Writing – review & editing, Supervision. **Ali Mokhtar:** Validation, Software. **Ali Salem:** Writing – review & editing, Visualization, Software, Funding acquisition. 

## **Declaration of Competing Interest** 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

## **Acknowledgments** 

The authors thank the School of Civil Engineering at Universiti Sains Malaysia for providing the supportive environment that made this research possible. We also extend our gratitude to the Iraqi Meteorological Organization and Seismology for supplying the meteorological station data used in this study. 

## **Data availability** 

Data will be made available on request. 

## **References** 

Abubakar, H.B., 2024. Evaluation of high-resolution precipitation datasets CHIRPS, TerraClimate and TAMSAT over the Enkangala Escarpment of South Africa. Al-Bazaz, H.A., Agha, O.M.A.M., 2023. A Study of the Homogeneity of Climatic Data for Rain, Temperature and Humidity for Nineveh Governorate. AlRafidain Eng. J. (AREJ) 28 (2), 173–185. https://doi.org/10.33899/rengj.2023.137763.1225. 

Ali, M., Hashmi, M.U., Ahmad, Z., Kazmi, N.U.A., Ittfaq, A., Ashraf, A., 2025. Hybrid Supervised Machine Learning Models for Enhanced Alzheimer’s Disease 

Classification. Proc. Pak. Acad. Sci.: A. Phys. Comput. Sci. 62 (4), 323–336. Al-Ozeer, A.Z., Abdaki, M.A., Al-Iraqi, A.R., Al-Samman, S.H., Al-Hammadi, N.A., 2020. Estimation of mean areal rainfall and missing data by using gis in nineveh, northern Iraq. Iraqi Geol. J. 53 (1), 93–103. https://doi.org/10.46717/igj.53.1e.7ry-2020-07.07. 

Al-Yaari, A., Condom, T., Anthelme, F., Cauvy-Frauni´e, S., Dangles, O., Junquas, C., Moret, P., Rabatel, A., 2024. Warming-induced cryosphere changes predict drier Andean eco-regions. Environ. Res. Lett. 19 (10). https://doi.org/10.1088/1748-9326/ad6ea6. 

- Behar, O., Khellaf, A., Mohammedi, K., 2013. A review of studies on central receiver solar thermal power plants. Renew. sustain. energy rev. 23, 12–39. 

- Casas, J.R., Chacon, R., Catbas, N., Riveiro, B., Tonelli, D., 2024. Remote Sensing in Bridge Digitalization: A Review. Remote Sens. 16 (23). ´ https://doi.org/10.3390/ rs16234438. 

Chen, T., 2016. XGBoost: A Scalable Tree Boosting System. Cornell University. 

- Chen, J., 2025. Improving Tropical Forest Biomass Predictions with Multi-Output Deep Learning Models for Above-and Belowground Estimates. Informatica 49 (37). Choudhury, A., 2024. Drought trend and its association with land surface temperature (LST) over homogeneous drought regions of India (2001–2019). Discov. Water 4 (1). https://doi.org/10.1007/s43832-024-00115-8. 

- de Andrade, J.M., Ribeiro Neto, A., Bezerra, U.A., Moraes, A.C.C., Montenegro, S.M.G.L., 2022. A comprehensive assessment of precipitation products: Temporal and spatial analyses over terrestrial biomes in Northeastern Brazil. Remote Sens. Appl. Soc. Environ. 28 (June). https://doi.org/10.1016/j.rsase.2022.100842. 

- Faiz, M.A., Baig, F., Muneer, S., Zhou, Z., Naz, F., 2025. Response of vegetation resilience to drought across river basins on a global scale. Int. J. Digit. Earth 18 (1), 2528661. 

- Gocic, M., Trajkovic, S., 2013. Analysis of changes in meteorological variables using Mann-Kendall and Sen’s slope estimator statistical tests in Serbia. Glob. Planet. Change 100, 172–182. https://doi.org/10.1016/j.gloplacha.2012.10.014. 

- Gudmundsson, L., Bremnes, J.B., Haugen, J.E., Engen-Skaugen, T., 2012. Technical Note: Downscaling RCM precipitation to the station scale using statistical transformations – a comparison of methods. Hydrol. Earth Syst. Sci. 16 (9), 3383–3390. https://doi.org/10.5194/hess-16-3383-2012. 

- Gueymard, C.A., 2014. A review of validation methodologies and statistical performance indicators for modeled solar radiation data: Towards a better bankability of solar projects. Renew. Sustain. Energy Rev. 39, 1024–1034. 

Hargreaves, G.H., Samani, Z.A., 1985. Reference crop evapotranspiration from temperature. Appl. eng. agric. 1 (2), 96–99. 

- Hashim, B.M., Alnaemi, A.N.A., Sultan, M.A., Alraheem, E.A., Abduljabbar, S.A., Halder, B., Shahid, S., Yaseen, Z.M., 2025. Impact of climate change on land use and relationship with land surface temperature: representative case study in Iraq. Acta Geophys. https://doi.org/10.1007/s11600-024-01514-0. 

- Li, M., Yao, Y., Feng, Z., Ou, M., 2025. Hydrological drought prediction and its influencing features analysis based on a machine learning model. Nat. Hazards Earth Syst. Sci. 25 (11), 4299–4316. 

- Liu, Xuebang, Yu, S., Yang, Z., Dong, J., Peng, J., 2024. The first global multi-timescale daily SPEI dataset from 1982 to 2021. Sci. Data 11 (1), 1–11. https://doi.org/ 10.1038/s41597-024-03047-z. 

- Liu, Xianfeng, Zhu, X., Zhang, Q., Yang, T., Pan, Y., Sun, P., 2020. A remote sensing and artificial neural network-based integrated agricultural drought index: Index development and applications. CATENA 186 (December 2019), 104394. https://doi.org/10.1016/j.catena.2019.104394. 

- Malik, A., Kumar, A., Kim, S., Kashani, M.H., Karimi, V., Sharafati, A., Ghorbani, M.A., Al-Ansari, N., Salih, S.Q., Yaseen, Z.M., Chau, K.W., 2020. Modeling monthly pan evaporation process over the Indian central Himalayas: Application of multiple learning artificial intelligence model. Eng. Appl. Comput. Fluid Mech. 14 (1), 323–338. 

- Mardian, J., Champagne, C., Bonsal, B., Berg, A., 2023. A Machine Learning Framework for Predicting and Understanding the Canadian Drought Monitor. Water Resour. Res. 59 (8), 1–23. https://doi.org/10.1029/2022WR033847. 

- Mohammadi, B., Abdallah, M., Oucheikh, R., Katipoglu, O.M., Cheraghalizadeh, M., 2025. Enhancing streamflow drought prediction: integrating wavelet ˘ decomposition with deep learning and quantile regression neural network models. Earth Sci. Inform. 18 (2), 232. https://doi.org/10.1007/s12145-025-01736-w. 

- Mokhtar, A., Jalali, M., He, H., Al-Ansari, N., Elbeltagi, A., Alsafadi, K., Rodrigo-Comino, J., 2021. Estimation of SPEI Meteorological Drought Using Machine Learning Algorithms. IEEE Access 9, 65503–65523. https://doi.org/10.1109/ACCESS.2021.3074305. 

- Newman, A.J., Kalb, C., Chakraborty, T.C., Fitch, A., Darrow, L.A., Warren, J.L., Strickland, M.J., Holmes, H.A., Monaghan, A.J., Chang, H.H., 2024. The Highresolution Urban Meteorology for Impacts Dataset (HUMID) daily for the Conterminous United States. Sci. Data 11 (1), 1–16. https://doi.org/10.1038/s41597024-04086-2. 

21 

_K. Qaraghuli et al.                                                                                                                                                                                                     Journal of Hydrology: Regional Studies 64 (2026) 103211_ 

- Oz, F.Y., ¨ Ozelkan, E., Tatlı, H., 2024. Comparative analysis of SPI, SPEI, and RDI ındices for assessing spatio-temporal variation of drought in Türkiye. Earth Sci. ¨ Inform. https://doi.org/10.1007/s12145-024-01401-8. 

- Peng, H., Long, F., Ding, C., 2005. Feature selection based on mutual information criteria of max-dependency, max-relevance, and min-redundancy. IEEE Trans. pattern anal. mach. intell. 27 (8), 1226–1238. 

- Poudel, B., Dahal, D., Banjara, M., Kalra, A., 2024. Assessing meteorological drought patterns and forecasting accuracy with spi and spei using machine learning models. Forecasting 6 (4), 1026–1044. 

- Prodhan, F.A., Zhang, J., Hasan, S.S., Pangali Sharma, T.P., Mohana, H.P., 2022. A review of machine learning methods for drought hazard monitoring and forecasting: Current research trends, challenges, and future research directions. Environ. Model. Softw. 149 (9), 105327. https://doi.org/10.1016/j. envsoft.2022.105327. 

- Qaraghuli, K., Murshed, M.F., M. Said, M.A., Mokhtar, A., Rousta, I., 2024. Univariate and multivariate imputation methods evaluation for reconstructing climate time series data: A case study of Mosul station-Iraq. J. Agrometeorol. 26 (3), 318–323. https://doi.org/10.54386/jam.v26i3.2657. 

- Rahman, G., Jung, M., Kim, T., Kwon, H., 2025. Drought impact, vulnerability, risk assessment, management and mitigation under climate change: A comprehensive review. 29(November 2024). 

- Sa’adi, Z., Yusop, Z., Alias, N.E., Chow, M.F., Muhammad, M.K.I., Ramli, M.W.A., Iqbal, Z., Shiru, M.S., Rohmat, F.I.W., Mohamad, N.A., Ahmad, M.F., 2023. Evaluating Imputation Methods for rainfall data under high variability in Johor River Basin, Malaysia. Appl. Comput. Geosci. 20 (July), 100145. https://doi.org/ 10.1016/j.acags.2023.100145. 

- Salman, S.A., Shahid, S., Ismail, T., Ahmed, K., Chung, E.S., Wang, X.J., 2019. Characteristics of Annual and Seasonal Trends of Rainfall and Temperature in Iraq. AsiaPac. J. Atmos. Sci. 55 (3), 429–438. https://doi.org/10.1007/s13143-018-0073-4. 

- Shapley, L.S., 1953. 17. A Value for n-Person Games. In: Kuhn, H.W., Tucker, A.W. (Eds.), Contributions to the Theory of Games (AM-28), Volume II. Princeton University Press, pp. 307–318. https://doi.org/10.1515/9781400881970-018. 

- Solaimani, K., Ahmadi, S.B., 2024. Evaluation of TerraClimate gridded data in investigating the changes of reference evapotranspiration in different climates of Iran. J. Hydrol. Reg. Stud. 52, 101678. https://doi.org/10.1016/j.ejrh.2024.101678. 

- Thai-Nghe, N., 2024. Intelligent Systems and Data Science: Third International Conference, ISDS 2025, Can Tho City, Vietnam, October 18-19, 2025, Proceedings, Part II (Vol. 2191). Springer Nature. 

- UN, 2023. Joint statement FAO and WFP joint call on World Food Day 2023 to Tackle Climate Change, Water Scarcity, and Food Insecurity in Iraq. October.. 

- Xu, Lei, Chen, N., Yang, C., Zhang, C., Yu, H., 2021. A parametric multivariate drought index for drought monitoring and assessment under climate change. Agric. For. Meteorol. 310 (September), 108657. https://doi.org/10.1016/j.agrformet.2021.108657. 

- Xu, Lichang, Ning, S., Xu, X., Wang, S., Chen, L., Long, R., Zhang, S., Zhou, Y., Zhang, M., Thapa, B.R., 2024. Comparative analysis of machine learning models and explainable AI for agriculture drought prediction: A case study of the Ta-pieh mountains. Agric. Water Manag. 306 (September), 109176. https://doi.org/ 10.1016/j.agwat.2024.109176. 

- Xue, C., Ghirardelli, A., Chen, J., Tarolli, P., 2024. Investigating agricultural drought in Northern Italy through explainable machine learning: insights from the 2022 drought. Comput. Electron. Agric. 227 (P1), 109572. https://doi.org/10.1016/j.compag.2024.109572. 

- Yahya, B.M., Seker, D.Z., 2019. Designing weather forecasting model using computational intelligence tools. Appl. Artif. Intell. 33 (2), 137–151. https://doi.org/ 10.1080/08839514.2018.1530858. 

- Yang, W., Doulabian, S., Shadmehri Toosi, A., Alaghmand, S., 2023. Unravelling the drought variance using machine learning methods in six capital cities of Australia. Atmosphere 15 (1), 43. https://doi.org/10.3390/atmos15010043. 

- Zamani, H., Pakdaman, Z., Shakari, M., Bazrafshan, O., Jamshidi, S., 2025. Enhancing drought monitoring with a multivariate hydrometeorological index and machine learning-based prediction in the south of Iran. Environ. Sci. Pollut. Res. 32 (9), 5605–5627. 

- Zhang, Q., Shi, R., Singh, V.P., Xu, C.Y., Yu, H., Fan, K., Wu, Z., 2022. Droughts across China: Drought factors, prediction and impacts. Sci. total environ. 803, 150018. 

22 

