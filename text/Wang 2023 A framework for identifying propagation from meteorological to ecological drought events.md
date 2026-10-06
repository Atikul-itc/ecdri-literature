Journal of Hydrology 625 (2023) 130142 



Contents lists available at ScienceDirect 

# Journal of Hydrology 

journal homepage: www.elsevier.com/locate/jhydrol 



#### Research papers 

## A framework for identifying propagation from meteorological to ecological drought events 



### Yihui Wang, Han Zhou<sup>*</sup> , Jiejun Huang, Jiaxin Yu, Yanbin Yuan 

_School of Resource and Environmental Engineering, Wuhan University of Technology, Wuhan, China_ 

|A R T I C L E I N F O|A B S T R A C T|
|---|---|
|_Keywords:_<br>Propagation<br>Meteorological drought<br>Ecological drought<br>GPP<br>SPEI|Drought severely affects vegetation growth owing to its multidimensional characteristics (e.g. duration and<br>severity). However, current studies regarding the propagation of meteorological to ecological drought are not<br>investigated well from an event-scale perspective. Therefore, a framework for identifying the propagation<br>relationship between meteorological and ecological drought at an event scale is proposed. The gross primary<br>productivity (GPP) and standardized precipitation evapotranspiration index are used to characterize ecological<br>and meteorological drought, respectively. The pooling of ecological drought events (GPP anomalous events, GAs)<br>and the exclusion of meteorological drought events (MDs) are considered in the framework. Matching events<br>between these two types of droughts are identified, and their propagation characteristics are analyzed. The<br>framework is tested in the Yangtze River Basin (YRB). The main results are as follows: (1) The propagation time<br>from meteorological to ecological drought in the YRB varied from 1 to 48 months, with significant spatiotem-<br>poral heterogeneity; (2) Four propagation types from meteorological to ecological drought are identified: mul-<br>tiple MDs trigger a GA (MTO), an MD triggers multiple GAs (OTM), an MD triggers a GA (OTO), and multiple<br>MDs trigger multiple GAs (MTM), which constituted 16.17%, 11.32%, 55.57%, and 16.94% of the total matching<br>events, respectively. Most of these events occur in semiarid and subhumid regions. In addition, OTO typically<br>occurs throughout the YRB. (3) For the four matching types, the average duration (or severity) of MDs (or GAs) is<br>in the order of MTM_>_OTM_>_MTO_>_OTO. For MTM and OTM, the duration of MD is longer (more severe) than<br>that of the GA caused by it, and a more significant linear relationship is indicated (_R_<sup>2</sup> _>_0_._7), whereas the<br>opposite is observed for OTM and OTO.|



##### **1. Introduction** 

Drought is a natural disaster that persists for a long duration and affects a large area (Haile et al., 2020; Mishra and Singh, 2010). Traditional drought classification is ’human-centred’ and can be classified into meteorological, hydrological, agricultural (soil moisture), and socioeconomic drought based on various factors (Wilhite and Glantz, 1985). Each type of drought is not independent of the others, drought propagation is the process by which one drought type can induce other types of drought through the water cycle (Peters et al., 2003; Van Loon et al., 2012). Currently, drought propagation efforts are mainly focused on meteorological, hydrological, and agricultural droughts (Gevaert et al., 2018; Wu et al., 2018a), but drought also has far-reaching impacts on the environmental system, Crausbay et al. (2017) proposed a new type of drought called ecological drought, which takes an ecological- 

centered approach. Ecological drought refers to the shortage of available water that affects the functioning and services of ecosystems, triggering negative feedback (Sadiqi et al., 2022). According to The Intergovernmental Panel on Climate Change Sixth Assessment Report, as the global warming intensifies in the future, more regions will be affected by increased agro-ecological drought (Seneviratne et al., 2021). As ecosystems (e.g. vegetated ecosystems) are an important component in maintaining the global carbon balance, understanding the propagation of drought to vegetated ecosystems can provide critical support for maintaining the stability of terrestrial ecosystem structures and functions (Vicente-Serrano et al., 2020). 

Ecosystem response mechanisms to drought stress are complex. First, various drought types and event properties (e.g. occurrence time, intensity, and duration) may impose diverse effects on ecosystems. For example, in terms of drought type, Xu et al. (2021) discovered that 

* Corresponding author. 

_E-mail addresses:_ 320787@whut.edu.cn (Y. Wang), hanzhou0925@whut.edu.cn (H. Zhou), hjj@whut.edu.cn (J. Huang), jx_y@whut.edu.cn (J. Yu), yybjm@126. com (Y. Yuan). 

https://doi.org/10.1016/j.jhydrol.2023.130142 Received 4 April 2023; Received in revised form 23 July 2023; Accepted 23 August 2023 Available online 11 September 2023 0022-1694/© 2023 Elsevier B.V. All rights reserved. 

_Journal of Hydrology 625 (2023) 130142_ 

_Y. Wang et al._ 

atmospheric water deficit imposed a greater effect on the gross primary productivity (GPP) in real time than soil moisture drought, whereas Yuan et al. (2019) emphasized that atmospheric drought exerted a significantly stronger inhibitory effect on vegetation growth than soil moisture drought. In terms of drought occurrence time, droughts, that occur at or immediately after the peak vegetation growth are more likely to affect the productivity of ecosystems (Jiao et al., 2022). Second, the sensitivity and vulnerability of vegetation to drought vary by ecosystem and climatic region. Grasslands were the most sensitive to drought, followed by shrubs and forests (Sun et al., 2021; Zhang et al., 2017). In contrast to the case in semiarid and subhumid regions, vegetation in humid areas was less sensitive to drought (Sun et al., 2021) but recovered more rapidly from drought. Owing to the high-level resistance of the ecosystem, the GPP may not respond to droughts of shorter durations and lower severity (Gazol et al., 2017). Finally, changes in vegetation are not necessarily attributed to drought alone. Solar radiation, heat waves, wildfires, and human activities affect vegetation conditions by altering the available water (Wang et al., 2020a). 

Currently, the complex mechanisms of vegetation response to drought are revealed and the propagation characteristics from other droughts to ecological drought are quantified based on statistical analysis methods such as correlation analysis and joint probability modeling (Weng et al., 2023). In the correlation analysis methods, the ecosystem response to drought is assessed mainly through the correlation between the vegetation and the drought index (Zhang et al., 2022b). For instance, Wei et al. (2022b) calculated the correlation between the standardized precipitation evapotranspiration index (SPEI) and GPP at different time scales to investigate the spatiotemporal patterns of drought’s legacy effects on global grasslands. The joint probabilistic modeling methods can quantify the propagation probability from drought to ecological drought and assess the propagation thresholds for drought triggering different levels of ecological drought (Fang et al., 2019). For example, Jiang et al. (2023) calculated the probability of meteorological drought triggering different levels of ecological drought using a hybrid machine learning copula method. However, there are limitations in using statistical analyses to study the complex mechanisms and processes of ecosystem response to drought (Schwalm et al., 2017; Yu et al., 2017). The drought index is not necessarily associated closely with the ecological index and does not necessarily affect the ecosystem output (Liu et al., 2019). For example, high temperature and intense radiation are typically regarded as the dominant factors limiting vegetation productivity, whereas in the high latitudes of the Northern Hemisphere and the Tibetan Plateau, these factors are more significant during drought conditions but increase vegetation productivity (Jiao et al., 2021; Myneni et al., 1997; Nemani et al., 2003; Wang et al., 2021). Therefore, it is essential to consider the climatic conditions that trigger ecological drought and identify the drought events that truly cause vegetation reduction. 

Although the relationship between drought and vegetation conditions has been extensively investigated, researchers have not identified a method to objectively characterize the propagation of meteorological drought into vegetative ecosystems. In particular, the quantification of propagation characteristics from meteorological to ecological drought at the event scale, considering climatic conditions, has not been conducted. The ecosystem will be affected by more complicated and severe droughtrelated consequences in the future owing to the increasing intensity, frequency, and duration of droughts (Sheffield and Wood, 2008). Therefore, the complex propagation process from meteorological to ecological drought must be determined at the event scale, and the propagation properties must be quantified. Here, a methodological framework is proposed that matches meteorological drought events (MDs) with ecological drought events (i.e. GPP anomalous events (GAs)). The framework is used to identify the characteristics and relationship types of the propagation from MDs to GAs. The Yangtze River Basin (YRB) in China is selected as the experimental area. The SPEI is used to characterize MDs, and GPP anomalous are used to characterize 

ecological drought. The framework comprises four contents: (1) identifying MDs and GAs, (2) excluding MDs that do not trigger GAs by considering the hydrothermal conditions affecting GPP growth, (3) matching the MDs and GAs, and (4) quantifying the relationships between the propagation characteristics of the optimized matching events. 

##### **2. Materials** 

##### _2.1. Study area_ 

The Yangtze River originates from Qinghai Province and flows through 11 provinces, including Tibet and Sichuan. The YRB (24<sup>◦</sup> 30′–35<sup>◦</sup> 45′N, 90<sup>◦</sup> 33′–122<sup>◦</sup> 25′E) is located in Southern China (Fig. 1a) and encompasses an area of approximately 1.8 million km<sup>2</sup> The YRB is sensitive to global change and exhibits highland mountainous and subtropical monsoon climates (Liu et al., 2022). Based on the mean annual water balance (precipitation minus potential evapotranspiration) method (Vicente-Serrano et al., 2013), the YRB can be classified into arid, semiarid, subhumid, and humid regions from west to east (Fig. 1b). The overall spatial distribution of mean multiyear GPP values in the basin is high in the southeast and low in the northwest (Fig. 1c). Its terrain is complex and diverse (Fig. 1a). Owing to the effects of climate and terrain, the multiyear mean temperatures in the Tibetan Plateau region and other regions within the YRB are approximately -5<sup>◦</sup> C and 16<sup>◦</sup> C–18<sup>◦</sup> C, respectively (Fig. 1d), and the multiyear mean precipitation is approximately 1100 mm, with the spatial distribution increasing from northwest to southeast (Chen et al., 2018). 

##### _2.2. Data_ 

##### _2.2.1. GPP dataset_ 

GPP data were obtained from an 8-day GPP dataset based on a revised Eddy Covariance-Light Use Efficiency model estimated by Yuan (available online at (https://doi.org/10.6084/m9.figshare.8942336. v3)) over the period 1982–2018 with a spatial resolution of 0.05<sup>◦</sup> . This GPP dataset was verified to perform better than MODIS-GPP (Zheng et al., 2020) and provide reliable long-term GPP estimates. 

##### _2.2.2. Drought index time series_ 

In this study, the SPEI is used to characterize wet and dry conditions in the YRB (Vicente-Serrano et al., 2010), with a negative (positive) SPEI indicating that the water balance is less (greater) than the regional multiyear average. The Digital Institutional Repository of the Spanish National Research Council provides a global multi-temporal-scale SPEI dataset at 0.5<sup>◦</sup> spatial resolution for the period 1901–2020 (https://sac. csic.es/spei/index.html). In this study, SPEI datasets from this institutional repository for 1 to 48 months in the period 1982–2018 were selected and then interpolated to 0.05<sup>◦</sup> . 

##### _2.2.3. Meteorological data_ 

Monthly average precipitation, potential evapotranspiration, and near-surface temperature data were obtained from the Centre for Climate Research version 4.05 time series dataset of the University of East Anglia (https://catalogue.ceda.ac.uk/uuid/c26a65020a5e4 b80b20018f148556681). This dataset included global monthly meteorological data with a spatial resolution of 0.5<sup>◦</sup> from 1901 to 2020. To match the temporal extent and spatial resolution of the GPP dataset, data from the period 1982–2018 were selected and interpolated to 0.05<sup>◦</sup> in this study. 

##### **3. Methods** 

##### _3.1. Framework for identifying propagation relationship from meteorological to ecological drought_ 

Fig. 2 illustrates the framework used to identify the propagation 

2 

_Journal of Hydrology 625 (2023) 130142_ 

_Y. Wang et al._ 



**Fig. 1.** Spatial distribution of a) elevation, b) climate region based on annual mean water balance (which includes the secondary sub-basins of the YRB, YLJ = Yalong River basin; MJ = Min River basin; WJ = Wu River basin; JLJ = Jialing River basin; HJ = Han River basin; M = mainstream; DTH = Dongting Lake basin; PYH = Poyang Lake basin; TH = Tai Lake basin), c) annual mean GPP, and d) annual mean temperature in the YRB. 



**Fig. 2.** Framework for identifying propagation relationships of meteorological to ecological drought. 

relationship between meteorological drought and ecological drought. First, MDs and GAs were identified, and some GAs might be merged based on certain rules (Section 3.1.1). Based on hydrothermal conditions, sensitivity analyses were conducted to determine the exclusion threshold and to exclude MDs that did not result in GAs (Section 3.1.2). Finally, based on the pooled GAs and the optimized MDs, the two types of events were matched and classified based on their start times, end times, and trigger intervals. Subsequently, the characteristics of the matched events under different types were identified and analyzed 

(Section 3.1.3). 

_3.1.1. Identification of meteorological drought and GPP anomalous events_ 

(1) GPP anomalous events identification. 

Considering that drought-induced GPP reduction is the main cause of changes in terrestrial carbon sinks (Piao et al., 2019), we used GPP anomalies to characterize ecological drought. In this study, the 8-day 

3 

_Journal of Hydrology 625 (2023) 130142_ 

_Y. Wang et al._ 

GPP dataset was aggregated into a monthly GPP dataset. Considering other factors that significantly affect the GPP, such as land use changes, we removed the linear trend of GPP for each month (Wang et al., 2022) and calculated the standard deviation of the detrended GPP ( _StdGPP_ ) using Eq. (1). A GA was defined as at least three months with an _StdGPP_ of less than 0. The duration and severity of the GAs and MDs were determined based on the run theory (Yevjevich, 1966). 



where y is the year from 1982 to 2018, c is the month, _mean_ ( _GPP_ (1982− 2018 _,c_ ) ) represents the mean GPP for month c for the period 1982–2018, and _sd_ ( _GPP_ (1982− 2018 _,c_ ) ) represents the standard deviation of the GPP for the c of 1982–2018. 

However, similar to the case of drought events, a significant GA may be identified as several mild interdependent GAs owing to short-term fluctuations in external conditions (Tu et al., 2019). Based on the pooling method for drought events (Zelenhasi´c and Salvai, 1987), if _GAi_ and _GAi_ +1 are separated by one month and the cumulative GPP departure during _GAi_ exceeds the GPP departure for the intervening month, then _GAi_ and _GAi_ +1 are merged into one event. The duration ( _t_ ) and severity ( _se_ ) are calculated as follows: 



where _ti, sei_ and _ti_ +1 _, sei_ +1 represent the duration and severity of _GAi_ and _GAi_ +1, respectively. 

(2) Identification of meteorological drought events. 

The cumulative month p (1 ≤ p ≤ 48) corresponding to the maximum absolute value of the Pearson correlation coefficient between the _StdGPP_ and the multiple time scales SPEI-p ( _p_ = 1 _,_ 2 _,_ ⋯ _,_ 48) is 

selected as the dominant time scale of MD to GA (SPEI-p has a significant linear relationship and homoscedasticity with _StdGPP_ , see Fig. S5 and Fig. S6) (Luo et al., 2020; Pena-Gallardo et al., 2019; Xu et al., 2020; ˜ Zhang et al., 2017). Additionally, p is the propagation time of MD to GA (Haslinger et al., 2014), and represents GPP losses due to water balance deficits in the previous p months. An MD is defined as an SPEI-p with a value of less than 0 for at least three months. 

##### _3.1.2. Exclusion of meteorological drought events_ 

- (1) Calculation of optimum temperature range. 

During MDs, the optimum temperature ranges and sufficient water balance may result in high GPP levels, and such MDs must be excluded. Brief examples follow (Fig. S1 and Fig. S2). Both water balance and temperature were considered within the other region, and only temperature was considered within the Tibetan Plateau region. 

The temperature response curve (Fig. 3) was first fitted using the GPP and temperature (Huang et al., 2019; Niu et al., 2012; Yang et al., 2021); _GPPmax_ is the maximum value of GPP on the temperature response curve, and GPP reached m% of _GPPmax_ in the optimum temperature range. The temperature-response curve between _GPPmax_ and _m_ % × _GPPmax_ was used to determine the optimum temperature range [ _tmpmin, tmpmax_ ]. 

- (2) Calculation of minimum water balance. 

Water balance is different from the optimum temperature. When an MD occurs, the water balance is typically less than average. Therefore, only the minimum water balance that satisfies photosynthesis ( _wbmin_ ) must be considered. 





**Fig. 3.** Schematic diagram showing the calculation of optimum temperature range (grey dots represent monthly GPP values, orange dots represent the 90th percentile for each 1<sup>◦</sup> C temperature bin, and their connecting line is the temperature response curve). (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.) 

4 

_Journal of Hydrology 625 (2023) 130142_ 

_Y. Wang et al._ 

where _wb_<sup>_i_</sup> 90 _th_<sup>is the 90th percentile of monthly water balance in a year</sup> _i_ , calculating _wbmin_ using the 70th percentile, 75th percentile, 80th percentile, and 85th percentile return similar conclusions (Fig. S3 and Fig. S4). _mean_ (∑ _i_ 2018=1982<sup>_wbi_</sup> 90 _th_ ) is the average of the 90th percentile of water balance in the period 1982–2018, and _n_ %(0 ≤ _n_ ≤ 100) is the percentage. 

- (3) Rules for excluding meteorological drought events. 

An _MDi_ is excluded if it satisfied the conditions in Eq. (4). 



where _di_ is the duration of _MDi_ (months); _d_ 1 is the total number of months during _MDi_ where the temperature is within [ _tmpmin, tmpmax_ ]; _d_ 2 is the total number of months during _MDi_ where the water balance exceeds _wbmin_ ; and _r_ 1 and _r_ 2 are the thresholds. Sensitivity analyses for parameters _m, n, r_ 1 _, and r_ 2 were performed as described in Section 5.1. 

##### _3.1.3. Matching of meteorological drought and GPP anomalous events_ 

- (1) Matching methods. 

where _d_ and _sMD_ are the duration and severity of the matched MDs, respectively; where _t_ and _sGA_ are the duration and severity of the matched GAs, respectively; and _k_ and _l_ represent the occurrence of _k_ MDs coinciding with the ETI of _l_ GAs. 

##### (2) Types of propagation events. 

Based on the causes, propagation events can be classified into four types. When a GA occurs and its intensity undergoes an increasing–decreasing–increasing trend, and the MD that caused it undergoes the occurrence–end–occurrence process, the propagation type is known as MTO (Fig. 5a). OTM is the occurrence of only one MD with an increasing–decreasing–increasing intensity, resulting in several GAs that undergo an occurrence–end–reoccurrence pattern (Fig. 5b). Both the MD and the GA that it triggers undergo an occurrence–end process only, which is known as the OTO type (Fig. 5c). MTM is one of the most complex types and involves the simultaneous occurrence of the first three types. For example, MD1 triggers GA1 and GA2, and MD2 triggers GA2 and GA3, both of which belong to the OTM; however, GA2 may be caused by MD1 and MD2 simultaneously. Hence, the propagation type is MTO, whereas MD3 results only in GA3, which belongs to OTO. When the three types above occur simultaneously, we assume that MD1, MD2, and MD3 simultaneously result in GA1, GA2, and GA3, which belong to the fourth type of MTM (Fig. 5d). In this case, all MDs and GAs undergo the occurrence–end–occurrence process. 

Before matching MDs and GAs, the event trigger interval (ETI) was calculated using the method described by Guo (Guo et al., 2020). Fig. 4 shows the ETI calculation details. Only MDs whose occurrence times overlap with the ETI may result in GAs, which are calculated as follows: 



where _tei_ is the end time of _GAi_ ; _tsi_ +1 and _tei_ +1 are the start and end times of _GAi_ +1, respectively; and p represents a GA that started responding to an MD p months before its occurrence (see Section 3.1.1). 

If the occurrence of _MDi_ overlaps with the ETI corresponding to _GAi_ , then _MDi_ is considered to have caused _GAi_ and matched. The duration and severity of the matched MDs and GAs can be expressed as: 



##### **4. Results** 

##### _4.1. Correlation between SPEI and GPP_ 

Fig. 6a shows the spatial distribution of the Pearson correlation coefficients with the highest absolute values between _StdGPP_ and the multiple time scale SPEI-p (p = 1, 2, ⋯, 48) (p _<_ 0.05). In the highaltitude Tibetan Plateau region, most pixels of the SPEI and GPP were negatively correlated, which indicates the need for the exclusion of MDs. Most of the YRB showed positive correlations, particularly in the southern Yalong River basin, Dongting Lake basin, and Poyang Lake basin, where the correlation coefficient was the highest at 0.6. 

By comparing the correlation between the SPEI and _StdGPP_ at multiple time scales, the spatial distribution of the propagation time from MDs to GAs was obtained by comparing the correlation between SPEI and _StdGPP_ at multiple timescales (Fig. 6b). The propagation times ranged from 1 to 48 months across the YRB, with an average of 17 months. The propagation times in the southern Yalong River basin and Han River basin were shorter (within 12 months). The correlation coefficients for the Poyang Lake basin and the Yalong River basin were consistent, but the propagation times differed significantly. 



**Fig. 4.** ETI calculation schematic diagram. 

5 

_Journal of Hydrology 625 (2023) 130142_ 

_Y. Wang et al._ 



**Fig. 5.** Schematic representation of the four matching types: a) MTO; b) OTM; c) OTO; d) MTM. 



**Fig. 6.** Spatial distribution of a) maximum correlation coefficients between _StdGPP_ and SPEI; b) propagation time. 

_4.2. Identified meteorological drought and GPP anomalous events_ 

Fig. 7 shows the spatial distribution of the number, average duration, and severity of MDs and GAs identified in the YRB. The results show that the greater the number of MDs, the shorter (less severe) their duration (severity) at the same location within the YRB. For example, frequent and short-duration MDs with low severity were discovered in the Yalong River basin, Han River basin, and southwest of the Poyang Lake basin, where the number of MDs exceeded 20 and their duration was less than 10 months. MDs of long duration and high severity tended to occur in the Min River basin, Jialing River basin, and south of the Yangtze River (Fig. 7a – c). 

##### _4.3. Analysis of matching event characteristics_ 

After matching and classifying the MDs and GAs, the spatial distribution of the number and proportion of the four matching types was obtained, and box plots of the number of matches for the nine sub-basins were constructed (Fig. 8). However, the number of OTO events varied significantly among the nine sub-basins (Fig. 8g), with the average number of events in Han River basin being six and most of the pixels being between five and eight, whereas the average number of events for Wu River basin, Tai Lake basin, and Poyang Lake basin was less than two. The number of events in the other three matching types varied less among the nine sub-basins, with fewer than three fields (Fig. 8i – l). 

Compared with the case of OTO, the probability of MTO, OTM, and MTM occurring in the YRB is lower (Fig. 8); however, when these three 

6 

_Journal of Hydrology 625 (2023) 130142_ 

_Y. Wang et al._ 



**Fig. 7.** Spatial distribution of number, average duration, and average severity of identified MDs and GAs. (a, b, c represent the number, average duration, and average severity of identified MDs, respectively; d, e, f represent the number, average duration, and average severity of identified GAs, respectively). 



**Fig. 8.** In MTO, OTM, OTO, MTM: (a–d) spatial distribution of the number of matched events; (e–h) box plots of the number of matching events in the sub-basin; (i–l) spatial distribution of the proportion of the number of matched events. 

types of events occur, the duration and severity of their corresponding MDs and GAs can be much higher than those of OTO. The average duration (severity) was the longest (highest) in MTM, and the duration of MD and GA reached 60 months (Fig. 9m and n) and severity of 60 (Fig. 9o and p) in regions such as the Dongting Lake basin and Wu River basin south of the Yangtze River, respectively. Droughts of this matching type cause long-lasting and severe losses in the terrestrial ecosystem GPP. Under OTM, the average duration and severity of the events were the second highest, with an average duration of 40 months in the Sichuan Basin and the southern region of the Dongting Lake basin (Fig. 9e and f), and an average severity exceeding 40 in Wu River basin and Dongting Lake basin (Fig. 9g and h). The average severity (average duration) of the events under MTO was approximately 20 (months) (Fig. 9a – d), mainly in the Yalong River basin, Han River basin, and southwestern Poyang Lake basin. The average severity of the OTO events was less than 20 in all cases. 

and GAs for different types of propagation relationships are shown in Figs. 10 and 11, respectively. Significant linear relationships (p _<_ 0.05) were indicated between the MDs and GAs throughout the different water balance subregions. 

In OTM and MTM, most of the scatter and fitted lines were above the 1:1 dashed line, indicating that the duration and severity of the MDs were greater than those of the GAs. Conversely, in MTO and OTO, shorter-duration (less severe) MDs were more likely to result in longerduration (more severe) GAs. In addition, the duration and severity of the matching events did not exhibit highly significant linear relationships with OTO ( _R_<sup>2</sup> _<_ 0 _._ 3). 

Within the different climatic regions, the highest numbers of MDs and GAs were observed in the semiarid and subhumid regions, and the severity was higher in both OTM and MTM than in the humid and arid regions. By contrast, matched events within the arid regions were the shortest and least severe. 

Scatter density plots of the duration and severity of the matched MDs 

7 

_Journal of Hydrology 625 (2023) 130142_ 

_Y. Wang et al._ 



**Fig. 9.** Spatial distribution of (a, e, i, m) average duration (months), (b, f, j, n) average severity of GAs; (e, g, k, o) average duration (months), (d, h, l, p) average severity of MDs under the four matching types. 

##### **5. Discussions** 

##### _5.1. Rationality of the methodology_ 

The cumulative effects of drought on vegetation were considered. Drought can affect vegetation photosynthesis and reduce tree growth for up to four years (Anderegg et al., 2015; Br´eda et al., 2006). Therefore, the SPEI with the most significant effect on the GPP was selected as the dominant time scale for the 1–48 month time scales. 

In this study, the spatial heterogeneity of the dominant factors limiting the GPP in the YRB was considered based on hydrothermal conditions. MDs that did not decrease the GPP were excluded. Hydrothermal conditions and the combination of precipitation and temperature were key factors affecting the spatial distribution of vegetation (Zhang et al., 2017). In the Tibetan Plateau region, the GPP was negatively correlated with the SPEI-p (Fig. 6a) as it was mainly temperaturelimited (Wei et al., 2022a; Zhang et al., 2022a). Therefore, within the Tibetan Plateau region, if the temperature during an MD remains within the optimum temperature range for vegetation growth, then it is excluded. The MD determined based on the SPEI represents only extreme events in a statistical sense (Reichstein et al., 2013). In the other region, which was mostly subhumid and humid (Fig. 1b), even when the SPEI was negative, the water balance index remained positive and did not trigger vegetation loss. Therefore, within this region, if the temperature and water balance during MD are appropriate for vegetation growth, then they are excluded. 

As each pixel has distinct hydrothermal conditions, the optimum temperature range and water balance required for vegetation growth are different, and the values of parameters _m, n, r_ 1 _, and r_ 2 are ambiguous. A sensitivity analysis was performed to determine the values of parameters _m, n, r_ 1 _, and r_ 2 for each pixel, where _m_ and _n_ were obtained from 50 to 90 at intervals of 5 (81 values in total) and at each value of _m_ and _n_ , the optimum temperature range corresponded to the minimum water balance (Fig. 3, Eq. (3)). However, _r_ 1 _and r_ 2 were not yet determined. Based on the case of _m_ = 50 _and n_ = 50 as an example (Fig. 12a), the _r_ 1 and _r_ 2 were set from 0.1 to 1 at intervals of 0.1, and the total number of MDs excluded was counted based on the specific pixel in these 100 cases. As shown in Fig. 12a, the number of MDs excluded varied significantly 

from _r_ 2 = 0 _._ 2 to _r_ 2 = 0 _._ 3 and from _r_ 1 = 0 _._ 7 to _r_ 1 = 0 _._ 8, after which the number of MDs excluded stabilized. Therefore, we determined that _r_ 1 = 0 _._ 8 _and r_ 2 = 0 _._ 3 for _m_ = 50 _and n_ = 50 (point R in Fig. 12a). Subsequently, we determined the values of _r_ 1 and _r_ 2 for different values of _m_ and _n_ , respectively (R points of Fig. 12b, 81 in total), and the number of drought events was excluded (values obtained for each layer of the colour bands in Fig. 12b). Finally, a sensitivity analysis of these 81 R points was conducted using the method shown in Fig. 12a, and _m_ and _n_ were obtained, which corresponded to the mutation point when it finally became stable. Once _m_ and _n_ of this pixel were determined, _r_ 1 and _r_ 2 were subsequently determined. 

##### _5.2. Rationality of matching results_ 

##### _5.2.1. Spatial and temporal distribution characteristics of different matching types_ 

The spatial distributions of the average duration and severity of the matched MDs and GAs were consistent with the annual mean water balance (Fig. 1b and Fig. 9). In contrast to the case of the arid and humid zones, the vegetation in the semiarid and subhumid zones was more sensitive to drought (Figs. 10 and 11), which is consistent with the findings of Zhang, i.e. vegetation in semiarid and subhumid zones require a longer duration to recover from drought (Zhang et al., 2021). Similar findings have been reported (Gouveia et al., 2017; Pasho et al., 2011; Poulter et al., 2014). Vegetation in arid regions adapts to waterdeficit conditions over the long term through different physiological and functional mechanisms (Chaves et al., 2003), and these droughtresistant genes enable plants to survive under drought conditions (Craine et al., 2013). The Han River basin is an exception of the semiarid and subhumid regions, as it shows the shortest vegetation response time to drought (Fig. 6b), and its MDs and GAs are frequent but short. Therefore, the basin indicated the highest number of OTO events (Fig. 8e), and the number of OTO events within the semiarid and subhumid regions exceeded 70,000. Within humid regions, higher soil water use efficiency coupled with a higher soil water storage capacity during non-drought periods can relieve drought stress and temporarily recover the GPP. However, if the drought duration and severity continue to increase, then the GPP will deteriorate. 

8 

_Journal of Hydrology 625 (2023) 130142_ 

_Y. Wang et al._ 



**Fig. 10.** Scatter density plots of GA and MD duration in arid, semiarid, subhumid, and humid regions under the four matching types (dashed grey lines represent y = x; N is the sample size, the scatter density is calculated from the normalized kernel density). 

_5.2.2. Possible reasons for the various matching types_ 

In MTO, a GA continued to occur during multiple MDs intervals (Fig. 5a), and temporary increases in precipitation and decreases in evapotranspiration did not cause the GPP to return to its normal level. This type of event might occur under deeper-rooted vegetation types such as forest and scrub (Sun et al., 2021). In such cases, the temporary water balance during the MDs interval would not replenish the deeper roots of the forest, thus causing lagged vegetation growth and persistent GPP anomalies (Breshears et al., 2005; Wu et al., 2018b). However, the soil moisture might have been excessively depleted by vigorous vegetative growth before the GPP anomaly occurred (Lian et al., 2020; Wang et al., 2020b). The increase in evapotranspiration caused by the MDs exacerbated the soil moisture anomaly (Chen et al., 2022) and did not fully supply the depleted soil moisture during the interval. In addition, no pooling of MDs was performed in this study, resulting in events associated with OTO being judged as MTO. 

OTM is the opposite of MTO, where MD persists but short-term increases in precipitation or decreases in evapotranspiration are sufficient to temporarily recover the GPP to normal levels. The vegetation condition is determined by a combination of drought and human activities 

(Fang et al., 2019), and changes in other relevant factors (e.g. enhanced solar radiation) may result in a temporary recovery of the GPP during drought (Wang et al., 2021). However, such events may occur in shallow-rooted vegetation, such as grasslands, which have rapid access to soil moisture from precipitation recharge thus, (Craine et al., 2013; Sala et al., 1992), allowing the GPP to recover temporarily. 

Two conditions exist within OTO. The former, where MDs and GAs occur simultaneously, generally occurs in the summer, and the compounding effects of heat and drought on vegetation productivity are nonlinearly superimposed (Dannenberg et al., 2022; Zhu et al., 2021), thus resulting in a rapidly responding GPP. The latter, MD occurred before the GA, which is similar to MTO, in that the vegetation did not immediately respond to meteorological drought. 

MTM is a complex process that includes (1) the occurrence of MD and the recovery of a GA, and (2) the occurrence of a GA at the end of an MD. It combines the first three types and is the result of the interaction among the underlying surface factors, and meteorological fluctuations. 

9 

_Journal of Hydrology 625 (2023) 130142_ 

_Y. Wang et al._ 



**Fig. 11.** Scatter density plots of GA and MD severity in, arid, semiarid, subhumid, and humid regions under the four matching types (dashed grey lines represent y = x; N is the sample size, the scatter density is calculated from the normalized kernel density). 



**Fig. 12.** Schematic illustration showing parameters _m, n, r_ 1 _, and r_ 2 determined via sensitivity analysis. 

**6. Conclusions** 

Herein, a framework for matching meteorological and ecological 

drought events was proposed to identify meteorological-ecological drought propagation relationships and characteristics at the event scale. The YRB was selected as an example, and the GPP anomaly was 

10 

_Journal of Hydrology 625 (2023) 130142_ 

_Y. Wang et al._ 

used to characterize ecological drought, whereas the SPEI was used to characterize meteorological drought. The run theory was used to determine the characteristics of MDs and GAs in terms of events, duration, and severity. Additionally, sensitivity analysis was performed to determine the optimum hydrothermal conditions for vegetation photosynthesis, where MDs that did not trigger GAs were excluded. Finally, MDs and GAs were matched by considering the propagation time relationship; the matched events were classified, and the characteristic relationships of the propagation events under different types were statistically calculated. The main conclusions are as follows: 

- (1) The spatiotemporal heterogeneity in the propagation time of meteorological–ecological droughts was significant. The propagation time from MDs to GAs ranged from 1 to 48 months across the YRB, with an average of 17 months. The MDs in the northern region of the YRB were frequent (more than 40) and short (within 10 months), whereas the opposite was observed in the southern region. 

- (2) Four types of meteorological–ecological drought event propagation and their spatial distribution characteristics were identified. Meteorological drought to GPP anomalies propagation was classified into four types: MTO, OTM, OTO, and MTM, all of which were mainly distributed in the semiarid and subhumid regions. Among them, OTO was mainly distributed in the Han River basin. 

- (3) The propagation characteristics of different types of meteorological–ecological drought events were quantified. In terms of the matching numbers, OTO was the most prevalent, with an average of three events per pixel identified across the YRB. The average duration (or severity) of the two event types ranked in the order of magnitude was as follows: MTM _>_ OTM _>_ MTO _>_ OTO. In terms of the corresponding characteristics (e.g. duration and severity) of the two events, MDs indicated a longer duration (greater severity) than GAs under MTM and OTM, and their linear relationships were more significant ( _R_<sup>2</sup> _>_ 0 _._ 7), whereas the opposite was observed for OTM and OTO. MTO might be related to vegetation roots and pre-vegetation activity, which might be related to other factors intervening in the propagation process and vegetation roots. The OTO might be related to hightemperature events and lagged effects, and the MTM is a complex combination of the first three types. 

This study provides a better understanding of drought propagation and provides methodological support for the identification and prediction of drought propagation. 

##### **Declaration of Competing Interest** 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

##### **Data availability** 

Data will be made available on request. 

##### **Acknowledgments** 

This work was supported by the National Natural Science Foundation of China (Nos. 42001018, 52079101, and 42171415), and the Fundamental Research Funds for the Central Universities (WUT: 2021IVA111 and 2021IVB016). 

##### **Appendix A. Supplementary data** 

Supplementary data to this article can be found online at https://doi. org/10.1016/j.jhydrol.2023.130142. 

##### **References** 

- Anderegg, W.R.L., Schwalm, C., Biondi, F., Camarero, J.J., Koch, G., Litvak, M., Ogle, K., Shaw, J.D., Shevliakova, E., Williams, A.P., Wolf, A., Ziaco, E., Pacala, S., 2015. Pervasive drought legacies in forest ecosystems and their implications for carbon cycle models. Science 349 (6247), 528–532. 

- Br´eda, N., Huc, R., Granier, A., Dreyer, E., 2006. Temperate forest trees and stands under severe drought: a review of ecophysiological responses, adaptation processes and long-term consequences. Annals of Forest Science 63 (6), 625–644. 

- Breshears, D.D., Cobb, N.S., Rich, P.M., Price, K.P., Allen, C.D., Balice, R.G., Romme, W. H., Kastens, J.H., Floyd, M.L., Belnap, J., Anderson, J.J., Myers, O.B., Meyer, C.W., 2005. Regional vegetation die-off in response to global-change-type drought. Proceedings of the National academy of Sciences of the United States of America 102 (42), 15144–15148. 

- Chaves, M.M., Maroco, J.P., Pereira, J.S., 2003. Understanding plant responses to drought — from genes to the whole plant. Functional Plant Biology 30 (3), 239. 

- Chen, F., Lin, A., Zhu, H., Niu, J., 2018. Quantifying Climate Change and Ecological Responses within the Yangtze River Basin. China. Sustainability 10, 3026. 

- Chen, N., Zhang, Y., Song, C., Xu, M., Zhang, T., Li, M., Cong, N., Zu, J., Zheng, Z., Ma, G., Huang, K.e., 2022. The chained effects of earlier vegetation activities and summer droughts on ecosystem productivity on the Tibetan Plateau. Agricultural and Forest Meteorology 321, 108975. 

- Craine, J.M., Ocheltree, T.W., Nippert, J.B., Towne, E.G., Skibbe, A.M., Kembel, S.W., Fargione, J.E., 2013. Global diversity of drought tolerance and grassland climatechange resilience. Nature Climate Change 3 (1), 63–67. 

- Crausbay, S.D., Ramirez, A.R., Carter, S.L., Cross, M.S., Hall, K.R., Bathke, D.J., Betancourt, J.L., Colt, S., Cravens, A.E., Dalton, M.S., Dunham, J.B., Hay, L.E., Hayes, M.J., McEvoy, J., McNutt, C.A., Moritz, M.A., Nislow, K.H., Raheem, N., Sanford, T., 2017. Defining Ecological Drought for the Twenty-First Century. Bulletin of the American Meteorological Society 98, 2543–2550. 

- Dannenberg, M.P., Yan, D., Barnes, M.L., Smith, W.K., Johnston, M.R., Scott, R.L., Biederman, J.A., Knowles, J.F., Wang, X., Duman, T., Litvak, M.E., Kimball, J.S., Williams, A.P., Zhang, Y., 2022. Exceptional heat and atmospheric dryness amplified losses of primary production during the 2020 U.S. Southwest hot drought. Global Change Biology 28 (16), 4794–4806. 

- Fang, W., Huang, S., Huang, Q., Huang, G., Wang, H., Leng, G., Wang, L.u., Li, P., Ma, L., 2019. Bivariate probabilistic quantification of drought impacts on terrestrial vegetation dynamics in mainland China. Journal of Hydrology 577, 123980. 

- Gazol, A., Camarero, J.J., Anderegg, W.R.L., Vicente-Serrano, S.M., 2017. Impacts of droughts on the growth resilience of Northern Hemisphere forests: Forest growth resilience to drought. Global Ecology and Biogeography 26 (2), 166–176. 

- Gevaert, A.I., Veldkamp, T.I.E., Ward, P.J., 2018. The effect of climate type on timescales of drought propagation in an ensemble of global hydrological models. Hydrology and Earth System Sciences 22, 4649–4665. 

- Gouveia, C.M., Trigo, R.M., Beguería, S., Vicente-Serrano, S.M., 2017. Drought impacts on vegetation activity in the Mediterranean region: An assessment using remote sensing data and multi-scale drought indicators. Global and Planetary Change, Climate Variability and Change in the Mediterranean Region 151, 15–27. 

- Guo, Y.i., Huang, S., Huang, Q., Leng, G., Fang, W., Wang, L.u., Wang, H., 2020. Propagation thresholds of meteorological drought for triggering hydrological drought at various levels. Science of The Total Environment 712, 136502. 

- Haile, G.G., Tang, Q., Li, W., Liu, X., Zhang, X., 2020. Drought: Progress in broadening its understanding. WIREs. Water 7 (2). 

- Haslinger, K., Koffler, D., Schoner, W., Laaha, G., 2014. Exploring the link between ¨ meteorological drought and streamflow: Effects of climate-catchment interaction. Water Resources Research 50 (3), 2468–2487. 

- Huang, M., Piao, S., Ciais, P., Penuelas, J., Wang, X., Keenan, T.F., Peng, S., Berry, J.A., ˜ Wang, K., Mao, J., Alkama, R., Cescatti, A., Cuntz, M., De Deurwaerder, H., Gao, M., He, Y., Liu, Y., Luo, Y., Myneni, R.B., Niu, S., Shi, X., Yuan, W., Verbeeck, H., Wang, T., Wu, J., Janssens, I.A., 2019. Air temperature optima of vegetation productivity across global biomes. Nature Ecology & Evolution 3, 772–779. 

- Jiang, T., Su, X., Zhang, G., Zhang, T., Wu, H., 2023. Estimating propagation probability from meteorological to ecological droughts using a hybrid machine learning copula method. Hydrology and Earth System Sciences 27, 559–576. 

- Jiao, W., Wang, L., Smith, W.K., Chang, Q., Wang, H., D’Odorico, P., 2021. Observed increasing water constraint on vegetation growth over the last three decades. Nature Communications 12, 3777. 

- Jiao, W., Wang, L., Wang, H., Lanning, M., Chang, Q., Novick, K.A., 2022. Comprehensive Quantification of the Responses of Ecosystem Production and Respiration to Drought Time Scale, Intensity and Timing in Humid Environments: A FLUXNET Synthesis. Journal of Geophysical Research. Biogeosciences 127 (5). 

- Lian, X., Piao, S., Li, L.Z.X., Li, Y., Huntingford, C., Ciais, P., Cescatti, A., Janssens, I.A., Penuelas, J., Buermann, W., Chen, A., Li, X., Myneni, R.B., Wang, X., Wang, Y., ˜ Yang, Y., Zeng, Z., Zhang, Y., McVicar, T.R., 2020. Summer soil drying exacerbated by earlier spring greening of northern vegetation. Science. Advances 6, eaax0255. 

- Liu, L., Gudmundsson, L., Hauser, M., Qin, D., Li, S., Seneviratne, S.I., 2019. Revisiting assessments of ecosystem drought recovery. Environmental Research Letters 14 (11), 114028. 

- Liu, J., Liu, S., Tang, X., Ding, Z., Ma, M., Yu, P., 2022. The Response of Land Surface Temperature Changes to the Vegetation Dynamics in the Yangtze River Basin. Remote Sensing 14, 5093. 

- Luo, M., Sa, C., Meng, F., Duan, Y., Liu, T., Bao, Y., 2020. Assessing extreme climatic changes on a monthly scale and their implications for vegetation in Central Asia. Journal of Cleaner Production 271, 122396. 

- Mishra, A.K., Singh, V.P., 2010. A review of drought concepts. Journal of Hydrology 391 (1-2), 202–216. 

11 

_Journal of Hydrology 625 (2023) 130142_ 

_Y. Wang et al._ 

Myneni, R.B., Keeling, C.D., Tucker, C.J., Asrar, G., Nemani, R.R., 1997. Increased plant growth in the northern high latitudes from 1981 to 1991. Nature 386 (6626), 698–702. 

- Nemani, R.R., Keeling, C.D., Hashimoto, H., Jolly, W.M., Piper, S.C., Tucker, C.J., Myneni, R.B., Running, S.W., 2003. Climate-Driven Increases in Global Terrestrial Net Primary Production from 1982 to 1999. Science 300 (5625), 1560–1563. 

- Niu, S., Luo, Y., Fei, S., Yuan, W., Schimel, D., Law, B.E., Ammann, C., Altaf Arain, M., Arneth, A., Aubinet, M., Barr, A., Beringer, J., Bernhofer, C., Andrew Black, T., Buchmann, N., Cescatti, A., Chen, J., Davis, K.J., Dellwik, E., Desai, A.R., Etzold, S., Francois, L., Gianelle, D., Gielen, B., Goldstein, A., Groenendijk, M., Gu, L., Hanan, N., Helfter, C., Hirano, T., Hollinger, D.Y., Jones, M.B., Kiely, G., Kolb, T.E., Kutsch, W.L., Lafleur, P., Lawrence, D.M., Li, L., Lindroth, A., Litvak, M., Loustau, D., Lund, M., Marek, M., Martin, T.A., Matteucci, G., Migliavacca, M., Montagnani, L., Moors, E., William Munger, J., Noormets, A., Oechel, W., Olejnik, J., U, K.T.P., Pilegaard, K., Rambal, S., Raschi, A., Scott, R.L., Seufert, G., Spano, D., Stoy, P., Sutton, M.A., Varlagin, A., Vesala, T., Weng, E., Wohlfahrt, G., Yang, B., Zhang, Z., Zhou, X., 2012. Thermal optimality of net ecosystem exchange of carbon dioxide and underlying mechanisms. New Phytologist 194 (3), 775–783. 

- Pasho, E., Camarero, J.J., de Luis, M., Vicente-Serrano, S.M., 2011. Impacts of drought at different time scales on forest growth across a wide climatic gradient in northeastern Spain. Agricultural and Forest Meteorology 151 (12), 1800–1811. 

- Pena-Gallardo, M., Vicente-Serrano, S.M., Quiring, S., Svoboda, M., Hannaford, J., ˜ Tomas-Burguera, M., Martín-Hern´andez, N., Domínguez-Castro, F., El Kenawy, A., 2019. Response of crop yield to different time-scales of drought in the United States: Spatio-temporal patterns and climatic and environmental drivers. Agricultural and Forest Meteorology 264, 40–55. 

- Peters, E., Torfs, P.J.J.F., van Lanen, H., a. J., Bier, G.,, 2003. Propagation of drought through groundwater—a new approach using linear reservoir theory. Hydrological Processes 17, 3023–3040. 

- Piao, S., Zhang, X., Chen, A., Liu, Q., Lian, X.u., Wang, X., Peng, S., Wu, X., 2019. The impacts of climate extremes on the terrestrial carbon cycle: A review. Science China Earth Sciences 62 (10), 1551–1563. 

- Poulter, B., Frank, D., Ciais, P., Myneni, R.B., Andela, N., Bi, J., Broquet, G., Canadell, J. G., Chevallier, F., Liu, Y.Y., Running, S.W., Sitch, S., van der Werf, G.R., 2014. Contribution of semi-arid ecosystems to interannual variability of the global carbon cycle. Nature 509 (7502), 600–603. 

- Reichstein, M., Bahn, M., Ciais, P., Frank, D., Mahecha, M.D., Seneviratne, S.I., Zscheischler, J., Beer, C., Buchmann, N., Frank, D.C., Papale, D., Rammig, A., Smith, P., Thonicke, K., van der Velde, M., Vicca, S., Walz, A., Wattenbach, M., 2013. Climate extremes and the carbon cycle. Nature 500 (7462), 287–295. 

- Sadiqi, S.S.J., Hong, E.-M., Nam, W.-H., Kim, T., 2022. Review: An integrated framework for understanding ecological drought and drought resistance. Science of The Total Environment 846, 157477. 

- Sala, O.E., Lauenroth, W.K., Parton, W.J., 1992. Long-Term Soil Water Dynamics in the Shortgrass Steppe. Ecology 73, 1175–1181. 

- Schwalm, C.R., Anderegg, W.R.L., Michalak, A.M., Fisher, J.B., Biondi, F., Koch, G., Litvak, M., Ogle, K., Shaw, J.D., Wolf, A., Huntzinger, D.N., Schaefer, K., Cook, R., Wei, Y., Fang, Y., Hayes, D., Huang, M., Jain, A., Tian, H., 2017. Global patterns of drought recovery. Nature 548 (7666), 202–205. 

- Seneviratne, S.I., X. Zhang, M. Adnan, W. Badi, C. Dereczynski, A. Di Luca, S. Ghosh, I. Iskandar, J. Kossin, S. Lewis, F. Otto, I. Pinto, M. Satoh, S.M. Vicente-Serrano, M. Wehner, and B. Zhou, 2021: Weather and Climate Extreme Events in a Changing Climate. In Climate Change 2021: The Physical Science Basis. Contribution of Working Group I to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change [Masson-Delmotte, V., P. Zhai, A. Pirani, S.L. Connors, C. P´ean, S. Berger, N. Caud, Y. Chen, L. Goldfarb, M.I. Gomis, M. Huang, K. Leitzell, E. Lonnoy, J.B.R. Matthews, T.K. Maycock, T. Waterfield, O. Yelekçi, R. Yu, and B. Zhou (eds.)]. Cambridge University Press, Cambridge, United Kingdom and New York, NY, USA, pp. 1513–1766. 

- Sheffield, J., Wood, E.F., 2008. Projected changes in drought occurrence under future global warming from multi-model, multi-scenario, IPCC AR4 simulations. Climate Dynamics 31 (1), 79–105. 

- Sun, S., Du, W., Song, Z., Zhang, D., Wu, X., Chen, B., Wu, Y., 2021. Response of Gross Primary Productivity to Drought Time-Scales Across China. Journal of Geophysical Research. Biogeosciences 126 (4). 

- Tu, X., Du, Y., Singh, V.P., Chen, X., Zhao, Y., Ma, M., Li, K., Wu, H., 2019. Bivariate Design of Hydrological Droughts and Their Alterations under a Changing Environment. Journal of Hydrologic Engineering 24, 04019015. 

- Van Loon, A.F., Van Huijgevoort, M.H.J., Van Lanen, H., a. J.,, 2012. Evaluation of drought propagation in an ensemble mean of large-scale hydrological models. Hydrology and Earth System Sciences 16, 4057–4078. 

- Vicente-Serrano, S.M., Beguería, S., Lopez-Moreno, J.I., 2010. A Multiscalar Drought ´ Index Sensitive to Global Warming: The Standardized Precipitation Evapotranspiration Index. Journal of Climate 23, 1696–1718. 

- Vicente-Serrano, S.M., Gouveia, C., Camarero, J.J., Beguería, S., Trigo, R., Lopez- ´ Moreno, J.I., Azorín-Molina, C., Pasho, E., Lorenzo-Lacruz, J., Revuelto, J., Moran- ´ Tejeda, E., Sanchez-Lorenzo, A., 2013. Response of vegetation to drought time-scales 

across global land biomes. Proceedings of the National Academy of Sciences 110 (1), 52–57. 

- Vicente-Serrano, S.M., Quiring, S.M., Pena-Gallardo, M., Yuan, S., Domínguez-Castro, F., ˜ 2020. A review of environmental droughts: Increased risk under global warming? Earth-Science Reviews 201, 102953. 

- Wang, Y., Fu, Z., Hu, Z., Niu, S., 2022. Tracking Global Patterns of Drought-Induced Productivity Loss Along Severity Gradient. Journal of Geophysical Research. Biogeosciences 127 (6). 

- Wang, H., Huang, J., Zhou, H., Deng, C., Fang, C., 2020a. Analysis of sustainable utilization of water resources based on the improved water resources ecological footprint model: A case study of Hubei Province. China. Journal of Environmental Management 262, 110331. 

- Wang, M., Wang, S., Zhao, J., Ju, W., Hao, Z., 2021. Global positive gross primary productivity extremes and climate contributions during 1982–2016. Science of The Total Environment 774, 145703. 

- Wang, S., Zhang, Y., Ju, W., Porcar-Castell, A., Ye, S., Zhang, Z., Brümmer, C., Urbaniak, M., Mammarella, I., Juszczak, R., Folkert Boersma, K., 2020b. Warmer spring alleviated the impacts of 2018 European summer heatwave and drought on vegetation photosynthesis. Agricultural and Forest Meteorology 295, 108195. 

- Wei, X., He, W., Zhou, Y., Ju, W., Xiao, J., Li, X., Liu, Y., Xu, S., Bi, W., Zhang, X., Cheng, N., 2022b. Global assessment of lagged and cumulative effects of drought on grassland gross primary production. Ecological Indicators 136, 108646. 

- Wei, J., Li, X., Liu, L., Christensen, T.R., Jiang, Z., Ma, Y., Wu, X., Yao, H., Lopez- ´ Blanco, E., 2022a. Radiation, soil water content, and temperature effects on carbon cycling in an alpine swamp meadow of the northeastern Qinghai-Tibetan Plateau. Biogeosciences 19, 861–875. 

- Weng, Z., Niu, J., Guan, H., Kang, S., 2023. Three-dimensional linkage between meteorological drought and vegetation drought across China. Science of The Total Environment 859, 160300. 

- Wilhite, D.A., Glantz, M.H., 1985. Understanding: the Drought Phenomenon: The Role of Definitions. Water International 10 (3), 111–120. 

- Wu, X., Liu, H., Li, X., Ciais, P., Babst, F., Guo, W., Zhang, C., Magliulo, V., Pavelka, M., Liu, S., Huang, Y., Wang, P., Shi, C., Ma, Y., 2018b. Differentiating drought legacy effects on vegetation growth over the temperate Northern Hemisphere. Global Change Biology 24 (1), 504–516. 

- Wu, J., Miao, C., Zheng, H., Duan, Q., Lei, X., Li, H.u., 2018a. Meteorological and Hydrological Drought on the Loess Plateau, China: Evolutionary Characteristics, Impact, and Propagation. Journal of Geophysical Research: Atmospheres 123 (20), 11,569–11,584. 

- Xu, X., Jiang, H., Guan, M., Wang, L., Huang, Y., Jiang, Y., Wang, A., 2020. Vegetation responses to extreme climatic indices in coastal China from 1986 to 2015. Science of The Total Environment 744, 140784. 

- Xu, M., Zhang, T., Zhang, Y., Chen, N., Zhu, J., He, Y., Zhao, T., Yu, G., 2021. Drought limits alpine meadow productivity in northern Tibet. Agricultural and Forest Meteorology 303, 108371. 

- Yang, D., Xu, X., Xiao, F., Xu, C., Luo, W., Tao, L., 2021. Improving modeling of ecosystem gross primary productivity through re-optimizing temperature restrictions on photosynthesis. Science of The Total Environment 788, 147805. 

- Yevjevich, V.M., 1966. Objective approach to definitions and investigations of continental hydrologic droughts. 

- Yu, Z., Wang, J., Liu, S., Rentch, J.S., Sun, P., Lu, C., 2017. Global gross primary productivity and water use efficiency changes under drought stress. Environmental Research Letters 12 (1), 014016. 

- Yuan, W., Zheng, Y., Piao, S., Ciais, P., Lombardozzi, D., Wang, Y., Ryu, Y., Chen, G., Dong, W., Hu, Z., Jain, A.K., Jiang, C., Kato, E., Li, S., Lienert, S., Liu, S., Nabel, J.E. M.S., Qin, Z., Quine, T., Sitch, S., Smith, W.K., Wang, F., Wu, C., Xiao, Z., Yang, S., 2019. Increased atmospheric vapor pressure deficit reduces global vegetation growth. Science. Advances 5, eaax1396. 

- Zelenhasi´c, E., Salvai, A., 1987. A method of streamflow drought analysis. Water Resources Research 23 (1), 156–168. 

- Zhang, T., Ji, X., Xu, M., Zhao, G., Zheng, Z., Tang, Y., Chen, N., Zhu, J., He, Y., Zhang, Y., 2022a. Influences of drought on the stability of an alpine meadow ecosystem. Ecosystem Health and Sustainability 8, 2110523. 

- Zhang, Z., Ju, W., Zhou, Y., Li, X., 2022b. Revisiting the cumulative effects of drought on global gross primary productivity based on new long-term series data (1982–2018). Global Change Biology 28 (11), 3620–3635. 

- Zhang, Q., Kong, D., Singh, V.P., Shi, P., 2017. Response of vegetation to different timescales drought across China: Spatiotemporal patterns, causes and implications. Global and Planetary Change 152, 1–11. 

- Zhang, S., Yang, Y., Wu, X., Li, X., Shi, F., 2021. Postdrought Recovery Time Across Global Terrestrial Ecosystems. Journal of Geophysical Research. Biogeosciences 126. 

- Zheng, Y., Shen, R., Wang, Y., Li, X., Liu, S., Liang, S., Chen, J.M., Ju, W., Zhang, L., Yuan, W., 2020. Improved estimate of global gross primary production for reproducing its long-term variation, 1982–2017. Earth System Science Data 12, 2725–2746. 

- Zhu, X., Zhang, S., Liu, T., Liu, Y., 2021. Impacts of Heat and Drought on Gross Primary Productivity in China. Remote Sensing 13, 378. 

12 

