def test_if_schema_json_loads_successfully():
    from metadata.metaschema.draft07.schema import METADATA_METASCHEMA_DRAFT07_SCHEMA


def test_if_schema_json_has_correct_schema_and_id_set():
    from metadata.metaschema.draft07.schema import METADATA_METASCHEMA_DRAFT07_SCHEMA

    assert (
        METADATA_METASCHEMA_DRAFT07_SCHEMA["$schema"]
        == "http://json-schema.org/draft-07/schema#"
    )
    assert (
        METADATA_METASCHEMA_DRAFT07_SCHEMA["$id"]
        == "http://json-schema.org/draft-07/schema#"
    )