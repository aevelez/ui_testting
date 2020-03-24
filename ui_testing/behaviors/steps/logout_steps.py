from behave import *
from ui_testing.behaviors.steps.login_steps import *
from ui_testing.tests.logout import LogoutTest

test= LogoutTest()

@given(u'Estoy en la autenticado en la pagina de Mercury Tours')
def step_impl(context):
    context.execute_steps(u"""
    given Estoy en la pagina de Mercury Tours 
    when Ingreso un usuario "aleno" y un password "123"
     """)
    test.setUpClass()


@when(u'Doy clic en SING OFF')
def step_impl(context):
    test.test_singoff()


@then(u'Regreso a la pantalla inicial')
def step_impl(context):
    test.test_logout()
    test.tearDownClass()
