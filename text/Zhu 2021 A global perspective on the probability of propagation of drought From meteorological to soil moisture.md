Version of Record: https://www.sciencedirect.com/science/article/pii/S0022169421009574 Manuscript_90488f59164a98ff866d79d02ce29082 

- 1 

# **A global perspective on the probability of propagation of drought: from** 

- 2 

# **meteorological to soil moisture** 

- 3 

- 4 Authors: Ye Zhu<sup>1</sup> ·Yi Liu<sup>2</sup> * ·Wen Wang<sup>2</sup> ·Vijay P. Singh<sup>3</sup> ·Liliang Ren<sup>2</sup> 

- 5 Affiliation: 1 School of Hydrology and Water Resources, Nanjing University of Information Science and Technology, 

- 6 

210044, China 

7 

- 2 College of Hydrology and Water Resources, Hohai University, Nanjing, 210098, China 

8 

- 3 Department of Biological and Agricultural Engineering, Texas A&M University, College Station, TX 

9 

77843-2117, USA 

- 10 *Corresponding author and email address: liuyihhdx@126.com; 

- 11 

- 12 **Abstract** : With a copula-based probabilistic model, this study presents a global view on the 

- 13 propagation of meteorological to soil moisture drought. Meta-Gaussian and three-dimensional vine 

- 14 copulas were employed to construct the bivariate and trivariate conditional joint drought distributions, 

- 15 respectively, using the time series of standardized precipitation evapotranspiration index (SPEI) and 

- 16 standardized soil moisture index (SMI) derived from the Global Land Data Assimilation System 

- 17 (GLDAS) simulations. Three different cases, including the probability and magnitude of soil 

- 18 moisture drought (SMI) conditioned on 1-month meteorological drought (SPEI1), seasonal 

- 19 meteorological drought (SPEI3), and the joint effects of SPEI1 and antecedent soil moisture 

- 20 conditions (SMIlag-1), were analyzed. Then, the duration of soil moisture drought in response to 

- 21 meteorological drought, and potentially affected cropland area were analyzed to assess potential 

- 22 agricultural impacts. Results showed that the likelihood of soil moisture drought conditioned on 

> © 2021 published by Elsevier. This manuscript is made available under the Elsevier user license https://www.elsevier.com/open-access/userlicense/1.0/ 

1 

- 23 SPEI1 in the Amazon rainforest, southern and eastern China, Southeast Asia, southeastern United 

- 24 States, and west Africa was generally higher than in other regions. Under the impact of seasonal 

- 25 meteorological drought, except for the Qinghai-Tibet Plateau in China, northern Russia, and North 

- 26 Africa, the probability of soil moisture drought occurrence overall increased with significant 

- 27 increments in Europe and North America. The antecedent soil moisture condition also influenced the 

- 28 probability of drought propagation, and this effect was particularly significant for Northern China, 

- 29 Russia, the U.S. Midwest, Canada, and Australia. Spatially, the western U.S., northern Canada, South 

- 30 Africa, eastern Europe, North China, northern Russia, and most parts of Australia present longer 

- 31 duration of soil moisture drought in response to meteorological drought. Comprehensive 

- 32 considerations of the conditional probability, duration, and potentially affected area of soil moisture 

- 33 drought for croplands revealed that among five continents, South America was more vulnerable to 

- 34 agricultural drought under the condition of meteorological drought. 

- 35 **Keywords** : Drought propagation; Probability; Meteorological drought; Soil moisture drought 

2 

- 36 **1 Introduction** 

- 37 Drought is a recurring natural phenomenon that occurs in virtually every region of the world 

- 38 (Wilhite and Glantz, 1985). In the context of global warming, recent years witnessed the growing 

- 39 frequency of extreme drought events (e.g., the Millennium drought in Australia; the 2010 droughts in 

- 40 Amazon, southwestern China, and Russia; the 2011 droughts in Texas-Mexico and East Africa; and 

- 41 the U.S. summer droughts in 2012 and 2016), which caused devastating impacts on agriculture, 

42 economy, and human society (Lewis et al., 2011; Schubert et al., 2014; Hao et al. 2014; Williams et 

- 43 al., 2015; Otkin et al. 2018; Liu et al. 2020). To better cope with drought and alleviate its impacts, it 

44 is essential to understand how droughts evolve and proceed at the atmosphere-land interface. 

- 45 Using historical observations and model projections, a multitude of studies have investigated 

46 the drying or wetting patterns at regional and global scales. The drought conditions under climate 

47 change have been established using the long-term series of various drought indices and their trends 

- 48 (e.g., Sheffield et al. 2012; Dai, 2013; Wang et al. 2015; Zhu et al. 2018). Several studies extracted 

- 49 historical droughts and analyzed their magnitude or characteristics (duration, intensity, affected area, 

- 50 and severity) and spatiotemporal migration patterns, using the threshold method (Sheffield and Wood, 

- 51 2007; Herrera-Estrada et al. 2017; Zhu et al. 2019; Gu et al. 2020). Focusing on the uncertainties in 

- 52 the assessment of drought, some studies discussed the impacts of data selection (e.g., length and 

- 53 temporal coverage of data set), formulation of hydrological components (e.g., evapotranspiration), 

- 54 and drought indices (Trenberth et al. 2014). These studies provided valuable insights into trends and 

- 55 characteristics of drought; however, the links between different drought types were neglected in their 

- 56 evaluation. 

- 57 From the perspective of causative mechanisms, the evolution of drought involves a complicated 

3 

- 58 transition of moisture deficiencies. The anomalous meteorological conditions resulting in 

- 59 precipitation deficit and expanding evaporative demand can travel through the terrestrial part of the 

- 60 hydrological cycle, leading to the depletion of soil moisture and ultimately developing into a 

- 61 hydrological drought (Van Loon, 2015; Liu et al. 2017; Han et al., 2019; Hellwig et al., 2020; Wu et 

- 62 al. 2020). The transition of drought signal from one type of drought to another is referred to as 

- 63 drought propagation (Haslinger; 2014; Apurv et al., 2017). This suggests that a certain region may 64 suffer more than one drought type at the same time. Although several studies investigated the nexus 

- 65 between different drought types and drought propagation features (e.g., Van Loon and Van Lanen 

- 66 2012; Wong et al. 2013; Yang et al. 2017; Liu et al. 2019), these were mostly case studies and a 

- 67 global evaluation of drought status with the consideration of propagation behavior was rare. 

68 In this study, we focused on soil moisture drought as the direct successor of meteorological 

- 69 drought, and used a probabilistic method to depict the process of drought propagation from a global 

- 70 perspective. Two issues were addressed: One referred to the probability of soil moisture drought 

- 71 conditioned on meteorological drought (to recognize globally sensitive regions vulnerable to 

- 72 meteorological drought), and the other referred to the characteristics of soil moisture droughts based 

- 73 on the established conditional joint distributions, including the probable magnitude of soil moisture 

- 74 drought (i.e., the extent to which the soil moisture condition may be drying) given meteorological 

- 75 drought at different severity levels, the extended duration of soil moisture droughts in response to 

- 76 meteorological droughts, and potential agricultural drought risk analysis. The reminder of this paper 

- 77 is organized as follows: Section 2 provides a brief description of the study area and data used in this 

- 78 study. Section 3 describes the probabilistic model for inferring the probability of soil moisture 

- 79 drought and the corresponding drought characteristics given meteorological drought under various 

4 

- 80 scenarios. Section 4 presents the results, Section 5 discusses the findings, and conclusions are drawn 

- 81 in Section 6. 

## 82 **2 Data** 

83 **2.1 Global Land Data Assimilation System** 

84 The Global Land Data Assimilation System (GLDAS) is designed to provide globally estimated 

- 85 land surface fluxes and storages of water and energy (e.g., actual evapotranspiration, soil moisture, 

86 surface runoff, and subsurface runoff) with finer spatiotemporal resolutions (Rodell et al., 2004). The 

- 87 version 1 of GLDAS (hereafter GLDAS-1) includes four land surface models, i.e., the Mosaic, Noah, 

- 88 CLM, and VIC. Evaluation of the GLDAS-1 showed that it introduced unnatural trends and led to 

89 highly uncertain forcing fields in 1995-1997 as a result of the switched forcing data sources 90 (Beaudoing et al., 2016). Aimed at creating more climatologically consistent data sets, recently, the 

- 91 Version 2 of GLDAS (hereafter GLDAS-2) was released with the enhancement of updated model 

- 92 version (only the simulations of the Noah model are available) and land surface parameters. 

93 The GLDAS-2 consists of 3-hour, daily, and monthly (generated through temporal averaging or 94 summation of the 3-hour products) products at 0.25<sup>°</sup> and 1.0<sup>°</sup> spatial resolutions. It has two different 95 forcing data-derived components: One refers to the GLDAS-2.0, which was run entirely with the 96 Princeton meteorological forcing data, and the other was forced with a combination of model and 97 observation based forcing data sets (hereafter, GLDAS-2.1). In this study, the monthly product 

98 (including precipitation, potential evapotranspiration (PET), and soil moisture) of GLDAS-2.0 99 (GLDAS_NOAH10_M_2.0) was used for drought analysis. This product was generated through the 

- 100 temporal averaging of reprocessed 3-hour data, and is currently available from January 1948 to 

101 December 2015. 

5 

- 102 **2.2 International Soil Moisture Network** 

- 103 The International Soil Moisture Network (ISMN; https://ismn.geo.tuwien.ac.at/en/) is an 

- 104 integrated system which hosts globally quality-controlled and harmonized in-situ soil moisture 

- 105 measurements from various ground validation campaigns and operational networks (Dorigo et al., 

- 106 2011). Since its establishment, the ISMN has experienced a rapid growth with increasing number of 

- 107 participating networks and stations. At present, ISMN contains data of 59 operational networks and 

- 108 8398 field observation stations. The database stored includes soil water contents of different soil 

- 109 layers (in units of volumetric soil moisture (m<sup>3</sup> ∙m<sup>−3</sup> )), and relevant hydrometeorological variables 

- 110 (e.g., precipitation, and air and soil temperatures), and serves as an important resource for validating 

- 111 satellite retrievals and land surface model-based soil moisture products. In this study, the ISMN was 

- 112 used to validate the soil moisture datasets from GLDAS. Although the time period of the entire 

- 113 products in ISMN spanned from 1952 until the present, the long-term time series of in-situ soil 

- 114 moisture observations on a global basis are still insufficient. For instance, rather limited data are 

- 115 available in Africa and South America. Daily soil moisture data from ISMN were aggregated into 

- 116 monthly averages, and 2455 sites with the temporal data coverage exceeding 120 months were 

- 117 selected to validate the accuracy of GLDAS (see Figure 1 for spatial distribution). 

6 

118 

119 Figure 1. Map of the distribution of networks and stations contained in the ISMN. Color circles show 



120 the temporal coverage fraction for each network and station. 

121 **2.3 ESA CCI Land cover dataset** 

- 122 The global land cover product released by the European Space Agency (ESA) Climate Change 

- 123 Initiative (CCI) (https://www.esa-landcover-cci.org/) is employed for investigating the ground 

- 124 information. With the objective of providing a consistent historical land cover dataset for climate 

- 125 modeling related issues, this product is developed by merging multiple earth observation products of 

- 126 the ESA. The ESA CCI land cover dataset contains 24 consistent global land cover maps on an 

- 127 annual basis from 1992 to 2015, and the spatial resolution is 300 m. For defining land cover classes, 

- 128 the United Nations Land Cover Classification System which describes the terrestrial land surface in 

- 129 37 original classes is adopted (Defourny et al. 2017). With strict quality control and validation, the 

- 130 accuracy of the ESA CCI land cover product is approximately 71.1%, with particularly high values 

- 131 (ranging between 83% and 92%) for cropland-related classes (Defourny et al. 2017). In this study, 

- 132 the most recent map series, namely the map of 2015 (v2.0.7), was used for analysis. Given a close 

- 133 relationship between cropland and soil moisture drought, we mainly focused on three land cover 

7 

134 types, i.e., rainfed cropland, irrigated cropland, and a mixture of cropland and natural vegetation. 

- 135 **3 Methods** 

- 136 **3.1 Standardized drought index** 

- 137 The standardized precipitation evapotranspiration index (SPEI) (Vicente-Serrano et al., 2010) 

- 138 and standardized soil moisture index (SMI) (Sheffield et al., 2004) were employed to decipher 

- 139 meteorological and soil moisture droughts, respectively. These two drought indices follow the 

- 140 mathematical algorithm of the standardized precipitation index (SPI) (McKee et al., 1993), which 

- 141 uses the normal quantile transformation to standardize the index (namely to make the drought index 

- 142 spatiotemporally comparable). The difference between the two indices mainly lies in the variables 

- 143 incorporated for estimating the moisture status. For SPEI, the difference between precipitation and 

- 144 PET was taken as input, while for SMI, only the soil moisture content was considered. Like SPI, 

- 145 SPEI and SMI can also be calculated at multiple time-scales by accumulating the moisture deficits in 

- 146 any predetermined time period (e.g., 1–24 months). The SMI and SPEI share the same classification 

- 147 criteria: values of the index less than -0.5 correspond to mild drought, less than -1 to moderate 

- 148 drought, less than -1.5 to severe drought, and less than -2 to extreme drought. In this study, SMI was 

- 149 accumulated at a 1-month time scale, and SPEI was accumulated at 1-month and 3-month time scales, 

- 150 respectively (denoted as SPEI1 and SPEI3), to investigate the influence of meteorological moisture 

- 151 deficits in the current month and its cumulative effect on the soil moisture drought. 

- 152 **3.2 Probabilistic drought analysis using copulas** 

- 153 Copulas are widely used for constructing the joint distributions due to their flexibility to model 

- 154 the dependence structure among random variables regardless of their marginals. According to Sklar’s 

- 155 theorem, for _n_ -dimensional continuous random variables ( _x1_ ,…, _xn_ ) with marginal cumulative 

8 

156 distributions _F1_ ( _x1_ ),…, _Fn_ ( _xn_ ), there always exists an _n_ -copula which can combine these univariate 157 marginal distributions into a joint distribution function (Nelsen, 2007): 158 _H_ ( _x_ 1,L, _xn_ ) = _C_ ( _F_ 1 ( _x_ 1 ) ,L, _Fn_ ( _xn_ )) = _C_ ( _u_ 1,L, _un_ ) (1) 

- 159 where _H_ (.) represents the joint distribution of random variables; _C_ is the copula function satisfying 

- 160 [0,1]<sup>n</sup> → [0,1]; _Fi_ ( _xi_ ), denoted by _ui_ ( _i_ =1,…, _n_ ) in the copula function, represents the marginal 

- 161 distribution. The joint density function _f_ ( _x1,…, xn_ ) can be decomposed using the copula density 162 function as: 



- 164 where _fi_ ( _xi_ ) and _c_ represent the marginal probability density of the marginal function and the copula 

- 165 function, respectively. Based on the copula concept, the conditional distribution of these variables 

- 166 can be derived to realize probabilistic drought prediction by establishing the nonlinear dependence 

- 167 between the predictand and predictors. In this study, we used variables ( _X_ 1, _X_ 2, _X_ 3) to represent 

- 168 meteorological drought (SPEI), antecedent soil moisture condition (denoted as SMIlag-1), and soil 

- 169 moisture drought (SMI), respectively. By constructing their joint distributions, we investigated the 

- 170 probability of soil moisture drought under different scenarios: 

- 171 (1) The probability of soil moisture drought ( _X_ 3) conditioned on meteorological drought ( _X_ 1). 

- 172 (2) The probability of soil moisture drought ( _X_ 3) conditioned on meteorological drought ( _X_ 1) and 

- 173 antecedent soil moisture condition ( _X_ 2). 

- 174 Figure 2 presents the framework of copula-based probabilistic drought analysis. Obviously, the first 175 scenario belongs to a bivariate case, and the meta-Gaussian copula was employed to construct the 

- 176 joint distribution. For the second scenario, vine copulas were selected to establish the trivariate joint 

- 177 distribution. Detailed formulas for the above two types of copulas are given below. 

9 

### 178 

## **3.2.1 Meta-Gaussian Copula** 

179 Given the capability of the Gaussian copula for modeling both positive and negative 

180 dependences among random variables, the bivariate form of the Gaussian copula was employed to 

181 construct the joint distribution of ( _X1_ , _X3_ ): 

182 

183 



184 

where _Φ_ is the cumulative distribution function of the standard normal distribution function, and _Φ_<sup>_-1_</sup> 

185 

represents the corresponding inverse function; _ρ_ is the dependence parameter for the Gaussian copula; 

186 _s_ and _t_ are integral variables. Accordingly, the conditional distribution of _X3_ given _X1_ = _x1_ ’ (or _u1_ given 

_u1_ ’) can be expressed as: 

187 



188 

For the meta-Gaussian copula, the conditional distribution in equation (4) can be expressed as (Aas 

189 

et al., 2009): 

190 



191 Since both _X_ 1 and _X_ 3 are the standardized drought indices (i.e., normally distributed), it is generally 

192 reasonable to assume a multivariate normal distribution function to model their joint behavior (Wilks, 

193 2011; Hao et al., 2016). Accordingly, for normal random variables _X1_ and _X3_ with the joint normal 

194 distribution, the analytical form of the conditional distribution of _X3_ given _X1_ is given as: 

195 

_X_ 3 | _X_ 1 ~ _N_ ( **μ** _X_ |3 _X_ 1, Σ _X_ |3 _X_ 1 ) (6) 

196 where<sup>**μ**</sup> _X3_ | _X1_ and<sup>**∑**</sup> _X3_ | _X1_ represent the conditional mean (i.e., the peak of the conditional probability 

197 density distribution curve in Figure 2, and is referred to as the most probable predicted value) and 

10 

198 conditional covariance matrix, respectively, which can be derived as: 



- 201 where **_μ_** _x_ 1 and **_μ_** _x_ 3 are means of _X1_ and _X3_ , and **∑** _x_ 1 _x_ 1, **∑** _x_ 1 _x_ 3, **∑** _x_ 3 _x_ 1, and **∑** _x_ 3 _x_ 3 are the covariance matrix. 

- 202 Detailed formulas for calculating the covariance matrix can be found in Hao et al. (2016, 2017). 

203 **3.2.2 Vine Copula** 

- 204 Vine copulas are effective tools for modeling flexible dependences in high dimensions without 

- 205 requiring a conditional independence assumption (Aas et al., 2009; Liu et al., 2016; 2018). Due to its 

- 206 flexibility in dependence modeling, the vine copula shows its superiority for constructing the 

- 207 conditional dependence, asymmetries, and tail dependence. These copulas are based on pair copula 

- 208 constructions (PCCs) which decompose an _n_ -dimensional multivariate density into _n_ ( _n_ -1)/2 bivariate 

- 209 copula densities (Aas et al., 2009). For a vine copula structure, _n_ ( _n_ -1)/2 pair copulas are arranged in 

- 210 _n_ -1 trees (Kurowicka and Cooke, 2006; Brechmann et al., 2013). There are two general types of vine 

- 211 copulas, i.e., canonical vines (C-vines) and drawable vines (D-vines). In this study, we used the 

- 212 C-vines to construct the joint distribution. The _n_ -dimensional density corresponding to a canonical 

- 213 vine is given by (Aas et al., 2009): 



- 215 where _f_ ( _x_ 1,…, _xn_ ) denotes the joint density function, _f_ ( _x_ i) are the marginal densities, and _ci_ ; _i_ + _j_ |1:( _i_ -1) 

- 216 represents the bivariate copula densities. To construct the C-vine copula, five bivariate copulas (i.e., 

- 217 Student _t_ , Gaussian, Clayton, Frank, and Gumbel-Hougaard) were selected as candidate pair copulas, 

- 218 and the optimal one for each pair copula was chosen through the Akaike information criterion 

11 

222 

223 

224 

225 

226 

227 228 

229 

230 

- 219 (Schepsmeier and Brechmann, 2015). For the trivariate case, the three-dimensional density function 

- 220 can be decomposed into three bivariate copula densities and their margins: 

221 





where _c_ 12 is the abbreviated form of _c_ 1, 2( _F_ ( _x_ 1), _F_ ( _x_ 2)). 

The following step was used to to compute the conditional distribution functions and conditional bivariate copulas in equation (10). According to Joe (1996) and Aas et al. (2009), the conditional distribution function _F_ ( _x_ | _w_ ) for an _m_ -dimensional vector _w_ = ( _w_ 1,…, _wm_ ) can be obtained through the following recursive function: 



where _wj_ ( _j_ =1,…, _m_ ) denotes any element in _w_ , _w_ - _j_ represents the vector without element _wj_ , and 

_Cxwj_ | _w_ - _j_ is the bivariate copula function. Let _ui_ ( _i_ =1,…, _n_ )= _F_ ( _xi_ ). Then, the trivariate case of the 

conditional distribution function in equation (11) can be written as: 







Let 







and 







Accordingly, equation (12) can be written as: 





238 The inverse form of equation (13) can be applied for conditional simulations. Taking the bivariate 

239 case as an example, assuming _h_ ( _u_ 2| _u_ 1) is the conditional distribution function of two random 

12 

240 variables _x_ 1 and _x_ 2. For fixed probabilities _τ_ (e.g., _τ_ = 0.05, 0.1,…, 0.95), _u_ 2 can be estimated through − 1 − 1 − 1 241 an explicit function _u_ 2 = _C u_ 2 _u_ 1 (τ ; _u_ 1 ) = _h_ (τ _u_ 1 ) , where _C u_ 2 _u_ 1 is the inverse of _τ_ quantile curve 

242 of the copula (Chen et al., 2009; Xu and Childs, 2013; Liu et al., 2015). The _τ_ th copula-based 

- 243 conditional quantile function of variable _x_ 2 can be written as: 

244 

245 



- where _F_<sup>-1</sup> is the inverse of _u_ 2. 

246 

247 

248 

249 

250 

Similarly, for the trivariate case, the variable _x_ 3 given variables _x_ 1 and _x_ 2 can be derived as: 



where _θ_ 12 is the parameter of joint distribution _c_ 12 which measures the dependency of underlying conditional variables ( _x_ 1, _x_ 2). Likewise, _θ_ 13 and _θ_ 23|1 represent the parameters of _c_ 13 and _c_ 23|1, respectively. 

251 

To obtain the best estimation of _x_ 3, the Monte Carlo simulations were employed to generate 1000 

252 

- random numbers (i.e., τ) over the interval [0, 1]. Then, equation (15) was used to compute 1000 

253 

estimated values of _x_ 3, and the mean value was considered as the best estimate of _x_ 3. 

254 

## **3.3 Framework** 

255 

256 

257 

The framework of copula-based drought propagation analysis is presented in Figure 2. Employing the time series of SPEI (1-month and 3-month time scales of SPEI were employed) and SMI (1-month time scale) generated from the GLDAS simulations and ISMN soil moisture 

- 258 

- 259 

   - observations, the bivariate and trivariate conditional joint distributions were constructed with meta-Gaussion copula and C-vine copula, respectively. Taking the case of SMI and SPEI1 as an 

- 260 

- example, the values of P(SMI|SPEI1) derived from GLDAS simulations were evaluated against those 

261 

- of ISMN in-situ measurements. Then, from a global perspective, the probability and most probable 

13 

- 262 magnitude of soil moisture drought (SMI) under varying scenarios were analyzed. These included 

- 263 the bivariate cases modeled by using the meta-Gaussian copula, i.e., the probability of soil moisture 

- 264 drought conditioned on 1-month meteorological drought (SPEI1), 3-month meteorological drought 

- 265 (SPEI3), and the triavariate case derived from vine copulas, i.e., the joint effects of SPEI1 and the 

- 266 antecedent soil moisture status (SMIlag-1). Finally, based on the ESA CCI land cover map, a further 

- 267 investigation into the proportion of affected cropland area given meteorological drought was carried 

- 268 out to analyze the potential agricultural drought impacts. 

14 









269 



270 Figure 2. Framework of copula-based analysis for estimating the probability and most probable 

271 

magnitude of soil moisture drought given meteorological drought under varying scenarios. 

272 

273 

15 

- 274 

## **4 Results** 

- 275 **4.1 GLDAS and in-situ comparison** 

- 276 To provide a direct assessment on the performance of GLDAS in estimating the probability of 

- 277 drought propagation, the conditional probabilities derived from GLDAS simulations were evaluated 

- 278 against those of ISMN stations. As an example, Figure 3 exhibits the relationship between soil 

- 279 moisture and meteorological droughts of different severity levels (i.e., moderate, severe, and extreme 

- 280 droughts when SPEI/SMI was no more than -1, -1.5, and -2, respectively) for the current month (i.e., 

- 281 SPEI1 was employed). The grey error bars in the figure represent the condition when several ISMN 

- 282 stations are located in the same grid cell of GLDAS, and the probabilities derived from GLDAS 

- 283 would correspond to a couple of ISMN-based values. As expected, some disparities were observed 

- 284 between the two estimated probability series with certain scatters from the 1:1 line. The scale 

- 285 mismatch between grid-based GLDAS data and point-based ISMN could be one reason. In particular, 

- 286 for areas where soil moisture exhibited large spatial heterogeneity, the estimated probability values 

- 287 could vary significantly from one site to another (these sites were located in the same grid cell of 

- 288 GLDAS), such as the large error bars in Figure 3. In addition, since most series of ISMN were 

- 289 intermittent, the different temporal coverages of soil moisture data employed for constructing the 

- 290 propagation relationship might also contribute to the discrepancies. Aside from the above mentioned 

- 291 aspects, there was generally a good agreement between the probabilities estimated from GLDAS and 

- 292 ISMN with the majority of scatters distributed around the 1:1 line, implying that the spatial pattern 

- 293 for the probability of drought propagation revealed by these two data sets were basically comparable. 

16 

294 



295 Figure 3. Comparison of the probability of soil moisture drought derived from GLDAS simulations 

296 

297 

298 

against those of ISMN in-situ measurements. P{SMI|SPEImoderate}, P{SMI|SPEIsevere}, and P{SMI|SPEIextreme} denote the probability of soil moisture under dry conditions (i.e., SMI<-0.5) when experiencing a meteorological drought at the moderate, severe, and 

299 

300 

301 

302 

303 

extreme category, respectively. P{SMImoderate|SPEImoderate}, P{SMIsevere|SPEIsevere}, and P{SMIextreme|SPEIextreme} denote the likelihood of moderate, severe, and extreme soil moisture drought conditioned on meteorological droughts of the same levels of drought severity. The grey error bars represent the condition when several ISMN stations are located in the same grid cell of GLDAS, and the probabilities based on GLDAS would 

304 

correspond to a couple of ISMN based values. 

305 

306 

17 

- 307 **4.2 Probability of soil moisture drought** 

- 308 The probability of drought propagation from meteorological to soil moisture under three 

- 309 different cases was analyzed. Based on SMI and SPEI1, the spatial patterns of drought propagation 

- 310 from meteorological to soil moisture for the current month were first detected. Then, SPEI1 was 

- 311 replaced with SPEI3 to analyze the effect of seasonal meteorological droughts on soil moisture 

- 312 droughts. Depletion of soil moisture storage is related to the initial condition of soil layer, and in the 

- 313 third case, the antecedent soil moisture status was also employed as a conditional variable for 

- 314 constructing the joint distribution. 

- 315 **4.2.1 Probability of soil moisture drought conditioned on meteorological drought** 

- 316 Figure 4 shows the probability of soil moisture drought given meteorological drought for the 

- 317 current month (SPEI1) under eight scenarios. Specifically, panels in the same row exhibit the varying 

- 318 probabilities of soil moisture drought given gradually enhanced signal of meteorological drought (i.e., 

- 319 conditioned on moderate, severe, and extreme meteorological drought from left to right), while 

- 320 panels in the same column present the varying probabilities of soil moisture drought at mild, 

- 321 moderate, and severe levels respectively, given the same condition of meteorological drought. Taking 

- 322 the case of the first row as an example (Figures 4a, c, and f), the probability of soil moisture drought 

- 323 occurrence significantly increased conditioned on meteorological drought of severity levels from 

- 324 moderate to extreme, implying that the likelihood of soil moisture drought tended to be higher when 

- 325 the climatic condition was drier. In particular, the scenario in Figure 4f reflected a typical condition 

- 326 where most regions of the world (except the extremely dry North Africa and extremely cold 

- 327 northeastern areas in Russia) exhibited rather high values (with probabilities above 0.6) for the case 

- 328 under on an extreme condition, implying that meteorological drought of an extreme level was very 

18 

- 329 likely to propagate into soil moisture drought at a large scale. With globally low values (around 

- 330 0.1-0.3) for Figures 4b and e, they revealed another phenomenon that the likelihood of soil moisture 

- 331 drought at the same severity level as meteorological drought was generally low. Besides, different 

- 332 regional behaviors on the probability of drought propagation could also be observed. Spatially, the 

- 333 Amazon rainforest, southern and eastern China, Southeast Asia, southeastern United States, West and 

- 334 Central Africa, were more sensitive to meteorological drought with the probabilities of soil moisture 

- 335 drought two to three fold higher than were other regions (Figure 4g). 

- 336 Figure 5 shows the probability of soil moisture drought conditioned on SPEI3. It can be seen 

- 337 that except for the cases of soil moisture drought at the same severity level as meteorological drought 

- 338 (Figures 5b, e), the probability of drought propagation under the seasonal meteorological drought 

- 339 overall increased compared with Figure 4. Spatially, Europe and North America were two major 

- 340 regions which exhibited significant changes. Taking the occurrence of soil moisture drought given a 

- 341 severe condition (Figure 5c) as an example, compared to the pattern in Figure 4c, the probability of 

- 342 soil moisture drought given severe meteorological drought in Europe largely increased with the 

- 343 values varying from 0.5 to 0.8. The change in North America was mainly manifested as the enlarged 

- 344 area from the southeastern United States to the entire North America region (Figures 4c and 5c) with 

- 345 higher probability values. To explore the underlying reasons for such a spatial pattern, the regionally 

- 346 averaged time series of SPEI and SMI in different climate regions were analyzed. It can be seen that 

- 347 for the Amazon rainforest which presents the highest value of conditional probability, the SMI is 

- 348 sensitive to the changes of climatic condition and varies synchronously with SPEI (Figure 6a). A 

- 349 general good agreement between SMI and SPEI were also observed in Europe, however, for minor 

- 350 meteorological droughts such as the 1999 drought event (right panel) in Figure 6b, the soil moisture 

19 

- 351 presents no response to the dry climate condition. Similarly, the cases for the eastern and western 

- 352 U.S. (Figure 7) also suggests a good consistency between the time series of SPEI and SMI 

- 353 contributes to high conditional probability. In contrast, the Qinghai-Tibet Plateau in China, northern 

- 354 Russia, and North Africa were less affected by the seasonal cumulative water deficits, and 

- 355 maintained rather low probability values (around 0.1-0.4) even under an extreme meteorological 

- 356 drought (Figure 5f). This may be related to the specific climate and geographical conditions of these 

- 357 regions. The Qinghai-Tibet Plateau in China and northern Russia are typical permafrost and 

- 358 snow-covered regions, where snow or permafrost acts as a natural reservoir to store water when the 

- 359 temperature is below zero, and to release water to ameliorate water shortage as a result of snowmelt. 

- 360 This leads to the land surface (e.g., soil moisture, and runoff) may have a slower response to 

- 361 meteorological drought than other regions (Van Loon and Van Lanen, 2012; Qi et al., 2020; Liu et al., 

- 362 2020). As for the North Africa, it is the driest area in the world with annual mean precipitation no 

- 363 more than 50 mm. Under this tropical desert climate, the soil layer maintains a dry status all the year 

- 364 around and is insensitive to the changes of climatic condition. 

- 365 

20 

366 



<!-- Start of picture text -->
Conditioned by meteorological drought of three categories<br>Moderate Severe Extreme<br>Mild<br>Moderate<br>various drought categories<br>The probability of soil moisture drought at<br>Severe<br><!-- End of picture text -->

- 367 Figure 4. Probability of mild, moderate, and severe soil moisture drought under meteorological 

- 368 drought (indicated by SPEI1) of various severity levels (i.e., conditioned on moderate, 

- 369 severe, and extreme meteorological drought from the left column to the right column), 

- 370 

   - respectively. 

- 371 

372 



<!-- Start of picture text -->
Conditioned by meteorological drought of three categories<br>Moderate Severe Extreme<br>Mild<br>Moderate<br>various drought categories<br>The probability of soil moisture drought at<br>Severe<br><!-- End of picture text -->

373 

Figure 5. As in Figure 4 but conditioned on SPEI3. 

21 

374 

378 





375 

376 

377 

Figure 6. Regionally averaged time series of SPEI3 and SMI for (a) Amazon and (b) Europe. The 

- right panels are the amplified time series of SPEI3 and SMI for dashed rectangle marked 

drought events in the left panels. 





379 

Figure 7. As in Figure 6 but for (a) eastern and (b) western U.S. 

380 381 382 

22 

- 383 **4.2.2 Probability of soil moisture drought conditioned on meteorological drought and** 

- 384 **antecedent soil moisture condition** 

- 385 Based on equations (10)-(13), the probability of soil moisture drought conditioned on 

- 386 meteorological drought and previous SMI values (denoted as SMIlag-1) can be derived. Figure 8 

- 387 shows the likelihood of soil moisture conditioned on meteorological droughts and normal antecedent 

- 388 soil moisture conditions (-0.5<SMIlag-1<0.5). Comparing to the patterns in Figure 4, it can be seen 

- 389 that globally the probability values of soil moisture drought under the joint condition of moderate, 

- 390 severe, and extreme meteorological drought and normal antecedent soil moisture status generally 

- 391 decreased, with significant reduction (from 0.5/0.6 to 0.1/0.2) in Northern China, Russia, the 

- 392 American Midwest, Canada, and Australia. The significant changes for the conditional probability of 

- 393 soil moisture drought in these regions are possibly related to the soil moisture–temperature coupling 

- 394 effect. According to the geographical definition, these regions are mostly “transitional regions”, 

- 395 where soil moisture has been shown to have a strong influence on the land-atmospheric interactions 

- 396 via the soil moisture-temperature coupling effect (Seneviratne et al., 2010). This includes the 

- 397 feedback loops that a positive anomaly of temperature in response to a negative soil moisture 

- 398 anomaly, and increased temperature leads to a higher vapor pressure deficit and evaporative demand. 

- 399 Variations in these climate factors may contribute to a potential increase in evapotranspiration 

- 400 despite the dry conditions, which possibly leading to a further decrease in soil moisture. Obviously, 

- 401 soil moisture plays a key role for the drought propagation process from meteorological to soil 

- 402 moisture through its impact on land energy and water balances in transitional regions. Exceptional 

- 403 cases were observed for the Amazon rainforest, southern and eastern China, southeastern United 

- 404 States, west Africa, and Southeast Asia, where the probability values (above 0.7) were as high as in 

23 

- 405 Figure 4, indicating that the effect of antecedent soil moisture in these regions was generally minor. 

406 



<!-- Start of picture text -->
(a) P{SMI|SPEI1moderate, SMIlag-1normal} (b) P{SMI|SPEI1severe, SMIlag-1normal}<br>(c) P{SMI|SPEI1extreme, SMIlag-1normal}<br><!-- End of picture text -->

- 407 Figure 8. Probability of soil moisture drought under the joint condition of (a) moderate, (b) severe, 

- 408 and (c) extreme meteorological drought (indicated by SPEI1) and normal antecedent soil 

- 409 moisture status (i.e., -0.5＜SMIlag-1＜0.5). 

## **4.3 Magnitude of soil moisture drought** 

- 410 **4.3 Magnitude of soil moisture drought** 411 Apart from the probability of soil moisture drought, it is also essential to figure out the most 

- 412 probable magnitude of drought (e.g., moderate or severe drought), which has significance for 413 drought mitigation and drought early warning. Based on the conditional probability distribution, the 

- 414 SMI values could be estimated through equations (7) and (15) for the bivariate (i.e., SMI conditioned 

- 415 on SPEI) and trivariate cases (i.e., SMI conditioned on SPEI and SMIlag-1), respectively. This may 416 produce SMI values of a wide range but with different probabilities (see the conditional probability 417 density distribution curve in Figure 2). For example, supposing the estimated range of SMI under a 418 severe meteorological drought (i.e., -1.5<=SPEI<-2) is -1.5 to 0.3, this suggests the magnitude of soil 

- 419 moisture drought might be one of the normal, mild, and moderate drought categories. From the 

24 

- 420 conditional probability density distribution curve, we can see that the likelihood becomes larger 

- 421 when the interval of estimated SMI values getting close to the mean. Obviously, the interval of 

- 422 estimated SMI values mostly close to mean is the most probable magnitude of a soil moisture 

- 423 drought, and is exactly the information we are concerned. Figure 9 exhibits the extent to which the 

- 424 soil moisture condition may be drying under six different scenarios. It can be seen that the estimated 

- 425 magnitude of soil moisture drought conditioned on SPEI1 was generally comparable to that 

- 426 conditioned on SPEI1 and SMIlag-1 (e.g., Figure 9a versus 9d). For most parts of the world, a 

- 427 moderate meteorological drought may cause little effect on the soil moisture condition, while severe 

- 428 and extreme meteorological drought may lead to mild soil moisture drought. However, for sensitive 

- 429 regions, such as the Amazon rainforest, southern and eastern China, west Africa, southeastern United 

- 430 States, and Southeast Asia, a mild soil moisture drought is likely to occur given moderate 

- 431 meteorological drought, and the soil moisture condition may become more drier given severe or 

- 432 extreme meteorological drought. 

25 

### (a) Conditioned by SPEImoderate 



<!-- Start of picture text -->
(d) Conditioned by SPEImoderate and SMIlag-1normal<br><!-- End of picture text -->





























<!-- Start of picture text -->
(b) Conditioned by SPEIsevere<br>(c) Conditioned by SPEIextreme<br><!-- End of picture text -->



<!-- Start of picture text -->
(e) Conditioned by SPEIsevere and SMIlag-1normal<br>(f) Conditioned by SPEIextreme and SMIlag-1normal<br><!-- End of picture text -->























433 



- 434 Figure 9. Magnitude of soil moisture drought under different scenarios. The left column shows the 

- 435 cases conditioned on SPEI1, while the right column shows the cases under the joint 

- 436 condition of SPEI1 and SMIlag-1normal. 

- 437 **4.4 Extended duration of soil moisture drought** 

- 438 The duration of soil moisture droughts provides important information for estimating potential 

- 439 drought impacts on crop productivity. To investigate how the meteorological droughts affect the 

- 440 duration of soil moisture drought, Figure 10 compares the average duration of soil moisture drought 

- 441 events (SMI1) against that of meteorological drought events (SPEI1). Positive values indicate soil 442 moisture drought lasts longer than meteorological drought, and negative values indicate soil moisture 

- 443 drought lasts shorter than meteorological drought. As shown in Figure 10, for most regions of the 

26 

- 444 world, the duration of soil moisture drought is overall longer than that of meteorological drought. 

- 445 This phenomenon is generally consistent with findings of previous studies (e.g., Van Loon, 2015), 

- 446 which claimed that the duration of drought would be lengthened during the drought propagation 

- 447 process from atmosphere to the land surface. Given different climates and underlying surfaces, the 

- 448 terrestrial water storage (e.g., soil moisture, surface water, and groundwater) may present different 

- 449 responses with lengthened duration of varying degrees. Spatially, the western U.S., northern Canada, 

- 450 South Africa, eastern Europe, North China, northern Russia, and most parts of Australia present 

- 451 larger values, where the average duration of soil moisture drought events are more than three months 

- 452 longer than that of meteorological drought events. The time series of SPEI3 and SMI1 for selected 

- 453 regions in Figures 6 and 7 also revealed this difference in terms of drought duration. For instance, 

- 454 from Figures 6 and 7 it can also be seen that in regions with low conditional probabilities like Europe 

- 455 and western U.S. (climatically Europe is drier than Amazon, and western U.S. is drier than eastern 

- 456 U.S.), although the meteorological droughts do not immediately initiate soil moisture droughts, once 

- 457 the soil moisture droughts do get initiated, they last longer than meteorological droughts. This is 

- 458 consistent with findings in Sheffield et al. (2004) which also showed higher persistence of soil 

- 459 moisture droughts in western U.S. compared to eastern U.S. Several grids in the west and north 

- 460 Africa are the exception, where negative values were observed. This suggests the soil moisture 

- 461 drought events on average, persist shorter than meteorological drought events. Meanwhile, it should 

- 462 be noted that the uncertainties of GLDAS in west and north Africa may also be responsible for these 

- 463 negative values (see details in Section 5.1). 

27 

464 



465 Figure 10. The average extended duration of soil moisture drought (SMI1) comparing to 

466 meteorological drought (SPEI1). Positive values indicate soil moisture drought lasts 467 longer than meteorological drought, and negative values indicate soil moisture drought 468 lasts shorter than meteorological drought. 

469 

## **4.5 Global agricultural drought impact analysis** 

470 Soil moisture has a close relationship with crop productivity, and one of the major impacts of 

- 471 soil moisture drought is agricultural losses (croplands) which threaten the food security. When a 

- 472 meteorological drought occurs, the likelihood of a soil moisture drought in different regions could be 

- 473 estimated through their conditional joint distributions. The occurrence of a soil moisture drought 

- 474 means reduced supply of moisture to the cropland, thus estimated conditional probability of the dry 

- 475 condition in soil layer may have some implications for recognizing the potential agricultural drought 

- 476 impacts. Besides, the duration of soil moisture drought (reflecting the persistence of moisture deficits 

- 477 of the soil layer), and its spatial coverage (reflecting how much area suffers from droughts) are also 

- 478 informative for estimating the strength of agricultural impacts. In this section, comprehensive 

- 479 considerations of drought propagation features, including the conditional probability, extended 

28 

- 480 duration, and affected area of soil moisture droughts in response to meteorological droughts for 

- 481 croplands were provided to assess globally potential agricultural drought impacts. 

- 482 Figure 11 presents the spatial distribution of croplands, and the proportion of affected crop area 

- 483 by mild, moderate, severe, and extreme drought given meteorological drought (indicated by SPEI1) 

- 484 for globe and each continent. As shown in Figure 11a, according to the ESA CCI Land cover dataset 

- 485 (v2.0.7), Asia (mainly distributed in China, India, and Southeast Asia) ranked first among the five 

- 486 continents which accounted for 34% of the global cropland area, followed by Europe (22%), Africa 

- 487 (17%), North America (13%), South America (11%), and Oceania (3%). From a global perspective 

- 488 (Figure 11b), it can be seen that a moderate meteorological drought may lead to approximately 44% 

- 489 of the crop area falling under soil moisture drought, and the potential agricultural drought impacts 

- 490 may be further enlarged (78% of the crop area for mild drought, and 10% for moderate drought) 

- 491 given a severe meteorological drought (i.e., SPEI<=-2). When the climatic condition becomes 

- 492 extreme, the affected crop area may increase to 98%, with 60% for mild drought, 35% for moderate 

- 493 drought, and 3% for severe drought. As the largest crop production base, Asia generally presents a 

- 494 pattern similar to that of the globe conditioned on a moderate and severe meteorological drought. 

- 495 However, for the extreme scenario, 7% of the crop area may suffer from severe drought, which is 

- 496 two-fold higher than the global value (Figure 11c). With regard to drought duration, Figure 10 

- 497 suggests the North China on average presents higher persistence of soil moisture droughts (may last 

- 498 for three to six months) in response to meteorological droughts, and are more vulnerable to 

- 499 agricultural disaster than other regions of Asia. For Europe, the affected crop area rapidly reaches up 

- 500 to 97% under a moderate meteorological drought (i.e., -1<SPEI1<=-1.5). Although such increments 

- 501 are mostly under mild dry condition (Figure 11d), the moisture deficits may cause substantial 

29 

- 502 damages for crop production given the overall long extended duration (persist three to six months on 

- 503 average, and negative anomalies of soil moisture over a long time especially in growing seasons may 

- 504 be harmful for crop growths) of soil moisture droughts in this continent (Figure 10). In terms of 

- 505 Africa and North America, the affected crop area conditioned on different values of SPEI1 is slightly 

- 506 lower than that of the globe (Figures 11e, f), and the middle U.S. is more likely to suffer agricultural 

- 507 losses in consideration of the longer duration of soil moisture droughts in this region (Figure 10). 

- 508 The case for South America is not optimistic, either. Although Figure 10 suggests the soil moisture 

- 509 drought for cropland in this continent would not persist for a long time, it may also induce large 

- 510 agricultural impacts when referring to the affected area of each drought category. As shown in Figure 

- 511 11g, 77% of the crop area may fall under drought given a mild meteorological drought (i.e., 

- 512 -0.5<SPEI1<=-1), while 69% may suffer from moderate drought when SPEI1 is no more than -2. 

- 513 These proportion values are approximately two-fold higher than the global average, suggesting that 

- 514 South America is more vulnerable to agricultural drought than other continents. 

- 515 

30 

516 





- 517 Figure 11. (a) Map of cropland distribution and proportion of cropland area for each continent. (b-g) 

- 518 The six rectangle panels show the proportion of affected crop area by mild, moderate, 

519 

   - severe, and extreme drought given meteorological drought (indicated by SPEI1) for globe 

- 520 and each continent. 

521 **5 Discussion** 

522 **5.1 Uncertainties** 

- 523 Some uncertainties may exist for the derived results regarding the selection of drought indices， 

- 524 time series of drought indices selected for constructing the conditional probability distribution, and 

- 525 GLDAS datasets. First, SPEI was employed in which precipitation and PET are treated equally for 

- 526 calculating the atmospheric moisture condition. Several previous studies claimed that the role of PET 

- 527 would be overestimated for estimating the dry status, particularly in arid zones (e.g., Cook et al., 

- 528 2014; Ma et al., 2014). To evaluate the impact of SPEI on the probability of drought propagation, the 

31 

- 529 derived results were compared with those derived from SPI. We found in most regions of the world, 

- 530 the probability of soil moisture drought derived from SPEI is very close to that derived from SPI, 

- 531 which also suggest high probabilities in the Amazon rainforest, southern and eastern China, 

- 532 Southeast Asia, southeastern U.S., West and Central Africa (see supplementary Figures S1 and S2). 

- 533 Major differences are mainly located in water limited regions (e.g., the north Africa and northwestern 

- 534 China), where the probability of soil moisture drought derived from SPEI is about 0.2 lower than 

- 535 those from SPI (Figure 12). For arid areas, PET (i.e., the evaporative demand by the atmosphere 

- 536 which represents the highest possible evapotranspiration) commonly far exceeds the actual moisture 

- 537 supply, which may lead to the overestimation of the actual amount of water transferred to the 

- 538 atmosphere (Raible et al., 2017). This leads to the climatic condition indicated by SPEI may present 

- 539 a dry signal, but the soil moisture would not make a response, resulted in a lower probability value 540 than derived from SPI. 

- 541 Second, the conditional probabilities were calculated by using complete time series of SPEI and 

- 542 SMI, and there are uncertainties for estimating agricultural impacts (Figure 11) since the periods of 

- 543 drought indices in growing seasons are more relevant for obtaining realistic implications of drought 

- 544 propagation. To evaluate the influence of time series, the conditional probabilities by using data of 

- 545 growing seasons were compared against those from complete time series. According to the frequency 

- 546 distributions of the probability of soil moisture drought conditioned on moderate meteorological 

- 547 drought (indicated by SPEI1 as an example) in Figure 13, it can be seen that the probability values 

- 548 derived from data of growing seasons (red dashed line) overall increase by 0.1 comparing to those 

- 549 derived from complete time series (the blue dashed line). Figure 14 exhibits the spatial distribution of 

- 550 probability differences. Except for northern Canada, South Africa, western and southern Russia 

32 

- 551 where the absolute values of probability difference range between 0.1 and 0.2, for most regions of 

- 552 the world, the differences of probability values would not exceed 0.05, plus or minus. This suggests 

- 553 there would be tiny differences for estimated probability values between complete series and data of 

- 554 growing seasons, but the associated global patterns of drought propagation (e.g., Figs. 4−11) would 555 not change in a significant way. 

- 556 Finally, limitations of the land surface model (e.g., the inadequate consideration of snow-related 

- 557 processes in cold regions and irrigation schemes) used in GLDAS also influence the quality of the 

- 558 simulated datasets, and therefore for the conditional probability. For instance, comparing to in-situ 

- 559 observations, Chen et al. (2013) found the four GLDAS models do not perform well in simulating 

- 560 the surface soil moisture in central Tibetan Plateau. Agutu et al. (2017) assessed the performance of 

- 561 GLDAS in characterizing agricultural drought in East African, and found GLDAS perform well in 

- 562 Tanzania but mischaracterized the 2005-2006 drought in Kenyan and Ugandan. Zaitchik et al., (2010) 

- 563 evaluated the performance of GLDAS in terms of global river discharge and found poor 

- 564 performances in Congo River and high-latitude basins with snowmelt, which may have associated 

- 565 effects on the accuracy of soil moisture estimates. In addition, the land surface models used in 

- 566 GLDAS do not include the modules of irrigation schemes (a common drawback for most global 

- 567 model simulation products), and there are uncertainties for irrigated cropland (Figure 11). For 

- 568 instance, based on hydrological model simulations, several previous studies found irrigation leads to 

- 569 increased evapotranspiration, decreased runoff, increased surface soil moisture, and decreased 

- 570 streamflow (Haddeland et al., 2006; Ozdogan et al., 2010; Shah et al., 2021). From a climatic 

- 571 perspective, several studies found irrigation would impact the water and energy balance near the 

- 572 ground, making the near-surface atmosphere cooler and moister than non-irrigated areas (Kueppers 

33 

- 573 et al., 2007; Mishra et al., 2020). This cooling effect may create a favorable condition for drought 

- 574 propagation. Therefore, we may speculate that the probability of soil moisture drought under 

- 575 meteorological drought may be underestimated to some extent for irrigated croplands (e.g., northern 

- 576 India and the North China) in growing seasons. In spite of such limitations, Kim et al. (2020) found 

- 577 the soil moisture datasets from GLDAS generally perform better than certain satellite-based soil 

- 578 moisture products over moderately irrigated areas and is recommended for use when ground-based 

- 579 soil moisture data are not available. In future researches, it is necessary to conduct regional studies 

- 580 by using more sophisticated hydrological models in high resolution to reflect more realistic 

- 581 information of drought propagation for irrigated croplands. 

- 582 



- 583 Figure 12. The difference of probability between SPEI1_SMI and SPI1_SMI. Positive values 

- 584 indicate the probability of soil moisture drought conditioned on SPEI1 is higher than 

- 585 that conditioned on SPI1, and vice versa. 

34 

586 



<!-- Start of picture text -->
Whole<br>25<br>Growing season<br>20<br>15<br>10<br>5<br>0<br>0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8<br>P{SMI|SPEImoderate}<br>Frequency (%)<br><!-- End of picture text -->

587 Figure 13. The frequency distribution of the probability of soil moisture drought conditioned on 

588 

moderate meteorological drought (indicated by SPEI1) calculated from complete time 

589 

590 

series (blue dashed line) and time series of growing seasons (red dashed line). 



591 Figure 14. The difference of probability of soil moisture drought under moderate meteorological 

592 

drought (indicated by SPEI1) by using the time series of growing seasons and complete 

593 

time series. 

594 

35 

## 595 **5.2 Implications** 

- 596 Previous studies for analyzing the process of drought propagation from meteorological to 

- 597 agricultural, or hydrological mostly focused on the drought characteristics of different types, with 

- 598 some features associated with lagging, lengthening, and attenuation recognized (van Loon, 2015; 

- 599 Apurv et al. 2017; Liu et al. 2019). From a probabilistic perspective, this study uses a copula-based 

- 600 model to estimate the likelihood of soil moisture droughts conditioned on meteorological droughts of 

- 601 varying severity levels. This probability value could be interpreted as the strength of drought signal 

- 602 during the propagation process, where higher values imply that most of the drought information 

- 603 would be conveyed into the territorial hydrological system, and soil moisture droughts are more 

- 604 likely to be initiated if a meteorological drought occurs. It should be noted that this probability value 

- 605 has essential distinctions from aridity, or the frequency of droughts. As shown in Fig. 4, humid 

- 606 regions such as the Amazon rainforest and southern China present higher probability values than arid 

- 607 regions such as the north Africa. This phenomenon is not in contradiction with previous findings 

- 608 associated with the global patterns of drying trends (e.g., arid lands become more drier). Instead, Fig. 

- 609 4 suggests that under the same meteorological drought conditions, regions in higher probability 

- 610 values like the Amazon rainforest and southern China are more vulnerable to soil moisture drought 611 than north Africa. 

- 612 In this study, we found the likelihood of soil moisture drought conditioned on SPEI1 was 

- 613 generally higher in Amazon rainforest, southern and eastern China, Southeast Asia, southeastern 

- 614 United States, and west Africa than in other regions. Comparison of SPEI and SMI in different 

- 615 climate regions suggests for high probability regions, the time series of SMI generally presents a 

- 616 good consistency with SPEI, and is sensitive to the changes of climate condition (Figures 6, 7). From 

36 

- 617 a climatic perspective, these regions are mostly in subtropical and tropical climate with sufficient 

- 618 precipitation (i.e., water supply) and high temperature (i.e., evaporative demand). A climatic dry spell 

- 619 suggests less water input (i.e., precipitation deficiency) is transported to the terrestrial system. At the 

- 620 same time, PET may also increase (resulted from increased temperature, radiation, wind speed, etc.) 

- 621 which can lead to boosted actual evapotranspiration with an extra loss of water from soil, vegetation, 

- 622 or open water bodies (Seneviratne et al. 2010). All these contribute to the depletion of soil moisture, 

- 623 which may further develop into a soil moisture drought. The moisture and heat condition produces a 

- 624 close hydraulic relation among precipitation, evapotranspiration, and soil moisture (Chagas and 

- 625 Chaffe, 2018; Yang et al. 2018), leading to a strong nexus between meteorological and soil moisture 

- 626 droughts. Similar to previous studies (e.g., Vicente-Serrano et al., 2005; Peña-Gallardo et al., 2019) 

- 627 which related accumulated SPEI of varying time scales to hydrological variables, the time scale 

- 628 effect of droughts was also observed in this study. As shown in Figure 5, the North America and 

- 629 Europe present significant increments in the probability values of soil moisture drought conditioned 

- 630 on SPEI3 than those conditioned on SPEI1 (Figure 4). This reflects the cumulative effects of 

- 631 meteorological water deficits on drought propagation. Meanwhile, the enhanced probabilistic link 

- 632 under SPEI3 in these regions also indicate a lagged (or slower) response of soil moisture to the 

- 633 climatic condition than regions of high probability values (e.g., the Amazon rainforest). This 

- 634 phenomenon agrees with findings in Bachmair et al. (2018) which also suggest the 3-month 635 meteorological drought indices are best linked to agricultural and forest droughts. 

- 636 Apart from the current meteorological condition, we found that the antecedent soil moisture 

- 637 status also influences the probability of drought propagation. Comparing to the patterns in Fig. 4, Fig. 

- 638 8 shows that under the joint condition of meteorological droughts (indicated by SPEI1) and normal 

37 

- 639 antecedent soil moisture status (-0.5<SMIlag-1<0.5), the likelihood of soil moisture drought 

- 640 significantly decreases in the Northern China, the U.S. Midwest, Australia, Russia, and Canada. 

- 641 According to the geographical definition, these regions are mostly “transitional regions”, where soil 

- 642 moisture has been shown to have a strong influence on the land-atmospheric interactions via the soil 

- 643 moisture-temperature coupling effect (Seneviratne et al., 2010). This includes the feedback loops that 

- 644 a positive anomaly of temperature in response to a negative soil moisture anomaly, and increased 

- 645 temperature contributes to a higher vapor pressure deficit and evaporative demand, which possibly 

- 646 leading to a further decrease in soil moisture (van Loon, 2015). This shows the key role of soil 

- 647 moisture in affecting the land energy and water balances in transitional regions, which is also the 

- 648 core content of drought propagation process from meteorological to soil moisture. 

- 649 Findings in this study highlight the varied responses of soil moisture to meteorological drought 

- 650 under different moisture conditions (both the atmospheric and the antecedent soil moisture status). 

- 651 Despite the uncertainties discussed above, the probability of drought propagation provides some 

- 652 implications for recognizing the potential impacts of soil droughts (Figure 11), which also has 

- 653 scientific guidance for water security assessment and drought management. Ongoing analysis on the 

- 654 propagation behavior in different stages (e.g., onset, recover) of drought, and the seasonality in 

- 655 different regions are needed for improving the understanding of drought propagation mechanism. 

- 656 **6 Conclusions** 

- 657 In this study, a copula based probabilistic model (i.e., the meta-Gaussian and vine copulas for 

- 658 bivariate and trivariate cases, respectively) was employed to illustrate the propagation of 

- 659 meteorological to soil moisture drought. Three different cases, including the probability of soil 

- 660 moisture drought (SMI) conditioned on 1-month meteorological drought (SPEI1), seasonal 

38 

- 661 meteorological drought (SPEI3), and the joint effects of SPEI1 and antecedent soil moisture 

- 662 conditions (SMIlag-1) were investigated. Based on the established conditional joint distributions, the 

- 663 characteristics of drought propagation, including the probable magnitude of soil moisture drought 

- 664 (i.e., the extent to which the soil moisture condition may be drying), the extended duration of soil 

- 665 moisture droughts in response to meteorological droughts, and potential agricultural drought risks 

- 666 

   - were analyzed. 

- 667 Results showed that the likelihood of soil moisture drought given SPEI1 tended to be higher 

- 668 when the meteorological condition was drier. Spatially, the Amazon rainforest, southern and eastern 

- 669 China, Southeast Asia, southeastern United States, and west Africa were more sensitive to 

- 670 meteorological drought with high probabilities. Under the impact of seasonal meteorological drought, 

- 671 the probability of soil moisture drought occurrence overall increased with significant increments in 

- 672 Europe and North America. In contrast, the Qinghai-Tibet Plateau in China, northern Russia, and 

- 673 North Africa were less affected and maintained rather low probability values when conditioned on 

- 674 SPEI1. The antecedent soil moisture condition also influenced the probability of drought propagation, 

- 675 and this effect was particularly significant for Northern China, Russia, the American Midwest, 

- 676 Canada, and Australia. In terms of the probable magnitude of soil moisture drought, a moderate 

- 677 meteorological drought may cause little effect on the soil moisture condition, while severe and 

- 678 extreme meteorological drought may lead to mild soil moisture drought for most parts of the world. 

- 679 Investigation on drought duration suggests the persistence of drought would be lengthened during the 

- 680 drought propagation process from meteorological to soil moisture, with spatially longer duration of 

- 681 soil moisture drought in the western U.S., northern Canada, South Africa, eastern Europe, North 

- 682 China, northern Russia, and most parts of Australia. 

39 

683 A further investigation into the affected cropland area revealed that a moderate meteorological 

- 684 drought may lead to approximately 44% of the cropland falling under drought, and the potential 

- 685 agricultural drought impacts may be further enlarged (78% of the crop area for mild drought, and 

- 686 10% for moderate drought) given severe meteorological drought. When the climatic condition 

- 687 becomes extreme, the affected cropland area may increase to 98%, with 60% for mild drought, 35% 

- 688 for moderate drought, and 3% for severe drought. With overall higher proportions of the affected 

- 689 cropland area than the global averages, South America is most likely to suffer from agricultural 

- 690 drought under meteorological drought, followed by Asia, Africa and North America. Europe is more 

- 691 sensitive to meteorological drought with 97% of the crop area may be affected under a moderate 

- 692 meteorological drought. Although these are mostly under mild dry condition, they could be 

- 693 damaging to agricultural production given the overall long duration of soil moisture droughts. 

- 694 From a global perspective, the above results provide a spatial image of the likelihood of soil 

- 695 moisture drought conditioned on moderate, severe, and meteorological droughts, which also have 

- 696 implications for drought prevention and mitigation strategies in the context of global warming. 

- 697 **CRediT author statement** 

- 698 Ye Zhu: Conceptualization, Validation, Investigation, Writing-Original draft. Yi Liu: Data curation, 

- 699 Methodology, Software, Resources. Wen Wang: Formal analysis, Supervision. Vijay P. Singh: 

- 700 Writing- Reviewing and Editing. Liliang Ren: Software, Resources. 

- 701 **Acknowledgments** 

- 702 This work was supported by the National Natural Science Foundation of China (nos., 41901037; 

- 703 41807165; 41971042), the National Natural Science Foundation of Jiangsu Province, China (Grant 

- 704 No. BK20180512), and the Natural Science Foundation of the Jiangsu Higher Education Institutions 

40 

- 705 of China (19KJB170023). The simulations of GLDAS for calculating SPEI and SMI are available at 

- 706 https://ldas.gsfc.nasa.gov/gldas. The soil moisture data of ISMN can be downloaded from 

- 707 https://ismn.geo.tuwien.ac.at/en/.The global land cover product released by the ESA CCI is archived 

- 708 at https://www.esa-landcover-cci.org/. 

- 709 **References:** 

- 710 Aas K, Czado C, Frigessi A, et al. (2009). Pair-copula constructions of multiple dependence[J]. 

- 711 Insurance: Mathematics and economics, 44(2): 182-198. 

- 712 Agutu, N.O., Awange, J.L., Zerihun, A., Ndehedehe, C.E., Kuhn, M., Fukuda, Y., 2017. Assessing 713 multi-satellite remote sensing, reanalysis, and land surface models' products in characterizing 714 agricultural drought in East Africa. Remote Sens. Environ. 194, 287–302. 

- 715 https://doi.org/10.1016/j.rse.2017.03.041. 

- 716 Apurv T, Sivapalan M, Cai X, et al. (2017). Understanding the Role of Climate Characteristics in 

- 717 Drought Propagation[J]. Water Resources Research, 53(11): 9304-9329. 

- 718 Bachmair S, Tanguy M, Hannaford J, et al. (2018). How well do meteorological indicators represent 

- 719 agricultural and forest drought across Europe?[J]. Environmental Research Letters, 13, 034042. 

- 720 Brechmann, E. C., K. Hendrich, and C. Czado (2013). Conditional copula simulation for systemic 721 risk stress testing, Insur. Math. Econ., 53(3), 22–732. 

- 722 Chagas V B P, Chaffe P L B. The Role of Land Cover in the Propagation of Rainfall Into Streamflow 

- 723 Trends[J]. Water Resources Research, 2018, 54(9). 

- 724 Chen Y., Yang K., Qin J., et al. Evaluation of AMSR-E retrievals and GLDAS simulations against 

- 725 observations of a soil moisture network on the central Tibetan Plateau[J]. Journal of Geophysical 

- 726 Research: Atmospheres, 2013, 118(10):4466-4475. 

41 

- 727 Chen, X., R. Koenker, and Z. Xiao (2009). Copula-based nonlinear quantile autoregression, Econ. J., 

- 728 12, 50–67. 

- 729 Cook, B.I., Smerdon, J.E., Seager, R., et al., 2014. Global warming and 21st century drying. Clim. 730 Dyn. http://dx.doi.org/10.1007/s00382-014-2075-y. 

- 731 Dai A, (2013). Increasing drought under global warming in observations and models. Nature climate 732 change, 3(1): 52-58. 

- 733 Defourny, P., S. Bontemps, C. Lamarche, C. Brockmann, M. Boettcher, J. Wevers, and G. Kirches. 

- 734 2017. Land Cover CCI: Product User Guide Version 2.0. 

- 735 Dorigo, W.A., Wagner, W., Hohensinn, R., et al. (2011). The International Soil Moisture Network: A 

- 736 data hosting facility for global in situ soil moisture measurements, Hydrology and Earth System 737 Sciences, 15 (5), 1675-1698. 

- 738 Gu L, Chen J, Yin J, et al. Drought hazard transferability from meteorological to hydrological 739 propagation. Journal of Hydrology, 2020: 124761. 

- 740 Han Z, Huang S, Huang Q, et al. Propagation dynamics from meteorological to groundwater drought 

- 741 and their possible influence factors. Journal of Hydrology, 2019, 578: 124102. 

- 742 Hao Z, AghaKouchak A, Nakhjiri N, et al. (2014). Global integrated drought monitoring and 743 prediction system. Scientific data, 1: 140001. 

- 744 Hao Z, Hao F, Singh V P, et al. (2016). Probabilistic prediction of hydrologic drought using a 745 conditional probability approach based on the meta-Gaussian model. Journal of Hydrology, 542: 746 772-780. 

- 747 Hao Z, Hao F, Singh V P, et al. (2017). Quantitative risk assessment of the effects of drought on 

- 748 extreme temperature in eastern China. Journal of Geophysical Research: Atmospheres, 122(17): 

42 

- 749 

## 9050-9059. 

- 750 Haslinger, K., Koffler, D., Schoner, W., & Laaha, G. (2014). Exploring the link between 

- 751 meteorological drought and streamflow: Effects of climate-catchment interaction. Water 752 Resources Research, 50(3), 2468-2487. 

- 753 Hellwig, J., De Graaf, I. E., Weiler, M., & Stahl, K. (2020). Large scale assessment of delayed 

- 754 groundwater responses to drought. Water Resources Research, 56(2). 

- 755 Herrera-Estrada J E, Satoh Y, Sheffield J. Spatiotemporal dynamics of global drought[J]. 756 Geophysical Research Letters, 2017, 44(5): 2254-2263. 

- 757 Joe, H. (1996), Families of m-variate distributions with given margins and m(m  1)/2 dependence 

- 758 parameters, in Distributions With Fixed Marginals and Related Topics, edited by L. Rüschendorf, 

- 759 B. Schweizer, and M. D. Taylor, pp. 120–141, Inst. Math. Stat., Hayward, Calif. 

- 760 Kim H, Wigneron J P, Kumard S, et al. Global scale error assessments of soil moisture estimates 

- 761 from microwave-based active and passive satellites and land surface models over forest and mixed 

- 762 irrigated/dryland agriculture regions[J]. Remote Sensing of Environment, 2020, 251. 

- 763 Kueppers L M, Snyder M A, Sloan L C. Irrigation cooling effect: Regional climate forcing by 

- 764 land-use change[J]. Geophysical Research Letters, 2007, 34(3):doi:10.1029/2006GL028679. 

- 765 Kurowicka, D., R. Cooke (2006). Uncertainty Analysis with High Dimensional Dependence 

- 766 Modelling, Wiley, Chichester. 

- 767 Lewis S L, Brando P M, Phillips O L, et al. (2011). The 2010 amazon drought. Science, 331(6017): 

- 768 554-554. 

- 769 Liu Y, Zhu Y, Ren L, et al. (2017). A multiscalar Palmer drought severity index. Geophysical 

- 770 Research Letters, 44(13): 6850-6858. 

43 

- 771 Liu Y, Zhu Y, Ren L, et al. (2019). Understanding the Spatiotemporal Links Between Meteorological 

- 772 and Hydrological Droughts From a Three-Dimensional Perspective. Journal of Geophysical 

- 773 Research: Atmospheres, 124(6): 3090-3109. 

- 774 Liu Y, Zhu Y, Zhang L, et al. (2020). Flash droughts characterization over China: From a perspective 

- 775 of the rapid intensification rate. Science of The Total Environment, 704: 135373. 

- 776 Liu Z, Cheng L, Hao Z, et al. (2018). A framework for exploring joint effects of conditional factors 

- 777 on compound floods. Water Resources Research, 54(4): 2681-2696. 

- 778 Liu Z, Törnros T, Menzel L. (2016). A probabilistic prediction network for hydrological drought 

- 779 identification and environmental flow assessment. Water Resources Research, 2016, 52(8): 780 6243-6262. 

- 781 Liu Z, Zhou P, Chen X, et al. (2015). A multivariate conditional model for streamflow prediction and 

- 782 spatial precipitation refinement. Journal of Geophysical Research: Atmospheres, 120(19): 783 10,116-10,129. 

- 784 Ma M W, Ren L L, Yuan F, Jiang S H, Liu, Y, Kong H, Gong L Y. (2014). A new standardized Palmer 

- 785 drought index for hydro-meteorological use. Hydrol. Process. 

- 786 http://dx.doi.org/10.1002/hyp.10063. 

- 787 McKee T B, Doesken N J, Kleist J. (1993). The relationship of drought frequency and duration to 

- 788 time scales[C]//Proceedings of the 8th Conference on Applied Climatology, 17(22): 179-183. 

- 789 Mishra V, Ambika A K, Asoka A, et al. Moist heat stress extremes in India enhanced by irrigation[J]. 

- 790 Nature Geoscience, 2020, 13(11):1-7. 

- 791 Nelsen R B. (2007). An introduction to copulas. Springer Science & Business Media. 

- 792 Otkin J A, Svoboda M, Hunt E D, et al. (2018). Flash droughts: a review and assessment of the 

44 

- 793 challenges imposed by rapid-onset droughts in the United States. Bulletin of the American 794 Meteorological Society, 99(5): 911-919. 

- 795 Ozdogan M, Rodell M, Beaudoing H K, et al. (2010). Simulating the Effects of Irrigation over the 

- 796 United States in a Land Surface Model Based on Satellite-Derived Agricultural Data[J]. Journal of 797 Hydrometeorology, 11(1):171-184. 

- 798 Qi W, Feng L, Liu J., et al. (2020). Snow as an important natural reservoir for runoff and soil 799 moisture in Northeast China[J]. Journal of Geophysical Research Atmospheres, doi: 800 10.1029/2020JD033086. 

- 801 Peña-Gallardo M, Vicente-Serrano S M, Hannaford J, et al. (2019). Complex influences of 

- 802 meteorological drought time-scales on hydrological droughts in natural basins of the contiguous 803 Unites States[J]. Journal of Hydrology, 568: 611–625. 

- 804 Raible, C. C., Bärenbold, O., & Gomez‐Navarro, J. J. (2017). Drought indices revisited−Improving 805 and testing of drought indices in a simulation of the last two millennia for Europe. Tellus A: 806 Dynamic Meteorology and Oceanography, 69(1), 1287492. 

- 807 Rodell M, Houser P R, Jambor U E A, et al. The global land data assimilation system[J]. Bulletin of 808 the American Meteorological Society, 2004, 85(3): 381-394. 

- 809 Santoro M, Kirches G, Wevers J, et al. (2017). Land Cover CCI: Product User Guide Version 2.0. 

- 810 Avaliable at: http://maps.elie.ucl.ac.be/CCI/viewer/. 

- 811 Schepsmeier, U., and E. C. Brechmann (2015), Package CDVine. [Available at 

812 

   - http://CRAN.R-project.org/package=CDVine.] 

- 813 Schubert S D, Wang H, Koster R D, et al. (2014). Northern Eurasian heat waves and droughts[J]. 

- 814 Journal of Climate, 27(9): 3169-3207. 

45 

- 815 Seneviratne, S. I., Corti, T., Davin, E. L., et al. (2010). Investigating soil moisture–climate 

- 816 interactions in a changing climate: A review[J]. Earth-Science Reviews, 99:125-161. 

- 817 Sheffield J, Goteti G, Wen F, et al. (2004). A simulated soil moisture based drought analysis for the 

- 818 United States[J]. Journal of Geophysical Research: Atmospheres, 109(D24). 

- 819 Shah D, Shah H L, Dave H M, et al. Contrasting influence of human activities on agricultural and 

- 820 hydrological droughts in India[J]. Science of The Total Environment, 2021, 774(20). 

- 821 Sheffield, J., and E. F. Wood (2007), Characteristics of global and regional drought, 1950-2000: 

- 822 Analysis of soil moisture data from off-line simulation of the terrestrial hydrologic cycle, J. 823 Geophys. Res., 112, D17115, doi:10.1029/2006JD008288. 

- 824 Sheffield J, Wood E F, Roderick M L. (2012). Little change in global drought over the past 60 years. 825 Nature, 491(7424): 435-438. 

- 826 Trenberth K E, Dai A, Van Der Schrier G, et al. (2014). Global warming and changes in drought. 827 Nature Climate Change, 4(1): 17-22. 

- 828 Van Loon A F, Van Lanen H A J. (2012). A process-based typology of hydrological drought[J]. 

- 829 Hydrology and Earth System Sciences, 16(7): 1915. 

- 830 Van Loon A F. (2015). Hydrological drought explained. Wiley Interdisciplinary Reviews: Water, 2(4): 

- 831 359-392. 

- 832 Vicente-Serrano, S. M., and J. I. López-Moreno (2005), Hydrological response to different time 

- 833 scales of climatological drought: An evaluation of the Standardized Precipitation Index in a 

- 834 mountainous Mediterranean basin, Hydrol. Earth Syst. Sci. Discuss., 9(5), 523–533. 

- 835 Vicente-Serrano S M, Beguería S, López-Moreno J I. (2010). A multiscalar drought index sensitive 

- 836 to global warming: the standardized precipitation evapotranspiration index[J]. Journal of climate, 

46 

- 837 23(7): 1696-1718. 

- 838 Wang, W., Zhu, Y., Xu, R., Liu, J. (2015). Drought severity change in China during 1961–2012 

- 839 indicated by SPI and SPEI. Natural Hazards, 75(3), 2437-2451. 

- 840 Wilhite D A, Glantz M H. (1985). Understanding: the drought phenomenon: the role of definitions[J]. 841 Water international, 10(3): 111-120. 

- 842 Wilks, D.S., 2011. Statistical Methods in the Atmospheric Sciences. Academic Press, San Diego, CA. 

- 843 Williams A P, Seager R, Abatzoglou J T, et al. (2015). Contribution of anthropogenic warming to 

- 844 California drought during 2012-2014. Geophysical Research Letters, 42(16): 6819-6828. 

- 845 Wong G, Van Lanen H A J, Torfs P. (2013). Probabilistic analysis of hydrological drought 

- 846 characteristics using meteorological drought. Hydrological Sciences Journal, 58(2): 253-270. 

- 847 Wu J, Chen X, Love C, et al. Determination of water required to recover from hydrological drought: 

- 848 Perspective from a drought propagation and non-standardized indices. Journal of Hydrology, 2020: 849 125227. 

- 850 Xu, Q., & T. Childs. (2013). Evaluating forecast performances of the quantile autoregression models 

- 851 in the present global crisis in international equity markets, Appl. Financ. Econ., 23(2), 105-117. 

- 852 Yang L., Sun G., Zhi L, et al. Negative soil moisture-precipitation feedback in dry and wet regions[J]. 

- 853 Scientific Reports, 2018, 8(1):4026. 

- 854 Yang, Y., Mcvicar, T. R., Donohue, R. J., et al. (2017). Lags in hydrologic recovery following an 

- 855 extreme drought: Assessing the roles of climate and catchment characteristics. Water Resources 856 Research, 53(6), 4821-4837. 

- 857 Zaitchik B F, Rodell M, Olivera F. Evaluation of the Global Land Data Assimilation System using 

- 858 global river discharge data and a source‐to‐sink routing scheme[J]. Water Resources Research, 

47 

859 

   - 2010, 46(6). 

- 860 Zhu Y, Liu Y, Wang W, et al. Three dimensional characterization of meteorological and hydrological 

- 861 droughts and their probabilistic links. Journal of Hydrology, 2019, 578: 124016. 

- 862 Zhu, Y., Liu, Y., Ma, X., Ren, L., Singh, V. P. (2018). Drought analysis in the Yellow River Basin 

- 863 based on a short-scalar Palmer Drought Severity Index. Water, 10(11), 1526. 

48 

