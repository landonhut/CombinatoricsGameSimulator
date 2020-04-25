from Game import *


num_vertices = 5
num_trials = 1000





def play_game(game):
    while game.graph.adj_list:
##        print(game.graph.adj_list)
        edge = game.make_choice(True)
##        print("{} removed {} - {}".format(game.turn.ident, edge[0], edge[1]))
        point_awarded = game.remove_bar(game.turn, edge[0], edge[1])
        if not (game.extra_turn and point_awarded):
            game.change_turns()
    
    if game.player1.score > game.player2.score:
        return game.player1.ident
    elif game.player1.score < game.player2.score:
        return game.player2.ident
    else:
        return 0






player1_wins = 0
player2_wins = 0
ties = 0
for i in range(num_trials):
    game = Game(num_vertices, False)
    game.graph.make_clique_graph()
    winner = play_game(game)
    if winner == game.player1.ident:
        player1_wins += 1
    elif winner == game.player2.ident:
        player2_wins += 1
    else:
        ties += 1

print("Player 1 Wins: {}".format(player1_wins))
print("Player 2 Wins: {}".format(player2_wins))
print("Ties: {}".format(ties))
