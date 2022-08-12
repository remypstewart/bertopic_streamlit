import streamlit as st
import streamlit.components.v1 as components


st.header("test html import")

barviz_html = open("./html/bar_viz.html", 'r', encoding='utf-8')
bar_source_code = barviz_html.read() 
components.html(bar_source_code)

docviz_html = open("./html/doc_viz.html", 'r', encoding='utf-8')
doc_source_code = docviz_html.read() 
components.html(doc_source_code)

hierviz_html = open("./html/hier_viz.html", 'r', encoding='utf-8')
hier_source_code = hierviz_html.read() 
components.html(hier_source_code)

topicviz_html = open("./html/topic_viz.html", 'r', encoding='utf-8')
topic_source_code = topicviz_html.read() 
components.html(topic_source_code)

heatmapviz_html = open("./html/heatmap_viz.html", 'r', encoding='utf-8')
heatmap_source_code = heatmapviz_html.read() 
components.html(heatmap_source_code)

distviz_html = open("./html/dist_viz.html", 'r', encoding='utf-8')
dist_source_code = distviz_html.read() 
components.html(dist_source_code)