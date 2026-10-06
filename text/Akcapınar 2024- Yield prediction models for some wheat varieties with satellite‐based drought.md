Received: 23 January 2024 

Revised: 6 May 2024 Accepted: 14 May 2024 

DOI: 10.1002/ird.2989 



#### R E S E A R C H A R T I C L E 

# Yield prediction models for some wheat varieties with satellite-based drought indices and machine learning algorithms 

## Muhammed Cem Akcapınar<sup>1</sup> | Belgin Çakmak<sup>2</sup> 

1Turkish State Meteorological Service Department of Climate and Agricultural Meteorology, Türkiye 

2Ankara University Department of Agricultural Structures and Irrigation, Türkiye 

##### Correspondence 

Muhammed Cem Akcapınar, Turkish State Meteorological Service Department of Climate and Agricultural Meteorology, Türkiye. 

Email: cemakcapinar@gmail.com 

### Abstract 

In recent years, frequent drought events in Konya, one of Türkiye's most important cereal production centres, have led to increased pressure on water and soil resources, resulting in yield losses, particularly in wheat production. Alternative yield prediction models, especially those that play a crucial role in agricultural import–export planning in the region, are important for economic contributions and the development of early warning systems. In this context, the aim of this study is to develop models that can be used in the yield prediction of wheat varieties widely grown in the Konya Altınova region. Agricultural drought indices obtained from Normalized Difference Vegetation Index (NDVI) and land surface temperature (LST) products of the Terra Moderate Resolution Imaging Spectroradiometer (MODIS) satellite were used to obtain model inputs. These indices are the Vegetation Condition Index (VCI), Temperature Condition Index (TCI), Vegetation Health Index (VHI) and Vegetation Supply Water Index (VSWI). In obtaining the input parameters for the models, the growth periods of the varieties in the region were also considered. Using various machine learning algorithms, 21 yield prediction models for Bayraktar-2000, 12 for Kızıltan-91 and 8 for Bezostaya-1 were presented as alternatives, with model performances (coefficient of determination, R<sup>2</sup> ) ranging between 0.74 and 0.97, 0.73 and 0.96, and 0.69 and 0.87, respectively. 

K E Y W O R D S 

drought, machine learning, satellite-based indices, wheat, yield prediction 

### Résumé 

À Konya, l'un des plus importants centres de production céréalière de Turquie, les épisodes de sécheresse, fréquents ces dernières années, ont accru la pression sur les ressources en eau et en sol et entraîné des pertes de rendement des 

Article title in French: Modèles de la prédiction du rendement de quelques variétés de blé à l'aide d'indices de sécheresse satellitaires et d'algorithmes d'apprentissage automatique. 

> This is an open access article under the terms of the Creative Commons Attribution-NonCommercial-NoDerivs License, which permits use and distribution in any medium, provided the original work is properly cited, the use is non-commercial and no modifications or adaptations are made. 

> © 2024 The Author(s). Irrigation and Drainage published by John Wiley & Sons Ltd on behalf of International Commission for Irrigation and Drainage. 

wileyonlinelibrary.com/journal/ird 

Irrig. and Drain. 2025;74:237–250. 

237 

AKCAPINAR and ÇAKMAK 

238 

cultures, en particulier du blé. Les modèles alternatifs de prévision des rendements, qui jouent un rôle important notamment dans la planification des importations et exportations agricoles dans la région, sont importants en termes de contribution économique et de développement de systèmes d'alerte précoce. Dans ce contexte, l'objectif de cette étude était de développer des modèles qui peuvent être utilisés dans la prédiction du rendement des variétés de blé communes dans la région d'Altınova de la province de Konya en utilisant les indices de sécheresse agricole Vegetation Condition Index (VCI), Temperature Condition Index (TCI), Vegetation Health Index (VHI), and Vegetation Supply Water Index (VSWI) obtenus à partir des produits Normalized Difference Vegetation Index (NDVI) et Land Surface Temperature (LST) du satellite Terra MODIS (Moderate Resolution Imaging Spectroradiometer). Lors de l'obtention des paramètres d'entrée du modèle, les périodes de croissance des variétés dans la région ont également été prises en considération. À l'issue de l'étude, 21 modèles de prévision du rendement pour Bayraktar-2000, 12 pour Kızıltan-91 et 8 pour Bezostaya-1 ont été présentés comme des alternatives avec des performances de modèle (R<sup>2</sup> ) comprises entre 0,736-0,973, 0,733–0,956 et 0,686-0,874, respectivement. 

M O T S C L É S 

Blé, sécheresse, prévision du rendement, indices satellitaires, apprentissage automatique 

## 1 | INTRODUCTION 

Drought, which is a factor that pressures natural resources, especially soil and water, in agriculture due to climate change, is becoming more common in Türkiye and throughout the world every year. Inadequate production due to severe drought events, especially in aridand semi-arid climate zone countries, disrupts the global supply chain and the food supply–demand balance. Therefore, the development of yield forecasting models to guide agricultural import–export planning is important in terms of providing economic contributions and developing early warning systems. 

Türkiye has very different climate types and microclimate areas due to its geographical location. Accordingly, irregularities in the distribution of precipitation cause water stress and drought in many regions. In Türkiye, the lowest average annual precipitation is observed around Tuz Lake, including the Altınova region of Konya, and the highest average annual precipitation is observed in the eastern Black Sea region (around Hopa) (MGM, 2021). There is a need to develop alternative forecasting models to aid in production planning in this region, which is one of the leading centres of cereal agriculture in Türkiye. 

Currently, many modelling studies on drought yield have been conducted. The effects of the Vegetation Condition Index (VCI) and Temperature Condition Index (TCI), 

which are the main satellite-based agricultural drought indices, on crop yields according to growing season averages have been investigated, and it has been determined that there are very strong relationships at critical stages (Kogan, 1997). The Normalized Difference Vegetation Index (NDVI) and land surface temperature (LST), which form the basis of many agricultural drought indices, were found to be negatively correlated in July and August, and it was revealed that the main factor limiting the growth of vegetation was water (Kloos et al., 2021). With the emergence of the concept of artificial intelligence, there has been a trend towards this direction in statistics-based studies. Today, various platforms enable these studies to be carried out. One of these platforms, WEKA (Waikato Environment for Knowledge Analysis), is used for many functions, such as data mining, clustering, classification and visualization (Aher & Lobo, 2011). In the MultilayerPerceptron algorithm in WEKA, which contains many algorithms, 75% accuracy was achieved in wheat yield estimation with 25 hidden layers and a 0.3 learning rate (Ejaz & Abbasi, 2020). Multilayer perceptrons are especially useful when a clear theoretical model cannot be established or when working with nonlinear models (Gardner & Dorling, 1998). Climatological studies based on remote sensing can sometimes encounter various difficulties. ClimateEngine is a web (https://app. climateengine.org/climateEngine) application developed to assist climatological studies (Huntington et al., 2017). 

AKCAPINAR and ÇAKMAK 

239 

In this study, the aim was to investigate the relationship between drought and yield in wheat by considering the growth stages of the crop and to develop variety-based yield prediction models with machine learning algorithms. 

## 2 | MATERIALS AND METHODS 

## 2.1 | Material 

## 2.1.1 | Study area and wheat plots 

The research area was the Altınova Agricultural Enterprise located in the northern Kadınhanı District of Konya Province. According to the Turkish State Meteorological 

Service (TSMS) data for the period 1929–2021, the average annual precipitation in Konya Province was 331.8 mm and the highest temperature was 40.6<sup>�</sup> C, recorded in July. The lowest temperature was �28.2<sup>�</sup> C, recorded in January (Figure 1) (MGM, 2022). 

This study was carried out in 12 wheat plots where the Kızıltan-91, Bayraktar-2000 and Bezostaya-1 varieties were planted between 2001 and 2020. The plots, which were scanned and marked in the same way, were divided into two sections, namely, the South (S) and North (N) sections, and rotational planting was carried out (Figure 2). In the rest of the study, the names of the varieties are used as Kızıltan, Bayraktar and Bezostaya. 

Bezostaya was planted between 2001 and 2008, followed by the Bayraktar or Kızıltan varieties. It was 



FIGURE 1 Konya Province 1929–2021 average climate parameters. Ave., average; D., duration; Mon., monthly; Prcp., precipitation; Suns., sunshine; T., total; Temp., temperature. 



FIGURE 2 Study area (Altınova Agricultural Enterprise). 

AKCAPINAR and ÇAKMAK 

240 

determined that the Kızıltan variety was planted throughout the 2001–2020 period, predominantly after 2008 (Table 1). 

In this study, plot-based wheat yield data from the Altınova Agricultural Enterprise for the period 2001– 2020, obtained from the Directorate General of Agricultural Enterprises (TIGEM), were<sup>_</sup> used as crop production data (TIGEM,<sup>_</sup> 2020). No different agricultural techniques were used on the plots of the enterprise. However, there may have been differences in practices over the years, depending on changing technologies and needs. 

## 2.1.2 | Satellite images and climate data 

In this study, NDVI and LST images were obtained from the MOD13Q1 and MOD11A1 datasets provided by the United States Geological Survey (USGS) through the ClimateEngine application (Huntington et al., 2017). Moderate Resolution Imaging Spectroradiometer (MODIS) MOD13Q1 data have a spatial resolution of 250 m, a temporal resolution of 16 days and a scale factor of 0.0001 (Didan et al., 2015). The MOD11A1 data, which provide the LST, have a spatial resolution of 1 km and a temporal resolution of 8 days. The temperature is presented in Kelvin (<sup>�</sup> K) (�273.15 for<sup>�</sup> C conversion), and the scale factor of the product is 0.02 (Wan, 2013). Due to the different spatial resolutions of the LST images, resampling was performed. 

The NDVI and LST images covering the study area were downloaded for the 20-year production period 

between the 2000–2001 and 2019–2020 agricultural seasons, from September, the earliest period of planting in the region, to July, the latest period of harvest. To cover the close periods together, the images were downloaded for each month and divided into two periods, 1_15 (between the 1st and 15th of the month) and 16_30 (between the 16th and 30th of the month). A total of �880 images (20 years, 11 months, 2 weeks) were used. North and South polygons were created for all plots so that only the cultivated area was processed. 

The ERA5 dataset was used for the daily meteorological data required for the growth degree day (GDD) calculations. The ERA5 dataset is the latest climate reanalysis product with a 0.25<sup>�</sup> x 0.25<sup>�</sup> resolution obtained by the European Centre for Medium-Range Weather Forecasts (ECMWF) by combining model and ground observations (Hersbach et al., 2018). 

The ERA5 dataset is available as open access on the official website (https://cds.climate.copernicus.eu/# !/search?text=ERA5&type=dataset). The latitude (38.7191) and longitude (32.1750) of the TSMS Kadınhanı Altınova TIGEM<sup>_</sup> (17744) Automatic Weather Station (AWS) were taken as references. 

## 2.2 | Method 

## 2.2.1 | Satellite-based drought indices 

The NDVI assesses vegetation by measuring the difference between the near-infrared (NIR) light reflected by vegetation and the red light absorbed (RED) (Equation 1): 

TABLE 1 Sowing periods of wheat varieties in plots. 

||Kızıltan||Bayrak|tar|Bezosta|ya|
|---|---|---|---|---|---|---|
|No|2001–<br>2008|2009–<br>2020|2001–<br>2008|2009–<br>2020|2001–<br>2008|2009–<br>2020|
|1|*|*|||||
|2|*|*|||||
|3|*|*|||||
|4||||*|||
|5||*|||*||
|6||*|||*||
|7||*|||*||
|8||||*|*||
|9||||*|*||
|10||||*|*||
|11||||*|*||
|12||||*|*||



*: Cultivation. 



The VCI focuses on the effects of drought on vegetation and can provide information on the onset, duration and severity of drought by comparing them historically (Svoboda & Fuchs, 2016). The VCI compares the current NDVI value with the range of values observed during the same period in previous years and is expressed as a percentage (%) (Equation 2): 



where NDVI j is the current year's NDVI value, NDVI max is the long-term maximum NDVI value, and NDVI min is the long-term minimum NDVI value. In some cases, the VCI alone is not sufficient for accurate drought analysis. Therefore, the need for information on thermal 

AKCAPINAR and ÇAKMAK 

241 

conditions was considered, and as a result, the TCI emerged (Equation 3) (Kogan, 1995). 

GDD values were calculated with Equation (6) (Do�gan & Karabulut, 2022). 





where LST is the land surface temperature of the current month or year, LST max is the maximum land surface temperature, and LST min is the minimum land surface temperature (Equation 3). 

The Vegetation Health Index (VHI) can be defined as a combined index of the NDVI and LST that can assess drought based on vegetation stress (Masitoh & Rusydi, 2019). The VHI is calculated using Equation (4): 



When the Vegetation Supply Water Index (VSWI) is too low, the transpiration rate of vegetation decreases and drought occurs. The smaller the VSWI value calculated according to Equation (5), the more severe the drought in that region (Arslan et al., 2016): 

where Tmin is the daily minimum temperature, Tmax is the daily maximum temperature, and Tthreshold is the threshold temperature. In total, the highest GDD values were observed for the Bayraktar variety, while the average GDD values required from sowing to harvest maturity for the studied wheat varieties varied between 2100 and 2300<sup>�</sup> C. The phenological periods studied were abbreviated as sowing ‘S’, emergence ‘E’, tillering ‘T’, stalk emergence ‘SE’, spiking ‘Sp’, flowering ‘F’, ripening ‘R’ and harvest maturity ‘H’ (Table 2). 

The dates of the growth periods were determined according to the GDD values. The index values representing the growth periods were calculated by averaging the monthly index values between these dates. 

## 2.2.3 | Yield prediction model 



## 2.2.2 | Determining phenological stages 

In determining phenological periods, due to the absence of phenological observation records at the TSMS Kadınhanı Altınova TIGEM AWS, the phenological observation<sup>_</sup> records of the nearest TSMS Yunak station (1995–2009 period) were used as a reference. First, the average GDD values of the phenological periods were calculated, and then the phenological periods were determined by proportioning these values to the sowing–harvest dates of the enterprise. For wheat, the base temperature was 0<sup>�</sup> C, the ceiling temperature was 30<sup>�</sup> C (threshold value), and 

WEKA, which was used to build the prediction models, is an open-source software and is a collection of machine learning algorithms that includes tools such as data preparation, classification, regression, clustering and visualization (Frank et al., 2016). The algorithms used and the groups to which they belong are shown with the names used in WEKA (Table 3). 

In the modelling, the yields of the Bayraktar, Kızıltan and Bezostaya cultivars were used as dependent variables (output), and satellite-based indices (NDVI, LST, VHI and VSWI) and periodic/cumulative growth period lengths (Gp/acGp) were used as independent variables (Table 4). 

Model variables are defined as combinations of these parameters. If more than one period is to be modelled together, ‘-’ is placed between the beginning and end of 

TABLE 2 GDD values of wheat varieties according to growth period (<sup>�</sup> C). 

|Variety|GDD|S–E|E–T|T–SE|SE–Sp|Sp–F|F–R|R–H|PGDD|
|---|---|---|---|---|---|---|---|---|---|
|Kızıltan|Periodic|250.4|572.5|192.7|253.9|292.1|321.8|296.7|2180.1|
||Cumulative|250.4|823.0|1015.6|1269.5|1561.6|1883.5|2180.1|-|
|Bayraktar|Periodic|265.0|605.7|203.8|268.6|308.9|340.5|313.9|2306.5|
||Cumulative|265.0|870.7|1074.5|1343.1|1652.1|1992.6|2306.5|-|
|Bezostaya|Periodic|241.3|551.6|185.6|244.6|281.3|310.1|285.9|2100.3|
||Cumulative|241.3|792.9|978.5|1223.1|1504.4|1814.4|2100.3|-|



Abbreviations: E–T, emergence to tillering; F–R, flowering to ripening; GDD, growth degree day; R, ripening to harvest maturity; S–E, sowing to emergence; SE–Sp, stalk emergence to spiking; Sp–F, spiking to flowering; T–SE, tillering to stalk emergence. 

AKCAPINAR and ÇAKMAK 

242 

the variables, and if different indices are to be modelled together, the variable phrases are separated by commas (,). For example, ‘N0-N3, L0-L3’ indicates that the NDVI and LST values from emergence to spiking are modelled together. In this case, the total number of independent variables is eight. In the modelling, VCI and TCI are not considered variables since they are normalized from the NDVI and LST. More than 3,000 alternative modelling experiments were performed with satellite-based indices by growth period and month, individually (e.g. ‘VH4, Y’), additively (e.g. ‘VH_My_I, VH_May_II, Y’), with each other (e.g. ‘N2, L2, Y’) and combined with growth period lengths (e.g. ‘N0-N5, acGp0-acGp5, Y’). The machine 

TABLE 3 Algorithms used for models. 

|Group|Algorithms|
|---|---|
|Functions|LinearRegression|
||MultilayerPerceptron|
|Lazy|IBk|
||KStar|
||LWL|
|Meta|Bagging|
|Rules|DecisionTable|
||M5Rules|
|Trees|M5P|
||RandomForest|
||RandomTree|
||REPTree|



learning algorithms described above were applied for all combinations of variables, with training sets set at 70%, 75% and 80% and with modifications to the algorithms' specific options. 

As a result, 21 models were determined for the Bayraktar variety, 12 models for the Kızıltan variety and 8 models for the Bezostaya variety. The variables and performance criteria used in the construction of the models are presented in Section 3. In selecting the models, the highest model performance (high coefficient of determination, R<sup>2</sup> , also known as R-squared) was achieved by using as few variables as possible at the earliest possible period. The criterion of R<sup>2</sup> ≥ 0.70 was accepted for the recommended models for all varieties except Model 8 for the Bezostaya variety. The Bezostaya Model 8 was included because it had an R<sup>2</sup> of 0.69 with a single variable (Table 5). 

## 2.2.4 | Model performance assessment 

The various performance measures described below were used to evaluate the success of the models. 

The correlation coefficient (r) is a statistical measure of the strength of a linear relationship between two variables and has values ranging from �1 to 1. A correlation coefficient equal to �1 indicates a perfect negative relationship, while a correlation coefficient equal to 1 indicates a perfect positive relationship, while a correlation coefficient equal to 0 means that there is no linear relationship. The correlation between two variables (x and y) is calculated by Equation (7): 

TABLE 4 Parameters and symbols for model variables. 

|No.|Parameters|Symbol|No.|Parameters|Symbol|
|---|---|---|---|---|---|
|1|NDVI|N|14|Ripening–harvest maturity (R–H)|6|
|2|LST|L|15|September|Se|
|3|VHI|VH|16|October|Oc|
|4|VSWI|Vs|17|November|Nv|
|5|Yield (kg/da)|Y|18|December|Dc|
|6|Growth period lengths (day)|Gp|19|January|Jn|
|7|Cumulative growth period lengths (day)|acGp|20|February|Fb|
|8|Sowing–emergence (S–E)|0|21|March|Mr|
|9|Emergence–tillering (E–T)|1|22|April|Ap|
|10|Tillering–stalk emergence (T–SE)|2|23|May|My|
|11|Stalk emergence–spiking (SE–Sp)|3|24|June|Jn|
|12|Spiking–flowering (Sp–F)|4|25|Period 1–15 of month|I|
|13|Flowering–ripening (F–R)|5|26|Period 16–31 of month|II|



Abbreviations: LST, Land Surface Temperature; NDVI, Normalized Difference Vegetation Index; VHI, Vegetation Health Index; VSWI, Vegetation Supply Water Index. 

AKCAPINAR and ÇAKMAK 

243 

TABLE 5 Designs of yield prediction models for wheat varieties. 

|Variety|Model<br>no.|Training|Algorithms|Classifier|
|---|---|---|---|---|
|B A Y R A K T A R|1|80.00%|Bagging -P 100 -S 1 -num-slots 1 -I 10 -W|RandomTree -K 0 -M 1.0 -V 0.001 -S 1|
||2|80.00%|Bagging -P 100 -S 1 -num-slots 1 -I 10 -W|RandomForest -P 100 -I 100 -num-slots 1 -K 0 -M<br>1.0 -V 0.001 -S 1|
||3|80.00%|Bagging -P 100 -S 1 -num-slots 1 -I 10 -W|RandomTree -K 0 -M 1.0 -V 0.001 -S 1|
||4|80.00%|Bagging -P 100 -S 1 -num-slots 1 -I 10 -W|M5P -M 4.0 -num-decimal-places 4|
||5|80.00%|Bagging -P 100 -S 1 -num-slots 1 -I 10 -W|RandomTree -K 0 -M 1.0 -V 0.001 -S 1|
||6|75.00%|Bagging -P 100 -S 1 -num-slots 1 -I 10 -W|REPTree -M 2 -V 0.001 -N 3 -S 1 -L�1 -I 0.0|
||7|80.00%|Bagging -P 100 -S 1 -num-slots 1 -I 10 -W|RandomForest -P 100 -I 100 -num-slots 1 -K 0 -M<br>1.0 -V 0.001 -S 1|
||8|75.00%|Bagging -P 100 -S 1 -num-slots 1 -I 10 -W|REPTree -M 2 -V 0.001 -N 3 -S 1 -L�1 -I 0.0|
||9|80.00%|Bagging -P 100 -S 1 -num-slots 1 -I 10 -W|RandomForest -P 100 -I 100 -num-slots 1 -K 0 -M<br>1.0 -V 0.001 -S 1|
||10|80.00%|MultilayerPerceptron -L 0.3 -M 0.2 -N 500 -V 0 -S 0<br>-E 20 -H a||
||11|80.00%|Bagging -P 100 -S 1 -num-slots 1 -I 10 -W|REPTree -M 2 -V 0.001 -N 3 -S 1 -L�1 -I 0.0|
||12|80.00%|Bagging -P 100 -S 1 -num-slots 1 -I 10 -W|M5P -M 4.0 -num-decimal-places 4|
||13|80.00%|MultilayerPerceptron -L 0.3 -M 0.2 -N 500 -V 0 -S 0<br>-E 20 -H a||
||14|75.00%|Bagging -P 100 -S 1 -num-slots 1 -I 10 -W|RandomForest -P 100 -I 100 -num-slots 1 -K 0 -M<br>1.0 -V 0.001 -S 1|
||15|75.00%|Bagging -P 100 -S 1 -num-slots 1 -I 10 -W|REPTree -M 2 -V 0.001 -N 3 -S 1 -L�1 -I 0.0|
||16|80.00%|Bagging -P 100 -S 1 -num-slots 1 -I 10 -W|REPTree -M 2 -V 0.001 -N 3 -S 1 -L�1 -I 0.0|
||17|80.00%|Bagging -P 100 -S 1 -num-slots 1 -I 10 -W|RandomForest -P 100 -I 100 -num-slots 1 -K 0 -M<br>1.0 -V 0.001 -S 1|
||18|80.00%|Bagging -P 100 -S 1 -num-slots 1 -I 10 -W|RandomForest -P 100 -I 100 -num-slots 1 -K 0 -M<br>1.0 -V 0.001 -S 1|
||19|70.00%|Bagging -P 100 -S 1 -num-slots 1 -I 10 -W|RandomForest -P 100 -I 100 -num-slots 1 -K 0 -M<br>1.0 -V 0.001 -S 1|
||20|80.00%|Bagging -P 100 -S 1 -num-slots 1 -I 10 -W|RandomTree -K 0 -M 1.0 -V 0.001 -S 1|
||21|70.00%|Bagging -P 100 -S 1 -num-slots 1 -I 10 -W|RandomForest -P 100 -I 10 -num-slots 3 -K 0 -M<br>1.0 -V 0.001 -S 1|
|K I Z I L T A N|1|80.00%|Bagging -P 100 -S 1 -num-slots 1 -I 100 -W|M5P -M 4.0 -num-decimal-places 4|
||2|80.00%|lazy. IBk -K 1 -W 0 -A||
||3|80.00%|Bagging -P 100 -S 1 -num-slots 1 -I 10 -W|REPTree -M 2 -V 0.001 -N 3 -S 1 -L�1 -I 0.0|
||4|80.00%|lazy. KStar -B 20 -M a||
||5|75.00%|lazy. IBk -K 1 -W 0 -A||
||6|70.00%|lazy. IBk -K 1 -W 0 -A||
||7|80.00%|MultilayerPerceptron -L 0.3 -M 0.2 -N 450 -V 0 -S 0<br>-E 20 -H“3, 6”||
||8|80.00%|MultilayerPerceptron -L 0.2 -M 0.1 -N 300 -V 0 -S 0<br>-E 20 -H 2||
||9|80.00%|Bagging -P 100 -S 1 -num-slots 1 -I 20 -W|M5P -M 4.0 -num-decimal-places 4|
||10|80.00%|Bagging -P 100 -S 1 -num-slots 1 -I 10 -W|REPTree -M 2 -V 0.001 -N 3 -S 1 -L�1 -I 0.0|
||11|70.00%|lazy. KStar -B 20 -M a||
||12|80.00%|MultilayerPerceptron -L 0.3 -M 0.2 -N 500 -V 0 -S 0<br>-E 20 -H“2, 2”||



(Continues) 

AKCAPINAR and ÇAKMAK 

244 

TABLE 5 (Continued) 

||Model||||
|---|---|---|---|---|
|Variety|no.|Training|Algorithms|Classifier|
|B E Z O S T A Y A|1|80.00%|MultilayerPerceptron -L 0.3 -M 0.2 -N 400 -V 0 -S 0<br>-E 20 -H 100||
||2|80.00%|Bagging -P 100 -S 1 -num-slots 1 -I 100 -W|RandomForest -P 100 -I 100 -num-slots 1 -K 0 -M<br>1.0 -V 0.001 -S 1|
||3|80.00%|Bagging -P 100 -S 1 -num-slots 1 -I 10 -W|RandomForest -P 100 -I 100 -num-slots 1 -K 0 -M<br>1.0 -V 0.001 -S 1|
||4|80.00%|MultilayerPerceptron -L 0.2 -M 0.2 -N 350 -V 0 -S 0<br>-E 20 -H 100||
||5|80.00%|Bagging -P 100 -S 1 -num-slots 1 -I 10 -W|trees. RandomForest -P 100 -I 100 -num-slots 1<br>-K 0 -M 1.0 -V 0.001 -S1|
||6|75.00%|RandomForest -P 100 -I 100 -num-slots 1 -K 0 -M<br>1.0 -V 0.001 -S 1|RandomTree -K 0 -M 1.0 -V 0.001 -S 1 -do-not-<br>check-capabilities|
||7|80.00%|lazy. IBk -K 1 -W 0 -A||
||8|80.00%|M5Rules -M 4.0 -num-decimal-places 4||





R<sup>2</sup> is used to assess how strong the linear relationship between two variables is and is calculated as the square of the correlation coefficient (Equation 8): 



The mean absolute error (MAE) is a statistical measure of the difference between the actual values (x) and predicted values (y) and is calculated as the sum of the absolute errors divided by the sample size (n) (Equation 9). The MAE provides information about the amount of error but does not provide information about the direction of the error: 



The root mean squared error (RMSE) is often used as a measure of error for numerical estimation and is the square root of the mean square of the square of the overall error (Equation 10). The smaller the MAE and RMSE are, the better the performance of the model: 



## 3 | RESULTS AND DISCUSSION 

Models developed using machine learning algorithms reveal genetic differences. A total of 21 yield prediction models were presented as alternatives for the Bayraktar variety, and the model performances ranged between 0.74 ≤ R<sup>2</sup> ≤ 0.97. The MAE and RMSE of the models also varied between 18.6 and 53.7 and 23.0 and 67.4, respectively. It was determined that the models established according to the growth periods yielded more successful results (Table 6). For the Bayraktar variety, the model with the highest performance (R<sup>2</sup> = 0.97, MAE = 18.6 and RMSE = 23.0) was Model 1, which included the NDVI values (N0-N4) for the growth periods from sowing to flowering. This model, which uses a total of five variables, offers the possibility of prediction from the flowering period (approximately 2 months before harvest). For Model 1, the actual and predicted yields of the test data for random years and the corresponding errors are shown in Figure 3. 

Similarly, Model 2, Model 4 and Model 10 are other alternatives that provide successful results 2 months before harvest. The common feature of these models is that they require a small number of variables. Model 3, Model 5, Model 9, Model 11 and Model 12 can forecast 3 months before harvest. Model 5 offers high performance (R<sup>2</sup> = 0.91) with only two variables (Table 6). 

The number of variables used in the growth periods decreases closer to planting, allowing earlier prediction, but model performance decreases. Model 17, with NDVI values for the growth periods from sowing to stalk emergence (N0-N2), and Model 21, with NDVI values from 

AKCAPINAR and ÇAKMAK 

245 

TABLE 6 Models and performance criteria for Bayraktar variety. 

|Model|Independent variables|Number of variables|r|R<sup>2</sup>|MAE|RMSE|
|---|---|---|---|---|---|---|
|1|N0-N4|5|0.99|0.97|18.6|23.0|
|2|N4, Gp4|2|0.97|0.94|23.3|25.7|
|3|N0-N3|4|0.97|0.94|21.7|26.4|
|4|N4|1|0.96|0.91|25.1|30.6|
|5|N_Ap_I, L_Ap_I|2|0.95|0.91|30.3|40.8|
|6|N0-N2, acGp0-acGp2|6|0.94|0.88|38.6|45.4|
|7|N2, Gp2|2|0.93|0.87|29.7|38.5|
|8|VH0-VH2, acGp0-acGp2|6|0.93|0.87|39.4|47.6|
|9|Vs0-Vs3|4|0.93|0.87|35.2|41.2|
|10|N_My_I|1|0.93|0.86|32.1|38.6|
|11|VH_Ap_I|1|0.93|0.86|41.0|51.5|
|12|N3|1|0.92|0.85|29.6|39.9|
|13|N0-N1, L0-L1, acGp0-acGp1|6|0.92|0.85|49.0|56.9|
|14|N0-N2, L0-L2|6|0.91|0.84|34.8|46.7|
|15|VH0-VH2|3|0.91|0.83|44.3|51.5|
|16|VH_Fb_II|1|0.90|0.81|41.0|46.4|
|17|N0-N2|3|0.89|0.79|41.6|50.6|
|18|N_Dc_I, N_Dc_II, L_Dc_I, L_Dc_II|4|0.87|0.79|53.7|67.4|
|19|N0-N1, Gp0-Gp1|4|0.88|0.77|38.6|48.4|
|20|N2|1|0.87|0.75|45.4|53.6|
|21|N0-N1|2|0.86|0.74|45.8|52.5|



Abbreviations: MAE, mean absolute error; r, correlation coefficient; R<sup>2</sup> , coefficient of determination; RMSE, root mean squared error. 



FIGURE 3 Model 1 test results for Bayraktar variety. 

sowing to tillering (N0-N1), were found to be successful, predictions approximately 4–5 months before harvest. with performance values of 0.79 and 0.74, respectively. Different alternative models with variables such as the These two models offer the possibility of making LST, VHI and Gp were also developed for early 

AKCAPINAR and ÇAKMAK 

246 

prediction. Model 18 can forecast approximately 7 months before harvest, while Model 13, Model 16 and Model 19 can forecast approximately 5–6 months before harvest. The performances of the models were 0.79, 0.85, 0.81 and 0.77, respectively (Table 6). The models established for the growth period from sowing to stalk emergence were Model 6, Model 7, Model 8, Model 14, Model 15 and Model 20 according to their performance. These models can make predictions approximately 4 months in advance. Among these models, Model 7 is built with only two variables and has an R<sup>2</sup> value of 0.87. Model 16 and Model 20 are alternative models with a single variable (Table 6). 

For the Kızıltan variety, a total of 12 yield alternatives were presented as prediction models, and the model performances ranged between 0.73 ≤ R<sup>2</sup> ≤ 0.96. The MAE and RMSE of the models also varied between 17.4–56.9 and 26.7–67.1, respectively. It was determined that the models established according to the monthly index values yielded more successful results (Table 7). The model with the highest performance (R<sup>2</sup> = 0.96, MAE = 22.6 and RMSE = 28.9) was Model 1, which was established with monthly NDVI and LST values from October to May. Model 1 and Model 2 (R<sup>2</sup> = 0.94, MAE = 17.4 and RMSE = 26.7) with a total of 32 variables each and Model 3 (R<sup>2</sup> = 0.92, MAE = 25.3, 

TABLE 7 Models and performance criteria for Kızıltan variety. 

|Model|Independent variables|Number of variables|r|R<sup>2</sup>|MAE|RMSE|
|---|---|---|---|---|---|---|
|1|N_Oc_I- N_My_II, L_Oc_I- L_My_II|32|0.98|0.96|22.6|28.9|
|2|VH_Oc_I- VH_My_II, Vs_Oc_I-Vs_My_II|32|0.97|0.94|17.4|26.7|
|3|N_My_I, N_My_II, L_Ap_I, L_Ap_II|4|0.96|0.92|25.3|34.7|
|4|N_Oc_I- N_Fe_II, L_Oc_I- L_Fe_II|20|0.96|0.92|21.2|32.4|
|5|N_Oc_I- N_Dc_II, L_Oc_I- L_Dc_II|12|0.94|0.89|21.4|34.9|
|6|VH_Oc_I- VH_Fe_II, Vs_Oc_I- Vs_Fe_II|20|0.93|0.86|24.2|41.8|
|7|N0-N4, acGp0-acGp4|10|0.92|0.85|37.1|42.7|
|8|N0-N2, L0-L2|6|0.92|0.84|54.5|59.8|
|9|N0-N3|4|0.91|0.83|39.6|53.7|
|10|VH0-VH4|5|0.90|0.81|38.1|50.5|
|11|N_Oc_I- N_Jn_II, L_Oc_I- L_Jn_II|16|0.89|0.80|26.5|45.0|
|12|N4|1|0.86|0.73|56.9|67.1|



Abbreviations: MAE, mean absolute error; r, correlation coefficient; R<sup>2</sup> , coefficient of determination; RMSE, root mean squared error. 



FIGURE 4 Model 1 test results for Kızıltan variety. 

AKCAPINAR and ÇAKMAK 

247 

and RMSE = 34.7) with 4 variables, have high performance and offer the opportunity to predict approximately 2 months before harvest. Among these three models, Model 3 stands out because it uses fewer variables. For Model 1, Model 2 (which has lower MAE and RMSE values than Model 1) and Model 3 (which has a small number of variables), the actual and predicted yields of the test data for random years and the corresponding errors are shown in Figures 4, 5 and 6. 

For the Kızıltan variety, models that allow forecasting 2–7 months in advance are presented as alternatives (Table 7). 

Model 7, Model 10 and Model 12 provide successful results when used in predictions starting from flowering, Model 8 from tillering and Model 9 from spiking. The performances (R<sup>2</sup> ) of these models are 0.85, 0.81, 0.73, 0.84 and 0.83, respectively. The numbers of variables in the models are 10, 5, 1, 6 and 4. Among these, the model 



FIGURE 5 Model 2 test results for Kızıltan variety. 



FIGURE 6 Model 3 test results for Kızıltan variety. 

AKCAPINAR and ÇAKMAK 

248 

that can be used for the earliest prediction is Model 8, which also has a high R<sup>2</sup> value (Table 7). 

Model 4, Model 5, Model 6 and Model 11 stand out as the models that can be used for the earliest prediction. All these models use monthly variables, and the number of variables is 20, 12, 20 and 16. Their performance values (R<sup>2</sup> ) are 0.92, 0.89, 0.86 and 0.80, respectively. Model 4 and Model 6 can be used for forecasting approximately 5 months, Model 11 can be used for forecasting approximately 6 months, and Model 5 can be used for forecasting approximately 7 months before harvest. Model 5 was determined to be the most appropriate model to use due to its relatively low number of variables, its direct use of monthly NDVI and LST values, its high-performance value and the fact that it allows the earliest prediction (Table 7). 

For the Bezostaya variety, a total of eight yield prediction models were presented as alternatives, and the model performances ranged between 0.69 ≤ R<sup>2</sup> ≤ 0.87 (Table 8). The MAE and RMSE of the models also varied between 30.1 and 48.9 and between 39.5 and 55.2, respectively. Model 1 obtained from monthly NDVI and LST values and Model 2 obtained with the combination of VHI and VSWI according to growth periods were determined as the models with the highest R<sup>2</sup> performance (0.87). In addition to its high performance, Model 1 stands out because it directly uses monthly NDVI and LST values and allows predictions approximately 6 months before harvest. For Model 1 and Model 2, the actual and predicted yields of the test data for random years and the corresponding errors are shown in Figure 7 and Figure 8, respectively. 

TABLE 8 Models and performance criteria for Bezostaya variety. 

|Model|Independent variables|Number of variables|r|R<sup>2</sup>|MAE|RMSE|
|---|---|---|---|---|---|---|
|1|N_Oc_I- N_Jn_II, L_Oc_I- L_Jn_II|16|0.94|0.87|41.6|47.8|
|2|VH0-VH3, Vs0-Vs3, Gp0-Gp3|12|0.94|0.87|48.9|55.2|
|3|VH0-VH3|4|0.93|0.86|43.5|52.3|
|4|N_Oc_I- N_Fe_II, L_Oc_I- L_Fe_II|20|0.92|0.84|39.4|46.3|
|5|N_Oc_I- N_My_II|16|0.90|0.80|34.8|41.4|
|6|N0-N4, L0-L4|10|0.85|0.72|41.0|47.6|
|7|VH_Ap_II,VH_My_I,Vs_Ap_II,Vs_My_I|4|0.85|0.72|30.1|39.5|
|8|N4|1|0.83|0.69|46.6|54.6|



Abbreviations: MAE, mean absolute error; r, correlation coefficient; R<sup>2</sup> , coefficient of determination; RMSE, root mean squared error. 



FIGURE 7 Model 1 test results for Bezostaya variety. 

AKCAPINAR and ÇAKMAK 

249 



FIGURE 8 Model 2 test results for Bezostaya variety. 

These two models are followed by Model 3, with an R<sup>2</sup> value of 0.86. However, among these three models, Model 1 stands out because it allows forecasting approximately 6 months before harvest. Model 2 and Model 3 are alternatives that can be used for forecasting approximately 3 months before harvest, and Model 4 can forecast approximately 5 months before harvest. Although the other model alternatives (Models 5, 6, 7 and 8) are slightly inferior in terms of model performance and early prediction, they are considered acceptable alternative models (Table 8). 

## 4 | CONCLUSION 

In this study, drought–wheat yield relationships were examined on a plot basis, and according to growth periods, yield prediction models could be developed with these approaches, and the model performances were evaluated as significantly successful and usable in the research field. It was concluded that yield prediction models with satellite-based drought indices are suitable for early warning purposes, especially in areas where there are problems with the variety and continuity of agricultural data. In addition, high-quality and diverse phenological observations will enable the development of very successful prediction models in similar studies and will help to monitor the impact of climate change more effectively. 

### ACKNOWLEDGEMENTS 

This article is derived from the dissertation by Muhammed Cem Akcapınar, which was written under the supervision of Belgin Çakmak. 

### DATA AVAILABILITY STATEMENT 

The findings of the study can be cited and used by other researchers by considering the ethical rules. 

### REFERENCES 

- Aher, S.B. & Lobo, L. (2011) Data mining in educational system using WEKA. In: International conference on emerging technology trends (ICETT), Vol. 3. USA: Foundation of Computer Science, pp. 20–25. 

- Arslan, M., Zahid, R. & Ghauri, B. (2016) Assessing the occurrence of drought based on NDVI, LST and rainfall pattern during 2010–2014. In: 2016 IEEE international geoscience and remote sensing symposium (IGARSS). Beijing, China: IEEE, pp. 4233– 4236. 

- Didan, K., Munoz, A.B., Solano, R. & Huete, A. (2015) MODIS vegetation index user's guide (MOD13 series). USA: University of Arizona: Vegetation Index and Phenology Lab, p. 35. 

- Do�gan, I. & Karabulut, M. (2022) Türkiye'de büyüme derece günler-<sup>_</sup> inin zamansal ve mekânsal trendinin incelenmesi. Do�gal Afetler Ve Çevre Dergisi, 8(1), 122–133. Available from: https://doi.org/ 10.21324/dacd.883309 

- Ejaz, N. & Abbasi, S. (2020) Wheat yield prediction using neural network and integrated svm-nn with regression. Pakistan Journal of Engineering, Technology & Science, 8(2), 77. 

- Frank, E., Hall, M.A. & Witten, I.H. (2016) The WEKA workbench.<sup>_</sup> In: Kaufmann, M. (Ed.) Online appendix for "data mining: 

AKCAPINAR and ÇAKMAK 

250 

practical machine learning tools and techniques", fourth edition. USA: Morgan Kaufmann. 

- Gardner, M.W. & Dorling, S.R. (1998) Artificial neural networks (the multilayer perceptron)—a review of applications in the atmospheric sciences. Atmospheric Environment, 32(14–15), 2627–2636. Available from: https://doi.org/10.1016/S1352-2310 (97)00447-0 

- Hersbach, H., Bell, B., Berrisford, P., Biavati, G., Hor�anyi, A., Muñoz Sabater, J., et al. (2018) ERA5 hourly data on single levels from 1959 to present. Copernicus Climate Change Service (C3S) Climate Data Store (CDS). UK: ECMWF. 

- Huntington, J.L., Hegewisch, K.C., Daudert, B., Morton, C.G., Abatzoglou, J.T., McEvoy, D.J., et al. (2017) Climate engine: cloud computing and visualization of climate and remote sensing data for advanced natural resource monitoring and process understanding. Bulletin of the American Meteorological Society, 98(11), 2397–2410. Available from: https://doi.org/10.1175/ BAMS-D-15-00324.1 

- Kloos, S., Yuan, Y., Castelli, M. & Menzel, A. (2021) Agricultural drought detection with MODIS based vegetation health indices in Southeast Germany. Remote Sensing, 13(19), 3907. Available from: https://doi.org/10.3390/rs13193907 

- Kogan, F.N. (1995) Application of vegetation index and brightness temperature for drought detection. Advances in Space Research, 15(11), 91–100. Available from: https://doi.org/10.1016/02731177(95)00079-T 

- Kogan, F.N. (1997) Global drought watch from space. Bulletin of the American Meteorological Society, 78(4), 621–636. Available from: https://doi.org/10.1175/1520-0477(1997)078<0621: GDWFS>2.0.CO;2 

   - conference series: earth and environmental science, Vol. 389. UK: IOP Publishing, 012033. https://doi.org/10.1088/1755-1315/ 389/1/012033 

- MGM. (2021) Meteoroloji Genel Müdürlü�gü 2021 Yılı Ya�gı¸s De�gerlendirmesi. Ankara, Türkiye. Website: https://www.mgm. gov.tr/FILES/arastirma/yagis-degerlendirme/ 2021yagisdegerlendirmesi.pdf Eri¸sim Tarihi: 6.12.2023 

- MGM. (2022) Meteoroloji Genel Müdürlü�gü Resmi Istatistikler_ . Ankara, Türkiye. Website: https://www.mgm.gov.tr/ veridegerlendirme/il-ve-ilceler-istatistik.aspx?k=A&m= KONYA Eri¸sim Tarihi: 05.12.2022 

- Svoboda, M.D. & Fuchs, B.A. (2016) Handbook of drought indicators and indices. Geneva: World Meteorological Organization, pp. 1–44. 

- TIGEM.<sup>_</sup> (2020) Tarım I¸sletmeleri_ Genel Müdürlü�gü. Ankara, Türkiye: Altınova Tarım I¸sletmesi üretim kay<sup>_</sup> ıtları. 

- Wan, Z. (2013) MODIS land surface temperature products users' guide- Collection-6. Santa Barbara, CA, USA: Earth Research Institute (ERI), University of California, p. 805. 

How to cite this article: Akcapınar, M.C. & Çakmak, B. (2025) Yield prediction models for some wheat varieties with satellite-based drought indices and machine learning algorithms. Irrigation and Drainage, 74(1), 237–250. Available from: <u>https://doi.org/10.1002/ird.2989</u> 

- Masitoh, F. & Rusydi, A.N. (2019) Vegetation Health Index (VHI) analysis during drought season in Brantas Watershed. In: IOP 

