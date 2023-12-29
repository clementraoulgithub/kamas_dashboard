# Nom du Projet: Kamas Dashboard
# Auteur: RAOUL Clément
# Date de Création: 17-12-2023
# Description: Ce projet à pour unique but de visualer le cours d'une devise virtuelle
# Licence: MIT License

import os

directory_path = "."

# Read header from file
with open("header.txt", "r") as file:
    header = file.read()


def header_present(file_path: str, header: str) -> bool:
    """
    Check if header is present in file

    Args:
        file_path (str): file path
        header (str): header

    Returns:
        bool: True if header is present, False otherwise
    """
    with open(file_path, "r") as file:
        content = file.read(len(header))
    return content == header


def add_header(file_path: str, header: str) -> None:
    """
    Add header to file

    Args:
        file_path (str): file path
        header (str): header
    """
    for dirpath, _, filenames in os.walk(directory_path):
        for filename in filenames:
            if filename.endswith(".py"):
                file_path = os.path.join(dirpath, filename)

                if not header_present(file_path, header):
                    with open(file_path, "r+") as file:
                        content = file.read()
                        file.seek(0, 0)
                        file.write(header.rstrip("\r\n") + "\n\n" + content)


add_header("header.h", header)
