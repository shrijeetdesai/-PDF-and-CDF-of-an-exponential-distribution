# README for -PDF-and-CDF-of-an-exponential-distribution

## Overview
This repository contains Python code to plot the Probability Density Function (PDF) and Cumulative Distribution Function (CDF) of an exponential distribution with a mean (μ) of 2/3, and to sample random variables from this distribution. It then compares the theoretical PDF with the sampled data using histograms.

## Requirements
To run this code, you need the following Python libraries:

numpy
matplotlib
You can install them via pip:
  #pip install numpy matplotlib

## Code Overview

# Parameters
mu: The mean of the exponential distribution. In this case, it is set to 2/3.
nsample: The number of random samples generated from the exponential distribution. Set to 10^6 (1 million samples).
x: A grid of values from 0 to 5, used to compute the PDF and CDF.

# Running the code
To execute the code, simply run the Python script:
python exponential_distribution.py

This will generate three plots:

A combined plot showing the PDF (red) and CDF (blue) of the exponential distribution.
A comparison between the sampled data (histogram) and the theoretical PDF (line plot).
A bar plot of the sampled data with the theoretical PDF overlaid.
The first figure is also saved as exponential.pdf in the current directory.

