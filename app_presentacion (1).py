"""
Presentación del proyecto — Agente de IA para el Índice de Bienestar/Felicidad Estudiantil (USTA)
Materia: Consultoría e Investigación
Ejecutar con:  streamlit run app_presentacion.py
"""

import streamlit as st

st.set_page_config(
    page_title="Agente IA - Índice de Bienestar Estudiantil USTA",
    page_icon="📊",
    layout="wide",
)

# ---------------------------------------------------------------
# ESTILOS PARA DIAGRAMAS DE FLUJO (HTML/CSS embebido)
# ---------------------------------------------------------------
FLOW_CSS = """
<style>
.flow-wrap {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 6px;
    margin: 14px 0 22px 0;
}
.flow-box {
    background: #1e293b;
    border: 1px solid #3b82f6;
    border-radius: 10px;
    padding: 12px 16px;
    color: #e2e8f0;
    font-size: 14px;
    min-width: 150px;
    text-align: center;
    line-height: 1.3;
}
.flow-box small { color: #94a3b8; }
.flow-arrow { color: #3b82f6; font-size: 22px; padding: 0 2px; }
.loop-box {
    background: #1e293b;
    border: 2px solid #a855f7;
    border-radius: 12px;
    padding: 14px 16px;
    color: #e2e8f0;
    font-size: 14px;
    min-width: 150px;
    text-align: center;
    line-height: 1.3;
}
.loop-box small { color: #c4b5fd; }
.loop-arrow { color: #a855f7; font-size: 22px; padding: 0 2px; }
.layer-card {
    background: #111827;
    border: 1px solid #334155;
    border-left: 5px solid #3b82f6;
    border-radius: 10px;
    padding: 14px 16px;
    margin-bottom: 12px;
}
.layer-title { color: #93c5fd; font-weight: 700; margin-bottom: 6px; }
.layer-item { color: #e2e8f0; font-size: 13.5px; margin: 2px 0; }
.concept-card {
    background: #111827;
    border: 1px solid #334155;
    border-left: 5px solid #a855f7;
    border-radius: 10px;
    padding: 14px 16px;
    margin-bottom: 12px;
}
.concept-title { color: #d8b4fe; font-weight: 700; margin-bottom: 6px; }
.concept-item { color: #e2e8f0; font-size: 13.5px; margin: 2px 0; }
.risk-solved { color: #4ade80; font-weight: 600; }
.risk-residual { color: #fbbf24; font-weight: 600; }
</style>
"""
st.markdown(FLOW_CSS, unsafe_allow_html=True)


def flow_diagram(steps, style="flow"):
    """steps: list of (title, subtitle_or_None). style: 'flow' or 'loop'."""
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


# ---------------------------------------------------------------
# SIDEBAR — NAVEGACIÓN
# ---------------------------------------------------------------
st.sidebar.title("📊 Agente IA — Bienestar Estudiantil")
st.sidebar.caption("Universidad Santo Tomás · Consultoría e Investigación")

seccion = st.sidebar.radio(
    "Navegación",
    [
        "0. Portada",
        "1. ¿Qué es un agente de IA?",
        "2. Datos e información del estudio",
        "3. Qué hace el agente",
        "4. Cómo funciona el agente",
        "5. Resultados que muestra",
        "6. Riesgos",
        "7. Diferencial y próximos pasos",
        "8. Entorno y herramientas de trabajo",
    ],
)

# =================================================================
# 0. PORTADA
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
        consultar esos resultados de forma reproducible y trazable — con
        miras a una futura interfaz conversacional tipo chatbot.
        """
    )
    st.info("Entrega — Materia de Consultoría e Investigación.")

# =================================================================
# 1. ¿QUÉ ES UN AGENTE DE IA? — sección conceptual profunda
# =================================================================
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
        que el usuario tenga que pedir cada uno por separado. Por ejemplo,
        para responder "¿hay diferencia de bienestar por género?", el
        agente no solo corre una prueba: primero verifica que la variable
        exista, revisa el tamaño de cada grupo, decide qué prueba estadística
        aplica, la ejecuta, y solo después redacta la respuesta.
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
                "Cada herramienta hace UNA cosa bien definida "
                "(un t-test, un alfa de Cronbach, un gráfico)",
                "Mismo input → siempre el mismo output (a diferencia del LLM)",
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

    st.markdown("## 1.4 El concepto técnico clave: *tool calling* / *function calling*")
    st.markdown(
        """
        Es el mecanismo que permite que un LLM, en vez de solo responder
        texto, pueda **invocar código externo de forma estructurada**: el
        modelo recibe una lista de "herramientas disponibles" (con su
        nombre, qué hace y qué parámetros necesita), y cuando detecta que
        una pregunta requiere una de ellas, genera una instrucción
        estructurada (no texto libre) para ejecutarla. El sistema ejecuta
        esa herramienta con código real, y el resultado —ya calculado por
        Python— se le devuelve al modelo para que lo interprete y lo
        redacte. **El modelo nunca "calcula": solo pide que se calcule.**
        """
    )

    st.markdown("## 1.5 Chatbot simple vs. Agente de IA (esta comparación es el corazón del proyecto)")
    st.markdown(
        """
        | | Chatbot simple (LLM aislado) | Agente de IA (este proyecto) |
        |---|---|---|
        | **Fuente de la respuesta** | Lo que el modelo "recuerda" de su entrenamiento | Cálculo real ejecutado sobre el dataset de la USTA |
        | **Acceso a datos propios** | No tiene acceso al dataset real | Sí, mediante herramientas conectadas al dataset |
        | **Cálculo numérico** | Lo genera el modelo (riesgo de alucinación) | Lo hace código Python determinista y auditable |
        | **Pasos múltiples** | Responde en un solo paso | Encadena pasos: validar → calcular → comparar → interpretar |
        | **Trazabilidad** | No explica cómo llegó al número | Registra dataset, método y parámetros usados |
        | **Fuentes externas** | Puede inventar referencias | Solo cita literatura que efectivamente consultó vía API |
        """
    )

    st.markdown("## 1.6 RAG: cómo el agente evita inventar literatura científica")
    st.markdown(
        """
        Para el módulo que consulta estudios externos, el agente usa el
        patrón **RAG (Retrieval-Augmented Generation — generación
        aumentada por recuperación)**: en vez de dejar que el LLM "recuerde"
        artículos (que podría inventar títulos, autores o cifras), el
        agente primero **recupera** artículos reales desde una fuente
        externa (PubMed, Crossref, etc.) y luego le entrega esos textos
        reales al LLM para que **solo los resuma** — el modelo no inventa la
        fuente, únicamente redacta sobre evidencia que sí existe.
        """
    )

    st.markdown("## 1.7 ¿Por qué SÍ es un agente de IA y no solo "'"un script con ChatGPT por encima"'"?")
    st.markdown(
        """
        Porque cumple las tres condiciones que distinguen a un agente:

        1. **Autonomía de decisión** — el agente decide qué método
           estadístico usar según los datos, no sigue un guion fijo escrito
           a mano para cada pregunta posible.
        2. **Uso de herramientas** — ejecuta código real (no solo genera
           texto) para producir cada resultado.
        3. **Encadenamiento de pasos con verificación** — valida, calcula,
           compara contra resultados previos y solo entonces responde; si
           algo no es posible (variable inexistente, muestra insuficiente),
           lo detecta y lo informa en vez de improvisar.
        """
    )

    st.markdown("## 1.8 Ejemplo aplicado, paso a paso")
    st.markdown('*Pregunta: "¿Hay diferencia en bienestar entre hombres y mujeres?"*')
    flow_diagram(
        [
            ("🧑 Pregunta", "del usuario"),
            ("🧭 Query Planner", "variable objetivo = T_global<br>variable de grupo = género"),
            ("⚙️ Statistical Engine", "revisa supuestos → elige<br>t-test o Mann-Whitney"),
            ("✅ Validator", "revisa tamaño de<br>muestra por grupo"),
            ("📝 Report Generator", "resultado + IC + tamaño<br>de efecto + interpretación"),
        ]
    )
    st.caption(
        "Cada flecha de este diagrama es una decisión autónoma del agente, "
        "no un paso que el usuario tuvo que pedir explícitamente."
    )

# =================================================================
# 2. DATOS E INFORMACIÓN DEL ESTUDIO
# =================================================================
elif seccion == "2. Datos e información del estudio":
    st.title("2. Datos e información del estudio")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
            **Diseño del estudio previo**
            - 1.813 respuestas válidas
            - Población objetivo ≈ 29.950 estudiantes
            - Muestreo estratificado, con factores de expansión
            - 29 ítems tipo Likert, agrupados en 6 dimensiones de bienestar
              psicológico
            - Análisis ya realizados: psicométrico, TRI/GRM, T-scores,
              inferencia poblacional, regresión WLS, comparaciones por
              seccional / modalidad / género / estrato / edad / programa
            """
        )
    with c2:
        st.markdown(
            """
            **Variables disponibles para el análisis**
            - Género, edad, estrato socioeconómico
            - Nivel de formación, modalidad, semestre
            - Sede/seccional, programa, núcleo básico de conocimiento (NBC)
            - Los 29 ítems + las 6 dimensiones + métrica global (T-score)
            - Factores de expansión (peso muestral)

            El análisis del componente socioeconómico se trabaja con
            **estrato**, que es la variable con la que sí cuenta el estudio.
            """
        )

    st.markdown("### Archivos del proyecto anterior")
    st.markdown(
        """
        | Archivo | Rol probable en el pipeline |
        |---|---|
        | `Formulario de la escala de bienestar subjetivo - Resultados Finales (1)` | Respuestas crudas de la encuesta |
        | `Indice_Felicidad_Dataset_Limpio` | Dataset depurado |
        | `01_dataset_preparado` | Dataset preparado para análisis |
        | `dataset_con_factores_expansion` | Dataset con pesos muestrales aplicados |
        | `03_dataset_IRT_ponderado` | Dataset con resultados IRT + ponderación |
        | `Indice_Felicidad_Estandarizado_IRT` | Resultados estandarizados (theta / T-score) |
        | `Parametros_GRM` | Parámetros del modelo GRM (discriminación, umbrales por ítem) |
        | `Tabla_Programa_NBC` | Tabla de equivalencia programa ↔ núcleo básico de conocimiento |
        | `muestra_bogota_estudio_felicidad_santoto_2025` | Marco muestral / muestra — sede Bogotá |
        | `muestra_bucaramanga_pregrado_estudio_felicidad_santoto_2025` | Marco muestral — Bucaramanga, pregrado |
        | `muestra_bucaramanga_posgrado_estudio_felicidad_santoto_2025` | Marco muestral — Bucaramanga, posgrado |
        | `muestra_tunja_estudio_felicidad_santoto_2025` | Marco muestral / muestra — sede Tunja |
        | `muestra_villavicencio_pregrado_estudio_felicidad_santoto_2025` | Marco muestral — Villavicencio, pregrado |
        | `muestra_villavicencio_posgrado_estudio_felicidad_santoto_2025` | Marco muestral — Villavicencio, posgrado |
        """
    )
    st.caption(
        "El rol de cada archivo se confirma inspeccionando su contenido "
        "(columnas y valores), no solo por su nombre — esa es la primera "
        "tarea técnica del agente."
    )

# =================================================================
# 3. QUÉ HACE EL AGENTE — mirada de estadístico
# =================================================================
elif seccion == "3. Qué hace el agente":
    st.title("3. Qué hace el agente")
    st.caption("Medidas y estudios estadísticos que ejecuta")

    st.markdown("### a) Replica y evalúa lo que ya se hizo")
    st.markdown(
        """
        El agente **reproduce las mismas medidas y modelos** que aplicó el
        estudio anterior (consistencia interna, GRM, T-scores, inferencia
        poblacional, WLS, comparaciones por grupo) y, además, **evalúa si
        siguen siendo pertinentes**: revisa supuestos, tamaño de muestra por
        subgrupo y calidad de ajuste, y si un método ya no es el más
        adecuado para una pregunta o subconjunto de datos, el agente lo
        señala y **propone una alternativa** (por ejemplo, una prueba no
        paramétrica en vez de una paramétrica si no se cumple normalidad).
        El objetivo es analizar el estudio **de forma integral**, no solo
        repetir cálculos de memoria.
        """
    )

    st.markdown("### b) Valida los resultados previos")
    st.markdown(
        """
        - Reproduce desde el dataset los indicadores reportados: *n*,
          consistencia interna (alfa de Cronbach), T-score global,
          proporciones de bienestar por categoría.
        - Compara cada resultado reproducido contra el valor documentado y
          lo clasifica como **validado / diferencia menor / diferencia
          importante / no reproducible**.
        - Valida el diseño muestral: consistencia de los factores de
          expansión, distribución por estrato y coherencia entre muestra y
          población.
        """
    )

    st.markdown("### c) Estadística descriptiva")
    st.markdown(
        """
        Frecuencias, porcentajes, medias, medianas, desviación estándar,
        percentiles e **intervalos de confianza**, siempre reportando el
        tamaño de muestra de cada subgrupo (una submuestra pequeña no
        permite las mismas conclusiones que la muestra completa).
        """
    )

    st.markdown("### d) Comparaciones entre grupos (por carrera, sede, género, edad, estrato…)")
    st.markdown(
        """
        El agente **no elige la prueba por popularidad**: evalúa tipo de
        variable, normalidad, homocedasticidad y tamaño de muestra, y
        selecciona:

        - **t-test** o **Mann-Whitney** (dos grupos, según se cumpla o no
          normalidad),
        - **ANOVA** o **Kruskal-Wallis** (más de dos grupos), con
          **pruebas post-hoc** cuando la diferencia global es significativa,
        - **chi-cuadrado** para variables categóricas,
        - y siempre reporta el **tamaño de efecto**, no solo el p-valor.
        """
    )

    st.markdown("### e) Asociaciones")
    st.markdown(
        "Correlación de Pearson o Spearman (según la escala de las "
        "variables) y tablas de contingencia para variables categóricas."
    )

    st.markdown("### f) Modelos de regresión — ¿qué factores explican el bienestar?")
    st.markdown(
        """
        - **Regresión WLS** (ponderada), continuando el enfoque del estudio
          anterior.
        - **Regresión logística / ordinal** cuando la variable de interés es
          una categoría de bienestar en vez del T-score continuo.
        - Revisa **colinealidad** entre predictores y reporta coeficientes
          con **intervalos de confianza, p-valores y R²**.
        """
    )

    st.markdown("### g) Disciplina de interpretación")
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown("**Descripción**")
    c1.caption('"El grupo A tiene mayor promedio."')
    c2.markdown("**Inferencia**")
    c2.caption('"Hay evidencia estadística de una diferencia."')
    c3.markdown("**Asociación**")
    c3.caption('"Las variables están asociadas."')
    c4.markdown("**Causalidad**")
    c4.caption("No se afirma — los datos son observacionales (encuesta), "
                "no un diseño experimental.")

# =================================================================
# 4. CÓMO FUNCIONA EL AGENTE — visual
# =================================================================
elif seccion == "4. Cómo funciona el agente":
    st.title("4. Cómo funciona el agente")
    st.caption("La aplicación concreta, en esta USTA, de los conceptos de la sección 1")

    st.markdown("### ¿De qué se alimenta?")
    flow_diagram(
        [
            ("📄 Dataset USTA", "ítems, dimensiones, sociodemográficas, pesos"),
            ("📑 Informes previos", "solo como punto de comparación"),
            ("🌐 Literatura externa", "PubMed, Crossref, OCDE, UNESCO, OMS"),
        ]
    )

    st.markdown("### ¿Con qué IA?")
    st.markdown(
        """
        Un **LLM usado como orquestador**: interpreta la pregunta, decide
        qué herramienta ejecutar y redacta la interpretación final. El
        **cálculo estadístico lo hace siempre código Python determinista**
        (pandas, scipy, statsmodels, librería de TRI para el GRM) — nunca
        un número generado directamente por el LLM. Esta separación evita
        que el modelo invente cifras.
        """
    )

    st.markdown("### Flujo de una consulta")
    flow_diagram(
        [
            ("🧑 Pregunta del<br>usuario", None),
            ("🧭 Query Planner", "identifica variables"),
            ("⚙️ Statistical Engine", "elige y ejecuta el método"),
            ("✅ Result / IRT<br>Validator", "revisa consistencia"),
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
                "Data / Weight Validator — dimensiones y factores de expansión",
                "Seguridad y anonimización",
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
            [
                "Statistical Engine — descriptivos, comparaciones, regresión",
                "Literature/API Agent — evidencia externa",
            ],
        )
        layer_card(
            "4 · Capa de orquestación y salida",
            [
                "Query Planner (LLM) — interpreta la pregunta",
                "Report Generator — informe final",
                "Trazabilidad — dataset, filtros, método, fecha",
            ],
        )

# =================================================================
# 5. RESULTADOS QUE MUESTRA
# =================================================================
elif seccion == "5. Resultados que muestra":
    st.title("5. Resultados que muestra el agente")
    st.caption("El resultado final siempre es un informe con el análisis del agente de IA")

    st.markdown("Cada respuesta del agente se entrega como un **informe**, no como una cifra suelta:")
    st.markdown(
        """
        1. **Pregunta** que se está respondiendo
        2. **Datos utilizados** (dataset, columnas, filtros aplicados)
        3. **Método estadístico** usado y por qué se eligió
        4. **Resultados** (tabla y/o gráfico)
        5. **Intervalos de confianza** / incertidumbre
        6. **Interpretación** en lenguaje comprensible para no estadísticos
        7. **Limitaciones** del análisis
        8. **Recomendaciones**, cuando aplique
        """
    )

    st.markdown("### Tipos de informe")
    st.markdown(
        """
        - **Informe ejecutivo** — hallazgos clave para la universidad, sin
          jerga estadística.
        - **Informe técnico** — método, supuestos, estadísticos completos,
          para auditoría o replicación.
        - **Informe por segmento** — por seccional, programa o grupo
          demográfico específico.
        - **Informe de validación** — comparación resultado anterior vs.
          reproducido.
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
# 6. RIESGOS
# =================================================================
elif seccion == "6. Riesgos":
    st.title("6. Riesgos")

    riesgos = [
        ("Archivos que no permiten reproducir el pipeline original",
         "Datos y reproducibilidad",
         "Se soluciona en la fase de inspección: se clasifica cada archivo "
         "por su contenido real (no por el nombre) antes de calcular nada.",
         True),
        ("Confundir un archivo depurado/ponderado con el original",
         "Datos y reproducibilidad",
         "Se soluciona documentando explícitamente el rol de cada archivo "
         "en docs/ANALISIS_PROYECTO_EXISTENTE.md antes de usarlo.",
         True),
        ("Subgrupos con muestra muy pequeña (ciertos programas o sedes)",
         "Estadístico",
         "Riesgo residual: se reporta el tamaño de muestra y el intervalo "
         "de confianza en cada resultado, pero no se puede aumentar la "
         "muestra ya recolectada.",
         False),
        ("Comparaciones múltiples (muchos grupos) inflan falsos positivos",
         "Estadístico",
         "Se soluciona aplicando corrección del umbral de significancia "
         "cuando se comparan varios grupos a la vez.",
         True),
        ("Interpretar asociación como causalidad",
         "Estadístico",
         "Se soluciona por diseño: el agente tiene prohibido usar lenguaje "
         "causal sobre datos observacionales.",
         True),
        ("Alucinación de cifras por parte del LLM",
         "Uso de IA",
         "Se soluciona con la arquitectura orquestador + motor estadístico "
         "separado: el LLM nunca calcula, solo interpreta resultados ya "
         "calculados por código.",
         True),
        ("El LLM simplifica de más al redactar un resultado técnico",
         "Uso de IA",
         "Riesgo residual: se mitiga con plantillas de informe fijas, pero "
         "requiere revisión humana periódica de la redacción.",
         False),
        ("Dependencia de APIs externas (literatura, LLM)",
         "Uso de IA",
         "Riesgo residual: costos, disponibilidad y límites de uso quedan "
         "fuera del control del proyecto.",
         False),
        ("Identificación indirecta en subgrupos pequeños",
         "Ético / privacidad",
         "Se soluciona anonimizando y agregando resultados por umbral "
         "mínimo de tamaño de grupo antes de mostrarlos.",
         True),
        ("Uso indebido de resultados para decisiones institucionales",
         "Ético / privacidad",
         "Riesgo residual: el agente incluye siempre limitaciones, pero no "
         "controla cómo se usa el informe una vez entregado.",
         False),
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

# =================================================================
# 7. DIFERENCIAL Y PRÓXIMOS PASOS
# =================================================================
elif seccion == "7. Diferencial y próximos pasos":
    st.title("7. Diferencial y próximos pasos")

    st.markdown("### ¿En qué se diferencia este agente de un chatbot común?")
    st.markdown(
        """
        Un chatbot corriente responde con lo que el LLM "cree" que es
        cierto, sin ejecutar cálculo real. Este agente separa
        explícitamente **razonamiento (LLM)** de **cálculo (código
        Python reproducible)**, y agrega **validación contra resultados
        previos** y **trazabilidad completa** de cada respuesta.
        """
    )

    st.markdown("### Próximos pasos inmediatos (fase 1)")
    pasos = [
        "Inspeccionar el contenido real de cada archivo del proyecto anterior",
        "Documentar el pipeline en docs/ANALISIS_PROYECTO_EXISTENTE.md",
        "Validar los resultados anteriores (n, alfa, T-score global, "
        "proporciones, diferencias por grupo)",
        "Construir el motor estadístico básico",
        "Construir el primer agente funcional (orquestador + herramientas)",
        "Pruebas automáticas de cada módulo",
    ]
    for i, paso in enumerate(pasos, start=1):
        st.markdown(f"**{i}.** {paso}")

    st.markdown("### Entregas futuras")
    st.markdown(
        """
        - Aplicativo interactivo que integra todos los resultados del
          estudio.
        - Interfaz conversacional (chatbot) para consultar los datos en
          lenguaje natural.
        - Generación automática de informes dinámicos.
        """
    )

# =================================================================
# 8. ENTORNO Y HERRAMIENTAS DE TRABAJO
# =================================================================
elif seccion == "8. Entorno y herramientas de trabajo":
    st.title("8. Entorno y herramientas de trabajo")

    st.markdown("### Dónde vive el proyecto")
    flow_diagram(
        [
            ("🐙 GitHub", "código, notebooks, docs, pruebas"),
            ("📓 Colab", "prototipado y validación rápida"),
            ("💻 VS Code / Codespaces", "construcción del agente como software"),
            ("🌐 Streamlit", "app / interfaz de resultados"),
        ]
    )

    col1, col2 = st.columns(2)
    with col1:
        layer_card(
            "Google Colab",
            [
                "Prototipar un cálculo puntual (¿se reproduce el GRM?, "
                "¿cómo se ve esta variable?)",
                "No requiere instalar nada, ya es el entorno donde se ha "
                "trabajado antes",
                "Ideal para exploración, no para organizar el agente "
                "completo como software",
            ],
        )
    with col2:
        layer_card(
            "VS Code / GitHub Codespaces",
            [
                "Construir el agente ya organizado en módulos "
                "(agent/core, agent/tools, agent/statistics…)",
                "Terminal integrada para correr pruebas (pytest) y la app "
                "de Streamlit",
                "Codespaces corre en la nube directo desde el botón "
                "'Code' del repo — no exige instalar nada localmente",
                "VS Code local hace lo mismo pero en el computador propio "
                "(requiere tener Python y Git instalados)",
            ],
        )

    st.markdown("### Librerías por tarea")
    st.markdown(
        """
        | Tarea | Herramienta |
        |---|---|
        | Manejo de datos | `pandas`, `numpy` |
        | Estadística clásica (t-test, ANOVA, chi-cuadrado, correlaciones) | `scipy.stats` |
        | Regresión (WLS, logística) e inferencia | `statsmodels` |
        | Modelo IRT / GRM | librería de TRI en Python (a definir si se replica en Python o si el estudio original usó R) |
        | Gráficos | `matplotlib` / `plotly` |
        | Pruebas automáticas | `pytest` |
        | Interfaz | `streamlit` |
        | LLM orquestador | API de un modelo de lenguaje (tool calling / function calling) |
        """
    )

    st.markdown("### Flujo de trabajo día a día")
    flow_diagram(
        [
            ("1️⃣ Prototipar<br>en Colab", None),
            ("2️⃣ Formalizar el<br>código en Codespaces", None),
            ("3️⃣ Subir a<br>GitHub", None),
            ("4️⃣ Correr como<br>app de Streamlit", None),
        ]
    )
