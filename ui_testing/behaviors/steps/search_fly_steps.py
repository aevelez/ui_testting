from behave import *
from ui_testing.behaviors.steps.login_steps import *
from ui_testing.tests.search_fly import SearchFlyTest

test= SearchFlyTest()

@given(u'que estoy en la app mercury tours')
def step_impl(context):
    context.execute_steps(u"""
    given Estoy en la pagina de Mercury Tours 
    when Ingreso un usuario "aleno" y un password "123"
     """)
    test.setUpClass()

@when(u'busco un vuelo de "{from_port}" a "{to}" en "{service_class}" para la aerolínea "{airline}"')
def step_impl(context, from_port, to, service_class, airline):
    test.test_search('1', from_port, 'July', '3', to, 'October', '4', airline,service_class)


@then(u'Se despliega la lista de vuelos de Paris a Seattle y de Seattle a Paris')
def step_impl(context):
    test.test_image()
    test.tearDownClass()