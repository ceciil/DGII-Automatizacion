# features/login.feature
Feature: Funcionalidad de Inicio de Sesión de Usuario

  @login_valid
  Scenario: Verificar que un usuario puede iniciar sesión correctamente con credenciales válidas
    Given que estoy en la página de inicio de sesión
    When introduzco un nombre de usuario y contraseña válidos
    And hago clic en el botón de Login
    Then debería ser redirigido al tablero con un mensaje de bienvenida "You logged into a secure area!"
    And cierro sesión

  @login_invalid
  Scenario: Verificar que un usuario no puede iniciar sesión con credenciales no válidas
    Given que estoy en la página de inicio de sesión
    When introduzco un nombre de usuario y contraseña no válidos
    And hago clic en el botón de Login
    Then debería ver un mensaje de error "Your username is invalid!"

  @login_missing_username
  Scenario: Verificar que se muestra una alerta cuando no se proporciona el nombre de usuario
    Given que estoy en la página de inicio de sesión
    When introduzco solo la contraseña
    And hago clic en el botón de Login
    Then debería ver un mensaje de error "Your username is invalid!"