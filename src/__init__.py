def contabilizar(ronda,tablaTotal,ronda_scores):
    for jugador, stats in ronda.items():
        kills = stats['kills']
        assists = stats['assists']
        muertes = stats['deaths']   
        puntos = kills * 3 + assists * 1 + (-1 if muertes else 0)
        tablaTotal[jugador]['kills'] += kills
        tablaTotal[jugador]['assists'] += assists
        tablaTotal[jugador]['muertes'] += int(muertes)
        tablaTotal[jugador]['puntos'] += puntos
        
        ronda_scores[jugador] = puntos
        
    max_puntos = max(ronda_scores.values())
    for jugador, puntos in ronda_scores.items():
        if puntos == max_puntos:
            print(f"El MVP de la ronda fue:  {jugador}")
            tablaTotal[jugador]['MVP'] += 1
            break
    print("{:<10} {:<6} {:<10} {:<8} {:<6} {:<7}".format("Jugador", "Kills", "Asistencias", "Muertes", "MVPs", "Puntos"))
    print("-" * 55)
    for jugador, datos in sorted(tablaTotal.items(), key=lambda x: x[1]['puntos'], reverse=True):
        print("{:<10} {:<6} {:<10} {:<8} {:<6} {:<7}".format(
            jugador,
            datos['kills'],
            datos['assists'],
            datos['muertes'],
            datos['MVP'],
            datos['puntos']
        ))