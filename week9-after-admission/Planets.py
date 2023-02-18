from collections import defaultdict

def find_min_cost(cost_per_orbit, planet_positions):
    min_cost = 0
    orbit_counts = defaultdict(int)

    for orbit in planet_positions:
        orbit_counts[orbit] += 1

    for orbit in orbit_counts:
        num_planets = orbit_counts[orbit]
        if num_planets <= cost_per_orbit:
            min_cost += num_planets
        else:
            min_cost += cost_per_orbit
    return min_cost

def main():
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        [num_orbits, cost_per_orbit] = list(map(int,input().split()))
        planet_positions = list(map(int,input().split()))
        print(find_min_cost(cost_per_orbit, planet_positions))

main()

#20min
#3sub