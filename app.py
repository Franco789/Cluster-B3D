import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="Neuroconectoma 3D: Psicopatología del Cluster B",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estética quirúrgica dark-mode con tipografía técnica
st.markdown("""
<style>
    .stApp { background-color: #010409; color: #e6edf3; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, monospace; }
    h1, h2, h3, h4 { color: #f0f6fc; font-weight: 700; letter-spacing: -0.02em; }
    .metric-panel {
        background: #0d1117; border: 1px solid #30363d;
        border-radius: 8px; padding: 12px 16px; margin-bottom: 10px;
    }
    .metric-val { font-size: 1.55rem; font-weight: 800; font-family: ui-monospace, Menlo, Consolas, monospace; }
    .metric-sub { font-size: 0.72rem; text-transform: uppercase; color: #8b949e; letter-spacing: 0.05em; }
    .evidence-card {
        background: #0d1117; border-left: 4px solid #38bdf8;
        padding: 14px 18px; border-radius: 4px; margin-top: 15px; margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# Base de Datos Neurobiológica y Conectómica (Espacio MNI152 y Criterios RDoC)
# -------------------------------------------------------------------------
DATABASE = {
    "TLP": {
        "title": "Trastorno Límite de la Personalidad (Borderline)",
        "subtitle": "Hiperreactividad Límbica, Ruptura Uncinada & Alarma de Dolor Social",
        "fa_uncinate": 0.18,
        "amg_activation": 1.95,
        "vmpfc_activity": 0.22,
        "acc_pain": 1.90,
        "rdoc_construct": "Sistemas de Valencia Negativa / Miedo al Abandono",
        "dti_evidence": "Schmahl et al. (2014) y New et al. (2009): Disminución crítica de anisotropía fraccional (FA < 0.20) en el fascículo uncinado bilateral y la radiación tálamo-frontal anterior. Desconexión anatómica del control prefrontal sobre el núcleo basolateral amigdalino.",
        "fmri_evidence": "En paradigmas Cyberball (dolor de exclusión) y lectura facial fásica: coactivación paroxística del dACC y de la ínsula anterior bilateral. La exclusión social recluta exactamente las mismas subredes que el dolor nociceptivo somático agudo (Eisenberger & Lieberman).",
        "nodes": [
            {"id": "amg_r", "name": "Amígdala Basolateral (Der)", "x": 2.4, "y": -0.7, "z": -1.5, "mni": "[+24, -7, -15]", "color": "#ef4444", "rad": 1.15, "hz": 8.0, "status": "HIPERTRÓFICA / HIPERACTIVA", "role": "Detección errónea de amenaza en rostros neutros; desregulación simpática aguda."},
            {"id": "amg_l", "name": "Amígdala Basolateral (Izq)", "x": -2.4, "y": -0.7, "z": -1.5, "mni": "[-24, -7, -15]", "color": "#ef4444", "rad": 1.15, "hz": 8.0, "status": "HIPERTRÓFICA / HIPERACTIVA", "role": "Respuesta fásica masiva ante señales percibidas de abandono o distanciamiento."},
            {"id": "vmpfc", "name": "vmPFC / Subgenual", "x": 0.0, "y": 4.6, "z": -0.9, "mni": "[0, +46, -9]", "color": "#38bdf8", "rad": 0.45, "hz": 1.2, "status": "HIPOFUNCIÓN CRÍTICA", "role": "Incapacidad para modular la intensidad afectiva; colapso de la mentalización."},
            {"id": "ofc", "name": "Córtex Orbitofrontal Lateral", "x": 1.8, "y": 4.0, "z": -1.8, "mni": "[+18, +40, -18]", "color": "#38bdf8", "rad": 0.45, "hz": 1.2, "status": "FALTA DE EXTINCIÓN", "role": "Falla en el cálculo flexible de consecuencias y en la extinción del condicionamiento aversivo."},
            {"id": "dacc", "name": "Cíngulo Anterior Dorsal (dACC)", "x": 0.0, "y": 2.4, "z": 2.8, "mni": "[0, +24, +28]", "color": "#f43f5e", "rad": 1.05, "hz": 7.2, "status": "HIPERREACTIVA (DOLOR SOCIAL)", "role": "Nodo central de la red de prominencia; traduce el rechazo vincular en vivencia de herida tisular."},
            {"id": "insula_r", "name": "Ínsula Anterior Agranular", "x": 3.9, "y": 0.7, "z": 0.1, "mni": "[+39, +7, +1]", "color": "#e11d48", "rad": 0.95, "hz": 6.5, "status": "SOBREACTIVACIÓN VISCERAL", "role": "Interocepción aversiva intolerable; sustrato neurofisiológico de la vivencia de 'vacío' crónico."},
            {"id": "dlpfc", "name": "dlPFC (Control Ejecutivo)", "x": 3.4, "y": 3.6, "z": 3.2, "mni": "[+34, +36, +32]", "color": "#475569", "rad": 0.50, "hz": 1.5, "status": "DESCONEXIÓN FUNCIONAL", "role": "Freno voluntario suprimido durante la crisis emocional."}
        ],
        "tracts": [
            {"from": "amg_r", "to": "vmpfc", "ctrl": [3.6, 2.0, -2.5], "name": "Fascículo Uncinado Derecho (FA: 0.18)", "status": "severed", "desc": "Tracto axonómico desmielinizado; pérdida de modulación inhibitoria frontolímbica."},
            {"from": "amg_l", "to": "vmpfc", "ctrl": [-3.6, 2.0, -2.5], "name": "Fascículo Uncinado Izquierdo (FA: 0.18)", "status": "severed", "desc": "Interrupción de la conectividad estructural recíproca amígdalo-prefrontal."},
            {"from": "dacc", "to": "vmpfc", "ctrl": [0.0, 3.5, 1.0], "name": "Vía Cíngulo-Frontal", "status": "hyper", "desc": "Sobrecarga de conflicto y dolor social sin resolución cognitiva."},
            {"from": "amg_r", "to": "insula_r", "ctrl": [3.1, -0.1, -0.7], "name": "Conexión Límbico-Insular", "status": "hyper", "desc": "Retroalimentación viscero-afectiva continua generadora de disforia paroxística."}
        ],
        "ecosystem": [
            {"name": "Vínculo de Pareja / Apego", "impact": "Splitting, terror al abandono, alternancia idealización-odio", "tension": 0.98, "coords": [7.5, 4.0, 2.0], "color": "#ef4444"},
            {"name": "Guardia Médica / Urgencias", "impact": "Consultas frecuentes por parasuicidio y autolesiones impulsivas", "tension": 0.95, "coords": [-7.0, 5.5, -3.0], "color": "#ef4444"},
            {"name": "Eje Identitario / Self", "impact": "Sensación de vacío insoportable, metamorfosis relacional y dispersión", "tension": 0.94, "coords": [5.5, -6.0, -2.5], "color": "#f43f5e"},
            {"name": "Entorno Familiar Primario", "impact": "Agotamiento crónico de cuidadores, hiperalerta y claudicación vincular", "tension": 0.88, "coords": [-6.0, -4.5, 3.5], "color": "#fb923c"},
            {"name": "Ámbito Laboral / Académico", "impact": "Interrupción de trayectoria funcional por crisis afectivas cíclicas", "tension": 0.70, "coords": [2.0, 7.5, -3.5], "color": "#eab308"}
        ]
    },
    "TASP": {
        "title": "Trastorno Antisocial / Psicopatía",
        "subtitle": "Ablación Funcional Frontolímbica & Falla de Aversión Moral",
        "fa_uncinate": 0.08,
        "amg_activation": 0.12,
        "vmpfc_activity": 0.18,
        "acc_pain": 0.15,
        "rdoc_construct": "Sistemas de Valencia Positiva / Desensibilización Moral",
        "dti_evidence": "Craig et al. (2009) y Motzkin et al. (2011) en delincuentes psicopáticos: reducción bilateral severa de anisotropía fraccional (FA < 0.10) en el fascículo uncinado. Desconexión microestructural masiva entre la amígdala anterior y la corteza orbitofrontal.",
        "fmri_evidence": "Ausencia de activación amigdalina e insular frente al condicionamiento al miedo (Birbaumer et al.) y frente al llanto/sufrimiento ajeno (Blair et al.). Hiperactivación estriatal desinhibida frente a incentivos materiales inmediatos sin coste afectivo vicario.",
        "nodes": [
            {"id": "amg_r", "name": "Amígdala (Hipoactiva)", "x": 2.4, "y": -0.7, "z": -1.5, "mni": "[+24, -7, -15]", "color": "#1f2937", "rad": 0.35, "hz": 0.3, "status": "ATROFIA FUNCIONAL", "role": "Inmunidad al condicionamiento por castigo; ausencia de alarma autonómica."},
            {"id": "amg_l", "name": "Amígdala (Hipoactiva)", "x": -2.4, "y": -0.7, "z": -1.5, "mni": "[-24, -7, -15]", "color": "#1f2937", "rad": 0.35, "hz": 0.3, "status": "ATROFIA FUNCIONAL", "role": "Cero reactividad electrodérmica ante amenazas o castigo anticipado."},
            {"id": "vmpfc", "name": "vmPFC Moral", "x": 0.0, "y": 4.6, "z": -0.9, "mni": "[0, +46, -9]", "color": "#374151", "rad": 0.40, "hz": 0.4, "status": "HIPOCONECTADA", "role": "Incapacidad para integrar el sufrimiento de terceros en el juicio moral."},
            {"id": "accumbens", "name": "Núcleo Accumbens (Estriado)", "x": 1.3, "y": 1.5, "z": -0.8, "mni": "[+13, +15, -8]", "color": "#eab308", "rad": 1.30, "hz": 7.5, "status": "HIPEREXCITABLE", "role": "Búsqueda predatoria de recompensa y ganancia inmediata sin cálculo de daños colaterales."},
            {"id": "insula_r", "name": "Ínsula Anterior (Anestesiada)", "x": 3.9, "y": 0.7, "z": 0.1, "mni": "[+39, +7, +1]", "color": "#1f2937", "rad": 0.30, "hz": 0.2, "status": "ANESTESIA INTEROCEPTIVA", "role": "Ausencia de marcadores somáticos vicarios; carencia absoluta de culpa o remordimiento."}
        ],
        "tracts": [
            {"from": "amg_r", "to": "vmpfc", "ctrl": [3.6, 2.0, -2.5], "name": "Fascículo Uncinado (Ablación Conectómica)", "status": "broken", "desc": "Interrupción axonal casi completa. Pérdida del canal de comunicación miedo-decisión moral."},
            {"from": "vmpfc", "to": "accumbens", "ctrl": [0.7, 3.1, -0.9], "name": "Vía Córtico-Estriatal Desinhibida", "status": "hyper", "desc": "El estriado opera sin freno inhibitorio frontal, favoreciendo conductas delictivas utilitarias."}
        ],
        "ecosystem": [
            {"name": "Fuero Penal & Penitenciario", "impact": "Reincidencia delictiva, transgresión deliberada del ordenamiento legal", "tension": 0.99, "coords": [-8.0, -4.0, 2.5], "color": "#ef4444"},
            {"name": "Víctimas / Vínculos Cosificados", "impact": "Explotación económica, violencia instrumental y manipulación fría", "tension": 0.96, "coords": [7.5, 5.0, 3.0], "color": "#ef4444"},
            {"name": "Entorno Contractual / Financiero", "impact": "Fraudes, estafas y parasitismo económico sostenido", "tension": 0.88, "coords": [-5.5, 6.0, -4.0], "color": "#fb923c"},
            {"name": "Peritajes Judiciales / Salud", "impact": "Simulación deliberada de cuadros psiquiátricos para atenuar condenas", "tension": 0.65, "coords": [4.0, -6.5, -3.0], "color": "#eab308"},
            {"name": "Eje Identitario", "impact": "Egosintonía completa; ausencia de conflicto intrapsíquico primario", "tension": 0.12, "coords": [6.0, -2.0, 5.0], "color": "#10b981"}
        ]
    },
    "TNP": {
        "title": "Trastorno Narcisista de la Personalidad",
        "subtitle": "Disociación Fronto-Insular & Vulnerabilidad Fásica al Desprecio",
        "fa_uncinate": 0.46,
        "amg_activation": 1.10,
        "vmpfc_activity": 0.48,
        "acc_pain": 1.80,
        "rdoc_construct": "Sistemas Sociales / Jerarquía, Dominancia & Reconocimiento",
        "dti_evidence": "Fan et al. (2011) y Jankowiak-Siuda et al. (2015): Alteración volumétrica y conectómica en la sustancia blanca prefrontal medial y cíngulo anterior. Preservación intacta de la Teoría de la Mente cognitiva con deterioro selectivo de la empatía afectiva.",
        "fmri_evidence": "En paradigmas de crítica o exclusión: picos de activación desproporcionados en el dACC y amígdala ('herida narcisista') que desestabilizan el constructo grandioso compensatorio sostenido por la red por defecto (DMN).",
        "nodes": [
            {"id": "dacc", "name": "dACC (Radar de Jerarquía)", "x": 0.0, "y": 2.4, "z": 2.8, "mni": "[0, +24, +28]", "color": "#a855f7", "rad": 1.25, "hz": 7.4, "status": "HIPERREACTIVO AL DESPRECIO", "role": "Alarma desmedida ante la desconfirmación, la crítica o la pérdida de estatus."},
            {"id": "vmpfc", "name": "vmPFC / Polo Frontal", "x": 0.0, "y": 4.6, "z": -0.9, "mni": "[0, +46, -9]", "color": "#c084fc", "rad": 0.85, "hz": 2.8, "status": "COMPENSACIÓN GRANDIOSA", "role": "Mantenimiento activo de la imagen idealizada del self como defensa ante la fragilidad."},
            {"id": "amg_r", "name": "Amígdala (Rabia Narcisista)", "x": 2.4, "y": -0.7, "z": -1.5, "mni": "[+24, -7, -15]", "color": "#ec4899", "rad": 0.80, "hz": 5.2, "status": "VULNERABILIDAD FÁSICA", "role": "Descarga de cólera vindicativa ante la exposición pública de fallas o debilidades."},
            {"id": "insula_r", "name": "Ínsula (Desconexión Vicaria)", "x": 3.9, "y": 0.7, "z": 0.1, "mni": "[+39, +7, +1]", "color": "#374151", "rad": 0.38, "hz": 0.8, "status": "EMPATÍA AFECTIVA ATROFIADA", "role": "Incapacidad para conmoverse o registrar visceralmente el daño provocado a terceros."}
        ],
        "tracts": [
            {"from": "dacc", "to": "vmpfc", "ctrl": [0.0, 3.5, 1.0], "name": "Eje de Autoevaluación Hipervigilante", "status": "hyper", "desc": "Circuito de monitoreo constante del estatus y de la aprobación externa."},
            {"from": "amg_r", "to": "dacc", "ctrl": [1.3, 0.8, 0.9], "name": "Circuito de Ira Vindicativa", "status": "hyper", "desc": "Descarga amigdalina directa al cíngulo que alimenta la hostilidad defensiva."},
            {"from": "insula_r", "to": "vmpfc", "ctrl": [2.3, 2.6, -0.6], "name": "Desconexión Fronto-Insular", "status": "broken", "desc": "Bloqueo selectivo de la empatía emocional con preservación de la empatía cognitiva instrumental."}
        ],
        "ecosystem": [
            {"name": "Vínculo de Pareja", "impact": "Desprecio punitivo, cosificación, triangulaciones y ley del hielo", "tension": 0.92, "coords": [7.0, 4.5, 2.0], "color": "#ef4444"},
            {"name": "Autoimagen & Cohesión del Self", "impact": "Fragilidad extrema; colapso disfórico ante pérdidas objetivas de éxito", "tension": 0.96, "coords": [0.0, -7.5, -2.5], "color": "#a855f7"},
            {"name": "Ámbito Profesional / Jerárquico", "impact": "Rivalidades destructivas con pares, litigios por honra y boicot a subordinados", "tension": 0.82, "coords": [-6.5, 5.0, 3.5], "color": "#fb923c"},
            {"name": "Familia de Origen", "impact": "Exigencia de pleitesía incondicional o ruptura agresiva", "tension": 0.76, "coords": [-5.5, -5.0, 3.0], "color": "#fb923c"},
            {"name": "Consultas a Salud Mental", "impact": "Abandono prematuro de tratamiento si el terapeuta no refuerza su estatus", "tension": 0.52, "coords": [4.5, 6.5, -3.5], "color": "#38bdf8"}
        ]
    },
    "THP": {
        "title": "Trastorno Histriónico de la Personalidad",
        "subtitle": "Labilidad Afectiva, Hipersensibilidad al Refuerzo Social & Cognición Impresionista",
        "fa_uncinate": 0.60,
        "amg_activation": 1.30,
        "vmpfc_activity": 0.36,
        "acc_pain": 1.10,
        "rdoc_construct": "Sistemas de Procesos Sociales / Afiliación & Búsqueda de Refuerzo",
        "dti_evidence": "Desconexión relativa entre la corteza prefrontal dorsolateral y las cortezas temporales asociativas, facilitando un estilo cognitivo impresionista, difuso y carente de integración analítica.",
        "fmri_evidence": "Hipersensibilidad de la red de recompensa estriatal y la amígdala frente a señales interpersonales de aprobación, acompañada de amplificación somatosensorial e insular (base de los síntomas conversivos).",
        "nodes": [
            {"id": "amg_r", "name": "Amígdala Límbica", "x": 2.4, "y": -0.7, "z": -1.5, "mni": "[+24, -7, -15]", "color": "#06b6d4", "rad": 0.88, "hz": 6.2, "status": "HIPEREXCITABLE LÁBIL", "role": "Emotividad intensa y cambiante; baja tolerancia a la frustración vincular."},
            {"id": "accumbens", "name": "Núcleo Accumbens Social", "x": 1.3, "y": 1.5, "z": -0.8, "mni": "[+13, +15, -8]", "color": "#22d3ee", "rad": 1.10, "hz": 6.5, "status": "DEMANDANTE DE REFUERZO", "role": "Búsqueda continua de validación externa, halagos y protagonismo."},
            {"id": "insula_r", "name": "Ínsula Somatosensorial", "x": 3.9, "y": 0.7, "z": 0.1, "mni": "[+39, +7, +1]", "color": "#0891b2", "rad": 0.85, "hz": 5.4, "status": "SOMATIZACIÓN INTEROCEPTIVA", "role": "Conversión corporal de afectos complejos; teatralidad física y somatizaciones."},
            {"id": "vmpfc", "name": "vmPFC Impresionista", "x": 0.0, "y": 4.6, "z": -0.9, "mni": "[0, +46, -9]", "color": "#475569", "rad": 0.42, "hz": 1.4, "status": "PROCESAMIENTO DIFUSO", "role": "Déficit en el procesamiento reflexivo y secuencial de la realidad."}
        ],
        "tracts": [
            {"from": "amg_r", "to": "accumbens", "ctrl": [1.8, 0.5, -1.0], "name": "Eje Límbico-Recompensa Interpersonal", "status": "hyper", "desc": "Circuito reforzador del histrionismo relacional y la búsqueda de atención."},
            {"from": "vmpfc", "to": "amg_r", "ctrl": [1.5, 2.1, -1.2], "name": "Modulación Frontal Deficitaria", "status": "severed", "desc": "Falla del control prefrontal para modular la labilidad afectiva superficial."}
        ],
        "ecosystem": [
            {"name": "Vínculo Conyugal / Pareja", "impact": "Seducción inapropiada, celotipia y dramatismo desmedido", "tension": 0.85, "coords": [6.5, 4.0, 2.0], "color": "#ef4444"},
            {"name": "Guardia Médica General", "impact": "Consultas reiteradas por síntomas neurológicos funcionales/conversivos", "tension": 0.82, "coords": [-5.5, 6.0, -3.0], "color": "#fb923c"},
            {"name": "Círculo Social Amplio", "impact": "Relaciones superficiales asumidas como íntimas; agotamiento del entorno", "tension": 0.72, "coords": [5.0, -5.5, 3.0], "color": "#fb923c"},
            {"name": "Eje de Autoestima", "impact": "Fragilidad subjetiva dependiente en forma exclusiva de la atención ajena", "tension": 0.80, "coords": [-2.0, -6.5, -2.5], "color": "#06b6d4"},
            {"name": "Ámbito Laboral Metódico", "impact": "Baja tolerancia al esfuerzo sostenido y al anonimato en equipos de trabajo", "tension": 0.50, "coords": [2.5, 7.0, -4.0], "color": "#38bdf8"}
        ]
    }
}

# --- Sidebar de Control ---
st.sidebar.markdown("## 🧠 Consola de Neuroimagen RDoC")
diag_key = st.sidebar.selectbox("Fenotipo Clínico:", list(DATABASE.keys()), format_func=lambda k: DATABASE[k]["title"])
stress_input = st.sidebar.slider("Vector de Estrés / Factor Desencadenante:", 0.0, 1.0, 0.5, 0.05)
view_level = st.sidebar.select_slider(
    "Escala de Visualización:",
    options=["1. Neuroanatomía Pial MNI152", "2. Tractografía Conectómica DTI", "3. Onda Expansiva Sistémica (Vidas)"],
    value="2. Tractografía Conectómica DTI"
)

profile = DATABASE[diag_key]

# Cálculos biométricos dinámicos
fa_calc = max(0.04, profile["fa_uncinate"] * (1.0 - 0.45 * stress_input))
amg_calc = profile["amg_activation"] * (1.0 + 0.5 * stress_input)
pfc_calc = max(0.04, profile["vmpfc_activity"] * (1.0 - 0.5 * stress_input))
ratio_top_down = pfc_calc / amg_calc

# --- Encabezado ---
st.title(profile["title"])
st.markdown(f"**Dominio RDoC:** `{profile['rdoc_construct']}` | **Circuito:** `{profile['subtitle']}`")

c1, c2, c3, c4 = st.columns(4)
with c1:
    col = "#ef4444" if fa_calc < 0.25 else "#38bdf8"
    st.markdown(f"""<div class="metric-panel"><div class="metric-sub">Integridad Fascículo Uncinado</div><div class="metric-val" style="color: {col};">{fa_calc:.2f} FA</div></div>""", unsafe_allow_html=True)
with c2:
    st.markdown(f"""<div class="metric-panel"><div class="metric-sub">Reactividad Amígdala (fMRI)</div><div class="metric-val" style="color: {'#ef4444' if amg_calc > 1.4 else '#94a3b8'};">{amg_calc:.2f} BOLD</div></div>""", unsafe_allow_html=True)
with c3:
    st.markdown(f"""<div class="metric-panel"><div class="metric-sub">Control Prefrontal (vmPFC)</div><div class="metric-val" style="color: {'#ef4444' if pfc_calc < 0.3 else '#38bdf8'};">{pfc_calc:.2f} z</div></div>""", unsafe_allow_html=True)
with c4:
    st.markdown(f"""<div class="metric-panel"><div class="metric-sub">Ratio Inhibitorio Top-Down</div><div class="metric-val" style="color: {'#ef4444' if ratio_top_down < 0.35 else '#10b981'};">{ratio_top_down:.2f}</div></div>""", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# Motor WebGL Three.js con Fresnel Shader y Streamlines DTI
# -------------------------------------------------------------------------
engine_payload = {
    "view": view_level,
    "stress": stress_input,
    "nodes": profile["nodes"],
    "tracts": profile["tracts"],
    "social": profile["ecosystem"],
    "fa": fa_calc
}

threejs_script = f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body {{ margin: 0; overflow: hidden; background: #010409; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, monospace; }}
    #viewport {{ width: 100vw; height: 100vh; position: relative; }}
    #hud {{
      position: absolute; bottom: 24px; left: 24px; z-index: 100;
      background: rgba(13, 17, 23, 0.94); backdrop-filter: blur(14px);
      border: 1px solid #30363d; border-radius: 8px;
      padding: 16px 20px; color: #f0f6fc; max-width: 500px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.85);
    }}
    .hud-header {{ font-weight: 700; color: #58a6ff; font-size: 1.05rem; margin-bottom: 6px; }}
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
      <div id="hud-body" class="hud-text">Interactúa con el modelo 3D usando el mouse. Pasa el cursor sobre cualquier nodo o tracto para visualizar las coordenadas MNI, el estado hemodinámico y el rol fisiopatológico exacto.</div>
    </div>
    <div id="legend-box">
      <div class="leg-row"><div class="leg-pill" style="background: #ef4444; box-shadow: 0 0 8px #ef4444;"></div> Hiperactividad / Dolor Social</div>
      <div class="leg-row"><div class="leg-pill" style="background: #38bdf8; box-shadow: 0 0 8px #38bdf8;"></div> Fascículo Preservado (FA Normal)</div>
      <div class="leg-row"><div class="leg-pill" style="background: #f43f5e;"></div> Disrupción Axonal / Ruptura</div>
      <div class="leg-row"><div class="leg-pill" style="background: #1f2937;"></div> Hipoactividad / Desensibilización</div>
    </div>
  </div>

  <script>
    const DATA = {json.dumps(engine_payload)};
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

    // Luces de calibración de neuroimagen
    scene.add(new THREE.AmbientLight(0xffffff, 0.85));
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
    // MALLA PIAL BIOFIEL DEL ESPACIO MNI152 (FRESNEL GLASS CORTEX)
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

          // Cisura interhemisférica longitudinal
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
    // NÚCLEOS SUBCORTICALES EN COORDENADAS MNI152
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
      mesh.position.set(n.x, n.y, n.z);
      mesh.userData = {{ 
        name: n.name + " " + n.mni, 
        desc: "<b>Estado:</b> " + n.status + "<br><b>Función:</b> " + n.role, 
        hz: n.hz, 
        baseSize: n.rad 
      }};
      scene.add(mesh);
      clickTargets.push(mesh);
      pulsingNodes.push(mesh);
      nodeCoords[n.id] = mesh.position;

      // Halo de difusión fMRI
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
    // TRACTOGRAFÍA DTI: STREAMLINES MULTIFILAMENTO
    // -------------------------------------------------------------
    if (!DATA.view.includes("3.")) {{
      DATA.tracts.forEach(t => {{
        if (nodeCoords[t.from] && nodeCoords[t.to]) {{
          const p0 = nodeCoords[t.from];
          const p1 = nodeCoords[t.to];
          const ctrl = new THREE.Vector3(...t.ctrl);

          const isFrayed = t.status === "severed" || t.status === "broken";
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
            if (t.status === "severed" || t.status === "broken") color = 0xef4444;
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
            fiberMesh.userData = {{ name: t.name, desc: t.desc }};
            scene.add(fiberMesh);
            clickTargets.push(fiberMesh);

            // Pulsos de potenciales de acción
            if (t.status !== "broken") {{
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
        sMesh.userData = {{ name: s.name, desc: s.impact + "<br><b>Tensión de Colapso:</b> " + (s.tension * 100).toFixed(0) + "%" }};
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
          hudBody.innerHTML = target.userData.desc;
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

components.html(threejs_script, height=660, scrolling=False)

# -------------------------------------------------------------------------
# Ficha Técnica y Evidencia Clínica para la Presentación
# -------------------------------------------------------------------------
st.markdown("---")
c_left, c_right = st.columns([1.3, 1.0])

with c_left:
    st.markdown("### 🔬 Sustrato Científico y Evidencia en Neuroimagen")
    st.markdown(f"""
    <div class="evidence-card">
      <b style="color: #38bdf8;">Tractografía DTI:</b> {profile['dti_evidence']}<br><br>
      <b style="color: #38bdf8;">Resonancia Funcional (fMRI):</b> {profile['fmri_evidence']}
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    * **Fascículo Uncinado (*Uncinate Fasciculus*):** Vía de sustancia blanca de maduración tardía que conecta el polo temporal con la corteza orbitofrontal y ventromedial. Su baja anisotropía fraccional (FA) demostrada en DTI explica la persistencia de respuestas emocionales no moduladas por la lógica o el aprendizaje previo.
    * **Red de Prominencia (*Salience Network*):** La coactivación de la ínsula anterior y el dACC detecta de manera distorsionada los estímulos interpersonales, interpretando la neutralidad como abandono inminente (TLP) o como desafío de jerarquía (TNP).
    """)

with c_right:
    st.markdown("### 🌐 El Fenómeno de Onda Expansiva (Vidas Afectadas)")
    st.markdown("""
    A diferencia de la patología neurótica convencional, donde el conflicto se contiene en el ámbito subjetivo, en el **Cluster B** la falla del freno inhibitorio biológico se traslada de forma directa al tejido social:
    * **Área Vinculante:** Ruptura destructiva de lazos de apego por mecanismos de escisión (*splitting*) o manipulación instrumental.
    * **Área Sanitaria:** Frecuentación compulsiva de guardias por conductas autolesivas o descompensaciones disfóricas agudas.
    * **Área Judicial / Penal:** Colisiones constantes con la ley en personalidades antisociales o litigios narcisistas por honra y patrimonio.
    """)
