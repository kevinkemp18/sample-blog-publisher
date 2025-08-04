import streamlit as st
import pandas as pd
import requests

# Sample blog data
df = pd.DataFrame([
    {
        "Title": "What Are the Gifts of the Holy Spirit?",
        "Slug": "gifts-of-the-holy-spirit",
        "Meta Title": "Gifts of the Holy Spirit – Explained",
        "Meta Description": "Understand the 9 spiritual gifts and how they empower your ministry.",
        "Category": "Faith",
        "Doc URL": "https://example.com/fake-doc",
        "Featured Image URL": "https://via.placeholder.com/600x400"
    }
])

# UI
st.title("📝 Sample Blog Publisher (Demo)")

site_choice = st.selectbox("Select Site", ["Demo Site"])
selected_blog = st.selectbox("Choose Blog to Publish", df['Title'])

blog_data = df[df['Title'] == selected_blog].iloc[0]
st.markdown(f"**Meta Title:** {blog_data['Meta Title']}")
st.markdown(f"**Meta Description:** {blog_data['Meta Description']}")
st.markdown(f"**Slug:** {blog_data['Slug']}")
st.markdown(f"**Category:** {blog_data['Category']}")
st.image(blog_data["Featured Image URL"], width=400)

def convert_doc_to_html(doc_url):
    return "<p>This is a simulated HTML blog content block.</p>"

def publish_fake():
    st.info("🔄 Sending mock blog post to WordPress...")
    return {"status_code": 201, "message": "Blog post successfully 'published'"}

if st.button("🚀 Publish Blog (Mock)"):
    html_content = convert_doc_to_html(blog_data["Doc URL"])
    response = publish_fake()
    if response["status_code"] == 201:
        st.success("✅ Blog published successfully (simulated)!")
    else:
        st.error("❌ Failed to publish.")
