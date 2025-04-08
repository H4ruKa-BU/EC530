import openai
import os

# Set up your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_sql_query(user_query):
    try:
        # Construct the prompt for the language model
        prompt = f"You are an AI assistant tasked with converting user queries into SQL statements. The database uses SQLite and contains the following tables:\n- sales (sale_id, product_id, quantity, sale_date, revenue)\n- products (product_id, product_name, category, price)\n- employees (employee_id, name, department, hire_date)\n- customers (customer_id, customer_name, location)\n\nUser Query: '{user_query}'\n\nSQL Query:"
        
        # Make the API call to OpenAI
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.5,
            max_tokens=150
        )
        
        sql_query = response.choices[0].text.strip()
        return sql_query
    except Exception as e:
        print(f"Error generating SQL query: {e}")
        return None
