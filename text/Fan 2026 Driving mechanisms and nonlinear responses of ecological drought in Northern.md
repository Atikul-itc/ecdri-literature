Journal of Hydrology: Regional Studies 64 (2026) 103174 



Contents lists available at ScienceDirect 

# Journal of Hydrology: Regional Studies 

journal homepage: www.elsevier.com/locate/ejrh 



## Driving mechanisms and nonlinear responses of ecological drought in Northern China's Agro-Pastoral Ecotone 



Yaoyuan Fan<sup>a</sup> , Jian Zhang<sup>a,*</sup> , Asim Biswas<sup>b</sup> , Siyi Cheng<sup>a</sup> , Xiaoran Ren<sup>a</sup> , Chunhui Zhan<sup>a</sup> 

a _College of Geography and Environmental Science, Northwest Normal University, Lanzhou 730070, China_ b _School of Environmental Sciences, University of Guelph, 50 Stone Road East, Guelph, ON N1G 2W1, Canada_ 

A R T I C L E I N F O 

A B S T R A C T 

_Keywords:_ Ecological drought Kernel vegetation index Machine learning interpretation Nonlinear thresholds LULC-dependence Agro-Pastoral Ecotone 

_Study region:_ Northern China's Agro-Pastoral Ecotone (APENC, 2000–2022) was selected as a climatically sensitive transition belt from semi-arid to semi-humid conditions. _Study focus:_ We developed a kernel Temperature–Vegetation Dryness Index (kTVDI) that exploits the kernel Normalized Difference Vegetation Index to overcome spectral saturation, and coupled it with XGBoost–SHAP and Generalized Additive Models to decode nonlinear drought drivers. Validated against an independent soil moisture dataset, kTVDI demonstrated superior sensitivity (ρ = − 0.604 vs. − 0.533 for TVDI) and stronger agreement with solar-induced chlorophyll fluorescence (SIF), supporting its use as an improved ecological drought indicator. Over 2000–2022 regional drought declined significantly (–1.328 × 10⁻³ yr⁻¹, p _<_ 0.01), but spatial heterogeneity persisted: south-eastern alleviation vs. north-western intensification. _New hydrological insights for the region:_ Temperature universally dominates (32.92–52.24 % SHAP importance), yet land-use/land-cover restructures secondary controls: vegetated systems exhibit evapotranspiration-regulated water balance, whereas deserts display precipitation-limited dynamics amplified by human disturbance. Critical thresholds marking energy–water regime shifts are 6.6<sup>◦</sup> C for temperature, 387 mm yr⁻¹ for evapotranspiration and 54.2 % for relative humidity. Interaction analysis further reveals land-use-specific synergies (humidity–soil in croplands, soil–topography in forests, topography–precipitation–human activity in deserts), underscoring ecosystem-dependent vulnerability. This interpretable framework advances process-based drought understanding in ecotones and furnishes quantitative thresholds for adaptive management under global change. 

### **1. Introduction** 

Drought ranks among Earth’s most pervasive natural hazards, with intensifying frequency and severity under anthropogenic climate change threatening water security, agricultural productivity, and ecosystem integrity globally (IPCC, 2022). Traditional drought paradigms—meteorological, agricultural, and hydrological—primarily characterize physical water deficits but insufficiently reflect how moisture stress propagates through vegetation structure and function (Crausbay et al., 2017; Slette et al., 2019; Cui et al., 2024). This conceptual limitation has motivated increasing attention to ecological drought, an integrative perspective that emphasizes 

* Corresponding author. 

_E-mail address:_ jianzhang@nwnu.edu.cn (J. Zhang). 

https://doi.org/10.1016/j.ejrh.2026.103174 

Received 28 October 2025; Received in revised form 7 January 2026; Accepted 21 January 2026 Available online 27 January 2026 2214-5818/© 2026 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/ ). 

_Journal of Hydrology: Regional Studies 64 (2026) 103174_ 

_Y. Fan et al._ 

how water scarcity cascades through biotic systems and may trigger ecological degradation or regime shifts (Walter et al., 2024). Ecological drought refers to water limitation pushing ecosystems toward or beyond vulnerability thresholds and inducing eco-physiological stress (Crausbay et al., 2017), which in remote-sensing contexts can be identified through observable changes in vegetation growth, evapotranspiration, or elevated land surface temperature (Zhu et al., 2024; Jiang et al., 2022). In ecologically fragile transition zones where multiple stressors converge, understanding ecological drought mechanisms becomes critical for anticipating degradation tipping points and designing resilience-based interventions. 

Ecological transition zones amplify environmental variability and thus serve as sentinel systems for drought dynamics. Northern China's Agro-Pastoral Ecotone (APENC)—a 9.1 × 10⁵ km² interface between semi-humid croplands and semi-arid rangelands—exemplifies such vulnerability (Li et al., 2024a). Situated near the northern boundary of the East Asian Summer Monsoon with steep southeast-to-northwest moisture gradients (600–200 mm annual precipitation), APENC functions simultaneously as an ecological security barrier against sandstorm intrusion and a primary agro-pastoral production base (Ding et al., 2023). Large-scale restoration programs initiated since the late 1990s, notably Grain-for-Green, have substantially increased vegetation cover, yet heightened evapotranspiration demands have intensified water-resource pressures, rendering drought risk a binding constraint on both ecological security and sustainable development (Wang et al., 2021; Zhang et al., 2023). This ecohydrological trade-off underscores the urgent need for accurate drought monitoring and mechanistic attribution in such transitional landscapes. 

Despite progress, three fundamental gaps constrain current ecological drought research. First, current remote-sensing drought indices remain limited in capturing vegetation water stress in ecologically heterogeneous regions. The widely used Temperature Vegetation Dryness Index (TVDI), derived from the NDVI–LST feature space, is prone to NDVI saturation under medium- to high vegetation cover and is highly sensitive to soil background signals, which compromises its reliability in complex surfaces such as agropastoral ecotones (Gao et al., 2023). The kernel NDVI (kNDVI) alleviates NDVI saturation and improves sensitivity to vegetation dynamics through nonlinear kernel mapping (Camps-Valls et al., 2021; Wang et al., 2023). Accordingly, we replace NDVI with kNDVI within the traditional TVDI framework to construct kernel Temperature Vegetation Dryness Index (kTVDI), aiming to enhance drought gradient characterization and vegetation stress responsiveness. Nevertheless, systematic evaluation of kTVDI remains scarce, particularly in transition zones with strong vegetation–soil heterogeneity, forming an important motivation for this study. 

Second, mechanistic understanding of drought drivers remains incomplete. Most studies apply conventional statistical approaches—correlation analysis, GeoDetector—that assume linear relationships and struggle to represent complex nonlinear interactions among climatic, topographic, and anthropogenic factors (Zhang et al., 2022a; Newcomb and Godsey, 2023; Yu et al., 2023). Although machine learning models capture nonlinearities effectively, their "black-box" nature hinders mechanistic interpretation (Niazkar et al., 2024; Slater et al., 2025). Emerging explainable AI methods, particularly Shapley Additive Explanations (SHAP), enable principled attribution by quantifying marginal contributions of individual predictors (Lundberg and Lee, 2017; Barredo Arrieta et al., 2020). However, most applications aggregate results regionally, obscuring Land use/Land cover (LULC)-specific mechanisms critical for targeted management. 

Third, nonlinear threshold effects and factor interactions are not consistently quantified across ecosystems. Drought responses can exhibit sharp transitions at critical environmental thresholds—temperature, evapotranspiration, and humidity—indicating shifts in dominant energy–water balance regimes (Li et al., 2023a; Yao et al., 2023). Likewise, synergistic interactions among drivers may amplify or dampen individual effects, yet relatively few studies have systematically identified dominant interaction structures across ecosystems. These gaps can constrain predictive capacity and hinder the translation of research into actionable early-warning systems. To address these deficiencies, we develop an integrated analytical framework coupling a physically enhanced drought index with interpretable machine learning and nonlinear response modeling. Our specific objectives are to: (1) construct kTVDI by integrating the 



**Fig. 1.** Geographical location and land use/land cover (LULC) distribution of the Agro-Pastoral Ecotone of Northern China (APENC). (a) Regional context within China showing major rivers and administrative boundaries. (b) LULC classification map. (c) Areal proportions of each LULC class. 

2 

_Journal of Hydrology: Regional Studies 64 (2026) 103174_ 

kNDVI, and validate its fidelity against dual independent benchmarks—soil moisture (SMCI) and solar-induced chlorophyll fluorescence (SIF)—across LULC types; (2) characterize spatiotemporal drought evolution across APENC (2000–2022) and quantify heterogeneity among ecosystems; (3) identify dominant drivers and their LULC-dependent mechanisms through XGBoost–SHAP attribution; (4) reveal nonlinear thresholds and critical transition points using Generalized Additive Models (GAM); and (5) quantify interaction structures among drivers to elucidate coupled processes governing drought dynamics. By systematically decoding processbased mechanisms with interpretable tools, this study advances fundamental understanding of ecological drought in transition zones and provides a transferable framework for monitoring and managing drought risk in vulnerable ecosystems under global environmental change. 

### **2. Materials and methods** 

### _2.1. Study area_ 

The Agro-Pastoral Ecotone of Northern China (APENC) is a climatically and ecologically transitional belt located between 100<sup>◦</sup> –125<sup>◦</sup> E and 35<sup>◦</sup> –50<sup>◦</sup> N, spanning approximately 9.1 × 10⁵ km² across multiple provincial-level regions in northern China (Fig. 1). This zone represents a critical interface between semi-humid agricultural landscapes in the southeast and semi-arid pastoral rangelands in the northwest, characterized by pronounced environmental gradients and high landscape heterogeneity (Ding et al., 2023). 

Topographically, elevation ranges from _>_ 5000 m in the southwestern Qilian Mountains to _<_ 100 m in the northeastern Songliao Plain, creating complex terrain that modulates local climate and hydrology. Mean annual precipitation exhibits a steep southeast-tonorthwest gradient from 600 mm to 200 mm, with 60–80 % concentrated during the May–September growing season when vegetation activity peaks and water demand intensifies. Mean annual temperature varies from 2<sup>◦</sup> C to 8<sup>◦</sup> C, and frequent wind–sand events exacerbate water–heat mismatches, elevating ecosystem vulnerability (Wei et al., 2018; Wang et al., 2021). 

Dominant soil types include chestnut, loessal, and aeolian sandy soils with variable water-holding capacity. The primary LULC classes are grassland (56.7 %) and cropland (28.9 %), interspersed with forest patches (12.4 %) and desert tracts (2.1 %) (Fig. 1c). Since the late 1990s, large-scale ecological restoration programs—especially Grain-for-Green—have markedly increased vegetation cover. However, enhanced evapotranspiration demand from revegetation has intensified water-resource pressures, making drought risk a key constraint on both ecological security and sustainable agro-pastoral development (Shao et al., 2019; Li et al., 2024a). Functioning as an ecological barrier against sandstorms and land degradation, APENC plays a strategic role in safeguarding northern China's environmental security, rendering accurate drought monitoring and mechanistic understanding imperative for adaptive management. 

### _2.2. Data sources and preprocessing_ 

This study adopts a pixel-based raster analysis framework, with the 1-km grid cell as the fundamental spatial unit of analysis. We assembled multi-source geospatial and hydrometeorological datasets spanning 2000–2022 to characterize ecological drought spatiotemporal patterns and quantify driving mechanisms (Table 1). All datasets were reprojected to the WGS84 geographic coordinate system and resampled to a uniform 1 km spatial resolution. Temporal gaps in gridded products were filled via linear interpolation, while spatially missing pixels were infilled using Inverse Distance Weighted (IDW) interpolation. 

Monthly kNDVI and NDVI were retrieved from NASA's Terra MODIS MOD13A3 product (1 km resolution). Land Surface Temperature (LST) data were obtained from the MOD11A2 product (1 km resolution, 8-day composites) and aggregated to monthly means 

**Table 1** 

Details of the data sources used in this study. 

|Factor name|Data type|Spatial resolution|Period|Source|
|---|---|---|---|---|
|NDVI|Raster|1 km|2000–2022|http://lpdaac.usgs.gov/|
|kNDVI|Raster|1 km|2000–2022|http://lpdaac.usgs.gov/|
|LST|Raster|1 km|2000–2022|http://lpdaac.usgs.gov/|
|DEM|Raster|90 m|2015|http://srtm.csi.cgiar.org/|
|SLO|Raster|90 m|2015|http://srtm.csi.cgiar.org/|
|TEM|Raster|0.01<sup>◦</sup>|2000–2022|http://www.ncdc.ac.cn|
|PRE|Raster|0.01<sup>◦</sup>|2000–2022|http://www.ncdc.ac.cn|
|RH|Raster|0.01<sup>◦</sup>|2000–2022|http://www.ncdc.ac.cn|
|WS|Raster|0.01<sup>◦</sup>|2000–2022|http://www.ncdc.ac.cn|
|SA|Raster|500 m|2000–2022|http://lpdaac.usgs.gov/|
|ET|Raster|500 m|2000–2022|http://lpdaac.usgs.gov/|
|LULC|Raster|30 m|2000–2022|https://zenodo.org/record/4417809|
|HFP|Raster|1 km|2000–2022|https://doi.org/10.1038/s41597–022–01284–8|
|SAND|Raster|90 m|Static|https://doi.org/10.11888/Terre.tpdc.301235|
|CLAY|Raster|90 m|Static|https://doi.org/10.11888/Terre.tpdc.301235|
|SMCI|Raster|1 km|2000–2022|https://data.tpdc.ac.cn/zh-hans/data/49b22de9–5d85–44f2-a7d5-a1ccd17086d2<br>i|
|SIF|Raster<br>i|0.05<sup>◦</sup>|2001–2022|https://figshare.com/articles/dataset/RTSIF_dataset/19336346/4|
|Boundary|Shapefile|—|—|http://bzdt.ch.mnr.gov.cn/|



_Note:_ Full names of all abbreviated variables are provided in the List of Abbreviations at the end of the manuscript. 

3 

_Journal of Hydrology: Regional Studies 64 (2026) 103174_ 

_Y. Fan et al.                                                                                                                                                                                                             Journal of Hydrology: Regional Studies_ 

by averaging all available observations within each calendar month. 

To clarify predictor preselection and model input construction, we first compiled a candidate set of driving factors based on ecohydrological theory and regional drought literature. We then applied variance inflation factor (VIF) screening (VIF ≥ 5) to remove collinear variables, yielding a final set of 11 predictors used in the XGBoost modeling (Fig. S1). These predictors cover five key 



**Fig. 2.** The framework of the study. 

4 

_Journal of Hydrology: Regional Studies 64 (2026) 103174_ 

_Y. Fan et al.                                                                                                                                                                                                             Journal of Hydrology: Regional Studies_ 

domains: topography, climate, surface energy, anthropogenic pressure and soil, providing consistent annual inputs for the subsequent kTVDI–driver analysis. Time-varying predictors that were not originally annual were aggregated to annual summary values, whereas time-invariant predictors were treated as constants and duplicated annually to ensure spatiotemporal consistency with the 2000–2022 kTVDI series. 

Topographic variables, namely elevation and slope, were derived from the Shuttle Radar Topography Mission (SRTM) digital elevation model (DEM; 90 m resolution). Slope was calculated from the DEM using standard surface analysis tools in ArcGIS Pro. Climate variables—mean temperature (TEM), precipitation (PRE), relative humidity (RH), and wind speed (WS)—were acquired as annual gridded products from the National Cryosphere Desert Data Center (Hu and Zhang, 2024).To represent surface energy processes, surface albedo (SA; from MCD43A3, 500 m, daily) and actual evapotranspiration (ET; from MOD16A2GF, 500 m, 8-day) were processed. They were first aggregated to monthly mean values for quality control and temporal consistency, then averaged to annual means for long-term analysis. Anthropogenic pressure was characterized by the Human Footprint index (HFP; 1 km, annual), which integrates eight pressure variables (e.g., population density, built-up fraction) into a standardized composite index (Mu et al., 2022). Soil properties, specifically sand (SAND) and clay (CLAY) content, were obtained from the China Soil Properties Dataset version 2 (CSDLv2) (Shi et al., 2025). All datasets were then reprojected to the WGS84 coordinate system, resampled to a 1 km resolution, and prepared as annual layers to maintain spatiotemporal consistency for the 2000–2022 modeling period. 

Annual LULC maps at 30 m resolution were obtained from the China Land Cover Dataset (Yang and Huang, 2021). To match the 1 km analysis resolution, the fractional coverage (i.e., area proportion) of each LULC class was computed based on the count of constituent 30-m pixels within every 1 km grid cell. Cells with a purity _>_ 80 % were assigned the dominant LULC class, resulting in four broad categories: cropland, forest, grassland, and desert. To isolate the intrinsic drought-response mechanisms attributable to LULC types, all subsequent LULC-specific trend and mechanism analyses were conducted exclusively on pixels whose dominant class remained stable from 2000 to 2022. 

For independent validation, we employed the Soil Moisture of China by in situ data (SMCI) v1.0 dataset (0–10 cm depth, 1 km, daily) (Li et al., 2022a), which assimilates _>_ 1600 in situ stations. In addition, we used the SIF product, a machine-learning–reconstructed TROPOMI SIF dataset (0.05<sup>◦</sup> , 8-day) that has been validated against tower-based SIF and other satellite SIF products (e.g., GOME-2, OCO-2), as a complementary benchmark of vegetation photosynthetic activity (Chen et al., 2022a). For validation purposes, both the daily SMCI and 8-day SIF datasets were aggregated to monthly mean values by averaging all observations within each calendar month. Administrative boundaries were obtained from the National Geomatics Center of China. 

### _2.3. Methods_ 

To systematically analyze the spatiotemporal Patterns and driving mechanisms of ED in APENC, this study constructed a comprehensive analytical framework (Fig. 2). This framework begins with the collection and preprocessing of multi-source data, followed by the construction and validation of kTVDI. Subsequently, we employed trend analysis methods to reveal the spatiotemporal evolution patterns of kTVDI. Finally, by integrating interpretable machine learning (XGBoost–SHAP) and GAM, we quantified the driving contributions, nonlinear responses, and interaction effects of multiple factors. The key methods in this framework are elaborated below. 

### _2.3.1. kTVDI Drought Index: Construction and Validation_ 

The kNDVI effectively mitigates saturation and mixed-pixel issues inherent in traditional NDVI, demonstrating enhanced stability and robustness, particularly in grasslands, croplands, mixed forests, and arid regions (Camps-Valls et al., 2021). To construct kTVDI, we replaced NDVI with kNDVI in the classical TVDI framework. Using a step size of 0.001, maximum and minimum LST values corresponding to each kNDVI interval were extracted to construct the LST–kNDVI feature space for APENC (2000–2022). Dry and wet edge equations were determined via linear regression as follows: 



|_T_max =_a_1+_b_1|×_kNDVI_<br>(2)|
|---|---|



|_T_min =_a_2+_b_2×_kNDVI_|(3)|
|---|---|



where Ts is observed LST, Tmax and Tmin represent maximum and minimum LST for a given kNDVI bin (dry and wet edges, respectively), and a1, a2, b1, b2 are regression coefficients. The kTVDI ranges from 0 to 1, with higher values indicating more severe drought. Drought intensity was classified as severe (0.8–1.0), moderate (0.6–0.8), mild (0.4–0.6), or no drought (0–0.4) (Ding et al., 2024). 

To comprehensively evaluate the ecological validity of kTVDI, we adopted a dual validation framework that considers both soilmoisture stress and vegetation physiological response during the growing season (May–September). Given that ecological drought in this region is primarily manifested as soil-moisture deficits constraining vegetation growth (Cui et al., 2024; Zhu et al., 2024), we used the high-accuracy SMCI dataset as the primary independent benchmark to test whether kTVDI and traditional TVDI can capture the ecohydrological dimension of drought driven by soil-water deficits, while satellite-derived SIF was introduced as a complementary indicator of canopy photosynthetic response to water stress. For APENC as a whole and for each LULC type, we quantified the associations between the drought indices and the validation datasets using Spearman’s rank correlation—selected because these 

5 

_Journal of Hydrology: Regional Studies 64 (2026) 103174_ 

relationships are typically non-normal, nonlinear yet monotonic (Zhang et al., 2021; Okoduwa et al., 2025)—and derived 95 % confidence intervals for the correlation coefficients via nonparametric bootstrap resampling to assess their strength, significance and uncertainty. 

### _2.3.2. Spatiotemporal trend analysis_ 

To quantify the interannual drought trends in the APENC from 2000 to 2022, we applied the non-parametric Theil–Sen median estimator in combination with the Mann–Kendall significance test (Chen et al., 2025). This robust approach mitigates the impact of outliers and does not assume the data follow a normal distribution. 

The Theil–Sen median slope (β), also known as Sen's slope, was calculated on a pixel-by-pixel basis to determine the magnitude of the kTVDI trend. It is defined as the median of all pairwise slopes in the time series: 



where β represents the interannual change rate of kTVDI; Median denotes the median of a series of data; xi and xj represent the data values for year i and year j in the time series, respectively; β _>_ 0 indicates an increasing trend, while β _<_ 0 indicates a decreasing trend. Subsequently, the Mann–Kendall method was used to statistically assess the significance of the Theil–Sen median trend. The Mann–Kendall method is a non-parametric statistical test proposed by Mann and Kendall, aimed at determining the significance of trend changes in time series data (Zhang et al., 2022b). This method does not require the data to follow a normal distribution and is resilient to the effects of outliers. The specific calculation formulas are as follows: 



where n represents the length of the time series. When the values meet the criteria of being independent and identically distributed, the variance can be calculated using the following formula: 



When n ≥ 10, S approximately follows a normal distribution, and the standardized Z statistic is obtained through standardization. The calculation expression is: 



When |Z| ≥ 1.96, it is considered to have reached the 95 % significance level. 

### _2.3.3. Extreme Gradient Boosting (XGBoost)_ 

XGBoost is an ensemble learning algorithm that combines additive trees with forward stepwise optimization, iteratively constructing decision trees to minimize prediction residuals while incorporating L1 and L2 regularization to prevent overfitting (Chen and Guestrin, 2016). We constructed separate XGBoost models for cropland, forest, grassland, desert, and the entire APENC region, using kTVDI as the response variable and the 11 driving factors retained after VIF diagnostics (VIF _<_ 5) — TEM, PRE, RH, WS, ET, SA, HFP, DEM, SLO, SAND, and CLAY — as predictors (Fig. S1). Data were split 70/30 into training and independent test sets. Model hyperparameters were optimized via 10-fold cross-validation on the training set, and generalization performance was evaluated using R², RMSE, and MAE on the held-out test set. To ensure reproducibility, the final optimized hyperparameters for both the overall APENC model and the models for each LULC type are fully listed in the Supplementary Materials (Table S1). 

To further assess the robustness of the selected driver set and quantify the relative importance of each predictor from a modelperformance perspective, we conducted a leave-one-feature-out sensitivity analysis for the overall APENC model. Specifically, using the baseline model containing all 11 predictors as a reference, we iteratively removed one predictor at a time and retrained the model under identical conditions (i.e., fixed train/test split, random seed, and hyperparameters), without re-tuning hyperparameters. The relative change in test-set RMSE was then computed as: ΔRMSE% = (RMSE_omit − RMSE_base) / RMSE_base × 100%. A larger positive ΔRMSE% indicates a greater loss of predictive skill when that predictor is omitted, thereby reflecting its higher marginal contribution to model performance. This analysis provides an independent, performance-based validation of the driver selection and offers evidence corroborating the importance patterns inferred from SHAP analysis (Fig. S2). Since omitting any of these predictors consistently degraded model performance (ΔRMSE% _>_ 0), we retained all 11 drivers that passed the initial VIF screening, confirming their collective value for explaining kTVDI variability. 

6 

_Journal of Hydrology: Regional Studies 64 (2026) 103174_ 

_Y. Fan et al.                                                                                                                                                                                                             Journal of Hydrology: Regional Studies_ 

### _2.3.4. Shapley Additive ExPlanations (SHAP)_ 

Although machine-learning models such as XGBoost exhibit strong nonlinear predictive capability, their internal decision-making processes are often treated as a “black box,” limiting mechanistic interpretation. To quantify the specific contribution of each driver to kTVDI predictions and clarify its direction of influence, we employed the game-theoretic SHAP (SHapley Additive exPlanations) framework (Lundberg and Lee, 2017). SHAP values compute the average marginal contribution of a given feature to the model output across all possible feature coalitions, providing a unified and theoretically sound measure of each predictor’s influence on individual predictions. In this study, positive SHAP values indicate that a factor increases kTVDI (intensifies drought), whereas negative SHAP values indicate that a factor decreases kTVDI (alleviates drought). All SHAP analyses were conducted on the independent test set reserved after model training to ensure objectivity and avoid bias. 

To further unravel the coupling mechanisms among multiple drivers, we computed SHAP interaction values to quantify synergistic effects between predictor pairs. However, absolute interaction strength is biased toward factors with strong main effects. To enable fair comparison, we introduce a normalized metric—Relative Interaction Strength (Ri,j): 



where Ii,j is the mean absolute SHAP interaction value for factors i and j, and Mi, Mj are their respective main effects. Expressed as a percentage, Ri,j objectively reflects interaction importance independent of main-effect magnitude, facilitating identification of dominant coupled processes within each LULC type. 

### _2.3.5. Generalized Additive Model (GAM)_ 

While SHAP effectively identifies key drivers, it does not intuitively reveal the shape of their continuous, nonlinear relationships with the drought index. To address this, we employed GAM. As an extension of Generalized Linear Models (GLM), GAM captures complex nonlinear trends by replacing the linear predictors with smooth functions of the independent variables, thereby breaking the rigid assumptions of linear models while retaining interpretability (Hastie and Tibshirani, 1990; Wood, 2017). The core formulation of a GAM is: 



Where g(u) is the link function, β0 is the intercept term, and fk(xk) is the smooth function of the independent variable xk. 

In this study, for the top-ranked drivers identified by SHAP, we fitted GAMs to model the relationship between the original values of 



**Fig. 3.** Validation of kTVDI against traditional TVDI and independent soil moisture (SMCI) during the growing season across LULC types. (a) Cropland. (b) Forest. (c) Grassland. (d) Desert. (e) Regional (APENC). Each panel shows three-way correlations among TVDI, kTVDI, and SMCI, with Spearman’s ρ, its bootstrap 95 % confidence interval (CI), and the p-value provided for each pair. 

7 

_Journal of Hydrology: Regional Studies 64 (2026) 103174_ 

_Y. Fan et al.                                                                                                                                                                                                             Journal of Hydrology: Regional Studies_ 

the driving factors and their corresponding SHAP values. This approach allows for a deep analysis of the nonlinear dependency between each factor and kTVDI, helping to reveal critical thresholds that mark regime shifts in energy-water balance mechanisms. 

### **3. Results** 

### _3.1. Enhanced sensitivity of kTVDI for ecological drought monitoring_ 

Validation against independent soil moisture data demonstrated kTVDI's superior performance over traditional TVDI (Fig. 3). At the pixel scale, kTVDI and TVDI exhibited extremely high correlations across the entire APENC and all LULC types (Spearman's ρ = 0.93–0.98), confirming that kTVDI reliably inherits the spatial drought gradient information embedded in the classical NDVI–LST feature space. More importantly, kTVDI showed significantly stronger negative correlation with SMCI region-wide (ρ = − 0.604) compared to TVDI (ρ = − 0.533), indicating closer alignment with true soil moisture dynamics. This superiority persisted across LULC classes. In cropland, the kTVDI–SMCI correlation (ρ = − 0.481) exceeded the TVDI–SMCI correlation (ρ = − 0.418). Forest showed similar patterns (kTVDI: ρ = − 0.509; TVDI: ρ = − 0.454). Grassland exhibited the strongest correlations overall, with kTVDI (ρ = − 0.619) outperforming TVDI (ρ = − 0.553), reflecting shallow root systems and strong dependence of vegetation status on surface moisture. Desert showed the weakest absolute correlations (kTVDI: ρ = − 0.415; TVDI: ρ = − 0.402) due to low vegetation cover and 



**Fig. 4.** Regional drought patterns in APENC. (a) Spatial distribution of mean kTVDI (2000–2022) and areal proportions of drought classes. (b) Spatial distribution of the significance of kTVDI trends (Mann–Kendall test) based on Theil–Sen slopes, together with the areal proportions of change categories. (c) Interannual variation of the regional mean kTVDI with standard-deviation bars and the fitted linear trend. 

8 

_Journal of Hydrology: Regional Studies 64 (2026) 103174_ 

_Y. Fan et al._ 

high soil optical/thermal variability, though kTVDI remained superior. All correlations reported here are significant at p _<_ 0.001. These results provide a robust soil-moisture-based foundation for the subsequent spatiotemporal analysis and mechanism investigation. 

The SIF-based validation is highly consistent with the SMCI-based findings: at the regional scale, kTVDI shows a stronger negative correlation with SIF (Spearman’s ρ = − 0.530) than TVDI (ρ = − 0.460). This advantage is most pronounced in grassland and desert, 



**Fig. 5.** Spatiotemporal trends and interannual variability of kTVDI by LULC types in the APENC. Panels (a–d) show Theil–Sen slopes, (e–h) annual mean kTVDI (±SD) with fitted linear trends, and (i–l) Mann–Kendall Z-statistics for cropland (a,e,i), forest (b,f,j), grassland (c,g,k) and desert (d,h,l); blue pixels indicate locations with significant trends (p _<_ 0.05). 

9 

_Journal of Hydrology: Regional Studies 64 (2026) 103174_ 

with Δρ improvements of 0.07 and 0.06, respectively, whereas in forest the two indices exhibit nearly identical correlations with SIF (Fig. S3). 

Overall, the dual validation using SMCI (surface soil-moisture stress) and SIF (canopy photosynthetic response) demonstrates that kTVDI is tightly coupled with ecological drought processes in both hydrological and eco-physiological dimensions. Compared with traditional TVDI, kTVDI not only preserves the sensitivity of the NDVI–LST feature space to surface wetness, but also exhibits higher responsiveness to soil moisture and vegetation functional changes across multiple LULC types, thus representing a more suitable remote-sensing indicator for ecological drought monitoring in the APENC. Moreover, the bootstrap-based uncertainty assessment further indicates that these relationships remain significant and robust across all LULC types. 

### _3.2. Spatiotemporal drought evolution reveals regional heterogeneity_ 

### _3.2.1. Overall regional patterns_ 

Across APENC during 2000–2022, the regional mean annual kTVDI declined significantly (− 1.328 × 10⁻³ yr⁻¹, p _<_ 0.01), indicating overall drought alleviation and a gradual improvement in surface moisture conditions (Fig. 4c). Interannual variability, however, remained pronounced: severe drought occurred in 2000, 2001, and 2004 (mean kTVDI = 0.647, 0.648, and 0.650, respectively). By 2013, the mean kTVDI decreased to 0.596; after 2019, it stabilized around 0.602–0.608, suggesting reduced drought severity and partial recovery of soil moisture and vegetation in recent years. 

Spatial patterns exhibited marked heterogeneity (Fig. 4a). Mild and moderate drought dominated—32.7 % and 59.0 % of the area, respectively—together exceeding 90 %. Severe drought covered 4.3 %, concentrated in desert and desert-transition zones, whereas non-drought areas comprised 4.0 %, primarily within protected forest reserves (Greater Khingan Mountains, Saihanba, and Qilian Mountains National Forest Parks). Trend analysis highlighted contrasting changes (Fig. 4b): 39.8 % of the region showed significant or highly significant alleviation (p _<_ 0.05), mainly in the northeastern and southern sectors, while 8.0 % exhibited significant or highly significant intensification (p _<_ 0.05), centered on the Ordos Plateau and Tengger Desert. 

### _3.2.2. LULC-specific drought dynamics_ 

Over the past two decades, all vegetated LULC types demonstrated significant drought alleviation, though rates differed markedly (Fig. 5). Forest showed the fastest decline (− 2.405 × 10<sup>-</sup> ³ yr<sup>-</sup> ¹), followed by cropland (− 1.973 × 10<sup>-</sup> ³ yr<sup>-</sup> ¹) and grassland (− 8.028 × 10<sup>-</sup> ⁴ yr<sup>-</sup> ¹). In contrast, desert areas displayed a slight, non-significant increasing trend with pronounced interannual fluctuation. Mean 



**Fig. 6.** XGBoost model performance on independent test sets. Scatter plots show predicted vs. reference kTVDI with performance metrics for (a) cropland, (b) forest, (c) grassland, (d) desert, and (e) APENC. Color gradients indicate point density. 

10 

_Y. Fan et al.                                                                                                                                                                                                             Journal of Hydrology: Regional Studies 64 (2026) 103174_ 

kTVDI values ranked forest (0.513 ± 0.127) _<_ cropland (0.630 ± 0.088) _<_ grassland (0.636 ± 0.119) _<_ desert (0.755 ± 0.178), indicating that forests possessed stronger drought resistance and were relatively less sensitive to water stress over the 23-year period, while deserts remained most susceptible. 

Spatial heterogeneity within LULC classes mirrored regional patterns. In cropland, 39.40 % of the area exhibited significant kTVDI decrease, concentrated in the Northeast Plain, while 3.18 % showed significant increase, primarily on the northern Loess Plateau. Forest demonstrated the most prominent alleviation, with 62.07 % of area showing significant decrease, especially in the Greater Khingan Mountains. Grassland displayed 20.85 % significant decrease (southern Loess Plateau, forest–grassland transition zones) and 8.01 % significant increase (northern Loess Plateau, Ordos Plateau). Distinct from vegetated systems, deserts exhibited differentiated evolution, with substantial kTVDI increase concentrated in the southern Kubuqi Desert, which emerged as a prominent hotspot for drought intensification. 

### _3.3. Drought Driving Mechanisms in the APENC_ 

### _3.3.1. XGBoost model performance_ 

XGBoost models achieved robust predictive accuracy across all LULC types and the entire region (Fig. 6), with test-set R² ranging from 0.8698 (cropland) to 0.9758 (desert). Desert exhibited the highest performance (R² = 0.9758, RMSE = 0.0289, MAE = 0.0218), indicating high sensitivity to driver changes and model stability. The regional model achieved R² = 0.9113 (RMSE = 0.0364, MAE = 0.0279), demonstrating robust fitting capability. Detailed training and test performance metrics for each LULC type are summarized in Table S2. These results confirm that XGBoost effectively captures complex nonlinear relationships between kTVDI and multidimensional drivers, providing a solid foundation for SHAP-based attribution, nonlinear analysis, and interaction quantification. 

### _3.3.2. Identification of dominant drivers_ 

SHAP analysis revealed TEM as the most pervasive driver across all models, with mean absolute SHAP contributions ranging from 32.92 % to 52.24 % (Fig. 7). Importance was highest in forest (52.24 %) and relatively lower in desert (32.92 %). Beeswarm plots indicate that higher TEM increase kTVDI (positive SHAP values), consistent with stronger atmospheric evaporative demand and intensified moisture stress. Furthermore, the leave-one-feature-out sensitivity analysis (Fig. S2) showed that omitting TEM caused the largest deterioration in model predictive performance (ΔRMSE% = +26.09 %), which is consistent with TEM being identified as the dominant driver by the SHAP analysis. 

Beyond temperature, secondary drivers varied systematically by LULC. For the entire APENC, ET, SA, and RH emerged as secondary core factors, while WS, HFP, and SLO played weaker roles. Low ET values concentrated in positive SHAP ranges, indicating that water scarcity and reduced ET exacerbate drought; conversely, high ET values aligned with negative SHAP values, reflecting latent heat cooling and drought alleviation when water is sufficient. High SA values consistently corresponded to positive SHAP values, reflecting the feedback loop whereby drought-induced vegetation degradation increases surface exposure and albedo, further intensifying 



**Fig. 7.** Integrated SHAP summary plots showing driver importance and effect direction on kTVDI across LULC types and the APENC. (a) Cropland. (b) Forest. (c) Grassland. (d) Desert. (e) APENC. Each panel overlays beeswarm plots (colored by feature value) with horizontal bars showing mean | SHAP| values, with percentages indicating relative contributions within each panel. 

11 

_Journal of Hydrology: Regional Studies 64 (2026) 103174_ 

_Y. Fan et al._ 

moisture stress. High RH values showed dense negative SHAP distributions, indicating that elevated atmospheric moisture capacity suppresses evaporative water loss and alleviates drought, while low RH accelerates water depletion. 

LULC-specific patterns revealed fundamental mechanistic differences. In cropland, DEM emerged as _a_ secondary core factor, with mid-to-high elevations more prone to drought and low-altitude areas experiencing relatively lighter stress. ET followed the universal pattern of high values alleviating and low values exacerbating drought. In forest, TEM dominated most strongly (52.24 %), with ET maintaining its dual role. Grassland mechanisms resembled cropland and forest, with TEM as the primary driver and ET showing consistent water-dependent effects. In desert, TEM's dominance declined relatively (32.92 %), while PRE became the second core factor—high values alleviated drought and low values exacerbated it, reflecting a system where water input depends critically on precipitation and loss is energy-controlled. Overall, LULC types fundamentally reshape non-TEM drivers' influence on kTVDI by modulating surface cover, water cycling, and energy balance processes, demonstrating clear mechanistic dependence on ecosystem structure. 

### _3.3.3. Spatial Contribution and Nonlinear Thresholds of Dominant Drivers_ 

Pixel-level SHAP spatial distributions revealed marked regional heterogeneity in how dominant factors affect drought (Fig. 8). TEM exacerbated drought across most regions, with stronger effects in the central Loess Plateau and along the southern margin, but predominantly alleviated drought in the northeastern Greater Khingan Mountains. ET and RH exhibited zonal changes along the southeast-northwest moisture gradient—primarily alleviating drought in the humid southeast, gradually shifting to exacerbation toward the arid northwest as moisture availability diminished. DEM effects varied with topography, alleviating drought in eastern plains while exacerbating it on medium-high hills of the west and Loess Plateau. CLAY exacerbated drought on the Loess Plateau but alleviated it in most other areas with higher clay fractions. SA generally exacerbated drought region-wide. This spatial heterogeneity underscores the importance of local biophysical context in modulating drought mechanisms. 

GAM nonlinear fitting identified critical thresholds marking regime shifts in energy–water balance mechanisms (Fig. 9). Across models, the GAM fits achieved high explanatory power (pseudo R² = 0.7235–0.9860, p _<_ 0.001), confirming robust nonlinear relationships. TEM exhibited a critical point at approximately 6.6<sup>◦</sup> C, below which it was associated with lower drought intensity (negative SHAP values) and above which it increased drought intensity (positive SHAP values). This threshold likely reflects the transition from energy-limited to water-limited regimes, where higher temperatures elevate vapor pressure deficit and intensify evaporative demand. ET showed a turning point near 387 mm yr⁻¹ —values below this threshold intensified drought (positive SHAP), while those above it mitigated drought (negative SHAP). Although different from precipitation, this threshold is functionally adjacent to the commonly referenced 400 mm annual precipitation isohyet in China, both marking the transition from energy- to water-limited systems (Li et al., 2024b). It is noteworthy that these regional-scale turning points exhibit systematic variations across LULC types 



**Fig. 8.** Spatial distribution of SHAP values for dominant drivers. (a) Temperature (TEM). (b) Evapotranspiration (ET). (c) Surface albedo (SA). (d) Relative humidity (RH). (e) Elevation (DEM). (f) Clay content (CLAY). Warm colors indicate drought exacerbation (positive SHAP), cool colors indicate alleviation (negative SHAP). 

12 

_Journal of Hydrology: Regional Studies 64 (2026) 103174_ 

_Y. Fan et al.                                                                                                                                                                                                             Journal of Hydrology: Regional Studies_ 



**Fig. 9.** GAM-fitted nonlinear relationships between key drivers and their SHAP values for kTVDI in APENC. (a) Temperature (TEM). (b) Evapotranspiration (ET). (c) Surface albedo (SA). (d) Relative humidity (RH). (e) Clay content (CLAY). (f) Elevation (DEM). Shaded bands represent 95 % confidence intervals, and gray dashed lines indicate identified tipping points. 

(Table S3). For instance, the TEM threshold for drought response is lowest in forests (5.9<sup>◦</sup> C) and highest in deserts (7.6<sup>◦</sup> C). In contrast, the ET threshold is highest in forests (502 mm yr⁻¹) and lowest in deserts (277 mm yr⁻¹). These patterns suggest that ecosystem structure and water-use strategies may modulate nonlinear responses to climatic drivers, contributing to LULC-dependent threshold behaviors. 

Beyond temperature and evapotranspiration, SA, RH, DEM, and CLAY also exhibited pronounced nonlinear threshold responses (Fig. 9). SA demonstrated a complex dual-threshold response at approximately 0.154 and 0.257, characterized by initial drought inhibition, followed by promotion, then re-inhibition. This nonlinearity reflects competing radiative effects—moderate albedo reduces net radiation and sensible heat flux (alleviating drought), but very high albedo indicates severe vegetation loss that overwhelms radiative benefits. RH exhibited a turning point around 54.2 %, below which it exacerbated drought and above which it alleviated drought by suppressing atmospheric evaporative demand. DEM displayed a three-stage, dual-threshold pattern, alleviating drought at lower elevations ( _<_ 1412 m) and very high elevations ( _>_ 4094 m), but exacerbating it at medium-high elevations (1412–4094 m). This pattern reflects elevation-dependent energy-water coupling: low elevations feature higher vegetation cover and latent-heat dominance; mid-elevations exhibit increased soil exposure, higher albedo, and sensible-heat dominance; high elevations experience energy limitation that again favors moisture retention. CLAY showed a threshold at approximately 15.4 %—low fractions promoted drought through reduced water-holding capacity, while high fractions alleviated drought via enhanced infiltration and retention. These quantitative thresholds provide mechanistic benchmarks for drought zoning, early-warning systems, and targeted management interventions. 

### _3.3.4. Interaction Effects of Driving Factors under Different LULC Types_ 

SHAP interaction analysis uncovered distinct factor coupling structures across LULC types (Fig. 10). Absolute interaction matrices (Fig. S4) showed that TEM-related pairs generally dominated, underscoring TEM's universal role as an energy-forcing driver. However, relative interaction strength—normalized by main effects—revealed LULC-specific dominant synergies that absolute metrics obscure. 

In cropland, interactions emphasized humidity-soil/topography synergies, with core pairs being RH × SAND (14.28 %), DEM × RH (10.98 %), and HFP × CLAY (10.49 %), while SLO-related pairs showed negligible impact. This pattern reflects the importance of moisture availability modulated by soil texture and terrain for agricultural water stress, with human activities (irrigation, tillage) coupled through soil property modifications. Forest exhibited balanced soil-topography/turbulence interactions, with prominent pairs SAND × CLAY (16.98 %), DEM × SAND (14.24 %), HFP × CLAY (12.65 %), and WS × RH (12.54 %). The strong wind-humidity coupling highlights canopy-atmosphere energy-water exchange processes critical in forest systems. Grassland displayed dualdominant soil-humidity coupling, typified by RH × SAND (15.58 %) and SAND × CLAY (12.83 %), with DEM × SAND (11.30 %) indicating topographic reinforcement of soil processes. This structure reflects grassland sensitivity to surface moisture availability controlled by soil texture and atmospheric humidity, with terrain modulating local hydrology. 

13 

_Journal of Hydrology: Regional Studies 64 (2026) 103174_ 



**Fig. 10.** Relative interaction strength matrices for driver pairs across LULC types. (a) Cropland. (b) Forest. (c) Grassland. (d) Desert. Circle size and color intensity indicate normalized interaction importance (%), revealing dominant coupled processes within each ecosystem independent of maineffect magnitude. 

Desert revealed a topography-centered network wherein DEM coupled strongly with HFP (10.91 %) and PRE (10.51 %), along with significant ET × WS (9.46 %) and HFP × PRE (8.94 %) interactions. This pattern indicates that in systems lacking vegetation buffering, topography becomes the dominant structural control modulating both anthropogenic disturbance impacts and precipitation effectiveness. The prominence of HFP-related interactions underscores that human activities exert amplified impacts on drought in arid environments, with influence magnitudes comparable to key natural factors. Overall, relative interaction strength effectively identifies dominant driver combinations and their structural hierarchy within each LULC type, demonstrating that drought responses emerge from ecosystem-specific synergistic processes rather than simple additive effects. 

14 

_Journal of Hydrology: Regional Studies 64 (2026) 103174_ 

### **4. Discussion** 

### _4.1. Enhanced monitoring capability of kTVDI and its LULC-dependent performance_ 

The superior performance of kTVDI stems from its use of kNDVI, which effectively mitigates spectral saturation and soilbackground noise under medium-to-high vegetation cover (Camps-Valls et al., 2021). This modification enhances the delineation and spatiotemporal stability of wet and dry edges in the LST–vegetation feature space, thereby improving sensitivity to soil-moisture stress. The performance of kTVDI is substantially enhanced across the APENC, as confirmed by dual validation against independent datasets (SMCI and SIF): it exhibits significantly stronger correlations with both indicators than traditional TVDI. These results demonstrate that kTVDI is more closely coupled with surface hydrological processes and more responsive to drought-induced constraints on vegetation physiology. By concurrently capturing soil-moisture stress and canopy photosynthetic response, kTVDI more faithfully represents the coupled dynamics of the soil–vegetation continuum during ecological drought, providing a more reliable and process-oriented remote-sensing indicator. 

kTVDI’s LULC-dependent performance is explained by ecosystem-specific water–energy coupling mechanisms. In forests, the correlation between kTVDI and SMCI was relatively weak, primarily due to the decoupling of surface temperature from shallow soil moisture caused by deep-root water uptake and canopy effects (Christina et al., 2017; Flores and Staal, 2022). Simultaneously, validation based on SIF also showed low correlations, reflecting the buffered, nonlinear drought response of forest photosynthesis that SIF captures. In grasslands, kTVDI exhibited stronger correlations with both SMCI and SIF, consistent with shallow root systems, strong surface-moisture dependence and rapid response to water-availability dynamics (O'Connor et al., 2021; Chen et al., 2020), which enables kTVDI to better track swift changes in both soil moisture and canopy photosynthetic function during drought. In croplands, irrigation, drainage and tillage practices alter natural water–energy coupling, yet kTVDI remained more robust than TVDI against both SMCI and SIF, demonstrating stronger resistance to management-induced signal noise (Fan et al., 2023; Yuan et al., 2023). In deserts, kTVDI showed the weakest absolute correlations with SMCI due to low vegetation cover, high soil optical and thermal variability and greater soil-moisture uncertainty, although it still outperformed TVDI (Chen et al., 2022b; Konkathi and Karthikeyan, 2022). By contrast, its correlation with SIF was relatively higher, which may reflect the fact that the detectable SIF signal—and thus the statistical relationship—is dominated by sparse vegetated patches where water stress and photosynthesis are tightly coupled. 

These LULC-dependent patterns, elucidated through dual validation with SMCI and SIF, underscore that kTVDI serves as a more reliable and mechanistically informative tool for regional ecological drought monitoring in heterogeneous transition zones, providing a robust foundation for spatiotemporal analysis and mechanism investigation. 

### _4.2. Mechanistic drivers of spatially heterogeneous drought patterns_ 

The observed juxtaposition of overall regional drought alleviation with localized northwestern intensification reflects a multi-scale interplay between climatic forcing and land-surface feedbacks. The spatial template is primarily shaped by the moisture gradient and transition-zone threshold effects jointly determined by monsoon dynamics and topography. Located near the northern boundary of the East Asian Summer Monsoon (EASM), APENC experiences rapid southeast-to-northwest moisture decline constrained by the uplift and barrier effects of the northeastern Tibetan Plateau and the Loess-Inner Mongolia Plateau complex (Ren et al., 2021; Hu et al., 2016; Guo et al., 2017). Consequently, eastern and northeastern regions lie in more favorable moisture pathways and windward positions, prone to sustained drought reduction, while the northwestern fringe persistently experiences a water-balance structure characterized by weak supply and strong evapotranspiration demand, rendering it highly sensitive to precipitation and temperature anomalies (Li et al., 2024b). Simultaneously, the transition zone's proximity to the humid-semi-arid threshold means that slight advances or retreats of the EASM northern boundary can trigger nonlinear amplification of moisture transport and precipitation (Qian et al., 2012; Chen et al., 2018), reinforcing the spatial pattern of overall relief with northwestern fringe sensitivity, consistent with independent studies on monsoon-boundary migration and ecological vulnerability zones (Wang et al., 2022a). 

Upon this climatic template, human activities and land-surface feedbacks determine the differentiation and persistence of alleviation zones versus intensification hotspots. Core drought-reduction areas highly overlap with focal regions of ecological restoration implementation over the past two decades—notably the Northeast Plain and southern Loess Plateau. Vegetation restoration establishes positive feedback loops of cooling, moisture conservation, and drought reduction by increasing surface roughness and evapotranspiration, reducing sensible heat flux, and improving infiltration and soil water retention (Wang et al., 2018; Ren et al., 2016; Qiu et al., 2022). Agricultural irrigation provides external water supplementation during high-temperature drought periods, peak-shaving water deficits and shortening drought duration, with canal networks expanding point signals into patchy alleviation (Li et al., 2023b). Conversely, sandy regions such as Ordos-Kubuqi-Mu Us-Tengger, under long-term drought background, feature low water retention, high albedo, and low vegetation cover, preventing precipitation from transforming into effective root-zone water. High albedo elevates land surface temperature, increasing atmospheric evaporative demand and forming a self-reinforcing loop characterized by short supply and prolonged deficit with significant memory effects (Scanlon et al., 2006; Luo et al., 2019; Sun et al., 2021), thereby solidifying and amplifying intensification hotspots (Li et al., 2022b; Wang and Yuan, 2022; Zeng and Yuan, 2024). In summary, the overall relief-hotspot intensification drought pattern in APENC represents a product of pattern-process coupling wherein large-scale climatic forcing defines the risk background while local biophysical and anthropogenic processes, conditioned by initial LULC types, ultimately shape drought manifestation and evolution through specific water-energy regulation and feedback mechanisms. 

15 

_Journal of Hydrology: Regional Studies 64 (2026) 103174_ 

_Y. Fan et al._ 

### _4.3. Nonlinear mechanisms and LULC-dependent drought responses_ 

The integrated XGBoost-SHAP-GAM framework successfully decoded the complex, nonlinear, multi-factor mechanisms underlying ecological drought in APENC. TEM emerged as the most universal driver region-wide, consistent with its fundamental role in controlling vapor pressure deficit and evapotranspiration demand (Scheff and Frierson, 2014; Grossiord et al., 2020). However, LULC types substantially modified the ranking and direction of secondary drivers, demonstrating ecosystem-dependent control hierarchies. In vegetated systems (cropland, forest, grassland), ET served as the key hydrological connector—alleviating drought via latent-heat cooling when water is sufficient, but exacerbating stress under water limitation (AghaKouchak et al., 2014). In deserts, PRE replaced ET as the second-ranked factor, reflecting a system dominated by water input variability and energy-controlled evaporative loss (Zhang et al., 2017). HFP also exhibited LULC-dependent effects, with amplified disturbance impacts in deserts where vegetation buffering is minimal, underscoring the complexity of anthropogenic interventions across ecosystems (Xiao et al., 2023). 

GAM-based threshold analysis revealed critical transition points marking shifts among dominant energy-water-surface process regimes. The TEM threshold (≈6.6<sup>◦</sup> C) and RH threshold (≈54.2 %) jointly regulate vapor pressure deficit, the key driver of atmospheric evaporative demand (Guo et al., 2023; Tu et al., 2024). Regional climate trend analysis showed significant warming across the APENC during 2000–2022, with warming hotspots concentrated in the central and northeastern parts of the region (Fig. S5a–b). This widespread warming has pushed ecosystems to operate closer to, or above, this TEM threshold, sustaining elevated evaporative demand where moisture supply does not keep pace. The ET threshold (387 mm yr⁻¹), while distinct from precipitation, is functionally adjacent to the widely recognized 400 mm annual precipitation isohyet in China, both indicating the transition from energy-limited to water-limited regimes (Li et al., 2024c). Consistent with this threshold behavior, PRE trends displayed a marked spatial contrast: increases were concentrated mainly in the northeastern and southern APENC, whereas much of the western and central interior showed only weak changes (Fig. S5c–d). This pattern allowed many eastern–southern areas to remain closer to an energy-limited, relatively humid regime, while drier western and northwestern zones were more likely to persist in a water-limited, drought-prone regime, helping to explain the kTVDI-derived pattern of drought alleviation in the southeast and intensification in the northwest. Southeast of this boundary, ET approaches potential levels and transpiration cooling is strong; northwest of it, water becomes limiting, sensible-heat partitioning increases, and drought risk rises (Huo et al., 2024). DEM and SA exhibited distinct nonlinear behaviors acting jointly through topography–albedo–energy allocation mechanisms: at low elevations, higher vegetation cover and lower albedo promote latent-heat dominance and drought alleviation; at mid-elevations, increased soil exposure and higher albedo enhance sensible-heat dominance and drought intensification; at very high elevations, energy limitation prevails and again favors moisture retention despite high albedo (Hu et al., 2023). 

Critically, thresholds varied systematically across LULC types (Table S3). Forests exhibited earlier TEM-related response shifts and higher ET turning points, suggesting partial buffering via evapotranspiration-mediated cooling when water is available. In contrast, deserts showed patterns consistent with strong water limitation, with drought conditions being more strongly constrained by limited moisture inputs. Grasslands and croplands displayed intermediate threshold characteristics, consistent with their transitional ecohydrological regimes. These quantitative thresholds provide mechanistic benchmarks for regional drought zoning, early-warning system design, and targeted mitigation strategies. 

SHAP interaction analysis, particularly through the normalized relative interaction strength metric, revealed LULC-specific synergistic structures that absolute metrics obscure. Although TEM-related pairs often showed high absolute interaction strength—reflecting its pervasive energy-driver role—normalization exposed distinct coupling hierarchies within each ecosystem. Cropland interactions emphasized humidity-soil/topography synergies, indicating moisture availability modulated by texture and terrain as critical for agricultural drought. Forest displayed balanced soil-topography and atmospheric exchange interactions, with prominent wind-humidity coupling highlighting canopy-atmosphere energy-water exchange. Grassland exhibited dual soil-humidity dominance, reflecting sensitivity to surface moisture controlled by texture and atmospheric humidity. Desert revealed a topographycentered network with strong HFP coupling, indicating that where vegetation buffering is absent, topography becomes the dominant structural control modulating both anthropogenic disturbance and precipitation effectiveness (Duniway et al., 2019). These LULC-dependent interaction structures underscore that drought emerges from ecosystem-specific synergistic processes rather than simple additive effects, with critical implications for differentiated management strategies. 

### _4.4. Management implications for ecological drought mitigation_ 

Based on the revealed LULC-dependent drought mechanisms and quantitative thresholds, we recommend implementing zonal early-warning systems and differentiated governance strategies across APENC. For cropland, particularly in intensification zones such as the northern Loess Plateau, priority should focus on enhancing water-use efficiency through drip irrigation, subsurface irrigation, conservation tillage, and mulching technologies that reduce non-productive evapotranspiration (Wang et al., 2022b). In alleviation zones such as the Northeast Plain, consolidating ecological project effectiveness while strictly controlling expansion of high water-consuming activities is essential. For forests, especially in key barrier zones such as the Greater Khingan Mountains, management should shift from area expansion to structural optimization and stability enhancement through thinning, mixed-species transformation, and construction of windbreak and sand-fixation belts to regulate near-surface microclimate (Schnabel et al., 2021). For grasslands, implementing grass-livestock balance, rotational grazing, and seasonal grazing bans in degraded areas such as the Ordos Plateau and northern Loess Plateau, combined with reseeding drought-resistant native grass species in severely degraded areas, can break positive feedbacks between drought and degradation (Jiang et al., 2025). For desert zones, particularly high-risk areas such as Kubuqi and Mu Us, strictly limiting mining and road disturbances while implementing emergency stabilization measures—sand 

16 

_Journal of Hydrology: Regional Studies 64 (2026) 103174_ 

_Y. Fan et al._ 

barriers, mixed shrub-grass-herb vegetation belts—can suppress amplification effects of human disturbance under conditions lacking vegetation buffering. 

Early-warning systems should incorporate vapor pressure deficit (derived from TEM and RH thresholds) and ET thresholds as core triggers, while integrating initial underlying surface conditions—topography, albedo, vegetation cover—into risk baselines. This mechanism-driven indicator framework supports regional adaptive management and project prioritization by explicitly accounting for LULC-specific vulnerabilities and synergistic factor interactions. Such targeted approaches are essential for enhancing ecological security and sustainable development in vulnerable transition zones under accelerating global environmental change. 

### _4.5. Limitations and future directions_ 

Although this study systematically revealed the spatiotemporal patterns and driving mechanisms of ecological drought in the APENC, several limitations should be acknowledged. First, while the HFP dataset provides an integrated measure of anthropogenic pressure, it cannot distinguish specific activity types (e.g., irrigated versus rain-fed croplands) or key management intensities (e.g., grazing pressure), and does not capture the directionality of their ecological effects. This constrains a mechanistic understanding of how different human activities shape water stress patterns. Furthermore, by focusing on ecosystems with stable land cover, this study establishes a clear baseline of inherent biophysical controls but does not directly quantify the effects of land-use conversion processes. Second, the 1 km spatial resolution is insufficient to capture fine-scale processes such as field-level irrigation scheduling and management practices, which can strongly influence local water balance. Third, although SHAP offers a principled attribution framework, it remains correlational rather than causal and cannot fully disentangle the confounding effects or time-lagged feedbacks inherent in complex Earth system processes (Flora et al., 2024). 

Future research should integrate more detailed human-activity data and develop multi-scale observation and model-fusion frameworks to better unravel the complex mechanisms linking human activities and drought. A particularly promising direction is to combine kTVDI with explicit land-use conversion trajectories to clarify how processes such as ecological restoration, agricultural transformation and urbanization regulate drought dynamics. Coupling process-based ecohydrological models with machine-learning approaches could strengthen causal inference and enable scenario projections under future climate and land-use change. Extending this framework to other ecotones globally would help test its transferability and identify both universal and region-specific drought mechanisms. Finally, integrating kTVDI-based monitoring with ecosystem-service assessments would enable a more comprehensive evaluation of drought impacts on multifunctional landscapes and support nature-based solutions for climate adaptation. 

### **5. Conclusion** 

This study developed an interpretable framework that couples the kTVDI with explainable machine learning (XGBoost-SHAP) and nonlinear modeling (GAM) to decode ecological drought mechanisms in Northern China’s Agro-Pastoral Ecotone (2000–2022). The principal findings are summarized as follows: 

- (1) kTVDI demonstrates superior sensitivity for ecological drought monitoring relative to the traditional TVDI, exhibiting not only a stronger association with independent soil moisture (SMCI; ρ = − 0.604 vs. − 0.533) but also an enhanced relationship with SIF. This supports its use as a more reliable indicator for heterogeneous transition zones. 

- (2) Regional drought showed significant overall alleviation (− 1.328 × 10⁻³ yr⁻¹, p _<_ 0.01), yet with pronounced spatial heterogeneity—southeastern mitigation contrasted with northwestern intensification. This pattern is consistent with monsoon–topography moisture gradients modulated by land–surface feedbacks. Across LULC types, vegetated land covers generally experienced alleviation, whereas deserts tended toward intensification. 

- (3) TEM emerged as the universal primary driver (32.92–52.24 % of total SHAP importance). Nevertheless, LULC types substantially reshaped secondary driver hierarchies and effect directions: vegetated systems exhibited ET-regulated water balance, while deserts displayed PRE-limited dynamics amplified by anthropogenic pressure. 

- (4) GAM analysis identified critical nonlinear thresholds at 6.6<sup>◦</sup> C (TEM), 387 mm yr⁻¹ (ET), and 54.2 % (RH), marking regime shifts in dominant energy–water balance mechanisms. 

- (5) Interaction analysis revealed distinct, LULC-specific synergistic structures, manifested as RH–soil dominance in croplands, coupled soil–topography and WS–RH interactions in forests, and DEM–PRE–HFP coupling in deserts. This indicates that drought emerges from ecosystem-dependent synergistic processes rather than simple additive effects. 

In summary, kTVDI effectively captures the eco-physiological processes underlying ecological drought, and the integrated interpretable framework proves powerful for disentangling complex mechanisms in ecotones. These findings highlight that LULC-specific controls are central to understanding drought responses in the APENC, offering a mechanistic basis for differentiated, thresholdinformed management and early warning systems in similar vulnerable regions under accelerating environmental change. 

### **Abbreviations** 

APENC 

Agro-Pastoral Ecotone of Northern China 

( _continued on next page_ ) 

17 

_Journal of Hydrology: Regional Studies 64 (2026) 103174_ 

_Y. Fan et al.                                                                                                                                                                                                             Journal of Hydrology: Regional Studies_ 

( _continued_ ) 

|CLAY|Clay content|
|---|---|
|DEM|Digital Elevation Model|
|ET|Evapotranspiration|
|GAM|Generalized Additive Model|
|HFP|Human Footprint|
|kNDVI|kernel Normalized Difference Vegetation Index|
|kTVDI|kernel Temperature Vegetation Dryness Index|
|LST|Land Surface Temperature|
|LULC|Land use/Land cover|
|PRE|Precipitation|
|RH|Relative Humidity|
|SA|Surface Albedo|
|SAND|Sand content|
|SHAP|SHapley Additive exPlanations<br>l|
|SIF|Solar-induced chlorophyll fluorescence|
|SLO|l<br>Slope|
|SMCI|Soil Moisture of China by in situ data|
|TEM|Temperature|
|TVDI|Temperature Vegetation Dryness Index<br>l|
|VIF|Variance Inflation Factor|
|WS|l<br>Wind Speed|
|XGBoost|eXtreme Gradient Boosting|



### **CRediT authorship contribution statement** 

**Chunhui Zhan:** Writing – review & editing, Conceptualization. **Xiaoran Ren:** Writing – review & editing. **Siyi Cheng:** Writing – review & editing, Data curation. **Asim Biswas:** Writing – review & editing. **Jian Zhang:** Writing – review & editing, Supervision, Project administration, Methodology, Conceptualization. **Yaoyuan Fan:** Writing – original draft, Visualization, Software, Data curation. 

### _Funding_ 

This research was funded by the National Natural Science Foundation of China [42061010]. 

### **Declaration of Competing Interest** 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

### **Appendix A. Supporting information** 

Supplementary data associated with this article can be found in the online version at doi:10.1016/j.ejrh.2026.103174. 

### **Data availability** 

Data will be made available on request. 

### **References** 

AghaKouchak, A., Cheng, L., Mazdiyasni, O., Farahmand, A., 2014. Global warming and changes in risk of concurrent climate extremes: insights from the 2014 California drought. Geophys. Res. Lett. 41, 8847–8852. https://doi.org/10.1002/2014GL062308. 

Barredo Arrieta, A., Díaz-Rodríguez, N., Del Ser, J., Bennetot, A., Tabik, S., Barbado, A., Garcia, S., Gil-Lopez, S., Molina, D., Benjamins, R., Chatila, R., Herrera, F., 2020. Explainable Artificial Intelligence (XAI): Concepts, taxonomies, opportunities and challenges toward responsible AI. Inf. Fusion 58, 82–115. https://doi. org/10.1016/j.inffus.2019.12.012. 

Camps-Valls, G., Campos-Taberner, M., Moreno-Martínez, A., Walther, S., Duveiller, G., Cescatti, A., Mahecha, M.D., Mu<sup>´</sup> noz-Marí, J., García-Haro, F.J., 2021. ˜ 

A unified vegetation index for quantifying the terrestrial biosphere. Sci. Adv. 7 (9), eabc7447. https://doi.org/10.1126/sciadv.abc7447. Chen, J., Huang, W., Jin, L., Chen, J., Chen, S., Chen, F., 2018. A climatological northern boundary index for the East Asian summer monsoon and its interannual variability. Sci. China Earth Sci. 61 (1), 13–22. https://doi.org/10.1007/s11430-017-9122-x. 

- Chen, J., Dong, G., Chen, J., Jiang, S., Qu, L., Legesse, T.G., Zhao, F., Tong, Q., Shao, C., Han, X., 2022b. Energy balance and partitioning over grasslands on the Mongolian Plateau. Ecol. Indic. 135, 108560. https://doi.org/10.1016/j.ecolind.2022.108560. 

- Chen, T., Guestrin, C., 2016. XGBoost: A scalable tree boosting system. Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. ACM, pp. 785–794. https://doi.org/10.1145/2939672.2939785. 

18 

_Y. Fan et al.                                                                                                                                                                                                             Journal of Hydrology: Regional Studies 64 (2026) 103174_ Chen, X., Huang, Y., Nie, C., Zhang, S., Wang, G., Chen, S., Chen, Z., 2022a. A long-term reconstructed TROPOMI solar-induced fluorescence dataset using machine learning algorithms. Sci. Data 9, 427. https://doi.org/10.1038/s41597-022-01520-1. Chen, Y., Zhao, Q., Liu, Y., Zeng, H., 2025. Exploring the impact of natural and human activities on vegetation changes: An integrated analysis framework based on trend analysis and machine learning. J. Environ. Manag. 374, 124092. https://doi.org/10.1016/j.jenvman.2025.124092. 

- Chen, Z., Wang, W., Fu, J., 2020. Vegetation response to precipitation anomalies under different climatic and biogeographical conditions in China. Sci. Rep. 10, 2892. https://doi.org/10.1038/s41598-020-57910-1. 

- Christina, M., Nouvellon, Y., Laclau, J.-P., Stape, J.L., Bouillet, J.-P., Lambais, G.R., le Maire, G., 2017. Importance of deep water uptake in tropical eucalypt forest. Funct. Ecol. 31 (2), 509–519. https://doi.org/10.1111/1365-2435.12727. 

- Crausbay, S.D., Ramirez, A., Carter, S., Cross, M., Hall, K., Bathke, D., Betancourt, J., Colt, S., Cravens, A., Dalton, M., Dunham, J., Hay, L., Hayes, M., McEvoy, J., McNutt, C., Moritz, M., Nislow, K., Raheem, N., Sanford, T., 2017. Defining ecological drought for the twenty-first century. Bull. Am. Meteorol. Soc. 98 (12), 2543–2550. https://doi.org/10.1175/BAMS-D-16-0292.1. 

- Cui, J., Chen, A., Huntingford, C., Piao, S., 2024. Integrating ecosystem water demands into drought monitoring and assessment under climate change. Nat. Water 2, 215–218. https://doi.org/10.1038/s44221-024-00217-6. 

- Ding, Y., Xu, R., Wang, R., Zhang, S., Ding, H., Liu, W., 2023. Can grain production be synergistic with socioeconomic development? Empirical evidence from the agro-pastoral ecotone in North China. Ecol. Indic. 156, 111191. https://doi.org/10.1016/j.ecolind.2023.111191. 

- Ding, Y., Zhang, L., He, Y., Cao, S., Gusev, A., Guo, Y., Ran, L., Wei, X., Mikalai, F., 2024. Nonlinear effects of agricultural drought on vegetation productivity in the Yellow River Basin, China. Sci. Total Environ. 948, 174903. https://doi.org/10.1016/j.scitotenv.2024.174903. 

- Duniway, M.C., Pfennigwerth, A.A., Fick, S.E., Nauman, T.W., Belnap, J., Barger, N.N., 2019. Wind erosion and dust from US drylands: A review of causes, consequences, and solutions in a changing world. Ecosphere 10 (3), e02650. https://doi.org/10.1002/ecs2.2650. 

- Fan, Y., Im, E., Lan, C., Lo, M., 2023. An increase in precipitation driven by irrigation over the North China Plain based on RegCM and WRF simulations. J. Hydrometeorol. 24 (6), 1155–1173. https://doi.org/10.1175/JHM-D-22-0131.1. 

- Flora, M., Potvin, C., McGovern, A., Handler, S., 2024. A machine learning explainability tutorial for atmospheric sciences. Artif. Intell. Earth Syst. 3 (1). https://doi. org/10.1175/AIES-D-23-0018.1. 

- Flores, B.M., Staal, A., 2022. Feedback in tropical forests of the Anthropocene. Glob. Change Biol. 28 (21), 6079–6095. https://doi.org/10.1111/gcb.16293. 

- Gao, S., Zhong, R., Yan, K., Ma, X., Chen, X., Pu, J., Gao, Sicong, Qi, J., Yin, G., Myneni, R.B., 2023. Evaluating the saturation effect of vegetation indices in forests using 3D radiative transfer simulations and satellite observations. Remote Sens. Environ. 295, 113665. https://doi.org/10.1016/j.rse.2023.113665. 

- Grossiord, C., Buckley, T.N., Cernusak, L.A., Novick, K.A., Poulter, B., Siegwolf, R.T.W., Sperry, J.S., McDowell, N.G., 2020. Plant responses to rising vapor pressure deficit. N. Phytol. 226 (6), 1550–1566. https://doi.org/10.1111/nph.16485. 

- Guo, X., Zhang, Y., Zha, T., Shang, G., Jin, C., Wang, Y., Yang, H., 2023. Biophysical controls of dew formation in a typical cropland and its relationship to drought in the North China Plain. J. Hydrol. 617 (Part B), 128945. https://doi.org/10.1016/j.jhydrol.2022.128945. 

- Guo, Y., Li, Y., Wang, F., Wei, Y., Xu, Z., 2017. The topography-related spatial distribution of precipitation and its long-term trend over the Tibetan Plateau. Hydrol. Sci. J. 62 (6), 863–879. https://doi.org/10.1080/02626667.2016.1259134. 

- Hastie, T.J., 1990. Generalized Additive Models: An Introduction with R, 1st ed. Routledge, London. https://doi.org/10.1201/9780203753781. Hu, X.M., Li, X., Xue, M., Wu, D., Fuentes, J.D., 2016. The formation of barrier winds east of the Loess Plateau and their effects on dispersion conditions in the North China Plains. Bound. Layer. Meteorol. 161 (1), 145–163. https://doi.org/10.1007/s10546-016-0159-4. 

- Hu, Y., Zhang, L., 2024. Added value of merging techniques in precipitation estimates relative to gauge-interpolation algorithms of varying complexity. J. Hydrol. 645, 132214. https://doi.org/10.1016/j.jhydrol.2024.132214. 

- Hu, Z., Sun, S., Sun, X., Lin, S., Song, C., Wang, G., 2023. Controlling factors of the spatial-temporal fluctuations in evapotranspiration along an elevation gradient across humid montane ecosystems. Water Resour. Res. 59, e2022WR033228. https://doi.org/10.1029/2022WR033228. 

- Huo, J., Bin, L., Yu, X., Jia, G., 2024. Spatial heterogeneity of watershed runoff sensitivity to climate and underlying surface changes in humid and sub-humid climates in China. J. Hydrol. Reg. Stud. 52, 101702. https://doi.org/10.1016/j.ejrh.2024.101702. 

- Intergovernmental Panel on Climate Change (IPCC), 2022. Climate Change 2022: Impacts, Adaptation, and Vulnerability. Contribution of Working Group II to the Sixth Assessment Report of the IPCC. Cambridge University Press. https://doi.org/10.1017/9781009325844. 

- Jiang, H., Zhou, Y., Li, W., Lu, Q., Xu, D., Ma, H., Ma, X., Tian, X., 2025. Reseeding native species promotes community stability by improving species diversity, niche, and interspecific relationships in the desert steppe of Northwest China. Ecol. Evol. 15, e70929. https://doi.org/10.1002/ece3.70929. 

- Jiang, T., Su, X., Singh, V.P., Zhang, G., 2022. Spatio-temporal pattern of ecological droughts and their impacts on health of vegetation in Northwestern China. J. Environ. Manag. 305, 114356. https://doi.org/10.1016/j.jenvman.2021.114356. 

- Konkathi, P., Karthikeyan, L., 2022. Error and uncertainty characterization of soil moisture and VOD retrievals obtained from L-band SMAP radiometer. Remote Sens. Environ. 280, 113146. https://doi.org/10.1016/j.rse.2022.113146. 

- Li, F., Zhang, M., Zhao, Y., Jiang, R., 2023a. Influence of irrigation and groundwater on the propagation of meteorological drought to agricultural drought. Agric. Water Manag. 277, 108099. https://doi.org/10.1016/j.agwat.2022.108099. 

- Li, J., Liu, G., Zhao, J., Zuo, L., Zheng, S., Su, X., 2024b. The variation of the 400 mm isohyet and its influence mechanism on the Qinghai–Tibet Plateau from 1982 to 2021. Ecol. Indic. 159, 111746. https://doi.org/10.1016/j.ecolind.2024.111746. 

- Li, M., Ge, C., Zong, S., Wang, G., 2022b. Drought assessment on vegetation in the Loess Plateau using a phenology-based vegetation condition index. Remote Sens. 14, 3043. https://doi.org/10.3390/rs14133043. 

- Li, Q., Shi, G., Shangguan, W., Nourani, V., Li, J., Li, L., Huang, F., Zhang, Y., Wang, C., Wang, D., Qiu, J., Lu, X., Dai, Y., 2022a. A 1 km daily soil moisture dataset over China using in situ measurement and machine learning. Earth Syst. Sci. Data 14, 5267–5286. https://doi.org/10.5194/essd-14-5267-2022. 

- Li, X., Piao, S., Huntingford, C., Penuelas, J., Yang, H., Xu, H., Chen, A., Friedlingstein, P., Keenan, T.F., Sitch, S., Wang, X., Zscheischler, J., Mahecha, M.D., 2023b. ˜ Global variations in critical drought thresholds that impact vegetation. Natl. Sci. Rev. 10 (5), nwad049. https://doi.org/10.1093/nsr/nwad049. 

- Li, X., Xu, X., Sonnenborg, T.O., Andreasen, M., He, C., 2024a. Effect of ecological restoration on evapotranspiration and water yield in the agro-pastoral ecotone in northern China during 2000–2018. J. Hydrol. 638, 131531. https://doi.org/10.1016/j.jhydrol.2024.131531. 

- Li, Z., Yang, Q., Ma, Z., Wu, P., Duan, Y., Li, M., Zheng, Z., 2024c. Aridification and its impacts on terrestrial hydrology and ecosystems over a comprehensive transition zone in China. J. Clim. 37 (5), 1651–1666. https://doi.org/10.1175/JCLI-D-23-0203.1. 

- Lundberg, S.M., Lee, S.I., 2017. A unified approach to interpreting model predictions. Adv. Neural Inf. Process. Syst. 30, 4765–4774. https://doi.org/10.48550/ arXiv.1705.07874. 

- Luo, Y., Zuo, X., Li, Y., Zhang, T., Zhang, R., Chen, J., Lv, P., Zhao, X., 2019. Community carbon and water exchange responses to warming and precipitation enhancement in sandy grassland along a restoration gradient. Ecol. Evol. 9 (19), 10938–10949. https://doi.org/10.1002/ece3.5490. 

- Mu, H., Li, X., Wen, Y., Huang, J., Du, P., Su, W., Miao, S., Geng, M., 2022. A global record of annual terrestrial Human Footprint dataset from 2000 to 2018. Sci. Data 9, 176. https://doi.org/10.1038/s41597-022-01284-8. 

- Newcomb, S.K., Godsey, S.E., 2023. Nonlinear riparian interactions drive changes in headwater streamflow. Water Resour. Res. 59, e2023WR034870. https://doi. org/10.1029/2023WR034870. 

- Niazkar, M., Menapace, A., Brentan, B., Piraei, R., Jimenez, D., Dhawan, P., Righetti, M., 2024. Applications of XGBoost in water resources engineering: A systematic literature review (Dec 2018–May 2023). Environ. Model. Softw. 174, 105971. https://doi.org/10.1016/j.envsoft.2024.105971. 

- O'Connor, J.C., Dekker, S.C., Staal, A., Tuinenburg, O.A., Rebel, K.T., Santos, M.J., 2021. Forests buffer against variations in precipitation. Glob. Change Biol. 27 (19), 4686–4696. https://doi.org/10.1111/gcb.15763. 

- Okoduwa, A.K., Mokhtarisabet, S., 2025. Spatiotemporal analysis of drought in the Sahelian region of northeastern Nigeria, sub-Saharan Africa. Theor. Appl. Climatol. 156, 293. https://doi.org/10.1007/s00704-025-05542-8. 

- Qian, W., Shan, X., Chen, D., Zhu, C., Zhu, Y., 2012. Droughts near the northern fringe of the East Asian summer monsoon in China during 1470–2003. Clim. Change 110 (1), 373–383. https://doi.org/10.1007/s10584-011-0096-7. 

19 

_Y. Fan et al.                                                                                                                                                                                                             Journal of Hydrology: Regional Studies 64 (2026) 103174_ 

- Qiu, D., Xu, R., Wu, C., Mu, X., Zhao, G., Gao, P., 2022. Vegetation restoration improves soil hydrological properties by regulating soil physicochemical properties in the Loess Plateau, China. J. Hydrol. 609, 127730. https://doi.org/10.1016/j.jhydrol.2022.127730. 

- Ren, Y., Yue, P., Zhang, Q., Liu, X., 2021. Influence of land surface aridification on regional monsoon precipitation in East Asian summer monsoon transition zone. Theor. Appl. Climatol. 144 (1), 93–102. https://doi.org/10.1007/s00704-021-03523-1. 

- Ren, Z., Zhu, L., Wang, B., Cheng, S., 2016. Soil hydraulic conductivity as affected by vegetation restoration age on the Loess Plateau, China. J. Arid Land 8 (4), 546–555. https://doi.org/10.1007/s40333-016-0010-2. 

- Scanlon, B.R., Keese, K.E., Flint, A.L., Flint, L.E., Gaye, C.B., Edmunds, W.M., Simmers, I., 2006. Global synthesis of groundwater recharge in semiarid and arid regions. Hydrol. Process. 20 (23), 4687–4709. https://doi.org/10.1002/hyp.6335. 

- Scheff, J., Frierson, D.M.W., 2014. Scaling potential evapotranspiration with greenhouse warming. J. Clim. 27, 1539–1556. https://doi.org/10.1175/JCLI-D-1300233.1. 

- Schnabel, F., Liu, X., Kunz, M., Barry, K.E., Bongers, F.J., Bruelheide, H., Fichtner, A., H¨ardtle, W., Li, S., Pfaff, C.-T., Schmid, B., Schwarz, J.A., Tang, Z., Yang, B., Bauhus, J., von Oheimb, G., Ma, K., Wirth, C., 2021. Species richness stabilizes productivity via asynchrony and drought-tolerance diversity in a large-scale tree biodiversity experiment. Sci. Adv. 7, eabk1643. https://doi.org/10.1126/sciadv.abk1643. 

- Shao, R., Zhang, B., Su, T., Long, B., Cheng, L., Xue, Y., Yang, W., 2019. Estimating the increase in regional evaporative water consumption as a result of vegetation restoration over the Loess Plateau, China. J. Geophys. Res. Atmospheres 124, 11783–11802. https://doi.org/10.1029/2019JD031295. 

- Shi, G., Sun, W., Shangguan, W., Wei, Z., Yuan, H., Li, L., Sun, X., Zhang, Y., Liang, H., Li, D., Huang, F., Li, Q., Dai, Y., 2025. A China dataset of soil properties for land surface modelling (version 2, CSDLv2). Earth Syst. Sci. Data 17, 517–543. https://doi.org/10.5194/essd-17-517-2025. 

- Slater, L., Blougouras, G., Deng, L., Deng, Q., Huang, E., van Dijk, H.A., Foord, F., Hoek, S.A., Moulds, S., Schepen, A., Yin, J., Zhang, B., 2025. Challenges and opportunities of ML and explainable AI in large-sample hydrology. Philos. Trans. R. Soc. A Math. Phys. Eng. Sci. 383, 20240287. https://doi.org/10.1098/ rsta.2024.0287. 

- Slette, I.J., Post, A.K., Awad, M., Even, T., Punzalan, A., Williams, S., Smith, M.D., Knapp, A.K., 2019. How ecologists define drought, and why we should do better. Glob. Change Biol. 25 (10), 3193–3200. https://doi.org/10.1111/gcb.14747. 

- Sun, C., Zhao, W., Liu, H., Zhang, Y., Zhou, H., 2021. Effects of textural layering on water regimes in sandy soils in a desert–oasis ecotone, northwestern China. Front. Earth Sci. 9, 627500. https://doi.org/10.3389/feart.2021.627500. 

- Tu, Y., Wang, X., Zhou, J., Wang, X., Jia, Z., Ma, J., Yao, W., Zhang, X., Sun, Z., Luo, P., Feng, X., Fu, B., 2024. Atmospheric water demand dominates terrestrial ecosystem productivity in China. Agric. For. Meteorol. 355, 110151. https://doi.org/10.1016/j.agrformet.2024.110151. 

- Walter, J.A., Atkins, J.W., Hulshof, C.M., 2024. Climate and topography control variation in the tropical dry forest–rainforest ecotone. Ecology 105 (11), e4442. https://doi.org/10.1002/ecy.4442. 

- Wang, H., Wang, N., Quan, H., Zhang, F., Fan, J., Feng, H., Cheng, M., Liao, Z., Wang, X., Xiang, Y., 2022b. Yield and water productivity of crops, vegetables and fruits under subsurface drip irrigation: A global meta-analysis. Agric. Water Manag. 269, 107645. https://doi.org/10.1016/j.agwat.2022.107645. 

- Wang, L., Lee, X., Schultz, N., Chen, S., Wei, Z., Fu, C., Gao, Y., Yang, Y., Lin, G., 2018. Response of surface temperature to afforestation in the Kubuqi Desert, Inner Mongolia. J. Geophys. Res. Atmos. 123, 1865–1879. https://doi.org/10.1002/2017JD027522. 

- Wang, Q., Moreno-Martínez, A., Mu<sup>´</sup> noz-Marí, J., Campos-Taberner, M., Camps-Valls, G., 2023. Estimation of vegetation traits with kernel NDVI. ISPRS J. ˜ Photogramm. Remote Sens. 195, 408–417. https://doi.org/10.1016/j.isprsjprs.2022.12.019. 

Wang, X., Zhang, B., Li, F., Li, X., Li, X., Wang, Y., Shao, R., Tian, J., He, C., 2021. Vegetation restoration projects intensify intraregional water recycling processes in the agro-pastoral ecotone of Northern China. J. Hydrometeorol. 22 (6), 1385–1403. https://doi.org/10.1175/JHM-D-20-0125.1. Wang, Y., Yuan, X., 2022. Land–atmosphere coupling speeds up flash drought onset. Sci. Total Environ. 851, 158109. https://doi.org/10.1016/j. scitotenv.2022.158109. 

- Wang, Z., Fu, Z., Liu, B., Zheng, Z., Zhang, W., Liu, Y., Zhang, F., Zhang, Q., 2022a. Northward migration of the East Asian summer monsoon northern boundary during the twenty-first century. Sci. Rep. 12 (1), 10066. https://doi.org/10.1038/s41598-022-13713-0. 

- Wei, B., Xie, Y., Jia, X., Wang, X., He, H., Xue, X., 2018. Land use/land cover change and its impacts on diurnal temperature range over the agricultural pastoral ecotone of Northern China. Land Degrad. Dev. 29, 3009–3020. https://doi.org/10.1002/ldr.3052. 

Wood, S.N., 2017. Generalized Additive Models: An Introduction with R, 2nd ed. Chapman and Hall/CRC, New York. https://doi.org/10.1201/9781315370279. 

- Xiao, C., Zaehle, S., Yang, H., Wigneron, J.-P., Schmullius, C., Bastos, A., 2023. Land cover and management effects on ecosystem resistance to drought stress. Earth Syst. Dyn. 14 (6), 1211–1230. https://doi.org/10.5194/esd-14-1211-2023. 

- Yang, J., Huang, X., 2021. The 30 m annual land cover dataset and its dynamics in China from 1990 to 2019. Earth Syst. Sci. Data 13, 3907–3925. https://doi.org/ 10.5194/essd-13-3907-2021. 

Yao, Y., Liu, Y., Zhou, S., Song, J., Fu, B., 2023. Soil moisture determines the recovery time of ecosystems from drought. Glob. Change Biol. 29, 3562–3574. https:// doi.org/10.1111/gcb.16620. 

- Yu, Y., Fang, S., Zhuo, W., 2023. Revealing the driving mechanisms of land surface temperature spatial heterogeneity and its sensitive regions in China based on GeoDetector. Remote Sens. 15, 2814. https://doi.org/10.3390/rs15112814. 

- Yuan, T., Tai, A.P.K., Mao, J., Tam, O.H.F., Li, R.K.K., Wu, J., Li, S., 2023. Effects of different irrigation methods on regional climate in North China Plain: A modeling study. Agric. For. Meteorol. 342, 109728. https://doi.org/10.1016/j.agrformet.2023.109728. 

- Zeng, D., Yuan, X., 2024. The important role of reduced moisture supplies from the monsoon region in the formation of spring and summer droughts over Northeast China. J. Clim. 37, 1703–1722. https://doi.org/10.1175/JCLI-D-23-0344.1. 

Zhang, G., Chen, X., Zhou, Y., Jiang, L., Jin, Y., Wei, Y., Li, Y., Pan, Z., An, P., 2022b. Aridification in a farming–pastoral ecotone of northern China from two perspectives: Climate and soil. J. Environ. Manag. 302 (Part B), 114070. https://doi.org/10.1016/j.jenvman.2021.114070. 

- Zhang, G., Chen, X., Zhou, Y., Zhao, H., Jin, Y., Luo, Y., Chen, S., Wu, X., Pan, Z., An, P., 2023. Land use/cover changes and subsequent water budget imbalance exacerbate soil aridification in the farming–pastoral ecotone of northern China. J. Hydrol. 624, 129939. https://doi.org/10.1016/j.jhydrol.2023.129939. 

Zhang, J., Guan, K., Peng, B., Pan, M., Zhou, W., Jiang, C., Kimm, H., Franz, T.E., Grant, R.F., Yang, Y., Rudnick, D.R., Heeren, D.M., Suyker, A.E., Bauerle, W.L., Miner, G.L., 2021. Sustainable irrigation based on co-regulation of soil water supply and atmospheric evaporative demand. Nat. Commun. 12 (1), 5549. https:// doi.org/10.1038/s41467-021-25254-7. 

Zhang, L.F., Yan, H.W., He, Y., Yao, S., Cao, S., Sun, Q., 2022a. Spatiotemporal prediction of alpine vegetation dynamic change based on a ConvGRU neural network model: A case study of the upper Heihe River basin in Northwest China. IEEE J. Sel. Top. Appl. Earth Obs. Remote Sens. 15, 6957–6971. https://doi.org/10.1109/ JSTARS.2022.3200521. 

Zhang, Y., Chiew, F.H.S., Pena-Arancibia, J., Sun, F., Li, H., Leuning, R., 2017. Global variation of transpiration and soil evaporation and the role of their major ˜ climate drivers. J. Geophys. Res. Atmosp. 122 (13), 6868–6881. https://doi.org/10.1002/2017JD027025. 

Zhu, Y., Jiang, S., Ren, L., Guo, J., Zhong, F., Du, S., Cui, H., He, M., Duan, Z., 2024. Three-dimensional ecological drought identification and evaluation method considering eco-physiological status of terrestrial ecosystems. Sci. Total Environ. 951, 175423. https://doi.org/10.1016/j.scitotenv.2024.175423. 

20 

