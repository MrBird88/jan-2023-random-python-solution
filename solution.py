def check(n, m, games):
    # Split the games into two vectors representing the two teams e.g. game = [[home], [away]]
    split_games = [[game[:n//2], game[n//2:]] for game in games]

    # Create a dictionary using player names (numbers) as keys and an empty set as a value
    players = {i: set() for i in range(1, n+1)}

    # For every player, go through every game
    for player in players:
        for game in split_games:
            # List of players in the opposing team
            other_team = game[0] if player in game[1] else game[1]

            # Add those players to our player's set
            players[player].update(other_team)

    # Finally, if a player has faced off against each player at least once then the length
    # of their set will equal n - 1 (the total number of players minus themselves).

    # We check if this is true for all players in our dictionary.
    return all(len(players[player]) == n - 1 for player in players)
