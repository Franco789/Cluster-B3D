import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="Atlas Neurobiológico & Conectómico 3D: Cluster B",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estética quirúrgica dark mode de alta precisión
st.markdown("""
<style>
    .stApp { background-color: #020617; color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, monospace; }
    h1, h2, h3 { color: #f8fafc; font-weight: 700; letter-spacing: -0.02em; }
    .biomarker-panel {
        background: #0b1329; border: 1px solid #1e293b; border-left: 3px solid #38bdf8;
        padding: 10px 14px; border-radius: 6px; margin-bottom: 8px;
    }
    .biomarker-val { font-size: 1.45rem; font-weight: 800; font-family: ui-monospace, Menlo, Consolas, monospace; }
    .biomarker-lbl { font-size: 0.70rem; text-transform: uppercase; color: #94a3b8; letter-spacing: 0.06em; }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# Base de Datos Neurobiológica y Conectómica con Citas Académicas Rigurosas
# -------------------------------------------------------------------------
CLINICAL_DATABASE = {
    "Trastorno Límite de la Personalidad (TLP)": {
        "short_key": "TLP",
        "fa_uncinate": 0.18,
        "amg_act": 1.95,
        "vmpfc_act": 0.22,
        "dacc_act": 1.90,
        "color_accent": "#ef4444",
        "circuit_name": "Hiperreactividad Límbica, Ruptura Uncinada & Alarma de Dolor Social",
        "dti_ref": "Schmahl et al. (2014, Biological Psychiatry) & New et al. (2009, NeuroImage): Desorganización microestructural con reducción severa de FA (< 0.20) en el fascículo uncinado bilateral.",
        "fmri_ref": "Eisenberger & Lieberman (2004, Science) & Ruocco et al. (2013, AJP): Coactivación paroxística de dACC e ínsula anterior ante el rechazo percibido en paradigmas Cyberball.",
        "nodes": [
            {
                "name": "Amígdala Basolateral Derecha",
                "coords": [2.3, -0.6, -1.4],
                "color": "#ef4444",
                "rad": 1.20,
                "hz": 8.0,
                "status": "HIPERTRÓFICA FÁSICA",
                "desc": "Alarma paroxística de supervivencia; traduce rostros neutros como amenazantes.",
                "voice": "Amígdala basolateral derecha. Hiperactividad fásica desregulada. Según New y colaboradores en NeuroImage 2009, existe un retraso crítico en la extinción del condicionamiento aversivo, interpretando la neutralidad afectiva como hostilidad inminente."
            },
            {
                "name": "Amígdala Basolateral Izquierda",
                "coords": [-2.3, -0.6, -1.4],
                "color": "#ef4444",
                "rad": 1.20,
                "hz": 8.0,
                "status": "HIPERTRÓFICA FÁSICA",
                "desc": "Descarga simpática autónoma inmediata ante la sospecha de distanciamiento interpersonal.",
                "voice": "Amígdala basolateral izquierda. Desencadena descargas adrenérgicas inmediatas ante señales de separación, constituyendo el sustrato biológico del terror al abandono."
            },
            {
                "name": "Córtex Prefrontal Ventromedial (vmPFC)",
                "coords": [0.0, 4.4, -0.8],
                "color": "#38bdf8",
                "rad": 0.42,
                "hz": 1.0,
                "status": "COLAPSO INHIBITORIO",
                "desc": "Falla del freno inhibitorio top-down; incapacidad de modular el afecto negativo.",
                "voice": "Corteza prefrontal ventromedial. Presenta hipofunción severa. Como demuestran Schmahl y Ruocco en el American Journal of Psychiatry, la falla de reclutamiento inhibitorio frontal anula la capacidad de mentalización durante crisis emocionales."
            },
            {
                "name": "Cíngulo Anterior Dorsal (dACC)",
                "coords": [0.0, 2.2, 2.8],
                "color": "#f43f5e",
                "rad": 1.10,
                "hz": 7.2,
                "status": "DOLOR SOCIAL AGUDO",
                "desc": "Epicentro de la Red de Prominencia; traduce la distancia vincular en angustia física.",
                "voice": "Córtex cingulado anterior dorsal. Nodo maestro de la red de prominencia. Naomi Eisenberger demostró en la revista Science que la vivencia de exclusión social activa exactamente los mismos vóxeles que el dolor físico somático agudo."
            },
            {
                "name": "Ínsula Anterior Agranular",
                "coords": [3.6, 0.8, -0.1],
                "color": "#e11d48",
                "rad": 0.95,
                "hz": 6.5,
                "status": "HIPEREXCITACIÓN INTEROCEPTIVA",
                "desc": "Sustrato neurofisiológico de la vivencia de vacío crónico y disforia visceral.",
                "voice": "Ínsula anterior agranular. Procesa la interocepción aversiva desregulada. Corresponde al correlato visceral de la vivencia subjetiva de vacío interior crónico y disforia paroxística."
            }
        ],
        "tracts": [
            {
                "from": [2.3, -0.6, -1.4], "to": [0.0, 4.4, -0.8], "ctrl": [3.4, 1.8, -2.2],
                "name": "Fascículo Uncinado Derecho",
                "status": "broken",
                "desc": "Tracto axonómico desmielinizado; pérdida de anisotropía fraccional (FA: 0.18).",
                "voice": "Fascículo uncinado derecho. La tractografía por tensor de difusión evidencia desmielinización y pérdida microestructural severa, interrumpiendo el canal de modulación prefrontal sobre el polo temporal."
            },
            {
                "from": [-2.3, -0.6, -1.4], "to": [0.0, 4.4, -0.8], "ctrl": [-3.4, 1.8, -2.2],
                "name": "Fascículo Uncinado Izquierdo",
                "status": "broken",
                "desc": "Interrupción de la conectividad recíproca amígdalo-prefrontal bilateral.",
                "voice": "Fascículo uncinado izquierdo. Presenta pérdida crítica de anisotropía fraccional documentada por Schmahl en Biological Psychiatry 2014, base estructural de la impulsividad conductual."
            },
            {
                "from": [0.0, 2.2, 2.8], "to": [0.0, 4.4, -0.8], "ctrl": [0.0, 3.4, 1.0],
                "name": "Proyección Cíngulo-Frontal",
                "status": "hyper",
                "desc": "Sobrecarga de conflicto social transmitida sin modulación prefrontal.",
                "voice": "Proyección cíngulo-frontal. Transmite sobrecarga continua de alarma afectiva hacia una corteza prefrontal incapaz de modular la respuesta conductual."
            }
        ],
        "ecosystem": [
            {"name": "Vínculo de Pareja / Apego", "desc": "Splitting, idealización vs devaluación y terror pánico al desapego.", "tension": 0.98, "coords": [7.0, 4.0, 2.0], "color": "#ef4444", "voice": "Esfera conyugal y de apego. Dominada por el mecanismo de escisión o splitting, oscilación violenta entre idealización y odio, y terror catastrófico a la separación."},
            {"name": "Guardia Médica / Urgencias", "desc": "Consultas reiteradas por gestos parasuicidas, sobredosis e impulsividad.", "tension": 0.95, "coords": [-6.5, 5.0, -2.5], "color": "#ef4444", "voice": "Servicio de urgencias. Hiperfrecuentación y saturación asistencial por conductas parasuicidas recurrentes, intoxicaciones impulsivas y microcrisis disfóricas."},
            {"name": "Sentido de Identidad / Self", "desc": "Sensación de vacío insoportable, autodifusión y fluctuación moral.", "tension": 0.94, "coords": [5.0, -5.5, -2.5], "color": "#f43f5e", "voice": "Eje identitario. Dispersión del self, vivencia intolerable de vacío crónico y labilidad severa de la autoimagen conforme al entorno."},
            {"name": "Soporte Familiar Primario", "desc": "Agotamiento de cuidadores, dinámicas de doble vínculo y claudicación.", "tension": 0.88, "coords": [-5.5, -4.0, 3.5], "color": "#fb923c", "voice": "Red familiar primaria. Agotamiento crónico de la red de cuidadores, tensión relacional permanente y claudicación del soporte afectivo."},
            {"name": "Ámbito Académico / Laboral", "desc": "Interrupción de ciclos de estudio/trabajo por crisis afectivas cíclicas.", "tension": 0.70, "coords": [2.0, 6.5, -3.5], "color": "#eab308", "voice": "Ámbito laboral y académico. Desestructuración de metas a mediano plazo por descompensaciones emocionales agudas recurrentes."}
        ]
    },
    "Trastorno Antisocial de la Personalidad (TASP)": {
        "short_key": "TASP",
        "fa_uncinate": 0.08,
        "amg_act": 0.12,
        "vmpfc_act": 0.18,
        "dacc_act": 0.15,
        "color_accent": "#f59e0b",
        "circuit_name": "Ablación Funcional Frontolímbica & Falla de Aversión Moral",
        "dti_ref": "Craig et al. (2009, Molecular Psychiatry) & Motzkin et al. (2011, J. Neuroscience): Reducción bilateral severa de FA (< 0.10) en el fascículo uncinado de poblaciones psicopáticas.",
        "fmri_ref": "Blair et al. (2004, NeuroImage) & Birbaumer et al. (2005, Arch. Gen. Psychiatry): Hipoactividad crítica de amígdala e ínsula ante estímulos de dolor ajeno o condicionamiento por castigo.",
        "nodes": [
            {
                "name": "Amígdala (Hipoactiva / Atrofiada)",
                "coords": [2.3, -0.6, -1.4],
                "color": "#1e293b",
                "rad": 0.38,
                "hz": 0.4,
                "status": "ATROFIA FUNCIONAL",
                "desc": "Inmunidad al condicionamiento por miedo o castigo; refractariedad autonómica.",
                "voice": "Amígdala hipoactiva. Craig y Blair demostraron la ausencia de respuesta hemodinámica ante expresiones faciales de terror o contingencias punitivas futuras."
            },
            {
                "name": "vmPFC (Polo Moral Desconectado)",
                "coords": [0.0, 4.4, -0.8],
                "color": "#334155",
                "rad": 0.42,
                "hz": 0.5,
                "status": "HIPOCONECTADA",
                "desc": "Juicio lógico analítico frío, pero sin integración somática del sufrimiento ajeno.",
                "voice": "Corteza prefrontal ventromedial. Desconectada de la señal autonómica amigdalina. Conduce a un razonamiento moral utilitario desprovisto de resonancia empática somática."
            },
            {
                "name": "Núcleo Accumbens (Estriado)",
                "coords": [1.3, 1.4, -0.8],
                "color": "#eab308",
                "rad": 1.25,
                "hz": 7.5,
                "status": "HIPERACTIVIDAD PREDATORIA",
                "desc": "Búsqueda insaciable de recompensa inmediata y dominancia instrumental.",
                "voice": "Núcleo accumbens estriatal. Hiperreactividad orientada a la ganancia inmediata y al control instrumental, sin cálculo de consecuencias negativas a terceros."
            },
            {
                "name": "Ínsula Anterior (Anestesiada)",
                "coords": [3.6, 0.8, -0.1],
                "color": "#1e293b",
                "rad": 0.32,
                "hz": 0.3,
                "status": "ANESTESIA INTEROCEPTIVA",
                "desc": "Carencia absoluta de culpa visceral o remordimiento somatizado.",
                "voice": "Ínsula anterior agranular anestesiada. Ausencia de marcadores viscerales de aversión o remordimiento frente a conductas transgresoras."
            }
        ],
        "tracts": [
            {
                "from": [2.3, -0.6, -1.4], "to": [0.0, 4.4, -0.8], "ctrl": [3.4, 1.8, -2.2],
                "name": "Fascículo Uncinado (Ablación Conectómica)",
                "status": "broken",
                "desc": "Interrupción casi completa del tracto microestructural (FA: 0.08).",
                "voice": "Fascículo uncinado. Demuestra ablación microestructural masiva documentada por Motzkin en el Journal of Neuroscience, suprimiendo la retroalimentación inhibitoria."
            },
            {
                "from": [0.0, 4.4, -0.8], "to": [1.3, 1.4, -0.8], "ctrl": [0.7, 3.0, -0.8],
                "name": "Vía Córtico-Estriatal Desinhibida",
                "status": "hyper",
                "desc": "El estriado opera sin freno inhibitorio frontal, facilitando conductas predatorias.",
                "voice": "Vía córtico-estriatal desinhibida. Opera sin freno frontal, facilitando la toma de decisiones orientada al beneficio instrumental exclusivo."
            }
        ],
        "ecosystem": [
            {"name": "Fuero Penal & Penitenciario", "desc": "Reiteración delictiva, crímenes patrimoniales/violentos y encarcelamiento.", "tension": 0.99, "coords": [-7.5, -3.5, 2.5], "color": "#ef4444", "voice": "Fuero penal y penitenciario. Colisión sistemática con el ordenamiento jurídico, litigios judiciales y reincidencia delictiva."},
            {"name": "Víctimas / Vínculos Explotados", "desc": "Cosificación instrumental, violencia predatoria y despojo patrimonial.", "tension": 0.96, "coords": [7.0, 4.5, 3.0], "color": "#ef4444", "voice": "Entorno vincular y víctimas. Cosificación utilitaria, violencia predatoria y manipulación interpersonal sin resonancia afectiva."},
            {"name": "Ámbito Contractual / Financiero", "desc": "Fraudes sistemáticos, estafas y ausencia de lealtad comercial.", "tension": 0.88, "coords": [-5.0, 5.5, -3.5], "color": "#fb923c", "voice": "Ámbito comercial y contractual. Fraudes reiterados, estafas premeditadas y transgresión continua de acuerdos normativos."},
            {"name": "Peritajes Médico-Legales", "desc": "Simulación calculada de trastornos mentales para eludir sanciones penales.", "tension": 0.65, "coords": [3.5, -6.0, -3.0], "color": "#eab308", "voice": "Peritajes forenses. Simulación instrumental de psicopatología para intentar eludir la imputabilidad judicial."},
            {"name": "Eje Identitario", "desc": "Egosintonía perfecta; ausencia de autocrítica o malestar interno.", "tension": 0.12, "coords": [5.5, -2.0, 4.5], "color": "#10b981", "voice": "Eje identitario. Egosintonía completa; ausencia radical de conflicto intrapsíquico o culpa subjetiva."}
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
        "dti_ref": "Fan et al. (2011, SCAN) & Nenadic et al. (2015, Psychiatry Research): Alteración estructural en la corteza insular anterior y cíngulo dorsal, preservando la cognición social fría.",
        "fmri_ref": "Pincus & Lukowitsky (2010) & Schulze et al. (2013): Picos de hiperactividad en dACC y amígdala frente a la crítica ('herida narcisista'), con reactividad vindicativa compensatoria.",
        "nodes": [
            {
                "name": "dACC (Radar de Jerarquía)",
                "coords": [0.0, 2.2, 2.8],
                "color": "#a855f7",
                "rad": 1.20,
                "hz": 7.4,
                "status": "HIPERREACTIVO AL DESPRECIO",
                "desc": "Alarma desmedida ante el desacato, la crítica o la pérdida de admiración.",
                "voice": "Cíngulo anterior dorsal. Opera como un sensor hipersensible de rango social. Cualquier indicio de crítica detona una señal paroxística de amenaza al estatus."
            },
            {
                "name": "vmPFC (Autoimagen Grandiosa)",
                "coords": [0.0, 4.4, -0.8],
                "color": "#c084fc",
                "rad": 0.85,
                "hz": 2.8,
                "status": "COMPENSACIÓN GRANDIOSA",
                "desc": "Mantenimiento activo del constructo de superioridad como defensa ante el vacío.",
                "voice": "Corteza prefrontal medial. Sostiene de forma compensatoria el relato de autosuficiencia y grandeza para proteger la extrema vulnerabilidad del self."
            },
            {
                "name": "Amígdala (Rabia Narcisista)",
                "coords": [2.3, -0.6, -1.4],
                "color": "#ec4899",
                "rad": 0.80,
                "hz": 5.2,
                "status": "VULNERABILIDAD FÁSICA",
                "desc": "Explosiones coléricas vindicativas ante la exposición de debilidad.",
                "voice": "Amígdala reactiva. Dispara respuestas fásicas de hostilidad y cólera vindicativa cuando la imagen idealizada es cuestionada públicamente."
            },
            {
                "name": "Ínsula (Desconexión Vicaria)",
                "coords": [3.6, 0.8, -0.1],
                "color": "#334155",
                "rad": 0.38,
                "hz": 0.8,
                "status": "ANESTESIA EMPÁTICA",
                "desc": "Incapacidad neurofisiológica de registrar el dolor causado a subordinados.",
                "voice": "Ínsula anterior desconectada. Fan demostró la existencia de una disociación crítica: preservación de la teoría de la mente cognitiva con anestesia de la empatía somatoafectiva."
            }
        ],
        "tracts": [
            {
                "from": [0.0, 2.2, 2.8], "to": [0.0, 4.4, -0.8], "ctrl": [0.0, 3.4, 1.0],
                "name": "Eje de Autoevaluación Hipervigilante",
                "status": "hyper",
                "desc": "Circuito de monitoreo constante del estatus y de la aprobación externa.",
                "voice": "Eje cíngulo-frontal. Monitorea permanentemente el nivel de reconocimiento externo para regular la homeostasis de la autoestima."
            },
            {
                "from": [2.3, -0.6, -1.4], "to": [0.0, 2.2, 2.8], "ctrl": [1.2, 0.7, 0.8],
                "name": "Circuito de Ira Vindicativa",
                "status": "hyper",
                "desc": "Descarga amigdalina directa al cíngulo que alimenta la hostilidad defensiva.",
                "voice": "Circuito amígdalo-cingulado. Transmite la señal de herida narcisista convirtiéndola en conductas de represalia interpersonal."
            },
            {
                "from": [3.6, 0.8, -0.1], "to": [0.0, 4.4, -0.8], "ctrl": [2.2, 2.4, -0.5],
                "name": "Desconexión Fronto-Insular",
                "status": "broken",
                "desc": "Bloqueo selectivo de la resonancia afectiva hacia el sufrimiento ajeno.",
                "voice": "Desconexión fronto-insular. Sustrato biológico del trato despersonalizado hacia personas percibidas de menor jerarquía."
            }
        ],
        "ecosystem": [
            {"name": "Vínculo de Pareja", "desc": "Cosificación, exigencia de pleitesía, humillación y ley del hielo.", "tension": 0.92, "coords": [6.5, 4.0, 2.0], "color": "#ef4444", "voice": "Relación conyugal. Exigencia de pleitesía incondicional, dinámica de devaluación y castigo mediante la ley del hielo frente a desacuerdos."},
            {"name": "Autoimagen & Cohesión del Self", "desc": "Fragilidad extrema; colapso disfórico profundo ante pérdidas de estatus.", "tension": 0.96, "coords": [0.0, -7.0, -2.5], "color": "#a855f7", "voice": "Cohesión del self. Riesgo elevado de colapso disfórico depresivo profundo cuando la fachada de éxito se quiebra de forma irrevocable."},
            {"name": "Ámbito Corporativo / Laboral", "desc": "Rivalidades destructivas, litigios por honra y boicot a colaboradores.", "tension": 0.84, "coords": [-6.0, 4.5, 3.0], "color": "#fb923c", "voice": "Ámbito corporativo y laboral. Rivalidad destructiva con pares, maltrato hacia subordinados y litigios constantes por preservación de estatus."},
            {"name": "Familia de Origen", "desc": "Exigencia de tributo incondicional o ruptura agresiva con exclusión total.", "tension": 0.76, "coords": [-5.0, -4.5, 3.0], "color": "#fb923c", "voice": "Familia de origen. Imposición de jerarquías rígidas y castigo con exclusión afectiva ante cualquier confrontación."},
            {"name": "Consultas a Salud Mental", "desc": "Abandono de psicoterapia ante señalamientos que confronten la grandiosidad.", "tension": 0.52, "coords": [4.0, 6.0, -3.0], "color": "#38bdf8", "voice": "Atención clínica. Elevada tasa de abandono terapéutico si el profesional no valida la posición de superioridad."}
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
        "dti_ref": "Buchsbaum et al. & Schore et al.: Desconexión relativa témporo-prefrontal dorsolateral, facilitando el procesamiento cognitivo impresionista y desestructurado.",
        "fmri_ref": "Somerville et al. & Vuilleumier et al.: Hiperreactividad del estriado ventral ante estímulos sociales, con amplificación somatosensorial en cuadros conversivos.",
        "nodes": [
            {
                "name": "Amígdala Límbica",
                "coords": [2.3, -0.6, -1.4],
                "color": "#06b6d4",
                "rad": 0.90,
                "hz": 6.2,
                "status": "HIPEREXCITABLE LÁBIL",
                "desc": "Emotividad intensa y cambiante; intolerancia al desinterés del entorno.",
                "voice": "Amígdala límbica lábil. Respuesta afectiva inmediata pero superficial y sujeta a rápida oscilación según el grado de atención recibida."
            },
            {
                "name": "Núcleo Accumbens Social",
                "coords": [1.3, 1.4, -0.8],
                "color": "#22d3ee",
                "rad": 1.10,
                "hz": 6.5,
                "status": "HIPERRESPUESTA AL FEEDBACK",
                "desc": "Dependencia absoluta del halago, la seducción y la validación externa.",
                "voice": "Núcleo accumbens social. Circuito de recompensa adicto a la mirada ajena, la seducción activa y el reconocimiento público constante."
            },
            {
                "name": "Ínsula Somatosensorial",
                "coords": [3.6, 0.8, -0.1],
                "color": "#0891b2",
                "rad": 0.85,
                "hz": 5.4,
                "status": "SOMATIZACIÓN INTEROCEPTIVA",
                "desc": "Conversión corporal de angustias afectivas; teatralidad física y somatizaciones.",
                "voice": "Ínsula somatosensorial. Traduce el malestar afectivo no metabolizado en manifestaciones corporales de carácter conversivo y teatral."
            },
            {
                "name": "vmPFC Impresionista",
                "coords": [0.0, 4.4, -0.8],
                "color": "#475569",
                "rad": 0.42,
                "hz": 1.4,
                "status": "PROCESAMIENTO DIFUSO",
                "desc": "Falla en el procesamiento lógico analítico; razonamiento guiado por impresiones.",
                "voice": "Corteza prefrontal medial impresionista. Procesamiento cognitivo global sin anclaje en el análisis detallado de contingencias complejas."
            }
        ],
        "tracts": [
            {
                "from": [2.3, -0.6, -1.4], "to": [1.3, 1.4, -0.8], "ctrl": [1.7, 0.4, -1.0],
                "name": "Eje Límbico-Recompensa Interpersonal",
                "status": "hyper",
                "desc": "Circuito reforzador del histrionismo relacional.",
                "voice": "Eje límbico-recompensa. Refuerza de forma condicionada las conductas de seducción y dramatización afectiva."
            },
            {
                "from": [0.0, 4.4, -0.8], "to": [2.3, -0.6, -1.4], "ctrl": [1.4, 1.9, -1.1],
                "name": "Modulación Frontal Deficitaria",
                "status": "broken",
                "desc": "Falla del control prefrontal para modular la labilidad afectiva.",
                "voice": "Modulación frontal deficitaria. Pérdida de contención inhibitoria frente a frustraciones interpersonales menores."
            }
        ],
        "ecosystem": [
            {"name": "Vínculo Conyugal / Pareja", "desc": "Seducción inapropiada, celopatía y reclamo permanente de protagonismo.", "tension": 0.85, "coords": [6.0, 3.5, 2.0], "color": "#ef4444", "voice": "Pareja. Reclamo permanente de exclusividad, conductas seductoras descontextualizadas y celotipia reactiva intensa."},
            {"name": "Guardia Médica de Emergencias", "desc": "Ingresos por síntomas neurológicos funcionales, pseudocrisis o hiperventilación.", "tension": 0.82, "coords": [-5.0, 5.5, -2.5], "color": "#fb923c", "voice": "Servicio de guardia. Consultas reiteradas por pseudocrisis no epilépticas, parestesias funcionales y cuadros conversivos agudos."},
            {"name": "Círculo Social Amplio", "desc": "Relaciones superficiales asumidas como íntimas; agotamiento del entorno.", "tension": 0.72, "coords": [4.5, -5.0, 2.5], "color": "#fb923c", "voice": "Círculo social. Idealización acelerada de vínculos superficiales y posterior desgaste del entorno por demandas afectivas continuas."},
            {"name": "Eje de Autoestima", "desc": "Sensación de desvanecimiento subjetivo ante la falta de atención o halago.", "tension": 0.80, "coords": [-1.8, -6.0, -2.0], "color": "#06b6d4", "voice": "Autoestima. Percepción de vacío y desaparición psicológica si no se cuenta con el interés manifiesto de la mirada ajena."},
            {"name": "Ámbito Laboral Metódico", "desc": "Incapacidad para labores rutinarias o sin visibilidad protagónica.", "tension": 0.50, "coords": [2.2, 6.5, -3.5], "color": "#38bdf8", "voice": "Ámbito laboral. Abandono prematuro de proyectos que exigen disciplina metódica y carecen de visibilidad protagónica."}
        ]
    }
}

# --- Sidebar de Control Clínico ---
st.sidebar.markdown("### 🎛️ Consola de Neuropsiquiatría")
selected_disorder = st.sidebar.selectbox("Entidad Patológica:", list(CLINICAL_DATABASE.keys()))
stress_slider = st.sidebar.slider("Carga de Estrés / Factor Desencadenante:", 0.0, 1.0, 0.5, 0.05)
view_selector = st.sidebar.radio("Modo de Inspección 3D:", ["1. Conectoma & Tractografía DTI", "2. Grafo de Onda Expansiva (Vidas Afectadas)"])

current_data = CLINICAL_DATABASE[selected_disorder]

# Dinámica de biomarcadores reactivos
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
    st.markdown(f"""<div class="biomarker-panel"><div class="biomarker-lbl">Integridad Fascículo Uncinado</div><div class="biomarker-val" style="color: {col};">{dyn_fa:.2f} FA</div></div>""", unsafe_allow_html=True)
with m2:
    st.markdown(f"""<div class="biomarker-panel"><div class="biomarker-lbl">Reactividad Amigdalina (fMRI)</div><div class="biomarker-val" style="color: {'#ef4444' if dyn_amg > 1.3 else '#94a3b8'};">{dyn_amg:.2f} BOLD</div></div>""", unsafe_allow_html=True)
with m3:
    st.markdown(f"""<div class="biomarker-panel"><div class="biomarker-lbl">Control Prefrontal (vmPFC)</div><div class="biomarker-val" style="color: {'#ef4444' if dyn_pfc < 0.3 else '#38bdf8'};">{dyn_pfc:.2f} z</div></div>""", unsafe_allow_html=True)
with m4:
    col_r = "#ef4444" if ratio_ctrl < 0.35 else "#10b981"
    st.markdown(f"""<div class="biomarker-panel"><div class="biomarker-lbl">Ratio Inhibitorio Top-Down</div><div class="biomarker-val" style="color: {col_r};">{ratio_ctrl:.2f}</div></div>""", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# Motor WebGL Three.js con Manejo Nativo de PointerEvents y Síntesis Vocal
# -------------------------------------------------------------------------
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
    body {{ margin: 0; overflow: hidden; background: #020617; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
    #viewport {{ width: 100vw; height: 100vh; position: relative; touch-action: none; }}
    canvas {{ width: 100% !important; height: 100% !important; display: block; outline: none; }}
    #hud {{
      position: absolute; bottom: 20px; left: 20px; z-index: 100;
      background: rgba(11, 19, 41, 0.94); backdrop-filter: blur(14px);
      border: 1px solid #1e293b; border-left: 3px solid #38bdf8; border-radius: 8px;
      padding: 16px 20px; color: #f1f5f9; max-width: 500px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.85); pointer-events: none;
    }}
    .hud-title {{ font-weight: 700; color: #38bdf8; font-size: 1.0rem; margin-bottom: 4px; font-family: monospace; }}
    .hud-desc {{ color: #94a3b8; font-size: 0.82rem; line-height: 1.45; }}
    #top-bar {{
      position: absolute; top: 20px; right: 20px; z-index: 100;
      display: flex; gap: 8px;
    }}
    .btn {{
      background: rgba(15, 23, 42, 0.9); border: 1px solid #334155; color: #cbd5e1;
      padding: 7px 14px; border-radius: 5px; font-size: 0.74rem; cursor: pointer;
      font-family: monospace; text-transform: uppercase; font-weight: 600;
    }}
    .btn:hover {{ background: #1e293b; color: #38bdf8; border-color: #38bdf8; }}
    .btn-active {{ background: #0284c7; color: #ffffff; border-color: #38bdf8; }}
    #voice-prompt {{
      position: absolute; top: 20px; left: 20px; z-index: 100;
    }}
  </style>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
</head>
<body>
  <div id="viewport">
    <div id="voice-prompt">
      <button id="voice-btn" class="btn btn-active" onclick="initVoiceSystem()">🔊 Audio Desactivado: Clic para Iniciar</button>
    </div>
    <div id="top-bar">
      <button class="btn" onclick="setCameraView('sagittal')">Sagital</button>
      <button class="btn" onclick="setCameraView('coronal')">Coronal</button>
      <button class="btn" onclick="setCameraView('axial')">Axial</button>
      <button class="btn" onclick="setCameraView('iso')">3D Libre</button>
    </div>
    <div id="hud">
      <div id="hud-head" class="hud-title">Conectoma Interactivo 3D</div>
      <div id="hud-body" class="hud-desc">1. Haz clic en "Iniciar Audio" arriba a la izquierda.<br>2. Arrastra con el ratón directamente sobre el cerebro para rotarlo en 360° o usa la rueda para zoom.<br>3. Haz clic sobre cualquier estructura para escuchar su análisis neurocientífico.</div>
    </div>
  </div>

  <script>
    const DATA = {json.dumps(payload)};
    const container = document.getElementById('viewport');

    // -------------------------------------------------------------
    // MOTOR DE VOZ CLÍNICA (WEB SPEECH API CON DESTRABE MANUAL)
    // -------------------------------------------------------------
    let voiceActive = false;
    function initVoiceSystem() {{
      voiceActive = !voiceActive;
      const b = document.getElementById('voice-btn');
      if (voiceActive) {{
        b.innerText = "🔊 Voz Científica: Activa";
        b.classList.add("btn-active");
        speakText("Motor neuro-vocal activado. Haz clic sobre cualquier núcleo o tracto para escuchar su correlato fisiopatológico.");
      }} else {{
        b.innerText = "🔇 Voz Silenciada";
        b.classList.remove("btn-active");
        if (window.speechSynthesis) window.speechSynthesis.cancel();
      }}
    }}

    function speakText(text) {{
      if (!voiceActive || !window.speechSynthesis) return;
      window.speechSynthesis.cancel();
      const utter = new SpeechSynthesisUtterance(text);
      utter.lang = 'es-ES';
      utter.rate = 1.0;
      utter.pitch = 1.0;
      window.speechSynthesis.speak(utter);
    }}

    // -------------------------------------------------------------
    // ESCENA THREE.JS
    // -------------------------------------------------------------
    const scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x020617, 0.024);

    const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.set(0, 3, 22);

    const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true, powerPreference: "high-performance" }});
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    container.appendChild(renderer.domElement);

    // Luces quirúrgicas
    scene.add(new THREE.AmbientLight(0xffffff, 0.85));
    const p1 = new THREE.PointLight(0x38bdf8, 2.5, 60);
    p1.position.set(6, 12, 14);
    scene.add(p1);

    const p2 = new THREE.PointLight(0xa855f7, 2.0, 50);
    p2.position.set(-10, -8, -10);
    scene.add(p2);

    const modelGroup = new THREE.Group();
    scene.add(modelGroup);

    // -------------------------------------------------------------
    // CONTROL TOTAL DE RATÓN (POINTER EVENTS INTRANSFERIBLES)
    // -------------------------------------------------------------
    let isPointerDown = false;
    let startX = 0, startY = 0;
    let targetRotX = 0.2, targetRotY = 0;
    let autoRotate = true;
    let isClickGesture = true;

    const canvas = renderer.domElement;

    canvas.addEventListener('pointerdown', (e) => {{
      canvas.setPointerCapture(e.pointerId);
      isPointerDown = true;
      startX = e.clientX;
      startY = e.clientY;
      autoRotate = false;
      isClickGesture = true;
    }});

    canvas.addEventListener('pointermove', (e) => {{
      if (!isPointerDown) return;
      const dx = e.clientX - startX;
      const dy = e.clientY - startY;

      if (Math.abs(dx) > 3 || Math.abs(dy) > 3) {{
        isClickGesture = false; // Fue arrastre, no clic
      }}

      targetRotY += dx * 0.007;
      targetRotX += dy * 0.007;
      startX = e.clientX;
      startY = e.clientY;
    }});

    canvas.addEventListener('pointerup', (e) => {{
      canvas.releasePointerCapture(e.pointerId);
      isPointerDown = false;
      if (isClickGesture) {{
        handleSceneClick(e);
      }}
    }});

    canvas.addEventListener('wheel', (e) => {{
      e.preventDefault();
      camera.position.z = Math.min(36, Math.max(7, camera.position.z + e.deltaY * 0.02));
    }}, {{ passive: false }});

    function setCameraView(view) {{
      autoRotate = false;
      if (view === 'sagittal') {{
        targetRotX = 0; targetRotY = Math.PI / 2; camera.position.set(24, 0, 0);
      }} else if (view === 'coronal') {{
        targetRotX = 0; targetRotY = 0; camera.position.set(0, 0, 24);
      }} else if (view === 'axial') {{
        targetRotX = Math.PI / 2; targetRotY = 0; camera.position.set(0, 24, 0);
      }} else {{
        targetRotX = 0.2; targetRotY = 0; camera.position.set(0, 3, 22);
        autoRotate = true;
      }}
      camera.lookAt(0, 0, 0);
    }}

    // -------------------------------------------------------------
    // MALLA CORTICAL ANATÓMICA (GLASS BRAIN BIOFIEL PBR)
    // -------------------------------------------------------------
    function createAnatomicalGlassCortex() {{
      const uSegs = 90, vSegs = 90;
      const geo = new THREE.BufferGeometry();
      const pos = [];

      for(let i=0; i<=uSegs; i++) {{
        let u = (i / uSegs) * Math.PI * 2;
        for(let j=0; j<=vSegs; j++) {{
          let v = (j / vSegs) * Math.PI;

          let rx = 4.4, ry = 5.8, rz = 4.1;
          // Ondulaciones calibradas según surcos piales y cisura de Silvio
          let sulci = 0.28 * Math.sin(8 * u) * Math.cos(7 * v) + 
                      0.18 * Math.sin(16 * v) * Math.cos(4 * u) +
                      0.08 * Math.sin(24 * u);

          let x = (rx + sulci) * Math.sin(v) * Math.cos(u);
          let y = (ry + sulci) * Math.sin(v) * Math.sin(u);
          let z = (rz + sulci) * Math.cos(v);

          // Cisura interhemisférica longitudinal
          if (x >= 0) x += 0.50; else x -= 0.50;
          // Curvatura polo frontal y fosa temporal
          z -= 0.08 * (y * y) / ry;

          pos.push(x, y, z);
        }}
      }}
      geo.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
      geo.computeVertexNormals();

      const mat = new THREE.MeshPhysicalMaterial({{
        color: 0x1e293b,
        emissive: 0x020617,
        roughness: 0.2,
        metalness: 0.1,
        transparent: true,
        opacity: DATA.view.includes("1.") ? 0.24 : 0.06,
        wireframe: true,
        depthWrite: false
      }});
      return new THREE.Mesh(geo, mat);
    }}

    const cortexMesh = createAnatomicalGlassCortex();
    modelGroup.add(cortexMesh);

    // -------------------------------------------------------------
    // CONSTRUCCIÓN DE NODOS Y TRACTOS
    // -------------------------------------------------------------
    const clickableObjects = [];
    const pulsingNodes = [];
    const synapticFlows = [];

    if (DATA.view.includes("1.")) {{
      // Modo Conectoma & Tractografía
      DATA.nodes.forEach(n => {{
        const geo = new THREE.SphereGeometry(n.rad, 32, 32);
        const mat = new THREE.MeshStandardMaterial({{
          color: n.color,
          emissive: n.color,
          emissiveIntensity: 1.6,
          roughness: 0.3
        }});
        const mesh = new THREE.Mesh(geo, mat);
        mesh.position.set(...n.coords);
        mesh.userData = {{
          name: n.name,
          desc: "<b>Estado:</b> " + n.status + "<br><b>Función:</b> " + n.desc,
          voice: n.voice,
          hz: n.hz
        }};
        modelGroup.add(mesh);
        clickableObjects.push(mesh);
        pulsingNodes.push(mesh);

        // Halo de activación fMRI
        const auraGeo = new THREE.SphereGeometry(n.rad * 1.45, 16, 16);
        const auraMat = new THREE.MeshBasicMaterial({{
          color: n.color,
          transparent: true,
          opacity: 0.22,
          wireframe: true
        }});
        const aura = new THREE.Mesh(auraGeo, auraMat);
        aura.position.copy(mesh.position);
        modelGroup.add(aura);
      }});

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
        tube.userData = {{
          name: t.name,
          desc: t.desc,
          voice: t.voice
        }};
        modelGroup.add(tube);
        clickableObjects.push(tube);

        // Potenciales de acción activos
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
          modelGroup.add(points);
          synapticFlows.push({{ points: points, curve: curve, speed: t.status === "hyper" ? 0.8 : 0.4 }});
        }}
      }});

    }} else {{
      // Modo Grafo de Onda Expansiva (Vidas Afectadas)
      DATA.ecosystem.forEach(e => {{
        const rad = 1.1 + e.tension * 0.55;
        const geo = new THREE.SphereGeometry(rad, 24, 24);
        const mat = new THREE.MeshStandardMaterial({{
          color: e.color,
          emissive: e.color,
          emissiveIntensity: e.tension * 2.0,
          roughness: 0.3
        }});
        const mesh = new THREE.Mesh(geo, mat);
        mesh.position.set(...e.coords);
        mesh.userData = {{
          name: e.name,
          desc: e.desc + "<br><b>Tensión Sistémica:</b> " + (e.tension * 100).toFixed(0) + "%",
          voice: e.voice
        }};
        modelGroup.add(mesh);
        clickableObjects.push(mesh);

        // Tensores de rotura
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
        modelGroup.add(new THREE.Line(lineGeo, lineMat));
      }});
    }}

    // -------------------------------------------------------------
    // RAYCASTER PARA CLIC Y DISPARO DE VOZ
    // -------------------------------------------------------------
    const raycaster = new THREE.Raycaster();
    const mouse = new THREE.Vector2();
    const hudHead = document.getElementById('hud-head');
    const hudBody = document.getElementById('hud-body');

    function handleSceneClick(event) {{
      const rect = renderer.domElement.getBoundingClientRect();
      mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
      mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

      raycaster.setFromCamera(mouse, camera);
      const hits = raycaster.intersectObjects(clickableObjects);

      if (hits.length > 0) {{
        const target = hits[0].object;
        if (target.userData && target.userData.name) {{
          hudHead.innerText = target.userData.name;
          hudBody.innerHTML = target.userData.desc;
          hudHead.style.color = "#38bdf8";
          if (target.userData.voice) {{
            speakText(target.userData.voice);
          }}
        }}
      }}
    }}

    // -------------------------------------------------------------
    // BUCLE DE RENDER CONTINUO A 60 FPS
    // -------------------------------------------------------------
    const clock = new THREE.Clock();
    function animate() {{
      requestAnimationFrame(animate);
      const t = clock.getElapsedTime();

      // Rotación suave manual o automática
      if (autoRotate) {{
        targetRotY += 0.003;
      }}
      modelGroup.rotation.y = targetRotY;
      modelGroup.rotation.x = targetRotX;

      // Pulsación senoidal en frecuencias neuronales calibradas
      pulsingNodes.forEach(mesh => {{
        const hz = mesh.userData.hz || 2.0;
        const s = 1.0 + Math.sin(t * hz) * 0.12;
        mesh.scale.set(s, s, s);
      }});

      // Movimiento continuo de partículas sobre los axones
      synapticFlows.forEach(sf => {{
        const pos = sf.points.geometry.attributes.position.array;
        const count = pos.length / 3;
        for(let i=0; i<count; i++) {{
          let progress = ((t * sf.speed) + (i / count)) % 1.0;
          let pt = sf.curve.getPoint(progress);
          pos[i*3] = pt.x;
          pos[i*3+1] = pt.y;
          pos[i*3+2] = pt.z;
        }}
        sf.points.geometry.attributes.position.needsUpdate = true;
      }});

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

components.html(html_webgl, height=660, scrolling=False)

# -------------------------------------------------------------------------
# Ficha Técnica y Evidencia Clínica para la Exposición
# -------------------------------------------------------------------------
st.markdown("---")
col_l, col_r = st.columns([1.3, 1.0])

with col_l:
    st.markdown("### 🔬 Sustrato Científico y Evidencia en Neuroimagen")
    st.markdown(f"""
    <div style="background-color: #0b1329; border-left: 4px solid #38bdf8; padding: 14px; border-radius: 4px; margin-bottom: 12px;">
      <b style="color: #38bdf8;">Tractografía DTI:</b> {current_data['dti_ref']}<br><br>
      <b style="color: #38bdf8;">Resonancia Funcional (fMRI):</b> {current_data['fmri_ref']}
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
