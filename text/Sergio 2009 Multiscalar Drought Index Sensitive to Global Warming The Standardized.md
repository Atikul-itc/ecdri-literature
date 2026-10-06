1696 

J O U R N A L O F C L I M A T E 

VOLUME 23 

# A Multiscalar Drought Index Sensitive to Global Warming: The Standardized Precipitation Evapotranspiration Index 

SERGIO M. VICENTE-SERRANO 

Instituto Pirenaico de Ecologı´a, Zaragoza, Spain 

SANTIAGO BEGUERI<sup>´</sup> A 

Estacio´ n Experimental de Aula Dei, Zaragoza, Spain 

JUAN I. LO<sup>´</sup> PEZ-MORENO 

Instituto Pirenaico de Ecologı´a, Zaragoza, Spain 

(Manuscript received 28 October 2008, in final form 6 October 2009) 

### ABSTRACT 

The authors propose a new climatic drought index: the standardized precipitation evapotranspiration index (SPEI). The SPEI is based on precipitation and temperature data, and it has the advantage of combining multiscalar character with the capacity to include the effects of temperature variability on drought assessment. The procedure to calculate the index is detailed and involves a climatic water balance, the accumulation of deficit/surplus at different time scales, and adjustment to a log-logistic probability distribution. Mathematically, the SPEI is similar to the standardized precipitation index (SPI), but it includes the role of temperature. Because the SPEI is based on a water balance, it can be compared to the self-calibrated Palmer drought severity index (sc-PDSI). Time series of the three indices were compared for a set of observatories with different climate characteristics, located in different parts of the world. Under global warming conditions, only the sc-PDSI and SPEI identified an increase in drought severity associated with higher water demand as a result of evapotranspiration. Relative to the sc-PDSI, the SPEI has the advantage of being multiscalar, which is crucial for drought analysis and monitoring. 

## 1. Introduction 

Drought is one of the main natural causes of agricultural, economic, and environmental damage (Burton et al. 1978; Wilhite and Glantz 1985; Wilhite 1993). Droughts are apparent after a long period without precipitation, but it is difficult to determine their onset, extent, and end. Thus, it is very difficult to objectively quantify their characteristics in terms of intensity, magnitude, duration, and spatial extent. For this reason, much effort has been devoted to developing techniques for drought analysis and monitoring. Among these, objective indices are the most widely used, but subjectivity in the definition of drought has made it very difficult to establish a unique and universal drought index (Heim 2002). A 

Corresponding author address: Sergio M. Vicente-Serrano, Avda. Montan˜ana 1004, P.O. Box 13034, Zaragoza 50080, Spain. E-mail: svicen@ipe.csic.es 

number of indices were developed during the twentieth century for drought quantification, monitoring, and analysis (Du Pisani et al. 1998; Heim 2002; Keyantash and Dracup 2002). 

In recent years, there have been many attempts to develop new drought indices, or to improve existing ones (Gonza´lez and Valde´s 2006; Keyantash and Dracup 2004; Wells et al. 2004; Tsakiris et al. 2007). Most studies related to drought analysis and monitoring systems have been conducted using either 1) the Palmer drought severity index (PDSI; Palmer 1965), based on a soil water balance equation, or 2) the standardized precipitation index (SPI; McKee et al. 1993), based on a precipitation probabilistic approach. 

The PDSI was a landmark in the development of drought indices. It enables measurement of both wetness (positive value) and dryness (negative values), based on the supply and demand concept of the water balance equation, and thus it incorporates prior precipitation, 

DOI: 10.1175/2009JCLI2909.1 

� 2010 American Meteorological Society 

Unauthenticated | Downloaded 10/06/26 05:05 AM UTC 

1697 

1 APRIL 2010 

V I C E N T E - S E R R A N O E T A L . 

moisture supply, runoff, and evaporation demand at the surface level. The calculation procedure has been explained in a number of studies (e.g., Karl 1983, 1986; Alley 1984). Nevertheless, the PDSI has several deficiencies (Alley 1984; Karl 1986; Soule´ 1992; Akinremi et al. 1996; Weber and Nkemdirim 1998), including the strong influence of calibration period, its limited utility in areas other than that used for calibration, problems in spatial comparability, and subjectivity in relating drought conditions to the values of the index. Many of these problems were solved by development of the selfcalibrated PDSI (sc-PDSI; Wells et al. 2004), which is spatially comparable and reports extreme wet and dry events at frequencies expected for rare conditions. Nevertheless, the main shortcoming of the PDSI has not been resolved. This relates to its fixed temporal scale (between 9 and 12 months) and an autoregressive characteristic, whereby index values are affected by the conditions up to four years in the past (Guttman 1998). 

It is commonly accepted that drought is a multiscalar phenomenon. McKee et al. (1993) clearly illustrated this essential characteristic of droughts through the consideration of usable water resources, including soil moisture, groundwater, snowpack, river discharges, and reservoir storages. The period from the arrival of water inputs to availability of a given usable resource differs considerably. Thus, the time scale over which water deficits accumulate becomes extremely important, and it functionally separates hydrological, environmental, agricultural, and other droughts. For example, the response of hydrological systems to precipitation can vary markedly as a function of time (Changnon and Easterling 1989; Elfatih et al. 1999; Pandey and Ramasastri 2001). This is determined by the different frequencies of hydrologic/climatic variables (Skøien et al. 2003). For this reason, drought indices must be associated with a specific time scale to be useful for monitoring and managing different usable water resources. This explains the wide acceptance of the SPI, which is comparable in time and space (Guttman 1998; Hayes et al. 1999), and it can be calculated at different time scales to monitor droughts with respect to different usable water resources. A number of studies have demonstrated variation in response of the SPI to soil moisture, river discharge, reservoir storage, vegetation activity, crop production, and piezometric fluctuations at different time scales (e.g., Szalai et al. 2000; Sims et al. 2002; Ji and Peters 2003; Vicente-Serrano and Lo´pez-Moreno 2005; VicenteSerrano et al. 2006; Patel et al. 2007; Vicente-Serrano 2007; Khan et al. 2008). 

The main criticism of the SPI is that its calculation is based only on precipitation data. The index does not consider other variables that can influence droughts, such as temperature, evapotranspiration, wind speed, and soil 

water holding capacity. Nevertheless, several studies have shown that precipitation is the main variable determining the onset, duration, intensity, and end of droughts (Chang and Cleopa 1991; Heim 2002). Thus, the SPI is highly correlated with the PDSI at time scales of 6–12 months (Lloyd-Hughes and Saunders 2002; Redmond 2002). Low data requirements and simplicity explain the wide use of precipitation-based indices, such as the SPI, for drought monitoring and analysis. 

Precipitation-based drought indices, including the SPI, rely on two assumptions: 1) the variability of precipitation is much higher than that of other variables, such as temperature and potential evapotranspiration (PET), and 2) the other variables are stationary (i.e., they have no temporal trend). In this scenario, the importance of these other variables is negligible, and droughts are controlled by the temporal variability in precipitation. However, some authors have warned against systematically neglecting the importance of the effect of temperature on drought conditions. For example, Hu and Willson (2000) assessed the role of precipitation and temperature in the PDSI and found that the index responded equally to changes of similar magnitude in both variables. Only where the temperature fluctuation was smaller than that of precipitation was variability in the PDSI controlled by precipitation. 

Empirical studies have shown that temperature rise markedly affects the severity of droughts. For example, Abramopoulos et al. (1988) used a general circulation model experiment to show that evaporation and transpiration can consume up to 80% of rainfall. In addition, they found that the efficiency of drying resulting from temperature anomalies is as high as that due to rainfall shortage. The role of temperature was evident in the devastating central European drought during the summer of 2003. Although previous precipitation was lower than normal, the extremely high temperatures over most of Europe during June and July (more than 48C above the average) caused the greatest damage to cultivated and natural systems, and dramatically increased evapotranspiration rates and water stress (Rebetez et al. 2006). Some studies have also found that the PDSI explains the variability in crop production and the activity of natural vegetation better than the SPI (Mavromatis 2007; Kempes et al. 2008). 

There has been a general temperature increase (0.58– 28C) during the last 150 years (Jones and Moberg 2003), and climate change models predict a marked increase during the twenty-first century (Solomon et al. 2007). It is expected that this will have dramatic consequences for drought conditions, with an increase in water demand as a result of evapotranspiration (Sheffield and Wood 2008). Dubrovsky et al. (2008) recently showed that the 

Unauthenticated | Downloaded 10/06/26 05:05 AM UTC 

1698 

J O U R N A L O F C L I M A T E 

VOLUME 23 

drought effects of warming predicted by global climate models can be clearly seen in the PDSI, whereas the SPI (which is based only on precipitation data) does not reflect expected changes in drought conditions. 

Therefore, the use of drought indices that include temperature data in their formulation (such as the PDSI) is preferable, especially for applications involving future climate scenarios. However, the PDSI lacks the multiscalar character essential for both assessing drought in relation to different hydrological systems and differentiating among different drought types. We therefore formulated a new drought index—the standardized precipitation evapotranspiration index (SPEI)—based on precipitation and PET. The SPEI combines the sensitivity of PDSI to changes in evaporation demand (caused by temperature fluctuations and trends) with the simplicity of calculation and the multitemporal nature of the SPI. The new index is particularly suited to detecting, monitoring, and exploring the consequences of global warming on drought conditions. 

## 2. Problem overview 

As an illustrative example, Fig. 1 shows the evolution of the sc-PDSI and the SPI at different time scales from 1910 to 2007 at the Indore observatory (India). The scPDSI was devised by Wells et al. (2004) to address the shortcomings of the PDSI. We used the software developed by Wells (2003) for calculations (available online at http://greenleaf.unl.edu/downloads). The time series of monthly precipitation and monthly-mean temperature were obtained from the Global Historical Climatology Network (GHCN-monthly) database (available online at http://www.ncdc.noaa.gov/oa/climate/ghcn-monthly/). The water field capacity at Indore, which was needed to derive the sc-PDSI, was obtained from a global digital format dataset of water holding capacity, described by Webb et al. (1993). The SPI was calculated according to a Pearson III distribution and the L-moment method to obtain the distribution parameters, following VicenteSerrano (2006). Figure 1 shows that the sc-PDSI has a unique time scale, in which the longest and most severe droughts were recorded in the decades 1910, 1920, 1950, 1960, and 2000. These episodes are also clearly identified by the SPI at long time scales (12–24 months). This provides evidence about the suitability of identifying and monitoring droughts using an index that only considers precipitation data. Moreover, this example shows the advantage of the SPI over the sc-PDSI, since the different time scales over which the SPI can be calculated allow for the identification of different drought types. At the shortest time scales, the drought series show a high frequency of drought and moist periods of 

short duration. In contrast, at the longest time scales, the drought periods are of longer duration and lower frequency. Thus, short time scales are mainly related to soil water content and river discharge in headwater areas, medium time scales are related to reservoir storages and discharge in the medium course of the rivers, and long time scales are related to variations in groundwater storage. Therefore, different time scales are useful for monitoring drought conditions in different hydrological subsystems. 

Climatic change processes result in two main predictions with implications for the duration and magnitude of droughts (Solomon et al. 2007): 1) precipitation will decrease in some regions, and 2) an increase in global temperature, which will be more intense in the Northern Hemisphere, will cause an increase in the evapotranspiration rate. 

A reduction in precipitation due to climate change will affect the severity of droughts. Current climate change A2 scenarios for the end of the twenty-first century (Solomon et al. 2007) show a maximum reduction of 15% in total precipitation in some regions. The influence of a reduction in precipitation on future drought conditions is identified by both the sc-PDSI and the SPI. Figure 2 shows the evolution of the sc-PDSI and the 18-month SPI at Albuquerque between 1910 and 2007. Both indices were calculated using a hypothetical progressive precipitation decrease of 15% during this period. Both the modeled SPI and sc-PDSI series showed an increase in the duration and magnitude of droughts at the end of the century relative to the series computed with real data. As a consequence of the precipitation decrease, droughts recorded in the decades of 1970–2000 increased in maximum intensity, total magnitude, and duration. In contrast, the humid periods showed the opposite behavior. Therefore, both indices have the capacity to record changes in droughts related to changes in precipitation. 

However, climate change scenarios also show a temperature increase during the twentieth century. In some cases, such as the A2 greenhouse gas emissions scenario, the models predict a temperature increase that might exceed 48C with respect to the 1960–90 average (Solomon et al. 2007). This increase will have consequences for drought conditions, which are clearly identified by the PDSI (Mavromatis 2007; Dubrovsky et al. 2008). Figure 3 shows the evolution of the sc-PDSI in Albuquerque, computed with real data between 1910 and 2007, but it also considers a progressive increase of 28–48C in the mean temperature series. The differences between the scPDSI using real data and the two modeled series are also shown. This simple experiment clearly shows an increase in the duration and magnitude of droughts at the end of 

Unauthenticated | Downloaded 10/06/26 05:05 AM UTC 

1699 

1 APRIL 2010 

V I C E N T E - S E R R A N O E T A L . 



FIG. 1. The sc-PDSI and 3-, 6-, 12-, 18-, and 24-month SPIs at the Indore observatory (1910–2007). 

the century, which is directly related to the temperature increase. A similar pattern could not be identified using the SPI, demonstrating the shortcomings of this widespread index in addressing the consequences of climate change. 

## 3. Methodology 

We describe here a simple multiscalar drought index (the SPEI) that combines precipitation and temperature data. The SPEI is very easy to calculate, and it is based on 

the original SPI calculation procedure. The SPI is calculated using monthly (or weekly) precipitation as the input data. The SPEI uses the monthly (or weekly) difference between precipitation and PET. This represents a simple climatic water balance (Thornthwaite 1948) that is calculated at different time scales to obtain the SPEI. 

The first step, the calculation of the PET, is difficult because of the involvement of numerous parameters, including surface temperature, air humidity, soil incoming radiation, water vapor pressure, and ground–atmosphere latent and sensible heat fluxes (Allen et al. 1998). 

Unauthenticated | Downloaded 10/06/26 05:05 AM UTC 

1700 

J O U R N A L O F C L I M A T E 

VOLUME 23 



FIG. 2. PDSI and 18-month SPI at the Albuquerque observatory (1910–2007). Both indices were calculated from precipitation series containing a progressive reduction of 15% between 1910 and 2007. The difference between the indices is also shown. 

Different methods have been proposed to indirectly estimate the PET from meteorological parameters measured at weather stations. According to data availability, such methods include physically based methods (e.g., the Penman–Monteith method; PM) and models based on empirical relationships, where PET is calculated with fewer data requirements. The PM method has been adopted by the International Commission on Irrigation and Drainage (ICID), the Food and Agriculture Organization of the United Nations (FAO), and the Ameri- 

can Society of Civil Engineers (ASCE) as the standard procedure for computing PET. The PM method requires large amounts of data because its calculation involves values for solar radiation, temperature, wind speed, and relative humidity. In the majority of regions of the world, these meteorological data are not available. Accordingly, alternative empirical equations have been proposed for PET calculation where data are scarce (Allen et al. 1998). Although some methods in general provide better results than others for PET quantification (Droogers and Allen 

Unauthenticated | Downloaded 10/06/26 05:05 AM UTC 

1701 

1 APRIL 2010 

V I C E N T E - S E R R A N O E T A L . 



FIG. 3. Evolution of the sc-PDSI at the Albuquerque observatory between 1910 and 2007, and under progressive temperature increase scenarios of 28 and 48C during the same period. The difference between the indices is also shown. 

2002), the purpose of including PET in the drought index calculation is to obtain a relative temporal estimation, and therefore the method used to calculate the PET is not critical. Mavromatis (2007) recently showed that the use of simple or complex methods to calculate the PET provides similar results when a drought index, such as the PDSI, is calculated. Therefore, we followed the simplest approach to calculate PET (Thornthwaite 1948), which has the advantage of only requiring data on monthly-mean temperature. Following this method, the monthly PET (mm) is obtained by 



where T is the monthly-mean temperature (8C); I is a heat index, which is calculated as the sum of 12 monthly 

index values i, the latter being derived from meanmonthly temperature using the formula 



m is a coefficient depending on I: m 5 6.75 3 10<sup>27</sup> I<sup>3</sup> 2 7.71 3 10<sup>25</sup> I<sup>2</sup> 1 1.79 3 10<sup>22</sup> I 1 0.492; and K is a correction coefficient computed as a function of the latitude and month, 



Here NDM is the number of days of the month and N is the maximum number of sun hours, which is calculated using 

Unauthenticated | Downloaded 10/06/26 05:05 AM UTC 

1702 

J O U R N A L O F C L I M A T E 

VOLUME 23 

the gamma distribution, a three-parameter distribution is needed to calculate the SPEI. In two-parameter distributions, the variable x has a lower boundary of zero (0 . x , ‘), whereas in three-parameter distributions, x can take values in the range (g . x , ‘), where g is the parameter of origin of the distribution; consequently, x can have negative values, which are common in D series. 



where -s is the hourly angle of sun rising, which is calculated using 



We tested the most suitable distribution to model the Di values calculated at different time scales. For this purpose, L-moment ratio diagrams were used because they allow for comparison of the empirical frequency distribution of D series computed at different time scales with a number of theoretical distributions (Hosking 1990). The L moments are analogous to conventional central moments, but they are able to characterize a wider range of distribution functions and are more robust in relation to outliers in the data. 

where u is the latitude in radians and d is the solar declination in radians, calculated using 



where J is the average Julian day of the month. 

With a value for PET, the difference between the precipitation P and PET for the month i is calculated using 

To create the L-moment ratio diagrams, L-moment ratios (L skewness t3 and L kurtosis t4) must be calculated. Here t3 and t4 are calculated as follows: 



which provides a simple measure of the water surplus or deficit for the analyzed month. Tsakiris et al. (2007) proposed the ratio of P to PET as a suitable parameter for obtaining a drought index that accounts for global warming processes. This approach has some shortcomings: the parameter is not defined when PET 5 0 (which is common in many regions of the world during winter), and the P/PET quotient reduces dramatically the range of variability and deemphasizes the role of temperature in droughts. 



where l2, l3, and l4 are the L moments of the D series, obtained from probability-weighted moments (PWMs) using the formulas 

The calculated Di values are aggregated at different time scales, following the same procedure as that for the SPI. The difference D<sup>k</sup> i, j<sup>inagivenmonthjandyeari</sup> depends on the chosen time scale k. For example, the accumulated difference for one month in a particular year i with a 12-month time scale is calculated using 







The PWMs of order s are calculated as 

where Fi is a frequency estimator calculated following the approach of Hosking (1990): 

where Di,l is the P 2 PET difference in the first month of year i, in millimeters. 

For calculation of the SPI at different time scales, a probability distribution of the gamma family is used (the two-parameter gamma or three-parameter Pearson III distributions), because the frequencies of precipitation accumulated at different time scales are well modeled using these statistical distributions. Although the SPI can be calculated using a two-parameter distribution, such as 



where i is the range of observations arranged in increasing order and N is the number of data points. The values for t3 and t4 were calculated from the D series of 11 observatories between 1910 and 2007 in different 

Unauthenticated | Downloaded 10/06/26 05:05 AM UTC 

1703 

1 APRIL 2010 

V I C E N T E - S E R R A N O E T A L . 



FIG. 4. Location of the 11 observatories used in the study. 

regions of the world, under varying conditions that included tropical (Tampa, Florida; Sa˜o Paulo, Brazil), monsoon (Indore), Mediterranean (Valencia, Spain), semiarid (Albuquerque), continental (Wien, Austria), cold (Punta Arenas, Chile), and oceanic (Abashiri, Japan) climates (Fig. 4). The dataset was obtained from the GHCNmonthly database. 

Figure 5 shows the L-moment diagrams for the D series, accumulated for time scales of 3 and 18 months for the 11 selected observatories. For each observatory 12 points are shown, each corresponding to a 1-month series. The empirical L-moment ratios for the analyzed D series at different time scales could be adjusted by different candidate distributions (e.g., Pearson III, lognormal, general extreme value, log-logistic) because the empirical statistics oscillate around these curves. According to the Kolmogorov–Smirnoff test, none of these 

four distributions can be rejected in the different monthly series and time scales for the 11 observatories analyzed. Figure 6 shows the curves of the four distributions and the empirical frequencies for the D series calculated at the time scales of 1, 3, 6, 12, 18, and 24 months for the Albuquerque observatory. It is evident that the four distributions adapt well to the empirical frequencies of the D series, independently of the time scale analyzed. Figure 7 shows the modeled accumulated probabilities F(x) for the Albuquerque observatory for time scales of 1, 6, 12, and 24 months, using the four distributions and the empirical cumulative probabilities. This figure shows the high degree of similarity among the four curves. Independently of the probability distribution selected, the modeled F(x) values adjust very well to the empirical probabilities. This was also observed for the other analyzed observatories. Therefore, selecting the most suitable distribution to 



FIG. 5. L-moment ratio diagrams for D series calculated at the time scales of 3 and 18 months. The theoretical L-moment ratios for different distributions are shown, as are the empirical values obtained from the monthly series at each observatory. 

Unauthenticated | Downloaded 10/06/26 05:05 AM UTC 

1704 

J O U R N A L O F C L I M A T E 

VOLUME 23 



FIG. 6. Empirical and modeled f(x) values using the Pearson III, log-logistic, lognormal and general extreme values distributions of the D series at the time scales of 1, 3, 6, 12, 18, and 24 months at the Albuquerque observatory. 

model the D series is difficult, given the similarity among the four distributions. Therefore, we based our selection on the behavior at the most extreme values. Given the marked decrease in the curves that adjust the lower values for the Pearson III, lognormal and general extreme value distributions, we found extremely low cumulative probabilities for very low values corresponding to fewer than 1 occurrence in 1 000 000 years, mainly at the shortest time scales. Also, in some cases we found values of D that were below the origin parameter of the distribution, which implies that f(x) and F(x) cannot be defined for these values. In contrast, the log-logistic distribution showed a more gradual decrease in the curve for low values, and more coherent probabilities were obtained for very low values of D, corresponding to 1 occurrence in 200–500 years. Additionally, no values were found below the origin parameter of the distribution. These results suggested the selection of the log-logistic distribution for standardizing the D series to obtain the SPEI. 

The probability density function of a three-parameter log-logistic distributed variable is expressed as 



where a, b, and g are scale, shape, and origin parameters, respectively, for D values in the range (g . D , ‘). 

Parameters of the log-logistic distribution can be obtained following different procedures. Among them, the L-moment procedure is the most robust and easy approach (Ahmad et al. 1988). When L moments are calculated, the parameters of the Pearson III distribution can be obtained following Singh et al. (1993): 



where G(b) is the gamma function of b. 

The log-logistic distribution adapted very well to the D series for all time scales. Figure 8 shows the probability density functions for the log-logistic distribution obtained from the D series at different time scales for the Albuquerque observatory. The log-logistic distribution can account for negative values, and it is capable of adopting different shapes to model the frequencies of the D series at different time scales. 

The probability distribution function of the D series, according to the log-logistic distribution, is given by 

Unauthenticated | Downloaded 10/06/26 05:05 AM UTC 

1705 

1 APRIL 2010 

V I C E N T E - S E R R A N O E T A L . 



FIG. 7. Empirical vs modeled F(x) values from Pearson III, log-logistic, lognormal and general extreme value distributions for D series at time scales of 1, 6, 12, and 24 months at the Albuquerque observatory. 



The F(x) values for the D series at different time scales adapt very well to the empirical F(x) values at the different observatories, independently of the climate characteristics and the time scale of the analysis. Figure 9 shows an example of the results for the 3- and 12-month series of Albuquerque; Sa˜o Paulo; and Helsinki, Finland, but similar observations were made for the other observatories and time scales. This demonstrates the suitability of the log-logistic distribution to model F(x) values from the D series in any region of the world. 

With F(x) the SPEI can easily be obtained as the standardized values of F(x). For example, following the classical approximation of Abramowitz and Stegun (1965), 



where 



and P is the probability of exceeding a determined D value, P 5 1 2 F(x). If P . 0.5, then P is replaced by 1 2 P and the sign of the resultant SPEI is reversed. The constants are C0 5 2.515517, C1 5 0.802853, C2 5 0.010328, d1 5 1.432788, d2 5 0.189269, and d3 5 0.001308. 



FIG. 8. Probability density functions of the log-logistic distribution for D series calculated at different time scales at the Albuquerque observatory. 

Unauthenticated | Downloaded 10/06/26 05:05 AM UTC 

1706 

J O U R N A L O F C L I M A T E 

VOLUME 23 



FIG. 9. Theoretical values according the log-logistic distribution (black line) vs empirical (dots) F(x) values for D series at time scales of 3 and 12 months for the Albuquerque, Sa˜o Paulo, and Helsinki observatories. 

The average value of SPEI is 0, and the standard deviation is 1. The SPEI is a standardized variable, and it can therefore be compared with other SPEI values over time and space. An SPEI of 0 indicates a value corresponding to 50% of the cumulative probability of D, according to a log-logistic distribution. 

## 4. Results 

## a. Current climatic conditions 

Figure 10 shows the sc-PDSI, and the 3-, 12- and 24monthly SPIs and SPEIs for Helsinki between 1910 and 2007. According to the sc-PDSI, the main drought epi- 

sodes occurred in the decades of 1930, 1940, 1970, and 2000. These droughts are also clearly identified by the SPI and the SPEI. Few differences were apparent between the SPI and the SPEI series, independently of the time scale of analysis. This result shows that under climate conditions in which low interannual variability of temperature dominates, both drought indices respond mainly to the variability in precipitation. Figure 11 shows the results for the Sa˜o Paulo observatory, in which the sc-PDSI identified drought episodes in the decades of 1910, 1920, 1960, and 2000. In contrast, these episodes were not clearly evident with the SPI, especially at longer time scales. Thus, the SPI identified droughts in the 

Unauthenticated | Downloaded 10/06/26 05:05 AM UTC 

1707 

1 APRIL 2010 

V I C E N T E - S E R R A N O E T A L . 



FIG. 10. The sc-PDSI; 3-, 12- and 24-month SPI; and SPEI at the Helsinki observatory (1910–2007). 

decades of 1910, 1950, and 1960 but not the long and severe drought of 2000. In contrast, the SPEI identified all four drought periods. The mean temperature increased markedly at Sa˜o Paulo between 1910 and 2007 (0.298C decade<sup>21</sup> ), and this increase would have produced a higher water demand by PET at the end of the century. This would have affected drought severity, which was clearly recorded by sc-PDSI in the decade of 2000. The role of a temperature increase on drought conditions was not recognized using the precipitation-based SPI drought index, but it was identified for the 2000 drought using the SPEI index. 

Figure 12 shows the correlation between the 191022007 series for sc-PDSI and the 1- to 24-monthly SPI and SPEI for each of the observatories shown in Fig. 4. As indicated 

in previous reports, there is strong agreement between the sc-PDSI and the SPI, with maximum values that oscillate between 0.6 and 0.85 at time scales between 5 and 24 months. A similar result was found for the SPEI; although, in general, the correlations increased with respect to the SPI, mainly for observatories affected by warming processes during the twentieth century, including Valencia (0.328C decade<sup>21</sup> ), Albuquerque (0.28C decade<sup>21</sup> ), and Sa˜o Paulo. The correlation between the SPI and the SPEI was high for the different series, independently of the time scale analyzed; the exceptions were Valencia and Albuquerque, where correlations decreased at the longest time scales. These results are in agreement with the hypothesis that the main explanatory variable for droughts is precipitation. 



FIG. 11. Same as Fig. 10 but at Sa˜o Paulo observatory (1910–2007). 

Unauthenticated | Downloaded 10/06/26 05:05 AM UTC 

1708 

J O U R N A L O F C L I M A T E 

VOLUME 23 



FIG. 12. Correlation between the 1910–2007 series for the sc-PDSI, and 1–24-month SPI and SPEI at the 11 analyzed observatories. 

Therefore, under the current climate conditions inclusion of a variable to quantify PET in the SPEI and the sc-PDSI does not provide much additional information. This is particularly obvious at those observatories where the evolution of temperature was stationary during the analysis period. However, some of the results presented in Fig. 12 indicate that this hypothesis may not hold over long time scales under global warming conditions, since differences were found between the SPI and the SPEI for the three observatories where temperature increased over the analysis period. 

## b. Global warming effects 

In the two scenarios (i.e., temperature increases of 28 and 48C), the D series obtained at the 11 observatories showed a similar statistical behavior to that observed under real climate conditions. Figure 13 shows the L-moment ratio diagrams for the D series at the same 11 observatories, but with the addition of a progressive temperature increase of 28 and 48C between 1910 and 2007, in relation to the original series from which the PET was calculated. The L-moment ratio diagrams show small changes from those obtained for the original series. The 

empirical L-moment ratios show that the log-logistic distribution is also suitable to model the D series at the various observatories, independent of the time scale involved and the magnitude of the temperature increase. Therefore, global warming does not affect the choice of model for determining the SPEI. The modeled F(x) values from the log-logistic distribution also showed a good fitting of the empirical F(x) values under a temperature increase of 28 and 48C at the various observatories, independently of the region of the world analyzed (Fig. 14). 

Figure 15 shows the evolution of the sc-PDSI obtained using the original and the modeled series for the Valencia observatory. The 18-month SPI and SPEI obtained with that series are also shown. Using the original data, the scPDSI identified the most important droughts in the decades of 1990 and 2000. With a progressive temperature increase of 28 and 48C, the droughts increased in magnitude and duration at the end of the century. The SPI did not identify those severe droughts associated with a marked temperature increase, and it did not take into account the role of increased temperature in reinforcing drought conditions, as was shown by the sc-PDSI. In 

Unauthenticated | Downloaded 10/06/26 05:05 AM UTC 

1709 

1 APRIL 2010 

V I C E N T E - S E R R A N O E T A L . 



FIG. 13. L-moment ratio diagrams for the D series calculated at the time scales of 3 and 18 months. Progressive temperature increase of (a) 28 and (b) 48C. The theoretical L-moment ratios for different distributions are shown, as are the empirical values obtained from the monthly series at each observatory. 

contrast, the main drought episodes were identified by the SPEI, with similar evolution to that observed for the sc-PDSI. Moreover, if temperature increased progressively by 28 or 48C, the reinforcement of drought severity associated with higher water demand by PET was readily identified by the SPEI, with the time series showing a high similarity to the sc-PDSI observed under warming scenarios. The same pattern was observed for the other analyzed observatories. Figure 16 shows the evolution at the Abashiri observatory, where no increase in temperature occurred during the 191022007 period. The SPI and SPEI series were similar, both identifying the main drought episodes in the decades of 1920, 1950, 1980, 1990, and 2000. There was also a high degree of similarity with the sc-PDSI series during the same period. If the temperature was increased by 28 and 48C during the same period, then the sc-PDSI showed reinforcement of drought severity at the end of the century. This was also observed with the SPEI. Therefore, the sc-PDSI and SPEI series were similar under the simulated warming conditions. 

Thus, under the progressive temperature increase predicted by current climate change models, the relationship 

between the sc-PDSI and the SPI was dramatically reduced. Figure 17 shows the correlations between the scPDSI, the SPI, and the SPEI under the two considered scenarios of a temperature increase. With a temperature increase of 28C, the correlation coefficients between the sc-PDSI and the SPI decreased noticeably in comparison to the sc-PDSI calculated from the original series. The correlation values for the original series were 0.6520.80 for the various observatories. Under a scenario of 28C temperature increase, the correlation values decreased to 0.52–0.75. However, the correlations between the scPDSI and the SPEI for a temperature increase of 28C were similar and higher than that calculated using the original series. This implies that the SPEI also accounts for the effect of warming processes on drought severity. In contrast, the correlation values between the SPI and the SPEI decreased noticeably under a scenario of a 28C temperature increase. This occurred mainly at the longest time scales, where deficits due to PET accumulate, and also in the observatories located in tropical (Sa˜o Paulo, Indore), Mediterranean (Valencia, Kimberley), and semiarid (Albuquerque, Lahore) climates. In these 

Unauthenticated | Downloaded 10/06/26 05:05 AM UTC 

1710 

J O U R N A L O F C L I M A T E 

VOLUME 23 



FIG. 14. Same as Fig. 9. Temperature increase of (a) 28 and (b) 48C. 

regions of high mean temperature, an additional temperature increase of 28C would markedly increase water losses by PET. In cold areas (e.g., Abashiri and Helsinki), the relationship between SPI and SPEI under a scenario of a 28C temperature increase did not change noticeably in relation to the original series, since PET would remain relatively low. 

With a temperature increase of 48C (Fig. 17b), the correlation between the sc-PDSI and the SPI decreased even more than for a 28C increase (0.4020.70), whereas the correlation between the sc-PDSI and the SPEI remained generally unchanged. At some observatories, values were higher than the indices calculated from the temperature series and for a temperature increase of 28C. With a temperature increase of 48C, the correlations between SPI and SPEI decreased markedly for the majority of observatories, particularly those located in warm climates. This suggests that if precipitation does not change from the present conditions, temperature will play a major role in determining future drought severity. 

Intensification of drought severity due to global warming is correctly identified by the sc-PDSI, which is based on a complex and reliable water balance widely accepted by the scientific community. Our results confirm that the 

increase in water demand as a result of PET in a global change context will affect the future occurrence, intensity, and magnitude of droughts. This suggests that the SPI is suboptimal for the analysis and monitoring of droughts under a warming scenario. However, given the fixed time scale of the sc-PDSI, the SPEI offers advantages because it provides similar patterns to that of the sc-PDSI; however, it accounts for different time scales, which is essential for the monitoring of different drought types and assessment of the potential effect of droughts on different usable water sources. Figure 18 compares the SPEI and the sc-PDSI under a 48C temperature increase scenario throughout the analysis period at the Tampa observatory. Under this warming scenario, the sc-PDSI shows quasi-continuous drought conditions between 1970 and 2000, with some minor humid periods. The persistent drought conditions during this period are also clearly identified by the SPEI, independent of the analysis time scale. Thus, the sc-PDSI provides the same information as the SPEI at time scales of 7–10 months (correlation R values between 0.850 and 0.857), but Fig. 18 clearly shows that the SPEI also provides information about drought conditions at shorter and longer time scales. 

Unauthenticated | Downloaded 10/06/26 05:05 AM UTC 

1711 

1 APRIL 2010 

V I C E N T E - S E R R A N O E T A L . 



FIG. 15. Evolution of the sc-PDSI, and 18-month SPI and SPEI at the Valencia observatory. The original series (1910–2007) and the sc-PDSI and SPEI were calculated for a temperature series with a progressive increase of 28 and 48C throughout the analyzed period. 

Unauthenticated | Downloaded 10/06/26 05:05 AM UTC 

1712 

J O U R N A L O F C L I M A T E 

VOLUME 23 



FIG. 16. Same as Fig. 15 but at the Abashiri observatory. 

5. Discussion and conclusions 

We have described a multiscalar drought index (the standardized precipitation evapotranspiration index; 

SPEI) that uses precipitation and temperature data and is based on a normalization of the simple water balance developed by Thornthwaite (1948). We assessed the properties and advantages of this index in comparison 

Unauthenticated | Downloaded 10/06/26 05:05 AM UTC 

1713 

1 APRIL 2010 

V I C E N T E - S E R R A N O E T A L . 



<!-- Start of picture text -->
FIG. 17. Same as Fig. 12. Temperature<br>increase of (a) 28 and (b) 48C.<br><!-- End of picture text -->

Unauthenticated | Downloaded 10/06/26 05:05 AM UTC 

1714 

J O U R N A L O F C L I M A T E 

VOLUME 23 



FIG. 18. Evolution of the sc-PDSI, and 1-, 3-, 6-, 12-, 18-, and 24-month SPEI at the Tampa observatory under a 48C temperature increase scenario relative to the origin. 

to the two most widely used drought indices: the selfcalibrated Palmer drought severity index (sc-PDSI) and the standardized precipitation index (SPI). A multiscalar drought index is needed to take into account defi- 

cits that affect different usable water sources and to distinguish different types of drought. This has been demonstrated in a number of studies that have shown how different usable water sources respond to the different 

Unauthenticated | Downloaded 10/06/26 05:05 AM UTC 

1715 

1 APRIL 2010 

V I C E N T E - S E R R A N O E T A L . 

time scales of a drought index (e.g., Szalai et al. 2000; Vicente-Serrano and Lo´ pez-Moreno 2005; VicenteSerrano 2007). 

Under climatic conditions with low temporal variability in temperature, the SPI is superior to the sc-PDSI, since it identifies different drought types because of its multiscalar character. Both indices have the capacity to identify an intensification of drought severity related to reduced precipitation in a climatic change context. Both indices similarly record the effect of a reduction in precipitation on the drought index. Nevertheless, we have demonstrated that global warming processes predicted by GCMs (Solomon et al. 2007) have important implications for evapotranspiration processes, increasing the influence of this parameter on drought severity. We have shown that this is readily identified by the PDSI, in line with recent results of Dubrovsky et al. (2008), but this behavior is not well recorded by the SPI, given the unique use of precipitation data in its calculation. 

There is some scientific debate about which climate parameters (e.g., precipitation, temperature, evapotranspiration, wind speed, relative humidity, solar radiation, etc.) are the most important in determining drought severity. There is general agreement on the importance of precipitation in explaining drought variability and the need to include this variable in the calculation of any drought index. However, inclusion of a variable that accounts for climatic water demand (such as evapotranspiration) is not always accepted, since its role in drought conditions is not well understood or it is underestimated. Various studies have shown that precipitation is the major variable defining the duration, magnitude, and intensity of droughts (Alley 1984; Chang and Cleopa 1991). Oladipo (1985) compared different drought indices and concluded that indices using only precipitation data provided the best option for identifying climatic droughts. Nevertheless, Hu and Willson (2000) demonstrated that evapotranspiration plays a major role in explaining drought variability in drought indices based on soil water balances, such as the PDSI, and that this is comparable to the role of precipitation under some circumstances. It is not well understood how evapotranspiration processes can affect different usable water resources and how the different time scales can determine water deficits. However, it is widely recognized that evapotranspiration determines soil moisture variability and, consequently, vegetation water content, which directly affects agricultural droughts commonly recorded using short time-scale drought indices. Thus, drought indices that only use evapotranspiration data to monitor agricultural droughts have shown better results than precipitation-based drought indices (Narasimhan and Srinivasan 2005). Soil water losses due to evapotranspiration will also affect runoff, and these deficits 

will affect river discharge and groundwater storage. However, PET can also cause large losses from water bodies, such as reservoirs (Wafa and Labib 1973; Snoussi et al. 2002), which commonly have a low temporal inertia and are well monitored by long time-scale drought indices (Szalai et al. 2000; Vicente-Serrano and Lo´pez-Moreno 2005). Therefore, although it is very complex to determine the influence of evapotranspiration on drought conditions, it seems reasonable to include this variable in the calculation of a drought index. The need for this increases under increasing temperature conditions and also because the role of different climate parameters in explaining water resource availability is not constant in space. For example, Syed et al. (2008) have shown that precipitation dominates terrestrial water storage variation in the tropics, but evapotranspiration is most effective in explaining the variability at midlatitudes. 

Where temporal trends in temperature are not apparent, we found little difference between the values obtained using a precipitation drought index, such as the SPI, and other indices that include PET values, such as the sc-PDSI and the SPEI. Given that drought is considered an abnormal water deficit with respect to average conditions, the onset, duration, and severity of drought could be determined from precipitation data. The inclusion of PET to calculate the SPEI only affects the index when PET differs from average conditions, for example, under global warming scenarios. The same pattern has been observed in the sc-PDSI. 

We detailed the procedure for calculating the SPEI. This is based on the method used to calculate the SPI but with modifications to include PET. The log-logistic distribution was chosen to model D (P 2 PET) values, and the resulting cumulative probabilities were transformed into a standardized variable. The distribution adapted very well to climate regions with different characteristics, independently of the time scale used to compute the deficits. Therefore, the log-logistic distribution was used to calculate the SPEI, whereas the Pearson III or gamma distributions were used to calculate the SPI. Only when the index was computed at short time scales for some few very low precipitation PET values (mainly arid locations with a highly variable climatology) were any problems experienced. These problems were minor and already known for SPI calculations when the twoparameter gamma distribution is used (Wu et al. 2007). However, the use of three-parameter distributions to calculate the SPEI reduced this problem noticeably. 

We showed that under warming climate conditions, the sc-PDSI decreases markedly, indicating more frequent and severe droughts. Thus, according to the sc-PDSI, temperature could play an important role in explaining drought conditions under global warming. This is consistent 

Unauthenticated | Downloaded 10/06/26 05:05 AM UTC 

1716 

J O U R N A L O F C L I M A T E 

VOLUME 23 

with the results of a number of studies that show an increase in future drought severity caused by a temperature increase (Beniston et al. 2007; Sheffield and Wood 2008). The increase in severity will be proportional to the magnitude of the temperature change, and in some regions, the observed temperature increase over the past century has already had an effect on the sc-PDSI values. This phenomenon can also be assessed using the SPEI, which was very similar to the sc-PDSI under the two temperature increase scenarios tested. This suggests that the SPEI should be used in preference to the sc-PDSI, given the former index’s simplicity, lower data requirements, and multiscalar properties. 

The SPI cannot identify the role of a temperature increase in future drought conditions, and independently of global warming scenarios, it cannot account for the influence of temperature variability and the role of heat waves, such as that which affected central Europe in 2003. The SPEI can account for the possible effects of temperature variability and temperature extremes beyond the context of global warming. Therefore, given the minor additional data requirements of the SPEI relative to the SPI, use of the former is preferable for the identification, analysis, and monitoring of droughts in any climate region of the world. 

In summary, the SPEI fulfills the requirements of a drought index, as indicated by Nkemdirim and Weber (1999), since its multiscalar character enables it to be used by different scientific disciplines to detect, monitor, and analyze droughts. Like the sc-PDSI and the SPI, the SPEI can measure drought severity according to its intensity and duration, and it can identify the onset and end of drought episodes. The SPEI allows for comparison of drought severity through time and space, since it can be calculated over a wide range of climates, as can the SPI. Moreover, Keyantash and Dracup (2002) indicated that drought indices must be statistically robust and easily calculated and have a clear and comprehensible calculation procedure. All these requirements are met by the SPEI. However, a crucial advantage of the SPEI over the most widely used drought indices that consider the effect of PET on drought severity is that its multiscalar characteristics enable identification of different drought types and effects in the context of global warming. 

Software has been created to automatically calculate the SPEI over a wide range of time scales. The software is freely available in the Web repository of the Spanish National Research Council (available online at http:// digital.csic.es/handle/10261/10002). 

Acknowledgments. This work has been supported by the research projects CGL2006-11619/HID, CGL200801189/BTE, and CGL2008-1083/CLI, financed by the 

Spanish Commission of Science and Technology and FEDER; EUROGEOSS (FP7-ENV-2008-1-226487) and ACQWA (FP7-ENV-2007-1-212250), financed by the VII Framework Programme of the European Commission; ‘‘Las sequı´as clima´ticas en la cuenca del Ebro y su respuesta hidrolo´gica’’ and ‘‘La nieve en el Pirineo Aragone´s: Distribucio´n espacial y su respuesta a las condiciones clima´ticas,’’ financed by ‘‘Obra Social La Caixa’’ and the Arago´n government; and the ‘‘Programa de grupos de investigacio´n consolidados,’’ financed by the Arago´n government. 

### REFERENCES 

- Abramopoulos, F., C. Rosenzweig, and B. Choudhury, 1988: Improved ground hydrology calculations for global climate models (GCMs): Soil water movement and evapotranspiration. J. Climate, 1, 921–941. 

- Abramowitz, M., and I. A. Stegun, 1965: Handbook of Mathematical Functions, with Formulas, Graphs, and Mathematical Tables. Dover Publications, 1046 pp. 

- Ahmad, M. I., C. D. Sinclair, and A. Werritty, 1988: Log-logistic flood frequency analysis. J. Hydrol., 98, 205–224. 

- Akinremi, O. O., S. M. McGinn, and A. G. Barr, 1996: Evaluation of the Palmer drought index on the Canadian prairies. J. Climate, 9, 897–905. 

- Allen, R. G., L. S. Pereira, D. Raes, and M. Smith, 1998: Crop evapotranspiration: Guidelines for computing crop water requirements. FAO Irrigation and Drainage Paper 56, 300 pp. 

- Alley, W. M., 1984: The Palmer drought severity index: Limitations and applications. J. Appl. Meteor., 23, 1100–1109. 

- Beniston, M., and Coauthors, 2007: Future extreme events in European climate: An exploration of regional climate model projections. Climatic Change, 81 (Suppl. 1), 71–95. 

- Burton, I., R. W. Kates, and G. F. White, 1978: The Environment as Hazard. Oxford University Press, 240 pp. 

- Chang, T. J., and X. A. Cleopa, 1991: A proposed method for drought monitoring. Water Resour. Bull., 27, 275–281. 

- Changnon, S. A., and W. E. Easterling, 1989: Measuring drought impacts: The Illinois case. Water Resour. Bull., 25, 27–42. 

- Droogers, P., and R. G. Allen, 2002: Estimating reference evapotranspiration under inaccurate data conditions. Irrig. Drain. Syst., 16, 33–45. 

- Dubrovsky, M., M. D. Svoboda, M. Trnka, M. J. Hayes, D. A. Wilhite, Z. Zalud, and P. Hlavinka, 2008: Application of relative drought indices in assessing climate-change impacts on drought conditions in Czechia. Theor. Appl. Climatol., 96, 155–171. 

- Du Pisani, C. G., H. J. Fouche´, and J. C. Venter, 1998: Assessing rangeland drought in South Africa. Agric. Syst., 57, 367–380. 

- Elfatih, A., B. Eltahir, and P. J. F. Yeh, 1999: On the asymmetric response of aquifer water level to floods and droughts in Illinois. Water Resour. Res., 35, 1199–1217. 

- Gonza´lez, J., and J. B. Valde´s, 2006: New drought frequency index: Definition and comparative performance analysis. Water Resour. Res., 42, W11421, doi:10.1029/2005WR004308. 

- Guttman, N. B., 1998: Comparing the Palmer Drought Index and the Standardized Precipitation Index. J. Amer. Water Resour. Assoc., 34, 113–121. 

Unauthenticated | Downloaded 10/06/26 05:05 AM UTC 

1717 

1 APRIL 2010 

V I C E N T E - S E R R A N O E T A L . 

- Hayes, M., D. A. Wilhite, M. Svoboda, and O. Vanyarkho, 1999: Monitoring the 1996 drought using the standardized precipitation index. Bull. Amer. Meteor. Soc., 80, 429–438. 

- Heim, R. R., 2002: A review of twentieth-century drought indices used in the United States. Bull. Amer. Meteor. Soc., 83, 1149– 1165. 

- Hosking, J. R. M., 1990: L-Moments: Analysis and estimation of distributions using linear combinations of order statistics. J. Roy. Stat. Soc., 52B, 105–124. 

- Hu, Q., and G. D. Willson, 2000: Effect of temperature anomalies on the Palmer drought severity index in the central United States. Int. J. Climatol., 20, 1899–1911. 

- Ji, L., and A. J. Peters, 2003: Assessing vegetation response to drought in the northern Great Plains using vegetation and drought indices. Remote Sens. Environ., 87, 85–98. 

- Jones, P. D., and A. Moberg, 2003: Hemispheric and large-scale surface air temperature variations: An extensive revision and an update to 2001. J. Climate, 16, 206–223. 

- Karl, T. R., 1983: Some spatial characteristics of drought duration in the United States. J. Climate Appl. Meteor., 22, 1356–1366. 

- ——, 1986: The sensitivity of the Palmer drought severity index and Palmer’s Z-index to their calibration coefficients including potential evapotranspiration. J. Climate Appl. Meteor., 25, 77–86. 

- Kempes, C. P., O. B. Myers, D. D. Breshears, and J. J. Ebersole, 2008: Comparing response of Pinus edulis tree-ring growth to five alternate moisture indices using historic meteorological data. J. Arid Environ., 72, 350–357. 

- Keyantash, J. A., and J. A. Dracup, 2002: The quantification of drought: An evaluation of drought indices. Bull. Amer. Meteor. Soc., 83, 1167–1180. 

- ——, and ——, 2004: An aggregate drought index: Assessing drought severity based on fluctuations in the hydrologic cycle and surface water storage. Water Resour. Res., 40, W09304, doi:10.1029/2003WR002610. 

- Khan, S., H. F. Gabriel, and T. Rana, 2008: Standard precipitation index to track drought and assess impact of rainfall on watertables in irrigation areas. Irrig. Drain. Syst., 22, 159–177. 

- Lloyd-Hughes, B., and M. A. Saunders, 2002: A drought climatology for Europe. Int. J. Climatol., 22, 1571–1592. 

- Mavromatis, T., 2007: Drought index evaluation for assessing fu- 

ture wheat production in Greece. Int. J. Climatol., 27, 911–924. McKee, T. B., N. J. Doesken, and J. Kleist, 1993: The relationship of drought frequency and duration to time scales. Preprints, Eighth Conf. on Applied Climatology. Anaheim, CA, Amer. Meteor. Soc., 179–184. 

- Narasimhan, B., and R. Srinivasan, 2005: Development and evaluation of Soil Moisture Deficit Index (SMDI) and Evapotranspiration Deficit Index (ETDI) for agricultural drought monitoring. Agric. For. Meteor., 133, 69–88. 

- Nkemdirim, L., and L. Weber, 1999: Comparison between the droughts of the 1930s and the 1980s in the southern prairies of Canada. J. Climate, 12, 2434–2450. 

- Oladipo, E. O., 1985: A comparative performance analysis of three 

meteorological drought indices. J. Climatol., 5, 655–664. Palmer, W. C., 1965: Meteorological droughts. U.S. Department of Commerce, Weather Bureau Research Paper 45, 58 pp. 

- Pandey, R. P., and K. S. Ramasastri, 2001: Relationship between the common climatic parameters and average drought frequency. Hydrol. Processes, 15, 1019–1032. 

- Patel, N. R., P. Chopra, and V. K. Dadhwal, 2007: Analyzing spatial patterns of meteorological drought using standardized precipitation index. Meteor. Appl., 14, 329–336. 

- Rebetez, M., H. Mayer, O. Dupont, D. Schindler, K. Gartner, J. P. Kropp, and A. Menzel, 2006: Heat and drought 2003 in Europe: A climate synthesis. Ann. For. Sci., 63, 569–577. 

- Redmond, K. T., 2002: The depiction of drought. Bull. Amer. Meteor. Soc., 83, 1143–1147. 

- Sheffield, J., and E. F. Wood, 2008: Projected changes in drought occurrence under future global warming from multi-model, multi-scenario, IPCC AR4 simulations. Climate Dyn., 31, 79–105. 

- Sims, A. P., D. dutta, S. Nigoyi, and S. Raman, 2002: Adopting drought indices for estimating soil moisture: A North Carolina case study. Geophys. Res. Lett., 29, 1183, doi:10.1029/ 2001GL013343. 

- Singh, V. P., H. Guo, and F. X. Yu, 1993: Parameter estimation for 3-parameter log-logistic distribution (LLD3) by Pome. Stochastic Hydrol. Hydraul., 7, 163–177. 

- Skøien, J. O., G. Blo¨schl, and A. W. Western, 2003: Characteristic space scales and timescales in hydrology. Water Resour. Res., 39, 1304, doi:10.1029/2002WR001736. 

- Snoussi, M., S. Haı¨da, and S. Imassi, 2002: Effects of the construction of dams on the water and sediment fluxes of the Moulouya and the Sebou Rivers, Morocco. Reg. Environ. Change, 3, 5–12. 

- Solomon, S., D. Qin, M. Manning, M. Marquis, K. Averyt, M. M. B. Tignor, H. L. Miller Jr., and Z. Chen, Eds., 2007: Climate Change 2007: The Physical Science Basis. Cambridge University Press, 996 pp. 

- Soule´, P. T., 1992: Spatial patterns of drought frequency and duration in the contiguous USA based on multiple drought event definitions. Int. J. Climatol., 12, 11–24. 

- Syed, T. H., J. S. Famiglietti, M. Rodell, J. Chen, and C. R. Wilson, 2008: Analysis of terrestrial water storage changes from GRACE and GLDAS. Water Resour. Res., 44, W02433, doi:10.1029/2006WR005779. 

- Szalai, S., Cs. Szinell, and J. Zoboki, 2000: Drought monitoring in Hungary. Early Warning Systems for Drought Preparedness and Drought Management, World Meteorological Organization Rep. WMO/TD 1037, 182–199. 

- Thornthwaite, C. W., 1948: An approach toward a rational classification of climate. Geogr. Rev., 38, 55–94. 

- Tsakiris, G., D. Pangalou, and H. Vangelis, 2007: Regional drought assessment based on the Reconnaissance Drought Index (RDI). Water Resour. Manage., 21, 821–833. 

- Vicente-Serrano, S. M., 2006: Differences in spatial patterns of drought on different time scales: An analysis of the Iberian Peninsula. Water Resour. Manage., 20, 37–60. 

- ——, 2007: Evaluating the Impact of Drought Using Remote Sensing in a Mediterranean, Semi-arid Region. Nat. Hazards, 40, 173–208. 

- ——, and J. I. Lo´ pez-Moreno, 2005: Hydrological response to different time scales of climatological drought: An evaluation of the standardized precipitation index in a mountainous Mediterranean basin. Hydrol. Earth Syst. Sci., 9, 523–533. 

- ——, J. M. Cuadrat-Prats, and A. Romo, 2006: Early prediction of crop productions using drought indices at different time-scales and remote sensing data: Application in the Ebro Valley (north-east Spain). Int. J. Remote Sens., 27, 511–518. 

- Wafa, T. A., and A. H. Labib, 1973: Seepage losses from Lake Nasser. Man-Made Lakes: Their Problems and Environmental Effects, Geophys. Monogr., Vol. 17, Amer. Geophys. Union, 287–291. 

Unauthenticated | Downloaded 10/06/26 05:05 AM UTC 

1718 

J O U R N A L O F C L I M A T E 

VOLUME 23 

- Webb, R. S., C. E. Rosenzweig, and E. R. Levine, 1993: Specifying land surface characteristics in general circulation models: Soil profile data set and derived water-holding capacities. Global Biogeochem. Cycles, 7, 97–108. 

- Weber, L., and L. C. Nkemdirim, 1998: The Palmer drought severity index revisited. Geogr. Ann., 80A, 153–172. 

- Wells, N., 2003: PDSI Users Manual Version 2.0. National Agricultural Decision Support System, University of Nebraska– Lincoln, 17 pp. [Available online at http://greenleaf.unl.edu/ downloads/PDSI_Manual.pdf.] 

- ——, S. Goddard, and M. J. Hayes, 2004: A self-calibrating Palmer drought severity index. J. Climate, 17, 2335–2351. 

- Wilhite, D. A., 1993: Drought Assessment, Management, and Planning: Theory and Case Studies. Natural Resource Management and Policy Series, Vol. 2, Kluwer, 293 pp. 

- ——, and M. H. Glantz, 1985: Understanding the drought phenomenon: The role of definitions. Water Int., 10, 111–120. 

- Wu, H., M. D. Svoboda, M. J. Hayes, D. A. Wilhite, and F. Wen, 2007: Appropriate application of the Standardized Precipitation Index in arid locations and dry seasons. Int. J. Climatol., 27, 65–79. 

Unauthenticated | Downloaded 10/06/26 05:05 AM UTC 

