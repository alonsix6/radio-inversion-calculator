# Migración: Media Investment Calculator → SiReset

**Fecha:** 2026-01-07
**Herramienta:** Calculadora de Inversión en Medios (Radio + TV)
**Versión Legacy:** 2.0.0

---

## 1. Resumen Ejecutivo

**Propósito:** Calculadora que estima inversión publicitaria en Radio (IBOPE) y TV (Instar) procesando archivos Excel con datos de pauta y aplicando fórmulas de CPM/CPR.

**Usuarios:** Media Planners, Analistas de medios, equipos de planning de cualquier cliente.

**Complejidad:** Media

**Tiempo estimado:** 4-5 días

### Funcionalidades a migrar:
1. **Procesador Radio (IBOPE)** - Upload Excel, cálculo de inversión por CPM × Impactos
2. **Procesador TV (Instar)** - Upload Excel, cálculo diferenciado CPR (spots) vs CPM (otros)
3. **Visualización de Rankings** - Modal con rankings CPI (radio) y Ratings (TV)
4. **Descarga de Templates** - Plantillas Excel con formato requerido
5. **Generación de Reportes** - Excel multi-hoja con resúmenes por marca/tipo/mes/medio

---

## 2. Arquitectura Propuesta en SiReset

### Backend (`backend/app/`)

```
backend/app/
├── api/routes/
│   └── media_investment.py          # Endpoints Radio + TV
├── processors/
│   ├── media_radio_processor.py     # Lógica procesamiento Radio
│   └── media_tv_processor.py        # Lógica procesamiento TV
├── schemas/
│   └── media_investment.py          # Pydantic models
└── data/
    └── media_config.py              # CPM, Rankings (archivo estático)
```

### Frontend (`frontend/src/`)

```
frontend/src/
├── pages/
│   └── MediaInvestment.jsx          # Página principal con tabs
└── components/
    └── MediaInvestment/
        ├── RadioUploader.jsx        # Upload zone Radio
        ├── TVUploader.jsx           # Upload zone TV
        ├── RankingsModal.jsx        # Modal rankings/ratings
        └── ConfigDisplay.jsx        # Tarjetas CPM/CPR
```

---

## 3. Mapeo Legacy → SiReset

### Backend

| Legacy | SiReset | Cambios |
|--------|---------|---------|
| `main.py:POST /process/radio` | `routes/media_investment.py:POST /api/media/process/radio` | Prefijo `/api/media` |
| `main.py:POST /process/tv` | `routes/media_investment.py:POST /api/media/process/tv` | Prefijo `/api/media` |
| `main.py:GET /rankings/radio` | `routes/media_investment.py:GET /api/media/rankings/radio` | Prefijo `/api/media` |
| `main.py:GET /rankings/tv` | `routes/media_investment.py:GET /api/media/rankings/tv` | Prefijo `/api/media` |
| `main.py:GET /template/*` | `routes/media_investment.py:GET /api/media/template/*` | Prefijo `/api/media` |
| `config/radio_config.py` | `data/media_config.py` | Unificar en un archivo |
| `config/tv_config.py` | `data/media_config.py` | Unificar en un archivo |
| `processors/radio_processor.py` | `processors/media_radio_processor.py` | Sin cambios lógicos |
| `processors/tv_processor.py` | `processors/media_tv_processor.py` | Sin cambios lógicos |

### Frontend

| Legacy | SiReset | Cambios |
|--------|---------|---------|
| `index.html` | `pages/MediaInvestment.jsx` | Convertir a React + Tailwind |
| `app.js` (Radio logic) | `components/MediaInvestment/RadioUploader.jsx` | React hooks |
| `app.js` (TV logic) | `components/MediaInvestment/TVUploader.jsx` | React hooks |
| `app.js` (Modal logic) | `components/MediaInvestment/RankingsModal.jsx` | React modal |
| `styles.css` | Tailwind inline classes | Aplicar Design System Reset |

---

## 4. Código Crítico - COPIAR ÍNTEGRO

### 4.1 Configuración Radio (CPM + Rankings)

```python
# data/media_config.py - SECCIÓN RADIO

# CPM calibrados con optimización (mínimos cuadrados)
# Calibrado contra inversión real SEMCO (sin IGV) 2023-2025
# Error < 0.1% en los 3 años de data
# Ratio SPOT:MENCION:P/D = 1:5.0:11.2
CPM_RADIO = {
    "SPOT": 16.30,
    "MENCION": 81.40,
    "P/D": 181.80
}

# Mapeo de tipos IBOPE a tipos agrupados
TIPO_MAPPING_RADIO = {
    "SPOT": "SPOT",
    "MENCION": "MENCION",
    "DESP.PROGRAMA": "P/D",
    "DESP.SUBPROGRAMA": "P/D",
    "PRES.PROGRAMA": "P/D",
    "PRES.SUBPROGRAMA": "P/D"
}

# Rankings de CPI por Año-Mes-Emisora
# IMPACTOS POR RANGO DE HORAS (valores en miles: 20.4 = 20,400 personas/hora)
# Target: H+M 15-24 ABC Lima
RANKINGS_RADIO = {
    # 2023 - SEPTIEMBRE
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

    # 2024 - JULIO
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

    # 2025 - JULIO
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

# Mapeo de mes disponible por año (solo hay un mes de datos por año)
MES_POR_AÑO_RADIO = {
    2023: "Septiembre",
    2024: "Julio",
    2025: "Julio"
}


def get_ranking_radio(año: int, mes: str, emisora: str) -> float:
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
    if key in RANKINGS_RADIO:
        return RANKINGS_RADIO[key]

    # Fallback: buscar en 2024 si no existe en año solicitado
    if año_buscar != 2024:
        key_fallback = (2024, "Julio", emisora)
        if key_fallback in RANKINGS_RADIO:
            return RANKINGS_RADIO[key_fallback]

    # Fallback: buscar en cualquier año
    for (a, m, e), v in RANKINGS_RADIO.items():
        if e == emisora:
            return v

    return 0.0
```

### 4.2 Configuración TV (CPM/CPR + Ratings)

```python
# data/media_config.py - SECCIÓN TV

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

# Orden de meses para calcular distancia
MES_ORDEN_TV = {
    "Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4,
    "Mayo": 5, "Junio": 6, "Julio": 7, "Agosto": 8,
    "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12
}

# Ratings de TV por Año-Mes-Canal (Rating promedio en puntos)
# ACTUALIZAR cuando salgan nuevos datos de Instar
RANKINGS_TV = {
    # 2024 - Enero a Diciembre (10 canales)
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
    # ... (continuar con todos los meses de 2024)

    # 2025 - Enero a Noviembre (11 canales, incluye LIGA 1 MAX)
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
    # ... (continuar con todos los meses de 2025)
}
# NOTA: Ver archivo legacy tv_config.py para datos completos de RANKINGS_TV


def get_tv_config(canal: str, tipo: str) -> dict:
    """Obtiene el CPM y CPR para una combinación canal-tipo."""
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
            return (meses_con_distancia[0][2] + meses_con_distancia[1][2]) / 2
        else:
            return meses_con_distancia[0][2]

    # Si no hay data del año, buscar promedio histórico del canal
    all_ratings = [v for (a, m, c), v in RANKINGS_TV.items() if c.upper() == canal.upper()]
    if all_ratings:
        return sum(all_ratings) / len(all_ratings)

    return 1.0  # Rating mínimo por defecto
```

### 4.3 Procesador Radio (Lógica Core)

```python
# processors/media_radio_processor.py

import pandas as pd
from io import BytesIO
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

from app.data.media_config import CPM_RADIO, TIPO_MAPPING_RADIO, get_ranking_radio


def process_radio_file(file_content: bytes, filename: str) -> BytesIO:
    """
    Procesa un archivo Excel de IBOPE y devuelve un Excel con los cálculos de inversión.

    Columnas requeridas: MARCA, TIPO, EMISORA/SITE, MES, AÑO, Suma de SPOTS
    """
    df = pd.read_excel(BytesIO(file_content))

    # Normalizar nombres de columnas
    df.columns = [str(col).strip().upper() for col in df.columns]

    # Mapear columnas conocidas
    column_mapping = {
        'EMISORA/SITE': 'EMISORA',
        'SUMA DE SPOTS': 'SPOTS',
        'SUMA DE SPOT': 'SPOTS',
        'SPOTS': 'SPOTS',
        'AÑO': 'AÑO',
        'ANO': 'AÑO',
    }

    for old_name, new_name in column_mapping.items():
        if old_name in df.columns:
            df = df.rename(columns={old_name: new_name})

    # Verificar columnas requeridas
    required_cols = ['MARCA', 'TIPO', 'EMISORA', 'MES', 'AÑO', 'SPOTS']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Columnas faltantes: {missing_cols}. Encontradas: {list(df.columns)}")

    # Limpiar datos
    df = df.dropna(subset=['MARCA', 'TIPO', 'EMISORA', 'SPOTS'])
    df['SPOTS'] = pd.to_numeric(df['SPOTS'], errors='coerce').fillna(0).astype(int)
    df['AÑO'] = pd.to_numeric(df['AÑO'], errors='coerce').fillna(2024).astype(int)

    # Calcular columnas adicionales
    df['TIPO_AGRUP'] = df['TIPO'].map(TIPO_MAPPING_RADIO).fillna('SPOT')
    df['CPM'] = df['TIPO_AGRUP'].map(CPM_RADIO).fillna(16.30)

    # Calcular ranking (el mes se ignora, solo importa el año)
    df['RANKING_MILES'] = df.apply(
        lambda row: get_ranking_radio(row['AÑO'], str(row['MES']), row['EMISORA']),
        axis=1
    )

    # === FÓRMULAS CRÍTICAS ===
    # Impactos = Spots × Ranking (rankings ya están en miles)
    # Inversión = Impactos × CPM
    df['Impactos_Miles'] = (df['SPOTS'] * df['RANKING_MILES']).round(0).astype(int)
    df['INVERSION_SOLES'] = (df['Impactos_Miles'] * df['CPM']).round(2)

    # Crear Excel de salida con múltiples hojas
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        # Hoja 1: Detalle completo
        df_output = df[['MARCA', 'TIPO', 'TIPO_AGRUP', 'EMISORA', 'MES', 'AÑO',
                        'SPOTS', 'CPM', 'RANKING_MILES', 'Impactos_Miles', 'INVERSION_SOLES']]
        df_output.to_excel(writer, sheet_name='Detalle', index=False)

        # Hoja 2: Resumen por Marca
        resumen_marca = df.groupby('MARCA').agg({
            'SPOTS': 'sum', 'Impactos_Miles': 'sum', 'INVERSION_SOLES': 'sum'
        }).reset_index()
        resumen_marca.columns = ['Marca', 'Total Spots', 'Impactos_Miles', 'Inversión (S/)']
        resumen_marca.to_excel(writer, sheet_name='Resumen por Marca', index=False)

        # Hoja 3: Resumen por Marca y Tipo
        resumen_tipo = df.groupby(['MARCA', 'TIPO_AGRUP']).agg({
            'SPOTS': 'sum', 'Impactos_Miles': 'sum', 'INVERSION_SOLES': 'sum'
        }).reset_index()
        resumen_tipo.columns = ['Marca', 'Tipo', 'Total Spots', 'Impactos_Miles', 'Inversión (S/)']
        resumen_tipo.to_excel(writer, sheet_name='Resumen por Tipo', index=False)

        # Hoja 4: Resumen por Marca y Mes
        resumen_mes = df.groupby(['MARCA', 'AÑO', 'MES']).agg({
            'SPOTS': 'sum', 'Impactos_Miles': 'sum', 'INVERSION_SOLES': 'sum'
        }).reset_index()
        resumen_mes.columns = ['Marca', 'Año', 'Mes', 'Total Spots', 'Impactos_Miles', 'Inversión (S/)']
        resumen_mes.to_excel(writer, sheet_name='Resumen por Mes', index=False)

        # Hoja 5: Resumen por Emisora
        resumen_emisora = df.groupby(['MARCA', 'EMISORA']).agg({
            'SPOTS': 'sum', 'Impactos_Miles': 'sum', 'INVERSION_SOLES': 'sum'
        }).reset_index()
        resumen_emisora.columns = ['Marca', 'Emisora', 'Total Spots', 'Impactos_Miles', 'Inversión (S/)']
        resumen_emisora.to_excel(writer, sheet_name='Resumen por Emisora', index=False)

        _apply_excel_formatting(writer.book, '#00FF85')  # Verde Reset

    output.seek(0)
    return output


def get_radio_summary_stats(file_content: bytes) -> dict:
    """Devuelve estadísticas resumidas del archivo."""
    df = pd.read_excel(BytesIO(file_content))
    df.columns = [str(col).strip().upper() for col in df.columns]

    column_mapping = {'EMISORA/SITE': 'EMISORA', 'SUMA DE SPOTS': 'SPOTS'}
    for old_name, new_name in column_mapping.items():
        if old_name in df.columns:
            df = df.rename(columns={old_name: new_name})

    return {
        'total_filas': len(df),
        'marcas': df['MARCA'].nunique() if 'MARCA' in df.columns else 0,
        'emisoras': df['EMISORA'].nunique() if 'EMISORA' in df.columns else 0,
        'columnas': list(df.columns)
    }


def _apply_excel_formatting(workbook, accent_color: str = '#00FF85'):
    """Aplica formato Reset a todas las hojas del workbook."""
    header_fill = PatternFill('solid', fgColor=accent_color.replace('#', ''))
    header_font = Font(bold=True, color='000000')

    for sheet_name in workbook.sheetnames:
        ws = workbook[sheet_name]
        for cell in ws[1]:
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = Alignment(horizontal='center')

        for column in ws.columns:
            max_length = 0
            column_letter = get_column_letter(column[0].column)
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            ws.column_dimensions[column_letter].width = min(max_length + 2, 40)
```

### 4.4 Procesador TV (Lógica Core)

```python
# processors/media_tv_processor.py

import pandas as pd
from io import BytesIO
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

from app.data.media_config import TIPO_MAPPING_TV, get_tv_config


def process_tv_file(file_content: bytes, filename: str) -> BytesIO:
    """
    Procesa un archivo Excel de Instar y devuelve un Excel con los cálculos de inversión.

    Columnas requeridas: MARCA, TIPO COMERCIAL, CANAL, MES, AÑO, TOTAL SPOTS, GRP#, GRP%
    Columna opcional: DURACIÓN (default 30 segundos)
    """
    df = pd.read_excel(BytesIO(file_content))

    # Normalizar nombres de columnas
    df.columns = [str(col).strip().upper() for col in df.columns]

    # Mapear columnas conocidas (nombres de Instar)
    column_mapping = {
        'CANAL/SITE': 'CANAL',
        'TOTAL SPOTS': 'SPOTS',
        'SUMA DE SPOTS': 'SPOTS',
        'SUMA DE SPOT': 'SPOTS',
        'SUMA DE AVISOS': 'SPOTS',
        'AVISOS': 'SPOTS',
        'SPOTS': 'SPOTS',
        'TIPO COMERCIAL': 'TIPO',
        'AÑO': 'AÑO',
        'ANO': 'AÑO',
        'DURACION': 'SEGUNDOS',
        'DURACIÓN': 'SEGUNDOS',
        'SUMA DE SEGUNDOS': 'SEGUNDOS',
        'GRP# [RATING]': 'GRP_NUM',
        'GRP#': 'GRP_NUM',
        'GRP% [RATING]': 'GRP_PCT',
        'GRP%': 'GRP_PCT',
    }

    for old_name, new_name in column_mapping.items():
        if old_name in df.columns:
            df = df.rename(columns={old_name: new_name})

    # Verificar columnas requeridas
    required_cols = ['MARCA', 'TIPO', 'CANAL', 'MES', 'AÑO', 'SPOTS', 'GRP_NUM', 'GRP_PCT']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Columnas faltantes: {missing_cols}. Encontradas: {list(df.columns)}")

    # Columna SEGUNDOS opcional (default 30)
    if 'SEGUNDOS' not in df.columns:
        df['SEGUNDOS'] = 30

    # Limpiar datos
    df = df.dropna(subset=['MARCA', 'TIPO', 'CANAL', 'SPOTS'])
    df['SPOTS'] = pd.to_numeric(df['SPOTS'], errors='coerce').fillna(0).astype(int)
    df['AÑO'] = pd.to_numeric(df['AÑO'], errors='coerce').fillna(2024).astype(int)
    df['SEGUNDOS'] = pd.to_numeric(df['SEGUNDOS'], errors='coerce').fillna(30).astype(int)
    df['GRP_NUM'] = pd.to_numeric(df['GRP_NUM'], errors='coerce').fillna(0)
    df['GRP_PCT'] = pd.to_numeric(df['GRP_PCT'], errors='coerce').fillna(0)

    # Calcular columnas adicionales
    df['TIPO_AGRUP'] = df['TIPO'].str.upper().map(TIPO_MAPPING_TV).fillna('SPOT')

    # Obtener CPM/CPR para cada fila
    def get_cpm_cpr(row):
        config = get_tv_config(row['CANAL'], row['TIPO_AGRUP'])
        return pd.Series({'CPM': config['cpm'], 'CPR': config['cpr']})

    df[['CPM', 'CPR']] = df.apply(get_cpm_cpr, axis=1)

    # Calcular impactos (referencia)
    df['Impactos_Miles'] = (df['GRP_NUM'] * 1000).round(0).astype(int)

    # === FÓRMULAS CRÍTICAS ===
    # Para SPOTS/NOTICIEROS: Inversión = GRP% × CPR × Segundos
    # Para otros (BANNER, L, MENCION): Inversión = GRP# × CPM
    def calcular_inversion(row):
        if row['TIPO_AGRUP'] in ('SPOT', 'NOTICIEROS'):
            return round(row['GRP_PCT'] * row['CPR'] * row['SEGUNDOS'], 2)
        else:
            return round(row['GRP_NUM'] * row['CPM'], 2)

    df['INVERSION_SOLES'] = df.apply(calcular_inversion, axis=1)

    # Crear Excel de salida con múltiples hojas
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        # Hoja 1: Detalle completo
        df_output = df[['MARCA', 'TIPO', 'TIPO_AGRUP', 'CANAL', 'MES', 'AÑO',
                        'SPOTS', 'SEGUNDOS', 'GRP_NUM', 'GRP_PCT', 'CPM', 'CPR',
                        'Impactos_Miles', 'INVERSION_SOLES']]
        df_output.to_excel(writer, sheet_name='Detalle', index=False)

        # Hoja 2: Resumen por Marca
        resumen_marca = df.groupby('MARCA').agg({
            'SPOTS': 'sum', 'GRP_NUM': 'sum', 'GRP_PCT': 'sum',
            'Impactos_Miles': 'sum', 'INVERSION_SOLES': 'sum'
        }).reset_index()
        resumen_marca.columns = ['Marca', 'Total Avisos', 'GRP#', 'GRP%', 'Impactos_Miles', 'Inversión (S/)']
        resumen_marca.to_excel(writer, sheet_name='Resumen por Marca', index=False)

        # Hoja 3: Resumen por Marca y Tipo
        resumen_tipo = df.groupby(['MARCA', 'TIPO_AGRUP']).agg({
            'SPOTS': 'sum', 'GRP_NUM': 'sum', 'GRP_PCT': 'sum',
            'Impactos_Miles': 'sum', 'INVERSION_SOLES': 'sum'
        }).reset_index()
        resumen_tipo.columns = ['Marca', 'Tipo', 'Total Avisos', 'GRP#', 'GRP%', 'Impactos_Miles', 'Inversión (S/)']
        resumen_tipo.to_excel(writer, sheet_name='Resumen por Tipo', index=False)

        # Hoja 4: Resumen por Marca y Mes
        resumen_mes = df.groupby(['MARCA', 'AÑO', 'MES']).agg({
            'SPOTS': 'sum', 'GRP_NUM': 'sum', 'GRP_PCT': 'sum',
            'Impactos_Miles': 'sum', 'INVERSION_SOLES': 'sum'
        }).reset_index()
        resumen_mes.columns = ['Marca', 'Año', 'Mes', 'Total Avisos', 'GRP#', 'GRP%', 'Impactos_Miles', 'Inversión (S/)']
        resumen_mes.to_excel(writer, sheet_name='Resumen por Mes', index=False)

        # Hoja 5: Resumen por Canal
        resumen_canal = df.groupby(['MARCA', 'CANAL']).agg({
            'SPOTS': 'sum', 'GRP_NUM': 'sum', 'GRP_PCT': 'sum',
            'Impactos_Miles': 'sum', 'INVERSION_SOLES': 'sum'
        }).reset_index()
        resumen_canal.columns = ['Marca', 'Canal', 'Total Avisos', 'GRP#', 'GRP%', 'Impactos_Miles', 'Inversión (S/)']
        resumen_canal.to_excel(writer, sheet_name='Resumen por Canal', index=False)

        _apply_excel_formatting(writer.book, '#6F42C1')  # Violeta para TV

    output.seek(0)
    return output


def get_tv_summary_stats(file_content: bytes) -> dict:
    """Devuelve estadísticas resumidas del archivo de TV."""
    df = pd.read_excel(BytesIO(file_content))
    df.columns = [str(col).strip().upper() for col in df.columns]

    column_mapping = {'CANAL/SITE': 'CANAL', 'TOTAL SPOTS': 'SPOTS', 'SUMA DE AVISOS': 'SPOTS'}
    for old_name, new_name in column_mapping.items():
        if old_name in df.columns:
            df = df.rename(columns={old_name: new_name})

    return {
        'total_filas': len(df),
        'marcas': df['MARCA'].nunique() if 'MARCA' in df.columns else 0,
        'canales': df['CANAL'].nunique() if 'CANAL' in df.columns else 0,
        'columnas': list(df.columns)
    }


def _apply_excel_formatting(workbook, accent_color: str = '#6F42C1'):
    """Aplica formato Reset a todas las hojas del workbook."""
    header_fill = PatternFill('solid', fgColor=accent_color.replace('#', ''))
    header_font = Font(bold=True, color='FFFFFF')

    for sheet_name in workbook.sheetnames:
        ws = workbook[sheet_name]
        for cell in ws[1]:
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = Alignment(horizontal='center')

        for column in ws.columns:
            max_length = 0
            column_letter = get_column_letter(column[0].column)
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            ws.column_dimensions[column_letter].width = min(max_length + 2, 40)
```

### 4.5 Schemas Pydantic

```python
# schemas/media_investment.py

from pydantic import BaseModel
from typing import List, Dict, Any, Optional


class FileStatsResponse(BaseModel):
    filename: str
    type: str  # "radio" o "tv"
    stats: Dict[str, Any]


class RankingItem(BaseModel):
    emisora: Optional[str] = None
    canal: Optional[str] = None
    ranking: Optional[float] = None
    rating: Optional[float] = None


class RadioRankingsResponse(BaseModel):
    type: str = "radio"
    cpm: Dict[str, float]
    rankings: Dict[int, Dict[str, List[RankingItem]]]
    stats: Dict[str, Any]


class TVRankingsResponse(BaseModel):
    type: str = "tv"
    cpm_por_canal: Dict[str, Dict[str, Dict[str, float]]]
    default_cpm: Dict[str, float]
    ratings: Dict[int, Dict[str, List[RankingItem]]]
    stats: Dict[str, Any]


class HealthResponse(BaseModel):
    status: str
    timestamp: str


class ErrorResponse(BaseModel):
    detail: str
```

### 4.6 Endpoints API

```python
# api/routes/media_investment.py

from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse, JSONResponse
from datetime import datetime
from io import BytesIO
import pandas as pd
import os

from app.processors.media_radio_processor import process_radio_file, get_radio_summary_stats
from app.processors.media_tv_processor import process_tv_file, get_tv_summary_stats
from app.data.media_config import (
    RANKINGS_RADIO, CPM_RADIO,
    RANKINGS_TV, CPM_TV, DEFAULT_TV_CPM
)
from app.schemas.media_investment import (
    FileStatsResponse, RadioRankingsResponse, TVRankingsResponse, HealthResponse
)

router = APIRouter(prefix="/api/media", tags=["Media Investment"])


@router.get("/health", response_model=HealthResponse)
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}


# ============== RADIO ENDPOINTS ==============

@router.post("/process/radio")
async def process_radio(file: UploadFile = File(...)):
    """Procesa archivo IBOPE y devuelve Excel con cálculos de inversión radio."""
    if not file.filename.endswith(('.xlsx', '.xls')):
        raise HTTPException(status_code=400, detail="Solo se aceptan archivos Excel (.xlsx, .xls)")

    try:
        content = await file.read()
        result = process_radio_file(content, file.filename)
        base_name = os.path.splitext(file.filename)[0]
        output_filename = f"{base_name}_INVERSION_RADIO.xlsx"

        return StreamingResponse(
            result,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={"Content-Disposition": f"attachment; filename={output_filename}"}
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error procesando archivo: {str(e)}")


@router.post("/preview/radio", response_model=FileStatsResponse)
async def preview_radio_file(file: UploadFile = File(...)):
    """Devuelve estadísticas básicas del archivo radio sin procesarlo."""
    if not file.filename.endswith(('.xlsx', '.xls')):
        raise HTTPException(status_code=400, detail="Solo se aceptan archivos Excel")

    try:
        content = await file.read()
        stats = get_radio_summary_stats(content)
        return {"filename": file.filename, "type": "radio", "stats": stats}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al leer: {str(e)}")


@router.get("/rankings/radio", response_model=RadioRankingsResponse)
async def get_radio_rankings():
    """Devuelve rankings CPI de radio organizados por año y mes."""
    rankings_organized = {}
    for (año, mes, emisora), valor in RANKINGS_RADIO.items():
        if año not in rankings_organized:
            rankings_organized[año] = {}
        if mes not in rankings_organized[año]:
            rankings_organized[año][mes] = []
        rankings_organized[año][mes].append({"emisora": emisora, "ranking": valor})

    for año in rankings_organized:
        for mes in rankings_organized[año]:
            rankings_organized[año][mes].sort(key=lambda x: x["ranking"], reverse=True)

    return {
        "type": "radio",
        "cpm": CPM_RADIO,
        "rankings": rankings_organized,
        "stats": {
            "años": sorted(rankings_organized.keys()),
            "total_registros": len(RANKINGS_RADIO),
            "emisoras_unicas": len(set(e for (_, _, e) in RANKINGS_RADIO.keys()))
        }
    }


# ============== TV ENDPOINTS ==============

@router.post("/process/tv")
async def process_tv(file: UploadFile = File(...)):
    """Procesa archivo Instar y devuelve Excel con cálculos de inversión TV."""
    if not file.filename.endswith(('.xlsx', '.xls')):
        raise HTTPException(status_code=400, detail="Solo se aceptan archivos Excel (.xlsx, .xls)")

    try:
        content = await file.read()
        result = process_tv_file(content, file.filename)
        base_name = os.path.splitext(file.filename)[0]
        output_filename = f"{base_name}_INVERSION_TV.xlsx"

        return StreamingResponse(
            result,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={"Content-Disposition": f"attachment; filename={output_filename}"}
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error procesando archivo: {str(e)}")


@router.post("/preview/tv", response_model=FileStatsResponse)
async def preview_tv_file(file: UploadFile = File(...)):
    """Devuelve estadísticas básicas del archivo TV sin procesarlo."""
    if not file.filename.endswith(('.xlsx', '.xls')):
        raise HTTPException(status_code=400, detail="Solo se aceptan archivos Excel")

    try:
        content = await file.read()
        stats = get_tv_summary_stats(content)
        return {"filename": file.filename, "type": "tv", "stats": stats}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al leer: {str(e)}")


@router.get("/rankings/tv", response_model=TVRankingsResponse)
async def get_tv_rankings():
    """Devuelve ratings de TV organizados por año y mes."""
    rankings_organized = {}
    for (año, mes, canal), valor in RANKINGS_TV.items():
        if año not in rankings_organized:
            rankings_organized[año] = {}
        if mes not in rankings_organized[año]:
            rankings_organized[año][mes] = []
        rankings_organized[año][mes].append({"canal": canal, "rating": valor})

    for año in rankings_organized:
        for mes in rankings_organized[año]:
            rankings_organized[año][mes].sort(key=lambda x: x["rating"], reverse=True)

    # Organizar CPM por canal
    cpm_por_canal = {}
    for (canal, tipo), values in CPM_TV.items():
        if canal not in cpm_por_canal:
            cpm_por_canal[canal] = {}
        cpm_por_canal[canal][tipo] = values

    return {
        "type": "tv",
        "cpm_por_canal": cpm_por_canal,
        "default_cpm": DEFAULT_TV_CPM,
        "ratings": rankings_organized,
        "stats": {
            "años": sorted(rankings_organized.keys()),
            "total_registros": len(RANKINGS_TV),
            "canales_unicos": len(set(c for (_, _, c) in RANKINGS_TV.keys()))
        }
    }


# ============== TEMPLATE DOWNLOADS ==============

@router.get("/template/radio")
async def download_radio_template():
    """Descarga plantilla Excel para Radio (IBOPE)."""
    data = {
        'MARCA': ['EMPRESA EJEMPLO', 'EMPRESA EJEMPLO', 'OTRA EMPRESA'],
        'TIPO': ['SPOT', 'MENCION', 'SPOT'],
        'EMISORA/SITE': ['RPP FM', 'MODA FM', 'RADIOMAR'],
        'MES': ['Enero', 'Enero', 'Febrero'],
        'AÑO': [2024, 2024, 2024],
        'Suma de SPOTS': [10, 5, 8]
    }
    df = pd.DataFrame(data)

    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Datos', index=False)
    output.seek(0)

    return StreamingResponse(
        output,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=Plantilla_Radio_IBOPE.xlsx"}
    )


@router.get("/template/tv")
async def download_tv_template():
    """Descarga plantilla Excel para TV (Instar)."""
    data = {
        'MARCA': ['EMPRESA EJEMPLO', 'EMPRESA EJEMPLO', 'OTRA EMPRESA'],
        'TIPO COMERCIAL': ['SPOT', 'BANNER', 'SPOT'],
        'CANAL': ['América Televisión', 'Latina', 'ATV'],
        'MES': ['Enero', 'Enero', 'Febrero'],
        'AÑO': [2024, 2024, 2024],
        'TOTAL SPOTS': [5, 3, 4],
        'DURACIÓN': [30, 15, 45],
        'GRP# [RATING]': [15.5, 8.2, 12.3],
        'GRP% [RATING]': [1.08, 0.57, 0.86]
    }
    df = pd.DataFrame(data)

    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Datos', index=False)
    output.seek(0)

    return StreamingResponse(
        output,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=Plantilla_TV_Instar.xlsx"}
    )
```

---

## 5. Mejoras a Implementar

| Problema Legacy | Solución SiReset |
|-----------------|------------------|
| Sin autenticación | Agregar `Depends(get_current_user)` en endpoints |
| CORS abierto (`*`) | Restringir a dominios SiReset |
| Datos hardcodeados | Mantener en archivo, pero estructurar para fácil actualización |
| Sin validación Pydantic | Usar schemas para request/response |
| Catch-all exceptions | Manejo específico de errores con códigos HTTP correctos |
| Color headers Excel hardcoded | Usar constantes del Design System (`#00FF85`, `#6F42C1`) |
| Frontend Vanilla JS | Migrar a React con hooks y componentes reutilizables |
| CSS custom | Usar Tailwind con clases del Design System Reset |

---

## 6. Plan de Implementación

### Día 1: Setup Backend
- [ ] Crear `data/media_config.py` con todas las configuraciones
- [ ] Crear `schemas/media_investment.py` con modelos Pydantic
- [ ] Crear estructura de carpetas `processors/`

### Día 2: Procesadores Backend
- [ ] Migrar `media_radio_processor.py` (sin cambios lógicos)
- [ ] Migrar `media_tv_processor.py` (sin cambios lógicos)
- [ ] Actualizar colores Excel al Design System Reset
- [ ] Testing unitario de fórmulas

### Día 3: API Routes
- [ ] Crear `routes/media_investment.py` con todos los endpoints
- [ ] Registrar router en `main.py`
- [ ] Agregar autenticación Supabase
- [ ] Documentación Swagger/OpenAPI

### Día 4: Frontend React
- [ ] Crear `pages/MediaInvestment.jsx` con tabs Radio/TV
- [ ] Crear `components/MediaInvestment/RadioUploader.jsx`
- [ ] Crear `components/MediaInvestment/TVUploader.jsx`
- [ ] Crear `components/MediaInvestment/RankingsModal.jsx`
- [ ] Aplicar estilos Tailwind Design System Reset

### Día 5: Integración y Testing
- [ ] Agregar ruta en `App.jsx`
- [ ] Agregar al menú/Dashboard
- [ ] Testing end-to-end con archivos reales
- [ ] Verificar que resultados coinciden con legacy
- [ ] Deploy a staging

---

## 7. Checklist Final

### Backend
- [ ] Endpoints documentados en Swagger (`/docs`)
- [ ] Validaciones con Pydantic en request/response
- [ ] Autenticación Supabase implementada
- [ ] Manejo de errores con HTTPException y códigos correctos
- [ ] Colores Excel usando Design System Reset

### Frontend
- [ ] Página responsive con tabs Radio/TV
- [ ] Upload drag & drop funcional
- [ ] Modal de rankings con filtros año/mes
- [ ] Botón descarga plantilla funcional
- [ ] Estilos Tailwind aplicados (bg-black, accent verde, violeta tablas)
- [ ] Fuentes: Bebas Neue (títulos), Montserrat (body)

### Validación Funcional
- [ ] Radio: Upload → Procesa → Descarga Excel con 5 hojas
- [ ] TV: Upload → Procesa → Descarga Excel con 5 hojas
- [ ] Rankings Radio: Modal muestra emisoras por año/mes
- [ ] Rankings TV: Modal muestra canales por año/mes
- [ ] Templates: Descargan correctamente

### Fórmulas Verificadas
- [ ] Radio: `Inversión = Spots × Ranking × CPM`
- [ ] TV SPOT: `Inversión = GRP% × CPR × Segundos`
- [ ] TV Otros: `Inversión = GRP# × CPM`

---

## 8. Notas de Mantenimiento

### Actualizar Rankings Radio (CPI)
1. Obtener nuevos datos de CPI (estudio anual)
2. Agregar entradas a `RANKINGS_RADIO` en `data/media_config.py`
3. Actualizar `MES_POR_AÑO_RADIO` si cambia el mes del estudio
4. Commit y deploy

### Actualizar Ratings TV (Instar)
1. Obtener nuevos datos de Instar (mensuales)
2. Agregar entradas a `RANKINGS_TV` en `data/media_config.py`
3. Commit y deploy

### Agregar Nuevo Canal/Emisora
1. Agregar CPM/CPR en `CPM_TV` o `CPM_RADIO`
2. Agregar rankings/ratings en diccionario correspondiente
3. El sistema usa fallbacks automáticos si falta data

---

**Documento generado:** 2026-01-07
**Herramienta:** Media Investment Calculator v2.0.0 → SiReset
