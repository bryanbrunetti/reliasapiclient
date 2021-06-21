import vcr as vcrpy
import json


def filter_keys(request):
    # Filter out all authentication type stuff
    if request.path == 'v1/authenticate':
        return None
    try:
        if request.body:
            body_json = json.loads(request.body.decode())
            if body_json.get('key') and body_json.get('token'):
                return None
    except json.decoder.JSONDecodeError:
        pass
    return request

vcr = vcrpy.VCR(
    path_transformer=vcrpy.VCR.ensure_suffix(".yaml"),
    cassette_library_dir="test/fixtures/vcr_cassettes",
    record_mode="once",
    match_on=["uri", "method"],
    filter_headers=[('Authorization', "XXXXXXOMITTEDXXXXXXX")],
    before_record_request=filter_keys
)