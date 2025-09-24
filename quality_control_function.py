import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import norm
from scipy.stats import t

def probability_analysis(**kwargs):
    
    # Default Parameters
    mu = kwargs.get("mu", 50)
    sigma = kwargs.get("sigma", 0.5)
    x_val = kwargs.get("x_val", 51.5)
    x_lower = kwargs.get("x_lower", 49)
    x_upper = kwargs.get("x_upper", 51)

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

def confidence_interval(**kwargs):
    # Default Parameters
    mu = kwargs.get("mu", 50)
    sigma = kwargs.get("sigma", None)
    x_val = kwargs.get("x_val", 51.5)
    x_lower = kwargs.get("x_lower", 49)
    x_upper = kwargs.get("x_upper", 51)
    n = kwargs.get("n", 25)                      # sample size
    x_bar = kwargs.get("x_bar", 50.1)            # sample mean
    confidence = kwargs.get("confidence", 0.95)  # confidence level
    s = kwargs.get("s", 0.52 )                   # sample standard deviation

    alpha = 1 - confidence

    # Determine whether to use z-distribution or t-distribution
    if sigma is not None and sigma > 0: # z-distribution
    
        SE = sigma / math.sqrt(n)
        critical_value = norm.ppf(1 - alpha/2)
        distribution_type = "Z"

    else: # t-distribution
        df = n - 1
        SE = s / math.sqrt(n)
        critical_value = t.ppf(1 - alpha/2, df)
        distribution_type = 'T'

    # Calculate margin error
    margin_error = critical_value * SE

    # Calculate confidence interval
    CI_lower = x_bar - margin_error
    CI_upper = x_bar + margin_error


    # Print results
    print(f"Using the {distribution_type}-distribution:")
    print(f"Standard Error (SE): {SE:.4f}")
    print(f"Critical value: {critical_value:.4f}")
    print(f"Margin of Error (ME): {margin_error:.4f}")
    print(f"{int(confidence*100)}% Confidence Interval: ({CI_lower:.3f}, {CI_upper:.3f})")
    print(f"We are {int(confidence*100)}% confident that the true mean lies between {CI_lower:.3f} and {CI_upper:.3f}.")

     # Return dictionary for easy plotting
    return {
        "mu": mu,
        "sigma": sigma,
        "x_val": x_val,
        "x_lower": x_lower,
        "x_upper": x_upper,
        "n": n,
        "x_bar": x_bar,
        "confidence": confidence,
        "s": s,
        "SE": SE,
        "critical_value": critical_value,
        "margin_error": margin_error,
        "ci_lower": CI_lower,
        "ci_upper": CI_upper,
        "distribution_type": distribution_type
    }

    
def plot_confidence_interval(results):
    x_bar = results["x_bar"]
    ME = results["margin_error"]
    CI_lower = results["ci_lower"]
    CI_upper = results["ci_upper"]
    SE = results["SE"]
    dist_type = results["distribution_type"]
    confidence = results["confidence"]

    fig, ax = plt.subplots(figsize=(8, 4))

    # Plot error bar for confidence interval around the mean
    ax.errorbar(x_bar, 0, xerr=ME, fmt='o', color='blue', capsize=5, label=f'{int(confidence*100)}% CI')

    # Vertical lines for CI bounds and sample mean
    ax.axvline(CI_lower, color='red', linestyle='--', label='CI Lower Bound')
    ax.axvline(CI_upper, color='green', linestyle='--', label='CI Upper Bound')
    ax.axvline(x_bar, color='black', linestyle='-', label='Sample Mean')

    # Styling
    ax.set_title(f"{int(confidence*100)}% Confidence Interval for Rod Length (σ {'known' if dist_type=='Z' else 'unknown'}, {dist_type}-distribution)")
    ax.set_xlabel("Rod Length (cm)")
    ax.set_yticks([])
    ax.set_xlim(x_bar - 4*SE, x_bar + 4*SE)
    ax.legend()
    plt.grid(axis='x')
    plt.tight_layout()

    # Save and show plot
    plt.savefig(f"ci_plot_{dist_type}_distribution.png")
    #plt.show()


probability_analysis()

results_t = confidence_interval(n=25, x_bar=50.1, s=0.52, sigma=None)  # t-dist case
plot_confidence_interval(results_t)

results_z = confidence_interval(n=25, x_bar=50.1, sigma=0.5)          # z-dist case
plot_confidence_interval(results_z)