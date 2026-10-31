import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="Cluster B: Neurobiología & Impacto Sistémico",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo profesional de baja luminosidad para ateneo médico
st.markdown("""
    <style>
    .main { background-color: #0b0f19; }
    h1, h2, h3, h4 { color: #f8fafc; font-family: 'Inter', sans-serif; }
    .stMetric { background-color: #1e293b; padding: 12px; border-radius: 8px; border: 1px solid #334155; }
    </style>
""", unsafe_allow_html=True)

# Parámetros psicopatológicos base por cuadro
CLINICAL_PROFILES = {
    "Trastorno Límite de la Personalidad (TLP)": {
        "amigdala_base": 0.90,
        "vmpfc_base": 0.25,
        "acc_base": 0.40,
        "insula_base": 0.85,
        "vincular_tension": 0.95,
        "legal_laboral_tension": 0.65,
        "salud_tension": 0.90,
        "autoimagen_tension": 0.95,
        "color_predominante": "#ef4444",
        "circuito_desc": "Hiperreactividad amigdalina aguda + falla severa del reclutamiento inhibitorio vmPFC/OFC frente al dolor social. Falla en mentalización y polarización afectiva (splitting).",
        "impacto_desc": "Alta demanda asistencial por urgencias (conductas parasuicidas, crisis de angustia), disolución caótica de lazos interpersonales por temor al abandono y labilidad de autoimagen."
    },
    "Trastorno Antisocial de la Personalidad (TASP)": {
        "amigdala_base": 0.20,
        "vmpfc_base": 0.30,
        "acc_base": 0.35,
        "insula_base": 0.25,
        "vincular_tension": 0.70,
        "legal_laboral_tension": 0.98,
        "salud_tension": 0.50,
        "autoimagen_tension": 0.30,
        "color_predominante": "#f59e0b",
        "circuito_desc": "Hipoactividad amigdalina e insular ante estímulos aversivos. Ausencia de condicionamiento al miedo/castigo con desconexión orbitofrontal en la evaluación moral de daños a terceros.",
        "impacto_desc": "Impacto colateral masivo en el ámbito legal, judicial y familiar por conductas transgresoras, manipulación utilitaria y ausencia de empatía vicaria."
    },
    "Trastorno Narcisista de la Personalidad (TNP)": {
        "amigdala_base": 0.60,
        "vmpfc_base": 0.50,
        "acc_base": 0.75,
        "insula_base": 0.40,
        "vincular_tension": 0.85,
        "legal_laboral_tension": 0.70,
        "salud_tension": 0.40,
        "autoimagen_tension": 0.90,
        "color_predominante": "#a855f7",
        "circuito_desc": "Respuesta amigdalina fluctuante y vulnerable ante la 'herida narcisista'. Disociación entre empatía cognitiva preservada y empatía afectiva deficitaria.",
        "impacto_desc": "Relaciones instrumentales con alternancia entre devaluación e idealización; descompensación depresiva o furia destructiva ante la pérdida de validación externa."
    },
    "Trastorno Histriónico de la Personalidad (THP)": {
        "amigdala_base": 0.75,
        "vmpfc_base": 0.45,
        "acc_base": 0.55,
        "insula_base": 0.70,
        "vincular_tension": 0.75,
        "legal_laboral_tension": 0.45,
        "salud_tension": 0.60,
        "autoimagen_tension": 0.80,
        "color_predominante": "#06b6d4",
        "circuito_desc": "Hipersensibilidad de los circuitos de recompensa y reactividad límbica ante señales sociales. Búsqueda de estimulación con procesamiento cognitivo superficial.",
        "impacto_desc": "Somatizaciones recurrentes, teatralidad con desgaste del entorno social inmediato y dependencia patológica de la mirada ajena."
    }
}

# --- Sidebar ---
st.sidebar.title("🎛️ Configuración Clínica")
selected_disorder = st.sidebar.selectbox("Entidad Patológica:", list(CLINICAL_PROFILES.keys()))
stress_level = st.sidebar.slider("Nivel de Disparador / Estrés Ambiental:", min_value=0.0, max_value=1.0, value=0.5, step=0.05)
view_mode = st.sidebar.radio("Nivel de Representación 3D:", ["Circuitos Neurobiológicos", "Ecosistema Sistémico e Impacto"])

profile = CLINICAL_PROFILES[selected_disorder]

# Modelado matemático dinámico de activación
amigdala_act = np.clip(profile["amigdala_base"] * (1.0 + 0.5 * stress_level), 0.05, 1.5)
vmpfc_act = np.clip(profile["vmpfc_base"] * (1.0 - 0.4 * stress_level), 0.05, 1.0)
acc_act = np.clip(profile["acc_base"] * (1.0 + 0.3 * stress_level), 0.05, 1.2)
insula_act = np.clip(profile["insula_base"] * (1.0 + 0.4 * stress_level), 0.05, 1.3)

ratio_control = vmpfc_act / amigdala_act

# --- Header ---
st.title(f"Visualización Tridimensional: {selected_disorder}")
st.caption("Ateneo Clínico-Académico | Modelo Integrativo de Redes Neurobiológicas y Consecuencias Sistémicas")

# Métricas directas
c1, c2, c3, c4 = st.columns(4)
c1.metric("Reactividad Amígdala (Bottom-Up)", f"{amigdala_act:.2f}", delta=f"{(amigdala_act - profile['amigdala_base']):.2f}")
c2.metric("Freno vmPFC / OFC (Top-Down)", f"{vmpfc_act:.2f}", delta=f"{(vmpfc_act - profile['vmpfc_base']):.2f}")
c3.metric("Ratio Control Inhibitorio", f"{ratio_control:.2f}", delta="Déficit Crítico" if ratio_control < 0.5 else "Compensado", delta_color="inverse")
c4.metric("Desestructuración del Entorno", f"{stress_level * 100:.0f}%", delta="Riesgo de Ruptura" if stress_level > 0.6 else "Estable")

# --- Generación Gráfica 3D ---
if view_mode == "Circuitos Neurobiológicos":
    # 1. Nube anatómica cerebral translúcida
    np.random.seed(42)
    n_points = 1800
    u = np.random.uniform(0, 1, n_points)
    v = np.random.uniform(0, 1, n_points)
    theta = u * 2.0 * np.pi
    phi = np.arccos(2.0 * v - 1.0)
    r = np.cbrt(np.random.uniform(0.7, 1.0, n_points)) * 9.0

    bx = r * np.sin(phi) * np.cos(theta) * 1.15
    by = r * np.sin(phi) * np.sin(theta) * 0.90
    bz = r * np.cos(phi) * 1.35
    bx = np.where(bx > 0, bx + 0.4, bx - 0.4)

    fig = go.Figure()

    # Puntos corticales
    fig.add_trace(go.Scatter3d(
        x=bx, y=by, z=bz,
        mode='markers',
        marker=dict(size=1.6, color='#38bdf8', opacity=0.18),
        name="Manto Cortical",
        hoverinfo='none'
    ))

    # Nodos anatómicos diana
    nodes = [
        {"name": "Amígdala (Der/Izq)", "x": [2.2, -2.2], "y": [-1.0, -1.0], "z": [0.5, 0.5], "act": amigdala_act, "color": "#ef4444"},
        {"name": "vmPFC / OFC", "x": [0.0], "y": [6.5], "z": [-1.5], "act": vmpfc_act, "color": "#22c55e"},
        {"name": "ACC (Cíngulo Anterior)", "x": [0.0], "y": [3.0], "z": [3.5], "act": acc_act, "color": "#f59e0b"},
        {"name": "Ínsula Anterior", "x": [4.0, -4.0], "y": [1.5, 1.5], "z": [0.0, 0.0], "act": insula_act, "color": "#a855f7"}
    ]

    for n in nodes:
        fig.add_trace(go.Scatter3d(
            x=n["x"], y=n["y"], z=n["z"],
            mode='markers+text',
            text=[n["name"]] * len(n["x"]),
            textposition="top center",
            textfont=dict(size=11, color='#ffffff'),
            marker=dict(
                size=n["act"] * 24,
                color=n["color"],
                opacity=0.9,
                line=dict(width=2, color='#ffffff')
            ),
            name=n["name"]
        ))

    # Tractos frontolímbicos (Líneas de conexión funcional)
    # De vmPFC a Amígdala
    for ax in [2.2, -2.2]:
        fig.add_trace(go.Scatter3d(
            x=[0.0, ax], y=[6.5, -1.0], z=[-1.5, 0.5],
            mode='lines',
            line=dict(color='#ef4444' if ratio_control < 0.5 else '#38bdf8', width=max(1.0, ratio_control * 6)),
            hoverinfo='none',
            showlegend=False
        ))

    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            bgcolor='#05070f'
        ),
        paper_bgcolor='#05070f',
        margin=dict(l=0, r=0, b=0, t=20),
        legend=dict(font=dict(color='#ffffff')),
        height=580
    )

    st.plotly_chart(fig, use_container_width=True)
    st.info(f"**Mecanismo Conectómico:** {profile['circuito_desc']}")

else:
    # 2. Modo Ecosistema Sistémico / Vidas Afectadas
    t_vincular = np.clip(profile["vincular_tension"] * (1 + 0.3 * stress_level), 0.1, 1.5)
    t_legal = np.clip(profile["legal_laboral_tension"] * (1 + 0.3 * stress_level), 0.1, 1.5)
    t_salud = np.clip(profile["salud_tension"] * (1 + 0.3 * stress_level), 0.1, 1.5)
    t_autoimagen = np.clip(profile["autoimagen_tension"] * (1 + 0.3 * stress_level), 0.1, 1.5)

    systems = [
        {"name": "Vínculos de Apego & Pareja", "x": 6, "y": 4, "z": 2, "tension": t_vincular, "desc": "Conflictos explosivos, escisión, miedo al abandono"},
        {"name": "Ámbito Legal, Social & Laboral", "x": -6, "y": -4, "z": 2, "tension": t_legal, "desc": "Transgresión de normas, cesantías laborales, litigios"},
        {"name": "Sistema Sanitario & Guardia", "x": -4, "y": 6, "z": -3, "tension": t_salud, "desc": "Ingresos por crisis, parasuicidio, abuso de sustancias"},
        {"name": "Autoimagen & Cohesión del Self", "x": 5, "y": -5, "z": -2, "tension": t_autoimagen, "desc": "Sensación de vacío, grandiosidad vulnerable, fragmentación"}
    ]

    fig_sys = go.Figure()

    # Paciente central
    fig_sys.add_trace(go.Scatter3d(
        x=[0], y=[0], z=[0],
        mode='markers+text',
        text=["ESTRUCTURA DEL PACIENTE"],
        textposition="top center",
        textfont=dict(size=14, color='#ffffff'),
        marker=dict(size=28, color=profile["color_predominante"], line=dict(color='#ffffff', width=3)),
        name="Individuo"
    ))

    # Nodos del entorno
    for s in systems:
        line_color = "#ef4444" if s["tension"] > 0.8 else "#38bdf8"
        fig_sys.add_trace(go.Scatter3d(
            x=[s["x"]], y=[s["y"]], z=[s["z"]],
            mode='markers+text',
            text=[f"{s['name']}<br>Tensión: {s['tension']:.2f}"],
            textposition="bottom center",
            textfont=dict(size=11, color='#cbd5e1'),
            marker=dict(size=16 * s["tension"], color=line_color, opacity=0.9),
            name=s["name"]
        ))

        # Vector de colapso/tensión relacional
        fig_sys.add_trace(go.Scatter3d(
            x=[0, s["x"]], y=[0, s["y"]], z=[0, s["z"]],
            mode='lines',
            line=dict(color=line_color, width=s["tension"] * 8, dash="solid" if s["tension"] < 1.0 else "dash"),
            showlegend=False
        ))

    fig_sys.update_layout(
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            bgcolor='#05070f'
        ),
        paper_bgcolor='#05070f',
        margin=dict(l=0, r=0, b=0, t=20),
        legend=dict(font=dict(color='#ffffff')),
        height=580
    )

    st.plotly_chart(fig_sys, use_container_width=True)
    st.warning(f"**Impacto Psicosocial y Relacional:** {profile['impacto_desc']}")

# --- Marco de Discusión Académica ---
st.markdown("---")
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Fundamentos Neurobiológicos")
    st.markdown("""
    * **Amígdala / Complejo Límbico:** Generador de la valencia afectiva primaria. En TLP exhibe hiperreactividad desproporcionada; en TASP se observa hiporreactividad selectiva al castigo.
    * **vmPFC & OFC:** Encargados de la codificación del valor subjetivo y el freno inhibitorio. Su desconexión impide la modulación del afecto por la experiencia o la norma.
    * **Corteza Cingulada Anterior (ACC):** Nodo central de detección de conflicto y dolor social (morfología alterada en exclusión interpersonal).
    """)

with col_b:
    st.subheader("Lectura Sistémica (Cluster B)")
    st.markdown("""
    * **Vínculos de apego:** La desregulación afectiva individual induce dinámicas reactivas en el entorno cercano (invalidación, respuestas defensivas, co-dependencia).
    * **Efecto onda expansiva:** Las patologías del Cluster B rara vez permanecen confinadas al sufrimiento subjetivo intrapsíquico; comprometen recursos de salud pública, redes judiciales y estructuras familiares completas.
    """)
