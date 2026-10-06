





© 2023 The Authors 

Journal of Water and Climate Change Vol 14 No 12, 4729 doi: 10.2166/wcc.2023.386 

# Early crop yield prediction for agricultural drought monitoring using drought indices, remote sensing, and machine learning techniques 

Parthsarthi Pandya * and Narendra Kumar Gontia 

College of Agricultural Engineering and Technology, Junagadh Agricultural University, Junagadh 362001, Gujarat, India *Corresponding author. E-mail: parthsarthi41@gmail.com 



PP, 0000-0002-5253-2987 

#### ABSTRACT 

The unpredictability of crop yield due to severe weather events such as drought and extreme heat continues to be a key worry. The present study evaluated six meteorological and three Landsat satellite-based vegetation drought indices from 1986 to 2019 in the drought-pronesemi-arid Saurashtra region of Gujarat (India). Cotton and groundnut crop yield prediction models were developed using multiple linear regression (MLR), artificial neural network with MLP, and random forest (RF). The models performed crop yield estimation at two timescales, i.e., 75 days after sowing and 105 days after sowing. The standardized precipitation evapotranspiration index/reconnaissance drought index among meteorological drought indices, normalized difference vegetation anomaly index/vegetation condition index, and normalized difference water index anomaly were chosen as best highest correlations with crop yields. The RF-based models were found most efficient in predicting the cotton and groundnut yield of Saurashtra with R<sup>2</sup> ranging from 0.77 to 0.92, Nash–Sutcliffe efficiency ranging from 71 to 90%, and root-mean-square error ranging from 80 to 133 kg/ha for cotton and 299 to 453 kg/ha for groundnut. This study demonstrated the method for making several decisions based on early crop yield prediction including timely drought mitigation measures. 

Key words: agricultural drought, cotton, groundnut, Gujarat, NDVI, random forest 

#### HIGHLIGHTS 

- Standardized precipitation evapotranspiration index/reconnaissance drought index and remote sensing-based indices were chosen as model inputs. 

- Multiple linear regression, artificial neural network–multilayer perception, and random forest techniques were employed for model development. 

- Random forest-based models efficiently predicted early crop yield of cotton and groundnut with R<sup>2</sup> ranging from 0.77 to 0.92. 

- The study established a method to enable better agricultural drought monitoring, mitigation, and early crop yield prediction. 

This is an Open Access article distributed under the terms of the Creative Commons Attribution Licence (CC BY 4.0), which permits copying, adaptation and redistribution, provided the original work is properly cited (http://creativecommons.org/licenses/by/4.0/). 

Downloaded from iwaponline.​com/​jwcc/​article-pdf/​14/​12/​4729/​1349676/​jwc0144729.​pdf by guest 

Journal of Water and Climate Change Vol 14 No 12, 4730 

#### GRAPHICAL ABSTRACT 



## 1. INTRODUCTION 

The uneven spatial and temporal distribution of water causes extreme events such as floods and droughts, which are detrimental to plants, animals, and humans. IPCC (2022) reported that there will be an increase in the frequency, intensity, and severity of droughts and floods in South Asia, and water security will be at risk due to increased temperature extremes and rainfall variability. The combination of remote sensing data, agrarian factors, and machine-learning approaches can help to reduce the socioeconomic effects of crop loss brought on by a natural disaster, such as a flood or a drought, and to organize humanitarian food assistance (Bharadiya et al. 2023). 

Drought is a periodic occurrence, and it is not possible to prevent; however, its effects can be reduced by using science and technology to create drought management plans. Agricultural drought is characterized by insufficient soil moisture for crop growth due to rainfall deficiency, which leads to poor crop health, and ultimately, it lowers crop productivity. Non-availability of a proper drought assessment tool in the drought-affected area is a major bottleneck to evolving better in-season crop management to minimize loss and offer subsequent mitigation and relief measures in drought-affected areas. 

The crop yield is affected by several factors which include technological (agricultural practices, managerial decisions, etc.), biological (diseases, insects, pests, weeds), and environmental (climatic condition, soil fertility, topography, water quality, etc.). Accurate yield prediction requires a fundamental understanding of the functional relationship between yield and these factors. The estimation of drought-induced crop yield and yield anomalies was observed to be a challenging task by several researchers due to the complex relationship between environment and crop yield. The meteorological drought indices and remote sensing-based vegetation indices were proven useful in predicting the consequences of drought on crop yields. Several machine-learning techniques such as multiple linear regression (MLR) for maize, rice, sorghum, soybean, and millet (Chen et al. 2016), random forest (RF) for cotton (Prasad et al. 2021), and comparison of MLR with RF (Jeong et al. 2016) and with artificial neural network (ANN) (Lee et al. 2017; Sayago & Bocco 2018; Gniewko 2019) were attempted, while Bhojani & Bhatt (2018) compared six techniques including Gaussian processes (GP), ANN, Kstar, sequential minimal optimization, model trees, and additive regression for wheat yield prediction. 

The widely used statistical models for crop yield prediction include simple and MLR models. However, statistical models developed based on machine-learning algorithms provide more promising results than traditional linear regression models. The artificial neural network often allows for better analysis results compared to classical statistical methods for crop 

Downloaded from iwaponline.​com/​jwcc/​article-pdf/​14/​12/​4729/​1349676/​jwc0144729.​pdf by guest 

Journal of Water and Climate Change Vol 14 No 12, 4731 

yield estimation (Gniewko 2019). Recently, a non-parametric type of advanced algorithm that works on the principle of ensemble technique, i.e., RF, has started gaining popularity due to high versatility, accuracy, and precision in predicting the results (Belgiu & Drăguţ 2016; Prasad et al. 2021). Several studies have used RF for crop yield prediction of wheat, maize, cotton, potato, oil seed rape, etc. (Jeong et al. 2016; Bouras et al. 2021; Prasad et al. 2021; Dhillon et al. 2023). The increasing availability and variety of global satellite products and the rapid development of new machine-learning algorithms have been explored recently for fast and accurate yield estimates. However, the consistency and reliability of suitable methodologies that provide accurate crop yield outcomes still need to be explored (Dhillon et al. 2023). 

Remote sensing has been instrumental in crop health monitoring and agricultural water management. The utilization of spatial information through remote sensing, facilitated by a diverse array of satellite sensor systems, provides important perspectives for evaluating agricultural drought. In semi-arid environments, water availability is usually the limiting factor for vegetation development and vitality, and hence, the vigor of the vegetation cover is a good indicator of the occurrence and severity of water stress (Belal et al. 2014). In other words, it can be inferred that lack of ‘greenness’ or vigor caused by poor weather conditions forms the basis of using satellite-based drought indices for agricultural drought assessment. Of numerous available satellite-based indices, the normalized difference vegetation index (NDVI) and its derivative-based indices such as the NDVI anomaly index (NAI) and vegetation condition index (VCI), the plant/soil moisture-based normalized difference water index (NDWI), the last surface temperature-based temperature condition index (TCI), and a combination of VCI and TCI, i.e., vegetation health index, are some of the most extensively used agricultural drought indices. (David et al. 2019; Tuvdendorj et al. 2019). Singh et al. (2021) and Bouras et al. (2021) observed that agricultural drought assessment models based on combining data from multiple sources outperformed the models based on a single source of information. 

India has experienced an increase in drought intensity and percentage of area affected by droughts along with the frequent occurrence of multi-year droughts during recent decades (Niranjan et al. 2013; Mallya et al. 2016). Agricultural crop production and the gross domestic product of India are greatly influenced by the performance of monsoon rainfall (Gadgil & Gadgil 2006). Gujarat is a chronic drought-prone state of India with substantial portions of the state being arid and semiarid. The present crop yield reduction estimation process in a drought year compared to a normal year in Gujarat is cumbersome and lengthy involving 25 steps, which results in delays and manipulation in the relief process (Bandyopadhyay et al. 2016). In such cases, final Kharif and Rabi crop estimates will be available after 2–3 months of the harvest. The parts of North Gujarat and Saurashtra have a limited source of alternate irrigation. Falling water tables in these regions have added stress to crops and water supplies (Lunagaria & Sur 2019). Various districts of the Saurashtra region of Gujarat suffer from mild droughts once in 3 years, moderate drought once in 9–10 years, and severe droughts once in 29–44 years (Pandya & Gontia 2023). 

The anatomy of drought needs to be understood at a local scale for near real-time drought management, and the development of a reliable crop yield prediction model is a crucial step toward it. The main aim of the present study was to develop models for early estimation of cotton and groundnut crop yields using machine-learning techniques such as MLR, artificial neural network, and RF by combining inputs as suitable meteorological and remote sensing-based indices for the Saurashtra region of Gujarat, India. This study aimed to support policymakers, farmers, scientists, development agencies, and extension workers to take appropriate monitoring and mitigation measures against agricultural droughts. 

## 2. STUDY AREA AND DATA USED 

### 2.1. Study area 

The study area includes the Saurashtra region of Gujarat located at the extreme western part of India (Figure 1). The region has 6.49 Mha geographical area and 3.91 Mha net sown area including 1.78 Mha irrigated area. A significant proportion of the total irrigated area, specifically 73%, relies on groundwater for irrigation (Anonymous 2020, Department of Agriculture and Farmers’ Welfare, Government of Gujarat). Hence, the seasonal rainfall received during the southwest monsoon (June– September) holds considerable importance in influencing crop production. 

A major part of the region falls under two agro-climatic zones, i.e., North Saurashtra agro-climatic zone (NSAZ) covering Amreli, Jamnagar, DevbhumiDwarka, and parts of Rajkot, Surendranagar, Bhavnagar, Botad, Morbi districts, as well as south Saurashtra agro-climatic zone (SSAZ) covering Junagadh, GirSomnath, and Porbandar districts. The average annual rainfall of the NSAZ ranges from 400 to 700 mm, while for SSAZ, it ranges from 645 to 700 mm (Anonymous 2020, Department of Agriculture and Farmers’ Welfare, Government of Gujarat). Cotton and groundnut are the main Kharif crops of the region. 

Downloaded from iwaponline.​com/​jwcc/​article-pdf/​14/​12/​4729/​1349676/​jwc0144729.​pdf by guest 

Journal of Water and Climate Change Vol 14 No 12, 4732 



Figure 1 | Location of the study area (Saurashtra) and rain gauge stations. 

The Kharif crops are sown generally in the middle of June depending on the commencement of rainfall. The cropping period of cotton is 150–180 days. The first seed to boll formation is the most critical stage with respect to water requirement followed by ball formation to ball maturity. The total water requirement of cotton ranges between 700 and 1,000 mm. The crop growth period for groundnut is 120 days with flowering, peg penetration, and pod development being critical stages with respect to water requirement. The water requirement of groundnut ranges between 400 and 600 mm. 

The flowchart of the methodology adopted in the study is depicted in Figure 2 and described in subsequent sections. 

### 2.2. Data used 

The daily rainfall, monthly minimum and maximum temperature, district-scale cotton and groundnut crop yields, and Landsat and Sentinel-2 satellite data were used in the study. The specifics regarding the data period, spatial scale, and data sources are summarized in Table 1. 

The Landsat images to derive vegetation indices are a collection of high-resolution satellite imagery, with a spatial resolution of 30 m, provided in a standardized, orthorectified format (Osman et al. 2014; Ghaleb et al. 2015). The surface reflectance from the Landsat program is already preprocessed, and it is a level 2 product, and thus, it eliminates the need for any further atmospheric correction. The Landsat products have an advantage over other satellites as data are free and have excellent search and browse facilities; data products undergo numerous calibrations, preprocessing, and normalizations (e.g., atmospheric correction); and data are available as processed products (e.g., reflectance). The year 1988 was a data-deficit year for the region, and no data sources were found available; hence, it was excluded from the study to estimate vegetation indices. Therefore, 33 years of data from 1986 to 2019 (excluding 1988) were used for computing remote sensing-based vegetation indices. 

Downloaded from iwaponline.​com/​jwcc/​article-pdf/​14/​12/​4729/​1349676/​jwc0144729.​pdf by guest 

Journal of Water and Climate Change Vol 14 No 12, 4733 



Figure 2 | Flowchart of methodology adopted. 

## 3. METHODOLOGY 

### 3.1. Estimation of drought indices 

The meteorological drought analysis was carried out using six indices including four rainfall-based indices, i.e., standardized precipitation index (SPI) (McKee et al. 1993), rainfall anomaly index (RAI) (Van Rooy 1965), drought area index (DAI) (Bhalme & Mooley 1980), and decile index (DI) (Gibbs & Maher 1967), and two rainfall and potential evapotranspiration-based indices, i.e., standardized precipitation evapotranspiration index (SPEI) (Vicente-Serrano et al. 2010) and reconnaissance drought index (RDI) (Tsakiris & Vangelis 2005). The study used three vegetation-based indices out of which two indices, NAI (Anyamba et al. 2001) and VCI (Kogan (1995), are derivative indices based on the NDVI and normalized difference water index anomaly (NDWIA) (Gao 1996), which is based on the NDWI. The computation procedure for these drought indices is given in Appendix A. All these multi-spectral datasets in the form of raster images were processed in QGIS open-source environment for the computation of vegetation indices. Crop masking was performed to remove the non-agricultural areas from the estimations using crops class (Band 5) of the ESRI (Environmental Systems Research Institute) land cover of 10 m � 10 m resolution (vector separated) based on Sentinel-2 imagery for the year 2020. 

Table 1 | Details of data used in the study 

|Type of Data|Duration|Spatial resolution|Source|
|---|---|---|---|
|Daily rainfall|1980–2019|36 stations|• State Water Data Centre Gandhinagar, Government of Gujarat<br>• IMD, Pune<br>• Various stations of Junagadh Agricultural University|
|Mean monthly minimum and<br>maximum temperature|1980–2019|36 stations|NASA/POWER, National Center for Environmental Prediction<br>(NCEP) global reanalysis data.https://power.larc.nasa.gov/|
|Yearly crop yield data|1980–2019|District average|Directorate of Agriculture, Government of Gujarat|
|Yearly/late September<br>satellite data|1986–2019|30 m�30 m|Landsat 5, Landsat 7, and Landsat 8 Thematic Mapper (TM).<br>https://earthexplorer.usgs.gov/|



Downloaded from iwaponline.​com/​jwcc/​article-pdf/​14/​12/​4729/​1349676/​jwc0144729.​pdf by guest 

Journal of Water and Climate Change Vol 14 No 12, 4734 

### 3.2. Development of crop yield prediction models 

The crop yield prediction models at the scale of the climatic zone are observed to be appropriate to predict crop yields (David et al. 2019). As crop yield data were available at the district scale, the climatic zone-wise crop yield prediction models were developed using district-scale data as inputs. The machine-learning techniques of MLR, artificial neural network (ANN)–multilayer perception (MLP), and RF were used to develop crop yield prediction models at two timescales as given in Table 2. 

The meteorological drought indices are computed at various timescales of 1, 3, 6, 9, or 12 months. Relatively shorter periods of 1 and 3 months are more appropriate to describe the drought effects on soil moisture conditions and vegetation growth (Mallya et al. 2016). Therefore, meteorological indices at monthly timescales were used as inputs for model development as it is expected to reflect more accurately the variability and cumulative effect of water deficit throughout the development of crops, especially under rainfed conditions. The satellite-based indices were estimated in late September when cotton and groundnut crops were at the stage of maximum NDVI occurrence. MLR is the simplest method often used for comparing the performance of advanced methods such as ANN and RF. The estimation model is multilinear and includes a slope and an interception. 

### 3.3. Artificial neural network–multilayer perceptron 

Among various ANN models and training algorithms, the multilayer perceptron neural network model (MLP) trained with a feed-forward backpropagation algorithm has been extensively used for simulating and predicting purposes in hydrology, water resources, and crop yield prediction (Gniewko 2019). MLPs consist of an input layer, a hidden layer(s) (where the actual processing is done via a system of weighted connections), and an output layer (where the answer is produced). The sigmoid function was used as an activation function for both hidden and output layers. The data were randomly partitioned in the ratio 70:30 (Gniewko 2019) for training and testing, respectively, and for each iteration of the k times, a model was run against the data (Figure 3). 

According to the study by Kim & Valdes (2003), the output value of the aforementioned network is given by 



Table 2 | Timescales and inputs for crop yield prediction models 

Timescale Inputs (i) On 31 August (75 days after sowing, i.e., approximately 1.5 months Monthly meteorological drought indices of June, July, and August before harvest for groundnut or first picking for cotton.) (ii) On 30 September (105 days after sowing, i.e., approximately 15 Monthly meteorological drought indices of June, July, August, days before harvest for groundnut or first picking for cotton.) and September along with vegetation Indices 



Figure 3 | Algorithm of random forest. 

Downloaded from iwaponline.​com/​jwcc/​article-pdf/​14/​12/​4729/​1349676/​jwc0144729.​pdf by guest 

Journal of Water and Climate Change Vol 14 No 12, 4735 

where fh is the activation function used in the hidden layer, wkj is the weight connecting the jth neuron in the hidden layer and kth neuron in the output layer, wko is the bias for the kth neuron in the output layer, and fo is the activation function for the output layer. The objective of using training algorithms is to optimize the parameters of the output function (weights in Equation (1)) so that the E(x,w) value, i.e., network’s global errors, becomes minimal. 





where p is the total number of training patterns, k is the total number of output neurons (in this study equals 1), yk is the desired output at the kth neuron, and yk̂ is the actual output at the kth neuron. For this purpose, the Levenberg–Marquardt (LM) (Levenberg 1944; Marquardt 1963) back propagation algorithm was used for neural network training. 

The MLP structure development consists of setting up the hyperparameters such as the learning rate (L), momentum (M), number of epochs (N), threshold for the number of consecutive errors (E), number of hidden layers (H), and number of nodes in hidden layer (HN). The learning rate sets the step size for parameter updates during training, influencing convergence and stability. Momentum accelerates convergence by incorporating a fraction of the previous update, enhancing learning and preventing local minima. The number of epochs defines how many times the dataset is passed through the network, impacting convergence and generalization. A threshold for consecutive errors (E) aids in deciding when to halt training, based on model performance. The number of hidden layers (H) influences the model’s ability to learn intricate patterns and generalize. The number of nodes in hidden layers (HN) determines the model’s feature representation capacity, avoiding underfitting or overfitting (Reed & Marks 1999; LeCun et al. 2012). 

### 3.4. Random forest 

RF is a popular machine-learning algorithm that belongs to the supervised learning technique. The RF algorithm was introduced by Breiman (2001) and used for both classification and regression. RF is based on the concept of ensemble learning, which is a process of combining multiple decision tree regressions. Each tree provides its prediction, and the optimal prediction of RF is obtained by averaging the prediction of all decision trees in case of regression problems and the maximum voting of all decision trees in case of classification problems. RF works in two phases: the first is to create the RF by combining N decision trees, and the second is to make predictions for each tree created in the first phase. The following are the steps involved in prediction using RF (Figure 3): 

- 1: Select random K data points from the training set. 

- 2: Build the decision trees associated with the selected data points (subsets). 

- 3: Choose the number N for the decision trees that you want to build. 

- 4: Repeat Steps 1 and 2. 

- 5: For new data points, find the predictions of each decision tree, and assign the new data points to the category that wins the majority of votes. 

The hyperparameters that need to be tuned in the RF algorithm are the number of trees or the number of regression trees, the number of features to consider when looking for the best split, and the maximum depth of the tree (Bouras et al. 2021). The greater number of trees in the forest leads to higher accuracy and prevents the problem of overfitting. Since the RF combines multiple trees to predict the class of the dataset, some decision trees may predict the correct output, while others may not. But together, all the trees predict the correct output. The best models were chosen based on the largest value of coefficient of determination (R<sup>2</sup> ) and Nash–Sutcliffe efficiency (NSE) and the smallest value of the root-mean-square errors (RMSEs) and fractional standard error (FSE) (Karran et al. 2014). 

Downloaded from iwaponline.​com/​jwcc/​article-pdf/​14/​12/​4729/​1349676/​jwc0144729.​pdf by guest 

Journal of Water and Climate Change Vol 14 No 12, 4736 

## 4. RESULTS AND DISCUSSION 

The first step for the model development was to find the most appropriate index among six meteorological drought indices and three vegetation indices for crop and climatic zone-specific model development. The appropriate indices were selected as input variables for model development based on the highest correlation coefficient r between indices and crop yields. 

### 4.1. Selection of drought indices model development 

The Pearson correlation coefficient (r) between various meteorological and vegetation drought indices and cotton and groundnut yields along with its significance for NSAZ and SSAZ are depicted in Table 3. The results revealed that for the majority of instances, the correlations of SPEI and RDI were higher and more significant than those of SPI, RAI, DAI, and DI. 

The rainfall-based indices can explain only the supply-side anomalies of soil moisture balance, while SPEI and RDI measure the demand-side anomalies of soil moisture availability, i.e., evaporation transpiration through Potential Evapotranspiration (PET). To acquire the diversity of drought prediction, evapotranspiration is deemed necessary for calculating meteorological droughts (Pandya & Gontia 2023). The evaporation rate is expected to increase due to global warming which results in drier conditions on the ground and an increase of water vapour in the atmosphere over time (Kumar et al. 2021). Moreover, the role of temperature is more crucial in characterizing the occurrence of climate extremes like droughts due to future projections of temperature increase and climate change (IPCC 2022) which necessitates the use of indices such as SPEI and RDI over only rainfall-based indices. The SPI is still the most widely used index across the globe including India for drought analysis (Pandya et al. 2020); however, owing to their multiscalar nature, in addition to holding all advantages of SPI (Tsakiris & Vangelis 2005; Vicente-Serrano et al. 2010; Chen et al. 2016; Pandya & Gontia 2023), SPEI and RDI are recommended over SPI. Among the two crops under study, groundnut yield was better correlated with drought indices as compared to cotton; the possible reasons were highlighted by Pandya et al. (2022) as better irrigation facilities 

Table 3 | Correlation coefficient (r) between various drought indices and crop yields 



Downloaded from iwaponline.​com/​jwcc/​article-pdf/​14/​12/​4729/​1349676/​jwc0144729.​pdf by guest 

Journal of Water and Climate Change Vol 14 No 12, 4737 

observed in cotton growing areas and the deep-rooted system of cotton that would be a responsible factor to withstand dry spells of longer duration compared to groundnut crop. 

The results depicted in Table 3 disclose that among vegetation indices, NAI for cotton in both zones groundnut in NSAZ, and VCI for cotton in SSAZ were better correlated with crop yields. The NDWIA was common for all models as inputs for predicting yield at 105 days after sowing. NDWI is a measure of liquid water molecules in vegetation canopies that interact with the incoming solar radiation and is complementary to, not a substitute for NDVI (Gao 1996). The Short Wave Infrared (SWIR) bands of NDWI respond to soil moisture and leaf water content differently, and, thus, combining multiple SWIR bands (rather than one SWIR band) with an NIR band may improve sensitivity in drought monitoring (AghaKouchak et al. 2015). The Manual for Drought Management, GoI (Anonymous 2016, Department of Agriculture, Cooperation & Farmers Welfare, Government of India) also advised to use NDWI in combination with VCI for agricultural drought declaration. Therefore, based on correlation analysis results, yield prediction models were developed using SPEI for cotton in NSAZ and SSAZ as well as for groundnut in SSAZ, while RDI for cotton in SSAZ. Among vegetation-based indices, NAI and NDWIA were used for cotton in NSAZ and SSAZ as well as for groundnut in SSAZ, while VCI and NDWIA were used for cotton in SSAZ. 

Considering the designated study period, the average cotton productivity was measured at 445 kg/ha for NSAZ and 570 kg/ha for SSAZ, whereas groundnut productivity stood at 1,241 kg/ha for NSAZ and 1,752 kg/ha for SSAZ. The analysis revealed a notably higher level of rainfall variability in SSAZ compared to NSAZ. For example, the average standard deviation of monthly rainfall was 165 mm for NSAZ and 253 mm for SSAZ, with an average coefficient of variation (%) of monthly rainfall at 89% for NSAZ and 109% for SSAZ. In terms of soil composition, NSAZ is characterized by shallow medium black soils, while SSAZ possesses shallow medium black and Calcareous soils. With regards to land usage, approximately 7% of the geographic area in NSAZ is covered by forest, with 68% dedicated to crop cultivation. Conversely, in SSAZ, about 11% is covered by forests and 60% is designated for cultivation. Notably, a significant portion of irrigation in Saurashtra relies on groundwater, with 32% of the cultivation area in NSAZ and 60% in SSAZ being irrigated through groundwater sources wells (https://www.aps.dac.gov.in/LUS/Public/Reports.aspx). This implies that the availability of life-saving groundwater irrigation in SSAZ due to groundwater recharge structures might have enabled the crops to resist the drought condition in a better way in SSAZ compared to NSAZ. These facts might be a few of the important reasons for higher crop productivity and weaker correlation with drought indices for SSAZ compared to NSAZ. Moreover, factors such as localized soil conditions, management practices, and crop varieties are not considered in this study which may mask the direct relationship between drought indices and crop yield, and affect the regional discrepancy in correlations between drought indices and actual crop yield. 

The previous studies evaluated the link of vegetation drought indices NDVI anomaly and VCI with crop yields in the Saurashtra region of Gujarat using relatively shorter term and coarser resolution satellite sensors data such as MODIS (250 m � 250 m or 500 m � 500 m) and AVHRR (1 km � 1 Km) as compared to our study with finer resolution Landsat (30 m �30 m) data of longer durations (33 years) (Chopra 2006; Bandyopadhyay & Saha 2016; Lunagaria & Sur 2019). However, comparatively lower correlations were obtained between vegetation indices and crop yields compared to our study. Small and marginal farmers (with a holding size of fewer than 2 ha) account for 68% of the total number of farmers in Gujarat (Gulati et al. 2021), and the coarser resolution satellite data could not have obtained clearer relations between yield and vegetation indices in previous studies. The resolution of NDVI datasets extracted from the MODIS sensor is 250 m and lacks accuracy for some applications (Nagler et al. 2005). Our study demonstrates the better effectiveness of fine resolution, long-term satellite data with proper crop masking for agricultural drought quantification, especially in areas where small and marginal farmers predominate. 

### 4.2. Development of crop yield prediction models using MLR, ANN-MLP, and RF 

The MLR equations for the prediction of cotton and groundnut yields are given in Table 4, and various parameters of ANNMLP optimized by the trial and error method for model development are presented in Table 5. The optimum number of hidden layers in models with three and six inputs was found as 2 and 3, respectively, while different learning rates were found for various models which are displayed in Table 5. 

The attribute importance for RF crop yield prediction models based on average impurity decrease (and the number of nodes using that attribute) can be observed in Table 6. The Gini importance (or mean decrease impurity) is computed from the RF structure. The features for internal nodes are selected with some criterion, which for classification tasks can be Gini impurity or information gain, and for regression is variance reduction. We can measure how each feature decreases the impurity of the split (the feature with the highest decrease is selected for the internal node), and for each feature, how on average it decreases 

Downloaded from iwaponline.​com/​jwcc/​article-pdf/​14/​12/​4729/​1349676/​jwc0144729.​pdf by guest 

Journal of Water and Climate Change Vol 14 No 12, 4738 

Table 4 | Multiple linear regression models for crop yield prediction 

|At 75 days after sowing||
|---|---|
|1<br>NSAZ cotton|86.8�SPEIJuneþ136.3�SPEIJuly þ90�SPEIAugþ440|
|2<br>NSAZ groundnut|298.8�SPEIJuneþ298.9�SPEIJulyþ355.8�SPEIAugþ1,223|
|3<br>SSAZ cotton|107.5�RDIJuneþ71.2�RDIJulyþ68.9�RDIAugþ560|
|4<br>SSAZ groundnut|544.7�SPEIJuneþ239.6�SPEIJulyþ284�SPEIAugþ1,685|
|At 105 days after sowing||
|5<br>NSAZ cotton|76.3�SPEIJuneþ117.4�SPEIJulyþ65.9�SPEIAugþ43�SPEISepþ1.3�NAIþ1.9�NDWIAþ433|
|6<br>NSAZ groundnut|274�SPEIJuneþ191.6�SPEIJuly þ223�SPEIAugþ132�SPEISepþ11�NAI�6�NDWIAþ1,185|
|7<br>SSAZ cotton|102.2�RDIJuneþ60.5�RDIJulyþ67.3�RDIAugþ15�RDISepþ3�VCI�2.3�NDWIAþ369|
|8<br>SSAZ groundnut|549.3�SPEIJuneþ214�SPEIJulyþ297.2�SPEIAugþ486.6�NDWIAþ1,615|



Table 5 | Parameters of MLP models architecture for crop yield prediction 

||MLP parameters||
|---|---|---|
|Zone and crop|At 75 days after sowing|At 105 days after sowing|
|NSAZ cotton|L 0.05-M 0.2-N 500-E 20-H1-HN2|L 0.2-M 0.2-N 500- E 20-H1-HN3|
|NSAZ groundnut|L 0.05-M 0.2-N 500-E 20-H1-HN2|L 0.2-M 0.2-N 500- E 20-H1-HN3|
|SSAZ cotton|L 0.2-M 0.2-N 500-E 20-H1-HN2|L 0.3-M 0.2-N 500-E 20-H1-HN3|
|SSAZ groundnut|L 0.1-M 0.2-N 500-E 20-H1-HN2|L 0.1-M 0.2-N 500-E 20-H1-HN3|



Note: L ¼ learning rate; M ¼ momentum; N ¼ number of epochs; E ¼ threshold for number of consecutive errors; H ¼ number of hidden layer; HN ¼ number of nodes in hidden layer. 

the impurity that can be collected. The average over all trees in the forest is the measure of the feature importance. Table 6 highlights that for predicting crop yields at 75 days after sowing, SPEI/RDI of August was the most important and showed the highest impurity decrease (information gain), followed by SPEI of July and June. Similarly for models at 105 days after sowing, the vegetation indices NAI/NDWIA/VCI were proven more important in RF model building. While for both the crops in NSAZ and for cotton in SSAZ, the SPEI of June and for groundnut in SSAZ, the SPEI of September was found least important among the six input variables. The predictive capability of RF can also provide useful information about the variable importance and dependence. 

The variable importance rank and the partial impact of the variable on the response can be evaluated for systems analysis (Díaz-Uriarte & Alvarez de Andrés 2006). The variable importance measure, mean decrease accuracy (% increase in meansquare error in RF output), was used to identify the most influential parameter to predict crop yields for both climatic zones ( Jeong et al. 2016). The same was employed in the present study. A higher impurity decrease implies more information gain and greater importance of variables in model development. In the RF models at 75 days, the SPEI/RDI of August was found to be the most important attribute for model development for both crops and both agro-climatic zones, and the SPEI/RDI of June was found to be the least important. While for models at 105 days, both remote sensing-based indices NAI/VCI and NDWIA were found more important, except for cotton in NSAZ, where SPEI was found as an important attribute after NAI. The indices value in June was observed to be the least important among all parameters, and similar results were found for models at 75 days. Based on the developed crop yield prediction models, the observed and predicted crop yields for cotton and groundnut for both climatic zones and both timescales are plotted in Figure 4. The performance of developed models for different techniques and timescales is clearly visible in Figure 4 by closeness or departure from the line of perfect agreement, which is discussed in the subsequent section. 

### 4.3. Performance evaluation of developed crop yield prediction models 

The performance of developed crop yield prediction models was evaluated using goodness of fit measures, namely, R<sup>2</sup> (coefficient of determination), NSE, RMSE, and FSE. The coefficient of determination, R<sup>2</sup> , for various models is shown in Figure 5. 

Downloaded from iwaponline.​com/​jwcc/​article-pdf/​14/​12/​4729/​1349676/​jwc0144729.​pdf by guest 

Journal of Water and Climate Change Vol 14 No 12, 4739 

Table 6 | Average impurity decrease (and number of nodes using that attribute) for random forest crop yield prediction models 

||NSAZ||SSAZ||
|---|---|---|---|---|
|Importance|Cotton|Groundnut|Cotton|Groundnut|
|At 75 days after sowing|||||
|1|SPEIAug<br>168474 (2180)|SPEIAug<br>2940134 (2037)|RDIAug<br>145757 (556)|SPEIAug<br>2113714(598)|
|2|SPEIJuly<br>148176 (3443)|SPEIJuly<br>1329742 (3414)|RDIJuly<br>100772 (1052)|SPEIJuly<br>1474312 (1060)|
|3|SPEIJune<br>68635 (4525)|SPEIJune<br>886477 (4749)|RDIJune<br>78529 (1546)|SPEIJune<br>1075874 (1572)|
|At 105 days after sowing|||||
|1|NAI|NDWIA|VCI|NDWIA|
||202434 (1121)|4331701 (808)|176824 (275)|3711101 (251)|
|2|SPEIJuly|NAI|NDWIA|NAI|
||157625 (2126)|2648543 (964)|137950 (206)|2875351 (330)|
|3|SPEISep<br>126364 (1488)|SPEISep<br>1889034 (1162)|RDIAug<br>119536 (528)|SPEIAug<br>1250905 (528)|
|4|SPEIAug<br>120651 (1614)|SPEIAug<br>1620077 (1565)|RDIJune<br>115597 (402)|SPEIJune<br>1035154 (972)|
|5|NDWIA<br>113595(855)|SPEIJuly<br>935413 (2266)|RDIJuly<br>80499 (737)|SPEIJuly<br>979075 (705)|
|6|SPEIJune|SPEIJune|RDIJune|SPEISep|
||55536 (2630)|634251 (2893)|67200 (930)|923216 (304)|



It shows that the best performance for both timescales, i.e., at 75 days and 105 days, RF with R<sup>2</sup> ranged between 0.77 and 0.92 for cotton and 0.77 and 0.91 for groundnut. 

A better performance in terms of R<sup>2</sup> was observed for MLP compared to MLR. It was also observed that R<sup>2</sup> for all three models was less for cotton in SSAZ compared to the rest of the pairs of models. A similar trend was observed in terms of performance measure NSE with the highest NSE obtained for RF-based models ranging between 72 and 83% at 75 days and 71 and 90% at 105 days (Figure 6). While between MLP and MLR, better performance was registered by MLP for all eight models in terms of NSE%, whose ranges are shown in Figure 6. 

The RMSE for various models in Figure 7 advocates that the RF-based models demonstrated the minimum RMSE at 75 days with values of 105 kg/ha for cotton in NSAZ and 373 kg/ha for groundnut in SSAZ (Figure 7). As the crop progressed to 105 days, the prediction errors reduced, and the RF-based models continued to showcase superior performance, achieving the lowest RMSE values of 80 kg/ha for cotton in NSAZ and 133 kg/ha for groundnut in SSAZ. To facilitate a more comprehensive comparison of model performance across different regions and crops, the scale-independent measure, FSE, was also incorporated (Figure 8). Notably, the RF-based models consistently demonstrated the lowest FSE when compared to MLR and MLP across all region-crop combinations. The FSE values suggest that cotton yield was more accurately predicted compared to groundnut. However, it is important to highlight that the variation in model performance between cotton and groundnut was more pronounced for NSAZ compared to SSAZ, a difference that may be attributed to factors elucidated in Section 4.1. 

It is worth mentioning that for NSAZ, cotton is the dominant crop, and for SSAZ, groundnut is the dominant crop. The performance of MLR-based models was not found comparable with that of MLP and RF. The drought–yield relationship is nonlinear because of the complexity of the water–yield relationship. The crop sensitivities to water stress vary by crop development stages (Steduto et al. 2012). When a drought event occurs at the non-sensitive stage of crop growth, the impact may not be as substantial as when the drought event happens at the sensitive crop growth stage (e.g., during flowering) (Mishra et al. 2014). Several researchers across the globe used MLR and several nonlinear models including RF and MLP for crop yield forecasting with satellite drought-based indices and other inputs and found the superior performance of nonlinear 

Downloaded from iwaponline.​com/​jwcc/​article-pdf/​14/​12/​4729/​1349676/​jwc0144729.​pdf by guest 

Journal of Water and Climate Change Vol 14 No 12, 4740 



Figure 4 | Observed and predicted yield of cotton and groundnut by MLR, MLP, and RF for cotton and groundnut at 75 days after sowing and 105 days after sowing (NSAZ ¼ North Saurashtra Agro-Climatic Zone, SSAZ ¼ South Saurashtra agro-climatic zone). 

models compared to MLR to predict crop yields. (Jeong et al. 2016; Cao et al. 2020; Kamir et al. 2020; Klompenburg et al. 2020; Bouras et al. 2021). 

The improvement in R<sup>2</sup> and NSE and reduction in RMSE was observed in models at 105 days compared to models at 75 days due to the combined signals of meteorological indices, NDVI-based NAI/VCI and NDWI-based NDWIA, rather than only meteorological indices of 3 months at 95 days. Dhillon et al. (2023) also obtained better crop yield prediction by RF while combining NDVI and climatic factors. The performance improvement was high in MLP and MLR compared to RF, which also shows a higher capability of RF to estimate the yield with limited data at 75 days. For cotton in NSAZ and groundnut in SSAZ, R<sup>2</sup> value suggests that MLP-based models are also capable of early prediction of yields for these crops and zones. 

Downloaded from iwaponline.​com/​jwcc/​article-pdf/​14/​12/​4729/​1349676/​jwc0144729.​pdf by guest 

Journal of Water and Climate Change Vol 14 No 12, 4741 



Figure 5 | The coefficient of determination R<sup>2</sup> for crop yield prediction models. 



Figure 6 | The NSE (%) for crop yield prediction models. 



Figure 7 | The RMSE (kg/ha) for crop yield prediction models. 

Downloaded from iwaponline.​com/​jwcc/​article-pdf/​14/​12/​4729/​1349676/​jwc0144729.​pdf by guest 

Journal of Water and Climate Change Vol 14 No 12, 4742 



Figure 8 | The FSE for crop yield prediction models. 

The use of the RF algorithm has gained popularity in ecological studies (Zhang et al. 2014); however, a few studies recently examined its capacity to predict crop yields and found the RF to be more efficient than several other machine-learning algorithms (Everingham et al. 2016; Jeong et al. 2016; Roell et al. 2020; Shahhosseini et al. 2020). The merits of RF for crop yield predictions at regional and global scales are high accuracy and precision, ease of use, and utility in data analysis. The RF algorithm has advantages such as taking less training time as compared to other algorithms, predicting output with high accuracy, even for a large dataset running efficiently, and maintaining accuracy when a large proportion of data is missing. 

The RF algorithms can use multiple types of predictors in a model more easily than traditional multiple linear or nonlinear regressions can (Berk 2008). RF is an ensemble of decision trees, which consist of binary nodes that split the response. At every RF node, any type of splitting of predictor variables, such as continuous and categorical, is evaluated and selected for the split under the same standard: how well the given variable can split the response (Jeong et al. 2016). The efficient results of RF are likely more evident when the response is a result of complex interactions between multiple predictors as in crop systems where interactions among biophysical, ecological, physiological, and management factors can complicate modelling. RF uses the single best variable when it splits responses at each node of decision trees and averages the predictions of the trees in the forest to make a multidimensional step function. This means that even if multiple variables are correlated and drive the response similarly, only one of them can affect the RF regression model at a time. Many predictors of crop production, such as climate, management, and soil, are often highly correlated with and within each other and may have multicolinearity. Variable colinearity can be a critical problem in traditional regression models that are derived from linear regression. The RF regression has advantages when predictor or explanatory variables are highly correlated (e.g., temperature-derived variables) (Gromping 2009). 

Researchers (Segal 2003; Berk 2008; Gromping 2009; Jeong et al. 2016) also observed some limitations of RF that may result in a loss of accuracy when predicting the extreme ends or responses beyond the boundaries of the training data. The RF algorithm intrinsically separates a random subset of data for performance testing from calibration data by using only the remaining set of data for model training. Therefore, splitting data for training and testing purposes are likely a redundant procedure when applying RF for crop yield modelling and its performance may increase as more data are included for training. There is a chance of over fitting of data in RF models outside the range of training datasets that may lump the predictions (Segal 2003). The behaviour of the RF model may be less intuitive to interpret than traditional regression models because its algorithm consists of an ensemble of a large number of decision trees that may not be fully described systematically. In addition, the RF algorithm may overfit data. For predicting crop yield in future scenarios, this limitation of RF regression could be critical, since at least some part of the current crop field is expected to have new and more extreme environmental conditions in the future that did not exist in the past and present data domains. The limitations of RF can be overcome by enhancing the sample size covering all probable extreme points. If the sample size is small, the application of RF should be avoided, and other machine-learning approaches like ANN should be adopted. 

Downloaded from iwaponline.​com/​jwcc/​article-pdf/​14/​12/​4729/​1349676/​jwc0144729.​pdf by guest 

Journal of Water and Climate Change Vol 14 No 12, 4743 

Agricultural drought is a result of meteorological drought linked to precipitation shortages, high evaporative demand, and soil moisture deficits. Agricultural drought is also characterized based on plant type, growth stage, and soil properties. Timely information about the onset of drought, its extent, intensity, duration, and impacts is essential for the agricultural sector. The unpredictability of the crop yield due to severe weather events like drought and extreme heat continues to be a key worry for farmers, markets, and governments, emphasizing the necessity of precise and timely estimates of crop output in a changing environment. For the implementation of agricultural policy, the forecasting and analysis of global trade trends, the identification of successful climate change adaptation measures, and the capacity to estimate crop yield in response to climate variability at a regional scale are essential. 

The dependence of farmers on rainfed farming should be reduced by adopting drought-resistant or early-maturing crops and implementing suitable water harvesting and irrigation methods (Pandya et al. 2020). The objective of designing such an early warning system regarding drought impact on crop yields is helpful to keep track of the leading indicators (agro-climatic, market socioeconomic indicators, and late anthropometric indicators) to get sufficient lead time to intervene at the drought onset phase itself. It is a well-established fact that drought-induced social and economic distress can only be addressed by adopting a better crisis management approach when the extent of loss is measured timely. An early warning helps to strengthen the capacity of communities in managing and reducing drought effects through building preparedness and providing coping strategies with sound contingency plans for resilient agricultural practices to secure sustainable food production. The advanced high-resolution data from satellites and recent seasonal climate model predictions have enabled the development of state-of-the-art monitoring and prediction systems that can help address the problems to improve drought monitoring and early warning. Combining data from multiple sources generally outperforms models based on a single dataset as it explains the single dimension of crop yield variations. 

The present study has shown the high potential of the combined use of high temporal resolution remote sensing images and drought indices to predict the early crop in a semi-arid region of NSAZ and SSAZ. The combined use of remote sensing and drought indices seems to be a very useful approach for early crop prediction, having good potential to reduce crop uncertainty for farmers, markets, and governments. The study presented the likelihood of specific impacts of drought on crop yields, which is more useful to resource managers and policymakers than presenting raw meteorological drought indices. In addition to climatic factors, it is important to acknowledge the influence of non-climatic factors on crop yield, including diseases, pest infestations, soil types, crop varieties, and various other variables that intricately impact crop performance. The limitation of not incorporating the aforementioned non-climatic factors in the present study may be addressed to enhance the effectiveness of the developed models. In addition, by incorporating both climatic and non-climatic parameters, as well as accounting for the exact availability of irrigation resources, future iterations of these models can offer a more holistic and accurate depiction of the intricate interactions that drive crop yield variations. Moreover, an attempt is being made to enhance the present study by developing operational yield prediction tools using dynamic inputs from several open-source data. This can be further explored by estimating future agricultural droughts and can yield loss risk for various climate change scenarios. 

## 5. CONCLUSIONS 

A comprehensive comparison of nine drought indices, including six meteorological drought indices and three remote sensingbased vegetation drought indices, was carried out with cotton and groundnut crop yields based on the correction coefficient. The climatic zone-wise crop yield prediction models were developed using the SPEI/RDI, NAI/VCI, and NDWIA, by comparing three machine-learning techniques. The evaluation of model performance indicated that RF exhibited superior predictive capabilities compared to MLR and ANN-MLP. Specifically, RF excelled in the early prediction of Kharif cotton and groundnut crop yields at two timescales: 75 days after sowing and 105 days after sowing. On the basis of our findings, we recommend the utilization of RF in combination with a judicious selection of appropriate meteorological drought indices and high-resolution, long-term, satellite-based vegetation indices as model inputs. This approach proves valuable in enabling the early estimation of crop yields, which is crucial for the timely assessment and mitigation of agricultural droughts. 

## ACKNOWLEDGEMENTS 

The authors acknowledge the State Water Data Centre, Gandhinagar Gujarat and the Department of Agrometeorology, JAU, Junagadh, for providing necessary meteorological data. 

Downloaded from iwaponline.​com/​jwcc/​article-pdf/​14/​12/​4729/​1349676/​jwc0144729.​pdf by guest 

Journal of Water and Climate Change Vol 14 No 12, 4744 

## AUTHOR CONTRIBUTIONS 

P.A.P.: worked on conceptualization, data collection, software, data analysis, computation, visualization, and writing – original draft preparation. N.K.G.: worked on conceptualization, supervision, writing – review, and editing the manuscript. The authors read and approved the final manuscript. 

## FUNDING 

This research was a part of Ph.D. research and did not receive any funding. 

## DATA AVAILABILITY STATEMENT 

All relevant data are included in the paper or its Supplementary Information. 

## CONFLICT OF INTEREST 

The authors declare there is no conflict. 

## REFERENCES 

AghaKouchak, A., Farahmand, A., Melton, F. S., Teixeira, J., Anderson, M. C., Wardlow, B. D. & Hain, C. R. 2015 Remote sensing of drought: Progress, challenges and opportunities. Reviews of Geophysics 53, 452–480. 

Anonymous 2016 Manual for Drought Management. Department of Agriculture, Cooperation & Farmers Welfare, Ministry of Agriculture & Farmers Welfare, Government of India, New Delhi. 

- Anonymous 2020 Provisional District Wise Land Utilization, Area Under Crops and Area Irrigated by Source of Gujarat State for 2018–19. Department of Agriculture and Farmers’ Welfare, Government of Gujarat, Gandhinagar. 

Anyamba, A., Tucker, C. J. & Eastman, J. R. 2001 NDVI anomaly patterns over Africa during the 1997/98 ENSO warm event. International Journal of Remote Sensing 22 (10), 1847–1859. 

Bandyopadhyay, N. & Saha, A. K. 2016 A comparative analysis of four drought indices using geospatial data in Gujarat, India. Arabian Journal of Geosciences 9, 341. 

Bandyopadhyay, N., Bhuiyan, C. & Saha, A. K. 2016 Heat waves, temperature extremes and their impacts on monsoon rainfall and meteorological droughts in Gujarat, India. Natural Hazards 82, 367–388. 

Belal, A., El-Ramady, H., Mohamed, E. S. & Saleh, A. 2014 Drought risk assessment using remote sensing and GIS techniques. Arabian Journal of Geosciences 7, 35–53. 

Belgiu, M. & Drăgut,̧ L. 2016 Random forest in remote sensing: A review of applications and future directions. ISPRS Journal of Photogrammetry and Remote Sensing 114, 24–31. 

Berk, R. A. 2008 Random forests. In: Statistical Learning from a Regression Perspective. Springer Series in Statistics (Allen, G., Veaux, R. De & Nugent, R., eds). Springer, New York, NY, pp. 233–293. 

- Bhalme, H. N. & Mooley, D. A. 1980 Large-scale droughts/floods and monsoon circulation. Monthly Weather Reviews 108, 1197–1211. 

Bharadiya, J. P., Tzenios, N. T. & Reddy, M. 2023 Forecasting of crop yield using remote sensing data, agrarian factors and machine learning approaches. Journal of Engineering Research and Reports 24 (12), 29–44. 

Bhojani, S. & Bhatt, N. 2018 Application of data mining technique for wheat crop yield forecasting for districts of Gujarat state. International Journal of Scientific Research and Publication 8 (7), 302–306. 

Bouras, E. H., Jarlan, L., Er-Raki, S., Balaghi, R., Amazirh, A., Richard, B. & Khabba, S. 2021 Cereal yield forecasting with satellite droughtbased indices, weather data and regional climate indices using machine learning in Morocco. Remote Sensing 13, 3101. 

Breiman, L. 2001 Random forests. Machine Learning 45, 5–32. 

Cao, J., Zhang, Z., Tao, F., Zhang, L., Luo, Y., Han, J. & Li, Z. 2020 Identifying the contributions of multi-source data for winter wheat yield prediction in China. Remote Sensing 12 (5), 750. 

Chen, T., Xia, G., Liu, T., Chen, W. & Chi, D. 2016 Assessment of drought impact on main cereal crops using a standardized precipitation evapotranspiration index in Liaoning province, China. Sustainability 8 (10), 1069. 

Chopra, P. 2006 Drought Risk Assessment Using Remote Sensing and GIS: A Case Study of Gujarat. Master Thesis (Unpblished), 

International Institute for Geo-Information Science and Earth Observation, Enschede, Netherlands. 

David, G., Sergio, C. & Johannes, H. 2019 Comparison of meteorological and satellite-based drought indices as yield predictors of Spanish cereals. Agricultural Water Management 213, 388–396. 

- Dhillon, M. S., Dahms, T., Kuebert, F. C., Rummler, T., Arnault, J., Steffan-Dewenter, I. & Ullmann, T. 2023 Integrating random forest and crop modeling improves the crop yield prediction of winter wheat and oil seed rape. Frontiers in Remote Sensing 3, 1–19. 

Díaz-Uriarte, R. & Alvarez de Andrés, S. 2006 Gene selection and classification of microarray data using random forest. BMC Bioinformatics 7, 3. 

- Everingham, Y., Sexton, J., Skocaj, D. & Geoff, I. B. 2016 Accurate prediction of sugarcane yield using a random forest algorithm. Agronomy for Sustainable Development 36, 27. 

Downloaded from iwaponline.​com/​jwcc/​article-pdf/​14/​12/​4729/​1349676/​jwc0144729.​pdf by guest 

Journal of Water and Climate Change Vol 14 No 12, 4745 

Gadgil, S. & Gadgil, S. 2006 The Indian monsoon, GDP and agriculture. Economic and Political Weekly 41 (47), 4887–4895. 

Gao, B. C. 1996 NDWI – A normalized difference water index for remote sensing of vegetation liquid water from space. Remote Sensing of Environment 58 (3), 257–266. 

Ghaleb, F., Mario, M. & Sandra, A. N. 2015 Regional Landsat-based drought monitoring from 1982 to 2014. Climate 3, 563–577. Gibbs, W. J. & Maher, J. V. 1967 Rainfall Deciles as Drought Indicators. Bureau of Meteorology Bulletin, 48, Commonwealth of Australia, Melbourne, Australia. 

Gniewko, N. 2019 Simple model based on artificial neural network for early prediction and simulation winter rapeseed yield. Journal of Integrative Agriculture 18 (1), 54–61. 

Gromping, U. 2009 Variable importance assessment in regression: Linear regression versus random forest. The American Statistician 63 (4), 308–319. 

Gulati, A., Roy, R., Hussain, S., 2021 Performance of agriculture in Gujarat. In: Revitalizing Indian Agriculture and Boosting Farmer Incomes. India Studies in Business and Economics (Gulati, A., Roy, R. & Saini, S., eds). Springer, Singapore, pp. 113–144. 

IPCC 2022 Summary for Policymakers (H.-O. Pörtner, D.C. Roberts, E.S. Poloczanska, K. Mintenbeck, M. Tignor, A. Alegría, M. Craig, 

S. Langsdorf, S. Löschke, V. Möller, A. Okem, eds.). In: Climate Change 2022: Impacts, Adaptation, and Vulnerability. Contribution of Working Group II to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change (H.-O. Pörtner, D.C. Roberts, M. Tignor, E.S. Poloczanska, K. Mintenbeck, A. Alegría, M. Craig, S. Langsdorf, S. Löschke, V. Möller, A. Okem, B. Rama, eds.). Cambridge University Press, Cambridge, UK and New York, NY. 

Jeong, J. H., Resop, J. P., Mueller, N. D., Fleisher, D. H., Yun, K., Butler, E. E. & Timlin, D. J. 2016 Random forests for global and regional crop yield predictions. Plos One 11 (6), e0156571. 

Kamir, E., Waldner, F. & Hochman, Z. 2020 Estimating wheat yields in Australia using climate records, satellite image time series and machine learning methods. ISPRS Journal of Photogrammetry and Remote Sensing 160, 124–135. 

Karran, D., Morin, E. & Adamowski, J. 2014 Multi-step streamflow forecasting using data-driven non-linear methods in contrasting climate regimes. Journal of Hydroinformatics 16, 671–689. 

Kim, T. & Valdes, J. B. 2003 Nonlinear model for drought forecasting based on a conjunction of wavelet transforms and neural networks. Journal of Hydrologic Engineering 8 (6), 319–328. 

Klompenburg, V. T., Kassahun, A. & Catal, C. 2020 Crop yield prediction using machine learning: A systematic literature review. Computers Electronics in Agriculture 177, 105709. 

Kogan, F. N. 1995 Application of vegetation index and brightness temperature for drought detection. Advances in Space Research 15 (11), 91–100. 

Kumar, S. K., Anand, R. P., Sreelatha, K. & Sridhar, V. 2021 Regional analysis of drought severity-duration-frequency and severity-areafrequency curves in the Godavari River Basin, India. International Journal of Climatology 41, 5481–5501. 

LeCun, Y. A., Bottou, L., Orr, G. B., Müller, K. R., 2012 Efficient backprop. In: Neural Networks: Tricks of the Trade. Lecture Notes in 

Computer Science, Vol. 7700 (Montavon, G., Orr, G. B. & Müller, K. R., eds). Springer, Berlin, Heidelberg, pp. 9–48. 

Lee, K. Y., Kim, K. H., Kang, J. J. & Choi, S. J. 2017 Comparison and analysis of linear regression and artificial neural network. International Journal of Applied Engineering Research 12 (20), 9820–9825. 

Levenberg, K. 1944 A method for the solution of certain non-linear problems in least squares. Quarterly of Applied Mathematics 5, 164–168. 

Lunagaria, M., Sur, K., 2019 Climate change and agriculture in Gujarat: Retrospective and prospective. In: Climate Change and Agriculture Causes, Impacts and Interventions (Prasada Rao, G. S. L. H. V., Uma Maheswara Rao, V. & Subba Rao, D. V., eds). New India Publishing Agency, New Delhi, pp. 259–574. 

Mallya, G., Mishra, V., Niyogi, D., Tripathi, S. & Govindaraju, R. S. 2016 Trends and variability of droughts over the Indian monsoon region. Weather Climate Extreme 12, 43–68. 

Marquardt, D. 1963 An algorithm for least-squares estimation of nonlinear parameters. Journal of the Society for Industrial and Applied Mathematics 11 (2), 431–441. 

McKee, T. B., Doesken, N. J. & Kliest, J. 1993 The relationship of drought frequency and duration to time scales. In: Proceedings of the 8th Conference on Applied Climatology, Anaheim, pp. 179–184. 

Mishra, A., Ines, A., Das, N., Khedun, C.P., Singh,V., Sivakumar, B. & Hansen, J. 2014 Anatomy ofa local-scale drought:Applicationof assimilated remote sensing products, crop model, and statistical methods to an agricultural drought study. Journal of Hydrology 526, 15–29. 

Nagler, P., Cleverly, J., Glenn, E., Lampkin, D., Huete, A. & Wan, Z. 2005 Predicting riparian evapotranspiration from MODIS vegetation 

indices and meteorological data. Remote Sensing of Environment 94 (1), 17–30. 

Niranjan, K., Rajeevam, M., Pao, D. S., Srivastava, A. K. & Preethi, B. 2013 On the observed variability of monsoon droughts over India. Weather Climate Extremes 1, 42–68. 

Osman, O., Semih, E. & Filiz, D.-C. 2014 Use of Landsat land surface temperature and vegetation indices for monitoring drought in the Salt Lake, Basin Area, Turkey. The Scientific World Journal 2014, 142939. 

Pandya, P. & Gontia, N. K. 2023 Development of drought severity–duration–frequency curves for identifying drought proneness in semi-arid regions. Journal of Water and Climate Change 14 (3), 824–842. 

Pandya, P., Kumarkhaniya, R., Parmar, R. & Ajani, P. 2020 Meteorological drought analysis using standardized precipitation index. Current World Environment 15 (3), 477–486. 

Downloaded from iwaponline.​com/​jwcc/​article-pdf/​14/​12/​4729/​1349676/​jwc0144729.​pdf by guest 

Journal of Water and Climate Change Vol 14 No 12, 4746 

Pandya, P., Gontia, N. K. & Parmar, H. V. 2022 Development of PCA-based composite drought index for agricultural drought assessment using remote-sensing. Journal of Agrometeorology 24 (4), 384–392. 

- Prasad, N. R., Patel, N. R. & Danodia, A. 2021 Crop yield prediction in cotton for regional level using random forest approach. Spatial Information Research 29, 195–206. 

Reed, R. & Marks, R. J. 1999 Neural Smiting: Supervised Learning in Feedforward Artificial Neural Networks. The MIT Press, Cambridge, MA, p. 360. 

Roell, Y. E., Amelie, B., Moller, P. G., Mette, B. G. & Morgens, H. G. 2020 Comparing a random forest based prediction of winter wheat yield to historical yield potential. Agronomy 10, 395. 

Sayago, S. & Bocco, M. 2018 Crop yield estimation using satellite images: Comparison of linear and non-linear models. AgriScientia 35, 1–9. 

Segal, M. R. 2003 Machine Learning Benchmarks and Random Forest Regression. Kluwer Academic Publishers, Netherlands. 

Shahhosseini, M., Hu, G. & Archontoulis, S. V. 2020 Forecasting corn yield with machine learning ensembles. Frontiers in Plant Science 11, 1120. 

Singh, T. P., Nandimath, P., Kumbhar-Patkar, V., Das, S. & Barne, P. 2021 Drought risk assessment and prediction using artificial intelligence over the southern Maharashtra state of India. Modeling Earth Systems and Environment 7, 2005–2013. 

Steduto, P., Hsiao, T., Fereres, E. & Raes, D. 2012 Crop Yield Response to Water. Food Agricultural Organization, United Nations, pp. 6–9. 

Tsakiris, G. & Vangelis, H. 2005 Establishing a drought index incorporating evapotranspiration. European Water 9–10, 3–11. 

Tuvdendorj, B., Wu, B., Zeng, H., Gantsetseg, B. & Nanzad, L. 2019 Determination of appropriate remote sensing indices for spring wheat 

yield estimation in Mongolia. Remote Sensing 11, 2568. 

Van Rooy, M. P. 1965 A rainfall anomaly index independent of time and space. Notos 14, 43–48. 

Vicente-Serrano, S. M., Beguería, S. & López-Moreno, J. I. 2010 A multiscalar drought index sensitive to global warming: The standardized precipitation evapotranspiration index. Journal of Climate 23, 1696–1718. 

- Zhang, L., Linlin, X., Shirong, P. & Wang, T. 2014 The basic principle of Random forest and its applications in Ecology—A case study of Pinusyunnanensis. ActaEcologicaSinica 34 (3), 650–659. 

First received 1 July 2023; accepted in revised form 22 November 2023. Available online 1 December 2023 

Downloaded from iwaponline.​com/​jwcc/​article-pdf/​14/​12/​4729/​1349676/​jwc0144729.​pdf by guest 

