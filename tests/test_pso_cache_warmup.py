import pytest
import graphics.pso_cache_warmup as mod

CASES = [
    ("warmup_async", (1,)),
    ("variant_key", (1,)),
    ("generation_guard", (1,)),
    ("request_merge", (1,)),
    ("ref_count", (1,)),
    ("evict_idle", (1,)),
    ("determinism", (1,)),
    ("validation", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("cache_lookup", (1,)),
    ("metrics", (1,)),
    ("pipeline_create", (1,)),
    ("shader_macro", (1,)),
    ("compile", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
