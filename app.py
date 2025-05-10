import streamlit as st
import requests

# --- page configuration---
st.set_page_config(
    page_title="StudyPal",
    page_icon="🧠",
    layout="centered", #wide

)

st.title("🧠 StudyPal Application")

#--- API details---
api_url = "http://127.0.0.1:8000/ask"
PROVIDERS = ["Groq","Ollama"]
MODELS = ["llama 3.3", "DeepSeek R1"]

#--- Initialize Session State ---
st.session_state.setdefault("show_settings",False)
st.session_state.setdefault("provider",PROVIDERS[0])
st.session_state.setdefault("model",MODELS[0])



#--- Layout ---
col1, col2 = st.columns([8,1])
question = col1.text_input(label="Ask your question",placeholder="e.g., What is ML?")

if col2.button("⚙️", help="Select Model  Settings"):
    st.session_state.show_settings = not st.session_state.show_settings

#---Model Settings---
if st.session_state.show_settings:
    with st.expander("🔧 Model Settings",expanded=True):
        st.session_state.provider = st.selectbox(label = "Provider",
                                options=PROVIDERS,
                                index=PROVIDERS.index(st.session_state.provider))
        st.session_state.model = st.selectbox(label = "Model",
                             options=MODELS,
                             index=MODELS.index(st.session_state.model) )
        st.success(f"using {st.session_state.provider} - {st.session_state.model}")


#---Get Answer from API---
if st.button("Get answer"):
    response = requests.post(
        url=api_url,
        json={"question": question}
    )

    result=response.json()
    answer=result["answer"]
    st.success(answer)
