import streamlit as st
from PIL import Image
import requests
import io
import time

# --- Page configuration ---
st.set_page_config(page_title="Camera Input", page_icon="📷")
st.title("📷 Take a Gesture Snapshot")
st.markdown("---")
st.markdown("<br><br>", unsafe_allow_html=True)


# --- API URL ---
API_URL = "https://emojiwave-718530444960.europe-west1.run.app/predict"

# --- Emoji mapping ---
emoji_map = {
    "thumbs_up": "👍",
    "call_me": "🤙",
    "fingers_crossed": "🤞",
    "index_up": "☝️",
    "okay": "👌",
    "paper": "🖐️",
    "rock": "👊",
    "rock_on": "🤘",
    "scissor": "✌️",
    "spock": "🖖",
}

# --- Fun camera challenge card ---
st.markdown("### Can your webcam handle the challenge? 📸")

st.markdown("""
    <style>
    @keyframes gentle-bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-6px); }
    }
    .bouncy-card {
        animation: gentle-bounce 2s ease-in-out infinite;
    }
    </style>

    <div class='bouncy-card' style='
        background-color: #fffdf8;
        padding: 25px;
        margin-top: 15px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(249,115,22,0.15);
    '>
        <p style='font-size:18px; margin-bottom: 12px;'>🎬 <strong>Ready to go live?</strong> Let's test your reflexes.</p>
        <p style='font-size:18px; margin-bottom: 8px;'>✋ Hold up a gesture to your webcam.</p>
        <p style='font-size:18px; margin-bottom: 8px;'>🧠 Watch closely... the AI is analyzing your move.</p>
        <p style='font-size:18px;'><strong>✨ Let's see if it nails the prediction!</strong></p>
    </div>
""", unsafe_allow_html=True)

# --- API communication ---
def send_prediction(image, source):
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    buffered.seek(0)
    files = {"file": ("image.jpg", buffered.read(), "image/jpeg")}
    data = {"source": source}
    return requests.post(API_URL, files=files, data=data)

# --- Session state ---
if "show_popup" not in st.session_state:
    st.session_state.show_popup = False
if "prediction" not in st.session_state:
    st.session_state.prediction = ""
if "trigger_prediction" not in st.session_state:
    st.session_state.trigger_prediction = False

# --- Camera input ---
captured_image = st.camera_input("Take a picture")

if captured_image:
    image = Image.open(captured_image)
    st.image(image, caption="Captured Image", width=400)
    st.session_state.captured_image = image

    if st.button("✨ Predict Gesture"):
        st.session_state.trigger_prediction = True

# --- Run prediction if triggered ---
if st.session_state.trigger_prediction and "captured_image" in st.session_state:
    with st.spinner("🔮 Analyzing your gesture..."):
        image = st.session_state.captured_image
        response = send_prediction(image, source="camera")
        time.sleep(1)

        if response.status_code == 200:
            result = response.json()
            st.session_state.prediction = result["prediction"]
            st.session_state.show_popup = True
        else:
            st.error("Prediction failed. Please check the API.")

        st.session_state.trigger_prediction = False
        del st.session_state.captured_image

# --- Show popup if prediction is ready ---
if st.session_state.show_popup:
    pred_class = st.session_state.prediction
    emoji = emoji_map.get(pred_class, "❓")
    pretty_name = pred_class.replace("_", " ").title()
    description = f"Wow! You got <strong style='color:#f97316'>{pretty_name}</strong>"

    st.markdown(f"""
        <style>
        .popup-overlay {{
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background-color: rgba(0,0,0,0.4);
            z-index: 1001;
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .popup-box {{
            background-color: #fff;
            padding: 40px;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0px 8px 20px rgba(0,0,0,0.3);
            animation: fadeIn 0.5s ease-in-out;
        }}
        .emoji-animated {{
            font-size: 100px;
            animation: bounce 1.2s infinite;
        }}
        .close-btn {{
            margin-top: 20px;
            background-color: #FFE4C4;
            border: none;
            color:#F97316;
            font-size: 16px;
            font-weight: bold;
            border-radius: 10px;
            padding: 10px 20px;
            cursor: pointer;
        }}
        @keyframes bounce {{
            0%, 100% {{ transform: translateY(0); }}
            50% {{ transform: translateY(-15px); }}
        }}
        @keyframes fadeIn {{
            from {{opacity: 0;}}
            to {{opacity: 1;}}
        }}
        </style>

        <div class="popup-overlay">
            <div class="popup-box">
                <div class="emoji-animated">{emoji}</div>
                <p style="font-size: 24px; margin-top: 10px;">{description}</p>
                <form action="" method="get">
                    <button class="close-btn" name="close_popup" type="submit">spin the wheel again!</button>
                </form>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #888;'>Crafted with ❤️ and 🤖 to Bring Hand Gestures to Life  ©️ 2025</p>", unsafe_allow_html=True)
