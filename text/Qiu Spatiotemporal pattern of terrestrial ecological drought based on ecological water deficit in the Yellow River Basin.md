© 2025 The Authors 







Hydrology Research Vol 56 No 11, 1182 doi: 10.2166/nh.2025.054 

# Spatiotemporal pattern of terrestrial ecological drought based on ecological water deficit in the Yellow River Basin 

Mengting Qiu<sup>a,b,c</sup> , Shanhu Jiang a,b,c,*, Jianying Guob, Yongwei Zhua, Yating Liud and Liliang Rena,c 

> a College of Hydrology and Water Resources, Hohai University, Nanjing 210098, China 

> b Yinshanbeilu Grassland Eco-hydrology National Observation and Research Station, China Institute of Water Resources and Hydropower Research, Beijing 100038, China 

> c The National Key Laboratory of Water Disaster Prevention, Hohai University, Nanjing 210098, China 

> d Hubei Institute of Water Resources Survey and Design Co., Ltd, Hubei 430000, China 

*Corresponding author. E-mail: hik0216@hhu.edu.cn 



SJ, 0000-0003-1560-4600 

#### ABSTRACT 

Ecological drought (ED) poses significant challenges to terrestrial ecosystems under environmental change. However, most existing remote sensing indices are merely descriptive, lacking a comprehensive ED assessment that integrates vegetation conditions, evapotranspiration, and water deficit. Therefore, the study developed a ‘Vegetation-Evapotranspiration-Water Balance’ framework that captures the complete process in water supply and demand balance and reflects the combined effects of meteorological conditions, soil moisture, and vegetation physiological status, revealing ED’s physio-ecological mechanisms. The study applied this framework to assess ED spatiotemporal patterns across the Yellow River Basin (YRB) from 1982 to 2020 using an eight-subregion division. Key findings include: (1) normalized difference vegetation index showed an abrupt circa around 2003, with 95.3% area of YRB exhibiting increases. (2) Crop coefficients increased in northern subregions but decreased in southern, reflecting divergent ecological responses; (3) ecological water metrics exhibited strong spatial gradients, with ecological water requirement (EWR) decreasing southward and ecological water consumption (EWC) and ecological water deficit (EWD) increasing from north to south; (4) despite rising EWR and EWC, EWD decreased in 54.6% area of YRB. Spatially, terrestrial ED was slightly alleviated in the upper reaches (loop irrigation area), remained stable in the middle reaches (Loess Plateau core), and was significantly alleviated across the downstream. 

Key words: crop coefficients, ecological water deficit, normalized difference vegetation index, terrestrial ecological drought, vegetation health index 

#### HIGHLIGHTS 

- Assess the spatial distribution and evolutionary trend of NDVI in the Yellow River Basin (YRB) from 1982 to 2020. 

- Analyze the distribution characteristics and evolutionary trend of crop coefficients. 

- Establish a ‘Vegetation-ET-Water balance’ framework for terrestrial ecological drought. 

- Quantify the spatial distribution and evolutionary trend of terrestrial ecological drought in the YRB. 

This is an Open Access article distributed under the terms of the Creative Commons Attribution Licence (CC BY 4.0), which permits copying, adaptation and redistribution, provided the original work is properly cited (http://creativecommons.org/licenses/by/4.0/). 

Hydrology Research Vol 56 No 11, 1183 

#### GRAPHICAL ABSTRACT 



## 1. INTRODUCTION 

Global warming has increased the frequency of extreme drought events (Chiang et al. 2021; Cao et al. 2025), imposing cascading water stress effects on terrestrial ecosystems (Anderegg et al. 2020; Zhang et al. 2024). Such stress disrupts carbon balance, diminishes biodiversity, and compromises ecosystem sustainability. Early investigations had primarily correlated meteorological and hydrological drought indicators with climatic variables to establish direct water deficit relationships. However, these studies failed to capture ecosystem-level cascade responses. This knowledge gap precipitated a paradigm shift toward ecological dimensions. In 2008, the Science for Nature and People Partnership (SNAPP) operationalized ecological drought (ED) assessment as water stress during vegetation growth phases ( Jiang et al. 2021; Higgins et al. 2023) was marked by the formal integration of drought assessment into ecological frameworks. With intensifying climate change, ED has emerged as a central paradigm for characterizing drought-induced ecological impacts (Wang et al. 2021). Fundamentally distinct from conventional drought typologies, ED resides in vegetation-soil system response mechanisms to water deficits. These reveal multiscale interactions among plant physiology, edaphic processes, and ecosystem functionality (Xu et al. 2021; Jiao et al. 2022). Critically, the Intergovernmental Panel on Climate Change Sixth Assessment Report (IPCC 2022, Ch8.2.2) projects that continued climate change will expand ED intensity and spatial extent. The risk of global ED would thus be exacerbated (Zhang et al. 2020). 

However, a standardized definition of ED remains lacking. SNAPP defines ED as water stress caused by climate change and human activities during vegetation growth. ED is viewed as an ecological feedback process related to water deficits in vegetation-soil systems. Current research predominantly adopts Crausbay’s framework, which integrates two dimensions: vulnerability components and the continuous integration of natural and anthropogenic factors. As ecological issues intensify, ED will become a central focus in future drought research. Nevertheless, terrestrial ecosystem responses to drought stress involve highly complex mechanisms. These encompass interactions among soil processes, plant physiology, and ecosystem functions, further complicated by combined climate change and human impacts. Consequently, significant challenges persist in ED monitoring and assessment. Therefore, developing reliable monitoring methods, improving assessment accuracy, and enhancing ecosystem climate adaptation capacity emerge as critical priorities. 

Hydrology Research Vol 56 No 11, 1184 

Currently, standardized indicator systems have been well-established in meteorological, agricultural, and hydrological areas (Wambua 2019; Zhang et al. 2019a, b). By contrast, ED monitoring lacks unified metrics. Current ED indicators derived from remote sensing data comprise three categories in Table 1: (1) univariate vegetation indices including normalized difference vegetation index (NDVI) (Jha et al. 2019; Fairbairn et al. 2025; Lu et al. 2025), gross primary production (GPP) (Turner et al. 2006; Yuan et al. 2019; Lai et al. 2024), solar-induced chlorophyll fluorescence (SIF) (Zhang et al. 2024; Cao et al. 2025), and enhanced vegetation index (EVI) (Chen et al. 2024; Meng et al. 2025; Zhao et al. 2025); (2) dual-variable coupling indices such as vegetation health index (VHI) which signals heat-water stress interaction ( Javed et al. 2021; Ghobadi & Badehian 2025), water use efficiency (WUE) which signals water limitation-ET synergy (Ding et al. 2024; Li et al. 2024; Ncisana et al. 2024), the standardized ED index (SESNDI) which signals ET, soil moisture (SM), NDVI (Zhu et al. 2024), and transformed difference vegetation index (TDVI), which signals NDVI-temperature integration ( Jiang et al. 2020; Khosravi & Ouarda 2025); and (3) vegetation water supply and demand indicators exemplified by EWC (Wang et al. 2006; Zhang et al. 2010), and EWD. Although existing remotely sensed vegetation indicators can indirectly reflect the ecological impacts of drought through vegetation and evapotranspiration (Zhang et al. 2017; Javed et al. 2021; Tariq et al. 2021), quantifying the dynamic equilibrium of ecosystem water supply and demand remains challenging (Yuan et al. 2019; Javed et al. 2021). Therefore, there is a need to monitor ED by introducing an indicator that integrates the state of the vegetation, the dynamics of evapotranspiration, and the imbalance of ecological water demand and consumption. In this paper, crop coefficients were calculated using the NDVI, which was then used to calculate ecological water requirement (EWR), ecological water consumption (EWC), and ecological water deficit (EWD), and cross-validated with the VHI. Research develops an ED framework through ‘Vegetation-ET-Water balance’ to quantify the vegetation drought from the perspective of the ecosystem (Zhao et al. 2007; Zhang et al. 2010). 

The Yellow River Basin (YRB) experiences a continental monsoon climate with June–September precipitation concentration. The basin contains 12.5% of China’s arable land but its rivers constitute only 2.1% of the nation’s total river runoff. Synergistic climate-anthropogenic pressures have substantially elevated ED risks, constraining regional high-quality development. Current research demonstrates that the study revealed (Wang et al. 2024) the spatial distribution characteristics of ED risk in the YRB and analyzed the dominant factors affecting the ED risk in the YRB. VHI has high applicability in vegetation drought determination in the YRB (Yang et al. 2024). By further revealing the heterogeneity of ecosystem response 

Table 1 | Advances in ED research 

|Form|Indices|Advantage|Limitations|References|
|---|---|---|---|---|
|Univariate vegetation<br>indices|NDVI|Directly reflecting vegetation<br>greenness|High vegetation coverage<br>areas are prone to<br>saturation|Fairbairnet al.(2025);Lu<br>et al.(2025);Jha et al.<br>(2019)|
||GPP|Directly reflecting the productivity<br>of the ecosystem|Model parameters are<br>complex|Lai et al. (2024);Turneret al.<br>(2006);Yuanet al.(2019)|
||SIF|Early-stress detection|Coarse spatial resolution|Cao et al. (2025);Zhang<br>et al.(2024)|
||EVI|Reduce the impact on the<br>atmosphere and soil|Complex calculation|Zhaoet al.(2025); Chen<br>et al.(2024);Menget al.<br>(2025)|
|Dual-variable coupling<br>indices|VHI|Comprehensive temperature-water<br>stress|Sensitive to vegetation types|Javed et al.(2021);Ghobadi<br>& Badehian (2025)|
||WUE|Directly reflecting vegetation<br>water use efficiency|Applicable to vegetation-<br>covered areas|Dinget al.(2024);Liet al.<br>(2024);Ncisanaet al.<br>(2024)|
||SESNDI|Capturing synergistic coercion|Soil background disturbance|Zhu et al.(2024)|
||TDVI|Strong drought sensitivity|Affected by cloud coverage|Khosravi & Ouarda (2025);<br>Jianget al.(2020)|
|Vegetation water supply<br>and demand indicators|EWC|Reflect real water consumption|Accuracy depends on input<br>data|Wanget al.(2006);Zhang<br>et al.(2010)|
||EWD|Directly quantify the gap between<br>water supply and demand|Ignore groundwater recharge|Yinet al.(2021);Shiet al.<br>(2022)|



Hydrology Research Vol 56 No 11, 1185 

to drought, the study pointed (Zhu et al. 2025) out that the resilience of the southern region of the watershed is higher than that of the northern region. Analysis of ED evolution in the YRB during 2004–2023 using GPP (Lu et al. 2024) and water supply drought index (WSDI) (Luan et al. 2025) revealed significantly higher drought severity in the upper basin compared to the middle/lower reaches, with the latter demonstrating a declining temporal trend. Although existing research has examined localized drought characteristics, driving mechanisms, or associated ecological risks within the YRB, there remains a lack of trend analysis concerning long-term evolution at the basin-wide scale (Cui et al. 2010; Wu et al. 2022). Consequently, a comprehensive YRB-scale multidimensional assessment constitutes a critical research imperative. 

However, critical knowledge gaps persist not only at the watershed scale, where most existing remote sensing indices (such as VHI and NDVI) remain descriptive rather than quantitative in quantifying the drivers of drought occurrence. This study not only describes the phenomenon of drought but also analyses the complete process of ‘vegetation growth status – vegetation evapotranspiration – water supply and demand balance’, reflecting the combined effects of meteorological conditions, soil moisture, and vegetation physiological status. It provides a quantitative analysis of the evolution patterns of ED and a qualitative analysis of its driving factors. Research proposes the following hypotheses for subsequent validation: H1: Spatial inconsistency between vegetation water supply and demand. H2: The consistency and inconsistency in the increase of vegetation water supply and demand. Both EWR and EWC increase, but the rise in EWC fails to match that of EWR, thereby exacerbating EWD. H3: Intense human activity may significantly alter the mismatch between vegetation water supply and demand. 

Guided by these hypotheses, the study developed an integrated ‘Vegetation-ET-Water Balance’ framework. This framework comprises three interrelated components: (i) vegetation growth status: determine growth stages based on NDVI, calculate kc for different stages, compute EWR and EWC, and finally validate drought conditions using vegetation remote sensing data. (ii) Vegetation evapotranspiration: reference crop evapotranspiration (ET0) is calculated by the Penman–Monteith formula, with actual crop evapotranspiration (ETa) determined by integrating kc. This module reflects the combined effects of meteorological conditions, soil moisture, and vegetative physiological regulation. (iii) Water supply-demand balance: quantifies ED by calculating the difference between EWR and EWC, thereby characterizing the degree of water imbalance. This study not only describes drought phenomena but also analyses the complete process of ‘vegetation growth status – vegetation evapotranspiration – water supply-demand balance’, reflecting the combined effects of meteorological conditions, soil moisture, and vegetation physiological status. Finally, it incorporates vegetation remote sensing data for validation. Applying this framework to the YRB, research systematically analyzed the spatial distribution patterns and evolutionary trends of terrestrial ED in the basin from 1980 to 2020. This study addresses the existing gap in trend analysis concerning ED evolution across the entire basin scale. 

## 2. STUDY AREA AND DATASET 

### 2.1. Overview of the study area 

The YRB (95°53<sup>0</sup> E–119°05<sup>0</sup> E, 32°10<sup>0</sup> N–41°50<sup>0</sup> N) spans 795,000 km<sup>2</sup> (including 42,000 km<sup>2</sup> endorheic area) across the Qinghai-Tibet Plateau, Loess Plateau, and North China Plain, bounded by the Bayan Har Mountains (west), Bohai Sea (east), Qinling Mountains (south), and Yin Mountains (north). Grassland was the dominant land cover type in the basin, accounting for 50% of the total area. Cropland (26%) and forestland (13%) were the other two predominant types, collectively representing 89% of the land cover. The climate is characterized by arid conditions in the west and more humid conditions in the east. Mean annual temperature ranges from 0.3 to 15 °C, while precipitation exhibits a southeastward-declining gradient (160– 700 mm annually). It has a well-developed water system and a complex topography, and the YRB is divided into eight subregions based on secondary water resource zoning (Figure 1). 

### 2.2. Research data 

Data sources and specifications employed in this study are presented in Table 2. A unified spatial resolution of 0.1° was established for all datasets to ensure consistency. Meteorological data were already available at 0.1° resolution and were used directly. NDVI data (0.05°) was sampled to 0.1° using bilinear interpolation to create a spatially continuous surface for subsequent analysis. Conversely, VHI data (4 km) were aggregated to the 0.1° grid using an arithmetic mean algorithm. This approach preserves the statistical integrity of the VHI data, providing a robust benchmark for validating our ED metrics at the same spatial scale. 

Hydrology Research Vol 56 No 11, 1186 



Figure 1 | Location of the study area. 

Table 2 | Data sources and specifications 

||Time|Temporal<br>resolution|Grid|Source|
|---|---|---|---|---|
|NDVI|1982–2020|Monthly|0.05°|https://www.ncei.noaa.gov|
|Surface Solar Radiation<br>(SSR)|1982–2020|Monthly|0.1°|https://cds.climate.copernicus.eu|
|TS|1982–2020|Monthly|0.1°|https://cds.climate.copernicus.eu|
|RH|1982–2020|Monthly|0.1°|https://cds.climate.copernicus.eu|
|U10|1982–2020|Monthly|0.1°|https://cds.climate.copernicus.eu|
|Surface Thermal<br>Radiation Downward|1982–2020|Monthly|0.1°|https://cds.climate.copernicus.eu|
|P|1982–2020|Monthly|0.1°|https://cds.climate.copernicus.eu|
|LUCC|1980,1990,1995,2000,2005,2010,2015,2020|Annual|0.1°|https://www.resdc.cn|
|VHI|1982–2020|Monthly|4 km|https://doi.org/10.6084/m9.figshare.19811854.v5|



## 3. METHODS 

### 3.1. Mutation and trend tests 

### 3.1.1. Mutation test 

The Pettitt test employs rank order statistics to identify mutation points in hydrometeorological time series. If the mutation point t exists in the original sequence {x1, x2, . . . , xT }, the sequence {x1, x2, . . . , xT } obeys the distribution of F1(x), and the sequence {xtþ1, xtþ2, . . . , xtþT } obeys F2(x), and F1(x) = F2(x). The original hypothesis H0 is that there is no mutation point t in the time series, and the alternative hypothesis H1 is that the time series does contain at least one mutation point t. 







Hydrology Research Vol 56 No 11, 1187 







where KT<sup>þcorresponds to a descending mutation and K</sup> T<sup>�corresponds to an ascending mutation, p corresponds to the signifi-</sup> cance level of KT<sup>þorK</sup> T<sup>�,andaisthegivensignificancelevel,p , arejectstheoriginalhypothesis,thereexistsamutation</sup> point in the original sequence, and the moment of the point of mutation is t. 

The Pettitt test is a non-parametric test that does not require the data to follow a normal distribution (Kundzewicz & Robson 2004). Compared with parametric tests (e.g., t-test), it avoids the risk of misclassification due to unsatisfied distributional assumptions, and it can accurately locate the position of the mutation points through the maximum rank statistic, which is more effective in detecting moderate-intensity change points than the piecewise regression models. 

### 3.1.2. Trend analysis 

Trend analysis is a linear regression analysis of time-varying variables using the principle of least squares, which detects trends in variables atthe pixel scale, and employstrend analysisto calculatechanges atthe pixel scale in order to reveal inter-annual trends and spatiotemporal dynamics of spatial and temporal changes in their characteristics. The Sen-MK method integrates Theil–Sen slope estimation and Mann–Kendall trend analysis to assess temporal trends in hydrometeorological datasets. 

Trends in crop coefficients (kc) and ED indicators were analyzed using Slope, and MK tests were separately applied to NDVI and VHI series. The Slope test is highly intuitive (Suroso et al. 2021) which provides intuitive numerical results by directly quantifying the strength of the trend through the value of the slope. The MK test is based on the non-parametric property of rank correlation (Gocic & Trajkovic 2013), is suitable for non-normal distributions of NDVI and VHI, and is highly reliable for datasets with sample sizes .30. 

### 3.2. Annual maximum value synthesis method 

kc was derived using the annual maximum NDVI synthesis method, which selects peak-growing-season NDVI values as primary inputs. This approach leverages the critical theoretical principle that annual maximum NDVI corresponds to peak vegetation conditions – characterized by maximal leaf area index, optimal canopy structure, and highest biomass – thus accurately capturing inter-annual photosynthetic capacity (Tucker 1979). By mitigating seasonal fluctuations, the method effectively eliminates short-term climatic noise and phenological disturbances, which enables robust estimation of potential maximum evapotranspiration under non-water-stressed conditions (Zhang et al. 2019a, b). Empirical validation confirms strong concordance between estimated and field-measured crop coefficients. 

### 3.3. Crop coefficients 

FAO-56 Manual (Allen et al. 1998) integrating various differences between plant evaporation and transpiration into kc. There is significant spatial heterogeneity in vegetation types and growth stages across regions, leading to varying kc. Referring to the categorization of growth stages (Jiang et al. 2022), the growth period is divided as follows: (i) calculate the mean NDVI values from January to December during the study period and sort them; (ii) The mid-growth period corresponds to the month with the maximum NDVI value and its adjacent 2 months before and after. The rapid growth period and late growth period are the month before and the 2 months after the mid-growth period, respectively; (iii) considering that the cumulative water deficit during the non-growth period also has a certain impact on vegetation growth, the vegetation coefficient for the remaining months is calculated based on the initial stage, which also ensures the integrity of the drought index series. 

kc represents the vegetation coefficient at different stages, such as the early growth stage (kc,ini), the rapid growth stage (kc,dev), the mid-growth stage (kc,mid), and the END GROWTH STAGE (kc,end). The calculation formula is as follows: 

kc,ini ¼ kc,ini(≏10) (6) 



Hydrology Research Vol 56 No 11, 1188 

kc,dev ¼ (kc,mid � kc,ini)=2 þ kc,ini 









kc,ini corresponds to the initial vegetation growth phase under precipitation infiltration less than 10 mm, which can be estimated from the FAO-56 Manual (Table 3). kc,full represents the coefficient at full canopy coverage. h represents the height of vegetation, the heights of grassland, scrubland, and woodland are set at 0.2, 1.5, and 5 m, respectively (Bo et al. 2010). fp represents actual vegetation coverage (0.01 , fp,1), which can be derived from remote sensing-based empirical formulas. sin (h) is the sine of the mean daily declination. NDVImin and NDVImax represent the minimum and maximum values of NDVI in each year, respectively. 

kc is defined as the ratio of actual crop evapotranspiration (ETa) and reference crop evapotranspiration (ET0), translating climate-driven potential water demand into actual water demand regulated by crops type (Zhang et al. 2023). kc as a bridge between vegetation physiological processes and climate-driven processes, can reflect crop water-demand characteristics, to reflect vegetation type specificity and growth stage dynamics (Lopez-Urrea et al. 2022). 

### 3.4. Ecological water deficit 

EWD is conventionally defined as the difference between effective precipitation and EWR (Chi et al. 2018; Feng & Su 2020). As there are other water resources supplied during vegetation growth, such as groundwater, Vicente-Serrano et al. (2018) improved the variable. By substituting effective precipitation with the actual water consumption by vegetation and deducting the evapotranspiration deficit from EWR, this approach provides a more precise representation of ecosystem water stress. 

### EWD ¼ EWC � EWR (12) 

EWC stands for ecological water consumption, mm. EWR stands for ecological water requirement, mm. EWR quantifies the volume of water necessary to sustain ecosystem functionality and health, which corresponds to the evapotranspiration of vegetation under ideal conditions without moisture, pest, and salinity stress. The calculation formula is as follows ( Jiang et al. 2021): 



EWR is derived by multiplying the crop coefficients by the crop reference evapotranspiration ET0. ET0 is calculated using the Penman–Monteith formula in FAO-56 (Allen et al. 1998). 



Table 3 | Assigned values of crop coefficients for precipitation infiltration depth , 10 mm 

|Humidity interval|Atmospheric evaporat<br>1-3 mm/day|ion intensity (ET0)<br>3-5 mm/day|5-7 mm/day|. 7 mm/day|
|---|---|---|---|---|
|Less than once a week|1.2－0.8|1.1－0.6|1.0－0.4|0.9－0.3|
|Once a week|0. 8|0.6|0.4|0.3|
|More than once a week|0.7－0.4|0.4－0.2<sup>a</sup>|0.4－0.2<sup>a</sup>|0.2－0.1|



> aAttention should be paid to the fact that excessive irrigation intervals will not be able to maintain sufficient transpiration of 1-year-old young crops. 

Hydrology Research Vol 56 No 11, 1189 

where ET0 is crop reference evapotranspiration; D is the slope of the saturation vapor pressure versus temperature curve; Rn is net radiation at the crop surface, MJ/(m<sup>2</sup> ·day); G is soil heat flux, MJ/(m<sup>2</sup> ·day); g is the wet-bulb constant; T is mean air temperature, °C; u2 is the mean wind speed at 2 m height, m/s; es is the saturation vapor pressure, kPa; ea is the actual vapor pressure, kPa for specific calculations. 

EWC refers to the water that must be lost to maintain the normal function of ecological vegetation, mainly including vegetation transpiration, inter-tree soil evaporation, and canopy interception evaporation of vegetation. The calculation formula is as follows (Qi 2017; Jiang et al. 2022): 

EWC ¼ Fr � ETa (15) 





NDVImax stands for the maximum value of NDVI at full vegetation cover among the growth stage. 

Although remotely sensed indicators can indirectly reflect the ecological impacts of drought through vegetation cover and ET, quantifying the dynamic balance between ecosystem water supply and demand remains challenging. Therefore, an index that integrates vegetation status, ET dynamics, and ecological water-demand consumption imbalance needs to be introduced to monitor ED (Wang et al. 2023a, b). 

### 3.5. Vegetation health index 

Drought affects the degree of stomatal opening and closing of vegetation, which in turn affects plant growth. Under adequate water availability, plants maintain optimal transpiration rates, and vegetation indices remain stable. Conversely, drought conditions induce partial stomatal closure, diminishing transpiration and leading to reduced vegetation indices. VHI scaled between 0 and 100 exhibits an inverse relationship with regional drought severity. The VHI is mathematically expressed as follows: 

### VHI ¼ aVCI þ (1 � a)TCI 



VHI contains two components: the vegetation condition index (VCI), reflecting vegetation greenness, and the temperature condition index (TCI), representing thermal conditions. A weighting coefficient (α) modulates their relative contributions within the VHI. Referring to the relevant norms and combining with the relevant studies in the YRB (Fathi-Taperasht et al. 2022), the class classification criteria of the drought index are just like the search (Zhang et al. 2015). 

To determine the optimal weighting parameters a, the range of values was set from 0.02 to 0.98 (with a step size of 0.02 and a total of 49 discrete values), and the VHI corresponding to each value was computed. Pearson correlation analysis was used to evaluate the spatial correlation between self-calibrating Palmer Drought Severity Index (sc-PDSI) and VHI, and accordingly selected the optimal combination of weights for VCI and TCI across ecoregions, and the annual VHI data were finally calculated the year-by-year VHI data based on the optimized a values. 

VHI has been selected in the FAO Global Agricultural Drought Monitoring System (GADMS), the essence of which is to assess integrated vegetation stress responses of vegetation. Moreover, it has been pointed out that VHI is highly applicable in determining the drought status of vegetation in the YRB (Yang et al. 2024). 

### 3.6. Reproducibility statement 

To ensure the full reproducibility of this study, the article provides the following details. All input datasets used in this analysis are publicly available. The NDVI data were obtained from the [A vhrr land NDVI dataset] (https://www.ncei.noaa.gov). The meteorological data (including surface pressure, relative humidity, etc.) were sourced from the [ERA5-Land monthly averaged data from 1950 to present] dataset (https://cds.climate.copernicus.eu). The land-use data were derived from the [China’s Land-Use/Cover Datasets (CNLUCC)] (https://www.resdc.cn). The vegetation health data were derived from [an improved global vegetation health index dataset] (https://doi.org/10.6084/m9.figshare.19811854.v5). To facilitate the full replication of this study, the supplementary material provides the complete data sources, a detailed workflow chart, and all mathematical formulations used in the analysis. 

Hydrology Research Vol 56 No 11, 1190 



Figure 2 | Schematic diagram of the workflow. 

The computational workflow is outlined in Figure 2. The calculation of ET0 is based on the Penman–Monteith formula, and specific parameters refer to FAO-56 Manual (Allen et al. 1998). 

## 4. RESULTS 

### 4.1. Trend analysis and mutation of NDVI 

Data processing employed the annual maximum synthesis method. Trends in NDVI time series and mutation points were statistically validated using Sen’s slope estimator and Pettitt’s test, respectively, with results presented in Figure 3(f). 

Sen’s trend analysis revealed significant spatiotemporal patterns of NDVI across the YRB during 1982–2020. Spatial distribution of annual maximum NDVI (Figure 3(a)) exhibited a declining south-north gradient (0.05–0.8) with elevated NDVI in eastern/western sectors and depressed values centrally. Zonal analysis (Figure 3(c)) identified Subregions 3–5 (Loess Plateau) as persistent NDVI minima (means: 0.37, 0.30, 0.44), attributable to synergistic semi-arid climatic constraints and topographic complexity. Inter-annual trends (Figure 3(e)) demonstrated statistically significant increases in basin-wide NDVI. 

Figure 3(b) delineated spatiotemporal trends of annual maximum NDVI (1982–2020), revealing increasing trajectories across 95.3% of the basin, with 88% exhibiting statistically significant gains (P, 0.05). This trend was particularly pronounced in the middle reaches, attributable to synergistic effects of ecological restoration policies (e.g., Grain for Green Program) and favorable climatic shifts. Implementation of the Three-North Shelter Forest Program since 1999 has converted steep-slope cropland to forest-grassland, driving marked NDVI enhancement in critical zones like Subregion 5. Pettitt’s change-point detection applied to NDVI values identified a significant shift circa 2003 in the basin’s annual maximum NDVI series (1982–2020), as visualized in Figure 3(f). Concurrently, middle-reach precipitation exhibited synchronous inflection during 2003. In 2002 and before, the precipitation and ET in upper basin regions showed a decreasing trend, but since 2003, both precipitation and ET have begun to increase. Consequently, the study period was partitioned into 1982–2002 and 2003–2020 phases for comparative analysis. 

### 4.2. Spatial and temporal evolution of crop water-demand characteristics 

kc was employed to quantify vegetation water-demand dynamics, with their fluctuations directly governed by physiological changes in vegetation and ground cover conditions. Growth stages were classified as: early growth, rapid growth, mid-growth, 

Hydrology Research Vol 56 No 11, 1191 



Figure 3 | Spatiotemporal patterns of NDVI Series (1982–2020): (a) mean value distribution; (b) trend analysis; (c) zonal statistics; (d) zonal trend metrics; (e) multi-year mean variation; (f) change-point detection. 

and late growth. It depicts spatial distributions of kc across growth stages: early growth (Figure 4(a) and 4(b)); rapid growth (Figure 4(c) and 4(d)); mid-growth (Figure 4(g) and 4(h)); late growth (Figure 4(j) and 4(k)). kc in the YRB ranged from 0.1 to 0.8, with stage-specific intervals: early growth (0.11–0.6); rapid growth: (0.15–0.71); mid-growth: (0.12–0.79); late growth: (0.15–0.77). Coefficient magnitudes peaked during mid-growth, followed by rapid growth and late growth, while early growth exhibited minimal values, aligning with established findings. Spatially, kc for both the 1982–2002 and 2003–2020 periods exhibited consistent geographical patterns, with high water demand in northern sectors. High-value clusters concentrated in southwestern Subregion 1 and northeastern Subregion 3 – dominated by forests, croplands, scrublands, and 

Hydrology Research Vol 56 No 11, 1192 



Figure 4 | Spatial distribution and characteristic metrics of crop coefficients in the YRB: early growth (a, b; c), rapid growth (d, e, f), midgrowth (g, h, i), late growth (j, k, l). 

grasslands. Elevated temperatures, high wind velocities, and dense ground cover primarily drove heightened crop water requirements in these zones. 

Trend analysis of kc across four growth stages (1982–2020) revealed consistent northward-increasing and southward-declining trajectories throughout the YRB. Rising trends predominated in southern sectors (42.8–48% areal coverage), while 

Hydrology Research Vol 56 No 11, 1193 



Figure 5 | Spatiotemporal trends and zonal statistics of kc in the YRB: early growth (a, b), rapid growth (c, d), mid-growth (e, f), late growth (g, h). 

decreases concentrated in the lower basin (Figure 5). Elevated water demands intensified ED vulnerability, particularly where kc surged. Subregional distributions of these trends are quantified (Table 4). 

The most significant upward trends were observed in Subregions 3–5. These subregions encompass the Ningxia and Hetao Plains within the YRB. Crop water demand in these plains demonstrated a significant upward trend (0.05–0.09/decade) from 1980 to 2020 (P , 0.05). This trend was attributed to synergistic effects of climatic shifts, agricultural policy transitions, and biophysical processes (Zhang et al. 2011; Liu et al. 2023). Climate change led to increased mean annual temperatures and extended growing seasons by 8–12 days, thereby expanding crop water demand. These policies’ agricultural policy 

Hydrology Research Vol 56 No 11, 1194 

Table 4 | Percentage of area with elevated kc during different growing periods (%) 

||YRB|1|2|3|4|5|6|7|8|
|---|---|---|---|---|---|---|---|---|---|
|kc,ini|42.8|39.6|68.4|87.4|83.3|71.6|37.3|9.1|19.2|
|kc,dev|46.8|41.4|72.1|74.7|73.4|65|34.9|8.1|19.6|
|kc,mid|43|45.9|72.2|80.2|80.3|70.5|35.1|9.7|22.9|
|kc,end|48|54.9|75.9|68.3|76.8|63.8|39.6|8.6|23.6|



interventions contributed to elevated water demand through the expansion of maize cultivation in Ningxia, which systematically replaced low-water-demand spring wheat. 

### 4.3. Spatial and temporal evolution of ED indicators 

The EWR, EWC, and EWD in the YRB showed obvious spatial differences (Figure 6). EWR exhibited a pronounced southward-declining gradient (151–890 mm). Peak EWR clustered in Subregions 3 (195–890 mm), 4 (227–740 mm), and 5 (213–760 mm), contrasting with minimal demands in Subregions 1 (151–460 mm) and 2 (152–560 mm). The spatial distribution of EWR was similar to that of kc, which also showed the close synergistic relationship between kc and EWR. Conversely, EWC increased southward (17–460 mm), reaching maxima in Subregions 6 (61–350 mm), 7 (130–340 mm), and 8 (130–460 mm) while Subregions 3–5 maintained lower values (18–284 mm). Southern deciduous broadleaf forests and croplands drove elevated EWC, amplified by higher field capacity, whereas northern grasslands/ deserts constrained transpiration. Precipitation gradients, soil properties, and vegetation structure collectively orchestrated these patterns. 

The spatial distribution of EWD mirrored EWR, severe EWD concentrated in Subregions 3–5 (0–804 mm). Fundamentally, EWD stems from supply–demand imbalances, particularly in northern sectors where high EWR (predominantly croplanddriven) and constrained water-consuming capacity (limited by edaphic and vegetative conditions) drive significant shortages. 



Figure 6 | Spatial distribution and temporal dynamics of EWR (a, d), EWC (b, e), EWD (c, f) in the YRB. 

Hydrology Research Vol 56 No 11, 1195 

Severe EWD concentrated in Subregions 3 (71–804 mm), 4 (125–536 mm), and 5 (0–634 mm), whereas Subregions 6–8 showed negligible deficits (uniformly less than 300 mm). 

Research has found that EWD is severe in Subregions 3–5, especially in the southern part of Inner Mongolia and the northern part of Shanxi, which roughly coincides with the "Ordos-Yulin Critical Water Deficit Zone". The Yellow River Basin soil and water conservation bulletin 2024 (Yellow River Conservancy Commission 2024) indicates that the degree of soil erosion in this area is serious. 

Trend trajectories of EWR, EWC, and EWD across the study period were analyzed for the YRB, and generated boxplots for each subregion. The results demonstrate that EWR exhibited an increasing trend, with 69.3% of the basin area experiencing rising demands. Notably, this trend was predominantly observed in the central and northern sectors of the basin, specifically in Subregions 3–5, where increasing EWR was detected across 86.7, 95.4, and 72.9% of their respective areas. Similarly, EWC showed a widespread increasing trend, observed in 98.5% of the basin, among which Subregions 4 and 5 exhibited particularly pronounced increases. In contrast, EWD generally displayed a decreasing trend, in 54.6% of the area. Persistent ED conditions were maintained in Subregions 2–4, whereas significant alleviation trends were evident in Subregions 6–8. 

A detailed analysis was further performed on temporal variations in the maximum, minimum, mean, and standard deviation of EWD across the eight subregions of the YRB (Figure 7(d)–7(f)). Collectively, the characteristic metrics of EWD exhibited a progressive reduction over time, which further validated the alleviation trend of ED within the YRB during the study period (Figure 8). 

## 5. DISCUSSION 

### 5.1. VHI cross-validation 

Quantitative results from this study were compared with previously published datasets as summarized in Table 5. 

The VHI effectively characterizes ED through the integration of water stress and thermal stress. A significant negative correlation was observed between VHI and ED severity, indicating declining VHI values during intensifying drought. Over the 



Figure 7 | Spatiotemporal trends and zonal box plots of EWR (a, d), EWC (b, e), and EWD (c, f) in the YRB. 

Hydrology Research Vol 56 No 11, 1196 



Figure 8 | Temporal variations in characteristic metrics of EWD across subregions in the YRB. 

period 1982–2020, an overall increasing trend in VHI was detected across the YRB (Figure 9(b)), particularly in Subregions 5–8. This trend indicates an alleviation of ED in these areas. 

Cross-validation analyses were conducted between ED distributions derived from the EWD framework in this study and VHI assessments. High consistency between EWD and VHI was observed in mid-lower reaches of the YRB (Subregions 6–8), whereas significant assessment discrepancies were identified across Subregions 2–4. 

These discrepancies are attributed to synergistic effects of acute water scarcity, delayed vegetation response, and subsurface heterogeneity. Notably, EWD is calculated based on water-demand-consumption balance, primarily reflecting systemic water carrying capacity. Conversely, VHI is derived from vegetation indices and climatic variables, capturing short-term vegetation 

Table 5 | Comparative analysis of ecological water metrics with established literature values (mm) 

|Study area|Type|Results of study|Literature values|
|---|---|---|---|
|The Yellow River Source Area|EWR|80–350|54–200 (Tianet al.2025)|
|Wetlands in the upstream of the YR|EWR|400–800|750–1,200 (Zhanget al.2014b; Sunet al.2010)|
|Guanzhong in Shaanxi|EWR|423.6–443.2|408–582 (Zhang 2018)|
|The upper and middle of the YRB|EWC|269–622|280–520 (Wang 2022)|
|Qaidam Basin|EWC|33–245|22–200 (Ma 2022)|
|Wuchuan County|EWD|58–62.5|46–55.4 (Zhanget al.2014a)|
|Minqin County|EWD|112–230|102–195 (Boet al.2010)|



Hydrology Research Vol 56 No 11, 1197 



Figure 9 | Spatial distribution pattern of mean VHI (a), temporal trend variation (b), zonal box plots by subregion (c), and ED characterization (d) in YRB. 

growth dynamics and stress responses. Fundamentally distinct computational principles underlie these two metrics. Geographically, Subregion 2 occupies the Loess Plateau, while Subregions 3 and 4 are situated within the Loess Plateau. In these areas, highly porous soils contribute to persistently elevated EWD values, whereas VHI responses to soil moisture exhibit temporal lags. This asynchrony results in divergent ED assessments. Drought impacts manifest differential temporal lags across surface runoff, vegetation productivity, and grain yield systems, with spatial heterogeneity observed in lag duration across geographic regions. 

### 5.2. Driving factor analysis 

### (i) Exploring the driving mechanisms of NDVI variations 

The abrupt shift in NDVI was observed in the YRB around 2003. This shift coincided temporally with the implementation of nationwide ecological restoration programs such as the ‘Grain for Green’ initiative (Yang et al. 2021). Vegetation growth in the headwaters region of the YRB is partially constrained by natural climatic conditions, rendering it relatively insensitive to policy interventions and short-term climatic fluctuations. The Loess Plateau in the middle of the YRB maintains relatively abundant vegetation cover. The upward trend in NDVI is influenced by the synergistic effects of climate and policy (Yu et al. 2013; Gu 2024). The lower part of YRB is predominantly cultivated land, significantly influenced by anthropogenic factors. Since 2003, rapid urbanization has increased impervious surfaces, exacerbating vapor pressure deficit (VPD), leading to declining NDVI trends in some areas (Yuan et al. 2020; Tian et al. 2021). 

Moreover, elevated CO2 concentrations under global change may stimulate vegetation growth through the fertilization effect (Feng et al. 2016), though the magnitude of this effect exhibits considerable uncertainty across different regions and 

Hydrology Research Vol 56 No 11, 1198 

vegetation types. Furthermore, it may interact with other stressors, such as increased VPD, thereby complicating predictions of future vegetation dynamics. 

### (ii) Exploring the driving mechanisms of ED assessment indicators 

An ED framework was developed through "Vegetation–ET–Water balance" to quantify the vegetation drought from the perspective of the ecosystem, and elucidated the spatiotemporal evolution mechanisms of ED in the YRB. Research has found that EWD is severe in Subregions 3–5, especially in the southern part of Inner Mongolia and the northern part of Shanxi. Mechanistically, this configuration stems from synergistic drivers: In northern sectors, substantial EWD originates from mismatches between high EWR and low EWC. Conversely, moderate drought conditions prevailed in lower reaches (Subregions 6–8) due to adequate precipitation, diverse vegetation cover, and cultivation of low-water-demand crops. Climate warming (0.34 °C/decade) intensified EWR through enhanced potential evapotranspiration, while crop restructuring in the Ningxia Plain further exacerbated water imbalances through increased evapotranspiration per unit area. Regarding EWC, abundant precipitation and high soil water retention sustained elevated consumption in southern subregions, whereas northern grasslands maintained water conservation via stomatal regulation adaptations. Spatially, mild drought alleviation was detected in the Hetao Irrigation District (Subregion 1), stable conditions persisted in the Loess Plateau core (Subregions 2–4), and significant mitigation occurred in the lower alluvial plains (Subregions 6–8). These findings align with existing research: Luan et al. (2025) confirmed greater drought intensity upstream using the standardized water storage deficit index (WSDI), and Lu et al. (2024) reported drought alleviation in 94% area of YRB during 2001–2020 via Net Primary Productivity NPP analysis, consistent with conclusions drawn herein. 

### 5.3. Uncertainty analysis 

### (i) Quantitative uncertainty budget analysis 

To align with 0.1° meteorological input data and ensure computational consistency, this study employed bilinear interpolation to resample 0.05° NDVI data to 0.1° resolution. Bilinear interpolation preserves spatial continuity of the data, ensuring that vegetation parameters (e.g., fp and kc) and subsequent drought indicators (EWR, EWC, EWD) accurately reflect regional gradients and spatial coherence, thereby providing a reliable foundation for basin-scale trend analysis. 

To systematically evaluate the uncertainty introduced by resampling high-resolution NDVI (0.05°) data to 0.1°, this study designed the following quantitative analysis workflow. The original 0.05° NDVI data were aggregated using algorithmic averaging and bilinear interpolation to sample at the same resolution (0.1°), with their mean absolute error and root mean square error systematically quantified. Results indicate that bilinear interpolation yields high consistency with the arithmetic mean benchmark (correlation coefficient R . 0.99), demonstrating its effective preservation of pixel-average information within the study area (Figure 10). Moreover, the fp and Fr indices calculated from NDVI represent standardized indices based on relative NDVI values, dependent on relative pixel values rather than absolute spatial detail. Consequently, subsequent computations using resampled NDVI data are credible. 

Although this study provides preliminary insights into ED assessment, certain limitations in computational methodologies must be acknowledged. Specifically, empirical formulas employed for estimating kc and EWC rely on statistical relationships between NDVI and key parameters (e.g., evapotranspiration, soil moisture) calibrated for specific regions or conditions. However, their applicability remains uncertain in areas with complex vegetation mosaics or non-representative ecosystems. 

### (ii) Regional uncertainty 

Uncertainty in the core ED metrics (EWR, EWC, EWD) is visually presented (Figure 11) using bar charts with 95% confidence intervals. These illustrate the mean values and estimation uncertainty across eight subregions and two time periods (1982–2002 and 2003–2020), offering a transparent depiction of the spatial heterogeneity and precision in drought assessment within the YRB. 

### 5.4. Limitations and future directions 

This study describes drought phenomena based on surface water and soil water, analyzing the complete process of ‘vegetation growth status – vegetation evapotranspiration – water supply and demand balance’, reflecting the combined effects of meteorological conditions, soil moisture, and vegetation physiological status. However, groundwater constitutes a vital water source for vegetation growth, and the omission of groundwater factors represents a limitation of this research. Neglecting 

Hydrology Research Vol 56 No 11, 1199 



Figure 10 | Aggregation (a, c) and resampling (b, d) results for the periods 1982–2002 and 2003–2020. 



Figure 11 | Visualization of uncertainty across subregions of the YRB. 

groundwater factors implies reliance on EWC that cannot fully represent actual conditions, potentially leading to an underestimation of EWD. In recent years, research exploring the relationship between groundwater and NDVI has gradually increased (Lv et al. 2013; Wang et al. 2014; Zhang et al. 2020). Vegetation richness peaks at groundwater depths of 2–4 m (Hao et al. 2009). 

Hydrology Research Vol 56 No 11, 1200 

To explicitly quantify groundwater contributions, future work will integrate GRACE satellite data with high-resolution hydrological models to develop a coupled surface–subsurface simulation framework. This refinement will provide a more mechanistic understanding of vegetation responses to water stress and enhance the accuracy of ED early warning systems. 

## 6. CONCLUSIONS 

Research developed an ED framework through ‘Vegetation-ET-Water balance’ to quantify vegetation drought impacts from the perspective of the ecosystem, and elucidated the spatiotemporal evolution mechanisms of ED in the YRB (1982– 2020). Spatiotemporal distribution patterns and evolutionary trends of NDVI were analyzed using Sen’s slope estimator and Pettitt’s test, revealing 2003 as a significant change-point year. Based on secondary water resource zoning, the YRB was partitioned into eight subregions. Crop coefficients were computed from NDVI, enabling subsequent derivation of EWR, EWC, and EWD. This integrated framework facilitated spatiotemporal assessment of ED metrics across all subregions. Cross-validation was performed using VHI to examine terrestrial ED evolution in the YRB. The principal findings are summarized as follows: 

- (1) Significant vegetation recovery was observed. NDVI in YRB ranged from 0.05 to 0.8, with an abrupt shift occurring circa 2003. Subregions 3–5 exhibited lower values relative to other areas, while 95.3% area of YRB demonstrated increasing trends. Leading to the division of the study period into two subperiods: 1982–2002 and 2003–2020. 

- (2) Enhanced spatial differentiation in crop water demand was identified. Crop coefficients across the YRB ranged from 0.1 to 0.8, peaking during the mid-growth stage (0.12–0.79), followed by rapid growth (0.15–0.71) and late growth stages (0.15– 0.77), with the early growth stage exhibiting the lowest values (0.11–0.6). Pronounced spatial heterogeneity was observed, manifested as predominantly increasing trends in northern sectors contrasted with decreasing patterns in southern regions. Notably, more than 63.8% of Subregions 3–5 exhibited elevated Crop coefficients across all growth stages. 

- (3) Distinct gradient patterns in ED Indicators were established. EWR (151–890 mm) decreased from north to south, whereas EWC (17–460 mm) demonstrated an opposite increasing trend. The spatial distribution of EWD (0–804 mm) mirrored that of EWR, high values are mainly in the northern area, with peak values concentrated in Subregions 3–5. This spatial configuration coincided with the Ordos-Yulin Severe Water Deficit Zone documented in official hydrological reports. 

- (4) A predominantly alleviating drought trend was observed. EWR and EWC as a whole showed an upward trend (69.3 and 98.5% area of YRB have increased), while the EWD showed a downward trend (54.6% area of YRB has decreased). The terrestrial ED in the Loop Irrigation Area (Subregion 1) was slightly alleviated, the core area of the Loess Plateau (Subregions 2–4) remained stable, and the drought in the downstream alluvial plain (Subregions 6–8) was significantly alleviated. 

## ACKNOWLEDGEMENTS 

This work was financially supported by the Yinshanbeilu Grassland Eco-hydrology National Observation and Research Station, China Institute of Water Resources and Hydropower Research (YSS202301); and the National Natural Science Foundation of China (52479009). 

## DECLARATION OF COMPETING INTEREST: 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

## DATA AVAILABILITY STATEMENT 

All relevant data are available from an online repository or repositories. 

## CONFLICT OF INTEREST 

The authors declare there is no conflict. 

## REFERENCES 

- Allen, R. G., Pereira, L. S., Raes, D. & Smith, M. (1998) Crop Evapotranspiration-Guidelines for Computing Crop Water Requirements-FAO Irrigation and Drainage Paper 56, Vol. 300(9). Rome: Fao, pp. D05109. 

Hydrology Research Vol 56 No 11, 1201 

- Anderegg, W. R., Trugman, A. T., Badgley, G., Konings, A. G. & Shaw, J. (2020) Divergent forest sensitivity to repeated extreme droughts, Nature Climate Change, 10 (12), 1091–1095. https://doi.org/10.1038/s41558-020-00919-1. 

- Bo, H. A. O., Xiaoling, S. & Xiaoyi, M. (2010) Study on ecological water requirement for natural vegetation in Minqin County of Gansu Province, Journal of Northwest Agriculture and Forestry University, 38, 158–164. 

- Cao, R., Zhang, Y., Fernández-Martínez, M., Zhang, Z., Lai, G., Ju, W. & Peñuelas, J. (2025) Global evidence for a positive relationship between tree species richness and ecosystem photosynthesis, Nature Plants, 11 (7), 1429–1440. https://doi.org/10.1038/s41477-02502046-1. 

Chen, S., Stark, S. C., Nobre, A. D., Cuartas, L. A., de Jesus Amore, D., Restrepo-Coupe, N., Smith, M. N., Chitra-Tarak, R., Ko, H., Nelson, B. W. & Saleska, S. R. (2024) Amazon forest biogeography predicts resilience and vulnerability to drought, Nature, 631, 111–117. https://doi.org/10.1038/s41586-024-07568-w. 

Chi, D., Wang, H., Li, X., Liu, H. & Li, X. (2018) Estimation of the ecological water requirement for natural vegetation in the Ergune River basin in northeastern China from 2001 to 2014, Ecological Indicators, 92, 141–150. https://doi.org/10.1016/j.ecolind.2017.04.014. Chiang, F., Mazdiyasni, O. & AghaKouchak, A. (2021) Evidence of anthropogenic impacts on global drought frequency, duration, and intensity, Nature Communications, 12, 2754. https://doi.org/10.1038/s41467-021-22314-w. 

- Cui, B., Hua, Y., Wang, C., Liao, X., Tan, X. & Tao, W. (2010) Estimation of ecological water requirements based on habitat response to water level in Huanghe River Delta, China, Chinese Geographical Science, 20, 318–329. https://doi.org/10.1007/s11769-010-0404-6. 

- Ding, H., Shi, X., Yuan, Z., Chen, X., Zhang, D. & Chen, F. (2024) Does vegetation greening have a positive effect on global vegetation carbon and water use efficiency?, Science of the Total Environment., 951, 175589. https://doi.org/10.1016/j.scitotenv.2024.175589. 

- Fairbairn, A. J., Katholnigg, S., Leichtle, T., Merkens, L., Schroll, L., Weisser, W. W. & Meyer, S. T. (2025) NDVI and vegetation volume as predictors of urban bird diversity, Scientific Reports, 15, 12863. https://doi.org/10.1038/s41598-025-96098-0. 

Fathi-Taperasht, A., Shafizadeh-Moghadam, H., Minaei, M. & Xu, T. (2022) Influence of drought duration and severity on drought recovery period for different land cover types: evaluation using MODIS-based indices, Ecological Indicators, 141, 109146. https://doi.org/10. 1016/j.ecolind.2022.109146. 

Feng, K. & Su, X. (2020) Spatiotemporal response characteristics of agricultural drought to meteorological drought from a three-dimensional perspective, Transactions of the Chinese Society of Agricultural Engineering, 36 (8), 103–113. 

Feng, X., Fu, B., Piao, S., Wang, S., Ciais, P., Zeng, Z., Lü, Y., Zeng, Y., Li, Y., Jiang, X. & Wu, B. (2016) Revegetation in China’s Loess plateau 

is approaching sustainable water resource limits, Nature Climate Change., 6 (11), 1019–1022. https://doi.org/10.1038/nclimate3092. Ghobadi, M. & Badehian, Z. (2025) Assessment of agricultural drought severity using multi-temporal remote sensing data in Lorestan region, Scientific Reports, 15, 18528. https://doi.org/10.1038/s41598-025-03087-4. 

Gocic, M. & Trajkovic, S. (2013) Analysis of changes in meteorological variables using Mann-Kendall and Sen’s slope estimator statistical tests in Serbia, Global and Planetary Change, 100, 172–182. https://doi.org/10.1016/j.gloplacha.2013.01.002. 

- Gu, T. (2024) Climate Change Impacts on the Ecological Environment of the Yellow River Basin. Unpublished doctoral dissertation, Lanzhou University. https://doi.org/10.27204/d.cnki.glzhu.2024.001324. 

Hao, X., Li, W. & Huang, X. (2009) Assessment of the groundwater threshold of desert riparian forest vegetation along the middle and lower reaches of the Tarim river, China, Hydrological Processes, 24 (2), 178–186.doi:10.1002/hyp.7432. 

- Higgins, S. I., Conradi, T. & Muhoko, E. (2023) Shifts in vegetation activity of terrestrial ecosystems attributable to climate trends, Nature Geoscience, 16, 147–153. https://doi.org/10.1038/s41561-022-01114-x. 

- IPCC (2022) Climate Change 2022: Mitigation of Climate Change. Contribution of Working Group III to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change. Cambridge, UK: Cambridge University Press. doi:10.1017/9781009157926. 

- Javed, T., Li, Y., Rashid, S., Li, F., Hu, Q. & Pulatov, B. (2021) Performance and relationship of four different agricultural drought indices for drought monitoring in China’s mainland using remote sensing data, Science of the Total Environment, 759, 143530. https://doi.org/10. 1016/j.scitotenv.2020.143530. 

- Jha, S., Das, J., Sharma, A., Hazra, B. & Goyal, M. K. (2019) Probabilistic evaluation of vegetation drought likelihood and its implications to resilience across India, Global and Planetary Change, 176, 23–35. https://doi.org/10.1016/j.ejrh.2024.101778. 

- Jiang, T. L. (2022) Spatiotemporal Evolution Characteristics of Ecological Drought in Northwest China and its Response to Meteorological Drought and Groundwater Drought. Doctoral dissertation, Northwest A&F University. https://doi.org/10.27409/ d.cnki.gxbnu.2022.002324. 

- Jiang, Z., Liu, H., Wang, H., Peng, J., Meersmans, J., Green, S. M., Quine, T. A., Wu, X. & Song, Z. (2020) Bedrock geochemistry influences vegetation growth by regulating the regolith water holding capacity, Nature Communications, 11, 2392. https://doi.org/10.1038/s41467020-16156-1. 

- Jiang, T., Su, X., Singh, V. P. & Zhang, G. (2021) A novel index for ecological drought monitoring based on ecological water deficit, Ecological Indicators, 129, 107804. https://doi.org/10.1016/j.ecolind.2021.107804. 

- Jiang, T., Su, X., Singh, V. P. & Zhang, G. (2022) Spatio-temporal pattern of ecological droughts and their impacts on health of vegetation in northwestern China, Journal of Environmental Management, 305, 114356. https://doi.org/10.1016/j.jenvman.2021.114356. 

- Jiao, W., Wang, L., Wang, H., Lanning, M., Chang, Q. & Novick, K. A. (2022) Comprehensive quantification of the responses of ecosystem production and respiration to drought time scale, intensity and timing in humid environments: a FLUXNET synthesis, Journal of Geophysical Research: Biogeosciences, 127 (5), e2021JG006431. https://doi.org/10.1029/2021JG006431. 

Hydrology Research Vol 56 No 11, 1202 

- Khosravi, Y. & Ouarda, T. B. M. J. (2025) Drought risks are projected to increase in the future in central and southern regions of the Middle East, Communications Earth & Environment, 6, 384. https://doi.org/10.1038/s43247-025-02359-1. 

- Kundzewicz, Z. W. & Robson, A. J. (2004) Change detection in hydrological records – a review of the methodology/Revue méthodologique de la détection de changements dans les chroniques hydrologiques, Hydrological Sciences Journal, 49 (1), 7–19. https://doi.org/10.1623/ hysj.49.1.7.53993. 

- Lai, J., Kooijmans, L. M. J., Sun, W., Lombardozzi, D., Campbell, J. E., Gu, L., Luo, Y., Kuai, L. & Sun, Y. (2024) Terrestrial photosynthesis inferred from plant carbonyl sulfide uptake, Nature, 634, 855–861. https://doi.org/10.1038/s41586-024-08050-3. 

- Li, X., Xia, K., Wu, T., Wang, S., Tang, H., Xiao, C., Tang, H., Xu, N. & Jia, D. (2024) Increased precipitation has not enhanced the carbon sequestration of afforestation in northwest China, Communications Earth & Environment, 5, 619. https://doi.org/10.1038/s43247-02401733-9. 

- Liu, Z., Li, L., Li, H., Liu, N., Wang, H. & Shao, L. (2023) Changes and influencing factors of crop coefficient of summer maize during the past 40 years in the north China plain, Chinese Journal of Eco-Agriculture, 31 (9), 1355–1367. https://doi.org/10.12357/cjea.20230197. 

- Lopez-Urrea, R., Martín de Santa Olalla, F., Montoro, A. & López-Fuster, P. (2022) Single and dual crop coefficients and water requirements for onion through field and modeling approaches, Agricultural Water Management, 272, 107879. https://doi.org/10.1016/j.agwat.2022. 107879. 

- Lu, D., Wei, W. & Wang, J. P. (2024) Important ecological function areas drought spatiotemporal evolution and its impact on key resources: a case study of the Yellow River basin, Huanjing Kexue, 45 (6), 3352–3362. https://doi.org/10.13227/j.hjkx.202306195. 

- Lu, Y., Yu, Y., Sun, L., Li, C., He, J., Guo, Z., Duan, L., Zhang, J. & Yu, R. (2025) NDVI based vegetation dynamics and responses to climate change and human activities at Xinjiang from 2001 to 2020, Scientific Reports, 15, 25848. https://doi.org/10.1038/s41598-02511677-5. 

- Luan, K., Xue, J. & Feng, G. (2025) Drought characteristics of terrestrial water storage in the Yellow River basin based on GRACE/GRACEFO, Arid Zone Research, 42, 246–257. 

- Lv, J., Wang, X., Zhou, Y., Qian, K., Wan, L., Eamus, D. & Tao, Z. (2013) Groundwater-dependent distribution of vegetation in Hailiutu River catchment, a semi-arid region in China, Ecohydrology, 6 (1), 142–149. https://doi.org/10.1002/eco.1254. 

- Ma, L. (2022) Study on Ecological Water Consumption in the Xiangride River Basin of Qaidam Basin. Master’s thesis, Qinghai Normal University. https://doi.org/10.14042/j.cnki.32.1309.2023.05.007. 

- Meng, X., Yu, Y. & Ginoux, P. (2025) Rise in dust emissions from burned landscapes primarily driven by small fires, Nature Geoscience, 18, 586–592. https://doi.org/10.1038/s41561-025-01730-3. 

- Ncisana, L., Nyathi, M. K., Mkhize, N. R., Mabhaudhi, T., Tjelele, T. J., Mbambalala, L. & Modi, A. T. (2024) Water use efficiency (WUE) and nutrient concentration of selected fodder radish (Raphanus sativus L.) genotypes for sustainable diets, Scientific Reports, 14, 31315. https://doi.org/10.1038/s41598-024-82727-7. 

- Qi, R. (2017) Relationship Between Eco-Hydrological Indices and Groundwater in the Ordos Plateau. Doctoral dissertation, China University of Geosciences, Beijing. 

- Shi, M., Yuan, Z. & Shi, X. (2022) Drought assessment of terrestrial ecosystems in the Yangtze river Basin, China, Journal of Cleaner Production, 362, 132234. https://doi.org/10.1016/j.jclepro.2022.132234. 

- Sun, L., Si, X. L. & Liao, Z. Q. (2010) Study on ecological water requirement of wetland in the north of Yellow River delta, Yellow River, 32 (12), 112–113. CNKI:SUN:RMHH.0.2010-12-047. 

- Suroso, S., Nadhilah, D., Ardiansyah & Aldrian, E. (2021) Drought detection in java island based on standardized precipitation and evapotranspiration index (SPEI), Journal of Water and Climate Change, 12 (6), 2734–2752. https://doi.org/10.2166/wcc.2021.022. 

- Tariq, S., Nawaz, H., Ul-Haq, Z. & Mehmood, U. (2021) Investigating the relationship of aerosols with enhanced vegetation index and meteorological parameters over Pakistan, Atmospheric Pollution Research, 12 (6), 101080. https://doi.org/10.1016/j.apr.2021. 101080. 

- Tian, F., Liu, L., Yang, J. & Wu, J.-J. (2021) Vegetation greening in more than 94% of the Yellow River basin (YRB) region in China during the 21st century caused jointly by warming and anthropogenic activities, Ecological Indicators., 125 (2), 107479. https://doi.org/10.1016/j. ecolind.2021.107479. 

- Tian, J. W., Yang, Y. & Zhang, X. Y. (2025) Study on ecological water requirement of soil and water conservation and its driving factors in the source region of the Yellow River, Journal of Yunnan University: Natural Sciences Edition, 47, 295–308. https://doi.org/10.7540/j.ynu. 20240145. 

- Tucker, C. J. (1979) Photosynthesis and stomatal conductance related to reflectance on the canopy scale, Remote Sensing of Environment, 21, 121–127. https://doi.org/10.1016/0034-4257(79)90013-1. 

- Turner, D. P., Ritts, W. D., Cohen, W. B., Gower, S. T., Running, S. W., Zhao, M. & Ahl, D. E. (2006) Evaluation of MODIS NPP and GPP products across multiple biomes, Remote Sensing of Environment, 102 (3–4), 282–292. https://doi.org/10.1016/j.rse.2006.02.017. 

- Vicente-Serrano, S. M., Miralles, D. G., Domínguez-Castro, F. & Peña-Gallardo, M. (2018) Global assessment of the standardized evapotranspiration deficit index (SEDI) for drought analysis and monitoring, Journal of Climate, 31 (14), 5371–5393. https://doi.org/10. 1175/JCLI-D-17-0775.s1. 

- Wambua, R. M. (2019) Hydrological drought forecasting using modified surface water supply index (SWSI) and streamflow drought index (SDI) in conjunction with artificial neural networks (ANNs), International Journal of Service Science, Management, Engineering, and Technology (IJSSMET), 10 (4), 39–57. https://doi.org/10.4018/IJSSMET.2019100103. 

Hydrology Research Vol 56 No 11, 1203 

- Wang, L. P. (2022) Optimization of Forest and Grass Allocation in the Upper and Middle Reaches of the Yellow River Based on Ecological 

Water Consumption Balance. Master’s thesis, Xi’an University of Technology. https://doi.org/10.27398/d.cnki.gxalu.2022.001682. Wang, Z., Chuang, L., Wenbo, C. & Xin, L. I. N. (2006) Preliminary comparison of MODIS-NDVI and MODIS-EVI in Eastern Asia, Geomatics and Information Science of Wuhan University, 31 (5), 407–410. 

- Wang, X., Wan, L. & R, Q. I. (2014) Interactions between groundwater and vegetation coverage in Odos Plateau, QuaternarySciences, 34 (5), 1013–1022. (in Chinese) doi: 10.3969/j.issn.1001-7410.2014.05.10. 

- Wang, Q., Zeng, J., Qi, J., Zhang, X., Zeng, Y., Shui, W. & Cong, J. (2021) A multi-scale daily SPEI dataset for drought characterization at observation stations over mainland China from 1961 to 2018, Earth System Science Data, 13 (2), 331–341. https://doi.org/10.5194/essd13-331-2021. 

- Wang, H., Zayit, A., He, X., Han, D., Yang, G. & Lv, G. (2023a) Ecological water requirement assessment for drought adaptation in arid basins, Water Resources Research, 59 (5), e2022WR033189. https://doi.org/10.1029/2022WR033189. 

- Wang, Y., Zhou, H., Huang, J., Yu, J. & Yuan, Y. (2023b) A framework for identifying propagation from meteorological to ecological drought events, Journal of Hydrology, 625, 130142. https://doi.org/10.1016/j.jhydrol.2023.130142. 

- Wang, Y., Wang, J. & Zhang, Q. (2024) Analysis of ecological drought risk characteristics and leading factors in the Yellow River basin, Theoretical and Applied Climatology, 155, 1739–1757. https://doi.org/10.1007/s00704-023-04720-w. 

- Wu, H., Shi, P., Qu, S., Zhang, H. & Ye, T. (2022) Establishment of watershed ecological water requirements framework: a case study of the lower Yellow River, China, Science of the Total Environment, 820, 153205. https://doi.org/10.1016/j.scitotenv.2022.153205. 

- Xu, M., Zhang, T., Zhang, Y., Chen, N., Zhu, J., He, Y. & Yu, G. (2021) Drought limits alpine meadow productivity in northern Tibet, Agricultural and Forest Meteorology, 303, 108371. https://doi.org/10.1016/j.agrformet.2021.108371. 

- Yang, D., Yang, Y. & Xia, J. (2021) Hydrological cycle and water resources in a changing world: a review, Geography and Sustainability, 2 (2), 115–122. https://doi.org/10.1016/j.geosus.2021.05.003. 

- Yang, X., Han, L. & Lv, C. (2024) Analysis of the influence of environmental conditions on the vegetation drought index in the Yellow River basin, Arid Zone Research, 41, 2083–2093. 

- Yellow River Conservancy Commission of the Ministry of Water Resources (2024) Yellow River Basin Soil and Water Conservation Bulletin (2024) [Annual Report]. Zhengzhou, China: Yellow River Conservancy Commission. Available at: http://www.yrcc.gov.cn/gzfw/stbcgb/ hhlystbcgb/202505/P020250604343284649208.pdf. 

- Yin, J., Yuan, Z. & Li, T. (2021) The spatial-Temporal variation characteristics of natural vegetation drought in the Yangtze River source region, China, International Journal of Environmental Research and Public Health, 18, 1613. https:// doi.org/10.3390/ ijerph18041613. 

- Yu, X., Wu, Z. & Guo, X. (2013) ’Investigating the potential of GIMMS and MODIS NDVI data sets for estimating gross primary productivity in Harvard Forest’, MultiTemp 2013: 7th International Workshop on the Analysis of Multi-Temporal Remote Sensing Images. 25–27 June 2013, Bologna, Italy. New York, NY: IEEE, pp. 1–4. doi: 10.1109/Multi-Temp.2013.6866013. 

- Yuan, W., Zheng, Y., Piao, S., Ciais, P., Lombardozzi, D., Wang, Y. & Yang, S. (2019) Increased atmospheric vapor pressure deficit reduces global vegetation growth, Science Advances, 5 (8), eaax1396. https://doi.org/10.1126/sciadv.aax1396. 

- Yuan, M., Wang, L., Lin, A., Liu, Z., Li, Q. & Qu, S. (2020) Vegetation green up under the influence of daily minimum temperature and urbanization in the Yellow River Basin, China, Ecological Indicators., 108, 105760. https://doi.org/10.1016/j.ecolind.2019.105760. 

- Zhang, J. (2018) Assessment of Ecological Water Requirements for Multi-Scale Vegetation-Soil Complex Systems in the Guanzhong-Tianshui Area Based on RS-GIS. Master’s thesis, Chang’an University. 

- Zhang, Y., Yang, S., Ouyang, W., Zeng, H. & Cai, M. (2010) Applying multi-source remote sensing data on estimating ecological water requirement of grassland in ungauged region, Procedia Environmental Sciences, 2, 953–963. https://doi.org/10.1016/j.proenv.2010.10. 107. 

Zhang, X., Chen, S., Sun, H., Shao, L. & Wang, Y. (2011) Changes in evapotranspiration over irrigated winter wheat and maize in north China plain over three decades, Agricultural Water Management, 98 (6), 1097–1104. https://doi.org/10.1016/j.agwat.2011.02.003. Zhang, A. N. Z., Pan, Z. H. & An, P. L. (2014a) The trend of ecological water shortage of farmland ecosystem in dryland under the 

- background of climate change: a case of Wuchuan County, Journal of Arid Land Resources and Environment, 28 (10), 68–75. 

Zhang, Y. L., Qi, G. P. & Zeng, X. C. (2014b) Analysis of ecological water requirement of Yintan Wetland in Lanzhou section of Yellow River 

- based on water balance method, Journal of Gansu Agricultural University, 1, 129–133 þ 139. https://doi.org/10.3969/j.issn.1003-4315. 2014.01.023. 

Zhang, B., Zhao, X. J. & Wu, P. (2015) Development and evaluation of a physically based multiscalar drought index: the standardized moisture anomaly index, Journal of Geophysical Research: Atmospheres, 120 (22), 11–575. https://doi.org/10.1002/2015JD023772. 

Zhang, Q., Kong, D., Singh, V. P. & Shi, P. (2017) Response of vegetation to different time-scales drought across China: spatiotemporal 

- patterns, causes and implications, Global and Planetary Change, 152, 1–11. https://doi.org/10.1016/j.gloplacha.2017.02.008. 

Zhang, B., AghaKouchak, A., Yang, Y., Wei, J. & Wang, G. (2019a) A water-energy balance approach for multi-category drought assessment 

   - across globally diverse hydrological basins, Agricultural and Forest Meteorology, 264, 247–265. https://doi.org/10.1016/j.agrformet. 2018.10.010Get rights and content. 

- Zhang, Y., Wang, X., Guo, J., Zeng, F. & Zeng, F. (2019b) Modeling of heterogeneous reservoirs with damaged hydraulic fractures, Journal of Hydrology, 574, 960–970. https://doi.org/10.1016/j.jhydrol.2019.04.089. 

Hydrology Research Vol 56 No 11, 1204 

Zhang, K., Lv, Y. H., Fu, B. J., Yin, L. C. & Yu, D. D. (2020) The effects of vegetation coverage changes on ecosystem service and their threshold in the Loess Plateau, Acta Geographica Sinica, 75 (5), 949–960. https://doi.org/10.1016/0273-1177(95)00079-T. 

Zhang, Y., Jin, G., Zhou, B., Zhang, Z., Chen, H. & Tang, H. (2023) Solute transport characteristics in the streambed due to rigid non- 

submerged plants: Experiment and simulations, Journal of Hydrology, 619, 129315. https://doi.org/10.1016/j.jhydrol.2023.129315. 

- Zhang, Z., Liu, J., Feng, K., Wang, F., Guo, H., Zhang, W. & Wang, S. (2024) Temporal and spatial characteristics of ecological drought in the Inland River Basin and its driving factors, Scientific Reports, 14, 28900. https://doi.org/10.1038/s41598-024-76988-5. 

- Zhao, W., Chang, X., He, Z. & Zhang, Z. (2007) Study on vegetation ecological water requirement in Ejina Oasis, Science in China Series D: Earth Sciences, 50, 121–129. https://doi.org/10.1007/s11430-007-2035-z. 

- Zhao, Z., Lu, C., Tonooka, H., Wu, L., Lin, H. & Jiang, X. (2025) Dynamic monitoring of vegetation phenology on the Qinghai-Tibetan plateau from 2001 to 2020 via the MSAVI and EVI, Scientific Reports, 15, 25698. https://doi.org/10.1038/s41598-025-11821-1. 

- Zhu, Y., Jiang, S., Ren, L., Guo, J., Zhong, F., Du, S., Cui, H. & He, M. (2024) Three-dimensional ecological drought identification and evaluation method considering eco-physiological status of terrestrial ecosystems, Science of The Total Environment, 951, 175423. https://doi.org/10.1016/j.scitotenv.2024.175423. 

- Zhu, X., Huang, S., Singh, V. P., Huang, Q., Zhang, H., Leng, G., Gao, L., Li, P., Guo, W. & Peng, J. (2025) Terrestrial ecosystem resilience to drought stress and driving mechanisms thereof in the Yellow River Basin, China, Journal of Hydrology, 649, 132480. https://doi.org/10. 1016/j.jhydrol.2024.132480. 

First received 26 March 2025; accepted in revised form 29 September 2025. Available online 17 October 2025 

