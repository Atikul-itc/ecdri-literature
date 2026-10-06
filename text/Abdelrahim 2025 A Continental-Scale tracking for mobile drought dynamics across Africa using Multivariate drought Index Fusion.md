International Journal of Applied Earth Observation and Geoinformation 144 (2025) 104917 



Contents lists available at ScienceDirect 

International Journal of Applied Earth Observation and Geoinformation 

journal homepage: www.elsevier.com/locate/jag 



A Continental-Scale tracking for mobile drought dynamics across Africa using Multivariate drought Index Fusion 



Nasser A.M. Abdelrahim<sup>a,b,e</sup> , Shuanggen Jin<sup>c,d,*</sup> 

a _Shanghai Astronomical Observatory, Chinese Academy of Sciences, Shanghai 200030, China_ b _School of Astronomy and Space Science, University of Chinese Academy of Sciences, Beijing 100049, China_ c _School of Artificial Intelligence, Anhui University, Hefei 230601, China_ d _School of Surveying and Land Information Engineering, Henan Polytechnic University, Jiaozuo 454003, China_ e _Civil Engineering Department, Faculty of Engineering, Sohag University, Sohag 82511, Egypt_ 

A R T I C L E I N F O 

A B S T R A C T 

_Keywords:_ Mobile drought Africa Drought index NDVI Multivariate Drought Index Fusion (MDIF) 

Drought remains the most widespread and debilitating climate hazard in Africa, which threatens food safety and socio-ecological stability across the continent. Traditional drought monitoring systems, however, typically never register the dynamic evolution of drought episodes, which can extend between areas and amplify effects downstream. This study proposes a new Multivariate Drought Index Fusion (MDIF) that, apart from merging different drought indicators, mainly tracks the spatiotemporal trajectory of mobile drought fronts across Africa from 2000 to 2024. Avoiding the shortcomings of static drought maps, this approach offers a dynamic presentation of drought propagation patterns required for timely warning and management. Through the use of Principal Component Analysis (PCA), MDIF integrates multiple drought indicators, Normalized Difference Vegetation Index (NDVI), Land Surface Temperature (LST), precipitation, Standardized PrecipitationEvapotranspiration Index (SPEI), and Vegetation Health Index (VHI), into a fused, highly reliable, meteorological-ecological sensitivity drought index. The MDIF exhibited significant correlations with SPI-3 (r = 0.72–0.84), particularly across arid and semi-arid regions, and with VHI (r = 0.76–0.87), further underscoring its robustness in capturing both meteorological and ecological drought conditions. The findings indicate the Horn of Africa as a long-term drought hotbed, with severe events during 2006, 2011, 2017–2019, and 2022–2023, while Southern Africa experienced severe multi-year droughts from 2014 to 2017. Our tracking analysis, for the first time, indicates a dominant northeast-to-southwest trajectory of drought fronts over sub-Saharan Africa. This research enhances continental drought early warning through dynamic mapping of intensity and mobility for resilience planning. 

# **1. Introduction** 

Drought remains one of the most devastating natural disasters in the world, and it has significant effects on ecosystems, agricultural yields, water resources, and human lives (Abdelrahim and Jin, 2025a; Ssembajwe et al., 2025). The Sahel, southern Africa, and the Horn of Africa regions, in particular, have been confronted with recurring drought emergencies leading to loss of crops, hunger, and internal displacement of individuals (Lambert et al., 2016; Samasse et al., 2020; Tong et al., 2020; Hassan and Jin, 2016). Against the backdrop of these acute socio-economic as well as environmental necessities, it is a priority on the agendas of national and global policymaking (FAO, 2023; Mishra and Singh, 2010). 

Major ocean–atmosphere teleconnections intricately interact to control drought regimes over Sub-Saharan Africa. A coupled Atlantic Multidecadal Oscillation (AMO) and Southern Oscillation Index (SOI) accounts for up to 43 % of West African drought variability (Ogunrinde et al., 2024). Drought events are intensified and made more spatially heterogenized through West African Monsoon system changes and land–atmosphere feedbacks (Heiss et al., 2025; Samasse et al., 2018). Another level of complexity is introduced by compound droughts, which occur together with heat waves and precipitation shortage. Han et al. (2022) concluded from a 2016–2017 Horn of Africa drought study that it was a 250-year event where small rainfall deficits were augmented by record (+1.02<sup>◦</sup> C) temperatures to enhance moisture stress, echoing global-scale behavior observed in California. 

* Corresponding author. 

_E-mail addresses:_ sgjin@hpu.edu.cn, sg.jin@yahoo.com (S. Jin). 

https://doi.org/10.1016/j.jag.2025.104917 

Received 3 June 2025; Received in revised form 12 September 2025; Accepted 12 October 2025 

Available online 17 October 2025 

1569-8432/© 2025 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY-NC license ( http://creativecommons.org/licenses/bync/4.0/ ). 

_N.A.M. Abdelrahim and S. Jin_ 

Single-index measures like the Standardized Precipitation Index (SPI) and the Standardized Precipitation Evapotranspiration Index (SPEI), controlled by atmospheric water deficits, are the backbone of traditional drought observation (Chere and Debalke, 2024; Dong et al., 2023). These indices are useful in hydrologic research but do not provide the complete picture of agricultural droughts where surface energy fluxes, vegetation response, and soil moisture deficit are of equal importance (Esfahanian et al., 2017). According to Chere and Debalke (2024) and Bento et al. (2018), single-index or single-sensor methods cannot identify initial stress in vegetation before the onset of symptoms. 

Remote sensing has revolutionized drought monitoring through enabling large-scale repetitive surveillance of vegetation condition, land surface temperature (LST), and soil moisture proxies (Abdelrahim and Jin, 2025a; Jia et al., 2020; Jin et al., 2017; Jin et al., 2025; Mostafa et al., 2021). Vegetation indices such as the Normalized Difference Vegetation Index (NDVI) (Adhikari et al., 2024; Bento et al., 2020), the Vegetation Health Index (VHI) (Chere and Debalke, 2024; Kogan, 1995), and soil-adjusted vegetation indices (Huete, 1988; Konno and Homma, 2023) have been widely used to detect vegetation stress. Bento et al. (2020) demonstrated the synergistic function of NDVI and LST in the context of VHI, particularly in dryland environments. Most recent research has also employed radar (SAR) and GNSS-Reflectometry data to estimate soil moisture, further contributing to the bountiful drought detection toolkit (Edokossi et al., 2020; Jin et al., 2024a,b). Machine learning methods, including self-organizing maps (C´er´eghino and Park, 2009; Iyer and Krishnan, 2024), random forests, and deep learning approaches (Choukri et al., 2024; Luo et al., 2024), have been proposed to integrate these multi-sensor observations into composite drought assessments with greater accuracy (Jiao et al., 2019; Kulkarni et al., 2020). Though numerous remote sensing–based drought monitoring methods are still centered on static severity classification or pixel-based temporal anomalies, the latest developments have increasingly attempted to replicate drought dynamics. Studies using GRACE-based water storage anomalies (Ali et al., 2023; Elameen et al., 2023), soil moisture anomaly monitoring (Ajaz et al., 2019; Alasow et al., 2024), and time-lagged vegetation indexes (Liu et al., 2021; Nigatu et al., 2024) are valuable contributions toward the characterization of drought propagation. However, there are not many models to dynamically monitor mobile drought fronts on a large scale. 

Despite these successes, there are some gaps in drought monitoring literature. While single-index approaches remain prevalent, multi-index and multi-source designs are increasingly becoming popular (e.g., SPEI, SSMI, and CHIRPS-based hybrids) (Palagiri and Pal, 2024; You et al., 2025), and regional/global systems such as the U.S. Drought Monitor (USDM) (Yin and Zhang, 2023) demonstrate successful operational fusion (Hao and Singh, 2015; Pozzi et al., 2013). Nonetheless, there remain challenges in creating uniform, transferable multivariate fusion models for continental-scale operational drought monitoring, especially in Africa. Similarly, while numerous studies have investigated drought propagation owing to soil moisture memory, plant stress, and lagged climate signals (Beyene et al., 2023; Bilal and Gupta, 2024; Gorugantula et al., 2025), methods to operationally detect and monitor propagating drought fronts at large spatial scales remain lacking. Second, multisensor data fusion, while promising (Du et al., 2013; Jiao et al., 2019), lacks universal consensus about the most adequate approaches for optimal fusion strategies, particularly for operational agricultural drought monitoring in Africa. Third, while significant advancements have been made in describing the spatiotemporal dynamics of drought propagation, particularly through the application of three-dimensional (3D) approaches to drought identification (Feng et al., 2025; Yoo et al., 2022), a matter of significant importance but less debated is the dynamic monitoring of drought fronts—drought’s progression and aggregation over landscapes as an evolving process (Bento et al., 2018; Brandt et al., 2016). Whereas station-based conditions are diagnosed by drought indices, attempts to dynamically track drought fronts, defining their speed, direction, and migration pathways, particularly at the 

_International Journal of Applied Earth Observation and Geoinformation 144 (2025) 104917_ 

continental scale in Sub-Saharan Africa, have been sparse. 

To this end, this paper aims to bridge these gaps with a twin innovation: (1) developing a Multivariate Drought Index Fusion (MDIF) based on PCA (A. Farrag et al., 2020; Abdelrahim and Jin, 2025b) to fuse and integrate principal drought variables from multi-source remote sensing and climate archives. and (2) the first continent-scale algorithmic surveillance of mobile drought fronts, their density, velocity, and dominant directions of propagation across Africa. We selected NDVI, LST, precipitation, SPEI, and VHI as surrogate drought indicators. NDVI and VHI indicate vegetation response (Adhikari et al., 2024; Zeng et al., 2023), LST indicates evapotranspiration and surface heat stress, and precipitation and SPEI indicate meteorological water deficits (Dong et al., 2023; Rahimi et al., 2025). Together, these variables indicate both ecosystem impacts and hydroclimatic drivers. For integration purposes, we used the PCA, which is a popular method that reduces dimensionality and extracts the dominant drought signal in correlated data (Schwartz et al., 2022). Using connected component analysis and vector tracking algorithms on them, we calculate the velocity (km/month), direction (degrees), and distance (km) of the movement of drought front in Africa. Such active monitoring offers valuable information for enabling anticipation of subsequent drought impacts before their complete development. Importantly, the methodological contribution of this paper lies in its use of MDIF to enable the first continent-scale monitoring of mobile drought fronts in Africa. By leveraging the integration and propagation analysis, we go beyond the traditional anomaly-based monitoring to detect the changing trajectories of drought across space and time. 

The main objectives of this study are to: (1) Develop a multivariate drought index by combining a number of remote sensing and climatic indicators using PCA; (2) Compare the proposed MDIF index with the globally accepted SPI, and VHI in correlation and time series comparison measures; (3) Track drought front dynamics across Africa for the years 2000–2024, quantifying their spatiotemporal characteristics (speed, direction, distance); and (4) Analyze the long-term trends and persistent corridors of drought propagation by aid of statistical and spatial analysis techniques. The innovation of this study is the coupling of multi-sensor index fusion and dynamic front tracking of droughts, underpinned by 25 years of monthly remote sensing data over the complete Sub-Saharan Africa region. This study moves from static monitoring of drought to dynamic propagation analysis and provides new scientific understanding of the dynamics of droughts as moving phenomena immediately relevant to agricultural management, water resource planning, and climate change adaptation strategies in Africa and elsewhere. The rest of this paper shows materials and methods in Section 2, Section 3 presents results, analysis and discussions, and finally the conclusion is given at Section 4. 

# **2. Materials and methods** 

# _2.1. Study areas_ 

This study spans the entire African continent (Fig. 1), covering more than 30 million km<sup>2</sup> and home to over 1.4 billion people, with climatic and ecological conditions ranging from hyper-arid deserts to humid tropics and temperate zones (Abdelrahim and Jin, 2025c). The Sahara prevails in North Africa, where rainfall amounts are below 100 mm per year, restricted to irrigated Nile and Mediterranean regions. To the south of the desert is the Sahel, which is sustained by summer rains (June–September) favoring millet, sorghum, and livestock, though it is very arid (FAO, 2022; Samasse et al., 2018). 

West Africa is experiencing a bimodal rainfall regime along the Gulf of Guinea (1,200–2,500 mm per year), with which cocoa, cassava, and oil palm are sustained. Central Africa, dominated by the Congo Basin, has over 2,000 mm of rainfall, supporting tropical rainforests and subsistence crops of cassava, plantains, and maize. East Africa is more climatically variable, notably in the Horn, where bimodal wet seasons govern agriculture but are often disrupted by ENSO and IOD anomalies, 

2 

_N.A.M. Abdelrahim and S. Jin                                                                                                                                                                                                               International Journal of Applied Earth Observation and Geoinformation_ 

_International Journal of Applied Earth Observation and Geoinformation 144 (2025) 104917_ 



**Fig. 1.** The map illustrates the African continent, Panel (a) displays the topographic variation across Africa, emphasizing key regions such as the Ethiopian Highlands and the Congo Basin. Panel (b) illustrates land cover types (e.g., forests, savannas, deserts) derived from MODIS MCD12Q1 data, highlighting agriculturally relevant zones masked for drought analysis. 

which create recurring droughts (Zeng et al., 2023). 

Southern Africa is characterized by a unimodal regime of summer rainfall (500–1,200 mm per year) favoring maize, soybean, and sugarcane but frequently affected by severe meteorological droughts, like in Zimbabwe and South Africa (Han et al., 2022). Such diverse climatic regimes, coupled with excess reliance on rainfed agriculture and uneven governance capacity, make Africa highly vulnerable to compound and complex drought events. Controlling drought hazard at the continental scale therefore requires approaches that can encapsulate the heterogeneity of the continent’s multi-ecological and multi-climatic nature. Climatic characteristics of the major zones treated in this study are shown in Table 1 (Abdelrahim and Jin, 2025c). 

# _2.2. Data_ 

To monitor and analyze drought situation across the African continent from 2000 to 2024, this study integrates a set of remotely sensed and climatic-based data that provide extensive coverage of both vegetation response and hydroclimatic drivers. Five key variables were selected: The NDVI, LST, Precipitation, SPEI, and VHI. Spatiotemporal analysis of drought development in detail is facilitated by the gridded spatial and monthly temporal resolution of all data sets. 

MODIS MOD13Q1 NDVI is widely accepted as a measure of natural ecosystem and agricultural wet stress sensitivity, and it is used as a proxy for photosynthesis and vegetation condition (Huang et al., 2021; Palagiri and Pal, 2024). LST, derived from MODIS MOD11A2, is a measure of land surface temperature and a reliable indicator of evapotranspiration anomalies, which are reported to be higher in instances of drought (Alexander, 2020; Khorrami and Gunduz, 2020). Precipitation estimates were taken from the Climate Hazards Group InfraRed Precipitation with Station (CHIRPS) dataset, which merges satellite and station data to 

provide accurate rainfall estimates across Africa’s diverse landscapes (Adloff et al., 2022; Khorrami et al., 2024). 

The SPEI was used in this study to detect climatic conditions of dryness across the African continent. In this work, data from SPEI at a 3- month timescale (SPEI-3) was used, which satisfactorily characterizes seasonally based moisture shortages that contribute to crop productivity and vegetation vigor (Dong et al., 2023; He et al., 2024). 3-month scale is a balance of short-term meteorological drought indices and longer hydrological stress, hence a perfect choice for agricultural drought monitoring (Hasan and Abdullah, 2023). SPEI data were retrieved from the SPEIbase v2.7 database, with the 2000–2024-time frame and a spatial resolution of 0.5<sup>◦</sup> (~50 km). This data fusion approach from multiple sources provides a solid foundation on which to establish a continental-scale integrated drought monitoring system that portrays both ecosystem response and climatic forcing (Jiao et al., 2019). Table 2 presents the data characteristics. 

# _2.3. Methodology_ 

The study uses a rigorous, multi-stage methodology to detect and monitor mobile drought fronts across the African continent from 2000 to 2024. The approach is divided into four major stages: harmonization and preprocessing of data, computation of the Multivariate Drought Index Fusion (MDIF), drought detection using the fused index, and drought front advances and dynamics monitoring as shown in Fig. 2. 

# _2.3.1. Data preprocessing_ 

Given the multi-source origin of the datasets, the initial step was a preliminary preprocessing step to ensure spatial and temporal homogeneity. The input datasets NDVI, LST, precipitation, VHI, and SPEI were all re-sampled to a consistent spatial resolution of 0.1<sup>◦</sup> (~10 km), as best 

3 

_N.A.M. Abdelrahim and S. Jin                                                                                                                                                                                                               International Journal of Applied Earth Observation and Geoinformation 144 (2025) 104917_ 

**Table 1** 

The main climatic features and crop systems across Africa’s five major subregions. 

|Region|Climate Type|Main<br>Crops|Rainfall (mm/<br>year)|Drought<br>Vulnerability|
|---|---|---|---|---|
|North<br>Africa|Predominantly<br>arid and semi-<br>arid, with<br>Mediterranean<br>influence along<br>the coast|Wheat,<br>barley,<br>olives,<br>dates|Less than 100<br>mm in the<br>Sahara;<br>200–600 mm<br>in coastal<br>zones|High, driven by<br>persistent water<br>scarcity and<br>advancing<br>desertification|
|West<br>Africa<br>(Guinea<br>Coast)|Humid tropical<br>climate with a<br>bimodal rainfall<br>pattern|Cocoa, oil<br>palm,<br>cassava|1,200–2,500<br>mm|Moderate,<br>though long-<br>term rainfall<br>reductions have<br>heightened<br>drought<br>sensitivity|
|Sahel<br>(West<br>Africa)|Semi-arid,<br>governed by<br>seasonal<br>monsoon rains|Millet,<br>sorghum,<br>livestock|200–600 mm|Very high, with<br>a history of<br>devastating<br>drought<br>episodes such as<br>those of the<br>1980 s|
|East<br>Africa<br>(Horn<br>&Rift<br>Valley)|Semi-arid to sub-<br>humid with two<br>rainy seasons|Maize, tea,<br>coffee|300–1,200<br>mm|Very high, with<br>recurrent<br>droughts linked<br>to ENSO and<br>Indian Ocean<br>Dipole, e.g.,<br>2016–2017|
|Central<br>Africa|Equatorial<br>rainforest|Cassava,<br>plantains,|1,500–2,500<br>mm|Low overall, but<br>susceptible to|
|(Congo<br>Basin)|climate with<br>year-round<br>humidity|maize||occasional short<br>dry spells|
|Southern<br>Africa|Semi-arid to sub-<br>humid,<br>characterized by<br>a unimodal<br>summer rainfall<br>regime|Maize,<br>soybeans,<br>sugarcane|500–1,200<br>mm|High, marked<br>by recent severe<br>droughts such<br>as the<br>2015–2016 El<br>Ni˜no-related<br>event|



practice in continental drought monitoring (Dibs et al., 2023; Ni et al., 2022). The original 16-day and 8-day composites of MODIS-based NDVI and LST data were combined to create monthly means. The monthly timescales were also used to average the weekly NOAA STAR VHI product (García et al., 2016; Patil and Dubey, 2017). To account for the seasonality of drought variability associated with agricultural impacts, SPEI was applied at the 3-month scale (SPEI-3) (Liu et al., 2021; VicenteSerrano et al., 2010). For continuous variables such as NDVI, LST, SPEI, VHI, and reprojection of CHIRPS precipitation data, bilinear 

interpolation (Iman Bin Hussain et al., 2025; Kian Kee Teoh et al., 2008) was applied to ensure spatial consistency and preserve the continuous nature of the data during resolution harmonization (Khorrami et al., 2024; Wu et al., 2019). For uniformity, all datasets were reprojection to WGS84 (EPSG:4326) coordinate system. Non-vegetation surface masking (water surface, urban, barren) was done in this step using MODIS MCD12Q1 land cover classification (Brandt et al., 2016), thus focusing analysis on agriculturally suitable and vegetated surface only. This harmonization routine produced monthly raster stacks for each variable, spatially and temporally consistent over the course of the study. 

# _2.3.2. Multivariate drought Index Fusion (MDIF)_ 

In order to synthesize the drought indications from a mix of indicators, a Multivariate Drought Index Fusion (MDIF) was developed through Principal Component Analysis (PCA) (Abdi and Williams, 2010; Kulkarni et al., 2020) of the preprocessed variables: NDVI, LST, precipitation, SPEI, and VHI. PCA is a widely recognized dimension reduction technique that transforms the variables correlated into uncorrelated principal components, which capture the maximum amount of variance (Esfahanian et al., 2017; Li, 2024). PCA was selected for MDIF due to its robustness, interpretability, and speed of computation, particularly for analysis at the continental scale spanning 25 years. PCA is efficient in lowering dimensionality as well as objectively integrating several indicators of drought by defining the dominant modes of variability (Li, 2024; Schwartz et al., 2022). While PCA assumes linearity among variables and does not always replicate complex nonlinear drought–climate interactions and composite events (e.g., heatwave–drought events), it produces an interpretable and unique composite drought signal that is crucial for operational surveillance. 

Drought-relevant monthly raster stacks were constructed by pixelwise stacking the five variables after normalizing them to standard scales (z-scores). PCA was then calculated pixel-wise both in space and time, with the first principal component (PC1) of maximum variance interpreted as the composite drought stress index (MDIF) (A. Farrag et al., 2020; Abdelrahim and Jin, 2025b). This combined index integrates meteorological drought (SPEI, precipitation), vegetation stress (NDVI, VHI), and thermal moisture stress (LST) and therefore overcomes natural limitations of single-variable drought indices (Li et al., 2024). Separate PCA calculations were conducted for each month to maintain temporal specificity, resulting in a monthly MDIF product for the entire study period. Validation of the MDIF index was conducted by comparing its outputs with VHI and the 3-month Standardized Precipitation Index (SPI-3), computed directly from precipitation data using R Studio. Precipitation data for SPI-3 calculation were used from the CHIRPS dataset (0.05<sup>◦</sup> resolution, monthly) to ensure consistency between the precipitation inputs used within the MDIF framework (Hasan and Abdullah, 2022; Ho et al., 2021). To both spatially and temporally align the two indices, the SPI-3 was upscaled to 0.1<sup>◦</sup> resolution by using bilinear 

**Table 2** 

Datasets and Remote Sensing Sources Used for Multivariate Drought Index Fusion (MDIF). 

|Variable|Dataset Name|Spatial Resolution|Temporal<br>Resolution|Period Covered|Source|
|---|---|---|---|---|---|
|NDVI (Normalized Difference<br>Vegetation Index)|MODIS MOD13Q1|250 m (resampled to 0.1<sup>◦</sup>)|16-day<br>(aggregated<br>monthly)|2000–2024|NASA LP DAAC<br>MODISMOD13Q1|
|LST (Land Surface Temperature)|MODIS MOD11A2|1 km (resampled to 0.1<sup>◦</sup>)|8-day (aggregated<br>monthly)|2000–2024|NASA LP DAAC<br>MODISMOD11A2|
|Precipitation|CHIRPS (Climate Hazards Group<br>InfraRed Precipitation with<br>Station)|0.05<sup>◦</sup>(~5 km)|Monthly|1981–present|CHIRPS Data<br>Portal<br>i|
|SPEI (3-month scale) (Standardized<br>Precipitation Evapotranspiration<br>Index)|SPEIbase v2.7 (3-month<br>aggregation)|0.5<sup>◦</sup>(~50 km)|Monthly (3-month<br>scale)|1901–2021 (recent<br>updates to 2023)|SPEI Official<br>Website|
|VHI (Vegetation Health Index)|NOAA STAR VHI|4 km (aggregated to<br>monthly&resampled to 0.1<sup>◦</sup>)|Weekly<br>(aggregated<br>monthly)|1981–2024|NOAASTAR VHI<br>Download|



4 

_N.A.M. Abdelrahim and S. Jin                                                                                                                                                                                                               International Journal of Applied Earth Observation and Geoinformation_ 

_International Journal of Applied Earth Observation and Geoinformation 144 (2025) 104917_ 



**Fig. 2.** Workflow Diagram Illustrating the MDIF Development and Drought Front Tracking Methodology. 

interpolation and synchronized to the MDIF monthly time steps (2000–2024). 

# _2.3.3. Drought detection using the fused MDIF Index_ 

Following the calculation of the MDIF index, monthly drought status was determined through the application of a threshold-based classification directly on the MDIF values. MDIF values falling below the 60th percentile was classified as drought-affected pixels, in line with standard drought mapping conventions using percentile ranks (Bhuyan-Erhardt et al., 2019; Hao and Singh, 2015). The threshold was chosen to capture moderate-to-severe drought status and avoid minor seasonal variability. Binary drought masks (1 = drought, 0 = non-drought) were generated for each month, developing a 300-month raster series for 2000–2024. Single drought patches with an area smaller than 1,000 km<sup>2</sup> were eliminated by using connected component analysis in order to retain only significant drought areas to be tracked (Chere and Debalke, 2024; Dalezios et al., 2012). This step converted the continuous MDIF outputs into discrete drought event layers, which are suitable for spatiotemporal movement analysis. 

# _2.3.4. Tracking mobile drought fronts_ 

The drought front tracking method operates on spatially contiguous drought clusters from MDIF monthly classifications. The “drought front” refers to a drought-affected contiguous region of pixels (≥1,000 km<sup>2</sup> ) that are classified as moderate-to-extreme drought (MDIF ≤ 60th percentile). The minimum area criterion was implemented to remove local noise and spurious observations that are common in remote sensing data so that the events extracted are meaningful and spatially consistent drought events. Furthermore, this criterion focuses the analysis on big-weather patterns of large-scale drought events of relevance to continental-scale monitoring and regional impact estimation, enhancing computational efficiency and tractability for the 25 years over Africa. The fronts are characterized by using a Connected Component Labeling (CCL) algorithm, consolidating the neighboring drought pixels into separate clusters. To track movement, clusters are linked between adjacent months under two conditions: (1) proximity (centroids ≤ 200 km) and (2) intersecting area (≥20 % spatial overlap). These thresholds suppress spurious linkages without suppressing gradual drought migration patterns. 

Movement velocity and direction are calculated from displacement of affiliated cluster centroids. Velocity (km/month) is the great-circle distance between centroids in month t and month t + 1 divided by the time interval (1 month). Direction is calculated from the azimuth angle between centroid coordinates, with north (0<sup>◦</sup> –360<sup>◦</sup> ). For example, a northeast-southwest trajectory would be ~ 225<sup>◦</sup> azimuth. Centroid movement over time allowed drought front speed and direction to be calculated. While rapidly computable and good for the identification of large-scale patterns of propagation at a continental scale, this method has certain weaknesses. It is too naive regarding sophisticated drought behavior, particularly when patches of drought coalesce, break apart, or experience large-scale shape changes, because the centroid is not necessarily representative of such intricate evolutions. 

Drought fronts were identified empirically from grid cells that were classified as drought using percentile-based MDIF thresholds (extreme ≤ 20th percentile, severe 20–40th, moderate 40–50th, and mild 5060th). Spatial co-aggregation of these drought-affected cells was subsequently used to delineate drought clusters, centroids of which were calculated to obtain the front centroids. Front displacement, velocity, and direction were subsequently derived from the temporal path of these centroids. Thus, the relationship of MDIF values and front properties is not assumed but is a natural consequence of the spatiotemporal distribution of MDIF anomalies. Local frequency of droughts is conveyed in terms of density of drought fronts (number of fronts per pixel over 2000–2024), whereas speed and direction feed into propagation dynamics. MDIF values directly influence front characteristics: small MDIF (extreme drought) results in larger, more persistent fronts, and sharp MDIF declines (e.g., abrupt vegetation stress) could trigger more rapid propagation. For instance, MDIF ≤ 20th percentile (extreme drought) often occur with fronts of speeds _>_ 150 km/month in moisture-sensitive regions like south Africa where the evaporative demand allows for enhanced spread of drought. 

# **3. Results and discussions** 

# _3.1. Development of Multivariate drought Index Fusion (MDIF)_ 

To build the MDIF, we applied PCA to common monthly anomalies in five most significant drought variables: NDVI, LST, Precipitation, SPEI, 

5 

_N.A.M. Abdelrahim and S. Jin_ 

_International Journal of Applied Earth Observation and Geoinformation 144 (2025) 104917_ 

and VHI. These variables both capture vegetation response (NDVI, VHI), atmospheric humidity conditions (SPEI, Precipitation), and heat stress (LST), in line with existing multi-sensor drought methodologies (Bento et al., 2018; Jiao et al., 2019). Prior to PCA, every variable was standardized to z-scores to remove unit differences as well as to offer equal weighting during the decomposition process (Esfahanian et al., 2017). 

PCA analysis revealed that PC1 accounted for 75 % of the variance, which is sufficient to develop a fused drought index. The eigenvector values for PC1 indicated that VHI (0.402) and SPEI (0.338) were the highest positive contributors, followed by NDVI (0.316) and Precipitation (0.261). In contrast, LST (− 0.317) was a negative contributor since drought severity is negatively correlated with it; an increase in temperature aggravates drought stress (Abdelrahim and Jin, 2025b; Hazaymeh and Hassan, 2017). 

The MDIF values were subsequently scaled between 0 % and 100 %, where 100 % indicates no drought (normal temperatures, good vegetation, normal rainfall) and 0 % indicates extreme drought (high temperatures, severe vegetation stress, rainfall deficit). In operational classification, the MDIF values were divided into five classes of drought severity: no drought (60–100 %), mild drought (50–60 %), moderate drought (40–50 %), severe drought (20–40 %), and extreme drought (0–20 %). This is a classification strategy in line with common thresholds used in global drought monitoring systems, e.g., the Vegetation Health Index (Kogan, 1995) and the SPEI method (Vicente-Serrano et al., 2010). 

By bringing together multiple drought-sensitive parameters in a single index, MDIF offers a robust, multivariate representation of drought status across Africa, overcoming the deficiencies of singlevariable indices. By this integration method, both meteorological forcing and ecosystem response are detected, making more vigorous spatial and temporal observation of drought dynamics possible (Chere and Debalke, 2024; Hasan and Abdullah, 2023). 

To ensure the performance of the newly established MDIF, its outputs were first cross-compared with the internationally recognized SPI at a 3- month timescale (SPI-3). SPI values were calculated from precipitation data using R Studio, and monthly SPI-3 maps for the 2000–2024 period were generated. Pearson correlation analysis at the pixel level between MDIF and SPI-3 across Africa revealed high correlations of 0.72 to 0.84 (p _<_ 0.05) in semi-dry and dry areas such as the Sahel, the Horn of Africa, and Southern Africa (Figs. 3a, b), confirming that MDIF is able to detect precipitation-induced drought signals (Bhuyan-Erhardt et al., 2019; Liu et al., 2021). 

To further extend the validation beyond meteorological drought, MDIF was also correlated against the Vegetation Health Index (VHI), which is a combination of NDVI and LST to represent vegetation and thermal stress, respectively. The correlation showed even stronger correlations, ranging from 0.76 to 0.87 (p _<_ 0.05), particularly over vegetated regions (Figs. 3c, d). This confirms that MDIF, apart from capturing rainfall anomalies, is equally well correlated with ecological drought indices. 



**Fig. 3.** Validation of the Multivariate Drought Index Fusion (MDIF) against benchmark indices. Panels (a) and (b) show the spatial distribution and density of Pearson correlation coefficients between MDIF and SPI-3 (precipitation-based meteorological drought index). Panels (c) and (d) show the corresponding correlation analysis between MDIF and VHI (vegetation and thermal stress index). Both validations indicate strong and statistically significant correlations (p _<_ 0.05), confirming that MDIF captures both meteorological and ecological drought components across Africa. 

6 

_International Journal of Applied Earth Observation and Geoinformation 144 (2025) 104917_ 

_N.A.M. Abdelrahim and S. Jin_ 

Across vegetated regions, MDIF also exhibited strong coherence with observed drought occurrences, such as the 2016–2017 East African drought (Han et al., 2022) and the 2002–2003 southern African drought (Zeng et al., 2023). Spatial overlays also confirmed that drought clusters identified by MDIF were well aligned with historical drought impact zones reported by Rhein and Jansesberger, (2024). These validation results confirm that MDIF not only confirms meteorological drought indices like SPI but also offers enhanced sensitivity by incorporating vegetation and thermal stress components, thus producing a more unified portrayal of drought. 

# _3.2. Spatiotemporal distribution of drought conditions across Africa_ 

The drought regimes across Africa between 2000 and 2024, as implied from the MDIF index, depict a very dynamic and regionally varying pattern of water stress. During the early 2000 s (2000–2004), Southern Africa always stood out as a drought hotspot as indicated in Fig. 4, with severe drought prevailing in more than 60 % of the subregion in 2001–2002, covering countries such as Namibia, Botswana, and South Africa. Concurrently, the Horn of Africa experienced chronic drought stress, while the Sahel became increasingly dry, particularly in its western parts. These regional droughts often propagated along a northeast-to-southwest axis, consistent with the dominant propagation pathway shown in Fig. 9. 

Between 2005 and 2009, drought severity again came back over Southern Africa, with its worst form in 2005 when over 70 % of the region faced severe to extreme conditions. The Horn of Africa concurrently faced some of its worst drought years, especially in 2006. Southern Africa received temporary relief in 2007, but the Horn and Sahel areas continued to face extensive dryness, as severe indicators of drought again returned in 2008–2009. These years witnessed the consolidation of the Horn of Africa as a persistent drought hot spot, whereas the Sahel showed migrating bands of moderate to severe drought stress. 

The period 2010–2015 registered some of the worst and most widespread droughts in decades. The 2010–2011 Horn of Africa drought covered nearly 80–90 % of the region, with the Sahel indicating sharply defined drought stripes in its central and eastern parts. Southern Africa entered another desperate drought phase in 2012–2015, culminating in 2015 when nearly 75 % of the region was affected. These large-scale droughts were directionally coherent, with the vectors of propagation localized in the northeast-to-southwest quadrant (Fig. 9b). 

From 2016 to 2023, Africa continued to experience repetitive, largescale drought incidents. Southern Africa suffered from severe drought during the year 2016, which was a multi-year extreme event, while the Horn of Africa was once more engaged in a prolonged period of exceptional drought from 2017. This three-year interval (2017–2019) saw the Horn and East Africa under the continuous effect of severe to extreme stress, with maps showing intense red hues over large areas. Southern Africa experienced more varied conditions after 2017, with some recovery in some regions but others remaining dry, particularly in the far south and west. The Sahel region showed strong dryness over its western and central sectors in these years. The final maps for 2020–2023 display the persistent vulnerability of the Horn of Africa, which was under extreme drought through 2022–2023—visually one of the most severe in the whole record. Southern Africa also saw persistent moderate to severe drought in its western and central parts, and the Sahel displayed repeated stripes of moderate dryness. 

During the whole 2000–2024 period, the Horn of Africa was the driest part of the continent, often affected by hard and prolonged crises, most notably in 2006, 2010–2011, 2017–2019, and 2022–2023 as shown in fig. 5. Southern Africa also experienced various large-scale drought episodes, including extensive multi-year periods during roughly 2001–2002, 2005–2006, and 2014–2017, with spillovers into the 2020 s. The Sahel also had high year-to-year variability, with alternation in intensity of drought latitudinally and longitudinally but 

often recurring. 

North Africa, controlled by the Sahara Desert, consistently gave dry MDIF signals, characteristic of its typical hyper-arid climate rather than intermittent drought anomalies. Central Africa, in contrast, was relatively less affected by large-scale extreme drought but experienced peripheral incursions of dryness during years of broader regional drought. Most significantly, the no clear continent-scale intensifying or disappearing trend of drought is apparent. Instead, a pattern emphasizes the complex interplay of regional climate drivers, namely oceanatmospheric teleconnections and land-atmospheric feedbacks, that has led to a chronic susceptibility and sensational spatiotemporal variability of drought occurrence in Africa over the past two decades. 

To facilitate simple interpretation of Fig. 5, the categories of drought (mild, moderate, severe, and extreme) were determined using percentile cutoff values of the MDIF distribution: extreme drought at or below the 20th percentile, severe drought between the 20th and 40th percentiles, moderate drought between the 40th and 50th percentiles, and mild drought between the 50th and 60th percentiles. This percentile-based grouping is also in agreement with commonly employed methodologies in global drought monitoring (Kogan, 1995; Hao and Singh, 2015), in that severity levels are directly comparable between regions and years. Fig. 5 therefore illustrates, for each African subregion and year, the proportion of land surface that falls within these standardized ranges of drought. 

To improve the demonstration of spatial consistency and performance of the MDIF, we present comparison maps of spatial distribution of MDIF, VHI, and SPI-3 for typical periods of extreme drought events in Africa. 

These maps provide visual validation of the ability of MDIF to reproduce the spatial area and intensity of the drought condition. Fig. 6 graphs MDIF versus VHI and SPI-3 for the 2011, 2019, and 2023 drought years. For each of these years, MDIF has excellent spatial correspondence with both indices, highlighting the 2011 Horn of Africa disaster, the 2019 South African drought, and the more heterogeneous 2023 condition. There are minor spatial variations, yet MDIF always indicates the spatial extent and severity of drought according to both precipitation- and vegetation-based criteria. These graphical results reinforce the statistical associations and highlight MDIF’s potential in merging meteorological and ecological indicators of drought into a coherent and reliable observing paradigm. Improvement in the future is through the integration of soil moisture data and application of machine learning models for detecting nonlinear drought drivers. Overall, MDIF is a sound, scalable, and operational tool for observing Africa-wide droughts, providing more perceptive perspectives on evolving drought risk in the continent. 

# _3.3. Spatiotemporal dynamics of drought movement_ 

Spatial and temporal examination of drought propagation across Africa according to observed drought front density, velocity, and dominating direction trends reveals complex regional disparities and varying drought migration pathways that reflect underlying climatic forcing and land–atmosphere coupling. 

The density map (Fig. 7a) reveals definitive drought front hotspots that have suffered multiple invasions of drought occurrences over the past two decades. Notably, southern Madagascar is one epicenter with the largest number of front occurrences, a maximum of 120 drought fronts, and during the observation period, being among the longest drought-affected places on the continent. This aligns with recent worstcase droughts that have precipitated humanitarian crises in the region. Similarly, north Algeria and Libya of the northern Sahel–Sahara transitional zone also show high drought density, more than 100 occurrences, and reflective of multiple drought initiation or persistence along this climatic boundary. 

There are other regions with moderate density hotspots (30 to 80 fronts) across east Ethiopia, north Somalia in the Horn of Africa, south 

7 

_International Journal of Applied Earth Observation and Geoinformation 144 (2025) 104917_ 

_N.A.M. Abdelrahim and S. Jin                                                                                                                                                                                                               International Journal of Applied Earth Observation and Geoinformation_ 



**Fig. 4.** Spatiotemporal distribution of drought severity, with reddish hues indicating drought intensity and bluish hues representing wetter conditions. This figure highlights persistent hotspots in the Horn of Africa and Southern Africa, as well as shifting drought patterns over the 24-year period. 

8 

_N.A.M. Abdelrahim and S. Jin_ 

_International Journal of Applied Earth Observation and Geoinformation 144 (2025) 104917_ 



**Fig. 5.** Timeline of Major Drought Episodes Across African Regions (2000–2024). The horizontal bars represent drought severity (moderate, severe, extreme) and spatial extent for five sub-regions: North Africa, West Africa, Central Africa, East Africa, Southern Africa, and the Sahel. Notable events include the 2011 Horn of Africa extreme drought and the 2015–2017 Southern Africa multi-year crisis. 

Angola, north Botswana, and mid-Sudan. These are secondary hotspots where drought occurrence frequencies have been considerably higher, pointing towards their vulnerability to monsoon failure as well as atmospheric circulation anomalies (Han et al., 2022; Samasse et al., 2018). Conversely, regions such as Central Africa have low front density, which indicates their relative hydrological stability due to equable tropical rain regimes. 

The average drought front rate map (Fig. 7b) reveals steep regional variations in the speed with which drought progresses. The highest spreading rates are widespread over south Angola, north Namibia, and south Mozambique, with initial speeds approximated to be as much as 180 km/month. These extreme spreading rates indicate high flash drought susceptibility, where evapotranspiration deficits and excessive evapotranspiration drive swift and severe moisture stress escalation (Bhuyan-Erhardt et al., 2019). 

Moderate rates of propagation between 75 and 125 km/month dominate across the Sahel’s eastern part (Chad, Sudan) and western Ethiopia and reflect seasonally recurring pulses of drought linked with monsoonal variation. Central Africa and coastal West Africa, however, have the lowest rates, typically below 50 km/month, as would be anticipated from their stable precipitation inputs and thick overlying vegetation cover that attenuate abrupt drought progress. 

The coincidence of high drought density and high-speed propagation across southern Africa exposes this sub-region to both repeat and rapidonset drought emergencies. The dynamic poses significant challenges to early warning and response systems that need to act on both chronic and acute drought threats. 

The temporal variability of movable drought fronts in Africa is depicted in Fig. 8. With significant inter-annual variability of alternating peaks and minima associated with widespread or limited drought activity, Fig. 8a shows the number of drought fronts that occur each year. The impact of dominant climate modes, including ENSO, IOD, and AMO, which regulate rainfall and the prevalence of drought across the continent, is consistent with variability. Fig. 8b presents the average yearly rate of drought front propagation in km/month with the same variability. High-speed years are in line with rapid spreading of droughts under strong atmospheric forcing or parched initial conditions, while low-speed years indicate more localized development. Overall, the results emphasize the frequency and mobility of the drought fronts and their dynamic time evolution. 

Directional analysis (Fig. 9 a and b) confirms a strong and continuous 

northeast-to-southwest axis of drought advancement across Africa. The most common vector direction (0<sup>◦</sup> –45<sup>◦</sup> sector) has over 200 observed fronts, which identifies this pathway as the overall trend of movement over the 25-year observation period. This dominant pathway suggests a teleconnection of drought onset in the Horn of Africa and northern Sahel and follow-through propagations towards central and southern Africa, mostly during El Nino and positive Indian Ocean Dipole (IOD) phases ˜ (Ogunrinde et al., 2024; Zeng et al., 2023). Secondary movement patterns include: Eastward dispersion (90<sup>◦</sup> ), particularly evident over the Sahel and south Africa, relating to lateral displacements in bands of droughts linked with zonal wind anomalies. Southward propagation (180<sup>◦</sup> ) with 50–75 occurrences, occurring mostly over eastern Africa, and Westward displacement (270<sup>◦</sup> ), though less frequent (~40 occurrences), relating to isolated east-to-west drought migration events. The movement of drought fronts is not random but happens in unique regional patterns, and There are specific regions more prone to drought front activity, indicating increased vulnerability. The speed of drought front propagation varies across the continent, impacting predictability and influence of drought events. 

Fig. 10 shows the spatial structure of drought front centroids, with each representing the centroid of a drought patch. Dense clustering appears over the Sahel, the Horn of Africa, and Southern Africa, confirming them to be chronic drought hotspots with frequent and extensive events. The Congo Basin and coastal West African regions have low centroid density, as would be expected from their humid settings and higher rainfall stability. Extended clusters, particularly from the Sahel to the southwest and extending across Southern Africa, highlight dominant corridors of drought propagation. The spatial perspective complements the temporal analysis by both identifying areas prone to drought and identifying giant drought mobility corridors across the continent. 

# _3.4. Discussion_ 

This article introduces a novel continental-scale monitoring system for mobile drought dynamics in Africa using the Multivariate Drought Index Fusion (MDIF). Through the integration of different remote sensing and climatic indicators (NDVI, LST, precipitation, SPEI, VHI) with principal component analysis (PCA), MDIF outperforms static assessments to quantify the dynamic expansion of drought fronts. 

Validation confirmed MDIF’s robustness, with significant correlations with SPI-3 and VHI (r = 0.72–0.84 and r = 0.76–0.87, respectively, 

9 

_International Journal of Applied Earth Observation and Geoinformation 144 (2025) 104917_ 



**Fig. 6.** Spatial Distribution Comparison of Drought Indices for Selected Years. Maps show drought conditions across Africa for (a) 2011, (b) 2019, and (c) 2023, as depicted by MDIF (left column), VHI (middle column), and SPI-3 (right column). Red/orange colors indicate drier conditions, while blue/green colors indicate wetter conditions. The visual consistency across indices highlights MDIF’s robust performance in capturing the spatial extent and severity of drought events. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.) 

10 

_International Journal of Applied Earth Observation and Geoinformation 144 (2025) 104917_ 

_N.A.M. Abdelrahim and S. Jin                                                                                                                                                                                                               International Journal of Applied Earth Observation and Geoinformation_ 



**Fig. 7.** Drought Front Density and Propagation Speed Across Africa. (a) Density Map: Hotspots of recurrent drought fronts (e.g., southern Madagascar, northern Sahel) with counts exceeding 100 fronts. (b) Speed Map: Regional contrasts in propagation velocity, with southern Africa experiencing rapid movements ( _>_ 150 km/ month) and Central Africa showing slower speeds ( _<_ 50 km/month). 



**Fig. 8.** Temporal Dynamics of Mobile Drought Fronts Across Africa (2000–2024). (a) Yearly count of identified mobile drought fronts, illustrating inter-annual variability in drought occurrence. (b) Average annual speed of mobile drought fronts (km/month), showing variations in propagation velocity over time. 

11 

_International Journal of Applied Earth Observation and Geoinformation 144 (2025) 104917_ 

_N.A.M. Abdelrahim and S. Jin                                                                                                                                                                                                               International Journal of Applied Earth Observation and Geoinformation_ 



**Fig. 9.** Dominant Propagation Directions of Drought Fronts. Rose diagrams depict azimuthal trends in drought front movement. The dominant northeast-tosouthwest axis (0<sup>◦</sup> –45<sup>◦</sup> ) aligns with teleconnections driving drought migration, while secondary eastward (90<sup>◦</sup> ) and southward (180<sup>◦</sup> ) patterns reflect regional climatic variability. 



**Fig. 10.** Density of Mobile Drought Front Centroids Across Africa (2000–2024). The concentration of points indicates regions with higher frequency and spatial extent of mobile drought events, highlighting persistent drought hotbeds and dominant propagation corridors. Each point represents the centroid of a detected drought patch. 

12 

_N.A.M. Abdelrahim and S. Jin_ 

in arid areas). This reflects its capability to monitor meteorological, agricultural, and ecological drought simultaneously. Compared to rainfall indices, MDIF successfully delineated the severe 2019–2021 Madagascar drought and accurately marked the 2016–2017 East African and 2002–2003 Southern African droughts, confirming with FAO (2022) and past studies (Han et al., 2022; Zeng et al., 2023). Drought front centrifugal spatial density noticeably separates chronic hotspots. Highest concentration levels were observed in the Horn of Africa, the Sahel, and Southern Africa, with the Horn region alone recording over 100 events on average. Such trends confirm their perennial exposure to dryness. MDIF’s ability to compile vegetation within regions where the precipitation indices are weak complements such area observation. 

The response of MDIF to drought is shaped by the varying behavior of its input indicators across Africa’s diverse climatic zones. In hyperarid regions such as North Africa, vegetation indicators like NDVI show limited variability, so MDIF tends to be more strongly influenced by meteorological components such as SPEI and precipitation. In contrast, in humid equatorial regions, NDVI remains relatively stable, and drought detection relies more on anomalies in rainfall and soil water balance. Semi-arid regions, including the Sahel and Southern Africa, exhibit strong LST responses to water stress due to rapid declines in evapotranspiration, making thermal indicators a dominant driver of MDIF variability. These regional contrasts mean that while a uniform percentile threshold facilitates continental comparison, it may not fully capture local drought severity. 

Tracking analysis revealed high spatial and temporal heterogeneity of drought mobility. Maximum velocities were in years such as 2000, 2003, 2008, and 2019, in correspondence with inter-annual fluctuations in atmospheric and land-surface conditions. Regionally, most significant velocities were in Southern Africa, at velocities of up to 180 km/month over Angola, Namibia, and Mozambique, in consistency with its flash drought susceptibility and high evaporative demand (Bhuyan-Erhardt et al., 2019; Bento et al., 2020). The Sahel had moderate rates (75–125 km/month), which reflect its intermediate climate, while Central Africa displayed the lowest movement (25–50 km/month) due to more rainfall buffering. The moving bands seen in the Sahel reflect past drought belt movements associated with monsoon variability (Samasse et al., 2018). Directional analysis further revealed a dominant Sonoran northeast-tosouthwest direction (Fig. 9) that implies that droughts tend to initiate in the Horn and Sahel and propagate into Eastern and Southern Africa. This is corroborated by studies linking propagation with large-scale teleconnections such as AMO and SOI, while the shifting drought belts in the Sahel align with monsoon variability (Ogunrinde et al., 2024). 

The successful development and validation of the MDIF for continental-scale drought monitoring in Africa suggest its strong potential for extensibility to other regions globally. However, for optimal performance and accurate representation of local drought conditions, direct application would require careful regional calibration. This includes re-deriving PCA component loadings and re-establishing percentile-based drought severity thresholds using historical data specific to the target region. Furthermore, local validation against groundbased observations would be essential to confirm the adapted MDIF’s accuracy and reliability in diverse climatic and ecological contexts. This adaptability highlights the broad utility of our framework for enhancing global drought monitoring capabilities. 

The real-time data on the speed, direction, and density of drought fronts provide actionable information for downstream impact forecasting, constituting a useful supplement to traditional static maps of drought. This method significantly enhances capacity for early warning and enables transboundary management of drought, particularly where events blur across borders. In spite of its important contributions, this research has some limitations. Methodologically, although PCA effectively aggregates a set of indicators, it requires linearity and thus possibly does not capture completely nonlinear interactions, i.e., compound heatwave-drought effects. The application of a homogenous 60th percentile threshold at the continental scale, although it guarantees 

_International Journal of Applied Earth Observation and Geoinformation 144 (2025) 104917_ 

comparability, possibly does not catch local drought intensity due to the heterogeneity of climatic zones in Africa. For instance, the MDIF in hyper-arid regions is controlled by meteorological factors, and thermal indicators prevail in semi-arid regions. Furthermore, the minimum patch size of 1,000 km<sup>2</sup> precludes localized events, and monthly temporal resolution can potentially miss capturing rapid-onset flash droughts. 

Future researches should address these constraints by constructing adaptive thresholds calibrated by climate zones or ecosystems to maximize local sensitivity. Increased product frequency (e.g., dekadal NDVI/LST, weekly soil moisture) would improve flash drought detectability and more accurately estimate front speed and direction. Combining microwave-based soil moisture observations (e.g., SMAP, ESA CCI) would better represent root-zone droughts in areas with cloud contamination. Also, transitions into PCA-machine learning model integration (e.g., autoencoders, random forests) could enhance detection of complex, nonlinear causes of drought. Quantifying the influence of leading ocean–atmosphere teleconnections (ENSO, IOD, AMO) on observed propagation patterns using direct correlation and regression analysis is one central direction of research. Finally, large-scale ground verification against streamflow, crop damage, and impact data is essential to improve the utility of MDIF for early warning applications. 

# **4. Conclusions** 

This study offers a stringent spatiotemporal analysis of African drought variability over 2000–2024 underpinned by a novel Multivariate Drought Index Fusion (MDIF) technique. Combining NDVI, LST, precipitation, SPEI, and VHI using PCA, MDIF captures both meteorological and ecological drought indices, with broader sensitivity than traditional single-variable ones. Validation with SPI-3 and VHI determined strong correlations (r = 0.72 to 0.84 and r = 0.76 to 0.87 respectively) in arid regions such as the Sahel, the Horn of Africa, and Southern Africa, which validate the framework. The outcomes determine established hotspots, particularly the Horn of Africa, with recurring crises in 2006, 2010–2011, 2017–2019, and 2022–2023. Southern Africa experienced multi-annual drought events in 2001–2002, 2005–2006, and 2014–2017, and the Sahel experienced recurring bands of high variability drought. The droughts progressed from northeast to southwest, with the fastest forward movement in Southern Africa. These findings align with earlier drought chronologies and confirm the use of the MDIF framework. 

In addition to its scientific significance, MDIF has implications for operation in early warning, drought risk estimation, and policy response. The framework can guide African governments and regional institutions for improving readiness and adjustment towards drought disasters. MDIF is a robust, scalable, and operational tool for Africa-wide drought monitoring, which provides enhanced insights into evolving drought risks across the continent. 

Funding. 

This work was supported by the Henan International Science and Technology Cooperation Key Project (Grant No. 241111520700), Henan Department of Education’s “Double First-Class” Project (Grant No. 760507/033) and Henan Polytechnic University Startup Foundation Project (Grant No. 722403/067/002). 

The datasets used in this study are publicly accessible from the following sources: 

NDVI: MODIS MOD13Q1 Version 6.1 (250 m resolution, 16-day composites) was sourced from NASA’s Land Processes Distributed Active Archive Center (LP DAAC) at https://lpdaac.usgs.gov/produ cts/mod13q1v061/. Monthly aggregates were generated from 16-day data. LST: MODIS MOD11A2 Version 6.1 (1 km resolution, 8-day composites) was obtained from NASA LP DAAC at https://lpdaac.usgs. gov/products/mod11a2v061/. Monthly means were computed from 8- day data. Precipitation: Climate Hazards Group InfraRed Precipitation with Station (CHIRPS) v2.0 (0.05<sup>◦</sup> resolution, monthly) was acquired 

13 

_N.A.M. Abdelrahim and S. Jin_ 

from the CHIRPS Data Portal at https://www.chc.ucsb.edu/data/chirps. SPEI-3: Standardized Precipitation Evapotranspiration Index (3-month scale, 0.5<sup>◦</sup> resolution) was derived from SPEIbase v2.7 at https://spei.cs ic.es/database.html. VHI: Vegetation Health Index (4 km resolution, weekly) was downloaded from NOAA STAR at https://www.star.nesdis. noaa.gov/smcd/emb/vci/VH/vh_browse.php and aggregated to monthly. Land Cover: MODIS MCD12Q1 Version 6.1 (500 m resolution) for non-vegetation masking was sourced from NASA LP DAAC at https: //lpdaac.usgs.gov/products/mcd12q1v061/. 

# **CRediT authorship contribution statement** 

**Nasser A.M. Abdelrahim:** Supervision. **Shuanggen Jin:** Writing – review & editing, Supervision, Resources, Project administration, Investigation, Funding acquisition. 

# **Declaration of competing interest** 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

# **Data availability** 

i have shared the link to my data 

# **References** 

- Abdelrahim, N.A.M., Jin, S., 2025a. Genetic Algorithm Optimized Multispectral SoilVegetation Drought Index (GA-MSVDI) for precision agriculture and drought monitoring in North Africa. Remote Sens. Appl.: Soc. Environ. 38, 101603. https:// doi.org/10.1016/j.rsase.2025.101603. 

- Abdelrahim, N.A.M., Jin, S., 2025b. A Novel Agricultural Remote Sensing Drought Index (ARSDI) for high-resolution drought assessment in Africa using Sentinel and Landsat data. Environ. Monit. Assess. 197, 242. https://doi.org/10.1007/s10661-025-136863. 

- Abdelrahim, N.A.M., Jin, S., 2025c. Continental maize mapping and distribution in Africa by integrating radar and optical imagery. Environ. Monit. Assess. 197, 1072. https://doi.org/10.1007/s10661-025-14502-8. 

- Abdi, H., Williams, L.J., 2010. Principal Component Analysis. Wires Computational Stats 2, 433–459. https://doi.org/10.1002/wics.101. 

- Adhikari, S., Zhou, W., Dou, Z., Sakib, N., Ma, R., Chaudhari, B., Liu, B., 2024. Analysis of Flash Drought and its Impact on Forest Normalized Difference Vegetation Index (NDVI) in Northeast China from 2000 to 2020. Atmos. 15, 818. https://doi.org/ 10.3390/atmos15070818. 

- Adloff, M., Singer, M.B., MacLeod, D.A., Michaelides, K., Mehrnegar, N., Hansford, E., Funk, C., Mitchell, D., 2022. Sustained Water Storage in Horn of Africa Drylands Dominated by Seasonal Rainfall Extremes. Geophys. Res. Lett. 49, e2022GL099299. https://doi.org/10.1029/2022GL099299. 

- Ajaz, A., Taghvaeian, S., Khand, K., Gowda, P.H., Moorhead, J.E., 2019. Development and Evaluation of an Agricultural Drought Index by Harnessing Soil Moisture and Weather Data. Water 11, 1375. https://doi.org/10.3390/w11071375. 

- Alasow, A.A., Hamed, M.M., Rady, M., Arab, M.A., Muhammad, M.K.I., Shahid, S., 2024. Spatiotemporal analysis of soil moisture drought in the Horn of Africa. Theor. Appl. Climatol. 155, 7165–7176. https://doi.org/10.1007/s00704-024-05052-z. 

- Alexander, C., 2020. Normalised difference spectral indices and urban land cover as indicators of land surface temperature (LST). Int. J. Appl. Earth Obs. Geoinf. 86, 102013. https://doi.org/10.1016/j.jag.2019.102013. 

- Ali, S., Khorrami, B., Jehanzaib, M., Tariq, A., Ajmal, M., Arshad, A., Shafeeque, M., Dilawar, A., Basit, I., Zhang, L., Sadri, S., Niaz, M.A., Jamil, A., Khan, S.N., 2023. Spatial Downscaling of GRACE Data based on XGBoost Model for improved Understanding of Hydrological Droughts in the Indus Basin Irrigation System (IBIS). Remote Sens. (Basel) 15, 873. https://doi.org/10.3390/rs15040873. 

- Bento, V.A., Gouveia, C.M., DaCamara, C.C., Libonati, R., Trigo, I.F., 2020. The roles of NDVI and Land Surface Temperature when using the Vegetation Health Index over dry regions. Global Planet. Change 190, 103198. https://doi.org/10.1016/j. gloplacha.2020.103198. 

- Bento, V.A., Gouveia, C.M., DaCamara, C.C., Trigo, I.F., 2018. A climatological assessment of drought impact on vegetation health index. Agric. For. Meteorol. 259, 286–295. https://doi.org/10.1016/j.agrformet.2018.05.014. 

- Beyene, T.K., Agarwal, A., Jain, M.K., Yadav, B.K., 2023. Investigation of the propagation of meteorological to hydrological drought and water required to recover from drought over Ethiopian basins. J. Water Clim. Change 14, 2988–3009. https://doi. org/10.2166/wcc.2023.024. 

- Bhuyan-Erhardt, U., Erhardt, T.M., Laaha, G., Zang, C., Parajka, J., Menzel, A., 2019. Validation of drought indices using environmental indicators: streamflow and 

_International Journal of Applied Earth Observation and Geoinformation 144 (2025) 104917_ 

- carbon flux data. Agric. For. Meteorol. 265, 218–226. https://doi.org/10.1016/j. agrformet.2018.11.016. 

- Bilal, S.B., Gupta, V., 2024. Deciphering the spatial fingerprint of drought propagation through precipitation, vegetation and groundwater. Intl Journal of Climatology 44, 4443–4461. https://doi.org/10.1002/joc.8590. 

- Brandt, M., Hiernaux, P., Rasmussen, K., Mbow, C., Kergoat, L., Tagesson, T., Ibrahim, Y. Z., W´el´e, A., Tucker, C.J., Fensholt, R., 2016. Assessing woody vegetation trends in Sahelian drylands using MODIS based seasonal metrics. Remote Sens. Environ. 183, 215–225. https://doi.org/10.1016/j.rse.2016.05.027. 

- C´er´eghino, R., Park, Y.-S., 2009. Review of the Self-Organizing Map (SOM) approach in water resources: Commentary. Environ. Model. Software 24, 945–947. https://doi. org/10.1016/j.envsoft.2009.01.008. 

- Chere, Z., Debalke, D.B., 2024. Modeling agricultural drought based on the earth observation-derived standardized precipitation evapotranspiration index and vegetation health index in the northeastern highlands of Ethiopia. Nat. Hazards 120, 3127–3151. https://doi.org/10.1007/s11069-023-06320-3. 

- Choukri, M., Laamrani, A., Chehbouni, A., 2024. Use of Optical and Radar Imagery for Crop Type Classification in Africa: a Review. Sensors 24, 3618. https://doi.org/ 10.3390/s24113618. 

- Dalezios, N.R., Blanta, A., Spyropoulos, N.V., 2012. Assessment of remotely sensed drought features in vulnerable agriculture. Nat. Hazards Earth Syst. Sci. 12, 3139–3150. https://doi.org/10.5194/nhess-12-3139-2012. 

- Dibs, H., Ali, A.H., Al-Ansari, N., Abed, S.A., 2023. Fusion Landsat-8 thermal TIRS and OLI Datasets for Superior monitoring and Change Detection using Remote Sensing. Emerg Sci J 7, 428–444. https://doi.org/10.28991/ESJ-2023-07-02-09. 

- Dong, J., Xing, L., Cui, N., Zhao, L., Guo, L., Gong, D., 2023. Standardized precipitation evapotranspiration index (SPEI) estimated using variant long short-term memory network at four climatic zones of China. Comput. Electron. Agric. 213, 108253. https://doi.org/10.1016/j.compag.2023.108253. 

- Du, L., Tian, Q., Yu, T., Meng, Q., Jancso, T., Udvardy, P., Huang, Y., 2013. A comprehensive drought monitoring method integrating MODIS and TRMM data. Int. J. Appl. Earth Obs. Geoinf. 23, 245–253. https://doi.org/10.1016/j. jag.2012.09.010. 

- Edokossi, K., Calabia, A., Jin, S., Molina, I., 2020. GNSS-Reflectometry and Remote Sensing of Soil Moisture: a Review of Measurement Techniques, Methods, and applications. Remote Sens. (Basel) 12, 614. https://doi.org/10.3390/rs12040614. 

- Elameen, A.M., Jin, S., Olago, D., 2023. Identification of drought events in major basins of Africa from GRACE total water storage and modeled products. Photogramm. Eng. Remote Sens. 89, 221–232. 

- Esfahanian, E., Nejadhashemi, A.P., Abouali, M., Adhikari, U., Zhang, Z., Daneshvar, F., Herman, M.R., 2017. Development and evaluation of a comprehensive drought index. J. Environ. Manage. 185, 31–43. https://doi.org/10.1016/j. jenvman.2016.10.050. 

- Fao, 2022. Drought in the Horn of Africa – Rapid response and mitigation plan to avert a humanitarian catastrophe. FAO. https://doi.org/10.4060/cb8280en. 

- FAO, F., 2023. The State of Food Security and Nutrition in the World 2023. FAO; IFAD; UNICEF; WFP; WHO; https://doi.org/10.4060/cc3017en. 

- Farrag, A., Mostafa, Y., Mohamed, N., 2020. Detecting land cover changes using VHR satellite images: A comparative study. J. Eng. Sci. 48, 200–211. https://doi.org/ 10.21608/jesaun.2019.264927. 

- Feng, X., Wang, Z., Wu, X., Huang, S., Li, J., Lai, C., Zeng, Z., Lin, G., 2025. Tracking 3D drought events across global river basins: climatology, spatial footprint, and temporal changes. Geophys. Res. Lett. 52, e2024GL111442. https://doi.org/ 10.1029/2024GL111442. 

- García, S., Ramírez-Gallego, S., Luengo, J., Benítez, J.M., Herrera, F., 2016. Big data preprocessing: methods and prospects. Big Data Anal. 1, 9. https://doi.org/10.1186/ s41044-016-0014-0. 

- Gorugantula, S.S., Kambhammettu, B.P., Lakshmi, S.J., Regonda, S.K., 2025. Multivariate drought indices to analyse spatiotemporal drought propagation in a semi-arid river basin. Theor. Appl. Climatol. 156, 36. https://doi.org/10.1007/ s00704-024-05236-7. 

- Han, X., Li, Y., Yu, W., Feng, L., 2022. Attribution of the Extreme Drought in the Horn of Africa during Short-Rains of 2016 and Long-Rains of 2017. Water 14, 409. https:// doi.org/10.3390/w14030409. 

- Hao, Z., Singh, V.P., 2015. Drought characterization from a multivariate perspective: a review. J. Hydrol. 527, 668–678. https://doi.org/10.1016/j.jhydrol.2015.05.031. 

- Hasan, I.F., Abdullah, R., 2023. Multivariate index for monitoring drought (case study, Northeastern of Iraq). Nat. Hazards 116, 3817–3837. https://doi.org/10.1007/ s11069-023-05837-x. 

- Hasan, I.F., Abdullah, R., 2022. Agricultural drought characteristics analysis using copula. Water Resour. Manag. 36, 5915–5930. https://doi.org/10.1007/s11269022-03331-w. 

- Hassan, A., Jin, S.G., 2016. Water storage changes and balances in Africa observed by satellite gravimetry and hydrologic models. Geod. Geodyn. 7 (1), 39–49. https://doi. org/10.1016/j.geog.2016.03.002. 

- Hazaymeh, K., Hassan, Q.K., 2017. A remote sensing-based agricultural drought indicator and its implementation over a semi-arid region. Jordan. J. Arid Land 9, 319–330. https://doi.org/10.1007/s40333-017-0014-6. 

- He, Y., Xie, Y., Liu, J., Hu, Z., Liu, J., Cheng, Y., Zhang, L., Wang, Z., Li, M., 2024. Generation of 1 km high resolution Standardized precipitation evapotranspiration Index for drought monitoring over China using Google Earth Engine. Int. J. Appl. Earth Obs. Geoinf. 135, 104296. https://doi.org/10.1016/j.jag.2024.104296. 

- Heiss, N., Meier, J., Gessner, U., Kuenzer, C., 2025. A Review: potential of Earth Observation (EO) for mapping small-scale agriculture and cropping systems in west africa. Land 14, 171. https://doi.org/10.3390/land14010171. 

14 

_N.A.M. Abdelrahim and S. Jin_ 

_International Journal of Applied Earth Observation and Geoinformation 144 (2025) 104917_ 

Ho, S., Tian, L., Disse, M., Tuo, Y., 2021. A new approach to quantify propagation time from meteorological to hydrological drought. J. Hydrol. 603, 127056. https://doi. org/10.1016/j.jhydrol.2021.127056.. 

Mishra, A.K., Singh, V.P., 2010. A review of drought concepts. J. Hydrol. 391, 202–216. https://doi.org/10.1016/j.jhydrol.2010.07.012. 

- org/10.1016/j.jhydrol.2021.127056.. Mostafa, Y., Mohamed, N., Farrag, A.F., 2021. Change detection for map updating using 

- Huang, L., Zhou, P., Cheng, L., Liu, Z., 2021. Dynamic drought recovery patterns over the very high resolution satellite images. JES. Journal of Engineering Sciences 0, Yangtze River Basin. Catena 201, 105194. https://doi.org/10.1016/j. 424–445. 10.21608/jesaun.2021.67949.1039. catena.2021.105194. Ni, R., Zhu, X., Lei, Y., Li, X., Dong, W., Zhang, C., Chen, T., Mburu, D.M., Hu, C., 2022. 

- Huete, A.R., 1988. A soil-adjusted vegetation index (SAVI). Remote Sens. Environ. 25, Effectiveness of Common Preprocessing Methods of time series for monitoring crop 295–309. https://doi.org/10.1016/0034-4257(88)90106-X. distribution in kenya. Agriculture 12, 79. https://doi.org/10.3390/ 

- Iman Bin Hussain, M.D., Katiyar, V., Nagai, M., Ichikawa, D., 2025. Enhancing Satellite agriculture12010079. Image Coregistration Using Mirror Array as Artificial Point Source for Multisource Nigatu, Z.M., You, W., Melesse, A.M., 2024. Drought Dynamics in the Nile River Basin: Image Harmonization. IEEE J. Sel. Top. Appl. Earth Observations Remote Sensing Meteorological, Agricultural, and Groundwater Drought Propagation. 18, 16983–16996. https://doi.org/10.1109/JSTARS.2025.3582238. Ogunrinde, A.T., Adigun, P., Xian, X., Yu, H., Koji, D., Adebiyi, A., Sabo, A.A., 2024. 

- Iyer, R.T., Krishnan, M.T., 2024. Spatial Prediction of Soil Micronutrients using Multi-scale drought variability over West Africa and the associated large-scale Supervised Self-Organizing Maps. Journal of Agriculture and Food Research 15, circulation patterns. Geomat. Nat. Haz. Risk 15, 2409199. https://doi.org/10.1080/ 101033. https://doi.org/10.1016/j.jafr.2024.101033. 19475705.2024.2409199. 

- Jia, Y., Jin, S.G., Savi, P., Yan, Q., Li, W., 2020. Modeling and theoretical analysis of Palagiri, H., Pal, M., 2024. Parametric and non-parametric indices for agricultural GNSS-R soil moisture retrieval based on the random forest and support vector drought assessment using ESACCI soil moisture data over the Southern Plateau and machine learning approach. Remote Sens. 12 (22), 3679. https://doi.org/10.3390/ Hills, India. Int. J. Appl. Earth Obs. Geoinf. 134, 104175. https://doi.org/10.1016/j. rs12223679. jag.2024.104175. 

- Jiao, W., Tian, C., Chang, Q., Novick, K.A., Wang, L., 2019. A new multi-sensor Patil, R., Dubey, M.S., 2017. A Review on Automatic Target Recognition and Detection integrated index for drought monitoring. Agric. For. Meteorol. 268, 74–85. https:// Image Preprocessing Approaches for SAR Images 04. doi.org/10.1016/j.agrformet.2019.01.008. Pozzi, W., Sheffield, J., Stefanski, R., Cripe, D., Pulwarty, R., Vogt;, J.V., Heim, R.R., 

- Jin, S., Chen, Z., Peng, H., 2025. High-frequency Centimeter-accuracy Water Level Brewer, M.J., Svoboda, M., Westerhoff, R., Van Dijk, A.I.J.M., Lloyd-Hughes, B., Estimation in the Yangtze River Using Multi-GNSS Interferometric Reflectometry. Pappenberger, F., Werner, M., Dutra, E., Wetterhall, F., Wagner, W., Schubert, S., IEEE TRANSACTIONS ON GEOSCIENCE AND REMOTE SENSING 63. Mo, K., Nicholson, M., Bettio, L., Nunez, L., Van Beek, R., Bierkens, M., De 

- Jin, S., Camps, A., Jia, Y., Wang, F., Martin-Neira, M., Huang, F., Yan, Q., Zhang, S., Goncalves, L.G.G., De Mattos, J.G.Z., Lawford, R., 2013. Toward Global Drought Li, Z., Edokossi, K., Yang, D., Xiao, Z., Ma, Z., Bai, W., 2024a. Remote sensing and its Early Warning capability: expanding international cooperation for the development applications using GNSS reflected signals: advances and prospects. Satell. Navig. 5, of a framework for monitoring and forecasting. Bull. Am. Meteorol. Soc. 94, 19. https://doi.org/10.1186/s43020-024-00139-4. 776–785. https://doi.org/10.1175/BAMS-D-11-00176.1. 

- Jin, S.G., Meng, X., Dardanelli, G., Zhu, Y., 2024b. Multi-Global Navigation Satellite Rahimi, E., Dong, P., Jung, C., 2025. Global NDVI-LST Correlation: Temporal and Spatial System for Earth Observation: Recent developments and new progress. Remote Sens. patterns from 2000 to 2024. Environments 12, 67. https://doi.org/10.3390/ 16 (24), 4800. https://doi.org/10.3390/rs16244800. environments12020067. 

- Jin, S.G., Zhang, Q., Qian, X., 2017. New progress and application prospects of Global Navigation Satellite System Reflectometry (GNSS+R). ACTA Geod. Cartograph. Sin. 46 (10), 1389–1398. https://doi.org/10.11947/j.AGCS.2017.20170282. 

   - Rhein, S., Jansesberger, V., 2024. Does drought exposure erode trust in the political system in Sub-Saharan Africa? Clim. Change 177, 114. https://doi.org/10.1007/ s10584-024-03768-5. 

- Khorrami, B., Gunduz, O., 2020. Spatio-temporal interactions of surface urban heat island and its spectral indicators: a case study from Istanbul metropolitan area. Turkey. Environ Monit Assess 192, 386. https://doi.org/10.1007/s10661-02008322-1. 

   - Samasse, K., Hanan, N., Tappan, G., Diallo, Y., 2018. Assessing Cropland Area in West Africa for Agricultural Yield Analysis. Remote Sens. (Basel) 10, 1785. https://doi. org/10.3390/rs10111785. 

   - Samasse, K., Hanan, N.P., Anchang, J.Y., Diallo, Y., 2020. A High-Resolution Cropland Map for the West African Sahel based on high-density training data, google earth engine, and locally optimized machine learning. Remote Sens. (Basel) 12, 1436. https://doi.org/10.3390/rs12091436. 

- Khorrami, B., Sahin, O., Gunduz, O., 2024. Comprehensive comparison of different gridded precipitation products over geographic regions of Türkiye. J. Appl. Remote Sens. 18. https://doi.org/10.1117/1.JRS.18.034503. 

- Teoh, K.K., Ibrahim, H., Bejo, S.K., 2008. Investigation on several basic interpolation methods for the use in remote sensing application. In: In: 2008 IEEE Conference on Innovative Technologies in Intelligent Systems and Industrial Applications. Presented at the 2008 IEEE Conference on Innovative Technologies in Intelligent Systems and Industrial Applications (CITISIA), pp. 60–65. https://doi.org/10.1109/ CITISIA.2008.4607336. 

   - Schwartz, C., Ellenburg, W.L., Mishra, V., Mayer, T., Griffin, R., Qamer, F., Matin, M., Tadesse, T., 2022. A statistical evaluation of Earth-observation-based composite drought indices for a localized assessment of agricultural drought in Pakistan. Int. J. Appl. Earth Obs. Geoinf. 106, 102646. https://doi.org/10.1016/j.jag.2021.102646. 

   - Ssembajwe, R., Nguefack, J., Mezafack, K.L., Kagezi, G.H., Gidudu, A., Arinaitwe, G., Voda, M., 2025. Spatiotemporal dynamics and drivers of agricultural droughts in the agroecological zones of Cameroon. Int. J. Appl. Earth Obs. Geoinf. 140, 104581. https://doi.org/10.1016/j.jag.2025.104581. 

- Kogan, F.N., 1995. Application of vegetation index and brightness temperature for drought detection. Adv. Space Res. 15, 91–100. https://doi.org/10.1016/0273-1177 (95)00079-T. 

   - Tong, X., Brandt, M., Hiernaux, P., Herrmann, S., Rasmussen, L.V., Rasmussen, K., Tian, F., Tagesson, T., Zhang, W., Fensholt, R., 2020. The forgotten land use class: Mapping of fallow fields across the Sahel using Sentinel-2. Remote Sens. Environ. 239, 111598. https://doi.org/10.1016/j.rse.2019.111598. 

- Konno, T., Homma, K., 2023. Prediction of Areal soybean lodging using a main stem elongation model and a soil-adjusted vegetation index that accounts for the ratio of vegetation cover. Remote Sens. (Basel) 15, 3446. https://doi.org/10.3390/ rs15133446. 

   - Vicente-Serrano, S.M., Beguería, S., Lopez-Moreno, J.I., 2010. A Multiscalar Drought ´ Index Sensitive to Global Warming: the Standardized Precipitation Evapotranspiration Index. J. Clim. 23, 1696–1718. https://doi.org/10.1175/ 2009JCLI2909.1. 

- Kulkarni, S.S., Wardlow, B.D., Bayissa, Y.A., Tadesse, T., Svoboda, M.D., Gedam, S.S., 2020. Developing a Remote Sensing-based combined drought indicator approach for agricultural drought monitoring over marathwada. India. Remote Sensing 12, 2091. https://doi.org/10.3390/rs12132091. 

   - Wu, W., Li, Y., Luo, X., Zhang, Y., Ji, X., Li, X., 2019. Performance evaluation of the CHIRPS precipitation dataset and its utility in drought monitoring over yunnan province, china. Geomat. Nat. Haz. Risk 10, 2145–2162. https://doi.org/10.1080/ 19475705.2019.1683082. 

- Lambert, M.-J., Waldner, F., Defourny, P., 2016. Cropland mapping over sahelian and sudanian agrosystems: a knowledge-based Approach using PROBA-V Time Series at 100-m. Remote Sens. (Basel) 8, 232. https://doi.org/10.3390/rs8030232. 

- Li, J., 2024. A novel composite drought index combining precipitation, temperature and evapotranspiration used for drought monitoring in the Huang-Huai-Hai Plain. Agric Water Manag. 

   - Yin, G., Zhang, H., 2023. A new integrated index for drought stress monitoring based on decomposed vegetation response factors. J. Hydrol. 618, 129252. https://doi.org/ 10.1016/j.jhydrol.2023.129252. 

- Li, J., Li, Y., Yin, L., Zhao, Q., 2024. A novel composite drought index combining precipitation, temperature and evapotranspiration used for drought monitoring in the Huang-Huai-Hai Plain. Agric Water Manag 291, 108626. https://doi.org/ 10.1016/j.agwat.2023.108626. 

   - Yoo, J., Kim, J., Kwon, H.-H., Kim, T.-W., 2022. A new drought monitoring approach using three-dimensional drought properties based on a dynamic drought detection technique algorithm. J. Hydrol.: Reg. Stud. 44, 101270. https://doi.org/10.1016/j. ejrh.2022.101270. 

- Liu, C., Yang, C., Yang, Q., Wang, J., 2021. Spatiotemporal drought analysis by the standardized precipitation index (SPI) and standardized precipitation evapotranspiration index (SPEI) in Sichuan Province. China. Sci Rep 11, 1280. https://doi.org/10.1038/s41598-020-80527-3. 

   - You, Y., Zhang, Y., Lu, Y., Hao, Y., Tang, Z., Hou, H., 2025. Spatiotemporal Dynamics of Drought in the Huai River Basin (2012–2018): analyzing patterns through hydrological simulation and geospatial methods. Remote Sens. (Basel) 17, 241. https://doi.org/10.3390/rs17020241. 

- Luo, Y., Wang, H., Cao, J., Li, J., Tian, Q., Leng, G., Niyogi, D., 2024. Evaluation of machine learning-dynamical hybrid method incorporating remote sensing data for in-season maize yield prediction under drought. Precis. Agric. 25, 1982–2006. https://doi.org/10.1007/s11119-024-10149-6. 

- Zeng, J., Zhou, T., Qu, Y., Bento, V.A., Qi, J., Xu, Y., Li, Y., Wang, Q., 2023. An improved global vegetation health index dataset in detecting vegetation drought. Sci. Data 10, 338. https://doi.org/10.1038/s41597-023-02255-3. 

15 

