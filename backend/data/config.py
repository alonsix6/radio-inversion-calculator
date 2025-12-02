"""
Tablas de configuración fijas para el cálculo de inversión en radio.
Actualizar RANKINGS cuando salgan nuevos estudios de CPI.
"""

# CPM por tipo de formato
CPM_CONFIG = {
    "SPOT": 11.6,
    "MENCION": 39.8,
    "P/D": 1.74
}

# Mapeo de tipos IBOPE a tipos agrupados
TIPO_MAPPING = {
    "SPOT": "SPOT",
    "MENCION": "MENCION",
    "DESP.PROGRAMA": "P/D",
    "DESP.SUBPROGRAMA": "P/D",
    "PRES.PROGRAMA": "P/D",
    "PRES.SUBPROGRAMA": "P/D"
}

# Mapeo de mes a mes de ranking más cercano
MES_TO_RANKING = {
    "enero": "Marzo",
    "febrero": "Marzo",
    "marzo": "Marzo",
    "abril": "Junio",
    "mayo": "Junio",
    "junio": "Junio",
    "julio": "Agosto",
    "agosto": "Agosto",
    "septiembre": "Septiembre",
    "octubre": "Noviembre",
    "noviembre": "Noviembre",
    "diciembre": "Noviembre"
}

# Rankings de CPI por Año-Mes-Emisora
# Formato: {(año, mes, emisora): ranking_en_miles}
# ACTUALIZAR cuando salgan nuevos estudios de CPI
RANKINGS = {
    # 2023 - Septiembre
    (2023, "Septiembre", "MODA FM"): 394.0,
    (2023, "Septiembre", "ONDA CERO FM"): 344.8,
    (2023, "Septiembre", "LA ZONA FM"): 292.5,
    (2023, "Septiembre", "RADIO DISNEY FM"): 227.4,
    (2023, "Septiembre", "PLANETA FM"): 205.6,
    (2023, "Septiembre", "OXIGENO FM"): 202.9,
    (2023, "Septiembre", "RITMO ROMANTICA FM"): 185.8,
    (2023, "Septiembre", "STUDIO 92 FM"): 185.6,
    (2023, "Septiembre", "LA KARIBEÑA FM"): 170.3,
    (2023, "Septiembre", "RPP FM"): 165.7,
    (2023, "Septiembre", "OASIS FM"): 154.0,
    (2023, "Septiembre", "NUEVA Q FM"): 128.0,
    (2023, "Septiembre", "PANAMERICANA FM"): 127.7,
    (2023, "Septiembre", "RADIOMAR FM"): 123.2,
    (2023, "Septiembre", "MAGICA FM"): 102.5,
    (2023, "Septiembre", "LA KALLE FM"): 92.8,
    (2023, "Septiembre", "RADIO AMERICA FM"): 92.4,
    (2023, "Septiembre", "CORAZON FM"): 90.9,
    (2023, "Septiembre", "LA INOLVIDABLE FM"): 89.3,
    (2023, "Septiembre", "EXITOSA FM"): 79.0,
    (2023, "Septiembre", "RADIO MEGAMIX FM"): 74.0,
    (2023, "Septiembre", "FELICIDAD FM"): 51.7,
    (2023, "Septiembre", "RADIO COMAS FM"): 12.3,
    
    # 2023 - Noviembre
    (2023, "Noviembre", "MODA FM"): 435.5,
    (2023, "Noviembre", "LA ZONA FM"): 340.5,
    (2023, "Noviembre", "ONDA CERO FM"): 308.3,
    (2023, "Noviembre", "RADIO DISNEY FM"): 286.5,
    (2023, "Noviembre", "OXIGENO FM"): 239.4,
    (2023, "Noviembre", "PLANETA FM"): 227.0,
    (2023, "Noviembre", "LA KARIBEÑA FM"): 214.8,
    (2023, "Noviembre", "NUEVA Q FM"): 212.5,
    (2023, "Noviembre", "RITMO ROMANTICA FM"): 194.5,
    (2023, "Noviembre", "PANAMERICANA FM"): 193.5,
    (2023, "Noviembre", "RADIO MEGAMIX FM"): 188.1,
    (2023, "Noviembre", "OASIS FM"): 170.7,
    (2023, "Noviembre", "CORAZON FM"): 167.5,
    (2023, "Noviembre", "STUDIO 92 FM"): 135.6,
    (2023, "Noviembre", "RADIOMAR FM"): 123.3,
    (2023, "Noviembre", "RPP FM"): 109.3,
    (2023, "Noviembre", "LA INOLVIDABLE FM"): 94.8,
    (2023, "Noviembre", "LA KALLE FM"): 92.7,
    (2023, "Noviembre", "FELICIDAD FM"): 70.8,
    (2023, "Noviembre", "MAGICA FM"): 68.3,
    (2023, "Noviembre", "EXITOSA FM"): 49.3,
    (2023, "Noviembre", "RADIO COMAS FM"): 30.5,
    
    # 2024 - Marzo
    (2024, "Marzo", "MODA FM"): 460.7,
    (2024, "Marzo", "ONDA CERO FM"): 342.0,
    (2024, "Marzo", "LA ZONA FM"): 282.6,
    (2024, "Marzo", "NUEVA Q FM"): 258.4,
    (2024, "Marzo", "RITMO ROMANTICA FM"): 194.6,
    (2024, "Marzo", "OXIGENO FM"): 190.5,
    (2024, "Marzo", "RADIO DISNEY FM"): 186.4,
    (2024, "Marzo", "PLANETA FM"): 185.7,
    (2024, "Marzo", "LA KARIBEÑA FM"): 174.0,
    (2024, "Marzo", "PANAMERICANA FM"): 158.9,
    (2024, "Marzo", "RADIOMAR FM"): 144.2,
    (2024, "Marzo", "RADIO MEGAMIX FM"): 141.1,
    (2024, "Marzo", "RPP FM"): 131.9,
    (2024, "Marzo", "STUDIO 92 FM"): 121.2,
    (2024, "Marzo", "CORAZON FM"): 109.7,
    (2024, "Marzo", "LA INOLVIDABLE FM"): 83.0,
    (2024, "Marzo", "EXITOSA FM"): 73.8,
    (2024, "Marzo", "MAGICA FM"): 62.4,
    (2024, "Marzo", "FELICIDAD FM"): 61.1,
    (2024, "Marzo", "LA KALLE FM"): 55.0,
    (2024, "Marzo", "RADIO COMAS FM"): 22.5,
    (2024, "Marzo", "NACIONAL FM"): 6.3,
    (2024, "Marzo", "INCA FM"): 4.2,
    
    # 2024 - Junio
    (2024, "Junio", "MODA FM"): 397.5,
    (2024, "Junio", "LA ZONA FM"): 335.7,
    (2024, "Junio", "ONDA CERO FM"): 304.1,
    (2024, "Junio", "RADIO DISNEY FM"): 229.7,
    (2024, "Junio", "RITMO ROMANTICA FM"): 223.0,
    (2024, "Junio", "PLANETA FM"): 210.9,
    (2024, "Junio", "OXIGENO FM"): 184.1,
    (2024, "Junio", "PANAMERICANA FM"): 165.4,
    (2024, "Junio", "STUDIO 92 FM"): 162.8,
    (2024, "Junio", "NUEVA Q FM"): 161.1,
    (2024, "Junio", "LA KARIBEÑA FM"): 160.5,
    (2024, "Junio", "RPP FM"): 141.5,
    (2024, "Junio", "CORAZON FM"): 126.6,
    (2024, "Junio", "RADIO MEGAMIX FM"): 116.4,
    (2024, "Junio", "MAGICA FM"): 93.5,
    (2024, "Junio", "LA KALLE FM"): 85.8,
    (2024, "Junio", "RADIOMAR FM"): 84.2,
    (2024, "Junio", "LA INOLVIDABLE FM"): 83.7,
    (2024, "Junio", "EXITOSA FM"): 81.8,
    (2024, "Junio", "FELICIDAD FM"): 70.8,
    (2024, "Junio", "RADIO COMAS FM"): 25.0,
    (2024, "Junio", "NACIONAL FM"): 4.6,
    (2024, "Junio", "INCA FM"): 4.6,
    
    # 2024 - Agosto
    (2024, "Agosto", "MODA FM"): 400.0,
    (2024, "Agosto", "LA ZONA FM"): 313.3,
    (2024, "Agosto", "ONDA CERO FM"): 293.0,
    (2024, "Agosto", "RITMO ROMANTICA FM"): 228.9,
    (2024, "Agosto", "RADIO DISNEY FM"): 214.1,
    (2024, "Agosto", "PLANETA FM"): 211.8,
    (2024, "Agosto", "OXIGENO FM"): 192.0,
    (2024, "Agosto", "NUEVA Q FM"): 190.0,
    (2024, "Agosto", "PANAMERICANA FM"): 189.6,
    (2024, "Agosto", "RPP FM"): 160.4,
    (2024, "Agosto", "LA KARIBEÑA FM"): 148.4,
    (2024, "Agosto", "RADIOMAR FM"): 145.9,
    (2024, "Agosto", "RADIO MEGAMIX FM"): 128.4,
    (2024, "Agosto", "STUDIO 92 FM"): 121.2,
    (2024, "Agosto", "EXITOSA FM"): 113.8,
    (2024, "Agosto", "LA INOLVIDABLE FM"): 112.0,
    (2024, "Agosto", "MAGICA FM"): 111.8,
    (2024, "Agosto", "FELICIDAD FM"): 103.1,
    (2024, "Agosto", "CORAZON FM"): 95.4,
    (2024, "Agosto", "LA KALLE FM"): 82.6,
    (2024, "Agosto", "RADIO COMAS FM"): 18.8,
    (2024, "Agosto", "NACIONAL FM"): 6.7,
    (2024, "Agosto", "INCA FM"): 3.7,
    (2024, "Agosto", "CANTO GRANDE FM"): 3.7,
    
    # 2024 - Noviembre
    (2024, "Noviembre", "MODA FM"): 385.1,
    (2024, "Noviembre", "ONDA CERO FM"): 304.9,
    (2024, "Noviembre", "LA ZONA FM"): 280.2,
    (2024, "Noviembre", "RADIO DISNEY FM"): 236.1,
    (2024, "Noviembre", "PLANETA FM"): 234.6,
    (2024, "Noviembre", "RITMO ROMANTICA FM"): 219.0,
    (2024, "Noviembre", "OXIGENO FM"): 206.9,
    (2024, "Noviembre", "NUEVA Q FM"): 189.2,
    (2024, "Noviembre", "RPP FM"): 183.9,
    (2024, "Noviembre", "LA KARIBEÑA FM"): 182.5,
    (2024, "Noviembre", "STUDIO 92 FM"): 151.8,
    (2024, "Noviembre", "PANAMERICANA FM"): 133.5,
    (2024, "Noviembre", "RADIOMAR FM"): 123.0,
    (2024, "Noviembre", "EXITOSA FM"): 104.6,
    (2024, "Noviembre", "RADIO MEGAMIX FM"): 99.7,
    (2024, "Noviembre", "CORAZON FM"): 96.4,
    (2024, "Noviembre", "MAGICA FM"): 91.6,
    (2024, "Noviembre", "LA INOLVIDABLE FM"): 82.1,
    (2024, "Noviembre", "FELICIDAD FM"): 60.0,
    (2024, "Noviembre", "LA KALLE FM"): 54.2,
    (2024, "Noviembre", "INCA FM"): 14.4,
    (2024, "Noviembre", "RADIO COMAS FM"): 12.5,
    (2024, "Noviembre", "NACIONAL FM"): 8.9,
    (2024, "Noviembre", "CANTO GRANDE FM"): 4.8,
    
    # 2025 - Marzo
    (2025, "Marzo", "MODA FM"): 373.2,
    (2025, "Marzo", "ONDA CERO FM"): 274.7,
    (2025, "Marzo", "LA ZONA FM"): 259.4,
    (2025, "Marzo", "RADIO DISNEY FM"): 228.3,
    (2025, "Marzo", "NUEVA Q FM"): 224.7,
    (2025, "Marzo", "PLANETA FM"): 181.3,
    (2025, "Marzo", "OXIGENO FM"): 176.2,
    (2025, "Marzo", "PANAMERICANA FM"): 173.2,
    (2025, "Marzo", "RADIOMAR FM"): 171.5,
    (2025, "Marzo", "LA KARIBEÑA FM"): 144.6,
    (2025, "Marzo", "RITMO ROMANTICA FM"): 137.5,
    (2025, "Marzo", "STUDIO 92 FM"): 135.9,
    (2025, "Marzo", "RPP FM"): 130.0,
    (2025, "Marzo", "CORAZON FM"): 105.4,
    (2025, "Marzo", "MAGICA FM"): 95.2,
    (2025, "Marzo", "RADIO MEGAMIX FM"): 87.0,
    (2025, "Marzo", "LA KALLE FM"): 79.9,
    (2025, "Marzo", "FELICIDAD FM"): 72.8,
    (2025, "Marzo", "LA INOLVIDABLE FM"): 70.7,
    (2025, "Marzo", "EXITOSA FM"): 49.5,
    (2025, "Marzo", "RADIO COMAS FM"): 24.2,
    (2025, "Marzo", "CANTO GRANDE FM"): 11.9,
    (2025, "Marzo", "NACIONAL FM"): 7.8,
    (2025, "Marzo", "BETHEL RADIO FM"): 6.9,
    
    # 2025 - Junio
    (2025, "Junio", "MODA FM"): 357.6,
    (2025, "Junio", "ONDA CERO FM"): 305.7,
    (2025, "Junio", "LA ZONA FM"): 251.9,
    (2025, "Junio", "NUEVA Q FM"): 224.0,
    (2025, "Junio", "RADIO DISNEY FM"): 212.2,
    (2025, "Junio", "PLANETA FM"): 208.1,
    (2025, "Junio", "OXIGENO FM"): 203.6,
    (2025, "Junio", "PANAMERICANA FM"): 190.6,
    (2025, "Junio", "RITMO ROMANTICA FM"): 181.2,
    (2025, "Junio", "RPP FM"): 175.7,
    (2025, "Junio", "LA KARIBEÑA FM"): 173.7,
    (2025, "Junio", "STUDIO 92 FM"): 146.8,
    (2025, "Junio", "CORAZON FM"): 143.7,
    (2025, "Junio", "RADIOMAR FM"): 135.6,
    (2025, "Junio", "EXITOSA FM"): 129.2,
    (2025, "Junio", "RADIO MEGAMIX FM"): 119.5,
    (2025, "Junio", "MAGICA FM"): 115.8,
    (2025, "Junio", "LA KALLE FM"): 114.0,
    (2025, "Junio", "LA INOLVIDABLE FM"): 89.0,
    (2025, "Junio", "FELICIDAD FM"): 75.2,
    (2025, "Junio", "CANTO GRANDE FM"): 25.9,
    (2025, "Junio", "RADIO COMAS FM"): 13.5,
    (2025, "Junio", "NACIONAL FM"): 7.8,
    (2025, "Junio", "BETHEL RADIO FM"): 5.5,
    
    # 2025 - Agosto
    (2025, "Agosto", "MODA FM"): 374.8,
    (2025, "Agosto", "ONDA CERO FM"): 292.5,
    (2025, "Agosto", "LA ZONA FM"): 231.0,
    (2025, "Agosto", "LA KARIBEÑA FM"): 220.9,
    (2025, "Agosto", "NUEVA Q FM"): 206.6,
    (2025, "Agosto", "OXIGENO FM"): 190.8,
    (2025, "Agosto", "RADIO DISNEY FM"): 185.6,
    (2025, "Agosto", "RPP FM"): 179.4,
    (2025, "Agosto", "PLANETA FM"): 179.1,
    (2025, "Agosto", "PANAMERICANA FM"): 170.4,
    (2025, "Agosto", "RADIOMAR FM"): 155.6,
    (2025, "Agosto", "STUDIO 92 FM"): 142.6,
    (2025, "Agosto", "RITMO ROMANTICA FM"): 140.2,
    (2025, "Agosto", "RADIO MEGAMIX FM"): 136.7,
    (2025, "Agosto", "CORAZON FM"): 125.8,
    (2025, "Agosto", "EXITOSA FM"): 104.5,
    (2025, "Agosto", "MAGICA FM"): 97.4,
    (2025, "Agosto", "LA KALLE FM"): 91.0,
    (2025, "Agosto", "LA INOLVIDABLE FM"): 67.8,
    (2025, "Agosto", "FELICIDAD FM"): 57.8,
    (2025, "Agosto", "RADIO COMAS FM"): 18.5,
    (2025, "Agosto", "CANTO GRANDE FM"): 18.4,
    (2025, "Agosto", "BETHEL RADIO FM"): 16.5,
    (2025, "Agosto", "NACIONAL FM"): 4.0,
    (2025, "Agosto", "RADIO DEL SUR FM"): 2.4,
    
    # 2025 - Noviembre
    (2025, "Noviembre", "MODA FM"): 295.4,
    (2025, "Noviembre", "NUEVA Q FM"): 234.5,
    (2025, "Noviembre", "ONDA CERO FM"): 232.2,
    (2025, "Noviembre", "LA ZONA FM"): 205.9,
    (2025, "Noviembre", "RADIO DISNEY FM"): 200.3,
    (2025, "Noviembre", "OXIGENO FM"): 188.6,
    (2025, "Noviembre", "PLANETA FM"): 178.9,
    (2025, "Noviembre", "LA KARIBEÑA FM"): 177.1,
    (2025, "Noviembre", "RPP FM"): 167.3,
    (2025, "Noviembre", "STUDIO 92 FM"): 157.1,
    (2025, "Noviembre", "RITMO ROMANTICA FM"): 148.4,
    (2025, "Noviembre", "CORAZON FM"): 129.8,
    (2025, "Noviembre", "RADIOMAR FM"): 127.4,
    (2025, "Noviembre", "RADIO MEGAMIX FM"): 120.5,
    (2025, "Noviembre", "PANAMERICANA FM"): 117.0,
    (2025, "Noviembre", "LA KALLE FM"): 87.8,
    (2025, "Noviembre", "EXITOSA FM"): 87.8,
    (2025, "Noviembre", "MAGICA FM"): 76.0,
    (2025, "Noviembre", "LA INOLVIDABLE FM"): 75.5,
    (2025, "Noviembre", "FELICIDAD FM"): 58.1,
    (2025, "Noviembre", "CANTO GRANDE FM"): 12.5,
    (2025, "Noviembre", "BETHEL RADIO FM"): 9.9,
    (2025, "Noviembre", "RADIO COMAS FM"): 6.5,
    (2025, "Noviembre", "RADIO DEL SUR FM"): 3.4,
}

# Orden de meses para calcular distancia
MES_ORDEN = {
    "Marzo": 3,
    "Junio": 6,
    "Agosto": 8,
    "Septiembre": 9,
    "Noviembre": 11
}

def get_ranking(año: int, mes: str, emisora: str) -> float:
    """
    Obtiene el ranking para una combinación año-mes-emisora.
    Estrategia de fallback:
    1. Buscar mes exacto
    2. Buscar los dos meses más cercanos del mismo año y promediar
    3. Si solo hay un mes en el año, usar ese
    4. Buscar promedio histórico de la emisora en todos los años
    """
    key = (año, mes, emisora)
    if key in RANKINGS:
        return RANKINGS[key]

    # Obtener todos los meses disponibles para esta emisora en este año
    meses_disponibles = [
        (m, RANKINGS[(a, m, e)])
        for (a, m, e) in RANKINGS.keys()
        if a == año and e == emisora
    ]

    if meses_disponibles:
        # Calcular distancia de cada mes disponible al mes buscado
        mes_num = MES_ORDEN.get(mes, 6)  # Default a Junio si no está en el mapeo

        meses_con_distancia = []
        for m, ranking in meses_disponibles:
            m_num = MES_ORDEN.get(m, 6)
            distancia = abs(mes_num - m_num)
            meses_con_distancia.append((distancia, m, ranking))

        # Ordenar por distancia
        meses_con_distancia.sort(key=lambda x: x[0])

        if len(meses_con_distancia) >= 2:
            # Promedio de los dos meses más cercanos
            ranking1 = meses_con_distancia[0][2]
            ranking2 = meses_con_distancia[1][2]
            return (ranking1 + ranking2) / 2
        else:
            # Solo hay un mes disponible, usar ese
            return meses_con_distancia[0][2]

    # Si no hay data del año, buscar promedio histórico de la emisora
    all_rankings = [v for (a, m, e), v in RANKINGS.items() if e == emisora]
    if all_rankings:
        return sum(all_rankings) / len(all_rankings)

    return 0.0
