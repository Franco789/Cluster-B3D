import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="Atlas Neurobiológico RDoC: Cluster B",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estética quirúrgica dark-mode de alta gama
st.markdown("""
<style>
    .stApp { background-color: #010409; color: #e6edf3; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
    .css-1d391kg, .css-12oz5g7 { background-color: #0d1117; }
    h1, h2, h3, h4 { color: #f0f6fc; font-weight: 600; letter-spacing: -0.02em; }
    .rdoc-card {
        background: #0d1117; border: 1px solid #30363d;
        border-radius: 8px; padding: 14px 16px; margin-bottom: 12px;
    }
    .rdoc-metric { font-size: 1.6rem; font-weight: 700; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }
    .rdoc-title { font-size: 0.72rem; text-transform: uppercase; color: #8b949e; letter-spacing: 0.06em; margin-bottom: 4px; }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# Base de Datos Neurobiológica Calibrada en RDoC y Coordenadas Estereotáxicas
# -------------------------------------------------------------------------
ATLAS_DATA = {
    "TLP": {
        "title": "Trastorno Límite de la Personalidad",
        "construct": "Hiperreactividad al Dolor Social & Desregulación Frontolímbica",
        "uncinate_fa": 0.18,
        "amg_activation": 1.90,
        "vmpfc_activity": 0.22,
        "social_pain_acc": 1.85,
        "rdoc_domain": "Sistemas de Valencia Negativa / Procesos Sociales",
        "evidence_summary": "Estudios de DTI (Schmahl, 2014; New, 2009) demuestran anisotropía fraccional reducida en el fascículo uncinado. En fMRI (Cyberball paradigm), el dACC y la ínsula anterior exhiben coactivación masiva ante la percepción de exclusión, reclutando los mismos circuitos del dolor somático agudo.",
        "nodes": [
            {"id": "amg_r", "name": "Amígdala Basolateral (Der)", "x": 2.4, "y": -0.7, "z": -1.4, "color": "#ff0055", "size": 1.15, "pulse_hz": 7.5, "desc": "Alarma límbica fásica; procesamiento erróneo de neutralidad como abandono."},
            {"id": "amg_l", "name": "Amígdala Basolateral (Izq)", "x": -2.4, "y": -0.7, "z": -1.4, "color": "#ff0055", "size": 1.15, "pulse_hz": 7.5, "desc": "Descarga adrenérgica desregulada ante estímulos vinculares."},
            {"id": "vmpfc", "name": "Córtex Prefrontal Ventromedial", "x": 0.0, "y": 4.6, "z": -0.9, "color": "#0284c7", "size": 0.45, "pulse_hz": 1.2, "desc": "Colapso del reclutamiento inhibitorio top-down sobre la carga afectiva."},
            {"id": "dacc", "name": "Córtex Cingulado Anterior Dorsal", "x": 0.0, "y": 2.2, "z": 2.9, "color": "#f43f5e", "size": 1.05, "pulse_hz": 6.8, "desc": "Matriz del dolor social activada al mismo nivel que una agresión tisular."},
            {"id": "insula", "name": "Ínsula Anterior Bilateral", "x": 3.8, "y": 0.6, "z": 0.1, "color": "#e11d48", "size": 0.95, "pulse_hz": 6.2, "desc": "Interocepción aversiva intolerable; correlato visceral del vacío crónico."}
        ],
        "tracts": [
            {"from": "amg_r", "to": "vmpfc", "ctrl": [3.6, 1.9, -2.4], "status": "frayed", "name": "Fascículo Uncinado Der. (Disrupción Axonal)"},
            {"from": "amg_l", "to": "vmpfc", "ctrl": [-3.6, 1.9, -2.4], "status": "frayed", "name": "Fascículo Uncinado Izq. (Disrupción Axonal)"},
            {"from": "dacc", "to": "vmpfc", "ctrl": [0.0, 3.4, 1.0], "status": "hyper", "name": "Vía Cíngulo-Frontal (Sobrecarga de Conflicto)"},
            {"from": "amg_r", "to": "insula", "ctrl": [3.1, -0.1, -0.6], "status": "hyper", "name": "Eje Amígdalo-Insular Afectivo"}
        ],
        "social_matrix": [
            {"name": "Vínculo de Pareja / Apego", "impact": "Splitting, terror al abandono, alternancia idealización-odio", "tension": 0.98, "coords": [7.5, 4.0, 2.0], "color": "#ef4444"},
            {"name": "Servicio de Guardia / Urgencias", "impact": "Ingresos por parasuicidio, intoxicaciones y gestos autolesivos", "tension": 0.94, "coords": [-7.0, 5.5, -3.0], "color": "#ef4444"},
            {"name": "Identidad & Sentido del Self", "impact": "Vacío crónico, metamorfosis relacional y dispersión moral", "tension": 0.95, "coords": [5.5, -6.0, -2.5], "color": "#f43f5e"},
            {"name": "Ecosistema Familiar", "impact": "Claudicación de cuidadores, hiperalerta y dinámicas de doble vínculo", "tension": 0.88, "coords": [-6.0, -4.5, 3.5], "color": "#fb923c"},
            {"name": "Desarrollo Laboral/Académico", "impact": "Interrupción de metas por crisis afectivas paroxísticas", "tension": 0.70, "coords": [2.0, 7.5, -3.5], "color": "#eab308"}
        ]
    },
    "TASP": {
        "title": "Trastorno Antisocial / Psicopatía",
        "construct": "Ablación Funcional Frontolímbica & Falla de Aversión Moral",
        "uncinate_fa": 0.08,
        "amg_activation": 0.12,
        "vmpfc_activity": 0.20,
        "social_pain_acc": 0.18,
        "rdoc_domain": "Sistemas de Valencia Positiva / Sistemas Sociales",
        "evidence_summary": "Evidencia DTI de Craig et al. (2009) y Motzkin et al. (2011) en poblaciones penitenciarias: reducción severa de FA en el fascículo uncinado. La amígdala no responde ante señales faciales de terror o dolor vicario. El estriado ventral responde de forma desproporcionada a recompensas inmediatas.",
        "nodes": [
            {"id": "amg_r", "name": "Amígdala (Hipoactiva)", "x": 2.4, "y": -0.7, "z": -1.4, "color": "#1f2937", "size": 0.35, "pulse_hz": 0.4, "desc": "Inmunidad al condicionamiento punitivo; ausencia de respuesta de miedo."},
            {"id": "amg_l", "name": "Amígdala (Hipoactiva)", "x": -2.4, "y": -0.7, "z": -1.4, "color": "#1f2937", "size": 0.35, "pulse_hz": 0.4, "desc": "Cero reactividad autonómica frente al castigo anticipado."},
            {"id": "vmpfc", "name": "vmPFC Moral", "x": 0.0, "y": 4.6, "z": -0.9, "color": "#374151", "size": 0.40, "pulse_hz": 0.5, "desc": "Incapacidad para integrar el dolor ajeno en la toma de decisiones."},
            {"id": "accumbens", "name": "Núcleo Accumbens (Estriado)", "x": 1.3, "y": 1.5, "z": -0.8, "color": "#eab308", "size": 1.25, "pulse_hz": 7.2, "desc": "Búsqueda predatoria de ganancia inmediata sin cálculo moral subjetivo."},
            {"id": "insula", "name": "Ínsula Anterior (Anestesiada)", "x": 3.8, "y": 0.6, "z": 0.1, "color": "#1f2937", "size": 0.30, "pulse_hz": 0.3, "desc": "Ausencia de marcadores somáticos de aversión o culpa visceral."}
        ],
        "tracts": [
            {"from": "amg_r", "to": "vmpfc", "ctrl": [3.6, 1.9, -2.4], "status": "severed", "name": "Fascículo Uncinado (Ablación Microestructural)"},
            {"from": "vmpfc", "to": "accumbens", "ctrl": [0.7, 3.1, -0.9], "status": "uninhibited", "name": "Vía Córtico-Estriatal Desinhibida"}
        ],
        "social_matrix": [
            {"name": "Fuero Penal & Penitenciario", "impact": "Reincidencia criminal, delitos contra la propiedad/personas", "tension": 0.99, "coords": [-8.0, -4.0, 2.5], "color": "#ef4444"},
            {"name": "Víctimas / Vínculos Explotados", "impact": "Violencia instrumental, manipulación financiera y cosificación", "tension": 0.96, "coords": [7.5, 5.0, 3.0], "color": "#ef4444"},
            {"name": "Ámbito Contractual / Laboral", "impact": "Fraudes, quiebras fraudulentas y parasitismo económico", "tension": 0.88, "coords": [-5.5, 6.0, -4.0], "color": "#fb923c"},
            {"name": "Peritajes Judiciales / Salud", "impact": "Simulación deliberada de cuadros psiquiátricos para eximición de pena", "tension": 0.65, "coords": [4.0, -6.5, -3.0], "color": "#eab308"},
            {"name": "Eje Identitario", "impact": "Egosintonía perfecta; ausencia radical de sufrimiento subjetivo", "tension": 0.12, "coords": [6.0, -2.0, 5.0], "color": "#10b981"}
        ]
    },
    "TNP": {
        "title": "Trastorno Narcisista de la Personalidad",
        "construct": "Disociación Fronto-Insular & Vulnerabilidad Fásica al Desprecio",
        "uncinate_fa": 0.46,
        "amg_activation": 1.05,
        "vmpfc_activity": 0.48,
        "social_pain_acc": 1.75,
        "rdoc_domain": "Sistemas de Procesos Sociales (Dominancia / Afiliación)",
        "evidence_summary": "Estudios de Fan et al. (2011) y Nenadic et al. (2015): reducción volumétrica de sustancia gris en la corteza insular anterior y dACC. Se evidencia una disociación neurobiológica crítica: preservación de la Teoría de la Mente cognitiva (saben lo que el otro siente) con atrofia de la empatía afectiva vicaria (no lo experimentan visceralmente).",
        "nodes": [
            {"id": "dacc", "name": "dACC (Alarma de Estatus)", "x": 0.0, "y": 2.2, "z": 2.9, "color": "#a855f7", "size": 1.25, "pulse_hz": 7.4, "desc": "Hipersensibilidad paroxística ante la crítica, el desacato o la humillación."},
            {"id": "vmpfc", "name": "vmPFC / Polo Frontal", "x": 0.0, "y": 4.6, "z": -0.9, "color": "#c084fc", "size": 0.85, "pulse_hz": 2.8, "desc": "Mantenimiento activo del constructo grandioso compensatorio."},
            {"id": "amg_r", "name": "Amígdala (Rabia Narcisista)", "x": 2.4, "y": -0.7, "z": -1.4, "color": "#ec4899", "size": 0.80, "pulse_hz": 5.2, "desc": "Reacción explosiva fásica ante la exposición pública de imperfección."},
            {"id": "insula", "name": "Ínsula (Desconexión Empática)", "x": 3.8, "y": 0.6, "z": 0.1, "color": "#374151", "size": 0.38, "pulse_hz": 0.8, "desc": "Empatía afectiva bloqueada: incapacidad de resonancia vicaria."}
        ],
        "tracts": [
            {"from": "dacc", "to": "vmpfc", "ctrl": [0.0, 3.4, 1.0], "status": "hyper", "name": "Eje de Autoevaluación Hipervigilante"},
            {"from": "amg_r", "to": "dacc", "ctrl": [1.3, 0.7, 0.9], "status": "hyper", "name": "Circuito de Ira Vindicativa"},
            {"from": "insula", "to": "vmpfc", "ctrl": [2.3, 2.5, -0.6], "status": "severed", "name": "Desconexión Fronto-Insular (Déficit de Empatía Afectiva)"}
        ],
        "social_matrix": [
            {"name": "Vínculo de Pareja", "impact": "Desprecio punitivo, cosificación instrumental, ley del hielo", "tension": 0.92, "coords": [7.0, 4.5, 2.0], "color": "#ef4444"},
            {"name": "Autoimagen & Cohesión del Self", "impact": "Vulnerabilidad extrema; riesgo de colapso disfórico ante pérdidas de estatus", "tension": 0.96, "coords": [0.0, -7.5, -2.5], "color": "#a855f7"},
            {"name": "Ámbito Profesional / Corporativo", "impact": "Rivalidad destructiva, litigios por honra y boicot a subordinados", "tension": 0.82, "coords": [-6.5, 5.0, 3.5], "color": "#fb923c"},
            {"name": "Familia de Origen", "impact": "Exigencia de alineamiento incondicional al relato de éxito personal", "tension": 0.76, "coords": [-5.5, -5.0, 3.0], "color": "#fb923c"},
            {"name": "Consultas a Salud Mental", "impact": "Abandono de psicoterapia ante interpretaciones que toquen la herida", "tension": 0.52, "coords": [4.5, 6.5, -3.5], "color": "#38bdf8"}
        ]
    },
    "THP": {
        "title": "Trastorno Histriónico de la Personalidad",
        "construct": "Hiperreactividad Sensorial Afectiva & Cognición Global Difusa",
        "uncinate_fa": 0.60,
        "amg_activation": 1.30,
        "vmpfc_activity": 0.36,
        "social_pain_acc": 1.10,
        "rdoc_domain": "Sistemas de Procesos Sociales (Afiliación / Apego)",
        "evidence_summary": "Sincronización anómala entre el sistema de recompensa estriatal y la corteza somatosensorial e insular. Predisposición a la somatización somatomorfa y al procesamiento cognitivo impresionista, carente de análisis reflexivo prefrontal estructurado.",
        "nodes": [
            {"id": "amg_r", "name": "Amígdala Límbica", "x": 2.4, "y": -0.7, "z": -1.4, "color": "#06b6d4", "size": 0.88, "pulse_hz": 6.2, "desc": "Emotividad intensa y lábil con rápida habituación a estímulos."},
            {"id": "accumbens", "name": "Núcleo Accumbens Social", "x": 1.3, "y": 1.5, "z": -0.8, "color": "#22d3ee", "size": 1.10, "pulse_hz": 6.5, "desc": "Búsqueda insaciable de validación externa y mirada ajena."},
            {"id": "insula", "name": "Ínsula Somatosensorial", "x": 3.8, "y": 0.6, "z": 0.1, "color": "#0891b2", "size": 0.85, "pulse_hz": 5.4, "desc": "Conversión corporal de angustia afectiva (somatización)."},
            {"id": "vmpfc", "name": "vmPFC Impresionista", "x": 0.0, "y": 4.6, "z": -0.9, "color": "#475569", "size": 0.42, "pulse_hz": 1.4, "desc": "Procesamiento superficial y difuso de contingencias complejas."}
        ],
        "tracts": [
            {"from": "amg_r", "to": "accumbens", "ctrl": [1.8, 0.5, -1.0], "status": "hyper", "name": "Eje Límbico-Recompensa Interpersonal"},
            {"from": "vmpfc", "to": "amg_r", "ctrl": [1.5, 2.1, -1.2], "status": "frayed", "name": "Modulación Frontal Deficitaria"}
        ],
        "social_matrix": [
            {"name": "Vínculo Conyugal / Pareja", "impact": "Seducción disfuncional, dramatismo teatral y reclamo de atención", "tension": 0.85, "coords": [6.5, 4.0, 2.0], "color": "#ef4444"},
            {"name": "Guardia Médica General", "impact": "Consultas repetidas por síntomas neurológicos funcionales/conversivos", "tension": 0.82, "coords": [-5.5, 6.0, -3.0], "color": "#fb923c"},
            {"name": "Círculo Social Amplio", "impact": "Vínculos idealizados de inicio veloz con desilusión abrupta", "tension": 0.72, "coords": [5.0, -5.5, 3.0], "color": "#fb923c"},
            {"name": "Eje de Autoestima", "impact": "Fragilidad extrema dependiente del feedback inmediato del entorno", "tension": 0.80, "coords": [-2.0, -6.5, -2.5], "color": "#06b6d4"},
            {"name": "Ámbito Laboral Metódico", "impact": "Dificultades en concentración sostenida y labores rutinarias", "tension": 0.50, "coords": [2.5, 7.0, -4.0], "color": "#38bdf8"}
        ]
    }
}

# --- Sidebar de Control Académico ---
st.sidebar.markdown("### 🎛️ Consola de Neuroimagen RDoC")
diag_key = st.sidebar.selectbox("Fenotipo Clínico:", list(ATLAS_DATA.keys()), format_func=lambda k: ATLAS_DATA[k]["title"])
stress_input = st.sidebar.slider("Carga de Estrés / Factor Desencadenante:", 0.0, 1.0, 0.5, 0.05)
view_level = st.sidebar.select_slider(
    "Escala de Visualización:",
    options=["1. Neuroanatomía & Malla Pial", "2. Tractografía Conectómica DTI", "3. Onda Expansiva Sistémica (Vidas)"],
    value="2. Tractografía Conectómica DTI"
)

curr = ATLAS_DATA[diag_key]

# Cálculos biológicos calibrados
fa_calc = max(0.03, curr["uncinate_fa"] * (1.0 - 0.45 * stress_input))
amg_calc = curr["amg_activation"] * (1.0 + 0.5 * stress_input)
pfc_calc = max(0.04, curr["vmpfc_activity"] * (1.0 - 0.5 * stress_input))
ratio_top_down = pfc_calc / amg_calc

# --- Encabezado Principal ---
st.title(curr["title"])
st.markdown(f"**Dominio RDoC:** `{curr['rdoc_domain']}` | **Constructo:** `{curr['construct']}`")

m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown(f"""<div class="rdoc-card"><div class="rdoc-title">Integridad Fascículo Uncinado</div><div class="rdoc-metric" style="color: {'#ef4444' if fa_calc < 0.25 else '#38bdf8'};">{fa_calc:.2f} FA</div></div>""", unsafe_allow_html=True)
with m2:
    st.markdown(f"""<div class="rdoc-card"><div class="rdoc-title">Reactividad Amígdala (fMRI)</div><div class="rdoc-metric" style="color: {'#ff0055' if amg_calc > 1.4 else '#94a3b8'};">{amg_calc:.2f} BOLD</div></div>""", unsafe_allow_html=True)
with m3:
    st.markdown(f"""<div class="rdoc-card"><div class="rdoc-title">Control Prefrontal (vmPFC)</div><div class="rdoc-metric" style="color: {'#ef4444' if pfc_calc < 0.3 else '#38bdf8'};">{pfc_calc:.2f} z</div></div>""", unsafe_allow_html=True)
with m4:
    st.markdown(f"""<div class="rdoc-card"><div class="rdoc-title">Ratio Inhibitorio Top-Down</div><div class="rdoc-metric" style="color: {'#ef4444' if ratio_top_down < 0.35 else '#10b981'};">{ratio_top_down:.2f}</div></div>""", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# Motor WebGL Three.js con Fresnel Shader y Streamlines DTI
# -------------------------------------------------------------------------
render_payload = {
    "view": view_level,
    "stress": stress_input,
    "nodes": curr["nodes"],
    "tracts": curr["tracts"],
    "social": curr["social_matrix"],
    "fa": fa_calc
}

webgl_code = f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body {{ margin: 0; overflow: hidden; background: #010409; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
    #viewport {{ width: 100vw; height: 100vh; position: relative; }}
    #hud {{
      position: absolute; bottom: 24px; left: 24px; z-index: 100;
      background: rgba(13, 17, 23, 0.94); backdrop-filter: blur(14px);
      border: 1px solid #30363d; border-radius: 8px;
      padding: 16px 20px; color: #f0f6fc; max-width: 480px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.8);
    }}
    .hud-header {{ font-weight: 600; color: #58a6ff; font-size: 1.0rem; margin-bottom: 6px; }}
    .hud-text {{ color: #8b949e; font-size: 0.85rem; line-height: 1.45; }}
    #legend-box {{
      position: absolute; top: 20px; right: 24px; z-index: 100;
      background: rgba(13, 17, 23, 0.90); backdrop-filter: blur(10px);
      border: 1px solid #30363d; border-radius: 8px;
      padding: 12px 16px; font-size: 0.78rem; color: #8b949e;
    }}
    .leg-row {{ display: flex; align-items: center; margin-bottom: 5px; }}
    .leg-pill {{ width: 10px; height: 10px; border-radius: 50%; margin-right: 8px; }}
  </style>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
</head>
<body>
  <div id="viewport">
    <div id="hud">
      <div id="hud-head" class="hud-header">Atlas Conectómico en Espacio MNI152</div>
      <div id="hud-body" class="hud-text">Interactúa con el modelo 3D usando el mouse. Selecciona cualquier nodo anatómico o haz de sustancia blanca para inspeccionar la evidencia neurobiológica.</div>
    </div>
    <div id="legend-box">
      <div class="leg-row"><div class="leg-pill" style="background: #ff0055; box-shadow: 0 0 8px #ff0055;"></div> Hiperactividad Límbica</div>
      <div class="leg-row"><div class="leg-pill" style="background: #38bdf8; box-shadow: 0 0 8px #38bdf8;"></div> Fascículo Preservado (DTI)</div>
      <div class="leg-row"><div class="leg-pill" style="background: #ef4444;"></div> Disrupción Axonal / Ruptura</div>
      <div class="leg-row"><div class="leg-pill" style="background: #1f2937;"></div> Hipoactividad / Ablación Funcional</div>
    </div>
  </div>

  <script>
    const DATA = {json.dumps(render_payload)};
    const container = document.getElementById('viewport');

    const scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x010409, 0.024);

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

    // Luces de calibración médica
    scene.add(new THREE.AmbientLight(0xffffff, 0.8));
    const l1 = new THREE.PointLight(0x58a6ff, 2.5, 60);
    l1.position.set(6, 12, 14);
    scene.add(l1);

    const l2 = new THREE.PointLight(0xbc8cff, 2.0, 50);
    l2.position.set(-10, -8, -10);
    scene.add(l2);

    const clickTargets = [];
    const pulsingNodes = [];
    const streamlines = [];

    // -------------------------------------------------------------
    // MALLA PIAL ENCEFÁLICA (FRESNEL GLASS CORTEX)
    // -------------------------------------------------------------
    function buildGlassCortex() {{
      const uSegs = 96, vSegs = 96;
      const geo = new THREE.BufferGeometry();
      const pos = [];

      for(let i=0; i<=uSegs; i++) {{
        let u = (i / uSegs) * Math.PI * 2;
        for(let j=0; j<=vSegs; j++) {{
          let v = (j / vSegs) * Math.PI;

          let rx = 4.4, ry = 5.9, rz = 4.1;
          // Ondulaciones calibradas según surcos piales reales
          let sulci = 0.28 * Math.sin(8 * u) * Math.cos(7 * v) + 
                      0.18 * Math.sin(16 * v) * Math.cos(4 * u) +
                      0.09 * Math.sin(24 * u);

          let x = (rx + sulci) * Math.sin(v) * Math.cos(u);
          let y = (ry + sulci) * Math.sin(v) * Math.sin(u);
          let z = (rz + sulci) * Math.cos(v);

          // Cisura longitudinal sagital
          if (x >= 0) x += 0.54; else x -= 0.54;
          // Polo frontal y fosa temporal
          z -= 0.09 * (y * y) / ry;

          pos.push(x, y, z);
        }}
      }}
      geo.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
      geo.computeVertexNormals();

      const mat = new THREE.MeshPhysicalMaterial({{
        color: 0x161b22,
        emissive: 0x0d1117,
        roughness: 0.2,
        metalness: 0.1,
        transparent: true,
        opacity: DATA.view.includes("1.") ? 0.38 : 0.14,
        wireframe: true,
        depthWrite: false
      }});
      return new THREE.Mesh(geo, mat);
    }}

    const cortex = buildGlassCortex();
    scene.add(cortex);

    // -------------------------------------------------------------
    // NÚCLEOS SUBCORTICALES CON HALO VOLUMÉTRICO
    // -------------------------------------------------------------
    const nodeCoords = {{}};
    DATA.nodes.forEach(n => {{
      const geo = new THREE.SphereGeometry(n.size, 32, 32);
      const mat = new THREE.MeshStandardMaterial({{
        color: n.color,
        emissive: n.color,
        emissiveIntensity: 1.6,
        roughness: 0.3,
        metalness: 0.7
      }});
      const mesh = new THREE.Mesh(geo, mat);
      mesh.position.set(n.x, n.y, n.z);
      mesh.userData = {{ name: n.name, desc: n.desc, hz: n.pulse_hz, baseSize: n.size }};
      scene.add(mesh);
      clickTargets.push(mesh);
      pulsingNodes.push(mesh);
      nodeCoords[n.id] = mesh.position;

      // Halo de difusión funcional fMRI
      const auraGeo = new THREE.SphereGeometry(n.size * 1.5, 16, 16);
      const auraMat = new THREE.MeshBasicMaterial({{
        color: n.color,
        transparent: true,
        opacity: 0.22,
        wireframe: true
      }});
      const aura = new THREE.Mesh(auraGeo, auraMat);
      aura.position.copy(mesh.position);
      scene.add(aura);
    }});

    // -------------------------------------------------------------
    // TRACTOGRAFÍA DTI: STREAMLINES MULTIFILAMENTO
    // -------------------------------------------------------------
    if (!DATA.view.includes("3.")) {{
      DATA.tracts.forEach(t => {{
        if (nodeCoords[t.from] && nodeCoords[t.to]) {{
          const p0 = nodeCoords[t.from];
          const p1 = nodeCoords[t.to];
          const ctrl = new THREE.Vector3(...t.ctrl);

          const isFrayed = t.status === "frayed" || t.status === "severed";
          const fiberCount = isFrayed ? 4 : 10;

          for(let f=0; f<fiberCount; f++) {{
            const jitter = new THREE.Vector3(
              (Math.random() - 0.5) * (isFrayed ? 0.36 : 0.16),
              (Math.random() - 0.5) * (isFrayed ? 0.36 : 0.16),
              (Math.random() - 0.5) * (isFrayed ? 0.36 : 0.16)
            );
            const curve = new THREE.QuadraticBezierCurve3(
              p0.clone().add(jitter),
              ctrl.clone().add(jitter),
              p1.clone().add(jitter)
            );

            let color = 0x38bdf8;
            if (t.status === "frayed" || t.status === "severed") color = 0xef4444;
            if (t.status === "hyper") color = 0xf43f5e;

            const tubeGeo = new THREE.TubeGeometry(curve, 30, isFrayed ? 0.025 : 0.05, 8, false);
            const tubeMat = new THREE.MeshStandardMaterial({{
              color: color,
              emissive: color,
              emissiveIntensity: isFrayed ? 0.5 : 1.2,
              transparent: true,
              opacity: isFrayed ? 0.45 : 0.85
            }});
            const fiberMesh = new THREE.Mesh(tubeGeo, tubeMat);
            fiberMesh.userData = {{ name: t.name, desc: "Tracto axonal documentado en DTI. Densidad e integridad dependiente del perfil psicopatológico." }};
            scene.add(fiberMesh);
            clickTargets.push(fiberMesh);

            // Pulsos de potenciales de acción
            if (t.status !== "severed") {{
              const pCount = 8;
              const pGeo = new THREE.BufferGeometry();
              const pPos = new Float32Array(pCount * 3);
              for(let k=0; k<pCount; k++) {{
                const p = curve.getPoint(k / pCount);
                pPos[k*3] = p.x; pPos[k*3+1] = p.y; pPos[k*3+2] = p.z;
              }}
              pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
              const pMat = new THREE.PointsMaterial({{ color: color, size: 0.14, transparent: true, opacity: 0.9 }});
              const pulse = new THREE.Points(pGeo, pMat);
              scene.add(pulse);
              streamlines.push({{ points: pulse, curve: curve, speed: t.status === "hyper" ? 0.75 : 0.35 }});
            }}
          }}
        }}
      }});
    }}

    // -------------------------------------------------------------
    // GRAFO DE ONDA EXPANSIVA SISTÉMICA (VIDAS AFECTADAS)
    // -------------------------------------------------------------
    if (DATA.view.includes("3.")) {{
      cortex.material.opacity = 0.05;

      DATA.social.forEach(s => {{
        const rad = 1.1 + s.tension * 0.6;
        const sGeo = new THREE.SphereGeometry(rad, 32, 32);
        const sMat = new THREE.MeshStandardMaterial({{
          color: s.color,
          emissive: s.color,
          emissiveIntensity: s.tension * 2.2,
          roughness: 0.3
        }});
        const sMesh = new THREE.Mesh(sGeo, sMat);
        sMesh.position.set(...s.coords);
        sMesh.userData = {{ name: s.name, desc: s.impact + " | Tensión de Colapso: " + (s.tension * 100).toFixed(0) + "%" }};
        scene.add(sMesh);
        clickTargets.push(sMesh);

        // Tensores estructurales de tensión
        const lGeo = new THREE.BufferGeometry().setFromPoints([
          new THREE.Vector3(0, 0, 0),
          new THREE.Vector3(...s.coords)
        ]);
        const lMat = new THREE.LineBasicMaterial({{
          color: s.tension > 0.88 ? 0xef4444 : 0x58a6ff,
          linewidth: 4,
          transparent: true,
          opacity: 0.8
        }});
        scene.add(new THREE.Line(lGeo, lMat));
      }});
    }}

    // Raycasting interactivo
    const raycaster = new THREE.Raycaster();
    const mouse = new THREE.Vector2();
    const hudHead = document.getElementById('hud-head');
    const hudBody = document.getElementById('hud-body');

    window.addEventListener('pointermove', (e) => {{
      const rect = renderer.domElement.getBoundingClientRect();
      mouse.x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
      mouse.y = -((e.clientY - rect.top) / rect.height) * 2 + 1;

      raycaster.setFromCamera(mouse, camera);
      const hits = raycaster.intersectObjects(clickTargets);

      if (hits.length > 0) {{
        const target = hits[0].object;
        if (target.userData && target.userData.name) {{
          hudHead.innerText = target.userData.name;
          hudBody.innerText = target.userData.desc;
          hudHead.style.color = "#58a6ff";
        }}
      }}
    }});

    // Bucle de renderizado continuo a 60 FPS
    const clock = new THREE.Clock();
    function render() {{
      requestAnimationFrame(render);
      const t = clock.getElapsedTime();

      // Pulsación biológica fásica diferenciada
      pulsingNodes.forEach(mesh => {{
        const hz = mesh.userData.hz || 2.0;
        const scale = 1.0 + Math.sin(t * hz) * 0.12;
        mesh.scale.set(scale, scale, scale);
      }});

      // Flujo de potenciales de acción sobre axones
      streamlines.forEach(sl => {{
        const pos = sl.points.geometry.attributes.position.array;
        const count = pos.length / 3;
        for(let i=0; i<count; i++) {{
          let progress = ((t * sl.speed) + (i / count)) % 1.0;
          let pt = sl.curve.getPoint(progress);
          pos[i*3] = pt.x;
          pos[i*3+1] = pt.y;
          pos[i*3+2] = pt.z;
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

components.html(webgl_code, height=660, scrolling=False)

# -------------------------------------------------------------------------
# Ficha Técnica y Evidencia Clínica para la Presentación
# -------------------------------------------------------------------------
st.markdown("---")
c_left, c_right = st.columns([1.3, 1.0])

with c_left:
    st.markdown("### 🔬 Sustrato Científico y Evidencia en Neuroimagen")
    st.markdown(f"""
    <div style="background-color: #0d1117; border-left: 4px solid #58a6ff; padding: 14px; border-radius: 4px; margin-bottom: 12px;">
      <b style="color: #58a6ff;">Evidencia DTI & fMRI:</b> {curr['evidence_summary']}
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    * **Fascículo Uncinado (*Uncinate Fasciculus*):** Es el tracto de sustancia blanca que conecta la corteza prefrontal ventromedial/orbitofrontal con la amígdala. Su baja integridad microestructural documentada en DTI impide la extinción normal del miedo y del afecto negativo.
    * **Red de Prominencia (*Salience Network*):** La coactivación del cíngulo anterior dorsal (dACC) y la ínsula anterior genera la vivencia visceral del dolor psíquico. En TLP, esta red se activa ante la mera posibilidad percibida de abandono; en TNP, ante la amenaza de descalificación del estatus personal.
    """)

with c_right:
    st.markdown("### 🌐 El Fenómeno de Onda Expansiva (Daño Sistémico)")
    st.markdown("""
    A diferencia de la patología neurótica convencional, donde el conflicto se contiene en el ámbito subjetivo, en el **Cluster B** la falla del freno inhibitorio biológico se traslada de forma directa al tejido social:
    * **Área Vinculante:** Ruptura destructiva de lazos de apego por mecanismos de escisión (*splitting*) o manipulación instrumental.
    * **Área Sanitaria:** Frecuentación compulsiva de guardias por conductas autolesivas o descompensaciones disfóricas agudas.
    * **Área Judicial / Penal:** Colisiones constantes con la ley en personalidades antisociales o litigios narcisistas por honra y patrimonio.
    """)
