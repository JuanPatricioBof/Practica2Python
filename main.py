rounds = [
 {
 'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
 'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
 'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
 'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
 'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
 },
 {
 'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
 'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
 'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
 'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
 'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}
 },
 {
 'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
 'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
 'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
 'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
 'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
 },
 {
 'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
 'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
 'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
 'Frost': {'kills': 1, 'assists': 1, 'deaths': True},
 'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
 },
 {
 'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
 'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
 'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
 'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
 'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}
 }
 ]
tablaTotal={
    'Shadow': {'kills': 0, 'assists': 0, 'muertes': 0, 'MVP': 0},
 'Blaze': {'kills': 0, 'assists': 0, 'muertes': 0, 'MVP': 0},
 'Viper': {'kills': 0, 'assists': 0, 'muertes': 0, 'MVP': 0},
 'Frost': {'kills': 0, 'assists': 0, 'muertes': 0, 'MVP': 0},
 'Reaper': {'kills': 0, 'assists': 0, 'muertes': 0, 'MVP': 0}
}
for i,ronda in enumerate(rounds, start=1):
    print(f"Ranking Ronda {i}")
    