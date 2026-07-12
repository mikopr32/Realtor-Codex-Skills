# Data Contract

## Claves

- `CITY_RESEARCH_ID`: estado-ciudad-fecha.
- `BUILDER_ID`: slug canónico del builder.
- `COMMUNITY_ID`: builder + comunidad + ciudad legal.
- `PHASE_ID`: comunidad + fase o colección.
- `MODEL_ID`: builder + comunidad/colección + modelo.
- `INVENTORY_ID`: builder + dirección/lote.
- `CLAIM_ID`: identificador único del dato observado.

## Columnas comunes

Toda tabla factual debe incluir, cuando aplique:

```csv
city_research_id,builder_id,community_id,phase_id,entity_type,entity_name,field,value,unit,status,confidence,source_url,source_title,published_date,effective_date,expiration_date,accessed_at,notes
```

## Builders y comunidades

```csv
builder_id,builder_name,builder_type,community_id,community_name,legal_city,marketed_city,county,state,zip,status,property_types,price_from,model_count,qmi_observed,cdd_status,cdd_amount,cdd_frequency,hoa_status,hoa_amount,hoa_frequency,amenities_summary,incentive_summary,last_verified,confidence,official_url
```

## Modelos

```csv
model_id,builder_id,community_id,phase_id,model_name,collection,property_type,stories,beds_min,beds_max,baths_min,baths_max,garage_min,garage_max,sqft_min,sqft_max,base_price,price_status,official_url,observed_at,confidence
```

## Quick move-ins

```csv
inventory_id,builder_id,community_id,phase_id,address_or_lot,model_name,price_current,price_previous,visible_reduction,beds,baths,garage,sqft,construction_status,estimated_completion,incentive_id,official_url,observed_at,availability_disclaimer,confidence
```

## Incentivos

```csv
incentive_id,builder_id,community_id,inventory_id,incentive_type,headline,value,eligibility,lender_required,title_required,loan_type,contract_deadline,closing_deadline,expiration_date,terms_status,official_url,observed_at,confidence
```

## Change Log

```csv
change_id,entity_type,entity_id,field,previous_value,current_value,change_type,previous_observed_at,current_observed_at,source_url,impact,confidence
```

## Verification Queue

Cada pendiente incluye prioridad `P0` a `P3`, entidad, dato, razón, búsquedas realizadas, fuente sugerida, owner y próximo paso. `P0` altera identidad o geografía; `P1` altera precio/costo/incentivo; `P2` altera producto/amenidad; `P3` es enriquecimiento.

## Reglas

- Fechas ISO 8601; timestamps con zona horaria.
- Dinero en USD salvo indicación contraria.
- Frecuencia nunca implícita.
- Celdas desconocidas usan estados normalizados, no ceros.
- Conservar texto promocional solo como resumen breve y enlazar la fuente.

