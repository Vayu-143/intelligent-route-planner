import streamlit as st
import requests
import time

API_URL = "https://intelligent-route-planner-api.onrender.com"

# ------------------------------------------------
# Page Configuration
# ------------------------------------------------
st.set_page_config(page_title="Intelligent Route Planner", layout="wide")

st.title("🚀 Intelligent Route Planner")
st.markdown("Find the shortest route using Graph Algorithms (Dijkstra & A*)")

# ------------------------------------------------
# Load Cities
# ------------------------------------------------
try:
    city_response = requests.get(f"{API_URL}/cities")
    cities = city_response.json()["cities"]
    
    selected_city = st.sidebar.selectbox("🏙️ City", cities)
    
    location_response = requests.get(f"{API_URL}/locations/{selected_city}")
    locations = location_response.json()["locations"]
except Exception:
    st.error("❌ FastAPI Server Not Running")
    st.info("Run:\n\nuvicorn api.app:app --reload")
    st.stop()

# ------------------------------------------------
# Inputs
# ------------------------------------------------
col1, col2 = st.columns(2)
with col1:
    source = st.selectbox("📍 Source Location", locations)
with col2:
    destination = st.selectbox("🎯 Destination Location", locations)

algorithm = st.selectbox("⚙️ Algorithm", ["Dijkstra", "A*"])

# ------------------------------------------------
# Find Route
# ------------------------------------------------
if st.button("🚀 Find Route"):
    endpoint = "/dijkstra" if algorithm == "Dijkstra" else "/astar"
    payload = {
        "city": selected_city,
        "source": source,
        "destination": destination
    }

    response = requests.post(API_URL + endpoint, json=payload)

    if response.status_code != 200:
        st.error("Unable to calculate route")
        st.stop()

    data = response.json()
    st.success("✅ Route Found Successfully")

    # --------------------------------------------
    # Analytics Dashboard
    # --------------------------------------------
    st.subheader("📊 Route Analytics")
    c1, c2, c3, c4, c5 = st.columns(5)
    
    c1.metric("Distance", f"{data['distance']} km")
    c2.metric("Visited Nodes", data["visited_nodes"])
    c3.metric("Algorithm", data["algorithm"])
    c4.metric("Runtime", f"{data['execution_time']} µs")
    c5.metric("City", data["city"])
        
    # --------------------------------------------
    # Route Display
    # --------------------------------------------
    st.subheader("🛣️ Optimized Route")
    st.info(" → ".join(data["path"]))

    # --------------------------------------------
    # Graph Visualization
    # --------------------------------------------
    st.subheader("📈 Route Visualization")
    image_url = f"{API_URL}/visualization?city={selected_city}&ts={int(time.time())}"
    st.image(image_url, caption="Shortest Path Visualization", use_container_width=True)

    # --------------------------------------------
    # PDF Download
    # --------------------------------------------
    st.subheader("📄 Download Report")
    st.markdown(f"[⬇ Download PDF Report]({API_URL}/report)")

# ------------------------------------------------
# Footer
# ------------------------------------------------
st.markdown("---")
st.markdown("""
### Technologies Used
- Graphs (Adjacency List)
- Dijkstra's Algorithm
- A* Search Algorithm
- FastAPI & Streamlit
- NetworkX & Matplotlib
- ReportLab
""")