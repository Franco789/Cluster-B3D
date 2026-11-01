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
        padding: 12px 14px; border-radius: 8px; margin-bottom: 8px;
    }
    .evidence-header { font-size: 0.68rem; text-transform: uppercase; color: #94a3b8; font-weight: 700; letter-spacing: 0.06em; }
    .evidence-title { font-size: 1.05rem; font-weight: 800; color: #38bdf8; font-family: ui-monospace, Menlo, monospace; margin: 2px 0; }
    .evidence-body { font-size: 0.74rem; color: #cbd5e1; line-height: 1.35; margin-top: 3px; }
    .evidence-ref { font-size: 0.68rem; color: #64748b; font-style: italic; margin-top: 4px; }
    
    .clinical-case-box {
        background: #080d1a; border: 1px solid #1e293b; border-left: 4px solid #ef4444;
        padding: 16px 20px; border-radius: 8px; margin-top: 15px; margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# Base de Datos Neurobiológica, Conectómica y Psicométrica Rigurosa
# -------------------------------------------------------------------------
CLINICAL_REGISTRY = {
    "Trastorno Límite de la Personalidad (TLP)": {
        "short_key": "TLP",
        "circuit_name": "Falla del Freno Top-Down & Alarma Nociceptiva del Dolor Social",
        "color_accent": "#ef4444",
        "biomarkers": {
            "dti": {
                "title": "Fascículo Uncinado Bilateral",
                "status": "Anisotropía Fraccional Disminuida (FA < 0.20)",
                "ref": "Schmahl et al. (2014, Biol Psychiatry) | New et al. (2009, NeuroImage)",
                "summary": "Desorganización microestructural en sustancia blanca frontolímbica. El cable de freno inhibitorio entre la corteza orbitofrontal y la amígdala pierde aislamiento de mielina, haciendo que la modulación racional llegue tarde."
            },
            "fmri_amygdala": {
                "title": "Complejo Amigdalino Basolateral",
                "status": "Hiperreactividad Fásica con Falla de Extinción",
                "ref": "Ruocco et al. (2013, Am J Psychiatry meta-analysis)",
                "summary": "Respuesta desproporcionada ante caras neutras o demoras en la comunicación interpersonal, codificadas por la amígdala como abandono o agresión inminente."
            },
            "fmri_pain": {
                "title": "Matriz del Dolor Social (dACC / Ínsula)",
                "status": "Coactivación Paroxística en Exclusión",
                "ref": "Eisenberger & Lieberman (2004, Science) | Domsalla et al. (2014)",
                "summary": "En paradigmas Cyberball, la exclusión vincular recluta los mismos sustratos nociceptivos que una lesión tisular física aguda, explicando la necesidad urgente de mitigar el dolor psíquico."
            },
            "ratio": {
                "title": "Acoplamiento vmPFC-Amígdala",
                "status": "Desacoplamiento Top-Down Severo",
                "ref": "Cullen et al. (2011) | Coccaro et al. (2007)",
                "summary": "Incapacidad de la corteza prefrontal ventromedial para reclutar recursos reflexivos (mentalización) durante picos de desregulación autonómica."
            }
        },
        "case_vignette": {
            "title": "Viñeta Clínica de Guardia: Descompensación por Dolor Social Agudo",
            "narrative": "Paciente de 24 años ingresa a la guardia hospitalaria tras ingerir 15 comprimidos de clonazepam y presentar cortes superficiales en ambos antebrazos. El desencadenante inmediato fue que su pareja canceló una cena de último momento por motivos laborales. Durante la entrevista, la paciente describe: 'Sentí un frío quemante en el pecho, como si dejara de existir; necesitaba que el dolor parara'.",
            "mechanistic_reading": "La cancelación vincular activa el dACC y la ínsula anterior simulando dolor nociceptivo real (Eisenberger, 2004). El fascículo uncinado desmielinizado (Schmahl, 2014) impide que el vmPFC envíe la señal inhibitoria de que 'solo fue un imprevisto laboral', dejando a la amígdala en alarma autonómica continua que culmina en parasuicidio impulsivo."
        },
        "nodes": [
            {
                "name": "Amígdala Basolateral Derecha",
                "coords": [1.8, -0.6, -1.3],
                "color": "#ef4444",
                "rad": 0.38,
                "hz": 8.0,
                "status": "HIPERTRÓFICA FÁSICA",
                "desc": "Alarma paroxística de supervivencia; decodificación errónea de neutralidad como agresión.",
                "voice": "Amígdala basolateral derecha. Imaginemos una alarma de humo ultrasensible que suena ante el simple vapor de una taza de café. En el TLP, un mensaje de texto sin responder durante veinte minutos es decodificado por este núcleo como una catástrofe de abandono inminente. Como demostraron New y Schmahl en NeuroImage, el circuito queda atrapado en una tormenta adrenérgica prolongada sin poder extinguir el miedo."
            },
            {
                "name": "Amígdala Basolateral Izquierda",
                "coords": [-1.8, -0.6, -1.3],
                "color": "#ef4444",
                "rad": 0.38,
                "hz": 8.0,
                "status": "HIPERTRÓFICA FÁSICA",
                "desc": "Descarga simpática autónoma inmediata ante la sospecha de distanciamiento interpersonal.",
                "voice": "Amígdala basolateral izquierda. Desencadena taquicardia, sudoración fría y pánico somático similar al ataque de un depredador ante la mera percepción de distanciamiento de la pareja."
            },
            {
                "name": "Córtex Prefrontal Ventromedial (vmPFC)",
                "coords": [0.0, 3.8, -0.8],
                "color": "#38bdf8",
                "rad": 0.36,
                "hz": 1.0,
                "status": "COLAPSO INHIBITORIO",
                "desc": "Falla del freno inhibitorio top-down; incapacidad de modular el afecto negativo.",
                "voice": "Corteza prefrontal ventromedial. Es el pedal de freno del cerebro emocional. En el TLP, este freno se queda sin líquido hidráulico. El paciente sabe racionalmente que cortarse o agredir verbalmente empeorará las cosas, pero la corteza frontal no tiene la fuerza sináptica para detener la inercia del impulso motor."
            },
            {
                "name": "Cíngulo Anterior Dorsal (dACC)",
                "coords": [0.0, 1.8, 1.8],
                "color": "#f43f5e",
                "rad": 0.40,
                "hz": 7.2,
                "status": "DOLOR SOCIAL AGUDO",
                "desc": "Epicentro de la Red de Prominencia; traduce la distancia vincular en angustia física.",
                "voice": "Cíngulo anterior dorsal. Es la estación central del dolor social. Naomi Eisenberger demostró en la revista Science que el cerebro procesa el rechazo afectivo en los mismos vóxeles que una quemadura física real. Cuando el paciente se siente rechazado, este núcleo se enciende con tal intensidad que la autolesión física busca paradójicamente apagar este dolor psíquico abrumador."
            },
            {
                "name": "Ínsula Anterior Agranular",
                "coords": [2.8, 0.7, -0.2],
                "color": "#e11d48",
                "rad": 0.34,
                "hz": 6.5,
                "status": "HIPEREXCITACIÓN INTEROCEPTIVA",
                "desc": "Sustrato neurofisiológico de la vivencia de vacío crónico y disforia visceral.",
                "voice": "Ínsula anterior agranular. Traduce el malestar psíquico en sensación visceral. Es el correlato biológico de ese agujero en el pecho o vacío intolerable que describe el paciente en consultorio, el cual a menudo precipita conductas purgativas, cortes o consumo compulsivo."
            }
        ],
        "tracts": [
            {
                "from": [1.8, -0.6, -1.3], "to": [0.0, 3.8, -0.8], "ctrl": [2.6, 1.5, -1.6],
                "name": "Fascículo Uncinado Derecho",
                "status": "broken",
                "desc": "Tracto axonómico desmielinizado; pérdida de anisotropía fraccional.",
                "voice": "Fascículo uncinado derecho. Es el cable de fibra óptica que conecta la corteza frontal con la amígdala. En el TLP está deshilachado. La orden de calmarse que emite la razón llega demasiado tarde o degradada al polo límbico."
            },
            {
                "from": [-1.8, -0.6, -1.3], "to": [0.0, 3.8, -0.8], "ctrl": [-2.6, 1.5, -1.6],
                "name": "Fascículo Uncinado Izquierdo",
                "status": "broken",
                "desc": "Interrupción de la conectividad recíproca amígdalo-prefrontal bilateral.",
                "voice": "Fascículo uncinado izquierdo. La tractografía DTI documentada por Schmahl en Biological Psychiatry demuestra una baja anisotropía fraccional bilateral, explicando por qué las crisis son refractarias a la lógica verbal convencional."
            },
            {
                "from": [0.0, 1.8, 1.8], "to": [0.0, 3.8, -0.8], "ctrl": [0.0, 2.8, 0.6],
                "name": "Proyección Cíngulo-Frontal",
                "status": "hyper",
                "desc": "Sobrecarga de conflicto social transmitida sin modulación prefrontal.",
                "voice": "Proyección cíngulo-frontal. Bombardea a la corteza ejecutiva con un flujo constante de angustia, provocando el clásico bloqueo cognitivo donde el paciente afirma no poder pensar con claridad."
            }
        ],
        "whodas_matrix": [
            {
                "domain": "Esfera Conyugal & Apego (CIE-11)",
                "severity": 96,
                "color": "#ef4444",
                "clinical_correlate": "Splitting o escisión defensiva. La pareja oscila entre el rol de salvador absoluto y enemigo hostil; el terror pánico al abandono precipita conductas de control asfixiante que terminan provocando la ruptura temida."
            },
            {
                "domain": "Servicio de Guardia & Salud Mental",
                "severity": 92,
                "color": "#ef4444",
                "clinical_correlate": "Hiperfrecuentación de urgencias por gestos parasuicidas, cortes no suicidas y sobredosis impulsivas como mecanismo biológico urgente para regular la disforia masiva."
            },
            {
                "domain": "Cohesión del Self & Identidad",
                "severity": 94,
                "color": "#f43f5e",
                "clinical_correlate": "Difusión de identidad (Kernberg). Vivencia dolorosa de vacío crónico; metamorfosis de valores, gustos y orientaciones según la figura de apego de turno para evitar la soledad."
            },
            {
                "domain": "Red Familiar Primaria (WHODAS 2.0)",
                "severity": 88,
                "color": "#fb923c",
                "clinical_correlate": "Claudicación de cuidadores. Familiares en estado de hiperalerta continuo, caminando sobre cáscaras de huevo para evitar crisis, lo que a largo plazo genera agotamiento y rechazo involuntario."
            },
            {
                "domain": "Funcionamiento Laboral / Académico",
                "severity": 72,
                "color": "#eab308",
                "clinical_correlate": "Ruptura reiterada de trayectorias formativas o laborales por ausentismo durante crisis disfóricas y desregulaciones interpersonales explosivas con compañeros o superiores."
            }
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
                "summary": "Interrupción casi completa del canal que comunica la señal de miedo/castigo con la corteza orbitofrontal. Desconexión estructural demostrada en poblaciones penitenciarias psicopáticas."
            },
            "fmri_amygdala": {
                "title": "Complejo Amigdalino Basolateral",
                "status": "Hipoactividad e Inmunidad al Condicionamiento",
                "ref": "Blair et al. (2004, NeuroImage) | Birbaumer et al. (2005)",
                "summary": "Ausencia de activación hemodinámica ante expresiones faciales de dolor o miedo ajeno. Cero respuesta autonómica electrodérmica ante la anticipación de castigo."
            },
            "fmri_pain": {
                "title": "Ínsula Anterior (Empatía Afectiva)",
                "status": "Anestesia Somatosensorial Vicaria",
                "ref": "Glenn & Raine (2014) | Decety et al. (2013)",
                "summary": "Falla en la activación insular frente al sufrimiento de terceros. Teoría de la Mente cognitiva intacta (capacidad de engaño) con anestesia de la compasión somatizada."
            },
            "ratio": {
                "title": "Bucle Córtico-Estriatal Predatorio",
                "status": "Sensibilidad Extrema a Ganancia Inmediata",
                "ref": "Buckholtz et al. (2010, Nature Neurosci)",
                "summary": "Hiperreactividad dopaminérgica del núcleo accumbens orientada a recompensas instrumentales inmediatas, sin que el lóbulo frontal compute costo moral ni riesgo punitivo."
            }
        },
        "case_vignette": {
            "title": "Viñeta Clínica Forense: Peritaje Penal por Estafa Reincidente y Violencia",
            "narrative": "Sujeto de 32 años evaluado en el fuero penal tras estafar a su círculo familiar directo y agredir físicamente a un socio comercial. Durante la evaluación pericial psiquiátrica se muestra relajado, simpático y con discurso seductor. Al preguntarle por el impacto económico y emocional en sus padres mayores, responde sonriendo: 'Ellos tenían los ahorros guardados sin usarlos; yo los puse a trabajar. Se ahogan en un vaso de agua'. Frecuencia cardíaca basal: 58 latidos por minuto.",
            "mechanistic_reading": "La bradicardia y la ausencia de sudoración ilustran la hiporreactividad amigdalina descrita por Blair (2004). El fascículo uncinado desconectado (Motzkin, 2011) impide que la noción moral de 'daño a los padres' frene la sobreactivación estriatal del núcleo accumbens, la cual opera exclusivamente bajo la búsqueda de incentivo material inmediato (Buckholtz, 2010)."
        },
        "nodes": [
            {
                "name": "Amígdala (Hipoactiva / Atrofiada)",
                "coords": [1.8, -0.6, -1.3],
                "color": "#1e293b",
                "rad": 0.28,
                "hz": 0.4,
                "status": "ATROFIA FUNCIONAL",
                "desc": "Inmunidad al condicionamiento por miedo o castigo; refractariedad autonómica.",
                "voice": "Amígdala hipoactiva. Imaginemos un detector de humo al que le quitaron la batería. Aunque haya fuego real alrededor, no suena. Mientras una persona común experimenta taquicardia al romper una regla o ver llorar a alguien, el individuo psicopático permanece en calma fisiológica absoluta. Craig y Blair demostraron en NeuroImage esta marcada inmunidad al castigo."
            },
            {
                "name": "vmPFC (Polo Moral Desconectado)",
                "coords": [0.0, 3.8, -0.8],
                "color": "#334155",
                "rad": 0.32,
                "hz": 0.5,
                "status": "HIPOCONECTADA",
                "desc": "Juicio lógico analítico frío, pero sin integración somática del sufrimiento ajeno.",
                "voice": "Corteza prefrontal ventromedial. Funciona como una calculadora desprovista de escrúpulos. Comprende las leyes y lo prohibido a nivel puramente conceptual, pero esa comprensión no tiene anclaje afectivo. Dañar al otro es simplemente un costo operativo admisible para conseguir un fin."
            },
            {
                "name": "Núcleo Accumbens (Estriado)",
                "coords": [1.0, 1.1, -0.7],
                "color": "#eab308",
                "rad": 0.44,
                "hz": 7.5,
                "status": "HIPERACTIVIDAD PREDATORIA",
                "desc": "Búsqueda insaciable de recompensa inmediata y dominancia instrumental.",
                "voice": "Núcleo accumbens estriatal. Es el motor predatorio de recompensa. Si una persona común ve la oportunidad de estafar, el freno moral bloquea el impulso; aquí el estriado se sobreactiva exigiendo la ganancia inmediata, sin importar el daño causado."
            },
            {
                "name": "Ínsula Anterior (Anestesiada)",
                "coords": [2.8, 0.7, -0.2],
                "color": "#1e293b",
                "rad": 0.26,
                "hz": 0.3,
                "status": "ANESTESIA INTEROCEPTIVA",
                "desc": "Carencia absoluta de culpa visceral o remordimiento somatizado.",
                "voice": "Ínsula anterior anestesiada. Es la sede de la empatía somatizada. Su hipofunción explica por qué pueden presenciar la ruina o el dolor de una víctima sin experimentar la menor aversión ni remordimiento en el estómago."
            }
        ],
        "tracts": [
            {
                "from": [1.8, -0.6, -1.3], "to": [0.0, 3.8, -0.8], "ctrl": [2.6, 1.5, -1.6],
                "name": "Fascículo Uncinado (Ablación Conectómica)",
                "status": "broken",
                "desc": "Interrupción casi completa del tracto microestructural.",
                "voice": "Fascículo uncinado cortado. Motzkin comprobó en reclusos que la línea de transmisión entre el centro del miedo y el juicio moral está fracturada. El cerebro no puede enviar la señal de freno somático ante la transgresión."
            },
            {
                "from": [0.0, 3.8, -0.8], "to": [1.0, 1.1, -0.7], "ctrl": [0.5, 2.4, -0.6],
                "name": "Vía Córtico-Estriatal Desinhibida",
                "status": "hyper",
                "desc": "El estriado opera sin freno inhibitorio frontal, facilitando conductas predatorias.",
                "voice": "Vía córtico-estriatal desinhibida. El lóbulo frontal no frena al núcleo de recompensa; se pone a su servicio para planificar estafas y manipulaciones con frialdad metodológica."
            }
        ],
        "whodas_matrix": [
            {
                "domain": "Fuero Penal & Sistema Judicial",
                "severity": 99,
                "color": "#ef4444",
                "clinical_correlate": "Reincidencia delictiva sistemática. Condenas por delitos patrimoniales, estafas o agresiones. La privación de la libertad no genera condicionamiento aversivo por falla amigdalina basal."
            },
            {
                "domain": "Esfera Vincular & Instrumentalización",
                "severity": 96,
                "color": "#ef4444",
                "clinical_correlate": "Cosificación utilitaria del prójimo. Relaciones afectivas concebidas como transacciones de poder, estatus o dinero, desechando a la persona cuando deja de ser útil."
            },
            {
                "domain": "Ámbito Contractual & Financiero",
                "severity": 90,
                "color": "#fb923c",
                "clinical_correlate": "Estafas premeditadas, fraudes y deshonestidad crónica. La palabra empeñada se utiliza como anzuelo estratégico sin intención real de cumplimiento de acuerdos."
            },
            {
                "domain": "Simulación Médico-Forense",
                "severity": 65,
                "color": "#eab308",
                "clinical_correlate": "Uso instrumental del sistema psiquiátrico. Simulación deliberada de delirios o amnesia durante peritajes con el objetivo de lograr eximición de pena o inimputabilidad."
            },
            {
                "domain": "Insight & Conciencia de Enfermedad",
                "severity": 10,
                "color": "#10b981",
                "clinical_correlate": "Plena egosintonía. Cero demanda voluntaria de tratamiento; la persona no experimenta sufrimiento intrapsíquico y atribuye el problema a la debilidad o ingenuidad del entorno."
            }
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
        "case_vignette": {
            "title": "Viñeta Clínica de Consultorio: Colapso Disfórico por Pérdida de Jerarquía",
            "narrative": "Hombre de 48 años, alto ejecutivo corporativo, consulta traído por su cónyuge tras ser removido de su cargo directivo durante una reestructuración de la empresa. Presenta insomnio global, desinterés vital profundo e ideación tanática pasiva. En la consulta expresa con amargura: 'No puedo tolerar que esos mediocres me miren con lástima en el club; prefiero no despertar más'. Rechaza tajantemente el diagnóstico de depresión considerándolo 'indigno de su historia'.",
            "mechanistic_reading": "El despido quiebra el andamio grandioso sostenido por la red por defecto (Scalabrini, 2017). La herida narcisista detona una activación del dACC y amígdala (Pincus, 2010) que, al no poder ser metabolizada mediante dominancia externa, colapsa en disforia melancólica con alto riesgo de suicidio vindicativo para evitar la vergüenza."
        },
        "nodes": [
            {
                "name": "dACC (Radar de Jerarquía)",
                "coords": [0.0, 1.8, 1.8],
                "color": "#a855f7",
                "rad": 0.42,
                "hz": 7.4,
                "status": "HIPERREACTIVO AL DESPRECIO",
                "desc": "Alarma desmedida ante el desacato, la crítica o la pérdida de admiración.",
                "voice": "Cíngulo anterior dorsal. Es un radar de jerarquía social en hipervigilancia continua. Si una opinión suya no es aplaudida de inmediato, este núcleo detecta una ofensa mortal a su estatus, detonando una respuesta de furia fría o venganza calculada."
            },
            {
                "name": "vmPFC (Autoimagen Grandiosa)",
                "coords": [0.0, 3.8, -0.8],
                "color": "#c084fc",
                "rad": 0.38,
                "hz": 2.8,
                "status": "COMPENSACIÓN GRANDIOSA",
                "desc": "Mantenimiento activo del constructo de superioridad como defensa ante el vacío.",
                "voice": "Corteza prefrontal ventromedial. Es como construir un andamio de oro sobre cimientos de barro. Se gasta una enorme cantidad de energía metabólica en sostener el relato de que se es superior a todos, precisamente para tapar un terror pánico a la mediocridad o al vacío interior."
            },
            {
                "name": "Amígdala (Rabia Narcisista)",
                "coords": [1.8, -0.6, -1.3],
                "color": "#ec4899",
                "rad": 0.34,
                "hz": 5.2,
                "status": "VULNERABILIDAD FÁSICA",
                "desc": "Explosiones coléricas vindicativas ante la exposición de debilidad.",
                "voice": "Amígdala fásica. Dispara la llamada rabia narcisista. Ante una crítica fundada de un subordinado o pareja, la herida narcisista desata una reacción colérica que busca descalificar y aniquilar verbalmente al otro para restituir el propio valor dañado."
            },
            {
                "name": "Ínsula (Desconexión Vicaria)",
                "coords": [2.8, 0.7, -0.2],
                "color": "#334155",
                "rad": 0.28,
                "hz": 0.8,
                "status": "ANESTESIA EMPÁTICA",
                "desc": "Incapacidad neurofisiológica de registrar el dolor causado a subordinados.",
                "voice": "Ínsula anterior desconectada. Fan demostró en la revista SCAN que el narcisista tiene empatía cognitiva intacta, es decir, sabe perfectamente qué te duele y cómo herirte, pero carece de empatía afectiva; no siente compasión alguna al hacerlo."
            }
        ],
        "tracts": [
            {
                "from": [0.0, 1.8, 1.8], "to": [0.0, 3.8, -0.8], "ctrl": [0.0, 2.8, 0.6],
                "name": "Eje de Autoevaluación Hipervigilante",
                "status": "hyper",
                "desc": "Circuito de monitoreo constante del estatus y de la aprobación externa.",
                "voice": "Eje de autoevaluación. Obliga al sujeto a monitorear obsesivamente cuántos aplausos o muestras de sumisión recibe por minuto para mantener equilibrada su autoestima."
            },
            {
                "from": [1.8, -0.6, -1.3], "to": [0.0, 1.8, 1.8], "ctrl": [0.9, 0.6, 0.5],
                "name": "Circuito de Ira Vindicativa",
                "status": "hyper",
                "desc": "Descarga amigdalina directa al cíngulo que alimenta la hostilidad defensiva.",
                "voice": "Circuito de ira vindicativa. Es el puente por donde la herida del orgullo se transforma en desprecio hacia quien osó marcarle un error."
            },
            {
                "from": [2.8, 0.7, -0.2], "to": [0.0, 3.8, -0.8], "ctrl": [1.5, 1.6, -0.4],
                "name": "Desconexión Fronto-Insular",
                "status": "broken",
                "desc": "Bloqueo selectivo de la resonancia afectiva hacia el sufrimiento ajeno.",
                "voice": "Desconexión fronto-insular. El tracto responsable de frenar la crueldad relacional está apagado; el otro es tratado como un objeto utilitario sin costo de conciencia."
            }
        ],
        "whodas_matrix": [
            {
                "domain": "Esfera Conyugal (Dinámica de Poder)",
                "severity": 92,
                "color": "#ef4444",
                "clinical_correlate": "Exigencia de pleitesía incondicional. El cónyuge es utilizado como espejo de admiración; el menor desacuerdo es castigado con semanas de silencio gélido o devaluación sistemática."
            },
            {
                "domain": "Cohesión del Self (Riesgo de Colapso)",
                "severity": 95,
                "color": "#a855f7",
                "clinical_correlate": "Fragilidad extrema. Ante pérdidas objetivas de estatus o bancarrotas, el andamio grandioso se derrumba, dando paso a depresiones colapsadas con altísimo riesgo de suicidio vindicativo."
            },
            {
                "domain": "Entorno Laboral & Jerárquico",
                "severity": 84,
                "color": "#fb923c",
                "clinical_correlate": "Liderazgos tiránicos. Apropiación del crédito ajeno, boicot a colaboradores brillantes y litigios corporativos constantes por cuestiones de honor personal."
            },
            {
                "domain": "Red Familiar de Origen",
                "severity": 76,
                "color": "#fb923c",
                "clinical_correlate": "Instrumentalización de hijos y parientes. Los descendientes son tratados como extensiones de su propia imagen y desheredados o repudiados si manifiestan autonomía de criterio."
            },
            {
                "domain": "Adherencia a Salud Mental",
                "severity": 50,
                "color": "#38bdf8",
                "clinical_correlate": "Alta deserción terapéutica. Abandono prematuro de tratamiento si el profesional señala aspectos disfuncionales o no valida su supuesta superioridad."
            }
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
                "ref": "Shapiro (Neurotic Styles) | Kernberg",
                "summary": "Incapacidad para sostener tareas sistemáticas o anonimato funcional; desorganización conductual ante la pérdida del rol protagónico."
            }
        },
        "case_vignette": {
            "title": "Viñeta Clínica de Urgencias: Crisis Somatomorfa tras Desatención Social",
            "narrative": "Mujer de 29 años ingresa en ambulancia a la guardia médica con paresia súbita de miembros inferiores e hiperventilación. El cuadro inició en una fiesta familiar cuando su hermana menor anunció su compromiso matrimonial y todos los presentes se concentraron en felicitarla. La paciente comenzó a sentirse 'desvanecer' y cayó al suelo sin pérdida real de conocimiento ni relajación de esfínteres. Estudios de laboratorio y tomografía sin hallazgos patológicos.",
            "mechanistic_reading": "La pérdida del foco de atención activa la ínsula somatosensorial (Perez, 2015) traduciendo la angustia de invisibilidad en un síntoma conversivo físico que recupera de inmediato el centro de la escena, ilustrando la cognición impresionista descrita por Shapiro."
        },
        "nodes": [
            {
                "name": "Amígdala Límbica",
                "coords": [1.8, -0.6, -1.3],
                "color": "#06b6d4",
                "rad": 0.36,
                "hz": 6.2,
                "status": "HIPEREXCITABLE LÁBIL",
                "desc": "Emotividad intensa y cambiante; intolerancia al desinterés del entorno.",
                "voice": "Amígdala límbica lábil. Funciona como fuegos artificiales de corta duración: una explosión de llanto dramático ante una nimiedad, seguida a los diez minutos por risas y seducción. Es una afectividad tan intensa como superficial."
            },
            {
                "name": "Núcleo Accumbens Social",
                "coords": [1.0, 1.1, -0.7],
                "color": "#22d3ee",
                "rad": 0.40,
                "hz": 6.5,
                "status": "HIPERRESPUESTA AL FEEDBACK",
                "desc": "Dependencia absoluta del halago, la seducción y la validación externa.",
                "voice": "Núcleo accumbens social. Circuito adicto a los reflectores. La persona no tolera no ser el centro de atención; si la conversación gira hacia otro tema, recurrirá a seducción inapropiada o una repentina indisposición física para recuperar la mirada de todos."
            },
            {
                "name": "Ínsula Somatosensorial",
                "coords": [2.8, 0.7, -0.2],
                "color": "#0891b2",
                "rad": 0.34,
                "hz": 5.4,
                "status": "SOMATIZACIÓN INTEROCEPTIVA",
                "desc": "Conversión corporal de angustias afectivas; teatralidad física y somatizaciones.",
                "voice": "Ínsula somatosensorial. El teatro no se actúa en palabras, se actúa en el cuerpo. Ante un conflicto no resuelto, la ínsula amplifica las señales corporales provocando parálisis funcionales o desmayos sin base orgánica."
            },
            {
                "name": "vmPFC Impresionista",
                "coords": [0.0, 3.8, -0.8],
                "color": "#475569",
                "rad": 0.32,
                "hz": 1.4,
                "status": "PROCESAMIENTO DIFUSO",
                "desc": "Falla en el procesamiento lógico analítico; razonamiento guiado por impresiones.",
                "voice": "Corteza prefrontal impresionista. Su estilo cognitivo es como una pintura al óleo vista de lejos: capta el ambiente emocional global pero es incapaz de dar precisiones lógicas sobre los hechos que provocaron el conflicto."
            }
        ],
        "tracts": [
            {
                "from": [1.8, -0.6, -1.3], "to": [1.0, 1.1, -0.7], "ctrl": [1.3, 0.4, -0.8],
                "name": "Eje Límbico-Recompensa Interpersonal",
                "status": "hyper",
                "desc": "Circuito reforzador del histrionismo relacional.",
                "voice": "Eje límbico de recompensa. Condiciona la conducta para que el individuo repita permanentemente puestas en escena teatrales que le aseguren la aprobación externa."
            },
            {
                "from": [0.0, 3.8, -0.8], "to": [1.8, -0.6, -1.3], "ctrl": [0.9, 1.4, -0.9],
                "name": "Modulación Frontal Deficitaria",
                "status": "broken",
                "desc": "Falla del control prefrontal para modular la labilidad afectiva.",
                "voice": "Modulación frontal deficitaria. Falla en poner orden y sobriedad cuando la situación amerita contención emocional, como reuniones formales de trabajo o velorios."
            }
        ],
        "whodas_matrix": [
            {
                "domain": "Esfera Conyugal (Sobredramatización)",
                "severity": 85,
                "color": "#ef4444",
                "clinical_correlate": "Reclamo continuo de pasión novelesca. Intolerancia a la calma cotidiana de convivencia; creación deliberada de crisis o coqueteos con terceros para reactivar la adrenalina del vínculo."
            },
            {
                "domain": "Servicio de Guardia Médica",
                "severity": 82,
                "color": "#fb923c",
                "clinical_correlate": "Consultas reiteradas en urgencias por pseudocrisis conversivas, parestesias no orgánicas o hiperventilación tras discusiones interpersonales menores."
            },
            {
                "domain": "Red Social Ampliada",
                "severity": 72,
                "color": "#fb923c",
                "clinical_correlate": "Idealización acelerada de conocidos recientes ('hermanos del alma') con posterior distanciamiento abrupto ante el agotamiento del entorno frente a demandas teatrales."
            },
            {
                "domain": "Autoestima & Dependencia Externa",
                "severity": 80,
                "color": "#06b6d4",
                "clinical_correlate": "Vivencia de desaparición psicológica si no se cuenta con la mirada atenta del público; autovaloración prestada de forma exclusiva por la validación externa."
            },
            {
                "domain": "Funcionamiento Laboral Sistemático",
                "severity": 50,
                "color": "#38bdf8",
                "clinical_correlate": "Baja tolerancia a tareas metódicas, rutinarias o de archivo que carezcan de exposición social protagónica o halago inmediato."
            }
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
    "whodas": current_data["whodas_matrix"],
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
          desc: "<b>Severidad de Discapacidad:</b> " + e.severity + "%<br>" + e.clinical_correlate,
          voice: e.domain + ". Severidad estimada del " + e.severity + " por ciento. " + e.clinical_correlate
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
# Viñeta Clínica y Lectura Fisiopatológica Dinámica por Cuadro
# -------------------------------------------------------------------------
st.markdown("---")
cv = current_data["case_vignette"]
st.markdown(f"""
<div class="clinical-case-box">
    <h3 style="color: #ef4444; margin: 0 0 8px 0;">📋 {cv['title']}</h3>
    <p style="color: #f8fafc; font-size: 0.90rem; line-height: 1.5; margin-bottom: 12px;"><b>Historia de Guardia / Consultorio:</b><br>{cv['narrative']}</p>
    <div style="background: rgba(15, 23, 42, 0.7); border-left: 3px solid #38bdf8; padding: 10px 14px; border-radius: 4px;">
        <b style="color: #38bdf8; font-size: 0.85rem;">Correlación Fisiopatológica Mecánica:</b><br>
        <span style="color: #cbd5e1; font-size: 0.82rem; line-height: 1.45;">{cv['mechanistic_reading']}</span>
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# Matriz Psicométrica y Conductual de Discapacidad (WHODAS 2.0 / CIE-11)
# -------------------------------------------------------------------------
st.subheader("📊 Matriz de Discapacidad Funcional y Ruptura Relacional")
st.caption("Operacionalización según criterios CIE-11 y escala WHODAS 2.0 de la Organización Mundial de la Salud")

matrix_cols = st.columns(len(current_data["whodas_matrix"]))
for idx, item in enumerate(current_data["whodas_matrix"]):
    with matrix_cols[idx]:
        st.markdown(f"""
        <div style="background: #0b1329; border: 1px solid #1e293b; border-top: 4px solid {item['color']}; padding: 12px; border-radius: 6px; min-height: 190px;">
            <div style="font-size: 0.68rem; text-transform: uppercase; color: #94a3b8; font-weight: 700;">{item['domain']}</div>
            <div style="font-size: 1.35rem; font-weight: 800; color: {item['color']}; margin: 4px 0;">{item['severity']}% <small style="font-size:0.65rem; color:#94a3b8;">Severidad</small></div>
            <div style="font-size: 0.74rem; color: #cbd5e1; line-height: 1.35;">{item['clinical_correlate']}</div>
        </div>
        """, unsafe_allow_html=True)
