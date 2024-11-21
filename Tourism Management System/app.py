from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure key

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Mani@1911',
    'database': 'tourism_dba'
}

# Database connection function
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# List all destinations or search by name/location
@app.route('/destinations', methods=['GET'])
def list_destinations():
    search_query = request.args.get('search', '')  # Get the search term from the query string

    conn = get_db_connection()
    cursor = conn.cursor()

    if search_query:
        # Perform a search by name or location (case-insensitive)
        query = '''
            SELECT * FROM destinations 
            WHERE name LIKE %s OR location LIKE %s
        '''
        cursor.execute(query, ('%' + search_query + '%', '%' + search_query + '%'))
    else:
        cursor.execute('SELECT * FROM destinations')

    destinations = cursor.fetchall()
    conn.close()

    return render_template('list.html', destinations=destinations)

# Add a destination
@app.route('/add', methods=['GET', 'POST'])
def add_destination():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        description = request.form['description']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO destinations (name, location, description) VALUES (%s, %s, %s)',
                       (name, location, description))
        conn.commit()
        conn.close()
        flash('Destination added successfully!', 'success')
        return redirect(url_for('list_destinations'))

    return render_template('add.html')

# Update a destination
@app.route('/update/<int:destination_id>', methods=['GET', 'POST'])
def update_destination(destination_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        description = request.form['description']

        cursor.execute('UPDATE destinations SET name = %s, location = %s, description = %s WHERE id = %s',
                       (name, location, description, destination_id))
        conn.commit()
        conn.close()
        flash('Destination updated successfully!', 'success')
        return redirect(url_for('list_destinations'))

    cursor.execute('SELECT * FROM destinations WHERE id = %s', (destination_id,))
    destination = cursor.fetchone()
    conn.close()
    return render_template('update.html', destination=destination)

# Delete a destination
@app.route('/delete/<int:destination_id>')
def delete_destination(destination_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM destinations WHERE id = %s', (destination_id,))
    conn.commit()
    conn.close()
    flash('Destination deleted successfully!', 'success')
    return redirect(url_for('list_destinations'))

if __name__ == '__main__':
    app.run(debug=True)
