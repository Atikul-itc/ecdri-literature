Climate Dynamics (2024) 62:141–163 https://doi.org/10.1007/s00382-023-06893-6 



# **Machine learning algorithms for merging satellite‑based precipitation products and their application on meteorological drought monitoring over Kenya** 

#### **Suravi Ghosh**<sup>**1**</sup> **· Jianzhong Lu**<sup>**1**</sup> **· Priyanko Das**<sup>**2**</sup> **· Zhenke Zhang**<sup>**2**</sup> 

Received: 28 December 2022 / Accepted: 11 July 2023 / Published online: 5 August 2023 © The Author(s), under exclusive licence to Springer-Verlag GmbH Germany, part of Springer Nature 2023 

#### **Abstract** 

This study evaluates the reliability of merged satellite precipitation products based on single machine learning (SML) and double machine learning (DML) algorithms to estimate meteorological drought events over Kenya from 2000 to 2019. This study selected four SML algorithms, including Random Forest (RF), Support Vector Machine (SVM), K-nearest neighbors (KNN), and the gradient boosting machine (GBM) algorithm, to merge satellite precipitation products. In contrast, the DML algorithm is developed based on the classification RF approach and combined with these regression machine learning models (i.e., RF-RF, RF-SVM, RF-KNN, and RF-GBM). The four gridded precipitation products, including Climate Hazards Group Infra-Red Precipitation with Station (CHIRPS), Integrated Multi-Satellite Retrievals for GPM (IMERG-v06), Precipitation Estimation from Remotely Sensed Information using Artificial Neural Network-Climate Data Record (PERSIANN-CDR) and ERA-5 reanalysis datasets utilized in merging approaches. In total, we compared twelve precipitation products, including four gridded precipitation products (GPPs), four SML, and four DML, against Climate Research Unit (CRU) based rain-gauge (RG) observation. The Standardized precipitation indices (SPI) were estimated from these twelve precipitation datasets and compared their performance of CRU observation across Kenya. In addition, a total of seven statistical metrics were utilized for the performance assessment of all precipitation estimates. The results revealed that the DML merged products achieved higher accuracy (CC = 0.75–0.9) compared to SML products or other GPPs products against observational data. Also, DML merged products show higher performance (CC = 0.8–0.86) for two rainy seasons (long rain and short rain) than other GPPs, and SML merged products, except RF. Moreover, our findings indicate that the DML merged precipitation products identified major meteorological drought events with the lowest RMSE error than other precipitation products based on multiple SPI timescales (SPI-3, SPI-6, and SPI-12). The DML algorithm significantly improves SML models for precipitation estimates to monitor meteorological drought events over Kenya. 

**Keywords** Machine learning · Meteorological drought · Precipitation merging · Satellite precipitation products · Kenya 

## **1 Introduction** 

- Jianzhong Lu lujzhong@whu.edu.cn 

- Priyanko Das 

   - priyanko_nju@outlook.com 

- 1 State Key Laboratory of Information Engineering in Surveying, Mapping, and Remote Sensing (LIESMARS), Wuhan University, Wuhan, China 

- 2 Institute of African Studies, School of Geography and Ocean Sciences, Nanjing University, Nanjing, China 

Drought is considered one of the most distractive natural disasters worldwide, influencing agriculture development, water resources, environmental sustainability, and socioeconomic development (Lai et al. 2019; Jiang et al. 2021; Prodhan et al. 2022). During the recent decade, the severity and complexity of drought occurrence have aggravated worldwide due to increased global temperature (Santos et al. 2021). The global hydrological cycle has changed, and droughts are expected to increase under the climate change scenario (Lai et al. 2019). In addition, drought was responsible for the high number of human death and affected 36.5 million people worldwide during 2003–2012 (Chen et al. 

Vol.:(0123456789)1 3 

S. Ghosh et al. 

142 

2022). Therefore, accurate estimation and prediction of drought events provide necessary information for policymakers, environmentalists, water resource managers, and hydrologists (Alizadeh and Nikoo 2018; Li et al. 2022; Zhong et al. 2019). According to several studies (Mohseni et al. 2021; Malik et al. 2022), drought is categorized into four types agricultural (Orimoloye 2022), hydrological (Lai et al. 2019), meteorological (Wei et al. 2021), and socio-economic drought (Liu et al. 2021). Meteorological drought is one of the major droughts that depends on diminished rainfall conditions for an extended period over a region (Pathak and Dodamoni 2020). In general, it is believed that meteorological droughts generate all types of droughts (Jiang et al. 2021). Several studies estimate various types of meteorological drought indices, such as the Deciles Index (DI) (Dikici 2020; Yaseen et al. 2021), the Palmer Drought Severity Index (PDSI) (Palmer 1965), and the Standardized Precipitation Evapotranspiration Index (SPEI) (Mehr et al. 2019; Zhang et al. 2019; Zhang et al. 2019). Although SPI is a standardized drought index that indicates drought features at multiple time scales and considers the precipitation effect on droughts (McKee et al. 1993; Li et al. 2022). In the year 2009, the World Meteorological Organization (WMO) found that the SPI is an important meteorological drought index and is recommended for drought measurement on a global scale (WMO 1994). In addition, estimating the SPI index only requires precipitation data as input and indicating both short- and long-term drought, making it very useful for monitoring drought (McKee et al. 1993). Therefore, our study considers the SPI index to predict meteorological drought conditions in Kenya. 

Precipitation is one of the major components of the hydrological cycle and is essential for understanding a region's drought events, water resource management, and climate variability (Rahman et al. 2021; Zhang et al. 2022). Therefore, accurate precipitation estimation is very important for the computation of meteorological drought indices (Zhong et al. 2019; Rahman et al. 2021). The Rain-Gauge (RG) precipitation observation has good precision for estimating drought indices, but sparse distribution and insufficient data availability originate more uncertainty in computation (Zhang et al. 2021a, b; Li et al. 2022). According to the WMO, it is necessary to have one RG device for every 575  km<sup>2</sup> , but it's challenging in every remote area, especially in the African region (Santos et al. 2021; Das et al. 2022a). Thus, various satellite precipitation and reanalysis products have been developed with a high spatial resolution (Lin et al. 2022). The reanalysis precipitation products have long data records, and satellite products provide information for nearreal-time monitoring (Fan et al. 2021). In general, satellite precipitation products are generated from Infrared (IR) and Passive Microwave (PMW) sensors (Atiah et al. 2020). In recent years, Precipitation Estimation from Remotely Sensed 

Information using Artificial Neural Network-Climate Data Record (PERSIANN-CDR) (Ashouri et al. 2015; de Brito et al. 2021; Guo et al. 2016), Tropical Measuring Mission (TRMM) Multi-Satellite Precipitation (TMPA) (Shobeiri et al. 2021), Climate Hazards Group InfraRed Precipitation with Station data (CHIRPS) (Funk et al. 2015; Shrestha et al. 2017; Zhong et al. 2019), Integrated Multi-Satellite Retrievals for Global precipitation measurement (IMERG) (Huffman et al. 2019; Behrangi and Wen 2017; Mayor et al. 2017) and ERA5 (Fan et al. 2021) precipitation products have used for drought monitoring in worldwide. However, the individual satellite and reanalysis precipitation products have large biases due to sampling error, retrieval algorithm, and sensor types (Fan et al. 2021). Therefore, several approaches have been used to merge these gridded precipitation products (GPPs) and improve the accuracy of precipitation estimation (Zhang et al. 2021a, b). 

In recent years, machine learning (ML) algorithms attracted the scientific community for research in different fields such as climate science (Prodhan et al. 2022), agriculture (Liakos et al. 2018; Rehman et al. 2019), environmental science (Mohammadi et al. 2023), and engineering (Zhang et al. 2021a, b; Flah et al. 2021). Several studies used ML algorithms to merge various precipitation products to improve and develop new precipitation estimates (Rahman et al. 2021). Lin et al _._ (2022) evaluated the error composition of TRMM and IMERG and used three merge tree-based ML algorithms, such as random forest (RF), Decision Tree (DT), and Adaptive Boosting Decision Tree (Adaboost), for improving precipitation estimates. Zandi et al _._ (2022) generate high-resolution monthly precipitation products based on TRMM, ERA5, MSWEP v2, and land surface properties using an extreme learning or metalearning approach which consists of RF, multilayer perceptron neural network (MLP) and support vector machine (SVM). Rahman et al _._ (2021) developed merged satellite precipitation datasets (MSPs) from GPPs using Dynamic Bayesian Model Averaging (DBMA), Dynamic Clustered Bayesian Model Averaging (DCBA), Dynamic Weighted Average Least Square (WALS), and Regional Dynamic Weighted Average Least Square (RWALS). Chen et al. (2020) proposed a Geographically Weighted Ridge Regression (GWRR) model for merging four satellite precipitation products with gauge observation in the Xijiang basin, China. Similarly, Zandi et al. (2023) estimate new precipitation estimates by merging three large-scale satellite products using the Locally Weighted Linear Regression (LWLR) model. Kolluru et al. (2020) used sixteen ML approaches for developing secondary precipitation estimates from three GPPs and four combinations. Fan et al. (2021) compared four ML approaches, including Multivariate Linear Regression (MLR), Feedforward Neural Network (FNN), RF, and Long Short-Term Memory Network (LSTM), for merging 

1 3 

Machine learning algorithms for merging satellite‑based precipitation products and their… 

143 

five GPPs and generate accurate precipitation estimates. Zhang et al. (2021a, b) introduce a novel Double Machine Learning (DML) algorithm for merging multi-precipitation products and RG observation over mainland China. The DML approach is developed from individual ML learning algorithms, which include RF, SVM, Extreme Learning Machine (ELM), and Artificial Neural Networks (ANN). This study found that the DML approach has a dominant performance compared to a single ML application for merging satellite precipitation products (SPPs). However, very few studies reported ML approaches for merging GPPs and used them for meteorological drought monitoring (Alizadeh and Nikoo 2018; Rahman et al. 2021). In addition, no studies were found for the computation of meteorological droughts based on DML approaches. 

Kenya is a drought-devastating country in East Africa, and for the last five decades, it's witnessing severe droughts under the climate change condition (Ayugi et al. 2020). This drought impacts Kenya's economy, health, infrastructure, and water resources (Tan et al. 2020). Although, the sparsely distributed RG observation in complex topography makes it difficult to estimate droughts over Kenya. Several studies used GPPs products for monitoring drought events, but low accuracy against RG is the major challenge for drought computation (Miller et al. 2021). For example, Das et al. (2022b) evaluated two GPPs products for meteorological drought monitoring in the Lake Victoria basin and found overestimated/underestimated values. Thus, we selected this study region to develop new precipitation estimates using four ML and DML merging approaches based on five GPPs products for meteorological drought monitoring. 

In this study, we used four ML, and DML approaches to merge GPPs for meteorological drought monitoring based on regression and classification models. In addition, we introduce two novel DML approaches and their reliability for drought event estimation. The validation of newly merged precipitation products and GPPs was tested over Kenya. This is the first time considering various ML and DML approaches for drought estimation in the East Africa region. The major objective of this study is—(i) to assess the potential GPPs products for drought monitoring over Kenya, (ii) to evaluate the effectiveness of DML approaches for precipitation estimation and compare them with SML and GPPs products, and (iii) to evaluate the accuracy and reliability of DML algorithms for short-term, mid-term, and long-term drought events monitoring against GPPs and SML products. Although, this study considers not only the detection capacity of DML approaches but also their spatiotemporal variability. This study helps to get the alternative potential precipitation source to monitor meteorological drought events over Kenya. In addition, it will assist the water resource manager, hydrologist, and environmentalist in improving water policy and water management in Kenya. 

## **2  Materials and method** 

### **2.1  Study area** 

Kenya is situated in East Africa and shares boundaries with Uganda, Tanzania, Ethiopia, Sudan, and Somalia. The country lies between 5º S and 5º N latitude and 34º and 42º E longitude (Fig. 1). The rain-fed agriculture is the main source of the economy and mainly occurs in arid and semi-arid land (ASAL), covering 80% of this country (Barrett et al. 2020). According to the KOppenGeiger classification, this region belongs to the Aw climatic region (tropical savanna climate), which define this study area has a high risk of shrinking water level (Peel et al. 2007). The population of Kenya is approximately 40 million (Mutsotso et al. 2018). The complex topography includes high-altitude central highlands, the Indian Ocean coastline, and the enormous Lake Victoria Basin (LVB) dominating the local climate and ecosystem (Ayugi et al. 2020). The inter-annual average rainfall is high (more than 2000 mm) in potential regions, whereas low rainfall (less than 250 mm) was received in the ASAL region of Kenya (Ochieng et al. 2022). The seasonal rainfall of this country is bimodal (Ayugi et al. 2019, 2020), experiencing two rainfall seasons, which include long rain from March to May (MAM) and Short-rain from October to December (OND). Long rain is associated with the breaking down the near-equatorial trough and northward passage, whereas short rain is associated with the southward passage of the near-equatorial trough (Hastenrath 2001). Although, the seasonal rainfall is influenced by the inter-tropical convergence zone (ITCZ) (Ongoma et al. 2018). In addition, the ITCZ affects the pattern of temperature fluctuation (Ayugi et al. 2019). The annual average temperature ranges from 19 to 30 ºC over the studied region. While the higher temperature is recorded from January to February (JF), and the lower temperature is observed from June to September (JJAS) (Ayugi et al. 2019). From the altitude perspective, the lowest temperature was recorded in the rift valley side, and high temperatures were observed in the ASAL region of Kenya (Tan et al. 2020). Table 1 shows the topographical and climatic characteristics of rain-gauge stations over Kenya. 

### **2.2  Data** 

This study considers four global daily precipitation estimations (CHIRPS, IMERG, PERSIANN-CDR, and ERA5) for utilizing four ML and DML approaches from 13 rain-gauge stations over Kenya during 2000–2019. The period is selected based on the data availability from all 

1 3 

S. Ghosh et al. 

144 

**Fig. 1** Location Map of Kenya with observation station and altitude 



**Table 1** Topographical and climate characteristics of RGs observations 

|RG stations|Latitude|Longitude|Elevation (m)|Annual rainfall<br>(mm)|Average<br>temperature<br>(℃)|
|---|---|---|---|---|---|
|Eldoret|0.514° N|35.269° E|2,090|1400|17.3|
|Garissa|0.453° S|39.646° E|146|467|33|
|Jomo Kenyatta|1.329° S|36.923° E|1624|1107|20|
|Kisii|0.677° S|34.779° E|1700|2141|21|
|Kitale|1.019° N|35.002° E|1900|1403|19|
|Lodwar|3.115° N|35.604° E|477|302|34|
|Malindi|3.219° S|40.116° E|7|1040|28|
|Mandera|3.935° N|41.855° E|218|397|33|
|Mombasa|4.043° S|39.668° E|50|1130|27|
|Moyale|3.521° N|39.054° E|955|840|26|
|Nakuru|0.303° S|36.080° E|1850|1116|23|
|Narok|1.087° S|35.877° E|1827|1039|22|



four GPPs products. The daily scale data is converted to a monthly scale for the computation of the SPI index. The main objective of this study is to generate alternative monthly precipitation estimation for drought monitoring; thus, we only evaluate monthly, yearly, and seasonal periods. Table 2 presents a details summary of all GPPs products. 

**Table 2** Details of the four GPPs products used for merging and SPI estimation 

|Datasets|Study period|Spatial reso-<br>lution|Temporal<br>resolution|
|---|---|---|---|
|CHIRPS|2000–2019|0.25|1 day|
|IMERG|2000–2019|0.10|1 day|
|PERSIANN-CDR|2000–2019|0.25|1 day|
|ERA-5|2000–2019|0.25|1 h|



1 3 

Machine learning algorithms for merging satellite‑based precipitation products and their… 

145 

#### **2.2.1  RG‑based reference data** 

This study uses high-resolution gridded precipitation datasets to evaluate the GPPs, SML, and DML merged products over Kenya. This dataset is available from 1901 to 2020 and obtained from Climate Research Unit (CRU) Time Series (TS) center. The monthly CRU TS data provides gaugebased precipitation estimates with no missing values and excellent quality control and homogeneity check. In addition, the datasets are gridded to a 0.5º grid using angular distance weighting (ADW) interpolation, which maintains the good quality of the datasets (Harris et al. 2020). However, it should be noted that the accuracy of the CRU TS datasets mostly depends on the number of gauge-station participating in the gridding and interpolation process. Although previous studies suggest that the CRU TS observation is reliable for evaluating other precipitation estimates, it’s used for worldwide drought monitoring (Zhao and Ma 2019; Wei et al. 2021; Das et al. 2022b). The CRU TS observation is freely available online (https:// sites. uea. ac. uk/ cru/ data) and downloaded from 2000 to 2019. 

#### **2.2.2  Gridded Precipitation Products (GPPs)** 

The CHIRPS datasets are collaboratively generated by the Climate Hazards Group (CHG) at the University of California laboratory, Santa Barbara (UCSB) (Funk et al. 2015). In general, the CHIRPS datasets combine the IR- derived precipitation and the CHG precipitation climatology (CHPclim) and blend with gauge observation (Funk et al. 2015). The CHIRPS data provides high spatial resolution (0.05º × 0.05º) and covers 50º N–50ºS latitudes of the earth's surface and is used for drought monitoring by various researchers such as de Brito et al. (2021), Bouaziz et al. (2021). This study selected the monthly CHIRPS V2 products and downloaded them from the CHG website (https:// www. chc. ucsb. edu/ data/ chirps) during 2000–2019. 

The IMERG products blend microwave-calibrated IR and merge all satellite microwave precipitation estimation, gauge analysis, and other precipitation estimators (Huffman et al. 2014). The datasets are available at 0.1º × 0.1º spatial resolution and cover 60ºN–60ºS latitudes of the quasi-global area (Huffman et al. 2019). This study considers the daily IMERG version 6 (V6) product, which is later converted to a monthly scale for drought monitoring and downloaded from the Goddard Earth Sciences Data and Information Service Centre (GES DISC) website (https:// disc. gsfc. nasa. gov/). 

The PERSIANN-CDR data is jointly developed by the Centre for Hydrometeorology and Remote Sensing (CHRS), University of California, Irvine (UCI), and Climate Datacenter (NCDC) at the National Oceanic and Atmospheric Administration (NOAA) based on the CDR (Ashouri et al. 2015). This precipitation estimation is generated from the 

ANN algorithm on the GridSat-B1 IR satellite sensor and coved the near-globe region (60º N–60º S) with a high spatial resolution at 0.25º × 0.25º (Ashouri et al. 2015). The datasets are freely accessible and downloaded from the CHRS website (https:// chrsd ata. eng. uci. edu/). 

The ERA5 dataset is a global reanalysis product provided by European Centre for Medium-Range Weather Forecast (ECMWF) and generated using the Integrated Forecast System (IFS) (Hersbach et al. 2020). The datasets are generally developed using the 4D var assimilation approach in cycle 41r2 (Hersbach et al. 2020). The daily ERA5 datasets are available from 1979 to the present at a global scale with 0.1º × 0.1º. The ERA5 reanalysis precipitation estimation is accessible at https:// cds. clima te. coper nicus. eu/ cdsapp# !/ home. 

### **2.3  Methodology** 

The study framework is described in Fig. 2. Although, this study considers four widely used Single ML (SML) and four newly developed DML approaches for merging four GPPs (i.e., CHIRPS, IMERG, PERSIANN-CDR, and ERA5) and station observation. The four SML schemes were generated based on regression models, including Random Forest (RF), Support Vector Machine (SVM), K-Nearest Neighbour (KNN), and Gradient Boosting Machine (GBM). The DML 



<!-- Start of picture text -->
GPP products (CHIRPS,<br>CRU TS  IMERG, PERSIANN-<br>observation CDR and ERA-5)<br>Aggregate (0.25)<br>RF SVM RF-RF RF-SVM<br>KNN GBM RF-KNN RF-GBM<br> SML                                     DML<br>Statistical Metrics<br>Validate precipitation products<br>at a monthly scale, seasonal<br>scale, and annual scale<br>Drought analysis and<br>SPI<br>SPI-3 SPI-6 SPI-12<br>Validation metrics<br>Comparison at<br>temporal scale<br>Comparison at<br>spa�al scale<br><!-- End of picture text -->

**Fig. 2** Flowchart of the methodology 

1 3 

S. Ghosh et al. 

146 

fusion approach is developed based on the classification model of RF in combination with four other SML models (i.e., RF, SVM, KNN, and GBM) and lead to four new DML fusion scheme including RF-RF, RF-SVM, RF-KNN, and RF-GBM followed by Zhang et al. (2021a, b). The drought index (SPI) was computed from the GPPs and newly developed precipitation estimates from SML and DML algorithms and compared to the gauge observation. The precipitation data is split into 70% for training and 30% for testing from 2000 to 2019. while 2000 to 2012 is selected for training data, and 2013 to 2019 is considered for the test dataset. 

#### **2.3.1  Single machine learning (SML) approach** 

**2.3.1.1 Random forest (RF)** The RF algorithm was first proposed by Breiman (2001), and it's based on the ensemble of the decision tree approach to perform the bagging process to solve the regression problem (Yaseen et al. 2021). This model deals with random binary trees, which use a subset of the observation using the bootstrap method. In contrast, a random subset of training data sampled from the raw datasets was utilized to develop the model (Mokhtar et al. 2021). The RF enhanced the generalization capability, reduced overfitting problems, and used ensemble prediction from the random selection and predictors of input variables (Zhang et al. 2021a, b). This study used an RF algorithm for data fusion as follows 



where _휌RF_ represents the merged output from RF, β represents the number of trees, _Se_<sup>∗ represent each decision tree, Z</sup> represents the input vector, and e represents the individual bootstrap sample (Fan et al. 2021). Our study selected classification and regression-based tree algorithms using root mean square error (RMSE). The number of trees or _ntree_ (β) was set to 300 after performing 25, 50, 100, 200, 300, and 400. In general, the RF model performed excellently when the _ntree_ was increased. Although, when β = 400, the RMSE and other error metrics values did not decrease. Thus, we set the regression tree to 300. Similarly, the RF performed better 

when the leaf node ( _nmin_ ) was set to 8 from 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. In addition, the number of features  (n _features_ ) was considered as 2 from 1, 2, 3, and 4 (Table 3). 

**2.3.1.2 Support vector machine (SVM)** The SVM is a supervised ML model developed by Cortes and Vapnik (1995) and used for classification and regression analysis (Zandi et al. 2022). The regression model finds an optimal hyperplane exhibited by a regression function that best expresses the observation output with an error tolerance. In contrast, the classification model finds an optimal hyperplane where the individual categories are divided by a clear gap (Zhang et al. 2021a, b). In addition, it finds a boundary layer to minimize an error function and appoint structural risk minimization (Yin et al _._ 2022). Several researchers used the SVM model for precipitation prediction and hydro-meteorological studies (Jose et al. 2022; Yoosefdoost et al. 2022; Zhang et al. 2022). The present study set the radial basis function (RBF) as the kernel function, and two hypermeters (γ, c) (Table 2) were determined using a random search approach in a grid layout with an error procedure followed by Zhang et al. (2021a, b Yin et al _._ (2022). We used the "e1071" package in R to implement the SVM model. 

**2.3.1.3 K‑Nearest Neighbour (KNN)** KNN is a non-parametric algorithm that defines "k" numbers of neighbors based on calibrated data and is used to predict new data from the Euclidean distance measures (Ahmed et al. 2020). This algorithm finds “k” educational points which are nearest to the hypothetical query point (Y0) and categorized based on the majority (Huang et al. 2017; Mehdizadeh 2020). For example, if the k = 1, then the object is allocated its nearest neighbors, and increasing the number (e.g., 1, 2, 3, 4) has an impact on decreasing the predictive error (Citakoglu & Coskun, 2022). Although, several authors used the KNN algorithm for precipitation prediction (Huang et al. 2017; Ahmed et al. 2020; Taghi Sattari et al. 2021). Therefore, the present study considers the KNN approach. To estimate the Euclidean distance for P- the dimension of the predictor, the function is followed – 

**Table 3** Description of the four SML merging methods 

|Model|Parameters|
|---|---|
|Random Forest (RF)|Number of trees (ntrees) = 300, leaf node (_nmin_), number of feature (_nfeatures_) = 2|
|Support Vector Machine (SVM)|Radial Basis Function (RBF), Hypermeters = γ, c|
|K-Nearest Neighbour (KNN)|Number of k = 1:16<br>method = “repeatedcv”<br>k fold = 10|
|Gradient Boosting Machine (GBM)|Number of tree or ntree (β) = 200, Interaction-depth = 8, Shrinkage = 0.1,<br>n.minobsinnode = 10|



1 3 

Machine learning algorithms for merging satellite‑based precipitation products and their… 

147 

_d훼_ , _훽_ = √( _훼_ − _훽_ )<sup>2</sup> 

where _훼_ is the new point, and _훽_ is the learning point. The next step is to arrange the data in ascending order with sample point after estimating the Euclidean distance and finding the numbers of neighbors (k), followed by Citakoglu and Coskun (2022). The present study set the number of k as 1:16 after performing 1, 2, 3…0.18. when the k is set to 1:17/18, the model's performance doesn't increase. The “repeatedcv" method was set, and the number of folds selects as 10 for training control parameters (Table 3). The KNN algorithm was implemented using the "caret” package in R. 

#### **2.3.1.4 Gradient boosting machine (GBM)** GBM is a tree- 

based ensemble learning approach proposed by Friedman (2001), and the main objective is to reduce the difference between observed and predictive values (Akinci 2022; Ebrahimi-Khusfi et al. 2022). The algorithm is trained decision tree in a persistent manner (Song et al. 2022), and the boosting term refers to a subsequential process for using gradient descent (Malik et al. 2022). In addition, the gradient descent maintains three main parameters: loss function optimization, an additive model, and a weak learner (Malik et al. 2022). Although, the GBM approach is used for classification and regression problems (Monego et al. 2022). However, the algorithm of GBM can be found in Friedman (2001). The present study selects the “GBM” method using R's "caret” package. The hyper-parameter, such as the number of trees or _ntree_ (β), was set to 200 after performing 50, 100, 150, 200, 250, and 300. The error matrices weren't reduced when the _ntree_ was 250 or 300. Thus, we set β = 200. The maximum tree depth (interaction depth) was set to 8 after performing 1,2,3……8, the shrinkage was set to 0.1, and the minimum terminal node size (n.minobsinnode) was set to 10 (Table 3). 

#### **2.3.2  Double machine learning (DML) fusion method** 

The present study proposed a DML approach from four regression and classification ML models to merge four GPPs product and RGs observation, inspired by the work of (Zhang et al. 2021a, b). First, we generated four classification models based on the single ML approach and evaluated them based on the test datasets. Similarly, the four-regression model was also created from the individual ML approach and evaluated from the test datasets. The evaluation process is based on statistical metrics and test datasets. However, the optimization process and training are similar for both classification and regression. The results indicate that the classification model gives more accuracy 

than the regression model, which is also noted by (Zhang et al. 2021a, b). In addition, the present study considers the RF classification model due to its better performance compared to the other three ML models (SVM, KNN, GBM). Finally, the four DML approaches were developed, which include RF-RF, RF-SVM, RF-KNN, and RF-GBM. The DML algorithm was developed using the "Meta-Learning" package in R. 

#### **2.3.3  Standardized precipitation index (SPI)** 

The present study used SPI for drought estimation from 2000 to 2019 in Kenya, East Africa. The SPI was developed by McKee et al. (1993) and is widely used for drought monitoring (Shrestha et al. 2017; Pathak and Dodamani 2020). The SPI requires only precipitation data for the performed algorithm, which is the major advantage of using this index. The standardized procedure to calculate the SPI, first the precipitation records used as input to fit in a distribution such as a gamma distribution or Pearson III, and secondly, the frequency of precipitation records calculated based on the fitted distribution and finally transformed into standardized normal distribution (Zhong et al. 2019). Generally, a drought event starts when the SPI value is equal to or less than – 1.0, and this drought event end when this value reaches greater than – 1.0 (de Brito et al. 2021). In addition, the precipitation frequency was fitted based on gamma distribution, and cumulative precipitation was applied to multiple time scales (i.e., 3, 6, 9, 12, 24) from the time series. The description of wetness and dryness intensity can be found in Table 3 (McKee et al. 1993). Although, the SPI values can be set as follows (Zhang and Li 2020): 





where " _휎_ " is the monthly precipitation, _e_ 0 = 2.515517, _e_ 1 = 0.802853, _e_ 2 = 0.010328, _f_ 1 = 1.43278, _f_ 2 = 0.189269, and _f_ 3 = 0.001308. _훾_ = time. 

" _휆_ ( _휎_ )" is the probability of the data series being translated into an incomplete gamma distribution function (Bouaziz et al. 2021; Liu et al. 2021), which is expressed as: 

1 3 

S. Ghosh et al. 

148 

**Table 4** Drought classification based on SPI values (Mckee et al. 1993) 

|Drought classification|SPI values|
|---|---|
|Extremely wet|> 2.0|
|severe wet|1.5–1.9|
|Moderately wet|1–1.49|
|Near Normal|0.99 to – 0.99|
|Moderately drought|– 1 to – 1.49|
|severe drought|– 1.5 to – 1.9|
|Extremely drought|< – 2.00|





where α parameter represents the shape, β is about scale factor, and _휎_ is the precipitation quality. Γ( _훼_ ) is the main function in the gamma distribution. 

This study considers three SPI time scales (i.e., SPI-3, SPI-6, SPI-12) to monitor the drought condition in Kenya from 2000 to 2019. The two parameters were used for probabilistic distribution of SPI from adjected precipitation data. The present study performed a meteorological drought index based on four GPPs, four ML, four DML, and RGs datasets. Hence, this study evaluates 432-time series (9-time-series * 16 data sets * 3 timescales) with 240 SPI values (20*12). The "wet" and "dry" conditions are categorized based on SPI values presented in Table 4 **.** 

#### **2.3.4  Performance evaluation** 

The present study considers seven statistical metrics to evaluate the performance of GPPs, SML, and DML precipitation products against reference data for drought monitoring. Four continuous statistical metrics, which include Correlation Coefficient (CC), Percent of BIAS (PBIAS), Modified Kling-Gupta Efficiency (MKGE) score, and Theil's, were used to show the spatial distribution to compare these precipitation estimates. In contrast, three validation metrics, including Root Mean Square Error (RMSE), Mean Absolute Error (MAE), and Relative Absolute Error (RAE), were used for temporal comparison. The CC establishes the linear relationship between two variables and quantifies their strength. The goodness of fit statistic PBIAS indicated the overestimated/underestimated values for predicted time series and showed four performance ratings (Shrestha et al. 2017). The MKGE score includes the linear correlation ( _r_ ), variability ratio ( _훾_ ), and bias ratio (β), which describes the relationship between observation and predicted variables (Kling et al. 2012). In addition, Theil'U was used to evaluate the performance of precipitation estimates, where close to 0 showed 

**Table 5** Details of the statistical metrics used for accuracy verification 

|Metrics|Equation|
|---|---|
|CC|∑_n_<br>_i_=1<br>�<br>_Xi_−<br>_X_<br>��<br>_Yi_−<br>_Y_<br>�<br><br>|
||~~�~~<br>∑_n_<br>_i_=1<br>~~�~~<br>_Xi_−<br>_X_<br>~~�~~<sup>~~�~~</sup><br>∑_n_<br>_i_=1<br>~~�~~<br>_Yi_−<br>_Y_<br>~~�~~|
|MKGE Score|1−<br>~~√~~<br>(_CC_−1)<sup>2 </sup>+ ( <sup>_휇_(</sup><sup>_Y_)</sup><br>_휇_(_X_) <sup>−1)</sup><br>2+ ( _휎_(_Y_)∕_휇_(_Y_)<br>_휎_(_X_)∕_휇_(_X_) <sup>−1)</sup><br>2|
|Theil's U|~~�~~<br>1<br>_n_<br>∑_n_<br>_i_=1 <sup>(</sup><sup>_Yi_</sup> <sup>−</sup><sup>_Xi_)2∕∑</sup><sup>_n_</sup><br>_i_=1 <sup>_Y_2</sup><br>_i_|
|PBIAS<br>RMSE|∑(_Xi_−_Yi_)<br>~~∑~~_Xi_<br>_X_100<br>~~�~~<br>1<br>_n_<br>∑<sup>�</sup>_Yi_−_Xi_<br>�|
|MAE|1<br>_n_<br>∑��_Yi_−_Xi_��|
|RAE|∑<sup>�</sup><br>(_Yi_−_Xi_)<sup>2�</sup><br>~~∑~~_Xi_<br>2<br>_X_100|



excellent performance, and close to 1 showed error (Rahman et al. 2020). Moreover, RMSE, MAE, and RAE were used to show the magnitude of the error and systematic error based on the precipitation estimates. The algorithm used to estimate these statistical metrics is shown in Table 5. 

## **3  Results** 

### **3.1  Overall performance assessment of monthly precipitation** 

Figure 3 represents the 2D kernel density of estimated precipitation against RGs observation in Kenya with seven error metrics, including CC, KGE, PBIAS, RMSE, MAE, RAE, and Theil'U. The IMERG product shows the best performance (CC = 0.79) among other GPPs, followed by CHIRPS (CC = 0.78), ERA-5 (CC = 0.77), and PERSIANNCDR (CC = 0.76) before fusing them (Fig. 3a–c). But the merged datasets from ML and DML algorithms are more accurate than GPPs and reduce the error between precipitation estimates and RGs. For the Single Machine Learning (SML) fusion approach, the RF method showed the best performance (CC = 0.93, RMSE = 19.9 mm/month) then the GPPs estimation product (Fig. 3e) followed by KNN (CC = 0.82, RMSE = 29.62 mm/month), GBM (CC = 0.81, RMSE = 30.47 mm/month) and SVM (CC = 0.79, RMSE = 31.56 mm/month) (Fig. 3f–h). Although, the precipitation estimates significantly improved after applying Double Machine Learning (DML) approaches (Fig. 3i-l). The RF-KNN merging method showed better performance (CC = 0.89) than the single KNN approach, and the MAE has been reduced from 18.49 mm/month to 15.1 mm/month (Fig. 3g, k). Similarly, RF-SVM (CC = 0.88) and RFGBM (CC = 0.86) fusion approaches have shown excellent 

1 3 

Machine learning algorithms for merging satellite‑based precipitation products and their… 

149 



**Fig. 3** Two-dimensional kernel density estimates plot of GPPs, SML and DML against RGs observation over Kenya (2000–2019). CHIRPS ( **a** ), IMERG ( **b** ), PERSIANN-CDR ( **c** ), ERA-5 ( **d** ), RF ( **e** ), SVM ( **f** ), KNN ( **g** ), GBM ( **h** ), RF-RF ( **i** ), RF-SVM ( **j** ), RF-KNN ( **k** ), RF-GBM ( **l** ) 

accuracy compared to single SVM (CC = 0.79) and GBM (CC = 0.81) algorithm (Fig. 3j, l) and the MAE has been reduced from 18.8 to 15.4 mm/month for SVM (Fig. 3f) and from 18.6 to 16.35 mm/month for GBM (Fig. 3h). It should be noted that the RMSE error has been increased from 19.9 to 29.59 mm/month for the RF-RF fusion method, indicating less accuracy of precipitation estimate. However, the results indicate that the DML fusion approach improved the precipitation estimate compared to the SML method, Except for RF. 

Figures 4–7 illustrate the spatial distribution of four continuous metrics. Among the GPPs products, IMERG and CHIRPS provide better Correlation (CC = 0.4–0.7) of monthly precipitation with RGs compared to PERSIANNCDR and ERA-5 (Fig. 4a–d). The high correlation between GPPs and RGs was found in the southeast portion of Kenya, especially in Mombasa RGs (CC = 0.8–0.86), while very less correlation was found in the northwest portion, especially in Lodwar RGs (CC = 0.3 – 0.47). Although, the correlation (CC) between GPPs and RGs observation 

ranges from 0.6 – 0.7 over Kenya. For SML approaches, the northeast and the southeast portion of Kenya showed a high correlation (CC = 0.75 – 0.92) compared to GPPs, except RF (Fig. 4e–h). It is noticeable that the RF performed best and was very highly correlated (CC = 0.9–1) across Kenya compared to other ML, GPPs, and DML approaches (Fig. 4e). A similar study by Fan et al. (2021) also found that RF's merged precipitation products had higher accuracy (CC = 0.87) than other ML algorithms. Also, the SVM, KNN, and GBM have shown better performance and high correlation (CC = 0.7–0.76) with RGs observation (Fig. 4f–h). For DML datasets, the RF-GBM provides better correlation (CC = 0.75–0.9) with RGs observation, followed by RF-KNN (CC = 0.7–0.85), RF-RF (CC = 0.75–0.9) and RF-SVM (CC = 0.65–0.85) (Fig. 4i–l). However, the southwest portion has shown less correlation compared to other regions in Kenya (Fig. 4a-l). 

The MKGE score is relatively small for PERSIANNCDR and ERA-5, which are 0.4 and 0.5, respectively 

1 3 

S. Ghosh et al. 

150 



**Fig. 4** Spatial plot of correlation Coefficient (CC) between RGs observation and twelve precipitation estimates (GPPs, SML and DML) over Kenya. CHIRPS ( **a** ), IMERG ( **b** ), PERSIANN-CDR ( **c** ), 

ERA-5 ( **d** ), RF ( **e** ), SVM ( **f** ), KNN ( **g** ), GBM ( **h** ), RF-RF ( **i** ), RFSVM ( **j** ), RF-KNN ( **k** ), RF-GBM ( **l** ) 

(Fig. 5c, d). In particular, the PERSIANN-CDR shows overestimated rainfall of more than 15 mm compared to the observed precipitation over Kenya. Yumnam et al. (2022) also revealed that the PERSIANN-CDR overestimated precipitation estimates (more than 400 mm) over the Vamsadhara basin, India. Similarly, Rahman et al. (2020) found that the PERSIANN-CDR overestimated the precipitation estimates, especially during the monsoon season in Pakistan. The IMERG and CHIRPS performed best among the GPPs, with an MKGE score of 0.6 (Fig. 5a, b). The merge datasets from four SML approaches (i.e., RF, SVM, KNN, and GBM) provide higher MKGE scores than the GPPs products, which are 0.78, 0.65, 0.6, and 0.59 (Fig. 5e–h). The merged product generated from the DML method (i.e., RF-RF, RF-SVM, RF-KNN, and RF-GBM) has very high MKGE (0.5–1.0) values than other precipitation estimates (Fig. 5i–l). Zhang et al. (2021a, b) also reported that the 

DML approaches' merged precipitation products had higher accuracy (KGE = 0.67–0.71) than GPPs in China. In general, the higher MKGE values (0.6–1.0) were shown in the southeast and northeast parts of Kenya, while a small MKGE value (0.2–0.4) is distributed in the southwest part of Kenya (Fig. 5a–l). However, the excellent MKGE score for all the RGs observations in Kenya was found in RF merged datasets (Fig. 5e). 

The spatial distribution of qualitative ratings of PBIAS indicates that most of the regions have "good" and "satisfactory" ratings among the original GPPs (Fig. 6a–d) (Table 6). The IMERG product was shown a "good" rating in most of the RGs, whereas the other three GPPs (CHIRPS, IMERG, PERSIANN-CDR, and ERA-5) products were shown to have a "Satisfactory" rating. The merge datasets from the SML algorithm (i.e., RF, SVM, KNN, and GBM) provide a “Very Good” performance rating than GPPs precipitation 

1 3 

Machine learning algorithms for merging satellite‑based precipitation products and their… 

151 



**Fig. 5** Spatial plot of modified Kling Gupta Efficiency (MKGE) score between RGs observation and twelve precipitation estimates (GPPs, SML and DML) over Kenya. CHIRPS ( **a** ), IMERG ( **b** ), PERSIANN- 

CDR ( **c** ), ERA-5 ( **d** ), RF ( **e** ), SVM ( **f** ), KNN ( **g** ), GBM ( **h** ), RF-RF ( **i** ), RF-SVM ( **j** ), RF-KNN ( **k** ), RF-GBM ( **l** ) 

estimates (Fig. 6e–h). Although, some RGs were shown "Good" performance ratings for SVM-generated datasets (Fig. 6f). Similarly, the merge precipitation estimates from DML (i.e., RF-RF, RF-SVM, RF-KNN, and RF-GBM) have shown a “Very good” performance rating across Kenya (Table 5) (Fig. 6i–l). It should be noticed that most of the RGs have underestimated rainfall for GPPs, SML, and DML algorithm-generated products. In addition, the spatial distribution of Theil'U indicates that the IMERG product has good performance (0.4–0.6) compared to the other three GPPs (i.e., CHIRPS, PERSIANN-CDR, and ERA-5) (Fig. 7a–d). The merge products generated from SML (i.e., RF, SVM, KNN, and GBM) provide excellent performance (0.00–0.40) of monthly precipitation estimates compared to GPPs (Fig. 7e–h). Similarly, the merge precipitation datasets from DML (i.e., RF-RF, RF-SVM, RF-KNN, and RF-GBM) have smaller Theil'U values (0.2–0.4) and well-detect precipitation estimates against RGs observation (Fig. 7i–l). In general, the lowest values of Theil's distribution are in the southern part of Kenya, while higher values 

are distributed in the northern side (Fig. 7a–l). However, our results revealed that the merged datasets from the DML approach have more accuracy than the SML algorithm and GPPs products, Except RF. Sattari et al. (2021) also found that the hybrid ML models perform better (r = 0.75) than individual ML models for estimating monthly precipitation in Urmia station, West Azarbaijan. A similar study by Mehdizadeh (2020) reported that the hybrid ML models with a combination of KNN denote higher accuracy in estimating monthly precipitation over two RG stations in Iran. 

### **3.2  Seasonal performance assessment** 

Figure 8 represents the violin plot of four error metrics (i.e., CC, RMSE, MAE, and RAE) for evaluating the 12 precipitation estimates based on two rainy seasons (long rain and short rain) and one dry season over Kenya. The dry season over the study area is from June to September, while long rain is from March to May, and Short rain is from October to December. In general, error metrics of SML and 

1 3 

S. Ghosh et al. 

152 



**Fig. 6** Spatial plot of Percentage of Bias (PBIAS) between RGs observation and twelve precipitation estimates (GPPs, SML and DML) over Kenya. CHIRPS ( **a** ), IMERG ( **b** ), PERSIANN-CDR ( **c** ), 

ERA-5 ( **d** ), RF ( **e** ), SVM ( **f** ), KNN ( **g** ), GBM ( **h** ), RF-RF ( **i** ), RFSVM ( **j** ), RF-KNN ( **k** ), RF-GBM ( **l** ) 

**Table 6** PBIAS range for a particular qualitative rating 

|PBIAS (%)|Performance rating|
|---|---|
|<  ± 15|Very good|
|± 15 to ± 30|Good|
|± 30 to ± 55|Satisfactory|
|± 55|Unsatisfactory|



DML merged products were always better than GPPs. In all seasons, the original GPPs products performed worse than the datasets from the merge DML approach in terms of CC (Fig. 8a–c). Among the GPPs datasets, the IMERG product shows comparable performance in both rainy seasons (i.e., long and short rain), and PERSIANN-CDR shows very lower performance in the dry season (CC = 0.3). The merged datasets from the SML approach (i.e., RF, SVM, KNN, and GBM) have shown better performance than GPPs in all the seasons over Kenya. However, the merged datasets from the DML algorithm shows higher performance than other products in the dry and rainy season (Fig. 8a–l). 

The CC of merged products from DML was better and higher (RF-RF = 0.85, RF-SVM = 0.86, RF-GBM = 0.84, RF-KNN = 0.81) in short rain and smaller (RF-RF = 0.6.4, RF-SVM = 0.66, RF-GBM = 0.63, RF-KNN = 0.55) in the dry season (Fig. 8a–c). Similarly, the RAE of four merged products from DML is shown excellent performance for short rain season (RF-RF = 0.51, RF-SVM = 0.50, RFGBM = 0.52, RF-KNN = 0.57) and worst performance for dry season (RF-RF = 0.98, RF-SVM = 0.99, RF-GBM = 1, RF-KNN = 1) than other precipitation products (Fig. 8j–l). The four merged datasets from SML and DML for long rain showed comparatively better performance than the dry season. In addition, the RF algorithm product has shown accurate precipitation estimates (CC = 0.9, RMSE = 28.3 mm/ month) in all seasons compared to GPPs products. However, it is noticeable that the RMSE and MAE error is better in the dry season and poor in the rainy season (Fig. 8d–i). Fan et al. (2021) also reported that the RMSE error is better in the dry season compared to the rainy season. 

1 3 

Machine learning algorithms for merging satellite‑based precipitation products and their… 

153 



**Fig. 7** Spatial plot of Theil’U between RGs observation and twelve precipitation estimates (GPPs, SML and DML) over Kenya. CHIRPS ( **a** ), IMERG ( **b** ), PERSIANN-CDR ( **c** ), ERA-5 ( **d** ), RF ( **e** ), SVM ( **f** ), KNN ( **g** ), GBM ( **h** ), RF-RF ( **i** ), RF-SVM ( **j** ), RF-KNN ( **k** ), RF-GBM ( **l** ) 

### **3.3  Assessment of the spatial distribution of annual precipitation** 

Figure 9 illustrates the spatial distribution of annual precipitation from RGs, GPPs, SML, and DML merged products. The highest annual rainfall of RGs was observed in the southwest region of Kenya, which is part of the Lake Victoria Basin. In contrast, Kenya's eastern and northwest regions recorded the lowest annual rainfall. The spatial characteristics generated from the SML and DML products are similar to the RGs observation. Among the GPPs products, the IMERG datasets show overestimated precipitation in the southwestern region of Kenya, followed by PERSIANN-CDR and ERA5 (9a-e). In a similar region, the merged products from SML (i.e., RF, SVM, KNN, and GBM) have shown underestimated precipitation (Fig. 9f–i). Similarly, the merged product from DML (i.e., RF-RF, RFSVM, RF-KNN, and RF-GBM) have shown underestimated precipitation, but the differences (20–40 mm) are negligible (Fig. 9j–m). It should be noticeable that the merged product from RF and CHIRPS datasets capture similar annual precipitation with RGs in the southern region of Kenya (Fig. 9b, 

f). However, the results demonstrate that the merged product from DML gives more accuracy than GPPs and SML in terms of precipitation estimation over Kenya, except RF. 

### **3.4  Assessment of drought estimation using SPI** 

#### **3.4.1  Temporal evolution** 

The SPI index was estimated at three timescales (SPI-3, SPI-6, and SPI-9) from GPPs, merged products of SML and DML then compared with RGs observation during 2000–2019. These timescales indicate the short (SPI-3), medium (SPI-6), and long-term (SPI-12) drought magnitude, which impacts the water resource availability in that region (Das et al. 2022b). Figure S1 (see the supplementary file) demonstrate the performance of SPI values estimate from GPPs, merged products of SML and DML in the training and testing period with multiple timescales. Generally, the SPI values estimated from DML precipitation products best match observed SPI (Fig· S1a–c). Although, the GPPs estimated SPI values show the worst performance with overestimation and underestimation values. The results from SPI-12 

1 3 

S. Ghosh et al. 

154 



**Fig. 8** Violin charts of four statistical metrics including CC, RMSE, MAE and RAE of the precipitation products and merged products over Kenya during three seasons. Dry season (CC) ( **a** ), Long Rain (cc) ( **b** ), Short Rain (cc) ( **c** ), Dry season (RMSE) ( **d** ), Long Rain 

(RMSE) ( **e** ), Short Rain (RMSE) ( **f** ), Dry season (MAE) ( **g** ), Long Rain (MAE) ( **h** ), Short Rain (MAE) ( **i** ), Dry season (RAE) ( **j** ), Long Rain (RAE) ( **k** ), Short Rain (RAE) ( **l** ) 

indicate the five major long-term drought events starting in 2004 and continuing until 2012, with severe conditions during 2000–2019 (Fig. S1c). While the SPI-12 from GPPs products started in 2004 was underestimated. Furthermore, the SVM and KNN showed a high fluctuation from the RGs SPI, whereas the RF algorithm had a very small fluctuation. 

Figure 10a–l illustrates the scatter plot between observed and predicted SPI at multi-scale (SPI-3, SPI-6, and SPI-12) during the testing period. In general, it is clear that the DML approach and RF algorithm is the best merging method, shows excellent performance in estimating SPI using four GPPs satellite products, and is reliable in estimating drought events. In addition, four error metrics (CC, RMSE, MAE, RAE) provide more accurate statements of short-term and long-term drought during the testing period (Table 7). Among the GPPs products, CHIRPS showed good correlation agreement with RGs observation (CC = 0.59) and low RMSE error (0.9), whereas ERA-5 shows very less correlation (CC = 0.4–0.5) compared with PERSIANN-CDR and IMERG. Although, the RF algorithm estimated datasets 

showing strong correlation (CC = 0.86–0.87) and very less error (RMSE = 0.54, MAE = 0.7, RAE = 0.45) compared to the other three ML algorithms (SVM, KNN, GBM). However, DML approach datasets have the ability to capture drought events multiple time-sale at the regional level. Moreover, the lowest MAE values of the DML algorithm revealed that the error is negligible for short- and long-term drought monitoring (Table 7). Previous studies also revealed that hybrid ML models could reduce drought estimation errors. Such as Alizadeh and Nikoo (2018) reported that the hybrid ML model had higher performance  (R<sup>2</sup> = 95%) than the individual ML approach and was effective for drought estimation in Fars province, Iran. Similarly, Citakoglu and Coşkun (2022) also reported that the hybrid ML models show high performance  (R<sup>2</sup> = 0.95) for estimating the shortterm drought events (SPI-3) in Turkey. 

Table 8 represents the severe drought events at multiple timescales (SPI-3, SPI-6, and SPI-12) based on RGs, GPPs, SML, and DML products during the training and testing period. Among the GPPs products, PERSIANN-CDR and ERA-5 estimated short-term (SPI-3) severe drought events 

1 3 

Machine learning algorithms for merging satellite‑based precipitation products and their… 

155 



**Fig. 9** Spatial distribution of annual precipitation of four GPPs products, four SML merged products and four DML merged products. CRU ( **a** ), CHIRPS ( **b** ), IMERG ( **c** ), PERSIANN-CDR ( **d** ), ERA-5 

( **e** ), RF ( **f** ), SVM ( **g** ), KNN ( **h** ), GBM ( **i** ), RF-RF ( **j** ), RF-SVM ( **k** ), RF-KNN ( **l** ), RF-GBM ( **m** ) 

were overestimated during the testing period, while CHIRPS and IMERG perfectly captured drought events with RGs observation. The SML and DML merged estimated drought events were underestimated during the testing period, except for SVM and RF-RF. For medium- and long-term drought (SPI-6 and SPI-12) events, except RF, all 12 precipitationestimated drought events were overestimated. However, RF and DML estimated drought events show the best performance for capturing the drought events. In addition, RF, RFSVM, and RF-KNN identify the long-term drought events (SPI-12) during the training and testing period (Table 8). 

#### **3.4.2  Spatial evolution** 

A short-term (SPI-3) drought event has been selected to evaluate the spatial distribution of GPPs, SML, and DML estimated products against RGs observation in the dry season of 2011 across Kenya and presented in Fig. 11a–m. In 

general, most of the regions in Kenya witnessed moderate drought in the dry season of 2011, whereas the western and northeastern regions had severe drought conditions. Among the GPPs products, CHIRPS and IMERG have failed to capture the drought events and show normal conditions in most regions (Figs. 11b, c). In addition, PERSIANN-CDR and ERA-5 could not capture the drought event against RGs observation (11d and 11e). The RF has similar spatial results and is suitable for capturing regional drought events (Fig. 11f). In contrast, RF-RF and RF-SVM have some overestimated values in the northern region (Fig. 11j, k). Among the SML estimated products, SVM, KNN, and GBM have high overestimated SPI-3 values in the country's northern region and capture extreme drought conditions (Fig. 11g–i). Although, low accuracy has been identified in high-altitude regions for DML products, especially in the southwestern region (Fig. 11j–m). However, DML and RF estimated SPI 

1 3 

S. Ghosh et al. 

156 



**Fig. 10** Scatter plot of SPI-3, SPI-6 and SPI-12 generated form four GPPs products, four SML merged products and four DML merged products during testing period. CHIRPS ( **a** ), IMERG ( **b** ), PER- 

SIANN-CDR ( **c** ), ERA-5 ( **d** ), RF ( **e** ), SVM ( **f** ), KNN ( **g** ), GBM ( **h** ), RF-RF ( **i** ), RF-SVM ( **j** ), RF-KNN ( **k** ), RF-GBM ( **l** ) 

values give more accuracy than GPPs products in most regions and are suitable for drought monitoring. 

#### **3.4.3  Basin‑wise evaluation** 

This study considers the five major river basins, which include the Lake Victoria Basin (LVB), Athi River Basin (ARB), Tana River Bain (TRB), Ewaso Ngiro Basin (ENB), and Rift Valley Basin (RVB) in Kenya for further evaluate the reliability of GPPs, SML, and DML products for drought monitoring. Therefore, Fig. 12a–e illustrates the radar diagram between observed and predicted SPI-3 during the testing period based on four error metrics. The results indicate that the DML approach has the best performance (CC = 0.67) and reduces the error (RMSE = 0.7, MAE = 0.57, RAE = 0.73) than SML products for estimating SPI-3 in all of the river basins of Kenya (Figure a-e). At the 

same time, the GPPs products performed worst for estimating short-term drought (SPI-3) for all the river basins, such that CC = 0.38, RMSE = 1.05, MAE = 0.8, and RAE = 1. Among the river basin, the LVB and ARB (Fig. 12a, b) show higher accuracy for all the twelve precipitation estimates compared to the other three river basins (TRB, ENB, RVB) (Fig. 12c–e). The GPPs and SML products show very low accuracy (CC = 0.28, RMSE = 1.12, MAE = 0.9, RAE = 1.2) for calculating SPI-3 over the ENB, except RF (CC = 0.6, RMSE = 0.9). The DML approach improved the precipitation estimates and had high accuracy (CC = 0.5, RMSE = 1, MAE = 0.7, RAE = 1) for estimating the drought events in ENB. The low accuracy of these three river basins is due to the less RGs observation. However, the DML approaches significantly improved the precipitation estimates for monitoring the drought events compared to the individual SML and GPPs products in all the river basins of Kenya. 

1 3 

Machine learning algorithms for merging satellite‑based precipitation products and their… 

157 

**Table 7** Performance assessment of GPPs, SML, and DML estimated SPI during the testing period 

||CHIRPS|IMERG|PER-<br>SIANN-<br>CDR|ERA5|RF|SVM|KNN|GBM|RF-RF|RF-SVM|RF-KNN|RF-GBM|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|SPI-3|||||||||||||
|CC|0.59|0.55|0.58|0.51|0.86|0.62|0.66|0.65|0.68|0.75|0.78|0.74|
|RMSE|0.93|1.00|1.05|1.07|0.54|0.90|0.87|0.87|0.83|0.74|0.69|0.75|
|MAE|0.64|0.70|0.76|0.77|0.37|0.62|0.63|0.60|0.60|0.50|0.49|0.52|
|RAE|0.79|0.86|0.94|0.95|0.45|0.76|0.78|0.74|0.74|0.62|0.60|0.64|
|SPI-6|||||||||||||
|CC|0.60|0.56|0.65|0.52|0.86|0.64|0.69|0.70|0.71|0.76|0.80|0.76|
|RMSE|0.92|1.02|1.04|1.07|0.53|0.89|0.84|0.82|0.80|0.72|0.66|0.72|
|MAE|0.67|0.73|0.75|0.75|0.38|0.62|0.61|0.55|0.56|0.51|0.47|0.51|
|RAE|0.81|0.73|0.91|0.91|0.45|0.75|0.74|0.67|0.68|0.61|0.57|0.62|
|SPI-12|||||||||||||
|CC|0.59|0.52|0.63|0.41|0.87|0.59|0.68|0.70|0.70|0.75|0.81|0.76|
|RMSE|0.85|0.99|1.05|1.11|0.47|0.88|0.80|0.76|0.77|0.67|0.61|0.68|
|MAE|0.63|0.72|0.76|0.79|0.34|0.65|0.59|0.55|0.55|0.50|0.44|0.50|
|RAE|0.89|1.02|1.08|1.12|0.49|0.92|0.84|0.78|0.79|0.70|0.63|0.71|



**Table 8** Number of severe drought months during the training and testing period 

|Datasets|Training|||Testing|||
|---|---|---|---|---|---|---|
||SPI3|SPI6|SPI12|SPI3|SPI6|SPI12|
|CRUTS|27|32|30|7|2|0|
|CHIRPS|26|27|27|7|8|3|
|IMERG|25|25|26|7|11|10|
|PERSIANN -CDR|18|22|28|11|10|13|
|ERA-5|27|25|24|9|7|10|
|RF|30|32|37|6|3|0|
|SVM|28|26|33|7|8|6|
|KNN|31|28|37|6|9|7|
|GBM|23|28|38|6|9|5|
|RF-RF|28|28|35|7|9|6|
|RF-SVM|28|28|35|5|7|2|
|RF—KNN|28|27|36|4|6|2|
|RF—GBM|28|28|36|4|7|3|



## **4  Discussion** 

This study demonstrates the reliability and accuracy of DML algorithms for merging global precipitation products and compares them with traditional ML approaches over complex regions of Kenya. The results show that the DML technique considerably reduces the random error of each GPPs and SML dataset. The performance of GPPs products in the study region is consistent with other studies (Ayugi et al. 2019; Macharia et al. 2020). It is notable that the RF approach has achieved high accuracy in terms of low systematic error in precipitation estimates. Compared to a study 

using a DML algorithm to merge GPPs products over China (Zhang et al _._ 2021a, b), our results provide higher accuracy for precipitation estimation with  R<sup>2</sup> scores of 0.9. In addition, the accuracy of precipitation estimates is influenced by the rain gauge density over the studied region. The high rain gauge density (southwest part) will capture precipitation patterns from the rain-gauge observation, GPPs, SML, and DML datasets. In contrast, the low rain gauge density (northwest and northeast part) represents poor performance, as shown in Figs. 4, 5, 6 and 7. Although, the newly merged products (SML and DML) have improved the precipitation estimates over the low rain-gauge density region compared 

1 3 

S. Ghosh et al. 

158 



**Fig. 11** variations of multiscale SPI from 2000 to 2019 computed from observed, GPPs, SML and DML precipitation products. CRU ( **a** ), CHIRPS ( **b** ), IMERG ( **c** ), PERSIANN-CDR ( **d** ), ERA-5 ( **e** ), RF 

( **f** ), SVM ( **g** ), KNN ( **h** ), GBM ( **i** ), RF-RF ( **j** ), RF-SVM ( **k** ), RF-KNN ( **l** ), RF-GBM ( **m** ) 

to individual GPPs datasets. However, the rain gauge density depends on the climatic and topographic features and varies from region to region. This result shows the effectiveness of the ML algorithm for accurate precipitation estimates over Kenya. This study also demonstrates that the DML and RF algorithm performs better than GPPs products on a regional scale and is a better alternative precipitation source. 

In recent years, previous studies have demonstrated that the various ML models can effectively merge precipitation estimates and accurately estimate drought events (Alizadeh and Nikoo 2018; Prodhan et al. 2022). Such as Rahman et al. (2021) revealed that merging products from the ML approach gives higher performance than individual satellite precipitation products for computing drought events. Similarly, Prodhan et al. (2022) found that the machine learning algorithm archived high accuracy, robustness, and effectiveness for estimating drought events. This study also indicated that the ML approach was satisfactory compared to GPPs 

datasets. The spatial and temporal pattern of SPI estimated from the GPPs products are not similar to the RGs observation, which means that the GPPs datasets are unable to capture the accurate drought events over Kenya. Our results show that the GPPs products overestimated or underestimated the SPI values, and similar results were reported by Das et al. (2022a, b). Also, we found that the individual SML products reported an overestimated SPI value, which did not show a satisfactory result. The DML products reproduce the spatial and temporal pattern of drought events well, especially the RF-SVM and RF-KNN merging approaches. Therefore, this study recommended using the DML algorithm for merging precipitation products for accurate drought monitoring. 

The people in Kenya were witnessing several droughts, and sparsely distributed rain gauges created a problem for capturing these drought events and water resource management. Therefore, this study finds an alternative precipitation 

1 3 

Machine learning algorithms for merging satellite‑based precipitation products and their… 

159 



**Fig. 12** Radar diagram of four statistical metrics, including CC, RMSE, MAE, and RAE of the precipitation products and merged products over five major river basins in Kenya. Lake Victoria Basin 

( **a** ), Athi River Basin ( **b** ), Tana River Basin ( **c** ), Ewaso Ngiro Basin ( **d** ), Rift Valley Basin ( **e** ) 

estimate to detect drought events. The major drought events were found in the year 2001, 2003, 2005, 2006, 2008, 2009, 2010, 2011, 2015, and 2018 using SPI-3, SPI-6, and SPI-12. Similar drought events were identified by (Mutsotso et al. 

2018; Ayugi et al. 2020). However, our results revealed that the DML algorithms performed better in identifying shortterm drought events (SPI-3) than GPPs and SML from 2000 to 2019. In addition, the RF, RF, RF-SVM, and RF-KNN 

1 3 

S. Ghosh et al. 

160 

algorithms perfectly capture the long-term drought (SPI-12) with the lowest RMSE and MAE error over Kenya, East Africa. Moreover, this study identified suitable precipitation estimates to capture the drought events in East Africa, which are utilized for water resource management in this region. 

## **5  Conclusion** 

This study applied four SML and DML approaches for merging multiple GPPs products (i.e., CHIRPS, IMERG, PERSIANN-CDR, and ERA-5) and RGs observation for drought monitoring from Kenya from 2000 to 2019. The RF classification model was used with a regression model of RF, SVM, KNN, and GBM, and developed four DML approaches, including RF-RF, RF-SVM, RF-KNN, and RF-GBM. This study compares four GPPs, SML (i.e., RF, SVM, KNN, and GBM) and DML (i.e., RF-RF, RF-SVM, RF-KNN, and RF-GBM) merged products to find an alternative option of precipitation estimates. The results indicate that the RF, RF-SVM, RF-KNN, and RF-GBM algorithms archive excellent performance (CC = 0.8 – 0.9) compared to other SML and GPPs products and capture major drought events using SPI-3. SP-6 and SPI-12. Although, these algorithms identified drought events with some overestimated and underestimated values, which are negligible for drought monitoring and accepted with the lowest RMSE error. In contrast, GPP products have shown less accuracy (CC = 0.4–0.7) with high RMSE error for SPI at multiple scales (i.e., SPI-3, SPI-6, and SPI-12). Therefore, this study recommended using DML approaches for drought monitoring then SML and other GPPs products. However, the CHIRPS and PERSIANN-CDR take time for error correction and are only suitable for historical drought assessment. These results provide information on recent drought events and alternative sources of precipitation to water resource managers and policymakers. 

Moreover, other climatic predictors, such as cloud properties and soil moisture, need to consider in future studies as they provide important information for precipitation estimates which is also stated by Zhang et al _._ (2021a; b). In addition, it will be valuable for considering all possible sensors and an environmental platform for assessing the ecological changes induced by human activity, creating a new boundary between data science and environmental sensing for drought disaster monitoring (Prodhan et al. 2022). The major contribution of this study is to introduce two novel DML approaches to merged GPPs products and tested over Kenya. As far as our knowledge, this study is the first attempt to use this merging approach for drought assessment in Kenya and compare it with GPPs products. 

**Supplementary Information** The online version contains supplementary material available at https:// doi. org/ 10. 1007/ s00382- 023- 06893-6. 

**Author contributions** SG, JL, and PD designed the paper. SG conducted the data processing and statistical analysis and wrote the paper. PD and JL made great efforts in writing and figure optimization. ZZ made a great effort for editing the manuscript. All the authors contributed to the paper. All authors have read and agreed to the publication of the present version of the manuscript. 

**Funding** This research received no specific grant from any funding agency. 

**Data availability** Publicly available datasets were analyzed in this study. This data can be found here: https:// www. chc. ucsb. edu/ data/ chirps, https:// sites. uea. ac. uk/ cru/ data https:// www. ecmwf. int/ en/ forec asts/ datas ets/ reana lysis- datas ets/ era- inter im, https:// disc. gsfc. nasa. gov/, and https:// chrsd ata. eng. uci. edu/. Also, Derived data supporting the finding of this study are available from the corresponding author on request. 

### **Declarations** 

**Conflict of interest** No potential conflict of interest was reported by the author(s). 

**Ethical Approval** All the work complies with Ethical standards. 

**Consent of Participate** Not applicable. 

## **References** 

- Ahmed K, Sachindra DA, Shahid S, Iqbal Z, Nawaz N, Khan N (2020) Multi-model ensemble predictions of precipitation and temperature using machine learning algorithms. Atmos Rese 236:104806. https:// doi. org/ 10. 1016/j. atmos res. 2019. 104806 

- Akinci H (2022) Assessment of rainfall-induced landslide susceptibility in Artvin, Turkey using machine learning techniques. J Afr Earth Sci 191:104535. https:// doi. org/ 10. 1016/j. jafre arsci. 2022. 104535 

- Alizadeh MR, Nikoo MR (2018) A fusion-based methodology for meteorological drought estimation using remote sensing data. Remote Sens Environ 211:229–247. https:// doi. org/ 10. 1016/j. rse. 2018. 04. 001 

- Ashouri H, Hsu KL, Sorooshian S, Braithwaite DK, Knapp KR, Cecil LD, Nelson BR, Prat OP (2015) PERSIANN-CDR: daily precipitation climate data record from multisatellite observations for hydrological and climate studies. Bull Am Meteorol Soc 96(1):197–210. https:// doi. org/ 10. 1175/ BAMS-D- 13- 00068.1 

- Atiah WA, Amekudzi LK, Aryee JNA, Preko K, Danuor SK (2020) Validation of satellite and merged rainfall data over Ghana, West Africa. Atmosphere 11(8):859. https:// doi. org/ 10. 3390/ atmos 11080 859 

- Ayugi B, Tan G, Ullah W, Boiyo R, Ongoma V (2019) Inter-comparison of remotely sensed precipitation datasets over Kenya during 1998–2016. Atmos Res 225(1):96–109. https:// doi. org/ 10. 1016/j. atmos res. 2019. 03. 032 

- Ayugi B, Tan G, Niu R, Dong Z, Ojara M, Mumo L, Babaousmail H, Ongoma V (2020) Evaluation of Meteorological Drought and Flood Scenarios over Kenya, East Africa. Atmosphere 11(3):307. https:// doi. org/ 10. 3390/ atmos 11030 307 

- Barrett AB, Duivenvoorden S, Salakpi EE, Muthoka JM, Mwangi J, Oliver S, Rowhani P (2020) Forecasting vegetation condition for 

1 3 

Machine learning algorithms for merging satellite‑based precipitation products and their… 

161 

   - drought early warning systems in pastoral communities in Kenya. Remote Sens Environ 248:111886. https:// doi. org/ 10. 1016/j. rse. 2020. 111886 

- Behrangi A, Wen Y (2017) On the spatial and temporal sampling errors of remotely sensed precipitation products. Remote Sens 9(11):1127. https:// doi. org/ 10. 3390/ rs911 1127 

- Bouaziz M, Medhioub E, Csaplovisc E (2021) A machine learning model for drought tracking and forecasting using remote precipitation data and a standardized precipitation index from arid regions. J Arid Environ 189:104478. https:// doi. org/ 10. 1016/j. jarid env. 2021. 104478 

- Breiman L (2001) Random Forest. Mach Learn 45:5–32 

- Chen S, Xiong L, Ma Q et al (2020) Improving daily spatial precipitation estimates by merging gauge observation with multiple satellite-based precipitation products based on the geographically weighted ridge regression method. J Hydrol 589:125156. https:// doi. org/ 10. 1016/j. jhydr ol. 2020. 125156 

- Chen S, Li Q, Zhong W, Wang R, Chen D, Pan S (2022) Improved monitoring and assessment of meteorological drought based on multi-source fused precipitation data. Int J Environ Res Public Health 19(3):1542. https:// doi. org/ 10. 3390/ ijerp h1903 1542 

- Citakoglu H, Coskun O (2022) Comparison of hybrid machine learning methods for the prediction of short-term meteorological droughts of Sakarya Meteorological Station in Turkey. Environ Sci Pollut Res 29:75487–75511. https:// doi. org/ 10. 1007/ s11356- 022- 21083-3 

- Cortes C, Vapnik V (1995) Support-vector networks. Mach Learn 20(3):273–297. https:// doi. org/ 10. 1007/ BF009 94018 

- Das P, Zhang Z, Ren H (2022a) Evaluation of four bias correction methods and random forest model for climate change projection in the Mara River Basin, East Africa. J Water Clim Change 13(4):1900. https:// doi. org/ 10. 2166/ wcc. 2022. 299 

- Das P, Zhang Z, Ren H (2022b) Evaluating the accuracy of two satellite-based Quantitative Precipitation Estimation products and their application for meteorological drought monitoring over the Lake Victoria Basin, East Africa. Geo-Spatial Inf Sci 25(3):500–518. https:// doi. org/ 10. 1080/ 10095 020. 2022. 20547 31 

- de Brito CS, da Silva RM, Santos CAG, Neto RMB, Coelho VHR (2021) Monitoring meteorological drought in a semi-arid region using two long-term satellite-estimated rainfall datasets: a case study of the Piranhas River Basin, Northeastern Brazil. Atmos Res 250:105380. https:// doi. org/ 10. 1016/j. atmos res. 2020. 105380 

- Dikici M (2020) Drought Analysis with Different Indices for the Asi Basin (Turkey). Sci Rep 10(1):20739. https:// doi. org/ 10. 1038/ s41598- 020- 77827-z 

- Ebrahimi-Khusfi Z, Dargahian F, Nafarzadegan AR (2022) Predicting the dust events frequency around a degraded ecosystem and determining the contribution of their controlling factors using gradient boosting-based approaches and game theory. Environ Sci Pollut Res 29(24):36655–36673. https:// doi. org/ 10. 1007/ s11356- 021- 17265-0 

- Fan Z, Li W, Jiang Q, Sun W, Wen J, Gao J (2021) A comparative study of four merging approaches for regional precipitation estimation. IEEE Access 9:33625–33637. https:// doi. org/ 10. 1109/ ACCESS. 2021. 30570 57 

- Flah M, Nunez I, Ben Chaabene W, Nehdi ML (2021) Machine learning algorithms in civil structural health monitoring: a systematic review. Arch Computat Methods Eng 28:2621–2643. https:// doi. org/ 10. 1007/ s11831- 020- 09471-9 

- Friedman JH (2001) Greedy function approximation: a gradient boosting machine. Ann Stat. https:// doi. org/ 10. 1214/ aos/ 10132 03451 

- Funk C, Peterson P, Landsfeld M, Pedreros D, Verdin J, Shukla S, Husak G, Rowland J, Harrison L, Hoell A (2015) The climate hazards infrared precipitation with stations—a new environmental record for monitoring extremes. Sci Data 2(9):150066 

- Guo H, Bao A, Liu T, Chen S, Ndayisaba F (2016) Evaluation of PERSIANN-CDR for meteorological drought monitoring over China. Remote Sens 8(5):379. https:// doi. org/ 10. 3390/ rs805 0379 

- Harris I, Osborn TJ, Jones P, Lister D (2020) Version 4 of the CRU TS monthly high-resolution gridded multivariate climate dataset. Sci Data 7(1):109. https:// doi. org/ 10. 1038/ s41597- 020- 0453-3 

- Hastenrath S (2001) Variations of East African climate during the past two centuries. Clim Change 50:209–217 

- Hersbach H, Bell B, Berrisford P, Hirahara S, Horányi A, MuñozSabater J, Nicolas J, Peubey C, Radu R, Schepers D, Simmons A (2020) The ERA5 global reanalysis. Q J R Meteorol Soc 146(730):1999–2049. https:// doi. org/ 10. 1002/ qj. 3803 

- Huang M, Lin R, Huang S, Xing T (2017) A novel approach for precipitation forecast via improved K-nearest neighbor algorithm. Adv Eng Inform 33:89–95. https:// doi. org/ 10. 1016/j. aei. 2017. 05. 003 

- Huffman G, Bolvin D, Braithwaite D, Hsu K, Joyce R, Xie P (2014) Integrated Multi-satellitE Retrievals for GPM (IMERG), version 4.4. NASA’s Precipitation Processing Center. ftp:// arthu rhou. pps. eosdis. nasa. gov/ gpmda ta/. Accessed 31 Mar 2015 

- Huffman GJ, Bolvin DT, Nelkin EJ, Tan J (2019) Integrated MultisatellitE Retrievals for GPM (IMERG) Technical Documentation. https:// docse rver. gesdi sc. eosdis. nasa. gov/ public/ proje ct/ GPM/ IMERG_ doc. 06. pdf. Accessed 18 Mar 2019 

- Jiang Q, Li W, Fan Z, He X, Sun W, Chen S, Wen J, Gao J, Wang J (2021) Evaluation of the ERA5 reanalysis precipitation dataset over Chinese Mainland. J Hydrol 595:125660. https:// doi. org/ 10. 1016/j. jhydr ol. 2020. 125660 

- Jose DM, Vincent AM, Dwarakish GS (2022) Improving multiple model ensemble predictions of daily precipitation and temperature through machine learning techniques. Sci Rep 12(1):4678. https:// doi. org/ 10. 1038/ s41598- 022- 08786-w 

- Kolluru V, Kolluru S, Wagle N, Acharya TD (2020) Secondary precipitation estimate merging using machine learning: development and evaluation over Krishna River Basin, India. Remote Sens 12(18):3013. https:// doi. org/ 10. 3390/ rs121 83013 

- Lai C, Zhong R, Wang Z, Wu X, Chen X, Wang P, Lian Y (2019) Monitoring hydrological drought using long-term satellite-based precipitation data. Sci Total Environ 649:1198–1208. https:// doi. org/ 10. 1016/j. scito tenv. 2018. 08. 245 

- Li Q, Han X, Liu Z, He P, Shi P, Chen Q, Du F (2022) A novel information changing rate and conditional mutual information-based input feature selection method for artificial intelligence drought prediction models. Clim Dyn 58(11–12):3405–3425. https:// doi. org/ 10. 1007/ s00382- 021- 06104-0 

- Liakos K, Busato P, Moshou D et al (2018) Machine learning in agriculture: a review. Sensors 18:2674. https:// doi. org/ 10. 3390/ s1808 2674 

- Lin Q, Peng T, Wu Z, Guo J, Chang W, Xu Z (2022) Performance evaluation, error decomposition and Tree-based Machine Learning error correction of GPM IMERG and TRMM 3B42 products in the Three Gorges Reservoir Area. Atmos Res 268:105988. https:// doi. org/ 10. 1016/j. atmos res. 2021. 105988 

- Liu C, Yang C, Yang Q, Wang J (2021) Spatiotemporal drought analysis by the standardized precipitation index (SPI) and standardized precipitation evapotranspiration index (SPEI) in Sichuan Province. China Sci Rep 11(1):1280. https:// doi. org/ 10. 1038/ s41598- 020- 80527-3 

- Macharia JM, Ngetich FK, Shisanya CA (2020) Agricultural and forest meteorology comparison of satellite remote sensing derived precipitation estimates and observed data in Kenya. Agric For Meteorol 284:107875. https:// doi. org/ 10. 1016/j. agrfo rmet. 2019. 107875 

- Malik A, Saggi MK, Rehman S, Sajjad H, Inyurt S, Bhatia AS, Farooque AA, Oudah AY, Yaseen ZM (2022) Deep learning versus gradient boosting machine for pan evaporation prediction. Eng 

1 3 

S. Ghosh et al. 

162 

Appl Comput Fluid Mech 16(1):570–587. https:// doi. org/ 10. 1080/ 19942 060. 2022. 20272 73 

- Mayor Y, Tereshchenko I, Fonseca-Hernández M, Pantoja D, Montes J (2017) Evaluation of error in IMERG precipitation estimates under different topographic conditions and temporal scales over Mexico. Remote Sens 9(5):503. https:// doi. org/ 10. 3390/ rs905 0503 

- McKee TB, Doesken NJ, Kleist J (1993) The relationship of drought frequency and duration to time scales. In: The 8th Conference on Applied Climatology, Anaheim, January 17–22 

- Mehdizadeh S (2020) Using AR, MA, and ARMA time series models to improve the performance of MARS and KNN approaches in monthly precipitation modeling under limited climatic data. Water Resour Manage 34(1):263–282. https:// doi. org/ 10. 1007/ s11269- 019- 02442-1 

- Mehr AD, Nourani V, Khosrowshahi VK, Ghorbani MA (2019) A hybrid support vector regression–firefly model for monthly rainfall forecasting. Int J Environ Sci Technol 16:335–346. https:// doi. org/ 10. 1007/ s13762- 018- 1674-2 

- Miller S, Mishra V, Ellenburg WL, Adams E, Roberts J, Limaye A, Griffin R (2021) Analysis of a Short-Term and a Seasonal Precipitation Forecast over Kenya. Atmosphere 12(11):1371. https:// doi. org/ 10. 3390/ atmos 12111 371 

- Mohammadi M, Farajpour A, Rastgoo A (2023) Coriolis effects on the thermo-mechanical vibration analysis of the rotating multilayer piezoelectric nanobeam. Acta Mechanica 234(2):751–774 

- Mohseni F, Kiani Sadr M, Eslamian S, Areffian A, Khoshfetrat A (2021) Spatial and temporal monitoring of drought conditions using the satellite rainfall estimates and remote sensing optical and thermal measurements. Adv Space Res 67(12):3942–3959. https:// doi. org/ 10. 1016/j. asr. 2021. 02. 017 

- Mokhtar A, Jalali M, He H, Al-Ansari N, Elbeltagi A, Alsafadi K, Abdo HG, Sammen SS, Gyasi-Agyei Y, Rodrigo-Comino J (2021) Estimation of SPEI meteorological drought using machine learning algorithms. IEEE Access 9:65503–65523 

- Monego VS, Anochi JA, de Campos Velho HF (2022) South America seasonal precipitation prediction by gradient-boosting machinelearning approach. Atmosphere 13(2):243. https:// doi. org/ 10. 3390/ atmos 13020 243 

- Mutsotso RB, Sichangi AW, Makokha GO (2018) Spatio-temporal drought characterization in Kenya from 1987 to 2016. Adv Remote Sens 07(02):125–143. https:// doi. org/ 10. 4236/ ars. 2018. 72009 

- Ochieng P, Nyandega I, Wambua B (2022) Spatial-temporal analysis of historical and projected drought events over Isiolo County, Kenya. Theor Appl Climatol 148:531–550. https:// doi. org/ 10. 1007/ s00704- 022- 03953-5 

- Ongoma V, Chen H, Omony GW (2018) Variability of extreme weather events over the equatorial East Africa, a case study of rainfall in Kenya and Uganda. Theor Appl Climatol 131(1–2):295–308. https:// doi. org/ 10. 1007/ s00704- 016- 1973-9 

- Orimoloye IR, Olusola AO, Belle JA et al (2022) Drought disaster monitoring and land use dynamics: identifcation of drought drivers using regression-based algorithms. Nat Hazards 112:1085– 1106. https:// doi. org/ 10. 1007/ s11069- 022- 05219-9 

- Palmer WC (1965) Meteorological drought. Res. Paper No. 45, Weather Bureau, Washington, D.C., p 58 

- Pathak AA, Dodamani BM (2020) Comparison of Meteorological Drought Indices for Different Climatic Regions of an Indian River Basin. Asia-Pac J Atmos Sci 56(4):563–576. https:// doi. org/ 10. 1007/ s13143- 019- 00162-5 

- Peel MC, Finlayson BL, Mcmahon TA (2007) Updated world map of the koppen-geiger climate classification. Hydrol Earth Syst Sci 11:1633–1644 

- Prodhan FA, Zhang J, Pangali Sharma TP, Nanzad L, Zhang D, Seka AM, Ahmed N, Hasan SS, Hoque MZ, Mohana HP (2022) 

Projection of future drought and its impact on simulated crop yield over South Asia using ensemble machine learning approach. Sci Total Environ 807:151029. https:// doi. org/ 10. 1016/j. scito tenv. 2021. 151029 

- Rahman KU, Shang S, Shahid M, Wen Y, Khan Z (2020) Application of a dynamic clustered Bayesian model averaging (DCBA) algorithm for merging multisatellite precipitation products over Pakistan. J Hydrometeorol 21(1):17–37. https:// doi. org/ 10. 1175/ JHM-D- 19- 0087.1 

- Rahman KU, Shang S, Zohaib M (2021) Assessment of merged satellite precipitation datasets in monitoring meteorological drought over Pakistan. Remote Sens 13(9):1662. https:// doi. org/ 10. 3390/ rs130 91662 

- Rehman A, Chandio AA, Hussain I, Jingdong L (2019) Fertilizer consumption, water availability and credit distribution: major factors affecting agricultural productivity in Pakistan. J Saudi Soc Agric Sci 18(3):269–274. https:// doi. org/ 10. 1016/j. jssas. 2017. 08. 002 

- Santos CAG, Brasil Neto RM, Nascimento doSilva daMishraFrade TVMRMMTG (2021) Geospatial drought severity analysis based on PERSIANN-CDR-estimated rainfall data for Odisha state in India (1983–2018). Sci Total Environ 750:141258. https:// doi. org/ 10. 1016/j. scito tenv. 2020. 141258 

- Sattari MT, Apaydin H, Band SS, Mosavi A, Prasad R (2021) Comparative analysis of kernel-based versus ANN and deep learning methods in monthly reference evapotranspiration estimation. Hydrol Earth Syst Sci 25(2):603–618. https:// doi. org/ 10. 5194/ hess- 25- 603- 2021 

- Shobeiri S, Sharafati A, Neshat A (2021) Evaluation of different gridded precipitation products in trend analysis of precipitation features over Iran. Acta Geophys 69:959–974. https:// doi. org/ 10. 1007/ s11600- 021- 00595-5 

- Shrestha NK, Qamer FM, Pedreros D, Murthy MSR, Wahid SM, Shrestha M (2017) Evaluating the Accuracy of Climate Hazard Group (CHG) Satellite Rainfall Estimates for Precipitation-based Drought Monitoring in Koshi Basin, Nepal. J Hydrol Reg Stud 13:138–151. https:// doi. org/ 10. 1016/j. ejrh. 2017. 08. 004 

- Song Z, Xia J, Wang G, She D, Hu C, Hong S (2022) Regionalization of hydrological model parameters using gradient boosting machine. Hydrol Earth Syst Sci 26(2):505–524. https:// doi. org/ 10. 5194/ hess- 26- 505- 2022 

- Taghi Sattari M, Feizi H, Samadianfard S, Falsafian K, Salwana E (2021) Estimation of monthly and seasonal precipitation: A comparative study using data-driven methods versus hybrid approach. Measurement 173:108512. https:// doi. org/ 10. 1016/j. measu rement. 2020. 108512 

- Tan G, Ayugi B, Ngoma H, Ongoma V (2020) Projections of future meteorological drought events under representative concentration pathways (RCPs) of CMIP5 over Kenya, East Africa. Atmos Res 246:105112. https:// doi. org/ 10. 1016/j. atmos res. 2020. 105112 

- Wei W, Zhang J, Zhou J, Zhou L, Xie B, Li C (2021) Monitoring drought dynamics in china using optimized meteorological drought index (OMDI) based on remote sensing data sets. J Environl Manag 292:112733. https:// doi. org/ 10. 1016/j. jenvm an. 2021. 112733 

- WMO (1994) Guide to hydrological practices: data acquisition and processing, analysis, forecasting and other applications, WMO 168. World Meteorological Organization, Geneva 

- Yaseen ZM, Ali M, Sharafati A, Al-Ansari N, Shahid S (2021) Forecasting standardized precipitation index using data intelligence models: regional investigation of Bangladesh. Sci Rep 11(1):3435. https:// doi. org/ 10. 1038/ s41598- 021- 82977-9 

- Yin G, Yoshikane T, Yamamoto K, Kubota T, Yoshimura K (2022) A support vector machine-based method for improving real-time hourly precipitation forecast in Japan. J Hydrol 612:128125. https:// doi. org/ 10. 1016/j. jhydr ol. 2022. 128125 

1 3 

Machine learning algorithms for merging satellite‑based precipitation products and their… 

163 

- Yoosefdoost I, Khashei-Siuki A, Tabari H, Mohammadrezapour O (2022) Runoff simulation under future climate change conditions: performance comparison of data-mining algorithms and conceptual models. Water Resour Manag 36(4):1191–1215. https:// doi. org/ 10. 1007/ s11269- 022- 03068-6 

- Yumnam K, Guntu RK, Rathinasamy M, Agarwal A (2022) Quantilebased bayesian model averaging approach towards merging of precipitation products. J Hydrol 604:14. https:// doi. org/ 10. 1016/j. jhydr ol. 2021. 127206 

- Zandi O, Zahraie B, Nasseri M, Behrangi A (2022) Stacking machine learning models versus a locally weighted linear model to generate high-resolution monthly precipitation over a topographically complex area. Atmos Res 272:106159. https:// doi. org/ 10. 1016/j. atmos res. 2022. 106159 

- Zandi O, Nasseri M, Zahraie B (2023) A locally weighted linear ridge regression framework for spatial interpolation of monthly precipitation over an orographically complex area. Int J Climatol 43:2601–2622. https:// doi. org/ 10. 1002/ joc. 7992 

- Zhang Y, Li Z (2020) Uncertainty analysis of standardized precipitation index due to the effects of probability distributions and parameter errors. Front Earth Sci 8:76. https:// doi. org/ 10. 3389/ feart. 2020. 00076 

- Zhang R, Chen ZY, Xu LJ, Ou CQ (2019) Meteorological drought forecasting based on a statistical model with machine learning techniques in Shaanxi province, China. Sci Total Environ 665(2019):338–346. https:// doi. org/ 10. 1016/j. scito tenv. 2019. 01. 431 

- Zhang L, Li X, Zheng D, Zhang K, Ma Q, Zhao Y, Ge Y (2021a) Merging multiple satellite-based precipitation products and gauge observations using a novel double machine learning approach. 

   - J Hydrol 594:125969. https:// doi. org/ 10. 1016/j. jhydr ol. 2021. 125969 

- Zhang W, Li H, Li Y et al (2021b) Application of deep learning algorithms in geotechnical engineering: a short critical review. Artif Intell Rev 54:5633–5673. https:// doi. org/ 10. 1007/ s10462- 021- 09967- 

- Zhang Z-C, Zeng X-M, Li G, Lu B, Xiao M-Z, Wang B-Z (2022) Summer precipitation forecast using an optimized artificial neural network with a genetic algorithm for Yangtze-Huaihe River Basin, China. Atmosphere 13(6):929. https:// doi. org/ 10. 3390/ atmos 13060 929 

- Zhao H, Ma Y (2019) Evaluating the drought-monitoring utility of four satellite-based quantitative precipitation estimation products at global scale. Remote Sens 11(17):2010. https:// doi. org/ 10. 3390/ rs111 72010 

- Zhong R, Chen X, Lai C, Wang Z, Lian Y, Yu H, Wu X (2019) Drought monitoring utility of satellite-based precipitation products across Mainland China. J Hydrol 568:343–359. https:// doi. org/ 10. 1016/j. jhydr ol. 2018. 10. 072 

**Publisher's Note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law. 

1 3 

Reproduced with permission of copyright owner. Further reproduction prohibited without permission. 

