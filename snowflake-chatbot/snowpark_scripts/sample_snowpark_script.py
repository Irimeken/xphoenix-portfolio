from snowflake.snowpark import Session
from snowflake.snowpark.functions import col

# Snowflake connection parameters (use your own credentials securely)
connection_parameters = {
    "account": "<FSGLYOJ-WY15433>",
    "user": "<Irimekyen>",
    "password": "<ZebraFusion89golden>",
    "role": "ACCOUNTADMIN",
    "warehouse": "COMPUTE_WH",
    "database": "TASTY_BYTES",
    "schema": "PUBLIC"
}

# Create session
session = Session.builder.configs(connection_parameters).create()

# Create a sample dataframe
df = session.create_dataframe([
    (1, "Alice", "Engineering"),
    (2, "Bob", "Marketing"),
    (3, "Carol", "Engineering")
], schema=["ID", "NAME", "DEPARTMENT"])

# Filter employees from Engineering department
engineering_df = df.filter(col("DEPARTMENT") == "Engineering")

# Show results
engineering_df.show()
