import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="Atlas Neurobiológico & Conectómico del Cluster B",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estética de consola médica de neuroimagen
st.markdown("""
<style>
    .stApp { background-color: #020617; color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    h1, h2, h3, h4 { color: #f8fafc; font-weight: 700; letter-spacing: -0.02em; }
    
    .evidence-panel {
        background: #0b1329; border: 1px solid #1e293b; border-left: 3px solid #38bdf8;
        padding: 12px 16px; border-radius: 8px; margin-bottom: 10px;
    }
    .evidence-header { font-size: 0.72rem; text-transform: uppercase; color: #94a3b8; font-weight: 700; letter-spacing: 0.06em; }
    .evidence-title { font-size: 1.15rem; font-weight: 800; color: #38bdf8; font-family: ui-monospace, Menlo, Consolas, monospace; margin: 2px 0; }
    .evidence-body { font-size: 0.78rem; color: #cbd5e1; line-height: 1.4; margin-top: 4px; }
    .evidence-ref { font-size: 0.70rem; color: #64748b; font-style: italic; margin-top: 4px; }
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
        "biomarkers": {
            "dti": {
                "title": "Fascículo Uncinado Bilateral",
                "status": "Anisotropía Fraccional Disminuida (p < 0.001)",
                "ref": "Schmahl et al. (2014, Biol Psychiatry) | New et al. (2009, NeuroImage)",
                "summary": "Desorganización microestructural en sustancia blanca frontolímbica. La vía eferente orbitofrontal no logra transmitir la señal inhibitoria de extinción hacia la amígdala."
            },
            "fmri_amygdala": {
                "title": "Complejo Amigdalino Basolateral",
                "status": "Hiperreactividad Fásica con Falla de Extinción",
                "ref": "Ruocco et al. (2013, Am J Psychiatry meta-analysis)",
                "summary": "Respuesta desproporcionada ante caras neutras o señales de distanciamiento interpersonal, codificadas erróneamente como amenaza inminente de abandono."
            },
            "fmri_pain": {
                "title": "Matriz del Dolor Social (dACC / Ínsula)",
                "status": "Coactivación Paroxística en Exclusión",
                "ref": "Eisenberger & Lieberman (2004, Science) | Domsalla et al. (2014)",
                "summary": "En paradigmas Cyberball, la exclusión vincular recluta exactamente los mismos sustratos nociceptivos que una lesión tisular física aguda."
            },
            "ratio": {
                "title": "Balance Conectómico Frontolímbico",
                "status": "Desacoplamiento Top-Down Severo",
                "ref": "Cullen et al. (2011) | Coccaro et al. (2007)",
                "summary": "Incapacidad del córtex prefrontal ventromedial para reclutar recursos reflexivos (mentalización) durante picos de desregulación simpática."
            }
        },
        "nodes": [
            {
                "name": "Amígdala Basolateral Derecha",
                "coords": [1.9, -0.6, -1.5],
                "color": "#ef4444",
                "rad": 0.40,
                "hz": 8.0,
                "status": "HIPERTRÓFICA FÁSICA",
                "desc": "Alarma paroxística de supervivencia; decodificación errónea de rostros neutros como amenazantes.",
                "voice": "Amígdala basolateral derecha. Imaginemos una alarma de humo ultrasensible que suena ante el simple vapor de una taza de café. En el TLP, un mensaje sin responder por diez minutos es interpretado como una amenaza mortal de abandono inminente. Como demostraron New y colaboradores en NeuroImage, el circuito queda atrapado en una tormenta adrenérgica prolongada sin poder extinguir el miedo."
            },
            {
                "name": "Amígdala Basolateral Izquierda",
                "coords": [-1.9, -0.6, -1.5],
                "color": "#ef4444",
                "rad": 0.40,
                "hz": 8.0,
                "status": "HIPERTRÓFICA FÁSICA",
                "desc": "Descarga simpática autónoma inmediata ante la sospecha de distanciamiento interpersonal.",
                "voice": "Amígdala basolateral izquierda. Dispara taquicardia y terror fisiológico similar al ataque de un depredador ante la mera percepción de frialdad en la pareja."
            },
            {
                "name": "Córtex Prefrontal Ventromedial (vmPFC)",
                "coords": [0.0, 4.2, -1.0],
                "color": "#38bdf8",
                "rad": 0.38,
                "hz": 1.0,
                "status": "COLAPSO INHIBITORIO",
                "desc": "Falla del freno inhibitorio top-down; incapacidad de modular el afecto negativo.",
                "voice": "Corteza prefrontal ventromedial. Es el pedal de freno del cerebro emocional. En el TLP, este freno se queda sin líquido hidráulico. El paciente sabe racionalmente que autolesionarse no resuelve el problema, pero la corteza frontal no tiene la fuerza sináptica para frenar la inercia del impulso. Schmahl y Ruocco confirmaron esta profunda desconexión prefrontal en el American Journal of Psychiatry."
            },
            {
                "name": "Cíngulo Anterior Dorsal (dACC)",
                "coords": [0.0, 1.8, 2.2],
                "color": "#f43f5e",
                "rad": 0.42,
                "hz": 7.2,
                "status": "DOLOR SOCIAL AGUDO",
                "desc": "Epicentro de la Red de Prominencia; traduce la distancia vincular en angustia física.",
                "voice": "Cíngulo anterior dorsal. Es la estación del dolor social. Naomi Eisenberger demostró en Science que el cerebro no distingue la exclusión afectiva de una quemadura física real. Cuando el paciente se siente ignorado, este núcleo se enciende con tal violencia que el dolor físico provocado en autolesiones busca apagar este dolor psíquico abrumador."
            },
            {
                "name": "Ínsula Anterior Agranular",
                "coords": [3.2, 0.7, -0.2],
                "color": "#e11d48",
                "rad": 0.38,
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
                "desc": "Tracto axonómico desmielinizado; pérdida de anisotropía fraccional.",
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
        "functional_domains": [
            {"domain": "Esfera Conyugal & Apego (CIE-11)", "desc": "Splitting, idealización vs devaluación y terror pánico a la separación.", "tension": 0.98, "coords": [6.2, 3.2, 1.6], "color": "#ef4444", "voice": "Esfera de pareja. Opera como un péndulo sin amortiguador. En un instante la pareja es el salvador absoluto, y ante una mínima tardanza pasa a ser el peor enemigo. Este splitting es el reflejo relacional directo de la desregulación amigdalina."},
            {"domain": "Servicio de Urgencias & Salud Mental", "desc": "Consultas reiteradas por gestos parasuicidas, sobredosis e impulsividad.", "tension": 0.95, "coords": [-5.8, 4.2, -2.0], "color": "#ef4444", "voice": "Servicio de guardia. El paciente consulta reiteradamente en crisis aguda tras discusiones afectivas, requiriendo contención ante gestos que no siempre buscan la muerte, sino silenciar el dolor psíquico."},
            {"domain": "Identidad & Cohesión del Self (DSM-5 Sección III)", "desc": "Sensación de vacío insoportable, autodifusión y fluctuación moral.", "tension": 0.94, "coords": [4.2, -4.8, -2.0], "color": "#f43f5e", "voice": "Eje identitario. Es como un camaleón que cambia de color para no morir. Adopta los gustos o valores de la persona que tiene al lado por terror a que, al quedarse solo, no quede nada de sí mismo."},
            {"domain": "Red Familiar Primaria (WHODAS 2.0)", "desc": "Agotamiento crónico de cuidadores, doble vínculo y claudicación vincular.", "tension": 0.88, "coords": [-4.8, -3.2, 2.8], "color": "#fb923c", "voice": "Entorno familiar. La familia vive caminando sobre cáscaras de huevo, midiendo cada palabra para no disparar una crisis, lo que a largo plazo agota los recursos de soporte."},
            {"domain": "Funcionamiento Ocupacional / Académico", "desc": "Interrupción de ciclos productivos por crisis afectivas cíclicas.", "tension": 0.70, "coords": [1.6, 5.6, -2.8], "color": "#eab308", "voice": "Ámbito laboral y académico. Despidos o renuncias intempestivas tras discusiones explosivas, desmoronando trayectorias promisorias por fallas en la tolerancia a la frustración."}
        ]
    },
    "Trastorno Antisocial de la Personalidad (TASP)": {
        "short_key": "TASP",
        "circuit_name": "Ablación Funcional Frontolímbica & Falla de Aversión Moral",
        "color_accent": "#f59e0b",
        "biomarkers": {
            "dti": {
                "title": "Fascículo Uncinado Bilateral",
                "status": "Ablación Microestructural Mayor (FA < 0.10)",
                "ref": "Craig et al. (2009, Mol Psychiatry) | Motzkin et al. (2011, J Neurosci)",
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
                "coords": [1.1, 1.2, -0.8],
                "color": "#eab308",
                "rad": 0.46,
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
                "desc": "Interrupción casi completa del tracto microestructural.",
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
        "functional_domains": [
            {"domain": "Fuero Penal & Penitenciario", "desc": "Reiteración delictiva, crímenes patrimoniales/violentos y encarcelamiento.", "tension": 0.99, "coords": [-6.8, -3.0, 2.0], "color": "#ef4444", "voice": "Fuero penal. El sujeto no aprende del castigo ni de la cárcel. Al salir de prisión, la falta de condicionamiento al miedo hace que reincida exactamente en las mismas conductas delictivas."},
            {"domain": "Víctimas & Vínculos Explotados", "desc": "Cosificación instrumental, violencia predatoria y despojo patrimonial.", "tension": 0.96, "coords": [6.2, 3.8, 2.2], "color": "#ef4444", "voice": "Vínculos explotados. Las personas son consideradas meras fichas de ajedrez. Una vez que ya no proveen dinero o placer, son desechadas sin el menor atisbo de nostalgia."},
            {"domain": "Ámbito Contractual / Financiero", "desc": "Fraudes sistemáticos, estafas y ausencia de lealtad comercial.", "tension": 0.88, "coords": [-4.2, 4.8, -2.8], "color": "#fb923c", "voice": "Ámbito financiero. Creación de fraudes y estafas piramidales. La promesa verbal es utilizada como un anzuelo sin intención real de cumplimiento."},
            {"domain": "Peritajes Médico-Legales", "desc": "Simulación calculada de trastornos mentales para eludir sanciones penales.", "tension": 0.65, "coords": [3.0, -5.2, -2.4], "color": "#eab308", "voice": "Peritajes forenses. El sujeto simula delirios o amnesia durante el examen psiquiátrico forense para ser declarado inimputable, desarmando la farsa cuando está fuera del ámbito judicial."},
            {"domain": "Identidad & Autocrítica (Sección III DSM-5)", "desc": "Egosintonía perfecta; ausencia de autocrítica o malestar interno.", "tension": 0.12, "coords": [4.8, -1.6, 3.8], "color": "#10b981", "voice": "Eje identitario. Plena egosintonía. El individuo no acude voluntariamente a consulta porque no sufre; considera que el problema es de los demás por ser débiles o ingenuos."}
        ]
    },
    "Trastorno Narcisista de la Personalidad (TNP)": {
        "short_key": "TNP",
        "circuit_name": "Disociación Fronto-Insular & Vulnerabilidad al Desprecio",
        "color_accent": "#a855f7",
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
        "nodes": [
            {
                "name": "dACC (Radar de Jerarquía)",
                "coords": [0.0, 1.8, 2.2],
                "color": "#a855f7",
                "rad": 0.44,
                "hz": 7.4,
                "status": "HIPERREACTIVO AL DESPRECIO",
                "desc": "Alarma desmedida ante el desacato, la crítica o la pérdida de admiración.",
                "voice": "Cíngulo anterior dorsal. Es un radar de jerarquía social en hipervigilancia continua. Si una opinión suya no es celebrada, este núcleo detecta una ofensa mortal a su estatus, detonando furia fría o venganza calculada."
            },
            {
                "name": "vmPFC (Autoimagen Grandiosa)",
                "coords": [0.0, 4.2, -1.0],
                "color": "#c084fc",
                "rad": 0.42,
                "hz": 2.8,
                "status": "COMPENSACIÓN GRANDIOSA",
                "desc": "Mantenimiento activo del constructo de superioridad como defensa ante el vacío.",
                "voice": "Corteza prefrontal ventromedial. Es como construir un andamio de oro sobre cimientos de barro. Se gasta una enorme cantidad de energía metabólica en sostener el relato de superioridad, precisamente para tapar el terror al vacío interior."
            },
            {
                "name": "Amígdala (Rabia Narcisista)",
                "coords": [1.9, -0.6, -1.5],
                "color": "#ec4899",
                "rad": 0.36,
                "hz": 5.2,
                "status": "VULNERABILIDAD FÁSICA",
                "desc": "Explosiones coléricas vindicativas ante la exposición de debilidad.",
                "voice": "Amígdala fásica. Dispara la llamada rabia narcisista. Ante una crítica fundada, la herida narcisista desata una reacción colérica que busca descalificar al otro para restituir el propio valor dañado."
            },
            {
                "name": "Ínsula (Desconexión Vicaria)",
                "coords": [3.2, 0.7, -0.2],
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
        "functional_domains": [
            {"domain": "Esfera Conyugal (Dominancia)", "desc": "Cosificación, exigencia de pleitesía, humillación y ley del hielo.", "tension": 0.92, "coords": [5.8, 3.2, 1.6], "color": "#ef4444", "voice": "Vínculo conyugal. Dinámica de dominación donde la pareja debe orbitar en torno a sus necesidades. El menor desacuerdo es castigado con semanas de silencio gélido o devaluación."},
            {"domain": "Cohesión del Self (Riesgo de Colapso)", "desc": "Fragilidad extrema; colapso disfórico profundo ante pérdidas de estatus.", "tension": 0.96, "coords": [0.0, -6.0, -2.0], "color": "#a855f7", "voice": "Cohesión del self. Cuando se produce una quiebra real de estatus (una bancarrota o un divorcio público), el andamio grandioso se derrumba, dando paso a una depresión de altísimo riesgo suicida."},
            {"domain": "Funcionamiento Ocupacional / Jerárquico", "desc": "Rivalidades destructivas, litigios por honra y boicot a colaboradores.", "tension": 0.84, "coords": [-5.2, 3.8, 2.6], "color": "#fb923c", "voice": "Ámbito laboral. Como líderes son tiranos que se apropian de los éxitos ajenos y culpan a otros de sus propios errores, generando ambientes laborales tóxicos y renuncias."},
            {"domain": "Red Familiar de Origen", "desc": "Exigencia de tributo incondicional o ruptura agresiva con exclusión total.", "tension": 0.76, "coords": [-4.2, -3.8, 2.6], "color": "#fb923c", "voice": "Familia de origen. Trata a los hijos como extensiones de su propia imagen. El que triunfa es exhibido como trofeo; el que piensa por sí mismo es desheredado o rechazado."},
            {"domain": "Adherencia a Salud Mental", "desc": "Abandono de psicoterapia ante señalamientos que confronten la grandiosidad.", "tension": 0.52, "coords": [3.4, 5.2, -2.4], "color": "#38bdf8", "voice": "Consulta clínica. Ante la primera interpretación del terapeuta que señale sus falencias, abandonan el tratamiento argumentando que el profesional no está a su nivel."}
        ]
    },
    "Trastorno Histriónico de la Personalidad (THP)": {
        "short_key": "THP",
        "circuit_name": "Labilidad Afectiva, Búsqueda de Refuerzo & Somatización",
        "color_accent": "#06b6d4",
        "biomarkers": {
            "dti": {
                "title": "Vías Frontoparietales Dorsolaterales",
                "status": "Varianza Difusa en Conectividad Frontal",
                "ref": "Buchsbaum et al. | Schore et al. (Neuropsychoanalysis)",
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
                "ref": "Shapiro (Neurotic Styles) | Kernberg (Organización Límite)",
                "summary": "Incapacidad para sostener tareas sistemáticas o anonimato funcional; desorganización conductual ante la pérdida del rol protagónico."
            }
        },
        "nodes": [
            {
                "name": "Amígdala Límbica",
                "coords": [1.9, -0.6, -1.5],
                "color": "#06b6d4",
                "rad": 0.38,
                "hz": 6.2,
                "status": "HIPEREXCITABLE LÁBIL",
                "desc": "Emotividad intensa y cambiante; intolerancia al desinterés del entorno.",
                "voice": "Amígdala límbica lábil. Funciona como fuegos artificiales de corta duración: una explosión de llanto dramático ante una nimiedad, seguida a los diez minutos por risas y seducción. Es una afectividad tan intensa como superficial."
            },
            {
                "name": "Núcleo Accumbens Social",
                "coords": [1.1, 1.2, -0.8],
                "color": "#22d3ee",
                "rad": 0.42,
                "hz": 6.5,
                "status": "HIPERRESPUESTA AL FEEDBACK",
                "desc": "Dependencia absoluta del halago, la seducción y la validación externa.",
                "voice": "Núcleo accumbens social. Circuito adicto a los reflectores. La persona no tolera no ser el centro de atención; si la conversación gira hacia otro tema, recurrirá a seducción inapropiada o una repentina indisposición física para recuperar la mirada de todos."
            },
            {
                "name": "Ínsula Somatosensorial",
                "coords": [3.2, 0.7, -0.2],
                "color": "#0891b2",
                "rad": 0.36,
                "hz": 5.4,
                "status": "SOMATIZACIÓN INTEROCEPTIVA",
                "desc": "Conversión corporal de angustias afectivas; teatralidad física y somatizaciones.",
                "voice": "Ínsula somatosensorial. El teatro no se actúa en palabras, se actúa en el cuerpo. Ante un conflicto no resuelto, la ínsula amplifica las señales corporales provocando parálisis funcionales o desmayos sin base orgánica."
            },
            {
                "name": "vmPFC Impresionista",
                "coords": [0.0, 4.2, -1.0],
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
        "functional_domains": [
            {"domain": "Esfera Conyugal (Dramatismo)", "desc": "Seducción inapropiada, celopatía y reclamo permanente de protagonismo.", "tension": 0.85, "coords": [5.2, 3.0, 1.6], "color": "#ef4444", "voice": "Pareja. Exige demostraciones de amor apasionadas todos los días. La rutina cotidiana normal es vivida como desamor, provocando celos infundados o coqueteos con terceros para reactivar el drama."},
            {"domain": "Servicio de Guardia Médica", "desc": "Ingresos por síntomas neurológicos funcionales, pseudocrisis o hiperventilación.", "tension": 0.82, "coords": [-4.2, 4.8, -2.0], "color": "#fb923c", "voice": "Guardia médica. Clásica consulta de madrugada por pseudocrisis o crisis de hiperventilación tras una discusión, requiriendo un abordaje empático pero firme que evite la sobremedicalización."},
            {"domain": "Red Social Ampliada", "desc": "Relaciones superficiales asumidas como íntimas; agotamiento del entorno.", "tension": 0.72, "coords": [3.8, -4.2, 2.0], "color": "#fb923c", "voice": "Círculo de amistades. Conocen a alguien hace dos días y ya lo consideran su hermano del alma, para luego distanciarse con la misma velocidad ante cualquier pequeñez que no satisfaga su estándar novelesco."},
            {"domain": "Autoestima & Dependencia del Halago", "desc": "Sensación de desvanecimiento subjetivo ante la falta de atención o halago.", "tension": 0.80, "coords": [-1.4, -5.2, -1.6], "color": "#06b6d4", "voice": "Autoestima. Si nadie los mira, sienten literalmente que no existen. Su valor interno es totalmente prestado por la mirada del público circunstancial."},
            {"domain": "Funcionamiento Laboral Sistemático", "desc": "Incapacidad para labores rutinarias o sin visibilidad protagónica.", "tension": 0.50, "coords": [1.8, 5.5, -2.8], "color": "#38bdf8", "voice": "Ámbito laboral. Excelente desenvolvimiento inicial en relaciones públicas o ventas, pero con un rápido agotamiento cuando el rol exige trabajo metódico de archivo o concentración sin público."}
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
st.caption(f"**Circuito Fisiopatológico:** {current_data['circuit_name']}")

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
# Motor WebGL Three.js con Morfología Biofiel y HUD Lateral No Invasivo
# -------------------------------------------------------------------------
payload = {
    "view": view_selector,
    "nodes": current_data["nodes"],
    "tracts": current_data["tracts"],
    "functional_domains": current_data["functional_domains"],
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
      <div id="hud-body" class="hud-desc">Arrastra libremente con el ratón para rotar el encéfalo en 360° o usa la rueda para zoom.<br><br><b>Haz clic en cualquier núcleo o tracto</b> para escuchar su análisis clínico con analogías y citas.</div>
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
        speakText("Motor vocal activado. Selecciona cualquier estructura anatómica o dominio funcional para escuchar su explicación con analogías y citas bibliográficas.");
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

    // Malla anatómica pial biofiel
    function createRealisticBrainCortex() {{
      const uSegs = 100, vSegs = 100;
      const geo = new THREE.BufferGeometry();
      const pos = [];

      for(let i=0; i<=uSegs; i++) {{
        let u = (i / uSegs) * Math.PI * 2;
        for(let j=0; j<=vSegs; j++) {{
          let v = (j / vSegs) * Math.PI;

          let rx = 4.3, ry = 5.9, rz = 4.1;
          let sulci = 0.28 * Math.sin(8 * u) * Math.cos(7 * v) + 
                      0.18 * Math.sin(16 * v) * Math.cos(4 * u) +
                      0.08 * Math.sin(24 * u);

          let x = (rx + sulci) * Math.sin(v) * Math.cos(u);
          let y = (ry + sulci) * Math.sin(v) * Math.sin(u);
          let z = (rz + sulci) * Math.cos(v);

          // Cisura sagital
          if (x >= 0) x += 0.48; else x -= 0.48;

          // Polo temporal en gancho
          if (z < -0.5 && y > -1.5 && y < 2.5) {{
            let tempFactor = Math.sin((y + 1.5) / 4.0 * Math.PI);
            x *= (1.0 + 0.18 * tempFactor);
            z -= 0.35 * tempFactor;
          }}

          // Polo occipital afinado
          if (y < -2.0) {{
            x *= (1.0 - 0.15 * Math.abs(y + 2.0) / 4.0);
          }}

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
      // Modo Matriz de Discapacidad Funcional (WHODAS 2.0 / CIE-11)
      DATA.functional_domains.forEach(e => {{
        const rad = 0.50 + e.tension * 0.25;
        const geo = new THREE.SphereGeometry(rad, 24, 24);
        const mat = new THREE.MeshStandardMaterial({{
          color: e.color,
          emissive: e.color,
          emissiveIntensity: 2.0,
          roughness: 0.3
        }});
        const mesh = new THREE.Mesh(geo, mat);
        mesh.position.set(...e.coords);
        mesh.userData = {{
          name: e.domain,
          desc: e.desc + "<br><b>Severidad de Discapacidad:</b> " + (e.tension * 100).toFixed(0) + "%",
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
# Ficha Técnica y Discusión Nosológica para la Presentación
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
