"""
Tablas de configuración fijas para el cálculo de inversión en radio.
Rankings basados en IMPACTOS POR RANGO DE HORAS (no Audiencia Acumulada).
Valores en miles (ej: 20.4 = 20,400 personas por hora).
CPM calibrados con Plan de Medios 2024 de UPN.
"""

# CPM calibrados con Plan 2024 (incluyen efecto de auspicios)
# Ratio SPOT:MENCION:P/D = 1:6.17:15.38
CPM_CONFIG = {
    "SPOT": 19.26,
    "MENCION": 118.82,
    "P/D": 296.17
}

# Mapeo de tipos IBOPE a tipos agrupados (sin cambios)
TIPO_MAPPING = {
    "SPOT": "SPOT",
    "MENCION": "MENCION",
    "DESP.PROGRAMA": "P/D",
    "DESP.SUBPROGRAMA": "P/D",
    "PRES.PROGRAMA": "P/D",
    "PRES.SUBPROGRAMA": "P/D"
}

# Rankings de CPI por Año-Mes-Emisora
# IMPACTOS POR RANGO DE HORAS (valores correctos: 0-25 miles)
# Formato: {(año, mes, emisora): impactos_en_miles}
RANKINGS = {
    # ===========================================
    # 2023 - SEPTIEMBRE
    # ===========================================
    (2023, "Septiembre", "MODA FM"): 20.4,
    (2023, "Septiembre", "ONDA CERO FM"): 14.6,
    (2023, "Septiembre", "RADIO DISNEY FM"): 13.8,
    (2023, "Septiembre", "LA ZONA FM"): 12.1,
    (2023, "Septiembre", "PLANETA FM"): 9.7,
    (2023, "Septiembre", "OXIGENO FM"): 7.1,
    (2023, "Septiembre", "STUDIO 92 FM"): 7.0,
    (2023, "Septiembre", "OASIS FM"): 6.5,
    (2023, "Septiembre", "NUEVA Q FM"): 6.3,
    (2023, "Septiembre", "RADIO AMERICA FM"): 5.7,
    (2023, "Septiembre", "LA KARIBEÑA FM"): 5.5,
    (2023, "Septiembre", "RADIO MEGAMIX FM"): 5.4,
    (2023, "Septiembre", "RITMO ROMANTICA FM"): 5.3,
    (2023, "Septiembre", "CORAZON FM"): 4.4,
    (2023, "Septiembre", "RPP FM"): 4.4,
    (2023, "Septiembre", "PANAMERICANA FM"): 3.9,
    (2023, "Septiembre", "RADIOMAR FM"): 3.6,
    (2023, "Septiembre", "LA INOLVIDABLE FM"): 3.6,
    (2023, "Septiembre", "LA KALLE FM"): 3.1,
    (2023, "Septiembre", "MAGICA FM"): 2.3,
    (2023, "Septiembre", "FELICIDAD FM"): 1.9,
    (2023, "Septiembre", "EXITOSA FM"): 1.3,
    (2023, "Septiembre", "RADIO COMAS FM"): 0.1,

    # ===========================================
    # 2024 - JULIO
    # ===========================================
    (2024, "Julio", "MODA FM"): 23.9,
    (2024, "Julio", "LA ZONA FM"): 14.8,
    (2024, "Julio", "RADIO DISNEY FM"): 14.4,
    (2024, "Julio", "ONDA CERO FM"): 13.9,
    (2024, "Julio", "PLANETA FM"): 10.6,
    (2024, "Julio", "RITMO ROMANTICA FM"): 8.1,
    (2024, "Julio", "OXIGENO FM"): 7.5,
    (2024, "Julio", "RADIO MEGAMIX FM"): 6.7,
    (2024, "Julio", "NUEVA Q FM"): 5.6,
    (2024, "Julio", "STUDIO 92 FM"): 5.6,
    (2024, "Julio", "CORAZON FM"): 4.7,
    (2024, "Julio", "PANAMERICANA FM"): 4.6,
    (2024, "Julio", "RPP FM"): 4.1,
    (2024, "Julio", "LA KARIBEÑA FM"): 4.1,
    (2024, "Julio", "MAGICA FM"): 3.7,
    (2024, "Julio", "FELICIDAD FM"): 3.4,
    (2024, "Julio", "LA INOLVIDABLE FM"): 3.3,
    (2024, "Julio", "RADIOMAR FM"): 2.5,
    (2024, "Julio", "EXITOSA FM"): 2.2,
    (2024, "Julio", "LA KALLE FM"): 1.9,
    (2024, "Julio", "RADIO COMAS FM"): 0.4,
    (2024, "Julio", "CANTO GRANDE FM"): 0.0,
    (2024, "Julio", "NACIONAL FM"): 0.0,

    # ===========================================
    # 2025 - JULIO
    # ===========================================
    (2025, "Julio", "MODA FM"): 16.3,
    (2025, "Julio", "ONDA CERO FM"): 12.9,
    (2025, "Julio", "RADIO DISNEY FM"): 11.9,
    (2025, "Julio", "PLANETA FM"): 10.7,
    (2025, "Julio", "LA ZONA FM"): 7.6,
    (2025, "Julio", "OXIGENO FM"): 6.8,
    (2025, "Julio", "LA KARIBEÑA FM"): 6.8,
    (2025, "Julio", "NUEVA Q FM"): 6.0,
    (2025, "Julio", "CORAZON FM"): 5.4,
    (2025, "Julio", "STUDIO 92 FM"): 5.3,
    (2025, "Julio", "PANAMERICANA FM"): 5.1,
    (2025, "Julio", "RITMO ROMANTICA FM"): 5.0,
    (2025, "Julio", "RPP FM"): 4.5,
    (2025, "Julio", "MAGICA FM"): 4.0,
    (2025, "Julio", "RADIO MEGAMIX FM"): 3.9,
    (2025, "Julio", "RADIOMAR FM"): 3.4,
    (2025, "Julio", "LA KALLE FM"): 2.7,
    (2025, "Julio", "LA INOLVIDABLE FM"): 2.3,
    (2025, "Julio", "EXITOSA FM"): 2.1,
    (2025, "Julio", "FELICIDAD FM"): 1.7,
    (2025, "Julio", "BETHEL RADIO FM"): 0.4,
    (2025, "Julio", "CANTO GRANDE FM"): 0.3,
    (2025, "Julio", "RADIO DEL SUR FM"): 0.1,
    (2025, "Julio", "NACIONAL FM"): 0.0,
}

# Mapeo de mes disponible por año
# Como solo hay un mes de datos por año, ignoramos el mes del archivo
MES_POR_AÑO = {
    2023: "Septiembre",
    2024: "Julio",
    2025: "Julio"
}


def get_ranking(año: int, mes: str, emisora: str) -> float:
    """
    Busca el ranking para una combinación año-emisora.
    Solo hay un mes disponible por año, se ignora el mes del archivo.

    Estrategia:
    1. Si año <= 2023 → usar datos de 2023 Septiembre
    2. Si año == 2024 → usar datos de 2024 Julio
    3. Si año >= 2025 → usar datos de 2025 Julio
    4. Fallback: buscar en 2024 si no existe en año solicitado
    5. Fallback: buscar en cualquier año disponible
    """
    if año <= 2023:
        año_buscar, mes_buscar = 2023, "Septiembre"
    elif año == 2024:
        año_buscar, mes_buscar = 2024, "Julio"
    else:
        año_buscar, mes_buscar = 2025, "Julio"

    key = (año_buscar, mes_buscar, emisora)
    if key in RANKINGS:
        return RANKINGS[key]

    # Fallback: buscar en 2024 si no existe en año solicitado
    if año_buscar != 2024:
        key_fallback = (2024, "Julio", emisora)
        if key_fallback in RANKINGS:
            return RANKINGS[key_fallback]

    # Fallback: buscar en cualquier año
    for (a, m, e), v in RANKINGS.items():
        if e == emisora:
            return v

    return 0.0
