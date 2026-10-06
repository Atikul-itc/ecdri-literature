



# <u>Water Resources Research</u> 

### RESEARCH ARTICLE 

10.1029/2017WR021959 

Key Points: 

- Develop a viable approach to validate the satellite soil moisture products 

� Translate model and satellite soil moisture into useful information for drought monitoring 

- An objective blended drought index is recommended 

Correspondence to: 

J. Yin, jifu.yin@noaa.gov 

Citation: 

Yin, J., Zhan, X., Hain, C. R., Liu, J., & Anderson, M. C. (2018). A method for objectively integrating soil moisture satellite observations and model simulations toward a blended drought index. Water Resources Research, 54, 6772–6791. https://doi.org/10.1029/ 2017WR021959 

Received 27 SEP 2017 

Accepted 3 MAY 2018 Accepted article online 7 MAY 2018 Published online 23 SEP 2018 

## A Method for Objectively Integrating Soil Moisture Satellite Observations and Model Simulations Toward a Blended Drought Index 

Jifu Yin<sup>1,2</sup> , Xiwu Zhan<sup>2</sup> , Christopher R. Hain<sup>3</sup> , Jicheng Liu<sup>1,2</sup> , and Martha C. Anderson<sup>4</sup> 

1ESSIC/CICS, University of Maryland College Park, College Park, MD, USA, 2NOAA NESDIS Center for Satellite Applications and Research, College Park, MD, USA,<sup>3</sup> Marshall Space Flight Center, Earth Science Branch, Huntsville, AL, USA,<sup>4</sup> Hydrology and Remote Sensing Laboratory, USDA-ARS, Beltsville, MD, USA 

Abstract With satellite soil moisture (SM) retrievals becoming widely and continuously available, we aim to develop a method to objectively integrate the drought indices into one that is more accurate and consistently reliable. The data sets used in this paper include the Noah land surface model-based SM estimations, Atmosphere-Land-Exchange-Inverse model-based Evaporative Stress Index, and the satellite SM products from the Advanced Scatterometer, WindSat, Soil Moisture and Ocean Salinity, and Soil Moisture Operational Product System. Using the Triple Collocation Error Model (TCEM) to quantify the uncertainties of these data, we developed an optically blended drought index (BDI_b) that objectively integrates drought estimations with the lowest TCEM-derived root-mean-square-errors in this paper. With respect to the reported drought records and the drought monitoring benchmarks including the U.S. Drought Monitor, the Palmer Drought Severity Index and the standardized precipitation evapotranspiration index products, the BDI_b was compared with the sample average blending drought index (BDI_s) and the RMSE-weighted average blending drought indices (BDI_w). Relative to the BDI_s and the BDI_w, the BDI_b performs more consistently with the drought monitoring benchmarks. With respect to the official drought records, the developed BDI_b shows the best performance on tracking drought development in terms of time evolution and spatial patterns of 2010-Russia, 2011-USA, 2013-New Zealand droughts and other reported agricultural drought occurrences over the 2009–2014 period. These results suggest that model simulations and remotely sensed observations of SM can be objectively translated into useful information for drought monitoring and early warning, in turn can reduce drought risk and impacts. 

#### 1. Introduction 

Of all natural disasters, the economic and environmental consequences of drought are among the most serious due to the duration varying from weeks to decades, and widespread spatial extent (AghaKouchak et al., 2015; Anderson et al., 2015; Hao et al., 2014; Lewis et al., 2011; Mazdiyasni & AghaKouchak, 2015; Mu et al., 2013; Zhang et al., 2017). Associated with global climate change, the frequency, duration and severity of drought events show an increasing tendency in some parts of the world (Dai, 2013; Mazdiyasni & AghaKouchak, 2015). Drought indicator development is essential for monitoring drought conditions, providing timely seasonal forecasts, and consequently reducing drought risk and impacts (Pozzi et al., 2013; Sheffield et al., 2014; Tarhule & Lamb, 2003). 

VC 2018. American Geophysical Union. All Rights Reserved. 

Agricultural drought is commonly defined as an event where root-zone soil moisture (SM) deficits result in a reduction in crop yields, plant biomass and ecologic productivity (Anderson et al., 2011; Azmi et al., 2016; Bolten & Crow, 2012; McNally et al., 2015; Wilhite & Glantz 1985; Zhang et al., 2017). The SM status in various soil layers is an important indicator of agricultural drought, providing more information than the rainfall anomaly alone. Modern land surface models (LSMs) offer a complex parameterization of the surface energy balance and detailed vertical water balance physics in an attempt to more accurately characterize temporal variations in root-zone soil moisture availability (Crow et al., 2012; Dai et al., 2003; Ek et al., 2003; Koster et al, 2000; Kowalczyk et al, 2006; Oleson et al., 2004; Yang et al, 2003; Yin et al., 2015a). However, these model-based estimates are typically subject to errors in the model physics and parameterizations, and in the meteorological forcing data (Reichle & Koster, 2004; Yin et al., 2014, 2015b). Data assimilation techniques 

YIN ET AL. 

6772 

Water Resources Research 

10.1029/2017WR021959 

permit the modeled soil moisture (SM) to be corrected toward the observations with the correction degree determined by the error levels associated with each (Reichle & Koster, 2004). With satellite SM retrievals becoming widely and continuously available, it is consequently believed that a land data assimilation system that merges satellite retrievals and model estimates of soil moisture may provide more reasonable values of land surface state variables (Crow & Wood, 2003; Hain et al. 2012; Koster et al., 2009; Kumar et al. 2009; Reichle & Koster, 2004; Yin et al., 2015b, 2015c; Xia et al., 2012; Zhan et al., 2012). In the most widely used ensemble Kalman filter (EnKF), still, satellite SM observations need to be bias-corrected to respect the assumption that retrieval errors are Gaussian-distributed. The current bias-correction approaches used for the EnKF data assimilation might have caused useful information in the observations lost in the model simulations (Nearing et al., 2016). 

While in situ measurements of SM provide reasonable assessments of moisture conditions at the local scale, they are deficient in representing the soil moisture and drought dynamics at large scales due to insufficient data coverage (Yuan et al., 2015). In contrast, microwave (MW, active or passive) remote sensing observations can provide spatially consistent estimates of the SM state. Although they can only sense the surface soil depth, usually within 0–5 cm (Kerr et al., 2001; Naeimi et al., 2009; Njoku et al., 2003; Wang et al., 2015; Yin et al., 2015b), there is generally a close relationship between surface SM and SM in the deeper soil layers at weekly and longer time scale (Albergel et al., 2008). The SM status in surface soil layer represents the fastest response soil moisture dynamics to meteorological anomalies and provides a measure for short-term droughts (Yuan et al., 2015); and the surface information propagating to deeper soil layers is very important to early warning agricultural droughts and monitoring flash droughts that can occur very rapidly (Otkin et al., 2015). However, the MW SM products suffer from the instrument noise and uncertainty in microwave emission modeling. Land surface temperature (LST)- and green vegetation fraction (GVF)-based quality control of the satellite SM retrievals can decrease the impacts of these uncertainties, but the empirical approaches are hard to be widely used (Kumar et al., 2009; Yin et al., 2014). 

Comparison of MW SM products to ground-based SM observations is the most common error estimation approach; however, the in situ observational data from low density networks in which one or two measurements are generally available per satellite footprint can lead to significant differences in the spatial sampling scale (Koster et al., 2009; Miralles et al., 2010). A triple collocation error model (TCEM) methodology was introduced to estimate the root mean square errors (RMSE) while simultaneously solving for systematic differences in the climatologies of a set of three independent data sources (Miralles et al., 2010; Scipal et al., 2008). Based on three separate time series assumed to approximate grid-scale SM products, the TCEM in previous reports exhibited robust capability to assess novel remotely sensed SM data sets in comparison with LSM estimations and in situ observations in a limited number of well sampled pixels (Draper et al., 2013; Miralles et al., 2010). 

Drought monitoring is a complex and multifaceted endeavor, warranting use of multiple tools and indicators; the nature of drought monitoring efforts should thus be based on multiple variables/indicators to provide a more robust and integrated measure of drought through a convergence-of-evidence methodology (AghaKouchak et al., 2015). Current operational drought monitoring products (Heim, 2002; Svoboda et al., 2002; Xia et al., 2014) are generally produced via integrating multiple data sources and derivative products based on a synthesis of indicators/model-simulations and subjective interpretation of how different indicators/model-simulations should be merged in the final analysis. These routinely running drought monitoring products are thus sensitive to the experts’ experiences/judgment and the model uncertainties from errors in the indicators. These types of artificial and product errors can be compensated for by objectively merging multisources drought evaluations through uncertainty-based optimization of remotely sensed observations and model estimations. 

Additionally, to capture different drought characteristic, numerous multivariate drought indices have been recently proposed. The ordinal regression model permits to estimate the probability of each drought category, and in turn to highlight probabilistic drought characterization in the categorical form (Hao et al., 2016). Yet its properly implement is limited by optimal choice of three drought indices in different regions and seasons. Besides, other blended drought indicators including the principal component analysis-based multivariate Aggregate Drought Index (Keyantash & Dracup, 2004; Rajsekhar et al., 2015), the joint distribution of the accumulated precipitation and streamflow-based Joint Drought Index (Kao & Govindaraju, 2010) and Multivariate Standardized Drought Index (Hao & AghaKouchak, 2013) are basically based on the water 

YIN ET AL. 

6773 

Water Resources Research 

10.1029/2017WR021959 

balance model and multivariate analysis (Hao et al., 2016). Thus, development of a method for objectively integrating soil moisture satellite observations and model simulations toward a blended drought index is still challenging. This paper is an attempt in this direction 

In this paper, we aim to objectively determine uncertainties of satellite observation- and model simulationbased drought estimations, and in turn to optimally merge any collection of drought indicators in a fully automated statistical framework. With respect to the drought monitoring benchmarks and the reported drought records, the advantages of the optimally objectively blended drought index over the traditional subjectively integrated drought indices are demonstrated. The specifics of the method are described in the next section. The results and validations are then presented in sections 3–5. The potential of applying the method in drought monitoring operation is discussed in section 6, and a brief summary is given in last section. 

#### 2. Data and Method 

##### 2.1. Data 

For this study, we use 6 different SM products. The first is a land surface model estimate of SM from the Noah version 3.2 (referred to as the NLSM). The layer thickness-weighted average of SM estimates in the top three soil layer (0–10 cm; 10–40 cm; 40–100 cm) is used to characterize root zone (0–100 cm) SM. The NLSM simulations were conducted on a near-global gridded domain (from 2608S, 21808W to 908N, 1808E) at 25 km spatial resolution. The model was spun up by cycling 50 times through the period from 2001 to 2007. Then the simulation was run over the 2008–2014 period with one half hour time-step inputs and daily outputs. Atmospheric forcing (Table 1) was taken from 3 hourly 25 km Global Land Data Assimilation System (GLDAS) precipitation and Global Data Assimilation System (GDAS) meteorological data. Various updates to the specification of vegetation in Noah have been implemented. For example, 2007–2010 Moderate Resolution Imaging Spectroradiometer (MODIS) collection 5 land cover maps and 8 day MODIS leaf area index (LAI)-based green vegetation fraction (GVF) were used to update the climatological fields in Noah (Yin et al, 2015a, 2016). 

The next drought indicator (Table 1) used in the analysis is the Evaporative Stress Index (ESI), generated with the Atmosphere Land Exchange Inverse (ALEXI) model using land surface temperature data retrieved from satellite thermal infrared imagery (Anderson et al., 1997, 2011). The ESI represents temporal anomalies in the ratio of actual evapotranspiration (ET) to potential ET (PET) and requires no information about antecedent precipitation or subsurface soil characteristics (Anderson et al., 2011; Hain et al., 2012). Until recently, ALEXI ESI data production has been limited to areas with high resolution temporal sampling of geostationary sensors (Hain et al., 2015). However, our research team has developed a new and novel method of using twice-daily observations from polar sensors such as MODIS and Visible Infrared Imaging Radiometer Suite (VIIRS) to estimate the mid-morning rise in LST that is used to drive the energy balance estimations within ALEXI. This allows the method to be applied globally using the sensors onboard polar-orbiting satellites rather than a global composite of all available geostationary datasets. The global ALEXI ESI product is available at a spatial resolution of 5 km and a period of record from 2001 to 2014, reprocessed to weekly timesteps and 25-km resolution for this study. 

Finally, we use four microwave-based SM products (Table 1), referred to as MWSM. These products include SM data from the Advanced Scatterometer (ASCAT, Wagner et al., 1999), WindSat (Li et al., 2010) the Soil Moisture and Ocean Salinity (SMOS, Kerr et al, 2001) instruments, and a blended product from the NOAA Soil Moisture Operational Product System (SMOPS, Yin et al., 2015b). The SMOPS has been developed to process satellite soil moisture observational data at the NOAA National Environmental Satellite, Data, and Information Service (NESDIS) for improving numerical weather prediction models at the NOAA National Weather Service (Yin et al., 2014). SMOPS scales the soil moisture data products from the European Space Agency SMOS satellite, ASCAT on EUMETSAT’s Metop-A and Metop-B satellites, and WindSat of Naval Research Lab to the climatology of the Noah land surface model, and merges them to a blended global soil moisture data product (Yin et al., 2015b). In this study, daily ASCAT, WindSat and SMOPS blended SM products are used from 2008 to 2014, along with SMOS SM data derived during the 2011–2014 period. These global microwave SM retrievals are all at 25 km spatial resolution. 

YIN ET AL. 

6774 

Water Resources Research 

10.1029/2017WR021959 

Weekly United States Drought Monitor (USDM) data sets from 2008 to 2014 are used to evaluate the performance of the various blended drought indices (BDIs) over the contiguous United States (CONUS). USDM is the drought map that policymakers and media use in discussions of drought and for allocating drought relief, reflecting drought signals conveyed in one or more indices, and reporting impacts and observations from more than 350 contributors around the country (Svoboda et al., 2002). In addition, the global BDIs’ drought monitoring capabilities are also evaluated against the standard anomalies of the monthly Palmer Drought Severity Index (PDSI) (against the 1985–2014 climatology) at 2.5 degree spatial resolution and the monthly 3 month standardized precipitation evapotranspiration index (SPEI) standard anomalies (against the 1985–2014 climatology) at 0.5 degree spatial resolution for the 2008–2014 time period (Dai, 2013; Vicente-Serrano et al., 2010). As a landmark in the development of drought indices, PDSI uses readily available temperature and precipitation data to estimate relative dryness and has been reasonably successful at quantifying long-term drought (Dai, 2013). SPEI is similar to the standardized precipitation index (SPI), but it includes the role of temperature (Vicente-Serrano et al., 2010). SPEI was developed in 2010 and has been used in an increasing number of climatology and hydrology studies (Beguer�ıa et al., 2014). 

##### 2.2. Method 

The Triple Collocation Error Model (TCEM) assumed that the uncertainties or errors of the three retrieval sources are from mutually distinct sources and are independent from each other (Draper et al., 2013; Janssen et al., 2007; Miralles et al., 2010; Scipal et al., 2008). In this paper, the TCEM is based on three categories of soil moisture data sets that provide 25 km grid-scale SM estimations: (1) the NLSM, which is subject to errors in the model representation and in the meteorological forcing data; (2) the ALEXI model-based ESI, which does not use any precipitation input, but is sensitive to the accuracy of the thermal infrared (TIR) satellite LST and other model inputs (e.g., vegetation cover, available energy); and (3) the microwave satellite retrievals which is based on land surface microwave radiation physics with error sources being microwave satellite sensor signal/noise ratio and soil moisture retrieval algorithm accuracy. 

All of the SM data used in this study were temporally composited over 4 week intervals. Then the uncertainty or RMSE for each of the four MW SM products was individually computed in combination with NLSM and ESI in TCEM in order to meet the error independence requirement of the three data sets used in TCEM. Meanwhile, the NLSM and ESI data sets were evaluated four times with each corresponding to a different MW SM data set. Their errors were calculated as the average of the four RMSE values respectively. The climatology of each of the above-mentioned soil moisture data sets was generated by assembling the variable values for a particular calendar week for all years of the study periods. Once the climatology was assembled, the standardized anomalies (w) were computed for week w, year y, and grid location (i, j), as 



where X and rX are climatology and climatological standard deviations for each of the six retrievals. Thus, drought estimations for MWSM (wMWSM), ESI (wESI) and NLSM (wNLSM) are then expressed as (Draper et al., 2013; Janssen et al., 2007; Miralles et al., 2010; Scipal et al., 2008) 



where P indicates the true drought status, and l, x, and q denote the unknown errors in the MWSM, ESI, and NLSM cases. First, we assume that the three kinds of errors are uncorrelated and: 



Then the RMSE values for MWSM (nMWSM), ESI (nESI) and NLSM (nNLSM) are given by (Miralles et al., 2010; Scipal et al., 2008; Stoffelen, 1998) 

YIN ET AL. 

6775 

Water Resources Research 

10.1029/2017WR021959 



Thus, based on the TCEM, the monthly RMSEs for each of the data sets can be estimated grid by grid within the global domain. 

#### 3. Blended Drought Index (BDI) 

Three techniques for combining the available retrievals into a blended index were evaluated. These include an equal weighted-average blending, an objectively weighted approach, and an optimal integration technique. Three blended drought indices are all generated on a near-global gridded domain (from 2608S, 21808W to 908N, 1808E) at 25 km spatial resolution over 2008–2014 time period. 

##### 3.1. Simple Equal Weighted-Average Blended Drought Index (BDI_s) 

BDI_s samples all SM products with equal importance. To increase the spatial coverage of drought estimations, BDI_s integrates all of the six SM retrievals using a weighted-average blending technique. For the BDI_s, all of the available data sets are assigned the same weight, where the weightings determine the relative importance of each quantity on the average. When the six SM retrievals are all available, the BDI_s for each pixel within the global domain is 



If an index is missing at a given pixel, the BDI_s is computed as an average of the available drought estimations. 

##### 3.2. Objectively Weighted Blended Drought Index (BDI_w) 

Relative to the BDI_s, the BDI_w treats SM products with lower RMSE as higher quality data and assigns that data set a greater weight. Thus, the BDI_w is objectively developed according to monthly TCEM-based RMSE values computed in equation (4). And a weight f(x) for an available index is 



When the drought assessments are all available, then N is 6, and the BDI_w for each pixel over the global domain is 



Given N values from 1 to 5 in equation (6), the BDI_w in equation (7) will be the summation without counting the unavailable drought estimations. 

##### 3.3. Optimal Blended Drought Index (BDI_b) 

The procedure of generating BDI_b for each pixel in the global domain is described in Figure 1. Each pixel is filled by the retrieval that is estimated to have the lowest RMSE based on its TCEM estimate, which ensures that all pixels across the global domain can be covered by the optimal drought estimation information, instead of integrating the evaluations by building their weights. The monthly TCEM-based RMSE for each of the six retrievals used here can characterize their time series throughout the year. 

#### 4. Evaluation With Benchmark Drought Monitor Products 

Drought intensity is classified in the USDM into five categories (Table 2) including D0, abnormally dry (percentile < 30%); D1, moderate drought (percentile < 20%); D2, severe drought (percentile < 10%); D3, extreme drought (percentile < 5%); and D4, exceptional drought (percentile < 2%). The statistics of 

YIN ET AL. 

6776 

Water Resources Research 

10.1029/2017WR021959 



Figure 1. The procedure for constructing the BDI_b using the RMSEs estimated from the Triple Collocation Error Model implemented for each grid in each calendar month. RMSEmin is the minimum RMSE for a grid. And RMSESMOPS, RMSENLSM, and RMSEESI are the monthly RMSE values for soil moisture data sets from SMOPS, NLSM and ESI cases, respectively. 

frequency probability for each case here was collected on the global domain over the study period. The large sample size indicates the statistical results here are qualitatively stable and high likely representative of common conditions. Thus, all the indices are classified into five categories using the thresholds in Table 2. 

Based on the assumptions that the drought categories are continuous numbers, Figures 2 and 3 show maps describing the temporal correlation between the USDM and each of the drought indices classified using the thresholds in Table 2, which are considered in the intercomparison of linear correlation in weekly climatedivision-based ranking of moisture conditions. The CONUS domain-averaged correlation coefficients (R) for the ASCAT (sample size N 5 364, there are 364 weeks during the period 2008–2014), SMOS (N 5 208, there are 208 weeks during the period 2011–2014), WindSat (N 5 364), SMOPS (N 5 364), NLSM (N 5 364), and ESI (N 5 364) retrievals are 0.38, 0.11, 0.18, 0.28, 0.40, and 0.35, respectively. The spatial patterns of the correlations between the USDM and the three BDIs agree well (Figure 3). Stronger correlations are observed over the Great Plains and the northeastern United States. These are areas of LST and vegetation indices tending 

YIN ET AL. 

6777 

Water Resources Research 

10.1029/2017WR021959 

|Table 1<br>Summary of th|e Commonly Used|Data Sets in This Pape|r|||
|---|---|---|---|---|---|
|Data|Data type|Spatial resolution|Spatial resolution|Period|Citations|
|GLDAS Prep|Forcing data|0.258|3 hourly|2001–2014|Rodell et al. (2004)|
|ESI|Drought Index|0.058|weekly|2001–2014|Hain et al. (2015)|
|ASCAT|Microwave SM|0.258|daily|2008–2014|Wagner et al. (1999)|
|WindSat|Microwave SM|0.258|daily|2008–2014|Li et al. (2010)|
|SMOS|Microwave SM|0.258|daily|2008–2014|Kerr et al. (2001)|
|SMOPS|Microwave SM|0.258|daily|2008–2014|Yin et al. (2015b)|
|PDSI|Drought Index|2.58|monthly|1985–2014|Dai (2013)|
|SPEI|Drought Index|0.58|monthly|1985–2014|Vicente-Serrano et al. (2010)|



to be anticorrelated, which indicates moisture-limiting vegetation growth conditions (Karnieli et al., 2010). The soil moisture-based BDIs are more sensitive to moisture condition changes. Reduced correlations between USDM and each BDI are observed over parts of the western and eastern US. In southwestern and southeastern US, the moisture changes are driven more by radiation and climate, and thus less tightly coupled with moisture-drought (Anderson et al., 2011). And in northwestern US, the short-term precipitation indices used in the USDM may become desynchronized from land surface moisture conditions, because of the hydrologic delays in snowpack-forming regions (Shukla & Wood, 2008). In comparison with the USDM, the average temporal correlation coefficients for BDI_s and BDI_w are 0.36 and 0.34; while the BDI_b yields the highest correlation (R 5 0.43) in all of the drought estimations. 

Based on 30 year (1985–2014) PDSI means, the correlation coefficients between PDSI standard anomalies and the drought assessments for each of the three BDIs can be found in Figure 4. The sample size for each BDI is 84, because there are 84 months during the 2008–2014 period. The higher correlation coefficients for each BDI are found in the areas where the weather stations are relatively dense, such as in the eastern U.S, Australia and portions of Eurasia (Chen et al., 2002; Mu et al., 2013). The correlation coefficients for BDI_s, BDI_w, and BDI_b in CONUS (238�488N, 21258�–658E) are 0.45, 0.47, and 0.47, respectively, and in Australia (–408�–108N, 1158�1658E) are 0.50, 0.53, and 0.59, respectively. The BDI_b (0.48) also yields the highest correlation coefficient in South Africa (–358�-508N, 2308�1658E) in comparison with the BDI_s (0.42) and BDI_w (0.44). Relative to BDI_s (0.36) and BDI_w (0.38), the BDI_b (0.40) presents successful to increase the correlation in Eurasia (–108�558N, 2208�1758E). In South America (–558�108N, 2908�–308E), the BDI_s (0.35) and BDI_w (0.43) exhibit relatively low correlations with respect to the PDSI standard anomalies, while this situation is significantly improved by the BDI_b (0.48). However, in the areas with weather stations and rain gauges sparsely distributed, the correlations between PDSI and BDIs are relatively low, such as northern Africa and the high latitude areas (Chen et al., 2002; Mu et al., 2013). 

With respect to the monthly 0.5 degree 3 month SPEI standard anomalies (against 1985–2014 averages) during the period 2008–2014 (sample size is 84), the correlation coefficients over global domain for each of 

Table 2 Drought Severity Information in the Original Standardized Scale 

|Categories|NLSM|ESI<br>ASCAT|SMOS|SMOPS|
|---|---|---|---|---|
|D0|0 to20.56|0 to20.81<br>0 to20.58|0 to20.63|0 to20.57|
|D1|20.57 to20.90|20.82 to21.12<br>20.59 to20.84|20.64 to21.00|20.58 to20.85|
|D2|20.91 to21.18|21.13 to21.37<br>20.85 to21.04|21.01 to21.23|20.86 to21.06|
|D3|21.19 to21.48|21.38 to21.67<br>21.05 to21.27|21.23 to21.42|21.07 to21.29|
|D4|21.49 or less|21.68 or less<br>21.27 or less|21.43 or less|21.3 or less|
|Categories|WindS|at<br>BDI_s|BDI_w|BDI_b|
|D0|0 to20.|58<br>0 to20.34|0 to20.31|0 to20.51|
|D1|20.59 to2|0.91<br>20.35 to20.56|20.32 to20.47|20.52 to20.77|
|D2|20.92 to2|1.18<br>20.57 to20.87|20.48 to20.68|20.78 to21.00|
|D3|21.19 to2|1.48<br>20.88 to21.14|20.69 to20.87|21.01 to21.40|
|D4|21.49 or l|ess<br>21.15 or less|20.88 or less|21.41 or less|



YIN ET AL. 

6778 

Water Resources Research 

10.1029/2017WR021959 



Figure 2. Correlation coefficients (R) between USDM and (a) ASCAT, (b) SMOS, (c) WindSat, (d) SMOPS, (e) NLSM, and (f) ESI. The grey color indicates insignificant correlations. 

the three BDIs are exhibited in Figure 5. The higher correlation coefficients for each BDI are shown in CONUS, Europe, Australia, the eastern China and southern South America, where the rain gauges are relatively dense (Chen et al., 2002). The correlation coefficients for BDI_s, BDI_w and BDI_b in CONUS are 0.46, 0.48, and 0.56, respectively, and in Australia are 0.54, 0.58, and 0.59, respectively. Relative to BDI_s (0.33) and BDI_w (0.37), the BDI_b (0.41) presents successful to increase the correlation in Eurasia. The BDI_b (0.40) also yields the highest correlation coefficient in South Africa in comparison with the BDI_s (0.33) and BDI_w (0.37). In South America, the BDI_s (0.27) and BDI_w (0.32) exhibit relatively low correlations with respect to the SPEI standard anomalies, while this situation is improved by the BDI_b (0.37). Similar to Figure 4, the low correlations between SPEI and BDIs can be found in the areas where the weather stations and 

YIN ET AL. 

6779 

Water Resources Research 

10.1029/2017WR021959 



Figure 3. Correlation coefficients (R) between USDM and BDIs over the 2008–2014 period. The gray color indicates insignificant correlations. 

rain gauges are sparsely, such as Amazon basin, northern Africa and the high latitude areas (Chen et al., 2002; Mu et al., 2013). 

#### 5. Evaluation of Drought Events Using BDIs 

BDI performance was also evaluated in relation to reported drought events over the 2009–2014 period (Figure 6). In general, the major annual drought patterns are captured by each BDI product at this coarse time scale. All of the three BDIs can well capture the western Russian drought of 2010 that was very long and intensive, and caused serious damage to the environment and economy (Kogan et al., 2013; Mu et al., 2013) with BDI_s showing a relatively weak signal. And both 2011 Texas drought and the US-Great Plains drought in summer 2012 (Hoerling et al., 2014; Otkin et al., 2015) are reasonably represented by the three BDIs, while major differences are noted in 2012 with BDI_s and BDI_w missing drought signals in the Eastern and Southern U.S. 

According to Australian National Climate Centre (NCC) records (2009a, 2009b), an exceptional drought hit Australia in 2009, which was mitigated by the widespread heavy rainfall throughout northern and central Australia in 2010, while the remaining drought was found in the western Australia (NCC, 2010). Frequent heavy rain events from spring 2010 to autumn 2011, and again in late 2011, lead to Australia’s wettest twoyear period on record, which was heavily influenced by La Nina conditions (NCC, 2012). During 2013, serious~ rainfall deficiencies created significant drought conditions that began to develop again and lasted over 2013–2014 period (NCC, 2013, 2014). These documented dry and wet conditions in Australia over 2009– 2014 period are effectively exhibited by the annual BDIs (Figure 6) with both BDI_s and BDI_w exhibiting slight drought intensity. 

Several other extreme droughts, such as 2010 Amazon drought (Atkinson et al., 2011; Lewis et al., 2011; Xu et al., 2011) and the continuous droughts during 2009–2012 period in East Africa (Lyon & DeWitt, 2012), are all well captured by the BDI_b (Figure 6c). However, BDI_s tends to reduce drought intensity for above 

YIN ET AL. 

6780 

Water Resources Research 

10.1029/2017WR021959 



Figure 4. Correlation coefficients between PDSI standard anomalies (against 1985–2014 averages) and BDIs over 2008–2014 period. The gray color indicates insignificance. 



Figure 5. Correlation coefficients between SPEI standard anomalies (against 1985–2014 averages) and BDIs over 2008–2014 period. The gray color indicates insignificance. 

YIN ET AL. 

6781 

Water Resources Research 

10.1029/2017WR021959 



Figure 6. (a) Annual global terrestrial BDI_s patterns over the 2009–2014 period. The BDI_s ranges from negative (red) to positive (green) values indicating dry to wet conditions. (b) Annual global terrestrial BDI_w patterns over the 2009–2014 period. The BDI_w ranges from negative (red) to positive (green) values indicating dry to wet conditions. (c) Annual global terrestrial BDI_b patterns over the 2009–2014 period. The BDI_b ranges from negative (red) to positive (green) values indicating dry to wet conditions. 

YIN ET AL. 

6782 

Water Resources Research 

10.1029/2017WR021959 

drought episodes and BDI_w cannot reasonably reflect the East Africa drought. In addition, Figure 6c illustrates how the western U.S. experienced abnormally dry conditions during the 2013–2014 period with the most severe conditions in California, which had been experiencing its worst drought in more than a century (AghaKouchak et al., 2015; Cheng et al., 2015); yet both BDI_s and BDI_w basically miss the drought signals for the California drought event [Figures 6a and 6b]. 

The severe drought caused by the great Russian heat wave of 2010 lead to extensive wildfires and thousands of human deaths (Barriopedro et al., 2011). The 2010 western Russia drought started in May and lasted through November with response to the record-breaking high temperature caused by a very strong La Nina~ event (Barriopedro et al., 2011; Kogan et al., 2013; Mu et al., 2013). Both BDI_s and BDI_w show the drought event ends in October 2011 with BDI_s showing lower intensity (Figures 7a and 7b); while the monthly BDI_b results effectively capture the documented droughts in western Russia in 2010 (Figure 7c). 

The 2011 drought over the U.S. Southern Great Plains seriously affected agriculture, severely impacted crop and livestock sectors and significantly influenced food prices at the retail level (Arndt & Blunden, 2012; Grigg, 2014) with the state of Texas experiencing its driest year since 1895 (Combs, 2012; Hoerling et al., 2014). This severe drought started in November 2010 and lasted through October 2011, and the dry situation was mitigated across the southeast Texas Panhandle and eastern Rolling plains in November 2011 by heavy precipitation (Combs, 2012). The BDIs are shown to the capture the evolution of the 2011 U.S drought with BDI_b providing a more reasonable representation of the observed drought conditions in in October and November 2011 [Figure 8]. 

The 2013 drought in New Zealand was one of the most extreme on record for this country. During the period of 2012–2013, the dry conditions were unusually widespread across New Zealand, and particularly serious in the North Island (National Institute of Water and Atmospheric Research, 2013a); which reduced agricultural production and cost the national economy at least US$1.3 billion (Herring et al., 2014). The New Zealand Drought Monitor shows the progression and recession of the drought from October 2012 to May 2013 with the entire New Zealand experiencing the severe drought in March 2013 (National Institute of Water and Atmospheric Research, 2013b). Figures 9a and 9b show both BDI_s and BDI_w cannot correctly capture the situations of 2012–2013 New Zealand drought events; while the BDI_b in Figure 9c perfectly exhibits the drought episodes. 

#### 6. Discussion 

The results shown in sections 4 and 5 indicate that the BDI_b technique, which objectively integrates drought estimations with the lowest TCEM-based RMSEs, can present more robust capability to track drought development with respect to historical records. However, there are several considerations relevant for interpreting these results. The challenges and opportunities are discussed further here associated with integration approaches and drought characteristics. 

##### 6.1. Shallow Sensing Depth of Microwave Soil Moisture 

One issue that must be considered is the shallow sensing depth afforded by the microwave SM products used in this paper. The LSM modeled drought estimates are based on 0–100 cm averages which are much deeper than the top few centimeters sampling depth of the microwave SM-based retrievals. And the ESI represents temporal standardized anomalies in the ratio of actual ET to potential ET (PET), which is also dependent on the root zone SM content related to the rooting depth of the active vegetation (Anderson et al., 2015; Otkin et al., 2015). In fact, using the surface-only microwave remote sensing product over sparsely vegetated areas is consistent with the properties of NLSM and ESI proxy (Yilmaz et al., 2012); and the potential vertical inconsistencies over densely vegetated areas can be effectively resolved at weekly time scales in terms of the strong linear relation between the surface and the vegetation-adjusted soil moisture simulations in Noah land surface model (Albergel et al., 2008; Yilmaz et al., 2012). Although the satellite SM retrievals can only penetrate a few centimeters depth, they represent the fastest response SM dynamics to meteorological anomalies and provide a measure for short-term droughts (Yuan et al., 2015). 

YIN ET AL. 

6783 

Water Resources Research 

10.1029/2017WR021959 



Figure 7. (a) Monthly BDI_s on the subregion (from 408N, 208E to 708N, 808E) domain in 2010. (b) Monthly BDI_w on the subregion (from 408N, 208E to 708N, 808E) domain in 2010. (c) Monthly BDI_b on the subregion (from 408N, 208E to 708N, 808E) domain in 2010. 

YIN ET AL. 

6784 

Water Resources Research 

10.1029/2017WR021959 



Figure 8. (a) Monthly BDI_s on the subregion (from 258N, 21158W to 408N, 2908W) domain in 2011. (b) Monthly BDI_w on the subregion (from 258N, 21158W to 408N, 2908W) domain in 2011. (c) Monthly BDI_b on the subregion (from 258N, 21158W to 408N, 2908W) domain in 2011. 

YIN ET AL. 

6785 

Water Resources Research 

10.1029/2017WR021959 



Figure 9. (a) Monthly BDI_s across the New Zealand domain (from 488S, 1658E to 2338S, 1808E) from August 2012 to July 2013. (b) Monthly BDI_w across the New Zealand domain (from 488S, 1658E to 2338S, 1808E) from August 2012 to July 2013. (c) Monthly BDI_b across the New Zealand domain (from 488S, 1658E to 2338S, 1808E) from August 2012 to July 2013. 

YIN ET AL. 

6786 

Water Resources Research 

10.1029/2017WR021959 

##### 6.2. Uncertainties From Defining the Errors and the Use of Standardized Anomalies 

TCEM has been implemented in previous studies using in situ observations, and it shows a surprisingly robust ability of accurate evaluation on the time series (Draper et al., 2013; Janssen et al., 2007; Miralles et al., 2010; Scipal et al., 2008). The three retrieval sources in this study sufficiently meet the assumption that their errors should be from mutually distinct sources and are not cross-correlated. Prior to the application of TCEM, we transform all the SM time series into standardized anomalies; and their error variances thus are transformed into the same scale, satisfying the assumptions used in the TCEM to quantify the original accuracy for all of the SM retrievals (Miralles et al., 2010; Yilmaz & Crow, 2013; Yilmaz et al., 2012). However, with narrowing our focus to drought assessments in this paper, the information content of the SMbased drought estimates can absolutely reflect the possibility that certain products are of higher quality than others (Miralles et al., 2010). 

##### 6.3. Timescale of Compositing Window and Length of Record 

For this study, composites are generated at 28 day time steps over 4 week moving windows for each of 6 SM retrievals. Across 2011–2014 (SMOS) and 2008–2014 (ASCAT, WindSat and SMOPS) years, the climatologies are based on samples of 112 (28 days 3 4 years) for SMOS and 196 (28 days 3 7 years) for ASCAT, WindSat and SMOPS. Additionally, the SM-based BDIs are also validated against PDSI and SPEI standardized anomalies with respect their 1985–2014 averages that should well capture climatological distributions. The large sample size and the regarded 30 year PDSI and SPEI averages indicate that the results shown in this paper are qualitatively stable and high likely representative of longer period, although the research periods for SMOS and other three MW SM products are 4 year and 7 year, respectively. 

##### 6.4. Errors Specific to Individual MW SM Products 

Microwave remote sensing SM products suffer from the instrument noise and uncertainty in microwave emission modeling, which hampers their use in operational drought monitoring. The ASCAT SM-based drought estimations exhibit higher correlations with the USDM data sets at the regional scale and the PDSI and SPEI products on a global domain in comparison with the passive microwave SM products including WindSat and SMOS. This suggests that the weights of the active SM signals should be increased to enhance the drought monitoring capabilities of the blended products that integrate satellite SM retrievals from multiple single sensors. However, active microwave sensors such as ASCAT, have been shown to have greater uncertainty over high-elevation areas (Wagner et al., 2013), which leads to the modest ASCAT performance (e.g., central Asia). The error propagation for the remotely sensed SM products can be easily tracked in the weighting-based BDI_s and BDI_w data sets with BDI_s being significantly impacted, while this kind of uncertainty is unreasonably identified in BDI_b maps. Using uniform weighting, the BDI_s is determined by the relative importance of each quantity on the average. The improvements related to the use of high quality data and degradations related to data sets with poor retrieval quality have equal opportunities to impact the BDI_s capabilities in monitoring drought events. Although BDI_w is objectively developed according to TCEM RMSE-based weights and the fractions of high (low) quality signals are increased (decreased), the lower weights of drought evaluations that have larger uncertainties can still strongly degrade BDI_w’s performance. Relative to weights-based BDI_s and BDI_w, the BDI_b can merge the drought estimation that has lower uncertainty with ignoring the poor representation of the soil moisture condition. 

##### 6.5. Seasonal Issues 

Drought monitoring and warning studies are generally focused on the drought events occurred during the growing season; however, recent studies have claimed that much more attention should be paid to cold season droughts since their occurrence and intensity are increasing, such as the California drought during November–April winters of 2011/12–2013/14, the 2010–2012 China Southwest drought, and consecutive and worsening winter drought conditions in Nepal during 2000–2009 period (Seager et al., 2015; Wang et al., 2013; Yin et al., 2015a). However, the remotely sensed observations used in drought monitoring are greatly hampered by the frozen soil and low evapotranspiration, which can lead to the poor performance of weights-based BDI_s and BDI_w in cold season with missing the drought signals. This situation can be significantly improved by BDI_b with integrating the drought assessments that can exhibit the lowest TCEM-based RMSE values. The statistical results show that the satellite SM signals assembled into BDI_b are around 12%, 22%, 29%, and 25% in winter (December, January, and February), spring (March, April, and May), summer (June, July, and August), and autumn (September, October, and November), respectively 

YIN ET AL. 

6787 

Water Resources Research 

10.1029/2017WR021959 

with shifting their detection toward North in the warm season (April–September) and toward South during October–March period. 

##### 6.6. Additional Future Works 

##### 6.6.1. Development of Finer Resolution BDI_b 

Microwave satellite sensors have proven to be effective for remotely sensed SM because of the large contrast of dielectric properties between liquid water and dry soil (Njoku & Kong, 1997). However, because of the current limitation of satellite antenna technology, the spatial resolutions of the microwave SM products are generally tens of kilometers. To overcome the coarse spatial scale limitation of relatively accurate microwave SM data, several downscaling algorithms have been proposed in recent literatures (Merlin et al., 2006; Narayan et al, 2006; Parinussa et al, 2014; Peng et al, 2016; Piles et al, 2011; Zhan et al., 2016). Additionally, the land surface temperature can be retrieved from thermal infrared imagery over a broad range of spatiotemporal resolutions from several meters to couple kilometers, which allows developing the finder spatial resolution ESI product on the whole global domain (Anderson et al., 2014). Based on the downscaled satellite SM products and the tens of meters ESI data, the finer spatial resolution BDI_b in drought occurence areas, which can provide much more details for decision makers, is expected to be developed in near future. 

##### 6.6.2. Integrating More Available Drought Evaluations 

We proposed to objectively integrate the SM satellite observations and model simulations based on quantitative evaluations of their uncertainties derived from the TCEM. TCEM requires three data sets with their errors totally independent from each other. This requirement will be met by selecting two independent data sets as anchors and use them to evaluate other data sets that are independent from the two anchor data sets and probably similar to each other. Thus, we will have the general form for equations (2–4): 



where wa1, wa2, and we are the standardized anomalies of the two anchor data sets and the evaluating product, respectively; and l<sup>�</sup> , x<sup>�</sup> , and q<sup>�</sup> are the corresponding unknown errors. With assumption the three kinds of errors are uncorrelated (l<sup>�</sup> q<sup>�</sup> 50; l<sup>�</sup> x<sup>�</sup> 50; q<sup>�</sup> x<sup>�</sup> 50), their RMSE values can be given by 



Specifically, for agricultural drought—the water deficit is the negative soil moisture anomaly that crop could not tolerate (Anderson et al., 2011; Wilhite & Glantz, 1985), the LSM simulations and the thermal infrared/ near-infrared satellite observations-based ESI/Vegetation Health Index (Kogan, 1997) can be used as the anchors. Current existing and upcoming microwave SM products and in situ SM measurements are thus able to be quantitative evaluated, and in turn to be objectively integrated toward the BDI_b. 

In recent years, increased attention has also been paid to the role of previously neglected water source (e.g., irrigation, water storage) processes on the surface energy balance, since traditional soil water balance modeling is only based on vertical water flow and neglecting secondary water source due to processes (Hain et al., 2015; Kumar et al., 2016). Thus, time series data sets of existing meteorological (e.g., satellite precipitation) and hydrological (e.g., satellite irrigation/water storage retrievals) drought monitoring indicators will be scaled to their standard anomalies. Based on quantitative evaluations of the TCEM-based uncertainties, short- and long-term BDI_b products are expected to be further improved with integrating meteorological and hydrological drought assessments, respectively. 

#### 7. Conclusions 

We integrated the commonly used satellite SM products, ALEXI-based ESI and LSM simulations into a subjective BDI_s and two objective BDIs (BDI_w and BDI_b) based on quantitative evaluations of the relative uncertainties of these products derived from a TCEM. Performance of the three BDIs was analyzed in 

YIN ET AL. 

6788 

Water Resources Research 

10.1029/2017WR021959 

comparison with drought monitoring benchmarks and the official drought records. BDI_s using the subjective weighting exhibits modest performance with trending to underestimate drought intensity. Relative to the weighting-based BDI_s and BDI_w, the BDI_b can more reasonably measure drought severity according to intensity and duration, and can provide better capability to identify the onset and end of drought episodes. Over the BDI_s and BDI_w, the BDI_b presents an advantage of higher consistence with the climatological PDSI and SPEI data sets and current operational USDM product. In addition to operational insights, the BDI_b is recommended as an indicator which can merge new upcoming satellite SM products and more available drought evaluations when they can respect to the TCEM assumptions. 

###### Acknowledgments 

This work was supported by a grant from NOAA JPSS Proving Ground and Risk Reduction (PGRR) Program and by a grant from the NASA Applied Sciences Water Resource Program (Award number: NNX12AK90G). SMOPS soil moisture data product could be obtained from NOAA-NESDIS at http://www.ospo.noaa.gov/ Products/land/smops/smops_loops. html. We would like to thank Dr. Aiguo Dai for providing the PDSI data. The 3 month SPEI data can be obtained from: https://climatedataguide.ucar. edu/climate-data/standardized-precipitation-evapotranspiration-index-spei. We are also grateful to the anonymous reviewers for helping significantly improve the quality of the manuscript. 

#### References 

AghaKouchak, A., Feldman, D., Hoerling, M., Huxman, T., & Lund, J. (2015). Recognize anthropogenic drought. Nature, 524 (7566), 409– 4011. https://doi.org/10.1038/524409a 

Albergel, C., Rudiger, C., Pellarin, T., Calvet, J.-C., Fritz, N., Froissard, F., et al. (2008). From near-surface to root-zone soil moisture using an€ exponential filter: An assessment of the method based on in-situ observations and model simulations. Hydrology and Earth System Sciences, 12, 1323–1337. https://doi.org/10.5194/hess-12-1323-2008 

Anderson, M. C., Hain, C., Gao, F., Semmens, K. A., Yang, Y., Schull, M. A., Ring, T., Kustas, W. P., & Alfieri, J. G. (2014). Scaling Surface Fluxes 

from Tower Footprint to Global Model Pixel Scale Using Multi-Satellite Data Fusion, AGU Fall Meeting Abstracts: 2014AGUFM.B52A. 02A Anderson, M. C., Hain, C. R., Wardlow, B. D., Pimstein, A., Mecikalski, J. R., & Kustas, W. P. (2011). Evaluation of drought indices based on thermal remote sensing of evapotranspiration over the continental United States. Journal of Climate, 24, 2025–2044. 

Anderson, M. C., Norman, J. M., Diak, G. R., Kustas, W. P., & Mecikalski, J. R. (1997). A two-source time-integrated model for estimating surface fluxes using thermal infrared remote sensing. Remote Sensing Environment, 60, 195–216. 

Anderson, M. C., Zolin, C. A., Hain, C. R., Semmens, K., Yilmaz, M. T., & Gao, F. (2015). Comparison of satellite-derived LAI and precipitation anomalies over Brazil with a thermal infrared-based Evaporative Stress Index for 2003–2013. Journal of Hydrology, 526, 287–302. 

Arndt, D. S., & Blunden, J. (2012). State of the climate in 2011. Bulletin of the American Meteorological Society, 93, S1–S280. 

Atkinson, P. M., Dash, J., & Jeganathan, C. (2011). Amazon vegetation greenness as measured by satellite sensors over the last decade. Geophysical Research Letters, 38, L19105. https://doi.org/10.1029/2011GL049118 

Azmi, M., Udiger, C. R., & Walker, J. P. (2016). A data fusion-based drought index. Water Resources Research, 52, 2222–2239. https://doi.org/ 10.1002/2015WR017834 

Barriopedro, D., Fischer, E. M., Luterbacher, J., Trigo, R. M., & Garc�ıa-Herrera, R. (2011). The hot summer of 2010: Redrawing the temperature record map of Europe. Science, 332, 220–224. 

Beguer�ıa, S., Vicente-Serrano, S. M., Reig, F., & Latorre, B. (2014). Standardized precipitation evapotranspiration index (SPEI) revisited: Parameter fitting, evapotranspiration models, tools, datasets and drought monitoring. International Journal of Climatology, 34, 3001– 3023. Bolten, J. D., & Crow, W. T. (2012). Improved prediction of quasi-global vegetation conditions using remotely-sensed surface soil moisture. Geophysical Research Letters, 39, L19406. https://doi.org/10.1029/2012GL053470 

Chen, M., Xie, P., Janowiak, J. E., & Arkin, P. A. (2002). Global land precipitation: A 50-yr monthly analysis based on gauge observations. Journal of Hydrometeorology, 3, 249–266. 

Cheng, L., Hoerling, M., AghaKouchak, A., Livneh, B., Quan, X.-W., & Eischeid, J. (2015). How has human-induced climate change affected California drought risk? Journal of Climate, 29(1), 111–120. https://doi.org/10.1175/JCLI-D-15-0260.1 

Combs, S. (2012). The Impact of the 2011 Drought and Beyond. Texas Comptroller of Public Accounts Special Report, Publication 96–1704 [available online at http://www.window.state.tx.us/specialrpt/drought/]. 

Crow, W. T., Kumar, S. V., & Bolten, J. D. (2012). On the utility of land surface models for agricultural drought monitoring. Hydrology and Earth System Sciences Discussions, 9, 5167–5193. 

Crow, W. T., & Wood, E. (2003). The assimilation of remotely sensed soil brightness temperature imagery into a land surface model using ensemble Kalman filtering: A case study based on ESTAR measurements during SGP97. Advances in Water Resources, 26, 137–149. 

Dai, A. (2013). Increasing drought under global warming in observations and models. Nature Climate Change, 3, 52–58. 

Dai, Y., Zeng, X., Dickinson, R. E., Baker, I., Bonan, G. B., Bosilovich, M. G., et al. (2003). The common land model. Bulletin of the American Meteorological Society, 99, https://doi.org/10.1175/BAMS-84-8-1013 

Draper, C., Reichle, R., De Jeu, R., Naeimi, V., Parinussa, R., & Wagner, W. (2013). Estimating root mean square errors in remotely sensed soil moisture over continental scale domains. Remote Sensing of Environment, 137, 288–298. 

Ek, M. B., Mitchell, K. E., Lin, Y., Rogers, E., Grunmann, P., Koren, V., et al. (2003). implementation of Noah land surface model advances in the National Centers for Environmental Prediction operational mesoscale Eta model. Journal of Geophysical Research, 108(D22), 8851. https://doi.org/10.1029/2002JD003296 

Grigg, N. S. (2014). The 2011–2012 drought in the United States: New lessons from a record event. International Journal of Water Resources Development, 30(2), 183–199. 

Hain, C. R., Crow, W. T., Anderson, M. C., & Mecikalski, J. R. (2012). An ensemble Kalman filter dual assimilation of thermal infrared and microwave satellite observations of soil moisture into the Noah land surface model. Water Resources Research, 48, W11517. https://doi. org/10.1029/2011WR011268 

Hain, C. R., Crow, W. T., Anderson, M. C., & Yilmaz, M. T. (2015). Diagnosing neglected soil moisture source–sink processes via a thermal infrared–based two-source energy balance model. Journal of Hydrometeorology, 16, 1070–1086. 

Hao, Z., & AghaKouchak, A. (2013). Multivariate standardized drought index: A parametric multi-index model. Advances in Water Resources, 57, 12–18. 

Hao, Z., Aghakouchak, A., Nakhjiri, N., & Farahmand, A. (2014). Global integrated drought monitoring and prediction system. Scientific Data, 1, 140001. https://doi.org/10.1038/sdata.2014.1 

Hao, Z., Hong, Y., Xia, Y., Singh, V. P., Hao, F., & Cheng, H. (2016). Probabilistic drought characterization in the categorical form using ordinal regression. Journal of Hydrology, 535, 331–339. Heim, R. R., Jr. (2002). A review of twentieth-century drought indices used in the United States. Bulletin of the American Meteorological Society, 83, 1149–1165. 

YIN ET AL. 

6789 

Water Resources Research 

10.1029/2017WR021959 

Herring, S. C., Hoerling, M. P., Peterson, T. C., Stott, P. A. (Eds.). (2014). Explaining extreme events of 2013 from a climate perspective. Bulletin of the American Meteorological Society, 95(9), S1–S96 

Hoerling, M., Eischeid, J., Kumar, A., Leung, R., Mariotti, A., Mo, K., et al. (2014). Causes and Predictability of the 2012 Great Plains Drought. Bulletin of the American Meteorological Society, 95, 269–282. 

Janssen, P., Abdalla, S., Hersbach, H., & Bidlot, J.-R. (2007). Error estimation of buoy, satellite, and model wave height data. Journal of Atmospheric and Oceanic Technology, 24, 1665–1677. 

Kao, S. C., & Govindaraju, R. S. (2010). A copula-based joint deficit index for droughts. Journal of Hydrology, 380(1–2), 121–134. Karnieli, A., Agam, N., Pinker, R. T., Anderson, M. C., Imhoff, M. L., Gutman, G. G., et al. (2010). Use of NDVI and land surface temperature for drought assessment: Merits and limitations. Journal of Climate, 23, 618–633. 

Kerr, Y. H., Waldteufel, P., Wigneron, J.-P., Martinuzzi, J.-M., Font, J., & Berger, M. (2001). Soil moisture retrieval from space: The Soil Moisture and Ocean Salinity (SMOS) Mission. IEEE Transactions on Geoscience and Remote Sensing, 39(8), 1729–1735. 

Keyantash, J. A., & Dracup, J. A. (2004). An aggregate drought index: Assessing drought severity based on fluctuations in the hydrologic cycle and surface water storage. Water Resources Research, 40, W09304. https://doi.org/10.1029/2003WR002610 

Kogan, F. (1997). Global drought watch from space. Bulletin of the American Meteorological Society, 78, 621–636. 

Kogan, F., Adamenko, T., & Guo, W. (2013). Global and regional drought dynamics in the climate warming era. Remote Sensing Letters, 4(4), 364–372. Koster, R. D., Guo, Z., Yang, R., Dirmeyer, P. A., Mitchell, K., & Puma, M. J. (2009). On the nature of soil moisture in land surface models. Journal of Climate, 22, 4322–4325. Koster, R. D., Suarez, M. J., Ducharne, A., Kumar, P., & Stieglitz, M. (2000). A catchmentbased approach to modeling land surface processes in a general circulation model 1. Model structure. Journal of Geophysical Research, 105(D20), 809–822. Kowalczyk, E. A., Wang, Y. P., Law, R. M., et al. (2006). CSIRO Atmosphere Biosphere Land Exchange model for use in climate models and as an offline model. CSIRO Technical Report, 37. 

Kumar, S. V., Reichle, R. H., Koster, R. D., Crow, W. T., & Peters-Lidard, C. D. (2009). Role of subsurface physics in the assimilation of surface soil moisture observations. Journal of Hydrometeorology, 10, 1534–1547. 

Kumar, S. V., Zaitchik, B. F., Peters-Lidard, C. D., Rodell, M., Reichle, R., Li, B., & Jasinski, M. (2016). Assimilation of gridded GRACE terrestrial water storage estimates in the North American Land Data Assimilation System. Journal of Hydrometeorology, 17, 1951–1972. https:// doi.org/10.1175/JHM-D-15–0157 

Lewis, S. L., Brando, P. M., Phillips, O. L., Van der Heijden, G. M. F., & Nepstad, D. (2011). The 2010 Amazon Drought. Science, 331, 554. 

Li, L., Gaiser, P. W., Gao, B.-C., Bevilacqua, R. M., Jackson, T. J., Njoku, E. G., et al. (2010). WindSat global soil moisture retrieval and validation. IEEE Transactions on Geoscience and Remote Sensing, 48(5), 2224–2241. 

Lyon, B., & DeWitt, D. G. (2012). A recent and abrupt decline in the East African long rains. Geophysical Research Letters, 39, L02702. https:// doi.org/10.1029/2011GL050337 

Mazdiyasni, O., & AghaKouchak, A. (2015). Substantial increase in concurrent droughts and heatwaves in the United States. Proceedings of the National Academy of Sciences, 112(37), 11484–11489. McNally, A., Husak, G., Brown, M., Carroll, M., Funk, C., Yatheendradas, S., et al. (2015). Calculating crop water requirement satisfaction in the West Africa Sahel with remotely sensed soil moisture. Journal of Hydrometeorology, 19, https://doi.org/10.1175/JHM-D-14-0049.1 Merlin, O., Chehbouni, G., Kerr, Y., & Goodrich, D. (2006). A downscaling method for distributing surface soil moisture within a microwave pixel: Application to the Monsoon’90 data. Remote Sensing of Environment, 101, 379–389. Miralles, D. G., Crow, W. T., & Cosh, M. H. (2010). Estimating Spatial Sampling Errors in Coarse-Scale Soil Moisture Estimates Derived from Point-Scale Observations. Journal of Hydrometeorology, 11, 1423–1429. 

Mu, Q., Zhao, M., Kimball, J. S., McDowell, N. G., & Running, S. W. (2013). A remotely sensed global terrestrial drought severity index. Bulletin of the American Meteorological Society, 94, 83–98. Naeimi, V., Scipal, K., Bartalis, Z., Hasenauer, S., & Wagner, W. (2009). An improved soil moisture retrieval algorithm for ERS and METOP scatterometer observations. IEEE Transactions on Geoscience and Remote Sensing, 47(7), 1999–2013. Narayan, U., Lakshmi, V., & Jackson, T. H. (2006). High-resolution change estimation of soil moisture using L-band radiometer and radar observations made during the SMEX02 experiments. IEEE Transactions on Geoscience and Remote Sensing, 44, 1545–1554. Vol. National Climate Centre. (2009a). Exceptional winter heat over large parts of Australia. Bureau of Meteorology Special Climate Statement 18: 2–13. National Climate Centre. (2009b). A prolonged spring heatwave over central and south-eastern Australia. Bureau of Meteorology Special Climate Statement 19: 2–17. 

National Climate Centre. (2010). An exceptionally wet Dry Season 2010 in northern and central Australia. Bureau of Meteorology Special Climate Statement 23: 2–6. 

National Climate Centre. (2012). Australia’s wettest two-year period on record; 2010–2011. Bureau of Meteorology Special Climate Statement 38: 2–9. National Climate Centre. (2013). Australia’s warmest September on record. Bureau of Meteorology Special Climate Statement 46: 1–9. National Climate Centre. (2014). Australia’s warmest spring on record. Bureau of Meteorology Special Climate Statement 50: 1–7. National Institute of Water and Atmospheric Research. (2013a). 2012-13 drought: A summary: 1–2 

National Institute of Water and Atmospheric Research (2013b). The 2012-13 drought: An assessment and historical perspective: 6–34 Nearing, G. S., Mocko, D. M., Peters-Lidard, C. D., Kumar, S. V., & Xia, Y. (2016). Benchmarking NLDAS-2 soil moisture and evapotranspiration to separate uncertainty contributions. Journal of Hydrometeorology, 17, 745–759. 

Njoku, E. G., Jackson, T. J., Lakshmi, V., Chan, T. K., & Nghiem, S. V. (2003). Soil moisture retrieval from AMSR-E. IEEE Transactions on Geoscience and Remote Sensing, 41, 215–229. 

Njoku, E. G., & Kong, J.-A. (1997). Theory for passive microwave remote sensing of near surface soil moisture. Journal of Geophysical Research, 82(20), 3109–3118. Oleson, K. W., Dai, Y., Bonan, G. et al. (2004). Technical description of the community land model (CLM). (NCAR Tech. Note NCAR/TN461 1 STR). Boulder, Colorado: National Center for Atmospheric Research. Otkin, J. A., Shafer, M., Svoboda, M., Wardlow, B., Anderson, M. C., Hain, C., & Basara, J. (2015). Facilitating the use of drought early warning information through interactions with agricultural stakeholders. Bulletin of the American Meteorological Society, 96, 1073–1078. Parinussa, R. M., Yilmaz, M. T., Anderson, M. C., Hain, C. R., & de Jeu, R. A. M. (2014). An intercomparison of remotely sensed soil moisture products at various spatial scales over the Iberian Peninsula. Hydrological Processes, 28(18), 4865–4876. Peng, J., Loew, A., Zhang, S., Wang, J., & Niesel, J. (2016). Spatial downscaling of satellite soil moisture data using a vegetation temperature condition index. IEEE Transactions on Geoscience and Remote Sensing, 54, 558–566. 

YIN ET AL. 

6790 

Water Resources Research 

10.1029/2017WR021959 

Piles, M., Camps, A., Vall-Llossera, M., Corbella, I., Panciera, R., Rudiger, C., et al. (2011). Downscaling SMOS derived soil moisture using€ MODIS visible/infrared data. IEEE Transactions on Geoscience and Remote Sensing, 49, 3156–3166. 

Pozzi, W., Sheffield, J, Stefanski, R., Cripe, D., Pulwarty, R., Jurgen, V. V., et al. (2013). Toward global drought early warning capability:€ Expanding international cooperation for the development of a framework for monitoring and forecasting. Bulletin of the American Meteorological Society, 94, 776–785. 

Rajsekhar, D., Singh, V. P., & Mishra, A. K. (2015). Multivariate drought index: An information theory based approach for integrated drought assessment. Journal of Hydrology, 526, 164–182. 

Reichle, R. H., & Koster, R. D. (2004). Bias reduction in short records of satellite soil moisture. Geophysical Research Letters, 31, L19501. https://doi.org/10.1029/2004GL020938 

Scipal, K., Holmes, T., de Jeu, R., Naeimi, V., & Wagner, W. (2008). A possible solution for the problem of estimating the error structure of global soil moisture data sets. Geophysical Research Letters, 35, L24403. https://doi.org/10.1029/2008GL035599 

Seager, R., Hoerling, M., Schubert, S., Wang, H., Lyon, B., Kumar, A., et al. (2015). Causes of the 2011-14 California drought. Journal of Climate, 28, 6997–7024. 

Sheffield, J., Wood, E. F., Chaney, N., Guan, K., Sadri, S., Yuan, X., et al. (2014). A Drought Monitoring and Forecasting System for Sub-Sahara African Water Resources and Food Security. Bulletin of the American Meteorological Society, 95, 861–882. 

Shukla, S., & Wood, A. W. (2008). Use of a standardized runoff index for characterizing hydrologic drought. Geophysical Research Letters, 35, L02405. https://doi.org/10.1029/2007GL032487 

Stoffelen, A. (1998). Toward the true near-surface wind speed: Error modeling and calibration using triple collocation. Journal of Geophysical Research, 123, 7755–7766. 

Svoboda, M., Lecomte, D., Hayes, M., Heim, R., Gleason, K., Angel, J., et al. (2002). The drought monitor. Bulletin of the American Meteorological Society, 83, 1181–1190. 

Tarhule, A., & Lamb, P. J. (2003). Climate research and seasonal forecasting for West Africans: Perceptions, dissemination, and use? Bulletin of the American Meteorological Society, 84, 1741–1759. 

Vicente-Serrano, S. M., Beguer�ıa, S., & Lopez-Moreno, J. I. (2010). A Multiscalar drought index sensitive to global warming: The standardized� precipitation evapotranspiration index. Journal of Climate, 23, 1696–1718. 

Wagner, W., Hahn, S., Kidd, R., Melzer, T., Bartalis, Z., Hasenauer, S., et al. (2013). The ASCAT soil moisture product: A review of its specifications, validation results, and merging applications. Meteorologische Zeitschrift, 22, 5–33. 

Wagner, W., Lemoine, G., & Rott, H. (1999). A method for estimating soil moisture from ERS scatterometer and soil data. Remote Sensing of Environment, 70, 191–207. 

Wang, H., Rogers, J., & Munroe, D. (2015). Commonly used drought indices as indicators of soil moisture in China. Journal of Hydrometeorology, 19, https://doi.org/10.1175/JHM-D-14-0076 

Wang, S.-Y., Yoon, J.-H., Gillies, R. R., & Cho, C. (2013). What caused the winter drought in Western Nepal during recent years. Journal Climate, 26, 8241–8256. 

Wilhite, D. A., & Glantz, M. H. (1985). Understanding the drought phenomenon: The role of definitions. Water International, 10, 111–120. 

Xia, Y., Ek, M. B., Peters-Lidard, C. D., Mocko, D., Svoboda, M., Sheffield, J., & Wood, E. F. (2014). Application of USDM statistics in NLDAS-2: Optimal blended NLDAS drought index over the continental United States. Journal of Geophysical Research: Atmospheres, 119, 2947– 2965. https://doi.org/10.1002/2013JD020994 

Xia, Y., Mitchell, K., Ek, M., Sheffield, J., Cosgrove, B., Wood, E., et al. (2012). Continental-scale water and energy flux analysis and validation for the North American Land Data Assimilation System project phase 2 (NLDAS-2): 1. Intercomparison and application of model products. Journal of Geophysical Research, 117, D03109. https://doi.org/10.1029/2011JD016048 

Xu, L., Samanta, A., Costa, M. H., Ganguly, S., Nemani, R. R., & Myneni, R. B. (2011). Widespread decline in greenness of Amazonian vegetation due to the 2010 drought. Geophysical Research Letters, 38, L07402. https://doi.org/10.1029/2011GL046824 

Yang, R., Cohn, S. E., da Silva, A., Joiner, J., & Houser, P. R. (2003). Tangent linear analysis of the Mosaic land surface model. Journal of Geophysical Research, 108(D2), 4054. https://doi.org/10.1029/2002JD002410 

Yilmaz, M. T., & Crow, W. T. (2013). The optimality of potential rescaling approaches in land data assimilation. Journal of Hydrometeorology, 14, 650–660. https://doi.org/10.1175/JHMD12052.1 

Yilmaz, M. T., Crow, W. T., Anderson, M. C., & Hain, C. (2012). An objective methodology for merging satellite and model-based soil moisture products. Water Resources Research, 48, W11502. https://doi.org/10.1029/2011WR011682 

Yin, J., Zhan, X., Zheng, Y., Hain, C., Ek, M., Wen, J., et al. (2016). Improving Noah Land Surface Model performance using Near Real Time Surface Albedo and Green Vegetation Fraction. Agricultural and Forest Meteorology, 218–219, 171–183. 

Yin, J., Zhan, X., Zheng, Y., Hain, C., Liu, J., & Fang, L. (2015c). Optimal ensemble size of Ensemble Kalman Filter in sequential soil moisture data assimilation of land surface model. Geophysical Research Letters, 16, 6710–6715. https://doi.org/10.1002/2015GL063366 

Yin, J., Zhan, X., Zheng, Y., Liu, J., Fang, L., & Hain, C. R. (2015b). Enhancing model skill by assimilating SMOPS blended soil moisture product into Noah Land Surface Model. Journal of Hydrometerorology, 16(2), 917–931. 

Yin, J., Zhan, X., Zheng, Y., Liu, J., Hain, C. R., & Fang, L. (2014). Impact of quality control of satellite soil moisture data on their assimilation into land surface model. Geophysical Research Letters, 41, 7159–7166. https://doi.org/10.1002/2014GL060659 

Yin, J., Zheng, Y., Zhan, X., Hain, C., Zhai, Q., Duan, C., et al. (2015a). An assessment of impacts of surface type changes on drought monitoring. International Journal of Remote Sensing, 36(24), 6116–6134. 

Yuan, X., Ma, Z., Pan, M., & Shi, C. (2015). Microwave remote sensing of short-term droughts during crop growing seasons. Geophysical Research Letters, 42, 4394–4401. https://doi.org/10.1002/2015GL064125 

Zhan, X., Houser, P. R., Walker, J. P., & Crow, W. (2006). A method for retrieving high resolution soilmoisture from Hydros L-Band radiometer and radar observations. IEEE Transactions on Geoscience and Remote Sensing, 44(k6), 1534–1544. 

Zhan, X., Zheng, Meng, W., Dong, J. J., & Ek, M. (2012). Impact of SMOS soil moisture data assimilation on NCEP-GFS forecasts. Geophysical Research Abstracts, 14: EGU2012–12724-1. 

Zhang, X., Chen, N., Li, J., Chen, Z., & Niyogi, D. (2017). Multi-sensor integrated framework and index for agricultural drought monitoring. Remote Sensing of Environment, 188, 141–163. 

YIN ET AL. 

6791 

