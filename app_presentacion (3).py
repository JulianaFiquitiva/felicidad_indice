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
.pending-card {
    background:#1c1410; border:1px solid #a16207; border-left:5px solid #eab308;
    border-radius:10px; padding:12px 16px; margin:10px 0; color:#fde68a; font-size:13.5px;
}
.q-card {
    background:#111827; border:1px solid #334155; border-left:5px solid #6366f1;
    border-radius:10px; padding:12px 16px; margin:8px 0; color:#e2e8f0; font-size:13.5px;
}
.q-label { color:#a5b4fc; font-weight:700; font-size:12px; text-transform:uppercase; letter-spacing:.03em; }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


def flow_diagram(steps):
    html = '<div class="flow-wrap">'
    for i, (title, sub) in enumerate(steps):
        html += f'<div class="flow-box">{title}'
        if sub:
            html += f'<br><small>{sub}</small>'
        html += "</div>"
        if i < len(steps) - 1:
            html += '<div class="flow-arrow">➜</div>'
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


def pending(text):
    st.markdown(f'<div class="pending-card">⏳ <strong>Pendiente — no se puede responder sin abrir el dato real:</strong> {text}</div>', unsafe_allow_html=True)


def qcard(label, question, answer):
    st.markdown(
        f'<div class="q-card"><div class="q-label">{label}</div>{question}<br><br>{answer}</div>',
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------------
st.sidebar.title("📊 Agente IA — Bienestar Estudiantil")
st.sidebar.caption("USTA · Consultoría e Investigación · Prof. Javier Mauricio Sierra")

seccion = st.sidebar.radio(
    "Navegación",
    [
        "0. Portada",
        "1. Problema y contexto actual",
        "2. Objetivos",
        "3. Estado del arte",
        "4. Resumen corto de los datos",
    ],
)

# =================================================================
# 0. PORTADA
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
        inteligencia artificial** que valida y permite consultar esos
        resultados de forma reproducible.

        **Para quién es esto:** exclusivamente para **apoyar la toma de
        decisiones de la universidad y sus dependencias** (Bienestar
        Universitario, direcciones de programa, seccionales) — no es una
        herramienta para el equipo que hizo el estudio anterior, aunque su
        trabajo es la base de datos y de pipeline sobre la que se construye.
        """
    )
    st.info("Entrega — Materia de Consultoría e Investigación.")

# =================================================================
# 1. PROBLEMA Y CONTEXTO ACTUAL
# =================================================================
elif seccion == "1. Problema y contexto actual":
    st.title("1. Problema y contexto actual")

    qcard(
        "¿Quién sufre este problema y desde cuándo?",
        "",
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
        "",
        "Cualquier pregunta nueva sobre el bienestar estudiantil (por "
        "ejemplo, \"¿cómo está Villavicencio pregrado comparado con "
        "Bogotá?\") solo puede responderse si alguien vuelve a abrir los "
        "notebooks originales y repite el análisis manualmente. No existe "
        "hoy una vía institucional para consultarlo sin depender de quien "
        "construyó el pipeline original.",
    )

    qcard(
        "¿Qué pasa si nadie hace nada?",
        "",
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

# =================================================================
# 2. OBJETIVOS
# =================================================================
elif seccion == "2. Objetivos":
    st.title("2. Objetivos")

    st.markdown("### Objetivo general")
    st.success(
        "Desarrollar un agente de inteligencia artificial que permita a la "
        "universidad y sus dependencias **validar y consultar** el Índice "
        "de Bienestar Estudiantil de forma reproducible y trazable, como "
        "insumo para la toma de decisiones institucionales."
    )

    st.markdown("### Objetivos específicos")
    st.caption(
        "Cada uno debe dejar una evidencia verificable — si los tres se "
        "cumplen, el objetivo general queda resuelto: se puede confiar en "
        "el dato (1), se puede interrogarlo (2), y la universidad puede "
        "usarlo para decidir (3)."
    )

    with st.expander("1. Validar la reproducibilidad de los resultados ya reportados"):
        st.markdown(
            """
            Reproducir desde el dataset los indicadores clave (n, alfa de
            Cronbach, T-score global, proporciones por categoría) y
            compararlos contra lo documentado en los informes anteriores.

            **Evidencia de cumplimiento:** una tabla de validación
            (Resultado | valor anterior | valor reproducido | diferencia |
            estado) con cada indicador clasificado.
            """
        )

    with st.expander("2. Habilitar consultas estadísticas segmentadas y confiables"):
        st.markdown(
            """
            Construir un motor que responda preguntas por sede, programa,
            género, edad y estrato, seleccionando el método estadístico
            correcto según los supuestos de cada caso.

            **Evidencia de cumplimiento:** un conjunto de consultas de
            prueba respondidas correctamente, con el método usado
            documentado en cada una.
            """
        )

    with st.expander("3. Entregar los resultados en un formato usable para decisiones institucionales"):
        st.markdown(
            """
            Generar informes en lenguaje comprensible para no
            estadísticos, con intervalos de confianza y limitaciones
            explícitas, dirigidos a las dependencias de la universidad.

            **Evidencia de cumplimiento:** al menos un informe ejecutivo
            real, generado a partir de datos reales, entregado a una
            dependencia de la universidad para su revisión.
            """
        )

    st.markdown("### Qué NO es un objetivo (son actividades, no fines)")
    st.markdown(
        """
        Inspeccionar el repositorio, documentar el pipeline en un archivo
        `.md`, o instalar librerías son **pasos necesarios**, no objetivos
        en sí mismos — sirven al objetivo específico 1 (validar), pero por
        sí solos no producen ningún valor para la universidad si se quedan
        ahí.
        """
    )

# =================================================================
# 3. ESTADO DEL ARTE
# =================================================================
elif seccion == "3. Estado del arte":
    st.title("3. Estado del arte")

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
        de esas fuentes construye una herramienta de IA para **auditar y
        volver consultable** un estudio de bienestar ya hecho. El aporte
        de este proyecto no es un instrumento de medición nuevo, sino la
        capa de validación y consulta reproducible que falta después de
        que la medición ya se hizo.
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

# =================================================================
# 4. RESUMEN CORTO DE LOS DATOS
# =================================================================
elif seccion == "4. Resumen corto de los datos":
    st.title("4. Resumen corto de los datos")

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
        "El objetivo específico 1 (validar reproducibilidad) depende de la "
        "variable de **T-score global** (o el theta del que se deriva), "
        "presente en `Indice_Felicidad_Estandarizado_IRT` — es la cifra "
        "puntual que hay que reproducir y comparar contra el valor "
        "reportado (≈ 50.7 según el informe anterior)."
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
        disponibles (por ejemplo, se puede validar consistencia interna y
        estadística descriptiva aunque falte el archivo de parámetros GRM,
        pero no se podría reproducir el T-score). El alcance se recorta de
        forma explícita, nunca se rellena el vacío con un valor inventado.
        """
    )
