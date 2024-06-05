import shutil
import logging
import subprocess
def install_software(software, command):
    """安装软件包"""
    if shutil.which(command):
        pass
    else:
        if command == 'DupGen_finder.pl':
            logging.warning("please install DupGen_finder by yourself")
            logging.warning('git clone https://github.com/qiao-xin/DupGen_finder.git')
            logging.warning('cd DupGen_finder')
            logging.warning(
                f'make\nchmod 775 DupGen_finder.pl\nchmod 775 DupGen_finder-unique.pl\nchmod 775 set_PATH.sh\nsource set_PATH.sh')
            raise
        else:
            try:
                logging.info(f"{software} not found. Installing {software} using Conda...")
                subprocess.run(["conda", "install", "-c", "bioconda", "-y", software], check=True)
                logging.info(f"{software} installation completed.")
            except subprocess.CalledProcessError as e:
                logging.info(f"An error occurred during {software} installation: {e}")


install_software('miniprot', 'miniprot')
install_software('bedtools', 'bedtools')
install_software('blast', 'makeblastdb')
install_software('DupGen_finder', 'DupGen_finder.pl')
install_software("dagchainer", "run_DAG_chainer.pl")
