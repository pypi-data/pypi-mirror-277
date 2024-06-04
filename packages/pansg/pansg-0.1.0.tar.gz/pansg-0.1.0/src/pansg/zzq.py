import subprocess
import shutil
import logging

from _logging import set_logging_level


def install_software(software, command):
    if shutil.which(command):
        pass
    else:
        try:
            logging.info(f"{software} not found. Installing {software} using Conda...")
            subprocess.run(["conda", "install", "-c", "bioconda", "-y", software], check=True)
            logging.info(f"{software} installation completed.")
        except subprocess.CalledProcessError as e:
            logging.info(f"An error occurred during {software} installation: {e}")


def main(config, pan_matrix, verbose):
    set_logging_level(verbose)
    install_software('miniprot', 'miniprot')
    install_software('bedtools', 'bedtools')
    subprocess.run(['bash',
                    'run_zzq.sh',
                    config, pan_matrix], shell=True, check=True)
