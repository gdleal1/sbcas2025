# <p align="center">Can Data Complexity Measures Detect Pre-Training Bias in Machine Learning? A Case-Study with Health Data.</p>

# 📖 About 
This repository was developed during my time as a scientific initiation fellow at Instituto de Informática - UFRGS. A paper summarizing the results obtained was written for the project. This paper was submitted and accepted for SBCAS 2025 (Simpósio Brasileiro de Computação Aplicada à Saúde). 

# 🚀 Install and Run
## 1. (Optional) Set up a virtual environment:
```bash
python -m venv venv
source venv/bin/activate    
```

## 2. Install the dependencies:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 3. Clone the repository:
```bash
git clone https://github.com/gdleal1/sbcas2025.git
```

## 4. Code execution
The execution guide and description of the files used in the project is available in [EXECUTION_GUIDE.txt](EXECUTION_GUIDE.txt).

# Abstract
This study investigates the potential of data complexity measures to identify biases in health datasets that may affect the fairness of machine learning models. Bias in healthcare data can lead to unfair outcomes for vulnerable populations, undermining the integrity and reliability of predictive models in medical applications. Our approach uses data complexity metrics to identify features at risk of introducing bias into model training. We validate our approach by comparing the identified features with traditional pre-training bias metrics, establishing the value of complexity measures as early indicators of bias. This complexity-based bias detection framework can inform bias mitigation strategies, such as feature selection and data reweighting, to improve model fairness in health-related machine learning applications. The results provide insights into using data complexity for bias detection and open pathways to fairer and more transparent predictive models in healthcare.

# Data Complexity Measures
Understanding the complexity of a dataset is fundamental to mitigating biases in machine learning models since complexity is directly related to the quality and diversity of the data, as well as the model's ability to generalize without learning biased patterns. The **data complexity measures** used in our study describe the regularities and irregularities contained in a dataset and are used to estimate the difficulty of separating instances into their expected classes. These measures were implemented in a R package called **ECoL**, divided into three groups:

**1) Featured-based measures:** Describe the level of information provided by the attributes available to distinguish the classes. Includes measures F1, F1v, F2, F3 and F4:

1. *Maximum Fisher’s discriminant ratio (F1):* Measures the separability between classes by comparing the average difference between the classes with the sum of the intra-class variances.
2. *The Directional-vector Maximum Fisher’s Discriminant Ratio (F1v):* Seeks to find a vector in the space of attributes that best separates the classes after projecting the data.
3. *Volume of overlap region (F2):* Calculates the overlap of attribute distributions within classes.
4. *Maximum Individual Feature Efficiency (F3):* Estimates the individual efficiency of each attribute in the separation of data classes. 
5. *Collective Feature Efficiency (F4):* Quantifies the number of steps needed to separate all the examples in a dataset by iteratively using the most discriminating attributes.

**2) Linearity measures:** Evaluates the feasibility of separating classes using a linear approach. Includes measures L1, L2 and L3:

1. *Sum of the Error Distance by Linear Programming (L1):* Evaluates whether the data is linearly separable by computing incorrectly classified examples for a linear threshold used in their classification.
2. *Error Rate of Linear Classifier (L2):* Measures linear separability in the original training dataset. 
3. *Non-Linearity of a Linear Classifier (L3):* Creates a new dataset by linearly interpolating pairs of examples from the same class. It uses a linear classifier trained on the original data, and its error rate is measured on the interpolated examples.

**3) Neighborhood measures:**  Characterize the presence and density of equal or different classes in local neighborhoods. Includes measures N1, N2, N3, N4, N5 and N6:

1. *Fraction of Borderline Points (N1):* Estimates the size and complexity of the class separation problem by identifying critical points in the data set, i.e., data that are very similar to each other but belong to different classes.
2. *Ratio of Intra/Extra Class Nearest Neighbor Distance (N2)*: Computes the overall distance between examples of different classes and the total distance between examples of the same class.
3. *Error Rate of the Nearest Neighbor Classifier (N3):* Evaluates the complexity of a dataset based on the error rate of a 1NN classifier.
4. *Non-Linearity of the Nearest Neighbor Classifier (N4):* Evaluates the non-linearity of a dataset based on the behavior of a NN classifier.
5. *Fraction of Hyperspheres Covering Data (T1 or N5):* Quantifies the complexity of the dataset based on how well the data can be covered by hyperspheres in feature space.
6. *Local Set Average Cardinality (LSC or N6):* Measures the local homogeneity of a dataset by calculating the average number of close neighbors belonging to the same class.

It is important to note that most of these measures vary between 0 and 1. **The closer the value is to the upper limit, the greater the complexity of the dataset analyzed.**

**All Measures in ECoL package:**

![Screenshot from 2024-10-25 09-30-14](https://github.com/user-attachments/assets/47434638-4e4b-4edf-acf4-20952162885b)

---

# Pre-Training Bias Metrics
The pre-training bias metrics used in this work consider for the calculation a demographic attribute that has
two values: One represents the group favored by the bias, i.e. the over-represented or
advantaged group. The other value represents the group disfavored by the bias, i.e. the
underrepresented or disadvantaged group. For example, if the attribute is sex, the favored
group is male and the disfavored group is female. These metrics are as follows:

**1) Class Imbalance (CI):** Measures the imbalance in the distribution of instances
between the groups of the demographic attribute considered. The values vary
between -1 and 1, with positive values indicating that instances of the favored
group have greater representation than the disadvantaged.

**2) Kullback-Leibler (KL) Divergence:** Measures the difference between label dis-
tributions (target attribute) for the groups of the demographic attribute considered.
The range of values for this metric is between 0 and ∞, with values close to zero
meaning that the different values for the target attribute are similarly distributed.

**3) Kolmogorov-Smirnov (KS):** Measures the maximum divergence between labels
in the distribution for the groups of the demographic attribute considered. The
values vary between 0 and 1, with values close to zero indicating that the target
attribute is more evenly distributed between the groups.

**5) Conditional Demographic Disparity in Labels (CDDL):** Evaluates demo-
graphic disparity by checking whether the target attribute is independent of the
demographic attribute considered. The values vary between -1 and 1, with pos-
itive values indicating demographic disparity and negative values suggesting the
opposite.

---

# Results

## 1. Intersectional-Bias Dataset
### a) Complexity measures for original dataset and variations:
![image](https://github.com/user-attachments/assets/f1bdd07d-b1e9-45c7-8ab6-ba370c5126ea)

### b) PCA graphics for variations:
![image](https://github.com/user-attachments/assets/0d132dc8-a279-4338-bff6-fe4f6eced4ce)

### c) Scores for original dataset and variations:
![image](https://github.com/user-attachments/assets/73dab500-312b-40c1-9136-0426fd7f3382)

### d) Pre-Training Bias Metrics:
![image](https://github.com/user-attachments/assets/13e13099-fbae-409c-85d5-02b22c0aedab)

## 2. Indian Liver Patient Dataset
### a) Complexity measures for original dataset and variations:
![original-female-male](https://github.com/user-attachments/assets/d28e1f03-7339-45c9-9728-3addb18e366e)

### b) PCA graphics for variations:
![image](https://github.com/user-attachments/assets/9230d010-c343-41b0-823e-7b63e44747ba)

### c) Scores for original dataset and variations:
![original-female-male-compare](https://github.com/user-attachments/assets/191dcf1e-de71-4056-a2c4-30e133ca1b7b)

### d) Pre-Training Bias Metrics:
![image](https://github.com/user-attachments/assets/2fced41f-8ea0-41f5-be08-bee93ec965a0)

# Conclusion
This study demonstrated that data complexity measures can indicate groups favored by bias in a dataset. In the Intersectional-Bias Dataset, the difference in complexity between the disadvantaged and advantaged groups was evident from the scores and pre-training metric calculations. Both the female and non-white groups proved to be the most negatively affected in the overall context of the dataset. Nevertheless, in the Indian Liver Patient Dataset, scores for the disadvantaged class did not increase in all complexity groups, and the pre-training bias metrics were not considerably low values. However, as the results show, we point out that the dataset is not free of bias that favors the male group.

The conclusions reached in this work contribute to the current context of machine learning models and data classification and motivate further experiments. By calculating the complexity of subsets of data divided according to a protected attribute and comparing the results with pre-training bias metrics, we suggest that this new approach can pose a new tool to obtain fairer results, especially in health scenarios. For future works, we aim to expand our experiments to new datasets and conduct a systematic analysis of results to derive stronger hypotheses and conclusions.

---

## Packages used:
 **ECoL:** https://github.com/lpfgarcia/ECoL
 
---
# References:
[1] [Arruda et al. 2020] Arruda, J. L., Prudˆencio, R. B., and Lorena, A. C. (2020). Measur-
ing instance hardness using data complexity measures. In Intelligent Systems: 9th
Brazilian Conference, BRACIS 2020, Rio Grande, Brazil, October 20–23, 2020, Pro-
ceedings, Part II 9, pages 483–497. Springer.

[2] [Karamizadeh et al. 2013] Karamizadeh, S., Abdullah, S. M., Manaf, A. A., Zamani, M.,
and Hooman, A. (2013). An overview of principal component analysis. Journal of
signal and information processing, 4(3):173–175.

[3] [Lorena et al. 2019] Lorena, A. C., Garcia, L. P. F., Lehmann, J., Souto, M. C. P., and Ho,
T. K. (2019). How complex is your classification problem?: A survey on measuring
classification complexity. ACM Computing Surveys (CSUR), 52(1):1–34.

[4] [Maslej et al. 2022] Maslej, M. et al. (2022). Intersectional-Bias-Assessment. INCF.
Available on internet: https://training.incf.org/lesson/intersectional-approach-model-construction-and-evaluation-mental-healthcare.

[5] [Ramana and Venkateswarlu 2022] Ramana, B. and Venkateswarlu, N. (2022). ILPD
(Indian Liver Patient Dataset). UCI Machine Learning Repository. DOI:
https://doi.org/10.24432/C5D02C.

[6] [Sotoca et al. 2005] Sotoca, J. M., S´anchez, J. S., and Mollineda, R. A. (2005). A review
of data complexity measures and their applicability to pattern classification problems.
Actas del III Taller Nacional de Mineria de Datos y Aprendizaje. TAMIDA, 77.
