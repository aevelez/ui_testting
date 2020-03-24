from behave import *
from ui_testing.behaviors.steps.login_steps import *
from ui_testing.tests.search_fly import SearchFlyTest

test= SearchFlyTest()


@given(u'Estoy en la autenticado en la pagina')
def step_impl(context):
    context.execute_steps(u"""
    given Estoy en la pagina de Mercury Tours 
    when Ingreso un usuario "aleno" y un password "123"
     """)
    test.setUpClass()


@when(u'Lleno el formulario de busqueda')
def step_impl(context):
    test.test_search()
    test.tearDownClass()


@then(u'Voy a la pagina de resultados')
def step_impl(context):
    test.test_image()
