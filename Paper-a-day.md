---
layout: page
title: Paper a day
permalink: /paper_a_day/
---



I've been inspired by [Tim Stuart](http://timoast.github.io/blog/2016-02-23-papers/) to try to read a paper every day. I'm going to track my progress here.

I have fallen off since the semester has started so I'm going to stop updating this page.




## September 21th, 2019

Samuel. Some Studies in Machine Learning Using the Game of Checkers.

## September 20th, 2019

Mattick. Rocking the foundations of molecular genetics. PNAS. []()

## September 19th, 2019

Lee et al. Simultaneous profiling of 3D genome structure and DNA methylation in single human cells. Nature Methods. []()

## September 18th, 2019

Finotello. Next-generation computational tools for interrogating cancer immunity. Nature Reviews Genetics. []()

## September 17th, 2019

Scocchia et al. Clinical whole genome sequencing as a first-tier test at a resource-limited dysmorphology clinic in Mexico. Genomic Medicine. []()

## September 16th, 2019

Grishin, Obbad, and Church. Data privacy in the age of personal genomics. Nature Biotechnology. []()

This is a short letter 


## September 15th, 2019
## September 14th, 2019
## September 13th, 2019


## September 12th, 2019

Soneson et al. A comprehensive examination of Nanopore native RNA sequencing for characterization of complex transcriptomes. Nature Communications. [https://doi.org/10.1038/s41467-019-11272-z](https://doi.org/10.1038/s41467-019-11272-z)

This paper investigates the direct sequencing of RNA molecules that was recently announced by ONT. The takeaway for me is that while this new method of RNA sequencing may find useful applications, it is not a panacea for all applications and has its own issues.


## September 11th, 2019

## September 10th, 2019



## September 9th, 2019



## September 8th, 2019

David Mumford. The Dawning of the Age of Stochasticity.

This was an optional reading for the probability course I am taking this semester. Mumford claims that this article is meant to be a polemic article. An interesting idea proposed is 


> The reductionist approach defines random variables in terms of measures, which are defined in terms of the theory of the reals, which are defined in terms of set theory, which is defined on top of predicate calculus. I'd like to propose instead that it should be possible to put random variables into the very foundations of both logic and mathematics and arrive at a more complete and more transparent formulation of the stochastic point of view. I do not have a complete formulation of this, but a sketch which draws on two sources I find very provocative.

I can't say I completely understood the formalism sketched out. Also interesting are the discussions of SDEs and Bayesian inference.



## September 7th, 2019

Bageritz et al. Gene expression atlas of a developing tissue by single cell expression correlation analysis. Nature Methods. [https://doi.org/10.1038/s41592-019-0492-x](https://doi.org/10.1038/s41592-019-0492-x)

This paper does some cool spatial transcriptomics in order to generate an atlas of the developing Drosophila wing. I am especially impressed by Figure 3. I didn't read this deeply, but it seems that they used a subset of genes (mapping genes) known to have spatially distinct patterns and generated maps for other genes using correlation to the mapping genes.



## September 6th, 2019

Saiz et al. Asynchronous fate decisions by single cells collectively ensure consistent lineage composition in the mouse blastocyst. Nature Communications. [https://doi.org/10.1038/ncomms13463](https://doi.org/10.1038/ncomms13463)

I originally grabbed this paper because I assumed from the title that it would use single cell sequencing, but it turns out that it actually uses a quantitative image analysis pipeline. There's a lot of developmental biology details here that I don't understand. From what I understood, they used quantitative imaging of fluorescent labeling in order to tease out how lineage formation is coordinated in blastocysts. I didn't get much out of this paper because my knowledge was insufficient to understand it.



## September 5th, 2019

Kircher et al. Saturation mutagenesis of twenty diseaseassociated regulatory elements at single base-pair resolution. Nature Communications. [https://doi.org/10.1038/s41467-019-11526-w](https://doi.org/10.1038/s41467-019-11526-w)

In this paper the authors performed saturation mutagenesis with massively parallel reporter assays on 20 diseaseassociated gene promoters and enhancers This gave them functional measurements for 30,000+ single nucleotide substitutions and deletions. Access to the dataset has been provided at [this website](https://mpra.gs.washington.edu/satMutMPRA/). This is definitely a paper worth digging into more.



## September 4th, 2019

Deelen et al. A meta-analysis of genome-wide association studies identifies multiple longevity genes. Nature Communications. [https://doi.org/10.1038/s41467-019-11558-2](https://doi.org/10.1038/s41467-019-11558-2)

This is a meta-analysis of longevity GWA studies. The results were consistent with past studies in identifying associations with APOE (of multiple variants). Using GTEx, they also found associations with tissue-specific expression and survival to the 90th percentile age.



## September 3rd, 2019

Buschmann. and Bystrykh. Levenshtein error-correcting barcodes for multiplexed DNA sequencing. BMC Bioinformatics. [https://doi.org/10.1186/1471-2105-14-272](https://doi.org/10.1186/1471-2105-14-272)

This paper describes improved error correction for multiplexed sequencing. The algorithm is available in the Bioconductor package [DNABarcodes](https://bioconductor.org/packages/release/bioc/html/DNABarcodes.html). Rather than using Hamming distance, the authors use an adaptated Levenshtein distance that is more effective in the context of DNA sequences. I read this paper because someone mentioned the package in the Shalek Lab. While the paper was originally meant for multiplexing samples, single cell sequencing is an important new application of multiplexing and error correction in this situation is key.



## September 2nd, 2019

Runcie and Crawford. Fast and flexible linear mixed models for genome-wide genetics. PLOS Genetics. [https://doi.org/10.1371/journal.pgen.1007978](https://doi.org/10.1371/journal.pgen.1007978)

This paper introduces Grid-LMM, an algorithm for fitting linear mixed models in statistical genetics. The idea is to use grid search over the simplex of possible parameter values (after a reparameterization to estimate variance component proportions so that the parameters sum to 1). Grid-LMM produces well-calibrated test statistics and is fast for a relatively small number of random effects.



## September 1st, 2019

Sanchez-Taltavull et al. Bayesian Correlation is a robust similarity measure for single cell RNA-seq data. bioRxiv. [http://dx.doi.org/10.1101/714824](http://dx.doi.org/10.1101/714824)

This paper develops Bayesian correlation, which is a basically Pearson correlation using posterior estimates as inputs. They show that with larger numbers of cells, results are consistent between classical Pearson correlation and Bayesian correlation, but that Bayesian correlation is more robust to the problems with single cell data with smaller numbers of cells. 



## August 31st, 2019

Pierson and Yau. ZIFA: Dimensionality reduction for zero-inflated single-cell gene expression analysis. [https://doi.org/10.1186/s13059-015-0805-z](https://doi.org/10.1186/s13059-015-0805-z)

This paper develops a model for factor analysis in the zero-inflated setting. The model is as follows: let \\(N\\) be the number of samples, \\(D\\) be the number of genes, and \\(K\\) be the number of latent dimensions. The data, \\(Y\\), is assumed to be generated by the following hierarchical model

$$z_i \sim N(0, I)$$
$$x_i | z_i \sim N(A z_i + \mu, W)$$
$$h_{ij} | x_{ij} \sim \text{Bernoulli}(p_0)$$

and then \\(y_{ij}\\) is either kept or set to 0 depending on the value of \\(h_{ij}\\). We assume \\(p_0 = e^{-\lambda \mu^2}\\) where \\(\mu\\) is the average expression of the gene and \\(\lambda\\) is a fitted parameter. The model parameters are determined using the EM algorithm.



## August 30th, 2019

Petti et al. A general approach for detecting expressed mutations in AML cells using single cell RNA-sequencing. Nature Communications. [https://doi.org/10.1038/s41467-019-11591-1](https://doi.org/10.1038/s41467-019-11591-1)

This paper describes a nice AML study where the authors performed eWGS (enhanced WGS, i.e. they used enrichment capture for the exome on top of WGS in order to get high coverage of the exome while simultaneously getting genome-wide coverage.), bulk RNAseq, and scRNAseq. They used a tool called cb_sniffer to do single cell pileups (and validated with the additional data) and used SciClone to infer the clonal architecture of each tumor.



## August 29th, 2019

Libbrecht and Noble. Machine learning in genetics and genomics. Nature Reviews Genetics. [https://doi.org/10.1038/nrg3920](https://doi.org/10.1038/nrg3920)

This review gives an overview of many fundamental topics in machine learning using examples taken from genetics and genomics. It may be a good intro for a biologist that doesn't have much experience in machine learning.



## August 28th, 2019

Dey et al. Visualizing the structure of RNA-seq expression data using grade of membership models. PLOS Genetics. [https://doi.org/10.1371/journal.pgen.1006599](https://doi.org/10.1371/journal.pgen.1006599)

This is a paper out of Matthew Stephens group and uses grade of membership models (i.e. LDA, STRUCTURE models) for the analysis of RNA-seq data from the GTEx dataset (using K=20). They also apply the model to several other datasets (including single cell). This paper is mostly a pitch for using grade of membership models in the analysis of RNA seq data (they even say as much in the first sentence of the discussion).



## August 27th, 2019

Robert and Casella. A Short History of Markov Chain Monte Carlo: Subjective Recol lections fromIncomplete Data. Statistical Science. [https://http://doi.org/10.1214/10-STS351](https://http://doi.org/10.1214/10-STS351)

This paper gives a nice history of MCMC from its origins in the Manhattan Project through the so-called MCMC revolution.



## August 26th, 2019

Chung et al. Statistical significance of variables driving systematic variation in high-dimensional data. Bioinformatics. [https://doi.org/10.1093/bioinformatics/btu674](https://doi.org/10.1093/bioinformatics/btu674)

This paper introduces a new approach called the **jackstraw** that identifies genomic variables that are statistically significantly associated with any subset or linear combination of PCs.






## August 25th, 2019

Yuan et al. Challenges and emerging directions in single-cell analysis. Genome Biology. [https://dx.doi.org/10.1186%2Fs13059-017-1218-y](https://dx.doi.org/10.1186%2Fs13059-017-1218-y)

This paper is essentially a laundry list of general problems in single cell methods. More interesting is the discussion of some future directions with spatial methods, in situ methods, lineage tracing, and muli-omic methods. I think if you're somewhat engaged in the single cell world that this paper doesn't have ideas you haven't been exposed to.



## August 24th, 2019

Ranganath et al. Black Box Variational Inference. PMLR. [http://proceedings.mlr.press/v33/ranganath14.html](http://proceedings.mlr.press/v33/ranganath14.html)






## August 23rd, 2019

Wherry. T cell exhaustion. Nature Immunology. [https://doi.org/10.1038/ni.2035](https://doi.org/10.1038/ni.2035)

This is a review on T cell exhaustion, which is the dysfunction or removal of antigen-specific T cells during chronic insults (infection, cancer etc.). This is a really great resource and I imagine that I will refer back to it in the future. Especially interesting from the perspective of scRNAseq users is that there are transcriptional phenotypes of exhaution and that exhausted cells of the same type are as dissimilar as different cell types.



## August 22nd, 2019

Yang et al. An enhanced genetic model of colorectal cancer progression history. Genome Biology. [https://doi.org/10.1186/s13059-019-1782-4](https://doi.org/10.1186/s13059-019-1782-4)

This paper analyzes 63 colorectal cancers in an attempt to discern the relative ordering of somatic mutations within those cancers. From the abstract:

> We find that driver point mutations, gene fusions, and arm-level copy losses typically arise early in tumorigenesis; different mechanisms act on distinct genomic regions to drive DNA copy changes; and chromothripsis—clustered rearrangements previously thought to occur as a single catastrophic event—is frequent and may occur multiple times independently in the same tumor through different mechanisms.



## August 21st, 2019

Gopalan et al. Scaling probabilistic models of genetic variation to millions of humans. Nature Genetics. [https://doi.org/10.1038/ng.3710](https://doi.org/10.1038/ng.3710)

This paper is an implementation of the STRUCTURE model using stochastic variational inference to speed up model inference. It's speed is competitive with ADMIXTURE and is much faster than other methods of posterior inference for STRUCTURE. The claim is that it can handle data size up the "tera" scale (i.e. \\(10^6\) individuals with \\(10^6\\) genotypes measured).



## August 20th, 2019

Raj et al. fastSTRUCTURE: Variational Inference of Population Structure in Large SNP Data Sets. Genetics. [https://doi.org/10.1534/genetics.114.164350](https://doi.org/10.1534/genetics.114.164350)

This paper is an implementation of the STRUCTURE model using variational inference to speed up model inference. It is still slower than ADMIXTURE (which optimizes a point estimate for the model, rather than finding the posterior distribution on the parameters).



## August 19th, 2019

Salimans et al. Markov Chain Monte Carlo and Variational Inference: Bridging the Gap. PMLR. [http://proceedings.mlr.press/v37/salimans15.html](http://proceedings.mlr.press/v37/salimans15.html)






## August 18th, 2019

Blei et al. Variational Inference: A Review for Statisticians. Journal of the American Statistical Association. [https://doi.org/10.1080/01621459.2017.1285773](https://doi.org/10.1080/01621459.2017.1285773)






## August 17th, 2019







## August 16th, 2019

The “All of Us” Research Program. NEJM. [doi.org/10.1056/NEJMsr1809937](doi.org/10.1056/NEJMsr1809937)

The All of Us research program is an effort to gather data from over 1 million individuals living in the US, especially seeking those who have been underrepresented in biomedical research (i.e. people not of European descent). Participants provide access to their EHR and also provide biospecimens to be tested for DNA, RNA, cfDNA, and physiological measurements. Many other sources of data are being collected as well, including using a smartphone. Data access will hopefully be available in 2020. Something else I think is worth mentioning is Sync for Science (a program for patients to opt-in to sharing their data with researchers).



## August 15th, 2019

Lotfollahi et al. scGen predicts single-cell perturbation responses. Nature Methods. [https://doi.org/10.1038/s41592-019-0494-8](https://doi.org/10.1038/s41592-019-0494-8)

This paper presents a deep model for predicting single cell responses to perturbation. The idea is to use train a variational autoencoder on perturbed single cell data. The VAE learns a latent space where perturbations can be represented by a single vector, \\(\delta\\). Then, cells that don't have corresponding perturbation data can be projected into the latent space, extrapolated using \\(\delta\\), and then decoded back into expression space. They demonstrate superior performance out of sample, in infection response, and across species.



## August 14th, 2019

Rahimi and Recht. Random Features for Large-Scale Kernel Machines. Neurips. [http://papers.nips.cc/paper/3182-random-features-for-large-scale-kernel-machines.pdf](http://papers.nips.cc/paper/3182-random-features-for-large-scale-kernel-machines.pdf)

This paper introduces the concept of random features for approximating kernel machines. In a kernel machine, you typically will operate on your data projected into a higher dimensional feature space (without actually projecting due to the nature of kernels). Rahimi and Recht show how to instead project your data into lower dimensional random feature spaces that where distances between points approximate the distances between points in the kernel space. Then, fast methods for solving linear SVMs can be applied to learn the decision boundary. This a really cool paper that I need to really dig my teeth into to understand the theory behind. In particular I want to understand how they came up with the idea of random Fourier features. Was this procedure already well-known? Did they already know the theorem they apply from harmonic analysis?



## August 13th, 2019

Allen and Mehler. Open science challenges, benefits and tips in early career and beyond. PLOS Biology. [https://doi.org/10.1371/journal.pbio.3000246](https://doi.org/10.1371/journal.pbio.3000246)

This is a discussion of open science, which the authors consider methods to improve scientific practices. These methods include sharing of resources, changing how we publish, choice of research questions (i.e. including replications and reanalysis as a valuable pursuit), and changes in methodology. Three challenges are described: restrictions on flexibility, time cost, no incentive structure in place. And three benefits are described: greater faith in research, new helpful systems, investment in your future. I think I had some idea about almost everything discussed in the article, but it was still a useful read.



## August 12th, 2019

Merton. The Matthew Effect in Science. Science. [https://doi.org/10.1126/science.159.3810.56](https://doi.org/10.1126/science.159.3810.56)

The Matthew Effect is the concept that advantages accumulate (i.e. the rich get richer). This paper is an investigation into the reward and communication systems in science. A key idea is that of the "41st chair". The French Academy only 40 individuals could qualify as members and so many talented individuals were excluded (including Descartes, Pascal, Rousseau, Proust and many more). The same happens with the Nobel Prize and other accolades. Nobel laureates have noted that famous scientists tend to soak up more credit while unknown scientists receive little to no credit for work of similar importance. It also appears that the same is true for scientists determining what literature to keep up to date on. They tend to read the work of investigators that they know and are familiar with, which results in the work of well-known scientists being much more likely to be read. One striking figure in the paper was "six universities (Harvard, Berkeley, Columbia, Princeton, California Institute of Technology, and Chicago) which produced 22 percent of the doctorates in the physical and biological sciences produced fully 69 percent of the Ph.D.'s who later became Nobel laureates."



## August 11th, 2019

Zeng et al. Increasing trend of scientists to switch between topics. Nature Communications. [https://doi.org/10.1038/s41467-019-11401-8](https://doi.org/10.1038/s41467-019-11401-8)

This paper studies the dynamics of researcher behavior. They investigated the number of research areas that researchers typically are involved in, how this has developed over time, and how this impacts researcher productivity. Interestingly, switching topics early in your career was associated with lower early career productivity, but higher late career productivity. Also, switching topics has become increasingly common over time.



## August 10th, 2019

Langan et al. De novo design of bioactive protein switches. Nature. [https://doi.org/10.1038/s41586-019-1432-8](https://doi.org/10.1038/s41586-019-1432-8)







## August 9th, 2019

van Dijk et al. Recovering Gene Interactions from Single-Cell Data Using Data Diffusion. Cell. [https://doi.org/10.1016/j.cell.2018.05.061](https://doi.org/10.1016/j.cell.2018.05.061)

This paper introduces MAGIC (Markov affinity-based graph imputation of cells), a method for imputation in scRNAseq data.







## August 8th, 2019

Stark et al. RNA sequencing: the teenage years. Nature Reviews Genetics. [https://doi.org/10.1038/s41576-019-0150-2](https://doi.org/10.1038/s41576-019-0150-2)

This is a really nice review of RNAseq. It describes and compares short and long read sequencing technologies, library prep techniques, experimental design, and computational analysis for bulk RNAseq experiments. Then, it discusses new developments in RNAseq methodology like single cell and spatial method. They also talk about methods for measuring active transcription and translation. Finally, they talk about how we can assay RNA's interactions with other molecules. If someone wants an overview RNAseq I think this is a decent place to start.



## August 7th, 2019

Siebert et al. Stem cell differentiation trajectories in Hydra resolved at single-cell resolution. Science. [https://http://doi.org/10.1126/science.aav9314](https://http://doi.org/10.1126/science.aav9314)








## August 6th, 2019

Reyna et al. Hierarchical HotNet: identifying hierarchies of altered subnetworks. Bioinformatics. [https://doi.org/10.1093/bioinformatics/bty613](https://doi.org/10.1093/bioinformatics/bty613)

Ben Raphael's lab has released another improvement to the HotNet algorithm. The method is illustrated in Fig 1 of the paper. 1. A biological interaction network and gene scores are combined to create a vertex-weighted graph. A joint similarity matrix \\(S\\) is derived from network topology and vertex weights using a random walks approach. 3. A dendrogram \\(T\\) of vertex sets is constructed frm \\(S\\) using symmetric hierarchical clustering. 4. Statistical significance is assessed for the hierarchical clustering. 5. Representative altered subnetworks are provided from the dendrogram. One high-level point from the discussion is "There is also a larger question about similarity measures on vertex-weighted graphs and what properties such measures should have. For the example, there is an interplay between the contributions from network topology and vertex weights, and an ideal method would attempt to quantify or balance these contributions to the discovery of a method’s results."



## August 5th, 2019

Sugden et al. Localization of adaptive variants in human genomes using averaged one-dependence estimation. Nature Communications. [http://doi.org/10.1038/s41467-018-03100-7](http://doi.org/10.1038/s41467-018-03100-7)

This paper presents a method called SWIF(r) (SWeep Inference Framework (controlling for correlation)). SWIF(r) uses AODEs to idenfity selective sweeps. In particular, SWIF(r) computes the per-site calibrated probability of a selective sweep. Posterior probablities are calibrated empirically and the model is trained using simulations of hard sweeps. The authors used SWIF(r) to identify known adaptive mutations in humans as well as to  identify previously unidentified adaptive variants in genomic data from the ‡Khomani San, a hunter-gatherer population in southern Africa.



## August 4th, 2019

Webb et al. Not So Naive Bayes: Aggregating One-Dependence Estimators. Machine Learning. [https://doi.org/10.1007/s10994-005-4258-6](https://doi.org/10.1007/s10994-005-4258-6)

This paper introduces Averaged One-Dependence Estimators (AODEs), a generalization of the naive Bayes method that includes some dependence between features. While you could include any level of conditional relationships in your model, this can quickly create a combinatorial search space for model selection. Instead, AODEs include a small subset of possible models and average between them rather than attempting to do model selection. For any feature, \\(x_i\\) we have

$$P(y,x) = P(y,x_i) P(x|y,x_i)$$

and since this is true for all features, we can also average over some collection of \\(m\\) of them

$$P(y,x) = \frac{\sum_{i=1}^m P(y,x_i) P(x|y,x_i)}{m}.$$

This is the key insight behind AODEs. Instead of assuming independence between features, we instead choose a subset of \\(m\\) of them and estimate conditional distributions over all other features given that one (hence **one-dependence estimators**) and then we average each of these estimators (hence **averaged** one-dependence estimators).



## August 3rd, 2019

Leiserson et al. Pan-cancer network analysis identifies combinations of rare somatic mutations across pathways and protein complexes. Nature Genetics. [https://doi.org/10.1038/ng.3168](https://doi.org/10.1038/ng.3168)

This paper analyzes TCGA data with a (then) new algorithm called HotNet2 which has the goal of the algorithm is to identify mutated subnetworks. Using HotNet2 they identified known cancer pathways and pathways that have not been well-characterized in cancer and identified new genes within known cancer-related pathways. HotNet2 (HotNet diffusion-oriented subnetworks) is an extension of the HotNet algorithm that incorporates directionality of diffusion. The input is a heat vector that encodes the score (i.e. mutation frequency) for a gene and a graph of biological pathways/interactions. Then, HotNet2 uses an insulated diffusion process until the graph is at equilibrium. "Hot" subnetworks are identified and statistical significance is tested.



## August 2nd, 2019

Fan et al. Characterizing transcriptional heterogeneity through pathway and gene set overdispersion analysis. Nature Methods. [http://dx.doi.org/10.1038/nmeth.3734](http://dx.doi.org/10.1038/nmeth.3734)

This paper describes an extension to SCDE (see July 30th). The idea is to model the overdispersion of individual genes and then to apply pathway/gene set analysis. In addition the authors developed a method for identifying *de novo* gene sets using hierarchical clustering (Ward's method). I think I should read this paper and its methods more deeply.



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

Wang et al. Comparative analysis of differential gene expression analysis tools for single-cell RNA sequencing data. BMC Bioinformatics. []()

https://bmcbioinformatics.biomedcentral.com/track/pdf/10.1186/s12859-019-2599-6

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
