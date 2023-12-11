# 05.Uma pista de Kart permite 5 voltas para cada um de 5 corredores. Escreva um programa que leia o nome do corredor e todos os seus tempos em segundos e os guarde em um dicionário, onde a chave é o nome do corredor e os valores são os tempos armazenados na forma de lista. Veja o exemplo:
# {
# 'João': [77.0, 77.3, 73.9, 77.1, 75.9],
# 'Maria': [79.2, 78.0, 78.5, 73.5, 78.9],
# 'Pedro': [79.1, 75.8, 76.5, 73.5, 79.2],
# 'Ana': [73.4, 75.2, 78.9, 76.5, 73.0],
# 'Carlos': [74.5, 79.1, 73.2, 76.6, 73.5]
# }

from operator import itemgetter  # Importing itemgetter from the operator module

# Function to register lap times for five runners
def registerTimes():
    runners_times = {}  # Initialize an empty dictionary to store runner names and their lap times

    for _ in range(5):  # For each of the 5 runners
        runner_name = input("Nome do corredor: ").strip()  # Input the name of the runner
        times = []

        for lap in range(5):  # Input lap times for each runner
            time = float(input("Tempo da volta (em segundos): "))  # Input the lap time for a specific lap
            times.append(time)  # Add the lap time to the list of times for the current runner

        runners_times[runner_name] = times  # Store the list of lap times for the runner

    return runners_times  # Return the dictionary containing all runner names and their lap times

# Function to calculate rankings based on lap times
def calculate_ranking(runners_times):
    ranking = []  # Initialize an empty list to store rankings

    # Calculate statistics for each runner and add them to the ranking list
    for runner, times in runners_times.items():
        total_time = round(sum(times), 1)  # Calculate total time for all laps of a runner
        average_time = round(sum(times) / len(times), 1)  # Calculate average time per lap for a runner
        best_lap = round(min(times), 1)  # Find the best (minimum) lap time for a runner
        ranking.append((runner, total_time, average_time, best_lap))  # Add runner statistics to the ranking list

    ranking.sort(key=itemgetter(1))  # Sort the ranking list by total time using itemgetter

    return ranking  # Return the sorted ranking list

def show_ranking(ranking):
    print("-------|------------------|-------------|-------------|--------------")
    print(f"{'Ordem':^7}|{'Nome do Corredor':^18}|{'Tempo Total':^13}|{'Tempo Médio':^13}|{'Melhor Volta':^14}")
    print("-------|------------------|-------------|-------------|--------------")

    for order, (runner, total_time, average_time, best_lap) in enumerate(ranking, start=1):
        print(f"{order:^7}|{runner:^18}|{total_time:^13}|{average_time:^13}|{best_lap:^14}")

    print("-------|------------------|-------------|-------------|--------------")

# Main function
def main():
    # Register runners' times
    runners_times = registerTimes()

    # Calculate ranking and show results
    ranking = calculate_ranking(runners_times)
    show_ranking(ranking)

# Execute the main function if this script is executed directly
if __name__ == "__main__":
    main()