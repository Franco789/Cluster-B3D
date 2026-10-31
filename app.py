import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="Atlas Neurobiológico 3D: Trastornos Cluster B",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .stApp { background-color: #030712; color: #f1f5f9; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    .stSelectbox, .stSlider { background-color: #0f172a; border-radius: 6px; padding: 4px; }
    h1, h2, h3 { color: #f8fafc; font-weight: 700; letter-spacing: -0.02em; }
    .stat-card {
        background: #0b1329; border: 1px solid #1e293b; border-radius: 8px;
        padding: 12px 16px; margin-bottom: 8px;
    }
    .stat-val { font-size: 1.5rem; font-weight: 800; font-family: monospace; }
    .stat-lbl { font-size: 0.72rem; text-transform: uppercase; color: #94a3b8; letter-spacing: 0.05em; }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# Base de Datos Neurobiológica y Conectómica Multidimensional
# -------------------------------------------------------------
DATA_REGISTRY = {
    "Trastorno Límite de la Personalidad (TLP)": {
        "short_key": "TLP",
        "fa_uncinate": 0.18,
        "amg_act": 1.95,
        "vmpfc_act": 0.22,
        "dacc_act": 1.85,
        "color_accent": "#ef4444",
        "circuit_name": "Hiperreactividad Límbica & Red del Dolor Social",
        "dti_findings": "Fascículo uncinado bilateral con anisotropía fraccional (FA) marcadamente deprimida (Schmahl et al., New et al.). Pérdida de integridad axonal frontotemporal que impide la inhibición top-down del afecto.",
        "fmri_findings": "Coactivación paroxística del dACC y de la ínsula anterior ante el rechazo percibido. El dolor de exclusión interpersonal recluta la misma matriz nociceptiva que el daño somático agudo.",
        "nodes": [
            {"name": "Amígdala Basolateral (Der)", "coords": [2.3, -0.6, -1.4], "color": "#ef4444", "rad": 1.15, "hz": 7.5, "status": "HIPERTRÓFICA FÁSICA", "desc": "Alarma paroxística de supervivencia; traduce rostros neutros como amenazantes."},
            {"name": "Amígdala Basolateral (Izq)", "coords": [-2.3, -0.6, -1.4], "color": "#ef4444", "rad": 1.15, "hz": 7.5, "status": "HIPERTRÓFICA FÁSICA", "desc": "Descarga simpática autónoma inmediata ante la sospecha de abandono."},
            {"name": "vmPFC (Córtex Frontomedial)", "coords": [0.0, 4.4, -0.8], "color": "#38bdf8", "rad": 0.45, "hz": 1.0, "status": "HIPOCONECTADA", "desc": "Falla del freno inhibitorio; incapacidad de extinguir el condicionamiento aversivo."},
            {"name": "dACC (Cíngulo Dorsal)", "coords": [0.0, 2.2, 2.8], "color": "#f43f5e", "rad": 1.05, "hz": 7.0, "status": "DOLOR SOCIAL AGUDO", "desc": "Nodo central de la red de prominencia; traduce la distancia vincular en angustia física."},
            {"name": "Ínsula Anterior", "coords": [3.6, 0.8, -0.1], "color": "#e11d48", "rad": 0.95, "hz": 6.2, "status": "HIPEREXCITACIÓN INTEROCEPTIVA", "desc": "Sustrato neurofisiológico de la vivencia de vacío crónico y disforia visceral."}
        ],
        "tracts": [
            {"from": [2.3, -0.6, -1.4], "to": [0.0, 4.4, -0.8], "ctrl": [3.4, 1.8, -2.2], "name": "Fascículo Uncinado Der. (Disrumpido)", "status": "broken"},
            {"from": [-2.3, -0.6, -1.4], "to": [0.0, 4.4, -0.8], "ctrl": [-3.4, 1.8, -2.2], "name": "Fascículo Uncinado Izq. (Disrumpido)", "status": "broken"},
            {"from": [0.0, 2.2, 2.8], "to": [0.0, 4.4, -0.8], "ctrl": [0.0, 3.4, 1.0], "name": "Proyección Cíngulo-Frontal", "status": "hyper"},
            {"from": [2.3, -0.6, -1.4], "to": [3.6, 0.8, -0.1], "ctrl": [2.9, 0.1, -0.7], "name": "Eje Límbico-Insular Afectivo", "status": "hyper"}
        ],
        "ecosystem": [
            {"name": "Vínculo de Pareja", "desc": "Splitting, idealización vs devaluación y terror pánico al desapego.", "tension": 0.98, "coords": [7.0, 4.0, 2.0], "color": "#ef4444"},
            {"name": "Guardia Médica / Urgencias", "desc": "Consultas reiteradas por gestos parasuicidas, sobredosis e impulsividad.", "tension": 0.95, "coords": [-6.5, 5.0, -2.5], "color": "#ef4444"},
            {"name": "Sentido de Identidad / Self", "desc": "Sensación de vacío insoportable, autodifusión y fluctuación moral.", "tension": 0.94, "coords": [5.0, -5.5, -2.5], "color": "#f43f5e"},
            {"name": "Soporte Familiar Primario", "desc": "Agotamiento de cuidadores, dinámicas de doble vínculo y claudicación.", "tension": 0.88, "coords": [-5.5, -4.0, 3.5], "color": "#fb923c"},
            {"name": "Ámbito Académico / Laboral", "desc": "Interrupción de ciclos de estudio/trabajo por crisis afectivas cíclicas.", "tension": 0.70, "coords": [2.0, 6.5, -3.5], "color": "#eab308"}
        ]
    },
    "Trastorno Antisocial de la Personalidad (TASP)": {
        "short_key": "TASP",
        "fa_uncinate": 0.08,
        "amg_act": 0.12,
        "vmpfc_act": 0.18,
        "dacc_act": 0.18,
        "color_accent": "#f59e0b",
        "circuit_name": "Ablación Funcional Frontolímbica & Falla de Aversión Moral",
        "dti_findings": "Craig et al. y Motzkin et al.: Reducción bilateral crítica de la integridad microestructural del fascículo uncinado (FA < 0.10). Desconexión anatómica casi total entre amígdala y corteza orbitofrontal.",
        "fmri_findings": "Hipoactividad severa de amígdala e ínsula frente al condicionamiento al castigo y ante señales de llanto/miedo ajeno. En contraste, el núcleo accumbens se sobreactiva con incentivos inmediatos.",
        "nodes": [
            {"name": "Amígdala (Hipoactiva)", "coords": [2.3, -0.6, -1.4], "color": "#1e293b", "rad": 0.40, "hz": 0.4, "status": "ATROFIA FUNCIONAL", "desc": "Inmunidad al condicionamiento por miedo o castigo; refractariedad autonómica."},
            {"name": "Amígdala Izquierda (Hipoactiva)", "coords": [-2.3, -0.6, -1.4], "color": "#1e293b", "rad": 0.40, "hz": 0.4, "status": "ATROFIA FUNCIONAL", "desc": "Ausencia de marcadores electrodérmicos de aversión o temor subjetivo."},
            {"name": "vmPFC (Polo Moral Desconectado)", "coords": [0.0, 4.4, -0.8], "color": "#334155", "rad": 0.45, "hz": 0.5, "status": "HIPOCONECTADA", "desc": "Juicio lógico analítico frío, pero sin integración del dolor ajeno en la decisión."},
            {"name": "Núcleo Accumbens (Estriado)", "coords": [1.3, 1.4, -0.8], "color": "#eab308", "rad": 1.25, "hz": 7.5, "status": "HIPERACTIVIDAD PREDATORIA", "desc": "Búsqueda insaciable de recompensa inmediata y dominancia instrumental."},
            {"name": "Ínsula Anterior (Anestesiada)", "coords": [3.6, 0.8, -0.1], "color": "#1e293b", "rad": 0.35, "hz": 0.3, "status": "ANESTESIA INTEROCEPTIVA", "desc": "Carencia absoluta de culpa visceral o remordimiento somatizado."}
        ],
        "tracts": [
            {"from": [2.3, -0.6, -1.4], "to": [0.0, 4.4, -0.8], "ctrl": [3.4, 1.8, -2.2], "name": "Fascículo Uncinado (Ablación Conectómica)", "status": "broken"},
            {"from": [0.0, 4.4, -0.8], "to": [1.3, 1.4, -0.8], "ctrl": [0.7, 3.0, -0.8], "name": "Vía Córtico-Estriatal Desinhibida", "status": "hyper"}
        ],
        "ecosystem": [
            {"name": "Fuero Penal & Penitenciario", "desc": "Reiteración delictiva, crímenes patrimoniales/violentos y condenas.", "tension": 0.99, "coords": [-7.5, -3.5, 2.5], "color": "#ef4444"},
            {"name": "Víctimas / Vínculos Explotados", "desc": "Cosificación instrumental, violencia predatoria y despojo patrimonial.", "tension": 0.96, "coords": [7.0, 4.5, 3.0], "color": "#ef4444"},
            {"name": "Ámbito Contractual / Financiero", "desc": "Fraudes sistemáticos, estafas y ausencia de lealtad comercial.", "tension": 0.88, "coords": [-5.0, 5.5, -3.5], "color": "#fb923c"},
            {"name": "Peritajes Médico-Legales", "desc": "Simulación calculada de trastornos mentales para eludir sanciones penales.", "tension": 0.65, "coords": [3.5, -6.0, -3.0], "color": "#eab308"},
            {"name": "Eje Identitario", "desc": "Egosintonía perfecta; ausencia de autocrítica o malestar interno.", "tension": 0.12, "coords": [5.5, -2.0, 4.5], "color": "#10b981"}
        ]
    },
    "Trastorno Narcisista de la Personalidad (TNP)": {
        "short_key": "TNP",
        "fa_uncinate": 0.46,
        "amg_act": 1.05,
        "vmpfc_act": 0.48,
        "dacc_act": 1.80,
        "color_accent": "#a855f7",
        "circuit_name": "Disociación Fronto-Insular & Vulnerabilidad al Desprecio",
        "dti_findings": "Fan et al., Nenadic et al.: Alteración volumétrica y conectómica en la sustancia blanca prefrontal medial e ínsula anterior. Teoría de la mente cognitiva intacta, con deterioro de la empatía afectiva somática.",
        "fmri_findings": "Picos de hiperactividad en el dACC y amígdala ante cualquier crítica o falta de admiración ('herida narcisista'), con reactividad vindicativa compensatoria.",
        "nodes": [
            {"name": "dACC (Radar de Jerarquía)", "coords": [0.0, 2.2, 2.8], "color": "#a855f7", "rad": 1.25, "hz": 7.4, "status": "HIPERREACTIVO AL DESPRECIO", "desc": "Alarma desmedida ante el desacato, la crítica o la pérdida de admiración."},
            {"name": "vmPFC (Autoimagen Grandiosa)", "coords": [0.0, 4.4, -0.8], "color": "#c084fc", "rad": 0.85, "hz": 2.8, "status": "COMPENSACIÓN GRANDIOSA", "desc": "Mantenimiento activo del constructo de superioridad como defensa ante el vacío."},
            {"name": "Amígdala (Rabia Narcisista)", "coords": [2.3, -0.6, -1.4], "color": "#ec4899", "rad": 0.80, "hz": 5.2, "status": "VULNERABILIDAD FÁSICA", "desc": "Explosiones coléricas vindicativas ante la exposición de debilidad."},
            {"name": "Ínsula (Desconexión Vicaria)", "coords": [3.6, 0.8, -0.1], "color": "#334155", "rad": 0.38, "hz": 0.8, "status": "ANESTESIA EMPÁTICA", "desc": "Incapacidad neurofisiológica de registrar el dolor causado a subordinados."}
        ],
        "tracts": [
            {"from": [0.0, 2.2, 2.8], "to": [0.0, 4.4, -0.8], "ctrl": [0.0, 3.4, 1.0], "name": "Eje de Autoevaluación Hipervigilante", "status": "hyper"},
            {"from": [2.3, -0.6, -1.4], "to": [0.0, 2.2, 2.8], "ctrl": [1.2, 0.7, 0.8], "name": "Circuito de Ira Vindicativa", "status": "hyper"},
            {"from": [3.6, 0.8, -0.1], "to": [0.0, 4.4, -0.8], "ctrl": [2.2, 2.4, -0.5], "name": "Desconexión Fronto-Insular", "status": "broken"}
        ],
        "ecosystem": [
            {"name": "Vínculo de Pareja", "desc": "Cosificación, exigencia de pleitesía, humillación y ley del hielo.", "tension": 0.92, "coords": [6.5, 4.0, 2.0], "color": "#ef4444"},
            {"name": "Autoimagen & Cohesión del Self", "desc": "Fragilidad extrema; colapso disfórico profundo ante pérdidas de estatus.", "tension": 0.96, "coords": [0.0, -7.0, -2.5], "color": "#a855f7"},
            {"name": "Ámbito Corporativo / Laboral", "desc": "Rivalidades destructivas, litigios por honra y boicot a colaboradores.", "tension": 0.84, "coords": [-6.0, 4.5, 3.0], "color": "#fb923c"},
            {"name": "Familia de Origen", "desc": "Exigencia de tributo incondicional o ruptura agresiva con exclusión total.", "tension": 0.76, "coords": [-5.0, -4.5, 3.0], "color": "#fb923c"},
            {"name": "Consultas a Salud Mental", "desc": "Abandono de psicoterapia ante señalamientos que confronten la grandiosidad.", "tension": 0.52, "coords": [4.0, 6.0, -3.0], "color": "#38bdf8"}
        ]
    },
    "Trastorno Histriónico de la Personalidad (THP)": {
        "short_key": "THP",
        "fa_uncinate": 0.60,
        "amg_act": 1.30,
        "vmpfc_act": 0.36,
        "dacc_act": 1.10,
        "color_accent": "#06b6d4",
        "circuit_name": "Labilidad Afectiva, Búsqueda de Refuerzo & Somatización",
        "dti_findings": "Desconexión relativa entre la corteza prefrontal dorsolateral y cortezas de asociación témporo-parietales, favoreciendo un estilo cognitivo impresionista, difuso y altamente sugestionable.",
        "fmri_findings": "Hipersensibilidad del núcleo accumbens y amígdala frente a la atención o halago social, con amplificación somatosensorial e insular (base de los síntomas conversivos).",
        "nodes": [
            {"name": "Amígdala Límbica", "coords": [2.3, -0.6, -1.4], "color": "#06b6d4", "rad": 0.90, "hz": 6.2, "status": "HIPEREXCITABLE LÁBIL", "desc": "Emotividad intensa y cambiante; intolerancia al desinterés del entorno."},
            {"name": "Núcleo Accumbens Social", "coords": [1.3, 1.4, -0.8], "color": "#22d3ee", "rad": 1.10, "hz": 6.5, "status": "HIPERRESPUESTA AL FEEDBACK", "desc": "Dependencia absoluta del halago, la seducción y la validación externa."},
            {"name": "Ínsula Somatosensorial", "coords": [3.6, 0.8, -0.1], "color": "#0891b2", "rad": 0.85, "hz": 5.4, "status": "SOMATIZACIÓN INTEROCEPTIVA", "desc": "Conversión corporal de angustias afectivas; teatralidad física y somatizaciones."},
            {"name": "vmPFC Impresionista", "coords": [0.0, 4.4, -0.8], "color": "#475569", "rad": 0.42, "hz": 1.4, "status": "PROCESAMIENTO DIFUSO", "desc": "Falla en el procesamiento lógico analítico; razonamiento guiado por impresiones."}
        ],
        "tracts": [
            {"from": [2.3, -0.6, -1.4], "to": [1.3, 1.4, -0.8], "ctrl": [1.7, 0.4, -1.0], "name": "Eje Límbico-Recompensa Interpersonal", "status": "hyper"},
            {"from": [0.0, 4.4, -0.8], "to": [2.3, -0.6, -1.4], "ctrl": [1.4, 1.9, -1.1], "name": "Modulación Frontal Deficitaria", "status": "broken"}
        ],
        "ecosystem": [
            {"name": "Vínculo Conyugal / Pareja", "desc": "Seducción inapropiada, celopatía y reclamo permanente de protagonismo.", "tension": 0.85, "coords": [6.0, 3.5, 2.0], "color": "#ef4444"},
            {"name": "Guardia Médica de Emergencias", "desc": "Ingresos por síntomas neurológicos funcionales, pseudocrisis o hiperventilación.", "tension": 0.82, "coords": [-5.0, 5.5, -2.5], "color": "#fb923c"},
            {"name": "Círculo Social Amplio", "desc": "Relaciones superficiales asumidas como íntimas; agotamiento del entorno.", "tension": 0.72, "coords": [4.5, -5.0, 2.5], "color": "#fb923c"},
            {"name": "Eje de Autoestima", "desc": "Sensación de desvanecimiento subjetivo ante la falta de atención o halago.", "tension": 0.80, "coords": [-1.8, -6.0, -2.0], "color": "#06b6d4"},
            {"name": "Ámbito Laboral Metódico", "desc": "Incapacidad para labores rutinarias o sin visibilidad protagónica.", "tension": 0.50, "coords": [2.2, 6.5, -3.5], "color": "#38bdf8"}
        ]
    }
}

# --- Controles en Barra Lateral ---
st.sidebar.markdown("### 🎛️ Consola de Neuropsiquiatría")
selected_disorder = st.sidebar.selectbox("Entidad Patológica:", list(DATA_REGISTRY.keys()))
stress_slider = st.sidebar.slider("Nivel de Disparador / Estrés Ambiental:", 0.0, 1.0, 0.5, 0.05)
view_selector = st.sidebar.radio("Modo de Inspección 3D:", ["1. Conectoma & Tractografía DTI", "2. Grafo de Onda Expansiva (Vidas Afectadas)"])

current_data = DATA_REGISTRY[selected_disorder]

# Cálculos dinámicos en tiempo real
dyn_fa = max(0.03, current_data["fa_uncinate"] * (1.0 - 0.45 * stress_slider))
dyn_amg = current_data["amg_act"] * (1.0 + 0.5 * stress_slider)
dyn_pfc = max(0.04, current_data["vmpfc_act"] * (1.0 - 0.5 * stress_slider))
ratio_ctrl = dyn_pfc / dyn_amg

# --- Encabezado y Métricas ---
st.title(selected_disorder)
st.caption(f"**Circuito Fisiopatológico:** {current_data['circuit_name']}")

m1, m2, m3, m4 = st.columns(4)
with m1:
    col = "#ef4444" if dyn_fa < 0.25 else "#38bdf8"
    st.markdown(f"""<div class="stat-card"><div class="stat-lbl">Integridad Fascículo Uncinado</div><div class="stat-val" style="color: {col};">{dyn_fa:.2f} FA</div></div>""", unsafe_allow_html=True)
with m2:
    st.markdown(f"""<div class="stat-card"><div class="stat-lbl">Reactividad Amigdalina (fMRI)</div><div class="stat-val" style="color: {'#ef4444' if dyn_amg > 1.3 else '#94a3b8'};">{dyn_amg:.2f} BOLD</div></div>""", unsafe_allow_html=True)
with m3:
    st.markdown(f"""<div class="stat-card"><div class="stat-lbl">Control Prefrontal (vmPFC)</div><div class="stat-val" style="color: {'#ef4444' if dyn_pfc < 0.3 else '#38bdf8'};">{dyn_pfc:.2f} z</div></div>""", unsafe_allow_html=True)
with m4:
    col_r = "#ef4444" if ratio_ctrl < 0.35 else "#10b981"
    st.markdown(f"""<div class="stat-card"><div class="stat-lbl">Ratio Inhibitorio Top-Down</div><div class="stat-val" style="color: {col_r};">{ratio_ctrl:.2f}</div></div>""", unsafe_allow_html=True)

# -------------------------------------------------------------
# Motor Gráfico WebGL Nativo (Three.js sin dependencias frágiles)
# -------------------------------------------------------------
payload = {
    "view": view_selector,
    "stress": stress_slider,
    "nodes": current_data["nodes"],
    "tracts": current_data["tracts"],
    "ecosystem": current_data["ecosystem"],
    "accent": current_data["color_accent"]
}

html_webgl = f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body {{ margin: 0; overflow: hidden; background: #030712; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
    #viewport {{ width: 100vw; height: 100vh; position: relative; }}
    #hud {{
      position: absolute; bottom: 20px; left: 20px; z-index: 100;
      background: rgba(11, 19, 41, 0.94); backdrop-filter: blur(12px);
      border: 1px solid #1e293b; border-left: 3px solid #38bdf8; border-radius: 6px;
      padding: 14px 18px; color: #f1f5f9; max-width: 480px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.8);
    }}
    .hud-title {{ font-weight: 700; color: #38bdf8; font-size: 0.95rem; margin-bottom: 4px; font-family: monospace; }}
    .hud-desc {{ color: #94a3b8; font-size: 0.80rem; line-height: 1.4; }}
    #view-btns {{
      position: absolute; top: 20px; right: 20px; z-index: 100;
      display: flex; gap: 8px;
    }}
    .btn {{
      background: rgba(15, 23, 42, 0.9); border: 1px solid #334155; color: #cbd5e1;
      padding: 6px 12px; border-radius: 4px; font-size: 0.72rem; cursor: pointer;
      font-family: monospace; text-transform: uppercase;
    }}
    .btn:hover {{ background: #1e293b; color: #38bdf8; border-color: #38bdf8; }}
  </style>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
</head>
<body>
  <div id="viewport">
    <div id="view-btns">
      <button class="btn" onclick="resetView()">Reset Cámara</button>
    </div>
    <div id="hud">
      <div id="hud-head" class="hud-title">Conectoma Interactivo</div>
      <div id="hud-body" class="hud-desc">Pasa el cursor sobre los núcleos o tractos axonales para ver el correlato funcional. Usa el clic izquierdo para rotar y la rueda para hacer zoom.</div>
    </div>
  </div>

  <script>
    const DATA = {json.dumps(payload)};
    const container = document.getElementById('viewport');

    const scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x030712, 0.025);

    const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.set(0, 3, 22);

    const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    container.appendChild(renderer.domElement);

    // Sistema orbital propio liviano (sin scripts externos que fallen)
    let isDragging = false;
    let prevMouseX = 0, prevMouseY = 0;
    let rotX = 0.2, rotY = 0;

    window.addEventListener('mousedown', (e) => {{ isDragging = true; prevMouseX = e.clientX; prevMouseY = e.clientY; }});
    window.addEventListener('mouseup', () => {{ isDragging = false; }});
    window.addEventListener('mousemove', (e) => {{
      if (isDragging) {{
        const deltaX = e.clientX - prevMouseX;
        const deltaY = e.clientY - prevMouseY;
        rotY += deltaX * 0.008;
        rotX += deltaY * 0.008;
        prevMouseX = e.clientX;
        prevMouseY = e.clientY;
      }}
    }});
    window.addEventListener('wheel', (e) => {{
      camera.position.z = Math.min(35, Math.max(8, camera.position.z + e.deltaY * 0.02));
    }});

    function resetView() {{
      rotX = 0.2; rotY = 0; camera.position.set(0, 3, 22);
    }}

    // Iluminación
    scene.add(new THREE.AmbientLight(0xffffff, 0.85));
    const pLight1 = new THREE.PointLight(0x38bdf8, 2.5, 60);
    pLight1.position.set(6, 12, 14);
    scene.add(pLight1);

    const pLight2 = new THREE.PointLight(0xa855f7, 2.0, 50);
    pLight2.position.set(-10, -8, -10);
    scene.add(pLight2);

    const interactiveGroup = new THREE.Group();
    scene.add(interactiveGroup);

    const hoverables = [];
    const pulsingNodes = [];
    const particleFlows = [];

    // -------------------------------------------------------------
    // MALLA ANATÓMICA CORTICAL CONTINUA (GLASS BRAIN VOLUMÉTRICO)
    // -------------------------------------------------------------
    function buildGlassBrain() {{
      const uSegs = 80, vSegs = 80;
      const geo = new THREE.BufferGeometry();
      const pos = [];

      for(let i=0; i<=uSegs; i++) {{
        let u = (i / uSegs) * Math.PI * 2;
        for(let j=0; j<=vSegs; j++) {{
          let v = (j / vSegs) * Math.PI;

          let rx = 4.4, ry = 5.8, rz = 4.1;
          // Ondulaciones anatómicas reales de giros y cisuras
          let sulci = 0.26 * Math.sin(8 * u) * Math.cos(7 * v) + 
                      0.16 * Math.sin(16 * v) * Math.cos(4 * u);

          let x = (rx + sulci) * Math.sin(v) * Math.cos(u);
          let y = (ry + sulci) * Math.sin(v) * Math.sin(u);
          let z = (rz + sulci) * Math.cos(v);

          // Cisura sagital interhemisférica
          if (x >= 0) x += 0.50; else x -= 0.50;
          z -= 0.08 * (y * y) / ry;

          pos.push(x, y, z);
        }}
      }}
      geo.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
      geo.computeVertexNormals();

      const mat = new THREE.MeshPhysicalMaterial({{
        color: 0x1e293b,
        emissive: 0x0f172a,
        roughness: 0.2,
        metalness: 0.1,
        transparent: true,
        opacity: DATA.view.includes("1.") ? 0.22 : 0.06,
        wireframe: true,
        depthWrite: false
      }});
      return new THREE.Mesh(geo, mat);
    }}

    const cortexMesh = buildGlassBrain();
    interactiveGroup.add(cortexMesh);

    // -------------------------------------------------------------
    // RENDERIZADO SEGÚN EL MODO SELECCIONADO
    // -------------------------------------------------------------
    if (DATA.view.includes("1.")) {{
      // Modo Conectoma & Tractografía
      DATA.nodes.forEach(n => {{
        const geo = new THREE.SphereGeometry(n.rad, 24, 24);
        const mat = new THREE.MeshStandardMaterial({{
          color: n.color,
          emissive: n.color,
          emissiveIntensity: 1.6,
          roughness: 0.3
        }});
        const mesh = new THREE.Mesh(geo, mat);
        mesh.position.set(...n.coords);
        mesh.userData = {{ name: n.name, desc: "<b>Estado:</b> " + n.status + "<br><b>Función:</b> " + n.desc, hz: n.hz }};
        interactiveGroup.add(mesh);
        hoverables.push(mesh);
        pulsingNodes.push(mesh);

        // Halo de activación
        const haloGeo = new THREE.SphereGeometry(n.rad * 1.4, 16, 16);
        const haloMat = new THREE.MeshBasicMaterial({{ color: n.color, transparent: true, opacity: 0.25, wireframe: true }});
        const halo = new THREE.Mesh(haloGeo, haloMat);
        halo.position.copy(mesh.position);
        interactiveGroup.add(halo);
      }});

      // Tractografía de haces axonales
      DATA.tracts.forEach(t => {{
        const p0 = new THREE.Vector3(...t.from);
        const p1 = new THREE.Vector3(...t.to);
        const ctrl = new THREE.Vector3(...t.ctrl);
        const curve = new THREE.QuadraticBezierCurve3(p0, ctrl, p1);

        const isBroken = t.status === "broken";
        const tubeColor = isBroken ? 0xef4444 : (t.status === "hyper" ? 0xf43f5e : 0x38bdf8);

        const tubeGeo = new THREE.TubeGeometry(curve, 32, isBroken ? 0.03 : 0.07, 8, false);
        const tubeMat = new THREE.MeshStandardMaterial({{
          color: tubeColor,
          emissive: tubeColor,
          emissiveIntensity: isBroken ? 0.5 : 1.2,
          transparent: true,
          opacity: isBroken ? 0.45 : 0.85
        }});
        const tube = new THREE.Mesh(tubeGeo, tubeMat);
        tube.userData = {{ name: t.name, desc: isBroken ? "Tracto con pérdida severa de anisotropía fraccional (FA) y desorganización axonal." : "Tracto en hiperactivación funcional fásica continua." }};
        interactiveGroup.add(tube);
        hoverables.push(tube);

        // Partículas de potenciales de acción
        if (!isBroken) {{
          const pCount = 10;
          const pGeo = new THREE.BufferGeometry();
          const pPos = new Float32Array(pCount * 3);
          for(let k=0; k<pCount; k++) {{
            const p = curve.getPoint(k / pCount);
            pPos[k*3] = p.x; pPos[k*3+1] = p.y; pPos[k*3+2] = p.z;
          }}
          pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
          const pMat = new THREE.PointsMaterial({{ color: tubeColor, size: 0.16, transparent: true, opacity: 0.95 }});
          const points = new THREE.Points(pGeo, pMat);
          interactiveGroup.add(points);
          particleFlows.push({{ points: points, curve: curve, speed: t.status === "hyper" ? 0.8 : 0.4 }});
        }}
      }});

    }} else {{
      // Modo Grafo de Onda Expansiva (Vidas Afectadas)
      DATA.ecosystem.forEach(e => {{
        const rad = 1.1 + e.tension * 0.5;
        const geo = new THREE.SphereGeometry(rad, 24, 24);
        const mat = new THREE.MeshStandardMaterial({{
          color: e.color,
          emissive: e.color,
          emissiveIntensity: e.tension * 2.0,
          roughness: 0.3
        }});
        const mesh = new THREE.Mesh(geo, mat);
        mesh.position.set(...e.coords);
        mesh.userData = {{ name: e.name, desc: e.desc + "<br><b>Tensión Sistémica:</b> " + (e.tension * 100).toFixed(0) + "%" }};
        interactiveGroup.add(mesh);
        hoverables.push(mesh);

        // Tensor de colapso hacia el centro
        const lineGeo = new THREE.BufferGeometry().setFromPoints([
          new THREE.Vector3(0, 0, 0),
          new THREE.Vector3(...e.coords)
        ]);
        const lineMat = new THREE.LineBasicMaterial({{
          color: e.tension > 0.88 ? 0xef4444 : 0x38bdf8,
          linewidth: 3,
          transparent: true,
          opacity: 0.8
        }});
        interactiveGroup.add(new THREE.Line(lineGeo, lineMat));
      }});
    }}

    // Raycasting para inspección con mouse
    const raycaster = new THREE.Raycaster();
    const mouse = new THREE.Vector2();
    const hudHead = document.getElementById('hud-head');
    const hudBody = document.getElementById('hud-body');

    window.addEventListener('pointermove', (e) => {{
      const rect = renderer.domElement.getBoundingClientRect();
      mouse.x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
      mouse.y = -((e.clientY - rect.top) / rect.height) * 2 + 1;

      raycaster.setFromCamera(mouse, camera);
      const hits = raycaster.intersectObjects(hoverables);

      if (hits.length > 0) {{
        const target = hits[0].object;
        if (target.userData && target.userData.name) {{
          hudHead.innerText = target.userData.name;
          hudBody.innerHTML = target.userData.desc;
          hudHead.style.color = "#38bdf8";
        }}
      }}
    }});

    // Loop de render a 60 FPS
    const clock = new THREE.Clock();
    function render() {{
      requestAnimationFrame(render);
      const t = clock.getElapsedTime();

      // Rotación suave del modelo
      interactiveGroup.rotation.x = rotX;
      interactiveGroup.rotation.y = rotY + t * 0.1;

      // Pulsación senoidal biológica de los núcleos
      pulsingNodes.forEach(mesh => {{
        const hz = mesh.userData.hz || 2.0;
        const scale = 1.0 + Math.sin(t * hz) * 0.12;
        mesh.scale.set(scale, scale, scale);
      }});

      // Movimiento de partículas sobre los axones
      particleFlows.forEach(pf => {{
        const pos = pf.points.geometry.attributes.position.array;
        const count = pos.length / 3;
        for(let i=0; i<count; i++) {{
          let progress = ((t * pf.speed) + (i / count)) % 1.0;
          let pt = pf.curve.getPoint(progress);
          pos[i*3] = pt.x;
          pos[i*3+1] = pt.y;
          pos[i*3+2] = pt.z;
        }}
        pf.points.geometry.attributes.position.needsUpdate = true;
      }});

      renderer.render(scene, camera);
    }}
    render();

    window.addEventListener('resize', () => {{
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    }});
  </script>
</body>
</html>
"""

components.html(html_webgl, height=660, scrolling=False)

# -------------------------------------------------------------
# Ficha Técnica y Evidencia Clínica para la Exposición
# -------------------------------------------------------------
st.markdown("---")
col_l, col_r = st.columns([1.3, 1.0])

with col_l:
    st.markdown("### 🔬 Sustrato Científico y Evidencia en Neuroimagen")
    st.markdown(f"""
    <div style="background-color: #0b1329; border-left: 4px solid #38bdf8; padding: 14px; border-radius: 4px; margin-bottom: 12px;">
      <b style="color: #38bdf8;">Tractografía DTI:</b> {current_data['dti_findings']}<br><br>
      <b style="color: #38bdf8;">Resonancia Funcional (fMRI):</b> {current_data['fmri_findings']}
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    * **Fascículo Uncinado (*Uncinate Fasciculus*):** Conecta directamente el polo anterior temporal/límbico con la corteza orbitofrontal y ventromedial. Su baja anisotropía fraccional demostrada en DTI explica la persistencia de respuestas emocionales no moduladas por la lógica o el aprendizaje previo.
    * **Red de Prominencia (*Salience Network*):** La coactivación de la ínsula anterior y el dACC detecta de manera distorsionada los estímulos interpersonales, interpretando la neutralidad como abandono inminente (TLP) o como desafío de jerarquía (TNP).
    """)

with col_r:
    st.markdown("### 🌐 El Fenómeno de Onda Expansiva (Vidas Afectadas)")
    st.markdown("""
    A diferencia de la patología neurótica convencional, donde el sufrimiento se contiene en el ámbito subjetivo, en el **Cluster B** la falla del freno inhibitorio biológico se traslada de forma directa al tejido social:
    * **Área Vinculante:** Ruptura destructiva de lazos de apego por mecanismos de escisión (*splitting*) o manipulación instrumental.
    * **Área Sanitaria:** Frecuentación compulsiva de guardias por conductas autolesivas o descompensaciones disfóricas agudas.
    * **Área Judicial / Penal:** Colisiones constantes con la ley en personalidades antisociales o litigios narcisistas por honra y patrimonio.
    """)
