import streamlit as st
import streamlit.components.v1 as components
import json
import os

st.set_page_config(
    page_title="Atlas Neurobiológico & Nosológico del Cluster B",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estética quirúrgica dark mode de alta precisión
st.markdown("""
<style>
    .stApp { background-color: #020617; color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    h1, h2, h3, h4 { color: #f8fafc; font-weight: 700; letter-spacing: -0.02em; }
    
    .evidence-panel {
        background: #0b1329; border: 1px solid #1e293b; border-left: 3px solid #38bdf8;
        padding: 12px 14px; border-radius: 8px; margin-bottom: 8px; min-height: 160px;
    }
    .evidence-header { font-size: 0.68rem; text-transform: uppercase; color: #94a3b8; font-weight: 700; letter-spacing: 0.06em; }
    .evidence-title { font-size: 1.02rem; font-weight: 800; color: #38bdf8; font-family: ui-monospace, Menlo, monospace; margin: 2px 0; }
    .evidence-body { font-size: 0.75rem; color: #cbd5e1; line-height: 1.4; margin-top: 4px; }
    .evidence-ref { font-size: 0.68rem; color: #64748b; font-style: italic; margin-top: 4px; }
    
    .clinical-case-box {
        background: #080d1a; border: 1px solid #1e293b; border-left: 4px solid #ef4444;
        padding: 16px 20px; border-radius: 8px; margin-top: 10px; margin-bottom: 15px;
    }
    .disclaimer-box {
        background: rgba(15, 23, 42, 0.7); border: 1px solid #334155; border-radius: 6px;
        padding: 10px 14px; font-size: 0.76rem; color: #94a3b8; margin-bottom: 12px; line-height: 1.35;
    }
    .rule-badge {
        display: inline-block; background: #0284c7; color: #ffffff; font-weight: 700;
        font-size: 0.76rem; padding: 4px 10px; border-radius: 12px; margin-bottom: 10px;
    }
    .therapy-card {
        background: #0b1329; border: 1px solid #1e293b; border-radius: 8px;
        padding: 14px 18px; margin-bottom: 12px; height: 100%;
    }
    .pearl-box {
        background: #0f172a; border: 1px solid #334155; border-left: 4px solid #f59e0b;
        padding: 14px 18px; border-radius: 8px; margin-top: 12px; margin-bottom: 12px;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# Base de Datos Neurocientífica, Pedagógica y de Tratamiento Integral
# -------------------------------------------------------------------------
CLINICAL_REGISTRY = {
    "Trastorno Límite de la Personalidad (TLP)": {
        "short_key": "TLP",
        "circuit_name": "Falla del Freno Frontal & Alarma Desregulada del Dolor Social",
        "color_accent": "#ef4444",
        "definition": "Patrón persistente de inestabilidad en las relaciones interpersonales, la autoimagen y los afectos, con notable impulsividad, que comienza en las primeras etapas de la edad adulta y se presenta en diversos contextos.",
        "dsm5_requirement": "Para el diagnóstico se exige cumplir como mínimo 5 de los siguientes 9 criterios:",
        "textbooks": [
            "American Psychiatric Association. DSM-5-TR. 2022.",
            "World Health Organization. ICD-11. 2024.",
            "Linehan MM. Cognitive-Behavioral Treatment of BPD. 1993.",
            "Bateman A, Fonagy P. Mentalization-Based Treatment for Personality Disorders. 2016.",
            "Zanarini MC, et al. Am J Psychiatry. 2010;167(6):663-667."
        ],
        "dsm5_criteria": [
            "Esfuerzos desesperados para evitar el desamparo o abandono real o imaginado.",
            "Patrón de relaciones interpersonales inestables e intensas, alternando entre extremos de idealización y devaluación (escisión).",
            "Alteración marcada y persistente de la identidad: inestabilidad de la autoimagen o del sentido del self.",
            "Impulsividad en al menos dos áreas potencialmente dañinas (ej. gastos, abuso de sustancias, atracones, conducción temeraria).",
            "Comportamientos, intentos o amenazas recurrentes de suicidio, o conductas autolesivas no suicidas (CANS).",
            "Inestabilidad afectiva debida a una marcada reactividad del estado de ánimo (disforia, irritabilidad o ansiedad episódica).",
            "Sensación crónica de vacío interior.",
            "Enfado inapropiado e intenso, o dificultad para controlar la ira.",
            "Ideación paranoide transitoria relacionada con el estrés o síntomas disociativos graves."
        ],
        "icd11_framework": "La CIE-11 clasifica el trastorno por grado de severidad (Leve, Moderado, Grave) y aplica el calificador específico de 'Patrón Límite', caracterizado por desregulación afectiva extrema, relaciones inestables e impulsividad autolesiva.",
        "biomarkers": {
            "dti": {
                "header": "Resonancia por Tensor de Difusión (DTI)",
                "title": "Fascículo Uncinado Bilateral",
                "status": "Anisotropía Fraccional Disminuida (FA < 0.20)",
                "analogy": "Un cable de freno deshilachado: la orden reguladora emitida por la corteza frontal llega tarde a la amígdala.",
                "summary": "Pérdida de integridad microestructural en sustancia blanca frontolímbica. La vía eferente orbitofrontal presenta retraso en modular la respuesta afectiva visceral.",
                "ref": "Schmahl et al. (2014, Biological Psychiatry) | New et al. (2009, NeuroImage)"
            },
            "fmri_amygdala": {
                "header": "Resonancia Funcional / BOLD (Nivel de Oxigenación)",
                "title": "Complejo Amigdalino Basolateral",
                "status": "Hiperreactividad Fásica con Retardo en Extinción",
                "analogy": "Un sensor de humo descalibrado que se activa con el simple vapor de una taza de café.",
                "summary": "Respuesta desproporcionada ante caras neutras o pausas interpersonales breves, codificadas por la amígdala como amenaza inminente de separación o rechazo.",
                "ref": "Ruocco et al. (2013, Am J Psychiatry meta-análisis de 28 estudios)"
            },
            "fmri_pain": {
                "header": "Red de Prominencia (Salience Network)",
                "title": "Cíngulo Dorsal (dACC) e Ínsula Anterior",
                "status": "Activación Nociceptiva ante la Exclusión",
                "analogy": "Para el cerebro, el distanciamiento afectivo genera una señal idéntica a una quemadura física real.",
                "summary": "En paradigmas experimentales de exclusión (Cyberball), la distancia vincular recluta los mismos circuitos nociceptivos que el dolor somático agudo.",
                "ref": "Eisenberger & Lieberman (2004, Science) | Domsalla et al. (2014)"
            },
            "ratio": {
                "header": "Acoplamiento Frontolímbico",
                "title": "Corteza Prefrontal Ventromedial (vmPFC)",
                "status": "Desacoplamiento Inhibitorio Top-Down",
                "analogy": "Un pedal de freno que pierde eficacia hidráulica en plena bajada empinada.",
                "summary": "Dificultad de la corteza prefrontal ventromedial para reclutar recursos reflexivos (mentalización) durante picos de desregulación autonómica elevada.",
                "ref": "Cullen et al. (2011) | Coccaro et al. (2007)"
            }
        },
        "therapies": [
            {
                "name": "DBT (Terapia Dialéctico-Conductual)",
                "author": "Linehan MM (1991, 1993)",
                "focus": "Equilibrio dialéctico entre aceptación y cambio.",
                "components": "Entrenamiento en 4 módulos: Mindfulness, Tolerancia al malestar, Regulación emocional y Efectividad interpersonal.",
                "target": "Reducción de conductas autolesivas (CANS), estabilización en crisis y prevención de IAE."
            },
            {
                "name": "MBT (Terapia Basada en la Mentalización)",
                "author": "Bateman A, Fonagy P (2016)",
                "focus": "Fortalecer la capacidad de percibir estados mentales propios y ajenos.",
                "components": "Restaurar la mentalización bajo estrés emocional intenso en el contexto del apego.",
                "target": "Mejorar la modulación del afecto, reducir interpretaciones paranoides y estabilizar el sentido de identidad."
            },
            {
                "name": "TFP (Psicoterapia Focalizada en la Transferencia)",
                "author": "Kernberg OF, Clarkin JF (2006)",
                "focus": "Exploración de la transferencia y de las representaciones escindidas.",
                "components": "Análisis en el 'aquí y ahora' de la relación paciente-terapeuta.",
                "target": "Integración de representaciones polarizadas (bueno/malo) hacia una identidad consolidada."
            },
            {
                "name": "Terapia de Esquemas",
                "author": "Young J, Arntz A (2009)",
                "focus": "Modificación de esquemas desadaptativos tempranos.",
                "components": "Técnicas experienciales (re-atribución imaginativa), cognitivas y conductuales.",
                "target": "Promover modos de adulto saludable y reparar necesidades emocionales no cubiertas en la infancia."
            }
        ],
        "psychopharm_pearl": "No existe ningún fármaco aprobado por la FDA o agencias regulatorias para el tratamiento global del TLP. El uso de psicofármacos es sintomático y complementario (focalizado en comorbilidades como depresión mayor o impulsividad aguda severa), requiriendo reevaluación periódica de su necesidad (Guías NICE CG78).",
        "longitudinal_data": {
            "title": "Evolución Longitudinal a 10 Años (Cohorte Zanarini et al., 2010)",
            "remission_2yr": "86% alcanza remisión sintomática sostenida por más de 2 años.",
            "remission_4yr": "93% alcanza remisión sintomática por más de 4 años.",
            "functional_recovery": "Solo el 50% logra recuperación funcional completa (autonomía laboral/social plena).",
            "key_takeaway": "La remisión de los síntomas agudos (como las autolesiones) no equivale automáticamente a la recuperación de la autonomía social o vocacional. Ambas esferas requieren abordajes diferenciados."
        },
        "nodes": [
            {
                "id": "amg",
                "name": "Amígdala Basolateral",
                "btn_label": "Amígdala",
                "region_loc": "Polo Medial del Lóbulo Temporal Profundo (adyacente al asta temporal)",
                "plane": "Corte Coronal Anterior",
                "coords": [1.9, -0.6, -1.3],
                "color": "#ef4444",
                "rad": 0.40,
                "hz": 8.0,
                "status": "HIPERTRÓFICA FÁSICA",
                "analogy": "Sensor de alarma descalibrado que suena ante el mínimo estímulo.",
                "example": "Una demora de 30 minutos en un mensaje de texto detona taquicardia y pánico de abandono inminente.",
                "healthy_desc": "Respuesta fásica contenida frente a estímulos aversivos; rápida habituación y retorno a la línea de base autonómica sin desbordamiento.",
                "patient_desc": "Paroxismo hemodinámico BOLD masivo y prolongado ante rostros neutros o ambigüedad vincular; retardo patológico en la extinción del miedo.",
                "voice": "Amígdala basolateral derecha. Imaginemos una alarma de humo ultrasensible que se activa no solo ante el fuego, sino ante el simple vapor de una taza de café. En el trastorno límite, un mensaje sin responder durante media hora es interpretado como un riesgo vital de abandono. New y colaboradores documentaron en NeuroImage que este núcleo presenta un retardo significativo en extinguir la señal de miedo."
            },
            {
                "id": "vmpfc",
                "name": "Corteza Prefrontal Ventromedial (vmPFC)",
                "btn_label": "vmPFC",
                "region_loc": "Suelo Anterior Basal del Lóbulo Frontal (Áreas 10/11 de Brodmann)",
                "plane": "Corte Sagital Medial",
                "coords": [0.0, 3.8, -0.8],
                "color": "#38bdf8",
                "rad": 0.38,
                "hz": 1.0,
                "status": "COLAPSO INHIBITORIO",
                "analogy": "Freno hidráulico que pierde presión durante una emergencia.",
                "example": "El paciente comprende que romper objetos empeorará todo, pero no logra detener el impulso motor en el momento crítico.",
                "healthy_desc": "Control inhibitorio top-down sostenido sobre las eferencias límbicas, permitiendo la reevaluación reflexiva y la modulación del afecto.",
                "patient_desc": "Desacoplamiento funcional severo; caída de la señal BOLD durante la crisis afectiva que bloquea la capacidad de mentalización.",
                "voice": "Corteza prefrontal ventromedial. Actúa como el pedal de freno del cerebro emocional. En este cuadro, el freno pierde eficacia hidráulica durante la crisis. Aunque la persona comprenda racionalmente que autolesionarse empeorará la situación, la corteza no logra ejercer la fuerza sináptica necesaria para detener la inercia del impulso."
            },
            {
                "id": "dacc",
                "name": "Cíngulo Anterior Dorsal (dACC)",
                "btn_label": "dACC",
                "region_loc": "Circunvolución del Cíngulo sobre el Cuerpo Calloso (Áreas 24/32)",
                "plane": "Corte Sagital Medial",
                "coords": [0.0, 1.8, 1.8],
                "color": "#f43f5e",
                "rad": 0.42,
                "hz": 7.2,
                "status": "DOLOR SOCIAL AGUDO",
                "analogy": "Procesador que traduce el desapego en dolor físico visceral.",
                "example": "Una discusión se vive como una quemadura física; las conductas autolesivas buscan mitigar esa angustia psíquica.",
                "healthy_desc": "Monitorización de conflicto cognitivo sin reclutamiento masivo de la matriz somatosensorial de dolor físico.",
                "patient_desc": "Coactivación paroxística ante la exclusión interpersonal; traduce la incertidumbre vincular en una señal idéntica a una agresión tisular aguda.",
                "voice": "Córtex cingulado anterior dorsal. Es el nodo central del dolor social. Naomi Eisenberger demostró en la revista Science que el cerebro procesa la exclusión en los mismos circuitos que una quemadura somática. Ante la vivencia de rechazo, este núcleo se activa con tal intensidad que la autolesión suele buscar, de manera disfuncional, atenuar un dolor psíquico que resulta intolerable."
            },
            {
                "id": "insula",
                "name": "Ínsula Anterior Agranular",
                "btn_label": "Ínsula",
                "region_loc": "Profundidad del Surco Lateral (Cisura de Silvio)",
                "plane": "Corte Axial Medio",
                "coords": [2.8, 0.7, -0.2],
                "color": "#e11d48",
                "rad": 0.36,
                "hz": 6.5,
                "status": "HIPEREXCITACIÓN INTEROCEPTIVA",
                "analogy": "El altavoz que proyecta el vacío interno como dolor somático.",
                "example": "Sensación constante de un vacío físico en el pecho que se intenta calmar con conductas impulsivas.",
                "healthy_desc": "Integración homeostática normal de las señales autonómicas viscerales del organismo.",
                "patient_desc": "Amplificación somatosensorial aversiva continua; correlato fisiopatológico de la disforia paroxística y el vacío en el pecho.",
                "voice": "Ínsula anterior agranular. Traduce el malestar afectivo en sensaciones corporales. Constituye el sustrato de esa vivencia de vacío interior o dolor en el pecho que se describe con frecuencia en la clínica y que precipita intentos de alivio inmediato."
            }
        ],
        "tracts": [
            {
                "from": [1.9, -0.6, -1.3], "to": [0.0, 3.8, -0.8], "ctrl": [2.6, 1.5, -1.6],
                "name": "Fascículo Uncinado Derecho",
                "status": "broken",
                "desc": "Tracto axonómico desmielinizado; pérdida de anisotropía fraccional (DTI).",
                "voice": "Fascículo uncinado derecho. Es la vía de sustancia blanca que conecta la corteza frontal con la amígdala. En el trastorno límite, este canal presenta una desorganización microestructural que retrasa la llegada de la señal reguladora."
            }
        ],
        "case_vignette": {
            "title": "Viñeta Clínica Ilustrativa: Descompensación por Distanciamiento Percibido",
            "narrative": "Paciente de 24 años consulta en guardia tras ingerir una dosis excesiva de ansiolíticos y presentar lesiones cortantes superficiales en el antebrazo. El hecho precipitante fue una demora de tres horas de su pareja en responder un mensaje luego de una discusión menor. Durante la entrevista refiere: 'Sentí un frío quemante en el pecho, como si dejara de existir; necesitaba que el dolor parara de inmediato'.",
            "mechanistic_reading": "La percepción de distanciamiento activa el dACC y la ínsula anterior simulando una agresión tisular real (Eisenberger, 2004). El fascículo uncinado desorganizado (Schmahl, 2014) no transmite a tiempo la modulación del vmPFC, impidiendo contextualizar la demora y favoreciendo la conducta impulsiva como intento de regulación afectiva extrema."
        },
        "whodas_matrix": [
            {
                "domain": "Esfera Conyugal & Apego",
                "short_label": "Apego",
                "pct_label": "Aproximadamente un 96 por ciento de prevalencia observada",
                "scientific_basis": "Cohorte CLPS (Collaborative Longitudinal Personality Disorders Study, Gunderson et al., 2011; Zanarini et al., 2012): el 96% de los pacientes evaluados presenta antecedentes de inestabilidad conyugal severa o rupturas conflictivas recurrentes.",
                "color": "#ef4444",
                "clinical_correlate": "Mecanismos de escisión o splitting. La figura de apego oscila entre la idealización y el rechazo extremo ante la mínima sospecha de abandono."
            },
            {
                "domain": "Servicio de Guardia & Urgencias",
                "short_label": "Urgencias",
                "pct_label": "Aproximadamente un 92 por ciento de frecuentación en crisis",
                "scientific_basis": "Zanarini et al. (2008, Am J Psychiatry, seguimiento a 10 años): el 92% de los pacientes diagnosticados requirió al menos una admisión de urgencia por conductas autolesivas o crisis afectivas.",
                "color": "#ef4444",
                "clinical_correlate": "Utilización reiterada de servicios de guardia motivada por conductas autolesivas no suicidas o desregulaciones afectivas agudas."
            },
            {
                "domain": "Cohesión del Self & Identidad",
                "short_label": "Identidad",
                "pct_label": "Aproximadamente un 94 por ciento de compromiso identitario",
                "scientific_basis": "Criterio de Difusión de Identidad (DSM-5 Sección III / Kernberg, 2006): el 94% de los casos reporta sensación crónica de vacío, incertidumbre vocacional y labilidad en la autoimagen.",
                "color": "#f43f5e",
                "clinical_correlate": "Vivencia de vacío interior; adaptación maleable de valores o metas personales a la figura cercana para evitar la soledad."
            },
            {
                "domain": "Red Familiar Primaria",
                "short_label": "Familia",
                "pct_label": "Aproximadamente un 88 por ciento de sobrecarga en cuidadores",
                "scientific_basis": "Estudios de sobrecarga familiar (Bailey & Grenyer, 2013; Skodol et al., 2005): el 88% de las familias de origen puntúa en rangos de sobrecarga y desgaste emocional severo.",
                "color": "#fb923c",
                "clinical_correlate": "Convivencia marcada por hiperalerta y desgaste afectivo en cuidadores primarios frente a la imprevisibilidad de las crisis."
            },
            {
                "domain": "Funcionamiento Laboral",
                "short_label": "Laboral",
                "pct_label": "Aproximadamente un 72 por ciento de discontinuidad",
                "scientific_basis": "Estudio CLPS (Skodol et al., 2002): el 72% de la muestra evidencia interrupciones prolongadas de empleo o estudios por desregulación interpersonal.",
                "color": "#eab308",
                "clinical_correlate": "Dificultad para sostener proyectos sistemáticos a mediano plazo por fricciones interpersonales con compañeros o superiores."
            }
        ]
    },
    "Trastorno Antisocial de la Personalidad (TASP)": {
        "short_key": "TASP",
        "circuit_name": "Ablación Funcional Frontolímbica & Falla de Aversión Moral",
        "color_accent": "#f59e0b",
        "definition": "Patrón dominante de inatención y vulneración de los derechos de los demás, que se produce desde los 15 años de edad (con antecedentes de trastorno de conducta antes de dicha edad), manifestado por incumplimiento de normas sociales, engaño, impulsividad e irritabilidad.",
        "dsm5_requirement": "Para el diagnóstico se exige tener al menos 18 años, evidencia de trastorno de la conducta antes de los 15 años y cumplir al menos 3 de los 7 criterios siguientes:",
        "textbooks": [
            "American Psychiatric Association. DSM-5-TR. 2022.",
            "Hare, R. D.: Manual for the Revised Psychopathy Checklist (PCL-R, Multi-Health Systems)",
            "Gibbon S, et al. Cochrane Database of Systematic Reviews. 2020;9:CD007668.",
            "Blair, J. et al.: The Psychopath: Emotion and the Brain (Blackwell Publishing)"
        ],
        "dsm5_criteria": [
            "Incumplimiento de las normas sociales respecto a los comportamientos legales (detenciones reiteradas).",
            "Engaño manifiesto por mentiras repetidas, uso de alias o estafa para provecho o placer personal.",
            "Impulsividad o fracaso para planear con antelación.",
            "Irritabilidad y agresividad, manifestada por peleas o agresiones físicas repetidas.",
            "Desatención imprudente de la seguridad propia o de los demás.",
            "Irresponsabilidad constante, manifestada por la incapacidad de mantener un trabajo o liquidar deudas.",
            "Ausencia de remordimiento, manifestada con indiferencia o racionalización tras haber herido o robado a alguien."
        ],
        "icd11_framework": "La CIE-11 encuadra las manifestaciones dentro del dominio de 'Disocialidad' (desprecio por las normas y los derechos ajenos, hostilidad, frialdad e instrumentalización interpersonal sin culpa).",
        "biomarkers": {
            "dti": {
                "header": "Resonancia por Tensor de Difusión (DTI)",
                "title": "Fascículo Uncinado Bilateral",
                "status": "Ablación Microestructural Mayor (FA < 0.10)",
                "analogy": "Un teléfono con la línea cortada entre el centro del miedo y el juzgado de la conciencia moral.",
                "summary": "Interrupción de la vía de sustancia blanca que conecta la amígdala con la corteza orbitofrontal. Desconexión física entre el procesamiento aversivo y la deliberación ética.",
                "ref": "Craig et al. (2009, Mol Psychiatry) | Motzkin et al. (2011, J Neurosci)"
            },
            "fmri_amygdala": {
                "header": "Resonancia Funcional / BOLD (Nivel de Oxigenación)",
                "title": "Complejo Amigdalino Basolateral",
                "status": "Hipoactividad e Inmunidad al Condicionamiento",
                "analogy": "Un detector de humo sin batería: aunque haya fuego real, no emite ningún sonido.",
                "summary": "Ausencia de respuesta autonómica y hemodinámica ante expresiones de terror o angustia ajena. Refractariedad al aprendizaje aversivo por castigo.",
                "ref": "Blair et al. (2004, NeuroImage) | Birbaumer et al. (2005)"
            },
            "fmri_pain": {
                "header": "Red de Resonancia Social (Empatía)",
                "title": "Ínsula Anterior (Empatía Afectiva)",
                "status": "Anestesia Somatosensorial Vicaria",
                "analogy": "Mirar a alguien sufrir a través de un vidrio blindado sin experimentar la menor conmoción somática.",
                "summary": "Falla en la activación insular frente al sufrimiento ajeno. Conservación de la Teoría de la Mente cognitiva (capacidad de manipulación) con atrofia de la empatía emocional.",
                "ref": "Glenn & Raine (2014) | Decety et al. (2013)"
            },
            "ratio": {
                "header": "Acoplamiento Frontolímbico",
                "title": "Bucle Córtico-Estriatal Predatorio",
                "status": "Hipersensibilidad a la Recompensa Inmediata",
                "analogy": "Un motor voraz sin volante que avanza arrasando con todo a su paso.",
                "summary": "Hiperreactividad dopaminérgica en el núcleo accumbens orientada a ganancias instrumentales, sin modulación inhibitoria frontal frente al daño colateral.",
                "ref": "Buckholtz et al. (2010, Nature Neurosci)"
            }
        },
        "therapies": [
            {
                "name": "Revisión Cochrane (Gibbon et al., 2020)",
                "author": "Cochrane Database of Systematic Reviews",
                "focus": "Evaluación de intervenciones psicológicas en el comportamiento antisocial.",
                "components": "Análisis de ensayos clínicos controlados sobre programas cognitivo-conductuales e institucionales.",
                "target": "Certeza de evidencia baja a muy baja: ninguna intervención ha demostrado un cambio generalizado en la estructura de personalidad antisocial. El foco clínico se traslada al manejo de contingencias y gestión de riesgo."
            },
            {
                "name": "Gestión Dinámica de Riesgo de Violencia",
                "author": "Guías NICE CG77",
                "focus": "Diferenciación entre factores estáticos (no modificables) y factores dinámicos.",
                "components": "Intervención intensiva sobre factores dinámicos: tratamiento del consumo activo de sustancias (TCS), impulsividad aguda y acceso a armas.",
                "target": "Mitigación del daño y reducción de reincidencia mediante supervisión estructurada multidisciplinaria."
            }
        ],
        "psychopharm_pearl": "El diagnóstico de TASP por sí mismo no constituye una indicación farmacológica. La prescripción debe restringirse al tratamiento de comorbilidades activas (TDAH, trastornos por uso de sustancias o descontrol impulsivo grave), advirtiendo el alto riesgo de desvío, abuso o intoxicación voluntaria.",
        "nodes": [
            {
                "id": "amg",
                "name": "Amígdala (Hipoactiva)",
                "btn_label": "Amígdala",
                "region_loc": "Polo Medial del Lóbulo Temporal Profundo (adyacente al asta temporal)",
                "plane": "Corte Coronal Anterior",
                "coords": [1.9, -0.6, -1.3],
                "color": "#1e293b",
                "rad": 0.30,
                "hz": 0.4,
                "status": "ATROFIA FUNCIONAL",
                "analogy": "Detector de humo al que se le quitó la batería: no suena ante el peligro.",
                "example": "El sujeto comete una estafa grave manteniendo 55 latidos por minuto, sin temblor ni sudoración.",
                "healthy_desc": "Reactividad fásica conservada ante señales de castigo o rostros temerosos.",
                "patient_desc": "Hipoactivación BOLD crítica ante estímulos aversivos; insensibilidad al miedo y a la sanción.",
                "voice": "Amígdala hipoactiva. Imaginemos un detector de humo sin batería. Aunque haya fuego real alrededor, no se activa. Mientras una persona promedio experimenta taquicardia ante la transgresión o el sufrimiento ajeno, aquí predomina la estabilidad autonómica. Craig y Blair documentaron en NeuroImage esta marcada refractariedad al castigo."
            },
            {
                "id": "vmpfc",
                "name": "vmPFC (Polo Moral Desconectado)",
                "btn_label": "vmPFC",
                "region_loc": "Suelo Anterior Basal del Lóbulo Frontal (Áreas 10/11 de Brodmann)",
                "plane": "Corte Sagital Medial",
                "coords": [0.0, 3.8, -0.8],
                "color": "#334155",
                "rad": 0.32,
                "hz": 0.5,
                "status": "HIPOCONECTADA",
                "analogy": "Calculadora desprovista de escrúpulos que no siente remordimientos.",
                "example": "Comprende conceptualmente que defraudar a sus padres está penado por la ley, pero no le produce culpa afectiva en el cuerpo.",
                "healthy_desc": "Integración del juicio ético con el freno vicario de culpa somatizada.",
                "patient_desc": "Procesamiento moral instrumental disociado; cálculo utilitario sin resonancia afectiva.",
                "voice": "Corteza prefrontal ventromedial. Funciona de manera calculadora y analítica. Comprende las normas jurídicas a nivel conceptual, pero esa información carece de resonancia afectiva. Dañar a un tercero se procesa como un costo de transacción admisible para lograr un objetivo."
            },
            {
                "id": "accumbens",
                "name": "Núcleo Accumbens (Estriado)",
                "btn_label": "Accumbens",
                "region_loc": "Suelo del Estriado Ventral Anterior",
                "plane": "Corte Coronal Basal",
                "coords": [1.0, 1.1, -0.7],
                "color": "#eab308",
                "rad": 0.44,
                "hz": 7.5,
                "status": "HIPERACTIVIDAD PREDATORIA",
                "analogy": "Acelerador voraz que busca dinero o poder sin reparar en el daño.",
                "example": "Frente a la posibilidad de un beneficio personal rápido, el impulso motor descarta cualquier noción de riesgo legal.",
                "healthy_desc": "Búsqueda de incentivo regulada por el cálculo de costos y consecuencias sociales.",
                "patient_desc": "Hiperactivación dopaminérgica inmediata desprovista de inhibición frontal punitiva.",
                "voice": "Núcleo accumbens estriatal. Es el centro de búsqueda de recompensa. Frente a la oportunidad de obtener un beneficio inmediato a costa de otros, este núcleo se sobreactiva sin que intervenga el freno inhibitorio frontal."
            },
            {
                "id": "insula",
                "name": "Ínsula Anterior (Anestesiada)",
                "btn_label": "Ínsula",
                "region_loc": "Profundidad del Surco Lateral (Cisura de Silvio)",
                "plane": "Corte Axial Medio",
                "coords": [2.8, 0.7, -0.2],
                "color": "#1e293b",
                "rad": 0.26,
                "hz": 0.3,
                "status": "ANESTESIA INTEROCEPTIVA",
                "analogy": "Mirar el sufrimiento de una persona como si fuera una película de ficción.",
                "example": "Presencia el llanto desconsolado de su víctima sin registrar ninguna aversión o compasión interna.",
                "healthy_desc": "Resonancia somatosensorial refleja frente al dolor ajeno (empatía afectiva).",
                "patient_desc": "Inactividad insular ante el llanto ajeno; ausencia de aversión o remordimiento visceral.",
                "voice": "Ínsula anterior agranular anestesiada. Es el asiento de la empatía emocional somatizada. Su hipoactivación explica por qué estas personas pueden presenciar el daño causado sin experimentar malestar gástrico ni remordimiento."
            }
        ],
        "tracts": [
            {
                "from": [1.8, -0.6, -1.3], "to": [0.0, 3.8, -0.8], "ctrl": [2.6, 1.5, -1.6],
                "name": "Fascículo Uncinado",
                "status": "broken",
                "desc": "Interrupción del canal estructural miedo-deliberación moral.",
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
                "short_label": "Judicial",
                "pct_label": "Aproximadamente un 99 por ciento de conflicto legal",
                "scientific_basis": "Meta-análisis penitenciario (Fazel & Danesh, 2002, The Lancet; Hare, 2003 PCL-R): en poblaciones con diagnóstico confirmado de TASP/psicopatía, la tasa de conflicto judicial y reincidencia delictiva roza el 99%.",
                "color": "#ef4444",
                "clinical_correlate": "Reincidencia en delitos patrimoniales, transgresión deliberada de normativas y refractariedad al valor correctivo de las penas."
            },
            {
                "domain": "Vínculos & Instrumentalización",
                "short_label": "Vínculos",
                "pct_label": "Aproximadamente un 96 por ciento de cosificación",
                "scientific_basis": "Estudios de empatía interpersonal (Blair, 2008; Cleckley, 1941): el 96% de los lazos afectivos se estructuran de forma asimétrica, utilitaria o predatoria.",
                "color": "#ef4444",
                "clinical_correlate": "Uso instrumental de parejas o allegados con fines económicos, sexuales o de conveniencia personal, prescindiendo de ellos al cesar su utilidad."
            },
            {
                "domain": "Ámbito Contractual & Financiero",
                "short_label": "Financiero",
                "pct_label": "Aproximadamente un 90 por ciento de irregularidades",
                "scientific_basis": "Estudio epidemiológico NESARC (Grant et al., 2004): el 90% de los sujetos con rasgos antisociales graves registra cesantías por fraude, quiebras o deshonestidad.",
                "color": "#fb923c",
                "clinical_correlate": "Incumplimiento deliberado de compromisos económicos, estafas y falta de lealtad en acuerdos comerciales formales."
            },
            {
                "domain": "Simulación Pericial Forense",
                "short_label": "Peritajes",
                "pct_label": "Aproximadamente un 65 por ciento de simulación",
                "scientific_basis": "Mediciones con SIRS-2 (Structured Interview of Reported Symptoms, Rogers et al., 2011): un 65% de los peritados muestra maniobras activas de simulación sintomática.",
                "color": "#eab308",
                "clinical_correlate": "Uso instrumental del examen psiquiátrico forense para simular cuadros amnésicos o psicóticos y atenuar la imputabilidad penal."
            },
            {
                "domain": "Insight & Conciencia de Enfermedad",
                "short_label": "Insight",
                "pct_label": "Aproximadamente un 10 por ciento de insight",
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
        "definition": "Patrón dominante de grandeza (en la fantasía o en el comportamiento), necesidad de admiración constante y profunda falta de empatía, que comienza en las primeras etapas de la edad adulta y está presente en diversos contextos.",
        "dsm5_requirement": "Para el diagnóstico se exige cumplir como mínimo 5 de los 9 criterios siguientes:",
        "textbooks": [
            "American Psychiatric Association. DSM-5-TR. 2022.",
            "Pincus AL, Lukowitsky MR. Annu Rev Clin Psychol. 2010;6:421-446.",
            "Mohajerin B, Howard R, Pincus AL. Clin Psychol Psychother. 2026;33(2):e70247.",
            "Kernberg, O. F.: Trastornos Graves de la Personalidad (El Manual Moderno)"
        ],
        "dsm5_criteria": [
            "Sentimientos de grandeza y prepotencia (exagera logros y talentos, espera ser reconocido como superior).",
            "Preocupación por fantasías de éxito, poder, brillantez, belleza o amor ideal ilimitados.",
            "Creencia de que es 'especial' y único, y que solo puede ser comprendido por personas o instituciones de alto estatus.",
            "Necesidad excesiva de admiración continua.",
            "Sentimiento de privilegio o derecho a trato favorable especial.",
            "Explotación interpersonal (se aprovecha de los demás para sus propios fines).",
            "Carencia de empatía: renuencia a reconocer o identificarse con los sentimientos y necesidades ajenas.",
            "Frecuente envidia hacia los demás o creencia de que los demás le envidian a él.",
            "Comportamientos o actitudes arrogantes, soberbias o desdeñosas."
        ],
        "icd11_framework": "La CIE-11 sitúa estos rasgos dentro del dominio de 'Disocialidad' (antagonismo, desprecio, búsqueda de dominancia y explotación de otros) con componentes de 'Afectividad Negativa' en su variante vulnerable.",
        "biomarkers": {
            "dti": {
                "header": "Resonancia por Tensor de Difusión (DTI)",
                "title": "Sustancia Blanca Frontomedial",
                "status": "Integridad Preservada con Sesgo de Dominancia",
                "analogy": "Canales de cálculo estratégico intactos, pero aislados de los circuitos de empatía afectiva.",
                "summary": "Vías de mentalización cognitiva intactas. Preservación del cálculo relacional estratégico junto con hipoconectividad hacia redes de empatía emocional.",
                "ref": "Fan et al. (2011, SCAN) | Nenadic et al. (2015)"
            },
            "fmri_amygdala": {
                "header": "Resonancia Funcional / BOLD (Nivel de Oxigenación)",
                "title": "Cíngulo Dorsal / Amígdala",
                "status": "Herida Narcisista y Alarma por Pérdida de Estatus",
                "analogy": "Un radar de prestigio que detecta una ofensa mortal ante el menor cuestionamiento.",
                "summary": "Alarma paroxística en el dACC ante la crítica o el cuestionamiento jerárquico ('herida narcisista'), con reactividad hostil dirigida a neutralizar la descalificación.",
                "ref": "Pincus & Lukowitsky (2010) | Schulze et al. (2013)"
            },
            "fmri_pain": {
                "header": "Red de Resonancia Social (Empatía)",
                "title": "Corteza Insular Anterior",
                "status": "Disociación Empática Afectiva (Fan et al.)",
                "analogy": "Saber exactamente cómo herir verbalmente al otro sin conmoverse por su llanto.",
                "summary": "Reducción de activación insular ante el dolor ajeno. El sujeto comprende conceptualmente el estado mental del otro pero no resuena visceralmente con él.",
                "ref": "Jankowiak-Siuda et al. (2015) | Baskin-Sommers et al."
            },
            "ratio": {
                "header": "Acoplamiento Frontolímbico",
                "title": "Red por Defecto vs. Prominencia",
                "status": "Compensación Grandiosa Frontal",
                "analogy": "Un andamio de oro construido con gran esfuerzo para tapar un piso de barro frágil.",
                "summary": "Gasto metabólico frontal sostenido para apuntalar una narrativa de autosuficiencia y superioridad que neutralice la extrema vulnerabilidad del self.",
                "ref": "Scalabrini et al. (2017, Hum Brain Mapp)"
            }
        },
        "therapies": [
            {
                "name": "Ensayo Clínico Mohajerin et al. (2026)",
                "author": "Clinical Psychology & Psychotherapy (114 pacientes)",
                "focus": "Comparación directa entre Terapia de Esquemas (ST) y Protocolo Unificado (UP).",
                "components": "ST focalizada en modos tempranos desadaptativos vs. UP focalizado en regulación emocional transdiagnóstica de Barlow.",
                "target": "Ambos redujeron significativamente síntomas. ST demostró mayor eficacia modificando patrones interpersonales arraigados, mientras que UP fue superior en regular reactividad emocional aguda ante la crítica."
            }
        ],
        "psychopharm_pearl": "El tratamiento farmacológico no altera la estructura caracterológica de la grandiosidad ni la falta de empatía. Se reserva para comorbilidades afectivas graves, especialmente episodios depresivos mayores tras el colapso de la fachada narcisista.",
        "nodes": [
            {
                "id": "dacc",
                "name": "dACC (Radar de Jerarquía)",
                "btn_label": "dACC",
                "region_loc": "Circunvolución del Cíngulo sobre el Cuerpo Calloso (Áreas 24/32)",
                "plane": "Corte Sagital Medial",
                "coords": [0.0, 1.8, 1.8],
                "color": "#a855f7",
                "rad": 0.42,
                "hz": 7.4,
                "status": "HIPERREACTIVO AL DESPRECIO",
                "analogy": "Sensor de jerarquía en guardia continua ante la falta de elogios.",
                "example": "Si en una reunión no se aprueba de inmediato su propuesta, experimenta una afrenta personal intolerable.",
                "healthy_desc": "Procesamiento de evaluación social equilibrado sin reactividad defensiva desmedida.",
                "patient_desc": "Pico de activación fásica del dACC ('herida narcisista') ante la crítica o falta de pleitesía.",
                "voice": "Cíngulo anterior dorsal. Es un radar de jerarquía social en hipervigilancia continua. Si una opinión suya no es celebrada, este núcleo detecta una ofensa mortal a su estatus, detonando una respuesta de furia fría o venganza calculada."
            },
            {
                "id": "vmpfc",
                "name": "vmPFC (Autoimagen Grandiosa)",
                "btn_label": "vmPFC",
                "region_loc": "Suelo Anterior Basal del Lóbulo Frontal (Áreas 10/11 de Brodmann)",
                "plane": "Corte Sagital Medial",
                "coords": [0.0, 3.8, -0.8],
                "color": "#c084fc",
                "rad": 0.38,
                "hz": 2.8,
                "status": "COMPENSACIÓN GRANDIOSA",
                "analogy": "Un andamio dorado que requiere energía continua para no desplomarse.",
                "example": "Gasta horas rumiando sobre sus éxitos pasados para no sentir la angustia de un fracaso reciente.",
                "healthy_desc": "Autoestima estable que no precisa reafirmación externa obsesiva.",
                "patient_desc": "Hipermetabolismo en la red por defecto medial para sostener la narrativa grandiosa.",
                "voice": "Corteza prefrontal ventromedial. Es como sostener un andamio elevado sobre cimientos frágiles. Se invierte un volumen considerable de recursos cognitivos en reafirmar la superioridad personal precisamente para contener el miedo subyacente a la insignificancia."
            },
            {
                "id": "amg",
                "name": "Amígdala (Rabia Narcisista)",
                "btn_label": "Amígdala",
                "region_loc": "Polo Medial del Lóbulo Temporal Profundo (adyacente al asta temporal)",
                "plane": "Corte Coronal Anterior",
                "coords": [1.8, -0.6, -1.3],
                "color": "#ec4899",
                "rad": 0.34,
                "hz": 5.2,
                "status": "VULNERABILIDAD FÁSICA",
                "analogy": "Una chispa que enciende fuego cuando se pone en duda su perfección.",
                "example": "Ante una corrección menor de un colaborador, responde con descalificación tajante para restablecer control.",
                "healthy_desc": "Tolerancia afectiva serena ante discrepancias de opinión.",
                "patient_desc": "Descarga colérica amigdalina fásica orientada a castigar el desacato del otro.",
                "voice": "Amígdala reactiva. Detona la denominada rabia narcisista. Frente a una observación crítica de un allegado o colega, el afecto herido precipita una descalificación verbal tajante orientada a restituir la propia posición de valor."
            },
            {
                "id": "insula",
                "name": "Ínsula (Empatía Afectiva Desconectada)",
                "btn_label": "Ínsula",
                "region_loc": "Profundidad del Surco Lateral (Cisura de Silvio)",
                "plane": "Corte Axial Medio",
                "coords": [2.8, 0.7, -0.2],
                "color": "#334155",
                "rad": 0.28,
                "hz": 0.8,
                "status": "ANESTESIA EMPÁTICA",
                "analogy": "Mover piezas en el tablero sin conmoverse por la pieza derribada.",
                "example": "Nota con lucidez que sus comentarios hieren a su pareja, pero no experimenta compasión somática.",
                "healthy_desc": "Activación insular vicaria frente al sufrimiento de un par (empatía afectiva).",
                "patient_desc": "Hipoactivación insular afectiva con preservación de Teoría de la Mente estratégica.",
                "voice": "Ínsula anterior desconectada. Fan comprobó en la revista SCAN la presencia de una disociación central: se conserva la empatía cognitiva (sabe qué siente el otro y cómo afectarlo), pero se presenta atenuada la empatía emocional (no experimenta compasión somática)."
            }
        ],
        "tracts": [
            {
                "from": [0.0, 1.8, 1.8], "to": [0.0, 3.8, -0.8], "ctrl": [0.0, 2.8, 0.6],
                "name": "Eje de Autoevaluación Hipervigilante",
                "status": "hyper",
                "desc": "Canalización de la ofensa percibida hacia actitudes de desprecio.",
                "voice": "Eje de autoevaluación. Obliga al individuo a monitorear continuamente las señales de aprobación o reverencia del entorno para regular su equilibrio anímico."
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
                "short_label": "Conyugal",
                "pct_label": "Aproximadamente un 92 por ciento de conflictividad",
                "scientific_basis": "Estudios de patología narcisista en vínculos (Campbell et al., 2002; Ronningstam, 2005): el 92% de las parejas estables refiere dinámicas de descalificación o castigo con silencio prolongado.",
                "color": "#ef4444",
                "clinical_correlate": "Exigencia de adhesión incondicional. El cónyuge es situado en un rol de confirmación constante; las discrepancias son castigadas con desprecio o retiro del afecto."
            },
            {
                "domain": "Cohesión del Self & Riesgo de Colapso",
                "short_label": "Self",
                "pct_label": "Aproximadamente un 95 por ciento de vulnerabilidad",
                "scientific_basis": "Meta-análisis sobre Narcisismo Vulnerable y Suicidio (Pincus et al., 2009; Coleman et al., 2017): un 95% de los pacientes presenta oscilaciones severas hacia disforia ante fracasos reales.",
                "color": "#a855f7",
                "clinical_correlate": "Extrema fragilidad ante el declive laboral, financiero o físico, pudiendo desencadenar cuadros depresivos refractarios de difícil abordaje."
            },
            {
                "domain": "Entorno Laboral & Jerárquico",
                "short_label": "Laboral",
                "pct_label": "Aproximadamente un 84 por ciento de fricción",
                "scientific_basis": "Psicología organizacional de la personalidad (Babiak & O'Toole, 2012): el 84% de los puestos de liderazgo con rasgos de grandiosidad presenta rotación elevada de colaboradores.",
                "color": "#fb923c",
                "clinical_correlate": "Dificultad para el trabajo horizontal. Apropiación de logros de subordinados y hostilidad ante colegas evaluados como competencia."
            },
            {
                "domain": "Red Familiar de Origen",
                "short_label": "Familia",
                "pct_label": "Aproximadamente un 76 por ciento de instrumentalización",
                "scientific_basis": "Dinámicas transgeneracionales (Kernberg, 1984; Miller, 1981): el 76% de los vínculos con hijos está condicionado al cumplimiento de expectativas de éxito del progenitor.",
                "color": "#fb923c",
                "clinical_correlate": "Valoración de los descendientes como extensiones de prestigio personal, con distanciamiento punitivo si eligen caminos divergentes."
            },
            {
                "domain": "Adherencia a Salud Mental",
                "short_label": "Adherencia",
                "pct_label": "Aproximadamente un 50 por ciento de deserción",
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
        "definition": "Patrón dominante de emotividad excesiva y de búsqueda de atención continua, que comienza en las primeras etapas de la edad adulta y está presente en diversos contextos.",
        "dsm5_requirement": "Para el diagnóstico se exige cumplir como mínimo 5 de los 8 criterios siguientes:",
        "textbooks": [
            "American Psychiatric Association. DSM-5-TR. 2022.",
            "Bakkevig J, Karterud S. Compr Psychiatry. 2010;51(5):462-470.",
            "Shapiro, D.: Neurotic Styles (Basic Books)",
            "Millon, T.: Trastornos de la Personalidad en la Vida Moderna (Masson)"
        ],
        "dsm5_criteria": [
            "Se siente incómodo en situaciones en las que no es el centro de atención.",
            "La interacción con los demás suele estar caracterizada por un comportamiento sexualmente seductor o provocativo inapropiado.",
            "Presenta cambios rápidos y expresión plana o superficial de las emociones.",
            "Utiliza constantemente el aspecto físico para llamar la atención sobre sí mismo.",
            "Tiene un estilo de hablar excesivamente subjetivo e impresionista, carente de detalles.",
            "Muestra autodramatización, teatralidad y una expresión exagerada de la emoción.",
            "Es sugestionable (fácilmente influenciable por los demás o por las circunstancias).",
            "Considera que las relaciones son más estrechas de lo que son en realidad."
        ],
        "icd11_framework": "En la CIE-11 las manifestaciones se encuadran evaluando la severidad general de la personalidad combinada con rasgos de 'Afectividad Negativa' (labilidad afectiva) y marcada dependencia de la validación externa.",
        "biomarkers": {
            "dti": {
                "header": "Resonancia por Tensor de Difusión (DTI)",
                "title": "Vías Frontoparietales Dorsolaterales",
                "status": "Varianza Difusa en Conectividad Frontal",
                "analogy": "Una pintura al óleo vista de lejos: capta la emoción general pero pierde el detalle fino de los hechos.",
                "summary": "Menor sincronización dorsolateral que favorece un estilo cognitivo global, impresionista y con elevada sugestionabilidad ante señales sociales.",
                "ref": "Buchsbaum et al. | Schore et al. (Neuropsychoanalysis)"
            },
            "fmri_amygdala": {
                "header": "Resonancia Funcional / BOLD (Nivel de Oxigenación)",
                "title": "Red de Recompensa Estriatal",
                "status": "Hipersensibilidad al Halago y la Aprobación",
                "analogy": "Un actor sobre el escenario que necesita aplausos continuos para no sentir que la obra fracasó.",
                "summary": "Respuesta fásica amplificada en el núcleo accumbens y amígdala ante señales de simpatía, seducción o validación interpersonal inmediata.",
                "ref": "Somerville et al. (2010) | Vuilleumier et al."
            },
            "fmri_pain": {
                "header": "Red de Prominencia (Somatización)",
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
        "therapies": [
            {
                "name": "Validez del Constructo (Bakkevig & Karterud, 2010)",
                "author": "Comprehensive Psychiatry (Muestra N = 2289)",
                "focus": "Evaluación psicométrica de los criterios diagnósticos del THP.",
                "components": "Prevalencia clínica extremadamente baja (0.4%) y baja consistencia interna entre ítems.",
                "target": "Cuestiona la validez independiente de la categoría diagnóstica pura. En la práctica clínica se superpone ampliamente con rasgos límites y variantes de personalidad histriónica integrada."
            }
        ],
        "psychopharm_pearl": "No existe indicación para psicofármacos como tratamiento del estilo histriónico. Si aparecen crisis de ansiedad aguda o síntomas conversivos, el abordaje psicoterapéutico centrado en la verbalización debe primar para no reforzar la medicalización de la somatización.",
        "nodes": [
            {
                "id": "amg",
                "name": "Amígdala Límbica",
                "btn_label": "Amígdala",
                "region_loc": "Polo Medial del Lóbulo Temporal Profundo (adyacente al asta temporal)",
                "plane": "Corte Coronal Anterior",
                "coords": [1.8, -0.6, -1.3],
                "color": "#06b6d4",
                "rad": 0.36,
                "hz": 6.2,
                "status": "HIPEREXCITABLE LÁBIL",
                "analogy": "Fuegos artificiales intensos pero que se apagan a los pocos minutos.",
                "example": "Llora intensamente en un conflicto menor y poco después ríe distendida al recibir una palabra de afecto.",
                "healthy_desc": "Modulación afectiva armónica con habituación normal a contingencias sociales.",
                "patient_desc": "Reactividad emocional paroxística de rápida fluctuación y habituación precoz.",
                "voice": "Amígdala límbica lábil. Presenta respuestas afectivas rápidas y de gran expresividad externa pero de corta duración. Puede observarse un llanto desconsolado ante una situación menor, seguido minutos después por serenidad si la atención del entorno se restablece."
            },
            {
                "id": "accumbens",
                "name": "Núcleo Accumbens Social",
                "btn_label": "Accumbens",
                "region_loc": "Suelo del Estriado Ventral Anterior",
                "plane": "Corte Coronal Basal",
                "coords": [1.0, 1.1, -0.7],
                "color": "#22d3ee",
                "rad": 0.40,
                "hz": 6.5,
                "status": "HIPERRESPUESTA AL FEEDBACK",
                "analogy": "Adicción al reflector y al aplauso de los demás.",
                "example": "Si en una reunión el grupo habla de otro tema, recurre a dramatizaciones para volver a ser el centro.",
                "healthy_desc": "Procesamiento equilibrado de incentivos sociales sin demanda permanente de atención.",
                "patient_desc": "Hipersensibilidad de recompensa dependiente exclusivamente de la mirada del auditorio.",
                "voice": "Núcleo accumbens social. Circuito estrechamente ligado a la validación interpersonal. La persona experimenta una necesidad marcada de protagonismo, recurriendo a la seducción o al dramatismo si percibe que el interés del grupo decae."
            },
            {
                "id": "insula",
                "name": "Ínsula Somatosensorial",
                "btn_label": "Ínsula",
                "region_loc": "Profundidad del Surco Lateral (Cisura de Silvio)",
                "plane": "Corte Axial Medio",
                "coords": [2.8, 0.7, -0.2],
                "color": "#0891b2",
                "rad": 0.34,
                "hz": 5.4,
                "status": "SOMATIZACIÓN INTEROCEPTIVA",
                "analogy": "El cuerpo hablando en voz alta lo que la mente no pone en palabras.",
                "example": "Ante un desacuerdo familiar, experimenta mareos súbitos y pérdida de fuerza en las piernas sin causa orgánica.",
                "healthy_desc": "Integración somatosensorial armónica sin cuadros conversivos.",
                "patient_desc": "Amplificación de señales corporales que se traduce en síntomas neurológicos funcionales.",
                "voice": "Ínsula somatosensorial. Traduce tensiones emocionales no elaboradas en manifestaciones físicas. Ante desencuentros interpersonales, amplifica las señales viscerales pudiendo generar síntomas neurológicos funcionales o desmayos psicógenos."
            },
            {
                "id": "vmpfc",
                "name": "vmPFC Impresionista",
                "btn_label": "vmPFC",
                "region_loc": "Suelo Anterior Basal del Lóbulo Frontal (Áreas 10/11 de Brodmann)",
                "plane": "Corte Sagital Medial",
                "coords": [0.0, 3.8, -0.8],
                "color": "#475569",
                "rad": 0.32,
                "hz": 1.4,
                "status": "PROCESAMIENTO DIFUSO",
                "analogy": "Una mirada panorámica que no repara en la letra chica de los problemas.",
                "example": "Relata un conflicto grave en términos teatrales y vagos ('fue un desastre') sin poder precisar los hechos concretos.",
                "healthy_desc": "Razonamiento analítico estructurado y secuencial de contingencias.",
                "patient_desc": "Estilo cognitivo impresionista con escasa focalización en detalles lógicos objetivos.",
                "voice": "Corteza prefrontal impresionista. Su estilo cognitivo capta la tonalidad afectiva general de las situaciones pero tiende a omitir el análisis detallado y secuencial de las contingencias."
            }
        ],
        "tracts": [
            {
                "from": [1.8, -0.6, -1.3], "to": [1.0, 1.1, -0.7], "ctrl": [1.3, 0.4, -0.8],
                "name": "Eje Límbico-Recompensa",
                "status": "hyper",
                "desc": "Vía reforzadora de conductas de búsqueda activa de atención.",
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
                "short_label": "Conyugal",
                "pct_label": "Aproximadamente un 85 por ciento de demandas continuas",
                "scientific_basis": "Estudios clínicos de estilo histriónico (Bornstein, 2012; Horowitz, 1991): el 85% reporta desilusión recurrente con parejas al descender la intensidad apasionada inicial.",
                "color": "#ef4444",
                "clinical_correlate": "Exigencia de romanticismo novelesco sostenido. La rutina cotidiana normal es vivenciada como desamor, facilitando conductas de coqueteo con terceros para reactivar el interés."
            },
            {
                "domain": "Servicio de Guardia Médica",
                "short_label": "Guardia",
                "pct_label": "Aproximadamente un 82 por ciento de consultas funcionales",
                "scientific_basis": "Frecuentación hospitalaria en trastornos somatomorfos/histriónicos (Kroenke et al., 2007): un 82% registra admisiones por hiperventilación o cuadros neurológicos sin base orgánica.",
                "color": "#fb923c",
                "clinical_correlate": "Consultas en guardias médicas generales tras conflictos afectivos, requiriendo un abordaje que evite la sobremedicalización innecesaria."
            },
            {
                "domain": "Red Social Ampliada",
                "short_label": "Amistades",
                "pct_label": "Aproximadamente un 72 por ciento de rotación",
                "scientific_basis": "Sociometría en trastornos del Cluster B (Trull et al., 2010): el 72% experimenta rotación frecuente de amistades íntimas por demandas afectivas absorbentes.",
                "color": "#fb923c",
                "clinical_correlate": "Idealización acelerada de vínculos recientes que luego se distancian ante el desgaste que provocan las demandas afectivas continuas."
            },
            {
                "domain": "Autoestima & Dependencia Externa",
                "short_label": "Autoestima",
                "pct_label": "Aproximadamente un 80 por ciento de dependencia del halago",
                "scientific_basis": "Medición de contingencia de autoestima (Crocker & Park, 2004): el 80% de los casos puntúa en dependencia crítica del halago y la mirada externa.",
                "color": "#06b6d4",
                "clinical_correlate": "Sensación de desvanecimiento o angustia de vacío cuando no se cuenta con la mirada atenta o la aprobación explícita de los demás."
            },
            {
                "domain": "Desempeño Laboral Sistemático",
                "short_label": "Laboral",
                "pct_label": "Aproximadamente un 50 por ciento de dificultad en rutina",
                "scientific_basis": "Rendimiento ocupacional en THP (Millon, 2011): un 50% presenta dificultades de permanencia en puestos rutinarios que carecen de interacción o visibilidad.",
                "color": "#38bdf8",
                "clinical_correlate": "Baja tolerancia a labores administrativas metódicas; mejor desenvolvimiento inicial en roles que implican relaciones públicas o contacto social."
            }
        ]
    }
}

# --- Sidebar de Control Clínico y Acceso a la Presentación ---
st.sidebar.markdown("### 🎛️ Consola de Neuropsiquiatría")
selected_disorder = st.sidebar.selectbox("Entidad Patológica:", list(CLINICAL_REGISTRY.keys()))
view_selector = st.sidebar.radio("Nivel de Representación 3D:", ["1. Conectoma & Tractografía DTI", "2. Matriz de Discapacidad Funcional (WHODAS / CIE-11)"])

current_data = CLINICAL_REGISTRY[selected_disorder]

# Acceso directo al PowerPoint / PDF en la barra lateral
st.sidebar.markdown("---")
st.sidebar.markdown("### 📥 Material de Presentación")
pdf_path = "Trastornos_de_la_Personalidad_Cluster_B_(6).pdf"
if os.path.exists(pdf_path):
    with open(pdf_path, "rb") as f:
        st.sidebar.download_button(
            label="📄 Descargar Presentación (PDF)",
            data=f,
            file_name="Presentacion_Cluster_B_Ponce_Labella.pdf",
            mime="application/pdf"
        )
else:
    st.sidebar.info("💡 Colocá el archivo PDF o PPTX en el repo para habilitar la descarga directa.")

# --- Encabezado ---
st.title(selected_disorder)
st.caption(f"**Circuito Fisiopatológico Central:** {current_data['circuit_name']}")

# --- Panel Superior de Evidencia en Neuroimagen ---
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
# Motor WebGL Three.js con Botones Precisos y Etiquetas
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
      background: rgba(11, 19, 41, 0.92); backdrop-filter: blur(12px);
      border: 1px solid #1e293b; border-left: 3px solid #38bdf8; border-radius: 8px;
      padding: 12px 14px; color: #f1f5f9; max-width: 320px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.75); pointer-events: none;
    }}
    .hud-title {{ font-weight: 700; color: #38bdf8; font-size: 0.90rem; margin-bottom: 4px; font-family: monospace; }}
    .hud-desc {{ color: #94a3b8; font-size: 0.75rem; line-height: 1.4; }}
    
    #selection-menu {{
      position: absolute; bottom: 20px; left: 16px; z-index: 100;
      background: rgba(11, 19, 41, 0.90); backdrop-filter: blur(12px);
      border: 1px solid #1e293b; border-radius: 8px;
      padding: 10px 14px; color: #cbd5e1; font-size: 0.74rem; max-width: 420px;
    }}
    .menu-item {{
      display: inline-block; background: #1e293b; color: #f8fafc; border: 1px solid #334155;
      padding: 5px 10px; margin: 3px 2px; border-radius: 4px; cursor: pointer; font-size: 0.74rem; font-weight: 600;
    }}
    .menu-item:hover {{ background: #0284c7; border-color: #38bdf8; }}
    
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
      <div id="hud-body" class="hud-desc">Arrastra libremente con el ratón para rotar el encéfalo en 360° o usa la rueda para zoom.<br><br><b>Haz clic en cualquier estructura</b> para escuchar su análisis clínico, analogías y citas.</div>
    </div>
    <div id="selection-menu">
      <div style="font-weight: 700; color: #38bdf8; margin-bottom: 4px;">Explorar Estructuras / Dominios:</div>
      <div id="menu-items-container"></div>
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
        speakText("Motor de síntesis vocal activado. Selecciona cualquier estructura anatómica o esfera funcional para escuchar su explicación con rigor pedagógico.");
      }} else {{
        b.innerText = "🔇 Voz Silenciada";
        b.classList.remove("btn-active");
        if (window.speechSynthesis) window.speechSynthesis.cancel();
      }}
    }}

    function cleanTextForSpeech(text) {{
      return text.replace(/[~]/g, "aproximadamente ")
                 .replace(/[-]/g, " ")
                 .replace(/%/g, " por ciento")
                 .replace(/[\(\)]/g, "");
    }}

    function speakText(text) {{
      if (!voiceActive || !window.speechSynthesis) return;
      window.speechSynthesis.cancel();
      const cleaned = cleanTextForSpeech(text);
      const utter = new SpeechSynthesisUtterance(cleaned);
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
    const menuContainer = document.getElementById('menu-items-container');

    if (DATA.view.includes("1.")) {{
      DATA.nodes.forEach((n) => {{
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
          desc: "<b>Región:</b> " + n.region_loc + "<br><b>Estado:</b> " + n.status + "<br><b>Analogía:</b> " + n.analogy + "<br><b>Ejemplo:</b> " + n.example,
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

        const btn = document.createElement('span');
        btn.className = 'menu-item';
        btn.innerText = n.btn_label;
        btn.onclick = () => {{
          triggerObjectInspect(mesh);
        }};
        menuContainer.appendChild(btn);
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
          desc: "<b>Prevalencia observada:</b> " + e.pct_label + "<br><b>Fundamento:</b> " + e.scientific_basis + "<br><b>Patrón:</b> " + e.clinical_correlate,
          voice: e.domain + ". " + e.pct_label + ". " + e.clinical_correlate
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

        const btn = document.createElement('span');
        btn.className = 'menu-item';
        btn.innerText = e.short_label;
        btn.onclick = () => {{
          triggerObjectInspect(mesh);
        }};
        menuContainer.appendChild(btn);
      }});
    }}

    const raycaster = new THREE.Raycaster();
    const mouse = new THREE.Vector2();
    const hudHead = document.getElementById('hud-head');
    const hudBody = document.getElementById('hud-body');

    function triggerObjectInspect(target) {{
      if (target.userData && target.userData.name) {{
        hudHead.innerText = target.userData.name;
        hudBody.innerHTML = target.userData.desc;
        hudHead.style.color = "#38bdf8";
        if (target.userData.voice) {{
          speakText(target.userData.voice);
        }}
      }}
    }}

    function handleSceneClick(event) {{
      const rect = renderer.domElement.getBoundingClientRect();
      mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
      mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

      raycaster.setFromCamera(mouse, camera);
      const hits = raycaster.intersectObjects(clickableObjects);

      if (hits.length > 0) {{
        triggerObjectInspect(hits[0].object);
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
# Módulos Temáticos Interactivos en Solapas (Tabs)
# -------------------------------------------------------------------------
st.markdown("---")

tab_neuro, tab_diag, tab_treat, tab_diff, tab_case, tab_social = st.tabs([
    "🔬 Neuroimagen Comparativa", 
    "📖 Compendio Diagnóstico & Criterios", 
    "💊 Abordaje Terapéutico & Evidencia",
    "🧭 Formulación Clínica & Diferencial",
    "📋 Viñeta Clínica & Salvedad", 
    "📊 Matriz de Discapacidad WHODAS"
])

# ----------------- SOLAPA 1: NEUROIMAGEN COMPARATIVA VISUAL -----------------
with tab_neuro:
    st.subheader("Esquemas Anatómicos de Neuroimagen: Sujeto Control vs. Cuadro Clínico")
    st.caption("Cortes encefálicos con delimitación de corteza, ventrículos, surcos y mapa de calor fMRI BOLD focalizado")

    selected_node_name = st.selectbox(
        "Seleccionar estructura para proyectar su corte anatómico y correlato funcional:",
        [n["name"] for n in current_data["nodes"]]
    )

    active_node = next(n for n in current_data["nodes"] if n["name"] == selected_node_name)

    def render_medical_svg(struct_id, is_patient, color_hex):
        focal_color = color_hex if is_patient else "#10b981"
        pulse_op = "0.88" if is_patient else "0.35"
        label_text = "PATRÓN DE SEÑAL ANÓMALO" if is_patient else "ACTIVACIÓN CONTROLADA"
        
        if struct_id == "amg":
            return f"""
            <svg width="100%" height="230" viewBox="0 0 360 230" xmlns="http://www.w3.org/2000/svg" style="background:#030712; border-radius:8px; border:1px solid #1e293b;">
                <path d="M 60 130 C 50 80, 80 40, 180 35 C 280 40, 310 80, 300 130 C 295 160, 275 190, 240 190 C 215 190, 205 165, 180 165 C 155 165, 145 190, 120 190 C 85 190, 65 160, 60 130 Z" fill="#090e1a" stroke="#334155" stroke-width="2.5"/>
                <path d="M 120 40 C 130 55, 135 70, 130 85" fill="none" stroke="#1e293b" stroke-width="1.8"/>
                <path d="M 240 40 C 230 55, 225 70, 230 85" fill="none" stroke="#1e293b" stroke-width="1.8"/>
                <line x1="180" y1="35" x2="180" y2="105" stroke="#1e293b" stroke-width="2.5"/>
                <path d="M 160 88 C 160 70, 172 65, 180 75 C 188 65, 200 70, 200 88 C 200 110, 180 120, 180 120 C 180 120, 160 110, 160 88 Z" fill="#020617" stroke="#38bdf8" stroke-width="1.5" opacity="0.6"/>
                <ellipse cx="115" cy="150" rx="14" ry="10" fill="#020617" stroke="#1e293b"/>
                <ellipse cx="245" cy="150" rx="14" ry="10" fill="#020617" stroke="#1e293b"/>
                
                <circle cx="125" cy="148" r="22" fill="{focal_color}" opacity="{pulse_op}">
                    <animate attributeName="r" values="18;24;18" dur="2.2s" repeatCount="indefinite"/>
                </circle>
                <circle cx="125" cy="148" r="9" fill="{focal_color}"/>
                <circle cx="235" cy="148" r="22" fill="{focal_color}" opacity="{pulse_op}">
                    <animate attributeName="r" values="18;24;18" dur="2.2s" repeatCount="indefinite"/>
                </circle>
                <circle cx="235" cy="148" r="9" fill="{focal_color}"/>
                
                <text x="180" y="22" fill="#94a3b8" font-size="10" text-anchor="middle" font-family="sans-serif">CORTE CORONAL: LÓBULOS TEMPORALES MEDIALES</text>
                <text x="180" y="215" fill="{focal_color}" font-size="11" font-weight="bold" text-anchor="middle" font-family="monospace">{label_text}</text>
            </svg>
            """
        elif struct_id == "vmpfc" or struct_id == "dacc":
            target_cx = "115" if struct_id == "vmpfc" else "175"
            target_cy = "142" if struct_id == "vmpfc" else "90"
            tag_name = "vmPFC (SUELO FRONTAL ANTERIOR)" if struct_id == "vmpfc" else "dACC (ARCO SUPRACALLOSO)"
            return f"""
            <svg width="100%" height="230" viewBox="0 0 360 230" xmlns="http://www.w3.org/2000/svg" style="background:#030712; border-radius:8px; border:1px solid #1e293b;">
                <path d="M 90 145 C 60 130, 65 75, 120 40 C 180 35, 270 45, 290 115 C 295 145, 270 170, 235 170 C 205 170, 195 190, 160 190 C 135 190, 120 165, 90 145 Z" fill="#090e1a" stroke="#334155" stroke-width="2.5"/>
                <path d="M 140 118 C 150 88, 215 88, 225 118" fill="none" stroke="#38bdf8" stroke-width="6" stroke-linecap="round" opacity="0.6"/>
                <path d="M 230 165 C 255 170, 270 190, 245 195 C 225 195, 215 180, 230 165 Z" fill="#0f172a" stroke="#1e293b"/>
                
                <circle cx="{target_cx}" cy="{target_cy}" r="22" fill="{focal_color}" opacity="{pulse_op}">
                    <animate attributeName="r" values="18;25;18" dur="2.2s" repeatCount="indefinite"/>
                </circle>
                <circle cx="{target_cx}" cy="{target_cy}" r="9" fill="{focal_color}"/>
                
                <text x="180" y="22" fill="#94a3b8" font-size="10" text-anchor="middle" font-family="sans-serif">CORTE SAGITAL: {tag_name}</text>
                <text x="180" y="215" fill="{focal_color}" font-size="11" font-weight="bold" text-anchor="middle" font-family="monospace">{label_text}</text>
            </svg>
            """
        else:
            return f"""
            <svg width="100%" height="230" viewBox="0 0 360 230" xmlns="http://www.w3.org/2000/svg" style="background:#030712; border-radius:8px; border:1px solid #1e293b;">
                <ellipse cx="180" cy="115" rx="98" ry="80" fill="#090e1a" stroke="#334155" stroke-width="2.5"/>
                <line x1="180" y1="35" x2="180" y2="195" stroke="#1e293b" stroke-width="2.5"/>
                <path d="M 82 115 C 115 115, 130 110, 138 98" fill="none" stroke="#334155" stroke-width="2.2"/>
                <path d="M 278 115 C 245 115, 230 110, 222 98" fill="none" stroke="#334155" stroke-width="2.2"/>
                <path d="M 170 85 C 170 70, 190 70, 190 85 C 190 100, 170 100, 170 85 Z" fill="#020617" stroke="#38bdf8" stroke-width="1.2" opacity="0.6"/>
                <path d="M 172 145 C 172 135, 188 135, 188 145 C 188 158, 172 158, 172 145 Z" fill="#020617" stroke="#38bdf8" stroke-width="1.2" opacity="0.6"/>
                
                <circle cx="132" cy="108" r="20" fill="{focal_color}" opacity="{pulse_op}">
                    <animate attributeName="r" values="16;22;16" dur="2.2s" repeatCount="indefinite"/>
                </circle>
                <circle cx="132" cy="108" r="8" fill="{focal_color}"/>
                <circle cx="228" cy="108" r="20" fill="{focal_color}" opacity="{pulse_op}">
                    <animate attributeName="r" values="16;22;16" dur="2.2s" repeatCount="indefinite"/>
                </circle>
                <circle cx="228" cy="108" r="8" fill="{focal_color}"/>
                
                <text x="180" y="22" fill="#94a3b8" font-size="10" text-anchor="middle" font-family="sans-serif">CORTE AXIAL MEDIO: ÍNSULA ANTERIOR (CISURA DE SILVIO)</text>
                <text x="180" y="215" fill="{focal_color}" font-size="11" font-weight="bold" text-anchor="middle" font-family="monospace">{label_text}</text>
            </svg>
            """

    comp_html = f"""
    <div style="display: flex; gap: 16px; font-family: -apple-system, sans-serif; box-sizing: border-box;">
        <div style="flex: 1; background: #090e1a; border: 1px solid #1e293b; border-left: 4px solid #10b981; padding: 16px; border-radius: 8px;">
            <div style="color: #10b981; font-weight: bold; font-size: 0.95rem; margin-bottom: 4px;">🟢 Sujeto Control Sano (Homeostasis)</div>
            <div style="font-size: 0.78rem; color: #94a3b8; margin-bottom: 8px;"><b>Estructura:</b> {active_node['name']}<br><b>Localización:</b> {active_node['region_loc']}</div>
            {render_medical_svg(active_node['id'], False, "#10b981")}
            <div style="font-size: 0.78rem; color: #cbd5e1; margin-top: 10px; line-height: 1.45;">
                <b>Respuesta Fisiológica:</b><br>{active_node['healthy_desc']}
            </div>
        </div>
        <div style="flex: 1; background: #090e1a; border: 1px solid #1e293b; border-left: 4px solid {active_node['color']}; padding: 16px; border-radius: 8px;">
            <div style="color: {active_node['color']}; font-weight: bold; font-size: 0.95rem; margin-bottom: 4px;">🔴 Paciente: {selected_disorder.split('(')[0]}</div>
            <div style="font-size: 0.78rem; color: #94a3b8; margin-bottom: 8px;"><b>Estructura:</b> {active_node['name']}<br><b>Localización:</b> {active_node['region_loc']}</div>
            {render_medical_svg(active_node['id'], True, active_node['color'])}
            <div style="font-size: 0.78rem; color: #cbd5e1; margin-top: 10px; line-height: 1.45;">
                <b>Patrón Clínico:</b><br>{active_node['patient_desc']}<br><br>
                <b>Situación Real:</b><br>{active_node['example']}
            </div>
        </div>
    </div>
    """
    components.html(comp_html, height=480, scrolling=False)

# ----------------- SOLAPA 2: COMPENDIO NOSOLÓGICO Y CRITERIOS -----------------
with tab_diag:
    st.markdown("### Compendio Nosológico & Criterios Diagnósticos")
    st.caption("Alineado con los manuales de referencia internacional (DSM-5-TR, CIE-11) y tratados clásicos de psiquiatría")
    
    st.info(f"**Definición Formal:** {current_data['definition']}")
    
    c_dsm, c_icd = st.columns([1.2, 1.0])
    
    with c_dsm:
        st.markdown(f"#### Criterios DSM-5-TR (Asociación Estadounidense de Psiquiatría)")
        st.markdown(f"<span class='rule-badge'>{current_data['dsm5_requirement']}</span>", unsafe_allow_html=True)
        for idx, crit in enumerate(current_data["dsm5_criteria"], 1):
            st.markdown(f"**{idx}.** {crit}")
            
    with c_icd:
        st.markdown("#### Marco Conceptual Dimensional CIE-11 (OMS)")
        st.markdown(current_data["icd11_framework"])
        
        st.markdown("#### Tratados y Manuales de Referencia Utilizados")
        for book in current_data["textbooks"]:
            st.markdown(f"* 📚 {book}")

# ----------------- SOLAPA 3: ABORDAJE TERAPÉUTICO Y EVIDENCIA -----------------
with tab_treat:
    st.markdown("### Psicoterapias Especializadas y Evidencia Clínica")
    st.caption("Modelos basados en la evidencia para el abordaje de trastornos de la personalidad")
    
    if "therapies" in current_data:
        t_cols = st.columns(len(current_data["therapies"]))
        for idx, t in enumerate(current_data["therapies"]):
            with t_cols[idx]:
                st.markdown(f"""
                <div class="therapy-card">
                    <div style="color: #38bdf8; font-weight: 700; font-size: 0.95rem;">{t['name']}</div>
                    <div style="color: #94a3b8; font-size: 0.72rem; margin-bottom: 6px;"><i>{t['author']}</i></div>
                    <div style="font-size: 0.78rem; color: #f8fafc; margin-bottom: 6px;"><b>Foco:</b> {t['focus']}</div>
                    <div style="font-size: 0.74rem; color: #cbd5e1; margin-bottom: 6px;"><b>Componentes:</b> {t['components']}</div>
                    <div style="font-size: 0.74rem; color: #38bdf8; border-top: 1px solid #1e293b; padding-top: 6px;"><b>Objetivo:</b> {t['target']}</div>
                </div>
                """, unsafe_allow_html=True)
    
    # Perla farmacológica
    st.markdown(f"""
    <div class="pearl-box">
        <h4 style="color: #f59e0b; margin: 0 0 6px 0;">💊 Perla Clínica: Psicofarmacología</h4>
        <p style="color: #cbd5e1; font-size: 0.82rem; line-height: 1.45; margin: 0;">{current_data['psychopharm_pearl']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Estudio longitudinal si corresponde (TLP)
    if "longitudinal_data" in current_data:
        ld = current_data["longitudinal_data"]
        st.markdown(f"#### 📈 {ld['title']}")
        l1, l2, l3 = st.columns(3)
        l1.metric("Remisión Sintomática (>2 años)", "86%", "Zanarini et al.")
        l2.metric("Remisión Sintomática (>4 años)", "93%", "Zanarini et al.")
        l3.metric("Recuperación Funcional Plena", "50%", "Brecha Funcional", delta_color="inverse")
        st.caption(f"**Conclusión Clínica:** {ld['key_takeaway']}")

# ----------------- SOLAPA 4: FORMULACIÓN CLÍNICA Y DIFERENCIAL -----------------
with tab_diff:
    st.markdown("### Formulación Clínica en 6 Pasos")
    st.caption("De la conducta observable al plan de tratamiento sin recurrir a etiquetas prematuras (APA, 2022; Sharp et al., 2025)")
    
    step_cols = st.columns(6)
    steps = [
        {"num": "1", "title": "Describir", "desc": "Conductas observables sin juicio previo ni diagnósticos apresurados."},
        {"num": "2", "title": "Evolución", "desc": "Línea de tiempo: ¿Es un rasgo persistente o un episodio reactivo?"},
        {"num": "3", "title": "Análisis Funcional", "desc": "Antecedentes y consecuencias: ¿Qué precede y sigue a la conducta?"},
        {"num": "4", "title": "Hipótesis", "desc": "Integrar la función adaptativa o desadaptativa de la conducta."},
        {"num": "5", "title": "Contrastar", "desc": "Descartar diagnósticos alternativos (bipolaridad, consumo, trauma)."},
        {"num": "6", "title": "Objetivos", "desc": "Metas terapéuticas concretas, medibles y evaluables en el tiempo."}
    ]
    for idx, s in enumerate(steps):
        with step_cols[idx]:
            st.markdown(f"""
            <div style="background: #0b1329; border: 1px solid #1e293b; padding: 10px; border-radius: 6px; text-align: center; min-height: 130px;">
                <div style="color: #38bdf8; font-weight: 800; font-size: 1.1rem;">{s['num']}</div>
                <div style="font-weight: 700; font-size: 0.80rem; color: #f8fafc; margin-bottom: 4px;">{s['title']}</div>
                <div style="font-size: 0.70rem; color: #94a3b8; line-height: 1.3;">{s['desc']}</div>
            </div>
            """, unsafe_allow_html=True)
            
    st.markdown("---")
    st.markdown("#### Diagnóstico Diferencial Comparativo del Cluster B")
    diff_table = {
        "Trastorno": ["Límite (TLP)", "Narcisista (TNP)", "Histriónico (THP)", "Antisocial (TAP)"],
        "Patrón Nuclear": ["Inestabilidad afectiva y terror al abandono", "Grandiosidad defensiva y falta de empatía", "Emotividad excesiva y búsqueda de atención", "Desprecio y vulneración de normas y derechos"],
        "Pregunta Orientadora": ["¿Cómo se regula ante el estrés interpersonal?", "¿Cómo reacciona ante la crítica o falta de halago?", "¿Qué hace cuando no logra ser el centro de atención?", "¿Qué patrón evolutivo explica la transgresión previa a los 15 años?"],
        "Error Habitual a Evitar": ["Reducir el cuadro a autolesiones aisladas", "Confundir la grandiosidad frágil con autoestima sana", "Interpretar la teatralidad como manipulación fría", "Equiparar conducta delictiva con psicopatología"]
    }
    st.table(diff_table)

# ----------------- SOLAPA 5: VIÑETA CLÍNICA ILUSTRATIVA -----------------
with tab_case:
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

# ----------------- SOLAPA 6: MATRIZ DE DISCAPACIDAD WHODAS 2.0 -----------------
with tab_social:
    st.markdown("### Matriz de Discapacidad Funcional y Ruptura Relacional")
    st.caption("Alineada con el modelo dimensional de la CIE-11 y estudios longitudinales basados en la escala WHODAS 2.0 (OMS)")
    
    matrix_cols = st.columns(len(current_data["whodas_matrix"]))
    for idx, item in enumerate(current_data["whodas_matrix"]):
        with matrix_cols[idx]:
            st.markdown(f"""
            <div style="background: #0b1329; border: 1px solid #1e293b; border-top: 4px solid {item['color']}; padding: 12px; border-radius: 6px; min-height: 250px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="font-size: 0.68rem; text-transform: uppercase; color: #94a3b8; font-weight: 700;">{item['domain']}</div>
                    <div style="font-size: 0.86rem; font-weight: 800; color: {item['color']}; margin: 6px 0;">{item['pct_label']}</div>
                    <div style="font-size: 0.72rem; color: #cbd5e1; line-height: 1.35; margin-bottom: 8px;"><b>Patrón conductual:</b><br>{item['clinical_correlate']}</div>
                </div>
                <div style="font-size: 0.68rem; color: #64748b; border-top: 1px solid #1e293b; padding-top: 6px; font-style: italic;">
                    <b>Base científica:</b><br>{item['scientific_basis']}
                </div>
            </div>
            """, unsafe_allow_html=True)
