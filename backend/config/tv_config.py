"""
Tablas de configuración fijas para el cálculo de inversión en TV (Instar).
Actualizar RANKINGS_TV cuando salgan nuevos estudios de rating.
"""

# CPM y CPR por Canal y Tipo
# Para SPOTS se usa CPR (Cost Per Rating por segundo)
# Para otros tipos se usa CPM (Cost Per Mille)
CPM_TV = {
    # Latina
    ("LATINA", "SPOT"): {"cpm": 22.7, "cpr": 120.5},
    ("LATINA", "BANNER"): {"cpm": 4.5, "cpr": 0},
    ("LATINA", "L"): {"cpm": 1.13, "cpr": 0},
    ("LATINA", "MENCION"): {"cpm": 45.4, "cpr": 0},
    ("LATINA", "NOTICIEROS"): {"cpm": 22.7, "cpr": 120.5},

    # America TV
    ("AMERICA TV", "SPOT"): {"cpm": 22.7, "cpr": 115.0},
    ("AMERICA TV", "BANNER"): {"cpm": 4.5, "cpr": 0},
    ("AMERICA TV", "L"): {"cpm": 1.13, "cpr": 0},
    ("AMERICA TV", "MENCION"): {"cpm": 45.4, "cpr": 0},
    ("AMERICA TV", "NOTICIEROS"): {"cpm": 22.7, "cpr": 115.0},

    # ATV
    ("ATV", "SPOT"): {"cpm": 18.2, "cpr": 95.0},
    ("ATV", "BANNER"): {"cpm": 3.6, "cpr": 0},
    ("ATV", "L"): {"cpm": 0.91, "cpr": 0},
    ("ATV", "MENCION"): {"cpm": 36.4, "cpr": 0},
    ("ATV", "NOTICIEROS"): {"cpm": 18.2, "cpr": 95.0},

    # Panamericana TV
    ("PANAMERICANA TV", "SPOT"): {"cpm": 15.9, "cpr": 85.0},
    ("PANAMERICANA TV", "BANNER"): {"cpm": 3.2, "cpr": 0},
    ("PANAMERICANA TV", "L"): {"cpm": 0.80, "cpr": 0},
    ("PANAMERICANA TV", "MENCION"): {"cpm": 31.8, "cpr": 0},
    ("PANAMERICANA TV", "NOTICIEROS"): {"cpm": 15.9, "cpr": 85.0},

    # Willax
    ("WILLAX", "SPOT"): {"cpm": 11.4, "cpr": 60.0},
    ("WILLAX", "BANNER"): {"cpm": 2.3, "cpr": 0},
    ("WILLAX", "L"): {"cpm": 0.57, "cpr": 0},
    ("WILLAX", "MENCION"): {"cpm": 22.8, "cpr": 0},
    ("WILLAX", "NOTICIEROS"): {"cpm": 11.4, "cpr": 60.0},

    # TV Peru
    ("TV PERU", "SPOT"): {"cpm": 9.1, "cpr": 48.0},
    ("TV PERU", "BANNER"): {"cpm": 1.8, "cpr": 0},
    ("TV PERU", "L"): {"cpm": 0.45, "cpr": 0},
    ("TV PERU", "MENCION"): {"cpm": 18.2, "cpr": 0},
    ("TV PERU", "NOTICIEROS"): {"cpm": 9.1, "cpr": 48.0},

    # Global TV
    ("GLOBAL TV", "SPOT"): {"cpm": 6.8, "cpr": 36.0},
    ("GLOBAL TV", "BANNER"): {"cpm": 1.4, "cpr": 0},
    ("GLOBAL TV", "L"): {"cpm": 0.34, "cpr": 0},
    ("GLOBAL TV", "MENCION"): {"cpm": 13.6, "cpr": 0},
    ("GLOBAL TV", "NOTICIEROS"): {"cpm": 6.8, "cpr": 36.0},

    # Cable canales principales
    ("MOVISTAR DEPORTES", "SPOT"): {"cpm": 13.6, "cpr": 72.0},
    ("MOVISTAR DEPORTES", "BANNER"): {"cpm": 2.7, "cpr": 0},
    ("MOVISTAR DEPORTES", "L"): {"cpm": 0.68, "cpr": 0},
    ("MOVISTAR DEPORTES", "MENCION"): {"cpm": 27.2, "cpr": 0},

    ("LIGA 1 MAX", "SPOT"): {"cpm": 15.9, "cpr": 84.0},
    ("LIGA 1 MAX", "BANNER"): {"cpm": 3.2, "cpr": 0},
    ("LIGA 1 MAX", "L"): {"cpm": 0.80, "cpr": 0},
    ("LIGA 1 MAX", "MENCION"): {"cpm": 31.8, "cpr": 0},

    ("ESPN", "SPOT"): {"cpm": 11.4, "cpr": 60.0},
    ("ESPN", "BANNER"): {"cpm": 2.3, "cpr": 0},
    ("ESPN", "L"): {"cpm": 0.57, "cpr": 0},
    ("ESPN", "MENCION"): {"cpm": 22.8, "cpr": 0},

    ("FOX SPORTS", "SPOT"): {"cpm": 10.2, "cpr": 54.0},
    ("FOX SPORTS", "BANNER"): {"cpm": 2.0, "cpr": 0},
    ("FOX SPORTS", "L"): {"cpm": 0.51, "cpr": 0},
    ("FOX SPORTS", "MENCION"): {"cpm": 20.4, "cpr": 0},

    ("CMD", "SPOT"): {"cpm": 9.1, "cpr": 48.0},
    ("CMD", "BANNER"): {"cpm": 1.8, "cpr": 0},
    ("CMD", "L"): {"cpm": 0.45, "cpr": 0},
    ("CMD", "MENCION"): {"cpm": 18.2, "cpr": 0},

    ("RPP TV", "SPOT"): {"cpm": 4.5, "cpr": 24.0},
    ("RPP TV", "BANNER"): {"cpm": 0.9, "cpr": 0},
    ("RPP TV", "L"): {"cpm": 0.23, "cpr": 0},
    ("RPP TV", "MENCION"): {"cpm": 9.0, "cpr": 0},
}

# Valores por defecto para canales no especificados
DEFAULT_TV_CPM = {"cpm": 10.0, "cpr": 50.0}

# Mapeo de tipos de Instar a tipos agrupados
TIPO_MAPPING_TV = {
    "SPOT": "SPOT",
    "AVISO": "SPOT",
    "COMERCIAL": "SPOT",
    "BANNER": "BANNER",
    "SOBREIMPRESION": "BANNER",
    "L": "L",
    "MENCION": "MENCION",
    "MENCIÓN": "MENCION",
    "NOTICIEROS": "NOTICIEROS",
    "NOTICIERO": "NOTICIEROS",
}

# Mapeo de mes a mes de rating más cercano (para TV se miden todos los meses)
MES_TO_RANKING_TV = {
    "enero": "Enero",
    "febrero": "Febrero",
    "marzo": "Marzo",
    "abril": "Abril",
    "mayo": "Mayo",
    "junio": "Junio",
    "julio": "Julio",
    "agosto": "Agosto",
    "septiembre": "Septiembre",
    "octubre": "Octubre",
    "noviembre": "Noviembre",
    "diciembre": "Diciembre"
}

# Orden de meses para calcular distancia
MES_ORDEN_TV = {
    "Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4,
    "Mayo": 5, "Junio": 6, "Julio": 7, "Agosto": 8,
    "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12
}

# Ratings de TV por Año-Mes-Canal (Rating promedio en puntos)
# Formato: {(año, mes, canal): rating_puntos}
# ACTUALIZAR cuando salgan nuevos datos de Instar
RANKINGS_TV = {
    # 2024 - Enero
    (2024, "Enero", "LATINA"): 8.5,
    (2024, "Enero", "AMERICA TV"): 9.2,
    (2024, "Enero", "ATV"): 5.8,
    (2024, "Enero", "PANAMERICANA TV"): 3.2,
    (2024, "Enero", "WILLAX"): 2.1,
    (2024, "Enero", "TV PERU"): 1.5,
    (2024, "Enero", "GLOBAL TV"): 1.2,
    (2024, "Enero", "MOVISTAR DEPORTES"): 1.8,
    (2024, "Enero", "ESPN"): 0.9,
    (2024, "Enero", "FOX SPORTS"): 0.7,

    # 2024 - Febrero
    (2024, "Febrero", "LATINA"): 8.8,
    (2024, "Febrero", "AMERICA TV"): 9.5,
    (2024, "Febrero", "ATV"): 6.0,
    (2024, "Febrero", "PANAMERICANA TV"): 3.4,
    (2024, "Febrero", "WILLAX"): 2.3,
    (2024, "Febrero", "TV PERU"): 1.6,
    (2024, "Febrero", "GLOBAL TV"): 1.3,
    (2024, "Febrero", "MOVISTAR DEPORTES"): 1.9,
    (2024, "Febrero", "ESPN"): 1.0,
    (2024, "Febrero", "FOX SPORTS"): 0.8,

    # 2024 - Marzo
    (2024, "Marzo", "LATINA"): 9.1,
    (2024, "Marzo", "AMERICA TV"): 9.8,
    (2024, "Marzo", "ATV"): 6.3,
    (2024, "Marzo", "PANAMERICANA TV"): 3.6,
    (2024, "Marzo", "WILLAX"): 2.5,
    (2024, "Marzo", "TV PERU"): 1.7,
    (2024, "Marzo", "GLOBAL TV"): 1.4,
    (2024, "Marzo", "MOVISTAR DEPORTES"): 2.1,
    (2024, "Marzo", "ESPN"): 1.1,
    (2024, "Marzo", "FOX SPORTS"): 0.9,

    # 2024 - Abril
    (2024, "Abril", "LATINA"): 8.7,
    (2024, "Abril", "AMERICA TV"): 9.4,
    (2024, "Abril", "ATV"): 6.1,
    (2024, "Abril", "PANAMERICANA TV"): 3.3,
    (2024, "Abril", "WILLAX"): 2.2,
    (2024, "Abril", "TV PERU"): 1.5,
    (2024, "Abril", "GLOBAL TV"): 1.2,
    (2024, "Abril", "MOVISTAR DEPORTES"): 1.9,
    (2024, "Abril", "ESPN"): 0.9,
    (2024, "Abril", "FOX SPORTS"): 0.7,

    # 2024 - Mayo
    (2024, "Mayo", "LATINA"): 8.4,
    (2024, "Mayo", "AMERICA TV"): 9.1,
    (2024, "Mayo", "ATV"): 5.9,
    (2024, "Mayo", "PANAMERICANA TV"): 3.1,
    (2024, "Mayo", "WILLAX"): 2.0,
    (2024, "Mayo", "TV PERU"): 1.4,
    (2024, "Mayo", "GLOBAL TV"): 1.1,
    (2024, "Mayo", "MOVISTAR DEPORTES"): 1.7,
    (2024, "Mayo", "ESPN"): 0.8,
    (2024, "Mayo", "FOX SPORTS"): 0.6,

    # 2024 - Junio
    (2024, "Junio", "LATINA"): 8.9,
    (2024, "Junio", "AMERICA TV"): 9.6,
    (2024, "Junio", "ATV"): 6.2,
    (2024, "Junio", "PANAMERICANA TV"): 3.5,
    (2024, "Junio", "WILLAX"): 2.4,
    (2024, "Junio", "TV PERU"): 1.6,
    (2024, "Junio", "GLOBAL TV"): 1.3,
    (2024, "Junio", "MOVISTAR DEPORTES"): 2.0,
    (2024, "Junio", "ESPN"): 1.0,
    (2024, "Junio", "FOX SPORTS"): 0.8,

    # 2024 - Julio
    (2024, "Julio", "LATINA"): 9.3,
    (2024, "Julio", "AMERICA TV"): 10.0,
    (2024, "Julio", "ATV"): 6.5,
    (2024, "Julio", "PANAMERICANA TV"): 3.8,
    (2024, "Julio", "WILLAX"): 2.6,
    (2024, "Julio", "TV PERU"): 1.8,
    (2024, "Julio", "GLOBAL TV"): 1.5,
    (2024, "Julio", "MOVISTAR DEPORTES"): 2.2,
    (2024, "Julio", "ESPN"): 1.2,
    (2024, "Julio", "FOX SPORTS"): 1.0,

    # 2024 - Agosto
    (2024, "Agosto", "LATINA"): 9.0,
    (2024, "Agosto", "AMERICA TV"): 9.7,
    (2024, "Agosto", "ATV"): 6.3,
    (2024, "Agosto", "PANAMERICANA TV"): 3.5,
    (2024, "Agosto", "WILLAX"): 2.4,
    (2024, "Agosto", "TV PERU"): 1.7,
    (2024, "Agosto", "GLOBAL TV"): 1.4,
    (2024, "Agosto", "MOVISTAR DEPORTES"): 2.0,
    (2024, "Agosto", "ESPN"): 1.1,
    (2024, "Agosto", "FOX SPORTS"): 0.9,

    # 2024 - Septiembre
    (2024, "Septiembre", "LATINA"): 8.6,
    (2024, "Septiembre", "AMERICA TV"): 9.3,
    (2024, "Septiembre", "ATV"): 6.0,
    (2024, "Septiembre", "PANAMERICANA TV"): 3.3,
    (2024, "Septiembre", "WILLAX"): 2.2,
    (2024, "Septiembre", "TV PERU"): 1.5,
    (2024, "Septiembre", "GLOBAL TV"): 1.2,
    (2024, "Septiembre", "MOVISTAR DEPORTES"): 1.8,
    (2024, "Septiembre", "ESPN"): 0.9,
    (2024, "Septiembre", "FOX SPORTS"): 0.7,

    # 2024 - Octubre
    (2024, "Octubre", "LATINA"): 8.8,
    (2024, "Octubre", "AMERICA TV"): 9.5,
    (2024, "Octubre", "ATV"): 6.1,
    (2024, "Octubre", "PANAMERICANA TV"): 3.4,
    (2024, "Octubre", "WILLAX"): 2.3,
    (2024, "Octubre", "TV PERU"): 1.6,
    (2024, "Octubre", "GLOBAL TV"): 1.3,
    (2024, "Octubre", "MOVISTAR DEPORTES"): 1.9,
    (2024, "Octubre", "ESPN"): 1.0,
    (2024, "Octubre", "FOX SPORTS"): 0.8,

    # 2024 - Noviembre
    (2024, "Noviembre", "LATINA"): 9.2,
    (2024, "Noviembre", "AMERICA TV"): 9.9,
    (2024, "Noviembre", "ATV"): 6.4,
    (2024, "Noviembre", "PANAMERICANA TV"): 3.7,
    (2024, "Noviembre", "WILLAX"): 2.5,
    (2024, "Noviembre", "TV PERU"): 1.8,
    (2024, "Noviembre", "GLOBAL TV"): 1.4,
    (2024, "Noviembre", "MOVISTAR DEPORTES"): 2.1,
    (2024, "Noviembre", "ESPN"): 1.1,
    (2024, "Noviembre", "FOX SPORTS"): 0.9,

    # 2024 - Diciembre
    (2024, "Diciembre", "LATINA"): 9.5,
    (2024, "Diciembre", "AMERICA TV"): 10.2,
    (2024, "Diciembre", "ATV"): 6.7,
    (2024, "Diciembre", "PANAMERICANA TV"): 3.9,
    (2024, "Diciembre", "WILLAX"): 2.7,
    (2024, "Diciembre", "TV PERU"): 1.9,
    (2024, "Diciembre", "GLOBAL TV"): 1.5,
    (2024, "Diciembre", "MOVISTAR DEPORTES"): 2.3,
    (2024, "Diciembre", "ESPN"): 1.2,
    (2024, "Diciembre", "FOX SPORTS"): 1.0,

    # 2025 - Enero
    (2025, "Enero", "LATINA"): 8.7,
    (2025, "Enero", "AMERICA TV"): 9.4,
    (2025, "Enero", "ATV"): 6.0,
    (2025, "Enero", "PANAMERICANA TV"): 3.4,
    (2025, "Enero", "WILLAX"): 2.3,
    (2025, "Enero", "TV PERU"): 1.6,
    (2025, "Enero", "GLOBAL TV"): 1.3,
    (2025, "Enero", "MOVISTAR DEPORTES"): 1.9,
    (2025, "Enero", "LIGA 1 MAX"): 2.5,
    (2025, "Enero", "ESPN"): 1.0,
    (2025, "Enero", "FOX SPORTS"): 0.8,

    # 2025 - Febrero
    (2025, "Febrero", "LATINA"): 9.0,
    (2025, "Febrero", "AMERICA TV"): 9.7,
    (2025, "Febrero", "ATV"): 6.3,
    (2025, "Febrero", "PANAMERICANA TV"): 3.6,
    (2025, "Febrero", "WILLAX"): 2.5,
    (2025, "Febrero", "TV PERU"): 1.7,
    (2025, "Febrero", "GLOBAL TV"): 1.4,
    (2025, "Febrero", "MOVISTAR DEPORTES"): 2.1,
    (2025, "Febrero", "LIGA 1 MAX"): 2.8,
    (2025, "Febrero", "ESPN"): 1.1,
    (2025, "Febrero", "FOX SPORTS"): 0.9,

    # 2025 - Marzo
    (2025, "Marzo", "LATINA"): 9.2,
    (2025, "Marzo", "AMERICA TV"): 9.9,
    (2025, "Marzo", "ATV"): 6.5,
    (2025, "Marzo", "PANAMERICANA TV"): 3.7,
    (2025, "Marzo", "WILLAX"): 2.6,
    (2025, "Marzo", "TV PERU"): 1.8,
    (2025, "Marzo", "GLOBAL TV"): 1.5,
    (2025, "Marzo", "MOVISTAR DEPORTES"): 2.2,
    (2025, "Marzo", "LIGA 1 MAX"): 3.0,
    (2025, "Marzo", "ESPN"): 1.2,
    (2025, "Marzo", "FOX SPORTS"): 1.0,

    # 2025 - Abril
    (2025, "Abril", "LATINA"): 8.9,
    (2025, "Abril", "AMERICA TV"): 9.6,
    (2025, "Abril", "ATV"): 6.2,
    (2025, "Abril", "PANAMERICANA TV"): 3.5,
    (2025, "Abril", "WILLAX"): 2.4,
    (2025, "Abril", "TV PERU"): 1.7,
    (2025, "Abril", "GLOBAL TV"): 1.4,
    (2025, "Abril", "MOVISTAR DEPORTES"): 2.0,
    (2025, "Abril", "LIGA 1 MAX"): 2.7,
    (2025, "Abril", "ESPN"): 1.0,
    (2025, "Abril", "FOX SPORTS"): 0.8,

    # 2025 - Mayo
    (2025, "Mayo", "LATINA"): 8.6,
    (2025, "Mayo", "AMERICA TV"): 9.3,
    (2025, "Mayo", "ATV"): 6.0,
    (2025, "Mayo", "PANAMERICANA TV"): 3.3,
    (2025, "Mayo", "WILLAX"): 2.2,
    (2025, "Mayo", "TV PERU"): 1.6,
    (2025, "Mayo", "GLOBAL TV"): 1.3,
    (2025, "Mayo", "MOVISTAR DEPORTES"): 1.9,
    (2025, "Mayo", "LIGA 1 MAX"): 2.6,
    (2025, "Mayo", "ESPN"): 0.9,
    (2025, "Mayo", "FOX SPORTS"): 0.7,

    # 2025 - Junio
    (2025, "Junio", "LATINA"): 9.1,
    (2025, "Junio", "AMERICA TV"): 9.8,
    (2025, "Junio", "ATV"): 6.4,
    (2025, "Junio", "PANAMERICANA TV"): 3.6,
    (2025, "Junio", "WILLAX"): 2.5,
    (2025, "Junio", "TV PERU"): 1.8,
    (2025, "Junio", "GLOBAL TV"): 1.4,
    (2025, "Junio", "MOVISTAR DEPORTES"): 2.1,
    (2025, "Junio", "LIGA 1 MAX"): 2.9,
    (2025, "Junio", "ESPN"): 1.1,
    (2025, "Junio", "FOX SPORTS"): 0.9,

    # 2025 - Julio
    (2025, "Julio", "LATINA"): 9.4,
    (2025, "Julio", "AMERICA TV"): 10.1,
    (2025, "Julio", "ATV"): 6.6,
    (2025, "Julio", "PANAMERICANA TV"): 3.8,
    (2025, "Julio", "WILLAX"): 2.7,
    (2025, "Julio", "TV PERU"): 1.9,
    (2025, "Julio", "GLOBAL TV"): 1.5,
    (2025, "Julio", "MOVISTAR DEPORTES"): 2.3,
    (2025, "Julio", "LIGA 1 MAX"): 3.1,
    (2025, "Julio", "ESPN"): 1.2,
    (2025, "Julio", "FOX SPORTS"): 1.0,

    # 2025 - Agosto
    (2025, "Agosto", "LATINA"): 9.3,
    (2025, "Agosto", "AMERICA TV"): 10.0,
    (2025, "Agosto", "ATV"): 6.5,
    (2025, "Agosto", "PANAMERICANA TV"): 3.7,
    (2025, "Agosto", "WILLAX"): 2.6,
    (2025, "Agosto", "TV PERU"): 1.8,
    (2025, "Agosto", "GLOBAL TV"): 1.5,
    (2025, "Agosto", "MOVISTAR DEPORTES"): 2.2,
    (2025, "Agosto", "LIGA 1 MAX"): 3.0,
    (2025, "Agosto", "ESPN"): 1.1,
    (2025, "Agosto", "FOX SPORTS"): 0.9,

    # 2025 - Septiembre
    (2025, "Septiembre", "LATINA"): 9.0,
    (2025, "Septiembre", "AMERICA TV"): 9.7,
    (2025, "Septiembre", "ATV"): 6.3,
    (2025, "Septiembre", "PANAMERICANA TV"): 3.5,
    (2025, "Septiembre", "WILLAX"): 2.5,
    (2025, "Septiembre", "TV PERU"): 1.7,
    (2025, "Septiembre", "GLOBAL TV"): 1.4,
    (2025, "Septiembre", "MOVISTAR DEPORTES"): 2.1,
    (2025, "Septiembre", "LIGA 1 MAX"): 2.8,
    (2025, "Septiembre", "ESPN"): 1.0,
    (2025, "Septiembre", "FOX SPORTS"): 0.8,

    # 2025 - Octubre
    (2025, "Octubre", "LATINA"): 9.1,
    (2025, "Octubre", "AMERICA TV"): 9.8,
    (2025, "Octubre", "ATV"): 6.4,
    (2025, "Octubre", "PANAMERICANA TV"): 3.6,
    (2025, "Octubre", "WILLAX"): 2.6,
    (2025, "Octubre", "TV PERU"): 1.8,
    (2025, "Octubre", "GLOBAL TV"): 1.4,
    (2025, "Octubre", "MOVISTAR DEPORTES"): 2.2,
    (2025, "Octubre", "LIGA 1 MAX"): 2.9,
    (2025, "Octubre", "ESPN"): 1.1,
    (2025, "Octubre", "FOX SPORTS"): 0.9,

    # 2025 - Noviembre
    (2025, "Noviembre", "LATINA"): 9.4,
    (2025, "Noviembre", "AMERICA TV"): 10.1,
    (2025, "Noviembre", "ATV"): 6.6,
    (2025, "Noviembre", "PANAMERICANA TV"): 3.8,
    (2025, "Noviembre", "WILLAX"): 2.7,
    (2025, "Noviembre", "TV PERU"): 1.9,
    (2025, "Noviembre", "GLOBAL TV"): 1.5,
    (2025, "Noviembre", "MOVISTAR DEPORTES"): 2.3,
    (2025, "Noviembre", "LIGA 1 MAX"): 3.1,
    (2025, "Noviembre", "ESPN"): 1.2,
    (2025, "Noviembre", "FOX SPORTS"): 1.0,
}


def get_tv_config(canal: str, tipo: str) -> dict:
    """
    Obtiene el CPM y CPR para una combinación canal-tipo.
    """
    key = (canal.upper(), tipo.upper())
    if key in CPM_TV:
        return CPM_TV[key]

    # Buscar solo por canal con tipo SPOT como default
    for (c, t), values in CPM_TV.items():
        if c == canal.upper() and t == "SPOT":
            return {"cpm": values["cpm"], "cpr": values.get("cpr", 0)}

    return DEFAULT_TV_CPM


def get_rating_tv(año: int, mes: str, canal: str) -> float:
    """
    Obtiene el rating para una combinación año-mes-canal.
    Estrategia de fallback:
    1. Buscar mes exacto
    2. Buscar los dos meses más cercanos del mismo año y promediar
    3. Si solo hay un mes en el año, usar ese
    4. Buscar promedio histórico del canal en todos los años
    """
    key = (año, mes, canal.upper())
    if key in RANKINGS_TV:
        return RANKINGS_TV[key]

    # Obtener todos los meses disponibles para este canal en este año
    meses_disponibles = [
        (m, RANKINGS_TV[(a, m, c)])
        for (a, m, c) in RANKINGS_TV.keys()
        if a == año and c.upper() == canal.upper()
    ]

    if meses_disponibles:
        mes_num = MES_ORDEN_TV.get(mes, 6)

        meses_con_distancia = []
        for m, rating in meses_disponibles:
            m_num = MES_ORDEN_TV.get(m, 6)
            distancia = abs(mes_num - m_num)
            meses_con_distancia.append((distancia, m, rating))

        meses_con_distancia.sort(key=lambda x: x[0])

        if len(meses_con_distancia) >= 2:
            rating1 = meses_con_distancia[0][2]
            rating2 = meses_con_distancia[1][2]
            return (rating1 + rating2) / 2
        else:
            return meses_con_distancia[0][2]

    # Si no hay data del año, buscar promedio histórico del canal
    all_ratings = [v for (a, m, c), v in RANKINGS_TV.items() if c.upper() == canal.upper()]
    if all_ratings:
        return sum(all_ratings) / len(all_ratings)

    return 1.0  # Rating mínimo por defecto
