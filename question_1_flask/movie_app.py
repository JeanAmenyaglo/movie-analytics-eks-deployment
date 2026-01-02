# # YOUR CODE BELOW
# # flask imports and create the flask app
# #############################

import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

def load_movie_data():
    """
    Load movie data from CSV using pandas
    """
    try:
        # Load the CSV file
        df = pd.read_csv('movie_dataset.csv')
        return df
    except FileNotFoundError:
        print("Error: movie_dataset.csv not found. Make sure it's in the same directory.")
        return pd.DataFrame()  # Return empty DataFrame if file not found

@app.route('/movies')
def movies():
    """
    Handler function for /movies endpoint
    Supports query parameters:
    - movie_rated: exact match for movie rating
    - director: partial match for director name
    - If both are empty or not provided, returns all movies
    """
    # Load the movie data
    df = load_movie_data()
    
    # If DataFrame is empty (file not found), return error
    if df.empty:
        return jsonify({"error": "Movie dataset not found"}), 500
    
    # Get query parameters
    movie_rated = request.args.get('movie_rated', '').strip()
    director = request.args.get('director', '').strip()
    
    # Start with all data
    filtered_df = df
    
    # Apply filters if provided
    if movie_rated:
        # Exact match for movie_rated (case-insensitive)
        filtered_df = filtered_df[filtered_df['Movie Rated'].str.lower() == movie_rated.lower()]
    
    if director:
        # Case-insensitive partial match for director
        filtered_df = filtered_df[filtered_df['Director'].str.contains(director, case=False, na=False)]
    
    # Convert to list of dictionaries for JSON response
    result = filtered_df.to_dict(orient='records')
    
    return jsonify(result)

@app.route('/')
def home():
    return """
    <h1>Welcome to the movies API</h1>
    <p>Below are the available endpoints:</p>
    <ul>
        <li><a href="/movies">/movies</a> - Get all movies</li>
        <li><a href="/movies?movie_rated=PG-13">/movies?movie_rated=PG-13</a> - Filter by exact movie rating</li>
        <li><a href="/movies?director=Peter">/movies?director=Peter</a> - Filter by partial director name</li>
        <li><a href="/movies?movie_rated=R&director=Nolan">/movies?movie_rated=R&director=Nolan</a> - Combine both filters</li>
    </ul>
    """

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)