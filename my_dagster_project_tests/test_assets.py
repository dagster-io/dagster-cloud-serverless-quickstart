from my_dagster_project.assets import cereals


def test_cereals():
    result = cereals()
    print(result)
    assert len(result) == 77
