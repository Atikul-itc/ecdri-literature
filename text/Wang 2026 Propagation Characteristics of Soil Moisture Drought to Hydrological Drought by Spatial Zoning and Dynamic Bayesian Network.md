IEEE JOURNAL OF SELECTED TOPICS IN APPLIED EARTH OBSERVATIONS AND REMOTE SENSING, VOL. 19, 2026 

29241 

# Propagation Characteristics of Soil Moisture Drought to Hydrological Drought by Spatial Zoning and Dynamic Bayesian Network 

Jie Wang , Nan Xia , Hai Yang, Jiale Liang , Ziyu Wang , Zhenkang Wang , Gengbin Cai, and Manchun Li 

**_Abstract_ —Understanding how soil moisture drought transitions into hydrological drought is essential for effective monitoring of water resources and assessing drought risk. Traditional methods for constructing drought indices often overlook regional heterogeneity and fail to adequately capture the dynamic dependencies among drought variables. Thus, this article proposes an integrated framework to characterize the propagation characteristics from soil moisture drought to hydrological drought. The k-means algorithm was first used to conduct the rough spatial zoning considering precipitation and evapotranspiration, and the standardized soil moisture index (SSMI) and standardized runoff index (SRI) were constructed. The sliding window-based Spearman’s correlation analysis on these two drought indices was subsequently applied to estimate the drought propagation time. Finally, dynamic Bayesian network (DBN) and Copula joint distribution functions were combined to model their dynamic relationships and infer the drought propagation probability. Results indicate that, during 1982–2023, drought propagation from soil moisture to hydrological droughts in the Yangtze River Basin is highly nonlinear and demonstrates substantial regional heterogeneity. The average drought propagation time is 7.39 months, with pronounced lag effects evident at higher elevations. Drought propagation probability also revealed spatial distribution differences and distinct hierarchical response patterns, with averaging 19.13% in the high-elevation upper reaches compared to 10.95% in the middle-lower reaches, and 16.52% under extreme soil moisture droughts compared to 12.33% under light droughts. Comparative evaluations demonstrated that spatial zoning based SSMI and SRI can more accurately reflect regional drought dynamics, and DBN can also enhance the sensitivity to the spatiotemporal changes of drought variables compared to conventional Bayesian network. The proposed probabilistic reasoning** 

Received 21 October 2025; revised 26 June 2026; accepted 10 August 2026. Date of publication 12 August 2026; date of current version 14 September 2026. This work was supported in part by the National Natural Science Foundation of China under Grant 42471455 and Grant 42230113, in part by the Research and Development Program of China under Grant 2022YFC3800804-01, and in part by the Postgraduate Research & Practice Innovation Program of Jiangsu Province under Grant 26CXJH0249. _(Corresponding author: Nan Xia.)_ 

Jie Wang, Hai Yang, Jiale Liang, Ziyu Wang, Zhenkang Wang, and Gengbin Cai are with the Jiangsu Provincial Key Laboratory for Advanced Remote Sensing and Geographic Information Technology, Nanjing University, Nanjing 210023, China, and also with the School of Geography and Ocean Science, Nanjing University, Nanjing 210023, China (e-mail: 502024270100@smail.nju.edu.cn; 502024270112@smail.nju.edu.cn; ljl0715@smail.nju.edu.cn; 502022270086@smail.nju.edu.cn; wangzhenkang @smail.nju.edu.cn; 502025270071@smail.nju.edu.cn). 

Nan Xia and Manchun Li are with the Key Laboratory for Land Satellite Remote Sensing Applications of Ministry of Natural Resources, Nanjing University, Nanjing 210023, China, and also with the Collaborative Innovation Center for the South Sea Studies, Nanjing University, Nanjing 210093, China (e-mail: xianan@nju.edu.cn; limanchun@nju.edu.cn). 

Digital Object Identifier 10.1109/JSTARS.2026.3723409 

**framework can help to strengthen the foundation for decisionmaking in agricultural production and ecological conservation.** 

**_Index Terms_ —Dynamic Bayesian network (DBN), hydrological drought, propagation characteristics, soil moisture drought, spatiotemporal modeling.** 

## I. INTRODUCTION 

ROUGHTS are prolonged natural disasters that can cause **D** severe damage by inducing abnormal and extended water shortages in affected regions [1], [2]. The World Meteorological Organization classifies droughts into four main types: meteorological, agricultural, hydrological, and socioeconomic droughts [3], [4]. These categories are inherently interconnected, with droughts typically originating as meteorological droughts driven by the imbalance between precipitation and evapotranspiration, which can propagate through the surface water cycle, resulting in soil moisture shortages and, subsequently, agricultural droughts [5], [6]. Reduced surface and subsurface runoff from these processes leads to hydrological droughts, impacting water resources, crop yields, and other critical sectors [5], [7]. 

**D** 

Research on drought propagation has elucidated the linkage and transition mechanisms among different types of droughts or regional drought events and analyzed their spatiotemporal evolution characteristics [8], [9]. Drought propagation is influenced by myriad factors, including meteorological, hydrological, ecological and environmental variables, human activities, and geographic conditions. Such research is essential for a comprehensive understanding of drought propagation mechanisms, enhancing drought risk assessment, and improving emergency mitigation strategies [10], [11]. 

Previous articles on drought propagation have primarily focused on the processes by which meteorological droughts evolve into agricultural and hydrological droughts, with a particular emphasis on the influence of precipitation variability and regional differences [12]. However, systematic research on the mutual transformation and expansion characteristics between agricultural and hydrological drought remains limited, which is a critical link in drought propagation [13], [14]. As a key indicator of agricultural drought, soil moisture drought refers to insufficient soil moisture due to abnormal meteorological conditions, which can rapidly impact vegetation growth and agricultural productivity [15], [16]. Persistent soil moisture drought without adequate precipitation can decrease groundwater levels, 

© 2026 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/ 

IEEE JOURNAL OF SELECTED TOPICS IN APPLIED EARTH OBSERVATIONS AND REMOTE SENSING, VOL. 19, 2026 

29242 

affect river and lake levels, and ultimately trigger hydrological drought, which may also lead to socioeconomic drought [17], [18]. The increasing frequency of extreme climate events and altered precipitation patterns, driven by climate change, have further complicated the relationships among different drought types, causing these drought evolution patterns to become more unpredictable and regionally variable [19], [20]. Thus, uncovering the propagation characteristics between soil moisture drought and hydrological drought is essential to the in-depth understanding of their evolution patterns and mechanisms, which is also critical for agricultural production and ecological conservation [4], [21]. 

The drought index is a common quantitative tool for measuring drought severity and quantitatively assessing drought intensity, duration, and spatial distribution [22], [23]. Drought indices are typically constructed from long-term remote sensing observations, such as precipitation flux, soil moisture, surface or subsurface runoff, and plant moisture [24], [25]. For better comparison, standardized forms of those indexes are further derived from probability distributions of time-series data, and positive/negative values denote wet/dry conditions, respectively, where smaller values represent more severe levels of drought [26]. Additionally, vegetation indices like the normalized difference vegetation index and vegetation health index, which reflect vegetation growth, can also indirectly represent regional drought status [27], [28]. 

Advancements in satellite remote sensing have enabled the creation of more accurate drought indices, improving the capability of monitoring, analyzing, and forecasting drought patterns [29], [30]. Amongst all, the famine early warning systems network land data assimilation system (FLDAS) dataset is most widely used due to its high data quality and accessibility, such as the standardized precipitation index (SPI), standardized runoff index (SRI), and standardized soil moisture index (SSMI) [31], [32]. However, most of these indices are calculated using the overall distribution of data within a region. Given that the natural environment within large river basins often exhibits significant spatial heterogeneity, fitting directly based on the overall data of theentirebasincanleadtosystematicerrorsincalculationsofthe local drought characteristics and their evolution patterns [33], [34], [35]. To mitigate these biases, rough spatial zoning can be applied to improve the regional consistency by incorporating neighboring grids, where the k-means algorithm is classic and efficient due to its advantages of simplicity, maturity, and rapid convergence [36], [37], [38]. 

Drought propagation time—a fundamental characteristic of drought propagation—refers to the time lag effect that occurs as drought signals expand across regions, which also serves as a key indicator for measuring drought expansion speed [39], [40]. By the processing the drought index time series of target drought types (e.g., using sequence shifting or sliding windows), this time lag is determined by identifying the timescale with the strongest correlation with source drought type [6], [21]. Spearman’s correlation coefficient is frequently applied to reveal the drought propagation time due to its robustness and applicability [41], [42], for example, using the SPI and SSMI time series to quantify the lag between agricultural and meteorological droughts [12]. 

However, due to the uncertainties inherent in drought propagation across systems and regions, time lag features alone cannot fully capture its dynamic processes [43], [44]. Propagation probability—the likelihood that one type of drought will follow another with a certain lag—is also essential to understand the intensity, pathway, and risk of drought propagation [7]. Given that drought propagation involves complex nonlinear dependencies among multiple factors, traditional linear correlation methods often fail to capture their internal relationships [35]. The Copula joint distribution functions, a flexible statistical modeling approach, can quantify conditional probabilities between variables and effectively capture dependence structures [4], [35]. Accordingly, it has been widely used to model and analyze the propagation probabilities among different drought types, offeringtheoreticalandtechnicalinsights [4], [45].Despitethese advantages, Copula functions are limited in handling missing data and dynamic interference, prompting the integration of machine learning methods, such as Bayesian network (BN), to improve feature recognition in drought propagation [12], [46]. 

BN employs directed acyclic graphs (DAGs) to describe conditional dependencies among random variables, effectively modeling static correlations and performing inference through conditional probability tables (CPTs) [47], [48]. However, BN typically assume static relationships and focus solely on drought indices, often neglecting key environmental drivers of drought propagation [49], [50]. Unlike standard BN, dynamic Bayesian network (DBN) extends the modeling framework by incorporating time dimension, enabling the modeling of evolutionary features among variables [51], [52]. DBNs are structured into timeslicesandtemporaledges,witheachslicecontainingastatic BN. This design supports dynamic inference and evolutionary modeling of complex temporal data, revealing how variables evolve during drought propagation [52], [53], [54]. Accordingly, in drought propagation studies, DBN can effectively model the complex dependencies among multiple variables, and precisely capturethedifferencesinpropagationpatternsatvariousdrought stages [55], [56]. DBN also enables the prediction of future drought probabilities to support various decision-making applications, including hydrological prediction, ecosystem assessment, and disaster risk management [57], [58]. Despite these significant potentials, the complexity of structure learning, high computational demands, and challenges in integrating long-term datasets have also limited the application of DBN in current drought propagation studies [59]. 

In general, existing studies on the characteristics of soil moisturedroughtpropagationtohydrologicaldroughtarepoorly understood. Additionally, calculations of drought indices often overlook regional heterogeneity, and propagation analyses do not fully account for the dynamic dependencies between these drought types, thereby compromising computational precision. Thus, taking the Yangtze River Basin as the study area, which has complex topography and significant spatial variability in soil moisture and surface runoff [60], this article proposes a framework for drought process modeling and characteristic computation and aims to: 1) conduct rough spatial zoning to generate subregions according to differences in precipitation and evapotranspiration using the k-means algorithm; 2) characterize soil moisture drought and hydrological drought in each 

WANG et al.: PROPAGATION CHARACTERISTICS OF SOIL MOISTURE DROUGHT TO HYDROLOGICAL DROUGHT 

29243 



Fig. 1. Location of the Yangtze River Basin. 

subregion using long-term FLDAS SSMI and SRI datasets, and apply correlation analysis to calculate the grid-level drought propagation time; and 3) incorporate multiple drought variables of precipitation, soil moisture, evapotranspiration and runoff to create a drought propagation network, and combine Copula functions and DBN inference model to quantify gridlevel drought propagation probability. We believe the proposed framework can enhance the accuracy of drought monitoring and propagation prediction. 

## II. STUDY AREA AND MATERIALS 

## _A. Study Area_ 

The Yangtze River originates on the Qinghai–Tibet Plateau, and traverses 11 provinces before emptying into the East China Sea, including Qinghai, Tibet, Sichuan, Yunnan, Chongqing, Hubei, Hunan, Jiangxi, Anhui, Jiangsu, and Shanghai. As China’s longest river, its basin spans approximately 1.8 million km<sup>2</sup> , accounting for nearly one-fifth of China’s total land area (Fig. 1). 

The Yangtze River Basin is a vast region comprising diverse geographical units, including plateaus, plains, and basins. With a dense population and advanced economic development, it supports approximately one-third of China’s total population and contributes over 40% of the nation’s GDP. This establishes its pivotal role in China’s socioeconomic development, national strategic framework, and sustainable advancement. Furthermore, the basin serves as a critical ecological security shield for the nation, with abundant water, biological, and land resources [19], [61]. Complex topographic and hydroclimatic features result in significant spatial differences in soil moisture and surface runoff within the basin. The upstream western region is dominated by alpine canyon landforms, with precipitation primarily influenced by the Southwest monsoon. Meanwhile, 

the mid- to downstream eastern areas are governed by the East Asian monsoon, resulting in uneven precipitation distribution with marked seasonality [60], [62]. 

## _B. Materials_ 

The FLDAS dataset was developed by the National Aeronautics and Space Administration for hydrometeorological monitoring and drought assessment [63]. Optimized specifically for global drought and water security monitoring [64], FLDAS flexibly integrates multiple land surface models (Noah LSM) andmultisourcemeteorologicalforcinginputs, includingremote sensing and ERA5 reanalysis data. This comprehensive integration can effectively reduce simulation uncertainties and ensures excellent performance even in data-sparse regions. Furthermore, by providing long-term continuous historical records and quantitative outputs with clear physical meanings, FLDAS is widely recognized as a highly authoritative and reliable dataset for accurately characterizing complex drought dynamics and supporting large-scale hydrological studies [65]. Considering that drought propagation is a relatively slow evolutionary process, monthly scale data are sufficient to capture its long-term dynamic trends [66].Therefore,aligningwithourresearchobjectives,thisarticle utilized monthly FLDAS data spanning 1982–2023, comprising 504 temporal records at a spatial resolution of 0.1° _×_ 0.1° (about 10 km), which yielded approximately 16 671 grids across the Yangtze River Basin. In the FLDAS dataset, the soil moisture variable described the water storage status and wetness or dryness of soil and is reported in m³/m³, whereas the surface runoff is reported in kg/m2/s. These monthly FLDAS variables were used as the basis for constructing SSMI and SRI. Additionally, precipitation (PRE) and evapotranspiration (ET) functioned as auxiliary variables for understanding the process from soil drought to hydrological drought. Their monthly data present 

IEEE JOURNAL OF SELECTED TOPICS IN APPLIED EARTH OBSERVATIONS AND REMOTE SENSING, VOL. 19, 2026 

29244 



Fig. 2. Technology roadmap. 

the daily average values within a month, and are measured in millimeters per day (mm/day). 

Since FLDAS is an assimilation dataset generated based on multisource observations and land surface models, it may contain a very small number of outliers due to local computational fluctuations. Therefore, this article conducted anomalous data cleaning on the FLDAS dataset using the moving window-based spatial consistency check method [67]. For each time step, a 3 _×_ 3 local spatial window was constructed centered on each grid. If the deviation of the center grid value from the mean of its neighboring grids exceeded three times the local standard deviation, it was identified as an isolated outlier. For these very fewabnormalvalues,spatialsmoothingwasappliedbyreplacing them with the spatial mean of their surrounding valid pixels. This process could effectively remove outliers, ensuring the spatial coherence of the data and the accuracy of the subsequent drought index calculations. 

## III. METHODS 

The research framework is mainly divided into three parts (Fig. 2). First, the k-means algorithm was used to conduct the spatial zoning in the Yangtze River Basin, and SSMI and SRI were constructed within different subregions to characterize soil moisture drought and hydrological drought. Then, the slidingwindow-based Spearman’s correlation coefficient was used to calculate the grid-level propagation time from soil moisture 

drought to hydrological drought. Finally, a drought propagation network covering precipitation, soil moisture, evapotranspiration, and runoff was constructed, with dependencies between network nodes modeling by the Copula joint distribution functions, and the grid-level propagation probability was obtained using DBN inference model. 

## _A. Drought Index Based on Spatial Zoning_ 

_1) Spatial Zoning by K-Means Algorithm:_ Significant spatial heterogeneity exists in the degree of drought within the Yangtze River Basin [34]. Thus, the direct use of basin-wide data to calculate the drought indices may inadequately reflect local drought characteristics. Therefore, the k-means algorithm was employed for rough spatial zoning of the study area to optimize the calculation of the drought indices. As an unsupervised clustering algorithm, k-means partitions datasets into distinct clusters by calculating the distance between each data point and the center of each cluster, subsequently assigning the data point to its nearest cluster [37]. In this article, the k-means spatial zoning was achieved based on the PRE and ET time-series data from FLDAS, which reflect changes in precipitation and the process of water evaporation and consumption, respectively. These two variables effectively capture the supply–demand dynamics of water resources and are intrinsically linked to drought propagation. This article employed the Elbow method to determine the optimal number of clusters, K, in the K-means algorithm [38]. 

29245 

WANG et al.: PROPAGATION CHARACTERISTICS OF SOIL MOISTURE DROUGHT TO HYDROLOGICAL DROUGHT 

By plotting the sum of squared errors (SSE) against different K values, we evaluated the compactness of the clustering results. While SSE naturally decreases as K increases, the marginal reduction in SSE diminishes significantly once K reaches its optimal value, creating a distinct inflection point (the “elbow”) on the curve. This elbow represents the optimal balance between classification accuracy and model complexity, allowing us to establish the ideal number of spatial partitions while avoiding overfitting. 

_2) CalculationofDroughtIndices:SSMIandSRI:_ TheSSMI and SRI were selected as quantitative indicators of soil moisture drought and hydrological drought, respectively. These indices characterize the long-term temporal anomalies in soil moisture and surface runoff across different subregions [68], [69]. The SSMI and SRI were calculated as follows: 1) monthly soil moisture and runoff data ( _X,_ 504 months) were collected for all grids in each subregion based on spatial zoning results; 2) due to their right-skewed, non-negative distributions [70], [71], the Python Fitter library was used to fit normal, exponential, and Gamma models, selecting the best probability distribution via goodness of fit tests; 3) once the optimal distribution was chosen, the probability density function (PDF) for each grid was determined using (1), and the cumulative distribution function (CDF) using (2); and 4) the inverse CDF of the standard normal distribution was then applied to convert the CDF of each grid to the standardized drought index using (3) (i.e., the SSMI and SRI of the grids). The aforementioned standardized procedures in each subregion could eliminate the bias in original soil moisture data and runoff data, enabling comparable assessments across diverse temporal and spatial scales 







where _X_ represents the monthly time-series data of soil moisture or runoff for all grids within defined subregion, _Xk_ is the soil moisture or runoff value at the _k_ th moment, _θ_ is the parameter of the optimal probability distribution, BestFitPDF is the optimally fitted probability distribution, _f(Xk;θ)_ and _F(Xk;θ)_ represent the PDF and CDF of the optimal probability distribution, respectively, Φ<sup>_−_1</sup> is the inverse CDF, and _Zk_ is the SSMI and SRI obeying the standard normal distribution. 

The SSMI and SRI are used to assess moisture conditions: positive values typically correspond to wetter conditions, while negative values denote drought [26]. According to China’s drought classification standards [72], the SSMI and SRI are classified into five levels corresponding to different drought states: extreme, severe, moderate, light, and no drought (Table I). 

## _B. Drought Propagation Time Based on Spearman’s Correlation_ 

Spearman’s correlation analysis was used to determine the propagation time from soil moisture drought to hydrological drought for its capability of capturing the correlations between 

TABLE I 

SSMI AND SRI LEVELS AND CORRESPONDING VALUES 



different variables effectively [73], [74]. First, using the 0.1° grid as the basic study unit, the corresponding raw monthly FLDAS soil moisture data were extracted for each grid. The cumulative calculation based on the sliding window was applied over _p_ consecutive months, resulting in cumulative soil moisture data at a _p_ -month timescale. The SSMI- _p_ sequences corresponding to the _p_ -month timescale were derived based on spatial zoning results and standardized methods in section III-A-2. Similarly, the SRI-1 sequences were computed for timescale _p_ = 1 (without cumulative calculation). 

Given the inherent time-lag effect in drought propagation, the original index sequences of SSMI and SRI typically exhibitphaseasynchrony,resultinginnonmonotonicrelationships. However, as the sliding window size _p_ applied to the SSMI converges upon the actual propagation duration, the evolutionary phases of the resulting SSMI-p and SRI-1 sequences progressively synchronize. At this critical threshold, the two variables exhibit their strongest monotonic dependence across the time series, thereby yielding the peak Spearman’s correlation coefficient. Guided by this theoretical premise, the Spearman’s correlation coefficients between the SSMI-p sequences across all evaluated timescales ( _p_ = 1–12 months) and the SRI-1 sequences were computed for each grid. Ultimately, the timescale _p_ yielding the maximum correlation coefficient was identified and designated as the transition lag time from SSMI to SRI, representing the propagation time from soil moisture drought to hydrological drought. 

## _C. Drought Propagation Probability Based on DBN_ 

_1) DBN Network Structure determination:_ DBN model is an extension of static BN in the temporal dimension to characterize the dependencies of variables as they evolve over time [51]. Unlike traditional BN that only capture conditional independencies between variables at a single moment, DBN divide the system into a series of “time slices.” Each slice retains identical DAG structures to the static network, while adjacent slices are interconnected via “temporal edges” to capture evolutionary dependencies between variables at different moments [53]. 

The network structure serves as the foundation for constructing the DBN. Each time slice contains different internal nodes. The SSMI and SRI are key variables in the drought propagation process, acting as core nodes within the DBN. Additionally, PRE and ET are incorporated as auxiliary variables due to their significant roles in the mechanisms of drought development, 

29246 

IEEE JOURNAL OF SELECTED TOPICS IN APPLIED EARTH OBSERVATIONS AND REMOTE SENSING, VOL. 19, 2026 



Fig. 3. Two-slice dynamic Bayesian network structure for drought-related variables. 

which enable more comprehensive representation of the relationships between drought propagation and the key environmental drivers [75], [76]. In this article, all drought variables were collected monthly and chronologically divided into 504 time slices, spanning the years 1982–2023. Each time slice, denoted as _t_ , contained four nodes: PRE _t_ , SSMI _t_ , ET _t_ , SRI _t_ . Immediate dependencies among these nodes were sequentially connected through the DAG as PRE _→_ SSMI _→_ ET _→_ SRI. Meanwhile, temporal edges connected two nodes across adjacent time slices, capturing the evolutionary dependencies and reflecting the propagation process of drought variables over time (Fig. 3). Since the formation of the SSMI and SRI relies on the k-means spatial zoning results, the same network structure was used to construct different DBN in various zones. 

_2) DBN Parameter Learning via Copula Joint Distribution functions:_ Parameter learning is a key step in DBN model construction, transforming qualitative dependencies in the network structure into quantitative descriptions, where the CPT forms the core parameter. Traditional parameter learning methods often face challenges with continuous variables, especially when complex nonlinear or tail dependencies exist among variables in the drought propagation process [77]. To address these issues, this article uses the Copula function to establish the joint distribution between drought variables related to drought propagation. By integrating Copula with preset threshold intervals, the conditional probabilities between variables were computed and applied to construct CPTs between DBN nodes. 

The Copula function is a mathematical tool for creating multivariate joint distributions, based on Sklar’s theorem [78]. For any two random variables ( _X, Y_ ) with cumulative probability distribution functions ( _FX(X)_ and _FY(Y)_ ), their joint distribution can be expressed as a Copula function – _C(FX(X), FY(Y)),_ which describes the dependency between the variables. Various types of Copula functions—such as Gaussian, _t_ -Copula, Gumbel, and Clayton—can be selected based on the dependency characteristics observed. The most suitable Copula for each set of drought variables can be selected by comparing maximum likelihood estimations and considering model selection criteria 

like the Akaike Information Criterion and Bayesian Information Criterion. 

In adjacent time slices of the DBN, dependencies between nodes were modeled using the Copula function through the following steps. 

- 1) The node pairs ( _X, Y_ ) requiring Copula construction were identified based on the immediate dependencies and evolutionarydependenciesbetweenthenodeswithintheDBN structure (Fig. 3). The optimal Copula was selected using the CDFs ( _FX(X)_ and _FY(Y)_ ) of the variables ( _X_ and _Y_ ) for joint distribution modeling. 

- 2) The different states of variables _X_ and _Y_ were defined through multiple threshold intervals. For the SSMI and SRI, five intervals were defined based on five drought states (Table I). For PRE and ET, three intervals were established using quantile transformation. 

- 3) For the threshold intervals ([ _x1, x2_ ] and [ _y1, y2_ ]) of variables ( _X, Y_ ), their endpoints were mapped to the [0,1] probability space using the CDFs ( _FX(X)_ and _FY(Y)_ ), respectively: [ _FX(x1), FX(x2)_ ], [ _FY(y1), FY(y2)_ ]), denoted as [ _u1, u2_ ], [ _v1, v2_ ]. 

- 4) The Copula function was used to calculate the joint distribution function values at the endpoints of the mapped threshold intervals, taking the values of _C_ ( _u1,v1_ ), _C_ ( _u1,v2_ ), _C_ ( _u2,v1_ ), and _C_ ( _u2,v2_ ). Subsequently, the conditional probability _P_ ( _Y_ ࢠ [ _y1,y2_ ] | _X_ ࢠ [ _x1,x2_ ]) was calculated using the formula 



where _P(Y_ ࢠ [ _y1,y2_ ] | _X_ ࢠ [ _x1,x2_ ]) denotes the conditional probability that _Y_ falls in the interval [ _y1,y2_ ] given that _X_ takes the value in the interval [ _x_ 1, _x2_ ]; _u_ 1, _u2_ , and _v1_ , _v2_ correspond to the probability values of the endpoints of the threshold intervals _x1_ , _x2_ , and _y1_ , _y2_ , respectively; and _C_ denotes the Copula joint distribution function. 

- 5) Conditional probabilities were derived for respective threshold intervals of node pairs ( _X, Y_ ), enabling CPT construction between DBN nodes and achieving DBN parameter learning. 

Through this methodological design, the extensive 42-year historical information is effectively preserved and encoded within the constructed the CPT, which govern the state transitions of the DBN. This mechanism successfully mitigates the inherent limitation of the “memoryless” property in first-order Markov models during the operational phase, ensuring that the DBN performs probabilistic inference of drought propagation grounded in long-term historical patterns. 

_3) DBN Inference for Drought Propagation Probability:_ DBN inference estimates the states of unobserved nodes in the network based on available observations to infer the most likely state of a variable by calculating its conditional probability, mainly including forward inference, backward inference, and smoothing [58]. Forward inference predicts a variable’s future 

WANG et al.: PROPAGATION CHARACTERISTICS OF SOIL MOISTURE DROUGHT TO HYDROLOGICAL DROUGHT 

29247 



Fig. 4. (a) Precipitation (PRE) and (b) evapotranspiration (ET) data for January 1982 in the Famine Early Warning Systems Network Land Data Assimilation System dataset for spatial zoning; (c) 10 zones identified by k-means spatial clustering; and (d) SSE (sum of squared errors) rate under different K values. 

state based on current and historical observations, making it suitable for predicting future states. Backward inference combines future observations to correct current state estimates, enhancing forward predictions. Smoothing combines forward and backward inference results to yield a comprehensive and accurate state estimate at a specific moment using historical and future information. 

DBN inference of drought propagation process is based on the hidden Markov model, which assumes that the current state depends only on the previous state [79]. State dependencies are thus only considered between neighboring time slices, which capture dynamic evolution while avoiding excessive complexity that would impede the estimation [80]. According to this property, the joint probability distribution _P_ ( _X1:t, Y1:t_ ) of the DBN at moment _t_ can be decomposed into the product of the initial slice _P_ ( _X1)_ distribution and state transfer probabilities between neighboring slices 



where _X_ 1 denotes the hidden state node at time _t_ ; _Yt_ is the observation node at time _t_ ; _P_ ( _X_ 1) denotes the probability distribution at the initial moment of the hidden state; _P_ ( _Xt_ | _Xt_ –1) denotes the state transition probability of the hidden state from the previous to the current moment, reflecting the evolutionary dependencies between the nodes across time slices; and _P_ ( _Yt_ | _Xt_ ) denotes the 

observation probability of different observing states _Yt_ from the hidden state _Xt_ , reflecting the immediate dependencies between nodes within the same time slice. 

The inference of propagation probability between the SSMI and SRI was realized by constructing a DBN for each spatial partition. For a specific grid within a zone, the SSMI data and the auxiliary variables (PRE and ET) at each time _t_ were extracted as observation data to conduct forward inference on the conditional probability of the SRI state at moment _t_ +1. Simultaneously, the SSMI state used in this inference was recorded. Next, the SRI data at moments _t+_ 2 and _t+_ 3 were treated as future observation data to perform backward inference, deriving the conditional probability of the SRI state at moment _t+1_ . Finally, the smoothed conditional probability of the SRI state at moment _t+1_ was obtained by combining the forward and backward inference results. 

In the inference process, for the soil moisture drought state corresponding to the SSMI observation data at moment _t_ , the conditional probabilities of the five hydrological drought states (extreme, severe, moderate, light, and no drought) of SRI at moment _t+_ 1 were derived through DBN inference. After performing inferences for all 504 SSMI observations, the results were categorized according to the five SSMI drought states. The average conditional probabilities for each SRI drought state under each SSMI drought state were thus calculated, creating a 5 _×_ 5 transition probability matrix as the drought propagation probabilities for this grid. For further analysis, the sum of the 

IEEE JOURNAL OF SELECTED TOPICS IN APPLIED EARTH OBSERVATIONS AND REMOTE SENSING, VOL. 19, 2026 

29248 



Fig. 5. Spatial distribution of drought propagation time and maximum correlation coefficient. (a) Propagation time from soil moisture drought to hydrological drought. (b) Spearman maximum correlation coefficients corresponding to propagation time; box plot of (c) propagation time, and (d) correlation coefficients for each zone. 

probabilities across the five SRI drought states for each SSMI drought state is processed to equal 1. 

## IV. RESULTS 

## _A. Spatial Zoning of the Yangtze River Basin_ 

Based on the PRE [Fig. 4(a)] and ET [Fig. 4(b)] data, the spatial zoning of the Yangtze River Basin was obtained via the k-means spatial clustering algorithm. The Elbow method was employed to compute the SSE for different clustering numbers _K_ [Fig. 4(d)]. At _K_ = 10, an inflection point was observed, and the subsequent decline in SSE became less pronounced. Therefore, the Yangtze River Basin was divided into 10 spatial units to reflect the spatial heterogeneity [Fig. 4(c)]. The zoning results were generally consistent with spatial differences in PRE and ET throughout the whole basin. For instance, Zones 1–4 in the middle-lower Yangtze River Basin corresponded to regions with elevated PRE, while Zone 10 situated on the Qinghai–Tibet Plateau exhibited significantly lower ET. Hence, k-means clustering effectively captured spatial heterogeneity in climate–hydrological variables. 

Among the 10 subregions, Zones 5 and 9 covered larger areas, contained 2402 and 2805 grids, respectively, and were 

characterized by typical hilly and high-altitude mountainous terrain. Conversely, Zones 2–4 covered smaller areas, averaging approximately 1200 grids each. They were located within the East China Plain region [Fig. 4(e)]. These zoning results were also consistent with the complex and variable topographic and geomorphological features of the Yangtze River Basin from the Qinghai–TibetPlateauinthewesttotheplainsintheeast(Fig. 1), thus verifying the reasonableness and necessity of k-means spatial zoning. 

## _B. Drought Propagation Time_ 

For each 0.1° _×_ 0.1° grid within the region, the Spearman’s correlations between the SSMI- _p_ (sliding window = _p_ months) and SRI-1 sequences were analyzed across different time scales. This approach enabled the mapping of spatial patterns for drought propagation time and maximum Spearman’s correlation coefficients in the Yangtze River Basin [Fig. 5(a) and (b)]. Overall, the average propagation time from soil moisture drought to hydrological drought in the Yangtze River Basin was 7.39 months, exhibiting a pronounced spatial pattern: longer in the west and shorter in the east. In particular, drought propagation time was notably extended in Zone 10 (west Qinghai–Tibet 

WANG et al.: PROPAGATION CHARACTERISTICS OF SOIL MOISTURE DROUGHT TO HYDROLOGICAL DROUGHT 

29249 



Fig. 6. Occurrence probabilities of different hydrological drought states under soil moisture drought; L: light, M: moderate, S: severe, E: extreme drought. The first letter denotes the soil moisture drought state, and the second letter denotes the hydrological drought state. For example, M-L represents the occurrence probability of light hydrological drought under moderate soil moisture drought. 

Plateau) and Zone 9 (high-elevation areas of Western Sichuan), some grids almost 12 months. This suggests an unusually slow drought propagation process in these areas, influenced by overlapping hydrological, meteorological, and topographical factors, resulting in a noticeable time lag. 

Conversely, in the eastern middle-lower plains (Zones 1–4), propagation time was generally less than four months, reflecting high sensitivity of runoff to soil moisture changes [Fig. 5(a)]. The median propagation time in Zones 2–4 in the plains of the lower Yangtze River reaches was concentrated at 3–4 months [Fig. 5(c)], with a narrow interquartile range (IQR) of approximately two months, reflecting rapid drought response and stable distributionpatterns.InZone1,themedianpropagationtimewas higher, about 6–7 months, likely influenced by stronger human activities intheYangtzeRiver Delta. Zone6exhibitedanaverage propagation of 7–8 months and contained numerous outliers. Zone 9, dominated by plateau mountains, had a median propagation time of approximately 12 months and an IQR exceeding 12 months, indicating substantial propagation lags, pronounced spatial heterogeneity, and significant local perturbations. 

In southeastern coastal regions and the lower Yangtze River Basin, the corresponding Spearman’s correlation coefficients for propagation time demonstrated a relatively uniform spatial distribution with limited variability, indicating homogeneous spatial characteristics [Fig. 5(b)]. Zones 1–5 exhibited median coefficient values between 0.75 and 0.8 with narrow IQR and low data dispersion, indicating strong and stable time-lag effect [Fig. 5(d)]. In contrast, Spearman’s correlation coefficients 

in the Western Sichuan Hills and parts of the Qinghai–Tibet Plateau generally fell below 0.4. Zones 6–8 showed expanded IQRs and more outliers, likely due to greater topographic heterogeneity. Zones 9–10 experienced further declines: mean correlation coefficients dropped to about 0.7, IQRs exceeded 0.35, and data dispersion was high. This suggests substantial uncertainty in drought propagation and reduced sensitivity to moisture changes. 

## _C. Drought Propagation Probability_ 

The propagation probability of soil moisture drought to hydrological drought was determined under varying conditions at 0.1° grid scale using a DBN model (Fig. 6). Notably, there are few no data grids in some large lakes, such as Poyang Lake, Dongting Lake, and Taihu Lake, mainly due to lack of original FLDAS soil moisture data and runoff data. Overall, the drought propagation probability showed significant spatial heterogeneity and hierarchical response characteristics, demonstrating nonlinear response patterns across the SSMI states. Under extreme soil moisture drought conditions [Fig. 6(a1)–(d1)], the mean propagation probability to hydrological drought was approximately 16.52%, with peak probabilities concentrated in high-elevation regionsalongtheQinghai–TibetPlateaumargins(upperYangtze River Basin) and Western Sichuan Plateau. This spatial pattern indicated enhanced soil moisture drought retention during the propagation process to runoff and more stabilized propagation processes. As soil moisture drought intensity lessened, the 

29250 

IEEE JOURNAL OF SELECTED TOPICS IN APPLIED EARTH OBSERVATIONS AND REMOTE SENSING, VOL. 19, 2026 

TABLE II 

AVERAGE PROBABILITY OF FOUR HYDROLOGICAL DROUGHT STATES IN VARIOUS REGIONS UNDER SOIL MOISTURE DROUGHT STATES 



probability of developing into extreme and severe hydrological drought decreased. However, in some areas of Western Sichuan hilly regions, propagation probabilities remained high at approximately 30% [Fig. 6(a1)–(a4), (b1)–(b4)]. This suggested that moderate to light soil moisture droughts was more likely to transform into extreme and severe hydrological droughts in regions with complex topographies. 

For light soil moisture droughts, the mean propagation probability to hydrological drought was about 12.33% [Fig. 6 (a4)–(d4)]. Notably, under moderate to light soil moisture drought state, the probability of corresponding hydrological droughtincreasedoverall,reachingameanof17.22%[Fig. 6(a3) –(d3), (a4)–(d4)]. High-probability areas extended toward the central-eastern plains and downstream areas, indicating that even less severe moisture droughts posed the elevated risk of triggering moderate to light hydrological droughts. This phenomenon is likely attributable to the complex variability of the subtropical monsoon climate in central-eastern China, illustrating how drought propagation mechanisms are influenced by fluctuations in moisture circulation. Further comparison revealed that the mean probability of moderate soil moisture drought leading to light hydrological drought (M-L) peaked at 21.01%, while the mean probability of light soil moisture droughttransformingintoseverehydrologicaldrought(L-S)was the lowest at 8.40%. This implies that hydrological drought risk cannot be predicted solely based on the soil moisture drought state, but rather requires an integrated assessment with regional climatic and environmental factors. 

From a basin-wide perspective, after soil moisture drought occurred, the probability of hydrological drought decreased with increasing SSMI states, from 18.93% (triggering light hydrological drought) to 12.34% (triggering extreme hydrological drought; Table Ⅱ), mirroring the effect of surface water cycles on drought propagation. However, significant spatial variations existed across subregions. In the upper Yangtze River Basin (Zones 9–10), the average propagation probability was relatively high, at approximately 19.13%. Notably, in Zone 10 (in the Qinghai–Tibet Plateau), the propagation probabilities from soil moisture drought to extreme, moderate, and light hydrological droughts far exceeded the basin average, reaching 21.26%, 22.50%, and 23.23%, respectively. Adjacent to the 

Qinghai–Tibet plateau, Zone 9 (Western Sichuan hilly region) exhibited complex mountainous terrain, where the probability of extreme hydrological drought triggered by soil moisture drought was as high as 20.38%. This suggests that areas with complex topography are highly sensitive to soil moisture changes in runoff systems, making them critical zones for future drought monitoring and mitigation. In contrast, the middle and lower Yangtze River regions (Zones 1–4) exhibited lower overall propagation probabilities, averaging approximately 10.95%. Notably, the probability of extreme hydrological drought remained below 7% in these areas, indicating strong drought resilience, as soil moisture droughts were mitigated by frequent moisture replenishment in these regions. 

## V. DISCUSSION 

## _A. Importance of Spatial Zoning for Drought Propagation_ 

_1) Influence of Spatial Zoning on Calculating the Drought Indices:_ Given the large differences in the natural conditions of different regions, calculating the drought indices under appropriate spatial zoning can significantly improve the accuracy and stability of regional drought feature extraction, avoided the limitation of neglecting spatial correlations in grid-based approaches and smoothing regional features in basin-wide approaches [81], [82]. In this article, the Yangtze River Basin was divided into 10 subregions based on PRE and ET data, whichreflectedtheregionalcomplexandvariableenvironmental gradients, from the western Qinghai–Tibet Plateau to the eastern plains. The zoning results were highly consistent with the spatial patterns of PRE and ET in the basin, including significantly higher precipitation in Zones 1 and 5 and significantly lower precipitation in Zone 10 in the northwest (Fig. 4). Hence, k- means clustering can effectively capture the spatial variability of climate–hydrological variables. 

To further verify the optimization effect of spatial zoning on drought index calculation, this article constructed comparative experiments spanning the western, central, and eastern regions of the Yangtze River Basin. We selected three representative regions: Zone 9 (western region), primarily covering western Sichuan Province of the plateau-basin transition zone with a significantverticalclimategradient [83];Zone5(centralregion), 

29251 

WANG et al.: PROPAGATION CHARACTERISTICS OF SOIL MOISTURE DROUGHT TO HYDROLOGICAL DROUGHT 



Fig. 7. Comparison of regional mean monthly time series of SSMI and SRI during 1982–2023, calculated based on spatial zoning versus whole-basin data across eastern (Zone 2), central (Zone 5), and western (Zone 9) regions of the Yangtze River Basin. 

encompassing most of Chongqing and Guizhou Province, where typical mountainous and karstic landforms lead to poor soil water retention and rapid surface moisture loss [84]; and Zone 2 (eastern region), primarily covering Jiangxi Province, which is a typical plain and river network area strongly influenced by the monsoon and lake regulation [85]. The varying geographical and climatic conditions across the basin result in significant differences in drought evolution characteristics among these three subregions. 

BasedonthecalculationmethodinSection III-A-2,thisarticle utilized spatial zoning (regional) data and whole-basin (global) data from 1982 to 2023 to calculate the monthly SSMI and SRI for each grid within the three typical regions mentioned above. The comparative time-series curves are constructed by extracting the regional mean values. The results show that across the three representative zones, the spatial zoning-based SSMI time series [Fig. 7(a1), (b1), and (c1)] maintained overall consistency with the global results in terms of fluctuation patterns, but exhibited higher sensitivity in detecting drought events and depicting the severity of extreme droughts. Traditional wholebasin calculations are constrained by the averaging effect of the vast basin space, often underestimating the severity of local water deficit conditions. Similarly, in the comparison of runoff indices [Fig. 7(a2), (b2), (c2)], the SRI based on whole-basin data displayed extremely dramatic and exaggerated fluctuations, which were primarily driven by the interference of extreme 

precipitation/runoff anomalies in other distant regions within the basin. In contrast, the spatial-zoning-based SRI series effectively eliminated these external interferences, demonstrating a more convergent fluctuation range and more precisely reflecting the true local hydrological drought or wet states. In general, compared to whole-basin-based indices, spatial-zoning-based indices account for regional heterogeneity and prevent the distortion of extreme values, depicting droughts more accurately in each subregion. 

_2) Influence of Spatial Zoning on DBN Modeling:_ Spatial zoning also plays an important role in parameter learning and conditional inference within DBN modeling. Thus, drought indices and auxiliary variables (PRE, SSMI, ET, and SRI) constructed from basin-wide data were used for DBN parameter learning and propagation probability inference. The associated results were compared with those derived from spatial-zoningbased indices. To enhance clarity, the probability inference results for the four states of soil moisture drought were averaged with those of their all-corresponding hydrological drought states. Comparative analysis revealed that the DBN inference based on partitioned modeling produced clearer spatial patterns, with higher propagation probabilities in upstream areas and lower probabilities downstream [Fig. 8(a1)–(a4)]. Regions with higher probability values appeared in upstream plateaus, high-mountain regions, and along the Sichuan Basin margin. In contrast, areas with dense rivers and lakes or flat terrains, such 

29252 

IEEE JOURNAL OF SELECTED TOPICS IN APPLIED EARTH OBSERVATIONS AND REMOTE SENSING, VOL. 19, 2026 



Fig. 8. Comparison of DBN inference probabilities from four levels of soil moisture drought to hydrological drought based on drought indices from spatial zoning data (a1)–(a4) and whole-basin data (b1)–(b4). L: light, M: moderate, S: severe, and E: extreme drought. 

as the Two-Lake Plain, Jianghan Plain, and the middle-lower reaches of the Yangtze River Delta, exhibited lower probabilities and more distinct spatial variation. Conversely, basin-wide DBN inference produced smoother transitions with less pronounced spatial differentiation [Fig. 8(b1)–(b4)], with an overall higher probability and an approximately 2% increase in the average probability of hydrological drought under various soil moisture drought states. 

The divergence between inference results primarily stemmed from differences in DBN training approaches. Zoning-based DBN models were trained independently using data from distinct spatial subdivisions, allowing them to capture localized spatial heterogeneity—particularly in areas with significant topographic variations, such as upstream mountainous regions versus downstream plains. In contrast, the basin-wide DBN model, trained on the entire watershed data, failed to account for inter-regional disparities and was thus unable to accurately capture localized characteristics. As a result, the basin-wide DBN yielded more homogeneous spatial distributions of propagation probabilities, particularly for extreme and severe soil moisture drought, resulting in smoother regional distinctions and higher overall predicted probabilities. 

## _B. Advantages of DBN for Drought Propagation_ 

Building upon traditional BN, DBN incorporates temporal modeling through time slices and temporal edges, enabling the capture of immediate and evolutionary dependencies [56]. Unlike BN with only modeling static relationships, DBN can handle uncertainties and missing data in time-series analysis and offer superior inferential power for sequential data, resulting in more accurate conditional probability estimates [55], [58]. To assess the advantages of DBN over BN in drought propagation probability studies, conditional inference was performed using both models for each grid. Specifically, a BN structure (SSMI _→_ SRI) was constructed, with the same SSMI and SRI time-series data for each grid. Dependencies directly between SSMI and SRI were modeled using the Copula function, and conditional probabilities of different SRI states under different SSMI states 

were inferred. To more intuitively reflect the differences between the two models, propagation probabilities of SRI were averaged across different SSMI states, and the inference results of hydrological drought under severe soil moisture drought were compared. 

The DBN inference results demonstrated more pronounced spatial heterogeneity across the watershed, with higher drought propagation probabilities in the Qinghai–Tibet Plateau and Western Sichuan mountainous regions [Fig. 9(a)], about 20%– 30%, and lower probabilities in the central-eastern plains. In contrast, BN inference results indicated relatively higher and more uniformly distributed propagation probabilities across the central-eastern plains, while the propagation probability is relatively low in the Qinghai–Tibet Plateau and the hilly areas of western Sichuan, about 10%–20% [Fig. 9(b)]. This discrepancy primarily resulted from incorporating multimoment observational data in the DBN, which better captures drought propagation dynamics. Moreover, DBN can recognize the dependencies between different time slices, enhancing inference accuracy and capturing spatial heterogeneity. In contrast, BN rely on single-moment data, missing temporal characteristics. This pattern likely reflects the BN’s structural omission of PRE and ET variables, which prevents it from accounting for the unique moisture recycling processes in central-eastern China’s subtropical monsoon climate system. Meanwhile, compared with DBN results, there are obviously more empty BN inference results in the hilly areas of western Sichuan and the middle reaches of the Yangtze River, which may be due to the complex terrain of the hills and the large errors in the observed SSMI data, leading to abnormal inference results. 

## _C. Policy Implications and Research Prospects_ 

This article combined the k-means algorithm and DBN model for drought propagation in subregions, enhancing the accuracy ofdroughtfeatureextraction.Asadata-drivenmodelingprocess, the proposed framework does not rely on complex physical hydrological parameters but are directly driven by conventional 

29253 

WANG et al.: PROPAGATION CHARACTERISTICS OF SOIL MOISTURE DROUGHT TO HYDROLOGICAL DROUGHT 



Fig. 9. Comparison of (a) DBN inference results and (b) BN inference results under severe soil moisture drought state, detailed display for local region 1, 2, 3. 

meteorological and hydrological data, exhibiting good transferability. Meanwhile, this framework has been preliminarily applied in the Yangtze River Basin with one of the most diverse climate and geographic environments, indicating its application potential to be generalized to other basins or regions with different hydroclimatic characteristics. 

Given the notable spatial heterogeneity of drought propagation features, region-specific countermeasures are required in the Yangtze River Basin. For instance, in the middle-lower reaches with short propagation time and high probability, real-time monitoring is needed to dynamically adjust risk assessments and provide early warning information. Additionally, emergency response capabilities in water resource dispatch, farmland irrigation, and disaster relief must be strengthened. In the western mountains and the Qinghai–Tibet Plateau with long drought propagation time but high probability, flexible multisource observation, and spatiotemporal correction should be prioritized to improve the monitoring effectiveness and actively block the drought propagation [86]. Additionally, given the nonlinear decreasing response of hydrological drought to soil moisture drought and the high probability of “light _→_ severe/extreme” transitions, policy-makers and researchers should focus on the nonlinear propagation mechanisms and multifactorial control frameworks in drought propagation [8]. 

However, there are still certain limitations in this drought propagation analysis framework. First, regarding data sources, reanalysis datasets such as FLDAS inevitably contain model structural errors and input forcing data errors [87]. To address this limitation, future article could consider adopting higher quality reanalysis datasets (e.g., ERA5 and GLDAS) or integrating in-situ observation data to further improve the accuracy of the drought indices. Additionally, finer-scale datasets of daily or weekly meteorological observations could be also introduced to capture the dynamic evolution of drought propagation [83]. 

Second, the k-means clustering in this article only selected two basic climatic variables for spatial zoning. Future article could expand more variables to reflect the regional heterogeneity, such as vegetation indices, soil properties, and topographic relief [88]. This would facilitate the construction of unique drought propagation processes tailored to each subregion, thereby effectively enhancing the DBN inference. Moreover, more intelligent clustering algorithms could be explored to capture the spatiotemporal evolution patterns of these variables, such as dynamic time warping and graph neural networks [89], [90], further elevating the physical rigor and accuracy of spatial zoning across basins. 

Third, regarding the method for extracting drought propagation time, although the Spearman correlation coefficient combined with multiscale drought data is effective and possesses 

29254 

IEEE JOURNAL OF SELECTED TOPICS IN APPLIED EARTH OBSERVATIONS AND REMOTE SENSING, VOL. 19, 2026 

strong statistical robustness, it essentially remains within the realm of traditional statistical analysis. Future article could introduce machine learning algorithms to capture nonlinear dependency relationships among different drought indices to better estimate the propagation time [91]. 

Finally, the current DBN model relies on only four key variables, limiting its capacity to fully capture the complex interactions among climatic, hydrological, and anthropogenic factors. Multisource environmental variables should be incorporated to depict these dynamic mechanisms more comprehensively. Furthermore, the inherent “memoryless” property of the DBN’s first-order Markov assumption restricts its ability to model historical dependencies in long-term climate fluctuations. Thus, future article will integrate advanced deep-learning architectures, such as LSTM, ConvLSTM, and SimVP models [92], [93], to effectively uncover complex dependencies and patterns of drought propagation over long-term sequences. 

## VI. CONCLUSION 

A thorough understanding of the mechanisms and patterns underlying the propagation of soil moisture drought to hydrological drought is critical for improving drought monitoring, emergency responses, vegetation sustainability, agricultural productivity, and ecological conservation. Taking the Yangtze River Basin as a case study, soil moisture and hydrological drought were assessed through the SSMI and SRI during 1982–2023, respectively, based on the spatial zoning results by k-means algorithm. Spearman’s correlations were applied to examine the spatial distribution of drought propagation times. Within each subregion, two auxiliary variables (PRE and ET) and two drought indices (SSMI and SRI) were incorporated into a DBN model, with dependencies modeled by the Copula function. The conditional probabilities for the transition from soil moisture drought to hydrological drought were then inferred. 

The findings indicate that the Yangtze River Basin can be segmentedinto10subregionsbasedonPREandET.Theaverage propagation time from soil moisture drought to hydrological drought is 7.39 months, with notable spatial heterogeneity observed across regions. Propagation probability also varied significantly, with higher values in the complex, precipitationdeficient areas, such as the Western Sichuan hills and the Qinghai–Tibet Plateau (average: 19.13%) and lower probabilities in the flat, precipitation-rich middle and lower reaches of the basin (average: 10.95%). The likelihood of hydrological drought occurrence increased in tandem with the severity of soil moisture drought, reaching 16.52% in extreme drought states and 12.33% under light droughts. Comparison experiments also prove that the integration of spatial zoning and DBN model can enhance the understanding of drought propagation dynamics. In the future, additional drought-relevant variables and more distinctive regions should be considered to further improve the calculation framework of propagation characteristics from soil moisture drought to hydrological drought. 

## ACKNOWLEDGMENT 

Sincere thanks are given for the comments and contributions of anonymous reviewers and members of the editorial team. 

## REFERENCES 

- [1] G. G. Haile, Q. Tang, W. Li, X. Liu, and X. Zhang, “Drought: Progress in broadening its understanding,” _WIREs Water_ , vol. 7, no. 2, 2020, Art. no. e1407. 

- [2] J.-T. Shiau, “Causality-based drought propagation analyses among meteorological drought, hydrologic drought, and water shortage,” _Sci. Total Environ._ , vol. 888, 2023, Art. no. 164216. 

- [3] C. Hao, J. Zhang, and F. Yao, “Combination of multi-sensor remote sensing data for drought monitoring over Southwest China,” _Int. J. Appl. Earth Observ. Geoinf._ , vol. 35, pp. 270–283, 2015. 

- [4] Y. Liu, F. Shan, H. Yue, X. Wang, and Y. Fan, “Global analysis of the correlation and propagation among meteorological, agricultural, surface water, and groundwater droughts,” _J. Environ. Manage._ , vol. 333, 2023, Art. no. 117460. 

- [5] Y. Liu et al., “Understanding the spatiotemporal links between meteorological and hydrological droughts from a three-dimensional perspective,” _J. Geophys. Res.: Atmos._ , vol. 124, no. 6, pp. 3090–3109, 2019. 

- [6] M. Dai et al., “Propagation characteristics and mechanism from meteorological to agricultural drought in various seasons,” _J. Hydrol._ , vol. 610, 2022, Art. no. 127897. 

- [7] A. F. Van Loon, “Hydrological drought explained,” _Wiley Interdiscipl. Rev.: Water_ , vol. 2, no. 4, pp. 359–392, 2015. 

- [8] Y. Xu, X. Zhang, X. Wang, Z. Hao, V. P. Singh, and F. Hao, “Propagation from meteorological drought to hydrological drought under the impact of human activities: A case study in northern China,” _J. Hydrol._ , vol. 579, 2019, Art. no. 124147. 

- [9] A. AghaKouchak et al., “Anthropogenic drought: Definition, challenges, and opportunities,” _Rev. Geophys._ , vol. 59, no. 2, 2021, Art. no. e2019RG000683. 

- [10] E. Peters, P. J. J. F. Torfs, H. A. J. van Lanen, and G. Bier, “Propagation of drought through groundwater—A new approach using linear reservoir theory,” _Hydrol. Processes_ , vol. 17, no. 15, pp. 3023–3040, 2003. 

- [11] Q. Zhang et al., “Spatiotemporal characteristics of meteorological to hydrological drought propagation under natural conditions in China,” _Weather Climate Extremes_ , vol. 38, 2022, Art. no. 100505. 

- [12] Z. Xu, Z. Wu, Q. Shao, H. He, and X. Guo, “From meteorological to agricultural drought: Propagation time and probabilistic linkages,” _J. Hydrol.: Regional Stud._ , vol. 46, 2023, Art. no. 101329. 

- [13] E. Savelli, M. Rusca, H. Cloke, and G. Di Baldassarre, “Drought and society: Scientific progress, blind spots, and future prospects,” _WIREs Climate Change_ , vol. 13, no. 3, 2022, Art. no. e761. 

- [14] Z. Wang et al., “Temporal and spatial propagation characteristics of meteorological drought to hydrological drought and influencing factors,” _Atmos. Res._ , vol. 299, 2024, Art. no. 107212. 

- [15] A. K. Mishra and V. P. Singh, “A review of drought concepts,” _J. Hydrol._ , vol. 391, no. 1, pp. 202–216, 2010. 

- [16] C. Ndehedehe, “Hydro-climatic extremes: Climate change and Human influence,” in _Hydro-Climatic Extremes in the Anthropocene_ . Cham, Switzerland: Springer International Publishing, 2023, pp. 25–55. 

- [17] G. Wang et al., “Exogenous moisture deficit fuels drought risks across China,” _NPJ Climate Atmos. Sci._ , vol. 6, no. 1, 2023, Art. no. 217. 

- [18] S. Wang et al., “Global anthropogenic effects on meteorological— Hydrological—Soil moisture drought propagation: Historical analysis and future projection,” _J. Hydrol._ , vol. 653, 2025, Art. no. 132755. 

- [19] B. Su, J. Huang, X. Zeng, C. Gao, and T. Jiang, “Impacts of climate change on streamflow in the upper Yangtze River basin,” _Climatic Change_ , vol. 141, no. 3, pp. 533–546, 2017. 

- [20] Y. Yang, Y. Feng, X. He, and M. Li, “Spatial heterogeneity and environmental drivers of drought vulnerability in the Yangtze River Basin,” _Ecol. Indicators_ , vol. 179, 2025, Art. no. 114246. 

- [21] L. Fawen, Z. Manjing, Z. Yong, and J. Rengui, “Influence of irrigation and groundwater on the propagation of meteorological drought to agricultural drought,” _Agricultural Water Manage._ , vol. 277, 2023, Art. no. 108099. 

- [22] S. Bachmair, C. Svensson, J. Hannaford, L. J. Barker, and K. Stahl, “A quantitative analysis to objectively appraise drought indicators and model drought impacts,” _Hydrol. Earth Syst. Sci._ , vol. 20, no. 7, pp. 2589–2609, 2016. 

- [23] Y. Mao, Z. Wu, H. He, G. Lu, H. Xu, and Q. Lin, “Spatio-temporal analysis of drought in a typical plain region based on the soil moisture anomaly percentage index,” _Sci. Total Environ._ , vol. 576, pp. 752–765, 2017. 

- [24] L. Yang, S. Zeng, Y. Jiang, J. Gu, and C. He, “Comparison of drought characteristics in the upstream of the Heihe River Basin based on Palmer Drought Severity Index and Standard Precipitation Index,” _Res. Soil Water Conservation_ , vol. 24, no. 2, pp. 132–136, 2017. 

29255 

WANG et al.: PROPAGATION CHARACTERISTICS OF SOIL MOISTURE DROUGHT TO HYDROLOGICAL DROUGHT 

- [25] Z. Q. Zhou et al., “Characteristics of propagation from meteorological drought to hydrological drought in the Pearl River Basin,” _J. Geophysical Res.-Atmos._ , vol. 126, no. 4, 2021, Art. no. e2020JD033959. 

- [26] Z. Hao and A. AghaKouchak, “A nonparametric multivariate multiindex drought monitoring framework,” _J. Hydrometeorol._ , vol. 15, no. 1, pp. 89–101, 2014. 

- [27] V. A. Bento, C. M. Gouveia, C. C. DaCamara, and I. F. Trigo, “A climatological assessment of drought impact on vegetation health index,” _Agricultural Forest Meteorol._ , vol. 259, pp. 286–295, 2018. 

- [28] W. Jiao, L. Wang, and M. F. McCabe, “Multi-sensor remote sensing for drought characterization: Current status, opportunities and a roadmap for the future,” _Remote Sens. Environ._ , vol. 256, 2021, Art. no. 112313. 

- [29] A. McNally et al., “Data descriptor: A land data assimilation system for sub-Saharan Africa food and water security applications,” _Sci. Data_ , vol. 4, 2017, Art. no. 170012. 

- [30] R. Albarakat, M.-H. Le, and V. Lakshmi, “Assessment of drought conditions over Iraqi transboundary rivers using FLDAS and satellite datasets,” _J. Hydrol.: Regional Stud._ , vol. 41, 2022, Art. no. 101075. 

- [31] L. Zhao, T. Wen, B. Zhao, and P. Shi, “Drought tendency and characteristic analysis in Southwest China during recent 50 years,” _J. China Hydrol._ , vol. 41, no. 6, pp. 91–95, 2021. 

- [32] T. Yu et al., “Evaluating surface soil moisture characteristics and the performance of remote sensing and analytical products in Central Asia,” _J. Hydrol._ , vol. 617, 2023, Art. no. 128921. 

- [33] S. Huang, P. Li, Q. Huang, G. Leng, B. Hou, and L. Ma, “The propagation from meteorological to hydrological drought and its potential influence factors,” _J. Hydrol._ , vol. 547, pp. 184–195, 2017. 

- [34] Y. Zhang et al., “Spatial heterogeneity of vegetation resilience changes to different drought types,” _Earth’s Future_ , vol. 11, no. 4, 2023, Art. no. e2022EF003108. 

- [35] R. Li et al., “Quantitative analysis of agricultural drought propagation process in the Yangtze River Basin by using cross wavelet analysis and spatial autocorrelation,” _Agricultural Forest Meteorol._ , vol. 280, 2020, Art. no. 107809. 

- [36] I. Harris, P. D. Jones, T. J. Osborn, and D. H. Lister, “Updated high-resolution grids of monthly climatic observations—The CRU TS3.10 dataset,” _Int. J. Climatol._ , vol. 34, no. 3, pp. 623–642, 2014. 

- [37] K. Krishna and M. N. Murty, “Genetic K-means algorithm,” _IEEE Trans. Syst., Man, Cybern., Part B_ , vol. 29, no. 3, pp. 433–439, Jun. 1999. 

- [38] D. Steinley, “K-means clustering: A half-century synthesis,” _Brit. J. Math. Statist. Psychol._ , vol. 59, no. 1, pp. 1–34, 2006. 

- [39] X. Zhang et al., “Drought propagation under global warming: Characteristics, approaches, processes, and controlling factors,” _Sci. Total Environ._ , vol. 838, 2022, Art. no. 156021. 

- [40] L. Ma et al., “Propagation dynamics and causes of hydrological drought in response to meteorological drought at seasonal timescales,” _Hydrol. Res._ , vol. 53, no. 1, pp. 193–205, 2021. 

- [41] A. G. Pendergrass et al., “Flash droughts present a new challenge for subseasonal-to-seasonal prediction,” _Nature Climate Change_ , vol. 10, no. 3, pp. 191–199, 2020. 

- [42] S. Ho, L. Tian, M. Disse, and Y. Tuo, “A new approach to quantify propagationtimefrommeteorologicaltohydrologicaldrought,” _J.Hydrol._ , vol. 603, 2021, Art. no. 127056. 

- [43] Z. Hao, V. P. Singh, and Y. Xia, “Seasonal drought prediction: Advances, challenges, and future prospects,” _Rev. Geophys._ , vol. 56, no. 1, pp. 108–141, 2018. 

- [44] V. M. B. Raposo, V. A. F. Costa, and A. F. Rodrigues, “A review of recent developments on drought characterization, propagation, and influential factors,” _Sci. Total Environ._ , vol. 898, 2023, Art. no. 165550. 

- [45] A. A. Pathak and B. M. Dodamani, “Connection between meteorological and groundwater drought with copula-based bivariate frequency analysis,” _J. Hydrologic Eng._ , vol. 26, no. 7, 2021, Art. no. 05021015. 

- [46] Y. Guo et al., “Elucidating the effects of mega reservoir on watershed drought tolerance based on a drought propagation analytical method,” _J. Hydrol._ , vol. 598, 2021, Art. no. 125738. 

- [47] G. Geng, B. Zhang, Q. Gu, Z. He, and R. Zheng, “Drought propagation characteristics across China: Time, probability, and threshold,” _J. Hydrol._ , vol. 631, 2024, Art. no. 130805. 

- [48] C. Yang, C. Liu, X. Xing, and X. Ma, “Predicting the risk and trigger thresholds for propagation of meteorological droughts to agricultural droughts in China based on Copula-Bayesian model,” _Agricultural Water Manage._ , vol. 313, 2025, Art. no. 109468. 

- [49] N. I. Trifonova, B. E. Scott, M. De Dominicis, J. J. Waggitt, and J. Wolf, “Bayesian network modelling provides spatial and temporal understanding of ecosystem dynamics within shallow shelf seas,” _Ecol. Indicators_ , vol. 129, 2021/10/01/2021, Art. no. 107997. 

- [50] Q. Zhang, Y. P. Li, G. H. Huang, H. Wang, and Z. Y. Shen, “Bayesian analysis of variance for quantifying multi-factor effects on drought propagation,” _J. Hydrol._ , vol. 632, 2024, Art. no. 130911. 

- [51] D. Youtian, C. Feng, X. Wenli, and L. Yongbin, “Recognizing interaction activities using dynamic Bayesian network,” in _Proc. 18th Int. Conf. Pattern Recognit._ , 2006, pp. 618–621. 

- [52] H. Huang et al., “Thriving arid oasis urban agglomerations: Optimizing ecosystem services pattern under future climate change scenarios using dynamic Bayesian network,” _J. Environ. Manage._ , vol. 350, 2024, Art. no. 119612. 

- [53] X. Wu, H. Liu, L. Zhang, M. J. Skibniewski, Q. Deng, and J. Teng, “A dynamic Bayesian network based approach to safety decision support in tunnel construction,” _Rel. Eng. System Saf._ , vol. 134, pp. 157–168, 2015. 

- [54] H. Wang, Y. Li, G. Huang, Q. Zhang, Y. Ma, and Y. Li, “Quantifying multidimensional drought propagation risks under climate change: A vinecopula Bayesian factorial analysis method,” _J. Hydrol._ , vol. 637, 2024, Art. no. 131396. 

- [55] G. Konapala and A. Mishra, “Review of complex networks application in hydroclimatic extremes with an implementation to characterize spatiotemporal drought propagation in continental USA,” _J. Hydrol._ , vol. 555, pp. 600–620, 2017. 

- [56] P. Shiguihara, A. D. A. Lopes, and D. Mauricio, “Dynamic Bayesian network modeling, learning, and inference: A survey,” _IEEE Access_ , vol. 9, pp. 117639–117648, 2021. 

- [57] R. F. Ropero, A. E. Nicholson, P. A. Aguilera, and R. Rumí, “Learning and inference methodologies for hybrid dynamic Bayesian networks: A case study for a water reservoir system in Andalusia, Spain,” _Stochastic Environ. Res. Risk Assessment_ , vol. 32, no. 11, pp. 3117–3135, 2018. 

- [58] J. Chang et al., “Dynamic Bayesian networks with application in environmental modeling and management: A review,” _Environ. Model. Softw._ , vol. 170, 2023, Art. no. 105835. 

- [59] E. Zhou, L. Wang, H. Wang, Z. Wang, and R. Wei, “Spatialtemporal distribution prediction of transmission corridor wildfire risk based on ARIMA-DBN,” _Front. Forests Glob. Change_ , vol. 8, 2025, Art. no. 1637263. 

- [60] K. Li, C. Zhu, L. Wu, and L. Huang, “Problems caused by the Three Gorges Dam construction in the Yangtze River Basin: A review,” _Environ. Rev._ , vol. 21, no. 3, pp. 127–135, 2013. 

- [61] X. Xu, H. Hu, Y. Tan, G. Yang, P. Zhu, and B. Jiang, “Quantifying the impacts of climate variability and human interventions on crop production andfoodsecurityintheYangtzeRiverBasin,China,1990–2015,” _Sci.Total Environ._ , vol. 665, pp. 379–389, 2019. 

- [62] T. Jiang, B. Su, and H. Hartmann, “Temporal and spatial trends of precipitation and river flow in the Yangtze River Basin, 1961–2000,” _Geomorphology_ , vol. 85, no. 3, pp. 143–154, 2007. 

- [63] A. McNally, NASA/GSFC/HSL, “FLDAS Noah Land Surface Model L4 Global Monthly 0.1 _×_ 0.1 degree (MERRA-2 and CHIRPS) V001,” Goddard Earth Sciences Data and Information Services Center (GES DISC), 2018. 

- [64] A. McNally et al., “A land data assimilation system for sub-Saharan Africa food and water security applications,” _Sci. Data_ , vol. 4, no. 1, 2017, Art. no. 170012. 

- [65] A. McNally et al., “A Central Asia hydrologic monitoring dataset for food and water security applications in Afghanistan,” _Earth Syst. Sci. Data_ , vol. 14, no. 7, pp. 3115–3135, 2022. 

- [66] J. Wu, C. Miao, H. Zheng, Q. Duan, X. Lei, and H. Li, “Meteorological and hydrological drought on the Loess Plateau, China: Evolutionary characteristics, impact, and propagation,” _J. Geophys. Res.: Atmos._ , vol. 123, no. 20, pp. 11,569–11,584, 2018. 

- [67] T.Sattler, B.Leibe, and L.Kobbelt, “SCRAMSAC: Improving RANSAC’s efficiency with a spatial consistency filter,” in _Proc. IEEE 12th Int. Conf. Comput. Vis._ , 2009, pp. 2090–2097. 

- [68] S. Shukla and A. W. Wood, “Use of a standardized runoff index for characterizing hydrologic drought,” _Geophys. Res. Lett._ , vol. 35, no. 2, 2008, Art. no. L02405. 

- [69] H. Carrão, S. Russo, G. Sepulcre-Canto, and P. Barbosa, “An empirical standardized soil moisture index for agricultural drought assessment from remotely sensed data,” _Int. J. Appl. Earth Observ. Geoinf._ , vol. 48, pp. 74–84, 2016. 

29256 

IEEE JOURNAL OF SELECTED TOPICS IN APPLIED EARTH OBSERVATIONS AND REMOTE SENSING, VOL. 19, 2026 

- [70] A. A. Berg, J. S. Famiglietti, J. P. Walker, and P. R. Houser, “Impact of bias correction to reanalysis products on simulations of North American soil moisture and hydrological fluxes,” _J. Geophys. Res.: Atmos._ , vol. 108, no. D16, 2003, Art. no. 4490. 

- [71] C. Alvarez-Garreton, D. Ryu, A. W. Western, W. T. Crow, and D. E. Robertson, “The impacts of assimilating satellite soil moisture into a rainfall–runoff model in a semi-arid catchment,” _J. Hydrol._ , vol. 519, pp. 2763–2774, 2014. 

- [72] General Administration of Quality Supervision, Inspection and Quarantine of the People’s Republic of China and Standardization Administration of China, _Grade of Agricultural Drought (GB/T 32136-2015)_ , Standards Press of China, Beijing, China, 2015. 

- [73] Z. Han et al., “GRACE-based high-resolution propagation threshold from meteorological to groundwater drought,” _Agricultural Forest Meteorol._ , vol. 307, 2021, Art. no. 108476. 

- [74] Y. Xu, X. Zhang, Z. Hao, V. P. Singh, and F. Hao, “Characterization of agricultural drought propagation over China based on bivariate probabilistic quantification,” _J. Hydrol._ , vol. 598, 2021, Art. no. 126194. 

- [75] A.Dai,T.Zhao,andJ.Chen,“ClimateChangeanddrought:Aprecipitation and evaporation perspective,” _Curr. Climate Change Rep._ , vol. 4, no. 3, pp. 301–312, 2018. 

- [76] W. H. Maes and K. Steppe, “Estimating evapotranspiration and drought stress with ground-based thermal remote sensing in agriculture: A review,” _J. Exp. Botany_ , vol. 63, no. 13, pp. 4671–4712, 2012. 

- [77] Y. Zhao, T. Zhu, Z. Zhou, H. Cai, and Z. Cao, “Detecting nonlinear information about drought propagation time and rate with nonlinear dynamic system and chaos theory,” _J. Hydrol._ , vol. 623, 2023, Art. no. 129810. 

- [78] A. J. K. Sklar, “Random variables, joint distribution functions, and copulas,” _Kybernetika_ , vol. 9, no. 6, pp. 449–460, 1973. 

- [79] J. C. Rajapakse and J. Zhou, “Learning effective brain connectivity with dynamic Bayesian networks,” _NeuroImage_ , vol. 37, no. 3, pp. 749–760, 2007. 

- [80] G. Rachid, I. Alameddine, M. A. Najm, S. Qian, and M. El-Fadel, “Dynamic Bayesian networks to assess anthropogenic and climatic drivers of saltwater intrusion: A decision support tool toward improved management,” _Integr. Environ. Assessment Manage._ , vol. 17, no. 1, pp. 202–220, 2021. 

- [81] J. Mardian, “The role of spatial scale in drought monitoring and early warning systems: A review,” _Environ. Rev._ , vol. 30, no. 3, pp. 438–459, 2022. 

- [82] H. Carrão, A. Singleton, G. Naumann, P. Barbosa, and J. V. Vogt, “An optimized system for the classification of meteorological drought intensity with applications in drought frequency analysis,” _J. Appl. Meteorol. Climatol._ , vol. 53, no. 8, pp. 1943–1960, Aug. 2014. 

- [83] S.Chenetal.,“Propagationofmeteorologicaltoagriculturalflashdroughts using a novel weekly index,” _J. Hydrol.: Regional Stud._ , vol. 63, 2026, Art. no. 102973. 

- [84] Y. Li, D. Xie, S. Wang, and C. Wei, “Impact of land cover types on the soil characteristics in karst area of Chongqing,” _J. Geographical Sci._ , vol. 16, no. 2, pp. 143–154, 2006. 

- [85] H. Guo, Q. Hu, and T. Jiang, “Annual and seasonal streamflow responses to climate and land-cover changes in the Poyang Lake Basin, China,” _J. Hydrol._ , vol. 355, no. 1–4, pp. 106–122, 2008. 

- [86] F. Sun, A. Mejia, P. Zeng, and Y. Che, “Projecting meteorological, hydrological and agricultural droughts for the Yangtze River Basin,” _Sci. Total Environ._ , vol. 696, 2019, Art. no. 134076. 

- [87] B. Li, A. Hazra, A. McNally, K. Slinski, S. Shukla, and W. Anderson, “Skills in sub-seasonal to seasonal terrestrial water storage forecasting: Insights from the FEWS NET land data assimilation system,” _Hydrol. Earth Syst. Sci._ , vol. 30, no. 4, pp. 1097–1115, 2026. 

- [88] Y. Zhang et al., “Spatial optimization of cultivated land protection policy implementation effect in China using a geographically optimal zonesbased heterogeneity model,” _GISci. Remote Sens._ , vol. 63, no. 1, 2026, Art. no. 2677378. 

- [89] A. Mueen and E. Keogh, “Extracting optimal performance from dynamic time warping,” in _Proc. 22nd ACM SIGKDD Int. Conf. Knowl. Discov. Data Mining_ , 2016, pp. 2129–2130. 

- [90] G. Corso, H. Stark, S. Jegelka, T. Jaakkola, and R. Barzilay, “Graph neural networks,” _Nature Rev. Methods Primers_ , vol. 4, no. 1, 2024, Art. no. 17. 

- [91] H. Wei, M. W. Boota, S. Ali, S. Nazli, C. Hu, and J. Guo, “Climate driven drought risk and machine learning approaches for urban resilience and sustainable water governance,” _Environ. Res._ , vol. 299, 2026, Art. no. 124220. 

- [92] T. Wang, X. Tu, V. P. Singh, X. Chen, K. Lin, and Z. Zhou, “Drought prediction: Insights from the fusion of LSTM and multi-source factors,” _Sci. Total Environ._ , vol. 902, 2023, Art. no. 166361. 

- [93] Q. Zhang, C. Miao, J. Gou, and H. Zheng, “Spatiotemporal characteristics and forecasting of short-term meteorological drought in China,” _J. Hydrol._ , vol. 624, 2023, Art. no. 129924. 

