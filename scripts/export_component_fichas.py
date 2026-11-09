#!/usr/bin/env python3
"""Exporta a CSV las fichas técnicas declaradas en index.html."""
import csv
import json
import re
from pathlib import Path


HTML = Path(__file__).resolve().parents[1] / "index.html"
OUTPUT = Path(__file__).resolve().parents[1] / "data/component_fichas_evidence.csv"
source = HTML.read_text(encoding="utf-8")


def extract_array(marker):
    start = source.index(marker) + len(marker)
    depth, quote, escaped = 0, None, False
    for end in range(start, len(source)):
        char = source[end]
        if quote:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = None
            continue
        if char in ('"', "'"):
            quote = char
        elif char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
            if depth == 0:
                return source[start : end + 1]
    raise ValueError(f"No se pudo leer el catálogo {marker}")


def parse_array(text, javascript=False):
    if javascript:
        result, quote, escaped = [], None, False
        for char in text:
            if quote == "'":
                if escaped:
                    result.append("\\" + char)
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == "'":
                    result.append('"')
                    quote = None
                else:
                    result.append('\\"' if char == '"' else char)
            elif quote == '"':
                result.append(char)
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == '"':
                    quote = None
            elif char == "'":
                result.append('"')
                quote = "'"
            else:
                result.append(char)
        text = re.sub(
            r"([,{]\s*)([A-Za-z_$][\w$]*)(\s*:)" , r'\1"\2"\3', "".join(result)
        )
    text = re.sub(r",\s*([}\]])", r"\1", text)
    return json.loads(text)


sections = parse_array(extract_array("const technicalSections="))
breakdowns = parse_array(extract_array("const illustratedBreakdowns="))
nxi = parse_array(extract_array("const nxiEquipment="), javascript=True)
source_block = source.split("const technicalSources={", 1)[1].split("\n};", 1)[0]
technical_sources = {
    key: (title, url)
    for key, title, url in re.findall(
        r"^\s{2}(\w+):\['([^']*)','([^']*)'\]", source_block, re.MULTILINE
    )
}
items = [
    {**item, "section": section}
    for section in sections
    for item in section["items"]
]
items_by_id = {item["id"]: item for item in items}
for breakdown in breakdowns:
    section = items_by_id[breakdown["parent"]]["section"]
    for item_id, name, description in breakdown["parts"]:
        item = {
            "id": item_id,
            "name": name,
            "description": description,
            "section": section,
            "parent": breakdown["parent"],
            "breakdown": breakdown,
        }
        items.append(item)
        items_by_id[item_id] = item
avionics = next(section for section in sections if section["id"] == "avionics")
items.extend({**item, "section": avionics, "nxi": True} for item in nxi)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
with OUTPUT.open("w", encoding="utf-8-sig", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(
        [
            "id", "ficha", "grupo", "descripcion", "modelo_o_zona", "fuentes_app",
            "fuentes_titulo_url",
            "evidencia_general", "geometria_local", "aplicabilidad_por_matricula",
            "estado_verificacion", "pagina_ipc", "figura_ipc",
        ]
    )
    for item in items:
        source_keys = item.get("sources", item["section"].get("sources", []))
        if item.get("nxi"):
            geometry = "Esquema didáctico NXi; no malla 3D validada por matrícula"
            evidence = "E2; E1 solo para contexto de flota"
        elif item.get("mesh"):
            geometry = "Referencia visual GLB FlightGear C172P; no equivale a geometría C172S/FAC"
            evidence = "E2; E3/E5 según tipo de ficha"
        elif item.get("breakdown"):
            geometry = "Despiece referenciado en IPC; sin malla individual confirmada"
            evidence = "E2"
        else:
            geometry = "Representación conceptual o funcional; aplicación por serie no confirmada"
            evidence = "E2; E3/E5 según tipo de ficha"
        breakdown = item.get("breakdown", {})
        writer.writerow(
            [
                item["id"], item.get("name", ""), item["section"].get("name", ""),
                item.get("description", ""), item.get("model", item.get("zone", "")),
                " | ".join(source_keys),
                " | ".join(
                    f"{technical_sources[key][0]} — {technical_sources[key][1]}"
                    for key in source_keys if key in technical_sources
                ),
                evidence, geometry,
                "Pendiente de verificar contra serial, IPC/WDM y lista de equipo FAC",
                "Referencia de despiece; no valida instalación FAC" if breakdown else "Didáctico; no validado por matrícula",
                breakdown.get("page", ""), breakdown.get("figure", ""),
            ]
        )
print(f"Exportadas {len(items)} fichas a {OUTPUT}")
