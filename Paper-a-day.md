---
layout: page
title: Paper a day
permalink: /papers/
---

I've been inspired by [Tim Stuart](http://timoast.github.io/blog/2016-02-23-papers/) to try to read a paper every day. I'm going to track my progress here.


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
