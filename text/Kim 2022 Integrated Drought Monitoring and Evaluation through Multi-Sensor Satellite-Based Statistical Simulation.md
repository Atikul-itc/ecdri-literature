**_remote sensing_** 





_Article_ 

# **Integrated Drought Monitoring and Evaluation through Multi-Sensor Satellite-Based Statistical Simulation** 

**Jong-Suk Kim**<sup>**1**</sup> **, Seo-Yeon Park**<sup>**2,**</sup> ***, Joo-Heon Lee**<sup>**2**</sup> **, Jie Chen**<sup>**1**</sup> **, Si Chen**<sup>**3**</sup> **and Tae-Woong Kim**<sup>**4**</sup> 

- 1 State Key Laboratory of Water Resources and Hydropower Engineering Science, Wuhan University, Wuhan 430072, China; jongsuk@whu.edu.cn (J.-S.K.); jiechen@whu.edu.cn (J.C.) 

- 2 Department of Civil Engineering, Joongbu University, Gyeonggi-do 10279, Korea; leejh@joongbu.ac.kr 

- 3 School of Resources and Environment, Hubei University, Wuhan 430062, China; kathryncs123@hotmail.com 

- 4 Department of Civil and Environmental Engineering, Hanyang University (ERICA), 

   - Gyeonggi-do 15588, Korea; twkim72@hanyang.ac.kr 

- Correspondence: sypark276@gmail.com 

### ��������� **�������** 

**Citation:** Kim, J.-S.; Park, S.-Y.; Lee, J.-H.; Chen, J.; Chen, S.; Kim, T.-W. Integrated Drought Monitoring and Evaluation through Multi-Sensor Satellite-Based Statistical Simulation. _Remote Sens._ **2021** , _13_ , 272. https://doi.org/10.3390/rs13020272 

Received: 20 November 2020 Accepted: 11 January 2021 Published: 14 January 2021 

**Publisher’s Note:** MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations. 



**Copyright:** © 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ 4.0/). 

**Abstract:** To proactively respond to changes in droughts, technologies are needed to properly diagnose and predict the magnitude of droughts. Drought monitoring using satellite data is essential when local hydrogeological information is not available. The characteristics of meteorological, agricultural, and hydrological droughts can be monitored with an accurate spatial resolution. In this study, a remote sensing-based integrated drought index was extracted from 849 sub-basins in Korea’s five major river basins using multi-sensor collaborative approaches and multivariate dimensional reduction models that were calculated using monthly satellite data from 2001 to 2019. Droughts that occurred in 2001 and 2014, which are representative years of severe drought since the 2000s, were evaluated using the integrated drought index. The Bayesian principal component analysis (BPCA)-based integrated drought index proposed in this study was analyzed to reflect the timing, severity, and evolutionary pattern of meteorological, agricultural, and hydrological droughts, thereby enabling a comprehensive delivery of drought information. 

**Keywords:** remote sensing; integrated drought monitoring; meteorological drought; hydrological drought; agricultural drought; Bayesian principal component analysis (BPCA); statistical simulation 

## **1. Introduction** 

Droughts, along with floods, are some of the most common and inevitable natural disasters faced by human beings [1–4]. Therefore, many researchers have been trying to monitor and predict droughts accurately, and the development of drought monitoring techniques based on satellite remote sensing (RS) data (as a representative method) has garnered special interest in recent years [4–9]. The onset and magnitude of drought in the region is still a challenge for researchers because of a lack of ground meteorological observatories [4]. However, satellite-based RS data partially solve the problem by providing information in a fast and cost-effective way. The advantage of RS-based monitoring using satellite data is that it is possible to monitor droughts in large areas and ungauged basins, and we can utilize multiple satellite imagery data to have accurate results; therefore, monitoring drought by using satellites has proven to be an efficient and reliable tool [6,10–13]. 

There are four kinds of droughts in the academic sense: meteorological, agricultural, hydrological droughts, and their socioeconomic impacts [2,14–16]. A meteorological drought is caused by a deficit through the shortage of rainfall and is mainly a short-term drought event [6]. An agricultural drought is determined based on the vitality of vegetation and the pattern of quantitative changes in soil moisture; it indicates short or medium-term drought situations [6,13]. A hydrological drought is commonly a mid or long-term drought condition; this drought identification is made based on a shortage of water resources 

_Remote Sens._ **2021** , _13_ , 272. https://doi.org/10.3390/rs13020272 

https://www.mdpi.com/journal/remotesensing 

2 of 18 

_Remote Sens._ **2021** , _13_ , 272 

required by human-environmental systems, such as river discharge, efficient water levels of dams, and reservoir storage [17]. A socioeconomic drought consists of a wide range that takes meteorological, agricultural, and hydrological droughts into account and is characterized by the temporal and spatial processes of water demand and supply [18]. 

A variety of drought indicators that help prevent disasters and reduce and allocate water resources have been developed to quantify different drought conditions, such as severity, duration, and frequency [3,5,17,19–25]. The standardized precipitation index (SPI; [19]) and the Palmer drought severity index (PDSI; [26]) are the most commonly used meteorological drought indices. The SPI standardization concept was also applied to other drought indices, such as the standardized runoff index (SRI; [20]) and standardized soil moisture index (SSI [22]). 

Because RS technology provides an alternative approach for analyzing drought events across a wide range of regions, many studies have introduced RS-based drought indices [5,7,23,24,27]. Zhang and Jia [27] proposed the microwave integrated drought index (MIDI) to monitor meteorological drought over semi-arid regions and the continental United States of America. Cunha et al. [23] calculated the normalized differences vegetation index (NDVI) and land surface temperature (LST) data to monitor the effects of drought on vegetation in real-time. Sur et al. [24] analyzed Korea’s drought conditions through a comparative analysis of the existing drought indices (SPI and PDSI) based on a satellite image-based drought index from 2004 to 2013. It was confirmed that the results of the evaporative stress index (ESI), and the energy-based water definition index (EWDI) showed high applicability for severe drought situations since 2010. Cong et al. [5] selected three widely used satellite drought indices as indicators suitable for drought monitoring in northeastern China and investigated the spatiotemporal patterns and trends of rainfall and drought; the indices were normalized monthly precipitation anomaly percentage (NPA), vegetation health index (VHI), and normalized vegetation supply water index (NVSWI). Zhang et al. [28] combined the global land data assimilation system version 2 (GLDAS-2) soil moisture data and NDVI with crop phenology data and assessed drought evolution and crop growth. Sur et al. [7] developed a new agricultural drought index called the agricultural dry condition index (ADCI) by combining various hydrometeorological variables and verified the applicability of the ADCI on the yield of paddy and arable crops in Korea. 

Through the review of previous studies, we can assume that information can be integrated from multi-sensor satellite data and multivariate analyses to effectively achieve comprehensive drought assessment goals. In addition to providing information based on different drought conditions (meteorological, agricultural, and hydrological), it is necessary to develop and apply an integrated drought index that considers complex factors that can provide comprehensive information about droughts and the required proactive response to drought situations. Inspired by this idea, our study seeks to diagnose complex droughts by using multi-sensor collaborative approaches and multivariate dimensional reduction models. In this study, we proposed an integrated drought assessment method to comprehensively convey drought information to the public and conducted statistical simulations to determine spatial sensitivity to various types of droughts to provide tailored information on local drought responses in a changing climate. 

## **2. Materials and Methods** 

## _2.1. Multi-Sensor Drought Indices_ 

## 2.1.1. Standardized Precipitation Index (SPI) 

The SPI is a drought index developed with the idea that it is initiated by a decrease in precipitation, thereby causing water shortage (compared to the relative water demand). In other words, it was developed from the above assumption that decreased precipitation has different effects on groundwater, reservoir storage, soil moisture, and river runoff. The SPI is an efficient way to calculate the impact of individual water sources on droughts by setting time units accumulated over a given period of time (over 1, 3, 6, and 12 months), and calculating the drought index by using the amount of precipitation on a time basis [19,28]. 

3 of 18 

_Remote Sens._ **2021** , _13_ , 272 

The SPI is also recommended by the World Meteorological Organization (WMO) for tracking meteorological droughts [21,25]. 

## 2.1.2. Agricultural Dry Condition Index (ADCI) 

The ADCI is an agricultural drought index that takes into account the vegetation conditions, soil moisture, and LST of the affected region. First, the vegetation condition index (VCI) is applied for vegetation analysis. Sur et al. [7] proposed the ADCI as a new agricultural drought index, which is a combination of the three indices mentioned above (SMSI, VCI, and TCI). The cause of the agricultural drought was developed based on the concept of reducing the vitality of vegetation due to the lack of soil moisture and overheating of the surface temperature caused by high temperatures, developing into agricultural drought as this phenomenon continues. The ADCI can be calculated by using the Equation (1) given below: 



The VCI is a suitable index for agricultural drought monitoring, such as temporal and spatial vegetation changes and the onset and intensity of drought [29,30]. Kogan [29] developed the VCI, which was standardized using the maximum and minimum values of the NDVI developed based on the notion that droughts do not provide normal water supply to plants (Equation (2)). 



where _NDVImin_ and _NDVImax_ represent the minimum and maximum values of NDVI for the entire period of the pixel. The following is the LST-related index, called the temperature condition index (TCI), which is an index developed by Kogan [29] based on the fact that LST affects the stress of vegetation and is one of the drought factors that affect soil moisture. The TCI is a standard LST that uses the maximum and minimum LST values and as shown in the following equation (Equation (3)). 



Finally, soil moisture needs to be considered for determining the ADCI. The soil moisture saturation index (SMSI) assumes that soil moisture is directly proportional to thermal inertia (TI). One of TI’s simple approximations is the apparent thermal inertia (ATI), which can be derived in Equation (4); note that we assume that the solar energy is uniform. 



where _α_ is the land surface albedo and _LSTday_ and _LSTnight_ are the surface temperatures during day and night, respectively. The SMSI can be calculated using the ATI, as shown in the following equation (Equation (5)). 



## 2.1.3. Water Budget-Based Drought Index (WBDI) 

The water budget-based drought index (WBDI), which was proposed by Sur et al. [18], was developed by adopting the water balance perspective and by using precipitation and evaporation as input variables. The evaporation of water balance is caused primarily by changing the state of water, which is achieved by changing the temperature [31]. The WBDI 

4 of 18 

_Remote Sens._ **2021** , _13_ , 272 

is defined as the difference between precipitation and evaporation as surface runoff and sub-surface runoff in the water budget equation, as given below (Equation (6)): 



where _P_ is the precipitation (mm), _E_ is actual evaporation (mm), _dS_ is soil moisture change (mm), and _R_ is the potential runoff (mm). The above results are treated as possible runoff in the basin and expressed in an index, as given below (Equation (6)): 



where _z_ denotes the standardization. Instead of monitoring the current precipitation and drought conditions through evaporation, the WBDI, estimated by using the water balance formula, defines a hydrological drought through potential (near future) runoff, thereby adopting a short-term prognosis approach. 

## _2.2. Study Area and Remote Sensing Data_ 

In this study, we used the moderate resolution imaging spectroradiometer (MODIS), precipitation estimation from remotely sensed information using an artificial neural network climate data record (PERSIANN-CDR), and global precipitation measurement (GPM) integrated multi-satellite retrievals for GPM (GPM IMERG) to calculate various drought indices. Through the MODIS satellite, the LST (MOD11A1), NDVI (MOD13A3), actual evapotranspiration (AET; MOD16A2), and albedo (MCD43B2) data from 2001 to 2019 were collected (Table 1). To obtain the precipitation data, we used the PERSIANN-CDR data from 1983 to 1997 that was generated by the center for hydrometeorology and remote sensing (CHRS) at the University of California in Irvine; the data were obtained before the tropical rainfall measuring mission (TRMM). The TRMM data from 1998 were utilized, and among many data, the gridded TRMM3B42 data were collected until 2014 (at the end of TRMM’s life), which was provided by the National Aeronautics and Space Administration (NASA) [32]. Following 2014, we used data from GPM IMERG that obtained data until 2019 to calculate the meteorological drought index [33]. Among the GPM IMERG data, the data after the last four months of the calibration were used to enhance the reliability of the precipitation data. Due to the different spatial and time resolutions of the collected data, the spatial resolution was set at 1 _×_ 1 km and the time resolution was considered to be monthly, which is consistently reprocessed. The main areas of this study were the five major rivers of the Korean Peninsula, and we analyzed 849 sub-basins (Figure 1). 

**Table 1.** Remote sensing (RS) data used in this study. 

||**Product**||**Resolution**|**Data Period**|
|---|---|---|---|---|
||MOD11A1|Land Surface<br>Temperature|1 km, daily||
|MODIS|MOD13A3|Vegetation Indices|1 km, monthly|2001–2019|
||MOD16A2|Evapotranspiration|0.5 km, 8 days||
||MCD43B2|Albedo|1 km, 8 days||
|PERSIANN-CDR|PERSIANN-CDR|Precipitation|25<sup>_◦_</sup>, daily|1983–1997|
|TRMM|TRMM3B42|Precipitation|25<sup>_◦_</sup>, 3 h|1998–2014|
|GPM|GPM IMERG|Precipitation|10<sup>_◦_</sup>, 30 min|2015–2019|



5 of 18 

_Remote Sens._ **2021** , _13_ , 272 



**Figure 1.** Geographical location of the five major river basins and the 849 sub-basins in Korea. 

_2.3. Integrated Drought Monitoring with Multi-Sensor Based Statistical Simulations_ 

The types of RS data, mainly used for drought monitoring, depend on the type of satellite used; however, data such as precipitation, vegetation, surface temperature, soil moisture, and evaporation are mostly used. The data can be used individually. However, drought phenomena may not be sufficient for drought analysis based on a single indicator because it is related to a number of variables [34]. However, it may be more useful to combine information in the form of an appropriate drought index for more accurate monitoring of complex drought phenomena. 

Hao and AghKouchak [23,34] proposed the multivariate standardized drought index (MSDI) based on a copula distribution or nonparametric joint distribution for a bivariate model of precipitation and soil moisture. However, with recent advances in technology, the size and complexity of data tend to increase. Such complexity makes it difficult to detect the dependence between the response variable and covariates because of the enormous number of available covariates [35]. To resolve these problems, an approach to reducing the number of covariates (through dimension reduction) is being used. Principal component analysis (PCA) is a tool that is commonly used for dimension reduction [36] and is a feature transformation method that directly transforms the variables (in dimension reduction methods) without losing much of the data’s inherent attribution information. In this study, for the three different multi-variables acquired from the satellite data, an integrated drought index is calculated through the application of the Bayesian PCA (BPCA; [37,38]) and intentionally biased bootstrap (IBB; [39]) simulation for characterizing three aspects of meteorological (using SPI), agricultural (using ADCI), and hydrological (using WBDI) droughts. The BPCA approach can <mark>estimate the intrinsic dimensionality of the multi-</mark> dimensional dataset with missing data, which is suitable for application to satellite data, and has been evaluated as an accurate and robust model [37,38,40]. The BPCA analysis is performed by using the following three procedures: principal component (PC) regression, Bayesian estimation, and an expectation-maximization (EM)-like repetitive algorithm [38]. 

6 of 18 

_Remote Sens._ **2021** , _13_ , 272 

The IBB a <mark>pp</mark> lied for statistical simulation of drou <mark>g</mark> ht indices is a kind of wei <mark>g</mark> hted <mark>bootstrap that follows constraints that are designed to select resampling probabilities and conditionally applied to data; this helps to improve the statistical performance and minimizes the distance of weighted distributions [39,41]. This study employed the IBB to evaluate regional drought changes in meteorological (SPI), agricultural (ADCI), and hydrological (WBDI) droughts and analyzed the relative sensitivity of each drought index to the RS-based integrated drought index (RSIDI) calculated by using the BPCA (Figure 2)</mark> . <mark>The IBB applied in this study is described as foll</mark> ows. 





**Figure 2.** Procedure of intentionally biased bootstrap (IBB) analysis for integrated drought management. 

The IBB simulation re-sam <mark>p</mark> les the observations _Xi_ to _n_ re <mark>p</mark> lacement (e. <mark>g</mark> ., bootstra <mark>p</mark> - <mark>p</mark> in <mark>g</mark> ) b <mark>y</mark> intentionall <mark>y</mark> increasin <mark>g</mark> or decreasin <mark>g</mark> the data b <mark>y</mark> as much as _δµ_ . The data _Xi_ are increasin <mark>g</mark> l <mark>y</mark> ordered b <mark>y</mark> assi <mark>g</mark> nin <mark>g</mark> different wei <mark>g</mark> hts _Wi,n_ accordin <mark>g</mark> to the ma <mark>g</mark> nitudes of <mark>the observations, as given below:</mark> 



where _i_ = 1, 2, 3, . . . , _n_ , and the data matrix is rearranged in the same order as the ordered _<mark>X</mark> i_ <mark>. The assigned weight</mark> _<mark>W</mark> i,n_ <mark>represents the probability of selection for</mark> _<mark>X</mark> i_ <mark>data in the IBB simulation. The intentional change of increase or decrease (</mark> _<mark>δ</mark> µ_ <mark>) can be calculated as given in Equation (9).</mark> 





7 of 18 

_Remote Sens._ **2021** , _13_ , 272 

Equation (9) can be generalized with a weight order ( _r_ ) as Equation (11). 



The selection of the weight order ( _r_ ) can be performed by using the self-organizing migrating algorithm (SOMA; [42]) with the following objective function (Equation (12)): 



Note that if _r_ < 0, then _δµ_ ( _r_ ) < 0, which implies a drier state, and if _r_ > 0, then _δµ_ ( _r_ ) > 0, which implies a wetter state. When _r_ < 0, lower values indicating the dry state are resampled more frequently than higher values indicating the humid state, causing _δµ_ ( _r_ ) to decrease. In addition, to objectively determine the accuracy of drought monitoring using three satellite-based drought indices, this study conducted a receiver operation characteristics (ROC) analysis. The ROC analysis was performed to evaluate the validity of the RSIDI calculations using the three drought indices (SPI, ADCI, and WBDI). The range of drought indices used in this study is given in Table 2. 

**Table 2.** Range of the drought indices used in this study. 

|**Drought Condition**|**SPI**|**ADCI**|**WBDI**|**RSIDI**|
|---|---|---|---|---|
|Normal|>0|>40|>0|>0|
|Attention|_−_1.0–0|30–40|0–_−_0.5|_−_1.0–0|
|Caution|_−_1.0–_−_1.5|20–30|_−_0.5–_−_1.0|_−_1.0–_−_1.5|
|Alert|_−_1.5–_−_2.0|10–20|_−_1.0–_−_1.5|_−_1.5–_−_2.0|
|Serious|<_−_2.0|0~10|<_−_1.5|<_−_2.0|



## **3. Results** 

In this study, the RSIDI was extracted for 849 sub-basins over the five major Korean river basins using a BPCA-based combination model for the three drought indices for 2001–2019. As a result of the evaluation of the proportion of variation (POV) of the three drought indices by region, the BPCA-based RSIDI explained the average POV (68.9%) of the 849 sub-basins (Han River basin: 68.1%, Nakdong River basin: 68.7%, Geum River basin: 71.3%, Youngsang River basin: 71.7%, and Sumjin River basin: 71.0%), showing a high POV, especially in the southern part of the country. In addition, the calculated RSIDI showed a relatively high correlation with SPI (median: 0.96) and WBDI (median: 0.96). In the case of the ADCI (maximum: 0.91, median: 0.53), the correlation with RSIDI was broad in the region and showed a relatively weak correlation in some areas of the Han and Nadkong River basins; however, on an average, the correlation was 0.53 ( _p_ -value < 0.001) in 849 sub-basins, indicating that the RSIDI can provide robust and comprehensive integrated drought information by maintaining the inherent characteristics of the three drought indices (Figure 3). By resolving the system equations for each drought index, it has been shown that the relative contribution of the RSIDI to each time-series can be assessed. Figure 4 illustrates the relative contribution of each drought index to the Gojicheon stream (#10011) of the Han River basin. 

In the following section, the droughts in 2001 and 2014, which are the representative severe drought years of severe droughts that have occurred since the 2000s, were assessed using the RSIDI produced by multi-sensor satellite data and multivariate analysis. The application of integrated drought monitoring based on satellite data was evaluated through spatial-temporal variability analysis between the RSIDI and other drought indices using the ROC analysis to test the accuracy of the models. In addition, the onset, intensity, and evolution patterns of droughts were compared to each drought index, and the applicability of the RSIDI was evaluated through an IBB simulation. 

8 of 18 

_Remote Sens._ **2021** , _13_ , 272 



**Figure 3.** Results of correlation analysis with RS-based integrated drought index (RSIDI) through Bayesian PCA (BPCA); ( **a** ) SPI (standardized precipitation index), ( **b** ) ADCI (agricultural dry condition index), and ( **c** ) WBDI (water budget-based drought index). The lower panel in the figure results from the analysis of the correlation of 849 sub-basins summarized in the boxplot and is illustrated by each applied drought index namely, SPI, ADCI, and WBDI. 

9 of 18 

_Remote Sens._ **2021** , _13_ , 272 





**Figure 4.** Time series of integrated drought index (IDI) for 2001–2019 in the Gojicheon stream in the Han River basin. ( **a** ) IDI index and ( **b** ) relative contribution evaluation. 

## _3.1. Drought Impact Assessment and Drought Monitoring_ 

The RSIDI was evaluated for the 2001 drought (Figures 5 and 6). The severe spring drought in 2001 began in the fall of 2000 and lasted until the spring of 2001. In spring, when the agricultural water demand was the highest due to the rice planting, the supply of agricultural water was insufficient, causing serious agricultural damages. In most parts of the Korean Peninsula, less than 50% of the average annual rainfall was recorded, and in some areas, only 10 to 30% of the average annual rainfall resulted in the most extensive agricultural drought damage in June [43]. The drought that occurred in 2001 was mostly resolved after more than 150 mm of rainfall since mid-June. 

The SPI and WBDI illustrate the drought from April to May was a serious event, and the drought centered in the central region since September also appears to be approaching the serious stage (Figure 5). The ROC analysis between the RSIDI and three drought indices also showed that the WBDI had the highest with 0.90, followed by SPI at 0.78, and ADCI at 0.65. For ADCI, the observed indicators showed significant spatial variation compared to the other drought indices, and in the 2000 drought, the effects of changes in the SMSI resulted in a weaker or earlier drought peak than those observed in cases of other drought indices (Figure 6). These features appear to be more sensitive to short-term droughts as the ADCI applied in this study was used only for the surface soil moisture. 

~~10 of 1~~ 8 

_~~Remote Sens.~~_ **~~2021~~** ~~,~~ _~~13~~_ ~~, 272~~ 



**Figure 5.** Spatial change of each drought index: SPI, ADCI, WBDI, and IDI (integrated drought index) for the 2001 drought. 



**Figure 6.** Spatial change of each drought index: SMSI (soil moisture saturation index), VCI (vegetation condition index), TCI (temperature condition index), and ADCI for the 2001 drought. 

Figures 7 and 8 show the results of the evaluation of the 2014 drought. In 2014, a drought occurred around the Han River basin; in the same year, the Gangwon Province had 70% of the average annual rainfall and the Gyeonggi Province area around Seoul had 59%, 

11 of 18 

_Remote Sens._ **2021** , _13_ , 272 

which was less compared to the previous years’ average annual rainfall. In particular, in 2014, a dry monsoon phenomenon occurred in which a drought that began in spring (due to the El Niño phenomenon) continued to cause no rainfall or a significantly lower amount of rainfall [44]. The rainfall between June 2014 and July 2014 was 48% (compared to the average in the past years), and the national water storage level also dropped significantly to 64% over the previous year. In August, the average water level of multi-purpose dams in Korea was only 36.1%. The droughts lasted until 2015, resulting in less than 70% of the average rainfall, and the hydrological droughts, with reservoirs in many multipurpose dams, reached dangerous levels [45]. Similar to the results of 2001, the RSIDI obtained could effectively describe the time and spatial occurrence patterns of the SPI and the WBDI, while the ADCI was analyzed to have delayed drought due to changes in SMSI. The ROC statistical analysis also confirmed that WBDI was highest and ADCI was relatively low in 2014 (SPI: 0.81, ADCI: 0.61, WBDI: 0.88). Through evaluation of past droughts, the RSIDI explained the three drought characteristics (meteorological, agricultural, and hydrological) well and confirmed the applicability of the integrated drought index through ROC analysis. 



**Figure 7.** Spatial change of each drought index: SPI (standardized precipitation index), ADCI (agricultural dry condition index), WBDI (water budget-based drought index), and IDI (integrated drought index) for the 2014 drought. 

12 of 18 

_Remote Sens._ **2021** , _13_ , 272 





**Figure 8.** Spatial change of each drought index: SMSI, VCI, TCI, and ADCI for the 2014 drought. 

## _3.2. Drought Transition Evaluation by Statistical Simulations_ 

This study simulated the impact on the spatiotemporal distribution of different drought conditions, such as agricultural and hydrological perspectives, by altering the intended difference of _δµ_ ( _r_ ) (Equat <mark>ion (11)) of the meteorological drought index (SPI)</mark> 1000 times to represent the changes in SPI. As _δµ_ ( _r_ ) <mark>was intentionally changed, all the</mark> sub-basins expe <mark>rienced various changes in their ADCI and WBDI. Figure 9 shows that</mark> statistical simul <mark>ations indicate that the changes in the state of agricultural (ADCI) and</mark> hydrological (W <mark>BDI) droughts correspond to the changes in meteorological drought (SPI).</mark> In addition, the <mark>results of the IBB simulation for up to three months of a lagged analysis</mark> were shown in <mark>Figure 10. Natural disasters, including droughts, are managed in four</mark> stages (Attentio <mark>n, Caution, Alert, and Serious) in Korea. In this study, the changes in other</mark> drought conditi <mark>ons were identif</mark> i <mark>ed by intentionally changing the meteorological drought</mark> condition by using a IBB simulation. 

First, when <mark>the meteorological drought (SPI) conditions were simulated from a stage</mark> of Normal to a <mark>stage of Attention (Figures 9a and 10a), the ADCI conditions, except for</mark> some parts of th <mark>e Han River basin, showed a stage of Attention (96.6%, 820 out of 849 sub-</mark> basins). Accord <mark>ing to the results of the one-month delay, the ADCI status in parts of the</mark> Han and Nakd <mark>ong River basins changed to Normal; however, 77.1% of the entire basin</mark> (45.8% of the t <mark>wo-month delay) was still in a stage of Attention. Over time, the ADCI</mark> conditions have <mark>shifted from a state of Attention to Normal in the southwestern part of the</mark> Han, Youngsan <mark>g River, and Sumjin River basins. Even if the SPI conditions are simulated</mark> from the Norm <mark>al stage to a stage of Attention, the results of the SPI are similar to those</mark> of time and space, and there are many sub-basins that are converted to the Normal stage over time. When the meteorological drought (SPI) conditions were simulated from the Normal stage to a stage of Caution (Figures 9b and 10b), excluding the parts of the Han River basin, more than 98.6% showed the ADCI to be in the Attention stage and 15.9% showed a stage of Caution. According to the results of the one-month delay, the ADCI in the northern parts of the Han River was still in a state of Caution; however, 88.5% of the 

13 of 18 

_Remote Sens._ **2021** , _13_ , 272 

<mark>entire basin was in the stage of Attention. Over time, the ADCI conditions shifted from a state of Attention to Normal in the southwestern parts of the Han, Youngsan, and Sumjin River basins. Although the mid</mark> - <mark>term drought (SPI6) was simulated from a Normal stage to a stage of Attention, changes in the spatiotemporal pattern of the ADCI were similar to the results obtained for SPI3, in which the scope of Attention conditions was reduced, and the number of s</mark> ub-basins converted to “Normal” over time increased in the southern parts of the country. 



**Figure 9.** Drought condition changes in intentionally biased bootstrap (IBB) simulation. ( **a** ) Case I (SPInormal _→_ SPIAttention) and ( **b** ) Case II (SPInormal _→_ SPICaution). The simulation results for the five basin areas are provided in the boxplot, and the results for the change in drought conditions are indicated in color in the map. 

For WBDI, when the SPI drought conditions were simulated from Normal to a stage of <mark>Attention, the WBDI conditions, excluding the Han River basins, showed a stage o</mark> f <mark>Alert (99.2%, 842 out of 849 sub-basins). As a result of the one-month delay, the WBD</mark> I <mark>status shifted from 75.7% of the total basin to a state of Attention, but 50.7% of the Han River basin and some areas of the Geum and Youngsan River basins were still in Caution levels. Over time, the WBDI conditions tended to shift from a state of Attention to Norma</mark> l <mark>in the southwestern parts of the Han and Geum River basins. The SPI drought conditions were simulated from Normal to Caution; more than 93.8% of the total basins showed their WBDI in a stage of Caution. Over time, the WBDI status shifted to a Normal state around the southwestern Han and Geum River basins.</mark> 

<mark>When the drought conditions of the RSID</mark> I were simulated from Normal to Attention (Figure 11a), in all three drought indices (SPI, ADCI, and WBDI), the drought conditions shifted to a state of Attention, confirming that the RSIDI expressed the overall drought in space effectively. If drought conditions were simulated from Normal to Caution, the SPI results showed that 78.6% of the total basins were in the same state as drought conditions in the RSIDI. However, we inferred that the Han River basin was relatively insensitive due to its status of Attention. Compared to the drought conditions of the SPI, the drought conditions of the ADCI and WBDI were shown to be mitigated by one level in the Han River and some areas of the Nakdong River, and the spatial conditions changed in the two drought indices (ADCI and WBDI) were similar. 

14 of 18 

_Remote Sens._ **2021** , _13_ , 272 



**Figure 10.** Drought condition changes in IBB simulation of ADCI and WBDI. ( **a** ) Case I (SPInormal _→_ SPIAttention) and ( **b** ) Case II (SPInormal _→_ SPICaution). The simulation results for the five basin areas for up to three months are colored in the map. 

15 of 18 

_Remote Sens._ **2021** , _13_ , 272 





**Figure 11.** Drought condition changes in IBB simulation. ( **a** ) Case I (IDInormal _→_ IDIAttention) and ( **b** ) Case II (IDInormal _→_ IDICaution). The simulation results for the five basin areas for up to three months are colored in the map. 

## **4. Discussion and Conclusions** 

<mark>As climate change accelerates due to global warming, changes in hydrological cycles occur signif</mark> i <mark>cantly, and water use and prediction of water resources may become diff</mark> i <mark>cult</mark> . <mark>In particular, in Korea, chronic drought has occurred continuously since the 1990s during the transition from winter to spring [46]. To cope with these droughts, technologies to identify and predict the magnitude of spatiotemporal droughts are required. Drought monitoring using satellite data will be essential to secure spatial resolution for accurate and spatial droughts when ground-based hydrometeorological data are not available, as well as monitoring the different characteristics of meteorological, agricultural, and hydrological drou</mark> ghts. 

<mark>Korea’s drought-related affairs are mainly handled by the Korea Meteorological Administration (KMA), Ministry of Agriculture, Food and Rural Affairs (MAFRA), Ministry of Environment (MOE), Ministry of Land, Infrastructure, and Transport (MOLIT), and the Ministry of Public Safety and Security (MPSS) [47]. The KMA diagnoses precipitation and drought in drought areas by assessing the SPI and PDSI and provides this information to the local governments. The MAFRA analyzes agricultural water through the soil moisture index (SMI), reservoir drought index (RDI), and integrated agricultural drought index. The MOLIT monitors dam water; the MOE monitors emergency water resources and water</mark> quality according to the drought stage and implements the appropriate countermeasures. The MPSS oversees the drought situation when it becomes extreme. However, some point out that the current drought measurement indices of different agencies are different in drought management, causing confusion and making it difficult to respond to drought 

16 of 18 

_Remote Sens._ **2021** , _13_ , 272 

proactively. Different ministries have different standards for determining the degree of drought. Additionally, it is not sufficient for a single drought indicator to characterize all the complex drought evolution processes [22]. The development and application of an integrated drought index are necessary to take into account the complex factors related to water use, such as the meteorological, agricultural, and hydrological perspectives. Thus, this study proposed an RS-based integrated drought index that was extracted from 849 subbasins in Korea’s five major river basins using multi-sensor collaborative approaches and multivariate dimensional reduction models, calculated through monthly satellite data. Droughts in 2001 and 2014, representative years of severe drought since the 2000s, were evaluated using the integrated drought index, and statistical simulations were used to diagnose the sensitivity and transition of drought. The BPCA-based integrated drought index proposed in this study was analyzed to reflect the timing, severity, and evolutionary pattern of meteorological, agricultural and hydrological droughts, enabling comprehensive delivery of drought information. Although the results relied on limited observations, it is expected that drought hotspot analyses and statistical simulations using IBB and BPCAbased RSIDI will identify the drought characteristics of the sub-basin, thereby promoting their use in preemptive drought response through drought prediction and early warning. 

Drought monitoring and accurate drought forecasting are still the main challenges in a relatively changing environment that has a long lead-time and natural and artificial factors. Therefore, future works to improve drought monitoring and prediction require further research, such as high-quality data assimilation, improving model development through major processes related to droughts, selecting or predicting optimal ensembles, and hybrid drought forecasting. 

**Author Contributions:** Conceptualization, Resources, Formal analysis, Writing—original draft, J.-S.K. and S.-Y.P.; Conceptualization, Methodology, Writing—review & editing, J.-H.L.; Writing—review & editing, J.C., S.C. and T.-W.K. All authors have read and agreed to the published version of the manuscript. 

**Funding:** This research was supported by the Korea Environment Industry & Technology Institute (KEITI) through the Water Management Research Program, which is funded by the Korea Ministry of Environment (MOE) (Grant No. 79616). We also appreciate the support of the State Key Laboratory of Water Resources and Hydropower Engineering Science, Wuhan University. 

**Conflicts of Interest:** The authors declare no conflict of interest. 

## **References** 

1. Zarafshani, K.; Sharafi, L.; Azadi, H.; Van Passel, S. Vulnerability Assessment Models to Drought: Toward a Conceptual Framework. _Sustainability_ **2016** , _8_ , 588. [CrossRef] 

2. Kim, J.S.; Seo, G.S.; Jang, H.W.; Lee, J.H. Correlation analysis between Korean spring drought and large-scale teleconnection patterns for drought forecasting. _KSCE J. Civ. Eng._ **2017** , _21_ , 458–466. [CrossRef] 

3. Yue, Y.; Shen, S.; Wang, Q. Trend and variability in droughts in Northeast China based on the reconnaissance drought index. _Water_ **2018** , _10_ , 318. [CrossRef] 

4. Qaiser, G.; Tariq, S.; Adnan, S.; Latif, M. Evaluation of a composite drought index to identify seasonal drought and its associated atmospheric dynamics in Northern Punjab, Pakistan. _J. Arid Environ._ **2021** , _185_ , 104332. [CrossRef] 

5. Cong, D.; Zhao, S.; Chen, C.; Duan, Z. Characterization of droughts during 2001–2014 based on remote sensing: A case study of Northeast China. _Ecol. Inf._ **2017** , _39_ , 56–67. [CrossRef] 

6. Park, S.Y.; Sur, C.; Kim, J.S.; Lee, J.H. Evaluation of multi-sensor satellite data for monitoring different drought impacts. _Stoch. Environ. Res. Risk Assess._ **2018** , _32_ , 2551–2563. [CrossRef] 

7. Sur, C.; Park, S.Y.; Kim, T.W.; Lee, J.H. Remote sensing-based agricultural drought monitoring using hydrometeorological variables. _KSCE J. Civ. Eng._ **2019** , _23_ , 5244–5256. [CrossRef] 

8. Abuzar, M.K.; Shafiq, M.; Mahmood, S.A.; Irfan, M.; Khalil, T.; Khubaib, N. Drought risk assessment in the khushab region of Pakistan using satellite remote sensing and geospatial methods. _Int. J. Econ. Environ. Geol._ **2019** , _10_ , 48–56. [CrossRef] 

9. Zhong, R.; Chen, X.; Lai, C.; Wang, Z.; Lian, Y.; Yu, H.; Wu, X. Drought monitoring utility of satellite-based precipitation products across mainland China. _J. Hydrol._ **2019** , _568_ , 343–359. [CrossRef] 

10. Carlson, T.N.; Gillies, R.R.; Perry, E.M. A method to make use of thermal infrared temperatureand NDVI measurements to infer surface soil water content and fractional vegetation cover. _Remote Sens. Rev._ **1994** , _9_ , 161–173. [CrossRef] 

17 of 18 

_Remote Sens._ **2021** , _13_ , 272 

11. Tadesse, T.; Demisse, G.B.; Zaitchik, B.; Dinku, T. Satellite-based hybrid drought monitoring tool for prediction of vegetation condition in Eastern Africa: A case study for Ethiopia. _Water Resour. Res._ **2014** , _50_ , 2176–2190. [CrossRef] 

12. Enenkel, M.; Steiner, C.; Mistelbauer, T.; Dorigo, W.; Wagner, W.; See, L. A combined satellite-derived drought indicator to support humanitarian aid organizations. _Rem. Sens._ **2016** , _8_ , 340. [CrossRef] 

13. Wang, J.; Xu, X.; Ding, S.; Zeng, J.; Spurr, R.; Liu, X.; Chance, K.; Mishchenko, M. A numerical testbed for remote sensing of aerosols, and its demonstration for evaluating retrieval synergy from a geostationary satellite constellation of GEO-CAPE and GOES-R. _J. Quant. Spectrosc. Radiat. Transfer._ **2014** , _146_ , 510–528. [CrossRef] 

14. Wilhite, D.A. _Drought Monitoring and Early Warning: Concepts, Progress and Future Challenges_ ; World Meteorological Organization: Geneva, Switzerland, 2006; p. 1006. 

15. Huang, S.; Huang, Q.; Leng, G.; Liu, S. A nonparametric multivariate standardized drought index for characterizing socioeconomic drought: A case study in the Heihe River Basin. _J. Hydrol._ **2016** , _542_ , 875–883. [CrossRef] 

16. Wu, Z.; Mao, Y.; Li, X.; Lu, G.; Lin, Q.; Xu, H. Exploring spatiotemporal relationships among meteorological, agricultural, and hydrological droughts in Southwest China. _Stoch Environ. Res. Risk Assess._ **2016** , _30_ , 1033–1044. [CrossRef] 

17. Sur, C.; Park, S.Y.; Kim, J.S.; Lee, J.H. Prognostic and diagnostic assessment of hydrological drought using water and energy budget-based indices. _J. Hydrol._ **2020** , _591_ , 125549. [CrossRef] 

18. Guo, Y.; Huang, S.; Huang, Q.; Wang, H.; Fang, W.; Yang, Y.; Wang, L. Assessing socioeconomic drought based on an improved multivariate standardized reliability and resilience index. _J. Hydrol._ **2019** , _568_ , 904–918. [CrossRef] 

19. McKee, T.B.; Doesken, N.J.; Kleist, J. The relationship of drought frequency and duration to time scales. In Proceedings of the 8th Conference on Applied Climatology, Anaheim, CA, USA, 17–22 January 1993; Volume 17, pp. 179–183. 

20. Shukla, S.; Wood, A.W. Use of a standardized runoff index for characterizing hydrologic drought. _Geophys. Res. Lett._ **2008** , _35_ , 1100. [CrossRef] 

21. Hayes, M.; Svoboda, M.; Wall, N.; Widhalm, M. The Lincoln declaration on drought indices: Universal meteorological drought index recommended. _Bull. Am. Meteorol. Soc._ **2011** , _92_ , 485–488. [CrossRef] 

22. Hao, Z.; AghaKouchak, A. A nonparametric multivariate multi-index drought monitoring framework. _J. Hydrometeor._ **2014** , _15_ , 89–101. [CrossRef] 

23. Cunha, A.P.M.; Alvalá, R.C.; Nobre, C.A.; Carvalho, M. A Monitoring vegetative drought dynamics in the Brazilian semiarid region. _Agric. Meteorol._ **2015** , _2014_ , 494–505. [CrossRef] 

24. Sur, C.; Hur, J.; Kim, K.; Choi, W.; Choi, M. An evaluation of satellite-based drought indices on a regional scale. _Int. J. Remote Sens._ **2015** , _36_ , 5593–5612. [CrossRef] 

25. Li, J.; Zhou, S.; Hu, R. Hydrological drought class transition using SPI and SRI time series by loglinear regression. _Water Resour. Manage._ **2016** , _30_ , 669–684. [CrossRef] 

26. Palmer, W. _Meteorological Drought, Weather Bureau Research Paper 45_ ; U.S. Weather Bureau: Washington, DC, USA, 1965; p. 58. 

27. Zhang, A.; Jia, G. Monitoring meteorological drought in semiarid regions using multi-sensor microwave remote sensing data. _Remote Sens. Environ._ **2013** , _134_ , 12–23. [CrossRef] 

28. Zhang, X.; Chen, N.; Li, J.; Chen, Z.; Niyogi, D. Multi-sensor integrated framework and index for agricultural drought monitoring. _Remote Sens. Environ._ **2017** , _188_ , 141–163. [CrossRef] 

29. Kogan, F.N. Application of vegetation index and brightness temperature for drought detection. _Adv. Space Res._ **1995** , _15_ , 91–100. [CrossRef] 

30. Kogan, F.N. Operational space technology for global vegetation assessment. _Bull. Am. Meteorol. Soc._ **2001** , _82_ , 1949–1964. [CrossRef] 

31. Oki, T.; Kanae, S. Global hydrological cycles and world water resources. _Science_ **2006** , _313_ , 1068–1072. [CrossRef] 

32. Huffman, G.J.; Adler, R.F.; Bolvin, D.T.; Gu, G.; Nelkin, E.J.; Bowman, K.P.; Hong, Y.; Stocker, E.F.; Wolff, D.B. The TRMM MultiSatellite Precipitation Analysis: Quasi-Global, Multi-Year, Combined-Sensor Precipitation Estimates at Fine Scale. _J. Hydrometeor._ **2007** , _8_ , 38–55. [CrossRef] 

33. McKee, T.B. Drought monitoring with multiple time scales. In Proceedings of the 9th Conference, Applied Climatology, Dallas, TX, USA, 15–20 January 1995; pp. 233–236. 

34. Hao, Z.; AghaKouchak, A. Multivariate Standarized Drought Index: A prametric multi-index model. _Adv. Water Resour._ **2013** , _57_ , 12–18. [CrossRef] 

35. Ma, Y.Y.; Zhu, L.P. A Review on Dimension Reduction. _Int. Stat. Rev._ **2012** , _81_ , 134–150. [CrossRef] [PubMed] 

36. Jolliffe, I.T. _Principal Component Analysis_ , 2nd ed.; Springer Science Business Media: Berlin, Germany, 2002. 

37. Oba, S.; Sato, M.A.; Takemasa, I.; Monden, M.; Matsubara, K.I.; Ishii, S. A Bayesian missing value estimation method for gene expression profile data. _Bioinformatics_ **2003** , _19_ , 2088–2096. [CrossRef] [PubMed] 

38. Lai, W.Y.; Kuok, K.K. A Study on Bayesian Principal Component Analysis for Addressing Missing Rainfall Data. _Water Resour. Manag._ **2019** , _33_ , 2615–2628. [CrossRef] 

39. Lee, T. Climate change inspector with intentionally biased bootstrapping (CCIIBB ver. 1.0)–methodology development. _Geosci. Model. Dev._ **2017** , _10_ , 525–536. [CrossRef] 

40. Bouveyron, C.; Latouche, P.; Mattei, P.A. Exact dimensinality selection for Bayesian PCA. _Scand. J. Statist._ **2020** , _47_ , 196–211. [CrossRef] 

18 of 18 

_Remote Sens._ **2021** , _13_ , 272 

41. Heng, C.; Lee, T.; Kim, J.-S.; Xiong, L. Influence analysis of central and Eastern Pacific El Niños to seasonal rainfall patterns over China using the intentional statistical simulations. _Atmos. Res._ **2020** , _233_ , 104706. [CrossRef] 

42. Zelinka, I. SOMA—self-organizing migrating algorithm. In _New Optimization Techniques in Engineering_ ; Springer: Berlin/Heidelberg, Germany, 2004; pp. 167–217. 

43. Baek, S.G.; Jang, H.W.; Kim, J.S.; Lee, J.H. Agricultural drought monitoring using the satellite-based vegetation index, Korea Water Resources Association. _J. Korea Water Resour. Assoc._ **2016** , _49_ , 305–314. (In Korean) [CrossRef] 

44. Lee, J.H.; Jang, H.W. Comparison on Characteristics and Historical Drought Events of summer drought in 2014. Korea Disaster Prevention Association. _J. Disaster Prev._ **2014** , _16_ , 46–56. (In Korean) 

45. Ministry of Land, Infrastructure and Transport (MLIT). _2015 Drought Impact Investigation Report_ ; Korea Ministry of Land, Infrastructure and Transport (MLIT): Sejong City, Korea, 2015. (In Korean) 

46. Bae, H.; Ji, H.; Lim, Y. Characteristics of drought propagation in South Korea: Relationship between meteorological, agricultural, and hydrological droughts. _Nat. Hazards._ **2019** , _99_ , 1–16. [CrossRef] 

47. Hong, I.P.; Lee, J.H.; Cho, H.S. National drought management framework for drought preparedness in Korea (lessons from the 2014–2015 drought). _Water Policy_ **2016** , _18_ , 89–106. [CrossRef] 

