import pytest
from prog_python.experiments.tests.libs.diff_validations import \
    compare_old_new_tenor


@pytest.mark.parametrize("old_tenor, new_tenor", [
    ("_ON", "TOD_TOM"),
    ("TS", "TOM_SPT")
])
def test_tenor_replacement(old_tenor, new_tenor):
    """
    Make sure, that old tenor were changed correctly to te new one.
        _ON -> TOD_TOM
         TS -> TOM_SPT
    """
    errors = compare_old_new_tenor(old_tenor, new_tenor)
    assert len(errors) == 0, f"Diffs were found in lines: {errors}"
