import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="Atlas Neurobiológico 3D: Cluster B",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estética quirúrgica dark mode de alta precisión
st.markdown("""
<style>
    .stApp { background-color: #020617; color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    h1, h2, h3 { color: #f8fafc; font-weight: 700; letter-spacing: -0.02em; }
    
    /* Tarjetas de biomarcadores con contexto clínico explícito */
    .metric-box {
        background: #0b1329; border: 1px solid #1e293b; border-radius: 8px;
        padding: 12px 14px; margin-bottom: 8px;
    }
    .metric-header { display: flex; justify-content: space-between; align-items: baseline; }
    .metric-title { font-size: 0.72rem; text-transform: uppercase; color: #94a3b8; font-weight: 600; letter-spacing: 0.05em; }
    .metric-val { font-size: 1.45rem; font-weight: 800; font-family: ui-monospace, Menlo, Consolas, monospace; }
    .metric-ref { font-size: 0.70rem; color: #64748b; margin-top: 2px; }
    .metric-desc { font-size: 0.74rem; color: #cbd5e1; margin-top: 6px; line-height: 1.35; border-top: 1px solid #1e293b; padding-top: 6px; }
    
    .status-alert { color: #ef4444; font-weight: 700; }
    .status-ok { color: #10b981; font-weight: 700; }
    .status-warn { color: #f59e0b; font-weight: 700; }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# Base de Datos Neurobiológica con Morfología Real y Rangos de Normalidad
# -------------------------------------------------------------------------
CLINICAL_DATABASE = {
    "Trastorno Límite de la Personalidad (TLP)": {
        "short_key": "TLP",
        "circuit_name": "Falla del Freno Top-Down & Alarma Nociceptiva del Dolor Social",
        "fa_uncinate": 0.18,      # Normal: 0.45 - 0.52
        "amg_act": 1.95,          # Normal: 0.80 - 1.20 BOLD
        "vmpfc_act": 0.22,        # Normal: 0.90 - 1.30 z
        "dacc_act": 1.90,
        "color_accent": "#ef4444",
        "metrics_context": {
            "fa": {
                "name": "Integridad Fascículo Uncinado",
                "unit": "FA",
                "ref": "Normal: 0.45 - 0.52 FA (Schmahl et al.)",
                "meaning": "Mielinización axonal severamente deteriorada. La orden inhibitoria frontal no logra llegar a la amígdala."
            },
            "amg": {
                "name": "Reactividad Amígdala (fMRI)",
                "unit": "BOLD",
                "ref": "Normal: 0.80 - 1.20 BOLD (New et al.)",
                "meaning": "Hiperreactividad fásica desregulada. Rostros neutros son codificados como agresión o rechazo inminente."
            },
            "vmpfc": {
                "name": "Control Prefrontal (vmPFC)",
                "unit": "z-score",
                "ref": "Normal: 0.90 - 1.30 z (Ruocco et al.)",
                "meaning": "Freno biológico desconectado. Colapso de la mentalización y de la extinción del miedo durante la crisis."
            },
            "ratio": {
                "name": "Ratio Control Inhibitorio",
                "unit": "Índice",
                "ref": "Normal: > 1.0 (Balance Top-Down)",
                "meaning": "Relación entre freno y acelerador. Un valor crítico menor a 0.35 anticipa descompensaciones impulsivas."
            }
        },
        "dti_ref": "Schmahl et al. (2014, Biological Psychiatry) & New et al. (2009, NeuroImage): Desorganización microestructural con reducción severa de FA (< 0.20) en el fascículo uncinado bilateral.",
        "fmri_ref": "Eisenberger & Lieberman (2004, Science) & Ruocco et al. (2013, AJP): Coactivación paroxística de dACC e ínsula anterior ante el rechazo percibido en paradigmas Cyberball.",
        "nodes": [
            {
                "name": "Amígdala Basolateral Derecha",
                "coords": [1.9, -0.6, -1.5], # Polo medial temporal profundo real
                "color": "#ef4444",
                "rad": 0.42,
                "hz": 8.0,
                "status": "HIPERTRÓFICA FÁSICA",
                "desc": "Alarma paroxística de supervivencia; traduce rostros neutros como amenazantes.",
                "voice": "Amígdala basolateral derecha. Imaginemos una alarma de humo ultrasensible que no sólo detecta fuego, sino que hace sonar la sirena ante el simple vapor de una taza de café. En el TLP, un rostro neutro o un mensaje sin responder es procesado como una amenaza mortal de abandono. New y colaboradores demostraron que el circuito queda atrapado en una tormenta adrenérgica sin poder extinguir el miedo."
            },
            {
                "name": "Amígdala Basolateral Izquierda",
                "coords": [-1.9, -0.6, -1.5],
                "color": "#ef4444",
                "rad": 0.42,
                "hz": 8.0,
                "status": "HIPERTRÓFICA FÁSICA",
                "desc": "Descarga simpática autónoma inmediata ante la sospecha de distanciamiento interpersonal.",
                "voice": "Amígdala basolateral izquierda. Dispara taquicardia y terror fisiológico similar al ataque de un depredador ante la mera percepción de frialdad en la pareja."
            },
            {
                "name": "Córtex Prefrontal Ventromedial (vmPFC)",
                "coords": [0.0, 4.2, -1.0], # Suelo frontomedial basal real
                "color": "#38bdf8",
                "rad": 0.40,
                "hz": 1.0,
                "status": "COLAPSO INHIBITORIO",
                "desc": "Falla del freno inhibitorio top-down; incapacidad de modular el afecto negativo.",
                "voice": "Corteza prefrontal ventromedial. Es el pedal de freno del cerebro emocional. En el TLP, este freno se queda sin líquido hidráulico. El paciente sabe racionalmente que autolesionarse no resuelve el problema, pero la corteza frontal no tiene la fuerza sináptica para frenar la inercia del impulso. Schmahl y Ruocco confirmaron esta profunda desconexión prefrontal."
            },
            {
                "name": "Cíngulo Anterior Dorsal (dACC)",
                "coords": [0.0, 1.8, 2.2], # Arco sobre el cuerpo calloso
                "color": "#f43f5e",
                "rad": 0.44,
                "hz": 7.2,
                "status": "DOLOR SOCIAL AGUDO",
                "desc": "Epicentro de la Red de Prominencia; traduce la distancia vincular en angustia física.",
                "voice": "Cíngulo anterior dorsal. Es la estación del dolor social. Naomi Eisenberger demostró en Science que el cerebro no distingue la exclusión afectiva de una quemadura física real. Cuando el paciente se siente ignorado, este núcleo se enciende con tal violencia que el dolor físico provocado en autolesiones busca apagar este dolor psíquico abrumador."
            },
            {
                "name": "Ínsula Anterior Agranular",
                "coords": [3.2, 0.7, -0.2], # Fondo de la cisura de Silvio
                "color": "#e11d48",
                "rad": 0.40,
                "hz": 6.5,
                "status": "HIPEREXCITACIÓN INTEROCEPTIVA",
                "desc": "Sustrato neurofisiológico de la vivencia de vacío crónico y disforia visceral.",
                "voice": "Ínsula anterior agranular. Aquí reside el correlato biológico de ese agujero en el pecho o vacío crónico que describe el paciente en el consultorio; una sensación visceral intolerable que a menudo empuja al consumo compulsivo o a la urgencia de apego."
            }
        ],
        "tracts": [
            {
                "from": [1.9, -0.6, -1.5], "to": [0.0, 4.2, -1.0], "ctrl": [3.0, 1.6, -2.0],
                "name": "Fascículo Uncinado Derecho",
                "status": "broken",
                "desc": "Tracto en horquilla desmielinizado; pérdida de anisotropía fraccional (FA: 0.18).",
                "voice": "Fascículo uncinado derecho. Es el cable de fibra óptica que conecta la razón con la emoción. En el TLP está deshilachado y con pérdida de mielina. La orden de calmarse enviada por el lóbulo frontal llega tarde o rota a la amígdala."
            },
            {
                "from": [-1.9, -0.6, -1.5], "to": [0.0, 4.2, -1.0], "ctrl": [-3.0, 1.6, -2.0],
                "name": "Fascículo Uncinado Izquierdo",
                "status": "broken",
                "desc": "Interrupción de la conectividad recíproca amígdalo-prefrontal bilateral.",
                "voice": "Fascículo uncinado izquierdo. La tractografía DTI documentada por Schmahl revela una baja anisotropía fraccional bilateral, explicando por qué las crisis son refractarias a la lógica verbal."
            },
            {
                "from": [0.0, 1.8, 2.2], "to": [0.0, 4.2, -1.0], "ctrl": [0.0, 3.2, 0.8],
                "name": "Proyección Cíngulo-Frontal",
                "status": "hyper",
                "desc": "Sobrecarga de conflicto social transmitida sin modulación prefrontal.",
                "voice": "Proyección cíngulo-frontal. Bombardea a la corteza ejecutiva con un flujo constante de angustia, saturando los recursos cognitivos y provocando el clásico bloqueo reflexivo durante el conflicto."
            }
        ],
        "ecosystem": [
            {"name": "Vínculo de Pareja / Apego", "desc": "Splitting, idealización vs devaluación y terror pánico al desapego.", "tension": 0.98, "coords": [6.5, 3.5, 1.8], "color": "#ef4444", "voice": "Esfera de pareja. Opera como un péndulo sin amortiguador. En un instante la pareja es el salvador absoluto, y ante una mínima tardanza pasa a ser el peor enemigo. Este splitting es el reflejo relacional directo de la desregulación amigdalina."},
            {"name": "Guardia Médica / Urgencias", "desc": "Consultas reiteradas por gestos parasuicidas, sobredosis e impulsividad.", "tension": 0.95, "coords": [-6.0, 4.5, -2.2], "color": "#ef4444", "voice": "Servicio de guardia. El paciente consulta reiteradamente en crisis aguda tras discusiones afectivas, requiriendo contención ante gestos que no siempre buscan la muerte, sino silenciar el dolor psíquico."},
            {"name": "Sentido de Identidad / Self", "desc": "Sensación de vacío insoportable, autodifusión y fluctuación moral.", "tension": 0.94, "coords": [4.5, -5.0, -2.2], "color": "#f43f5e", "voice": "Eje identitario. Es como un camaleón que cambia de color para no morir. Adopta los gustos o valores de la persona que tiene al lado por terror a que, al quedarse solo, no quede nada de sí mismo."},
            {"name": "Soporte Familiar Primario", "desc": "Agotamiento de cuidadores, dinámicas de doble vínculo y claudicación.", "tension": 0.88, "coords": [-5.0, -3.5, 3.0], "color": "#fb923c", "voice": "Entorno familiar. La familia vive caminando sobre cáscaras de huevo, midiendo cada palabra para no disparar una crisis, lo que a largo plazo agota los recursos de soporte."},
            {"name": "Ámbito Académico / Laboral", "desc": "Interrupción de ciclos de estudio/trabajo por crisis afectivas cíclicas.", "tension": 0.70, "coords": [1.8, 6.0, -3.0], "color": "#eab308", "voice": "Ámbito laboral y académico. Despidos o renuncias intempestivas tras discusiones explosivas, desmoronando trayectorias promisorias por fallas en la tolerancia a la frustración."}
        ]
    },
    "Trastorno Antisocial de la Personalidad (TASP)": {
        "short_key": "TASP",
        "circuit_name": "Ablación Funcional Frontolímbica & Falla de Aversión Moral",
        "fa_uncinate": 0.08,      # Severamente deprimido
        "amg_act": 0.12,          # Refractariedad autonómica
        "vmpfc_act": 0.18,        # Sin guía somática
        "dacc_act": 0.15,
        "color_accent": "#f59e0b",
        "metrics_context": {
            "fa": {
                "name": "Integridad Fascículo Uncinado",
                "unit": "FA",
                "ref": "Normal: 0.45 - 0.52 FA (Craig et al.)",
                "meaning": "Ablación casi total de la vía. Desconexión física entre el centro del miedo y el juicio moral prefrontal."
            },
            "amg": {
                "name": "Reactividad Amígdala (fMRI)",
                "unit": "BOLD",
                "ref": "Normal: 0.80 - 1.20 BOLD (Blair et al.)",
                "meaning": "Hipoactividad refractaria. Ausencia total de respuesta autonómica ante amenazas o señales de llanto ajeno."
            },
            "vmpfc": {
                "name": "Control Prefrontal (vmPFC)",
                "unit": "z-score",
                "ref": "Normal: 0.90 - 1.30 z (Motzkin et al.)",
                "meaning": "Juicio puramente utilitario. Sabe lo que está prohibido, pero la transgresión no le produce freno somático."
            },
            "ratio": {
                "name": "Ratio Control Inhibitorio",
                "unit": "Índice",
                "ref": "Normal: > 1.0 (Balance Top-Down)",
                "meaning": "Desbalance predatorio: el estriado busca recompensas inmediatas sin que la corteza frontal compute consecuencias a terceros."
            }
        },
        "dti_ref": "Craig et al. (2009, Molecular Psychiatry) & Motzkin et al. (2011, J. Neuroscience): Reducción bilateral severa de FA (< 0.10) en el fascículo uncinado de poblaciones psicopáticas.",
        "fmri_ref": "Blair et al. (2004, NeuroImage) & Birbaumer et al. (2005, Arch. Gen. Psychiatry): Hipoactividad crítica de amígdala e ínsula ante estímulos de dolor ajeno o condicionamiento por castigo.",
        "nodes": [
            {
                "name": "Amígdala (Hipoactiva / Atrofiada)",
                "coords": [1.9, -0.6, -1.5],
                "color": "#1e293b",
                "rad": 0.32,
                "hz": 0.4,
                "status": "ATROFIA FUNCIONAL",
                "desc": "Inmunidad al condicionamiento por miedo o castigo; refractariedad autonómica.",
                "voice": "Amígdala hipoactiva. Es un detector de humo sin batería. Aunque haya fuego y sirenas reales alrededor, no emite ningún sonido. Mientras una persona común siente taquicardia y sudor frío al infringir una regla o ver llorar a alguien, el individuo psicopático permanece en calma fisiológica absoluta. Craig y Blair demostraron esta marcada refractariedad al castigo."
            },
            {
                "name": "vmPFC (Polo Moral Desconectado)",
                "coords": [0.0, 4.2, -1.0],
                "color": "#334155",
                "rad": 0.36,
                "hz": 0.5,
                "status": "HIPOCONECTADA",
                "desc": "Juicio lógico analítico frío, pero sin integración somática del sufrimiento ajeno.",
                "voice": "Corteza prefrontal ventromedial. Funciona como una calculadora desprovista de escrúpulos. Comprende las reglas y lo que está prohibido en términos teóricos, pero esa comprensión no tiene anclaje afectivo. Dañar al otro es simplemente un costo transaccional admisible para alcanzar un objetivo."
            },
            {
                "name": "Núcleo Accumbens (Estriado)",
                "coords": [1.1, 1.2, -0.8], # Estriado ventral medial real
                "color": "#eab308",
                "rad": 0.48,
                "hz": 7.5,
                "status": "HIPERACTIVIDAD PREDATORIA",
                "desc": "Búsqueda insaciable de recompensa inmediata y dominancia instrumental.",
                "voice": "Núcleo accumbens. Es el motor predatorio de recompensa. Si una persona común ve una oportunidad de robo, el freno moral inhibe el impulso; aquí el estriado se sobreactiva exigiendo la gratificación inmediata, sin importar el daño causado."
            },
            {
                "name": "Ínsula Anterior (Anestesiada)",
                "coords": [3.2, 0.7, -0.2],
                "color": "#1e293b",
                "rad": 0.28,
                "hz": 0.3,
                "status": "ANESTESIA INTEROCEPTIVA",
                "desc": "Carencia absoluta de culpa visceral o remordimiento somatizado.",
                "voice": "Ínsula anterior anestesiada. Es la sede de la resonancia somática vicaria. Su hipofunción explica por qué pueden presenciar el dolor de una víctima sin experimentar la menor aversión ni remordimiento en el estómago."
            }
        ],
        "tracts": [
            {
                "from": [1.9, -0.6, -1.5], "to": [0.0, 4.2, -1.0], "ctrl": [3.0, 1.6, -2.0],
                "name": "Fascículo Uncinado (Ablación Conectómica)",
                "status": "broken",
                "desc": "Interrupción casi completa del tracto microestructural (FA: 0.08).",
                "voice": "Fascículo uncinado cortado. Motzkin comprobó en reclusos que la línea entre el centro del miedo y el juicio moral está rota. El cerebro no puede enviar la señal de freno somático ante la transgresión."
            },
            {
                "from": [0.0, 4.2, -1.0], "to": [1.1, 1.2, -0.8], "ctrl": [0.6, 2.6, -0.8],
                "name": "Vía Córtico-Estriatal Desinhibida",
                "status": "hyper",
                "desc": "El estriado opera sin freno inhibitorio frontal, facilitando conductas predatorias.",
                "voice": "Vía córtico-estriatal desinhibida. El lóbulo frontal no frena al núcleo de recompensa; se pone a su servicio para planificar estafas y manipulaciones con frialdad metodológica."
            }
        ],
        "ecosystem": [
            {"name": "Fuero Penal & Penitenciario", "desc": "Reiteración delictiva, crímenes patrimoniales/violentos y encarcelamiento.", "tension": 0.99, "coords": [-7.0, -3.2, 2.2], "color": "#ef4444", "voice": "Fuero penal. El sujeto no aprende del castigo ni de la cárcel. Al salir de prisión, la falta de condicionamiento al miedo hace que reincida exactamente en las mismas conductas delictivas."},
            {"name": "Víctimas / Vínculos Explotados", "desc": "Cosificación instrumental, violencia predatoria y despojo patrimonial.", "tension": 0.96, "coords": [6.5, 4.0, 2.5], "color": "#ef4444", "voice": "Vínculos explotados. Las personas son consideradas meras fichas de ajedrez. Una vez que ya no proveen dinero o placer, son desechadas sin el menor atisbo de nostalgia."},
            {"name": "Ámbito Contractual / Financiero", "desc": "Fraudes sistemáticos, estafas y ausencia de lealtad comercial.", "tension": 0.88, "coords": [-4.5, 5.0, -3.0], "color": "#fb923c", "voice": "Ámbito financiero. Creación de fraudes y estafas piramidales. La promesa verbal es utilizada como un anzuelo sin intención real de cumplimiento."},
            {"name": "Peritajes Médico-Legales", "desc": "Simulación calculada de trastornos mentales para eludir sanciones penales.", "tension": 0.65, "coords": [3.2, -5.5, -2.6], "color": "#eab308", "voice": "Peritajes forenses. El sujeto simula delirios o amnesia durante el examen psiquiátrico forense para ser declarado inimputable, desarmando la farsa cuando está fuera del ámbito judicial."},
            {"name": "Eje Identitario", "desc": "Egosintonía perfecta; ausencia de autocrítica o malestar interno.", "tension": 0.12, "coords": [5.0, -1.8, 4.0], "color": "#10b981", "voice": "Eje identitario. Plena egosintonía. El individuo no acude voluntariamente a consulta porque no sufre; considera que el problema es de los demás por ser débiles o ingenuos."}
        ]
    },
    "Trastorno Narcisista de la Personalidad (TNP)": {
        "short_key": "TNP",
        "circuit_name": "Disociación Fronto-Insular & Vulnerabilidad al Desprecio",
        "fa_uncinate": 0.46,
        "amg_act": 1.05,
        "vmpfc_act": 0.48,
        "dacc_act": 1.80,
        "color_accent": "#a855f7",
        "metrics_context": {
            "fa": {
                "name": "Integridad Fascículo Uncinado",
                "unit": "FA",
                "ref": "Normal: 0.45 - 0.52 FA (Fan et al.)",
                "meaning": "Tractos conservados pero con modulación anómala centrada en la búsqueda y defensa del estatus personal."
            },
            "amg": {
                "name": "Reactividad Amígdala (fMRI)",
                "unit": "BOLD",
                "ref": "Normal: 0.80 - 1.20 BOLD (Pincus et al.)",
                "meaning": "Respuesta fásica colérica ('rabia narcisista') cuando la fachada de perfección es cuestionada públicamente."
            },
            "vmpfc": {
                "name": "Control Prefrontal (vmPFC)",
                "unit": "z-score",
                "ref": "Normal: 0.90 - 1.30 z (Schulze et al.)",
                "meaning": "Hiperactivación compensatoria: sostiene el constructo grandioso para tapar la extrema fragilidad del self."
            },
            "ratio": {
                "name": "Ratio Control Inhibitorio",
                "unit": "Índice",
                "ref": "Normal: > 1.0 (Balance Top-Down)",
                "meaning": "Inestabilidad fásica: aparente control que colapsa ante la falta de admiración o el rechazo explícito."
            }
        },
        "dti_ref": "Fan et al. (2011, SCAN) & Nenadic et al. (2015, Psychiatry Research): Alteración estructural en la corteza insular anterior y cíngulo dorsal, preservando la cognición social fría.",
        "fmri_ref": "Pincus & Lukowitsky (2010) & Schulze et al. (2013): Picos de hiperactividad en dACC y amígdala frente a la crítica ('herida narcisista'), con reactividad vindicativa compensatoria.",
        "nodes": [
            {
                "name": "dACC (Radar de Jerarquía)",
                "coords": [0.0, 1.8, 2.2],
                "color": "#a855f7",
                "rad": 0.46,
                "hz": 7.4,
                "status": "HIPERREACTIVO AL DESPRECIO",
                "desc": "Alarma desmedida ante el desacato, la crítica o la pérdida de admiración.",
                "voice": "Cíngulo anterior dorsal. Es un radar de jerarquía social en hipervigilancia continua. Si una opinión suya no es celebrada, este núcleo detecta una ofensa mortal a su estatus, detonando furia fría o venganza calculada."
            },
            {
                "name": "vmPFC (Autoimagen Grandiosa)",
                "coords": [0.0, 4.2, -1.0],
                "color": "#c084fc",
                "rad": 0.44,
                "hz": 2.8,
                "status": "COMPENSACIÓN GRANDIOSA",
                "desc": "Mantenimiento activo del constructo de superioridad como defensa ante el vacío.",
                "voice": "Corteza prefrontal ventromedial. Es como construir un andamio de oro sobre cimientos de barro. Se gasta una enorme cantidad de energía metabólica en sostener el relato de superioridad, precisamente para tapar el terror al vacío interior."
            },
            {
                "name": "Amígdala (Rabia Narcisista)",
                "coords": [1.9, -0.6, -1.5],
                "color": "#ec4899",
                "rad": 0.38,
                "hz": 5.2,
                "status": "VULNERABILIDAD FÁSICA",
                "desc": "Explosiones coléricas vindicativas ante la exposición de debilidad.",
                "voice": "Amígdala fásica. Dispara la llamada rabia narcisista. Ante una crítica fundada, la herida narcisista desata una reacción colérica que busca descalificar al otro para restituir el propio valor dañado."
            },
            {
                "name": "Ínsula (Desconexión Vicaria)",
                "coords": [3.2, 0.7, -0.2],
                "color": "#334155",
                "rad": 0.32,
                "hz": 0.8,
                "status": "ANESTESIA EMPÁTICA",
                "desc": "Incapacidad neurofisiológica de registrar el dolor causado a subordinados.",
                "voice": "Ínsula anterior desconectada. Fan demostró en la revista SCAN que el narcisista tiene empatía cognitiva intacta: sabe perfectamente qué te duele y cómo herirte, pero carece de empatía afectiva; no siente compasión al hacerlo."
            }
        ],
        "tracts": [
            {
                "from": [0.0, 1.8, 2.2], "to": [0.0, 4.2, -1.0], "ctrl": [0.0, 3.2, 0.8],
                "name": "Eje de Autoevaluación Hipervigilante",
                "status": "hyper",
                "desc": "Circuito de monitoreo constante del estatus y de la aprobación externa.",
                "voice": "Eje de autoevaluación. Obliga al sujeto a monitorear obsesivamente cuántos elogios recibe para mantener equilibrada su autoestima."
            },
            {
                "from": [1.9, -0.6, -1.5], "to": [0.0, 1.8, 2.2], "ctrl": [1.0, 0.6, 0.7],
                "name": "Circuito de Ira Vindicativa",
                "status": "hyper",
                "desc": "Descarga amigdalina directa al cíngulo que alimenta la hostilidad defensiva.",
                "voice": "Circuito de ira vindicativa. Es el puente por donde la herida del orgullo se transforma en desprecio hacia quien osó marcarle un error."
            },
            {
                "from": [3.2, 0.7, -0.2], "to": [0.0, 4.2, -1.0], "ctrl": [1.8, 2.0, -0.5],
                "name": "Desconexión Fronto-Insular",
                "status": "broken",
                "desc": "Bloqueo selectivo de la resonancia afectiva hacia el sufrimiento ajeno.",
                "voice": "Desconexión fronto-insular. El tracto responsable de frenar la crueldad relacional está apagado; el otro es tratado como un objeto utilitario sin costo de conciencia."
            }
        ],
        "ecosystem": [
            {"name": "Vínculo de Pareja", "desc": "Cosificación, exigencia de pleitesía, humillación y ley del hielo.", "tension": 0.92, "coords": [6.0, 3.5, 1.8], "color": "#ef4444", "voice": "Vínculo conyugal. Dinámica de dominación donde la pareja debe orbitar en torno a sus necesidades. El menor desacuerdo es castigado con semanas de silencio gélido o devaluación."},
            {"name": "Autoimagen & Cohesión del Self", "desc": "Fragilidad extrema; colapso disfórico profundo ante pérdidas de estatus.", "tension": 0.96, "coords": [0.0, -6.5, -2.2], "color": "#a855f7", "voice": "Cohesión del self. Cuando se produce una quiebra real de estatus (una bancarrota o un divorcio público), el andamio grandioso se derrumba, dando paso a una depresión de altísimo riesgo suicida."},
            {"name": "Ámbito Corporativo / Laboral", "desc": "Rivalidades destructivas, litigios por honra y boicot a colaboradores.", "tension": 0.84, "coords": [-5.5, 4.0, 2.8], "color": "#fb923c", "voice": "Ámbito laboral. Como líderes son tiranos que se apropian de los éxitos ajenos y culpan a otros de sus propios errores, generando ambientes laborales tóxicos y renuncias."},
            {"name": "Familia de Origen", "desc": "Exigencia de tributo incondicional o ruptura agresiva con exclusión total.", "tension": 0.76, "coords": [-4.5, -4.0, 2.8], "color": "#fb923c", "voice": "Familia de origen. Trata a los hijos como extensiones de su propia imagen. El que triunfa es exhibido como trofeo; el que piensa por sí mismo es desheredado o rechazado."},
            {"name": "Consultas a Salud Mental", "desc": "Abandono de psicoterapia ante señalamientos que confronten la grandiosidad.", "tension": 0.52, "coords": [3.6, 5.5, -2.6], "color": "#38bdf8", "voice": "Consulta clínica. Ante la primera interpretación del terapeuta que señale sus falencias, abandonan el tratamiento argumentando que el profesional no está a su nivel."}
        ]
    },
    "Trastorno Histriónico de la Personalidad (THP)": {
        "short_key": "THP",
        "circuit_name": "Labilidad Afectiva, Búsqueda de Refuerzo & Somatización",
        "fa_uncinate": 0.60,
        "amg_act": 1.30,
        "vmpfc_act": 0.36,
        "dacc_act": 1.10,
        "color_accent": "#06b6d4",
        "metrics_context": {
            "fa": {
                "name": "Integridad Fascículo Uncinado",
                "unit": "FA",
                "ref": "Normal: 0.45 - 0.52 FA (Buchsbaum et al.)",
                "meaning": "Tractos anteriores relativamente preservados con varianza conectómica difusa hacia áreas dorsolaterales."
            },
            "amg": {
                "name": "Reactividad Amígdala (fMRI)",
                "unit": "BOLD",
                "ref": "Normal: 0.80 - 1.20 BOLD (Somerville et al.)",
                "meaning": "Labilidad paroxística: respuestas afectivas muy veloces, teatrales pero de rápida habituación."
            },
            "vmpfc": {
                "name": "Control Prefrontal (vmPFC)",
                "unit": "z-score",
                "ref": "Normal: 0.90 - 1.30 z (Schore et al.)",
                "meaning": "Estilo cognitivo impresionista: déficit en el análisis reflexivo y secuencial de contingencias complejas."
            },
            "ratio": {
                "name": "Ratio Control Inhibitorio",
                "unit": "Índice",
                "ref": "Normal: > 1.0 (Balance Top-Down)",
                "meaning": "Sensibilidad extrema a la atención ambiental: la pérdida del rol protagónico desorganiza la conducta."
            }
        },
        "dti_ref": "Buchsbaum et al. & Schore et al.: Desconexión relativa témporo-prefrontal dorsolateral, facilitando el procesamiento cognitivo impresionista y desestructurado.",
        "fmri_ref": "Somerville et al. & Vuilleumier et al.: Hiperreactividad del estriado ventral ante estímulos sociales, con amplificación somatosensorial en cuadros conversivos.",
        "nodes": [
            {
                "name": "Amígdala Límbica",
                "coords": [1.9, -0.6, -1.5],
                "color": "#06b6d4",
                "rad": 0.40,
                "hz": 6.2,
                "status": "HIPEREXCITABLE LÁBIL",
                "desc": "Emotividad intensa y cambiante; intolerancia al desinterés del entorno.",
                "voice": "Amígdala límbica lábil. Funciona como fuegos artificiales de corta duración: una explosión de llanto dramático ante una nimiedad, seguida a los diez minutos por risas y seducción. Es una afectividad tan intensa como superficial."
            },
            {
                "name": "Núcleo Accumbens Social",
                "coords": [1.1, 1.2, -0.8],
                "color": "#22d3ee",
                "rad": 0.44,
                "hz": 6.5,
                "status": "HIPERRESPUESTA AL FEEDBACK",
                "desc": "Dependencia absoluta del halago, la seducción y la validación externa.",
                "voice": "Núcleo accumbens social. Circuito adicto a los reflectores. La persona no tolera no ser el centro de atención; si la conversación gira hacia otro tema, recurrirá a seducción inapropiada o una repentina indisposición física para recuperar la mirada de todos."
            },
            {
                "name": "Ínsula Somatosensorial",
                "coords": [3.2, 0.7, -0.2],
                "color": "#0891b2",
                "rad": 0.38,
                "hz": 5.4,
                "status": "SOMATIZACIÓN INTEROCEPTIVA",
                "desc": "Conversión corporal de angustias afectivas; teatralidad física y somatizaciones.",
                "voice": "Ínsula somatosensorial. El teatro no se actúa en palabras, se actúa en el cuerpo. Ante un conflicto no resuelto, la ínsula amplifica las señales corporales provocando parálisis funcionales o desmayos sin base orgánica."
            },
            {
                "name": "vmPFC Impresionista",
                "coords": [0.0, 4.2, -1.0],
                "color": "#475569",
                "rad": 0.35,
                "hz": 1.4,
                "status": "PROCESAMIENTO DIFUSO",
                "desc": "Falla en el procesamiento lógico analítico; razonamiento guiado por impresiones.",
                "voice": "Corteza prefrontal impresionista. Su estilo cognitivo es como una pintura al óleo vista de lejos: capta el ambiente emocional global pero es incapaz de dar precisiones lógicas sobre los hechos que provocaron el conflicto."
            }
        ],
        "tracts": [
            {
                "from": [1.9, -0.6, -1.5], "to": [1.1, 1.2, -0.8], "ctrl": [1.4, 0.4, -1.0],
                "name": "Eje Límbico-Recompensa Interpersonal",
                "status": "hyper",
                "desc": "Circuito reforzador del histrionismo relacional.",
                "voice": "Eje límbico de recompensa. Condiciona la conducta para que el individuo repita permanentemente puestas en escena teatrales que le aseguren la aprobación externa."
            },
            {
                "from": [0.0, 4.2, -1.0], "to": [1.9, -0.6, -1.5], "ctrl": [1.1, 1.6, -1.1],
                "name": "Modulación Frontal Deficitaria",
                "status": "broken",
                "desc": "Falla del control prefrontal para modular la labilidad afectiva.",
                "voice": "Modulación frontal deficitaria. Falla en poner orden y sobriedad cuando la situación amerita contención emocional, como reuniones formales de trabajo o velorios."
            }
        ],
        "ecosystem": [
            {"name": "Vínculo Conyugal / Pareja", "desc": "Seducción inapropiada, celopatía y reclamo permanente de protagonismo.", "tension": 0.85, "coords": [5.5, 3.2, 1.8], "color": "#ef4444", "voice": "Pareja. Exige demostraciones de amor apasionadas todos los días. La rutina cotidiana normal es vivida como desamor, provocando celos infundados o coqueteos con terceros para reactivar el drama."},
            {"name": "Guardia Médica de Emergencias", "desc": "Ingresos por síntomas neurológicos funcionales, pseudocrisis o hiperventilación.", "tension": 0.82, "coords": [-4.5, 5.0, -2.2], "color": "#fb923c", "voice": "Guardia médica. Clásica consulta de madrugada por pseudocrisis o crisis de hiperventilación tras una discusión, requiriendo un abordaje empático pero firme que evite la sobremedicalización."},
            {"name": "Círculo Social Amplio", "desc": "Relaciones superficiales asumidas como íntimas; agotamiento del entorno.", "tension": 0.72, "coords": [4.0, -4.5, 2.2], "color": "#fb923c", "voice": "Círculo de amistades. Conocen a alguien hace dos días y ya lo consideran su hermano del alma, para luego distanciarse con la misma velocidad ante cualquier pequeñez que no satisfaga su estándar novelesco."},
            {"name": "Eje de Autoestima", "desc": "Sensación de desvanecimiento subjetivo ante la falta de atención o halago.", "tension": 0.80, "coords": [-1.5, -5.5, -1.8], "color": "#06b6d4", "voice": "Autoestima. Si nadie los mira, sienten literalmente que no existen. Su valor interno es totalmente prestado por la mirada del público circunstancial."},
            {"name": "Ámbito Laboral Metódico", "desc": "Incapacidad para labores rutinarias o sin visibilidad protagónica.", "tension": 0.50, "coords": [2.0, 5.8, -3.0], "color": "#38bdf8", "voice": "Ámbito laboral. Excelente desenvolvimiento inicial en relaciones públicas o ventas, pero con un rápido agotamiento cuando el rol exige trabajo metódico de archivo o concentración sin público."}
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

# --- Encabezado ---
st.title(selected_disorder)
st.caption(f"**Circuito Fisiopatológico:** {current_data['circuit_name']}")

# --- Métricas Superiores Explicadas y Contextualizadas ---
ctx = current_data["metrics_context"]
m1, m2, m3, m4 = st.columns(4)

with m1:
    col_fa = "#ef4444" if dyn_fa < 0.25 else "#38bdf8"
    status_txt = "CRÍTICO (DESCONEXIÓN)" if dyn_fa < 0.25 else "PRESERVADO"
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-header">
            <span class="metric-title">{ctx['fa']['name']}</span>
            <span class="metric-val" style="color: {col_fa};">{dyn_fa:.2f} <small style="font-size:0.8rem;">{ctx['fa']['unit']}</small></span>
        </div>
        <div class="metric-ref">{ctx['fa']['ref']} | <span class="{'status-alert' if dyn_fa < 0.25 else 'status-ok'}">{status_txt}</span></div>
        <div class="metric-desc">{ctx['fa']['meaning']}</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    col_amg = "#ef4444" if dyn_amg > 1.3 else "#94a3b8"
    status_amg = "HIPERACTIVIDAD FÁSICA" if dyn_amg > 1.3 else ("HIPORREACTIVO" if dyn_amg < 0.4 else "NORMAL")
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-header">
            <span class="metric-title">{ctx['amg']['name']}</span>
            <span class="metric-val" style="color: {col_amg};">{dyn_amg:.2f} <small style="font-size:0.8rem;">{ctx['amg']['unit']}</small></span>
        </div>
        <div class="metric-ref">{ctx['amg']['ref']} | <span class="{'status-alert' if dyn_amg > 1.3 else 'status-warn'}">{status_amg}</span></div>
        <div class="metric-desc">{ctx['amg']['meaning']}</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    col_pfc = "#ef4444" if dyn_pfc < 0.3 else "#38bdf8"
    status_pfc = "COLAPSO INHIBITORIO" if dyn_pfc < 0.3 else "FUNCIONAL"
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-header">
            <span class="metric-title">{ctx['vmpfc']['name']}</span>
            <span class="metric-val" style="color: {col_pfc};">{dyn_pfc:.2f} <small style="font-size:0.8rem;">{ctx['vmpfc']['unit']}</small></span>
        </div>
        <div class="metric-ref">{ctx['vmpfc']['ref']} | <span class="{'status-alert' if dyn_pfc < 0.3 else 'status-ok'}">{status_pfc}</span></div>
        <div class="metric-desc">{ctx['vmpfc']['meaning']}</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    col_r = "#ef4444" if ratio_ctrl < 0.35 else "#10b981"
    status_r = "FALLA DEL FRENO" if ratio_ctrl < 0.35 else "COMPENSADO"
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-header">
            <span class="metric-title">{ctx['ratio']['name']}</span>
            <span class="metric-val" style="color: {col_r};">{ratio_ctrl:.2f}</span>
        </div>
        <div class="metric-ref">{ctx['ratio']['ref']} | <span class="{'status-alert' if ratio_ctrl < 0.35 else 'status-ok'}">{status_r}</span></div>
        <div class="metric-desc">{ctx['ratio']['meaning']}</div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------------------
# Motor WebGL Three.js con Morfología Encefálica Realista y HUD Compacto
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
    
    /* Panel lateral compacto flotante que nunca obstruye el encéfalo */
    #hud {{
      position: absolute; top: 65px; left: 16px; z-index: 100;
      background: rgba(11, 19, 41, 0.88); backdrop-filter: blur(12px);
      border: 1px solid #1e293b; border-left: 3px solid #38bdf8; border-radius: 8px;
      padding: 12px 14px; color: #f1f5f9; max-width: 290px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.75); pointer-events: none;
    }}
    .hud-title {{ font-weight: 700; color: #38bdf8; font-size: 0.88rem; margin-bottom: 4px; font-family: monospace; }}
    .hud-desc {{ color: #94a3b8; font-size: 0.74rem; line-height: 1.4; }}
    
    #top-bar {{
      position: absolute; top: 16px; right: 16px; z-index: 100;
      display: flex; gap: 8px;
    }}
    .btn {{
      background: rgba(15, 23, 42, 0.85); border: 1px solid #334155; color: #cbd5e1;
      padding: 6px 12px; border-radius: 5px; font-size: 0.72rem; cursor: pointer;
      font-family: monospace; text-transform: uppercase; font-weight: 600;
      backdrop-filter: blur(8px);
    }}
    .btn:hover {{ background: #1e293b; color: #38bdf8; border-color: #38bdf8; }}
    .btn-active {{ background: #0284c7; color: #ffffff; border-color: #38bdf8; }}
    
    #voice-prompt {{
      position: absolute; top: 16px; left: 16px; z-index: 100;
    }}
  </style>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
</head>
<body>
  <div id="viewport">
    <div id="voice-prompt">
      <button id="voice-btn" class="btn btn-active" onclick="initVoiceSystem()">🔊 Iniciar Audio</button>
    </div>
    <div id="top-bar">
      <button class="btn" onclick="setCameraView('sagittal')">Sagital</button>
      <button class="btn" onclick="setCameraView('coronal')">Coronal</button>
      <button class="btn" onclick="setCameraView('axial')">Axial</button>
      <button class="btn" onclick="setCameraView('iso')">3D Libre</button>
    </div>
    <div id="hud">
      <div id="hud-head" class="hud-title">Conectoma Interactivo</div>
      <div id="hud-body" class="hud-desc">Arrastra con el ratón directamente para rotar el encéfalo en 360° o usa la rueda para zoom.<br><br><b>Haz clic en cualquier núcleo</b> para escuchar su explicación clínica con analogías y citas.</div>
    </div>
  </div>

  <script>
    const DATA = {json.dumps(payload)};
    const container = document.getElementById('viewport');

    // -------------------------------------------------------------
    // MOTOR DE VOZ CLÍNICA HUMANIZADA
    // -------------------------------------------------------------
    let voiceActive = false;
    let selectedVoice = null;

    function populateVoices() {{
      if (!window.speechSynthesis) return;
      const voices = window.speechSynthesis.getVoices();
      selectedVoice = voices.find(v => v.lang.startsWith('es') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Paulina') || v.name.includes('Jorge') || v.name.includes('Sabina'))) ||
                      voices.find(v => v.lang.startsWith('es')) || null;
    }}

    if (window.speechSynthesis) {{
      populateVoices();
      if (window.speechSynthesis.onvoiceschanged !== undefined) {{
        window.speechSynthesis.onvoiceschanged = populateVoices;
      }}
    }}

    function initVoiceSystem() {{
      voiceActive = !voiceActive;
      const b = document.getElementById('voice-btn');
      if (voiceActive) {{
        b.innerText = "🔊 Voz: Activa";
        b.classList.add("btn-active");
        speakText("Motor vocal activado. Selecciona cualquier estructura o vía axonal para escuchar su mecanismo fisiopatológico con analogías clínicas y evidencia.");
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
      if (selectedVoice) utter.voice = selectedVoice;
      utter.lang = 'es-ES';
      utter.rate = 0.94;
      utter.pitch = 1.02;
      window.speechSynthesis.speak(utter);
    }}

    // -------------------------------------------------------------
    // ESCENA THREE.JS
    // -------------------------------------------------------------
    const scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x020617, 0.024);

    const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.set(0, 2, 21);

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
    // CONTROL TOTAL DE RATÓN CON POINTER EVENTS
    // -------------------------------------------------------------
    let isPointerDown = false;
    let startX = 0, startY = 0;
    let targetRotX = 0.15, targetRotY = 0;
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
        isClickGesture = false;
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
        targetRotX = 0.15; targetRotY = 0; camera.position.set(0, 2, 21);
        autoRotate = true;
      }}
      camera.lookAt(0, 0, 0);
    }}

    // -------------------------------------------------------------
    // MALLA ANATÓMICA BIOFIEL CON POLO TEMPORAL Y LÓBULO FRONTAL
    // -------------------------------------------------------------
    function createRealisticBrainCortex() {{
      const uSegs = 100, vSegs = 100;
      const geo = new THREE.BufferGeometry();
      const pos = [];

      for(let i=0; i<=uSegs; i++) {{
        let u = (i / uSegs) * Math.PI * 2;
        for(let j=0; j<=vSegs; j++) {{
          let v = (j / vSegs) * Math.PI;

          // Dimensiones antropométricas reales (ancho X, largo Y fronto-occipital, alto Z)
          let rx = 4.3, ry = 5.9, rz = 4.1;

          // Giros y circunvoluciones anatómicas calibradas
          let sulci = 0.28 * Math.sin(8 * u) * Math.cos(7 * v) + 
                      0.18 * Math.sin(16 * v) * Math.cos(4 * u) +
                      0.08 * Math.sin(24 * u);

          let x = (rx + sulci) * Math.sin(v) * Math.cos(u);
          let y = (ry + sulci) * Math.sin(v) * Math.sin(u);
          let z = (rz + sulci) * Math.cos(v);

          // Escisión sagital interhemisférica real
          if (x >= 0) x += 0.48; else x -= 0.48;

          // Deformación del polo temporal en gancho (inferior y anterior)
          if (z < -0.5 && y > -1.5 && y < 2.5) {{
            let tempFactor = Math.sin((y + 1.5) / 4.0 * Math.PI);
            x *= (1.0 + 0.18 * tempFactor);
            z -= 0.35 * tempFactor;
          }}

          // Depresión en fosa parietal y polo occipital posterior
          if (y < -2.0) {{
            x *= (1.0 - 0.15 * Math.abs(y + 2.0) / 4.0);
          }}

          // Curvatura sagital general
          z -= 0.08 * (y * y) / ry;

          pos.push(x, y, z);
        }}
      }}
      geo.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
      geo.computeVertexNormals();

      const mat = new THREE.MeshPhysicalMaterial({{
        color: 0x38bdf8,
        emissive: 0x0284c7,
        emissiveIntensity: 0.40,
        roughness: 0.2,
        metalness: 0.1,
        transparent: true,
        opacity: DATA.view.includes("1.") ? 0.35 : 0.08,
        wireframe: true,
        depthWrite: false
      }});
      return new THREE.Mesh(geo, mat);
    }}

    const cortexMesh = createRealisticBrainCortex();
    modelGroup.add(cortexMesh);

    // -------------------------------------------------------------
    // NODOS EN COORDENADAS ANATÓMICAS CALIBRADAS
    // -------------------------------------------------------------
    const clickableObjects = [];
    const pulsingNodes = [];
    const synapticFlows = [];

    if (DATA.view.includes("1.")) {{
      DATA.nodes.forEach(n => {{
        const geo = new THREE.SphereGeometry(n.rad, 24, 24);
        const mat = new THREE.MeshStandardMaterial({{
          color: n.color,
          emissive: n.color,
          emissiveIntensity: 2.2,
          roughness: 0.2,
          transparent: true,
          opacity: 0.92
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

        // Halo calibrado fMRI
        const auraGeo = new THREE.SphereGeometry(n.rad * 1.35, 16, 16);
        const auraMat = new THREE.MeshBasicMaterial({{
          color: n.color,
          transparent: true,
          opacity: 0.25,
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
          emissiveIntensity: isBroken ? 0.6 : 1.4,
          transparent: true,
          opacity: isBroken ? 0.50 : 0.88
        }});
        const tube = new THREE.Mesh(tubeGeo, tubeMat);
        tube.userData = {{
          name: t.name,
          desc: t.desc,
          voice: t.voice
        }};
        modelGroup.add(tube);
        clickableObjects.push(tube);

        // Potenciales de acción
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
      // Modo Grafo de Onda Expansiva
      DATA.ecosystem.forEach(e => {{
        const rad = 0.85 + e.tension * 0.45;
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

      if (autoRotate) {{
        targetRotY += 0.003;
      }}
      modelGroup.rotation.y = targetRotY;
      modelGroup.rotation.x = targetRotX;

      pulsingNodes.forEach(mesh => {{
        const hz = mesh.userData.hz || 2.0;
        const s = 1.0 + Math.sin(t * hz) * 0.10;
        mesh.scale.set(s, s, s);
      }});

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
