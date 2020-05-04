# Data Scientist Nanodegree Term 1 Project: Finding Donors

## Setup:

* Jupyter notebook 6.0.3
* Python 3.8.2
* Numpy 1.18.1
* Pandas 1.0.1
* IPython 7.12.0
* Matplotlib 3.1.3
* Scipy 1.4.1
* Sklearn

## Questions to reviewer:

1. I spent a lot of time proving dependent features via statistics methods (applying chi2 method because most features are categorical) but couldn't convince myself the chi2 I computed from scratch is correct... could you recommend an implemented library?
[Notes after review] Chi-square is only tested in categorical variables, intuitively we cannot even compare numeric-feature-vs-label-correlation against categorical-feature-vs-label-relationship... So it only makes sense to compare for example categorical-feature[1]-vs-label-relationship against categorical-feature[2]-vs-label-relationship using chi-square... Homework: Try scipy.stats.chisquare

2. I also wasted a lot of time finding a way to split features for one model e.g. Naive-Bayes and the other e.g. Boosting, and ensemble them given they predict based on splitted features. I kind of feel this is cool because many features seem correlated to each other by intuition, example: 'relationship' vs 'marital-status'... Again is there an implemented library?
[Notes after review] No one seems to train models that way, people usually build a [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html), in case of feature selection we may use [RecursiveFeatureElimination](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html).

3. GaussianNB assumes data being Gaussian distributed... seems there are other NB estimators from sklearn e.g. BernoulliNB that do not assume Gaussian distribution... I feel uncomfortable using GaussianNB to fit all features especially the categorical ones... Is there a library that combines BernoulliNB for categorical features and GaussianNB for numeric? (I'm not talking about ensemble here)
[Notes after review] There seems to be no such library from sklearn but from external resource there is a [Hybrid Naive Bayes](https://github.com/ashkonf/HybridNaiveBayes), perhaps incompatible to sklearn objects...
