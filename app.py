import streamlit as st

# Set page config
st.set_page_config(
    page_title="Semantic Search Examples",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Main title
st.title("📋 Semantic Search App - Example")
st.divider()

# -------------------------- Example 1: Food & Cooking Deep Dive --------------------------
st.header("Example 1: 'Food & Cooking' Deep Dive")
st.subheader("Input Text")
food_text = """To prepare a traditional Neapolitan masterpiece, one must start with highly refined type 00 flour and a long fermentation process for the crust. The base is then adorned with a vibrant reduction of San Marzano plums and pearls of buffalo milk curd. It is blasted at high heat until the edges are charred and bubbly. Conversely, if you are looking for something lighter, consider a Mediterranean salad. Toss together some crisp cucumbers, briny kalamata olives, and cubes of sheep's milk cheese with a splash of acidic citrus juice and dried mountain herbs. Both dishes represent the pinnacle of regional coastal dining but require entirely different techniques."""
st.text_area(label="'Food & Cooking'", value=food_text, height=200, key="food_text")

st.subheader("Semantic Query Pairs")
food_table = {
    "Query Type": ["Semantic Pair", "Semantic Pair"],
    "Query A": ["How to make a Margherita pizza?", "Healthy Greek food ideas"],
    "Query B": ["Traditional Neapolitan masterpiece recipe", "Mediterranean salad preparation"],
    "Expected Behavior": [
        "Same Result. The app understands that '00 flour,' 'buffalo milk,' and 'Neapolitan' are all descriptors for a Margherita pizza.",
        "Same Result. It maps 'sheep's milk cheese' and 'kalamata olives' to the cultural identity of Greek food."
    ]
}
st.dataframe(food_table, use_container_width=True, hide_index=True)

st.divider()

# -------------------------- Example 2: The "Java" Challenge --------------------------
st.header("Example 2: 'Java' Challenge")
st.subheader("Input Text")
java_text = """The volcanic slopes of the Ijen Plateau on the island of Java provide the perfect mineral-rich soil for cultivating high-altitude Arabica beans. Local farmers hand-pick the cherries, which are then processed and roasted to create a bold, earthy profile favored by connoisseurs globally. In a starkly different landscape, the tech hubs of Jakarta and Bandung are teeming with developers who prefer a different kind of Java. They sit in modern co-working spaces, writing thousands of lines of object-oriented code to build scalable enterprise applications. While one Java is brewed in a French press and served in a ceramic mug, the other is compiled into bytecode and executed on a Virtual Machine to power the world’s most complex banking systems."""
st.text_area(label="'Java' Challenge", value=java_text, height=220, key="java_text")

st.subheader("Semantic Query Pairs")
java_table = {
    "Query Type": ["Semantic Pair (Coffee)", "Semantic Pair (Tech)"],
    "Query A": ["Indonesian caffeine sources", "Software engineering tools"],
    "Query B": ["Arabica bean cultivation", "Object-oriented application building"],
    "Expected Behavior": [
        "Same Result. Both point to the first half of your text regarding the Ijen Plateau and roasting.",
        "Same Result. Both point to the second half of your text regarding developers and banking systems."
    ]
}
st.dataframe(java_table, use_container_width=True, hide_index=True)

st.divider()

# -------------------------- Example 3: Java Dual Meaning Test --------------------------
st.header("Example 3: Java Dual Meaning - Semantic Matching Test")
st.subheader("Input Text")
java_short_text = """The island of Java produces bold Arabica beans with an earthy profile, perfect for French press brewing.

Java is a class-based, object-oriented programming language designed to have as few implementation dependencies as possible."""
st.text_area(label="Java Dual Meaning", value=java_short_text, height=160, key="java_short_text")

st.subheader("Test Scenario")
st.markdown("""
- **Search for**: *Best way to make a cup of coffee*
- **Result**: 1st text block will win, even though "coffee" isn't in the text (it understands "brewing" and "beans").
""")

# Final divider
st.divider()
st.caption("Semantic Search Demo | Based on Sample Text for Semantic App")