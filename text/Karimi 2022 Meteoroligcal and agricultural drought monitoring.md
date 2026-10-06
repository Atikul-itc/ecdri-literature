Stochastic Environmental Research and Risk Assessment (2022) 36:3707–3724 https://doi.org/10.1007/s00477-022-02220-3 (0123456789().,-volV)(0123456789().,volV) 

ORIGINAL PAPER 



# Meteorological and agricultural drought monitoring in Southwest of Iran using a remote sensing-based combined drought index 

Mahshid Karimi<sup>1•</sup> Kaka Shahedi<sup>1•</sup> Tayeb Raziei<sup>2•</sup> Mirhassan Miryaghoubzadeh<sup>3</sup> 

Accepted: 20 March 2022 / Published online: 18 April 2022 � The Author(s), under exclusive licence to Springer-Verlag GmbH Germany, part of Springer Nature 2022 

#### Abstract 

Drought is one of the most devastating natural hazards in the world, affecting millions of individuals in in different ways, so it’s better monitoring and comprehensive assessment is important. Univariate or multivariate drought indices are able to monitor one type of drought and can not reflect comprehensive drought information from meteorological to agricultural aspects. For this purpose, by combining the Vegetation Condition Index (VCI), Temperature Condition Index (TCI), the Soil Water Index (SWI) and the precipitation condition index (PCI) a comprehensive drought index called Combined Drought Index (CDI) was proposed. In this study, meteorological and agricultural droughts from 2001 to 1397 in Karkheh Basin in southwestern Iran were monitored. The Principal Component Analysis (PCA) method, which is a mainstay of modern data analysis tools for constructing a composite index, was applied to a data matrix that contains the time series of the computed PCI, VCI, TCI, and SWI indices for a given location, and the first leading component of the PCA was introduced as CDI index. The results indicated that the highest correlation (r = 0.53, r = 0.56) between the CDI, SPI-1 and SDI was observed respectively, which indicates the ability of this index for drought comprehensive monitoring. It is also suggested that in order to improve the performance of the CDI, in addition to the considered parameters in this study, other factors affecting the performance of each of the remote sensing indicators such as vegetation type, plant root, soil texture type, evaporation and Transpiration also be considered in future studies. 

Keywords Principal component analysis � TRMM � MODIS � Combined drought index � Karkheh 

## 1 Introduction 

Drought is one of the natural hazards causing many problems in environmental, social, and economic sectors (Zhang et al. 2017). There are 4 types of drought, including meteorological, hydrological, agricultural, and socio-economic droughts (Dracup et al. 1980; Keyantash and Dracup 2004; Orville 1990), from which the first three categories are related to water scarcity (Hao et al. 2015; Wang et al. 

> & Mahshid Karimi karimi.mahshid88@gmail.com 

> 1 Department of Watershed Management, Sari Agricultural Science and Natural Resources University, Sari, Iran 

- 2 Soil Conservation and Watershed Management Research Institute (SCWMRI), Agricultural Research, Education and Extension Organization (AREEO), Tehran, Iran 

> 3 Department of Rangeland and Watershed Management, Urmia University, Urmia, Iran 

2019). Various drought indicators are used to quantitatively analyze drought from various disciplinary perspectives. Many indices such as the Standardized Precipitation Index (SPI) (McKee et al. 1993) which is a precipitation-based drought index, are useful for studying meteorological drought though it is capable of monitoring other kinds of drought when the appropriate time scale is used (Raziei et al. 2009). However, to incorporate more climate variables into a single drought index, Vicente-Serrano et al. (2010) have proposed the Standardized PrecipitationEvapotranspiration Index (SPEI) which, in addition to precipitation, takes into consideration the atmospheric water demand represented by evapotranspiration estimation. Nonetheless, the input variables required for computing these indices are measured at meteorological stations that are sparsely distributed over the globe, particularly over the deserts and mountainous areas of the world. Therefore, the coarse spatial resolution of the available climate variables limits proper drought 

123 

Stochastic Environmental Research and Risk Assessment (2022) 36:3707–3724 

3708 

monitoring and characterization with adequate spatial distribution (Jiao et al. 2016; Wang et al. 2019). With the availability of satellite data and their widespread usage, it has become possible to use remote sensing data and provide more effective and accurate drought monitoring information (Heim 2002). Several drought indices including the Normalized Difference Vegetation Index (NDVI) (Yang et al. 1998), the Vegetation Condition Index (VCI) (Kogan 1995a, b), and the Temperature Condition Index (TCI) (Jiao et al. 2019) have been yet derived from remote sensing data. However, the univariate drought indices computed with either observation or remotely sensed data are not sufficient to characterize drought conditions. 

A univariate drought index monitors drought solely based on only one variable such as precipitation, runoff, or soil moisture (Waseem et al. 2015). Given that drought properties can not be fully signaled with a single climatological/environmental variable, a univariate drought index is not able to adequately reflect the complex attributes of drought events (Xu et al. 2015). For this reason, a large number of multivariate drought indicators were developed (Zargar et al. 2011). Very likely, the Palmer Drought Severity Index (PDSI) (Palmer 1965), the Surface Water Supply Index (SWSI) (Shafer and Dezman 1982), and SPEI (Vicente-Serrano et al. 2010) which are widely used for drought monitoring (e.g., Wells et al. 2004; Kwon and Kim 2010; Vicente-Serrano et al. 2011; Ma et al. 2014; Begueria et al. 2014; Li et al. 2015; Soh et al. 2018; Wambua 2019) are examples from this category. In general, univariate and multivariate drought indices mentioned above are mainly able to monitor one type of droughts, i.e., meteorological, hydrological, agricultural, or socio-economic drought (Yang et al. 2018). However, there may be several types of drought in an area that can not be identified simultaneously using univariate or the aforementioned multivariate indicators. To solve this problem, the combined drought indicators which are a combination of various univariate and multivariate drought indicators were proposed (Rajsekhar et al. 2015) to simultaneously monitor different types of drought (Chang et al. 2016; Yang et al. 2018). Numerous studies have emphasized the use of combined drought indicators for monitoring drought worldwide (Du et al. 2013; Hao et al. 2015; Waseem et al. 2015; Yang et al. 2018; Wang and Wei 2019; Liu et al. 2019; Sur et al. 2019; Kulkarni et al. 2020; Chen et al. 2020; Fassouli et al. 2021; Wei et al. 2021; Jiao et al. 2021). Different methods such as copula functions (Huang et al. 2014; Xu et al. 2015; Liu et al. 2019), Ordered Weighted Averaging (OWA) method (Jiao et al. 2019), multivariable linear regression method (Liu et al. 2020) and Principle Component Analysis (PCA) (Keyantash and Dracup 2004; Du et al. 2013; Bazrafshan et al. 2014; Hao et al. 2015; Liu et al. 2019; Kulkarni et al. 2020; Han et al. 

2020) have been proposed for this purpose. Among these approaches, PCA is an appropriate candidate for creating a composite drought index. PCA simply establishes a correlation matrix between the pool of drought indicators to statistically derive the most significant components based on a linear combination of the indicators defined by appropriately weighting the individual indicators and multiplying the weights to the indicators (Mainali and Pricope 2017). In this study, the PCA method was used to combine four satellite-based drought indices (Du et al. 2013; Hao et al. 2015), namely, the Vegetation Condition Index (VCI), Temperature Condition Index (TCI), Soil Water Index (SWI), and Precipitation Condition Index (PCI) to create the combined drought index (CDI) as a Meteorological/ Vegetation Drought Index (Hao et al. 2015). Many studies have already reported good performances of VCI, TCI, SWI, and PCI for drought monitoring in different areas of the world (e.g.,Van Hoek et al. 2016; Hu et al. 2019; Jiao et al. 2019; Baniya et al. 2019; Wang et al. 2019; Li et al. 2020; Han et al. 2020; Mishra et al. 2021). The VCI index which directly measures vegetation health (Quiring and Ganesh 2010) is a useful tool for monitoring drought onset and assessing the intensity, duration, and impact of drought around the World with a fine spatial resolution (Seiler et al. 2000; Anyamba et al. 2001; Ji and Peters 2003; Quiring and Ganesh 2010). The TCI index derived from the Land Surface Temperature (LST) data has a clear climatological perspective (Rhee et al. 2010; Zhang and Jia 2013; Jiao et al. 2019) and is being used to determine temperature-related plant stress (Karnieli et al. 2010). The SWI is also a very simple index useful for analyzing potential climate-induced plants’ root zone drought events and the associated consequences (Muukkonen et al. 2015). The PCI determined solely based on rainfall is not affected by changes in the land surfaces such as variations in land use and DEM (Wei et al. 2021). 

In this study, by combining rainfall, vegetation, soil moisture, and surface temperature parameters of the growing season, a combined drought index was created for monitoring meteorological and agricultural drought in the Karkheh Basin, southwest of Iran, based on a combination of VCI, TCI, SWI, and PCI indices derived from multisensor remote sensing data. It is assumed that the CDI derived from remote sensing data is better suited for meteorological and agricultural drought monitoring in the area since it integrated rainfall, vegetation, soil moisture, and surface temperature parameters of the growing season in a single drought index. The performance of the created CDI was evaluated by comparing it with the time series of SPI and Streamflow Drought Index (SDI) computed for the basin (e.g. Du et al. 2013; Waseem et al. 2015; Zhang et al. 2017; Jiao et al. 2019; Wang et al. 2019; Qaiser et al. 2021; Kulkarni et al. 2020; Wei et al. 2021; Fassouli et al. 2021). 

123 

Stochastic Environmental Research and Risk Assessment (2022) 36:3707–3724 

3709 

So, the purposes of this study are to: (1) The use of meteorological and vegetation drought indices (VCI, TCI, SWI and PCI) from multi-sensor remote sensing data for monitoring meteorological and agricultural drought. (2) The Presentation of a new reliable Combined Drought Index (CDI) to achieve a better monitoration of drought (3) the evaluation of the performance of CDI index to the changes of precipitation and Streamflow by SPI and SDI Indicators respectively. 

## 2 Materials and methods 

shows the location of the study area inside Iran and the spatial distribution of the used rain gauge stations over the basin (Fig. 1). 

### 2.2 Data 

#### 2.2.1 In situ data 

For this study 11 meteorological stations located in the main branches of the basin and possessing full data records during the 2001 to 2018 period were selected and used (Table1). 

### 2.1 Study area 

#### 2.2.2 Remote sensing data 

Karkheh basin is located in the middle and southwestern part of the Zagros Mountains in the west of Iran, extending from 30� 08<sup>0</sup> to 35� 04<sup>0</sup> N and 46� 06<sup>0</sup> to 49� 10<sup>0</sup> E (Fig. 1). The basin stretches over 50,768 km<sup>2</sup> , from which approximately 55.5% is situated in the mountainous areas and the rest in the plains and foothills. The mean annual temperature of the basin varies from less than 5 �C in the elevated areas of the basin to 25 �C in the southern regions. Figure 1 

The MODIS sensor images of the March to July period as the growing season were downloaded for 2000 to 2018 from the USGS website at https://earthexplorer.usgs.gov/. The 16-day NDVI with 1 km resolution (MOD13A3, collection v005) and 16-day LST with 1 km resolution (MOD11A2, collection v005) were retrieved from the images and used to calculate the VCI, TCI, and SWI indices. The TRMM monthly precipitation data (3B43) 



Fig. 1 Location of the study area and the spatial distribution of the rain gauge stations over the basin 

123 

Stochastic Environmental Research and Risk Assessment (2022) 36:3707–3724 

3710 

Table 1 Characteristics of the 

|<br>selected rain gauge and|Station code|Longitude|Latitude|Height (m)|Established year|Station type|
|---|---|---|---|---|---|---|
|hydrometry stations in the<br>KkhhRiBi|21–111|48�04<sup>0</sup>|34�50<sup>0</sup>|1803|1967|Rain gauge|
|are ver asn|21–113|47�33<sup>0</sup>|34�24<sup>0</sup>|1443|1966|Rain gauge and hydrometry|
||21–127|47�26<sup>0</sup>|34�21<sup>0</sup>|1280|1970|Rain gauge and hydrometry|
||21–133|46�47<sup>0</sup>|34�33<sup>0</sup>|1310|1966|Rain gauge and hydrometry|
||21–147|46�39<sup>0</sup>|33�44<sup>0</sup>|703|1966|Rain gauge and hydrometry|
||21–157|49�39<sup>0</sup>|33�44<sup>0</sup>|907|1981|Rain gauge and hydrometry|
||21–167|48�47<sup>0</sup>|33�31<sup>0</sup>|1770|1969|Rain gauge and hydrometry|
||21–173|48�47<sup>0</sup>|32�48<sup>0</sup>|960|1967|Rain gauge and hydrometry|
||21–189|48�05<br>0|32�48<sup>0</sup>|300|1969|Rain gauge and hydrometry|
||21–191|48�09<sup>0</sup>|32�25<sup>0</sup>|90|1956|Rain gauge and hydrometry|
||21–411|47�26<sup>0</sup>|33�11<sup>0</sup>|571|1977|Rain gauge and hydrometry|



relative to the 2000 to 2018 period were also retrieved from the Goddard Earth Sciences Data and Information Services Center at http://disc.sci.gsfc.nasa.gov/ (Table 2). 

### 2.3 Methods 

#### 2.3.1 Calculation of drought indices 

2.3.1.1 Vegetation condition index (VCI) The MOD13A2 product provides NDVI values for the pixels with 1 km spatial resolution, from which the VCI is calculated for each pixel and month of the years considered using Eq. 1 (Kogan 1997): 



where NDVIi is the value for the pixel and month i, NDVImax and NDVImin are the maximum and minimum values of the NDVI time series. The computed VCI values range between 0 and 1. The very low and very high values of VCI display unfavorable and favorable conditions, respectively (Amalo and Hidayat 2017). 

2.3.1.2 Temperature Condition Index (TCI) The MOD11A2 product provides LST values at pixels with 1 km spatial resolution. The TCI is computed by the following equation (Kogan 1997): 

Table 2 Characteristics of the satellite-based datasets used in the study 

|Satellite|Sensor|Spatial resolution|Product|
|---|---|---|---|
|Terra|MODIS|1 km|MOD13A2|
|Terra|MODIS|1 km|MOD11A2|
|Terra|MODIS|1 km|MOD13A2 and MOD11A2|
|TRMM|TMI|0.25�* 0.25�|3B43|





where LSTi is the LST value at a given pixel for the month i, LSTmax and LSTmin are the maximum and minimum values of the LST time series. As for VCI, the TCI values range from 0 to 1, with the lower and higher values displaying unfavorable and favorable conditions, respectively (Roswintiarti et al. 2011; Wang et al. 2012; Cong et al. 2017). 

2.3.1.3 Soil water index (SWI) This index shows the relationship between the land surface, vegetation, and soil moisture. To extract SWI, a triangular space concept was formed between the LST and NDVI data (Fig. 2). 

This condition occurs if we have a large range of vegetation and areas with different surface moisture in the image. In this figure, both wet and dry edges were obtained by fitting a linear equation to the minimum and maximum values of the earth’s surface temperature, respectively. 



Fig. 2 The hypothetical trapezoidal shape based on the relation between Ts and NDVI (Wang et al. 2012) 

123 

Stochastic Environmental Research and Risk Assessment (2022) 36:3707–3724 

3711 

After forming a triangular space, the SWI can be achieved for each point using Eq. 3 (Mallick et al. 2009): 



where i is the pixel number, LST(i) is the LST value for ith pixel, LSTmin(i) and LSTmax(i) are the maximum and minimum observed temperature of the intended pixel: 



where a1 and a2 are the y-intercept of the maximum and minimum surface temperature, respectively. Also, b1 and b2 are the slopes of the lines fitted to these variables that together formed the wet and dry edges as depicted in Fig. 2. 

2.3.1.4 Precipitation concentration index (PCI) Using the 

TRMM3B43 product of the TRMM satellite, the PCI index can be calculated as in Eq. 5. The PCI algorithm is the same as that in the VCI index. In this research, the TRMM3B43 data were resampled to 1 km spatial resolution and then used for calculating monthly PCI values. The range of this index also lies between zero and one. When the value of the index is close to or equal to zero it indicates a very low amount of precipitation, however, it is close to one when precipitation values are high (Liu et al. 2019). 



where TRMMmax and TRMMmin refer to the maximum and minimum values observed in the study period, and TRMMi is precipitation value observed in the ith month. Table 3 shows the classification of VCI, TCI, SWI, and PCI indicators. 

#### 2.3.2 Principal component analysis (PCA) 

PCA is a multivariate statistical method commonly used to uncover the relationship that exists between several 

Table 3 Classification of VCI, TCI, SWI, and PCI indicators 

|Satellite drought indices|Category|
|---|---|
|0 �VCI, TCI, SWI, and PCI\10|Extremely dry|
|10 �VCI, TCI, SWI, and PCI\20|Very dry|
|20�VCI, TCI, SWI, and PCI �30|Moderately dry|
|30 �VCI, TCI, SWI, and PCI �40|Mild dry|
|40\VCI, TCI, SWI, and PCI �100|No drought|



variables and expresses their relative importance in an orderly manner. The main purpose of the PCA method is to decrease the dimensionality of P-dependent variables into a few independent components (Deng et al. 2008). When the variables are highly correlated the few leading components can explain a large amount of information inherent in the data set. Accordingly, with a few principal components of the combined variables, an information structure is created that has the maximum characteristics of the primary data (Hao et al. 2015). The history of using PCA for dimension reduction in the meteorological, hydrological, and agricultural data dates back to several decades ago. However, the use of this method for extracting drought indices was first examined by Kiantash and Drcup (2004) who introduced the Aggregate Drought Index (ADI). PCA is of great importance in remote sensing as it is commonly used to compress massive data of different bands of an image. The output of this method is usually a few new bands with minimal inter-correlation as they are independent of each other but dependent on the original data. In this research, PCA was used to retain the main information coming from the linear relationship between the VCI, TCI, SWI, and PCI drought indices. Therefore, the computed VCI, TCI, SWI, and PCI at each pixel were introduced as the input of PCA for that pixel. The first principal component (PC1) of each PCA implemented for each pixel generally explains more than 80% of the total variance of the matrix of VCI, TCI, SWI, and PCI drought indices. Therefore, for each pixel, PC1 is introduced as the combined drought index (CDI) for that pixel. Finally, the CDI index is divided into five classes (Table 3) according to their magnitudes (Du et al. 2013). Figure 3 illustrates how CDI is computed and validated with SPI. 

#### 2.3.3 Validation 

To evaluate the performance of CDI at each pixel, correlation coefficient (r), Root Mean Square Error (RMSE), and Nash–Sutcliffe Efficiency (NSE) were calculated between the CDI and SPI computed at 1-, 3-, and 6- month time scales as well as the SDI computed for the basin. The correlation coefficient is used to measure the degree of dependence between the CDI and SPI/ SDI drought indices (Zeng et al. 2014; Hao et al. 2015) while RMSE and NSE criteria are used to measure the degree of deviation of CDI from SPI and SDI drought indices. If the RMSE between the two indices tends to be 0, and R and NSE approach 1, the estimated values are closer to the actual values (Nourani et al. 2019a, 2019b; Payab and Turker 2019). Here, the SPI and SDI are considered as the actual values with which the CDI is compared. 

123 

Stochastic Environmental Research and Risk Assessment (2022) 36:3707–3724 

3712 

Fig. 3 Flowcharts of the research steps 



#### 2.3.3.1 Standardized precipitation index (SPI) The SPI is 

a very popular meteorological drought index that is computed from long-term monthly precipitation data (Dutta et al. 2015). Based on the research of McKee et al. (1993), among the various series of SPI, the 1-, 3-, and 6-month time scales represent the short-term droughts while 12-, 24, and 48-month time scales are representative of the longterm drought periods. Short-term time scales are very sensitive to moisture conditions and are used to study meteorological and agricultural droughts whereas longterm time scales are used to study hydrological droughts. To calculate the SPI, the precipitation series of a given station accumulated at a given time scale ended at each calendar month must be fitted to an appropriate probability distribution function (PDF). McKee et al. (1993) showed that the gamma PDF has a good fit to the precipitation series of most of the climate areas aggregated to any given time scale. In this study, SPI was calculated using the monthly precipitation data aggregated at 1-, 3- and 6- month time scales. Positive SPI values illustrate that precipitation is higher than the long-term mean, while negative values show precipitation anomalies less than the longterm mean. The gamma distribution is defined as (McKee et al. 1993): 

where a [ 0 is the shape parameter, b [ 0 is the scale parameter, x is the precipitation amount, and C(a) is the gamma function. 

2.3.3.2 Streamflow Drought Index (SDI) Using the river discharge data of the basin, the SDI index was calculated with Eqs. 6 and 7 (Nalbantis and Tsakiris, 2009). 



where, i is the hydrological year, j is the month (e.g., for October j = 1 and for September j = 12), k is the reference period, Q is the monthly streamflow volume, Vi,k is the cumulative streamflow volume for the ith hydrological year and the kth reference period, and V k and Sk are respectively the mean and the standard deviation of cumulative streamflow volumes. Table 4 shows the classification of drought status for SPI and SDI (Nalbantis and Tsakiris, 2009; Du et al. 2013). 



123 

Stochastic Environmental Research and Risk Assessment (2022) 36:3707–3724 

3713 

Table 4 Classification of SPI and SDI indicators 

|SPI|SDI|Category|
|---|---|---|
|SPI\-2|SDI\-2|Extremely dry|
|- 2 �SPI\-1.5|- 2 �SDI\-1.5|Very dry|
|- 1.5 �SPI\-1|- 1.5 �SDI\-1|Moderately dr|
|- 1 �SPI\0|- 1 �SDI\0|Mild dry|
|0\SP|0\SDI|No drought|



## 3 Results and discussion 

### 3.1 Determining drought periods with CDI index 

The CDI index was calculated for March to July period of 2001 to 2018 and mapped for all individual months of the years. The created CDI maps were then classified into very severe, moderate, and mild drought classes plus a no drought class. Examining the CDI of March showed that drought has occurred in all the studied years. In 2008, 85.9% of the basin area was affected by drought, so that the classes of very severe, severe, moderate, and mild drought were 9%, 23%, 27.5%, and 26.4%, respectively and the no drought class covers 14.1% of the total basin area (Fig. 4). 

Examining the performance of the CDI index in April showed that drought phenomenon has occurred in all studied years, but the maximum incidence of this phenomenon was observed in 2008 so that drought with very severe, severe, moderate, and mild intensity accounts for 32.2%, 32.3%, 14.5% and 11% of the basin, respectively, and 11% of the total basin area was identified with no drought class (Fig. 5). 

The performance of the CDI index in May showed that the phenomenon of drought occurred in all years studied, but in 2008 and 2014 it hit 75.9% and 82.6% of the basin, respectively, by very severe to mild drought classes. The maximum incidence of this phenomenon was observed in 2014 so that the drought class was very severe, severe, moderate, and mild in 11.8%, 25%, 25.8%, and 19.9% of the basin, respectively; and the no drought class covers 17.4% of the total area of the basin (Fig. 6). 

The performance of the CDI index in June showed that the phenomenon of drought has occurred in all years studied, but in 2008 and 2014 it covered 80.4% and 71.8% of the area with very severe and mild drought, respectively. The maximum incidence of this phenomenon was observed in 2008 when very severe, severe, moderate, and mild drought occupied 25.6%, 27.5%, 16.2%, and 11.2% of the basin, respectively while the no drought class covers 19.6% of the total area of the basin (Fig. 7). 

The performance of the CDI index in July showed that the phenomenon of drought occurred in all years studied, but in 2008 and 2014 it spread over 62.4% and 55.9% of the basin. The maximum incidence of this phenomenon was observed in 2008 in which the very severe, severe, moderate, and mild drought occupied 9.6%, 12.3%, 19.5%, and 21.1% of the area, respectively (Fig. 8). 

Examining the CDI maps of the March to July period showed that the index appropriately monitored the occurrence of the most severe and widespread drought of 2008 which was identified as one of the severe droughts from 2000 to 2010 by the Meteorological Organization of Iran. In studies previously conducted by Rezaei Moghadam et al. (2012), Mirmousavi and Kareimei (2013), Rezaei Banafsheh et al (2015), and Mirahsani et al. (2017), the year 2008 has been identified as the driest year in Iran. The CDI index showed the onset of severe drought in May 2014, which was identified as one of the severe droughts from 2010 to 2018 by the Meteorological Organization of Iran. This result is also consistent with what achieved by Khodaei et al. (2016) and Mirahasani et al. (2017). So, the severe droughts of 2010 and 2014 were well monitored by the CDI maps shown in Figs. 4, 5, 6, 7 and 8. The drought events detected by CDI are consistent with the meteorological droughts identified by other studies (Porhemat et al. 2015; Karimi et al. 2019, 2020). However, the areal extent of droughts determined by the CDI differs from those reported by the aforementioned studies because CDI is a synthesized drought index that not only includes precipitation information but also the response of vegetation and soil to drought (Du et al. 2013). 

### 3.2 Performance evaluation of CDI 

To evaluate how the CDI performs in monitoring the meteorological and agricultural droughts in the basin, the remote sensing drought indices, i.e., VCI, TCI, SWI, PCI, and CDI were compared with the two most used drought indices, namely the SPI (McKee et al. 1993) and SDI (Nalbantis and Tsakiris 2009) indices computed for the stations considered, using the correlation coefficient, RMSE, and NSE performance indicators. There was found a linear relationship between the CDI and SPI/SDI drought indices in all studied stations. The VCI, TCI, SWI, and PCI drought indices also linearly correlated with SPI/SDI. Therefore, the Pearson correlation coefficient was used to assess the degree of association between the remote sensing drought indices and the SPI/SDI drought indices at the studied stations. Since the number of stations at which the indices were compared is enormous we avoid presenting the scatter plots of the linear correlations between the indices at the individual stations, instead, the average correlation coefficient of the stations is given in Fig. 9 

123 

Stochastic Environmental Research and Risk Assessment (2022) 36:3707–3724 

3714 

Fig. 4 Spatial distribution of drought intensity in March based on CDI index 



through Fig. 13. As shown in Fig. 9, the CDI time series of March moderately correlated with the SPI time series computed at 1-, 3-, and 6-month time scales (r = 0.56, 0.53, and 0.46, respectively, p-value \ 0.05 for all cases) and the SDI (r = 0.54). As depicted in Fig. 10, the correlation coefficient between CDI and SPI-1 slightly increases in April (r = 0.59). A similar correlation coefficient is observed between the CDI and SPI computed at 1-, 3-, and 6-month time scale (r = 0.56, 0.50, and 0.50, respectively) and the SDI (r = 0.52) for May (Fig. 11). In June, the correlation coefficient between the CDI and SPI at the considered time scales is 0.50, 0.47, and 0.44, respectively, 

and 0.50 between the CDI and SDI (Fig. 12). As is seen, the correlation coefficient between the CDI and SPI at 1-, 3-, and 6-month time scales is reduced to 0.43, 0.40, 0.39, and 0.44, respectively for July (Fig. 13). The result shows that the CDI has generally a better match with SPI than with VCI, TCI, SWI, and PCI drought indices. 

According to the results, the correlation coefficient between the satellite-based drought indices and SPI/SDI drought index computed with the ground-based data varies over the months of the growing season. Since the vegetation in the basin is mixed, it has caused different correlations between the satellite-based indices and the indices 

123 

Stochastic Environmental Research and Risk Assessment (2022) 36:3707–3724 

3715 

Fig. 5 Spatial distribution of drought intensity in April based on CDI index 



computed with the at situ ground-based data (Hao et al. 2015). The VCI showed the highest correlation coefficient with SPI-3 in March (r = 0.51) and April (r = 0.55) and with SPI-6 (r = 0.49) in May. A noticeable lower correlation coefficient observed for June and July is related to their less dense vegetation cover due to increasing the air temperature and atmospheric water demand (i.e., evapotranspiration) and drying out the soil moisture. VCI generally showed a better match with SPI3 and SPI6 time series. Zambrano et al. (2016), Winkler et al. (2017), and Jiao et al. (2019) also achieved similar results in their 

researches. This result indicates a temporal delay between effective precipitation and maximum vegetation growth (Winkler et al. 2017). Given that the effective precipitation in the study area usually begins in early winter, this temporal delay seems reasonable. On the other hand, the amount of this temporal delay depends on vegetation type and characteristics, soil situation, and potential evapotranspiration (Winkler et al. 2017). Also, due to the weak correlation between VCI and SPI-1, there is no coincidence between the meteorological and agricultural droughts in all the years. This finding agrees with the results of 

123 

Stochastic Environmental Research and Risk Assessment (2022) 36:3707–3724 

3716 

Fig. 6 Spatial distribution of drought severity in May based on CDI index 



Moazzenzadeh et al. (2013), Fatehi Maraj, and Heidarian (2013). Although vegetation is affected by precipitation, however, the VCI classes differ from those of SPI since the degree and the time of influence of precipitation on vegetation cover varies by time (Winkler et al. 2017). Also, because vegetation has always been affected by climate, it is very complicated to study the relationship between meteorological and agricultural droughts, and it seems that in addition to precipitation, other factors such as temperature, evapotranspiration, location height, land cover, land use, type of vegetation, type of soil texture and soil moisture, water supply for irrigation of the basin, amount 

and times of blockage and opening of the region’s dams are effective in the health and vegetation growth of the region (Bayarjargal et al. 2006; Mirahsani et al. 2017; Quiring and Papakryiakou 2003). On the other hand, the sensitivity of vegetation to precipitation is dependent on the region’s climate. Thus, areas with arid and semi-arid climates, where water is a limiting Parameter, show higher sensitivity than the humid regions (Winkler et al. 2017; Zhang et al. 2017; Jiao et al. 2019; Guo et al. 2020). The TCI has a relatively stronger correlation with SPI-3, indicating that it is more suitable for drought monitoring at shorter time scales. This result agrees with the findings of Zhang et al. 

123 

Stochastic Environmental Research and Risk Assessment (2022) 36:3707–3724 

3717 

Fig. 7 Spatial distribution of drought intensity in June based on CDI index 



(2017), Wang and Wei (2019), and Wei et al., (2021). The VCI showed a better performance than the TCI. One reason is that the TCI is mainly based on the LST data and the LST data is only derived from the thermal band information. Other information except the temperature can also be a good criterion for drought monitoring. Also, since the surface air temperature increases earlier than the vegetation cover decrease (Parviz and Khailghi 2011), the effectiveness of TCI in agricultural drought monitoring is ambiguous. 

A higher correlation exists between SWI and SPI-1 in regions with low vegetation density than the regions with high vegetation density, so SWI is more suitable for monitoring short-term drought conditions as confirmed by 

the findings of Jiao et al. (2019) and Zhang et al. (2017). The PCI performs similarly to SWI, as it showed a higher correlation with SPI-1 than SPI-3 and SPI-6. Since the PCI index is calculated based on precipitation information only and it is not affected by changes in vegetation, land use, and DEM (Wei et al. 2021), it can be expected that the PCI index properly shows the short-term meteorological conditions of the region as confirmed by the findings of Jiao et al. (2019), Zhang et al. (2017) and Wei et al. (2021). In Figs. 9, 10, 11, 12, and 13, unlike VCI, the TCI, PCI, and SWI showed a weak correlation with the SDI than SPI. The SDI and SPI have different nature and structure and determine the onset and duration of drought, respectively (Kavianpour et al. 2018). Therefore, since TCI, PCI and 

123 

Stochastic Environmental Research and Risk Assessment (2022) 36:3707–3724 

3718 

Fig. 8 Spatial distribution of July drought intensity based on CDI index 



SWI have a higher correlation with SPI, they can indicate the onset of drought like SPI and are suitable for short-term drought monitoring. 

The correlations between the satellite-derived drought indices and SPI computed at different time scales showed that CDI better matches SPI than the VCI, TCI, SWI, and PCI indices. The CDI showed the highest correlation with SPI-1 in March to July period. This finding is similar to the results of Du et al. (2013); Hao et al. (2015); Jiao et al. (2019) and Guo et al. (2020); Wang et al. (2019); Zhang et al. (2017). 

The RMSE and NSE indicators that measure the correspondence between the satellite-derived drought indices and SPI computed at different time scales (Table 5) also indicate an acceptable performance of CDI for drought monitoring in the basin. The lowest RMSE and highest NSE values in Table 5 correspond to the association between the CDI and SPI-1. According to the RMSE and NSE values of Table 5, the CDI has the poorer agreement with the streamflow records represented by SDI, which can be related to the fact that CDI is a combination of meteorological and vegetation conditions. 

123 

Stochastic Environmental Research and Risk Assessment (2022) 36:3707–3724 

3719 



<!-- Start of picture text -->
Fig. 9 The correlation 0.60<br>coefficientremotein March,sensingaveragedbetweendroughtSPIoverindicesandall thethe 0.50 0.49 0.51 0.48 March 0.51 0.49 0.47 0.56 0.530.460.54<br>studied stations 0.42 0.39 0.41<br>0.40<br>0.33<br>0.32<br>0.30 0.28 0.28<br>0.25 0.25<br>0.20<br>0.20<br>0.10<br>0.00<br>VCI TCI SWI PCI CDI<br>SPI1 SPI3 Index<br>SPI6 SDI<br>Fig. 10 The correlation 0.70<br>coefficient between SPI and the<br>April 0.59<br>remote sensing drought indices 0.60 0.55 0.55 0.50 0.56<br>in April, averaged over all the 0.50<br>studied stations 0.50 0.44 0.430.47 0.45 0.45 0.43<br>0.41 0.41<br>0.40<br>0.32<br>0.29<br>0.30 0.25<br>0.21<br>0.20 0.16 0.19<br>0.10<br>0.00<br>VCI TCI SWI PCI CDI<br>SPI1 SPI3 Index<br>SPI6 SDI<br>Fig. 11 The correlation 0.60<br>coefficientremote sensingbetweendroughtSPI indicesand the 0.49 May 0.50 0.48 0.560.500.500.52<br>in May, averaged over all the 0.50 0.43 0.46<br>studied stations 0.41 0.39<br>0.39<br>0.40 0.35 0.36<br>0.34<br>0.30 0.26 0.23 0.25<br>0.20 0.18<br>0.20<br>0.10<br>0.00<br>VCI TCI SWI PCI CDI<br>SPI1 SPI3<br>Index<br>SPI6 SDI<br>Correlation Coefficient<br>Correlation Coefficient<br>Correlation Coefficient<br><!-- End of picture text -->

123 

Stochastic Environmental Research and Risk Assessment (2022) 36:3707–3724 

3720 

Fig. 12 The correlation coefficient between SPI and the remote sensing drought indices in June, averaged over all the studied stations 

Fig. 13 The correlation coefficient between SPI and the remote sensing drought indices in July, averaged over all the studied stations 



<!-- Start of picture text -->
0.60<br>June 0.50 0.50<br>0.50 0.47<br>0.44<br>0.42<br>0.40 0.38 0.40 0.39 0.39<br>0.40 0.34 0.34<br>0.32 0.31<br>0.28<br>0.30 0.25<br>0.22 0.21 0.20<br>0.20<br>0.20<br>0.10<br>0.00<br>VCI TCI SWI PCI CDI<br>Index<br>SPI1 SPI3<br>SPI6 SDI<br>0.50<br>0.43 0.44<br>0.45 July 0.40<br>0.36 0.39<br>0.40 0.36 0.35<br>0.33 0.34 0.34<br>0.35 0.31 0.31<br>0.30<br>0.30 0.28<br>0.25<br>0.20 0.22<br>0.19 0.19<br>0.20 0.18 0.18<br>0.15<br>0.10<br>0.05<br>0.00<br>VCI TCI SWI PCI CDI<br>SPI1 SPI3 Index<br>SPI6 SDI<br>Correlation Coefficient<br>Correlation Coefficient<br><!-- End of picture text -->

Table 5 The mean RMSE and NSE values measuring the association between CDI and SPI/SDI of the growing season in the basin 

|Growing season|Combined drought index|SPI-1||SPI-3||SPI-6||SDI||
|---|---|---|---|---|---|---|---|---|---|
|||NSE|RMSE|NSE|RMSE|NSE|RMSE|NSE|RMSE|
|March|CDI|0.15|0.77|0.17|0.71|0.20|0.65|0.31|0.58|
|April|CDI|0.14|0.79|0.16|0.75|0.22|0.63|0.33|0.55|
|May|CDI|0.16|0.74|0.18|0.69|0.25|0.60|0.38|0.50|
|June|CDI|0.25|0.61|0.31|0.56|0.37|0.52|0.47|0.44|
|July|CDI|0.32|0.54|0.33|0.53|0.38|0.49|0.48|0.41|



Besides the good performance of CDI found in this study, the observed limitations that influence the analysis of drought events are (1) there is not a real ‘‘ground truth’’ measure of drought events in the basin to compare with the 

CDI. Although SPI and SDI indexes were used as the ‘‘ground truth’’ measures of drought in the basin, both of them are based on a single variable and are not the real representative of drought conditions in the area. Therefore, 

123 

Stochastic Environmental Research and Risk Assessment (2022) 36:3707–3724 

3721 

we were not able to provide a reliable and confident validation on the CDI. (2) None of the indicators (e.g., univariate, multivariate or composite) are inherently superior to the other indicators, but each of them is more suitable for its specific application than the other indicators. For example, when monitoring the meteorological drought conditions is of particular interest, the SPI would still be the main choice. (3) According to the studies on drought monitoring, the results derived from satellite data depend on the time and place of the studies, so these indicators operate regionally and their results may differ from a region to another. (4) The residual cloud noise in remote sensing images and their low spatial resolution might influence the results. 

## 4 Conclusions 

The present study examined the performance of a combinatorial drought index constructed based on meteorological and agricultural information relative to the growing season of the March to July period to comprehensively monitor drought in the Karkheh basin, southwest of Iran. For this purpose, in this study, VCI, TCI, SWI, and PCI indices were calculated and used for monitoring drought conditions in the whole Karkheh basin for the growing season of 2001–2018. The remote sensing drought indices were compared with SPI computed at 1-, 3- and 6- month time scales and SDI index computed with the in-situ precipitation and streamflow records. By applying the PCA to the time series of VCI, TCI, SWI, and PCI drought indices for each pixel the resulting first leading principal component was considered as a combinatorial drought index in this analysis. The results showed that the correlation coefficient between the combinatorial index and SPIs/SDI is higher than that obtained between the individual drought indices and SPIs/SDI which is confirmed by the lower RMSE and higher NSE values. In general, in the vegetation-based drought index, the parameters such as vegetation type, plant root, plant growth period, etc., can have a great impact on the performance of the index. In addition, the vegetation index does not perform well in areas with low density and sparse vegetation due to the effect of surface bare soil. On the other hand, due to their inherent characteristics, plants can cope with the lack of moisture, so they may respond to the occurrence of drought with a delay. The results indicate that the vegetation index in the months of declining plant growth (June and July) presented a poorer performance than the CDI index. Also, considering that the TCI index only considers the ground surface temperature and the SWI is sensitive to vegetation density and diversity and the PCI index only considers the precipitation parameter, they only describe the meteorological condition of the 

region. Therefore, these cases have created limitations in using single indicators. However, the CDI combines vegetation status, rainfall anomalies, surface heat stress, and soil moisture status. Therefore, it showed a more balanced and acceptable response in most of the studied months. Also, the high correlation coefficient between the CDI index and the 1-month SPI index indicates the ability of this index to monitor drought without delay. 

According to the results of this study, the ability of the combined drought index in drought monitoring in comparison to other drought indices is confirmed because: 

- (1) The combined drought index showed a higher correlation coefficient with SPI-1, SPI-3, and SPI-6 and SDI indices than other remote sensing indices (Figs. 9, 10, 11, 12 and 13). 

- (2) The RMSE and NSE tests also confirmed the better performance of the combined drought index for meteorological and agricultural drought monitoring (Table 5). 

- (3) The maps of CDI clearly show the extent and severity of the 2008 and 2014 droughts (Figs. 4, 5, 6, 7 and 8) which is in agreement with the previous studies (Rezaei Moghadam et al. 2012; Mirmousavi and Kareimei 2013; Rezaei Banafsheh et al. 2013; Mirahsani et al. 2017). For example, according to the reports of the Meteorological Organization of Iran, due to the 2008 drought, the Karkheh River was faced with a drastic water deficiency and the area under summer cultivation decreased about 10,000 hectares compared to previous years <u>(https://www.</u> farsnews.ir; http://www.wrm.ir/). Similarly, the occurrence of a very severe drought of 2014 dried up a large part of the Hawizeh Marshes which supplies its needed water through the Karkheh basin (http:// www.wrm.ir/). Finally, based on the studies and the above statistics and information, the maps of the combined drought index are consistent with the occurred realities in the study area. It is also suggested that in order to improve the performance of the CDI, in addition to the considered parameters in this study, other factors affecting the performance of each of the remote sensing indicators such as vegetation type, plant root, soil texture type, evaporation, and transpiration should be also considered in future studies. 

Author contributions MK: Conceptualization, statistical analysis, model implementation, writing original draft and review and editing. KS:: Conceptualization, review, and editing. TR: Conceptualization, review, and editing.MM: review and editing. 

Funding There is no funding regarding this paper. 

123 

Stochastic Environmental Research and Risk Assessment (2022) 36:3707–3724 

3722 

Data and material availability The datasets used and/or analyzed during the current study are available from the corresponding author on request. 

Code availability Software applications or custom code used during the current study are available from the corresponding author on reasonable request. 

### Declarations 

Conflict of interest The authors declare that they have no competing interests. 

Ethical approval Not applicable. 

Consent to participate All authors acknowledge their participation. 

Consent for publication All the authors read the paper, approved the final manuscript, and agreed to its submission to the Journal of Stochastic Environmental Research and Risk Assessment. 

## References 

- Amalo LF (2017) Hidayat R (2017) Comparison between remotesensing-based drought indices in east Java. IOP Conf. Series 54:012009. https://doi.org/10.1088/1755-315/54/1/012009 

- Anyamba A, Tucker CJ, Eastman JR (2001) NDVI anomaly patterns over Africa during the 1997/98 ENSO warm event. Int J Remote Sens 22:1847–1859. https://doi.org/10.1080/ 01431160010029156 

- Baniya B, Tang Q, Xu X, Haile GG, Chhipi-Shrestha G (2019) Spatial and temporal variation of drought based on satellite derived vegetation condition index in Nepal from 1982–2015. Sensors 19(2):430. https://doi.org/10.3390/s19020430 

- Bayarjargal Y, Karnieli A, Bayasgalan M, Khudulmur S, Gandush C, Tucker CJ (2006) A comparative study of NOAA–AVHRR derived drought indices using change vector analysis. Remote Sens Environ 105(1):9–22. https://doi.org/10.1016/j.rse.2006.06. 003 

- Bazrafshan J, Hejabi S, Rahimi J (2014) Drought monitoring using the Multivariate Standardized Precipitation index (MSPI). Water Resour Manage. https://doi.org/10.1007/s11269-014-0533-2 

- Begueria S, Vicente-Serrano SM, Reig F, Latorre B (2014) Standardized precipitation evapotranspiration index (SPEI) revisited: parameter fitting, evapotranspiration models, tools, datasets and drought monitoring. Int J Climatol 34(10):3001–3023. https://doi.org/10.1002/joc.3887 

- Chang J, Li Y, Wang Y, Yuan M (2016) Copula-based drought risk assessment combined with an integrated index in the Wei River Basin. China J Hydrol 540:824–834. https://doi.org/10.1016/j. jhydrol.2016.06.064 

- Chen S, Zhong W, Pan S, Xie Q, Kim TW (2020) Comprehensive drought assessment using a modified composite drought index: a case study in Hubei Province. China Water 12(2):462. https:// doi.org/10.3390/w12020462 

- Cong D, Zhao S, Chen C, Duan Z (2017) Characterization of droughts during 2001–2014 based on remote sensing: a case study of Northeast China. Eco Inform 39:56–67. https://doi.org/10.1016/j. ecoinf.2017.03.005 

- Deng JS, Wang K, Deng YH, Qi GJ (2008) PCA-based land-use change detection and analysis using multitemporal and multisensor satellite data. Int J Remote Sens 29(16):4823–4838. https://doi.org/10.1080/01431160801950162 

- Dracup JA, Lee KS, Paulson EGJr, (1980) on the statistical characteristics of drought events. Water Resour Res 16(2):289–296. https://doi.org/10.1029/WR016i002p00289 

- Du L, Tian Q, Yu T, Meng Q, Jancso T, Udvardy P, Huang Y (2013) A comprehensive drought monitoring method integrating MODIS and TRMM data. Int J Appl Earth Obs Geoinf 23:245–253. https://doi.org/10.1016/j.jag.2012.09.010 

- Dutta D, Kundu A, Patel NR, Saha SK, Siddiqui AR (2015) Assessment of agricultural drought in Rajasthan (India) using remote sensing derived Vegetation Condition Index (VCI) and Standardized Precipitation Index (SPI). Egypt J Remote Sens Space Sci 18(1):53–63. https://doi.org/10.1016/j.ejrs.2015.03. 006 

- Fassouli VP, Karavitis CA, Tsesmelis DE, Alexandris SG (2021) Factual Drought Index (FDI): a composite index based on precipitation and evapotranspiration. Hydrol Sci J 66(11):1638–1652. https://doi.org/10.1080/02626667.2021. 1957477 

- Fatehi maraj A, Heydarian SA, (2013) Investigation of meteorological, agricultural and hydrological drought using GIS in Khuzestan province. Iran-Watershed Manage Sci Eng 7(23):19–32 (In Persian) 

- Guo E, Wang Y, Jirigala B, Jin E (2020) Spatiotemporal variations of precipitation concentration and their potential links to drought in mainland China. J Clean Prod 267:1–14. https://doi.org/10.1016/ j.jclepro.2020.122004 

- Han Y, Li Z, Huang C, Zhou Y, Zong S, Hao T, Niu H, Yao H (2020) Monitoring droughts in the Greater Changbai Mountains using multiple remote sensing-based drought indices. Remote Sens 12(3):530. https://doi.org/10.3390/rs12030530 

- Hao C, Zhang J, Yao F (2015) Combination of multi-sensor remote sensing data for drought monitoring over Southwest China. Int J Appl Earth Obs Geoinf 35:270–283. https://doi.org/10.1016/j. jag.2014.09.011 

- Hu X, Ren H, Tansey K, Zheng Y, Ghent D, Liu X, Yan L (2019) Agricultural drought monitoring using European Space Agency Sentinel 3A land surface temperature and normalized difference vegetation index imageries. Agric Meteorol 279:107707. https:// doi.org/10.1016/j.agrformet.2019.107707 

- Huang S, Chang J, Huang Q, Chen Y (2014) Spatio-temporal changes and frequency analysis of drought in the Wei River Basin China. Water Resources Manage 28(10):3095–3110. https://doi.org/10. 1007/s11269-014-0657-4 

- Ji L, Peters A (2003) Assessing vegetation response to drought in the northern Great Plains using vegetation and drought indices. Remote Sens Environ 87:85–89. https://doi.org/10.1016/S00344257(03)00174-3 

- Jiao W, Tian C, Chang Q, Novick KA, Wang L (2019) A new multisensor integrated index for drought monitoring. Agric Meteorol 268:74–85. https://doi.org/10.1016/j.agrformet.2019.01.008 

- Jiao W, Wang L, McCabe MF (2021) Multi-sensor remote sensing for drought characterization: current status, opportunities and a roadmap for the future. Remote Sens Environ 256:112313. https://doi.org/10.1016/j.rse.2021.112313 

- Jiao W, Zhang L, Chang Q, Fu D, Cen Y, Tong Q (2016) Evaluating an enhanced vegetation condition index (VCI) based on VIUPD for drought monitoring in the continental United States. Remote Sensing 8(3):224. https://doi.org/10.3390/rs8030224 

- Karimi M, Shahedi K, Raziei T, Miryaghoubzadeh M (2019) Analysis of Performance of vegetation indices on agricultural drought using remote sensing technique in Karkheh basin. J Remote Sens GIS 11(4):29–46 (In Persian) 

- Karimi M, Vicente-Serrano SM, Reig F, Shahedi K, Raziei T, Miryaghoubzadeh M (2020) Recent trends in atmospheric evaporative demand in Southwest Iran: implications for change 

123 

Stochastic Environmental Research and Risk Assessment (2022) 36:3707–3724 

3723 

in drought severity. Theoret Appl Climatol 142(3):945–958. https://doi.org/10.1007/s00704-020-03349-3 

- Karnieli A, Agam N, Pinker RT, Anderson M, Imhoff ML, Gutman GG, Panov N, Goldberg A (2010) Use of NDVI and land surface temperature for drought assessment: merits and limitations. J Clim 23(3):618–633. https://doi.org/10.1175/2009JCLI2900.1 

- Keyantash JA, Dracup JA (2004) An aggregate drought index: assessing drought severity based on fluctuations in the hydrologic cycle and surface water storage. Water Resour Res 40(9):1–13. https://doi.org/10.1029/2003WR002610 

- Kavianpour M, Seyedabadi M, Moazami S (2018) Spatial and temporal analysis of drought based on a combined index using copula. Environ Earth Sci 77(22):1–12. https://doi.org/10.1007/ s12665-018-7942-0 

- Khodaei M, Shad R, Maghsudi mehari Y, Ghemi M, (2016) Determining an optimal multi-sensor remote sensing index to improve the real-time drought monitoring process in areas with heterogeneous land cover. Ecohydrology 3(3):439–454 (In Persian) 

- Kogan F (1995a) Application of vegetation index and brightness temperature for drought detection. Adv Space Res 15(11):91–100. https://doi.org/10.1016/0273-1177(95)00079-T 

- Kogan F (1995b) Droughts of the late 1980s in the United States as derived from NOAA polar-orbiting satellite data. Bull Am Meteor Soc 76(5):655–668. https://doi.org/10.1175/15200477(1995)076%3c0655:DOTLIT%3e2.0.CO;2 

- Kogan F (1997) Global drought watches from space. Bull Am Meteor Soc 78(4):621–636. https://doi.org/10.1175/15200477(1997)078%3c0621:GDWFS%3e2.0.CO;2 

- Kulkarni SS, Wardlow BD, Bayissa YA, Tadesse T, Svoboda MD, Gedam SS (2020) Developing a remote sensing-based combined drought indicator approach for agricultural drought monitoring over Marathwada India. Remote Sens 12(13):2091. https://doi. org/10.3390/rs12132091 

- Kwon HJ, Kim SJ (2010) Assessment of distributed hydrological drought based on hydrological unit map using SWSI drought index in South Korea. KSCE J Civ Eng 14(6):923–929. https:// doi.org/10.1007/s12205-010-0827-8 

- Li X, He B, Quan X, Liao Z, Bai X (2015) Use of the standardized precipitation evapotranspiration index (SPEI) to characterize the drying trend in southwest China from 1982–2012. Remote Sens 7(8):10917–10937. https://doi.org/10.3390/rs70810917 

- Li Z, Han Y, Hao T (2020) Assessing the consistency of remotely sensed multiple drought indices for monitoring drought phenomena in continental China. IEEE Trans Geosci Remote Sens 58(8):5490–5502. https://doi.org/10.1109/TGRS.2020.2966658 

- Liu Q, Zhang S, Zhang H, Bai Y, Zhang J (2020) Monitoring drought using composite drought indices based on remote sensing. Sci Total Environ 711:134585. https://doi.org/10.1016/j.scitotenv. 2019.134585 

- Liu Y, Zhu RL, Yong B, Singh VP, Yuan F, Jiang S, Yang X (2019) On the mechanisms of two composite methods for construction of multivariate drought indices. Sci Total Environ 647:981–991. https://doi.org/10.1016/j.scitotenv.2018.07.273 

- Ma M, Ren L, Yuan F, Jiang S, Liu Y, Kong H, Gong L (2014) A new standardized Palmer drought index for hydro-meteorological use. Hydrol Process 28(23):5645–5661. https://doi.org/10.1002/ hyp.10063 

- Mainali J, Pricope NG (2017) High-resolution spatial assessment of population vulnerability to climate change in Nepal. Appl Geogr 82:66–82. https://doi.org/10.1016/j.apgeog.2017.03.008 

- Mallick K, Bhattacharya BK, Patel NK (2009) Estimating volumetric surface moisture content for cropped soils using a Soil Wetness Index based on surface temperature and NDVI. Agric for Meteorol 149:1327–1342. https://doi.org/10.1016/j.agrformet. 2009.03.004 

- McKee TB, Doesken NJ, Kleist J (1993) The relationship of drought frequency and duration to time scales. In Eighth Conference on Applied Climatology, 17–22 January, Anaheim, CA, 179–184. DOI: https://doi.org/10.4236/oalib.1104254. 

- Mirahsani MS, Mahini AR, Safanian AR, Modares R, Jafari R, Mohamadi J (2017) Regional drought monitoring of ZayandehRud basin based on index time series changes VCI index MODIS Sensors and SPI index. J Geogr Environ Hazards 24(1):1–22. https://doi.org/10.22067/geo.v6i4.62601 (In Persian) 

- Mirmousavi SH, Kareimei H (2013) Effect of drought on vegetation cover using MODIS sensing images case: Kurdistan province. Geography and Development 11(31):57–76. https://doi.org/10. 22111/gdij.2013.794 (In Persian) 

- Mishra D, Goswami S, Matin S, Sarup J (2021) Analyzing the extent of drought in the Rajasthan state of India using vegetation condition index and standardized precipitation index. Model Earth Syst Environ https://doi.org/10.1007/s40808-021-01102-x 

- Moazzenzadeh R, Arshad S, Ghahraman B, Davari K (2013) Drought monitoring in unirrigated lands based on the remote sensing technique. Water Irrig Manag 2(2):39–52. https://doi.org/10. 22059/jwim.2013.30339 (In Persian) 

- Muukkonen P, Nevalainen S, Lindgren M, Peltoniemi M (2015) Spatial occurrence of drought-associated damages in Finnish boreal forests: results from forest condition monitoring and GIS analysis. J Boreal Environ Res 20:172–180 

- Nalbantis I, Tsakiris G (2009) Assessment of hydrological drought revisited. Water Resour Manage 23(5):881–897. https://doi.org/ 10.1007/s11269-008-9305-1 

- Nourani V, Molajou A, Uzelaltinbula S, Sadikoglu F (2019a) Emotional artificial neural networks (EANNs) for multi-step ahead prediction of monthly precipitation; case study: northern Cyprus. Theoret Appl Climatol 138(3):1419–1434. https://doi. org/10.1007/s00704-019-02904-x 

- Nourani V, Razzaghzadeh Z, Baghanam AH, Molajou A (2019b) ANN-based statistical downscaling of climatic parameters using decision tree predictor screening method. Theoret Appl Climatol 137(3):1729–1746. https://doi.org/10.1007/s00704-018-2686-z 

- Orville HD (1990) AMS statement on meteorological drought. Bull Am Meteorol Soc 71(7):1021–1025 

- Palmer, W.C., 1965. Meteorological drought. US Department of Commerce, Weather Bureau. 30: 58 p. 

- Parviz L, Khailghi M, (2011) Evaluation of the efficiency of indicators resulting from remote sensing technology in assessing meteorological drought (Case study: Sefidrood catchment). Geogr Dev Iran J 9(22):147–164 (In Persian) 

- Porhemat J, Razi T, Rahimibandarabadi S (2015) Investigation on Spatio-temporal Variability of Meteorological Drought in Southwestern Iran (case study in Karkheh basin). Irrigat Water Eng 5(3):60–79 

- Qaiser G, Tariq S, Adnan S, Latif M (2021) Evaluation of a composite drought index to identify seasonal drought and its associated atmospheric dynamics in Northern Punjab, Pakistan. J Arid Environ 185: https://doi.org/10.1016/j.jaridenv.2020.104332 

- Quiring SM, Ganesh S (2010) Evaluating the utility of the vegetation condition index (VCI) for monitoring meteorological drought in Texas. Agric for Meteorol 150(3):330–339. https://doi.org/10. 1016/j.agrformet.2009.11.015 

- Quiring SM, Papakryiakou TN (2003) An evaluation of agricultural drought indices for the Canadian prairies. Agric Meteorol 118(1–2):49–62. https://doi.org/10.1016/S0168-1923(03)000728 

- Rajsekhar D, Singh VP, Mishra AK (2015) Multivariate drought index: AN information theory based approach for integrated drought assessment. J Hydrol 526:164–182. https://doi.org/10. 1016/j.jhydrol.2014.11.031 

123 

Stochastic Environmental Research and Risk Assessment (2022) 36:3707–3724 

3724 

- Raziei T, Saghafian B, Paulo AA, Pereira LS, Bordi I (2009) Spatial and temporal variability of drought in western Iran. Water Resour Manag 23:439–455. https://doi.org/10.1007/s11269-0089282-4 

- Rezaei Banafsheh M, Rezaei A, Faridpor M (2015) Analyzing agricultural drought in east Azarbaijan province emphasizing remote sensing technique and vegetation condition index. Water Soil Sci (agric Sci) 25(1):113–123 (In Persian) 

- Rezaei Moghadam MH, Valizadeh Kamran KH, Rostamzadeh H, Rezaei A (2012) Evaluating the adequacy of MODIS in the assessment of drought (case study: Urmia lake basin). Geogr Environ Sustain 2(5):37–52 (In Persian) 

- Rhee J, Im J, Carbone GJ (2010) Monitoring agricultural drought for arid and humid regions using multi-sensor remote sensing data. Remote Sens Environ 114(12):2875–2887. https://doi.org/10. 1016/j.rse.2010.07.005 

- Richard R, Jr H (2002) A review of twentieth-century drought indices used in the United States. Bull Am Meteor Soc 83(8):1149–1166. https://doi.org/10.1175/1520-0477-83.8.1149 

- Roswintiarti O, Sofan P, Anggraini N (2011) Monitoring of droughtvulnerable area in Java Island, Indonesia using satellite remotesensing data. Jurnal Penginderaan Jauh Dan Pengolahan Data Citra Digital 8:21–34 

- Seiler RA, Kogan F, Wei G (2000) Monitoring weather impact and crop yield from NOAA AVHRR data in Argentina. Adv Space Res 26(7):1177–1185. https://doi.org/10.1016/S02731177(99)01144-8 

- Shafer BA, Dezman LE (1982) January. Development of surface water supply index (SWSI) to assess the severity of drought condition in snowpack runoff areas. Proceeding of the Western Snow Conference. Colo. State Univ. Fort Collins, pp 164–175 

- Soh YW, Koo CH, Huang YF, Fung KF (2018) Application of artificial intelligence models for the prediction of standardized precipitation evapotranspiration index (SPEI) at Langat River Basin, Malaysia. Comput Electron Agric 144:164–173. https:// doi.org/10.1016/j.compag.2017.12.002 

- Sur C, Park SY, Kim TW, Lee JH (2019) Remote sensing-based agricultural drought monitoring using hydrometeorological variables. KSCE J Civ Eng 23(12):5244–5256. https://doi.org/ 10.1007/s12205-019-2242-0 

- Van Hoek M, Jia L, Zhou J, Zheng C, Menenti, (2016) Early drought detection by spectral analysis of satellite time series of precipitation and normalized difference vegetation index (NDVI). Remote Sens 8(5):422. https://doi.org/10.3390/ rs8050422 

- Vicente-Serrano SM, Beguerı´a S, Lo´pez-Moreno JI (2010) A multiscalar drought index sensitive to global warming: the standardized precipitation evapotranspiration index. J Clim 23(7):1696–1718. https://doi.org/10.1175/2009JCLI2909.1 

- Vicente-Serrano SM, Beguerı´a S, Lo´pez-Moreno JI (2011) Comment on ‘‘Characteristics and trends in various forms of the Palmer Drought Severity Index (PDSI) during 1900–2008’’ by Aiguo Dai. J Geophys Res 116(D19):1–9. https://doi.org/10.1029/ 2011JD016410 

- Wambua RM (2019) Hydrological drought forecasting using modified surface Water Supply Index (SWSI) and Streamflow Drought Index (SDI) in conjunction with artificial neural networks (ANNs). Int J Serv Sci Manage Eng Technol (IJSSMET) 10(4):39–57. https://doi.org/10.4018/IJSSMET.2019100103 

- Wang K, Li T, Wei J (2019) Exploring drought conditions in the three river headwaters region from 2002 to 2011 using multiple drought indices. Water 11(2):190. https://doi.org/10.3390/ w11020190 

- Wang W, Zhang ZZ, Wang XG, Wang HM (2012) Evaluation of using the modified water deficit index derived from MODIS vegetation index and land surface temperature products for monitoring drought. In: 2012 IEEE international geoscience and remote sensing symposium, 5951–5954. Doi: https://doi.org/10. 1109/IGARSS.2012.6352253. 

- Waseem M, Ajmal M, Kim TW (2015) Development of a new composite drought index for multivariate drought assessment. J Hydrol 527:30–37. https://doi.org/10.1016/j.jhydrol.2015.04. 044 

- Wei W, Zhang J, Zhou L, Xie B, Zhou J, Li C (2021) Comparative evaluation of drought indices for monitoring drought based on remote sensing data. Environ Sci Pollut Res 28(16):20408–20425. https://doi.org/10.1007/s11356-02012120-0 

- Wells N, Goddard S, Hayes MJ (2004) A self-calibrating Palmer drought severity index. J Clim 17(12):2335–2351. https://doi. org/10.1175/1520-0442(2004)017%3c2335:ASPDSI%3e2.0. CO;2 

- Winkler K, Gessner U, Hochschild V (2017) Identifying droughts affecting agriculture in Africa based on remote sensing time series between 2000–2016: rainfall anomalies and vegetation condition in the context of ENSO. Remote Sens 9(831):1–27. https://doi.org/10.3390/rs9080831 

- Xu K, Yang D, Xu X, Lei H (2015) Copula based drought frequency analysis considering the spatio-temporal variability in Southwest China. J Hydrol 527:630–640. https://doi.org/10.1016/j.jhydrol. 2015.05.030 

- Yang J, Chang J, Wang Y, Li Y, Hu H, Chen Y, Huang Q, Yao J (2018) Comprehensive drought characteristics analysis based on a nonlinear multivariate drought index. J Hydrol 557:651–667. https://doi.org/10.1016/j.jhydrol.2017.12.055 

- Yang L, Wylie BK, Tieszen LL, Reed BC (1998) An analysis of relationships among climate forcing and time-integrated NDVI of grasslands over the US northern and central Great Plains. Remote Sens Environ 65(1):25–37. https://doi.org/10.1016/ S0034-4257(98)00012-1 

- Zambrano F, Lillo-Saavedra M, Verbist K, Lagos O (2016) Sixteen years of agricultural drought assessment of the BioBı´o region in Chile using a 250 m resolution Vegetation Condition Index (VCI). Remote Sensing 8(6):530. https://doi.org/10.3390/ rs8060530 

- Zargar A, Sadiq R, Naser B, Khan FI (2011) A review of drought indices. Environ Rev 19:333–349. https://doi.org/10.1139/a11013 

- Zeng L, Shan J, Xiang D (2014) March. Monitoring drought using multi-sensor remote sensing data in cropland of Gansu Province. In: IOP conference series: earth and environmental science (Vol. 17, No. 1, p. 012017). IOP Publishing 

- Zhang A, Jia G (2013) Monitoring meteorological drought in semiarid regions using multi-sensor microwave remote sensing data. Remote Sens Environ 134:12–23. https://doi.org/10.1016/j.rse. 2013.02.023 

- Zhang L, Jiao W, Zhang H, Huang C, Tong Q (2017) Studying drought phenomena in the Continental United States in 2011 and 2012 using various drought indices. Remote Sens Environ 190:96–106 

Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

123 

Reproduced with permission of copyright owner. Further reproduction prohibited without permission. 

