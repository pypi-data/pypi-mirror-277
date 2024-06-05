import streamlit as st

from civilpy.transportation.rail_network_simulator.RailNetworkSimulator import *

# Create the World Object
W = World(
    name="AF-RO",
    deltan=1,
    tmax=1000,
    print_mode=1, save_mode=0, show_mode=1,
    random_seed=0
)

# Define Southern (Low MP) Orgins
W.addNode("yard1_org", 0, 14)
W.addNode("y1e", 3, 14)
W.addNode("yard2_org", 0, 12)
W.addNode("yard3_org", 0, 10)
W.addNode("main3_org", 0, 8)
W.addNode("main2_org", 0, 6)
W.addNode("main1_org", 0, 4)
W.addNode("NS_org", 14, 2)
W.addNode("NS_yard", 0, 2)
W.addNode("Setoff Track", 22, 2)
W.addNode("Setoff End", 30, 2)

# Define Switches
W.addNode("0_S", 5, 12)
W.addNode("1_S", 3, 12)
W.addNode("3_S", 5, 10)
W.addNode("5_S", 7, 10)
W.addNode("7_S", 9, 8)
W.addNode("9_S", 9, 6)
W.addNode("11_S", 11, 4)
W.addNode("13_S", 11, 8)
W.addNode("15_S", 13, 10)
W.addNode("17_S", 15, 8)
W.addNode("19_S", 13, 6)
W.addNode("21_S", 15, 6)
W.addNode("23_S", 17, 8)
W.addNode("25_S", 16, 6)
W.addNode("27_S", 16, 4)
W.addNode("29_S", 18, 4)
W.addNode("31_S", 19, 4)
W.addNode("33_S", 21, 6)
W.addNode("35_S", 20, 4)
W.addNode("37_S", 22, 6)
W.addNode("39_S", 24, 4)
W.addNode("41_S", 20, 8)
W.addNode("43_S", 22, 10)
W.addNode("45_S", 23, 6)
W.addNode("47_S", 25, 8)

# Add Destinations
W.addNode("main0_dest", 30, 4)
W.addNode("main1_dest", 30, 6)
W.addNode("main2_dest", 30, 8)
W.addNode("main3_dest", 30, 10)

# Define links between Values
# Crossovers
W.addLink("1-3X", "1_S", "3_S", length=50, free_flow_speed=30, number_of_lanes=1)
W.addLink("5-7X", "5_S", "7_S", length=50, free_flow_speed=30, number_of_lanes=1)
W.addLink("9-11X", "9_S", "11_S", length=50, free_flow_speed=30, number_of_lanes=1)
W.addLink("13-19X", "13_S", "19_S", length=50, free_flow_speed=30, number_of_lanes=1)
W.addLink("15-17X", "15_S", "17_S", length=50, free_flow_speed=30, number_of_lanes=1)
W.addLink("21-23X", "21_S", "23_S", length=50, free_flow_speed=30, number_of_lanes=1)
W.addLink("25-29X", "25_S", "29_S", length=50, free_flow_speed=30, number_of_lanes=1)
W.addLink("31-33X", "31_S", "33_S", length=50, free_flow_speed=30, number_of_lanes=1)
W.addLink("37-39X", "37_S", "39_S", length=50, free_flow_speed=30, number_of_lanes=1)
W.addLink("41-43X", "41_S", "43_S", length=50, free_flow_speed=30, number_of_lanes=1)
W.addLink("45-47X", "45_S", "47_S", length=50, free_flow_speed=30, number_of_lanes=1)

# Yard Segments
W.addLink("yard1", "y1e", "yard1_org", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)
W.addLink("y1_2", "y1e", "0_S", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)
W.addLink("yard2", "yard2_org", "1_S", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)
W.addLink("NS", "NS_org", "27_S", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)
W.addLink("NS Yard", "NS_org", "NS_yard", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)
W.addLink("yard0_0", "0_S", "1_S", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)
W.addLink("Setoff_Track", "Setoff Track", "Setoff End", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)
W.addLink("Setoff Track", "Setoff Track", "35_S", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)

# Main 0 Segments
W.addLink("0_0", "main1_org", "11_S", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)
W.addLink("0_1", "11_S", "27_S", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)
W.addLink("0_2", "27_S", "29_S", length=50, free_flow_speed=50, number_of_lanes=1)
W.addLink("0_3", "29_S", "31_S", length=50, free_flow_speed=50, number_of_lanes=1)
W.addLink("0_4", "31_S", "35_S", length=50, free_flow_speed=50, number_of_lanes=1)
W.addLink("0_5", "35_S", "39_S", length=50, free_flow_speed=50, number_of_lanes=1)
W.addLink("0_6", "39_S", "main0_dest", length=50, free_flow_speed=50, number_of_lanes=1)

# Main 1 Segments
W.addLink("1_0", "main2_org", "9_S", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)
W.addLink("1_1", "9_S", "19_S", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)
W.addLink("1_2", "19_S", "21_S", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)
W.addLink("1_3", "21_S", "25_S", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)
W.addLink("1_4", "25_S", "33_S", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)
W.addLink("1_5", "33_S", "37_S", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)
W.addLink("1_6", "37_S", "45_S", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)
W.addLink("1_7", "45_S", "main1_dest", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)

# Main 2 Segments
W.addLink("2_0", "main3_org", "7_S", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)
W.addLink("2_1", "7_S", "13_S", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)
W.addLink("2_2", "13_S", "17_S", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)
W.addLink("2_3", "17_S", "23_S", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)
W.addLink("2_4", "23_S", "41_S", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)
W.addLink("2_5", "41_S", "47_S", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)
W.addLink("2_6", "47_S", "main2_dest", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)

# Main 3 Segments
W.addLink("3_0", "yard3_org", "3_S", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)
W.addLink("3_1", "3_S", "5_S", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)
W.addLink("3_2", "5_S", "15_S", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)
W.addLink("3_3", "15_S", "43_S", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)
W.addLink("3_4", "43_S", "main3_dest", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color: teal;'>Rail Network Simulator</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: green;'>Outage Selection</h1>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    col1.header('Before AF')
    st.checkbox("Yard 1 Outage", key='pre_AF_yard1_disabled')
    st.checkbox("Yard 2 Outage", key='pre_AF_yard2_disabled')
    st.checkbox("Yard 3 Outage", key='pre_AF_yard3_disabled')
    st.checkbox("Main 3 Outage", key='pre_AF_main3_disabled')
    st.checkbox("Main 2 Outage", key='pre_AF_main2_disabled')
    st.checkbox("Main 1 Outage", key='pre_AF_main1_disabled')
    st.checkbox("NS Outage",     key='pre_AF_ns_disabled')

with col2:
    col2.header('AF-Slaters Lane')
    st.checkbox("Main 3 Outage", key='AF_Slaters_main3_disabled')
    st.checkbox("Main 2 Outage", key='AF_Slaters_main2_disabled')
    st.checkbox("Main 1 Outage", key='AF_Slaters_main1_disabled')
    st.checkbox("Main 0 Outage", key='AF_Slaters_main0_disabled')

with col3:
    col3.header('Slaters Lane-RO')
    st.checkbox("Main 3 Outage", key='Slaters_RO_main3_disabled')
    st.checkbox("Main 2 Outage", key='Slaters_RO_main2_disabled')
    st.checkbox("Main 1 Outage", key='Slaters_RO_main1_disabled')
    st.checkbox("Main 0 Outage", key='Slaters_RO_main0_disabled')

with col4:
    col4.header('After RO')
    st.checkbox("Main 3 Outage", key='After_RO_main3_disabled')
    st.checkbox("Main 2 Outage", key='After_RO_main2_disabled')

st.markdown("<h1 style='text-align: center; color: green;'>Traffic Sliders</h1>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    col1.header('Main 3 Traffic')
    main_3_traffic = st.slider("main_3_traffic", min_value=0., max_value=1., step=0.01)
with col2:
    col2.header('Main 2 Traffic')
    main_2_traffic = st.slider("main_2_traffic", min_value=0., max_value=1., step=0.01)
with col3:
    col3.header('Main 1 Traffic')
    main_1_traffic = st.slider("main_1_traffic", min_value=0., max_value=1., step=0.01)
with col4:
    col4.header('Main 0 Traffic')
    main_0_traffic = st.slider("main_0_traffic", min_value=0., max_value=1., step=0.01)


W.adddemand("yard3_org", "main3_dest", 0, 1000, main_3_traffic)
W.adddemand("main3_org", "main2_dest", 0, 1000, main_2_traffic)


def run_analysis():
    time.sleep(5)
    W.exec_simulation()
    W.analyzer.print_simple_stats()


    # gif from local file
    file_ = open("D:\\Jetbrains\\PycharmProjects\\civilpy\\Notebooks\\outAF-RO\\anim_network1.gif", "rb")
    contents = file_.read()


with st.spinner('Running Analysis...'):
    st.button(label="Run Analysis", on_click=run_analysis())


st.pyplot(W.show_network(figsize=(15, 15)))



