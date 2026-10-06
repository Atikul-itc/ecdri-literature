J Arid Land (2026) 18(5): 774–792 doi: 10.1016/j.jaridl.2026.05.003; CSTR: 32276.14.JAL.20250544 







# **Spatiotemporal patterns of meteorological–soil moisture drought propagation on the Qinghai-Xizang Plateau, China** 

WANG Zegen<sup>1*</sup> , CHEN Mi<sup>1,2</sup> , LIU Yaxin<sup>1</sup> , RAN Yaowen<sup>1</sup> , YONG Zhiwei<sup>1,3</sup> HUANG Yaoxuan<sup>1</sup> , WANG Yingyang<sup>1</sup> , ZHAO Junxin<sup>4</sup> 

1 School of Geoscience and Technology, Southwest Petroleum University, Chengdu 610500, China; 

- 2 Technology Innovation Center for Remote Sensing Monitoring of Natural Resources in Southwest China Mountains, Ministry of Natural Resources, Chengdu 610100, China; 

3 School of Resources and Environment, Chengdu University of Information Technology, Chengdu 610225, China; 

4 School of Civil Engineering and Geomatics, Southwest Petroleum University, Chengdu 610500, China 

**Abstract:** Drought is among the most destructive and recurrent natural disasters worldwide. In recent decades, the frequency of drought events has increased, exerting significant impacts on socioeconomic development. The propagation of meteorological drought (MD) to soil moisture drought (SMD) is a common natural process; however, its dynamics across different seasons and vegetation types on the Qinghai-Xizang Plateau, as well as the underlying meteorological driving mechanisms, remain insufficiently understood. This study utilized precipitation and soil moisture data from the European Centre for Medium-Range Weather Forecasts (ECMWF) Reanalysis v5 (ERA5)-Land reanalysis dataset for the period 1982–2022. The standardized precipitation index (SPI) and standardized soil moisture index (SSMI) were employed to characterize MD and SMD, respectively. By integrating run theory with an optimal parameter geographical detector (OPGD) model, this study systematically analyzed the average duration and propagation time of MD and SMD across the Qinghai-Xizang Plateau, and quantitatively evaluated the explanatory power of various meteorological and topographical factors influencing drought propagation. The results indicated that the mean duration of SMD across the Qinghai-Xizang Plateau from 1982 to 2022 was generally longer than that of MD. Significant seasonal differences in propagation time were observed, with the average propagation time ranked as winter (21 d)>spring (14 d)>autumn (10 d)>summer (8 d). Spatial variability of propagation time was more pronounced in spring and winter than in summer and autumn. Furthermore, the analysis of driving mechanisms revealed that drought propagation from MD to SMD on the Qinghai-Xizang Plateau was primarily influenced by precipitation (relative contribution proportion of 51.9%), followed by evaporation (15.1%) and snowmelt (13.6%), with the strongest interaction effects associated with precipitation. Although the dominant factors across different vegetation types were generally consistent with those for the entire plateau, solar radiation also showed a relatively high contribution (average 13.9%) across vegetation types. In summary, this study provides a scientific basis for improving drought early warning systems and optimizing water resource management strategies. 

**Keywords:** meteorological drought; soil moisture drought; drought propagation time; run theory; optimal parameter geographical detector (OPGD) model; standardized precipitation index (SPI); standardized soil moisture index (SSMI) 

**Citation:** WANG Zegen, CHEN Mi, LIU Yaxin, RAN Yaowen, YONG Zhiwei, HUANG Yaoxuan, WANG Yingyang, ZHAO 

> ∗Corresponding author: WANG Zegen (E-mail: zegen01@126.com) 

> Received: 2025-10-31; revised: 2026-04-15; accepted: 2026-04-27 

> © 2026 Xinjiang Institute of Ecology and Geography, Chinese Academy of Sciences, and Science Press. Publishing services by Elsevier B.V. on behalf of KeAi Communications Co. Ltd. 

This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/). 

**http://jal.xjegi.com; https://www.keaipublishing.com/en/journals/journal-of-arid-land/** 

WANG Zegen et al.: Spatiotemporal patterns of meteorological–soil moisture… 

775 

Junxin. 2026. Spatiotemporal patterns of meteorological–soil moisture drought propagation on the Qinghai-Xizang Plateau, China. Journal of Arid Land, 18(5): 774–792. https://doi.org/10.1016/j.jaridl.2026.05.003; https://cstr.cn/32276.14.JAL.20250544 

## **1  Introduction** 

Global warming is now an indisputable reality (Kaufman and Broadman, 2023), and under this context, both the frequency and intensity of drought events have increased significantly (Spinoni et al., 2018). Drought is one of the most widespread and destructive natural disasters (Ahmadi and Moradkhani, 2019; Sun et al., 2023), typically triggered by insufficient precipitation, a condition referred to as meteorological drought (MD). As MD persists, it leads to declines in soil moisture, reductions in surface runoff, and decreases in groundwater levels, gradually evolving into soil moisture and hydrological droughts (Zhang et al., 2022b). When water resource systems are unable to meet normal societal demands over an extended period, socioeconomic drought occurs, ultimately exerting adverse effects on economic development (Potop et al., 2014; Grillakis, 2019; Mei et al., 2025). Research indicates that nearly 70.0% of natural disasters worldwide are associated with meteorological phenomena, with droughts accounting for more than 50.0% of these events (Huang et al., 2016; Bai et al., 2023; Geng et al., 2024). Furthermore, the Sixth Assessment Report of the Intergovernmental Panel on Climate Change (IPCC) highlights that ongoing climate change is expected to accelerate the global hydrological cycle, leading to more frequent droughts and increasing their associated risks and impacts (Mondal et al., 2021; Corner, 2022). These trends pose significant challenges for the development of drought early warning systems and the implementation of effective mitigation strategies. 

Drought is generally classified into four fundamental types: meteorological, hydrological, soil moisture, and socioeconomic droughts (Mishra and Singh, 2010; Tian et al., 2022; Zhou et al., 2024), all of which are closely associated with imbalances at different stages of the hydrological cycle. MD is typically triggered by persistently below-average precipitation and often acts as a precursor to both soil moisture and hydrological droughts (Sturchio et al., 2004; Du et al., 2022). When precipitation deficits are accompanied by elevated vapor pressure deficits or increased atmospheric evaporative demand, soil moisture depletion occurs, hindering normal plant growth and reducing crop yields, thereby leading to soil moisture drought (SMD) (Yang et al., 2022a). A continued decline in soil moisture further reduces surface runoff and river discharge (runoff drought) and decreases groundwater storage and baseflow (groundwater drought), ultimately developing into hydrological drought (Geyaert et al., 2018). When drought conditions intensify to the extent that water resources can no longer meet societal demands, they may evolve into socioeconomic drought (Shi et al., 2018; Lin et al., 2023b), thereby exerting significant impacts on regional sustainable development. Notably, different types of droughts may occur either independently or simultaneously (Lin et al., 2023b). They exhibit strong spatiotemporal linkages, interact with one another, and undergo dynamic transformations through complex land-atmosphere interactions and hydrological processes (Peters-Lidard et al., 2021). The process by which drought signals are transmitted and evolve from one type to another is referred to as drought propagation (Sturchio et al., 2004; Apurv et al., 2017). Investigating drought propagation provides a valuable basis for the practical implementation of mitigation strategies. A robust understanding of the role of meteorological factors in SMD propagation, as well as in the transmission of drought-related impacts, is essential for improving the accuracy and effectiveness of drought mitigation efforts. 

To date, numerous studies have investigated drought propagation patterns, response mechanisms, and the identification of influencing factors. At the global scale, the propagation time from MD to hydrological drought is generally concentrated within 5–10 months, with a stronger linkage observed in humid regions characterized by high evapotranspiration, whereas this linkage is relatively weaker in arid regions (Shi et al., 2022). Based on terrestrial water storage (TWS), Cui et al. (2024) analyzed the response of hydrological drought to MD at the global scale and found that the propagation time ranges 0–4 months on the intra-annual scale and 1–16 months on the interannual scale, primarily influenced by the El Niño-Southern Oscillation, the North Atlantic Oscillation, and potential evapotranspiration (PET). At the regional scale, Wang et al. (2024) 

JOURNAL OF ARID LAND 2026 Vol. 18 No. 5 

776 

examined the propagation pathways and driving factors of multiple drought types on the Qinghai-Xizang Plateau, highlighting that natural factors such as precipitation, temperature, and PET, as well as human activities such as land use, significantly influence drought propagation. Focusing on different climate zones in China, Ding et al. (2021) analyzed the mechanisms underlying propagation among MD, SMD, and hydrological drought, and found that the linkage from SMD to hydrological drought is stronger in summer and autumn than in spring, and stronger in eastern regions than in western regions. Zhou et al. (2024) systematically reviewed the types, research methods, and characteristic parameters of drought propagation, and further synthesized the effects of natural factors (e.g., precipitation and evaporation) and human activities (e.g., reservoirs and irrigation) on propagation processes. 

The ecosystems of the Qinghai-Xizang Plateau are characterized by high sensitivity and fragility (Cui et al., 2015). Against the backdrop of global warming, drought conditions have become increasingly prevalent in this region (Feng et al., 2020; Wang et al., 2024), posing significant challenges to regional water vapor transport. Existing studies indicate that the probability of both SMD and hydrological drought increases with the intensification of MD (Wu and Hu, 2024; Wang et al., 2025b). SMD typically exhibits a lagged response to MD of approximately 2 – 3 months, with this lag period gradually extending from summer to winter (Lin et al., 2023b). Although these studies have improved our understanding of drought propagation and evolution mechanisms, research on the specific pathways and driving factors governing the transition from MD to SMD remains limited (Zhang et al., 2022b). Moreover, most existing studies are conducted at monthly temporal scales (Li et al., 2022a; Shi et al., 2022), which makes it difficult to capture rapid drought propagation processes and may compromise the accurate characterization of actual propagation dynamics. Therefore, there is an urgent need for systematic investigations at finer (daily) temporal resolutions to better understand rapid drought propagation and its driving mechanisms across the Qinghai-Xizang Plateau. 

In response to the aforementioned issues, this study employed the standardized precipitation index (SPI) and standardized soil moisture index (SSMI) to characterize MD and SMD, respectively. Drought events were identified using run theory, and the propagation time from MD to SMD, along with its driving mechanisms, is systematically analyzed using an optimal-parameter geographical detector (OPGD) model. Specifically, this study aims to: (1) reveal the spatiotemporal distribution patterns of MD and SMD on the Qinghai-Xizang Plateau from 1982 to 2022; (2) identify differences in drought propagation time across different seasons and vegetation types; and (3) explore the key driving factors of the drought propagation process. The findings are expected to provide theoretical support and a scientific basis for improving drought early warning and dynamic monitoring, optimizing regional water resource allocation strategies, and promoting ecological protection and sustainable development on the Qinghai-Xizang Plateau. 

## **2  Data and methods** 

### **2.1  Study area** 

The Qinghai-Xizang Plateau, located in western China (25°59′37″–39°49′33″N, 73°29′56″– 104°40′20″E), has an average elevation exceeding 4000 m, making it the highest plateau in the world. It is widely recognized as the "Water Tower of Asia" because it serves as the source of several major rivers (Sun et al., 2021), including the Yangtze River, the Yellow River, the Yarlung Tsangpo River, and the Lancang River. The plateau provides essential water resources for agriculture, industry, and domestic use to vast downstream populations. In addition, its extensive glaciers and lakes constitute a critical freshwater reserve, playing a vital role in maintaining regional ecological balance and regulating climate (Liu et al., 2020). The topography and vegetation distribution of the Qinghai-Xizang Plateau are illustrated in Figure 1. 

### **2.2  Data sources and preprocessing** 

The European Centre for Medium-Range Weather Forecasts (ECMWF) Reanalysis v5 (ERA5)-Land 

WANG Zegen et al.: Spatiotemporal patterns of meteorological–soil moisture… 

777 



**Fig. 1** Topography (a) and vegetation type distribution (b) of the Qinghai-Xizang Plateau. DEM, digital elevation model. 

reanalysis dataset, provided by the ECMWF (https://www.ecmwf.int/), offers multiple variables over the Qinghai-Xizang Plateau for the period 1982–2022, including total precipitation, 2 m air temperature, soil moisture in the first layer (0–7 cm), total evaporation, surface net solar radiation, snowmelt, and 10 m _u_ - and _v_ -wind components. Previous studies have demonstrated its high reliability and accuracy (Muñoz-Sabater et al., 2021; Sun et al., 2023). To further assess the applicability of ERA5-Land precipitation data for SPI calculation, this study collected observational records from 93 meteorological stations across and surrounding the Qinghai-Xizang Plateau, obtained from the National Meteorological Information Center of China (http://data.cma.cn/). Validation results showed strong consistency between ERA5-Land precipitation data and station-observed daily precipitation, with correlation coefficients generally exceeding 0.6 (Fig. 2). Considering potential biases in instrumental observations, the use of ERA5-Land precipitation data for SPI calculation is deemed both feasible and reliable. In addition, the ERA5-Land soil moisture data used for SSMI calculation also demonstrate high reliability. Previous studies indicate that this dataset performs consistently in representing temporal variability and shows good agreement with ground observations (Li et al., 2022b; Wang et al., 2022a). Given its temporal continuity and spatial consistency, ERA5-Land was considered a suitable soil moisture dataset for the Qinghai-Xizang Plateau (Dong et al., 2022); therefore, the SSMI derived from this dataset is reliable. In this study, soil moisture from the 0–7 cm layer was selected because grassland is the dominant vegetation type on the Qinghai-Xizang Plateau (Zhou et al., 2025), and plant roots are primarily concentrated in the surface soil layer. Consequently, vegetation water uptake mainly depends on surface soil moisture conditions, whereas deeper soil moisture contributes relatively little to plant water demand through root water absorption (Liu et al., 2025; Mei et al., 2025). The dataset has an hourly temporal resolution and a spatial resolution of 0.1°×0.1°. On the basis of the original hourly data, daily-scale variables were derived, including accumulated total precipitation, evaporation, surface net solar radiation, and snowmelt; 24-h averages of 2 m air temperature and soil moisture in the first layer (0–7 cm); and 24-h average wind speed calculated from the 10 m _u_ - and _v_ -wind components. 

The vegetation data were obtained from the 1:1,000,000 vegetation type spatial distribution dataset provided by the Data Center for Resources and Environmental Sciences, Chinese Academy 

JOURNAL OF ARID LAND 2026 Vol. 18 No. 5 

778 



**Fig. 2** Standardized Taylor diagram of daily total precipitation. RMSD, root mean square deviation. 

of Sciences (https://www.resdc.cn/Default.aspx), with an original spatial resolution of 1 km (Gong et al., 2023). In this study, coniferous forests, broadleaf forests, and mixed conifer-broadleaf forests were grouped into a single forest category, while grasslands and tussock vegetation were classified as grasslands. To facilitate the analysis of drought propagation time across different vegetation types and their influencing factors, we resampled the dataset to a spatial resolution of 0.1° using the mode method. 

The elevation data used in this study were obtained from the Shuttle Radar Topography Mission Digital Elevation Model (SRTM DEM) (https://www.gscloud.cn/sources/details/305?pid=302). This dataset, jointly produced by the National Aeronautics and Space Administration (NASA), the National Geospatial-Intelligence Agency (NGA), and other institutions, provides high-precision topographic information on a global scale, with a spatial resolution of 90 m. To ensure consistency with other datasets, we clipped the digital elevation model (DEM) to the study area and resampled to a uniform spatial resolution of 0.1°. 

### **2.3  Methods** 

The methodological framework of this study consists of three main components (Fig. 3). First, MD and SMD are identified, and their spatiotemporal distribution patterns across the Qinghai-Xizang Plateau are analyzed. Second, propagation events from MD to SMD are detected, and the temporal characteristics of drought propagation are examined. Finally, the driving factors influencing the timing of drought propagation are explored. 

### **2.3.1** Drought indices 

The SPI is derived from observed precipitation data and is widely used to characterize MD features across different spatial and temporal scales (Yang et al., 2023). The SSMI effectively captures the full drought cycle, from onset and progression to alleviation, making it suitable for monitoring and assessing regional SMD conditions (Yang et al., 2022b). Accordingly, this study employed SPI and SSMI to identify MD and SMD, respectively. The calculation of SPI involves treating precipitation data over a specified time scale as a probability density function, from which the corresponding cumulative probability function is derived (Mckee et al., 1993). This cumulative probability is then transformed into a standard normal distribution. The calculation principle of SSMI is analogous to that of SPI (Zhou et al., 2019a). 

### **2.3.2** Drought propagation time 

Drought propagation time generally refers to the interval between the onset of MD and the onset of 

WANG Zegen et al.: Spatiotemporal patterns of meteorological–soil moisture… 

779 





**Fig. 3** Technical flowchart of this study. MD, meteorological drought; SMD, soil moisture drought; SPI, standardized precipitation index; SSMI, standardized soil moisture index; OPGD, optimal parameter geographical detector; IQR, interquartile range. 

SMD. Run theory, a widely used time series analysis method in drought research, was employed in this study to identify the onset and termination of MD and SMD on the basis of SPI and SSMI, respectively (Lin et al., 2023b). Following the classification criteria for SMD and MD grades (GB/T 20481-2017) issued by the National Climate Center of China (Lin et al., 2023a; Xu et al., 2023), a threshold of – 0.5 was adopted for identifying both MD and SMD events (Fig. 4). The specific identification procedure is as follows: the first date on which SPI remains continuously below –0.5 is considered the onset of MD, and drought events lasting more than 10 consecutive days with SPI values below –0.5 are identified (Wang et al., 2022b). When SPI rises to –0.5 or above, the drought is deemed to have ended. The same procedure was applied to the SSMI series to identify SMD events. Drought duration is defined as the period from onset to termination, while drought frequency refers to the number of drought events occurring within a given time frame. Drought propagation frequency is defined as the frequency of MD evolving into SMD. 

**2.3.3** OPGD model 

The geographical detector is a spatial statistical method widely used to reveal the heterogeneity of geographic elements and their driving mechanisms, as well as to identify the spatial distribution characteristics of variables and their influencing factors (Wang and Xu, 2017). However, traditional geographical detector models have clear limitations in data processing, particularly regarding the discretization of spatial data and the assessment of spatial scale effects, which often rely on subjective judgment and lack quantitative standards. To overcome these limitations, the OPGD model systematically optimizes key parameters, thereby enhancing the accuracy and objectivity of spatial analyses (Song et al., 2020). In this study, the OPGD model was employed to analyze the influence of natural factors on the propagation time from MD to SMD through factor detection. The factor detector uses the _q_ -statistic to quantify the explanatory power of a driving factor _X_ on the spatial heterogeneity of the dependent variable _Y_ , calculated as follows (Wang and Xu, 2017): 

JOURNAL OF ARID LAND 2026 Vol. 18 No. 5 

780 



**Fig. 4** Schematic diagram of run theory: illustration of MD to SMD propagation events 



where _Nv_ and σ _v_ 2 represent the number and variance of observations in the entire study area, 2 respectively; and _Nv_ , _j_ and σ _v_ , _j_ denote the number and variance of observations in the _j_<sup>th</sup> ( _j_ =1, 2, …, _M_ ) variable, respectively. Larger values of _q_ indicate that the explanatory variable has a relatively greater influence on the spatial heterogeneity of the dependent variable. 

Building on this, to more intuitively compare the relative importance of different natural factors in a multi-driver scenario, this study further introduced the contribution rate index. This index was calculated by normalizing the _q_ -value of a single driving factor against the sum of _q_ -values for all factors included in the analysis, and is expressed as a percentage to represent the relative contribution of each factor to the overall explanatory power. Compared with the raw _q_ -value, the contribution rate more clearly reflects the relative contribution structure among multiple driving factors and is therefore used to highlight the dominant factors in drought propagation. 

## **3  Results** 

### **3.1  Spatiotemporal patterns of MD and SMD duration** 

The distribution of MD and SMD durations on the Qinghai-Xizang Plateau from 1982 to 2022 at interannual and seasonal scales is presented in Figure 5. At the interannual scale, the mean duration of MD ranged from 81 to 125 d (Fig. 5a), with the Qaidam Basin and the southwestern Qinghai-Xizang Plateau experiencing significantly longer droughts than other regions. The annual mean duration of SMD ranged from 0 to 169 d (Fig. 5b), with longer durations generally observed in the western and northern Qinghai-Xizang Plateau compared with the east. At the seasonal scale, the mean duration of MD across the four seasons ranged from 11 to 40 d (Fig. 5c, e, g, and i). The spatial distribution in spring, summer, and autumn generally mirrored the interannual patterns, whereas in winter, drought duration in the central Qinghai-Xizang Plateau increased markedly, exceeding that in other areas. The seasonal mean duration of SMD ranged from 0 to 102 d (Fig. 5d, f, h, and j). In spring, summer, and autumn, SMD persisted longer in the northwest than in the southeast, while in winter the spatial pattern was reversed. Overall, from 1982 to 2022, the average duration of SMD on the Qinghai-Xizang Plateau was generally longer than that of MD. 

### **3.2  Propagation time from MD to SMD** 

**3.2.1** Frequency of drought propagation events occurring across different seasons 

Figure 6 shows the spatial distribution of the annual and seasonal frequencies of MD-to-SMD 

WANG Zegen et al.: Spatiotemporal patterns of meteorological–soil moisture… 

781 





**Fig. 5** Distribution of MD and SMD interannual (a and b) and seasonal (c–j) durations on the Qinghai-Xizang Plateau from 1982 to 2022. Spring, March–May; summer, June–August; autumn, September–November; winter, December–February. 

propagation events across the Qinghai-Xizang Plateau from 1982 to 2022. The annual average frequency ranged from 0 to 103 events, with high-frequency areas primarily concentrated in the southwestern and southeastern Qinghai-Xizang Plateau, as well as the Qaidam Basin. Seasonal analysis indicated that the frequency of propagation events ranged from 0 to 42 occurrences, with spring, summer, and autumn exhibiting markedly higher frequencies than winter. The highest average frequency occurred in summer (18 events), followed by spring and autumn (13 events each), while winter showed the lowest frequency, with only 5 events. 

JOURNAL OF ARID LAND 2026 Vol. 18 No. 5 

782 





**Fig. 6** Spatial patterns of annual (a) and seasonal (b–e) average frequencies of MD to SMD propagation events on the Qinghai-Xizang Plateau from 1982 to 2022 

### **3.2.2** Drought propagation time for different vegetation types 

Further analysis of the propagation time from MD to SMD across the Qinghai-Xizang Plateau from 1982 to 2022 indicated a range of 3–53 d, with an average propagation time of 11 d (Fig. 7a). Spatially, the shortest propagation time was observed in the western and central-southern regions, as well as in the Qaidam Basin, whereas relatively longer propagation time occurred in the eastern Qinghai-Xizang Plateau. The longest propagation time was found in the southwestern and southern regions. Regionally, 19.1% of the Qinghai-Xizang Plateau experienced propagation time of 3–9 d, while the majority (74.5%) fell within 9–15 d (Fig. 7b). Additionally, 6.3% of the area exhibited propagation time of 15–25 d, and only a very small proportion (0.1%) showed propagation time extending from 25 to 53 d. Analysis of propagation time across different vegetation types revealed that meadows have a mean propagation time of 12 d, while forests, shrubs, and grasslands each have an average of 11 d (Fig. 7c). The maximum propagation time reached 53 d for forests and meadows, compared with 24 d for shrubs and grasslands. Overall, there was no significant difference in the average propagation speed from MD to SMD among vegetation types; however, in terms of maximum propagation time, meadows and forests exhibited longer durations than grasslands and shrubs. 

### **3.2.3** Drought propagation time in different seasons 

Figure 8 shows the spatial distribution of MD-to-SMD propagation times across different seasons. Overall, propagation time exhibited clear seasonal variations: 0–96 d in spring (mean 14 d), 1–57 d 

WANG Zegen et al.: Spatiotemporal patterns of meteorological–soil moisture… 

783 



**Fig. 7** Propagation time from MD to SMD on the Qinghai-Xizang Plateau from 1982 to 2022. (a), spatial distribution of average propagation time from MD to SMD; (b), probability density function of MD to SMD propagation time; (c), propagation time from MD to SMD for different vegetation types. 



**Fig. 8** Spatial distribution of propagation time from MD to SMD across different seasons on the Qinghai-Xizang Plateau from 1982 to 2022. (a), spring; (b), summer; (c), autumn; (d), winter. 

in summer (mean 8 d), 0–47 d in autumn (mean 10 d), and 0–142 d in winter (mean 21 d). Propagation times in spring and winter were notably longer than those in summer and autumn. 

Spatially, the southeastern Qinghai-Xizang Plateau exhibited notably longer propagation time in spring. In summer, regional differences were generally minor, with only slightly longer durations 

JOURNAL OF ARID LAND 2026 Vol. 18 No. 5 

784 

observed in a few southern areas. During autumn, relatively longer propagation time was concentrated in the southwestern region, while in winter, propagation time was generally prolonged across the entire Qinghai-Xizang Plateau, particularly in the northwest, where some areas exceeded two months. Regarding spatial heterogeneity, spring and winter displayed much greater variability in propagation time compared with summer and autumn. 

Based on the above analysis, we further examined the probability density functions of MD-to-SMD propagation time across different seasons (Fig. 9a). The results indicated that in spring, 61.7% of the Qinghai-Xizang Plateau experienced propagation time of 5–15 d; in summer, 83.3% of areas fell within 5–15 d; in autumn, 90.7% of areas exhibited propagation times of 5–20 d; and in winter, 70.8% of the region had propagation time of 10–30 d. Overall, propagation time was longest in winter, followed by spring, and shortest in summer and autumn. Figure 9b illustrates seasonal propagation time across different vegetation types. Both the mean and variability of propagation time in winter were significantly higher than in other seasons, particularly in grasslands. Propagation time in spring was also relatively long, whereas summer and autumn generally exhibited shorter and more concentrated propagation time across all vegetation types. Although some differences were observed among vegetation types, the overall seasonal variation pattern remained consistent. 



**Fig. 9** Propagation time from MD to SMD for different vegetation types and seasons. (a), probability density function of propagation time from MD to SMD across different seasons; (b), propagation time from MD to SMD across different seasons for various vegetation types. 

### **3.3  Driving factors of MD to SMD propagation** 

### **3.3.1** Single factor driving force 

Globally, the driving factors of drought are highly complex, with various natural factors regulating the drought propagation process by affecting different components of the hydrological cycle. In this study, precipitation, evaporation, temperature, snowmelt, elevation, wind speed, and solar radiation were selected as key driving factors. Using the OPGD model, the influence of each individual factor on the spatial heterogeneity of drought propagation time across the Qinghai-Xizang Plateau was quantified. The results are presented in Figures 10 and 11. 

The results indicated that the propagation from MD to SMD was jointly regulated by multiple factors, with precipitation, evaporation, and snowmelt identified as the primary drivers, exhibiting explanatory powers ( _q_ -values) of 0.133, 0.039, and 0.035, respectively (Fig. 10a). Notably, precipitation played a dominant role in the drought propagation process, contributing more than 50.0% to the overall effect (Fig. 10b). In contrast, environmental factors such as elevation, solar radiation, temperature, and wind speed exerted weaker influences, reflecting the constraints imposed by the alpine geomorphology on drought propagation. 

Considering different vegetation types, the dominant driving factors of drought propagation varied significantly. For forests, precipitation, snowmelt, air temperature, and solar radiation played major roles, with cumulative contributions exceeding 80.0% (Fig. 10b); their respective _q_ -values 

WANG Zegen et al.: Spatiotemporal patterns of meteorological–soil moisture… 

785 





**Fig. 10** Single-factor explanatory power (a) and contribution to different vegetation types (b) 

were 0.154, 0.118, 0.053, and 0.051, respectively. In contrast, evaporation, elevation, and wind speed exerted smaller influences, with _q_ -values of 0.023, 0.038, and 0.027, respectively (Fig. 11a). For grasslands and shrubs, drought propagation time was primarily governed by the combined effects of precipitation, evaporation, and snowmelt, with cumulative contributions of 75.4% and 69.4%, respectively (Fig. 10b). Among these, the _q_ -values of precipitation for grasslands and shrubs were 0.210 and 0.085, respectively (Fig. 11b and c). For meadows, propagation time was mainly influenced by precipitation, solar radiation, elevation, and snowmelt, each contributing over 15.0% (Fig. 10b), with respective _q_ -values of 0.113, 0.087, 0.083, and 0.082 (Fig. 11d). **3.3.2** Multi-factor interactions 

Using the interaction detection method, the effects of interactions among driving factors on the propagation time from MD to SMD were further analyzed (Figs. 10 and 11). The results showed that the interaction effects were generally stronger than the influence of individual factors, primarily exhibiting dual-factor enhancement or nonlinear enhancement patterns. This finding 

JOURNAL OF ARID LAND 2026 Vol. 18 No. 5 

786 





**Fig. 11** Single-factor explanatory power and factor interaction across different vegetation types. (a), forest; (b), grassland; (c), shrub; (d), meadow. 

indicated that the drought propagation process is not controlled by any single factor, but rather results from the combined influence of multiple environmental variables. 

Overall, the strongest interactive combinations were all associated with precipitation, highlighting its central role in the drought propagation process. Specifically, interactions between precipitation and temperature, evaporation, snowmelt, and solar radiation were the most significant, 

WANG Zegen et al.: Spatiotemporal patterns of meteorological–soil moisture… 

787 

with _q_ -values of 0.187, 0.183, 0.182, and 0.208, respectively (Fig. 10a). These findings aligned with the single-factor analysis and further confirmed the dominant roles of precipitation, evaporation, and snowmelt in drought propagation. From the perspective of different vegetation types (Fig. 11), propagation time in forests was most strongly influenced by interactions between precipitation and evaporation and between precipitation and snowmelt, with _q_ -values of 0.264 and 0.247, respectively. In grasslands, the dominant interactions occurred between precipitation and temperature and between precipitation and snowmelt, with _q_ -values of 0.284 and 0.297, respectively. For shrubs, drought propagation was primarily driven by interactions between precipitation and solar radiation and between precipitation and evaporation, with _q_ -values of 0.187 and 0.180, respectively. In meadows, the most significant interactions were between solar radiation and precipitation, evaporation, and elevation, with _q_ -values of 0.215, 0.215, and 0.213, respectively. In summary, multi-factor interaction analysis indicated that precipitation was the core driving factor in the propagation from MD to SMD, and its interactions with other environmental variables exerted strong influences across all vegetation types. 

## **4  Discussion** 

### **4.1  Drought propagation mechanism** 

From 1982 to 2022, the overall duration of SMD on the Qinghai-Xizang Plateau was longer than that of MD (Fig. 5), consistent with previous studies (Lin et al., 2023b; Lu et al., 2024; Sun et al., 2025). The relatively shorter duration of MD can be attributed to the rapid re-establishment of water balance following increases in precipitation or decreases in evaporation, which facilitates quick drought alleviation (Mei et al., 2025). In contrast, SMD exhibits a pronounced lagged response to changes in precipitation and evaporation. Even after the cessation of MD, SMD may persist and require a longer recovery period to return to normal conditions (Zhu et al., 2021). Regarding seasonal distribution, the frequency of drought propagation events was higher in summer than in winter (Fig. 6). This is primarily because meteorological anomalies, such as high temperature and elevated evaporation, are rapidly transmitted through the active "soil-vegetation-atmosphere" system (Lin et al., 2023b). Strong solar radiation and vigorous vegetation transpiration accelerate soil moisture depletion. In contrast, during winter, vegetation dormancy and soil freezing weaken water exchange within the system, reducing the efficiency of drought propagation (Zhang et al., 2022b). 

The propagation time from MD to SMD across the Qinghai-Xizang Plateau exhibited pronounced spatial heterogeneity (Fig. 7), which is closely linked to multiple factors, including geographical environment, climatic conditions, and human activities (Sun et al., 2023; Wang et al., 2024). Under varying environmental conditions, the drought propagation process differs, particularly in alpine regions, where climatic inputs are jointly influenced by watershed area, soil moisture content, and vegetation type. Vegetation further regulates this process through its control of evaporation (Vicente-Serrano et al., 2019; Sun et al., 2025). No significant differences were observed in the average propagation speed from MD to SMD among different vegetation types. However, meadows and forests exhibited slightly longer propagation time than grasslands and shrubs, primarily due to their higher vegetation coverage, denser canopy structures, and deeper root systems (Zhao et al., 2018). During MDs, deep roots can access water from deeper soil layers, making these vegetation types less sensitive to fluctuations in surface soil moisture and helping maintain higher plant water status (Deng et al., 2021; Zhang et al., 2022a), thereby delaying the onset of drought stress. In contrast, shrubs and grasslands rely predominantly on shallow soil moisture (Shao et al., 2022). While they can sustain growth using shallow water storage during the early stages of drought, prolonged drought leads to rapid depletion of available water, resulting in faster drought propagation and consequently shorter propagation time (Wu et al., 2018). 

Further analysis of the seasonal characteristics of drought propagation revealed that the propagation time from MD to SMD was generally longer in spring and winter than in summer and autumn (Fig. 8), and this seasonal pattern was consistent across different vegetation types (Fig. 9). 

JOURNAL OF ARID LAND 2026 Vol. 18 No. 5 

788 

During summer, the simultaneous increase in temperature and precipitation accelerates the regional water cycle and enhances vegetation evaporation demand (Qian et al., 2016). These factors collectively promote the rapid development of drought, thereby shortening the propagation time from MD to SMD (Han et al., 2019). This finding aligns with previous studies (Sun et al., 2023), which reported that MD-to-SMD propagation is slower in spring and winter. Specifically, after the frozen period ends in spring, rising temperatures and meltwater from snow and frozen soil replenish surface runoff, delaying the onset of SMD (Dong et al., 2020). 

### **4.2  Driving factors of drought propagation** 

MD often evolves into SMD, a propagation process characterized by notable lag effects and threshold behavior (Li et al., 2023). This evolution is jointly influenced by multiple factors, including climatic variables, human activities, evaporation, and elevation (Dai et al., 2020; Ndehedehe et al., 2020; Li et al., 2022c). To quantify these influences, this study employed the OPGD to assess the extent to which precipitation, temperature, evaporation, snowmelt, solar radiation, wind speed, and elevation affect the propagation time from MD to SMD across the Qinghai-Xizang Plateau. The results indicate that precipitation and evaporation are the primary drivers of drought propagation (Fig. 10), consistent with previous studies (Schubert et al., 2016; Wu et al., 2024; Mei et al., 2025). 

Specifically, precipitation exerts the most significant influence among all factors (Wang et al., 2024). As precipitation increases, its relationship with surface runoff strengthens, indicating that even minor fluctuations in rainfall can substantially alter surface water conditions (Peterson et al., 2021). Conversely, a decrease in precipitation directly reduces soil moisture, particularly in the topsoil, where water content drops rapidly, thereby limiting the water uptake capacity of crop roots (Zhou et al., 2019b). Furthermore, soil moisture depletion caused by initial precipitation deficits can further reduce actual evaporation and near-surface atmospheric moisture, leading to an increase in vapor pressure deficit (VPD) (Zhou et al., 2019b). This feedback loop exacerbates soil water depletion, amplifying drought conditions (Wang et al., 2025a). Rising temperatures enhance evaporation and accelerate soil moisture loss. Under hot and dry conditions, vegetation water demand increases, further intensifying soil water depletion and aggravating SMD (Liu et al., 2024; Mei et al., 2025). Snowmelt also plays an important role on the Qinghai-Xizang Plateau, as it replenishes soil moisture and surface runoff, mitigating SMD to some extent (Peña-Guerrero et al., 2020). Across different vegetation types, the primary drivers of drought propagation are generally consistent with the overall pattern on the Qinghai-Xizang Plateau, with precipitation remaining the most significant factor (Fig. 11). Elevation is particularly influential in meadow areas, as it regulates soil water storage and consumption, thereby significantly affecting drought propagation time (Mei et al., 2025). Overall, the propagation of MD to SMD on the Qinghai-Xizang Plateau is primarily controlled by precipitation, evaporation, and snowmelt, with their interactions jointly shaping the drought propagation process. Therefore, studies of meteorological and SMD in this region should comprehensively consider precipitation, evaporation, snowmelt, and other environmental factors under varying seasonal and vegetation conditions, as well as regional socioeconomic contexts, to systematically support adaptive drought risk management (Li et al., 2022c; Wang et al., 2024). 

### **4.3  Uncertainties and future works** 

This study examined the duration of MD and SMD, the propagation time from MD to SMD, and their driving factors across the Qinghai-Xizang Plateau from 1982 to 2022. Due to complex land-atmosphere interactions, the drought propagation process exhibits pronounced spatial heterogeneity (Wang et al., 2025b). A comprehensive understanding of this process is essential for elucidating the mechanisms underlying drought propagation. However, existing studies face several limitations. First, the accuracy of the datasets may influence statistical results. In particular, the ERA5-Land reanalysis dataset over the Qinghai-Xizang Plateau may contain systematic biases due to sparse observational stations and complex terrain. Second, the drought indices currently applied may introduce uncertainties. For example, the SPI may overestimate or underestimate actual 

WANG Zegen et al.: Spatiotemporal patterns of meteorological–soil moisture… 

789 

drought severity, especially in regions primarily supplied by glacier and snowmelt runoff (Rehana and Monish, 2021). Therefore, it is necessary to evaluate the applicability of different drought indices, identify those best suited to local climatic conditions, or establish a multi-index integrated framework to improve the accuracy of drought assessment. Additionally, while the SSMI adopts the computational framework of the SPI, differences in input data introduce uncertainties related to the choice of distribution functions, calculation periods, and data quality (Ding et al., 2021). Future studies should refine the SSMI algorithm and enhance its robustness by integrating multi-source datasets. Finally, interactions between meteorological and soil moisture droughts are complex and bidirectional, influenced by diverse and dynamically changing factors. Although this study considered meteorological variables such as precipitation, evaporation, and temperature, future research should incorporate socioeconomic indicators (e.g., GDP), human activities, multi-layer soil moisture, and topographic features (e.g., slope and aspect) to more comprehensively reveal the mechanisms driving drought propagation. 

## **5  Conclusions** 

In this study, we using meteorological and remote sensing data from 1982 to 2022, and integrating run theory and the optimal-parameter geographic detector method to systematically analyze the temporal characteristics of MD propagating to SMD on the Qinghai-Xizang Plateau and to elucidate the driving mechanisms of meteorological factors in this process. The main conclusions as follow, from 1982 to 2022, the average duration of SMD on the Qinghai-Xizang Plateau was generally longer than that of MD. The annual average frequency of MD-to-SMD propagation events ranged from 0 to 103, with significantly higher frequencies observed in spring, summer, and autumn compared with winter. There was no significant difference in the average propagation speed from MD to SMD among different vegetation types, although meadows and forests exhibited slightly longer propagation times than grasslands and shrubs. Distinct seasonal variations were observed in propagation time, following the order: winter (21 d)>spring (14 d)>autumn (10 d)>summer (8 d). Additionally, spatial variability in propagation time was more pronounced in spring and winter than in summer and autumn. The propagation time from MD to SMD on the Qinghai-Xizang Plateau was primarily influenced by precipitation (51.9%), evaporation (15.1%), and snowmelt (13.6%), with the strongest interactive factor combinations all involving precipitation. While the dominant driving factors were generally consistent across different vegetation types, solar radiation also contributed substantially in all vegetation types (average 13.9%), indicating that drought propagation is jointly governed by the interaction of multiple factors. Based on these findings, drought prevention and management on the Qinghai-Xizang Plateau should consider the time lag and seasonal differences in the propagation of MD to SMD, using MD as an early-warning precursor, while simultaneously promoting ecological restoration and structural optimization tailored to different vegetation types, in order to slow the progression of drought. 

## **Conflict of interest** 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

## **Acknowledgements** 

This research was supported by the Sichuan Science and Technology Program Project (2024YFHZ0133), the Science and Technology Innovation Center for Remote Sensing and Monitoring of Natural Resources in Southwest Mountainous Areas of the Ministry of Natural Resources (RSMNRSCM-2024-008), the Science and Technology Program Project of Xizang Autonomous Region (XZ201901-GA-07), the National Key Research and Development Program Project (2023YFC3006700), and the Sichuan Science and Technology Program (2025ZNSFSC0004). 

## **Author contributions** 

Conceptualization: WANG Zegen, CHEN Mi, HUANG Yaoxuan; Methodology: WANG Zegen, CHEN Mi, LIU 

JOURNAL OF ARID LAND 2026 Vol. 18 No. 5 

790 

Yaxin, RAN Yaowen, YONG Zhiwei, HUANG Yaoxuan; Supervision: WANG Zegen; Writing - original draft: CHEN Mi; Writing - review & editing: WANG Zegen, RAN Yaowen, YONG Zhiwei, WANG Yingyang; Research: CHEN Mi; Data management: LIU Yaxin; Software: ZHAO Junxin. All authors approved the manuscript. 

#### **References** 

Ahmadi B, Moradkhani H. 2019. Revisiting hydrological drought propagation and recovery considering water quantity and quality. Hydrological Processes, 33(10): 1492–1505. 

Apurv T, Sivapalan M, Cai X M. 2017. Understanding the role of climate characteristics in drought propagation. Water Resources Research, 53(11): 9304–9329. 

- Bai M, Li Z L, Huo P Y, et al. 2023. Propagation characteristics from meteorological drought to agricultural drought over the Heihe River Basin, Northwest China. Journal of Arid Land, 15(5): 523–544. 

- Corner S P. 2022. The sixth major IPCC assessment report and its implications: 15 September 2021. Weather, 77(2): 70–71. 

- Cui A H, Li J F, Zhou Q M, et al. 2024. Propagation dynamics from meteorological drought to GRACE-based hydrological drought and its influencing factors. Remote Sensing, 16(6): 976, doi: 10.3390/rs16060976. 

- Cui P, Su F H, Zou Q, et al. 2015. Risk assessment and disaster reduction strategies for mountainous and meteorological hazards in Tibetan Plateau. Chinese Science Bulletin, 60(32): 3067–3077. (in Chinese) 

Dai M, Huang S Z, Huang Q, et al. 2020. Assessing agricultural drought risk and its dynamic evolution characteristics. Agricultural Water Management, 231: 106003, doi: 10.1016/j.agwat.2020.106003. 

- Deng Y, Wang X H, Wang K, et al. 2021. Responses of vegetation greenness and carbon cycle to extreme droughts in China. Agricultural and Forest Meteorology, 298: 108307, doi: 10.1016/j.agrformet.2020.108307. 

- Ding Y B, Gong X L, Xing Z X, et al. 2021. Attribution of meteorological, hydrological and agricultural drought propagation in different climatic regions of China. Agricultural Water Management, 255: 106996, doi: 10.1016/j.agwat.2021.106996. 

- Dong Q, Chen X H, Chen J, et al. 2020. Mapping winter wheat in North China using Sentinel 2A/B data: A method based on phenology-time weighted dynamic time warping. Remote Sensing, 12(8): 1274, doi: 10.3390/rs12081274. 

- Dong X F, Lai X, Wang Y S, et al. 2022. Applicability evaluation of multiple sets of soil moisture data on the Tibetan Plateau. Frontiers in Earth Science, 10: 872413, doi: 10.3389/feart.2022.872413. 

- Du C, Chen J S, Nie T Z, et al. 2022. Spatial-temporal changes in meteorological and agricultural droughts in Northeast China: change patterns, response relationships and causes. Natural Hazards, 110(1): 155–173. 

- Feng W, Lu H W, Yao T C, et al. 2020. Drought characteristics and its elevation dependence in the Qinghai-Tibet Plateau during the last half-century. Scientific Reports, 10(1): 14323, doi: 10.1038/s41598-020-71295-1. 

- Geng G P, Zhang B, Gu Q, et al. 2024. Drought propagation characteristics across China: Time, probability, and threshold. Journal of Hydrology, 631: 130805, doi: 10.1016/j.jhydrol.2024.130805. 

- Geyaert A I, Veldkamp T I E, Ward P J. 2018. The effect of climate type on timescales of drought propagation in an ensemble of global hydrological models. Hydrology and Earth System Sciences, 22(9): 4649–4665. 

- Gong H D, Cheng Q P, Jin H Y, et al. 2023. Effects of temporal, spatial, and elevational variation in bioclimatic indices on the NDVI of different vegetation types in Southwest China. Ecological Indicators, 154: 110499, doi: 10.1016/j.ecolind.2023.110499. 

- Grillakis M G. 2019. Increase in severe and extreme soil moisture droughts for Europe under climate change. Science of The Total Environment, 660: 1245–1255. 

- Han Z M, Huang S Z, Huang Q, et al. 2019. Propagation dynamics from meteorological to groundwater drought and their possible influence factors. Journal of Hydrology, 578: 124102, doi: 10.1016/j.jhydrol.2019.124102. 

- Huang J P, Yu H P, Guan X D, et al. 2016. Accelerated dryland expansion under climate change. Nature Climate Change, 6(2): 166–171. 

- Kaufman D S, Broadman E. 2023. Revisiting the Holocene global temperature conundrum. Nature, 614(7948): 425–435. 

- Li C, Zhang X, Yin G D, et al. 2022a. Evaluation of drought propagation characteristics and influencing factors in an arid region of Northeast Asia (ARNA). Remote Sensing, 14(14): 3307, doi: 10.3390/rs14143307. 

- Li N, Zhou C Y, Zhao P. 2022b. The validation of soil moisture from various sources and its influence factors in the Tibetan Plateau. Remote Sensing, 14(16): 4109, doi: 10.3390/rs14164109. 

- Li Q Q, Ye A Z, Zhang Y H, et al. 2022c. The peer-to-peer type propagation from meteorological drought to soil moisture drought occurs in areas with strong land-atmosphere interaction. Water Resources Research, 58(9): e2022WR032846, doi: 10.1029/2022WR032846. 

- Li Y F, Huang S Z, Wang H, et al. 2023. Warming and greening exacerbate the propagation risk from meteorological to soil moisture drought. Journal of Hydrology, 622: 129716, doi: 10.1016/j.jhydrol.2023.129716. 

WANG Zegen et al.: Spatiotemporal patterns of meteorological–soil moisture… 

791 

- Lin C, He Y L, Wang Z Y. 2023a. Sensitivity of vegetation productivity to extreme droughts across the Yunnan Plateau, China. Atmosphere, 14(6): 1026, doi: 10.3390/atmos14061026. 

- Lin H, Yu Z B, Chen X G, et al. 2023b. Spatial-temporal dynamics of meteorological and soil moisture drought on the Tibetan Plateau: trend, response, and propagation process. Journal of Hydrology, 626: 130211, doi: 10.1016/j.jhydrol.2023.130211. 

- Liu Q, Liang L Q, Mcvicar T R, et al. 2024. Globally assessing how evapotranspiration feedbacks govern the impacts of multi-year droughts. Journal of Hydrology, 641: 131852, doi: 10.1016/j.jhydrol.2024.131852. 

- Liu Y W, Fan X W, Wang W, et al. 2025. Soil moisture drought and diverse impacts on vegetation across the Tibetan Plateau in recent three decades. Science of The Total Environment, 963: 178367, doi : 10.1016/j.scitotenv.2025.178367. 

- Liu Z F, Yao Z J, Wang R, et al. 2020. Estimation of the Qinghai-Tibetan Plateau runoff and its contribution to large Asian rivers. Science of The Total Environment, 749: 141570, doi: 10.1016/j.scitotenv.2020.141570. 

- Lu H L, Qiu J, Hu B X, et al. 2024. Potential impact of precipitation temporal structure on meteorological drought and vegetation 

condition: A case study on Qinghai-Tibet Plateau. Journal of Hydrology: Regional Studies, 56: 102048, doi: 10.1016/j.ejrh.2024.102048. 

McKee T B, Doesken N J, Kleist J R. 1993. The relationship of drought frequency and duration to time scales. In: Proceedings of the 8<sup>th</sup> Conference on Applied Climatology. American Meteorological Society. Anaheim, USA, 179 – 183. 

Mei L, Aru H, Tong S Q, et al. 2025. Study on the propagation processes and driving mechanisms of meteorological, hydrological, 

and agricultural droughts on the Mongolian Plateau. Journal of Hydrology, 660: 133511, doi: 10.1016/j.jhydrol.2025.133511. 

Mishra A K, Singh V P. 2010. A review of drought concepts. Journal of Hydrology, 391(1–2): 204–216. 

Mondal S K, Huang J L, Wang Y J, et al. 2021. Doubling of the population exposed to drought over South Asia: CMIP6 multi-model-based analysis. Science of The Total Environment, 771: 145186, doi: 10.1016/j.scitotenv.2021.145186. 

- Muñoz-sabater J, Dutra E, Agustí-Panareda A, et al. 2021. ERA5-Land: a state-of-the-art global reanalysis dataset for land applications. Earth System Science Data, 13(9): 4349–4383. 

Ndehedehe C E, Agutu N O, Ferreira V G, et al. 2020. Evolutionary drought patterns over the Sahel and their teleconnections with low frequency climate oscillations. Atmospheric Research, 233: 104700, doi: 10.1016/j.atmosres.2019.104700. 

- Peña-Guerrero M D, Nauditt A, Muñoz-robles C, et al. 2020. Drought impacts on water quality and potential implications for agricultural production in the Maipo River Basin, Central Chile. Hydrological Sciences Journal, 65(6): 1005–1021. 

- Peters-Lidard C D, Mocko D M, Su L, et al. 2021. Advances in land surface models and indicators for drought monitoring and prediction. Bulletin of the American Meteorological Society, 102(5): E1099–E1122. 

Peterson T J, Saft M, Peel M C, et al. 2021. Watersheds may not recover from drought. Science, 372(6543): 745–749. 

- Potop V, BoroneanŢ C, Možný M, et al. 2014. Observed spatiotemporal characteristics of drought on various time scales over the Czech Republic. Theoretical and Applied Climatology, 115(3): 563–581. 

- Qian Y Q, He F P, Wang W. 2016. Seasonality, rather than nutrient addition or vegetation types, influenced short-term temperature sensitivity of soil organic carbon decomposition. PLoS ONE, 11(4): e0153415, doi: 10.1371/journal.pone.0153415. 

- Rehana S, Monish N T. 2021. Impact of potential and actual evapotranspiration on drought phenomena over water and energy-limited regions. Theoretical and Applied Climatology, 144(1): 215–238. 

- Schubert S D, Stewart R E, Wang H L, et al. 2016. Global meteorological drought: A synthesis of current understanding with a focus on SST drivers of precipitation deficits. Journal of Climate, 29(11): 3989–4019. 

- Shao H, Zhang Y D, Yu Z, et al. 2022. The resilience of vegetation to the 2009/2010 extreme drought in Southwest China. Forests, 13(6): 851, doi: 10.3390/f13060851. 

- Shi H Y, Chen J, Wang K Y, et al. 2018. A new method and a new index for identifying socioeconomic drought events under climate change: A case study of the East River Basin in China. Science of The Total Environment, 616–617: 363–375. 

- Shi H Y, Zhou Z Q, Liu L, et al. 2022. A global perspective on propagation from meteorological drought to hydrological drought during 1902–2014. Atmospheric Research, 280: 106441, doi: 10.1016/j.atmosres.2022.106441. 

- Song Y Z, Wang J F, Ge Y, et al. 2020. An optimal parameters-based geographical detector model enhances geographic characteristics of explanatory variables for spatial heterogeneity analysis: cases with different types of spatial data. GIScience & Remote Sensing, 57(5): 593–610. 

- Spinoni J, Vogt J V, Naumann G, et al. 2018. Will drought events become more frequent and severe in Europe? International Journal of Climatology, 38(4): 1718–1736. 

- Sturchio N C, Du X, Purtschert R, et al. 2004. One million year old groundwater in the Sahara revealed by krypton-81 and chlorine-36. Geophysical Research Letters, 31(5): L05503, doi: 10.1029/2003GL019234. 

- Sun P, Liu R L, Yao R, et al. 2023. Responses of agricultural drought to meteorological drought under different climatic zones and vegetation types. Journal of Hydrology, 619: 129305, doi: 10.1016/j.jhydrol.2023.129305. 

- Sun P, Liu R L, Yao R, et al. 2025. Propagation threshold from meteorological to agricultural drought and its potential influence 

JOURNAL OF ARID LAND 2026 Vol. 18 No. 5 

792 

factors. Journal of Hydrology, 655: 132920, doi: 10.1016/j.jhydrol.2025.132920. 

Sun Y X, Liu S L, Liu Y X, et al. 2021. Effects of the interaction among climate, terrain and human activities on biodiversity on the Qinghai-Tibet Plateau. Science of The Total Environment, 794: 148497, doi: 10.1016/j.scitotenv.2021.148497. 

Tian F, Yang J H, Liu L Z, et al. 2022. Progress of research on the conception, characteristic, and influencing factors of drought 

propagation from the perspective of geographic sciences. Progress in Geography, 41(1): 173–184. (in Chinese) 

Vicente-Serrano S M, Peña-Gallardo M, Hannaford J, et al. 2019. Climate, irrigation, and land cover change explain streamflow trends in countries bordering the Northeast Atlantic. Geophysical Research Letters, 46(19): 10821–10833. 

Wang H, Zhao H, Wang F Q, et al. 2024. Study on the multi-type drought propagation process and driving factors on the Tibetan Plateau. Journal of Hydrology, 645: 132162, doi: 10.1016/j.jhydrol.2024.132162. 

Wang H M, Zan B L, Wei J F, et al. 2022a. Spatiotemporal characteristics of soil moisture and land-atmosphere coupling over the 

Tibetan Plateau derived from three gridded datasets. Remote Sensing, 14(22): 5819, doi: 10.3390/rs14225819. 

Wang J, Xu C. 2017. Geodetector: Principle and prospective. Acta Geographica Sinica, 72(1): 116–134. (in Chinese) 

Wang L, Wei W, Wang L X, et al. 2025a. Trigger thresholds and propagation mechanism of meteorological drought to agricultural 

drought in an inland river basin. Agricultural Water Management, 311: 109378, doi: 10.1016/j.agwat.2025.109378. 

Wang S Q, Huang S Z, Wang C, et al. 2025b. Global anthropogenic effects on meteorological—hydrological—soil moisture drought propagation: Historical analysis and future projection. Journal of Hydrology, 653: 132755, doi: 10.1016/j.jhydrol.2025.132755. 

Wang X D, Zhang B, Ma B, et al. 2022b. Spatial and temporal evolution of drought in Northeast China in recent 58 years based on daily SPEI. Plateau Meteorology, 41(3): 721–732. (in Chinese) 

Wu C G, Xu Y, Jin J L, et al. 2024. Meteorological to agricultural drought propagation time analysis and driving factors recognition considering time-variant characteristics. Water Resources Management, 38(3): 991–1010. 

Wu D, Hu Z Y. 2024. Characterization of drought propagation over the Tibetan Plateau. Journal of Hydrology-Regional Studies, 56: 102035, doi: 10.1016/j.ejrh.2024.102035. 

Wu X C, Liu H Y, Li X Y, et al. 2018. Differentiating drought legacy effects on vegetation growth over the temperate Northern Hemisphere. Global Change Biology, 24(1): 504–516. 

Xu Z G, Wu Z Y, Shao Q X, et al. 2023. From meteorological to agricultural drought: Propagation time and probabilistic linkages. Journal of Hydrology-Regional Studies, 46: 101329, doi: 10.1016/j.ejrh.2023.101329. 

Yang F, Duan X W, Guo Q K, et al. 2022a. The spatiotemporal variations and propagation of droughts in Plateau Mountains of China. Science of The Total Environment, 805: 150257, doi: 10.1016/j.scitotenv.2021.150257. 

Yang P, Zhai X Y, Huang H Q, et al. 2023. Association and driving factors of meteorological drought and agricultural drought in Ningxia, Northwest China. Atmospheric Research, 289: 106753, doi: 10.1016/j.atmosres.2023.106753. 

Yang W J, Li J Z, Feng P. 2022b. Evaluation of agricultural drought in Luanhe River Basin based on the standardized soil moisture index. Chinese Journal of Applied Ecology, 33(3): 801–807. (in Chinese) 

Zhang R R, Wu X P, Zhou X Z, et al. 2022a. Investigating the effect of improved drought events extraction method on spatiotemporal characteristics of drought. Theoretical and Applied Climatology, 147(1): 395–408. 

Zhang X, Hao Z C, Singh V P, et al. 2022b. Drought propagation under global warming: Characteristics, approaches, processes, and controlling factors. Science of The Total Environment, 838: 156021, doi: 10.1016/j.scitotenv.2022.156021. 

Zhao A Z, Zhang A B, Cao S, et al. 2018. Responses of vegetation productivity to multi-scale drought in Loess Plateau, China. CATENA, 163: 165–171. 

Zhou G S, Ren H R, Zhang L, et al. 2025. Annual vegetation maps in the Qinghai-Tibet Plateau (QTP) from 2000 to 2022 based on MODIS series satellite imagery. Earth System Science Data, 17(2): 773–797. 

Zhou H K, Wu J J, Li X H, et al. 2019a. Suitability of assimilated data-based standardized soil moisture index for agricultural drought monitoring. Acta Ecologica Sinica, 39(6): 2191–2202. (in Chinese) 

Zhou S, Williams A P, Berg A M, et al. 2019b. Land-atmosphere feedbacks exacerbate concurrent soil drought and atmospheric aridity. Proceedings of the National Academy of Sciences of the United States of America, 116(38): 18848–18853. 

Zhou Z Q, Wang P, Li L Q, et al. 2024. Recent development on drought propagation: A comprehensive review. Journal of Hydrology, 645: 132196, doi: 10.1016/j.jhydrol.2024.132196. 

Zhu Y, Liu Y, Wang W, et al. 2021. A global perspective on the probability of propagation of drought: From meteorological to soil moisture. Journal of Hydrology, 603: 126907, doi: 10.1016/j.jhydrol.2021.126907. 

