import sqlite3
# Opens a connection to an SQLite database.
# Returns a Connection object that represent the database connection.
# A new database file will be created if it doesn't already exist.
con = sqlite3.connect('social_network.db')