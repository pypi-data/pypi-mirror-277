import subprocess

from _logging import set_logging_level


def main(config, pan_matrix, verbose):
    set_logging_level(verbose)
    subprocess.run(['bash',
                    'run_zzq.sh',
                    config, pan_matrix], shell=True, check=True)
