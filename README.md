# Controlador-de-Carro

![Guante 2](https://github.com/Controlador-de-Carro/Dumentacion/assets/137660800/c04cb2fd-abce-4831-8a05-7f9c9ad1725a)

# Integrantes
Alejandro Valero<br />
Jonathan Ducuara<br />
Camilo Torres<br />

# Descripción del Proyecto
Este proyecto busca poder controlar un carro a control remoto por medio de conexión inalambrica y el movimiento de la mano. 

PROBLEMÁTICA:<br />
- Actualmente, el manejo de carros a control remoto mediante mandos o aplicaciones móviles puede resultar poco intuitivo y difícil de dominar para muchas personas. Los controles convencionales, como los mandos con múltiples botones o las interfaces de aplicaciones móviles, pueden presentar barreras de entrada para aquellos que no están familiarizados con ellos. Esto puede llevar a una experiencia frustrante y limitar el disfrute y la eficiencia en el manejo de los carros a control remoto.

ALCANCE:<br />
- El guante con sensores de movimiento proporcionaría una experiencia más intuitiva y natural para los usuarios, lo que facilitaría el aprendizaje y el manejo del carro a control remoto.
- La solución permitiría una mayor precisión en los movimientos y una mejor maniobrabilidad del carro. Los gestos y movimientos naturales de la mano y la muñeca ofrecerían una mayor sensibilidad y control en comparación con los controles convencionales.
- El uso del guante con sensores de movimiento brindaría una experiencia más inmersiva y gratificante al manejar el carro a control remoto. Los usuarios sentirían una mayor conexión con el dispositivo y podrían disfrutar plenamente de la experiencia de conducción.

OBJETIVOS:<br />
- Diseñar un guante con sensores de movimiento intuitivo: El objetivo principal es desarrollar un guante con sensores de movimiento que sea intuitivo y fácil de usar para el control de carros a control remoto. El diseño del guante se centrará en capturar los gestos y movimientos naturales de la mano y la muñeca, proporcionando una experiencia de manejo más intuitiva y fluida.
- Simplificar la curva de aprendizaje: Se buscará simplificar la curva de aprendizaje para los usuarios nuevos o poco experimentados en el manejo de carros a control remoto. El guante intuitivo y fácil de usar reducirá la frustración y permitirá a los usuarios aprender rápidamente las técnicas de control necesarias para operar los carros de forma efectiva.
- Promover una experiencia de usuario satisfactoria: El objetivo es proporcionar a los usuarios una experiencia de usuario satisfactoria y gratificante al controlar los carros a control remoto. El guante con sensores de movimiento mejorará la interacción y la conexión entre el usuario y el carro, lo que aumentará el disfrute y el compromiso del usuario durante el manejo del dispositivo.

# Diagrama de Flujo de la Solución
DIAGRAMA DE FLUJO:
![Diagrama en blanco](https://github.com/Controlador-de-Carro/Dumentacion/assets/137632667/5792136f-9b92-474c-9dac-3117a216cd4a)

DIAGRAMA DE CAJA NEGRA SIN LA TECNOLOGÍA
![Diagrama de caja negra sin tecnologia](https://github.com/Controlador-de-Carro/Dumentacion/assets/137632667/6ef0f93f-aa9b-47e0-b6d4-f3838f4a8224)

DIAGRAMA DE CAJA NEGRA CON LA TECNOLOGÍA
![Caja Negra con tecnología](https://github.com/Controlador-de-Carro/Dumentacion/assets/137632667/8e5d4a00-8542-46d7-b5b0-7811dbd693c8)

# Imagenes de los diseños realizados en el tablero del salón

Circuito propuesto: ![Tablero TEB 1](https://github.com/Controlador-de-Carro/Dumentacion/assets/137660800/ab082287-abfb-4442-82b4-f190a1d138b9)


# Implementación

PCB: Fue hecha mediante el programa proteus 8, las complicaciones se presentaron al no haber librerias ni de la ESP32 ni del giroscopio MPU-6050, por lo que se hicieron las respectivasm mediciones de los pines para poder fabricar esta, ademas en el PDF se muestra en forma espejo ya que asi se manda a imprimir para que la serigrafia quede bien, con esta nos podemos guiar de la posición de los pines. Tambien se adjuntan las imagenes del ruteo y el diseño en 3D.
[PCB FINAL.PDF](https://github.com/Controlador-de-Carro/Dumentacion/files/11861697/PCB.FINAL.PDF). ![Captura de pantalla 2023-06-25 205715](https://github.com/Controlador-de-Carro/Dumentacion/assets/137660800/14a0acb3-7d7d-4fd1-b494-d941a09cea24). ![Captura de pantalla 2023-06-25 205658](https://github.com/Controlador-de-Carro/Dumentacion/assets/137660800/02e1e8d5-5f4d-42ca-8107-ab8cb8aa46b4)

# Evidencias de implementación y desarrollo del proyecto
Circuito ![Circuito](https://github.com/Controlador-de-Carro/Dumentacion/assets/137660800/0c20bc43-397f-4015-8f74-cb7ec915a10c)

Probando el código del giro del dispositivo rotando en los diferentes ejes<br />
https://github.com/Controlador-de-Carro/Dumentacion/assets/137632667/93d23020-855f-4cdd-9650-059f637b97df

