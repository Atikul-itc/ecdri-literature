www.nature.com/scientificdata 



**OPEN** 

**DATA DESCRIPTOR** 

# **a global drought dataset for Multivariate Composite Drought Index (MCDI) and its constituent drought indices** 

**Mengjia Yuan**<sup>**1,2**</sup> **, Guojing Gan**<sup>**3**✉</sup> **, Jingyi Bu**<sup>**4**</sup> **, Yanxin Su**<sup>**1,2**</sup> **, Hongyu Ma**<sup>**1,2**</sup> **, Xianghe Liu**<sup>**1,2**</sup> **, Leyao Zhang**<sup>**1,2**</sup> **, Yongqiang Zhang**<sup>**1**</sup> **& Yanchun Gao**<sup>**1**✉</sup> 

**High-resolution drought index datasets are essential for drought monitoring and assessment. Despite numerous global/regional drought index datasets, the composite drought index datasets that comprehensively consider meteorological, agricultural, and hydrological factors are still very few, thus hindering the capture of complex drought dynamics and comprehensive risk assessment. To address this gap, this study produced a 0.1° resolution global drought dataset (1980–2019) based on the newly developed concept of Multivariate Composite Drought Index (MCDI), which considered the time lag and cumulative effects of drought and could characterize comprehensive drought characteristics effectively. The dataset contains MCDI and its four constituent indices (Standardized Precipitation Actual Evapotranspiration Index (SPAEI), Standardized Soil Moisture Index (SSI), Standardized Runoff Index (SRI), Water Storage Deficit Index (WSDI)) on a monthly scale. Verification results showed that they indicated the drought evolution and ecosystem response process well, especially the MCDI. Overall, the dataset compensated for the data deficit of the comprehensive drought index and would provide data support for global drought monitoring and adaptive management of drought under climate change.** 

## **Background & Summary** 

Drought is a natural hazard triggered by intense and persistent water deficits with relatively wide-ranging impacts<sup>1–3</sup> . Severe drought events can impede crop and vegetation growth, threaten ecosystem health, disrupt normal livelihoods, and cause significant socio-economic losses<sup>4–6</sup> . Moreover, these impacts are often unevenly distributed, disproportionately affecting vulnerable populations and thereby exacerbating global health, well-being, and gender inequalities<sup>7</sup> . Under the combined pressures of climate change and human activities, drought will become more frequent, severe, and unpredictable in many regions of the world<sup>8–10</sup> . Given its extensive reach and destructive potential, drought has garnered widespread attention from various sectors in recent years, which has also highlighted the urgency of developing quantitative drought indicators and establishing corresponding datasets for drought monitoring<sup>5,11,12</sup> . 

Drought index is one of the most widely used and effective tools to quantitatively characterize drought<sup>13</sup> . The existing drought indices can be broadly categorized into drought indices constructed for specific types of droughts (e.g., meteorological drought, agricultural drought, etc.) and composite drought indices for a comprehensive assessment of drought<sup>14,15</sup> . The first type of drought indices tends to rely on environmental variables related to a specific type of drought. For example, the Standardized Precipitation Index (SPI)<sup>16</sup> , Standardized Soil Moisture Index (SSI)<sup>17</sup> , and Standardized Runoff Index (SRI)<sup>18</sup> are often used to characterize meteorological, agricultural, and hydrological drought, respectively. This is due to the fact that they are constructed solely based on precipitation (P), soil moisture (SM), and runoff (RO), respectively. Composite drought indices, on 

1Key Laboratory of Water cycle and Related Land Surface Processes, institute of Geographic Sciences and natural Resources Research, Chinese Academy of Sciences, Beijing, 100101, China.<sup>2</sup> University of chinese Academy of Sciences, Beijing, 100049, China.<sup>3</sup> State Key Laboratory of Lake and Watershed Science for Water Security, nanjing Institute of Geography and Limnology, Chinese Academy of Sciences, Nanjing, 211135, China.<sup>4</sup> earth Systems Research center, institute for the Study of earth, Oceans, and Space, University of new Hampshire, Durham, nH, 03824, USA.<sup>✉</sup> e-mail: gjgan@niglas.ac.cn; gaoyanc@igsnrr.ac.cn 

Scientific **Data** | _(2025) 12:2035_ | https://doi.org/10.1038/s41597-025-06320-x 

1 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

the other hand, are indices that combine more environmental variables or different types of univariate drought indices<sup>19–21</sup> . For example, Zhang, _et al_ .<sup>5</sup> constructed a multivariate standardized drought index (MMSDI) by integrating P, evapotranspiration (ET), and SM, finding that MMSDI had advantages in agricultural drought detection in China. Based on the Gaussian copula function, Shah and Mishra<sup>6</sup> developed an Integrated Drought Index (IDI) by integrating the SPI, SRI, SSI, and standardized groundwater index (SGI), finding that IDI could effectively monitor and assess drought under retrospective and future climates in India. Compared to the first type of drought indices, the composite drought indices can better reflect the characteristics of integrated, complex drought events<sup>15,22,23</sup> . 

As droughts become more frequent, many studies have pointed to the need to consider the lagging and cumulative effects of drought in drought research-related work<sup>6,24–26</sup> . This is because the frequency and severity of droughts may lead to the normalization of one drought event before the end of another, leading to the gradual collapse of ecosystems<sup>27–29</sup> . Accounting for the effects of previous droughts and the environmental context in which droughts occur can better reflect the ecosystem response to drought and provide a scientific basis for drought monitoring and early warning<sup>25</sup> . To make up for the fact that the existing composite drought indices seldom consider the lagged and cumulative effects of drought, Yuan, _et al_ .<sup>30</sup> recently proposed a new composite drought index named the Multivariate Composite Drought Index (MCDI). Based on the Gringorten empirical formula, MCDI integrated the meteorological drought index (Standardized Precipitation Actual Evapotranspiration Index (SPAEI)), agricultural drought index (SSI), and hydrological drought indices (SRI, Water Storage Deficit Index (WSDI)) with accounting for the time lag between different types of droughts and the cumulative effects of droughts. The application results in China showed that MCDI has good potential for drought monitoring and assessment, and this is also the drought index used in this study to construct the global drought dataset. 

The exploration of drought indices emphasizes the need for high-quality drought datasets, and the lack of consistent source data increases the difficulty of quantifying drought<sup>3,31</sup> . Many global/regional drought datasets have been generated, such as self-calibrating Palmer Drought Severity Index (scPDSI)<sup>32–34</sup> , SPEI<sup>13,35–37</sup> , and SPI<sup>3,16,38</sup> datasets with different spatial-temporal resolution. It can be noted that although many drought index datasets have emerged globally and regionally, there are still very few composite drought index datasets. This means that many of the ideas for constructing a composite drought index have not been converted into realistic datasets, which would be unfavorable for methodological development and research. Firstly, the lack of a composite drought index dataset is equivalent to the loss of a means of comprehensively assessing drought. Secondly, the lack of a composite drought index dataset would be detrimental to the emergence of new composite drought indices and their assessment. Specifically, when a new composite drought index appears, it cannot be compared with existing composite drought indices due to missing data. Moreover, comparisons with other types of drought indices may make the assessment unfair and inaccurate, and ultimately lead to the masking of its shortcomings or strengths. Therefore, it is particularly essential to produce a high-resolution composite drought index dataset to compensate for the data deficiencies. 

In this study, we constructed a 0.1° resolution global drought dataset (1980–2019) for MCDI and its constituent indices on a monthly scale. Specifically, we referred to the methodology of MCDI to first generate WSDI as well as SPAEI, SSI, and SRI at different time scales and then fused the indices to generate MCDI with accounting for the time lag and cumulative effects of drought. In this process, apart from the MCDI data, SPAEI, SSI, SRI, and WSDI data were generated as intermediates. Subsequently, we validated the credibility and usability of this dataset to provide effective data to support the development of drought management and adaptation strategies. 

## **Methods** 

**Data sources.** The precipitation (P) and actual evapotranspiration (AET) data were used to produce SPAEI. Monthly P data for 1980–2019 were obtained from Multi-Source Weighted-Ensemble Precipitation (MSWEP). The P data have a spatial resolution of 0.1° and are available online (https://www.gloh2o.org/mswep/)<sup>39–41</sup> . Monthly AET data for the period 1980–2019 were sourced from the fourth generation of the Global Land Evaporation Amsterdam Model (GLEAM) with a spatial resolution of 0.1° (available online https://www.gleam.eu/)<sup>42</sup> . The soil moisture (SM) data were used for calculating SSI. Monthly-scale SM for 1980–2019 was obtained from the ECMWF Reanalysis v5 (ERA5)-Land dataset (available online https://www.ecmwf.int/en/forecasts/ dataset/ecmwf-reanalysis-v5-land) with a spatial resolution of 0.1°. The dataset contains SM data for four soil horizons (0–7 cm, 7–28 cm, 28–100 cm, and 100–289 cm), and SM in the 0–10 cm soil layer was weighted according to soil layer thickness<sup>43,44</sup> . 

The runoff (RO) data were used to generate SRI. The monthly RO data were obtained from the ERA5-Land, Famine Early Warning Systems Network (FEWS NET) Land Data Assimilation System (FLDAS) (available online https://disc.gsfc.nasa.gov/datasets/FLDAS_NOAH01_C_GL_M_001/summary), and Ghiggi, _et al_ .<sup>45</sup> (available online https://figshare.com/articles/dataset/Grun_Global_Runoff_Reconstruction/9228176). Their spatial resolutions are 0.1°, 0.1°, and 0.5°, respectively. The bilinear interpolation<sup>36,46,47</sup> was chosen in this study to resample the data to 0.1° to unify the spatial resolution. It is important to note that this interpolation process redistributes the original 0.5° data onto a finer grid but does not enhance the actual spatial detail of the source data. To further reduce the uncertainties from the source data, the final RO data for 1980–2019 at 0.1° resolution were generated by averaging the three sources. 

The terrestrial water storage anomaly (TWSA) data were used for generating WSDI. Due to the requirement of temporal continuity and length of data, the reconstructed datasets of TWSA were selected for this study. The monthly TWSA data from 1980 to 2019 with a spatial resolution of 0.5° were obtained from Li, _et al_ .<sup>48</sup> (available online https://datadryad.org/dataset/doi:10.5061/dryad.z612jm6bt) and Humphrey and Gudmundsson<sup>49</sup> (available online https://figshare.com/articles/dataset/GRACE-REC_A_reconstruction_of_climate-driven_water_ storage_changes_over_the_last_century/7670849). To reduce uncertainties in the data sources, the final TWSA 

Scientific **Data** | _(2025) 12:2035_ | https://doi.org/10.1038/s41597-025-06320-x 

2 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

|**Category**|**SPAEI, SSI, SRI, MCDI**|**scPDSI**|**WSDI**|
|---|---|---|---|
|Normal|≥−<br>.0 5|≥−<br>.1 0|0 5<br>≥−<br>.|
|Slight Drought|−.<br>−<br>.<br>1 0<br>0 5<br>~|−.<br>−<br>.<br>2 0<br>1 0<br>~|−.<br>−<br>.<br>~<br>1 0<br>0 5|
|Moderate Drought|1 5<br>1 0<br>~<br>−.<br>−<br>.|3 0<br>2 0<br>−.<br>−<br>.<br>~|~<br>−.<br>−<br>.<br>2 0<br>1 0|
|Severe Drought|~<br>2 0<br>1 5<br>−.<br>−<br>.|~<br>−.<br>−<br>.<br>4 0<br>3 0|~<br>−.<br>−<br>.<br>3 0<br>2 0|
|Extreme Drought|2 0<br>≤−<br>.|4 0<br>≤−<br>.|4 0<br>3 0<br>~<br>−.<br>−<br>.|



**Table 1.** The drought categorization for drought indices. 

data were produced by averaging the three datasets before resampling to a 0.1° grid using bilinear interpolation. Similarly, bilinear interpolation merely distributes spatial information onto a finer-resolution grid without adding any new spatial information. 

**MCDI calculation.** As a comprehensive drought index, MCDI showed good ability to identify and characterize drought over China<sup>30</sup> . Therefore, referencing previous work, we developed a global high-resolution drought index dataset, which includes MCDI and its intermediates (SPAEI, SSI, SRI, WSDI). The generation of MCDI was mainly divided into three steps: 

Firstly, calculating the drought indices (SPAEI, SSI, SRI, WSDI) involved in constructing MCDI. The standardized drought indices (SDI, including SPAEI, SSI, and SRI) share a common calculation principle. For a given time scale, the cumulative values of the underlying variable are fitted to a probability distribution and then converted to a standard normal distribution. Specifically, the SPAEI was derived by fitting the cumulative difference between P and AET to a Log-Logistic distribution<sup>50,51</sup> , whereas SSI and SRI were obtained by fitting cumulative SM, RO to a gamma distribution, respectively<sup>9,18</sup> . These indices were considered for time scales from 1 to 12 months, denoted as SDI1, SDI2,…, and SDI12. In contrast, WSDI was calculated directly by normalizing the water storage deficit (WSD) based on the mean and standard deviation of the WSD time series<sup>52,53</sup> . In which WSD was the deviation of the monthly TWSA from its long-term climatic mean<sup>54</sup> . Table 1 lists the drought classifications for SDI and WSDI. 

Secondly, calculating the lag time between different types of droughts at the pixel scale and regenerating drought indices data based on the lag time. Specifically, for meteorological and hydrological droughts, we calculated the Pearson correlation coefficient between the hydrological drought index (WSDI) and the meteorological drought index (SPAEI) across cumulative timescales from 1 to 12 months (SPAEI-n, n = 1, 2,…, 12). The lag time for a given pixel was definitively identified as the specific timescale n (months) at which this correlation coefficient reached its maximum value. Then we created the new dataset (SPAEInew) by mapping each pixel to the drought index value at its specific lag timescale. For example, in the resulting SPAEInew dataset, a pixel with a 3-month lag time was assigned the SPAEI3 value. This method was subsequently repeated to construct the SSInew and SRInew datasets. 

Finally, the MCDI was constructed based on the regenerated drought index dataset and the Gringorten empirical joint probability distribution<sup>55</sup> . For a total of N = 480 monthly observations, the joint empirical probability _pi_ for the i-th observation was calculated as ( _mi_<sup>−</sup> 0 44. )/( _N_ + 0 12). . Here, _mi_ counted how often all four indices were simultaneously at or below their i-th values. Then, MCDI was computed by transforming _pi_ using the inverse standard normal distribution. A more detailed calculation procedure can be found in Yuan, _et al_ .<sup>30</sup> . The drought classification of MCDI is shown in Table 1. The datasets, variables involved in developing MCDI, and the process of generating and validating MCDI are shown in Fig. 1. 

**Evaluation criteria.** The self-calibrating Palmer Drought Severity Index (scPDSI)<sup>34</sup> is one of the most recognized and widely used drought indices at present. Compared with other drought indices, scPDSI involves multiple variables in the water cycle process and is relatively more comprehensive. Therefore, this study used the existing scPDSI dataset to assess the performance of MCDI and its constituent indices (SPAEI, SSI, SRI, WSDI). The monthly scPDSI data from 1980 to 2019 with a spatial resolution of 0.5° were available online https://crudata.uea.ac.uk/cru/data/drought/<sup>32,33</sup> . To harmonize the spatial resolution of the data, scPDSI data were resampled to 0.1° using bilinear interpolation, which merely redistributes the data onto a finer grid without adding spatial detail. 

The Normalized Difference Vegetation Index (NDVI) was used to evaluate the performance of MCDI on the global scale. Furthermore, it helped explore the consistency of MCDI and ecosystem responses to droughts. The NDVI data were obtained from the PKU GIMMS Normalized Difference Vegetation Index product (PKU GIMMS NDVI, version 1.2) (available online https://zenodo.org/records/8253971)<sup>56</sup> . Based on a machine learning model, PKU GIMMS NDVI integrated Landsat Surface Reflectance data, the GIMMS NDVI3g (V1.0) product, and the MODIS Vegetation Index product. Accuracy validation results showed that PUK GIMMS NDVI effectively removed the evident orbital drift and sensor degradation effects in the tropics. PKU GIMMS NDVI has a spatial resolution of 1/12° and a temporal resolution of half a month. To unify the resolution, we averaged the two images for each month to obtain the monthly mean and resampled the data to 0.1° using bilinear interpolation. It is acknowledged that this process results in a spatial degradation and a smoothing of the original high-resolution information. 

Flux data obtained from FLUXNET (https://fluxnet.org/data)<sup>57</sup> were used to further assess the validity of this drought dataset. We first filtered out 30 flux sites by several conditions: (1) data were available for at least 10 

Scientific **Data** | _(2025) 12:2035_ | https://doi.org/10.1038/s41597-025-06320-x 

3 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



**Fig. 1** The flowchart for the global drought index dataset generation and validation. P, AET, SM, RO, and TWSA represent precipitation, actual evapotranspiration, soil moisture, runoff, and terrestrial water storage anomaly, respectively. IDIs represent intermediate drought indices. 

years; (2) Gross primary productivity (GPP) and ET data were available; (3) all drought indices had valid values at this site. Then we standardized GPP and ET by subtracting their multi-year contemporaneous means and dividing by their standard deviations. Details of the flux sites are shown in Table 2. 

Apart from the above four evaluation indicators, we also selected three typical drought events to assess the ability of MCDI to monitor drought. These events caused relatively large losses and attracted widespread attention, occurring in Australia, the Contiguous United States, and South Africa, respectively. For Australia, 2019 was the driest year on record<sup>58</sup> . The widespread drought in Australia was primarily driven by excessive temperatures and persistent precipitation deficits that in 2017<sup>59</sup> . In 2019, temperatures were 1.52 °C above the multi-year average, and a precipitation deficit from April to November prevented soil moisture and runoff generation<sup>60,61</sup> . This extreme drought had led to massive canopy dieback and record-breaking wildfire events in southeastern Australia<sup>62</sup> . For the Contiguous United States, the drought that happened in 2012 was one of the most severe drought events since 1950<sup>63</sup> . It began during the growing season and affected 80% of the agricultural land in the Contiguous United States, causing not only significant economic losses but also a major impact on food security and food prices<sup>64</sup> . For South Africa, between December 2015 and February 2016, a severe drought event triggered by El Niño occurred<sup>65</sup> . Statistically, this drought event reached the highest extreme temperatures in the past 50 years<sup>66</sup> . In addition, the drought also had a significant impact on food production. The model simulations showed that this drought event led to the largest reduction in food production over the past 30 years<sup>67</sup> . 

**Statistical methods.** In geographical and hydrological research, Pearson correlation coefficients (PCC) are often used to analyze the degree of correlation between variables and to evaluate the accuracy of a variable against a reference variable<sup>68</sup> . In this study, the PCC between scPDSI/NDVI/GPP/ET and MCDI, as well as intermediate drought indices (SPAEI, SSI, SRI, WSDI), was calculated separately to assess their credibility and usability. The strength of the correlation was interpreted based on the absolute value of the PCC (|PCC|). Within the context of drought indices, correlations commonly fall in the 0.3~0.5 range, and values above 0.5 are generally regarded as indicating a relatively strong association<sup>69–73</sup> . Accordingly, we adopted the explicit criteria from Wang, _et al_ .<sup>74</sup> . The correlations were classified as follows: |PCC| ≥ 0.8 for extremely strong, 0.8 > |PCC| ≥ 0.5 for strong, 0.5 > |PCC| ≥ 0.3 for medium, and |PCC| < 0.3 for weak correlation. Consequently, |PCC| = 0.3 and |PCC| = 0.5 were employed as the two key thresholds in this study. 

## **Data Records** 

The dataset for the MCDI and indices used to construct the MCDI (SPAEI, SSI, SRI, WSDI) is openly available on the Zenodo repository under the Creative Commons Attribution 4.0 International (CC BY 4.0) license (https://doi.org/10.5281/zenodo.15143908<sup>75</sup> ). The high-resolution dataset has a spatial resolution of 0.1° × 0.1°, a spatial range of 180°W to 180°E and 90°S to 90°N, a period of 1980–2019, and a temporal resolution of monthly scale. The dataset is presented in geographic latitude/longitude projection (EPSG: 4326) and stored using the NetCDF format. A total of 38 data files are included in the dataset, with drought index names in the file names. For SPAEI, SSI, and SRI with multi-timescale characteristics, the drought index names are followed by the timescale, e.g., SPAEI3/SSI3/SRI3. 

Scientific **Data** | _(2025) 12:2035_ | https://doi.org/10.1038/s41597-025-06320-x 

4 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

|**Site**<br>AT-Neu|**IGBP**<br>GRA|**Lon (°)**<br>11.32|**Lat (°)**<br>47.12|**Data availability**<br>2002–2012|
|---|---|---|---|---|
|AU-How|WSA|131.15|−12.49|2001–2014|
|AU-Tum|EBF|148.15|−35.66|2001–2014|
|BE-Lon|CRO|4.75|50.55|2004–2014|
|BE-Vie|MF|6.0|50.31|1996–2014|
|CH-Dav|ENF|9.86|46.82|1997–2014|
|DE-Geb|CRO|10.91|51.1|2001–2014|
|DE-Gri|GRA|13.51|50.95|2004–2014|
|DE-Hai|DBF|10.45|51.08|2000–2012|
|DE-Tha|ENF|13.57|50.96|1996–2014|
|FI-Sod|ENF|26.64|67.36|2001–2014|
|FR-LBr|ENF|−0.77|44.72|1996–2008|
|FR-Pue|EBF|3.56|43.74|2000–2014|
|IT-BCi|CRO|14.96|40.52|2004–2014|
|IT-Lav|ENF|11.28|45.96|2003–2014|
|IT-MBo|GRA|11.05|46.01|2003–2013|
|NL-Loo|ENF|5.74|52.17|1996–2014|
|RU-Fyo|ENF|32.92|56.46|1998–2014|
|US-Blo|ENF|−120.63|38.9|1997–2007|
|US-GLE|ENF|−106.24|41.37|2004–2014|
|US-Me2|ENF|−121.56|44.45|2002–2014|
|US-MMS|DBF|−86.41|39.32|1999–2014|
|US-Ne1|CRO|−96.48|41.17|2001–2013|
|US-Ne2|CRO|−96.47|41.16|2001–2013|
|US-Ne3|CRO|−96.44|41.18|2001–2013|
|US-NR1|ENF|−105.55|40.03|1998–2014|
|US-SRM|WSA|−110.87|31.82|2004–2014|
|US-Ton|WSA|−120.97|38.43|2001–2014|
|US-Var|GRA|−120.95|38.41|2000–2014|
|US-Wkg|GRA|−109.94|31.74|2004–2014|



**Table 2.** The description of 30 flux sites used in this study. IGBP = International Geosphere Biosphere Programme, CRO = Croplands, EBF = Evergreen broadleaf forests, ENF = Evergreen needleleaf forests, GRA = Grasslands, MF = Mixed forests, WSA = Woody Savannas. 



**Fig. 2** The spatial distribution of the Pearson correlation coefficient ( _p_ < 0.05) for the MCDI and scPDSI over the period 1980–2019. 

## **Technical Validation** 

**Agreement between MCDI (SPAEI, SSI, SRI, WSDI) and scPDSI.** Figure 2 presents the spatial distribution of the Pearson correlation coefficients ( _p_ < 0.05) for the MCDI and scPDSI over the period 1980–2019. MCDI and scPDSI exhibited similar spatial distribution characteristics with good correlation. To quantify their agreement, we used |PCC| = 0.3 and |PCC| = 0.5 as thresholds, corresponding to medium and strong correlation levels, respectively. Although these criteria were applied symmetrically to both positive and negative correlations, the spatial proportion of pixels with significant negative correlations (PCC ≤ −0.3) was negligible (consistently below 0.5% in all comparisons). Therefore, we focus on the dominant positive correlation patterns here. Globally, the proportion of pixels with PCC greater than 0.5 between MCDI and scPDSI was 59.84% ( _p_ < 0.05), while the proportion of pixels with PCC greater than 0.3 was as high as 86.69% ( _p_ < 0.05). The mean values of the 

Scientific **Data** | _(2025) 12:2035_ | https://doi.org/10.1038/s41597-025-06320-x 

5 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



**Fig. 3** The spatial distribution of the maximum Pearson correlation coefficient ( _p_ < 0.05) between scPDSI and SPAEI, SSI, and SRI on different time scales (1–12 months) and the correlation between scPDSI and WSDI over the period 1980–2019. 

PCC between MCDI and scPDSI in North America, South America, Europe, Asia, Africa, and Oceania were 0.46, 0.54, 0.61, 0.51, 0.40, and 0.56 ( _p_ < 0.05), respectively. Spatially, the areas with relatively lower correlation between MCDI and scPDSI were mainly concentrated in tropical regions and high-latitude regions, such as tropical Africa and northern North America, which has also been found in other studies<sup>65,76</sup> . This phenomenon may be because these two regions are susceptible to factors such as large-scale circulation, resulting in the inability of the aridity index to correctly capture the characteristics of wet and dry dynamics. In addition, the susceptibility of sparsely vegetated areas in Africa to surface radiation may lead to poorer quality source data from satellite observations, transferring errors to the drought index, which ultimately results in poorer correlations among the drought indices<sup>65,77</sup> . 

Figure 3 displays the maximum correlation between scPDSI and SPAEI/SSI/SRI on different time scales and the correlation between scPDSI and WSDI. The percentages of pixels with PCC greater than 0.5 for SPAEI, SSI, SRI, and WSDI were 50.38%, 50.34%, 47.69%, and 59.34% ( _p_ < 0.05), respectively. The proportion of pixels with PCC greater than 0.3 between SPDSI and SPAEI, SSI, SRI as well as WSDI all exceeded 80.0% but was lower than 84.0% ( _p_ < 0.05). Even though the spatial distribution of correlations between different drought indices (SPAEI, SSI, SRI, and WSDI) and scPDSI showed similar characteristics, the correlation values between them varied in different regions. This result may be due to fundamental differences in construction principles or dependent variables between drought indices<sup>78</sup> . 

Although drought indices in this dataset all showed good correlations with the scPDSI, the MCDI presented some superiority compared to the others. The percentage of pixels with correlations greater than 0.5 for MCDI and scPDSI was 9.46%, 9.51%, 12.16%, and 0.51% ( _p_ < 0.05) higher than SPAEI, SSI, SRI, and WSDI, respectively. In addition, the mean values of the correlations of MCDI and scPDSI in different continents were always higher than other drought indices or lower than others by a small difference. The possible reason for this phenomenon is that MCDI has the advantage of being a comprehensive drought index by considering multiple components of the water balance theory<sup>30</sup> . While other drought indices are constructed based on different components with their focus, this fundamental difference may lead to their inherent limitations in characterizing drought<sup>79</sup> . 

**Agreement between MCDI (SPAEI, SSI, SRI, WSDI) and NDVI.** Figure 4 presents the PCC between MCDI/scPDSI and NDVI as well as the difference between them. Overall, both MCDI and scPDSI showed relatively high positive correlations with NDVI in southern Africa, inland Australia, eastern and southern South America, southern North America, and southern Asia. In some tropical rainforests, perennial high-humidity areas (e.g., Central African rainforests, parts of the Amazon Basin), and high-latitude areas (e.g., Northern Europe and Asia), the correlation between MCDI/scPDSI and NDVI was relatively low or even sporadically negative. Apart from the quality of the source data, this may be because vegetation growth in these areas is also 

6 

Scientific **Data** | _(2025) 12:2035_ | https://doi.org/10.1038/s41597-025-06320-x 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



**Fig. 4** The spatial distribution of the Pearson correlation coefficient ( _p_ < 0.05) between MCDI/scPDSI and NDVI as well as their difference over the period 1982–2019. 

affected by temperature, radiation, or other factors, not just water constraints<sup>3</sup> . In other words, it is the complexity of vegetation physiological processes and other climatic and environmental drivers that cause non-synergistic variations in vegetation and drought indices<sup>65,76</sup> . Compared to scPDSI, MCDI presented higher PCC in some regions. The proportion of pixels with PCC greater than 0.3 between MCDI and NDVI was 31.89% ( _p_ < 0.05), while scPDSI was only 23.99% ( _p_ < 0.05). The differences in the correlation between the two and NDVI were mainly found in regions such as southern and eastern Africa and Australia. It indicated that the explanatory power of MCDI for NDVI was generally higher than that of scPDSI in these regions and that MCDI was better able to capture the response of vegetation to wet-dry changes, also suggesting its greater applicability and stability 

Scientific **Data** | _(2025) 12:2035_ | https://doi.org/10.1038/s41597-025-06320-x 

7 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



**Fig. 5** The spatial distribution of the Pearson correlation coefficient ( _p_ < 0.05) between NDVI and WSDI and the maximum Pearson correlation coefficient ( _p_ < 0.05) with SPAEI, SSI, and SRI at different time scales (SPAEI-n/SSI-n/SRI-n (n = 1, 2,…, 12)) over the period 1982–2019. 



**Fig. 6** The Pearson correlation coefficients between the drought indices (MCDI, SPAEI, SSI, SRI, WSDI, scPDSI) and measured flux data (GPP, ET) at 30 flux sites during droughts. 

in capturing multifactorial moisture dynamics. As for the reason, it may be that NDVI has a lag in its response to the environment, and the MCDI was constructed in such a way as to account for the lag and cumulative effects of environmental and climatic conditions. 

Figure 5 illustrates the correlation between NDVI and WSDI and the maximum correlation with SPAEI, SSI, and SRI at different time scales (SPAEI-n/SSI-n/SRI-n (n = 1, 2,…, 12)). The percentages of pixels with PCC greater than 0.3 for SPAEI, SSI, SRI, and WSDI were 22.38%, 45.59%, 37.61%, and 30.01% ( _p_ < 0.05), respectively. It can be found that the spatial distribution of the correlations presented by the four drought indices with NDVI was like that of MCDI and scPDSI. They showed significant positive correlations with NDVI in regions such as inland Australia and Central Asia, while they had low or even negative correlations at high latitudes and in regions with overabundant thermal and hydrological conditions. That is, like MCDI and scPDSI, they were also effective in capturing ecosystem responses to changes in the external environment, though there were some differences among local areas. 

**Agreement between MCDI (SPAEI, SSI, SRI, WSDI) and measured flux data.** GPP and ET are commonly used to indicate ecosystem status<sup>80,81</sup> . Figure 6 presents the Pearson correlation coefficients between the drought indices (MCDI, scPDSI, SPAEI, SSI, SRI, WSDI) and measured flux data (GPP, ET) at 30 flux sites 

8 

Scientific **Data** | _(2025) 12:2035_ | https://doi.org/10.1038/s41597-025-06320-x 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



**Fig. 7** The spatial and temporal dynamics of MCDI, the constituent indices of MCDI (SPAEI3, SSI3, SRI3, WSDI), scPDSI, and NDVI for August, October, and December 2019 in Australia. 

during droughts. The mean PCC values of drought indices (MCDI, scPDSI, SPAEI, SSI, SRI, WSDI) and GPP at 30 flux sites were 0.33, 0.27, 0.31, 0.36, 0.34, and 0.30, respectively. Among them, MCDI exhibited a more concentrated data distribution profile, which may be attributed to the fact that MCDI integrates multiple meteorological and hydrological factors<sup>30</sup> . In contrast, although scPDSI also considers multiple variables of the water cycle, it performed poorly with high variance. This may be due to the fact that scPDSI does not account for the long-term cumulative effect of drought and the lagged response of ecosystems, which ultimately leads to non-synergistic changes in scPDSI and GPP<sup>26,47,82</sup> , whereas MCDI makes up for this deficiency. Moisture is a key limiting factor for plant photosynthesis, and soil moisture and runoff affect GPP through direct water supply and resource 

Scientific **Data** | _(2025) 12:2035_ | https://doi.org/10.1038/s41597-025-06320-x 

9 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



**Fig. 8** The spatial and temporal dynamics of MCDI, the constituent indices of MCDI (SPAEI3, SSI3, SRI3, WSDI), scPDSI, and NDVI for June and October 2012, and February 2013 in the Contiguous United States. 

reallocation, respectively<sup>44,77,83</sup> . Thus, the phenomenon of SSI and SRI showing a favorable correlation with GPP was also explained. The average PCC values of drought indices (MCDI, scPDSI, SPAEI, SSI, SRI, WSDI) and ET at 30 flux sites were 0.34, 0.31, 0.35, 0.33, 0.30, and 0.26, respectively. Due to the close linkage between GPP and ET, the correlation between drought indices and ET showed similar characteristics<sup>84</sup> . The main reason for the superior correlation between SPAEI and ET over other indices was that the SPAEI considered actual evapotranspiration, and the MCDI, which incorporated the SPAEI, similarly reflected this advantage. Overall, validation with measured flux data showed that the changes in MCDI (SPAEI, SSI, SRI, WSDI) were consistent with the ecosystem response to droughts, and MCDI were more robust compared to other indices. 

**Performance of drought indices (MCDI, SPAEI, SSI, SRI, WSDI) during specific drought events.** Figure 7 presents the spatial and temporal dynamics of MCDI, the constituent indices of MCDI (SPAEI3, SSI3, SRI3, WSDI), scPDSI, and NDVI in Australia for August, October, and December 2019. Australia was in a persistent drought from August to December, with a peak of drought severity (drought extent and drought index values) in December. The NDVI showed a decline in vegetation productivity in December in almost all regions, particularly in eastern Australia. Correspondingly, the scPDSI presented drought conditions 

Scientific **Data** | _(2025) 12:2035_ | https://doi.org/10.1038/s41597-025-06320-x 

10 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



**Fig. 9** The spatial and temporal dynamics of MCDI, the constituent indices of MCDI (SPAEI3, SSI3, SRI3, WSDI), scPDSI, and NDVI for November 2015, January 2016, and March 2016 in South Africa. 

across almost all of Australia, particularly in the southeastern and southern regions. As we know, the drought in 2019 was caused by the accumulation of pre-drought environmental conditions, and at this point, the type of drought might have switched to one dominated by agricultural and hydrological drought<sup>58,59</sup> . This might also be the reason why SPAEI3 showed lower drought extent and severity compared to other drought indices. Soil moisture and runoff were not recharged for a long period, so it was reasonable that SSI3 and SRI3 both exhibited severe drought status. WSDI characterizes changes in terrestrial water storage, accounting for a combination of variables such as surface water and groundwater<sup>85</sup> . Although WSDI values were relatively lower and less variable during drought, it was equally effective in indicating drought conditions. MCDI integrated SPAEI, SSI, SRI, and WSDI, 

Scientific **Data** | _(2025) 12:2035_ | https://doi.org/10.1038/s41597-025-06320-x 

11 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

showing their combined characteristics. Thus, the differences presented by different drought indices in characterizing the same drought event and the extremes exhibited by a single drought index were effectively avoided. 

Figure 8 displays the spatial and temporal dynamics of MCDI, the constituent indices of MCDI (SPAEI3, SSI3, SRI3, WSDI), scPDSI, and NDVI during the drought event that happened in the Contiguous United States. During the period from June 2012 to February 2013, the drought severity continued to decrease, and the extent of drought gradually narrowed from the global state to the Midwest. By October 2012, a significant decline in NDVI was observed in the central Contiguous United States, which is dominated by agricultural cultivation, suggesting that crops in this region were severely affected by the drought. In the subsequent months up to February 2013, productivity in the northern and western regions was also shown to be impacted. However, scPDSI seemed not to be successful in indicating the drought status of these regions across this period. In contrast, the drought status indicated by the MCDI and the vegetation growth status indicated by the NDVI were in better agreement. In addition, this drought event led to increased water use, and ultimately, groundwater declined due to the lack of precipitation and prolonged soil moisture deficits, which also might be the reason why the WSDI still indicated drought in the eastern part of the region in February 2013<sup>86,87</sup> . 

Figure 9 shows the spatial and temporal dynamics of MCDI, the constituent indices of MCDI (SPAEI3, SSI3, SRI3, WSDI), scPDSI, and NDVI for November 2015, January 2016, and March 2016 in South Africa. The decreasing NDVI over a wide area from November 2015 to January 2016 signified that the drought had a large impact on vegetation productivity within South Africa. By March 2016, the area with NDVI affected gradually narrowed down to parts of the eastern and central regions. However, at this time, the drought indices still indicated widespread drought conditions, especially MCDI and scPDSI. The reason for this phenomenon might be that the improvement of NDVI may result from occasional light rainfall or drought adaptation of vegetation, while the drought indices reflect a combination of available water and climatic conditions<sup>76</sup> . Due to the El Niño phenomenon, where high temperatures and moisture deficits co-existed, the drought indices were influenced by historical cumulative water deficits and thus still indicated drought conditions. In addition, despite the differences in spatial and temporal performance between the different indices, it must be recognized that all drought indices captured the characteristics of drought events well. 

## **Data availability** 

The dataset is available at https://doi.org/10.5281/zenodo.15143908. 

## **Code availability** 

The code used to synthesize results and replicate all the figures in this manuscript can be accessed from the link https://zenodo.org/records/16343702. The scripts were written in Python version 3.9.7 (https://www.python.org/). 

Received: 28 July 2025; Accepted: 13 November 2025; Published: xx xx xxxx 

## **References** 

1. Zargar, A., Sadiq, R., Naser, B. & Khan, F. I. A review of drought indices. _Environmental Reviews_ **19** , 333–349, https://doi.org/10.1139/ a11-013 (2011). 

2. Yu, H., Wang, L., Zhang, J. & Chen, Y. A global drought-aridity index: The spatiotemporal standardized precipitation evapotranspiration index. _Ecological Indicators_ **153** , https://doi.org/10.1016/j.ecolind.2023.110484 (2023). 

3. Zhang, Q. _et al_ . A new high-resolution multi-drought-index dataset for mainland China. _Earth Syst. Sci. Data_ **17** , 837–853, https:// doi.org/10.5194/essd-17-837-2025 (2025). 

4. Zhang, Y. _et al_ . Assessment of drought evolution characteristics based on a nonparametric and trivariate integrated drought index. _Journal of Hydrology_ **579** , https://doi.org/10.1016/j.jhydrol.2019.124230 (2019). 

5. Zhang, Q. _et al_ . Nonparametric Integrated Agrometeorological Drought Monitoring: Model Development and Application. _Journal of Geophysical Research: Atmospheres_ **123** , 73–88, https://doi.org/10.1002/2017jd027448 (2018). 

6. Shah, D. & Mishra, V. Integrated Drought Index (IDI) for Drought Monitoring and Assessment in India. _Water Resources Research_ **56** , https://doi.org/10.1029/2019wr026284 (2020). 

7. Rusca, M., Savelli, E., Di Baldassarre, G., Biza, A. & Messori, G. Unprecedented droughts are expected to exacerbate urban inequalities in Southern Africa. _Nat Clim Change_ **13** , 98–105, https://doi.org/10.1038/s41558-022-01546-8 (2023). 

8. Ault, T. R. On the essentials of drought in a changing climate. _Science_ **368** , 256–260, https://doi.org/10.1126/science.aaz5492 (2020). 

9. Yang, C. _et al_ . A novel comprehensive agricultural drought index accounting for precipitation, evapotranspiration, and soil moisture. _Ecological Indicators_ **154** , https://doi.org/10.1016/j.ecolind.2023.110593 (2023). 

10. Schwalm, C. R. _et al_ . Global patterns of drought recovery. _Nature_ **548** , 202-+, https://doi.org/10.1038/nature23021 (2017). 

11. Trenberth, K. E. _et al_ . Global warming and changes in drought. _Nat Clim Change_ **4** , 17–22, https://doi.org/10.1038/nclimate2067 (2013). 

12. Vicente-Serrano, S. M., Quiring, S. M., Peña-Gallardo, M., Yuan, S. & Domínguez-Castro, F. A review of environmental droughts: Increased risk under global warming? _Earth-Science Reviews_ **201** , 102953, https://doi.org/10.1016/j.earscirev.2019.102953 (2020). 

13. Vicente-Serrano, S. M., Begueria, S. & Lopez-Moreno, J. I. A Multiscalar Drought Index Sensitive to Global Warming: The Standardized Precipitation Evapotranspiration Index. _J Climate_ **23** , 1696–1718, https://doi.org/10.1175/2009jcli2909.1 (2010). 

14. AghaKouchak, A. _et al_ . Remote sensing of drought: Progress, challenges and opportunities. _Reviews of Geophysics_ **53** , 452–480, https://doi.org/10.1002/2014rg000456 (2015). 

15. Hao, Z. & Singh, V. P. Drought characterization from a multivariate perspective: A review. _Journal of Hydrology_ **527** , 668–678, https://doi.org/10.1016/j.jhydrol.2015.05.031 (2015). 

16. McKee, T. B., Doesken, N. J. & Kleist, J. in _Proceedings of the 8th Conference on Applied Climatology_ . 179–183 (California). 

17. Hao, Z. & AghaKouchak, A. Multivariate Standardized Drought Index: A parametric multi-index model. _Advances in Water Resources_ **57** , 12–18, https://doi.org/10.1016/j.advwatres.2013.03.009 (2013). 

18. Vicente-Serrano, S. _et al_ . Accurate Computation of a Streamflow Drought Index. _Journal of Hydrologic Engineering_ **17** , 318–332, https://doi.org/10.1061/(ASCE)HE.1943-5584.0000433 (2012). 

19. AghaKouchak, A. & Hao, Z. A Nonparametric Multivariate Multi-Index Drought Monitoring Framework. _Journal of Hydrometeorology_ **15** , 89–101, https://doi.org/10.1175/jhm-d-12-0160.1 (2014). 

Scientific **Data** | _(2025) 12:2035_ | https://doi.org/10.1038/s41597-025-06320-x 

12 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

20. Yang, B. _et al_ . Combined multivariate drought index for drought assessment in China from 2003 to 2020. _Agricultural Water Management_ **281** , https://doi.org/10.1016/j.agwat.2023.108241 (2023). 

21. Faiz, M. A. _et al_ . A composite drought index developed for detecting large-scale drought characteristics. _Journal of Hydrology_ **605** , https://doi.org/10.1016/j.jhydrol.2021.127308 (2022). 

22. Alahacoon, N. & Edirisinghe, M. A comprehensive assessment of remote sensing and traditional based drought monitoring indices at global and regional scale. _Geomat Nat Haz Risk_ **13** , 762–799, https://doi.org/10.1080/19475705.2022.2044394 (2022). 

23. Sadiqi, S. S. J., Hong, E.-M., Nam, W.-H. & Kim, T. Review: An integrated framework for understanding ecological drought and drought resistance. _Science of the Total Environment_ **846** , https://doi.org/10.1016/j.scitotenv.2022.157477 (2022). 

24. Zhang, Z. & Li, X. The resilience of ecosystems to drought. _Global Change Biology_ **29** , 3517–3518, https://doi.org/10.1111/gcb.16724 (2023). 

25. Wei, X. _et al_ . Global assessment of lagged and cumulative effects of drought on grassland gross primary production. _Ecological Indicators_ **136** , https://doi.org/10.1016/j.ecolind.2022.108646 (2022). 

26. Xu, S. _et al_ . Evaluating the cumulative and time-lag effects of vegetation response to drought in Central Asia under changing environments. _Journal of Hydrology_ **627** , https://doi.org/10.1016/j.jhydrol.2023.130455 (2023). 

27. Forzieri, G., Dakos, V., McDowell, N. G., Ramdane, A. & Cescatti, A. Emerging signals of declining forest resilience under climate change. _Nature_ **608** , 534–539, https://doi.org/10.1038/s41586-022-04959-9 (2022). 

28. Seddon, A. W. R., Macias-Fauria, M., Long, P. R., Benz, D. & Willis, K. J. Sensitivity of global terrestrial ecosystems to climate variability. _Nature_ **531** , 229–232, https://doi.org/10.1038/nature16986 (2016). 

29. Jha, S., Das, J. & Goyal, M. K. Assessment of Risk and Resilience of Terrestrial Ecosystem Productivity under the Influence of Extreme Climatic Conditions over India. _Scientific Reports_ **9** , 18923, https://doi.org/10.1038/s41598-019-55067-0 (2019). 

30. Yuan, M. _et al_ . A new multivariate composite drought index considering the lag time and the cumulative effects of drought. _Journal of Hydrology_ **653** , 132757, https://doi.org/10.1016/j.jhydrol.2025.132757 (2025). 

31. Tian, L., Zhang, B. & Wu, P. A global drought dataset of standardized moisture anomaly index incorporating snow dynamics (SZIsnow) and its application in identifying large-scale drought events. _Earth Syst. Sci. Data_ **14** , 2259–2278, https://doi.org/10.5194/ essd-14-2259-2022 (2022). 

32. van der Schrier, G., Barichivich, J., Briffa, K. R. & Jones, P. D. A scPDSI-based global data set of dry and wet spells for 1901–2009. _Journal of Geophysical Research: Atmospheres_ **118** , 4025–4048, https://doi.org/10.1002/jgrd.50355 (2013). 

33. Barichivich, J., Osborn, T., Harris, I., van der Schrier, G. & Jones, P. Monitoring global drought using the self-calibrating Palmer Drought Severity Index. _Bulletin of the American Meteorological Society_ **104** , S66–S67, https://doi.org/10.1175/bams-d-23-0090.1 (2023). 

34. Wells, N., Goddard, S. & Hayes, M. J. A self-calibrating Palmer Drought Severity Index. _J Climate_ **17** , 2335–2351, 10.1175/1520-0442 (2004)017<2335:ASPDSI>2.0.CO;2 (2004). 

35. Beguería, S., Vicente-Serrano, S. M. & Angulo-Martínez, M. A Multiscalar Global Drought Dataset: The SPEIbase: A New Gridded Product for the Analysis of Drought Variability and Impacts. _Bulletin of the American Meteorological Society_ **91** , 1351–1356, https:// doi.org/10.1175/2010BAMS2988.1 (2010). 

36. Peng, S., Ding, Y., Liu, W. & Li, Z. 1 km monthly temperature and precipitation dataset for China from 1901 to 2017. _Earth Syst. Sci. Data_ **11** , 1931–1946, https://doi.org/10.5194/essd-11-1931-2019 (2019). 

37. Wang, Q. _et al_ . A multi-scale daily SPEI dataset for drought characterization at observation stations over mainland China from 1961 to 2018. _Earth Syst. Sci. Data_ **13** , 331–341, https://doi.org/10.5194/essd-13-331-2021 (2021). 

38. Guttman, N. B. Accepting the standardized precipitation index: a calculation algorithm. _JAWRA Journal of the American Water Resources Association_ **35** , 311–322, https://doi.org/10.1111/j.1752-1688.1999.tb03592.x (1999). 

39. Beck, H. E. _et al_ . MSWEP V2 Global 3-Hourly 0.1° Precipitation: Methodology and Quantitative Assessment. _Bulletin of the American Meteorological Society_ **100** , 473–500, https://doi.org/10.1175/BAMS-D-17-0138.1 (2019). 

40. Beck, H. E. _et al_ . Global-scale evaluation of 22 precipitation datasets using gauge observations and hydrological modeling. _Hydrol. Earth Syst. Sci._ **21** , 6201–6217, https://doi.org/10.5194/hess-21-6201-2017 (2017). 

41. Beck, H. E. _et al_ . Daily evaluation of 26 precipitation datasets using Stage-IV gauge-radar data for the CONUS. _Hydrol. Earth Syst. Sci._ **23** , 207–224, https://doi.org/10.5194/hess-23-207-2019 (2019). 

42. Miralles, D. G. _et al_ . GLEAM4: global land evaporation and soil moisture dataset at 0.1 resolution from 1980 to near present. _Scientific Data_ **12** , 416, https://doi.org/10.1038/s41597-025-04610-y (2025). 

43. Liu, L. _et al_ . Soil moisture dominates dryness stress on ecosystem production globally. _Nature Communications_ **11** , https://doi.org/ 10.1038/s41467-020-18631-1 (2020). 

44. Yu, T. _et al_ . Interannual and seasonal relationships between photosynthesis and summer soil moisture in the Ili River basin, Xinjiang, 

   - 2000–2018. _Science of The Total Environment_ **856** , https://doi.org/10.1016/j.scitotenv.2022.159191 (2023). 

45. Ghiggi, G., Humphrey, V., Seneviratne, S. I. & Gudmundsson, L. GRUN: an observation-based global gridded runoff dataset from 1902 to 2014. _Earth Syst. Sci. Data_ **11** , 1655–1674, https://doi.org/10.5194/essd-11-1655-2019 (2019). 

46. Xue, Y. Y., Liang, H. B., Zhang, B. Q. & He, C. S. Vegetation restoration dominated the variation of water use efficiency in China. _Journal of Hydrology_ **612** , https://doi.org/10.1016/j.jhydrol.2022.128257 (2022). 

47. Zhao, A., Wang, D., Xiang, K. & Zhang, A. Vegetation photosynthesis changes and response to water constraints in the Yangtze River and Yellow River Basin, China. _Ecological Indicators_ **143** , https://doi.org/10.1016/j.ecolind.2022.109331 (2022). 

48. Li, F., Kusche, J., Chao, N., Wang, Z. & Löcher, A. Long‐Term (1979‐Present) Total Water Storage Anomalies Over the Global Land Derived by Reconstructing GRACE Data. _Geophysical Research Letters_ **48** , https://doi.org/10.1029/2021gl093492 (2021). 

49. Humphrey, V. & Gudmundsson, L. GRACE-REC: a reconstruction of climate-driven water storage changes over the last century. _Earth System Science Data_ **11** , 1153–1170, https://doi.org/10.5194/essd-11-1153-2019 (2019). 

50. Vergni, L., Vinci, A. & Todisco, F. Effectiveness of the new standardized deficit distance index and other meteorological indices in the assessment of agricultural drought impacts in central Italy. _Journal of Hydrology_ **603** , https://doi.org/10.1016/ j.jhydrol.2021.126986 (2021). 

51. Wang, H., Chen, Y., Pan, Y., Chen, Z. & Ren, Z. Assessment of candidate distributions for SPI/SPEI and sensitivity of drought to climatic variables in China. _Int J Climatol_ **39** , 4392–4412, https://doi.org/10.1002/joc.6081 (2019). 

52. Thomas, A. C., Reager, J. T., Famiglietti, J. S. & Rodell, M. A GRACE-based water storage deficit approach for hydrological drought characterization. _Geophysical Research Letters_ **41** , 1537–1545, https://doi.org/10.1002/2014GL059323 (2014). 

53. Sinha, D., Syed, T. H., Famiglietti, J. S., Reager, J. T. & Thomas, R. C. Characterizing Drought in India Using GRACE Observations of Terrestrial Water Storage Deficit. _Journal of Hydrometeorology_ **18** , 381–396, https://doi.org/10.1175/JHM-D-16-0047.1 (2017). 

54. Khorrami, B. & Gunduz, O. An enhanced water storage deficit index (EWSDI) for drought detection using GRACE gravity estimates. _Journal of Hydrology_ **603** , 126812, https://doi.org/10.1016/j.jhydrol.2021.126812 (2021). 

55. Gringorten, I. I. A plotting rule for extreme probability paper. _Journal of Geophysical Research (1896-1977)_ **68** , 813–814, https://doi.org/ 10.1029/JZ068i003p00813 (1963). 

56. Li, M. _et al_ . Spatiotemporally consistent global dataset of the GIMMS Normalized Difference Vegetation Index (PKU GIMMS NDVI) from 1982 to 2022. _Earth Syst. Sci. Data_ **15** , 4181–4203, https://doi.org/10.5194/essd-15-4181-2023 (2023). 

57. Pastorello, G. _et al_ . The FLUXNET2015 dataset and the ONEFlux processing pipeline for eddy covariance data. _Scientific Data_ **7** , 225, https://doi.org/10.1038/s41597-020-0534-3 (2020). 

Scientific **Data** | _(2025) 12:2035_ | https://doi.org/10.1038/s41597-025-06320-x 

13 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

58. Nguyen, H., Wheeler, M. C., Hendon, H. H., Lim, E.-P. & Otkin, J. A. The 2019 flash droughts in subtropical eastern Australia and their association with large-scale climate drivers. _Weather Clim Extreme_ **32** , 100321, https://doi.org/10.1016/j.wace.2021.100321 (2021). 

59. Falster, G., Coats, S. & Abram, N. How unusual was Australia’s 2017–2019 Tinderbox Drought? _Weather Clim Extreme_ **46** , 100734, https://doi.org/10.1016/j.wace.2024.100734 (2024). 

60. Qiu, B., Ge, J., Guo, W., Pitman, A. J. & Mu, M. Responses of Australian Dryland Vegetation to the 2019 Heat Wave at a Subdaily Scale. _Geophysical Research Letters_ **47** , e2019GL086569, https://doi.org/10.1029/2019GL086569 (2020). 

61. Pepler, A. Record Lack of Cyclones in Southern Australia During 2019. _Geophysical Research Letters_ **47** , e2020GL088488, https://doi.org/ 10.1029/2020GL088488 (2020). 

62. Losso, A. _et al_ . Canopy dieback and recovery in Australian native forests following extreme drought. _Scientific Reports_ **12** , 21608, https://doi.org/10.1038/s41598-022-24833-y (2022). 

63. AghaKouchak, A. A baseline probabilistic drought forecasting framework using standardized soil moisture index: application to the 2012 United States drought. _Hydrol. Earth Syst. Sci._ **18** , 2485–2492, https://doi.org/10.5194/hess-18-2485-2014 (2014). 

64. PaiMazumder, D. & Done, J. M. Potential predictability sources of the 2012 U.S. drought in observations and a regional model ensemble. _Journal of Geophysical Research: Atmospheres_ **121** , 12,581–512,592, https://doi.org/10.1002/2016JD025322 (2016). 

65. Gebrechorkos, S. H. _et al_ . Global high-resolution drought indices for 1981–2022. _Earth Syst. Sci. Data_ **15** , 5449–5466, https://doi.org/ 10.5194/essd-15-5449-2023 (2023). 

66. Mbokodo, I. L. _et al_ . Heatwave Variability and Structure in South Africa during Summer Drought. _Climate_ **11** , 38, https://doi.org/ 10.3390/cli11020038 (2023). 

67. Meza, I. _et al_ . Drought risk for agricultural systems in South Africa: Drivers, spatial patterns, and implications for drought risk management. _Science of The Total Environment_ **799** , 149505, https://doi.org/10.1016/j.scitotenv.2021.149505 (2021). 

68. Wei, W. _et al_ . Comparative evaluation of drought indices for monitoring drought based on remote sensing data. _Environmental Science and Pollution Research_ **28** , 20408–20425, https://doi.org/10.1007/s11356-020-12120-0 (2021). 

69. Ding, Y. _et al_ . Attribution of meteorological, hydrological and agricultural drought propagation in different climatic regions of China. _Agricultural Water Management_ **255** , https://doi.org/10.1016/j.agwat.2021.106996 (2021). 

70. Liu, Q., Zhang, S., Zhang, H., Bai, Y. & Zhang, J. Monitoring drought using composite drought indices based on remote sensing. _Science of The Total Environment_ **711** , 134585, https://doi.org/10.1016/j.scitotenv.2019.134585 (2020). 

71. Liu, Y., Shan, F., Yue, H., Wang, X. & Fan, Y. Global analysis of the correlation and propagation among meteorological, agricultural, surface water, and groundwater droughts. _Journal of Environmental Management_ **333** , 117460, https://doi.org/10.1016/ j.jenvman.2023.117460 (2023). 

72. Zhang, A. _et al_ . A global near real-time dataset of Microwave Integrated Drought Index from the Fengyun-3 satellites. _Scientific Data_ **12** , 583, https://doi.org/10.1038/s41597-025-04935-8 (2025). 

73. Zhang, X., Duan, J., Cherubini, F. & Ma, Z. A global daily evapotranspiration deficit index dataset for quantifying drought severity from 1979 to 2022. _Scientific Data_ **10** , 824, https://doi.org/10.1038/s41597-023-02756-1 (2023). 

74. Wang, Q., Liu, X., Wang, Z., Zhao, L. & Zhang, Q.-p. Time scale selection and periodicity analysis of grassland drought monitoring index in Inner Mongolia. _Global Ecology and Conservation_ **36** , https://doi.org/10.1016/j.gecco.2022.e02138 (2022). 

75. Yuan, M. & Gao, Y. A high-resolution global drought dataset for Multivariate Composite Drought Index (MCDI) and its constituent drought indices from 1980 to 2019. _Zenodo_ https://doi.org/10.5281/zenodo.15143908 (2025). 

76. Peng, J. _et al_ . A pan-African high-resolution drought index dataset. _Earth Syst. Sci. Data_ **12** , 753–769, https://doi.org/10.5194/essd12-753-2020 (2020). 

77. Faiz, M. A. _et al_ . Drought index revisited to assess its response to vegetation in different agro-climatic zones. _Journal of Hydrology_ **614** , https://doi.org/10.1016/j.jhydrol.2022.128543 (2022). 

78. Pathak, A. A. & Dodamani, B. M. Comparison of Meteorological Drought Indices for Different Climatic Regions of an Indian River Basin. _Asia-Pac J Atmos Sci_ **56** , 563–576, https://doi.org/10.1007/s13143-019-00162-5 (2020). 

79. Liu, Y. _et al_ . On the mechanisms of two composite methods for construction of multivariate drought indices. _Science of the Total Environment_ **647** , 981–991, https://doi.org/10.1016/j.scitotenv.2018.07.273 (2019). 

80. Zhang, S. L., Yang, Y. T., Wu, X. C., Li, X. Y. & Shi, F. Z. Postdrought Recovery Time Across Global Terrestrial Ecosystems. _Journal of Geophysical Research-Biogeosciences_ **126** , https://doi.org/10.1029/2020JG005699 (2021). 

81. Luo, S., Tetzlaff, D., Smith, A. & Soulsby, C. Long-term drought effects on landscape water storage and recovery under contrasting landuses. _Journal of Hydrology_ **636** , https://doi.org/10.1016/j.jhydrol.2024.131339 (2024). 

82. Ren, P. _et al_ . Satellite monitoring reveals short-term cumulative and time-lag effect of drought and heat on autumn photosynthetic phenology in subtropical vegetation. _Environmental Research_ **239** , https://doi.org/10.1016/j.envres.2023.117364 (2023). 

83. Zhao, Z. & Wang, K. Capability of Existing Drought Indices in Reflecting Agricultural Drought in China. _Journal of Geophysical Research-Biogeosciences_ **126** , https://doi.org/10.1029/2020jg006064 (2021). 

84. Shi, X., Chen, F., Shi, M., Ding, H. & Li, Y. Construction and application of Optimized Comprehensive Drought Index based on lag time: A case study in the middle reaches of Yellow River Basin, China. _Science of the Total Environment_ **857** , https://doi.org/10.1016/ j.scitotenv.2022.159692 (2023). 

85. Khorrami, B. & Gunduz, O. Detection and analysis of drought over Turkey with remote sensing and model-based drought indices. _Geocarto International_ **37** , 12171–12193, https://doi.org/10.1080/10106049.2022.2066197 (2022). 

86. Basara, J. B. _et al_ . The evolution, propagation, and spread of flash drought in the Central United States during 2012. _Environmental Research Letters_ **14** , 084025, https://doi.org/10.1088/1748-9326/ab2cc0 (2019). 

87. Rippey, B. R. The U.S. drought of 2012. _Weather Clim Extreme_ **10** , 57–64, https://doi.org/10.1016/j.wace.2015.10.004 (2015). 

## **Acknowledgements** 

This work was supported by the Key Project of the National Natural Science Foundation of China (Grant No. 42330506), the General Program of the National Natural Science Foundation of China (Grant No. 42071054), and the International (Regional) Cooperation and Exchange Project of the National Natural Science Foundation of China (Grant No. 42361144709). 

## **author contributions** 

Mengjia Yuan: Methodology, Software, Writing-original draft, Writing-review & editing. Guojing Gan: Funding acquisition, Methodology, Writing-review & editing. Jingyi Bu: Methodology, Writing-review & editing. Yanxin Su: Writing-review & editing. Hongyu Ma: Writing-review & editing. Xianghe Liu: Writing-review & editing. Leyao Zhang: Writing-review & editing. Yongqiang Zhang: Writing-review & editing. Yanchun Gao: Conceptualization, Writing-review & editing, Supervision, Funding acquisition, Project administration. 

## **Competing interests** 

The authors declare no competing interests. 

Scientific **Data** | _(2025) 12:2035_ | https://doi.org/10.1038/s41597-025-06320-x 

14 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

## **additional information** 

**Correspondence** and requests for materials should be addressed to G.G. or Y.G. 

**Reprints and permissions information** is available at www.nature.com/reprints. 

**Publisher’s note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

**Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/. 

© The Author(s) 2025 

Scientific **Data** | _(2025) 12:2035_ | https://doi.org/10.1038/s41597-025-06320-x 

15 

