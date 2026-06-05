import streamlit as st
import requests
import pandas as pd
from pathlib import Path

API_URL = "http://127.0.0.1:8000"

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="Intelligent Route Planner",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Intelligent Route Planner")

st.write(
    "Find the shortest route using Graph Algorithms "
    "(Dijkstra & A*)"
)

# -------------------------------------------------
# CITY DATASET SWITCHER
# -------------------------------------------------

st.sidebar.title("⚙ Settings")

dataset = st.sidebar.selectbox(
    "City Dataset",
    [
        "Sample City",
        "Bengaluru"
    ]
)

st.sidebar.success(
    f"Current Dataset: {dataset}"
)

# -------------------------------------------------
# LOAD LOCATIONS
# -------------------------------------------------

try:

    response = requests.get(
        f"{API_URL}/locations"
    )

    locations = response.json()["locations"]

except Exception:

    st.error(
        "FastAPI Server Not Running"
    )

    st.stop()

# -------------------------------------------------
# INPUTS
# -------------------------------------------------

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
    "⚙ Algorithm",
    [
        "Dijkstra",
        "A*"
    ]
)

# -------------------------------------------------
# FIND ROUTE
# -------------------------------------------------

if st.button("🚀 Find Route"):

    endpoint = (
        "/dijkstra"
        if algorithm == "Dijkstra"
        else "/astar"
    )

    payload = {
        "source": source,
        "destination": destination
    }

    response = requests.post(
        API_URL + endpoint,
        json=payload
    )

    if response.status_code != 200:

        st.error(
            f"API Error: {response.text}"
        )

        st.stop()

    data = response.json()

    st.success(
        "Route Found Successfully"
    )

    # ---------------------------------------------
    # ANALYTICS CARDS
    # ---------------------------------------------

    st.subheader("📊 Route Analytics")

    col1, col2, col3, col4 = st.columns(4)

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

    # ---------------------------------------------
    # ROUTE
    # ---------------------------------------------

    st.subheader(
        "🗺 Optimized Route"
    )

    st.info(
        " ➜ ".join(
            data["path"]
        )
    )

    # ---------------------------------------------
    # BENCHMARK SECTION
    # ---------------------------------------------

    st.subheader(
        "⚡ Algorithm Benchmark"
    )

    dijkstra_response = requests.post(
        f"{API_URL}/dijkstra",
        json=payload
    )

    astar_response = requests.post(
        f"{API_URL}/astar",
        json=payload
    )

    dijkstra_data = (
        dijkstra_response.json()
    )

    astar_data = (
        astar_response.json()
    )

    benchmark_df = pd.DataFrame(
        {
            "Algorithm": [
                "Dijkstra",
                "A*"
            ],

            "Distance (km)": [
                dijkstra_data["distance"],
                astar_data["distance"]
            ],

            "Visited Nodes": [
                dijkstra_data["visited_nodes"],
                astar_data["visited_nodes"]
            ],

            "Runtime (µs)": [
                dijkstra_data["execution_time"],
                astar_data["execution_time"]
            ]
        }
    )

    st.dataframe(
        benchmark_df,
        use_container_width=True
    )

    # ---------------------------------------------
    # VISUALIZATION
    # ---------------------------------------------

    st.subheader(
        "📈 Route Visualization"
    )

    image_path = Path(
        "outputs/optimized_route.png"
    )

    if image_path.exists():

        st.image(
            str(image_path),
            use_container_width=True
        )

    # ---------------------------------------------
    # PDF DOWNLOAD
    # ---------------------------------------------

    st.subheader(
        "📄 Download Report"
    )

    pdf_path = Path(
        "outputs/route_report.pdf"
    )

    if pdf_path.exists():

        with open(
            pdf_path,
            "rb"
        ) as file:

            st.download_button(
                label="⬇ Download PDF Report",
                data=file,
                file_name="route_report.pdf",
                mime="application/pdf"
            )

# -------------------------------------------------
# FOOTER
# -------------------------------------------------

st.markdown("---")

st.subheader(
    "Technologies Used"
)

st.markdown(
    """
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