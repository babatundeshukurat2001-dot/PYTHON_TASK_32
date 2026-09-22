population = 8_300_000_000
growth_rate = 0.008

print(f"{'Year':>5} {'Population':>20} {'Increase':>20}")

original_population = population

for year in range(1, 101):

    increase = population * growth_rate
    population += increase

    print(f"{year:>5} {population:>20,.0f} {increase:>20,.0f}")

    if population >= original_population * 2:
        print(f"Population doubled by year {year}")
        break
