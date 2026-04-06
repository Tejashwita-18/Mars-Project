import matplotlib.pyplot as plt
import numpy as np

def plot_scores(mars_score, earth_score, mars_name="Mars"):
    planets = [mars_name, "Earth"]
    scores = [mars_score, earth_score]

    plt.bar(planets, scores)
    plt.title("Habitability Comparison")
    plt.xlabel("Planet")
    plt.ylabel("Score")

    plt.ylim(0, 10)

    for i,v in enumerate(scores):
        plt.text(i, v + 0.2, str(v), ha="center")

    plt.show()

def plot_factor_comparison(mars_details, earth_details, mars_name="Mars"):

    factors = list(mars_details.keys())

    mars_values = [1 if v in ["suitable", "sufficient", "balanced", "available", "protective", "stable"] else 0
                   for v in mars_details.values()]
    
    earth_values = [1 if v in ["suitable", "sufficient", "balanced", "available", "protective", "stable"] else 0
                    for v in earth_details.values()]
    
    # make Mars values visible even if 0
    mars_values = [v if v == 1 else 0.05 for v in mars_values]

    x = np.arange(len(factors))
    width = 0.35

    plt.figure()

    # side-by-side bars
    plt.bar(x - width/2, mars_values, width, label=mars_name)
    plt.bar(x + width/2, earth_values, width, label="Earth")

    plt.xticks(x, factors)
    plt.ylabel("Suitability (1 = Yes, 0 = No)")
    plt.title("Habitability Factor Comparison")

    # add value labels for mars
    for i,v in enumerate(mars_values):
        plt.text(i - width/2, v + 0.02, str(round(v,2)), ha="center")

    # add value labels for earth
    for i,v in enumerate(earth_values):
        plt.text(i + width/2, v + 0.02, str(v), ha="center")

    plt.legend()
    plt.ylim(0, 1.2)
    plt.show()
