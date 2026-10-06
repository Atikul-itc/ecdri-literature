Agricultural Water Management 286 (2023) 108405 



Contents lists available at ScienceDirect 

# Agricultural Water Management 

journal homepage: www.elsevier.com/locate/agwat 



## Evaluating established deep learning methods in constructing integrated remote sensing drought index: A case study in China 



### Zhenheng Xu, Hao Sun<sup>*</sup> , Tian Zhang, Huanyu Xu, Dan Wu, JinHua Gao 

_College of Geoscience and Surveying Engineering, China University of Mining and Technology-Beijing, Beijing 100083, China_ 

##### A R T I C L E I N F O 

##### A B S T R A C T 

Handling Editor - Dr R Thompson Agricultural drought seriously threatens the food and ecological security of most of the world’s developing countries. Data-driven integrated agricultural drought index with remote sensing provides an effective tool to _Keywords:_ monitor, evaluate, and predict the agricultural drought. However, there is still a lack of comprehensive analytical Agricultural drought work on taking the most effective machine learning (ML) and deep learning (DL) methods to construct such Remote sensing integrated drought index. In other words, it is still unclear whether the recent DL methods can improve inteData driven grated drought monitoring as compared with the currently widely used ML methods. Therefore, we critically Deep learning Machine learning evaluated the performances of four representative DL methods (represents the four currently popular DL network Inductive bias types) i.e., Entity Embedding Deep Neural Network (EEDNN), One-dimensional Convolutional Neural Network (1D-CNN), Gated Recurrent Unit (GRU), and Self-Attention Mechanism (SAM) and three widely used tree-based ML methods i.e., Cubist, Random Forest (RF), and Light Gradient Boosting Machine (LGBM), through constructing a QuickDRI like integrated drought index (abbreviated as QuickDRI-China). About 30 years of meteorological data, 14 years of remote sensing data, and various biophysical variables in China such as land use/land cover, available water capacity, irrigated agriculture, elevation, and ecoregion were employed in this study. Results showed that the EEDNN performed best, followed by the RF and LGBM, and then the other methods including the currently wide used Cubist, according to the station accuracy evaluations, spatial description evaluations, and responses to specific drought event. The tree-based ML methods such as RF and LGBM are still competitive in constructing the integrated agricultural drought index at the current stage. However, the higher accuracy, the smoother spatial description, and the more responsive ability of the EEDNN demonstrate great potential of DL methods. The future integrated agricultural drought monitoring with remote sensing should develop a specialized DL network for heterogeneous agricultural drought features. 

#### **1. Introduction** 

Drought is a recurring, destructive and complex extreme climate event that occurs in most parts of the world (Asadi Zarch et al., 2015; Dai, 2011; Vicente-Serrano et al., 2020). It is generally classified into four types: meteorological, agricultural, hydrological, and socioeconomic (Wilhite and Glantz, 1985). Among them, agricultural drought refers to the phenomenon of impaired plant function due to lack of soil moisture, which can lead to reduced or total failure of crops and forages (Jiao et al., 2019). Agricultural drought seriously threatens the security of food and socio-economics, causing direct economic losses of billions of dollars every year, and with global climate change, this threat is still intensifying (AghaKouchak et al., 2015; Dai, 2013; Gao et al., 2019; 

Naumann et al., 2021). Therefore, real-time and accurate drought monitoring is particularly important, which can provide decision makers with the necessary information to take appropriate response actions to reduce drought losses (Rhee and Im, 2017). 

The most effective and commonly used approach for agricultural drought monitoring is to construct suitable drought indices, which can be defined as variables used to describe the physical characteristics of drought such as severity, spatial extent, and duration (Hao and Singh, 2015). Historically, the traditional drought indices were based on ground stations (West et al., 2019). The station-based drought indices are mainly calculated from the measured values of precipitation, temperature, and soil moisture at ground stations. Among them, Palmer Drought Severity Index (PDSI) (Palmer, 1965), Standardized 

* Correspondence to: College of Geoscience and Surveying Engineering, China University of Mining and Technology - Beijing, Ding No.11 Xueyuan Road, Haidian District, Beijing 100083 PR China. 

_E-mail address:_ sunhao@cumtb.edu.cn (H. Sun). 

https://doi.org/10.1016/j.agwat.2023.108405 

Received 28 February 2023; Received in revised form 16 May 2023; Accepted 6 June 2023 Available online 11 June 2023 

0378-3774/© 2023 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/bync-nd/4.0/). 

_Agricultural Water Management 286 (2023) 108405_ 

_Z. Xu et al._ 

Precipitation Index (SPI) (McKee et al., 1993), Standardized Precipitation Evapotranspiration Index (SPEI) (Vicente-Serrano et al., 2010), etc. are widely used. The advantages of station-based drought indices are their reliability and long-term observations (Asadi Zarch et al., 2015). However, agricultural drought is a regional event, and the stations are distributed unevenly and discontinuously in space, it cannot well describe the detailed characteristics of the regional spatial distribution of drought (Beck et al., 2017; Hao et al., 2015). 

With the advent and development of remote sensing technology, benefiting from the large-scale and time-sensitive advantages of satellite observation, a paradigm shift occurred in drought monitoring (West et al., 2019). The remote sensing-based drought indices are mainly developed based on the land surface temperature, rainfall, soil moisture, vegetation coverage and other information observed by satellites. The commonly used remote sensing-based drought indices include: Vegetation Condition Index (VCI) (Felix N. F.N. Kogan, 1995; Felix N. FelixN. Kogan, 1995), Temperature Condition Index (TCI) (Kogan, 1995), Enhanced Vegetation Index (EVI) (Huete et al., 2002), Vegetation Drought Index (VDI) (Sun et al., 2013), etc. The advantages of remote sensing-based drought indices are that they can carry out large-scale continuous coverage of drought monitoring and can effectively describe the detailed spatial heterogeneity of drought (Sun et al., 2017; Zhang and Jia, 2013). However, due to the influence of uncertain atmospheric conditions and retrieval model errors, the accuracy of remote sensing-based drought indices still has some problems (Feng et al., 2019; Zhang et al., 2019). And a single drought index cannot fully describe the complex characteristics of agricultural drought (Jiao et al., 2019). 

As more and more remotely sensed data became available, integrated agricultural drought monitoring indices were developed. Integrated agricultural drought monitoring uses a variety of remote sensing, ground station, and geographic background data, which can more comprehensively describe the characteristics of agricultural drought and improve the accuracy of drought monitoring (Hao and Singh, 2015; Jiao et al., 2021). Among them, the integrated drought monitoring based on data-driven methods is one of the most important mainstreams (Jiao et al., 2021). Brown et al. (2008) integrated station-based drought indices (SPI, PSDI), remote sensing vegetation drought indices, and other biophysical information to construct the Vegetation Drought Response Index (VegDRI) based on the Cubist method. The VegDRI can produce a 1 km U.S. drought map in near real-time. Tadesse et al. (2017) used the same approach to generate the VegDRI-Canada for agricultural drought monitoring. Subsequently, Earth Resources Observation and Science (EROS) Center developed the Quick Drought Response Index (QuickDRI) based on a similar technical framework, which can effectively reflect short-term drought conditions and capture sudden drought events. In addition, Park et al. (2016) used tree-based machine learning methods such as Random Forest (RF), Boosted regression trees, and Cubist to fuse 16 remote sensing drought factors with station-based SPI, and the generated integrated drought maps showed strong visual consistency with the U.S. Drought Monitor (USDM) maps. Based on SPI and EVI, Roodposhti et al. (2017) used Support Vector Machine (SVM) to generate a drought sensitivity map under the consideration for geographic background data, which can effectively reflect the drought sensitivity spatiotemporal pattern of vegetation coverage. Feng et al. (2019) screened 30 remotely sensed drought factors from MODIS and TRMM satellite sensors, and used machine learning methods to perform a data-driven fusion of remotely sensed drought factors and station-based SPEI, which successfully mapped the agricultural drought in southeastern Australia and the map correlated well with crop yields. 

Data-driven methods play an important role in integrated drought monitoring, which directly affect the accuracy of drought monitoring. In previous research, data-driven mostly used machine learning methods, the most representative of which are tree-based methods such as RF, Cubist (Feng et al., 2019; Park et al., 2016; Rhee and Im, 2017). In recent years, deep learning has developed rapidly and been widely used in various fields (LeCun et al., 2015). Deep learning has good nonlinear 

fitting ability and high data-driven upper limit, which is very suitable for describing complex drought phenomena (Yuan et al., 2020). Some studies have begun to use deep supervised learning as the data-driven method for integrated drought monitoring, and most of the deep learning techniques used in these studies are Deep Neural Network (DNN), also known as Multi-Layer Perceptron (MLP) (Alizadeh and Nikoo, 2018; Feng et al., 2019; Liu et al., 2020; Prodhan et al., 2021; Shen et al., 2019). But, the results of some studies are inconsistent. Alizadeh and Nikoo (2018) compared the performance of MLP and four machine learning methods (including tree-based method), and found that MLP performed best. The results reported by Feng et al. (2019) showed that the tree-based machine learning method performed better than MLP. Whether deep learning can effectively improve integrated drought monitoring is still unclear. In addition, many popular deep learning techniques, such as Convolutional Neural Network (CNN) (Alzubaidi et al., 2021), Recurrent Neural Network (RNN), and Transformer based on Attention Mechanism (AM) (Vaswani et al., 2017), have not been fully explored for their ability to monitor drought. There is still a lack of comprehensive analytical work on taking the most effective machine learning and deep learning methods to construct the integrated drought index. In other words, it is still unclear whether the deep learning methods can improve integrated drought monitoring as compared with the currently widely used machine learning methods. 

Therefore, based on the QuickDRI framework, this paper systematically compares the drought monitoring performance of four currently popular deep learning techniques and three tree-based methods; four deep learning techniques are: DNN, CNN, RNN, AM, and three treebased methods are: Cubist, the original model in QuickDRI framework, RF, which performed well in previous integrated drought monitoring research, Light Gradient Boosting Machine (LGBM), which is an advanced ensemble learning model. The overarching objective of this paper is to comprehensively explore and analyze the data-driven capabilities of deep learning for integrated drought monitoring, and provide a reference for the selection of data-driven methods. The specific research objectives of this paper are: (1) According to mainstream deep supervised learning technologies such as DNN, CNN, RNN, and AM, the specific deep learning network architectures are used or designed respectively. The integrated drought monitoring accuracy of different deep learning networks and tree-based methods is evaluated based on ground stations. (2) Comparing the drought spatial distribution performance of different data-driven methods. (3) Comparing the responses to typical drought events of different data-driven methods. (4) Generating QuickDRI-China based on the best data-driven method. 

#### **2. Materials and methods** 

#### _2.1. Study area_ 

The study area is China (Fig. 1), latitude 4<sup>◦</sup> N-53<sup>◦</sup> 30<sup>′</sup> N and longitude 73<sup>◦</sup> 40<sup>′</sup> E-135<sup>◦</sup> 05<sup>′</sup> E. China’s terrain is diverse, including plains, mountains, hills, plateaus, and basins. In terms of climate, it can be divided into the eastern monsoon region, the northwest arid and semi-arid region, and the Qinghai-Tibet alpine region. China’s complex terrain and climatic conditions result in diverse drought situations, providing an ideal opportunity to explore the integrated drought monitoring capabilities of different data-driven methods. 

#### _2.2. QuickDRI-China and input data_ 

#### _2.2.1. The overall framework of QuickDRI-China_ 

The QuickDRI is an integrated drought monitoring index that uses the data-driven method to integrate data from multiple sources such as ground stations, remote sensing satellites, and biophysical information to detect short-term changes and rapid intensification of drought conditions. The overall flowchart of QuickDRI-China is shown in Fig. 2 First, the remote sensing and biophysical variable values at ground 

2 

_Agricultural Water Management 286 (2023) 108405_ 



**Fig. 1.** The study area and the 1724 weather stations used in the study. 



**Fig. 2.** Overall flowchart of QuickDRI-China. Details of the input data are in Table 1. The detailed technical route of step (2) is shown in Fig. 3. QuickDRI: quick drought response index; SPI: standardized precipitation index; SPEI: standardized precipitation evapotranspiration index; SVI: standardized vegetation index; SOSA: start of season anomaly; ESI: evaporative stress index; SMA: soil moisture anomaly; LULC: land use/land cover; AWC: available water capacity; IrrAg: irrigated agriculture; Ele: elevation; Eco: ecoregion. 

3 

_Agricultural Water Management 286 (2023) 108405_ 

station locations were extracted, together with the station-based climate variables (SPI, SPEI), to generate the feature variables dataset. The station-based SPEI is the dependent variable, and the remaining features are the independent variables. Details of feature variables are shown in Table 1. Then, the feature variables dataset was trained by data-driven method to develop the QuickDRI model. Dataset generation and model development were organized by month from January to December. Finally, the independent variable raster data were input into the developed QuickDRI model to draw the QuickDRI map. In this study, the data-driven step evaluated and compared the integrated drought monitoring performance of four deep learning techniques (DNN, CNN, RNN, AM) and three tree-based methods (Cubist, RF, LGBM). The best performing one was chosen as the data-driven method for developing the QuickDRI-China. 

#### _2.2.2. Climate variables_ 

The 1-month time scale SPI and SPEI were calculated based on monthly cumulative precipitation and monthly mean temperature at ground stations over a 30-year period from 1985 to 2014. The weather station dataset (Daily meteorological dataset of basic meteorological elements of China National Surface Weather Station) used in the study comes from the China Meteorological Data Service Center (CMDC; https://data.cma.cn) and The National Tibetan Plateau Data Center (TPDC; http://data.tpdc.ac.cn/). This dataset contains daily measurements of basic meteorological elements at 2474 stations in China from 1951 to 2014. First, the monthly average temperature and monthly cumulative precipitation of each month from 1985 to 2014 were calculated. Months with valid temperature measurements greater than 20 days in a single month and without any missing day of precipitation 

**Table 1** 

Details of feature variables for the QuickDRI-China. 

|Feature Variable|Type|Acronym|Source - dataset|Source<br>Format|
|---|---|---|---|---|
|Standardized<br>Precipitation Index|Climate|SPI|CMDC/TPDC<br>-Weather<br>Stations|ASCII|
|Standardized<br>Precipitation|Climate|SPEI|CMDC/TPDC<br>-Weather|ASCII|
|Evapotranspiration<br>Index|||Stations||
|Standardized|Satellite|SVI|CAS CNIC GDC-|500 m|
|Vegetation Index|||MODND1M|raster|
|Start of Season<br>Anomaly|Satellite|SOSA|LP DAAC -<br>MCD12Q2.006|500 m<br>raster|
|Evaporative Stress|Satellite|ESI|SERVIR|5 km|
|Index|||GLOBAL - ESI|raster|
|Soil Moisture<br>Anomaly|Satellite|SMA|NASA GES DISC<br>- FLDAS|0.1<sup>◦</sup>raster|
|Land use/Land cover|Biophysical|LULC|LP DAAC -<br>MCD12Q1.006|500 m<br>raster|
|Available Water<br>Capacity|Biophysical|AWC|ISRIC - SoilGrids|250 m<br>raster|
|Irrigated Agriculture|Biophysical|IrrAg|NBS -<br>Agricultural<br>Statistics&<br>LP DAAC<br>-MCD12Q1.006|500 m<br>raster|
|Elevation|Biophysical|Ele|CGIAR - SRTM<br>DEM v4|90 m<br>raster<br>i|
|Ecoregion|Biophysical|Eco|RESOLVE -<br>Ecoregions|shapefile|



Note: QuickDRI: quick drought response index; CMDC: China Meteorological Data Service Center; TPDC: National Tibetan Plateau Data Center; CAS CNIC GDC: Geospatial Data Cloud site, Computer Network Information Center, Chinese Academy of Sciences; LP DAAC: Land Processes Distributed Active Archive Center; GES DICS: Goddard Earth Sciences Data and Information Services Center; ISRIC: International Soil Reference and Information Center; NBS: National Bureau of Statistics of China; CGIAR: Consultative Group for International Agricultural Research. 

in a single month were considered valid months, and all stations with invalid months were removed. Then, the SPI and SPEI were calculated using the R-Package ’SPEI’ (https://spei.csic.es) developed by Santiago Beguería and Sergio M. Vicente-Serrano. Finally, 1-month SPI and SPEI of 1724 stations from 1985 to 2014 were obtained, and the location distribution is shown in Fig. 1. 

#### _2.2.3. Remote sensing variables_ 

_2.2.3.1. Standardized vegetation index (SVI)._ The SVI (Peters et al., 2002) is a standardization of NDVI deviations from a historical normal, which can effectively reflect the vegetation status in areas with varying drought conditions. The formula for calculating SVI is: _SVI_ = ( _V_ − _Vμ_ ) _/Vσ_ . In the formula, V is the NDVI value of a certain time period in a year, _Vμ_ and _Vσ_ respectively represent the mean and standard deviation of V in the benchmark long-term historical year. In the study, the 1-month SVI were calculated based on the monthly 500 m NDVI data from 2001 to 2014. The NDVI dataset (MODND1M) is provided by Geospatial Data Cloud site, Computer Network Information Center, Chinese Academy of Sciences (CAS CNIC GDC; http://www.gscloud.cn). MODND1M is generated by processing MOD09GA. 

_2.2.3.2. Start of season anomaly (SOSA)._ The SOSA (Brown et al., 2008) represents the temporal difference between the start of the growing season in a given year and the historical average, which can be used to quantitatively characterize the temporal variation of vegetation phenology in different years. The formula of SOSA is: _SOSAk_ = _STk_ − _STμ_ . In the formula, _SOSAk_ is the SOSA of year k, _STk_ is the start time of the growing season in that year, and _STμ_ is the average start time of the growing season in the historical year. The start time of the growing season were obtained from the MCD12Q2.006 product provided by The Land Processes Distributed Active Archive Center (LP DAAC; https ://lpdaac.usgs.gov/). This product provides the time estimates of vegetation phenology on a global scale with a spatial resolution of 500 m, and has been published annually since 2001. In the study, SOSA was calculated for each year based on the start time of the growing season from 2001 to 2014. 

_2.2.3.3. Evaporative stress index (ESI)._ The monthly ESI (Anderson et al., 2011) used in the study comes from the Evaporative Stress Index product provided by SERVIR GLOBAL (https://servirglobal.net/). This product has a spatial resolution of 5 km and is available on both 4-week and 12-week time scales. In the study, the 4-week time scales product was used as the monthly ESI (Anderson et al., 2007; Hain and Anderson, 2017), and downloaded data for each month from 2001 to 2014. 

_2.2.3.4. Soil moisture anomaly (SMA)._ The SMA describes the deviation of soil moisture condition for a given period of a year from the soil moisture climatology for that period (Gao et al., 2016). The SMA calculation formula (Gao et al., 2016; Orlowsky and Seneviratne, 2013) used in the study is: _SMA_ = ( _SM_ − _SMμ_ ) _/SMσ_ . In the formula, SM is the 0–100 cm soil moisture content of a certain month, _SMμ_ and _SMσ_ represent the mean and standard deviation of SM for all historical years (2001–2014). The soil moisture data used in this study came from the Famine Early Warning Systems Network (FEWS NET) Land Data Assimilation System (FLDAS) dataset (McNally, 2018; McNally et al., 2017) provided by NASA Goddard Earth Sciences Data and Information Services Center (GES DISC). This dataset has a spatial resolution of 0.1<sup>◦</sup> and a temporal resolution of 1 month. 

#### _2.2.4. Biophysical variables_ 

_2.2.4.1. Land use/Land cover (LULC)._ The LULC data from 2001 to 2014 used in the study is the MCD12Q1.006 product provided by LP DAAC. This product provides global land cover with a spatial resolution 

4 

_Agricultural Water Management 286 (2023) 108405_ 

_Z. Xu et al._ 

of 500 m, and is published annually. 

_2.2.4.2. Available water capacity (AWC)._ The root-zone available water capacity data comes from the SoilGrids250m (Hengl et al., 2017) dataset provided by International Soil Reference and Information Center (ISRIC) - World Soil Information (https://data.isric.org/). This dataset has a spatial resolution of 250 m and contains the available soil water capacity until wilting point at 7 standard depths. Since the depth of vegetation roots is generally around 1–1.5 m, the data at a depth of 200 cm was used in the study. 

_2.2.4.3. Irrigated agriculture (IrrAg)._ The IrrAg (Brown et al., 2008) represents the proportion of irrigated farmland area to total farmland area in an administrative unit. The IrrAg value is assigned to the pixels whose land cover is farmland in the administrative region, and the non-farmland area is set to a constant background value of 0, which means that there is no irrigation. In the study, Chinese prefecture-level cities were taken as administrative units. The statistical data of farmland effective irrigated area and total farmland area are obtained from the websites of provincial statistics bureaus (http://www.stats.gov.cn), and the land cover data is the MCD12Q1.006 product. The IrrAg maps with 500 m spatial resolution for each year from 2001 to 2014 were generated. 

_2.2.4.4. Elevation._ The elevation data comes from the SRTM Digital Elevation Data Version 4 dataset (Reuter et al., 2007) provided by Consultative Group for International Agricultural Research-Consortium for Spatial Information (CGIAR-CSI; https://srtm.csi.cgiar.org). This dataset provides global elevation information with a spatial resolution of 90 m. 

_2.2.4.5. Ecoregion._ The ecoregion data comes from the RESOLVE Ecoregions dataset (Dinerstein et al., 2017) provided by RESOLVE Biodiversity and Wildlife Solutions (https://ecoregions.appspot.com/). This dataset includes descriptions of 846 terrestrial ecoregions around the world. 

#### _2.3. Training and evaluation of data-driven step_ 

Training and accuracy evaluation of the QuickDRI models based on different deep learning networks and tree-based methods are shown in Fig. 3. This process was trained once every month based on the dataset of that month, a total of 12 times from January to December. The specific process is as follows: (1) The data from 2001 to 2012 in dataset of a certain month was used as the training set and validation set for hyperparameter tuning. (2) Hyperparameter tuning for all data-driven methods using 5-fold cross-validation and Bayesian optimization. The optimal hyperparameters of different deep learning networks and treebased methods were obtained. (3) The optimal hyperparameters were used to develop the QuickDRI models of different data-driven methods. (4) The data of 2013 and 2014 was used as the test set for unbiased estimation of QuickDRI models based on different data-driven methods. 

_2.3.1. Deep learning network architectures_ 

The essence of data-driven integrated drought monitoring is a supervised learning process. DNN, CNN, RNN, and AM are currently the four most widely used deep supervised learning techniques. In the study, specific network architecture was used or designed respectively, and all were implemented by PyTorch (https://pytorch.org/). 

_2.3.1.1. Entity embedding deep neural network (EEDNN)._ In this study, EEDNN (Guo and Berkhahn, 2016) is the specific architecture implementation of DNN, as shown in Fig. 4. This network uses the classic two fully connected layer architecture of DNN, which can effectively fit functions of any complexity in theory (Goodfellow et al., 2016). And the 



**Fig. 3.** Training and accuracy evaluation of the QuickDRI models based on different data-driven methods. EEDNN, 1D-CNN, GRU, and SAM correspond to the specific network architecture implementations of the four deep learning technologies respectively. QuickDRI: quick drought response index; EEDNN: entity embedding deep neural network; 1D-CNN: one-dimensional convolutional neural network; GRU: gated recurrent unit; SAM: self-attention mechanism; RF: random forest; LGBM: light gradient boosting machine; R<sup>2</sup> : coefficient of determination; RMSE: root mean square error. 

embedding layer using in the network can effectively deal with the categorical variables (LULC, Eco) in this study. 

_2.3.1.2. One-dimensional convolutional neural network (1D-CNN)._ The CNN was originally used to analyze two-dimensional images (2D-CNN) (Krizhevsky et al., 2012), and later developed architectures for analyzing time series (1D-CNN) and analyzing spatiotemporal information (3D-CNN). Since the integrated drought monitoring variables used in the study do not have spatial structure, in order to evaluate the ability of CNN, the time series data was used for supervised learning. In the study, the independent variable time series with a 3-month scale (current month and the previous two months) was used as input to regression with the dependent variable of the current month. The 1D-CNN architecture shown in Fig. 5 was designed to analyze time series, the most important of which is the size of the convolution kernel. In order to take advantage of CNN’s multi-scale analysis, referring to the TextCNN architecture (Kim, 2014), 1D-CNN uses convolution kernels of three sizes: 1-month, 2-month, and 3-month to convolve the time series. Meanwhile, considering that closer time nodes have a stronger impact on drought monitoring, 1-month size only convolutes the last month of the time series, 2-month convolutes the last two months, and 3-month convolutes all three months. 

_2.3.1.3. Gated recurrent unit (GRU)._ The RNN technology in this study refers to the generalized Recurrent Neural Network. Common RNN 

5 

_Agricultural Water Management 286 (2023) 108405_ 

_Z. Xu et al._ 



**Fig. 4.** Schematic diagram of EEDNN (Entity Embedding Deep Neural Network) architecture. The interpretation of architectural hyperparameters is shown in Table 2. 



**Fig. 5.** Schematic diagram of 1D-CNN (One-dimensional Convolutional Neural Network) architecture. The interpretation of architectural hyperparameters is shown in Table 2. 

architectures include Elman RNN, GRU, LSTM (Long Short-Term Memory), etc. In this study, GRU (Cho et al., 2014) was used as the specific network architecture of RNN, as shown in Fig. 6. Compared with Elman RNN and LSTM, GRU is an advanced network architecture, which can take into account lower time cost and good operation effect (Chung et al., 2014). Because the input data of GRU is generally sequence data, the independent variable time series with a 3-month scale was used as input like 1D-CNN. 

#### _2.3.1.4. Self-attention mechanism (SAM)._ The network using the Atten- 

tion Mechanism (Niu et al., 2021) is an emerging network type in recent years, the most representative one is Transformer based on Self-Attention Mechanism (Vaswani et al., 2017). The Self-Attention Mechanism can obtain the correlation between variables, thereby 

highlighting important variables. The network architecture of SAM in the study is shown in Fig. 7. In order to enable categorical variables to perform self-attention analysis effectively, the embedding technology is used for dense encoding. The output dimension of encoding is 1, which is to prevent the multi-dimensional output classification variables from causing ambiguity in the meaning of the correlation coefficient with other variables. 

#### _2.3.2. Tree-based machine learning methods_ 

In the study, three typical tree-based methods were also used for integrated drought monitoring data-driven: Cubist, the original model in the QuickDRI framework, RF, which performed well in previous integrated drought monitoring research, LGBM, which is an advanced ensemble learning model. The three tree-based methods are representative. Cubist is a traditional decision tree model, which represents a non-ensemble learning method. RF and LGBM represent the two mainstream ensemble learning methods Bagging and Boosting, respectively. 

_2.3.2.1. Cubist._ Cubist is a rule-based decision tree model (Quinlan, 1993, 1992). It can build rule-based linear models between multiple variables and target values, and these linear models are included in the leaf nodes of the tree. Cubist has the advantage that the volume of the model is small with good accuracy. And the rule-based model is more interpretable. In the study, the Cubist package of R (https://cran.r-pr oject.org/web/packages/Cubist) developed by RuleQuest Research (https://www.rulequest.com/) was used for implementation. 

_2.3.2.2. Random forest (RF)._ RF is an ensemble learning model that includes many decision trees (Breiman, 2001; Ho, 1995). The ensemble 



**Fig. 6.** Schematic diagram of GRU (Gated Recurrent Unit) architecture. The interpretation of architectural hyperparameters is shown in Table 2. 

6 

_Agricultural Water Management 286 (2023) 108405_ 

_Z. Xu et al._ 



**Fig. 7.** Schematic diagram of SAM (Self-Attention Mechanism) architecture. The interpretation of architectural hyperparameters is shown in Table 2. 

learning strategy of the RF is Bagging, which trains the decision trees by randomly extracting training samples with retractions and randomly selecting feature subsets, and then using the average value returned by many decision trees as the predicted value of the RF. The introduction of two randomness makes the generalization ability of RF stronger and insensitive to missing values and outliers. In the study, the scikit-learn package of Python (https://scikit-learn.org/) (Pedregosa et al., 2011) was used to implement the RF. 

_2.3.2.3. Light gradient boosting machine (LGBM)._ LGBM (Ke et al., 2017) is an ensemble learning model based on Boosting strategy. LGBM is an efficient implementation of Gradient Boosting Decision Tree (GBDT) (Friedman, 2001). It builds new decision trees multiple times to fit the residual of the existing decision tree, so as to improve the prediction accuracy of the model, and uses the negative gradient of the loss function of the existing decision tree as the residual approximation. Compared with the same type of XGBoost (Chen and Guestrin, 2016), LGBM can achieve higher training efficiency and lower memory usage while maintaining high prediction accuracy, and also supports direct input of categorical variables. In the study, the LightGBM package of Python (https://lightgbm.readthedocs.io/) provided by Microsoft was used for implementation. 

#### _2.3.3. Dataset generation_ 

_2.3.3.1. Datasets of each month._ Two types of datasets were established in the study: tabular dataset and time-series dataset. The time-series dataset was to meet the time series input requirements of 1D-CNN and GRU. Both types of datasets were divided by month, each generating 12month datasets, and all generated datasets cover the time length from 2001 to 2014. Finally, 12 tabular datasets and 12 time-series datasets were generated. 

The specific steps to generate the datasets are as follows: (1) Generate the tabular datasets of each month. Every weather station is a sample. Extract the average values of the remote sensing and biophysical raster data within 5 km × 5 km at the location of the weather station as the independent variable values of the station sample. The station-based SPEI is the dependent variable of the sample. The reason for choosing a 5 km × 5 km window is to compromise the spatial resolution of each independent variable raster. (2) Based on the tabular datasets, generate the time-series datasets of each month. For a time-series sample, the tabular independent variables of the current month and the previous 

two months of a station were used to generate the 3-month scale timeseries independent variables, and the SPEI of the current month of the station was used as the dependent variable. (3) Since the independent variable data at some stations may have invalid null values in some months, it is necessary to remove the station samples with null values in the tabular datasets and time-series datasets of each month. After removing invalid samples, in order to ensure the comparability of tabular datasets and time-series datasets, it is necessary to ensure that the tabular datasets and time-series datasets of each month cover the same stations. Finally, only samples of stations that are common to both were kept in the datasets. 

_2.3.3.2. Data normalization and categorical variable encoding._ In order to eliminate the influence of abnormal samples and speed up the convergence of deep learning networks, it is necessary to normalize the continuous feature variables in the datasets. Commonly used normalization methods include z-score normalization and min-max normalization. In the study, SPEI, SPI, SVI, ESI, and SMA are z-score normalized data, so the remaining AWC, SOSA, Ele, and IrrAg need to be normalized. Because AWC and SOSA conform to the normal distribution, z- score was used for normalization. Ele and IrrAg do not conform to the normal distribution, so the min-max normalization was used. At the same time, most deep learning networks and tree-based methods cannot directly deal with categorical variables, one-hot encoding (Qu et al., 2019) was used for the two categorical variables of LULC and Eco. 

#### _2.3.4. Hyperparameter tuning_ 

Hyperparameters are an important factor affecting the performance of deep learning networks, so scientific hyperparameter tuning is necessary. In the study, there are training hyperparameters and architectural hyperparameters. The training hyperparameters mainly control the training process of the networks, and the architecture hyperparameters are used to control the architectural details of the networks. Training hyperparameters include: learning rate, number of epochs, regularization, and batch size. The learning rate and the number of epochs were dynamically determined by the learning rate scheduler and early stopping. The learning rate scheduler will continuously reduce the learning rate according to the loss of the validation set during training, so as to prevent the problem of non-convergence caused by too large initial learning rate or slow convergence caused by too small initial learning rate. The early stopping is to determine that the network has converged when the validation set loss does not decrease for n 

7 

_Agricultural Water Management 286 (2023) 108405_ 

_Z. Xu et al._ 

consecutive times (n = 150 in the study), and to stop the training early to prevent the network from overfitting. The L2 regularization was used and the batch size was set to 32 (Masters and Luschi, 2018). The architectural hyperparameters are different for each network and method, detailed in Table 2. 

In the study, 5-fold cross-validation and Bayesian optimization (Bergstra et al., 2011) were used for hyperparameter tuning. Data from 2001 to 2012 in the datasets of each month was used for the 5-fold cross-validation. In order to ensure the effectiveness of cross-validation, the data distribution of the validation set needs to be similar to that of the test set, so the data of two adjacent years was used as the validation set. In the 5 times of cross-validation, select 2007–2008, 2008–2009, 2009–2010, 2010–2011, 2011–2012 as the validation set in turn, and the remaining years data was used as the training set in each time. The results of cross-validation were used for Bayesian optimization, and the best combination of hyperparameters was finally returned. Bayesian optimization is a hyperparameter tuning method based on prior, which uses the performance of the hyperparameters that have been searched to infer the next hyperparameter tuning direction, thereby reducing the search space and greatly improving the search efficiency. In the study, the Hyperopt package of python (http://hyperopt.github.io/hyperopt) (Bergstra et al., 2013) was used to implement Bayesian optimization. 

#### _2.3.5. Evaluation method_ 

_2.3.5.1. Accuracy evaluation._ In order to evaluate the integrated drought monitoring accuracy of different deep learning networks and tree-based methods, the coefficient of determination (R<sup>2</sup> ) and root mean square error (RMSE) were used for quantitative evaluation. The evaluation metrics are as follows: 





In the formula, _N_ is the number of samples; _si_ and _qi_ are the real value of station-based SPEI and the predicted value of QuickDRI of sample _i_ , respectively. 

_2.3.5.2. Spatial distribution evaluation._ In the study, according to the 

**Table 2** 

Details of the architectural hyperparameters for each data-driven model. 

|Model|Hyperparameter|Interpretation|
|---|---|---|
|EEDNN|dim_FC1|The number of neurons in Fully Connected Layer 1.|
||dim_FC2<br>dim_Emb|The number of neurons in Fully Connected Layer 2.<br>The output dimension of Embedding encoding for<br>categorical variables.|
|1D-<br>CNN|dim_FC|The number of neurons in the Fully Connected Layer.|
|GRU|hidden_size<br>dim_FC|The number of features in the Hidden State.<br>The number of neurons in the Fully Connected Layer.|
|SAM|dim_QKV|The dimensions of the linear transformation for the<br>Q, K, V matrices, which represent different viewing<br>angles on the input variables.|
||dim_FC|The number of neurons in the Fully Connected Layer.|
|RF|max_depth|The maximum depth of the decision tree.|
||num_estimators|The number of decision trees.|
|LGBM|max_depth<br>num_leaves|The maximum depth of the decision tree.<br>The number of leaf nodes.|



Note: EEDNN: entity embedding deep neural network; 1D-CNN: onedimensional convolutional neural network; GRU: gated recurrent unit; SAM: self-attention mechanism; RF: random forest; LGBM: light gradient boosting machine. 

accuracy evaluation results, the data-driven methods with better performance were selected for the spatial mapping of QuickDRI-China. This is to further evaluate the spatial distribution (macroscale and microscale) performance and drought response ability of the QuickDRI-China generated by different data-driven methods. At the same time, the 0.5<sup>◦</sup> gridded 1-month scale SPEI of the Global SPEI database (https://spei.csi c.es/) (Beguería et al., 2022) was used as the reference data of the spatial distribution. 

#### **3. Result** 

#### _3.1. Accuracy evaluation_ 

Table 3 shows the R<sup>2</sup> and RMSE of the Quick models (January to December) of different data-driven methods, and Fig. 8 shows the corresponding boxplots. For each month, the method with the best performance on the evaluation metrics and the methods within 0.005 of the best metrics were considered as the preferred methods for the month. It can be seen from Table 3 that: (1) Both EEDNN and RF are the preferred method in 8 months. The EEDNN performed best in the 5 months of February, March, May, August, and November. The RF performed best in the three months of June, July and September. LGBM, 1D-CNN, and GRU are the preferred method in 6, 4, and 2 months, respectively. SAM and Cubist are the preferred method in only 1 month. (2) The months where RF is the preferred method show a tendency for RF to perform better for those months where the average goodness of fit is higher. June, July and September with the best performance of the RF are also the three months with the highest average goodness of fit, and the average R<sup>2</sup> are all greater than 0.95. The EEDNN does not show such a tendency, and performs well in months with high, medium, and low average goodness-of-fit. It shows that EEDNN is more adaptable to different month conditions. 

Fig. 8 shows the overall performance of the accuracy evaluation of the models of each month. The EEDNN performs best on median, outliers, and volatility. The LGBM has the next best median, but the outliers performed poorly. The median performance of RF is similar to that of 1D-CNN and GRU, but the outliers of RF are better. The medians of SAM and Cubist both perform poorly, and Cubist outliers also show poor performance. 

Based on the evaluation results of each month’s QuickDRI model, the performance of each data-driven method is ranked as follows: EEDNN _>_ RF _>_ LGBM _>_ 1D-CNN _>_ GRU _>_ SAM ≈ Cubist. The EEDNN performed the best overall, followed by the RF. They were the preferred methods in most months, and their boxplots performed well. The LGBM was the preferred method in half of the months, and the median performance was good, but the performance in March was poor. The performance of 1D-CNN and GRU was medium, and 1D-CNN was better than GRU. The SAM and Cubist performed poorly. 

Fig. 9 is a scatterplot of the QuickDRI predicted values and the station-based SPEI. It contains the predictions of all month’s QuickDRI models based on different data-driven methods, and the overall R<sup>2</sup> and RMSE are calculated. The overall accuracy evaluation metrics (R<sup>2</sup> / RMSE) from high to low is: EEDNN (0.914/0.299) _>_ RF (0.912/0.302) _>_ LGBM (0.908/0.308) _>_ 1D-CNN (0.907/0.310) _>_ SAM (0.905/0.313) ≈ GRU (0.904/0.314) _>_ Cubist (0.902/0.318). The EEDNN has the best performance, followed by the RF, they are in the tier 1 (highest accuracy); the LGBM and 1D-CNN are in the tier 2; the GRU and SAM are in the tier 3. Compared with other methods, the Cubist has more discrete outliers and relatively poor accuracy, it is in the tier lowest. 

Finally, considering the monthly and overall performance of each method, the accuracy evaluation ranking from high to low is: EEDNN _>_ RF _>_ LGBM _>_ 1D-CNN _>_ SAM ≈ GRU _>_ Cubist. Among them, The EEDNN and RF show obvious advantages over other methods, and they also represent deep learning method and tree-based method respectively. 

8 

_Z. Xu et al._ 

_Agricultural Water Management 286 (2023) 108405_ 

**Table 3** 

Accuracy evaluation results of the QuickDRI models (January to December) based on different data-driven methods. 

|Month|EEDNN|1D-CNN|GRU|SAM|Cubist|RF|LGBM|EEDNN|1D-CNN|GRU|SAM|Cubist|RF|LGBM|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||R<sup>2</sup>|||||||RMSE||||
|January|**0.7919**|**0.7881**|0.7831|0.7633|**0.7931**|0.7832|**0.7921**|**0.3518**|**0.3550**|0.3592|0.3753|**0.3509**|0.3591|**0.3517**|
|February|**0.8813**|0.8493|0.8547|0.8578|0.8733|0.8700|0.8642|**0.3142**|0.3540|0.3476|0.3438|0.3245|0.3287|0.3360|
|March|**0.7030**|0.6705|0.6582|0.6801|0.6406|**0.7022**|0.6520|**0.5759**|0.6066|0.6178|0.5976|0.6334|**0.5766**|0.6233|
|April|0.8554|**0.8569**|0.8376|0.8458|0.8333|0.8481|**0.8596**|0.3661|**0.3642**|0.3879|0.3780|0.3931|0.3752|**0.3608**|
|May|**0.9449**|0.9363|0.9363|0.9382|0.9348|**0.9429**|**0.9440**|**0.2297**|0.2470|0.2470|0.2432|0.2498|**0.2338**|**0.2315**|
|June|**0.9580**|0.9546|0.9570|0.9549|0.9527|**0.9598**|0.9554|**0.1863**|0.1937|0.1885|0.1930|0.1977|**0.1821**|0.1919|
|July|0.9773|0.9755|**0.9785**|0.9764|0.9753|**0.9790**|0.9776|0.1701|0.1770|**0.1656**|0.1736|0.1777|**0.1639**|0.1690|
|August|**0.9457**|**0.9439**|**0.9441**|**0.9443**|0.9429|**0.9442**|**0.9443**|**0.2264**|**0.2303**|**0.2297**|**0.2295**|0.2322|**0.2295**|**0.2295**|
|September|0.9664|0.9658|0.9654|0.9636|0.9619|**0.9712**|0.9648|0.1931|0.1946|0.1959|0.2009|0.2055|**0.1787**|0.1973|
|October|**0.8913**|0.8883|0.8830|0.8835|0.8763|**0.8935**|**0.8945**|**0.3033**|0.3074|0.3146|0.3140|0.3235|**0.3003**|**0.2988**|
|November|**0.9205**|**0.9177**|0.9149|0.9101|0.9041|0.9052|0.9071|**0.2466**|**0.2510**|0.2552|0.2623|0.2708|0.2693|0.2667|
|December|0.9355|0.9299|0.9294|0.9246|0.9300|**0.9398**|**0.9420**|0.2556|0.2664|0.2675|0.2764|0.2662|**0.2470**|**0.2423**|



Note: The bold represent the preferred data-driven methods for the month, including the method with the best performance on the evaluation metrics and the methods within 0.005 of the best metrics. QuickDRI: quick drought response index; EEDNN: entity embedding deep neural network; 1D-CNN: one-dimensional convolutional neural network; GRU: gated recurrent unit; SAM: self-attention mechanism; RF: random forest; LGBM: light gradient boosting machine; R<sup>2</sup> : coefficient of determination; RMSE: root mean square error. 



**Fig. 8.** The boxplot and dot plot of the accuracy evaluation metrics of the QuickDRI models (January to December) based on different data-driven methods. QuickDRI: quick drought response index; EEDNN: entity embedding deep neural network; 1D-CNN: one-dimensional convolutional neural network; GRU: gated recurrent unit; SAM: self-attention mechanism; RF: random forest; LGBM: light gradient boosting machine; R<sup>2</sup> : coefficient of determination; RMSE: root mean square error. 

#### _3.2. Spatial patterns of QuickDRI-China_ 

According to the above accuracy evaluation, the EEDNN and RF perform better, representing the best method for deep learning and treebased method, respectively. In order to further compare the integrated drought monitoring capabilities of these two methods, the spatial patterns of the QuickDRI-China generated by EEDNN and RF were compared in the study. 

As shown in Figs. 10 and 11, the QuickDRI-China generated by EEDNN and RF are indistinguishable in macroscopic spatial pattern. And they are all similar to the macroscopic spatial pattern of the 1-month scale SPEI of the Global SPEI database. This shows that the QuickDRIChina generated by both can accurately characterize the macroscopic spatial pattern of drought. 

Fig. 12 is a comparison of the micro-scale spatial distribution of the QuickDRI-China. The location is around Weishan Lake, the largest freshwater lake in northern China. It can be found that the QuickDRI based on EEDNN have richer spatial details than that based on RF, especially in October. In addition, the QuickDRI based on RF showed obvious boundary effect when describing regions with different drought degrees, as shown in August and September. The spatial distribution of the QuickDRI based on EEDNN is smoother, and there is no obvious boundary between regions of different drought degrees. 

#### _3.3. Responses to typical drought events_ 

From early July to mid-August 2013, a once-in-a-century drought occurred in southern China, involving 9 provinces and 2 provincial 

9 

_Z. Xu et al._ 

_Agricultural Water Management 286 (2023) 108405_ 



**Fig. 9.** The QuickDRI predicted values based on different data-driven methods vs. The station-based SPEI. Includes QuickDRI predicted values for all month’s models. The R<sup>2</sup> and RMSE represent the overall accuracy evaluation. QuickDRI: quick drought response index; SPEI: standardized precipitation evapotranspiration index; EEDNN: entity embedding deep neural network; 1D-CNN: one-dimensional convolutional neural network; GRU: gated recurrent unit; SAM: self-attention mechanism; RF: random forest; LGBM: light gradient boosting machine; R<sup>2</sup> : coefficient of determination; RMSE: root mean square error. 



**Fig. 10.** The QuickDRI-China (Spatial resolution 500 m) in March, June, September and December 2013. The first line is based on EEDNN, and the third line is based on RF. The second line is the 1-month scale SPEI of the Global SPEI database (Spatial resolution 0.5<sup>◦</sup> ) used as a reference. QuickDRI: quick drought response index; EEDNN: entity embedding deep neural network; RF: random forest; SPEI: standardized precipitation evapotranspiration index. 

municipalities (Yuan et al., 2016). During the same period, floods occurred in parts of Northwest China, North China and Northeast China. A rare spatial pattern of "drought in the south and flood in the north" appeared in China. Fig. 13 is the QuickDRI-China in July 2013, 

developed by EEDNN and RF respectively. It can be found that both of them have captured the severe drought in southern China well, and the monitored drought range is consistent with the relevant historical data (China Meteorological Administration, 2015). They also show the 

10 

_Agricultural Water Management 286 (2023) 108405_ 



**Fig. 11.** The QuickDRI-China in March, June, September and December 2014. The relevant information is the same as in Fig. 10. 



**Fig. 12.** The micro-scale spatial pattern of QuickDRI-China near Weishan Lake from August to October 2013. The first line is based on EEDNN, and the second line is based on RF. QuickDRI: quick drought response index; EEDNN: entity embedding deep neural network; RF: random forest. 

characteristics of "drought in the south and flood in the north" in the spatial pattern. The above shows that the QuickDRI-China developed by EEDNN and RF can effectively respond to macroscopic and large-scale drought events, and can accurately characterize their spatial patterns. 

In order to further compare the ability of the QuickDRI-China generated by EEDNN and RF to capture drought events in local areas. In the study, the drought monitoring in Hunan Province was further analyzed. As the most severe drought area, Hunan had the largest area of 

11 

_Agricultural Water Management 286 (2023) 108405_ 

_Z. Xu et al._ 



**Fig. 13.** The QuickDRI-China in July 2013. The left is developed based on EEDNN, and the right is developed based on RF. A rare and severe drought occurred in southern China that month. QuickDRI: quick drought response index; EEDNN: entity embedding deep neural network; RF: random forest. 



**Fig. 14.** Responses to local drought events. The QuickDRI-China of Hunan Province, July 2013. (a) The QuickDRI-China in Hunan Province developed by EEDNN. The red circle is the area where the more extreme drought events captured by the QuickDRI developed by EEDNN. (b) The QuickDRI-China in Hunan Province developed by RF. (c) In 2013, the amount of grain yield reduction in the counties of Hunan (excluding municipal districts), which were calculated by subtracting the total grain yield of each county in 2013 from the total grain yield of each county in 2012. The data comes from Hunan Provincial Bureau of Statistics (https://tjj.huna n.gov.cn/). QuickDRI: quick drought response index; EEDNN: entity embedding deep neural network; RF: random forest. 

12 

_Agricultural Water Management 286 (2023) 108405_ 

_Z. Xu et al._ 

crop damage and crop failure. As shown in Fig. 14, it can be found that compared with the QuickDRI developed by RF (Fig. 14 (b)), the QuickDRI based on EEDNN (Fig. 14 (a)) has detected more severe drought events in central Hunan. The region where these detected extreme drought events occurred coincided highly with the region where the 2013 grain yield reduction was most severe (Fig. 14 (c)). This shows that the QuickDRI based on EEDNN can more effectively capture extreme drought events at local scales. 

#### **4. Discussion** 

#### _4.1. Heterogeneous drought features and inductive biases of the datadriven methods_ 

In the study, according to the architectural characteristics of 1D-CNN and GRU, the time series variables were used for training. Although the information was increased, the accuracy was not as good as EEDNN. When we analyze the reasons from the inductive biases of each method, we can find that: many CNN and RNN network architectures, including 1D-CNN and GRU, are designed for homogeneous data such as audio, text and images from the beginning, that is, the nature of each feature input into the network is the same (Borisov et al., 2022; Katzir et al., 2021). For example, in text sequence data, each sequence node is a word text, and the coding features corresponding to each word text are homogeneous. Another example is image data, when the pixels at adjacent spatial positions of the image are sent as features to the convolution kernel for calculation (CNN convolution operation), the fundamental nature of different pixel features is the same. However, for most of today’s integrated drought indices (including the QuickDRI), the features often include a variety of numerical (continuous or discrete) variables and categorical variables with different nature, which is a kind of heterogeneous tabular data. When the data-driven methods (GRU and 1D-CNN) with homogeneous inductive bias are used to train heterogeneous drought data, there will inevitably be deviations from the expected results (Borisov et al., 2022). The same is true for the SAM. The Transformer based on the self-attention mechanism is carefully designed to train sequence data. When performing self-attention analysis, it is considered that there is homogeneity between different features. When analyzing heterogeneous integrated drought features, especially when the features contain categorical variables, the effectiveness of the self-attention mechanism will be greatly reduced. For the DNN, as a classic fully connected layer network, it does not have such a strong homogeneous inductive bias like RNN and CNN at the beginning of its design, and it is often used for nonlinear multiple regression of tabular data. At the same time, the EEDNN used in this paper itself improves the ability of the network to simultaneously process continuous and categorical variables on the basis of DNN (Guo and Berkhahn, 2016). The Embedding technology used in EEDNN has been proven to effectively improve the ability of the network to process heterogeneous data (Cheng et al., 2016). This shows that the inductive bias of EEDNN matches heterogeneous data and is more adaptable to heterogeneous features in integrated drought monitoring. In addition, studies have shown that proper regularization can make the Multi-Layer Perceptron (also known as DNN) more effective in dealing with heterogeneous tabular data (Kadra et al., 2021). In this study, the optimal L2 regularization was determined through the learning rate scheduler and early stopping, which may further improve the ability of EEDNN to deal with heterogeneous data. Finally, for the tree-based ensemble learning methods such as RF and LGBM, they are originally designed to solve tabular data, and naturally have a good ability to deal with heterogeneous tabular data (Grinsztajn et al., 2022). This is why the accuracy evaluation of RF and LGBM in this study is still excellent. However, tree-based methods have limitations in the spatial description of drought, which will be discussed in the next subsection. 

#### _4.2. Deep learning has unique advantages in describing the spatial distribution of drought_ 

From the results in Section 3.2, we can see that the QuickDRI developed by RF shows obvious "boundary effect" in the detailed spatial description, while the spatial description of the QuickDRI developed by EEDNN is relatively smooth. Drought is a continuous spatial event and spatial description must be considered in integrated drought monitoring. Many studies have shown that neural networks are biased towards low frequency (smooth) target functions; while tree-based methods, which learn piece-wise constant functions, favor irregular (non-smooth) patterns (Grinsztajn et al., 2022; Rahaman et al., 2019). A simulation experiment was also carried out in the study to verify this conclusion: Four methods were selected, including EEDNN and 1D-CNN with the highest accuracy of deep learning, and RF and LGBM with the highest accuracy of tree-based method. The two spatial continuous independent variables of ESI and SMA were simulated in the range of (− 2.5, 2.5) according to the step size of 0.01. Other continuous variables took the median, classification variables took the mode, and kept constant during the simulation. The QuickDRI models of July with the highest average R<sup>2</sup> and March with the lowest average R<sup>2</sup> were used for the experiment. The results of the simulation experiment are shown in Fig. 15. It can be found that the predicted values of QuickDRI based on the tree-based methods show obvious boundaries and strips, while the predicted values based on the deep learning methods are smooth without obvious boundaries. The non-smooth bias of the tree-based method has little effect on general tabular data that does not have spatial properties, and even shows advantages on some tabular data that obeys irregular patterns (Grinsztajn et al., 2022). But this non-smooth bias is fatal for tabular data that has spatial properties and requires continuous spatial distribution mapping. According to the Tobler’s first law of geography: For continuous spatial variables, closer locations mean closer values (Tobler, 1970). The smooth bias of the target function of deep learning makes the transition between the predicted values of the approximate independent variables smooth, and thus smooth in space. However, the non-smooth bias of the tree-based method may lead to a clear boundary between the predicted values of the approximate independent variables, which also leads to the "boundary effect" in the spatial description. This "boundary effect" is obviously inconsistent with the spatial continuity characteristics of drought events, while the smooth spatial description of deep learning is closer to the real situation. Therefore, we believe that for the events with spatial continuity characteristics including drought, the smooth inductive bias of deep learning has a natural advantage in spatial description. 

#### _4.3. Conception of specialized deep learning network for integrated drought monitoring_ 

Deep learning has a unique advantage in spatial description of drought because of its smooth bias of target function. At the same time, in terms of accuracy evaluation, EEDNN achieves higher accuracy results due to its weak homogeneous inductive bias, combined with embedding coding technology and appropriate regularization. However, considering the elaborate and complex design of EEDNN and the high time cost of hyperparameter tuning, it still does not show absolute advantages in accuracy evaluation compared with tree-based ensemble methods. Due to its better adaptability to heterogeneous data and lower cost of hyperparameter tuning, the tree-based ensemble methods still show strong competitiveness without considering the spatial description of drought. We believe that at the present stage, deep learning has improved the ability of integrated drought monitoring, which is more inclined to the unique advantages of deep learning in spatial description, as well as its potential to achieve higher prediction accuracy than the traditional tree-based ensemble methods through appropriate architecture design and hyperparameter tuning. This potential of deep learning still has great room for improvement, and there is still a lack of mature 

13 

_Agricultural Water Management 286 (2023) 108405_ 

_Z. Xu et al._ 



**Fig. 15.** Simulation predictions of the QuickDRI based on different data-driven methods. Simulation prediction was performed using continuous variables ESI, SMA (step size 0.01, range − 2.5 to 2.5), and the rest of the variables were kept constant. The first row is the simulated predicted values of the QuickDRI models of March (the month with the lowest average R<sup>2</sup> ), and the second row is that of July (the month with the highest average R<sup>2</sup> ). The corresponding data-driven methods from left to right are EEDNN, 1D-CNN, RF, LGBM. ESI: evaporative stress index; SMA: soil moisture anomaly; QuickDRI: quick drought response index; EEDNN: entity embedding deep neural network; 1D-CNN: one-dimensional convolutional neural network; RF: random forest; LGBM: light gradient boosting machine; R<sup>2</sup> : coefficient of determination. 

deep learning technology that specializes in processing heterogeneous tabular data. In the future, coupling the respective advantages of deep learning and tree-based methods may become a feasible improvement method. The tree-based models are not differentiable and cannot be directly trained jointly with deep learning modules. Therefore, this coupling is more inclined to combine the inductive bias of the tree-based method that match heterogeneous data, and develop a specialized deep learning network for heterogeneous tabular data. The advantages of this specialized network are: (1) It has a good ability to handle heterogeneous data; (2) It maintains the advantages of deep learning in spatial description; (3) It can be combined with other deep learning networks for joint training. With the increase of drought-related data acquisition means and the increase of data volume, drought feature extraction only through expert knowledge will not be able to fully obtain all the drought information in large data volumes. The deep learning technologies such as CNN and RNN with homogeneous inductive bias are suitable for extracting drought features from homogeneous data such as remote sensing images and meteorological time series. The heterogeneous drought features extracted by deep learning and expert knowledge are fed into the specialized deep learning network for joint training. This will further improve the accuracy, spatial mapping and intelligence of integrated drought monitoring. 

#### **5. Conclusions** 

In this study, four representative deep learning methods (i.e., EEDNN, 1D-CNN, GRU, and SAM) and three widely used tree-based machine learning methods (i.e., Cubist, RF, and LGBM) were critically evaluated in constructing the integrated agricultural drought index QuickDRI-China. The main insights and conclusions of this paper are as follows: 

- (1) In terms of station accuracy evaluation, not all deep learning methods presented better performances than the tree-based 

machine learning methods. Their overall accuracy evaluation metrics (R<sup>2</sup> /RMSE) from high to low are: EEDNN (0.914/0.299) _>_ RF (0.912/0.302) _>_ LGBM (0.908/0.308) _>_ 1D-CNN (0.907/ 0.310) _>_ SAM (0.905/0.313) ≈ GRU (0.904/0.314) _>_ Cubist (0.902/0.318). The reason may lie in the adaptability to heterogeneous input features. Since the features that employed in constructing the integrated agricultural drought index are heterogeneous, the method who has the adaptability to heterogeneous features tend to perform better. The EEDNN effectively deals with heterogeneous drought features thanks to the weak homogeneous inductive bias of DNN, advanced embedding coding technology and appropriate regularization means. The RF and LGBM have their natural advantage in dealing with heterogeneous data, and the 1D-CNN, GRU, and SAM have homogeneous inductive bias. Resultantly, the EEDNN performed best, followed by the RF and LGBM, and then the other methods. 

- (2) In terms of spatial description evaluation, both the EEDNN method (representative of deep learning) and the RF method (representative of machine learning) can accurately describe the macroscopic spatial pattern of drought. However, the EEDNNderived QuickDRI-China has richer spatial details than the RFderived QuickDRI-China at the micro scale. Moreover, the former has a smoother spatial description than the latter, which implies that the EEDNN-derived result is more in line with the actual spatial continuity of agricultural drought, while the RFderived result is prone to obvious boundaries in the spatial description. This smoother spatial description benefits from the fact that neural networks are biased toward low-frequency functions, while tree-based methods favor irregular (nonsmooth) patterns. 

- (3) In terms of responses to drought events, both the EEDNN-derived QuickDRI-China and the RF-derived QuickDRI-China can effectively reflect the macroscopic and large-scale drought events. But 

14 

_Agricultural Water Management 286 (2023) 108405_ 

_Z. Xu et al._ 

the EEDNN performed better at local scale, and it can capture some extreme drought events that the RF cannot detect. 

To sum up, the tree-based ensemble machine learning methods such as RF and LGBM are still competitive in constructing the integrated drought index as compared with the deep learning methods at the current stage. However, the higher accuracy, the smoother spatial description, and the more responsive ability of the EEDNN demonstrate great potential of deep learning methods for integrated agricultural drought monitoring. We believe that developing a specialized deep learning network for heterogeneous agricultural drought features can further improve the performances of integrated agricultural drought monitoring. This should be one of the focuses in the next study of remote sensing of agricultural drought. 

#### **Acknowledgments** 

This work was supported by Beijing Natural Science Foundation (grant numbers 6222045). 

#### **Declaration of Competing Interest** 

The authors declare that they have no knowncompeting financial interests or personal relationships that could haveappeared to influence the work reported in this paper. 

#### **Data availability** 

Data will be made available on request. 

#### **References** 

- [dataset]McNally, A., 2018. FLDAS Noah land surface model L4 Global Monthly 0.1×0.1<sup>◦</sup> (MERRA-2 and CHIRPS). GES DISC, v001. https://doi.org/10.5067/ 5NHC22T9375G. (accessed 6 October 2022). 

- AghaKouchak, A., Farahmand, A., Melton, F.S., Teixeira, J., Anderson, M.C., Wardlow, B. D., Hain, C.R., 2015. Remote sensing of drought: Progress, challenges and opportunities. Rev. Geophys. 53, 452–480. https://doi.org/10.1002/ 2014RG000456. 

- Alzubaidi, L., Zhang, J., Humaidi, A.J., Al-Dujaili, A., Duan, Y., Al-Shamma, O., Santamaría, J., Fadhel, M.A., Al-Amidie, M., Farhan, L., 2021. Review of deep learning: concepts, CNN architectures, challenges, applications, future directions. J. Big Data 8, 53. https://doi.org/10.1186/s40537-021-00444-8. 

- Anderson, M.C., Norman, J.M., Mecikalski, J.R., Otkin, J.A., Kustas, W.P., 2007. A climatological study of evapotranspiration and moisture stress across the continental United States based on thermal remote sensing: 1. Model formulation. J. Geohys. Res. D. 112, D10117 https://doi.org/10.1029/2006JD007506. 

- Anderson, M.C., Hain, C., Wardlow, B., Pimstein, A., Mecikalski, J.R., Kustas, W.P., 2011. Evaluation of drought indices based on thermal remote sensing of evapotranspiration over the continental United States. J. Clim. 24, 2025–2044. https://doi.org/10.1175/2010JCLI3812.1. 

- Asadi Zarch, M.A., Sivakumar, B., Sharma, A., 2015. Droughts in a warming climate: a global assessment of Standardized precipitation index (SPI) and reconnaissance drought index (RDI). J. Hydrol. 526, 183–195. https://doi.org/10.1016/j. jhydrol.2014.09.071. 

- Beck, H.E., van Dijk, A.I.J.M., Levizzani, V., Schellekens, J., Miralles, D.G., Martens, B., de Roo, A., 2017. MSWEP: 3-hourly 0.25<sup>◦</sup> global gridded precipitation (1979–2015) by merging gauge, satellite, and reanalysis data. Hydrol. Earth. Syst. Sci. 21, 589–615. https://doi.org/10.5194/hess-21-589-2017. 

- China Meteorological Administration, 2015. Yearbook of Meteorological Disasters in 

China (2014). China. Meteorological Press,, Beijing. 

, 2022[dataset] Beguería, S., Vicente Serrano, S.M., Reig-Gracia, F.,Latorre Garc´es, B., 2022. SPEIbase. DIGITAL.CSIC, v2.7.https://doi.org/10.20350/digitalCSIC/14612. (accessed 16 January 2023). 

- Alizadeh, M.R., Nikoo, M.R., 2018. A fusion-based methodology for meteorological drought estimation using remote sensing data. Remote Sens. Environ. 211, 229–247. https://doi.org/10.1016/j.rse.2018.04.001. 

- Bergstra, J., Bardenet, R., Bengio, Y., K´egl, B., 2011. Algorithms for hyper-parameter optimization, In: Proceedings of the 24th International Conference on Neural Information Processing Systems, NIPS 2011. Curran Associates Inc., pp. 2546–2554. https://dl.acm.org/doi/10.5555/2986459.2986743. 

- Bergstra, J., Yamins, D., Cox, D.D., 2013. Making a science of model search: hyperparameter optimization in hundreds of dimensions for vision architectures, In: Proceedings of the 30th International Conference on International Conference on Machine Learning - Volume 28, ICML 2013. PMLR, pp. 115–123. https://dl.acm.org/ doi/10.5555/3042817.3042832. 

- Borisov, V., Leemann, T., Seßler, K., Haug, J., Pawelczyk, M., Kasneci, G., 2022. Deep neural networks and tabular data: a survey. IEEE Trans. Neural Netw. Learn. Syst. 1–21. https://doi.org/10.1109/TNNLS.2022.3229161. 

- Breiman, L., 2001. Random forests. Mach. Learn. 45, 5–32. https://doi.org/10.1023/A: 1010933404324. 

- Brown, J.F., Wardlow, B.D., Tadesse, T., Hayes, M.J., Reed, B.C., 2008. The vegetation drought response index (VegDRI): a new integrated approach for monitoring drought stress in vegetation. GISci. Remote Sens. 45, 16–46. https://doi.org/10.2747/15481603.45.1.16. 

- Chen, T., Guestrin, C., 2016. XGBoost: a scalable tree boosting system. In: Proceedings of the 22nd Acm Sigkdd International Conference on Knowledge Discovery and Data Mining, Kdd 2016. Assoc Computing Machinery, pp. 785–794. https://doi.org/ 10.1145/2939672.2939785. 

- Cheng, H.-T., Koc, L., Harmsen, J., Shaked, T., Chandra, T., Aradhye, H., Anderson, G., Corrado, G., Chai, W., Ispir, M., Anil, R., Haque, Z., Hong, L., Jain, V., Liu, X., Shah, H., 2016. Wide & deep learning for recommender systems, In: Proceedings of the 1st Workshop on Deep Learning for Recommender Systems, DLRS 2016. Association for Computing Machinery, pp. 7–10. https://doi.org/10.1145/2988450.2988454. 

- Cho, K., van Merri¨enboer, B., Gulcehre, C., Bahdanau, D., Bougares, F., Schwenk, H., Bengio, Y., 2014. Learning phrase representations using RNN encoder–decoder for statistical machine translation, In: Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing, EMNLP 2014. Association for Computational Linguistics, pp. 1724–1734. https://doi.org/10.3115/v1/D14–1179. 

- Chung, J., Gulcehre, C., Cho, K., Bengio, Y., 2014. Empirical evaluation of gated recurrent neural networks on sequence modeling. arXiv 1412, 3555. https://doi.org/ 10.48550/arXiv.1412.3555. 

- Dai, A., 2011. Drought under global warming: a review. WIREs Clim. Change 2, 45–65. https://doi.org/10.1002/wcc.81. 

- Dai, A., 2013. Increasing drought under global warming in observations and models. Nat. Clim. Change 3, 52–58. https://doi.org/10.1038/NCLIMATE1633. 

- Dinerstein, E., Olson, D., Joshi, A., Vynne, C., Burgess, N.D., Wikramanayake, E., Hahn, N., Palminteri, S., Hedao, P., Noss, R., Hansen, M., Locke, H., Ellis, E.C., Jones, B., Barber, C.V., Hayes, R., Kormos, C., Martin, V., Crist, E., Sechrest, W., Price, L., Baillie, J.E.M., Weeden, D., Suckling, K., Davis, C., Sizer, N., Moore, R., Thau, D., Birch, T., Potapov, P., Turubanova, S., Tyukavina, A., de Souza, N., Pintea, L., Brito, J.C., Llewellyn, O.A., Miller, A.G., Patzelt, A., Ghazanfar, S.A., Timberlake, J., Kloser, H., Shennan-Farp¨ on, Y., Kindt, R., Lilles´ ø, J.-P.B., van Breugel, P., Graudal, L., Voge, M., Al-Shammari, K.F., Saleem, M., 2017. An ecoregion-based approach to protecting half the terrestrial realm. BioScience 67, 534–545. https://doi.org/10.1093/biosci/bix014. 

- Feng, P., Wang, B., Liu, D.L., Yu, Q., 2019. Machine learning-based integration of remotely-sensed drought factors can improve the estimation of agricultural drought in South-Eastern Australia. Agric. Syst. 173, 303–316. https://doi.org/10.1016/j. agsy.2019.03.015. 

- Friedman, J.H., 2001. Greedy function approximation: a gradient boosting machine. Ann. Stat. 29, 1189–1232. https://doi.org/10.1214/aos/1013203451. 

- Gao, L., Tao, B., Miao, Y., Zhang, L., Song, X., Ren, W., He, L., Xu, X., 2019. A global data set for economic losses of extreme hydrological events during 1960-2014. Water Resour. Res. 55, 5165–5175 https://doi.org/10.1029./2019WR025135. 

- Gao, Y., Markkanen, T., Thum, T., Aurela, M., Lohila, A., Mammarella, I., K¨am¨ar¨ainen, M., Hagemann, S., Aalto, T., 2016. Assessing various drought indicators in representing summer drought in boreal forests in Finland. Hydrol. Earth Syst. Sci. 20, 175–191. https://doi.org/10.5194/hess-20-175-2016. 

- Goodfellow, I., Bengio, Y., Courville, A., 2016. Deep Learning. The MIT Press,, 

   - Cambridge, Massachusetts. 

- Grinsztajn, L., Oyallon, E., Varoquaux, G., 2022. Why do tree-based models still outperform deep learning on typical tabular data?, In: Proceedings of the 35th International Conference on Neural Information Processing Systems, NIPS 2022. Curran Associates, Inc., pp.507–520. https://hal.science/hal-03723551v2. 

- Guo, C., Berkhahn, F., 2016. Entity embeddings of categorical variables. arXiv 1604, 06737. https://doi.org/10.48550/arXiv.1604.06737. 

- Hain, C.R., Anderson, M.C., 2017. Estimating morning change in land surface temperature from MODIS day/night observations: applications for surface energy balance modeling. Geophys. Res. Lett. 44, 9723–9733. https://doi.org/10.1002/ 2017GL074952. 

- Hao, C., Zhang, J., Yao, F., 2015. Combination of multi-sensor remote sensing data for drought monitoring over Southwest China. Int. J. Appl. Earth Obs. Geoinf. 35, 270–283. https://doi.org/10.1016/j.jag.2014.09.011. 

- Hao, Z., Singh, V.P., 2015. Drought characterization from a multivariate perspective: a review. J. Hydrol. 527, 668–678. https://doi.org/10.1016/j.jhydrol.2015.05.031. 

- Hengl, T., Jesus, J.M., de, Heuvelink, G.B.M., Gonzalez, M.R., Kilibarda, M., Blagoti´c, A., Shangguan, W., Wright, M.N., Geng, X., Bauer-Marschallinger, B., Guevara, M.A., Vargas, R., MacMillan, R.A., Batjes, N.H., Leenaars, J.G.B., Ribeiro, E., Wheeler, I., Mantel, S., Kempen, B., 2017. SoilGrids250m: global gridded soil information based on machine learning. PLOS One 12, e0169748. https://doi.org/10.1371/journal. pone.0169748. 

- Ho, T.K., 1995. Random decision forests, In: Proceedings of 3rd International Conference on Document Analysis and Recognition - Volume 1. IEEE, pp. 278–282. https://doi. org/10.1109/ICDAR.1995.598994. 

- Huete, A., Didan, K., Miura, T., Rodriguez, E.P., Gao, X., Ferreira, L.G., 2002. Overview of the radiometric and biophysical performance of the MODIS vegetation indices. Remote Sens. Environ. 83, 195–213. https://doi.org/10.1016/S0034-4257(02) 

   - 00096-2. 

- Jiao, W., Tian, C., Chang, Q., Novick, K.A., Wang, L., 2019. A new multi-sensor integrated index for drought monitoring. Agric. For. Meteorol. 268, 74–85. https:// doi.org/10.1016/j.agrformet.2019.01.008. 

15 

_Agricultural Water Management 286 (2023) 108405_ 

_Z. Xu et al._ 

- Jiao, W., Wang, L., McCabe, M.F., 2021. Multi-sensor remote sensing for drought characterization: current status, opportunities and a roadmap for the future. Remote Sens. Environ. 256, 112313 https://doi.org/10.1016/j.rse.2021.112313. 

- Kadra, A., Lindauer, M., Hutter, F., Grabocka, J., 2021. Well-tuned simple nets excel on tabular datasets, In: Proceedings of the 34th International Conference on Neural Information Processing Systems, NIPS 2021. Curran Associates, Inc., pp. 23928–23941. https://doi.org/10.48550/arXiv.2106.11189. 

- Katzir, L., Elidan, G., El-Yaniv, R., 2021. Net-DNF: Effective Deep Modeling of Tabular Data. In: Proceedings of the International Conference on Learning Representations, ICLR 2021. OpenReview. https://openreview.net/forum?id=73WTGs96kho. 

- Ke, G., Meng, Q., Finley, T., Wang, T., Chen, W., Ma, W., Ye, Q., Liu, T.-Y., 2017. LightGBM: A highly efficient gradient boosting decision tree, In: Proceedings of the 31st International Conference on Neural Information Processing Systems, NIPS 2017. Curran Associates, Inc., pp. 3149–3157. https://dl.acm.org/doi/10.5555/ 3294996.3295074. 

- Kim, Y., 2014. Convolutional neural networks for sentence classification, In: Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing, EMNLP 2014. Association for Computational Linguistics, pp. 1746–1751. https:// doi.org/10.3115/v1/D14–1181. 

- Kogan, F.N., 1995. Application of vegetation index and brightness temperature for drought detection. Adv. Space Res. 15, 91–100. https://doi.org/10.1016/0273-1177 (95)00079-T. 

- Kogan, Felix N., 1995. Droughts of the Late 1980s in the United States as derived from NOAA polar-orbiting satellite data. Bull. Am. Meteorol. Soc. 76, 655–668. https:// doi.org/10.1175/1520-0477(1995)076 _<_ 0655:DOTLIT _>_ 2.0.CO;2. 

- Krizhevsky, A., Sutskever, I., Hinton, G.E., 2012. ImageNet classification with deep convolutional neural networks, In: Proceedings of the 25th International Conference on Neural Information Processing Systems, NIPS 2012. Curran Associates, Inc., pp.84–90. https://doi.org/10.1145/3065386. 

- LeCun, Y., Bengio, Y., Hinton, G., 2015. Deep learning. Nature 521, 436–444. https:// doi.org/10.1038/nature14539. 

- Liu, X., Zhu, X., Zhang, Q., Yang, T., Pan, Y., Sun, P., 2020. A remote sensing and artificial neural network-based integrated agricultural drought index: index development and applications. Catena 186, 104394. https://doi.org/10.1016/j. catena.2019.104394. 

- Masters, D., Luschi, C., 2018. Revisiting small batch training for deep neural networks. arXiv 1804, 07612. https://doi.org/10.48550/arXiv.1804.07612. 

- McKee, T.B., Doesken, N.J., Kleist, J., 1993. The relationship of drought frequency and duration to time scales, In: Proceedings of the 8th Conference on Applied Climatology. Boston, MA, USA, pp. 179–183. 

- McNally, A., Arsenault, K., Kumar, S., Shukla, S., Peterson, P., Wang, S., Funk, C., PetersLidard, C.D., Verdin, J.P., 2017. Data descriptor: a land data assimilation system for sub-Saharan Africa food and water security applications. Sci. Data 4, 170012. https://doi.org/10.1038/sdata.2017.12. 

- Naumann, G., Cammalleri, C., Mentaschi, L., Feyen, L., 2021. Increased economic drought impacts in Europe with anthropogenic warming. Nat. Clim. Change 11, 485–491. https://doi.org/10.1038/s41558-021-01044-3. 

- Niu, Z., Zhong, G., Yu, H., 2021. A review on the attention mechanism of deep learning. Neurocomputing 452, 48–62. https://doi.org/10.1016/j.neucom.2021.03.091. 

- Orlowsky, B., Seneviratne, S.I., 2013. Elusive drought: uncertainty in observed trends and short- and long-term CMIP5 projections. Hydrol. Earth Syst. Sci. 17, 1765–1781. https://doi.org/10.5194/hess-17-1765-2013. 

- Palmer, W.C., 1965. Meteorological Drought. U.S. Department of Commerce, Weather Bureau, Washington, D.C. 

- Park, S., Im, J., Jang, E., Rhee, J., 2016. Drought assessment and monitoring through blending of multi-sensor indices using machine learning approaches for different climate regions. Agric. For. Meteorol. 216, 157–169. https://doi.org/10.1016/j. agrformet.2015.10.011. 

- Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., Perrot, M., Duchesnay, E., 2011. Scikit-learn: machine learning in Python. J. Mach. Learn. Res. 12, 2825–2830 https://dl.acm.org/doi/ 10.5555/1953048.2078195. 

- Peters, A.J., Walter-Shea, E.A., Ji, L., Vina, A., Hayes, M., Svoboda, M.D., 2002. Drought monitoring with NDVI-based standardized vegetation index. Photogramm. Eng. Remote Sens. 68, 71–75. 

- Prodhan, F.A., Zhang, J., Yao, F., Shi, L., Pangali Sharma, T.P., Zhang, D., Cao, D., Zheng, M., Ahmed, N., Mohana, H.P., 2021. Deep learning for monitoring agricultural drought in South Asia using remote sensing data. Remote Sens. 13, 1715. https://doi.org/10.3390/rs13091715. 

- Qu, Y., Fang, B., Zhang, W., Tang, R., Niu, M., Guo, H., Yu, Y., He, X., 2019. Productbased neural networks for user response prediction over multi-field categorical data. ACM Trans. Inf. Syst. 37, 5. https://doi.org/10.1145/3233770. 

- Quinlan, J.R., 1992. Learning with continuous classes, In: Proceedings of the 5th Australian Joint Conference On Articial Intelligence. World Scientific, pp. 343–348. https://doi.org/10.1142/9789814536271. 

- Quinlan, J.R., 1993. Combining instance-based and model-based learning, In: Proceedings of the Tenth International Conference on Machine Learning, ICML1993. Morgan Kaufmann Publishers Inc., pp. 236–243. https://dl.acm.org/doi/10.5555/ 3091529.3091560. 

- Rahaman, N., Baratin, A., Arpit, D., Draxler, F., Lin, M., Hamprecht, F., Bengio, Y., Courville, A., 2019. On the spectral bias of neural networks, In: Proceedings of the 36th International Conference on Machine Learning, ICML 2019. PMLR, pp. 5301–5310. https://doi.org/10.48550/arXiv.1806.08734. 

- Reuter, H.I., Nelson, A., Jarvis, A., 2007. An evaluation of void-filling interpolation methods for SRTM data. Int. J. Geogr. Inf. Sci. 21, 983–1008. https://doi.org/ 10.1080/13658810601169899. 

- Rhee, J., Im, J., 2017. Meteorological drought forecasting for ungauged areas based on machine learning: using long-range climate forecast and remote sensing data. Agric. For. Meteorol. 237–238, 105–122. https://doi.org/10.1016/j. agrformet.2017.02.011. 

- Roodposhti, M.S., Safarrad, T., Shahabi, H., 2017. Drought sensitivity mapping using two one-class support vector machine algorithms. Atmos. Res. 193, 73–82. https://doi. org/10.1016/j.atmosres.2017.04.017. 

- Shen, R., Huang, A., Li, B., Guo, J., 2019. Construction of a drought monitoring model using deep learning based on multi-source remote sensing data. Int. J. Appl. Earth Obs. Geoinf. 79, 48–57. https://doi.org/10.1016/j.jag.2019.03.006. 

- Sun, H., Zhao, X., Chen, Y., Gong, A., Yang, J., 2013. A new agricultural drought monitoring index combining MODIS NDWI and day–night land surface temperatures: a case study in China. Int. J. Remote Sens 34, 8986–9001. https://doi. org/10.1080/01431161.2013.860659. 

- Sun, H., Liu, W., Wang, Y., Yuan, S., 2017. Evaluation of typical spectral vegetation indices for drought monitoring in cropland of the North China Plain. IEEE J. Sel. Top. Appl. Earth Obs. Remote Sens. 10, 5404–5411. https://doi.org/10.1109/ JSTARS.2017.2734800. 

- Tadesse, T., Champagne, C., Wardlow, B.D., Hadwen, T.A., Brown, J.F., Demisse, G.B., Bayissa, Y.A., Davidson, A.M., 2017. Building the vegetation drought response index for Canada (VegDRI-Canada) to monitor agricultural drought: first results. GISci. Remote Sens. 54, 230–257. https://doi.org/10.1080/15481603.2017.1286728. 

- Tobler, W.R., 1970. A computer movie simulating urban growth in the Detroit region. Econ. Geogr. 46, 234–240. https://doi.org/10.2307/143141. 

- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, Ł., Polosukhin, I., 2017. Attention is all you need, In: Proceedings of the 31st International Conference on Neural Information Processing Systems, NIPS 2017. Curran Associates, Inc., pp.6000–6010. https://dl.acm.org/doi/10.5555/ 3295222.3295349. 

- Vicente-Serrano, S.M., Begueria, S., Lopez-Moreno, J.I., 2010. A multiscalar drought index sensitive to global warming: the standardized precipitation evapotranspiration index. J. Clim. 23, 1696–1718. https://doi.org/10.1175/2009JCLI2909.1. 

- Vicente-Serrano, S.M., Quiring, S.M., Pena-Gallardo, M., Yuan, S., Domínguez-Castro, F., ˜ 2020. A review of environmental droughts: increased risk under global warming? Earth Sci. Rev. 201, 102953 https://doi.org/10.1016/j.earscirev.2019.102953. 

- West, H., Quinn, N., Horswell, M., 2019. Remote sensing for drought monitoring & impact assessment: progress, past challenges and future opportunities. Remote Sens. Environ. 232, 111291 https://doi.org/10.1016/j.rse.2019.111291. 

- Wilhite, D.A., Glantz, M.H., 1985. Understanding: the drought phenomenon: the role of definitions. Water Int. 10, 111–120. https://doi.org/10.1080/02508068508686328. 

- Yuan, Q., Shen, H., Li, T., Li, Z., Li, S., Jiang, Y., Xu, H., Tan, W., Yang, Q., Wang, J., Gao, J., Zhang, L., 2020. Deep learning in environmental remote sensing: achievements and challenges. Remote Sens. Environ. 241, 111716 https://doi.org/ 10.1016/j.rse.2020.111716. 

- Yuan, W., Cai, W., Chen, Y., Liu, Shuguang, Dong, W., Zhang, H., Yu, G., Chen, Z., He, H., Guo, W., Liu, D., Liu, Shaoming, Xiang, W., Xie, Z., Zhao, Z., Zhou, G., 2016. Severe summer heatwave and drought strongly reduced carbon uptake in Southern China. Sci. Rep. 6, 1–12. https://doi.org/10.1038/srep18813. 

- Zhang, A., Jia, G., 2013. Monitoring meteorological drought in semiarid regions using multi-sensor microwave remote sensing data. Remote Sens. Environ. 134, 12–23. https://doi.org/10.1016/j.rse.2013.02.023. 

- Zhang, A., Jia, G., Wang, H., 2019. Improving meteorological drought monitoring capability over tropical and subtropical water-limited ecosystems: evaluation and ensemble of the microwave integrated drought index. Environ. Res. Lett. 14, 044025 https://doi.org/10.1088/1748-9326/ab005e. 

16 

