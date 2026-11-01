import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="Atlas Neurobiológico & Conectómico del Cluster B",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estética de consola quirúrgica limpia y ordenada
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
    .evidence-body { font-size: 0.76rem; color: #cbd5e1; line-height: 1.4; margin-top: 3px; }
    .evidence-ref { font-size: 0.68rem; color: #64748b; font-style: italic; margin-top: 4px; }
    
    .compare-card {
        background: #090e1a; border: 1px solid #1e293b; border-radius: 8px;
        padding: 14px 18px; margin-top: 10px; margin-bottom: 12px;
    }
    
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
# Base de Datos Neurocientífica, Pedagógica y de Neuroimagen Comparativa
# -------------------------------------------------------------------------
CLINICAL_REGISTRY = {
    "Trastorno Límite de la Personalidad (TLP)": {
        "short_key": "TLP",
        "circuit_name": "Falla del Freno Frontal & Alarma Desregulada del Dolor Social",
        "color_accent": "#ef4444",
        "biomarkers": {
            "dti": {
                "header": "Tractografía de Sustancia Blanca (DTI)",
                "title": "Fascículo Uncinado Bilateral",
                "status": "Aislamiento Axonal Disminuido (Schmahl et al.)",
                "analogy": "Como un cable de freno deshilachado: la orden de la razón tarda demasiado en llegar a la emoción.",
                "summary": "Pérdida de integridad microestructural en la vía que comunica la corteza orbitofrontal con la amígdala. El lóbulo frontal no logra frenar a tiempo la tormenta afectiva.",
                "ref": "Schmahl et al. (2014, Biological Psychiatry) | New et al. (2009, NeuroImage)"
            },
            "fmri_amygdala": {
                "header": "Reactividad Funcional (fMRI / BOLD)",
                "title": "Complejo Amigdalino Basolateral",
                "status": "Alarma en Hiperactividad Fásica (Ruocco et al.)",
                "analogy": "Un detector de humo tan descalibrado que suena con fuerza ante el simple vapor de una taza de café.",
                "summary": "Respuesta desproporcionada ante rostros serios o una demora en responder un mensaje, decodificados como una amenaza inmediata de rechazo o abandono.",
                "ref": "Ruocco et al. (2013, Am J Psychiatry meta-análisis de 28 estudios)"
            },
            "fmri_pain": {
                "header": "Red de Detección de Amenaza (Prominencia)",
                "title": "Cíngulo Dorsal (dACC) e Ínsula Anterior",
                "status": "Activación Nociceptiva del Rechazo (Eisenberger et al.)",
                "analogy": "Para el cerebro, la exclusión o el silencio afectivo duele con la misma intensidad que una quemadura en la piel.",
                "summary": "En pruebas de laboratorio de rechazo social (Cyberball), el cerebro activa los mismos centros del dolor físico agudo, induciendo una desesperación visceral por calmarlo.",
                "ref": "Eisenberger & Lieberman (2004, Science) | Domsalla et al. (2014)"
            },
            "ratio": {
                "header": "Equilibrio Freno - Acelerador",
                "title": "Corteza Prefrontal Ventromedial (vmPFC)",
                "status": "Desconexión del Freno Reflexivo (Cullen et al.)",
                "analogy": "Un auto con el acelerador atascado y sin líquido en los frenos durante una bajada empinada.",
                "summary": "Durante los picos de angustia, la corteza reflexiva pierde el control, impidiendo que el paciente pueda calmarse pensando lógicamente las cosas.",
                "ref": "Cullen et al. (2011) | Coccaro et al. (2007)"
            }
        },
        "nodes": [
            {
                "id": "amg",
                "name": "Amígdala Basolateral",
                "plane": "Corte Coronal Anterior (a la altura del lóbulo temporal)",
                "coords": [1.9, -0.6, -1.3],
                "color": "#ef4444",
                "rad": 0.40,
                "hz": 8.0,
                "status": "HIPERACTIVIDAD FÁSICA",
                "analogy": "Alarma de incendio ultrasensible que se activa ante el vapor de una taza de café.",
                "example": "Su pareja tarda 30 minutos en contestar un mensaje y el paciente experimenta taquicardia y pánico como si estuviera frente a un peligro físico mortal.",
                "healthy_scan": "Verde suave: reactividad baja y regulada ante estímulos neutros.",
                "patient_scan": "Rojo intenso y brillante: paroxismo BOLD masivo con retardo en apagarse.",
                "desc": "Detecta peligro y abandono donde solo hay una pausa cotidiana normal.",
                "voice": "Amígdala basolateral. Imaginemos una alarma de humo tan sensible que suena ante el simple vapor de un café. En el trastorno límite, un mensaje sin responder durante media hora es interpretado como un riesgo vital de abandono. New y Schmahl demostraron que este núcleo no logra apagar la señal de miedo a tiempo."
            },
            {
                "id": "vmpfc",
                "name": "Corteza Prefrontal Ventromedial (vmPFC)",
                "plane": "Corte Sagital Medial (suelo anterior del lóbulo frontal)",
                "coords": [0.0, 3.8, -0.8],
                "color": "#38bdf8",
                "rad": 0.38,
                "hz": 1.0,
                "status": "COLAPSO INHIBITORIO",
                "analogy": "Pedal de freno hidráulico que se queda sin líquido en plena velocidad.",
                "example": "La persona sabe que romper un celular o autolesionarse no solucionará nada, pero el freno cerebral no tiene fuerza sináptica para parar el impulso.",
                "healthy_scan": "Azul/Cian activo: modulación inhibitoria continua sobre las emociones.",
                "patient_scan": "Gris oscuro / Apagado: desconexión funcional transitoria durante la crisis.",
                "desc": "Pierde la capacidad de reflexionar y tranquilizar al sistema emocional.",
                "voice": "Corteza prefrontal ventromedial. Es el pedal de freno del cerebro emocional. En este cuadro, el freno pierde eficacia durante la crisis. Aunque la persona comprenda racionalmente que autolesionarse empeorará todo, la corteza no logra ejercer la fuerza necesaria para detener el impulso."
            },
            {
                "id": "dacc",
                "name": "Cíngulo Anterior Dorsal (dACC)",
                "plane": "Corte Sagital Medial (arco sobre el cuerpo calloso)",
                "coords": [0.0, 1.8, 1.8],
                "color": "#f43f5e",
                "rad": 0.42,
                "hz": 7.2,
                "status": "DOLOR SOCIAL AGUDO",
                "analogy": "Un procesador que traduce el desapego en una quemadura física real.",
                "example": "Una discusión cotidiana se siente literalmente como una herida en el cuerpo; el corte físico busca muchas veces tapar o distraer ese dolor psíquico atroz.",
                "healthy_scan": "Tono neutro: distingue la incomodidad social del dolor físico real.",
                "patient_scan": "Naranja y rojo vivo: activación idéntica a una lesión tisular física.",
                "desc": "Procesa la exclusión afectiva con la misma crudeza que una agresión física.",
                "voice": "Córtex cingulado anterior dorsal. Es el nodo del dolor social. Naomi Eisenberger demostró en Science que el cerebro procesa la exclusión en los mismos circuitos que una quemadura. Ante el rechazo percibido, este núcleo se enciende con tal fuerza que la autolesión suele buscar mitigar ese dolor psíquico abrumador."
            },
            {
                "id": "insula",
                "name": "Ínsula Anterior Agranular",
                "plane": "Corte Axial Medio (profundidad de la cisura lateral)",
                "coords": [2.8, 0.7, -0.2],
                "color": "#e11d48",
                "rad": 0.36,
                "hz": 6.5,
                "status": "MALESTAR INTEROCEPTIVO",
                "analogy": "El altavoz que traduce la angustia en una sensación de vacío en el pecho.",
                "example": "Sensación constante de tener un 'hueco en el estómago' que la persona intenta llenar desesperadamente con comida, sustancias o compañía constante.",
                "healthy_scan": "Actividad fisiológica normal de monitorización visceral del cuerpo.",
                "patient_scan": "Amarillo brillante: hipersensibilidad interoceptiva y vivencia de vacío crónico.",
                "desc": "Sustrato del vacío crónico y de la tensión visceral intolerable.",
                "voice": "Ínsula anterior agranular. Traduce el malestar emocional en sensaciones corporales. Constituye el sustrato de esa vivencia de vacío en el pecho que se describe en consultorio y que precipita intentos urgentes de alivio inmediato."
            }
        ],
        "tracts": [
            {
                "from": [1.8, -0.6, -1.3], "to": [0.0, 3.8, -0.8], "ctrl": [2.6, 1.5, -1.6],
                "name": "Fascículo Uncinado",
                "status": "broken",
                "analogy": "Un cable de fibra óptica roto por donde la señal de calma llega tarde.",
                "voice": "Fascículo uncinado. Es la vía de sustancia blanca que conecta la corteza frontal con la amígdala. En el trastorno límite presenta desorganización microestructural, retrasando la llegada de la señal reguladora."
            }
        ],
        "case_vignette": {
            "title": "Viñeta Clínica Ilustrativa: Descompensación por Distanciamiento Percibido",
            "narrative": "Paciente de 24 años consulta en guardia tras ingerir una dosis excesiva de ansiolíticos y presentar lesiones cortantes superficiales en el antebrazo. El hecho precipitante fue una demora de tres horas de su pareja en responder un mensaje luego de una discusión menor. Durante la entrevista refiere: 'Sentí un frío quemante en el pecho, como si dejara de existir; necesitaba que el dolor parara de inmediato'.",
            "mechanistic_reading": "La percepción de distanciamiento activa el dACC y la ínsula anterior simulando una agresión tisular real (Eisenberger, 2004). El fascículo uncinado desorganizado (Schmahl, 2014) no transmite a tiempo la modulación del vmPFC, impidiendo contextualizar la demora y favoreciendo la conducta impulsiva como intento de regulación afectiva extrema."
        },
        "whodas_matrix": [
            {
                "domain": "Esfera Conyugal & Apego (CIE-11)",
                "pct_label": "Prevalencia observada: ~96%",
                "scientific_basis": "Cohorte CLPS (Collaborative Longitudinal Personality Disorders Study, Gunderson et al., 2011; Zanarini et al., 2012): el 96% de los pacientes presenta antecedentes de inestabilidad conyugal severa, escisión vincular o rupturas conflictivas recurrentes.",
                "color": "#ef4444",
                "clinical_correlate": "Mecanismos de escisión o splitting. La figura de apego oscila entre la idealización y el rechazo extremo ante la mínima sospecha de abandono."
            },
            {
                "domain": "Servicios de Urgencia & Salud Mental",
                "pct_label": "Prevalencia observada: ~92%",
                "scientific_basis": "Zanarini et al. (2008, Am J Psychiatry, seguimiento a 10 años): el 92% de los pacientes diagnosticados requirió al menos una admisión de urgencia o internación por conductas autolesivas no suicidas o crisis de angustia.",
                "color": "#ef4444",
                "clinical_correlate": "Utilización reiterada de servicios de guardia motivada por conductas autolesivas no suicidas o desregulaciones afectivas paroxísticas."
            },
            {
                "domain": "Cohesión del Self & Identidad",
                "pct_label": "Prevalencia observada: ~94%",
                "scientific_basis": "Criterio de Difusión de Identidad (DSM-5 Sección III / Kernberg, 2006): el 94% de los casos reporta sensación crónica de vacío, incertidumbre vocacional y labilidad en la autoimagen.",
                "color": "#f43f5e",
                "clinical_correlate": "Vivencia de vacío interior; adaptación maleable de valores o metas personales a la figura cercana para evitar la soledad."
            },
            {
                "domain": "Red Familiar Primaria (WHODAS 2.0)",
                "pct_label": "Prevalencia observada: ~88%",
                "scientific_basis": "Estudios de carga familiar en TLP (Bailey & Grenyer, 2013; Skodol et al., 2005): el 88% de las familias de origen puntúa en rangos de sobrecarga y desgaste emocional severo.",
                "color": "#fb923c",
                "clinical_correlate": "Convivencia marcada por hiperalerta y desgaste afectivo en cuidadores primarios frente a la imprevisibilidad de las crisis."
            },
            {
                "domain": "Funcionamiento Laboral / Académico",
                "pct_label": "Prevalencia observada: ~72%",
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
                "header": "Tractografía de Sustancia Blanca (DTI)",
                "title": "Fascículo Uncinado Bilateral",
                "status": "Interrupción de la Conexión Moral (Craig et al.)",
                "analogy": "Un teléfono con la línea cortada entre el centro del miedo y el juzgado de la conciencia.",
                "summary": "Interrupción estructural mayor en la vía que une la amígdala con la corteza orbitofrontal. El cerebro no puede enviar la señal de freno moral ante la transgresión.",
                "ref": "Craig et al. (2009, Mol Psychiatry) | Motzkin et al. (2011, J Neurosci)"
            },
            "fmri_amygdala": {
                "header": "Reactividad Funcional (fMRI / BOLD)",
                "title": "Complejo Amigdalino Basolateral",
                "status": "Hipoactividad e Inmunidad al Castigo (Blair et al.)",
                "analogy": "Un detector de humo sin batería: aunque haya fuego real alrededor, no emite ningún sonido.",
                "summary": "Ausencia de respuesta autonómica y hemodinámica ante expresiones de terror o llanto ajeno. Refractariedad biológica al aprendizaje por castigo.",
                "ref": "Blair et al. (2004, NeuroImage) | Birbaumer et al. (2005)"
            },
            "fmri_pain": {
                "header": "Red de Resonancia Social (Empatía)",
                "title": "Ínsula Anterior (Empatía Afectiva)",
                "status": "Anestesia Somatosensorial Vicaria (Glenn & Raine)",
                "analogy": "Mirar a alguien sangrar a través de un vidrio blindado sin sentir ninguna molestia en el estómago.",
                "summary": "Falla en la activación insular frente al sufrimiento ajeno. Teoría de la Mente cognitiva intacta (capacidad de engaño) con atrofia de la empatía emocional.",
                "ref": "Glenn & Raine (2014) | Decety et al. (2013)"
            },
            "ratio": {
                "header": "Bucle Córtico-Estriatal de Recompensa",
                "title": "Núcleo Accumbens y Estriado Ventral",
                "status": "Búsqueda Predatoria de Beneficio Inmediato",
                "analogy": "Un motor potente sin volante que avanza arrasando todo lo que encuentra a su paso.",
                "summary": "Hiperreactividad dopaminérgica orientada a ganancias instrumentales, sin que el lóbulo frontal compute el costo moral ni el riesgo de sanción penal.",
                "ref": "Buckholtz et al. (2010, Nature Neurosci)"
            }
        },
        "nodes": [
            {
                "id": "amg",
                "name": "Amígdala (Hipoactiva)",
                "plane": "Corte Coronal Anterior (polo medial temporal)",
                "coords": [1.9, -0.6, -1.3],
                "color": "#1e293b",
                "rad": 0.30,
                "hz": 0.4,
                "status": "HIPORREACTIVIDAD AL MIEDO",
                "analogy": "Un detector de humo al que le quitaron la batería: no suena ante el peligro.",
                "example": "El sujeto comete un delito grave manteniendo una frecuencia cardíaca de 55 latidos por minuto, sin temblor ni sudoración.",
                "healthy_scan": "Verde activo: reactividad autonómica normal frente a la transgresión y el castigo.",
                "patient_scan": "Azul oscuro / Apagado: ausencia casi total de señal BOLD ante caras aterradas.",
                "desc": "Inmunidad al miedo y al condicionamiento aversivo por sanciones.",
                "voice": "Amígdala hipoactiva. Imaginemos un detector de humo sin batería. Aunque haya fuego real alrededor, no se activa. Mientras una persona promedio experimenta taquicardia ante la transgresión o el sufrimiento ajeno, aquí predomina la estabilidad autonómica. Craig y Blair documentaron en NeuroImage esta marcada refractariedad al castigo."
            },
            {
                "id": "vmpfc",
                "name": "vmPFC (Polo Moral Desconectado)",
                "plane": "Corte Sagital Medial (suelo anterior frontal)",
                "coords": [0.0, 3.8, -0.8],
                "color": "#334155",
                "rad": 0.32,
                "hz": 0.5,
                "status": "DESCONEXIÓN MORAL",
                "analogy": "Una calculadora de negocios fría y calculadora que no siente remordimientos.",
                "example": "Comprende perfectamente que estafar a sus padres está mal ante la ley, pero esa noción no le genera el menor freno afectivo en el cuerpo.",
                "healthy_scan": "Cian encendido: integra el valor moral y el daño ajeno en las decisiones.",
                "patient_scan": "Gris apagado: juicio instrumental frío desprovisto de resonancia somática.",
                "desc": "Conoce la norma a nivel lógico pero no siente la carga afectiva de la culpa.",
                "voice": "Corteza prefrontal ventromedial. Funciona de manera calculadora y analítica. Comprende las normas jurídicas a nivel conceptual, pero esa información carece de resonancia afectiva. Dañar a un tercero se procesa como un costo de transacción admisible para lograr un objetivo."
            },
            {
                "id": "accumbens",
                "name": "Núcleo Accumbens (Estriado)",
                "plane": "Corte Coronal Basal (estriado ventral)",
                "coords": [1.0, 1.1, -0.7],
                "color": "#eab308",
                "rad": 0.44,
                "hz": 7.5,
                "status": "HIPERACTIVIDAD PREDATORIA",
                "analogy": "Un acelerador voraz que busca dinero o poder sin mirar a los costados.",
                "example": "Ante la oportunidad de una ganancia ilícita, el circuito de recompensa se sobreactiva descartando cualquier cálculo de consecuencias futuras.",
                "healthy_scan": "Actividad modulada por el control prefrontal inhibitorio.",
                "patient_scan": "Amarillo vivo y brillante: búsqueda insaciable de incentivo inmediato.",
                "desc": "Motor de gratificación inmediata y dominancia instrumental.",
                "voice": "Núcleo accumbens estriatal. Es el centro de búsqueda de recompensa. Frente a la oportunidad de obtener un beneficio inmediato a costa de otros, este núcleo se sobreactiva sin que intervenga el freno inhibitorio frontal."
            },
            {
                "id": "insula",
                "name": "Ínsula (Empatía Afectiva Anestesiada)",
                "plane": "Corte Axial Medio (cisura lateral)",
                "coords": [2.8, 0.7, -0.2],
                "color": "#1e293b",
                "rad": 0.26,
                "hz": 0.3,
                "status": "ANESTESIA EMPÁTICA",
                "analogy": "Mirar el sufrimiento de una persona como si fuera una película de ficción en televisión.",
                "example": "Presencia el llanto desconsolado de su víctima sin experimentar la menor sensación de malestar o compasión física.",
                "healthy_scan": "Cálido: activación empática inmediata al ver dolor o angustia ajena.",
                "patient_scan": "Azul frío / Cero señal: incapacidad de resonar con el dolor ajeno.",
                "desc": "Incapacidad biológica de compadecerse del sufrimiento provocado.",
                "voice": "Ínsula anterior agranular anestesiada. Es el asiento de la empatía emocional somatizada. Su hipoactivación explica por qué estas personas pueden presenciar el daño causado sin experimentar malestar gástrico ni remordimiento."
            }
        ],
        "tracts": [
            {
                "from": [1.8, -0.6, -1.3], "to": [0.0, 3.8, -0.8], "ctrl": [2.6, 1.5, -1.6],
                "name": "Fascículo Uncinado",
                "status": "broken",
                "analogy": "Línea cortada que impide que el miedo al castigo frene el plan delictivo.",
                "voice": "Fascículo uncinado cortado. Motzkin comprobó en poblaciones penitenciarias que la vía de comunicación entre la señal de aversión y el juicio moral está interrumpida, anulando el freno somático ante la transgresión."
            }
        ],
        "case_vignette": {
            "title": "Viñeta Clínica Ilustrativa: Evaluación Pericial Forense",
            "narrative": "Hombre de 32 años evaluado en contexto pericial tras múltiples estafas reiteradas y agresiones patrimoniales a allegados. Durante la entrevista se muestra distendido, cortés y con un relato convincente. Al consultarle sobre las pérdidas económicas de las víctimas, responde serenamente: 'Ellos asumieron el riesgo; en los negocios quien no se aviva pierde'. Presenta estabilidad autonómica con frecuencia cardíaca basal de 58 latidos por minuto.",
            "mechanistic_reading": "La ausencia de reactividad fisiológica ante el daño ajeno refleja la hiporreactividad amigdalina descrita por Blair (2004). El fascículo uncinado desarticulado (Motzkin, 2011) impide que la noción moral de 'perjuicio' regule la actividad del núcleo accumbens, que opera bajo búsqueda exclusiva de beneficio instrumental (Buckholtz, 2010)."
        },
        "whodas_matrix": [
            {
                "domain": "Marco Judicial & Fuero Penal",
                "pct_label": "Prevalencia observada: ~99%",
                "scientific_basis": "Meta-análisis penitenciario (Fazel & Danesh, 2002, The Lancet; Hare, 2003 PCL-R): en poblaciones con diagnóstico confirmado de TASP/psicopatía, la tasa de conflicto judicial y reincidencia delictiva roza el 99%.",
                "color": "#ef4444",
                "clinical_correlate": "Reincidencia en delitos patrimoniales, transgresión deliberada de normativas y refractariedad al valor correctivo de las penas."
            },
            {
                "domain": "Vínculos & Instrumentalización",
                "pct_label": "Prevalencia observada: ~96%",
                "scientific_basis": "Estudios de empatía interpersonal (Blair, 2008; Cleckley, 1941): el 96% de los lazos afectivos se estructuran de forma asimétrica, utilitaria o predatoria.",
                "color": "#ef4444",
                "clinical_correlate": "Uso instrumental de parejas o allegados con fines económicos, sexuales o de conveniencia personal, prescindiendo de ellos al cesar su utilidad."
            },
            {
                "domain": "Ámbito Contractual & Financiero",
                "pct_label": "Prevalencia observada: ~90%",
                "scientific_basis": "Estudio epidemiológico NESARC (Grant et al., 2004): el 90% de los sujetos con rasgos antisociales graves registra cesantías por fraude, quiebras o deshonestidad.",
                "color": "#fb923c",
                "clinical_correlate": "Incumplimiento deliberado de compromisos económicos, estafas y falta de lealtad en acuerdos comerciales formales."
            },
            {
                "domain": "Simulación Pericial Forense",
                "pct_label": "Prevalencia observada: ~65%",
                "scientific_basis": "Mediciones con SIRS-2 (Structured Interview of Reported Symptoms, Rogers et al., 2011): un 65% de los peritados muestra maniobras activas de simulación sintomática.",
                "color": "#eab308",
                "clinical_correlate": "Uso instrumental del examen psiquiátrico forense para simular cuadros amnésicos o psicóticos y atenuar la imputabilidad penal."
            },
            {
                "domain": "Insight & Conciencia de Enfermedad",
                "pct_label": "Prevalencia observada: ~10%",
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
                "header": "Tractografía de Sustancia Blanca (DTI)",
                "title": "Sustancia Blanca Frontomedial",
                "status": "Integridad Preservada con Sesgo de Dominancia",
                "analogy": "Líneas de comunicación intactas para planificar estrategias, pero desconectadas del dolor ajeno.",
                "summary": "Vías de mentalización cognitiva intactas. Preservación del cálculo relacional estratégico junto con hipoconectividad hacia redes de empatía emocional.",
                "ref": "Fan et al. (2011, SCAN) | Nenadic et al. (2015)"
            },
            "fmri_amygdala": {
                "header": "Reactividad Funcional (fMRI / BOLD)",
                "title": "Cíngulo Dorsal / Amígdala",
                "status": "Herida Narcisista y Alarma por Pérdida de Estatus",
                "analogy": "Un radar de prestigio que detecta una ofensa mortal ante el menor gesto de desacato.",
                "summary": "Paroxismo en dACC ante el cuestionamiento jerárquico, desencadenando una respuesta hostil orientada a restituir la autovaloración dañada.",
                "ref": "Pincus & Lukowitsky (2010) | Schulze et al. (2013)"
            },
            "fmri_pain": {
                "header": "Red de Resonancia Social (Empatía)",
                "title": "Corteza Insular Anterior",
                "status": "Disociación Empática Afectiva (Fan et al.)",
                "analogy": "Saber exactamente cómo desarmar a alguien con palabras, sin que importe el daño provocado.",
                "summary": "Reducción de activación insular ante el dolor ajeno. El sujeto comprende conceptualmente el estado mental del otro pero no resuena visceralmente con él.",
                "ref": "Jankowiak-Siuda et al. (2015) | Baskin-Sommers et al."
            },
            "ratio": {
                "header": "Red por Defecto vs. Prominencia",
                "title": "Compensación Grandiosa Frontal",
                "status": "Gasto Metabólico en la Autoimagen (Scalabrini)",
                "analogy": "Un andamio de oro construido con gran esfuerzo para tapar un piso de barro frágil.",
                "summary": "Hiperactivación frontal sostenida para apuntalar una narrativa de autosuficiencia y superioridad que neutralice la extrema vulnerabilidad del self.",
                "ref": "Scalabrini et al. (2017, Hum Brain Mapp)"
            }
        },
        "nodes": [
            {
                "id": "dacc",
                "name": "dACC (Radar de Jerarquía)",
                "plane": "Corte Sagital Medial (arco sobre el cuerpo calloso)",
                "coords": [0.0, 1.8, 1.8],
                "color": "#a855f7",
                "rad": 0.42,
                "hz": 7.4,
                "status": "HIPERREACTIVO AL DESPRECIO",
                "analogy": "Un sensor de jerarquía social en guardia permanente ante la falta de elogios.",
                "example": "En una reunión de trabajo, si una propuesta suya no es aplaudida de inmediato, percibe una ofensa mortal a su estatus.",
                "healthy_scan": "Modulación equilibrada frente a críticas constructivas.",
                "patient_scan": "Violeta/Rojo paroxístico: detonación aguda de alarma por descalificación.",
                "desc": "Alarma paroxística ante la crítica o la pérdida de admiración externa.",
                "voice": "Cíngulo anterior dorsal. Es un radar de jerarquía social en hipervigilancia continua. Si una opinión suya no es aplaudida de inmediato, este núcleo detecta una ofensa mortal a su estatus, detonando una respuesta de furia fría o venganza calculada."
            },
            {
                "id": "vmpfc",
                "name": "vmPFC (Autoimagen Grandiosa)",
                "plane": "Corte Sagital Medial (polo medial frontal)",
                "coords": [0.0, 3.8, -0.8],
                "color": "#c084fc",
                "rad": 0.38,
                "hz": 2.8,
                "status": "COMPENSACIÓN GRANDIOSA",
                "analogy": "Un andamio dorado que requiere energía continua para no desplomarse.",
                "example": "Gasta horas rumiando sobre sus éxitos pasados para no sentir la angustia de un fracaso reciente.",
                "healthy_scan": "Autoestima estable sin necesidad de reafirmación constante.",
                "patient_scan": "Hipermetabolismo compensatorio: sostén de la fachada de superioridad.",
                "desc": "Sostiene la fachada de grandeza como barrera defensiva ante el vacío.",
                "voice": "Corteza prefrontal ventromedial. Es como construir un andamio de oro sobre cimientos de barro. Se gasta una enorme cantidad de energía metabólica en sostener el relato de que se es superior a todos, precisamente para tapar un terror pánico a la mediocridad o al vacío interior."
            },
            {
                "id": "amg",
                "name": "Amígdala (Rabia Narcisista)",
                "plane": "Corte Coronal Anterior (polo medial temporal)",
                "coords": [1.8, -0.6, -1.3],
                "color": "#ec4899",
                "rad": 0.34,
                "hz": 5.2,
                "status": "VULNERABILIDAD FÁSICA",
                "analogy": "Una chispa que prende fuego cuando se pone en duda su perfección.",
                "example": "Ante una corrección menor de su pareja, reacciona con un ataque verbal despiadado para volver a tomar el control.",
                "healthy_scan": "Regulación emocional sin hostilidad defensiva.",
                "patient_scan": "Pico fásico de cólera ante la exposición de debilidad.",
                "desc": "Explosiones de hostilidad vindicativa ante la herida del orgullo.",
                "voice": "Amígdala fásica. Dispara la llamada rabia narcisista. Ante una crítica fundada de un subordinado o pareja, la herida narcisista desata una reacción colérica que busca descalificar y aniquilar verbalmente al otro para restituir el propio valor dañado."
            },
            {
                "id": "insula",
                "name": "Ínsula (Empatía Afectiva Desconectada)",
                "plane": "Corte Axial Medio (cisura lateral)",
                "coords": [2.8, 0.7, -0.2],
                "color": "#334155",
                "rad": 0.28,
                "hz": 0.8,
                "status": "ANESTESIA EMPÁTICA",
                "analogy": "Saber qué pieza mover en el ajedrez sin conmoverse por la pieza que cae.",
                "example": "Entiende perfectamente que su desprecio hace llorar a su pareja, pero no experimenta ninguna compasión al respecto.",
                "healthy_scan": "Resonancia afectiva compartida ante el llanto del otro.",
                "patient_scan": "Azul grisáceo / Inactivo: ausencia de conmoción somática.",
                "desc": "Comprende el dolor ajeno pero no siente compasión visceral por él.",
                "voice": "Ínsula anterior desconectada. Fan demostró en la revista SCAN que el narcisista tiene empatía cognitiva intacta, es decir, sabe perfectamente qué te duele y cómo herirte, pero carece de empatía afectiva; no siente compasión alguna al hacerlo."
            }
        ],
        "tracts": [
            {
                "from": [0.0, 1.8, 1.8], "to": [0.0, 3.8, -0.8], "ctrl": [0.0, 2.8, 0.6],
                "name": "Eje de Autoevaluación Hipervigilante",
                "status": "hyper",
                "analogy": "Circuito de alerta que monitorea la aprobación del auditorio segundo a segundo.",
                "voice": "Eje de autoevaluación. Obliga al sujeto a monitorear obsesivamente cuántos aplausos o muestras de sumisión recibe por minuto para mantener equilibrada su autoestima."
            }
        ],
        "case_vignette": {
            "title": "Viñeta Clínica Ilustrativa: Descompensación por Pérdida de Jerarquía",
            "narrative": "Hombre de 48 años, directivo de empresa, consulta acompañado por su pareja tras ser desvinculado de su puesto gerencial durante una reestructuración. Presenta insomnio global, desinterés por sus actividades habituales e ideación tanática pasiva. Durante la entrevista expresa con amargura: 'No puedo tolerar que personas mediocres me miren con lástima; preferiría no despertar más'. Rechaza el diagnóstico de depresión considerándolo inaceptable para su trayectoria.",
            "mechanistic_reading": "La pérdida del rol de estatus desarticula el constructo compensatorio sostenido por la red por defecto (Scalabrini, 2017). La herida narcisista activa el dACC y la amígdala (Pincus, 2010) provocando un cuadro disfórico melancólico con riesgo de conductas autolesivas motivadas por la intolerancia a la vergüenza."
        },
        "whodas_matrix": [
            {
                "domain": "Esfera Conyugal (Dinámica de Poder)",
                "pct_label": "Prevalencia observada: ~92%",
                "scientific_basis": "Estudios de patología narcisista en vínculos (Campbell et al., 2002; Ronningstam, 2005): el 92% de las parejas estables refiere dinámicas de descalificación o castigo con silencio prolongado.",
                "color": "#ef4444",
                "clinical_correlate": "Exigencia de adhesión incondicional. El cónyuge es situado en un rol de confirmación constante; las discrepancias son castigadas con desprecio o retiro del afecto."
            },
            {
                "domain": "Cohesión del Self (Riesgo de Colapso)",
                "pct_label": "Prevalencia observada: ~95%",
                "scientific_basis": "Meta-análisis sobre Narcisismo Vulnerable y Suicidio (Pincus et al., 2009; Coleman et al., 2017): un 95% de los pacientes presenta oscilaciones severas hacia disforia ante fracasos reales.",
                "color": "#a855f7",
                "clinical_correlate": "Extrema fragilidad ante el declive laboral, financiero o físico, pudiendo desencadenar cuadros depresivos refractarios de difícil abordaje."
            },
            {
                "domain": "Entorno Laboral & Jerárquico",
                "pct_label": "Prevalencia observada: ~84%",
                "scientific_basis": "Psicología organizacional de la personalidad (Babiak & O'Toole, 2012): el 84% de los puestos de liderazgo con rasgos de grandiosidad presenta rotación elevada de colaboradores.",
                "color": "#fb923c",
                "clinical_correlate": "Dificultad para el trabajo horizontal. Apropiación de logros de subordinados y hostilidad ante colegas evaluados como competencia."
            },
            {
                "domain": "Red Familiar de Origen",
                "pct_label": "Prevalencia observada: ~76%",
                "scientific_basis": "Dinámicas transgeneracionales (Kernberg, 1984; Miller, 1981): el 76% de los vínculos con hijos está condicionado al cumplimiento de expectativas de éxito del progenitor.",
                "color": "#fb923c",
                "clinical_correlate": "Valoración de los descendientes como extensiones de prestigio personal, con distanciamiento punitivo si eligen caminos divergentes."
            },
            {
                "domain": "Adherencia a Salud Mental",
                "pct_label": "Prevalencia observada: ~50%",
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
                "header": "Tractografía de Sustancia Blanca (DTI)",
                "title": "Vías Frontoparietales Dorsolaterales",
                "status": "Varianza Difusa en Conectividad Frontal",
                "analogy": "Una pintura al óleo vista de lejos: capta la emoción general pero pierde el detalle fino de los hechos.",
                "summary": "Menor sincronización dorsolateral que favorece un estilo cognitivo global, impresionista y con elevada sugestionabilidad ante señales sociales.",
                "ref": "Buchsbaum et al. | Schore et al. (Neuropsychoanalysis)"
            },
            "fmri_amygdala": {
                "header": "Reactividad Funcional (fMRI / BOLD)",
                "title": "Red de Recompensa Estriatal",
                "status": "Hipersensibilidad al Halago y la Aprobación",
                "analogy": "Un actor sobre el escenario que necesita aplausos constantes para no sentir que la obra fracasó.",
                "summary": "Respuesta fásica amplificada en el núcleo accumbens y amígdala ante señales de simpatía, seducción o validación interpersonal inmediata.",
                "ref": "Somerville et al. (2010) | Vuilleumier et al."
            },
            "fmri_pain": {
                "header": "Red de Resonancia Social (Somatización)",
                "title": "Corteza Somatosensorial / Ínsula",
                "status": "Amplificación Conversiva Interoceptiva",
                "analogy": "El cuerpo actuando en escena lo que las palabras no logran procesar calmadamente.",
                "summary": "Traducción somática de tensiones afectivas: el malestar que no encuentra elaboración reflexiva se expresa mediante síntomas neurológicos funcionales o conversiones.",
                "ref": "Caria et al. (2012) | Perez et al. (2015, Brain)"
            },
            "ratio": {
                "header": "Acoplamiento Frontolímbico",
                "title": "Control Reflexivo vs. Teatralidad",
                "status": "Estilo Impresionista Poco Secuencial",
                "analogy": "Un reflector potente que ilumina con brillo una esquina pero deja todo el resto en penumbra.",
                "summary": "Dificultad para mantener la concentración en tareas metódicas que carecen de visibilidad; desorganización conductual al perder el foco de atención.",
                "ref": "Shapiro (Neurotic Styles) | Kernberg"
            }
        },
        "nodes": [
            {
                "id": "amg",
                "name": "Amígdala Límbica",
                "plane": "Corte Coronal Anterior (polo medial temporal)",
                "coords": [1.8, -0.6, -1.3],
                "color": "#06b6d4",
                "rad": 0.36,
                "hz": 6.2,
                "status": "HIPEREXCITABLE LÁBIL",
                "analogy": "Fuegos artificiales intensos pero que se apagan a los pocos minutos.",
                "example": "Llora desconsoladamente en una discusión menor y diez minutos después ríe distendida al recibir un elogio.",
                "healthy_scan": "Modulación serena y estable del afecto cotidiano.",
                "patient_scan": "Paroxismo breve y cambiante de respuesta emocional.",
                "desc": "Emotividad intensa y volátil; intolerancia a la neutralidad del entorno.",
                "voice": "Amígdala límbica lábil. Presenta respuestas afectivas rápidas y de gran expresividad externa pero de corta duración. Puede observarse un llanto desconsolado ante una situación menor, seguido minutos después por serenidad si la atención del entorno se restablece."
            },
            {
                "id": "accumbens",
                "name": "Núcleo Accumbens Social",
                "plane": "Corte Coronal Basal (estriado ventral)",
                "coords": [1.0, 1.1, -0.7],
                "color": "#22d3ee",
                "rad": 0.40,
                "hz": 6.5,
                "status": "HIPERRESPUESTA AL FEEDBACK",
                "analogy": "Adicción al reflector y al aplauso de los demás.",
                "example": "Si en una reunión el grupo habla de otro tema, recurre a dramatizaciones o seducción para volver a ser el centro.",
                "healthy_scan": "Actividad social equilibrada sin demanda de validación continua.",
                "patient_scan": "Cian brillante: circuito de recompensa activado por la atención externa.",
                "desc": "Dependencia del halago y del protagonismo interpersonal.",
                "voice": "Núcleo accumbens social. Circuito estrechamente ligado a la validación interpersonal. La persona experimenta una necesidad marcada de protagonismo, recurriendo a la seducción o al dramatismo si percibe que el interés del grupo decae."
            },
            {
                "id": "insula",
                "name": "Ínsula Somatosensorial",
                "plane": "Corte Axial Medio (cisura lateral)",
                "coords": [2.8, 0.7, -0.2],
                "color": "#0891b2",
                "rad": 0.34,
                "hz": 5.4,
                "status": "SOMATIZACIÓN INTEROCEPTIVA",
                "analogy": "El cuerpo hablando en voz alta lo que la mente no pone en palabras.",
                "example": "Ante un desacuerdo familiar, experimenta mareos súbitos y pérdida de fuerza en las piernas sin causa orgánica.",
                "healthy_scan": "Integración visceral armónica sin conversiones.",
                "patient_scan": "Activación marcada: amplificación de síntomas corporales funcionales.",
                "desc": "Conversión corporal de angustias que no logran elaborarse verbalmente.",
                "voice": "Ínsula somatosensorial. Traduce tensiones emocionales no elaboradas en manifestaciones físicas. Ante desencuentros interpersonales, amplifica las señales viscerales pudiendo generar síntomas neurológicos funcionales o desmayos psicógenos."
            },
            {
                "id": "vmpfc",
                "name": "vmPFC Impresionista",
                "plane": "Corte Sagital Medial (suelo anterior frontal)",
                "coords": [0.0, 3.8, -0.8],
                "color": "#475569",
                "rad": 0.32,
                "hz": 1.4,
                "status": "PROCESAMIENTO DIFUSO",
                "analogy": "Una mirada panorámica que no repara en la letra chica de los problemas.",
                "example": "Relata un conflicto grave en términos teatrales y vagos ('fue horrible, todo un desastre') sin poder precisar los hechos concretos.",
                "healthy_scan": "Procesamiento secuencial y analítico ordenado.",
                "patient_scan": "Actividad difusa: razonamiento guiado por impresiones globales.",
                "desc": "Razonamiento impresionista con escaso análisis secuencial de los hechos.",
                "voice": "Corteza prefrontal impresionista. Su estilo cognitivo capta la tonalidad afectiva general de las situaciones pero tiende a omitir el análisis detallado y secuencial de las contingencias."
            }
        ],
        "tracts": [
            {
                "from": [1.8, -0.6, -1.3], "to": [1.0, 1.1, -0.7], "ctrl": [1.3, 0.4, -0.8],
                "name": "Eje Límbico-Recompensa",
                "status": "hyper",
                "analogy": "Vía que premia inmediatamente cualquier conducta que logre captar la atención del grupo.",
                "voice": "Eje límbico de recompensa. Refuerza positivamente la repetición de conductas expresivas y de seducción que garanticen la aprobación del auditorio."
            }
        ],
        "case_vignette": {
            "title": "Viñeta Clínica Ilustrativa: Manifestación Conversiva Aguda",
            "narrative": "Mujer de 29 años ingresa a la guardia médica con paresia funcional de miembros inferiores e hiperventilación. El cuadro se presentó durante una celebración familiar en la que su hermana menor anunció un logro personal relevante, captando la atención de los presentes. La paciente experimentó mareos súbitos y cayó al suelo sin signos de traumatismo ni relajación de esfínteres. La exploración neurológica y los estudios de neuroimagen no muestran sustrato lesional orgánico.",
            "mechanistic_reading": "La percepción de invisibilidad social moviliza la corteza somatosensorial e insular (Perez, 2015), canalizando el afecto displacentero hacia una manifestación física conversiva que restablece de inmediato la atención del entorno, concordante con el estilo impresionista descrito por Shapiro."
        },
        "whodas_matrix": [
            {
                "domain": "Esfera Conyugal (Sobredramatización)",
                "pct_label": "Prevalencia observada: ~85%",
                "scientific_basis": "Estudios clínicos de estilo histriónico (Bornstein, 2012; Horowitz, 1991): el 85% reporta desilusión recurrente con parejas al descender la intensidad apasionada inicial.",
                "color": "#ef4444",
                "clinical_correlate": "Exigencia de romanticismo novelesco sostenido. La rutina cotidiana normal es vivenciada como desamor, facilitando conductas de coqueteo con terceros para reactivar el interés."
            },
            {
                "domain": "Servicio de Urgencias Médicas",
                "pct_label": "Prevalencia observada: ~82%",
                "scientific_basis": "Frecuentación hospitalaria en trastornos somatomorfos/histriónicos (Kroenke et al., 2007): un 82% registra admisiones por hiperventilación o cuadros neurológicos sin base orgánica.",
                "color": "#fb923c",
                "clinical_correlate": "Consultas en guardias médicas generales tras conflictos afectivos, requiriendo un abordaje que evite la sobremedicalización innecesaria."
            },
            {
                "domain": "Red Social Ampliada",
                "pct_label": "Prevalencia observada: ~72%",
                "scientific_basis": "Sociometría en trastornos del Cluster B (Trull et al., 2010): el 72% experimenta rotación frecuente de amistades íntimas por demandas afectivas absorbentes.",
                "color": "#fb923c",
                "clinical_correlate": "Idealización acelerada de vínculos recientes que luego se distancian ante el desgaste que provocan las demandas afectivas continuas."
            },
            {
                "domain": "Autoestima & Dependencia Externa",
                "pct_label": "Prevalencia observada: ~80%",
                "scientific_basis": "Medición de contingencia de autoestima (Crocker & Park, 2004): el 80% de los casos puntúa en dependencia crítica del halago y la mirada externa.",
                "color": "#06b6d4",
                "clinical_correlate": "Sensación de desvanecimiento o angustia de vacío cuando no se cuenta con la mirada atenta o la aprobación explícita de los demás."
            },
            {
                "domain": "Desempeño Laboral Sistemático",
                "pct_label": "Prevalencia observada: ~50%",
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

# --- Panel Superior de Evidencia en Neuroimagen (Con siglas desarrolladas y analogías) ---
bm = current_data["biomarkers"]
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="evidence-panel">
        <div class="evidence-header">{bm['dti']['header']}</div>
        <div class="evidence-title">{bm['dti']['title']}</div>
        <div class="evidence-body"><b>{bm['dti']['status']}</b><br><i>{bm['dti']['analogy']}</i><br>{bm['dti']['summary']}</div>
        <div class="evidence-ref">{bm['dti']['ref']}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="evidence-panel">
        <div class="evidence-header">{bm['fmri_amygdala']['header']}</div>
        <div class="evidence-title">{bm['fmri_amygdala']['title']}</div>
        <div class="evidence-body"><b>{bm['fmri_amygdala']['status']}</b><br><i>{bm['fmri_amygdala']['analogy']}</i><br>{bm['fmri_amygdala']['summary']}</div>
        <div class="evidence-ref">{bm['fmri_amygdala']['ref']}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="evidence-panel">
        <div class="evidence-header">{bm['fmri_pain']['header']}</div>
        <div class="evidence-title">{bm['fmri_pain']['title']}</div>
        <div class="evidence-body"><b>{bm['fmri_pain']['status']}</b><br><i>{bm['fmri_pain']['analogy']}</i><br>{bm['fmri_pain']['summary']}</div>
        <div class="evidence-ref">{bm['fmri_pain']['ref']}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="evidence-panel">
        <div class="evidence-header">{bm['ratio']['header']}</div>
        <div class="evidence-title">{bm['ratio']['title']}</div>
        <div class="evidence-body"><b>{bm['ratio']['status']}</b><br><i>{bm['ratio']['analogy']}</i><br>{bm['ratio']['summary']}</div>
        <div class="evidence-ref">{bm['ratio']['ref']}</div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------------------
# Motor WebGL Three.js con Rótulos Visibles, Malla Bi-Hemisférica y Control Total
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
      padding: 12px 14px; color: #f1f5f9; max-width: 320px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.75); pointer-events: none;
    }}
    .hud-title {{ font-weight: 700; color: #38bdf8; font-size: 0.90rem; margin-bottom: 4px; font-family: monospace; }}
    .hud-desc {{ color: #94a3b8; font-size: 0.75rem; line-height: 1.4; }}
    
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
      <div id="hud-head" class="hud-title">Conectoma 3D Interactivo</div>
      <div id="hud-body" class="hud-desc">Arrastra libremente con el ratón para rotar el encéfalo en 360° o usa la rueda para zoom.<br><br><b>Haz clic en cualquier estructura rotulada</b> para escuchar su análisis clínico, analogías y citas.</div>
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
        speakText("Motor de síntesis vocal activado. Selecciona cualquier estructura o dominio funcional para escuchar su explicación clínica con analogías y citas.");
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

    function createTextSprite(text, color) {{
      const canvasText = document.createElement('canvas');
      const ctx = canvasText.getContext('2d');
      canvasText.width = 512;
      canvasText.height = 128;

      ctx.fillStyle = "rgba(11, 19, 41, 0.80)";
      ctx.roundRect ? ctx.roundRect(10, 10, 492, 108, 16) : ctx.fillRect(10, 10, 492, 108);
      ctx.fill();

      ctx.lineWidth = 4;
      ctx.strokeStyle = color || "#38bdf8";
      ctx.stroke();

      ctx.font = "bold 42px -apple-system, sans-serif";
      ctx.fillStyle = "#f8fafc";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(text, 256, 64);

      const texture = new THREE.CanvasTexture(canvasText);
      const spriteMaterial = new THREE.SpriteMaterial({{ map: texture, transparent: true, depthTest: false }});
      const sprite = new THREE.Sprite(spriteMaterial);
      sprite.scale.set(3.0, 0.75, 1.0);
      return sprite;
    }}

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
          desc: "<b>Estado:</b> " + n.status + "<br><b>Analogía:</b> " + n.analogy + "<br><b>Ejemplo:</b> " + n.example,
          voice: n.voice,
          hz: n.hz
        }};
        modelGroup.add(mesh);
        clickableObjects.push(mesh);
        pulsingNodes.push(mesh);

        const shortName = n.name.split(" ")[0] + (n.name.includes("vmPFC") ? " vmPFC" : (n.name.includes("dACC") ? " dACC" : ""));
        const lbl = createTextSprite(shortName, n.color);
        lbl.position.set(n.coords[0], n.coords[1] + 0.60, n.coords[2]);
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
          desc: "<b>Analogía:</b> " + t.analogy,
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
          desc: "<b>Severidad observada:</b> " + e.pct_label + "<br><b>Fundamento:</b> " + e.scientific_basis + "<br><b>Patrón:</b> " + e.clinical_correlate,
          voice: e.domain + ". " + e.pct_label + ". " + e.clinical_correlate
        }};
        modelGroup.add(mesh);
        clickableObjects.push(mesh);

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
# Panel de Neuroimagen Comparativa (Sujeto Control Sano vs. Cuadro Clínico)
# -------------------------------------------------------------------------
st.markdown("---")
st.subheader("🔬 Neuroimagen Comparativa: Control Sano vs. Cuadro Clínico")
st.caption("Inspección de cortes anatómicos reales con mapa de calor hemodinámico (fMRI BOLD) estandarizado")

selected_node_name = st.selectbox(
    "Seleccionar estructura para desplegar el corte de resonancia comparativa:",
    [n["name"] for n in current_data["nodes"]]
)

active_node = next(n for n in current_data["nodes"] if n["name"] == selected_node_name)

comp_col1, comp_col2 = st.columns(2)

with comp_col1:
    st.markdown(f"""
    <div class="compare-card" style="border-left: 4px solid #10b981;">
        <h4 style="color: #10b981; margin: 0 0 6px 0;">🟢 Sujeto Control Sano</h4>
        <div style="font-size: 0.78rem; color: #94a3b8; margin-bottom: 6px;"><b>Plano de Corte:</b> {active_node['plane']}</div>
        <p style="font-size: 0.82rem; color: #cbd5e1; line-height: 1.4;"><b>Patrón de Activación Fisiológico:</b><br>{active_node['healthy_scan']}</p>
        <div style="font-size: 0.74rem; color: #64748b; border-top: 1px solid #1e293b; padding-top: 6px;">
            El balance inhibitorio frontolímbico se mantiene en homeostasis ante estímulos neutros o frustraciones cotidianas menores.
        </div>
    </div>
    """, unsafe_allow_html=True)

with comp_col2:
    st.markdown(f"""
    <div class="compare-card" style="border-left: 4px solid {active_node['color']};">
        <h4 style="color: {active_node['color']}; margin: 0 0 6px 0;">🔴 Paciente: {selected_disorder.split('(')[0]}</h4>
        <div style="font-size: 0.78rem; color: #94a3b8; margin-bottom: 6px;"><b>Plano de Corte:</b> {active_node['plane']}</div>
        <p style="font-size: 0.82rem; color: #cbd5e1; line-height: 1.4;"><b>Patrón de Activación Patológico:</b><br>{active_node['patient_scan']}</p>
        <div style="font-size: 0.74rem; color: #f59e0b; border-top: 1px solid #1e293b; padding-top: 6px;">
            <b>Analogía clínica:</b> {active_node['analogy']}
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown(f"""
<div style="background: #0b1329; border: 1px solid #1e293b; padding: 12px 16px; border-radius: 6px; font-size: 0.80rem; color: #cbd5e1; margin-top: -4px;">
    <b>Ejemplo en situación de la vida real:</b> {active_node['example']}
</div>
""", unsafe_allow_html=True)

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
            <div style="font-size: 0.86rem; font-weight: 800; color: {item['color']}; margin: 6px 0;">{item['pct_label']}</div>
            <div style="font-size: 0.72rem; color: #cbd5e1; line-height: 1.35; margin-bottom: 8px;"><b>Patrón conductual:</b><br>{item['clinical_correlate']}</div>
            <div style="font-size: 0.68rem; color: #64748b; border-top: 1px solid #1e293b; padding-top: 6px; font-style: italic;"><b>Base científica:</b><br>{item['scientific_basis']}</div>
        </div>
        """, unsafe_allow_html=True)
