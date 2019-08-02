---
layout: page
title: Paper a day
permalink: /papers/
---

I've been inspired by [Tim Stuart](http://timoast.github.io/blog/2016-02-23-papers/) to try to read a paper every day. I'm going to track my progress here.


## August 1st, 2019

Tian and Taylor. Selective inference with a randomized response. The Annals of Statistics. [doi.org/10.1214/17-AOS1564](doi.org/10.1214/17-AOS1564)

I didn't completely read this paper. There are lemmas in it that I already can't state from memory and I didn't even read the proofs. The big idea is to apply an idea from privacy research (randomized response) to the problem of model selection and inference for linear regression. In randomized response, you (the statistician) artificially add noise to your data before performing your analysis. This is used for research in delicate areas (say on crime where study participants won't necessarily want to answer honestly). For example, participants may flip a coin before answering a question and they will answer honestly if the coin comes up heads and always answer true if the coin comes up tails. You can then subtract out the expected number of "true" responses to find the actual proportion. To use this idea in model selection and inference you add some noise to your data for model selection and then do your inference with the original data. This improves the calibration of your inference (see the paper I read on July 26th).


## July 31st, 2019

Efron et al. Empirical Bayes Analysis of a Microarray Experiment. Journal of the American Statistical Association. [https://doi.org/10.1198/016214501753382129](https://doi.org/10.1198/016214501753382129)

This paper describes the use of empirical Bayes for gene expression data. The authors describe a comparative experiment where there are two biological samples (1,2) and these samples are either un-irradiated or irradiated (U,I) with two technical replicates of each resulting in 8 samples: U1A, U1B, I1A, I1B, U2A, U2B, I2A, I2B. Then, the key idea is to use the technical replicates to generate empirical null distributions.



## July 30th, 2019

Kharchenko et al. Bayesian approach to single-cell differential expression analysis. Nature Methods. [https://doi.org/10.1038/nmeth.2967](https://doi.org/10.1038/nmeth.2967)

This paper describes a Bayesian method for single-cell differential expression that the Kharchenko lab developed called SCDE. A major insight is that there are two types of measured transcripts in two-single cells of the same cell type: correlated transcripts and those affected by dropout. The authors model this situation by using a mixture model with two components. The first is a negative binomial component for the correlated transcripts and then second is a low-magnitude Poisson component for dropout (rather than simply a constant zero component). The EM algorithm is used on each cell to estimate mixture components and then bootstrap is used for differential expression analysis. You can find the software [here](https://hms-dbmi.github.io/scde/).



## July 29th, 2019

This study evaluates methjods for differential expression analysis in scRNAseq data (SCDE, MAST, scDD, D3E, Monocle2, SINCERA, DEsingle, SigEMD). It briefly describes the model used in each method and then evaluates them all on simulated and real data. Something concerning is the low concordance between methods on real data. Simulations are great, but gold standard single cell data like we have in whole genome sequencing would be nice.



## July 28th, 2019

Stensrud and Valberg. Inequality in genetic cancer risk suggests bad genes rather than bad luck. Nature Communications. [https://doi.org/10.1038/s41467-017-01284-y](https://doi.org/10.1038/s41467-017-01284-y)

This is an interesting paper to read soon after the paper by Tomasetti and Vogelstein that I read on July 23rd. While we often estimate heritability of disease using twin studies and GWAS, these heritability estimates are only a single number and tell us nothing about the distribution of genetic risk among the population. In this paper the authors model this distribution in order to understand the **inequality** of genetic cancer risk. There are potentially public health consequences from this. If we can identify the individuals who carry the majority of the heritable risk for cancer, we could preferentially screen them for the cancers that they are most susceptible to.


## July 27th, 2019

Efron. Large-Scale Simultaneous Hypothesis Testing: The Choice of a Null Hypothesis. Journal of the American Statistical Association. [https://dx.doi.org/10.1198/016214504000000089](https://dx.doi.org/10.1198/016214504000000089)

This paper develops a strategy for using an empirical Bayes strategy for determining the null distribution of test statistics when conducting multiple hypothesis tests. Efron also discusses using the **local FDR** for inference.




## July 26th, 2019

Taylor and Tibshirani. Statistical learning and selective inference. PNAS. [https://doi.org/10.1073/pnas.1507583112](https://doi.org/10.1073/pnas.1507583112)

This paper is an introduction to the idea of selective inference. Selective inference is the idea of properly assessing statistical significance when you have "cherry-picked" the statistical tests that you are running. Exact solutions for this problem are given in the case of testing significance of coefficients identified by forward stepwise regression and LASSO regression. These exact solutions are derived in other papers from the authors. I think this paper was meant to be an introduction to the topic for a broader audience.



## July 25, 2019

Zhang, Xu, and Yosef. Simulating multiple faceted variability in single cell RNA sequencing. Nature Communications. [https://doi.org/10.1038/s41467-019-10500-w](https://doi.org/10.1038/s41467-019-10500-w)

This paper presents a new single-cell RNAseq simulator that models three types of variation: "noise intrinsic to the process of transcription, extrinsic variation indicative of different cell states (both discrete and continuous), and technical variation due to low sensitivity and measurement noise and bias". Extrinsic variation refers to differences in cellular states (i.e. cell type, stage of cell cycle, etc), intrinsic variation includes using a kinetic model to generate "true" counts based off the extrinsic variation, and technical variation includes biases introduced from assay steps (fragmentation, PCR, sensitivity, UMIs, sequencing, etc.). You can turn each of these knobs in the SymSim software associated with the paper. They use SymSim to generate datasets to evaluate methods for clustering, differential expression and trajectdory inference.

## July 24, 2019

Traag, Waltman, and van Eck. From Louvain to Leiden: guaranteeing well-connected communities. Scientific Reports. [https://doi.org/10.1038/s41598-019-41695-z](https://doi.org/10.1038/s41598-019-41695-z)

The Louvain algorithm is a common one for community detection in networks. In this paper the authors discuss a defect in the algorithm that results in communities that have undesired properties (badly connected, disconnected). An alternative algorithm (the Leiden algorithm) is proposed to remedy these problems. It never produces disconnected communities, has fewer badly connected communities, and even runs faster (in some cases musch faster) than Louvain. The Leiden algorithm provides a number of guarantees. I can't say that I understand the algorithm right now since I only read the main text and the algorithm is in the supplemental (as are proofs of the guarentees). 

## July 23, 2019

Tomasetti and Vogelstein. Variation in cancer risk among tissues can be explained by the number of stem cell divisions. Science. [https://doi.org/10.1126/science.1260825](https://doi.org/10.1126/science.1260825)

This is a short paper that shows a strong correlation (0.81) between lifetime risk of cancer in a particular tissue and the total number of stem cell divisions in that tissue. They segment cancers by (by tissue) into cancers whose initiation are mostly due to stochastic effects and those that are more preventable.

## July 22, 2019

Skinnider et al. Evaluating measures of association for single-cell transcriptomics. Nature Methods. [https://doi.org/10.1038/s41592-019-0372-4](https://doi.org/10.1038/s41592-019-0372-4)

The main takeaway from this paper is that we might want to use so-called **proportionality** measures for as our measures of association for single-cell data. I find this idea pretty interesting and want to read further about it. Two papers that propose this idea (and that I plan to read) are Lovell et al. 2014 and Quinn et al. 2017.
