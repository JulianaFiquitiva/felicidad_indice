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
CSS = """
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
.pending-card {
    background:#1c1410; border:1px solid #a16207; border-left:5px solid #eab308;
    border-radius:10px; padding:12px 16px; margin:10px 0; color:#fde68a; font-size:13.5px;
}
.q-card {
    background:#111827; border:1px solid #334155; border-left:5px solid #6366f1;
    border-radius:10px; padding:12px 16px; margin:8px 0; color:#e2e8f0; font-size:13.5px;
}
.q-label { color:#a5b4fc; font-weight:700; font-size:12px; text-transform:uppercase; letter-spacing:.03em; }
.dash-card {
    background:#0b1220; border:1px solid #1e293b; border-left:5px solid #22c55e;
    border-radius:10px; padding:12px 16px; margin:8px 0; color:#e2e8f0; font-size:13.5px;
}
.dash-title { color:#86efac; font-weight:700; margin-bottom:4px; }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


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


def pending(text):
    st.markdown(f'<div class="pending-card">⏳ <strong>Pendiente — no se puede responder sin abrir el dato real:</strong> {text}</div>', unsafe_allow_html=True)


def qcard(question, answer):
    st.markdown(
        f'<div class="q-card"><div class="q-label">{question}</div>{answer}</div>',
        unsafe_allow_html=True,
    )


def dash_card(title, items):
    html = f'<div class="dash-card"><div class="dash-title">📊 {title}</div>'
    for it in items:
        html += f'<div>• {it}</div>'
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


# ---------------------------------------------------------------
# SIDEBAR — DOS PARTES SEPARADAS
# ---------------------------------------------------------------
st.sidebar.title("📊 Agente IA — Bienestar Estudiantil")
st.sidebar.caption("USTA · Consultoría e Investigación · Prof. Javier Mauricio Sierra")

parte = st.sidebar.radio(
    "Parte de la presentación",
    ["Parte 1 · El agente de IA", "Parte 2 · El proyecto"],
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
            "4. Cómo se presenta: el dashboard",
        ],
    )
else:
    seccion = st.sidebar.radio(
        "Sección",
        [
            "5. Problema y contexto actual",
            "6. Objetivos",
            "7. Estado del arte",
            "8. Resumen corto de los datos",
        ],
    )

# =================================================================
# PARTE 1 · EL AGENTE DE IA
# =================================================================

if seccion == "0. Portada":
    st.title("Agente de IA para el Índice de Bienestar Estudiantil")
    st.subheader("Universidad Santo Tomás · Herramienta de apoyo a la toma de decisiones institucional")

    col1, col2, col3 = st.columns(3)
    col1.metric("Respuestas del estudio previo", "1.813")
    col2.metric("Población objetivo aprox.", "29.950")
    col3.metric("Ítems tipo Likert", "29")

    st.markdown(
        """
        Este proyecto retoma el estudio de bienestar estudiantil ya
        realizado en la USTA (2025–2026) y construye un **agente de
        inteligencia artificial** que hace análisis exploratorio, **replica
        el análisis del estudio anterior** para validarlo, y presenta todo
        de forma **ilustrativa, como un dashboard interactivo**.

        **Para quién es esto:** exclusivamente para **apoyar la toma de
        decisiones de la universidad y sus dependencias** (Bienestar
        Universitario, direcciones de programa, seccionales) — no es una
        herramienta para el equipo que hizo el estudio anterior, aunque su
        trabajo es la base de datos y de pipeline sobre la que se construye.
        """
    )
    st.info("Entrega — Materia de Consultoría e Investigación.")

elif seccion == "1. ¿Qué es un agente de IA?":
    st.title("1. ¿Qué es un agente de IA?")
    st.caption("Los conceptos que sostienen todo lo demás en esta presentación")

    st.markdown("## 1.1 Definición")
    st.markdown(
        """
        Un **agente de IA** es un sistema que, a diferencia de un modelo de
        lenguaje (LLM) usado de forma aislada, no solo **genera texto**: es
        capaz de **percibir** una tarea o pregunta, **razonar** sobre qué
        pasos seguir, **actuar** usando herramientas externas (código,
        datos), **observar** el resultado, y **decidir si necesita otro
        paso o ya puede responder**. Es un sistema con **autonomía
        acotada**: decide *cómo* resolver el problema dentro de reglas que
        no puede romper.

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
        "Este patrón (**ReAct** — *Reasoning + Acting*) es lo que le "
        "permite a un agente encadenar varios pasos sin que el usuario "
        "tenga que pedir cada uno por separado."
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
        Es el mecanismo que permite que un LLM **invoque código externo de
        forma estructurada**: recibe una lista de "herramientas
        disponibles", y cuando detecta que una pregunta requiere una de
        ellas, genera una instrucción estructurada para ejecutarla. El
        resultado —ya calculado por Python— se le devuelve al modelo para
        que lo interprete y lo redacte. **El modelo nunca "calcula": solo
        pide que se calcule.**
        """
    )

    st.markdown("## 1.5 Chatbot simple vs. Agente de IA")
    st.markdown(
        """
        | | Chatbot simple (LLM aislado) | Agente de IA (este proyecto) |
        |---|---|---|
        | **Fuente de la respuesta** | Lo que el modelo "recuerda" de su entrenamiento | Cálculo real sobre el dataset de la USTA |
        | **Acceso a datos propios** | No tiene acceso al dataset real | Sí, mediante herramientas conectadas al dataset |
        | **Cálculo numérico** | Lo genera el modelo (riesgo de alucinación) | Lo hace código Python determinista y auditable |
        | **Pasos múltiples** | Responde en un solo paso | Encadena pasos: explorar → replicar → comparar → mostrar |
        | **Trazabilidad** | No explica cómo llegó al número | Registra dataset, método y parámetros usados |
        """
    )

    st.markdown("## 1.6 ¿Por qué SÍ es un agente y no un script con IA por encima?")
    st.markdown(
        """
        1. **Autonomía de decisión** — decide qué método estadístico usar
           según los datos, no sigue un guion fijo.
        2. **Uso de herramientas** — ejecuta código real, no solo genera texto.
        3. **Encadenamiento de pasos con verificación** — explora, replica,
           compara y solo entonces muestra el resultado en el dashboard.
        """
    )

elif seccion == "2. Qué hace el agente":
    st.title("2. Qué hace el agente")
    st.caption("El trabajo real: análisis exploratorio + réplica del estudio anterior")

    st.markdown("### a) Análisis exploratorio de datos (EDA)")
    st.markdown(
        """
        Antes de replicar nada, el agente **explora el dataset real**: tipos
        de variable, valores faltantes, distribución de cada ítem y cada
        dimensión, tamaños de muestra por grupo (sede, programa, género,
        estrato, edad), y detección de inconsistencias. Este paso es el que
        confirma —o corrige— los supuestos con los que se construyó el
        resto del análisis.
        """
    )

    st.markdown("### b) Replica y evalúa el análisis del estudio anterior")
    st.markdown(
        """
        El agente **reproduce las mismas medidas y modelos** que aplicó el
        estudio previo (consistencia interna, GRM, T-scores, inferencia
        poblacional, WLS, comparaciones por grupo) y, además, **evalúa si
        siguen siendo pertinentes**: revisa supuestos, tamaño de muestra por
        subgrupo y calidad de ajuste. Si un método ya no es el más
        adecuado, lo señala y **propone una alternativa** (por ejemplo, una
        prueba no paramétrica en vez de una paramétrica si no se cumple
        normalidad).
        """
    )

    st.markdown("### c) Valida los resultados previos")
    st.markdown(
        """
        - Reproduce desde el dataset los indicadores reportados: *n*, alfa
          de Cronbach, T-score global, proporciones de bienestar.
        - Compara cada resultado contra el valor documentado y lo clasifica
          como **validado / diferencia menor / diferencia importante / no
          reproducible**.
        """
    )

    st.markdown("### d) Comparaciones entre grupos y modelos de regresión")
    st.markdown(
        """
        Selecciona el método según tipo de variable, normalidad,
        homocedasticidad y tamaño de muestra (t-test/Mann-Whitney,
        ANOVA/Kruskal-Wallis, chi-cuadrado), reporta tamaño de efecto, y
        ajusta regresión **WLS** (continuando el enfoque del estudio
        anterior) para explicar qué factores se asocian al bienestar.
        """
    )

    st.markdown("### e) Disciplina de interpretación")
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

    st.markdown("### Flujo: exploración → réplica → dashboard")
    flow_diagram(
        [
            ("🔍 EDA", "perfilar el dataset real"),
            ("🧮 Réplica", "recalcular lo del estudio anterior"),
            ("✅ Validator", "compara vs. lo reportado"),
            ("📊 Dashboard", "muestra todo de forma visual"),
        ]
    )

    st.markdown("### Estructura del agente, por capas")
    col1, col2 = st.columns(2)
    with col1:
        layer_card(
            "1 · Capa de datos",
            [
                "Data Profiler — EDA: columnas, tipos, faltantes, sensibles",
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
            "4 · Capa de presentación",
            [
                "Query Planner (LLM) — interpreta la pregunta",
                "Dashboard — la cara visible de todo lo anterior",
                "Trazabilidad — dataset, filtros, método, fecha",
            ],
        )

elif seccion == "4. Cómo se presenta: el dashboard":
    st.title("4. Cómo se presenta: el dashboard")
    st.caption("Todo el análisis se entrega de forma ilustrativa, no como texto suelto")

    st.markdown(
        """
        El resultado final del agente no es un PDF estático ni una
        respuesta de chat aislada: es un **dashboard interactivo** (esta
        misma app de Streamlit es el prototipo de esa idea) donde la
        universidad puede ver, filtrar y comparar sin depender de que
        alguien le redacte un informe cada vez.
        """
    )

    st.markdown("### Qué muestra el dashboard")
    col1, col2 = st.columns(2)
    with col1:
        dash_card(
            "Panel de exploración (EDA)",
            [
                "Distribución de cada dimensión de bienestar",
                "Tamaño de muestra por sede, programa, género, estrato",
                "Valores faltantes e inconsistencias detectadas",
            ],
        )
        dash_card(
            "Panel de validación",
            [
                "Tabla: valor anterior vs. valor reproducido vs. estado",
                "Indicador visual (verde/ámbar/rojo) por cada resultado",
            ],
        )
    with col2:
        dash_card(
            "Panel comparativo",
            [
                "Bienestar por sede, programa, género, edad, estrato",
                "Gráficos con intervalo de confianza, no solo el promedio",
            ],
        )
        dash_card(
            "Panel de modelos",
            [
                "Coeficientes de la regresión WLS con su intervalo",
                "Qué variables se asocian más al bienestar",
            ],
        )

    st.markdown("### Ejemplo de tabla que vería la universidad en el dashboard")
    st.table(
        {
            "Resultado": ["n muestral", "Alfa de Cronbach", "T-score global"],
            "Valor anterior": ["1.813", "0.909", "50.7"],
            "Valor reproducido": ["—", "—", "—"],
            "Estado": ["pendiente", "pendiente", "pendiente"],
        }
    )
    st.caption(
        "Las columnas de la derecha se llenan una vez el agente calcule "
        "sobre el dataset real — este es el formato, no el resultado."
    )

# =================================================================
# PARTE 2 · EL PROYECTO
# =================================================================

elif seccion == "5. Problema y contexto actual":
    st.title("5. Problema y contexto actual")

    qcard(
        "¿Quién sufre este problema y desde cuándo?",
        "La universidad y sus dependencias (Bienestar Universitario, "
        "direcciones de programa, seccionales) no cuentan con una forma "
        "propia de consultar, validar o profundizar en los resultados del "
        "estudio de bienestar estudiantil. El problema existe **desde que "
        "el estudio anterior entregó sus resultados**: quedaron fijados en "
        "PDFs y notebooks en el momento de la entrega, sin quedar una "
        "herramienta reutilizable por la institución.",
    )

    qcard(
        "¿Cómo se está resolviendo hoy, sin este agente?",
        "Cualquier pregunta nueva sobre el bienestar estudiantil (por "
        "ejemplo, \"¿cómo está Villavicencio pregrado comparado con "
        "Bogotá?\") solo puede responderse si alguien vuelve a abrir los "
        "notebooks originales y repite el análisis manualmente. No existe "
        "hoy una vía institucional para consultarlo sin depender de quien "
        "construyó el pipeline original.",
    )

    qcard(
        "¿Qué pasa si nadie hace nada?",
        "Los resultados quedan como documentos estáticos que la "
        "universidad no puede volver a interrogar ni validar de forma "
        "independiente. Cualquier decisión institucional que dependa de "
        "\"qué tan bien está el bienestar estudiantil por sede o "
        "programa\" seguiría basada en una cifra fija de un informe, sin "
        "posibilidad de profundizar, segmentar o actualizar el análisis.",
    )

    st.markdown("### Contexto del estudio sobre el que se construye")
    st.markdown(
        """
        - 1.813 respuestas válidas, población objetivo ≈ 29.950 estudiantes
        - Muestreo estratificado con factores de expansión
        - 29 ítems tipo Likert, agrupados en 6 dimensiones de bienestar
          psicológico
        - Ya se hizo: análisis psicométrico, TRI/GRM, T-scores, inferencia
          poblacional, regresión WLS, comparaciones por seccional,
          modalidad, género, estrato, edad y programa
        """
    )

elif seccion == "6. Objetivos":
    st.title("6. Objetivos")

    st.markdown("### Objetivo general")
    st.success(
        "Desarrollar un agente de inteligencia artificial que explore, "
        "replique y valide el Índice de Bienestar Estudiantil, y presente "
        "los resultados en un **dashboard interactivo** como insumo para "
        "la toma de decisiones de la universidad y sus dependencias."
    )

    st.markdown("### Objetivos específicos")
    st.caption(
        "Cada uno deja una evidencia verificable — si los tres se "
        "cumplen, el objetivo general queda resuelto: se exploró y conoce "
        "el dato (1), se validó contra lo anterior (2), y quedó "
        "presentable y usable por la universidad (3)."
    )

    with st.expander("1. Hacer el análisis exploratorio de datos (EDA)"):
        st.markdown(
            """
            Perfilar el dataset real: tipos de variable, faltantes,
            distribución de ítems y dimensiones, tamaños de muestra por
            grupo, e inconsistencias.

            **Evidencia de cumplimiento:** un panel de EDA en el dashboard
            con esas distribuciones y alertas de calidad de dato.
            """
        )

    with st.expander("2. Replicar y validar el análisis del estudio anterior"):
        st.markdown(
            """
            Reproducir desde el dataset los indicadores clave (n, alfa de
            Cronbach, T-score global, comparaciones por grupo, regresión
            WLS) y compararlos contra lo documentado.

            **Evidencia de cumplimiento:** una tabla de validación
            (valor anterior vs. valor reproducido vs. estado) para cada
            indicador replicado.
            """
        )

    with st.expander("3. Presentar todo en un dashboard interactivo para la universidad"):
        st.markdown(
            """
            Entregar el EDA y la réplica del análisis en un dashboard
            visual (no en texto suelto), que las dependencias de la
            universidad puedan explorar por su cuenta.

            **Evidencia de cumplimiento:** el dashboard funcionando con
            datos reales, revisado por una dependencia de la universidad.
            """
        )

    st.markdown("### Qué NO es un objetivo (son actividades, no fines)")
    st.markdown(
        """
        Inspeccionar el repositorio, documentar el pipeline en un archivo
        `.md`, o instalar librerías son **pasos necesarios**, no objetivos
        en sí mismos — sirven al objetivo específico 1 y 2, pero por sí
        solos no producen ningún valor para la universidad si se quedan
        ahí.
        """
    )

elif seccion == "7. Estado del arte":
    st.title("7. Estado del arte")

    st.markdown("### Bienestar estudiantil universitario")
    st.markdown(
        """
        En Colombia se han propuesto modelos de evaluación de bienestar
        estudiantil universitario que integran información demográfica,
        salud, desarrollo humano, promoción socioeconómica, recreación,
        cultura y deporte.
        *(Fuente: Modelo de evaluación del bienestar estudiantil
        universitario en Colombia, SciELO)*

        El instrumento de 29 ítems y seis dimensiones usado en el estudio
        previo de la USTA corresponde al mismo tipo de escala que la
        adaptación española de la escala de Ryff, validada
        psicométricamente para población colombiana por Pineda Roa, Castro
        Muñoz y Chaparro Clavijo (2017). Investigaciones posteriores con
        esta escala en universitarios colombianos reportan niveles
        generales de bienestar psicológico altos, con variaciones
        asociadas principalmente a la edad.
        *(Fuente: Ciencia Latina, Evaluación del Bienestar Psicológico de
        Estudiantes Universitarios de Psicología, 2024)*
        """
    )

    st.markdown("### Dos enfoques distintos para medir "'"bienestar"'" — y por qué importa la diferencia")
    st.markdown(
        """
        La literatura revisada contrasta dos formas de medir el bienestar
        que **no son intercambiables**:

        - **Bienestar psicológico multidimensional (Ryff, 6 dimensiones)**
          — el que usa el estudio de la USTA — mide autonomía, dominio del
          entorno, crecimiento personal, relaciones positivas, propósito
          vital y autoaceptación por separado.
        - **Bienestar subjetivo general (p. ej. WHO-5)** — usado en otros
          estudios universitarios latinoamericanos — mide con pocos ítems
          un estado de ánimo general, sin distinguir dimensiones.
          *(Fuente: Redalyc, Validez e invariancia factorial del Índice de
          Bienestar General WHO-5 en universitarios peruanos)*

        Esto importa para el agente: si en el futuro se compara el
        resultado de la USTA contra otro estudio, hay que verificar primero
        que ambos midieron el **mismo constructo** — de lo contrario la
        comparación es metodológicamente inválida, no solo una diferencia
        de cifras.
        """
    )

    pending(
        "¿Cuál de estas fuentes los hizo cambiar de idea sobre algo del "
        "diseño del proyecto, y en qué? Esa es una pregunta de reflexión "
        "del equipo — no se puede completar sin que ustedes mismos "
        "recuerden qué leyeron y qué les hizo dudar."
    )

    st.markdown("### Por qué este proyecto no es una repetición de lo ya leído")
    st.markdown(
        """
        Toda la literatura revisada **mide** bienestar estudiantil — ninguna
        de esas fuentes construye una herramienta de IA para **explorar,
        replicar y volver consultable en un dashboard** un estudio de
        bienestar ya hecho. El aporte de este proyecto no es un instrumento
        de medición nuevo, sino la capa de validación y presentación que
        falta después de que la medición ya se hizo.
        """
    )

    st.markdown("### Agentes de IA como orquestadores (no como calculadoras)")
    st.markdown(
        """
        La literatura técnica distingue entre un LLM usado como chatbot
        simple y un **agente LLM**, que usa el modelo como motor de
        razonamiento rodeado de herramientas para planificar y ejecutar
        tareas.
        *(Fuente: DataCamp, explicación sobre agentes LLM)*

        Los marcos de orquestación actuales permiten que un LLM
        descomponga una consulta en subtareas, delegue cada una a un
        componente especializado (validación, cálculo, consulta externa) y
        unifique los resultados en una respuesta trazable — el mismo
        principio que separa aquí el LLM (orquestador) del cálculo
        estadístico (código Python).
        *(Fuentes: IBM, orquestación de LLM; IIC, agentes inteligentes
        basados en LLM)*
        """
    )

elif seccion == "8. Resumen corto de los datos":
    st.title("8. Resumen corto de los datos")

    col1, col2, col3 = st.columns(3)
    col1.metric("Respuestas válidas", "1.813")
    col2.metric("Población objetivo", "≈ 29.950")
    col3.metric("Ítems / dimensiones", "29 / 6")

    st.markdown("### Archivos identificados (nombres, aún sin abrir su contenido)")
    st.markdown(
        """
        `Formulario de la escala de bienestar subjetivo - Resultados
        Finales (1)` · `Indice_Felicidad_Dataset_Limpio` ·
        `01_dataset_preparado` · `dataset_con_factores_expansion` ·
        `03_dataset_IRT_ponderado` · `Indice_Felicidad_Estandarizado_IRT` ·
        `Parametros_GRM` · `Tabla_Programa_NBC` · seis archivos
        `muestra_<sede>[_<nivel>]_estudio_felicidad_santoto_2025`
        (Bogotá, Bucaramanga pregrado/posgrado, Tunja, Villavicencio
        pregrado/posgrado)
        """
    )

    st.markdown("### Variable que responde al primer objetivo específico")
    st.markdown(
        "El objetivo específico 1 (EDA) depende de poder abrir todos "
        "estos archivos; el objetivo 2 (validar reproducibilidad) depende "
        "en particular de la variable de **T-score global** (o el theta "
        "del que se deriva), presente en "
        "`Indice_Felicidad_Estandarizado_IRT` — es la cifra puntual que "
        "hay que reproducir y comparar contra el valor reportado "
        "(≈ 50.7 según el informe anterior)."
    )

    pending(
        "¿Alguien del equipo ya abrió alguno de estos archivos? ¿Cuántas "
        "filas tiene el dataset real? Ninguna de las dos se puede "
        "responder todavía — es la primera tarea técnica antes de calcular "
        "nada."
    )

    st.markdown("### Qué hacer si el dato no llega a tiempo")
    st.markdown(
        """
        Si alguno de los archivos no llega o no se puede abrir a tiempo,
        el plan es **no detener todo el proyecto**: se documenta
        explícitamente qué archivo falta y qué parte del análisis queda
        bloqueada por eso, y se avanza con los archivos que sí están
        disponibles (por ejemplo, se puede hacer EDA y estadística
        descriptiva aunque falte el archivo de parámetros GRM, pero no se
        podría reproducir el T-score). El alcance se recorta de forma
        explícita, nunca se rellena el vacío con un valor inventado.
        """
    )
