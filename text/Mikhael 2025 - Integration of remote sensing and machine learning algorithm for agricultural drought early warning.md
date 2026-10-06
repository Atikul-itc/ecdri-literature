Environ Monit Assess (2025) 197:243 https://doi.org/10.1007/s10661-025-13708-0 

RESEARCH 



# **Integration of remote sensing and machine learning algorithm for agricultural drought early warning over Genale Dawa river basin, Ethiopia** 

## **Mikhael G. Alemu · Fasikaw A. Zimale** 

Received: 18 June 2024 / Accepted: 24 January 2025 / Published online: 4 February 2025 © The Author(s), under exclusive licence to Springer Nature Switzerland AG 2025 

**Abstract** Drought remains a menace in the Horn of Africa; as a result, the Ethiopia’s Genale Dawa River Basin is one of the most vulnerable to agricultural drought. Hence, this study integrates remote sensing and machine learning algorithm for early warning identification through assessment and prediction of index-based agricultural drought over the basin. To track the severity of the drought in the basin from 2003 to 2023, a range of high-resolution satellite imagery output indexes were used, including the Vegetation Condition Index (VCI), Thermal Condition Index (TCI), and Vegetation Health Index (VHI). Additionally, the Artificial Neural Network machine learning technique was used to predict agricultural drought VHI for the period of 2028 and 2033. Results depict that during the 2023 period, 25% of severe drought and 18% of extreme drought countered at 

the lower part of the basin at Dolo ado and Chereti regions. A high TCI value was found that around 23.24% under extreme drought and low precipitation countered in areas of Moyale, Dolo ado, Dolobay, Afder, and Bure lower than 3.57 mm per month. Similarly, increment of severe drought from 24.26% to 24.58% and 16.53% to 16.58% of extreme drought value of VHI might be experienced during the 2028 and 2033 period respectively in the area of Mada Wolabu, Dolo ado, Dodola, Gore, Gidir, and Rayitu. The findings of this study are significantly essential for the institutes located particularly in the basin as they will allow them to adapt drought-coping mechanisms and decision-making easily. 

**Keywords** Agricultural drought · Artificial Neural Networks · Genale Dawa river basin 

M. G. Alemu (*) Department of Climate Change Engineering, Pan African University Institute for Water and Energy Sciences -Including Climate Change (PAUWES), Tlemcen, Algeria e-mail: michaelgetu22@gmail.com 

M. G. Alemu 

Action for Human Rights and Development, PO Box 1551, Adama, Ethiopia 

F. A. Zimale Faculty of Civil and Water Resources Engineering, Bahir Dar Institute of Technology, Bahir Dar University, Bahir Dar, Ethiopia e-mail: fasikaw@gmail.com 

## **Introduction** 

The world is plagued by frequent devastating drought events, thus, making drought one of the most natural disasters. In recent decades, droughts have increased due to global warming and can have detrimental effects on the environment, economy, health, and agriculture (Ndehedehe et al., 2023; Liu et al., 2023; Raihan, 2023; Fleming ‐ Muñoz et al., 2023). Drought is the biggest threat to crops and cattle in almost every region of the world, indirectly affecting an estimated 55 million people annually (Talisuna et al., 

Vol.: (0123456789) 

**243** Page 2 of 25 

Environ Monit Assess (2025) 197:243 

2020; Thornton et al., 2022). According to the World Health Organization (2023) report, drought puts people’s livelihoods in jeopardy, raises the possibility of illness and death, and encourages mass migration and 40% of the world’s population suffers from water scarcity, and by 2030, up to 700 million people could face displacement due to drought. 

A drought is an extended dry spell that can happen anywhere in the world as part of the natural climatic cycle (Rezvani et al., 2023). Also, there is a scarcity of water as a result of the slow-onset calamity caused by the absence of precipitation (Dabrowska et al., 2023). Typically, drought falls into one of the following categories: meteorological, hydrological, agricultural, and socioeconomic (Lin et al., 2023; Pan et al., 2023; Sun et al., 2023; Zhou et al., 2023). While each type of drought has a distinct severity but agricultural drought is the most damaging as it directly affects natural ecosystems and drastically lowers crop output. 

Agricultural drought can sometimes develop quickly and become increasingly challenging to control. For instance, Shi et al. (2022) present a conceptual framework for comprehending the combined effects of the drought on Gansu Province’s Yuzhong County, in China focusing on five farmer clusters in the county’s southern parts. As a result, there was a significant economic loss and widespread drought disaster throughout the nation, which increased the rate of food insecurity and the affordability gap. Additionally, USA went through severe drought from 2014 to 2016. Grass, fodder, and plantains were the crops most severely damaged by the year 2015 in Puerto Rico; taken collectively and they accounted for 85% of in agricultural losses and $14 million damage (Holupchinski et al., 2020). Similarly, at SubSaharan Africa, Ahmed (2020) assessed the effects of future climate change and drought-driven agricultural policies on the effectiveness of large-scale irrigation projects. After the severe drought of 1984, the optimal scenario demonstrated that the growth of food crops on the more costly cash crops led to a drop of 83% in gross net benefits and a loss of 63% in irrigation water. 

The continent of Africa, particularly the Horn of Africa is highly vulnerable to drought. According to the International Federation of Red Cross and Red Crescent Societies (2023), an updated report depicts that, acute food insecurity affected 23.4 million people in the Horn of Africa (HoA) due to the protracted 

drought, and 5.1 million children in drought-stricken parts of Ethiopia, Kenya, and Somalia suffered from acute malnutrition. The drought is thought to have forced 2.7 million people to relocate. Hence, Ethiopia is one of the nations that is vulnerable to high drought frequency, and a majority of the drought percentage is contributed from the Genale Dawa river basin. Estimating agricultural drought in the Genale Dawa River Basin, Ethiopia, is vital for ensuring food security, as the region heavily depends on rain-fed agriculture (Alemayehu & Kabite, 2023). In addition to World Bank (2020) report shows that the Borena region of Oromia has been considered a drought-prone lowlands in recent decades which is found in this basin (Negewo & Sarma, 2021; Tessema et al., 2020). Poor soil and water conservation (SWC) planning and management (Tessema et al., 2020), water stress is caused by change in future climate conditions (Negewo & Sarma, 2021), insufficient information about the relationship between vegetation variability and climate (Alemayehu & Kabite, 2023), the intensity, speed, and degree of land use/land cover (LULC) change (Ayalew & Nigussie, 2023), and ground water potential resource of the basin (Kassahun & Mohamed, 2018) are the primary reason for drought occurrence in the basin. As such, to lessen the detrimental effects of agricultural droughts on freshwater supplies, natural ecosystems, agriculture, and food production, precise monitoring of agricultural droughts in the study area is necessary. 

There are numerous ways to cope with the agricultural drought monitoring and its identification all over the world. Users can monitor drought conditions at a very fine spatial scale by applying satellite imagery to offer high-resolution data (Cai et al., 2023; Derradji et al., 2023; Mullapudi et al., 2023). The importance of remote sensing is enormous, particularly in areas where it is difficult to monitor the intensity of drought. To evaluate the response of transitional ecosystems, certain regions used the Normalized Ecosystem Drought Index (NEDI) (Gidey et al., 2018), the Standardized Precipitation Evapotranspiration Index (SPEI) (Dong et al., 2023), the Standardized Precipitation Index, and the Palmer Drought Severity Index (PDSI) (Wang et al., 2022), and the Standardized Precipitation Index (SPI) (Alemu et al., 2023a, b) is frequently employed. Hence, these approaches might not be as helpful for evaluating other types of droughts, such as agricultural or socioeconomic drought, since 

Vol:. (1234567890) 

Page 3 of 25 **243** 

Environ Monit Assess (2025) 197:243 

they do not take into account how drought affects vegetation health and productivity. To evaluate the effects of heat and water stress on vegetation development, three drought indicators are used: the Vegetation Condition Index (VCI), the Thermal Condition Index (TCI), and the Vegetation Health Index (VHI) (Ren et al., 2023; Senhorelo et al., 2023; Zeng et al., 2023). Moreover, several studies also took into account the Soil Moisture Content (SMC), Modified Normalized Difference Water Index (MNDWI), and Normalized Vegetation Difference Index (NDVI) when evaluating agricultural drought (Bandak et al., 2023; Priya et al., 2023; Qi et al., 2022). Recently, determining SMC using remote sensing become advanced and able to improve the severity of agriculture drought. For instance, Zhu et al. (2023) and Yin et al. (2023) use GLDAS Noah (the Noah land surface model driven by Global Land Data Assimilation System) against two in situ observation networks. While, the GLDAS Noah model performs better than the other soil moisture products with less degree of uncertainty. 

In addition to analyzing actual agricultural droughts through remote sensing, researchers are becoming more and more interested in estimating future agriculture droughts using machine learning (ML) due to the significance growth of population and food deficit. Kafy et al. (2023) investigated the use of machine learning (ML) methods for predicting drought using NDVI, LST, Precipitation, SMC, TCI, and VCI indicators over Bangladesh using Artificial Neural Network (ANN) algorithms. Additionally, Khan et al. (2020) also performed models of random forest (RF), multivariate linear regression, support vector regression, autoregressive integrated moving average (AMIRA), and convolutional neural network to predict drought in Pakistan. Over the study area, most of the article focused on the historical agricultural drought analysis including Tessema et al. (2020) and Negewo and Sarma (2021). Hence, estimating the agricultural drought vulnerability using machine learning considering VHI is still unreached and in addition to that, predicting agricultural drought significantly contributes on the drought scenario estimation over the study area. Thus, the outcome is crucial for making decisions on different research fields and identifying the severity of drought in the future. Hence, the article focused on the assessing and estimation of agricultural drought on the future. So to assess, the study monitors the spatiotemporal 

dynamics of agricultural drought risk over the Genale Dawa river basin from 2003 to 2023 using NDVI, MNDWI, TCI, VCI, VHI, precipitation, and soil moisture variables. Also, it predicts VHI change using ANN-CA algorithms for years 2028 and 2033. 

## **Material and methodology** 

## Description of the study area 

The study area is located in the Eastern part of Africa (Fig. 1A) particularly in Ethiopia, which is the third largest basin. It is situated between 3°30′, 7°20′ north latitude and 37°05′, 43°20′ east longitude, covering 171,050  km<sup>2</sup> and represents 13.87% of the nation’s total area and it is distinguished by a highly diverse landscape that includes plains, steep gorges, high, rough mountains, and plateaus with a flat top (Mengistu et al., 2022). There are five sub-basins in the Genale-Dawa river basin; the primary rivers defining the basin are Weyb and Genale-Dawa, along with their respective sub-catchments; the other two subbasins, Lege-Sure and Bare have no permanent water courses, with the latter being fully within the Somali area. Three regional entities make up the basin: Oromia (91,901  km<sup>2</sup> ) contains 53% of the basin, Somali Region (77,901  km<sup>2</sup> ) contains 45%, and the Southern Nations, Nationalities and Peoples (SNNP) (3067 km<sup>2</sup> ) contains 1.8%. Mount Dimtu, the highest mountain in the Oromia region of the basin, is located on the northern edge of the basin and has an attitude that decreases from north to south at 4377 m above sea level (Alemayehu & Kabite, 2023). The region experiences bimodal rainfall, with a mean of 772 mm and a range of 425 mm to 1429 mm (Negewo & Sarma, 2021). It is believed that the lowlands in the Borena region of Oromia are susceptible to drought. There is a minor peak in April and a maximum peak in August in the semi-bimodal rainfall pattern in the GenaleDawa Lowland area. The lower portion of the basin is not developing as much because of persistent water scarcity (Alemayehu & Kabite, 2023). 

## Remote sensing data collection and preprocessing 

Landsat satellite images are the primary data used for the assessment of drought in the study area. The images were taken during the pre-monsoon period 

Vol.: (0123456789) 

**243** Page 4 of 25 

Environ Monit Assess (2025) 197:243 



**Fig. 1** Location map of Genale Dawa river basin: ( **A** ) East African basins including Ethiopian basins, ( **B** ) Genale Dawa river basin including sub-Administrations 

(extreme heat, and little rain) season of Ethiopia from March up to May. The data was downloaded from USGS Earth Explorer (https:// earth explo rer. usgs. gov/) under (cloud cover < 5%) for the years 2003–2023 at 5 years interval periods with a resolution of 30*30 m at 168/54 path and row respectively for all Landsat’s. Before the data is subjected to further analysis, data preparation is a crucial step in the study. After downloading, the data were put through a mosaic, radiometric and atmosphere corrected, the zero value pixels were removed, and the spatial extent of the data was clipped. The next step was organizing and setting up the data for analysis, which included choosing the right bands and data layers and resampling the data to the required spatial resolution. The right band selection is important because NDVI, LST, MNDWI, TCI, VCI, and VHI parameters were assessed using various bands from Landsat 7 ETM, Landsat OLI/TIRS 8, and Landsat OLI/TIRS 9. Additionally, from 2003 to 2023, soil moisture content 

(SMC) was estimated using the GLDAS-NOAH model and the data available at https:// giova nni. gsfc. nasa. gov/ giova nni. at various depths (0–10 cm, 10–40 cm, and 40–100 cm). Finally, the precipitation data was extracted from the Climate Hazard Group InfraRed Precipitation with station data CHRIPS-V2 (https:// data. chc. ucsb. edu/ produ cts/ CHIRPS- 2.0/) used as input analysis. As Solomon et al. (2018) and Klutse et al. (2021) discussed, CHIRPS models provide better correlation and significantly reduce biases and error by comparing different climate models and being able to capture the daily rainfall characteristics as well. Hence, the same model was used in this analysis. 

Drought driving Index parameters estimation 

There are numerous driving factors for the analysis of drought in the study area. NDVI, MNDWI, SMC, precipitation TCI, VCI, and VHI are commonly used 

Vol:. (1234567890) 

Page 5 of 25 **243** 

Environ Monit Assess (2025) 197:243 

parameters to assess drought conditions (Gelata et al., 2023; Alshammari & Mohammed, 2023; Ezzahra et al., 2023; Kafy et al., 2023). 

For calculating this spectral index NDVI using satellite data on vegetation, reflectance in the red and near-infrared (NIR) wavelengths was used (Eq. (1)). The reflectance bands vary based on the Landsat images (Kim et al., 2020; Mirzaee & Mirzakhani Nafchi, 2023). NDVI outputs are also used for Land surface emissivity measurement for surface emits thermal radiation. Greater vegetation cover and productivity are indicated by higher values of the NDVI, which range from − 1 to 1. This spectral indicator has negative values that are near to (− 1) high probability of being a water resource, a (0)-value that indicates no green leaves, and 0.2 to 0.3 values that indicate barren soil (Al-Kindi et al., 2023; Eisfelder et al., 2023). For this study, the NDVI values were categorized into different classes, ranging from no vegetation to healthy vegetation (Table 2), taking into account the features of the research area. Lower NDVI values might be the result of decreased productivity and vegetation cover during a drought. It is feasible to evaluate the effects of drought on vegetation health and productivity by tracking NDVI values over time. 



MNDWI is an additional metric that efficiently distinguishes between urban and water areas in satellite imagery (Alshammari & Mohammed, 2023). Additionally, it reduces how much other indices reflect the features of built-up areas, which are typically linked to open water. This has proven to be more precise and accurate as the noise of the vegetation and the builtup areas can be mitigated with the assistance of green and medium infrared bands (Mousa et al., 2022). The range of MNDWI readings was + 1 for pure water and − 1 for vegetation and land surface. Because light is absorbed, the MNDWI provides higher positive values of − 1 to + 1 for water than the NDWI’s nearinfrared (NIR) range (Mousa et al., 2022). Hence, short-wave infrared 1 (SWIR1) and visible green (GREEN) spectral bands are used in this procedure (Eq. (2)). 



Satellite data that can be integrated and has the qualities of high precision and a wide observable range can be used to estimate agricultural potential and available water storage (Nakalembe et al., 2021). This study addresses soil moisture, including subsurface soil water obtained from satellite data, excluding groundwater, which is limited to plant roots or surface soil water. GLDAS-NOAH model soil moisture content at different depths was the primary input for the analysis of the correlation with drought and to examine SMC the data captured from 2003 to 2023 with an interval of 5 years. 

Variations in the climate during the agricultural drought play a crucial role. Notably, there is a virtual impact from long-term changes in temperature and precipitation due to change in drought increment (Amognehegn et al., 2023; Orke & Li, 2022; Yadeta et al., 2020). The CHIRPS-V2 satellite data was utilized to record the monthly variation in precipitation, and the satellite images were utilized to compute the Land Surface Temperate (LST) for temperature by selecting the relevant bands. The outputs are scaled Digital Numbers (DN) that have been quantized and calibrated to represent the multispectral image data (Cao et al., 2020). The Landsat 8 and Landsat 9 product data, obtained through the use of the Thermal Infrared Sensor (TIRS) and Operational Land Imager (OLI), are provided in an unsigned integer format of 16 bits (Masek et al., 2020). Conversely, the data from a single sensor is used to create Landsat 7 products, which are provided in an 8-bit unsigned integer format (Dwyer et al., 2018). Therefore, different formulas are used to extract brightness temperatures from the top of the atmosphere (TOA) and convert them to radiance. Plank’s law is used to estimate the Land surface temperature (LST) using Landsat thermal bands (Pahlevanzadeh et al., 2019). For the Landsat TM image digital numbers of the thermal band (band 6) for Landsat image 7 and band (10) for Landsat images 8 and 9 were converted into radiance using the following Eqs. (3) and (4) respectively. 







where; _L휆_ = TOA spectral radiance (Watts/(m.<sup>2</sup> * srad * μm)), QCAL = digital number,  LMINλ = spectral 

Vol.: (0123456789) 

**243** Page 6 of 25 

Environ Monit Assess (2025) 197:243 

radiance scales to QCALMIN,  LMAXλ = spectral radiance scales to QCALMAX, QCALMIN = the minimum quantized calibrated pixel value (typically = 1), QCALMAX = the maximum quantized calibrated pixel value (typically = 255), _ML_ = Bandspecific multiplicative rescaling factor, _AL_ = Bandspecific additive rescaling factor and _Qcal_ = Quantized and calibrated standard product pixel values (DN) 





where; _T_ = Top of atmosphere brightness temperature (K), _L휆_ = TOA spectral radiance (Watts/(m<sup>2</sup> * srad * μm)), _K_ 1 = Band-specific thermal conversion constant for Landsat 7 “666.09”, for Landsat 8 “774.8853” and for Landsat 9 “799.0284”, _K_ 2 = Band-specific thermal conversion constant for Landsat 7 “1282.71”, for Landsat 8 “1321.0789”, and for Landsat 9 “1329.2405”. 

**Table 1** Corresponding NDVI and emissivity for land surface temperature (LST) (Kafy et al., 2023) 

|NDVI|emissivity (Ɛ)|
|---|---|
|NDVI <  − 0.185|0.995|
|− 0002E185 ≤ NDVI < 0.157|0.970|
|0.157 ≤ NDVI ≤ 0002E727|1.0094 + 0.047 ln (NDVI)|
|NDVI > 0.727|0.990|



To conduct LST, several driving factors affect the surface emissivity including surface topography and moisture (Neinavaz et al., 2020; Taylor et al., 2020). To cope with such, factor integration of NDVI was conducted for measuring emissivity (Kasim et al., 2020; Neinavaz et al., 2020). Table 1 indicates the emissivity factor with NDVI correspondence. 





where; T = represents the sensor’s brightness temperature, ρ = 1.43*10<sup>−2</sup> mk, Plank’s constant (h) = 6.6261034 J.s, velocity of light (c) = 2.998108 m  s<sup>−2</sup> and Boltzmann constant ( σ ) = 1.381023 J  K<sup>−1</sup> . 

## Estimation of drought indices 

Estimation of drought is a combination of driving variables and classified as extreme, severe, moderate, mild and no drought (Table 2). One often used drought indicator in remote is the Vegetation Health Index (VHI) (Elfadli & Zurqani, 2022; Zeng et al., 2023). Numerous academics have used VHI for a variety of objectives that may have an immediate impact on society, such as assessing losses in wheat output or examining the expansion of malaria vectors, among other things (Abdelradi et al., 2020; Kogan, 2023a, b). Additionally, VHI measures how well a 

**Table 2** Overall indexes threshold values and corresponding drought severity ranges (Kafy et al., 2023) 

|NDVI, Rainfall|, and LST thres|hold values and|their correspon|ding classes|Drought seve|rity Ranges|||
|---|---|---|---|---|---|---|---|---|
|NDVI Range|Classes|Rainfall<br>(mm/month)|Classes|LST Range<br>(℃)|TCI Range<br>(%)|VCI Range<br>(%)|VHI Range<br>(%)|Drought<br>Severity|
|< 0.15|No Vegeta-<br>tion|< 2|Light rainfall|> 31|>45|< 10|0–10|**Extreme**|
|0.15 =  < 0.30|Poor Vegeta-<br>tion|2- < 10|Light rainfall|31—27|45- < 35|10- < 20|10- < 20|**Severe**|
|0.30 =  < 0.45|Moderate<br>Vegetation|10- < 100|Moderate<br>rainfall|27—24|35- < 25|20- < 30|20- < 30|**Moderate**|
|0.45 =  < 0.60|Sparse|100- < 250|Heavy rain-<br>fall|24—21|25- < 15|30- < 40|30- < 40|**Mild**|
|≥ 0.60|Dense Veg-<br>etation|≥ 250|Very Heavy<br>Rainfall|< 21|< 15|>40|>40|**No**|



Vol:. (1234567890) 

Page 7 of 25 **243** 

Environ Monit Assess (2025) 197:243 

plant can withstand stress. It can be used to analyze drought-related issues, and eventually, to create mitigating and adaptable remedies (van Ginkel & Biradar, 2021; Lubanyana, 2021). The temperature (TCI) and vegetation (VCI) distributions, which are obtained from observations made during various electromagnetic spectrum windows, have a significant impact on the VHI indices (Table 2). TCI, which is obtained from the thermal infrared window and discusses how temperature affects vegetative stress (Bento et al., 2020; Xu et al., 2022). On the other hand, VCI, which is based on visible and near-infrared components, illustrates how NDVI is typically used to compute the moisture state of the vegetation (Ali et al., 2023; Pham et al., 2022). Both VCI and TCI range between 0 and 100 in percentile. High values of VCI indicate that the vegetation values are stable (Table 2), whereas high TCI identifies that the plant is under stress due to high temperatures and low precipitation to make the SMC dry (Cheng et al., 2022; Kafy et al., 2023). VCI, TCI, and VHI can be computed by Eqs. (9), (10), (11) reactively. 







where; _훼_ is the weighting factor that determines the relative importance of the VCI and TCI in the calculation of the VHI, NDVI, and LST = value of a given pixel and period,  NDVImin/LSTmin = Minimum value of NDVI/LST for all pixels  NDVImax/LSTmax = Maximum value of NDVI/LST for all pixels. 

Selection of machine learning modelsfor drought prediction 

For the prediction of drought using mathematical models, the involvement of driving variables works the essential part to find transition locations. Today, a variety of machine learning models can be applied to precisely approximate and generate the drought and landcover change including Multi-Layer Perceptron (MLP); (Girma et al., 2022), Logistic Regression 

(LR); (Gaur et al., 2020), Multi-Criteria Evaluation (MCE); (Niway et al., 2022), Weights of Evidence (WoE); (Gayen & Saha, 2017), and Random Forest (RF); (Elbeltagi et al., 2023) which are some of them used to generate the transition. The article uses MLP using Artificial neural network (ANN) as a consideration for the analysis of the comparison due to the familiarity and gives a reasonable output of drought prediction potential of mathematical algorisms over the Ethiopian basins using Cellular Automata (CA) simulation (Damtew et al., 2022; Girma et al., 2022; Shawul & Chakma, 2019). Additionally, ANN models occasionally struggle to precisely estimate the temporal and spatial variations of the drought. These models can be paired with CA models using QGIS software under MOLUSCE Plugin, where the CA can add the spatial link, to get over this issue. 

## _Artificial neural network (ANN)_ 

An ANN and CA-based model, in which the CA predicts temporal changes and the ANN provides transition potential maps, can be used to predict future droughts (VHI) as mentioned in Fig. 2. To estimate the VHI by using ANN six driving variable (NDVI, MNDWI, Precipitation, LST, TCI, and VCI) used as input for the model to train until sufficient and accurate results are obtained (Fig. 2). During inputing the driving variable, the historical data from 2003 to 2023 used to estimate VHI for 2028 by following the sequence of the neutrals. Next to that, for estimating 2033 the estimated 2028 included as a drive for the other. After predicting, the An ANN is a directed graph made up of layers of nodes, each of which is completely connected to the layer below it (Gagrani 



**Fig. 2** Overall schematics of Artificial Neural Network for the prediction of drought over Genale Dawa 

Vol.: (0123456789) 

**243** Page 8 of 25 

Environ Monit Assess (2025) 197:243 

et al., 2022). By altering the input and output layer weights, the ANN model is trained via the backpropagation technique. The model performance depends on hyperparameters such as the number of layers, learning rate, and iterations (Eq. (12)). Big learning rates and momentum allow fast learning, but the learning process can be unstable. Small learning rate and momentum mean stable, but slow learning ANN value (Lv, 2021). 



where _f_ is the activation function, _N_ is the number of neurons, and _W_ are the ANN model weights and _b_ is the bias vector. A binary classification MLP’s output is a value between 0 and 1, which could be considered as the probability of the positive target class. Given data input _Xi_ ( _i_ = 1, 2,..., _N_ ), the neural model output _y_ can be obtained. Model selection was performed by optimizing the number of hidden layers and the number of hidden neurons per layer of the ANN using training data. 

## Model calibration, validation, and accuracy assessment 

Model calibration is a crucial stage for machine learning with an actual drought calibration and validation was done by evaluating the model’s capability to capture drought change, the persistence of each class, as well as the spatial distribution of the change. There are a number of metrics that may be used to validate a model. This study used Kappa coefficients Eq. (13), precision Eq. (14), and recall Eq. (15) and also by combining a model’s precision and recall scores, two opposing metrics, which has led to its extensive application in machine learning (Korotcov et al., 2017; Venugopalan et al., 2021). Hence, the f1-score is used in addition to ensure accuracy in the prediction machine learning model Eq. (16). This alternative machine learning evaluation metric is important for the analysis of the multi-classification metrics since it elaborates on a model’s performance on a class-wide basis rather than evaluating it overall based on accuracy (Ajagbe et al., 2021; Tahir et al., 2023). Lastly, accuracy counts the percentage of cases that are correctly classified out of all the objects in the dataset. 

To analyze the driving variable relation, Pearson’s correlation method was used to assess between variables. According to De Winter et al. (2016), Pearson’s correlation,  (rp,) which was defined as the covariance of the two variables divided by the product of their standard deviations, the linear correlation between two variables is measured parametrically Eq. (17). How closely two maps agree concerning the quantity of cells in each category and the placement of the cells in each category can be determined with precision using kappa indices. 



where; r = number of rows and columns in the error matrix, N = the total number of observations (pixels) Xii = observation in row i and column i,  Xii +  = marginal total of rows i, and x + 1 = marginal total of column i. Perfect agreement is indicated by a Kappa coefficient of 1, whereas a number near to 0 indicates that the agreement is just slightly better than would be predicted by chance. 









where, _TP_ ; Total True Positive counts across all classes, _FP_ ; Total False Positive is the sum of false positive counts across all classes, _FN_ ; Total False Negative is the sum of false negative counts across all classes. 



The Pearson’s correlation coefficient, or  rp, is between − 1 and 1. A value of 0 indicates that there is no linear relationship between the two variables, but values of 1 and − 1 indicate perfect positive and negative relationships, respectively with reference to Daba and You (2022). Existing and potential characteristics 

Vol:. (1234567890) 

Page 9 of 25 **243** 

Environ Monit Assess (2025) 197:243 

of the study region include height, slope gradient, separation from the main road, and separation from the rivers considered for this study. 

## **Results** 

Drought driving parameters distribution 

## _Variation of vegetation distribution (NDVI)_ 

The Normalized Difference Vegetation Index (NDVI) is a commonly utilized remote sensing metric for assessing vegetation cover because of its strong sensitivity to vegetation and a key indicator of the agricultural drought in the Genale Dawa river basin from 2003 to 2023. Figure 3A–E illustrates the vegetation coverage over the Genale Dawa river basin and it shows that the majority of the basin region’s NDVI coverage is suspected under the moderate and less vegetation during 

the entire period in Oromia and Somali province. Through the period, the proportion of vegetation coverage decreased in both Oromia and Somali provinces, whereas, the Southern Nations Nationalities and Peoples (SNNP) province increased and became dense vegetation, particularly at the upper part of the basin at the end of the period. During the entire period lower part of the basin experiences poor and moderate vegetation cover in an area of Filtu, Moyale, Adelana Wadera, and Libera. Additionally, Afder, Chereti, and Bare were exposed to no vegetation coverage during 2018 and 2023 year. The lower part of the Genale Dawa river basin experiences less amount of rainfall and is exposed to high climate change. 

The large portion of moderate and poor vegetation coverage during the years 2003 and 2008 found in the Oromia and Somali provinces covers 35.88% and 41.98% of the basin particularly in the sub-region of Goro and Bare respectively are the highest proportion areas (Fig. 3A and B) and 



**Fig. 3** Historical indices from “A up to E” for NDVI, from “F up to J” for MNDWI, and from “K up to O” for LST over the Genale Dawa river basin during 2003–2023 period 

Vol.: (0123456789) 

**243** Page 10 of 25 

Environ Monit Assess (2025) 197:243 

(Fig. 7A). Spare vegetation coverage found in the upper part of the basin at Southern Nations Nationalities and Peoples (SNNP) province covers 18.64% and 18.65% during the 2003 and 2008 periods of the basin and increased significantly through the period. During the 2023 period, the highest coverage of NDVI found under Poor Vegetation covers 54.38% (Fig. 7A). 

## _Variation of MNDWI and SMC_ 

Nowadays, one of the major leading concerns about agriculture drought is access to surface water and soil moisture content particularly in the basin. The result illustrated the variation of MNDWI index being spatially higher during 2008 period (between − 0.99 and 0.88) values in the upper part of the basin SNNP province in the area of Bensa, Bore, Hawasa, and Adolana Wadera (Fig. 3A). On the other hand, for the past 10 years (2013–2023) the basin has been under low water stress MNDWI 

(around − 0.87 to 0.99) due to altering amount of precipitation. The agricultural drought, available adaptation strategies, and soil loss are all directly correlated with the MNDWI and SMC. Hence, historical SMC was extracted from the GLDAS-NOAH model Soil Moisture Content (SMC) at different depths for the Genale Dawa river basin to identify the relation with agricultural drought moisture content between years 2003 and 2023 (Fig. 4). Water in the top 10 cm of the soil is known as surface soil moisture, whereas water and organic matter accessible to plants typically thought to be in the upper soil is known as root zone soil moisture. When it comes to the production of crops, the subsoil, which is found at a depth of 40–100 cm, greatly varies with ground water depletion, and the SMC depth of 10–40 cm is the soil layer that initiates fertility as a result of plowing. Overall, the basin is significantly vulnerable to SMC, particularly at the lower part of the basin which is directly correlated with MNDWI and the rainfall of the basin. 



**Fig. 4** Historical GLDAS-NOAH model Soil Moisture Content (SMC) of Genale Dawa river basin at depth of 0_10 cm; “A–E”, 10_40 cm; “F–J” and 40_100 cm; “K–O” for 2003 up to 2023 periods 

Vol:. (1234567890) 

Page 11 of 25 **243** 

Environ Monit Assess (2025) 197:243 

The upper part of the basin has comparatively the highest concentration of SMC in overall depths. During the year 2018, province of SNNPs and Oromia experienced the maximum SMC in the as Adaba, Goba, and Bule sub-regions reached high SMC at a depth of 0–10 cm around 37.61 kg/m<sup>2</sup> , 37.19 kg/m<sup>2</sup> , and 35.91 kg/m<sup>2</sup> reactively (Fig. 4D). Additionally, in the same area, the SMC experiences 112.40 kg/m<sup>2</sup> at a depth of 10–40 cm and 222.64 kg/m<sup>2</sup> at a depth of 40–100 cm (Fig. 4I and N). In reverse at Oromia province, partial part of sub-region Hagere Mariam was observed (around 15.80 kg/m<sup>2</sup> ) and at Somali subregion Dolo ado (around 16.10 kg/m<sup>2</sup> ) of moisture content during the year 2008 at a depth of 0–10 cm countered (Fig. 4B). Similarly, at depth of 10–40 and 40–100 cm, Hagere Mariam sub-region area experience the low SMC severity (around 39.82 kg/m<sup>2</sup> and 55.37 kg/m<sup>2</sup> ) (Fig. 4G and L). Overall, the results showed that lower SMC as elevation decreased and deeper soil and higher SMC were linked to easier vertical water movement. 

## _Precipitation and temperature distribution_ 

In Ethiopia, climate change is one of the threats due to variations of temperature and rainfall that cause significant climate events like drought. Historically, the study area was exposed to low-intensity rainfall and high temperature at the lower part of the basin for a long time (Fig. 5) and (Fig. 3) respectively. The nation’s terrain, which is varied in terms of mountains, divided plateaus, valleys, plains, and lowlands, influences how much rainfall and temperature are in each area. 

The upper part of SNNPs province including Hawassa, Bore, Uraga, and Yirgachefe shows a high amount of rainfall intensity but through time the rainfall concentration during the pre-monsoon period shifted into the Oromia region. The highest and dominant rainfall occurred during the year 2023 at the Odo shkiso, Uraga, and Hulla around 255.30 mm, 249.80 mm, and 245.22 mm respectively (Fig. 5E). Lower rainfall consecration dominantly occurred in 



**Fig. 5** Historical CHRIPS-V2 value from “A up to E”, TCI result from “F up to J” and VCI result from “K up to O” over the Genale Dawa river basin during 2003–2023 period 

Vol.: (0123456789) 

**243** Page 12 of 25 

Environ Monit Assess (2025) 197:243 

the entire basin, except for the SNNP province. But during the 2003 year at Chereti and Dolo ado subregions depicts low concentration of rainfall which is around 2.93 mm and 3.57 mm (Fig. 5A). One of the main challenges of agricultural droughts is an increment of temperature over the basin. Figure 3A to O demonstrates the Land Surface temperature (LST) over the basin derived from the remote sensing bands reflectance. In the year 2018, the spatial temperature coverage of the basin was high at Liben, Afder, Dolobay, and Bare around 30.16 ℃ , 34.50 ℃ , 37.51 ℃ , and 34.06 ℃ respectively (Fig. 3N). The hottest coverage of the basin occurred in the 2013 period between 31 and 27 ℃ and covered 38.22% of the basin. On the reverse, the coldest period occurred during the 2008 period covering 64.52% of the basin (Fig. 7B). Since this pre-monsoon period, there is no sufficient rainfall and high temperature, particularly in the lower part of the basin which makes the basin favorable for agricultural drought and indirectly affects the economic, environmental, social impacts and health risks on humans. Hence, it results in the basin being under severe climate anxieties in terms of related causes of drought. 

## _Variation of VCI, TCI, and VHI for drought assessment_ 

VCI and TCI are one of the main driving variables indices used to identify the severity of the drought throughout the remote sensing studies. Both indices are essential for identifying and understanding the vegetation standard over the study area. Hence each variable has its characteristics and contribution to estimating the agricultural drought, particularly VHI value. The VCI can represent abrupt weather variations, remove spatial variations in the NDVI, lessen the influence of physical or biological system characteristics including weather, soil, vegetation type, and topography, and create regional comparability, whereas, TCI is used to quantify the impact that extreme heat and moisture have on plants. 

As seen in Fig. 5, high TCI can be a warning of significant levels of moisture stress and evaporation brought on by intense heat, while low VCI can be a symptom of agricultural dryness in the basin. Unfortunately, the TCI and VCI indices are not accurate enough to determine the drought conditions of the study region; instead, it is preferable to use the 

values of the vegetation health indices (VHI) when computing the drought conditions. Reduced VHI levels might be interpreted as an indicator of worsening drought conditions since low VHI values can suggest dry or stressed vegetation. Many variables, such as high evaporation, limited rainfall, and high temperatures, can all exacerbate drought conditions and result in a decline in the VHI. 

As a result, the index value of TCI, VCI, and VHI seems quite related. In the basin, a high VCI value was observed during the years 2008, 2013, and 2018, and the basin vegetation condition lies under no drought up to moderate drought for the entire basin. The maximum VCI percentage occurred in almost more than half of the entire basin is around 69.14%, 71.28%, and 51.30% respectively (Fig. 5L, M, and N) and (Fig. 7D). However, because of the high heat wave, the TCI value affects soil moisture conditions and controls transpiration and evapotranspiration values in basins that are classified as experiencing extreme, severe, and moderate drought (Fig. 5F to J). About 41.48% of TCI was observed during the year of 2013 and 58.54% in the year of 2018 particularly, in Oromia and Somali provinces (Fig. 5H and J) and (Fig. 7C). Such vulnerability is more suspected in the basin under severe drought. VHI value occurred in response to the VCI and TCI values, which resulted in the basin drought being under moderate drought intensity. The highest VHI or agricultural drought intensity occurred in the year of 2008 and covers 44.34% of the entire basin area (Fig. 7D). Next to that, 31.72% intensity occurred during the 2013 period, and the worst severe experience at year of 2018 (Fig. 6B, C, and D) and (Fig. 7D). The dominant provinces that VHI highly impacts are Oromia and Somali regions in the areas of Liben, Bare, Dolo ado, Moyale, Filtu, Hagere Maryam, and Ginir (Fig. 6B, C, and D). 

## Drought correlation with driving parameters 

An evaluation of the correlation between NDVI, MNDWI, Precipitation (PCP), SMC (0_10 cm, 10_40 cm, and 40_100 cm), VCI, TCI, and VHI has been carried out to determine the relationship and it enhances comprehension of the historical record. Figure 8 from (A up to E) depicts the overall historical correlation of the study area. There is a positive correlation between the (VHI, TCI, and VCI) and (PCP 

Vol:. (1234567890) 

Page 13 of 25 **243** 

Environ Monit Assess (2025) 197:243 



**Fig. 6** Historical Vegetation Health Indices (VHI) of Genale Dawa river basin during the 2003–2023 period form “A up to E” respectively 

and SMC 0–10 cm) in the early period of 2003. Furthermore, there is a positive link between VCI and NDVI, while a negative association exists between TCI and LST (Fig. 8A). Similarly, the highest positive correlation countered between (VHI and TCI), (VCI and NDVI) and (TCI and MNDWI) and a negative correlation was found between LST and VHI during the 2008 period. In both periods, the vegetation health index is significantly affected by the variation of LST and indirectly by the lack of precipitation which causes the soil moisture to dry over the basin and consequently, decreases the vegetation coverage (NDVI) and leads to severe drought. 

In contrast, from 2013 up to 2023 the highest positive correlations were countered among (PCP and NDVI), (PCP and SMC 0–10). A negative correlation was found between (LST and MNDWI) in the years of 2013, and 2023 (Fig. 8C and E) and between (LST and TCI) in a year of 2018 and 2023 (Fig. 8D and E). At this period, the insufficient amount of precipitation over the basin is the main reason to experience the severity of drought. A low concentration of MNDWI is related to the high temperature for the past 10 years puts the basin under drought. In the study area, there is a massive loss of vegetation that 

is exposed to severe drought and the main constraints are PCP and LST indirectly affect the basin’s lack of vegetation coverage. Temperature and precipitation both have the power to alter the surface’s moisture balance because excessive heat can alter agricultural and hydrological dryness, resulting in increasing transpiration, evaporation, and precipitation. It can also hasten the variability of drought by changing the amount of rainfall or inducing less of it. 

## Model performance and accuracy assessment 

For the prediction of drought over the study area, calibrating the driving variable is an essential step. NDVI, precipitation, MNDWI, LST, VCI, and TCI are the main driving variables to predict VHI. At the initial period of the process, every pixel size of the variable must be at the same size to conduct the analysis. By utilizing ANN-CA algorithms historical transition, VHI from 2003 up to 2013 was used to estimate VHI for 2018, and from 2003 up to 2018, VHI was used for predicting VHI 2023 through training the neural networks for better understanding of algorithm calibration performance of kappa values. The model ANN learning rate, momentum 

Vol.: (0123456789) 

**243** Page 14 of 25 

Environ Monit Assess (2025) 197:243 



**Fig. 7** Overall historical indices area coverage in percent; “A” for NDVI, “B” for LST, “C” for TCI, “D” for VCI, and “E” for VHI over the Genale Dawa river basin during the 2003–2023 period 

factor, and iteration values were altered till accurate results were achieved. For this study, initial training for ANN model 1000 random points from input VHI was selected by the model as the initial iteration in the training procedure. The learning rate of 0.045 and 0.015 momentum values were used for the better performance overall calibration kappa in both predictions and Table 3 depicts the overall 0.872 for the validation result of VHI 2018 and 0.887 for the VHI 2023 was observed. It indicates the algorithm able to predict with a precise result. 

After validating the model, the performance of the predicted model was conducted through precision, recall, and f1-score. Based on the results, the actual VHI with the predicted model output shows a high precision. Table 4 indicates the overall performance conducted through python environment by taking random samples for each pixel-categorized drought class for both actual and predicted VHI. The ANNCA algorithm predicts better performance and overall accuracy shows around 0.894 and 0.931 precision for VHI 2018 and 2023 respectively. It depicts the model 

Vol:. (1234567890) 

Page 15 of 25 **243** 

Environ Monit Assess (2025) 197:243 



**Fig. 8** Overall Historical drought driving variables correlation among the respective variables over Genale Dawa river basin during the 2003–2023 period form “A up to E” respectively 

**Table 3** Overall kappa and correctness value of VHI validated ANN-CA algorithms results for the years 2018 and 2023 

||Model calibratio|n||Model valid|ation|||
|---|---|---|---|---|---|---|---|
|Input VHI for|Change of over-|Min valida-|Current|% of Cor-|Kappa location|Kappa historical|Kappa overall|
|model analysis|all accuracy|tion error|kappa value|rectness||||
|VHI of 2018|**− 0.00157**|0.0091|0.894|86|0.823|0.871|0.872|
|VHI of 2023|**− 0.00136**|0.0079|0.917|88|0.851|0.920|0.887|



|**Table 4**Machine<br>algorithm predicted model||Predicted V|HI 2018||Predicted V|HI 2023||
|---|---|---|---|---|---|---|---|
|VHI 2018 and 2023|Drought categories|precision|recall|f1-score|precision|recall|f1-score|
|erformance throuh||||||||
|p g<br>precision, recall, and|Extreme drought|0.800|0.878|0.837|0.929|0.929|0.929|
|f1-score analysis|Severe drought|0.848|0.872|0.860|0.957|0.946|0.951|
||Moderate drought|0.943|0.911|0.927|0.919|0.955|0.936|
||Mild drought|0.922|0.879|0.900|0.883|0.912|0.897|
||No drought|0.697|0.885|0.780|1.000|0.816|0.899|
||Accuracy|0.894|0.894|0.894|0.931|0.931|0.931|
||Macro-average|0.842|0.885|0.861|0.938|0.912|0.923|



Vol.: (0123456789) 

**243** Page 16 of 25 

Environ Monit Assess (2025) 197:243 

performing very well in estimating future drought over the study area. Additionally, Table 5 depicts the overall errors between the VHI 2018 and 2023, and results show that there is no significant change in the area as well as percentile change for each multi-class. 

## Drought prediction analysis 

After the model was validated carefully and using ANN-CA forced to generate the predicted VHI for estimation and identify the hazardous area in the basin for the upcoming decades (2028 up to 2033). As Fig. 9 and Table 6 illustrate, the VHI value predicted for the drought of different years and in Oromia and Somali regions are the severity of extreme drought expected to increase. Overall, 16.53% of extreme drought is expected during the 2028 year and rises by the end of 2033 to 16.58% and it covers 24,267.30 and 24,341.63  km<sup>2</sup> respectively. Similarly, severe drought is expected to be 24.26% during the 2028 period and covers 35,611.65  km<sup>2</sup> and 24.58% expected by the year 2033 and it covers 36,561.63  km<sup>2</sup> of the basin. The moderate drought comparatively shows a decrease in change from 2028 to 2033 by 21.32% to 20.18% by the end of the period (Fig. 9A and B). In comparison to the historical change, the severity of drought increased during (2018–2028 and 2018–2033) by 11.99% and 12.04% respectively under the extreme drought stage (Fig. 10B). Such drought highly dominated the Somali and Oromia provinces around Dolo ado, 

Elkere areas during the 2028 period. Additionally, during the 2033 year, Dolobay was also included as a hazardous area (Fig. 9A and B). With a similar pattern of agricultural drought, some of the basin areas are situated under extreme and severe drought for the coming years. 

Similarly, in the study area, the historical change in drought is high under the categories of severe drought. During the 2003–2013 period, there was a 25.65% severe drought and during 2008–2013 period showed a slight decrease to 24.25% and in recent years (2018–2023) the change increment in severity drought is around 2.74%. But, to reverse the severe drought shifted into extreme drought and trend is expected to continue during 2028 and 2033 years. The interpolated spatial extent of extreme drought frequency was the highest in the case of Somali and some parts of Oromia regions for the upcoming decades. 

## **Discussions** 

Nowadays, identifying, assessing and analyzing the severity of the drought is a major step for building adaptation mechanisms. Further estimation leads us to understand the early warning of drought which significantly contributes for sustainability development. NDVI is one of them and the result shows poor vegetation coverage of the study area and it decreases throughout the period in the lower part of the basin 

**Table 5** Overall area as well as percentile change of Actual and Predicted VHI 2018 (A) and VHI 2023 (A) 

|A)|Actual VHI||Predicted VHI||Change analysis||
|---|---|---|---|---|---|---|
|Drought categories|Area 2018|2018%|Area 2018|2018%|Change in Area|Change in Percentile|
|Extreme drought|6667.71|4.54|7331.95|5.00|664.24|0.45|
|Severe drought|33,903.79|23.09|33,609.61|22.90|− 294.18|− 0.19|
|Moderate drought|73,243.71|49.89|72,019.40|49.07|− 1224.31|− 0.82|
|Mild drought|23,432.30|15.96|22,807.92|15.54|− 624.38|− 0.42|
|No drought|9565.79|6.52|11,006.13|7.50|1440.34|0.98|
|B)|||||Change analysis||
|Drought categories|Area 2023|2023%|Area 2023|2023%|Change in Area|Change in Percentile|
|Extreme drought|26,992.44|18.39|24,730.22|16.85|− 2262.22|− 1.54|
|Severe drought|37,920.91|25.83|36,792.43|25.07|− 1128.48|− 0.76|
|Moderate drought|32,498.52|22.14|34,263.42|23.34|1764.90|1.21|
|Mild drought|27,185.59|18.52|27,843.03|18.97|657.44|0.45|
|No drought|22,215.83|15.13|23,145.89|15.77|930.07|0.64|



Vol:. (1234567890) 

Page 17 of 25 **243** 

Environ Monit Assess (2025) 197:243 



**Fig. 9** Overall historical drought driving variables correlation among the respective variables over Genale Dawa river basin during the 2003–2023 period form “A up to E” respectively 

particularly the Oromia and Somali province including in area of Filtu, Moyale, Adelana Wadera, and Libera. Such less vegetation coverage occurs due to high vulnerability to climate change (Dagnachew et al., 2020; Hussien et al., 2023; Takele et al., 2022). Additionally, the positive correlation among the precipitation and negative correlation with LST indirectly causes the soil moisture to dry over the basin and consequently, decreases the vegetation coverage (NDVI) and leads to severe drought. Alemayehu and Kabite (2023) discussed the variation of climate variables (rainfall and temperature) in response to vegetation greenness (NDVI) in the Genale Dawa river basin. Additionally, Stojanovic et al. (2022) analyzed the correlation of precipitation with soil moisture due to lack of sufficient precipitation over the Ethiopian basins. Both authors concluded that climate change significantly affects the basin vegetation coverage over the study area. These factors also cause the study 

area to become severely sifted to a lack of agricultural coverage throughout the entire period (Aneseyee et al., 2020; Chere et al., 2022; Moisa et al., 2022). 

Next to that, the SMC and MNDWI another of the major leading driving variable concerning about agriculture drought is access to surface water and soil moisture content (Liou & Mulualem, 2019; Mera, 2018). The higher MNDWI index was found in the 2008 period but, from 2013 to 2023 period significantly decreased in the lower part of the basin which impacts the agriculture productivity (Gashaw et al., 2023; Tessema et al., 2020). Low water stress MNDWI (around − 0.87 to 0.99) occurs due to altering amount of precipitation, groundwater recharge, surface runoff, actual evapotranspiration, lateral flow, water output, and river flows, causing water stress in the basin (Kassahun & Mohamed, 2018; Negewo & Sarma, 2021). Recently, the county has experienced a change in climate due to the rise in 

Vol.: (0123456789) 

**243** Page 18 of 25 

Environ Monit Assess (2025) 197:243 



**Fig. 10** Overall historical drought driving variables correlation among the respective variables over Genale Dawa river basin during the 2003–2023 period form “A up to E” respectively 

**Table 6** Historical and predicted drought coverage in squire kilometer  (km<sup>2</sup> ) during the year 2003–2033 at the Genale Dawa river basin 

|Drought categories|2003|2008|2013|2018|2023|2028|2033|
|---|---|---|---|---|---|---|---|
|Extreme drought|37,207.33|29,228.60|14,039.93|24,267.30|24,341.18|24,267.30|24,341.18|
|Severe drought|24,729.09|26,843.65|62,445.61|36,611.65|36,561.63|35,611.65|36,561.63|
|Moderate drought|44,783.88|65,099.39|46,568.53|31,293.20|31,091.23|31,293.20|31,091.23|
|Mild drought|37,557.49|18,910.76|16,681.23|26,262.66|25,687.11|27,300.30|25,687.11|
|No drought|2535.50|6730.89|7078.00|28,340.20|29,093.84|28,340.20|29,093.84|



temperature at different basins (Alemu & Wubneh, 2023). Temperature and precipitation both have the power to alter the surface’s moisture balance because excessive heat can alter agricultural and hydrological dryness, resulting in increasing transpiration, evaporation, and precipitation. Historical GLDAS-NOAH model Soil Moisture Content (SMC) at different depths (0–10, 10–40 and 40–100) cm used for identifying the relation with agricultural drought moisture content. Depending on the kind of crop, numerous variables, such as soil type and related plants, affect soil moisture content as well as meteorological conditions (Rasheed et al., 2022). Overall, the basin is significantly vulnerable to SMC, particularly at the lower part of the 

basin which is directly correlated with MNDWI and the rainfall of the basin and the upper part of the basin has comparatively the highest concentration of SMC in all depths. Even though the SMC concentration varies in different areas, the lower portion of the basin including the Oromia and Somali regions depicts a significantly low conservation of SMC compared to Ethiopian basins (Bekele et al., 2023; Sishah et al., 2023; Sishah et al., 2023). One of the ultimate challenges of SMC is a poor concentration of rainfall and water (Mengistu et al., 2022; Negewo & Sarma, 2021), high heat waves, massive soil loss (Dechasa et al., 2022), and poor soil rehab mechanisms in the basin (Dejene et al., 2023; Mustefa et al., 2023; Tessema et al., 2020). 

Vol:. (1234567890) 

Page 19 of 25 **243** 

Environ Monit Assess (2025) 197:243 

In Ethiopia, climate change is one of the threats due to variations of temperature and rainfall that cause significant climate events like drought (Alemu et al., 2022, 2023a, b; Bogale & Erena, 2022). The premonsoon period of the study area is exposed to dry periods and regions are on the edges, and the majority of the population is pastoralist (livestock dependent) and agropastoral (meaning they also produce crops for subsistence farming) particularly in Oromia and Somali provinces (Dejene et al., 2023; Mohamed et al., 2023; Worku et al., 2022). Such severity is one of the causes of drought initiation and accelerated its severity in Genale Dawa river basin for the past year (Dejene et al., 2023; Muse et al., 2023). The occurrence of rainfall in the basin during the pre-monsoon period shifted from SNNP into the Oromia region. The dominant rainfall occurrence found at the Odo shkiso by the year of 2023 around 255.30 mm and lower found at the SNNP province around 2.93 mm at the Chareti sub-region. Such low rainfall occurrence during the entire period made the basin vulnerable to Metrological drought and indirectly affects the agricultural drought, especially in the Somali province as discussed by Mohamed et al. (2023) and Bogale and Erena (2022) over Kebri Dahar district. The hottest coverage of the basin occurred in the 2013 period between 31 and 27 ℃ and covered 38.22% of the basin. Such variation impacts drought especially in agriculture directly related to the rainfall as well as temperature change (Alemu et al., 2023a, b). Since pre-monsoon period, there is no sufficient rainfall and high temperature, particularly in the lower part of the basin makes the basin vulnerable for agricultural drought and indirectly affects the economic, environmental, social impacts and health risks on humans. One of the implications is, since the late 2020, the region has seen four unsuccessful rainy seasons in a row, causing one of the worst droughts caused by climate change in the Borena region of Genale Dawa basin (Gemechu et al., 2020). And also, Shibru et al. (2023) emphasized that drastic rainfall, temperature increases, and are the main factors contributing to climate concerns drought in the Basin. 

VCI and TCI are the driving variables used to identify the severity of the drought throughout remote sensing studying (Jalayer et al., 2023; Zhao et al., 2022). To improve the precision of drought conditions quantifying VHI more preferable (Chere & Debalke, 2023; Fentaw et al., 2023). As a result, the 

index value of TCI, VCI, and VHI seems positively correlated. The maximum VCI percentage occurred in almost more than half of the entire basin around 71.28%. However, because of high value of TCI, the soil moisture conditions vulnerability is more suspected in the basin under severe drought. The dominant provinces that VHI highly impacted are Oromia and Somali regions in areas of Liben, Bare, Dolo ado, Moyale, Filtu, Hagere Maryam, and Ginir. Dejene et al. (2023) determined the standardized precipitation index (SPI), which is used to determine the extent, intensity, and severity of drought during the rainy season, at Borena woredas, which are located in the Genale Dawa river basin. This allows for the monitoring of the characteristics of the drought in the southern Ethiopian region. The findings indicate that, there were severe and extreme droughts during both the second wet season and the first rainy season. Furthermore, Zewdu (2020) also analyzed similar impact of climate change on the livestock system and pastoralist adaptation over Dolo Ado woredas in the Somali region. The severity of drought is directly related to the rainfall variation and it increases the high refugee status due to extreme severity and high starvation during 2008–2023 in the study area (Betts et al., 2023). VHI affects the drought’s susceptibility, particularly by influencing the occurrence of extreme heat episodes and their effects on people’s health and welfare (Ainembabazi, 2022; Wright et al., 2020). In addition to destroying crops and driving up food costs, droughts brought on by VHI cause financial losses for impoverished households and farmers (Hammad & Falchetta, 2022; Kar, 2022). 

For the prediction of drought over the study area, calibrating and validating the driving variable is an essential step. NDVI, Precipitation, MNDWI, LST, VCI, and TCI are the main driving variables to predict VHI. Overall, validation kappa of 0.872 for predicted VHI 2018 and 0.887 for the VHI 2023 of Kappa was observed. And the predicted VHI value depicts that there is an increment of extreme drought in the Oromia and Somali regions in both durations (2028 and 2033). Overall, there is an increment of extreme drought from 16.53% to 16.58% during 2028 and 2033 respectively. Similarly, severe drought is expected to be 24.26% during the 2028 period and covers 35,611.65  km<sup>2</sup> and increases into 24.58% by the year 2033 and it covers 36,561.63  km<sup>2</sup> of the basin. In comparison to the historical change, the 

Vol.: (0123456789) 

**243** Page 20 of 25 

Environ Monit Assess (2025) 197:243 

severity of drought increased during 2018–2028 and 2018–2033 by 11.99% and 12.04% respectively under the extreme drought stage. Such drought highly dominated the Somali and Oromia provinces around Dolo Ado, Elkere during the 2028 period. Additionally, during the 2033 year, Dolobay was also included as a hazardous area. After evaluating the trend and using the drought severity index (VCI) to evaluate the patterns of drought during the cropping season, Liou and Mulualem (2019) report that the drought severity over the central highlands and northwest region of Ethiopia is getting worse. According to the results, such change in extreme drought trend in Ethiopia observed in areas were exposed to drought. As highlighted, the spatial extent of extreme drought frequency at the Somali and some parts of Oromia regions for the upcoming decades. 

## **Conclusion and recommendation** 

The study assesses and predicts the agricultural drought hazard area over the Genale Dawa river basin, Ethiopia. The basin is highly vulnerable to climate change particularly on precipitation and temperature variation during the pre-monsoon period. Several driving variables including NDVI, MNDWI, precipitation, SMC, LST, TCI, and VCI were used to assess the agricultural drought VHI. Furthermore, machine learning algorithm of Artificial Neural Network (ANN) with integration of Cellular Automata (CA) was also used to predict the agricultural drought hazard for 2028 and 2033 year. 

For proactive planning and risk mitigation assessing and estimating 5-year interval agricultural drought index is crucial. It helps to quantify drought severity, predict trends, and identify vulnerable areas, enabling timely interventions like improved irrigation and drought-resistant crops. In the lower part of the basin at Oromia and Somali province, there is less concentration of NDVI and simultaneously there is low access to SMC and MNDWI during the assessment period. Additionally, the severity of the agriculture drought has significantly correlated with LST values and indirectly affects the TCI and VHI results. Most of the basin agricultural drought occurs in the sub-region of Dolo Ado, Dodola shows a severe and extreme drought during the 2018 and 2023 period. The predicted model was 

well performed and the confusion metrics kappa and the overall accuracy of precision, recall, and f1-score becomes 0.894. Somali provinces at Dolo ado and Elkere were exposed to 16.53% extreme and 24.26% severe drought spatially in VHI for the 2028 period and a slight increase to 16.58% of extreme and 24.58% of severe drought at similar areas and includes Dolobay regions during the 2033 period. The outcome is essential for the natural resources and maintaining the water balance of the study area to protect the basin from drought. It is imperative to advocate for the creation of long-term local and national strategies and their execution regarding the protection of natural resources and drought hazard in Genale Dawa river basin. By providing timely and pertinent information regarding the evaluation and monitoring of drought change, as well as its effects on the physical and human environment, such studies are significant to ensure that the drought can secure the effect of the nations in the best possible ways in the future. Furthermore, it guides policy decisions, resource allocation, and climate resilience strategies, and in reducing the socio-economic impacts. 

Promoting climate-resilient agriculture is critical at the basin, including drought-resistant crop varieties and the adoption of sustainable practices such as crop rotation and agroforestry. Enhancing water resource management is another aspect through efficient irrigation systems like drip and sprinkler irrigation, along with the construction of water harvesting structures, can optimize water use and storage during wet periods. Strengthening vegetation cover through afforestation and reforestation programs with native and drought-tolerant species will help improve soil moisture retention and combat land degradation. 

**Author contribution** Mikhael G. Alemu and Fasikaw A. Zimale contributed to the study. Mikhael G. Alemu analyzed and wrote up the manuscript and Fasikaw A. Zimale reanalysis the result and edited the manuscript. All authors contributed to the study and agreed to the publication. 

**Data availability** No datasets were generated or analysed during the current study. 

### **Declarations** 

**Ethics approval** All authors have read, understood, and have complied as applicable with the statement on “Ethical responsibilities of Authors” as found in the Instructions for Authors. 

Vol:. (1234567890) 

Page 21 of 25 **243** 

Environ Monit Assess (2025) 197:243 

Based on the assurances provided by the authors regarding the ethical conduct of the study, we certify that the work is original, has never been published, and is not currently being considered for publication anywhere. 

We attest that the previously mentioned authors have read the work over and given approval. Again, to reiterate, the only person you should contact regarding the editing process is the Corresponding Author. 

**Competing interests** The authors declare no competing interests. 

## **References** 

- Abdelradi, Fadi, and Dalia Yassin. (2020). “Climate impact on Egyptian agriculture: An efficiency analysis approach.” _Climate Change Impacts on Agriculture and Food Security in Egypt: Land and Water Resources—Smart Farming—Livestock, Fishery, and Aquaculture_ : 603–24. 

- Abdule, M., Abay, A. M., & Woldemichael, A. (2023). Impact of climate and land use/cover changes on streamflow in Yadot Watershed, Genale Dawa Basin, Ethiopia. _Air, Soil and Water Research, 16_ , 11786221231200106. 

- Ahmed, S. M. (2020). Impacts of drought, food security policy and climate change on performance of irrigation schemes in Sub-Saharan Africa: The case of Sudan. _Agricultural Water Management, 232_ , 106064. 

- Ainembabazi, Suzan. (2022). “Comparison of Standardized Precipitation Index (SPI) and Vegetation Health Index (VHI) in drought monitoring in Isingiro District.” 

- Ajagbe, S. A., Amuda, K. A., Oladipupo, M. A., Oluwaseyi, F. A., & Okesola, K. I. (2021). Multi-classification of Alzheimer disease on magnetic resonance images (MRI) using deep convolutional neural network (DCNN) approaches. _International Journal of Advanced Computer Research, 11_ (53), 51. 

- Alemayehu, Z., & Gizachew K. (2023). “Spatiotemporal climate and vegetation trends, and their relationship: A case of Genale Dawa Basin, Ethiopia.” _Remote Sensing Applications: Society and Environment_ : 101070. 

- Alemu, M. G., & Wubneh, M. A. (2023). Climate extreme indices analysis and spatiotemporal trend variation over Lake Tana Sub-Basin, Upper Blue Nile Basin, Ethiopia: Under future climate change. _Arabian Journal of Geosciences, 16_ (12), 1–27. 

- Alemu, M. G., Wubneh, M. A., Worku, T. A., Womber, Z. R., & Chanie, K. M. (2023a). Comparison of CMIP5 models for drought predictions and trend analysis over mojo catchment, Awash Basin. _Ethiopia. Scientific African, 22_ , e01891. 

- Alemu, M. G., Wubneh, M. A., Sahlu, D., & Zimale, F. A. (2023b). Spatiotemporal change of climate extremes under the projection of CMIP6 model analysis over Awash Basin, Ethiopia. _Sustainable Water Resources Management, 9_ (6), 195. 

- Alemu, Mikhael G, Melsew A Wubneh, and Tadege A Worku. (2022). “Impact of climate change on hydrological response of Mojo River Catchment, Awash 

River Basin, Ethiopia.” _Geocarto International_ (justaccepted): 2152497. 

- Ali, S. S., Koyel, M., Papia K, & Piu S. (2023). “Spatiotemporal agricultural drought monitoring using remote sensing indices.” In _Advancement of GI-Science and Sustainable Agriculture: A Multi-Dimensional Approach_ , Springer, 41–58. 

- Al-Kindi, K. M., Nadhairi, R. A., & Akhzami, S. A. (2023). Dynamic change in Normalised Vegetation Index (NDVI) from 2015 to 2021 in Dhofar, Southern Oman in response to the climate change. _Agriculture, 13_ (3), 592. 

- Alshammari, L., & Mohammed, O. N. (2023). Monthly drought monitoring of the surface water area of Sawa Lake, Iraq during 2016–2022 using remote sensing data. _Periodicals of Engineering and Natural Sciences, 11_ (1), 48–63. 

- Amognehegn, A. E., Nigussie, A. B., Adamu, A. Y., & Mulu, G. F. (2023). Analysis of future meteorological, hydrological, and agricultural drought characterization under climate change in Kessie Watershed, Ethiopia. _Geocarto International, 38_ (1), 2247377. 

- Aneseyee, A. B., Elias, E., Soromessa, T., & Feyisa, G. L. (2020). Land use/land cover change effect on soil erosion and sediment delivery in the Winike Watershed, Omo Gibe Basin, Ethiopia. _Science of the Total Environment, 728_ , 138776. 

- Ayalew, Solomon E, and Tewodros A Nigussie. (2023). “Historical and projected land-use/land cover changes of the Welmel River Watershed, Genale Dawa Basin, Ethiopia.” _Journal of Water and Land Development_ : 89–98. 

- Bandak, S., Movahedi Naeini, S. A. R., Komaki, C. B., Verrelst, J., Kakooei, M., & Mahmoodi, M. A. (2023). Satellite-based estimation of soil moisture content in croplands: A case study in golestan Province, north of Iran. _Remote Sensing, 15_ (8), 2155. 

- Bekele, Daniel, Agumassie G., Daniel M., & Andargachew D. (2023). “Remote sensing based soil moisture estimation for agricultural productivity: A note from Lake Tana Sub Basin, NW Ethiopia.” 

- Bento, V. A., Gouveia, C. M., DaCamara, C. C., Libonati, R., & Trigo, I. F. (2020). The roles of NDVI and land surface temperature when using the Vegetation Health Index over dry regions. _Global and Planetary Change, 190_ , 103198. 

- Betts, A., Stierna, M. F., Omata, N., & Sterck, O. (2023). Refugees welcome? Inter-group interaction and host community attitude formation. _World Development, 161_ , 106088. 

- Bogale, G. A., & Erena, Z. B. (2022). Drought vulnerability and impacts of climate change on livestock production and productivity in different agro-ecological zones of Ethiopia. _Journal of Applied Animal Research, 50_ (1), 471–489. 

- Cai, S., Zuo, D., Wang, H., Xu, Z., Wang, G., & Yang, H. (2023). Assessment of agricultural drought based on multi-source remote sensing data in a major grain producing area of Northwest China. _Agricultural Water Management, 278_ , 108142. 

- Cao, H., Gu, X., Wei, X., Yu, T., & Zhang, H. (2020). Lookup table approach for radiometric calibration of miniaturized 

Vol.: (0123456789) 

**243** Page 22 of 25 

Environ Monit Assess (2025) 197:243 

multispectral camera mounted on an unmanned aerial vehicle. _Remote Sensing, 12_ (24), 4012. 

- Cheng, M., Li, B., Jiao, X., Huang, X., Fan, H., Lin, R., & Liu, K. (2022). Using multimodal remote sensing data to estimate regional-scale soil moisture content: A case study of Beijing. _China. Agricultural Water Management, 260_ , 107298. 

- Chere, Z., Abegaz, A., Tamene, L., & Abera, W. (2022). Modeling and mapping the spatiotemporal variation in agricultural drought based on a satellite-derived Vegetation Health Index across the highlands of Ethiopia. _Modeling Earth Systems and Environment, 8_ (4), 4539–4552. 

- Chere, Z., & Debalke, D. B. (2024). Modeling agricultural drought based on the earth observation-derived standardized precipitation evapotranspiration index and vegetation health index in the northeastern highlands of Ethiopia. _Natural Hazards, 120_ (3), 3127–3151. 

- Daba, M. H., & You, S. (2022). Quantitatively assessing the future land-use/land-cover changes and their driving factors in the upper stream of the Awash River based on the CA–Markov model and their implications for water resources management. _Sustainability, 14_ (3), 1538. 

- Dąbrowska, J., Orellana, A. E. M., Kilian, W., Moryl, A., Cielecka, N., Michałowska, K., ... & Włóka, A. (2023). Between flood and drought: How cities are facing water surplus and scarcity. _Journal of Environmental Management_ , _345_ , 118557. 

- Dagnachew, M., Kebede, A., Moges, A., & Abebe, A. (2020). Effects of climate variability on Normalized Difference Vegetation Index (NDVI) in the Gojeb River Catchment, Omo-Gibe Basin, Ethiopia. _Advances in Meteorology, 2020_ , 1–16. 

- Damtew, A., Teferi, E., & Ongoma, V. (2022). Farmers’ perceptions and spatial statistical modeling of most systematic LULC transitions: Drivers and livelihood implications in Awash Basin, Ethiopia. _Remote Sensing Applications: Society and Environment, 25_ , 100661. 

- Dechasa, A., Aga, A. O., & Dufera, T. (2022). Erosion risk assessment for prioritization of conservation measures in the watershed of Genale Dawa-3 Hydropower Dam, Ethiopia. _Quaternary, 5_ (4), 39. 

- Dejene, I. N., Moisa, M. B., & Gemeda, D. O. (2023). Spatiotemporal monitoring of drought using satellite precipitation products: The case of Borena agro-pastoralists and pastoralists regions, South Ethiopia. _Heliyon, 9_ (3). 

- Derradji, T., Belksier, M. S., Bouznad, I. E., Zebsa, R., Bengusmia, D., & Guastaldi, E. (2023). Spatio-temporal drought monitoring and detection of the areas most vulnerable to drought risk in Mediterranean region, based on remote sensing data (Northeastern Algeria). _Arabian Journal of Geosciences, 16_ (1), 1. 

- Dong, J., Xing, L., Cui, N., Zhao, L., Guo, L., & Gong, D. (2023). Standardized precipitation evapotranspiration index (SPEI) estimated using variant long short-term memory network at four climatic zones of China. _Computers and Electronics in Agriculture, 213_ , 108253. 

- Dwyer, J. L., Roy, D. P., Sauer, B., Jenkerson, C. B., Zhang, H. K., & Lymburner, L. (2018). Analysis ready data: Enabling analysis of the Landsat archive. _Remote Sensing, 10_ (9), 1363. 

- Eisfelder, C., Asam, S., Hirner, A., Reiners, P., Holzwarth, S., Bachmann, M.,  & Kuenzer, C. (2023). Seasonal vegetation trends for Europe over 30 years from a Novel Normalised Difference Vegetation Index (NDVI) timeseries—The TIMELINE NDVI Product. _Remote Sensing_ , _15_ (14), 3616. 

- Elbeltagi, A., Pande, C. B., Kumar, M., Tolche, A. D., Singh, S. K., Kumar, A., & Vishwakarma, D. K. (2023). Prediction of meteorological drought and standardized precipitation index based on the random forest (RF), random tree (RT), and Gaussian process regression (GPR) models. _Environmental Science and Pollution Research, 30_ (15), 43183–43202. 

- Elfadli, Khalid I, and Hamdi A Zurqani. (2022). “Spatiotemporal analysis of Vegetation Health Index (VHI) and drought patterns in Libya based on remote sensing time series.” In _Environmental Applications of Remote Sensing and GIS in Libya_ , Springer, 53–79. 

- Ezzahra, F. F., Ahmed, A., & Abdellah, A. (2023). Variancebased fusion of VCI and TCI for efficient classification of agriculture drought using landsat data in the high atlas (Morocco, North Africa). _Nature Environment and Pollution Technology, 22_ (3), 1421–1429. 

- Fentaw, A. E., Yimer, A. A., & Zeleke, G. A. (2023). Monitoring spatio-temporal drought dynamics using multiple indices in the dry land of the upper Tekeze Basin. _Ethiopia. Environmental Challenges, 13_ , 100781. 

- Fleming-Muñoz, D. A., Whitten, S., & Bonnett, G. D. (2023). The economics of drought: A review of impacts and costs. _Australian Journal of Agricultural and Resource Economics, 67_ (4), 501–523. 

- Gagrani, M., Rainone, C., Yang, Y., Teague, H., Jeon, W., Bondesan, R., & Zappi, P. (2022). Neural topological ordering for computation graphs. _Advances in Neural Information Processing Systems, 35_ , 17327–17339. 

- Gashaw, T., Worqlul, A. W., Lakew, H., Taye, M. T., Seid, A., & Haileslassie, A. (2023). Evaluations of satellite/ reanalysis rainfall and temperature products in the Bale Eco-Region (Southern Ethiopia) to enhance the quality of input data for hydro-climate studies. _Remote Sensing Applications: Society and Environment, 31_ , 100994. 

- Gaur, S., Mittal, A., Bandyopadhyay, A., Holman, I., & Singh, R. (2020). Spatio-temporal analysis of land use and land cover change: A systematic model inter-comparison driven by integrated modelling techniques. _International Journal of Remote Sensing, 41_ (23), 9229–9255. 

- Gayen, A., & Saha, S. (2017). Application of Weights-of-Evidence (WoE) and Evidential Belief Function (EBF) models for the delineation of soil erosion vulnerable zones: A study on Pathro River Basin, Jharkhand, India. _Modeling Earth Systems and Environment, 3_ (3), 1123–1139. 

- Gebrechorkos, S. H., Hülsmann, S., & Bernhofer, C. (2018). Evaluation of multiple climate data sources for managing environmental resources in East Africa. _Hydrology and Earth System Sciences, 22_ (8), 4547–4564. 

- Gelata, F. T., Jiqin, H., Chaka Gemeda, S., & Wubishet Asefa, B. (2023). Application of GIS using NDVI and LST estimation to measure climate variability-induced drought risk assessment in Ethiopia. _Journal of Water and Climate Change, 14_ (7), 2479–2489. 

Vol:. (1234567890) 

Page 23 of 25 **243** 

Environ Monit Assess (2025) 197:243 

- Gemechu, Dejene, Nega Jibat, and Gudina Abashula. (2020). “Livestock banking as innovative response to effects of recurrent drought in pastoralist communities: The case of Borana, Ethiopia.” _ILIRIA International Review_ 10(2). 

- Gidey, E., Dikinya, O., Sebego, R., Segosebe, E., & Zenebe, A. (2018). Analysis of the long-term agricultural drought onset, cessation, duration, frequency, severity and spatial extent using Vegetation Health Index (VHI) in Raya and its environs, Northern Ethiopia. _Environmental Systems Research, 7_ , 1–18. 

- Girma, R., Fürst, C., & Moges, A. (2022). Land use land cover change modeling by integrating artificial neural network with cellular automata-Markov chain model in Gidabo River Basin, Main Ethiopian Rift. _Environmental Challenges, 6_ , 100419. 

- Hammad, A. T., & Falchetta, G. (2022). Probabilistic forecasting of remotely sensed cropland vegetation health and its relevance for food security. _Science of the Total Environment, 838_ , 156157. 

- Holupchinski, E., Álvarez-Berríos, N., Gould, W., & Fain, J. (2020). Drought impacts to crops in the US Caribbean. _Geology, 703_ , 648–5953. 

- Hussien, K., Kebede, A., Mekuriaw, A., Beza, S. A., & Erena, S. H. (2023). Spatiotemporal trends of NDVI and its response to climate variability in the Abbay River Basin, Ethiopia. _Heliyon_ , _9_ (3). 

- International Federation of Red Cross and Red Crescent Societies. 2023. “Drought in the Horn of Africa.” _World Bank_ (July): 1–4. https:// docs. wfp. org/ api/ docum ents/ WFP00001 51188/ downl oad/. 

- Jalayer, S., Sharifi, A., Abbasi-Moghadam, D., Tariq, A., & Qin, S. (2023). Assessment of spatiotemporal characteristic of droughts using in situ and remote sensing-based drought indices. _IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, 16_ , 1483–1502. 

- Kafy, A. A., Bakshi, A., Saha, M., Al Faisal, A., Almulhim, A. I., Rahaman, Z. A., & Mohammad, P. (2023). Assessment and prediction of index based agricultural drought vulnerability using machine learning algorithms. _Science of the Total Environment, 867_ , 161394. 

- Kar, Amal. (2022). “Adaptation of the agri-based society to environmental changes in Thar Desert.” In _Climate Change, Disaster and Adaptations: Contextualising Human Responses to Ecological Change_ , Springer, 151–71. 

- Kasim, O., Agbola, S., & Oweniwe, M. (2020). Land use land cover change and land surface emissivity in Ibadan, Nigeria. _Town and Regional Planning, 77_ , 71–88. 

- Kassahun, N., & Mohamed, M. (2018). Groundwater potential assessment and characterization of Genale-Dawa River Basin. _Open Journal of Modern Hydrology, 8_ (4), 126–144. 

- Kassaye, A. Y., Shao, G., Wang, X., & Shiqing, Wu. (2021). Quantification of drought severity change in Ethiopia during 1952–2017. _Environment, Development and Sustainability, 23_ , 5096–5121. 

- Khan, N., Sachindra, D. A., Shahid, S., Ahmed, K., Shiru, M. S., & Nawaz, N. (2020). Prediction of droughts over Pakistan using machine learning algorithms. _Advances in Water Resources, 139_ , 103562. 

- Kim, S. W., Jung, D., & Choung, Y.-J. (2020). Development of a multiple linear regression model for meteorological 

   - drought index estimation based on landsat satellite imagery. _Water, 12_ (12), 3393. 

- Klutse, N. A. B., Quagraine, K. A., Nkrumah, F., Quagraine, K. T., Berkoh-Oforiwaa, R., Dzrobi, J. F., & Sylla, M. B. (2021). The climatic analysis of summer monsoon extreme precipitation events over West Africa in CMIP6 simulations. _Earth Systems and Environment, 5_ , 25–41. 

- Kogan, Felix. (2023a). “Malaria performance trend during 1981–2020 global warming.” In _Remote Sensing Land Surface Changes: The 1981–2020 Intensive Global Warming_ , Springer, 333–71. 

- Kogan, F. (2023b). _Remote Sensing Land Surface Changes: The 1981–2020 Intensive Global Warming_ . Springer Nature. 

- Korotcov, A., Tkachenko, V., Russo, D. P., & Ekins, S. (2017). Comparison of deep learning with multiple machine learning methods and metrics using diverse drug discovery data sets. _Molecular Pharmaceutics, 14_ (12), 4462–4475. 

- Lin, Q., Wu, Z., Zhang, Y., Peng, T., Chang, W., & Guo, J. (2023). Propagation from meteorological to hydrological drought and its application to drought prediction in the Xijiang River basin, South China. _Journal of Hydrology, 617_ , 128889. 

- Liou, Y.-A., & Mulualem, G. M. (2019). Spatio–temporal assessment of drought in Ethiopia and the impact of recent intense droughts. _Remote Sensing, 11_ (15), 1828. 

- Liu, Y., Shan, F., Yue, H., Wang, X., & Fan, Y. (2023). Global analysis of the correlation and propagation among meteorological, agricultural, surface water, and groundwater droughts. _Journal of Environmental Management, 333_ , 117460. 

- Lubanyana, Andile Njabulo Blessing. (2021). “Mapping drought stress in commercial eucalyptus forest plantations using remotely sensed techniques in Southern Africa.” 

- Lv, H. (2021). Martial arts competitive decision-making algorithm based on improved BP neural network. _Journal of Healthcare Engineering, 2021_ , 1–8. 

- Masek, J. G., Wulder, M. A., Markham, B., McCorkel, J., Crawford, C. J., Storey, J., & Jenstrom, D. T. (2020). Landsat 9: Empowering open science and applications through continuity. _Remote Sensing of Environment, 248_ , 111968. 

- Mengistu, T. D., Feyissa, T. A., Chung, I. M., Chang, S. W., Yesuf, M. B., & Alemayehu, E. (2022). Regional flood frequency analysis for sustainable water resources management of Genale-Dawa River Basin. _Ethiopia. Water, 14_ (4), 637. 

- Mera, G. A. (2018). Drought and its impacts in Ethiopia. _Weather and Climate Extremes, 22_ (June), 24–35. 

- Mirzaee, S., & Nafchi, A. M. (2023). Monitoring spatiotemporal vegetation response to drought using remote sensing data. _Sensors, 23_ (4), 2134. 

- Mohamed, A. A., Ahmed, B., & Palanisamy, K. (2023). Perceptional differences on drought occurrence and resilience building mechanisms in Kebri Dehar District, Somali Region of Ethiopia. _International Journal of Professional Business Review, 8_ (7), 45. 

- Moisa, M. B., Merga, B. B., & Gemeda, D. O. (2022). Multiple indices-based assessment of agricultural drought: A case 

Vol.: (0123456789) 

**243** Page 24 of 25 

Environ Monit Assess (2025) 197:243 

study in Gilgel Gibe Sub-Basin, Southern Ethiopia. _Theoretical and Applied Climatology, 148_ (1–2), 455–464. 

- Mousa, Y. A., Hasan, A. F., & Helmholz, P. (2022). Spatiotemporal analysis of Sawa Lake’s physical parameters between (1985–2020) and drought investigations using landsat imageries. _Remote Sensing, 14_ (8), 1831. 

- Mullapudi, A., Vibhute, A. D., Mali, S., & Patil, C. H. (2023). A review of agricultural drought assessment with remote sensing data: Methods, issues, challenges and opportunities. _Applied Geomatics, 15_ (1), 1–13. 

- Muse, N. M., Tayfur, G., & Safari, M. J. S. (2023). Meteorological drought assessment and trend analysis in Puntland Region of Somalia. _Sustainability, 15_ (13), 10652. 

- Nakalembe, C., Becker-Reshef, I., Bonifacio, R., Hu, G., Humber, M. L., Justice, C. J., & Sanchez, A. (2021). A review of satellite-based global agricultural monitoring systems available for Africa. _Global Food Security, 29_ , 100543. 

- Ndehedehe, C. E., Ferreira, V. G., Adeyeri, O. E., Correa, F. M., Usman, M., Oussou, F. E., & Dewan, A. (2023). Global assessment of drought characteristics in the Anthropocene. _Resources, Environment and Sustainability, 12_ , 100105. 

- Negewo, T. F., & Sarma, A. K. (2021). Estimation of water yield under baseline and future climate change scenarios in Genale Watershed, Genale Dawa River Basin, Ethiopia, using SWAT model. _Journal of Hydrologic Engineering, 26_ (3), 5020051. 

- Neinavaz, E., Skidmore, A. K., & Darvishzadeh, R. (2020). Effects of prediction accuracy of the proportion of vegetation cover on land surface emissivity and temperature using the NDVI threshold method. _International Journal of Applied Earth Observation and Geoinformation, 85_ , 101984. 

- Niway, W. F., Molla, D. D., & Lohani, T. K. (2022). Holistic approach of GIS based Multi-Criteria Decision Analysis (MCDA) and WetSpass models to evaluate groundwater potential in Gelana Watershed of Ethiopia. _Journal of Groundwater Science and Engineering, 10_ (2), 138–152. 

- Orke, Y. A., & Li, M.-H. (2022). Impact of climate change on hydrometeorology and droughts in the Bilate Watershed, Ethiopia. _Water, 14_ (5), 729. 

- Pahlevanzadeh, N., Janalipour, M., Teharni, N. A., & Farhanj, F. (2019). Accuracy improvement of land surface temperature extracted from thermal bands of landsat satellite using linear regression and ground observations. _Geography and Environmental Planning, 30_ (3), 59–78. 

- Pan, Y., Zhu, Y., Lü, H., Yagci, A. L., Fu, X., Liu, E., & Liu, R. (2023). Accuracy of agricultural drought indices and analysis of agricultural drought characteristics in China between 2000 and 2019. _Agricultural Water Management, 283_ , 108305. 

- Pham, H. T., Awange, J., Kuhn, M., Nguyen, B. V., & Bui, L. K. (2022). Enhancing crop yield prediction utilizing machine learning on satellite-based vegetation health indices. _Sensors, 22_ (3), 719. 

- Priya, M. V., Kalpana, R., Pazhanivelan, S., Kumaraperumal, R., Ragunath, K. P., Vanitha, G., & Vasumathi, V. (2023). Monitoring vegetation dynamics using multitemporal Normalized Difference Vegetation Index (NDVI) and Enhanced Vegetation Index (EVI) images of Tamil Nadu. _Journal of Applied and Natural Science, 15_ (3), 1170–1177. 

- Qi, Y., Dou, H., & Wang, Z. (2022). An adaptive threshold selected method from remote sensing image based on water index. In Journal of Physics: Conference Series (Vol. 2228, No. 1, p. 012001). IOP Publishing. 

- Raihan, A. (2023). A review of the global climate change impacts, adaptation strategies, and mitigation options in the socio-economic and environmental sectors. _Journal of Environmental Science and Economics, 2_ (3), 36–58. 

- Rasheed, M. W., Tang, J., Sarwar, A., Shah, S., Saddique, N., Khan, M. U., & Sultan, M. (2022). Soil moisture measuring techniques and factors affecting the moisture dynamics: A comprehensive review. _Sustainability, 14_ (18), 11538. 

- Ren, J., Yang, J., Wu, F., Sun, W., Xiao, X., & Xia, J. C. (2023). Regional thermal environment changes: Integration of satellite data and land use/land cover. _Iscience_ , _26_ (2). 

- Rezvani, R., Na, W., & Najafi, M. R. (2023). Lagged compound dry and wet spells in Northwest North America under 1.5° C–4° C global warming levels. _Atmospheric Research, 290_ , 106799. 

- Senhorelo, A. P., Sousa, E. F. D., Santos, A. R. D., Ferrari, J. L., Peluzio, J. B. E., Zanetti, S. S., & Dias, H. M. (2023). Application of the Vegetation Condition Index in the Diagnosis of Spatiotemporal Distribution of Agricultural Droughts: A Case Study Concerning the State of Espírito Santo. _Southeastern Brazil. Diversity, 15_ (3), 460. 

- Shawul, A. A., & Chakma, S. (2019). Spatiotemporal detection of land use/land cover change in the large basin using integrated approaches of remote sensing and GIS in the Upper Awash Basin, Ethiopia. _Environmental Earth Sciences, 78_ (5), 141. 

- Shi, Y., Zhao, L., Zhao, X., Lan, H., & Teng, H. (2022). The integrated impact of drought on crop yield and farmers’ livelihood in semi-arid rural areas in China. _Land, 11_ (12), 2260. 

- Shibru, M., Opere, A., Omondi, P., & Gichaba, M. (2023). Understanding physical climate risks and their implication for community adaptation in the Borana Zone of Southern Ethiopia using mixed-methods research. _Scientific Reports, 13_ (1), 6916. 

- Sishah, S., Abrahem, T., Azene, G., Dessalew, A., & Hundera, H. (2023). Downscaling and validating SMAP soil moisture using a machine learning algorithm over the Awash River basin. _Ethiopia. Plos One, 18_ (1), e0279895. 

- Stojanovic, M., Mulualem, G. M., Sori, R., Vazquez, M., Nieto, R., & Gimeno, L. (2022). Precipitation moisture sources of Ethiopian River Basins and their role during drought conditions. _Frontiers in Earth Science, 10_ , 929497. 

- Sun, P., Liu, R., Yao, R., Shen, H., & Bian, Y. (2023). Responses of agricultural drought to meteorological drought under different climatic zones and vegetation types. _Journal of Hydrology, 619_ , 129305. 

- Tahir, M., Naeem, A., Malik, H., Tanveer, J., Naqvi, R. A., & Lee, S. W. (2023). DSCC_Net: Multi-classification deep learning models for diagnosing of skin cancer using dermoscopic images. _Cancers, 15_ (7), 2179. 

- Takele, A., Lakew, H. B., & Kabite, G. (2022). Does the recent afforestation program in Ethiopia influenced vegetation cover and hydrology? A case study in the upper awash basin, Ethiopia. _Heliyon, 8_ (6). 

- Talisuna, A. O., Okiro, E. A., Yahaya, A. A., Stephen, M., Bonkoungou, B., Musa, E. O., & Fall, I. S. (2020). 

Vol:. (1234567890) 

Page 25 of 25 **243** 

Environ Monit Assess (2025) 197:243 

Spatial and temporal distribution of infectious disease epidemics, disasters and other potential public health emergencies in the World Health Organisation Africa region, 2016–2018. _Globalization and health, 16_ , 1–12. 

- Taylor, S., Wright, J. B., Forrest, E. C., Jared, B., Koepke, J., & Beaman, J. (2020). Investigating relationship between surface topography and emissivity of metallic additively manufactured parts. _International Communications in Heat and Mass Transfer, 115_ , 104614. 

- Tessema, Y. M., Jasińska, J., Yadeta, L. T., Świtoniak, M., Puchałka, R., & Gebregeorgis, E. G. (2020). Soil loss estimation for conservation planning in the welmel watershed of the Genale Dawa Basin. _Ethiopia. Agronomy, 10_ (6), 777. 

- Thornton, P., Nelson, G., Mayberry, D., & Herrero, M. (2022). Impacts of heat stress on global cattle production during the 21st century: A modelling study. _The Lancet Planetary Health, 6_ (3), e192–201. 

- van Ginkel, M., & Biradar, C. (2021). Drought early warning in agri-food systems. _Climate, 9_ (9), 134. 

- Venugopalan, J., Tong, Li., Hassanzadeh, H. R., & Wang, M. D. (2021). Multimodal deep learning models for early detection of Alzheimer’s disease stage. _Scientific Reports, 11_ (1), 3254. 

- Wang, Z., Yang, Y., Zhang, C., Guo, H., & Hou, Y. (2022). Historical and future Palmer Drought Severity Index with improved hydrological modeling. _Journal of Hydrology, 610_ , 127941. 

- Winter, De., Joost, C. F., Gosling, S. D., & Potter, J. (2016). Comparing the Pearson and Spearman correlation coefficients across distributions and sample sizes: A tutorial using simulations and empirical data. _Psychological Methods, 21_ (3), 273. 

- Worku, M. A., Feyisa, G. L., Beketie, K. T., & Garbolino, E. (2022). Rainfall variability and trends in the Borana Zone of Southern Ethiopia. _Journal of Water and Climate Change, 13_ (8), 3132–3151. 

- World Bank. (2020). “Challenges and opportunities for water in development in the lowlands of Ethiopia.” : 24. https:// docum ents1. world bank. org/ curat ed/ ar/ 88754 15927 63258 049/ pdf/ Chall enges- and- Oppor tunit ies- forWater- in- Devel opment- in- the- Lowla nds- of- Ethio pia. pdf. Accessed 15 Dec 2024 

- World Health Organization. (2023). “Tracking universal health coverage: 2023 global monitoring report.” 

- Wright, A., Shill, J., Honey, N., Jorm, A. F., & Bolam, B. (2020). The VicHealth Indicators population survey: 

Methodology, prevalence of behavioural risk factors, and use in local policy. _BMC Public Health, 20_ , 1–21. 

- Xu, M., Yao, N., Hu, A., de Goncalves, L. G. G., Mantovani, F. A., Horton, R., & Liu, G. (2022). Evaluating a new temperature-vegetation-shortwave infrared reflectance dryness index (TVSDI) in the continental United States. _Journal of Hydrology, 610_ , 127785. 

- Yadeta, D., Kebede, A., & Tessema, N. (2020). Climate change posed agricultural drought and potential of rainy season for effective agricultural water management, Kesem SubBasin, Awash Basin, Ethiopia. _Theoretical and Applied Climatology, 140_ , 653–666. 

- Yin, J., Zhan, X., Barlage, M., Kumar, S., Fox, A., Albergel, C., & Liu, J. (2023). Assimilation of Blended Satellite Soil Moisture Data Products to Further Improve NoahMP Model Skills. _Journal of Hydrology, 621_ , 129596. 

- Zeng, J., Zhou, T., Qu, Y., Bento, V. A., Qi, J., Xu, Y., & Wang, Q. (2023). An improved global vegetation health index dataset in detecting vegetation drought. _Scientific Data, 10_ (1), 338. 

- Zewdu, D. (2020). The impacts of climate variability on livestock resources and pastoralist adaptation responses in Dollo Ado Woreda, Ethio-Somali National Regional State. _Journal of Environmental and Agricultural Studies, 1_ (2), 10–18. 

- Zhao, X., Xia, H., Liu, B., & Jiao, W. (2022). Spatiotemporal comparison of drought in Shaanxi–Gansu–Ningxia from 2003 to 2020 using various drought indices in Google Earth Engine. _Remote Sensing, 14_ (7), 1570. 

- Zhou, Z., Tu, X., Wang, T., Singh, V. P., Chen, X., & Lin, K. (2023). Bivariate socioeconomic drought assessment based on a hybrid framework and impact of human activities. _Journal of Cleaner Production, 409_ , 137150. 

- Zhu, C., Li, S., Hagan, D. F. T., Wei, X., Feng, D., Lu, J., & Wang, G. (2023). Long-Term Characteristics of Surface Soil Moisture over the Tibetan Plateau and Its Response to Climate Change. _Remote Sensing, 15_ (18), 4414. 

**Publisher’s note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law. 

Vol.: (0123456789) 

Reproduced with permission of copyright owner. Further reproduction prohibited without permission. 

