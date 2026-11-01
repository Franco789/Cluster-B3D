import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="Atlas Neurobiológico & Conectómico del Cluster B",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estética quirúrgica dark mode de alta gama
st.markdown("""
<style>
    .stApp { background-color: #020617; color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    h1, h2, h3, h4 { color: #f8fafc; font-weight: 700; letter-spacing: -0.02em; }
    
    .evidence-panel {
        background: #0b1329; border: 1px solid #1e293b; border-left: 3px solid #38bdf8;
        padding: 12px 16px; border-radius: 8px; margin-bottom: 10px;
    }
    .evidence-header { font-size: 0.70rem; text-transform: uppercase; color: #94a3b8; font-weight: 700; letter-spacing: 0.06em; }
    .evidence-title { font-size: 1.10rem; font-weight: 800; color: #38bdf8; font-family: ui-monospace, Menlo, Consolas, monospace; margin: 2px 0; }
    .evidence-body { font-size: 0.76rem; color: #cbd5e1; line-height: 1.4; margin-top: 4px; }
    .evidence-ref { font-size: 0.68rem; color: #64748b; font-style: italic; margin-top: 4px; }
    
    .atlas-card {
        background: #090e1a; border: 1px solid #1e293b; border-radius: 8px;
        padding: 14px 18px; margin-bottom: 12px;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# Base de Datos Neurobiológica Calibrada en Literatura Internacional
# -------------------------------------------------------------------------
CLINICAL_REGISTRY = {
    "Trastorno Límite de la Personalidad (TLP)": {
        "short_key": "TLP",
        "circuit_name": "Falla del Freno Top-Down & Alarma Nociceptiva del Dolor Social",
        "color_accent": "#ef4444",
        "dti_ref": "Schmahl et al. (2014, Biological Psychiatry) & New et al. (2009, NeuroImage)",
        "fmri_ref": "Eisenberger & Lieberman (2004, Science) & Ruocco et al. (2013, Am J Psychiatry meta-analysis)",
        "biomarkers": {
            "dti": {
                "title": "Fascículo Uncinado Bilateral",
                "status": "Anisotropía Fraccional Disminuida (FA < 0.20)",
                "ref": "Schmahl et al. (2014, Biol Psychiatry) | New et al. (2009, NeuroImage)",
                "summary": "Desorganización microestructural en sustancia blanca frontolímbica. La vía eferente orbitofrontal no logra transmitir la señal inhibitoria de extinción hacia la amígdala."
            },
            "fmri_amygdala": {
                "title": "Complejo Amigdalino Basolateral",
                "status": "Hiperreactividad Fásica con Falla de Extinción",
                "ref": "Ruocco et al. (2013, Am J Psychiatry)",
                "summary": "Respuesta desproporcionada ante caras neutras o señales de distanciamiento interpersonal, codificadas erróneamente como amenaza inminente de abandono."
            },
            "fmri_pain": {
                "title": "Matriz del Dolor Social (dACC / Ínsula)",
                "status": "Coactivación Paroxística en Exclusión",
                "ref": "Eisenberger & Lieberman (2004, Science)",
                "summary": "En paradigmas Cyberball, la exclusión vincular recluta exactamente los mismos sustratos nociceptivos que una lesión tisular física aguda."
            },
            "ratio": {
                "title": "Balance Conectómico Frontolímbico",
                "status": "Desacoplamiento Top-Down Severo",
                "ref": "Cullen et al. (2011) | Coccaro et al. (2007)",
                "summary": "Incapacidad del córtex prefrontal ventromedial para reclutar recursos reflexivos (mentalización) durante picos de desregulación simpática."
            }
        },
        "neuroimaging_slices": {
            "sagittal": {
                "plane": "Sagital Medial (x = 0 mm)",
                "target": "Cíngulo Anterior Dorsal (dACC) & vmPFC Subgenual",
                "signal": "Hiperintensidad BOLD en dACC (Brodmann 24/32) ante exclusión relacional. Atenuación marcada de vmPFC (Brodmann 10/11) durante tareas de reevaluación cognitiva.",
                "clinical_correlate": "Falla en la modulación del afecto negativo; dolor psíquico abrumador traducido en impulsos autolesivos."
            },
            "coronal": {
                "plane": "Coronal Anterior (y = -4 mm)",
                "target": "Complejos Amigdalinos Bilaterales & Lóbulo Temporal",
                "signal": "Asimetría en la respuesta fásica con hiperactivación del polo amigdalino basolateral derecho frente a expresiones faciales neutras.",
                "clinical_correlate": "Hipersensibilidad de alarma; decodificación paranoide del distanciamiento afectivo de la pareja."
            },
            "axial": {
                "plane": "Axial Orbitofrontal (z = -12 mm)",
                "target": "Fascículo Uncinado & Ínsula Anterior Bilateral",
                "signal": "Pérdida de anisotropía fraccional (FA) demostrada por tensores DTI en la curvatura del uncinado alrededor de la ínsula.",
                "clinical_correlate": "Desconexión estructural directa entre el procesamiento visceral (vacío insular) y el juicio reflexivo prefrontal."
            }
        },
        "nodes": [
            {
                "name": "Amígdala Basolateral Derecha",
                "coords": [1.9, -0.6, -1.3],
                "color": "#ef4444",
                "rad": 0.40,
                "hz": 8.0,
                "status": "HIPERTRÓFICA FÁSICA",
                "desc": "Alarma paroxística de supervivencia; decodificación errónea de rostros neutros como amenazantes.",
                "voice": "Amígdala basolateral derecha. Imaginemos una alarma de humo ultrasensible que suena ante el simple vapor de una taza de café. En el TLP, un mensaje sin responder es interpretado como una amenaza mortal de abandono. New y colaboradores demostraron que el circuito queda atrapado en una tormenta adrenérgica sin poder extinguir el miedo."
            },
            {
                "name": "Amígdala Basolateral Izquierda",
                "coords": [-1.9, -0.6, -1.3],
                "color": "#ef4444",
                "rad": 0.40,
                "hz": 8.0,
                "status": "HIPERTRÓFICA FÁSICA",
                "desc": "Descarga simpática autónoma inmediata ante la sospecha de distanciamiento interpersonal.",
                "voice": "Amígdala basolateral izquierda. Dispara taquicardia y terror fisiológico similar al ataque de un depredador ante la mera percepción de frialdad en la pareja."
            },
            {
                "name": "Córtex Prefrontal Ventromedial (vmPFC)",
                "coords": [0.0, 4.0, -0.8],
                "color": "#38bdf8",
                "rad": 0.38,
                "hz": 1.0,
                "status": "COLAPSO INHIBITORIO",
                "desc": "Falla del freno inhibitorio top-down; incapacidad de modular el afecto negativo.",
                "voice": "Corteza prefrontal ventromedial. Es el pedal de freno del cerebro emocional. En el TLP, este freno se queda sin líquido hidráulico. El paciente sabe racionalmente que autolesionarse no resuelve el problema, pero la corteza frontal no tiene la fuerza sináptica para frenar la inercia del impulso."
            },
            {
                "name": "Cíngulo Anterior Dorsal (dACC)",
                "coords": [0.0, 1.8, 2.0],
                "color": "#f43f5e",
                "rad": 0.42,
                "hz": 7.2,
                "status": "DOLOR SOCIAL AGUDO",
                "desc": "Epicentro de la Red de Prominencia; traduce la distancia vincular en angustia física.",
                "voice": "Cíngulo anterior dorsal. Naomi Eisenberger demostró en Science que el cerebro no distingue la exclusión afectiva de una quemadura física real. Cuando el paciente se siente ignorado, este núcleo se enciende con tal violencia que el dolor físico provocado en autolesiones busca apagar este dolor psíquico abrumador."
            },
            {
                "name": "Ínsula Anterior Agranular",
                "coords": [3.0, 0.7, -0.2],
                "color": "#e11d48",
                "rad": 0.36,
                "hz": 6.5,
                "status": "HIPEREXCITACIÓN INTEROCEPTIVA",
                "desc": "Sustrato neurofisiológico de la vivencia de vacío crónico y disforia visceral.",
                "voice": "Ínsula anterior agranular. Aquí reside el correlato biológico de ese agujero en el pecho o vacío crónico que describe el paciente en el consultorio; una sensación visceral intolerable que empuja a la impulsividad de alivio inmediato."
            }
        ],
        "tracts": [
            {
                "from": [1.9, -0.6, -1.3], "to": [0.0, 4.0, -0.8], "ctrl": [2.8, 1.5, -1.8],
                "name": "Fascículo Uncinado Derecho",
                "status": "broken",
                "desc": "Tracto axonómico desmielinizado; pérdida de anisotropía fraccional.",
                "voice": "Fascículo uncinado derecho. Es el cable de fibra óptica que conecta la razón con la emoción. En el TLP está deshilachado y con pérdida de mielina. La orden de calmarse enviada por el lóbulo frontal llega tarde o rota a la amígdala."
            },
            {
                "from": [-1.9, -0.6, -1.3], "to": [0.0, 4.0, -0.8], "ctrl": [-2.8, 1.5, -1.8],
                "name": "Fascículo Uncinado Izquierdo",
                "status": "broken",
                "desc": "Interrupción de la conectividad recíproca amígdalo-prefrontal bilateral.",
                "voice": "Fascículo uncinado izquierdo. La tractografía DTI documentada por Schmahl revela una baja anisotropía fraccional bilateral, explicando por qué las crisis son refractarias a la lógica verbal."
            },
            {
                "from": [0.0, 1.8, 2.0], "to": [0.0, 4.0, -0.8], "ctrl": [0.0, 3.0, 0.7],
                "name": "Proyección Cíngulo-Frontal",
                "status": "hyper",
                "desc": "Sobrecarga de conflicto social transmitida sin modulación prefrontal.",
                "voice": "Proyección cíngulo-frontal. Bombardea a la corteza ejecutiva con un flujo constante de angustia, saturando los recursos cognitivos y provocando el clásico bloqueo reflexivo durante el conflicto."
            }
        ],
        "whodas_domains": [
            {"domain": "Compromiso Vincular & Apego", "severity": 96, "indicator": "Splitting paroxístico, pánico al desapego e idealización/odio", "impact": "Inestabilidad catastrófica en relaciones íntimas con rupturas caóticas recurrentes."},
            {"domain": "Utilización de Servicios de Urgencias", "severity": 92, "indicator": "Ingresos por gestos parasuicidas e intoxicaciones", "impact": "Sobrecarga de servicios de emergencia por conductas de regulación afectiva extrema."},
            {"domain": "Cohesión del Self & Autodirección", "severity": 94, "indicator": "Vivencia de vacío crónico y dispersión identitaria", "impact": "Incapacidad para sostener proyectos de vida independientes sin validación continua."},
            {"domain": "Soporte Familiar & Red Primaria", "severity": 88, "indicator": "Claudicación vincular y dinámicas de doble vínculo", "impact": "Agotamiento crónico de cuidadores primarios con desgaste afectivo severo."},
            {"domain": "Desempeño Ocupacional / Académico", "severity": 72, "indicator": "Abandono de estudios y cesantías laborales", "impact": "Fracaso vocacional secundario a ausentismo y conflictos explosivos interpersonales."}
        ]
    },
    "Trastorno Antisocial de la Personalidad (TASP)": {
        "short_key": "TASP",
        "circuit_name": "Ablación Funcional Frontolímbica & Falla de Aversión Moral",
        "color_accent": "#f59e0b",
        "dti_ref": "Craig et al. (2009, Molecular Psychiatry) & Motzkin et al. (2011, J Neuroscience)",
        "fmri_ref": "Blair et al. (2004, NeuroImage) & Birbaumer et al. (2005, Arch Gen Psychiatry)",
        "biomarkers": {
            "dti": {
                "title": "Fascículo Uncinado Bilateral",
                "status": "Ablación Microestructural Mayor (FA < 0.10)",
                "ref": "Craig et al. (2009, Mol Psychiatry) | Motzkin et al. (2011)",
                "summary": "Desconexión anatómica casi total entre amígdala anterior y corteza orbitofrontal. Interrupción del canal que comunica la señal de miedo/castigo con la toma de decisiones morales."
            },
            "fmri_amygdala": {
                "title": "Complejo Amigdalino Basolateral",
                "status": "Hipoactividad e Inmunidad al Condicionamiento",
                "ref": "Blair et al. (2004, NeuroImage) | Birbaumer et al. (2005)",
                "summary": "Ausencia de respuesta hemodinámica ante rostros temerosos o estímulos aversivos. Falta de condicionamiento electrodérmico al castigo anticipado."
            },
            "fmri_pain": {
                "title": "Ínsula Anterior (Empatía Afectiva)",
                "status": "Anestesia Somatosensorial Vicaria",
                "ref": "Glenn & Raine (2014) | Decety et al. (2013)",
                "summary": "Falla en la activación insular ante el sufrimiento ajeno. Preservación de Teoría de la Mente cognitiva (manipulación instrumental) con carencia de culpa somatizada."
            },
            "ratio": {
                "title": "Bucle Córtico-Estriatal Predatorio",
                "status": "Sensibilidad Extrema a Ganancia Inmediata",
                "ref": "Buckholtz et al. (2010, Nature Neurosci)",
                "summary": "Hiperreactividad dopaminérgica del núcleo accumbens orientada a recompensas inmediatas sin computar daño colateral ni riesgo de sanción penal."
            }
        },
        "neuroimaging_slices": {
            "sagittal": {
                "plane": "Sagital Medial (x = 0 mm)",
                "target": "vmPFC & Córtex Cingulado Anterior",
                "signal": "Hipoactivación marcada de la corteza prefrontal ventromedial durante dilemas morales que involucran daño a terceros.",
                "clinical_correlate": "Juicio ético disociado de afecto; comprensión intelectual de la norma sin freno visceral de culpa."
            },
            "coronal": {
                "plane": "Coronal Anterior (y = -4 mm)",
                "target": "Amígdalas & Estriado Ventral (Accumbens)",
                "signal": "Hipoatenuación de amígdala acoplada a hiperactivación fásica de núcleos accumbens frente a incentivos materiales inmediatos.",
                "clinical_correlate": "Impulso predatorio hacia el beneficio propio desprovisto de miedo al castigo penitenciario."
            },
            "axial": {
                "plane": "Axial Orbitofrontal (z = -12 mm)",
                "target": "Tractos Uncinados & Corteza Orbitofrontal Lateral",
                "signal": "Ablación de haces de difusión DTI: anisotropía fraccional severamente degradada con pérdida de conectividad estructural frontotemporal.",
                "clinical_correlate": "Incapacidad para asociar la transgresión de normas con el condicionamiento punitivo futuro."
            }
        },
        "nodes": [
            {
                "name": "Amígdala (Hipoactiva / Atrofiada)",
                "coords": [1.9, -0.6, -1.3],
                "color": "#1e293b",
                "rad": 0.30,
                "hz": 0.4,
                "status": "ATROFIA FUNCIONAL",
                "desc": "Inmunidad al condicionamiento por miedo o castigo; refractariedad autonómica.",
                "voice": "Amígdala hipoactiva. Es un detector de humo sin batería. Aunque haya fuego alrededor, no emite ningún sonido. Mientras una persona común siente taquicardia al infringir una regla o ver llorar a alguien, el individuo psicopático permanece en calma fisiológica absoluta."
            },
            {
                "name": "vmPFC (Polo Moral Desconectado)",
                "coords": [0.0, 4.0, -0.8],
                "color": "#334155",
                "rad": 0.34,
                "hz": 0.5,
                "status": "HIPOCONECTADA",
                "desc": "Juicio lógico analítico frío, pero sin integración somática del sufrimiento ajeno.",
                "voice": "Corteza prefrontal ventromedial. Funciona como una calculadora desprovista de escrúpulos. Comprende las reglas y lo que está prohibido en términos teóricos, pero esa comprensión no tiene anclaje afectivo. Dañar al otro es simplemente un costo transaccional admisible."
            },
            {
                "name": "Núcleo Accumbens (Estriado)",
                "coords": [1.0, 1.2, -0.7],
                "color": "#eab308",
                "rad": 0.46,
                "hz": 7.5,
                "status": "HIPERACTIVIDAD PREDATORIA",
                "desc": "Búsqueda insaciable de recompensa inmediata y dominancia instrumental.",
                "voice": "Núcleo accumbens. Es el motor predatorio de recompensa. Si una persona común ve una oportunidad de robo, el freno moral inhibe el impulso; aquí el estriado se sobreactiva exigiendo la gratificación inmediata, sin importar el daño causado."
            },
            {
                "name": "Ínsula Anterior (Anestesiada)",
                "coords": [3.0, 0.7, -0.2],
                "color": "#1e293b",
                "rad": 0.26,
                "hz": 0.3,
                "status": "ANESTESIA INTEROCEPTIVA",
                "desc": "Carencia absoluta de culpa visceral o remordimiento somatizado.",
                "voice": "Ínsula anterior anestesiada. Es la sede de la resonancia somática vicaria. Su hipofunción explica por qué pueden presenciar el dolor de una víctima sin experimentar la menor aversión ni remordimiento en el estómago."
            }
        ],
        "tracts": [
            {
                "from": [1.9, -0.6, -1.3], "to": [0.0, 4.0, -0.8], "ctrl": [2.8, 1.5, -1.8],
                "name": "Fascículo Uncinado (Ablación Conectómica)",
                "status": "broken",
                "desc": "Interrupción casi completa del tracto microestructural.",
                "voice": "Fascículo uncinado cortado. Motzkin comprobó en reclusos que la línea entre el centro del miedo y el juicio moral está rota. El cerebro no puede enviar la señal de freno somático ante la transgresión."
            },
            {
                "from": [0.0, 4.0, -0.8], "to": [1.0, 1.2, -0.7], "ctrl": [0.5, 2.5, -0.7],
                "name": "Vía Córtico-Estriatal Desinhibida",
                "status": "hyper",
                "desc": "El estriado opera sin freno inhibitorio frontal, facilitando conductas predatorias.",
                "voice": "Vía córtico-estriatal desinhibida. El lóbulo frontal no frena al núcleo de recompensa; se pone a su servicio para planificar estafas y manipulaciones con frialdad metodológica."
            }
        ],
        "whodas_domains": [
            {"domain": "Marco Judicial & Fuero Penal", "severity": 99, "indicator": "Reincidencia criminal y transgresión deliberada de la ley", "impact": "Colisión sistemática con el sistema penal; litigios por delitos patrimoniales y violentos."},
            {"domain": "Esfera Vincular & Instrumentalización", "severity": 96, "indicator": "Cosificación utilitaria y violencia predatoria", "impact": "Destrucción patrimonial y psicológica de parejas y familiares convertidos en víctimas."},
            {"domain": "Funcionamiento Contractual / Financiero", "severity": 90, "indicator": "Estafas premeditadas, fraudes y deshonestidad", "impact": "Quiebras fraudulentas, despidos disciplinarios y evasión crónica de responsabilidades."},
            {"domain": "Simulación Médico-Forense", "severity": 65, "indicator": "Manipulación deliberada de síntomas en peritajes", "impact": "Uso instrumental del sistema de salud mental para eludir imputabilidad jurídica."},
            {"domain": "Insight & Conciencia de Enfermedad", "severity": 10, "indicator": "Egosintonía perfecta; ausencia de autocrítica", "impact": "Cero demanda espontánea de tratamiento; el sufrimiento es exclusivamente externo."}
        ]
    },
    "Trastorno Narcisista de la Personalidad (TNP)": {
        "short_key": "TNP",
        "circuit_name": "Disociación Fronto-Insular & Vulnerabilidad al Desprecio",
        "color_accent": "#a855f7",
        "dti_ref": "Fan et al. (2011, SCAN) & Nenadic et al. (2015, Psychiatry Research)",
        "fmri_ref": "Pincus & Lukowitsky (2010) & Schulze et al. (2013)",
        "biomarkers": {
            "dti": {
                "title": "Sustancia Blanca Frontomedial",
                "status": "Integridad Preservada con Sesgo de Dominancia",
                "ref": "Fan et al. (2011, SCAN) | Nenadic et al. (2015)",
                "summary": "Tractos de mentalización cognitiva intactos. Preservación del cálculo estratégico con hipoconectividad hacia redes de empatía afectiva."
            },
            "fmri_amygdala": {
                "title": "Cíngulo Dorsal / Amígdala",
                "status": "Hiperreactividad ante Amenaza al Estatus",
                "ref": "Pincus & Lukowitsky (2010) | Schulze et al. (2013)",
                "summary": "Paroxismo en dACC ('herida narcisista') ante el desacato o la crítica. Respuesta colérica defensiva para restituir la autovaloración."
            },
            "fmri_pain": {
                "title": "Corteza Insular Anterior",
                "status": "Disociación Empática Afectiva",
                "ref": "Jankowiak-Siuda et al. (2015) | Baskin-Sommers et al.",
                "summary": "Reducción volumétrica de sustancia gris en ínsula anterior. El sujeto comprende el dolor del otro pero no resuena visceralmente con él."
            },
            "ratio": {
                "title": "Red por Defecto vs. Prominencia",
                "status": "Compensación Grandiosa Hipertrófica",
                "ref": "Scalabrini et al. (2017, Hum Brain Mapp)",
                "summary": "Gasto metabólico frontal desmedido para sostener una autoimagen inflada que actúe como barrera frente al vacío interior."
            }
        },
        "neuroimaging_slices": {
            "sagittal": {
                "plane": "Sagital Medial (x = 0 mm)",
                "target": "dACC Dorsal & Polo Frontal Superior",
                "signal": "Hiperactivación fásica del cíngulo dorsal ante paradigmas de evaluación social peyorativa o pérdida de prestigio.",
                "clinical_correlate": "Herida narcisista aguda; viraje hacia hostilidad defensiva y desprecio punitivo del interlocutor."
            },
            "coronal": {
                "plane": "Coronal Anterior (y = -4 mm)",
                "target": "Ínsulas Anteriores & Amígdalas",
                "signal": "Hipoactivación de la ínsula anterior frente al sufrimiento ajeno combinada con amígdala reactiva a la crítica personal.",
                "clinical_correlate": "Empatía cognitiva instrumental preservada con ausencia de compasión afectiva somatizada."
            },
            "axial": {
                "plane": "Axial Orbitofrontal (z = -12 mm)",
                "target": "Red por Defecto Medial (DMN)",
                "signal": "Sobreactivación persistente de la corteza prefrontal medial dorsomedial durante tareas de reposo y autorreflexión.",
                "clinical_correlate": "Rumiación obsesiva sobre estatus, grandiosidad compensatoria y vigilancia de jerarquías sociales."
            }
        },
        "nodes": [
            {
                "name": "dACC (Radar de Jerarquía)",
                "coords": [0.0, 1.8, 2.0],
                "color": "#a855f7",
                "rad": 0.44,
                "hz": 7.4,
                "status": "HIPERREACTIVO AL DESPRECIO",
                "desc": "Alarma desmedida ante el desacato, la crítica o la pérdida de admiración.",
                "voice": "Cíngulo anterior dorsal. Es un radar de jerarquía social en hipervigilancia continua. Si una opinión suya no es celebrada, este núcleo detecta una ofensa mortal a su estatus, detonando furia fría o venganza calculada."
            },
            {
                "name": "vmPFC (Autoimagen Grandiosa)",
                "coords": [0.0, 4.0, -0.8],
                "color": "#c084fc",
                "rad": 0.40,
                "hz": 2.8,
                "status": "COMPENSACIÓN GRANDIOSA",
                "desc": "Mantenimiento activo del constructo de superioridad como defensa ante el vacío.",
                "voice": "Corteza prefrontal ventromedial. Es como construir un andamio de oro sobre cimientos de barro. Se gasta una enorme cantidad de energía metabólica en sostener el relato de superioridad, precisamente para tapar el terror al vacío interior."
            },
            {
                "name": "Amígdala (Rabia Narcisista)",
                "coords": [1.9, -0.6, -1.3],
                "color": "#ec4899",
                "rad": 0.36,
                "hz": 5.2,
                "status": "VULNERABILIDAD FÁSICA",
                "desc": "Explosiones coléricas vindicativas ante la exposición de debilidad.",
                "voice": "Amígdala fásica. Dispara la llamada rabia narcisista. Ante una crítica fundada, la herida narcisista desata una reacción colérica que busca descalificar al otro para restituir el propio valor dañado."
            },
            {
                "name": "Ínsula (Desconexión Vicaria)",
                "coords": [3.0, 0.7, -0.2],
                "color": "#334155",
                "rad": 0.30,
                "hz": 0.8,
                "status": "ANESTESIA EMPÁTICA",
                "desc": "Incapacidad neurofisiológica de registrar el dolor causado a subordinados.",
                "voice": "Ínsula anterior desconectada. Fan demostró en la revista SCAN que el narcisista tiene empatía cognitiva intacta: sabe perfectamente qué te duele y cómo herirte, pero carece de empatía afectiva; no siente compasión al hacerlo."
            }
        ],
        "tracts": [
            {
                "from": [0.0, 1.8, 2.0], "to": [0.0, 4.0, -0.8], "ctrl": [0.0, 3.0, 0.7],
                "name": "Eje de Autoevaluación Hipervigilante",
                "status": "hyper",
                "desc": "Circuito de monitoreo constante del estatus y de la aprobación externa.",
                "voice": "Eje de autoevaluación. Obliga al sujeto a monitorear obsesivamente cuántos elogios recibe para mantener equilibrada su autoestima."
            },
            {
                "from": [1.9, -0.6, -1.3], "to": [0.0, 1.8, 2.0], "ctrl": [1.0, 0.6, 0.6],
                "name": "Circuito de Ira Vindicativa",
                "status": "hyper",
                "desc": "Descarga amigdalina directa al cíngulo que alimenta la hostilidad defensiva.",
                "voice": "Circuito de ira vindicativa. Es el puente por donde la herida del orgullo se transforma en desprecio hacia quien osó marcarle un error."
            },
            {
                "from": [3.0, 0.7, -0.2], "to": [0.0, 4.0, -0.8], "ctrl": [1.6, 1.8, -0.4],
                "name": "Desconexión Fronto-Insular",
                "status": "broken",
                "desc": "Bloqueo selectivo de la resonancia afectiva hacia el sufrimiento ajeno.",
                "voice": "Desconexión fronto-insular. El tracto responsable de frenar la crueldad relacional está apagado; el otro es tratado como un objeto utilitario sin costo de conciencia."
            }
        ],
        "whodas_domains": [
            {"domain": "Esfera Conyugal (Dinámica de Poder)", "severity": 92, "indicator": "Dominación, devaluación y ley del hielo", "impact": "Relación asimétrica; exigencia de pleitesía con castigo afectivo ante la discrepancia."},
            {"domain": "Cohesión del Self & Riesgo de Colapso", "severity": 95, "indicator": "Fragilidad extrema ante pérdidas de estatus", "impact": "Riesgo de descompensación depresiva disfórica grave ante bancarrotas o pérdidas públicas."},
            {"domain": "Entorno Corporativo / Jerárquico", "severity": 84, "indicator": "Rivalidad destructiva y boicot a subordinados", "impact": "Clima laboral tóxico, maltrato institucional y rotación continua de equipos a su cargo."},
            {"domain": "Red Familiar de Origen", "severity": 76, "indicator": "Instrumentalización de descendientes", "impact": "Hijos tratados como trofeos de éxito o excluidos si manifiestan autonomía de pensamiento."},
            {"domain": "Adherencia Terapéutica", "severity": 50, "indicator": "Abandono ante confrontación de defensas", "impact": "Deserción prematura de psicoterapia al negarse a reconocer vulnerabilidad o falencias."}
        ]
    },
    "Trastorno Histriónico de la Personalidad (THP)": {
        "short_key": "THP",
        "circuit_name": "Labilidad Afectiva, Búsqueda de Refuerzo & Somatización",
        "color_accent": "#06b6d4",
        "dti_ref": "Buchsbaum et al. & Schore et al. (Neuropsychoanalysis)",
        "fmri_ref": "Somerville et al. (2010) & Vuilleumier et al.",
        "biomarkers": {
            "dti": {
                "title": "Vías Frontoparietales Dorsolaterales",
                "status": "Varianza Difusa en Conectividad Frontal",
                "ref": "Buchsbaum et al. | Schore et al.",
                "summary": "Desconexión relativa dorsolateral que facilita el estilo cognitivo impresionista, superficial y altamente sugestionable."
            },
            "fmri_amygdala": {
                "title": "Red de Recompensa Estriatal",
                "status": "Hipersensibilidad al Halago y Mirada Ajena",
                "ref": "Somerville et al. (2010) | Vuilleumier et al.",
                "summary": "Hiperreactividad fásica del núcleo accumbens y de la amígdala ante señales de atracción o validación social inmediata."
            },
            "fmri_pain": {
                "title": "Corteza Somatosensorial / Ínsula",
                "status": "Amplificación Conversiva Interoceptiva",
                "ref": "Caria et al. (2012) | Perez et al. (2015, Brain)",
                "summary": "Conversión corporal de conflictos afectivos: la angustia no elaborada verbalmente se traduce en pseudocrisis neurológicas o somatizaciones."
            },
            "ratio": {
                "title": "Control Reflexivo vs. Teatralidad",
                "status": "Cognición Impresionista Desregulada",
                "ref": "Shapiro (Neurotic Styles) | Kernberg",
                "summary": "Incapacidad para sostener tareas sistemáticas o anonimato funcional; desorganización conductual ante la pérdida del rol protagónico."
            }
        },
        "neuroimaging_slices": {
            "sagittal": {
                "plane": "Sagital Medial (x = 0 mm)",
                "target": "vmPFC & Cíngulo Rostral",
                "signal": "Procesamiento prefrontal atenuado durante tareas que exigen razonamiento lógico secuencial y abstracto.",
                "clinical_correlate": "Estilo cognitivo global e impresionista; baja tolerancia a la deliberación analítica profunda."
            },
            "coronal": {
                "plane": "Coronal Anterior (y = -4 mm)",
                "target": "Estriado Ventral & Corteza Somatomotora",
                "signal": "Hiperreactividad del núcleo accumbens ante reforzadores sociales acoplada a hipersensibilidad somatosensorial.",
                "clinical_correlate": "Conductas de seducción descontextualizada y traducción corporal de la angustia no verbalizada."
            },
            "axial": {
                "plane": "Axial Orbitofrontal (z = -12 mm)",
                "target": "Lóbulos Temporales Anteriores",
                "signal": "Activación dispersa témporo-límbica con rápida habituación y labilidad en la codificación de memorias afectivas.",
                "clinical_correlate": "Emotividad volátil: afectos intensos pero efímeros que cambian con la presencia o ausencia de público."
            }
        },
        "nodes": [
            {
                "name": "Amígdala Límbica",
                "coords": [1.9, -0.6, -1.3],
                "color": "#06b6d4",
                "rad": 0.38,
                "hz": 6.2,
                "status": "HIPEREXCITABLE LÁBIL",
                "desc": "Emotividad intensa y cambiante; intolerancia al desinterés del entorno.",
                "voice": "Amígdala límbica lábil. Funciona como fuegos artificiales de corta duración: una explosión de llanto dramático ante una nimiedad, seguida a los diez minutos por risas y seducción. Es una afectividad tan intensa como superficial."
            },
            {
                "name": "Núcleo Accumbens Social",
                "coords": [1.0, 1.2, -0.7],
                "color": "#22d3ee",
                "rad": 0.42,
                "hz": 6.5,
                "status": "HIPERRESPUESTA AL FEEDBACK",
                "desc": "Dependencia absoluta del halago, la seducción y la validación externa.",
                "voice": "Núcleo accumbens social. Circuito adicto a los reflectores. La persona no tolera no ser el centro de atención; si la conversación gira hacia otro tema, recurrirá a seducción inapropiada o una repentina indisposición física para recuperar la mirada de todos."
            },
            {
                "name": "Ínsula Somatosensorial",
                "coords": [3.0, 0.7, -0.2],
                "color": "#0891b2",
                "rad": 0.36,
                "hz": 5.4,
                "status": "SOMATIZACIÓN INTEROCEPTIVA",
                "desc": "Conversión corporal de angustias afectivas; teatralidad física y somatizaciones.",
                "voice": "Ínsula somatosensorial. El teatro no se actúa en palabras, se actúa en el cuerpo. Ante un conflicto no resuelto, la ínsula amplifica las señales corporales provocando parálisis funcionales o desmayos sin base orgánica."
            },
            {
                "name": "vmPFC Impresionista",
                "coords": [0.0, 4.0, -0.8],
                "color": "#475569",
                "rad": 0.34,
                "hz": 1.4,
                "status": "PROCESAMIENTO DIFUSO",
                "desc": "Falla en el procesamiento lógico analítico; razonamiento guiado por impresiones.",
                "voice": "Corteza prefrontal impresionista. Su estilo cognitivo es como una pintura al óleo vista de lejos: capta el ambiente emocional global pero es incapaz de dar precisiones lógicas sobre los hechos que provocaron el conflicto."
            }
        ],
        "tracts": [
            {
                "from": [1.9, -0.6, -1.3], "to": [1.0, 1.2, -0.7], "ctrl": [1.4, 0.4, -0.9],
                "name": "Eje Límbico-Recompensa Interpersonal",
                "status": "hyper",
                "desc": "Circuito reforzador del histrionismo relacional.",
                "voice": "Eje límbico de recompensa. Condiciona la conducta para que el individuo repita permanentemente puestas en escena teatrales que le aseguren la aprobación externa."
            },
            {
                "from": [0.0, 4.0, -0.8], "to": [1.9, -0.6, -1.3], "ctrl": [1.0, 1.5, -1.0],
                "name": "Modulación Frontal Deficitaria",
                "status": "broken",
                "desc": "Falla del control prefrontal para modular la labilidad afectiva.",
                "voice": "Modulación frontal deficitaria. Falla en poner orden y sobriedad cuando la situación amerita contención emocional, como reuniones formales de trabajo o velorios."
            }
        ],
        "whodas_domains": [
            {"domain": "Esfera Conyugal (Sobredramatización)", "severity": 85, "indicator": "Reclamo continuo de pasión novelesca y celotipia", "impact": "Intolerancia a la rutina de convivencia; creación de conflictos teatrales para revivir intensidad."},
            {"domain": "Servicio de Guardia Médica", "severity": 82, "indicator": "Pseudocrisis conversivas e hiperventilación", "impact": "Consultas reiteradas en urgencias por cuadros neurológicos funcionales tras estrés vincular."},
            {"domain": "Red Social Ampliada", "severity": 72, "indicator": "Idealización veloz y relaciones efímeras", "impact": "Amistades intensas asumidas como íntimas que se diluyen ante el agotamiento del entorno."},
            {"domain": "Autoestima & Dependencia Externa", "severity": 80, "indicator": "Desvanecimiento subjetivo ante la falta de atención", "impact": "Sensación de inexistencia si no se cuenta con la mirada atenta o el halago del público."},
            {"domain": "Desempeño Laboral Sistemático", "severity": 50, "indicator": "Baja tolerancia a labores metódicas o sin público", "impact": "Dificultades en roles administrativos; mejor desempeño inicial en relaciones públicas o ventas."}
        ]
    }
}

# --- Sidebar de Control Clínico ---
st.sidebar.markdown("### 🎛️ Consola de Neuropsiquiatría")
selected_disorder = st.sidebar.selectbox("Entidad Patológica:", list(CLINICAL_REGISTRY.keys()))
view_selector = st.sidebar.radio("Nivel de Representación 3D:", ["1. Conectoma & Tractografía DTI", "2. Matriz de Discapacidad Funcional (WHODAS / CIE-11)"])

current_data = CLINICAL_REGISTRY[selected_disorder]

# --- Encabezado ---
st.title(selected_disorder)
st.caption(f"**Circuito Fisiopatológico Central:** {current_data['circuit_name']}")

# --- Panel Superior de Evidencia en Neuroimagen ---
bm = current_data["biomarkers"]
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="evidence-panel">
        <div class="evidence-header">Resonancia DTI</div>
        <div class="evidence-title">{bm['dti']['title']}</div>
        <div class="evidence-body"><b>{bm['dti']['status']}</b><br>{bm['dti']['summary']}</div>
        <div class="evidence-ref">{bm['dti']['ref']}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="evidence-panel">
        <div class="evidence-header">fMRI / BOLD fásica</div>
        <div class="evidence-title">{bm['fmri_amygdala']['title']}</div>
        <div class="evidence-body"><b>{bm['fmri_amygdala']['status']}</b><br>{bm['fmri_amygdala']['summary']}</div>
        <div class="evidence-ref">{bm['fmri_amygdala']['ref']}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="evidence-panel">
        <div class="evidence-header">Red de Prominencia</div>
        <div class="evidence-title">{bm['fmri_pain']['title']}</div>
        <div class="evidence-body"><b>{bm['fmri_pain']['status']}</b><br>{bm['fmri_pain']['summary']}</div>
        <div class="evidence-ref">{bm['fmri_pain']['ref']}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="evidence-panel">
        <div class="evidence-header">Acoplamiento Frontolímbico</div>
        <div class="evidence-title">{bm['ratio']['title']}</div>
        <div class="evidence-body"><b>{bm['ratio']['status']}</b><br>{bm['ratio']['summary']}</div>
        <div class="evidence-ref">{bm['ratio']['ref']}</div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------------------
# Motor WebGL Three.js con Malla Bi-Hemisférica Limpia y HUD Lateral
# -------------------------------------------------------------------------
payload = {
    "view": view_selector,
    "nodes": current_data["nodes"],
    "tracts": current_data["tracts"],
    "whodas": current_data["whodas_domains"],
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
      <div id="hud-head" class="hud-title">Atlas Conectómico 3D</div>
      <div id="hud-body" class="hud-desc">Arrastra con el ratón directamente para rotar el encéfalo en 360° o usa la rueda para zoom.<br><br><b>Haz clic en cualquier núcleo o tracto</b> para escuchar su análisis clínico con analogías y citas.</div>
    </div>
  </div>

  <script>
    const DATA = {json.dumps(payload)};
    const container = document.getElementById('viewport');

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
        speakText("Motor vocal activado. Selecciona cualquier estructura o tracto para escuchar su correlato clínico y citas bibliográficas.");
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

    const scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x020617, 0.024);

    const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.set(0, 2, 21);

    const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true, powerPreference: "high-performance" }});
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    container.appendChild(renderer.domElement);

    scene.add(new THREE.AmbientLight(0xffffff, 0.85));
    const p1 = new THREE.PointLight(0x38bdf8, 2.5, 60);
    p1.position.set(6, 12, 14);
    scene.add(p1);

    const p2 = new THREE.PointLight(0xa855f7, 2.0, 50);
    p2.position.set(-10, -8, -10);
    scene.add(p2);

    const modelGroup = new THREE.Group();
    scene.add(modelGroup);

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

    // Construcción limpia de corteza cerebral anatómica (Hemisferio Izquierdo y Derecho independientes)
    function buildCleanBrainMesh() {{
      const brainGeo = new THREE.BufferGeometry();
      const pos = [];
      const uSegs = 70, vSegs = 70;

      for (let side = -1; side <= 1; side += 2) {{
        for (let i = 0; i <= uSegs; i++) {{
          let u = (i / uSegs) * Math.PI;
          for (let j = 0; j <= vSegs; j++) {{
            let v = (j / vSegs) * Math.PI * 2;

            // Parámetros elipsoidales calibrados por hemisferio
            let rx = 2.4, ry = 5.2, rz = 3.6;
            let sulci = 0.16 * Math.sin(7 * u) * Math.cos(6 * v) + 0.08 * Math.sin(12 * v);

            let x = (rx + sulci) * Math.sin(u) * Math.cos(v) + (side * 2.2);
            let y = (ry + sulci) * Math.sin(u) * Math.sin(v);
            let z = (rz + sulci) * Math.cos(u);

            // Aplanamiento medial hacia la cisura interhemisférica
            if (side === 1 && x < 0.35) x = 0.35;
            if (side === -1 && x > -0.35) x = -0.35;

            // Curvatura occipital posterior
            if (y < -2.0) {{
              z -= 0.15 * Math.abs(y + 2.0);
            }}

            pos.push(x, y, z);
          }}
        }}
      }}

      brainGeo.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
      brainGeo.computeVertexNormals();

      const mat = new THREE.MeshPhysicalMaterial({{
        color: 0x38bdf8,
        emissive: 0x0284c7,
        emissiveIntensity: 0.35,
        roughness: 0.25,
        metalness: 0.1,
        transparent: true,
        opacity: DATA.view.includes("1.") ? 0.28 : 0.06,
        wireframe: true,
        depthWrite: false
      }});
      return new THREE.Mesh(brainGeo, mat);
    }}

    const cortexMesh = buildCleanBrainMesh();
    modelGroup.add(cortexMesh);

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
      // Modo Matriz de Discapacidad WHODAS 2.0 / CIE-11
      const coordsDomains = [
        [5.2, 2.8, 1.4],
        [-5.0, 3.8, -1.8],
        [3.8, -4.2, -1.8],
        [-4.2, -2.8, 2.4],
        [1.4, 5.0, -2.4]
      ];

      DATA.whodas.forEach((e, idx) => {{
        const pt = coordsDomains[idx % coordsDomains.length];
        const rad = 0.45 + (e.severity / 100) * 0.25;
        const color = e.severity > 85 ? 0xef4444 : (e.severity > 60 ? 0xf59e0b : 0x10b981);

        const geo = new THREE.SphereGeometry(rad, 24, 24);
        const mat = new THREE.MeshStandardMaterial({{
          color: color,
          emissive: color,
          emissiveIntensity: 2.0,
          roughness: 0.3
        }});
        const mesh = new THREE.Mesh(geo, mat);
        mesh.position.set(...pt);
        mesh.userData = {{
          name: e.domain,
          desc: "<b>Indicador CIE-11:</b> " + e.indicator + "<br><b>Severidad de Discapacidad:</b> " + e.severity + "%<br>" + e.impact,
          voice: e.domain + ". Severidad del " + e.severity + " por ciento. " + e.impact
        }};
        modelGroup.add(mesh);
        clickableObjects.push(mesh);

        const lineGeo = new THREE.BufferGeometry().setFromPoints([
          new THREE.Vector3(0, 0, 0),
          new THREE.Vector3(...pt)
        ]);
        const lineMat = new THREE.LineBasicMaterial({{
          color: color,
          linewidth: 3,
          transparent: true,
          opacity: 0.8
        }});
        modelGroup.add(new THREE.Line(lineGeo, lineMat));
      }});
    }}

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
# Cortes Estereotáxicos Detallados (Formato Paper de Neuroimagen)
# -------------------------------------------------------------------------
st.markdown("---")
st.subheader("Atlas de Cortes Anatómicos (Espacio Estereotáxico MNI152)")
st.caption("Inspección sistemática de planos ortogonales según protocolos de fMRI y tractografía DTI")

slices = current_data["neuroimaging_slices"]
s_col1, s_col2, s_col3 = st.columns(3)

with s_col1:
    st.markdown(f"""
    <div class="atlas-card">
        <h4 style="color: #38bdf8; margin: 0 0 6px 0;">Plano Sagital</h4>
        <div style="font-size: 0.76rem; color: #94a3b8; margin-bottom: 8px;"><b>Corte:</b> {slices['sagittal']['plane']}</div>
        <p style="font-size: 0.80rem; color: #e2e8f0; margin-bottom: 8px;"><b>Estructuras Diana:</b> {slices['sagittal']['target']}</p>
        <p style="font-size: 0.76rem; color: #cbd5e1; line-height: 1.4;"><b>Patrón de Señal:</b> {slices['sagittal']['signal']}</p>
        <div style="border-top: 1px solid #1e293b; padding-top: 6px; font-size: 0.74rem; color: #f59e0b;"><b>Correlato Clínico:</b> {slices['sagittal']['clinical_correlate']}</div>
    </div>
    """, unsafe_allow_html=True)

with s_col2:
    st.markdown(f"""
    <div class="atlas-card">
        <h4 style="color: #38bdf8; margin: 0 0 6px 0;">Plano Coronal</h4>
        <div style="font-size: 0.76rem; color: #94a3b8; margin-bottom: 8px;"><b>Corte:</b> {slices['coronal']['plane']}</div>
        <p style="font-size: 0.80rem; color: #e2e8f0; margin-bottom: 8px;"><b>Estructuras Diana:</b> {slices['coronal']['target']}</p>
        <p style="font-size: 0.76rem; color: #cbd5e1; line-height: 1.4;"><b>Patrón de Señal:</b> {slices['coronal']['signal']}</p>
        <div style="border-top: 1px solid #1e293b; padding-top: 6px; font-size: 0.74rem; color: #f59e0b;"><b>Correlato Clínico:</b> {slices['coronal']['clinical_correlate']}</div>
    </div>
    """, unsafe_allow_html=True)

with s_col3:
    st.markdown(f"""
    <div class="atlas-card">
        <h4 style="color: #38bdf8; margin: 0 0 6px 0;">Plano Axial</h4>
        <div style="font-size: 0.76rem; color: #94a3b8; margin-bottom: 8px;"><b>Corte:</b> {slices['axial']['plane']}</div>
        <p style="font-size: 0.80rem; color: #e2e8f0; margin-bottom: 8px;"><b>Estructuras Diana:</b> {slices['axial']['target']}</p>
        <p style="font-size: 0.76rem; color: #cbd5e1; line-height: 1.4;"><b>Patrón de Señal:</b> {slices['axial']['signal']}</p>
        <div style="border-top: 1px solid #1e293b; padding-top: 6px; font-size: 0.74rem; color: #f59e0b;"><b>Correlato Clínico:</b> {slices['axial']['clinical_correlate']}</div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------------------
# Matriz de Discapacidad y Discusión Nosológica Rigurosa
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
    st.markdown("### 🌐 Matriz de Discapacidad Funcional (WHODAS 2.0 / CIE-11)")
    st.markdown("""
    A diferencia de la patología neurótica convencional, donde el sufrimiento se contiene en el ámbito subjetivo, en el **Cluster B** la falla del freno inhibitorio biológico se traslada de forma directa al tejido social:
    * **Esfera Conyugal y de Apego:** Ruptura destructiva de lazos por mecanismos de escisión (*splitting*) o manipulación instrumental.
    * **Servicio de Urgencias Médicas:** Hiperfrecuentación compulsiva por conductas autolesivas o descompensaciones disfóricas agudas.
    * **Área Judicial / Penal:** Colisiones constantes con la ley en personalidades antisociales o litigios por honra y patrimonio.
    """)
