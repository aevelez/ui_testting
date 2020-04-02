Feature: Buscar un vuelo

   Scenario:
    Given que estoy en la app mercury tours
    When busco un vuelo de "Paris" a "Seattle" en "Business" para la aerolínea "Blue Skies Airlines"
    Then Se despliega la lista de vuelos de Paris a Seattle y de Seattle a Paris