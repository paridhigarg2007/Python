import streamlit as st
import json

st.set_page_config(page_title="Amazon Demo", layout="wide")

st.title("🛒 Amazon-Style Product Demo")
st.write("This is a simple Streamlit UI that looks similar to an Amazon product grid.")

# --- Mock product data ---
products = [
    {
        "name": "Wireless Headphones",
        "price": 59.99,
        "rating": 4.5,
        "image": "https://via.placeholder.com/200",
        "desc": "Noise-canceling over-ear headphones."
    },
    {
        "name": "USB-C Charging Cable",
        "price": 9.49,
        "rating": 4.7,
        "image": "https://via.placeholder.com/200",
        "desc": "Durable 6ft USB-C cable for fast charging."
    },
    {
        "name": "Smartwatch Series 5",
        "price": 199.00,
        "rating": 4.3,
        "image": "https://via.placeholder.com/200",
        "desc": "Fitness tracking, heart rate monitor, GPS."
    },
]

cols = st.columns(3)

for col, product in zip(cols, products):
    with col:
        st.image(product["image"])
        st.subheader(product["name"])
        st.write(product["desc"])
        st.write(f"💲 **${product['price']}**")
        st.write(f"⭐ {product['rating']}/5")
        if st.button(f"Add to Cart — {product['name']}"):
            st.success(f"Added {product['name']} to cart!")
