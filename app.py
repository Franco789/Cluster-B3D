import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="Atlas Neurobiológico & Conectómico del Cluster B",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estética de consola quirúrgica / estación de neuroimagen funcional
st.markdown("""
<style>
    .stApp { background-color: #020617; color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    .stSelectbox, .stSlider { background-color: #0b1329; border-radius: 8px; padding: 4px; }
    h1, h2, h3 { color: #f8fafc; font-weight: 700; letter-spacing: -0.03em; }
    .hud-box {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.9) 0%, rgba(2, 6, 23, 0.95) 100%);
        border: 1px solid rgba(56, 189, 248, 0.25);
        border-radius: 10px; padding: 14px 18px; margin-bottom: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6);
    }
    .hud-metric { font-size: 1.5rem; font-weight: 800; color: #38bdf8; font-family: monospace; }
    .hud-sub { font-size: 0.72rem; text-transform: uppercase; color: #94a3b8; letter-spacing: 0.08em; }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# Matriz Conectómica Fisiopatológica Calibrada (Coordenadas MNI152)
# -------------------------------------------------------------------------
CLINICAL_DATABASE = {
    "TLP": {
        "title": "Trastorno Límite de la Personalidad (Borderline)",
        "subtitle": "Hiperreactividad Límbica, Ruptura Uncinada & Alarma de Dolor Social",
        "fa_uncinate": 0.19, # Anisotropía fraccional severamente degradada (Schmahl et al.)
        "amg_activity": 1.95,
        "vmpfc_control": 0.20,
        "acc_social_pain": 1.80,
        "pathology_code": "BORDERLINE",
        "circuit_summary": "La hiperactividad amigdalina fásica secuestra el procesamiento cognitivo. El fascículo uncinado no logra transmitir la señal inhibitoria top-down desde la corteza orbitofrontal, provocando que la señal de rechazo active la red del dolor físico/social (dACC/Ínsula) con intensidad catastrófica.",
        "nodes": [
            {"id": "amg_r", "name": "Amígdala Basolateral Der.", "x": 2.4, "y": -0.6, "z": -1.5, "color": "#ff0055", "size": 1.1, "pulse_speed": 8.0, "desc": "Sensibilidad fásica a rostros neutros procesados como amenazantes o abandonantes."},
            {"id": "amg_l", "name": "Amígdala Basolateral Izq.", "x": -2.4, "y": -0.6, "z": -1.5, "color": "#ff0055", "size": 1.1, "pulse_speed": 8.0, "desc": "Desregulación autonómica; descarga simpática masiva inmediata."},
            {"id": "vmpfc", "name": "Córtex Prefrontal Ventromedial", "x": 0.0, "y": 4.8, "z": -0.8, "color": "#0284c7", "size": 0.5, "pulse_speed": 1.0, "desc": "Incapacidad para contextualizar la experiencia afectiva; colapso de mentalización."},
            {"id": "ofc", "name": "Córtex Orbitofrontal", "x": 1.8, "y": 4.0, "z": -1.8, "color": "#0284c7", "size": 0.5, "pulse_speed": 1.0, "desc": "Falla en la extinción del condicionamiento aversivo; memoria de apego traumático."},
            {"id": "dacc", "name": "Cíngulo Anterior Dorsal (dACC)", "x": 0.0, "y": 2.4, "z": 2.8, "color": "#f43f5e", "size": 1.0, "pulse_speed": 6.5, "desc": "Nodo central de dolor social (paradigmas Cyberball); activa el circuito de dolor tisular."},
            {"id": "insula_r", "name": "Ínsula Anterior Derecha", "x": 3.9, "y": 0.8, "z": 0.2, "color": "#e11d48", "size": 0.95, "pulse_speed": 6.0, "desc": "Interocepción aversiva: vivencia somática del 'vacío' y disforia intolerable."},
            {"id": "insula_l", "name": "Ínsula Anterior Izquierda", "x": -3.9, "y": 0.8, "z": 0.2, "color": "#e11d48", "size": 0.95, "pulse_speed": 6.0, "desc": "Amplificación somatomorfa del dolor psicológico."}
        ],
        "tracts": [
            {"from": "amg_r", "to": "ofc", "ctrl": [3.8, 2.0, -2.6], "type": "uncinate", "status": "frayed", "name": "Fascículo Uncinado Derecho (FA: 0.19)"},
            {"from": "amg_l", "to": "vmpfc", "ctrl": [-3.8, 2.0, -2.6], "type": "uncinate", "status": "frayed", "name": "Fascículo Uncinado Izquierdo (FA: 0.18)"},
            {"from": "dacc", "to": "vmpfc", "ctrl": [0.0, 3.6, 1.2], "type": "cingulum", "status": "hyperactive", "name": "Proyección Cíngulo-Frontal"},
            {"from": "amg_r", "to": "insula_r", "ctrl": [3.2, 0.0, -0.6], "type": "salience", "status": "hyperactive", "name": "Vía Amígdalo-Insular Afectiva"}
        ],
        "social_nodes": [
            {"name": "Vínculo de Pareja / Apego", "impact": "Splitting, devaluación paroxística y pánico a la separación", "tension": 0.98, "coords": [7.5, 4.0, 2.0], "color": "#ef4444"},
            {"name": "Guardia Médica / Urgencias", "impact": "Consultas reiteradas por parasuicidio y autolesiones no suicidas", "tension": 0.95, "coords": [-7.0, 5.5, -3.0], "color": "#ef4444"},
            {"name": "Identidad / Self", "impact": "Sensación de vacío insoportable, autodifusión y fluctuación moral", "tension": 0.94, "coords": [5.5, -6.0, -2.5], "color": "#f43f5e"},
            {"name": "Soporte Familiar Cercano", "impact": "Agotamiento de cuidadores, doble vínculo y triangulaciones", "tension": 0.89, "coords": [-6.0, -4.5, 3.5], "color": "#fb923c"},
            {"name": "Estabilidad Académico/Laboral", "impact": "Interrupción de trayectorias por episodios disfóricos agudos", "tension": 0.72, "coords": [2.0, 7.5, -3.5], "color": "#eab308"}
        ]
    },
    "TASP": {
        "title": "Trastorno Antisocial de la Personalidad (Psicopatía)",
        "subtitle": "Desconexión Frontolímbica Estructural, Atrofia Amigdalina & Insensibilidad al Castigo",
        "fa_uncinate": 0.09,
        "amg_activity": 0.15,
        "vmpfc_control": 0.22,
        "acc_social_pain": 0.20,
        "pathology_code": "ANTISOCIAL",
        "circuit_summary": "Interrupción casi completa del fascículo uncinado. La amígdala no genera señales de alarma ante rostros asustados o amenazas punitivas. En contraste, el núcleo accumbens opera sin regulación inhibitoria, dirigiendo la conducta hacia la predación instrumental.",
        "nodes": [
            {"id": "amg_r", "name": "Amígdala (Hipoactiva)", "x": 2.4, "y": -0.6, "z": -1.5, "color": "#1e293b", "size": 0.4, "pulse_speed": 0.3, "desc": "Inmunidad al condicionamiento aversivo; atrofia de la respuesta de alarma."},
            {"id": "amg_l", "name": "Amígdala (Hipoactiva)", "x": -2.4, "y": -0.6, "z": -1.5, "color": "#1e293b", "size": 0.4, "pulse_speed": 0.3, "desc": "Ausencia de marcadores biológicos de culpa o temor."},
            {"id": "vmpfc", "name": "vmPFC Moral", "x": 0.0, "y": 4.8, "z": -0.8, "color": "#334155", "size": 0.45, "pulse_speed": 0.5, "desc": "Juicio moral disociado del afecto visceral."},
            {"id": "accumbens", "name": "Núcleo Accumbens (Estriado Ventral)", "x": 1.4, "y": 1.6, "z": -0.9, "color": "#eab308", "size": 1.25, "pulse_speed": 7.0, "desc": "Sensibilidad extrema a incentivos inmediatos y dominancia instrumental."},
            {"id": "insula_r", "name": "Ínsula Anterior (Anestesiada)", "x": 3.9, "y": 0.8, "z": 0.2, "color": "#1e293b", "size": 0.35, "pulse_speed": 0.3, "desc": "Ausencia de resonancia empática ante el dolor ajeno."}
        ],
        "tracts": [
            {"from": "amg_r", "to": "vmpfc", "ctrl": [3.8, 2.0, -2.6], "type": "uncinate", "status": "severed", "name": "Fascículo Uncinado (Ablación Conectómica DTI)"},
            {"from": "vmpfc", "to": "accumbens", "ctrl": [0.8, 3.2, -0.9], "type": "frontostriatal", "status": "uninhibited", "name": "Vía Estriatal Desinhibida"}
        ],
        "social_nodes": [
            {"name": "Sistema Penal / Penitenciario", "impact": "Reiteración delictiva, transgresión sistemática del marco normativo", "tension": 0.99, "coords": [-8.0, -4.0, 2.5], "color": "#ef4444"},
            {"name": "Víctimas / Vínculos Cosificados", "impact": "Explotación económica, violencia instrumental y manipulación fría", "tension": 0.96, "coords": [7.5, 5.0, 3.0], "color": "#ef4444"},
            {"name": "Entorno Laboral / Contractual", "impact": "Estafas, fraudes corporativos, conductas predatorias interpersonales", "tension": 0.88, "coords": [-5.5, 6.0, -4.0], "color": "#fb923c"},
            {"name": "Sistema Sanitario", "impact": "Litigios, peritajes forenses, simulación de patología para eximición", "tension": 0.60, "coords": [4.0, -6.5, -3.0], "color": "#eab308"},
            {"name": "Eje Identitario", "impact": "Egosintonía completa; ausencia radical de autocrítica", "tension": 0.15, "coords": [6.0, -2.0, 5.0], "color": "#10b981"}
        ]
    },
    "TNP": {
        "title": "Trastorno Narcisista de la Personalidad",
        "subtitle": "Disociación Fronto-Insular, Hipersensibilidad al Estatus & Alarma por Devaluación",
        "fa_uncinate": 0.48,
        "amg_activity": 1.10,
        "vmpfc_control": 0.45,
        "acc_social_pain": 1.70,
        "pathology_code": "NARCISSISTIC",
        "circuit_summary": "Marcada disociación entre la corteza insular anterior (empatía afectiva atenuada) y el dACC (hiperactivo frente a cualquier indicio de devaluación o crítica). La red por defecto sostiene una autoimagen grandiosa artificial, vulnerable al colapso disfórico.",
        "nodes": [
            {"id": "dacc", "name": "dACC (Radar de Jerarquía)", "x": 0.0, "y": 2.4, "z": 2.8, "color": "#a855f7", "size": 1.2, "pulse_speed": 7.5, "desc": "Alarma desmedida ante el desprecio, la indiferencia o la falta de tributo."},
            {"id": "vmpfc", "name": "vmPFC / Polo Frontal", "x": 0.0, "y": 4.8, "z": -0.8, "color": "#c084fc", "size": 0.85, "pulse_speed": 3.0, "desc": "Construcción hipertrofiada del constructo grandioso compensatorio."},
            {"id": "amg_r", "name": "Amígdala (Rabia Narcisista)", "x": 2.4, "y": -0.6, "z": -1.5, "color": "#ec4899", "size": 0.85, "pulse_speed": 5.0, "desc": "Explosiones coléricas fásicas ante la exposición de debilidad."},
            {"id": "insula_r", "name": "Ínsula (Desconexión Vicaria)", "x": 3.9, "y": 0.8, "z": 0.2, "color": "#334155", "size": 0.4, "pulse_speed": 0.8, "desc": "Incapacidad para conmoverse ante el dolor ajeno provocado."}
        ],
        "tracts": [
            {"from": "dacc", "to": "vmpfc", "ctrl": [0.0, 3.6, 1.2], "type": "salience", "status": "hyperactive", "name": "Eje de Autoevaluación Hipervigilante"},
            {"from": "amg_r", "to": "dacc", "ctrl": [1.4, 0.8, 1.0], "type": "affective", "status": "hyperactive", "name": "Circuito de Ira Vindicativa"},
            {"from": "insula_r", "to": "vmpfc", "ctrl": [2.4, 2.6, -0.6], "type": "empathy", "status": "severed", "name": "Desconexión Fronto-Insular (Empatía Afectiva Deficitaria)"}
        ],
        "social_nodes": [
            {"name": "Vínculo de Pareja", "impact": "Cosificación, exigencia de pleitesía, humillación y castigo silencioso", "tension": 0.91, "coords": [7.0, 4.5, 2.0], "color": "#ef4444"},
            {"name": "Autoimagen / Cohesión del Self", "impact": "Fragilidad extrema; riesgo de colapso depresivo con ideación tanática", "tension": 0.95, "coords": [0.0, -7.5, -2.5], "color": "#a855f7"},
            {"name": "Ámbito Profesional / Jerárquico", "impact": "Rivalidades implacables, maltrato a subordinados y litigios de honor", "tension": 0.84, "coords": [-6.5, 5.0, 3.5], "color": "#fb923c"},
            {"name": "Núcleo Familiar de Origen", "impact": "Exigencia de alineamiento incondicional o ruptura definitiva", "tension": 0.78, "coords": [-5.5, -5.0, 3.0], "color": "#fb923c"},
            {"name": "Servicio de Salud Mental", "impact": "Abandono de tratamiento por resistencia a ser cuestionado", "tension": 0.50, "coords": [4.5, 6.5, -3.5], "color": "#38bdf8"}
        ]
    },
    "THP": {
        "title": "Trastorno Histriónico de la Personalidad",
        "subtitle": "Labilidad Afectiva, Hipersensibilidad al Refuerzo Social & Procesamiento Global",
        "fa_uncinate": 0.62,
        "amg_activity": 1.35,
        "vmpfc_control": 0.38,
        "acc_social_pain": 1.05,
        "pathology_code": "HISTRIONIC",
        "circuit_summary": "Amplificación de las señales socioemocionales inmediatas con un estilo cognitivo difuso. El estriado ventral y la amígdala responden con extrema labilidad al feedback ambiental, mientras que la falta de control analítico prefrontal favorece la dramatización y la somatización somatomorfa.",
        "nodes": [
            {"id": "amg_r", "name": "Amígdala Límbica", "x": 2.4, "y": -0.6, "z": -1.5, "color": "#06b6d4", "size": 0.9, "pulse_speed": 6.0, "desc": "Emotividad intensa, superficial y rápidamente intercambiable."},
            {"id": "accumbens", "name": "Núcleo Accumbens Social", "x": 1.4, "y": 1.6, "z": -0.9, "color": "#22d3ee", "size": 1.1, "pulse_speed": 6.8, "desc": "Búsqueda insaciable de validación externa, atención y halago."},
            {"id": "insula_r", "name": "Ínsula (Somatización)", "x": 3.9, "y": 0.8, "z": 0.2, "color": "#0891b2", "size": 0.85, "pulse_speed": 5.0, "desc": "Conversión corporal de afectos no metabolizados analíticamente."},
            {"id": "vmpfc", "name": "vmPFC Impresionista", "x": 0.0, "y": 4.8, "z": -0.8, "color": "#64748b", "size": 0.45, "pulse_speed": 1.5, "desc": "Déficit en el procesamiento reflexivo y secuencial."}
        ],
        "tracts": [
            {"from": "amg_r", "to": "accumbens", "ctrl": [1.9, 0.6, -1.1], "type": "reward", "status": "hyperactive", "name": "Eje Límbico-Recompensa Interpersonal"},
            {"from": "vmpfc", "to": "amg_r", "ctrl": [1.6, 2.2, -1.3], "type": "control", "status": "weakened", "name": "Modulación Frontal Deficitaria"}
        ],
        "social_nodes": [
            {"name": "Vínculo Conyugal / Pareja", "impact": "Seducción inadecuada, reclamo de protagonismo permanente y dramatismo", "tension": 0.86, "coords": [6.5, 4.0, 2.0], "color": "#ef4444"},
            {"name": "Servicio de Guardia / Emergencias", "impact": "Consultas por pseudocrisis neurológicas disociativas o conversivas", "tension": 0.80, "coords": [-5.5, 6.0, -3.0], "color": "#fb923c"},
            {"name": "Círculo Social Amplio", "impact": "Idealización precipitada de conocidos; relaciones intensas pero efímeras", "tension": 0.74, "coords": [5.0, -5.5, 3.0], "color": "#fb923c"},
            {"name": "Eje de Autoestima", "impact": "Autovaloración tributaria de la aprobación y el encanto externo", "tension": 0.82, "coords": [-2.0, -6.5, -2.5], "color": "#06b6d4"},
            {"name": "Ámbito de Trabajo Metódico", "impact": "Baja tolerancia al esfuerzo sostenido y al anonimato laboral", "tension": 0.54, "coords": [2.5, 7.0, -4.0], "color": "#38bdf8"}
        ]
    }
}

# --- Sidebar ---
st.sidebar.markdown("## 🧠 Consola de Neuroimagen")
selected_disorder_key = st.sidebar.selectbox(
    "Cuadro Nosológico:", 
    list(CLINICAL_DATABASE.keys()), 
    format_func=lambda k: CLINICAL_DATABASE[k]["title"]
)
stress_input = st.sidebar.slider("Carga de Estrés / Factor Desencadenante:", 0.0, 1.0, 0.5, 0.05)
view_depth = st.sidebar.select_slider(
    "Profundidad de Campo:",
    options=["1. Neuroanatomía Pial", "2. Tractografía Conectómica DTI", "3. Onda Expansiva Sistémica (Vidas)"],
    value="2. Tractografía Conectómica DTI"
)

profile = CLINICAL_DATABASE[selected_disorder_key]

# --- Cálculo de biomarcadores reactivos ---
calc_fa = max(0.04, profile["fa_uncinate"] * (1.0 - 0.45 * stress_input))
calc_amg = profile["amg_activity"] * (1.0 + 0.5 * stress_input)
calc_pfc = max(0.05, profile["vmpfc_control"] * (1.0 - 0.5 * stress_input))
ratio_index = calc_pfc / calc_amg

# --- Encabezado ---
st.title(profile["title"])
st.markdown(f"**Circuito:** `{profile['subtitle']}`")

h1, h2, h3, h4 = st.columns(4)
with h1:
    st.markdown(f"""<div class="hud-box"><div class="hud-sub">Integridad Fascículo Uncinado</div><div class="hud-metric">{calc_fa:.2f} FA</div></div>""", unsafe_allow_html=True)
with h2:
    st.markdown(f"""<div class="hud-box"><div class="hud-sub">Reactividad Amígdala (fMRI)</div><div class="hud-metric">{calc_amg:.2f} BOLD</div></div>""", unsafe_allow_html=True)
with h3:
    st.markdown(f"""<div class="hud-box"><div class="hud-sub">Control Prefrontal (vmPFC)</div><div class="hud-metric">{calc_pfc:.2f} z</div></div>""", unsafe_allow_html=True)
with h4:
    color_ratio = "#ef4444" if ratio_index < 0.35 else "#38bdf8"
    st.markdown(f"""<div class="hud-box"><div class="hud-sub">Ratio Control Top-Down</div><div class="hud-metric" style="color: {color_ratio};">{ratio_index:.2f}</div></div>""", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# Motor WebGL Three.js con Shaders, Malla Pial y Tractografía Multifilamento
# -------------------------------------------------------------------------
engine_payload = {
    "mode": view_depth,
    "stress": stress_input,
    "nodes": profile["nodes"],
    "tracts": profile["tracts"],
    "social": profile["social_nodes"],
    "fa": calc_fa
}

threejs_pipeline = f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body {{ margin: 0; overflow: hidden; background: #020617; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
    #viewport {{ width: 100vw; height: 100vh; position: relative; }}
    #hud-panel {{
      position: absolute; bottom: 24px; left: 24px; z-index: 100;
      background: rgba(11, 19, 41, 0.92); backdrop-filter: blur(14px);
      border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 12px;
      padding: 16px 22px; color: #f8fafc; max-width: 460px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.85);
    }}
    .hud-title {{ font-weight: 700; color: #38bdf8; font-size: 1.05rem; margin-bottom: 6px; }}
    .hud-body {{ color: #cbd5e1; font-size: 0.84rem; line-height: 1.45; }}
    #tools {{
      position: absolute; top: 20px; right: 24px; z-index: 100;
      background: rgba(11, 19, 41, 0.85); backdrop-filter: blur(10px);
      border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 10px;
      padding: 12px 18px; font-size: 0.78rem; color: #94a3b8;
    }}
    .tool-row {{ display: flex; align-items: center; margin-bottom: 5px; }}
    .tool-dot {{ width: 10px; height: 10px; border-radius: 50%; margin-right: 8px; }}
  </style>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
</head>
<body>
  <div id="viewport">
    <div id="hud-panel">
      <div id="hud-title" class="hud-title">Conectoma en Espacio MNI152</div>
      <div id="hud-body" class="hud-body">Haz clic o pasa el cursor sobre las regiones anatómicas o haces axonales para desplegar la semiología neurofuncional.</div>
    </div>
    <div id="tools">
      <div class="tool-row"><div class="tool-dot" style="background: #ef4444; box-shadow: 0 0 8px #ef4444;"></div> Hiperactividad / Ruptura de Tracto</div>
      <div class="tool-row"><div class="tool-dot" style="background: #38bdf8; box-shadow: 0 0 8px #38bdf8;"></div> Fascículo Preservado (FA normal)</div>
      <div class="tool-row"><div class="tool-dot" style="background: #eab308; box-shadow: 0 0 8px #eab308;"></div> Estriado Ventral / Recompensa</div>
      <div class="tool-row"><div class="tool-dot" style="background: #475569;"></div> Falla del Freno Top-Down</div>
    </div>
  </div>

  <script>
    const CONFIG = {json.dumps(engine_payload)};

    const container = document.getElementById('viewport');
    const scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x020617, 0.022);

    const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.set(0, 3, 22);

    const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true, powerPreference: "high-performance" }});
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    container.appendChild(renderer.domElement);

    const controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;
    controls.autoRotate = true;
    controls.autoRotateSpeed = 0.5;

    // Sistema de Luces Médicas
    scene.add(new THREE.AmbientLight(0xffffff, 0.9));
    const mainLight = new THREE.PointLight(0x38bdf8, 2.2, 60);
    mainLight.position.set(5, 12, 14);
    scene.add(mainLight);

    const subLight = new THREE.PointLight(0xa855f7, 2.0, 50);
    subLight.position.set(-10, -8, -10);
    scene.add(subLight);

    const targets = [];
    const pulsingElements = [];
    const streamlines = [];

    // -------------------------------------------------------------
    // GENERACIÓN ANATÓMICA DE ALTA FIDELIDAD (CÓRTEX PIAL)
    // -------------------------------------------------------------
    function buildAnatomicalCortex() {{
      const uSegs = 90, vSegs = 90;
      const geo = new THREE.BufferGeometry();
      const pos = [];

      for(let i=0; i<=uSegs; i++) {{
        let u = (i / uSegs) * Math.PI * 2;
        for(let j=0; j<=vSegs; j++) {{
          let v = (j / vSegs) * Math.PI;

          // Parámetros antropométricos encefálicos
          let rx = 4.4, ry = 5.9, rz = 4.1;

          // Armónicos esféricos calibrados para cisuras anatómicas (Silvio, Rolando, Parietooccipital)
          let sulci = 0.28 * Math.sin(8 * u) * Math.cos(7 * v) + 
                      0.18 * Math.sin(16 * v) * Math.cos(4 * u) +
                      0.09 * Math.sin(24 * u);

          let x = (rx + sulci) * Math.sin(v) * Math.cos(u);
          let y = (ry + sulci) * Math.sin(v) * Math.sin(u);
          let z = (rz + sulci) * Math.cos(v);

          // Cisura interhemisférica longitudinal profunda
          if (x >= 0) x += 0.52; else x -= 0.52;
          
          // Depresión anatómica temporal inferior
          if (y < 0 && z < 0) x *= 0.92;
          // Curvatura del polo frontal y occipital
          z -= 0.09 * (y * y) / ry;

          pos.push(x, y, z);
        }}
      }}
      geo.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
      geo.computeVertexNormals();

      const mat = new THREE.MeshPhysicalMaterial({{
        color: 0x1e293b,
        emissive: 0x0f172a,
        roughness: 0.25,
        metalness: 0.1,
        transparent: true,
        opacity: CONFIG.mode.includes("1.") ? 0.35 : 0.15,
        wireframe: true,
        depthWrite: false
      }});
      return new THREE.Mesh(geo, mat);
    }}

    const cortex = buildAnatomicalCortex();
    scene.add(cortex);

    // -------------------------------------------------------------
    // NODOS SUBCORTICALES Y NÚCLEOS VOLUMÉTRICOS
    // -------------------------------------------------------------
    const nodeCoords = {{}};
    CONFIG.nodes.forEach(n => {{
      const geo = new THREE.SphereGeometry(n.size, 32, 32);
      const mat = new THREE.MeshStandardMaterial({{
        color: n.color,
        emissive: n.color,
        emissiveIntensity: 1.5,
        roughness: 0.3,
        metalness: 0.7
      }});
      const mesh = new THREE.Mesh(geo, mat);
      mesh.position.set(n.x, n.y, n.z);
      mesh.userData = {{ name: n.name, desc: n.desc, pulse: n.pulse_speed, baseSize: n.size }};
      scene.add(mesh);
      targets.push(mesh);
      pulsingElements.push(mesh);
      nodeCoords[n.id] = mesh.position;

      // Halo de difusión funcional
      const auraGeo = new THREE.SphereGeometry(n.size * 1.5, 16, 16);
      const auraMat = new THREE.MeshBasicMaterial({{
        color: n.color,
        transparent: true,
        opacity: 0.25,
        wireframe: true
      }});
      const aura = new THREE.Mesh(auraGeo, auraMat);
      aura.position.copy(mesh.position);
      scene.add(aura);
    }});

    // -------------------------------------------------------------
    // TRACTOGRAFÍA DTI STREAMLINES (HACES MULTIFILAMENTO)
    // -------------------------------------------------------------
    if (!CONFIG.mode.includes("3.")) {{
      CONFIG.tracts.forEach(t => {{
        if (nodeCoords[t.from] && nodeCoords[t.to]) {{
          const p0 = nodeCoords[t.from];
          const p1 = nodeCoords[t.to];
          const ctrl = new THREE.Vector3(...t.ctrl);
          const curve = new THREE.QuadraticBezierCurve3(p0, ctrl, p1);

          const isFrayed = t.status === "frayed" || t.status === "severed";
          const fiberCount = isFrayed ? 4 : 9; // El tracto patológico pierde densidad axonal

          for(let f = 0; f < fiberCount; f++) {{
            // Desplazamiento aleatorio para recrear el grosor real del haz axonal
            const offset = new THREE.Vector3(
              (Math.random() - 0.5) * (isFrayed ? 0.35 : 0.18),
              (Math.random() - 0.5) * (isFrayed ? 0.35 : 0.18),
              (Math.random() - 0.5) * (isFrayed ? 0.35 : 0.18)
            );
            const fiberCurve = new THREE.QuadraticBezierCurve3(
              p0.clone().add(offset),
              ctrl.clone().add(offset),
              p1.clone().add(offset)
            );

            let tubeColor = 0x38bdf8;
            if (t.status === "frayed" || t.status === "severed") tubeColor = 0xef4444;
            if (t.status === "hyperactive") tubeColor = 0xf43f5e;

            const tubeGeo = new THREE.TubeGeometry(fiberCurve, 28, isFrayed ? 0.025 : 0.05, 8, false);
            const tubeMat = new THREE.MeshStandardMaterial({{
              color: tubeColor,
              emissive: tubeColor,
              emissiveIntensity: isFrayed ? 0.6 : 1.2,
              transparent: true,
              opacity: isFrayed ? 0.5 : 0.85
            }});
            const fiberMesh = new THREE.Mesh(tubeGeo, tubeMat);
            fiberMesh.userData = {{ name: t.name, desc: "Tractografía por Tensor de Difusión (DTI). Grosor e integridad axonal estricta." }};
            scene.add(fiberMesh);
            targets.push(fiberMesh);

            // Transmisión de impulsos sinápticos dinámicos (Partículas BOLD)
            if (t.status !== "severed") {{
              const pCount = 8;
              const pGeo = new THREE.BufferGeometry();
              const pPos = new Float32Array(pCount * 3);
              for(let k=0; k<pCount; k++) {{
                const p = fiberCurve.getPoint(k / pCount);
                pPos[k*3] = p.x; pPos[k*3+1] = p.y; pPos[k*3+2] = p.z;
              }}
              pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
              const pMat = new THREE.PointsMaterial({{ color: tubeColor, size: 0.14, transparent: true, opacity: 0.9 }});
              const pulsePoints = new THREE.Points(pGeo, pMat);
              scene.add(pulsePoints);
              streamlines.push({{ points: pulsePoints, curve: fiberCurve, speed: t.status === "hyperactive" ? 0.8 : 0.3 }});
            }}
          }}
        }}
      }});
    }}

    // -------------------------------------------------------------
    // RED SISTÉMICA / ONDA EXPANSIVA (VIDAS AFECTADAS)
    // -------------------------------------------------------------
    if (CONFIG.mode.includes("3.")) {{
      cortex.material.opacity = 0.06;

      CONFIG.social.forEach(s => {{
        const sGeo = new THREE.SphereGeometry(1.2 + s.tension * 0.5, 32, 32);
        const sMat = new THREE.MeshStandardMaterial({{
          color: s.color,
          emissive: s.color,
          emissiveIntensity: s.tension * 2.0,
          roughness: 0.3
        }});
        const sMesh = new THREE.Mesh(sGeo, sMat);
        sMesh.position.set(...s.coords);
        sMesh.userData = {{ name: s.name, desc: s.impact + " | Tensión de Ruptura: " + (s.tension * 100).toFixed(0) + "%" }};
        scene.add(sMesh);
        targets.push(sMesh);

        // Tensor elástico central al paciente
        const lPoints = [new THREE.Vector3(0, 0, 0), new THREE.Vector3(...s.coords)];
        const lGeo = new THREE.BufferGeometry().setFromPoints(lPoints);
        const lMat = new THREE.LineBasicMaterial({{
          color: s.tension > 0.88 ? 0xef4444 : 0x38bdf8,
          linewidth: 4,
          transparent: true,
          opacity: 0.8
        }});
        scene.add(new THREE.Line(lGeo, lMat));
      }});
    }}

    // Raycaster para despliegue de información inmediata
    const raycaster = new THREE.Raycaster();
    const mouse = new THREE.Vector2();
    const titleEl = document.getElementById('hud-title');
    const descEl = document.getElementById('hud-body');

    window.addEventListener('pointermove', (e) => {{
      const rect = renderer.domElement.getBoundingClientRect();
      mouse.x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
      mouse.y = -((e.clientY - rect.top) / rect.height) * 2 + 1;

      raycaster.setFromCamera(mouse, camera);
      const hits = raycaster.intersectObjects(targets);

      if (hits.length > 0) {{
        const obj = hits[0].object;
        if (obj.userData && obj.userData.name) {{
          titleEl.innerText = obj.userData.name;
          descEl.innerText = obj.userData.desc;
          titleEl.style.color = "#38bdf8";
        }}
      }}
    }});

    // Loop de renderizado continuo a 60 FPS
    const clock = new THREE.Clock();
    function render() {{
      requestAnimationFrame(render);
      const t = clock.getElapsedTime();

      // Pulsación biológica fásica
      pulsingElements.forEach(mesh => {{
        const freq = mesh.userData.pulse || 2.0;
        const scale = 1.0 + Math.sin(t * freq) * 0.12;
        mesh.scale.set(scale, scale, scale);
      }});

      // Movimiento continuo de partículas sobre los tractos de axones
      streamlines.forEach(sl => {{
        const positions = sl.points.geometry.attributes.position.array;
        const count = positions.length / 3;
        for(let i=0; i<count; i++) {{
          let progress = ((t * sl.speed) + (i / count)) % 1.0;
          let pt = sl.curve.getPoint(progress);
          positions[i*3] = pt.x;
          positions[i*3+1] = pt.y;
          positions[i*3+2] = pt.z;
        }}
        sl.points.geometry.attributes.position.needsUpdate = true;
      }});

      controls.update();
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

components.html(threejs_pipeline, height=660, scrolling=False)

# -------------------------------------------------------------------------
# Marco Teórico de Respaldo Académico para el Ateneo
# -------------------------------------------------------------------------
st.markdown("---")
col_l, col_r = st.columns([1.2, 1.0])

with col_l:
    st.markdown("### 🔬 Mecanismo Fisiopatológico y Sustrato Conectómico")
    st.info(profile["circuit_summary"])
    st.markdown("""
    * **Fascículo Uncinado (*Uncinate Fasciculus*):** Vía de sustancia blanca de maduración tardía que conecta el sistema límbico anterior con el polo frontal y la corteza orbitofrontal. Su baja anisotropía fraccional (FA) documentada en DTI explica la persistencia de respuestas emocionales arcaicas no moduladas por la lógica o las consecuencias futuras.
    * **Red de Prominencia (*Salience Network*):** La coactivación de la ínsula anterior y el dACC detecta de manera distorsionada los estímulos interpersonales, interpretando la neutralidad como rechazo inminente (TLP) o como desafío de jerarquía (TNP).
    """)

with col_r:
    st.markdown("### 🌐 El Fenómeno de Onda Expansiva (Vidas Afectadas)")
    st.warning("""
    A diferencia de la patología neurótica convencional, donde el sufrimiento suele quedar encapsulado en el mundo interno del paciente (Cluster C), en el **Cluster B** la falla del freno inhibitorio biológico se traslada de forma directa al tejido social:
    * **Desestructuración conyugal y familiar:** Ciclos de idealización y hostilidad.
    * **Impacto institucional sanitario:** Hiperutilización de guardias por conductas impulsivas y parasuicidas.
    * **Fuero jurídico/penal:** Litigios, denuncias y transgresión sistemática de normativas en casos con componente antisocial o narcisista grave.
    """)
