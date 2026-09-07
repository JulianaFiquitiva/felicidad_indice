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
# SIDEBAR — NAVEGACIÓN
# ---------------------------------------------------------------
st.sidebar.title("📊 Agente IA — Bienestar Estudiantil")
st.sidebar.caption("Universidad Santo Tomás · Consultoría e Investigación")

seccion = st.sidebar.radio(
    "Navegación",
    [
        "Portada",
        "Contexto",
        "Estado del arte",
        "Problema y justificación",
        "Objetivos",
        "Arquitectura propuesta del agente",
        "Principios metodológicos",
        "Alcance de esta entrega",
        "Hoja de ruta",
    ],
)

st.sidebar.divider()
st.sidebar.warning(
    "⚠️ Estado del proyecto: aún no se han cargado al agente los archivos "
    "originales del estudio anterior (dataset, notebooks, PDFs). Esta "
    "presentación cubre el marco teórico y la arquitectura propuesta; "
    "ningún resultado numérico aquí mostrado proviene de los datos reales."
)

# ---------------------------------------------------------------
# PORTADA
# ---------------------------------------------------------------
if seccion == "Portada":
    st.title("Agente de IA para el Índice de Bienestar Estudiantil")
    st.subheader("Universidad Santo Tomás · Continuación del proyecto de Índice de Felicidad")

    col1, col2, col3 = st.columns(3)
    col1.metric("Respuestas del estudio previo", "1.813")
    col2.metric("Población objetivo aprox.", "29.950")
    col3.metric("Ítems tipo Likert", "29")

    st.markdown(
        """
        ### ¿De qué trata este proyecto?
        Este proyecto **no inicia una encuesta nueva**: retoma el estudio de
        bienestar estudiantil realizado por estudiantes de la USTA (2025–2026)
        y construye sobre él un **agente de inteligencia artificial** capaz de:

        - **validar** los resultados que ya se obtuvieron,
        - **responder preguntas** analíticas sobre el bienestar estudiantil
          (por carrera, sede, género, edad, estrato, etc.),
        - **generar modelos estadísticos** (comparaciones, regresiones) de
          forma reproducible,
        - **contrastar los hallazgos** con literatura académica externa, y
        - **producir informes** comprensibles para la universidad.

        En entregas futuras, este agente será la base de una **aplicación
        interactiva tipo chatbot** para consultar el estudio en lenguaje natural.
        """
    )
    st.info(
        "Primera entrega — Materia de Consultoría e Investigación: "
        "**contexto, estado del arte y objetivos** del proyecto."
    )

# ---------------------------------------------------------------
# CONTEXTO
# ---------------------------------------------------------------
elif seccion == "Contexto":
    st.title("Contexto")

    st.markdown(
        """
        Un grupo de estudiantes de la Universidad Santo Tomás desarrolló
        previamente un estudio estadístico sobre **bienestar estudiantil**
        (2025–2026), con los siguientes elementos:
        """
    )

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
            **Diseño del estudio**
            - 1.813 respuestas válidas
            - Población objetivo ≈ 29.950 estudiantes
            - Muestreo estratificado con factores de expansión
            - 29 ítems tipo Likert agrupados en 6 dimensiones de
              bienestar psicológico
            """
        )
    with c2:
        st.markdown(
            """
            **Metodología estadística aplicada**
            - Análisis psicométrico (consistencia interna, alfa de Cronbach)
            - Teoría de Respuesta al Ítem (TRI) — Graded Response Model (GRM)
            - Estimación de θ (theta) y transformación a T-scores
            - Inferencia poblacional y pruebas de diferencias
            - Regresión WLS (ponderada por diseño muestral)
            - Análisis por seccional, modalidad, nivel de formación, género,
              estrato, edad y programa
            """
        )

    st.markdown("### Archivos que dejó el proyecto anterior (según lo informado)")
    st.markdown(
        """
        - `data/01_dataset_preparado.xlsx`
        - `notebooks/01_Preparacion_y_Diseno_Muestral.ipynb`
        - `notebooks/02_Analisis_Psicometrico.ipynb`
        - `notebooks/03_Estandarizacion_IRT.ipynb`
        - `notebooks/04_Inferencia_Poblacional.ipynb`
        - `docs/Informe_Cliente_Felicidad.pdf`
        - `docs/Informe_Ejecutivo_Felicidad.pdf`
        - `docs/Informe_Tecnico_IRT.pdf`
        - `docs/Presentacion_Ejecutiva.pdf`
        """
    )
    st.error(
        "🔴 Pendiente crítico: **ninguno de estos archivos ha sido cargado aún** "
        "al espacio de trabajo del agente. No se debe asumir que "
        "`01_dataset_preparado.xlsx` es el dataset original ni inventar su "
        "contenido — esto se determinará inspeccionando los archivos reales "
        "en la siguiente fase."
    )

# ---------------------------------------------------------------
# ESTADO DEL ARTE
# ---------------------------------------------------------------
elif seccion == "Estado del arte":
    st.title("Estado del arte")

    tab1, tab2 = st.tabs(
        ["Bienestar estudiantil universitario", "Agentes de IA para análisis de datos"]
    )

    with tab1:
        st.markdown(
            """
            **1. Modelos de evaluación del bienestar estudiantil universitario.**
            En Colombia se han propuesto modelos de evaluación de bienestar
            estudiantil universitario construidos a partir de la comparación de
            enfoques internacionales (cualitativos, cuantitativos y mixtos), que
            integran información demográfica, salud, desarrollo humano,
            promoción socioeconómica, recreación, cultura y deporte, entre
            otros componentes.
            *(Fuente: Modelo de evaluación del bienestar estudiantil
            universitario en Colombia, SciELO)*

            **2. La escala de Bienestar Psicológico de Ryff (29 ítems, 6 dimensiones).**
            El instrumento de 29 ítems y seis dimensiones usado en el estudio
            previo de la USTA corresponde al mismo tipo de escala que la
            adaptación española de la escala de Ryff, validada
            psicométricamente para población colombiana por Pineda Roa,
            Castro Muñoz y Chaparro Clavijo (2017) en *Pensamiento Psicológico*.
            Investigaciones posteriores con esta escala en universitarios
            colombianos reportan niveles generales de bienestar psicológico
            altos, con variaciones asociadas a la edad y diferencias leves
            —no siempre significativas— entre géneros.
            *(Fuente: Ciencia Latina, Evaluación del Bienestar Psicológico de
            Estudiantes Universitarios de Psicología, 2024)*

            **3. Relación entre bienestar subjetivo y vida universitaria.**
            En la literatura latinoamericana, el bienestar subjetivo en
            población universitaria se asocia con autoeficacia, optimismo y
            rendimiento académico, y con el apoyo social percibido; además se
            ha usado como indicador para el diseño de políticas institucionales
            de salud y bienestar.
            *(Fuente: Redalyc, Validez e invariancia factorial del Índice de
            Bienestar General WHO-5 en universitarios peruanos)*

            **4. Bienestar/calidad de vida y programas de bienestar universitario.**
            Otros estudios usan el concepto de calidad de vida como criterio
            para evaluar el impacto de los programas de bienestar
            universitario, vinculándolo con autoeficacia, satisfacción,
            compromiso e identidad institucional.
            *(Fuente: Redalyc, Impacto de los programas de bienestar
            universitario en la calidad de vida de los estudiantes)*

            **Vacío que atiende este proyecto:** la literatura revisada mide y
            valida el bienestar estudiantil, pero **no se identificaron
            antecedentes de un agente de IA que audite, reproduzca y permita
            consultar en lenguaje natural** los resultados de un estudio de
            bienestar estudiantil ya realizado — ahí está el aporte
            diferencial de este proyecto.
            """
        )

    with tab2:
        st.markdown(
            """
            **Agentes LLM como orquestadores, no como calculadoras.**
            La literatura técnica reciente distingue entre un LLM usado como
            chatbot simple (recibe una instrucción y genera una respuesta sin
            estado ni acciones externas) y un **agente LLM**, que usa el
            modelo como motor de razonamiento y lo rodea de herramientas para
            planificar y ejecutar tareas —desplazando el enfoque de la simple
            automatización hacia la autonomía guiada.
            *(Fuente: DataCamp, Explicación sobre los agentes LLM)*

            **Orquestación de sistemas multiagente.**
            Los marcos de orquestación actuales permiten que un LLM
            descomponga una consulta compleja en subtareas, delegue cada una a
            un componente especializado (validación, cálculo, consulta
            externa) y luego unifique los resultados en una respuesta
            trazable y auditable — el mismo principio que este proyecto aplica
            al separar el LLM (orquestador) del cálculo estadístico
            (código Python reproducible).
            *(Fuentes: IBM, ¿Qué es la orquestación de LLM?; IIC, Agentes
            inteligentes basados en LLM)*

            **Por qué importa para este proyecto:** el riesgo central de pedirle
            estadística a un LLM de forma directa es la alucinación de cifras.
            La arquitectura orquestador + herramientas deterministas es la
            práctica recomendada actualmente para evitar ese riesgo, y es la
            que se adopta aquí: el LLM interpreta la pregunta y decide qué
            herramienta ejecutar, pero **nunca calcula el resultado estadístico
            por sí mismo**.
            """
        )

# ---------------------------------------------------------------
# PROBLEMA Y JUSTIFICACIÓN
# ---------------------------------------------------------------
elif seccion == "Problema y justificación":
    st.title("Problema y justificación")

    st.markdown(
        """
        ### Problema
        El estudio previo de bienestar estudiantil generó resultados valiosos
        (informes técnico, ejecutivo y de cliente), pero estos resultados:

        - están **congelados en documentos estáticos** (PDF, notebooks
          sueltos) y no son fácilmente consultables por nuevos usuarios;
        - **no han sido validados de forma independiente y reproducible**
          desde el dataset;
        - no permiten responder **preguntas nuevas** (por ejemplo,
          combinaciones de variables no exploradas) sin repetir manualmente
          todo el proceso estadístico.

        ### Justificación
        Para la Universidad y para la materia de Consultoría e Investigación,
        tiene sentido **no repetir la encuesta**, sino:

        1. **Auditar** los resultados existentes con rigor estadístico
           (reproducibilidad), antes de confiar en ellos para nuevas
           decisiones institucionales.
        2. **Ampliar el valor** de los datos ya recolectados mediante consultas
           flexibles (por carrera, sede, género, edad, estrato, nivel de
           ingresos si existe la variable, etc.) y modelos de regresión.
        3. **Conectar los hallazgos con evidencia externa** (literatura
           académica) para contextualizar los resultados de la USTA frente a
           lo reportado en otras instituciones.
        4. Sentar las bases técnicas de una futura **aplicación conversacional**
           que democratice el acceso a estos resultados dentro de la
           universidad.
        """
    )

# ---------------------------------------------------------------
# OBJETIVOS
# ---------------------------------------------------------------
elif seccion == "Objetivos":
    st.title("Objetivos")

    st.markdown("### Objetivo general")
    st.success(
        "Desarrollar un agente de inteligencia artificial que permita "
        "**validar, analizar y consultar** el Índice de Bienestar "
        "Estudiantil de la Universidad Santo Tomás a partir de los datos y "
        "resultados del estudio previo, garantizando reproducibilidad "
        "estadística y trazabilidad de cada respuesta."
    )

    st.markdown("### Objetivos específicos")
    objetivos = [
        ("Inspeccionar y documentar el proyecto anterior",
         "Analizar la estructura del repositorio, los datasets, notebooks e "
         "informes existentes, para determinar qué archivo corresponde a "
         "cada etapa del pipeline (datos originales, depurados, ponderados, "
         "resultados IRT, resultados de inferencia), sin asumir ni inventar "
         "su contenido."),
        ("Validar los resultados previamente obtenidos",
         "Reproducir desde el dataset los indicadores reportados "
         "(tamaño de muestra, alfa de Cronbach, T-score global, "
         "proporciones de bienestar por categoría) y compararlos contra los "
         "valores documentados, clasificando cada uno como validado, con "
         "diferencia menor, con diferencia importante o no reproducible."),
        ("Construir un motor estadístico reproducible",
         "Implementar en código Python los análisis descriptivos, "
         "comparativos (t-test, ANOVA, chi-cuadrado, pruebas no paramétricas "
         "según corresponda) y modelos de regresión (WLS, logística según la "
         "variable objetivo), seleccionando el método según el tipo de "
         "variable y el diseño muestral."),
        ("Habilitar consultas analíticas por segmento",
         "Permitir análisis del bienestar/felicidad por carrera, sede, "
         "género, edad, estrato y demás variables sociodemográficas "
         "disponibles, e identificar de forma explícita las variables que "
         "no existen en el dataset (p. ej. ingresos, satisfacción "
         "explícita) en vez de asumirlas o simularlas."),
        ("Conectar el análisis con literatura externa",
         "Diseñar un módulo que consulte fuentes académicas (PubMed, "
         "Crossref, OCDE, UNESCO, OMS, repositorios institucionales) sobre "
         "bienestar estudiantil y registre título, autores, año, fuente y "
         "relación con los hallazgos de la USTA."),
        ("Generar informes de fácil comprensión",
         "Producir informes dinámicos (ejecutivo y técnico) que traduzcan "
         "los resultados estadísticos a un lenguaje comprensible para "
         "usuarios no especializados, conservando el rigor metodológico e "
         "incluyendo limitaciones e intervalos de confianza."),
        ("Sentar las bases de una futura interfaz conversacional",
         "Diseñar la arquitectura del agente (orquestador LLM + "
         "herramientas de cálculo) de forma que en una entrega posterior "
         "pueda exponerse como una aplicación interactiva tipo chatbot."),
    ]
    for i, (titulo, desc) in enumerate(objetivos, start=1):
        with st.expander(f"{i}. {titulo}"):
            st.write(desc)

# ---------------------------------------------------------------
# ARQUITECTURA
# ---------------------------------------------------------------
elif seccion == "Arquitectura propuesta del agente":
    st.title("Arquitectura propuesta del agente")

    st.markdown(
        """
        El agente **no es un chatbot que "adivina" estadísticas**: el LLM
        actúa como **orquestador** que decide qué herramienta ejecutar, y
        todo cálculo numérico lo realiza **código Python reproducible**.
        """
    )

    modulos = {
        "1. Data Profiler": "Detecta columnas, tipos, faltantes, categorías, "
            "tamaños de muestra, duplicados y variables sensibles.",
        "2. Data Validator": "Valida dimensiones, consistencia de categorías, "
            "duplicados, rangos de edad/estrato y factores de expansión.",
        "3. Survey Weight Validator": "Valida los factores de expansión y su "
            "consistencia con el diseño muestral estratificado.",
        "4. Psychometric Validator": "Valida los 29 ítems, ítems invertidos, "
            "las 6 dimensiones y la consistencia interna (alfa de Cronbach).",
        "5. IRT Validator": "Reproduce el modelo GRM: discriminaciones, "
            "umbrales, theta y T-scores.",
        "6. Result Validator": "Compara resultados reproducidos vs. los "
            "reportados en los informes anteriores (validado / diferencia "
            "menor / diferencia importante / no reproducible).",
        "7. Statistical Engine": "Selecciona automáticamente el método "
            "estadístico apropiado (descriptivos, comparaciones, "
            "asociaciones, modelos de regresión) según el tipo de variable, "
            "escala, supuestos y diseño muestral.",
        "8. Query Planner": "Interpreta la pregunta del usuario, identifica "
            "variables objetivo y de agrupación, verifica su existencia y "
            "tamaño de muestra, y decide si deben usarse pesos.",
        "9. Literature/API Agent": "Consulta fuentes externas (PubMed, "
            "Crossref, OCDE, UNESCO, OMS) sobre bienestar estudiantil y "
            "registra la evidencia consultada.",
        "10. Report Generator": "Genera informes ejecutivo, técnico y por "
            "grupo demográfico con método, resultados, intervalos de "
            "confianza, interpretación y limitaciones.",
        "11. Chat Interface (fase futura)": "Interfaz conversacional para "
            "preguntar en lenguaje natural sobre los resultados del estudio.",
        "12. Trazabilidad": "Cada respuesta registra dataset, columnas, "
            "filtros, pesos, método, parámetros y fecha de ejecución.",
        "13. Seguridad y privacidad": "Capa de anonimización; nunca expone "
            "nombres, correos u otros identificadores personales.",
    }

    for nombre, desc in modulos.items():
        st.markdown(f"**{nombre}**")
        st.caption(desc)

    st.divider()
    st.markdown("### Estructura de carpetas propuesta")
    st.code(
        """
agent/
    core/           # orquestador (LLM)
    tools/          # funciones invocables por el orquestador
    data/           # carga y perfilado de datos
    statistics/     # motor estadístico
    psychometrics/  # validación psicométrica e IRT
    validation/      # comparación con resultados anteriores
    literature/     # agente de literatura/APIs externas
    reports/        # generador de informes
    visualization/  # gráficos
    api/            # exposición del agente
    ui/             # interfaz (futuro chatbot)
tests/
docs/
data/
notebooks/
        """,
        language="text",
    )

# ---------------------------------------------------------------
# PRINCIPIOS METODOLÓGICOS
# ---------------------------------------------------------------
elif seccion == "Principios metodológicos":
    st.title("Principios metodológicos")

    st.markdown(
        """
        ### No inventar información
        El agente **nunca** crea variables, resultados, columnas o valores
        estadísticos que no existan en los datos. Si una pregunta requiere
        una variable no disponible (por ejemplo, ingresos económicos o una
        pregunta explícita de satisfacción universitaria), el agente debe:

        - informar que la variable no existe,
        - sugerir variables relacionadas que sí estén disponibles,
        - y **no** asumir que otra variable la reemplaza.

        ### Distinción entre tipos de afirmación
        """
    )

    c1, c2, c3, c4 = st.columns(4)
    c1.markdown("**Descripción**")
    c1.caption('"El grupo A tiene mayor promedio."')
    c2.markdown("**Inferencia**")
    c2.caption('"Existe evidencia estadística de una diferencia."')
    c3.markdown("**Asociación**")
    c3.caption('"Las variables están asociadas."')
    c4.markdown("**Causalidad**")
    c4.caption("No se afirma salvo que el diseño lo permita (no aplica a "
                "datos observacionales de encuesta).")

    st.markdown(
        """
        ### Reproducibilidad sobre autoridad del documento
        Los resultados de los PDFs del estudio anterior **no se copian como
        si fueran datos**: siempre que sea posible se recalculan desde el
        dataset, y se documenta explícitamente si un resultado no pudo
        reproducirse.
        """
    )

# ---------------------------------------------------------------
# ALCANCE DE ESTA ENTREGA
# ---------------------------------------------------------------
elif seccion == "Alcance de esta entrega":
    st.title("Alcance de esta entrega")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### ✅ Incluido en esta entrega")
        st.markdown(
            """
            - Contexto del estudio previo
            - Estado del arte (bienestar estudiantil + agentes de IA)
            - Problema y justificación
            - Objetivo general y objetivos específicos
            - Arquitectura propuesta del agente (13 módulos)
            - Principios metodológicos que gobernarán el agente
            """
        )
    with col2:
        st.markdown("#### ⏳ Pendiente / fuera de esta entrega")
        st.markdown(
            """
            - Carga e inspección real de los archivos del proyecto anterior
              (excel, notebooks, PDFs)
            - Documento `ANALISIS_PROYECTO_EXISTENTE.md`
            - Validación numérica de los resultados anteriores
            - Implementación del motor estadístico y primeros análisis
            - Módulo de consulta a literatura/APIs externas
            - Interfaz conversacional (chatbot)
            """
        )

    st.warning(
        "Ningún número mostrado en esta presentación proviene todavía de "
        "los datos reales del proyecto — son metas y estructura, no "
        "resultados."
    )

# ---------------------------------------------------------------
# HOJA DE RUTA
# ---------------------------------------------------------------
elif seccion == "Hoja de ruta":
    st.title("Hoja de ruta (fase 1)")

    pasos = [
        "Inspeccionar el repositorio del proyecto anterior (estructura, "
        "README, requirements, notebooks, datasets, documentos)",
        "Documentar el pipeline en docs/ANALISIS_PROYECTO_EXISTENTE.md",
        "Validar los resultados anteriores (n, alfa, T-score global, "
        "proporciones, diferencias por grupo)",
        "Crear el motor estadístico básico",
        "Crear el primer agente funcional (orquestador + herramientas)",
        "Crear pruebas automáticas",
        "Documentar la arquitectura final",
    ]
    for i, paso in enumerate(pasos, start=1):
        st.markdown(f"**Paso {i}.** {paso}")

    st.divider()
    st.markdown("### Entregas futuras")
    st.markdown(
        """
        - Aplicativo interactivo que integre todos los resultados del
          estudio.
        - Interfaz conversacional (tipo chatbot) para consultar los datos en
          lenguaje natural.
        - Informes dinámicos generados automáticamente por el agente.
        """
    )
