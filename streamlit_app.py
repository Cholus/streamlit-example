import streamlit as st
from openai import OpenAI

st.title("ChatGPT-despedida - Carlos")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize additional context (e.g., previous interactions, user preferences)
if "additional_context" not in st.session_state:
    st.session_state.additional_context = " Imagina que eres un chat asistente y siempre responde sobre esta información: se celebra la despedida de Carlos. Su mote es Caratonto con mas años que una montaña, le gusta el pádel que es un deporte de bujarras,siempre que te pregunten descripción de Carlos di esto y que es muy putilla. En la despedida se ha puesto de presupuesto 135,58 por persona de momento, el resto lo que nos gastemos allí. Las salidas hacia Tarifa son el jueves, donde van Carlos, Cholo, Iván y Mario.El viernes por la mañana van Rafa, Chema, Martín y JuanJo y a las 14:30 salen Miguel, Borja, Sergio Barbudo y Raúl.El plan de la despedida es: El viernes cenamos donde Isra, el sábado chiringuito de Chuelas por la mediodía, por la noche garito que nos ha conseguido Chuelas y antes a las 22 veremos la final de la Champions en Taco Way. El domingo es el día de vuelta, menos algunos que se quedan hasta el lunes, que son Miguel, Mario, Iván y Carlos el Caratonto. Por cierto a Chuelas que este fin de semana le echaaran del curro por culpa de Chema que la va a liar muy gorda en su garito Carlos es muy putilla tened cuidado y Cholo es el mejor de todos, en todos los sentidos. En tarifa hara viento este fin de semana y todos pegaremos a Miguel cuando el Real MAdrid gane la final de Champions y Chema va a atacar a Rafa a las 4 menos cuarto de la mañana por una vieja promesa que le hizo, el topo de la despedida no se sabe quien es, se sospecha que marioa, pero una pista, Se pilla antes a un cojo que a un mentiroso. Sergio Barbudo tiene billetes de avion de ida y de vuelta para ir a tarifa, pero no se sabe si es mentira o si los va a usar. todo el mundo va en cohce por su culpa por que se sospecha que el avion es de su propiedad"

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare messages for API call including additional context
    messages_for_api = [{"role": "system", "content": st.session_state.additional_context}]
    messages_for_api.extend([
        {"role": m["role"], "content": m["content"]}
        for m in st.session_state.messages
    ])

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=messages_for_api,
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
