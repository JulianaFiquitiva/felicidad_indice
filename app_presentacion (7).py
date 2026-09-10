"""
Presentación del proyecto — Agente de IA para el Índice de Bienestar/Felicidad Estudiantil (USTA)
Materia: Consultoría e Investigación · Docente: Javier Mauricio Sierra
Ejecutar con:  streamlit run app_presentacion.py
"""

import streamlit as st

st.set_page_config(
    page_title="Bienestar Estudiantil USTA",
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
.rq-box {
    background: linear-gradient(135deg, #1e1b4b 0%, #312e81 100%);
    border: 1px solid #4338ca; border-radius: 14px; padding: 20px 24px;
    color: #e0e7ff; font-size: 19px; font-weight: 600; line-height: 1.4;
    margin: 14px 0 20px 0;
}
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
st.sidebar.title("📊 Bienestar Estudiantil")
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
            "Inicio",
            "Qué incluye el agente",
            "El proceso que se quiere desarrollar",
            "Cómo se presenta: el dashboard",
        ],
    )
else:
    seccion = st.sidebar.radio(
        "Sección",
        [
            "La pregunta de investigación",
            "El estudio que se hizo",
            "Resumen de los datos y evaluación",
            "Objetivos",
            "Estado del arte",
        ],
    )

# =================================================================
# PARTE 1 · EL AGENTE DE IA
# =================================================================

if seccion == "Inicio":
    st.title("Agente de IA para el Índice de Bienestar Estudiantil")
    st.subheader("Universidad Santo Tomás · Herramienta de apoyo a la toma de decisiones institucional")

    col1, col2, col3 = st.columns(3)
    col1.metric("Respuestas del estudio previo", "1.813")
    col2.metric("Población objetivo aprox.", "29.950")
    col3.metric("Ítems tipo Likert", "29")

    st.markdown(
        """
        Esta presentación tiene dos partes independientes:

        **Parte 1 — el agente de IA en sí**: qué es, qué incluye, qué
        insights de inteligencia artificial se le aplican, y el proceso
        que se va a desarrollar para construirlo.

        **Parte 2 — el proyecto**: la réplica del estudio de bienestar
        estudiantil de la USTA, para responder con estadística una
        pregunta concreta sobre qué factores se asocian al bienestar bajo.
        """
    )
    st.info("Entrega — Materia de Consultoría e Investigación.")

elif seccion == "Qué incluye el agente":
    st.title("Qué incluye el agente")
    st.caption("Componentes, insights de IA aplicados y arquitectura por capas")

    st.markdown("### Los insights de IA que se aplican a este agente")
    c1, c2 = st.columns(2)
    with c1:
        concept_card(
            "🧠 Patrón orquestador (LLM + herramientas deterministas)",
            [
                "El LLM interpreta y decide, pero NUNCA calcula un número",
                "El cálculo estadístico siempre lo hace código Python",
                "Insight aplicado: separar razonamiento de cómputo evita "
                "que el modelo invente cifras",
            ],
        )
        concept_card(
            "🛠️ Herramientas de responsabilidad única",
            [
                "Cada función hace UNA cosa bien definida",
                "Mismo input → siempre el mismo output (determinismo)",
                "Insight aplicado: piezas pequeñas y auditables, no un "
                "prompt gigante que intenta hacerlo todo",
            ],
        )
    with c2:
        concept_card(
            "🗂️ Trazabilidad como principio de diseño",
            [
                "Cada respuesta registra dataset, filtros, método, parámetros",
                "Insight aplicado: en un contexto institucional, un "
                "resultado que no se puede auditar no sirve para decidir",
            ],
        )
        concept_card(
            "🚧 Guardrails (reglas que no se pueden romper)",
            [
                "No inventar variables, columnas ni resultados",
                "No usar lenguaje causal en datos observacionales",
                "No exponer información personal identificable",
            ],
        )

    st.markdown("### Estructura real del agente (código ya construido)")
    st.caption(
        "Carpeta por carpeta, con el módulo principal de cada una — no es "
        "una propuesta, es la estructura del repositorio actual."
    )
    col1, col2 = st.columns(2)
    with col1:
        layer_card(
            "agent/core — el cerebro",
            [
                "config.py — ítems, dimensiones, resultados reportados, rutas",
                "orchestrator.py — conecta LLM, motor estadístico, validadores y literatura",
                "query_planner.py — interpreta la pregunta en lenguaje natural",
            ],
        )
        layer_card(
            "agent/data — carga y perfilado",
            [
                "loader.py — carga los Excel, invierte ítems negativos",
                "profiler.py — EDA automático: tipos, faltantes, sensibles",
                "validator.py — integridad general de los datos",
            ],
        )
        layer_card(
            "agent/statistics — el motor",
            [
                "descriptive.py — estadística descriptiva ponderada",
                "inference.py — comparaciones con selección automática de prueba",
                "regression.py — OLS, WLS y logística con odds ratios",
                "statistical_engine.py — selector automático de método",
            ],
        )
    with col2:
        layer_card(
            "agent/psychometrics — psicometría e IRT",
            [
                "scale.py — alfa de Cronbach, correlación ítem-total",
                "irt.py — modelo GRM (librería girth), theta, T-scores",
            ],
        )
        layer_card(
            "agent/validation — los 4 validadores",
            [
                "psychometric_validator.py, irt_validator.py",
                "result_validator.py — compara contra lo reportado, con tolerancias",
                "survey_weights.py — factores de expansión y DEFF",
            ],
        )
        layer_card(
            "agent/literature, reports, ui, visualization",
            [
                "literature/searcher.py — busca en Crossref y PubMed (APIs gratuitas)",
                "reports/generator.py — informe ejecutivo, técnico, por seccional y comparativo",
                "ui/cli.py — interfaz de línea de comandos",
                "visualization/charts.py — histogramas, barras con IC, perfil de dimensiones",
            ],
        )

    st.markdown("### ¿Con qué IA, y qué pasa si falla?")
    st.markdown(
        """
        El agente soporta **tres proveedores de LLM** (OpenAI, Claude o
        Gemini) con detección automática de cuál está configurado — el
        LLM se usa como orquestador vía API (tool calling), y nunca recibe
        microdatos crudos, solo resultados ya agregados por el motor
        Python.

        Si **no hay ninguna clave de API configurada**, el agente no se
        detiene: cae en un **modo de respaldo por reglas**
        (`_fallback_plan()`) que detecta palabras clave como "género" o
        "seccional" y decide el análisis por coincidencia de texto en vez
        de por interpretación del LLM. Es más limitado, pero garantiza que
        el agente siga funcionando sin depender de una API externa.
        """
    )

    st.markdown("### El modelo IRT/GRM ya quedó resuelto: se hizo en Python")
    st.markdown(
        "Se implementó con la librería `girth`, con un método manual de "
        "respaldo si `girth` no está instalada — no hubo que interoperar "
        "con R."
    )

elif seccion == "El proceso que se quiere desarrollar":
    st.title("El proceso que se quiere desarrollar")
    st.caption("De los datos crudos al dashboard, paso a paso")

    flow_diagram(
        [
            ("1️⃣ EDA", "perfilar el dataset real"),
            ("2️⃣ Réplica", "recalcular lo del estudio anterior"),
            ("3️⃣ Validación", "comparar vs. lo reportado"),
            ("4️⃣ Variable de<br>bienestar bajo", "construirla desde el T-score"),
            ("5️⃣ Regresión<br>logística", "factores sociodemográficos y académicos"),
            ("6️⃣ Dashboard", "presentar todo de forma visual"),
        ]
    )

    st.markdown("### Qué implica cada paso")
    st.markdown(
        """
        1. **EDA** — conocer el dato real antes de asumir nada: tipos,
           faltantes, distribución de ítems y dimensiones, tamaño de
           muestra por grupo.
        2. **Réplica** — recalcular las medidas que ya aplicó el estudio
           anterior (alfa, GRM, T-scores, WLS) directamente desde el dataset.
        3. **Validación** — comparar cada cifra reproducida contra lo
           documentado y clasificarla (validado / diferencia menor /
           diferencia importante / no reproducible).
        4. **Construcción de la variable de bienestar bajo** — a partir del
           T-score ya calculado, definir el corte que separa "bienestar
           bajo" del resto, siguiendo el mismo criterio que usó el estudio
           anterior si ya existe, o dejándolo documentado si hay que
           definirlo.
        5. **Regresión logística** — modelar la probabilidad de bienestar
           bajo en función de las variables sociodemográficas (género,
           edad, estrato) y académicas (sede, modalidad, nivel de
           formación, semestre, programa), ponderando por el diseño
           muestral.
        6. **Dashboard** — mostrar todo lo anterior de forma interactiva,
           no como texto suelto.
        """
    )

elif seccion == "Cómo se presenta: el dashboard":
    st.title("Cómo se presenta: el dashboard")
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
    st.caption(
        "Cada panel corresponde a un tipo de informe que ya genera "
        "`reports/generator.py`: ejecutivo, técnico, por seccional y "
        "comparativo — el dashboard es la forma visual de mostrar esos "
        "mismos cuatro informes, no algo aparte."
    )
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
            "Panel del modelo de factores asociados",
            [
                "Odds ratios de la regresión logística, con su IC",
                "Qué variables aumentan o reducen la probabilidad de "
                "bienestar bajo",
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

elif seccion == "La pregunta de investigación":
    st.title("Planteamiento del problema y pregunta de investigación")

    st.markdown("### Planteamiento del problema")
    st.markdown(
        """
        El bienestar psicológico de los estudiantes universitarios es un
        aspecto fundamental para su desarrollo integral y para su
        experiencia académica, personal y social. Las instituciones de
        educación superior necesitan información confiable sobre el
        bienestar de sus estudiantes para poder orientar acciones
        institucionales que respondan a las necesidades identificadas.

        En la USTA se midió el bienestar subjetivo de la comunidad
        estudiantil durante el segundo semestre de 2025, con una versión
        adaptada de la Escala de Bienestar Psicológico de Ryff (29 ítems,
        6 dimensiones). El puntaje T global resultante (≈ 50,7) se
        clasifica como un nivel medio de bienestar — pero **ese promedio no
        representa a todos los estudiantes por igual**: el propio estudio
        estima que cerca del 14,8 % de la población (~4.400 estudiantes)
        está en niveles bajo o muy bajo de bienestar, mientras que cerca
        del 19,2 % (~5.700 estudiantes) está en niveles alto o muy alto.

        Además, las diferencias **entre programas académicos dentro de una
        misma seccional** (hasta ~8 puntos T) son mucho mayores que las
        diferencias **entre seccionales** (~1 punto T, no significativas
        estadísticamente) — lo que indica que el problema no es geográfico,
        sino que está concentrado en programas específicos. También se
        observaron diferencias por modalidad (virtual por encima de
        presencial) y por nivel de formación (posgrado por encima de
        pregrado).

        Esto muestra que **un único promedio institucional no es
        suficiente** para tomar decisiones: hace falta identificar
        poblaciones prioritarias, reconocer brechas entre grupos, y aportar
        evidencia para diseñar estrategias de intervención — algo que el
        estudio anterior ya señaló como pendiente, incluyendo la necesidad
        de un monitoreo longitudinal con mediciones periódicas.
        """
    )

    st.markdown("### Pregunta de investigación")
    st.markdown(
        '<div class="rq-box">¿Cómo puede la validación y ampliación del '
        'Índice de Bienestar de los estudiantes de la Universidad Santo '
        'Tomás, complementada con un agente de inteligencia artificial, '
        'contribuir a la identificación de brechas y factores asociados '
        'al bienestar y al desarrollo de recomendaciones basadas en '
        'evidencia para apoyar la formulación y seguimiento de '
        'estrategias institucionales de bienestar y felicidad '
        'estudiantil?</div>',
        unsafe_allow_html=True,
    )

    st.markdown("### La sub-pregunta estadística que opera esto")
    st.markdown(
        """
        La pregunta institucional de arriba se responde, en la práctica,
        modelando estadísticamente: **¿qué factores sociodemográficos y
        académicos están asociados con la probabilidad de que un
        estudiante presente un nivel bajo de bienestar subjetivo?**
        """
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Variable de respuesta (dependiente)**")
        st.markdown(
            "Bienestar subjetivo **bajo/muy bajo** vs. resto — una "
            "variable binaria construida a partir del T-score / "
            "clasificación de bienestar que ya calculó el estudio anterior."
        )
    with col2:
        st.markdown("**Variables explicativas (independientes)**")
        st.markdown(
            "- Sociodemográficas: género, edad, estrato\n"
            "- Académicas: sede/seccional, **programa** (la brecha más "
            "marcada), modalidad, nivel de formación, semestre"
        )

    st.markdown("### Método propuesto")
    st.markdown(
        """
        **Regresión logística** (binaria), ponderada según el diseño
        muestral cuando corresponda, que permite estimar la probabilidad
        de bienestar bajo en función de cada variable y reportar
        **razones de probabilidades (odds ratios)** con su intervalo de
        confianza — es el método estándar en la literatura revisada para
        este tipo de pregunta (ver Estado del arte).
        """
    )

    st.markdown("### Por qué esta pregunta y no otra")
    st.markdown(
        """
        Le da **valor de decisión** a la universidad: no es solo "¿cómo
        está el bienestar en promedio?" —eso ya se respondió y esconde la
        brecha real—, sino **"¿qué perfil de estudiante y qué programas
        concentran el bienestar bajo, y qué tanto pesa cada factor?"** —
        una pregunta que una tabla de promedios por grupo no responde, pero
        un modelo de regresión logística sí.
        """
    )

elif seccion == "El estudio que se hizo":
    st.title("El estudio que se hizo")
    st.caption("Explicación del estudio anterior, base sobre la que se construye este proyecto")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            **Diseño del estudio previo**
            - 1.813 respuestas válidas
            - Población objetivo ≈ 29.950 estudiantes
            - Muestreo estratificado sistemático, con factores de expansión
            - 29 ítems tipo Likert (escala de 6 puntos), agrupados en 6
              dimensiones de bienestar psicológico (escala tipo Ryff)
            - Medición realizada en el segundo semestre de 2025
            """
        )
    with col2:
        st.markdown(
            """
            **Qué se hizo con esos datos**
            - Teoría Clásica de los Test y Teoría de Respuesta al Ítem
              (Modelo de Respuesta Graduada — GRM)
            - Estimación de theta y transformación a T-scores
            - Inferencia poblacional con factores de expansión
            - Comparaciones por seccional, programa, modalidad, nivel de
              formación, género, estrato y edad
            """
        )

    st.markdown("### Los resultados que ya reportó el estudio")
    r1, r2, r3 = st.columns(3)
    r1.metric("T global", "≈ 50,7", "nivel medio")
    r2.metric("Bienestar bajo/muy bajo", "≈ 14,8 %", "~4.400 estudiantes")
    r3.metric("Bienestar alto/muy alto", "≈ 19,2 %", "~5.700 estudiantes")

    st.markdown(
        """
        - Las diferencias **entre programas académicos** (dentro de una
          misma seccional) llegan hasta **~8 puntos T** — la brecha más
          grande encontrada en todo el estudio.
        - Las diferencias **entre seccionales** son de solo ~1 punto T y
          **no resultaron estadísticamente significativas** — es decir, el
          problema no es de sede, es de programa.
        - Modalidad **virtual** por encima de modalidad **presencial**.
        - **Posgrado** (especialización/maestría) por encima de
          **pregrado**.
        - El propio estudio propone monitoreo longitudinal, focalizar
          acciones en estudiantes de bienestar bajo, y priorizar los
          programas con peores resultados.
        """
    )

    st.markdown("### Lo que este proyecto retoma de ese estudio")
    st.markdown(
        """
        - El **dataset y su pipeline** (preparación, ponderación,
          estandarización IRT) como base a auditar y reutilizar.
        - La **clasificación de bienestar** (T-score / categorías bajo,
          medio, alto) como punto de partida para construir la variable
          binaria de "bienestar bajo" que responde la pregunta de
          investigación.
        - Las **variables sociodemográficas y académicas** ya recolectadas,
          con especial atención a **programa** (la variable donde ya se vio
          la brecha más marcada) como predictor del modelo.
        """
    )

    st.markdown("### Lo que este proyecto agrega")
    st.markdown(
        """
        El estudio anterior **describió** el bienestar (un promedio global
        y comparaciones grupo a grupo) y **señaló** que hace falta
        profundizar en factores asociados y recomendaciones basadas en
        evidencia — pero no llegó a construir esa capa. Este proyecto la
        construye: **modela la probabilidad** de que un estudiante
        presente bienestar bajo en función de varios factores a la vez, y
        lo entrega mediante un agente de IA que deja el proceso trazable y
        reutilizable, no un informe estático más.
        """
    )

elif seccion == "Resumen de los datos y evaluación":

    st.title("Resumen de los datos y evaluación")

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

    st.markdown("### Las 6 dimensiones que mide la escala")
    st.caption(
        "Qué significa cada una conceptualmente — sin resultados, solo la "
        "definición de qué pregunta responde cada dimensión."
    )
    dim_col1, dim_col2 = st.columns(2)
    dimensiones = [
        ("1. Autoaceptación", "¿Te sientes bien siendo quien eres?",
         "Mide qué tanto te aceptas con tus fortalezas y debilidades. "
         "Incluye sentirte en paz con tu historia personal, reconocer tus "
         "logros y también tus áreas por mejorar, sin juzgarte con dureza."),
        ("2. Crecimiento personal", "¿Sientes que estás creciendo?",
         "Mide si sientes que estás en un proceso de desarrollo continuo, "
         "que aprendes cosas nuevas, que te abres a nuevas experiencias y "
         "que eres mejor persona que hace un año."),
        ("3. Propósito de vida", "¿Sabes hacia dónde vas?",
         "Mide si tienes objetivos claros, si sientes que tu vida tiene "
         "dirección y sentido. No se trata de tener todo planeado, sino de "
         "sentir que lo que haces tiene un propósito."),
        ("4. Dominio del entorno", "¿Sientes que controlas tu vida?",
         "Evalúa si sientes que puedes manejar las demandas de tu día a "
         "día: tus responsabilidades académicas, tu tiempo, tus finanzas, "
         "tu entorno. Es la sensación de tener las cosas bajo control."),
        ("5. Relaciones positivas", "¿Tienes personas que te apoyan?",
         "Mide la calidad de tus relaciones interpersonales: si tienes "
         "personas en quienes confías, si sientes que puedes contar con "
         "alguien, si tus relaciones son significativas y no solo "
         "superficiales."),
        ("6. Autonomía", "¿Tomas tus propias decisiones?",
         "Evalúa si sientes que eres dueño de tus decisiones, si actúas "
         "por convicción propia y no solo por presión social, y si puedes "
         "resistir la presión de \"hacer lo que todos hacen\"."),
    ]
    for i, (titulo, pregunta, desc) in enumerate(dimensiones):
        col = dim_col1 if i % 2 == 0 else dim_col2
        with col:
            with st.expander(f"{titulo} — {pregunta}"):
                st.markdown(desc)

    st.markdown("### Los 29 ítems: dimensión, inversión y sentido")
    st.caption(
        "Tomado del Cuadro 3 (Asignación dimensional e inversión de los "
        "29 ítems de la escala). Sentido '+' = a mayor puntaje, mayor "
        "bienestar; sentido '−' = ítem redactado en negativo, se invierte "
        "antes de analizarse."
    )
    dim_nombre = {
        "AU": "Autoaceptación", "CP": "Crecimiento personal",
        "PV": "Propósito de vida", "DE": "Dominio del entorno",
        "RP": "Relaciones positivas", "AT": "Autonomía",
    }
    items_escala = [
        (1, "AU", "Satisfacción con la mayoría de aspectos de mi personalidad", "No", "+"),
        (2, "RP", "A menudo me siento solo/a porque tengo pocos amigos", "Sí", "−"),
        (3, "CP", "Siento que con el tiempo he crecido mucho como persona", "No", "+"),
        (4, "PV", "No tengo una buena idea de lo que intento hacer en la vida", "Sí", "−"),
        (5, "DE", "Las demandas de la vida diaria a menudo me deprimen", "Sí", "−"),
        (6, "AT", "Soy capaz de resistir las presiones sociales", "No", "+"),
        (7, "AU", "En general, me siento seguro/a y positivo/a conmigo mismo/a", "No", "+"),
        (8, "RP", "No tengo muchas personas dispuestas a escucharme", "Sí", "−"),
        (9, "CP", "No quiero intentar nuevas formas de hacer las cosas", "Sí", "−"),
        (10, "PV", "Tengo clara la dirección y el objetivo de mi vida", "No", "+"),
        (11, "DE", "Soy bueno/a manejando responsabilidades diarias", "No", "+"),
        (12, "AT", "Tengo confianza en mis opiniones, incluso si son contrarias", "No", "+"),
        (13, "AU", "A veces no me siento satisfecho/a conmigo mismo/a", "Sí", "−"),
        (14, "RP", "Siento que mis amistades me aportan muchas cosas", "No", "+"),
        (15, "CP", "Pienso que es importante tener nuevas experiencias", "No", "+"),
        (16, "PV", "Mis objetivos en la vida han sido fuente de satisfacción", "No", "+"),
        (17, "DE", "He sido capaz de construir un modo de vida a mi gusto", "No", "+"),
        (18, "AT", "Suelo preocuparme por lo que otra gente piensa de mí", "No", "+"),
        (19, "AU", "Me gusta la mayor parte de mi forma de ser", "Sí", "−"),
        (20, "RP", "Me parece que la mayor parte de la gente tiene más amigos", "No", "+"),
        (21, "PV", "Disfruto haciendo planes para el futuro", "No", "+"),
        (22, "DE", "A menudo me siento abrumado/a por mis responsabilidades", "No", "+"),
        (23, "AT", "Es difícil para mí expresar mis opiniones en temas polémicos", "Sí", "−"),
        (24, "CP", "En general, siento que sigo aprendiendo sobre mí mismo/a", "No", "+"),
        (25, "PV", "Mi vida cotidiana es interesante para mí", "No", "+"),
        (26, "RP", "No he experimentado relaciones cálidas con los demás", "Sí", "−"),
        (27, "DE", "Soy capaz de organizar mi tiempo de manera eficaz", "No", "+"),
        (28, "AT", "No me preocupa lo que los demás piensen de mis decisiones", "No", "+"),
        (29, "DE", "Soy capaz de manejar situaciones difíciles", "No", "+"),
    ]
    with st.expander("Ver la tabla completa de los 29 ítems"):
        st.table(
            {
                "Ítem": [it[0] for it in items_escala],
                "Dim.": [it[1] for it in items_escala],
                "Dimensión": [dim_nombre[it[1]] for it in items_escala],
                "Contenido abreviado": [it[2] for it in items_escala],
                "Inv.": [it[3] for it in items_escala],
                "Sentido": [it[4] for it in items_escala],
            }
        )
        st.caption(
            "Tras la inversión, un puntaje más alto en cualquier ítem "
            "refleja mayor bienestar subjetivo; todos los análisis "
            "posteriores (TCT, IRT) operan sobre los datos ya invertidos."
        )

    st.markdown("### Evaluación: ¿tenemos lo que necesita el modelo?")
    st.markdown(
        """
        | Necesita el modelo | ¿Se tiene? |
        |---|---|
        | Variable de bienestar (T-score / theta) para construir la variable binaria | Sí, en `Indice_Felicidad_Estandarizado_IRT` (a confirmar al abrir el archivo) |
        | Variables sociodemográficas (género, edad, estrato) | Sí, reportadas como recolectadas en el estudio previo |
        | Variables académicas (sede, modalidad, nivel de formación, semestre, programa) | Sí, incluyendo `Tabla_Programa_NBC` para el núcleo básico de conocimiento |
        | Factores de expansión, para ponderar el modelo | Sí, en `dataset_con_factores_expansion` |
        | Variable de ingreso económico | **No existe** — no se usa; el componente socioeconómico se cubre con estrato |
        """
    )

    st.markdown("### Qué hacer si el dato no llega a tiempo")
    st.markdown(
        """
        Si algún archivo no llega o no se puede abrir a tiempo, se
        documenta explícitamente qué queda bloqueado por eso y se avanza
        con lo disponible — por ejemplo, se puede hacer EDA y estadística
        descriptiva sin el archivo de parámetros GRM, pero no se podría
        reproducir el T-score exacto. El alcance se recorta de forma
        explícita, nunca se rellena el vacío con un valor inventado.
        """
    )

elif seccion == "Objetivos":
    st.title("Objetivos")

    st.markdown("### Objetivo general")
    st.success(
        "Validar y ampliar el Índice de Bienestar Estudiantil de la USTA "
        "mediante un agente de inteligencia artificial que identifique "
        "brechas y factores sociodemográficos y académicos asociados al "
        "bienestar subjetivo bajo, y presente los resultados en un "
        "dashboard interactivo como evidencia para apoyar la formulación "
        "y seguimiento de estrategias institucionales de bienestar."
    )

    st.markdown("### Objetivos específicos")
    st.caption(
        "Cada uno deja una evidencia verificable — si los tres se "
        "cumplen, el objetivo general queda resuelto: el dato es confiable "
        "(1), el modelo responde la pregunta (2), y queda presentable y "
        "usable por la universidad (3)."
    )

    with st.expander("1. Replicar y validar el análisis del estudio anterior"):
        st.markdown(
            """
            Hacer el EDA del dataset real y reproducir los indicadores
            clave (n, alfa de Cronbach, T-score global, comparaciones por
            grupo) comparándolos contra lo documentado.

            **Evidencia de cumplimiento — ya construida:**
            `result_validator.py` compara cada indicador contra lo
            reportado con una tolerancia numérica definida (p. ej. n ±5 o
            1 %, T-global ±0,5 o 2 %, alfa ±0,02 o 3 %) y lo clasifica como
            VALIDADO, DIFERENCIA MENOR o NO REPRODUCIBLE. Esto está
            respaldado por **73 pruebas automáticas** (28 de datos, 39 del
            pipeline completo, 6 de casos de uso).
            """
        )

    with st.expander("2. Modelar los factores asociados al bienestar bajo"):
        st.markdown(
            """
            Construir la variable binaria de bienestar bajo a partir del
            T-score, y ajustar un modelo de regresión logística con las
            variables sociodemográficas y académicas disponibles,
            reportando odds ratios e intervalos de confianza.

            **Evidencia de cumplimiento:** la tabla de coeficientes del
            modelo, con su significancia e interpretación en términos de
            probabilidad.
            """
        )

    with st.expander("3. Presentar todo en un dashboard interactivo para la universidad"):
        st.markdown(
            """
            Entregar el EDA, la validación y el modelo de factores
            asociados en un dashboard visual, que las dependencias de la
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
        en sí mismos — sirven al objetivo específico 1, pero por sí solos
        no responden la pregunta de investigación ni producen valor para
        la universidad.
        """
    )

elif seccion == "Estado del arte":
    st.title("Estado del arte")

    st.markdown("### La escala y el estudio base")
    st.markdown(
        """
        El instrumento de 29 ítems y seis dimensiones usado en el estudio
        previo de la USTA corresponde al mismo tipo de escala que la
        adaptación española de la escala de bienestar psicológico de Ryff,
        validada psicométricamente para población colombiana por Pineda
        Roa, Castro Muñoz y Chaparro Clavijo (2017).
        *(Fuente: Pensamiento Psicológico, vía Ciencia Latina)*
        """
    )

    st.markdown("### Precedentes metodológicos directos: regresión logística sobre bienestar/salud mental estudiantil")
    st.markdown(
        """
        La pregunta de este proyecto tiene precedentes metodológicos claros
        en la literatura colombiana y latinoamericana:

        - Un estudio en una universidad de la costa Atlántica colombiana
          (n = 6.224) usó regresión logística para relacionar variables
          sociodemográficas —sexo, edad, estado civil, estrato, programa
          académico— con la presencia de ansiedad y depresión en
          estudiantes universitarios, encontrando asociaciones
          significativas con varias de esas variables.
          *(Fuente: Universitas Psychologica, Redalyc)*
        - Un estudio con la escala de bienestar psicológico de Ryff en
          estudiantes universitarios usó **regresión logística binomial**
          para relacionar ansiedad y resiliencia con el bienestar
          psicológico, reportando razones de posibilidades (OR) con su
          intervalo de confianza — el mismo tipo de resultado que se
          espera producir en este proyecto.
          *(Fuente: Revista Guatemalteca de Educación Superior)*
        - Un estudio con estudiantes de ciencias de la salud usó regresión
          logística para identificar los factores que mejor explican la
          sintomatología depresiva y la ansiedad, reportando razones de
          prevalencia ajustadas con intervalos de confianza.
          *(Fuente: revista indexada en SciELO Colombia)*

        Estos antecedentes confirman que la regresión logística —con
        variables sociodemográficas y académicas como predictoras, y
        odds ratios como resultado— es el método estándar y ya validado
        en este dominio, no una elección arbitraria.
        """
    )

    st.markdown("### Dos enfoques distintos para medir "'"bienestar"'" — y por qué importa la diferencia")
    st.markdown(
        """
        - **Bienestar psicológico multidimensional (Ryff, 6 dimensiones)**
          — el que usa el estudio de la USTA — mide autonomía, dominio del
          entorno, crecimiento personal, relaciones positivas, propósito
          vital y autoaceptación por separado.
        - **Bienestar subjetivo general (p. ej. WHO-5)** — usado en otros
          estudios universitarios latinoamericanos — mide con pocos ítems
          un estado de ánimo general, sin distinguir dimensiones.
          *(Fuente: Redalyc, Índice de Bienestar General WHO-5 en
          universitarios peruanos)*

        Esto importa porque, si en el futuro se compara el resultado de la
        USTA contra otro estudio, hay que verificar primero que ambos
        midieron el **mismo constructo** — de lo contrario la comparación
        es metodológicamente inválida, no solo una diferencia de cifras.
        """
    )

    st.markdown("### Por qué este proyecto no es una repetición de lo ya leído")
    st.markdown(
        """
        La literatura revisada modela factores asociados a bienestar o
        salud mental **a partir de una encuesta levantada para ese fin
        específico**. Este proyecto aplica ese mismo tipo de modelo sobre
        una encuesta **ya existente**, construida originalmente con otro
        objetivo (índice de bienestar con enfoque psicométrico/IRT), y lo
        hace mediante un **agente de IA que automatiza y deja trazable**
        todo el proceso de validación y modelado — eso no aparece en
        ninguna de las fuentes revisadas.
        """
    )

    st.markdown("### Agentes de IA y dashboards ya aplicados en contexto universitario")
    st.markdown(
        """
        - La **Universidad Nacional Autónoma de Honduras (UNAH)** opera un
          tablero interactivo ("Mi Bienestar UNAH") que caracteriza el
          bienestar estudiantil de forma multidimensional (académico,
          socioeconómico, salud, alimentario) para generar evidencia de
          decisión institucional — es el precedente más cercano en formato
          de entrega (dashboard institucional de bienestar).
          *(Fuente: Observatorio Universitario UNAH)*
        - Algunas universidades (p. ej. Universidad de California) ya usan
          **chatbots de IA de bienestar** que dan consejos personalizados
          directamente al estudiante.
          *(Fuente: Innovación Educativa UPC)*
        - Se han propuesto modelos de **machine learning** (Random Forest,
          XGBoost, redes neuronales) para identificar tempranamente
          vulnerabilidad emocional y estrés académico a partir de variables
          múltiples.
          *(Fuente: modelo de IA para mitigación del estrés académico,
          SciELO)*
        - La literatura sobre agentes de IA institucionales insiste en que
          las trazas de auditoría y la supervisión humana deben quedar
          almacenadas y accesibles — el mismo principio de trazabilidad que
          gobierna el diseño de este agente.
          *(Fuente: Agentes de IA para universidades — apoyo a la
          educación superior)*
        """
    )

    st.markdown("### Comparación: qué se ha hecho vs. qué se quiere hacer aquí")
    st.table(
        {
            "Fuente / estudio": [
                "Pineda Roa et al. (2017) — escala Ryff Colombia",
                "Universitas Psychologica (n=6.224)",
                "Rev. Guatemalteca de Ed. Superior",
                "UNAH — 'Mi Bienestar UNAH'",
                "Chatbot de bienestar (Univ. de California)",
                "Modelo IA estrés académico (RF/XGBoost)",
            ],
            "Palabras clave": [
                "bienestar psicológico, escala Ryff, validación psicométrica",
                "regresión logística, factores sociodemográficos, ansiedad/depresión",
                "bienestar psicológico, regresión logística, odds ratio",
                "dashboard, bienestar multidimensional, decisión institucional",
                "chatbot, IA conversacional, apoyo psicológico",
                "machine learning, predicción de riesgo, estrés académico",
            ],
            "Qué hicieron": [
                "Validaron el instrumento de 29 ítems / 6 dimensiones en Colombia",
                "Asociaron variables sociodemográficas con síntomas clínicos",
                "Relacionaron ansiedad/resiliencia con bienestar vía logística",
                "Tablero visual de bienestar para toma de decisiones",
                "Dan consejos personalizados en tiempo real al estudiante",
                "Predicen riesgo individual con modelos de caja negra",
            ],
            "Coincide con este proyecto en": [
                "el mismo instrumento (29 ítems, 6 dimensiones)",
                "el mismo método (regresión logística) y tipo de predictores",
                "instrumento + método + tipo de resultado (OR e IC)",
                "el formato de entrega (dashboard institucional)",
                "el uso de IA en el dominio de bienestar estudiantil",
                "el objetivo de identificar estudiantes en riesgo",
            ],
            "Se diferencia en": [
                "solo valida el instrumento, no construye herramienta de consulta",
                "mide síntomas clínicos, no bienestar psicológico; sin IA ni dashboard",
                "encuesta levantada para ese fin, sin agente de IA ni reutilización",
                "sin modelo inferencial (regresión) ni agente de IA orquestador",
                "apoyo directo al estudiante, no evidencia para la institución",
                "modelo de caja negra, sin la interpretabilidad (OR, IC) que exige la decisión institucional",
            ],
        }
    )
    st.caption(
        "El aporte de este proyecto está en la intersección de las tres "
        "columnas: mismo instrumento y método estadístico que la "
        "literatura clínica, mismo formato de entrega que los dashboards "
        "institucionales, y el principio de trazabilidad de los agentes de "
        "IA institucionales — pero sobre una encuesta ya existente, no "
        "levantada de nuevo."
    )
