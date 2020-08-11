from pytest import fixture


@fixture(
    params=[(1, 0), (0, 1), (-1, 0), (0, -1)],
    ids=["right", "down", "left", "up"],
)
def direction(request):
    return request.param
