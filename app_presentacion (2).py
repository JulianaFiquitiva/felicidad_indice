"""
Presentación del proyecto — Agente de IA para el Índice de Bienestar/Felicidad Estudiantil (USTA)
Materia: Consultoría e Investigación · Docente: Javier Mauricio Sierra
Ejecutar con:  streamlit run app_presentacion.py
"""

import streamlit as st

st.set_page_config(
    page_title="Agente IA - Índice de Bienestar Estudiantil USTA",
    page_icon="📊",
    layout="wide",
)

# ---------------------------------------------------------------
# ESTILOS
# ---------------------------------------------------------------
FLOW_CSS = """
<style>
.flow-wrap { display: flex; flex-wrap: wrap; align-items: center; gap: 6px; margin: 14px 0 22px 0; }
.flow-box {
    background: #1e293b; border: 1px solid #3b82f6; border-radius: 10px;
    padding: 12px 16px; color: #e2e8f0; font-size: 14px; min-width: 150px;
    text-align: center; line-height: 1.3;
}
.flow-box small { color: #94a3b8; }
.flow-arrow { color: #3b82f6; font-size: 22px; padding: 0 2px; }
.loop-box {
    background: #1e293b; border: 2px solid #a855f7; border-radius: 12px;
    padding: 14px 16px; color: #e2e8f0; font-size: 14px; min-width: 150px;
    text-align: center; line-height: 1.3;
}
.loop-box small { color: #c4b5fd; }
.loop-arrow { color: #a855f7; font-size: 22px; padding: 0 2px; }
.layer-card {
    background: #111827; border: 1px solid #334155; border-left: 5px solid #3b82f6;
    border-radius: 10px; padding: 14px 16px; margin-bottom: 12px;
}
.layer-title { color: #93c5fd; font-weight: 700; margin-bottom: 6px; }
.layer-item { color: #e2e8f0; font-size: 13.5px; margin: 2px 0; }
.concept-card {
    background: #111827; border: 1px solid #334155; border-left: 5px solid #a855f7;
    border-radius: 10px; padding: 14px 16px; margin-bottom: 12px;
}
.concept-title { color: #d8b4fe; font-weight: 700; margin-bottom: 6px; }
.concept-item { color: #e2e8f0; font-size: 13.5px; margin: 2px 0; }
.risk-solved { color: #4ade80; font-weight: 600; }
.risk-residual { color: #fbbf24; font-weight: 600; }
.rubric-badge {
    display:inline-block; background:#312e81; color:#c7d2fe; font-size:12px;
    font-weight:700; padding:3px 10px; border-radius:999px; margin-bottom:10px;
}
.pending-card {
    background:#1c1410; border:1px solid #a16207; border-left:5px solid #eab308;
    border-radius:10px; padding:12px 16px; margin:10px 0; color:#fde68a; font-size:13.5px;
}
</style>
"""
st.markdown(FLOW_CSS, unsafe_allow_html=True)


def flow_diagram(steps, style="flow"):
    box_cls = "loop-box" if style == "loop" else "flow-box"
    arrow_cls = "loop-arrow" if style == "loop" else "flow-arrow"
    html = '<div class="flow-wrap">'
    for i, (title, sub) in enumerate(steps):
        html += f'<div class="{box_cls}">{title}'
        if sub:
            html += f'<br><small>{sub}</small>'
        html += "</div>"
        if i < len(steps) - 1:
            html += f'<div class="{arrow_cls}">➜</div>'
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


def layer_card(title, items):
    html = f'<div class="layer-card"><div class="layer-title">{title}</div>'
    for it in items:
        html += f'<div class="layer-item">• {it}</div>'
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


def concept_card(title, items):
    html = f'<div class="concept-card"><div class="concept-title">{title}</div>'
    for it in items:
        html += f'<div class="concept-item">• {it}</div>'
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


def rubric_badge(text):
    st.markdown(f'<span class="rubric-badge">{text}</span>', unsafe_allow_html=True)


def pending(text):
    st.markdown(f'<div class="pending-card">⏳ <strong>Pendiente de conseguir con la contraparte:</strong> {text}</div>', unsafe_allow_html=True)


# ---------------------------------------------------------------
# SIDEBAR — NAVEGACIÓN EN DOS PARTES
# ---------------------------------------------------------------
st.sidebar.title("📊 Agente IA — Bienestar Estudiantil")
st.sidebar.caption("USTA · Consultoría e Investigación · Prof. Javier Mauricio Sierra")

parte = st.sidebar.radio(
    "Parte de la presentación",
    ["Parte 1 · El agente de IA", "Parte 2 · El proyecto de consultoría"],
)
st.sidebar.divider()

if parte == "Parte 1 · El agente de IA":
    seccion = st.sidebar.radio(
        "Sección",
        [
            "0. Portada",
            "1. ¿Qué es un agente de IA?",
            "2. Qué hace el agente",
            "3. Cómo funciona el agente",
            "4. Resultados que muestra",
        ],
    )
else:
    seccion = st.sidebar.radio(
        "Sección",
        [
            "5. Contraparte y necesidad",
            "6. Diseño y configuración",
            "7. Implementación técnica y entorno",
            "8. Valor agregado y pruebas",
            "9. Riesgos del dominio",
            "10. Sustentación — qué nos van a preguntar",
            "11. Próximos pasos",
        ],
    )

# =================================================================
# PARTE 1
# =================================================================

if seccion == "0. Portada":
    st.title("Agente de IA para el Índice de Bienestar Estudiantil")
    st.subheader("Universidad Santo Tomás · Continuación del proyecto de Índice de Felicidad")

    col1, col2, col3 = st.columns(3)
    col1.metric("Respuestas del estudio previo", "1.813")
    col2.metric("Población objetivo aprox.", "29.950")
    col3.metric("Ítems tipo Likert", "29")

    st.markdown(
        """
        Este proyecto **no levanta una encuesta nueva**: retoma el estudio de
        bienestar estudiantil ya realizado en la USTA y construye sobre él un
        **agente de inteligencia artificial** que valida, analiza y permite
        consultar esos resultados de forma reproducible y trazable.

        **Contraparte:** el equipo de estudiantes que hizo el estudio anterior,
        y la universidad — que necesita una herramienta para seguir analizando
        esta información sin repetir el proceso manual cada vez.
        """
    )
    st.info("Entrega — Materia de Consultoría e Investigación · Consultoría de 3 semanas · 20 % del corte.")

elif seccion == "1. ¿Qué es un agente de IA?":
    st.title("1. ¿Qué es un agente de IA?")
    st.caption("Los conceptos que sostienen todo lo demás en esta presentación")

    st.markdown("## 1.1 Definición")
    st.markdown(
        """
        Un **agente de IA** es un sistema que, a diferencia de un modelo de
        lenguaje (LLM) usado de forma aislada, no solo **genera texto**: es
        capaz de **percibir** una tarea o pregunta, **razonar** sobre qué
        pasos seguir para resolverla, **actuar** usando herramientas
        externas (código, bases de datos, APIs), **observar** el resultado
        de esas acciones, y **decidir si necesita otro paso o ya puede
        responder**. Es un sistema con **autonomía acotada**: decide *cómo*
        resolver el problema dentro de reglas que no puede romper.

        La diferencia con un chatbot común no es de "inteligencia", es de
        **arquitectura**: un chatbot responde con lo que el modelo genera a
        partir de su entrenamiento; un agente **ejecuta cosas reales** para
        producir la respuesta.
        """
    )

    st.markdown("## 1.2 El ciclo de un agente: percibir → razonar → actuar → observar")
    flow_diagram(
        [
            ("👁️ Percibe", "la pregunta o tarea"),
            ("🧠 Razona", "planifica qué hacer"),
            ("🛠️ Actúa", "ejecuta una herramienta"),
            ("🔎 Observa", "revisa el resultado obtenido"),
            ("🔁 Repite o<br>responde", "si falta info, otro ciclo"),
        ],
        style="loop",
    )
    st.markdown(
        """
        Este patrón (conocido técnicamente como **ReAct** — *Reasoning +
        Acting*) es lo que le permite a un agente encadenar varios pasos sin
        que el usuario tenga que pedir cada uno por separado.
        """
    )

    st.markdown("## 1.3 Los componentes de este agente")
    c1, c2 = st.columns(2)
    with c1:
        concept_card(
            "🧠 Razonamiento — el LLM como orquestador",
            [
                "Interpreta la pregunta en lenguaje natural",
                "Decide QUÉ herramienta usar y en qué orden",
                "Redacta la interpretación final en lenguaje claro",
                "Nunca calcula un número por sí mismo",
            ],
        )
        concept_card(
            "🛠️ Herramientas (tools) — el cálculo real",
            [
                "Funciones de código Python deterministas",
                "Cada herramienta hace UNA cosa bien definida",
                "Mismo input → siempre el mismo output",
            ],
        )
    with c2:
        concept_card(
            "🗂️ Memoria y trazabilidad",
            [
                "Registra qué dataset, filtros, método y parámetros usó",
                "Permite auditar y reproducir cualquier respuesta anterior",
            ],
        )
        concept_card(
            "🚧 Reglas fijas (guardrails)",
            [
                "No inventar variables, columnas ni resultados",
                "No usar lenguaje causal en datos observacionales",
                "No exponer información personal identificable",
            ],
        )

    st.markdown("## 1.4 Tool calling / function calling")
    st.markdown(
        """
        Es el mecanismo que permite que un LLM, en vez de solo responder
        texto, pueda **invocar código externo de forma estructurada**: el
        modelo recibe una lista de "herramientas disponibles", y cuando
        detecta que una pregunta requiere una de ellas, genera una
        instrucción estructurada para ejecutarla. El resultado —ya
        calculado por Python— se le devuelve al modelo para que lo
        interprete y lo redacte. **El modelo nunca "calcula": solo pide
        que se calcule.**
        """
    )

    st.markdown("## 1.5 Chatbot simple vs. Agente de IA")
    st.markdown(
        """
        | | Chatbot simple (LLM aislado) | Agente de IA (este proyecto) |
        |---|---|---|
        | **Fuente de la respuesta** | Lo que el modelo "recuerda" de su entrenamiento | Cálculo real ejecutado sobre el dataset de la USTA |
        | **Acceso a datos propios** | No tiene acceso al dataset real | Sí, mediante herramientas conectadas al dataset |
        | **Cálculo numérico** | Lo genera el modelo (riesgo de alucinación) | Lo hace código Python determinista y auditable |
        | **Pasos múltiples** | Responde en un solo paso | Encadena pasos: validar → calcular → comparar → interpretar |
        | **Trazabilidad** | No explica cómo llegó al número | Registra dataset, método y parámetros usados |
        """
    )

    st.markdown("## 1.6 ¿Por qué SÍ es un agente y no un script con IA por encima?")
    st.markdown(
        """
        1. **Autonomía de decisión** — decide qué método estadístico usar
           según los datos, no sigue un guion fijo.
        2. **Uso de herramientas** — ejecuta código real, no solo genera texto.
        3. **Encadenamiento de pasos con verificación** — valida, calcula,
           compara y solo entonces responde; si algo no es posible, lo
           informa en vez de improvisar.
        """
    )

elif seccion == "2. Qué hace el agente":
    st.title("2. Qué hace el agente")
    st.caption("Medidas y estudios estadísticos que ejecuta, y por qué cada uno")

    st.markdown("### a) Replica y evalúa lo que ya se hizo")
    st.markdown(
        """
        El agente **reproduce las mismas medidas y modelos** que aplicó el
        estudio anterior (consistencia interna, GRM, T-scores, inferencia
        poblacional, WLS, comparaciones por grupo) y, además, **evalúa si
        siguen siendo pertinentes**: revisa supuestos, tamaño de muestra por
        subgrupo y calidad de ajuste, y si un método ya no es el más
        adecuado, lo señala y **propone una alternativa**.
        """
    )

    st.markdown("### b) Valida los resultados previos")
    st.markdown(
        """
        - Reproduce desde el dataset los indicadores reportados: *n*, alfa
          de Cronbach, T-score global, proporciones de bienestar.
        - Compara cada resultado contra el valor documentado y lo clasifica
          como **validado / diferencia menor / diferencia importante / no
          reproducible**.
        """
    )

    st.markdown("### c) Estadística descriptiva")
    st.markdown(
        "Frecuencias, medias, medianas, desviación estándar, percentiles e "
        "**intervalos de confianza**, siempre con el tamaño de muestra de "
        "cada subgrupo."
    )

    st.markdown("### d) Comparaciones entre grupos (carrera, sede, género, edad, estrato…)")
    st.markdown(
        """
        El agente **no elige la prueba por popularidad**: evalúa tipo de
        variable, normalidad, homocedasticidad y tamaño de muestra, y
        selecciona t-test/Mann-Whitney, ANOVA/Kruskal-Wallis (con post-hoc)
        o chi-cuadrado según corresponda, y siempre reporta **tamaño de
        efecto**, no solo el p-valor.
        """
    )

    st.markdown("### e) Modelos de regresión — ¿qué factores explican el bienestar?")
    st.markdown(
        """
        Regresión **WLS** (ponderada, continuando el enfoque del estudio
        anterior) y logística/ordinal para categorías de bienestar, con
        revisión de colinealidad e intervalos de confianza.
        """
    )

    st.markdown("### f) Disciplina de interpretación")
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown("**Descripción**")
    c1.caption('"El grupo A tiene mayor promedio."')
    c2.markdown("**Inferencia**")
    c2.caption('"Hay evidencia estadística de una diferencia."')
    c3.markdown("**Asociación**")
    c3.caption('"Las variables están asociadas."')
    c4.markdown("**Causalidad**")
    c4.caption("No se afirma — datos observacionales de encuesta.")

elif seccion == "3. Cómo funciona el agente":
    st.title("3. Cómo funciona el agente")

    st.markdown("### ¿De qué se alimenta?")
    flow_diagram(
        [
            ("📄 Dataset USTA", "ítems, dimensiones, sociodemográficas, pesos"),
            ("📑 Informes previos", "solo como punto de comparación"),
        ]
    )

    st.markdown("### ¿Con qué IA?")
    st.markdown(
        """
        Un **LLM usado como orquestador**: interpreta la pregunta, decide
        qué herramienta ejecutar y redacta la interpretación final. El
        **cálculo estadístico lo hace siempre código Python determinista**
        — nunca un número generado directamente por el LLM.
        """
    )

    st.markdown("### Flujo de una consulta")
    flow_diagram(
        [
            ("🧑 Pregunta del<br>usuario", None),
            ("🧭 Query Planner", "identifica variables"),
            ("⚙️ Statistical Engine", "elige y ejecuta el método"),
            ("✅ Result Validator", "revisa consistencia"),
            ("📝 Report Generator", "tabla + gráfico + interpretación"),
            ("🔍 Trazabilidad", "queda registrada"),
        ]
    )

    st.markdown("### Estructura del agente, por capas")
    col1, col2 = st.columns(2)
    with col1:
        layer_card(
            "1 · Capa de datos",
            [
                "Data Profiler — columnas, tipos, faltantes, sensibles",
                "Data / Weight Validator — factores de expansión",
            ],
        )
        layer_card(
            "2 · Capa de validación estadística",
            [
                "Psychometric Validator — ítems, dimensiones, alfa",
                "IRT Validator — GRM, theta, T-score",
                "Result Validator — comparación vs. resultados previos",
            ],
        )
    with col2:
        layer_card(
            "3 · Capa de análisis",
            ["Statistical Engine — descriptivos, comparaciones, regresión"],
        )
        layer_card(
            "4 · Capa de orquestación y salida",
            [
                "Query Planner (LLM) — interpreta la pregunta",
                "Report Generator — informe final",
                "Trazabilidad — dataset, filtros, método, fecha",
            ],
        )

elif seccion == "4. Resultados que muestra":
    st.title("4. Resultados que muestra el agente")
    st.caption("El resultado final siempre es un informe con el análisis del agente de IA")

    st.markdown(
        """
        1. **Pregunta** que se está respondiendo
        2. **Datos utilizados** (dataset, columnas, filtros aplicados)
        3. **Método estadístico** usado y por qué se eligió
        4. **Resultados** (tabla y/o gráfico)
        5. **Intervalos de confianza** / incertidumbre
        6. **Interpretación** en lenguaje comprensible
        7. **Limitaciones** del análisis
        8. **Recomendaciones**, cuando aplique
        """
    )

    st.markdown("### Ejemplo de tabla de validación (formato, no datos reales)")
    st.table(
        {
            "Resultado": ["n muestral", "Alfa de Cronbach", "T-score global"],
            "Valor anterior": ["1.813", "0.909", "50.7"],
            "Valor reproducido": ["—", "—", "—"],
            "Diferencia": ["—", "—", "—"],
            "Estado": ["pendiente", "pendiente", "pendiente"],
        }
    )

# =================================================================
# PARTE 2 — EL PROYECTO DE CONSULTORÍA (alineado a la rúbrica)
# =================================================================

elif seccion == "5. Contraparte y necesidad":
    st.title("5. Contraparte y necesidad")
    rubric_badge("Criterio 1 · Justificación y necesidad · 20 %")

    st.markdown("### ¿Quién es la contraparte?")
    st.markdown(
        """
        Dos partes interesadas reales, con necesidades distintas pero
        conectadas:

        - **El equipo de estudiantes que hizo el estudio anterior** — son
          dueños del pipeline (dataset, notebooks, informes) y necesitan
          que alguien externo lo audite y les confirme si sus resultados
          son reproducibles.
        - **La universidad** — necesita una herramienta que le permita
          seguir consultando esta información sin depender de que ese
          equipo original repita el análisis a mano cada vez que surge una
          pregunta nueva (por ejemplo, del área de Bienestar Universitario).
        """
    )

    st.markdown("### Lo que piden vs. lo que necesitan")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Lo que piden**")
        st.markdown(
            "- Que se revisen sus resultados\n"
            "- Que se pueda seguir analizando el bienestar por grupo\n"
        )
    with col2:
        st.markdown("**Lo que necesitan (más allá de lo pedido)**")
        st.markdown(
            "- Confirmación *independiente y reproducible* de que sus "
            "cifras son correctas — no solo una revisión visual del PDF\n"
            "- Una forma de consultar el dato **sin depender de ellos** — "
            "la universidad debe poder usarlo aunque el equipo original ya "
            "no esté disponible"
        )

    pending(
        "Entrevista formal con ambas contrapartes: minutos que toma HOY "
        "responder una pregunta nueva sobre el estudio (sin agente), cuántas "
        "veces al mes se recibe una solicitud de este tipo, y qué error o "
        "vacío ya detectaron ellos mismos en su propio proceso."
    )

    st.markdown("### ¿Por qué esto exige un agente y no un script fijo?")
    st.markdown(
        """
        - **Decisión sobre casos no previstos**: el método estadístico
          correcto cambia según la pregunta (¿dos grupos o más? ¿se cumple
          normalidad? ¿hay pesos?) — un script fijo tendría que anticipar
          cada combinación a mano; el agente decide en el momento.
        - **Orquestación de varias herramientas**: perfilado, validación
          psicométrica/IRT, motor estadístico y generación de informe son
          pasos distintos que deben encadenarse según la pregunta — no es
          una sola función.
        - **Entrada no estructurada**: la contraparte pregunta en lenguaje
          natural ("¿hay diferencia entre sedes?"), no en un formulario con
          parámetros fijos.
        """
    )

    st.markdown("### Alcance para estas 3 semanas (propuesta a confirmar con el docente)")
    st.markdown(
        """
        La visión completa (13 módulos, literatura externa, chatbot final)
        **no cabe en 3 semanas**. Se propone acotar el encargo a:

        **Dentro del alcance:** inspección y documentación del proyecto
        anterior, validación reproducible de los indicadores clave (n, alfa,
        T-score global, proporciones), motor estadístico básico
        (descriptivos + comparaciones + un modelo de regresión), y un
        Query Planner simple que responda preguntas por segmento
        (carrera, sede, género, edad, estrato).

        **Fuera del alcance de esta entrega** (queda documentado como
        trabajo futuro, no como algo olvidado): el módulo de literatura
        externa vía API, la interfaz conversacional/chatbot final, y la
        reproducción completa y afinada del modelo IRT/GRM si el estudio
        original lo hizo en una herramienta distinta a Python.
        """
    )

    st.markdown("### Otras alternativas consideradas y por qué se descartaron")
    st.markdown(
        """
        - **Repetir la encuesta desde cero** — descartado: ya existe una
          muestra representativa; repetirla desperdicia lo ya recolectado y
          no responde a la necesidad real (auditar y reutilizar, no
          recolectar de nuevo).
        - **Un dashboard estático (Power BI / Excel dinámico)** — descartado
          como única solución: sirve para ver gráficos fijos, pero no puede
          decidir qué prueba estadística aplica según la pregunta, ni
          responder algo que no esté precalculado.
        - **Un script fijo por cada pregunta esperada** — descartado: exige
          anticipar cada combinación de variables de antemano; no escala a
          preguntas nuevas de la contraparte.
        """
    )

elif seccion == "6. Diseño y configuración":
    st.title("6. Diseño y configuración")
    rubric_badge("Criterio 2 · Diseño y configuración · 20 %")

    st.markdown("### Flujo completo: entrada → herramientas → verificación → salida")
    flow_diagram(
        [
            ("🧑 Entrada", "pregunta en lenguaje natural"),
            ("🧭 Query Planner", "identifica variables"),
            ("⚙️ Statistical Engine", "ejecuta el método"),
            ("✅ Validator", "revisa consistencia"),
            ("📝 Salida", "informe con método + IC"),
        ]
    )

    st.markdown("### Rutas de error y criterio de parada")
    st.markdown(
        """
        | Situación | Qué hace el agente |
        |---|---|
        | La variable pedida no existe (p. ej. ingresos) | Se detiene, informa que no existe y sugiere variables relacionadas (estrato) |
        | El subgrupo tiene muestra insuficiente | Se detiene, entrega el resultado con advertencia explícita de baja confiabilidad, no lo oculta |
        | El LLM devuelve una instrucción de herramienta mal formada | Se reintenta una vez; si vuelve a fallar, responde que no pudo completar el análisis en vez de improvisar |
        | Los supuestos de una prueba no se cumplen | Cambia automáticamente a la alternativa no paramétrica y lo declara en el informe |
        """
    )

    st.markdown("### Elección del modelo de lenguaje (LLM) — comparada contra alternativas")
    st.markdown(
        """
        | Opción | Confidencialidad del dato | Costo | Latencia | Ventana de contexto |
        |---|---|---|---|---|
        | **API comercial (Claude / GPT)** | El LLM solo ve resultados ya agregados por el motor Python — nunca microdatos crudos, lo que reduce el riesgo | Costo por token, pero bajo volumen esperado en 3 semanas | Baja (segundos) | Amplia, suficiente para redactar informes largos |
        | **Modelo local (open-weight, cuantizado)** | Máxima confidencialidad — nada sale de la máquina | Sin costo por uso, pero requiere hardware | Depende del hardware disponible | Normalmente más limitada |

        **Decisión propuesta:** API comercial, justificada por la
        arquitectura orquestador — como el LLM nunca recibe la microdata
        (solo cálculos ya agregados), el riesgo de confidencialidad que
        normalmente inclinaría la balanza hacia un modelo local queda
        mitigado por diseño, y se gana calidad de razonamiento y de
        tool calling maduro.
        """
    )

    st.markdown("### Qué NO debe hacer el agente")
    st.markdown(
        """
        - No calcula ningún número directamente — todo cálculo pasa por el
          motor estadístico en Python.
        - No inventa variables, columnas ni resultados que no existan en
          el dataset.
        - No usa lenguaje causal sobre datos observacionales.
        - No expone identificadores personales ni resultados de subgrupos
          por debajo de un tamaño mínimo sin advertencia.
        """
    )

    st.markdown("### Cómo se verifica la salida antes de usarla")
    st.markdown(
        """
        - **Result Validator**: compara cada cifra reproducida contra el
          valor documentado en los informes anteriores.
        - **Validación de esquema**: antes de ejecutar cualquier
          instrucción que venga del LLM, se revisa que tenga los campos
          esperados (variable, método, filtros) — si no, se rechaza y se
          reintenta.
        - **Revisión humana periódica** de una muestra de respuestas del
          agente, como control de calidad adicional.
        """
    )

elif seccion == "7. Implementación técnica y entorno":
    st.title("7. Implementación técnica y entorno")
    rubric_badge("Criterio 3 · Implementación técnica · 20 %")

    st.markdown("### Reproducibilidad")
    st.markdown(
        """
        - `README.md` con pasos para correr el proyecto desde cero en otra
          máquina.
        - `requirements.txt` con versiones fijadas (no solo nombres de
          librería).
        - Código organizado en módulos con **responsabilidad única**
          (un archivo no mezcla validación con generación de informes).
        - Credenciales del LLM en variables de entorno (`.env`), nunca
          escritas en el código ni subidas al repositorio.
        """
    )

    st.markdown("### Prompts versionados (ejemplo del tipo de iteración esperada)")
    st.markdown(
        """
        **v1 (primer intento, sin estructura):**
        > "Eres un asistente que analiza datos de bienestar estudiantil,
        > responde las preguntas del usuario."

        **v2 (con rol, contrato de salida y restricciones — la razón del
        cambio: v1 dejaba que el modelo redactara cifras libremente):**
        > Rol: orquestador estadístico. Nunca calcules un número tú mismo;
        > siempre invoca una herramienta. Responde únicamente con una
        > instrucción de herramienta en el formato esperado (variable,
        > método, filtros). Si la variable no existe, indícalo en vez de
        > aproximarla.

        Este tipo de comparación (`v1 → v2`, con la razón del cambio) debe
        quedar documentado en el repositorio, no solo en la memoria del
        equipo.
        """
    )

    st.markdown("### Manejo de errores por tipo")
    st.markdown(
        """
        | Tipo de error | Manejo |
        |---|---|
        | Tiempo de espera agotado (API del LLM) | Reintento con backoff, y mensaje claro si persiste |
        | Salida del LLM no parseable | Se descarta, se reintenta una vez, luego se informa el fallo |
        | Herramienta interna caída (p. ej. falla el cálculo IRT) | Se informa qué parte del análisis no se pudo completar, sin fingir un resultado |
        | Límite de tasa de la API | Se espera y reintenta; se documenta el límite del plan usado |
        """
    )

    st.markdown("### Medición de recursos")
    st.markdown(
        "Se debe registrar, para al menos un conjunto de consultas de "
        "prueba: tokens aproximados por consulta, costo estimado y "
        "latencia observada — no basta con mencionar que se usará una API, "
        "hay que medir el uso real durante las pruebas."
    )

    st.divider()
    st.markdown("### Entorno de trabajo")
    flow_diagram(
        [
            ("🐙 GitHub", "código, notebooks, docs, pruebas"),
            ("📓 Colab", "prototipado y validación rápida"),
            ("💻 VS Code / Codespaces", "construcción del agente como software"),
            ("🌐 Streamlit", "app / interfaz de resultados"),
        ]
    )

    st.markdown("### Librerías por tarea")
    st.markdown(
        """
        | Tarea | Herramienta |
        |---|---|
        | Manejo de datos | `pandas`, `numpy` |
        | Estadística clásica | `scipy.stats` |
        | Regresión (WLS, logística) e inferencia | `statsmodels` |
        | Modelo IRT / GRM | librería de TRI en Python (a definir si se replica en Python o si el estudio original usó R) |
        | Gráficos | `matplotlib` / `plotly` |
        | Pruebas automáticas | `pytest` |
        | Interfaz | `streamlit` |
        | LLM orquestador | API de un modelo de lenguaje (tool calling) |
        """
    )

elif seccion == "8. Valor agregado y pruebas":
    st.title("8. Valor agregado y pruebas")
    rubric_badge("Criterio 4 · Pertinencia y valor agregado · 15 %")

    st.markdown("### Conjunto de casos de prueba propio")
    st.markdown(
        """
        | Tipo de caso | Ejemplo | Qué debe pasar |
        |---|---|---|
        | **Acierto** | "¿Hay diferencia de bienestar por género?" | Elige la prueba correcta según supuestos y reporta IC + tamaño de efecto |
        | **Fallo esperado / variable inexistente** | "¿Cómo varía el bienestar según el ingreso?" | Responde que la variable no existe y sugiere estrato — nunca inventa un valor |
        | **Caso límite — muestra pequeña** | Bienestar en un programa con muy pocos encuestados | Advierte explícitamente el tamaño de muestra insuficiente en vez de dar una cifra sin contexto |
        | **Caso límite — resultado no reproducible** | Comparar T-score global contra el informe anterior | Si no coincide, lo marca como "diferencia importante", no lo oculta |
        """
    )

    st.markdown("### Comparación contra la línea base")
    pending(
        "Cifra real de cuánto tiempo toma HOY responder manualmente una "
        "pregunta nueva sobre el estudio (sin el agente), para poder "
        "comparar tiempo y trazabilidad antes/después."
    )

    st.markdown("### Dónde falla el agente (honestidad sobre límites)")
    st.markdown(
        """
        - En subgrupos con muestra muy pequeña, ningún método —por bueno
          que sea el agente— puede dar una estimación confiable; el agente
          lo advierte, no lo resuelve.
        - Si el estudio original usó una herramienta distinta a Python
          para el modelo IRT/GRM, reproducirlo con exactitud puede requerir
          más de las 3 semanas — se documenta como limitación, no se fuerza
          una réplica aproximada presentada como exacta.
        - El agente no reemplaza el criterio de un estadístico para decidir
          si un hallazgo amerita una recomendación institucional.
        """
    )

    st.markdown("### Que la contraparte pueda usarlo sin el equipo")
    st.markdown(
        """
        - Instrucciones de uso en el lenguaje de la contraparte (no solo
          técnico), en el README.
        - Cada respuesta del agente muestra el método usado y el intervalo
          de confianza, para que cualquier persona pueda cuestionar el
          resultado sin ser estadístico.
        - El Result Validator queda disponible como herramienta reusable,
          no como algo que solo el equipo sabe correr.
        """
    )

elif seccion == "9. Riesgos del dominio":
    st.title("9. Riesgos del dominio")
    rubric_badge("Parte del Criterio 4 · riesgos y su mitigación")

    riesgos = [
        ("Archivos que no permiten reproducir el pipeline original",
         "Datos y reproducibilidad",
         "Se soluciona en la fase de inspección: se clasifica cada archivo "
         "por su contenido real antes de calcular nada.", True),
        ("Subgrupos con muestra muy pequeña (ciertos programas o sedes)",
         "Estadístico",
         "Riesgo residual: se reporta el tamaño de muestra y el IC, pero "
         "no se puede aumentar la muestra ya recolectada.", False),
        ("Comparaciones múltiples inflan falsos positivos",
         "Estadístico",
         "Se soluciona aplicando corrección del umbral de significancia.",
         True),
        ("Interpretar asociación como causalidad",
         "Estadístico",
         "Se soluciona por diseño: prohibido el lenguaje causal sobre "
         "datos observacionales.", True),
        ("Alucinación de cifras por parte del LLM",
         "Uso de IA",
         "Se soluciona con la arquitectura orquestador + motor estadístico "
         "separado.", True),
        ("Dependencia de la API externa del LLM",
         "Uso de IA",
         "Riesgo residual: costos, disponibilidad y límites de uso quedan "
         "fuera del control del proyecto.", False),
        ("Identificación indirecta en subgrupos pequeños",
         "Ético / privacidad",
         "Se soluciona anonimizando y agregando resultados por umbral "
         "mínimo de tamaño de grupo.", True),
        ("Uso indebido de resultados para decisiones institucionales",
         "Ético / privacidad",
         "Riesgo residual: el agente incluye limitaciones, pero no "
         "controla cómo se usa el informe una vez entregado.", False),
    ]
    categorias = sorted(set(r[1] for r in riesgos))
    for cat in categorias:
        st.markdown(f"#### {cat}")
        for riesgo, _, mitigacion, resuelto in riesgos:
            if _ != cat:
                continue
            etiqueta = (
                '<span class="risk-solved">✔ Se soluciona</span>'
                if resuelto
                else '<span class="risk-residual">⚠ Riesgo residual (se asume)</span>'
            )
            st.markdown(
                f"**{riesgo}** — {etiqueta}<br><span style='color:#cbd5e1;font-size:13.5px'>{mitigacion}</span>",
                unsafe_allow_html=True,
            )
            st.write("")

elif seccion == "10. Sustentación — qué nos van a preguntar":
    st.title("10. Sustentación — qué nos van a preguntar")
    rubric_badge("Criterio 5 · Sustentación y comunicación · 25 % · individual")

    st.warning(
        "Este criterio se califica por separado a cada integrante. Ambos "
        "deben poder justificar cualquier decisión, incluidas las que tomó "
        "el otro, y responder contrafácticos en vivo (¿y si el dato fuera "
        "confidencial? ¿y si el volumen se multiplicara por cien?)."
    )

    st.markdown("### Preguntas que debemos poder responder sin guion preparado")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Sobre el problema (Criterio 1)**")
        st.markdown(
            "- ¿Con quién hablamos y qué nos dijo que no esperábamos?\n"
            "- ¿Quién hace hoy esta tarea sin el agente, y cuánto le toma?\n"
            "- ¿Qué otros casos consideramos y por qué los descartamos?\n"
            "- ¿Qué recortamos del alcance al ver que eran 3 semanas?"
        )
        st.markdown("**Sobre el diseño (Criterio 2)**")
        st.markdown(
            "- ¿Qué arquitectura descartamos y cuándo supimos que no servía?\n"
            "- ¿Qué se rompe si quitamos tal herramienta?\n"
            "- ¿Por qué ese modelo de lenguaje y no uno más pequeño?\n"
            "- ¿Cómo sabe el agente que terminó, y qué pasa si una "
            "herramienta no responde?"
        )
    with c2:
        st.markdown("**Sobre la implementación (Criterio 3)**")
        st.markdown(
            "- ¿Qué falló en la primera versión del prompt y qué cambiamos?\n"
            "- ¿Qué pasa si el modelo devuelve algo que el código no puede leer?\n"
            "- ¿Dónde está la clave de API y por qué está ahí?"
        )
        st.markdown("**Sobre el valor (Criterio 4)**")
        st.markdown(
            "- Denme un caso donde falla. ¿Por qué falla ahí?\n"
            "- ¿Qué decisión de este proceso nunca le delegaríamos al agente?\n"
            "- Si mañana desaparecemos, ¿la contraparte puede seguir usándolo?"
        )

    st.markdown("### La pregunta más importante")
    st.info(
        "**¿Qué de este proyecto todavía no entendemos del todo?** "
        "Responder \"no, todo claro\" es la peor respuesta posible — "
        "reconocer con precisión dónde termina lo que entendemos es señal "
        "de que entendimos el resto."
    )

elif seccion == "11. Próximos pasos":
    st.title("11. Próximos pasos")

    st.markdown("### Inmediatos (semana 1)")
    pasos = [
        "Entrevista formal con la contraparte (estudiantes anteriores + "
        "universidad) para conseguir la línea base cuantificada",
        "Inspeccionar el contenido real de cada archivo del proyecto anterior",
        "Documentar el pipeline en docs/ANALISIS_PROYECTO_EXISTENTE.md",
        "Validar los resultados anteriores (n, alfa, T-score global, "
        "proporciones, diferencias por grupo)",
    ]
    for i, paso in enumerate(pasos, start=1):
        st.markdown(f"**{i}.** {paso}")

    st.markdown("### Semanas 2–3")
    pasos2 = [
        "Construir el motor estadístico básico y el Query Planner simple",
        "Definir y correr el conjunto de casos de prueba (aciertos, "
        "fallos, casos límite)",
        "Medir recursos (tokens, costo, latencia) sobre las pruebas",
        "Escribir el README y dejar el proyecto ejecutable desde cero",
    ]
    for i, paso in enumerate(pasos2, start=1):
        st.markdown(f"**{i}.** {paso}")

    st.markdown("### Fuera del alcance de esta entrega (fase futura)")
    st.markdown(
        """
        - Módulo de literatura externa vía API
        - Interfaz conversacional (chatbot) completa
        - Generación automática de informes dinámicos para todos los segmentos
        """
    )
