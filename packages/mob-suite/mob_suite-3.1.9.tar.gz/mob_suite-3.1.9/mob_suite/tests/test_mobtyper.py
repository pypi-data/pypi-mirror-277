import mob_suite.mob_typer
import os,sys
import pandas
import logging

TEST_ROOT = os.path.dirname(__file__)
LOG_FORMAT = '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
logging.basicConfig(format=LOG_FORMAT)
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def check_if_output_dir_exists_and_create():
    if not os.path.exists(os.path.join(TEST_ROOT,"run_test")):
        os.mkdir(os.path.join(TEST_ROOT,"run_test"))

def test_mean_and_multireplicon_frame():
    logger.info("Testing MOB-typer")
    check_if_output_dir_exists_and_create()
    args = [
        "--infile", os.path.dirname(__file__) + "/TestData/pCAV1453-208.fasta",
        "--out_file", TEST_ROOT + "/run_test/mobtyper_pCAV1453-208_results.txt",
    ]

    sys.argv[1:] = args
    mob_suite.mob_typer.main()
    assert os.path.exists(TEST_ROOT + "/run_test/mobtyper_pCAV1453-208_results.txt"), "Missing mobtyper_results.txt. Error MOB-typer did not run successfully"
