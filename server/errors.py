import re
import schema

from app import app, jsonify


@app.errorhandler(schema.SchemaForbiddenKeyError)
def schema_forbidden_key_error(error):
    return jsonify({"error": error.code}), 400


@app.errorhandler(schema.SchemaMissingKeyError)
def schema_missing_key_error(error):
    key_search = re.search(r"Missing key: '([^']+)'", error.code)
    keys_search = re.search(r"Missing keys: '([^']+)'", error.code)

    if key_search:
        key = key_search.group(1)
    elif keys_search:
        key = keys_search.group(1)
    else:
        key = "?"

    return jsonify({"error": f"The key '{key}' is missing."}), 400


@app.errorhandler(schema.SchemaUnexpectedTypeError)
def schema_unexcepted_type_error(error):
    return jsonify({"error": error.code}), 400


@app.errorhandler(schema.SchemaWrongKeyError)
def schema_wrong_key_error(error):
    return jsonify({"error": error.code}), 400


@app.errorhandler(schema.SchemaError)
def schema_error(error):
    return jsonify({"error": error.code}), 400
