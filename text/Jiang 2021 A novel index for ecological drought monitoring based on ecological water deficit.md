Ecological Indicators 129 (2021) 107804 



Contents lists available at ScienceDirect 

# Ecological Indicators 

journal homepage: www.elsevier.com/locate/ecolind 



## A novel index for ecological drought monitoring based on ecological water deficit 



### Tianliang Jiang<sup>a,b</sup> , Xiaoling Su<sup>a,b,*</sup> , Vijay P. Singh<sup>c,d</sup> , Gengxi Zhang<sup>a,b</sup> 

a _College of Water Resources and Architectural Engineering, Northwest A & F University, Yangling, Shannxi 712100, China_ 

b _Key Laboratory for Agricultural Soil and Water Engineering in Arid Area of Ministry of Education, Northwest A & F University, Yangling, Shannxi 712100, China_ 

c _Department of Biological and Agricultural Engineering and Zachry Department of Civil & Environmental Engineering, Texas A & M University, College Station, TX 77843-2117, USA_ 

d _National Water and Energy Center, UAE University, Al Ain, United Arab Emirates_ 

|A R T I C L E I N F O|A B S T R A C T|
|---|---|
|_Keywords:_<br>Ecological drought<br>Vegetation index<br>Remote sensing<br>Rotational empirical orthogonal function<br>Northwestern China|Although the concept of ecological drought was first defined by the Science for Nature and People Partnership<br>(SNAPP) in 2016, there remains no widely accepted ecological drought monitoring index. Therefore, this study<br>constructed a new ecological drought index, the standardized ecological water deficit index (SEWDI). The SEWDI<br>is based on the difference between ecological water requirement and consumption, referred to as the stan-<br>dardized precipitation index (SPI) method, which was used to monitor ecological drought in Northwestern China<br>(NWRC). The performance of the SEWDI was compared with that of other widely–used drought indices,<br>including standardized root soil moisture index (SSI), self–calibrated Palmer drought index (scPDSI), standard-<br>ized precipitation–evaporation drought index (SPEI), and SPI, using the Pearson correlations between these<br>indices and standardized normalized difference vegetation index (SNDVI) under different time scales, wetness<br>and water use efficiencies (WUE) of vegetation. The SEWDI at a 12–month scale was decomposed in NWRC<br>during 1982–2015 using the rotational empirical orthogonal function (REOF) in order to demarcate five<br>ecological drought regions, including southeastern sub–region (SE), southwestern sub–region (SW), north-<br>western sub–region (NW), northeastern sub–region (NE), and central sub–region (CT). The characteristics of<br>ecological drought in NWRC, such as intensity, duration, and frequency, were extracted using the run theory. The<br>return periods of five types of drought were calculated using wavelet analysis. Results showed that the perfor-<br>mance of SEWDI in monitoring ecological drought was the best among the drought indices under different time<br>scales, and the 12–month–scale was largely unaffected by wetness and WUE. Results of monitoring indicated that<br>serious ecological droughts in the NWRC mainly occurred in 1982–1986, 1990–1996, and 2005–2010, primarily<br>in SE, SW, and CT, SW and NE, and NW, NE, and CT, respectively. Furthermore, SEWDI in the arid SW, NW and<br>CT showed a longer return period compared to that in the humid NE and SE, and the evolution of ecological<br>drought in arid regions was mainly influenced by meteorological drought and the scarcity of root soil moisture.<br>This study provides ant approach for quantifying ecological drought severity across natural vegetation areas<br>which can be employed by decision makers|



#### **1. Introduction** 

Global warming and climate change are allegedly increasing the intensities and frequencies of meteorological droughts. Long–term meteorological droughts often lead to a deficit in soil moisture and a drop in groundwater, which affect vegetation growth and poses a severe threat to the ecosystem (Chen et al., 2021; Li et al., 2020; Chang et al., 2016). The increasing severity of ecological degradation due to drought 

is leading to the focus on ecological drought. For example, the Ecological Drought Working Group, established by the Science for Nature and People Partnership (SNAPP) in 2016, defined ecological drought as episodic deficit in available water induced by climate and human factors during the vegetation growth period, which ultimately affects other systems. On this basis, Crausbay et al. (2017) defined ecological drought as an episodic deficit in water availability that drives ecosystems beyond thresholds of resilience into a vulnerable state, impacts ecosystem 

* Corresponding author at: College of Water Resources and Architectural Engineering, Northwest A & F University, Weihui Road 23, Yangling, Shaanxi, China. _E-mail address:_ xiaolingsu@nwafu.edu.cn (X. Su). 

https://doi.org/10.1016/j.ecolind.2021.107804 Received 16 February 2021; Received in revised form 6 May 2021; Accepted 8 May 2021 Available online 4 June 2021 

1470-160X/© 2021 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/). 

_Ecological Indicators 129 (2021) 107804_ 

_T. Jiang et al._ 



**Fig. 1.** A map of Northwestern China showing the spatial distribution of elevation. 

services, and triggers feedbacks in natural and/or human systems. Most recent ecological drought research has been based on the concept proposed by Crausbay (Bradford et al., 2020; Kovach et al., 2019; Li et al., 2018; McEvoy et al., 2018; Raheem et al., 2019; Slette et al., 2019; Vicente-Serrano et al., 2020; Zhang et al., 2019a). However, there remains no widely–accepted drought index to monitor ecological drought. Conventional definitions of drought based on meteorological drought impacts (agricultural, hydrological, and socioeconomic) view drought through a human-centric lens (Crausbay et al., 2017). The corresponding drought indices have been constructed based on precipitation, runoff, soil water storage, evaporative balance, vegetation index, and water–energy ratio to quantify drought from meteorological, hydrological, agricultural, and socioeconomic perspectives (Zhang et al., 2019a; Chang et al., 2019). Although these indices can reflect the hydro–meteorological elements that affect the ecosystem, they are not able to characterize the role of the ecosystem in the drought evolution. For example, various vegetation types show different evapotranspiration rates in the same water–scarce environment (Bradford et al., 2020; Marumbwa et al., 2021). Park et al. (2020) argued that ecological drought should be quantified from an ecosystem perspective, with separate assessments for aquatic and terrestrial ecosystems. 

Previous studies on the effects of ecological droughts on aquatic ecosystems focused on watersheds and wetlands. McEvoy et al. (2018) developed drought regulation measures for five watersheds in the southwestern region of Montana, U.S., through a new ecological drought framework and evaluated drought impacts on the function of riparian habitats and entrainment threats for grayling. Kim et al. (2019) evaluated risk to river water quality induced by ecological drought and estimated the probability of compromise to river water quality exceeding the target thresholds under extreme drought conditions using a nonparametric kernel density method. Based on river ecological flow and minimum flow targets for fish, Park et al. (2020) proposed a method to monitor ecological drought and established an ecological drought indicator to assess the intensity of ecological drought in the Gam River basin, South Korea. Hou et al. (2015) used the minimum ecological water level of a wetland, based on the water balance principle, to construct a drought indicator for ecological drought evaluation in the Hulun wetland, China. 

Previous studies typically used vegetation indices based on remote sensing that have been used to characterize the response of terrestrial 

ecosystem to drought, including temperature vegetation drought index (TVDI) (Yan et al., 2019), normalized difference vegetation index (NDVI) (Nanzad et al., 2019), enhanced vegetation index (EVI) (Roodposhti et al., 2017), vegetation condition index (VCI) (Measho et al., 2019), and vegetation water supply index (VWSI) (Wang et al., 2020). Although these vegetation indices can indirectly reflect the impact of drought on ecology, they do not generally reflect the dynamic changes in the balance between ecological water consumption and water requirements during the drought evolution. There is typically a decline in the vegetation index subsequent to the ecological water deficit persisting for a certain period of time (Marcos et al., 2018). In addition, anomalies in vegetation indices are also influenced by other factors, such as flood, fire, pests, hail, and human activities. Therefore, the use of vegetation indices is not optimal for guiding efficient drought-relief measures and drought risk management. 

Ayantobo and Wei (2019) argued that an appropriate drought index should be capable of determining the duration of drought, identifying drought in real time, delineating drought levels to formulate response measures, and facilitating the study of relationships between different droughts. Similarly, an appropriate ecological drought index should include the aforementioned properties in addition to being able to reflect the imbalance between ecological water consumption and requirement, and should detect abnormalities in the energy balance of the land–air interface due to changes in meteorological and hydrological conditions. Thus, there is a need for the development of an ecological drought index having the above–mentioned characteristics. 

There has been a trend of warming and humidification in Northwestern China (NWRC) since 1961, which has been more notable in the central and western regions (Zhu et al., 2017). For example, the average rate of warming in Gansu province from 1961 to 2015 had been 0.29<sup>◦</sup> C per decade, and precipitation in 2015 exceeded the historical average by 27% (Wen et al., 2017). Meanwhile, the Chinese Government has been implementing the “Grain for Green” program in northern China for over 20 years. This has resulted in an increase in vegetation coverage of the Hexi Corridor by 3.7% per decade since the 2000 (Duan et al., 2011). For example, the vegetated area in the Qilian Mountains increased by 10,779 km<sup>2</sup> from 2000 to 2011 (Deng et al., 2013). The NWRC is a typical ecologically–fragile region in which the underlying surface conditions have changed significantly under climate change and human activities (Xiao and Xiao, 2019). Therefore, a study of the pattern of 

2 

_Ecological Indicators 129 (2021) 107804_ 

_T. Jiang et al._ 

ecological drought in the region can act as a valuable scientific reference for ecological sustainability in the NWRC. 

The main objectives of the current study therefore were to: (1) construct a novel index based on ecological water deficit to capture drought from ecosystem perspectives; (2) evaluate whether the performance of the developed index in detecting the impact of ecological drought on vegetation under different conditions (time scales, wetness, water use efficiency (WUE)) is an improvement over those of other commonly used drought indices; (3) and analyze the spatial–temporal patterns of ecological drought characteristics of the NWRC. 

#### **2. Study area** 

Northwestern China (NWRC; 73<sup>◦</sup> 25<sup>′</sup> –111<sup>◦</sup> 15<sup>′</sup> E, 31<sup>◦</sup> 35<sup>′</sup> –49<sup>◦</sup> 15<sup>′</sup> N) is in northwest Asia, and includes the Xinjiang Uyghur Autonomous Region, the Ningxia Hui Autonomous Region, and the provinces of Qinghai, Gansu, and Shaanxi, with an area of ~3.2 million km<sup>2</sup> , accounting for ~30% of the land area of China (Fig. 1). The climate of the region is largely affected by water vapor from the Indian and the Atlantic Oceans colliding with the Kunlun–Qilian Mountains in the southwest and the Tibetan Plateau, and the Altai Mountains in the north, respectively. The Tienshan Mountain is located in the middle of the region, and contains plateau, an inland basin, and the Gobi. There is an uneven spatial and temporal distribution of precipitation in the NWRC, decreasing from east and west, thereby forming arid, semi–arid, semi–humid, and humid regions (Liu et al., 2021). 

#### **3. Materials and methods** 

#### _3.1. Data sources and preprocessing_ 

The NDVI dataset used in the current study originated from the Global Inventory Modeling and Mapping Studies (GIMMS) group (http://ecocast.arc.nasa.gov/), and has a resolution of 1/12<sup>◦</sup> × 1/12<sup>◦</sup> (~8 km) and a monthly time scale, extending from 1982 to 2015. Land use data at 1 km spatial resolution was extracted from China’s multi–period land use/cover change monitoring dataset (http://www.resdc. cn/). Surface reflectance, temperature, vegetation cover, leaf area index, atmospheric pressure, relative humidity, wind speed, downward shortwave radiation, and longwave radiation were obtained from the ECWMF ERA5 reanalysis dataset (https://cds.climate.copernicus.eu/) with a resolution of 0.1<sup>◦</sup> × 0.1<sup>◦</sup> (~9 km) (Hersbach et al., 2020). The self–calibrated Palmer drought index (scPDSI) series used in the current study was developed by the University of East Anglia Climate Research Centre (Blunden and Arndt, 2019) (https://crudata.uea.ac.uk/) with resolution of 0.5<sup>◦</sup> × 0.5<sup>◦</sup> . Root soil moisture dataset used in the current study was issued by the Global Land Data Assimilation System (GLDAS; https://ldas.gsfc.nasa.gov/gldas) with a resolution of 0.25<sup>◦</sup> × 0.25<sup>◦</sup> . Net Primary Production (NPP) dataset used in the current study originated from the Numerical Terradynamic Simulation Group (NTSG), and was constructed using the global moderate–resolution imaging spectroradiometer (MODIS) NPP algorithm (http://files.ntsg.umt.edu/) with a resolution of 1/12<sup>◦</sup> × 1/12<sup>◦</sup> . Land-use data were obtained from a multiperiod land use/cover remote sensing monitoring dataset in China (http://www.resdc.cn/). The current study used land use data for 1980, 1990, 2000, 2005, 2010, and 2015 seven periods under secondary classification. All spatial datasets were extracted from 1982 to 2015 and resampled onto a resolution of 1/12<sup>◦</sup> × 1/12<sup>◦</sup> using the bilinear interpolation method, which can depict spatial position accuracy and efficiency (Smith, 1981), for consistent spatial resolution and time series length among the six datasets. 

#### _3.2. Construction of ecological drought index_ 

Crausbay et al. (2017) proposed that ecological drought is the phenomenon of a long–term ecosystem water deficit, during which 

vegetation is the primary driver of water consumption. Therefore, the current study used the vegetation water deficit to construct an ecological drought index. 

#### _3.2.1. Ecological water deficit (EWD)_ 

Previous studies (Chi et al., 2018; Feng and Su, 2020) calculated the EWD as the difference between effective precipitation and the ecological water requirement (EWR). However, this approach ignores other sources of water for vegetation growth, such as groundwater. Meanwhile, a consideration of evaporation deficit is more relevant than that of evapotranspiration and precipitation from agronomic and ecological perspectives (Vicente-Serrano et al., 2018). Thus, the present study calculated EWD using Eq. (1) based on the water balance principle: 

#### _EWD_ = _EWC_ − _EWR_ (1) 

In Eq. (1), _EWC_ and _EWR_ are the ecological water consumption and ecological water requirement, respectively. _EWC_ is calculated using the surface energy balance system (SEBS) algorithm, which aims to derive the actual evaporation using latent heat fluxes based on the energy balance theory. PySEBS is a widely used Python package suitable for the calculation of evapotranspiration under different scenarios, and was developed by Kwast and De Jong (2004) based on the results of Su (2002). The PySEBS packages includes sub–models to derive the energy balance, the heat transfer coefficient, and the stability coefficient. 

EWR represents the amount of water required to maintain the function and health of the ecosystem (Deb et al., 2019), and is equivalent to vegetation evapotranspiration under the ideal condition with no stresses associated with supply of water, pests, and salinity. EWR was calculated using the single crop coefficient method, called the FAO–56 (Allen et al., 1998), as recommended by the Food and Agriculture Organization (FAO) of the United Nations. This method has been extended to estimate the EWR of herbaceous and woody plants (Zhang et al., 2010; Chi et al., 2018). 



In Eq. (2), _Kc_ is the vegetation coefficient of different growth stages, and is categorized into four stages, namely the initial, development, mid-season, and the end of the late season stages. _ET0_ is the reference crop evapotranspiration, calculated by the Penman–Monteith formula. 

The growth period of natural vegetation in the NWRC generally ranges from April to October (Wang et al., 2006). However, the NWRC has a large spatial span with apparent spatial heterogeneity of vegetation growth period. For example, the mid-season growth stage of grass in southeastern NWRC extends from May to August, whereas it extends from June to September in the northwestern part of the NWRC. Therefore, the use of a uniform vegetation growth stage classification for the NWRC will result in large deviations in the calculated EWD. A previous study found that NDVI reach a maximum at the mid-season stage (Chen et al., 2018). The current study therefore proposed a method to classify growth stages using the NDVI. Under this approach, the average NDVI at a grid–scale from January to December during 1982–2015 was calculated and sorted, and the mid-season stage was regarded as the period corresponding to the maximum NDVI and adjacent months. The development and the end of the late season stages were then taken to be previous one months and follow two months after the mid-season stage, respectively, whereas the remaining months were calculated as the initial stage. For example, if the maximum NDVI occurred in June, the mid-season stage comprised May, June, and July, the development stage comprised March and April, the end of the late season stage comprised August and September, and the remaining months were calculated as the initial stage. Fig. S2 shows the distribution of months corresponding to the maximum NDVI. The vegetation coefficients for different growth stages were calculated as follows: 



3 

_Ecological Indicators 129 (2021) 107804_ 

_T. Jiang et al._ 



**Fig. 2.** Spatio–temporal distribution EWD in the NWRC during four periods (1982–1990, 1991–2000, 2001–2010 and 2011–2015. White space indicates the areas without vegetation). 







In Eqs. (3)–(8), _Kc,_ ini(~10) is the vegetation coefficient at the initial stage during which infiltration depth is _<_ 10 mm and is obtained using Fig. 29 in the FAO–56 handbook (Allen et al., 1998), _Kc,_ min is the minimum vegetation coefficient under a condition of the lowest vegetation cover at the corresponding stage (0.15 _< Kc,_ min _<_ 0.20), _Kc,_ full is the vegetation coefficient under the entirely covered condition, _h_ is the vegetation height, _fp_ is the actual vegetation coverage (0.01 _< fp <_ 1) calculated using remote-sensed NDVI, _f_ peff is the effective vegetation coverage (0.01 _< f_ peff _<_ 1), sin( _η_ ) is the sine of the mean solar angle, and _NDVI_ min and _NDVI_ max represent the minimum and the maximum NDVI of each grid in each year during the study period, respectively. 

#### _3.2.2. Standardized ecological water deficit index (SEWDI)_ 

A new series ( _x2i_ ) at each grid was obtained by normalizing the time series ( _x1i_ ) of EWD using Eq. (9). The values of 1 and 0 in _x2i_ were replaced by 0.999 and 0.001, respectively for facilitating the fitting of distribution functions. 



The gamma, log–logistic, and P–III distribution functions were then chosen to fit the series normalized above to obtain the probability density function ( _fx_ 2 _i_ ( _t_ )) and evaluated using the Akaike information criterion (AIC) (Akaike, 1998). The cumulative probability ( _Fx_ 2 _i_ ( _t_ )) of EWD was then calculated using the density function that showed the best performance: 



Finally, the inverse standardization method was used to obtain the standardized ecological water deficit index (SEWDI).: 



#### _3.3. Standardized NDVI (SNDVI)_ 

Vegetation indices are commonly used to describe land cover and classify the characteristics of vegetation (Zhang et al., 2020). Among them, the NDVI has the broadest applicability in analyzing the response of ecosystem to droughts. However, the vegetation coverage affects the correlation between drought indices and NDVI. For example, Zhang et al. (2019b), Ding et al. (2020), and Fang et al. (2019) determined that the maximum correlation coefficient between different drought indices and NDVI was statistically insignificant in regions with sparse vegetation. In addition, strong seasonality and regionality of changes in vegetation result in the NDVI being insensitive to the change in drought index (Fabricante et al., 2009; Fang et al., 2019). The standardization method used reflects the deviation of each index from the intermediate state at each grid, which can eliminate the seasonal and regional influence (Zang et al., 2020). Therefore, the standardized NDVI (SNDVI) values were obtained by transforming the NDVI series to standardized units following the same approach as used for SEWDI, facilitating a direct comparison with drought indices mentioned above. 

#### _3.4. Applicability of SEWDI for monitoring ecological drought_ 

By referencing the applicability assessment method used for the agricultural drought index (Anderson et al., 2016), the present study considered SNDVI as the criterion for evaluating the performance of SEWDI against four widely used drought indicators, including SPI, SPEI, SSI, and scPDSI, which represent different aspects that directly affect vegetation growth. Among them, SPI, SPEI and SSI were calculated by standardizing precipitation, the difference between precipitation and potential evapotranspiration, and soil moisture in the root zone, respectively. The values of correlation coefficient (r) between SNDVI and the assessed drought indices under different time scales, wetness index (WI = Precipitation/Potential Evapotranspiration), and vegetation water use efficiency (WUE = NPP/Evapotranspiration) were then compared. 

#### _3.5. Characteristics of ecological drought in the NWRC_ 

The rotated empirical orthogonal function (REOF) is constructed by rotating the pattern of the empirical orthogonal function (EOF), and appears to be the most widely used method for the spatio–temporal 

4 

_Ecological Indicators 129 (2021) 107804_ 

_T. Jiang et al._ 



**Fig. 3.** Distribution of 12–month–scale SEWDI in the NWRC during four periods, 1982–1990, 1991–2000, 2001–2010, and 2011–2015. 

analysis of drought (Liu et al., 2016). The present study used REOF to decompose 12–month SEWDI during 1982–2015, which allowed the clustering of grids with similar trends of ecological drought intensity in the same region, thereby facilitating the analysis of annual ecological drought characteristics in different parts of the NWRC. Hannachi et al. (2007) provides more details on the procedure used for the REOF calculation. The ecological drought characteristics of each division, including severity, duration, and frequency, were separately extracted using run theory. Identifying drought events using run theory required two conditions (Ma et al., 2019): 1) the drought intensity should fall below a given threshold; 2) two drought events separated by one month in which the drought intensity in studied month remained negative were merged into one event. The current study selected − 1 and − 1.5 as the thresholds for identifying moderate and severe ecological drought, representing the probability distribution scenarios in which SEWDI falls below the threshold of 10% and 5%, respectively. The Morlet wavelet was used to analyze the return periods of different types of drought, and consisting of a plane wave modulated by a Gaussian function: 

_ψ_ ( _η_ ) = _π_<sup>(−1</sup><sup>_/_4)</sup> e<sup>_iwη_−</sup><sup>_η_2</sup><sup>_/_2</sup> (12) 

In Eq. (12), _η_ is the dimensionless time parameter and _ω_ is the dimensionless frequency. 

#### **4. Results** 

#### _4.1. Distributions of EWD_ 

The EWD was generally higher in the west–central regions and lower in the southeastern regions of the NWRC (Fig. 2). The spatial distribution of the EWC in the NWRC could be divided into four categories: 1) regions showed relatively higher EWD, including the Qilian Mountains, the Kunlun Plateau, and other areas with relatively higher altitude and low EWR and EWC (Fig. S3 shows the spatial distribution of EWR and EWC); 2) regions with the highest EWD located in the desert areas of the NWRC, such as the Tarim, the Qaidam, and the Turpan basin, and the Hexi Corridor, which had high EWR and extremely low EWC; 3) regions with large fluctuations in EWD which were mainly located in the plateau of southern Qinghai, characterized by high EWR and EWC that was sensitive to climate change; 4) regions with no EWD which were distributed in the southern Qinling Mountains, characterized by low 



**Fig. 4.** The first four eigenvectors of REOF of SEWDI–12 in the NWRC (SE, SW, NW, NE, and CT represent southeastern sub–region, southwestern sub–region, northwestern sub–region, northeastern sub–region and central sub–region, respectively.) 

5 

_Ecological Indicators 129 (2021) 107804_ 

_T. Jiang et al._ 



**Fig. 5.** Pearson correlation coefficients representing the correlations between scPDSI, SPEI, SPI, SSI, and SEWDI with SNDVI over time scales of 1 to 48 months within five subregions of the NWRC during 1982–2015. 

EWR and abundant available water resources. Temporal variability in EWD manifested as decreases in southern Qinghai, southern Ningxia, and most of Shaanxi and increases in the Qilian Mountains, the Hexi Corridor, and the Qaidam Basin since the start of the 21st century, whereas there were little changes in EWD in the remaining regions of the NWRC. 

#### _4.2. Ecological drought divisions_ 

As shown in Fig. 3, the 12–month scale SEWDI for 1982–2015 was calculated to clearly show the geographical characteristic of ecological drought. Empirical orthogonal decomposition (EOF) was then conducted on 97,128 pixels among the NWRC, and results showed that the contribution of the ten largest eigenvectors to cumulative variance could reach up to 67% (Table S1). Finally, the first ten eigenvectors were rotated orthogonally to obtain a more uniform variance contribution (Table S1), concentrating on the relevant distributed feature in a relatively small area. The first four spatial modes were extracted to characterize the spatio–temporal variation of ecological drought in the NWRC, and ecological drought was separated into five categories (Fig. 4). In the first spatial mode, the large eigenvalues accounted for 13.3% of the total variance, and this model represented areas mainly distributed in the middle temperate and warm temperate regions, such as the Turpan basin, the Tarim and the Qaidam basin, the plateau in eastern Gansu, the basin in central Shaanxi, the Hexi corridor, and the Qilian mountains, indicating that the changes in ecological drought in these regions were more sensitive to the cumulative temperature. Within the second spatial mode, the large eigenvalues were mainly 

concentrated in the high–altitude areas of the northern NWRC, including the northern Kunlun Mountains and the plateau of southern Qinghai, indicating that the changes in ecological drought in these regions were sensitive to the interactions between the plateau thermal condition and the East Asian subtropical monsoon (Feng et al., 2020). The higher eigenvalues of the third spatial mode were mainly located in the arid regions of the NWRC with higher vegetation cover, including the Yili basin and the Altai mountains. The fourth spatial mode contained low eigenvalues in arid areas such as the Hexi corridor, the Turpan basin, the Tarim basin, and in semi–arid regions such as the Eastern Qilian Mountains, whereas this mode contained large eigenvalues in the humid southern Shaanxi and semi–humid central Shaanxi regions, indicating that the changes in ecological drought were sensitive to moisture. Southeastern sub–region (SE), northeastern sub–region (NE) and central subregion (CT) were categorized based on the first and the fourth spatial mode. SE represented humid areas of the NWRC with large eigenvalues and was placed in the fourth spatial mode, with dominant vegetation of this region constituting evergreen deciduous and broad–leaved mixed forests. NE of the NWRC represented the semi–humid area with large eigenvalues categorized into first spatial mode, with grassland being the dominant vegetation type. SW and northwestern sub–region (NW) both contained large eigenvalues and fell in second and third spatial modes, respectively. Dominant in the southwestern sub–region (SW) was alpine grassland, whereas that of NW was grass and coniferous forest. The remaining parts fell within central sub–region (CT), characterized as desert area in the arid region of the mesothermal temperate zone in which the primary vegetation was desert grassland. 

6 

_Ecological Indicators 129 (2021) 107804_ 

_T. Jiang et al._ 



**Fig. 6.** A plot of wetness index (WI) versus r representing the correlations between SEWDI, SSI, SPEI, SPI, and scPDSI with SNDVI in the NWRC at a 12–month time scale. The black line is the linear regression curve. K indicates the slope of the regression curve. R<sup>2</sup> is the goodness–of–fit, which was significant at P _<_ 0.05). 

_4.3. Applicability of SEWDI compared with commonly used drought indices_ 

Long–term changes in vegetation are mainly driven by prolonged 

drought, differences in moisture between different areas and the WUE of vegetation (Lin et al., 2020). Therefore, the present study compared the correlations between different drought indices and SNDVI under different timescales, WI, and WUE to evaluate their performances for 



**Fig. 7.** A plot of water use efficiency (WUE) versus r representing the correlations between SEWDI, SSI, SPEI, SPI, and scPDSI with SNDVI in the NWRC at a 12–month time scale. (The black line is the linear regression curve. K indicates the slope of the regression curve. R<sup>2</sup> is goodness–of–fit.) 

7 

_Ecological Indicators 129 (2021) 107804_ 

_T. Jiang et al._ 



**Fig. 8.** Time series of monthly SEWDI at different time scales (1–48 months) in the NWRC and five subregions (1982–2015). 

monitoring ecological drought. 

#### _4.3.1. Applicability under different time scales_ 

The accumulation of EWD may result in the large-scale degradation of vegetation over a certain period of time (Chi et al., 2018; Zhou et al., 2020). Thus, the Pearson correlation coefficients between SEWDI, SPI, SPEI, SSI, and scPDSI with SNDVI in the five divisions at 1– to 48– month time scales from 1982 to 2015 were calculated (Fig. 5). The wetness index of SE and NE were larger than those of other sub–regions, at 0.81 and 0.54, respectively, and the ranking of drought indices according to their correlations to SNDVI under different time scales was SEWDI _>_ SPEI _>_ SSI _>_ SPI _>_ scPDSI. The correlation between SEWDI, SPEI, SSI and SPI with SNDVI increased with increasing time scale, indicating that changes in vegetation in humid regions was affected by long-term water scarcity. The ranking of drought indices in SW, NW, and CT according to their correlations with SNDVI was SEWDI _>_ scPDSI _>_ SSI _>_ SPI _>_ SPEI, with average WIs of 0.31, 0.23, and 0.18, respectively. The correlation of SEWDI–SNDVI, SPEI–SNDVI, SSI–SNDVI and SPI–SNDVI shifted from increase to decrease with increasing time scales, indicating that the vegetation in arid regions was more sensitive to drought than in humid regions. Additionally, a larger correlation between each index and SNDVI at a longer time scale, indicating that the change of vegetation is driven by long-term water deficit. Ecological drought can therefore be more rapidly detected by the 

monitoring of vegetation in arid regions as compared to the SNDVI. As shown in Fig. 5, SEWDI represented factors resulting in changes to vegetation over most time scales in the five regions. However, scPDSI showed the highest correlation with SNDVI over short time scales ( _<_ 8 months), especially in the humid region (SE), indicating that scPDSI was more representative of short–term ecological drought. 

#### _4.3.2. Applicability of drought indices under the influence of wetness_ 

A multitude of studies (Ayantobo and Wei, 2019; Zhang et al., 2015) have shown that the applicability of drought indices for monitoring drought is susceptible to wetness. The current study calculated the correlation between the commonly-used drought indices and SNDVI at a 12–month scale under different degrees of wetness. Results showed that the average r values for the correlation between SEWDI with SNDVI exceeded those for the remaining four drought indices. Both SEWDI and scPDSI were insensitive to changes in wetness within their relationships with SNDVI. The average r values representing the correlation between SPI and SSI with SNDVI were higher in water–limited regions with low moisture than that with SPEI, with this result being opposite to that in energy–limited regions with high moisture (Fig. 6). 

_4.3.3. Applicability of drought indices under the influence of water use efficiency_ 

One of the main reasons for the difference in resistance to drought 

8 

_Ecological Indicators 129 (2021) 107804_ 

_T. Jiang et al._ 







**Fig. 9.** Box plots showing ecological drought characteristics based on 3–month and 12–month SEWDI using thresholds of SEWDI _<_ − 1 for the five subregions of the NWRC (The red line in each box represent the median value. The red point is average value). (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.) 

NWRC entered the wet period from 2010 to 2015, characterized by relatively high SEWDI. 

#### _4.4.2. Severity, duration, times of ecological drought_ 

The ecological drought events of each region were extracted based on the SEDWI thresholds of –1 and –1.5, and were characterized by severity, duration, and the number of drought events (Fig. 9, Fig. S4). The drought start and end times of each region were mainly concentrated in the vegetation growth period from April to October, during which both EWR and EWD were large. The earliest start time and end time of ecological drought at a 3–month scale started in CT (6.50) and SE (6.57), whereas the latest started in SW (6.87) and ended in NE (6.95), respectively. By comparison, the earliest average start time and end time of ecological drought at a 12–month time scale started in CT (6.19) and ended in SE (6.26), whereas the latest started (6.87) and ended (6.67) both in NE, respectively. The duration of ecological drought increased with increasing cumulative period and decreasing threshold, and the regions could be ordered according to the duration of ecological drought as SE _<_ NE _<_ SW _<_ NW _<_ CT. The severity of the ecological drought was correspondingly greater at longer time scales and lower threshold in the order of CT _<_ SW _<_ NE _<_ SE _<_ NW. The number of ecological drought events decreased with increasing time scales and decreasing thresholds, and the regions were ranked in terms of number of ecological drought events as NW _<_ SW _<_ CT _<_ NE _<_ SE. In general, the ecological drought events in SE of the NWRC were of greater intensity, higher frequency, earlier start time and shorter duration. Ecological drought events in SW were of less intensity, of lower frequency, had a later start time, and were more prolonged. Ecological drought events in NW were characterized by greater intensity, lower frequency, and longer duration. The characteristics of ecological drought in NE were of greater intensity, higher frequency, had later start time and shorter duration. Lastly, ecological drought events in CT were of less intensity, lower frequency, earlier start time, and more prolonged duration. 

#### _4.4.3. Return periods comparison between different types of drought_ 

among different types of vegetation is the difference in their WUE (Liu et al., 2020, 2016). For example, vegetation in the southeastern NWRC has been shown to be insensitive to drought at the short time scales compared to other regions due to its higher WUE (Liu et al., 2015; Zhang et al., 2019a). Similarly, results of the present study showed that the correlations between the drought indices and SNDVI decreased with increasing WUE. This trend was especially obvious for SPI and SSI, which are single–element drought indices and reflect single factors affecting changes in vegetation. Of note was the finding that the average r value of the correlation between SEWDI with SNDVI was consistently high under different WUEs (Fig. 7), suggesting that SEWDI can better characterize the ecological drought without being influenced by WUE. 

#### _4.4. Ecological drought characteristics_ 

#### _4.4.1. Drought intensity at different time scales_ 

Fig. 8 shows the average SEWDI distribution in the NWRC and five regions at timescales of 1 to 48 months during 1982–2015. The time series of SEWDI became smother with an increasing time scale, with more prolonged dry and wet periods. More intensive ecological drought periods in the NWRC were mainly concentrated in 1982–1986, 1990–1996, and 2005–2010, occurring in SE, SW, and CT, SW and NE, and NW, NE, and CT, respectively. Regions such as SE and NE with higher WI experienced higher fluctuation of ecological drought intensity with more pronounced interannual and interdecadal variation. In contrast, SW, NW, and CT of the NWRC with lower WI experienced oscillations in ecological drought at lower frequencies. It is worth noting that SW experienced only one apparent oscillation cycle. Although the precipitation in the NWRC has increased since the 21st century, the rise in NDVI and temperature intensified EWD in SE, SW, and CT, and resulted in the intensification of ecological drought. Each region of the 

Wavelet analysis was conducted to obtain the return periods of different types of drought, with the results showing that the first major periods of SEWDI, SPEI, SPI, SSI, and scPDSI in the NWRC were 9, 4, 9, 31 and 8 years, respectively, corresponding to the peaks of wavelet variance (Fig. 10). More specifically, the return periods of ecological drought in the SW, NW and CT, representing arid regions with the first major period exceeding 15 years, were longer than those in the humid SE and NE. SEWDI in the desert-dominated NW and CT showed a similar waveform to those of SPI and SPEI, indicating that the ecological drought in these regions was more likely to be driven by meteorological drought. Similarly, the changes in ecological drought in the SW were largely driven by soil moisture. However, the waveform of SEWDI in humid regions differed significantly from those of other drought indices. This phenomenon in the SE was particularly obvious due to the complex relationship between water resources and vegetation growth in this region. 

#### **5. Discussion** 

_5.1. Reasons for the good performance of the SEWDI in characterizing ecological drought_ 

Monitoring of ecological drought in previous studies has remained in an exploratory stage and has mainly involved the use of three types of indices. The first type is the single–element drought index, such as the surface water supply index (SWSI) based on snowpack or runoff (Wambua, 2019), SPI based on precipitation (Vicente-Serrano et al., 2012), and the reclamation drought index (RDI) based on the ratio of precipitation to evaporation (Shah et al., 2013). The drought indices falling under this type reflect the influence of only a single factor on changes in vegetation. The second type of drought index encompasses 

9 

_Ecological Indicators 129 (2021) 107804_ 

_T. Jiang et al._ 



**Fig. 10.** Annual wavelet variance of SEWDI, SSI, SPEI, SPI, and scPDSI in the NWRC and its five sub–regions. 

the vegetation indices which are used to characterize the response of vegetation to drought, including the NDVI (Nanzad et al., 2019), the VCI (Measho et al., 2019), the EVI (Roodposhti et al., 2017), and so on. However, the vegetation indices show limited practical use within real–time drought monitoring and regulation of water resources. The third type of drought indices are comprehensive drought indices, and are constructed by combining two or more elements to characterize the integrated effects of drought, including TVDI (Wang et al., 2004), representing the integration of meteorological elements with vegetation elements, PDSI and the standardized moisture anomaly index SZI (Zhang et al., 2019a), which reflect multiple balances in the hydrological processes, and SWI (Liu et al., 2017), which combine climate with land surface change. However, this type of drought index ignores the role of vegetation in the water cycle. Vegetation not only reduces soil erosion by retaining regional precipitation, but also regulates the evapotranspiration of the region (Ma et al., 2019). Therefore, the balance between EWR and EWC changes with the change of meteorological, hydrological, and vegetation conditions. Higher vegetation cover in energy–rich regions can result in vegetation “pumping” more water from the soil, whereas energy–limited regions are less influenced by the amount of vegetation (Kim and Rhee, 2016). By considering the net radiation as the energy supply for vegetation evapotranspiration and water consumption as the actual amount of water “pumped” by vegetation, the desert areas and the Hexi Corridor in the NWRC are energy–rich and water–limited regions. In contrast, Southern Shaanxi is a 

water–rich and energy–limited region. Therefore, the level of ecological drought is a factor of different combinations of the balance between water and energy. The SEWDI ecological drought index proposed in the current study was constructed by focusing on vegetation, which considers the climatic and hydrological elements of vegetation growth and reflects the dynamics of the energy balance and water balance, respectively. Results of the present study demonstrated a good performance of the SEWDI under different timescales, degrees of wetness, and water use efficiencies. Meanwhile, the standardized method used in the present study reflected the multi–temporal scale characteristics of ecological drought, which could be easily combined with other standardized drought indices to study their relationships with different types of drought. Therefore, SEWDI is an effective index for monitoring of ecological drought. 

_5.2. Possible approaches to further improving the performance of SEWDI in the monitoring of ecological drought_ 

SEWDI is a standardized drought index, reflecting a relative water–scarce degree over a certain period. It is obtained through fitting a probability distribution function to the EWD time series at each grid, after which it is standardized through an inverse function. Thus, although SE showed a greater drought intensity (Fig. 9d), it did not actually experience water scarcity during 1982–2015 (Fig. 3). Similarly, CT experienced a relatively low drought intensity, but was nevertheless 

10 

_Ecological Indicators 129 (2021) 107804_ 

_T. Jiang et al._ 

the most water–scarce region among the five regions. This result could be attributed to the presence of a slight variation in EWD during 1982–2015, resulting in a relatively low peak in the probability distribution, and a relatively flat cumulative distribution curve. This phenomenon is common to standardized drought indices (Zang et al., 2020), as a drought is different from the dryness in that drought characterizes the extent to which water deficits deviating from normal levels, thereby allowing the spatial comparison between droughts. Therefore, extending the time series is necessary to obtain a more objective normal drought level. In addition, EWR and EWC are two critical factors required for calculating EWD, where EWC can be simulated at a field scale using experimental models, following which it is inverted at a large spatial scale using remote sensing data (Granata, 2019). However, few studies have focused on the method used to calculate EWR, particularly at large spatio–temporal scales in which considerable heterogeneity in the vegetation growth stages and vegetation types exists. Therefore, the classification of vegetation growth stage based on the different types of vegetation could improve the accuracy of EWR, which is another critical element required to further improve the capacity to monitor SEWDI. 

#### **6. Conclusion** 

The newly proposed concept of ecological drought could effectively guide vegetation conservation and management. However, there remains no widely accepted approach for monitoring ecological drought. Therefore, the current study constructed the ecological drought index (SEWDI) using a time series of EWD and applied the index to the NWRC. Some main conclusions of the current study are listed below. 

- (1) The SEWDI was shown to have a better performance in characterizing ecological drought at different time compared to other drought indices in both arid and humid areas. SEWDI at a 12–month scale was largely unaffected by WI and vegetation WUE. The ability of SEWDI to monitor ecological drought can be further improved by extending the time series of data used and enhancing the EWR calculation method. 

- (2) Among the widely used drought indices assessed, SPI and SSI performed well in monitoring the trends in ecological drought in water–limited (arid) regions. Simultaneously, the capability of SPEI increased in energy–limited (humid) regions, and scPDSI was shown to perform well in monitoring ecological drought at short time scales. The correlation of SPI, SPEI, SSI, and scPDSI with SNDVI decreased with the increase of vegetation WUE. 

- (3) Severe ecological droughts occurred more frequently in the SE, SW, and CT regions of the NWRC during 1982–1986, in SW and NE during 1990–1996, and in NW, NE, and CT during 2005–2010. The return periods of ecological drought in the arid NW, CT and SW exceeded those in the humid SE and NE. The ecological drought in the NWRC overall exhibited an overall wetting trend after 2010, especially in the humid SE and NE. 

The ecological drought index proposed in the current study effectively identified ecological drought in the terrestrial ecosystem of the NWRC. The impact of climate change and human activities has resulted in more frequent and more severe drought events since the 21st century. Therefore, there is potential for the future application of the SEWDI to similar regions globally for analyzing and predicting the impact of drought on ecosystems. 

#### **CRediT authorship contribution statement** 

**Tianliang Jiang:** Methodology, Writing - original draft, Visualization, Software. **Xiaoling Su:** Conceptualization, Investigation, Funding acquisition, Supervision. **Vijay P. Singh:** Writing - review & editing, Conceptualization. **Gengxi Zhang:** Writing - review & editing, Validation. 

#### **Declaration of Competing Interest** 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

#### **Acknowledgement** 

We are grateful for the support from the National Natural Science Foundation of China (Grants 52079111; 51879222; 91425302). 

#### **Appendix A. Supplementary data** 

Supplementary data to this article can be found online at https://doi. org/10.1016/j.ecolind.2021.107804. 

#### **References** 

- Akaike, H., 1998. Information theory and an extension of the maximum likelihood principle. In: Selected Papers of Hirotugu Akaike. Springer, pp. 199–213. 

- Allen, R.G., Pereira, L.S., Raes, D., Smith, M., 1998. Crop Evapotranspiration-Guidelines for Computing Crop Water Requirements-FAO Irrigation and Drainage Paper 56. Fao, Rome 300, D05109. 

- Anderson, M.C., Zolin, C.A., Sentelhas, P.C., Hain, C.R., Semmens, K., Tugrul Yilmaz, M., Gao, F., Otkin, J.A., Tetrault, R., 2016. The Evaporative Stress Index as an indicator of agricultural drought in Brazil: an assessment based on crop yield impacts. Remote Sens. Environ. 174, 82–99. 

- Ayantobo, O.O., Wei, J., 2019. Appraising regional multi-category and multi-scalar drought monitoring using standardized moisture anomaly index (SZI): a waterenergy balance approach. J. Hydrol. 579, 124139. https://doi.org/10.1016/j. jhydrol.2019.124139. 

- Blunden, J., Arndt, D.S., 2019. State of the Climate in 2018. Bull. Am. Meteorol. Soc. 100, Si-S306. 

- Bradford, J.B., Schlaepfer, D.R., Lauenroth, W.K., Palmquist, K.A., 2020. Robust ecological drought projections for drylands in the 21st century. Glob. Change Biol. 26 (7), 3906–3919. 

- Chang, J., Li, Y., Wang, Y., Yuan, M., 2016. Copula-based drought risk assessment combined with an integrated index in the Wei River Basin, China. J. Hydrol. 540, 824–834. 

- Chang, J., Guo, A., Wang, Y., Ha, Y., Zhang, R., Xue, L.u., Tu, Z., 2019. Reservoir operations to mitigate drought effects with a hedging policy triggered by the drought prevention limiting water level. Water Resour. Res. 55 (2), 904–922. 

- Chen, C., He, B., Guo, L., Zhang, Y., Xie, X., Chen, Z., 2018. Identifying Critical Climate Periods for Vegetation Growth in the Northern Hemisphere. J. Geophys. Res. Biogeosci. 123 (8), 2541–2552. 

- Chen, S., Huang, Y., Wang, G., 2021. Detecting drought-induced GPP spatiotemporal variabilities with sun-induced chlorophyll fluorescence during the 2009/2010 droughts in China. Ecol. Ind. 121, 107092. https://doi.org/10.1016/j. ecolind.2020.107092. 

- Chi, D., Wang, H., Li, X., Liu, H., Li, X., 2018. Estimation of the ecological water requirement for natural vegetation in the Ergune River basin in Northeastern China from 2001 to 2014. Ecol. Ind. 92, 141–150. 

- Crausbay, S.D., Ramirez, A.R., Carter, S.L., Cross, M.S., Hall, K.R., Bathke, D.J., Betancourt, J.L., Colt, S., Cravens, A.E., Dalton, M.S., 2017. Defining ecological drought for the twenty-first century. Bull. Am. Meteorol. Soc. 98, 2543–2550. 

- Deb, P., Kiem, A.S., Willgoose, G., 2019. A linked surface water-groundwater modelling approach to more realistically simulate rainfall-runoff non-stationarity in semi-arid regions. J. Hydrol. 575, 273–291. 

- Deng, S.-f., Yang, T.-B., Zeng, B., Zhu, X.-F., Xu, H.-J., 2013. Vegetation cover variation in the Qilian Mountains and its response to climate change in 2000–2011. J. Mount. Sci. 10 (6), 1050–1062. 

- Ding, Y., Xu, J., Wang, X., Peng, X., Cai, H., 2020. Spatial and temporal effects of drought on Chinese vegetation under different coverage levels. Sci. Total Environ. 716, 137166. https://doi.org/10.1016/j.scitotenv.2020.137166. 

- Duan, H., Wang, T., Wen, X., Xue, X., Guo, J., 2011. Spatial-temporal variations of NDVI and their relationship with different land use types in Hexi region from 1999 to 2009. In: 2011 International Conference on Remote Sensing, Environment and Transportation Engineering. IEEE, pp. 1590–1593. 

- Fabricante, I., Oesterheld, M., Paruelo, J.M., 2009. Annual and seasonal variation of NDVI explained by current and previous precipitation across Northern Patagonia. J. Arid Environ. 73 (8), 745–753. 

- Fang, W., Huang, S., Huang, Q., Huang, G., Wang, H., Leng, G., Wang, L.u., Li, P., Ma, L., 2019. Bivariate probabilistic quantification of drought impacts on terrestrial vegetation dynamics in mainland China, 123980 J. Hydrol. 577. https://doi.org/ 10.1016/j.jhydrol.2019.123980. 

- Feng, K., Su, X., 2020. Spatiotemporal response characteristics of agricultural drought to meteorological drought from a three-dimensional perspective. Trans. Chine. Soc. Agric. Eng. 36, 103–113. 

- Feng, W., Lu, H., Yao, T., Yu, Q., 2020. Drought characteristics and its elevation dependence in the Qinghai-Tibet plateau during the last half-century. Sci. Rep. 10, 14323. 

11 

_Ecological Indicators 129 (2021) 107804_ 

_T. Jiang et al._ 

Granata, F., 2019. Evapotranspiration evaluation models based on machine learning algorithms—a comparative study. Agric. Water Manag. 217, 303–315. 

Hannachi, A., Jolliffe, I., Stephenson, D., 2007. Empirical orthogonal functions and 

related techniques in atmospheric science: a review. Int. J. Climatol.: J. R. Meteorol. Soc. 27, 1119–1152. 

- Hersbach, H., Bell, B., Berrisford, P., Hirahara, S., Horanyi, A., Mu´ noz-Sabater, J., ˜ Nicolas, J., Peubey, C., Radu, R., Schepers, D., 2020. The ERA5 global reanalysis. Q. J. R. Meteorolog. Soc. 146, 1999–2049. 

- Hou, J., Liu, X., Yan, D., Weng, B., Yuan, Y., 2015. Hulun lake ecological drought evaluate. Water Conservancy Hydropower Technol. 46, 22–25. 

- Kim, D., Rhee, J., 2016. A drought index based on actual evapotranspiration from the Bouchet hypothesis. Geophys. Res. Lett. 43 (19), 10,277–10,285. 

- Kim, J.-S., Jain, S., Lee, J.-H., Chen, H., Park, S.-Y., 2019. Quantitative vulnerability assessment of water quality to extreme drought in a changing climate. Ecol. Ind. 103, 688–697. 

- Kovach, R.P., Dunham, J.B., Al-Chokhachy, R., Snyder, C.D., Letcher, B.H., Young, J.A., Beever, E.A., Pederson, G.T., Lynch, A.J., Hitt, N.P., 2019. An integrated framework for ecological drought across riverscapes of North America. BioScience 69, 418–431. 

- Kwast, J., De Jong, S., 2004. Modelling Evapotranspiration using the Surface Energy Balance Systems (sebs) and landsat tm data (rabat region, morocco). European association of remote sensing laboratories. 

- Li, C., Leal Filho, W., Yin, J., Hu, R., Wang, J., Yang, C., Yin, S., Bao, Y., Ayal, D.Y., 2018. Assessing vegetation response to multi-time-scale drought across inner Mongolia plateau. J. Cleaner Prod. 179, 210–216. 

- Li, J., Zhang, S., Huang, L., Zhang, T., Feng, P., 2020. Drought prediction models driven by meteorological and remote sensing data in Guanzhong Area, China. Hydrol. Res. 51, 942–958. 

- Lin, S., Wang, G., Hu, Z., Huang, K., Sun, J., Sun, X., 2020. Spatiotemporal variability and driving factors of Tibetan plateau water use efficiency. J. Geophys. Res.: Atmos. 125 e2020JD032642. 

- Liu, H., Jia, J., Lin, Z., Wang, Z., Gong, H., 2021. Relationship between net primary production and climate change in different vegetation zones based on EEMD detrending – a case study of Northwest China. Ecol. Ind. 122, 107276. https://doi. org/10.1016/j.ecolind.2020.107276. 

- Liu, M., Xu, X., Xu, C., Sun, A.Y., Wang, K., Scanlon, B.R., Zhang, L., 2017. A new drought index that considers the joint effects of climate and land surface change. Water Resour. Res. 53 (4), 3262–3278. 

- Liu, X., Cui, Y., Wu, Z., Zhao, Y., Hu, X., Bi, Q., Yang, S., Wang, L., 2020. Transcriptome and co-expression network analyses identify the molecular signatures underlying drought resistance in Yellowhorn. Forests 11 (8), 840. https://doi.org/10.3390/ f11080840. 

- Liu, Y., Xiao, J., Ju, W., Zhou, Y., Wang, S., Wu, X., 2015. Water use efficiency of China’s terrestrial ecosystems and responses to drought. Sci. Rep. 5, 13799. 

- Liu, Z., Menzel, L., Dong, C., Fang, R., 2016. Temporal dynamics and spatial patterns of drought and the relation to ENSO: a case study in Northwest China. Int. J. Climatol. 36 (8), 2886–2898. 

- Ma, Z., Yan, N., Wu, B., Stein, A., Zhu, W., Zeng, H., 2019. Variation in actual 

   - evapotranspiration following changes in climate and vegetation cover during an ecological restoration period (2000–2015) in the Loess Plateau, China. Sci. Total Environ. 689, 534–545. 

- Marcos, F.C.C., Silveira, N.M., Mokochinski, Joao.B., Sawaya, A.C.H.F., Marchiori, P.E. ˜ R., Machado, E.C., Souza, G.M., Landell, M.G.A., Ribeiro, R.V., 2018. Drought tolerance of sugarcane is improved by previous exposure to water deficit. J. Plant. Physiol. 223, 9–18. 

- Marumbwa, F.M., Cho, M.A., Chirwa, P.W., 2021. Geospatial analysis of meteorological drought impact on Southern Africa biomes. Int. J. Remote Sens. 42 (6), 2155–2173. 

- McEvoy, J., Bathke, D.J., Burkardt, N., Cravens, A.E., Haigh, T., Hall, K.R., Hayes, M.J., Jedd, T., Podˇebradska, M., Wickham, E., 2018. Ecological Drought: accounting for ´ the non-human impacts of water shortage in the Upper Missouri Headwaters Basin, Montana, USA. Resources 7 (1), 14. https://doi.org/10.3390/resources7010014. 

- Measho, S., Chen, B., Trisurat, Y., Pellikka, P., Guo, L., Arunyawat, S., Tuankrua, V., Ogbazghi, W., Yemane, T., 2019. Spatio-temporal analysis of vegetation dynamics as a response to climate variability and drought patterns in the Semiarid region, Eritrea. Remote Sens. 11 (6), 724. https://doi.org/10.3390/rs11060724. 

- Nanzad, L., Zhang, J., Tuvdendorj, B., Nabil, M., Zhang, S., Bai, Y., 2019. NDVI anomaly for drought monitoring and its correlation with climate factors over Mongolia from 2000 to 2016. J. Arid Environ. 164, 69–77. 

- Park, S.-Y., Sur, C., Lee, J.-H., Kim, J.-S., 2020. Ecological drought monitoring through fish habitat-based flow assessment in the Gam river basin of Korea. Ecol. Ind. 109, 105830. https://doi.org/10.1016/j.ecolind.2019.105830. 

- Raheem, N., Cravens, A.E., Cross, M.S., Crausbay, S., Ramirez, A., McEvoy, J., Zoanni, D., Bathke, D.J., Hayes, M., Carter, S., Rubenstein, M., Schwend, A., Hall, K., Suberu, P., 

2019. Planning for ecological drought: Integrating ecosystem services and vulnerability assessment. Wiley Interdiscip. Rev.: Water e1352. https://doi.org/ 10.1002/wat2.1352. 

- Roodposhti, M.S., Safarrad, T., Shahabi, H., 2017. Drought sensitivity mapping using two one-class support vector machine algorithms. Atmos. Res. 193, 73–82. 

- Shah, R., Manekar, V., Christian, R., Mistry, N., 2013. Estimation of Reconnaissance Drought Index (RDI) for Bhavnagar District, Gujarat, India. World Acad. Sci., Eng. Technol., Int. J. Environ., Chem., Ecol., Geol. Geophys. Eng. 7, 507–510. 

- Slette, I.J., Post, A.K., Awad, M., Even, T., Punzalan, A., Williams, S., Smith, M.D., Knapp, A.K., 2019. How ecologists define drought, and why we should do better. Glob. Change Biol. 25 (10), 3193–3200. 

- Smith, P.R., 1981. Bilinear interpolation of digital images. Ultramicroscopy 6 (1), 201–204. 

- Su, Z., 2002. The Surface Energy Balance System (SEBS) for estimation of turbulent heat fluxes. Hydrol. Earth Syst. Sci. 6 (1), 85–100. 

- Vicente-Serrano, S.M., Beguera, S., Lorenzo-Lacruz, J., Camarero, J.S.J., Lpez-Moreno, J. I., Azorin-Molina, C., Revuelto, J.S., Morn-Tejeda, E., Sanchez-Lorenzo, A., 2012. Performance of drought indices for ecological, agricultural, and hydrological applications. Earth Interact. 16, 1–27. 

- Vicente-Serrano, S.M., Miralles, D.G., Domínguez-Castro, F., Azorin-Molina, C., El Kenawy, A., McVicar, T.R., Tom´as-Burguera, M., Beguería, S., Maneta, M., Pena- ˜ Gallardo, M., 2018. Global assessment of the standardized evapotranspiration deficit index (SEDI) for drought analysis and monitoring. J. Clim. 31 (14), 5371–5393. 

- Vicente-Serrano, S.M., Quiring, S.M., Pena-Gallardo, M., Yuan, S., Domínguez-Castro, F., ˜ 2020. A review of environmental droughts: increased risk under global warming? Earth Sci. Rev. 201, 102953. https://doi.org/10.1016/j.earscirev.2019.102953. 

- Wambua, R.M., 2019. Hydrological drought forecasting using modified surface water supply index (SWSI) and streamflow drought index (SDI) in conjunction with artificial neural networks (ANNs). Int. J. Serv. Sci., Manag., Eng., Technol. 10, 39–57. 

- Wang, C., Qi, S., Niu, Z., Wang, J., 2004. Evaluating soil moisture status in China using the temperature–vegetation dryness index (TVDI). Can. J. Remote Sens. 30 (5), 671–679. 

- Wang, H., Li, X., Han, R., Ge, Y., 2006. Variability of vegetation growth season in different latitudinal zones of North China: a monitoring by NOAA NDVI and MSAVI. J. Appl. Ecol. 17, 2236–2240. 

- Wang, Q., Zeng, J., Qi, J., Zhang, X., Zeng, Y., Shui, W., Xu, Z., Zhang, R., Wu, X., 2020. A multi-scale daily SPEI dataset for drought monitoring at observation stations over the Mainland China from 1961 to 2018. Earth Syst. Sci. Data 2020, 1–33. 

- Wen, X., Wu, X., Gao, M., 2017. Spatiotemporal variability of temperature and precipitation in Gansu Province (Northwest China) during 1951–2015. Atmos. Res. 197, 132–149. 

- Xiao, Y., Xiao, Q., 2019. The ecological consequences of the large quantities of trees planted in Northwest China by the Government of China. Environ. Sci. Pollut. Res. 26 (32), 33043–33053. 

- Yan, H., Zhou, G., Yang, F., Lu, X., 2018. DEM correction to the TVDI method on drought monitoring in karst areas. Int. J. Remote Sens. 40 (5-6), 2166–2189. 

- Zang, C.S., Buras, A., Esquivel-Muelbert, A., Jump, A.S., Rigling, A., Rammig, A., 2020. Standardized drought indices in ecological research: Why one size does not fit all. Glob. Change Biol. 26 (2), 322–324. 

- Zhang, B., AghaKouchak, A., Yang, Y., Wei, J., Wang, G., 2019a. A water-energy balance approach for multi-category drought assessment across globally diverse hydrological basins. Agric. For. Meteorol. 264, 247–265. 

- Zhang, B., Zhao, X., Jin, J., Wu, P., 2015. Development and evaluation of a physically based multiscalar drought index: The Standardized Moisture Anomaly Index. J. Geophys. Res.: Atmos. 120 (22), 11,575–11,588. 

- Zhang, G., Su, X., Hao, L., Wu, H., 2019b. Response of vegetation to drought based on NDVI and scPDSI data sets from 1982 to 2015 across China. Trans. Chin. Soc. Agric. Eng. 35, 145–151. 

Zhang, G., Su, X., Singh, V.P., 2020. Modelling groundwater-dependent vegetation index using Entropy theory. Ecol. Model. 416, 108916. https://doi.org/10.1016/j. ecolmodel.2019.108916. 

- Zhang, Y., Yang, S., Ouyang, W., Zeng, H., Cai, M., 2010. Applying multi-source remote sensing data on estimating ecological water requirement of Grassland in Ungauged Region. Procedia Environ. Sci. 2, 953–963. 

- Zhou, Z., Ding, Y., Shi, H., Cai, H., Fu, Q., Liu, S., Li, T., 2020. Analysis and prediction of vegetation dynamic changes in China: past, present and future. Ecol. Ind. 117, 106642. https://doi.org/10.1016/j.ecolind.2020.106642. 

- Zhu, B., Wang, X., Rioual, P., 2017. Multivariate indications between environment and ground water recharge in a sedimentary drainage basin in northwestern China. J. Hydrol. 549, 92–113. 

12 

