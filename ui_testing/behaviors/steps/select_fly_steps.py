from behave import *
from ui_testing.behaviors.steps.search_fly_steps import *
from ui_testing.tests.select_fly import SelectFlyTest

test= SelectFlyTest()


@given(u'que he buscado un vuelo y estoy en la pagina de resultados')
def step_impl(context):
    context.execute_steps(u"""
       given que estoy en la app mercury tours 
       when busco un vuelo de "Paris" a "Seattle" en "Business" para la aerolínea "Pangea Airlines"
        """)
    test.setUpClass()


@when(u'selecciono un vuelo de ida y un vuelo de vuelta')
def step_impl(context):
    test.select_fly_test()


@then(u'Se despliega la pagina de reserva del vuelo')
def step_impl(context):
    test.test_image()
    test.tearDownClass()
