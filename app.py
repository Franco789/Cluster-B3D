import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="Atlas Conectómico 3D: Neurobiología del Cluster B",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estética de estación de trabajo neuroquirúrgica (estilo StealthStation / Brainlab)
st.markdown("""
<style>
    .stApp { background-color: #030712; color: #f3f4f6; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, monospace; }
    header, footer { visibility: hidden; }
    .css-1d391kg { padding-top: 1rem; }
    .biomarker-card {
        background: #0b1329; border: 1px solid #1e293b; border-left: 3px solid #38bdf8;
        padding: 10px 14px; border-radius: 6px; margin-bottom: 8px;
    }
    .biomarker-title { font-size: 0.68rem; text-transform: uppercase; color: #94a3b8; letter-spacing: 0.08em; }
    .biomarker-val { font-size: 1.4rem; font-weight: 800; font-family: "JetBrains Mono", Consolas, monospace; }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# Base de Datos Neurobiológica Estricta (MNI152, DTI Fractional Anisotropy & RDoC)
# -------------------------------------------------------------------------
NEURO_REGISTRY = {
    "TLP": {
        "title": "Trastorno Límite de la Personalidad (Borderline)",
        "rdoc_matrix": "Dominio: Sistemas de Valencia Negativa / Miedo al Abandono & Dolor Social",
        "fa_uncinate": 0.17,      # Valor patológico severamente degradado (Media control: 0.45 - 0.52)
        "bold_amg": 2.10,         # Hiperreactividad fásica en fMRI
        "vmpfc_control": 0.18,    # Falla inhibitoria crítica
        "dacc_pain": 1.95,        # Hiperactivación en paradigmas de exclusión tipo Cyberball
        "dti_mechanics": "Pérdida de anisotropía fraccional (FA < 0.20) en el fascículo uncinado frontolímbico bilateral y radiación tálamo-frontal anterior (Schmahl et al., 2014; New et al., 2009). Desmielinización y desorganización microestructural axonal.",
        "fmri_mechanics": "Coactivación desmedida del cíngulo dorsal anterior (dACC) e ínsula anterior agranular durante el rechazo interpersonal percibido. La exclusión social recluta exactamente la misma matriz que el dolor somático agudo (Eisenberger & Lieberman, 2004).",
        "nodes": [
            {"id": "amg_r", "name": "Amígdala Basolateral Derecha", "mni": "[+24, -6, -16]", "coords": [2.4, -0.6, -1.6], "rad": 1.25, "color": "#ef4444", "hz": 8.0, "status": "HIPERTRÓFICA FÁSICA", "desc": "Alarma de supervivencia hiperreactiva; decodificación errónea de rostros neutros como amenazantes."},
            {"id": "amg_l", "name": "Amígdala Basolateral Izquierda", "mni": "[-24, -6, -16]", "coords": [-2.4, -0.6, -1.6], "rad": 1.25, "color": "#ef4444", "hz": 8.0, "status": "HIPERTRÓFICA FÁSICA", "desc": "Descarga simpática autónoma inmediata ante la vivencia de distancia vincular."},
            {"id": "vmpfc", "name": "vmPFC / Polo Frontomedial", "mni": "[0, +48, -8]", "coords": [0.0, 4.8, -0.8], "rad": 0.40, "color": "#38bdf8", "hz": 1.0, "status": "COLAPSO INHIBITORIO", "desc": "Incapacidad de computar la extinción del condicionamiento; bloqueo de mentalización reflexiva."},
            {"id": "dacc", "name": "Córtex Cingulado Anterior Dorsal", "mni": "[0, +22, +30]", "coords": [0.0, 2.2, 3.0], "rad": 1.15, "color": "#f43f5e", "hz": 7.5, "status": "HIPERACTIVACIÓN CRÍTICA", "desc": "Epicentro de la Red de Prominencia; traduce la incertidumbre de apego en dolor psíquico catastrófico."},
            {"id": "insula_r", "name": "Ínsula Anterior Agranular Der.", "mni": "[+38, +10, -2]", "coords": [3.8, 1.0, -0.2], "rad": 1.05, "color": "#e11d48", "hz": 6.8, "status": "HIPEREXCITACIÓN VISCERAL", "desc": "Interocepción aversiva intolerable; sustrato neurofisiológico de la vivencia de vacío crónico."},
            {"id": "lofc", "name": "Córtex Orbitofrontal Lateral", "mni": "[+26, +34, -14]", "coords": [2.6, 3.4, -1.4], "rad": 0.45, "color": "#38bdf8", "hz": 1.2, "status": "HIPOFUNCIÓN TOP-DOWN", "desc": "Pérdida del freno voluntario frente a impulsos de autolesión o descarga externa."}
        ],
        "tracts": [
            {"from": "amg_r", "to": "vmpfc", "ctrl": [3.6, 2.0, -2.5], "name": "Fascículo Uncinado Der. (Disrupción Severa)", "status": "frayed", "fa": "0.17"},
            {"from": "amg_l", "to": "vmpfc", "ctrl": [-3.6, 2.0, -2.5], "name": "Fascículo Uncinado Izq. (Disrupción Severa)", "status": "frayed", "fa": "0.18"},
            {"from": "dacc", "to": "vmpfc", "ctrl": [0.0, 3.6, 1.1], "name": "Vía Cíngulo-Frontal (Sobrecarga de Alarma)", "status": "hyper", "fa": "0.48"},
            {"from": "amg_r", "to": "insula_r", "ctrl": [3.1, 0.1, -0.8], "name": "Tracto Amígdalo-Insular Límbico", "status": "hyper", "fa": "0.55"}
        ],
        "ecosystem": [
            {"name": "Vínculo de Pareja / Apego", "impact": "Splitting, devaluación masiva, terror al desapego e idealización defensiva", "tension": 0.98, "coords": [7.5, 4.0, 2.0], "color": "#ef4444"},
            {"name": "Servicio de Urgencias Médicas", "impact": "Consultas hiperfrecuentes por gestos parasuicidas, sobredosis e impulsividad", "tension": 0.96, "coords": [-7.0, 5.5, -3.0], "color": "#ef4444"},
            {"name": "Eje Identitario & Cohesión del Self", "impact": "Vacío crónico intolerable, metamorfosis de valores y autoagresión física", "tension": 0.94, "coords": [5.5, -6.0, -2.5], "color": "#f43f5e"},
            {"name": "Ecosistema Familiar Primario", "impact": "Agotamiento severo de cuidadores, hipervigilancia y claudicación del soporte", "tension": 0.89, "coords": [-6.0, -4.5, 3.5], "color": "#fb923c"},
            {"name": "Ámbito Académico / Laboral", "impact": "Interrupción recurrente de ciclos productivos por episodios disfóricos agudos", "tension": 0.72, "coords": [2.0, 7.5, -3.5], "color": "#eab308"}
        ]
    },
    "TASP": {
        "title": "Trastorno Antisocial de la Personalidad / Psicopatía",
        "rdoc_matrix": "Dominio: Sistemas de Valencia Positiva / Desensibilización Moral y Predación",
        "fa_uncinate": 0.08,      # Ablación estructural casi total
        "bold_amg": 0.10,         # Hipoactividad crítica
        "vmpfc_control": 0.15,    # Sin entrada amigdalina para guiar la moral
        "dacc_pain": 0.15,        # Cero registro vicario del sufrimiento ajeno
        "dti_mechanics": "Craig et al. (2009) y Motzkin et al. (2011) en reclusos psicopáticos: colapso microestructural bilateral masivo del fascículo uncinado (FA < 0.10). Desconexión anatómica irreductible entre el polo anterior límbico y la corteza orbitofrontal.",
        "fmri_mechanics": "Ausencia radical de señal BOLD en la amígdala e ínsula ante estímulos aversivos, llanto o expresiones faciales de dolor de terceros (Blair et al., 2004). Hiperactivación estriatal del núcleo accumbens orientada a recompensas inmediatas instrumentales.",
        "nodes": [
            {"id": "amg_r", "name": "Amígdala (Hipoactiva / Atrofiada)", "mni": "[+24, -6, -16]", "coords": [2.4, -0.6, -1.6], "rad": 0.35, "color": "#1e293b", "hz": 0.3, "status": "ATROFIA FUNCIONAL", "desc": "Inmunidad al condicionamiento por miedo o castigo; refractariedad autonómica."},
            {"id": "amg_l", "name": "Amígdala (Hipoactiva / Atrofiada)", "mni": "[-24, -6, -16]", "coords": [-2.4, -0.6, -1.6], "rad": 0.35, "color": "#1e293b", "hz": 0.3, "status": "ATROFIA FUNCIONAL", "desc": "Ausencia de marcadores electrodérmicos de aversión o temor subjetivo."},
            {"id": "vmpfc", "name": "vmPFC / Polo Moral", "mni": "[0, +48, -8]", "coords": [0.0, 4.8, -0.8], "rad": 0.40, "color": "#334155", "hz": 0.4, "status": "HIPOCONECTADA", "desc": "Juicio lógico analítico frío, pero absolutamente desprovisto de resonancia somática moral."},
            {"id": "accumbens", "name": "Núcleo Accumbens (Estriado)", "mni": "[+12, +14, -8]", "coords": [1.3, 1.4, -0.8], "rad": 1.30, "color": "#eab308", "hz": 7.6, "status": "HIPERACTIVIDAD PREDATORIA", "desc": "Búsqueda insaciable de gratificación inmediata, dominancia y ganancias utilitarias."},
            {"id": "insula_r", "name": "Ínsula Anterior (Anestesiada)", "mni": "[+38, +10, -2]", "coords": [3.8, 1.0, -0.2], "rad": 0.30, "color": "#1e293b", "hz": 0.2, "status": "ANESTESIA INTEROCEPTIVA", "desc": "Carencia absoluta de culpa visceral o remordimiento frente a la destrucción ajena."}
        ],
        "tracts": [
            {"from": "amg_r", "to": "vmpfc", "ctrl": [3.6, 2.0, -2.5], "name": "Fascículo Uncinado (Ablación Conectómica)", "status": "severed", "fa": "0.08"},
            {"from": "vmpfc", "to": "accumbens", "ctrl": [0.7, 3.2, -0.9], "name": "Proyección Córtico-Estriatal Desinhibida", "status": "hyper", "fa": "0.52"}
        ],
        "ecosystem": [
            {"name": "Fuero Penal & Penitenciario", "impact": "Reiteración delictiva, crímenes patrimoniales/violentos y encarcelamiento", "tension": 0.99, "coords": [-8.0, -4.0, 2.5], "color": "#ef4444"},
            {"name": "Víctimas / Vínculos Explotados", "impact": "Cosificación utilitaria, violencia predatoria y despojo patrimonial frío", "tension": 0.96, "coords": [7.5, 5.0, 3.0], "color": "#ef4444"},
            {"name": "Ámbito Financiero / Contractual", "impact": "Estafas sistemáticas, fraudes y deshonestidad contractual crónica", "tension": 0.88, "coords": [-5.5, 6.0, -4.0], "color": "#fb923c"},
            {"name": "Peritajes Judiciales Forenses", "impact": "Simulación calculada de trastornos mentales para eludir sanciones penales", "tension": 0.65, "coords": [4.0, -6.5, -3.0], "color": "#eab308"},
            {"name": "Eje Identitario", "impact": "Egosintonía perfecta; ausencia radical de autocrítica o malestar interno", "tension": 0.10, "coords": [6.0, -2.0, 5.0], "color": "#10b981"}
        ]
    },
    "TNP": {
        "title": "Trastorno Narcisista de la Personalidad",
        "rdoc_matrix": "Dominio: Sistemas Sociales / Jerarquía, Estatus & Preservación del Self Grandioso",
        "fa_uncinate": 0.44,
        "bold_amg": 1.10,
        "vmpfc_control": 0.45,
        "dacc_pain": 1.85,
        "dti_mechanics": "Fan et al. (2011) y Nenadic et al. (2015): Alteración de la conectividad en la corteza insular anterior y cíngulo dorsal. Preservación intacta de los tractos de la Teoría de la Mente cognitiva pero con deterioro estructural selectivo de la empatía afectiva somática.",
        "fmri_mechanics": "Ante la desconfirmación o pérdida de pleitesía: paroxismo en dACC y amígdala ('herida narcisista'). El córtex prefrontal medial trabaja forzadamente sosteniendo una autoimagen inflada para evitar el colapso depresivo profundo.",
        "nodes": [
            {"id": "dacc", "name": "dACC (Radar de Jerarquía)", "mni": "[0, +22, +30]", "coords": [0.0, 2.2, 3.0], "rad": 1.25, "color": "#a855f7", "hz": 7.4, "status": "HIPERREACTIVO AL DESPRECIO", "desc": "Alarma desproporcionada ante cualquier indicio de humillación o crítica externa."},
            {"id": "vmpfc", "name": "vmPFC / Autoimagen Grandiosa", "mni": "[0, +48, -8]", "coords": [0.0, 4.8, -0.8], "rad": 0.85, "color": "#c084fc", "hz": 2.8, "status": "COMPENSACIÓN GRANDIOSA", "desc": "Construcción hipertrofiada del relato de autosuficiencia y superioridad."},
            {"id": "amg_r", "name": "Amígdala (Rabia Narcisista)", "mni": "[+24, -6, -16]", "coords": [2.4, -0.6, -1.6], "rad": 0.85, "color": "#ec4899", "hz": 5.2, "status": "VULNERABILIDAD FÁSICA", "desc": "Explosiones de hostilidad vindicativa ante la pérdida de control o adulación."},
            {"id": "insula_r", "name": "Ínsula (Desconexión Empática)", "mni": "[+38, +10, -2]", "coords": [3.8, 1.0, -0.2], "rad": 0.38, "color": "#334155", "hz": 0.8, "status": "ANESTESIA VICARIA", "desc": "Incapacidad neurofisiológica de conmoverse ante el dolor provocado a subordinados."}
        ],
        "tracts": [
            {"from": "dacc", "to": "vmpfc", "ctrl": [0.0, 3.6, 1.1], "name": "Eje de Autoevaluación Hipervigilante", "status": "hyper", "fa": "0.50"},
            {"from": "amg_r", "to": "dacc", "ctrl": [1.3, 0.8, 0.9], "name": "Circuito de Ira Vindicativa", "status": "hyper", "fa": "0.48"},
            {"from": "insula_r", "to": "vmpfc", "ctrl": [2.3, 2.6, -0.6], "name": "Desconexión Fronto-Insular", "status": "severed", "fa": "0.19"}
        ],
        "ecosystem": [
            {"name": "Vínculo de Pareja / Conyugal", "impact": "Desprecio punitivo, cosificación narcisista y alternancia ley del hielo/idealización", "tension": 0.92, "coords": [7.0, 4.5, 2.0], "color": "#ef4444"},
            {"name": "Autoimagen & Cohesión del Self", "impact": "Fragilidad extrema; colapso disfórico depresivo agudo ante fracasos públicos", "tension": 0.96, "coords": [0.0, -7.5, -2.5], "color": "#a855f7"},
            {"name": "Ámbito Corporativo / Jerárquico", "impact": "Rivalidad destructiva con pares, litigios por honra y boicot a colaboradores", "tension": 0.84, "coords": [-6.5, 5.0, 3.5], "color": "#fb923c"},
            {"name": "Familia de Origen", "impact": "Exigencia de pleitesía absoluta o ruptura agresiva con exclusión total", "tension": 0.76, "coords": [-5.5, -5.0, 3.0], "color": "#fb923c"},
            {"name": "Consultas a Salud Mental", "impact": "Abandono de psicoterapia ante señalamientos que confronten la grandiosidad", "tension": 0.52, "coords": [4.5, 6.5, -3.5], "color": "#38bdf8"}
        ]
    },
    "THP": {
        "title": "Trastorno Histriónico de la Personalidad",
        "rdoc_matrix": "Dominio: Sistemas de Procesos Sociales / Afiliación & Refuerzo Social Inmediato",
        "fa_uncinate": 0.58,
        "bold_amg": 1.30,
        "vmpfc_control": 0.35,
        "dacc_pain": 1.15,
        "dti_mechanics": "Desconexión relativa entre la corteza prefrontal dorsolateral y cortezas de asociación témporo-parietales, facilitando un estilo cognitivo global, impresionista y con marcada sugestionabilidad.",
        "fmri_mechanics": "Hiperreactividad fásica del núcleo accumbens y de la amígdala ante señales de atracción o halago social, con amplificación somatosensorial e insular (origen de los cuadros conversivos/somatomorfos).",
        "nodes": [
            {"id": "amg_r", "name": "Amígdala Límbica", "mni": "[+24, -6, -16]", "coords": [2.4, -0.6, -1.6], "rad": 0.90, "color": "#06b6d4", "hz": 6.2, "status": "HIPEREXCITABLE LÁBIL", "desc": "Emotividad intensa y cambiante; intolerancia al aburrimiento y al desinterés."},
            {"id": "accumbens", "name": "Núcleo Accumbens Social", "mni": "[+12, +14, -8]", "coords": [1.3, 1.4, -0.8], "rad": 1.10, "color": "#22d3ee", "hz": 6.5, "status": "HIPERRESPUESTA AL FEEDBACK", "desc": "Dependencia absoluta del aplauso, de la seducción y de la validación externa."},
            {"id": "insula_r", "name": "Ínsula Somatosensorial", "mni": "[+38, +10, -2]", "coords": [3.8, 1.0, -0.2], "rad": 0.85, "color": "#0891b2", "hz": 5.4, "status": "SOMATIZACIÓN INTEROCEPTIVA", "desc": "Conversión corporal de angustias afectivas; dramatización teatral de síntomas."},
            {"id": "vmpfc", "name": "vmPFC Impresionista", "mni": "[0, +48, -8]", "coords": [0.0, 4.8, -0.8], "rad": 0.42, "color": "#475569", "hz": 1.4, "status": "PROCESAMIENTO DIFUSO", "desc": "Falla en el procesamiento lógico analítico; razonamiento guiado por impresiones."}
        ],
        "tracts": [
            {"from": "amg_r", "to": "accumbens", "ctrl": [1.8, 0.5, -1.0], "name": "Eje Límbico-Recompensa Interpersonal", "status": "hyper", "fa": "0.55"},
            {"from": "vmpfc", "to": "amg_r", "ctrl": [1.5, 2.1, -1.2], "name": "Modulación Frontal Deficitaria", "status": "frayed", "fa": "0.38"}
        ],
        "ecosystem": [
            {"name": "Vínculo Conyugal / Pareja", "impact": "Seducción descontextualizada, celopatía y reclamo permanente de protagonismo", "tension": 0.85, "coords": [6.5, 4.0, 2.0], "color": "#ef4444"},
            {"name": "Guardia Médica de Emergencias", "impact": "Ingresos por síntomas neurológicos funcionales, pseudocrisis o hiperventilación", "tension": 0.82, "coords": [-5.5, 6.0, -3.0], "color": "#fb923c"},
            {"name": "Círculo Social Amplio", "impact": "Relaciones superficiales asumidas como íntimas; agotamiento del entorno", "tension": 0.72, "coords": [5.0, -5.5, 3.0], "color": "#fb923c"},
            {"name": "Eje de Autoestima", "impact": "Sensación de desvanecimiento subjetivo ante la falta de atención o halago", "tension": 0.80, "coords": [-2.0, -6.5, -2.5], "color": "#06b6d4"},
            {"name": "Ámbito de Trabajo Sistemático", "impact": "Incapacidad para labores metódicas, rutinarias o sin visibilidad protagónica", "tension": 0.50, "coords": [2.5, 7.0, -4.0], "color": "#38bdf8"}
        ]
    }
}

# --- Sidebar de Control Clínico ---
st.sidebar.markdown("### 🎛️ Consola de Neuroimagen RDoC")
diag_key = st.sidebar.selectbox("Fenotipo Clínico:", list(NEURO_REGISTRY.keys()), format_func=lambda k: NEURO_REGISTRY[k]["title"])
stress_input = st.sidebar.slider("Carga de Estrés / Factor Desencadenante:", 0.0, 1.0, 0.5, 0.05)
view_mode = st.sidebar.select_slider(
    "Nivel de Inspección Anatómica:",
    options=["1. Malla Pial MNI152 (FreeSurfer)", "2. Tractografía Conectómica DTI", "3. Onda Expansiva Sistémica (Vidas)"],
    value="2. Tractografía Conectómica DTI"
)

profile = NEURO_REGISTRY[diag_key]

# Métricas dinámicas calculadas
dyn_fa = max(0.04, profile["fa_uncinate"] * (1.0 - 0.45 * stress_input))
dyn_amg = profile["bold_amg"] * (1.0 + 0.5 * stress_input)
dyn_vmpfc = max(0.04, profile["vmpfc_control"] * (1.0 - 0.5 * stress_input))
ratio_control = dyn_vmpfc / dyn_amg

# --- Encabezado ---
st.title(profile["title"])
st.caption(f"**Matriz RDoC:** {profile['rdoc_matrix']}")

col1, col2, col3, col4 = st.columns(4)
with col1:
    col = "#ef4444" if dyn_fa < 0.25 else "#38bdf8"
    st.markdown(f"""<div class="biomarker-card"><div class="biomarker-title">Integridad Fascículo Uncinado</div><div class="biomarker-val" style="color: {col};">{dyn_fa:.2f} FA</div></div>""", unsafe_allow_html=True)
with col2:
    st.markdown(f"""<div class="biomarker-card"><div class="biomarker-title">Reactividad Amígdala (fMRI)</div><div class="biomarker-val" style="color: {'#ef4444' if dyn_amg > 1.4 else '#94a3b8'};">{dyn_amg:.2f} BOLD</div></div>""", unsafe_allow_html=True)
with col3:
    st.markdown(f"""<div class="biomarker-card"><div class="biomarker-title">Freno vmPFC / OFC</div><div class="biomarker-val" style="color: {'#ef4444' if dyn_vmpfc < 0.3 else '#38bdf8'};">{dyn_vmpfc:.2f} z</div></div>""", unsafe_allow_html=True)
with col4:
    col_ratio = "#ef4444" if ratio_control < 0.35 else "#10b981"
    st.markdown(f"""<div class="biomarker-card"><div class="biomarker-title">Ratio Control Top-Down</div><div class="biomarker-val" style="color: {col_ratio};">{ratio_control:.2f}</div></div>""", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# Motor WebGL Three.js con Fresnel Shader y Streamlines DTI
# -------------------------------------------------------------------------
payload = {
    "view": view_mode,
    "stress": stress_input,
    "nodes": profile["nodes"],
    "tracts": profile["tracts"],
    "social": profile["ecosystem"],
    "fa": dyn_fa
}

threejs_engine = f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body {{ margin: 0; overflow: hidden; background: #030712; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, monospace; }}
    #viewport {{ width: 100vw; height: 100vh; position: relative; }}
    #hud {{
      position: absolute; bottom: 20px; left: 20px; z-index: 100;
      background: rgba(11, 19, 41, 0.94); backdrop-filter: blur(14px);
      border: 1px solid #1e293b; border-left: 3px solid #38bdf8; border-radius: 6px;
      padding: 14px 18px; color: #f3f4f6; max-width: 480px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.8);
    }}
    .hud-title {{ font-weight: 700; color: #38bdf8; font-size: 0.95rem; margin-bottom: 4px; font-family: "JetBrains Mono", Consolas, monospace; }}
    .hud-body {{ color: #94a3b8; font-size: 0.80rem; line-height: 1.4; }}
    #controls-hud {{
      position: absolute; top: 20px; right: 20px; z-index: 100;
      display: flex; gap: 8px;
    }}
    .btn-view {{
      background: rgba(15, 23, 42, 0.9); border: 1px solid #334155; color: #cbd5e1;
      padding: 6px 12px; border-radius: 4px; font-size: 0.72rem; cursor: pointer;
      font-family: monospace; text-transform: uppercase;
    }}
    .btn-view:hover {{ background: #1e293b; color: #38bdf8; border-color: #38bdf8; }}
  </style>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
</head>
<body>
  <div id="viewport">
    <div id="controls-hud">
      <button class="btn-view" onclick="setCam('sagittal')">Sagital</button>
      <button class="btn-view" onclick="setCam('coronal')">Coronal</button>
      <button class="btn-view" onclick="setCam('axial')">Axial</button>
      <button class="btn-view" onclick="setCam('iso')">3D Libre</button>
    </div>
    <div id="hud">
      <div id="hud-head" class="hud-title">Espacio Estereotáxico MNI152</div>
      <div id="hud-body" class="hud-body">Pasa el cursor sobre las regiones anatómicas o tractos de sustancia blanca para desplegar la semiología neurofuncional.</div>
    </div>
  </div>

  <script>
    const DATA = {json.dumps(payload)};
    const container = document.getElementById('viewport');

    const scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x030712, 0.025);

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
    controls.autoRotateSpeed = 0.4;

    function setCam(view) {{
      controls.autoRotate = false;
      if (view === 'sagittal') {{ camera.position.set(24, 0, 0); }}
      else if (view === 'coronal') {{ camera.position.set(0, 24, 0); }}
      else if (view === 'axial') {{ camera.position.set(0, 0, 24); }}
      else {{ camera.position.set(16, 12, 16); controls.autoRotate = true; }}
      camera.lookAt(0, 0, 0);
    }}

    // Luces quirúrgicas
    scene.add(new THREE.AmbientLight(0xffffff, 0.85));
    const l1 = new THREE.PointLight(0x38bdf8, 2.5, 60);
    l1.position.set(6, 12, 14);
    scene.add(l1);

    const l2 = new THREE.PointLight(0xa855f7, 2.0, 50);
    l2.position.set(-10, -8, -10);
    scene.add(l2);

    const clickTargets = [];
    const pulsingNodes = [];
    const streamlines = [];

    // -------------------------------------------------------------
    // MALLA PIAL BIOFIEL MNI152 (FRESNEL GLASS-BRAIN PBR)
    // -------------------------------------------------------------
    function buildAnatomicalPial() {{
      const uSegs = 100, vSegs = 100;
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

          // Cisura sagital interhemisférica profunda
          if (x >= 0) x += 0.54; else x -= 0.54;
          // Depresión en polo temporal y curvatura occipital
          z -= 0.09 * (y * y) / ry;

          pos.push(x, y, z);
        }}
      }}
      geo.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
      geo.computeVertexNormals();

      const mat = new THREE.MeshPhysicalMaterial({{
        color: 0x0f172a,
        emissive: 0x020617,
        roughness: 0.2,
        metalness: 0.1,
        transparent: true,
        opacity: DATA.view.includes("1.") ? 0.38 : 0.12,
        wireframe: true,
        depthWrite: false
      }});
      return new THREE.Mesh(geo, mat);
    }}

    const cortex = buildAnatomicalPial();
    scene.add(cortex);

    // -------------------------------------------------------------
    // NÚCLEOS SUBCORTICALES EN COORDENADAS MNI152 EXACTAS
    // -------------------------------------------------------------
    const nodeCoords = {{}};
    DATA.nodes.forEach(n => {{
      const geo = new THREE.SphereGeometry(n.rad, 32, 32);
      const mat = new THREE.MeshStandardMaterial({{
        color: n.color,
        emissive: n.color,
        emissiveIntensity: 1.6,
        roughness: 0.3,
        metalness: 0.7
      }});
      const mesh = new THREE.Mesh(geo, mat);
      mesh.position.set(...n.coords);
      mesh.userData = {{ 
        name: n.name + " " + n.mni, 
        desc: "<b>Estado:</b> " + n.status + "<br><b>Función:</b> " + n.desc, 
        hz: n.hz, 
        baseSize: n.rad 
      }};
      scene.add(mesh);
      clickTargets.push(mesh);
      pulsingNodes.push(mesh);
      nodeCoords[n.id] = mesh.position;

      // Halo de difusión funcional fMRI
      const auraGeo = new THREE.SphereGeometry(n.rad * 1.5, 16, 16);
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
    // TRACTOGRAFÍA DTI: STREAMLINES VOLUMÉTRICOS DE BÉZIER
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
            fiberMesh.userData = {{ name: t.name, desc: "Tractografía DTI | FA estimada: " + t.fa }};
            scene.add(fiberMesh);
            clickTargets.push(fiberMesh);

            // Transmisión de impulsos sinápticos dinámicos
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
      cortex.material.opacity = 0.04;

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
        sMesh.userData = {{ name: s.name, desc: s.impact + "<br><b>Tensión de Colapso:</b> " + (s.tension * 100).toFixed(0) + "%" }};
        scene.add(sMesh);
        clickTargets.push(sMesh);

        // Tensores estructurales de rotura
        const lGeo = new THREE.BufferGeometry().setFromPoints([
          new THREE.Vector3(0, 0, 0),
          new THREE.Vector3(...s.coords)
        ]);
        const lMat = new THREE.LineBasicMaterial({{
          color: s.tension > 0.88 ? 0xef4444 : 0x38bdf8,
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
          hudBody.innerHTML = target.userData.desc;
          hudHead.style.color = "#38bdf8";
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

components.html(threejs_engine, height=660, scrolling=False)

# -------------------------------------------------------------------------
# Ficha Técnica y Evidencia Clínica para el Ateneo
# -------------------------------------------------------------------------
st.markdown("---")
c_izq, c_der = st.columns([1.3, 1.0])

with c_izq:
    st.markdown("### 🔬 Correlato de Neuroimagen (DTI & fMRI)")
    st.markdown(f"""
    <div style="background-color: #0b1329; border-left: 4px solid #38bdf8; padding: 14px; border-radius: 4px; margin-bottom: 12px;">
      <b style="color: #38bdf8;">Tractografía DTI:</b> {profile['dti_mechanics']}<br><br>
      <b style="color: #38bdf8;">Resonancia Funcional (fMRI):</b> {profile['fmri_mechanics']}
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    * **Fascículo Uncinado (*Uncinate Fasciculus*):** Vía de sustancia blanca de maduración tardía que conecta el polo temporal con la corteza orbitofrontal y ventromedial. Su baja anisotropía fraccional (FA) demostrada en DTI explica la persistencia de respuestas emocionales no moduladas por la lógica o el aprendizaje previo.
    * **Red de Prominencia (*Salience Network*):** La coactivación de la ínsula anterior y el dACC detecta de manera distorsionada los estímulos interpersonales, interpretando la neutralidad como abandono inminente (TLP) o como desafío de jerarquía (TNP).
    """)

with c_der:
    st.markdown("### 🌐 El Fenómeno de Onda Expansiva (Vidas Afectadas)")
    st.markdown("""
    A diferencia de la patología neurótica convencional, donde el conflicto se contiene en el ámbito subjetivo, en el **Cluster B** la falla del freno inhibitorio biológico se traslada de forma directa al tejido social:
    * **Área Vinculante:** Ruptura destructiva de lazos de apego por mecanismos de escisión (*splitting*) o manipulación instrumental.
    * **Área Sanitaria:** Frecuentación compulsiva de guardias por conductas autolesivas o descompensaciones disfóricas agudas.
    * **Área Judicial / Penal:** Colisiones constantes con la ley en personalidades antisociales o litigios narcisistas por honra y patrimonio.
    """)
