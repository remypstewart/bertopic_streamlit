import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
st.set_page_config(layout="wide")

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Topic-Document Distribution", "Intertopic Distance", "Topic Bar Chart", "Topic Heat Map", "Topic Hierarchy", "Topic Probability for One Record", "Topic Keyword DataFrame"])

with tab1:
    st.header("BERTopic Results on ONET Task Data")
    st.subheader("Topic-Document Distribution")
    count_tab1 = st.radio("Fitted Topic Model Count", ('50 Topics', '360 (All) Topics'), key="st1", horizontal=True)
    st.markdown("This visualization plots the ONET task sentence embeddings based on their proximity to other embedded tasks, while simultanelously color-coding the embeddings by their most probable document. This offers an overview of both the full sentences associated with found topics as well as how the topics are mapped in proximity to each other within the projected embedding space. You can hover over a data point and see its full task sentence.")
    if count_tab1 == "50 Topics":
        docviz_html = open("./html/doc_viz.html", 'r', encoding='utf-8')
        doc_source_code = docviz_html.read() 
        components.html(doc_source_code, height=1100, width=1200)
    else: 
        docviz_html = open("./html/topic_doc_full.html", 'r', encoding='utf-8')
        doc_source_code = docviz_html.read() 
        components.html(doc_source_code, height=1100, width=1200)

with tab2:
    st.header("BERTopic Results on ONET Task Data")
    st.subheader("Intertopic Distance")
    count_tab2 = st.radio("Fitted Topic Model Count", ('50 Topics', '360 (All) Topics'), key="st2", horizontal=True)
    st.markdown("This visualization illustrates found topics as circles with their size reflecting their rate of occurance among the task sentences. The figure's axes represent the two largest principle components of variation within the sentence embeddings. The mapped topic circles therefore naturally agglomerate into subclusters of topics identified by BERTopic to represent conceptually similar job tasks.")
    if count_tab2 == "50 Topics":
        topicviz_html = open("./html/topic_viz.html", 'r', encoding='utf-8')
        topic_source_code = topicviz_html.read() 
        components.html(topic_source_code, height=1000, width=1000)
    else:
        topicviz_html = open("./html/topics_viz_full.html", 'r', encoding='utf-8')
        topic_source_code = topicviz_html.read() 
        components.html(topic_source_code, height=1000, width=1000)

with tab3:
    st.header("BERTopic Results on ONET Task Data")
    st.subheader("Topic Bar Chart")
    count_tab3 = st.radio("Fitted Topic Model Count", ('50 Topics', '360 (All) Topics'), key="st3", horizontal=True)
    st.markdown("This visualization provides the 16 most common topics segmented by their top five keywords. These keywords are ranked by their respective cluster Term Frequency-Inverse Document Frequency (TF-IDF) score computed by our BERTopic model.")
    if count_tab3 == "50 Topics":
        barviz_html = open("./html/bar_viz.html", 'r', encoding='utf-8')
        bar_source_code = barviz_html.read() 
        components.html(bar_source_code, height=1000, width=1000)
    else: 
        barviz_html = open("./html/bar_viz_full.html", 'r', encoding='utf-8')
        bar_source_code = barviz_html.read() 
        components.html(bar_source_code, height=1000, width=1000)

with tab4:
    st.header("BERTopic Results on ONET Task Data")
    st.subheader("Topic Heat Map")
    count_tab4 = st.radio("Fitted Topic Model Count", ('50 Topics', '360 (All) Topics'), key="st4", horizontal=True)
    st.markdown("This visualization creates a 50x50 topic matrix of each topic's cosine similarity score with each of the other topics within embedding space. You can hover over a given cell to review the score associated with each topic comparison.")
    if count_tab4 == "50 Topics":
        heatmapviz_html = open("./html/heatmap_viz.html", 'r', encoding='utf-8')
        heatmap_source_code = heatmapviz_html.read() 
        components.html(heatmap_source_code, height=1000, width=1000)   
    else: 
        heatmapviz_html = open("./html/heatmap_full.html", 'r', encoding='utf-8')
        heatmap_source_code = heatmapviz_html.read() 
        components.html(heatmap_source_code, height=1000, width=1000)   

with tab5:
    st.header("BERTopic Results on ONET Task Data")
    st.subheader("Topic Hierarchy")
    count_tab5 = st.radio("Fitted Topic Model Count", ('50 Topics', '360 (All) Topics'), key="st5", horizontal=True)
    st.markdown("This visualization delineates the hierarchical clustering relationships discovered by BERTopic as the model segments individual topics. It provides insights towards the common thematic ancestry between the final topics.")
    if count_tab5 == "50 Topics":
        hierviz_html = open("./html/hier_viz.html", 'r', encoding='utf-8')
        hier_source_code = hierviz_html.read() 
        components.html(hier_source_code, height=1000, width=1000)
    else: 
        hierviz_html = open("./html/hierarchy_full.html", 'r', encoding='utf-8')
        hier_source_code = hierviz_html.read() 
        components.html(hier_source_code, height=5900, width=1000)

with tab6:
    st.header("BERTopic Results on ONET Task Data")
    st.subheader("Topic Probabilities for One Record")
    count_tab6 = st.radio("Fitted Topic Model Count", ('50 Topics', '360 (All) Topics'), key="st6", horizontal=True)
    st.markdown('This visualization displays the topic probabilities of a single task sentence within the ONET data. The task record this visual refers to is "Direct, plan, or implement policies, objectives, or activities of organizations and businesses to ensure continuing operations, to maximize returns on investments, or to increase productivity."')
    if count_tab6 == "50 Topics":
        distviz_html = open("./html/dist_viz.html", 'r', encoding='utf-8')
        dist_source_code = distviz_html.read() 
        components.html(dist_source_code, height=1000, width=1000)
    else: 
        distviz_html = open("./html/dist_full.html", 'r', encoding='utf-8')
        dist_source_code = distviz_html.read() 
        components.html(dist_source_code, height=1000, width=1000)

with tab7:
    st.header("BERTopic Results on ONET Task Data")
    st.subheader("Topic Counts & Keywords")
    count_tab7 = st.radio("Fitted Topic Model Count", ('50 Topics', '360 (All) Topics'), key="st7", horizontal=True)
    st.markdown('This table ranks topics by their frequency counts and to their top keywords.')
    if count_tab7 == "50 Topics":
        topics_50 = pd.read_parquet("./pqt/50_topics.pqt")
        st.dataframe(topics_50, height=2000, width=1300)
    else:
        topics_full = pd.read_parquet("./pqt/full_topics.pqt")
        st.dataframe(topics_full, height=2000, width=1300)