# 05.Uma pista de Kart permite 5 voltas para cada um de 5 corredores. Escreva um programa que leia o nome do corredor e todos os seus tempos em segundos e os guarde em um dicionário, onde a chave é o nome do corredor e os valores são os tempos armazenados na forma de lista. Veja o exemplo:
# {
# 'João': [77.0, 77.3, 73.9, 77.1, 75.9],
# 'Maria': [79.2, 78.0, 78.5, 73.5, 78.9],
# 'Pedro': [79.1, 75.8, 76.5, 73.5, 79.2],
# 'Ana': [73.4, 75.2, 78.9, 76.5, 73.0],
# 'Carlos': [74.5, 79.1, 73.2, 76.6, 73.5]
# }

from operator import itemgetter

def registerTimes():
    runners_times = {}

    for _ in range(5):  # For each of the 5 runners
        runner_name = input().strip()
        times = []

        for lap in range(5):  # 5 laps for each runner
            time = float(input())
            times.append(time)

        runners_times[runner_name] = times

    return runners_times

def calculate_ranking(runners_times):
    ranking = []

    for runner, times in runners_times.items():
        total_time = round(sum(times), 1)
        average_time = round(sum(times) / len(times), 1)
        best_lap = round(min(times), 1)
        ranking.append((runner, total_time, average_time, best_lap))

    ranking.sort(key=itemgetter(1))  # Sort by total time

    return ranking

def show_ranking(ranking):
    print("-------|------------------|-------------|-------------|--------------")
    print(f"{'Ordem':^7}|{'Nome do Corredor':^18}|{'Tempo Total':^13}|{'Tempo Médio':^13}|{'Melhor Volta':^14}")
    print("-------|------------------|-------------|-------------|--------------")

    for order, (runner, total_time, average_time, best_lap) in enumerate(ranking, start=1):
        print(f"{order:^7}|{runner:^18}|{total_time:^13}|{average_time:^13}|{best_lap:^14}")

    print("-------|------------------|-------------|-------------|--------------")

def main():
    # Register runners' times
    runners_times = registerTimes()

    # Calculate ranking and show results
    ranking = calculate_ranking(runners_times)
    show_ranking(ranking)

if __name__ == "__main__":
    main()