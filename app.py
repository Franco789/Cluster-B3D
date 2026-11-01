import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="Atlas Neurobiológico & Conectómico del Cluster B",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estética de consola médica de alta precisión
st.markdown("""
<style>
    .stApp { background-color: #020617; color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    h1, h2, h3, h4 { color: #f8fafc; font-weight: 700; letter-spacing: -0.02em; }
    
    .evidence-panel {
        background: #0b1329; border: 1px solid #1e293b; border-left: 3px solid #38bdf8;
        padding: 12px 14px; border-radius: 8px; margin-bottom: 8px;
    }
    .evidence-header { font-size: 0.68rem; text-transform: uppercase; color: #94a3b8; font-weight: 700; letter-spacing: 0.06em; }
    .evidence-title { font-size: 1.02rem; font-weight: 800; color: #38bdf8; font-family: ui-monospace, Menlo, monospace; margin: 2px 0; }
    .evidence-body { font-size: 0.75rem; color: #cbd5e1; line-height: 1.4; margin-top: 4px; }
    .evidence-ref { font-size: 0.68rem; color: #64748b; font-style: italic; margin-top: 4px; }
    
    .clinical-case-box {
        background: #080d1a; border: 1px solid #1e293b; border-left: 4px solid #ef4444;
        padding: 16px 20px; border-radius: 8px; margin-top: 15px; margin-bottom: 15px;
    }
    .disclaimer-box {
        background: rgba(15, 23, 42, 0.7); border: 1px solid #334155; border-radius: 6px;
        padding: 8px 14px; font-size: 0.74rem; color: #94a3b8; margin-bottom: 12px; line-height: 1.35;
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
                "header": "Resonancia por Tensor de Difusión (DTI)",
                "title": "Fascículo Uncinado Bilateral",
                "status": "Anisotropía Fraccional Disminuida (FA < 0.20)",
                "ref": "Schmahl et al. (2014, Biol Psychiatry) | New et al. (2009, NeuroImage)",
                "summary": "Pérdida de integridad microestructural en sustancia blanca frontolímbica. La vía que comunica la corteza orbitofrontal con la amígdala presenta un menor aislamiento axonal, retrasando la modulación del afecto negativo."
            },
            "fmri_amygdala": {
                "header": "Resonancia Funcional / BOLD (Nivel de Oxigenación)",
                "title": "Complejo Amigdalino Basolateral",
                "status": "Hiperreactividad Fásica con Retardo en Extinción",
                "ref": "Ruocco et al. (2013, Am J Psychiatry meta-análisis de 28 estudios)",
                "summary": "Respuesta desproporcionada ante caras neutras o pausas interpersonales breves, que son codificadas por la amígdala como amenaza inminente de separación o rechazo."
            },
            "fmri_pain": {
                "header": "Red de Prominencia (Salience Network)",
                "title": "Cíngulo Dorsal (dACC) e Ínsula Anterior",
                "status": "Coactivación Paroxística ante la Exclusión",
                "ref": "Eisenberger & Lieberman (2004, Science) | Domsalla et al. (2014)",
                "summary": "En paradigmas experimentales de exclusión (Cyberball), la distancia vincular recluta los mismos circuitos nociceptivos que el dolor somático agudo, induciendo una vivencia física intolerable."
            },
            "ratio": {
                "header": "Acoplamiento Frontolímbico",
                "title": "Corteza Prefrontal Ventromedial (vmPFC)",
                "status": "Desacoplamiento Inhibitorio Top-Down",
                "ref": "Cullen et al. (2011) | Coccaro et al. (2007)",
                "summary": "Dificultad de la corteza prefrontal ventromedial para reclutar recursos reflexivos (mentalización) durante estados de desregulación autonómica elevada."
            }
        },
        "case_vignette": {
            "title": "Viñeta Clínica Ilustrativa: Descompensación Afectiva Aguda",
            "narrative": "Paciente de 24 años consulta en guardia de salud mental tras ingerir una dosis excesiva de ansiolíticos y presentar lesiones cortantes superficiales en el antebrazo. El hecho precipitante fue una demora de tres horas de su pareja en responder un mensaje tras una discusión menor. Durante la entrevista refiere: 'Sentí un frío quemante en el pecho, como si dejara de existir; necesitaba que el dolor parara de inmediato'.",
            "mechanistic_reading": "La percepción de distanciamiento activa el dACC y la ínsula anterior simulando una agresión tisular real (Eisenberger, 2004). El fascículo uncinado desorganizado (Schmahl, 2014) no transmite a tiempo la modulación del vmPFC, impidiendo contextualizar la demora y favoreciendo la conducta impulsiva como intento de regulación afectiva extrema."
        },
        "nodes": [
            {
                "name": "Amígdala Basolateral Derecha",
                "coords": [1.9, -0.6, -1.3],
                "color": "#ef4444",
                "rad": 0.40,
                "hz": 8.0,
                "status": "HIPERTRÓFICA FÁSICA",
                "desc": "Alarma paroxística; decodifica la neutralidad o la pausa vincular como amenaza inminente.",
                "voice": "Amígdala basolateral derecha. Imaginemos una alarma de humo ultrasensible que se activa no solo ante el fuego, sino ante el simple vapor de una taza de café. En el trastorno límite, un mensaje sin responder durante media hora es interpretado como un riesgo vital de abandono. New y colaboradores documentaron en NeuroImage que este núcleo presenta un retardo significativo en extinguir la señal de miedo."
            },
            {
                "name": "Amígdala Basolateral Izquierda",
                "coords": [-1.9, -0.6, -1.3],
                "color": "#ef4444",
                "rad": 0.40,
                "hz": 8.0,
                "status": "HIPERTRÓFICA FÁSICA",
                "desc": "Descarga simpática autónoma inmediata ante la vivencia de separación afectiva.",
                "voice": "Amígdala basolateral izquierda. Desencadena taquicardia, sensación de opresión y pánico somático similar al encuentro con un peligro físico, frente a la sospecha de distanciamiento interpersonal."
            },
            {
                "name": "Córtex Prefrontal Ventromedial (vmPFC)",
                "coords": [0.0, 3.8, -0.8],
                "color": "#38bdf8",
                "rad": 0.38,
                "hz": 1.0,
                "status": "COLAPSO INHIBITORIO",
                "desc": "Falla del freno inhibitorio; incapacidad de modular el afecto negativo en crisis.",
                "voice": "Corteza prefrontal ventromedial. Actúa como el pedal de freno del cerebro emocional. En este cuadro, el freno pierde eficacia hidráulica durante la crisis. Aunque la persona comprenda racionalmente que autolesionarse o increpar empeorará la situación, la corteza no logra ejercer la fuerza sináptica necesaria para detener la inercia del impulso."
            },
            {
                "name": "Cíngulo Anterior Dorsal (dACC)",
                "coords": [0.0, 1.8, 1.8],
                "color": "#f43f5e",
                "rad": 0.42,
                "hz": 7.2,
                "status": "DOLOR SOCIAL AGUDO",
                "desc": "Epicentro de la Red de Prominencia; traduce el rechazo vincular en vivencia física de dolor.",
                "voice": "Córtex cingulado anterior dorsal. Es el nodo central del dolor social. Naomi Eisenberger demostró en la revista Science que el cerebro procesa la exclusión en los mismos circuitos que una quemadura somática. Ante la vivencia de rechazo, este núcleo se activa con tal intensidad que la autolesión suele buscar, de manera disfuncional, atenuar un dolor psíquico que resulta intolerable."
            },
            {
                "name": "Ínsula Anterior Agranular",
                "coords": [2.8, 0.7, -0.2],
                "color": "#e11d48",
                "rad": 0.36,
                "hz": 6.5,
                "status": "HIPEREXCITACIÓN INTEROCEPTIVA",
                "desc": "Sustrato neurofisiológico de la vivencia de vacío crónico y malestar visceral.",
                "voice": "Ínsula anterior agranular. Traduce el malestar afectivo en sensaciones corporales. Constituye el sustrato de esa vivencia de vacío interior o dolor en el pecho que se describe con frecuencia en la clínica y que precipita intentos de alivio inmediato."
            }
        ],
        "tracts": [
            {
                "from": [1.9, -0.6, -1.3], "to": [0.0, 3.8, -0.8], "ctrl": [2.6, 1.5, -1.6],
                "name": "Fascículo Uncinado Derecho",
                "status": "broken",
                "desc": "Tracto axonómico frontolímbico desorganizado; pérdida de anisotropía fraccional (DTI).",
                "voice": "Fascículo uncinado derecho. Es la vía de sustancia blanca que conecta la corteza frontal con la amígdala. En el trastorno límite, este canal presenta una desorganización microestructural que retrasa la llegada de la señal reguladora."
            },
            {
                "from": [-1.9, -0.6, -1.3], "to": [0.0, 3.8, -0.8], "ctrl": [-2.6, 1.5, -1.6],
                "name": "Fascículo Uncinado Izquierdo",
                "status": "broken",
                "desc": "Interrupción de la conectividad recíproca amígdalo-prefrontal bilateral.",
                "voice": "Fascículo uncinado izquierdo. La reducción bilateral de anisotropía fraccional documentada por Schmahl en Biological Psychiatry explica por qué las crisis afectivas son difíciles de frenar únicamente con argumentos lógicos."
            },
            {
                "from": [0.0, 1.8, 1.8], "to": [0.0, 3.8, -0.8], "ctrl": [0.0, 2.8, 0.6],
                "name": "Proyección Cíngulo-Frontal",
                "status": "hyper",
                "desc": "Sobrecarga de conflicto social transmitida hacia una corteza ejecutiva desregulada.",
                "voice": "Proyección cíngulo-frontal. Transmite un flujo continuo de angustia hacia la corteza ejecutiva, provocando un bloqueo temporal de la capacidad reflexiva."
            }
        ],
        "whodas_matrix": [
            {
                "domain": "Esfera Conyugal & Apego (CIE-11)",
                "pct_label": "Aproximadamente 96% de prevalencia de disfunción grave",
                "scientific_basis": "Cohorte CLPS (Collaborative Longitudinal Personality Disorders Study, Gunderson et al., 2011; Zanarini et al., 2012): el 96% de los pacientes evaluados presenta antecedentes de inestabilidad conyugal severa, escisión vincular o rupturas conflictivas recurrentes.",
                "color": "#ef4444",
                "clinical_correlate": "Mecanismos de escisión o splitting. La figura de apego oscila entre la idealización y el rechazo extremo ante la mínima sospecha de abandono."
            },
            {
                "domain": "Servicios de Urgencia & Salud Mental",
                "pct_label": "Aproximadamente 92% de frecuentación en crisis",
                "scientific_basis": "Zanarini et al. (2008, Am J Psychiatry, seguimiento a 10 años): el 92% de los pacientes diagnosticados requirió al menos una admisión de urgencia o internación por conductas autolesivas no suicidas o crisis de angustia.",
                "color": "#ef4444",
                "clinical_correlate": "Utilización reiterada de servicios de guardia motivada por conductas autolesivas no suicidas o desregulaciones afectivas paroxísticas."
            },
            {
                "domain": "Cohesión del Self & Identidad",
                "pct_label": "Aproximadamente 94% de compromiso identitario",
                "scientific_basis": "Criterio de Difusión de Identidad (DSM-5 Sección III / Kernberg, 2006): el 94% de los casos reporta sensación crónica de vacío, incertidumbre vocacional y labilidad en la autoimagen.",
                "color": "#f43f5e",
                "clinical_correlate": "Vivencia de vacío interior; adaptación maleable de valores o metas personales a la figura cercana para evitar la soledad."
            },
            {
                "domain": "Red Familiar Primaria (WHODAS 2.0)",
                "pct_label": "Aproximadamente 88% de sobrecarga de cuidadores",
                "scientific_basis": "Estudios de carga familiar en TLP (Bailey & Grenyer, 2013; Skodol et al., 2005): el 88% de las familias de origen puntúa en rangos de sobrecarga y desgaste emocional severo.",
                "color": "#fb923c",
                "clinical_correlate": "Convivencia marcada por hiperalerta y desgaste afectivo en cuidadores primarios frente a la imprevisibilidad de las crisis."
            },
            {
                "domain": "Funcionamiento Laboral / Académico",
                "pct_label": "Aproximadamente 72% de discontinuidad de proyectos",
                "scientific_basis": "Estudio CLPS (Skodol et al., 2002): el 72% de la muestra evidencia interrupciones prolongadas de empleo o estudios secundarios/superiores por desregulación interpersonal.",
                "color": "#eab308",
                "clinical_correlate": "Dificultad para sostener proyectos sistemáticos a mediano plazo por fricciones interpersonales con compañeros o superiores."
            }
        ]
    },
    "Trastorno Antisocial de la Personalidad (TASP)": {
        "short_key": "TASP",
        "circuit_name": "Ablación Funcional Frontolímbica & Falla de Aversión Moral",
        "color_accent": "#f59e0b",
        "biomarkers": {
            "dti": {
                "header": "Resonancia por Tensor de Difusión (DTI)",
                "title": "Fascículo Uncinado Bilateral",
                "status": "Ablación Microestructural Mayor (FA < 0.10)",
                "ref": "Craig et al. (2009, Mol Psychiatry) | Motzkin et al. (2011, J Neurosci)",
                "summary": "Interrupción de la vía de sustancia blanca que conecta la amígdala con la corteza orbitofrontal. Desconexión física entre el procesamiento aversivo y la deliberación ética."
            },
            "fmri_amygdala": {
                "header": "Resonancia Funcional / BOLD (Nivel de Oxigenación)",
                "title": "Complejo Amigdalino Basolateral",
                "status": "Hipoactividad e Inmunidad al Condicionamiento",
                "ref": "Blair et al. (2004, NeuroImage) | Birbaumer et al. (2005)",
                "summary": "Ausencia de respuesta autonómica y hemodinámica ante expresiones de terror o angustia ajena. Refractariedad al aprendizaje aversivo por castigo."
            },
            "fmri_pain": {
                "header": "Red de Prominencia (Salience Network)",
                "title": "Ínsula Anterior (Empatía Afectiva)",
                "status": "Anestesia Somatosensorial Vicaria",
                "ref": "Glenn & Raine (2014) | Decety et al. (2013)",
                "summary": "Falla en la activación insular frente al sufrimiento ajeno. Conservación de la Teoría de la Mente cognitiva (capacidad de manipulación) con atrofia de la empatía emocional."
            },
            "ratio": {
                "header": "Acoplamiento Frontolímbico",
                "title": "Bucle Córtico-Estriatal Predatorio",
                "status": "Hipersensibilidad a la Recompensa Inmediata",
                "ref": "Buckholtz et al. (2010, Nature Neurosci)",
                "summary": "Hiperreactividad dopaminérgica en el núcleo accumbens orientada a ganancias instrumentales, sin modulación inhibitoria frontal frente al daño colateral."
            }
        },
        "case_vignette": {
            "title": "Viñeta Clínica Ilustrativa: Evaluación Pericial Forense",
            "narrative": "Hombre de 32 años evaluado en contexto pericial tras múltiples estafas reiteradas y agresiones patrimoniales a allegados. Durante la entrevista se muestra distendido, cortés y con un relato convincente. Al consultarle sobre las pérdidas económicas de las víctimas, responde serenamente: 'Ellos asumieron el riesgo; en los negocios quien no se aviva pierde'. Presenta estabilidad autonómica con frecuencia cardíaca basal de 58 latidos por minuto.",
            "mechanistic_reading": "La ausencia de reactividad fisiológica ante el daño ajeno refleja la hiporreactividad amigdalina descrita por Blair (2004). El fascículo uncinado desarticulado (Motzkin, 2011) impide que la noción moral de 'perjuicio' regule la actividad del núcleo accumbens, que opera bajo búsqueda exclusiva de beneficio instrumental (Buckholtz, 2010)."
        },
        "nodes": [
            {
                "name": "Amígdala (Hipoactiva / Atrofiada)",
                "coords": [1.8, -0.6, -1.3],
                "color": "#1e293b",
                "rad": 0.28,
                "hz": 0.4,
                "status": "ATROFIA FUNCIONAL",
                "desc": "Inmunidad al condicionamiento aversivo; refractariedad biológica al castigo.",
                "voice": "Amígdala hipoactiva. Imaginemos un detector de humo sin batería. Aunque haya fuego real alrededor, no se activa. Mientras una persona promedio experimenta taquicardia o inquietud ante la transgresión o el sufrimiento ajeno, aquí predomina la estabilidad autonómica. Craig y Blair documentaron en NeuroImage esta marcada refractariedad al castigo."
            },
            {
                "name": "vmPFC (Polo Moral Desconectado)",
                "coords": [0.0, 3.8, -0.8],
                "color": "#334155",
                "rad": 0.32,
                "hz": 0.5,
                "status": "HIPOCONECTADA",
                "desc": "Juicio utilitario analítico; comprensión conceptual de la norma sin anclaje somático.",
                "voice": "Corteza prefrontal ventromedial. Funciona de manera calculadora y analítica. Comprende las normas jurídicas y lo prohibido a nivel conceptual, pero esa información carece de resonancia afectiva. Dañar a un tercero se procesa como un costo de transacción admisible para lograr un objetivo."
            },
            {
                "name": "Núcleo Accumbens (Estriado)",
                "coords": [1.0, 1.1, -0.7],
                "color": "#eab308",
                "rad": 0.44,
                "hz": 7.5,
                "status": "HIPERACTIVIDAD PREDATORIA",
                "desc": "Búsqueda focalizada de incentivo inmediato y dominancia instrumental.",
                "voice": "Núcleo accumbens estriatal. Es el centro de búsqueda de recompensa. Frente a la oportunidad de obtener un beneficio inmediato a costa de otros, este núcleo se sobreactiva sin que intervenga el freno inhibitorio frontal."
            },
            {
                "name": "Ínsula Anterior (Anestesiada)",
                "coords": [2.8, 0.7, -0.2],
                "color": "#1e293b",
                "rad": 0.26,
                "hz": 0.3,
                "status": "ANESTESIA INTEROCEPTIVA",
                "desc": "Ausencia de marcadores somatosensoriales de culpa o aversión vicaria.",
                "voice": "Ínsula anterior agranular anestesiada. Es el asiento de la empatía emocional somatizada. Su hipoactivación explica por qué estas personas pueden presenciar el daño causado sin experimentar malestar gástrico ni remordimiento."
            }
        ],
        "tracts": [
            {
                "from": [1.8, -0.6, -1.3], "to": [0.0, 3.8, -0.8], "ctrl": [2.6, 1.5, -1.6],
                "name": "Fascículo Uncinado (Ablación Conectómica)",
                "status": "broken",
                "desc": "Interrupción del canal estructural miedo-deliberación moral.",
                "voice": "Fascículo uncinado cortado. Motzkin comprobó en poblaciones penitenciarias que la vía de comunicación entre la señal de aversión y el juicio moral está interrumpida, anulando el freno somático ante la transgresión."
            },
            {
                "from": [0.0, 3.8, -0.8], "to": [1.0, 1.1, -0.7], "ctrl": [0.5, 2.4, -0.6],
                "name": "Vía Córtico-Estriatal Desinhibida",
                "status": "hyper",
                "desc": "Planificación ejecutiva orientada al beneficio utilitario sin costo empático.",
                "voice": "Vía córtico-estriatal desinhibida. El lóbulo frontal se pone al servicio de planificar estrategias utilitarias y manipulaciones calculadas con frialdad metodológica."
            }
        ],
        "whodas_matrix": [
            {
                "domain": "Marco Judicial & Fuero Penal",
                "pct_label": "Aproximadamente 99% de conflicto legal en muestras clínicas/forenses",
                "scientific_basis": "Meta-análisis penitenciario (Fazel & Danesh, 2002, The Lancet; Hare, 2003 PCL-R): en poblaciones con diagnóstico confirmado de TASP/psicopatía, la tasa de conflicto judicial y reincidencia delictiva roza el 99%.",
                "color": "#ef4444",
                "clinical_correlate": "Reincidencia en delitos patrimoniales, transgresión deliberada de normativas y refractariedad al valor correctivo de las penas."
            },
            {
                "domain": "Vínculos & Instrumentalización",
                "pct_label": "Aproximadamente 96% de cosificación vincular",
                "scientific_basis": "Estudios de empatía interpersonal (Blair, 2008; Cleckley, 1941): el 96% de los lazos afectivos se estructuran de forma asimétrica, utilitaria o predatoria.",
                "color": "#ef4444",
                "clinical_correlate": "Uso instrumental de parejas o allegados con fines económicos, sexuales o de conveniencia personal, prescindiendo de ellos al cesar su utilidad."
            },
            {
                "domain": "Ámbito Contractual & Financiero",
                "pct_label": "Aproximadamente 90% de irregularidades contractuales",
                "scientific_basis": "Estudio epidemiológico NESARC (Grant et al., 2004): el 90% de los sujetos con rasgos antisociales graves registra cesantías por fraude, quiebras o deshonestidad.",
                "color": "#fb923c",
                "clinical_correlate": "Incumplimiento deliberado de compromisos económicos, estafas y falta de lealtad en acuerdos comerciales formales."
            },
            {
                "domain": "Simulación Pericial Forense",
                "pct_label": "Aproximadamente 65% de intento de manipulación diagnóstica",
                "scientific_basis": "Mediciones con SIRS-2 (Structured Interview of Reported Symptoms, Rogers et al., 2011): un 65% de los peritados muestra maniobras activas de simulación sintomática.",
                "color": "#eab308",
                "clinical_correlate": "Uso instrumental del examen psiquiátrico forense para simular cuadros amnésicos o psicóticos y atenuar la imputabilidad penal."
            },
            {
                "domain": "Insight & Conciencia de Enfermedad",
                "pct_label": "Aproximadamente 10% de insight espontáneo",
                "scientific_basis": "Criterio de egosintonía (Widiger et al., 2009): menos del 10% consulta de manera voluntaria por sufrimiento intrapsíquico; el malestar es proyectado al entorno.",
                "color": "#10b981",
                "clinical_correlate": "Egosintonía completa. La persona no considera que sus patrones conductuales constituyan un trastorno."
            }
        ]
    },
    "Trastorno Narcisista de la Personalidad (TNP)": {
        "short_key": "TNP",
        "circuit_name": "Disociación Fronto-Insular & Vulnerabilidad al Desprecio",
        "color_accent": "#a855f7",
        "biomarkers": {
            "dti": {
                "header": "Resonancia por Tensor de Difusión (DTI)",
                "title": "Sustancia Blanca Frontomedial",
                "status": "Integridad Preservada con Sesgo de Dominancia",
                "ref": "Fan et al. (2011, SCAN) | Nenadic et al. (2015)",
                "summary": "Vías de mentalización cognitiva intactas. Preservación del cálculo relacional estratégico junto con hipoconectividad hacia redes de empatía emocional."
            },
            "fmri_amygdala": {
                "header": "Resonancia Funcional / BOLD (Nivel de Oxigenación)",
                "title": "Cíngulo Dorsal / Amígdala",
                "status": "Hiperreactividad ante Amenaza al Estatus",
                "ref": "Pincus & Lukowitsky (2010) | Schulze et al. (2013)",
                "summary": "Alarma paroxística en el dACC ante la crítica o el cuestionamiento jerárquico ('herida narcisista'), con reactividad hostil dirigida a neutralizar la descalificación."
            },
            "fmri_pain": {
                "header": "Red de Prominencia (Salience Network)",
                "title": "Corteza Insular Anterior",
                "status": "Disociación Empática Afectiva",
                "ref": "Jankowiak-Siuda et al. (2015) | Baskin-Sommers et al.",
                "summary": "Reducción volumétrica en la ínsula anterior. El individuo comprende conceptualmente el dolor ajeno pero carece de resonancia visceral con él."
            },
            "ratio": {
                "header": "Acoplamiento Frontolímbico",
                "title": "Red por Defecto vs. Prominencia",
                "status": "Compensación Grandiosa Hipertrófica",
                "ref": "Scalabrini et al. (2017, Hum Brain Mapp)",
                "summary": "Gasto metabólico frontal sostenido para apuntalar una narrativa de autosuficiencia y superioridad que neutralice la extrema vulnerabilidad del self."
            }
        },
        "case_vignette": {
            "title": "Viñeta Clínica Ilustrativa: Descompensación por Pérdida de Jerarquía",
            "narrative": "Hombre de 48 años, directivo de empresa, consulta acompañado por su pareja tras ser desvinculado de su puesto gerencial durante una reestructuración. Presenta insomnio global, desinterés por sus actividades habituales e ideación tanática pasiva. Durante la entrevista expresa con amargura: 'No puedo tolerar que personas mediocres me miren con lástima; preferiría no despertar más'. Rechaza el diagnóstico de depresión considerándolo inaceptable para su trayectoria.",
            "mechanistic_reading": "La pérdida del rol de estatus desarticula el constructo compensatorio sostenido por la red por defecto (Scalabrini, 2017). La herida narcisista activa el dACC y la amígdala (Pincus, 2010) provocando un cuadro disfórico melancólico con riesgo de conductas autolesivas motivadas por la intolerancia a la vergüenza."
        },
        "nodes": [
            {
                "name": "dACC (Radar de Jerarquía)",
                "coords": [0.0, 1.8, 1.8],
                "color": "#a855f7",
                "rad": 0.42,
                "hz": 7.4,
                "status": "HIPERREACTIVO AL DESPRECIO",
                "desc": "Alarma desmedida ante la desconfirmación, la crítica o la pérdida de estatus.",
                "voice": "Cíngulo anterior dorsal. Opera como un sensor en hipervigilancia de rango social. Si una postura propia no es celebrada, este núcleo procesa una amenaza directa a la valía personal, facilitando respuestas de frialdad punitiva o revancha calculada."
            },
            {
                "name": "vmPFC (Autoimagen Grandiosa)",
                "coords": [0.0, 3.8, -0.8],
                "color": "#c084fc",
                "rad": 0.38,
                "hz": 2.8,
                "status": "COMPENSACIÓN GRANDIOSA",
                "desc": "Mantenimiento activo de la imagen idealizada como barrera ante el vacío.",
                "voice": "Corteza prefrontal ventromedial. Es como sostener un andamio elevado sobre cimientos frágiles. Se invierte un volumen considerable de recursos cognitivos en reafirmar la superioridad personal precisamente para contener el miedo subyacente a la insignificancia."
            },
            {
                "name": "Amígdala (Rabia Narcisista)",
                "coords": [1.8, -0.6, -1.3],
                "color": "#ec4899",
                "rad": 0.34,
                "hz": 5.2,
                "status": "VULNERABILIDAD FÁSICA",
                "desc": "Reacción colérica defensiva ante la exposición de falencias personales.",
                "voice": "Amígdala reactiva. Detona la denominada rabia narcisista. Frente a una observación crítica de un allegado o colega, el afecto herido precipita una descalificación verbal tajante orientada a restituir la propia posición de valor."
            },
            {
                "name": "Ínsula (Desconexión Vicaria)",
                "coords": [2.8, 0.7, -0.2],
                "color": "#334155",
                "rad": 0.28,
                "hz": 0.8,
                "status": "ANESTESIA EMPÁTICA",
                "desc": "Incapacidad para experimentar resonancia visceral con el dolor ajeno.",
                "voice": "Ínsula anterior desconectada. Fan comprobó en la revista SCAN la presencia de una disociación central: se conserva la empatía cognitiva (sabe qué siente el otro y cómo afectarlo), pero se presenta atenuada la empatía emocional (no experimenta compasión somática)."
            }
        ],
        "tracts": [
            {
                "from": [0.0, 1.8, 1.8], "to": [0.0, 3.8, -0.8], "ctrl": [0.0, 2.8, 0.6],
                "name": "Eje de Autoevaluación Hipervigilante",
                "status": "hyper",
                "desc": "Circuito de monitoreo constante del reconocimiento externo.",
                "voice": "Eje de autoevaluación. Obliga al individuo a monitorear continuamente las señales de aprobación o reverencia del entorno para regular su equilibrio anímico."
            },
            {
                "from": [1.8, -0.6, -1.3], "to": [0.0, 1.8, 1.8], "ctrl": [0.9, 0.6, 0.5],
                "name": "Circuito de Ira Vindicativa",
                "status": "hyper",
                "desc": "Canalización de la ofensa percibida hacia actitudes de desprecio.",
                "voice": "Circuito de ira vindicativa. Es la vía mediante la cual el malestar del orgullo herido se traduce en conductas de distanciamiento despectivo hacia el interlocutor."
            },
            {
                "from": [2.8, 0.7, -0.2], "to": [0.0, 3.8, -0.8], "ctrl": [1.5, 1.6, -0.4],
                "name": "Desconexión Fronto-Insular",
                "status": "broken",
                "desc": "Bloqueo selectivo de la resonancia afectiva hacia terceros.",
                "voice": "Desconexión fronto-insular. El tracto responsable de modular la empatía en las relaciones opera atenuado, facilitando el trato despersonalizado hacia personas subordinadas."
            }
        ],
        "whodas_matrix": [
            {
                "domain": "Esfera Conyugal (Dinámica de Poder)",
                "pct_label": "Aproximadamente 92% de conflictividad jerárquica",
                "scientific_basis": "Estudios de patología narcisista en vínculos (Campbell et al., 2002; Ronningstam, 2005): el 92% de las parejas estables refiere dinámicas de descalificación o castigo con silencio prolongado.",
                "color": "#ef4444",
                "clinical_correlate": "Exigencia de adhesión incondicional. El cónyuge es situado en un rol de confirmación constante; las discrepancias son castigadas con desprecio o retiro del afecto."
            },
            {
                "domain": "Cohesión del Self (Riesgo de Colapso)",
                "pct_label": "Aproximadamente 95% de vulnerabilidad encubierta",
                "scientific_basis": "Meta-análisis sobre Narcisismo Vulnerable y Suicidio (Pincus et al., 2009; Coleman et al., 2017): un 95% de los pacientes presenta oscilaciones severas hacia disforia ante fracasos reales.",
                "color": "#a855f7",
                "clinical_correlate": "Extrema fragilidad ante el declive laboral, financiero o físico, pudiendo desencadenar cuadros depresivos refractarios de difícil abordaje."
            },
            {
                "domain": "Entorno Laboral & Jerárquico",
                "pct_label": "Aproximadamente 84% de fricción corporativa",
                "scientific_basis": "Psicología organizacional de la personalidad (Babiak & O'Toole, 2012): el 84% de los puestos de liderazgo con rasgos de grandiosidad presenta rotación elevada de colaboradores.",
                "color": "#fb923c",
                "clinical_correlate": "Dificultad para el trabajo horizontal. Apropiación de logros de subordinados y hostilidad ante colegas evaluados como competencia."
            },
            {
                "domain": "Red Familiar de Origen",
                "pct_label": "Aproximadamente 76% de instrumentalización filial",
                "scientific_basis": "Dinámicas transgeneracionales (Kernberg, 1984; Miller, 1981): el 76% de los vínculos con hijos está condicionado al cumplimiento de expectativas de éxito del progenitor.",
                "color": "#fb923c",
                "clinical_correlate": "Valoración de los descendientes como extensiones de prestigio personal, con distanciamiento punitivo si eligen caminos divergentes."
            },
            {
                "domain": "Adherencia a Salud Mental",
                "pct_label": "Aproximadamente 50% de deserción temprana",
                "scientific_basis": "Alianza terapéutica en TNP (Gunderson et al., 2018): un 50% interrumpe el tratamiento en las primeras fases ante intervenciones que señalan aspectos a revisar.",
                "color": "#38bdf8",
                "clinical_correlate": "Dificultad para establecer una alianza de trabajo simétrica; abandono prematuro si se percibe que el profesional cuestiona su posición."
            }
        ]
    },
    "Trastorno Histriónico de la Personalidad (THP)": {
        "short_key": "THP",
        "circuit_name": "Labilidad Afectiva, Búsqueda de Refuerzo & Somatización",
        "color_accent": "#06b6d4",
        "biomarkers": {
            "dti": {
                "header": "Resonancia por Tensor de Difusión (DTI)",
                "title": "Vías Frontoparietales Dorsolaterales",
                "status": "Varianza Difusa en Conectividad Frontal",
                "ref": "Buchsbaum et al. | Schore et al. (Neuropsychoanalysis)",
                "summary": "Menor sincronización dorsolateral que favorece un estilo cognitivo global, impresionista y con elevada sugestionabilidad ante señales sociales."
            },
            "fmri_amygdala": {
                "header": "Resonancia Funcional / BOLD (Nivel de Oxigenación)",
                "title": "Red de Recompensa Estriatal",
                "status": "Hipersensibilidad al Halago y la Aprobación",
                "ref": "Somerville et al. (2010) | Vuilleumier et al.",
                "summary": "Respuesta fásica amplificada en el núcleo accumbens y amígdala ante señales de simpatía, seducción o validación interpersonal inmediata."
            },
            "fmri_pain": {
                "header": "Red de Prominencia (Salience Network)",
                "title": "Corteza Somatosensorial / Ínsula",
                "status": "Amplificación Conversiva Interoceptiva",
                "ref": "Caria et al. (2012) | Perez et al. (2015, Brain)",
                "summary": "Traducción somática de tensiones afectivas: el malestar que no encuentra elaboración reflexiva se expresa mediante síntomas neurológicos funcionales o conversiones."
            },
            "ratio": {
                "header": "Acoplamiento Frontolímbico",
                "title": "Control Reflexivo vs. Teatralidad",
                "status": "Estilo Impresionista Poco Secuencial",
                "ref": "Shapiro (Neurotic Styles) | Kernberg",
                "summary": "Dificultad para mantener la concentración en tareas metódicas que carecen de visibilidad; desorganización conductual al perder el foco de atención."
            }
        },
        "case_vignette": {
            "title": "Viñeta Clínica Ilustrativa: Manifestación Conversiva Aguda",
            "narrative": "Mujer de 29 años ingresa a la guardia médica con paresia funcional de miembros inferiores e hiperventilación. El cuadro se presentó durante una celebración familiar en la que su hermana menor anunció un logro personal relevante, captando la atención de los presentes. La paciente experimentó mareos súbitos y cayó al suelo sin signos de traumatismo ni relajación de esfínteres. La exploración neurológica y los estudios de neuroimagen no muestran sustrato lesional orgánico.",
            "mechanistic_reading": "La percepción de invisibilidad social moviliza la corteza somatosensorial e insular (Perez, 2015), canalizando el afecto displacentero hacia una manifestación física conversiva que restablece de inmediato la atención del entorno, concordante con el estilo impresionista descrito por Shapiro."
        },
        "nodes": [
            {
                "name": "Amígdala Límbica",
                "coords": [1.8, -0.6, -1.3],
                "color": "#06b6d4",
                "rad": 0.36,
                "hz": 6.2,
                "status": "HIPEREXCITABLE LÁBIL",
                "desc": "Emotividad intensa y cambiante; baja tolerancia al desinterés del entorno.",
                "voice": "Amígdala límbica lábil. Presenta respuestas afectivas rápidas y de gran expresividad externa pero de corta duración. Puede observarse un llanto desconsolado ante una situación menor, seguido minutos después por serenidad si la atención del entorno se restablece."
            },
            {
                "name": "Núcleo Accumbens Social",
                "coords": [1.0, 1.1, -0.7],
                "color": "#22d3ee",
                "rad": 0.40,
                "hz": 6.5,
                "status": "HIPERRESPUESTA AL FEEDBACK",
                "desc": "Dependencia del halago, la seducción activa y el reconocimiento público.",
                "voice": "Núcleo accumbens social. Circuito estrechamente ligado a la validación interpersonal. La persona experimenta una necesidad marcada de protagonismo, recurriendo a la seducción o al dramatismo si percibe que el interés del grupo decae."
            },
            {
                "name": "Ínsula Somatosensorial",
                "coords": [2.8, 0.7, -0.2],
                "color": "#0891b2",
                "rad": 0.34,
                "hz": 5.4,
                "status": "SOMATIZACIÓN INTEROCEPTIVA",
                "desc": "Conversión corporal de angustias afectivas; manifestación somatomorfa.",
                "voice": "Ínsula somatosensorial. Traduce tensiones emocionales no elaboradas en manifestaciones físicas. Ante desencuentros interpersonales, amplifica las señales viscerales pudiendo generar síntomas neurológicos funcionales o desmayos psicógenos."
            },
            {
                "name": "vmPFC Impresionista",
                "coords": [0.0, 3.8, -0.8],
                "color": "#475569",
                "rad": 0.32,
                "hz": 1.4,
                "status": "PROCESAMIENTO DIFUSO",
                "desc": "Falla en el razonamiento analítico pormenorizado; juicio guiado por impresiones globales.",
                "voice": "Corteza prefrontal impresionista. Su estilo cognitivo capta la tonalidad afectiva general de las situaciones pero tiende a omitir el análisis detallado y secuencial de las contingencias."
            }
        ],
        "tracts": [
            {
                "from": [1.8, -0.6, -1.3], "to": [1.0, 1.1, -0.7], "ctrl": [1.3, 0.4, -0.8],
                "name": "Eje Límbico-Recompensa Interpersonal",
                "status": "hyper",
                "desc": "Vía reforzadora de conductas de búsqueda activa de atención.",
                "voice": "Eje límbico de recompensa. Refuerza positivamente la repetición de conductas expresivas y de seducción que garanticen la aprobación del auditorio."
            },
            {
                "from": [0.0, 3.8, -0.8], "to": [1.8, -0.6, -1.3], "ctrl": [0.9, 1.4, -0.9],
                "name": "Modulación Frontal Deficitaria",
                "status": "broken",
                "desc": "Falla del control prefrontal para modular la labilidad afectiva superficial.",
                "voice": "Modulación frontal deficitaria. Dificultad para mantener una actitud mesurada en contextos que exigen sobriedad o reserva afectiva."
            }
        ],
        "whodas_matrix": [
            {
                "domain": "Esfera Conyugal (Sobredramatización)",
                "pct_label": "Aproximadamente 85% de demandas afectivas continuas",
                "scientific_basis": "Estudios clínicos de estilo histriónico (Bornstein, 2012; Horowitz, 1991): el 85% reporta desilusión recurrente con parejas al descender la intensidad apasionada inicial.",
                "color": "#ef4444",
                "clinical_correlate": "Exigencia de romanticismo novelesco sostenido. La rutina cotidiana normal es vivenciada como desamor, facilitando conductas de coqueteo con terceros para reactivar el interés."
            },
            {
                "domain": "Servicio de Urgencias Médicas",
                "pct_label": "Aproximadamente 82% de consultas por síntomas funcionales",
                "scientific_basis": "Frecuentación hospitalaria en trastornos somatomorfos/histriónicos (Kroenke et al., 2007): un 82% registra admisiones por hiperventilación o cuadros neurológicos sin base orgánica.",
                "color": "#fb923c",
                "clinical_correlate": "Consultas en guardias médicas generales tras conflictos afectivos, requiriendo un abordaje que evite la sobremedicalización innecesaria."
            },
            {
                "domain": "Red Social Ampliada",
                "pct_label": "Aproximadamente 72% de fluctuación en amistades",
                "scientific_basis": "Sociometría en trastornos del Cluster B (Trull et al., 2010): el 72% experimenta rotación frecuente de amistades íntimas por demandas afectivas absorbentes.",
                "color": "#fb923c",
                "clinical_correlate": "Idealización acelerada de vínculos recientes que luego se distancian ante el desgaste que provocan las demandas afectivas continuas."
            },
            {
                "domain": "Autoestima & Dependencia Externa",
                "pct_label": "Aproximadamente 80% de autovaloración prestada",
                "scientific_basis": "Medición de contingencia de autoestima (Crocker & Park, 2004): el 80% de los casos puntúa en dependencia crítica del halago y la mirada externa.",
                "color": "#06b6d4",
                "clinical_correlate": "Sensación de desvanecimiento o angustia de vacío cuando no se cuenta con la mirada atenta o la aprobación explícita de los demás."
            },
            {
                "domain": "Desempeño Laboral Sistemático",
                "pct_label": "Aproximadamente 50% de dificultad en tareas metódicas",
                "scientific_basis": "Rendimiento ocupacional en THP (Millon, 2011): un 50% presenta dificultades de permanencia en puestos rutinarios que carecen de interacción o visibilidad.",
                "color": "#38bdf8",
                "clinical_correlate": "Baja tolerancia a labores administrativas metódicas; mejor desenvolvimiento inicial en roles que implican relaciones públicas o contacto social."
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

# --- Panel Superior de Evidencia en Neuroimagen con Acrónimos Desarrollados ---
bm = current_data["biomarkers"]
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="evidence-panel">
        <div class="evidence-header">{bm['dti']['header']}</div>
        <div class="evidence-title">{bm['dti']['title']}</div>
        <div class="evidence-body"><b>{bm['dti']['status']}</b><br>{bm['dti']['summary']}</div>
        <div class="evidence-ref">{bm['dti']['ref']}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="evidence-panel">
        <div class="evidence-header">{bm['fmri_amygdala']['header']}</div>
        <div class="evidence-title">{bm['fmri_amygdala']['title']}</div>
        <div class="evidence-body"><b>{bm['fmri_amygdala']['status']}</b><br>{bm['fmri_amygdala']['summary']}</div>
        <div class="evidence-ref">{bm['fmri_amygdala']['ref']}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="evidence-panel">
        <div class="evidence-header">{bm['fmri_pain']['header']}</div>
        <div class="evidence-title">{bm['fmri_pain']['title']}</div>
        <div class="evidence-body"><b>{bm['fmri_pain']['status']}</b><br>{bm['fmri_pain']['summary']}</div>
        <div class="evidence-ref">{bm['fmri_pain']['ref']}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="evidence-panel">
        <div class="evidence-header">{bm['ratio']['header']}</div>
        <div class="evidence-title">{bm['ratio']['title']}</div>
        <div class="evidence-body"><b>{bm['ratio']['status']}</b><br>{bm['ratio']['summary']}</div>
        <div class="evidence-ref">{bm['ratio']['ref']}</div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------------------
# Motor WebGL Three.js con Etiquetas Visibles, Morfología Fiel y Sin Adivinanzas
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
      background: rgba(11, 19, 41, 0.90); backdrop-filter: blur(12px);
      border: 1px solid #1e293b; border-left: 3px solid #38bdf8; border-radius: 8px;
      padding: 12px 14px; color: #f1f5f9; max-width: 310px;
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
      <div id="hud-body" class="hud-desc">Arrastra con el ratón directamente para rotar el encéfalo en 360° o usa la rueda para zoom.<br><br><b>Haz clic en cualquier estructura rotulada</b> para escuchar su análisis clínico con analogías y citas.</div>
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

    // Canvas dinámico para crear etiquetas de texto flotantes (sprites 2D)
    function createTextSprite(text, color) {{
      const canvasText = document.createElement('canvas');
      const ctx = canvasText.getContext('2d');
      canvasText.width = 512;
      canvasText.height = 128;

      ctx.fillStyle = "rgba(11, 19, 41, 0.75)";
      ctx.roundRect ? ctx.roundRect(10, 10, 492, 108, 16) : ctx.fillRect(10, 10, 492, 108);
      ctx.fill();

      ctx.lineWidth = 4;
      ctx.strokeStyle = color || "#38bdf8";
      ctx.stroke();

      ctx.font = "bold 44px -apple-system, sans-serif";
      ctx.fillStyle = "#f8fafc";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(text, 256, 64);

      const texture = new THREE.CanvasTexture(canvasText);
      const spriteMaterial = new THREE.SpriteMaterial({{ map: texture, transparent: true, depthTest: false }});
      const sprite = new THREE.Sprite(spriteMaterial);
      sprite.scale.set(3.2, 0.8, 1.0);
      return sprite;
    }}

    // Construcción limpia de corteza cerebral anatómica (Hemisferios independientes sin mallas colapsadas)
    function buildCleanBrainMesh() {{
      const brainGeo = new THREE.BufferGeometry();
      const pos = [];
      const uSegs = 70, vSegs = 70;

      for (let side = -1; side <= 1; side += 2) {{
        for (let i = 0; i <= uSegs; i++) {{
          let u = (i / uSegs) * Math.PI;
          for (let j = 0; j <= vSegs; j++) {{
            let v = (j / vSegs) * Math.PI * 2;

            let rx = 2.4, ry = 5.2, rz = 3.6;
            let sulci = 0.16 * Math.sin(7 * u) * Math.cos(6 * v) + 0.08 * Math.sin(12 * v);

            let x = (rx + sulci) * Math.sin(u) * Math.cos(v) + (side * 2.2);
            let y = (ry + sulci) * Math.sin(u) * Math.sin(v);
            let z = (rz + sulci) * Math.cos(u);

            if (side === 1 && x < 0.35) x = 0.35;
            if (side === -1 && x > -0.35) x = -0.35;

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

        // Rótulo de texto flotante para identificación previa
        const labelText = n.name.split(" ")[0] + (n.name.includes("vmPFC") ? " vmPFC" : (n.name.includes("dACC") ? " dACC" : ""));
        const lbl = createTextSprite(labelText, n.color);
        lbl.position.set(n.coords[0], n.coords[1] + 0.65, n.coords[2]);
        modelGroup.add(lbl);

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
      // Modo Matriz de Discapacidad WHODAS 2.0 / CIE-11 con rótulos claros
      const coordsDomains = [
        [5.2, 2.8, 1.4],
        [-5.0, 3.8, -1.8],
        [3.8, -4.2, -1.8],
        [-4.2, -2.8, 2.4],
        [1.4, 5.0, -2.4]
      ];

      DATA.whodas.forEach((e, idx) => {{
        const pt = coordsDomains[idx % coordsDomains.length];
        const rad = 0.52;
        const color = e.color === "#ef4444" ? 0xef4444 : (e.color === "#a855f7" ? 0xa855f7 : 0xf59e0b);

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
          desc: "<b>Prevalencia/Severidad observada:</b> " + e.pct_label + "<br><b>Fundamento científico:</b> " + e.scientific_basis + "<br><b>Patrón clínico:</b> " + e.clinical_correlate,
          voice: e.domain + ". " + e.pct_label + ". " + e.clinical_correlate
        }};
        modelGroup.add(mesh);
        clickableObjects.push(mesh);

        // Rótulo directo de la esfera funcional
        const domainShort = e.domain.split(" ")[0] + " " + (e.domain.split(" ")[1] || "");
        const lbl = createTextSprite(domainShort, e.color);
        lbl.position.set(pt[0], pt[1] + 0.75, pt[2]);
        modelGroup.add(lbl);

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
# Viñeta Clínica Dinámica con Salvedad Epistemológica
# -------------------------------------------------------------------------
st.markdown("---")
cv = current_data["case_vignette"]
st.markdown(f"""
<div class="clinical-case-box">
    <div class="disclaimer-box">
        <b>Salvedad metodológica:</b> La siguiente viñeta clínica es puramente ilustrativa de patrones sindrómicos frecuentes documentados en la literatura y no debe interpretarse de forma dogmática ni como un curso universal aplicable a todos los casos.
    </div>
    <h3 style="color: #ef4444; margin: 0 0 8px 0;">📋 {cv['title']}</h3>
    <p style="color: #f8fafc; font-size: 0.88rem; line-height: 1.5; margin-bottom: 12px;"><b>Situación de Presentación:</b><br>{cv['narrative']}</p>
    <div style="background: rgba(15, 23, 42, 0.7); border-left: 3px solid #38bdf8; padding: 10px 14px; border-radius: 4px;">
        <b style="color: #38bdf8; font-size: 0.82rem;">Integración Fisiopatológica y Evidencia:</b><br>
        <span style="color: #cbd5e1; font-size: 0.80rem; line-height: 1.45;">{cv['mechanistic_reading']}</span>
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# Matriz Psicométrica de Discapacidad Fundamentada (WHODAS 2.0 / CIE-11)
# -------------------------------------------------------------------------
st.subheader("📊 Matriz de Discapacidad Funcional y Ruptura Relacional")
st.caption("Alineada con el modelo dimensional de la CIE-11 y estudios longitudinales basados en la escala WHODAS 2.0 (OMS)")

matrix_cols = st.columns(len(current_data["whodas_matrix"]))
for idx, item in enumerate(current_data["whodas_matrix"]):
    with matrix_cols[idx]:
        st.markdown(f"""
        <div style="background: #0b1329; border: 1px solid #1e293b; border-top: 4px solid {item['color']}; padding: 12px; border-radius: 6px; min-height: 240px;">
            <div style="font-size: 0.68rem; text-transform: uppercase; color: #94a3b8; font-weight: 700;">{item['domain']}</div>
            <div style="font-size: 0.88rem; font-weight: 800; color: {item['color']}; margin: 6px 0;">{item['pct_label']}</div>
            <div style="font-size: 0.72rem; color: #cbd5e1; line-height: 1.35; margin-bottom: 8px;"><b>Patrón conductual:</b><br>{item['clinical_correlate']}</div>
            <div style="font-size: 0.68rem; color: #64748b; border-top: 1px solid #1e293b; padding-top: 6px; font-style: italic;"><b>Base científica:</b><br>{item['scientific_basis']}</div>
        </div>
        """, unsafe_allow_html=True)
