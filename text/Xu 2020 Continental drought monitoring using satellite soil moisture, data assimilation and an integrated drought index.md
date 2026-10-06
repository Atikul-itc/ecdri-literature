Remote Sensing of Environment 250 (2020) 112028 



Contents lists available at ScienceDirect 

# Remote Sensing of Environment 

journal homepage: www.elsevier.com/locate/rse 



## Continental drought monitoring using satellite soil moisture, data assimilation and an integrated drought index 



<!-- Start of picture text -->
T<br><!-- End of picture text -->

### Lei Xu<sup>a,b</sup> , Peyman Abbaszadeh<sup>a</sup> , Hamid Moradkhani<sup>a,⁎</sup> , Nengcheng Chen<sup>b,c</sup> , Xiang Zhang<sup>b</sup> 

> a Center for Complex Hydrosystems Research, Department of Civil, Construction and Environmental Engineering, The University of Alabama, USA 

> b State Key Laboratory of Information Engineering in Surveying, Mapping, and Remote Sensing, Wuhan University, Wuhan 430079, China 

> c Collaborative Innovation Center of Geospatial Technology, Wuhan 430079, China 

|A R T I C L E I N F O|A B S T R A C T|
|---|---|
|Keywords:<br>Data assimilation<br>Particle filter<br>|Satellite remote sensing provides unprecedented information on near-surface soil moisture at a global scale,<br>enabling a wide range of studies such as drought monitoring and forecasting. Data Assimilation (DA) has been<br>recognized as an effective means to incorporate such observations into hydrologic models to better predict and|
|Soil moisture<br>Drought monitoring<br>Land surface model|forecast hydroclimatic variables. In this study, we use a recently developed Evolutionary Particle Filter with<br>Markov Chain Monte Carlo (EPFM) approach to assimilate Soil Moisture Active Passive (SMAP) soil moisture<br>data into Variable Infiltration Capacity (VIC) hydrologic model to provide more reliable topsoil layer moisture<br>(0~–5 cm) over the entire Continental United States (CONUS). The EPFM outperformed an Ensemble Kalman<br>filter (EnKF) in terms of correlations and the unbiased root mean square error (ubRMSE) with in situ mea-<br>surements from the Soil Climate Analysis Network (SCAN) and the United States Climate Reference Network<br>(USCRN). Also, we used a multivariate probability distribution based on a Copula function to integrate the<br>posterior soil moisture, precipitation (from the North American Land Data Assimilation System (NLDAS)) and<br>evapotranspiration (from the Moderate Resolution Imaging Spectroradiometer (MODIS)) information to develop<br>a new integrated drought index, i.e. SPESMI. To validate the usefulness of the developed integrated drought<br>index, we compared the drought events detected by this index with those reported by the United States Drought<br>Monitor (USDM). The results indicated a strong temporal consistency of the drought areas detected by our<br>approach and the USDM over the entire period of study (April 2015 to June 2018). In addition to such promising<br>results, we noticed that our approach could capture theflash drought in 2017 in the U.S. Northern Plains earlier<br>than the USDM, and could identify some severe to extreme drought events that had been underestimated by the<br>USDM. Moreover, the SPESMI has a high correlation with the yield loss of spring and winter wheat in the United<br>States. This novel drought monitoring framework can serve as an independent and potentially complementary<br>drought monitoring system.|



#### 1. Introduction 

Soil moisture is a key hydrologic variable that significantly influences the global water cycle despite its small volume (McColl et al., 2017). Accurate soil moisture estimation is vital for agricultural drought monitoring (Narasimhan and Srinivasan, 2005), vegetation growth (D'Odorico et al., 2007) and water resources management (Dobriyal et al., 2012). The ongoing climate change is causing more extreme weather (Huang et al., 2016; Samaniego et al., 2018; Schlaepfer et al., 2017), posing great risk of floods and droughts for agriculture (Xu et al., 2019a). Prolonged and severe droughts have occurred in many areas of the globe (Mann and Gleick, 2015; Qiu, 2010; Spinoni et al., 2015), causing enormous socioeconomic losses, 

especially during the crop growing season. Therefore, accurate water content monitoring is needed to estimate crop drought stress and water demand to provide early warning of agricultural drought in order to reduce crop production loss. Soil moisture is an important indicator of water content beneath the land surface and can be used to estimate agricultural drought conditions through observations or model simulations. 

Satellite remote sensing provides the ability to monitor soil moisture over a large spatial scale (Ahmadalipour et al., 2017; Bolten et al., 2009; Wang and Qu, 2007), which is practically and logistically unachievable from in-situ observation networks. The Soil Moisture Active Passive (SMAP) (Entekhabi et al., 2010) mission, developed by the National Aeronautics and Space Administration (NASA), measures 

> ⁎ Corresponding author. 

E-mail address: hmoradkhani@ua.edu (H. Moradkhani). 

https://doi.org/10.1016/j.rse.2020.112028 Received 4 March 2020; Received in revised form 29 July 2020; Accepted 1 August 2020 Available online 21 August 2020 0034-4257/ © 2020 Elsevier Inc. All rights reserved. 

_Remote Sensing of Environment 250 (2020) 112028_ 

L. Xu, et al. 

global land surface soil moisture fields derived from the L-band radiances with a revisit frequency of 2–3 days. Although in-situ sensors provide continuous soil moisture measurements at multiple soil depths, they are only available at certain locations and are not suitable for large-scale studies. These networks are most often used for validation of satellite retrievals. Remotely sensed soil moisture observations are achievable everywhere on the land surface, ideal for a wide range of large-scale hydroclimate applications (Abbaszadeh et al., 2019b; Dong et al., 2019), such as drought monitoring (in particular, agricultural drought). A limitation of satellite data is its daily spatial coverage that is limited due to its revisit cycle. Another limitation of the satellite soil moisture retrieval is its consideration of the surface layer (0-5 cm) only. Model simulations can provide spatiotemporally continuous estimations of soil moisture. The soil moisture simulations from land surface models (LSMs) and global hydrological models (GHMs) are widely used in water resources planning, drought monitoring, flood warning and hydrological forecasts (Mujumdar and Kumar, 2012; Srivastava et al., 2013; Xu et al., 2018; Xu et al., 2019b; Yan et al., 2017). Hydrologic model simulations are most often erroneous and biased as the model is subject to different sources of uncertainties, including forcing data, parameters, model structural, initial and boundary condition uncertainties (Abbaszadeh et al., 2019a; Moradkhani et al., 2018). 

Data assimilation (DA) is recognized as an effective means to integrate model state variables with its corresponding observations to improve model simulations and forecasts. The ensemble Kalman filter (EnKF) (Evensen, 1994) is a commonly used DA method to incorporate satellite observations into a hydrological model. Despite the widespread use of this assimilation technique in hydrologic studies, the method is subject to some inherent limitations that result in sub-optimal model performance (Abbaszadeh et al., 2018; DeChant and Moradkhani, 2012; Yan et al., 2018). As an alternative to EnKF, the Particle Filter (PF) has garnered increasing attention in the hydrologic community over the last decade mainly due to its advantage in preserving the water balance and relaxing the Gaussian assumptions of model and observation errors (Dong et al., 2016; Pathiraja et al., 2018; Yan et al., 2018). For satellite soil moisture (e.g., SMAP) assimilation, the majority of studies have used the EnKF algorithm (Blankenship et al., 2018; Kolassa et al., 2017; Lievens et al., 2017; Reichle et al., 2019) and a few utilized PF (Lu et al., 2019; Lu et al., 2017b). This is mainly attributed to the computational complexity of PF at the continental scale. Therefore, it is necessary to fill this gap and examine the extent to which the PF based assimilation of satellite soil moisture would improve the skill of drought monitoring compared to traditional use of the EnKF approach. 

Drought happens in the United States (U.S.) each year at different places, causing widespread risk in crop yield loss, wildfires, forest insects and diseases, tree mortality and biodiversity reduction (Anderegg et al., 2015; Clark et al., 2016; Kolb et al., 2016; Littell et al., 2016; Lu et al., 2017a; Westerling and Swetnam, 2003). Continuous and accurate drought monitoring can help mitigate the socioeconomic impacts. For example, daily monitoring of crop drought stress can tell the farmers the current condition of crop water scarcity. If a specific crop is in severe drought condition, irrigation is needed to meet the crop water demand to reduce crop production loss. Therefore, drought monitoring provides the water scarcity information for farmers to adopt some measures in order to mitigate the drought impacts. In drought monitoring, drought index is commonly calculated to represent the drought condition based on one or more relevant variables, such as the standardized soil moisture index (SSMI) (AghaKouchak, 2014), the soil water deficit index (SWDI) (Mishra et al., 2017) and the US Drought Monitor (USDM) (Svoboda et al., 2002). The univariate drought index is well suited to monitor a specific drought type for a specific sector, such as the soil moisture drought for agriculture, while the multivariate drought index is useful in detecting multiple drought information simultaneously. SSMI is a standardized drought index based on parametric or non-parametric probability distribution of soil moisture over a long-term climatology. SWDI quantifies drought conditions by 

considering volumetric soil moisture content at available water capacity (AWC), field capacity (FC) and wilting point. USDM is an integrated drought index considering the information from precipitation, temperature, soil moisture, streamflow and local observations. Despite its widespread use in reporting the drought condition across the U.S., the USDM exhibits some disadvantages, including the fact that it is slow to detect emerging drought conditions (Sivakumar and Motha, 2008; Yan et al., 2018). This deficiency may be attributed to the involved variables or indices in the USDM that do not coincide with each other. USDM considers different types of drought to quantify an overall drought condition by combining meteorological drought, agricultural drought and hydrological drought. These drought types have different responses to drought in time (Wang et al., 2016). Generally, meteorological drought happens first due to abnormal precipitation and high evapotranspiration (ET), and then propagates to agricultural drought and hydrological drought. Using a unique drought index to capture comprehensive drought information is important for overall water scarcity evaluation regionally. Therefore, developing a multivariate drought index to represent different drought information is invaluable for regional water resources planning. Although the multivariate Standardized Precipitation Evapotranspiration Index (SPEI) (VicenteSerrano et al., 2010) considers precipitation and potential evapotranspiration (PET) which are widely used in drought assessment, it is a meteorological drought index that does not provide any insight on soil moisture and hydrological drought information. Therefore, it is vital to take soil moisture into account while studying drought as it represents water content in the land surface and is a key indicator of surface and subsurface water storage. 

In this study, we aim to develop a multivariate drought index by incorporating precipitation, PET and soil moisture to provide continuous drought monitoring over the CONUS. The spatiotemporally continuous soil moisture is obtained by assimilating SMAP soil moisture observations into Variable Infiltration Capacity (VIC) hydrological model using a recently developed data assimilation method, i.e. the Evolutionary Particle Filter with Markov Chain Monte Carlo (EPFM) (Abbaszadeh et al., 2018). The EPFM is compared with the EnKF as the most commonly used DA algorithm through multiple performance measures to demonstrate the advantage of the former. The posterior soil moisture is then used to develop a new drought index together with precipitation and PET using copula function. The skill of drought monitoring based on our newly developed drought index is compared with that of USDM to investigate its fidelity. The spring wheat and winter wheat crops in the U.S. are also used to examine the correlation of their yield losses and the integrated drought index to further demonstrate the usefulness of the integrated drought index. 

#### 2. Study area and data 

#### 2.1. Study area and the in-situ soil moisture stations 

This study is conducted over the CONUS (Fig. 1). In 2015, approximately 28.7% of the CONUS experienced moderate to exceptional drought according to USDM, causing tremendous drop in crop production and socioeconomic losses with billions of dollars in damage. Therefore, it is important to monitor and track drought evolution which helps in mitigation planning and minimizing negative consequences. There are a limited number of in-situ soil moisture stations that can be used for drought monitoring over the CONUS. The Soil Climate Analysis Network (SCAN) (Schaefer et al., 2007) soil moisture stations and the United States Climate Reference Network (USCRN) (Bell et al., 2013) stations are widely used to validate the satellite soil moisture data, although in-situ networks are not representative of the soil moisture within the satellite footprint (i.e., 20–50 km grid cell). Sparse networks of pointwise in situ measurements such as SCAN and USCRN suffer from representativeness errors but they can capture a large range of biomes and climate conditions. A total of 189 SCAN stations and 134 USCRN 

2 

_Remote Sensing of Environment 250 (2020) 112028_ 

L. Xu, et al. 



Fig. 1. A demonstration of the study area and used soil moisture stations. 

stations are used for validation of assimilated soil moisture. Furthermore, it was decided to use a densely observed site, which better represents the soil moisture in the grid cell. Therefore, in this study, we chose the Walnut Gulch Watershed (WGW) located in southeastern Arizona (Goodrich et al., 2008). Within this watershed, 19 soil moisture stations are available for hydrological monitoring. This watershed has an area of 150 km<sup>2</sup> and is a part of the upper San Pedro River Basin. WGW is an experimental watershed which is usually used for validation of satellite retrievals. The main land use in this watershed is grass, shrubs, trees and built-up areas. The measurement depth of in-situ soil moisture stations ranges from 5 cm to 100 cm. The depth nearest to model simulations (usually 10 cm) is used for validation. The hourly SCAN and USCRN data and the half-hourly soil moisture data in the WGW are aggregated to daily resolution to compare with model simulations. 

Sentinel as a replacement of its active radar sensor to produce an activepassive high-resolution soil moisture data at 1-km and 3-km (Das et al., 2016). The SMAP/Sentinel-1 L2 Radiometer/Radar soil moisture dataset (Das et al., 2018) has been recently released although it has not undergone validation process yet. In this study, we used SMAP 36-km soil moisture data to assimilate it into the VIC hydrological model in order to provide more accurate soil moisture estimates spatiotemporally across the entire CONUS. The SMAP soil moisture observations at both ascending and descending orbits are averaged to obtain the daily soil moisture data from April 1st 2015 to June 30th 2018. The 36-km SMAP soil moisture data are resampled to 25-km using the bilinear interpolation in order to be consistent with the VIC hydrologic model spatial resolution. 

#### 2.3. Precipitation and potential evapotranspiration 

#### 2.2. SMAP soil moisture 

SMAP satellite (Entekhabi et al., 2010), using its L-band microwave sensor, currently provides soil moisture at the top 5 cm soil layer with 36-km spatial resolution. This satellite was initially designed to provide soil moisture at 3-km resolution through its radar and radiometer sensors. Unfortunately, due to the failure of the radar instrument on July 7, 2015, since then the radiometer sensor has been the only operational instrument, of the satellite providing soil moisture data at the resolution of 36-km. The SMAP soil moisture data has been extensively validated against several core validation sites (Chan et al., 2016; Colliander et al., 2017) and the results showed that it meets the satellite retrieval accuracy of 0.04 m<sup>3</sup> /m<sup>3</sup> . The SMAP team planned to use 

The precipitation data are obtained from the North American Land Data Assimilation System (NLDAS) version 2 (Mitchell et al., 2004; Xia et al., 2012) forcing, which is a temporal disaggregation of a gauge-only Climate Prediction Center (CPC) analysis of daily precipitation after an orographic adjustment. Here, the hourly precipitation data with a spatial resolution of 12.5-km are aggregated into 25-km. The PET data are retrieved from the Moderate Resolution Imaging Spectroradiometer (MODIS) 8-day level 4 global 500 m product. The MODIS PET data are downloaded from January 1st 2001 to December 31st 2018 and are aggregated to 25-km. To calculate weekly drought index, precipitation data are aggregated into a weekly time scale and the 8-day MODIS PET data are also processed onto a weekly scale by nearest interpolation. 

3 

_Remote Sensing of Environment 250 (2020) 112028_ 

L. Xu, et al. 



Fig. 2. The proposed framework for drought monitoring using a multivariate drought index. 

#### 2.4. Crop yield data 

The spring and winter wheat crops in the U.S. are used to calculate the correlation between yield loss and drought indices. The annual crop yield data from 2001 to 2018, cropland data layer in year 2010 (Liu et al., 2004) and crop calendar data are obtained from the U.S. Department of Agriculture (USDA) National Agricultural Statistics Service (USDA-NASS, 2018). The national crop yield statistics are collected from the USDA (https://www.nass.usda.gov/index.php). This repository also provides the spatial map of crop planted area. As it is obtained from national survey report, the crop yield data is a national average of specific crop types, not limited to several sites. The countylevel spatial crop yield map can be obtained from USDA. The crop yield data are de-trended by a second order polynomial regression model (Lu et al., 2017a). The correlation coefficient is calculated between the yearly crop yield loss over the cultivated areas and the averaged drought index during the crop growing season. 

#### 3. Methodology 

Fig. 2 illustrates the proposed framework in this study for drought monitoring. A new multivariate drought index (hereafter SPESMI) is developed based on the precipitation, MODIS PET and the posterior soil moisture. The posterior soil moisture is obtained through assimilating the SMAP soil moisture observations into VIC model. The assimilation process is performed using the recently developed EPFM approach (Abbaszadeh et al., 2018). The EPFM is an assimilation technique that utilizes Markov Chain Monte Carlo (MCMC) and genetic algorithm (GA) within the importance sampling step of the PF to refine the prior state distribution, and hence, generate a more accurate and complete representation of posterior distribution. This approach also addresses the sample impoverishment and particle degeneracy that were the main problems in particle filtering data assimilation. In the data assimilation step, the prior states are generated by the VIC model control run. The prior states are then used to generate optimal prior based on GA-MCMC method and SMAP soil moisture observations. An importance resampling step is conducted to resample the particles with a probability greater than the uniform probability. The posterior states are then used for running VIC model in the next time step. 

Afterward, we used the copula function to integrate the information of posterior soil moisture, precipitation and PET through their joint cumulative distribution function (CDF). The joint CDF is then rescaled to the union of marginal CDFs in order to ensure a fair evaluation of drought condition without overestimating the drought severity and area. The inverse normal of the rescaled CDF is therefore considered as the integrated drought index and is used for drought monitoring. In the 

following subsections, we provide a progressive outline describing the components of the proposed drought monitoring approach. 

#### 3.1. VIC hydrologic model and assimilation setup 

The VIC model is a macroscale semi-distributed hydrologic model with three soil layers on the land surface (Liang et al., 1994). VIC simulates the water and energy balances at the grid scale and requires a separate routing module to derive the water movement over a basin. The latest VIC version 5 requires sub-daily meteorological inputs, such as precipitation, temperature, atmospheric pressure, incoming shortwave and longwave radiation, vapor pressure and wind speed. The VIC model has been successfully applied in numerous studies to assist water resources management, drought monitoring and climate change impact assessment (García-Valdecasas-Ojeda et al., 2017; Guo et al., 2009; Wang et al., 2012). The VIC simulations from the Global Land Data Assimilation System (GLDAS) (Rodell et al., 2004) provide global estimation of land surface fluxes and states at ~100 km resolution from 1979 to present. The VIC simulations in the NLDAS (Mitchell et al., 2004) provide hourly estimation of land surface states over central North America at ~12.5 km resolution. Only the top layer soil moisture in the VIC simulations is used for the analysis. The top layer in VIC model is generally 10 cm deep and may vary with regions. 

In this study, the VIC model is used to simulate the surface soil moisture over the CONUS using pre-calibrated parameters from NLDAS version 2. The calibrated parameters at ~12.5 km resolution are resampled to ~25 km by bilinear interpolation. Meteorological forcings from NLDAS are aggregated to a 6-h time interval in order to be consistent with the VIC model temporal resolution. The top surface soil layer depth is mostly 10 cm over the CONUS, with some variations due to vegetation covers and soil types. The multiple vegetation tiles in each grid cell in the NLDAS soil and vegetation datasets are modified to include only one vegetation type in each grid cell by selecting the vegetation with the largest proportion. Such representation of the vegetation tiles in each 25 km*25 km grid cell may degrade the drought monitoring capability for finer resolutions (e.g. 5 km*5 km) knowing that the subgrid drought condition may be different within each vegetation tile. We assume that the vegetation tile with the largest fraction of areas could represent the drought condition in this grid cell, which reduces the computational intensity. We deactivated the snow band option in the VIC simulation process to further save the model runtime. For operational monitoring systems, the snow band should be activated in order to better simulate the hydrological processes in snowcovered areas. 

The precipitation forcing data from NLDAS are perturbed using a lognormal distribution with a standard deviation of 0.3. The VIC model 

4 

_Remote Sensing of Environment 250 (2020) 112028_ 

L. Xu, et al. 

run using an ensemble of perturbed forcings without any updating process is regarded as the reference open loop (OL) run. In the EnKF and EPFM models, the simulated soil moisture is perturbed following Gaussian distribution with a standard deviation of 25% of the predicted values. The SMAP soil moisture error is assumed as 15% of the observation. These parameters are set by a trial and error process. Some studies adopted 0.04 m<sup>3</sup> /m<sup>3</sup> as the observation error (Mao et al., 2019; Yan et al., 2018), however, this constant error may not be appropriate due to the spatiotemporal heterogeneity of soil moisture at a large scale. The triple collocation and instrumental variable techniques are commonly used to obtain the remote sensing soil moisture error (AlvarezGarreton et al., 2013; Dong and Crow, 2018; Gruber et al., 2017; Gruber et al., 2016). However, the obtained error is time-invariant and cannot reflect the temporal error structure (Alvarez-Garreton et al., 2013). Therefore, the time-variant soil moisture observation error is used in this study. The systematic difference between the remote sensing soil moisture and modeled soil moisture is removed by empirical CDF matching. 

#### 3.2. Ensemble Kalman filter (EnKF) 

The state-space model (Moradkhani et al., 2018) which represents the dynamic earth system can be expressed as follows: 



#### _yt_ = _h_ ( _xt_ ) + _rt_ (2) 

where xt-1 and xt are the state variables at time t-1 and t, respectively; yt is the observation data; θ is the model parameters; f(∙) is a nonlinear operator that simulates the system from time t-1 to time t, such as the VIC model; ut is the atmospheric forcing data, such as precipitation and temperature; h(∙) is the nonlinear function that connects the states to observations. qt and rt denotes the model error and observation error, respectively. qt and rt are assumed to follow a Gaussian distribution with zero mean and the covariance Qt and Rt, respectively. 

EnKF (Evensen, 1994) is an ensemble form of Kalman filter. The EnKF relaxes the linearization process in the Kalman updating and uses an ensemble to quantify the covariances. This greatly improves the flexibility of Kalman filter in complex dynamic system models. Given an ensemble of simulations, the covariances of states and simulated observations can be obtained. 





where CXY is the covariance between the states and predicted observations and CYY is the covariances of predicted observations.  _xt_<sup>−</sup> , _i_ denotes the priori state vector for ith ensemble member at time t and  _yt_ , _i_ denotes the predicted observations for ith ensemble member at time t. E (∙) is the expectation and n is the ensemble size. The Kalman gain can be estimated as a function of these covariances. 



where Kt is the Kalman gain at time t; Rt is the covariance of observation error. 

In the updating process, each ensemble member is updated individually. 





where  _xt_ , _i_ and  _yt_ , _i_ are the same as that in Eq. (3); K is the Kalman gain; yt,i is the ith sample of observation at time t; rt, i is the observation error for ith ensemble at time t. N(0, Rt) represents the Gaussian distribution 

with zero mean and Rt variance. The EnKF used in this study is pointwise without horizontal covariances. A total of 50 ensemble members are used. The effect of sampling error is not considered here and the moderate ensemble size is chosen to alleviate the effect of sampling error on data assimilation (Anderson, 2016; Poterjoy et al., 2014). 

#### 3.3. Evolutionary PF-MCMC (EPFM) 

EPFM (Abbaszadeh et al., 2018) is built upon the Particle FilterMarkov Chain Monte Carlo (PF-MCMC) data assimilation method (Abbaszadeh et al., 2018). The PF-MCMC is also an extension of the PF sampling importance resampling (PF-SIR) (Abbaszadeh et al., 2018) where an ensemble of model states and parameters is generated (initialized), then the ensemble is evolved (forecasted) through the dynamic model and finally the ensemble members are updated using the observations. In the EPFM, the GA is combined with MCMC to generate an informative prior in order to produce a more reliable posterior. The MCMC step is used twice in the EPFM, first in the utilization of GA and MCMC to obtain a reliable prior state distribution, and then in updating the parameters similar to PF-MCMC. 

The incorporation of GA-MCMC into PF is designed to reduce the particle degeneracy and increase the particle diversity in order to improve the data assimilation accuracy. GA is a heuristic search method based on natural selectin and evolution. For PF, each particle is considered as a chromosome and each state variable is regarded as a gene. The crossover and mutation operations in the GA are used to select and generate good offspring according to Darwin's evolution theory, that is, to select good particles and states. Here, the roulette wheel selection method is used to select good chromosomes from parents according to the fitness value. This is similar to the role of weights in particles. Therefore, the weights in the particles can be regarded as the fitness value. 



where ft,i denotes the fitness value for ith particle at time t and wt, i+ is the posterior weight for particle i at time t. 

The roulette wheel selection method (Lipowski and Lipowska, 2012) selects the chromosome based on the proportion of its fitness. Given an ensemble of particles arranged according to their fitness values fti (i = 1,2, …, n), the selection probability of a chromosome is estimated as 



where Pt,i is the selection probability for ith chromosome at time t and ft,i is the fitness value for ith particle at time t. 

In this way, the particles with small weights are discarded and the particles with large weights are kept. The next step is crossover to generate new offspring from parents. Here the arithmetic crossover is used to crossover the chromosomes. In the arithmetic crossover, a pair of new particles are produced based on the combination of parent particles. 





where xi, t−1 and xj, t−1 are parent particles; xi, t−1′ and xj, t−1′ are the new generated offspring. The ξ parameter is a uniform value between 0 and 1. If ξ is equal to 1, the crossover will not generate new information from parent particles. Otherwise the information in xj, t−1 will be totally transferred into xi, t−1′ (xi, t−1 to xj, t−1′) if ξ is equal to 0. A crossover probability (ρc) is used to specify how many particles to be involved in the roulette selection and crossover process. The parameter ρc is set 0.8 to crossover 80% of the particles and 20% of the particles remain unchanged to ensure the stability. 

5 

_Remote Sensing of Environment 250 (2020) 112028_ 

L. Xu, et al. 

The original EPFM method includes a mutation operation to further increase the diversity of the particles. Here, the mutation procedure is not included because the experimental results change little with or without including the mutation part. After crossover, the new offspring with the same number of particles with parents are produced. The next step is to decide which particles should be accepted or rejected. This is similar to the procedure in the PF-MCMC (Moradkhani et al., 2012). The joint state-parameter probability density function p(xt, ip, θt, i−| y1:t) is expressed as 





where xt, ip and xt−1, ip denote the proposal states for ith particle at time t and t-1, respectively. f(∙) is the nonlinear operator, referred to Eq. (1). ut, i is the forcing data for ith particle at time t. θt, i− is the prior parameters for ith ensemble member at time t. p(y1:t| xt, ip, θt, i−) is calculated based on Gaussian likelihood function. The proposal state distribution p(xt, ip| θt, i−, y1:t−1) is fitted using a marginal Gaussian distribution with a mean of ut and a variance of σt2. The weighted mean and variance of the filtering posterior need to be calculated to obtain the proposal probability distribution. 





where xt, i− is the prior states for ith particle at time t. xt−1, i+ is the posterior states for ith particle at time t-1. μt and σt2 are the mean and variance of the proposal probability distribution. ut, i and θt, i− are referred to Eq. (12). wt−1, i+ is the posterior weight for ith particle at time t-1. 

The joint probability distribution of the proposal and prior states are compared using the metropolis acceptance ratio to decide which states should be accepted. 



where α is the metropolis acceptance ratio. The meanings of other parameters can refer to the equations above. 

The GA-MCMC process ensures that an appropriate prior state distribution is established before the parameter updating process. A suitable prior state distribution can help construct a reliable and accurate posterior distribution. After the GA-MCMC step, the parameters are then updated using the procedures in 3.2. The 50 particles are used in the EPFM assimilation experiment, the same with that of the EnKF. 

3.4. The standardized precipitation, evapotranspiration and soil moisture index (SPESMI) 

The SPESMI is constructed by the joint probability of surface soil moisture and a differenced variable using precipitation and PET based on copula. Copula can be used to model the joint distribution of two variables, regardless of their different marginal distributions (Madadgar and Moradkhani, 2013; Sklar, 1973). Suppose the soil moisture variable X and the differenced variable Y (P-PET), the joint CDF can be expressed as 



where C denotes the copula; F1 and F2 are the CDFs of X and Y, respectively. The variable Y is obtained by P-PET. Before modeling the joint CDF, the X and Y variables are preprocessed by subtracting the weekly averaged climatology. The climatology for a specific week is 

defined as the average of a variable covering the same week over all the 18 years from 2001 to 2018. 

The marginal distribution of a variable can be modeled by parametric or non-parametric distribution and both are widely used in calculating drought indices. Non-parametric modeling should be more suitable when a parametric distribution cannot properly describe the data. Here, the non-parametric kernel distribution is used to model the distribution of the variables X and Y since the distributions of both variables cannot be well-modeled by a parametric distribution due to the limited samples. A kernel distribution is a non-parametric description of the probability distribution of a random variable, defined by a kernel smoothing function and a bandwidth value. The kernel density estimation (KDE) approach is used to model the marginal distribution of soil moisture and P-PET. 



where x is a random variable, n is the sample size, h is the bandwidth, and K(∙) is the kernel function. The Gaussian kernel function is adopted and the bandwidth is determined by an optimal estimation (Bowman and Azzalini, 1997). 

There are numerous copulas that can be used to model the dependence structures of the bivariate case. The Archimedean copulas are a family of copulas and can model the dependence of multiple variables at arbitrary high dimension. Three Archimedean copulas, the Clayton, Frank, and Gumbel copulas, are widely used in modeling the dependence structures of two variables (Chen et al., 2012; Hao and AghaKouchak, 2013; Kao and Govindaraju, 2010). The Clayton copula is an asymmetric Archimedean copula and exhibits large dependence in the negative tail. 



where its generator is given by 



The appropriate copula is selected based on the two-sample Kolmogorov-Smirnov (K-S) test (Massey Jr, 1951) between the copula fitted CDF and the empirical CDF. If the p-value of K-S test is smaller than 0.01, the null hypothesis that the copula fitted CDF and the empirical CDF follow the same distribution is rejected at 1% significance level. The Clayton copula is found suitable for the modeling of the dependence of X and Y in Eq. (18) relative to Gaussian, Frank and Gumbel copulas. In a previous study (Hao and AghaKouchak, 2014), the inverse normal of the copula fitted CDF is usually regarded as a standardized drought index. However, this may lead to an overestimation of drought severity because the joint probability of two drought-related variables is often smaller than their marginal probabilities. The overestimation phenomenon may result in unfair assessment of drought area, intensity and duration. Therefore, a rescaling procedure is employed to rescale the copula fitted CDF to the CDFs of soil moisture and P-PET. 



where F<sup>−1</sup> represents the inverse of CDF, i.e. quantile function. Here, the empirical quantile mapping method is used to map the distribution of copula fitted CDF to the union of marginal CDFs. 

Once the joint CDF is obtained and rescaled, the SPESMI is defined as the inverse normal of the rescaled CDF. 

#### SPESMI = _φ_ −1 ( _p_ ) (23) 

where φ(∙) is the standard normal distribution and p is the rescaled CDF. 

The SPESMI is calculated based on the weekly percentile to represent the short-term drought conditions. It also can be calculated biweekly, monthly (~4 weeks), seasonally (~13 weeks) and biannual (~26 weeks), similar to the Standardized Precipitation Index (SPI) 

6 

_Remote Sensing of Environment 250 (2020) 112028_ 

L. Xu, et al. 

Table 1 

Classification of drought indices for different drought categories. 

|Category|Description|SPEI / SSMI / SPESMI|
|---|---|---|
|D0|Abnormally dry|[−0.8, −0.3)|
|D1|Moderate drought|[−1.3, −0.8)|
|D2|Severe drought|[−1.6, −1.3)|
|D3|Extreme drought|[−2.0, −1.6)|
|D4|Exceptional drought|[−∞, −2.0)|



(McKee et al., 1993). The weekly SPESMI can be used to monitor flash drought and the 6-month SPESMI is suitable for long-term drought assessment. The classification of drought category (Table 1) is defined based on the 40%, 20%, 10%, 5% and 2% percentiles for D0, D1, D2, D3 and D4 drought category, respectively, which is similar to that of the SPI. The assimilated soil moisture from April 1st 2015 to June 30th 2018 are used to calculate the SSMI and SPEI together with the VIC soil moisture simulations from 2001 to 2018. The assimilated soil moisture are rescaled to VIC soil moisture simulations based on quantile mapping for the overlapping time period to ensure temporally-consistent estimation of soil moisture. 

performance of the data assimilation approaches used in this study. The correlation coefficient measures the linear correlation between two variables x and y. A PCC value of 1 (−1) means a perfect correlation (anticorrelation) and a value of zero means no correlation. 



where xi and yi are data samples of x and y, respectively; <u>x</u> and <u>y</u> are arithmetic average of x and y, respectively; n denotes the sample size. 

The ubRMSE is the unbiased root mean square error (RMSE) by excluding the mean signal. It measures the absolute difference between two time series x and y after removing the mean values. 



The bias measures the mean deviation of simulations from observations. 

#### bias = y − <u>y</u> (26) 

#### 3.5. Evaluation metrics 

where y ̂ and <u>y</u> are the average of estimated soil moisture and observations, respectively. 

Three metrics, i.e. Pearson's correlation coefficient (PCC), unbiased root mean square error (ubRMSE) and bias, are used to measure the 



Fig. 3. The correlation, ubRMSE and bias of OL and assimilated soil moisture by the EnKF and EPFM assimilation techniques validated by in-situ observations. 

7 

_Remote Sensing of Environment 250 (2020) 112028_ 

L. Xu, et al. 



Fig. 4. A comparison of the assimilated soil moisture based on the EPFM method, OL, SMAP observations and the in-situ soil moisture data at the Walnut Gulch Watershed. 

#### 4. Results and discussion 

#### 4.1. Data assimilation performance assessment 

The spatial performances of OL and DA based on both EnKF and EPFM are demonstrated in Fig. 3. Compared to in-situ soil moisture observations, the EnKF method exhibits significant improvement over OL run in terms of correlation and ubRMSE and reduces the bias in some stations. This is especially evident in the central, southern and northern CONUS. The EPFM outperforms the EnKF in terms of correlation and ubRMSE in the majority of the validated stations across the CONUS. The overall averaged correlation coefficient, ubRMSE and bias for the EPFM (OL and EnKF) assimilated soil moisture are 0.56 (0.54 and 0.47), 0.054 (0.061 and 0.058) m<sup>3</sup> /m<sup>3</sup> and 0.016 (−0.039 and 0.004) m<sup>3</sup> /m<sup>3</sup> , respectively. Some areas in the southeastern and southwestern CONUS exhibit poor performance in the EPFM and EnKF relative to OL run, which is probably due to high variability of soil moisture by natural climate variability or human activities (Sadri et al., 2018). 

The median ubRMSE (Fig. S1) is 0.059, 0.057 and 0.051 m<sup>3</sup> /m<sup>3</sup> for OL, EnKF and EPFM, respectively, when validated using the in-situ observations. Although SMAP observations have a coarse spatial resolution relative to in-situ data, it represents the overall soil moisture in a 36 km grid cell, not a small representative area of the in-situ data. The median ubRMSE in EPFM is much closer to SMAP than that of the OL and EnKF, suggesting a better assimilation performance. The median correlation in the EPFM (0.59) is higher than the OL (0.56) and the EnKF (0.50). In terms of median bias, the EPFM (0.027) and the EnKF (0.012) have a smaller value than the OL (−0.035) run. Although the median bias in the EPFM is higher than the EnKF, the distribution and range of bias are more similar between them. 

#### 4.2. In-situ comparison over the walnut gulch watershed 

The sparse in-situ soil moisture data over the CONUS suffer from the representativeness error when comparing with grid cell averaged simulations. It should be noted that the spatial averages of sparse network based soil moisture evaluation is representative of dense soil 

moisture networks (Dong et al., 2020). In the meantime, the representative error does exist for a grid or a small region. The WGW area is a small region with dense soil moisture measurements over the study period. It is appropriate to examine whether the assimilated soil moisture falls within the range of in-situ data or not. If the assimilated soil moisture is consistently within the confidence interval of in-situ measurements, it is very likely to be accurate. It is seen the ensemble mean of the assimilated soil moisture is well within the 95% confidence interval of in-situ observations (Fig. 4). Most of the DA obtained soil moisture is well within the 68% confidence interval, i.e. the range of one standard deviation, indicating the DA results are strongly consistent with in-situ data. This consistency provides the evidence that the EPFM assimilated soil moisture is able to reproduce the in-situ observations at fine resolutions. A slight overestimation of the soil moisture in autumn or winter time is seen in DA versus in-situ measurement, which is a result of slight overestimation of SMAP observations. It should be noted that the 36 km SMAP radiometer soil moisture in a grid cell (36*36 = 1296 km<sup>2</sup> ) is used for assimilation and may not be comparable to a 150 km<sup>2</sup> WGW region. Therefore, the representativeness error might exist between assimilated soil moisture and in-situ measurement. 

#### 4.3. Drought monitoring over the CONUS 

The drought conditions at year 2017 based on 3-month SPESMI are taken as an example to demonstrate the drought monitoring result visually (Fig. 5). According to the SPESMI, mild drought spread out in the southern CONUS and the Midwest in the early spring, especially in Missouri and southern Illinois. The mild drought occurred in some areas of southeastern CONUS in the middle spring, similar to the USDM (NDMC, 2020), CPC soil moisture model (NCDC, 2017a) and the Soil Moisture and Ocean Salinity (SMOS) (Kerr et al., 2001) measurements (NCDC, 2017d). During late summer, severe to extreme drought prevailed in northwestern CONUS, especially in Montana, consistent with the results from USDA topsoil moisture observations (NCDC, 2017b) and NLDAS simulations (NCDC, 2017e). In the early autumn, severe drought occurred in the southern Illinois, West Virginia, Kansas and northwestern areas, consistent with the precipitation anomaly shown 

8 

L. Xu, et al. 



<!-- Start of picture text -->
Remote Sensing of Environment 250 (2020) 112028<br><!-- End of picture text -->



Fig. 5. The SPESMI for drought monitoring in year 2017. 

by the SPI (NOAA, 2017). The SPESMI can capture well the evolution of the 2017 flash drought in U.S. northern plains (Jencso et al., 2019). In late autumn, severe to extreme drought happened in central and southwestern areas, especially in Arizona, corresponding well with the Gravity Recovery and Climate Experiment (GRACE) (Tapley et al., 2004) based root zone soil moisture index (NCDC, 2017c). The severe to extreme droughts in southern California and Arizona persisted during the winter, and the extreme drought was concentrated in northern Texas, western Oklahoma, southern Kansas and eastern New Mexico, similar to the USDM based on the drought report (NOAA, 2018). 

The 1-month drought indices are compared with the flash drought detection capability in the U.S. Northern Plains (USNP) in May 2017 (Fig. 6). The USDM detects a small drought area from May 2 to May 23, and can identify the flash drought to a large extent until the end of May. 

The SPEI detects the drought onset on May 9, 2017 in major portion of the USNP. A negative soil moisture anomaly begins to appear on May 9 and prevails until May 23. The SSMI_OL exhibits severe to extreme droughts in the northeastern USNP from May 2 to May 30, while the USDM and SPEI do not suggest severe drought on May 2. The official report does not indicate severe soil moisture deficits on May 2 (Jencso et al., 2019). Therefore, the SSMI_DA could detect the gradual evolution of flash drought relative to SSMI_OL, indicating an improvement of drought monitoring by using soil moisture data assimilation. The SPESMI_OL and SPESMI_DA can detect the flash drought onset on May 9 due to its integration of meteorological and soil moisture indicators, much earlier than the USDM. Although only small differences are seen between the SPESMI_OL and SPESMI_DA, the SPESMI_DA can detect extreme drought areas in the northeast Montana on May 30 while 

9 

_Remote Sensing of Environment 250 (2020) 112028_ 

L. Xu, et al. 



Fig. 6. A demonstration of the flash drought evolution in the U.S. Northern Plains in May 2017. 

SPESMI_OL detects largely moderate drought. 

Three weeks are selected to compare the drought monitoring capability by the USDM, SPEI, SSMI_OL, SSMI_DA, SPESMI_OL and SPESMI_DA (Fig. 7). On April 7, 2015, severe to extreme droughts are detected in large parts of the western US by the USDM, extending from California, Arizona, Utah and Nevada to the Pacific Northwest. Moderate to extreme droughts are detected by the SPEI in the northern and northwestern areas. Some drought areas are detected by the SSMI_OL and SSMI_DA in California, South Dakota and the northeastern areas, while the SSMI_DA detects more severe and extreme drought areas and is more consistent with the USDM. The SPESMI_OL and SPESMI_DA integrate the SPEI and the SSMI results and highlight severe droughts in the northwestern, northern and northeastern part of CONUS. However, the SPESMI_OL and SPESMI_DA miss the extreme drought in northern Texas and western Oklahoma compared to the USDM. The SPI (NOAA, 2015) and CPC soil moisture (NCDC, 2015) do not show a drought event in northern Texas and western Oklahoma but the GRACE satellite indicates a severe negative water storage anomaly (NASA, 2020) in this area. Therefore, the failure to detect the extreme drought in northern Texas and western Oklahoma by the SPESMI_OL and SPESMI_DA can be attributed to ignoring the groundwater condition. The groundwater condition is related to hydrological drought but not discussed here as agricultural drought is the main scope of this research. 

On December 20, 2016, extreme droughts are exhibited in the southern California and south Atlantic, and mild to severe droughts are shown in Midwest, western and southern areas. There are very small drought areas in southern California from model simulations (NCDC, 

2016e), and SMOS retrieval (NCDC, 2016d) but severe droughts in the groundwater (NCDC, 2016b) at this time. Therefore, this miss can be explained by the absence of a groundwater variable or local observations in the SPESMI_OL and SPESMI_DA. Few extreme droughts are indicated by the SPEI in southeastern region, while the SSMI_DA and SPESMI_DA suggest extreme to exceptional soil moisture droughts, consistent with CPC soil moisture (NCDC, 2016a), GRACE estimates (NCDC, 2016b) and streamflow observations (NCDC, 2016c). SSMI_DA and SPESMI_DA indicate exceptional droughts in the southeastern region, which seem to be more consistent with the USDM and other hydrological estimates (NCDC, 2016a, 2016b, 2016e) than SSMI_OL and SPESMI_OL. 

On December 12, 2017, the spatial patterns of drought area detected by the SPESMI_OL and SPESMI_DA are consistent with the USDM, such as the mild to exceptional droughts in southwestern and southern areas. The SSMI_OL and SSMI_DA both detect severe to extreme droughts in the southwestern, southern and northern CONUS. The USDM only detects moderate (D1) droughts in the southwestern CONUS, while the SPEI and SSMI_DA indicate that there is severe to extreme meteorological and soil moisture droughts in this area. However, the SPESMI_DA could capture the severe to extreme droughts in the southwestern areas, as it integrates information from precipitation, PET and soil moisture. 

USDM is an integrated drought index incorporating multisource geophysical information, such as precipitation, soil moisture, streamflow, evapotranspiration and local observations. The USDM and SPESMI may have different sensitivity to precipitation because they 

10 

_Remote Sensing of Environment 250 (2020) 112028_ 

L. Xu, et al. 



Fig. 7. A comparison of the USDM, SPEI, SSMI_OL, SSMI_DA, SPESMI_OL and SPESMI_DA in drought monitoring. The SPEI, SSMI_OL, SSMI_DA, SPESMI_OL and SPESMI_DA are calculated at 3-month time scale, which facilitates the comparison with USDM because the USDM depicts both short-term and long-term drought conditions. The day April 7, 2015 shown in the first column means the weekly drought conditions beginning on April 7, 2015 and ending on April 13, 2015, the same with USDM. The same descriptions are used throughout the texts unless additional statement. 

11 

_Remote Sensing of Environment 250 (2020) 112028_ 

L. Xu, et al. 



Fig. 8. The drought extent from April 1, 2015 to June 30, 2018 estimated by the USDM and the SPESMI. 



Fig. 9. A demonstration of the SPEI, SSMI and SPESMI on April 1, 2015 for a 1-week time scale. Different colors of scatter points represent different drought classes (D0-D4) based on SPESMI. The blue, cyan, green, orange and red horizontal and vertical lines denote the D0-D4 drought threshold for SSMI and SPEI, respectively. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.) 

12 

_Remote Sensing of Environment 250 (2020) 112028_ 

L. Xu, et al. 



Fig. 10. Multiscalar representation of drought indices at 44.875°N, 114.375°W (central Idaho). 

consider different hydroclimate variables (at different time scales) for identification of drought. We aim to examine the differences between USDM and SPESMI, and see how SPESMI can complement drought monitoring. The results discussed above indicate the added values of SPESMI in detecting drought relative to USDM. In particular, the SPESMI was able to detect the drought events which have been underestimated by USDM. Therefore, the SPESMI could serve as an independent and complementary drought monitoring index. 

A comparison of the drought extent between the USDM and the SPESMI over the CONUS is shown in Fig. 8 to examine the temporal consistency and differences between the approaches. Strong temporal consistency is seen in drought extent between the USDM and SPESMI indicating the suitability of the SPESMI as an overall drought indicator. There are several temporal drought hot spots detected by the USDM, such as in October 2015, November 2016 and February 2018. The temporal drought hot spots detected by the SPESMI agree well with that in the USDM. The areas under D0-D4 droughts detected by the SPESMI are generally consistent with the USDM, which is suitable for different drought categories estimation. Some differences also exist in the detected drought area between the USDM and the SPESMI. For example, the SPESMI estimates smaller drought extent in January 2016 than that of the USDM. This difference is likely due to several reasons, such as the inclusion of streamflow factor in the USDM and the different time scales in the calculation of drought index. The SPESMI exhibits a higher correlation (0.69) with the USDM in the moderate to exceptional drought area than SPEI (0.55) and SSMI (0.62) (Fig. S2). Overall, the drought extent based on the SPESMI does not deviate from the USDM in drought monitoring during the studied period. It should be noted that although the temporal drought extent between the USDM and SPESMI is similar, their spatial patterns are different. 

#### 4.4. The SPESMI at multiple temporal scales 

A scatter plot is drawn to demonstrate the difference of SPEI, SSMI and SPESMI in the representation of drought category (Fig. 9). The scatter points are identified as drought events if the SPESMI value in a corresponding location falls under a specific drought category (D0-D4). The lower left area of the vertical and horizontal dashed blue lines denotes the drought area (mild to exceptional drought) for SPEI and SSMI, respectively. The SPESMI can identify some drought events with negative SPEI but with positive SSMI. Similarly, the SPESMI can identify some drought events with negative SSMI but with positive SPEI. In other words, a region under meteorological drought condition may not exhibit agricultural drought, that is low soil moisture. In this case, the SPESMI may detect the meteorological drought. Similarly, a point under soil moisture drought conditions may correspond to the end of meteorological drought and the SPESMI may detect the soil moisture drought. Although some regions under meteorological drought and with normal soil moisture conditions are not recognized as drought based on the SPESMI (not shown), the SPESMI can integrate the drought information from soil moisture and P-PET. For example, it is not certain to recognize the case as a drought event if a region is under meteorological drought but with high soil moisture. If this case is considered as a drought, the multivariate drought assessment would lead to a much larger estimation of drought magnitude and extent than the univariate case, when two or more drought-related variables are incorporated. However, the drought magnitude and extent should not be exaggerated for multivariate drought evaluation in practice. The SPESMI enables a fair multivariate drought evaluation by rescaling the joint CDF to the union of univariate CDFs. 

The 1-month, 3-month and 6-month drought indices are shown in Fig. 10 to demonstrate the flexibility of the SPESMI at different time scales. The 1-month drought index can be used to measure short-term 

13 

L. Xu, et al. 



<!-- Start of picture text -->
Remote Sensing of Environment 250 (2020) 112028<br><!-- End of picture text -->



Fig. 11. The correlation between drought indices and crop yield loss (bushels per acre) over the CONUS. Only the negative drought indices are used (i.e. dry years) when computing the correlation. 

drought condition and the 6-month drought index is suitable for longterm water deficits assessment. The SPESMI models the joint probability of soil moisture and P-PET, thus integrating multivariate information from the SPEI and SSMI. This characteristic enables a strong detection capability of the drought signal from precipitation anomaly, ET increase and soil moisture deficits. When the precipitation is substantially lower than normal and the meteorological drought is declared, but the soil moisture is a normal state, the SPESMI recognizes this case as drought, which is helpful for agricultural drought early warnings. When the precipitation is back to normal but the soil moisture anomaly is not recovered to a large extent, the drought is not terminated based on the SPESMI. Therefore, the SPESMI is able to incorporate the meteorological and soil moisture drought information to represent an overall drought condition. 

#### 4.5. Correlation between drought indices and crop yield loss 

A crop specific correlation between the nationwide yield loss and 

drought indices are conducted to further demonstrate the usefulness of the integrated drought index (Fig. 11). The SPESMI_DA index exhibits a significant improvement of the correlation with yield loss over SPEI and SSMI_DA in spring wheat and winter wheat. A better correlation of drought indices after data assimilation is seen in the SSMI_DA and SPESMI_DA than the OL indices of SSMI_OL and SPESMI_OL, indicating an added value of data assimilation. The correlation may have large confidence intervals based on the 18-year crop yield data, which prevents the conclusion of a better drought index for wheat yield forecasting. However, it is likely capable to forecast wheat crop yield based on the SPESMI_DA. 

#### 5. Conclusion 

In this study, a new data assimilation algorithm, the EPFM, is implemented to improve the soil moisture simulations over the CONUS based on SMAP satellite soil moisture observations. Compared to the commonly used EnKF method, the EPFM technique can improve the soil 

14 

_Remote Sensing of Environment 250 (2020) 112028_ 

##### L. Xu, et al. 

moisture estimation in terms of the correlation and ubRMSE in most of the in-situ stations validated over the CONUS. Compared with the densely distributed in-situ soil moisture measurements in the WGW area, the EPFM assimilated soil moisture generally falls within one standard deviation of the in-situ observations, suggesting the effectiveness of the assimilated soil moisture at fine resolutions. These validations are not representative of the entire CONUS domain. To obtain a validation over the entire domain, other techniques such as triple colocation (with two other independent observation or simulation sources) could be used (Stoffelen, 1998). 

As for drought monitoring, a new drought index, the SPESMI, is developed by incorporating precipitation, PET and soil moisture based on a copula function. The posterior soil moisture through EPFM assimilation are used to calculate the SPESMI together with NLDAS precipitation and MODIS PET. The SPESMI serves as an agrometeorological drought index, integrating information from meteorological drought and soil moisture drought. As a result, the early drought signal from precipitation and ET and the soil moisture memory are jointly captured by the SPESMI. Compared with the USDM, the SPESMI can detect some severe drought events underestimated by the USDM and can detect the flash drought signal early. A strong temporal consistency of the detected drought areas is found between the SPESMI and the USDM. The integrated drought index also exhibits high correlation with the yield loss of spring wheat and winter wheat crops of U.S., suggesting the potential for crop yield forecasting. Overall, the SPESMI based on multivariate factors can serve as an efficient and potentially complementary index for drought monitoring. 

The SPESMI is calculated based on the climatology from 2001 to 2018 due to the limited observations of ET from MODIS, which is a relatively short period. A longer time period could be used to extend the time interval of climatology based on model simulations. The SPESMI incorporates precipitation, PET and soil moisture. A potential way to enhance this approach is to include the shallow groundwater as a new water content information from GRACE satellites. However, the GRACE data span a short time period but the multivariate copula modeling needs enough samples. One possibility is to resort to model simulations to increase the sample size. An integrated drought index considering precipitation, ET, soil moisture and shallow groundwater may have good potential in quantifying overall water deficits and to perform drought monitoring at regional or global scales. 

#### Declaration of Competing Interest 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

#### Acknowledgements 

Partial financial support for this project was provided by the National Oceanic and Atmospheric Administration (NOAA) Modeling, Analysis, Predictions, and Projections (MAPP) (Grant No. NA18OAR4310319). The first author also acknowledges partial financial support from the China Scholarship Council (201906270231). 

#### Appendix A. Supplementary data 

Supplementary data to this article can be found online at https:// doi.org/10.1016/j.rse.2020.112028. 

#### References 

Abbaszadeh, P., Moradkhani, H., Yan, H., 2018. Enhancing hydrologic data assimilation by evolutionary particle filter and Markov chain Monte Carlo. Adv. Water Resour. 111, 192–204. https://doi.org/10.1016/j.advwatres.2017.11.011. 

Abbaszadeh, P., Moradkhani, H., Daescu, D.N., 2019a. The quest for model uncertainty 

- quantification: a hybrid ensemble and Variational data assimilation framework. Water Resour. Res. 55, 2407–2431. https://doi.org/10.1029/2018WR023629. 

Abbaszadeh, P., Moradkhani, H., Zhan, X., 2019b. Downscaling SMAP radiometer soil 

   - moisture over the CONUS using an ensemble learning method. Water Resour. Res. 55, 324–344. https://doi.org/10.1029/2018WR023354. 

- AghaKouchak, A., 2014. A baseline probabilistic drought forecasting framework using standardized soil moisture index: application to the 2012 United States drought. Hydrol. Earth Syst. Sci. 18, 2485–2492. https://doi.org/10.5194/hess-18-2485-2014. 

- Ahmadalipour, A., Moradkhani, H., Yan, H., Zarekarizi, M., 2017. Remote sensing of drought: Vegetation, soil moisture, and data assimilation. In: Remote Sensing of Hydrological Extremes. Springer, pp. 121–149. https://doi.org/10.1007/978-3-31943744-6_7. 

- Alvarez-Garreton, C., Ryu, D., Western, A., Crow, W., Robertson, D., 2013. Impact of observation error structure on satellite soil moisture assimilation into a rainfall-runoff model. In: Piantadosi, J., Anderssen, R., Boland, J. (Eds.), MODSIM2013, 20th International Congress on Modelling and Simulation. Modelling and Simulation Society of Australia and New Zealand, pp. 3071–3077. 

- Anderegg, W.R., Hicke, J.A., Fisher, R.A., Allen, C.D., Aukema, J., Bentz, B., Hood, S., Lichstein, J.W., Macalady, A.K., McDowell, N., 2015. Tree mortality from drought, insects, and their interactions in a changing climate. New Phytol. 208, 674–683. https://doi.org/10.1111/nph.13477. 

- Anderson, J.L., 2016. Reducing correlation sampling error in ensemble Kalman filter data assimilation. Mon. Weather Rev. 144, 913–925. 

- Bell, J.E., Palecki, M.A., Baker, C.B., Collins, W.G., Lawrimore, J.H., Leeper, R.D., Hall, M.E., Kochendorfer, J., Meyers, T.P., Wilson, T., 2013. US climate reference network soil moisture and temperature observations. J. Hydrometeorol. 14, 977–988. https:// doi.org/10.1175/JHM-D-12-0146.1. 

- Blankenship, C., Case, J., Hain, C., 2018. Impact of SMAP Soil Moisture Assimilation on Numerical Weather Forecasts over the Contiguous United States and East Africa. 

- Bolten, J.D., Crow, W.T., Zhan, X., Jackson, T.J., Reynolds, C.A., 2009. Evaluating the utility of remotely sensed soil moisture retrievals for operational agricultural drought monitoring. IEEE J. Select. Topics Appl. Earth Observ. Remote Sens. 3, 57–66. https://doi.org/10.1109/JSTARS.2009.2037163. 

- Bowman, A.W., Azzalini, A., 1997. Applied Smoothing Techniques for Data Analysis: The Kernel Approach with S-Plus Illustrations. OUP Oxford. 

- Chan, S.K., Bindlish, R., O’Neill, P.E., Njoku, E., Jackson, T., Colliander, A., Chen, F., Burgin, M., Dunbar, S., Piepmeier, J., 2016. Assessment of the SMAP passive soil moisture product. IEEE Trans. Geosci. Remote Sens. 54, 4994–5007. https://doi.org/ 10.1109/TGRS.2016.2561938. 

- Chen, L., Singh, V.P., Guo, S., Mishra, A.K., Guo, J., 2012. Drought analysis using copulas. J. Hydrol. Eng. 18, 797–808. https://doi.org/10.1061/(ASCE)HE.1943-5584. 0000697. 

- Clark, J.S., Iverson, L., Woodall, C.W., Allen, C.D., Bell, D.M., Bragg, D.C., D’Amato, A.W., Davis, F.W., Hersh, M.H., Ibanez, I., 2016. The impacts of increasing drought on forest dynamics, structure, and biodiversity in the United States. Glob. Chang. Biol. 22, 2329–2352. https://doi.org/10.1111/gcb.13160. 

- Colliander, A., Jackson, T.J., Bindlish, R., Chan, S., Das, N., Kim, S., Cosh, M., Dunbar, R., Dang, L., Pashaian, L., 2017. Validation of SMAP surface soil moisture products with core validation sites. Remote Sens. Environ. 191, 215–231. https://doi.org/10.1016/ j.rse.2017.01.021. 

- Das, N.N., Entekhabi, D., Kim, S., Yueh, S., O’Neill, P., 2016. Combining SMAP and sentinel data for high-resolution soil moisture product. In: 2016 IEEE International Geoscience and Remote Sensing Symposium (IGARSS). IEEE, pp. 129–131. 

- Das, N., Entekhabi, D., Dunbar, R., Kim, S., Yueh, S., Colliander, A., O'Neill, P., Jackson, T., 2018. SMAP/Sentinel-1 L2 Radiometer/Radar 30-Second Scene 3 km EASE-Grid Soil Moisture, Version 2. Boulder, Colorado USA. NASA National Snow and Ice Data Center Distributed Active Archive Centerhttps://doi.org/10.5067/KE1CSVXMI95Y. 

- DeChant, C.M., Moradkhani, H., 2012. Examining the effectiveness and robustness of sequential data assimilation methods for quantification of uncertainty in hydrologic forecasting. Water Resour. Res. 48. https://doi.org/10.1029/2011WR011011. 

- Dobriyal, P., Qureshi, A., Badola, R., Hussain, S.A., 2012. A review of the methods available for estimating soil moisture and its implications for water resource management. J. Hydrol. 458, 110–117. https://doi.org/10.1016/j.jhydrol.2012.06.021. 

- D'Odorico, P., Caylor, K., Okin, G.S., Scanlon, T.M., 2007. On soil moisture–vegetation feedbacks and their possible effects on the dynamics of dryland ecosystems. J. Geophys. Res. Biogeosci. 112. https://doi.org/10.1029/2006JG000379. 

- Dong, J., Crow, W.T., 2018. The added value of assimilating remotely sensed soil moisture for estimating summertime soil moisture-air temperature coupling strength. Water Resour. Res. 54, 6072–6084. https://doi.org/10.1029/2018WR022619. 

- Dong, J., Steele-Dunne, S.C., Ochsner, T.E., Giesen, N.v.d., 2016. Estimating soil moisture and soil thermal and hydraulic properties by assimilating soil temperatures using a particle batch smoother. Adv. Water Resour. 91, 104–116. https://doi.org/10.1016/j. advwatres.2016.03.008. 

- Dong, J., Crow, W., Reichle, R., Liu, Q., Lei, F., Cosh, M.H., 2019. A global assessment of added value in the SMAP level 4 soil moisture product relative to its baseline land surface model. Geophys. Res. Lett. 46, 6604–6613. https://doi.org/10.1029/ 2019GL083398. 

- Dong, J., Crow, W.T., Tobin, K.J., Cosh, M.H., Bosch, D.D., Starks, P.J., Seyfried, M., Collins, C.H., 2020. Comparison of microwave remote sensing and land surface modeling for surface soil moisture climatology estimation. Remote Sens. Environ. 242, 111756. https://doi.org/10.1016/j.rse.2020.111756. 

- Entekhabi, D., Njoku, E.G., O’Neill, P.E., Kellogg, K.H., Crow, W.T., Edelstein, W.N., Entin, J.K., Goodman, S.D., Jackson, T.J., Johnson, J., 2010. The soil moisture active passive (SMAP) mission. Proc. IEEE 98, 704–716. https://doi.org/10.1109/JPROC. 2010.2043918. 

Evensen, G., 1994. Sequential data assimilation with a nonlinear quasi-geostrophic model 

15 

_Remote Sensing of Environment 250 (2020) 112028_ 

L. Xu, et al. 

using Monte Carlo methods to forecast error statistics. J. Geophys. Res. Oceans 99, 10143–10162. https://doi.org/10.1029/94JC00572. 

García-Valdecasas-Ojeda, M., de Franciscis, S., Raquel Gámiz-Fortis, S., Castro-Díez, Y., Jesús Esteban-Parra, M., 2017. Hydrological characterization of Guadalquivir River basin for the period 1980-2010 using VIC model. In: EGU General Assembly Conference Abstracts, pp. 17838. 

- Goodrich, D.C., Keefer, T.O., Unkrich, C.L., Nichols, M.H., Osborn, H.B., Stone, J.J., Smith, J.R., 2008. Long-term precipitation database, walnut gulch experimental watershed, Arizona, United States. Water Resour. Res. 44. https://doi.org/10.1029/ 2006WR005782. 

- Gruber, A., Su, C.-H., Zwieback, S., Crow, W., Dorigo, W., Wagner, W., 2016. Recent advances in (soil moisture) triple collocation analysis. Int. J. Appl. Earth Obs. Geoinf. 45, 200–211. https://doi.org/10.1016/j.jag.2015.09.002. 

- Gruber, A., Dorigo, W.A., Crow, W., Wagner, W., 2017. Triple collocation-based merging of satellite soil moisture retrievals. IEEE Trans. Geosci. Remote Sens. 55, 6780–6792. https://doi.org/10.1109/TGRS.2017.2734070. 

- Guo, S., Guo, J., Zhang, J., Chen, H., 2009. VIC distributed hydrological model to predict climate change impact in the Hanjiang basin. Sci. China Series E. 52, 3234. https:// doi.org/10.1007/s11431-009-0355-2. 

- Hao, Z., AghaKouchak, A., 2013. Multivariate standardized drought index: a parametric multi-index model. Adv. Water Resour. 57, 12–18. https://doi.org/10.1016/j. advwatres.2013.03.009. 

- Hao, Z., AghaKouchak, A., 2014. A nonparametric multivariate multi-index drought monitoring framework. J. Hydrometeorol. 15, 89–101. https://doi.org/10.1175/ JHM-D-12-0160.1. 

- Huang, J., Yu, H., Guan, X., Wang, G., Guo, R., 2016. Accelerated dryland expansion under climate change. Nat. Clim. Chang. 6, 166. https://doi.org/10.1038/ nclimate2837. 

- Jencso, K., Parker, B., Downey, M., Hadwen, T., Howell, J., Leaf, R., Edwards, L., Akyuz, A., Kluck, D., Peck, D., Rath, M., Syner, M., Umphlett, N., Wilmer, H., Barnes, V., Clabo, D., Fuchs, B., He, M., Johnson, S., Kimball, J., Longknife, D., Martin, D., Nickerson, N., Sage, J., Fransen, T., 2019. Flash Drought: Lessons Learned from the 2017 Drought Across the U.S. Northern Plains and Canadian Prairies. NOAA National Integrated Drought Information System. 

- Kao, S.-C., Govindaraju, R.S., 2010. A copula-based joint deficit index for droughts. J. Hydrol. 380, 121–134. https://doi.org/10.1016/j.jhydrol.2009.10.029. 

- Kerr, Y.H., Waldteufel, P., Wigneron, J.-P., Martinuzzi, J., Font, J., Berger, M., 2001. Soil moisture retrieval from space: the soil moisture and ocean salinity (SMOS) mission. IEEE Trans. Geosci. Remote Sens. 39, 1729–1735. https://doi.org/10.1109/36. 942551. 

- Kolassa, J., Reichle, R., Liu, Q., Cosh, M., Bosch, D., Caldwell, T., Colliander, A., Holifield Collins, C., Jackson, T., Livingston, S., 2017. Data assimilation to extract soil moisture information from SMAP observations. Remote Sens. 9, 1179. https://doi.org/10. 3390/rs9111179. 

- Kolb, T.E., Fettig, C.J., Ayres, M.P., Bentz, B.J., Hicke, J.A., Mathiasen, R., Stewart, J.E., Weed, A.S., 2016. Observed and anticipated impacts of drought on forest insects and diseases in the United States. For. Ecol. Manag. 380, 321–334. https://doi.org/10. 1016/j.foreco.2016.04.051. 

- Liang, X., Lettenmaier, D.P., Wood, E.F., Burges, S.J., 1994. A simple hydrologically based model of land surface water and energy fluxes for general circulation models. J. Geophys. Res.-Atmos. 99, 14415–14428. https://doi.org/10.1029/94JD00483. 

- Lievens, H., Reichle, R.H., Liu, Q., De Lannoy, G., Dunbar, R.S., Kim, S., Das, N.N., Cosh, M., Walker, J.P., Wagner, W., 2017. Joint Sentinel-1 and SMAP data assimilation to improve soil moisture estimates. Geophys. Res. Lett. 44, 6145–6153. https://doi.org/ 10.1002/2017GL073904. 

- Lipowski, A., Lipowska, D., 2012. Roulette-wheel selection via stochastic acceptance. Phys. A: Stat. Mech. Appl. 391, 2193–2196. https://doi.org/10.1016/j.physa.2011. 12.004. 

- Littell, J.S., Peterson, D.L., Riley, K.L., Liu, Y., Luce, C.H., 2016. A review of the relationships between drought and forest fire in the United States. Glob. Chang. Biol. 22, 2353–2369. https://doi.org/10.1111/gcb.13275. 

- Liu, W., Gopal, S., Woodcock, C.E., 2004. Uncertainty and confidence in land cover classification using a hybrid classifier approach. Photogramm. Eng. Remote. Sens. 70, 963–971. https://doi.org/10.14358/PERS.70.8.963. 

- Lu, J., Carbone, G.J., Gao, P., 2017a. Detrending crop yield data for spatial visualization of drought impacts in the United States, 1895–2014. Agric. For. Meteorol. 237, 196–208. https://doi.org/10.1016/j.agrformet.2017.02.001. 

- Lu, Y., Steele-Dunne, S.C., Farhadi, L., van de Giesen, N., 2017b. Mapping surface heat fluxes by assimilating SMAP soil moisture and GOES land surface temperature data. Water Resour. Res. 53, 10858–10877. https://doi.org/10.1002/2017WR021415. 

- Lu, Y., Dong, J., Steele-Dunne, S.C., 2019. Impact of soil moisture data resolution on soil moisture and surface heat flux estimates through data assimilation: a case study in the southern Great Plains. J. Hydrometeorol. 20, 715–730. https://doi.org/10.1175/ JHM-D-18-0234.1. 

- Madadgar, S., Moradkhani, H., 2013. A Bayesian framework for probabilistic seasonal drought forecasting. J. Hydrometeorol. 14, 1685–1705. https://doi.org/10.1175/ JHM-D-13-010.1. 

- Mann, M.E., Gleick, P.H., 2015. Climate change and California drought in the 21st century. Proc. Natl. Acad. Sci. 112, 3858–3859. https://doi.org/10.1073/pnas. 1503667112. 

- Mao, Y., Crow, W.T., Nijssen, B., 2019. A framework for diagnosing factors degrading the Streamflow performance of a soil moisture data assimilation system. J. Hydrometeorol. 20, 79–97. https://doi.org/10.1175/JHM-D-18-0115.1. 

- Massey Jr., F.J., 1951. The Kolmogorov-Smirnov test for goodness of fit. J. Am. Stat. Assoc. 46, 68–78. https://doi.org/10.1080/01621459.1951.10500769. 

- McColl, K.A., Alemohammad, S.H., Akbar, R., Konings, A.G., Yueh, S., Entekhabi, D., 

2017. The global distribution and dynamics of surface soil moisture. Nat. Geosci. 10, 100. https://doi.org/10.1038/ngeo2868. 

- McKee, T.B., Doesken, N.J., Kleist, J., 1993. The relationship of drought frequency and duration to time scales. In: Proceedings of the 8th Conference on Applied Climatology. American Meteorological Society, Boston, MA, pp. 179–183. 

- Mishra, A., Vu, T., Veettil, A.V., Entekhabi, D., 2017. Drought monitoring with soil moisture active passive (SMAP) measurements. J. Hydrol. 552, 620–632. https://doi. org/10.1016/j.jhydrol.2017.07.033. 

- Mitchell, K.E., Lohmann, D., Houser, P.R., Wood, E.F., Schaake, J.C., Robock, A., Cosgrove, B.A., Sheffield, J., Duan, Q., Luo, L., 2004. The multi-institution north American land data assimilation system (NLDAS): utilizing multiple GCIP products and partners in a continental distributed hydrological modeling system. J. Geophys. Res.-Atmos., 109. https://doi.org/10.1029/2003JD003823. 

- Moradkhani, H., DeChant, C.M., Sorooshian, S., 2012. Evolution of ensemble data assimilation for uncertainty quantification using the particle filter-Markov chain Monte Carlo method. Water Resour. Res. 48. https://doi.org/10.1029/2012WR012144. 

- Moradkhani, H., Nearing, G., Abbaszadeh, P., Pathiraja, S., 2018. Fundamentals of data assimilation and theoretical advances. In: Duan (Ed.), Handbook of Hydrometeorological Ensemble Forecasting. Springer, Berlin, Heidelberg, pp. 1–26. https://doi.org/10.1007/978-3-642-40457-3_30-1. 

- Mujumdar, P., Kumar, D.N., 2012. Floods in a Changing Climate: Hydrologic Modeling. Cambridge University Press. 

- Narasimhan, B., Srinivasan, R., 2005. Development and evaluation of soil moisture deficit index (SMDI) and evapotranspiration deficit index (ETDI) for agricultural drought monitoring. Agric. For. Meteorol. 133, 69–88. https://doi.org/10.1016/j.agrformet. 2005.07.012. 

- NASA, 2020. Groundwater Percentile. https://nasagrace. unl.edu/Archive.aspx (accessed 16 May 2020). 

- NCDC, 2015. Calculated Soil Moisture Ranking Percentile in April. pp. 2015. https:// www.ncdc.noaa.gov/monitoring-content/sotc/drought/2015/04/noaa-nws-cpc-soilmoist-pct-apr15.gif accessed 15 May 2020. 

- NCDC, 2016a. Calculated Soil Moisture Ranking Percentile in December. pp. 2016. https://www.ncdc.noaa.gov/monitoring-content/sotc/drought/2016/12/noaa-nwscpc-soil-moist-pct-dec16.gif accessed 16 May 2020. 

- NCDC, 2016b. GRACE-Based Shallow Groundwater Drought Indicator on December 26. pp. 2016. https://www.ncdc.noaa.gov/monitoring-content/sotc/drought/2016/12/ nasa-groundwater-pct-1226-GRACE_GWS.png (accessed 17 May 2020). 

- NCDC, 2016c. Map of Monthly Streamflow Compared to Historical Streamflow for the Month of the Year (United States). https://www.ncdc.noaa.gov/monitoring-content/ sotc/drought/2016/12/usgs-streamflow-pct-us-dec16-huc.png. 

- NCDC, 2016d. SMOS Soil Moisture Difference from Average in December. pp. 2016. https://www.ncdc.noaa.gov/monitoring-content/sotc/drought/2016/12/SMOS_ DiffAvgSM_2016_12_Month.pdf accessed 16 May 2020. 

- NCDC, 2016e. VIC Soil Moisture Percentage Change in December. pp. 2016. https:// www.ncdc.noaa.gov/monitoring-content/sotc/drought/2016/12/uwa-vic-soilmoist-pct-change-1130-to-1231.gif accessed 16 May 2020. 

- NCDC, 2017a. Calculated Soil Moisture Ranking Percentile on APR 30. pp. 2017. https:// www.ncdc.noaa.gov/monitoring-content/sotc/drought/2017/04/noaa-nws-cpc-soilmoist-pct-0430.gif accessed 15 May 2020. 

- NCDC, 2017b. Extent of Topsoil Short or Very Short of Moisture on Aug 27. pp. 2017. https://www.ncdc.noaa.gov/monitoring-content/sotc/drought/2017/08/topsoilstatewide-statistics-0827.pdf accessed 15 May 2020. 

- NCDC, 2017c. GRACE-Based Root Zone Soil Moisture Drought Indicator on Nov 27. pp. 2017. https://www.ncdc.noaa.gov/monitoring-content/sotc/drought/2017/11/ nasa-root-zone-soil-moist-GRACE_RTZSM_20171127.png accessed 16 May 2020. 

- NCDC, 2017d. SMOS Soil Moisture Difference from Average in April. pp. 2017. https:// www.ncdc.noaa.gov/monitoring-content/sotc/drought/2017/04/SMOS_DiffAvgSM_ 2017_4_Month.pdf accessed 16 May 2020. 

- NCDC, 2017e. Top 1M Soil Moisture Percentile in Aug. pp. 2017. https://www.ncdc.noaa. gov/monitoring-content/sotc/drought/2017/08/noaa-ncep-nldas-ensemble-soilmoist-pct-aug17-top-1m.gif accessed 16 May 2020. 

- NDMC, 2020. United States Drought Monitor. https://droughtmonitor.unl.edu/Maps/ MapArchive.aspx accessed 15 May 2020. 

- NOAA, 2015. National Drought Overview in April 2015. https://www.ncdc.noaa.gov/ sotc/drought/201504 accessed 16 May 2020. 

- NOAA, 2017. National Drought Overview in September. pp. 2017. https://www.ncdc. noaa.gov/sotc/drought/201709 accessed 16 May 2020. 

- NOAA, 2018. National Drought Overview in February 2018. https://www.ncdc.noaa. gov/sotc/drought/201802 (accessed 17 May 2020). 

- Pathiraja, S., Moradkhani, H., Marshall, L., Sharma, A., Geenens, G., 2018. Data-driven model uncertainty estimation in hydrologic data assimilation. Water Resour. Res. 54, 1252–1280. https://doi.org/10.1002/2018WR022627. 

- Poterjoy, J., Zhang, F., Weng, Y., 2014. The effects of sampling errors on the EnKF assimilation of inner-core hurricane observations. Mon. Weather Rev. 142, 1609–1630. 

- Qiu, J., 2010. China Drought Highlights Future Climate Threats. Nature Publishing Group. 

- Reichle, R.H., Liu, Q., Koster, R.D., Crow, W.T., De Lannoy, G.J., Kimball, J.S., Ardizzone, J.V., Bosch, D., Colliander, A., Cosh, M., 2019. Version 4 of the SMAP Level-4 soil moisture algorithm and data product. J. Adv. Model. Earth Syst. https://doi.org/10. 1029/2019MS001729. 

- Rodell, M., Houser, P., Jambor, U., Gottschalck, J., Mitchell, K., Meng, C.-J., Arsenault, K., Cosgrove, B., Radakovich, J., Bosilovich, M., 2004. The global land data assimilation system. Bull. Am. Meteorol. Soc. 85, 381–394. https://doi.org/10.1175/BAMS-85-3381. 

- Sadri, S., Wood, E.F., Pan, M., 2018. Developing a drought-monitoring index for the contiguous US using SMAP. Hydrol. Earth Syst. Sci. 22, 6611–6626. https://doi.org/ 

16 

_Remote Sensing of Environment 250 (2020) 112028_ 

L. Xu, et al. 

10.5194/hess-22-6611-2018. 

- Samaniego, L., Thober, S., Kumar, R., Wanders, N., Rakovec, O., Pan, M., Zink, M., Sheffield, J., Wood, E.F., Marx, A., 2018. Anthropogenic warming exacerbates European soil moisture droughts. Nat. Clim. Chang. 8, 421. https://doi.org/10.1038/ s41558-018-0138-5. 

- Schaefer, G.L., Cosh, M.H., Jackson, T.J., 2007. The USDA natural resources conservation service soil climate analysis network (SCAN). J. Atmos. Ocean. Technol. 24, 2073–2077. https://doi.org/10.1175/2007JTECHA930.1. 

- Schlaepfer, D.R., Bradford, J.B., Lauenroth, W.K., Munson, S.M., Tietjen, B., Hall, S.A., Wilson, S.D., Duniway, M.C., Jia, G., Pyke, D.A., 2017. Climate change reduces extent of temperate drylands and intensifies drought in deep soils. Nat. Commun. 8, 14196. https://doi.org/10.1038/ncomms14196. 

- Sivakumar, M.V., Motha, R.P., 2008. Managing Weather and Climate Risks in Agriculture. Springer Science & Business Media. 

- Sklar, A., 1973. Random variables, joint distribution functions, and copulas. Kybernetika 9, 449–460. 

- Spinoni, J., Naumann, G., Vogt, J.V., Barbosa, P., 2015. The biggest drought events in Europe from 1950 to 2012. J. Hydrol. 3, 509–524. https://doi.org/10.1016/j.ejrh. 2015.01.001. 

- Srivastava, P.K., Han, D., Rico-Ramirez, M.A., Al-Shrafany, D., Islam, T., 2013. Data fusion techniques for improving soil moisture deficit using SMOS satellite and WRFNOAH land surface model. Water Resour. Manag. 27, 5069–5087. https://doi.org/ 10.1007/s11269-013-0452-7. 

- Stoffelen, A., 1998. Toward the true near-surface wind speed: error modeling and calibration using triple collocation. J. Geophys. Res. Oceans 103, 7755–7766. https:// doi.org/10.1029/97JC03180. 

- Svoboda, M., LeComte, D., Hayes, M., Heim, R., Gleason, K., Angel, J., Rippey, B., Tinker, R., Palecki, M., Stooksbury, D., 2002. The drought monitor. Bull. Am. Meteorol. Soc. 83, 1181–1190. https://doi.org/10.1175/1520-0477-83.8.1181. 

- Tapley, B.D., Bettadpur, S., Watkins, M., Reigber, C., 2004. The gravity recovery and climate experiment: Mission overview and early results. Geophys. Res. Lett. 31. https://doi.org/10.1029/2004GL019920. 

- USDA-NASS, 2018. Agricultural Statistics 2017. National Agriculture Statistics Services Washington, DC. 

Vicente-Serrano, S.M., Beguería, S., López-Moreno, J.I., 2010. A multiscalar drought 

index sensitive to global warming: the standardized precipitation evapotranspiration index. J. Clim. 23, 1696–1718. https://doi.org/10.1175/2009JCLI2909.1. 

Wang, L., Qu, J.J., 2007. NMDI: a normalized multi-band drought index for monitoring soil and vegetation moisture with satellite remote sensing. Geophys. Res. Lett. 34. https://doi.org/10.1029/2007GL031021. 

- Wang, G., Zhang, J., Jin, J., Pagano, T., Calow, R., Bao, Z., Liu, C., Liu, Y., Yan, X., 2012. Assessing water resources in China using PRECIS projections and a VIC model. Hydrol. Earth Syst. Sci. 16, 231–240. https://doi.org/10.5194/hess-16-231-2012. 

- Wang, W., Ertsen, M.W., Svoboda, M.D., Hafeez, M., 2016. Propagation of drought: from meteorological drought to agricultural and hydrological drought. Adv. Meteorol. 2016. https://doi.org/10.1155/2016/6547209. 

- Westerling, A.L., Swetnam, T.W., 2003. Interannual to decadal drought and wildfire in the western United States. EOS Trans. Am. Geophys. Union 84, 545–555. https://doi. org/10.1029/2003EO490001. 

- Xia, Y., Mitchell, K., Ek, M., Sheffield, J., Cosgrove, B., Wood, E., Luo, L., Alonge, C., Wei, H., Meng, J., 2012. Continental-scale water and energy flux analysis and validation for the north American land data assimilation system project phase 2 (NLDAS-2): 1. Intercomparison and application of model products. J. Geophys. Res.-Atmos. 117. https://doi.org/10.1029/2011JD016051. 

- Xu, L., Chen, N., Zhang, X., Chen, Z., 2018. An evaluation of statistical, NMME and hybrid models for drought prediction in China. J. Hydrol. 566, 235–249. https://doi.org/10. 1016/j.jhydrol.2018.09.020. 

- Xu, L., Chen, N., Zhang, X., 2019a. Global drought trends under 1.5 and 2° C warming. Int. J. Climatol. 39, 2375–2385. https://doi.org/10.1002/joc.5958. 

- Xu, L., Chen, N., Zhang, X., Chen, Z., Hu, C., Wang, C., 2019b. Improving the north American multi-model ensemble (NMME) precipitation forecasts at local areas using wavelet and machine learning. Clim. Dyn. 53, 601–615. https://doi.org/10.1007/ s00382-018-04605-z. 

- Yan, H., Moradkhani, H., Zarekarizi, M., 2017. A probabilistic drought forecasting framework: a combined dynamical and statistical approach. J. Hydrol. 548, 291–304. https://doi.org/10.1016/j.jhydrol.2017.03.004. 

- Yan, H., Zarekarizi, M., Moradkhani, H., 2018. Toward improving drought monitoring using the remotely sensed soil moisture assimilation: a parallel particle filtering framework. Remote Sens. Environ. 216, 456–471. https://doi.org/10.1016/j.rse. 2018.07.017. 

17 

