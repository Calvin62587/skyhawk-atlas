# Skyhawk Atlas — guía didáctica interactiva

## Abrir el MVP

Abre `index.html` en Safari, Chrome o Firefox. El HTML lleva incorporados Three.js, sus controles y lector glTF, además de la geometría del avión: no requiere servidor ni conexión para cargar el modelo. El archivo fuente `c172-reference.glb`, su licencia y el manifiesto permanecen junto a la aplicación para poder inspeccionarlos. La atribución MIT del código Three.js incluido se conserva en `THREE-LICENSE.txt`.

Para consultar fotografías de unidades FAC, el dibujo dimensional del 172S y referencias de fabricante, abre el botón **Galería visual** en la cabecera de Atlas o [`galeria-referencias-c172.html`](galeria-referencias-c172.html). Esa galería carga las fotos desde las publicaciones de origen y necesita conexión; los derechos y créditos siguen siendo de sus titulares. El 3D y los diagramas locales del curso no dependen de esas imágenes.

La investigación del proceso de compra y las referencias **4700019976**, **CTO 119/22** y **149/22-4700019976** está en [`contrato-fac-cessna-172s-investigacion.md`](contrato-fac-cessna-172s-investigacion.md). El contrato firmado y la configuración por número de serie siguen pendientes de acceso al anexo y a la lista de equipos.

El paquete de resultados y los datos importables están en [`research/investigacion-gemelo-digital-cessna-172s.md`](research/investigacion-gemelo-digital-cessna-172s.md) y en [`data/`](data/): registro de evidencia E1–E5, matrículas/seriales, fuentes de geometría y manuales, y exportación de las fichas actuales. Los seriales sin respaldo público quedan vacíos. Los manuales con derechos controlados y las fotos de terceros se enlazan, no se redistribuyen. Para regenerar el catálogo de fichas: `python3 scripts/export_component_fichas.py`.

## Para empezar desde cero

La **Ruta de aprendizaje** reúne 42 lecciones en seis etapas. Cubre aeronave y limitaciones, sistemas interrelacionados, operación normal, emergencias, navegación y G1000 NXi, y evaluación interna. Cada lección indica un objetivo, su posición y la siguiente lección.

La **Biblioteca de vuelo** reúne 28 accesos por tarea, con búsqueda por palabras y filtro por cinco temas. Por ejemplo, «presión estática» lleva al circuito y sus fichas, «Direct-To» abre la práctica y «61.87» abre las referencias FAA. Los accesos de inventario de piezas y mapa de cabina también están disponibles desde la barra lateral.

Los diagramas conectan mando, transmisión, alimentación, sensor e indicación. Las prácticas incluyen interpretación del POH/AFM, cálculo ficticio de centrado, revisión de performance, planificación del vuelo y decisiones por fase. Cuatro escenarios guiados permiten ensayar pérdida de potencia, aviso de CO, datos de aire inválidos y desvío por meteorología.

El laboratorio G1000 NXi contiene cuatro misiones con datos ficticios. El alumno edita y verifica un plan, selecciona un tramo, activa un Direct-To sin borrar el plan, transfiere COM y comprueba el CDI, y distingue carga y activación de un procedimiento. Los pasos se complementan con el mapa de cabina y la guía Garmin. El alumno practica los mandos y las funciones completas en un entrenador compatible bajo supervisión.

La evaluación de 15 preguntas muestra el resultado y enlaza cada respuesta errónea a su lección. El criterio didáctico es alcanzar el 80 % y acertar todas las preguntas críticas. La fase concluye con una demostración oral y práctica que revisa el instructor según los criterios de la escuela.

Al elegir una pieza, el visor la encuadra y muestra su ficha. **Separar conjuntos** lleva la separación al 100 %. Desde **Conjunto** puedes abrir una bandeja por sistema. Las piezas del grupo se distribuyen sin solaparse en planta, con marcadores numerados y un selector **Pieza** que también funciona por teclado. **Encuadrar bandeja** recupera la vista completa del grupo y **Reunir** devuelve las mallas a su posición original.

**Instalaciones internas** presenta 65 elementos didácticos seleccionables con el contorno del avión como referencia. Incluye guayas y transmisión de mandos, actuador de flaps, servos de alabeo y cabeceo cuando se instala GFC 700, mazos eléctricos, enlaces de aviónica, conductos pitot y estáticos, líneas hidráulicas de freno, alimentación, retorno, venteo y ramales de inyección, así como elementos de lubricación y calefacción. El grosor de las líneas y las posiciones son aproximaciones visuales.

La parte operativa incluye preparación, arranque, carreteo, vuelo, maniobras, aterrizaje y parada. La revisión FAA amplió el curso con normativa y responsabilidad, interpretación de METAR y TAF, aptitud del piloto, aeródromo y radiotelefonía, prevención de barrena, vuelo nocturno y referencias instrumentales.

Las fichas distinguen identificaciones relativamente claras de nombres ambiguos del modelo. En las piezas dudosas se conserva el identificador original y se expresa la función como probable o pendiente de confirmar. El catálogo distingue 205 instancias de malla del C172P y 65 elementos funcionales añadidos del C172S.

## Inventario técnico y cabina NAV III

**Inventario técnico** reúne 245 fichas de los ocho grupos según el catálogo actual de `index.html`. Cada ficha identifica el componente, explica su función y enlaza sus fuentes. **Ver en el GLB C172P** señala una malla original. **Ver trazado didáctico** señala una representación funcional añadida. Una ficha de conjunto puede enlazar su mando visible aunque el cuerpo interno solo esté documentado. **Ver piezas del conjunto** muestra los despieces incorporados y cada ficha enlaza a su figura del IPC, con regreso al conjunto.

**Cabina NAV III** muestra la fotografía del fabricante del panel Skyhawk con Garmin G1000 NXi y reserva digital GI 275. Incluye 18 marcadores y ampliación. Los marcadores corresponden al panel fotografiado, cuya configuración debe cotejarse con la matrícula FAC. **Circuitos** muestra recorridos funcionales y **Localizar tubo pitot** encuadra la sonda bajo el ala izquierda. [Cessna Skyhawk · Textron Aviation](https://cessna.txtav.com/en/piston/cessna-skyhawk)

La comprobación de todos los números de pieza requiere número de serie de célula y motor, lista de equipo de la unidad, IPC 172RPC vigente, WDM 172RWD, manual 172RMM, suplementos y planos de instalación aplicables. El POH y las guías Garmin documentan configuraciones de referencia. El IPC identifica piezas y aplicabilidad, y el GLB C172P aporta geometría seleccionable. Son niveles distintos de evidencia.

- [Cessna NAV III, POH y figuras de sistemas](https://www.norcalflight.com/pdfs/poh/POH_C172S_Nav_III.pdf)
- [Garmin G1000 NXi NAV III, guía de piloto](https://static.garmin.com/pumac/190-02177-03_a.pdf)
- [Lycoming, IPC del IO-360-L2A](https://www.lycoming.com/publications/io-360-l2a-illustrated-parts-catalog)
- [Textron, publicaciones técnicas 1View](https://ww2.txtav.com/TechnicalPublications)
- [NTSB, extracto del despiece Cessna del tren de nariz](https://data.ntsb.gov/Docket/Document/docBLOB?FileExtension=pdf&FileName=NLG+IPC+excerpt-Rel.pdf&ID=16495954)

Al seleccionar **Aviónica e instrumentos**, se abre la referencia **Garmin G1000 NXi**. Incluye 23 fichas de pantallas, unidades remotas, sensores, interconexión y equipos opcionales. Al elegir **Garmin G1000 NXi**, **Cabina** o **Circuitos**, el visor central muestra el esquema correspondiente. Seleccionar un componente resalta su posición o recorrido y actualiza su ficha. **Ver avión 3D** vuelve a la maqueta C172P. Los esquemas NAV III representan la disposición y función de referencia sin escala. Las fichas NXi representan la configuración descrita en las guías de Garmin y Textron. El 172S de la FAC está documentado y hay reportes del NXi en unidades recientes. Los equipos opcionales, versiones y módulos exactos quedan por confirmar mediante la lista de equipo y suplementos de cada matrícula.

## Inspección y límites del GLB

El GLB 2.0 tiene 226 nodos, 204 definiciones de malla y 205 instancias/primitivas. Las extensiones y bounds se documentan en `c172-reference-manifest.json`. Sus extensiones geométricas aproximadas son X 8.233, Y 2.458 y Z 11.320 unidades del modelo; **no son dimensiones aeronáuticas**. La orientación se infiere como eje longitudinal X, vertical Y y envergadura Z, según posiciones y nombres. Es una inferencia, no una especificación de coordenadas certificada.

La fuente identifica el avión como un **Cessna 172P derivado de FlightGear**, con licencia GPL-2.0, no un C172S. La maqueta permite enseñar formas y principios generales, pero no demuestra geometría, motor, aviónica, equipamiento o procedimientos de un 172S específico. Algunas piezas proceden de nombres de escena que pueden ser genéricos, heredados o ambiguos.

## Uso educativo

Este recurso sirve para familiarización visual y conceptos iniciales. No sustituye al instructor, el POH/AFM vigente del avión de matrícula concreta, sus suplementos ni las listas de comprobación aprobadas. No debe emplearse para operación, mantenimiento, inspección, planificación de peso y balance o decisiones de aeronavegabilidad.

**Alcance y referencias FAA** relaciona los temas con el ACS de piloto privado de avión e identifica las áreas que deben completarse con instrucción. Distingue el estudio y la instrucción registrada de la Parte 61 del currículo aprobado de una escuela bajo Parte 141. La evaluación de Atlas es interna, sin crédito de horas, certificación ni endoso para vuelo solo. Para la FAC u otra jurisdicción rigen los requisitos y procedimientos que correspondan a esa operación.

- [14 CFR §§ 61.105 y 61.107 · Conocimientos y competencia de vuelo](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-D/part-61/subpart-E)
- [14 CFR § 61.87 · Vuelo solo del alumno](https://www.ecfr.gov/current/title-14/section-61.87)
- [14 CFR Parte 141, apéndice B · Curso de certificación de piloto privado](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-H/part-141/appendix-Appendix%20B%20to%20Part%20141)
- [FAA-S-ACS-6C · Piloto privado de avión](https://www.faa.gov/training_testing/testing/acs/private_airplane_acs_6.pdf)

## Seguridad y disponibilidad

El HTML funciona localmente. La política de seguridad permite únicamente los scripts incorporados identificados por sus huellas SHA-256 y limita las conexiones a las texturas locales temporales del visor. El lector del modelo rechaza referencias externas y los nombres de malla se tratan como texto. Los enlaces de consulta se abren por decisión del usuario y sin enviar la página de origen. Al modificar un bloque de script es necesario regenerar su huella en la política del encabezado.

Si el navegador carece de WebGL, las lecciones, la biblioteca, las fichas y los laboratorios siguen disponibles. Restablecer el visor conserva la actividad abierta. Las animaciones de las lecciones se reproducen a petición y el visor ofrece vistas predefinidas seleccionables con el teclado.

## Fuentes verificables

- [Créditos, licencia y descarga de la geometría](https://theflightplaybook.com/credits/)
- [Repositorio fuente C172P de FlightGear](https://github.com/c172p-team/c172p)
- [FAA — Pilot’s Handbook of Aeronautical Knowledge](https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/phak)
- [FAA — Instrument Flying Handbook (altimetría)](https://www.faa.gov/sites/faa.gov/files/regulations_policies/handbooks_manuals/aviation/FAA-H-8083-15B.pdf)
- [FAA — Airplane Flying Handbook](https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/airplane_handbook)
- [Lycoming — IO-360-L2A](https://www.lycoming.com/engines/10017)
- [POH/AFM C172S NAV III, ejemplo de configuración y serie](https://www.camarilloairport.com/downloads/N577ND_AFM-POH.pdf). No es el POH/AFM de la aeronave de la escuela.
- [FAA Type Certificate Data Sheet 3A12](https://drs.faa.gov/browse/excelExternalWindow/038B3F7D7FEEC0EB8625796D0069D3A9.0001?modalOpened=true)

Para convertir la maqueta en una representación fiel del C172S de la FAC hacen falta geometría autorizada de esa variante y documentación técnica/equipo vinculada a sus números de serie. Hasta entonces, el modelo, asignaciones y fichas se presentan como material didáctico de referencia con límites explícitos.
