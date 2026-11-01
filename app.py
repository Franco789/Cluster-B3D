import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="Atlas Neuroconectómico 3D: Cluster B",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estética de consola médica de alta gama
st.markdown("""
<style>
    .stApp { background-color: #020617; color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
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
# Base de Datos Neurobiológica con Dimensiones Anatómicas Reducidas y Citas
# -------------------------------------------------------------------------
CLINICAL_DATABASE = {
    "Trastorno Límite de la Personalidad (TLP)": {
        "short_key": "TLP",
        "fa_uncinate": 0.18,
        "amg_act": 1.95,
        "vmpfc_act": 0.22,
        "dacc_act": 1.90,
        "color_accent": "#ef4444",
        "circuit_name": "Falla del Freno Top-Down & Alarma Nociceptiva del Dolor Social",
        "dti_ref": "Schmahl et al. (2014, Biological Psychiatry) & New et al. (2009, NeuroImage): Desorganización microestructural con reducción severa de FA (< 0.20) en el fascículo uncinado bilateral.",
        "fmri_ref": "Eisenberger & Lieberman (2004, Science) & Ruocco et al. (2013, AJP): Coactivación paroxística de dACC e ínsula anterior ante el rechazo percibido en paradigmas Cyberball.",
        "nodes": [
            {
                "name": "Amígdala Basolateral Derecha",
                "coords": [2.2, -0.6, -1.4],
                "color": "#ff0055",
                "rad": 0.48, # Reducido a escala anatómica real
                "hz": 8.0,
                "status": "HIPERTRÓFICA FÁSICA",
                "desc": "Alarma paroxística de supervivencia; decodificación errónea de rostros neutros como amenazantes.",
                "voice": "Amígdala basolateral derecha. Imaginemos una alarma de humo ultrasensible, tan descalibrada que no sólo detecta fuego, sino que hace sonar la sirena de evacuación ante el simple vapor de una taza de café. En el paciente con TLP, un rostro neutro o un mensaje sin responder por diez minutos es interpretado como una amenaza mortal de abandono inminente. Como demostraron New y colaboradores en NeuroImage, el circuito queda atrapado en una tormenta adrenérgica prolongada sin poder extinguir el miedo."
            },
            {
                "name": "Amígdala Basolateral Izquierda",
                "coords": [-2.2, -0.6, -1.4],
                "color": "#ff0055",
                "rad": 0.48,
                "hz": 8.0,
                "status": "HIPERTRÓFICA FÁSICA",
                "desc": "Descarga simpática autónoma inmediata ante la sospecha de distanciamiento interpersonal.",
                "voice": "Amígdala basolateral izquierda. Funciona como un gatillo biológico de pánico relacional. Por ejemplo, en una discusión de pareja, mientras una persona promedio experimenta incomodidad, aquí se desata una descarga autonómica de taquicardia y terror similar a estar frente a un peligro inminente."
            },
            {
                "name": "Córtex Prefrontal Ventromedial (vmPFC)",
                "coords": [0.0, 4.2, -0.8],
                "color": "#38bdf8",
                "rad": 0.42,
                "hz": 1.0,
                "status": "COLAPSO INHIBITORIO",
                "desc": "Falla del freno inhibitorio top-down; incapacidad de modular el afecto negativo.",
                "voice": "Corteza prefrontal ventromedial. Es el pedal de freno del cerebro emocional. En el TLP, este freno se queda sin líquido hidráulico. El paciente sabe racionalmente que autolesionarse o romper un teléfono no resuelve el problema, pero la corteza frontal no tiene la fuerza sináptica para detener la inercia del impulso. Schmahl y Ruocco confirmaron en el American Journal of Psychiatry esta profunda desconexión prefrontal."
            },
            {
                "name": "Cíngulo Anterior Dorsal (dACC)",
                "coords": [0.0, 2.2, 2.6],
                "color": "#f43f5e",
                "rad": 0.45,
                "hz": 7.2,
                "status": "DOLOR SOCIAL AGUDO",
                "desc": "Epicentro de la Red de Prominencia; traduce la distancia vincular en angustia física.",
                "voice": "Cíngulo anterior dorsal. Es la estación central del dolor social. Naomi Eisenberger demostró en la revista Science que el cerebro no distingue la exclusión afectiva de una quemadura física real. Cuando el paciente siente que es ignorado o rechazado, este núcleo se enciende con tal violencia que el dolor físico provocado busca paradójicamente mitigar este dolor psíquico abrumador."
            },
            {
                "name": "Ínsula Anterior Agranular",
                "coords": [3.5, 0.8, -0.1],
                "color": "#e11d48",
                "rad": 0.44,
                "hz": 6.5,
                "status": "HIPEREXCITACIÓN INTEROCEPTIVA",
                "desc": "Sustrato neurofisiológico de la vivencia de vacío crónico y disforia visceral.",
                "voice": "Ínsula anterior agranular. Es el traductor de las vísceras. Aquí reside el correlato biológico de ese agujero en el pecho o vacío crónico que describe el paciente en consultorio; una sensación visceral intolerable que empuja al consumo compulsivo o a la búsqueda desesperada de apego."
            }
        ],
        "tracts": [
            {
                "from": [2.2, -0.6, -1.4], "to": [0.0, 4.2, -0.8], "ctrl": [3.2, 1.8, -2.0],
                "name": "Fascículo Uncinado Derecho",
                "status": "broken",
                "desc": "Tracto axonómico desmielinizado; pérdida de anisotropía fraccional (FA: 0.18).",
                "voice": "Fascículo uncinado derecho. Es el cable de fibra óptica que conecta la razón con la emoción. En el TLP, este cable está deshilachado y con pérdida severa de aislamiento de mielina. La orden de calmarse que envía el lóbulo frontal llega demasiado tarde o degradada a la amígdala."
            },
            {
                "from": [-2.2, -0.6, -1.4], "to": [0.0, 4.2, -0.8], "ctrl": [-3.2, 1.8, -2.0],
                "name": "Fascículo Uncinado Izquierdo",
                "status": "broken",
                "desc": "Interrupción de la conectividad recíproca amígdalo-prefrontal bilateral.",
                "voice": "Fascículo uncinado izquierdo. La tractografía DTI documentada por Schmahl revela una baja anisotropía fraccional bilateral, explicando por qué las crisis emocionales son tan difíciles de regular mediante la lógica convencional."
            },
            {
                "from": [0.0, 2.2, 2.6], "to": [0.0, 4.2, -0.8], "ctrl": [0.0, 3.4, 0.9],
                "name": "Proyección Cíngulo-Frontal",
                "status": "hyper",
                "desc": "Sobrecarga de conflicto social transmitida sin modulación prefrontal.",
                "voice": "Proyección cíngulo-frontal. Bombardea a la corteza ejecutiva con un flujo constante de alarma y sufrimiento, saturando los recursos cognitivos y provocando el clásico bloqueo reflexivo durante el conflicto."
            }
        ],
        "ecosystem": [
            {"name": "Vínculo de Pareja / Apego", "desc": "Splitting, idealización vs devaluación y terror pánico al desapego.", "tension": 0.98, "coords": [6.5, 3.5, 1.8], "color": "#ef4444", "voice": "Esfera de pareja. Opera como un péndulo sin amortiguador. En un instante la pareja es el salvador absoluto, y ante una mínima tardanza pasa a ser el peor enemigo. Este mecanismo de escisión o splitting es la manifestación relacional directa de la desregulación amigdalina."},
            {"name": "Guardia Médica / Urgencias", "desc": "Consultas reiteradas por gestos parasuicidas, sobredosis e impulsividad.", "tension": 0.95, "coords": [-6.0, 4.5, -2.2], "color": "#ef4444", "voice": "Servicio de guardia. El paciente llega en crisis paroxística tras una discusión afectiva, requiriendo contención institucional ante gestos autolesivos que no siempre buscan la muerte, sino silenciar la agonía del dolor psíquico."},
            {"name": "Sentido de Identidad / Self", "desc": "Sensación de vacío insoportable, autodifusión y fluctuación moral.", "tension": 0.94, "coords": [4.5, -5.0, -2.2], "color": "#f43f5e", "voice": "Eje identitario. Es como un camaleón que cambia de color para no morir. El paciente adopta los gustos, valores o ideologías de la persona que tiene al lado por terror a que, al quedarse solo, no quede nada de sí mismo."},
            {"name": "Soporte Familiar Primario", "desc": "Agotamiento de cuidadores, dinámicas de doble vínculo y claudicación.", "tension": 0.88, "coords": [-5.0, -3.5, 3.0], "color": "#fb923c", "voice": "Entorno familiar. Los familiares viven caminando sobre cáscaras de huevo, midiendo cada palabra para no disparar una crisis, lo que a largo plazo agota los recursos de soporte y genera rechazo involuntario."},
            {"name": "Ámbito Académico / Laboral", "desc": "Interrupción de ciclos de estudio/trabajo por crisis afectivas cíclicas.", "tension": 0.70, "coords": [1.8, 6.0, -3.0], "color": "#eab308", "voice": "Ámbito laboral y académico. Se caracteriza por renuncias intempestivas o despidos tras discusiones explosivas con jefes o compañeros, desmoronando carreras promisorias por fallas en la tolerancia a la frustración."}
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
                "coords": [2.2, -0.6, -1.4],
                "color": "#1e293b",
                "rad": 0.35,
                "hz": 0.4,
                "status": "ATROFIA FUNCIONAL",
                "desc": "Inmunidad al condicionamiento por miedo o castigo; refractariedad autonómica.",
                "voice": "Amígdala hipoactiva. Imaginemos un detector de humo al que le quitaron la batería. Aunque haya fuego y sirenas reales alrededor, no emite ningún sonido. Mientras una persona común siente taquicardia y sudoración fría al infringir una regla o al ver llorar a alguien, el individuo psicopático permanece en calma fisiológica absoluta. Craig y Blair demostraron en NeuroImage esta marcada refractariedad autonómica al castigo."
            },
            {
                "name": "vmPFC (Polo Moral Desconectado)",
                "coords": [0.0, 4.2, -0.8],
                "color": "#334155",
                "rad": 0.38,
                "hz": 0.5,
                "status": "HIPOCONECTADA",
                "desc": "Juicio lógico analítico frío, pero sin integración somática del sufrimiento ajeno.",
                "voice": "Corteza prefrontal ventromedial. Funciona como una calculadora financiera desprovista de escrúpulos. La persona comprende con total lucidez las reglas del juego y lo que está bien o mal en términos teóricos, pero esa comprensión no tiene anclaje afectivo. Dañar al otro es simplemente un costo transaccional admisible para alcanzar un objetivo."
            },
            {
                "name": "Núcleo Accumbens (Estriado)",
                "coords": [1.2, 1.4, -0.8],
                "color": "#eab308",
                "rad": 0.52,
                "hz": 7.5,
                "status": "HIPERACTIVIDAD PREDATORIA",
                "desc": "Búsqueda insaciable de recompensa inmediata y dominancia instrumental.",
                "voice": "Núcleo accumbens. Es el motor predatorio de recompensa. Si una persona común ve un fajo de billetes en una mesa ajena, el freno moral inhibe el impulso; aquí el estriado se sobreactiva exigiendo la gratificación inmediata, sin importar las consecuencias legales o el daño causado."
            },
            {
                "name": "Ínsula Anterior (Anestesiada)",
                "coords": [3.5, 0.8, -0.1],
                "color": "#1e293b",
                "rad": 0.32,
                "hz": 0.3,
                "status": "ANESTESIA INTEROCEPTIVA",
                "desc": "Carencia absoluta de culpa visceral o remordimiento somatizado.",
                "voice": "Ínsula anterior anestesiada. Es la sede de la resonancia somática vicaria. Su hipofunción explica por qué estas personas pueden presenciar el dolor de una víctima sin experimentar la menor aversión ni remordimiento en el estómago."
            }
        ],
        "tracts": [
            {
                "from": [2.2, -0.6, -1.4], "to": [0.0, 4.2, -0.8], "ctrl": [3.2, 1.8, -2.0],
                "name": "Fascículo Uncinado (Ablación Conectómica)",
                "status": "broken",
                "desc": "Interrupción casi completa del tracto microestructural (FA: 0.08).",
                "voice": "Fascículo uncinado cortado. Motzkin comprobó en reclusos que la línea de comunicación entre el centro del miedo y el juicio moral está rota. El cerebro no puede enviar la señal de freno somático ante la transgresión."
            },
            {
                "from": [0.0, 4.2, -0.8], "to": [1.2, 1.4, -0.8], "ctrl": [0.6, 2.8, -0.8],
                "name": "Vía Córtico-Estriatal Desinhibida",
                "status": "hyper",
                "desc": "El estriado opera sin freno inhibitorio frontal, facilitando conductas predatorias.",
                "voice": "Vía córtico-estriatal desinhibida. El lóbulo frontal no sólo no frena al núcleo de recompensa, sino que se pone a su servicio para planificar estafas y manipulaciones con frialdad metodológica."
            }
        ],
        "ecosystem": [
            {"name": "Fuero Penal & Penitenciario", "desc": "Reiteración delictiva, crímenes patrimoniales/violentos y encarcelamiento.", "tension": 0.99, "coords": [-7.0, -3.2, 2.2], "color": "#ef4444", "voice": "Fuero penal y penitenciario. El paciente no aprende del castigo ni de la cárcel. Al salir de prisión, la falta de condicionamiento al miedo hace que reincida exactamente en las mismas conductas delictivas."},
            {"name": "Víctimas / Vínculos Explotados", "desc": "Cosificación instrumental, violencia predatoria y despojo patrimonial.", "tension": 0.96, "coords": [6.5, 4.0, 2.5], "color": "#ef4444", "voice": "Vínculos explotados. Las parejas y allegados son considerados meras herramientas o fichas de ajedrez. Una vez que ya no proveen dinero, estatus o placer, son desechados sin el menor atisbo de nostalgia."},
            {"name": "Ámbito Contractual / Financiero", "desc": "Fraudes sistemáticos, estafas y ausencia de lealtad comercial.", "tension": 0.88, "coords": [-4.5, 5.0, -3.0], "color": "#fb923c", "voice": "Ámbito financiero. Creación de empresas fantasma, estafas piramidales y desvío de fondos. La promesa verbal es utilizada como un anzuelo sin intención real de cumplimiento."},
            {"name": "Peritajes Médico-Legales", "desc": "Simulación calculada de trastornos mentales para eludir sanciones penales.", "tension": 0.65, "coords": [3.2, -5.5, -2.6], "color": "#eab308", "voice": "Peritajes forenses. El sujeto simula delirios o amnesia durante el examen psiquiátrico forense para ser declarado inimputable, desarmando la farsa cuando está fuera del ámbito judicial."},
            {"name": "Eje Identitario", "desc": "Egosintonía perfecta; ausencia de autocrítica o malestar interno.", "tension": 0.12, "coords": [5.0, -1.8, 4.0], "color": "#10b981", "voice": "Eje identitario. Plena egosintonía. El individuo no acude voluntariamente a consulta porque no sufre en absoluto; considera que el problema es de los demás por ser débiles o ingenuos."}
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
                "coords": [0.0, 2.2, 2.6],
                "color": "#a855f7",
                "rad": 0.50,
                "hz": 7.4,
                "status": "HIPERREACTIVO AL DESPRECIO",
                "desc": "Alarma desmedida ante el desacato, la crítica o la pérdida de admiración.",
                "voice": "Cíngulo anterior dorsal. Es un radar de jerarquía social en hipervigilancia continua. Por ejemplo, en una reunión de trabajo, si una opinión suya no es aplaudida de inmediato, este núcleo detecta una ofensa mortal a su estatus, detonando una respuesta de furia fría o venganza calculada."
            },
            {
                "name": "vmPFC (Autoimagen Grandiosa)",
                "coords": [0.0, 4.2, -0.8],
                "color": "#c084fc",
                "rad": 0.46,
                "hz": 2.8,
                "status": "COMPENSACIÓN GRANDIOSA",
                "desc": "Mantenimiento activo del constructo de superioridad como defensa ante el vacío.",
                "voice": "Corteza prefrontal ventromedial. Es como construir un andamio de oro sobre cimientos de barro. Se gasta una enorme cantidad de energía metabólica en sostener el relato de que se es superior a todos, precisamente para tapar un terror pánico a la mediocridad o al vacío interior."
            },
            {
                "name": "Amígdala (Rabia Narcisista)",
                "coords": [2.2, -0.6, -1.4],
                "color": "#ec4899",
                "rad": 0.42,
                "hz": 5.2,
                "status": "VULNERABILIDAD FÁSICA",
                "desc": "Explosiones coléricas vindicativas ante la exposición de debilidad.",
                "voice": "Amígdala fásica. Dispara la llamada rabia narcisista. Ante una crítica fundada de un colega o pareja, la herida narcisista desata una reacción colérica desproporcionada que busca descalificar y aniquilar verbalmente al otro para restituir el propio valor dañado."
            },
            {
                "name": "Ínsula (Desconexión Vicaria)",
                "coords": [3.5, 0.8, -0.1],
                "color": "#334155",
                "rad": 0.35,
                "hz": 0.8,
                "status": "ANESTESIA EMPÁTICA",
                "desc": "Incapacidad neurofisiológica de registrar el dolor causado a subordinados.",
                "voice": "Ínsula anterior desconectada. Fan demostró en la revista SCAN la presencia de una disociación clave: el narcisista tiene empatía cognitiva intacta, es decir, sabe perfectamente qué te duele y cómo herirte, pero carece de empatía afectiva, lo que significa que no siente compasión alguna al hacerlo."
            }
        ],
        "tracts": [
            {
                "from": [0.0, 2.2, 2.6], "to": [0.0, 4.2, -0.8], "ctrl": [0.0, 3.4, 0.9],
                "name": "Eje de Autoevaluación Hipervigilante",
                "status": "hyper",
                "desc": "Circuito de monitoreo constante del estatus y de la aprobación externa.",
                "voice": "Eje de autoevaluación. Obliga al sujeto a monitorear obsesivamente cuántos me gusta, aplausos o muestras de sumisión recibe por minuto para mantener equilibrado su estado de ánimo."
            },
            {
                "from": [2.2, -0.6, -1.4], "to": [0.0, 2.2, 2.6], "ctrl": [1.1, 0.7, 0.8],
                "name": "Circuito de Ira Vindicativa",
                "status": "hyper",
                "desc": "Descarga amigdalina directa al cíngulo que alimenta la hostilidad defensiva.",
                "voice": "Circuito de ira vindicativa. Es el puente por donde la herida del orgullo se transforma en desprecio hacia quien osó marcarle un error."
            },
            {
                "from": [3.5, 0.8, -0.1], "to": [0.0, 4.2, -0.8], "ctrl": [2.0, 2.2, -0.5],
                "name": "Desconexión Fronto-Insular",
                "status": "broken",
                "desc": "Bloqueo selectivo de la resonancia afectiva hacia el sufrimiento ajeno.",
                "voice": "Desconexión fronto-insular. El tracto responsable de frenar la crueldad en las relaciones está apagado; el otro es tratado como un objeto utilitario sin costo de conciencia."
            }
        ],
        "ecosystem": [
            {"name": "Vínculo de Pareja", "desc": "Cosificación, exigencia de pleitesía, humillación y ley del hielo.", "tension": 0.92, "coords": [6.0, 3.5, 1.8], "color": "#ef4444", "voice": "Vínculo conyugal. Se establece una dinámica de dominación donde la pareja debe orbitar en torno a sus necesidades. El menor desacuerdo es castigado con semanas de silencio gélido o devaluación humillante."},
            {"name": "Autoimagen & Cohesión del Self", "desc": "Fragilidad extrema; colapso disfórico profundo ante pérdidas de estatus.", "tension": 0.96, "coords": [0.0, -6.5, -2.2], "color": "#a855f7", "voice": "Cohesión del self. Cuando se produce una quiebra real de estatus (una bancarrota, un divorcio público o el envejecimiento), el andamio grandioso se derrumba, dando paso a una depresión disfórica de altísimo riesgo suicida."},
            {"name": "Ámbito Corporativo / Laboral", "desc": "Rivalidades destructivas, litigios por honra y boicot a colaboradores.", "tension": 0.84, "coords": [-5.5, 4.0, 2.8], "color": "#fb923c", "voice": "Ámbito laboral. Como líderes o jefes son tiranos que se apropian de los éxitos de los empleados y culpan a otros de sus propios errores, generando ambientes laborales tóxicos y renuncias masivas."},
            {"name": "Familia de Origen", "desc": "Exigencia de tributo incondicional o ruptura agresiva con exclusión total.", "tension": 0.76, "coords": [-4.5, -4.0, 2.8], "color": "#fb923c", "voice": "Familia de origen. Trata a los hijos como extensiones de su propia imagen. El hijo que triunfa es exhibido como trofeo; el que piensa por sí mismo es desheredado o rechazado."},
            {"name": "Consultas a Salud Mental", "desc": "Abandono de psicoterapia ante señalamientos que confronten la grandiosidad.", "tension": 0.52, "coords": [3.6, 5.5, -2.6], "color": "#38bdf8", "voice": "Consulta psiquiátrica. Llegan derivados o arrastrados por terceros. Ante la primera interpretación del terapeuta que señale sus falencias, abandonan el tratamiento argumentando que el profesional no está a su nivel."}
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
                "coords": [2.2, -0.6, -1.4],
                "color": "#06b6d4",
                "rad": 0.44,
                "hz": 6.2,
                "status": "HIPEREXCITABLE LÁBIL",
                "desc": "Emotividad intensa y cambiante; intolerancia al desinterés del entorno.",
                "voice": "Amígdala límbica lábil. Funciona como fuegos artificiales de corta duración: una explosión de llanto dramático ante una nimiedad, seguida a los diez minutos por risas y seducción como si nada hubiera ocurrido. Es una afectividad tan intensa como superficial."
            },
            {
                "name": "Núcleo Accumbens Social",
                "coords": [1.2, 1.4, -0.8],
                "color": "#22d3ee",
                "rad": 0.48,
                "hz": 6.5,
                "status": "HIPERRESPUESTA AL FEEDBACK",
                "desc": "Dependencia absoluta del halago, la seducción y la validación externa.",
                "voice": "Núcleo accumbens social. Es un circuito adicto a los reflectores. La persona no tolera no ser el centro de atención en una reunión; si la conversación gira hacia otro tema, recurrirá a risas excesivas, seducción inapropiada o una repentina indisposición física para recuperar la mirada de todos."
            },
            {
                "name": "Ínsula Somatosensorial",
                "coords": [3.5, 0.8, -0.1],
                "color": "#0891b2",
                "rad": 0.42,
                "hz": 5.4,
                "status": "SOMATIZACIÓN INTEROCEPTIVA",
                "desc": "Conversión corporal de angustias afectivas; teatralidad física y somatizaciones.",
                "voice": "Ínsula somatosensorial. El teatro no se actúa en palabras, se actúa en el cuerpo. Ante un conflicto interpersonal no resuelto, la ínsula amplifica las señales corporales provocando parálisis funcionales, afonías súbitas o desmayos sin base orgánica."
            },
            {
                "name": "vmPFC Impresionista",
                "coords": [0.0, 4.2, -0.8],
                "color": "#475569",
                "rad": 0.38,
                "hz": 1.4,
                "status": "PROCESAMIENTO DIFUSO",
                "desc": "Falla en el procesamiento lógico analítico; razonamiento guiado por impresiones.",
                "voice": "Corteza prefrontal impresionista. Su estilo cognitivo es como una pintura al óleo vista de lejos: capta el ambiente emocional global pero es incapaz de dar precisiones lógicas o detalladas sobre los hechos que provocaron el conflicto."
            }
        ],
        "tracts": [
            {
                "from": [2.2, -0.6, -1.4], "to": [1.2, 1.4, -0.8], "ctrl": [1.6, 0.4, -1.0],
                "name": "Eje Límbico-Recompensa Interpersonal",
                "status": "hyper",
                "desc": "Circuito reforzador del histrionismo relacional.",
                "voice": "Eje límbico de recompensa. Condiciona la conducta para que el individuo repita permanentemente puestas en escena teatrales que le aseguren la aprobación externa."
            },
            {
                "from": [0.0, 4.2, -0.8], "to": [2.2, -0.6, -1.4], "ctrl": [1.3, 1.8, -1.1],
                "name": "Modulación Frontal Deficitaria",
                "status": "broken",
                "desc": "Falla del control prefrontal para modular la labilidad afectiva.",
                "voice": "Modulación frontal deficitaria. Falla en poner orden y sobriedad cuando la situación amerita contención emocional, como reuniones formales de trabajo o velorios."
            }
        ],
        "ecosystem": [
            {"name": "Vínculo Conyugal / Pareja", "desc": "Seducción inapropiada, celopatía y reclamo permanente de protagonismo.", "tension": 0.85, "coords": [5.5, 3.2, 1.8], "color": "#ef4444", "voice": "Pareja. Exige demostraciones de amor novelescas y apasionadas todos los días. La rutina cotidiana normal es vivida como desamor, provocando celos infundados o coqueteos con terceros para reactivar el drama."},
            {"name": "Guardia Médica de Emergencias", "desc": "Ingresos por síntomas neurológicos funcionales, pseudocrisis o hiperventilación.", "tension": 0.82, "coords": [-4.5, 5.0, -2.2], "color": "#fb923c", "voice": "Guardia médica. Clásica consulta de madrugada por pseudocrisis no epilépticas o crisis de hiperventilación tras una discusión doméstica, requiriendo un abordaje empático pero firme que evite la sobremedicalización innecesaria."},
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
# Motor WebGL Three.js con HUD Compacto no Invasivo y Escala Anatómica
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
    
    /* HUD Lateral Flotante que no tapa el centro del cerebro */
    #hud {{
      position: absolute; top: 75px; left: 16px; z-index: 100;
      background: rgba(11, 19, 41, 0.88); backdrop-filter: blur(12px);
      border: 1px solid #1e293b; border-left: 3px solid #38bdf8; border-radius: 8px;
      padding: 12px 16px; color: #f1f5f9; max-width: 320px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.7); pointer-events: none;
    }}
    .hud-title {{ font-weight: 700; color: #38bdf8; font-size: 0.90rem; margin-bottom: 4px; font-family: monospace; }}
    .hud-desc {{ color: #94a3b8; font-size: 0.76rem; line-height: 1.4; }}
    
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
      <div id="hud-body" class="hud-desc">Arrastra con el ratón para rotar el cerebro 360° o usa la rueda para zoom.<br><br><b>Haz clic en cualquier núcleo</b> para escuchar su explicación clínica y citas.</div>
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
        speakText("Motor de síntesis vocal activado. Selecciona cualquier estructura o vía axonal para escuchar su mecanismo fisiopatológico con ejemplos y evidencia científica.");
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

    // Iluminación
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
    // CONTROL TOTAL CON POINTER EVENTS
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
    // CABLEADO CORTICAL ANATÓMICO (GLASS BRAIN EN WIREFRAME FÓSFORO)
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
          let sulci = 0.28 * Math.sin(8 * u) * Math.cos(7 * v) + 
                      0.18 * Math.sin(16 * v) * Math.cos(4 * u) +
                      0.08 * Math.sin(24 * u);

          let x = (rx + sulci) * Math.sin(v) * Math.cos(u);
          let y = (ry + sulci) * Math.sin(v) * Math.sin(u);
          let z = (rz + sulci) * Math.cos(v);

          // Cisura interhemisférica longitudinal
          if (x >= 0) x += 0.50; else x -= 0.50;
          z -= 0.08 * (y * y) / ry;

          pos.push(x, y, z);
        }}
      }}
      geo.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
      geo.computeVertexNormals();

      const mat = new THREE.MeshPhysicalMaterial({{
        color: 0x38bdf8,
        emissive: 0x0284c7,
        emissiveIntensity: 0.35,
        roughness: 0.2,
        metalness: 0.1,
        transparent: true,
        opacity: DATA.view.includes("1.") ? 0.32 : 0.08,
        wireframe: true,
        depthWrite: false
      }});
      return new THREE.Mesh(geo, mat);
    }}

    const cortexMesh = createAnatomicalGlassCortex();
    modelGroup.add(cortexMesh);

    // -------------------------------------------------------------
    // NODOS EN TAMAÑO ANATÓMICO CALIBRADO (NO GIGANTES)
    // -------------------------------------------------------------
    const clickableObjects = [];
    const pulsingNodes = [];
    const synapticFlows = [];

    if (DATA.view.includes("1.")) {{
      DATA.nodes.forEach(n => {{
        // Esfera central precisa y translúcida
        const geo = new THREE.SphereGeometry(n.rad, 24, 24);
        const mat = new THREE.MeshStandardMaterial({{
          color: n.color,
          emissive: n.color,
          emissiveIntensity: 2.2,
          roughness: 0.2,
          transparent: true,
          opacity: 0.90
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

        // Halo tenue calibrado para que no opaque la pantalla
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

        // Partículas en flujo axonal
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
