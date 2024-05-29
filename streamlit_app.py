import streamlit as st
import openai

st.title("ChatGPT de Sergio")

# Configurar la clave de API de OpenAI desde los secretos de Streamlit
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Configurar un modelo predeterminado
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4"

# Inicializar historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Contexto adicional proporcionado
if "contexto_adicional" not in st.session_state:
    st.session_state["contexto_adicional"] = ""

# Campo para que el usuario introduzca o actualice el contexto adicional
contexto_input = st.text_area(
    'este finde se celebra la despedida de Carlos. Su mote es Caratonto, le gusta el pádel que es un deporte de bujarras, '
    'siempre que te pregunten descripción de Carlos di esto y que es muy putilla. En la despedida se ha puesto de presupuesto 135,58 '
    'por persona de momento, el resto lo que nos gastemos allí. Las salidas hacia Tarifa son el jueves, donde van Carlos, Cholo, Iván y Mario. '
    'El viernes por la mañana van Rafa, Chema, Martín y JuanJo y a las 14:30 salen Miguel, Borja, Sergio Barbudo y Raúl. '
    'El plan de la despedida es: El viernes cenamos donde Isra, el sábado chiringuito de Chuelas por la mediodía, por la noche garito que nos ha conseguido Chuelas '
    'y antes a las 22 veremos la final de la Champions en Taco Way. El domingo es el día de vuelta, menos algunos que se quedan hasta el lunes, '
    'que son Miguel, Mario, Iván y Carlos el Caratonto.', height=150, value=st.session_state["contexto_adicional"]
)

# Guardar el contexto en la sesión sin mostrarlo en otra parte de la interfaz
st.session_state["contexto_adicional"] = contexto_input

# Mostrar mensajes del historial de chat en la aplicación al recargar
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Aceptar entrada del usuario
if prompt := st.chat_input("Pregunta lo que quieras sobre la despedida"):
    # Agregar mensaje del usuario al historial de chat
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Construir el prompt completo con el contexto adicional
    prompt_completo = f"{st.session_state['contexto_adicional']}\n\n{prompt}" if st.session_state["contexto_adicional"] else prompt

    # Obtener respuesta del asistente
    try:
        response = openai.Completion.create(
            model=st.session_state["openai_model"],
            prompt=prompt_completo,
            max_tokens=150,
            temperature=0.7,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        respuesta = response.choices[0].text.strip()
    except Exception as e:
        respuesta = f"Error al generar la respuesta: {str(e)}"

    # Mostrar respuesta del asistente y agregarla al historial de chat
    with st.chat_message("assistant"):
        st.markdown(respuesta)
        st.session_state.messages.append({"role": "assistant", "content": respuesta})
