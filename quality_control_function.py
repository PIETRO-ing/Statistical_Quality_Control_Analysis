import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import norm
from scipy.stats import t

def quality_control_analysis(**kwargs):
    
    # Default Parameters
    mu = kwargs.get(mu, 50)
    sigma = kwargs.get(sigma, 0.5)
    x_val = kwargs.get(x_val, 51.5)
    x_lower = kwargs.get(x_lower, 49)
    x_upper = kwargs.get(x_upper, 51)
    n = kwargs.get(n, 25)                      # sample size
    x_bar = kwargs.get(x_bar, 50.1)            # sample mean
    confidence = kwargs.get(confidence, 0.95)  # confidence level
    s = kwargs.get(s, 0.52 )                   # sample standard deviation

    
