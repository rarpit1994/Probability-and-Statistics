#!/usr/bin/env python
# coding: utf-8

# <b> <h1> Maximum Likelihood Estimation (MLE) </h1> </b>
# 
# The Maximum Likelihood Estimation (MLE) provides a way to determines the natural parameters (The parameters on which the algorithm's performance governs) optimal values and other.
# 
# The provides the following things like:
# <ol>
#     <li> It provides the point estimate i.e., if the algorithm is having more than 1 natural parameters it can provide best natural parameter for the respective algorithm.</li>
#     <li> It can provide the best estimator of the respective algorithm i.e., Mean/ Mode/ Meadian. </li>
# </ol>
# It's more like works as the Probability Density Function (PDF) but it can give the probability of the whole sample (where, sample size>1).
# 
# It is also called as <b> Deterministic Approximate Inference Method.</b> 

# <b> What is Likelihhood Function ?</b>
# 
# Likelihood Function is also a Probability Density Function (PDF) which tells the probability of occurance of particular values in a sample.
# 
# Likelihood Function denoted as the <b> L()</b> .
# <br>
# <br>
# <b> Let's find out the Minimum Variance and Unbaised Estimator (MVU) using the Maximum Likelihood Estimate (MLE) Method for the Normal/Gaussian Distribution. </b>
# <br>
# <br>
# \begin{equation}
#  L() = P(X_{1} = x_{1} \cap X_{2} = x_{2} \cap X_{3} = x_{3} \cap X_{4} = x_{4} \cap X_{5} = x_{5} \cap X_{6} = x_{6}) 
# \end{equation}
# <br>
# In the generalized way,
# <br>
# \begin{equation}
# L() = P(X_{1} = x_{1} \cap X_{2} = x_{2} \cap X_{3} = x_{3}  \cap... X_{n} = x_{n}) 
# \end{equation}
# 
# <br>
# \begin{equation}
# L() = P(X = x_{1}) . P(X = x_{2}) . ... P(X = x_{n})  
# \end{equation}
# <br>
# <br>
# So,<br>
# \begin{equation}
# L() = \frac{1}{\sqrt{2\pi}(\sigma^{\wedge})} \mathrm{e}^{\frac{-(x_{1}-(\mu^{\wedge}))^2}{2(\sigma^{\wedge})^2}}  \frac{1}{\sqrt{2\pi}(\sigma^{\wedge})} \mathrm{e}^{\frac{-(x_{2}-(\mu^{\wedge}))^2}{2(\sigma^{\wedge})^2}}...\frac{1}{\sqrt{2\pi}(\sigma^{\wedge})} \mathrm{e}^{\frac{-(x_{n}-(\mu^{\wedge}))^2}{2(\sigma^{\wedge})^2}}\
# \end{equation}
# <br>
# $\sigma, \mu$= are unknown and we will estimate then so we will use cap $(\wedge)$ on above natural parameters so,  $\sigma^{\wedge} , \mu^{\wedge}$
# <br>
# <br>
# It is independent samples so we have multiplied them and it is distributed identically so, $\sigma^{\wedge} , \mu^{\wedge}$ are same.
# <br>
# \begin{equation}
# L(\sigma^{\wedge} , \mu^{\wedge}) = \frac{1}{\sqrt{2\pi}(\sigma^{\wedge})} \mathrm{e}^{\frac{-\sum_{i=1}^{N}(x_{i}-(\mu^{\wedge}))^2}{2(\sigma^{\wedge})^2}}\
# \end{equation}
# <br>
# It is a Likelihood Function for the two variables ($\sigma^{\wedge} , \mu^{\wedge}$).
# <br>
# Now, we want to find such values of $\sigma $ and $\mu$ such that $L(\sigma^{\wedge} , \mu^{\wedge})$ reaches its maximum values.
# <br>
# <br>
# We need to perform following things before applying it:
# <ol>
#     <li> For the smoothing of the function, we will use Log function. </li>
#     <li> For the reversal of the non-convex function graph, we will use the negative (-) sign. It will provide the global maximum. </li>
# </ol>
# <br>
# 
# After all the alteration in the whole function the final equation of the function is:
# <br>
# <br>
# \begin{equation}
# -log\ L(\sigma^{\wedge} , \mu^{\wedge})] = -log \frac{1}{\sqrt{2\pi}(\sigma^{\wedge})} \mathrm{e}^{\frac{-\sum_{i=1}^{N}(x_{i}-(\mu^{\wedge}))^2}{2(\sigma^{\wedge})^2}}
# \end{equation}
# <br>
# <br>
# We will simplify the equative to find the natural parameters functions.
# <br>
# 
# \begin{equation}
# = -log_{e} \frac{1}{\sqrt{2\pi}(\sigma^{\wedge})}^N + log_{e}\mathrm{e}^{\frac{-\sum_{i=1}^{N}(x_{i}-(\mu^{\wedge}))^2}{2(\sigma^{\wedge})^2}}\,
# \end{equation}
# <br>
# <br>
# \begin{equation}
# = -(-N \log_{e} (\sqrt{2\pi}(\sigma^{\wedge})) - {\frac{-\sum_{i=1}^{N}(x_{i}-(\mu^{\wedge}))^2}{2(\sigma^{\wedge})^2}})
# \end{equation}
# <br>
# <br>
# \begin{equation}
# -log_{e}(L(\sigma^{\wedge} , \mu^{\wedge}))= (N \log_{e} (\sqrt{2\pi}(\sigma^{\wedge}))) + {\frac{-\sum_{i=1}^{N}(x_{i}-(\mu^{\wedge}))^2}{2(\sigma^{\wedge})^2}}
# \end{equation}
# <br>
# <br>
# we will use the partial derivation to solve the equation further on.
# <br>
# \begin{equation}
# = \frac{\delta}{\delta \mu^{\wedge}}(N \log_{e} (\sqrt{2\pi}(\sigma^{\wedge}))) + {\frac{-\sum_{i=1}^{N}(x_{i}-(\mu^{\wedge}))^2}{2(\sigma^{\wedge})^2}}
# \end{equation}
# <br>
# <br>
# \begin{equation}
# \mu^{\wedge}_{ML} = \frac{\sum_{i=1}^{N} (x_{i})}{N}
# \end{equation}
# <br>
# <br>
# \begin{equation}
# \sigma^{\wedge^2}_{ML} = \frac{\sum_{i=1}^{N} (x_{i}-\mu^{\wedge})^2}{N}
# \end{equation}
# 
