def get_winner(players):
    player1 = players.get(1)
    player2 = players.get(2)
    winner = None
    loser = None
    slovo = ''
    if player1 == 'makaze':
        if player2 == 'papir':
            winner = 1
            loser = 2
            slovo += 'u'
        elif player2 == 'kamen':
            winner = 2
            loser = 1
            slovo += 'e'
    elif player1 == 'papir':
        if player2 == 'kamen':
            winner = 1
            loser = 2
            slovo += 'e'
        elif player2 == 'makaze':
            winner = 2
            loser = 1
            slovo += 'u'
    else:
        if player2 == 'makaze':
            winner = 1
            loser = 2
            slovo += 'e'
        elif player2 == 'papir':
            winner = 2
            loser = 1
            slovo += 'e'
    if not winner:
        print(f'Nerešeno jer su oba igrača izabrala {player1}')
    else:
        win_str = None
        if winner == 1:
            win_str = 'prvi'
        else:
            win_str = 'drugi'
        print(f'Pobedio je {win_str} jer {players.get(winner)} pobeđuj{slovo} {players.get(loser)}')


if __name__ == '__main__':
    game_on = True
    players = {1: '', 2: ''}
    p1, p2 = None, None
    while True:

        while True:
            p1 = input('Prvi igrač bira: ').casefold().strip(' ')
            if p1 != 'kamen' and p1 != 'papir' and p1 != 'makaze':
                if p1 == 'predaja':
                    game_on = False
                    break
                print(
                    "Nevalidan unos. Probajte sa: kamen, papir ili makaze (ili 'predaja' ako hoćete da odustanete D: )")
                continue
            break

        if not game_on:
            break

        while True:
            p2 = input('Drugi igrač bira: ').casefold().strip(' ')
            if p2 != 'kamen' and p2 != 'papir' and p2 != 'makaze':
                if p2 == 'predaja':
                    game_on = False
                    break
                print(
                    "Nevalidan unos. Probajte sa: kamen, papir ili makaze (ili 'predaja' ako hoćete da odustanete D: )")
                continue
            break

        if not game_on:
            break

        players[1] = p1
        players[2] = p2

        get_winner(players)

    print('Kraj igre!')
