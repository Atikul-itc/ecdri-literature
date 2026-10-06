IEEE JOURNAL OF SELECTED TOPICS IN APPLIED EARTH OBSERVATIONS AND REMOTE SENSING, VOL. 19, 2026 

1703 

## A Deep Learning Model for Integrating Landsat-8 and Sentinel 2 Satellite Images to Improve the Spatiotemporal Fusion Network for Drought Monitoring 

Aravinth J _, Member, IEEE_ , and Anand R _, Member, IEEE_ 

**_Abstract_ —Thisstudyproposesadeeplearningmodelfortheintegration of Landsat-8 and Sentinel satellite imagery to enhance the spatial, spectral, and temporal resolution of drought forecasting. Landsat-8 offers a superior spatial resolution but lower temporal frequency, whereas Sentinel imagery provides a higher temporal frequency but a reduced spatial resolution. The integration of these datasets mitigates the limitations inherent in each dataset, thereby improving the quality of Earth observation data and creating a more robust dataset for precise monitoring of droughts. Correlation analysis revealed that the fused dataset achieved stronger relationships between VCI and NDWI (** **_r_ = 0** **_._ 72) and between VCI and SPEI (** **_r_ = 0** **_._ 65) than the relationships achieved using the Sentinel-2 (** **_r_ = 0** **_._ 68,** **_r_ = 0** **_._ 62) and Landsat-8 (** **_r_ = 0** **_._ 60,** **_r_ = 0** **_._ 58) datasets. A bi-directional long short-term memory (BiLSTM) model was then applied to predict SPEI-12 from the vegetation and hydrological variables. The model achieved an** **_R_**<sup>**2**</sup> **of 0.7946 and an root mean square error (RMSE) of 0.5709, indicating a strong agreement between the predicted and observed drought values. Compared with conventional LSTM and random forest models, the Bi-LSTM showed approximately 9–12% improvement in** **_R_**<sup>**2**</sup> **and a 15–20% reduction in RMSE, demonstrating superior capability in capturing nonlinear vegetation–climate dependencies.** 

**_Index Terms_ —Drought assessment, Landsat-8, multiscale and attention mechanism, residual, Sentinel-2.** 

applications such as agricultural monitoring, forest mapping, water stress detection, and climate analysis. It allows researchers to study the interaction between solar radiation and surface materials, providing spectral signatures that are useful for classification and change detection. Common indices, such as the Normalized Difference Vegetation Index (NDVI), Normalized Difference Water Index (NDWI), and Vegetation Condition Index (VCI), are derived from specific MSI bands and are sensitive to vegetation health and moisture conditions. In this study, two important sources of MSI data were used: Landsat 8 and Sentinel-2 A. Landsat 8, operated by the USGS and NASA, provides 30 m spatial resolution with a 16-day revisit time. Sentinel-2 A, launched by the European Space Agency (ESA), offers a higher spatial resolution (10–60 m depending on the band) and a more frequent revisit cycle of five days. These differences not only make each dataset valuable, but also introduce challenges in direct comparisons or analyses. Hence, combining their strengths through data fusion is essential for consistent and detailed Earth observation. 

### I. INTRODUCTION 

ULTISPECTRAL imaging (MSI) is a remote sensing **M** technique that acquires image data across specific wavelength ranges within the electromagnetic spectrum. In contrast to RGB images, which are confined to three bands (Red, Green, Blue), MSI encompasses multiple bands, frequently extending into the near-infrared (NIR), shortwave infrared (SWIR), and occasionally thermal infrared regions. This enables a detailed analysis of land surface features, particularly vegetation, soil, and water bodies [1]. MSI plays a crucial role in Earth observation 

# **M** 

Received 12 August 2025; revised 23 October 2025 and 10 November 2025; accepted 23 November 2025. Date of publication 26 November 2025; date of current version 22 December 2025. _(Corresponding author: Aravinth J.)_ Aravinth J is with the Department of Electronics and Communication Engineering, Amrita School of Engineering, Coimbatore, Amrita Vishwa Vidyapeetham, Haridwar 249408, India (e-mail: j_aravinth@cb.amrita.edu). 

Anand R is with the Department of Electrical and Electronics Engineering, Amrita School of Engineering, Coimbatore, Amrita Vishwa Vidyapeetham, Haridwar 249408, India (e-mail: r_anand2@cb.amrita.edu). 

Digital Object Identifier 10.1109/JSTARS.2025.3637223 

### _A. Need for Data Fusion in Remote Sensing_ 

Despite the availability of high-quality MSI data from multiple satellites, single-sensor analyses often face limitations in terms of spatial resolution, temporal frequency, and spectral richness. For example, Landsat has a wide range of spectral bands but is limited in terms of its temporal resolution. In contrast, Sentinel-2 has high spatial and temporal resolutions but may lack some bands or face frequent cloud cover. Data fusion techniques have been employed to overcome these challenges. Fusion integrates complementary data from different sensors to create a new dataset rich in spatial, temporal, and spectral information. In remote sensing, fusion allows for the following. 

- 1) Improving spatial detail without sacrificing spectral information. 

- 2) Filling temporal gaps using multiple sources with different revisit times. 

- 3) Reducing cloud interference by leveraging multiple observations. 

© 2025 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/ 

IEEE JOURNAL OF SELECTED TOPICS IN APPLIED EARTH OBSERVATIONS AND REMOTE SENSING, VOL. 19, 2026 

1704 

- 4) Enhancing accuracy in vegetation, soil moisture, and drought assessments. 

In this study, a multiscale and attention-based fusion mechanism was implemented to combine the Landsat 8 and Sentinel-2 A data. The multiscale design captures features at different spatial levels, thereby allowing the preservation of fine and coarse details. The attention mechanism helps the model focus on the most informative parts of the input data by assigning different weights to the features based on their relevance. This intelligent fusion approach generates a highquality dataset that retains the strengths of both input sources and supports improved environmental monitoring in the future. The fused dataset was then used to derive various vegetationand drought-related indices. These indices were used as inputs for the deep learning model, enabling accurate drought predictions. 

### _B. Understanding Drought and Its Impact_ 

Drought is one of the most severe and widespread natural hazards affecting agriculture, water supply, ecosystems, and economies. Unlike rapid-onset disasters such as floods or earthquakes, droughts develop slowly over time owing to prolonged periods of insufficient rainfall, high temperatures, or water demand exceeding supply. The impact of drought is often longlasting, leading to crop failure, reduced water availability, and economic losses, particularly in regions that depend on rain-fed agriculture. There are different types of droughts. 

- 1) Meteorological drought refers to a prolonged period of very less rainfall. 

- 2) It occurs when the moisture in soil is not sufficient for growth of the crop. 

- 3) Hydrological drought involves declining water levels in rivers, lakes, and reservoirs. 

- 4) Socio-economic drought results when water shortages begin to affect society and the economy. 

Droughtmonitoringisacomplextaskthatrequirescontinuous data over time and in space. Remote sensing has emerged as a powerful tool for monitoring vegetation health and surface water conditions using satellite imagery-derived indices. In addition, climate-based indices, such as the Standardized PrecipitationEvapotranspiration Index (SPEI), offer valuable insights into rainfall anomalies and temperature influences. In this study, satellite and meteorological data were combined. Vegetation indices, such as NDVI, NDWI, and VCI, were calculated from the fused MSI data, while SPEI was computed using meteorological datasets, such as precipitation and temperature. This multisource approach ensured a comprehensive understanding of drought conditions. The major contributions of this research are as follows. 

- 1) Despite progress in satellite image fusion and artificial intelligence (AI)-based drought prediction, many existing models face limitations, such as reliance on single-source data, limited nonlinear feature extraction, and a narrow focus on either vegetation or climate indices. 

- 2) Our approach overcomes these limitations by using dualfusion of Landsat-8 and Sentinel-2, deep learning-based 

fusion methods, and a unified framework that integrates both vegetation and climate indices. 

- 3) Unlike conventional methods that analyze vegetation or climate factors independently, the proposed framework jointly incorporates vegetation indices (VCI, NDVI) and climate indices (SPEI, NDWI) to provide a comprehensive assessment of drought severity. 

- 4) The use of a Bidirectional Long Short-Term Memory (Bi-LSTM) network captures bidirectional temporal dependencies in multiyear time-series data, enabling robust prediction of vegetation response under varying climatic conditions. 

### II. RELATED WORKS 

The initial phase of this project focuses on the methodologies discussed by Zhang et al. [2], where Landsat-8 and Sentinel-2 imagery were fused to enhance the spatial and temporal resolution. The fusion helped us obtain a richer dataset by combining Landsat’s thermal data with Sentinel’s multispectral data, which offer information on the chlorophyll content present in plants and trees, which is very important for estimating vegetation health and land surface temperature (LST), which are essential indicators of drought. Khosravi et al. [3] presented a similar approach for soil contamination mapping, that such fusion leads to enhanced and improved mapping accuracy of environmental pollutants, which is advantageous for broader environmental modeling applications. The research conducted by Li et al. [4] employed a pixel-wise normalization method to integrate the high-resolution spatial characteristics of Sentinel-2 into Landsat data, which led to improvements in both image sharpness and continuity. Traditional mathematical models, such as PCA [5] and pixel-level integration, can compress multispectral data while preserving essential information, streamlining environmental analysis workflows, and offering improved computational efficiency. However, they often lack the deep contextual understanding that modern AI methods provide [6]. 

Recent breakthroughs in deep learning have revolutionized the combination of different types of imagery for environmental analysis, offering substantial benefits over traditional models. For instance, Azarang et al. [7] created a neural network framework using convolutional autoencoders to seamlessly merge multispectral and panchromatic (PC) images. Their approach automatically identifies key features and sharpens fine spatial details, thereby improving the image clarity. Dian et al. [8] showed that Convolutional Neural Network (CNN) denoisers preserve spectral information while sharpening images ensuring vibrant, high-quality outputs. 

Cheng et al. [9] later pushed these techniques and advanced this domain by further integrating multiscale analysis and attention mechanisms for spatiotemporal fusion, achieving 10-m resolution predictions suitable for complex land cover scenarios it also allows models to prioritize important spatial and temporal patterns for accurate, high-resolution predictions [10]. Tang et al. [11] developed the Fusion Near Real-Time (FNRT) algorithm to monitor tropical forest disturbances, which combines data from Sentinel-1, Sentinel-2, and Landsat to monitor 

1705 

J AND R: DEEP LEARNING MODEL FOR INTEGRATING LANDSAT-8 AND SENTINEL 2 SATELLITE IMAGES 

TABLE I 

SUMMARY OF RECENT STUDIES ON SPATIOTEMPORAL FUSION, DROUGHT MONITORING, AND DEEP LEARNING APPLICATIONS IN REMOTE SENSING 



environmental changes in near real time. Although their main focus was on deforestation, their multisensor fusion pipeline showcased a strategy for addressing the spatial and temporal data gaps present in satellite imagery, which is an important factorfordroughtapplicationsinfluencedbyvaryingcloudcover conditions. These techniques are closely aligned with the fusion architecture applied in our study, where spectral and spatial enhancements were conducted before drawing conclusions related to the drought. 

Thesubsequent phaseofourprojectfocusesonutilizingfused satellite data to predict drought conditions using remote sensing indices and deep learning techniques. Fused satellite data were employed to extract biophysical indicators, including the NDVI, NDWI, and VCI, along with climate-related indices such as the SPEI. These indices are extensively used to assess vegetation health, soil moisture levels, and prolonged drought patterns. A key study conducted by Ejaz et al. [12] successfully integrated theVegetationHealthIndex(VHI)withtheSPEIbyutilizingfeatures derived from Landsat and the Google Earth Engine (GEE) to investigate regional drought patterns in the country. Their findings underscore the importance of merging vegetation and climate indices for comprehensive spatial drought assessment. This dual approach is reflected in our model, which enhances accuracy by incorporating both vegetation indices and climate variables into the model [13]. 

Zhang et al. [14] created OPTRAM-ET, a novel model that employs the trapezoidal relationship between the vegetation index and SWIR reflectance to estimate evapotranspiration (ETa) independently of thermal data. This method is significant because it allows for the estimation of crop water 

stress at finer resolutions using only optical sensors, which is essential in regions where data are scarce or thermal bands are unavailable. 

Xu et al. [15] proposed an integrated drought index (QuickDRI-China) based on deep learning models including Entity Embedding Deep Neural Networks, 1D-CNNs, gated recurrent unit (GRUs), and self-attention mechanisms and compared them against machine learning models such as random forest and LGBM. This study revealed the superior spatial and temporal consistency of deep learning methods for complex drought conditions [16]. Agana and Homaifar [17] proposed a Deep Belief Network (DBN) aimed at predicting long-term droughts by utilizing lagged Soil Moisture Index values as input variables. By employing a layer-wise unsupervised learning approach, DBNs effectively identified nonlinear relationships, demonstrating superior performance compared to multilayer perceptron (MLP) and support vector regression (SVR) models in terms of root mean square error RMSE and MAE across various forecasting timeframes. These models offer significant insights into the potential of uncovering hidden connections within climatic data to improve predictive accuracy [18]. 

The objective of the study conducted by Nikdad et al. [19] was to identify the essential variables that can predict agricultural drought in various climatic conditions in Iran by utilizing feature selection methods. By integrating these methods with machine learning algorithms, this study aimed to improve drought prediction accuracy and efficiency. These results emphasize the critical role of selecting appropriate features to optimize model performance in forecasting agricultural droughts [20]. Furthermore, Chen et al. [21] developed the interpretable machine 

1706 

IEEE JOURNAL OF SELECTED TOPICS IN APPLIED EARTH OBSERVATIONS AND REMOTE SENSING, VOL. 19, 2026 



TABLE II 

DATA ACQUISITION DATES OF LANDSAT-8 AND SENTINEL-2 



Fig. 1. Flowchart of the proposed model. 

### III. METHODOLOGY 

learning drought index (IMLDI) by integrating multisource remote sensing data, including solar-induced chlorophyll fluorescence (SIF), soil moisture, LST, and water balance metrics. Utilizing LightGBM. By utilizing a Bayesian-optimized Light Gradient Boosting Machine (LightGBM) and SHapley Additive exPlanations (SHAP), the model offers both high accuracy and interpretability for drought assessment. The IMLDI demonstrated superior spatial and temporal consistency with established indices, such as the SPEI, and effectively captured historical drought events in China, highlighting its potential for monitoring agricultural droughts in real-world settings. 

Sivasubramanian et al. [22] conducted an extensive study that enhanced the understanding and significance of vegetationbased indices and their various combinations in evaluating drought conditions, utilizing fused data from Landsat-8 and Sentinel-2. Their results highlighted the critical roles of the VCI and Temperature Condition Index (TCI), demonstrating that these indices are not merely effective on their own but are essential when integrated with climatic factors such as the SPEI. In addition, their machine learning model evaluated the relevance of different features throughout the cropping season, enabling more accurate identification of areas susceptible to droughts [23]. 

Our research adopts a dual approach to this problem. Initially, we employed image fusion techniques based on both traditional and deep learning methodologies to create high-resolution multispectral fused images that captured the spatiotemporal complexities of agricultural environments [24]. Next, we applied various indices, including NDVI, VCI, NDWI, and SPEI, utilizing deep learning architectures such as BiLSTM, to analyze time-series data for more precise drought pattern forecasting in the region. We validated our models for drought events in differentregionsandcroppingcycles.Performancemetrics,such as RMSE, MAE, and correlation coefficients, demonstrated the superiority of our deep learning-based framework over static statistical approaches [25]. 

This literature review highlights the importance of integrating vegetation indices with climate indicators, combining satellite data with temporal AI models, and merging traditional environmental monitoring with innovative deep learning frameworks, as shown in Table I. Collectively, these elements constitute the foundation of the AI-driven prediction system. 

The proposed workflow, shown in Fig. 1, outlines the process for fusing Landsat 8 and Sentinel 2 imagery data for drought prediction using deep learning. The study began with the collection of Sentinel 2 and Landsat 8 datasets from the Copernicus Dataspace Ecosystem and Earth Explorer, respectively, followed by preprocessing techniques such as atmospheric correction, resampling, and the creation of band composites. The data were fused using multiscale and attention mechanisms, and the resulting data, along with secondary soil data, were fed into a deep-learning model for drought prediction. Finally, we used performance metrics to evaluate the results of our experiments. 

### _A. Data Acquisition_ 

_1) Multispectral Images:_ A multispectral image consists of multiple layers, each capturing the same scene at different wavelength bands. This technique enhances the ability to analyze various applications in agriculture, healthcare, and industry. Multispectral images contain two main types of information: spatial and spectral. Spatial information refers to the location of each pixel in an image and the ground area it represents. In contrast, spectral information is related to the specific wavelengths of the electromagnetic spectrum captured by the satellite sensor. 

_2) Dataset:_ Landsat 8 delivers moderate-resolution imagery (15–100 m) of the Earth’s terrestrial and polar regions across several spectral ranges, including the visible, NIR, SWIR, and thermal infrared. Its payload consists of two primary instruments: the Operational Land Imager (OLI) and Thermal Infrared Sensor (TIRS). These instruments provide seasonal coverage with spatial resolutions of 30 m for the visible, NIR, and SWIR bands, 100 m for the thermal bands, and 15 m for PC data. In contrast, Sentinel-2 is a European initiative designed for wide-swath, high-resolution MSI applications. It features an optical payload that captures data across 13 spectral bands with spatial resolutions of 10 m for four bands, 20 m for six bands, and 60 m for three bands. The Sentinel-2 satellite has an extensive orbital swath width of 290 km. Both datasets were collected monthly between 2021 and 2024, as shown in Table II. 

The dataset was divided into three subsets for model development and evaluation purposes. Specifically, 70% of the total samples were used for training, selected across multiple years (2021–2023) to ensure the temporal variability. A validation set 

J AND R: DEEP LEARNING MODEL FOR INTEGRATING LANDSAT-8 AND SENTINEL 2 SATELLITE IMAGES 

1707 

comprising 15% of the samples was employed for hyperparameter tuning and early stopping during the model training. The remaining 15% of the data, primarily from 2024, were reserved as an independent test set to evaluate the generalization capability of the proposed model under unseen temporal and spatial conditions. Ground truth data were collected using a FigSpec spectroradiometer in May 2025. The dataset consisted of hyperspectral image cubes, which were preprocessed to extract specific spectral bands corresponding to those used in the band composites. 

### _B. Data Preprocessing_ 

_1) Atmospheric Correction:_ The data containing top-ofatmosphere (TOA) reflectance values need to be preprocessed. We converted the TOA to the bottom of atmosphere (BOA) reflectance. This can be achieved through atmospheric corrections. This improves the interpretation accuracy of the surface features. TOA reflectance is the raw reflectance of the Earth as measured from space, whereas BOA reflectance is the actual reflectance of the Earth’s surface. 

The atmospheric correction process begins by converting the raw satellite digital numbers (DN) to TOA reflectance using the radiometric calibration equation as follows: 



Inthisequation, _ρ_<sup>_′_</sup> _λ_<sup>representstheTOAreflectanceataspecific</sup> wavelength _λ_ . _Mρ_ is the multiplicative reflectance rescaling factor, and _Aρ_ is the additive reflectance rescaling factors, respectively, both of which are provided in the image metadata. _Qcal_ is the quantized and calibrated DN obtained from the sensor. This transformation ensured that the DN values were scaled to the physical reflectance values, facilitating further atmospheric and geometric correction. 

Subsequently, a sun angle correction was applied to compensate for the varying angle of incoming solar radiation owing to the sun’s position. The corrected reflectance is given by 



Here, _ρλ_ is the TOA reflectance corrected for solar geometry. _θSE_ denotes the solar elevation angle,) which is the angle between the sun and the horizon. When using cos( _θSE_ ), it refers to a solar zenith-based correction (because _θZ_ = 90<sup>_◦_</sup> _− θSE_ ). This correction ensured consistency in the reflectance values for different acquisition times and solar angles. 

Finally, to retrieve the surface reflectance (also known as bottom-of-atmosphere or BOA reflectance), the contribution from the atmospheric path reflectance was subtracted. In this expression, BOA = _ρ_<sup>_′_</sup> _λ_<sup>- AR, where AR represents the atmospheric</sup> reflectance, which accounts for the portion of the signal scattered back to the sensor by atmospheric particles and gases before it reaches the Earth’s surface. Subtracting the AR from the TOA reflectance yields the surface reflectance, which is crucial for accurate land surface analysis and comparison across different times and locations. 

_2) Resampling:_ Resampling was used to change the spatial resolution of images. It is the interpolation of pixel values to create a new image with a different pixel size but the same geographic content. This process is necessary for combining images with different spatial resolutions. We used a technique called the nearest-neighbor algorithm for resampling. The methodology involves attributing a value to each “corrected” pixel based on the nearest “uncorrected” pixel. The nearest-neighbor technique is advantageous because of its straightforwardness and capacity to maintain the original values within an unchanged scene. This resampling technique assigns the DN of the closest input pixel, determined by spatial proximity, to the corresponding output pixels. 

_3) Band Composite/Layer Stacking:_ Band composition involves stacking different spectral bands of multispectral images to create a unified image. It is used to highlight features and improve visual interpretation. In this study, the composite involved merging seven bands of Landsat data. This step was performed separately for each dataset in the study. 

### _C. Fusion Architecture_ 

The fusion architecture proposed in this study is a comprehensive approach that combines the distinct spatial and spectral features of Landsat-8 and Sentinel-2 imagery using a combination of multiscale and attentional mechanisms. The aim is to enhance spatial resolution, preserve spectral integrity, and produce high-fidelity fused imagery suitable for land surface monitoring and drought prediction [26]. The complete architectural flow is illustrated in Fig. 2, which provides a visual representation of how data from Landsat and Sentinel sources are preprocessed and combined to yield high-resolution outputs. The proposed architecture integrates multisource satellite data by fusing low-resolution Landsat 30 m and high-resolution Sentinel 10 m imagery to generate enhanced Landsat 10 m outputs. The Sentinel path undergoes convolution and rectified linear unit (ReLU) activation to extract rich spatial features, followed by an attention mechanism that emphasizes the salient information. Simultaneously, the Landsat 30 m input was processed through a multiscale module and upsampled to match the Sentinel resolution [27]. These two streams are fused via element-wise addition and passed through a series of convolutional and residual dense blocks to refine feature representations. A final convolution layer reconstructs the fused output, yielding an enhanced Landsat image at a 10 m resolution with improved spatial and spectral fidelity. 

_1) Multiscale Feature Extraction:_ Multiscale feature extractionisfundamentalforcapturingspatiallydiversefeaturesacross different resolutions of the images. Landsat-8 imagery, with its relatively coarse 30-m resolution, lacks the finer spatial details necessary for high-resolution applications. To compensate for this, we applied a multiscale convolutional strategy that involved parallel convolutional layers with different receptive fields. The design ensures that features are extracted across multiple scales to enhance texture sensitivity and edge detection. Dilated convolutions are a key component of this stage because they systematically increase the effective receptive field of the convolutional 

IEEE JOURNAL OF SELECTED TOPICS IN APPLIED EARTH OBSERVATIONS AND REMOTE SENSING, VOL. 19, 2026 

1708 



Fig. 2. Fusion architecture. 

filters without significantly increasing the computational cost. Different dilation rates enable the model to access both local and global contexts. The outputs from each convolutional stream were concatenated, normalized, and passed through the activation layers to obtain comprehensive feature representations. Following feature extraction, the Landsat-derived features were upsampled to match the 10-m resolution of the Sentinel imagery. This upsampling ensured that feature alignment and fusion with Sentinel features occurred at a uniform scale, thereby facilitating spatial consistency. 

_2) Attention Mechanism:_ The Sentinel 10-m input was processed using a series of 3 _×_ 3 convolution layers, followed by ReLU activation. The resulting features then undergo refinement through an attention mechanism designed to emphasize informative spectral and spatial patterns. This component follows the squeeze-and-excitation (SE) block structure and performs channel-wise attention-recalibration. In this block, the squeeze operation applies global average pooling across the spatial dimensions to produce a descriptor vector that represents the importance of each feature channel. This is followed by an excitation step involving a lightweight MLP that predicts the channel-attention weights. The final scale operation applies these weights to the original features, modulating the influence of each channel. By embedding attention at this stage, the architecture ensures that the Sentinel features passed into the fusion module are rich in semantic and spatial cues relevant for high-resolution analysis. This helps guide the network in discerning the critical patterns during fusion. 

_3) Residual Dense Block With Attention Mechanism:_ After the upsampled Landsat and attention-refined Sentinel features were concatenated, they passed through a 1 _×_ 1 convolution layer to standardize the channel dimensions before entering a residual dense block. This block is pivotal for enhancing feature representation and mitigating gradient vanishing through residual and dense connectivity. 

Each layer in the residual dense block receives inputs from all preceding layers, resulting in a richer and more expressive cumulative feature representation. The block contained six layers, each consisting of a 3 _×_ 3 convolution and ReLU activation. The dense concatenation strategy allows earlier-learned features to influence later computations, preserving both low and high spatial cues. To further amplify the discriminative ability, spatial attention modules were integrated within the residual blocks. These modules use convolutional filters and pooling strategies to generate spatial attention maps, thereby enabling location-sensitive recalibration of features. The output is a refined representation that captures spatial patterns that are critical for fusion. The final output _FO_ of the residual block is 

computed as 



Here, _Ft_ denotes the transformed features and _Fd_ represents the original features passed via skip connections. This residual operation enhances the final feature map’s stability and informativeness 

_4) Reconstruction and Output Generation:_ Once the refined features are obtained, they are passed through two final convolutional layers. The first is a 1 _×_ 1 convolution that reduces the dimensionality to match the expected output channels, followed by a 3 _×_ 3 convolution that reconstructs the final, fused image. The result is an enhanced Landsat-like image with a 10-m resolution, capturing both the spatial richness from Sentinel and the spectral fidelity from Landsat. This design ensures high-resolution, spectrally consistent outputs that serve as robust inputs for downstream applications, such as vegetation index computation, drought monitoring, and land cover classification. 

### IV. DROUGHT EXPERIMENTAL ASSESSMENT 

Drought assessment is a critical component in understanding the severity, frequency, and duration of drought events, particularly in agriculturally significant regions. In this study, we assessed using both original and fused satellite data to improve the spatial resolution and capture finer details for more accurate evaluations. The datasets included Landsat imagery for 2005, 2010, 2015, 2020, and 2024 and Sentinel-2 imagery for 2015, 2020, and 2024. The fusion of the two datasets provided an accurate analysis of the data. Four key drought indicators were used for the assessment: NDVI, VCI, NDWI, and SPEI. The NDVI and NDWI were derived using red, NIR, and SWIR bands. These indices help detect changes in vegetation health and soil moisture levels [28]. 

The VCI was calculated from NDVI to capture deviations in vegetation conditions across different years, whereas the SPEI, based on precipitation and evapotranspiration data, was used to monitor climatic droughts over various temporal scales. The indices were computed for each time period using both individual (Landsat and Sentinel) and fused datasets. This allowed for a comparative analysis and validation of the efficacy of the proposed fusion model [29]. A correlation matrix was then developed to analyze the relationships among the indices (NDVI, VCI, NDWI, and SPEI) for the specified years. This matrix helped determine the interdependency between vegetation and climate-based indices and offered insights into spatial and temporal drought patterns across the region. Correlation analysis 

J AND R: DEEP LEARNING MODEL FOR INTEGRATING LANDSAT-8 AND SENTINEL 2 SATELLITE IMAGES 

1709 



Fig. 3. Study area of the proposed model. 

was performed using the GEE, which enables the cloud-based processing of large datasets. 

### _A. Dataset Descriptions_ 

The current study on drought prediction was conducted in the Tiruppur district, situatedinthewesternregionof Tamil Nadu, as shown in Fig. 3. This district is of strategic significance as a key economic player in the state, mainly because of its flourishing textile and agricultural activities. Its selection as the focus of this study is further justified by its vulnerability to climate variability, especially recurrent droughts, which greatly affect agricultural productivity, water supply, and the overall socioeconomic stability of the region. Tiruppur is located within the latitudinal boundaries of 10°14’N to 11°20’N and the longitudinal boundaries of 77°27’E to 77°56’E. These geographic coordinates represent a semi-arid region that experiences variable rainfall both spatially and temporally, making it an ideal location for studying drought dynamics and their potential effects on vegetation. Given the district’s climatic characteristics and economic reliance on water-dependent industries, examining the efficiency of drought forecasting methods and the associated mitigation approaches is essential. 



Fig. 4. Atmospheric correction. (a) Before atmospheric correction. (b) After atmospheric correction. 

bands Blue (B2), Green (B3), Red (B4), Red Edge 2(B6), Red Edge 3 (B7), NIR (B8) – 10 m resolution, and SWIR (B11 and B12) – 20 m resolution. The Landsat-8 dataset has 11 bands, and we focused on the blue (B2), green (B3), red (B4), SWIR (B6 and B7), NIR, and Thermal Infrared (B5 and B1) bands, as shown in Fig. 5. 

### _C. Image Fusion_ 

### _B. Preprocessing Results_ 

_1) AtmosphericCorrectionandBandComposite:_ Inthisprocess, we converted the TOA to the BOA, as shown in Fig. 4(a) and (b). The Sentinel-2 dataset has 13 bands, and we focused on 

Fig. 6 visually represents the fused results of Landsat-8 and Sentinel-2 for January 2021. The resulting 10 m image offers a substantial enhancement in resolution compared to the initial 30 m image. 

IEEE JOURNAL OF SELECTED TOPICS IN APPLIED EARTH OBSERVATIONS AND REMOTE SENSING, VOL. 19, 2026 

1710 



Fig. 5. Composite band images (Bands 2,3,4,5,6,7,10) and composite result. (a) Band 2. (b) Band 3. (c) Band 4. (d) Band 5. (e) Band 6. (f) Band 7. (g) Band 10. (h) Composite result. 

Fig. 7(a) and (b) shows detailed views of the highlighted subsets. The fusion results demonstrated a significant enhancement in spatial resolution, improving Landsat 8’s 30 m imagery to a refined 10 m output while preserving spectral integrity. The attention mechanism effectively retains critical spatial features, and the multiscale approach ensures a smooth transition of details. Quantitative evaluation confirmed superior performance, with a lower RMSE (0.0233), higher PSNR (32.78 dB), and 



Fig. 6. 10 m resolution of fused image. 



Fig. 7. Image fusion for our research area. (a) Before Fusion. (b) After Fusion. 

SSIM(0.9592),outperformingtheexistingfusionmodels.Fused imagery reduces artifacts, enhances feature clarity, and provides a more reliable dataset for vegetation analysis, drought monitoring, and land cover classification, making it highly applicable to environmental and agricultural research. 

### _D. Performance Metrics_ 

_1) Mean Squared Error (MSE):_ The MSE is a metric that measures the average of the squared difference between the predicted and actual values in a regression task. A larger MSE value indicates that the data points are widely spread across the mean. MSE can be mathematically expressed as 



where _o_ denotes the output of the model, _t_ denotes the target area, and _N_ denotes the number of areas in each training dataset. 

_2) ERGAS:_ The ERGAS is a metric used to calculate the accuracy of fused images. It can be expressed as 



where _H_ and _L_ are the spatial resolutions of the high-resolution (fused) and low-resolution images, respectively. RMSE _i_ is the 

J AND R: DEEP LEARNING MODEL FOR INTEGRATING LANDSAT-8 AND SENTINEL 2 SATELLITE IMAGES 

1711 



Fig. 8. Visual comparison of Landsat-8, Sentinel-2, and the fused image. 

Root Mean Square Error of the _i_ th band between the fused and reference images and _n_ is the number of spectral bands. 

_3) Structural Similarity Index (SSIM):_ The SSIM is a metric used to measure the quality of an image and to compare the similarity between two images. It can be expressed as 



where _μx_ and _μy_ are the averages of _x_ and _y_ , respectively, _σx_<sup>2</sup> and _σy_<sup>2are their variances,</sup><sup>_σxy_is the covariance between</sup><sup>_x_and</sup> _y_ , _c_ 1 = ( _k_ 1 _L_ )<sup>2</sup> and _c_ 2 = ( _k_ 2 _L_ )<sup>2</sup> are constants used to stabilize the division when the denominator is weak, and _k_ 1 = 0 _._ 01 and _k_ 2 = 0 _._ 03 by default. 

_4) Peak Signal-Noise Ratio (PSNR):_ The PSNR is a logarithmic metric based on MSE that is used to evaluate the quality of an image. It is defined as the ratio of the maximum possible pixel value to the RMSE. It is expressed as 



where R – Maximum possible pixel value in the image and MSE – Mean Square Error. Fig. 8 presents a visual comparison of Landsat-8, Sentinel-2, and the fused image generated by the proposed model. The top row shows the original and fused scenes, and the bottom row shows the magnified sections from the same spatial region. The fused output effectively integrates the spatial 

details of Sentinel-2 with the spectral richness of Landsat-8. The zoomed-in regions highlight that the fusion image preserves fine texture details and minimizes spectral distortion, demonstrating superior visual consistency compared with the individual source images. 

Table III compares the performance of the four methods—STARFM-SI, DSTFN, MARSTFN, and Modified MARSTFN—using RMSE, PSNR, and SSIM as evaluation metrics. Among all methods, the Modified MARSTFN achieved the best performance, with the lowest RMSE of 0.0243, indicating a minimal prediction error, and the highest PSNR of 32.78 dB, reflecting superior reconstruction quality. It also recorded the highest SSIM value of 0.9572, demonstrating the best structural similarity with the reference data. MARSTFN also performed well, ranking second across all three metrics, whereas DSTFN slightly outperformed STARFM-SI, which showed the lowest accuracy among the compared methods. Overall, the results show that the modifications introduced in the Modified MARSTFN led to significant improvements in both accuracy and visual quality. The proposed framework, termed Modified MARSTFN + Bi-LSTM, integrates a lightweight multiscale attention-based spatiotemporal fusion network with a Bi-LSTM module. The Modified MARSTFN component enhances the spatial–spectral fusion of Landsat-8 and Sentinel-2 data through shared convolutional kernels and reduced residual attention blocks, 

IEEE JOURNAL OF SELECTED TOPICS IN APPLIED EARTH OBSERVATIONS AND REMOTE SENSING, VOL. 19, 2026 

1712 

TABLE III 

PERFORMANCE COMPARISON OF DIFFERENT METHODS 



improving efficiency while preserving fine spatial details. The Bi-LSTM layer subsequently models temporal dependencies across multidate-fused images, capturing bidirectional trends in vegetation and climate dynamics. This hybrid architecture effectively combines spatial fusion and temporal sequence learning for robust and high-resolution drought monitoring. 

### _E. Drought Metrics_ 

_1) NDVI:_ The NDVI measures the greenness and density of the vegetation captured in a satellite image 



where 

a) NIR – light reflected in the NIR spectrum, 

b) RED – light reflected in the red range of the spectrum. The NDVI index value ranges from _−_ 1 _._ 0 to 1.0. 

_2) NDWI:_ NDWI is used to highlight open water features in a satellite image, allowing the water body to stand out against soil and vegetation 



where 

a) GREEN – light reflected in the green range of the spectrum. 

b) NIR – light reflected in the NIR spectrum. 

The NDWI index value ranges from _−_ 1 _._ 0 to 1.0. 

_3) VCI:_ The VCI is a metric used to monitor droughts by assessing vegetation health. It is calculated using satellite-derived NDVI values to measure the deviation of current vegetation conditions from their historical range 



_4) SPEI:_ The SPEI is a widely used drought monitoring metric that incorporates both precipitation and potential evapotranspiration (PET) to assess the climatic water balance. SPEI is calculated by determining the difference between precipitation and PET over a specified time scale, fitting the result to a probabilitydistribution,andtransformingitintoastandardizednormal distribution. This standardization allows for comparisons across regions and time periods. 

A negative SPEI value indicates dry conditions (drought), whereas a positive value indicates wet conditions. 

The general form of the SPEI computation involves the following: 



#### TABLE IV 

DATA FROM FUSED IMAGE 



#### TABLE V 

TABLE 4-3 SENTINEL-2 DERIVED DATA 



#### TABLE VI 

TABLE 4-4 LANDSAT-8 DERIVED DATA 



where _Di_ is the climatic water balance at time _i_ , _Pi_ is the precipitation at time _i_ , and PET _i_ is the PET at time _i_ . The series _Di_ is then fitted to a probability distribution (commonly a log-logistic distribution) and transformed to a standard normal distribution (mean = 0, standard deviation = 1) to produce SPEI values. 

### _F. Indices Calculated_ 

The VCI and NDWI were calculated from the fused imagery, Sentinel-2, and Landsat-8 datasets for different time periods (see Tables IV–VI). The VCI serves as an indicator of vegetation 

J AND R: DEEP LEARNING MODEL FOR INTEGRATING LANDSAT-8 AND SENTINEL 2 SATELLITE IMAGES 

1713 

#### TABLE VII 

SPEI-12 VALUES (2006–2024) 



TABLE VIII 

CORRELATION MATRIX FOR FUSED DATA (LANDSAT + SENTINEL) 



#### TABLE IX 

CORRELATION MATRIX FOR SENTINEL-2 DERIVED DATA 

health, whereas the NDWI reflects the water content in vegetation and soil. Temporal variation in these indices allows for the assessment of seasonal and interannual changes in vegetation and water stress, supporting agricultural monitoring and drought assessment. 

Table VII presents the annual SPEI-12 values for the period 2006–2024, illustrating the interannual variability in long-term droughtandwetnessconditions.Negativevalues,suchasin2006 ( _−_ 1 _._ 10) and 2007 ( _−_ 0 _._ 40), indicate drier-than-normal years, whereas positive values, particularly in 2022 (2.80) and 2023 (3.50), reflect wetter-than-average conditions. The data revealed a general shift toward wetter years in the latter part of the record, with occasional dry anomalies, providing insights into the changing climatic moisture balance over the study area. 

_1) Spatial Distribution of VCI:_ The spatial distribution of the VCI from 2021 to 2024 is depicted in Fig. 9. Each subfigure represents seasonal snapshots (January, May, and September) for respective years, enabling comparison of vegetation patterns over time. The maps show seasonal variations and interannual differences, helping to identify trends in vegetation conditions, drought stress, and recovery phases during the study period, respectively. 

_2) Spatial Distribution of NDWI:_ The spatial distribution of NDWI from 2021 to 2024, shown in Fig. 10, illustrates the seasonal and interannual variations in water content across the study area. Each subfigure represents NDWI values for different months (January, May, and September) within a given year, enabling a visual comparison of wet and dry season dynamics. These patterns indicate fluctuations in surface water availability, likely influenced by rainfall variability, land use changes, and climatic conditions during the study period. 

### _G. Correlation Analysis Between VCI, NDWI, and SPEI_ 

This study assessed the linear association between Remote Sensing Drought Indices (RSDIs) and the meteorological drought index SPEI. The Pearson Correlation Coefficient (CC) was used to quantify this relationship. To identify anomalies within the RSDIs, the Standardized Anomaly Index (SAI) was applied by computing standardized deviations from the longterm average. The anomalies in the RSDIs were then statistically compared to the SPEI at various temporal scales to determine the strength and nature of their interrelationships. The SAI was calculated using the following formula: 





#### TABLE X 

CORRELATION MATRIX FOR LANDSAT-8 DERIVED DATA 



where _xi_ is the observed value at time _i_ , ¯ _x_ is the long-term mean, and _σ_ is the standard deviation. 

_1) Correlation Matrices:_ The correlation analysis between the VCI, NDWI, and SPEI is presented in Tables VIII–X. For the fused dataset (Landsat + Sentinel) in Table VIII, VCI showed a strong correlation with NDWI ( _r_ = 0 _._ 72) and a moderately strong correlation with SPEI ( _r_ = 0 _._ 65), indicating a close link between vegetation health, water availability, and meteorological drought conditions. In Table IX, Sentinel-2 derived data are slightly lower, with VCI–NDWI ( _r_ = 0 _._ 68) and VCI–SPEI ( _r_ = 0 _._ 62). Table X shows that Landsat-8 derived data have comparatively weaker associations with VCI–NDWI ( _r_ = 0 _._ 60) and VCI–SPEI ( _r_ = 0 _._ 58). Overall, these findings suggest that integrating multisensor datasets enhances the ability to capture vegetation–climate interactions, likely because of improvedtemporalandspectralcoverage.TheSPEIiscalculated by first collecting rainfall (P) and temperature (T) data. Using temperature, PET was estimated to determine water loss. The water balance is then found as _D_ = _P −_ PET, where negative values indicate a drought. This balance is averaged over different time periods (e.g., three months) and compared to historical data using probability models. Finally, the values are standardized to fit a normal scale, where negative SPEI indicates drought and positive SPEI indicates wet conditions. We have calculated the SPEI values ranging from the year 2006–2022 as shown in Fig. 11. 

The actual SPEI-12 values from 2006 to 2024 reflected significant fluctuations in drought intensity over the years. Values below zero indicate drought conditions, with the most severe drought observed in 2006. Positive SPEI-12 values suggest periods of above-average wetness, notably in 2022 and 2023, where the SPEI-12 exceeded 2.5, indicating anomalously wet conditions. The Bi-LSTM prediction model was effective in replicating these trends in the data. While the prediction line 

IEEE JOURNAL OF SELECTED TOPICS IN APPLIED EARTH OBSERVATIONS AND REMOTE SENSING, VOL. 19, 2026 

1714 



Fig. 9. Spatial distribution of VCI from January 2021 to May 2024 with an enlarged color bar. (a) 2021 - Jan. (b) 2021 - Feb. (c) 2021 - Mar. (d) 2022 - Jan. (e) 2022 - Feb. (f) 2022 - Mar. (g) 2022 - Apr. (h) 2022 - Aug. (i) 2022 - Dec. (j) 2023 - Jan. (k) 2023 - Feb. (l) 2023 - May. (m) 2024 - Feb. (n) 2024 - Mar. (o) 2024 - Apr. (p) 2024 - May. 

1715 

J AND R: DEEP LEARNING MODEL FOR INTEGRATING LANDSAT-8 AND SENTINEL 2 SATELLITE IMAGES 



Fig. 10. Spatial distribution of NDWI from January 2021 to May 2024. (a) 2021 - Jan. (b) 2021 - Feb. (c) 2021 - Mar. (d) 2022 - Jan. (e) 2022 - Feb. (f) 2022 - Mar. (g) 2022 - Apr. (h) 2022 - Aug. (i) 2022 - Dec. (j) 2023 - Jan. (k) 2023 - Feb. (l) 2023 - May. (m) 2024 - Feb. (n) 2024 - Mar. (o) 2024 - Apr. (p) 2024 - May. 

1716 

IEEE JOURNAL OF SELECTED TOPICS IN APPLIED EARTH OBSERVATIONS AND REMOTE SENSING, VOL. 19, 2026 



Fig. 11. Validation process of drought prediction model with secondary data. 

(orange) smooths out some extreme fluctuations compared to the actual values (blue), the general pattern and timing of the drought and wet periods were well captured. This confirms the model’s capability of modeling long-term drought dynamics. 

In this study, we combined satellite data and predictive modeling to assess the drought conditions. Although data limitations posed a challenge, we overcame this by analyzing historical climate patterns to maintain the continuity of the study. To predict drought trends for 2023, 2024, and 2025, we used SPEI values from 2006 to 2022 and applied the RNN-LSTM model. This helped us forecast future conditions and gain insight into evolving climate patterns. The SPEI-1 prediction Fig. 12 provides a clear picture of the expected drought conditions for the coming years, with markers indicating moderate, severe, and extreme drought levels. We also calculated the NDVI and VCI values for the same period, and when we compared them with our predicted SPEI trends, they aligned well. The correlation between SPEI and remote sensing indices was more in fused results than Landsat 8 and Sentinel 2 individually. This alignment reassures us that our predictions are on the right track, making this approach a reliable method for evaluating drought conditions using multiple indicators. 



Fig. 12. Predicted SPEI-12 values. 

A performance comparison of the different models for predicting SPEI-12 is presented in Table XI. Among all models, the Bi-LSTM achieved the highest coefficient of determination 

J AND R: DEEP LEARNING MODEL FOR INTEGRATING LANDSAT-8 AND SENTINEL 2 SATELLITE IMAGES 

1717 

TABLE XI 

COMPARISON OF MODEL PERFORMANCE FOR SPEI-12 PREDICTION (TEST SET) 



( _R_<sup>2</sup> = 0 _._ 7946) and the lowest error metrics (RMSE = 0.5709, SSE = 11.08, and MAE = 0.412), indicating superior predictive accuracy and stability. In contrast, the standard LSTM and random forest models yielded slightly lower correlations ( _R_<sup>2</sup> = 0 _._ 72 and 0.70, respectively) and higher RMSE values (0.624 and 0.660). The CNN and SVR models performed comparatively poorly, with _R_<sup>2</sup> values below 0.70 and higher error magnitudes. Overall, the Bi-LSTM model demonstrated approximately 10% –15% improvement in predictive accuracy and a 15% –20% reduction in error compared to other models, confirming its effectiveness in capturing nonlinear vegetation–climate interactions for drought assessment. 

### _H. Results Findings_ 

The performance of the proposed Modified MARSTFN + Bi-LSTM framework demonstrated a significant improvement over existing spatiotemporal fusion and drought monitoring approaches. Compared with traditional models, such as STARFMSI and DSTFN, the proposed method achieved lower RMSE and higher SSIM and PSNR values (see Table III), indicating better spectral and spatial consistency in the fused outputs. Similar to the findings reported by LSFuseNet [18] and MARSTFN [16], our results confirm that attention-based multiscale fusion enhances vegetation dynamics representation. However, by integrating Bi-LSTM for temporal learning, the proposed framework further improves the ability to capture bidirectional temporal dependencies across multiyear data, outperforming conventional unidirectional or static-fusion models. 

### V. CONCLUSION 

In conclusion, we proposed a comprehensive framework for predicting droughts using a dual fusion approach of Landsat-8 and Sentinel-2 imagery combined with deep learning-based temporal modeling techniques. The fusion process significantly enhanced the spatial, temporal, and spectral resolution of the given input data, allowing for more precise derivation of remote sensing indices such as NDVI, NDWI, VCI, and climatic indicators like SPEI. These indices, when processed through BiLSTM networks, provided accurate predictions of drought conditions across the area that we clipped and targeted. The quantitative metrics from the fusion phase (PSNR, RMSE, and SSIM) and the validation results from the prediction phase confirmed the strength of the proposed methodology. The developed system not only addresses the limitations of individual satellite datasets, butalsocontributestothedevelopmentofscalable,interpretable, 

and data-rich decision support systems for climate resilience and agricultural planning in the region. 

While our model delivers better results, several changes and improvements can be made in future work to obtain even better outcomes. One key area will be the addition of more environmental and auxiliary data sources, such as precipitation records, groundstationmeasurements,soilmoisture(fromSMAP),evapotranspiration, and LST, which will provide additional contextual information to refine both the fusion and prediction stages. The regional scope of our project can be expanded by applying the methodology to varied climatic zones, such as places which have conditions like arid deserts, farmlands, or monsoondependent regions. This would help evaluate the robustness of the model under diverse environmental and cropping conditions in the future. Similarly, a comprehensive investigation of the seasonal variability of vegetation patterns and their responses to water stress can be facilitated by conducting analyses over multiple years. Moreover, adapting this pipeline into a nearreal-time framework utilizing cloud platforms, such as GEE, or integrating it into API-based dashboards can greatly improve its operational and functional utility. 

### REFERENCES 

- [1] R. Anand, “Quantum-enhanced soil nutrient estimation exploiting hyperspectral data with quantum Fourier transform,” _IEEE Geosci. Remote Sens. Lett._ , vol. 22, Jul. 2025, Art. no. 3591445, doi: 10.1109/LGRS. 2025.3591445. 

- [2] H. Zhang, Y. Zhang, T. Gao, S. Lan, F. Tong, and M. Li, “Landsat 8 and Sentinel-2 fused dataset for high spatial-temporal resolution monitoring of farmland in China’s diverse latitudes,” _Remote Sens._ , vol. 15, no. 11, Art. no. 2951, 2023, doi: 10.3390/rs15112951. 

- [3] V. Khosravi, A. Gholizadeh, and M. Saberioon, “Soil toxic elements determination using integration of Sentinel-2 and Landsat-8 images: Effect of fusion techniques on model performance,” _Environ. Pollut._ , vol. 310, Art. no. 119828, 2022, doi: 10.1016/j.envpol.2022.119828. 

- [4] Y. Li, Z. Zhang, J. Tang, L. Zhang, and X. Li, “Fusing Sentinel-2 and Landsat-8 surface reflectance data via pixel-wise local normalization,” _IEEE J. Sel. Topics Appl. Earth Observ. Remote Sens._ , vol. 15, pp. 7359–7374, 2022, doi: 10.1109/JSTARS.2022.3192639. 

- [5] F. Gao, J. G. Masek, M. Schwaller, and F. G. Hall, “On the blending of the Landsat and MODIS surface reflectance: Predicting daily Landsat surface reflectance,” _IEEE Trans. Geosci. Remote Sens._ , vol. 44, no. 8, pp. 2207–2218, Aug. 2006, doi: 10.1109/TGRS.2006.872081. 

- [6] T. Seleem, D. Bafi, M. Karantzia, and I. Parcharidis, “Water quality monitoring using Landsat 8 and Sentinel-2 satellite data (2014–2020) in Timsah Lake, Ismailia, Suez canal region (Egypt),” _J. Indian Soc. Remote Sens._ , vol. 50, no. 6, pp. 1223–1238, 2022, doi: 10.1007/s12524-021-01487-4. 

- [7] A. Azarang, H. E. Manoochehri, and N. Kehtarnavaz, “Convolutional autoencoder-based image fusion,” _IEEE Access_ , vol. 7, pp. 35673–35683, 2019, doi: 10.1109/ACCESS.2019.2904807. 

- [8] R. Dian, S. Li, and X. Kang, “Regularizing hyperspectral and multispectral image fusion by CNN denoiser,” _IEEE Trans. Neural Netw. Learn. Syst._ , vol. 31, no. 4, pp. 1240–1252, Apr. 2020, doi: 10.1109/TNNLS.2019.2892409. 

- [9] Q. Cheng, R. Xie, J. Wu, and F. Ye, “Deep learning-based spatiotemporal fusion architecture of Landsat 8 and Sentinel-2 data for 10 m series imagery,” _Remote Sens._ , vol. 16, no. 6, Mar. 14 2024, Art. no. 1033, doi: 10.3390/rs16061033. 

- [10] A. Raju, “Tree counting and classification of different level of trees using machine learning algorithms,” _∗AIP Conf. Proc.∗_ , vol. 2915, no. 1, May 2024, Art. no. 0 20014, doi: 10.1063/5.0192745. 

- [11] I. X. Tang, K. H. Bratley, K. Cho, E. L. Bullock, P. Olofsson, and C. E. Woodcock, “Near real-time monitoring of tropical forest disturbance by fusion of Landsat, Sentinel-2, and Sentinel-1 data,” _Remote Sens. Environ._ , vol. 294, 2023, Art. no. 113626, doi: 10.1016/j.rse.2023.113626. 

IEEE JOURNAL OF SELECTED TOPICS IN APPLIED EARTH OBSERVATIONS AND REMOTE SENSING, VOL. 19, 2026 

1718 

- [12] N. Ejaz, J. Bahrawi, K. M. Alghamdi, K. U. Rahman, and S. Shang, “Drought monitoring using Landsat derived indices and Google earth engine platform: A case study from AL-Lith watershed, kingdom of Saudi Arabia,” _Remote Sens._ , vol. 15, no. 4, 2023, Art. no. 984, doi: 10.3390/rs15040984. 

- [13] X. Li, P. Wang, and X. Liu, “Improved STARFM-SI for spatio-temporal fusion of Landsat and Sentinel-2 data,” _Remote Sens._ , vol. 13, no. 21, 2021, Art. no. 4321, doi: 10.3390/rs13214321. 

- [14] L. Zhang, W. Sun, K. Fu, and W. Li, “Deep spatiotemporal fusion network for generating high-resolution satellite time series,” in _Proc. IEEE Int. Geosci. Remote Sens. Symp. (IGARSS)_ , 2022, pp. 1341–1344. 

- [15] Z. Xu, H. Sun, T. Zhang, H. Xu, D. Wu, and J. Gao, “Evaluating established deep learning methods in constructing integrated remote sensing drought index: A case study in China,” _Agric. Water Manage._ , vol. 286, 2023, Art. no. 108405, doi: 10.1016/j.agwat.2023.108405. 

   - [27] Z. Ao, Y. Sun, and Q. Xin, “Constructing 10-m NDVI time series from Landsat 8 and Sentinel-2 images using convolutional neural networks,” _IEEE Geosci.Remote Sens.Lett._ ,vol.18,no.8,pp. 1461–1465,Aug.2021, doi: 10.1109/LGRS.2020.3003322. 

   - [28] M. M. Hosseini et al., “Cropping intensity mapping in Sentinel-2 and Landsat-8/9 remote sensing data using temporal transfer of a stacked ensemble machine-learning model within google earth engine,” _Geocarto Int._ , vol. 39, no. 1, 2024, Art. no. 2387786, doi: 10.1080/10106049.2024.2387786. 

   - [29] J. Chen and Z. Zhang, “An improved fusion of Landsat-7/8, Sentinel-2, and Sentinel-1 data for monitoring alfalfa: Implications for crop remote sensing,” _Int. J. Appl. Earth Observation Geoinformation_ , vol. 124, 2023, Art. no. 103533, doi: 10.1016/j.jag.2023.103533. 

- [16] Q. Yang, Z. Zhao, X. Tang, and L. Zhang, “Multiscale attention residual spatiotemporal fusion network (MARSTFN) for high-resolution timeseries generation,” _Remote Sens._ , vol. 16, no. 5, 2024, Art. no. 1123. 

- [17] N. A. Agana and A. Homaifar, “A deep learning based approach for longtermdroughtprediction,”in _Proc.SoutheastCon_ 2017,Concord,NC,USA, 2017, pp. 1–8. 

- [18] Y. Zhao, H. Wu, J. Li, and Q. Du, “LSFuseNet: Dual-fusion of Landsat-8 and Sentinel-2 multispectral time series for permutation invariant applications,” in _Proc. IEEE 10th Int. Conf. Data Sci. Adv. Analytics (DSAA)_ , 2023, pp. 201–208. 

- [19] P. Nikdad, M. Ghaleni, M. Moghaddasi, and B. Pradhan, “Enhancing a machine learning model for predicting agricultural drought through feature selection techniques,” _Appl. Water Sci._ , vol. 14, 2024, Art. no. 125, doi: 10.1007/s13201-024-02193-4. 

- [20] P. Sreevidya, S. Veni, and O. V. Ramana Murthy, “Elder emotion classification through multimodal fusion of intermediate layers and crossmodal transfer learning,” _Signal, Image Video Process._ , vol. 16, no. 5, pp. 1281–1288, 2022, doi: 10.1007/s11760-021-02079-x. 

- [21] H. Chen et al., “A novel agricultural drought index based on multi-source remote sensing data and interpretable machine learning,” _Agricultural Water Manage._ , vol. 308, 2025, doi: 10.1016/j.agwat.2025.109303. 

- [22] A. Sivasubramanian, D. Sasidharan, V. Sowmya, and V. Ravi, “Efficient feature extraction using light-weight CNN attention-based deep learning architectures for ultrasound fetal plane classification,” _Phys. Eng. Sci. Med._ , 2025, pp. 1–15, doi: 10.1007/s13246-025-01566-6. 

- [23] F. Prodhan et al., “Deep learning for monitoring agricultural drought in South Asia using remote sensing data,” _Remote Sens._ , vol. 13, 2021, doi: 10.3390/rs13091715. 

- [24] K. Sundararajan and K. Srinivasan, “A synergistic optimization algorithm with attribute and instance weighting approach for effective drought prediction in tamil nadu,” _Sustainability_ , vol. 16, no. 7, 2024, Art. no. 2936, doi: 10.3390/su16072936. 

- [25] J. Wu, Q. Cheng, H. Li, S. Li, X. Guan, and H. Shen, “Spatiotemporal fusion with only two remote sensing images as input,” _IEEE J. Sel. Topics Appl. Earth Observ. Remote Sens._ , vol. 13, pp. 6206–6219, 2020, doi: 10.1109/JSTARS.2020.3028116. 

- [26] J. Sigurdsson, S. Armannsson, M. Ulfarsson, and J. Sveinsson, “Fusing Sentinel-2 and Landsat 8 satellite images using a model-based method,” _Remote Sens._ , vol. 14, 2022, Art. no. 3224, doi: 10.3390/rs14133224. 

**Aravinth J** (Member, IEEE) received the B.E. degree in electronics and communication from Periyar University, Salem, India, in 2004, and the M.E. degree in applied electronics and the Ph.D. degree in information and communication engineering from Anna University, Chennai, India, in 2007 and 2017, respectively. 

He is an Associate Professor with the Department of Electronics and Communication Engineering, Amrita Vishwa Vidyapeetham, Coimbatore, India. Since 2010, he has been a Faculty Member with Amrita and is actively involved in research and development in the areas of his research fields. His research interests include digital image processing, hyperspectral remote sensing, LiDAR data processing, multimodal biometrics, and soft computing. 

**Anand R** (Member, IEEE) received the AICTE QIP SPONSORED PG (Diploma Program) in data science and quantum computing from the Atal Bihari Vajpayee-Indian Institute of Information Technology and Management, Gwalior, India, the M.Tech. degree in communication engineering and signal processing from the Amrita School of Engineering, Coimbatore, India, and the Ph.D. degree in optimization-based band selection for hyperspectral remote sensing from Amrita Vishwa Vidyapeetham and RRSCISRO, Bengaluru, in 2022. 



In 2023, he joined the Amrita Vishwa Vidyapeetham and RRSC, ISRO, Bangalore, India. His research interests include machine and deep learning for signal and image processing applications, signal and image analysis, and hyperspectral images. 

