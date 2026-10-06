Earth Science Informatics (2024) 17:4949–4968 https://doi.org/10.1007/s12145-024-01437-w 

**RESEARCH** 



# **Integration of machine learning and remote sensing for drought index prediction: A framework for water resource crisis management** 

#### **Hamed Talebi**<sup>**1**</sup> **· Saeed Samadianfard**<sup>**1**</sup> 

Received: 13 May 2024 / Accepted: 30 July 2024 / Published online: 7 August 2024 © The Author(s), under exclusive licence to Springer-Verlag GmbH Germany, part of Springer Nature 2024 

#### **Abstract** 

A drought is a complex event characterized by low rainfall and has negative implications for agricultural and hydrological systems, as well as for community life. A common meteorological drought index used for drought monitoring and water resource management is the Standardized Precipitation Evapotranspiration Index (SPEI). Using SPEI can assist in predicting drought onset and estimating drought severity. The objective of this research is to assess the accuracy of machine learning models in estimating the SPEI-1 (one-month) index in semi-arid climates. To achieve this goal, the data will be analyzed using remote sensing parameters, a worldwide database, and meteorological station information. SPEI-1 was predicted in Tabriz, Iran, between 1990 and 2022 using multilayer perceptron (MLP) and random forest (RF) techniques combined with genetic algorithm (GA) methods. The parameters used are average air temperature, average relative humidity, monthly precipitation, wind speed, sunny hours, as well as the one-month standard precipitation index (SPI-1) (from ground data), daily precipitation products from satellites named PERSIANN (PRC-PR) (from remote sensing), and SPEIbase data (from global databases). The results suggest that the use of satellite remote sensing characteristics and global databases has significantly enhanced the precision and efficiency of prediction models. Based on the GA-RF model with an  R<sup>2</sup> of 0.992 and an RMSE of 0.124, it exhibits the best performance among all models in Scenario 1. By combining remote sensing parameters, this study presents an innovative approach to predicting the SPEI index and demonstrates their capabilities in drought management and mitigation. 

**Keywords** Standardized Precipitation Evapotranspiration Index · PERSIANN · Remote sensing · Global databases · Genetic algorithm 

## **Introduction** 

Drought is a severe and complex climatic phenomenon caused by deficient precipitation over an extended period, which then leads to soil moisture deficiency. Consequently, water sources are depleted and there is a shortage of water, resulting in adverse effects on the environment, food security, and water reserves (Getahun and Li 2023). It is estimated that over the last three decades, approximately 25 percent of humanity has experienced abnormal rainfall every year (Damania et al. 2017). Although future rainfall 

##### Communicated by Hassan Babaie. 

> * Saeed Samadianfard 

> s.samadian@tabrizu.ac.ir 

> 1 Department of Water Engineering, Faculty of Agriculture, University of Tabriz, Tabriz, Iran 

estimates are characterized by significant uncertainty, there is a widespread consensus that as temperatures increase, rainfall patterns will exhibit more volatility and intensity (Otto et al. 2023). In its most basic form, drought is a condition characterized by a lack of rainfall, which negatively impacts agricultural and hydrological systems as well as the lives of communities (Getahun and Li 2023; Salvador et al. 2020). Drought has subtle effects at first, but if precautions are not taken, these effects will become more severe and will last for a long time. Due to Iran's geographic location, drought is one of the most dangerous natural phenomena there, and the severity of drought is expected to increase across this region of the Asian continent, particularly in the second half of the twenty-first century (Ansari Amoli et al. 2022; Shayeghi et al. 2024). Drought has subtle and minimal effects at its onset; however, these effects tend to intensify significantly without proactive measures, and they tend to last for an extended 

Vol.:(0123456789) 

Earth Science Informatics (2024) 17:4949–4968 

4950 

period even after the drought has ended (Wilhite 2002). For modeling purposes, it can be beneficial to observe the gradual progression of drought to anticipate this event in advance (Cancelliere et al. 2007). The anticipation and mitigation of risks are integral components of sustainable development policy. Various modeling approaches have recently made it possible to gain insight into precipitation deficits, ultimately enhancing the capability of monitoring droughts. In virtually every climatic region, drought poses a pervasive threat to water and food security, as well as water consumption sectors, impacting livelihoods (Manatsa et al. 2010). The prevalence of drought in recent years has illustrated the vulnerability of affluent societies to this phenomenon, which has resulted in conflicts among water consumers. Global climate change is causing dry and semi-arid areas to have more frequent, intense, and widespread droughts. (Derdour et al. 2022). Unlike other natural disasters such as floods and landslides, drought affects a wide area and tends to persist for a relatively long time (Nafarzadegan et al. 2012). The four categories of droughts include meteorological, agricultural, hydrological, and socio-economic (Yuce et al. 2023). It is common to define meteorological drought in terms of the severity and duration of dry conditions. Meteorological droughts occur when precipitation is insufficient compared to the average conditions at a particular location during a particular period (Fotse et al. 2024). Meteorological droughts are monitored and quantified using different indicators. The Palmer Drought Severity Index (PDSI), the Standardized Precipitation Index (SPI), and the Standard Precipitation Evaporation Index (SPEI) are the most often used meteorological drought indexes (Balbo et al. 2019; Tirivarombo et al. 2018). It has been widely recognized as one of the most widely used drought indices for predictive purposes since Vicente-Serrano et al. (2010) introduced the SPEI. The SPEI differs from the SPI in that it incorporates both precipitation and potential evapotranspiration (PET) data in its calculation. Mousavi et al. (2023) conducted a study examining drought conditions in Southern Alberta, Canada. Their findings indicated that, overall, the SPEI performs better than the SPI in detecting drought conditions. A study by Wang et al. (2023) evaluated the effectiveness of the SPEI in capturing summer drought variations in China across various temporal scales. According to the results, the one-month SPEI (SPEI-1) reflected summer soil moisture (SM) variations better across different temporal scales. Considering the intricate calculation process involved in SPEI, it is evident that SPEI exhibits a stronger correlation with precipitation (P) than PET. According to the research conducted by Nwayor and Robeson (2023), both the SPEI and SPI indices demonstrate a positive correlation with each other globally. However, across all 

levels of aridity, ranging from humid regions to hyper-arid areas, a declining trend in correlation is observed. 

Precipitation is a crucial component of the hydrological cycle, serving a vital function in preserving the equilibrium of water and energy on Earth. Water resource management and natural disaster prevention are fundamentally dependent upon spatial–temporal patterns of precipitation (Correa et al. 2017). As a critical input for hydrological research and operational applications, precise, uninterrupted, and consistent observation of precipitation is essential. The scientific community continues to face significant challenges in determining precipitation intensity and duration, primarily due to spatial and temporal variations (Sorooshian et al. 2000). Three main instruments used for measuring precipitation are rain gauges, radars, and satellites. Precipitation is directly measured via rain gauges. However, most countries do not provide intermittent coverage of this technique. Many countries lack access to radar technology, and even in those countries that do have access, ground beam blockage presents a significant obstacle e to use (Yang et al. 2017). Furthermore, rain gauges and radars are unable to measure precipitation over oceans. For drought monitoring, watershed water balance, early flood warning, and soil moisture modeling, satellite precipitation products can serve as valuable inputs (Asadollah et al. 2024). Monitoring drought, with its complex spatial–temporal characteristics and severity, is a challenging task. Hence, it is important to maintain continuous monitoring and effective tactics at various geographic scales to support early warning systems and the development of solutions to alleviate the impact of drought. The use of remote sensing for drought research has increased significantly in recent years due to its advantages in terms of systematic measurements across different periods and locations, as well as its ability to cover a wide region. High-resolution satellite data may now be used to monitor real-time flood and drought management (Alvino and Marino 2017). Precipitation measurement has mostly been used to monitor drought indicators, with satellite remote sensing playing a crucial role in this aspect by using precipitation products (Kumar et al. 2024). The use of satellite-based products, similar to global weather models, can facilitate a more accurate representation of precipitation patterns by enhancing the spatial and temporal resolution of precipitation data (Ziveh et al. 2022). There are several types of satellite precipitation algorithms available, including those based on infrared thermal data (TIR), passive microwave data (PM), radar precipitation data (PR), surface rain gauge measurements (SM), and numerical weather prediction (NWP) (Mitra et al. 2018). Many satellite-based precipitation products have been produced using a combination of these techniques, including: microwave/infrared rainfall rate algorithm (MIRAA), Precipitation Estimation from Remotely Sensed Information using Artificial Neural Networks (PERSIANN) Climate 

Earth Science Informatics (2024) 17:4949–4968 

4951 

Hazards Group, and station-based infrared precipitation (CHIRPS) (Aksu et al. 2022). In a research conducted by Eini et al. (2023), the accuracy of two satellite-based datasets, PERSIANN-CDR and SM2RAIN-ASCAT, was tested for monthly precipitation estimates and drought monitoring in Poland and neighbouring countries. Based on the results, PERSIANN-CDR showed a higher degree of accuracy in precipitation estimation and was more effective in identifying agricultural and hydrological droughts than SM2RAINASCAT. The accuracy of PERSIANN-CDR, TRMM, and CHIRPS satellite precipitation products for precipitation estimation and drought detection in Iran from 1983 to 2017 was assessed by Kazemzadeh et al. (2022). The findings showed that, especially in arid and semi-arid regions, PERSIANN-CDR and TRMM performed better in drought event detection than CHIRPS. 

Lack of basic information is a major constraint on research in meteorology and drought in most developing countries. In areas where data exist, they often don't fully meet the informational needs of a study, either because they are short-term or because they are widely dispersed. Recently, several global research centers have developed networked systems that provide drought information worldwide with relatively adequate resolution. Following the creation of the SPEI, the scientific community received a new worldwide dataset known as SPEIbase. The SPEIbase is a vast repository of SPEI data gathered from more than 10,000 sites worldwide. This database is very helpful for climate scientists, hydrologists, and other researchers who are exploring the effects of climate change (Spinoni et al. 2019). 

Machine learning has recently captured the attention of academics for research in a variety of fields. One of the most prominent positive characteristics of machine learning in science is the high computational power and speed, as well as the ability to analyze large amounts of data. Despite the fact that drought is generally recognized as a nonlinear and unstable phenomenon (Hao et al. 2015), stochastic models for drought monitoring are unable to accurately capture these characteristics (Katipoğlu 2023b; Wei et al. 2012). A machine learning model, however, is capable of self-organizing and adapting to nonlinear features, enabling it to model and estimate meteorological and hydrological data for describing droughts. A great deal of research has been conducted in the field of predicting drought indicators using machine learning models (Achite et al. 2023a, b; Katipoğlu 2023a). 

Multilayer Perceptron Neural Network (MLPNN) was used by Ali et al. (2017) to predict drought. For seventeen climatic stations in the northern region of Pakistan, the MLPNN algorithm was applied and tested using monthly time series data of SPEI. MLPNN demonstrated potential capabilities in forecasting SPEI drought and enabling proactive water resource planning and management actions 

through its integration into decision-making processes. In their study, Mouatadid et al. (2018) employed Extreme Learning Machine (ELM), Multiple Linear Regression (MLR), Artificial Neural Network (ANN), and Least Squares Support Vector Regression (LSSVR) models to forecast SPEI in a drought-prone region in eastern Australia. The results indicated that ELM and ANN models outperformed MLR and LSSVR models in terms of performance. Dikshit et al. (2020) employed Multilayer perceptron (MLP) model and support vector regression (SVR) to forecast the SPEI drought index. To achieve this, they utilized 13 distinct variables, comprising 8 climate drivers and sea surface temperature indices, alongside various other meteorological variables. The findings indicated that the ANN model (R<sup>2</sup> = 0.86) outperformed SVR  (R<sup>2</sup> = 0.75) in predicting temporal drought trends. In other research, Barzkar et al. (2022) formulated the SPEI index for various climates using Gene Expression Programming (GEP), Model Tree (MT), and Multivariate Adaptive Regression Splines (MARS). The results of developing artificial intelligence models showed that the M5 MT version provides the most accurate SPEI prediction for all climatic conditions compared to GEP and MARS techniques. 

There are still a lot of unanswered questions about properly predicting droughts, even with extensive research on the subject especially in arid and semi-arid areas like Iran. Prior research has mostly focused on conventional meteorological data, frequently ignoring the advantages of incorporating data from remote sensing. In order to close these gaps, this study will forecast the SPEI index by utilizing meteorological and remote sensing data in conjunction with individual and hybrid machine learning models. By concentrating on Iran's semi-arid climate, this research will offer insightful information and increase the precision of drought forecasts, both of which are essential for efficient management of water resources in these vulnerable areas. 

Iran's primary natural hazard is drought. Iranian regions are characterized by arid and semiarid climates. For the management of water resources, the SPEI drought index must be forecasted. The innovation of this approach lies in combining remote sensing parameters with meteorological parameters to predict the SPEI index using both individual and hybrid machine learning models, making it unique in its own right. Therefore, for the years 1990 to 2022, in the semi-arid climate of Iran, specifically at the Tabriz station, the objectives of this research are as follows: 1- Comparing the accuracy of meteorological station input variables and remote sensing in estimating drought indices. 2- Investigating the accuracy of individual and hybrid machine learning models in predicting drought indices. 3- Estimating drought indices using limited meteorological station variables in semi-arid climates for water crisis management in areas lacking meteorological stations. 

Earth Science Informatics (2024) 17:4949–4968 

4952 

## **Materials and methods** 

### **Study area** 

Arid and semi-arid climates have increasingly scarce water resources, making secure management of water resources crucial for sustainable development (Khan et al. 2023). The current study utilized a climatic location covering Tabriz station to achieve this objective. Tabriz is situated in East Azerbaijan Province in northwest Iran. It lies between approximately 37.870 to 38.640 latitude and 48.850 to 

46.690 longitude, covering an area of 1781  km<sup>2</sup> . According to the De Martonn climate classification method, Tabriz experiences a semi-arid climate (Talebi et al. 2023b). The annual precipitation in Tabriz is approximately 286 mm, with dry and semi-warm summers and mild and moderate springs. The average annual temperature is estimated to be around 13 °C. From a topographic perspective, the northern and southern regions of Tabriz feature elevated points, while its center has relatively low elevation, with the highest point reaching 3633 m and the lowest point at 1280 m (Fig. 1). 



**Fig. 1** The geographical position of the research site (Digital Elevation Model—DEM) and the De Martonne climate classification method for Iran 

Earth Science Informatics (2024) 17:4949–4968 

4953 

### **Methodology of the study** 

In the first step, using meteorological station data, SPEI-1 values were calculated using the Hargreaves-Samani method and employed as the baseline. Subsequently, to investigate SPEI-1 within the studied time interval, an analysis of the SPEI-1 drought index was conducted for the semi-arid climate for the years 1990–2022. For the years 1990 to 2022, a variety of input variables from three types of data sources were utilized to estimate the one-month SPEI-1 in a semi-arid climate. The second 

step involved gathering all the meteorological and remote sensing parameters utilized in the research, and, ultimately, evaluating the capabilities of machine learning models in estimating SPEI-1 for Tabriz station using various scenarios. A diagram of the different stages of the study is shown in Fig. 2. 

### **Data sources** 

To estimate the SPEI-1 drought index, three different types of data sources have been utilized: ground-based data, 



**Fig. 2** Flowchart of SPEI estimation method in semi-arid climate (Tabriz station) 

Earth Science Informatics (2024) 17:4949–4968 

4954 

satellite remote sensing data, and global databases, each of which will be further elaborated on below. 

#### **Ground‑based data** 

In the terrestrial data section, parameters including mean air temperature (Tm), average relative humidity (RHm), monthly precipitation (PRC), average wind speed (U2), sunshine hours (n), and also the Standardized Precipitation Index for one month (SPI-1) have been utilized. These parameters were obtained from the National Meteorological Organization for the studied stations. The calculation method of the SPI-1 index is explained subsequently. 

decision-making within short time intervals (1 h to 2 days). PERSIANN-CDR provides quasi-global daily precipitation coverage from January 1, 1983, to the present. Considering the desired time period, PERSIANN-CDR precipitation products were obtained from the Google Earth Engine platform (https:// earth engine. google. com/), and after preprocessing the data, they were used in the modelling process (Additionally, access to PERSIANN products can be obtained through the following link: https:// chrsd ata. eng. uci. edu/). Table 1 illustrates the spatial and temporal resolution and coverage of PERSIANN precipitation products (Ashouri et al. 2015). 

#### **Global database** 

**Standardized precipitation index** SPI is a drought index that relies solely on precipitation as a variable. SPI is currently widely used on a global level for drought monitoring and analysis (McKee et al. 1993). Using the SPEI package in R, all of these steps were performed (Beguería et al. 2017). 

In the Global Data section, SPEIbase data has been utilized for drought modelling. This diversity in data sources enhances the accuracy and predictive power of the model, providing a comprehensive analysis of drought conditions across different periods. 

#### **Remote sensing data** 

In the remote sensing data sources portion, we used the satellite-derived daily precipitation product called PERSIANN. Subsequently, we transformed this data into a monthly version. 

**Satellite precipitation data from PERSIANN** The Center for Hydrometeorology and Remote Sensing at the University of California, Irvine, has been working with NASA, NOAA, and UNESCO's Global Network of Drylands Research to produce the PERSIANN precipitation product suite over the last twenty years. The PERSIANN family comprises three satellite-based precipitation estimation products referred to as PERSIANN, PERSIANN-CCS, PERSIANN-CDR, PDIR _-_ Now, and PERSIANN _-_ CCS _-_ CDR. Various web-based interfaces allow researchers, experts, and the general public to access the products. In various fields including hydrology, water resource management, and climate studies, researchers have repeatedly utilized PERSIANN products. Several applications of PERSIANN products include modelling soil moisture, predicting runoff, analyzing precipitation patterns, monitoring droughts, forecasting rainfall, and analyzing trends (Nguyen et al. 2018). Climate dataset PERSIANN-CDR covers approximately 35 years, which is suitable for examining statistical trends in meteorological phenomena and frequency analysis. PERSIANN and PERSIANN-CCS, on the other hand, are designed to support 

**SPEIbase** The development of the SPEI index has enabled the scientific community to access a novel global dataset known as SPEIbase. The monthly precipitation and temperature data from the Climatic Research Unit gridded time series (CRU TS) were utilized in the development of the SPEIbase dataset. These are the most exhaustive and current gridded data available on account of their comprehensive and current nature (Vicente ‐ Serrano et al. 2023). The CRU TS dataset provides a monthly, high-resolution grid of land observations (excluding the South Pole) dating back to 1901. There are no missing values within the defined range. The CRU TS dataset was first published in 2000 and interpolated monthly observation anomalies onto a 0.5-degree grid on Earth's surfaces (excluding the South Pole) using Angular-distance weighting (ADW). CRU TS has been widely utilized in research and application domains since its first publication in 2000 (Harris et al. 2020). This extensively utilized dataset has been made available at https:// spei. csic. es/ spei- datab ase for drought research. The dataset includes monthly SPEI values on time scales ranging from 1 to 48 months. Since the aim of this research is to estimate one-month SPEI, monthly data was utilized. The SPEIbase database is based on the FAO56-Penman–Monteith method for estimating potential evapotranspiration (PET), which outperforms the Thornthwaite method (Potop et al. 2014). 

|**Table 1**Coverage and<br>spatio-temporal separation|Product|temporal resolution|Spatial resolution|Time coverage|Spatial coverage|
|---|---|---|---|---|---|
|of PERSIANN satellite<br>|PERSIANN|30 min|0.25 degree|2000- present|60°N-60°S|
|precipitation products|PERSIANN-CCS|30 min|0.04 degree|2003- present||
||PERSIANN-CDR|1–2 day|0.25 degree|1983- present||



Earth Science Informatics (2024) 17:4949–4968 

4955 

**Fig. 3** GA algorithm flowchart 



### **Calculation of SPEI drought index** 

Calculating the SPEI is nearly analogous to the SPI, with the distinction that, in addition to precipitation, temperature also plays a role through the utilization of the PET parameter. Several models are available for calculating PET, which can be classified according to mass transfer, temperature, radiation, and combined models (Al-Hasani and Shahid 2022). There are several different types of models used in the field of mass transfer. These include the Ivanov model, which focuses on mass transfer, the Thornthwaite and Hargreaves-Samani models, which are focused on temperature, the Priestley and Taylor models, which rely on radiation, and the Penman—Monteith model, which combines multiple factors (Ortiz-Gómez et al. 2022). In order to calculate PET, the Hargreaves, Thornthwaite, and Penman–Monteith methods are commonly employed. PET was calculated using the Hargreaves-Samani method in this study. Below is a detailed explanation of how to calculate the SPEI. Following is a description of how SPEI is calculated. As a first step, differences between precipitation (Pi) and potential evapotranspiration (PETi) for a month i (Di) were calculated and aggregated at various time scales  (D<sup>k</sup> ). 



k is the number of months or the interest time scale, and n is the month in which the calculation is performed. 

Thus, SPEI is used to describe the probability of occurrence of a given event based on three parameters of the logistic probability distribution function. The cumulative probability function consists of the following three parameters. It is important to note that the parameters α, β, and λ represent the scale, shape, and origin, respectively. In order to determine the logistics distribution parameters, a different approach can be used. An L-moment method is one of the most powerful and convenient methods available for calculating the cumulative function coefficient of the above relationship. 





Earth Science Informatics (2024) 17:4949–4968 

4956 



The probability-weighted moments are _휔_ 0 , _휔_ 1 , and _휔_ 2 , and the Gamma function is Г (β). Here, we provide the probability distribution function of the  D<sup>k</sup> series using the loglogistic distribution. 



As a final step, the obtained F(x) values are converted into corresponding Z-standardized average values in order to calculate SPEI. Using the SPEI package in R, all of these steps were performed (Beguería et al. 2017). 

### **Genetic algorithm** 

In 1992, Holland introduced the Genetic Algorithm (GA) (Fig. 3) for the first time (Holland 1992). The method is derived from Darwin's theory of evolution and is regarded as a classical meta-heuristic algorithm. However, it is one of the most effective methods for addressing optimization issues (Talebi and Samadianfard 2023). Generally, a GA comprises a population where each component, called a chromosome, represents a solution to a given problem. In this algorithm, the search process commences by generating a random population. Through selection, crossover, and mutation, subsequent generations of this population are expanded. The population undergoes evolutionary changes from one generation to the next based on the concept of natural selection favoring individuals with the highest fitness. Just like in natural evolution, this strategy resulted in the next generation being better adapted to its environment than the previous generation. As a result, an almost perfect solution to the problem can be found within the population of the final generation (Mirjalili et al. 2020). This study used GAs to identify the most advantageous point for complex nonlinear functions when combined with MLP and RF. 

### **Multilayer perceptron optimized with genetic algorithm** 

There is no doubt that neural networks (NNs) are the most popular machine learning models, used across a wide range of applications (Qi et al. 2019). Artificial Neural Networks (ANNs) are a fundamental type of neural network that leverages the architecture of the human brain to tackle intricate problem-solving challenges. ANNs are composed of three 

layers: the input layer, one or more hidden layers, and the output layer. Layers are interconnected through processing elements called neurons. Neurons in the hidden layer are assigned weights based on the strength of their connections to the input variables in the input layer. ANNs employ two distinct learning processes: supervised learning and unsupervised learning. In supervised learning, the anticipated output is evaluated by comparing it with the known output to gain knowledge. Unsupervised learning does not require relevant output knowledge for comparison and learning. A Multilayer Perceptron (MLP) is the most commonly used type of ANN for supervised learning and is widely used to model complex nonlinear processes, such as drought (Ghasemi et al. 2021). MLP is a type of Feedforward Neural Network (FFNN) that is composed of one or more hidden layers. Data transmission in the neural network occurs exclusively 



**Fig. 4** GA-MLP algorithm flowchart 

Earth Science Informatics (2024) 17:4949–4968 

4957 



**Fig. 5** GA-RF algorithm flowchart 

in the forward direction, from the input nodes to the hidden nodes and finally to the output nodes. An activation function (or transfer function) that is non-linear is used in the calculations (Senthilkumar 2010). An activation function in a multilayer neural network determines whether a node is active or inactive. A genetic algorithm is used to optimize the weights and bias values of an artificial neural network. The genetic algorithm's objective function is established by the outcomes of the MLP. (Ecer et al. 2020). The error rate was calculated using training data by randomly inserting a population of size P in each iteration of the MLP. After analyzing the input and output values, the subsequent action was modifying the network properties. The algorithm's training process was repeated till the network features improved, considering the recently developed population. The model execution was finished by minimizing the discrepancy between the outputs acquired via network execution and the real values. The multilayer perceptron architecture optimized by genetic algorithms is shown in Fig. 4. 

**Table 2** Statistical characteristics of input parameters 

|Parameters|Unit|Max|Min|Mean|Std. Deviation|
|---|---|---|---|---|---|
|SPEI-1|-|2.331|-2.246|0.011|0.977|
|SPI-1|-|2.444|-4.437|-0.068|1.119|
|SPEIbase|-|2.420|-2.490|-0.185|1.021|
|PRC|mm|114.84|0.000|21.073|20.549|
|PRC-PE|mm|177.313|0.000|40.228|26.818|
|RHm|%|81.072|21.995|50.930|14.582|
|n|hr|5.761|0.258|3.109|1.372|
|U2|m.s<sup>−1</sup>|5.693|0.782|3.309|0.982|
|Tm|°C|30.290|-6.452|13.111|9.953|



### **Random forest optimized with genetic algorithm** 

Breiman (2001) was the first to propose the Random Forest (RF) algorithm (Fawagreh et al. 2014). RF is a machine learning algorithm that is based on decision trees. RF can be applied to both classification and regression tasks due to its simplicity and versatility. A decision tree is fitted to various subsets of training data. The advantage of RF is that it can estimate the importance of each input variable. The RF algorithm utilizes many input variables that may contribute to estimation (Tyralis et al. 2019). Optimization with the genetic algorithm primarily consists of two components: parameter tuning and optimization of the Random Forest method. The initial section identifies the random forest settings, including the forest scale, the number of features used for splitting, and the maximum depth of the decision trees. In the optimization part of the Random Forest utilizing the genetic algorithm, the goal is to maximize the profit score by optimizing the combination of decision trees. This is done by considering both actual and projected returns and losses (Ye et al. 2018). Figure 5 illustrates the overall view of the optimized Random Forest with the genetic algorithm. In this research, we utilized Python for data preprocessing, model training, and evaluation. Scikit-learn was used for implementing Random Forest (RF) algorithms, TensorFlow/Keras for Multilayer Perceptron (MLP) neural networks, and NumPy and Pandas for data manipulation and handling. 

### **Evaluation criteria** 

The models' performance was assessed using traditional statistical evaluation methods. As part of this procedure, 

Earth Science Informatics (2024) 17:4949–4968 

4958 

four important metrics were calculated: Willmott's index of agreement (WI) (Eq. 8), root mean square error (RMSE) 

(Eq. 9), coefficient of determination  (R<sup>2</sup> ) (Eq. 10), and Nash–Sutcliffe efficiency (NS) (Eq. 11). 





<!-- Start of picture text -->
√√ N<br>√ 1<br>RMSE = N ∑ (SPEIi(observed) − SPEIi(model)) 2 (9)<br>√ i=1<br>∑Ni=1 (SPEIi(observed) − SPEIi(model))<br>R 2 = 1 −<br>(10)<br>∑ Ni=1 (SPEIi(observed) − SPEImean)<br>NS = 1 − ⎡⎢ ∑Ni=1 (SPEIi(observed) − SPEIi(model))2 ⎤⎥ (11)<br>⎢⎣ ∑ Ni=1 (SPEIi(observed) − SPEIi(observed))2 ⎥⎦<br><!-- End of picture text -->

The variable N denotes the quantity of observed Standardized Precipitation-Evapotranspiration Index (SPEI). The observed SPEI is denoted as  SPEIi(observed), whereas the estimated SPEI is denoted as  SPEIi(model). Additionally, the average value of the observed SPEI is represented as SPEImean (Talebi et al. 2023a, b, c). 

## **Results and discussion** 

The present study evaluates the effectiveness of machine learning models in predicting the one-month Standardized Precipitation Evapotranspiration Index (SPEI-1) for semiarid climates, specifically in Tabriz, Iran. Table 2 displays the statistical properties of the parameters utilized in forecasting SPEI at the Tabriz stations, encompassing the maximum (Max), minimum (Min), mean, and standard deviation (Std. Deviation). The SPEI-1 values vary between a maximum of 2.331 and a minimum of -2.246. The average value is 0.011, and the standard deviation is 0.977. This indicates moderate variability in the short-term drought conditions. The maximum value for SPI-1 is 2.444, while the minimum value is -4.437. The mean value is -0.068, and the standard deviation is 1.119. This suggests significant variability in precipitation conditions affecting drought severity. The SPEIbase dataset has a maximum value of 2.420 and a lowest value of -2.490. The dataset's mean is -0.185, 

**Table 3** The Pearson correlation coefficient between the target variable and input parameters in Tabriz 

|Input parameter<br>SP|I<br>SPE|Ibase|PRC|PRC-PE|RHm|n|U2|Tm|
|---|---|---|---|---|---|---|---|---|
|Correlation coefficient<br>0.|830<br>0.79|8|0.641|0.390|0.262|0.223|-0.106|-0.083|
|**Table 4**Combination of input<br>parameters|Scenario|Input p|arameters||||||
||1|SPI|SPEIbase|PRC|PRC-PE|RHm|n<br>U2|Tm|
||2|SPI|SPEIbase|PRC|PRC-PE|RHm|n<br>U2||
||3|SPI|SPEIbase|PRC|PRC-PE|RHm|n||
||4|SPI|SPEIbase|PRC|PRC-PE|RHm|||
||5|SPI|SPEIbase|PRC|PRC-PE||||
||6|SPI|SPEIbase|PRC|||||
||7|SPI|SPEIbase||||||
||8|SPI|||||||



Earth Science Informatics (2024) 17:4949–4968 

4959 

and the standard deviation is 1.021. The observed precipitation levels range from 114.84 mm to 0.000 mm, with an average of 21.073 mm and a standard deviation of 20.549 mm. The PRC-PE measurements vary from 177.313 mm to 0.000 mm, with an average of 40.228 mm and a standard deviation of 26.818 mm. This variability underscores the unpredictability of precipitation patterns crucial for water supply. The range of relative humidity values is between 81.072% and 21.995%, with an average of 50.930% and a standard deviation of 14.582%. The duration of sunshine ranges from 5.761 h to 0.258 h, with an average of 3.109 h and a standard deviation of 1.372 h. The wind speed ranges from 5.693 m/s to 0.782 m/s, with an average of 3.309 m/s and a standard deviation of 0.982 m/s. The temperature varies between 30.290 °C and -6.452 °C, with an average of 13.111 °C and a standard deviation of 9.953 °C. Temperature variations impact water demand, snowmelt patterns, and overall climatic conditions affecting water resources. 

These parameters collectively illustrate the dynamic nature of climatic variables influencing water availability 

and drought conditions in Tabriz, Iran. The wide ranges and significant standard deviations across SPEI, precipitation, humidity, sunshine duration, wind speed, and temperature underscore the complexity of managing water resources in semi-arid climates. Understanding these fluctuations is crucial for implementing adaptive water management strategies that can respond effectively to variable climatic conditions and ensure sustainable water use in the region. 

To provide accurate estimates for SPEI, various parameters from meteorological stations, remote sensing data, and a global database were combined. The Pearson correlation coefficient with the target variable (SPEI) established the ideal combination of these characteristics for input to machine learning models. In Table 3, all parameters except for  U2 and  Tm are positively correlated with SPEI at the semi-arid station. As a result of the parameters considered, SPI (0.830) is the one with the highest correlation, while  Tm (-0.083) is the one with the lowest correlation. Due to the data input pattern, all parameters were used in the prediction of SPEI in the first scenario. According to the second 

**Table 5** Model parameters for RF and GA-RF 

|Model|Paramet|er|||||||
|---|---|---|---|---|---|---|---|---|
||a|b|c|d|e|f|g|h|
|GA-RF-1|78|65|0.148|98|13|68|0.245|37|
|GA-RF-2|94|86|0.281|41|20|3|0.302|64|
|GA-RF-3|78|65|0.167|98|13|68|0.254|37|
|GA-RF-4|81|65|0.221|1|80|55|0.254|37|
|GA-RF-5|81|65|0.221|1|80|55|0.245|37|
|GA-RF-6|81|36|0.284|1|80|55|0.291|64|
|GA-RF-7|81|36|0.221|1|80|55|0.308|64|
|GA-RF-8|81|65|0.181|1|80|55|0.243|37|
|RF|100|10|0.100|2|4|3|0.200|42|



a: Random Forest.number_of_trees, b: Random Forest.maximal_depth, c: Random Forest.confidence, d: Random Forest.minimal_leaf_size, e: Random Forest.minimal_size_for_split, f: Random Forest.number_ of_prepruning_alternatives, g: Random Forest.subset_ratio, h: Random Forest.local_random_seed 

**Table 6** Model parameters for MLP and GA-MLP 

|Model|Parameter|||||
|---|---|---|---|---|---|
||(a)NN.train_<br>cycles|NN.learn_rate|NN.momentum|NN.err_epsilon|NN.<br>random_<br>seed|
|GA-MLP-1|96|0.488|0.681|(b)Inf|74|
|GA-MLP-2|57|0.916|0.304|Inf|64|
|GA-MLP-3|57|0.916|0.304|Inf|64|
|GA-MLP-4|96|0.713|0.681|Inf|9|
|GA-MLP-5|57|0.72|0.304|Inf|1|
|GA-MLP-6|87|0.72|0.631|Inf|1|
|GA-MLP-7|87|0.72|0.631|Inf|82|
|GA-MLP-8|57|0.916|0.304|Inf|1|
|MLP|200|0.010|0.900|0.0001|1992|



(a) Neural Net, (b) Infinity 

Earth Science Informatics (2024) 17:4949–4968 

4960 

**Table 7** Results of training and testing MLP and RF models 

|Model|Train (19|91–2012)|||Test (201|3–2022)|||
|---|---|---|---|---|---|---|---|---|
||R<sup>2</sup>|RMSE|NS|WI|R<sup>2</sup>|RMSE|NS|WI|
|MLP-1|0.936|0.341|0.873|0.965|0.935|0.456|0.800|0.947|
|MLP-2|0.940|0.330|0.881|0.969|0.933|0.468|0.861|0.961|
|MLP-3|0.943|0.326|0.884|0.969|0.936|0.380|0.790|0.947|
|MLP-4|0.936|0.338|0.875|0.966|0.923|0.417|0.833|0.953|
|MLP-5|0.935|0.344|0.871|0.964|0.923|0.426|0.826|0.953|
|MLP-6|0.931|0.352|0.864|0.964|0.935|0.805|0.752|0.931|
|MLP-7|0.922|0.406|0.820|0.954|0.935|0.463|0.794|0.943|
|MLP-8|0.881|0.456|0.773|0.934|0.901|0.513|0.747|0.926|
|RF-1|0.989|0.146|0.977|0.994|0.941|0.398|0.848|0.955|
|RF-2|0.988|0.157|0.973|0.993|0.944|0.392|0.852|0.956|
|RF-3|0.988|0.154|0.974|0.993|0.946|0.384|0.858|0.959|
|RF-4|0.987|0.158|0.973|0.993|0.943|0.387|0.856|0.958|
|RF-5|0.987|0.161|0.972|0.993|0.935|0.409|0.839|0.955|
|RF-6|0.986|0.165|0.970|0.992|0.936|0.411|0.837|0.954|
|RF-7|0.982|0.185|0.962|0.990|0.913|0.464|0.793|0.942|
|RF-8|0.957|0.281|0.914|0.977|0.874|0.560|0.699|0.912|



**Table 8** Results of training and testing GA-RF and GA-MLP hybrid models 

|Model|Train (19|91–2012)|||Test (201|3–2022)|||
|---|---|---|---|---|---|---|---|---|
||R<sup>2</sup>|RMSE|NS|WI|R<sup>2</sup>|RMSE|NS|WI|
|GA-MLP-1|0.934|0.343|0.872|0.964|0.928|0.414|0.835|0.946|
|GA-MLP-2|0.924|0.366|0.854|0.959|0.924|0.397|0.849|0.957|
|GA-MLP-3|0.926|0.363|0.856|0.960|0.928|0.389|0.854|0.957|
|GA-MLP-4|0.922|0.38|0.843|0.957|0.925|0.399|0.847|0.958|
|GA-MLP-5|0.915|0.397|0.828|0.952|0.923|0.402|0.844|0.953|
|GA-MLP-6|0.922|0.372|0.829|0.958|0.917|0.415|0.835|0.954|
|GA-MLP-7|0.911|0.395|0.830|0.952|0.889|0.476|0.872|0.930|
|GA-MLP-8|0.877|0.460|0.769|0.931|0.839|0.578|0.679|0.890|
|GA-RF-1|0.992|0.124|0.983|0.996|0.945|0.385|0.858|0.958|
|GA-RF-2|0.992|0.128|0.982|0.995|0.945|0.384|0.858|0.957|
|GA-RF-3|0.992|0.128|0.982|0.995|0.945|0.380|0.861|0.959|
|GA-RF-4|0.992|0.129|0.982|0.995|0.944|0.381|0.861|0.960|
|GA-RF-5|0.991|0.137|0.979|0.995|0.939|0.396|0.849|0.957|
|GA-RF-6|0.990|0.138|0.979|0.995|0.937|0.406|0.842|0.956|
|GA-RF-7|0.988|0.150|0.975|0.994|0.931|0.434|0.819|0.949|
|GA-RF-8|0.969|0.241|0.937|0.983|0.907|0.495|0.765|0.932|



scenario, the parameter with the lowest correlation coefficient with the target variable was removed from the model, which resulted in one fewer parameter being considered. The process continues in this manner until the eighth scenario (last scenario) is reached. As a result of the last scenario, there is only one input parameter that has the highest correlation coefficient with SPEI. Table 3 provides the Pearson correlation between the input parameters and the target variable. Table 4 presents the input parameters for each scenario. 

The RF and GA-RF models' parameters are shown in Table 5. The parameters include the number of trees, maximal 

depth, confidence, minimal leaf size, minimal size for split, number of preparing alternatives, subset ratio, and local random seed. In contrast to the standalone RF model, which has constant parameters for every scenario, the GA-optimized hybrid model's RF model parameters vary depending on the scenario (Nourani et al. 2022). Table 6 details the parameters for the MLP and GA-MLP models. These parameters include the number of training cycles, learning rate, momentum, error epsilon, and random seed. While the parameters for the GAMLP models vary across different scenarios, the parameters for the standalone MLP model are fixed. 

Earth Science Informatics (2024) 17:4949–4968 

4961 



**Fig. 6** Taylor diagram for the training phase of MLP (a), RF (b), GA-MLP (c), and GA-RF (d) 



**Fig. 7** Taylor diagram for the testing phase of MLP (a), RF (b), GA-MLP (c), and GA-RF (d) 

Earth Science Informatics (2024) 17:4949–4968 

4962 

Table 7 illustrates the accuracy of the MLP and RF models for estimating one-month SPEI at Tabriz station. According to Table 7, in most scenarios, training is more effective than testing. For the MLP model, the  R<sup>2</sup> , RMSE, NS, and WI values in the training phase were 0.943–0.881, 0.456–0.326, 0.884–0.773, and 0.969–0.934, respectively. During the testing phase of the MLP model, the statistical parameters fall within the ranges of 0.936–0.901, 0.805–0.380, 0.861–0.747, and 0.961–0.926. The  R<sup>2</sup> , RMSE, NS, and WI values for the RF model in the training phase were 0.989–0.957, 0.281–0.146, 0.977–0.914, and 0.994–0.977, respectively. In the testing phase of the RF model, these statistical parameters range between 0.946–0.874, 0.560–0.384, 0.858–0.699, and 0.959–0.912. Table 8 presents the results and performance of the hybrid MLP and RF model optimized using the GA algorithm. During the training phase, the  R<sup>2</sup> , RMSE, NS, and WI ranges for the GA-MLP model are 0.934–0.877, 0.460–0.343, 0.872–0.769, and 0.964–0.931, respectively. During the testing phase, these values are 0.928–0.839, 0.578–0.389, 0.872–0.679, and 0.958–0.890. The  R<sup>2</sup> , RMSE, NS, and WI values for the GA-RF model 

in the training phase were 0.992–0.969, 0.241–0.124, 0.983–0.937, and 0.996–0.983, respectively. In the testing phase of the RF model, these statistical parameters range between 0.945–0.907, 0.495–0.380, 0.861–0.765, and 0.960–0.932. 

The drought estimation results in the training (Fig. 6) and testing (Fig. 7) phase were analyzed using the Taylor diagram for each model. We construct the Taylor diagram by using the geometric correlation between R, standard deviation, and RMSE. It is possible to identify the optimal combination of parameters for a given task and compare the performance of various algorithms using the Taylor diagram. It illustrates the tradeoff between accuracy and efficiency (Taylor 2001). As shown in Fig. 6, Scenario 8 with a single input parameter (SPI) exhibits the poorest performance in all models during the training phase. According to the findings, when using six input factors, the MLP model demonstrates higher accuracy in Scenario 3. Conversely, the RF, GA-MLP, and GA-RF models exhibit optimal performance in Scenario 1 when utilizing all input parameters. Le et al. (2016) used an MLP together with meteorological factors to forecast the SPEI. The findings demonstrated that the 



**Fig. 8** Scatter plot for all scenarios in the training phase 

Earth Science Informatics (2024) 17:4949–4968 

4963 



**Fig. 9** Scatter plot for all scenarios in the testing phase 

**Fig. 10** The Notched Boxplot diagram estimating SPEI-1 for MLP and GA-MLP models for all scenarios at Tabriz station 



Earth Science Informatics (2024) 17:4949–4968 

4964 

**Fig. 11** The Notched Boxplot diagram estimating SPEI-1 for RF and GA-RF models for all scenarios at Tabriz station 



inclusion of meteorological factors increased estimation accuracy. Testing results differ slightly from training results. In the testing phase, similar to the training phase, all models exhibited the weakest performance in Scenario 8. However, the highest performance for each model was observed in Scenario 3 (although with very slight differences). 

In order to assess the accuracy of all four models in predicting SPEI at the Tabriz station across 8 scenarios, scatter plots were utilized both during the training period (Fig. 8) and the testing phase (Fig. 9), each separately. When comparing the scatter plot results throughout the training period, the GA-RF model demonstrated the closest distribution to the 1:1 line in all scenarios. In comparison to the two MLP and GA-MLP models, the MLP model displayed a distribution that was closer to the 1:1 line in all scenarios. During the testing phase, except for scenario 3 and 7, the GA-RF model outperformed the other models and exhibited similar performance to the training phase across the remaining scenarios. In scenario 3, the RF model and in scenario 7, the MLP model showed better performance with  R<sup>2</sup> values of 0.944 and 0.935 respectively compared to the GA-RF model. In scenario 5, the scatter of points around the 1:1 line for 

both MLP and GA-MLP models is similar, with both having an  R<sup>2</sup> value of 0.923. In the remaining scenarios, the MLP model performed better than the GA-MLP model, resembling its performance during the training phase. 

During the testing phase, Notched Boxplot diagrams were used to assess the accuracy of the individual RF and MLP models, as well as the combined models (Fig. 10 and Fig. 11). Notched Boxplots are basically box plots, but their median region is modified in a brief way, in the shape of a notch (McGill et al. 1978). The notches in the boxes indicate an approximate 95% confidence interval for the medians. The hollow circle represents the mean, while the diamond-shaped symbols indicate outliers. Outliers are data points that fall below the minimum or exceed the maximum. Furthermore, in all scenarios, individual models are represented with hatching, while combined models are displayed as solid colors. In both models, similar scenarios are depicted in similar colors. The SPEI-1 value generated from the data is shown in black to facilitate accurate visual examination. Based on Fig. 10, there are no outliers in any of the MLP model scenarios, while outliers are only observed in the combined GA-MLP model. 

**Table 9** The average statistical parameters of machine learning models across all scenarios examined throughout the training and testing periods 

|Model|Train||||Test||||
|---|---|---|---|---|---|---|---|---|
||R<sup>2</sup>|RMSE|NS|WI|R<sup>2</sup>|RMSE|NS|WI|
|MLP|0.928|0.362|0.855|0.961|0.928|0.491|0.800|0.945|
|RF|0.983|0.176|0.964|0.991|0.929|0.426|0.823|0.949|
|GA-MLP|0.916|0.385|0.835|0.954|0.909|0.434|0.827|0.943|
|GA-RF|0.988|0.147|0.975|0.994|0.937|0.408|0.839|0.954|



Earth Science Informatics (2024) 17:4949–4968 

4965 

Using a boxplot comparison between MLP and GA-MLP models across eight scenarios, the results indicate that the MLP model is more compatible with SPEI observations in scenarios 1, 2, and 3. All scenarios except scenario 2 show significant differences in the MLP and GA-MLP models. The results indicate that in the experimental phase, the MLP model demonstrates better uniformity compared to the GA-MLP model in most scenarios. As shown in Fig. 11, at the Tabriz station, there are no outliers in either the RF or GA-RF models. In analyzing the results of Fig. 11 for both RF and GA-RF models, it is observed that in scenarios 1, 2, and 3 with a large number of input parameters, there is not much difference in the accuracy of both models with observational SPEI. However, in scenarios 7 and 8 (with two and one input parameters, respectively), the combined GA-RF model demonstrates greater compatibility with observational SPEI. Additionally, for both models, it is observed that the lower and upper bounds lines of the boxplots are noticeably short and restricted. This indicates the limited distribution of the data in these scenarios. The interquartile ranges in the boxplots for most scenarios are remarkably consistent and uniform in size. This indicates a higher compatibility of the SPEI estimation models with observational values. The average statistical results for each of the four models are shown in Table 9 for scenarios 1 to 8 during the testing and training phases. According to the findings, the GA-RF model outperformed the other models in the training phase, demonstrating the highest  R<sup>2</sup> (0.988), NS (0.975), and WI (0.994) values, along with the lowest RMSE (0.147). In addition, the GA-MLP model showed the lowest  R<sup>2</sup> (0.916), NS (0.835), and WI (0.954) values, along with the highest RMSE (0.385), as compared to other models during the training phase. In the testing phase as well, the GA-RF model exhibits superior performance compared to other models, mirroring its performance in the training phase. According to these results, the incorporation of the GA algorithm into the RF model has improved its performance compared to its standalone configuration. Conversely, the standalone MLP model outperforms the hybrid GA-MLP model, indicating a reversal of the aforementioned trend. Elbeltagi et al. (2023) use machine learning methods to forecast climatic droughts in central Maharashtra, India. The authors constructed models using historical data from the SPI via the use of RF, random trees, and Gaussian process regression approaches. The findings indicated that the RF model exhibited the highest level of accuracy in predicting droughts, therefore establishing its potential as a reliable drought warning approach, which aligns with the outcomes of this investigation. Danandeh Mehr et al. (2022) used the GA-RF model to simulate and forecast multi-temporal drought indicators (SPEI-3 and SPEI-6) at two meteorological stations (Beypazari and Nallihan) located in Ankara, 

Turkey. This study included a comparison of the outcomes obtained via traditional RF, Extreme Learning Machine (ELM), and an optimized combined ELM model known as Bat-ELM. Achite et al. (2023a, b) conducted a study in which the prediction of the standardized runoff index was performed using simple ELMs and wavelet-based extreme learning machines (W-ELMs). Despite the results demonstrating that both algorithms accurately predict hydrological droughts, the hybrid model (W-ELM) has maintained a superior performance at most hydrological stations with R<sup>2</sup> = 0.74 and RMSE = 0.36. Although it was consistent with the results of this research, the results of the current research are better than that. The prediction results demonstrated that GA-RF surpasses the performance of benchmark models, which is consistent with the conclusions of this research. 

## **Conclusion** 

An investigation of the accuracy of estimating the Standardized Precipitation Evapotranspiration Index (SPEI) in a semiarid climate was conducted at the Tabriz station in this study. To estimate the one-month SPEI-1 for the semi-arid climate for the time period of 1990 to 2022, a variety of input variables from three data sources were used. Training phase data spanned from 1990 to 2021 (70%), while testing phase data spanned from 2013 to 2022 (30%). Three types of data sources have been utilized to estimate the SPEI-1 drought index: ground-based data, satellite remote sensing data, and global databases. The terrestrial data section includes parameters such as mean air temperature (Tm), relative humidity (RHm), monthly precipitation (PRC), wind speed (U2), sunshine hours (n), and Standardized Precipitation Index (SPI-1). Remote sensing data sources were converted into monthly format from PERSIANN (PRC-PE), a satellite-derived daily precipitation product. Global Data used SPEIbase data to model drought. The machine learning models utilized for estimating SPEI-1 include: random forest (RF), multilayer perceptron (MLP), GA-RF, and GA-MLP are genetic algorithm-optimized hybrid models of these two. Based on the correlation between predictor parameters and SPEI, eight scenarios were defined as follows: the first scenario includes all parameters, while the last scenario consists of only one parameter with the highest correlation with SPEI. 

1. The lowest correlation coefficient (-0.083) is associated with mean air temperature (Tm), indicating a weak negative relationship with SPEI. Meanwhile, the highest positive correlation is observed with SPI (0.830), signifying a strong association with SPEI. Additionally, SPEIbase shows a notable positive correlation (0.798), 

Earth Science Informatics (2024) 17:4949–4968 

4966 

while PRC-PE and PRC exhibit positive correlations (0.390 and 0.641, respectively) with SPEI. 

2. In both the training and testing phases, the models demonstrated the best performance with the parameters of the first scenario (all parameters) and the weakest performance with the parameter of the last scenario (SPI-1). 

3. The hybrid GA-RF model outperformed the RF model, while the MLP model yielded better results in most scenarios compared to the hybrid GA-MLP model. 

4. In all scenarios, the hybrid GA-MLP model exhibited superior statistical parameter performance in comparison to the MLP model. During the training phase, the R2, RMSE, NS, and WI ranges for the GA-MLP model were 0.934–0.877, 0.460–0.343, 0.872–0.769, and 0.964–0.931, respectively. Similarly, during the testing phase, these values were 0.928–0.839, 0.578–0.389, 0.872–0.679, and 0.958–0.890, respectively. 

In general, it can be concluded that hybrid models may not always be the optimal choice for estimating the SPEI-1 index in semi-arid climates. This implies that while hybrid models like GA-RF and GA-MLP show strong performance, simpler models with well-chosen predictors can sometimes yield comparable or even superior results. Additionally, the inclusion of predictor parameters such as SPEIbase and PRC-PE plays an important role in estimating this index. Accurately estimating SPEI-1 is vital for effective water resource management in semi-arid regions. Accurate drought predictions enable policymakers and water resource managers to implement timely measures to mitigate the adverse impacts of drought on agriculture, water supply, and ecosystem health. For instance, advanced warning of drought conditions can guide water allocation decisions, optimize irrigation schedules, and support drought preparedness plans. In conclusion, the diverse data sources, advanced machine learning techniques, and scenariobased analysis collectively contribute to a robust and reliable framework for estimating the SPEI-1 index in semi-arid climates. This study faced limitations such as restricted access to ground-based data, potential inconsistencies due to varying quality and temporal coverage of satellite data, limited model generalizability to other climatic conditions, potential discrepancies arising from diverse data sources, and the increased computational complexity associated with hybrid models like GA-RF and GA-MLP. For research purposes, it is critical to analyze and contrast these parameters in relation to alternative machine learning models and across different climate conditions. Future studies should consider expanding the data scope by incorporating multiple stations in other semi-arid regions to enhance the generalizability of the results, evaluating model accuracy across different time periods to identify climatic trends, testing more advanced machine learning models, analyzing the impact of long-term climate changes on the SPEI-1 

index and employed models, and improving the accuracy of satellite data to refine estimates. 

**Author contribution** H.T.: Conceptualization, Methodology, Writing – original draft. S.S.: Software, Writing – review & editing. 

**Funding** The authors declare no funding sources for this research. 

**Data availability** The datasets generated during and/or analyzed during the current study are available from the corresponding author on reasonable request. 

### **Declarations** 

**Conflict of interest** The authors declare no competing interests. 

## **References** 

- Achite M, Jehanzaib M, Elshaboury N, Kartal V, Ali S (2023a) Hydrological drought prediction based on hybrid extreme learning machine: Wadi Mina Basin Case Study, Algeria. Atmosphere 14(9):1447 

- Achite M, Katipoglu OM, Şenocak S, Elshaboury N, Bazrafshan O, Dalkılıç HY (2023b) Modeling of meteorological, agricultural, and hydrological droughts in semi-arid environments with various machine learning and discrete wavelet transform. Theoret Appl Climatol 154(1):413–451 

- Aksu H, Cavus Y, Aksoy H, Akgul MA, Turker S, Eris E (2022) Spatiotemporal analysis of drought by CHIRPS precipitation estimates. Theoret Appl Climatol 148(1):517–529 

- Al-Hasani AAJ, Shahid S (2022) Spatial distribution of the trends in potential evapotranspiration and its influencing climatic factors in Iraq. Theoret Appl Climatol 150(1–2):677–696 

- Ali Z, Hussain I, Faisal M, Nazir HM, Hussain T, Shad MY ... Hussain Gani S (2017) Forecasting drought using multilayer perceptron artificial neural network model. Adv Meteorol 2017(1):5681308. https:// doi. org/ 10. 1155/ 2017/ 56813 08 

- Alvino A, Marino S (2017) Remote sensing for irrigation of horticultural crops. Horticulturae 3(2):40 

- Ansari Amoli A, Aghighi H, Lopez-Baeza E (2022) Drought risk evaluation in Iran by using geospatial technologies. Remote Sensing 14(13):3096 

- Asadollah SBHS, Sharafati A, Saeedi M, Shahid S (2024) Estimation of soil moisture from remote sensing products using an ensemble machine learning model: a case study of Lake Urmia Basin, Iran. Earth Sci Inform 17(1):385–400. https:// doi. org/ 10. 1007/ s12145- 023- 01172-8 

- Ashouri H, Hsu K-L, Sorooshian S, Braithwaite DK, Knap, KR, Cecil LD ... Prat OP (2015) PERSIANN-CDR: daily precipitation climate data record from multisatellite observations for hydrological and climate studies. Bull Am Meterol Soc 96(1): 69–83 

- Balbo F, Wulandari R, Nugraha M, Dwiandani A, Syahputra M, Suwarman R (2019) The evaluation of drought indices: standard precipitation index, standard precipitation evapotranspiration index, and palmer drought severity index in cilacap-central java. IOP Conf Ser: Earth Environ Sci 303(1):012012. https:// doi. org/ 10. 1088/ 1755- 1315/ 303/1/ 012012 

- Barzkar A, Najafzadeh M, Homaei F (2022) Evaluation of drought events in various climatic conditions using data-driven models and a reliability-based probabilistic model. Nat Hazards 110(3):1931–1952. https:// doi. org/ 10. 1007/ s11069- 021- 05019-7 

Earth Science Informatics (2024) 17:4949–4968 

4967 

- Beguería S, Vicente-Serrano SM, Beguería MS (2017) Package ‘spei’. In: Calculation of the standardised precipitation-evapotranspiration index, CRAN [Package]. CiteSeerX Pennsylvania State University: State College, PA, USA 

- Cancelliere A, Mauro GD, Bonaccorso B, Rossi G (2007) Drought forecasting using the standardized precipitation index. Water Resour Manage 21:801–819 

- Correa SW, de Paiva RCD, Espinoza JC, Collischonn W (2017) Multidecadal hydrological retrospective: case study of Amazon floods and droughts. J Hydrol 549:667–684 

- Damania R, Desbureaux S, Hyland M, Islam A, Rodella A-S, Russ J, Zaveri E (2017) Uncharted waters: the new economics of water scarcity and variability. The World Bank Publications, Washington, DC (© World Bank. https:// openk nowle dge. world bank. org/ handle/ 10986/ 28096 License: CC BY 3.0 IGO) 

- Danandeh Mehr A, Torabi Haghighi A, Jabarnejad M, Safari MJS, Nourani V (2022) A new evolutionary hybrid random forest model for SPEI forecasting. Water 14(5): 755. https:// www. mdpi. com/ 2073- 4441/ 14/5/ 755. Accessed 27 Feb 2022 

- Derdour A, Bouarfa S, Kaid N, Baili J, Al-Bahrani M, Menni Y, Ahmad H (2022) Assessment of the impacts of climate change on drought in an arid area using drought indices and Landsat remote sensing data. Int J Low-Carbon Technol 17:1459–1469 

- Dikshit A, Pradhan B, Alamri AM (2020) Temporal hydrological drought index forecasting for New South Wales, Australia Using Machine Learning Approaches. Atmosphere 11(6):585 

- Ecer F, Ardabili S, Band SS, Mosavi A (2020) Training multilayer perceptron with genetic algorithms and particle swarm optimization for modeling stock price index prediction. Entropy 22(11):1239. https:// www. mdpi. com/ 1099- 4300/ 22/ 11/ 1239. Accessed 31 Oct 2020 

- Eini MR, Rahmati Ziveh A, Salmani H, Mujahid S, Ghezelayagh P, Piniewski M (2023) Detecting drought events over a region in Central Europe using a regional and two satellite-based precipitation datasets. Agric for Meteorol 342:109733. https:// doi. org/ 10. 1016/j. agrfo rmet. 2023. 109733 

- Elbeltagi A, Pande CB, Kumar M, Tolche AD, Singh SK, Kumar A, Vishwakarma DK (2023) Prediction of meteorological drought and standardized precipitation index based on the random forest (RF), random tree (RT), and Gaussian process regression (GPR) models. Environ Sci Pollut Res 30(15):43183–43202. https:// doi. org/ 10. 1007/ s11356- 023- 25221-3 

- Fawagreh K, Gaber MM, Elyan E (2014) Random forests: from early developments to recent advancements. Syst Sci Control Eng: Open Access J 2(1):602–609 

- Fotse ARG, Guenang GM, Mbienda AJK, Vondou DA (2024) Appropriate statistical rainfall distribution models for the computation of standardized precipitation index (SPI) in Cameroon. Earth Sci Inf 17(1):725–744. https:// doi. org/ 10. 1007/ s12145- 023- 01188-0 

- Getahun YS, Li M-H (2023) Flash drought evaluation using evaporative stress and evaporative demand drought indices: a case study from Awash River Basin (ARB), Ethiopia. Theor Appl Climatol 155(1):85–104 

- Ghasemi P, Karbasi M, Zamani Nouri A, Sarai Tabrizi M, Azamathulla HM (2021) Application of Gaussian process regression to forecast multi-step ahead SPEI drought index. Alex Eng J 60(6):5375– 5392. https:// doi. org/ 10. 1016/j. aej. 2021. 04. 022 

- Hao C, Zhang J, Yao F (2015) Combination of multi-sensor remote sensing data for drought monitoring over Southwest China. Int J Appl Earth Obs Geoinf 35:270–283 

- Harris I, Osborn TJ, Jones P, Lister D (2020) Version 4 of the CRU TS monthly high-resolution gridded multivariate climate dataset. Sci Data 7(1):109. https:// doi. org/ 10. 1038/ s41597- 020- 0453-3 

- Holland JH (1992) Adaptation in natural and artificial systems: an introductory analysis with applications to biology, control, and artificial intelligence. MIT Press, Cambridge 

- Katipoğlu OM (2023a) Predicting hydrological droughts using ERA 5 reanalysis data and wavelet-based soft computing techniques. Environ Earth Sci 82(24):600 

- Katipoğlu OM (2023b) Prediction of streamflow drought index for short-term hydrological drought in the semi-arid Yesilirmak Basin using Wavelet transform and artificial intelligence techniques. Sustainability 15(2):1109 

- Kazemzadeh M, Noori Z, Alipour H, Jamali S, Akbari J, Ghorbanian A, Duan Z (2022) Detecting drought events over Iran during 1983–2017 using satellite and ground-based precipitation observations. Atmos Res 269:106052. https:// doi. org/ 10. 1016/j. atmos res. 2022. 106052 

- Khan MW, Ahmad S, Dahri ZH, Syed Z, Ahmad K, Khan F, Azmat M (2023) Development of high resolution daily gridded precipitation and temperature dataset for potohar plateau of indus basin. Theoret Appl Climatol 154(3):1179–1201. https:// doi. org/ 10. 1007/ s00704- 023- 04626-7 

- Kumar V, Sharma KV, Pham QB, Srivastava AK, Bogireddy C, Yadav S (2024) Advancements in drought using remote sensing: assessing progress, overcoming challenges, and exploring future opportunities. Theor Appl Climatol 1–38. https:// doi. org/ 10. 1007/ s00704- 024- 04914-w 

- Le MH, Perez GC, Solomatine D, Nguyen LB (2016) Meteorological drought forecasting based on climate signals using artificial neural network–a case study in Khanhhoa Province Vietnam. Procedia Eng 154:1169–1175 

- Manatsa D, Mukwada G, Siziba E, Chinyanganya T (2010) Analysis of multidimensional aspects of agricultural droughts in Zimbabwe using the Standardized Precipitation Index (SPI). Theoret Appl Climatol 102:287–305 

- McGill R, Tukey JW, Larsen WA (1978) Variations of Box Plots. Am Stat 32(1):12–16. https:// doi. org/ 10. 1080/ 00031 305. 1978. 10479 236 

- McKee TB, Doesken NJ, Kleist J (1993) The relationship of drought frequency and duration to time scales. In: Proceedings of the Eighth Conference on Applied Climatology (Boston, Massachusetts) American Meteorological Society, pp 17–22 

- Mirjalili S, Song Dong J, Sadiq AS, Faris H (2020) Genetic algorithm: theory, literature review, and application in image reconstruction. Nature-Inspired Optimizers: Theories, Literature Reviews and Applications 811:69–85 

- Mitra A, Kaushik N, Singh AK, Parihar S, Bhan S (2018) Evaluation of INSAT-3D satellite derived precipitation estimates for heavy rainfall events and its validation with gridded GPM (IMERG) rainfall dataset over the Indian region. Remote Sens Appl: Soc Environ 9:91–99 

- Mouatadid S, Raj N, Deo RC, Adamowski JF (2018) Input selection and data-driven model performance optimization to predict the standardized precipitation and evaporation Index in a droughtprone region. Atmos Res 212:130–149. https:// doi. org/ 10. 1016/j. atmos res. 2018. 05. 012 

- Mousavi R, Johnson D, Kroebel R, Byrne J (2023) Analysis of historical drought conditions based on SPI and SPEI at various timescales in the South Saskatchewan River Watershed, Alberta, Canada. Theor Appl Climatol 153(1):873–887 

- Nafarzadegan A, Zadeh MR, Kherad M, Ahani H, Gharehkhani A, Karampoor M, Kousari M (2012) Drought area monitoring during the past three decades in Fars province, Iran. Quat Int 250:27–36 

- Nguyen P, Ombadi M, Sorooshian S, Hsu K, AghaKouchak A, Braithwaite D ... Thorstensen AR (2018) The PERSIANN family of global satellite precipitation data: A review and evaluation of products. Hydrol Earth Syst Sci 22(11): 5801–5816 

- Nourani M, Alali N, Samadianfard S, Band SS, Chau K-W, Shu C-M (2022) Comparison of machine learning techniques for predicting porosity of chalk. J Petrol Sci Eng 209:109853 

Earth Science Informatics (2024) 17:4949–4968 

4968 

- Nwayor IJ, Robeson SM (2023) Exploring the relationship between SPI and SPEI in a warming world. Theoretic Appl Climatol 155(4):2559–2569 

- Ortiz-Gómez R, Flowers-Cano RS, Medina-García G (2022) Sensitivity of the RDI and SPEI drought indices to different models for estimating evapotranspiration potential in semiarid regions. Water Resour Manage 36(7):2471–2492 

- Otto FE, Zachariah M, Saeed F, Siddiqi A, Kamil S, Mushtaq H ... 

   - Barnes C (2023) Climate change increased extreme monsoon rainfall, flooding highly vulnerable communities in Pakistan. Environ Res: Climate 2(2): 025001 

- Potop V, Boroneanţ C, Možný M, Štěpánek P, Skalák P (2014) Observed spatiotemporal characteristics of drought on various time scales over the Czech Republic. Theoret Appl Climatol 115:563–581 

- Qi X, Chen G, Li Y, Cheng X, Li C (2019) Applying neural-networkbased machine learning to additive manufacturing: current applications, challenges, and future perspectives. Engineering 5(4):721–729. https:// doi. org/ 10. 1016/j. eng. 2019. 04. 012 

- Salvador C, Nieto R, Linares C, Díaz J, Gimeno L (2020) Effects of droughts on health: Diagnosis, repercussion, and adaptation in vulnerable regions under climate change. Challenges for future research. Sci Total Environ 703:134912 

- Senthilkumar M (2010) 5 - Use of artificial neural networks (ANNs) in colour measurement. In: Gulrajani ML (ed) Colour measurement. Woodhead Publishing, Cambridge, pp 125–146. https:// doi. org/ 10. 1533/ 97808 57090 195.1. 125 

- Shayeghi A, Ziveh AR, Bakhtar A, Teymoori J, Hanel M, Godoy MRV ... AghaKouchak A (2024) Assessing drought impacts on groundwater and agriculture in Iran using high-resolution precipitation and evapotranspiration products. J Hydrol 631:130828. https:// doi. org/ 10. 1016/j. jhydr ol. 2024. 130828 

- Sorooshian S, Hsu K-L, Gao X, Gupta HV, Imam B, Braithwaite D (2000) Evaluation of PERSIANN system satellite-based estimates of tropical rainfall. Bull Am Meteor Soc 81(9):2035–2046 

- Spinoni J, Barbosa P, De Jager A, McCormick N, Naumann G, Vogt JV ... Mazzeschi M (2019) A new global database of meteorological drought events from 1951 to 2016. J Hydrol: Reg Stud 22: 100593 

- Talebi H, Samadianfard S (2023) Effect of land surface temperature of MODIS sensor in estimating daily reference evapotranspiration in two different climates. Environ Water Eng 9(3):367–383 

- Talebi H, Samadianfard S, Kamran KV (2023a) Investigating the roles of different extracted parameters from satellite images in improving the accuracy of daily reference evapotranspiration estimation. Appl Water Sci 13(2):59 

- Talebi H, Samadianfard S, Valizadeh Kamran K (2023b) Estimation of daily reference evapotranspiration implementing satellite image data and strategy of ensemble optimization algorithm of stochastic gradient descent with multilayer perceptron. Environ Dev Sustain. https:// doi. org/ 10. 1007/ s10668- 023- 04037-8 

- Talebi H, Samadianfard S, Valizadeh Kamran K (2023) A novel method based on Landsat 8 and MODIS satellite images to estimate monthly reference evapotranspiration in arid and semi-arid 

climates. Water Soil Manag Model 3(3):180–195. https:// doi. org/ 10. 22098/ mmws. 2023. 12048. 1198 

- Taylor KE (2001) Summarizing multiple aspects of model performance in a single diagram. J Geophys Res: Atmospheres 106(D7):7183–7192 

- Tirivarombo S, Osupile D, Eliasson P (2018) Drought monitoring and analysis: standardised precipitation evapotranspiration index (SPEI) and standardised precipitation index (SPI). Phys Chem Earth, Parts a/b/c 106:1–10 

- Tyralis H, Papacharalampous G, Langousis A (2019) A brief review of random forests for water scientists and practitioners and their recent history in water resources. Water 11(5):910 

- Vicente-Serrano SM, Beguería S, López-Moreno JI (2010) A multiscalar drought index sensitive to global warming: the standardized precipitation evapotranspiration index. J Clim 23(7):1696–1718 

- Vicente ‐ Serrano SM, Domínguez ‐ Castro F, Reig F, Tomas ‐ Burguera M, Peña ‐ Angulo D, Latorre B ... Lorenzo ‐ Lacruz J (2023) A global drought monitoring system and dataset based on ERA5 reanalysis: A focus on crop ‐ growing regions. Geosci Data J 10(4): 505–518 

- Wang C, Huang M, Zhai P, Yu R (2023) Change of summer drought over China during 1961–2020 based on standardized precipitation evapotranspiration index. Theor Appl Climatol 153(1):297–309. https:// doi. org/ 10. 1007/ s00704- 023- 04471-8 

- Wei S, Zuo D, Song J (2012) Improving prediction accuracy of river discharge time series using a Wavelet-NAR artificial neural network. J Hydroinf 14(4):974–991 

- Wilhite DA (2002) Combating drought through preparedness. Natural resources forum, vol 4. Wiley, Hoboken, pp 275–285. https:// doi. org/ 10. 1111/ 1477- 8947. 00030 

- Yang P, Xia J, Zhang Y, Hong S (2017) Temporal and spatial variations of precipitation in Northwest China during 1960–2013. Atmos Res 183:283–295 

- Ye X, Dong L-A, Ma D (2018) Loan evaluation in P2P lending based on Random Forest optimized by genetic algorithm with profit score. Electron Commer Res Appl 32:23–36. https:// doi. org/ 10. 1016/j. elerap. 2018. 10. 004 

- Yuce MI, Deger IH, Esit M (2023) Hydrological drought analysis of Yeşilırmak Basin of Turkey by streamflow drought index (SDI) and innovative trend analysis (ITA). Theoret Appl Climatol 153(3–4):1439–1462 

- Ziveh AR, Bakhtar A, Shayeghi A, Kalantari Z, Bavani AM, Ghajarnia N (2022) Spatio-temporal performance evaluation of 14 global precipitation estimation products across river basins in southwest Iran. J Hydrol Reg Stud 44:101269 

**Publisher's Note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law. 

Reproduced with permission of copyright owner. Further reproduction prohibited without permission. 

