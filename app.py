import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="Neurobiología & Conectómica del Cluster B",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estética de consola médica de neuroimagen
st.markdown("""
    <style>
    .main { background-color: #030712; }
    h1, h2, h3, h4 { color: #f9fafb; font-family: 'Inter', -apple-system, sans-serif; font-weight: 600; }
    .stMetric { background-color: #111827; border: 1px solid #1f2937; border-radius: 8px; padding: 12px; }
    .report-box { background-color: #0f172a; border-left: 4px solid #38bdf8; padding: 16px; border-radius: 4px; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# Base de Datos Neurobiológica y Conectómica (Evidencia DTI/fMRI)
# -------------------------------------------------------------
NEURO_DATA = {
    "Trastorno Límite de la Personalidad (TLP)": {
        "color_theme": "#ef4444",
        "uncinate_integrity": 0.22,      # Fuerte alteración del fascículo uncinado
        "cingulum_integrity": 0.45,      # Cíngulo con hiperconectividad al dolor social
        "frontostriatal_integrity": 0.35,# Falla en modulación de impulsos
        "regions": {
            "Amígdala Bilateral": {"coords": [(2.2, -0.8, -1.2), (-2.2, -0.8, -1.2)], "activity": 1.45, "role": "Hiperreactividad basal e hipersensibilidad a caras neutras/amenazantes", "status": "HIPERTRÓFICA / HIPERACTIVA"},
            "vmPFC": {"coords": [(0.0, 4.2, -1.2)], "activity": 0.25, "role": "Falla del control inhibitorio top-down sobre la carga afectiva", "status": "HIPOCONECTADA"},
            "OFC (Corteza Orbitofrontal)": {"coords": [(1.6, 3.8, -2.0), (-1.6, 3.8, -2.0)], "activity": 0.30, "role": "Incapacidad de computar la extinción del castigo y el valor flexible del estímulo", "status": "HIPOFUNCIÓN"},
            "dACC (Cíngulo Anterior Dorsal)": {"coords": [(0.0, 2.2, 2.8)], "activity": 1.30, "role": "Hipersensibilidad de la red del dolor social ante la exclusión o desapego", "status": "HIPERREACTIVA"},
            "Ínsula Anterior": {"coords": [(3.6, 0.8, 0.0), (-3.6, 0.8, 0.0)], "activity": 1.25, "role": "Interocepción visceral amplificada del malestar psíquico", "status": "SOBREACTIVADA"},
            "Núcleo Accumbens": {"coords": [(1.2, 1.2, -0.8), (-1.2, 1.2, -0.8)], "activity": 0.90, "role": "Disregulación hedónica e impulsividad hedónica/purgativa", "status": "INCONSISTENTE"}
        },
        "dti_findings": "Microestructura de sustancia blanca con anisotropía fraccional (FA) marcadamente reducida en el fascículo uncinado bilateral y la radiación tálamo-frontal. Falla del bucle prefronto-amigdalino.",
        "relational_impact": {
            "Pareja / Apego": {"t": 0.98, "desc": "Idealización vs devaluación masiva, miedo pánico al abandono, terror vincular"},
            "Servicio de Urgencias": {"t": 0.92, "desc": "Ingresos recurrentes por gestos parasuicidas, intoxicaciones agudas e impulsividad"},
            "Autoimagen / Identidad": {"t": 0.95, "desc": "Sensación crónica de vacío interior, dispersión identitaria, metamorfosis relacional"},
            "Ámbito Familiar": {"t": 0.88, "desc": "Desgaste catastrófico del entorno, triangulación y claudicación del soporte"},
            "Ámbito Laboral/Legal": {"t": 0.65, "desc": "Inestabilidad por descompensaciones afectivas súbitas"}
        }
    },
    "Trastorno Antisocial de la Personalidad (TASP / Psicopatía)": {
        "color_theme": "#f59e0b",
        "uncinate_integrity": 0.10,      # Desconexión estructural severa
        "cingulum_integrity": 0.30,
        "frontostriatal_integrity": 0.85, # Conexión estriatal preservada orientada a ganancia inmediata
        "regions": {
            "Amígdala Bilateral": {"coords": [(2.2, -0.8, -1.2), (-2.2, -0.8, -1.2)], "activity": 0.18, "role": "Hipoactividad severa ante el miedo condicionado y señales de llanto/angustia ajena", "status": "HIPORREACTIVA / ATROFIA FUNCIONAL"},
            "vmPFC": {"coords": [(0.0, 4.2, -1.2)], "activity": 0.20, "role": "Incapacidad para integrar juicio moral afectivo y empatía somática", "status": "HIPOCONECTADA"},
            "OFC (Corteza Orbitofrontal)": {"coords": [(1.6, 3.8, -2.0), (-1.6, 3.8, -2.0)], "activity": 0.25, "role": "Indiferencia a las contingencias punitivas y aversivas futuras", "status": "HIPOFUNCIÓN CRÍTICA"},
            "dACC (Cíngulo Anterior Dorsal)": {"coords": [(0.0, 2.2, 2.8)], "activity": 0.25, "role": "Monitoreo de error cognitivo sin carga afectiva vicaria", "status": "ATENUADO"},
            "Ínsula Anterior": {"coords": [(3.6, 0.8, 0.0), (-3.6, 0.8, 0.0)], "activity": 0.20, "role": "Ausencia de marcadores somáticos de aversión o culpa", "status": "HIPOACTIVA"},
            "Núcleo Accumbens": {"coords": [(1.2, 1.2, -0.8), (-1.2, 1.2, -0.8)], "activity": 1.40, "role": "Hiperreactividad de recompensa orientada a incentivos inmediatos e instrumentales", "status": "HIPEREXCITABLE"}
        },
        "dti_findings": "Reducción bilateral crítica en la integridad estructural del fascículo uncinado. Desconexión anatómica estricta entre la amígdala anterior y la corteza prefrontal ventromedial.",
        "relational_impact": {
            "Ámbito Legal / Penal": {"t": 0.99, "desc": "Conductas delictivas, transgresión sistemática de leyes, reincidencia penitenciaria"},
            "Vínculos / Pareja": {"t": 0.90, "desc": "Parasitismo, manipulación utilitaria, cosificación del otro, violencia instrumental"},
            "Ámbito Laboral": {"t": 0.82, "desc": "Estafas, despidos por deshonestidad, ausencia de lealtad contractual"},
            "Servicio de Urgencias": {"t": 0.55, "desc": "Traumatismos por riñas, sobredosis recreativas o simulación judicial"},
            "Autoimagen / Identidad": {"t": 0.25, "desc": "Egosintonía completa; ausencia de malestar intrapsíquico primario"}
        }
    },
    "Trastorno Narcisista de la Personalidad (TNP)": {
        "color_theme": "#a855f7",
        "uncinate_integrity": 0.50,
        "cingulum_integrity": 0.65,
        "frontostriatal_integrity": 0.70,
        "regions": {
            "Amígdala Bilateral": {"coords": [(2.2, -0.8, -1.2), (-2.2, -0.8, -1.2)], "activity": 0.85, "role": "Reactividad fásica aguda ante la humillación o pérdida de estatus ('herida narcisista')", "status": "VULNERABILIDAD FÁSICA"},
            "vmPFC": {"coords": [(0.0, 4.2, -1.2)], "activity": 0.45, "role": "Oscilación entre autosuficiencia defensiva y desmoronamiento autovalorativo", "status": "REGULACIÓN INESTABLE"},
            "OFC (Corteza Orbitofrontal)": {"coords": [(1.6, 3.8, -2.0), (-1.6, 3.8, -2.0)], "activity": 0.60, "role": "Procesamiento de jerarquías sociales y valor de dominancia", "status": "MODULADO POR ESTATUS"},
            "dACC (Cíngulo Anterior Dorsal)": {"coords": [(0.0, 2.2, 2.8)], "activity": 1.35, "role": "Alarma desproporcionada ante la devaluación o falta de admiración externa", "status": "HIPERREACTIVO AL DESPRECIO"},
            "Ínsula Anterior": {"coords": [(3.6, 0.8, 0.0), (-3.6, 0.8, 0.0)], "activity": 0.40, "role": "Empatía afectiva reducida con preservación de la empatía cognitiva (teoría de la mente instrumental)", "status": "DISOCIACIÓN COGNITIVO-AFECTIVA"},
            "Núcleo Accumbens": {"coords": [(1.2, 1.2, -0.8), (-1.2, 1.2, -0.8)], "activity": 1.15, "role": "Dependencia del feedback de admiración externa para sostener el tono hedónico", "status": "DEMANDANTE DE REFUERZO"}
        },
        "dti_findings": "Alteraciones en la sustancia blanca prefrontal medial y anomalías en la red por defecto (DMN) y red de prominencia, asociadas a la discrepancia entre el self grandioso y el self vulnerable.",
        "relational_impact": {
            "Pareja / Apego": {"t": 0.86, "desc": "Alternancia entre cosificación narcisista y desprecio punitivo ante críticas"},
            "Ámbito Laboral": {"t": 0.78, "desc": "Rivalidad hostil con pares, explotación de subordinados, sabotaje corporativo"},
            "Autoimagen / Identidad": {"t": 0.94, "desc": "Equilibrio precario: grandiosidad manifiesta sostenida sobre un vacío basal aterrador"},
            "Ámbito Familiar": {"t": 0.75, "desc": "Exigencia de subordinación al proyecto personal o rechazo tajante"},
            "Servicio de Urgencias": {"t": 0.45, "desc": "Consultas por crisis depresivas colapsadas ante bancarrota o pérdida irrevocable de estatus"}
        }
    },
    "Trastorno Histriónico de la Personalidad (THP)": {
        "color_theme": "#06b6d4",
        "uncinate_integrity": 0.60,
        "cingulum_integrity": 0.55,
        "frontostriatal_integrity": 0.80,
        "regions": {
            "Amígdala Bilateral": {"coords": [(2.2, -0.8, -1.2), (-2.2, -0.8, -1.2)], "activity": 1.10, "role": "Respuesta emocional amplificada, lábil y de rápida habituación", "status": "HIPEREXCITABLE SUPERFICIAL"},
            "vmPFC": {"coords": [(0.0, 4.2, -1.2)], "activity": 0.40, "role": "Déficit en el procesamiento analítico reflexivo; cognición global e impresionista", "status": "PROCESAMIENTO GLOBAL/LAXO"},
            "OFC (Corteza Orbitofrontal)": {"coords": [(1.6, 3.8, -2.0), (-1.6, 3.8, -2.0)], "activity": 0.50, "role": "Búsqueda acelerada de señales de aprobación interpersonal", "status": "ORIENTACIÓN INTERPERSONAL"},
            "dACC (Cíngulo Anterior Dorsal)": {"coords": [(0.0, 2.2, 2.8)], "activity": 0.85, "role": "Alarma ante la neutralidad del entorno (vivenciada como rechazo catastrófico)", "status": "INTOLERANCIA AL DESINTERÉS"},
            "Ínsula Anterior": {"coords": [(3.6, 0.8, 0.0), (-3.6, 0.8, 0.0)], "activity": 1.15, "role": "Conversión somatomorfa de conflictos afectivos y teatralidad expresiva", "status": "SOMATIZACIÓN INTEROCEPTIVA"},
            "Núcleo Accumbens": {"coords": [(1.2, 1.2, -0.8), (-1.2, 1.2, -0.8)], "activity": 1.20, "role": "Refuerzo continuo por atención social y validación externa", "status": "HIPERRESPUESTA AL FEEDBACK"}
        },
        "dti_findings": "Varianza conectómica difusa con reducción de sincronización fronto-temporal dorsolateral, facilitando el estilo de procesamiento cognitivo superficial y disociativo.",
        "relational_impact": {
            "Pareja / Apego": {"t": 0.85, "desc": "Seducción descontextualizada, dramatización afectiva y agotamiento del partner"},
            "Ámbito Social/Amigos": {"t": 0.70, "desc": "Relaciones superficiales asumidas como íntimas; celos y teatralidad"},
            "Servicio de Urgencias": {"t": 0.72, "desc": "Consultas frecuentes por crisis disociativas, pseudoconvulsiones o somatizaciones agudas"},
            "Autoimagen / Identidad": {"t": 0.80, "desc": "Autoestima dependiente por completo de la atención y atracción provocada"},
            "Ámbito Laboral": {"t": 0.50, "desc": "Dificultades en tareas sistemáticas; intolerancia a la falta de protagonismo"}
        }
    }
}

# --- Panel Lateral de Control ---
st.sidebar.markdown("## ⚙️ Parámetros Clínicos")
disorder = st.sidebar.selectbox("Trastorno del Cluster B:", list(NEURO_DATA.keys()))
stress = st.sidebar.slider("Nivel de Disparador / Crisis Ambiental:", min_value=0.0, max_value=1.0, value=0.5, step=0.05)
view_selection = st.sidebar.radio("Modo de Render 3D:", ["1. Conectoma & Circuitos Anatómicos 3D", "2. Ecosistema Relacional & Onda Expansiva"])

data = NEURO_DATA[disorder]

# -------------------------------------------------------------
# Generadores de Geometría Neuroanatómica Realista
# -------------------------------------------------------------
def build_cortex_surface():
    """Genera una superficie paramétrica cortical continua con surcos y cisura interhemisférica."""
    u = np.linspace(0, 2 * np.pi, 90)
    v = np.linspace(0, np.pi, 60)
    U, V = np.meshgrid(u, v)
    
    # Radios basales anatómicos del cerebro (longitudinal, lateral, vertical)
    rx, ry, rz = 4.2, 5.8, 4.0
    
    # Ondulaciones biomórficas (surcos y circunvoluciones cerebrales mediante armónicos esféricos)
    sulci = 0.22 * np.sin(7 * U) * np.cos(6 * V) + 0.12 * np.sin(14 * V)
    
    X = (rx + sulci) * np.sin(V) * np.cos(U)
    Y = (ry + sulci) * np.sin(V) * np.sin(U)
    Z = (rz + sulci) * np.cos(V)
    
    # Creación de cisura interhemisférica anatómica longitudinal
    hemisphere_split = 0.45
    X = np.where(X >= 0, X + hemisphere_split, X - hemisphere_split)
    
    # Ligera curvatura fronto-occipital
    Z = Z - 0.08 * (Y**2) / ry
    return X, Y, Z

def build_tract_curve(p0, p1, control, n_points=40):
    """Genera curvas de Bézier cuadráticas para modelar fascículos y tractos axonales curvos."""
    t = np.linspace(0, 1, n_points)
    curve_x = (1 - t)**2 * p0[0] + 2 * (1 - t) * t * control[0] + t**2 * p1[0]
    curve_y = (1 - t)**2 * p0[1] + 2 * (1 - t) * t * control[1] + t**2 * p1[1]
    curve_z = (1 - t)**2 * p0[2] + 2 * (1 - t) * t * control[2] + t**2 * p1[2]
    return curve_x, curve_y, curve_z

# -------------------------------------------------------------
# RENDERIZADO PRINCIPAL
# -------------------------------------------------------------
st.title(f"Ateneo Neurobiológico: {disorder}")
st.caption("Conectómica Frontolímbica, Desregulación Afectiva y Colapso Interpersonal en Psiquiatría de Enlace")

# Panel Superior de Métricas Fisiopatológicas
c1, c2, c3, c4 = st.columns(4)
uncinate_val = max(0.02, data["uncinate_integrity"] * (1.0 - 0.4 * stress))
amigdala_dyn = data["regions"]["Amígdala Bilateral"]["activity"] * (1.0 + 0.5 * stress)
vmpfc_dyn = max(0.05, data["regions"]["vmPFC"]["activity"] * (1.0 - 0.45 * stress))
ratio_top_down = vmpfc_dyn / amigdala_dyn

c1.metric("Integridad Fascículo Uncinado", f"{uncinate_val:.2f}", delta="- Disrupción DTI" if uncinate_val < 0.4 else "Normal")
c2.metric("Reactividad Amigdalina", f"{amigdala_dyn:.2f}", delta=f"{'+' if stress > 0 else ''}{stress*100:.0f}% Estrés")
c3.metric("Freno vmPFC / OFC", f"{vmpfc_dyn:.2f}", delta="Atenuado" if vmpfc_dyn < 0.4 else "Preservado", delta_color="inverse")
c4.metric("Ratio de Inhibición Top-Down", f"{ratio_top_down:.2f}", delta="Falla Crítica" if ratio_top_down < 0.4 else "Funcional", delta_color="inverse")

if view_selection.startswith("1."):
    # -------------------------------------------------------------
    # MODO 1: MODELO ANATÓMICO Y TRACTOGRAFÍA 3D
    # -------------------------------------------------------------
    fig = go.Figure()

    # 1. Manto Cortical 3D Realista (Superficie continua semi-translúcida)
    CX, CY, CZ = build_cortex_surface()
    fig.add_trace(go.Surface(
        x=CX, y=CY, z=CZ,
        colorscale=[[0, '#0f172a'], [0.5, '#1e293b'], [1, '#334155']],
        opacity=0.18,
        showscale=False,
        hoverinfo='none',
        name="Manto Cortical (Espacio MNI)"
    ))

    # 2. Núcleos Subcorticales y Áreas Funcionales (Geometrías volumétricas detalladas)
    for name, rdata in data["regions"].items():
        coords = rdata["coords"]
        act = rdata["activity"] * (1.0 + 0.3 * stress if "HIPER" in rdata["status"] else 1.0 - 0.3 * stress)
        node_color = "#ef4444" if "HIPER" in rdata["status"] else ("#10b981" if "PRESERV" in rdata["status"] else "#f59e0b")
        if "HIPO" in rdata["status"]:
            node_color = "#3b82f6"

        for idx, pt in enumerate(coords):
            # Renderizado esférico de alta resolución para cada núcleo
            phi_s, theta_s = np.mgrid[0.0:np.pi:14j, 0.0:2.0*np.pi:14j]
            rad = 0.55 * np.clip(act, 0.4, 1.8)
            sx = pt[0] + rad * np.sin(phi_s) * np.cos(theta_s)
            sy = pt[1] + rad * np.sin(phi_s) * np.sin(theta_s)
            sz = pt[2] + rad * np.cos(phi_s)

            fig.add_trace(go.Surface(
                x=sx, y=sy, z=sz,
                colorscale=[[0, node_color], [1, '#ffffff']],
                opacity=0.88,
                showscale=False,
                hovertext=f"<b>{name}</b><br>Estado: {rdata['status']}<br>Rol: {rdata['role']}",
                hoverinfo="text",
                name=name,
                showlegend=(idx == 0)
            ))

    # 3. Tractografía: Fascículo Uncinado Bilateral (Amígdala <-> vmPFC / OFC)
    # Modelado anatómico con curvatura alrededor del lóbulo insular
    for side in [1, -1]:
        p_amig = (side * 2.2, -0.8, -1.2)
        p_vmpfc = (side * 0.4, 4.2, -1.2)
        ctrl_unc = (side * 3.5, 1.5, -2.4) # Curvatura ventrolateral característica del uncinado
        ux, uy, uz = build_tract_curve(p_amig, p_vmpfc, ctrl_unc, n_points=50)

        is_severely_impaired = uncinate_val < 0.35
        t_color = "#ef4444" if is_severely_impaired else "#38bdf8"
        t_dash = "dot" if is_severely_impaired else "solid"

        fig.add_trace(go.Scatter3d(
            x=ux, y=uy, z=uz,
            mode='lines',
            line=dict(color=t_color, width=max(2.0, uncinate_val * 10), dash=t_dash),
            name="Fascículo Uncinado (DTI)" if side == 1 else "",
            showlegend=(side == 1),
            hovertext=f"Fascículo Uncinado: Integridad FA = {uncinate_val:.2f} ({'DESCONECTADO / PUNTEADO' if is_severely_impaired else 'FUNCIONAL'})",
            hoverinfo="text"
        ))

    # 4. Tractografía: Haz del Cíngulo (ACC <-> Formación Hipocámpica/Temporal)
    for side in [1, -1]:
        p_acc = (side * 0.3, 2.2, 2.8)
        p_hipp = (side * 2.4, -2.8, -1.0)
        ctrl_cing = (side * 0.8, -0.2, 3.4) # Curva arqueada sobre el cuerpo calloso
        cx, cy, cz = build_tract_curve(p_acc, p_hipp, ctrl_cing, n_points=50)

        fig.add_trace(go.Scatter3d(
            x=cx, y=cy, z=cz,
            mode='lines',
            line=dict(color="#f59e0b" if data["cingulum_integrity"] > 0.5 else "#64748b", width=5, dash="solid"),
            name="Vía del Cíngulo" if side == 1 else "",
            showlegend=(side == 1),
            hovertext="Haz del Cíngulo: Transmisión del conflicto y valencia social",
            hoverinfo="text"
        ))

    # 5. Tractografía Córtico-Estriatal (vmPFC/OFC <-> Accumbens)
    for side in [1, -1]:
        p_ofc = (side * 1.6, 3.8, -2.0)
        p_accumbens = (side * 1.2, 1.2, -0.8)
        fig.add_trace(go.Scatter3d(
            x=[p_ofc[0], p_accumbens[0]],
            y=[p_ofc[1], p_accumbens[1]],
            z=[p_ofc[2], p_accumbens[2]],
            mode='lines',
            line=dict(color="#10b981", width=4),
            name="Proyección Córtico-Estriatal" if side == 1 else "",
            showlegend=(side == 1),
            hovertext="Bucle Córtico-Estriatal: Modulación hedónica e impulsividad",
            hoverinfo="text"
        ))

    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            bgcolor='#030712',
            camera=dict(
                eye=dict(x=1.6, y=-1.5, z=1.2),
                center=dict(x=0, y=0, z=-0.2)
            )
        ),
        paper_bgcolor='#030712',
        margin=dict(l=0, r=0, b=0, t=10),
        legend=dict(font=dict(color='#cbd5e1'), bgcolor='#0f172a', bordercolor='#1f2937', borderwidth=1),
        height=680
    )

    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown(f"""
    <div class="report-box">
        <h4 style="color: #38bdf8; margin: 0 0 8px 0;">Hallazgos en Neuroimagen Estructural y Funcional (DTI / fMRI)</h4>
        <p style="color: #e2e8f0; margin: 0; line-height: 1.5;">{data["dti_findings"]}</p>
    </div>
    """, unsafe_allow_html=True)

else:
    # -------------------------------------------------------------
    # MODO 2: ECOSISTEMA RELACIONAL Y ONDA EXPANSIVA (GRAFO 3D)
    # -------------------------------------------------------------
    fig_sys = go.Figure()

    # Posición central del paciente
    patient_pos = (0, 0, 0)
    fig_sys.add_trace(go.Scatter3d(
        x=[patient_pos[0]], y=[patient_pos[1]], z=[patient_pos[2]],
        mode='markers+text',
        text=["<b>NÚCLEO DEL PACIENTE</b><br>(Desregulación Frontolímbica)"],
        textposition="top center",
        textfont=dict(size=14, color='#ffffff'),
        marker=dict(size=24, color=data["color_theme"], line=dict(color='#ffffff', width=3)),
        name="Paciente"
    ))

    # Coordenadas tridimensionales de las esferas vitales
    rel_nodes = {
        "Pareja / Apego": (5.5, 4.0, 2.5),
        "Ámbito Legal / Penal": (-6.0, -3.5, 2.0),
        "Servicio de Urgencias": (-4.5, 5.5, -3.0),
        "Autoimagen / Identidad": (4.5, -5.0, -2.5),
        "Ámbito Laboral": (6.0, -2.0, 3.5),
        "Ámbito Familiar": (-5.0, 1.0, 4.5),
        "Ámbito Social/Amigos": (2.0, 6.0, 1.0)
    }

    for domain_name, domain_info in data["relational_impact"].items():
        if domain_name in rel_nodes:
            pos = rel_nodes[domain_name]
            tension_dyn = np.clip(domain_info["t"] * (1.0 + 0.4 * stress), 0.1, 1.6)
            is_critical = tension_dyn > 0.85
            edge_color = "#ef4444" if is_critical else "#38bdf8"
            edge_dash = "dash" if is_critical else "solid"

            # Esfera periférica
            fig_sys.add_trace(go.Scatter3d(
                x=[pos[0]], y=[pos[1]], z=[pos[2]],
                mode='markers+text',
                text=[f"<b>{domain_name}</b><br>Tensión: {tension_dyn:.2f}"],
                textposition="bottom center",
                textfont=dict(size=11, color='#e2e8f0'),
                marker=dict(size=14 * tension_dyn, color=edge_color, opacity=0.9),
                hovertext=f"<b>{domain_name}</b><br>{domain_info['desc']}",
                hoverinfo="text",
                name=domain_name
            ))

            # Tensor de tensión que conecta con el centro
            fig_sys.add_trace(go.Scatter3d(
                x=[patient_pos[0], pos[0]],
                y=[patient_pos[1], pos[1]],
                z=[patient_pos[2], pos[2]],
                mode='lines',
                line=dict(color=edge_color, width=max(2.0, tension_dyn * 8), dash=edge_dash),
                showlegend=False,
                hoverinfo='none'
            ))

    fig_sys.update_layout(
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            bgcolor='#030712',
            camera=dict(
                eye=dict(x=1.8, y=1.8, z=1.2),
                center=dict(x=0, y=0, z=0)
            )
        ),
        paper_bgcolor='#030712',
        margin=dict(l=0, r=0, b=0, t=10),
        legend=dict(font=dict(color='#cbd5e1'), bgcolor='#0f172a', bordercolor='#1f2937', borderwidth=1),
        height=680
    )

    st.plotly_chart(fig_sys, use_container_width=True)

    st.markdown("""
    <div class="report-box">
        <h4 style="color: #38bdf8; margin: 0 0 8px 0;">Dinámica Sistémica y Efecto de Onda Expansiva</h4>
        <p style="color: #e2e8f0; margin: 0; line-height: 1.5;">
        A diferencia de los trastornos del Cluster A o C, las fallas frontolímbicas del Cluster B no se limitan al sufrimiento intrapsíquico: se proyectan al exterior a través de conductas que estresan, saturan o rompen las redes sociales, familiares, jurídicas y sanitarias. Al elevar el deslizador de estrés, las líneas rojas punteadas señalan las esferas que entran en crisis de ruptura o saturación institucional.
        </p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------
# Tabla Semiográfica Comparativa
# -------------------------------------------------------------
st.markdown("### Correlación Estructural-Semiológica")
tab_data = []
for r_name, r_vals in data["regions"].items():
    tab_data.append({
        "Estructura Anatómica": r_name,
        "Estado Conectómico": r_vals["status"],
        "Rol en la Patología": r_vals["role"]
    })
st.dataframe(pd.DataFrame(tab_data), use_container_width=True, hide_index=True)
