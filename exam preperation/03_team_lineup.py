def team_lineup(*args):
    from collections import defaultdict

    players_by_country = defaultdict(list)
    for player, country in args:
        players_by_country[country].append(player)

    sorted_countries = sorted(players_by_country.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []
    for country, players in sorted_countries:
        result.append(f"{country}:")
        for player in players:
            result.append(f"  -{player}")

    return "\n".join(result)


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))
