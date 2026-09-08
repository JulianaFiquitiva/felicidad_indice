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
        "0. Portada",
        "1. Datos e información del estudio",
        "2. Qué haremos con el agente",
        "3. Cómo funcionará el agente",
        "4. Resultados que mostrará",
        "5. Riesgos",
        "6. Diferencial y próximos pasos",
    ],
)

st.sidebar.divider()
st.sidebar.warning(
    "⚠️ Aún no se han cargado al agente los archivos originales del estudio "
    "anterior (dataset, notebooks, PDFs). Esta presentación es el marco "
    "teórico y de diseño; ningún número mostrado aquí proviene de los "
    "datos reales todavía."
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
# 1. DATOS E INFORMACIÓN DEL ESTUDIO
# =================================================================
elif seccion == "1. Datos e información del estudio":
    st.title("1. Datos e información del estudio")

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
            **Variables que se espera encontrar**
            - Género, edad, estrato socioeconómico
            - Nivel de formación, modalidad, semestre
            - Sede/seccional, programa, núcleo básico de conocimiento
            - Los 29 ítems + las 6 dimensiones + métrica global (T-score)
            - Factores de expansión (peso muestral)
            """
        )
        st.warning(
            "**No se debe asumir** que existe una variable de ingreso "
            "económico ni una pregunta explícita de satisfacción "
            "universitaria. Si no existen en el dataset, el agente debe "
            "reportarlo — nunca inventarlas ni aproximarlas con otra "
            "variable."
        )

    st.markdown("### Archivos que dejó el proyecto anterior (según lo informado)")
    st.markdown(
        """
        | Archivo | Rol esperado en el pipeline (a confirmar) |
        |---|---|
        | `data/01_dataset_preparado.xlsx` | Dataset — **no asumir que es el original** |
        | `notebooks/01_Preparacion_y_Diseno_Muestral.ipynb` | Preparación y diseño muestral |
        | `notebooks/02_Analisis_Psicometrico.ipynb` | Análisis psicométrico |
        | `notebooks/03_Estandarizacion_IRT.ipynb` | Estandarización IRT (GRM, theta, T-score) |
        | `notebooks/04_Inferencia_Poblacional.ipynb` | Inferencia poblacional y WLS |
        | `docs/Informe_Cliente_Felicidad.pdf` | Informe para la universidad |
        | `docs/Informe_Ejecutivo_Felicidad.pdf` | Informe ejecutivo |
        | `docs/Informe_Tecnico_IRT.pdf` | Informe técnico IRT |
        | `docs/Presentacion_Ejecutiva.pdf` | Presentación ejecutiva |
        """
    )
    st.error(
        "🔴 Ninguno de estos archivos ha sido cargado aún al agente. La "
        "primera tarea técnica del agente será inspeccionar el repositorio "
        "real y clasificar cada archivo (datos originales, depurados, "
        "ponderados, resultados IRT, resultados de inferencia, informes) "
        "antes de calcular nada."
    )

# =================================================================
# 2. QUÉ HAREMOS CON EL AGENTE — mirada de estadístico
# =================================================================
elif seccion == "2. Qué haremos con el agente":
    st.title("2. Qué vamos a hacer con el agente")
    st.caption("Medidas y estudios estadísticos que el agente ejecutará")

    st.markdown("### a) Validación de lo ya hecho")
    st.markdown(
        """
        - Reproducir desde el dataset los indicadores reportados: *n*,
          consistencia interna (alfa de Cronbach), T-score global,
          proporciones de bienestar por categoría.
        - Comparar cada resultado reproducido contra el valor documentado en
          los informes anteriores y clasificarlo como **validado /
          diferencia menor / diferencia importante / no reproducible**.
        - Validar el diseño muestral: consistencia de los factores de
          expansión, distribución por estrato y coherencia entre muestra y
          población.
        """
    )

    st.markdown("### b) Estadística descriptiva")
    st.markdown(
        """
        Frecuencias, porcentajes, medias, medianas, desviación estándar,
        percentiles e **intervalos de confianza** — siempre reportando el
        tamaño de muestra de cada subgrupo, porque una submuestra pequeña
        (por ejemplo, un programa con pocos encuestados) no permite las
        mismas conclusiones que la muestra completa.
        """
    )

    st.markdown("### c) Comparaciones entre grupos (bienestar por carrera, sede, género, edad, estrato…)")
    st.markdown(
        """
        El agente **no elige la prueba por popularidad**: antes de aplicar
        un método evalúa tipo de variable, normalidad, homocedasticidad y
        tamaño de muestra, y de ahí selecciona:

        - **t-test** o **Mann-Whitney** (dos grupos, según se cumpla o no
          normalidad),
        - **ANOVA** o **Kruskal-Wallis** (más de dos grupos), con
          **pruebas post-hoc** cuando la diferencia global es significativa,
        - **chi-cuadrado** para variables categóricas (p. ej. proporción de
          bienestar bajo/alto por género),
        - y siempre reporta el **tamaño de efecto**, no solo el p-valor —
          una diferencia puede ser estadísticamente significativa y
          irrelevante en la práctica, o viceversa.
        """
    )

    st.markdown("### d) Asociaciones")
    st.markdown(
        "Correlación de Pearson o Spearman (según la escala de las "
        "variables) y tablas de contingencia para relaciones entre "
        "variables categóricas."
    )

    st.markdown("### e) Modelos de regresión — ¿qué factores explican el bienestar?")
    st.markdown(
        """
        - **Regresión WLS** (ponderada), cuando el diseño muestral y los
          factores de expansión lo justifiquen — es la continuidad natural
          del enfoque que ya usó el estudio anterior.
        - **Regresión logística / ordinal** cuando la variable de interés
          sea una categoría de bienestar en vez del T-score continuo.
        - Antes de interpretar cualquier modelo: revisión de
          **colinealidad** entre predictores, evaluación de supuestos, y
          reporte de coeficientes con **intervalos de confianza, p-valores
          y R²** — nunca solo el coeficiente aislado.
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
    c4.caption("No se afirma — los datos son observacionales (encuesta), "
                "no un diseño experimental.")

# =================================================================
# 3. CÓMO FUNCIONARÁ EL AGENTE — mirada de estadístico
# =================================================================
elif seccion == "3. Cómo funcionará el agente":
    st.title("3. Cómo funcionará el agente")

    st.markdown("### ¿De qué se alimenta?")
    st.markdown(
        """
        - **Datos internos:** el dataset validado del estudio USTA (ítems,
          dimensiones, variables sociodemográficas, factores de expansión) —
          una vez inspeccionado y clasificado en la fase 1.
        - **Resultados previos documentados:** los valores reportados en los
          PDF del estudio anterior, usados únicamente como **punto de
          comparación**, nunca como fuente de datos nuevos.
        - **Literatura externa (vía API):** artículos y reportes sobre
          bienestar estudiantil (PubMed, Crossref, OCDE, UNESCO, OMS), para
          contrastar los hallazgos de la USTA con evidencia externa —
          registrando siempre título, autores, año, fuente y relación con el
          análisis.
        """
    )

    st.markdown("### ¿Con qué IA?")
    st.markdown(
        """
        Un **modelo de lenguaje (LLM) usado como orquestador**, no como
        calculadora: el LLM interpreta la pregunta del usuario, decide qué
        herramienta ejecutar y redacta la interpretación final, pero
        **el cálculo estadístico lo hace siempre código Python
        determinista y auditable** (pandas, scipy, statsmodels, y una
        librería de TRI para reproducir el GRM) — nunca un número generado
        directamente por el LLM.

        Esta separación (LLM = razonamiento y lenguaje / código = cálculo)
        es la práctica que evita el riesgo más conocido de usar IA
        generativa para estadística: que el modelo **invente cifras**
        plausibles pero incorrectas.
        """
    )

    st.markdown("### Estructura del agente (por módulos)")
    modulos = {
        "Data Profiler": "Detecta columnas, tipos, faltantes, categorías, "
            "tamaños de muestra, duplicados y variables sensibles.",
        "Data / Weight Validator": "Valida dimensiones, consistencia de "
            "categorías y factores de expansión frente al diseño muestral.",
        "Psychometric Validator": "Valida los 29 ítems, ítems invertidos, "
            "las 6 dimensiones y el alfa de Cronbach.",
        "IRT Validator": "Reproduce el GRM: discriminaciones, umbrales, "
            "theta y T-scores.",
        "Result Validator": "Compara resultados reproducidos vs. los "
            "reportados anteriormente (tabla validado / diferencia).",
        "Statistical Engine": "Selecciona y ejecuta el método estadístico "
            "apropiado según tipo de variable, supuestos y diseño muestral.",
        "Query Planner": "Traduce la pregunta del usuario en variables "
            "objetivo/agrupación, verifica su existencia y tamaño de muestra.",
        "Literature/API Agent": "Consulta fuentes académicas externas sobre "
            "bienestar estudiantil.",
        "Report Generator": "Ensambla el informe final (método, resultados, "
            "IC, interpretación, limitaciones).",
        "Trazabilidad": "Registra dataset, columnas, filtros, pesos, "
            "método, parámetros y fecha de cada respuesta.",
        "Seguridad y anonimización": "Nunca expone nombres, correos u otros "
            "identificadores personales.",
    }
    for nombre, desc in modulos.items():
        st.markdown(f"**{nombre}**")
        st.caption(desc)

    st.markdown("### Flujo de una consulta")
    st.markdown(
        """
        `Usuario pregunta → Query Planner identifica variables → Statistical
        Engine elige y ejecuta el método → Result/IRT Validator revisa
        consistencia → Report Generator redacta la respuesta con tabla,
        gráfico, método usado y advertencias → se registra la trazabilidad`
        """
    )

# =================================================================
# 4. RESULTADOS QUE MOSTRARÁ
# =================================================================
elif seccion == "4. Resultados que mostrará":
    st.title("4. Resultados que mostrará el agente")
    st.caption("El resultado final siempre es un informe con el análisis del agente de IA")

    st.markdown(
        """
        Cada respuesta del agente se entrega como un **informe**, no como
        una cifra suelta. Estructura estándar de cada informe:
        """
    )
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
    st.caption(
        "La columna 'Valor anterior' son las cifras que reportan los "
        "documentos del estudio previo; las columnas 'reproducido / "
        "diferencia / estado' solo se llenan cuando el agente calcule "
        "sobre el dataset real."
    )

# =================================================================
# 5. RIESGOS
# =================================================================
elif seccion == "5. Riesgos":
    st.title("5. Riesgos")

    st.markdown("#### Riesgos de datos y reproducibilidad")
    st.markdown(
        """
        - Que los archivos entregados **no permitan reproducir** el pipeline
          original (código incompleto, dataset sin las variables que
          generaron el theta/T-score, falta de metadatos).
        - Confundir un archivo depurado o ponderado con el dataset original
          y sacar conclusiones sobre una base equivocada.
        - Subgrupos con **muestra muy pequeña** (ciertos programas o sedes)
          que produzcan intervalos de confianza demasiado amplios para ser
          útiles.
        """
    )

    st.markdown("#### Riesgos estadísticos")
    st.markdown(
        """
        - **Comparaciones múltiples**: al analizar muchos grupos (carrera,
          sede, estrato, edad, género…) aumenta la probabilidad de encontrar
          "diferencias significativas" por azar si no se corrige el umbral
          de significancia.
        - **Interpretar asociación como causalidad** — los datos son de
          encuesta (observacionales), no de un experimento.
        - Aplicar una prueba estadística sin verificar sus supuestos
          (normalidad, homocedasticidad, independencia).
        """
    )

    st.markdown("#### Riesgos propios de usar un LLM")
    st.markdown(
        """
        - **Alucinación de cifras** si se le pide al LLM calcular
          directamente en vez de delegar en código — se mitiga con la
          arquitectura orquestador + motor estadístico separado.
        - Que el LLM **redondee o simplifique de más** al "traducir" un
          resultado técnico y pierda matices importantes (por ejemplo,
          diluir un intervalo de confianza amplio).
        - Dependencia de una **API externa** de literatura/IA: costos,
          disponibilidad y límites de uso.
        """
    )

    st.markdown("#### Riesgos éticos y de privacidad")
    st.markdown(
        """
        - Los datos de la encuesta pueden contener información
          potencialmente identificable a nivel de programa/sede con muestras
          pequeñas, aunque no haya nombres — riesgo de identificación
          indirecta.
        - Uso indebido de los resultados para decisiones institucionales
          sin comunicar las limitaciones del estudio (tamaño de muestra,
          representatividad, fecha de recolección).
        """
    )

    st.markdown("#### Riesgo de alcance del proyecto")
    st.markdown(
        "Construir funcionalidades avanzadas (chatbot, modelos de regresión "
        "complejos) **antes** de validar el pipeline base — por eso la fase "
        "1 se limita deliberadamente a inspección, documentación y "
        "validación."
    )

# =================================================================
# 6. DIFERENCIAL Y PRÓXIMOS PASOS
# =================================================================
elif seccion == "6. Diferencial y próximos pasos":
    st.title("6. Diferencial y próximos pasos")

    st.markdown("### ¿En qué se diferencia este agente de un chatbot común?")
    st.markdown(
        """
        Un chatbot corriente responde con lo que el LLM "cree" que es
        cierto, sin ejecutar cálculo real. Este agente separa
        explícitamente **razonamiento (LLM)** de **cálculo (código
        Python reproducible)**, y agrega una capa que la mayoría de
        chatbots de datos no tiene: **validación contra resultados
        previos** y **trazabilidad completa** de cada respuesta (qué
        dataset, qué filtros, qué método, qué parámetros).
        """
    )

    st.markdown("### Próximos pasos inmediatos (fase 1)")
    pasos = [
        "Cargar e inspeccionar los archivos reales del proyecto anterior",
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
        - Aplicativo interactivo que integre todos los resultados del
          estudio.
        - Interfaz conversacional (chatbot) para consultar los datos en
          lenguaje natural.
        - Generación automática de informes dinámicos.
        """
    )
