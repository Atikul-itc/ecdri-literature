Received: 20 May 2024 

Revised: 31 August 2025 Accepted: 14 November 2025 



DOI: 10.1002/ecs2.70600 

### A R T I C L E 

C l i m a t e E c o l o g y 

Ecological drought patterns and drivers in Inner Mongolia using a modified temperature vegetation drought index 

Jiapei Zhao<sup>1</sup> | Enliang Guo<sup>1</sup> | Yongfang Wang<sup>1,2</sup> | Yao Kang<sup>1</sup> | Jisiguleng Wu<sup>1</sup> | Yaodong Zhang<sup>1</sup> | Mengmeng Zhang<sup>1</sup> 

1College of Geographical Science, Inner Mongolia Normal University, Hohhot, China 

2Provincial Key Laboratory of Mongolian Plateau’s Climate System, Inner Mongolia Normal University, Hohhot, China 

#### Correspondence 

Enliang Guo 

Email: guoel1988@imnu.edu.cn 

#### Funding information 

Key Research and Development and Achievement Transformation Plan Projects of Inner Mongolia Autonomous Region, Grant/Award Numbers: 2025YFSH0056, 2025YFDZ0133, 2025KJHZ0047; First-Class Discipline Research Special Project, Grant/Award Number: YLXKZX-NSD-027; Inner Mongolia Normal University Graduate Student Research and Innovation Fund Program, Grant/Award Number: CXJJB23015; Natural Science Foundation of Inner Mongolia Autonomous Region of China, Grant/Award Number: 2024MS04002; National Natural Science Foundation of China, Grant/Award Numbers: 42261019, 42361014 

Handling Editor: Robert 

A. Washington-Allen 

## Abstract 

Inner Mongolia, situated in an arid and semiarid region, is characterized by a fragile ecological environment heavily impacted by frequent and intense droughts. The accurate assessment of ecological drought and identification of its drivers are crucial for drought disaster management in this area. In this study, we propose a novel ecological drought index, the kernel temperature vegetation drought index (kTVDI), which refines the traditional temperature vegetation drought index (TVDI) by incorporating the kernel normalized difference vegetation index (kNDVI) derived from MODIS data spanning from 2000 to 2022. We analyzed the spatial and temporal dynamics as well as future trends of ecological drought during the growing season in Inner Mongolia using Theil–Sen trend analysis, the Mann–Kendall test, and the Hurst index. This research also explored the correlations between the kTVDI and meteorological variables, such as potential evapotranspiration (PET), temperature (TM), and precipitation (PRE), on an image-by-image basis through partial correlation analysis. Additionally, it examines the impact of human activities on ecological drought through residual analysis. Structural equation modeling (SEM) was applied to elucidate the pathways through which natural environmental elements and human activities influence ecological drought. Our findings indicate a general trend toward the amelioration of ecological drought during the growing season in Inner Mongolia from 2000 to 2022, with the highest incidence of breakpoints occurring in July. Spatially, the ecological drought conditions transitioned from mild wetness in the northeast to severe drought in the southwest. Temporal trend analysis indicated increased dryness in May, June, and August, whereas wetness trends were prominent in July, September, and October. Notably, the future spatial patterns of ecological drought may show reverse trends. Precipitation was negatively correlated with ecological drought across 89% of the region, whereas PET and TM were positively correlated in 42.2% and 51.5% of the area, respectively. Furthermore, human activities exacerbated ecological drought in western Inner Mongolia 

> This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited. 

> © 2026 The Author(s). Ecosphere published by Wiley Periodicals LLC on behalf of The Ecological Society of America. 

https://onlinelibrary.wiley.com/r/ecs2 1 of 23 

Ecosphere. 2026;17:e70600. https://doi.org/10.1002/ecs2.70600 

2 of 23 

ZHAO ET AL. 

and mitigated it in the eastern regions. The SEM results emphasize that climatic conditions and human activities indirectly influence ecological drought through their impacts on the leaf area and productivity of vegetation. K E Y W O R D S ecological drought, kTVDI, MODIS, structural equation modeling 

# INTRODUCTION 

Drought is commonly defined as a natural phenomenon in which precipitation falls significantly below normal levels over a specific period, resulting in dry atmospheric conditions and insufficient soil moisture (SM). Droughts are one of the most severe natural disasters globally and are characterized by their slow onset, prolonged duration, and widespread impact (Dai, 2013). The intensification of global climate change has increased the frequency and severity of droughts (Fuentes et al., 2022; Spinoni et al., 2014), adversely affecting agricultural production, economic growth, water resource management, and ecosystem stability (Wang, Qi, et al., 2020; Wang, Shao, et al., 2020; Zhang et al., 2019). Droughts are traditionally categorized into four types: meteorological, hydrological, agricultural, and socioeconomic (Mishra & Singh, 2010). Drought categorization is primarily based on affected receptors, such as water resources, agriculture, and socioeconomic systems, enabling a more precise characterization of drought impacts across sectors. However, this receptor-based perspective often overlooks the essential role that ecosystems play in the onset and progression of drought. Furthermore, it often disregards the feedback mechanisms and adaptive capacities that ecosystems exhibit in response to drought. Therefore, it is crucial to investigate the complex interactions between drought and ecosystems, including the potential positive and negative feedbacks exerted by ecosystems throughout the drought cycle. To address this, Crausbay et al. (2017) introduced the concept of ecological drought. Ecological drought is defined as an episodic deficit in water availability that drives ecosystems beyond the thresholds of vulnerability, impacts ecosystem services, and triggers feedback in natural and/or human systems. This reduction leads to diminished water flow into wetlands and aquifers, which alters hydro-ecological processes, affects both aquatic and terrestrial ecosystems in various ways, and ultimately triggers ecological droughts (Wang, Lai, et al., 2023; Wang, Moreno-Martínez, et al., 2023; Wang, Zhang, et al., 2023; Wang, Zhou, et al., 2023; Zhang, Chen, et al., 2022; Zhang, Hao, et al., 2022). Ecological drought encompasses factors such as climate change and human activity and is closely related to vegetation 

conditions and ecosystem health. Therefore, monitoring and studying the spatial and temporal evolution of ecological drought aids in understanding current drought conditions as well as reveals the impacts of drought on vegetation and ecosystems. Such research is essential for mitigating drought disaster risks, effectively managing soil and water resources, and protecting and utilizing ecosystems. 

Ecological drought monitoring remains at the exploratory stage and involves three main indices (Jiang et al., 2021). The first type is the single drought index, including the precipitation-based Standardized Precipitation Index (SPI) (McKee et al., 1993), the Standardized Precipitation Evapotranspiration Index (SPEI) (Vicente-Serrano et al., 2012), and the Palmer Drought Severity Index (PDSI) (Palmer, 1965). These indices typically perform well in monitoring anomalies in meteorological and hydrological variables. Although these drought indices are not explicitly designed to predict ecological drought conditions or plant water stress, they are frequently used for this purpose (Fischer et al., 2007; Pasho et al., 2011; Tian et al., 2018). The second type comprises vegetation indices (VIs) that characterize vegetation conditions, including the normalized difference vegetation index (NDVI) (Nanzad et al., 2019), Vegetation Condition Index (VCI) (Measho et al., 2019), and Enhanced Vegetation Index (EVI) (Roodposhti et al., 2017). By monitoring the growth of vegetation, their response to drought was assessed to characterize the drought exposure of the ecosystems. However, the practical applications of VIs in real-time drought monitoring and water resource management remain limited. The third type of drought index is the composite drought index, which characterizes the combined effects of drought by integrating two or more components. For instance, the temperature vegetation drought index (TVDI) combines land surface temperature (LST) and VIs to simulate soil surface moisture changes and holds significant potential for application in surface drought monitoring and has been widely applied across various regions (Chen et al., 2011; Liang et al., 2014; Wang et al., 2004). However, TVDI has certain limitations. For instance, the NDVI used in TVDI construction is limited in handling atmospheric noise, soil 

3 of 23 

ECOSPHERE 

background, and saturation (Alencar et al., 2020). To overcome these limitations, Camps-Valls et al. (2021) proposed a new vegetation index: the kernel NDVI (kNDVI). Compared with traditional VIs, kNDVI incorporates core machine learning concepts and applies kernel methods in the extraction and computation of NDVI (Rojo-Alvarez<sup>´</sup> et al., 2018). kNDVI has demonstrated superiority compared to NDVI and the remotely sensed near-infrared reflectance of the vegetation index (NIRv) across various application scenarios, biomes, and climatic zones. It exhibits enhanced resistance to saturation, bias, and complex phenological cycles (Wang, Lai, et al., 2023; Wang, Moreno-Martínez, et al., 2023; Wang, Zhang, et al., 2023; Wang, Zhou, et al., 2023). Additionally, kNDVI has a solid theoretical foundation, is computationally efficient, and holds high value for studying natural and agricultural systems. Therefore, the development of a new index, the kernel temperature vegetation drought index (kTVDI), by combining kNDVI and LST, can provide a novel perspective and an innovative tool for monitoring ecological drought. 

Drought is a complex natural phenomenon, and its formation and evolution are driven by a combination of factors. An in-depth analysis of these driving factors is essential to understand the causes and progression of droughts. Current research on drought drivers primarily employs statistical methods (Ji et al., 2022), including multiple correlation analysis, linear regression analysis, principal components analysis, and residual analysis (Apurv et al., 2019; Jiang et al., 2022; Pasho et al., 2012). Partial correlation analysis can reduce the influence of other meteorological factors by controlling for one or more variables, thereby accurately estimating the relationships between individual meteorological factors and ecological droughts. Residual analysis is often employed to investigate the effects of human activity on drought. This method reveals the differences between predicted and actual observations, thus highlighting the additional effects of human activities. Although these methods are computationally efficient and complex, they cannot characterize the nonlinear relationships between variables and are not directly applicable to causal inferences. Specifically, traditional linear analyses often struggle to distinguish the strengths and interactions between factors when natural and anthropogenic influences on drought are combined (Zhu et al., 2020). 

Structural equation modeling (SEM) has been widely applied to explore the driving mechanisms of meteorological drought as a tool for effectively assessing complex interactions among drought drivers. The model not only quantifies the influence of individual independent variables while controlling for the effects of others but also 

assesses the combined effect of multiple factors on a target variable and accounts for interactions among independent variables (Fan et al., 2016). However, few studies have employed this approach to reveal the nonlinear thresholds and relative importance of the multiple factors influencing ecological drought. The formation mechanism of ecological drought differs from that of other drought types, as it originates from meteorological and hydrological droughts (Wang, Lai, et al., 2023; Wang, Moreno-Martínez, et al., 2023; Wang, Zhang, et al., 2023; Wang, Zhou, et al., 2023), and is further shaped by the combined effects of climate change and human activities during the propagation process. Therefore, employing SEM to investigate ecological drought drivers captures nonlinear relationships within the data and elucidates the complex interrelations among variables, thereby enhancing the reliability of the conclusions. Additionally, when constructing the SEM, it is essential to consider that changes in ecological drought are influenced by climate change and human activities, as well as by vegetation status. Therefore, indicators representing vegetation status, such as leaf area index (LAI) and gross primary production (GPP), should be incorporated. Ultimately, examining drought drivers through a combination of linear and nonlinear methods overcomes the limitations of traditional linear analysis and provides a novel perspective for comprehensively assessing the interaction of multiple drivers of ecological drought. 

As a vital ecological barrier in northern China and a frontier region characterized by typical arid and semiarid conditions, Inner Mongolia experiences some of the most frequent droughts in northern China, making droughts the primary extreme climatic events impacting regional ecosystems (An et al., 2020). Studies have indicated that drought significantly affects the vegetation and ecosystem of a region. For example, Zhang, Wang, et al. (2023) and Zhang, Zhang, et al. (2023) demonstrated that increased drought led to a decline in vegetation growth in Inner Mongolia. Liu et al. (2023) found that drought exacerbated vegetation decline. Guo et al. (2023) reported that semiarid grassland ecosystems in Inner Mongolia are particularly vulnerable to drought events, showing a reduction in drought resistance in recent years. Inner Mongolia supports diverse vegetation types, each of which responds differently to drought, leading to varying levels of drought exposure across ecosystems (Zhang et al., 2017). Furthermore, increased human activities in Inner Mongolia, especially long-term mineral development and highly water-consuming practices, such as agricultural and animal husbandry activities, have placed significant pressure on local water resources. In recent years, Inner Mongolia has implemented a series of ecological projects to restore vegetation and enhance the 

4 of 23 

ZHAO ET AL. 

water cycle, thereby positively affecting the regional ecosystems (Feng et al., 2022; Fu et al., 2024). Nevertheless, climate warming and increased human activity continue to pose serious threats to regional ecosystems. However, the dynamics and mechanisms driving ecological drought in this region remain unclear. Therefore, Inner Mongolia was selected for ecological drought research to enhance our understanding of how ecological droughts in the region respond to climate change and human activity. 

In conclusion, this study aimed to achieve three primary objectives: (1) develop a new ecological drought monitoring index, the kTVDI; (2) analyze the spatial and temporal evolution of ecological drought in Inner Mongolia using the kTVDI; and (3) assess the impacts of meteorological factors and human activities on ecological drought through partial correlation analysis, residual analysis, and SEM. The findings of this study will improve remote sensing monitoring of ecological drought as well as provide a scientific foundation for development of future ecological and environmental protection policies. 

# STUDY AREA 

Inner Mongolia is situated in northern China, covering an area of approximately 1.183 × 10<sup>6</sup> km<sup>2</sup> with a narrow and elongated topography extending diagonally from northeast to southwest. The region primarily consists of highland landforms with most areas at elevations exceeding 1 km above sea level (Figure 1a). Due to its unique geographic location and topography, most of Inner Mongolia falls within the temperate continental arid climate zone. The average annual precipitation generally ranges from 50 to 450 mm, exhibiting a spatial gradient that decreases from northeast to southwest. The climate gradually transitions from semi-humid in the east to arid to semiarid in the west (Hu et al., 2015). Vegetation types transition sequentially from northeast to southwest, ranging from coniferous forests to meadow grasslands, typical steppes, desert steppes, and the Gobi Desert (Figure 1b). 

# DATA AND METHODS 

# Data 

MODIS data for this study were acquired using the Google Earth Engine (GEE) platform. It included the 16-day composite MOD13A2 NDVI data and 8-day composite MOD11A2 LST data. The spatial resolution was 1 km, with a temporal range from May to October for the years 2000–2022. kNDVI, NDVI, and LST were aggregated to 

monthly scales to calculate kTVDI and TVDI using the averaging method. Additionally, LAI data were obtained from MOD15A2H and GPP data were obtained from MOD17A2H, both with a spatial resolution of 500 m and an 8-day temporal resolution. 

Monthly precipitation (PRE) and temperature (TM) data were obtained from 115 meteorological stations across Inner Mongolia between May and October from 2000 to 2022. Potential evapotranspiration (PET) data were calculated using the Penman–Monteith method (Penman, 1948) based on data from the Inner Mongolia Meteorological Station. 

Given the long time series and missing values in the meteorological station data, the monthly average SM data from ERA5-Land were selected as a substitute. Luo et al. (2021) validated the suitability of this product for Inner Mongolia. The ERA5 reanalysis data are a global atmospheric reanalysis product provided by the European Center for Medium-Range Weather Forecasts (ECMWF). It offers meteorological and soil data, including temperature, humidity, wind speed, and other parameters, from 1979 to the recent years. For this study, SM data at a 0–7 cm surface depth from May to October, 2000–2022, were selected at a spatial resolution of 0.25 degrees. 

Population data (POP) and gross regional domestic product (GDP) data were obtained from the Inner Mongolia Statistical Yearbook, with values recorded annually. 

# Methods 

# Construction of kTVDI 

The TVDI uses remote sensing to monitor SM and identify drought conditions. This index is calculated based on the relationship between vegetation index and surface temperature. The TVDI is calculated as (Sandholt et al., 2002) 







where Ts is the surface temperature, Tsmin is the lowest surface temperature under the same kNDVI conditions, Ts max is the highest surface temperature under the same kNDVI conditions, and a1, a2, a3, a4 are the coefficients of the fitting equation. The TVDI is in the range of [0,1], and the closer the value is to 0, the wetter the soil; the 

5 of 23 

ECOSPHERE 



F I G U R E 1 Schematic map of the study area and vegetation types. (a) Inner Mongolia elevation map; (b) vegetation-type map of Inner Mongolia. DEM, digital elevation model. 

6 of 23 

ZHAO ET AL. 

closer the value is to 1, the more arid and water-scarce the soil. 

ecological aridity based on the kTVDI was classified into five grades, as detailed in Table 1. 

The formula for kNDVI is 



where NDVI is the normalized vegetation index and tanh is the hyperbolic tangent function. 

Figure 2 demonstrates the principle of TVDI construction in the feature space based on NDVI and LST. The diagonal line in the feature space can be regarded as the contour of the TVDI, and the larger the slope of the diagonal line, the larger the TVDI value. The scatter represents the TVDI values in different pixel windows, the image elements at different locations in the study area in the remote sensing image. The TVDI value of each pixel represents drought conditions in the area, and all pixels constitute the TVDI raster data image of the study area. 

In this study, kTVDI was constructed using kNDVI instead of traditional NDVI. The kNDVI was first extracted in steps of 0.01 for the maximum and minimum surface temperatures corresponding to the kNDVI image elements, and the Ts-kNDVI feature space of surface temperatures in Inner Mongolia for the growing seasons of 2000–2022 was constructed by calculating the wet and dry side equations through linear fitting to calculate the kTVDI, which takes the same range of values as TVDI. Finally, the degree of 

# Sen slope method and nonparametric Mann–Kendall significance test 

The Sen slope method was used to calculate the amount of trend change in the time series data, which can identify the linear trend and thus infer the trend change in the data (Sen, 1968). The nonparametric Mann–Kendall significance test was used to analyze the significance of trend change in the time series data (Wang, Qi, et al., 2020; Wang, Shao, et al., 2020). In this study, the Sen slope is an indicator for analyzing the trend change in the kTVDI time series data and is calculated as follows: 

T A B L E 1 Ecological drought classification criteria based on kernel temperature vegetation drought index (kTVDI). 

|Drought grade|kTVDI|
|---|---|
|Severe wet|0 < kTVDI≤0.2|
|Mild wet|0.2 < kTVDI≤0.4|
|Normal|0.4 < kTVDI≤0.6|
|Mild dry|0.6 < kTVDI≤0.8|
|Severe dry|0.8 < kTVDI≤1.0|





F I G U R E 2 Schematic diagram of the construction of the temperature vegetation dryness index (TVDI). LST, land surface temperature; NDVI, normalized vegetation index. 

7 of 23 

ECOSPHERE 



persistently dry. This helps us understand possible future changes in the kTVDI. 



where median denotes the median function and kTVDIj and kTVDIi denote the data values of kTVDI in the time series of j and i, respectively. Positive SkTVDI denotes an increasing trend and negative SkTVDI value denotes a decreasing trend. The Mann–Kendall test statistic is calculated as follows: 







When n ≥ 10, S approximately follows a standard normal distribution and the test statistic Z is used for trend detection. 



where var denotes the variance. A significance level of α = 0.05 was used for the significance test, indicating that the change in trend was considered insignificant when jZj < 1.96. 

# Hurst index 

The Hurst index is an effective method for assessing the time series persistence and long-term correlations (Zhou, Bo, et al., 2020; Zhou, Ding, et al., 2020). Based on the magnitude of the resultant value according to the Hurst index, the future persistence of the kTVDI series can be determined as follows: if 0.5 < H < 1, the time series is persistent, and future changes will be consistent with past trends. If H = 0.5, the time series lacks persistence and represents a random sequence with no long-term correlation. If 0 < H < 0.5, the time series exhibits inverse persistence, indicating that future changes are contrary to past trends. The Sen slope results were coupled with the Hurst index results to categorize future ecological drought trends as persistently wetter, dry to wet, stable, wet to dry, and 

# Residual trend (RESTREND) method 

Residual analysis is a key statistical tool for assessing the fit of a model. Specifically, it does so by calculating the differences between observed values and model predictions, which are referred to as “residuals” (Wang, Lai, et al., 2023; Wang, Moreno-Martínez, et al., 2023; Wang, Zhang, et al., 2023; Wang, Zhou, et al., 2023). In this study, we used multiple linear regression and residual analyses to quantify the impacts of human activity on ecological drought. The method consisted of the following three steps. The first step involved selecting the ecological drought index in the growing season as the dependent variable and temperature and precipitation as the independent variables. A binary linear regression model was established, and the parameters of the model were calculated. In the second step, the predicted value of kTVDICC was calculated using temperature and precipitation information combined with the parameters of the regression model, which indicated the effect of climate change on kTVDI. In the third step, the difference between kTVDI and kTVDICC was calculated from the remote sensing image inversion, which is defined as kTVDIHA. kTVDIHA represents the impact of human activities on ecological drought and is calculated as follows: 





where a, b, and ε are the parameters of the binary linear regression model; Tmp and Pre refer to the average growing season temperature and total precipitation in degrees Celsius and millimeters, respectively; and kTVDIHA is the residual. 

To determine the relative impact of anthropogenic activities on ecological drought, we calculated the trend of kTVDIHA using the Sen slope method, where a positive trend value of kTVDIHA indicates that anthropogenic activities exacerbate ecological drought and vice versa. 

# Structural equation model 

SEM is a type of modeling used to establish, estimate, and test causal relationships among multiple variables. SEM combines the advantages of traditional methods such as multiple regression analysis, pathway analysis, factor analysis, and analysis of covariance. This model structure 

8 of 23 

ZHAO ET AL. 

includes observable explicit variables and integrates latent variables that are not directly observable and can clearly reveal the relationship between the overall impact of individual indicators and the interactions between indicators (Lefcheck, 2016; Tarka, 2018). Therefore, in this study, meteorological factors (PRE and TM), anthropogenic indicators (POP and GDP), and vegetation growth parameters (GPP and LAI) were selected to investigate their joint contributions to ecological drought using SEM. 

SEM typically consists of two main components: a measurement model and a structural model. The measurement model describes the relationship between observed and latent variables. This is usually evaluated using factor analysis. In a measurement model, it is assumed that observed variables are explained by one or more latent variables and an error term. 

The measurement model can be represented by the following equation: 



method to conduct a linear fitting between kTVDI, TVDI, RRE, and SM to assess the accuracy of kTVDI. 

Figures 3 and 4 present the validation results for the accuracy of kTVDI. kTVDI demonstrates a correlation coefficient (R<sup>2</sup> ) of −0.49 with PRE, compared to −0.42 for TVDI. Additionally, kTVDI shows a correlation coefficient (R<sup>2</sup> ) of −0.61 with SM, whereas for TVDI the value is −0.52. These results suggest that kTVDI outperforms traditional TVDI in capturing both precipitation and SM deficits. Since TVDI is already a widely used index for ecological drought monitoring, we conclude that kTVDI, as an ecological drought index, not only provides a more accurate reflection of ecological drought conditions but also surpasses TVDI in monitoring effectiveness. 

# Spatiotemporal characteristics of ecological drought 

# Patterns and breakpoints in temporal ecological drought trend 



where x and y represent the exogenous variables (observed variables). Ʌx and Ʌy are the factor loading matrices between the exogenous variables and the latent variables. ξ and η are the latent factors for the explanatory (independent) and response (dependent) variables, respectively, δ and ϵ are the measurement errors. 

Structural modeling describes the causal relationships between the underlying variables. This is usually evaluated using multivariate regression analysis. The formula for structural modeling is as follows: 



where η is the latent factor of the dependent variable, and B is the matrix of relationship coefficients between the latent factors of the dependent variable. Γ is the matrix of influence coefficients of the latent factor of the independent variable on the latent factor of the dependent variable. ξ is the latent factor of the independent variable. ζ is the error term of the structural model. 

# RESULTS 

# kTVDI accuracy validation 

Both the atmosphere and soil are essential components of ecosystems, and RRE and SM serve as key parameters for characterizing water scarcity in ecosystems. Therefore, this study applied the Pearson correlation 

Figure 5 illustrates the time series trend of the kTVDI for each vegetation type across different months. Results 



F I G U R E 3 Scatter density plots of the correlation of kernel temperature vegetation drought index (kTVDI) and TVDI with precipitation (PRE). (a) Scatter density plot of kTVDI and PRE; (b) scatter density plot of TVDI and PRE. 

9 of 23 

ECOSPHERE 



F I G U R E 4 Scatter density plots of the correlation of kernel temperature vegetation drought index (kTVDI) and TVDI with soil moisture (SM). (a) Scatter density plot of kTVDI and SM; (b) scatter density plot of TVDI and SM. 

show that the mean kTVDI value was highest in October, reaching 0.74 (mild drought level), and lowest in July, at 0.56 (normal level). Overall, the kTVDI showed a decreasing trend from June to October, indicating that the ecological drought conditions during the growing season in Inner Mongolia have been alleviated over the past 23 years. Both the coniferous forest and meadow steppe showed a decreasing trend in kTVDI from May to October. For the typical steppe, kTVDI also showed a decreasing trend from June to October. In contrast, the desert steppe exhibited an increase in kTVDI from May to September, whereas the kTVDI value for Gobi Desert region showed an increase in May, June, August, and September, and a decrease in July and October. These observations suggest that regions with higher vegetation cover tend to have lower monthly mean kTVDI values, indicating less ecological drought. Additionally, the drought frequency map (Figure 6) demonstrates the occurrence frequencies of mild and severe droughts across different months over the years. Drought frequency was relatively high in May, September, and October while the frequency was lower from June to August. Overall, these results indicate that the ecological 

drought conditions in Inner Mongolia are more severe in May, September, and October and relatively less severe from June to August. In terms of vegetation type, coniferous forests exhibit a lower frequency of drought occurrence throughout the growing season. The meadow steppe exhibited a mild drought frequency in May, September, and October, with no drought in the other months. The typical steppe exhibited a high frequency of mild drought in May, followed by a gradual decrease in June, reaching a minimum in August. However, drought conditions intensified in September, with severe drought observed in October. Desert steppe drought conditions improved from June but intensified in September, reaching their peak in October. The Gobi Desert region consistently experienced severe drought each month, but the conditions eased from June to August with a mild drought frequency. Additionally, we found that vegetation is prone to drought at the beginning and end of the growing season, and that frequent droughts negatively impact vegetation growth and development, potentially affectingthe final yield (Seleiman et al., 2021). 

The BFAST method proposed by Verbesselt et al. (2012) decomposes time series data into seasonal, trend, and residual components using iterative time series analysis (Watts & Laffan, 2014). Figure 7 presents the pixel-by-pixel breakpoint detection results of monthly scale kTVDI using the BFAST method. Breakpoints accounted for approximately 2.5% of the total area, whereas the blank area indicated that no breakpoints occurred. The purpose of this study was to explore long-term trends in mutation events rather than the specific timing of individual mutation events; therefore, month-by-month breakpoints across different years were combined. Analysis of the proportion of breakpoints in each month reveals a tendency for breakpoints to occur more frequently in specific months. The monthly proportions among all breakpoints were 13.1%, 10.8%, 25.9%, 15.2%, 16.8%, and 18.2%, respectively. Spatially, these breakpoints are primarily concentrated in the eastern part of the study area, particularly in the Hulunbeier and Xilingol Leagues, which are dominated by typical steppes. In contrast, the breakpoints were relatively sparse in the central and western regions. Typical steppes accounted for the highest proportion of all breakpoints, followed by meadow steppe and coniferous forest, whereas the Gobi Desert and desert steppes exhibited relatively low breakpoint proportions. 

# Spatial hierarchy of ecological drought 

Figure 8 illustrates the spatial distribution of the multiyear average ecological drought levels in Inner 

10 of 23 

ZHAO ET AL. 



F I G U R E 5 Temporal trends of kernel temperature vegetation drought index (kTVDI) for different vegetation types in Inner Mongolia in different months during 2000–2022. 

Mongolia. The ecological drought intensity for each month gradually increased from northeast to southwest. Specifically, the western part of the study area was categorized as a severe drought zone, the central part was primarily classified as a mild drought or normal zone, and the eastern part fell within a mildly wet zone category. 

Severe wetness was also observed in the eastern region, although it represented only a small proportion ranging from 0.2% to 0.7%. This spatial distribution of ecological drought levels is closely related to variations in vegetation cover. As shown in Figure 1b, vegetation cover gradually decreases from the northeast to the southwest, 

11 of 23 

ECOSPHERE 



F I G U R E 6 Frequency of light and severe drought classes in different months in Inner Mongolia, 2000–2022. 

reducing both the ground water retention capacity and the water resource supply of the ecosystem. As vegetation cover and water supply capacity decline, SM also gradually decreases (D’Odorico et al., 2007), which in turn exacerbates the ecological drought intensity. Consequently, the spatial distribution of ecological aridity in Inner Mongolia exhibits a distinct longitudinal zonal pattern, with mildly humid, normal or mildly arid, and severely arid zones progressing from the northeast to the southwest. 

# Ecological drought spatial trend change 

Figure 9 illustrates the spatial trends in ecological drought during the growing season in Inner Mongolia from 2000 to 2022. Overall, ecological drought conditions in the central and western parts of Inner 

Mongolia showed an increasing trend, whereas those in the eastern part indicated a mitigating trend. Specifically, in May, June, and August, the areas experiencing intensified drought were larger than wet areas, accounting for 49.3%, 38.2%, and 46.6% of the total study area, respectively. Conversely, in July, September, and October, the wetter areas were larger than the drier areas, accounting for 47.7%, 48.1%, and 78.3% of the total area, respectively. Coniferous forests primarily experienced wetting throughout each month of the growing season, whereas meadow steppe also showed a wetting trend, Typical steppe mainly showed drying in May, June, and August, and wetting in July, September, and October. The desert steppe primarily dried in May, June, August, and September, stabilized in July, and wetted in October, whereas in the Gobi Desert, the main change was drying in August and stabilizing in the other months. 

12 of 23 

ZHAO ET AL. 



F I G U R E 7 Spatial distribution of breakpoints of kernel temperature vegetation drought index (kTVDI) in Inner Mongolia from 2000 to 2022 using the BFAST method. 

# Ecological drought future trends 

By combining the results of the Sen slope analysis with Hurst index values, we predicted future trends in ecological drought in Inner Mongolia. Figure 10 presents the predicted future trends in ecological drought across Inner Mongolia. These results indicate that future ecological aridity changes in most areas will be the opposite of the past trends. Overall, the trend indicates central and western regions becoming wetter, while the eastern regions become drier. Specifically, areas that changed from dry to wet in May, June, and August accounted for 45.8%, 35.6%, and 38.7% of the total study area, respectively. In contrast, the change in area from wet to dry in July, 

September, and October was larger, accounting for 45.2%, 46%, and 74.3% of the total study area, respectively. With respect to vegetation type, the coniferous forest showed a shift from wet to dry throughout the growing season (May–October), whereas the meadow steppe changed from dry to wet in May and from wet to dry from June to October. The typical steppe transitioned from dry to wet in May and June and from wet to dry from July to October. The desert steppe shifted from dry to wet in May, June, August, and September, was stable in July, and transitioned from wet to dry in October. In the Gobi Desert, a dry-to-wet change was observed in August, while the aridity trends for other months remained undetermined. 

13 of 23 

ECOSPHERE 



F I G U R E 8 (a–f) Spatial distribution of May–October ecological drought levels during 2000–2022 in Inner Mongolia. 

# Driving factors of ecological drought 

# The impact of climate change on ecological drought 

Partial correlation analysis is a multivariate statistical tool for exploring the relationship between two variables and can be performed while controlling for one or more variables (Zhang, Chen, et al., 2022; Zhang, Hao, et al., 2022). Figure 11 presents the results of the partial correlation analysis between kTVDI and PET, TM, and PRE. Results indicate a negative correlation of 89% between PRE and kTVDI, with 64.2% being significant and 24.8% being nonsignificant. This suggests that increased precipitation can improve water availability on the surface and vegetation, thereby alleviating ecological drought. The positive correlation area accounted for 11%, with 10.4% being significant and 0.6% nonsignificant, and was mainly located in the agricultural and pastoral areas of Chifeng and Tongliao in eastern Inner Mongolia, indicating that precipitation may not be the main determinant of drought in these areas. This may be due to the combined effects of human activities (e.g., excessive water use and land use changes), environmental degradation, and climate change, which 

exacerbate water scarcity and intensify drought conditions in the region (Zhou, Bo, et al., 2020; Zhou, Ding, et al., 2020). PET showed a negative correlation with kTVDI in 42.2% of the area, with 40.7% being significantly negative and 1.5% nonsignificantly negative, primarily distributed in the forested Daxing’anling forest region in the eastern and western Alxa Gobi Desert. Despite the high PET, these areas maintained an ecological balance due to sufficient water supply, which met the vegetation transpiration needs and promoted photosynthesis. In the western Gobi Desert, although high PET usually indicates intense solar radiation and high temperatures, elevated PET instead alleviates ecological drought owing to the extreme dryness of the ground surface, where even minimal precipitation can be rapidly absorbed and utilized by vegetation (Li, Gong, et al., 2023; Li, Li, et al., 2023). Positive correlation areas accounted for 57.8%, primarily distributed in the central region, with 51.5% being significantly positive and 6.3% nonsignificantly positive. Here, high PET caused soil and vegetation to experience water stress due to an insufficient water supply, exacerbating drought conditions. The areas of negative correlation between TM and kTVDI accounted for 48.5%, with 46.8% showing a significant negative correlation and 1.7% showing a nonsignificant 

14 of 23 

ZHAO ET AL. 



F I G U R E 9 (a–f) Spatial distribution of growing season ecological drought trends in Inner Mongolia, May–October 2000–2022. 

negative correlation. Positive correlation areas accounted for 51.5%, with 48.9% being significant and 2.6% being nonsignificant. In positively correlated areas, increased temperatures lead to higher water evaporation from the surface and vegetation, and if this increased evaporation is not offset by the corresponding precipitation, drought conditions are intensified. In negatively correlated regions, warmer temperatures did not necessarily worsen drought conditions, possibly because of increased water availability or other ecosystem regulation mechanisms. For instance, plants may adapt to higher temperatures by expanding root depths or enhancing water use efficiency, thereby maintaining or increasing biomass under hot conditions to counteract drought effects (Condon et al., 2020). 

# The impact of human change on ecological drought 

Figure 12 presents the results of the residual analysis of the annual kTVDI from 2000 to 2022, indicating that areas where human activities exacerbated ecological drought accounted for 51.3% of the total region, mainly in central and western Inner Mongolia. In contrast, areas where 

human activity has mitigated ecological drought are primarily in eastern Inner Mongolia. From the perspective of vegetation type, human activities primarily aggravated ecological drought in the Gobi Desert and desert steppe regions, while mitigating ecological drought in the typical steppe, meadow steppe, and coniferous forest regions. In the western region, irrational tree-planting practices and groundwater extraction led to a decline in ecosystem moisture. Earlier studies have indicated that runoff and SM has decreased in temperate regions due to increased evapotranspiration demand (Brown et al., 2005). Additionally, in the desert steppe and typical grassland areas of the west, excessive agricultural and pastoral activities, particularly unsustainable irrigation and land management practices (e.g., overgrazing and unsuitable farming) alter soil structure and disrupt soil water-holding capacity, thereby exacerbating drought conditions (Gao et al., 2023). In contrast, the eastern region is dominated by forest vegetation, with relatively low human activity and minimal land pressure. Forest ecosystems have maintained their natural regulatory functions and exhibited strong drought resistance. Furthermore, forest protection measures, such as fire prevention, afforestation, and no-logging restoration, have further enhanced the regulatory role of forests in mitigating 

15 of 23 

ECOSPHERE 



F I G U R E 1 0 (a–f) Spatial distribution of future ecological drought trends in Inner Mongolia, May–October. 

ecological drought in this region (Wu, Liu, & Bao, 2023; Wu, Wang, et al., 2023; Yin et al., 2018). The differing impacts of human activities on ecological drought in eastern and western Inner Mongolia also contributed to the contrasting trends in ecological drought observed in these regions over the 23-year period. Along with the effects of climatic factors, human activities have a complex compound effect on ecological drought. For instance, in the west, human activities and higher temperatures exacerbates ecological drought conditions. In the east, both precipitation and human activities help alleviate ecological drought, and high vegetation cover contributes to mildly humid ecological drought. 

of −0.3826 and −0.2459, respectively, suggesting that improvement in vegetation growth can help alleviate ecological drought. Additionally, the positive correlation between LAI and GPP (correlation coefficient of 0.3339) reflects a synergistic effect between vegetation leaf area and productivity. Regarding meteorological factors, PRE and PET were positively correlated with both LAI and GPP, whereas TM was negatively correlated. For anthropogenic indicators, population size was negatively correlated with LAI and positively correlated with GPP, whereas GDP showed a strong positive correlation with both LAI and GPP, with coefficients of 0.9405 and 0.7149, respectively. These results suggest that meteorological factors and human activities primarily influence LAI and GPP and that these effects indirectly impact ecological drought. 

# Interacting effects of climate change and human activities on ecological drought 

# DISCUSSION 

Figure 13 presents the SEM results for the drivers of ecological drought in Inner Mongolia. These results indicate that meteorological and anthropogenic factors directly influence ecological drought as well as indirectly affect it through impact on vegetation conditions. Specifically, LAI and GPP showed negative correlations with kTVDI, with coefficients 

# Spatial and temporal variation in ecological drought 

In this study, kNDVI was calculated using MODIS NDVI data with a 1-km resolution, improving the NDVI in 

16 of 23 

ZHAO ET AL. 



F I G U R E 1 1 Spatial distribution of the results of bias correlation analysis between kernel temperature vegetation drought index (kTVDI) and climate factors in Inner Mongolia. (a) Bias correlation between potential evapotranspiration (PET) and kTVDI, (b) bias correlation between temperature (TM) and kTVDI, and (c) bias correlation between precipitation (PRE) and kTVDI. 

TVDI and constructing a new ecological drought index: kTVDI. Based on the concept of ecological drought, two indicators, PRE and SM, were selected for correlation analysis with the kTVDI. The results showed that the correlation coefficients of kTVDI with PRE and SM were close to or greater than −0.5. As the atmosphere and soil are essential components of an ecosystem, this further illustrates the applicability of the kTVDI in ecological drought monitoring. This study analyzed the temporal changes in ecological drought in Inner Mongolia from 2000 to 2022 based on the kTVDI, revealing a slight trend of ecological drought mitigation in the region since 2000. Wei et al. (2022) monitored drought in Inner Mongolia 

and concluded that drought is mitigating and vegetation cover is increasing, which aligns with the conclusion of this study on ecological drought mitigation. Spatially, ecological drought in eastern Inner Mongolia showed a mitigating trend, whereas the central and western regions exhibited an aggravating trend. The future ecological drought trend is likely to reverse, with the central and western parts of Inner Mongolia becoming wetter, and the eastern part becoming drier. Predictions by Li et al. (2020) based on the CMIP5 model indicate that under Representative Concentration Pathway 4.5, the future temperature in Inner Mongolia will gradually increase from west to east, with the increase in precipitation in the western part expected to exceed that in 

17 of 23 

ECOSPHERE 

the east. These findings support the phenomena observed in this study and suggest that the Hurst index can effectively capture future trends in ecological drought. 



F I G U R E 1 2 Spatial distribution of kernel temperature vegetation drought index (kTVDI) residual analysis results in Inner Mongolia. 

# Analysis of ecological drought drivers 

Over a 23-year period, ecological drought conditions in Inner Mongolia during the growing season were alleviated, mainly due to increased precipitation and improved vegetation growth (Kang et al., 2021). Ecological drought conditions were more severe in May, September, and October and less severe from June to August. This is attributed to the relatively high precipitation in Inner Mongolia from June to August, which accounts for approximately 60% of the total annual precipitation (Li, Gong, et al., 2023; Li, Li, et al., 2023). Increased precipitation during this period improved the SM and promoted vegetation growth, effectively mitigating ecological drought. However, decreased precipitation from September onwards, combined with the cumulative and lag effects of drought propagation (Zhang, Chen, et al., 2022; Zhang, Hao, et al., 2022), and led to worsening ecological drought conditions in September and October. From a vegetation-type perspective, higher vegetation cover correlates with less severe ecological drought conditions and lower drought frequency. This may be due to enhanced SM retention capacity in areas with higher vegetation cover. Densely vegetated areas typically 



F I G U R E 1 3 Results of structural equation modeling (SEM) of ecological drought drivers in Inner Mongolia. GDP, gross domestic product; GPP, gross primary production; kTVDI, kernel temperature vegetation drought index; LAI, leaf area index; PET, potential evapotranspiration; PRE, precipitation; TM, temperature. 

18 of 23 

ZHAO ET AL. 

have well-developed root systems and abundant ground cover, which enhance soil water retention and infiltration capacity. Additionally, the thicker ground cover in these areas effectively reduces surface moisture evaporation. Moreover, areas with high vegetation cover have healthier and more stable ecosystems, and these systems have stronger self-recovery and regulatory capabilities. The results from the BFAST method indicate different ecological drought trends before and after the mutation, with the highest probability of mutation occurring in July. According to statistical data, July had the highest precipitation in Inner Mongolia. This suggests that the vegetation and ecosystem health during this month largely depend on the regularity and sufficiency of precipitation. Poor precipitation stability (e.g., fluctuations in precipitation amount, shifts in timing, or uneven distribution) may negatively affect vegetation and ecosystems, leading to ecological drought. Among the vegetation types, typical grasslands had the highest percentage of mutations, highlighting their greater vulnerability to drought than other ecosystems in the study area. Grassland vegetation is typically shorter with shallower root systems, making it more susceptible to damage under drought conditions as SM decreases rapidly and vegetation struggles to access sufficient water (Liu et al., 2023). In addition, water availability in grassland areas is inherently unstable and often relies on seasonal precipitation (Zhang, Wang, et al., 2023; Zhang, Zhang, et al., 2023). When precipitation patterns shift, drought risk in grasslands increases. 

Spatially, the central and western parts of Inner Mongolia exhibited a trend of increasing drought conditions during the 23-year period, whereas the eastern part showed a trend toward more humid conditions. The western region, dominated by the Gobi Desert, experiences rapid surface moisture evaporation during droughts, further exacerbating aridity (Sternberg, 2014). In contrast, the eastern region is dominated by forests where ecosystems play a vital role in regulating the climate by reducing surface moisture evaporation, enhancing SM retention and water circulation, and effectively alleviating drought conditions (Wu, Liu, & Bao, 2023; Wu, Wang, et al., 2023). 

Figure 13 illustrates the results of the SEM analysis, which were chosen primarily because of the complexity of ecological drought mechanisms and involvement of multiple interacting factors. Ecological drought is directly affected by meteorological conditions (e.g., precipitation, temperature, and evapotranspiration), and is significantly influenced by human activities (e.g., population density and economic development). Furthermore, these factors indirectly influence ecological drought by altering vegetation characteristics (the LAI and GPP). The model clearly presents the relationship between kTVDI (ecological 

drought index) and several factors. Arrows indicate paths of influence, numbers represent influence intensity, negative values indicate negative correlations, and bold numbers indicate statistical significance. The SEM results showed negative correlations between the VIs, LAI, GPP, and kTVDI. This indicates that a decrease in leaf area and ecosystem productivity led to vegetation deterioration, which exacerbated ecological drought. The positive correlation between LAI and GPP suggests that a larger leaf area implies more chlorophyll and a greater photosynthetic area, promoting photosynthetic efficiency and output (Gitelson et al., 2014). The positive correlation between PRE, GPP, and LAI indicates that increased precipitation contributes to higher leaf area and productivity, improves vegetation conditions, and alleviates ecological drought. Conversely, the negative correlation between temperature, GPP, and LAI may indicate that increased temperature accelerates SM evaporation, reduces photosynthetic efficiency, and limits vegetation growth and leaf area expansion. The positive correlation between PET and LAI suggests that favorable evapotranspiration conditions promote vegetation transpiration and increase leaf area and productivity. A higher PET typically indicates favorable heat and moisture conditions for plant transpiration (Yang et al., 2023). The negative correlation of demographic factors with LAI and the positive correlation with GPP may indicate the adverse impacts of land-use changes (e.g., deforestation, urban sprawl, or agricultural expansion) on natural vegetation cover due to population growth, resulting in decreased LAI (Krein et al., 2023). The strong positive correlation of GDP with LAI and GPP suggests that as GDP the grows, the district may invest more in environmental protection and ecological restoration programs, such as afforestation and wetland restoration, which directly enhance vegetation cover and biomass. Studies have confirmed that the district has implemented a series of ecological engineering projects, including the Three North Shelter Forest Program (TNSFP), the Grain to Green Program (GGP), the Natural Forest Protection Program (NFPP) (Guo et al., 2021), and the Farming Return to Forest and Grassland Project. Key policies include reducing livestock, prohibiting grazing, and reconverting farmland to grassland (Zhang et al., 2020). The Fenced Grassland and Relocated Users Project, implemented by Inner Mongolia’s government in 2002, is another strategy to relocate herders from degraded grassland areas, thereby reducing pressure on damaged grasslands (Li et al., 2007; Yu & Farrell, 2013). An ecological protection subsidy incentive mechanism was also implemented to balance the herders’ income with ecological protection of grasslands, and these institutional arrangements collectively contributed to grassland restoration (Meng et al., 2018). 

19 of 23 

ECOSPHERE 

Additionally, agricultural advances driven by economic development, urban greening programs, stricter environmental regulations, and increased public environmental awareness have contributed to increases in LAI and GPP (Sun, 2022). 

# Research shortcomings and prospects 

In this study, we enhanced the traditional TVDI for ecological drought monitoring by introducing kNDVI and examined the drivers of ecological drought. Although our study has made progress, we recognize that human impact on ecological drought is highly complex and encompasses aspects such as land-use change and water resource management. Future studies should analyze these drivers and their interrelationships in greater depth to get a better understanding of their combined effects on ecological droughts. In constructing the SEM, we initially considered including livestock headcount as a factor influencing ecological drought. However, because livestock headcount showed only a weak correlation with the other variables in our analysis, we ultimately decided to exclude it from the final SEM. Additionally, we hope to combine the kTVDI with climate model predictions and socioeconomic data to explore the future impacts of climate change and human activities on ecological drought in greater depth. To further enhance the practicality and accuracy of the kTVDI, we hope to investigate its performance across different ecosystems and climatic conditions and refine its calculation method to improve its applicability and accuracy on regional and global scales. 

2. Ecological drought conditions in the vegetation growing season of Inner Mongolia from 2000 to 2022 showed alleviated. Ecological drought condition was more severe in May, September, and October and less severe in June, July, and August. 

3. The spatial distribution of ecological drought in Inner Mongolia followed the order of mildly humid areas, normal or mildly dry areas, and severely dry areas from northeast to southwest. From 2000 to 2022, the central and western parts of Inner Mongolia became drier while the eastern part became wetter. Arid areas expanded more than humid areas in May, June, and August, whereas humid areas expanded more than arid areas in July, September, and October. Future trends suggest that the Midwest will become wetter, whereas the east will become drier. 

4. The negative and positive correlations between PRE and ecological drought were 89% and 11%, respectively. For PET, these values were 57.8% and 42.2%, and for TM the values were 48.5% and 51.5%. Human activity has exacerbated ecological drought in 51.3% of Inner Mongolia, primarily in the central and western regions, whereas 48.7% of the area has experienced mitigation effects, mainly concentrated in the eastern region. 

5. SEM results indicated that the correlation coefficients between LAI and GPP with kTVDI were −0.3826 and −0.2459, respectively, while the correlation coefficient between LAI and GPP was 0.3339. Meteorological factors and human activities influenced ecological drought primarily by impacting vegetation. 

## ACKNOWLEDGMENTS 

# CONCLUSIONS 

In this study, a new ecological drought index, kTVDI, was constructed based on MODIS data. This index was used to analyze the spatial and temporal distribution characteristics of ecological drought during the vegetation growing season in Inner Mongolia from 2000 to 2022, examine future trends, and explore the drivers of ecological drought. The following conclusions were obtained: 

1. The R<sup>2</sup> values of kTVDI and TVDI with PRE were −0.49 and −0.42, respectively, with the R<sup>2</sup> values of TVDI and SM were −0.61 and −0.52, respectively. The kTVDI, improved through kNDVI, showed a superior ability to monitor ecological drought compared to TVDI in Inner Mongolia. 

This research was funded by the National Natural Science Foundation of China (42261019, 42361014), Natural Science Foundation of Inner Mongolia Autonomous Region of China (2024MS04002), FirstClass Discipline Research Special Project (YLXKZXNSD-027), the Key Research and Development and Achievement Transformation Plan Projects of Inner Mongolia Autonomous Region (2025YFSH0056, 2025YFDZ0133, 2025KJHZ0047), and Inner Mongolia Normal University Graduate Student Research and Innovation Fund Program (CXJJB23015). 

## CONFLICT OF INTEREST STATEMENT 

The authors declare no conflicts of interest. 

## DATA AVAILABILITY STATEMENT 

Data (Lin, 2026) are available from Figshare: https://doi. org/10.6084/m9.figshare.27288660. 

20 of 23 

ZHAO ET AL. 

## REFERENCES 

- Alencar, A., J. Z. Shimbo, F. Lenti, C. Balzani Marques, B. Zimbres, M. Rosa, and M. Barroso. 2020. “Mapping Three Decades of Changes in the Brazilian Savanna Native Vegetation Using Landsat Data Processed in the Google Earth Engine Platform.” Remote Sensing 12(6): 924. https://doi.org/10.3390/rs12060924. 

- An, Q., H. He, Q. Nie, Y. Cui, J. Gao, C. Wei, and J. You. 2020. “Spatial and Temporal Variations of Drought in Inner Mongolia, China.” Water 12(6): 1715. https://doi.org/10.3390/ w12061715. 

- Apurv, T., Y. P. Xu, Z. Wang, and X. Cai. 2019. “Multidecadal Changes in Meteorological Drought Severity and their Drivers in Mainland China.” Journal of Geophysical Research: Atmospheres 124(23): 12937–52. https://doi.org/10.1029/2019 JD031317. 

- Brown, A. E., L. Zhang, T. A. McMahon, A. W. Western, and R. A. Vertessy. 2005. “A Review of Paired Catchment Studies for Determining Changes in Water Yield Resulting from Alterations in Vegetation.” Journal of Hydrology 310(1–4): 28–61. https://doi.org/10.1016/j.jhydrol.2004.12.010. 

- Camps-Valls, G., M. Campos-Taberner, A.´ Moreno-Martínez, S. Walther, G. Duveiller, A. Cescatti, and S. W. Running. 2021. “A Unified Vegetation Index for Quantifying the Terrestrial Biosphere.” Science Advances 7(9): eabc7447. https://doi.org/ 10.1126/sciadv.abc7447. 

- Chen, J., C. Wang, H. Jiang, L. Mao, and Z. Yu. 2011. “Estimating Soil Moisture Using Temperature–Vegetation Dryness Index (TVDI) in the Huang-Huai-Hai (HHH) Plain.” International Journal of Remote Sensing 32(4): 1165–77. https://doi.org/10. 1080/01431160903527421. 

- Condon, L. E., A. L. Atchley, and R. M. Maxwell. 2020. “Evapotranspiration Depletes Groundwater under Warming over the Contiguous United States.” Nature Communications 11(1): 873. https://doi.org/10.1038/s41467-020-14688-0. 

- Crausbay, S. D., A. R. Ramirez, S. L. Carter, M. S. Cross, K. R. Hall, D. J. Bathke, and T. Sanford. 2017. “Defining Ecological Drought for the Twenty-First Century.” Bulletin of the American Meteorological Society 98(12): 2543–50. https://doi. org/10.1175/BAMS-D-16-0292.1. 

- Dai, A. 2013. “Increasing Drought under Global Warming in Observations and Models.” Nature Climate Change 3(1): 52–58. https://doi.org/10.1038/nclimate1633. 

- D’Odorico, P., K. Caylor, G. S. Okin, and T. M. Scanlon. 2007. “On Soil Moisture–Vegetation Feedbacks and their Possible Effects on the Dynamics of Dryland Ecosystems.” Journal of Geophysical Research: Biogeosciences 112(G4): G04010. https:// doi.org/10.1029/2006JG000379. 

- Fan, Y., J. Chen, G. Shirkey, R. John, S. R. Wu, H. Park, and C. Shao. 2016. “Applications of Structural Equation Modeling (SEM) in Ecological Studies: An Updated Review.” Ecological Processes 5: 1–12. https://doi.org/10.1186/s13717-016-0063-3. 

- Feng, S., X. Liu, W. Zhao, Y. Yao, A. Zhou, X. Liu, and P. Pereira. 2022. “Key Areas of Ecological Restoration in Inner Mongolia Based on Ecosystem Vulnerability and Ecosystem Service.” Remote Sensing 14(12): 2729. https://doi.org/10.3390/rs141 22729. 

- Fischer, E. M., S. I. Seneviratne, D. Lüthi, and C. Schär. 2007. “Contribution of Land-Atmosphere Coupling to Recent 

European Summer Heat Waves.” Geophysical Research Letters 34(6): L06707. https://doi.org/10.1029/2006GL029068. 

- Fu, F., S. Wang, X. Wu, F. Wei, P. Chen, and J. M. Grünzweig. 2024. “Locating Hydrologically Unsustainable Areas for Supporting Ecological Restoration in China’s Drylands.” Earth’s Future 12(3): e2023EF004216. https://doi.org/10.1029/ 2023EF004216. 

- Fuentes, I., J. Padarian, and R. W. Vervoort. 2022. “Spatial and Temporal Global Patterns of Drought Propagation.” Frontiers in Environmental Science 10: 788248. https://doi.org/10.3389/ fenvs.2022.788248. 

- Gao, W., H. Jiang, S. Zhang, C. Hai, and B. Liu. 2023. “Vegetation Characteristics and Soil Properties in Grazing Exclusion Areas of the Inner Mongolia Desert Steppe.” International Soil and Water Conservation Research 11(3): 549–560. https://doi.org/ 10.1016/j.iswcr.2022.11.005. 

- Gitelson, A. A., Y. Peng, T. J. Arkebauer, and J. Schepers. 2014. “Relationships between Gross Primary Production, Green LAI, and Canopy Chlorophyll Content in Maize: Implications for Remote Sensing of Primary Production.” Remote Sensing of Environment 144: 65–72. https://doi.org/10.1016/j.rse.2014. 01.004. 

- Guo, E., Y. Wang, C. Wang, Z. Sun, Y. Bao, N. Mandula, and H. Li. 2021. “NDVI Indicates Long-Term Dynamics of Vegetation and its Driving Forces from Climatic and Anthropogenic Factors in Mongolian Plateau.” Remote Sensing 13(4): 688. https://doi.org/10.3390/rs13040688. 

- Guo, J., X. Yang, W. Jiang, X. Xing, M. Zhang, A. Chen, and B. Xu. 2023. “Resistance of Grassland under Different Drought Types in the Inner Mongolia Autonomous Region of China.” Remote Sensing 15(20): 5045. https://doi.org/10.3390/rs15205045. 

- Hu, Q., F. Pan, X. Pan, D. Zhang, Q. Li, Z. Pan, and Y. Wei. 2015. “Spatial Analysis of Climate Change in Inner Mongolia during 1961–2012, China.” Applied Geography 60: 254–260. https:// doi.org/10.1016/j.apgeog.2014.10.009. 

- Ji, B., Y. Qin, T. Zhang, X. Zhou, G. Yi, M. Zhang, and M. Li. 2022. “Analyzing Driving Factors of Drought in Growing Season in the Inner Mongolia Based on Geodetector and GWR Models.” Remote Sensing 14(23): 6007. https://doi.org/10.3390/ rs14236007. 

- Jiang, T., X. Su, V. P. Singh, and G. Zhang. 2021. “A Novel Index for Ecological Drought Monitoring Based on Ecological Water Deficit.” Ecological Indicators 129: 107804. https://doi.org/10. 1016/j.ecolind.2021.107804. 

- Jiang, W., Z. Niu, L. Wang, R. Yao, X. Gui, F. Xiang, and Y. Ji. 2022. “Impacts of Drought and Climatic Factors on Vegetation Dynamics in the Yellow River Basin and Yangtze River Basin, China.” Remote Sensing 14(4): 930. https://doi.org/10.3390/ rs14040930. 

- Kang, Y., E. Guo, Y. Wang, Y. Bao, Y. Bao, and N. Mandula. 2021. “Monitoring Vegetation Change and its Potential Drivers in Inner Mongolia from 2000 to 2019.” Remote Sensing 13(17): 3357. https://doi.org/10.3390/rs13173357. 

- Krein, D. D. C., M. Rosseto, F. Cemin, L. A. Massuda, and A. Dettmer. 2023. “Recent Trends and Technologies for Reduced Environmental Impacts of Fertilizers: A Review.” International journal of Environmental Science and Technology 20(11): 12903–18. https://doi.org/10.1007/s13762-023-04929-2. 

21 of 23 

ECOSPHERE 

- Lefcheck, J. S. 2016. “piecewiseSEM: Piecewise Structural Equation Modelling in R for Ecology, Evolution, and Systematics.” Methods in Ecology and Evolution 7(5): 573–79. https://doi.org/10.1111/2041-210X.12512. 

- Li, C., L. Li, X. Wu, A. Tsunekawa, Y. Wei, Y. Liu, and K. Bai. 2023. “Increasing Precipitation Promoted Vegetation Growth in the Mongolian Plateau during 2001–2018.” Frontiers in Environmental Science 11: 1153601. https://doi.org/10.3389/ fenvs.2023.1153601. 

- Li, W. J., S. H. Ali, and Q. Zhang. 2007. “Property Rights and Grassland Degradation: A Study of the Xilingol Pasture, Inner Mongolia, China.” Journal of Environmental Management 85(2): 461–470. https://doi.org/10.1016/j.jenvman.2006.10.010. 

- Li, Y., H. Gong, W. Chen, L. Wang, R. Wu, Z. Dong, and K. Ma. 2023. “Summer Precipitation Variability in the Mongolian Plateau and its Possible Causes.” Global and Planetary Change 228: 104189. https://doi.org/10.1016/j.gloplacha.2023.104189. 

- Li, Y., S. Tong, Y. Bao, E. Guo, and Y. Bao. 2020. “Prediction of Droughts in the Mongolian Plateau Based on the CMIP5 Model.” Water 12(10): 2774. https://doi.org/10.3390/w121 02774. 

- Liang, L., S. H. Zhao, Z. H. Qin, K. X. He, C. C. Chen, Y. X. Luo, and X. D. Zhou. 2014. “Drought Change Trend Using MODIS TVDI and its Relationship with Climate Factors in China from 2001 to 2010.” Journal of Integrative Agriculture 13(7): 1501–8. https://doi.org/10.1016/S2095-3119(14)60813-3. 

- Lin, R. 2026. “kTVDI.” Figshare. Dataset. https://doi.org/10.6084/ m9.figshare.27288660.v1. 

- Liu, C., M. Siri, H. Li, C. Ren, J. Huang, C. Feng, and K. Liu. 2023. “Drought Is Threatening Plant Growth and Soil Nutrients of Grassland Ecosystems: A Meta-Analysis.” Ecology and Evolution 13(5): e10092. https://doi.org/10. 1002/ece3.10092. 

- Luo, M., F. Meng, C. Sa, Y. Duan, Y. Bao, T. Liu, and P. De Maeyer. 2021. “Response of Vegetation Phenology to Soil Moisture Dynamics in the Mongolian Plateau.” Catena 206: 105505. https://doi.org/10.1016/j.catena.2021.105505. 

- McKee, T. B., N. J. Doesken, and J. Kleist. 1993. “The Relationship of Drought Frequency and Duration to Time Scales.” In Proceedings of the 8th Conference on Applied Climatology, 179–183. 

- Measho, S., B. Chen, Y. Trisurat, P. Pellikka, L. Guo, S. Arunyawat, and T. Yemane. 2019. “Spatio-Temporal Analysis of Vegetation Dynamics as a Response to Climate Variability and Drought Patterns in the Semiarid Region, Eritrea.” Remote Sensing 11(6): 724. https://doi.org/10.3390/rs11060724. 

- Meng, Z., X. Dang, Y. Gao, X. Ren, Y. Ding, and M. Wang. 2018. “Interactive Effects of Wind Speed, Vegetation Coverage and Soil Moisture in Controlling Wind Erosion in a Temperate Desert Steppe, Inner Mongolia of China.” Journal of Arid Land 10: 534–547. https://doi.org/10.1007/ s40333-018-0059-1. 

- Mishra, A. K., and V. P. Singh. 2010. “A Review of Drought Concepts.” Journal of Hydrology 391(1–2): 202–216. https:// doi.org/10.1016/j.jhydrol.2010.07.012. 

- Nanzad, L., J. Zhang, B. Tuvdendorj, M. Nabil, S. Zhang, and Y. Bai. 2019. “NDVI Anomaly for Drought Monitoring and its Correlation with Climate Factors over Mongolia from 2000 to 

   - 2016.” Journal of Arid Environments 164: 69–77. https://doi. org/10.1016/j.jaridenv.2019.01.019. 

- Palmer, W. C. 1965. “Meteorological Drought.” U.S. Weather Bureau Research Paper 45: 1–58. 

- Pasho, E., J. J. Camarero, M. de Luis, and S. M. Vicente-Serrano. 2011. “Impacts of Drought at Different Time Scales on Forest Growth across a Wide Climatic Gradient in North-Eastern Spain.” Agricultural and Forest Meteorology 151(12): 1800–1811. https://doi.org/10.1016/j.agrformet.2011.07.018. 

- Pasho, E., J. J. Camarero, M. de Luis, and S. M. Vicente-Serrano. 2012. “Factors Driving Growth Responses to Drought in Mediterranean Forests.” European Journal of Forest Research 131: 1797–1807. https://doi.org/10.1007/ s10342-012-0633-6. 

- Penman, H. L. 1948. “Natural Evaporation from Open Water, Bare Soil and Grass.” Proceedings of the Royal Society of London. Series A: Mathematical and Physical Sciences 193(1032): 120–145. https://doi.org/10.1098/rspa.1948.0037. 

- Rojo-Alvarez,<sup>´</sup> J. L., M. Martínez-Ramon,� J. Munoz-Mari, and G. Camps-Valls. 2018. Digital Signal Processing with Kernel Methods. Hoboken, NJ: John Wiley & Sons. 

- Roodposhti, M. S., T. Safarrad, and H. Shahabi. 2017. “Drought Sensitivity Mapping Using Two One-Class Support Vector Machine Algorithms.” Atmospheric Research 193: 73–82. https://doi.org/10.1016/j.atmosres.2017.04.017. 

- Sandholt, I., K. Rasmussen, and J. Andersen. 2002. “A Simple Interpretation of the Surface Temperature/Vegetation Index Space for Assessment of Surface Moisture Status.” Remote Sensing of Environment 79(2–3): 213–224. https://doi.org/10. 1016/S0034-4257(01)00274-7. 

- Seleiman, M. F., N. Al-Suhaibani, N. Ali, M. Akmal, M. Alotaibi, Y. Refay, and M. L. Battaglia. 2021. “Drought Stress Impacts on Plants and Different Approaches to Alleviate its Adverse Effects.” Plants 10(2): 259. https://doi.org/10.3390/plants 10020259. 

- Sen, P. K. 1968. “Estimates of the Regression Coefficient Based on Kendall’s Tau.” Journal of the American Statistical Association 63(324): 1379–89. https://doi.org/10.1080/01621459.1968. 10480934. 

- Spinoni, J., G. Naumann, H. Carrao, P. Barbosa, and J. Vogt. 2014. “World Drought Frequency, Duration, and Severity for 1951–2010.” International Journal of Climatology 34(8): 2792–2804. https://doi.org/10.1002/joc.3875. 

- Sternberg, T. 2014. “Drought and Extreme Climate Stress on Human-Environment Systems in the Gobi Desert, Mongolia.” In Vulnerability of Land Systems in Asia, edited by A. K. Braimoh and H. Q. Huang, 9–26. Chichester: Wiley Online Library. https://doi.org/10.1002/ 9781118854945.ch2. 

- Sun, Y. 2022. “Environmental Regulation, Agricultural Green Technology Innovation, and Agricultural Green Total Factor Productivity.” Frontiers in Environmental Science 10: 955954. https://doi.org/10.3389/fenvs.2022.955954. 

- Tarka, P. 2018. “An Overview of Structural Equation Modeling: Its Beginnings, Historical Development, Usefulness and Controversies in the Social Sciences.” Quality & Quantity 52: 313–354. https://doi.org/10.1007/ s11135-017-0469-8. 

22 of 23 

ZHAO ET AL. 

- Tian, L., S. Yuan, and S. M. Quiring. 2018. “Evaluation of Six Indices for Monitoring Agricultural Drought in the South-Central United States.” Agricultural and Forest Meteorology 249: 107–119. https://doi.org/10.1016/j.agrformet. 2017.11.024. 

- Verbesselt, J., A. Zeileis, and M. Herold. 2012. “Near Real-Time Disturbance Detection Using Satellite Image Time Series.” Remote Sensing of Environment 123: 98–108. https://doi.org/10. 1016/j.rse.2012.02.022. 

- Vicente-Serrano, S. M., S. Beguería, J. Lorenzo-Lacruz, J. J. Camarero, J. I. L�opez-Moreno, C. Azorin-Molina, and A. Sanchez-Lorenzo. 2012. “Performance of Drought Indices for Ecological, Agricultural, and Hydrological Applications.” Earth Interactions 16(10): 1–27. https://doi.org/10.1175/ 2012EI000434.1. 

- Wang, C., S. Qi, Z. Niu, and J. Wang. 2004. “Evaluating Soil Moisture Status in China Using the Temperature–Vegetation Dryness Index (TVDI).” Canadian Journal of Remote Sensing 30(5): 671–79. https://doi.org/10.5589/m04-029. 

- Wang, F., H. Lai, Y. Li, K. Feng, Q. Tian, Z. Zhang, and H. Yang. 2023. “Terrestrial Ecological Drought Dynamics and its Response to Atmospheric Circulation Factors in the North China Plain.” Atmospheric Research 294: 106944. https://doi. org/10.1016/j.atmosres.2023.106944. 

- Wang, F., W. Shao, H. Yu, G. Kan, X. He, D. Zhang, and G. Wang. 2020. “Re-Evaluation of the Power of the Mann-Kendall Test for Detecting Monotonic Trends in Hydrometeorological Time Series.” Frontiers in Earth Science 8: 14. https://doi.org/10. 3389/feart.2020.00014. 

- Wang, Q., A.´ Moreno-Martínez, J. Muñoz-Marí, M. Campos-Taberner, and G. Camps-Valls. 2023. “Estimation of Vegetation Traits with Kernel NDVI.” ISPRS Journal of Photogrammetry and Remote Sensing 195: 408–417. https:// doi.org/10.1016/j.isprsjprs.2022.12.019. 

- Wang, Q., J. Qi, H. Wu, Y. Zeng, W. Shui, J. Zeng, and X. Zhang. 2020. “Freeze-Thaw Cycle Representation Alters Response of Watershed Hydrology to Future Climate Change.” Catena 195: 104767. https://doi.org/10.1016/j. catena.2020.104767. 

- Wang, X., X. Zhang, W. Li, X. Cheng, Z. Zhou, Y. Liu, and X. Ling. 2023. “Quantitative Analysis of Climate Variability and Human Activities on Vegetation Variations in the Qilian Mountain National Nature Reserve from 1986 to 2021.” Forests 14(10): 2042. https://doi.org/10.3390/ f14102042. 

- Wang, Y., H. Zhou, J. Huang, J. Yu, and Y. Yuan. 2023. “A Framework for Identifying Propagation from Meteorological to Ecological Drought Events.” Journal of Hydrology 625: 130142. https://doi.org/10.1016/j.jhydrol.2023.130142. 

- Watts, L. M., and S. W. Laffan. 2014. “Effectiveness of the BFAST Algorithm for Detecting Vegetation Response Patterns in a Semi-Arid Region.” Remote Sensing of Environment 154: 234–245. https://doi.org/10.1016/j.rse.2014.08.023. 

- Wei, Y., L. Zhu, Y. Chen, X. Cao, and H. Yu. 2022. “Spatiotemporal Variations in Drought and Vegetation Response in Inner Mongolia from 1982 to 2019.” Remote Sensing 14(15): 3803. https://doi.org/10.3390/rs14153803. 

- Wu, X., G. Liu, and Q. Bao. 2023. “Impact of Economic Growth on the Changes in Forest Resources in Inner Mongolia of China.” Frontiers in Environmental Science 11: 1241703. https://doi. org/10.3389/fenvs.2023.1241703. 

- Wu, Y., W. Wang, W. Li, S. Zhao, S. Wang, and T. Liu. 2023. “Assessment of the Spatiotemporal Characteristics of Vegetation Water Use Efficiency in Response to Drought in Inner Mongolia, China.” Environmental Science and Pollution Research 30(3): 6345–57. https://doi.org/10.1007/s113 56-022-22622-8. 

- Yang, Y., M. L. Roderick, H. Guo, D. G. Miralles, L. Zhang, S. Fatichi, and D. Yang. 2023. “Evapotranspiration on a Greening Earth.” Nature Reviews Earth and Environment 4(9): 626–641. https://doi.org/10.1038/s43017-023-00464-3. 

- Yin, H., D. Pflugmacher, A. Li, Z. Li, and P. Hostert. 2018. “Land Use and Land Cover Change in Inner Mongolia— Understanding the Effects of China’s Re-Vegetation Programs.” Remote Sensing of Environment 204: 918–930. https://doi.org/10.1016/j.rse.2017.08.030. 

- Yu, L., and K. N. Farrell. 2013. “Individualized Pastureland Use: Responses of Herders to Institutional Arrangements in Pastoral China.” Human Ecology 41: 759–771. https://doi.org/ 10.1007/s10745-013-9580-1. 

- Zhang, J., S. Chen, Z. Wu, and Y. H. Fu. 2022. “Review of Vegetation Phenology Trends in China in a Changing Climate.” Progress in Physical Geography: Earth and Environment 46(6): 829–845. https://doi.org/10.1177/03091333221114737. 

- Zhang, K., Q. Wang, L. Chao, J. Ye, Z. Li, Z. Yu, and Q. Ju. 2019. “Ground Observation-Based Analysis of Soil Moisture Spatiotemporal Variability across a Humid to Semi-Humid Transitional Zone in China.” Journal of Hydrology 574: 903–914. https://doi.org/10.1016/j.jhydrol.2019.04.087. 

- Zhang, Q., D. Kong, V. P. Singh, and P. Shi. 2017. “Response of Vegetation to Different Time-Scales Drought across China: Spatiotemporal Patterns, Causes and Implications.” Global and Planetary Change 152: 1–11. https://doi.org/10.1016/j. gloplacha.2017.02.008. 

- Zhang, W., Z. Wang, H. Lai, R. Men, F. Wang, K. Feng, and S. Huang. 2023. “Dynamic Characteristics of Meteorological Drought and its Impact on Vegetation in an Arid and Semi-Arid Region.” Water 15(22): 3882. https://doi.org/10. 3390/w15223882. 

- Zhang, X., Z. Hao, V. P. Singh, Y. Zhang, S. Feng, Y. Xu, and F. Hao. 2022. “Drought Propagation under Global Warming: Characteristics, Approaches, Processes, and Controlling Factors.” Science of the Total Environment 838: 156021. https:// doi.org/10.1016/j.scitotenv.2022.156021. 

- Zhang, Y., Q. Wang, Z. Wang, Y. Yang, and J. Li. 2020. “Impact of Human Activities and Climate Change on the Grassland Dynamics under Different Regime Policies in the Mongolian Plateau.” Science of the Total Environment 698: 134304. https://doi.org/10.1016/j.scitotenv.2019.134304. 

- Zhang, Z., Z. Zhang, Y. Hautier, H. Qing, J. Yang, T. Bao, and A. K. Knapp. 2023. “Effects of Intra-Annual Precipitation Patterns on Grassland Productivity Moderated by the Dominant Species Phenology.” Frontiers in Plant Science 14: 1142786. https://doi.org/10.3389/fpls.2023.1142786. 

23 of 23 

ECOSPHERE 

- Zhou, F., Y. Bo, P. Ciais, P. Dumas, Q. Tang, X. Wang, and Y. Wada. 2020. “Deceleration of China’s Human Water Use and its Key Drivers.” Proceedings of the National Academy of Sciences of the United States of America 117(14): 7702–11. https://doi.org/10.1073/pnas.1909902117. 

- Zhou, Z., Y. Ding, H. Shi, H. Cai, Q. Fu, S. Liu, and T. Li. 2020. “Analysis and Prediction of Vegetation Dynamic Changes in China: Past, Present and Future.” Ecological Indicators 117: 106642. https://doi.org/10.1016/j.ecolind.2020.106642. 

- Zhu, L., J. Meng, and L. Zhu. 2020. “Applying Geodetector to Disentangle the Contributions of Natural and Anthropogenic Factors to NDVI Variations in the Middle Reaches of the Heihe River Basin.” Ecological Indicators 117: 106545. https:// doi.org/10.1016/j.ecolind.2020.106545. 

How to cite this article: Zhao, Jiapei, Enliang Guo, Yongfang Wang, Yao Kang, Jisiguleng Wu, Yaodong Zhang, and Mengmeng Zhang. 2026. “Ecological Drought Patterns and Drivers in Inner Mongolia Using a Modified Temperature Vegetation Drought Index.” Ecosphere 17(4): e70600. <u>https://doi.org/10.1002/ ecs2.70600</u> 

