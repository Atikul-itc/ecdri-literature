

# **Rapid #: -27622118** 

CROSS REF ID: **896741** 

LENDER: **CS1 (Calif State Univ., San Marcos) :: Main Library** BORROWER: **IRU (New Mexico State University) :: Main Library** 

TYPE: Article CC:CCG JOURNAL TITLE: Physics and chemistry of the earth USER JOURNAL TITLE: Physics and Chemistry of the Earth, Parts A/B/C ARTICLE TITLE: Drought monitoring using Enhanced Soil Moisture Drought Index (ESMDI) downscaled with deep learning from multi-satellite data for achieving food and water security ARTICLE AUTHOR: , Salau Rahmon Abiodun VOLUME: 141 ISSUE: pt.2 MONTH: 11 YEAR: 2025 PAGES: 104165 ISSN: 1474-7065 OCLC #: Processed by RapidX: 10/5/2026 12:31:09 PM 

This material may be protected by copyright law (Title 17 U.S. Code) 

Physics and Chemistry of the Earth 141 (2025) 104165 



Contents lists available at ScienceDirect 

## Physics and Chemistry of the Earth 

journal homepage: www.elsevier.com/locate/pce 



Drought monitoring using Enhanced Soil Moisture Drought Index (ESMDI) downscaled with deep learning from multi-satellite data for achieving food and water security 



Rahmon Abiodun Salau<sup>a</sup> , Bashir Adelodun<sup>b,c,d</sup> , Qudus Adeyi<sup>a</sup> , Adisa Hammed Akinsoji<sup>a</sup> , Kyung Sook Choi<sup>a,e,*</sup> 

a _Department of Agricultural Civil Engineering, Kyungpook National University, Daegu, 41566, South Korea_ b _Arusha Climate and Environmental Research Centre, Aga Khan University, Arusha, 23201, Tanzania_ c _School of Resource and Environmental Management, Simon Fraser University, Burnaby, Canada_ d _Department of Agricultural and Biosystems Engineering, University of Ilorin, Ilorin, 240003, Nigeria_ e _Institute of Agricultural Science & Technology, Kyungpook, National University, Daegu, 41566, South Korea_ 

|A R T I C L E I N F O|A B S T R A C T|
|---|---|
|_Keywords:_<br>Drought<br>Deep believe network<br>Enhanced Standardized Soil Moisture Index<br>(ESMDI)<br>Climate change<br>Sustainable development goals 2 and 6|Drought conditions are often assessed based on the available soil moisture from land surface models. However,<br>these models operate at low resolution, rendering them suitable primarily for large-scale drought monitoring<br>while constraining their ability to capture variability at the landscape level. The present study developed an<br>Enhanced Standardized Soil Moisture Drought Index (ESMDI). The development of ESMDI was based on the 1 km<br>downscaled soil moisture data from the Global Land Data Assimilation System (GLDAS_CLSM025) from 2004 to<br>2023 over the Gyeongsangbuk-do region. Three models- Deep Believe Network (DBN), Random forest (RF), and<br>Extreme Gradient Boosting (XGB) were models used to downscale GLDAS soil moisture using six Moderate<br>Resolution Imaging Spectroradiometers (MODIS), which include albedo, land surface temperature (LST),<br>Normalized Difference Vegetation Index (NDVI), Enhanced Vegetation Index (EVI), Leaf Area Index (LAI), and<br>evapotranspiration (ET)., precipitation data from Climate Hazards Group InfraRed Precipitation with Station<br>Data (CHIRPS-V2.0), Digital Elevation Model (DEM) and bulk density. The downscaled soil moisture was vali-<br>dated against ground-based measurements. Among the three evaluated models, DBN outperformed in terms of in<br>situ comparisons, achieving an average R-score of 0.93, a Root Mean Square Error (RMSE) of 0.0266 m<sup>3</sup>/m<sup>3</sup>, a<br>Mean Absolute Error (MAE) of 0.0158 m<sup>3</sup>/m<sup>3</sup>, and a Bias of 0.0026 m<sup>3</sup>/m<sup>3</sup>across the ten observation stations<br>selected. ESMDI was developed by normalizing the downscaled soil moisture. The strong correlation of ESMDI<br>with meteorological and hydrological drought indices, particularly in the spring and autumn seasons, and crop<br>yield in July, indicates its effectiveness in drought management.|



### **1. Introduction** 

Drought characterized by insufficient precipitation, low soil moisture, insufficient water flow, and water levels in water bodies has been identified as a natural hazard with the most financial burden, impacting food security, socioeconomics, water supply, and ecosystems (Sa’adi et al., 2023; Su et al., 2021; Yan et al., 2025). It was estimated that about 9 billion US dollars were expended annually to extenuate the effect of drought globally and regionally, which is projected to increase due to the persistent impacts of climate change (Lee et al., 2022; Liu et al., 

2025b; Zhang et al., 2025). Drought can be categorized into five forms, namely: meteorological, agricultural, hydrological, socioeconomic, and stream health drought (Arabameri et al., 2022). The drought often begins with a meteorological drought when the precipitation is below normal conditions and propagates into the hydrological drought, driven by water scarcity in the hydrological system (Li et al., 2025a, 2025b; Wei et al., 2025). Agricultural drought is characterized by low soil moisture, which affects crop yields. Stream health drought is a period of insufficient streamflow that has permanent effects on aquatic ecosystems (Liu et al., 2025b). The economic consequences arising from agricultural, 

* Corresponding author. Department of Agricultural Civil Engineering, Kyungpook National University, Daegu, 41566, South Korea. 

_E-mail addresses:_ olanrewajusalau2790@gmail.com (R.A. Salau), bashir.adelodun@aku.edu adisaakinsoji@knu.ac.kr (A.H. Akinsoji), ks.choi@knu.ac.kr (K.S. Choi). 

(B. Adelodun), adeyi.qudus.tech@gmail.com (Q. Adeyi), 

https://doi.org/10.1016/j.pce.2025.104165 

Received 16 May 2025; Received in revised form 21 October 2025; Accepted 27 October 2025 Available online 30 October 2025 1474-7065/© 2025 Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies. 

_Physics and Chemistry of the Earth 141 (2025) 104165_ 

_R.A. Salau et al._ 

hydrological, stream health, and meteorological droughts, specifically affecting the availability and demand of different economic commodities, are called socioeconomic droughts (Hao and Singh, 2015). 

Soil moisture is one of the most important climatic variables and is crucial for modeling water and energy balance, as it signifies the fraction of precipitation that is retained in the unsaturated zone rather than being lost through processes such as evaporation or runoff (Hussain et al., 2024; Wei et al., 2024; Zhang et al., 2025). This stored moisture is crucial in modulating latent and sensible heat fluxes, influencing albedo and evapotranspiration, as well as facilitating energy transfer between the Earth’s surface and atmosphere (Im et al., 2016; Li et al., 2024; Wang et al., 2025). Furthermore, soil moisture is crucial for drought monitoring due to its relationship with agricultural productivity, precipitation, and evapotranspiration (ET) (Wang et al., 2025). It provides valuable data for assessing drought conditions, particularly agricultural drought, which significantly affects crop growth (Lu et al., 2025; Yi et al., 2022). 

Generally, soil moisture obtained from in situ measurement can realize high accuracy with frequent temporal readings, especially within the surface soil layer, which is essential for promoting optimal crop growth. However, there are limitations. Observation points are often unevenly distributed within monitoring networks, and the number of available ground observation sites may be limited (Zhao et al., 2023; Pang et al., 2024). Soil moisture monitoring stations are typically located on flat terrain, which may not represent conditions on steep slopes or at high altitudes (Zhao et al., 2022). Moreover, point-based soil moisture measurements cannot represent spatial variability, especially over large areas, and field measurements can be costly (Zhu et al., 2017). 

Over the past five decades, remote sensing emerged, which provides continuous spatiotemporal coverage of soil moisture data at shallow depths (1–5 cm). Soil moisture data have been retrieved from a range of satellite sensors (Li et al., 2021; Sun et al., 2024), which include the Advanced Scatterometry (ASCAT) launched in 2006 aboard the MetOp-A satellite by the European Organisation for the Exploitation of Meteorological Satellites (EUMETSAT) (Srivastava et al., 2016), Soil Moisture and Ocean Salinity sensor (SMOS) launched in 2009 by the European Space Agency (ESA) (Mecklenburg et al., 2012), Advanced Microwave Scanning Radiometer 2 (AMSR2) launched in 2012 by the Japan Aerospace Exploration Agency (JAXA) aboard the Global Change Observation Mission 1st-Water (GCOM-W1) (Okuyama and Imaoka, 2015), and Soil Moisture Active Passive (SMAP) launched by the National Aeronautics and Space Administration (NASA) in 2015. The accuracy of soil moisture measurements derived from satellite observations is considerably influenced by the specifications of the sensors, in addition to local environmental factors such as climatic conditions, land cover, and topography (Liu et al., 2025a; Wang et al., 2024). Alongside satellite data, Land Surface Models (LSMs), including the GLDAS-V1 and V2, Variable Infiltration Capacity (VIC), Mosaic, and the Community Land Model (CLM) provide spatiotemporally consistent global information on soil moisture (Rodell et al., 2004). LSMs typically provide more reliable data than satellite-based sources, integrating observed and satellite data within their simulations (Sun et al., 2024; Wang et al., 2024; Ying et al., 2025). These models offer extensive historical records over various temporal resolutions, including 3-hourly, daily, and pentad at the surface and root zone depth (Tavakol et al., 

2021). 

Several drought indices have been developed from remote sensing and LSM data. One of the recent drought indices is the High-resolution Soil Moisture Drought Index (HSMDI) developed by (Park et al., 2017) to assess meteorological, hydrological, and Agricultural drought in the Korean peninsula. Using random forest, the HSMDI was estimated by normalizing AMSR-E soil moisture downscaled with MODIS and the Tropical Precipitation Measuring Mission (TRMM) precipitation. HSMDI showed the most significant relationship with the 1-month Standardized Precipitation Index (SPI). Sun et al. (2022) developed a Standardized Soil Moisture Drought Index (SSMI). SSMI is derived from GLDAS soil 

moisture by calculating the ratio between the deviation of soil moisture from its multiyear average at each grid point and the standard deviation of multiyear soil moisture. This index is derived from pixel-level data, providing a dimensionless measure that monitors agricultural drought in southwest China (Zhou et al., 2024). Standardized soil moisture anomaly (SSMA), which monitors soil moisture anomalies in southern America, was developed by (Spennemann et al., 2015). SSMA was estimated by standardizing Soil moisture from different LSM such as GLDAS-1, GLDAS-2 v2, Mosaic, VIC, and CLM2 and were compared with the SPI and Soil Moisture derived from Microwave observations (SM-MW). SSMA developed from GLDAS-2 v2 shows the highest correlation with SPI in all seasons. 

Satellite-derived soil moisture and LSM drought indices are highly effective means of monitoring agricultural drought (Ning et al., 2024). However, low spatial resolution remains a common limitation. Complex topography and heterogeneous land cover types may be enclosed within a single pixel extent. This limitation may hinder the accurate representation of drought conditions at local or regional levels, potentially reducing the effectiveness of their agriculture and water resource management applications in those areas. While drought indices derived from global soil moisture data offer valuable insights into drought conditions across extensive regions, the use of High-resolution soil moisture data is crucial for accurately identifying local drought conditions and guiding policymakers’ decision-making processes. 

Advancements in machine learning (ML) and deep learning (DL) in recent times have significantly contributed to drought research, downscaling soil moisture, monitoring, and forecasting. Random Forest, Support Vector Machines, and Gradient Boosting are some of the ML models commonly applied for data fusion of dissimilar environmental parameters and drought assessment accuracy enhancement (Senanayake et al., 2024) Concurrently, DL techniques, such as convolutional and recurrent neural networks, are demonstrated to have outstanding ability in mimicking intricate spatio-temporal relations of soil moisture processes and augmenting the monitoring of drought using higher spatial resolutions (Zhao et al., 2022). In addition to improving the spatial resolution of soil moisture products, these techniques also make them more feasible for use in agricultural drought evaluation and water resources management. 

Recently, numerous techniques have been proposed to enhance the resolution of soil moisture derived from LSM and remote sensing (Li et al., 2023; Senanayake et al., 2024; Zhou et al., 2024). A prevalent technique for downscaling is the model-based technique, which can be classified into statistical models and machine learning models (Senanayake et al., 2024). This research examines the effectiveness of deep learning and machine learning techniques for downscaling 25 km resolution GLDAS soil moisture data to a resolution of 1 km, using six MODIS surface products alongside static data and CHIRPS precipitation data. 

This study has two distinct but interconnected objectives. The first objective is to generate a high-resolution (1 km) soil moisture product by downscaling GLDAS data using advanced deep-learning techniques. The second objective is to develop a new drought assessment method through the Enhanced Soil Moisture Drought Index (ESMDI). The downscaling methodology’s effectiveness is independently validated against in-situ measurements. At the same time, ESMDI’s performance is evaluated through comprehensive comparisons with established drought indices, including SPI and Palmer Drought Severity Index (PDSI), as well as hydrological indices and crop yield data for agricultural drought. This dual-validation approach ensures both the quality of the downscaled data product and the reliability of the drought assessment method. 

2 

_Physics and Chemistry of the Earth 141 (2025) 104165_ 

_R.A. Salau et al._ 

### **2. Methodology** 

### _2.1. Study area_ 

The study area is Gyeongsang Buk-do, located in the eastern part of South Korea, with Andong city as the provincial capital, and lies between 36<sup>◦</sup> 15′ N and 128<sup>◦</sup> 45′E with an elevation of 1400 m (Fig. 1). The study area covers an estimated area of 20,071.61 km<sup>2</sup> , bordered to the north by Gangwon-do, Gyeongsangnam-do, and Ulsan to the south, East Sea to the east, and Chungcheongbuk-do and Jeollabuk-do to the west. In addition to Daegu City, the study site has ten cities and thirteen counties bordering the Taebaek and Sobaek Mountains to the east and west, respectively. 

The climatic conditions of Gyeongsangbuk-do are humid and temperate monsoon with four seasons, namely, the summer season, which is characterized by monsoon precipitation and the hottest season between June and August; winter, which starts from December to February, is characterized by cold and severely dry, while Autumn and Spring run from September to October and March to May, respectively. The average annual precipitation within the study area is 1300 mm, with much of the precipitation concentrated in the summer months, primarily due to the East Asian monsoon. The average temperature within the area is around 12<sup>◦</sup> C. Summer temperatures can be elevated, reaching around 30<sup>◦</sup> C, whereas winter temperatures can be significantly lower, frequently falling below 0<sup>◦</sup> C. (Jung et al., 2020). 

Gyeongsangbuk-do is prone to drought conditions during the agricultural season, which spans from April to October, because of the variability in precipitation. This region is particularly susceptible to drought, especially during the summer when water demand by crops is 

at its peak (Park et al., 2017). Over the past few decades, Gyeongsangbuk-do has seen an increase in drought events as a result of changes in the weather patterns of the East Asian monsoons. Water reservoirs and agricultural production have been markedly affected during long drought seasons, particularly in the eastern and northern parts of the region (Karunakalage et al., 2024). 

### _2.2. Data source_ 

### _2.2.1. GLDAS soil moisture data_ 

The GLDAS is jointly maintained by the National Aeronautics and Space Administration (NASA), Goddard Space Flight Centre (GSFC), and the National Centres for Environmental Prediction (NCEP), National Oceanic and Atmospheric Administration (NOAA) (Rodell et al., 2004). GLDAS is developed to generate optimal representations of land surface states and fluxes through the integration of satellite and ground-based observational data products by using land surface modelling and data assimilation methodologies (Huang and Li, 2023; Rodell et al., 2004). The GLDAS models apply three topography schemes: Mosaic, Noah, and the CLM. 

This study uses three-hourly (0.25-degree resolution) GLDAS Noah LSM data due to its relatively higher resolution among LSM soil moisture products, making it more suitable for regional-scale drought monitoring in South Korea. Additionally, GLDAS provides long-term, consistent soil moisture data, which is essential for analyzing historical drought trends and anomalies. Soil moisture data at a depth of 10 cm were specifically used, as this corresponds to the moisture content of the topsoil in satellite-derived soil moisture measurements. Since soil moisture data is provided every 3 h at this depth, eight-day soil moisture data were 



**Fig. 1.** The study area showing key monitoring sites and land cover classification derived from Sentinel-2. 

3 

_Physics and Chemistry of the Earth 141 (2025) 104165_ 

_R.A. Salau et al._ 

calculated by aggregating the three-hourly data. This study focuses exclusively on Korea’s growing season, from April to October, over the period of 2004–2023. 

### _2.2.2. MODIS data_ 

MODIS on Terra and Aqua covers a wide range of environmental and biophysical properties for various applications. In this study, six MODIS data were used, which include Leave Area Index (LAI-MYD15A2H) with spatial and temporal resolution of 500 m/8days, Albedo (MCD43A3) 500 m/16days, Land Surface Temperature (LST-MYD11A2) 1 km/8 days, Evapotranspiration (ET-MOD16A2) 500 m/8dyas, Normalized Difference Vegetation Index and Enhanced vegetation index (NDVI & EVI-MYD13A2) 1 km/16days. 

The MODIS products were selected because they capture the key factors influencing soil moisture variability, such as surface energy balance, evapotranspiration, which directly affect soil moisture dynamics, vegetation greenness and density, which affect soil water uptake and transpiration. These capture the complex land–atmosphere exchanges that are in charge of regulating soil moisture distribution and have been widely proven to improve prediction and downscaling accuracy (Rostami et al., 2023). To ensure consistency across datasets, all products were resampled spatially and temporally to 1 km/8 days resolution. Covering the period from 2004 to 2023 (April to October), these datasets were obtained from the NASA archive via Google Earth Engine. The nearest neighbor was chosen as a resampling technique in order to preserve original pixel values without introducing interpolation artefacts. Although certain products (e.g., NDVI, EVI, LAI) are inherently available at 500 m, upscaling them to 1 km using nearest neighbor guarantees consistency with larger predictors while preserving the original measurements. This approach has been generally applied in downscaling studies in which resolution consistency is of utmost importance (Piles et al., 2011). 

### _2.2.3. CHIRPS precipitation_ 

CHIRPS gridded precipitation products at the spatial resolution of 0.25<sup>◦</sup> , with a comprehensive time series that extends from 1981 to the current date. It is available daily, monthly, pentad, and annually (Funk et al., 2015). CHIRPS is developed using ground-based observations, satellite data, and global precipitation data. Key data sources for CHIRPS include TMPA 3B42, pentad precipitation data, the National Climatic Data Centre (NCDC), NOAA’s Climate Prediction System atmospheric model precipitation fields, thermal infrared data from the Climate Prediction Center (CPC), and Satellite Precipitation Gauge (SPG) observations. The final CHIRPS data are derived using the Inverse Distance Weighting (IDW) technique and infrared cold cloud duration (CCD) observations (Zhou et al., 2025). The present research used CHIRPS daily precipitation data version 2.0, characterized by a resolution of 0.25<sup>◦</sup> and spanning the period from 2004 to 2023 (specifically from April to October). This dataset was sourced from the (https://data.chc. ucsb.edu/products/CHIRPS-2.0/). The data were subsequently aggregated into 8-day intervals to facilitate integration with other datasets. 

### _2.2.4. DEM_ 

The digital elevation model (DEM) provided by the Space Shuttle Radar Topography Mission (SRTM) launched in 2002 was used in this study to obtain elevation data on Gyeongsangbuk-do (Wu and Li, 2024). SRTM covers approximately 119 million square kilometers between N60<sup>◦</sup> , including South Korea. In this study, the selected DEM data covers Gyeongsangbuk-do at a resolution of 30 m. The data acquired from the USGS was resampled to a resolution of 1 km to align with other datasets. 

### _2.2.5. Bulk density_ 

Bulk density is one of the major physical properties of soil that directly controls soil moisture dynamics. It refers to the mass of the soil per unit volume and incorporates both solids and pore spaces, usually denoted in g/cm<sup>3</sup> . Bulk density is one factor that determines the water 

retention ability, rate of infiltration, or the amount of moisture available to the plant. Soils of low bulk density have a high percentage of pore space; thus, they can retain more water. On the other hand, high bulk density shows compaction and thus fewer pore spaces for the entry and storage of water. Bulk density, therefore, becomes pivotal in regulating the availability of soil moisture, particularly with respect to plant water uptake and all other soil-water interactions. The bulk density used in this study was downloaded from (www.soilgrids.org) at a resolution of 250 m, but was resampled to 1 km resolution. 

### _2.2.6. In situ data_ 

In situ observations are essential for evaluating the modelled product; soil moisture data from ten observation points in Gyeongsangbuk-do obtained from the Korea Rural Development Agency (RDA) through their open API portal (http://weather.rda.go.kr/) for the period of April to October 2014 to 2017 were used in this study to evaluate the downscaled soil moisture. RDA uses time record reflectometry (TDR) to provide hourly, daily, and monthly soil moisture data at 10 cm, 30 cm, and 40 cm depth based on the relationship between soil dielectric strength and moisture level (Albergel et al., 2012). Most of the observation sites are situated in agricultural areas, predominantly characterized by sandy loam, clay, and clay loam soil types. 

The validation of developed indices is an important step in demonstrating their applicability. It is always challenging to validate this drought index, as ground truth observations of drought severities and magnitudes are unavailable. Comparing the developed index with the main drought events reported or well-accepted drought indices in terms of spatial and temporal comparison using data from governmental reports, historical records, satellite observations, and previously established drought indices is suggested for validating the new drought index. References to previous studies by Hao and Singh (2015) and Prajapati et al. (2022) suggest that this validation approach has been recognized and used in the scientific literature to assess the reliability of drought indices. 

The SPI proposed by McKee et al., in 1993 was one of the indices used for the evaluation of ESMDI. It is recommended by the World Meteorological Organization (WMO) to indicate the amount of precipitation over a specific period (Ojha et al., 2021). It is a drought monitoring tool that quantifies precipitation deficits over varying timescales, typically from one to several months. SPI ranges in value from − 2 to 2. Positive values of SPI indicate wetter-than-normal periods, while negative values reflect drier-than-normal periods. 

The PDSI developed by Palmer (1965), incorporates antecedent precipitation and moisture supply into a hydrologic accounting framework. Thus, the PDSI has become one of the most widely used comparable indices of localized drought conditions in space and time and a valuable tool for drought definition and water resource management (Dehghan et al., 2020). The Monthly index values range from − 4.00 to 4.00, with values below − 2.5 referring to dry periods and values above − 2.5 indicating wet periods. This study uses a 3-month scale SPI and PDSI for April to October (2004–2017) as meteorological drought indices to validate ESMDI; the Disaster Prevention Research Institute provided the data. Yearly crop yield data was employed to validate the ESMDI regarding Agricultural drought. Sesame yield (2006–2015) provided by the Korean Statistics (KOSTAT; http://kostat. go.kr/) was used. Sesame was considered in this study due to its responsiveness to variability in soil moisture and the availability of high-quality yield data, thus it serves as a representative crop for validation of the downscaled product. 

The data on agricultural reservoir storage and inflow from April to September 2004 to 2017, provided by the Korean Rural Community Corporation (KRC), were used as hydrological drought to evaluate ESMDI. This study targeted agricultural reservoirs located near agricultural areas, particularly at five monitoring stations: Nohong-Daegu, Geumhwa-Gumi, Deogga-Mungyeong, Simgog-Pohang, and Dongmyeon-Yeongju, shown in Fig. 1. For comparison of the EMDI, the 

4 

_R.A. Salau et al.                                                                                                                                                                                                                                Physics and Chemistry of the Earth_ 

_Physics and Chemistry of the Earth 141 (2025) 104165_ 

reservoir water levels and inflow data from 2004 to 2017 (April to September) were standardized by fitting into the Gamma distribution function. On this scale, a scaled value less than zero indicates drought conditions, while a scaled value greater than zero indicates humidity. The summary of the dataset used in this study is presented in Table 1. 

### _2.3. Proposed methodology_ 

The downscaling technique proposed by (Zhao et al., 2022) was adopted in this study, which assumes that the correlation between soil moisture and auxiliary data is scale-independent; in other words, the correlation under low-resolution conditions can be used to derive high resolution by using high-resolution cofactors. Fig. 2 presents a flowchart detailing the downscaling process. The process consists of five parts: Firstly, the auxiliary data were spatially and temporally resampled to 25 km/8-day to match the GLDAS soil moisture data. The nearest neighbor interpolation method was used for resampling. Secondly, low-resolution data were used to train downscaling models, such as deep belief networks, random forests, and extreme gradient boosting models. Before training, null values in both GLDAS-SM and corresponding auxiliary data were removed, and all data were standardized. In the prediction phase, high-resolution auxiliary data, including MODIS, DEM, and bulk density, with a resolution of 1 km, were used as inputs into the trained models to derive soil moisture estimates at the same 1 km resolution. The next phase involved residual correction, where a 25 km raster was used to calibrate the downscaled results to preserve the original raster’s information. In the fourth stage, the latitude and longitude coordinates of the observed soil moisture data were used to extract corresponding values from the downscaled soil moisture for evaluation. The performance of the downscaled soil moisture was evaluated using RMSE, MAE, Bias and R<sup>2</sup> by comparing model predictions at each fine-resolution grid cell with the corresponding observed values from ground stations following Chen et al. (2013), with the Deep Belief Network demonstrating superior performance compared to the other models. The final step includes estimating ESMDI by normalizing the downscaled soil moisture, and the ESMDI was assessed using drought indices. 

To evaluate the results of soil moisture downscaling models, in situ soil moisture data at ten monitoring sites in Gyeongsangbuk-do were downloaded from the RDA through their open API portal (http://weath er.rda.go.kr/) for the period April to October 2014 to 2017. The downloaded daily data were aggregated over 8 days to match the temporal resolution of downscaled soil moisture. These measurements, collected at a depth of 10 cm from each monitoring station, were used for the validation. Since the observed soil moisture is point data that is measured at a particular point, it is difficult to compare downscaled GLDAS with in situ measurements simply because of spatial repressiveness (Im et al., 2016). To address this problem, the latitude and longitude of _the_ in situ measurement points were transformed into 

pixel-based row and column indices using the downscaled GLDAS spatial reference system, ensuring accurate targeting within the raster grid. To enhance data accuracy and mitigate spatial discrepancies, soil moisture values were extracted from a 3 × 3 pixel window around the identified location rather than a single pixel. Given that each pixel represents 1 km<sup>2</sup> , this method averages the values from the surrounding 3 km by 3 km area. This approach provides a more reliable and stable estimate of soil moisture by accounting for local variations, making the comparison between downscaled GLDAS data and in situ measurements more meaningful. 

To assess the impact of residual correction both soil moisture at 25 km resolution and the downscaled soil moisture product (SMs) were validated against ground-truth measurements from in situ stations. The performance of the downscaled soil moisture was evaluated using RMSE, MAE, Bias, and R<sup>2</sup> by comparing model predictions at each fineresolution grid cell with the corresponding observed values from ground stations, following Chen et al. (2013), with the Deep Belief Network demonstrating superior performance compared to the other models. The final step involves estimating ESMDI by normalizing the downscaled soil moisture, and the ESMDI is then assessed using drought indices. 

### _2.4. Deep learning and machine learning based approaches for soil moisture downscaling_ 

The Deep Belief Network (DBN) is a foundational deep learning architecture developed by Hinton et al. (2006). This model addresses the training challenges associated with Deep Neural Networks (DNNs) and facilitates the swift advancement of deep learning approaches. The DBN possesses a strong non-linear adaptability with its multilayer characteristic. This study applied the DBN model to downscale GLDAS-SM products in a systematic four-step process. Firstly, the input data (auxiliary data), which consists of various surface environmental variables that greatly influence soil moisture, were extracted with a resolution of 25 km for every time step considered in this study (April to October 2004–2023). These input variables were independent variables, while GLDAS soil moisture data acted as label data (dependent variable). Secondly, the input and label data were combined into a column-wise 2D matrix to create matched data pairs. Rows with missing values were identified and removed to ensure the quality of the dataset. The remaining input data were then standardized using a standard scaler to ensure consistent scaling, improving the efficiency of model training. 

Thirdly, the DBN model was trained in clean and standardized data. Its architecture comprises a visible layer, multiple hidden layers trained using Restricted Boltzmann Machines (RBMs), and an output layer, as shown in Fig. 3, enabling it to learn abstract and hierarchical representations of the input data. The training process involved backpropagation, with a mean squared error (MSE) loss function and an Adam optimizer to fine-tune the model’s weights. By learning the 

**Table 1** 

The summary of the dataset used in this study. 

|Datasets|Source|Temporal<br>Coverage|Spatial Resolution|Usage in the Study|
|---|---|---|---|---|
|CHIRPS Precipitation|CHIRPS V2.0|2004–2023|0.25<sup>◦</sup>(~25 km)|Precipitation input for the soil moisture<br>downscaling model|
|Bulk Density|SoilGrids|Static|250 m|Static variable for downscaling model|
|In-situ Soil Moisture|RDA Weather Service|2014–2017|Point locations|Validation of downscaled soil moisture|
|Annual Crop Data<br>l|Statistics Korea|2004–2023|1 km/administrative<br>unit|Crop data for validation of ESMDI|
|Reservoir Water Level and Inflow|Korea Rural Community Corporation (KRC)<br>(available upon request)|2004–2017|Point locations|Hydrological input for drought Validation|
|MODIS Products (LST, NDVI, EVI,<br>LAI, ET, Albedo)|Google Earth Engine–MODIS|2004–2023|500m-1 km|Auxiliary variables for downscaling|
|Digital Elevation Model (DEM)|USGS Earth Explorer|Static|30 m|Topographic variable for downscaling|
|SPI and PDSI|Korea Disaster Prevention Research Institute<br>(available upon request)|2004–2017|Point locations|Comparison and validation of drought<br>indices|
|GLDAS Noah LSM Soil Moisture|NASA DISC–GLDAS|2004–2023|0.25<sup>◦</sup>(~25 km)|Source soil moisture data for downscaling|



5 

_R.A. Salau et al._ 

_Physics and Chemistry of the Earth 141 (2025) 104165_ 



**Fig. 2.** Flowchart of the proposed framework. 

complex relationships between auxiliary data and soil moisture, the DBN effectively captured the underlying patterns in the input data. After training, high-resolution auxiliary data were incorporated to generate high-resolution soil moisture products. 

The architecture and performance of the DBN were optimized by carefully choosing the hyperparameters. Key parameters like hidden layer number and size, number of neurons at each layer, learning rate, dropout rate, and activation functions were estimated using preliminary experiments. The final configuration includes three hidden layers with 512, 256, and 128 neurons, respectively, a 0.3 dropout rate, ReLU activation, and an Adam optimizer with mean squared error loss, which was chosen for its ability to balance model complexity and training stability with prediction accuracy. 

In addition to deep learning, this study also explored ensemble-based machine learning models such as RF and XGB. They are ensemble learning approaches that are widely used for downscaling tasks due to their ability to handle complex datasets and accurately predict outcomes. RF is based on Classification and Regression Trees (CART; Breiman, 2001), a decision tree-based algorithm. It uses an ensemble approach by combining predictions from multiple decision trees, typically numbering between 500 and 1000. The term "random forest" stems from the randomness introduced during training, where a subset of training samples is randomly selected to grow each tree, and a random 

subset of variables is chosen for splitting at each tree node. These mechanisms mitigate common issues such as overfitting and sensitivity to training data. RF aggregates predictions from individual trees using averaging for regression tasks or majority voting for classification tasks. It also calculates variable importance by assessing the increased percentage of mean square error (MSE) using out-of-bag (OOB) data when a variable is permuted with random values. RF has been extensively applied in remote sensing for classification, regression, and downscaling tasks, demonstrating its reliability and accuracy in transforming coarseresolution soil moisture data into finer resolutions (Kim et al., 2015). 

XGB, on the other hand, is an advanced ensemble learning algorithm based on the gradient boosting tree method. It constructs multiple decision trees, where each tree is built sequentially, depending on the residuals or errors of the previous trees. This iterative process enhances the model’s predictive performance by refining its focus on poorly predicted samples. The predicted value for each sample is determined by summing the leaf values across all trees. Like RF, XGB effectively manages multicollinearity and complex nonlinearity interactions, making it suitable for high-resolution downscaling tasks. Its ability to prioritize meaningful splits during tree construction renders multicollinearity irrelevant. XGB is particularly efficient in terms of computation and accuracy, making it an ideal choice for downscaling applications. 

To implement these models, the key hyperparameters were set based 

6 

_R.A. Salau et al._ 

_Physics and Chemistry of the Earth 141 (2025) 104165_ 



**Fig. 3.** Deep belief network structure. 

on standard practices and prior literature. For RF, the key hyperparameters such as the number of trees, maximum depth, and number of features considered for splitting were set based on standard practices and prior literature (Park et al., 2017), with the number of trees typically ranging from 500 to 1000. The stability of the predictor was evaluated using out-of-bag (OOB) error estimation. For XGB, hyperparameters like the number of boosting rounds, learning rate, and maximum depth of tree, and subsample ratios were set based on the practice by Ali et al. (2023), with a priority to strike a balance between predictive performance and computational cost. Though an exhaustive search for hyperparameters was not performed, these sets of configurations proved satisfactory to achieve accurate and stable downscaling results over the entire study region. 

DBN, RF, and XGB were chosen because they effectively learn the nonlinear, high-dimensional, and noisy characteristics of environmental data. DBN has the ability to learn hierarchical and abstract feature representations via unsupervised pre-training, which regularizes learning when data are noisy or scarce, which is a frequent issue in soil moisture research (Cai et al., 2022). Random Forests (RF), as an ensemble of decision trees, are immune to overfitting, handle multicollinearity with ease, and provide interpretable variable importance scores and thus are favored in soil and hydrological modeling (Abowarda et al., 2021). Extreme Gradient Boosting (XGB), a refined boosting algorithm, efficiently learns complex non-linear patterns and typically outperforms traditional ensemble methods with stellar performance in environmental prediction tasks (Kumar et al., 2024). These models were applied separately to assess their individual performance in soil moisture downscaling, as each provides complementary strengths in feature learning, robustness, and predictive accuracy, making them suitable candidates for soil moisture downscaling. Among these models, DBN proved superior in preliminary evaluations due to its ability to 

handle high-dimensional data and learn nonlinear relationships. Besides, the DBN architecture enables the model to leverage the hierarchical structure of input data, which coincides with the multilevel factors of soil moisture. These features, therefore, influenced the selection of DBN as the main model in this study. The comparative evaluation between RF, XGB, and DBN showed that DBN outperformed these models by a large margin across several performance metrics. This study underlines the potential of DBN in addressing the challenges of downscaling soil moisture data while offering a robust and scalable approach. 

### _2.5. Residual correction_ 

In the downscaling procedure of GLDAS-SM, low-resolution rasters were employed to calibrate the downscaled results, thereby enhancing their alignment with the distribution of the original rasters. The technique known as residual smoothing has exhibited significant effectiveness in prior downscaling research, as evidenced by the studies conducted by (Q. Wanget al.,2015; Zhao et al., 2022). The process is delineated in several specific steps. Firstly, low-resolution cofactors are introduced into the downscaling learning model to derive the estimated low-resolution soil moisture product, denoted as SMk. Subsequently, the coarse-scale residual is determined by subtracting SMk from the associated SMr value obtained from the original GLDAS-SM dataset. This is followed by the derivation of the fine-scale residual, Rs, through nearest-neighbor interpolation techniques. This relationship is mathematically represented as Rs (1 km) = FNearNeigbor (SMr − SMk), where = FNearNeigbor denotes the nearest neighbor interpolation function. Finally, the residual Rs (1 km) was integrated with the downscaled 1 km soil moisture (SMs), resulting in the final high-resolution soil moisture product, SMsa. The equation SMsa = SMs + Rs can succinctly express this stage. 

7 

_Physics and Chemistry of the Earth 141 (2025) 104165_ 

_R.A. Salau et al._ 

### _2.6. Estimation and evaluation of ESDMI_ 

ESMDI was developed based on the methodology proposed by (Park et al., 2017). ESMDI was developed using 1 km bias-corrected downscaled soil moisture data, which were generated from auxiliary data modelled with a DBN, which is the best-performing model among the models considered in this study. ESMDI is estimated by normalizing the maximum and minimum soil moisture values for each pixel(kth) on the same day of the year (DOY) every 8 days during 2004–2023 using equation (1). The ESMDI highlights regions that are drier (indicated by 0), or wetter (indicated by 1) compared to their typical conditions. Values within 0.6 are classified as normal conditions, and values below 0.5 are classified as drought, as 0.5 represents the median status over 20 years. 



ESMDI was validated using observational reference data from meteorological, agricultural, and hydrological sources. Time-series patterns between ESMDI and the SPI and PDSI were analyzed to assess meteorological drought. Regression analysis was conducted to examine the correlation between the ESMDI and annual crop yield as indicators of agricultural drought. The monthly ESMDI was also validated with the Reservoir water level and inflow of selected agricultural reservoirs. 

### **3. Results and discussions** 

### _3.1. Evaluation of downscaled soil moisture with observed soil moisture_ 

Fig. 4 compares the annual mean of 25 km coarse-resolution soil moisture and DBN, XGB, and RF downscaled products for wet years (2008, 2012) and a dry year (2017). The difference between coarse-scale and fine-scale representations is striking. The 25 km dataset represents soil moisture in large, homogeneous blocks (pixels), which conceal spatial heterogeneity. In contrast, the downscaled products exhibit more subtle differences on a finer scale, with patches of wetness or dryness within the same coarse pixel. Such fine resolution is crucial in understanding land-surface processes and enhancing water resources management. Most regions are marked as moderately or highly saturated for 

the peak months of precipitation on the coarse-resolution maps. However, the DBN, XGB, and RF models reveal subtle distinctions in moisture. For example, the DBN emphasizes regions characterized by high values of moisture ( _>_ 30). The XGB and RF models show comparable improvements; however, their spatial coverages are somewhat different, indicating differences in responsiveness within the models to auxiliary inputs, including vegetation indices, topography, and meteorological conditions (Anees et al., 2024). 

The impact of residual correction was assessed by validating both the soil moisture at 25 km resolution and the downscaled soil moisture product (SMs) against ground-truth measurements from in situ stations, as shown in Fig. 5(a–d). The results demonstrate that incorporating residual correction reduces systematic errors, decreases RMSE and bias, and increases the correlation with observed soil moisture. This indicates that residual correction effectively improves the accuracy and reliability of the downscaled high-resolution soil moisture. The dry year also illustrates the benefits of downscaling. The 25 km data set has extensive areas of low soil moisture content, with minimal differentiation in each pixel. The DBN, XGB, and RF models, however, can pick out sub-regions with extreme soil moisture deficits, thus highlighting areas that are especially at risk from drought-related problems. This level of resolution is essential to precision agriculture and drought management, allowing for targeted actions such as localized irrigation planning and early warning systems. This contrast underscores the value of downscaling soil moisture data for hydrological modeling and climate adaptation planning. While coarse-resolution data provides a general overview, DBN, XGB, and RF provide essential fine-scale detail that informs agricultural decision-making, water resource management, and environmental planning. 

Fig. 6(a–d) shows the validation outcomes of bias-corrected downscaled soil moisture models (DBN, RF, and XGB) with the observed measurements at 10 stations from 2014 to 2017 (April to October), which is a period of severe drought in most of the year, especially in 2014 and 2015 (Ryu et al., 2019). All models show strong correlations with observed soil moisture data in all stations. Among the three evaluated models, DBN has a better performance with an average R-score of 0.93, a Root Mean Square Error (RMSE) of 0.02656 m<sup>3</sup> /m<sup>3</sup> , a Mean Absolute Error (MAE) of 0.01575 m<sup>3</sup> /m<sup>3,</sup> and a Mean Bias Deviation (MBD) of 0.00264 m<sup>3</sup> /m<sup>3</sup> . A significant correlation exists within the 



**Fig. 4.** Coarse Soil moisture vs. bias corrected downscaled soil moisture. 

8 

_Physics and Chemistry of the Earth 141 (2025) 104165_ 

_R.A. Salau et al.                                                                                                                                                                                                                                Physics and Chemistry of the Earth_ 



**Fig. 5.** (a–d). Validation of 25 km GLDAS soil moisture and downscaled soil moisture against in situ measurements across stations from 2014 to 2017 **.** 

data, especially at the observation stations in Seongju, Yecheon, and Mungyeong. This correlation is attributable to the uniformity of soil types at these locations, which predominantly consist of loamy and clayey soils. Considering the superior performance of DBN in terms of average metrics, it is therefore selected for the ESMDI development. 

In the feature importance analysis, ET emerged as the most influential variable, significantly contributing to soil moisture estimation in all the downscaling models used in this study. This is consistent with previous studies highlighting evapotranspiration as a key driver of soil moisture variability (Du et al., 2021; Wang et al., 2025). Additionally, DEM, LAI, CHIRPS precipitation, NDVI, EVI, Bulk Density, and LST also played notable roles, as topographic, surface temperature, and vegetation-related factors strongly influence surface hydrological processes. 

Albedo had minimal influence, suggesting that albedo may not be the primary driver in these model setups (Kumar et al., 2025). The same feature importance trends were observed across all the models. For clarity, the feature importance of the DBN model, which was the best-performing model, is presented in Fig. 7. 

### _3.2. Meteorological drought_ 

The drought index, ESMDI, was evaluated using the monthly SPI and PDSI from 2004 to 2017 (April to October) obtained from the Korea Disaster Prevention Research Institute. Soil moisture data at a depth of 10 cm were specifically used for validation, as this corresponds to the moisture content of the topsoil in satellite-derived soil moisture measurements. While the top layer is sensitive to short-term precipitation, 

indices such as SPI-0 or SPI-1 could react too strongly to a single rainfall event and not capture persistent anomalies. anomalies (Smith et al., 2022; Frazier et al., 2022). Future studies should address this gap by considering short time scales, such as SPI-1. We therefore selected SPI-3, which accumulates precipitation over three months and provides a more stable measure of short-to medium-term moisture conditions. This timescale was seen to describe agricultural and hydrological drought processes better and hence provide a more credible basis on which to verify the downscaled soil moisture. The correlation coefficient values between ESMDI and 3-month SPI, as well as ESMDI and PDSI at 10 stations, are shown in Fig. 8. In South Korea, temperatures begin to rise in March, peak in August, and gradually decline from late August through February of the following year. Most farming activities typically take place from April to October. 

The seasonal relationships between the ESMDI, SPI, and PDSI, explain the periodic variation in soil moisture and drought conditions for the various months of the year. These correlations underscore the interrelationship that exists between precipitation and the general hydrological factors, providing insights into how well drought indices capture soil moisture variability throughout the year. 

The strongest correlations among these indices occur in August, September, and October when the SPI and PDSI are in close agreement with the ESMDI. This phenomenon is attributable to the significant residual soil moisture resulting from preceding precipitation events influenced by monsoons. These months are characterized as climatic periods with persistent precipitation and low evapotranspiration, allowing both the SPI, which emphasizes precipitation, and the PDSI, which incorporates soil moisture, temperature, and evaporation, to 

9 

_R.A. Salau et al.                                                                                                                                                                                                                                Physics and Chemistry of the Earth_ 

_Physics and Chemistry of the Earth 141 (2025) 104165_ 



**Fig. 6.** (a–d). Validation of bias-corrected downscaled soil moisture against in situ measurements across stations from 2014 to 2017. 



**Fig. 7.** Feature important identification. 

capture analogous drought dynamics effectively (Zhang and Jia, 2013; Sohrabi et al., 2015). Even as precipitation declines in October, the accumulated soil moisture sustains high correlations between PDSI and ESMDI. 

Conversely, other months, such as April, June, and July, display moderate correlations with increased variability. In April, the SPI demonstrated a closer correlation with the ESMDI, as it is more 

responsive to drought, whereas the PDSI’s broader hydrological considerations resulted in a weaker association. The negative correlation coefficients observed during May–July can be attributed to several factors. During these summer months, intense precipitation events from the East Asian monsoon can lead to rapid changes in soil moisture that may not be immediately reflected in the SPI and PDSI indices. Additionally, high temperatures and increased evapotranspiration during this period 

10 

_R.A. Salau et al._ 

_Physics and Chemistry of the Earth 141 (2025) 104165_ 



**Fig. 8.** Boxplots of Correlation plot between ESMDI, SPI, and PDSI from April to October. 

can result in rapid soil moisture depletion, creating a temporal disconnect between precipitation-based indices and actual soil moisture conditions. This phenomenon is particularly pronounced in May, representing a transition period between spring and summer seasons, where soil moisture dynamics are influenced by residual spring conditions and emerging summer patterns (Kwon et al., 2019). The negative correlations suggest that ESMDI may be more sensitive to immediate changes in soil moisture conditions compared to the more slowly responding SPI and PDSI during these months. 

The time series analysis of the SPI, ESMDI, and PDSI across five stations—Gyeongju, Seongju, Cheongdo, Andong, and Pohang from 2004 to 2017 (April to October), as shown in Fig. 9, describes the dynamics of drought and wetness. The SPI indicates meteorological drought, with values falling below 0, denoting drought conditions. ESMDI reflects agricultural drought, and values below 0.5 reflect soil moisture stress. The PDSI, which reflects long-term meteorological conditions, is considered to depict drought when its value is below − 2.5. Notably, all stations experienced significant drought periods between 2004 and 2017, especially in 2010, 2014–2015, and 2017, characterized by recurrent soil moisture deficits and extended meteorological stress. There were periods of intermittent wetting, especially in 2007,2008, 2012, and 2013, when positive trends in the indices indicated a recovery phase. Gyeongju and Andong experienced more intense drought conditions, especially in 2017. Cheongdo and Seongju showed more severe droughts with relatively quicker recovery periods, especially during transitional monsoon seasons. This phenomenon can be attributed to variations in local climate and topography, which may have enhanced the capacity for precipitation capture and soil moisture retention (M. Wanget al.,2021). Pohang and Andong exhibited significant drought stress in ESMDI during the early years (2005–2006), although it improved more rapidly afterward, suggesting improved surface moisture recovery relative to long-term meteorological conditions. 

The number of drought events per year for ESMDI, PDSI, and SPI, equivalent to the duration of each event per year, is summarized in Fig. 10. The meteorological drought index (SPI) indicates a higher frequency of drought events compared to ESMDI and PDSI, particularly during the 2014–2017 period across all stations. This observation aligns with the findings of (Lee et al., 2022; Van Loon et al., 2012),who demonstrated that the average number of meteorological drought events was approximately three times those of the other types of droughts. 

ESMDI and PDSI show moderate agreement in drought detection, 

although ESMDI typically identifies more events. Notably, this discrepancy is most pronounced at Andong and Seongju stations, where ESMDI captured significant drought events during 2010–2012 that were not as strongly reflected in PDSI measurements. Spatial variations are also evident across stations. For example, Andong and Pohang exhibit more frequent drought events across all indices than other stations, particularly during 2008–2010 and 2014–2016. This spatial heterogeneity suggests that local factors, such as variations in soil moisture retention capacity, groundwater recharge rates, and land cover characteristics, may influence drought manifestation despite the stations’ regional proximity (He et al., 2025; Nazir et al., 2024). For instance, Andong’s higher elevation and forested landscape may lead to greater evapotranspiration losses, whereas Pohang’s coastal influence and agricultural dominance could affect soil moisture availability. Additionally, differences in precipitation patterns and subsurface water storage may contribute to these variations. These findings align with water cycle theories, emphasizing the role of surface and subsurface hydrological processes in shaping drought severity and frequency (Yang et al., 2021). Temporal analysis reveals an increased frequency of drought events in recent years (2014–2017) across all stations, with SPI detecting this trend most prominently. 

### _3.3. Hydrological drought_ 

Insufficient precipitation, soil characteristics, and other hydrological parameters, such as evaporation, lead to low runoff in watersheds and water levels in dams and reservoirs that evolve into hydrological droughts. ESMDI was validated using the standardized agricultural reservoir inflow and water level provided by KRCC. The monthly inflow and water level were fitted into gamma distribution to achieve the Standardized watershed inflow index (SWII) and Standardized Reservoir Storage index (SRSI), respectively. The correlation between ESMDI and SRSI, as well as ESMDI and SWII, were evaluated from April to September 2004 to 2017, as shown in Fig. 11. 

The correlation boxplot shows the complex interaction between Soil moisture and hydrological processes. In April, SRSI and SWII showed a low correlation with ESMDI; this is influenced by the contribution of snowmelt from the winter season to the soil moisture and the slow reactivation of hydrological systems. In May, SRSI showed a moderate correlation with ESMDI, which indicates that the response of the reservoirs became more direct to increasing precipitation and soil moisture, 

11 

_R.A. Salau et al._ 

_Physics and Chemistry of the Earth 141 (2025) 104165_ 



**Fig. 9.** Time series plot of SPI, PDSI, and ESMDI. 

signalling the start of the agricultural season. 

In summer, correlation patterns are more dynamic and reveal a shift from negative to positive correlations. June presents the most significant drop for both SWII and SRSI. This could be attributed to the lag between hydrological inputs and soil moisture, where inflows and reservoir storage are still adjusting to earlier seasonal conditions (Gong et al., 2025). As summer progresses toward July and August, ESMDI correlations with SWII and SRSI begin to increase, as reflected in a better concordance between soil moisture conditions and the hydrological systems. This is the effect of peak precipitation or monsoon seasons whereby soil moisture and inflow of water into reservoirs start to be in tune with the current meteorological conditions. Notably, SRSI fluctuates less than SWII, suggesting that reservoir management practices help buffer against short-term weather variations, stabilizing water storage compared to the more immediate response seen in watershed inflows. 

In September, the correlations peaked, and the ESMDI had strong positive values with SWII and SRSI. This indicates that the hydrologic systems have already reached their full response to cumulative summer precipitation. The higher variability in SWII compared to SRSI could stem from watershed inflows responding more directly to recent weather events, while reservoir storage is buffered by water management, allowing for more stable, gradual adjustments. Fig. 12 illustrates the time series plot of the ESMDI, SWII, and SRSI from April to 

September between 2004 and 2017 across five reservoirs: Nohong, Dongmeyeon, Deogga, Geumhwa, and Simgog, all situated in the agricultural area and serve as irrigation purpose. The plots reveal distinct hydrological patterns. At Dongmeyeon and Deogga, drought conditions indicated by the SWII and the SRSI were relatively common. However, the ESMDI indicates fewer occurrences of drought conditions, suggesting that fluctuations in inflow and reservoir storage have a diminished impact on soil moisture. The same trend was observed at Geumhwa Station, where both inflow and water storage indicate drought conditions; however, soil moisture remains relatively unaffected. At Simgog, the SWII exhibits significant fluctuations, while the SRSI and EMDI indices demonstrate stable conditions. At Nohong, inflow and storage exhibit frequent droughts with relative consistency in the ESMDI, indicating a strong resilience of soil moisture to reservoir water management. 

Given the frequent occurrence of drought events as indicated by SRSI and SWII, soil moisture conditions in Dongmyeon and Nohong show a relatively stable status due to effective water management systems that minimize the impact of drought on soil moisture levels. Similar findings were reported by Wan et al. (2017), indicating that reservoir operations and land management practices mitigate the impact of drought on soil moisture. 

SRSI demonstrates greater responsiveness to short-term fluctuations 

12 

_R.A. Salau et al._ 

_Physics and Chemistry of the Earth 141 (2025) 104165_ 



**Fig. 10.** Number of drought events per year of ESMDI, PDSI, and SPI. 

in watershed inflows (SWII) than to soil moisture dynamics (ESMDI) during drought conditions, particularly at the Geumhwa Reservoir. This observed disparity can be attributed to reservoir management practices that mitigate short-term fluctuations in inflow, thereby ensuring a stable water supply. This phenomenon has been supported by previous research conducted by (Huang et al., 2025; Wei et al., 2022). 

The analysis of ESMDI, SRSI, and SWII drought events, as presented in Fig. 13, across five stations evaluated in this study reveals distinct patterns in drought detection. SWII shows a higher frequency of drought events in Dongmyeon and Deogga during 2014–2016, whereas SRSI demonstrates pronounced drought detection in Simgog during 2008–2009. In contrast, ESMDI exhibits moderate drought detection rates but shows notable peaks in Geumhwa during 2010–2011. 

The temporal coherence among the indices varies significantly. The 2014–2016 period demonstrates strong agreement across all three indices at most stations, particularly in Geumhwa and Deogga. 

However, earlier periods (2004–2008) display less consistency, indicating differing sensitivities to various drought conditions. 

Spatial analysis highlights that Simgog and Deogga experienced more frequent drought events compared to other stations, especially when measured by SRSI. This pattern likely reflects local hydrological conditions influencing runoff processes. A stronger correlation is observed between SRSI and SWII, likely due to their shared focus on hydrological parameters. However, ESMDI captures unique drought events not detected by the other indices, particularly in Geumhwa and Dongmyeon during 2010–2012. 

These findings suggest that while ESMDI, SRSI, and SWII generally capture similar drought patterns, their differing sensitivities to hydrological components provide complementary insights. This highlights the importance of comparing ESMDI with other indices, such as SRSI and SWII, to understand the drought conditions of the region comprehensively. 

13 

_R.A. Salau et al.                                                                                                                                                                                                                                Physics and Chemistry of the Earth_ 

_Physics and Chemistry of the Earth 141 (2025) 104165_ 



**Fig. 11.** Boxplots of the Correlation plot between ESMDI, SWII, and SRSI. 

### _3.4. Agricultural drought_ 

The phenological stage of the crop primarily determines crop yield and has been used in previous studies to validate drought indices for monitoring drought conditions (Mishra et al., 2015; Rhee et al., 2010). Crop sensitivities to water stress are usually proportional to the development stage (Steduto et al., 2012). When a drought occurs at a crop non-sensitive growth stage, the impact on yield may be minimal compared to when the drought occurs at a sensitive stage of crop growth (Mishra et al., 2015). This study used Sesame yield obtained from Adong, Uiseong, Gunwi, and Yecheon from 2006 to 2015 to evaluate ESMDI. The correlation between sesame and ESMDI from April to October was estimated in each station, and the correlation between sesame yield and ESMDI was highest in July of all the months. July, which is summer and the phenological stage for most open-field crops in Korea, is characterized by heat, which can hinder crop yield because yield diminishes once the temperature is above the critical threshold ( _>_ 35<sup>◦</sup> C for sesame during the flowering stage) (Kumazaki et al., 2009). The high correlation in July suggests that heat stress-induced soil moisture deficits greatly impact crop yield. This sensitivity to heat is high during the thermal-sensitive period (TSP), which coincides with the flowering stage of the crops, usually occurring in summer over the period of June to August. 

The strong relationship of ESMDI with yield outputs of sesame is probably a result of the inclusion of LST in the computation of ESMDI. This agrees with earlier studies that identified the susceptibility of crucial phenological stages of corn and soybeans to drought, a vital component of crop yield estimation (Johnson, 2014; Otkin et al., 2016). Fig. 14 shows the Scatter plots of annual yield (kg/ha) versus ESMDI together with the value of R<sup>2</sup> from all stations. The statistical analysis revealed a significant correlation, p _<_ 0.05, for all stations. Even though the amount of data for sesame is five years, correlations look promising, and the R<sup>2</sup> are 0.61, 0.76, 0.71, and 0.78 for Andong, Gunwi, Uiseong, and Yecheon, respectively. 

### _3.5. Advancements, and potential ESMDI_ 

The Enhanced Standardized Soil Moisture Drought Index (ESMDI) builds upon previous work in soil moisture-based drought monitoring, 

particularly the concepts introduced by Park et al. (2017) and Sun et al. (2022). The novelty of this study lies in integrating high-resolution downscaled soil moisture data from the land surface model (GLDAS) with multiple environmental variables (LST, NDVI, EVI, LAI, ET, Albedo, CHIRPS-V2.0 precipitation, DEM, and bulk density) through advanced deep-learning techniques, thereby enhancing the spatial detail and accuracy of drought monitoring. This approach represents an evolution of existing methodologies with improvements focused on the integration of multiple data sources and downscaling approaches. The soil moisture-based drought index is very useful for monitoring meteorological drought that occurs due to the lack of precipitation, hydrological drought characterized by low stream flow or water level in reservoirs, and agricultural drought that is triggered by soil moisture deficiency. 

The 1 km downscaled soil moisture data offers several practical benefits compared to the original 0.25-degree resolution. Local variations in soil moisture are crucial for effective agricultural management and drought monitoring at this finer resolution. For example, a single 0.25-degree pixel covers about 625 km<sup>2</sup> , which may obscure significant local differences in soil moisture patterns. The 1 km resolution enables the detection of moisture variations at the field level, which is especially important in areas with complex topography or diverse land use, such as Gyeongsangbuk-do. The approach used in this study can be applied to any region, particularly where ground-based soil moisture observations are scarce, as all data used in this study are derived from land surface models and satellite sources. The development and validation of the Enhanced Soil Moisture Drought Index (ESMDI) have provided valuable insights into its drought monitoring capabilities. The enhancedresolution (1 km) soil moisture data produced through deep-learning downscaling offers more detailed spatial information than traditional coarse-resolution products. Strong correlations with established drought indices in spring and autumn indicate ESMDI’s effectiveness in identifying seasonal drought patterns. However, its variable performance during the summer months underscores the challenges of drought monitoring during periods of intense meteorological activity. The evaluation of ESMDI demonstrates its ability to effectively monitor the three main types of droughts: meteorological, hydrological, and agricultural, particularly during the dry seasons (spring and autumn) when precipitation is minimal due to the high correlation of these indices with ESMDI. 

14 

_R.A. Salau et al.                                                                                                                                                                                                                                Physics and Chemistry of the Earth_ 

_Physics and Chemistry of the Earth 141 (2025) 104165_ 



**Fig. 12.** Time series plot of SWII, SRSI, and ESMDI. 

### _3.6. Policy Implementation_ 

The Improved Soil Moisture Drought Index (ESMDI), built with a high spatial resolution of 1 km, is of immense potential for improving drought policy and management practices. Its power to detect meteorological, hydrological, and agricultural droughts makes it a reliable tool for early warning, allowing governments to identify and act on drought more quickly and accurately. With the integration of ESMDI into national and subnational drought planning initiatives, policymakers can issue early warnings that help farmers, water managers, and local communities evade water scarcity impacts. The high correlation of the index with crop yields at peak growth phases implies its ability to help in agricultural planning and precision irrigation, thereby enabling the maximum exploitation of available limited water resources to preserve food production. Moreover, ESMDI has the ability to inform land-use planning, reservoir management, and climate adaptation policy through detailed insight into local soil moisture variability. Such integration directly facilitates the achievement of Sustainable Development Goals, specifically SDG 2 Zero Hunger and SDG 6 Clean Water and Sanitation, through sustainable water use and food security enhancement. Most importantly, ESMDI is scalable beyond the initial study region because it is based on globally available satellite and model data, making the methodology transferable to other drought regions where ground monitoring is limited. The integration of ESMDI into policy 

mechanisms, both at the national and regional levels, therefore, has the capacity to enhance anticipatory action against drought, minimize agricultural as well as economic losses, and build climate change resilience (Liu et al., 2025c). 

### _3.7. Limitations of ESMDI_ 

Despite the robustness of ESMDI, there are some limitations that need to be recognized. While the downscaled soil moisture data has a resolution of 1 km, it may still contain inaccuracies in areas with heterogeneous land cover or complex topography. The dependence on GLDAS-V2 soil moisture data derived from model outputs could introduce biases, particularly in regions where in situ validation data is scarce. Additionally, the performance of deep learning models may vary with seasonal and climatic changes, which could affect soil moisture dynamics and the model’s applicability across different time periods. 

The study area includes agricultural regions with active irrigation systems, particularly during growing seasons and drought periods. While irrigation practices can significantly influence soil moisture measurements, the models used in the study do not explicitly account for these anthropogenic interventions. This limitation may affect the accuracy of soil moisture estimates in irrigated agricultural areas, as the actual soil moisture levels could be higher than model predictions due to irrigation inputs. 

15 

_R.A. Salau et al._ 

_Physics and Chemistry of the Earth 141 (2025) 104165_ 



**Fig. 13.** Number of drought events per year of ESMDI, SRSI, and SWII. 

There is a limitation for acquiring validation data. The downscaled soil moisture data was validated using ten observational data sources; however, these sources may not adequately represent the soil conditions across the entire study area due to their inherent heterogeneity. Future research will incorporate irrigation data and agricultural management practices to improve model accuracy. This could include data on irrigation schedules, water application rates, and irrigation system types to better capture the complete soil moisture dynamics in managed agricultural landscapes. Furthermore, the validation dataset will be augmented with supplementary ground measurements. Additionally, the exploration of the application of the Enhanced Soil Moisture Dynamics Index (ESMDI) across various climatic regions will be undertaken, alongside efforts to optimize model performance during the summer months through improved feature selection. 

### **4. Conclusion** 

The study of soil moisture, a critical determinant of crop yield, is 

essential as it directly contributes to the enhancement of food security, aligning with Sustainable Development Goal 2. This research focuses on soil moisture, which is a key factor in monitoring drought. Six MODIS environmental variables, DEM, bulk density, and CHIRPS precipitation data were used to enhance the resolution of 25 km GLDAS soil moisture data by downscaling it to 1 km resolution through the application of DBN, RF, and XGB. The downscaled SM showed a high correlation with observed measurement, with DBN outperforming RF and XGB in terms of RMSE, MAE, MBD, and R-score metrics. A novel drought index, ESMDI, was developed by normalizing downscaled soil moisture. ESMDI was validated using SPI, PDSI for metrological drought, SWII, and SRSI for Hydrological drought, and yearly sesame yield as a reference for agricultural drought. ESMDI showed a high correlation with metrological and hydrological drought indices, especially during the spring and autumn, although ESMDI demonstrated inconsistent efficacy in monitoring meteorological and hydrological drought conditions in the summer season. There is a high correlation between ESMDI and Sesame yield, especially during the reproductive stage. Future research will 

16 

_Physics and Chemistry of the Earth 141 (2025) 104165_ 

_R.A. Salau et al._ 



**Fig. 14.** Scatter plot between ESMDI and annual Sesame yield (p _<_ 0.05) in July. 

focus on integrating additional soil moisture data and incorporating agricultural/crop management and anthropogenic activities data into downscaling land surface models and soil moisture data. 

### **CRediT authorship contribution statement** 

**Rahmon Abiodun Salau:** Writing – original draft, Software, Methodology, Investigation, Formal analysis, Data curation, Conceptualization. **Bashir Adelodun:** Writing – review & editing, Visualization, Validation, Supervision, Methodology, Investigation, Conceptualization. **Qudus Adeyi:** Visualization, Software, Methodology, Investigation, Data curation. **Adisa Hammed Akinsoji:** Visualization, Software, Methodology, Data curation. **Kyung Sook Choi:** Visualization, Validation, Supervision, Resources, Project administration, Funding acquisition. 

### **Data availability** 

The CHIRPS Precipitation data are freely accessed at https://data. chc.ucsb.edu/products/CHIRPS-2.0/. The Bulk density is available at https://www.soilgrids.org. The In-situ soil moisture is obtained from http://weather.rda.go.kr/. The annual crop data is obtained from https://kostat.go.kr/. The data on agricultural reservoir water level and inflow is available upon request from the Korea Rural Community Corporation (KRC) https://www.ekr.or.kr/. The MODIS dataset is freely accessible at https://developers.google.com/earth-engine/datasets /catalog?filter=MODIS. The digital elevation model (DEM) is freely available at https://earthexplorer.usgs.gov/. The SPI and PDSI data are available upon request from the Korea Disaster Prevention Research Institute. The GLDAS Noah LSM data can be accessed from https://disc. gsfc.nasa.gov/datasets/GLDAS_CLSM025_DA1_D_2.2/summary? keywords=GLDAS. 

### **Declaration of competing interest** 

### **References** 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

### **Acknowledgement** 

This work was supported by the National Research Foundation of Korea (NRF) grant funded by the Korea government (MSIT) (RS-202500562379). 

- Abowarda, A.S., Bai, L., Zhang, C., Long, D., Li, X., Huang, Q., Sun, Z., 2021. Generating surface soil moisture at 30 m spatial resolution using both data fusion and machine learning toward better water resources management at the field scale. Remote Sens. Environ. 255. https://doi.org/10.1016/j.rse.2021.112301. 

Albergel, C., de Rosnay, P., Gruhier, C., Munoz-Sabater, J., Hasenauer, S., Isaksen, L., ˜ Kerr, Y., Wagner, W., 2012. Evaluation of remotely sensed and modelled soil moisture products using global ground-based in situ observations. Remote Sens. Environ. 118, 215–226. https://doi.org/10.1016/j.rse.2011.11.017. 

Ali, S., Khorrami, B., Jehanzaib, M., Tariq, A., Ajmal, M., Arshad, A., Shafeeque, M., Dilawar, A., Basit, I., Zhang, L., Sadri, S., Niaz, M.A., Jamil, A., Khan, S.N., 2023. Spatial downscaling of GRACE data based on XGBoost model for improved understanding of hydrological droughts in the Indus Basin Irrigation System (IBIS). Remote Sens (Basel) 15. https://doi.org/10.3390/rs15040873. 

17 

_Physics and Chemistry of the Earth 141 (2025) 104165_ 

_R.A. Salau et al._ 

- Anees, S.A., Mehmood, K., Khan, W.R., Sajjad, M., Alahmadi, T.A., Alharbi, S.A., Luo, M., 2024. Integration of machine learning and remote sensing for above ground biomass estimation through Landsat-9 and field data in temperate forests of the Himalayan region. Ecol. Inform. 82. https://doi.org/10.1016/j.ecoinf.2024.102732. 

- Arabameri, A., Chandra Pal, S., Santosh, M., Chakrabortty, R., Roy, P., Moayedi, H., 2022. Drought risk assessment: integrating meteorological, hydrological, agricultural and socio-economic factors using ensemble models and geospatial techniques. Geocarto Int. 37, 6087–6115. https://doi.org/10.1080/ 10106049.2021.1926558. 

- Cai, Y., Fan, P., Lang, S., Li, M., Muhammad, Y., Liu, A., 2022. Downscaling of SMAP soil moisture data by using a deep belief network. Remote Sens. 14 (22). https://doi.org/ 10.3390/rs14225681. 

- Chen, Y., Yang, K., Qin, J., Zhao, L., Tang, W., Han, M., 2013. Evaluation of AMSR-E retrievals and GLDAS simulations against observations of a soil moisture network on the central Tibetan Plateau. J. Geophys. Res. Atmos. 118, 4466–4475. https://doi. org/10.1002/jgrd.50301. 

- Dehghan, S., Salehnia, N., Sayari, N., Bakhtiari, B., 2020. Prediction of meteorological drought in arid and semi-arid regions using PDSI and SDSM: a case study in Fars Province, Iran. J Arid Land 12, 318–330. https://doi.org/10.1007/s40333-0200095-5. 

- Du, M., Zhang, J., Wang, Y., Liu, H., Wang, Z., Liu, C., Yang, Q., Hu, Y., Bao, Z., Liu, Y., Jin, J., Zhou, X., Wang, G., 2021. Evaluating the contribution of different environmental drivers to changes in evapotranspiration and soil moisture, a case study of the Wudaogou Experimental Station. J. Contam. Hydrol. 243. https://doi. org/10.1016/j.jconhyd.2021.103912. 

- Frazier, A.G., Giardina, C.P., Giambelluca, T.W., et al., 2022. A century of drought in Hawaiʻi: geospatial analysis and synthesis across hydrological, ecological, and socioeconomic scales. Sustainability 14. https://doi.org/10.3390/su141912023. 

- Funk, C., Peterson, P., Landsfeld, M., Pedreros, D., Verdin, J., Shukla, S., Husak, G., Rowland, J., Harrison, L., Hoell, A., Michaelsen, J., 2015. The climate hazards infrared precipitation with stations - a new environmental record for monitoring extremes. Sci. Data 2. https://doi.org/10.1038/sdata.2015.66. 

- Gong, J., Liu, X., Yao, C., Li, Z., Weerts, A.H., Li, Q., Bastola, S., Huang, Y., Xu, J., 2025. State updating of the Xin’anjiang model: joint assimilating streamflow and multisource soil moisture data via the asynchronous ensemble Kalman filter with enhanced error models. Hydrol. Earth Syst. Sci. 29, 335–360. https://doi.org/ 10.5194/hess-29-335-2025. 

- Hao, Z., Singh, V.P., 2015. Drought characterization from a multivariate perspective: a review. J. Hydrol. (Amst.). https://doi.org/10.1016/j.jhydrol.2015.05.031. 

- He, M., Dong, J., Liu, X., Kang, S., Sun, Y., Deng, L., Zhang, X., 2025. Lithium isotope fractionation in Weinan loess and implications for pedogenic processes and groundwater impact. Glob. Planet. Change. 252, 104865. https://doi.org/10.1016/j. gloplacha.2025.104865. 

- Hinton, G.E., Osindero, S., The, Y.W., 2006. A fast learning algorithm for deep belief nets. Neural Comput. 18 (7), 1527–1554. https://doi.org/10.1162/ neco.2006.18.7.1527. 

- Huang, B.Q., Li, X., 2023. Wave attenuation by sea ice in the Arctic Marginal ice zone observed by spaceborne SAR. Geophys. Res. Lett. 50 (21), e2023GL105059. https:// doi.org/10.1029/2023GL105059. 

- Huang, E., Zhu, G., Meng, G., Wang, Y., Chen, L., Miao, Y., Li, W., 2025. Historical dataset of reservoir construction in arid regions. Sci. Data 12 (1), 1428. https://doi. org/10.1038/s41597-025-05712-3. 

- Hussain, S., Mubeen, M., Nasim, W., Karuppannan, S., Ahmad, A., Amjad, M., Akram, W., 2024. Assessing the impact of land use land cover changes on soil moisture and vegetation cover in Southern Punjab, Pakistan using multi-temporal satellite data. Geol. ecol. landsc. 1–16. https://doi.org/10.1080/24749508.2024.2338970. 

- Im, J., Park, S., Rhee, J., Baik, J., Choi, M., 2016. Downscaling of AMSR-E soil moisture with MODIS products using machine learning approaches. Environ. Earth Sci. 75. https://doi.org/10.1007/s12665-016-5917-6. 

- Johnson, D.M., 2014. An assessment of pre- and within-season remotely sensed variables for forecasting corn and soybean yields in the United States. Remote Sens. Environ. 141, 116–128. https://doi.org/10.1016/j.rse.2013.10.027. 

- Jung, H.C., Kang, D.H., Kim, E., Getirana, A., Yoon, Y., Kumar, S., Peters-lidard, C.D., Hwang, E.H., 2020. Towards a soil moisture drought monitoring system for South Korea. J. Hydrol. (Amst.) 589. https://doi.org/10.1016/j.jhydrol.2020.125176. 

- Karunakalage, A., Lee, J.Y., Daqiq, M.T., Cha, J., Jang, J., Kannaujiya, S., 2024. Characterization of groundwater drought and understanding of climatic impact on groundwater resources in Korea. J. Hydrol. (Amst.) 634. https://doi.org/10.1016/j. jhydrol.2024.131014. 

- Kim, M., Im, J., Han, H., Kim, J., Lee, S., Shin, M., Kim, H.C., 2015. Landfast sea ice monitoring using multisensor fusion in the Antarctic. GIsci Remote Sens 52, 239–256. https://doi.org/10.1080/15481603.2015.1026050. 

- Kumar, A., Kaushik, K., Singh, G., 2024. Predicting soil moisture levels using ensemble machine learning methods. In: 10th International Conference on Advanced Computing and Communication Systems, pp. 127–132. https://doi.org/10.1109/ ICACCS60874.2024.10716881. ICACCS 2024. 

- Kumar, M., Paramaputra, K., Mousa, A., Kong, S.Y., Garg, A., Anggraini, V., 2025. Field based analysis of vegetation and climate impacts on the hydrological properties of urban vegetated slope. Sci. Rep. 15. https://doi.org/10.1038/s41598-025-92031-7. 

- Kumazaki, T., Yamada, Y., Karaya, S., Kawamura, M., Hirano, T., Yasumoto, S., Katsuta, M., Michiyama, H., 2009. Effects of day length and air and soil temperatures on sesamin and sesamolin contents of sesame seed. Plant Prod. Sci. 12 (4), 481–491. https://doi.org/10.1626/pps.11.178. 

- Kwon, M., Kwon, H.H., Han, D., 2019. Spatio-temporal drought patterns of multiple drought indices based on precipitation and soil moisture: a case study in South Korea. Int. J. Climatol. 39, 4669–4687. https://doi.org/10.1002/joc.6094. 

- Lee, J., Kim, Y., Wang, D., 2022. Assessing the characteristics of recent drought events in South Korea using WRF-Hydro. J. Hydrol. (Amst.) 607. https://doi.org/10.1016/j. jhydrol.2022.127459. 

- Li, F., Lu, H., Wang, G., Qiu, J., 2024. Long-term capturability of atmospheric water on a global scale. Water Resour. Res. 60 (12), e2023WR034757. https://doi.org/ 10.1029/2023WR034757. 

- Li, R., Qi, X., Chen, L., Zhu, G., Meng, G., Wang, Y., Li, W., 2025a. Hydrological processes in continental valley basins: evidence from water stable isotopes. Catena 259, 109314. https://doi.org/10.1016/j.catena.2025.109314. 

- Li, R., Zhu, G., Chen, L., Qi, X., Lu, S., Meng, G., Gun, Y., 2025b. Global stable isotope dataset for surface water. Earth Syst. Sci. Data 17 (5), 2135–2145. https://doi.org/ 10.5194/essd-17-2135-2025. 

- Li, Z.L., Leng, P., Zhou, C., Chen, K.S., Zhou, F.C., Shang, G.F., 2021. Soil moisture retrieval from remote sensing measurements: current knowledge and directions for the future. Earth Sci. Rev. https://doi.org/10.1016/j.earscirev.2021.103673. 

- Li, Z.L., Wu, H., Duan, S.B., Zhao, W., Ren, H., Liu, X., Leng, P., Tang, R., Ye, X., Zhu, J., Sun, Y., Si, M., Liu, M., Li, J., Zhang, X., Shang, G., Tang, B.H., Yan, G., Zhou, C., 2023. Satellite remote sensing of global land surface temperature: definition, methods, products, and applications. Rev. Geophys. https://doi.org/10.1029/ 2022RG000777. 

- Liu, T., Yu, L., Yan, Z., Li, X., Bu, K., Yang, J., 2025b. Enhanced climate mitigation feedbacks by wetland vegetation in semi-arid compared to humid regions. Geophys. Res. Lett. 52 (9), e2025GL115242. https://doi.org/10.1029/2025GL115242. 

- Liu, W., Wang, J., Zuo, H., Fu, Z., Xiao, W., Cui, Y., Zhou, Z., 2025a. Spatiotemporal distribution and variation characteristics of convective activities in different climate zones in Northern China based on 25 years of satellite observations. Int. J. Climatol. 45 (10), e8908. https://doi.org/10.1002/joc.8908. 

- Liu, Y., Qiu, H., Wang, N., Yang, D., Zhao, K., Yang, G., Luo, W., 2025c. Thermokarst disturbance responses to climate change across the circumpolar permafrost regions from 1990 to 2023. Geosci. Front., 102147 https://doi.org/10.1016/j. gsf.2025.102147. 

- Lu, S., Zhu, G., Qiu, D., Li, R., Jiao, Y., Meng, G., Chen, L., 2025. Optimizing irrigation in arid irrigated farmlands based on soil water movement processes: knowledge from water isotope data. Geoderma 460, 117440. https://doi.org/10.1016/j. geoderma.2025.117440. 

- Mecklenburg, S., Drusch, M., Kerr, Y.H., Font, J., Martin-Neira, M., Delwart, S., Buenadicha, G., Reul, N., Daganzo-Eusebio, E., Oliva, R., Crapolicchio, R., 2012. ESA’s soil moisture and ocean salinity mission: mission performance and operations. IEEE Trans. Geosci. Rem. Sens. 50, 1354–1366. https://doi.org/10.1109/ TGRS.2012.2187666. 

- Mishra, A.K., Ines, A.V.M., Das, N.N., Prakash Khedun, C., Singh, V.P., Sivakumar, B., Hansen, J.W., 2015. Anatomy of a local-scale drought: application of assimilated remote sensing products, crop model, and statistical methods to an agricultural drought study. J. Hydrol. (Amst.) 526, 15–29. https://doi.org/10.1016/j. jhydrol.2014.10.038. 

- Nazir, J., Ali, M., Sarwar, A., Khan, S., Rehman, K., Fahim, B., Iqbal, B., 2024. Delineation and validation of GIS-based groundwater potential zones under arid to semi-arid environment using multi-influence-factors approach. Geol. ecol. landsc. 1–17. https://doi.org/10.1080/24749508.2024.2392382. 

- Ning, J., Yao, Y., Fisher, J.B., Li, Y., Zhang, Xiaotong, Jiang, B., Xu, J., Yu, R., Liu, L., Zhang, Xueyi, Xie, Z., Fan, J., Zhang, L., 2024. Soil moisture-derived SWDI at 30 m based on multiple satellite datasets for agricultural drought monitoring. Remote Sens (Basel) 16. https://doi.org/10.3390/rs16183372. 

- Ojha, S.S., Singh, V., Roshni, T., 2021. Comparison of meteorological drought using spi and spei. Civil Engineering Journal (Iran) 7, 2130–2149. https://doi.org/10.28991/ cej-2021-03091783. 

- Okuyama, A., Imaoka, K., 2015. Intercalibration of Advanced Microwave Scanning Radiometer-2 (AMSR2) brightness temperature. IEEE Trans. Geosci. Rem. Sens. 53, 4568–4577. https://doi.org/10.1109/TGRS.2015.2402204. 

- Otkin, J.A., Anderson, M.C., Hain, C., Svoboda, M., Johnson, D., Mueller, R., Tadesse, T., Wardlow, B., Brown, J., 2016. Assessing the evolution of soil moisture and vegetation conditions during the 2012 United States flash drought. Agric. For. Meteorol. 218–219, 230–242. https://doi.org/10.1016/j.agrformet.2015.12.065. 

- Pang, Q., Zhao, G., Wang, D., Zhu, X., Xie, L., Zuo, D., Chu, W., 2024. Water periods impact the structure and metabolic potential of the nitrogen-cycling microbial communities in rivers of arid and semi-arid regions. Water Res. 267, 122472. 

   - https://doi.org/10.1016/j.watres.2024.122472. 

- Park, Seonyoung, Im, J., Park, Sumin, Rhee, J., 2017. Drought monitoring using high resolution soil moisture through multi-sensor satellite data fusion over the Korean peninsula. Agric. For. Meteorol. 237–238, 257–269. https://doi.org/10.1016/j. agrformet.2017.02.022. 

- Piles, M., Camps, A., Vall-Llossera, M., Corbella, I., Panciera, R., Rudiger, C., Kerr, Y.H., Walker, J., 2011. Downscaling SMOS-derived soil moisture using MODIS visible/ infrared data. IEEE Trans. Geosci. Rem. Sens. 49 (9), 3156–3166. https://doi.org/ 10.1109/TGRS.2011.2120615. 

- Rhee, J., Im, J., Carbone, G.J., 2010. Monitoring agricultural drought for arid and humid regions using multi-sensor remote sensing data. Remote Sens. Environ. 114, 2875–2887. https://doi.org/10.1016/j.rse.2010.07.005. 

- Rodell, B.M., Houser, P.R., Jambor, U., Gottschalck, J., Mitchell, K., Meng, C., Arsenault, K., Cosgrove, B., Radakovich, J., Bosilovich, M., Entin, J.K., Walker, J.P., Lohmann, D., Toll, D., 2004. The Global Land Data Assimilation System This Powerful New Land Surface Modeling System Integrates Data from Advanced Observing Systems to Support Improved Forecast Model Initialization and Hydrometeorological Investigations, 10.1. 

- Rostami, A., Raeini-Sarjaz, M., Chabokpour, J., Chadee, A.A., 2023. Soil moisture monitoring by downscaling of remote sensing products using LST/VI space derived 

18 

_Physics and Chemistry of the Earth 141 (2025) 104165_ 

_R.A. Salau et al._ 

from MODIS products. Water Supply 23 (2), 688–705. https://doi.org/10.2166/ 

WS.2023.002. 

- Ryu, J.H., Han, K.S., Lee, Y.W., Park, N.W., Hong, S., Chung, C.Y., Cho, J., 2019. Different agricultural responses to extreme drought events in neighboring counties of South and North Korea. Remote Sens (Basel) 11. https://doi.org/10.3390/ rs11151773. 

- Sa’adi, Z., Yusop, Z., Alias, N.E., Shiru, M.S., Muhammad, M.K.I., Ramli, M.W.A., 2023. Application of CHIRPS dataset in the selection of rain-based indices for drought assessments in Johor River Basin, Malaysia. Sci. Total Environ. 892. https://doi.org/ 10.1016/j.scitotenv.2023.164471. 

- Senanayake, I.P., Pathira Arachchilage, K.R.L., Yeo, I.Y., Khaki, M., Han, S.C., Dahlhaus, P.G., 2024. Spatial downscaling of satellite-based soil moisture products using machine learning techniques: a review. Remote Sens (Basel). https://doi.org/ 10.3390/rs16122067. 

- Smith, A.A., Tetzlaff, D., Maneta, M., Soulsby, C., 2022. Critical zone response times and water age relationships under variable catchment wetness states: insights using a tracer-aided ecohydrological model. Water Resour. Res. 58. https://doi.org/ 10.1029/2021WR030584. 

- Sohrabi, M.M., Ryu, J.H., Abatzoglou, J., Tracy, J., 2015. Development of soil moisture drought index to characterize droughts. J. Hydrol. Eng. 20. https://doi.org/ 10.1061/(asce)he.1943-5584.0001213. 

- Spennemann, P.C., Rivera, J.A., Celeste Saulo, A., Penalba, O.C., 2015. A comparison of GLDAS soil moisture anomalies against standardized precipitation index and multisatellite estimations over South America. J. Hydrometeorol. 16, 158–171. https://doi.org/10.1175/JHM-D-13-0190.1. 

- Srivastava, P.K., Pandey, V., Suman, S., Gupta, M., Islam, T., 2016. Available data sets and satellites for terrestrial soil moisture estimation. In: Satellite Soil Moisture Retrieval: Techniques and Applications. Elsevier Inc., pp. 29–44. https://doi.org/ 10.1016/B978-0-12-803388-3.00002-4 

- Steduto, P., Hsiao, T.C., Fereres, E., Raes, D., Müller, A., 2012. Crop yield response to 

   - water. Food And Agriculture Organization Of The United Nations. 

- Su, Y., Cui, Y., Dupla, J., Canou, J., 2021. Soil-water retention behaviour of fine/coarse soil mixture with varying coarse grain contents and fine soil dry densities. Can. Geotech. J. 59 (2), 291–299. https://doi.org/10.1139/cgj-2021-0054. 

- Sun, H., Ma, X., Liu, Y., Zhou, G., Ding, J., Lu, L., Zhang, F., 2024. A new multiangle method for estimating fractional biocrust coverage from Sentinel-2 data in arid areas. IEEE Trans. Geosci. Remote Sens. 62, 1–15. https://doi.org/10.1109/ TGRS.2024.3361249. 

- Sun, X., Lai, P., Wang, S., Song, L., Ma, M., Han, X., 2022. Monitoring of extreme agricultural drought of the past 20 years in Southwest China using GLDAS soil moisture. Remote Sens (Basel) 14. https://doi.org/10.3390/rs14061323. 

- Tavakol, A., McDonough, K.R., Rahmani, V., Hutchinson, S.L., Hutchinson, J.M.S., 2021. The soil moisture data bank: the ground-based, model-based, and satellite-based soil moisture data. Remote Sens. Appl. https://doi.org/10.1016/j.rsase.2021.100649. 

- Van Loon, A.F., Van Huijgevoort, M.H.J., Van Lanen, H.A.J., 2012. Evaluation of drought propagation in an ensemble mean of large-scale hydrological models. Hydrol. Earth Syst. Sci. 16, 4057–4078. https://doi.org/10.5194/hess-16-4057-2012. 

- Wan, W., Zhao, J., Li, H.Y., Mishra, A., Ruby Leung, L., Hejazi, M., Wang, W., Lu, H., Deng, Z., Demissisie, Y., Wang, H., 2017. Hydrological drought in the anthropocene: impacts of local water extraction and reservoir regulation in the U.S. J. Geophys. Res. Atmos. 122 (11). https://doi.org/10.1002/2017JD026899, 313-11,328. 

- Wang, M., He, G., Hu, T., Yang, M., Zhang, Z., Zhang, Z., et al., 2024. Innovative hybrid algorithm for simultaneous land surface temperature and emissivity retrieval: case study with SDGSAT-1 data. Remote Sens. Environ. 315, 114449. https://doi.org/ 10.1016/j.rse.2024.114449. 

Eurasia. Atmos. Res. 314, 107813. https://doi.org/10.1016/j. 

atmosres.2024.107813. 

   - Wang, S., Zhu, C., Huang, Z., Li, Y., Cui, C., Zhang, C., 2025. Primary roles of soil evaporation and vegetation in driving terrestrial evapotranspiration across global drylands. Sci. Total Environ. 958. https://doi.org/10.1016/j.scitotenv.2024.178073. 

   - Wei, W., Xu, W., Deng, J., Guo, Y., 2022. Self-aeration development and fully crosssectional air diffusion in high-speed open channel flows. J. Hydraul. Res. 60 (3), 445–459. https://doi.org/10.1080/00221686.2021.2004250. 

   - Wei, Z., Kou, J., Miao, L., Hu, F., Li, L., Wu, X., Meng, L., 2025. Exploring diurnal variation in soil moisture via sub-daily estimates reconstruction. J. Hydrol. 662, 134005. https://doi.org/10.1016/j.jhydrol.2025.134005. 

   - Wei, Z., Miao, L., Peng, J., Zhao, T., , moisture mapping by coupling physic, Meng, L., Lu, H., Shi, J., 2024. Bridging spatio-temporal discontinuities in global soil s in deep learning. Remote Sens. Environ. 313, 114371. https://doi.org/10.1016/j. rse.2024.114371. 

   - Wu, K., Li, X., 2024. Deep learning for retrieving omni-directional ocean wave spectra from spaceborne synthetic aperture radar. Remote Sens. Environ. 314, 114386. https://doi.org/10.1016/j.rse.2024.114386. 

   - Yan, F., He, B., Lyne, V., Fan, R., Cui, Y., Wang, X., Su, F., 2025. Global coastal water clarity has increased due to human intervention. Commun. Earth Environ. 6 (1), 641. https://doi.org/10.1038/s43247-025-02638-x. 

   - Yang, D., Yang, Y., Xia, J., 2021. Hydrological cycle and water resources in a changing world: a review. Geogr. Sustain. https://doi.org/10.1016/j.geosus.2021.05.003. 

   - Yi, J., Li, H., Zhao, Y., Shao, M., Zhang, H., Liu, M., 2022. Assessing soil water balance to optimize irrigation schedules of flood-irrigated maize fields with different cultivation histories in the arid region. Agric. Water Manag. 265, 107543. https:// doi.org/10.1016/j.agwat.2022.107543. 

   - Ying, X., Liu, L., Lin, Z., Shi, Y., Wang, Y., Li, R., An, W., 2025. Infrared small target detection in satellite videos: a new dataset and a novel recurrent feature refinement framework. IEEE Trans. Geosci. Remote Sens. 63, 1–18. https://doi.org/10.1109/ TGRS.2025.3542368. 

   - Zhang, A., Jia, G., 2013. Monitoring meteorological drought in semiarid regions using multi-sensor microwave remote sensing data. Remote Sens. Environ. 134, 12–23. https://doi.org/10.1016/j.rse.2013.02.023. 

   - Zhang, Q., Liu, W., Yue, P., Zhang, L., Wang, S., Yang, J., Yan, X., 2025. Discussion on major drought issues in the Northern drought-prone Belt in China. Bull. Am. Meteorol. Soc. 106 (4), E678–E706. https://doi.org/10.1175/BAMS-D-24-0176.1. 

   - Zhao, H., Li, J., Yuan, Q., Lin, L., Yue, L., Xu, H., 2022. Downscaling of soil moisture products using deep learning: Comparison and analysis on Tibetan Plateau. J. Hydrol. (Amst.) 607. https://doi.org/10.1016/j.jhydrol.2022.127570. 

   - Zhao, Y., Wang, H., Song, B., Xue, P., Zhang, W., Peth, S., Horn, R., 2023. Characterizing uncertainty in process-based hydraulic modeling, exemplified in a semiarid Inner Mongolia steppe. Geoderma 440, 116713. https://doi.org/10.1016/j. geoderma.2023.116713. 

   - Zhou, G., Qian, L., Gamba, P., 2024. A novel iterative self-organizing pixel matrix entanglement classifier for remote sensing imagery. IEEE Trans. Geosci. Remote Sens. 62, 1–21. https://doi.org/10.1109/TGRS.2024.3424227. 

   - Zhou, G., Zhi, H., Gao, E., Lu, Y., Chen, J., Bai, Y., Zhou, X., 2025. DeepU-Net: a parallel dual-branch model for deeply fusing multiscale features for road extraction from high-resolution remote sensing images. IEEE J. Sel. Top. Appl. Earth Obs. 18, 9448–9463. https://doi.org/10.1109/JSTARS.2025.3555636. 

   - Zhu, Q., Zhou, Z., Duncan, E.W., Lv, L., Liao, K., Feng, H., 2017. Integrating real-time and manual monitored data to predict hillslope soil moisture dynamics with high spatiotemporal resolution using linear and non-linear models. J. Hydrol. (Amst.) 545, 1–11. https://doi.org/10.1016/j.jhydrol.2016.12.014. 

- Wang, Q., Liu, Y., Zhu, G., Lu, S., Chen, L., Jiao, Y., Wang, Y., 2025. Regional differences in the effects of atmospheric moisture residence time on precipitation isotopes over 

19 

