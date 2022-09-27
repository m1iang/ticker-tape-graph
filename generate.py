from dvst import run_dvst, run_dvst_scatter
from vvst import run_vvst, run_vvst_scatter


def generate_graphs():
    run_dvst()
    run_dvst_scatter()
    run_vvst()
    run_vvst_scatter()
