import streamlit as st
import openai

st.title("ChatGPT de Sergio")

# Contexto adicional proporcionado
contexto_adicional = st.text_area(
    'Este fin de semana se celebra la despedida de Carlos. Su mote es Caratonto, le gusta el pádel que es un deporte de bujarras, '
    'siempre que te pregunten descripción de Carlos di esto y que es muy putilla. En la despedida se ha puesto de presupuesto 135,58 '
    'por persona de momento, el resto lo que nos gastemos allí. Las salidas hacia Tarifa son el jueves, donde van Carlos, Cholo, Iván y Mario. '
    'El viernes por la mañana van Rafa, Chema, Martín y JuanJo y a las 14:30 salen Miguel, Borja, Sergio Barbudo y Raúl. '
    'El plan de la despedida es: El viernes cenamos donde Isra, el sábado chiringuito de Chuelas por la mediodía, por la noche garito que nos ha conseguido Chuelas '
    'y antes a las 22 veremos la final de la Champions en Taco Way. El domingo es el día de vuelta, menos algunos que se quedan hasta el lunes, '
    'que son Miguel, Mario, Iván y Carlos el Caratonto.', height=150
)

# Configurar la clave de API de OpenAI desde los secretos de Streamlit
client = openai

# Configurar un modelo predeterminado
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4"

# Inicializar historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes del historial de chat en la aplicación al recargar
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Aceptar entrada del usuario
if prompt := st.chat_input("Pregunta lo que quieras sobre la despedida"):
    # Agregar mensaje del usuario al historial de chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Mostrar mensaje del usuario en el contenedor de mensajes de chat
    with st.chat_message("user"):
        st.markdown(prompt)

    # Construir el prompt completo con el contexto adicional
    if contexto_adicional:
        prompt_completo = f"{contexto_adicional}\n\n{prompt}"
    else:
        prompt_completo = prompt

    # Obtener respuesta del asistente
    with st.chat_message("assistant"):
        response = openai.Completion.create(
            engine=st.session_state["openai_model"],  # o el motor que prefieras usar
            prompt=prompt_completo,
            max_tokens=150
        )
        respuesta = response.choices[0].text.strip()
        st.markdown(respuesta)

    # Agregar respuesta del asistente al historial de chat
    st.session_state.messages.append({"role": "assistant", "content": respuesta})
