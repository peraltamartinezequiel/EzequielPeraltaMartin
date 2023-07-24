"""
This script runs the ProyectoFinal application using a development server.
"""

from os import environ
from ProyectoFinal import app

if __name__ == '__main__':
    app.run(debug=True)
