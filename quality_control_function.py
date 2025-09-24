import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import norm
from scipy.stats import t

def quality_control_analysis(**kwargs):
    
    # Default Parameters
    mu = kwargs.get("mu", 50)
    sigma = kwargs.get("sigma", 0.5)
    x_val = kwargs.get("x_val", 51.5)
    x_lower = kwargs.get("x_lower", 49)
    x_upper = kwargs.get("x_upper", 51)
    n = kwargs.get("n", 25)                      # sample size
    x_bar = kwargs.get("x_bar", 50.1)            # sample mean
    confidence = kwargs.get("confidence", 0.95)  # confidence level
    s = kwargs.get("s", 0.52 )                   # sample standard deviation

    # Calculate PDF
    pdf_51_5 = norm.pdf(x_val, mu, sigma)
    print(f"PDF value at length {x_val} cm: {pdf_51_5:.5f}\n {pdf_51_5:.5f} is a very low value.\n")

    # Calculate z-score
    z_score = (51.5 - mu) / sigma
    print(f'The z_score is: {z_score}\nWe are {z_score} standard deviation above the mean\n')
 
    # Calculate CDF → p(x ≤ z_score) or p(x ≤ 51.5)
    p_z_score_le = norm.cdf(x_val, mu, sigma)
    p_z_score_le_perc = p_z_score_le * 100
    p_z_score_mo = 1 - p_z_score_le
    p_z_score_mo_perc = p_z_score_mo * 100

    print(f"The probability that a rod is 51.5 cm or less is: {p_z_score_le_perc:.4f}%")
    print(f"The probability that a rod is 51.5 cm or greater is: {p_z_score_mo_perc:.4f}%")
    print(f"Rods 51.5 cm long they occur {p_z_score_mo_perc:.2f}% only of the distribution, they are quite unusual, and likely a defect.\n")  

    #  Calculte z-score for the bounds
    z_x_upper = (x_upper - mu) / sigma
    z_x_lower = (x_lower - mu) / sigma

    # Probability within ± 1cm
    p_z_x_upper = norm.cdf(z_x_upper)
    p_z_x_lower = norm.cdf(z_x_lower)
    p_within_1cm = p_z_x_upper - p_z_x_lower
    p_within_1cm_perc = p_within_1cm * 100
    print(f"The probability that a randomly selected rod has a length ± 1cm from the mean is: {p_within_1cm_perc:.2f}%\n")


quality_control_analysis()