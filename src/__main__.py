# Nom du Projet: Kamas Dashboard
# Auteur: RAOUL Clément
# Date de Création: 17-12-2023
# Description: Ce projet à pour unique but de visualer le cours d'une devise virtuelle
# Licence: MIT License

"""Entry point of the application."""

import os

from src.utils.scraping.scraping import schedule_scrapping

schedule_scrapping()
debug = os.environ.get("BACKEND_HOST", "localhost") == "localhost"

# pylint: disable=wrong-import-position
# pylint: disable=unused-import
from src.app import app, server

if __name__ == "__main__":
    app.run(debug=debug, host="0.0.0.0", port=80)
