import streamlit as st

st.set_page_config(page_title="Absolute Clownery Generator", page_icon="🎮")

st.title("🎮 Absolute Clownery")
st.caption("FFXIV raid Markdown generator")

day = st.number_input("Day", min_value=1, value=28)
report_input = st.text_input(
    "FFLogs report ID or URL",
    value="kjtLwJz2d7CXpbTG"
)
twitch = st.text_input("Twitch username", value="lvuea")
youtube = st.text_input("YouTube VoD URL")

# Accept either a report ID or a complete FFLogs URL
report = report_input.strip().split("?")[0].rstrip("/").split("/")[-1]
twitch = twitch.strip().rstrip("/").split("/")[-1]

markdown = f"""**Absolute Clownery - Day {day}**
- Live log: [[FFLogs]](https://www.fflogs.com/reports/{report}) [[Tomestone]](https://tomestone.gg/activity/report/{report})
- Live stream: [[Twitch]](https://www.twitch.tv/{twitch})
- VoD: [[YouTube]]({youtube})
- Wipe analyzers: [[P1 Arrows]](https://analyzer.wtfdig.info/arrows?report={report}) [[P2 Forsaken]](https://analyzer.wtfdig.info/forsaken?report={report}) [[P3 Limitcut]](https://analyzer.wtfdig.info/kefka-lc?report={report}) [[P3 Black Hole]](https://analyzer.wtfdig.info/black-hole?report={report})"""

st.subheader("Generated Markdown")
st.code(markdown, language="markdown")

st.subheader("Preview")
st.markdown(markdown)
