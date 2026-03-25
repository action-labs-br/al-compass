# Data Dictionary — accidents.csv

This document describes every column in the `accidents.csv` dataset. The data contains ~60,000 accident records from Brazilian federal highways, collected by the PRF (Policia Rodoviaria Federal).

---

## Temporal

| Column | Type | Description |
|--------|------|-------------|
| `date` | string | Date of the accident (YYYY-MM-DD) |
| `day_of_week` | string | Day of week in Portuguese (Segunda, Terca, Quarta, Quinta, Sexta, Sabado, Domingo) |
| `hour` | int | Hour of day (0-23) |
| `time_of_day` | string | Period of the day (Pleno dia, Plena noite, Amanhecer, Anoitecer) |

## Geographic

| Column | Type | Description |
|--------|------|-------------|
| `state` | string | Brazilian state abbreviation (e.g. MG, SP, PR) |
| `highway` | string | Federal highway code (e.g. BR-116, BR-101) |
| `km_marker` | float | Kilometer marker on the highway |
| `municipality` | string | City or municipality name |
| `latitude` | float | Latitude coordinate of the accident location |
| `longitude` | float | Longitude coordinate of the accident location |

## Accident Details

| Column | Type | Description |
|--------|------|-------------|
| `accident_cause` | string | Reported cause category (e.g. Falta de atenção, Velocidade incompatível) |
| `accident_type` | string | Type of collision (e.g. Colisão traseira, Saída de leito carroçável, Capotamento) |
| `vehicles_involved` | int | Number of vehicles involved in the accident |

## Road Conditions

| Column | Type | Description |
|--------|------|-------------|
| `weather` | string | Weather conditions at the time (Céu Claro, Chuva, Nublado, Sol, Nevoeiro/Neblina, Vento, Granizo) |
| `road_type` | string | Road classification (Simples, Dupla, Múltipla) |
| `road_geometry` | string | Road geometry at the accident site (Reta, Curva, Interseção de vias, Desvio temporário, Rotatória, Retorno regulamentado) |
| `road_direction` | string | Direction of traffic flow (Crescente, Decrescente, Não informado) |
| `land_use` | string | Land use classification of the area (Rural, Urbano) |

## Outcome Counts

| Column | Type | Description |
|--------|------|-------------|
| `people_involved` | int | Total number of people involved in the accident |
| `deaths` | int | Number of deaths at the scene |
| `serious_injuries` | int | Number of people with serious injuries |
| `minor_injuries` | int | Number of people with minor injuries |
| `uninjured` | int | Number of uninjured people |
| `unknown_status` | int | Number of people with unknown injury status |
| `total_injuries` | int | Total number of injuries (serious + minor) |

## Target

| Column | Type | Description |
|--------|------|-------------|
| `is_fatal` | bool | Whether the accident resulted in at least one death (True/False) |
