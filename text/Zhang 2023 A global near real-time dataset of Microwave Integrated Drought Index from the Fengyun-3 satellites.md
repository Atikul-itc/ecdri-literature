www.nature.com/scientificdata 



# **oPeN** 

**DaTa DeSCrIPTor** 

**a global near real-time dataset of Microwave Integrated Drought Index from the Fengyun-3 satellites** 

**anzhi Zhang**<sup>**1**</sup> **, Hao Gao**<sup>**2**✉</sup> **, Ronghan Xu**<sup>**2**</sup> **, Xiaoqing Li**<sup>**2**</sup> **, Huichen Zhao**<sup>**1**</sup> **& Gensuo Jia**<sup>**3**✉</sup> 

**Droughts have become more frequent and intense with increasing climate warming, posing widespread risks on ecosystem, agricultural, and water resources, therefore effective and timely drought monitoring is critical to drought assessment, management, and mitigation. Here, we presented a global monthly and ten-day drought dataset of the Fengyun-3 Microwave Integrated Drought Index (FY-3 MIDI) by integrating the inconsistency corrected FY-3B/C/D derived microwave precipitation, soil moisture, and land surface temperature with optimal weights from June 2014 to present. The dataset was evaluated and validated against the Standardized Precipitation Evapotranspiration Index, the Selfcalibrating Palmer Drought Severity Index, and the non-FY MIDI at 0.25°. The FY-3 MIDI can effectively observe drought condition and characteristics as captured by the reference datasets, and it was reliable in monitoring meteorological drought with the ability to work in all-weather condition. Based on the operational Fengyun-3 series satellite, it provided valuable operational service in near real-time on a monthly and ten-day time scale, guaranteeing present and future continuous applications to support global and regional drought monitoring and assessment.** 

## **Background & Summary** 

Drought is a recurring extreme climate event characterized by a prolonged dry spell<sup>1</sup> , and it can cause devastating impacts on regional agriculture, ecosystem, water resources, social economy, and human health<sup>2,3</sup> . Droughts are typically classified into four types including meteorological (precipitation deficit), agricultural (soil moisture deficit), hydrological (runoff, ground water, or water storage deficit), and socioeconomic drought (water supply cannot meet the social demand)<sup>2</sup> . All types of droughts originate from a sustained precipitation deficit, and the meteorological drought often triggers other types of droughts. Climate warming increases atmospheric evaporative demand and likely to lead to an overall drying tendency<sup>4</sup> , and droughts have increased in many regions and are projected to become more frequent, quicker, longer and more intense in a warming future<sup>5–9</sup> . In addition, the water limitation on terrestrial ecosystems is enhancing<sup>10–12</sup> , and the impact of drought on vegetation productivity is increasing over recent decades and under future warming<sup>13,14</sup> . Therefore, near real-time drought monitoring is urgently needed to minimise the adverse impacts of drought and improve the adaptive capacity of natural ecosystems and human-managed environments. 

Satellite observations provide unique capability to monitor the global near real-time drought with improved spatial resolution compared to ground-based observation<sup>15,16</sup> , and various remote sensing drought indices have been proposed to monitor drought from different perspectives based on individual or multiple drought-related variables (precipitation, soil moisture, land surface temperature, evapotranspiration, vegetation index, etc.)<sup>17–21</sup> . The Microwave Integrated Drought Index (MIDI) is a robust and integrated drought monitoring approach through combining of the microwave remote sensing derived precipitation, soil moisture, and land surface temperature, and the MIDI can work in all weather conditions and is reliable in monitoring short-term drought, especially the meteorological drought<sup>15,20,22,23</sup> . The integration approach improves the drought monitoring 

1CAS Key Laboratory of Regional Climate-Environment for Temperate East Asia, Institute of Atmospheric Physics, Chinese Academy of Sciences, Beijing, 100029, China.<sup>2</sup> Key Laboratory of Radiometric Calibration and Validation for Environmental Satellites, National Satellite Meteorological Centre (National Centre for Space Weather)/CMA Innovation Centre for Fengyun Meteorological Satellites (FYSIC), China Meteorological Administration (CMA), Beijing, 100081, China.<sup>3</sup> State Key Laboratory of Earth System Numerical Modeling and Application, Institute of Atmospheric Physics, Chinese Academy of Sciences, Beijing, 100029, China.<sup>✉</sup> e-mail: gaohao@cma.gov.cn; jiong@ tea.ac.cn 

Scientific **Data** | _(2025) 12:583_ | https://doi.org/10.1038/s41597-025-04935-8 

1 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

capability compared to the individual remote sensing drought indices<sup>15,20</sup> . The process of defining combination weights plays a pivotal role in optimizing the reliability of MIDI for drought monitoring. Previously, the empirical weights of MIDI are fixed globally, which were obtained based on regional evaluation<sup>22,23</sup> . However, the data availability and applicability of FY-3 precipitation, soil moisture, and land surface temperature for drought monitoring vary in space, and the fixed combination weights would not fully take advantage of drought monitoring capability of the individual variables and may reduce the application prospects of the MIDI. Therefore, evaluating and determining the contribution weights of PCI, SMCI, and TCI to MIDI in space is a key issue that needs to be addressed. On the other hand, the near real-time global drought monitoring and continuous update services of MIDI are lacking, and the potential capability of drought quick assessments should become operational applications. 

The near real-time global drought monitoring service of MIDI with improved capability in a timely and easily accessible manner is needed to assist the stakeholders and policy makers in decision making and risk management. The Fengyun meteorological satellites have been adopted by the World Meteorological Organization (WMO) for operational meteorological services, and the data are widely used globally<sup>24</sup> . The Microwave Radiation Imager (MWRI) on board the polar-orbit Fengyun-3 series satellites (FY-3B/C/D) provide operational and sustainable updated microwave derived global daily precipitation, soil moisture, and land surface temperature in recent years<sup>25,26</sup> , have the potential to fulfil the MIDI drought monitoring service in near real-time and historical assessment. Moreover, the FY-3 MIDI could be further extended because the FY-3D is still operational, and similar MWRI sensors have been secured for the future (FY-3F/G). However, there is no single FY-3 MWRI sensor that covers the entire period from 2014 and on, and for reliable and consistent drought monitoring, the inconsistency of datasets between FY-3B/C/D should be corrected to minimize the systematic biases in time and space. 

The present study aims to develop the global monthly and ten-day FY-3 MIDI by integrating the FY-3B/C/D MWRI derived precipitation, soil moisture, and land surface temperature at a spatial resolution of 0.25° from June 2014 and on. The FY-3 MIDI development scheme is shown in Fig. 1. We first performed quality control and inter-sensor rescaling to ensure the consistency and continuity of FY-3 MWRI derived global precipitation, soil moisture, and land surface temperature in space and time. Then, the optimal combination weights of FY-3 MIDI were obtained through evaluating the different types of MIDI against the different time scale Standardized Precipitation Evapotranspiration Index (SPEI), a widely used drought index based on gridded data from ground meteorological observations. Finally, the FY-3 MIDI were further validated against drought indices based on remote sensing data and ground meteorological observations, and the FY-3 MIDI dataset at ten-day and monthly time scale were generated from June 2014 and on. This approach allows us to provide a near real-time global drought monitoring service through in orbit operating FY-3D satellite, and intends to provide the opportunity to assess the historical characteristics of droughts and their impact on terrestrial ecosystems in space and time from 2014 onwards. 

## **Methods** 

**Spatial coverage.** The moderate resolution imaging spectroradiometer land cover climate modelling grid version 6.1 (MCD12C1 v061; https://lpdaac.usgs.gov/) data product provides the International GeosphereBiosphere Programme (IGBP) land cover types at a spatial resolution of 0.05°<sup>27</sup> . The data in 2022, the latest available data, was converted to 0.25° using the majority filter within each grid. The study area covered global land with vegetation, including tropical forests (forests over latitudinal band of 23.5° S~23.5° N), extratropical forests, shrublands, savannas, grasslands, and croplands, and other land cover types were excluded from this study. 

**Drought indices based on meteorological data.** The Standardized Precipitation Evapotranspiration Index (SPEI) is based on monthly precipitation and potential evapotranspiration from Climatic Research Unit (CRU) of the University of East Anglia, and it offers long-time, multi-scale character and detailed information of drought conditions since 1901 with a 0.5° spatial resolution<sup>28,29</sup> . The global 1-, 3-, 6-, 9-, and 12-month SPEI dataset (SPEIbase v.2.8<sup>30</sup> , 1901–2021, the latest available version when the study began; the SPEIbase v.2.9<sup>31</sup> , 1901–2022; https://spei.csic.es/database.html), the lower time scales were more suitable to monitor short-term drought, were used to evaluate and validate the drought monitoring capability of MIDI. The Self-calibrating Palmer Drought Severity Index (scPDSI) is calculated from time series of CRU precipitation and temperature, and it provides robust and comparable drought information in space<sup>32</sup> . The scPDSI dataset, spanning the period 1901–2022 with monthly resolution and at a 0.5° spatial resolution (https://crudata.uea.ac.uk/cru/data/drought/) were also used to validate the FY-3 MIDI<sup>33</sup> . The SPEI and scPDSI datasets were further interpolated to 0.25° grid using a nearest-neighbor method. 

**Fengyun-3 satellite data.** The operational global precipitation, soil moisture, and land surface temperature datasets derived from FY-3B/C/D Microwave Radiation Imager (MWRI) were provided by the National Satellite Meteorological Center (NSMC), China Meteorological Administration (CMA) (http://data.nsmc.org.cn), with a spatial resolution of 0.25° at a daily, ten-day, or monthly temporal resolution, and a time span from June 2014 and on (Table 1). The FY-3 MWRI instruments operate at five frequencies of 10.65, 18.7, 23.8, 36.5, and 89 GHz with vertical and horizontal polarization<sup>34,35</sup> . The operational rain rate retrieval algorithms from MWRI include two steps: rain screening and quantitative retrieval. The FY-3B algorithm relies on statistical formulations for retrieval, while the FY-3C/3D algorithm employ a Bayesian retrieval framework. Both of them exploit the full spectral range of MWRI from 10.65 GHz to 89 GHz, except for the 23.8 GHz horizontal polarization channel. The relative error is less than 25% as validated against ground-based rain gauges and spaceborne precipitation measurement radars<sup>34,36,37</sup> . The soil moisture is retrieved from 10.65 GHz vertical and horizontal brightness temperature based on a parameterized surface emission model, the Qp model<sup>38</sup> , and the root mean square error is 

Scientific **Data** | _(2025) 12:583_ | https://doi.org/10.1038/s41597-025-04935-8 

2 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



**Fig. 1** Flow chart for generating the Microwave Integrated Drought Index based on Fengyun-3 satellites derived precipitation, soil moisture, and land surface temperature (FY-3 MIDI). 

within 0.06 cm<sup>3</sup> cm<sup>−3</sup> in the medium to low vegetation cover areas<sup>25</sup> . The retrieval of land surface temperature is implemented through a multi-channel linear regression approach<sup>39</sup> , utilizing dual-polarized brightness temperature from four microwave frequencies (18.7, 23.8, 36.5, and 89 GHz). The regression coefficients are calibrated against infrared-based land surface temperature, and the average temperature bias is about 3.5–4.5 K in moderately to densely vegetated areas. 

The products had been validated and showed comparable quality with similar satellite sensor observations<sup>25,26,34</sup> . We performed data quality control, geolocation of the swath to the grid, and reprojection of the EASE-GRID to the geographic grid (Fig. 1). The average values of the ascending and descending data at a 

Scientific **Data** | _(2025) 12:583_ | https://doi.org/10.1038/s41597-025-04935-8 

3 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

||**FY-3B**|**FY-3C**|**FY-3D**|
|---|---|---|---|
||Daily swath:|Dail swath: 20150205-20200131|Daily grid (lat, lon): 20190501~|
|Precipitation|20140601-20190531|y|Monthly grid (lat, lon): 20190531~|
||/|Daily grid (EASE-GRID): 20140601-20200203|Daily grid (lat, lon): 20180712~|
||/|10-day grid (EASE-GRID): 20140610-20200131|10-day grid (lat, lon): 20180720~|
|Soil moisture|/|Monthly grid (EASE-GRID): 20140630-20200131|Monthly grid (lat, lon): 20180731~|
||/|Daily grid (EASE-GRID): 20140601-20200131|Daily grid (EASE-GRID): 20191101~|
|Land surface temerature|/|10-day grid (EASE-GRID): 20140610-20200131|10-day grid (EASE-GRID): 20191110~|
|p|/|Monthly grid (EASE-GRID): 20140630-20200131|Monthly grid (EASE-GRID): 20191130~|



**Table 1.** Details of the Fengyun-3B/C/D derived precipitation, soil moisture, and land surface temperature datasets used in the study. 



**Fig. 2** Temporal coverages of Fengyun-3B/C/D derived precipitation, soil moisture, and land surface temperature from 2014 to 2023 ( **a** ). An example of the rescaling of the monthly FY-3C and FY-3D land surface temperature ( **b** ). The FY-3C rescaled (purple line) and FY-3D (wine line) were shaded by the merged signal (olive line) except for the overlap period. 

daily, ten-day, and monthly time scale were further calculated based on the data obtained from the web portal. Furthermore, the alternative datasets of the ten-day and monthly averages were calculated from the daily files of the previous step and were used when the ten-day and monthly values from the web portal were not available. The MWRI derived precipitation, soil moisture, and land surface temperature datasets from June 2014 to July 2023 were used to develop, validate, and evaluate the FY-3 MIDI. And the near real-time drought monitoring service of FY-3 MIDI was calculated based on data from June 2014 to the most recent data available. 

**Fengyun-3B/C/D data rescale and merge.** To ensure consistency of the MWRI derived precipitation, soil moisture, and land surface temperature data from FY-3B/C/D, the data between sensors were rescaled and merged for each grid cell. The rescaling and merging approach were similar to method used by previous researches, which was robust to both the trends and sudden changes<sup>40</sup> . In this study, the FY-3B/C data have been rescaled against those of FY-3D, as the FY-3D is still in orbit, thus ensuring the near real-time drought monitoring service based on the operational FY-3D data. The overlap period for precipitation, soil moisture, and land surface temperature between FY-3C and FY-3D was 9, 19, and 3 months, respectively (Fig. 2a), hence, the mean and standardized deviation of the relatively shorter overlap period were not be sufficiently representative of the full signal range of FY-3C and FY-3D. Therefore, the mean and standardized deviation of the whole period of FY-3C and FY-3D were employed in this study, which was different from the initially proposed overlap period. 

Taken the detailed procedure of rescaling and merging of monthly land surface temperature between FY-3C and FY-3D for example (Fig. 2b). The FY-3C data were firstly rescaled followed the equation pixel by pixel: 



where the 3 _C_ rescaled<sup>and</sup> 3<sup>_C_</sup> original<sup>were the rescaled and original monthly FY-3C land surface temperature data,</sup> and 3 _C_ mean<sup>and</sup> 3<sup>_C_</sup> SD<sup>referred to the mean and standardized derivation of land surface temperature for the whole</sup> period of FY-3C (June 2014 to January 2020). Similarly, 3 _D_ mean<sup>and</sup> 3<sup>_D_</sup> SD<sup>referred to the mean and standardized</sup> derivation of land surface temperature for the whole period of FY-3D (November 2019 to July 2023). Secondly, we averaged the rescaled FY-3C and original FY-3D monthly values to obtain a merged FY-3 land surface temperature dataset from June 2014. The merged data demonstrated a high degree of continuity and consistency, providing a reliable dataset for long-term drought monitoring (Fig. 2b). For precipitation, the FY-3C data was firstly rescaled against the FY-3D, and the FY-3B time series were further rescaled against the rescaled FY-3C data, finally the merged dataset was the averages of rescaled FY-3B (June 2014 to January 2015), rescaled FY-3C (February 2015 to January 2020), and original FY-3D (May 2019 to July 2023). Consequently, the ten-day and 

Scientific **Data** | _(2025) 12:583_ | https://doi.org/10.1038/s41597-025-04935-8 

4 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

|**Drought Indices**|**Formula**|
|---|---|
|PCI|(Pi−Pmin)/(Pmax−Pmin)|
|SMCI|(SMi−SMmin)/(SMmax−SMmin)|
|TCI|(LSTmax−LSTi)/(LSTmax−LSTmin)|
|MIDI_XX0|_α_ ×PCI+ _β_ ×SMCI|
|MIDI_X0X|_α_ ×PCI+ _β_ ×TCI|
|MIDI_0XX|_α_ ×SMCI+ _β_ ×TCI|
|MIDI_XXX|_α_ ×PCI+ _β_ ×SMCI+(1−_α_−_β_)×TCI|



**Table 2.** Descriptions of remote sensing drought indices. Four types of weight constitutions (α and β) were used to calculate the Microwave Integrated Drought Index (MIDI). 

monthly merged datasets of FY-3 MWRI precipitation, soil moisture, and land surface temperature were obtained to develop the FY-3 MIDI. 

**optimization of the FY-3 Microwave Integrated Drought Index (FY-3 MIDI).** The optimization of the combination weights is an important factor to improving the MIDI’s drought monitoring capability. For determination of the combination weights of multiple variables integrated drought index, several methods, such as the empirical weights<sup>19,20</sup> , the Principal Component Analysis (PCA)<sup>41</sup> , and the constrained optimization<sup>42,43</sup> , have been proposed and effectively used in previous studies. The constrained optimization method is employed to optimize the weights of individual remote sensing variables when they are combined, with the process of optimization being constrained by the maximization of their correlations with meteorological drought indices<sup>42,43</sup> . The constrained optimization method ensures the attainment of the optimal weights in a flexible manner for different combinations of FY-3 MIDI. Furthermore, it fully takes the advantage of the FY-derived precipitation, soil moisture, and land surface temperature pixel-by-pixel for drought monitoring owing to their availability, reliability, and applicability. Here, to further improve the drought monitoring reliability and applicability of the FY-3 MIDI, the optimal weights on a grid-by-grid basis were determined through the utilisation of the constrained optimization method<sup>42,43</sup> . Consequently, the global monthly and ten-day datasets of FY-3 MIDI were established using the following steps: 

_Calculation of the FY-3 MIDI._ The Precipitation Condition Index (PCI), the Soil Moisture Condition Index (SMCI), and the Temperature Condition Index (TCI) were linearly scaled from 0 to 1 pixel by pixel based on the absolute maximum and minimum values of the same month (ten-day) for FY-3 MWRI derived precipitation, soil moisture, and land surface temperature respectively from June 2014 to July 2023 (Table 2)<sup>20,23</sup> . Then, monthly datasets of four MIDI types were obtained based on varied weights (Fig. 1 and Table 2). For the two variable constituted MIDI_XX0 (precipitation and soil moisture), MIDI_X0X (precipitation and land surface temperature), and MIDI_0XX (soil moisture and land surface temperature), the parameter _α_ or _β_ was set to vary in step of 0.1, starting from 0.3 and increasing to 0.7 (Table 3). The MIDI_XXX integrates three variables, and the weights of _α_ and _β_ varied from 0.3 to 0.5 and 0.2 to 0.5 respectively (Table 3). The sets of weights ensured the integrated measure of droughts and avoided the overdependence of individual variables, that should be considered in composite drought monitoring<sup>15,44</sup> . 

_Optimization of the FY-3 MIDI weights pixel by pixel._ The correlation coefficients (R) were firstly calculated between the monthly remote sensing drought indices (DIRS: PCI, SMCI, TCI, MIDI_XX0, MIDI_X0X, MIDI_0XX, and MIDI_XXX) and the 1-, 3-, 6-, 9-, 12-month SPEI from February 2015 to December 2021 (the overlapping period of the FY-3C/D MIDI and SPEI v.2.8) pixel by pixel, and the maximum correlations for each type of DIRS (seven in total) were further estimated in space (Fig. 3). Then, the optimal weights for each type of DIRS ( _weightR_Typeoptimal_ ) were selected as the combinations that hold the maximum correlation ( _weightMax R_ ( _DIRS_ , _weight_ , _SPEI_ )) pixel by pixel (Fig. 1): 



Furthermore, the spatial patterns of the overall maximum correlations were obtained as the highest correlation of all seven types of DIRS (Fig. 4a), and the overall optimal weights for MIDI ( _weightR_Maxoptimal_ ) were derived according to the overall maximum correlations occupied combinations ( _weight Overall Max R_ ( _DIRS_ , _weight_ , _SPEI_ )) for each pixel (Fig. 5): 



_Production of the optimal MIDI._ After obtaining the overall optimal weights, we built times series of the FY-3 MIDI rasters (R_Max) with the overall optimal weights ( _weightR_Maxoptimal_ ) at both monthly and ten-day time steps, that were considered as a first choice of the optimal MIDI product. However, the PCI, SMCI, and TCI were not consistently available for generation of the optimal MIDI rasters (R_Max). Consequently, the alternate MIDI rasters (R_Type) were also produced based on the data availability of PCI, SMCI, and TCI as well as the optimal 

Scientific **Data** | _(2025) 12:583_ | https://doi.org/10.1038/s41597-025-04935-8 

5 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

||**Weigh**|**ts**||**Mean co**|**rrelations**|||||
|---|---|---|---|---|---|---|---|---|---|
|**Indices**|**PCI**|**SMCI**|**TCI**|**R_Max**|**SPEI-1**|**SPEI-3**|**SPEI-6**|**SPEI-9**|**SPEI-12**|
|PCI|1|||0.248|0.200|0.109|0.089|0.078|0.066|
|SMCI||1||**0.322**|0.258|0.206|0.162|0.125|0.100|
|TCI|||1|0.286|0.211|0.171|0.144|0.131|0.121|
||0.3|0.7||**0.386**|0.332|0.244|0.194|0.162|0.129|
||0.4|0.6||0.381|0.332|0.238|0.189|0.158|0.127|
|MIDI_XX0|0.5|0.5||0.369|0.324|0.224|0.179|0.150|0.122|
||0.6|0.4||0.352|0.310|0.207|0.166|0.139|0.114|
||0.7|0.3||0.334|0.293|0.188|0.151|0.127|0.105|
||0.3||0.7|**0.362**|0.310|0.229|0.186|0.169|0.151|
||0.4||0.6|0.360|0.312|0.224|0.182|0.164|0.146|
|MIDI_X0X|0.5||0.5|0.352|0.307|0.212|0.173|0.155|0.137|
||0.6||0.4|0.338|0.294|0.197|0.160|0.143|0.126|
||0.7||0.3|0.322|0.279|0.180|0.146|0.129|0.114|
|||0.3|0.7|0.352|0.289|0.237|0.194|0.171|0.151|
|||0.4|0.6|0.366|0.304|0.250|0.204|0.177|0.154|
|MIDI_0XX||0.5|0.5|0.376|0.314|0.259|0.211|0.180|0.154|
|||0.6|0.4|**0.380**|0.315|0.261|0.212|0.178|0.151|
|||0.7|0.3|0.378|0.310|0.257|0.208|0.172|0.143|
||0.3|0.3|0.4|0.430|0.389|0.288|0.231|0.203|0.174|
||0.3|0.4|0.3|**0.434**|0.391|0.290|0.232|0.201|0.169|
||0.3|0.5|0.2|0.428|0.382|0.282|0.226|0.193|0.160|
||0.4|0.3|0.3|0.418|0.379|0.272|0.219|0.190|0.162|
|MIDI_XXX|0.4|0.4|0.2|0.416|0.375|0.269|0.216|0.185|0.155|
||0.4|0.5|0.1|0.406|0.361|0.259|0.207|0.175|0.143|
||0.5|0.2|0.3|0.395|0.357|0.248|0.199|0.171|0.145|
||0.5|0.3|0.2|0.389|0.348|0.241|0.193|0.164|0.136|
||0.5|0.4|0.1|0.392|0.354|0.247|0.199|0.174|0.150|



**Table 3.** Correlation coefficients between 1- to 12-month SPEI and different FY-3 MIDI combinations. The maximum correlations between 1- to 12-month SPEI and different MIDI combinations were referred as R_max. The highest correlations of individual drought index or different MIDI combinations were indicated in bold. 

weights ( _weightR_Typeoptimal_ ) for each type of DIRS. Ultimately, the global monthly and ten-day optimal MIDI datasets, that covered the maximum spatial extent, were produced as a combinations of the R_Max and R_Type rasters. The valid values of the MIDI R_Max rasters were the primary component, while the pixel values of MIDI R_Type were incorporated when those of the former was invalid (Fig. 1). 

Finally, the FY-3 MIDI was produced by the integrating the FY-3 MWRI derived PCI, SMCI, and TCI with optimal weights. The FY-3 MIDI was dimensionless. Its values ranged from 0 to 1, with lower values corresponding to more severe levels of drought. Drought conditions were categorized into four classes, the extreme (0.05 and less), severe (0.06 to 0.15), moderate (0.16 to 0.25), and mild (0.26 to 0.35) drought (Table 4). 

**The non-FY-3 Microwave Integrated Drought Index (non-FY-3 MIDI).** The monthly non-FY-3 MIDI dataset from June 2014 to July 2023 were calculated based on the widely used Global Precipitation Measurement Integrated Multi-satellitE Retrievals for GPM precipitation (GPM_3IMERGM 07, https://disc.gsfc. nasa.gov/)<sup>45</sup> , the European Space Agency Climate Change Initiative active and passive microwave combined soil moisture (ESA CCI SM v09.1, https://climate.esa.int/en/)<sup>46,47</sup> , and the Land Parameter Retrieval Model land surface temperature from the Advanced Microwave Scanning Radiometer 2 (LPRM_AMSR2_SOILM3 v001, https:// disc.gsfc.nasa.gov/)<sup>48–50</sup> at a spatial resolution of 0.25° followed previous work<sup>22</sup> . 

**Statistical methods.** The correlation coefficients (R) were calculated between the monthly FY-3 MIDI and the different time scale SPEI (1-, 3-, 6-, 9-, 12-month), scPDSI, and non-FY-3 MIDI using the Spearman correlation analysis, which measures the monotonic relationship between variables based on ranks<sup>51</sup> . The Theil-Sen (TS) method was used to estimate the linear trends of different drought indices, which is robust in trend detection and insensitive to outliers<sup>52,53</sup> , and a nonparametric Mann-Kendall approach was used to test the significance of trend<sup>54,55</sup> . A _p_ -value of 0.05 was used to test the significance for both the correlation and trend. 

**evaluation and validation of the FY-3 MIDI.** The FY-3 MIDI were evaluated by comparing the results of monthly values with that of SPEI, scPDSI, and non-FY-3 MIDI. The Spearman’s rank correlations between monthly FY-3 MIDI and different time scale SPEI (1-, 3-, 6-, 9-, 12-month, SPEIbase v.2.8), scPDSI, and non-FY-3 MIDI were evaluated in space (Figs. 3, 4, 6). The drought spatiotemporal distributions (Fig. 7), drought area 

6 

Scientific **Data** | _(2025) 12:583_ | https://doi.org/10.1038/s41597-025-04935-8 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

|**Category**|**MIDI**|**SPEI**|**scPDSI**|
|---|---|---|---|
|Extreme drought|0.05 and less|−2 and less|−4 and less|
|Severe drought|0.06 to 0.15|−1.5 to−1.99|−3 to−3.99|
|Moderate drought|0.16 to 0.25|−1 to−1.49|−2 to−2.99|
|Mild drought|0.26 to 0.35|−0.5 to−0.99|−1 to−1.99|
|None|0.36 and above|−0.49 and above|−0.99 and above|



**Table 4.** Drought categories based on different drought indices. 

(Fig. 8), and drought trend of FY-3 MIDI (Fig. 9) were validated against that of the SPEI (SPEIbase v.2.9), scPDSI, and non-FY-3 MIDI. 

## **Data Records** 

The historical global monthly and ten-day FY-3 MIDI products from June 2014 to December 2024 are freely available at the Science Data Bank (https://doi.org/10.57760/sciencedb.17942)<sup>56</sup> . The data projection is GCS_ WGS_1984, and these data are at a spatial resolution of 0.25° in GeoTIFF format. For monthly data, each file is named as “FY-3_MIDI_MONTH_yyyymmdd.tif”; while for the ten-day data, each file is named as “FY-3_ MIDI_10DAY_yyyymmdd.tif”. Where, “yyyy” represents the year, “mm” stands for the month, and “dd” represents the day, respectively. The FY-3 MIDI data is comprised of two bands: the first band contains the MIDI value data, and the second band contains the MIDI corresponding combination type flag. The corresponding combination weights can be found in code files. 

## **technical Validation** 

**evaluation and validation of the FY-3 MIDI against different time scale SPeI.** To evaluate the performance of FY-3 MIDI, the maximum correlation coefficients between PCI, SMCI, TCI, different types of MIDI and the 1-, 3-, 6-, 9-, 12-month SPEI were obtained in space (Fig. 3) and for each type of constitution (Table 3). The correlations between remote sensing drought indices and SPEI were highest with 1-month SPEI, with a subsequent decrease in correlation as the time scale of SPEI increased (Table 3), suggesting that the MIDI were more suitable in monitoring the meteorological drought globally, in accordance with the findings of previous studies<sup>20,23</sup> . Regarding the individual drought indices, the SMCI exhibited the highest correlation, followed by the TCI and PCI (Fig. 3a–c). The maximum correlations showed similar distribution patterns in space (Fig. 3), with the MIDI_XXX having the highest spatial mean correlation (0.474), followed by the MIDI_XX0 (0.421), MIDI_0XX (0.420), and MIDI_X0X (0.399). Furthermore, the different types of MIDI exhibited superior performance (higher correlations) compared to individual drought indices (Fig. 3), thereby demonstrating a remarkably enhanced drought monitoring capability of the FY-3 MIDI through the integration of multiple variables<sup>15</sup> . The overall maximum correlations demonstrated the robustness of FY-3 MIDI in monitoring global droughts (Fig. 4). It revealed that approximately 47.1% of the pixels exhibited strong positive correlations (R > 0.5), occupying the majority part of North America, Eurasia, southeastern South America, Australia, and north and southeast Africa. In the meantime, relatively weaker correlations were primarily concentrated in the tropical and Arctic regions (Fig. 4a). The highest mean correlation was found for croplands (0.56), followed by grasslands (0.51), extratropical forests (0.49), shrublands (0.45), savannas (0.44), and tropical forests (0.34). From perspective of latitudinal distribution, the results indicated higher correlations over middle latitudes with a decrease towards both the poles and the equator for the globe and all vegetation biomes (Fig. 4c). The optimal combination weights for constituting MIDI, maximising the drought monitoring capability of individual drought indices, were obtained based on the overall maximum correlations, and the PCI, SMCI, and TCI showed distinct and complementary spatial distributions (Fig. 5). The percentages with the greatest weight for PCI, SMCI, and TCI were 20.6%, 39.5%, and 39.9% in space, respectively, which suggested that the FY-3 derived soil moisture and land surface temperature played a more important role than the precipitation in constituting the MIDI. The PCI showed higher weights over tropical forests covered regions, southeast United States, central Siberia, and eastern Siberia (Fig. 5a). In contrast, the SMCI exhibited greater weights across large parts of north America, southern South America, Europe, majority of Asia, and Australia (Fig. 5b). Furthermore, the TCI was the key factor in the Arctic, Africa, and northern and central South America (Fig. 5c). Demonstrating a latitudinal pattern, whereby the SMCI exerted dominance over middle latitudes, the TCI over high latitudes, and PCI and TCI in concert over tropics (Fig. 5d–f). 

**Validation the FY-3 MIDI with scPDSI and non-FY-3 MIDI.** To further validate the FY-3 MIDI, alternative drought indices were employed, namely the remotely sensed non-FY-3 MIDI and the ground observation-based scPDSI. The spatial and latitudinal distributions of correlations between non-FY-3 MIDI, scPDSI, and FY-3 MIDI were obtained (Fig. 6). In general, the correlations exhibited comparable patterns to those observed between FY-3 MIDI and SPEI in space and by latitude, showing higher correlations in middle latitudes and lower correlations in high and lower latitudes (Figs. 4, 6). The FY-3 MIDI exhibited a markedly stronger correlation with the non-FY-3 MIDI than with scPDSI, with the R values approaching those between FY-3 MIDI and SPEI. This finding showed the reliability of FY-3 MIDI in monitoring drought, particularly in comparison with the non-FY-3 MIDI derived from the state-of-art global datasets. The discrepancies in correlation values were also found to be highly related to the suitability of drought indices for monitoring short-term or long-term drought. The MIDI was proved to be more reliable in monitoring the short-term drought<sup>15,23</sup> , whereas the scPDSI 

Scientific **Data** | _(2025) 12:583_ | https://doi.org/10.1038/s41597-025-04935-8 

7 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



**Fig. 3** Spatial patterns of maximum correlation between 1- to 12-month SPEI and different FY-3 MIDI combinations. The mean correlation coefficients were shown in parentheses. 

was found to be more suitable for monitoring the long-term drought<sup>33,57</sup> . The results demonstrated that the FY-3 MIDI were reliable in monitoring the short-term drought, especially the meteorological drought. 

**Comparison of the spatial-temporal patterns of drought characteristics.** The spatial-temporal patterns of global drought were compared between the FY-MIDI, non-FY-3 MIDI, SPEI, and scPDSI for July from 2016 to 2021 as an example (Fig. 7). We found an overall favorable agreement between global drought patterns of the FY-3 MIDI and the reference datasets, and the FY-3 MIDI presented a higher consistency with the non-FY-3 MIDI, followed with that of 1-month SPEI and the scPDSI. In general, the FY-3 MIDI was able to observe similar drought patterns in space and time over the North America, Europe, Asia, and Australia when compared to the other reference drought indices. It was found that severe droughts occurred in South America from 2016 to 2018, as indicated by the non-FY-3 MIDI, SPEI and scPDSI; however, limited drought affected area was identified by the FY-3 MIDI. Conversely, all indices captured similar drought patterns during 2020 and 2021. Furthermore, relatively large differences were found between drought indices in Africa. The discrepancy in the detection of severe drought between different drought datasets around 2016 over tropical South America and Africa might be due to the sparse coverage of ground weather stations, the higher uncertainties in satellite precipitation retrievals, and the availability and applicability of FY-3-derived precipitation, soil moisture, and land surface temperature over these regions<sup>25,58,59</sup> . 

The changes in the extent of drought were compared for July between different drought indices from 2014 to 2023, and the FY-3 MIDI demonstrated a high degree of consistency in terms of both temporal variations and magnitude when compared to the other drought indices (Fig. 8). The global area affected by drought (the sum of mild, moderate, severe, and extreme droughts) fluctuated around 39%, and the values were the lowest in 2016, and it increased gradually over time, reaching a peak in 2021. During this period, droughts were widespread in the south hemisphere and high latitude north hemisphere (Fig. 7). From 2022 and on, the drought area decreased. 

The comparison of the global drought trend from 2014 to 2022 revealed spatial heterogeneity, with similar proportions of wetting and drying (approximately 50%) (Fig. 9). The results indicated a significant and common wetting trend in the South Asia, Southeast Russia, eastern Mongolia, and northeast China. Additionally, a consistent drying trend was observed over central United States, Central Asia, and the southwestern part of South 

8 

Scientific **Data** | _(2025) 12:583_ | https://doi.org/10.1038/s41597-025-04935-8 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



**Fig. 4** The distributions of overall maximum correlation between 1- to 12-month SPEI and different FY-3 MIDI combinations in space ( **a** ), by biome ( **b** ), and by latitude ( **c** ). The color boxes or lines represented different vegetation biomes. The blue dots in ( **b** ) were the mean correlation coefficients for each biome. 



**Fig. 5** The spatial and latitudinal patterns of the optimal combination weights of PCI, SMCI, and TCI for constituting FY-3 MIDI. 

America. The wetting trend of MIDI exhibited a larger extent in north Africa than that of SPEI and scPDSI. Furthermore, the larger areas with wetting trends over northeast South America, as evidenced by other drought indices, were not observed in the FY-3 MIDI. The scPDSI presented a greater number of areas exhibiting a 

Scientific **Data** | _(2025) 12:583_ | https://doi.org/10.1038/s41597-025-04935-8 

9 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



**Fig. 6** The spatial and latitudinal distributions of correlations between the non-FY-3 MIDI, scPDSI, and FY-3 MIDI. 



**Fig. 7** The spatial-temporal changes of drought detected by the FY-3 MIDI ( **a** – **f** ), non-FY-3 MIDI ( **g** – **i)** , 1-month SPEI ( **m** – **r** ), and scPDSI ( **s** – **x** ) in July from 2016 to 2021. The drought category classifications of each drought index were indicated above the corresponding legend. 

significant trend (scPDSI: 69.3%, FY-3 MIDI: 24%, non-FY-3 MIDI: 29.6%, SPEI: 21.7%), reflecting of its intrinsic capability for monitoring long-term drought with a smoother time series and a clearer trend. 

## **Usage Notes** 

Drought indices and datasets were fundamental to detect and assess the spatial-temporal distributions and change patterns of drought. The FY-3 MIDI provided a reliable tool to monitoring the global meteorological drought by integrating the microwave derived precipitation, soil moisture, and land surface temperature from the operational Fengyun-3 satellites in an optimal manner. The global monthly and ten-day drought dataset spanned from June 2014 to present at a spatial resolution of 0.25°. The historic data could be employed 

Scientific **Data** | _(2025) 12:583_ | https://doi.org/10.1038/s41597-025-04935-8 

10 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



**Fig. 8** Temporal variation of drought area monitored by different drought indices for July from 2014 to 2023. 



**Fig. 9** Comparison in spatial patterns of linear trend for the FY-3 MIDI ( **a** ), non-FY-3 MIDI ( **b** ), 1-month SPEI ( **c** ), and scPDSI ( **d** ) from 2014 to 2022. 

to evaluate the characteristics and change associated with drought, as well as the impact of drought on vegetation growth, carbon uptake, agricultural production, and water resources at the regional and global levels. Furthermore, the near real-time data provided by the FY-3 MIDI, based on operational satellites, fulfilled the primary requirement for the most recent drought monitoring service. This has effectively transformed the potential capability of satellite remote sensing for drought monitoring into a practically operational application, and it can provide valuable information for drought quick assessments. 

The data generated by this work was freely accessible from the aforementioned repository. The dataset will be updated regularly in accordance with the availability of operational FY-3 MWRI precipitation, soil moisture, and land surface temperature data. The near real-time monthly and ten-day MIDI products can be accessed from web service under drought of disaster events section (http://fyearth.nsmc.org.cn/area/global/weather). Owing to the lack of reliable input data, the FY-3 MIDI values were not available for some areas in the middle to high latitudes during cold season. A median filter is suggested to eliminate the spatially sporadic noise in order to obtain a better visual clarity of the results in space. 

The data can be used to assess the distribution and evolution of droughts; however, it should be noted that the FY-3 MIDI may still include uncertainties due to data availability, data quality, inconsistency between sensors, short record of length, and the spatial differentiation of drought monitoring capability. It was not possible for FY-3 MIDI to be entirely consistent with other drought indices, as drought indices were based on different datasets and methods, and represented various aspects of drought, given the complex nature of this phenomenon<sup>1,15</sup> . The favorable agreement between the spatial-temporal patterns of drought characteristics for FY-3 MIDI and the reference datasets provided the confidence that the FY-3 MIDI was an effective tool for monitoring and assessing the distribution and evolution of droughts on a finer scale in near real-time. The different drought indices have advantages and limitations, and the comprehensive drought information should be based 

Scientific **Data** | _(2025) 12:583_ | https://doi.org/10.1038/s41597-025-04935-8 

11 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

on multiple sources<sup>8,15,60,61</sup> . The FY-3 MIDI proved to be a valuable tool for the remote sensing of meteorological drought conditions, providing information in near real-time that was beneficial for decision-making and disaster prevention. By integrating this data with other sources of drought information, it was possible to enhance understanding of drought characteristics and to improve the assessment of drought situations. 

## **Code availability** 

All calculations of the global FY-3 MIDI products were based on the Interactive Data Language (IDL), and the codes and files of optimal weights are available at GitHub (https://github.com/xiaohe009009/FY-3-MIDI.git). 

Received: 5 December 2024; Accepted: 31 March 2025; Published: xx xx xxxx 

## **References** 

1. Dai, A. Drought under global warming: a review. _Wiley Interdiscip. Rev.-Clim. Chang._ **2** , 45–65, https://doi.org/10.1002/wcc.81 (2011). 

2. Wilhite, D. A. _Drought and Water Crises: Science, Technology, and Management Issues_ , https://doi.org/10.1201/9781420028386 (CRC Press, 2005). 

3. Smith, A. B. & Matthews, J. L. Quantifying uncertainty and variable sensitivity within the US billion-dollar weather and climate disaster cost estimates. _Nat. Hazards_ **77** , 1829–1851, https://doi.org/10.1007/s11069-015-1678-x (2015). 

4. Sherwood, S. & Fu, Q. A drier future? _Science_ **343** , 737–739, https://doi.org/10.1126/science.1247620 (2014). 

5. Ault, T. R. On the essentials of drought in a changing climate. _Science_ **368** , 256–260, https://doi.org/10.1126/science.aaz5492 (2020). 

6. Chiang, F., Mazdiyasni, O. & AghaKouchak, A. Evidence of anthropogenic impacts on global drought frequency, duration, and intensity. _Nat. Commun._ **12** , 2754, https://doi.org/10.1038/s41467-021-22314-w (2021). 

7. IPCC. _Climate Change 2023: Synthesis Report. Contribution of Working Groups I, II and III to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change_ [Core Writing Team, H. Lee and J. Romero (eds.)], https://doi.org/10.59327/IPCC/AR69789291691647 (IPCC, Geneva, Switzerland, 2023). 

8. Trenberth, K. E. _et al_ . Global warming and changes in drought. _Nat. Clim. Chang._ **4** , 17–22, https://doi.org/10.1038/nclimate2067 (2013). 

9. Yuan, X. _et al_ . A global transition to flash droughts under climate change. _Science_ **380** , 187–191, https://doi.org/10.1126/science. abn6301 (2023). 

10. Denissen, J. M. C. _et al_ . Widespread shift from ecosystem energy to water limitation with climate change. _Nat. Clim. Chang._ **12** , 677–684, https://doi.org/10.1038/s41558-022-01403-8 (2022). 

11. Yuan, W. _et al_ . Increased atmospheric vapor pressure deficit reduces global vegetation growth. _Sci. Adv._ **5** , eaax1396, https://doi. org/10.1126/sciadv.aax1396 (2019). 

12. Zhang, A., Jia, G. & Ustin, S. L. Water availability surpasses warmth in controlling global vegetation trends in recent decade: revealed by satellite time series. _Environ. Res. Lett._ **16** , 074028, https://doi.org/10.1088/1748-9326/ac0b68 (2021). 

13. Gampe, D. _et al_ . Increasing impact of warm droughts on northern ecosystem productivity over recent decades. _Nat. Clim. Chang._ **11** , 772–779, https://doi.org/10.1038/s41558-021-01112-8 (2021). 

14. Xu, C. _et al_ . Increasing impacts of extreme droughts on vegetation productivity under climate change. _Nat. Clim. Chang._ **9** , 948–953, https://doi.org/10.1038/s41558-019-0630-6 (2019). 

15. AghaKouchak, A. _et al_ . Remote sensing of drought: progress, challenges and opportunities. _Rev. Geophys._ **53** , 452–480, https://doi. org/10.1002/2014rg000456 (2015). 

16. Kogan, F. N. Global drought watch from space. _Bull. Amer. Meteorol. Soc_ . **78** , 621-636, 10.1175/1520-0477(1997)078<0621:GDWFS> 2.0.CO;2 (1997). 

17. Kogan, F. N. Application of vegetation index and brightness temperature for drought detection. _Adv. Space Res._ **15** , 91–100, https:// doi.org/10.1016/0273-1177(95)00079-T (1995). 

18. Mu, Q., Zhao, M., Kimball, J. S., McDowell, N. G. & Running, S. W. A remotely sensed global terrestrial drought severity index. _Bull. Amer. Meteorol. Soc._ **94** , 83–98, https://doi.org/10.1175/BAMS-D-11-00213.1 (2013). 

19. Rhee, J., Im, J. & Carbone, G. J. Monitoring agricultural drought for arid and humid regions using multi-sensor remote sensing data. _Remote Sens. Environ._ **114** , 2875–2887, https://doi.org/10.1016/j.rse.2010.07.005 (2010). 

20. Zhang, A. & Jia, G. Monitoring meteorological drought in semiarid regions using multi-sensor microwave remote sensing data. _Remote Sens. Environ._ **134** , 12–23, https://doi.org/10.1016/j.rse.2013.02.023 (2013). 

21. Zhang, X., Chen, N., Li, J., Chen, Z. & Niyogi, D. Multi-sensor integrated framework and index for agricultural drought monitoring. _Remote Sens. Environ._ **188** , 141–163, https://doi.org/10.1016/j.rse.2016.10.045 (2017). 

22. Zhang, A. & Jia, G. Satellite observed reversal in trends of tropical and subtropical water availability. _Int. J. Appl. Earth Obs. Geoinf._ **86** , 102015, https://doi.org/10.1016/j.jag.2019.102015 (2020). 

23. Zhang, A., Jia, G. & Wang, H. Improving meteorological drought monitoring capability over tropical and subtropical water-limited ecosystems: evaluation and ensemble of the Microwave Integrated Drought Index. _Environ. Res. Lett_ . **14** , https://doi. org/10.1088/1748-9326/ab005e (2019). 

24. Xian, D., Zhang, P., Fang, M., Liu, C. & Jia, X. The first Fengyun satellite international user conference. _Adv. Atmos. Sci._ **38** , 1429–1432, https://doi.org/10.1007/s00376-020-2011-5 (2020). 

25. Xian, D. _et al_ . Fengyun meteorological satellite products for earth system science applications. _Adv. Atmos. Sci._ **38** , 1267–1284, https://doi.org/10.1007/s00376-021-0425-3 (2021). 

26. Yao, P. _et al_ . A global daily soil moisture dataset derived from Chinese FengYun Microwave Radiation Imager (MWRI) (2010-2019). _Sci. Data_ **10** , 133, https://doi.org/10.1038/s41597-023-02007-3 (2023). 

27. Friedl, M. & Sulla-Menashe, D. _MODIS/Terra+Aqua Land Cover Type Yearly L3 Global 0.05Deg CMG V061_ . _NASA EOSDIS Land Processes Distributed Active Archive Center_ , https://doi.org/10.5067/MODIS/MCD12C1.061 (2022). 

28. Vicente-Serrano, S. M., Beguería, S. & López-Moreno, J. I. A multiscalar drought index sensitive to global warming: the Standardized Precipitation Evapotranspiration Index. _J. Clim._ **23** , 1696–1718, https://doi.org/10.1175/2009jcli2909.1 (2010). 

29. Vicente-Serrano, S. M., Beguería, S., López-Moreno, J. I., Angulo, M. & El Kenawy, A. A new global 0.5° gridded dataset (1901–2006) of a multiscalar drought index: comparison with current drought index datasets based on the Palmer Drought Severity Index. _J. Hydrometeorol._ **11** , 1033–1043, https://doi.org/10.1175/2010jhm1224.1 (2010). 

30. Beguería, S., Vicente-Serrano, S. M., Reig-Gracia, F. & Latorre Garcés, B. SPEIbase v.2.8. _DIGITAL.CSIC_ https://doi.org/10.20350/ digitalCSIC/15121 (2023). 

31. Beguería, S., Vicente-Serrano, S. M., Reig-Gracia, F. & Latorre Garcés, B. SPEIbase v.2.9. _DIGITAL.CSIC_ https://doi.org/10.20350/ DIGITALCSIC/15470 (2023). 

32. van der Schrier, G., Barichivich, J., Briffa, K. R. & Jones, P. D. A scPDSI-based global data set of dry and wet spells for 1901–2009. _J. Geophys. Res.-Atmos._ **118** , 4025–4048, https://doi.org/10.1002/jgrd.50355 (2013). 

Scientific **Data** | _(2025) 12:583_ | https://doi.org/10.1038/s41597-025-04935-8 

12 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

33. Barichivich, J., Osborn, T. J., Harris, I., van der Schrier, G. & Jones, P. D. Monitoring global drought using the self-calibrating Palmer Drought Severity Index [in “State of the Climate in 2022”]. _Bull. Amer. Meteorol. Soc._ **104** , S66–S67, https://doi. org/10.1175/2023BAMSStateoftheClimate.1 (2023). 

34. Yang, H., Zou, X., Li, X. & You, R. Environmental data records from FengYun-3B Microwave Radiation Imager. _IEEE Trans. Geosci. Remote Sensing_ **50** , 4986–4993, https://doi.org/10.1109/tgrs.2012.2197003 (2012). 

35. Yang, Z. _et al_ . Capability of Fengyun-3D satellite in earth system observation. _J. Meteorol. Res._ **33** , 1113–1130, https://doi. org/10.1007/s13351-019-9063-4 (2020). 

36. Li, X., Yang, H., You, R., Zhao, F. & Qiao, Y. Remote sensing typhoon Songda’s rainfall structure based on Microwave Radiation Imager of FY-3B satellite. _Chinese J. Geophys. (in Chinese)_ **55** , 2843–2853, https://doi.org/10.6038/j.issn.0001-5733.2012.09.004 (2012). 

37. Li, X. & You, R. _Status of QPE products from Fengyun satellites_ https://www.cgms-info.org/Agendas/GetWpFile.ashx?wid=fb00d913- 

   - 3aed-4348-8e94-36a14ea9c4a6&aid=157fbf60-10f8-43af-908c-4fb01318372e (2020). 

38. Shi, J. _et al_ . Physically based estimation of bare-surface soil moisture with the passive radiometers. _IEEE Trans. Geosci. Remote Sensing_ **44** , 3145–3153, https://doi.org/10.1109/TGRS.2006.876706 (2006). 

39. McFarland, M. J., Miller, R. L. & Neale, C. M. U. Land surface temperature derived from the SSM/I passive microwave brightness temperatures. _IEEE Trans. Geosci. Remote Sensing_ **28** , 839–845, https://doi.org/10.1109/36.58971 (1990). 

40. Tao, S. _et al_ . A global long-term, high-resolution satellite radar backscatter data record (1992-2022+): merging C-band ERS/ASCAT and Ku-band QSCAT. _Earth Syst. Sci. Data_ **15** , 1577–1596, https://doi.org/10.5194/essd-15-1577-2023 (2023). 

41. Du, L. _et al_ . A comprehensive drought monitoring method integrating MODIS and TRMM data. _Int. J. Appl. Earth Obs. Geoinf._ **23** , 245–253, https://doi.org/10.1016/j.jag.2012.09.010 (2013). 

42. Hao, C., Zhang, J. & Yao, F. Combination of multi-sensor remote sensing data for drought monitoring over Southwest China. _Int. J. Appl. Earth Obs. Geoinf._ **35** , 270–283, https://doi.org/10.1016/j.jag.2014.09.011 (2015). 

43. Zeng, J. _et al_ . An improved global vegetation health index dataset in detecting vegetation drought. _Sci. Data_ **10** , 338, https://doi. org/10.1038/s41597-023-02255-3 (2023). 

44. Zhang, L., Jiao, W., Zhang, H., Huang, C. & Tong, Q. Studying drought phenomena in the Continental United States in 2011 and 2012 using various drought indices. _Remote Sens. Environ._ **190** , 96–106, https://doi.org/10.1016/j.rse.2016.12.010 (2017). 

45. Huffman, G. J., Stocker, E. F., Bolvin, D. T., Nelkin, E. J. & Tan, J. GPM IMERG Final Precipitation L3 1 month 0.1 degree × 0.1 degree V07, _Goddard Earth Sciences Data and Information Services Center (GES DISC)_ , https://doi.org/10.5067/GPM/IMERG/3BMONTH/07 (2023). 

46. Gruber, A., Scanlon, T., van der Schalie, R., Wagner, W. & Dorigo, W. Evolution of the ESA CCI Soil Moisture climate data records and their underlying merging methodology. _Earth Syst. Sci. Data_ **11** , 717–739, https://doi.org/10.5194/essd-11-717-2019 (2019). 

47. Dorigo, W. _et al_ . ESA Soil Moisture Climate Change Initiative (Soil_Moisture_cci): COMBINED product, Version 09.1. _NERC EDS Centre for Environmental Data Analysis_ https://doi.org/10.5285/0e346e1e1e164ac99c60098848537a299 (2024). 

48. Owe, M., de Jeu, R. & Holmes, T. Multi-sensor historical climatology of satellite-derived global land surface moisture. _J. Geophys. Res._ **113** , F01002, https://doi.org/10.1029/2007jf000769 (2008). 

49. Vrije Universiteit Amsterdam (Richard de Jeu) & NASA GSFC (Manfred Owe). AMSR2/GCOM-W1 surface soil moisture (LPRM) L3 1 day 25 km x 25 km descending V001. _Goddard Earth Sciences Data and Information Services Center (GES DISC)_ , https://doi. org/10.5067/CGDEOBASZ178 (2014). 

50. Vrije Universiteit Amsterdam (Richard de Jeu) & NASA GSFC (Manfred Owe). AMSR2/GCOM-W1 surface soil moisture (LPRM) L3 1 day 25 km x 25 km ascending V001. _Goddard Earth Sciences Data and Information Services Center (GES DISC)_ , https://doi. org/10.5067/M5DTR2QUYLS2 (2014). 

51. Helsel, D. R., Hirsch, R. M., Ryberg, K. R., Archfield, S. A. & Gilroy, E. J. _Statistical Methods in Water Resources: U.S. Geological Survey Techniques and Methods, book 4, chap. A3_ , https://doi.org/10.3133/tm4a3, (USGS, 2020). 

52. Sen, P. K. Estimates of the regression coefficient based on Kendall’s tau. _J. Am. Stat. Assoc._ **63** , 1379–1389, https://doi.org/10.1080/0 1621459.1968.10480934 (1968). 

53. Theil, H. _A Rank-Invariant Method of Linear and Polynomial Regression Analysis_ . **23** , 345-381, https://doi.org/10.1007/978-94-0112546-8_20 (Springer, Dordrecht, 1992). 

54. Kendall, M. G. _Rank Correlation Method_ s (Griffin, 1975). 

55. Mann, H. B. Non-parametric tests against trend. _Econometrica_ **13** , 245–259, https://doi.org/10.2307/1907187 (1945). 

56. Zhang, A., Gao, H. & Jia, G. A dataset of global Fengyun-3 Microwave Integrated Drought Index from 2014 and on. V2. _Science Data Bank_ https://doi.org/10.57760/sciencedb.17942 (2025). 

57. Dai, A. Increasing drought under global warming in observations and models. _Nat. Clim. Chang._ **3** , 52–58, https://doi.org/10.1038/ nclimate1633 (2012). 

58. Harris, I., Osborn, T. J., Jones, P. & Lister, D. Version 4 of the CRU TS monthly high-resolution gridded multivariate climate dataset. _Sci. Data_ **7** , 109, https://doi.org/10.1038/s41597-020-0453-3 (2020). 

59. Sun, Q. _et al_ . A review of global precipitation data sets: data sources, estimation, and intercomparisons. _Rev. Geophys._ **56** , 79–107, https://doi.org/10.1002/2017RG000574 (2018). 

60. Hao, Z., AghaKouchak, A., Nakhjiri, N. & Farahmand, A. Global integrated drought monitoring and prediction system. _Sci. Data_ **1** , 140001, https://doi.org/10.1038/sdata.2014.1 (2014). 

61. Jiao, W., Wang, L. & McCabe, M. F. Multi-sensor remote sensing for drought characterization: current status, opportunities and a roadmap for the future. _Remote Sens. Environ._ **256** , 112313, https://doi.org/10.1016/j.rse.2021.112313 (2021). 

## **acknowledgements** 

This work was supported by the Funding by Fengyun Application Pioneering Project (FY-APP-ZX-2022.0221) and the Belt and Road International Science Organization Alliance Sustainable Development Research Program (CAS-ANSO-SDRP-2024-08). 

## **author contributions** 

A.Z., H.G. and G.J. conceived the study. R.X. X.L. and H.Z. helped to collect and process the FY-3 data. A.Z. developed the method, carried out the analysis, and wrote the manuscript. A.Z. and H.G. developed the dataset. H.G. and G.J. provided advices on the analysis and the manuscript writing. All authors reviewed and edited the manuscript. 

## **Competing interests** 

The authors declare no competing interests. 

## **additional information** 

**Correspondence** and requests for materials should be addressed to H.G. or G.J. 

Scientific **Data** | _(2025) 12:583_ | https://doi.org/10.1038/s41597-025-04935-8 

13 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

**Reprints and permissions information** is available at www.nature.com/reprints. 

**Publisher’s note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

**Open Access** This article is licensed under a Creative Commons Attribution-NonCommercialNoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/. 

© The Author(s) 2025 

Scientific **Data** | _(2025) 12:583_ | https://doi.org/10.1038/s41597-025-04935-8 

14 

