Science of the Total Environment 951 (2024) 175423 



Contents lists available at ScienceDirect 

# Science of the Total Environment 

journal homepage: www.elsevier.com/locate/scitotenv 



Three-dimensional ecological drought identification and evaluation method considering eco-physiological status of terrestrial ecosystems 



Yongwei Zhu<sup>a,b</sup> , Shanhu Jiang<sup>a,b,c,*</sup> , Liliang Ren<sup>a,b,d</sup> , Jianying Guo<sup>c</sup> , Feng Zhong<sup>b</sup> , Shuping Du<sup>b</sup> , Hao Cui<sup>b</sup> , Miao He<sup>b</sup> , Zheng Duan<sup>e</sup> 

a _The National Key Laboratory of Water Disaster Prevention, Hohai University, Nanjing 210098, China_ 

b _College of Hydrology and Water Resources, Hohai University, Nanjing 210098, China_ 

c _Yinshanbeilu Grassland Eco-hydrology National Observation and Research Station, China Institute of Water Resources and Hydropower Research, Beijing 100038, China_ 

d _Cooperative Innovation Center for Water Safety and Hydro-Science, Hohai University, Nanjing 210098, China_ e _Department of Physical Geography and Ecosystem Science, Lund University, Lund, Sweden_ 

### H I G H L I G H T S 

### G R A P H I C A L A B S T R A C T 

- Three-dimensional ecological drought 

- identification and evaluation method. 

- Coupled evaporation, soil moisture and vegetation index can reflect SIF changes. 

- The ecological drought primarily occurred from 1990 to 2010 across China. 

- Continuous ecological restoration alleviates ecological drought during 2010–2020. 



### A R T I C L E I N F O 

### A B S T R A C T 

Editor: Fernando Pacheco _Keywords:_ Ecological drought Drought propagation Three-dimensional clustering algorithm Climate change Ecological restoration 

Ecological drought is a complex process in terrestrial ecosystems where vegetation's eco-physiological functions are impaired due to water stress. However, there is currently a lack of long-term assessment of ecological drought from an eco-physiological perspective. In this study, the standardized ecological drought index (SESNDI) was developed using actual evaporation, root soil moisture, and kernel normalized difference vegetation index via the Euclidean distance method, reflecting ecosystem physiology, water supply capacity, and vegetation status. Solarinduced chlorophyll fluorescence validated SESNDI by reflecting vegetation photosynthesis. Using China as an example, severely impacted by climate change and ecological restoration, ecological drought's spatio-temporal variation and propagation characteristics was evaluated using clustering algorithms. The results demonstrated that (1) SESNDI showed superior performance over several other drought indices. (2) During 1982–2020, ecological drought was prevalent from 1990 to 2010, especially in the central and northeastern regions. (3) Compared to 1982–2000, the median duration and affected area of ecological drought events during 2001–2020 reduced by four months and 1.51 × 10<sup>5</sup> km<sup>2</sup> , respectively, while the median intensity increased by 0.06. (4) 

- Corresponding author at: The National Key Laboratory of Water Disaster Prevention, Hohai University, Nanjing 210098, China. _E-mail address:_ hik0216@hhu.edu.cn (S. Jiang). 

https://doi.org/10.1016/j.scitotenv.2024.175423 

Received 20 May 2024; Received in revised form 23 July 2024; Accepted 7 August 2024 Available online 10 August 2024 

0048-9697/© 2024 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies. 

_Y. Zhu et al._ 

_Science of the Total Environment 951 (2024) 175423_ 

Decreased precipitation and increased temperature were the primary factors contributing to the frequent occurrence of ecological drought in China from 1990 to 2010. This study offers a crucial methodology for evaluating ecological drought, serving as a reference for developing effective terrestrial restoration strategies. 

## **1. Introduction** 

Due to the intensifying effects of global warming, extreme climate events such as heatwaves and droughts have become prevalent, occurring with greater frequency and severity (Mukherjee and Mishra, 2021; Yuan et al., 2023; Zscheischler et al., 2018). Drought-induced water stress often triggers a chain reaction, impacting meteorological, agricultural, and hydrological systems, which in turn exert multiple pressures on terrestrial ecosystems (Christian et al., 2021; Fang et al., 2019; Guo et al., 2023). These cascading effects have significant negative consequences for the carbon balance, and biodiversity, posing a serious threat to the health and sustainability of terrestrial ecosystems (Gampe et al., 2021; Qiu et al., 2022). Ecological drought, an abbreviation for terrestrial ecosystem drought, has been widely studied as a new type of drought (Cui et al., 2024). Compared to meteorological and hydrological droughts, the response mechanisms of terrestrial ecosystems to drought stress are intricate, involving complex interactions among soil, plant physiology, and ecosystem structure and function (Munson et al., 2021; Sadiqi et al., 2022; Zhang et al., 2019). Furthermore, human-induced land-use changes, such as ecological restoration in China and multiple cropping in India agricultural fields, also influence the patterns of ecological drought evolution through the promotion of vegetation growth (Li et al., 2023b; Chen et al., 2019; Zhu et al., 2024). Consequently, monitoring ecological drought becomes more challenging and receives widespread attention due to these factors along with the impacts of climate change (Chang et al., 2023; Crausbay et al., 2020). 

Currently, there is no unified definition for ecological drought. The sixth assessment report from the Intergovernmental Panel on Climate Change (IPCC) classified ecological drought as a new type of drought and defined it as an ecological feedback related to plant water stress (Wang et al., 2023a). In addition, Crausbay et al. (2017) defined ecological drought as an episodic deficit in water availability that drives ecosystems beyond thresholds of vulnerability, impacts ecosystem services, and triggers feedbacks in natural or human systems. These definitions focus on water stress experienced by terrestrial ecosystems during ecological droughts (Bradford et al., 2020; Crausbay et al., 2020). When ecological drought occurs, the photosynthesis and transpiration of vegetation are often constrained. Therefore, some researchers argue that ecological drought can be defined as plant water stress (Chang et al., 2023; Munson et al., 2021). However, the measurement of plant sensitivity to water stress is challenging, making the monitoring of ecological drought extremely difficult (Wang et al., 2023c). Given climate change and vegetation greening, there is an urgent need for effective methods to detect ecological drought, which can enhance the ability of terrestrial ecosystems to cope with ongoing climate change (Crausbay et al., 2020; Jiang et al., 2021b). 

At present, several drought indices are used to monitor meteorological, agricultural, and hydrological droughts, such as the standardized precipitation index (SPI), standardized precipitation evapotranspiration index (SPEI), standardized soil moisture index (SSMI), standardized runoff index (SRI), and Palmer drought severity index (PDSI) (Cui et al., 2023; Gaire et al., 2023; Jiang et al., 2023a). However, there is no recognized indicator for monitoring ecological drought (Crausbay et al., 2017). Several indicators have been proposed for identifying ecological drought, including the evaporative stress index (ESI), which considers the degree of coupling between actual evaporation (ET) and potential evaporation (PET) (Chang et al., 2023), the ecological water deficit index (EWDI), which considers the supplydemand water balance for vegetation (Jiang et al., 2021b), the Gross Primary Productivity (GPP) anomaly index that evaluates the land 

carbon balance (Wang et al., 2023c), and the vegetation health index (VHI) that assesses the status of vegetation health (Wang et al., 2023a). These indicators effectively reflect the drought status of certain aspects of ecosystems. However, there is a lack of description of ecological drought from the perspective of ecosystem eco-physiological functions. Additionally, the complexity of calculating EWDI and the infrequent updates of GPP products have hindered timely assessments of ecological drought. Among these ecological drought indicators, vegetation and evaporation are the two key variables in defining ecological drought. Additionally, soil moisture, as a crucial water source for terrestrial ecosystems, is also considered in ecological drought monitoring. Ecological drought is necessarily a comprehensive drought of terrestrial ecosystems involving soil moisture, vegetation and evaporation, which in turn affects plant photosynthesis and transpiration (Chang et al., 2023; Munson et al., 2021). For instance, ESI can capture dynamic responses of vegetation to water limitation (Chang et al., 2023). Soil moisture can restrict vegetation water supply (Sun et al., 2023), and vegetation condition also can directly reflect water limitation (Wang et al., 2023a). Overall, evaporation, soil moisture, and vegetation can directly or indirectly indicate ecological drought. Evaporation, soil moisture, and vegetation are three key variables that reflect the physiological function, water supply capacity and vegetation status of terrestrial ecosystems (Hu et al., 2023; Jiang et al., 2023b). However, an ecological drought index coupled evaporation, soil moisture and vegetation has not been developed. 

In the three-dimensional index coupling method, the use of the Euclidean distance method to develop a three-dimensional drought index for meteorological and agricultural drought monitoring has gained widespread recognition (Amani et al., 2017; Liu et al., 2023b; Wei et al., 2020). When selecting specific indicators, root soil moisture (SMroot) is preferred over surface soil moisture (SMsur) as it can better reflect the moisture status in the vegetation root zone (Liu et al., 2023c). Similarly, kernel normalized difference vegetation index (kNDVI) is preferred over vegetation indices like leaf area index, as it provides a more accurate measure of land carbon sinks (Camps-Valls et al., 2021). Therefore, the goal of this study is to develop a standardized ecological drought index (SESNDI) by coupling ET, SMroot, and kNDVI using the Euclidean distance method on a spatial scale. Solar-induced chlorophyll fluorescence (SIF) can reflect vegetation photosynthesis (Entekhabi, 2023). In this study, we assume SESNDI can represent ecological drought. The correlation between SSIF and SESNDI was used to verify SESNDI in vegetation photosynthesis. To demonstrate the applicability of SESNDI, China was selected as a typical study area, which was severely affected by climate change and ecological restoration (Fu et al., 2023; Ge et al., 2021). Furthermore, we utilized a clustering algorithm to identify ecological drought events in the study area (Jiang et al., 2022; Wang et al., 2023b). 

In general, we developed a three-dimensional ecological drought identification and evaluation framework considering the ecological physiological status of terrestrial ecosystems. The primary purpose of this framework is to (1) verify the validity of the SESNDI in ecological drought detection compared with meteorological drought index, agricultural drought index, vegetation drought index, and another ecological drought index (SESI) considers evaporation functions, (2) reveal the spatiotemporal variation characteristics of two-dimensional and threedimensional ecological drought events in China using clustering algorithms, (3) analyze the driving factors behind the characteristics of ecological drought variation. Moreover, the two-dimensional ecological drought refers to the spatio-temporal distribution characteristics of ecological drought, while the three-dimensional ecological drought 

2 

_Y. Zhu et al._ 

_Science of the Total Environment 951 (2024) 175423_ 

pertains to the propagation process of ecological drought events. 

## **2. Methods** 

Three-dimensional ecological drought identification and evaluation framework considering eco-physiological status of terrestrial ecosystems includes the following three stages. First, SESNDI was developed based on ET, SMroot, and kNDVI. The effectiveness of SESNDI, along with SESI, SPI, SPEI, SSMI, and SVHI, in monitoring ecological drought is compared using SIF data (Section 2.1). Subsequently, the ecological drought characteristics of China from 1982 to 2020 were assessed using the standardized method, Sen's slope, and Mann-Kendall trend test (Section 2.2). Finally, China's three-dimensional ecological drought events were identified and evaluated through a three-dimensional clustering algorithm (Section 2.3). The specific methods used in each section are as follows. 

## _2.1. Definition and validation of SESNDI_ 

Drought monitoring indices constructed using the Euclidean distance method have been widely applied in countries such as the United States, Australia, and China (Amani et al., 2017; Liu et al., 2023b; Xu et al., 2022). As shown in Fig. 1, this study adopted the Euclidean distance method to construct SESNDI based on ET, SMroot, and kNDVI. The first step here is normalization of indicator variables. 







where _ETi_ , _SMrooti_ , and _kNDVIi_ represent the actual evaporation, root soil moisture, and kNDVI of the i-th month, respectively. 

ESNDI was created based on the Euclidean distance method. Its values range from 0 to 1, decreasing with increasing SMroot and kNDVI, and increasing with ET (Fig. 1). 





In Euclidean distance method, <u>√3̅̅3</u><sup>−</sup><sup>_NET_</sup> means that it and kNDVI ( ) 

(SMroot) have opposite influences on SESNDI. Finally, parameter estimation was performed by fitting the probability distribution function, and SESNDI was obtained by integrating the probability distribution function. 





In SESNDI, S stands for standardized, ESM represents ET, SMroot, and kNDVI, and DI stands for drought index. Based on references from other studies regarding drought level classification (Jiang et al., 2022; Feng et al., 2023), this study categorizes ecological drought level based on SESNDI as shown in Table 1. 

Previous studies have indicated that different probability distribution fittings yield minimal differences in optimal values. Although different probability distribution functions may affect the extreme values of the integration results, the overall distribution of the integration results remains relatively consistent (Feng et al., 2023). In this study, the commonly used gamma distribution is selected to fit and integrate ESI, P, SMI, VHI, and SIF. Using the method to calculate SESNDI, we computed SESI, SPI, SSMI, SVHI, and SSIF. The calculation formulas for ESI and VHI are as follows. 





The value of α is typically taken as 0.5. However, in this study, the value of α is considered in light of the dynamic index for scPDSI correction. VCI and TCL are normalized vegetation and land surface temperature indices, respectively, which can be referenced in (Zeng et al., 2023). 

The SIF, with its unique technical advantages in measuring vegetation photosynthetic physiology, serves as a direct detection method for assessing actual photosynthesis (Damm et al., 2015). In this study, we assume that SESNDI can represent ecological drought. The correlation between SSIF and SESNDI was used to verify SESNDI in vegetation photosynthesis. The Pearson correlation coefficient is calculated as follows. 



where _xi_ and _~~x~~_ are the values of SESNDI, SSEI, SPI, SPEI, SSMI, and SVHI for the i-th month and the average of all months, respectively. _yi_ and _~~y~~_ are the values of SSIF for the i-th month and the average of all months, respectively. 

## _2.2. Spatial trend analysis_ 

Spatial trend analysis and significance testing are mainly conducted 

**Table 1** 

**Fig. 1.** Definition and validation of SESNDI. On the left side, the red line (ED) represents the Euclidean distance, ranging from 0 to 1, where 1 indicates the maximum dryness and 0 indicates the minimum dryness. On the right side, the Stokes' shift phenomenon allows measurement of vegetation photosynthesis. By assessing the correlation with SIF, ecological drought index can be developed. SESNDI decreases with increasing kNDVI and SMroot, and increases with increasing ET. 

Drought level classification based on SESNDI. 

|Drought level|SESNDI|Drought severity|
|---|---|---|
|1|−<br>1_< SESNDI_|No drought|
|2|−<br>1_._5_< SESNDI_≤−<br>1_._0|Moderate drought|
|3|−<br>2_._0_< SESNDI_≤−<br>1_._5|Severe drought|
|4|_SESNDI_≤−<br>2_._0|Extreme drought|



3 

_Y. Zhu et al._ 

_Science of the Total Environment 951 (2024) 175423_ 

using Sen's slope and Mann-Kendall trend test (Gocic and Trajkovic, 2013). In the Sen's slope trend analysis method, the magnitude of β is the primary indicator for measuring trend changes. 



where the _β_ value _>_ 0 indicates an increasing trend, while the β value _<_ 0 indicates a decreasing trend. 

The steps for conducting the Mann-Kendall trend test are as follows. 



where n is the sample size. sgn represents the sign function, _xj_ and _xi_ are the j-th and i-th values of the sample sequence, respectively. _S_ is the statistic that follows a normal distribution. The standardized statistic of the time series is defined as Z. Trend and significance determination are shown in Table 2. 





## _2.3. Three-dimensional clustering algorithm_ 

The occurrence process of ecological drought involves dynamic propagation in both time and space. Three-dimensional spatial clustering algorithm is an important technique for identifying spatial drought patterns (Andreadis et al., 2005), which consists of three steps: drought clusters identification, temporal propagation of drought clusters, and migration of drought center locations (Fig. 2) (Liu et al., 2023c). In a two-dimensional context, ecological drought is considered to occur when SESNDI _<_ − 1. Clustering algorithms are used to aggregate grid points with SESNDI _<_ − 1, forming ecological drought clusters (Table 1). If the area of a drought cluster is larger than a threshold value (A), it is regarded as an ecological drought event in the two-dimensional space. Previous studies have suggested that the suitable value for A is 1.6 % of the study area. In this study, different area sizes were tested (Fig. S1), and A value was set as 1.6 % of the study area (i.e., 1538 grids) (Jiang et al., 2022; Wang et al., 2023b). In a three-dimensional context, adjacent monthly drought clusters are considered as the same ecological drought event if their overlapping area exceeds A. They are assigned the same identification number. Additionally, the center point of the ecological drought is calculated as the weighted center of ecological drought intensity. 



**Table 2** 

Trend features for Sen's slope and Mann-Kendall trend test methods. 

|_β_|_Z_|Trend features|
|---|---|---|
|_β >_0|_Z_≥1_._96|Significant increase<br>i|
||1_._65≤_Z <_1_._96|Slowly increase significantly<br>i|
|_β_≤0 or_β >_0|−<br>1_._65_< Z <_1_._65|No significant change<br>i|
|_β <_0|−<br>1_._96_< Z_≤−<br>1_._65|Slow down significantly<br>i|
||_Z_≤−<br>1_._96|Significant decline|





**Fig. 2.** Three-dimensional identification and propagation features of ecological drought. (a) Three-dimensional identification of ecological drought. (b) Process of ecological propagation. (c) Determination of the direction of ecological drought propagation. 

where _wi_ is the ecological drought intensity of the i-th grid, _xi_ and _yi_ are the latitude and longitude of the i-th grid. Furthermore, the ecological drought characteristics used in this study mainly include duration, intensity, affected area, center point, and center point migration direction. The intensity of ecological drought events refers to the weighted average of their area and SESNDI value. The center point migration direction is divided into four categories: east (315<sup>◦</sup> -45<sup>◦</sup> ), north (45<sup>◦</sup> -135<sup>◦</sup> ), west (135<sup>◦</sup> -225<sup>◦</sup> ), and south (225<sup>◦</sup> -315<sup>◦</sup> ). 

## **3. Material** 

## _3.1. Study area_ 

China, with a land area of approximately 9.6 million km<sup>2</sup> . From 1982 to 2020, China experienced an annual average precipitation of 636.3 mm and an annual average temperature of 9.7<sup>◦</sup> C. Additionally, this study divides China into seven regions (Fig. 3) based on multi-year average temperature, precipitation, and moisture conditions according to the results of Yao et al. (2018): the temperate and warm-temperate desert of northwest China (TWD), the temperate grassland of Inner Mongolia (TG), the temperate humid and sub-humid northeast China (THS), the warm-temperate humid and sub-humid north China (WHS), the subtropical humid central and south China (SH), the QinghaiTibetan Plateau (QTP), and the tropical humid south China (TH). 

## _3.2. Data_ 

Table 3 presents the detailed information about the remote sensing data utilized in this study. All data underwent validation and demonstrated good reliability (Wu and Gao, 2013; Zhong et al., 2022; Liu et al., 2023c; Li et al., 2023a; Li and Xiao, 2019; Zeng et al., 2023). Additionally, the nearest method was utilized in this study to interpolate data of different resolutions to a 0.1<sup>◦</sup> × 0.1<sup>◦</sup> resolution. Precipitation data was used for calculating SPI. PET and ET data were employed for building SESI. The soil moisture data includes SMsur and SMroot. SMsur data was applied for constructing SMI. NDVI data is used to build kNDVI. ET, SMroot, and kNDVI data were utilized for constructing SESNDI. SIF data was used for constructing SSIF. VHI, corrected based on scPDSI, was employed for constructing SVHI. The ecological restoration data are sourced from Bryan et al. (2018) and the China State Forestry and Grassland Administration. 

4 

_Y. Zhu et al._ 

_Science of the Total Environment 951 (2024) 175423_ 



**Fig. 3.** Geographical location and climatic division of China. 

**Table 3** 

Remote sensing data information and sources used in this study. 

|Production|Time|Resolution|Source|Version|
|---|---|---|---|---|
|P/T|1982–2020|0.25<sup>◦</sup>|Wu and Gao. (2013)|CN05.1|
|ET/PET|1982–2020|0.25<sup>◦</sup>|https://www.gleam.eu/|v3.7a|
|SM|1982-2020|0.1<sup>◦</sup>|https://www.geodata.cn/da<br>ta/|v1|
|NDVI|1982-2020|1/12<sup>◦</sup>|doi:https://doi.org/10.<br>5281/zenodo.8253971|v1|
|SIF|2000–2020|0.05<sup>◦</sup>|https://globalecology.unh.<br>edu/data/|v2|
|SPEI|1982-2020|0.5<sup>◦</sup>|https://spei.csic.es/databas<br>e.html|v2.9|
|VHI|1982-2020|4 km|Zeng et al. (2023)|v1|
|Wind|1982–2020|0.25<sup>◦</sup>|https://cds.climate.coperni<br>cus.eu/|ERA5|



Note: P, precipitation. T, temperature. ET, actual evaporation. PET, potential evaporation. SM, soil moisture. NDVI, normalized difference vegetation index. SIF, solar-induced chlorophyll fluorescence. SPEI, standardized precipitation evapotranspiration Index. VHI, vegetation health index. Wind direction at 800 hPa. 

## **4. Results** 

## _4.1. Applicability of SESNDI in ecological drought detection_ 

The Pearson correlation coefficients between SESNDI, SESI, SPI, SPEI, SMI, and SVHI with SSIF were calculated for eight regions at different time scales from 2001 to 2020 (Fig. 4). In the THS, QTP, SH, and TH regions, the Pearson correlation coefficients between SESNDI and SSIF outperformed SESI, SPI, SPEI, SMI, and SVHI at different time scales. Specifically, in the humid regions (SH and TH), the trend of Pearson correlation coefficients with SSIF was SESNDI _>_ SESI, SMI _>_ SVHI, SPEI, SPI. In the TWD, TG, and WHS regions, SESNDI and SSIF did 

not exhibit the strongest correlation compared to other drought monitoring indicators. For example, in the WHS region, SESI and SVHI showed better monitoring capability for ecological drought than SESNDI. In China, except for SVHI, the Pearson correlation coefficients with SSIF followed the pattern SESNDI _>_ SESI _>_ SMI _>_ SPI _>_ SPEI. Additionally, SVHI showed significant uncertainties in monitoring ecological drought at different regions and time scales, performing best in the WHS region and worst in the THS region. Moreover, at longer time scales, the Pearson correlation coefficients between each index and SSIF were higher, indicating that ecological drought is driven by long-term water deficiency (Jiang et al., 2022). 

The spatial distribution of Pearson correlation coefficients between different drought indices (SESNDI, SESI, SPI, SPEI, SMI, and SVHI) and SSIF from 2001 to 2020 at a 12-month scale was shown in Fig. 5. The proportions of SESNDI, SESI, SPI, SPEI, SMI, and SVHI with Pearson correlation coefficients _<_ 0.2 were 26.4 %, 31.6 %, 42.3 %, 51.3 %, 35.8 %, and 44.3 %, respectively, indicating that SESNDI _>_ SESI _>_ SMI _>_ SPI _>_ SVHI _>_ SPEI in terms of monitoring ecological drought. In terms of spatial distribution (Fig. 5 and Fig. S2), SESNDI displayed better ability for ecological drought monitoring compared to other drought monitoring indices in the THS, QTP, SH, and TH regions. In the TWD and WHS regions, SVHI performed better in ecological drought monitoring. In the TG region, SPI exhibited superior capability in ecological drought monitoring. Generally, in arid and semi-arid regions (TWD, TG, QTP), SPI and SVHI exhibited higher sensitivity to ecological drought compared to SESNDI. In humid and semi-humid regions (THS, SH, TH), SMI displayed greater sensitivity to ecological drought compared to SPI and SVHI but weaker than SESNDI. In addition, the Pearson correlation coefficient between SSIF and drought indices in different months and regions of China also supported the superior applicability of SESNDI in ecological drought detection compared to other drought detection indices (Figs. S3 and S4). Furthermore, the proportions of SESNDI and SSIF with positive and statistically significant Pearson correlation 

5 

_Y. Zhu et al._ 

_Science of the Total Environment 951 (2024) 175423_ 



**Fig. 4.** Pearson correlation coefficients between different types of drought indices with SSIF at different time scales in various regions of China from 2001 to 2020. 

coefficients in the TWD, TG, THS, QTP, WHS, SH, TH, and China were 69.1 %, 91.9 %, 76.9 %, 70.5 %, 77.5 %, 84.5 %, 95.0 %, and 78.9 %, respectively (Table 4). This indicates that the statistical correlation was reliable. SESNDI is an ecological drought index that considers the ecolphysiological status of terrestrial ecosystems. SSIF represents vegetation photosynthesis. In regions where the correlation between SESNDI and SSIF is low, SESNDI is not suitable as a substitute for monitoring vegetation photosynthesis using SSIF. 

## _4.2. Ecological drought characteristics_ 

The average distribution of SESNDI in different regions of China at timescales of 1–24 months from 1982 to 2020 are represented in Fig. 6. In terms of the temporal distribution of ecological drought in different regions, the TWD region mainly experienced ecological drought during the periods of 1989–1995 and 2000–2008. The TG and THS regions encountered ecological drought mainly from 1999 to 2011. The QTP region witnessed ecological drought primarily during 1986–1987, 1990–1995, and 2006–2007. The WHS region faced ecological drought mostly in 1986–1987, 1991–1995, 1997–2003, and 2006–2008. The TH and SH regions experienced ecological drought mainly from 1991 to 2009. In terms of the temporal distribution of wet and dry patterns in different regions, the TWD, QTP, SH, and TH regions showed a trend towards wet conditions after 2010. The WHS region exhibited an alternating pattern of wet and dry periods from 1982 to 2020. Notably, ecological drought in China was mainly prevalent from 1991 to 2010, with a shift towards wet conditions since 2010. 

Based on Mann-Kendall trend test and Sen's slope method, the interannual variation trend of SESNDI in China was analyzed. The spatial distribution of ecological drought trend in China showed certain heterogeneity, with values ranging from − 0.084 to 0.086 (Fig. 7a). In China, approximately 34.2 % of the regions displayed a drought trend, 

primarily concentrated in the northwest of the TWD region, TG region, THS region, the southern part of the QTP region, WHS region, and the northern part of the SH region (Fig. 7a). Additionally, Fig. 7b presents the Z values obtained from the Mann-Kendall trend test method in different regions of China. The median values for TWD, TG, THS, QTP, WHS, SH, TH, and China regions were 1.72, − 1.77, − 1.11, 3.00, 0.48, 1.84, 2.64, and 1.38, respectively. Among these regions, the median values for TWD, QTP, SH, and TH regions were _>_ 1.65, indicating that a significant decrease in ecological drought ( _P <_ 0.1). Specifically, the QTP region's median value exceeded 2.65, indicating that a significant decrease in ecological drought ( _P <_ 0.05). The TG region's median value fell below 1.65, indicating a slow increase in ecological drought (P _<_ 0.1). Additionally, Fig. 7c demonstrates that the proportions of regions experiencing significantly increasing, slowly increasing, relatively stable, slowly decreasing, and significantly decreasing ecological drought were 14.8 %, 3.2 %, 35.5 %, 4.6 %, and 41.9 %, respectively. Furthermore, the characteristics of ecological drought trend variation in different regions of China during different months were shown in Fig. S5, which aligned with the results of the inter-annual trend changes. 

## _4.3. Spatiotemporal propagation of three-dimensional ecological drought_ 

Based on the three-dimensional clustering algorithm, a total of 58 three-dimensional ecological drought events were detected from 1982 to 2020 (Table S1). However, it was observed that short-term threedimensional ecological drought events were unstable. Therefore, the following study primarily focuses on events lasting longer than 6 months. Table S2 provides detailed information on 34 identified ecological drought events lasting longer than 6 months. Fig. 8 illustrates the spatial distribution characteristics of these events, including their locations, average affected area, and average intensity. The size of the circles represents the average affected area of the ecological drought 

6 

_Y. Zhu et al._ 

_Science of the Total Environment 951 (2024) 175423_ 



**Fig. 5.** The spatial distribution of Pearson correlation coefficients between different types of drought indices and SSIF of in different regions of China. SESNDI, standardized ecological drought index. SESI, standardized evaporative stress index. SPI, standardized precipitation index. SPEI, standardized precipitation evapotranspiration index. SSMI, standardized soil moisture index. SVHI, standardized vegetation health index. 

events, while the color represents the average intensity. Notably, the intensity, affected area, and duration of ecological drought events exhibited significant spatial heterogeneity. The TWD, TG, THS, QTP, WHS, SH, and TH regions experienced 4, 1, 4, 9, 6, 10, and 0 ecological drought events, respectively. The majority of ecological drought events occurred in the TWD, THS, QTP, WHS, and SH regions, with average 

durations of 11 months, 19 months, 22 months, 11 months, and 22 months, respectively. The average affected areas of the TWD, THS, QTP, WHS, and SH regions were 4.3 × 10<sup>5</sup> km<sup>2</sup> , 7.6 × 10<sup>5</sup> km<sup>2</sup> , 9.2 × 10<sup>5</sup> km<sup>2</sup> , 5.5 × 10<sup>5</sup> km<sup>2</sup> , and 7.5 × 10<sup>5</sup> km<sup>2</sup> , while the average intensities were − 1.45, − 1.39, − 1.45, − 1.52, and − 1.51, respectively. 

The temporal evolution of ecological drought events in China was 

7 

_Y. Zhu et al._ 

_Science of the Total Environment 951 (2024) 175423_ 

**Table 4** 

Significance statistics of Pearson correlation coefficients between SESNDI and SSIF in different regions of China (0.1<sup>◦</sup> × 0.1<sup>◦</sup> ). 

|Regions|Total|_>_0|_>_0 and<br>significant|Proportion<br>of_>_ 0|Proportion of<br>_>_0 and<br>significant|
|---|---|---|---|---|---|
|TWD|9518|7493|6577|78.7 %|69.1 %|
|TG|8979|8566|8248|95.4 %|91.9 %|
|THS|10,741|9585|8256|89.2 %|76.9 %|
|QTP|17,361|14,084|12,245|81.1 %|70.5 %|
|WHS|9301|7840|7209|84.3 %|77.5 %|
|SH|17,642|15,853|14,911|89.9 %|84.5 %|
|TH|4856|4705|4611|96.9 %|95.0 %|
|China|78,295|68,029|61,763|86.9 %|78.9 %|





**Fig. 6.** Distribution of SESNDI in different regions of China at 1–24 months timescales from 1982 to 2020. The color green represents wet conditions, while the color red indicates drought conditions. TWD, TG, THS, QTP, WHS, SH, and TH are abbreviations for different regions in China. 

shown in Fig. 9a, with the average centroid positions of the first and second halves of the events represents by blue and orange, respectively. The spatial propagation of ecological drought events in China exhibited diverse directions. Specifically, the occurrences of ecological drought events in China were as follows: 9 times in direction 1 (0<sup>◦</sup> -45<sup>◦</sup> ), 4 times in direction 2 (45<sup>◦</sup> -90<sup>◦</sup> ), 2 times in direction 3 (90<sup>◦</sup> -135<sup>◦</sup> ), 5 times in direction 4 (135<sup>◦</sup> -180<sup>◦</sup> ), 5 times in direction 5 (180<sup>◦</sup> -225<sup>◦</sup> ), 2 times in direction 6 (225<sup>◦</sup> -270<sup>◦</sup> ), 1 time in direction 7 (270<sup>◦</sup> -315<sup>◦</sup> ), and 6 times in direction 8 (315<sup>◦</sup> -360<sup>◦</sup> ) (Fig. 9b-c). The proportions of ecological drought events occurring in the east (315<sup>◦</sup> -45<sup>◦</sup> ), north (45<sup>◦</sup> -135<sup>◦</sup> ), west (135<sup>◦</sup> -225<sup>◦</sup> ), and south (225<sup>◦</sup> -315<sup>◦</sup> ) directions in China were 44.2 %, 17.6 %, 29.4 %, and 8.8 %, respectively, indicating the ecological drought events in China were most likely to propagate towards the east. 

Furthermore, Fig. 10 illustrates the variation in the characteristics (duration, affected area, intensity and migration distance) of ecological drought events in China before and after 2000. The median duration of ecological drought events in China has decreased from 17.5 months to 13.5 months. The median affected area of ecological drought events has decreased from 7.47 × 10<sup>5</sup> km<sup>2</sup> to 5.96 × 10<sup>5</sup> km<sup>2</sup> . The median intensity 



**Fig. 7.** Interannual variation trends and significance levels of ecological drought in different regions of China from 1982 to 2020. 



**Fig. 8.** Spatial distribution of ecological drought events in China from 1982 to 2020. Circle size represents the average affected area of ecological drought events, while circle color represents the average intensity of ecological drought events. 

of ecological drought events in China has decreased from − 1.44 to − 1.50. From the box diagram (Fig. 10), the intensity of ecological drought increased significantly. The median migration distance of ecological drought events in China has decreased from 51 km to 34 km. This indicates that under the influence of climate change and human activities, compared to the period from 1982 to 2000, ecological drought events in China have occurred with a shorter duration and higher intensity during the period of 2001–2020. 

## _4.4. A three-dimensional typical ecological drought event in China_ 

Based on monitored ecological drought events, a typical ecological drought event was selected for analysis (Fig. 11). In southwest China, a severe meteorological drought occurred from 2009 to 2010, with a significant decrease in precipitation ranging from 30 % to 80 % during the same period, causing significant impacts on terrestrial ecosystems (Liu et al., 2023b). The method proposed in this study successfully monitored this ecological drought event (ED47). Fig. 11 illustrates the propagation mechanism of the ecological drought event in southwest 

8 

_Y. Zhu et al._ 

_Science of the Total Environment 951 (2024) 175423_ 



**Fig. 9.** Temporal evolution of the ecological drought events locations in China. (a) Trajectory of event locations over time, with blue and orange indicating the average center positions of the first and second halves of the event, respectively; (b) Distribution of movement direction and distance; (c) The number of ecological droughts in 8 directions: 1 (0<sup>◦</sup> -45<sup>◦</sup> ), 2 (45<sup>◦</sup> -90<sup>◦</sup> ), 3 (90<sup>◦</sup> -135<sup>◦</sup> ), 4 (135<sup>◦</sup> -180<sup>◦</sup> ), 5 (180<sup>◦</sup> -225<sup>◦</sup> ), 6 (225<sup>◦</sup> -270<sup>◦</sup> ), 7 (270<sup>◦</sup> -315<sup>◦</sup> ) and 8 (315<sup>◦</sup> -360<sup>◦</sup> ). 



**Fig. 10.** The characteristics of ecological drought events in China before and after 2000. 

China. ED47 began in December 2009 and ended in October 2010 (Fig. 11a). The center of ED47 initially started at 103.3<sup>◦</sup> E, 24.9<sup>◦</sup> N, and remained in this area for three months. The regional center then shifted to 106.1<sup>◦</sup> E, 26.1<sup>◦</sup> N, and remained there for four months. Subsequently, the regional center moved to 104.6<sup>◦</sup> E, 24.7<sup>◦</sup> N, and persisted there for another four months, marking the end of this ecological drought event. More details of the spatial distribution of ED47 can be obtained in the Fig. S6. Additionally, the cumulative intensity of the ED47 event peaked at − 32 (Fig. 11b). Furthermore, in May 2010, the affected area by the ecological drought event reached its maximum, covering an area of 7.6 × 105 km<sup>2</sup> (Fig. 11c). 

## **5. Discussion** 

## _5.1. Advantages of a new method for ecological drought identification_ 

The definition of ecological drought is still in the exploratory stage. Currently, indicators for characterizing ecological drought can be categorized into three types. The first type is single indicator, such as ecological drought indices considering GPP and NDVI anomalies (Nanzad et al., 2019; Wang et al., 2023c). These indices provide a simple and intuitive perspective from a specific aspect. The second type is composite indicators involving two variables, such as ecological drought indices decoupling ET and PET (Anderson et al., 2011; Chang et al., 2023), ecological drought indices coupling soil moisture and vegetation (Sun et al., 2023), and ecological drought indices coupling vegetation and temperature (Wang et al., 2023a). These indices aim to identify compound drought events in terrestrial ecosystems based on the relationship between two related variables. The third type is to develop the ecological drought index from the perspective of water supply and demand of vegetation (Jiang et al., 2022; Shi et al., 2022). 

Ecological drought is indeed a complex response of terrestrial ecosystems to drought (Crausbay et al., 2020; Munson et al., 2021). The above methods provide insights from specific perspectives but may lack comprehensive characterization of complex terrestrial ecosystems. In this study, a new method was proposed, considering three key variables: ET, SMroot, and kNDVI. These variables represent the physiological function, water supply capacity, and vegetation status of terrestrial ecosystems, respectively. Furthermore, the SESNDI was validated against the SSIF index, which reflects actual plant photosynthesis (Damm et al., 2015; Liu et al., 2023b). In the Section 4.1, we demonstrated that the SESNDI outperforms other drought indices, including meteorological drought indices (SPI and SPEI), agricultural drought indices (SSMI), vegetation drought indices (SVHI), and another ecological drought indices (SESI), in terms of ecological drought monitoring. 

In addition, from a regional perspective, Jiang et al., 2021b developed an ecological drought index based on vegetation's ecological water deficit and assessed ecological drought in the northwest region of China. The study revealed that ecological drought in this region was more frequent before 2000, followed by a dry-wet alternation between 2000 and 2010, and entered a humid period after 2010. These findings are consistent with the results obtained in our study, which focused on a similar region in China (TWD) (Fig. 6a). Furthermore, the new ecological drought index proposed in our study successfully detected the typical ecological drought event in southwest China (Fig. 11). From a nationwide perspective, Wang et al. (2023a) reflected the ecological drought situation in China by considering the vegetation health index coupled with vegetation and temperature. The study indicated that ecological drought in various regions of China has been gradually alleviated from 1982 to 2020. Similar conclusions were also drawn in our study, which provided insights into the characteristics of ecological drought events in different regions and periods in China. Therefore, overall, the ecological drought index (SESNDI) proposed in this study is considered scientific, rigorous, and excellent in representing ecological drought. In addition, compared to SIF, SESNDI has two advantages: it reflects longer-term trends and reveals ecological drought from ecophysiological status of terrestrial ecosystems. 

## _5.2. Impacts of climate change and human activities on ecological drought propagation_ 

Drought propagation refers to the temporal and spatial development process of drought events. The variation in the characteristics of drought propagation is mainly caused by the combined effect of climate change and human activities (Wang et al., 2023b; Zhang et al., 2023). Relevant studies have shown that climate change will intensify the frequency and severity of droughts (Yuan et al., 2023; Zscheischler et al., 2018). China, 

9 

_Y. Zhu et al._ 

_Science of the Total Environment 951 (2024) 175423_ 



**Fig. 11.** Spatiotemporal evolution of the ecological drought event in southwest China. (a) Three-dimensional spatiotemporal evolution, (b) cumulative impact intensity and center migration trajectory, (c) monthly variations in the affected area and intensity of ecological drought. 

located in eastern Asia, is one of the country most severely affected by climate change (Chen and Sun, 2015; Jiang et al., 2021a). As shown in Fig. 12, from 1982 to 2020, approximately 78 % of regions experienced 

an increase in precipitation, with 19 % of these areas displaying a significant rise. The average annual precipitation in China exhibited an insignificant upward trend from 1982 to 2020 but witnessed a 



**Fig. 12.** Climate change in China during 1982–2020. (a) Trend characteristics of precipitation, (b) average precipitation and wind direction, (c) Trend characteristics of temperature, and (d) average temperature and wind direction. 

10 

_Y. Zhu et al._ 

_Science of the Total Environment 951 (2024) 175423_ 

considerable increase after 2010 (Fig. 12a). Additionally, 100 % of areas experienced a temperature rise, with 96 % of these regions showing a significant increase. The average annual temperature in China demonstrated a noticeable upward trend from 1982 to 2020 (Fig. 12c). Moreover, due to the differential thermal effects between the sea and land, the land rapidly heats up during summer, forming a thermal lowpressure system (Ge et al., 2021). This system prompts warm and moist air to flow from the surrounding oceans towards the low-pressure center (Wang et al., 2023b). The transport of atmospheric water vapor leads to decreased precipitation in the downwind regions, which causes the spread of drought towards the downwind areas (Fig. 12b and d). This was the main reason for the eastward propagation of ecological drought in China. 

In addition, human activities that alter the underlying surface can also contribute to changes in the characteristics of drought propagation (Liu et al., 2023a; Zhang et al., 2022). Over the past four decades, China has implemented 16 ecological restoration projects (P1-P16) (Bryan et al., 2018), covering a cumulative area of 6.2 million km<sup>2</sup> with a total investment of 378 billion dollars (Fig. 13a and b). Particularly, the Grain for Green Program (P8) and Grassland Ecological Protection Program (P15) have played a significant role in transforming the underlying surface of China (Fig. 13c), leading to increased vegetation and greening (Chen et al., 2019; Li et al., 2021). This study revealed the variations in drought and wetness in different regions of China in Fig. 6 and Fig. 7. Ecological drought in China primarily occurred between 1990 and 2010, primarily due to a combination of reduced precipitation and higher temperatures during this period. However, from 2010 to 2020, China experienced a significant decline in the frequency of ecological drought due to increased precipitation and vegetation greening. The statistical findings presented in Fig. 10 indicate a decrease in the duration, affected area, and migration distance of ecological drought in China between 2001 and 2020, compared to the period from 1982 to 2000. However, the intensity of ecological drought has increased, suggesting that ecological restoration of China has enhanced the resilience of terrestrial 

ecosystems to drought, but the impact of rising temperature has resulted in more severe ecological drought events. 

## _5.3. Uncertainties and limitations_ 

Although the method proposed in this study takes into account three key characteristic variables that reflect the physiological function, water supply capacity and vegetation status of terrestrial ecosystems, there are still some uncertainties and limitations. Firstly, there is uncertainty in the data itself. The ET data is derived from the widely recognized GLEAM dataset. The SM data is sourced from (Liu et al., 2023c), which incorporates a weighted fusion of MERRA-2, CFSR, and ERA5-Land data, providing higher reliability. The NDVI data is sourced from (Li et al., 2023a), which is based on AVHRR, MODIS, and high-quality Landsat NDVI samples, also offering higher reliability. However, these remote sensing or model-derived datasets have inherent uncertainties, and future studies can utilize more remote sensing products and measured data to enhance the reliability of the results. Secondly, there is uncertainty in the monitoring indicators. For example, in the WHS region of China, the SESNDI proposed in this study is weaker in ecological drought monitoring than another ecological drought index (SESI) and vegetation health index (SVHI). This is mainly due to the fact that this region is a major agricultural production area in China, and human intervention has increased the difficulty of ecological drought monitoring (Wu et al., 2018). Furthermore, from Fig. 5a, it can be observed that SESNDI and SSIF exhibit a relatively low proportion of strong correlation ( _r >_ 0.6), indicating some limitations of SESNDI in replacing SSIF. However, SESNDI itself can reflect ecological drought conditions. In the future, more studies will be needed to better substitute SSIF in monitoring vegetation photosynthesis. The response of terrestrial ecosystems to drought is complex, and more methods need to be explored in the future to monitor ecological drought. 



**Fig. 13.** Ecological restoration projects in China. (a) start time of ecological restoration projects, (b) Cumulative area and investment for ecological restoration, and (c) Grain for Green Program during 1999–2019. P1-P16: 16 sustainability ecological restoration projects in China. 

11 

_Y. Zhu et al._ 

_Science of the Total Environment 951 (2024) 175423_ 

## **6. Conclusions** 

In this study, we have developed a new ecological drought index (SESNDI) based on three crucial variables that capture the physiological functioning, water supply capacity, and vegetation status of terrestrial ecosystems. By focusing on China as an example, a country significantly impacted by climate change and ecological restoration, we evaluated the spatiotemporal variations and three-dimensional propagation of ecological drought using the SESNDI. Our findings emphasize that the SESNDI is superior to meteorological drought index (SPI and SPEI), soil moisture index (SSMI), vegetation health index (SVHI) and another ecological drought index (SESI) in ecological drought monitoring. On a temporal scale, the ecological drought in China was predominantly concentrated between 1990 and 2010. Geographically, the TG, THS, and WHS regions of China were particularly vulnerable to ecological droughts. Moreover, in terms of the three-dimensional propagation of ecological drought, compared to the period of 1982–2000, the duration of ecological drought events in China during 2001–2020 has decreased by four months, the affected area has reduced by 1.51 × 10<sup>5</sup> km<sup>2</sup> , and the intensity has increased by 0.06. In our analysis of the causative factors, we highlight that reduced precipitation and increased temperature were the primary factors contributing to the frequent occurrence of ecological drought events in China during 1990–2010. However, increased precipitation and ecological restoration were the main drivers behind the significant reduction in ecological drought events during 2010–2020. Furthermore, while China's ongoing ecological restoration initiatives have enhanced the resilience of terrestrial ecosystems to drought, higher temperatures have contributed to the severity of ecological drought events. This study presents a crucial methodology for accurately monitoring and evaluating ecological drought. It also serves as a valuable reference for the development of effective terrestrial ecological restoration strategies. Future research needs to further utilize SIF or vegetation optical depth to quantify terrestrial ecosystem responses to drought. 

## **CRediT authorship contribution statement** 

**Yongwei Zhu:** Writing – original draft, Software, Methodology, Conceptualization. **Shanhu Jiang:** Writing – review & editing, Supervision, Funding acquisition. **Liliang Ren:** Supervision, Funding acquisition. **Jianying Guo:** Investigation. **Feng Zhong:** Visualization. **Shuping Du:** Software. **Hao Cui:** Methodology. **Miao He:** Methodology. **Zheng Duan:** Writing – review & editing. 

## **Declaration of competing interest** 

The authors declare no competing interests. 

## **Data availability** 

Data will be made available on request. 

## **Acknowledgements** 

This work was financially supported by the National Natural Science Foundation of China (U2243203); the Yinshanbeilu Grassland Ecohydrology National Observation and Research Station, China Institute of Water Resources and Hydropower Research (YSS202301); and the Fund of National Key Laboratory of Water Disaster Prevention (5240152I2). 

## **Appendix A. Supplementary data** 

Supplementary data to this article can be found online at https://doi. org/10.1016/j.scitotenv.2024.175423. 

## **References** 

- Amani, M., Salehi, B., Mahdavi, S., Masjedi, A., Dehnavi, S., 2017. Temperaturevegetation-soil moisture dryness index (TVMDI). Remote Sens. Environ. 197, 1–14. https://doi.org/10.1016/j.rse.2017.05.026. 

- Anderson, M.C., Hain, C., Wardlow, B., et al., 2011. Evaluation of drought indices based on thermal remote sensing of evapotranspiration over the continental United States. J. Climate 24 (8), 2025–2044. https://doi.org/10.1175/2010jcli3812.1. 

- Andreadis, K.M., Clark, E.A., Wood, A.W., Hamlet, A.F., Lettenmaier, D.P., 2005. Twentieth-century drought in the conterminous United States. J. Hydrometeorol. 6 (6), 985–1001. https://doi.org/10.1175/Jhm450.1. 

- Bradford, J.B., Schlaepfer, D.R., Lauenroth, W.K., Palmquist, K.A., 2020. Robust ecological drought projections for drylands in the 21st century. Glob. Chang. Biol. 26 (7), 3906–3919. https://doi.org/10.1111/gcb.15075. 

- Bryan, B.A., Gao, L., Ye, Y.Q., et al., 2018. China's response to a national land-system sustainability emergency. Nature 559 (7713), 193–204. https://doi.org/10.1038/ s41586-018-0280-2. 

- Camps-Valls, G., Campos-Taberner, M., Moreno-Martínez, A., et al., 2021. A unified vegetation index for quantifying the terrestrial biosphere. Sci. Adv. 7 (9), eabc7447 https://doi.org/10.1126/sciadv.abc7447. 

- Chang, Q., Ficklin, D.L., Jiao, W.Z., et al., 2023. Earlier ecological drought detection by involving the interaction of phenology and eco-physiological function. Earths Futur. 11 (3), e2022EF002667 https://doi.org/10.1029/2022EF002667. 

- Chen, H.P., Sun, J.Q., 2015. Changes in drought characteristics over China using the standardized precipitation evapotranspiration index. J. Climate 28 (13), 5430–5447. https://doi.org/10.1175/Jcli-D-14-00707.1. 

- Chen, C., Park, T., Wang, X.H., et al., 2019. China and India lead in greening of the world through land-use management. Nat. Sustain. 2 (2), 122–129. 

- Christian, J.I., Basara, J.B., Hunt, E.D., et al., 2021. Global distribution, trends, and drivers of flash drought occurrence. Nat. Commun. 12 (1), 6330. https://doi.org/ 10.1038/s41467-021-26692-z. 

- Crausbay, S.D., Ramirez, A.R., Carter, S.L., et al., 2017. Defining ecological drought for the twenty-first century. Bull. Am. Meteorol. Soc. 98 (12), 2543–2550. https://doi. org/10.1175/Bams-D-16-0292.1. 

- Crausbay, S.D., Betancourt, J., Bradford, J., et al., 2020. Unfamiliar territory: emerging themes for ecological drought research and management. One Earth 3 (3), 337–353. https://doi.org/10.1016/j.oneear.2020.08.019. 

- Cui, H., Jiang, S., Gao, B., et al., 2023. On method of regional non-stationary flood frequency analysis under the influence of large reservoir group and climate change. J. Hydrol. 618, 129255 https://doi.org/10.1016/j.jhydrol.2023.129255. 

- Cui, J., Chen, A., Huntingford, C., et al., 2024. Integrating ecosystem water demands into drought monitoring and assessment under climate change. Nat. Water 2, 215–218. https://doi.org/10.1038/s44221-024-00217-6. 

- Damm, A., Guanter, L., Paul-Limoges, E., et al., 2015. Far-red sun-induced chlorophyll fluorescence shows ecosystem-specific relationships to gross primary production: an assessment based on observational and modeling approaches. Remote Sens. Environ. 166, 91–105. https://doi.org/10.1016/j.rse.2015.06.004. 

- Entekhabi, D., 2023. Propagation in the drought cascade: observational analysis over the continental US. Water Resour. Res. 59, e2022WR032608. 

- Fang, W., Huang, S.Z., Huang, Q., et al., 2019. Probabilistic assessment of remote sensing-based terrestrial vegetation vulnerability to drought stress of the Loess Plateau in China. Remote Sens. Environ. 232, 111290 https://doi.org/10.1016/j. rse.2019.111290. 

- Feng, K., Yan, Z.Q., Li, Y.B., et al., 2023. Spatio-temporal dynamic evaluation of agricultural drought based on a three-dimensional identification method in Northwest China. Agric. Water Manag. 284, 108325 https://doi.org/10.1016/j. agwat.2023.108325. 

- Fu, B.J., Liu, Y.X., Meadows, M.E., 2023. Ecological restoration for sustainable development in China. Natl. Sci. Rev. 10 (7), nwad033 https://doi.org/10.1093/nsr/ nwad033. 

- Gaire, N.P., Zaw, Z., Br¨auning, A., et al., 2023. The impact of warming climate on Himalayan silver fir growth along an elevation gradient in the Mt. Everest region. Agr. Forest Meteorol. 339, 109575 https://doi.org/10.1016/j. agrformet.2023.109575. 

- Gampe, D., Zscheischler, J., Reichstein, M., et al., 2021. Increasing impact of warm droughts on northern ecosystem productivity over recent decades. Nat. Clim. Chang. 11 (9), 772–779. https://doi.org/10.1038/s41558-021-01112-8. 

- Ge, J., Qiu, B., Chu, B.W., et al., 2021. Evaluation of coupled regional climate models in representing the local biophysical effects of afforestation over continental China. J. Climate 34 (24), 9879–9898. https://doi.org/10.1175/Jcli-D-21-0462.1. 

- Gocic, M., Trajkovic, S., 2013. Analysis of changes in meteorological variables using Mann-Kendall and Sen’s slope estimator statistical tests in Serbia. Global Planet. Change 100, 172–182. https://doi.org/10.1016/j.gloplacha.2012.10.014. 

- Guo, W.W., Huang, S.Z., Huang, Q., et al., 2023. Drought trigger thresholds for different levels of vegetation loss in China and their dynamics. Agric. For. Meteorol. 331, 109349 https://doi.org/10.1016/j.agrformet.2023.109349. 

- Hu, Y., Wei, F.L., Fu, B.J., Zhang, W.M., Sun, C.L., 2023. Ecosystems in China have become more sensitive to changes in water demand since 2001. Commun. Earth Environ. 4 (1), 444. https://doi.org/10.1038/s43247-023-01105-9. 

- Jiang, S.H., Wei, L.Y., Ren, L.L., et al., 2021a. Utility of integrated IMERG precipitation and GLEAM potential evapotranspiration products for drought monitoring over mainland China. Atmos. Res. 247, 105141 https://doi.org/10.1016/j. atmosres.2020.105141. 

- Jiang, T.L., Su, X.L., Singh, V.P., Zhang, G.X., 2021b. A novel index for ecological drought monitoring based on ecological water deficit. Ecol. Indic. 129, 107804 https://doi.org/10.1016/j.ecolind.2021.107804. 

12 

_Y. Zhu et al._ 

_Science of the Total Environment 951 (2024) 175423_ 

- Jiang, T.L., Su, X.L., Singh, V.P., Zhang, G.X., 2022. Spatio-temporal pattern of ecological droughts and their impacts on health of vegetation in Northwestern China. J. Environ. Manage. 305, 114356 https://doi.org/10.1016/j.jenvman.2021.114356. 

- Jiang, S.H., Cui, H., Ren, L.L., et al., 2023a. Will China’s Yellow River basin suffer more serious combined dry and wet abrupt alternation in the future? J. Hydrol. 624, 129871 https://doi.org/10.1016/j.jhydrol.2023.129871. 

- Jiang, S.H., Zhu, Y.W., Ren, L.L., et al., 2023b. A complementary streamflow attribution framework coupled climate, vegetation and water withdrawal. Water Resour. Manag. 37 (12), 4807–4822. https://doi.org/10.1007/s11269-023-03582-1. 

- Li, X., Xiao, J., 2019. A global 0.05-degree product of solar-induced chlorophyll fluorescence derived from OCO-2, MODIS, and reanalysis data. Remote Sens. (Basel) 11, 517. https://doi.org/10.3390/rs11050517. 

- Li, C.J., Fu, B.J., Wang, S., et al., 2021. Drivers and impacts of changes in China's drylands. Nat. Rev. Earth Environ. 2 (12), 858–873. https://doi.org/10.1038/ s43017-021-00226-z. 

- Li, M.Y., Cao, S., Zhu, Z.C., et al., 2023a. Spatiotemporally consistent global dataset of the GIMMS normalized difference vegetation index (PKU GIMMS NDVI) from 1982 to 2022. Earth Syst. Sci. Data 15 (9), 4181–4203. https://doi.org/10.5194/essd-154181-2023. 

- Li, Y.F., Huang, S.Z., Wang, H., et al., 2023b. Warming and greening exacerbate the propagation risk from meteorological to soil moisture drought. J. Hydrol. 622, 129716 https://doi.org/10.1016/j.jhydrol.2023.129716. 

- Liu, Y., Shan, F.Z., Yue, H., Wang, X., 2023a. Characteristics of drought propagation and effects of water resources on vegetation in the karst area of Southwest China. Sci. Total Environ. 891, 164663 https://doi.org/10.1016/j.scitotenv.2023.164663. 

- Liu, Y., Yu, X.Y., Dang, C.Y., et al., 2023b. A dryness index TSWDI based on land surface temperature, sun-induced chlorophyll fluorescence, and water balance. Isprs J. Photogramm. 202, 581–598. https://doi.org/10.1016/j.isprsjprs.2023.07.005. 

- Liu, Y.X., Yang, Y.P., Song, J., 2023c. Variations in global soil moisture during the past decades: climate or human causes? Water Resour. Res. 59 (7), e2023WR034915 https://doi.org/10.1029/2023WR034915. 

- Mukherjee, S., Mishra, A.K., 2021. Increase in compound drought and heatwaves in a warming world. Geophys. Res. Lett. 48 (1), e2020GL090617 https://doi.org/ 10.1029/2020GL090617. 

- Munson, S.M., Bradford, J.B., Hultine, K.R., 2021. An integrative ecological drought framework to span plant stress to ecosystem transformation. Ecosystems 24 (4), 739–754. https://doi.org/10.1007/s10021-020-00555-y. 

- Nanzad, L., Zhang, J.H., Tuvdendorj, B., et al., 2019. NDVI anomaly for drought monitoring and its correlation with climate factors over Mongolia from 2000 to 2016. J. Arid Environ. 164, 69–77. https://doi.org/10.1016/j.jaridenv.2019.01.019. 

- Qiu, R.A., Li, X., Han, G., et al., 2022. Monitoring drought impacts on crop productivity of the US Midwest with solar-induced fluorescence: GOSIF outperforms GOME-2 SIF and MODIS NDVI, EVI, and NIRv. Agric. For. Meteorol. 323, 109038 https://doi.org/ 10.1016/j.agrformet.2022.109038. 

- Sadiqi, S.S.J., Hong, E.M., Nam, W.H., Kim, T., 2022. Review: an integrated framework for understanding ecological drought and drought resistance. Sci. Total Environ. 846, 157477 https://doi.org/10.1016/j.scitotenv.2022.157477. 

- Shi, M.Q., Yuan, Z., Shi, X.L., et al., 2022. Drought assessment of terrestrial ecosystems in the Yangtze River Basin, China. J. Clean. Prod. 362, 132234 https://doi.org/ 10.1016/j.jclepro.2022.132234. 

- Sun, M.Z., Li, X.Y., Xu, H., et al., 2023. Drought thresholds that impact vegetation reveal the divergent responses of vegetation growth to drought across China. Glob. Chang. Biol. 30, e16998 https://doi.org/10.1111/gcb.16998. 

- Wang, F., Lai, H.X., Li, Y.B., et al., 2023a. Dynamic variations of terrestrial ecological drought and propagation analysis with meteorological drought across the mainland China. Sci. Total Environ. 896, 165314 https://doi.org/10.1016/j. scitotenv.2023.165314. 

- Wang, X.J., Zhang, B.Q., Zhang, Z.Y., et al., 2023b. Identifying spatiotemporal propagation of droughts in the agro-pastoral ecotone of northern China with longterm WRF simulations. Agric. For. Meteorol. 336, 109474 https://doi.org/10.1016/ j.agrformet.2023.109474. 

- Wang, Y.H., Zhou, H., Huang, J.J., Yu, J.X., Yuan, Y.B., 2023c. A framework for identifying propagation from meteorological to ecological drought events. J. Hydrol. 625, 130142 https://doi.org/10.1016/j.jhydrol.2023.130142. 

- Wei, W., Pang, S.F., Wang, X.F., et al., 2020. Temperature vegetation precipitation dryness index (TVPDI)-based dryness-wetness monitoring in China. Remote Sens. Environ. 248, 111957 https://doi.org/10.1016/j.rse.2020.111957. 

- Wu, J., Gao, X.J., 2013. A gridded daily observation dataset over China region and comparison with the other datasets. Chin. J. Geophys. 56 (4), 1102–1111. https:// doi.org/10.6038/cjg20130406. 

- Wu, L.Y., Feng, J.M., Miao, W.H., 2018. Simulating the impacts of irrigation and dynamic vegetation over the North China Plain on regional climate. J. Geophys. Res.-Atmos. 123 (15), 8017–8034. 

- Xu, M.Y., Yao, N., Hu, A.N., et al., 2022. Evaluating a new temperature-vegetationshortwave infrared reflectance dryness index (TVSDI) in the continental United States. J. Hydrol. 610, 127785 https://doi.org/10.1016/j.jhydrol.2022.127785. 

- Yao, N., Li, Y., Lei, T., et al., 2018. Drought evolution, severity and trends in mainland China over 1961-2013. Sci. Total Environ. 616, 73–89. 

- Yuan, X., Wang, Y.M., Ji, P., et al., 2023. A global transition to flash droughts under climate change. Science 380 (6641), 187–191. https://doi.org/10.1126/science. abn6301. 

- Zeng, J.Y., Zhou, T., Qu, Y.P., et al., 2023. An improved global vegetation health index dataset in detecting vegetation drought. Sci. Data 10 (1), 338. https://doi.org/ 10.1038/s41597-023-02255-3. 

- Zhang, B.Q., AghaKouchak, A., Yang, Y.T., Wei, J.H., Wang, G.Q., 2019. A water-energy balance approach for multi-category drought -assessment across globally diverse hydrological basins. Agric. For. Meteorol. 264, 247–265. https://doi.org/10.1016/j. agrformet.2018.10.010. 

- Zhang, T., Su, X.L., Zhang, G.X., et al., 2022. Evaluation of the impacts of human activities on propagation from meteorological drought to hydrological drought in the Weihe River Basin, China. Sci. Total Environ. 819, 153030 https://doi.org/ 10.1016/j.scitotenv.2022.153030. 

- Zhang, Q., Miao, C.Y., Guo, X.Y., Gou, J.J., Su, T., 2023. Human activities impact the propagation from meteorological to hydrological drought in the Yellow River Basin, China. J. Hydrol. 623, 129752 https://doi.org/10.1016/j.jhydrol.2023.129752. 

- Zhong, F., Jiang, S., Dijk, A., 2022. Revisiting large-scale interception patterns constrained by a synthesis of global experimental data. Hydrol. Earth Syst. Sci. 26, 5647–5667. https://doi.org/10.5194/hess-26-5647-2022. 

- Zhu, Y., Jiang, S., Ren, L., et al., 2024. A systematic feedback assessment framework to identify the impact of climate change and ecological restoration on water yield patterns. Water Resour. Manag. 38, 3179–3195. 

- Zscheischler, J., Westra, S., van den Hurk, B., et al., 2018. Future climate risk from compound events. Nat. Clim. Chang. 8, 469–477. https://doi.org/10.1038/s41558018-0220-z. 

13 

