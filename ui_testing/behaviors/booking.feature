Feature: Realiza reserva de vuelos

  Scenario:
    Given que he seleccionado un vuelo de ida y vuelta
    When ingreso la información personal
    And Ingreso la información de medio de pago
    And ingreso la dirección de facturación
    And ingreso la dirección de entrega
    And Selecciono comprar vuelo
    Then el vuelo queda reservado
    And se genera un código de reserva