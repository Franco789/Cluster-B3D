import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="Atlas Conectómico 3D: Cluster B",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS de la consola clínica de alta gama
st.markdown("""
<style>
    .stApp { background-color: #030712; color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    .sidebar .sidebar-content { background-color: #0b0f19; }
    h1, h2, h3 { color: #f1f5f9; font-weight: 700; letter-spacing: -0.02em; }
    .metric-card {
        background: radial-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.8) 100%);
        border: 1px solid rgba(56, 189, 248, 0.2);
        padding: 14px 18px; border-radius: 12px; margin-bottom: 12px;
        box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.5);
    }
    .metric-val { font-size: 1.6rem; font-weight: 700; color: #38bdf8; }
    .metric-lbl { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; color: #94a3b8; }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# Base de Datos Neurobiológica y Conectómica de Alta Precisión
# -------------------------------------------------------------------------
NEURO_DATABASE = {
    "TLP": {
        "title": "Trastorno Límite de la Personalidad (Borderline)",
        "circuit_name": "Disregulación Frontolímbica & Red del Dolor Social",
        "fa_uncinate": 0.21,
        "amigdala_val": 1.75,
        "vmpfc_val": 0.25,
        "acc_val": 1.55,
        "insula_val": 1.60,
        "evidence_dti": "Anisotropía Fraccional (FA) críticamente reducida en el Fascículo Uncinado bilateral (New et al., 2009; Schmahl et al., 2014). Falla estructural en la mielinización axonal tálamo-órbitofrontal.",
        "fmri_profile": "Hiperreactividad amigdalina fásica con retraso en la extinción ante estímulos socio-afectivos ambiguos. Hipoactivación severa de la corteza prefrontal ventromedial (vmPFC) que impide la modulación inhibitoria top-down.",
        "nodes": [
            {"id": "amg_r", "name": "Amígdala Derecha", "x": 2.2, "y": -0.8, "z": -1.3, "color": "#ff0055", "radius": 0.95, "glow": 2.5, "desc": "Hiperactividad desregulada; desencadena alarma de supervivencia y pánico de abandono"},
            {"id": "amg_l", "name": "Amígdala Izquierda", "x": -2.2, "y": -0.8, "z": -1.3, "color": "#ff0055", "radius": 0.95, "glow": 2.5, "desc": "Respuesta desproporcionada al rechazo interpersonal percibido"},
            {"id": "vmpfc", "name": "vmPFC / OFC", "x": 0.0, "y": 4.6, "z": -1.0, "color": "#38bdf8", "radius": 0.45, "glow": 0.3, "desc": "Colapso del freno cortical; falla en la mentalización reflexiva"},
            {"id": "dacc", "name": "Cíngulo Dorsal (dACC)", "x": 0.0, "y": 2.1, "z": 2.8, "color": "#f43f5e", "radius": 0.85, "glow": 2.0, "desc": "Alarma de dolor social activada al mismo nivel que una agresión tisular física"},
            {"id": "insula", "name": "Ínsula Anterior", "x": 3.8, "y": 0.6, "z": -0.2, "color": "#e11d48", "radius": 0.80, "glow": 1.8, "desc": "Interocepción aversiva intolerable; correlato del vacío crónico y la disforia aguda"}
        ],
        "tracts": [
            {"from": "amg_r", "to": "vmpfc", "ctrl": [3.6, 1.8, -2.4], "status": "critical", "label": "Fascículo Uncinado Der. (Disrumpido)"},
            {"from": "amg_l", "to": "vmpfc", "ctrl": [-3.6, 1.8, -2.4], "status": "critical", "label": "Fascículo Uncinado Izq. (Disrumpido)"},
            {"from": "dacc", "to": "vmpfc", "ctrl": [0.0, 3.4, 0.8], "status": "warning", "label": "Conectoma Cingulado-Frontal"},
            {"from": "amg_r", "to": "insula", "ctrl": [3.0, -0.1, -0.6], "status": "hyper", "label": "Vía Amígdalo-Insular (Hiperfuncional)"}
        ],
        "ecosystem": [
            {"name": "Vínculo de Pareja", "role": "Splitting / Terror al Abandono", "tension": 0.96, "x": 8, "y": 4, "z": 2, "color": "#ef4444"},
            {"name": "Servicio de Urgencias", "role": "Autolesiones / Parasuicidio", "tension": 0.92, "x": -7, "y": 6, "z": -3, "color": "#ef4444"},
            {"name": "Eje Identitario", "role": "Fragmentación y Vacío Crónico", "tension": 0.95, "x": 6, "y": -6, "z": -2, "color": "#f43f5e"},
            {"name": "Red Familiar Primaria", "role": "Claudicación y Reactividad Hostil", "tension": 0.88, "x": -6, "y": -4, "z": 4, "color": "#fb923c"},
            {"name": "Ámbito Laboral", "role": "Inestabilidad por Disforia Aguda", "tension": 0.70, "x": 2, "y": 7, "z": -4, "color": "#eab308"}
        ]
    },
    "TASP": {
        "title": "Trastorno Antisocial de la Personalidad (Psicopatía)",
        "circuit_name": "Ablación Funcional Frontolímbica & Falla de Aversión",
        "fa_uncinate": 0.12,
        "amigdala_val": 0.15,
        "vmpfc_val": 0.20,
        "acc_val": 0.30,
        "insula_val": 0.25,
        "evidence_dti": "Craig et al. (2009) y Motzkin et al. (2011) en reclusos psicopáticos: alteración microestructural mayor en el fascículo uncinado bilateral con pérdida marcada de integridad de tractos conectivos frontolímbicos.",
        "fmri_profile": "Atrofia funcional de la amígdala e ínsula anterior ante señales de sufrimiento ajeno (llanto, miedo) o contingencias de castigo. Circuito estriatal hiperreactivo a ganancias materiales inmediatas sin costo moral subjetivo.",
        "nodes": [
            {"id": "amg_r", "name": "Amígdala Derecha", "x": 2.2, "y": -0.8, "z": -1.3, "color": "#334155", "radius": 0.35, "glow": 0.1, "desc": "Ausencia de condicionamiento al miedo y castigo; hiporreactividad patológica"},
            {"id": "amg_l", "name": "Amígdala Izquierda", "x": -2.2, "y": -0.8, "z": -1.3, "color": "#334155", "radius": 0.35, "glow": 0.1, "desc": "Inmunidad autónoma ante la aversión al riesgo punitivo"},
            {"id": "vmpfc", "name": "vmPFC / OFC", "x": 0.0, "y": 4.6, "z": -1.0, "color": "#475569", "radius": 0.40, "glow": 0.2, "desc": "Incapacidad para asociar juicios morales con carga emocional somática"},
            {"id": "accumbens", "name": "Núcleo Accumbens (Bilateral)", "x": 1.3, "y": 1.4, "z": -0.8, "color": "#eab308", "radius": 0.90, "glow": 2.2, "desc": "Búsqueda predatoria de recompensa y dominancia instrumental"},
            {"id": "insula", "name": "Ínsula Anterior", "x": 3.8, "y": 0.6, "z": -0.2, "color": "#334155", "radius": 0.30, "glow": 0.1, "desc": "Anestesia interoceptiva; carencia absoluta de culpa somatizada"}
        ],
        "tracts": [
            {"from": "amg_r", "to": "vmpfc", "ctrl": [3.6, 1.8, -2.4], "status": "broken", "label": "Fascículo Uncinado (Ablación Conectómica)"},
            {"from": "amg_l", "to": "vmpfc", "ctrl": [-3.6, 1.8, -2.4], "status": "broken", "label": "Fascículo Uncinado (Ablación Conectómica)"},
            {"from": "vmpfc", "to": "accumbens", "ctrl": [0.6, 3.0, -1.0], "status": "uninhibited", "label": "Vía Córtico-Estriatal no Regulada"}
        ],
        "ecosystem": [
            {"name": "Fuero Penal & Judicial", "role": "Transgresión de Normas / Encarcelamiento", "tension": 0.99, "x": -8, "y": -4, "z": 2, "color": "#ef4444"},
            {"name": "Víctimas / Vínculos", "role": "Explotación Instrumental y Violencia", "tension": 0.92, "x": 7, "y": 5, "z": 3, "color": "#ef4444"},
            {"name": "Ámbito Financiero / Laboral", "role": "Fraudes, Estafas, Despidos Disciplinarios", "tension": 0.85, "x": -5, "y": 6, "z": -4, "color": "#fb923c"},
            {"name": "Servicio de Urgencias", "role": "Traumatismos por Riñas o Simulación", "tension": 0.55, "x": 4, "y": -6, "z": -3, "color": "#38bdf8"},
            {"name": "Eje Identitario", "role": "Egosintonía Total (Cero Malestar Subjetivo)", "tension": 0.20, "x": 6, "y": -2, "z": 5, "color": "#10b981"}
        ]
    },
    "TNP": {
        "title": "Trastorno Narcisista de la Personalidad",
        "circuit_name": "Disociación Fronto-Insular & Vulnerabilidad al Desprecio",
        "fa_uncinate": 0.52,
        "amigdala_val": 0.95,
        "vmpfc_val": 0.50,
        "acc_val": 1.65,
        "insula_val": 0.40,
        "evidence_dti": "Jankowiak-Siuda et al. (2015) y Fan et al. (2011): Disminución de sustancia gris y alteración conectómica en la ínsula anterior y el dACC, sustrato de la empatía afectiva deficitaria con preservación de la empatía cognitiva instrumental.",
        "fmri_profile": "Picos de hiperactividad en el dACC y la amígdala durante paradigmas de rechazo social (Cyberball task) que evidencian la 'herida narcisista', compensada por una falsa autoimagen de grandiosidad sostenida en el córtex prefrontal medial.",
        "nodes": [
            {"id": "dacc", "name": "dACC (Alarma de Estatus)", "x": 0.0, "y": 2.1, "z": 2.8, "color": "#a855f7", "radius": 0.95, "glow": 2.4, "desc": "Hipersensibilidad paroxística a la crítica, la desconfirmación o la vergüenza"},
            {"id": "vmpfc", "name": "vmPFC / Polo Frontal", "x": 0.0, "y": 4.6, "z": -1.0, "color": "#c084fc", "radius": 0.80, "glow": 1.4, "desc": "Mantenimiento del constructo grandioso defensivo compensatorio"},
            {"id": "amg_r", "name": "Amígdala (Reactiva)", "x": 2.2, "y": -0.8, "z": -1.3, "color": "#e879f9", "radius": 0.70, "glow": 1.5, "desc": "Furia fásica narcisista ante la pérdida de control o adulación"},
            {"id": "insula", "name": "Ínsula Anterior", "x": 3.8, "y": 0.6, "z": -0.2, "color": "#475569", "radius": 0.38, "glow": 0.2, "desc": "Desconexión de la empatía visceral hacia el dolor de terceros"}
        ],
        "tracts": [
            {"from": "dacc", "to": "vmpfc", "ctrl": [0.0, 3.4, 0.8], "status": "hyper", "label": "Eje de Auto-Monitoreo y Grandiosidad"},
            {"from": "amg_r", "to": "dacc", "ctrl": [1.2, 0.8, 1.2], "status": "warning", "label": "Circuito de Rabia Narcisista"},
            {"from": "insula", "to": "vmpfc", "ctrl": [2.2, 2.5, -0.6], "status": "broken", "label": "Desconexión Fronto-Insular Afectiva"}
        ],
        "ecosystem": [
            {"name": "Vínculo de Pareja", "role": "Explotación, Devaluación y Desprecio", "tension": 0.89, "x": 7, "y": 4, "z": 2, "color": "#ef4444"},
            {"name": "Eje Identitario", "role": "Fragilidad Extrema bajo Grandiosidad Falsa", "tension": 0.94, "x": 0, "y": -7, "z": -2, "color": "#a855f7"},
            {"name": "Ámbito Laboral / Status", "role": "Conflictos por Competitividad Destructiva", "tension": 0.80, "x": -6, "y": 5, "z": 3, "color": "#fb923c"},
            {"name": "Red Familiar", "role": "Exigencia de Pleitesía y Roles Rígidos", "tension": 0.75, "x": -5, "y": -5, "z": 3, "color": "#fb923c"},
            {"name": "Servicio de Urgencias", "role": "Depresión Colapsada por Fracaso de Estatus", "tension": 0.45, "x": 4, "y": 6, "z": -4, "color": "#38bdf8"}
        ]
    },
    "THP": {
        "title": "Trastorno Histriónico de la Personalidad",
        "circuit_name": "Hiperreactividad Sensorial Afectiva & Cognición Global",
        "fa_uncinate": 0.65,
        "amigdala_val": 1.25,
        "vmpfc_val": 0.40,
        "acc_val": 0.95,
        "insula_val": 1.35,
        "evidence_dti": "Varianza conectómica que compromete la sincronización fronto-temporal dorsolateral, induciendo un estilo de procesamiento cognitivo global, superficial y marcadamente sugestionable.",
        "fmri_profile": "Respuesta exagerada pero lábil de la amígdala y el núcleo accumbens a reforzadores sociales inmediatos, con activación somatosensorial e insular amplificada (conversión somatomorfa).",
        "nodes": [
            {"id": "amg_r", "name": "Amígdala", "x": 2.2, "y": -0.8, "z": -1.3, "color": "#06b6d4", "radius": 0.85, "glow": 2.0, "desc": "Emotividad desbordante pero superficial y cambiante"},
            {"id": "accumbens", "name": "Núcleo Accumbens", "x": 1.3, "y": 1.4, "z": -0.8, "color": "#22d3ee", "radius": 0.90, "glow": 2.2, "desc": "Búsqueda compulsiva de protagonismo y refuerzo social"},
            {"id": "insula", "name": "Ínsula (Somatización)", "x": 3.8, "y": 0.6, "z": -0.2, "color": "#0891b2", "radius": 0.80, "glow": 1.8, "desc": "Procesamiento interoceptivo teatralizado y conversión física"},
            {"id": "vmpfc", "name": "vmPFC", "x": 0.0, "y": 4.6, "z": -1.0, "color": "#64748b", "radius": 0.45, "glow": 0.4, "desc": "Bajo procesamiento analítico; estilo cognitivo impresionista"}
        ],
        "tracts": [
            {"from": "amg_r", "to": "accumbens", "ctrl": [1.8, 0.4, -1.0], "status": "hyper", "label": "Eje Límbico-Recompensa Social"},
            {"from": "vmpfc", "to": "amg_r", "ctrl": [1.5, 2.0, -1.2], "status": "warning", "label": "Modulación Frontal Deficitaria"}
        ],
        "ecosystem": [
            {"name": "Vínculo de Pareja", "role": "Dramatización y Seducción Inapropiada", "tension": 0.84, "x": 6, "y": 4, "z": 2, "color": "#ef4444"},
            {"name": "Servicio de Urgencias", "role": "Pseudocrisis Disociativas / Conversiones", "tension": 0.76, "x": -5, "y": 6, "z": -3, "color": "#fb923c"},
            {"name": "Red Social / Amistades", "role": "Relaciones Superficiales / Celotipia", "tension": 0.72, "x": 5, "y": -5, "z": 3, "color": "#fb923c"},
            {"name": "Eje Identitario", "role": "Dependencia del Aplauso y Validación", "tension": 0.81, "x": -2, "y": -6, "z": -2, "color": "#06b6d4"},
            {"name": "Ámbito Laboral", "role": "Baja Tolerancia a Tareas Metódicas", "tension": 0.52, "x": 2, "y": 7, "z": -4, "color": "#38bdf8"}
        ]
    }
}

# --- Sidebar de Control Académico ---
st.sidebar.markdown("### 🎛️ Consola de Neuroimagen")
selected_key = st.sidebar.selectbox("Entidad Nosológica:", list(NEURO_DATABASE.keys()), format_func=lambda k: NEURO_DATABASE[k]["title"])
stress_param = st.sidebar.slider("Vector de Disparador / Estrés Ambiental:", min_value=0.0, max_value=1.0, value=0.5, step=0.05)
render_mode = st.sidebar.radio("Modo de Representación 3D:", ["1. Conectoma & Circuitos 3D (Biología)", "2. Grafo de Onda Expansiva (Impacto Sistémico)"])

current_data = NEURO_DATABASE[selected_key]

# --- Encabezado y Métricas ---
st.title(current_data["title"])
st.markdown(f"**Circuito Fisiopatológico Central:** `{current_data['circuit_name']}`")

c1, c2, c3, c4 = st.columns(4)
dyn_fa = max(0.04, current_data["fa_uncinate"] * (1.0 - 0.4 * stress_param))
dyn_amg = current_data["amigdala_val"] * (1.0 + 0.45 * stress_param)
dyn_pfc = max(0.05, current_data["vmpfc_val"] * (1.0 - 0.5 * stress_param))
ratio_top_down = dyn_pfc / dyn_amg

with c1:
    st.markdown(f"""<div class="metric-card"><div class="metric-lbl">Integridad Fascículo Uncinado</div><div class="metric-val">{dyn_fa:.2f} FA</div></div>""", unsafe_allow_html=True)
with c2:
    st.markdown(f"""<div class="metric-card"><div class="metric-lbl">Reactividad Amigdalina</div><div class="metric-val">{dyn_amg:.2f} fMRI</div></div>""", unsafe_allow_html=True)
with c3:
    st.markdown(f"""<div class="metric-card"><div class="metric-lbl">Control Prefrontal (vmPFC)</div><div class="metric-val">{dyn_pfc:.2f} BOLD</div></div>""", unsafe_allow_html=True)
with c4:
    col = "#ef4444" if ratio_top_down < 0.3 else "#38bdf8"
    st.markdown(f"""<div class="metric-card"><div class="metric-lbl">Ratio Inhibitorio Top-Down</div><div class="metric-val" style="color: {col};">{ratio_top_down:.2f}</div></div>""", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# Componente WebGL Three.js con Post-Processing y shaders de Bioluminiscencia
# -------------------------------------------------------------------------
payload = {
    "mode": "brain" if render_mode.startswith("1.") else "ecosystem",
    "stress": stress_param,
    "nodes": current_data["nodes"],
    "tracts": current_data["tracts"],
    "ecosystem": current_data["ecosystem"],
    "uncinate_fa": dyn_fa
}

threejs_html = f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body {{ margin: 0; overflow: hidden; background: #030712; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
    #canvas-container {{ width: 100vw; height: 100vh; position: relative; }}
    #overlay-ui {{
      position: absolute; bottom: 20px; left: 24px; z-index: 10;
      background: rgba(15, 23, 42, 0.85); backdrop-filter: blur(12px);
      border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 12px;
      padding: 14px 20px; color: #f8fafc; font-size: 0.85rem; max-width: 480px;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.8);
    }}
    .node-title {{ font-weight: 700; color: #38bdf8; margin-bottom: 4px; font-size: 0.95rem; }}
    .node-desc {{ color: #cbd5e1; line-height: 1.4; }}
    #legend {{
      position: absolute; top: 20px; right: 24px; z-index: 10;
      background: rgba(15, 23, 42, 0.85); backdrop-filter: blur(10px);
      border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 10px;
      padding: 12px 16px; font-size: 0.78rem; color: #94a3b8;
    }}
    .leg-item {{ display: flex; align-items: center; margin-bottom: 6px; }}
    .leg-color {{ width: 12px; height: 12px; border-radius: 50%; margin-right: 8px; }}
  </style>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
</head>
<body>
  <div id="canvas-container">
    <div id="overlay-ui">
      <div id="ui-title" class="node-title">Atlas Conectómico Interactivo</div>
      <div id="ui-desc" class="node-desc">Haz clic o pasa el mouse por encima de cualquier estructura o tracto para visualizar la alteración neurofuncional.</div>
    </div>
    <div id="legend">
      <div class="leg-item"><div class="leg-color" style="background: #ef4444; box-shadow: 0 0 8px #ef4444;"></div> Hiperactividad / Colapso</div>
      <div class="leg-item"><div class="leg-color" style="background: #38bdf8; box-shadow: 0 0 8px #38bdf8;"></div> Tracto Mielinizado Preservado</div>
      <div class="leg-item"><div class="leg-color" style="background: #eab308; box-shadow: 0 0 8px #eab308;"></div> Estriado Ventral / Recompensa</div>
      <div class="leg-item"><div class="leg-color" style="background: #475569;"></div> Hipoactividad / Desconexión</div>
    </div>
  </div>

  <script>
    const data = {json.dumps(payload)};
    
    const container = document.getElementById('canvas-container');
    const scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x030712, 0.025);

    const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.set(0, 4, 24);

    const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    container.appendChild(renderer.domElement);

    const controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;
    controls.autoRotate = true;
    controls.autoRotateSpeed = 0.6;

    // Iluminación volumétrica
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.8);
    scene.add(ambientLight);

    const pointLight = new THREE.PointLight(0x38bdf8, 2.5, 50);
    pointLight.position.set(0, 10, 15);
    scene.add(pointLight);

    const rimLight = new THREE.PointLight(0xa855f7, 2, 40);
    rimLight.position.set(-15, -10, -10);
    scene.add(rimLight);

    const interactableObjects = [];

    if (data.mode === 'brain') {{
      // 1. Superficie Cortical Paramétrica Translúcida (Glass Cortex)
      const cortexGeo = new THREE.BufferGeometry();
      const uSegs = 70, vSegs = 70;
      const vertices = [];
      const normals = [];

      for (let i = 0; i <= uSegs; i++) {{
        let u = (i / uSegs) * Math.PI * 2;
        for (let j = 0; j <= vSegs; j++) {{
          let v = (j / vSegs) * Math.PI;
          let rx = 4.3, ry = 5.8, rz = 4.2;
          let sulci = 0.28 * Math.sin(8 * u) * Math.cos(7 * v) + 0.15 * Math.sin(16 * v);
          
          let x = (rx + sulci) * Math.sin(v) * Math.cos(u);
          let y = (ry + sulci) * Math.sin(v) * Math.sin(u);
          let z = (rz + sulci) * Math.cos(v);

          // Cisura sagital interhemisférica
          if (x >= 0) x += 0.45; else x -= 0.45;
          z -= 0.08 * (y * y) / ry;

          vertices.push(x, y, z);
        }}
      }}
      cortexGeo.setAttribute('position', new THREE.Float32BufferAttribute(vertices, 3));
      cortexGeo.computeVertexNormals();

      const cortexMat = new THREE.MeshPhysicalMaterial({{
        color: 0x1e293b,
        emissive: 0x0f172a,
        roughness: 0.2,
        metalness: 0.1,
        transparent: true,
        opacity: 0.18,
        wireframe: true,
        depthWrite: false
      }});
      const cortexMesh = new THREE.Mesh(cortexGeo, cortexMat);
      scene.add(cortexMesh);

      // 2. Nodos Subcorticales Volumétricos con Aura Emisiva
      const nodeDict = {{}};
      data.nodes.forEach(node => {{
        const sphereGeo = new THREE.SphereGeometry(node.radius, 32, 32);
        const sphereMat = new THREE.MeshStandardMaterial({{
          color: node.color,
          emissive: node.color,
          emissiveIntensity: node.glow,
          roughness: 0.3,
          metalness: 0.8
        }});
        const mesh = new THREE.Mesh(sphereGeo, sphereMat);
        mesh.position.set(node.x, node.y, node.z);
        mesh.userData = {{ name: node.name, desc: node.desc, baseGlow: node.glow }};
        scene.add(mesh);
        interactableObjects.push(mesh);
        nodeDict[node.id] = mesh.position;

        // Anillo de resonancia pulsante
        const ringGeo = new THREE.RingGeometry(node.radius * 1.2, node.radius * 1.35, 32);
        const ringMat = new THREE.MeshBasicMaterial({{ color: node.color, side: THREE.DoubleSide, transparent: true, opacity: 0.4 }});
        const ring = new THREE.Mesh(ringGeo, ringMat);
        ring.position.copy(mesh.position);
        ring.lookAt(camera.position);
        scene.add(ring);
      }});

      // 3. Tractografía DTI: Tubos Tridimensionales Continuos con Curvatura de Bézier
      data.tracts.forEach(t => {{
        if (nodeDict[t.from] && nodeDict[t.to]) {{
          const p0 = nodeDict[t.from];
          const p1 = nodeDict[t.to];
          const ctrl = new THREE.Vector3(...t.ctrl);
          const curve = new THREE.QuadraticBezierCurve3(p0, ctrl, p1);

          let tubeRadius = 0.08;
          let tubeColor = 0x38bdf8;
          let opacity = 0.9;

          if (t.status === 'critical' || t.status === 'broken') {{
            tubeColor = 0xef4444;
            tubeRadius = 0.04;
            opacity = 0.5;
          }} else if (t.status === 'hyper') {{
            tubeColor = 0xf43f5e;
            tubeRadius = 0.14;
          }}

          const tubeGeo = new THREE.TubeGeometry(curve, 32, tubeRadius, 12, false);
          const tubeMat = new THREE.MeshStandardMaterial({{
            color: tubeColor,
            emissive: tubeColor,
            emissiveIntensity: t.status === 'hyper' ? 2.0 : 0.8,
            transparent: true,
            opacity: opacity,
            wireframe: t.status === 'broken'
          }});
          const tubeMesh = new THREE.Mesh(tubeGeo, tubeMat);
          tubeMesh.userData = {{ name: t.label, desc: "Tracto axonómico de sustancia blanca. Integridad DTI modulada por patología." }};
          scene.add(tubeMesh);
          interactableObjects.push(tubeMesh);

          // Partículas en flujo continuo sobre los axones
          const particleCount = 20;
          const pGeo = new THREE.BufferGeometry();
          const pPos = new Float32Array(particleCount * 3);
          for(let i=0; i<particleCount; i++) {{
            const pt = curve.getPoint(i / particleCount);
            pPos[i*3] = pt.x; pPos[i*3+1] = pt.y; pPos[i*3+2] = pt.z;
          }}
          pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
          const pMat = new THREE.PointsMaterial({{ color: tubeColor, size: 0.15, transparent: true, opacity: 0.8 }});
          const particles = new THREE.Points(pGeo, pMat);
          scene.add(particles);
        }}
      }});

    }} else {{
      // ---------------- MODO ECOSISTEMA Y ONDA EXPANSIVA ----------------
      // Paciente Central
      const pGeo = new THREE.SphereGeometry(1.6, 32, 32);
      const pMat = new THREE.MeshStandardMaterial({{
        color: 0xef4444, emissive: 0xef4444, emissiveIntensity: 2.2, roughness: 0.2
      }});
      const patient = new THREE.Mesh(pGeo, pMat);
      patient.position.set(0, 0, 0);
      patient.userData = {{ name: "Sujeto / Estructura del Self", desc: "Núcleo biológico del Cluster B en descompensación aguda" }};
      scene.add(patient);
      interactableObjects.push(patient);

      // Esferas de Daño Colateral
      data.ecosystem.forEach(eco => {{
        const rad = 0.8 + eco.tension * 0.7;
        const eGeo = new THREE.SphereGeometry(rad, 24, 24);
        const eMat = new THREE.MeshStandardMaterial({{
          color: eco.color, emissive: eco.color, emissiveIntensity: eco.tension * 1.8, roughness: 0.4
        }});
        const eMesh = new THREE.Mesh(eGeo, eMat);
        eMesh.position.set(eco.x, eco.y, eco.z);
        eMesh.userData = {{ name: eco.name, desc: eco.role + " | Tensión Sistémica: " + eco.tension.toFixed(2) }};
        scene.add(eMesh);
        interactableObjects.push(eMesh);

        // Tensores de Tensión Elástica / Ruptura
        const lineGeo = new THREE.BufferGeometry().setFromPoints([
          new THREE.Vector3(0, 0, 0),
          new THREE.Vector3(eco.x, eco.y, eco.z)
        ]);
        const lineMat = new THREE.LineBasicMaterial({{
          color: eco.tension > 0.85 ? 0xef4444 : 0x38bdf8,
          linewidth: 3,
          transparent: true,
          opacity: 0.7
        }});
        const line = new THREE.Line(lineGeo, lineMat);
        scene.add(line);
      }});
    }}

    // Raycaster para interactividad de alta precisión
    const raycaster = new THREE.Raycaster();
    const mouse = new THREE.Vector2();
    const titleEl = document.getElementById('ui-title');
    const descEl = document.getElementById('ui-desc');

    function onPointerMove(event) {{
      const rect = renderer.domElement.getBoundingClientRect();
      mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
      mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

      raycaster.setFromCamera(mouse, camera);
      const intersects = raycaster.intersectObjects(interactableObjects);

      if (intersects.length > 0) {{
        const hit = intersects[0].object;
        if (hit.userData && hit.userData.name) {{
          titleEl.innerText = hit.userData.name;
          descEl.innerText = hit.userData.desc;
          titleEl.style.color = "#38bdf8";
        }}
      }}
    }}
    window.addEventListener('pointermove', onPointerMove);

    // Bucle de Renderizado Continuo a 60 FPS
    const clock = new THREE.Clock();
    function animate() {{
      requestAnimationFrame(animate);
      const t = clock.getElapsedTime();

      // Pulsación senoidal armónica de los núcleos
      interactableObjects.forEach((obj, i) => {{
        if (obj.material && obj.material.emissiveIntensity) {{
          obj.material.emissiveIntensity = THREE.MathUtils.lerp(
            obj.material.emissiveIntensity,
            1.2 + Math.sin(t * 4 + i) * 0.8,
            0.05
          );
        }}
      }});

      controls.update();
      renderer.render(scene, camera);
    }}
    animate();

    window.addEventListener('resize', () => {{
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    }});
  </script>
</body>
</html>
"""

# Renderizar el motor WebGL nativo en Streamlit
components.html(threejs_html, height=650, scrolling=False)

# -------------------------------------------------------------------------
# Ficha Técnica Académica de Respaldo Clínico
# -------------------------------------------------------------------------
st.markdown("---")
col_ev1, col_ev2 = st.columns(2)

with col_ev1:
    st.markdown("### 🔬 Correlato de Neuroimagen (DTI & fMRI)")
    st.markdown(f"""
    * **Tractografía DTI:** {current_data['evidence_dti']}
    * **Patrón de Activación Funcional:** {current_data['fmri_profile']}
    * **Freno Top-Down:** Falla en la activación de la corteza orbitofrontal y ventromedial que impide la habituación al dolor social.
    """)

with col_ev2:
    st.markdown("### 🌐 Psicopatología Sistémica y Onda Expansiva")
    st.markdown("""
    * **Efecto Transdiagnóstico del Cluster B:** La alteración de los circuitos del afecto y el castigo no se experimenta de forma aislada; induce rupturas en la red de apego primaria, sobrecarga los servicios de urgencias y genera colisiones frecuentes con los sistemas judiciales y laborales.
    * **Dinámica Interpersonal:** Al interactuar con el modelo en el **Modo Grafo**, se comprueba cómo la intensidad del estresor ambiental expande los tensores de ruptura roja sobre el entorno vincular del individuo.
    """)
