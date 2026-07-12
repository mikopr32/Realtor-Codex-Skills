# Property Data Contract

## Claves

- `PROPERTY_ID`: dirección normalizada + ZIP.
- `RESEARCH_RUN_ID`: property ID + timestamp.
- `CLAIM_ID`: identificador único de observación.
- `COMP_ID`: comparable + fuente.
- `RISK_ID`: riesgo u oportunidad.
- `EVENT_ID`: evento de desempeño.

## Claim Ledger

```csv
claim_id,property_id,category,field,value,unit,status,confidence,source_url,source_title,published_date,effective_date,accessed_at,expiration_date,allowed_use,owner,conflict_id,notes
```

## Comparable Ledger

```csv
comp_id,property_id,address,status,distance_miles,sale_or_list_date,price,original_price,dom,beds,baths,sqft,year_built,lot_size,property_type,condition,community,hoa_cdd,adjustments,adjusted_indication,source,accessed_at,confidence,inclusion_reason,exclusion_reason
```

## Risk & Opportunity Register

```csv
risk_id,property_id,type,domain,finding,evidence,probability,impact,early_signal,mitigation,owner,review_date,status,confidence
```

## Performance Events

```csv
event_id,property_id,period_start,period_end,source,metric,value,unit,definition,benchmark,variance,notes
```

## Change Log

```csv
change_id,property_id,entity,field,previous_value,current_value,observed_at,source,impact,owner
```

## Approval Register

```csv
approval_id,property_id,asset_or_decision,version,status,requested_at,approved_at,approver,notes
```

## Normalization

- ISO 8601 para fechas y timestamps.
- USD salvo indicación contraria.
- Pies cuadrados y millas con unidad explícita.
- Desconocidos usan estados; nunca cero por defecto.
- Conservar dato original y normalizado.

