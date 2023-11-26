# 4. Um time de basquete possui 12 jogadores. Deseja-se um programa que, dado o nome e a altura dos jogadores, determine:
# a. o nome e a altura do jogador mais alto;
# b. a média de altura do time;
# c. os jogadores com altura superior à média, listando o nome e a altura de cada um.


# Function that returns information about the biggest player among the list of 12 players
def tallestPlayer(players):
    # Initializing variables for the tallest player
    tallestName = ''
    tallestHeight = 0

    # Iterating through the list of players to find the tallest
    for player in players:
        name, height = player
        
        if height > tallestHeight:
            tallestName = name
            tallestHeight = height

    return tallestName, tallestHeight

# Function that calculates the average height of the team
def averageHeight(players):
    totalHeight = 0
    
    # Iterating through the players' heights to calculate the total height
    for player in players:
        totalHeight += player[1]
    
    # Calculating the average height
    average = totalHeight / len(players)

    return average

# Filters players who are above average
def aboveAverage(players, average):
    aboveAveragePlayers = []

    # Iterating through the players to find those with height above the average
    for name, height in players:
        if height > average:
            aboveAveragePlayers.append((name, height))

    return aboveAveragePlayers

# Collects player information
def getPlayersInfo():
    playersList = []

    # Collecting player information (name and height)
    for i in range(12):
        name = input(f"Digite o nome do jogador {i + 1}: ")
        height = float(input(f"Insira a altura de {name}: "))
        # Appending player info to the list
        playersList.append((name, height))  

    return playersList

# Main function
def main():
    # Getting player information
    playersList = getPlayersInfo()

    # Finding the tallest player
    tallest = tallestPlayer(playersList)

    print("JOGADOR MAIS ALTO DO TIME")
    print(f"Nome: {tallest[0]}\nAltura: {tallest[1]:.2f} m\n")

    # Calculating the team's average height
    avg = averageHeight(playersList)

    print("ALTURA MÉDIA DO TIME")
    print(f"{avg:.2f} m\n")

    # Finding players taller than the average height
    aboveAvgPlayers = aboveAverage(playersList, avg)
    
    print("JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME")
    if aboveAvgPlayers:
        for player in aboveAvgPlayers:
            print(f"Nome: {player[0]}\nAltura: {player[1]:.2f} m\n")

# Identify function main for execute
if __name__ == "__main__":
    main()
