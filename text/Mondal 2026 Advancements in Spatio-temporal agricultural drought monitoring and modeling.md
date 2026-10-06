

# **Rapid #: -27622243** 

CROSS REF ID: **896740** 

LENDER: **YY$ (The University of Osaka) :: Main Library** 

BORROWER: **IRU (New Mexico State University) :: Main Library** 

TYPE: Article CC:CCG JOURNAL TITLE: Theoretical and applied climatology USER JOURNAL TITLE: Theoretical and applied climatology. ARTICLE TITLE: Advancements in Spatio-temporal agricultural drought monitoring and modeling: a comprehensive review on multi-source remote sensing and machine learning techniques ARTICLE AUTHOR: Mondal, Suresh VOLUME: 157 ISSUE: 4 MONTH: YEAR: 2026 PAGES: 222ISSN: 0177-798X OCLC #: 41248414 Processed by RapidX: 10/5/2026 7:55:42 PM 

Under our agreement with the publisher, we are not permitted to provide the PDF to the patron through interlibrary loan. Please print the PDF and provide the patron with a paper copy. 

Theoretical and Applied Climatology (2026) 157:222 https://doi.org/10.1007/s00704-026-06136-8 

**REVIEW** 



## **Advancements in Spatio-temporal agricultural drought monitoring and modeling: a comprehensive review on multi-source remote sensing and machine learning techniques** 

**Suresh Mondal**<sup>**1**</sup> **· Kumar Arun Prasad**<sup>**1**</sup> **· A. L. Achu**<sup>**2**</sup> **· S. Kaliraj**<sup>**3**</sup> **· K. Balasubramani**<sup>**1**</sup> 

Received: 29 September 2025 / Accepted: 23 February 2026 / Published online: 18 March 2026 © The Author(s), under exclusive licence to Springer-Verlag GmbH Austria, part of Springer Nature 2026 

##### **Abstract** 

Agricultural drought occurs when soil moisture is insufficient to meet the specific requirements of a given crop during its growth stage, resulting in reduced crop health and yield. Advanced geospatial techniques can effectively monitor and model the spatiotemporal dynamics of agricultural droughts using multiple satellite data products and machine learning (ML) methods, which are accurate, cost-effective, and transferable across space and time. In this study, we comprehensively synthesize the contributions of multi-source remote sensing data and artificial intelligence (AI) approaches (including machine learning and deep learning (DL)) for monitoring, evaluating, and modelling agricultural drought. Additionally, we comprehensively reviewed the latest developments in time-series satellite data analysis, remote-sensing spectral indices, and numerical models used worldwide for rapid, accurate drought monitoring and modeling. Moreover, we critically examined several case studies of drought assessment using ML/DL coupled with satellite data, multi-parametric datasets, and ground-based data to monitor agricultural droughts at local and regional scales and for prediction modelling, owing to their ability to handle complex, non-linear, and large-scale datasets effectively. Overall, big data analytics has great potential for monitoring and assessing agricultural drought using multi-source satellite data, combined with ensemble, hybrid, and physics-based machine learning and deep learning approaches. The review offers a solid theoretical framework and a comprehensive summary of advanced geospatial and ML approaches used for agricultural drought monitoring and modeling, which can be utilized by decision-makers, policy planners, and research organizations to inform policies related to sustainable and climate-smart agriculture. 

Kumar Arun Prasad arunprasad@acad.cutn.ac.in 

Suresh Mondal sureshmondal22@students.cutn.ac.in 

A. L. Achu achu.geomatics@gmail.com 

S. Kaliraj s.kaliraj@ncess.gov.in K. Balasubramani geobalas@acad.cutn.ac.in 

> 1 Department of Geography, School of Earth Sciences, Central University of Tamil Nadu, Thiruvarur 610005, Tamil Nadu, India 

- 2 Department of Climate Variability and Aquatic Ecosystems, Kerala University of Fisheries and Ocean Studies, Kochi (KUFOS), Kochi 682508, Kerala, India 

- 3 National Centre for Earth Science Studies (NCESS), Ministry of Earth Sciences, Thiruvananthapuram 695011, Kerala, India 

### **1 Introduction** 

The drought is considered one of the most complex natural catastrophes since it is difficult to identify its beginning, duration, severity, and geographic coverage (Aadhar and Mishra 2017). Such an unpredictable nature causes an adverse impact on the terrestrial ecosystem, consequently impeding its achievement of the Sustainable Development Goals (SDGs). The large-scale climate models indicate that the frequency of occurrence of drought would substantially increase in the 21 st century (Holgate et al. 2023). Specifically, under the high emission scenario, the compound drought and heat wave events are expected to increase significantly in South Asia, and the population in 70% of the landmass area of the region is going to be affected by such extreme events by the middle of the 21 st century (Ullah et al. 2023). Drought is a stochastic natural and climatic disaster that occurs frequently in many parts 

```
1 3
```

**<mark>222</mark>** <mark>Page 2 of 28</mark> 

S. Mondal et al. 

of the world at any time without any indication (Dutta 2018). Droughts can be defined as an absence or deficiency of precipitation that does not meet demand, and they typically occur over a period of time, such as a week, months, or even years. It is influenced by different factors such as high temperatures, low humidity, strong winds, duration, timing, severity, and distribution of rainy days (Mishra and Singh 2010). It results in economic loss, affecting the largest part of society, agriculture, and environmental problems (Halwatura et al. 2017). It is estimated that drought led to 11.73 million casualties between 1900 and 2021. Further, an economic loss of 6 to 8 billion USD is estimated per year, which is far ahead of any natural disaster (Xu et al. 2023). According to the Australian Bureau of Agricultural and Resource Economics, the 2006 drought had a devastating impact on rural Australia. Winter cereal production decreased by 36%, resulting in estimated economic losses of around AUD $3.5 billion. This significant downturn put many farmers under serious financial pressure, threatening the stability of farming communities across the country (Mishra and Singh 2010; Wong et al. 2010). It is evident from recent severe droughts in around the world such as northern China (2010–2011), California (2011–2017), Europe (2011, 2015, 2018), the Horn of Africa (2011–2012), the Caribbean (2013–2016), southeastern Brazil (2014–2017), South Africa (2015–2016, 2018), India (2016, 2019), and Vietnam (2016) that the degree of exposure, susceptibility, and lack of coping capacity is linked to the risk of adverse effects associated with droughts (Meza et al. 2020). Drought monitoring is a crucial aspect of planning, mitigation, and policymaking for sustainable community development. 

There are numerous definitions of drought. The World Meteorological Organization (WMO) defines drought as a persistent natural hazard characterized by lower-thanexpected or lower-than-normal precipitation that, when prolonged over a season or longer period, is insufficient to meet the demands of human activities and the environment. (WMO 2006). According to the WHO, the drought can be classified into four categories (Fig. 1), namely, (i) Meteorological drought, (ii) Hydrological drought, (iii) Agricultural drought, and (iv) Socio-economic drought, based on their induced factors. 

#### **1.1 Meteorological drought** 

Meteorological drought is a climatic anomaly that refers to the deficiency of precipitation over a certain period, significantly affecting soil-water-crop balances (Ayugi et al. 2022). It could be linked to different variables such as high temperatures, low humidity levels, and high evapotranspiration rates, all of which could potentially exacerbate the 

consequences of meteorological drought (Dingman 2002). Indian Meteorological Department (IMD) further classified this into three classes: (i) Mild meteorological drought (when seasonal rainfall over an area is less than 25% of the normal rainfall), (ii) Moderate meteorological drought (rainfall in between 26 and 50%), and (iii) Severe meteorological drought (rainfall deficit < 75%). Researchers used numerous techniques or indices to understand and monitor the condition of meteorological drought, including the Standard Precipitation Index (SPI), Rainfall Anomaly Index (RAI), and Palmer Drought Severity Index (PDSI) (Alley 1984; Aryal et al. 2022). 

#### **1.2 Hydrological drought** 

Hydrological drought can be defined as a condition where the surface and subsurface water resources are inadequate to meet the normal and specific needs in a specific area (Van Loon 2015). It occurred due to a lack of precipitation and overuse of water from reserves such as rivers, reservoirs, and aquifers. Hydrological drought reduces streamflow, lowers groundwater levels, and can lead to the drying of lakes, wetlands, and rivers. These impacts are often intensified by higher temperatures and increased evaporative demand, which accelerate water loss from both soil and open water bodies. As a consequence, hydrological drought strongly affects aquatic ecosystems by shrinking habitat availability, degrading water quality, and increasing ecological stress on freshwater organisms (Lake 2011). 

#### **1.3 Agricultural drought** 

Agricultural drought is connected to meteorological and hydrological drought (Wang et al. 2016). The rainfall deficiency and water scarcity result in reduced soil moisture content, which affects plant growth and leads to a decline in crop production, a phenomenon referred to as agricultural drought (Seleiman et al. 2021). Soil moisture content is directly related to rainfall or water. If rainfall is deficient, the soil moisture in the area also decreases, negatively impacting crop growth and production, and affecting the country’s food security. Various factors, including crop variety, development stage, soil type, weather, and plant water requirements, determine the amount of water needed for agriculture (Mishra and Singh 2010). Agricultural drought can occur at any time during the crop’s growth. The need for soil moisture varies with crops; hence, the effects of agricultural drought will differ across regions depending on the crops grown (Chowdhury and Gore 1989). It can be further classified into five categories: early-season drought, mid-season drought, terminal season drought, permanent drought, and apparent drought (Sai et al. 2016). 

```
1 3
```

<mark>Page 3 of 28</mark> **<mark>222</mark>** 

Advancements in Spatio-temporal agricultural drought monitoring and modeling: a comprehensive review on… 



**Fig. 1** The sequence of drought impacts associated with meteorological, hydrological, and agricultural drought (adapted and modified from NDMC, 2012) 

#### **1.4 Socio-economic drought** 

Water scarcity refers to the condition in which the available water cannot meet the supply and demand of both human society and animals. This affects health, the economy, society, and quality of life (Zhao et al. 2019; 

Ziolkowska 2016). Socioeconomic drought primarily concerns the social dimensions, emphasizing how drought affects and interacts with human activities. It focuses on the extent to which the environment and society can develop sustainably with the help of the available water resources. (Wang et al. 2022). 

```
1 3
```

**<mark>222</mark>** <mark>Page 4 of 28</mark> 

S. Mondal et al. 

Our primary objectives are to review the applications of satellite remote sensing and Artificial Intelligence (AI) based on geospatial modeling techniques for characterizing and predicting agricultural drought conditions, including Machine Learning (ML) and Deep Learning (DL) approaches. This review aims to provide a comprehensive overview of recent trends in agricultural drought modeling studies that integrate machine learning and deep learning with big data concepts, using multi-source remote sensing and climatic indices. 

### **2 Methodology** 

A literature search was conducted using Google Scholar, BASE, and Semantic Scholar (searches performed up to August 2025). The search focused on two complementary keyword sets: (1) (“Drought” OR “Agricultural drought”) AND (“remote sensing” OR “GIS”), and (2) (“Drought” OR “Agricultural drought”) AND (“AI” OR “machine learning” OR “ML”). These searches were conducted separately to achieve maximum coverage of the literature from both the Remote Sensing/GIS and ML/DL perspectives. There were no restrictions on publication year or study location in the search process to ensure the inclusion of both foundational and recent contributions to drought monitoring and modeling. The final set of eligible studies spanned the period from 1974 to 2025. As the keyword search returned a very large number of records, a relevance-ranked screening strategy was employed, focusing only on those papers that met the eligibility criteria. For each keyword query, results were sorted by relevance, and the top 300 records were screened (Haddaway et al. 2015). Additional relevant studies were identified through citation snowballing. Studies were eligible for inclusion if they addressed drought or agricultural drought from the perspective of Remote Sensing/GIS and/or ML/DL approaches. Whereas predefined search keywords were used for the initial retrieval of candidate records, and the final inclusion was determined through title/abstract screening, as well as full-text assessment (including methodological details). In addition, foundational methodological studies (e.g., drought indices, remote sensing indices, and core ML algorithms) were included when they were directly relevant and frequently cited by eligible drought studies. Papers were excluded if they dealt with unrelated ecological or engineering topics, did not provide a detailed methodology, were in a nonEnglish language, or represented the same paper through multiple databases. The final dataset comprised 205 publications, including journal articles, Proceedings Papers, Early Access Articles, and Conference Papers. From the selected studies, the objectives, study area and scale, 

drought type and indices, data sources, and sensors (for RS/ GIS), as well as the algorithms and features used (for AI studies) were systematically collected (Table 1). 

### **3 Impact of agricultural drought** 

The impact of agricultural drought can vary over time. It adversely affects various aspects of society, their economic condition, and the environment of the concerned area (Wilhite and Glantz 1985). The growth of plants primarily depends on soil moisture and nutrient availability. Factors such as water supply, insect infestations, and plant diseases can negatively affect plant growth (Dixon 2015), leading to reduced crop quality and yield. When plant growth is affected, it also impacts livestock production, which ultimately results in economic losses, displacement of people, and a risk of famine, as well as public health issues, habitat damage, and an increase in farmers’ suicides (Sundararajan et al. 2021). Figure 2 illustrates the major areas of drought vulnerability worldwide, showing that large-scale, intensive drought events have occurred, affecting extensive areas of Europe, Africa, Asia, parts of Australia, South America, and Central America. 

### **4 Rationale for agricultural drought monitoring and modeling** 

Agricultural drought monitoring involves the systematic observation of soil moisture, crop conditions, and related hydroclimatic variables to detect emerging water stress and assess its impacts on crop production (Ajaz et al. 2019; Kaliraj et al. 2024). Unlike flood events, drought processes develop slowly and remain challenging to detect in their early stages, while climate change further increases the risks for climate-sensitive sectors, particularly agriculture (Mishra and Singh 2010). Agricultural drought modeling supports monitoring by enabling early warning, identifying vulnerable areas, and guiding interventions that reduce impacts on food production and water resources (Solh and Ginkel 2014; Ginkel and Biradar 2021). Since a large fraction of the global population directly depends on agriculture, severe drought impacts can trigger cascading socio-economic consequences, including livestock loss, food insecurity, and increased burden on government resources (Bodner et al. 2015; Mera 2018; Speranza et al. 2008). Therefore, timely and reliable drought monitoring and modeling are essential for providing policymakers, the Government, farmers, and other stakeholders with accurate information on cropping strategies, irrigation management, and food security planning. 

```
1 3
```

<mark>Page 5 of 28</mark> **<mark>222</mark>** 

Advancements in Spatio-temporal agricultural drought monitoring and modeling: a comprehensive review on… 

**Table 1** Summarized workflow for the literature search, screening, and selection based on eligibility criteria 

|Step|Stage|Description|
|---|---|---|
|1|Databases/search engines|Google Scholar, BASE, and Semantic Scholar|
|2|Search period (coverage)|Searches performed up to August 2025; eligible studies span<br>1974–2025|
|3|Keyword set 1|(“Drought” OR “Agricultural drought”) AND (“remote sensing”<br>OR “GIS”)|
|4|Keyword set 2|(“Drought” OR “Agricultural drought”) AND (“AI” OR “machine<br>learning” OR “ML”)|
|5|Restrictions applied|No restriction on publication year or study region; English-language<br>only|
|6|Initial retrieval|Keyword searches returned a very large number of results across<br>search engines|
|7|Screening approach|A relevance-ranked screening strategy was applied to manage the<br>large volume of records|
|8|Screening threshold|For each keyword query, results were sorted by relevance, and the<br>top 300 records were screened|
|9|Duplicate handling|Duplicate records across the three sources were removed|
|10|Eligibility assessment|Screening was conducted sequentially: title → abstract → full text|
|11|Additional records|Additional eligible studies (including foundational and highly<br>cited papers) related to drought were identified through citation<br>snowballing.|
|12|Inclusion criteria|Studies were included if they: (i) focused on drought/agricultural<br>drought, and (ii) applied RS/GIS and/or AI/ML/DL approaches,<br>and (iii) provided sufficient methodological details for extraction<br>(indices/sensors/data sources/algorithms/features).|
|13|Exclusion criteria|Studies were excluded if they: (i) were not drought/agricultural<br>drought focused, (ii) lacked RS/GIS or AI/ML/DL methodological<br>relevance, (iii) provided insufficient methodological details, (iv)<br>were non-English, or (v) were duplicates|
|14|Documents type|<br>Eligible document types included journal articles, proceedings<br>papers, early access articles, and conference papers|
|15|Final included studies|205publications were included in this study|





**Fig. 2** Drought vulnerability map of the world. (Source: UNCCD. Global Drought Snapshot, 2023) 

```
1 3
```

**<mark>222</mark>** <mark>Page 6 of 28</mark> 

S. Mondal et al. 

|**Table 2**List of regional and global<br>|Drought MonitoringPlatform|Drought MonitoringIndices|Source/References|
|---|---|---|---|
|drought monitoring platforms<br>(collected and modified from: Ala-<br>hacoon and Edirisinhe2022)|ClimatView - a tool for viewing<br>monthly climate data|SPI<br>f|(Japan Meteorolog-<br>ical Agencyn.d.)|
|g|Flood and drought portal|SPI, Effective Drought Index (EDI), Normalized<br>Difference Vegetation Index (NDVI), Vegetation<br>Condition Index (VCI), Soil Water Index (SWI),<br>Vegetation Health Index (VHI), Agricultural Stress<br>Index (ASI), Combined Drought Index (CDI)|<br>(UNEP-DHIn.d.)|
||North American Drought Moni-<br>toring System|SPI, Percent of Average Precipitation, PDSI|(NOAA-NCEIn.d.)|
||Global Drought Information<br>System|SPI, VHI|(NOAA-GDIS<br>n.d.)|
||Global integrated drought moni-<br>toring and prediction system<br>(GIDMaPS)|SPI, Standardized Soil Moisture<br>Index (SSMI), Multivariate Standardized<br>Drought Index (MSDI)|(Hao et al.2014)|
||IRI Global drought analysis tool|SPI|(IRI-Columbia<br>Universityn.d.)|
||SPEI Global Drought Monitor|Standardized Precipitation Evapotranspiration<br>Index (SPEI)|(CSICn.d.)|
||African Flood and Drought<br>Monitoring System|SPI, NDVI|(AFDM-Princeton<br>Universityn.d.)|
||CIIFEN Drought Monitor||(CIIFENn.d.)|
||European Drought Observatory|CDI, SPI, Soil Moisture Anomaly (SMA), Veg-<br>etation Productivity Anomaly (fAPAR Anomaly)|(EC & JRCn.d.)|
||South Asia Drought Monitoring<br>System (SADMS)|Integrated Drought Severity Index (IDSI), SPI,<br>SMI, VCI, Temperature Condition Index (TCI),<br>Precipitation Condition Index(PCI)|(IWMIn.d.)|



However, drought monitoring based only on station observations is often insufficient due to sparse spatial coverage and limited representativeness, particularly in datascarce regions (Mishra and Singh 2010; Sardar et al. 2021). Satellite remote sensing can partially address these limitations by providing spatially continuous and near-real-time information on vegetation condition, land surface temperature, and surface moisture anomalies (AghaKouchak et al. 2015; Ahady et al. 2025; Łągiewska and Bartold 2025; Mullapudi et al. 2023). Nevertheless, remote sensing products can be affected by cloud contamination, index saturation in dense canopies, and differences in sensor resolution (Jiao et al. 2021; Qin et al. 2021). Monitoring agricultural drought requires integration of multiple sources of information to complement precipitation data (Fioravanti et al. 2025). While ML and DL approaches are increasingly being adopted to integrate multi-source datasets and capture nonlinear relationships between drought, climate, and vegetation drivers (Hou et al. 2025; Obsie and Liu 2025; Prodhan et al. 2022; Rahmati et al. 2020; Rao et al. 2025; Senapati et al. 2025; Tanriverdi and Batmaz 2025). Still, their performance may not transfer well across agroclimatic regions, and many models remain difficult to interpret or validate due to limited ground observations (Houmma et al. 2022; Mi et al. 2025; Prodhan et al. 2022). Therefore, a comprehensive synthesis of remote sensing indices and sensors, along with an AI framework that includes their strengths, 

limitations, and suitability across scales, is essential to support improved drought early warning and risk reduction. In this context, Table 2; Fig. 3 summarize the major regional and global drought monitoring and forecasting platforms. 

### **5 Role of remotely sensed data in understanding the agricultural drought** 

Remote sensing is highly effective for characterizing spatiotemporal changes in land cover in terms of essential physical properties, such as surface radiance and emissivity data (Orhan et al. 2014). Compared with traditional datasets, such as rainfall records and in situ observations, remote sensing provides operational, sustained, and near–real–time measurements with broad spatiotemporal coverage and consistency, thereby overcoming the limitations of measurement error, spatial sparsity, and reporting delays (Jiao et al. 2021; Chandramohan et al. 2024). Since the late 1980 s, remote sensing has been utilized for drought monitoring (Tucker and Choudhury 1987) (Fig. 4). This approach provides data with time intervals and historical records for the same location over a longer period (Stagge et al. 2015). Drought can be assessed using Earth observation (EO) satellite systems, which broadly include: (i) meteorological satellites, such as METEOSAT and NOAA/AVHRR, which provide frequent (near-real-time) observations useful for capturing 

```
1 3
```

<mark>Page 7 of 28</mark> **<mark>222</mark>** 

Advancements in Spatio-temporal agricultural drought monitoring and modeling: a comprehensive review on… 

**Fig. 3** Regional and global drought monitoring and prediction systems around the world (adapted and modified from Gyaneshwar et al. 2023) 





**Fig. 4** Development process of drought monitoring indices (adapted and modified from Liu et al. 2016) 

```
1 3
```

**<mark>222</mark>** <mark>Page 8 of 28</mark> 

S. Mondal et al. 

large-scale atmospheric and vegetation anomalies related to drought (Dalezios et al. 2009), and (ii) land EO satellites, such as the Landsat and Sentinel missions, as well as commercial high-resolution sensors (e.g., SPOT, IKONOS, WorldView), which provide detailed information on vegetation condition, land surface characteristics, and land cover changes relevant to agricultural drought assessment (Gaikwad et al. 2022). 

Large amounts of satellite data are available for agricultural drought research, including the Landsat and Sentinel series, the Moderate Resolution Imaging Spectroradiometer (MODIS), and Soil Moisture Active Passive (SMAP), which are often used for drought monitoring (Table 3). These all provide near-real-time, medium to high-resolution datasets for assessing vegetation cover, soil moisture, crop condition, and water body estimation for lakes, rivers, and reservoirs (Prodhan et al. 2022). Landsat series’ archived 

and real-time data is one of the most frequently used for drought assessment because of its high spatial and temporal resolution. While MODIS and Sentinel are also useful tools for tracking drought conditions, they provide free access and regular Earth observations with extensive temporal and spatial coverage (Mullapudi et al. 2023). 

Satellite data are used to monitor the current situation, as well as pre- and post-disaster conditions (Belal et al. 2012). The technique of remote sensing provides quick, accurate, and continuous relevant data information about vast areas. In the present day, remote sensing-derived products, such as evapotranspiration rates, soil moisture, and vegetation indices, are available for use in agricultural drought monitoring (Rembold et al. 2015). There are a variety of archived remotely sensed data with different spatial and temporal resolution acquired by the different sensors like MODIS, Advanced Spaceborne Thermal Emission and Reflectance 

**Table 3** Current regional and global satellite missions relevant to drought monitoring from 1990 (prepared by author) 



```
1 3
```

<mark>Page 9 of 28</mark> **<mark>222</mark>** 

Advancements in Spatio-temporal agricultural drought monitoring and modeling: a comprehensive review on… 

**Table 3** (continued) 



(ASTER), Advanced Microwave Scanning Radiometer – Earth Observing System (AMSR-E), Advanced Very HighResolution Radiometer (AVHRR), Soil Moisture and Ocean Salinity (SMOS), Advanced wide Field Sensor (AWiFS), Linear Imaging Self Scanning Sensor (LISS-III), Enhanced Thematic Mapper (ETM+) etc. (Amani et al. 2021; Balsamo et al. 2018; Peng et al. 2017) are available for drought monitoring. 

Remote sensing data can also be used to calculate different methods and indices to monitor agricultural drought, like NDVI, VCI, Crop Moisture Index (CMI), TCI, VHI, Soil Moisture Deficit Index (SMDI), SPI, PDSI, RAI, Surface Water Supply Index (SWSI), Drought Area Index (DAI), etc. (Balew et al. 2021; Niemeyer 2008; Zargar et al. 2011; Kaliraj et al. 2025) (refer to Fig. 5). These indices rely on distinctive spectral patterns exhibited by surface soil and canopy characteristics, specifically within the red, nearinfrared, shortwave infrared, and thermal spectral ranges (Hazaymeh and Hassan 2017). For example, the Water 

Deficit Index (WDI) was developed by Moran et al. (1994). Kogan (1995) proposed the VCI for drought monitoring, aiming to remove the influence of both spatial variation in the NDVI and other geographic and ecological parameters. Later, the normalized difference water index (NDWI) was proposed by Gao (1996), followed by the development of the Vegetation Temperature Condition Index (VTCI) (Wang et al. 2001). Sandholt et al. (2002) put forward the temperature vegetation drought index (TVDI) to estimate soil moisture based on the relationship between land surface temperature (LST) and vegetation index (VI); this method is significant for monitoring agricultural drought conditions through soil moisture assessment. This information was later used to propose the VHI by linearly integrating TCI and VCI (Boken et al. 2004; Kogan et al. 2013). Agricultural drought can be analyzed both spatially and temporally using remote sensing data and Geographic Information Systems (GIS) techniques. There are at least four main types of sensors that can be utilized for collecting data in remote 

```
1 3
```

**<mark>222</mark>** <mark>Page 10 of 28</mark> 

S. Mondal et al. 



**Fig. 5** Various remote sensing data sources and techniques used for agriculture drought assessment (adapted and modified from Mullapudi et al. 2023) 

sensing, including optical, thermal, passive microwave, and active microwave systems. Each type has its own benefits and drawbacks (Wang and Qu 2009). 

- i) For identifying vegetation conditions, soil water status, and evapotranspiration, mostly optical and thermal data were used (AghaKouchak et al. 2015; Kaliraj et al. 2022). 

- ii) Microwave remote sensing has mainly been used to estimate the soil moisture content, which is the most important indicator of agricultural drought (Njoku and Entekhabi 1996). 

- iii) LiDAR is the best approach to obtaining structural information of vegetation, and it can also be used to retrieve various biochemical variables, such as leaf water content (Zhu et al. 2017). 

#### **5.1 Optical Remote Sensing method for agriculture drought monitoring** 

Agricultural drought assessment primarily involves understanding or monitoring soil water/moisture content, as well as vegetation condition. Optical remote sensing provides a distinctive perspective by capturing electromagnetic radiation reflected from or emitted by the Earth’s surface and atmosphere (Qin et al. 2021). Optical remote sensing 

operates within specific spectral bands, including visible (VIS), near-infrared (NIR), and shortwave infrared (SWIR) wavelengths, for identifying the condition of vegetation greenness and wetness (Hazaymeh and Hassan 2017) (Table 4). However, index definitions and formulations were cross-referenced using the Index Database  ( h t t p s : / / w w w . i n d e x d a t a b a s e . d e / ) , an open-access repository of remote sensing indices that includes their equations, references, and reported applications. In addition to index descriptions, we provide a concise summary of the main strengths and limitations of drought-relevant optical indices to support the practical selection of indices. It provides valuable information about vegetation health, soil moisture, and drought stress. Healthy vegetation is characterized by its ability to absorb a substantial portion of incident visible light, particularly in the red spectrum, and reflect a significant amount of light in the NIR spectrum. Conversely, unhealthy or stressed vegetation tends to reflect more light in the visible spectrum and less in the NIR spectrum. This is because chlorophyll in plant leaves strongly absorbs visible light for photosynthesis, while leaf cell structure strongly reflects nearinfrared light (Cohen-Cline et al. 2015). Surface reflectance often increases with greater water deficiency, especially in the SWIR, when studying the spectral response of plants at varying water content levels. This relationship between water content and surface reflectance can be used to assess 

```
1 3
```

<mark>Page 11 of 28</mark> **<mark>222</mark>** 

Advancements in Spatio-temporal agricultural drought monitoring and modeling: a comprehensive review on… 

|Key limitation<br>References|Requires soil adjustment factor (L), not stable<br>across all regions<br>(Bowell et al.<br>2021)|Needs blue band; sensor dependent; more com-<br>plex than NDVI<br>(Yoon et al.<br>2020)|d<br>Requires a long-term historical reference period;<br>sensitive to land-cover and cropping pattern<br>changes<br>(Yoon et al.<br>2020)|Often site-specific; affected by canopy/soil<br>mixture<br>(Picoli et al.<br>2017)|-<br>Sensitive to atmospheric correction and sensor<br>differences<br>(Hazaymeh<br>and Hassan<br>2017)|n<br>Sensitive to mixed pixels (soil & vegetation)<br>and requires SWIR availability; affected by<br>clouds/atmospheric noise<br>(Zhao et al.<br>2013)|<br>ht<br>Influenced by soil background, atmosphere/<br>cloud effects, and vegetation phenology, reduc-<br>ing drought-specificity<br>(Chakraborty<br>and Sehgal<br>2010)|i<br><br> <br>Requires additional parameters/assumptions;<br>can be unstable across crops/regions<br>(Ghulam et al.<br>2008)|-<br>Requires SWIR bands (limits sensors); impacted<br>by cloud contamination<br>(Wang and<br>Qu2007)|<br>Not drought-specific, chlorophyll decline may<br>also be caused by nutrient stress, pests, or disease<br>(Gitelson et<br>al.2005)<br>Requires sensors with red-edge bands (limited<br>satellite availability); stress may not be exclu-<br>il dhtdi<br>(Gitelson et<br>al.2005)|svey roug-rven<br>Needs long-term data record; sensitive to land<br>cover change<br>(Singh et al.<br>2003)|Not directly a drought index; responds strongly<br>to vegetation density, not drought only<br>(Baret and<br>Guyot1991)<br>May confuse drought with phenological<br>changes; influenced by soil and canopy effects<br>(Hunt and<br>Rock1989)<br>Needs soil line estimation; not robust in hetero-<br>geneous landscapes<br>(Richardson<br>& Wiegand,<br>1977)|Saturates in dense vegetation; sensitive to soil<br>background and atmosphere<br>(Rouse et al.<br>1974)|l                    , ~ 1.64, and ~ 2.14 μm) bands; M is the slope of the soil line; fv is the|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|n<br>Main strength|Reduces soil background effect<br>compared to NDVI (better in sparse<br>vegetation)|Better than NDVI in high biomass;<br>reduces atmospheric effects|Provides a standardized anomaly-base<br>drought signal, enabling comparison<br>across years and regions|Simple water stress detection|Useful to monitor both soil and vegeta<br>tion drought|Strong indicator of vegetation water<br>content, often detects stress earlier tha<br>NDVI|Highly sensitive to vegetation/canopy<br>moisture stress, useful for early droug<br>detection|Enhances drought detection by reduc-<br>ing the vegetation fraction effect,<br>applicable over variable soil types and<br>topography|Good at capturing both soil and vegeta<br>tion moisture variations|Effective proxy for chlorophyll/vigor,<br>supports early stress detection in crops<br>Detects early chlorophyll stress and<br>avoids NDVI saturation in dense<br>tti|vegeaon<br>Good drought signal by normalizing<br>vegetation condition relative to the<br>hiil|storca range<br>Related to LAI/APAR and canopy<br>condition<br>Captures moisture stress using SWIR/<br>NIR<br>Minimizes soil background noise|Simple, widely used vegetation condi-<br>tion indicator; good long-term trend<br>monitoring|l             R1, SWIR2, and SWIR3 centred at ~ 1.24|
|Applicatio<br>Area|Kenya|<br>East Asia|<br>East Asia|Brazil|Jordon|China|India|China|<br>China|f|India|f<br>USA|US|l            nfrared (SWI|
|Formula/Expression<br>Application|SAVI =<br>(1 +_L_)<br>_ρ NIR−ρ RED_<br>_ρ NIR_+_ρ RED_+_L_<br>Understanding drought<br>conditions using the<br>drought indicator|EVI =<br>_G_<br>_ρ NIR−ρ RED_<br>_ρ NIR_+_C_1_ρ Red−C_2_ρ Blue_+_L_<br>Drought assessment using<br>the vegetation index|_z_ = _NDV I−_<br>_NDV I_<br>_σ_<br>SVI =_P_(_Z < z_)<br>Agriculture drought stress<br>assessment|SRWI =<br>_ρ NIR_<br>_ρ SW IR_1<br>Measurement of drought<br>events|<br>VSDI =<br>1_−_(_ρ SW IR_+_ρ RED −_2_ρ Blue_)<br>Application for soil and<br>vegetation water content|fe<br>NDII =<br>_ρ NIR−ρ SW IR_2<br>_ρ NIR_+_ρ SW IR_2<br>Monitoring vegetation<br>water stress|NDWI =<br>_ρ NIR−ρ SW IR_1<br>_ρ NIR_+_ρ SW IR_1<br>Monitoring vegetation<br>water content for agricul-<br>tural drought|<br> <br>MPDI =<br>1<br>1_−F V C_ (_PDI −FV C ∗PDIV_)<br>Crop water stress for<br>drought estimation|<br>NMDI =<br>_ρ NIR−_(_ρ SW IR_1 _−ρ SW IR_3 )<br>_ρ NIR_+(_ρ SW IR_1+_ρ SW IR_3)<br>Application for soil and<br>vegetation water/moisture<br>content|GCI =<br>(<br>_NIR_<br>_GREEN_<br>)_−_1<br>Study for estimating<br>chlorophyll content<br> <br>Cl Red-edge =<br>(<br>_NIR_<br>_REDEDGE_<br>)_−_1<br>Study for the estimation o<br>chlorophyll content|VCI =100_∗_<br>_NDV Ii−NDV Imin_<br>_NDV Imax−NDV Imin_<br>Vegetation condition for<br>drought monitoring|-<br>NRVI =<br>_RV I−_1<br>_RV I_+1<br>For understanding the lea<br>area index<br> <br>MSI =<br>_ρ SW IR_2<br>_ρ NIR_<br>Plant water stress<br>detection<br>PVI =<br>1<br>_√_<br>_M_2+1 (_ρ NIR −Mρ RED −_1)<br>Vegetation and soil<br>condition|fe<br>NDVI =<br>(_NIR−RED_)<br>(_NIR_+_RED_)<br>Vegetation health<br>monitoring|ltance value of blue (B), red (R), near infrared (NIR), and shortwave i|
|Index/Method|Soil Adjusted Vegeta-<br>tion Index (SAVI)|Enhanced Vegetation<br>Index (EVI)|Standardized Vegeta-<br>tion Index (SVI)|Simple Ratio Water<br>Index (SRWI)|<br>Visible and Shortwave<br>Infrared Drought<br>Index (VSDI)|<br>Normalized Differenc<br>Infrared Index (NDII)|Normalized Drought<br>Water Index (NDWI)|Modified Perpen-<br>dicular Drought Index<br>(MPDI)|Normalized Multiband<br>Drought Index<br>(NMDI)|Green Chlorophyll<br>Index (GCI)<br>Chlorophyll Red-edge<br>Index (Cl Red-edege)|Vegetation Condition<br>Index (VCI)|Normalized Ratio Veg<br>etation Index (NRVI)<br>Moisture Stress Index<br>(MSI)<br>Perpendicular Vegeta-<br>tion Index (PVI)|Normalized Differenc<br>Vegetation Index<br>(NDVI)|(ρ is the surface reflec<br>vegetation fraction)|



```
1 3
```

**<mark>222</mark>** <mark>Page 12 of 28</mark> 

S. Mondal et al. 

plant water stress and drought conditions (Holzman et al. 2021). Optical remote sensing operates within a 400– 2500 nm wavelength range of the spectrum to study agricultural drought conditions. In between, water exhibits two major absorptions at 1470 nm and 1900 nm, as well as two minor peaks at 970 nm and 1200 nm (Bablet et al. 2018). 

In general, the optical remote sensing-based agricultural drought indices can be further divided into three groups e.g.: (a) vegetation drought monitoring indices, such as NDVI, MSI, VCI, etc., which are more applicable for moderately to densely vegetative areas; (b) soil drought monitoring indices, like Perpendicular Drought Index (PDI), applicable for bare soil surface; and (c) vegetation and soil drought indices, such as moisture stress index (MSI), visible and shortwave drought index (VSDI), and normalized multiband drought index (NMDI) (Hazaymeh and Hassan 2017) and again, vegetation drought monitoring indices are also further classified into (i) slope-based vegetation indices, and (ii) distance-based vegetation indices (Jackson and Huete 1991). 

##### **5.1.1 Multispectral Remote Sensing** 

Multispectral remote sensing is widely applied in agricultural management, including crop health assessment, irrigation and water resource monitoring, and detection of vegetation stress, by capturing surface reflectance at multiple wavelength bands (Ahmad et al. 2021). Multispectral sensors utilize a limited number of discrete spectral bands with relatively broad bandwidths across the visible, NIR, and SWIR regions, enabling operational monitoring of vegetation condition and moisture variability (Liaghat and Balasundram 2010). These bands support the derivation of widely used drought-related indices such as NDVI/ EVI (vegetation greenness) and NDWI/NDMI/MSI (vegetation moisture and water stress). In recent years, multispectral drought-related indices have been extensively used to characterize and monitor agricultural drought conditions across different spatial scales (Mansour Badamassi et al. 2020; Prodhan et al. 2021). Key multispectral satellite missions commonly used in drought studies include the Landsat series, Sentinel-2, and MODIS, which provide long-term time series observations with varying spatial and temporal resolutions, making them suitable for agricultural drought monitoring (Namazi et al. 2023; Wassie et al. 2022; Widiyatmoko et al., 2021). 

##### **5.1.2 Hyperspectral Remote Sensing** 

Hyperspectral remote sensing is a modern and prominent technology that can be utilized for precision agriculture applications, including drought monitoring, crop 

monitoring, yield estimation, water stress measurement, and crop classification (Singh and KV 2022). Hyperspectralbased methods are one way to enhance our ability to observe drought, according to recent research (Ramamoorthy et al. 2022). Hyperspectral remote sensing involves the acquisition of data across hundreds of narrow, contiguous spectral bands spanning the electromagnetic spectrum from visible light to shortwave infrared. It ranges from 400 to 2500 nm, which provides a detailed spectral signature of the surface. Unlike traditional broadband optical sensors, hyperspectral remote sensing offers the potential to more accurately identify physiological and biochemical changes in plants under water stress (Lu et al. 2020; Manjunath et al. 2011; Zou et al. 2023). Hyperspectral remote sensing data are available for agricultural studies from ground-based, airborne, and spaceborne sources (Wong et al. 2022). Many vegetation and moisture indices (e.g., NDVI, EVI, NDWI, MSI) were originally developed for multispectral sensors but can also be derived from hyperspectral reflectance. In contrast, rededge and other narrow-band chlorophyll indices represent hyperspectral-capable indicators and are typically more sensitive to early crop stress. Therefore, a representative list of hyperspectral-derived indices is provided here for completeness (refer to Table 5). 

NASA introduced the first successful Hyperion EO-1 as a hyperspectral satellite sensor into Earth’s orbit in November 2000 (Lamine et al. 2019). In recent years, hyperspectral remote sensing has made significant progress in both commercial and research applications, surpassing multispectral remote sensing. This is due to the development of several hyperspectral remote sensing missions, including the Italian PRecursore IperSpettrale della Missione Applicativa (PRISMA), Germany’s Environmental Mapping and Analysis Program (EnMAP), and NASA’s Hyperspectral Infrared Imager (HyspIRI) (Lopinto and Ananasso 2014; Singh et al. 2020). 

#### **5.2 Thermal Remote Sensing** 

Thermal remote sensing has several applications in agricultural drought monitoring, owing to its ability to collect temperature-related data. This approach involves assessing the temperature of both crops and soil, providing insights into water stress levels and various environmental factors that influence plant growth at different geographical scales (Hazaymeh and Hassan 2017). Thermal infrared sensors primarily detect thermal radiation emitted by the Earth’s surface, and the magnitude of this radiation is associated with both LST and Land Surface Emissivity (LSE), which can serve as indicators of drought stress and plant stress (Hulley & Hook, 2011). So, temperature-based drought indices can also be calculated using thermal remote sensing data 

```
1 3
```

<mark>Page 13 of 28</mark> **<mark>222</mark>** 

Advancements in Spatio-temporal agricultural drought monitoring and modeling: a comprehensive review on… 

|**Table 5**Agriculture drought monitor<br>|Index/Method<br>-|Formula/Expression|Year|References|
|---|---|---|---|---|
|ing indices derived from hyperspec-<br>tral observations|Normalized Difference Vegetation<br>Index (NDVI)|NDVI =<br>_ρ_ 800_−ρ_ 680<br>_ρ_ 800+_ρ_ 680|2017|(Sun et al.2017)|
||Enhanced Vegetation Index (EVI)|EVI<sup>= 2</sup><sup>_._5(</sup><br>_R_1828_−R_630<br>_R_1828+6_R_630_−_7_._5_R_450+1<br>)|2014|(Son et al.2014)|
||Leaf Water Index (LWI)|LWI =<br>_R_1350<br>_R_1450|2008|(Seelig et al.2008)|
||Green Chlorophyll Index<br>(_Clgreen_)|_Clgreen_ = <sup>(</sup> <sup>_ρ_ 750</sup><br>_ρ_ 550<br>)_−_1|2005|(Gitelson et al.2005)|
||Red edge Chlorophyll Index<br>(_Clred−edge_)|_Clred−edge_ = <sup>(</sup> <sup>_ρ_ 750</sup><br>_ρ_ 710<br>)_−_1|2005|(Gitelson et al.2005)|
||Simple Ratio (SR)|SR =<sup>_ρ_ 800</sup><br>_ρ_ 680|1997|(Gitelson and Merzlyak<br>1997)|
||Normalized Difference Water<br>Index (NDWI)|NDWI =<sup>_ρ_ 857</sup><sup>_−ρ_ 1241</sup><br>_ρ_ 857+_ρ_ 1241|1996|(Gao1996)|
||Water Index (WI)|WI =<br>_ρ_ 900<br>_ρ_ 970|1993|(Peñuelas et al.1993)|
||Moisture Stress Index (MSI)|MSR =<sup>_R_1600</sup><br>_R_820|1989|(Hunt and Rock1989)|



(ρ and R are the surface reflectance value of blue (B), red (R), near infrared (NIR), and shortwave infrared (SWIR1, SWIR2, and SWIR3 centred at ~ 1.24, ~ 1.64, and ~ 2.14 μm) bands) 

(Hazaymeh and Hassan 2017). AVHRR, ASTER, LANDSAT, MODIS, and ATLAS are some thermal infrared sensors deployed on satellite and airborne platforms. The most commonly used thermal remote sensing indices are given in Table 6. 

#### **5.3 Microwave Remote Sensing** 

Microwave remote sensing offers advantages for assessing agricultural drought, including the ability to conduct observations both during the day and at night and deeper signal penetration, which provides a more comprehensive assessment of 

moisture conditions across the entire canopy (Table 7). It can be used in all weather conditions and can penetrate through clouds, which is not possible with other remote sensing techniques (Vreugdenhil et al. 2022). Microwave sensors detect signals in the frequency range of 0.3 to 300 GHz, equal to wavelengths from 1 m to 1 mm (Ulaby et al. 1986). L-, C-, X-, and Ku-bands operate using microwave sensors for earth observation, spanning frequencies between 1 and 18 GHz, and are highly sensitive to the water content in the surface soil layer (Vreugdenhil et al. 2022). Because of their sensitivity to the dielectric constant, microwaves can detect the amount of water in the top layer of soil and the biomass above ground. 

**Table 6** Agriculture drought monitoring indices using thermal remote sensing 

|Index/<br>Method|Formul|a/Expression|Application|Applica-<br>tion Area<br>|Main strength<br>f|Key limitation|References|
|---|---|---|---|---|---|---|---|
|Temperature<br>Ratio Index<br>(TRI)|TRI =|( <sup>_dT_</sup><br>_dt_ <sup>)</sup>_Max_<sup>_−_(</sup> <sup>_dT_</sup><br>_dt_ <sup>)</sup><br>_i_<br>( <sup>_dT_</sup><br>_dt_ <sup>)</sup>_Max_<sup>_−_(</sup> <sup>_dT_</sup><br>_dt_ <sup>)</sup>_Min_|Used for the<br>analysis of agri-<br>cultural drought|Australia|Simple and effective for<br>representing relative thermal<br>stress by comparing tem-<br>perature signals|Sensitive to seasonal back-<br>ground temperature changes;<br>interpretation may vary across<br>regions and crop stages|(Hu et al.<br>2020)|
|Apparent<br>Thermal Iner-<br>tia (ATI)|ATI =|<sup>_C ∗_1</sup><sup>_−α_</sup><br>_∆Ts_|Estimate soil<br>water content<br>using thermal<br>index|Italy|Strong indicator of surface<br>moisture status, and useful<br>for early drought stress<br>detection|Requires day–night LST and<br>accurate surface parameters;<br>performance reduces under<br>dense vegetation/clouds<br>and with coarse temporal<br>resolution<br>f|(Claps and<br>Laguardia<br>2004)|
|Normalized<br>Difference<br>Temperature<br>Index (NDTI)|NDTI =|<br>_T_1_−TS_<br>_T_1_−T_0|Estimation of<br>vegetation cover<br>and condition, as<br>well as soil mois-<br>ture, for drought<br>circumstances.|Australia|Captures temperature anom-<br>aly/stress signal clearly;<br>useful for identifying hot/dry<br>conditions over croplands|Highly affected by cloud<br>contamination, emissivity<br>uncertainty, and surface<br>heterogeneity (bare soil vs.<br>vegetation)|(McVicar<br>and Jupp<br>1998)|
|Temperature<br>Condition<br>Index (TCI)|TCI =<br>|(<br>_TSMax −TS_<br>_TS Max−TSMin_<br>)<br>_∗_100|Calculate the<br>drought effect on<br>vegetation|US|Useful for agricultural<br>drought because temperature<br>rises under water stress|Temperature can rise due<br>to heatwaves/urbanization<br>also and require clear sky<br>conditions|(Kogan<br>1995)|



(C is the solar correction factor; a is the surface albedo; _∆Ts_ is the difference between the afternoon and midnight land surface temperature; _TSMax_ and _TSMin_ are the maximum and minimum Ts from all images in the dataset, respectively. _T_ 1 and _T_ 0 are the modeled surface temperatures if there is an infinite or zero surface resistance, respectively) 

```
1 3
```

**<mark>222</mark>** <mark>Page 14 of 28</mark> 

S. Mondal et al. 

**Table 7** Agriculture drought monitoring indices using microwave remote sensing 

|Index/Method|Formula|/Expression|Application|Applica-<br>tion Area|Main strength|Key limitation|References|
|---|---|---|---|---|---|---|---|
|TRMM<br>Precipitation<br>Condition<br>Index (PCI)|PCI =<br>_T_|_TRMM−T RMMMin_<br>_RMMMax−T RMMMin_|Monitoring<br>drought under<br>different weather<br>conditions|China|Provides a normalized<br>rainfall anomaly signal,<br>useful for the rapid detec-<br>tion of drought onset at<br>the regional scale|Limited by TRMM spatial<br>resolution and retrieval<br>uncertainty, and rainfall deficit<br>may not directly represent<br>agricultural drought impacts|(Zhang and<br>Jia2013)|
|Soil Moisture<br>Condition<br>Index (SMCI)|SMCI =|<br>_SM−SMMin_<br>_SMMax−SMMin_|Monitoring<br>short-term<br>drought under<br>different weather<br>conditions|China|Directly represents soil<br>water deficit, making<br>it highly relevant for<br>agricultural drought<br>monitoring and crop<br>stress assessment|Satellite soil moisture data are<br>coarse and sensitive to vegeta-<br>tion cover, surface roughness,<br>and depth limitations, so they<br>may not accurately reflect the<br>moisture in the deeper root zone.|(Zhang and<br>Jia2013)|
|Microwave<br>Polarization<br>Difference<br>Index (MPDI)|MPDI =|<br>_TBV −TBH_<br>_TBV_+_TBH_|Retrieving soil<br>moisture and<br>vegetation opti-<br>cal depth|USA|Good soil moisture<br>retrieval even under some<br>vegetation|Coarse resolution in passive<br>microwave; mixed pixel<br>problem<br>f|(Owe et al.<br>2001)|
|Normalized<br>Backscatter<br>Moisture Index<br>(NBMI)|NBMI =|<br>_Bt_1_−Bt_2<br>_bt_1_−Bt_2|High spatial<br>resolution for<br>soil moisture<br>conditions|Israel|Works in all weather,<br>day/night; sensitive to<br>soil moisture|Backscatter is affected by sur-<br>face roughness and vegetation<br>structure|(Shoshany<br>et al.2000)|



_TRMMMin_ and _TRMMMax_ ; _SMMin_ and _SMMax_ are the minimum and maximum values of TRMM and SM of the pixel during the study period, respectively. _TBV_ and _TBH_ are brightness temperatures at Vertical and Horizontal polarization, respectively; _Bt_ 1 and _Bt_ 2 are the backscatter coefficients at different time steps 

Microwaves can detect soil, vegetation, and water through their sensitivity to the dielectric constant (Wang and Qu 2009). Two types of microwave remote sensing, active and passive microwave remote sensing-based models/indices, have shown promising results for water content estimation and agricultural drought studies (Moran 2004). 

Passive microwave remote sensing involves measuring the natural microwave radiation emitted by the Earth’s surface and atmosphere. This remote sensing measures the soil surface emission intensity using a radiometer (Engman 1991). It can provide information about the surface temperature, vegetation cover, and soil moisture content (Njoku and Entekhabi 1996). The Scanning Multichannel Microwave Radiometer (SMMR), Special Sensor Microwave/Imager (SSM/I), and SMAP are examples of passive microwave remote sensing sensors. 

Active microwave sensors are particularly useful for monitoring soil moisture and assessing the onset and severity of agricultural drought, as they can operate both day and night and have the ability to penetrate cloud cover (Walker et al. 2004). In active microwave remote sensing, sensors such as Synthetic Aperture Radar (SAR) systems transmit microwave radiation and capture backscattered signals at various frequencies, including C-, L-, and X-band. The radiation can be emitted and received by both horizontal polarization and vertical polarization, and at different angles (Vreugdenhil et al. 2022). This can be further grouped into three categories: (a) theoretical approaches (e.g., Integral equation model), (b) empirical approaches (e.g., Normalized Backscatter Moisture Index and Wetness Index), and (c) Semiempirical approaches (Hazaymeh and Hassan 2017). 

#### **5.4 Combined remote sensing-based method for agriculture drought monitoring** 

Monitoring agricultural drought with combined remote sensing-based approaches from multiple remote sensing sources and sensors to provide a more comprehensive and precise evaluation of drought conditions over a large area. These techniques use a variety of remote sensing technologies, including optical, thermal, and microwave sensors, to capture various environmental variables (Hazaymeh and Hassan 2017). Optical remote sensing sensors, such as multispectral and hyperspectral sensors, can be used to monitor vegetation health and land cover, while thermal remote sensing provides information on soil and crop temperatures, which indicate water stress (Gerhards et al. 2019). Combining optical and thermal data can provide more comprehensive insight into crops’ or plants’ responses to drought conditions (Zhang and Zhou 2015), for example, the VHI, Normalized Difference Drought Index (NDDI), VTCI, WDI, etc. (see Table 8). 

On the other hand, microwave sensors, such as SAR data, can penetrate cloud cover and other weather conditions and are sensitive to soil moisture levels. Combining optical and thermal data with SAR can provide more accurate and precise information on soil moisture and vegetation health during drought. Recent advancements in microwave remote sensing enable the assessment of agricultural drought across diverse topographic and land-cover settings, using both active and passive microwave measurements. Specifically, missions such as ALOS-PALSAR, SMOS, and SMAP provide a valuable combination of passive and 

```
1 3
```

<mark>Page 15 of 28</mark> **<mark>222</mark>** 

Advancements in Spatio-temporal agricultural drought monitoring and modeling: a comprehensive review on… 

|Key limitation<br>References|n<br>Strongly affected by seasonality and<br>land cover differences; can confuse<br>drought with phenology/harvest<br>changes<br>(Gu et al.<br>2007)<br>Sensitive to soil background and<br>atmospheric effects; performance<br>decreases in sparse vegetation<br>(Jang et al.<br>2006)|h<br>Depends on temperature/LST quality<br>and can be biased by cloud contami-<br>nation and sensor noise<br>(Wu and<br>Lu2016)|s<br>Requires local calibration and is<br>sensitive to weather variability<br>(Tang and<br>Li2014)|Needs stable NDVI–LST relationship;<br>affected by heterogeneous land cover<br>and mixed pixels<br>(Hassan et<br>al.2007)|<br>Assumes well-defined wet/dry<br>edges; errors in complex terrain, and<br>irrigated areas<br>(Sandholt<br>et al.2002)|Sensitive to land cover change and crop<br>calendar; may miss short-term drought<br>if the compositing period is long<br>(Kogan<br>2002)<br>Requires correct dry/wet edge<br>definition; impacted by clouds and<br>topographic temperature gradients<br>(Wang et<br>al.2001)|l<br>The relationship varies by crop type<br>and phenology stage.<br>(Lambin<br>and Ehrlich<br>1996)<br>Strongly affected by phenology and<br>vegetation density; weaker in hetero-<br>geneous landscapes<br>(Carlson et<br>al.1994)<br>Requires multiple sensors and care-<br>ful preprocessing; uncertainty from<br>microwave retrieval noise<br>(Liu et al.<br>2017)<br>r-<br>Microwave coarse resolution and<br>vegetation effects limit use at the field<br>scale and dense canopy<br>(Zhang and<br>Jia2013)<br>Composite weights/normalization can<br>introduce subjectivity; results depend<br>on input datasets and scalingchoices<br>(Rhee et al.<br>2010)<br>perature at the dry edge;_TMin_is the minimum surface<br>NDVI value in a study area, respectively._TsNDV Ii_is<br>_θ wet_the wet edge;_θ S_is the surface potential tempera-<br>fi   ve Polarization Difference Index.)|
|---|---|---|---|---|---|---|---|
|n<br>Main strength|Combines vegetation & moisture<br>sensitivity, enabling better detectio<br>of vegetation water stress than<br>NDVI alone<br>Simple and effective indicator of<br>canopy/soil moisture variation|Improved drought sensitivity by<br>integrating vegetation response wit<br>atmospheric demand, useful for<br>|spatiotemporal drought tracking<br>Directly represents crop water stres<br>and irrigation requirement; highly<br>useful at field scale|i<br>Integrates vegetation and thermal<br>information to reflect surface wet-<br>ness, useful for early crop stress|<br>Strong for estimating relative soil<br>moisture/dryness using the NDVI–<br>LST triangle method|Combines greenness and tempera-<br>ture effects, giving a robust indica-<br>tor of agricultural drought severity<br>Effective proxy of soil moisture<br>stress by linking NDVI with LST-<br>based dryness conditions|Captures vegetation–temperature<br>coupling and stress response, usefu<br>for drought detection<br>Links vegetation response with<br>water supply, helpful for seasonal<br>drought monitoring<br>Integrates thermal and microwave<br>signals, improving drought detec-<br>tion under cloud cover and vegeta-<br>tion effects<br>Uses microwave sensitivity to soil<br>moisture, good for drought monito<br>ing even under clouds/haze<br>Multi-indicator composite index<br>improves reliability by combining<br>different drought signals<br>y;_TMax_is the maximum surface tem<br>eratures of pixels that have the same<br>al evaporation,_θ dry_is the dry edge; <br>d coefficients, MPDI means Microwa  f|
|Applicatio<br>Area|<br>USA<br>USA|China|Affrica|Canada|<br>Affrica|World<br>China|-<br>Affrica<br>USA<br>China<br>China<br>USA<br>eriod of stud<br>surface temp<br>T is the actu<br>undetermine fi     f|
|Application|Enhances the drought-captur-<br>ing ability using both vegeta-<br>tion greenness and wetness<br>conditions<br>Evaluate thermal and water<br>stress of vegetation, the com-<br>bination of vegetation green-<br>ness and wetness conditions|Monitoring drought<br>conditions|Agriculture drought<br>monitoring|Estimate land surface water<br>content|Applied for the assessment of<br>surface soil moisture status|Drought monitoring<br>Monitoring drought occur-<br>rences at the regional level|Understanding drought condi<br>tions and broad scales<br>Delineate the drought<br>condition<br>Monitoring a heavy drought<br>area<br>Monitoring agriculture and<br>meteorological drought over<br>cropland and grassland<br>Agricultural drought assess-<br>ment over arid and humid<br>regions<br>VSWI of the pixel during the p<br>maximum and minimum land<br>VIi; Ta is the air temperature; E<br>erature limit, a and b represent  fi     f|
|Formula/Expression|NDDI = _NDV I−NDW I_<br>_NDV I_+_NDW I_<br> <br>NMI = NDVI-NDWI|<br>MVWSI = _RNDV I_<br>_RLST_2|<br>CWSI=<br>(_T s−T a_)_−_(_T s−T a_)_Min_<br>(_T s−T a_)_Max−_(_T s−T a_)_Min_|TVWI =<br>_θ dry−θ S_<br>_θ dry_+_θ wet_|TVDI =<br>_TS−TSMin_<br>_TSMax_+_TSMin_|<br>VHI = 0.5*VCI+(1-0.5)*TCI<br>VTCI =<br>_T sNDV IMax −T sNDV Ii_<br>_T sNDV IMax_+_T sNDV IMin_|TVX =<br>_TS_<br>_NDV I_<br>VWSI = _NDV I_<br>_TS_<br>TMVDI =<br>_LSTi−LSTMin_<br>_a_+_b∗MP DI−LSTMin_<br>MIDI = α * PCI + β * SMCI +<br>(1 − α – β) TCI<br>SDCI = (1/4) * Scaled TS + (2/4)<br>* Scaled TRMM + (1/4) Scaled<br>NDVI<br>e minimum and maximum values of<br>_DV IMax_and_TsNDV IMin_are the<br>ne pixel whose NDVI value is ND<br>ature,_LSTMin_lower surface temp       fi     f|
|Type<br>Index/Method|A combi-<br>nation of<br>optical-based<br>indices<br>Normalized Dif-<br>ference Drought<br>Index (NDDI)<br>Normalized Mois-<br>ture Index (NMI)|A combina-<br>tion of surface<br>temperature<br> <br>Modified Vegeta-<br>tion Water Supply<br>Index (MVWSI)|and vegeta-<br>tion Index<br>Crop Water Stress<br>Index (CWSI)|Temperature Veg-<br>etation Wetness<br>Index (TVWI)|<br>Temperature Veg-<br>etation Dryness<br>Index (TVDI)|Vegetation Health<br>Index (VHI)<br>Vegetation<br>Temperature<br>Condition Index<br>VTCI|()<br>Temperature<br>Vegetation Index<br>(TVX)<br>Vegetation Water<br>Supply Index<br>(VWSI)<br>Combined<br>optical,<br>thermal, and<br>microwave<br>index<br>Temperature<br>Microwave<br>Vegetation Index<br>(TMVDI)<br>Microwave Inte-<br>grated Drought<br>Index (MIDI)<br>Scaled Drought<br>Condition Index<br>(SDCI)<br>(VSWImin and VSWImax are th<br>temperature at the wet edge;_TsN _<br>the land surface temperature of o<br>ture,_LSTi_means surface temper|



```
1 3
```

**<mark>222</mark>** <mark>Page 16 of 28</mark> 

S. Mondal et al. 

active microwave data, and they can provide highly accurate drought monitoring solutions by improving the accuracy of soil moisture and vegetation water content retrievals (Hazaymeh and Hassan 2017). 

### **6 Big data and machine learning (ML) methods for agricultural drought study** 

Big data and ML have become increasingly important for agricultural drought monitoring, as they can handle large, heterogeneous datasets and extract insights that enable real-time analysis, predictive modeling, and improved decision-making. As droughts grow more frequent and severe worldwide, interest in integrating big data and ML techniques has intensified, engaging engineers, environmental scientists, and researchers from diverse disciplines (Prodhan et al. 2022). Because manual processing and interpretation of remote sensing imagery and meteorological data are labor-intensive and time-consuming, big data and machine learning offer effective, scalable alternatives for feature extraction and information retrieval from large spatiotemporal datasets. Within computational intelligence, these approaches have become essential for drought monitoring and prediction, improving the accuracy of both situational assessment and forecasting. In particular, the remote sensing data cubes, which organize Earth observation and ancillary data into a consistent spatiotemporal-spectral array, enable efficient, reproducible queries and large-scale analytics, further streamlining drought assessment and forecasting workflows (Xu et al. 2020). 

Big data analytics allow for processing large datasets from multiple sources, like remote sensing, meteorological stations, and agriculture surveys, to track drought conditions adequately (Balti et al. 2020). For example, Zhang et al. (2017) analysed and predicted a big data-based approach for the California drought. The authors used diverse datasets, including climate sensor and satellite data, weather data, drought conditions, and water-use reports. Similarly, Shah et al. (2017) proposed a Big Data analytics approach to predict drought occurrence using a Random Forest (RF) model and manage droughts based on historical rainfall, temperature, and evapotranspiration data. 

Similarly, Machine Learning and Deep Learning models have been found helpful in evaluating complex datasets and detecting patterns associated with drought by using past data (Agana and Homaifar 2017; Prodhan et al. 2021, 2022; Rahmati et al. 2020). Popular ML models in the literature include decision tree models, such as Classification and Regression Trees (CART) (Veettil and Mishra 2023), Conditional Inference Trees and multivariate regression trees (Paez-Trujilo et al. 2023), Support Vector Machine (SVM) models (Linear 

SVM (Pande et al. 2023), Kernel SVMs (Pande et al. 2023), Support Vector Regression (Tian et al., 2018) and One-Class SVM (Roodposhti et al. 2017), Boosting models (Adaptive Boosting (AdaBoost) (Koteswararao and Rajendran 2025), Gradient Boosting Machines (GBM), Xtreme Gradient Boosting (XGBoost) (Ekmekcioğlu 2023), Categorical Boosting (CatBoost), Ensemble models (RF) (Zarei et al. 2023), Bagging models, Extremely Random Trees (XTR) (Elbeltagi et al. 2023), Stacking models) and Neural network– based models (Multilayer Perceptron (MLP) NNs (Kan et al. 2023) and deep learning models such as Convolutional Neural Networks (CNN) (Kan et al. 2023), Autoencoders (Xing et al. 2025), Long Short-Term Memory (LSTM) (Kheyruri et al. 2023), and Graph Neural Networks (GNN) (Chandra et al. 2025) have been widely used to predict agricultural droughts with high accuracy. Although picking a single most suitable model still remains a topic of debate. 

Machine learning techniques are coupled with remote sensing data, such as satellite imagery and climate data, to improve the temporal and spatial accuracy of drought monitoring. Rahmati et al. (2020) evaluate the Relative Departure Soil Moisture (RDSM) method for mapping agricultural drought hazards using CART, boosted regression trees (BRT), RF, multivariate adaptive regression splines (MARS), flexible discriminant analysis (FDA), and SVM in Australia. The study found that approximately 26% of the area is at high or very high risk of drought. Similar work was conducted by Kafy et al. (2023) using Cellular Automata (CA) and Artificial Neural Network (ANN) algorithms to assess and predict agricultural drought vulnerability in Bangladesh, based on remote sensing-based indices. Similarly, Nie et al. (2018) employed SVM, RF, ANN, and BPNN (Back-Propagation Neural Network) models to predict soil moisture. The findings indicated that SVM outperformed RF and BPNN in terms of prediction accuracy, with terrain, precipitation, and relative humidity being the primary factors influencing soil moisture. Therefore, big data integration approaches would benefit real-time drought disaster forecasting and mapping. The importance of environmental decision-making in drought disaster analysis will be further enhanced by a knowledge-based system with a big data platform, incorporating ML and data mining (Prodhan et al. 2022). However, there is still a need for different hybrid and physics based ML techniques such as Autoencoder coupled with RF/XGBoost, Physics-Informed Neural Network (PINN), Process-Guided Neural Networks (PGNNs) with high computational efficiency that will likely focus on leveraging large amounts of data sets (big data), such as combining remote sensing data, weather data, and other relevant data to improve the accuracy and speed of predictions. Table 9 lists contemporary models and methods for handling various features of big data in drought monitoring. 

```
1 3
```

<mark>Page 17 of 28</mark> **<mark>222</mark>** 

Advancements in Spatio-temporal agricultural drought monitoring and modeling: a comprehensive review on… 

**Table 9** Big data drought monitoring tools. (source: Balti et al. 2020) 

|Character-<br>istics|Tool used|Remarks|References|
|---|---|---|---|
|Volume|Hadoop|Distributed<br>processing|(Rathore et al.2015;<br>Zou et al.2018)|
|Variety|Hadoop|Schema-less data<br>store|(Rathore et al.2015;<br>Zou et al.2018)|
|Velocity|Weka, H2O|Query data inside<br>RAM instead of disk|(Yu et al.2019;<br>Zhang et al.2017)|
|Veracity|Heroku|Stream processing|(Zhang et al.2017)|
|Visualization|ArcGIS,<br>Weka|Friendly user<br>interface|(Xu et al.2016)|



### **7 Agriculture drought modeling and prediction using remote sensing data** 

Agricultural drought can affect multiple dimensions of society, including a decline in crop and livestock productivity. Although drought cannot be fully prevented, its impacts can be reduced through effective monitoring and early warning systems based on historical trends and predictive modelling (Ortega-Gaucin et al. 2016; Hao et al. 2014). Forecasting of drought is a challenging task due to the highly complex interactions of meteorological and hydrological processes (Wu 2014). Even agricultural drought models that rely on meteorological factors often struggle to provide precise predictions due to the alterations in established patterns caused by climate change (Park et al. 2019). Therefore, accurate agricultural drought prediction can help farmers adjust planting schedules, select suitable crops, and adapt irrigation methods, particularly in areas vulnerable to drought. In this case, remote sensing (RS) data are reliable and efficient for agricultural drought studies, as they provide spatially continuous and temporally consistent observations over large areas (Zhao et al. 2019). Satellite products capture various hydroclimatic factors relevant to drought evolution, including precipitation, surface temperature, soil moisture, snow cover, and vegetation health, on both regional and global scales (AghaKouchak et al. 2015; Wardlow et al. 2012). Traditional drought assessment approaches that depend mainly on sparse station observations, while RS data can support near-real-time monitoring with greater spatiotemporal detail (Sardar et al. 2021). This helps in understanding the onset, duration, severity, and recovery of drought. 

Agricultural drought monitoring, evaluation, and forecasting are commonly based on meteorological indices (e.g., SPI, SPEI, PDSI) and vegetation/temperature-based indices (e.g., NDVI, VCI, VHI, CMI, crop-specific indices, etc.), and among other composite indices (Carlson et al. 1994; Chere and Debalke 2024; Docheshmeh Gorgij et al. 2022; Kan et al. 2023). These indices serve as valuable tools for quantifying the impacts of drought on agriculture, particularly through changes in vegetation condition 

and crop stress (Park et al. 2019). Vegetation indices (VIs) are especially useful because they capture spectral changes associated with reduced greenness and moisture stress during drought periods (Lekakis et al. 2022). While meteorological indices remain widely used, satellite time-series indicators are increasingly supporting improved prediction performance by better representing spatial variability and showing strong potential for enhancing prediction accuracy (Sardar et al. 2021). 

In general, drought prediction approaches can be categorized into Stochastic time-series models (AutoRegressive Integrated Moving Average (ARIMA), Seasonal Autoregressive Integrated Moving Average (SARIMA) that capture temporal persistence and seasonality), dynamic models (Global Circulation Model), index-based approaches (Index-based class), and data-driven ML/DL models that learn nonlinear relationships from multi-source predictors (Box 2013; Breiman 2001; Park et al. 2019; Sardar et al. 2021; Tian et al. 2013, 2016) (Table 10). When integrated with GIS-based spatial analysis, these approaches enhance agricultural drought early warning systems by improving predictive skills and supporting informed decision-making across various spatial scales (Ahmad et al. 2010; Chen et al. 2012; Moody and Darken 1989; Tian et al., 2018). 

### **8 Discussions** 

Numerous recent studies have explored historical drought events worldwide. Mitigating the effects of drought and other extreme weather events requires timely and reliable information, which is crucial for decision-making (Mullapudi et al. 2023). Recent developments in geospatial technology and data computing have led to a notable increase in research focusing on the multivariate monitoring and modeling of agricultural drought. This comprehensive study examines the recent progress in this field, encompassing the application of multisource remote sensing data, various machine learning models, and big data approaches. Agricultural drought modelling essentially encompasses three significant components: descriptive modelling of drought characteristics (onset, intensity, and termination), multivariate predictive modelling of drought intensity, and multivariate risk mapping (Houmma et al. 2022). 

A diverse range of multi-sensor approaches to agricultural drought modeling have been developed and tested around the world based on the integration of earth observation data with other data sources using various machine learning applications (Kan et al. 2023; Qin et al. 2021; Rahmati et al. 2020; Sandeep et al. 2021). Different researchers have employed various remote sensing-based indicators to monitor and analyze agricultural drought in their respective 

```
1 3
```

**<mark>222</mark>** <mark>Page 18 of 28</mark> 

S. Mondal et al. 

|Reference|(Başakın et al.<br>2021)<br>i<br>(Aghelpour et<br>al.2021)|(Malik et al.<br>2021)|(Rezaei et al.<br>2025)<br>(Xu et al.<br>2024)<br>(Raza et al.<br>2025)<br>(Kan et al.<br>2023)<br>(Achite et al.<br>2022)<br>(Elbeltagi et<br>al.2023)<br>(Mohammed<br>et al.2022)<br>(Park et al.<br>2019)<br>(Park et al.<br>2018)<br>(Achite et al.<br>2023)<br>(Tian et al.,<br>2018)<br>(Mokhtarzad<br>et al.2017)<br>(Deo and<br>Sahin2015)|
|---|---|---|---|
|Key limitation|e<br>High computational cost and<br>results depend strongly on<br>decomposition settings (mode<br>selection)<br>e<br>Optimization can be slow/<br>unstable and may overfit if the<br>validation strategy is weak|<br>e<br>Computationally heavy;<br>performance sensitive to<br>optimizer hyperparameters<br>and search space|Metaheuristic optimization<br>may converge inconsistently<br>and increase model complex-<br>ity/replicability issues<br> <br>d<br>Increased complexity makes<br>interpretation difficult and<br>may lead to over-optimization<br>without real physical meaning<br>d<br>Single trees easily overfit,<br>leading to unstable drought<br>predictions across regions<br>r<br>Less effective for long<br>lead-time forecasting, and<br>interpretability is still limited<br>compared to simple models<br>Sensitive to kernel/parameter<br>choice; weak scalability for<br>very large spatiotemporal<br>datasets<br>i-<br>Needs large training samples<br>and careful regularization;<br>prone to overfitting|
|Main strength|Decomposes non-stationary<br>drought time series into simpler<br>components, thereby enhancing th<br>stability of ANFIS predictions<br>,<br>Metaheuristic tuning improves<br>SVM parameter selection, often<br>achieving higher accuracy than th<br>default SVM|.<br>Strong for nonlinear drought fore-<br>casting; hybrid optimizers improv<br>SVR generalization and reduce<br>manual tuning|,<br>Automatic hyperparameter<br>optimization improves model<br>performance and reduces subjec-<br>tive tuning<br>Improves robustness and accuracy<br>by combining multiple learners an<br>reduces single-model bias<br> <br>Highly interpretable, useful for<br>identifying key drought drivers an<br>thresholds<br>Strong performance with nonlinea<br>relationships, handles mixed<br>predictors, and provides feature<br>importance<br>,<br>2,<br>Strong performance with limited<br>samples and high-dimensional<br>drought predictors<br> <br>Learns nonlinear relationships<br>between drought indices and mult<br>source predictors<br>,|
|<br>Accuracy of the Models|NSE = 0.96, MSE = 0.18<br>RMSE = 0.817,<br>NRMSE = 0.097, WI = 0.940<br>_R_= 0.889|RMSE = 0.535–0.965,<br>MAE = 0.363–0.622,<br>NSE = 0.558–0.860,<br>COC = 0.760–0.930,<br>WI = 0862–0959)|..<br>RMSE = 0.012,<br>MARE = 0.178,<br>BIAS = − 0.069, NSE = 0.804<br>WI = 0.780, CI 0.627<br>The CBR Model has higher<br>accuracy with R2= 0.9065<br>The voting ensemble outper-<br>formed with the highest F1<br>score of 84.80%.<br>MAE = 11.95, R2= 0.59<br>RMSE = 0.28, MAE = 0.19,<br>NSE = 0.86, R2= 0.90<br>_R_= 0.961, MAE = 0.361,<br>RMSE = 0.538<br>_R_= 0.91, MAE = 0.30,<br>RMSE = 0.42, RAE = 36.45,<br>RRSE = 40.29<br>RMSE = 0.382, MAE = 0.375<br>R2 = 0.58<br>_R_= 0.70 RMSE = 0.133<br>CC = 0.908, MAE = 0.305,<br>RMSE = 0.431, RAE = 37.41<br>RRSE = 41.963<br>MAPE = 0.218,<br>RMSE = 0.275, NSE = 0.886<br>RMSE = 0.08125,_R_= 0.9237<br>MAE = 0.602, RMSE = 0.172<br>CD = 0.578,WI = 0.92|
|Application<br>Area|<br>Turkey<br>Iran|India|Iran<br>Chaina<br>Pakistan<br>Sweden<br>Algeria<br>India<br>Syria<br>Kenya<br>East Asia<br>Algeria<br>China<br>Iran<br>Australia|
|Drought Index<br>used|self-calibrated<br>Palmer Drought<br>Severity Index<br>(sc-PDSI)<br>PDSI|EDI|ASPI<br>SPEI<br>Drought<br>detection<br>PDSI<br>Standardized<br>rainfall/runoff<br>Index (SRI)<br>SPI<br> <br>SPI<br>SMI<br>VSDI with<br>MJO and VSDI<br>without MJO<br>SPI<br>SPEI<br>SPI<br>EVI|
|Application|Prediction of meteorological<br>drought indices<br>Agriculture drought<br>prediction|Predict meteorological<br>drought|Agriculture drought<br>prediction<br>19 individual ML models<br>with a stacking ensemble<br>approach to predict<br>Combines 6 ML models with<br>ensemble methods (Bagging<br>and Voting)<br>Prediction of agricultural<br>drought indicators<br>Hydrological drought<br>prediction<br>Drought Prediction<br>Agriculture and Hydrological<br>Drought Prediction<br>Predicting drought severity<br>sites<br>short-period drought<br>prediction<br>Drought forecasting<br>Agriculture drought<br>prediction<br>Drought forecasting<br>Drought Prediction|
|Algorithms<br>Model/Technique|Hybrid Model<br>Empirical Mode Decompo-<br>sition-Adaptive Neuro-<br>Fuzzy Inference System<br>(EMD-ANFIS)<br>Support Vector Machine-<br>Dragonfly Algorithm<br>(SVM-DA)|Hybrid SVR with Particle<br>Swarm Optimization (PSO)<br>and Harris Hawks Optimiza-<br>tion (HHO) algorithm|ANN-Pelican optimization<br>algorithm(POA), ANFIS-<br>POA, and SVM-POA<br>Machine Learn-<br>ing (ML)<br>Ensemble ML<br>Decision Tree (DT)<br>Random Forest (RF)<br>Support Vector Machine<br>(SVM)<br>Artificial Neural Network<br>(ANN)|



```
1 3
```

<mark>Page 19 of 28</mark> **<mark>222</mark>** 

Advancements in Spatio-temporal agricultural drought monitoring and modeling: a comprehensive review on… 

|Reference|<br>fi<br>(Chandra et al.<br>2025)<br>(Abbes et al.<br>2023)<br> <br>(Sardar et al.<br>2021)<br>(Chaudhari et<br>al.2021)<br>(Agana and<br>Homaifar<br>2017)<br>(Hong and<br>Hong2015)<br>(Malik et al.<br>2020)<br>(Özger et al.<br>2012)<br> <br>(Tian et al.<br>2016)<br>t<br> <br> <br>(Mossad and<br>Alazba2015)<br>(Han et al.<br>2013)|
|---|---|
|Key limitation|<br>Requires substantial data and<br>computing resources; difficult<br>to interpret and sensitive to<br>sequence design<br> <br>Needs large labelled datasets;<br>weak for pure temporal fore-<br>casting unless coupled with<br>sequence models<br>Easily becomes a black-box,<br>making scientific justifica-<br>tion difficult for drought<br>decision-making<br> <br>Membership rule design<br>is subjective, with limited<br>scalability for large-scale,<br>real-time drought analytics<br>s<br>Performance drops when<br>drought patterns become<br>non-stationary due to climate<br>variability/change<br> <br>g<br>Weak under nonlinear drough<br>behavior and cannot integrate<br>multi-source RS/climate driv-<br>ers well|
|Main strength|Best suited for drought time-series<br>forecasting because it learns long-<br>term dependencies and lag effects<br>Excellent for extracting spatial<br>drought patterns directly from RS<br>imagery<br> <br>Strong baseline deep model for<br>multivariate drought prediction<br>with RS and climate predictors<br> <br>Handles uncertainty well and<br>produces human-readable drought<br>rules (useful for early warning)<br>Strong for seasonal drought indice<br>(SPI/SPEI) time series with clear<br>periodicity<br>Strong baseline for linear drought<br>index forecasting (SPI/SPEI) usin<br>past values|
|n<br>Accuracy of the Models|_R_= 0.82, MAE = 0.19,<br>RMSE = 0.33<br>_R_= 0.92, MAPE = 9.246,<br>RMSE = 0.03, Bias = 0.00512<br>improved accuracy up to 96%<br>Overall accuracy of all indi-<br>ces is 0.89.<br>R2= 0.91302, MSE = 0.00303,<br>RMSE = 0.05507,<br>MAE = 0.03969<br>_R_= 0.94, MAE = 0.28, RMSE<br>= 0.34<br>Prediction accuracy is higher<br>for all time scales<br>NSSS = 0.903, CC = 0.951<br>RMSE = 0.0818<br>R2= 0.974, RMSE = 0.180,<br>MAE = 0.121<br>_R_= 0.985|
|Applicatio<br>Area|India<br>Iran<br>India<br> <br>Ethiopia<br>USA<br>Malaysia<br>India<br>USA<br>China<br>Saudi<br>Arabia<br>China|
|Drought Index<br>used|SPI, SPEI,<br>PDSI, NDVI/<br>VCI<br>SPEI, NDVI,<br>and meteoro-<br>logical data<br>NDVI<br>NDVI, SAVI,<br>EVI, and<br>Atmospherically<br>Resistant Veg-<br>etation Index<br>(ARVI)<br>or<br>Standardized<br>Streamflow<br>Index (SSI)<br>SPI<br>SPI<br>PDSI, Palmer<br>Modified<br>Drought Index<br>(PMDI)<br>VTCI<br>SPEI<br>SPI|
|Application|Agriculture drought<br>forecasting<br>Drought forecasting<br> <br>Agriculture drought<br>prediction<br>Drought prediction<br>Predict long-term drought f<br>drought monitoring<br>Drought forecasting<br>Drought index prediction<br>Long-term drought<br>forecasting<br>Agriculture drought<br>forecasting<br>Drought forecasting in a<br>hyper-arid climate<br>Drought forecasting|
|Model/Technique|<br>Long Short-Term Memory<br>(LSTM)<br>Convolution Neural Network<br>(CNN)<br>Deep Multilayer Perceptron<br>(MLP)<br>Fuzzy Logic<br>Seasonal Autoregressive<br>Integrated Moving Average<br>(SARIMA)<br>Autoregressive Integrated<br>Moving Average (ARIMA)|
|Algorithms|Deep Learning<br>Fuzzy/Neuro<br>fuzzy<br>Statistical/<br>Time-series|



```
1 3
```

**<mark>222</mark>** <mark>Page 20 of 28</mark> 

S. Mondal et al. 

study areas (Aswathi et al. 2018; Hazaymeh and Hassan 2017; Naskar 2022; Tang and Li 2014). The integration of multiple drought indices or CDI enhances the ability to accurately detect both global and local drought events. CDI is a technique that integrates multiple variables and aims to reconstruct quantitative and qualitative information for assessing and monitoring drought. Bayissa et al. (2022) developed an agricultural combined drought index (agCDI) using a principal component analysis (PCA) approach to monitor and characterize the spatial and temporal patterns of drought in Sri Lanka, employing satellite-based indices to mitigate the adverse impacts in the area. 

Similarly, Chattopadhyay et al. (2020) utilized meteorological, land-based, and remote sensing observation data to develop CDI using a weightage overlay analysis in India. Other CDIs, such as the Vegetation Drought Response Index (VegDRI), were developed by Brown et al. (2008). Rojas (2021) utilized the Agricultural Stress Index System (ASIS), while Liu et al. (2020) developed an ANN-based Integrated Agricultural Drought Index (IADI), among other methods, to identify areas vulnerable to agricultural drought. Even though many researchers are now using multiple ML techniques to predict drought using various hydroclimatic and RS data, this suggests that multivariate composite models can provide valuable insights into different forms of drought simultaneously. The potential disadvantage of these models is that they require multiple datasets, which often have quite different characteristics, necessitating normalization and downscaling treatments (Houmma et al. 2022). On the other hand, multiple dimensions of agricultural drought have been described and/or simulated using both machine learning and deep learning models. 

The application of ML, hybrid models, and big data is an increasingly popular trend in drought modelling. Every study employs a distinct technique in terms of the choice of response variable and the algorithm used to assess the relative importance of variables or indices in the multivariate models developed by Houmma et al. (2022). Multivariate predictive analyses offer a practical approach to mapping expected risks, including their intensity and spatial distribution (Rahmati et al. 2020). A significant number of ML/DL algorithm-based models have been used (Aghelpour et al. 2021; Fung et al. 2020; Tian et al., 2018). Bali and Singla (2021) recently demonstrated considerable support for the movement toward increased use of hybrid models and deep learning for prediction, particularly of crop yields. To address this, Tian et al. (2018) analyzed the relation between soil moisture and drought, and predicted agricultural drought in the Xiangjiang River basin, China. They developed an SVR model to predict agricultural droughts using climate indices. Simultaneously, LSTM has been utilized by Kheyruri et al. (2023) based on large-scale indicators (big data), such as 

El Niño-Southern Oscillation (ENSO), NDVI, and meteorological parameters, at time lags of 1–4 months to understand the predictors of agricultural drought. They revealed NDVI values predicting better performance in semi-arid and arid areas of Iran. Similar work has been conducted (Sardar et al. 2021) to predict drought or no-drought conditions using a CNN model based on NDVI from satellite images in Karnataka, India, achieving 96% accuracy. Additionally, numerous scientific studies have been conducted to compare various types of ML and DL models for analyzing agricultural drought. For example, Kan et al. (2023) compared seven ML/DL models, namely RF, decision tree (DT), multivariate linear regression (MLR), SVR, ARIMA, ANN, and CNN, in combination with the indicators of soil moisture and PDSI. The best-performing models for predicting soil moisture were the multi-feature RF model (better suited for national-scale prediction) and the temporal ARIMA model (best suited for local-scale prediction), and all these models performed better than PDSI. In another work, the applicability of four ML algorithms, such as bagging, random subspace (RSS), random tree, and RF, has been used by Mohammed et al. (2022) in predicting drought events in the eastern Mediterranean based on SPI-3 and SPI-12. They obtained results from the bagging algorithm, which outperformed the other algorithms and is more dynamic in capturing drought. Roushangar et al. (2021) suggested that integrated models might perform noticeably better than single models, improving predictive modeling accuracy by up to 40% and 50%. However, deep learning models for drought prediction still face challenges, particularly in delivering accurate long-range forecasts and high-resolution spatial outputs, and in their reliance on large amounts of data, which are often insufficient in many regions of the world (Gyaneshwar et al. 2023). 

To overcome the problem, large, long-term datasets (big data) can be used for agricultural drought analysis, especially in combination with hybrid and physics-based machine learning and deep learning approaches, leveraging higher-temporal- and spatial-resolution satellite data. Further, the emerging technologies such as UAV-based high-resolution data, high-precision field-based sensors, affordable cloud computing platforms, and integration through Internet of Things (IoT) have enabled researchers to monitor agricultural drought spatiotemporally at finer resolution and to develop an early warning system (Anandan et al. 2024; da Silva et al. 2025; Dahir et al. 2023; Fei et al. 2023; Masupha et al. 2025; Yang et al. 2024). Further, Artificial Intelligence (AI) could be explored to enhance the accuracy of agricultural predictive modelling, as it resembles biological processes and operates on logical systems such as sentential and predicate logic (Kikon and Deka 2022; Oyarzabal et al. 2025). Moreover, these 

```
1 3
```

<mark>Page 21 of 28</mark> **<mark>222</mark>** 

Advancements in Spatio-temporal agricultural drought monitoring and modeling: a comprehensive review on… 

advancements are directly linked to the achievement of the United Nations SDGs, particularly SDG 2 (Zero Hunger) through safeguarding food security, SDG 6 (Clean Water and Sanitation) by ensuring sustainable water management, SDG 13 (Climate Action) by enhancing resilience against climate-related hazards, and SDG 15 (Life on Land) through the promotion of sustainable agriculture and the prevention of land degradation (Efremova et al. 2023; Jain and Mitra 2025; Mandal et al. 2025; Nan et al. 2025; Zaigham Abbas Naqvi et al., 2025; Ziesche et al. 2023). 

### **9 Conclusion** 

Agriculture is the most sensitive and vulnerable sector, and it is strongly affected by rainfall variability and drought. Agricultural drought monitoring and modelling remain challenging because drought is driven by complex interactions among hydroclimatic, environmental, and human factors, which ultimately influence ecosystems, hydrology, socioeconomics, and food security. Although drought impacts cannot be fully avoided, improved monitoring and early warning can substantially reduce losses. But the inconsistent high spatial resolution and long-term data are the major obstacles. This paper provides a critical review of the details of various agricultural drought indices and techniques for monitoring and modeling using multi-source remote-sensing satellite data and ML- and DL-based geospatial approaches. This paper outlines the fundamental concepts of drought, its various types, and their impact. The review identifies that among various remote sensing spectral indices, NDVI, SMA, VCI, and VHI are widely used to characterize agricultural drought. Similarly, precipitationbased indices, such as the SPI and the SPEI, are among the most widely used indicators for drought assessment and prediction. We further found that the MODIS and Landsat datasets are the most widely used remote sensing datasets for drought assessment due to their long-term continuity and accessibility. 

Beyond summarizing the existing literature, this review highlights that the choice of drought indices and satellite data is highly context-dependent, and that multi-index integration is consistently more robust than single-index drought mapping. In drought modeling and forecasting, methods such as RF, ANN, SVM, LSTM, CNN, ANFIS, and MLP are widely adopted, but their performance often depends more on input feature selection, lag design, validation strategy, and spatial transferability than on the algorithm itself. The literature also indicates that drought research increasingly covers both static drought classification and advanced probabilistic, predictive, and near-real-time early warning systems supported by ML and DL approaches. Future 

research should prioritize high-resolution soil moisture estimation, especially for root-zone conditions, as it plays a crucial role in agricultural drought monitoring and crop yield assessment. The development of advanced and innovative Physics-guided and hybrid ML approaches is also necessary to improve generalization and reliability under climate non-stationarity. Additionally, it should focus on integrating drought monitoring with impact assessment, including crop yield-loss modeling and vulnerability/risk mapping. 

**Acknowledgements** The first author would like to acknowledge the University Grants Commission, Government of India, for providing a fellowship to pursue his doctoral research. 

**Author contributions** Conceptualization: Suresh Mondal, Kumar Arun Prasad; Methodology: Suresh Mondal, Kumar Arun Prasad; Literature search and data analysis: Suresh Mondal; Writing - original draft preparation: Suresh Mondal; Writing - review and editing: Suresh Mondal, Kumar Arun Prasad, Achu A. L., S. Kaliraj, and K. Balasubramani; Supervision: Kumar Arun Prasad. All authors read and approved the final version of the manuscript. 

**Funding** The authors declare that no funds, grants, or other support were received during the preparation of this manuscript. 

**Data availability** Data availability is not applicable as no datasets were generated or analyzed during the current study. 

#### **Declarations** 

**Competing interests** The authors declare no competing interests. 

### **References** 

- Aadhar S, Mishra V (2017) High-resolution near real-time drought monitoring in South Asia. Sci Data 4(1):170145.  h t t p s : / / d o i . o r g / 1 0 . 1 0 3 8 / s d a t a . 2 0 1 7 . 1 4 5 

- Abbes AB, Inoubli R, Rhif M, Farah IR (2023) Combining deep learning methods and multi-resolution analysis for drought forecasting modeling. Earth Sci Inform 16(2):1811–1820.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 2 1 4 5 - 0 2 3 - 0 1 0 0 9 - 4 

- Achite M, Jehanzaib M, Elshaboury N, Kim TW (2022) Evaluation of machine learning techniques for hydrological drought modeling: a case study of the Wadi Ouahrane basin in Algeria. Water.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / w 1 4 0 3 0 4 3 1 

- Achite M, Elshaboury N, Jehanzaib M, Vishwakarma DK, Pham QB, Anh DT, Abdelkader EM, Elbeltagi A (2023) Performance of machine learning techniques for meteorological drought forecasting in the Wadi Mina Basin, Algeria. Water 15(4):4.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / w 1 5 0 4 0 7 6 5 

- AFDM-Princeton University. (n.d.). African Flood and Drought Monitor. Retrieved January 15 (2026) from  h t t p s : / / h y d r o l o g y . s o t o n . a c . u k / a p p s / a f d m / 

- Agana NA, Homaifar A (2017) A deep learning based approach for long-term drought prediction. SoutheastCon 2017, 1–8.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / S E C O N . 2 0 1 7 . 7 9 2 5 3 1 4 

- AghaKouchak A, Farahmand A, Melton FS, Teixeira J, Anderson MC, Wardlow BD, Hain CR (2015) Remote sensing of drought: progress, challenges and opportunities. Rev Geophys 53(2):452–480. h t t p s : / / d o i . o r g / 1 0 . 1 0 0 2 / 2 0 1 4 R G 0 0 0 4 5 6 

```
1 3
```

**<mark>222</mark>** <mark>Page 22 of 28</mark> 

S. Mondal et al. 

- Aghelpour P, Mohammadi B, Mehdizadeh S, Bahrami-Pichaghchi H, Duan Z (2021) A novel hybrid dragonfly optimization algorithm for agricultural drought prediction. Stoch Environ Res Risk Assess 35(12):2459–2477.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 0 0 4 7 7 - 0 2 1 - 0 2 0 1 1 - 2 

- Ahady AB, Klopries E-M, Schüttrumpf H, Wolf S (2025) Drought analysis methods: a multidisciplinary review with insights on key decision-making factors in method selection. Water 17(15):2248. h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / w 1 7 1 5 2 2 4 8 

- Ahmad S, Kalra A, Stephen H (2010) Estimating soil moisture using remote sensing data: a machine learning approach. Adv Water Resour 33(1):69–80. h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . a d v w a t r e s . 2 0 0 9 . 1 0 . 0 0 8 

- Ahmad U, Alvino A, Marino S (2021) A review of crop water stress assessment using remote sensing. Remote Sens 13(20):4155 

- Ajaz A, Taghvaeian S, Khand K, Gowda PH, Moorhead JE (2019) Development and evaluation of an agricultural drought index by harnessing soil moisture and weather data. Water 11(7):7.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / w 1 1 0 7 1 3 7 5 

- Alahacoon N, Edirisinghe M (2022) A comprehensive assessment of remote sensing and traditional based drought monitoring indices at global and regional scale. Geomat Nat Hazards Risk 13(1):762–799.  h t t p s : / / d o i . o r g / 1 0 . 1 0 8 0 / 1 9 4 7 5 7 0 5 . 2 0 2 2 . 2 0 4 4 3 9 4 

- Alley WM (1984) The palmer drought severity index: limitations and assumptions. J Appl Meteorol Climatol 23(7):1100–1109 

- Amani M, Ghorbanian A, Asgarimehr M, Yekkehkhany B, Moghimi A, Jin S, Naboureh A, Mohseni F, Mahdavi S, Layegh NF (2021) Remote sensing systems for ocean: a review (Part 1: passive systems). IEEE J Sel Top Appl Earth Observations Remote Sens 15:210–234 

- Anandan P, Saillaja V, Kovarasan RK, Padmaloshani P, VIM, Rajmohan M (2024) Enhanced Water Security and Resilience in Drought-Prone Zones with IoT and SVM classifier for Early Warning Systems. 2024 Int Conf Adv Mod Age Technol Health Eng Sci (AMATHE) 1(5).  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / A M A T H E 6 1 6 5 2 . 2 0 2 4 . 1 0 5 8 2 0 8 3 

- Aryal A, Maharjan M, Talchabhadel R, Thapa BR (2022) Characterizing meteorological droughts in Nepal: a comparative analysis of standardized precipitation index and rainfall anomaly index. Earth 3(1):409–432 

- Aswathi PV, Nikam B, Chouksey A, Aggarwal SP (2018) Assessment and monitoring, of agricultural, droughts in maharashtra using meteorological and remote sensing based indices. ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Information Sciences. h t t p s : / / w w w . s e m a n t i c s c h o l a r . o r g / p a p e r / A S S E S S M E N T - A N D - M O N I T O R I N G - O F - A G R I C U L T U R A L - D R O U G H T S - A s w a t h i - N i k a m / c d a d 7 a 4 a 0 2 0 9 3 5 5 6 b 4 e e 0 9 e 5 c 9 8 1 0 4 8 a 0 8 b f 2 f 9 5 

- Ayugi B, Eresanya EO, Onyango AO, Ogou FK, Okoro EC, Okoye CO, Anoruo CM, Dike VN, Ashiru OR, Daramola MT, Mumo R, Ongoma V (2022) Review of meteorological drought in Africa: historical trends, impacts, mitigation measures, and prospects. Pure Appl Geophys 179(4):1365–1386. h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 0 0 0 2 4 - 0 2 2 - 0 2 9 8 8 - z 

- Bablet A, Vu PVH, Jacquemoud S, Viallefont-Robinet F, Fabre S, Briottet X, Sadeghi M, Whiting ML, Baret F, Tian J (2018) Marmit: a multilayer radiative transfer model of soil reflectance to estimate surface soil moisture content in the solar domain (400–2500 nm). Remote Sens Environ 217:1–17.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . r s e . 2 0 1 8 . 0 7 . 0 3 1 

- Balew A, Legese B, Semaw F (2021) A Review of Some Indices Used for Drought Monitoring.  h t t p s : / / c o r e . a c . u k / d o w n l o a d / p d f / 4 8 1 6 0 9 1 0 3 . p d f 

- Bali N, Singla A (2021) Emerging trends in machine learning to predict crop yield and study its influential factors: a survey. Arch Comput Methods Eng.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 1 8 3 1 - 0 2 1 - 0 9 5 6 9 - 8 

- Balsamo G, Agusti-Parareda A, Albergel C, Arduini G, Beljaars A, Bidlot J, Blyth E, Bousserez N, Boussetta S, Brown A (2018) Satellite and in situ observations for advancing global Earth surface modelling: a review. Remote Sens 10(12):2038 

- Balti H, Abbes AB, Mellouli N, Farah IR, Sang Y, Lamolle M (2020) A review of drought monitoring with big data: issues, methods, challenges and research directions. Ecol Informatics 60:101136 

- Baret F, Guyot G (1991) Potentials and limits of vegetation indices for LAI and APAR assessment. Remote Sens Environ 35(2):161– 173.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / 0 0 3 4 - 4 2 5 7 ( 9 1 ) 9 0 0 0 9 - U 

- Başakın EE, Ekmekcioğlu Ö, Özger M (2021) Drought prediction using hybrid soft-computing methods for semi-arid region. Model Earth Syst Environ 7(4):2363–2371. h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 4 0 8 0 8 - 0 2 0 - 0 1 0 1 0 - 6 

- Bayissa Y, Srinivasan R, Joseph G, Bahuguna A, Shrestha A, Ayling S, Punyawardena R, Nandalal KDW (2022) Developing a combined drought index to monitor agricultural drought in Sri Lanka. Water 14(20):3317.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / w 1 4 2 0 3 3 1 7 

- Belal A, El-Ramady H, Mohamed E, Saleh A (2012) Drought risk assessment using remote sensing and GIS techniques. Arab J Geosci.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 2 5 1 7 - 0 1 2 - 0 7 0 7 - 2 

- Bodner G, Nakhforoosh A, Kaul H-P (2015) Management of crop water under drought: a review. Agron Sustain Dev 35:401–442 

- Boken VK, Cracknell AP, Heathcote RL (2004) Monitoring and predicting agricultural drought: A global study. Oxford University Press 

- Bowell A, Salakpi EE, Guigma K, Muthoka JM, Mwangi J, Rowhani P (2021) Validating commonly used drought indicators in Kenya. Environ Res Lett 16(8):084066.  h t t p s : / / d o i . o r g / 1 0 . 1 0 8 8 / 1 7 4 8 - 9 3 2 6 / a c 1 6 a 2 

- Box G (2013) Box and Jenkins: Time Series Analysis, Forecasting and Control. In T. C. Mills (Ed.), A Very British Affair: Six Britons and the Development of Time Series Analysis During the 20th Century (pp. 161–215). Palgrave Macmillan UK.  h t t p s : / / d o i . o r g / 1 0 . 1 0 5 7 / 9 7 8 1 1 3 7 2 9 1 2 6 4 _ 6 

- Breiman L (2001) Random Forests. Mach Learn 45(1):5–32.  h t t p s : / / d o i . o r g / 1 0 . 1 0 2 3 / A : 1 0 1 0 9 3 3 4 0 4 3 2 4 

- Brown J, Wardlow B, Tadesse T, Hayes M, Reed B (2008) The vegetation drought response index (VegDRI): a new integrated approach for monitoring drought stress in vegetation. GISci Remote Sens 45:16–46.  h t t p s : / / d o i . o r g / 1 0 . 2 7 4 7 / 1 5 4 8 - 1 6 0 3 . 4 5 . 1 . 1 6 

- Carlson T, Gillies R, Perry E (1994) A method to make use of thermal infrared temperature and NDVI measurements to infer surface soil water content and fractional vegetation cover. Remote Sens Rev 9:161–173.  h t t p s : / / d o i . o r g / 1 0 . 1 0 8 0 / 0 2 7 5 7 2 5 9 4 0 9 5 3 2 2 2 0 

- Chakraborty A, Sehgal V (2010) Assessment of agricultural drought using MODIS derived normalized difference water index. J Agric Phys 10:28–36 

- Chandra V, Rao S, Subrahmanyam V, Pulyala R, Shireesha P (2025) Spatio-Temporal Deep Learning Models for Forecasting Agricultural Drought in Rain-Fed Regions. 11, 2025 

- Chandramohan K, Elayapillai P, Vijayalakshmi G, Kaliraj S (2024) Chapter 43—Evaluating the relation of NDVI, NDWI, SMI, and LAI to land and soil degradation processes—A case study of Virudhunagar district, Tamil Nadu, India. In S. Dharumarajan, S. Kaliraj, K. Adhikari, M. Lalitha, & N. Kumar (Eds.), Remote Sensing of Soils (pp. 689–697). Elsevier.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / B 9 7 8 - 0 - 4 4 3 - 1 8 7 7 3 - 5 . 0 0 0 4 0 - 5 

- Chattopadhyay N, Malathi K, Tidke N, Attri SD, Ray K (2020) Monitoring agricultural drought using combined drought index in India. J Earth Syst Sci 129(1):155. h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 2 0 4 0 - 0 2 0 - 0 1 4 1 7 - w 

- Chaudhari S, Sardar V, Rahul DS, Chandan M, Shivakale MS, Harini KR (2021) Performance Analysis of CNN, AlexNet and VGGNet Models for Drought Prediction using Satellite Images. 2021 

```
1 3
```

<mark>Page 23 of 28</mark> **<mark>222</mark>** 

Advancements in Spatio-temporal agricultural drought monitoring and modeling: a comprehensive review on… 

   - Asian Conference on Innovation in Technology (ASIANCON), 1–6.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / A S I A N C O N 5 1 3 4 6 . 2 0 2 1 . 9 5 4 5 0 6 8 

- Chen J, Li M, Wang W (2012) Statistical uncertainty estimation using random forests and its application to drought forecast. Mathematical Problems in Engineering, 2012.  h t t p s : / / w w w . h i n d a w i . c o m / j o u r n a l s / m p e / 2 0 1 2 / 9 1 5 0 5 3 / a b s / 

- Chere Z, Debalke DB (2024) Modeling agricultural drought based on the earth observation-derived standardized precipitation evapotranspiration index and vegetation health index in the northeastern highlands of Ethiopia. Nat Hazards 120(3):3127–3151.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 1 0 6 9 - 0 2 3 - 0 6 3 2 0 - 3 

- Chowdhury A, Gore PG (1989) An index to assess agricultural drought in India. Theor Appl Climatol 40:103–109 

- CIIFEN. (n.d.). Centro Internacional para la Investigación del Fenómeno de El Niño. Retrieved January 15 (2026) from h t t p s : / / c i i f e n . o r g / ? o p t i o n = c o m _ content&view=article&id = 2172& Itemid = 469 ⟨ = es 

- Claps P, Laguardia G (2004) Assessing spatial variability of soil water content through Thermal Inertia and NDVI. Proc SPIE - Int Soc Opt Eng 5232.  h t t p s : / / d o i . o r g / 1 0 . 1 1 1 7 / 1 2 . 5 1 0 9 8 4 

- Cohen-Cline H, Turkheimer E, Duncan G (2015) Access to green space, physical activity and mental health: a twin study. J Epidemiol Community Health. h t t p s : / / d o i . o r g / 1 0 . 1 1 3 6 / j e c h - 2 0 1 4 - 2 0 4 6 6 7 

- CSIC. (n.d.). SPEI Global Drought Monitor. Retrieved January 15 (2026) from h t t p s : / / s p e i . c s i c . e s / m a p / m a p s . h t m l . m o n t h s . 1 . m o n t h . 1 0 . y e a r . 2 0 2 5 

- da Silva TL, Romani LAS, Evangelista SRM, Datcu M, Massruhá SMFS (2025) Drought monitoring in the Agrotechnological Districts of the Semear Digital Center. Atmosphere 16(4):465.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / a t m o s 1 6 0 4 0 4 6 5 

- Dahir A, Omar M, Abukar Y (2023) Internet of things based agricultural drought detection system: case study Southern Somalia. Bull Electr Eng Inf 12(1):69–74.  h t t p s : / / d o i . o r g / 1 0 . 1 1 5 9 1 / e e i . v 1 2 i 1 . 4 1 1 7 

- Dalezios N, Bampzelis D, Domenikiotis C (2009) An integrated methodological procedure for alternative drought mitigation in Greece 

- Deo R, Sahin M (2015) Application of the extreme learning machine algorithm for the prediction of monthly effective drought index in eastern Australia. Atmos Res. h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . a t m o s r e s . 2 0 1 4 . 1 0 . 0 1 6 

- Dingman SL (2002) Physical Hydrology’Prentice Hall, Upper Saddle River. Waveland, New Jersey (US) 

- Dixon GR (2015) Water, irrigation and plant diseases. CABI Reviews 1–18.  h t t p s : / / d o i . o r g / 1 0 . 1 0 7 9 / P A V S N N R 2 0 1 5 1 0 0 0 9 

- Docheshmeh Gorgij A, Alizamir M, Kisi O, Elshafie A (2022) Drought modelling by standard precipitation index (SPI) in a semi-arid climate using deep learning method: long short-term memory. Neural Comput Appl 34(3):2425–2442. h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 0 0 5 2 1 - 0 2 1 - 0 6 5 0 5 - 6 

- Dutta R (2018) Drought monitoring in the dry zone of Myanmar using MODIS derived NDVI and satellite derived CHIRPS precipitation data. Sustain Agric Res 7:46.  h t t p s : / / d o i . o r g / 1 0 . 5 5 3 9 / s a r . v 7 n 2 p 4 6 

- EC, & JRC. (n.d.). _European Drought Observatory (EDO)_ . Retrieved January 15, (2026) from  h t t p s : / / d r o u g h t . e m e r g e n c y . c o p e r n i c u s . e u / t u m b o / e d o / m a p / ? i d = 1 0 0 0 

- Efremova N, Foley JC, Unagaev A, Karimi R (2023) AI for Sustainable Agriculture and Rangeland Monitoring. In F. Mazzi & L. Floridi (Eds.), _The Ethics of Artificial Intelligence for the Sustainable Development Goals_ (pp. 399–422). Springer International Publishing.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / 9 7 8 - 3 - 0 3 1 - 2 1 1 4 7 - 8 _ 2 2 

- Ekmekcioğlu Ö (2023) Drought forecasting using integrated variational mode decomposition and extreme gradient boosting. Water 15(19):3413.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / w 1 5 1 9 3 4 1 3 

- Elbeltagi A, Pande CB, Kumar M, Tolche AD, Singh SK, Kumar A, Vishwakarma DK (2023) Prediction of meteorological drought and standardized precipitation index based on the random forest (RF), random tree (RT), and Gaussian process regression (GPR) models. Environ Sci Pollut Res 30(15):43183–43202.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 1 3 5 6 - 0 2 3 - 2 5 2 2 1 - 3 

- Engman ET (1991) Applications of microwave remote sensing of soil moisture for water resources and agriculture. Remote Sens Environ 35(2):213–226.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / 0 0 3 4 - 4 2 5 7 ( 9 1 ) 9 0 0 1 3 - V 

- Fei S, Hassan MA, Xiao Y, Su X, Chen Z, Cheng Q, Duan F, Chen R, Ma Y (2023) UAV-based multi-sensor data fusion and machine learning algorithm for yield prediction in wheat. Precis Agric 24(1):187–212.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 1 1 1 9 - 0 2 2 - 0 9 9 3 8 - 8 

- Fioravanti G, Toreti A, Cammalleri C, Muñoz CA, Bavera D, De Jager A, Hrast Essenfelder A, Di Ciollo C, Masante D, Magni D, Navarro JA, Mazzesch M, Maetens W (2025) A dataset for monitoring agricultural drought in Europe. Sci Data 12(1):308.  h t t p s : / / d o i . o r g / 1 0 . 1 0 3 8 / s 4 1 5 9 7 - 0 2 4 - 0 4 1 9 9 - 8 

- Fung KF, Huang YF, Koo CH, Mirzaei M (2020) Improved SVR machine learning models for agricultural drought prediction at downstream of Langat River Basin, Malaysia. J Water Clim Change 11(4):1383–1398.  h t t p s : / / d o i . o r g / 1 0 . 2 1 6 6 / w c c . 2 0 1 9 . 2 9 5 

- Gaikwad SV, Vibhute AD, Kale KV (2022) Assessing meteorological drought and detecting LULC dynamics at a regional scale using SPI, NDVI, and random forest methods. SN Computer Science 3(6):458.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 4 2 9 7 9 - 0 2 2 - 0 1 3 6 1 - 0 

- Gao B (1996) NDWI—A normalized difference water index for remote sensing of vegetation liquid water from space. Remote Sens Environ 58(3):257–266.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / S 0 0 3 4 - 4 2 5 7 ( 9 6 ) 0 0 0 6 7 - 3 

- Gerhards M, Schlerf M, Mallick K, Udelhoven T (2019) Challenges and future perspectives of multi-/Hyperspectral thermal infrared remote sensing for crop water-stress detection: a review. Remote Sens 11(10):1240 

- Ghulam A, Li Z-L, Qin Q, Yimit H, Wang J (2008) Estimating crop water stress with ETM + NIR and SWIR data. Agric For Meteorol 148(11):1679–1695. h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . a g r f o r m e t . 2 0 0 8 . 0 5 . 0 2 0 

- Gitelson AA, Merzlyak MN (1997) Remote estimation of chlorophyll content in higher plant leaves. Int J Remote Sens 18(12):2691–2697 

- Gitelson AA, Viña A, Ciganda V, Rundquist DC, Arkebauer TJ (2005) Remote estimation of canopy chlorophyll content in crops. Geophys Res Lett 32(8):2005GL022688. h t t p s : / / d o i . o r g / 1 0 . 1 0 2 9 / 2 0 0 5 G L 0 2 2 6 8 8 

- Gu Y, Brown JF, Verdin JP, Wardlow B (2007) A five-year analysis of MODIS NDVI and NDWI for grassland drought assessment over the central Great Plains of the United States. Geophys Res Lett.  h t t p s : / / d o i . o r g / 1 0 . 1 0 2 9 / 2 0 0 6 G L 0 2 9 1 2 7 

- Gyaneshwar A, Mishra A, Chadha U, Raj Vincent PMD, Rajinikanth V, Pattukandan Ganapathy G, Srinivasan K (2023) A contemporary review on deep learning models for drought prediction. Sustainability 15(7):7.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / s u 1 5 0 7 6 1 6 0 

- Haddaway NR, Collins AM, Coughlin D, Kirk S (2015) The role of Google Scholar in evidence reviews and its applicability to grey literature searching. PLoS One 10(9):e0138237.  h t t p s : / / d o i . o r g / 1 0 . 1 3 7 1 / j o u r n a l . p o n e . 0 1 3 8 2 3 7 

- Halwatura D, McIntyre N, Lechner AM, Arnold S (2017) Capability of meteorological drought indices for detecting soil moisture droughts. J Hydrology: Reg Stud 12:396–412.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . e j r h . 2 0 1 7 . 0 6 . 0 0 1 

- Han P, Wang P, Tian M, Zhang S, Liu J, Zhu D (2013) Application of the ARIMA Models in Drought Forecasting Using the Standardized Precipitation Index. In D. Li & Y. Chen (Eds.), Computer 

```
1 3
```

**<mark>222</mark>** <mark>Page 24 of 28</mark> 

S. Mondal et al. 

and Computing Technologies in Agriculture VI (pp. 352–358). Springer.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / 9 7 8 - 3 - 6 4 2 - 3 6 1 2 4 - 1 _ 4 2 

Hao Z, AghaKouchak A, Nakhjiri N, Farahmand A (2014) Global integrated drought monitoring and prediction system. Sci Data 1(1):140001.  h t t p s : / / d o i . o r g / 1 0 . 1 0 3 8 / s d a t a . 2 0 1 4 . 1 

- Hassan Q, Bourque C, Meng F-R, Cox R (2007) A wetness index using terrain-corrected surface temperature and normalized difference vegetation index derived from standard MODIS products: an evaluation of its use in a humid forest-dominated region of eastern Canada. Sensors 7:2028–2048. h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / s 7 1 0 2 0 2 8 

- Hazaymeh K, Hassan QK (2017) A remote sensing-based agricultural drought indicator and its implementation over a semi-arid region, Jordan. J Arid Land 9(3):319–330.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 4 0 3 3 3 - 0 1 7 - 0 0 1 4 - 6 

- Holgate CM, Pepler AS, Rudeva I, Abram NJ (2023) Anthropogenic warming reduces the likelihood of drought-breaking extreme rainfall events in southeast Australia. Weather Clim Extremes 42:100607.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . w a c e . 2 0 2 3 . 1 0 0 6 0 7 

- Holzman ME, Rivas RE, Bayala MI (2021) Relationship between TIR and NIR-SWIR as indicator of vegetation water availability. Remote Sens 13(17):17.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / r s 1 3 1 7 3 3 7 1 

- Hong D, Hong KA (2015) Drought Forecasting Using MLP Neural Networks. 2015 8th International Conference on U- and e-Service, Science and Technology (UNESST), 62–65.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / U N E S S T . 2 0 1 5 . 2 3 

- Hou X-X, Liu Y, Zhang X, Ma Q, Shang G (2025) Spatiotemporal dynamics and drivers of agricultural drought in the Huang-HuaiHai Plain based on crop water stress index and spatial machine learning. Remote Sens 17(22):3678.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / r s 1 7 2 2 3 6 7 8 

- Houmma I, Mansouri L, Gadal S, Garba M, Hadria R (2022) Modelling agricultural drought: a review of latest advances in big data technologies. Geomat Nat Hazards Risk 13:2737–2776.  h t t p s : / / d o i . o r g / 1 0 . 1 0 8 0 / 1 9 4 7 5 7 0 5 . 2 0 2 2 . 2 1 3 1 4 7 1 

- Hu T, Renzullo LJ, van Dijk AIJM, He J, Tian S, Xu Z, Zhou J, Liu T, Liu Q (2020) Monitoring agricultural drought in Australia using MTSAT-2 land surface temperature retrievals. Remote Sens Environ 236:111419.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . r s e . 2 0 1 9 . 1 1 1 4 1 9 

- Hulley G, Hook S (2011) Generating consistent land surface temperature and emissivity (LST&E) products between ASTER and MODIS data for earth science research. Geoscience and Remote Sensing, IEEE Transactions On 49:1304–1315.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / T G R S . 2 0 1 0 . 2 0 6 3 0 3 4 

- Hunt ER, Rock BN (1989) Detection of changes in leaf water content using near- and middle-infrared reflectances. Remote Sens Environ 30(1):43–54.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / 0 0 3 4 - 4 2 5 7 ( 8 9 ) 9 0 0 4 6 - 1 

- IRI-Columbia University. (n.d.). International Research Institute for Climate and Society-Global Drought Analysis Tool. Retrieved January 15 (2026) from h t t p s : / / i r i d l . l d e o . c o l u m b i a . e d u / m a p r o o m / G l o b a l / D r o u g h t / G l o b a l / C P C _ G O B / A n a l y s i s . h t m l 

- IWMI. (n.d.). South Asia Drought Monitoring System (SADMS). International Water Management Institute. Retrieved January 15 (2026) from https://dms.iwmi.org/home 

- Jackson RD, Huete AR (1991) Interpreting vegetation indices. Prev Vet Med 11(3–4):185–200 

- Jain V, Mitra A (2025) Leveraging Machine Learning and Data Mining: Enhancing Agricultural Productivity and Sustainability (SDG 2 Zero Hunger). In _Machine and Deep Learning Solutions for Achieving the Sustainable Development Goals_ (pp. 209–228). IGI Global Scientific Publishing.  h t t p s : / / d o i . o r g / 1 0 . 4 0 1 8 / 9 7 9 - 8 - 3 6 9 3 - 8 1 6 1 - 8 . c h 0 1 1 

- Jang J, Viau AA, Anctil F (2006) Thermal-water stress index from satellite images. Int J Remote Sens 27(8):1619–1639.  h t t p s : / / d o i . o r g / 1 0 . 1 0 8 0 / 0 1 4 3 1 1 6 0 5 0 0 5 0 9 1 9 4 

- Japan Meteorological Agency. (n.d.). _ClimatView_ . Retrieved January 14, 2026, from  h t t p s : / / d s . d a t a . j m a . g o . j p / t c c / t c c / p r o d u c t s / c l i m a t e / c l i m a t v i e w / f r a m e . p h p ? & s = 1 & r = 0 & d = 0 & y = 2 0 1 9 & m = 2 & e = 8 & t = 0 & l = 0 & k = 0 & s = 1 

- Jiao W, Wang L, McCabe MF (2021) Multi-sensor remote sensing for drought characterization: current status, opportunities and a roadmap for the future. Remote Sens Environ 256:112313 

- Kafy A-A, Bakshi A, Saha M, Faisal AA, Almulhim AI, Rahaman ZA, Mohammad P (2023) Assessment and prediction of index based agricultural drought vulnerability using machine learning algorithms. Sci Total Environ 867:161394.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . s c i t o t e n v . 2 0 2 3 . 1 6 1 3 9 4 

- Kaliraj S, Parmar M, Bahuguna IM, Rajawat AS (2022) Assessment of Desertification and Land Degradation Vulnerability in Humid Tropics and Sub-tropical Regions of India Using Remote Sensing and GIS Techniques. In H. Sajjad, L. Siddiqui, A. Rahman, M. Tahir, & M. A. Siddiqui (Eds.), Challenges of Disasters in Asia (pp. 15–25). Springer Nature.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / 9 7 8 - 9 8 1 - 1 9 - 3 5 6 7 - 1 _ 2 

- Kaliraj S, Srinivas R, Kiruthika N, Vairaveni E, Mohamed H, Palanivel K, Lakshumanan C, Chandrasekar N (2024) Chapter 4—Remote sensing indices based soil properties measurement – a case study of the Thamirabarani River Basin, South India. In S. Dharumarajan, S. Kaliraj, K. Adhikari, M. Lalitha, & N. Kumar (Eds.), Remote Sensing of Soils (pp. 45–63). Elsevier.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / B 9 7 8 - 0 - 4 4 3 - 1 8 7 7 3 - 5 . 0 0 0 3 0 - 2 

- Kaliraj S, Krishnan KA, Suresh D, Kasivisvanathan KS, Chandrasekar N (2025) Evaluating soil erosion patterns and potential impacts of rainfall and vegetation index in the semi-arid river basin of southern India. Environ Monit Assess 197(8):848.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 0 6 6 1 - 0 2 5 - 1 4 2 7 7 - y 

- Kan J-C, Ferreira CSS, Destouni G, Haozhi P, Vieira Passos M, Barquet K, Kalantari Z (2023) Predicting agricultural drought indicators: ML approaches across wide-ranging climate and land use conditions. Ecol Indic 154:110524.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . e c o l i n d . 2 0 2 3 . 1 1 0 5 2 4 

- Kheyruri Y, Sharafati A, Neshat A (2023) Predicting agricultural drought using meteorological and ENSO parameters in different regions of Iran based on the LSTM model. Stoch Env Res Risk Assess 37(9):3599–3613.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 0 0 4 7 7 - 0 2 3 - 0 2 4 6 5 - 6 

- Kikon A, Deka PC (2022) Artificial intelligence application in drought assessment, monitoring and forecasting: a review. Stoch Environ Res Risk Assess 36(5):1197–1214.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 0 0 4 7 7 - 0 2 1 - 0 2 1 2 9 - 3 

- Kogan FN (1995) Application of vegetation index and brightness temperature for drought detection. Adv Space Res 15(11):91–100.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / 0 2 7 3 - 1 1 7 7 ( 9 5 ) 0 0 0 7 9 - T 

- Kogan F (2002) World droughts in the new millennium from AVHRRbased vegetation health indices. Eos Trans Am Geophys Union 83(48):557–563 

- Kogan F, Adamenko T, Guo W (2013) Global and regional drought dynamics in the climate warming era. Remote Sens Lett 4(4):364– 372.  h t t p s : / / d o i . o r g / 1 0 . 1 0 8 0 / 2 1 5 0 7 0 4 X . 2 0 1 2 . 7 3 6 0 3 3 

- Koteswararao SK, Rajendran T (2025) Higher accuracy of drought prediction using logistic regression algorithm over AdaBoost algorithm. AIP Conference Proceedings, 3267(1), 020095.  h t t p s : / / d o i . o r g / 1 0 . 1 0 6 3 / 5 . 0 2 7 0 5 6 8 

- Łągiewska M, Bartold M (2025) An integrated approach using remote sensing and multi-criteria decision analysis to mitigate agricultural drought impact in the Mazowieckie Voivodeship, Poland. Remote Sens 17(7):1158.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / r s 1 7 0 7 1 1 5 8 

- Lake PS (2011) Drought and aquatic ecosystems: Effects and responses. John Wiley & Sons. h t t p s : / / b o o k s . g o o g l e . c o m / b o o k s ? h l = e n & l r = & i d = t o - x C c Y K s s k C & o i = f n d & p g = P T 5 & d q = H y d r o l o g i c a l + d r o u g h t + c a n + r e d u c e + t h e + s u r f a c e + w a t e r , + f a l l + i n + g r o u n 

```
1 3
```

<mark>Page 25 of 28</mark> **<mark>222</mark>** 

Advancements in Spatio-temporal agricultural drought monitoring and modeling: a comprehensive review on… 

d + w a t e r + l e v e l s , + d r y i n g + o f + l a k e s , + s t r e a m s , + r i v e r + e t c + w h i c h + a l s o + d i r e c t l y + n e g a t i v e + i m p a c t e d + o n + e n v i r o n m e n t . + & o t s = r s f M 0 y b g n P & s i g = y e f j F n V m X z Q a 5 H R V M z 7 Z i P 2 1 a D w 

- Lambin EF, Ehrlich D (1996) The surface temperature-vegetation index space for land cover and land-cover change analysis. Int J Remote Sens 17:463–487.  h t t p s : / / d o i . o r g / 1 0 . 1 0 8 0 / 0 1 4 3 1 1 6 9 6 0 8 9 4 9 0 2 1 

- Lamine S, Petropoulos GP, Brewer PA, Bachari N-E-I, Srivastava PK, Manevski K, Kalaitzidis C, Macklin MG (2019) Heavy metal soil contamination detection using combined geochemistry and field spectroradiometry in the United Kingdom. Sensors 19(4):4.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / s 1 9 0 4 0 7 6 2 

- Lekakis E, Dimitrakos A, Oikonomopoulos E, Mygdakos G, Tsioutsia IM, Kotsopoulos S (2022) Evaluation of a satellite drought indicator approach and its potential for agricultural drought prediction and crop loss assessment. The case of BEACON project. Int J Sustainable Agricultural Manage Inf 8(1):40.  h t t p s : / / d o i . o r g / 1 0 . 1 5 0 4 / I J S A M I . 2 0 2 2 . 1 2 3 0 3 9 

- Liaghat S, Balasundram S (2010) A Review: The Role of Remote Sensing in Precision Agriculture. Am J Agricultural Biol Sci. 5 h t t p s : / / d o i . o r g / 1 0 . 3 8 4 4 / a j a b s s p . 2 0 1 0 . 5 0 . 5 5 

- Liu X, Zhu X, Pan Y, Li S, Liu Y, Ma Y (2016) Agricultural drought monitoring: progress, challenges, and prospects. J Geogr Sci 26(6):750–767.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 1 4 4 2 - 0 1 6 - 1 2 9 7 - 9 

- Liu L, Liao J, Chen X, Zhou G, Su Y, Xiang Z, Wang Z, Liu X, Li Y, Wu J (2017) The microwave temperature vegetation drought index (MTVDI) based on AMSR-E brightness temperatures for long-term drought assessment across China (2003–2010). Remote Sens Environ 199:302–320 

- Liu X, Zhu X, Zhang Q, Yang T, Pan Y, Sun P (2020) A remote sensing and artificial neural network-based integrated agricultural drought index: index development and applications. CATENA 186:104394.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . c a t e n a . 2 0 1 9 . 1 0 4 3 9 4 

- Lopinto E, Ananasso C (2014) THE PRISMA HYPERSPECTRAL MISSION. h t t p s : / / w w w . s e m a n t i c s c h o l a r . o r g / p a p e r / T H E - P R I S M A - H Y P E R S P E C T R A L - M I S S I O N - L o p i n t o - A n a n a s s o / a 9 9 c 3 e d 5 1 2 6 7 a 8 0 9 7 6 1 a 7 5 b d 9 7 6 9 1 e 9 a 6 7 2 9 0 9 c 6 

- Lu B, Dao PD, Liu J, He Y, Shang J (2020) Recent advances of hyperspectral imaging technology and applications in agriculture. Remote Sens 12(16):16.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / r s 1 2 1 6 2 6 5 9 

- Malik A, Kumar A, Salih SQ, Kim S, Kim NW, Yaseen ZM, Singh VP (2020) Drought index prediction using advanced fuzzy logic model: regional case study over Kumaon in India. PLoS One.  h t t p s : / / d o i . o r g / 1 0 . 1 3 7 1 / j o u r n a l . p o n e . 0 2 3 3 2 8 0 

- Malik A, Tikhamarine Y, Sammen SS, Abba S, Shahid S (2021) Prediction of meteorological drought by using hybrid support vector regression optimized with HHO versus PSO algorithms. Environmental Science and Pollution Research International.  h t t p s : / / w w w . s e m a n t i c s c h o l a r . o r g / p a p e r / P r e d i c t i o n - o f - m e t e o r o l o g i c a l - d r o u g h t - b y - u s i n g - w i t h - M a l i k - T i k h a m a r i n e / 8 7 2 f 4 3 4 5 e 1 3 6 1 3 6 f 3 f 2 4 4 7 2 0 c 8 c a 7 7 9 f b c 6 8 b b 3 3 

- Mandal S, Yadav A, Panwar R, Kumar SS, Karthick A, Priya A, Vijayakumar R, Ganesh SS (2025) Smart water management for SDG 6: a review of AI and IoT-enabled solutions. Water Conserv Sci Eng 10(2):83.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 4 1 1 0 1 - 0 2 5 - 0 0 4 0 7 - 

- Manjunath KR, Ray SS, Panigrahy S (2011) Discrimination of spectrally-close crops using ground-based hyperspectral data. J Indian Soc Remote Sens 39(4):599–602. h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 2 5 2 4 - 0 1 1 - 0 0 9 9 - x 

- Mansour Badamassi MB, El-Aboudi A, Gbetkom PG (2020) A new index to better detect and monitor agricultural drought in Niger using multisensor remote sensing data. Prof Geogr 72(3):421–432 

- Masupha TE, Moeletsi ME, Tsubo M (2025) Employing a metric to quantify the effectiveness of an agricultural drought early warning system during the fourth industrial revolution. Comput 

   - Electron Agric 230:109906.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . c o m p a g . 2 0 2 5 . 1 0 9 9 0 6 

- McVicar TR, Jupp DLB (1998) The current and potential operational uses of remote sensing to aid decisions on drought exceptional circumstances in Australia: a review. Agric Syst 57(3):399–468. h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / S 0 3 0 8 - 5 2 1 X ( 9 8 ) 0 0 0 2 6 - 2 

- Mera GA (2018) Drought and its impacts in Ethiopia. Weather Clim Extremes 22:24–35 

- Meza I, Siebert S, Döll P, Kusche J, Herbert C, Eyshi Rezaei E, Nouri H, Gerdener H, Popat E, Frischen J, Naumann G, Vogt JV, Walz Y, Sebesvari Z, Hagenlocher M (2020) Global-scale drought risk assessment for agricultural systems. Nat Hazards Earth Syst Sci 20(2):695–712.  h t t p s : / / d o i . o r g / 1 0 . 5 1 9 4 / n h e s s - 2 0 - 6 9 5 - 2 0 2 0 

- Mi Q, Huo Z, Li M, Zhang L, Kong R, Zhang F, Wang Y, Huo Y (2025) Development of a drought monitoring system for winter wheat in the Huang-Huai-Hai Region, China, utilizing a machine learning–physical process hybrid model. Agronomy 15(3):696.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / a g r o n o m y 1 5 0 3 0 6 9 6 

- Mishra A, Singh V (2010) A review of drought concepts. J Hydrol 391:202–216.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . j h y d r o l . 2 0 1 0 . 0 7 . 0 1 2 

- Mohammed S, Elbeltagi A, Bashir B, Alsafadi K, Alsilibe F, Alsalman A, Zeraatpisheh M, Széles A, Harsányi E (2022) A comparative analysis of data mining techniques for agricultural and hydrological drought prediction in the eastern Mediterranean. Comput Electron Agric 197:106925.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . c o m p a g . 2 0 2 2 . 1 0 6 9 2 5 

- Mokhtarzad M, Eskandari F, Vanjani N, Arabasadi A (2017) Drought forecasting by ANN, ANFIS, and SVM and comparison of the models. Environ Earth Sci.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 2 6 6 5 - 0 1 7 - 7 0 6 4 - 0 

- Moody J, Darken CJ (1989) Fast learning in networks of locally-tuned processing units. Neural Comput 1(2):281–294 

- Moran MS (2004) Thermal infrared measurement as an indicator of plant ecosystem health. Thermal Remote Sensing in Land Surface Processing. CRC 

- Moran MS, Clarke TR, Inoue Y, Vidal A (1994) Estimating crop water deficit using the relation between surface-air temperature and spectral vegetation index. Remote Sens Environ 49(3):246–263. h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / 0 0 3 4 - 4 2 5 7 ( 9 4 ) 9 0 0 2 0 - 5 

- Mossad A, Alazba A (2015) Drought forecasting using stochastic models in a hyper-arid climate. Atmosphere 6(4):410–430.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / a t m o s 6 0 4 0 4 1 0 

- Mullapudi A, Vibhute AD, Mali S, Patil CH (2023) A review of agricultural drought assessment with remote sensing data: methods, issues, challenges and opportunities. Appl Geomat 15(1):1–13.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 2 5 1 8 - 0 2 2 - 0 0 4 8 4 - 6 

- Namazi F, Ezoji M, Parmehr EG (2023) Paddy rice mapping in fragmented lands by improved phenology curve and correlation measurements on Sentinel-2 imagery in Google earth engine. Environ Monit Assess 195(10):1220. h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 0 6 6 1 - 0 2 3 - 1 1 8 0 8 - 3 

- Nan VA, Badea G, Badea AC, Grădinaru AP (2025) A systematic review of AI-Based classifications used in agricultural monitoring in the context of achieving the sustainable development goals. Sustainability 17(19):8526.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / s u 1 7 1 9 8 5 2 6 

- Naskar MK (2022) Remote Sensing based Agricultural Drought Monitoring. In S. R. Choudhury, Climate Change Dimensions and Mitigation Strategies for Agricultural Sustainability Vol 1 (1st ed.). New Delhi Publishers. h t t p s : / / d o i . o r g / 1 0 . 3 0 9 5 4 / N D P - c l i m a t e v 1 . 2 0 

- NDMC (2012) National Drought Mitigation Center. What is Drought? Nie H, Yang L, Li X, Ren L, Xu J, Feng Y (2018) Spatial Prediction of Soil Moisture Content in Winter Wheat Based on Machine Learning Model. 2018 26th International Conference on Geoinformatics, 1–6. h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / G E O I N F O R M A T I C S . 2 0 1 8 . 8 5 5 7 1 1 9 

```
1 3
```

**<mark>222</mark>** <mark>Page 26 of 28</mark> 

S. Mondal et al. 

Niemeyer S (2008) New drought indices. Options Méditerranéennes. Série A: Séminaires Méditerranéens 80:267–274 

Njoku EG, Entekhabi D (1996) Passive microwave remote sensing of soil moisture. J Hydrol 184(1):101–129.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / 0 0 2 2 - 1 6 9 4 ( 9 5 ) 0 2 9 7 0 - 2 

- NOAA-GDIS. (n.d.). Global Drought Information System (GDIS). Retrieved January 15 (2026) from  h t t p s : / / g d i s - n o a a . h u b . a r c g i s . c o m / % 2 0 p a g e s / d r o u g h t - m o n i t o r i n g 

- NOAA-NCEI. (n.d.). North American Drought Monitoring System. Retrieved January 14 (2026) from h t t p s : / / w w w . n c d c . n o a a . g o v / t e m p a n d - p r e c i p / d r o u g h t / n a d m / m a p s 

- Obsie EY, Liu Y (2025) Enhancing drought prediction through machine learning: advanced techniques combining phenotypic and agrometeorological data. Smart Agricultural Technology 12:101227. h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . a t e c h . 2 0 2 5 . 1 0 1 2 2 7 

- Orhan O, Ekercin S, Dadaser-Celik F (2014) Use of Landsat land surface temperature and vegetation indices for monitoring drought in the Salt Lake Basin Area, Turkey. The Scientific World Journal 2014:1–11.  h t t p s : / / d o i . o r g / 1 0 . 1 1 5 5 / 2 0 1 4 / 1 4 2 9 3 9 

- Ortega-Gaucin D, Pérez ML, Cortés FA (2016) Drought risk management in Mexico: progress and challenges. Int J Saf Secur Eng 6(2):161–170 

- Owe M, De Jeu R, Walker J (2001) A methodology for surface soil moisture and vegetation optical depth retrieval using the microwave polarization difference index. IEEE Transactions on Geoscience and Remote Sensing 39(8):1643–1654. h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / 3 6 . 9 4 2 5 4 2 

- Oyarzabal RS, Santos LBL, Cunningham C, Broedel E, de Lima GRT, Cunha-Zeri G, Peixoto JS, Anochi JA, Garcia K, Costa LCO, Pampuch LA, Cuartas LA, Zeri M, Guedes MRG, Negri RG, Muñoz VA, Cunha APMA (2025) Forecasting drought using machine learning: a systematic literature review. Nat Hazards 121(8):9823–9851.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 1 0 6 9 - 0 2 5 - 0 7 1 9 5 - 2 

- Özger M, Mishra AK, Singh VP (2012) Long lead time drought forecasting using a wavelet and fuzzy logic combination model: a case study in Texas. J Hydrometeorol 13(1):284–297.  h t t p s : / / d o i . o r g / 1 0 . 1 1 7 5 / J H M - D - 1 0 - 0 5 0 0 7 . 1 

- Paez-Trujilo A, Cañon J, Hernandez B, Corzo G, Solomatine D (2023) Multivariate regression trees as an explainable machine learning approach to explore relationships between hydroclimatic characteristics and agricultural and hydrological drought severity: case of study Cesar River basin. Nat Hazards Earth Syst Sci 23(12):3863–3883.  h t t p s : / / d o i . o r g / 1 0 . 5 1 9 4 / n h e s s - 2 3 - 3 8 6 3 - 2 0 2 3 

- Pande CB, Kushwaha NL, Orimoloye IR, Kumar R, Abdo HG, Tolche AD, Elbeltagi A (2023) Comparative assessment of improved SVM method under different kernel functions for predicting multi-scale drought index. Water Resour Manage 37(3):1367– 1399.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 1 2 6 9 - 0 2 3 - 0 3 4 4 0 - 0 

- Park S, Seo E, Kang D, Im J, Lee M-I (2018) Prediction of drought on pentad scale using remote sensing data and MJO index through random forest over East Asia. Remote Sens 10(11):1811.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / r s 1 0 1 1 1 8 1 1 

- Park H, Kim K, Lee DK (2019) Prediction of severe drought area based on random forest: using satellite image and topography data. Water 11(4):705.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / w 1 1 0 4 0 7 0 5 

- Peng J, Loew A, Merlin O, Verhoest NEC (2017) A review of spatial downscaling of satellite remotely sensed soil moisture. Rev Geophys 55(2):341–366.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 2 / 2 0 1 6 R G 0 0 0 5 4 3 

- Peñuelas J, Filella I, Biel C, Serrano L, Savé R (1993) The reflectance at the 950–970 nm region as an indicator of plant water status. Int J Remote Sens 14(10):1887–1905.  h t t p s : / / d o i . o r g / 1 0 . 1 0 8 0 / 0 1 4 3 1 1 6 9 3 0 8 9 5 4 0 1 0 

- Picoli MCA, Duft DG, Machado PG (2017) Identifying drought events in sugarcane using drought indices derived from Modis sensor. Pesqui Agropecu Bras 52(11):1063–1071.  h t t p s : / / d o i . o r g / 1 0 . 1 5 9 0 / s 0 1 0 0 - 2 0 4 x 2 0 1 7 0 0 1 1 0 0 0 1 2 

- Prodhan FA, Zhang J, Yao F, Shi L, Pangali Sharma TP, Zhang D, Cao D, Zheng M, Ahmed N, Mohana HP (2021) Deep learning for monitoring agricultural drought in South Asia using remote sensing data. Remote Sens 13(9):1715.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / r s 1 3 0 9 1 7 1 5 

- Prodhan FA, Zhang J, Hasan SS, Pangali Sharma TP, Mohana HP (2022) A review of machine learning methods for drought hazard monitoring and forecasting: current research trends, challenges, and future research directions. Environ Model Softw 149:105327. h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . e n v s o f t . 2 0 2 2 . 1 0 5 3 2 7 

- Qin Q, Wu Z, Zhang T, Sagan V, Zhang Z, Zhang Y, Zhang C, Ren H, Sun Y, Xu W, Zhao C (2021) Optical and thermal remote sensing for monitoring agricultural drought. Remote Sens 13(24):5092.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / r s 1 3 2 4 5 0 9 2 

- Rahmati O, Falah F, Dayal KS, Deo RC, Mohammadi F, Biggs T, Moghaddam DD, Naghibi SA, Bui DT (2020) Machine learning approaches for spatial modeling of agricultural droughts in the south-east region of Queensland Australia. Sci Total Environ 699:134230.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . s c i t o t e n v . 2 0 1 9 . 1 3 4 2 3 0 

- Ramamoorthy P, Samiappan S, Wubben M, Brooks J, Shrestha A, Panda R, Reddy K, Bheemanahalli R (2022) Hyperspectral reflectance and machine learning approaches for the detection of drought and root-knot nematode infestation in cotton. Remote Sens 14:4021.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / r s 1 4 1 6 4 0 2 1 

- Rao DVCS, Subrahmanyam DV, Manjula DA, Radhika P,Dr.P.Shireesha (2025) Spatio-Temporal Deep Learning Models for Forecasting Agricultural Drought in Rain-Fed Regions. Int J Environ Sci 11(4s):692–701 

- Rathore MMU, Paul A, Ahmad A, Chen B-W, Huang B, Ji W (2015) Real-time big data analytical architecture for remote sensing application. IEEE J Sel Top Appl Earth Observ Remote Sens 8(10):4610–4621.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / J S T A R S . 2 0 1 5 . 2 4 2 4 6 8 3 

- Raza MO, Mahoto NA, Al Reshan MS, Alqazzaz A, Rajab A, Shaikh A (2025) Drought detection in satellite imagery: a layered ensemble machine learning approach. Int J Comput Intell Syst 18(1):161.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 4 4 1 9 6 - 0 2 5 - 0 0 9 0 3 - 7 

- Rembold F, Meroni M, Urbano F, Royer A, Atzberger C, Lemoine G, Eerens H, Haesen D (2015) Remote sensing time series analysis for crop monitoring with the SPIRITS software: new functionalities and use examples. Front Environ Sci 3:46 

- Rezaei M, Moghaddam MA, Piri J, Azizyan G, Shamsipour AA (2025) Drought prediction using advanced hybrid machine learning for arid and semi-arid environments. KSCE J Civ Eng 29(4):100025. h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . k s c e j . 2 0 2 4 . 1 0 0 0 2 5 

- Rhee J, Im J, Carbone GJ (2010) Monitoring agricultural drought for arid and humid regions using multi-sensor remote sensing data. Remote Sens Environ 114(12):2875–2887.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . r s e . 2 0 1 0 . 0 7 . 0 0 5 

- Richardsons AJ, Wiegand A (1977) DISTINGUISHING VEGETATION FROM SOIL BACKGROUND INFORMATION. Photogrammetric Engineering and Remote Sensing.  h t t p s : / / w w w . s e m a n t i c s c h o l a r . o r g / p a p e r / D I S T I N G U I S H I N G - V E G E T A T I O N - F R O M - S O I L - B A C K G R O U N D - R i c h a r d s o n s - W i e g a n d / 3 e 0 4 9 b c 0 b f 9 d 0 6 c 1 4 6 4 8 f 5 a 3 6 0 3 6 b 8 a f 7 6 2 8 a 4 c e 

- Rojas O (2021) Next generation agricultural stress index system (ASIS) for agricultural drought monitoring. Remote Sens 13(5):5. h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / r s 1 3 0 5 0 9 5 9 

- Roodposhti MS, Safarrad T, Shahabi H (2017) Drought sensitivity mapping using two one-class support vector machine algorithms. Atmos Res 193:73–82.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . a t m o s r e s . 2 0 1 7 . 0 4 . 0 1 7 

- Rouse JW, Haas RH, Schell JA, Deering DW (1974), January 1 Monitoring vegetation systems in the Great Plains with ERTS.  h t t p s : / / n t r s . n a s a . g o v / c i t a t i o n s / 1 9 7 4 0 0 2 2 6 1 4 

- Roushangar K, Ghasempour R, Kirca VSO, Demirel M (2021) Hybrid point and interval prediction approaches for drought modeling using ground-based and remote sensing data. Hydrol Res.  h t t p s : / / d o i . o r g / 1 0 . 2 1 6 6 / n h . 2 0 2 1 . 0 2 8 

```
1 3
```

<mark>Page 27 of 28</mark> **<mark>222</mark>** 

Advancements in Spatio-temporal agricultural drought monitoring and modeling: a comprehensive review on… 

- Sai MS, Murthy CS, Chandrasekar K, Jeyaseelan AT, Diwakar PG, Dadhwal VK (2016) Agricultural drought: Assessment & monitoring. Mausam 67(1):131–142 

- Sandeep P, Obi Reddy GP, Jegankumar R, Arun Kumar KC (2021) Monitoring of agricultural drought in semi-arid ecosystem of Peninsular India through indices derived from time-series CHIRPS and MODIS datasets. Ecol Indic 121:107033.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . e c o l i n d . 2 0 2 0 . 1 0 7 0 3 3 

- Sandholt I, Rasmussen K, Andersen J (2002) A simple interpretation of the surface temperature/vegetation index space for assessment of surface moisture status. Remote Sens Environ 79(2–3):213–224. h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / S 0 0 3 4 - 4 2 5 7 ( 0 1 ) 0 0 2 7 4 - 7 

- Sardar VS, Chaudhari MYK, S. S., Ghosh P (2021) Convolution Neural Network-based Agriculture Drought Prediction using Satellite Images. 2021 IEEE Mysore Sub Section International Conference (MysuruCon), 601–607. h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / M y s u r u C o n 5 2 6 3 9 . 2 0 2 1 . 9 6 4 1 5 3 1 

- Seelig H-D, Hoehn A, Stodieck L, Klaus D, Adams WW, Emery W (2008) Relations of remote sensing leaf water indices to leaf water thickness in cowpea, bean, and sugarbeet plants. Remote Sens Environ.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . r s e . 2 0 0 7 . 0 5 . 0 0 2 

- Seleiman MF, Al-Suhaibani N, Ali N, Akmal M, Alotaibi M, Refay Y, Dindaroglu T, Abdul-Wajid HH, Battaglia ML (2021) Drought stress impacts on plants and different approaches to alleviate its adverse effects. Plants 10(2):259 

- Senapati U, Srivastava A, Maity R (2025) High-resolution agricultural drought hazard mapping using the potential of geospatial data and machine learning approaches. Environ Monit Assess 197(11):1195.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 0 6 6 1 - 0 2 5 - 1 4 5 3 8 - w 

- Shah H, Rane V, Nainani J, Jeyakumar B, Giri N (2017) Drought prediction and management using big data analytics. Int J Comput Appl 162:27–30.  h t t p s : / / d o i . o r g / 1 0 . 5 1 2 0 / i j c a 2 0 1 7 9 1 3 2 7 6 

- Shoshany M, Svoray T, Curran PJ, Foody GM, Perevolotsky A (2000) The relationship between ERS-2 SAR backscatter and soil moisture: generalization from a humid to semi-arid transect. Int J Remote Sens 21(11):2337–2343.  h t t p s : / / d o i . o r g / 1 0 . 1 0 8 0 / 0 1 4 3 1 1 6 0 0 5 0 0 2 9 6 2 0 

- Singh S, KV SB (2022) Role of hyperspectral imaging for precision agriculture monitoring. ADBU J Eng Technol, 11(1).  h t t p s : / / j o u r n a l s . d b u n i v e r s i t y . a c . i n / o j s / i n d e x . p h p / A J E T / a r t i c l e / v i e w / 3 5 8 7 

- Singh R, Roy S, Kogan F (2003) Vegetation and temperature condition indices from NOAA AVHRR data for drought monitoring over India. Int J Remote Sens 24:4393–4402.  h t t p s : / / d o i . o r g / 1 0 . 1 0 8 0 / 0 1 4 3 1 1 6 0 3 1 0 0 0 0 8 4 3 2 3 

- Singh P, Pandey PC, Petropoulos GP, Pavlides A, Srivastava PK, Koutsias N, Deng KAK, Bao Y (2020) Hyperspectral remote sensing in precision agriculture: Present status, challenges, and future trends. In Hyperspectral Remote Sensing (pp. 121–146). Elsevier. h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / B 9 7 8 - 0 - 0 8 - 1 0 2 8 9 4 - 0 . 0 0 0 0 9 - 7 

- Solh M, van Ginkel M (2014) Drought preparedness and drought mitigation in the developing world ׳s drylands. Weather Clim Extremes 3:62–66 

- Son NT, Chen CF, Chen CR, Minh VQ, Trung NH (2014) A comparative analysis of multitemporal MODIS EVI and NDVI data for large-scale rice yield estimation. Agric For Meteorol 197:52–64 

- Speranza CI, Kiteme B, Wiesmann U (2008) Droughts and famines: the underlying factors and the causal links among agro-pastoral households in semi-arid Makueni district, Kenya. Glob Environ Change 18(1):220–233 

- Stagge JH, Kohn I, Tallaksen LM, Stahl K (2015) Modeling drought impact occurrence based on meteorological drought indices in Europe. J Hydrol 530:37–50. h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . j h y d r o l . 2 0 1 5 . 0 9 . 0 3 9 

- Sun P, Zhang Q, Wen Q, Singh VP, Shi P (2017) Multisource databased integrated agricultural drought monitoring in the Huai River Basin, China. J Geophys Res Atmos 122(20):10,75110,772.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 2 / 2 0 1 7 J D 0 2 7 1 8 6 

- Sundararajan K, Garg L, Srinivasan K, Bashir A, Kaliappan J, Ganapathy G, Selvaraj S, Meena T (2021) A contemporary review on drought modeling using machine learning approaches. Comput Model Eng Sci 128(2):447–487.  h t t p s : / / d o i . o r g / 1 0 . 3 2 6 0 4 / c m e s . 2 0 2 1 . 0 1 5 5 2 8 

- Tang H, Li Z-L (2014) Applications of Thermal Remote Sensing in Agriculture Drought Monitoring and Thermal Anomaly Detection. In: Tang H, Li Z-L (eds) Quantitative Remote Sensing in Thermal Infrared. Springer, Berlin Heidelberg, pp 203–256.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / 9 7 8 - 3 - 6 4 2 - 4 2 0 2 7 - 6 _ 7 

- Tanriverdi I, Batmaz İ (2025) AI-driven U.S. drought prediction using machine learning and deep learning. Clim Dyn 63(6):249.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 0 0 3 8 2 - 0 2 5 - 0 7 7 2 0 - w 

- Tian M, Wang P, Han P, Zhang S (2013) Drought forecasts based on SARIMA models and vegetation temperature condition index. Nongye Jixie Xuebao/Transactions Chin Soc Agricultural Mach 44:109–116.  h t t p s : / / d o i . o r g / 1 0 . 6 0 4 1 / j . i s s n . 1 0 0 0 - 1 2 9 8 . 2 0 1 3 . 0 2 . 0 2 1 

- Tian M, Wang P, Khan J (2016) Drought forecasting with vegetation temperature condition index using ARIMA models in the Guanzhong Plain. Remote Sens 8(9):9.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / r s 8 0 9 0 6 9 0 

- Tian Y, Xu Y-P, Wang G (2018) Agricultural drought prediction using climate indices based on support vector regression in Xiangjiang River basin. Sci Total Environ 622:710–720.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . s c i t o t e n v . 2 0 1 7 . 1 2 . 0 2 5 

- Tucker CJ, Choudhury BJ (1987) Satellite remote sensing of drought conditions. Remote Sens Environ 23(2):243–251.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / 0 0 3 4 - 4 2 5 7 ( 8 7 ) 9 0 0 4 0 - X 

- Ulaby FT, Moore RK, Fung AK (1986) Microwave remote sensing: Active and passive. Volume 3-From theory to applications.  h t t p s : / / n t r s . n a s a . g o v / c i t a t i o n s / 1 9 8 6 0 0 4 1 7 0 8 

- Ullah I, Zeng X-M, Mukherjee S, Aadhar S, Mishra AK, Syed S, Ayugi BO, Iyakaremye V, Lv H (2023) Future amplification of multivariate risk of compound drought and heatwave events on South Asian population. Earths Future 11(12):e2023EF003688.  h t t p s : / / d o i . o r g / 1 0 . 1 0 2 9 / 2 0 2 3 E F 0 0 3 6 8 8 

- UNCCD. (2023), December 1 Global drought snapshot 2023: The need for immediate action. UNCCD.  h t t p s : / / w w w . u n c c d . i n t / r e s o u r c e s / p u b l i c a t i o n s / g l o b a l - d r o u g h t - s n a p s h o t - 2 0 2 3 - n e e d - i m m e d i a t e - a c t i o n 

- UNEP-DHI. (n.d.). Flood and Drought Portal. Retrieved January 14 (2026) from  h t t p s : / / w w w . fl  o o d d r o u g h t m o n i t o r . c o m / h o m e 

- van Ginkel M, Biradar C (2021) Drought early warning in agri-food systems. Climate 9:134.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / c l i 9 0 9 0 1 3 4 

- Van Loon AF (2015) Hydrological drought explained. Wiley Interdisciplinary Reviews: Water 2(4):359–392 

- Veettil AV, Mishra AK (2023) Quantifying thresholds for advancing impact-based drought assessment using classification and regression tree (CART) models. J Hydrol 625:129966.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . j h y d r o l . 2 0 2 3 . 1 2 9 9 6 6 

- Vreugdenhil M, Greimeister-Pfeil I, Preimesberger W, Camici S, Dorigo W, Enenkel M, van der Schalie R, Steele-Dunne S, Wagner W (2022) Microwave remote sensing for agricultural drought monitoring: recent developments and challenges. Frontiers in Water.  h t t p s : / / d o i . o r g / 1 0 . 3 3 8 9 / f r w a . 2 0 2 2 . 1 0 4 5 4 5 1 

- Walker JP, Houser PR, Willgoose GR (2004) Active microwave remote sensing for soil moisture measurement: a field evaluation using ERS-2. Hydrol Process 18(11):1975–1997 

- Wang L, Qu J (2007) NMDI: a normalized multi-band drought index for monitoring soil and vegetation moisture with satellite remote sensing. Geophysical Research Letters - GEOPHYS RES LETT. h t t p s : / / d o i . o r g / 1 0 . 1 0 2 9 / 2 0 0 7 G L 0 3 1 0 2 1 

- Wang L, Qu JJ (2009) Satellite remote sensing applications for surface soil moisture monitoring: a review. Front Earth Sci China 3(2):237–247.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 1 7 0 7 - 0 0 9 - 0 0 2 3 - 7 

- Wang P, Li X, Gong J, Song C (2001) Vegetation temperature condition index and its application for drought monitoring. IGARSS 2001. Scanning the Present and Resolving the Future. Proceedings. IEEE 2001 International Geoscience and Remote Sensing 

```
1 3
```

**<mark>222</mark>** <mark>Page 28 of 28</mark> 

S. Mondal et al. 

   - Symposium (Cat. No. 01CH37217), 1, 141–143.  h t t p s : / / i e e e x p l o r e . i e e e . o r g / a b s t r a c t / d o c u m e n t / 9 7 6 0 8 3 / 

- Wang W, Ertsen MW, Svoboda MD, Hafeez M (2016) Propagation of drought: from meteorological drought to agricultural and hydrological drought. Adv Meteorol 2016:1–5.  h t t p s : / / d o i . o r g / 1 0 . 1 1 5 5 / 2 0 1 6 / 6 5 4 7 2 0 9 

- Wang T, Tu X, Singh VP, Chen X, Lin K, Lai R, Zhou Z (2022) Socioeconomic drought analysis by standardized water supply and demand index under changing environment. J Clean Prod 347:131248.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . j c l e p r o . 2 0 2 2 . 1 3 1 2 4 8 

- Wardlow BD, Anderson MC, Verdin JP (eds) (2012) Remote Sensing of Drought: Innovative Monitoring Approaches. CRC.  h t t p s : / / d o i . o r g / 1 0 . 1 2 0 1 / b 1 1 8 6 3 

- Wassie SB, Mengistu DA, Birlie AB (2022) Agricultural drought assessment and monitoring using MODIS-based multiple indices: the case of North Wollo, Ethiopia. Environ Monit Assess 194(11):787.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 0 6 6 1 - 0 2 2 - 1 0 4 5 5 - 4 

- Widiyatmoko W, Sudibyakto, Nurjani E (2021) Agricultural drought risk assessment in upper progo watershed using multi-temporal landsat 8 imagery. IOP Conference Series: Earth and Environmental Science, 683, 012097.  h t t p s : / / d o i . o r g / 1 0 . 1 0 8 8 / 1 7 5 5 - 1 3 1 5 / 6 8 3 / 1 / 0 1 2 0 9 7 

- Wilhite DA, Glantz MH (1985) Understanding: the drought phenomenon: the role of definitions. Water Int 10(3):111–120 

- WMO (2006) Drought monitoring and early warning: Concepts, progress, and future challenges. World Meteorological Organization 

- Wong G, Lambert MF, Leonard M, Metcalfe AV (2010) Drought analysis using trivariate copulas conditional on climatic states. J Hydrol Eng 15(2):129–141.  h t t p s : / / d o i . o r g / 1 0 . 1 0 6 1 / ( A S C E ) H E . 1 9 4 3 - 5 5 8 4 . 0 0 0 0 1 6 9 

- Wong C, Gilbert M, Pierce MA, Parker TA, Palkovic A, Gepts P, Magney T, Buckley T (2022) Hyperspectral Remote Sensing for Phenotyping the Physiological Drought Response of Common and Tepary Bean. Plant Phenomics.  h t t p s : / / w w w . s e m a n t i c s c h o l a r . o r g / p a p e r / H y p e r s p e c t r a l - R e m o t e - S e n s i n g - f o r - P h e n o t y p i n g - t h e - o f - W o n g - G i l b e r t / b 3 ff  2 b 8 5 b a 2 f c 6 2 b f 1 e 0 9 f 2 0 2 0 9 d 5 d e b 1 5 5 e 7 d f 8 

- Wu J (2014) Agricultural Drought Monitoring And Prediction Using Soil Moisture Deficit Index. Theses and Dissertations.  h t t p s : / / c o m m o n s . u n d . e d u / t h e s e s / 1 6 0 8 

- Wu M, Lu H (2016) A modified vegetation water supply index (MVWSI) and its application in drought monitoring over Sichuan and Chongqing, China. J Integr Agric 15(9):2132–2141.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / S 2 0 9 5 - 3 1 1 9 ( 1 5 ) 6 1 2 5 7 - 6 

- Xing X, Wei S, Chen X, Qian J, Peng S, Sun J, Sun B, Chen C (2025) A Deep Learning-Based Composite Agricultural Drought Index for Monitoring and Impact Assessment in Central Asia (SSRN Scholarly Paper No. 5358177). Social Science Research Network.  h t t p s : / / d o i . o r g / 1 0 . 2 1 3 9 / s s r n . 5 3 5 8 1 7 7 

- Xu X, Xie F, Zhou X (2016) Research on spatial and temporal characteristics of drought based on GIS using remote sensing big data. Cluster Comput 19(2):757–767.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 0 5 8 6 - 0 1 6 - 0 5 5 6 - y 

- Xu D, Ma Y, Yan J, Liu P, Chen L (2020) Spatial-feature data cube for spatiotemporal remote sensing data processing and analysis. Computing 102(6):1447–1461.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 0 0 6 0 7 - 0 1 8 - 0 6 8 1 - y 

- Xu F, Bento VA, Qu Y, Wang Q (2023) Projections of global drought and their climate drivers using CMIP6 global climate models. Water 15(12):12.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / w 1 5 1 2 2 2 7 2 

- Xu X, Chen F, Wang B, Harrison MT, Chen Y, Liu K, Zhang C, Zhang M, Zhang X, Feng P, Hu K (2024) Unleashing the power of machine learning and remote sensing for robust seasonal drought monitoring: a stacking ensemble approach. J Hydrol 634:131102. h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . j h y d r o l . 2 0 2 4 . 1 3 1 1 0 2 

- Yang X, Gao F, Yuan H, Cao X (2024) Integrated UAV and satellite multi-spectral for agricultural drought monitoring of winter wheat in the seedling stage. Sensors 24(17):5715.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / s 2 4 1 7 5 7 1 5 

- Yoon D-H, Nam W-H, Lee H-J, Hong E-M, Feng S, Wardlow BD, Tadesse T, Svoboda MD, Hayes MJ, Kim D-E (2020) Agricultural drought assessment in East Asia using satellite-based indices. Remote Sens 12(3):3.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / r s 1 2 0 3 0 4 4 4 

- Yu H, Li L, Liu Y, Li J (2019) Construction of comprehensive drought monitoring model in Jing-Jin-Ji region based on multisource remote sensing data. Water 11(5):5.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / w 1 1 0 5 1 0 7 7 

- Zaigham Abbas Naqvi SM, Hussain S, Awais M, Tahir MN, Saleem SR, Al-Yarimi FAM, Ashurov M, Saidani O, Khan MI, Wu J, Wei Z, Hu J (2025) Climate-resilient water management: leveraging IoT and AI for sustainable agriculture. Egypt Inform J 30:100691. h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . e i j . 2 0 2 5 . 1 0 0 6 9 1 

- Zarei AR, Mahmoudi MR, Moghimi MM (2023) Determining the most appropriate drought index using the random forest algorithm with an emphasis on agricultural drought. Nat Hazards 115(1):923– 946.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 1 0 6 9 - 0 2 2 - 0 5 5 7 9 - 2 

- Zargar A, Sadiq R, Naser B, Khan FI (2011) A review of drought indices. Environ Rev 19(NA):333–349.  h t t p s : / / d o i . o r g / 1 0 . 1 1 3 9 / a 1 1 - 0 1 3 

- Zhang A, Jia G (2013) Monitoring meteorological drought in semiarid regions using multi-sensor microwave remote sensing data. Remote Sens Environ 134:12–23.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . r s e . 2 0 1 3 . 0 2 . 0 2 3 

- Zhang F, Zhou G (2015) Estimation of canopy water content by means of hyperspectral indices based on drought stress gradient experiments of maize in the North Plain China. Remote Sens 7(11):15203–15223.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / r s 7 1 1 1 5 2 0 3 

- Zhang P, Gao J, Thomas AG, Alagupackiam K, Mannava K, Bosco PI, Chiao S (2017) On Building a Big Data Analysis System for California Drought.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / B i g D a t a S e r v i c e . 2 0 1 7 . 2 3 

- Zhao S, Wang Q, Zhang F, Yao Y, Qin Q, You L, Li J, Li Z, Wu Y, Liu S, Li Y (2013) Drought mapping using two shortwave infrared water indices with MODIS data under vegetated season. J Environ Inf 21:102–111.  h t t p s : / / d o i . o r g / 1 0 . 3 8 0 8 / j e i . 2 0 1 3 0 0 2 3 7 

- Zhao M, Huang S, Huang Q, Wang H, Leng G, Xie Y (2019) Assessing socio-economic drought evolution characteristics and their possible meteorological driving force. Geomatics Nat Hazards Risk 10(1):1084–1101.  h t t p s : / / d o i . o r g / 1 0 . 1 0 8 0 / 1 9 4 7 5 7 0 5 . 2 0 1 8 . 1 5 6 4 7 0 6 

- Zhu X, Wang T, Skidmore AK, Darvishzadeh R, Niemann KO, Liu J (2017) Canopy leaf water content estimated using terrestrial LiDAR. Agric For Meteorol 232:152–162. h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . a g r f o r m e t . 2 0 1 6 . 0 8 . 0 1 6 

- Ziesche S, Agarwal S, Nagaraju U, Prestes E, Singha N (2023) Role of Artificial Intelligence in Advancing Sustainable Development Goals in the Agriculture Sector. In F. Mazzi & L. Floridi (Eds.), _The Ethics of Artificial Intelligence for the Sustainable Development Goals_ (pp. 379–397). Springer International Publishing.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / 9 7 8 - 3 - 0 3 1 - 2 1 1 4 7 - 8 _ 2 1 

- Ziolkowska JR (2016) Socio-economic implications of drought in the agricultural sector and the state economy. Economies 4(3):19 

- Zou Q, Li G, Yu W (2018) MapReduce functions to remote sensing distributed data processing—global vegetation drought monitoring as example. Software Pract Exper 48(7):1352–1367.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 2 / s p e . 2 5 7 8 

- Zou X, Jin J, Mõttus M (2023) Potential of satellite spectral resolution vegetation indices for estimation of canopy chlorophyll content of field crops: mitigating effects of leaf angle distribution. Remote Sens 15(5):5.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / r s 1 5 0 5 1 2 3 4 

**Publisher’s note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law. 

```
1 3
```

