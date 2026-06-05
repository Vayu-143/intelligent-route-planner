import os
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

# ------------------------------------------------
# Page Configuration
# ------------------------------------------------

st.set_page_config(
    page_title="Intelligent Route Planner",
    layout="wide"
)

st.title(
    "🚀 Intelligent Route Planner"
)

st.markdown(
    "Find the shortest route using Graph Algorithms (Dijkstra & A*)"
)

# ------------------------------------------------
# Load Cities
# ------------------------------------------------

try:

    city_response = requests.get(
        f"{API_URL}/cities"
    )

    cities = (
        city_response.json()
        ["cities"]
    )

    city = st.sidebar.selectbox(
        "🏙️ City",
        cities
    )

    location_response = requests.get(
        f"{API_URL}/locations/{city}"
    )

    locations = (
        location_response.json()
        ["locations"]
    )

except Exception:

    st.error(
        "❌ FastAPI Server Not Running"
    )

    st.info(
        "Run:\n\nuvicorn api.app:app --reload"
    )

    st.stop()

# ------------------------------------------------
# Inputs
# ------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    source = st.selectbox(
        "📍 Source Location",
        locations
    )

with col2:

    destination = st.selectbox(
        "🎯 Destination Location",
        locations
    )

algorithm = st.selectbox(
    "⚙️ Algorithm",
    [
        "Dijkstra",
        "A*"
    ]
)

# ------------------------------------------------
# Find Route
# ------------------------------------------------

if st.button(
    "🚀 Find Route"
):

    endpoint = (
        "/dijkstra"
        if algorithm == "Dijkstra"
        else "/astar"
    )

    payload = {

    "city":
    city,

    "source":
    source,

    "destination":
    destination
}

    response = requests.post(
        API_URL + endpoint,
        json=payload
    )

    if response.status_code != 200:

        st.error(
            "Unable to calculate route"
        )

        st.stop()

    data = response.json()

    st.success(
        "✅ Route Found Successfully"
    )
    st.info(
    f"🏙️ Dataset: {data['city']}"
)
 
    # --------------------------------------------
    # Analytics Dashboard
    # --------------------------------------------

    st.subheader(
        "📊 Route Analytics"
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:

        st.metric(
            "Distance",
            f"{data['distance']} km"
        )

    with col2:

        st.metric(
            "Visited Nodes",
            data["visited_nodes"]
        )

    with col3:

        st.metric(
            "Algorithm",
            data["algorithm"]
        )

    with col4:

        st.metric(
    "Runtime",
    f"{data['execution_time']} µs"
)
        
        with col5:

         st.metric(
        "City",
        data["city"]
    )
        
    # --------------------------------------------
    # Route Display
    # --------------------------------------------

    st.subheader(
        "🛣️ Optimized Route"
    )

    st.info(
        " → ".join(
            data["path"]
        )
    )

    # --------------------------------------------
    # Graph Visualization
    # --------------------------------------------

    st.subheader(
        "📈 Route Visualization"
    )

    image_path = (
        "outputs/optimized_route.png"
    )

    if os.path.exists(
        image_path
    ):

        st.image(
            image_path,
            caption=
            "Shortest Path Visualization",
            use_container_width=True
        )

    else:

        st.warning(
            "Visualization image not found."
        )

    # --------------------------------------------
    # PDF Download
    # --------------------------------------------

    st.subheader(
        "📄 Download Report"
    )

    pdf_path = (
        "outputs/route_report.pdf"
    )

    if os.path.exists(
        pdf_path
    ):

        with open(
            pdf_path,
            "rb"
        ) as pdf_file:

            st.download_button(
                label=
                "⬇ Download PDF Report",

                data=pdf_file,

                file_name=
                "route_report.pdf",

                mime=
                "application/pdf"
            )

    else:

        st.warning(
            "PDF report not found."
        )

# ------------------------------------------------
# Footer
# ------------------------------------------------

st.markdown("---")

st.markdown(
    """
    ### Technologies Used

    - Graphs (Adjacency List)
    - BFS
    - DFS
    - Dijkstra's Algorithm
    - A* Search Algorithm
    - FastAPI
    - Streamlit
    - NetworkX
    - Matplotlib
    - ReportLab
    """
)