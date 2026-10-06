



## **RESEARCH ARTICLE** 

### 10.1029/2024EF004674 

#### **Key Points:** 

- Propagating surface soil moisture drought has greater impact of meteorological drought (MD) than initial land and atmospheric conditions 

- Propagating soil moisture drought (SMD) at rootzone has comparable influence of MD and initial soil moisture at longer propagation times 

- Considering MD duration and intensity together yields higher causation between MD and propagating SMD than accounting for them exclusively 

#### **Supporting Information:** 

Supporting Information may be found in the online version of this article. 

#### **Correspondence to:** 

L. Karthikeyan, karthikl@iitb.ac.in 

#### **Citation:** 

Gupta, A., & Karthikeyan, L. (2024). Role of initial conditions and meteorological drought in soil moisture drought propagation: An event‐based causal analysis over South Asia. _Earth's Future_ , _12_ , e2024EF004674. https://doi.org/10. 1029/2024EF004674 

Received 22 MAR 2024 Accepted 29 SEP 2024 

# **Role of Initial Conditions and Meteorological Drought in Soil Moisture Drought Propagation: An Event‐Based Causal Analysis Over South Asia** 

### **Amitesh Gupta**<sup>**1**</sup> **and L. Karthikeyan**<sup>**1,2**</sup> 

> 1Centre of Studies in Resources Engineering, IIT Bombay, Mumbai, India, 2Centre for Climate Studies, IIT Bombay, Mumbai, India 

**Abstract** The role of meteorological droughts and initial conditions (land and atmosphere) in soil moisture drought (SMD) propagation are not yet fully understood. This work uses a drought event‐based causal framework to investigate the relative importance of meteorological drought (MD) duration and intensity and initial conditions that result in surface and rootzone SMD, considering their event‐level propagation time (PT) over South Asia. Initially, spatial variability of drought propagation is assessed by the Propagation Ratio (PR) computed based on MD counts that trigger SMD at various lags. PR depicts 2–3 months slower rootzone propagation than at surface. The gradual decrease in PR with increasing regional aridity indicates faster propagation over humid regions. The causal impact of initial conditions and MD parameters on propagating SMD are evaluated using normalized mutual information and a newly proposed normalized conditional mutual information. We found greater importance of triggering MD parameters followed by initial soil moisture condition on propagating SMD. This behavior is more evident for the surface layer propagation at shorter PT. There is a confounding effect of initial atmospheric conditions on drought propagation through initial soil moisture, depicting the significance of land‐atmosphere interactions prior to propagation. In the rootzone propagation, initial soil moisture has a greater influence on propagation, especially at longer PT, indicating the significance of soil moisture persistence. Stronger causal links obtained through the joint influence of MD parameters on SMD suggest the importance of accounting for MD duration and intensity simultaneously, which are not considered in drought index‐based propagation studies. 

**Plain Language Summary** Understanding the process of meteorological droughts transitioning to soil moisture droughts helps improve drought prediction capabilities and effectively manage agricultural water resources. This work explicitly addresses how meteorological drought “events” propagate into soil moisture drought “events” at surface and rootzone layers with variable propagation time—a critical aspect overlooked in the past. Our findings depict slower and weaker propagation to the rootzone layer compared to the surface layer and suggest that the transition rate is sensitive to regional aridity. Causal associations between initial land‐ atmospheric conditions and triggering meteorological drought properties with propagating soil moisture droughts are established using novel entropy‐based mutual information metrics. We found higher importance of triggering drought parameters on propagating droughts both at surface and rootzone soil when their joint influence is considered rather than accounting for any individual initial condition or an individual triggering drought parameter. These causations also vary regionally and event‐wise with changes in propagation times. The current work advocates investigating drought propagation at the event level instead of using standardized timeseries information. The findings would also be helpful for future studies linking land‐atmosphere interactions with drought events. 

## **1. Introduction** 

> © 2024. The Author(s). This is an open access article under the terms of the Creative Commons Attribution‐NonCommercial‐NoDerivs License, which permits use and distribution in any medium, provided the original work is properly cited, the use is non‐commercial and no modifications or adaptations are made. 

Drought is a spatiotemporally scale‐variant complex natural phenomenon caused by incessant dryness in the atmosphere, continental water bodies, soil or groundwater (A. K. Mishra & Singh, 2010; Peters et al., 2005; Van Loon, 2015). Among various drought types, agricultural droughts are primarily characterized by depleting soil moisture (SM) (hence, we further used the term soil moisture drought (SMD) in this study). The South Asia region has experienced frequent droughts in the past decades (Aadhar & Mishra, 2017, 2021). It is likely to exacerbate even further and intensify in the future (Aadhar & Mishra, 2020; Mondal et al., 2021). This region is the residence of 24.89% of the world's population, and more than 60% are associated with the agricultural sector for their 

1 of 21 

GUPTA AND KARTHIKEYAN 

**Earth's Future** 

10.1029/2024EF004674 

livelihood (Aryal et al., 2020). It is essential to understand the drought mechanisms in this regional context, which could assist in better forecasting and alleviating the drought's impact on people. 

The characteristics of various drought types over a region are noticed as interconnected; however, they could vary regionally and temporarily (Vorobevskii et al., 2022). Thus, one drought type may lead to another, resulting in long‐term drought conditions. This transition of drought from one type to another is known as drought propagation (Huang et al., 2017; A. F. Van Loon et al., 2012; Q. Zhang et al., 2022). Meteorological drought (MD) has been primarily noticed as a predecessor to other drought types (Fang et al., 2020; Gevaert et al., 2018). There are several studies carried out in the context of MD to hydrological drought propagation, which suggest the importance of drought timescale, seasonality of climate components and watershed characteristics to understand complex relations among terrestrial and atmospheric components in the hydrological cycle (Apurv & Cai, 2020; Lin et al., 2023; Q. Liu et al., 2023; Yang et al., 2022). During MD, precipitation (PRE) deficit, coupled with higher air temperature (AT), leads to an increase in the vapor pressure deficit (VPD) and potential evapotranspiration (PET) (Trenberth, 2011). Higher wind speed (WS) and solar radiation (Radn) also accelerate the evapotranspiration from the soil and inland water bodies (Crocetti et al., 2020; Heck et al., 2020; Schumacher et al., 2019). Few studies suggest that antecedent meteorological conditions, such as AT, PRE, PET, WS and VPD, as well as prevailing land conditions, such as SM and land surface temperature, are crucial for SMD prediction (AghaKouchak, 2014; Chatterjee et al., 2022; Hao et al., 2018). 

The SM exhibits inconsistent lag to atmospheric water deficit conditions (Tian et al., 2022). Thus, at a shorter timescale, a MD does not instinctively cause a decline in SM to trigger drought (Entekhabi, 2023). However, the time difference between MD and its subsequent SMD, that is, the propagation time (PT), could vary spatially and temporally (Dai et al., 2022). Thus, accounting for changes in PT is important to comprehend the process of drought propagation over different regions. 

The nature of SMD heavily depends on the SM dynamics of the corresponding soil layer. This is because the soil‐ water interactions vary at different soil depths due to variations in soil properties (Iwata, 2020). SM in the deeper soil has a greater persistence than at the surface (Ghannam et al., 2016). Thus, drought impact varies from the surface to rootzone soil (A. K. Mishra et al., 2015). Prior studies only focused on MD to surface soil moisture drought (SSMD) propagation. According to McColl et al., 2017, SM has greater temporal dynamics at the surface level compared to the deeper soil. Besides, rootzone SM is critical for plant water uptake (Dralle et al., 2020). It is, therefore, imperative to study how MD propagate to rootzone soil moisture drought (RSMD) and how different it possibly could be from MD propagation into the surface soil. 

Most of the existing works on drought propagation utilize time series of drought indices. These studies typically employ correlation methods to assess the PT and probabilistic approaches to gain insight into the propagation process. There are three major limitations associated with such work. One, the entire timeseries of drought indices would contain information pertaining to non‐drought periods, which affects the analysis related to drought propagation. Two, despite their popularity correlation methods only depict the linear association and not the true causation (Altman & Krzywinski, 2015). Third, PT may vary for each drought event, which could not be revealed while using the correlation method. Therefore, the influence of triggering factors on propagating droughts at different PT could also vary (X. Zhang et al., 2022). Accounting for these limitations, identifying drought events instead of using drought indices would be more appropriate. Our approach also serves well in the context of developing drought early warning systems, as stakeholders would be interested in knowing the nature of the entire drought (onset, intensity, and duration). In particular, the second limitation could be addressed by using the information theory, which has been widely applied to understand causal associations. 

A few attempts have been made to study the nature of drought propagation in the context of hydrological and soil moisture droughts at an event level (Q. Li et al., 2022; J. Wu et al., 2018). However, the causal influence of the various drivers of propagating SMD remains unexplored, which is of crucial importance in the context of the changing climate and the increased demand for early warning systems. To the best of our knowledge, none of the studies have taken the PT, a dynamic parameter attributed to each propagated drought event, into cognizance while assessing the drought propagation. This study attempts to address these gaps using an event‐based causal approach for assessing the relative importance of initial conditions and MD on propagated SSMD and RSMD over South Asia. As mentioned earlier, this is important in the context of developing regional‐scale early warning systems for droughts, as the factors with higher relative importance on propagating drought at longer PT could be 

2 of 21 

GUPTA AND KARTHIKEYAN 

**Earth's Future** 

10.1029/2024EF004674 

used for seasonal‐level drought prediction, which may not be similar in the case of predicting drought propagation in the sub‐seasonal scale. 

To determine the causal association between triggering MD and propagating SMD, we propose a new causal metric called Normalized Conditional Mutual Information (NCMI), derived from information theory (Shannon, 1948a, 1948b) in this work. We used NCMI and Normalized Mutual Information (NMI) in the causal analysis. Our proposed NCMI, analogous to NMI, provides a value between 0 and 1; thus, it enables comparison among several cases assessed using NMI and NCMI. 

Through this study, we aimed to address the following research questions: 

- What is the spatial pattern of MD propagating into SSMD and RSMD with respect to lags and regional aridity? 

- What is the relative contribution of initial conditions and MD parameters to propagating SSMD and RSMD properties? 

- How do the drought propagation strengths vary at a regional level and with respect to PT? 

The remainder of the manuscript is structured as follows. Section 2 describes the data sets and methods used in the current study. Section 3 presents the results found during this investigation. Section 4 discusses the key findings and conclusions of the work. 

## **2. Data and Methods** 

### **2.1. Data** 

The present study focuses on the South Asia region (6°–38°N, 66°–98°E), where 56.9% of the total land area is arable (databank.worldbank.org). To investigate MD, we used daily products of PRE from Multi‐Source Weighted‐Ensemble Precipitation (MSWEP v2; Beck et al., 2019) and Potential Evapotranspiration (PET) data from Singer et al. (2021), where daily PET is estimated from ERA‐5 Land reanalysis products using the Penman‐Monteith method (Allen et al., 1998). Both daily PRE and PET data sets are generated at 0.1° spatial resolution and are converted into a monthly scale for calculating water balance (difference between PRE and PET). For SMD analysis, the surface and rootzone SM products are obtained from the Global Land Evaporation Amsterdam Model (GLEAM v3.6; Martens et al., 2017) at a monthly scale and spatial resolution of 0.25°. The climatological mean (1981–2020) of PRE, PET, and SM at the surface and rootzone layers are shown in Figure S1 in Supporting Information S1. Initial conditions apart from PRE, PET and SM, net solar radiation (Radn) and WS data on a monthly scale and 2‐m AT and dew point temperature data on an hourly scale are obtained from ERA‐5. Daily maximum AT is identified from hourly AT data and converted into the monthly scale. Similarly, hourly AT and dew point temperature are converted into a daily scale to calculate VPD (followed by the method of Yuan et al., 2019) and converted into a monthly scale. To maintain consistency, all data sets are regridded to 0.25° × 0.25° resolution to match the GLEAM grid system. The calculation of standardized anomalies for initial conditions is explained in Text S1 in Supporting Information S1. The average anomalies of the initial conditions are shown in Figure S2 in Supporting Information S1. 

### **2.2. Tools** 

### **2.2.1. Drought Indices** 

We use the Standardized Precipitation Evapotranspiration Index (SPEI; Vicente‐Serrano et al., 2010) to characterize MD because SPEI is subtler to changes in water balance in the atmosphere (C. Liu et al., 2021; Pei et al., 2020). The Standardized Soil Moisture Index (SSMI; Carrão et al., 2016) is used to assess SSMD and RSMD. The timescale of drought indices (SPEI and SSMI) is chosen to 1 month to account for intra‐ and inter‐ seasonal drought events (McKee et al., 1995). We fit eight different probability distribution functions—Normal, Log‐Normal, Log‐Logistic, Weibull, Beta, Gamma, Pearson‐III and Generalized Extreme Value to the monthly timeseries of the difference in water balance (PRE‐PET), surface and rootzone SM over all grids. The best suitable distribution at each grid is identified based on the Kolmogorov–Smirnov (KS) test (Massey, 1951), followed by the lowest Akaike information criterion (AIC; Akaike, 1974) value (Figure S3 in Supporting Information S1). 

3 of 21 

GUPTA AND KARTHIKEYAN 

**Earth's Future** 

10.1029/2024EF004674 



**Figure 1.** A portion of SPEI and SSMI timeseries obtained from a randomly selected grid location. Here, MD1, MD3 and MD4 (triggering droughts) are followed by SMD1, SMD2 and SMD3 (propagated droughts), respectively. MD2 is considered a non‐propagating drought because it is not followed by any soil moisture drought (SMD). MD3 and MD4 propagate into their consecutive SMD at different lags (L2 and L3, respectively). Thus, a meteorological drought may not propagate within a short lag but eventually propagate if a longer lag is considered. The yellow shaded portions are the time periods (one timestep prior to the SMD onset) corresponding to initial land and atmosphere conditions that can affect the propagating soil moisture droughts. 

### **2.2.2. Drought Parameters** 

We used the theory of run (Yevjevich, 1967) with a threshold of − 1 to identify drought events (Apurv et al., 2019; Han & Singh, 2021; Kazemzadeh et al., 2022; Naumann et al., 2012; Rousta et al., 2020). In this process, we estimated drought frequency at each grid and seven drought parameters for all drought events. These include (a) start‐index (time step of drought initiation), (b) end‐index (time step of drought termination), (c) total duration (duration between drought initiation and drought termination), (d) intensity (the lowest SPEI or SSMI value during a drought event, following Apurv et al. (2017) and Apurv and Cai (2020)), (e) peak‐index (time step corresponding to intensity), (f) development period (duration between peak‐index and start‐index), and (g) recovery period (difference between end‐index and peak‐index). In the case of 1–2 months duration droughts, the peak‐index co‐occurs with the start‐index and/or the end‐index. We considered the development and/or recovery duration of 0.5 months for those respective cases. Figure S4 in Supporting Information S1 exhibits a schematic diagram of a drought event's characteristics. To denote the intensity and duration of droughts, we used subscripts of “ _I_ ” and “ _D_ ,” respectively, further in this paper. 

### **2.2.3. Propagation Ratio** 

We identified the triggering MD events that result in propagated SSMD and RSMD at several lags over each grid location. For this purpose, we computed the PT between a triggering MD and a propagated SSMD (RSMD). The difference between the peak‐index of the concerned triggering and propagated drought is considered as the PT of the respective triggering MD (Bhardwaj et al., 2020; Sattar et al., 2019; X. Zhang et al., 2022) (refer to Figure 1). If the duration is lesser or equal to a predefined value of lag (L), we consider that the concerned MD is a triggering drought at that particular L. In this process, we computed the propagation ratio (PR) for several lags over each grid (Equation 1). 



As discussed earlier, the triggering MD event is the event that precedes a SSMD or RSMD event (Fang et al., 2020). Acknowledging longer drought persistence at rootzone soil (Ho et al., 2021), we computed PRL for 

4 of 21 

GUPTA AND KARTHIKEYAN 

**Earth's Future** 

10.1029/2024EF004674 

MD‐SSMD and MD‐RSMD, considering lags up to 6 and 8 months, respectively. We further computed the average of PRL values across the lags (PRavg) at each grid for further analysis. 

### **2.2.4. Mutual Information Metrics** 

In this work, we used Mutual Information (MI) and Conditional Mutual Information (CMI) metrics derived from the information theory (Cover & Thomas, 2006). MI depicts the amount of information shared between two random variables, whereas CMI quantifies the quantity of information obtained about one random variable from another random variable in the presence of a third random variable (Kraskov et al., 2004; Vejmelka & Paluš, 2008). The computation of MI and CMI uses Shannon's Entropy (Shannon, 1948b), which measures the average information or uncertainty intrinsic to a new value of a random variable. Shannon's Entropy ( _H_ ) or marginal entropy of a random variable is _X_ as in Equation 2. 



where values of _X_ are segregated into “ _a_ ” number of bins and _pi_ is the relative frequency of the _i_ th bin. _H_ ( _X_ ) is a positive entity with a maximum value of log( _pi_ ) and the base of log is 2 (Shannon, 1948b). Consider sample data of two random variables _X_ and _Y_ , which are used to estimate relative frequency _pi_ , _j_ (for _i_ , _j_ th bin) while considering “ _a_ ” and “ _b_ ” number of bins, respectively. The joint entropy of _X_ and Y can be computed as in Equation 3. 



Similarly, a joint entropy for three random variables _X_ , _Y_ , and _Z_ can be computed as in Equation 4. 



where, _pi_ , _j_ , _k_ is the relative frequency for _i_ , _j_ , _k_ th bin; “ _c_ ” is the number of bins considered for data pertaining to _Z_ . Using the above equations, CMI can be computed using marginal and joint entropies (Cover & Thomas, 2006) as in Equation 5. 



where, CMI( _X_ ; _Y_ | _Z_ ) represents CMI between _X_ and _Y_ given _Z_ . 

It is noteworthy that CMI is a non‐negative value that can vary from zero to infinity. Hence, it is difficult to interpret and compare multiple scenarios using MI and CMI. Strehl and Ghosh (2002) computed NMI analogous to the Pearson correlation coefficient as in Equation 6. 



where, MI( _X_ ; _Y_ ) denotes the MI between _X_ and _Y_ variables. MI( _X_ ; _Y_ ) can be expressed in terms of marginal and joint entropies as— 



Following a similar approach, we proposed a new metric NCMI, which can be computed using Equation 8 

5 of 21 

GUPTA AND KARTHIKEYAN 

**Earth's Future** 

10.1029/2024EF004674 



where, _H_ ( _X_ | _Z_ ) and _H_ ( _Y_ | _Z_ ) represent the conditional entropy of _X_ given _Z_ and Y given _Z_ , respectively (Equations 9 and 10). 





Therefore, Equation 8 can be written in terms of marginal and joint entropies as— 



It could be seen that in the case of _Y_ = _X_ , NCMI( _X_ ; _Y_ | _Z_ ) equates to 1. Comparing NCMI( _X_ ; _Y_ | _Z_ ) and NMI( _X_ ; _Y_ ) offers us insights on the nature of influence between the random variables. NCMI( _X_ ; _Y_ | _Z_ ) < NMI( _X_ ; _Y_ ) indicates there is redundant information between _X_ and _Z_ , and _Y_ and _Z_ , which results in no new information adding between _X_ and Y in the presence of Z. Under this condition, _Z_ acts as a confounding variable that influences the relationship between _X_ and Y. NCMI( _X_ ; _Y_ | _Z_ ) = NMI( _X_ ; _Y_ ) indicates _Z_ is independent of _X_ and Y, and does not alter the information shared between _X_ and Y. However, NCMI( _X_ ; _Y_ | _Z_ ) > NMI( _X_ ; _Y_ ) indicates that the presence of _Z_ helped to improve the information shared between _X_ and Y, which indicates that there is significant information present between _X_ and _Y_ , _X_ and _Z_ , and _Y_ and _Z_ . 

### **2.3. Methods** 

The proposed approach is based on the hypothesis that the drought propagation “strength” and PT depend on the drought duration and intensity along with initial conditions. To support our hypothesis, we present a schematic of the Standardized Precipitation Evapotranspiration Index (SPEI‐1 month) and Standardized Soil Moisture Index (SSMI‐1 month) at a randomly selected grid cell in South Asia in Figure 1. Considering a threshold of − 1 for both indices, we identify SMD that is triggered by preceding MD (MD1, MD3, MD4 in Figure 1). In these cases, SMD (SMD1, SMD2, and SMD3 in Figure 1) is called as propagating drought and MD is called the triggering drought (Fang et al., 2020). There is also a MD (MD2) in Figure 1 that doesn't propagate to SMD. Each of these droughts has different parameters (duration and intensity). Considering the distance between the peaks of triggering MD and propagating SMD as PT, we observe that PT also varies from event to event. The proposed method offers two key advantages compared to past studies: (a) we can identify only the drought periods rather than working on full timeseries of drought indices and (b) the PT remains an event‐dependent variable, unlike past studies where one value of PT is estimated using full timeseries of MD and SMD indices at a location. 

Conducting the above analysis pixel‐wise would result in an inadequate number of triggering and propagated drought events to determine joint distributions. To address this issue, we pooled pixels into a few distinct clusters by performing the unsupervised Mean‐Shift Clustering algorithm (Y. Cheng, 1995). It is an unsupervised classification method where the optimal number of classes is estimated based on data distribution and density, and it uses an adaptive bandwidth selection technique which optimizes neighborhood size to estimate the mean shift vectors (Aliyari Ghassabeh & Rudzicz, 2018; Hu et al., 2017). In this process, we used MD and SMD parameters (frequency, total duration, and intensity) and locational information (latitude, longitude, and altitude) as inputs. All inputs are scaled from 0 to 1 using the MinMaxScaler from scikit‐learn before performing clustering. The clustering technique is implemented separately for MD and SSMD drought parameters and MD and RSMD drought parameters, along with location information. 

We used NMI and NCMI metrics distinctly. NMI is computed between propagated SSMD duration (intensity) and initial condition of respective SSMD events and triggering MD duration (intensity), where SSMD _D_ (SSMD _I_ ) is considered as _X_ variable and Radn, AT, PRE, PET, VPD, SM and MD _D_ (MD _I_ ) are individually considered as Y variable as shown in Equation 6. NCMI is computed between propagating SSMD _D_ (SSMD _I_ ) and triggering MD _D_ (MD _I_ ) with conditioning of triggering MD _I_ (MD _D_ ). For instance, NCMI (SSMD _D_ ; MD _D|_ MD _I_ ) is computed using 

6 of 21 

GUPTA AND KARTHIKEYAN 

**Earth's Future** 

10.1029/2024EF004674 

Equation 11, where SSMD _D_ , MD _D_ , and MD _I_ are considered as _X_ , _Y_ , and _Z_ variables, respectively. NCMI depicts the amount of information shared between triggering and propagating drought duration (intensity) in the presence of triggering drought intensity (duration). We pooled the information of all triggering and propagating drought events from each cluster separately to compute NMI and NCMI. After that, we further segregate the propagation events based on their PT (1–6 months) and repeat the same process of employing NMI and NCMI between MD and respectively propagated SSMD parameters for those events. Similarly, the entire process is repeated for propagating RSMD and triggering MD event properties over MD‐RSMD clusters. It may be noted that NCMI computations have not been applied to initial conditions, considering the uncertainties involved in estimating high dimensional joint distributions and further complexities associated with normalizing CMI. 

To infer the relative importance of initial conditions and triggering drought parameters for propagated drought conditions, we used Equation 12 and found how this relative importance changes over different drought clusters in the South Asia region. 



where, RI<sup>_C_</sup> _f_<sup>is the relative importance (expressed in %) of factor</sup><sup>_f_in terms of propagation strength in cluster C.</sup> Variable _f_ represents the initial conditions and triggering MD parameters. _I_<sup>_c_</sup> _X_<sup>isthepropagationstrengthof</sup> variable _f_ in cluster C, which is obtained by either NMI (Equation 6) or NCMI (Equation 11). Radn, AT, PRE, PET, VPD, SM, and MD _D_ or MD _I_ are considered as variable _f_ in case of computing NMI and MD _D_ |MD _I_ or MD _I_ | MD _D_ is considered as _f_ in case of computing NCMI. To obtain the overall importance of a particular variable ( _f_ ) in the study area, we averaged the RI<sup>_C_</sup> _f_<sup>of that variable across all clusters (C = 1, …11 for MD‐SSMD and C = 1,</sup> …10 for MD‐RSMD). Intercomparing _RI_ of different variables in each of the four cases (i.e., propagation strengths for SMD duration and intensity at surface and rootzone layers) helped us to assess the relative impact of initial conditions and triggering meteorological droughts on propagated SMD parameters. 

## **3. Results** 

### **3.1. Regional Variations in Drought Characteristics** 

We found significant variations in the spatial patterns of the characteristics of MD, SSMD, and RSMD across South Asia (Figure 2). The frequency of soil moisture droughts (both at the surface and rootzone) is higher over north‐west India, Pakistan, the Tibet region and the southern part of peninsular India, whereas frequent MD is experienced over rain‐shadow areas of the Shivalik and Greater Himalayas, western India, Pakistan and some parts of the eastern Tibet. Overall, SSMD events are more frequent than MD and RSMD events in this region. Interestingly, we observed that appx. 69% of this entire region experienced high drought frequency in surface soil, whereas approximately 56% of this region registered moderate drought frequency for MD and RSMD (Table S1 in Supporting Information S1). We can infer that a significantly large area in South Asia experiences more frequent SSMD than MD and RSMD. 

The average total drought duration for RSMD is significantly longer than that of SSMD (MD) in this region. Spatial maps of the total drought duration (in months) of MD, SSMD, and RSMD (in Figure 2) show that MD duration (MDD) in East and North‐East India is relatively less than in North and Central India. Shorter SSMD _D_ is noticed only over the eastern part of Central India, whereas Central India and some East India experienced shorter RSMD _D_ . Overall, 60%–80% of the entire South Asia region experienced soil moisture droughts (SSMD and RSMD) of 3–6 months duration (Table S1 in Supporting Information S1). 

The Central Indian region registered higher intensity MD than the rest of the region. However, SSMD _I_ and RSMD _I_ are higher in the Northern Indo‐Gangetic Plains and Southern parts of India than in the rest areas. Overall, SSMD events across the study area are more intensive than MD and RSMD. However, the average intensity for all three drought types is between − 1.5 and − 2.0 over 78%–85% of the entire region (Table S1 in Supporting Information S1). It indicates that rootzone soil in South Asia is more exposed to prolonged droughts than surface soil, and contrarily, surface soil undergoes higher drought intensity frequently than rootzone. 

7 of 21 

GUPTA AND KARTHIKEYAN 

**Earth's Future** 

10.1029/2024EF004674 



**Figure 2.** Meteorological, Surface, and Rootzone Soil Moisture Drought Event Properties. Frequency is the total number of drought events occurred at a location. Total Duration and Drought Intensity are the average values of duration and intensity calculated across all drought events at a location. 

The spatial pattern of drought development (DD) and its recovery (DR) are similar to the total drought duration (Figure S5 in Supporting Information S1). The average DD and DR for MD are lower than RSMD and SSMD over this entire region. Overall, drought recovery is significantly faster than its development in this region. 

Acknowledging the uncertainty associated with different precipitation data sets, we have also identified the MD frequency, average duration and average intensity with three different precipitation data sets (MSWEP, CHIRPS and GLDAS) and the PET derived from the ERA‐5. We found comparable patterns of MD estimated from these three data combinations (Figures S6 and S7 in Supporting Information S1). Uncertainties about SMD parameters with SM data sets could be explored in future. 

### **3.2. Analysis of Drought Propagation Ratio** 

The PR reveals the frequency‐based assessment of event propagations at different lags, that is, how many MD events subsequently caused SSMD or RSMD within certain time gaps. Higher PR indicates that more MD 

8 of 21 

GUPTA AND KARTHIKEYAN 

**Earth's Future** 

10.1029/2024EF004674 



**Figure 3.** MD‐SSMD and MD‐RSMD Propagation Ratios at different lags. 

propagated at that particular lag based on past records. The MD‐SSMD and MD‐RSMD at different lags are shown in Figure 3. At each lag, higher PR is noticed over North‐East India, Indo‐Gangetic Plains, Western Ghats, and Myanmar regions. PR values are lower in North‐West India, Pakistan, the Tibetan Plateau, and the interior of Peninsular India. We found approximately 50%, 70%, and 90% of MD propagate into SSMD (RSMD) at a lag of 2 (4), 4 (6), and 6 (8) months, respectively (Figure S8 in Supporting Information S1). In the cases of MD‐SSMD and MD‐RSMD, we observed an average increment of 9% and 7% at each lag (lag is further denoted as capital L in the text), respectively. However, a maximum rise in PR is noticed at L3 and L4 (L7 and L8) for surface and rootzone propagations. The magnitude of the maximum increase in PR is also lesser in MD‐RSMD than in MD‐SSMD, 

9 of 21 

GUPTA AND KARTHIKEYAN 

**Earth's Future** 

10.1029/2024EF004674 



**Figure 4.** (a) Regional variations in Average Propagation Ratio (PRavg) and annual mean precipitation (PRE) and potential evapotranspiration (PET) with respect to Aridity Index is shown here. The red line represents PRavg for meteorological to rootzone soil moisture drought propagation (MD‐RSMD), and the blue line represents PRavg for meteorological to surface soil moisture drought propagation (MD‐SSMD). Their standard deviations are shown in hues of similar colors. PRE and PET over those similar regions are shown in bar graphs (in blue and woody colors, respectively) with standard deviation as error bars. (b) PRavg and PRE, and (c) PRavg and PET of those classes are plotted in a scatter diagram to depict their association. A logarithmic best‐fit line (dashed line) is fitted in both the cases, and thus, obtained adjusted R<sup>2</sup> values showed in the same graph. In both (b) and (c), the blue dashed line is for MD‐SSMD, and the green dashed line is for MD‐RSMD propagations. In both scatter plots, vertical error bars represent the standard deviation of PRavg, whereas horizontal error bars show the standard deviation of PRE and PET. 

which implies that MD‐RSMD propagation is more gradual and slower months than propagation in the surface soil. 

We computed the Aridity Index (AI; Barrow, 1992) and identified the arid (AI > 2.25), humid (AI ≤ 0.9) and transitional (0.9 < AI ≤ 2.25) zones in South Asia (Figure S9 in Supporting Information S1). We found PRavg of 0.73 (0.6), 0.56 (0.46), and 0.66 (0.54) for MD‐SSMD (MD‐RSMD) propagation over humid, arid and transitional zones, respectively. Further, we divided the study region into 35 classes based on AI and found a gradual decrease in PRavg with increasing AI (Figure 4a). It indicates that humid areas are prone to more frequent drought propagation than transitional and arid areas. The wet (sub‐humid and humid) regions in South Asia experience high seasonality in PRE. Thus, during a PRE‐deficit period, the soil dries faster due to greater ET, which leads to frequent dry/wet transitions and lowers the SM persistence (Grayson et al., 1997). Eventually, it leads to a higher transition rate of MD into the soil (Z. Xu et al., 2023), also reflected by higher PR at shorter lags. On the other hand, the arid and semi‐arid environments are usually accustomed to lesser PRE (Manoj et al., 2022). However, 

10 of 21 

GUPTA AND KARTHIKEYAN 

**Earth's Future** 

10.1029/2024EF004674 

SM variabilities in such regions are primarily controlled by their coupling to ET and the amount of runoff (W. Wu & Dickinson, 2004) and are hardly influenced by PRE (Z. Xu et al., 2023). It is relevant because semi‐arid and arid regions in the current study area experience minimal PRE and multi‐fold higher PET on an annual scale (Figure 4a). Thus, a MD doesn't immediately cause significant SM depletion to trigger a SMD over drier areas (Du et al., 2022). According to Cai et al. (2022), the degree of SM persistence increases with regional aridity (from humid to arid), and higher SM persistence slows down drought propagation (Bhardwaj et al., 2020). Hence, our findings are concordant with those of previous studies. 

Further, we found that PRavg has a logarithm relation with PRE (Figures 4b and 4c). It suggests that any linear method would not be adequate to link the regional variations in drought propagation with anomalies in precipitation. The adjusted R<sup>2</sup> indicates a better association between PRavg and PRE than PET. An interesting observation is noted as the drastic decrease in PRavg over aridity index of 0.9–3.75 (accounts for transitional and part of arid regions), where the annual PET lies within 1,000–1,200 mm/year but the annual PRE lowers from 1,100 to 300 mm/year. Hence, an episodic decrease in PRE would cause a rise in atmospheric water demand, which eventually accelerates the evaporation of SM and results in event propagation from MD to SMD. It explains east to west gradient in propagation ratios over Indian subcontinent. It can thus be inferred that spatial heterogeneity of PRE plays a greater role in governing the spatial pattern of MD propagation. Apart from the regional aridity, catchment properties, and anthropogenic factors could also contribute to the regional variations in the occurrences of drought propagation events (Apurv et al., 2017; Konapala et al., 2022; Meresa et al., 2023; Wang et al., 2021; T. Zhang et al., 2022). 

We have also computed the PT for each triggering and propagating drought event. We have shown the spatial variability of average PT for MD‐SSMD and MD‐RSMD propagation in Figure S10a and S10b in Supporting Information S1. It exhibits relatively longer PT over the western and northern parts of South Asia, contrary to much shorter PT over Central India and Gangetic plains. Figure S10c and S10d in Supporting Information S1 show the frequency of events with varying PT over each cluster. It depicts the majority of the propagation events attributed to 1–3 months of PT over each cluster, thereby suggesting that the study area experiences significant drought propagation at the sub‐seasonal to seasonal scale. Spatial variations in PT with regional aridity are also shown in Figure S10e in Supporting Information S1. It also shows an increase in PT with increasing aridity, confirming agreement with the spatial variabilities of PR. 

### **3.3. Drought Clusters** 

To understand the regional patterns of event propagation, we identified 11 (10) clusters jointly characterized by the properties of MD and SSMD (RSMD) and their location information. The spatial distribution of these clusters is shown in Figures 5a and 5b. It depicts distinct patterns in the extent of clusters over central and Peninsular India for MD‐SSMD and MD‐RSMD, signifying that the interactions between MD and SSMD properties differ from those between MD and RSMD properties. However, clusters in the north and northwest parts of South Asia are approximately similar in both cases. 

Distinct drought characteristics over each cluster are shown in Figures 5c–5h. Clusters in the north and northwest parts of South Asia have larger spatial coverage and registered maximum drought occurrences (the frequency of all droughts is more than 45,000). In contrast, clusters in the southern part of the study area have fewer drought occurrences than the rest. All the MD‐SSMD (MD‐RSMD) clusters experienced longer SSMD (RSMD) than MD. The clusters in central India experienced comparatively less intensive soil moisture droughts than MD, while the rest experienced more intensive dryness in the soil than in the atmosphere. The overall patterns suggest higher regional variations in drought intensity than duration and frequency. 

Z‐score values of each parameter over all clusters are shown in Figure S11 in Supporting Information S1. It shows higher variations in drought characteristics over MD‐SSMD clusters than MD‐RSMD. We found that the clusters located over the eastern part of South Asia (Lower Gangetic Plain, North‐East India and Myanmar regions) have relatively high variation in MD parameters than SSMD (RSMD) parameters. Contrarily, clusters over the North and Central India region have higher variations in SSMD (RSMD) parameters than MD. Clusters over Peninsular India have fewer variations in their regional drought patterns than the other clusters in the South Asia region. 

11 of 21 

GUPTA AND KARTHIKEYAN 

**Earth's Future** 

10.1029/2024EF004674 



**Figure 5.** The spatial extent of MD‐SSMD and MD‐RSMD clusters are shown in the top (a) left and (b) right, followed by (c–d) Frequency, (e–f) Total Duration, and (g– h) Intensity of meteorological drought and surface soil moisture drought (RSMD) over MD‐SSMD (MD‐RSMD) clusters. 

12 of 21 

GUPTA AND KARTHIKEYAN 

**Earth's Future** 

10.1029/2024EF004674 



**Figure 6.** The overall relative importance of initial conditions (Radn, AT, VPD, WS, PRE, PET, SM) and meteorological drought (MD) parameters to propagated surface soil moisture drought (SSMD) and RSMD parameters. Overall relative importance is calculated by averaging the relative importance of a variable across all clusters. Cluster‐wise, the relative importance of variables is provided in Tables S2–S5 in Supporting Information S1. Duration (intensity) of MD, SSMD and RSMD are mentioned as MD_dur, SSMD_dur and RSMD_dur (MD_inten, SSMD_inten and RSMD_inten), respectively, in the legend. MD_inten|MD_dur indicates NCMI between soil moisture drought (SMD) and MD intensities conditioned on MD duration. And MD_dur|MD_inten indicates NCMI between SMD and MD durations conditioned on MD intensity, where SMD is estimated for surface (SSMD) and rootzone (RSMD) layers. NMI is used to compute propagation strength between SMD parameters and remaining cases where no conditioning variable is involved. 

### **3.4. Relative Importance of Initial Conditions and MD Parameters** 

The average of anomalies of Radn, AT, VPD, WS, PRE, PET and SM during onset months ( _to_ ) and 1 month prior to onset ( _to_ − 1, which is considered as initial conditions) are shown in Figure S2 in Supporting Information S1. Higher positive (negative) anomalies are prominent for VPD (SM) during the onset period. However, during the initial period ( _to_ − 1), anomalies are prominent for SM across the region. Comparatively, anomalies in atmospheric initial conditions (Radn, AT, VPD, WS, PRE and PET during _to_ − 1) are lower and primarily observed over the central and eastern Gangetic plains. Overall, the contrasts between the initial and onset conditions are relatively higher for RSMD than SSMD, indicating that the rapid development in land anomalies and atmospheric conditions have helped develop the droughts in deeper soil. 

The overall relative importance of initial conditions (Radn, AT, VPD, WS, PRE, PET, SM) and triggering drought parameters (duration and intensity of MD) to propagating drought conditions are shown in Figure 6. The individual influence of different initial conditions and MD parameters is obtained using NMI, whereas the conditional influence of MD parameters is obtained through NCMI. 

We observed that the initial conditions have a greater importance (total RI of initial conditions is 68% at surface layer and 70% at the rootzone layer) in influencing the propagating drought intensity, which translates to the magnitude of SM deficit, than the duration (total RI of initial conditions is 48% at surface layer and 61% at the rootzone layer), which depicts the period of anomalously dry soils during drought, both at the surface and rootzone layers. Interestingly, atmospheric initial conditions act similarly in both MD‐SSMD and MD‐RSMD, whereas initial SM has a relatively greater impact on propagating SMD in the rootzone than at the surface level. 

13 of 21 

GUPTA AND KARTHIKEYAN 

**Earth's Future** 

10.1029/2024EF004674 

This indicates a greater influence of antecedent SM on propagating SMD in the rootzone layer than the surface layer. The importance of triggering MD parameters on propagating SMD is greater at the surface soil compared to the rootzone layer. This shows the diminished effect of MD conditions from surface to deeper soil. 

Interestingly, NCMI values are consistently greater than NMI values across all regions (Tables S2–S5 in Supporting Information S1). For instance, if NCMI (SSMD _D_ ; MD _D_ |MD _I_ ) is greater than NMI (SSMD _D_ ; MD _D_ ), it indicates, MD _I_ helped in increasing the information shared between SSMD _D_ and MD _D_ . This further indicates that there is unique information coming from both MD _D_ as well as MD _I_ . Since both MD _D_ and MD _I_ influence SSMD _D_ , we inferred that there is a “joint” influence of MD parameters (both MD _D_ and MD _I_ ) on propagating SSMD _D_ . Further explanation on comparisons between NCMI and NMI is provided in Section 2.2.4. Results reveal the dominant joint influence of MD parameters on propagating SMD compared to when the individual influence MD parameter (duration or intensity) is used for estimating propagation strength (i.e., causation). It indicates weaker association between durations and intensities of MD, in turn, signifies the importance to account for both MD parameters to comprehend regional drought propagation processes. In other words, considering either MD duration or intensity would not elucidate a potential causal relationship between triggering MD and propagating SMD. We also noted that the joint influence of triggering MD parameters is greater for propagating SMD duration rather than SMD intensity, as well as there is a decrease in this joint influence of MD parameters for propagating droughts at rootzone layer than surface soil. This indicates the persistent behavior of soil moisture at deeper layer, where the initial soil moisture and soil properties play a vital role in influencing the drought conditions (A. Mishra et al., 2017; T. Xu et al., 2021). 

We also found notable differences in the causations asserted by different initial conditions and MD parameters in individual clusters (Tables S2–S5 in Supporting Information S1). Over the clusters located in the eastern part of South Asia, which typically belong to sub‐humid and humid regions, the propagating SMD registered higher joint influence of triggering MD parameters compared to the clusters located in the western semiarid and arid regions. Over the clusters located in the transitional zone (refer to Figure S9 in Supporting Information S1 for aridity index and Figures 5a and 5b for location of the drought clusters), we observed that the joint influence of MD parameters is relatively higher for the duration of propagating SMD, however opposite over the humid areas. Among the initial conditions, VPD and WS have a greater impact on propagating SMD intensity than its duration and such observation is more evident over the clusters located North‐East India and Myanmar regions. Over those dense vegetative humid regions, higher VPD results in an increase in evaporative demand, while stronger winds exert greater stress on ecosystems, leading to a rapid rise in evapotranspiration rates and a subsequent sharp decline in soil moisture (Chiang et al., 2021; Schönbeck et al., 2022). It indicates an indirect effect of initial atmospheric conditions on propagating SMD through altering SM, which is of greater relevance for estimating SMD intensity than its duration. On the other hand, SM and VPD have a greater impact among the initial conditions on propagating drought at the surface layer over the central India region, while the similar observation is noted at the rootzone layer over Gangetic Plains. Past studies also identified these regions experiencing varying land‐ atmosphere interactions (Anand et al., 2022; Ganeshi et al., 2020; Konkathi & Karthikeyan, 2024; Navale & Karthikeyan, 2023). Furthermore, the impact of land‐atmosphere interactions on drought propagation may not only vary across space but also at soil depths (S. Cheng & Huang, 2016; Gentine et al., 2019; Hirschi et al., 2014; Schumacher et al., 2022). 

These regional‐level variations in the impact of initial conditions and MD parameters on the propagating SMD both at surface and rootzone attest the dominant role of the joint influence of MD parameters and initial SM. In the next section, we assess the nature of propagation strength of MD properties and initial SM with changing PT. 

### **3.5. Changes in Propagation Strength With PT** 

We investigated variations in causal associations (i.e., propagation strengths) with PT in two different cases—(a) between triggering and propagating drought parameters and (b) initial SM and propagated drought parameters. Both these cases are estimated during MD‐SSMD and MD‐RSMD. Examining the average propagation strength in the case of SSMD duration (Figures 7a and 7b) indicates that the joint influence of MD parameters governs the duration of SSMD propagating at shorter PT. This is prominent in clusters 4, 6, and 10 of MD‐SSMD (Figure 7a), which mostly contain Central India and the Ganges basin. We observed relatively lesser variations in propagation strengths for drought intensity over the drier northwest region (clusters 9 and 11 of MD‐SSMD and Cluster 1 and 

14 of 21 

GUPTA AND KARTHIKEYAN 

**Earth's Future** 

10.1029/2024EF004674 



**Figure 7.** Variations in propagation strengths with propagation times over (a–d) MD‐SSMD and (e–h) MD‐RSMD clusters are shown here. The _y_ ‐axis of line graphs in the left (right) column shows NCMI (NMI) values. The broken line depicts propagation strengths over different clusters, whereas the solid line represents their average. The notation for drought parameters is similar to that in Figure 6. 

15 of 21 

GUPTA AND KARTHIKEYAN 

**Earth's Future** 

10.1029/2024EF004674 

3 of MD‐RSMD) of the study area. Furthermore, at longer PT, the propagating soil moisture droughts both at the surface and rootzone have the influence of triggering MD parameters as well as initial SM conditions. 

In the case of RSMD duration and intensity (Figures 7f and 7h), interestingly, the influence of initial SM increases with longer PT, which further suggests the importance of SM persistence on drought propagation in the rootzone layer. The overall behavior of triggering MD parameters and initial SM is similar for propagating SSMD intensity at all PTs (Figures 7c and 7d), as their influence of propagation SSMD intensity increased gradually up to PT of 4 months and then decreased rapidly. It indicates that the water deficiencies in the surface soil could not have a major influence on land or atmospheric conditions at longer PT, which might be linked to the seasonality of regional climate. However, in the case of propagating RSMD intensity (Figures 7g and 7h), we noticed a consistent relevance of MD parameters as well as initial SM with an increase in PT. 

In summary, we found that MD parameters have a noticeably varying impact on propagating SMD parameters at all PT. Observing the contrasts in the relevance of initial SM, for the duration and intensity of propagated SMD in the surface and rootzone soil, it could be inferred that SM persistence doesn't have similar importance in all scenarios of drought propagation. Since the persistence behavior of SM also depends on the soil type, vegetation characteristics, and precipitation regime, our observations regarding the variations in the causation asserted by the initial SM over different regions at longer PT are anticipated. 

## **4. Discussion and Conclusions** 

Predicting drought events and mitigating its effect on agroeconomic society is crucial for managing water resources and developmental planning. In this work, we first looked into the sensitivity of drought propagation from meteorological to surface and rootzone soil moisture. Then, we assessed the relative importance of different initial conditions and MD parameters on propagated drought conditions and how their causal association varied at different propagation times. Our emphasis on drought events rather than drought indices ensures that the entire study is restricted to deficit conditions (excluding non‐drought periods). 

We applied the run theory to identify the meteorological (MD), soil moisture droughts at the surface (SSMD) and rootzone (RSMD) levels. We computed the Propagation Ratio (PR) at various lags to investigate the sensitivity of drought events' propagation across space. We have proposed a novel method, NCMI, which normalizes the CMI and ensures that its quantification ranges between 0 and 1, analogous to NMI. It helps enable the comparative assessment of multiple scenarios wherever NMI or NCMI is used. We employed these two metrics to estimate the causal association between initial land‐atmosphere conditions and triggering drought parameters with propagating drought parameters. While NMI is computed using both initial conditions and triggering MD parameters, NCMI is computed only using triggering MD parameters. Comparison of NMI and NCMI values of triggering MD parameters helps to infer their individual and joint influence on propagating soil moisture droughts. The following are the major findings of our study. 

Across South Asia, SSMD events are more frequent and intense than MD and RSMD, whereas RSMD is comparatively longer than SSMD and MD. A significantly large area experiences inter‐seasonal soil moisture droughts, depicting greater concern for food security and the urgency of developing drought mitigation strategies. There is a gradual decrease in the transition rate of drought events with increasing regional aridity, which suggests humid areas are more prone to drought propagation, followed by transitional and arid areas. This regional sensitivity of drought propagation has largely a non‐linear relation with precipitation and PET and is relatively more governed by precipitation than PET. Therefore, any linear approach would be unsuitable for elucidating the role of water balance in the occurrence of event propagation. Overall, the transition rate of drought events is comparatively slower in the rootzone than in the surface soil, suggesting that an early warning system for SSMD would effectively predict RSMD across space. 

The relative importance of land and atmosphere initial conditions and MD parameters on propagating drought parameters indicates that the triggering MD properties are of greater importance than initial conditions. This observation is more pertinent for the propagation of SSMD, whereas the initial SM exerts a relatively greater influence on propagating RSMD than SSMD. We found the initial SM to be of relatively greater importance in propagating drought intensity among different initial conditions accounted for, followed by the anomalies in VPD and precipitation. This outcome indicates a confounding effect of atmospheric variables on initial soil moisture conditions (Entekhabi et al., 1996), in turn influencing the intensity of propagating SMD. These confounding 

16 of 21 

GUPTA AND KARTHIKEYAN 

**Earth's Future** 

10.1029/2024EF004674 

effects of atmospheric initial conditions could be interpreted as a signal of land‐atmosphere interactions, which can impact the SMD intensities (Alessi et al., 2022; Miralles et al., 2019). 

We found that accounting for both the duration and intensity of triggering MD simultaneously yields a higher propagation strength for soil moisture droughts both at the surface and rootzone levels, compared to the cases where only the duration or intensity of MD is considered. This is due to the fact that accounting for an individual MD parameter did not allow the underlying potential causation to be revealed, given the lower degree of association between MD durations and intensities at the regional scale. The joint influence of MD parameters has a greater effect on propagating SMD duration (intensity) compared to its intensity (duration) at surface (rootzone) layer over most of the regions in South Asia. This is specifically notable over the transitional regions, followed by arid regions, which indicates the wet‐dry transitioning through land‐atmospheric feedback processes (S. Cheng & Huang, 2016; Green et al., 2017; Miralles et al., 2019; Schumacher et al., 2022). Analysis of Relative Importance (RI) indicates that triggering MD parameters (both intensity and duration) have greater influence on the duration of propagating SMD compared to its intensity. In the latter case, initial land and atmosphere conditions are of increased importance. The RI of MD parameters weakened at the rootzone than the surface, and subsequently, an increasing influence of initial conditions, primarily initial SM, is observed. 

Our investigation also shows the variations in propagation strengths for drought duration and intensity with propagation times across different regions. It suggests that the influence of MD conditions on SSMD propagating at short PT is more significant than that of antecedent SM, and this is pertinent in regions where energy‐limited conditions are dominant (W. Li et al., 2023). However, MD and initial land conditions have a similar influence on RSMD propagating at longer PT, suggesting the greater significance of SM persistence in deeper soil, contrary to surface soil, where atmospheric states primarily govern soil conditions. 

Our findings underscore the significance of event‐based analysis in better comprehending the underlying causations between the atmosphere and land processes. The results highlight the complex interplay between soil moisture, land‐atmosphere interactions, and meteorological drought in determining the nature of soil moisture drought dynamics. The findings also suggest accounting for initial land conditions along with meteorological conditions while forecasting droughts at sub‐seasonal to seasonal timescales in South Asia. The regional variations in the importance of precursors underscore the need to develop location specific drought forecasting mechanisms, which could be achieved using the state‐of‐the‐art deep learning architectures. It may be noted that the anthropogenic footprints, such as land use change and irrigation sources, have not been accounted for in the current work, which could have certain explanatory factors in understanding the spatial variations of drought propagation locally (T. Zhang et al., 2022). Besides, the current framework is limited to studying drought propagation at a regional scale. Future efforts could assess the variations in drought propagation from one event to another at a localized scale. It would also be interesting to expand the applicability of NCMI to initial land and atmosphere conditions by developing the necessary multivariate formulation (considering more than three random variables). The observed variations in propagation strengths with propagation times could be attributed to regional aridity, soil properties and vegetation types. These aspects, along with the influence of atmospheric teleconnections on drought propagation, must be studied in the future. 

## **Data Availability Statement** 

All data sets used in the work have been obtained from publicly available sources. GLEAM (Martens et al., 2017) soil moisture for surface and rootzone levels have been obtained from https://www.gleam.eu/, accessed last on 12 December 2022. Three different precipitation products—MSWEPv2 (Beck et al., 2019) is accessed from https:// www.gloh2o.org/mswep/ on 16 December 2022, CHIRPS (Funk et al., 2015) from https://chc.ucsb.edu/data/ chirps on 10 May 2024, and precipitation of GLDAS (Rodell et al., 2004) have been accessed from https://disc. gsfc.nasa.gov/ on 12 May 2024. ERA‐5 derived PET (Singer et al., 2021) data is accessed from https://doi.org/10. 5523/bris.qb8ujazzda0s2aykkv0oq0ctp on 10 December 2022. Air temperature, vapor pressure deficit, radiation and WS data of ERA‐5 (Hersbach et al., 2020) have been collected from the Copernicus climate data store https:// cds.climate.copernicus.eu/ and last accessed on 16 May 2024. Analytical results and scripts are uploaded to zenodo.org, which can be found in Gupta and Lanka (2024). 

17 of 21 

GUPTA AND KARTHIKEYAN 

**Earth's Future** 

10.1029/2024EF004674 

#### **Acknowledgments** 

The authors gratefully acknowledge the financial support given by the Ministry of Earth Sciences, Government of India (Project ID: MOES/16/04/2022‐RDESS/ AI‐ML‐04). We acknowledge funding support from the GISE Hub at IIT Bombay (Project ID: RD/0123‐GISIR00‐006). 

## **References** 

Aadhar, S., & Mishra, V. (2017). High‐resolution near real‐time drought monitoring in South Asia. _Scientific Data_ , _4_ (1), 170145. https://doi.org/ 10.1038/sdata.2017.145 Aadhar, S., & Mishra, V. (2020). On the projected decline in droughts over South Asia in CMIP6 multimodel ensemble. _Journal of Geophysical Research: Atmospheres_ , _125_ (20), e2020JD033587. https://doi.org/10.1029/2020JD033587 Aadhar, S., & Mishra, V. (2021). On the occurrence of the worst drought in South Asia in the observed and future climate. _Environmental Research Letters_ , _16_ (2), 024050. https://doi.org/10.1088/1748‐9326/abd6a6 

AghaKouchak, A. (2014). A baseline probabilistic drought forecasting framework using standardized soil moisture index: Application to the 2012 United States drought. _Hydrology and Earth System Sciences_ , _18_ (7), 2485–2492. https://doi.org/10.5194/hess‐18‐2485‐2014 

Akaike, H. (1974). A new look at the statistical model identification. _IEEE Transactions on Automatic Control_ , _19_ (6), 716–723. https://doi.org/10. 1109/TAC.1974.1100705 Alessi, M. J., Herrera, D. A., Evans, C. P., DeGaetano, A. T., & Ault, T. R. (2022). Soil moisture conditions determine land‐atmosphere coupling and drought risk in the northeastern United States. _Journal of Geophysical Research: Atmospheres_ , _127_ (6), e2021JD034740. https://doi.org/10. 1029/2021JD034740 Aliyari Ghassabeh, Y., & Rudzicz, F. (2018). Modified mean shift algorithm. _IET Image Processing_ , _12_ (12), 2172–2177. https://doi.org/10.1049/ iet‐ipr.2018.5600 

Allen, R. G., Pereira, L. S., Raes, D., & Smith, M. (1998). _Crop evapotranspiration. Guidelines for computing crop water requirements_ . FAO Irrigation and Drainage Paper (FAO). Retrieved from https://scholar.google.com/scholar_lookup?title=Crop+evapotranspiration.+ Guidelines+for+computing+crop+water+requirements&author=Allen%2C+R.G.&publication_year=1998 

Altman, N., & Krzywinski, M. (2015). Association, correlation and causation. _Nature Methods_ , _12_ (10), 899–900. https://doi.org/10.1038/nmeth. 3587 Anand, N., Satheesh, S. K., & Moorthy, K. K. (2022). Land‐atmosphere interactions at a semi‐arid region in the Deccan Plateau. _Journal of Geophysical Research: Atmospheres_ , _127_ (21), e2022JD037211. https://doi.org/10.1029/2022JD037211 Apurv, T., & Cai, X. (2020). Drought propagation in contiguous U.S. watersheds: A process‐based understanding of the role of climate and watershed properties. _Water Resources Research_ , _56_ (9), e2020WR027755. https://doi.org/10.1029/2020WR027755 Apurv, T., Sivapalan, M., & Cai, X. (2017). Understanding the role of climate characteristics in drought propagation. _Water Resources Research_ , _53_ (11), 9304–9329. https://doi.org/10.1002/2017WR021445 Apurv, T., Xu, Y.‐P., Wang, Z., & Cai, X. (2019). Multidecadal changes in meteorological drought severity and their drivers in mainland China. _Journal of Geophysical Research: Atmospheres_ , _124_ (23), 12937–12952. https://doi.org/10.1029/2019JD031317 Aryal, J. P., Sapkota, T. B., Khurana, R., Khatri‐Chhetri, A., Rahut, D. B., & Jat, M. L. (2020). Climate change and agriculture in South Asia: Adaptation options in smallholder production systems. _Environment, Development and Sustainability_ , _22_ (6), 5045–5075. https://doi.org/10. 1007/s10668‐019‐00414‐4 

Barrow, C. J. (1992). World atlas of desertification (United Nations environment programme), edited by N. Middleton and D. S. G. Thomas. Edward Arnold, London, 1992. isbn 0 340 55512 2, £89.50 (hardback), ix + 69 pp. _Land Degradation and Development_ , _3_ (4). 249–249. https:// doi.org/10.1002/ldr.3400030407 

Beck, H. E., Wood, E. F., Pan, M., Fisher, C. K., Miralles, D. G., van Dijk, A. I. J. M., et al. (2019). MSWEP V2 global 3‐hourly 0.1° precipitation: Methodology and quantitative assessment [Dataset]. _Bulletin of the American Meteorological Society_ , _100_ (3), 473–500. https://doi.org/10. 1175/BAMS‐D‐17‐0138.1 Bhardwaj, K., Shah, D., Aadhar, S., & Mishra, V. (2020). Propagation of meteorological to hydrological droughts in India. _Journal of Geophysical Research: Atmospheres_ , _125_ (22), e2020JD033455. https://doi.org/10.1029/2020JD033455 Cai, J., Chen, T., Yan, Q., Chen, X., & Guo, R. (2022). The spatial‐temporal characteristics of soil moisture and its persistence over Australia in the last 20 years. _Water_ , _14_ (4), 598. https://doi.org/10.3390/w14040598 

Carrão, H., Naumann, G., & Barbosa, P. (2016). Mapping global patterns of drought risk: An empirical framework based on sub‐national estimates of hazard, exposure and vulnerability. _Global Environmental Change_ , _39_ , 108–124. https://doi.org/10.1016/j.gloenvcha.2016.04.012 Chatterjee, S., Desai, A. R., Zhu, J., Townsend, P. A., & Huang, J. (2022). Soil moisture as an essential component for delineating and forecasting agricultural rather than meteorological drought. _Remote Sensing of Environment_ , _269_ , 112833. https://doi.org/10.1016/j.rse.2021.112833 Cheng, S., & Huang, J. (2016). Enhanced soil moisture drying in transitional regions under a warming climate. _Journal of Geophysical Research: Atmospheres_ , _121_ (6), 2542–2555. https://doi.org/10.1002/2015JD024559 Cheng, Y. (1995). Mean shift, mode seeking, and clustering. _IEEE Transactions on Pattern Analysis and Machine Intelligence_ , _17_ (8), 790–799. https://doi.org/10.1109/34.400568 

Chiang, F., Mazdiyasni, O., & AghaKouchak, A. (2021). Evidence of anthropogenic impacts on global drought frequency, duration, and intensity. _Nature Communications_ , _12_ (1), 2754. https://doi.org/10.1038/s41467‐021‐22314‐w 

Cover, T. M., & Thomas, J. A. (2006). _Elements of information theory_ (2nd ed.). John Wiley & Sons, Inc. 

Crocetti, L., Forkel, M., Fischer, M., Jurečka, F., Grlj, A., Salentinig, A., et al. (2020). Earth Observation for agricultural drought monitoring in the Pannonian Basin (southeastern Europe): Current state and future directions. _Regional Environmental Change_ , _20_ (4), 123. https://doi.org/10. 1007/s10113‐020‐01710‐w 

Dai, M., Huang, S., Huang, Q., Zheng, X., Su, X., Leng, G., et al. (2022). Propagation characteristics and mechanism from meteorological to agricultural drought in various seasons. _Journal of Hydrology_ , _610_ , 127897. https://doi.org/10.1016/j.jhydrol.2022.127897 

Dralle, D. N., Hahm, W. J., Rempe, D. M., Karst, N., Anderegg, L. D. L., Thompson, S. E., et al. (2020). Plants as sensors: Vegetation response to rainfall predicts root‐zone water storage capacity in Mediterranean‐type climates. _Environmental Research Letters_ , _15_ (10), 104074. https://doi. org/10.1088/1748‐9326/abb10b 

Du, C., Chen, J., Nie, T., & Dai, C. (2022). Spatial–temporal changes in meteorological and agricultural droughts in Northeast China: Change patterns, response relationships and causes. _Natural Hazards_ , _110_ (1), 155–173. https://doi.org/10.1007/s11069‐021‐04940‐1 

Entekhabi, D. (2023). Propagation in the drought cascade: Observational analysis over the continental US. _Water Resources Research_ , _59_ (9), e2022WR032608. https://doi.org/10.1029/2022WR032608 

Entekhabi, D., Rodriguez‐Iturbe, I., & Castelli, F. (1996). Mutual interaction of soil moisture state and atmospheric processes. _Journal of Hydrology_ , _184_ (1), 3–17. https://doi.org/10.1016/0022‐1694(95)02965‐6 

Fang, W., Huang, S., Huang, Q., Huang, G., Wang, H., Leng, G., & Wang, L. (2020). Identifying drought propagation by simultaneously considering linear and nonlinear dependence in the Wei River basin of the Loess Plateau, China. _Journal of Hydrology_ , _591_ , 125287. https:// doi.org/10.1016/j.jhydrol.2020.125287 

18 of 21 

GUPTA AND KARTHIKEYAN 

**Earth's Future** 

10.1029/2024EF004674 

Funk, C., Peterson, P., Landsfeld, M., Pedreros, D., Verdin, J., Shukla, S., et al. (2015). The climate hazards infrared precipitation with stations— A new environmental record for monitoring extremes [Dataset]. _Scientific Data_ , _2_ (1), 150066. https://doi.org/10.1038/sdata.2015.66 Ganeshi, N. G., Mujumdar, M., Krishnan, R., & Goswami, M. (2020). Understanding the linkage between soil moisture variability and temperature extremes over the Indian region. _Journal of Hydrology_ , _589_ , 125183. https://doi.org/10.1016/j.jhydrol.2020.125183 

Gentine, P., Massmann, A., Lintner, B. R., Hamed Alemohammad, S., Fu, R., Green, J. K., et al. (2019). Land–atmosphere interactions in the tropics – A review. _Hydrology and Earth System Sciences_ , _23_ (10), 4171–4197. https://doi.org/10.5194/hess‐23‐4171‐2019 

Gevaert, A. I., Veldkamp, T. I. E., & Ward, P. J. (2018). The effect of climate type on timescales of drought propagation in an ensemble of global hydrological models. _Hydrology and Earth System Sciences_ , _22_ (9), 4649–4665. https://doi.org/10.5194/hess‐22‐4649‐2018 

Ghannam, K., Nakai, T., Paschalis, A., Oishi, C. A., Kotani, A., Igarashi, Y., et al. (2016). Persistence and memory timescales in root‐zone soil moisture dynamics. _Water Resources Research_ , _52_ (2), 1427–1445. https://doi.org/10.1002/2015WR017983 

Grayson, R. B., Western, A. W., Chiew, F. H. S., & Blöschl, G. (1997). Preferred states in spatial soil moisture patterns: Local and nonlocal controls. _Water Resources Research_ , _33_ (12), 2897–2908. https://doi.org/10.1029/97WR02174 

Green, J. K., Konings, A. G., Alemohammad, S. H., Berry, J., Entekhabi, D., Kolassa, J., et al. (2017). Regionally strong feedbacks between the atmosphere and terrestrial biosphere. _Nature Geoscience_ , _10_ (6), 410–414. https://doi.org/10.1038/ngeo2957 

Gupta, A., & Lanka, K. (2024). Role of initial conditions and meteorological drought on soil moisture drought propagation: An event‐based causal analysis over South Asia [Dataset]. _Earth’s Future_ . https://doi.org/10.5281/zenodo.12768601 

Han, J., & Singh, V. P. (2021). Impacts of Rossby wave packets and atmospheric rivers on meteorological drought in the continental United States. _Water Resources Research_ , _57_ (12), e2021WR029966. https://doi.org/10.1029/2021WR029966 

Hao, Z., Singh, V. P., & Xia, Y. (2018). Seasonal drought prediction: Advances, challenges, and future prospects. _Reviews of Geophysics_ , _56_ (1), 108–141. https://doi.org/10.1002/2016RG000549 

Heck, K., Coltman, E., Schneider, J., & Helmig, R. (2020). Influence of radiation on evaporation rates: A numerical analysis. _Water Resources Research_ , _56_ (10), e2020WR027332. https://doi.org/10.1029/2020WR027332 

Hersbach, H., Bell, B., Berrisford, P., Hirahara, S., Horányi, A., Muñoz‐Sabater, J., et al. (2020). The ERA5 global reanalysis [Dataset]. _Quarterly Journal of the Royal Meteorological Society_ , _146_ (730), 1999–2049. https://doi.org/10.1002/qj.3803 

Hirschi, M., Mueller, B., Dorigo, W., & Seneviratne, S. I. (2014). Using remotely sensed soil moisture for land–atmosphere coupling diagnostics: The role of surface vs. root‐zone soil moisture variability. _Remote Sensing of Environment_ , _154_ , 246–252. https://doi.org/10.1016/j.rse.2014. 08.030 

Ho, S., Tian, L., Disse, M., & Tuo, Y. (2021). A new approach to quantify propagation time from meteorological to hydrological drought. _Journal of Hydrology_ , _603_ , 127056. https://doi.org/10.1016/j.jhydrol.2021.127056 

Hu, X., Chen, W., & Xu, W. (2017). Adaptive mean shift‐based identification of individual trees using airborne LiDAR data. _Remote Sensing_ , _9_ (2), 148. https://doi.org/10.3390/rs9020148 

Huang, S., Li, P., Huang, Q., Leng, G., Hou, B., & Ma, L. (2017). The propagation from meteorological to hydrological drought and its potential influence factors. _Journal of Hydrology_ , _547_ , 184–195. https://doi.org/10.1016/j.jhydrol.2017.01.041 

Iwata, S. (2020). _Soil‐water interactions: Mechanisms applications_ (2nd ed.). CRC Press. Revised Expanded. 

Kazemzadeh, M., Noori, Z., Alipour, H., Jamali, S., Akbari, J., Ghorbanian, A., & Duan, Z. (2022). Detecting drought events over Iran during 1983–2017 using satellite and ground‐based precipitation observations. _Atmospheric Research_ , _269_ , 106052. https://doi.org/10.1016/j. atmosres.2022.106052 

Konapala, G., Mondal, S., & Mishra, A. (2022). Quantifying spatial drought propagation potential in North America using complex network theory. _Water Resources Research_ , _58_ (3), e2021WR030914. https://doi.org/10.1029/2021WR030914 

Konkathi, P., & Karthikeyan, L. (2024). Utility of L‐band and X‐band vegetation optical depth to examine vegetation response to soil moisture droughts in South Asia. _Remote Sensing of Environment_ , _301_ , 113933. https://doi.org/10.1016/j.rse.2023.113933 

Kraskov, A., Stögbauer, H., & Grassberger, P. (2004). Estimating mutual information. _Physical Review E_ , _69_ (6), 066138. https://doi.org/10.1103/ PhysRevE.69.066138 

Li, Q., Ye, A., Zhang, Y., & Zhou, J. (2022). The peer‐to‐peer type propagation from meteorological drought to soil moisture drought occurs in areas with strong land‐atmosphere interaction. _Water Resources Research_ , _58_ (9), e2022WR032846. https://doi.org/10.1029/2022WR032846 Li, W., Reichstein, M., O, S., May, C., Destouni, G., Migliavacca, M., et al. (2023). Contrasting drought propagation into the terrestrial water cycle between dry and wet regions. _Earth’s Future_ , _11_ (7), e2022EF003441. https://doi.org/10.1029/2022EF003441 

Lin, Q., Wu, Z., Zhang, Y., Peng, T., Chang, W., & Guo, J. (2023). Propagation from meteorological to hydrological drought and its application to drought prediction in the Xijiang River basin, South China. _Journal of Hydrology_ , _617_ , 128889. https://doi.org/10.1016/j.jhydrol.2022.128889 

Liu, C., Yang, C., Yang, Q., & Wang, J. (2021). Spatiotemporal drought analysis by the standardized precipitation index (SPI) and standardized precipitation evapotranspiration index (SPEI) in Sichuan Province, China. _Scientific Reports_ , _11_ (1), 1280. https://doi.org/10.1038/s41598‐020‐ 80527‐3 

Liu, Q., Yang, Y., Liang, L., Jun, H., Yan, D., Wang, X., et al. (2023). Thresholds for triggering the propagation of meteorological drought to hydrological drought in water‐limited regions of China. _Science of the Total Environment_ , _876_ , 162771. https://doi.org/10.1016/j.scitotenv. 2023.162771 

Manoj, J. A., Guntu, R. K., & Agarwal, A. (2022). Spatiotemporal dependence of soil moisture and precipitation over India. _Journal of Hydrology_ , _610_ , 127898. https://doi.org/10.1016/j.jhydrol.2022.127898 

Martens, B., Miralles, D. G., Lievens, H., van der Schalie, R., de Jeu, R. A. M., Fernández‐Prieto, D., et al. (2017). GLEAM v3: Satellite‐based land evaporation and root‐zone soil moisture [Dataset]. _Geoscientific Model Development_ , _10_ (5), 1903–1925. https://doi.org/10.5194/gmd‐10‐ 1903‐2017 

Massey, F. J. (1951). The Kolmogorov‐Smirnov test for goodness of fit. _Journal of the American Statistical Association_ , _46_ (253), 68–78. https:// doi.org/10.1080/01621459.1951.10500769 

McColl, K. A., Alemohammad, S. H., Akbar, R., Konings, A. G., Yueh, S., & Entekhabi, D. (2017). The global distribution and dynamics of surface soil moisture. _Nature Geoscience_ , _10_ (2), 100–104. https://doi.org/10.1038/ngeo2868 

McKee, T. B., Doesken, N. J., & Kleist, J. (1995). Drought monitoring with multiple time scales. In _Proceedings of 9th Conference on Applied Climatology, Boston_ (Vol. 1995, pp. 233–236). American Meteorological Society. Retrieved from https://cir.nii.ac.jp/crid/ 1571417125805810560 

Meresa, H., Zhang, Y., Tian, J., & Abrar Faiz, M. (2023). Understanding the role of catchment and climate characteristics in the propagation of meteorological to hydrological drought. _Journal of Hydrology_ , _617_ , 128967. https://doi.org/10.1016/j.jhydrol.2022.128967 Miralles, D. G., Gentine, P., Seneviratne, S. I., & Teuling, A. J. (2019). Land‐atmospheric feedbacks during droughts and heatwaves: State of the science and current challenges. _Annals of the New York Academy of Sciences_ , _1436_ (1), 19–35. https://doi.org/10.1111/nyas.13912 

19 of 21 

GUPTA AND KARTHIKEYAN 

**Earth's Future** 

10.1029/2024EF004674 

Mishra, A., Vu, T., Veettil, A. V., & Entekhabi, D. (2017). Drought monitoring with soil moisture active passive (SMAP) measurements. _Journal of Hydrology_ , _552_ , 620–632. https://doi.org/10.1016/j.jhydrol.2017.07.033 Mishra, A. K., Ines, A. V. M., Das, N. N., Prakash Khedun, C., Singh, V. P., Sivakumar, B., & Hansen, J. W. (2015). Anatomy of a local‐scale drought: Application of assimilated remote sensing products, crop model, and statistical methods to an agricultural drought study. _Journal of Hydrology_ , _526_ , 15–29. https://doi.org/10.1016/j.jhydrol.2014.10.038 Mishra, A. K., & Singh, V. P. (2010). A review of drought concepts. _Journal of Hydrology_ , _391_ (1–2), 202–216. https://doi.org/10.1016/j.jhydrol. 2010.07.012 Mondal, S. K., Huang, J., Wang, Y., Su, B., Zhai, J., Tao, H., et al. (2021). Doubling of the population exposed to drought over South Asia: CMIP6 multi‐model‐based analysis. _Science of the Total Environment_ , _771_ , 145186. https://doi.org/10.1016/j.scitotenv.2021.145186 Naumann, G., Barbosa, P., Carrao, H., Singleton, A., & Vogt, J. (2012). Monitoring drought conditions and their uncertainties in Africa using TRMM data. _Journal of Applied Meteorology and Climatology_ , _51_ (10), 1867–1874. https://doi.org/10.1175/JAMC‐D‐12‐0113.1 

Navale, A., & Karthikeyan, L. (2023). Understanding recycled precipitation at different spatio‐temporal scales over India: An Eulerian water tagging approach. _Water Resources Research_ , _59_ (1), e2022WR032605. https://doi.org/10.1029/2022wr032605 

Pei, Z., Fang, S., Wang, L., & Yang, W. (2020). Comparative analysis of drought indicated by the SPI and SPEI at various timescales in inner Mongolia, China. _Water_ , _12_ (7), 1925. https://doi.org/10.3390/w12071925 Peters, E., van Lanen, H. A. J., Torfs, P. J. J. F., & Bier, G. (2005). Drought in groundwater—Drought distribution and performance indicators. _Journal of Hydrology_ , _306_ (1), 302–317. https://doi.org/10.1016/j.jhydrol.2004.09.014 

Rodell, M., Houser, P. R., Jambor, U., Gottschalck, J., Mitchell, K., Meng, C.‐J., et al. (2004). The global land data assimilation system [Dataset]. _Bulletin of the American Meteorological Society_ , _85_ (3), 381–394. https://doi.org/10.1175/BAMS‐85‐3‐381 

Rousta, I., Olafsson, H., Moniruzzaman, M., Zhang, H., Liou, Y.‐A., Mushore, T. D., & Gupta, A. (2020). Impacts of drought on vegetation 

assessed by vegetation indices and meteorological factors in Afghanistan. _Remote Sensing_ , _12_ (15), 2433. https://doi.org/10.3390/rs12152433 Sattar, M. N., Lee, J.‐Y., Shin, J.‐Y., & Kim, T.‐W. (2019). Probabilistic characteristics of drought propagation from meteorological to hydrological drought in South Korea. _Water Resources Management_ , _33_ (7), 2439–2452. https://doi.org/10.1007/s11269‐019‐02278‐9 

Schönbeck, L. C., Schuler, P., Lehmann, M. M., Mas, E., Mekarni, L., Pivovaroff, A. L., et al. (2022). Increasing temperature and vapour pressure deficit lead to hydraulic damages in the absence of soil drought. _Plant, Cell & Environment_ , _45_ (11), 3275–3289. https://doi.org/10.1111/pce. 14425 Schumacher, D. L., Keune, J., Dirmeyer, P., & Miralles, D. G. (2022). Drought self‐propagation in drylands due to land–atmosphere feedbacks. _Nature Geoscience_ , _15_ (4), 262–268. https://doi.org/10.1038/s41561‐022‐00912‐7 

Schumacher, D. L., Keune, J., van Heerwaarden, C. C., Vilà‐Guerau de Arellano, J., Teuling, A. J., & Miralles, D. G. (2019). Amplification of mega‐heatwaves through heat torrents fuelled by upwind drought. _Nature Geoscience_ , _12_ (9), 712–717. https://doi.org/10.1038/s41561‐019‐ 0431‐6 Shannon, C. E. (1948a). A mathematical theory of communication. _The Bell System Technical Journal_ , _27_ (4), 623–656. https://doi.org/10.1002/j. 1538‐7305.1948.tb00917.x Shannon, C. E. (1948b). A mathematical theory of communication. _The Bell System Technical Journal_ , _27_ (3), 379–423. https://doi.org/10.1002/j. 1538‐7305.1948.tb01338.x 

Singer, M. B., Asfaw, D. T., Rosolem, R., Cuthbert, M. O., Miralles, D. G., MacLeod, D., et al. (2021). Hourly potential evapotranspiration at 0.1° resolution for the global land surface from 1981–present [Dataset]. _Scientific Data_ , _8_ (1), 224. https://doi.org/10.1038/s41597‐021‐01003‐9 Strehl, A., & Ghosh, J. (2002). Cluster ensembles – A knowledge reuse framework for combining multiple partitions. _Journal of Machine Learning Research_ , _3_ , 583–617. 

Tian, Q., Lu, J., & Chen, X. (2022). A novel comprehensive agricultural drought index reflecting time lag of soil moisture to meteorology: A case study in the Yangtze River basin, China. _Catena_ , _209_ , 105804. https://doi.org/10.1016/j.catena.2021.105804 Trenberth, K. (2011). Changes in precipitation with climate change. _Climate Research_ , _47_ (1), 123–138. https://doi.org/10.3354/cr00953 Van Loon, A. F. (2015). Hydrological drought explained. _WIREs Water_ , _2_ (4), 359–392. https://doi.org/10.1002/wat2.1085 Van Loon, A. F., Van Huijgevoort, M. H. J., & Van Lanen, H. A. J. (2012). Evaluation of drought propagation in an ensemble mean of large‐scale hydrological models. _Hydrology and Earth System Sciences_ , _16_ (11), 4057–4078. https://doi.org/10.5194/hess‐16‐4057‐2012 Vejmelka, M., & Paluš, M. (2008). Inferring the directionality of coupling with conditional mutual information. _Physical Review E_ , _77_ (2), 026214. https://doi.org/10.1103/PhysRevE.77.026214 

Vicente‐Serrano, S. M., Beguería, S., & López‐Moreno, J. I. (2010). A multiscalar drought index sensitive to global warming: The standardized precipitation evapotranspiration index. _Journal of Climate_ , _23_ (7), 1696–1718. https://doi.org/10.1175/2009JCLI2909.1 

Vorobevskii, I., Kronenberg, R., & Bernhofer, C. (2022). Linking different drought types in a small catchment from a statistical perspective – Case study of the Wernersbach catchment, Germany. _Journal of Hydrology X_ , _15_ , 100122. https://doi.org/10.1016/j.hydroa.2022.100122 

Wang, M., Jiang, S., Ren, L., Xu, C.‐Y., Menzel, L., Yuan, F., et al. (2021). Separating the effects of climate change and human activities on drought propagation via a natural and human‐impacted catchment comparison method. _Journal of Hydrology_ , _603_ , 126913. https://doi.org/10. 1016/j.jhydrol.2021.126913 Wu, J., Chen, X., Yao, H., Liu, Z., & Zhang, D. (2018). Hydrological drought instantaneous propagation speed based on the variable motion relationship of speed‐time process. _Water Resources Research_ , _54_ (11), 9549–9565. https://doi.org/10.1029/2018WR023120 Wu, W., & Dickinson, R. E. (2004). Time scales of layered soil moisture memory in the context of land–atmosphere interaction. _Journal of Climate_ , _17_ (14), 2752–2764. https://doi.org/10.1175/1520‐0442(2004)017<2752:TSOLSM>2.0.CO;2 Xu, T., Wu, X., Tian, Y., Li, Y., Zhang, W., & Zhang, C. (2021). Soil property plays a vital role in vegetation drought recovery in karst region of Southwest China. _Journal of Geophysical Research: Biogeosciences_ , _126_ (12), e2021JG006544. https://doi.org/10.1029/2021JG006544 Xu, Z., Wu, Z., Shao, Q., He, H., & Guo, X. (2023). From meteorological to agricultural drought: Propagation time and probabilistic linkages. _Journal of Hydrology: Regional Studies_ , _46_ , 101329. https://doi.org/10.1016/j.ejrh.2023.101329 Yang, F., Duan, X., Guo, Q., Lu, S., & Hsu, K. (2022). The spatiotemporal variations and propagation of droughts in Plateau Mountains of China. _Science of the Total Environment_ , _805_ , 150257. https://doi.org/10.1016/j.scitotenv.2021.150257 Yevjevich, V. (1967). An objective approach to definitions and investigations of continental hydrologic droughts. _Journal of Hydrology_ , _7_ (3), 353. https://doi.org/10.1016/0022‐1694(69)90110‐3 Yuan, W., Zheng, Y., Piao, S., Ciais, P., Lombardozzi, D., Wang, Y., et al. (2019). Increased atmospheric vapor pressure deficit reduces global vegetation growth. _Science Advances_ , _5_ (8), eaax1396. https://doi.org/10.1126/sciadv.aax1396 Zhang, Q., Miao, C., Gou, J., Wu, J., Jiao, W., Song, Y., & Xu, D. (2022). Spatiotemporal characteristics of meteorological to hydrological drought propagation under natural conditions in China. _Weather and Climate Extremes_ , _38_ , 100505. https://doi.org/10.1016/j.wace.2022.100505 

20 of 21 

GUPTA AND KARTHIKEYAN 

**Earth's Future** 

10.1029/2024EF004674 

- Zhang, T., Su, X., Zhang, G., Wu, H., Wang, G., & Chu, J. (2022). Evaluation of the impacts of human activities on propagation from meteorological drought to hydrological drought in the Weihe River Basin, China. _Science of the Total Environment_ , _819_ , 153030. https://doi.org/10. 1016/j.scitotenv.2022.153030 

- Zhang, X., Hao, Z., Singh, V. P., Zhang, Y., Feng, S., Xu, Y., & Hao, F. (2022). Drought propagation under global warming: Characteristics, approaches, processes, and controlling factors. _Science of the Total Environment_ , _838_ , 156021. https://doi.org/10.1016/j.scitotenv.2022.156021 

21 of 21 

GUPTA AND KARTHIKEYAN 

