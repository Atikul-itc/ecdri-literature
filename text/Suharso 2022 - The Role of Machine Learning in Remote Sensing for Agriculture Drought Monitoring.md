_(IJACSA) International Journal of Advanced Computer Science and Applications, Vol. 13, No. 12, 2022_ 

# The Role of Machine Learning in Remote Sensing for Agriculture Drought Monitoring: A Systematic Review 

Aries Suharso<sup>1</sup> , Yeni Hediyeni<sup>2</sup> , Suria Darma Tarigan<sup>3</sup> , Yandra arkeman<sup>4</sup> Department of Computer Science, IPB University, Bogor, Indonesia<sup>1, 2</sup> Informatics of Computer Science, University of Singaperbangsa Karawang<sup>1</sup> Department of Soil and Land Resource, IPB University, Bogor, Indonesia<sup>3</sup> Department of Agro-Industrial Technology, IPB University, Bogor, Indonesia<sup>4</sup> 

**_Abstract_ —Agricultural drought is still difficult to anticipate even though there have been developments in remote sensing technology, especially satellite imagery that is useful for farmers in monitoring crop conditions. The availability of open and free satellite imagery still has a weakness, namely the level of resolution is low and coarse with atmospheric disturbances in the form of cloud cover, as well as the location and period for taking images that are different from the presence of weather stations on Earth. This problem is a challenge for researchers trying to monitoring agricultural drought conditions through satellite imagery. One approach that has recently used is high computational techniques through machine learning, which is able to predict satellite image data according to the conditions of mapping land types and plants in the field. Furthermore, using time series data from satellite imagery, a predictive model of crop cycles can be regarding future crop drought conditions. So, through this technology, we can encourage farmers to make decisions to anticipate the dangers of agricultural drought. Unfortunately, exploration of the use of machine learning for classification and prediction of agricultural drought conditions has not conducted, and the existing methods can still improve. This review aims to present a comprehensive overview of methods that used to monitor agricultural drought using remote sensing and machine learning, which are the subjects of future research.** 

|**_Abstrac_**|**_t_—Agricultural drought is still difficult to anticipate**|DT|Decision Tree|
|---|---|---|---|
|**even thoug**|**h there have been developments in remote sensing**|ERT|Extreme Regression Tree|
|**technology**<br>**in monitor**<br>**satellite im**<br>**resolution**|**, especially satellite imagery that is useful for farmers**<br>**ing crop conditions. The availability of open and free**<br>**agery still has a weakness, namely the level of**<br>**is low and coarse with atmospheric disturbances in the**|ESA-CCI<br>ESTARFM<br>EVI|European Space Agency - Climate Change Initiative<br>Enhanced Spatial and Temporal Adaptive Reflectance Fusion<br>Model<br>Enhanced Vegetation Index|
|**form of clo**<br>**images tha**|**ud cover, as well as the location and period for taking**<br>**t are different from the presence of weather stations**|GA<br>GAM|Genetic Algorithm<br>General Additive Model|
|**on Earth.**|**This problem is a challenge for researchers trying to**|GDEM|Global Digital Elevation Model|
|**monitoring**<br>**imagery.**<br>**computatio**<br>**able to pre**<br>**mapping l**|**agricultural drought conditions through satellite**<br>**One approach that has recently used is high**<br>**nal techniques through machine learning, which is**<br>**dict satellite image data according to the conditions of**<br>**and types and plants in the field. Furthermore, using**|GLDAS-2<br>GMDH<br>GPCP<br>GPM<br>|<br>Global Land Data Assimilation System Version-2<br>Group Method of Data Handling<br>Global Precipitation Climatology Project<br>Global Precipitation Measurement<br>|
|**time series**<br>**cycles can**|**data from satellite imagery, a predictive model of crop**<br>**be regarding future crop drought conditions. So,**|GRACE<br>HSMDI|Gravity Recovery and Climate Experiment<br>High Soil Moisture Drought Index|
|**through th**|**is technology, we can encourage farmers to make**|IMERG|Integrated Multi-satellitE Retrievals for GPM|
|**decisions**|**to anticipate the dangers of agricultural drought.**|ISMN|International Soil Moisture Network|
|**Unfortunat**<br>|**ely, exploration of the use of machine learning for**<br>|KKN|K-nearest neighbors algorithm|
|**classificati**|**on and prediction of agricultural drought conditions**|Landsat|Landsat + Enhanced Thematic Maer|
|**has not co**|**nducted, and the existing methods can still improve.**|ETM|pp|
|**This revie**<br>**methods th**<br>**sensing an**<br>**research.**|**w aims to present a comprehensive overview of**<br>**at used to monitor agricultural drought using remote**<br>**d machine learning, which are the subjects of future**|LST<br>M5P<br>MERRA-2<br>MIDI|Land Surface Temperature<br>is a reconstruction of Quinlan's M5 algorithm for inducing trees of<br>regression models.<br>Modern-Era Retrospective analysis for Research and Applications<br>Microwave Integrated Drought Index|
|**_Keywor_**|**_ds—Drought monitoring; exploration of the use of_**|MLP|Multi-Layer Preceptron|
|**_machine le_**|**_arning; Landsat imagery; remote sensing_**|MODIS<br>MCD43C4|Moderate Resolution Imaging Spectroradiometer<br>MODIS Product|
||GLOSSARY|MOD11C1|MODIS Product|
|**Term**|**Description**|MOD13A3<br>|MODIS Product<br>|
|AMSR-E|Advanced Microwave Scanning Radiometer 2|MYD11C3|MODIS Product|
|ANFIS|Adaptive Neuro-Fuzzy Inference System|MYD13C2|MODIS Product<br>MODIS Product rovides lobal land cover tes at earl|
|ANN<br>ASTER|Artificial Neural Network<br>Advanced<br>Spaceborne<br>Thermal<br>Emission<br>and<br>Reflection<br>Radiometer|MCD12Q1|p g   yp  yy<br>intervals (2001-2016) derived from six different classification<br>schemes<br>|
|AVHRR|<br>Advanced Very High Resolution Radiometer|MCD43A4|MODIS Product contains 16 days of data provided in a level-3<br>gridded data set in Sinusoidal projection|
||||MODIS Product provides an estimate of the surface spectral|
|AWS|Autonomous Weather Stations||<br>|
|BRT|Boosted Regression Trees|MOD09A1|reflectance of Terra MODIS bands 1-7 at 500m resolution and<br>corrected for atmospheric conditions such as gasses, aerosols, and|
|CDR|Climate Data Record||<br>Rayleigh scattering|
|CHOMPS|CICS<br>High-Resolution<br>Optimal<br>Interpolation<br>Microwave<br>Precipitation from Satellite|MOD11A2|<br>MODIS Product provides an average 8-day land surface<br>temperature (LST) in a 1200 x 1200 kilometer grid|
|CMAP|CPC Merge Analysis of Precipitation||MODIS Product provide Evapotranspiration/Latent Heat Flux<br>|
|DEM|Digital Elevation Model|MOD16A2|product is an 8-day composite product produced at 500 meter pixel<br>resolution|
|DFNN|Deep Forward Neural Network|NDVI|Normalized Difference Vegetation Index|



764 | P a g e 

www.ijacsa.thesai.org 

_(IJACSA) International Journal of Advanced Computer Science and Applications, Vol. 13, No. 12, 2022_ 

|NOAA|National Oceanic and Atmospheric Administration|
|---|---|
|ORLIKE-<br>OWA|ORLIKE-Ordered Weighted Averaged (OWA)|
|ORNESS-<br>OWA|ORNESS-Ordered Weighted Averaged (OWA)|
|PCI|Precipitation Condition Index|
|PERSIANN|Precipitation Estimation From Remotely Sensed Information using<br>Artificial Neural Networks|
|RCI|Rainfall Condition Index|
|RF|Random Forest|
|RFE|Recursive Feature Elimination|
|SMAP|Soil Moisture Active Passive|
|SMDI|Soil Moisture Deficit Index|
|SPEI|Standardized Precipitation Evaporation Index|
|SPI|Standardized Precipitation Index|
|SRTM|Shuttle Radar Topography Mission|
|SVM|Support Vektor Machine|
|SVR|Support Vektor Regression|
|SWDI|Soil Water Deficit Index|
|TAMSAT|Tropical Applications of Meteorology using Satellite data|
|TCI|Temperature Condition Index|
|TRMM<br>(3B43)|Tropical Rainfall Measuring Mission|
|UAV|Unmanned Aerial Vehicle|
|VCI|Vegetation Condition Index|
|VSDI|Shortwave Infrared Drought Index|
|VSWI|Vegetation Supply Water Index|
|VTCI|Vegetation Temperature Condition Index|



## I. INTRODUCTION 

One of the problems of rainfed agriculture productivity is prolonged drought, lack of rainfall, and lack of water supply in the soil during the vegetative growth phase [1], [2], [3], [4]. In addition, high temperatures during the ripening phase can reduce the conversion yield of sucrose to fructose and glucose [5]. Climate change can also cause diseases and pests [6]. Therefore, it is essential to monitor drought conditions to schedule appropriate irrigation based on the response of plants to drought at various stages of vegetation [7], [8]. 

However, measuring plant response to drought is very difficult and complex [9], [10], [11], [12], [13], [14]. Detecting and integrating crop water deficits is still complex based on single plant responses [15]. Until 2017 [16]  grouped four methods to monitor plant response to drought, namely, (1) Groundwater measurement; (2) Groundwater balanced approach; (3) Plant-based approach; (4) Remote sensing methods. The approach (4) remote sensing is based on the spectral index of vegetation obtained from the Unmanned Aircraft Systems (UAS) hyperspectral sensor, which is the best considering the cost of the sensor is not expensive; the determination of leaf moisture status indicators and plant stomata conductance is high. Non-destructive and non-labor intensive is suitable for automation. The remote sensing method can be adopted as an irrigation scheduling decision [17]. 

The fact there is an abundance of free Landsat satellite data with open access globally by the US Geological Survey (USGS) starting in 2008 [18] on the Earth Resources Observation and Science (EROS) Center website  has attracted researchers from various countries to apply it as a producer of 

land use land cover (LULC) maps in their respective regions [19], [20]. However, constructing medium and high-resolution land cover maps in cloud-prone areas is still challenging due to infrequent satellite visits and the lack of cloud-free data. It is both an opportunity and a challenge for researchers to accurately map plant droughtes with hyperspectral indices through machine learning classification methods for persistent cloud areas with high temporal dynamics of land cover types that require further investigation. Overall, there have been numerous former studies showing that the use of remote sensing to monitor drought has increased significantly in recent times. Still, the application of machine learning to remote sensing for drought monitoring has not been welldiversified, so there are still numerous exploration gaps that show that its application has not been thoroughly assessed or utilized for drought monitoring purposes. 

As a result, in this article we attempt to conduct a systematic review utilizing the meta-analysis method of prior studies using machine learning techniques in remote sensing for agricultural drought monitoring. Meta-analysis methods and systematic reviews can aid in the creation of evaluations that are clearer and more succinct [21]. If there are more studies on similar subjects, the advantages of systematic reviews can be further extended [22]. Systematic reviews can help scientists uncover factors faster, lessen data bias, more accurately define variables, spot trends that previous researchers might have missed, and choose the direction of future study topics [23]. Additionally, systematic reviews can assist researchers in comparing, debating, and choosing from the larger body of literature in order to obtain more trustworthy results [24]. 

## II. RELATED WORK 

The use of machine learning techniques to categorize satellite imaging data in remote sensing applications has gained popularity in recent years. On this subject, several research studies have been released, some of which are listed in the paragraphs below. 

- Various formalisms are used in applications of machine learning and signal/image processing, including classification and clustering, regression and function approximation, image coding, recovery and enhancement, source separation, data aggregation, and feature selection and extraction [25]. 

- Machine learning techniques have recently been used in various ways to process data from multispectral and hyperspectral remote sensing [26]. 

- Using the input data from the satellites Spot5, Sentinel1, and Sentinel2, a Symbolic Machine Learning (SML) classifier with spatial generalization treatment, random theme noise, and spatial displacement noise was created. It made use of multiple Maximum Likelihood Supervised Algorithms, Logistic Regression, Linear Discriminant Analysis, Naive Bayes, Decision Trees, Random Forests, and Support Vector Machines [27]. 

765 | P a g e 

www.ijacsa.thesai.org 

_(IJACSA) International Journal of Advanced Computer Science and Applications,_ 

_Vol. 13, No. 12, 2022_ 

- Training data needs, user-defined parameter selection and optimization, impact and attenuation feature space, computing costs, and choice of k-nearest neighbor algorithms, enhanced DT, single decision tree (DT), Random Forest, and somewhat mature support vector machine (k-NN) approaches are all taken into account [28]. 

These studies have shown how well machine learning algorithms work for categorizing remote sensing images and the possibility for further improving the precision and effectiveness of these algorithms through on-going study and development. Previous studies on machine learning in remote sensing have concentrated on a range of methods, such as deep learning algorithms and other supervised and unsupervised approaches, and have investigated their application to various types of remote sensing data and application domains. Overall, applying machine learning to remote sensing has the potential to dramatically increase this field's capabilities and open up a number of new and enhanced applications for satellite data. 

## III. MATERIALS AND METHODS 

The aim of this work is expected to be able to answer the following four research questions ( _RQ_ ): 

- RQ1: What publications are the main targets of machine learning based remote sensing drought monitoring? 

- RQ2: What kind of environment observed for drought monitoring? What types of remote sensing data have been used? 

- RQ3: Which is the most widely used and most accurate machine learning algorithm for the drought monitoring approach? 

- RQ4: How does machine learning play a role in drought monitoring? 

After determining the research question ( _RQ_ ) of interest, selecting a candidate paper, and performing data extraction, the last step of a systematic literature study is to synthesize the results. For each _RQ_ , the inclusion results are classified into categories corresponding to the _RQ_ , and the results are presented in graphs or tables. Furthermore, the results are discussed using various evaluation approaches. Finally, the narrative summary describes the main findings of the systematic literature study. 

In this work, we collect and determine the most relevant literature for this particular study with the PRISMA method [29] search strategy to provide a comprehensive and systematic review of relevant previous studies related to the role of machine learning algorithms in remote sensing for drought monitoring on crop land cover maps. Food, semi-arid plantation is suspected to experience drought. A recent search was conducted on Harzing's Publish or Perish search engine with open data sources Google Schoolar and Crossref based on the title text "Drought monitoring" with keywords "remote sensing" and "machine learning" in the publication period between 2010 and 2021. 

This study eliminates research that does not use remote sensing and machine learning approaches from the collection of articles obtained. Each article is rated based on the use of remote sensing databases, machine learning methods, accuracy of results, and year of publication. There are about 1147 articles on remote sensing drought monitoring published from 2010 to 2021 (Fig. 1). The search for literature was conducted on July 6, 2022, through the search engine Harzing's Publish or Perish on two open-source articles, namely Google scholar and Crossref with the context of the article title "drought monitoring" and the keywords "remote sensing" and "machine learning," with the limitation of the publication period between 2010 and 2021. 

The literature search selection process in Fig. 1 is conducted according to the PRISMA concept, as follows: 

_1) Identification_ : initial search obtained 147 articles from open-source Google Scholar and one thousand articles from open-source Crossref. Our next step is to limit the selected articles based on the number of citations in each article to at least twenty citations. This is done to select articles that have referenced popularity by researchers. The results of this limit of twenty citations selected thirty-four articles from the opensource Google Scholar and 171 articles from the open source Crossref, so that the initial number of identified article data containing the context of the article title "drought monitoring" and the keywords "remote sensing" and "machine learning" was as much as 205 articles. 

_2) Screening_ : 205 articles from the previous stage (Identification) were checked for duplication of articles, and it turned out that there were 11 related articles, so that they were obtained ( _n_ = 194). The process at this stage is conducted on the Microsoft Excel application. Next is the excluded process, namely, discarding a number of articles that do not contain relevant text related to "remote sensing" and "machine learning" in the Abstract section. The results excluded at this stage are _n_ = 166, so the remaining _n_ = 28 articles. 

_3) Eligibility_ : at this stage, the articles are examined in full text with the aim of finding research articles that consistently apply machine learning algorithms and the studies carried out contain quantitative analysis or accuracy values. The results are discarded ( _n_ = 8 papers without the use of machine learning algorithms); ( _n_ = 5 types of paper reviews); ( _n_ = 3 papers without quantitative analysis or accuracy scores), leaving ( _n_ = 12) articles using machine learning algorithms. The process at this stage is conducted on the Zotero and Mendeley application. 

_4) Included_ : from _n_ = 12 selected articles containing the context of "drought monitoring", "remote sensing", and "machine learning", with the type of research article based on observation or experimentation, not a review article. This is done because of a systematic review and meta-analysis, not a narrative review. Furthermore, the selected articles are used as a reference for the main systematic review or meta-analysis. 

766 | P a g e 

www.ijacsa.thesai.org 

_(IJACSA) International Journal of Advanced Computer Science and Applications, Vol. 13, No. 12, 2022_ 



Fig. 1. PRISMA workflow diagram for new systematic review which included search of free database. 

## IV. RESULT AND DISCUSSION 

The inclusion of the PRISMA strategy brief yielded the results of twelve articles that were then analyzed in depth for the content of a meta-analysis that could answer four research questions ( _RQ_ s). 

In response to _RQ_ 1, Fig. 2 demonstrates that out of a total of 194 papers, the publishers who publish the most scientific journals mention remote sensing-based drought monitoring. The breakdown is as follows: MDPI 50% ( _n_ = 97), Elsevier 30% ( _n_ = 57), Taylor & Francis 10% ( _n_ = 20), IEEE 3% ( _n_ = 7), Springer and Wiley both 2% ( _n_ = 4), and the remaining 3% from various publishers ( _n_ = 5). 

Details of the names of the candidate publication journals are listed in Table I. 



<!-- Start of picture text -->
Springer  Wiley  Other<br>2%  2%  3%<br>Taylor & Francis  Elsevier<br>10%<br>29%<br>IEEE<br>4%<br>MDPI<br>50%<br><!-- End of picture text -->

Fig. 2. Publication sources of selected study works. 

TABLE I. PUBLICATION SOURCE SELECTED PAPERS 

|**Journal Name**|**Publisher**|**Total**|
|---|---|---|
|Remote Sensing|MDPI|97|
|Remote Sensing of Environment|Elsevier|42|
|International Journal of Remote Sensing|Taylor & Francis|13|
|GIScience & Remote Sensing|Taylor & Francis|5|
|Journal of Applied Remote Sensing|Other|5|
|Agricultural and forest meteorology|Elsevier|4|
|Water Resources Research|Wiley AGU|4|
|Environmental monitoring and assessment|Springer|4|
|IEEE Geoscience and Remote Sensing Letters|IEEE|3|
|IEEE Journal of Selected Topics in Applied<br>Earth Observations and Remote Sensing|IEEE|3|
|International<br>Journal<br>of<br>Applied<br>Earth<br>Observation and Geoinformation|Elsevier|3|
|ISPRS<br>Journal<br>of<br>Photogrammetry<br>and<br>Remote Sensing|Elsevier|3|
|Computers and Electronics in Agriculture|Elsevier|2|
|Journal of Hydrology|Elsevier|2|
|Remote Sensing Letters|Taylor & Francis|2|
|Science of The Total Environment|Elsevier|2|



The list of journal names in Table I can be used as a reference source. It is remarkably interesting to observe that all these journals are indexed in the Journal Citation Report, mostly in the _Q_ 1 and _Q_ 2 quartiles. 

Fig. 3 presents the trend in the number of articles published per year from 2010 to 2019. This graph shows that there has been a significant increase in the number of publications in the area of Remote Sensing for Drought monitoring. Since 2010, this growth has followed a linear trend. Although the number of selected papers is not too many, it does not rule out the possibility of many publications at the end of 2021. 

In order to respond to the _RQ_ 2 questions, we looked through the chosen articles and then searched for metadata pertaining to each paper's research location and the environmental state of the area covered. Table II lists the location, the surrounding environment, and remote sensing data for observations of regions thought to be experiencing drought conditions. We also complete the dryness index that was utilized in each chosen publication. 



Fig. 3. Publication trends throughout the years 2010 – 2021. 

767 | P a g e 

www.ijacsa.thesai.org 

_(IJACSA) International Journal of Advanced Computer Science and Applications, Vol. 13, No. 12, 2022_ 

TABLE II. ENVIRONMENT AND REMOTE SENSING DATA 

|**Ref.**|**Environment**|**Data**|**Index**|**Validation**|
|---|---|---|---|---|
|[30]|Basin area (Iran)|NOAA-AVHRR, Landsat ETM|VCI, NDVI, AVI|NDVI from Landsat+ETM 18 years<br>(1982 - 1999)|
|[31]|Climate (China)|GRACE|TWSA|TWSC, SWS, SMS, GWS. Fifty-five<br>stations in Yunnan and Guizhou (1950–<br>2012)|
|[32]|Corn and Soybean (USA)|NDVI<br>(MOD16A2<br>ET<br>and<br>MOD13A3);<br>LST<br>(MOD11A2<br>and<br>MOD09A1);<br>TRMM 3B43|LST, NDVI, NDWI, NMDI, ET,<br>and TRMM|SPI at 54 stations (28 stations in the arid<br>region and twenty-six stations in the<br>humid region) from 1975 to 2012.<br>NDMC|
|[33]|Sierra Nevada Forest Tree<br>(California, USA)|MODIS<br>Terra<br>and<br>Aqua<br>observations<br>(MCD43A4,<br>collection<br>5);<br>DEM|NDVI, EVI, NDWI|reserved validation dataset from USDA<br>Forest Service (USFS) Aerial Detection<br>Surveys (ADS)|
|[34]|Nineteen percent rice paddies<br>and<br>64%<br>forests<br>(South<br>Korea)|TRMM 3B43, GPM IMERG ,<br>MCD43C4<br>,<br>MYD11C3<br>,<br>MYD13C2|SPI and SPEI from ASOS|SPI and SPEI calculated from 61 ASOS<br>weather stations, with 3-, 6-, 9-, and 12-<br>month time scales.|
|[35]|crop yield and land cover<br>(Korea)|AMSR-E, MODIS,TRMM|High resolution Soil Moisture<br>Drought Index (HSMDI|SPIs for March to November (2003–<br>2011); twenty-nine stations (1973 to<br>2011|
|[36]|agriculture (East Asia)|ESA-CCI for soil moisture;<br>MOD11C1 for LST and NDVI;<br>TRMM 3B42 forprecipitation|PCI, TCI, VCI, SDCI, SMCI,<br>MIDI, VSDI; Madden–Julian<br>Oscillation(MJO)Index;|Three satellite-based drought indices<br>SDCI, MIDI, and VSDI|
|[37]|three distinct climatic regions<br>including the mountainous<br>area (Iran)|GPCP,<br>CMAP,<br>CHOMPS,<br>PERSIANN-CDR,<br>TRMM,<br>MERRA-2 and GLDAS-2|nonparametric-SPI;<br>ORNESS-OWA;<br>ORLIKE-OWA;<br>K-nearest neighbors‟ algorithm<br>(KNN)|Precipitation<br>data<br>for<br>twenty-four<br>stations<br>(1981<br>-<br>2011);<br>the Fars Meteorological Organization<br>and Fars Regional Water Organization|
|[38]|pasture (Kenya)|MODIS and TAMSAT|NDVI, VCI, RFE, RCI, SPI|Precipitation data from TAMSAT|
|[39]|terrain<br>mountains,<br>plains,<br>basins, valleys, and River<br>(China)|Vegetation<br>index<br>product<br>(MOD13A3),<br>surface<br>temperature<br>product<br>(MOD11A2),<br>land use product (MCD12Q1),<br>and<br>TRMM,<br>SRTM-DEM.|<br>NDVI, EVI, LST, TCI, CI,<br>SPEI, AWC, VSWI, Percentage<br>of precipitation anomaly and<br>TRMM-Z index|_Fifteen major meteorological stations<br>and nine agricultural meteorological<br>stations<br>in<br>Henan<br>Province,<br>(http://data.cma.cn/).<br>_soil Available Water Capacity (AWC),<br>(http://globalchange.bnu.edu.cn/).|
|[40]|Bare land, Woodland, Water,<br>and Winter wheat (China)|MODIS NDVI, MODIS LST,<br>Sentinel-2<br>NDVI,<br>Sentinel-2<br>biophysical,ASTER GDEM|VCTI|Daily precipitation data in eighteen<br>selected counties of the Guanzhong<br>Plain|
|[41]|Darling<br>River<br>Basin<br>(Australia)|SMAP,<br>GLDAS,<br>Soil attribute product, GPM,<br>ISMN.|SWDI, SMDI|ISMN provides in situ Soil Moisture<br>(SM) measurements of 1400 stations<br>and<br>thirty-five<br>international<br>SM<br>networks available from 1952 to the<br>present. https://<br>ismn.geo.tuwien.ac. at|



Data are gathered from Table II. It turns out that the majority of studies employ MODIS satellite data products to gauge the extent of drought in different types of ecosystems. However, some studies use validation data received from data centers, while the majority of research is based on observations from ground observation stations. 

On the basis of the metadata analysis of the selected papers shown in Table III, _RQ_ 3 may be addressed by stating that the following categories can be used to categorize the application of machine learning in remote sensing for agricultural drought monitoring. The potency of each machine learning method is shown in Table III. There is evidence that ANN (91.00 percent in [31]), BRT (93 percent in [32]), GA (95.73 percent in [37]), and RF are algorithms with accuracy values of more than 90 percent (93 percent in [32] and 96.30 percent in [33]). 

Although the GA method competes with RF among other algorithms for the second-best accuracy value, in actuality, researchers frequently choose for the RF approach. This could be the result of a number of problematic situations and different facts. 

Responding to _RQ_ 4 based on an analysis of the metadata of a few articles as indicated in Table IV. The following four categories describe how machine learning is used in remote sensing to monitor agricultural drought. First, for prediction NDVI [30], waves [31], unmeasured area [34], drought [36], np-SPI [37], vegetation condition [38], and vegetation temperature [40]. Second, detect tree death [33]. Third, it measures degree of correlation (sixteen drought factors [32], various hazard factors [39]). Fourth, down-scaling (AMSR-E and TRMM [35], SMAP-SM [41]). 

768 | P a g e 

www.ijacsa.thesai.org 

_(IJACSA) International Journal of Advanced Computer Science and Applications,_ 

_Vol. 13, No. 12, 2022_ 

TABLE III. MACHINE LEARNING ALGORITHM FOR THE DROUGHT MONITORING APPROACH 

|**Algorithm**|**Ref.**||**Acc**|**uracy**||
|---|---|---|---|---|---|
|ANFIS|[37]|85.72||||
|ANN|[30], [31],<br>[38]|79.00|**91.00**|83.00||
|BRT|[32]|**93.00**||||
|CUBIST|[32]|60.00||||
|DFNN|[39]|85.60||||
|DT|[34]|15.92||||
|ERT|[34]|32.01||||
|ESTARFM-SVM|[40]|83.00||||
|GA-ORNESS-<br>OWA|[37]|**95.73**||||
|GAM|[38]|86.00||||
|GMDH|[37]|88.21||||
|KKN|[37]|89.68||||
|M5P model tree|[37]|89.78||||
|MLP|[37]|90.47||||
|PERSIANN|[41]|80.00||||
|RF|[32], [33],<br>[35], [36]|**93.00**|**96.30**|69.00|70.00|
|SVM|[40]|83.00||||
|SVR|[37]|83.57||||



TABLE IV. ROLE OF MACHINE LEARNING IN REMOTE SENSING FOR AGRICULTURE DROUGHT MONITORING 

|**Ref.**|**Algorithm**|**Role**|
|---|---|---|
|[30]|ANN|Forecast of NDVI|
|[31]|ANN|Forecasting future waves|
|[32]|RF; BRT; Cubist|Model of the relationship|
|[33]|RF|Detection trees mortality|
|[34]|DT; RF; ERT;|Models for decision making drought in<br>unmeasured areas|
|[35]|RF|Downscale AMSR-E soil moisture and<br>TRMMprecipitation|
|[36]|RF|Developed drought prediction models|
|[37]|KNN;<br>MLP;<br>ANFIS;<br>M5P;GMDH;SVR;GA|Estimating np-SPI based on remotely<br>sensed data|
|[38]|GAM; ANN|To predict vegetation conditions|
|[39]|DFNN|To construct models by considering a<br>number of various hazard factors|
|[40]|SVM; ESTARFM|Developing<br>a<br>fused<br>vegetation<br>temperature condition index(VTCI)|
|[41]|PERSIANN|Downscaled SMAP-SM as well as<br>GLDAS-SM against the in-situ SM|



Our review of the two literature with the highest yields [33], [37] showed that the results of the CRF model analysis [33] found that baseline summer NDVI or EVI was one of the key variables to differentiate significant tree mortality. Higher ground may be denser or have higher biomass, resulting in more opportunities to obtain more water during prolonged dry seasons, and thus more resistant to stressors and mortality. The model also reveals that altitude also plays a significant 

role in the vulnerability of the Sierra Nevada Forest to surviving drought conditions. Altitude affects the local climate and water availability, and thus affects the distribution and drought tolerance of forest types. Vegetation index Z-scores, such as NDVI, proved to be another important variable for detecting tree mortality. The NDVI z-score in a given year represents the cumulative impact of drought on vegetation activity, while the NDWI z-score shows reduced water content. Single-dated mid-resolution imagery from MODIS and VIIRS is limited for monitoring forest health and detecting mortality, particularly at finer scales, but higher temporal frequencies, e.g., daily coverage, are a major advantage for monitoring forest health and potential forecasting capabilities across the globe (big landscape). 

Meanwhile, the second-best body of research [37] demonstrates that the ORNESS-OWA fusion approach considerably enhances estimates compared to other models and that ORNESS-OWA performs better for long-term timelines than for short-term estimates. CHOMPS, GPCP, CMAP, PERSIANN-CDR, TRMM, GLDAS-2, and MERRA2 are some examples of remote sensing precipitation products that can be used to estimate np-SPI. Three sophisticated data fusion approaches (ORNESS-OWA, ORLIKE-OWA, and KNN) are also tested against ground-based np-SPI estimations. 

Even though they both employ various methodologies and observational settings, each with their own set of limitations, the two literatures produce the finest results to date. However, further research is still required to achieve results with higher spatial and temporal resolution, wider coverage, and more cost-effective operation. Future study will likely integrate satellite imagery data with field camera and aerial photography in order to provide a more comprehensive strategy that takes into account all factors, including the plant cycle. This will undoubtedly present new challenges. 

## V. CONCLUSION 

This systematic review has provided sophisticated quantitative and qualitative analysis in this fast-growing field. Since 2010, more than 1147 journal and conference papers were found, and this trend is expected to continue in the future. A selection of the 12 most cited papers was undertaken to obtain an in-depth view of the state of the research. Drought monitoring based on remote sensing is a very active area of research with a significant impact on enhancing global sustainability and optimizing natural resources. This is supported by sensor observation technology with open access to satellite data and advances in digital machine learning computational techniques. The role of Machine learning methods has proven to be effective in prediction, detection, correlation and downscaling tasks when processing satellite imagery data. 

## ACKNOWLEDGMENT 

This work was supported by the Infrormatics Program Study, Faculty of Computer Science, University of Singaperbangsa Karawang with Computer Science Department, Faculty of Mathematics and Natural Science, IPB Bogor University. 

769 | P a g e 

www.ijacsa.thesai.org 

_(IJACSA) International Journal of Advanced Computer Science and Applications, Vol. 13, No. 12, 2022_ 

## REFERENCES 

- [1] J. A. O. Reyes, D. E. Casas, J. L. Gandia, and E. F. Delfin, Drought impact on sugarcane production, vol. 35, no. June. 2021. 

- [2] T. Ji, G. Li, H. Yang, R. Liu, and T. He, “Comprehensive drought index as an indicator for use in drought monitoring integrating multi-source remote sensing data: A case study covering the Sichuan-Chongqing region,” Int. J. Remote Sens., vol. 39, no. 3, pp. 786–809, 2018, doi: 10.1080/01431161.2017.1392635. 

- [3] Y. D. Giroh and A. A. Girei, “Analysis of the Factors affecting Sugarcane ( Saccharum officinarum ) Production under the Out growers Scheme in Numan Local Government Area Adamawa State, Nigeria,” J. Educ. Pract., vol. 3, no. 8, pp. 195–201, 2012, [Online]. Available: www.iiste.org 

- [4] M. Â. C. C. de Carvalho et al., “Drought monitoring based on remote sensing in a grain-producing region in the cerrado–amazon transition, brazil,” Water (Switzerland), vol. 12, no. 12, pp. 1–16, 2020, doi: 10.3390/w12123366. 

- [5] A. K. Mishra and V. P. Singh, “Drought modeling - A review,” J. Hydrol., vol. 403, no. 1–2, pp. 157–175, 2011, doi: 10.1016/j.jhydrol.2011.03.049. 

- [6] Y. R. Li and L. T. Yang, “Sugarcane Agriculture and Sugar Industry in China,” Sugar Tech, vol. 17, no. 1, pp. 1–8, 2015, doi: 10.1007/s12355014-0342-1. 

- [7] S. Geerts et al., “Simulating yield response of quinoa to water availability with aquacrop,” Agron. J., vol. 101, no. 3, pp. 499–508, 2009, doi: 10.2134/agronj2008.0137s. 

- [8] J. R. Mahan, A. W. Young, and P. Payton, “Deficit irrigation in a production setting: Canopy temperature as an adjunct to ET estimates,” Irrig. Sci., vol. 30, no. 2, pp. 127–137, 2012, doi: 10.1007/s00271-0110269-1. 

- [9] M. M. Chaves et al., “How plants cope with water stress in the field. Photosynthesis and growth,” Ann. Bot., vol. 89, no. SPEC. ISS., pp. 907–916, 2002, doi: 10.1093/aob/mcf105. 

- [10] P. Steduto, T. C. Hsiao, E. Fereres, and D. Raes, Crop yield response to water. FAO IRRIGATION AND DRAINAGE PAPER 66, 2012. 

- [11] S. Mahajan and N. Tuteja, “Cold, salinity and drought stresses: An overview,” Arch. Biochem. Biophys., vol. 444, no. 2, pp. 139–158, 2005, doi: 10.1016/j.abb.2005.10.018. 

- [12] S. B. Idso, R. D. Jackson, P. J. Pinter, R. J. Reginato, and J. L. Hatfield, “Normalizing the stress-degree-day parameter for environmental variability,” Agric. Meteorol., vol. 24, no. C, pp. 45–55, 1981, doi: 10.1016/0002-1571(81)90032-7. 

- [13] H. G. Jones and P. Schofield, “Principles of thermal remote sensing.,” Heat Capacit. Mapp. Mission Anthol., pp. 7–14, 1982. 

- [14] E.-D. Schulze, E. Beck, and K. Muller-Hohenstein, Plant Ecology. Springer International Publishing, 2005. doi: 10.1016/j.ecoinf.2020.101136. 

- [15] H. G. Jones, “Remote detection of crop water „stress‟ and distinguishing it from other stresses,” Acta Hortic., vol. 922, pp. 23–34, 2011, doi: 10.17660/ActaHortic.2011.922.2. 

- [16] S. O. Ihuoma and C. A. Madramootoo, “Recent advances in crop water stress detection,” Comput. Electron. Agric., vol. 141, pp. 267–275, 2017, doi: 10.1016/j.compag.2017.07.026. 

- [17] S. Park, D. Ryu, S. Fuentes, H. Chung, M. O‟connell, and J. Kim, “Dependence of cwsi‐based plant water stress estimation with diurnal acquisition times in a nectarine orchard,” Remote Sens., vol. 13, no. 14, pp. 1–13, 2021, doi: 10.3390/rs13142775. 

- [18] Z. Zhu and C. E. Woodcock, “Continuous change detection and classification of land cover using all available Landsat data,” Remote Sens. Environ., vol. 144, pp. 152–171, 2014, doi: 10.1016/j.rse.2014.01.011. 

- [19] S. E. Franklin, O. S. Ahmed, M. A. Wulder, J. C. White, T. Hermosilla, and N. C. Coops, “Large Area Mapping of Annual Land Cover Dynamics Using Multitemporal Change Detection and Classification of Landsat Time Series Data,” Can. J. Remote Sens., vol. 41, no. 4, pp. 293–314, 2015, doi: 10.1080/07038992.2015.1089401. 

- [20] C. D. Man, T. T. Nguyen, H. Q. Bui, K. Lasko, and T. N. T. Nguyen, “Improvement of land-cover classification over frequently cloud- 

covered areas using landsat 8 time-series composites and an ensemble of supervised classifiers,” Int. J. Remote Sens., vol. 39, no. 4, pp. 1243– 1255, 2018, doi: 10.1080/01431161.2017.1399477. 

- [21] J. L. Peters, A. J. Sutton, D. R. Jones, K. R. Abrams, and L. Rushton, “The contribution of systematic review and meta-analysis methods to human health risk assessment: Neurobehavioral effects of manganese,” Hum. Ecol. Risk Assess., vol. 14, no. 6, pp. 1250–1272, 2008, doi: 10.1080/10807030802494592. 

- [22] C. N. Cook, H. P. Possingham, and R. A. Fuller, “Contribution of systematic reviews to management decisions,” Conserv. Biol., vol. 27, no. 5, pp. 902–915, 2013, doi: 10.1111/cobi.12114. 

- [23] E. C. O‟Hagan, S. Matalon, and L. A. Riesenberg, “Systematic reviews of the literature: A better way of addressing basic science controversies,” Am. J. Physiol. - Lung Cell. Mol. Physiol., vol. 314, no. 3, pp. L439–L442, 2018, doi: 10.1152/ajplung.00544.2017. 

- [24] W. Canon-Montanez and A. L. Rodriguez-Acelas, “Contribution of Systematic Reviews and Meta-analyses to Nursing Education, Research, and Practice,” Aquichan, vol. 21, no. 4, p. e2143, 2021, doi: 10.5294/aqui.2021.21.4.3. 

- [25] D. Tuia and G. Camps-Valls, “RECENT ADVANCES IN REMOTE SENSING IMAGE PROCESSING,” IEEE Int. Conf. Image Process., vol. 16, pp. 3661–3664, 2009, doi: 10.1117/12.913262. 

- [26] H. Z. M. Shafri, “Machine Learning in Hyperspectral and Multispectral Remote Sensing Data Analysis,” pp. 3–9, 2017, doi: 10.1142/9789813206823_0001. 

- [27] P. Martino, S. Vasileios, and J. A. Maria, Benchmarking of the Symbolic Machine Learning classifier with state of the art image classification methods Application to remote sensing imagery. 2015. doi: 10.2788/638672. 

- [28] A. E. Maxwell, T. A. Warner, and F. Fang, “Implementation of machine-learning classification in remote sensing: an applied review,” Int. J. Remote Sens., vol. 39, no. 9, pp. 2784–2817, 2018, doi: 10.1080/01431161.2018.1433343. 

- [29] M. J. Page et al., “The PRISMA 2020 statement: An updated guideline for reporting systematic reviews,” BMJ, vol. 372, 2021, doi: 10.1136/bmj.n71. 

- [30] A. F. Marj and A. M. J. Meijerink, “Agricultural drought forecasting using satellite images, climate indices and artificial neural network,” Int. J. Remote Sens., vol. 32, no. 24, pp. 9707–9719, 2011, doi: 10.1080/01431161.2011.575896. 

- [31] D. Long et al., “Drought and flood monitoring for a large karst plateau in Southwest China using extended GRACE data,” Remote Sens. Environ., vol. 155, pp. 145–160, 2014, doi: 10.1016/j.rse.2014.08.006. 

- [32] S. Park, J. Im, E. Jang, and J. Rhee, “Drought assessment and monitoring through blending of multi-sensor indices using machine learning approaches for different climate regions,” Agric. For. Meteorol., vol. 216, pp. 157–169, 2016, doi: 10.1016/j.agrformet.2015.10.011. 

- [33] S. Byer and Y. Jin, “Detecting drought-induced tree mortality in Sierra Nevada forests with time series of satellite data,” Remote Sens., vol. 9, no. 9, pp. 14–17, 2017, doi: 10.3390/rs9090929. 

- [34] J. Rhee and J. Im, “Meteorological drought forecasting for ungauged areas based on machine learning: Using long-range climate forecast and remote sensing data,” Agric. For. Meteorol., vol. 237–238, pp. 105–122, 2017, doi: 10.1016/j.agrformet.2017.02.011. 

- [35] S. Park, J. Im, S. Park, and J. Rhee, “Drought monitoring using high resolution soil moisture through multi-sensor satellite data fusion over the Korean peninsula,” Agric. For. Meteorol., vol. 237–238, pp. 257– 269, 2017, doi: 10.1016/j.agrformet.2017.02.022. 

- [36] S. Park, E. Seo, D. Kang, J. Im, and M. I. Lee, “Prediction of drought on pentad scale using remote sensing data and MJO index through random forest over East Asia,” Remote Sens., vol. 10, no. 11, pp. 1–18, 2018, doi: 10.3390/rs10111811. 

- [37] M. R. Alizadeh and M. R. Nikoo, “A fusion-based methodology for meteorological drought estimation using remote sensing data,” Remote Sens. Environ., vol. 211, no. March, pp. 229–247, 2018, doi: 10.1016/j.rse.2018.04.001. 

- [38] C. Adede, R. Oboko, P. W. Wagacha, and C. Atzberger, “A mixed model approach to vegetation condition prediction using Artificial 

770 | P a g e 

www.ijacsa.thesai.org 

_(IJACSA) International Journal of Advanced Computer Science and Applications, Vol. 13, No. 12, 2022_ 

Neural Networks (ANN): Case of Kenya‟s operational drought monitoring,” Remote Sens., vol. 11, no. 9, pp. 1–18, 2019, doi: 10.3390/rs11091099. 

- [39] R. Shen, A. Huang, B. Li, and J. Guo, “Construction of a drought monitoring model using deep learning based on multi-source remote sensing data,” Int. J. Appl. Earth Obs. Geoinf., vol. 79, no. 219, pp. 48– 57, 2019, doi: 10.1016/j.jag.2019.03.006. 

monitoring at field scales using Sentinel-2 and MODIS imagery,” Comput. Electron. Agric., vol. 168, no. 17, p. 105144, 2020, doi: 10.1016/j.compag.2019.105144. 

   - [41] B. Fang, P. Kansara, C. Dandridge, and V. Lakshmi, “Drought monitoring using high spatial resolution soil moisture data over Australia in 2015–2019,” J. Hydrol., vol. 594, no. July 2020, p. 125960, 2021, doi: 10.1016/j.jhydrol.2021.125960. 

- [40] X. Zhou, P. Wang, K. Tansey, S. Zhang, H. Li, and L. Wang, “Developing a fused vegetation temperature condition index for drought 

771 | P a g e 

www.ijacsa.thesai.org 

