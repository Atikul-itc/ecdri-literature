**International Journal of Remote Sensing** 



**ISSN: 0143-1161 (Print) 1366-5901 (Online) Journal homepage: www.tandfonline.com/journals/tres20** 



# **Agricultural drought forecasting using satellite images, climate indices and artificial neural network** 

## **Ahmad Fatehi Marj & Allard M. J. Meijerink** 

**To cite this article:** Ahmad Fatehi Marj & Allard M. J. Meijerink (2011) Agricultural drought forecasting using satellite images, climate indices and artificial neural network, International Journal of Remote Sensing, 32:24, 9707-9719, DOI: 10.1080/01431161.2011.575896 

**To link to this article:** <u>https://doi.org/10.1080/01431161.2011.575896</u> 











Published online: 26 Jul 2011. Submit your article to this journal Article views: 1678 View related articles Citing articles: 26 View citing articles 



Full Terms & Conditions of access and use can be found at https://www.tandfonline.com/action/journalInformation?journalCode=tres20 

_International Journal of Remote Sensing_ Vol. 32, No. 24, 20 December 2011, 9707–9719 

## **Agricultural drought forecasting using satellite images, climate indices and artificial neural network** 

AHMAD FATEHI MARJ*† and ALLARD M. J. MEIJERINK‡ 

†National Centre for Agricultural Drought Management, Ministry of Jihad Agriculture, Tehran, Iran 

‡Department of Water Resources, International Training Centre for Aerial Survey (ITC), Enschede, The Netherlands 

( _Received 5 November 2008; in final form 30 November 2010_ ) 

A new model is proposed for agricultural drought forecasting based on normalized difference vegetation index (NDVI), which is based on satellite data, using effective climatic signals and artificial neural network (ANN). The applied ANN is a feedforward multiple neural network. The inputs of the model are the climatic signals Southern Oscillation Index (SOI) and North Atlantic Oscillation (NAO). In order to forecast NDVI with ANN, the normal method (NM) was used for the recent period, and for evaluation, the moving window method (MWM) was used for a longer (18 years) period. This model was applied to Ahar-chay Basin in Azerbaijan Province, which is located in the northwest of Iran. The results show that in spring (May, June and July (MJJ)) synthetic NDVI can be predicted using ANN, with the input of SOI and NAO indices of the preceding (1 year) spring period. The determinant coefficient ( _R_<sup>2</sup> ) between observed and predicted NDVI is 0.79, the root mean square error (RMSE) is 0.011 and the discrepancies are less than 1 SD. 

### **1. Introduction** 

Dryness is a permanent climatic attribute of a semi-arid area. Drought is a phenomenon due to less than normal rainfall in an area that is not necessarily a semi-arid area. Therefore, drought is not a permanent attribute of an area. There are various types of drought, such as climatological, hydrological and agricultural drought. Agricultural drought, which is the subject of this article, occurs when the vegetation cover reduces substantially during the growing period in rain-fed lands or pasturelands and its impact persists even after the end of the event. In the hilly or mountainous nature of the studied area in the west of Iran, the income of most of the people is related to non-irrigated agriculture (rain-fed) and livestock (pastureland). Agricultural drought therefore causes economical and social problems in this area. 

In order to plan alleviation measures it is desirable to avail of a timely forecast of agricultural drought, preferably by looking ahead to the next growing season. The objective of this study is to develop a method to forecast the effects of drought and test it with historical data of a semi-arid watershed in northwest Iran. 

*Corresponding author. Email: fatehi1339@gmail.com 

_International Journal of Remote Sensing_ ISSN 0143-1161 print/ISSN 1366-5901 online © 2011 Taylor & Francis http://www.tandf.co.uk/journals 

http://dx.doi.org/10.1080/01431161.2011.575896 

_A. Fatehi Marj and A. M. J. Meijerink_ 

9708 

A forecast of the effects of drought should be spatially distributed especially in relief-rich terrain where precipitation varies with altitude. Exposition of hill ranges and soil moisture storage depends on variable soil thickness and textures. Although precipitation data are the prime source for drought evaluation, paucity of stations hampers insight into spatial drought patterns, particularly in the studied area where snowfall stations are absent and rainfall stations are at higher altitudes. Hence, a data source, which provides spatial information about the effects of rainfall, is of relevance to this study. 

Therefore, the vegetation cover may be used not only as a response to rainfall and snowmelt but also to include effects of soil moisture storage. 

The spatial vegetation patterns can be studied by using the well-known normalized difference vegetation index (NDVI) explained below. NDVI data are widely used to monitor vegetation cover and drought events throughout the world (Goward _et al_ . 1985, Walsh 1987, Reed 1993, Kogan 1997). The evolution of the vegetation cover can be studied by using a time series of NDVI, which can be obtained from the Advanced Very High Resolution Radiometer (AVHRR) operated by the National Oceanic Atmospheric Administration (NOAA), having a high temporal frequency. 

Near-future weather systems at local scale of interest for a forecast are dependent on regional and global circulation patterns and therefore attention was given to global climatic signals, which were published from the readily available material. Such signals have been used to forecast rainfall and streamflow (Culen and De Menocal 2000, Culen _et al_ . 2002) and for these reasons their value for drought forecasting was adopted here. 

This study attempted to relate a forecast of NDVI, which may be regarded as synthetic NDVI values, with two climatic signals by using artificial neural network (ANN) analysis. 

A part of this study was to investigate whether this type of analysis is suitable to make an NDVI forecast with the input of two climatic signals. 

Therefore, the research question is: Is it possible with climatic signals, available now, to forecast the vegetation cover as an indicator of drought in the near future by employing ANNs? 

If a positive answer can be obtained, it would give the authorities time to prepare alleviation measures, but it should not prevent the real-time monitoring of NDVI when the drought has become manifest. 

### **2. Vegetation indices** 

Thanks to the availability of satellite data, it is possible to monitor vegetation density by means of a measure or index (Rouse _et al_ . 1974, Richards and Wiegand 1977, Tucker 1979). This measure, or vegetation index, makes use of the difference in spectral reflection of green vegetation in the near infrared (NIR) and the red parts of the spectrum (RED). The reflectance is recorded as digital numbers in the various bands or channels of satellite sensors. 

In terms of leaf area index (LAI) the NDVI varies more or less linearly with LAI values in the range of 0 LAI (bare soil) to LAI of about 2 (Baret 1991). For LAI _>_ 2 the relationship gradually reaches saturation for higher LAI (say LAI _>_ 4) values. This makes the NDVI suitable for studying vegetation cover in semi-arid areas, where rangeland vegetation prevails with NDVI values contrasting with those of rainfed crops. However, for low LAI values, the effect of differences of soil reflectance 

_Drought forecasting using satellite images_ 

9709 

influences NDVI values (Bartholome 1991). Higher NDVI values usually represent greater photosynthetic capacity (or greenness) of vegetation canopy (Tucker 1979). 

In order to avail of a time series of the vegetation index over long periods, the data provided by weather satellites such as NOAA-AVHRR can be used. Various indices have been used; three of them have been selected for this study as follows: NDVI is defined as 



Theoretically, values of NDVI vary from −1 to +1, for vegetation cover from 0 to 1. Anomaly vegetation index (AVI) is defined as 



where _i_ denotes the pixel value of the image and NDVImean is the average of NDVI. Vegetation condition index (VCI) is defined as 



where NDVImax and NDVImin are the maximum and minimum values of NDVI for each pixel in all periods. 

Many researchers such as Nicholson _et al._ (1990) investigated the relationship between NDVI and rainfall in area in Africa for 1982–1985. They found high correlation between NDVI and annual and monthly rainfall. Anyamba _et al._ (2001) investigated drought by using NDVI in South Africa and noticed two different patterns in El Nino Southern Oscillation (ENSO) years. Using NDVI data, they could predict drought for 1997–1998, a severe ENSO year. They found that the accuracy of the method using NDVI is higher than that of the method that used rainfall for drought forecasting. For studying droughts in Brazil, Liu and Negron (2001) used NDVI. They found that 19 out of 21 droughts conform to NDVI time series. Karabulut (2003) investigated different rainfall regimes using biweekly maximum value composite (MVC) of NDVI data in order to assess vegetation response in the south-eastern part of the Black Hills region, SD, USA. 

VCI and temperature condition index (TCI) used by Kogan (1997) in Africa and Asia have been useful in detecting and monitoring large-area, drought-related vegetation stress. He used NDVI on a large area with much diversified ecological resources. Spatial and temporal variations in meteorological, hydrological and vegetative (VDI) drought indices in the Aravalli terrain of western India have been analysed and correlated for monsoon and non-monsoon seasons during the years 1984–2000 by Bhuiyan _et al._ (2006). The results show that the combination of various indices offers better understanding and better monitoring of drought conditions for a hilly, semi-arid terrain like the Aravalli. Bayarjargal _et al._ (2007) presented detection of drought-affected regions by calculating the NDVI for a Mediterranean semi-arid region. Gu _et al_ . (2007) analysed grassland drought assessment within the central USA. Results of this research show strong relationships among NDVI, normalized difference water index (NDWI) and drought condition. Ratana _et al._ (2007) used a 16-day composite NDVI and 7 years (2000–2006) of precipitation data. They found spatial rainfall and NDVI anomalies as well as time lag relationships between rainfall and NDVI. Results of this 

_A. Fatehi Marj and A. M. J. Meijerink_ 

9710 

research showed downward trends in the 7-year NDVI temporal profiles with negative anomalies in rice, crops, orchards and deciduous forest. This suggests that the impact of drought on vegetation can be seen with satellite observations. 

### **3. Climate indices: SOI and NAO** 

As mentioned in §1, the use of these indices is explored to forecast the near-future NDVI variation, which allows an insight into the spatial patterns of the effects of drought because of near absence of precipitation stations in the studied area. 

Results of worldwide studies show that there are many regions where rainfall is related to climatic signals. These signals are identified as numerical climate indices such as North Atlantic Oscillation (NAO) and Southern Oscillation Index (SOI), which are provided and standardized by using measures of temperature and air pressure in different regions of oceans (Hughes and Saunders 2001, Nicholson 2001). ENSO is composed of two words El Nino and Southern Oscillation. ENSO is a combination of interrelated oceanic and atmospheric processes that occur every 2–7 years. The Southern Oscillation refers to the changeover of atmospheric pressure between the eastern and western halves of the Equatorial Pacific. Although the Southern Oscillation and the El Nino are closely related, an El Nino may occur independently or at the same time as a Southern Oscillation. When the two coincide the result is an extreme global atmospheric and oceanographic event. The difference of pressure between Tahiti in the east and Darwin in the west of the Pacific is used as a base for measuring SOI, and negative and positive amounts indicate different phases of ENSO (Bell _et al_ . 2000). 

The NAO is a climatic phenomenon in the North Atlantic Ocean of fluctuations in the difference of sea-level pressure between the Icelandic Low and the Azores High. Through east–west rocking motions of the Icelandic Low and the Azores High, it controls the strength and direction of westerly winds and storm tracks across the North Atlantic (Bradbury _et al_ . 2002) and their effect on the weather of central Asia. 

Some authors investigated the relationships between climatic signal and streamflow or rainfall. Culen and De Menocal (2000) analysed the impact of NAO on river discharge of the Digleh-Forat River in Iraq and Turkey and found some degree of correlation between winter streamflow and NAO in Turkey ( _r_ = −0.42) and Iraq ( _r_ = −0.48). The impact of NAO on winter streamflow of the Karon River in southern Iran is weak but significant ( _r_ = −0.29) according to a study by Culen _et al._ (2002). Nazemosadat _et al._ (2006) found that the impact of ENSO on autumn rainfall is significant in northwest Iran. Fatehi Marj _et al._ (2006) observed a significant correlation between spring NAO and SOI with next spring streamflow in Urmieh Lake basin in northwest Iran. 

For this study, whether the climatic signals could be of use for the forecast of synthetic NDVI in the study area and what the optimal periods of lead time were had to be investigated. Obviously, too short a period, say, less than a few weeks, would render the effort less significant as real-time NDVI monitoring with satellite sensors would be preferred. However, a meaningful contribution would be achieved in case the analysis would indicate that a forecast with much longer lead times is possible. 

The desirability of longer lead times contributed much to the selection of the ANN approach described below. For forecasting stochastic models are often used, but for this type of study long-term rainfall would be required, which is non-existent in the area and moreover, stochastic models have probabilistic results with limited time steps. 

_Drought forecasting using satellite images_ 

9711 

### **4. Materials and methods** 

### **4.1** **_Study area_** 

The procedures described below were applied to the Ahar-chay sub-basin of the Arras River basin in Azerbaijan Province, in the northwest of Iran. The area of this basin is 1760 km<sup>2</sup> ; the rainfall is about 250 mm but is probably higher in the elevated parts, where much of the precipitation occurs as snow. An NDVI image of the basin taken by Landsat Enhanced Thematic Mapper Plus (ETM+) at 30 m resolution on 4 July 2002 is shown in figure 1. The locations of the sample pixels of the low-resolution NOAAAVHRR image time series are indicated. Previous research by Fatehi Marj _et al._ (2006) in the western part of Azerbaijan province (Urmieh Lake basin) shows that there are significant relationships between climatic signals and next year streamflow. For the Ahar-chay Basin there are only NDVI images for drought investigation (no rainfall data and no streamflow data). 

### **4.2** **_Vegetation index based on satellite data_** 

Daily RED and NIR bands of NOAA-AVHRR images for the period, with a spatial resolution of the ground elements of 8 km × 8 km, were used to prepare NDVI images using equation (1). NOAA-AVHRR data are available from National Aeronautics and Space Administration (NASA), Goddard Space Flight Center, Greenbelt, MD, USA. As mentioned the NDVI values have been converted by the data source to the range of 1–255, wherein high values are associated with dense vegetation and low values with bare conditions or sparse vegetation cover. No atmospheric corrections were made. The NDVI images are maximum 10-day composite NDVI images, from which monthly average NDVI was obtained. AVI and VCI were calculated from equations 



<!-- Start of picture text -->
N<br>NDVI<br>0.32<br>0.21<br>0.09<br>–0.02<br>–0.14<br>–0.25 Mixed pasture and rain-fed<br>River farming<br>46° 20′ E 46° 30′ E 46° 40′ E 46° 50′ E 47° 00′ E 47° 10′ E<br>′ ° 3840N<br>′ ° 3830N<br><!-- End of picture text -->

Figure 1. Normalized difference vegetation index (NDVI) image of study area and sample points (4 July 2002). 

_A. Fatehi Marj and A. M. J. Meijerink_ 

9712 

(2) and (3), respectively. For the average vegetation condition during spring, NDVI values for May, June and July (MJJ) were calculated according to the growing season in this area. Data for the period 1982–2000 were selected to coincide with the available rainfall data of the nearest rainfall station (Tabriz) near the selected Ahar-chay Basin. Using NDVI images, VCI, AVI and NDVI were investigated in order to differentiate between dry and wet periods. The wet and dry periods are distinguished using polynomial (poly) equation. It was found that AVI and VCI were highly correlated with NDVI (figure 2). Therefore NDVI was selected for this study, because NDVI is a better index for variation of vegetation cover. 

On average, nine pixels around the sample point (figure 1) of the NDVI images covering rangelands and rain-fed agriculture were used as observation data. These pixels were first selected on Landsat ETM+ images with a spatial resolution of 30 m × 30 m and then overlaid on the NOAA-AVHRR NDVI images. 

### **4.3** **_SOI and NAO indices_** 

Monthly time series of SOI and NAO for the above-mentioned period were used as input in the ANN analysis. These data were downloaded from 



<!-- Start of picture text -->
( a )<br>105.00<br>90.00<br>VCI Poly (VCI)<br>75.00<br>60.00<br>45.00<br>30.00<br>15.00<br>0.00<br>Month and year<br>( b )<br>0.31<br>0.28<br>NDVI Poly (NDVI)<br>0.25<br>0.22<br>0.19<br>0.16<br>0.13<br>0.10<br>Month and year<br>( c )<br>3.00<br>2.00 AVI Poly (AVI)<br>1.00<br>0.00<br>–1.00<br>–2.00<br>–3.00<br>Month and year<br>VCI<br>1982 5 1982 6 1982 7 1983 5 1983 6 1983 7 1984 5 1984 6 1984 7 1985 5 1985 6 1985 7 1986 5 1986 6 1986 7 1987 5 1987 6 1987 7 1988 5 1988 6 1988 7 1989 5 1989 6 1989 7 1990 5 1990 6 1990 7 1991 5 1991 6 1991 7 1992 5 1992 6 1992 7 1993 5 1993 6 1993 7 1994 5 1994 6 1994 7 1995 5 1995 6 1995 7 1996 5 1996 6 1996 7 1997 5 1997 6 1997 7 1998 5 1998 6 1998 7 1999 5 1999 6 1999 7<br>NDVI<br>1982 5 1982 6 1982 7 1983 5 1983 6 1983 7 1984 5 1984 6 1984 7 1985 5 1985 6 1985 7 1986 5 1986 6 1986 7 1987 5 1987 6 1987 7 1988 5 1988 6 1988 7 1989 5 1989 6 1989 7 1990 5 1990 6 1990 7 1991 5 1991 6 1991 7 1992 5 1992 6 1992 7 1993 5 1993 6 1993 7 1994 5 1994 6 1994 7 1995 5 1995 6 1995 7 1996 5 1996 6 1996 7 1997 5 1997 6 1997 7 1998 5 1998 6 1998 7 1999 5 1999 6 1999 7<br>AVI<br>1982 5 1982 6 1982 7 1983 5 1983 6 1983 7 1984 5 1984 6 1984 7 1985 5 1985 6 1985 7 1986 5 1986 6 1986 7 1987 5 1987 6 1987 7 1988 5 1988 6 1988 7 1989 5 1989 6 1989 7 1990 5 1990 6 1990 7 1991 5 1991 6 1991 7 1992 5 1992 6 1992 7 1993 5 1993 6 1993 7 1994 5 1994 6 1994 7 1995 5 1995 6 1995 7 1996 5 1996 6 1996 7 1997 5 1997 6 1997 7 1998 5 1998 6 1998 7 1999 5 1999 6 1999 7<br><!-- End of picture text -->

Figure 2. ( _a_ ) Vegetation condition index (VCI), ( _b_ ) normalized difference vegetation index (NDVI) and ( _c_ ) anomaly vegetation index (AVI) time series. 

_Drought forecasting using satellite images_ 

9713 

http: _//_ www.cdc.noaa.gov _/_ ClimateIndices _/_ Analysis. As mentioned above, the effect of SOI and NAO on rainfall and streamflow in this region was demonstrated by Fatehi Marj _et al._ (2006). The research shows that spring SOI and NAO had the greatest effect on autumn and winter rainfall, followed by next-year spring streamflow. Therefore, spring SOI and NAO are examined to forecast next spring NDVI using a non-linear tool such as ANN. For training and testing of the ANN model, average SOI and NAO for spring (April, May and June) (1982–1999) were used as input, and average NDVI for MJJ was selected as output. Forecasting was done for 1-year lead time (figure 3). 

### **4.4** **_Artificial neural network_** 

In most cases an ANN is an _adaptive system_ that changes its structure based on external or internal information that flows through the network during the learning phase. Neural networks are _non-linear statistical data modelling_ tools. They can be used to model complex relationships between inputs and outputs or to _find patterns_ in data. 

ANN has been used for forecasting rainfall and streamflow. Silverman and Dracup (2000) applied feedforward ANN and climate indices for rainfall forecasts in different parts of California with reasonably accurate results. Danh _et al._ (1999) predicted discharges of the Da Nhim and La Nga Rivers in Vietnam using ANN and obtained results that were better than those obtained by a hydrological tank model simulation. A similar research by Tingsanchali and Gautam (2000) obtained the same result in Thailand. Campolo _et al_ . (2003) used ANN for forecasting Arno River discharge for 6 h ahead in Italy. Forecasts of drought in the Conchos River in Mexico using ANN were made by Kim and Valdes (2003) for 6-month lead time. 

Although one may come across various references on the use of ANN for forecasting streamflow or rainfall, no references could be found where climate indices were used as input in ANN for NDVI forecasts. Because of the importance of agricultural drought forecasting, we have tried here to use SOI and NAO climate indices as input in ANN to obtain NDVI as output. 

In this research, the ANN for forecasting is a feedforward multilayer or multilayer perceptron that was recommended by Shamseldin (1997) and Silverman and Dracup (2000) for water resources studies. Normally, back-propagation learning statute is used for training. Topology of ANN multilayers is completed with back-propagation error statute (Teshnelab and Watanabe 1999). The designed neural network contains one input layer with two neurons, one hidden layer with six neurons and an output layer 



<!-- Start of picture text -->
0.30<br>NDVI Average<br>0.25<br>Poly (NDVI)<br>0.20<br>0.15<br>0.10<br>Month and year<br>NDVI<br>1982 5 1982 6 1982 7 1983 5 1983 6 1983 7 1984 5 1984 6 1984 7 1985 5 1985 6 1985 7 1986 5 1986 6 1986 7 1987 5 1987 6 1987 7 1988 5 1988 6 1988 7 1989 5 1989 6 1989 7 1990 5 1990 6 1990 7 1991 5 1991 6 1991 7 1992 5 1992 6 1992 7 1993 5 1993 6 1993 7 1994 5 1994 6 1994 7 1995 5 1995 6 1995 7 1996 5 1996 6 1996 7 1997 5 1997 6 1997 7 1998 5 1998 6 1998 7 1999 5 1999 6 1999 7<br><!-- End of picture text -->

Figure 3. Evolution of normalized difference vegetation index (NDVI) in Ahar-chay Basin (1982–1999). 

_A. Fatehi Marj and A. M. J. Meijerink_ 

9714 

with one neuron. The use of a single hidden layer is usually recommended. The use of extra hidden layers substantially increases the number of parameters and may slow the calibration process. Furthermore, determination of optimum number of neurons in the hidden layer is essential. Choosing too few or too many neurons may deteriorate the performance of the network. Too few neurons may cause the network to become too parsimonious in its use of parameters. However, it is known that use of too many neurons may cause overfitting of the calibration dataset. The number of neurons in the hidden layer was selected using a trial-and-error approach (Shamseldin 1997, Silverman and Dracup 2000). The base function is according to equation (4): 



where _Hi_ is the neural net input, _w_ is the weight of each input for each neuron; _x_ is the input value; _i_ is the _i_ th neuron; _j_ is the _j_ th input; and _bi_ is the threshold value of each neuron. Different transfer functions can be used: sigmoid, hyperbolic tangent and linear. In this research, based on the range of input (SOI and NAO) and output data (NDVIpredicted) the hyperbolic tangent transfer function was used, see equation (5): 



The data for the period 1990–1995 were selected for training of the neural network, because it contained one drought and one wet period. The network can be trained using minimum and maximum values. In order to forecast agricultural drought, NDVI of 1996–1999 was used. Data from 1996 to 1999 were not used for training. 

The number of neurons in the input layer and the output layer is the same as the number of inputs and outputs. The number of neurons in the hidden layer was six, using trial and error. The criteria for the selection of the number of neurons were high _R_<sup>2</sup> and low mean square error (MSE) between observed and predicted values in the training period. The training of the network was continued until the MSE was found to increase. A higher number of neurons may increase the accuracy of the training but decrease the accuracy of the forecast. Concerning the feedforward multilayer ANN, about 80% of data were used for training and 20% were retained for testing. 

### **4.5** **_Forecast with normal method and moving window method in ANN_** 

Vegetation cover, and thus NDVI, is maximum in MJJ in the study area. Therefore, the averaged NDVI for these 3 months is considered as spring vegetation cover. Forecasting of NDVI was done using two methods in ANN: the so-called normal method (NM) and the moving window method (MWM). 

The NM is a method that considers 80–90% of data for training of network and the remaining 20–10% for testing or forecasting. Normally, the forecasting period is selected at the end of the time series. Most of the research using ANN used NM (Shamseldin 1997, Silverman and Dracup 2000). In NM, the result is valid for a given period and it is not clear whether the result is valid or not if the forecasting period changes. Therefore, the MWM is applied in order to confirm NM results for forecasting NDVI for all years. In the MWM, the first step is similar to the NM for training 

_Drought forecasting using satellite images_ 

9715 

and testing, but training and forecasting are repeated for many periods. A window with 5 years is selected for forecasting (testing). In the next training 1 year from forecasting moves to training period and 1 year from training moves to forecasting period. This training and forecasting is continued till all years are placed in the forecasting period. The input of the model is seasonal SOI and NAO. The model was trained for four states. For each training state, spring NDVI was the output, and NAO and SOI of one, two, three and four preceding seasons were selected as separate input. For confirmation of the results by NM, MWM was used for all years (1982–1999) and the accuracy of results was assessed using _R_<sup>2</sup> and root mean square error (RMSE) statistic. 

### **5. Results** 

The NDVI time series show that there are two drought periods (1982–1985 and 1996– 1999) and two wet periods (1986–1989 and 1990–1995) in the basin (see figure 2). It was found that the three indices investigated (NDVI, AVI and VCI) had highly similar results and NDVI was used as the vegetation index. Rainfall data also show at least one drought and one wet period from 1995 to 1999 (see figure 4), but there is no close association between rainfall variations and NDVI variations. This is because the rainfall station is located in a plain whereas most of the study area in the mountainous region and much of the precipitation occurs as snowfall in this basin. Therefore, there is no close association between green vegetation in the basin and rainfall at the single station. Furthermore, rainfall totals have been used, but the time distribution and rainfall intensities influence soil moisture, which affects plant growth and thus NDVI. Much water is lost by run-off in the hilly watershed when rainfall intensities are high, while snowmelt, which is an important source of soil moisture in spring, is poorly represented by total rainfall of a low-altitude station. Therefore, in our opinion, agricultural drought should be assessed by NDVI values rather than by rainfall data from a station that may not be representative for indication of the supply of soil moisture. 

A surprise was that spring NDVI was best predicted in terms of _R_<sup>2</sup> and RMSE when last spring NAO and SOI indices were used as input. Earlier research in this region 



<!-- Start of picture text -->
400<br>Annual rainfall<br>350<br>Average<br>300<br>250<br>200<br>150<br>100<br>50<br>0<br>Year<br>Rainfall (mm)<br>1982 1983 1984 1985 1986 1987 1988 1989 1990 1991 1992 1993 1994 1995 1996 1997 1998 1999<br><!-- End of picture text -->

Figure 4. Evolution of rainfall in Tabriz station (1982–2000). 

_A. Fatehi Marj and A. M. J. Meijerink_ 

9716 



<!-- Start of picture text -->
0.23<br>Observed<br>0.22 Predicted<br>0.21<br>0.20<br>0.19<br>0.18<br>0.17<br>0.16<br>0.15<br>1995 1996 1997 1998 1999<br>Year<br>NDVI<br><!-- End of picture text -->

Figure 5. Observed and predicted normalized difference vegetation index (NDVI) values (1995–1999). 

(Fatehi Marj _et al_ . 2006) showed that spring streamflow was affected by NAO and SOI indices pertaining to periods preceding spring streamflow. The result of forecasting is shown in figure 5. The result of training and testing with input of only one, two or three preceding seasons before spring is poor; the RMSE is more than 100 and _R_<sup>2</sup> is less than 0.1. 

Based on the existing data the average NDVI over the period of 18 years is 175 (figure 3). The NDVI for 1995–1999 is below that average. Comparison of predicted and observed NDVI values shows not much difference between the two. The determinant coefficient ( _R_<sup>2</sup> ) between observed and predicted NDVI values is 0.8 with an RMSE of 4, while the SD is 6. The difference between observed and predicted NDVI values is less than 1 SD. Vegetation, and thus NDVI, depends on rainfall, but rainfall of the station used and NDVI averaged over the observation pixels of NOAA-AVHRR in the subwatershed are not highly correlated. In this area, between spring rainfall and spring NDVI, _R_<sup>2</sup> is 0.64 and between winter rainfall and spring NDVI, _R_<sup>2</sup> is 0.45. However, the purpose of this research is long-term forecasting and the rainfalls of the same season and one preceding season were not used in the above forecast. Evaluation of the NM shows its validity for 19951999, but it remains unknown whether other drought (low NDVI) periods can be predicted. Because of this problem the MWM was applied to make a forecast for all years of the period 1982–1999 using 5-year forecasting periods. 

The result of MWM for forecasting is shown in figure 6 and table 1. Evaluation of MWM shows that the determinant coefficient ( _R_<sup>2</sup> ) between observed and predicted NDVI values is 0.79 and the RMSE is 0.015 for the period 1982–1999. Comparison of NDVI forecasting for dry and wet periods shows a somewhat higher correlation for wet periods ( _R_<sup>2</sup> = 0.82 and RMSE = 0.012) than for dry periods ( _R_<sup>2</sup> = 0.68 and RMSE = 0.018). The result shows that a good match was found between the predicted NDVI and the observed NDVI (see figure 6). The discrepancies between the two are less than 1 SD. In fact, this is a surprise because the predicted NDVI is based on climatic signals, NAO and SOI, which only indirectly affect the soil moisture conditions for vegetation growth in the study area. This result is important because of the relatively poor correlation between rainfall of the station used and NDVI. In other words, use of climatic signals to forecast rainfall in the study area may not be of direct relevance for agricultural drought. 

_Drought forecasting using satellite images_ 

9717 



<!-- Start of picture text -->
0.28<br>0.26<br>0.24 Observed Predicted<br>0.22<br>0.20<br>0.18<br>0.16<br>0.14<br>0.12<br>0.10<br>Year<br>NDVI<br>1981 1982 1983 1984 1985 1986 1987 1988 1989 1990 1991 1992 1993 1994 1995 1996 1997 1998 1999<br><!-- End of picture text -->

Figure 6. Observed and predicted normalized difference vegetation index (NDVI) using moving window method (MWM). 

Table 1. Observed and predicted NDVI. 

|Year|Observe|d|Predicted|Observed – Predicted|
|---|---|---|---|---|
|1981|0.20||0.17|0.02|
|1982|0.24||0.23|0.01|
|1983|0.22||0.22|0.00|
|1984|0.22||0.22|0.00|
|1985|0.21||0.21|0.00|
|1986|0.21||0.21|−0.01|
|1987|0.17||0.18|−0.02|
|1988|0.19||0.19|0.00|
|1989|0.21||0.21|0.00|
|1990|0.24||0.24|0.00|
|1991|0.22||0.22|0.00|
|1992|0.23||0.24|−0.01|
|1993|0.25||0.25|0.00|
|1994|0.27||0.24|0.03|
|1995|0.21||0.21|0.00|
|1996|0.21||0.22|−0.01|
|1997|0.22||0.22|0.00|
|1998|0.20||0.19|0.01|
|1999|0.18||0.17|0.00|
|||Average=0.22<br>SD=0.03<br>_R_<sup>2 </sup>=0.89<br>RMSE=0.011|||



Note: NDVI, normalized difference vegetation index; SD, standard deviation; _R_<sup>2</sup> , determinant coefficient; RMSE, root mean square error. 

### **6. Conclusions** 

A vegetation index based on a 10-day composite satellite data (NDVI) of the growing season May–July, considered to represent agricultural drought conditions, can be predicted in northwest Iran with 1-year lead time using the climatic signals represented by NAO and SOI. A good match was found for the investigated period 1981–1999. The NDVI represents the actual vegetation condition and is therefore an indicator of agricultural drought, much to be preferred over rainfall because of the relatively 

_A. Fatehi Marj and A. M. J. Meijerink_ 

9718 

poor correlation between rainfall data of the nearest station and NDVI. Moreover, the NDVI mapping by satellite covers the effects of temporal and spatial distributions of rainfall and snowmelt over the entire watershed. 

The forecast is possible if an ANN is trained with input of the two climatic signals pertaining to the preceding spring. Use of these climatic signals of other periods did not contribute to the NDVI forecast. 

### **Acknowledgements** 

The data used by the authors in this study include the data produced through funding from the Earth Observing System Pathfinder Program of NASA’s Mission to Planet Earth in cooperation with NOAA. The data were provided by the Earth Observing System Data and Information System, Distributed Active Archive Center at Goddard Space Flight Center, which archives, manages and distributes this dataset. We thank an anonymous reviewer and the editor for their critical and constructive remarks. 

### **References** 

- ANYAMBA, A., TUCKER, J. and EASTMAN, J.R., 2001, NDVI anomaly patterns over Africa during the 1997 _/_ 98 ENSO warm event. _International Journal of Remote Sensing_ , **22** , pp. 1847–1859. 

- BARET, F., 1991, Vegetation canopy reflectance: factors of variations and application to agriculture. In _Remote Sensing Applications and GIS for Resources Management in Developing Countries_ , A.S. Belward and C.R. Valenzuela (Eds.), pp. 145–168 (Dordrecht: Kluwer Academic Publishers). 

- BARTHOLOME, E., 1991, Remote sensing and agricultural production monitoring in Sahelian countries. In _Remote Sensing Applications and GIS for Resources Management in Developing Countries_ , A.S. Belward and C.R. Valenzuela (Eds.), pp. 189–214 (Dordrecht: Kluwer Academic Publishers). 

- BAYARJARGAL, YU., ADYASUREN, TS. and MUNKHTUYA, SH., 2007, Drought and vegetation monitoring in the arid and semi-arid regions of the Mongolia using remote sensing and ground data. _Journal of Natural Hazard_ , **40** , pp. 173–208. 

- BELL, G.D., CHANGNON, D.S., CHANNGNON, A., KOUSKY, V.E., PIELKE JR., V. and WILKINS, L., 2000, _El Nino 1997–1998, the Climate Event of the Century_ , pp. 136–150 (Oxford: Oxford University Press). 

- BHUIYAN, C., SINGH, R.P. and KOGAN, F.N., 2006, Monitoring drought dynamics in the Aravalli region (India) using different indices based on ground and remote sensing data. _International Journal of Applied Earth Observation and Geoinformation_ , **8** , pp. 289–302. 

- BRADBURY, J., DINGMAN, A.S.L. and KEIM, D., 2002, New England drought and relations with large scale atmospheric circulation pattern. _Journal of the American Water Resources Association_ , **38** , pp. 1287–1299. 

- CAMPOLO, M., SOLDAT, A. and ANDREUSSI, P., 2003, Artificial neural network approach to flood forecasting in the river Arno. _Hydrological Sciences_ , **48** , pp. 381–398. 

- CULEN, H.M. and DE MENOCAL, P.B., 2000, North Atlantic influence on Tigris-Euphrates streamflow. _International Journal of Climatology_ , **20** , pp. 853–863. 

- CULEN, H.M., KAPLAN, A., ARKIN, P.A. and MENOCAL, P.B., 2002, Impact of the North Atlantic Oscillation on middle eastern climate and streamflow. _Climatic Change_ , **55** , pp. 315–338. 

- DANH, N.T., PHIEN, H.N. and GUPTA, A.D., 1999, Neural network model for river flow forecasting. _Water South Africa (SA)_ , **25** , pp. 33–39. 

- FATEHI MARJ, A., DARIANE, A.B. and MAHDIAN, M.H., 2006, Impact of climatic signals on streamflow in Urmieh Lake Basin northwest of Iran. In _3rd International Conference_ 

_Drought forecasting using satellite images_ 

9719 

_on Water Resources in Mediterranean Basins_ , 1–3 November 2006, Lebanese University, Tripoli, Lebanon. 

GOWARD, S.N., TUCKER, C.J. and DYE, D.G., 1985, North American vegetation patterns observed with the NOAA-7 advanced very high resolution radiometer. _Vegetation_ , **64** , pp. 3–14. 

- GU, Y., BROWN, J.F., VERDIN, J.P. and WARDLOW, B., 2007, A five-year analysis of MODIS NDVI and NDWI for grassland drought assessment over the central Great Plains of the United States. _Geophysical Research Letters_ , **34** , L06407, pp. 25–35. 

- HUGHES, B.L. and SAUNDERS, A.M., 2001, Seasonal prediction of European spring precipitation from ENSO and local SST. _International Journal of Climatology_ , **14** , pp. 1–23. 

KARABULUT, M., 2003, An examination of relationships between vegetation and rainfall using maximum value composite AVHRR-NDVI data. _Turkish Journal of Botany_ , **27** , pp. 93–101. 

- KIM, T.W. and VALDES, J.B., 2003, A nonlinear model for drought forecasting based on conjunction of wavelet transforms and neural networks. _Journal of Hydrologic Engineering_ , **8** , pp. 19–28. 

- KOGAN, F.N., 1997, Global drought watch from space. _Bulletin of the American Meteorological Society_ , **78** , pp. 621–636. 

- LIU, W.T. and NEGRON, R.I., 2001, ENSO drought onset prediction in northeast Brazil using NDVI. _International Journal of Remote Sensing_ , **17** , pp. 3483–3501. 

- NAZEMOSADAT, M.J., SAMANI, N., BARRY, D.A. and MOLAII NIKO, M., 2006, ENSO the forcing on climate change in Iran, precipitation analysis. _Iranian Journal of Science and Technology, Transaction B-Engineering_ , **30** , pp. 555–565. 

- NICHOLSON, S.E., 2001, The relationship between El-Nino and drought. _Journal of Climate_ , **14** , pp. 323–335. 

- NICHOLSON, S.E., MICHAEL, L.D. and MALO, A.R., 1990, A comparison of the vegetation response to rainfall in the Sahel and East Africa using NDVI index from NOAA AVHRR. _Climatic Change_ , **17** , pp. 209–241. 

- RATANA, P., WATTANAKIJ, N. and MONGKOLSAWAT, C., 2007, Recent drought in NE Thailand: regional vegetation dynamics and NDVI-rainfall relationships. Center of Geo-informatics for the Development of Northeast Thailand, Khon Kaen University, Thailand. Available online at: http: _//_ gecnet.kku.ac.th _/_ research _/_ i_proceed _/_ i_2550. html. 

- REED, B.C., 1993, Using remote sensing and GIS for analyzing landscape _/_ drought interaction. _International Journal of Remote Sensing_ , **14** , pp. 3489–3503. 

- RICHARDS, A.J. and WIEGAND, C.L., 1977, Distinguishing vegetation from soil background information. _Photogrammetric Engineering & Remote Sensing_ , **43** , pp. 1541–1552. 

- ROUSE, J.W., HAAS, R.H., SCHELL, J.A. and DEERING, D.W., 1974, Monitoring vegetation systems in the Great Plains with ERTS. In _3rd ERTS_ -1 _Symposium_ , NASA SP-351, Washington, DC, pp. 309–317. 

- SHAMSELDIN, A.Y., 1997, Application of a neural network technique to rainfall-runoff modelling. _Journal of Hydrology_ , **199** , pp. 272–294. 

- SILVERMAN, D. and DRACUP, J.A., 2000, Artificial neural network and long range precipitation prediction in California. _Journal of Applied Meteorology_ , **31** , pp. 57–66. 

- TESHNELAB, M. and WATANABE, K., 1999, _Intelligent Control Based on Flexible Neural Network_ , pp. 74–76 (Dordrecht: Kluwer Academic Publishers). 

- TINGSANCHALI, T. and GAUTAM, M.R., 2000, Application of Tank, NAM, ARMA and neural network models to flood forecasting. _Hydrological Process_ , **14** , pp. 2473–2487. 

- TUCKER, C.J., 1979, Red and photographic infrared linear combination for monitoring vegetation. _Remote Sensing of Environment_ , **8** , pp. 127–150. 

- WALSH, J.S., 1987, Comparison of NOAA AVHRR data to meteorological drought indices. _Photogrammetric Engineering & Remote Sensing_ , **53** , pp. 1069–1074. 

