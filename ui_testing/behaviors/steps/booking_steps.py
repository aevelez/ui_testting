from behave import *
from ui_testing.behaviors.steps.select_fly_steps import *
from ui_testing.tests.booking import BookingFlyTest

test= BookingFlyTest()


@given(u'que he seleccionado un vuelo de ida y vuelta')
def step_impl(context):
    context.execute_steps(u"""
        given que he buscado un vuelo y estoy en la pagina de resultados 
        when selecciono un vuelo de ida y un vuelo de vuelta
        """)
    test.setUpClass()


@when(u'ingreso la información personal')
def step_impl(context):
    test.fillPersonalInformation()


@when(u'Ingreso la información de medio de pago')
def step_impl(context):
    test.fillCreditCard()


@when(u'ingreso la dirección de facturación')
def step_impl(context):
    test.fillBillingAddress()


@when(u'ingreso la dirección de entrega')
def step_impl(context):
    test.fillDeliveryAddress()


@when(u'Selecciono comprar vuelo')
def step_impl(context):
    test.purchaseFly()


@then(u'el vuelo queda reservado')
def step_impl(context):
    test.test_image()


@then(u'se genera un código de reserva')
def step_impl(context):
    test.test_image()
    test.tearDownClass()

