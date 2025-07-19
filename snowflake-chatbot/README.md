# 🧠 Snowflake AI Chatbot with Snowpark

Welcome to the **Snowflake AI Chatbot** project — a powerful and scalable chatbot solution that uses **Snowflake's Snowpark for Python**, built as part of the [TastyBytes sample dataset](https://docs.snowflake.com/en/user-guide/sample-data-tastybytes) exploration and Snowflake developer training.

---

## 📌 Project Overview

This chatbot connects to Snowflake using **Snowpark for Python**, interacts with structured datasets like `TastyBytes`, and can be extended with AI/ML logic for answering business-related queries, generating insights, or automating workflows.

---

## 🧱 Architecture

```plaintext
           +-------------------+
           |   Streamlit UI    |
           +-------------------+
                     |
                     v
         +-----------------------+
         |  Snowpark for Python |
         +-----------------------+
                     |
                     v
          +---------------------+
          |  Snowflake Database |
          +---------------------+
