# app/services/validator_service.py

def validate_results(results):
    final = {}

    for field in ["CEO", "Founded", "Headquarters"]:
        values = [r.get(field, "Unknown") for r in results]
        values = [v for v in values if v != "Unknown"]

        final[field] = max(set(values), key=values.count) if values else "Unknown"

    return final