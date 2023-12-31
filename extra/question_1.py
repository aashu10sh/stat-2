from typing import List, Tuple
import numpy as np
from numpy.typing import NDArray
import matplotlib.pyplot as plt


class DrunkenWalk:
    def __init__(self, steps: int, simulations: int) -> None:
        self.steps = steps
        self.simulations = simulations

        self.total_distances: List[Tuple[float, float]] = []
        self.max: List[float] = []
        self.average: List[float] = []

    def simulate_walk(self) -> Tuple[NDArray[np.float64], NDArray[np.float64]]:
        initial_x = np.zeros(self.steps)
        initial_y = np.zeros(self.steps)

        for i in range(0, self.steps):
            angle: float = np.random.uniform(0, 2 * np.pi)
            # angle = angle / 360 * 10
            initial_x[i] = initial_x[i - 1] + np.cos(angle)
            initial_y[i] = initial_y[i - 1] + np.sin(angle)

        return (initial_x, initial_y)

    def calculate_distance(
        self, x_distances: NDArray[np.float64], y_distances: NDArray[np.float64]
    ) -> Tuple[float, float]:
        total_distance = np.sqrt(x_distances**2 + y_distances**2)
        average = np.average(total_distance)
        max = np.max(total_distance)
        self.average.append(average)
        self.max.append(max)

        return (average, max)

    @classmethod
    def main(cls, steps: int = 1000, simulations: int = 1000):
        drunk_boy = DrunkenWalk(steps=steps, simulations=simulations)
        for i in range(simulations):
            x, y = drunk_boy.simulate_walk()
            average, max = drunk_boy.calculate_distance(x, y)
            drunk_boy.total_distances.append((average, max))
            if i == 0:
                plt.plot(x, y, label="Drunken Walk")

        plt.title("Drunken Walk Simulation")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.legend()
        plt.show()

        average = np.average(drunk_boy.average)
        max = np.max(drunk_boy.max)

        print(f"The Average is {average}")
        print(f"The Max is {max}")


if __name__ == "__main__":
    DrunkenWalk.main()
