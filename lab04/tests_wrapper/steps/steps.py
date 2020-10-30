from behave import *
from wrapper import RoundDetail
from wrapper import RoundHole
from wrapper import SquareDetail
from wrapper import SquareDetailAdapter


@given('size of round detail - radius "{detail_size}" and size of round hole - "{hole_radius}"')
def step(context, detail_size, hole_radius):
    context.round_detail = RoundDetail(int(detail_size))
    context.hole = RoundHole(int(hole_radius))


@given('size of square detail - width "{detail_size}" and size of round hole - "{hole_radius}"')
def step(context, detail_size, hole_radius):
    context.square_detail = SquareDetail(int(detail_size))
    context.hole = RoundHole(int(hole_radius))


@then('detail and hole compatible')
def step(context):
    assert context.hole.fits(context.round_detail) == f"Деталь подходит. " \
                                                      f"Радиус детали: {context.round_detail.get_radius()}, " \
                                                      f"радиус отверстия {context.hole.get_radius()}", \
        "Тест не пройден"


@then('detail and hole incompatible')
def step(context):
    assert context.hole.fits(context.round_detail) == f"Деталь не подходит. " \
                                                      f"Радиус детали: {context.round_detail.get_radius()}, " \
                                                      f"радиус отверстия {context.hole.get_radius()}", \
        "Тест не пройден"


@then('the square detail is not comparable to the round hole')
def step(context):
    f = 0
    try:
        context.hole.fits(context.square_detail)
    except AttributeError:
        f = 1
    finally:
        assert f == 1, "Тест не пройден"


@then('detail and hole compatible after conversion via wrapper')
def step(context):
    context.adapter = SquareDetailAdapter(context.square_detail)
    assert context.hole.fits(context.adapter) == f"Деталь подходит. " \
                                                 f"Радиус детали: {context.adapter.get_radius()}, " \
                                                 f"радиус отверстия {context.hole.get_radius()}", \
        "Тест не пройден"


@then('detail and hole incompatible after conversion via wrapper')
def step(context):
    context.adapter = SquareDetailAdapter(context.square_detail)
    assert context.hole.fits(context.adapter) == f"Деталь не подходит. " \
                                                 f"Радиус детали: {context.adapter.get_radius()}, " \
                                                 f"радиус отверстия {context.hole.get_radius()}", \
        "Тест не пройден"
