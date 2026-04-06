# Mars evolution over time
from scoring import habitability_score
import matplotlib.pyplot as plt

mars_timeline = [
    {
        "time" : "4B years ago",
        "temperature" : 20,
        "oxygen" : 5,
        "co2" : 20,
        "water" : 0.9,
        "magnetic_field" : 0.9,
        "gravity" : 3.7
    },
    {
        "time" : "3B years ago",
        "temperature" : 10,
        "oxygen" : 3,
        "co2" : 40,
        "water" : 0.7,
        "magnetic_field" : 0.7,
        "gravity" : 3.7
    },
    {
        "time" : "2B years ago",
        "temperature" : -10,
        "oxygen" : 1,
        "co2" : 70,
        "water" : 0.4,
        "magnetic_field" : 0.3,
        "gravity" : 3.7
    },
    {
        "time" : "Present",
        "temperature" : -60,
        "oxygen" : 0.13, 
        "co2" : 95,
        "water" : 0.2,
        "magnetic_field" : 0.1,
        "gravity" : 3.7
    }
]

def simulate_mars_evolution():
    results = []

    for stage in mars_timeline:
        score, _ = habitability_score(stage)
        results.append((stage["time"], score))

    return results

def plot_evolution(results):
    times = list(r[0] for r in results)
    scores = list(r[1] for r in results)

    plt.figure()

    plt.plot(times, scores, marker='o')

    plt.title("Mars Habitability Over Time")
    plt.xlabel("Time")
    plt.ylabel("Habitability Score")

    plt.ylim(0, 12)

    for i,v in enumerate(scores):
        plt.text(i, v + 0.2, str(v), ha="center")

    plt.show()
