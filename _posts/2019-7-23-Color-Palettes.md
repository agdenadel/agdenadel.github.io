---
layout: post
title: Color palettes
tags: programming libraries R plotting visualization
---

When I was working at Illumina one of my projects was to create a visualization for the results of the whole genome sequencing pipeline. I took my figure to one of my coworkers to ask him what he thought. His response was that he thought that the structure was nice, but he couldn't distinguish between some of the colors because he was colorblind. He shared [this article](https://www.nature.com/articles/nmeth.1618) with me, and that was my first real introduction into using different color palettes for figures.

Recently, someone else shared [this library](https://github.com/karthik/wesanderson) of Wes Anderson themed palettes with me. The palettes are mostly derived from [this blog](https://wesandersonpalettes.tumblr.com/) It seems like a fun way to make your color choices, although I haven't tried it out on any of my plots yet. Here are the palettes available (image taken from [this blog post](https://www.datanovia.com/en/blog/top-r-color-palettes-to-know-for-great-data-visualization/))

![Wes Anderson Palettes](/images/color-palettes/029-r-color-palettes-wes-anderson-color-palettes-r-1.png)

In case you're interested, here's an example of the plot I created. The top plot shows all of the structural variants that were called by plotting a parabola from startpoint to endpoint with the height representing the confidence of the call (it's very messy because this particular cancer sample has a lot of structural variants). The bottom two figures are both coverage plots and the middle plot is color-coded by copy number variation calls of various types. 

![SV and CNV plot](/images/color-palettes/NA12892-Rep03-combined_S1.summary.png)