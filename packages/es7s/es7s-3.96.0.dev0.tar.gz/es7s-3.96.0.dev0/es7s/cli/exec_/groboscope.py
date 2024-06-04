# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2024 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
from es7s.cli._decorators import cli_adaptive_input, AdaptiveInputAttrs
from .._base_opts_params import CMDTRAIT_ADAPTIVE_INPUT
from .._decorators import cli_command, catch_and_log_and_exit


@cli_command(
    __file__,
    "&(gro)up &brutef&orce &d&eco&der",
    traits=[CMDTRAIT_ADAPTIVE_INPUT],
    **AdaptiveInputAttrs,
)
@cli_adaptive_input()
@catch_and_log_and_exit
def invoker(**kwargs):
    """
    Read the data from specified FILE
    """
    from es7s.cmd.groboscope import action

    action(**kwargs)
