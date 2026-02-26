import streamlit as st
import os
import time
import glob
import os
from gtts import gTTS
from PIL import Image
import base64

st.title("Audio Libro Para niños")
image = Image.open("Barbie y las 3 mosqueteras.png")
st.image(image, width=350)
with st.sidebar:
    st.subheader("Esrcibe y/o selecciona texto para ser escuchado.")


try:
    os.mkdir("temp")
except:
    pass

st.subheader("Barbie y las 3 mosqueteras")
st.write('Había una vez una joven llamada Corinne que soñaba con algo que nadie esperaba: quería ser mosquetera, igual que su padre. Aunque muchos le decían que eso no era para chicas, ella no dejó que apagaran su sueño y viajó hasta París con el corazón lleno de esperanza. Al llegar al palacio, no la aceptaron como mosquetera y terminó trabajando como sirvienta. Pero el destino tenía otros planes. Allí conoció a tres chicas valientes y muy diferentes entre sí. Una era ágil como el viento, otra fuerte como un roble y otra tan inteligente que siempre encontraba la solución perfecta. Juntas descubrieron que compartían el mismo deseo: proteger al reino. Por las noches entrenaban en secreto, practicando con espadas y aprendiendo a confiar unas en otras. Y justo a tiempo, descubrieron un plan malvado contra el príncipe. Sin dudarlo, las cuatro amigas unieron fuerzas y, con valentía y trabajo en equipo, lograron salvar el día. Desde entonces, demostraron que el coraje no depende de quién seas, sino de lo que llevas en el corazón. Y así, Corinne y sus amigas se convirtieron en las mosqueteras más valientes del reino.'
        
        )
           
st.markdown(f"Quieres escucharlo?, copia el texto y pégalo aquí abajo")
text = st.text_area("Ingrese El texto a escuchar.")

tld='com'
option_lang = st.selectbox(
    "Selecciona el lenguaje",
    ("Español", "English"))
if option_lang=="Español" :
    lg='es'
if option_lang=="English" :
    lg='en'

def text_to_speech(text, tld,lg):
    
    tts = gTTS(text,lang=lg) # tts = gTTS(text,'en', tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, text


#display_output_text = st.checkbox("Verifica el texto")

if st.button("convertir a Audio"):
     result, output_text = text_to_speech(text, 'com',lg)#'tld
     audio_file = open(f"temp/{result}.mp3", "rb")
     audio_bytes = audio_file.read()
     st.markdown(f"## Tú audio:")
     st.audio(audio_bytes, format="audio/mp3", start_time=0)

     #if display_output_text:
     
     #st.write(f" {output_text}")
    
#if st.button("ElevenLAabs",key=2):
#     from elevenlabs import play
#     from elevenlabs.client import ElevenLabs
#     client = ElevenLabs(api_key="a71bb432d643bbf80986c0cf0970d91a", # Defaults to ELEVEN_API_KEY)
#     audio = client.generate(text=f" {output_text}",voice="Rachel",model="eleven_multilingual_v1")
#     audio_file = open(f"temp/{audio}.mp3", "rb")

     with open(f"temp/{result}.mp3", "rb") as f:
         data = f.read()

     def get_binary_file_downloader_html(bin_file, file_label='File'):
        bin_str = base64.b64encode(data).decode()
        href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
        return href
     st.markdown(get_binary_file_downloader_html("audio.mp3", file_label="Audio File"), unsafe_allow_html=True)

def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)


remove_files(7)
