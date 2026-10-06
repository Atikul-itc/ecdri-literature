Agricultural Water Management 308 (2025) 109303 



Contents lists available at ScienceDirect 

# Agricultural Water Management 

journal homepage: www.elsevier.com/locate/agwat 



A novel agricultural drought index based on multi-source remote sensing data and interpretable machine learning 



Hao Chen<sup>a,b,1</sup> , Ni Yang<sup>c,d,1</sup> , Xuanhua Song<sup>a,b</sup> , Chunhua Lu<sup>a,b</sup> , Menglan Lu<sup>a,b</sup> , Tan Chen<sup>e</sup> , Shulin Deng<sup>a,b,*</sup> 

a _Key Laboratory of Environment Change and Resources Use in Beibu Gulf (Nanning Normal University), Ministry of Education, Nanning 530001, China_ b _School of Geography and Planning, Nanning Normal University, Nanning 530001, China_ 

c _School of Geography and Information Engineering, China University of Geosciences, Wuhan 430074, China_ 

d _School of Management Science and Engineering, Guangxi University of Finance and Economics, Nanning 530003, China_ 

e _Key Laboratory of Watershed Geographic Sciences, Nanjing Institute of Geography and Limnology, Chinese Academy of Sciences, Nanjing 210008, China_ 

A R T I C L E I N F O 

### A B S T R A C T 

Handling Editor: J.E. Fern´andez 

_Keywords:_ Interpretable machine learning drought index (IMLDI) Agricultural drought monitoring Solar-induced chlorophyll fluorescence The eastern parts of China 

Drought is a frequent, destructive, and complex natural hazard, and seriously threatens eco-environment, socioeconomy, and the health of human. Previous studies suggested that integrated multi-source remote sensing drought indices have the potential to comprehensively monitor drought conditions, however most existing integrated drought indices still have several limitations. Here, we used solar-induced chlorophyll fluorescence, water balance, soil moisture, and land surface temperature to develop a new integrated remote sensing drought index, namely interpretable machine learning drought index (IMLDI), based on the Bayesian optimized treebased Light Gradient Boosting Machine and SHapley Additive exPlainations. The different land cover types were further considered, and the categories of drought severity were objectively determined by the iterative optimized method. The drought monitoring performance of IMLDI was validated in the eastern parts of China, and three integrated drought indies composited by PCA, multiple linear regression, and gradient boosting method were also included for comparison. The results show that IMLDI has a higher spatial and temporal consistency with standardized precipitation evapotranspiration index, can better reflect the real-world observed drought-affected cropland areas and gross primary production, and can also well describe the evolutions of 2009/2010 and 2019 drought events in the eastern parts of China, indicating higher drought monitoring performance of IMLDI. Besides, IMLDI-based agricultural drought risk analysis shows that the Huang-Hai Region and Yunnan, Guizhou, and Guangxi Provinces have a high risk to suffer from severe agricultural droughts. Overall, IMLDI has a great potential to use as a new integrated remote sensing drought index for agricultural drought monitoring. 

## **1. Introduction** 

Drought is a frequent, destructive, long-lasting, and complex extreme weather event (Liu et al., 2023a; Pradhan et al., 2017; Zhang et al., 2017; Zhang and Yuan, 2020). Drought is generally classified into meteorological drought, agricultural drought, hydrological drought, and socioeconomic drought (Dracup et al., 1980; Wilhite and Glantz, 1985). Meteorological drought is a specified period with an imbalance between precipitation and evaporation. Agricultural drought occurs when soil 

moisture deficits below the levels necessary for sustaining plant growth, and usually leads to substantial crop yield reductions and severe economic repercussions (Jiao et al., 2019; Mishra and Singh, 2010). Hydrological drought occurs when rivers and other water bodies fall below their normal levels or the water level of underground aquifers. Socioeconomic drought refers to an insufficient water supply to meet the economic demands. Under background of global warming, drought became much more frequent and intensified in most parts of the world during recent decades, which poses a serious threat to the health of 

* Corresponding author at: Key Laboratory of Environment Change and Resources Use in Beibu Gulf (Nanning Normal University), Ministry of Education, Nanning 530001, China. 

_E-mail address:_ dengshulin@nnnu.edu.cn (S. Deng). 

> 1 Hao Chen and Ni Yang contributed equally to this work and are co-first authors. 

https://doi.org/10.1016/j.agwat.2025.109303 

Received 1 December 2024; Received in revised form 6 January 2025; Accepted 9 January 2025 

Available online 16 January 2025 

0378-3774/© 2025 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY-NC license ( http://creativecommons.org/licenses/bync/4.0/ ). 

_Agricultural Water Management 308 (2025) 109303_ 

_H. Chen et al.                                                                                                                                                                                                                                    Agricultural Water Management_ 



**Fig. 1.** The technical flowchart. 

human and eco-environment, and causes direct economic losses of billions of dollars every year (AghaKouchak et al., 2015; Gao et al., 2019; Naumann et al., 2021; Verhoeven et al., 2022). For example, according to the “China Flood and Drought Disaster Bulletin”, China experienced a severe drought disaster in 2019, which covers 18.23 million ha agricultural area and causes a shortage of drinking water for 6.92 million people and 3.68 million livestock. Therefore, it is important to develop effective drought indices to accurately monitor drought conditions and understand reginal drought risks (Rhee and Im, 2017; Samantaray et al., 2022). 

Numerous drought indices have been developed in recent years, such as Palmer Drought Severity Index (PDSI) (Palmer, 1965), Standardized Precipitation Index (SPI) (McKee et al., 1993), and Standardized Precipitation Evapotranspiration Index (SPEI) (Vicente-Serrano et al., 2010). As an improved version of SPI, SPEI is defined by the difference between evapotranspiration and precipitation (Zhang and Jia, 2013; Zhang et al., 2018b). SPEI is a multi-scalar drought index for quantifying the onset, duration, and magnitude of drought, and is better than PDSI in monitoring short-term droughts (Hao et al., 2015; Hao and Singh, 2015). These traditional drought indices are generally calculated based on ground-based observed meteorological variables. Ground-based observations can provide reliable observed data, but cannot capture spatial and temporal distributions of drought due to the sparse and uneven distributions (Beck et al., 2017; Jiao et al., 2019; Sun et al., 2017; West et al., 2019). 

Remote sensing can obtain spatiotemporal continuous data of long time series in near real time and provides a new way to monitor drought. During recent years, many remote sensing drought indices, such as Normalized Difference Vegetation Index (NDVI) (Rouse et al., 1974), 

Enhanced Vegetation Index (EVI) (Huete et al., 2002), Vegetation Condition Index (VCI) (Kogan, 1995a), Temperature Condition Index (TCI) (Kogan, 1995b), Normalized Difference Water Index (NDWI) (Gao, 1996), Precipitation Condition Index (PCI) (Du et al., 2013), Soil Moisture Condition Index (SMCI) (Zhang and Jia, 2013), and Vegetation Drought Index (VDI) (Sun et al., 2013), have been developed to monitor regional or global drought conditions (Lu et al., 2016; Rhee et al., 2010; Wang et al., 2012; Wu et al., 2013). However, these single hydrometeorological variable-based drought indices cannot fully and reliably capture drought conditions because of the complexity processes and diverse impacts of drought (Guo et al., 2019; Tian et al., 2018). 

As more drought-related variables are successfully retrieved from remote sensing measurements, many integrated multi-sources remote sensing drought indices have also been developed to better comprehensively assess and monitor drought conditions (Li et al., 2020a, 2020b). The common used and representative integrated remote sensing drought indices are the Vegetation Health Index (VHI) (Kogan et al., 2004), scaled drought condition index (SDCI) (Rhee et al., 2010), Microwave Integrated Drought Index (MIDI) (Zhang and Jia, 2013), Synthesized Drought Index (SDI) (Du et al., 2013), Optimized Vegetation Drought Index (OVDI) (Hao and Singh, 2015), Process-based Accumulated Drought Index (PADI) (Zhang Xiang et al., 2017), Integrated Remote Sensing Drought Monitoring Index (IRSDI) (Sun et al., 2017), Geographically Independent Integrated Drought Index (GIIDI) (Jiao et al., 2019), Temperature Vegetation Precipitation Dryness Index (TVPDI) (Wei et al., 2020), Temperature Fluorescence Drought Index (TFDI) (Zhang et al., 2020), Fluorescence Healthy Vegetation Index (SHI) (Liu et al., 2021a), Bivariate Soil Moisture and Evapotranspiration Index (BSMEI) (Wu et al., 2021), drought index integrated by gradient 

2 

_Agricultural Water Management 308 (2025) 109303_ 

_H. Chen et al.                                                                                                                                                                                                                                    Agricultural Water Management_ 



**Fig. 2.** Spatial distribution of land cover types in the eastern parts of China. 

boosting method (GBMDI) (Zhang et al., 2022), Temperature-vegetation-soil-moisture-precipitation-dryness Index (TVMPDI) (Wang et al., 2022), temperature-sun-induced chlorophyll fluorescence-water balance dryness index (TSWDI) (Liu et al., 2023b), Geographically Integrated Dryness Index (GIDI) (Wei et al., 2023), and Combined Drought Index (CDI) (Bas¸akın et al., 2024). However, these integrated drought indices still have several limitations when applied to drought monitoring. 

These integrated remote sensing drought indices were generally developed based on NDVI, precipitation, and other variables. One limitation is that NDVI is easy to be affected by the soil background and saturated especially in high vegetation coverage areas, and precipitation cannot fully assess the wet and dry conditions of the climate (Birky, 2001; Hmimina et al., 2013; Liu et al., 2021a, 2021b; Sui et al., 2013). The solar-induced chlorophyll fluorescence (SIF) is directly related to the internal photosynthesis mechanism of plants and is less affected by soil background and clouds, and thus can directly reflect the dynamics of actual plant photochemical production (Cui et al., 2017; Guanter et al., 2014; Lee et al., 2013). Many previous studies suggested that SIF is much more sensitive to drought stress than NDVI (Daumard et al., 2010; Liu and Yue, 2018; Yoshida et al., 2015; Zhang et al., 2019a, 2019b). The water balance (WB) is constructed from surface runoff, precipitation, and evapotranspiration, which provides a more accurate reflection of climatic wet and dry conditions than precipitation (Liu et al., 2023b; Sheffield et al., 2009). 

Another issue is that many previous drought indices were developed without considering different land cover types (Malczewski and Liu, 2014; Tang et al., 2018). However, drought conditions are significantly influenced by land cover types because different vegetation species have different physiological mechanisms and adaptation processes to drought stresses (Abbas et al., 2014; Hua et al., 2017; Lamchin et al., 2018; Li et al., 2018a, 2018b). Additionally, drought severity categories of most previous drought indices were arbitrarily classified, which may overestimation or underestimation of the actual drought conditions (Guo et al., 2019; Hao et al., 2015). 

There are many different methods of generating integrated remote sensing drought indices, such as the linear combination, principal 

components analysis (PCA), joint distribution methods, and machine learning models (Xu et al., 2023). Among these methods, the linear combination method is the simplest and most easily applied method, but determining the weights of different variables objectively is very difficult (Cai et al., 2017; Hao and Singh, 2015). Machine learning models, such as tree-based Light Gradient Boosting Machine (LGBM), have been proved to be powerful and flexible methods in many linear and nonlinear regression applications, and provide a new method to develop integrated drought indices (Feng et al., 2019; Park et al., 2016; Rhee and Im, 2017). However, machine learning models have a complex structure and many parameters, which leads to high difficulty in parameter tuning and overfitting (Alibrahim and Ludwig, 2021; Feurer and Hutter, 2019). Moreover, machine learning models are regarded as black-box models, which makes it difficult to understand why the models make a particular regression or prediction, thus limiting the model trustworthiness and scope of application (Li, 2022; Van den Broeck et al., 2022). 

To address these limitations, this study aims to propose a new interpretable machine learning drought index (IMLDI) based on the following considerations: (i) SIF, WB, soil moisture (SM), and land surface temperature (LST) variables are used, (ii) drought index is developed for different land cover types, (iii) drought index is composited by the Bayesian optimized LGBM model and interpreted with SHapley Additive explanations (SHAP), and (iv) drought severity categories are objectively classified by iterative optimization method. The drought monitoring performance of IMLDI was evaluated in the eastern parts of China, where observed and statistical data can serve as a reference for validation. 

## **2. Material and methods** 

The technical flowchart is shown in Fig. 1, including data collection, drought index development, and verification. 

## _2.1. Study area_ 

The eastern parts of China (Fig. 2) cover 37.12 % of China’s land area (22<sup>◦</sup> - 42<sup>◦</sup> N, 97<sup>◦</sup> - 135<sup>◦</sup> E), and the main land cover types are forest, 

3 

_Agricultural Water Management 308 (2025) 109303_ 

_H. Chen et al._ 

scrubland, grassland, sparse vegetation, rainfed cropland, irrigated cropland, and non-vegetated areas. It locates in East Asian Monsoon region, where climate is characterized by pronounced shift in wet and dry seasons. The study area contains the marginal tropical humid (subregion 1), northern subtropical humid (sub-region 2), warm temperate semi-humid (sub-region 3), and plateau temperate semi-arid (sub-region 4) climatic zones. The eastern parts of China are low in east and high in west, and mainly include the Yangtze River, Pearl River, Yellow River, Huai River, Hai River, Southwest River, and Southeast River basins. In recent decades, the eastern parts of China suffered from extreme drought events frequently (Chen et al., 2023; Shi et al., 2020; Yu and Zhai, 2020). 

## _2.2. Data_ 

## _2.2.1. Observed meteorological data_ 

The CN05.1 gridded monthly precipitation and temperature datasets with a spatial resolution of 0.25<sup>◦</sup> × 0.25<sup>◦</sup> during 2001–2020 were used, which is interpolated from in situ observed precipitation and temperature at approximately 2400 meteorological stations in China using the anomaly app-roach method. Strict quality control has also been implemented before these datasets release. 

## _2.2.2. Remote sensing data_ 

In this work, the monthly global OCO-2-based Sun-induced Chlorophyll Fluorescence (GOSIF) (Li and Xiao, 2019a), GOSIF gross primary production (GPP), Moderate Resolution Imaging Spectroradiometer products (MODIS), and the Climate Hazards Group InfraRed Precipitation with Station (CHIRPS) datasets derived from remote sensing measurements, and the monthly Global Land Data Assimilation System Version 2 (GLDAS-2.1) Noah model simulation products were used. Table S1 provides detailed information about these remote sensing and assimilation datasets. All datasets are collected over the period from 2001 to 2020. 

GOSIF was developed based on discrete OCO-2 SIF soundings, MODIS remote sensing data, and MERRA-2 meteorological reanalysis data using the Cubist model (Li and Xiao, 2019a), which has good spatial resolution, continuous global coverage, and long records (Qiu et al., 2022; Shekhar et al., 2022). GOSIF GPP dataset was developed by using the linear relationships between SIF and GPP (Li and Xiao, 2019b). MODIS NDVI (MOD13C1) and LST (MOD11A2) with a spatial resolution of 0.05<sup>◦</sup> were obtained from National Aeronautics and Space Administration’s Earth Observing System Data and Information System. CHIRPS is a quasi-global (50<sup>◦</sup> S-50<sup>◦</sup> N) long-term precipitation dataset, which is developed by the United States Geological Survey and Climate Hazards Group (Funk et al., 2015a, 2015b, 2014). The GLDAS-2.1 products were derived from station-based and satellite-based observations using data assimilation algorithms. Previous studies suggested that spatiotemporal continuous SM, evapotranspiration (ET), and runoff (SR) from GLDAS can well capture the spatial and temporal variations of corresponding observed hydrometeorological variable (Jasinski et al., 2019; Kumar et al., 2019; Wei et al., 2021). Therefore, monthly 0–10 cm depth SM, ET, and SR from GLDAS-V2.1 Noah Model L4 were used. 

## _2.2.3. The statistical drought-affected cropland areas and Land cover data_ 

The statistical drought-affected cropland areas data during 2001–2020 was sourced from the crop databank of the Chinese Crop Farming Information center at https://data.stats.gov.cn/. These statistical records were used to validate the drought monitoring performance of the newly developed drought index. 

The land cover types data was obtained from the European Space Agency for the Climate Change Initiative (ESA CCI) (Li et al., 2018c). This land cover types data consists of 37 land cover types with a resolution of 300 m, which has a higher overall accuracy in China than many other land cover types products (Gessner et al., 2015; Hartley et al., 2017; Li et al., 2018c; Yang et al., 2017). The original ESA CCI land cover types were re-grouped into forest, shrubland, grassland, sparse 

**Table 1** 

Descriptions of scaled remote sensing drought indices. 

|Drought indices<br>Formula<br>Ref.|
|---|
|VCI<br>_NDVIi_−_NDVI_min<br>(Kogan, 1995a)|
|_NDVI_max −_NDVI_min|
|FCI<br>_SIFi_−_SIF_min<br>(Zhang et al., 2021)|
|_SIF_max −_SIF_min|
|PCI<br>_Pi_ −_P_min<br>(Zhang and Jia, 2013)|
|_P_max −_P_min<br>i|
|WB<br>WB=P-Q-E<br>(Sheffield et al., 2009)|
|i<br>WBCI<br>_WBi_ −_WB_min<br>(Liu et al., 2023b)|
|vegetation, rainfed cropland, and irrigated cropland in the eastern parts<br>of China. Note that all grid datasets used were resampled to a 0.5<sup>◦</sup>grid.<br>_2.3. Methods_<br>_WB_max −_WB_min<br>SMCI<br>_SMi_ −_SM_min<br>_SM_max −_SM_min<br>(Zhang and Jia, 2013)<br>TCI<br>_LST_max −_LSTi_<br>_LST_max−_LST_min<br>(Kogan, 1995b)|
|VCI, SIF condition index (FCI), PCI, water balance condition index|
|(WBCI), SMCI, and TCI were taken as input variables to develop multiple<br>remote sensing drought indices. Integrated remote sensing drought|
|indices composited by PCA (PSDI), multiple linear regression (MRSDI),<br>and gradient boosting method (GBMDI) were used to validate the<br>drought monitoring performance of IMLDI. Note that PSDI, MRSDI,<br>GBMDI, and IMLDI were developed for each month in a year.|



vegetation, rainfed cropland, and irrigated cropland in the eastern parts of China. Note that all grid datasets used were resampled to a 0.5<sup>◦</sup> grid. 

## _2.3.1. Standardized precipitation evapotranspiration index_ 

SPEI is calculated from the difference between precipitation and temperature, which is widely used to assess drought conditions (Vicente-Serrano et al., 2010). It is often used to validate other drought indices (Park et al., 2017; Um et al., 2018; Zhang et al., 2013). SPEI preserves multiple time scales to indicate different types of droughts, such as meteorological and agricultural droughts. Previous studies suggested that the 3-month SPEI could better monitor the evolutions of agricultural drought in China (Mishra and Singh, 2010; Zambrano et al., 2016, 2017), and thus 3-month SPEI was calculated from observed meteorological data in this work. 

## _2.3.2. Scaled remote sensing drought indices_ 

NDVI, SIF, precipitation (P), WB, SM, and LST were used to calculate scaled VCI, FCI, PCI, WBCI, SMCI, and TCI, respectively. The calculation formulas are shown in Table 1, wherein ∗ _i_ , ∗max, and ∗min are the pixel values, maximum values, and minimum values of variable *, respectively, in the same month during 2001–2020. The values of the scaled remote sensing drought indices range from 0 to 1. A scale value of 0 represents the driest conditions, and 1 represents the wettest conditions (Wei et al., 2020). 

## _2.3.3. Integrated remote sensing drought indices for comparison_ 

PCA is a linear transformation reducing redundancy by translating and/or rotating the axes of the original feature space, so that drought information can be represented without correlation in a new component space (Du et al., 2013; Lasaponara, 2006; Zhang et al., 2022). PCA was used to composite monthly VCI, PCI, SMCI, and TCI remote sensing variables, and the first principal component of the PCA output for each month in a year is taken as PSDI (Liu et al., 2019). 

MRSDI was developed by combining independent VCI, PCI, and TCI remote sensing variables, and the coefficients for each month in a year (Table S2) were determined by multiple linear regression model (Gr´egoire, 2014; Noi et al., 2017). In this case, SMCI is the major mechanism behind agricultural drought, which was used as the dependent variable (Sun et al., 2017; Zhang et al., 2018a, 2022). 

Gradient boosting machine (GBM) can significantly improve 

4 

_Agricultural Water Management 308 (2025) 109303_ 

_H. Chen et al.                                                                                                                                                                                                                                    Agricultural Water Management_ 

**Table 2** 

Drought severity categories of SPEI, PSDI, MRSDI, GBMDI, IMLDI. 

|Drought<br>categories|SPEI|PSDI|MRSDI|GBMDI|IMLDI|
|---|---|---|---|---|---|
|Extreme<br>drought|≤−2|≤0.12|≤0.4|≤0.10|≤0.14|
|Severe drought|−2 ~|0.12 ~|0.40 ~|0.10 ~|0.14 ~|
||−1.50|0.24|0.46|0.20|0.24|
|Moderate|−1.50 ~|0.24 ~|0.46 ~|0.20 ~|0.24 ~|
|drought|−1|0.36|0.52|0.30|0.34|
|Mild drought|−1 ~ 0|0.36 ~|0.52 ~|0.30 ~|0.34 ~|
|||0.48|0.58|0.40|0.52|
|No drought|≥0|≥0.48|≥0.58|≥0.40|≥0.52|



prediction accuracy, optimize computational efficiency, and effectively avoid overfitting (De’Ath, 2007; Zhang and Haghani, 2015). GBMDI is integrated remote sensing drought index based on the GBM (Zhang et al., 2022). Monthly VCI, PCI, SMCI, and TCI as the input variables, 

and monthly SPEI was taken as the reference data. The scaled relative importance of these input variables for each month in a year (shown in Table S3) was used as weights to develop GBMDI. Drought severity categories of PSDI, MRSDI, and GBMDI are given in Table 2. 

_2.3.4. Light gradient boosting machine, Bayesian hyperparameter optimization, and SHapley Additive exPlanation_ 

LGBM is an ensemble learning model based on boosting strategy, and is an efficient implementation of gradient boosting decision tree (Ke et al., 2017). It incrementally improves the predictive accuracy of the entire model by successively adding new decision trees capable of predicting the residuals of previous models and using the negative gradient of the loss function as a guide. Compared with its counterpart GBM and eXtreme Gradient Boosting (XGBoost), LGBM can achieve higher training efficiency and lower memory footprint while maintaining high prediction accuracy (Bent´ejac et al., 2021; Chen and Guestrin, 2016; Szczepanek, 2022). 

In machine learning models, the number (complexity) of 



**Fig. 3.** Relative contributions (%) of FCI, WBCI, SMCI, and TCI to SPEI for each month in six different land cover types. 

5 

_Agricultural Water Management 308 (2025) 109303_ 

_H. Chen et al._ 



**Fig. 4.** The SHAP beeswarm plots of the input remote sensing variables contributions to SPEI in different land cover types during April. 

hyperparameters is often large (high), and traditional grid search and stochastic search methods are difficult to find the optimal solutions in a reasonable time (Alibrahim and Ludwig, 2021; Feurer and Hutter, 2019). The Bayesian hyperparameter optimization is an efficient, global, and adaptive optimization method, and can find a near-optimal combination of hyperparameters in a smaller number of iterations (Snoek et al., 2012; Wu et al., 2019). Previous studies suggested that the Bayesian optimized LGBM model can form a more powerful machine learning framework (Zhou et al., 2024). 

As a machine learning model interpretation tool based on a game theory approach, SHAP provides global and local interpretability for the model by calculating the value of each feature’s contribution to the model regression or prediction results (Mokhtari et al., 2019). The SHAP value can be used as a measure of the importance of features, which helps users to understand which features have the greatest impact on the model’s regression or prediction results (Yang et al., 2021). 

## _2.3.5. Iterative optimized method_ 

To objectively classify drought severity categories, the iterative optimized method (Um et al., 2018) was adopted to find more meaningful breakpoints of IMLDI by minimizing the difference in the sum of the drought frequency and drought area between SPEI and IMLDI. IMLDI was categorized into four drought categories to better compare with other previous drought indices. For each category, drought frequency error is calculated as the total sum of squares of the relative frequency errors in each pixel, and drought area error is calculated as the total sum of squares of the area errors for each month. The total error is summarized from 8 cases, including the four drought categories for the two types of errors (4 categories × 2 errors). The optimized thresholds were chosen as the minimum total error by iterating the categorical threshold values with a step of 0.01. 

## _2.3.6. Statistical methods_ 

The Pearson correlation analysis was used to quantify the correlations in validation of IMLDI. When the p-value is less than 0.05 (0.01), the correlation is significant at 95 % (99 %) confident level (Ren et al., 2024). 

The theory of runs (Yevjevich, 1967) was used to express the duration, severity, and peak of agricultural drought events in IMLDI-based agricultural drought risk analysis. The threshold value of the IMLDI was set at 0.52 to identify the beginning and end of an agricultural drought event. 

## **3. Results** 

## _3.1. Development of interpretable machine learning drought index (IMLDI)_ 

There are five steps to develop IMLDI. (1) FCI, WBCI, SMCI, and TCI were selected as the input remote sensing variables, and SPEI was taken as the reference data. (2) IMLDI was developed for each land cover type. (3) LGBM optimized by Bayesian hyperparameter optimization was used to construct IMLDI, and the importance of input remote sensing variables was interpreted by SHAP. (4) The scaled mean SHAP values of input remote sensing variables were taken as weights to composite IMLDI. (5) Drought severity categories of IMLDI were objectively classified by the iterative optimized method, and are shown in Table 2. 

The scaled mean SHAP values (or weights in another word) of input remote sensing variables in the development of IMLDI are given in Fig. 3. For July to February next year, SMCI is a dominant contributor to drought in most land cover types. This may be because the reduction in soil moisture cannot provide enough water for vegetation and finally triggers agricultural drought (Li et al., 2020b; Zhang and Jia, 2013). However, WBCI dominates drought in most land cover types from March to June. The relative contribution of TCI to SPEI exceeds 40 % in grassland from January to April, which is much greater than that of SMCI, WBCI, and FCI. The contributions of FCI to drought are relatively low compared to other input variables, which agrees with the results from Zhang et al. (2022). However, FCI contributes to a relative higher extent in grassland, sparse vegetation, and shrubland compared to other land cover types. Previous studies also found similar results when exploring the correlations of VCI and SPEI in different land cover types (Vicente-Serrano, 2007). 

Moreover, April and August were taken as examples to show the 

6 

_Agricultural Water Management 308 (2025) 109303_ 

_H. Chen et al.                                                                                                                                                                                                                                    Agricultural Water Management_ 



**Fig. 5.** The SHAP beeswarm plots of the input remote sensing variables contributions to SPEI in different land cover types during August. 



**Fig. 6.** Spatial distribution of correlation coefficients between PSDI, MRSDI, GBMDI, IMLDI and SPEI during 2001–2020. 

7 

_Agricultural Water Management 308 (2025) 109303_ 

_H. Chen et al.                                                                                                                                                                                                                                    Agricultural Water Management_ 



**Fig. 7.** Correlation coefficients for all months between PSDI, MRSDI, GBMDI, and IMLDI and SPEI from January 2001 to December 2020. ** denotes significant correlation at 0.01 significance level. 

positive and negative contributions from each variable to drought in different land cover types (Figs. 4 and 5). A positive SHAP value suggests that the sample have a promote effect on SPEI, while a negative SHAP value means the opposite effect in the beeswarm plots. During April (Fig. 4), WBCI has the highest positive correlations with SPEI, followed by SMCI and TCI in forest, shrubland, sparse vegetation, rainfed cropland, and irrigated cropland. However, TCI is the most important contributors and has a positive contribution to SPEI in grassland. During August (Fig. 5), larger values of SMCI, WBCI, and TCI contribute to a bigger SPEI value in most land cover types, but TCI has a negative contribution to SPEI in shrubland and irrigated cropland. 

## _3.2. Validation of interpretable machine learning drought index (IMLDI)_ 

## _3.2.1. Comparisons of integrated remote sensing drought indices and SPEI_ 

To assess the drought monitoring performance of IMLDI, we used the Pearson correlation analysis (Cohen et al., 2009) to compare correlation coefficients between integrated remote sensing drought indices (PSDI, MRSDI, GBMDI, and IMLDI) and SPEI. The spatial distributions of correlation coefficients between each integrated remote sensing drought index and SPEI from 2001 to 2020 are shown in Fig. 6. Generally, PSDI, MRSDI, GBMDI and IMLDI are positively correlated with SPEI, and the correlation coefficients are significant at 0.01 level in almost the eastern parts of China. These results indicate that PSDI, MRSDI, GBMDI, and IMLDI can well capture the observed drought. However, IMLDI has higher correlation coefficients (higher than the 0.4) with SPEI than PSDI, MRSDI, and GBMDI in most parts, especially in Southeast China 

and Yunnan province. The spatial correlation coefficients between PSDI and MRSDI and SPEI are relatively low in most parts. This may be due to the fact that the PCA method omits some important information in the development of drought index (Greenacre et al., 2022; Hao et al., 2015; Kim et al., 2021), as well as the multiple linear regression model is based on the assumption of linearity and thus the model may not be fitted well when there are nonlinear relationships in input variables (Abdul Gafoor et al., 2022; Kim et al., 2020; Uyanık and Güler, 2013). 

Moreover, we analyze the monthly spatial correlations between PSDI, MRSDI, GBMDI, and IMLDI and SPEI from 2001 to 2020 (Fig. 7). The percentages of months with correlation coefficients higher than 0.4 (average correlation coefficients) between PSDI, MRSDI, GBMDI, and IMLDI and SPEI are 58.33 % (0.433), 50.00 % (0.372), 60.00 % (0.439), and 71.67 % (0.508), respectively, from January 2001 to December 2020. The correlation coefficients are also significant at 99 % confident level in almost all months. The correlations analysis results indicate that IMLDI can better capture drought conditions than PSDI, MRSDI, and GBMDI. 

## _3.2.2. Cross-validation with statistical drought-affected cropland areas and_ 

## _GPP_ 

The annual drought index-based drought-affected cropland areas were counted in each province, were further compared to the real-world observed drought-affected cropland areas. For each integrated remote sensing drought index, the grids of cropland in which moderate, severe, or extreme droughts occurs for more than two consecutive months in a year were identified as the annual drought index-based drought-affected 

8 

_Agricultural Water Management 308 (2025) 109303_ 

_H. Chen et al.                                                                                                                                                                                                                                    Agricultural Water Management_ 





**Fig. 8.** The scatter plots and correlations of annual real-world observed and drought index-based drought-affected cropland areas. The drought-affected cropland areas are scaled. 

cropland areas (Rivera and Penalba, 2014; Sun et al., 2017). It can be seen from Fig. 8 that the correlations between the scaled drought-affected cropland areas monitored by PSDI, MRSDI, GBMDI, and IMLDI and the scaled real-world observed drought-affected cropland areas are higher than 0.35, and significant at 99 % confident level. Compared to PSDI (0.41), MRSDI (0.35) and GBMDI (0.39) indices, the drought-affected cropland areas monitored by IMLDI (0.47) have a higher correlation coefficient with the real-world observed drought-affected cropland areas. 

The spatial correlations of integrated remote sensing drought indices and GPP are also compared (Fig. 9). PSDI and MRSDI have a positive correlation with GPP (p _<_ 0.01) in Guangxi province, Guizhou province, and the northern parts. GBDMI shows a positive correlation with GPP (p _<_ 0.01) only in Guangxi and Guizhou provinces. Compared with PSDI, MRSDI, and GBDMI, IMLDI is significantly positive correlated with GPP in much larger areas, which covers almost the entire study area. In terms of each province, GPP is significant correlated with IMLDI in most provinces. The number of provinces with significant correlation (the value of correlation coefficients) of IMLDI and GPP is larger (higher) than that of PSDI, MRSDI, and GBDMI and GPP. To further validate the capabilities of reflecting GPP of crops, we analyze the spatial correlations of integrated remote sensing drought indices and GPP with a special focus on agricultural land (Supplementary Fig. S1). We found that the correlations of IMLDI and GPP are significant in almost all agricultural land, and the correlation coefficients are also higher than other three drought indices in most agricultural land. 

_3.2.3. Two typical drought events monitoring using integrated remote sensing drought indices_ 

Southwestern China suffered a severe drought from autumn 2009 to spring 2010. According to the survey of the Ministry of Civil Affairs, around 21 million people were short of drinking water, and economic losses reached nearly US$30-billion during this drought event (Lu et al., 2011; Yang et al., 2012; Zhang et al., 2012). In 2019, drought disasters occurred in 24 provinces in China, and the area of crops affected by drought reached 8777.83 thousand hectares (Ding and Gao, 2020; Yan et al., 2021). Particularly, serious drought occurred in Yunnan province and Huang-Huai-Hai Region during April to August 2019, which have caused great damage to local vegetation. Therefore, these two severe drought events were selected to further evaluate the performance of IMLDI in monitoring drought evolutions. 

We analyzed the spatial distributions of PSDI, MRSDI, GBMDI, and IMLDI during August 2009 to June 2010 (Figs. 10 and 11), and validated them by SPEI. Drought conditions indicated by SPEI were initially located in much eastern parts of China during August 2009 and drought center appeared in Southwest China in September 2009. After that, drought became more severity and affected more areas in Southwest China during October 2009, continued to April 2010, and ended in June 2010. The spatial distributions of PSDI, MRSDI, GBMDI, and IMLDI generally agree with SPEI in most parts during the stages of onset, progression, and end of 2009/2010 drought. However, MRSDI and GBMDI overestimate the spatial extent and severity of drought indicated by SPEI in August 2009 and October 2009. Drought affected areas observed by PSDI are relatively fragmented, especially in August 2009 and June 2010, which is inconsistent with regional spatial aggregation of drought. Moreover, PSDI, MRSDI, and GBMDI underestimate the 

9 

_Agricultural Water Management 308 (2025) 109303_ 

_H. Chen et al._ 



**Fig. 9.** Spatial distributions of correlation coefficients between PSDI, MRSDI, GBMDI, IMLDI and GPP. The stippling areas indicate that the correlations are significant at the 99 % confidence level. * and ** denote that the correlations are significant at 95 % and 99 % confidence levels, respectively. 

drought affected areas in Southwest China in April 2010. Overall, compared with PSDI, MRSDI, and GBMDI, IMLDI can better capture the evolutions of 2009/2010 drought. 

In 2019 (Fig. 12), drought centers indicated by SPEI are located in Yunnan province and Huang-Huai-Hai Region. PSDI, MRSDI, GBMDI and IMLDI can capture the onset, progression, and end of this drought event to a certain extent. However, MRSDI and GBMDI cannot capture drought conditions in July in Yunnan province. MRSDI (PSDI) overestimated (underestimated) the severity and affected areas of drought in Huang-Huai-Hai Region during May to July 2019, which may be explained by the fact that MRSDI or PSDI failed to fully integrate all the information from the input remote sensing variables (Zhang et al., 2022). The integrated remote sensing drought indices generally underestimate the severity of drought because agricultural drought are always less severe than meteorological drought in the same area during the 

same time periods (Degefu, 1987; Hao et al., 2015). In summary, drought conditions monitored by IMLDI are more consistent with the actual situations, and thus IMLDI is more suitable for regional drought monitoring. 

_3.3. IMLDI-based agricultural drought risk analysis in the eastern parts of China_ 

Spatial distributions of frequency, average duration, average severity, and average peak of agricultural drought during 2001–2020 are given in Fig. 13. Agricultural drought tends to occur frequently in East China, but the values of duration, severity, and peak of drought are relatively low. More than 25 agricultural drought events are detected in Huang-Hai Region and Yunnan province, and the duration, severity, and peak of drought are quite high. The values of frequency, duration, 

10 

_Agricultural Water Management 308 (2025) 109303_ 

_H. Chen et al.                                                                                                                                                                                                                                    Agricultural Water Management_ 





**Fig. 10.** Spatial and temporal evolutions of drought monitored by SPEI, PSDI, MRSDI, GBMDI, and IMLDI during August 2009 to December 2009. 

severity, and peak of drought are high in Guizhou and Guangxi Provinces. These results indicate that Huang-Hai Region and Yunnan, Guizhou, and Guangxi Provinces suffered from severe agricultural droughts frequently, which is consistent with the results of Wu et al. (2022). 

To analyze the occurrence risks of more severe agricultural droughts, we analyzed the univariate and bivariate return periods for duration (D _>_ 14), severity (S _>_ 2.2) and peak (P _>_ 0.45) of drought events in the eastern parts of China (Fig. 14). The marginal distributions of the duration, severity, and peak of agricultural drought were fitted by the exponential, gamma, and Pareto cumulative distribution functions, respectively. Bivariate joint distribution functions were selected from the best-fitting Archimedean copula functions of Clayton, Frank, and 

Gumbel. The results show that a relatively short return period (approximately 5–15 years) of drought with duration more than 14 months or severity higher than 2.2 is mainly detected in Huang-Hai Region and Yunnan, Guizhou, and Guangxi Provinces (Fig. 14a and b). The short return period of peak (P _>_ 0.45) is mainly located in Guangdong, Guangxi, and Guizhou provinces (Fig. 14c). Moreover, the logical ‘or’ (Fig. 14d-f) and ‘and’ (Fig. 14g-i) bivariate return period analysis also show that the short return periods of duration (D _>_ 14), severity (S _>_ 2.2) and/or peak (P _>_ 0.45) of drought events are observed in HuangHai Region, and Yunnan, Guizhou, and Guangxi Provinces. Overall, the return period analysis suggests that Huang-Hai Region and Yunnan, Guizhou, and Guangxi Provinces have a high risk to suffer from severe 

11 

_Agricultural Water Management 308 (2025) 109303_ 

_H. Chen et al.                                                                                                                                                                                                                                    Agricultural Water Management_ 





**Fig. 11.** Spatial and temporal evolutions of drought monitored by SPEI, PSDI, MRSDI, GBMDI, and IMLDI during January 2010 to June 2010. 

12 

_Agricultural Water Management 308 (2025) 109303_ 

_H. Chen et al.                                                                                                                                                                                                                                    Agricultural Water Management_ 





**Fig. 12.** Spatial and temporal evolutions of drought monitored by SPEI, PSDI, MRSDI, GBMDI, and IMLDI during December April 2019 to August 2019. 

agricultural droughts. 

## **4. Discussion** 

During recent decades, droughts become more frequent and intensified due to climate warming (Dai et al., 2020; Niu et al., 2023), which poses a serious threat to the agriculture, ecosystem, and sustainable infrastructure and resource management (Hussein and Basel, 2024; Valjarevi´c et al., 2022). Drought index is a way to quantitatively describe drought characteristics and facilitate drought risk analysis and monitoring. NDVI, P, SM, and LST retrieved from remote sensing are 

most widely used to develop integrated drought indices, such as GIDI and CDI. However, previous studies suggested that the response of NDVI to drought stress has a considerably long lag time (Song et al., 2018; Sun et al., 2015), and P cannot accurate reflect climatic wet and dry conditions. As SIF can reflect the physiological characteristics of vegetation and WB affects vegetation absorbing water from the soil, NDVI and P were replaced by SIF and WB, respectively, to develop IMLDI in this work, which may improve the performance of agricultural drought monitoring (Figs. 6–12). Previous study also used SIF, WB, and LST to develop TSWDI, and found it can better describe drought conditions than TVPDI based on NDVI, P, and LST (Liu et al., 2023b). 

13 

_Agricultural Water Management 308 (2025) 109303_ 

_H. Chen et al._ 



**Fig. 13.** Frequency (a), average duration (b, month), average severity (c), and average peak (d) of agricultural drought during 2001–2020. 

The weights of each variable in drought index are the key to accurately monitoring drought (Guo et al., 2019). Previous studies used simple linear combinations to constructed integrated drought indices, such as TVPDI, TSWDI, MIDI, and Optimal Scaled Drought Condition Index (OSDCI) (Guo et al., 2019). Simple linear combination models have the advantage of being relatively easy to compute and simple to implement (Hao and Singh, 2015; Jiao et al., 2019), but the wights of input variables are determined subjectively. In recent years, several studies have used machine learning methods to calculate the weights of input variables (Jiao et al., 2021; Xu et al., 2023), which is more suitable for describing complex drought phenomena. The weights of Composite Drought Monitoring Index (CDMI) and Comprehensive remote sensing-based Agriculture Drought Condition Indicator (CADCI) were determined by the random forest method (Alkaraki and Hazaymeh, 2023; Hanad´e Houmma et al., 2022), and the GBMDI was constructed based on the gradient boosting method (Zhang et al., 2022). Compared with other widely used drought indices, these integrated drought indices have a better performance in drought monitoring. However, there are still issues with hyperparameter optimization, overfitting, and black-box characteristics. Our work combines Bayesian-optimized LGBM and SHAP to obtain accurate and interpretable results for the development of IMLDI. The results (Figs. 6–12) from drought indices comparisons, cross-validation, and typical drought events monitoring indicate that IMLDI is a more reliable drought index for agricultural drought monitoring. 

The application of IMLDI can be extended in other regions based on different remote sensing datasets and land cover types. If climates and land cover types in other regions are quite different from the study area of this work, the weights of input remote sensing variables should be recalculated and the performance of IMLDI should be further validated. All remote sensing datasets used in the development of IMLDI are public 

available in a near-real time. Moreover, IMLDI was developed based on R and RStudio, which are also open source and freely available software, and can be easily reproduced by practitioners with a certain professional knowledge. Therefore, IMLDI can be used to monitor agricultural drought in a near-real time. 

Despite all these advantages, there are some limitations that may affect the performance of IMLDI. Firstly, the development of IMLDI relies heavily on multi-source remote sensing data. However, remote sensing is susceptible to atmospheric water vapors, aerosols, cloud cover, and sensor degradation, and usually has data gaps in some regions (Rousta et al., 2021). Therefore, remote sensing data has certain observation uncertainties, which may directly lead to accumulated uncertainties in drought monitoring of IMLDI. Secondly, as the correlations of annual real-world observed and drought index-based drought-affected cropland areas may be affected by various factors, such as the quality of statistical areas and spatial resolution of drought index, the results of validation based on annual statistical drought-affected cropland areas should be interpreted with caution. In future research, the performance of IMLDI should be tested against a broader range of real-world scenarios or field-based drought indices (e.g., SPI, PDSI), which may further verify the reliability of IMLDI in drought monitoring. 

## **5. Conclusion** 

Due to the complexity of drought disasters, a single or two variablesbased drought indices cannot fully reflect the real situation of agricultural drought. The development of integrated multiple variables drought indices is still urgent needed, and can benefit from the application of machine learning. In this work, a new agricultural drought index (IMLDI) was developed based on multi-source remote sensing data (SIF, WB, SM, and LST) and interpretable machine learning. The performance 

14 

_Agricultural Water Management 308 (2025) 109303_ 

_H. Chen et al._ 



**Fig. 14.** Spatial distributions of univariate and bivariate return periods for drought duration (D _>_ 14, month), severity (S _>_ 2.2) and peak (P _>_ 0.45). a, b, and c indicate univariate return periods of drought duration, severity, and peak. d, e, and f are bivariate logic ‘or’ joint return periods. g, h, and i are bivariate logic ‘and’ joint return periods. 

of IMLDI was systematically evaluated using SPEI, three widely used drought indices, the real-world drought-affected cropland areas, GPP, and two severe drought events. Besides, IMLDI-based drought risks were also analyzed in the eastern parts of China during 2001–2020. 

Compared with PSDI, MRSDI, and GBDMI, IMLDI can better capture drought conditions indicated by SPEI, has higher correlation coefficients with the real-world observed drought-affected cropland areas, and is significantly positive correlated with GPP in much larger areas (almost 

15 

_Agricultural Water Management 308 (2025) 109303_ 

_H. Chen et al._ 

in the entire regions). IMLDI can also successfully detect the drought dynamic changes of 2009/2010 and 2019 drought events, and thus IMLDI can be well employed to monitor agricultural drought. The Huang-Hai Region and Yunnan, Guizhou, and Guangxi Provinces experienced more than 25 severe agricultural drought events during 2001–2020, and the return period analysis also suggests that these regions have a high risk to suffer from severe agricultural droughts. In summary, this work provides a new and useful agricultural drought index based on multi-source remote sensing data, and has a great potential to improve agricultural drought monitoring in regions with limited ground-based observations. 

## **CRediT authorship contribution statement** 

**Hao Chen:** Writing – original draft, Visualization, Validation, Software, Methodology, Investigation, Formal analysis, Data curation, Conceptualization. **Ni Yang:** Writing – review & editing, Visualization, Supervision, Resources, Methodology, Funding acquisition, Formal analysis. **Xuanhua Song:** Visualization, Validation, Methodology, Investigation, Data curation. **Chunhua Lu:** Writing – review & editing, Software, Methodology, Investigation. **Menglan Lu:** Writing – review & editing, Methodology, Data curation. **Tan Chen:** Writing – review & editing, Visualization, Conceptualization. **Shulin Deng:** Writing – review & editing, Validation, Supervision, Resources, Project administration, Methodology, Funding acquisition. 

## **Declaration of Competing Interest** 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

## **Acknowledgements** 

This work was supported by the National Natural Science Foundations of China (grant no. 42061071 and 42101047), Guangxi Natural Science Foundation Program (grant no. 2021GXNSFBA220061), and Innovation Project of Guangxi Graduate Education (grant no. YCSW2024480). This work was supported by the Construction project of Natural Resources Digital Industry College，and was also supported by Guangxi First-class Discipline Statistics Construction Project Fund. 

## **Appendix A. Supporting information** 

Supplementary data associated with this article can be found in the online version at doi:10.1016/j.agwat.2025.109303. 

## **Data availability** 

The data that has been used is confidential. 

## **References** 

- Abbas, S., Nichol, J.E., Qamer, F.M., Xu, J., 2014. Characterization of drought development through remote sensing: a case study in Central Yunnan, China. Remote Sens. 6 (6), 4998–5018. 

- Abdul Gafoor, F., Al-Shehhi, M.R., Cho, C.-S., Ghedira, H., 2022. Gradient boosting and linear regression for estimating coastal bathymetry based on sentinel-2 images. Remote Sens. 14 (19), 5037. 

- AghaKouchak, A., Farahmand, A., Melton, F.S., Teixeira, J., Anderson, M.C., Wardlow, B. D., Hain, C.R., 2015. Remote sensing of drought: progress, challenges and opportunities. Rev. Geophys. 53 (2), 452–480. 

- Alibrahim, H., Ludwig, S.A., 2021. Hyperparameter optimization: Comparing genetic algorithm against grid search and bayesian optimization. In: IEEE Congress on Evolutionary Computation (CEC), 2021. IEEE, pp. 1551–1559. 

- Alkaraki, K.F., Hazaymeh, K., 2023. A comprehensive remote sensing-based Agriculture Drought Condition Indicator (CADCI) using machine learning. Environ. Chall. 11, 100699. 

- Bas¸akın, E.E., Stoy, P.C., Demirel, M.C., Ozdogan, M., Otkin, J.A., 2024. Combined 

   - drought index using high-resolution hydrological models and explainable artificial intelligence techniques in Türkiye. Remote Sens. 16 (20), 3799. 

- Beck, H.E., Van Dijk, A.I., Levizzani, V., Schellekens, J., Miralles, D.G., Martens, B., De Roo, A., 2017. MSWEP: 3-hourly 0.25 global gridded precipitation (1979–2015) by merging gauge, satellite, and reanalysis data. Hydrol. Earth Syst. Sci. 21 (1), 589–615. 

- Bent´ejac, C., Csorg¨ o, A., Martínez-Mu˝ noz, G., 2021. A comparative analysis of gradient ˜ boosting algorithms. Artif. Intell. Rev. 54, 1937–1967. 

- Birky, A.K., 2001. NDVI and a simple model of deciduous forest seasonal dynamics. Ecol. Model. 143 (1-2), 43–58. 

- Cai, Z., Jonsson, P., Jin, H., Eklundh, L., 2017. Performance of smoothing methods for ¨ reconstructing NDVI time-series and estimating vegetation phenology from MODIS data. Remote Sens. 9 (12), 1271. 

- Chen, L., Li, Y., Ge, Z.-A., Lu, B., Wang, L., Wei, X., Sun, M., Wang, Z., Li, T., Luo, J.-J., 2023. Causes of the extreme drought in late summer–autumn 2019 in Eastern China and Its Future Risk. J. Clim. 36 (4), 1085–1104. 

- Chen, T., Guestrin, C., 2016. Xgboost: A scalable tree boosting system, Proceedings of the 22nd acm sigkdd international conference on knowledge discovery and data mining, pp. 785-794. 

- Cohen, I., Huang, Y., Chen, J., Benesty, J., Benesty, J., Chen, J., Huang, Y., Cohen, I., 2009. Pearson correlation coefficient. Noise Reduct. Speech Process. 1–4. 

- Cui, T., Sun, R., Qiao, C., Zhang, Q., Yu, T., Liu, G., Liu, Z., 2017. Estimating diurnal courses of gross primary production for maize: a comparison of sun-induced chlorophyll fluorescence, light-use efficiency and process-based models. Remote Sens. 9 (12), 1267. 

- Dai, M., Huang, S., Huang, Q., Leng, G., Guo, Y., Wang, L., Fang, W., Li, P., Zheng, X., 2020. Assessing agricultural drought risk and its dynamic evolution characteristics. Agric. Water Manag. 231, 106003. 

- Daumard, F., Champagne, S., Fournier, A., Goulas, Y., Ounis, A., Hanocq, J.-F., Moya, I., 2010. A field platform for continuous measurement of canopy fluorescence. IEEE Trans. Geosci. Remote Sens. 48 (9), 3358–3368. 

- De’Ath, G., 2007. Boosted trees for ecological modeling and prediction. Ecology 88 (1), 243–251. 

- Degefu, W., 1987. Some aspects of meteorological drought in Ethiopia. Drought Hunger Afr.: Denying famine a Future 23–36. 

- Ding, T., Gao, H., 2020. The record-breaking extreme drought in Yunnan Province, Southwest China during spring-early summer of 2019 and possible causes. J. Meteorol. Res. 34 (5), 997–1012. 

- Dracup, J.A., Lee, K.S., Paulson Jr, E.G., 1980. On the statistical characteristics of drought events. Water Resour. Res. 16 (2), 289–296. 

- Du, L., Tian, Q., Yu, T., Meng, Q., Jancso, T., Udvardy, P., Huang, Y., 2013. A comprehensive drought monitoring method integrating MODIS and TRMM data. Int. J. Appl. Earth Obs. Geoinf. 23, 245–253. 

Feng, P., Wang, B., Li Liu, D., Yu, Q., 2019. Machine learning-based integration of remotely-sensed drought factors can improve the estimation of agricultural drought in South-Eastern Australia. Agric. Syst. 173, 303–316. 

- Feurer, M., Hutter, F., 2019. Hyperparameter optimization. Autom. Mach. Learn.: Methods, Syst., Chall. 3–33. 

- Funk, C.C., Peterson, P.J., Landsfeld, M.F., Pedreros, D.H., Verdin, J.P., Rowland, J.D., Romero, B.E., Husak, G.J., Michaelsen, J.C., Verdin, A.P., 2014. A quasi-global precipitation time series for drought monitoring, 2327-638X. US Geological Survey. 

- Funk, C., Peterson, P., Landsfeld, M., Pedreros, D., Verdin, J., Shukla, S., Husak, G., Rowland, J., Harrison, L., Hoell, A., 2015a. The climate hazards infrared 

   - precipitation with stations—a new environmental record for monitoring extremes. Sci. data 2 (1), 1–21. 

- Funk, C., Verdin, A., Michaelsen, J., Peterson, P., Pedreros, D., Husak, G., 2015b. A global satellite-assisted precipitation climatology. Earth Syst. Sci. Data 7 (2), 275–287. 

- Gao, B.-C., 1996. NDWI—a normalized difference water index for remote sensing of vegetation liquid water from space. Remote Sens. Environ. 58 (3), 257–266. 

- Gao, L., Tao, B., Miao, Y., Zhang, L., Song, X., Ren, W., He, L., Xu, X., 2019. A global data set for economic losses of extreme hydrological events during 1960-2014. Water Resour. Res. 55 (6), 5165–5175. 

- Gessner, U., Machwitz, M., Esch, T., Tillack, A., Naeimi, V., Kuenzer, C., Dech, S., 2015. Multi-sensor mapping of West African land cover using MODIS, ASAR and TanDEMX/TerraSAR-X data. Remote Sens. Environ. 164, 282–297. 

- Greenacre, M., Groenen, P.J., Hastie, T., d’Enza, A.I., Markos, A., Tuzhilina, E., 2022. Principal component analysis. Nat. Rev. Methods Prim. 2 (1), 100. 

- Gr´egoire, G., 2014. Multiple linear regression. Eur. Astron. Soc. Publ. Ser. 66, 45–72. Guanter, L., Zhang, Y., Jung, M., Joiner, J., Voigt, M., Berry, J.A., Frankenberg, C., Huete, A.R., Zarco-Tejada, P., Lee, J.-E., 2014. Global and time-resolved monitoring of crop photosynthesis with chlorophyll fluorescence. Proc. Natl. Acad. Sci. 111 (14), E1327–E1333. 

- Guo, H., Bao, A., Liu, T., Ndayisaba, F., Jiang, L., Zheng, G., Chen, T., De Maeyer, P., 2019. Determining variable weights for an optimal scaled drought condition index (OSDCI): evaluation in central Asia. Remote Sens. Environ. 231, 111220. 

Hanad´e Houmma, I., El Mansouri, L., Hadria, R., Emran, A., Chehbouni, A., 2022. Retrospective analysis and version improvement of the satellite-based drought composite index. A semi-arid Tensift-Morocco application. Geocarto Int. 37 (11), 3069–3090. 

- Hao, Z., Singh, V.P., 2015. Drought characterization from a multivariate perspective: a review. J. Hydrol. 527, 668–678. 

Hao, C., Zhang, J., Yao, F., 2015. Combination of multi-sensor remote sensing data for drought monitoring over Southwest China. Int. J. Appl. Earth Obs. Geoinf. 35, 270–283. 

16 

_Agricultural Water Management 308 (2025) 109303_ 

_H. Chen et al._ 

Hartley, A., MacBean, N., Georgievski, G., Bontemps, S., 2017. Uncertainty in plant functional type distributions and its impact on land surface models. Remote Sens. Environ. 203, 71–89. 

- Hmimina, G., Dufrˆene, E., Pontailler, J.-Y., Delpierre, N., Aubinet, M., Caquet, B., De Grandcourt, A., Burban, B., Flechard, C., Granier, A., 2013. Evaluation of the potential of MODIS satellite data to predict vegetation phenology in different biomes: an investigation using ground-based NDVI measurements. Remote Sens. Environ. 132, 145–158. 

- Hua, T., Wang, X., Zhang, C., Lang, L., Li, H., 2017. Responses of vegetation activity to drought in northern China. Land Degrad. Dev. 28 (7), 1913–1921. 

- Huete, A., Didan, K., Miura, T., Rodriguez, E.P., Gao, X., Ferreira, L.G., 2002. Overview of the radiometric and biophysical performance of the MODIS vegetation indices. Remote Sens. Environ. 83 (1-2), 195–213. 

- Hussein, N.A.-H.K., Basel, O.M., 2024. Integrating renewable energy systems into urban planning for sustainable cities. ESTIDAMAA 2024, 15–21. 

- Jasinski, M.F., Borak, J.S., Kumar, S.V., Mocko, D.M., Peters-Lidard, C.D., Rodell, M., Rui, H., Beaudoing, H.K., Vollmer, B.E., Arsenault, K.R., 2019. NCA-LDAS: overview and analysis of hydrologic trends for the national climate assessment. J. Hydrometeorol. 20 (8), 1595–1617. 

- Jiao, W., Tian, C., Chang, Q., Novick, K.A., Wang, L., 2019. A new multi-sensor integrated index for drought monitoring. Agric. For. Meteorol. 268, 74–85. 

- Jiao, W., Wang, L., McCabe, M.F., 2021. Multi-sensor remote sensing for drought characterization: current status, opportunities and a roadmap for the future. Remote Sens. Environ. 256, 112313. 

- Ke, G., Meng, Q., Finley, T., Wang, T., Chen, W., Ma, W., Ye, Q., Liu, T.-Y., 2017. Lightgbm: a highly efficient gradient boosting decision tree. Adv. Neural Inf. Process. Syst. 30. 

- Kim, S.W., Jung, D., Choung, Y.-J., 2020. Development of a multiple linear regression model for meteorological drought index estimation based on landsat satellite imagery. Water 12 (12), 3393. 

- Kim, J.E., Yu, J., Ryu, J.-H., Lee, J.-H., Kim, T.-W., 2021. Assessment of regional drought vulnerability and risk using principal component analysis and a Gaussian mixture model. Nat. Hazards 109 (1), 707–724. 

- Kogan, F.N., 1995a. Application of vegetation index and brightness temperature for drought detection. Adv. Space Res. 15 (11), 91–100. 

- Kogan, F.N., 1995b. Droughts of the late 1980s in the United States as derived from NOAA polar-orbiting satellite data. Bull. Am. Meteorol. Soc. 76 (5), 655–668. 

- Kogan, F., Stark, R., Gitelson, A., Jargalsaikhan, L., Dugrajav, C., Tsooj, S., 2004. Derivation of pasture biomass in Mongolia from AVHRR-based vegetation health indices. Int. J. Remote Sens. 25 (14), 2889–2896. 

- Kumar, S.V., Jasinski, M., Mocko, D.M., Rodell, M., Borak, J., Li, B., Beaudoing, H.K., Peters-Lidard, C.D., 2019. NCA-LDAS land analysis: development and performance of a multisensor, multivariate land data assimilation system for the national climate assessment. J. Hydrometeorol. 20 (8), 1571–1593. 

- Lamchin, M., Lee, W.-K., Jeon, S.W., Wang, S.W., Lim, C.H., Song, C., Sung, M., 2018. Long-term trend and correlation between vegetation greenness and climate variables in Asia based on satellite data. Sci. Total Environ. 618, 1089–1095. 

- Lasaponara, R., 2006. On the use of principal component analysis (PCA) for evaluating interannual vegetation anomalies from SPOT/VEGETATION NDVI temporal series. Ecol. Model. 194 (4), 429–434. 

- Lee, J.-E., Frankenberg, C., van der Tol, C., Berry, J.A., Guanter, L., Boyce, C.K., Fisher, J. B., Morrow, E., Worden, J.R., Asefi, S., 2013. Forest productivity and water stress in Amazonia: observations from GOSAT chlorophyll fluorescence. Proc. R. Soc. B: Biol. Sci. 280 (1761), 20130171. 

- Li, Z., 2022. Extracting spatial effects from machine learning model using local interpretation method: an example of SHAP and XGBoost. Comput., Environ. Urban Syst. 96, 101845. 

- Li, R., Chen, N., Zhang, X., Zeng, L., Wang, X., Tang, S., Li, D., Niyogi, D., 2020a. Quantitative analysis of agricultural drought propagation process in the Yangtze River Basin by using cross wavelet analysis and spatial autocorrelation. Agric. For. Meteorol. 280, 107809. 

- Li, Z., Han, Y., Hao, T., 2020b. Assessing the consistency of remotely sensed multiple drought indices for monitoring drought phenomena in continental China. IEEE Trans. Geosci. Remote Sens. 58 (8), 5490–5502. 

- Li, C., Leal Filho, W., Yin, J., Hu, R., Wang, J., Yang, C., Yin, S., Bao, Y., Ayal, D.Y., 2018a. Assessing vegetation response to multi-time-scale drought across inner Mongolia plateau. J. Clean. Prod. 179, 210–216. 

- Li, W., MacBean, N., Ciais, P., Defourny, P., Lamarche, C., Bontemps, S., Houghton, R.A., Peng, S., 2018c. Gross and net land cover changes in the main plant functional types derived from the annual ESA CCI land cover maps (1992–2015). Earth Syst. Sci. Data 10 (1), 219–234. 

- Li, C., Wang, J., Hu, R., Yin, S., Bao, Y., Ayal, D.Y., 2018b. Relationship between vegetation change and extreme climate indices on the Inner Mongolia Plateau, China, from 1982 to 2013. Ecol. Indic. 89, 101–109. 

- Li, X., Xiao, J., 2019a. A global, 0.05-degree product of solar-induced chlorophyll fluorescence derived from OCO-2, MODIS, and reanalysis data. Remote Sens. 11 (5), 517. 

- Li, X., Xiao, J., 2019b. Mapping photosynthesis solely from solar-induced chlorophyll fluorescence: a global, fine-resolution dataset of gross primary production derived from OCO-2. Remote Sens. 11 (21), 2563. 

- Liu, Y., Dang, C., Yue, H., Lyu, C., Dang, X., 2021a. Enhanced drought detection and monitoring using sun-induced chlorophyll fluorescence over Hulun Buir Grassland, China. Sci. Total Environ. 770, 145271. 

- Liu, Y., Qian, J., Yue, H., 2021b. Comparison and evaluation of different dryness indices based on vegetation indices-land surface temperature/albedo feature space. Adv. Space Res. 68 (7), 2791–2803. 

- Liu, Y., Shan, F., Yue, H., Wang, X., Fan, Y., 2023a. Global analysis of the correlation and propagation among meteorological, agricultural, surface water, and groundwater droughts. J. Environ. Manag. 333, 117460. 

- Liu, Y., Yu, X., Dang, C., Yue, H., Wang, X., Niu, H., Zu, P., Cao, M., 2023b. A dryness index TSWDI based on land surface temperature, sun-induced chlorophyll fluorescence, and water balance. ISPRS J. Photogramm. Remote Sens. 202, 581–598. 

- Liu, Y., Yue, H., 2018. The temperature vegetation dryness index (TVDI) based on Biparabolic NDVI-Ts space and gradient-based structural similarity (GSSIM) for longterm drought assessment across Shaanxi province, China (2000–2016). Remote Sens. 10 (6), 959. 

- Liu, Y., Zhu, Y., Ren, L., Yong, B., Singh, V.P., Yuan, F., Jiang, S., Yang, X., 2019. On the mechanisms of two composite methods for construction of multivariate drought indices. Sci. Total Environ. 647, 981–991. 

- Lu, E., Luo, Y., Zhang, R., Wu, Q., Liu, L., 2011. Regional atmospheric anomalies responsible for the 2009–2010 severe drought in China. J. Geophys. Res.: Atmos. 116 (D21). 

- Lu, X., Wang, L., Pan, M., Kaseke, K.F., Li, B., 2016. A multi-scale analysis of Namibian rainfall over the recent decade–comparing TMPA satellite estimates and ground observations. J. Hydrol.: Reg. Stud. 8, 59–68. 

- Malczewski, J., Liu, X., 2014. Local ordered weighted averaging in GIS-based multicriteria analysis. Ann. GIS 20 (2), 117–129. 

- McKee, T.B., Doesken, N.J., Kleist, J., 1993. The relationship of drought frequency and duration to time scales, Proceedings of the 8th Conference on Applied Climatology. Boston, pp. 179-183. 

- Mishra, A.K., Singh, V.P., 2010. A review of drought concepts. J. Hydrol. 391 (1-2), 202–216. 

- Mokhtari, K.E., Higdon, B.P., Bas¸ar, A., 2019. Interpreting financial time series with SHAP values, Proceedings of the 29th annual international conference on computer science and software engineering, pp. 166-172. 

- Naumann, G., Cammalleri, C., Mentaschi, L., Feyen, L., 2021. Increased economic drought impacts in Europe with anthropogenic warming. Nat. Clim. Change 11 (6), 485–491. 

- Niu, Y., Abdullayev, V., Alyar, A., Asgarov, T., 2023. Resilience and adaptation to climate change: community-based strategies in coastal regions. ESTIDAMAA 2023, 37–44. 

- Noi, P.T., Degener, J., Kappas, M., 2017. Comparison of multiple linear regression, cubist regression, and random forest algorithms to estimate daily air surface temperature from dynamic combinations of MODIS LST data. Remote Sens. 9 (5), 398. 

- Palmer, W.C., 1965. Meteorological drought, 30. US Department of Commerce, Weather Bureau. 

- Park, S., Im, J., Jang, E., Rhee, J., 2016. Drought assessment and monitoring through blending of multi-sensor indices using machine learning approaches for different climate regions. Agric. For. Meteorol. 216, 157–169. 

- Park, S., Im, J., Park, S., Rhee, J., 2017. Drought monitoring using high resolution soil moisture through multi-sensor satellite data fusion over the Korean peninsula. Agric. For. Meteorol. 237, 257–269. 

- Pradhan, P., Costa, L., Rybski, D., Lucht, W., Kropp, J.P., 2017. A systematic study of sustainable development goal (SDG) interactions. Earth’S. Future 5 (11), 1169–1179. 

- Qiu, R., Li, X., Han, G., Xiao, J., Ma, X., Gong, W., 2022. Monitoring drought impacts on crop productivity of the U.S. Midwest with solar-induced fluorescence: GOSIF outperforms GOME-2 SIF and MODIS NDVI, EVI, and NIRv. Agric. For. Meteorol. 323, 109038. 

- Ren, H., Du, L., Peng, C., Yang, J., Gao, W., 2024. The composite drought index incorporated solar-induced chlorophyll fluorescence enhances the monitoring capability of short-term drought. J. Hydrol., 131361 

- Rhee, J., Im, J., 2017. Meteorological drought forecasting for ungauged areas based on machine learning: using long-range climate forecast and remote sensing data. Agric. For. Meteorol. 237, 105–122. 

- Rhee, J., Im, J., Carbone, G.J., 2010. Monitoring agricultural drought for arid and humid regions using multi-sensor remote sensing data. Remote Sens. Environ. 114 (12), 2875–2887. 

- Rivera, J.A., Penalba, O.C., 2014. Trends and spatial patterns of drought affected area in Southern South America. Climate 2 (4), 264–278. 

- Rouse, J.W., Haas, R.H., Schell, J.A., Deering, D.W., 1974. Monitoring vegetation systems in the Great Plains with ERTS. NASA Spec. Publ. 351 (1), 309. 

- Rousta, I., Olafsson, H., Nasserzadeh, M.H., Zhang, H., Krzyszczak, J., Baranowski, P., 2021. Dynamics of daytime land surface temperature (LST) variabilities in the Middle East countries during 2001–2018. Pure Appl. Geophys. 178 (6), 2357–2377. 

- Samantaray, A.K., Ramadas, M., Panda, R.K., 2022. Changes in drought characteristics based on rainfall pattern drought index and the CMIP6 multi-model ensemble. Agric. Water Manag. 266, 107568. 

- Sheffield, J., Ferguson, C.R., Troy, T.J., Wood, E.F., McCabe, M.F., 2009. Closing the terrestrial water budget from satellite remote sensing. Geophys. Res. Lett. 36 (7). 

- Shekhar, A., Buchmann, N., Gharun, M., 2022. How well do recently reconstructed solarinduced fluorescence datasets model gross primary productivity? Remote Sens. Environ. 283, 113282. 

- Shi, J., Cui, L., Tian, Z., 2020. Spatial and temporal distribution and trend in flood and drought disasters in East China. Environ. Res. 185, 109406. 

- Snoek, J., Larochelle, H., Adams, R.P., 2012. Practical bayesian optimization of machine learning algorithms. Adv. Neural Inf. Process. Syst. 25. 

- Song, L., Guanter, L., Guan, K., You, L., Huete, A., Ju, W., Zhang, Y., 2018. Satellite suninduced chlorophyll fluorescence detects early response of winter wheat to heat stress in the Indian Indo-Gangetic Plains. Glob. Change Biol. 24 (9), 4023–4037. 

- Sui, X.-X., Qin, Q.-M., Dong, H., Wang, J.-L., Meng, Q.-Y., Liu, M.-C., 2013. Monitoring of farmland drought based on LST-LAI spectral feature space. Spectrosc. Spectr. Anal. 33 (1), 201–205. 

17 

_Agricultural Water Management 308 (2025) 109303_ 

_H. Chen et al._ 

- Sun, Y., Fu, R., Dickinson, R., Joiner, J., Frankenberg, C., Gu, L., Xia, Y., Fernando, N., 2015. Drought onset mechanisms revealed by satellite solar-induced chlorophyll fluorescence: insights from two contrasting extreme events. J. Geophys. Res.: Biogeosciences 120 (11), 2427–2440. 

- Sun, P., Zhang, Q., Wen, Q., Singh, V.P., Shi, P., 2017. Multisource data-based integrated agricultural drought monitoring in the Huai River basin, China. J. Geophys. Res.: Atmos. 122 (20), 10,751–10,772. 

- Sun, H., Zhao, X., Chen, Y., Gong, A., Yang, J., 2013. A new agricultural drought monitoring index combining MODIS NDWI and day–night land surface temperatures: a case study in China. Int. J. Remote Sens. 34 (24), 8986–9001. 

- Szczepanek, R., 2022. Daily streamflow forecasting in mountainous catchment using XGBoost, LightGBM and CatBoost. Hydrology 9 (12), 226. 

- Tang, Z., Zhang, H., Yi, S., Xiao, Y., 2018. Assessment of flood susceptible areas using spatially explicit, probabilistic multi-criteria decision analysis. J. Hydrol. 558, 144–158. 

- Tian, L., Yuan, S., Quiring, S.M., 2018. Evaluation of six indices for monitoring agricultural drought in the south-central United States. Agric. For. Meteorol. 249, 107–119. 

- Um, M.-J., Kim, Y., Park, D., 2018. Evaluation and modification of the drought severity index (DSI) in East Asia. Remote Sens. Environ. 209, 66–76. 

- Uyanık, G.K., Güler, N., 2013. A study on multiple linear regression analysis. ProcediaSoc. Behav. Sci. 106, 234–240. 

- Valjarevi´c, A., Popovici, C., Stili<sup>ˇ</sup> ´c, A., Radojkovi´c, M., 2022. Cloudiness and water from cloud seeding in connection with plants distribution in the Republic of Moldova. Appl. Water Sci. 12 (12), 262. 

- Van den Broeck, G., Lykov, A., Schleich, M., Suciu, D., 2022. On the tractability of SHAP explanations. J. Artif. Intell. Res. 74, 851–886. 

- Verhoeven, E., Wardle, G.M., Roth, G.W., Greenville, A.C., 2022. Characterising the spatiotemporal dynamics of drought and wet events in Australia. Sci. Total Environ. 846, 157480. 

- Vicente-Serrano, S.M., 2007. Evaluating the impact of drought using remote sensing in a Mediterranean, semi-arid region. Nat. Hazards 40, 173–208. 

- Vicente-Serrano, S.M., Beguería, S., Lopez-Moreno, J.I., 2010. A multiscalar drought ´ index sensitive to global warming: the standardized precipitation evapotranspiration index. J. Clim. 23 (7), 1696–1718. 

- Wang, L., d’Odorico, P., Evans, J., Eldridge, D., McCabe, M., Caylor, K., King, E., 2012. Dryland ecohydrology and climate change: critical issues and technical advances. Hydrol. Earth Syst. Sci. 16 (8), 2585–2603. 

- Wang, Z., Wang, Z., Xiong, J., He, W., Yong, Z., Wang, X., 2022. Responses of the remote sensing drought index with soil information to meteorological and agricultural droughts in Southeastern Tibet. Remote Sens. 14 (23), 6125. 

- Wei, W., Pang, S., Wang, X., Zhou, L., Xie, B., Zhou, J., Li, C., 2020. Temperature vegetation precipitation dryness index (TVPDI)-based dryness-wetness monitoring in China. Remote Sens. Environ. 248, 111957. 

- Wei, W., Zhang, X., Liu, C., Xie, B., Zhou, J., Zhang, H., 2023. A new drought index and its application based on geographically weighted regression (GWR) model and multisource remote sensing data. Environ. Sci. Pollut. Res. 30 (7), 17865–17887. 

- Wei, W., Zhang, J., Zhou, J., Zhou, L., Xie, B., Li, C., 2021. Monitoring drought dynamics in China using Optimized Meteorological Drought Index (OMDI) based on remote sensing data sets. J. Environ. Manag. 292, 112733. 

- West, H., Quinn, N., Horswell, M., 2019. Remote sensing for drought monitoring & impact assessment: progress, past challenges and future opportunities. Remote Sens. Environ. 232, 111291. 

- Wilhite, D.A., Glantz, M.H., 1985. Understanding: the drought phenomenon: the role of definitions. Water Int. 10 (3), 111–120. 

- Wu, J., Chen, X.-Y., Zhang, H., Xiong, L.-D., Lei, H., Deng, S.-H., 2019. Hyperparameter optimization for machine learning models based on Bayesian optimization. J. Electron. Sci. Technol. 17 (1), 26–40. 

- Wu, D., Li, Z., Zhu, Y., Li, X., Wu, Y., Fang, S., 2021. A new agricultural drought index for monitoring the water stress of winter wheat. Agric. Water Manag. 244, 106599. 

- Wu, X., Zhang, R., Bento, V.A., Leng, S., Qi, J., Zeng, J., Wang, Q., 2022. The effect of drought on vegetation gross primary productivity under different vegetation types across China from 2001 to 2020. Remote Sens. 14 (18), 4658. 

- Wu, J., Zhou, L., Liu, M., Zhang, J., Leng, S., Diao, C., 2013. Establishing and assessing the Integrated Surface Drought Index (ISDI) for agricultural drought monitoring in mid-eastern China. Int. J. Appl. Earth Obs. Geoinf. 23, 397–410. 

- Xu, Z., Sun, H., Zhang, T., Xu, H., Wu, D., Gao, J., 2023. Evaluating established deep learning methods in constructing integrated remote sensing drought index: a case study in China. Agric. Water Manag. 286, 108405. 

- Yan, X., Zhang, B., Yao, Y., Yang, Y., Li, J., Ran, Q., 2021. GRACE and land surface models reveal severe drought in eastern China in 2019. J. Hydrol. 601, 126640. 

- Yang, C., Chen, M., Yuan, Q., 2021. The application of XGBoost and SHAP to examining the factors in freight truck-related crashes: an exploratory analysis. Accid. Anal. Prev. 158, 106153. 

- Yang, J., Gong, D., Wang, W., Hu, M., Mao, R., 2012. Extreme drought event of 2009/ 2010 over southwestern China. Meteorol. Atmos. Phys. 115, 173–184. 

- Yang, Y., Xiao, P., Feng, X., Li, H., 2017. Accuracy assessment of seven global land cover datasets over China. ISPRS J. Photogramm. Remote Sens. 125, 156–173. 

- Yevjevich, V.M., 1967. An objective approach to definitions and investigations of continental hydrologic droughts, 23. Colorado State University Fort Collins, CO, USA. 

- Yoshida, Y., Joiner, J., Tucker, C., Berry, J., Lee, J.-E., Walker, G., Reichle, R., Koster, R., Lyapustin, A., Wang, Y., 2015. The 2010 Russian drought impact on satellite measurements of solar-induced chlorophyll fluorescence: insights from modeling and comparisons with parameters derived from satellite reflectances. Remote Sens. Environ. 166, 163–177. 

- Yu, R., Zhai, P., 2020. Changes in compound drought and hot extreme events in summer over populated eastern China. Weather Clim. Extrem. 30, 100295. 

- Zambrano, F., Lillo-Saavedra, M., Verbist, K., Lagos, O., 2016. Sixteen years of agricultural drought assessment of the BioBío region in Chile using a 250 m resolution Vegetation Condition Index (VCI). Remote Sens. 8 (6), 530. 

- Zambrano, F., Wardlow, B., Tadesse, T., Lillo-Saavedra, M., Lagos, O., 2017. Evaluating satellite-derived long-term historical precipitation datasets for drought monitoring in Chile. Atmos. Res. 186, 26–42. 

- Zhang, Q., Fan, K., Singh, V.P., Sun, P., Shi, P., 2018a. Evaluation of remotely sensed and reanalysis soil moisture against in situ observations on the himalayan-tibetan plateau. J. Geophys. Res.: Atmos. 123 (14), 7132–7148. 

- Zhang, Y., Haghani, A., 2015. A gradient boosting method to improve travel time prediction. Transp. Res. Part C: Emerg. Technol. 58, 308–324. 

- Zhang, N., Hong, Y., Qin, Q., Liu, L., 2013. VSDI: a visible and shortwave infrared drought index for monitoring soil and vegetation moisture based on optical remote sensing. Int. J. Remote Sens. 34 (13), 4585–4609. 

- Zhang, A., Jia, G., 2013. Monitoring meteorological drought in semiarid regions using multi-sensor microwave remote sensing data. Remote Sens. Environ. 134, 12–23. 

- Zhang, L., Jiao, W., Zhang, H., Huang, C., Tong, Q., 2017. Studying drought phenomena in the Continental United States in 2011 and 2012 using various drought indices. Remote Sens. Environ. 190, 96–106. 

- Zhang, Y., Kong, D., Gan, R., Chiew, F.H., McVicar, T.R., Zhang, Q., Yang, Y., 2019b. Coupled estimation of 500 m and 8-day resolution global evapotranspiration and gross primary production in 2002–2017. Remote Sens. Environ. 222, 165–182. 

- Zhang, Q., Li, Q., Singh, V.P., Shi, P., Huang, Q., Sun, P., 2018b. Nonparametric integrated agrometeorological drought monitoring: model development and application. J. Geophys. Res.: Atmos. 123 (1), 73–88. 

- Zhang, L., Qiao, N., Huang, C., Wang, S., 2019a. Monitoring drought effects on vegetation productivity using satellite solar-induced chlorophyll fluorescence. Remote Sens. 11 (4), 378. 

- Zhang, Q., Shi, R., Xu, C.-Y., Sun, P., Yu, H., Zhao, J., 2022. Multisource data-based integrated drought monitoring index: model development and application. J. Hydrol. 615, 128644. 

- Zhang, L., Xiao, J., Li, J., Wang, K., Lei, L., Guo, H., 2012. The 2010 spring drought reduced primary productivity in southwestern China. Environ. Res. Lett. 7 (4), 045706. 

- Zhang, Z., Xu, W., Qin, Q., Long, Z., 2020. Downscaling solar-induced chlorophyll fluorescence based on convolutional neural network method to monitor agricultural drought. IEEE Trans. Geosci. Remote Sens. 59 (2), 1012–1028. 

- Zhang, Z., Xu, W., Shi, Z., Qin, Q., 2021. Establishment of a comprehensive drought monitoring index based on multisource remote sensing data and agricultural drought monitoring. IEEE J. Sel. Top. Appl. Earth Obs. Remote Sens. 14, 2113–2126. 

- Zhang, M., Yuan, X., 2020. Rapid reduction in ecosystem productivity caused by flash droughts based on decade-long FLUXNET observations. Hydrol. Earth Syst. Sci. 24 (11), 5579–5593. 

- Zhang Xiang, Z.X., Chen NengCheng, C.N., Li JiZhen, L.J., Chen ZhiHong, C.Z., Niyogi, D., 2017. Multi-sensor integrated framework and index for agricultural drought monitoring. 

- Zhou, S., Zhang, D., Wang, M., Liu, Z., Gan, W., Zhao, Z., Xue, S., Müller, B., Zhou, M., Ni, X., 2024. Risk-driven composition decoupling analysis for urban flooding prediction in high-density urban areas using Bayesian-Optimized LightGBM. J. Clean. Prod. 457, 142286. 

18 

