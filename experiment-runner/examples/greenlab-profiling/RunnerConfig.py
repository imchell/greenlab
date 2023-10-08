from EventManager.Models.RunnerEvents import RunnerEvents
from EventManager.EventSubscriptionController import EventSubscriptionController
from ConfigValidator.Config.Models.RunTableModel import RunTableModel
from ConfigValidator.Config.Models.FactorModel import FactorModel
from ConfigValidator.Config.Models.RunnerContext import RunnerContext
from ConfigValidator.Config.Models.OperationType import OperationType
from ProgressManager.Output.OutputProcedure import OutputProcedure as output

import yaml
from fabric import Connection

from typing import Dict, List, Any, Optional
from pathlib import Path
from os.path import dirname, realpath

import psutil
import time
import pandas as pd
import threading

class RunnerConfig:
    ROOT_DIR = Path(dirname(realpath(__file__)))

    # ================================ USER SPECIFIC CONFIG ================================
    """The name of the experiment."""
    name:                       str             = "new_runner_experiment"

    """The path in which Experiment Runner will create a folder with the name `self.name`, in order to store the
    results from this experiment. (Path does not need to exist - it will be created if necessary.)
    Output path defaults to the config file's path, inside the folder 'experiments'"""
    results_output_path:        Path             = ROOT_DIR / 'experiments'

    """Experiment operation type. Unless you manually want to initiate each run, use `OperationType.AUTO`."""
    operation_type:             OperationType   = OperationType.AUTO

    """The time Experiment Runner will wait after a run completes.
    This can be essential to accommodate for cooldown periods on some systems."""
    time_between_runs_in_ms:    int             = 1000

    # Dynamic configurations can be one-time satisfied here before the program takes the config as-is
    # e.g. Setting some variable based on some criteria
    def __init__(self):
        """Executes immediately after program start, on config load"""

        EventSubscriptionController.subscribe_to_multiple_events([
            (RunnerEvents.BEFORE_EXPERIMENT, self.before_experiment),
            (RunnerEvents.BEFORE_RUN       , self.before_run       ),
            (RunnerEvents.START_RUN        , self.start_run        ),
            (RunnerEvents.START_MEASUREMENT, self.start_measurement),
            (RunnerEvents.INTERACT         , self.interact         ),
            (RunnerEvents.STOP_MEASUREMENT , self.stop_measurement ),
            (RunnerEvents.STOP_RUN         , self.stop_run         ),
            (RunnerEvents.POPULATE_RUN_DATA, self.populate_run_data),
            (RunnerEvents.AFTER_EXPERIMENT , self.after_experiment )
        ])
        self.run_table_model = None  # Initialized later
        self.fabconfig = None
        self.c = None
        self.t = None
        self.pid = None
        self.cpu_usage = None
        self.stop_measurement_thread = False
        self.stop_run_thread = False
        output.console_log("Custom config loaded")

    def create_run_table_model(self) -> RunTableModel:
        """Create and return the run_table model here. A run_table is a List (rows) of tuples (columns),
        representing each run performed"""

        factor_algo = FactorModel("Algorithm", ['helloworld', 'fasta'])
                                  # ['fasta', 'knucleotide', 'pidigits', 'regexredux', 'revcomp'])
        factor_language = FactorModel("Language", ['py'])
        # TODO: add handwritten factor
        factor_gpt = FactorModel("GPT", [False])
        self.run_table_model = RunTableModel(
            factors=[factor_algo, factor_language, factor_gpt],
            data_columns=['avg_cpu', 'avg_mem']
        )
        
        return self.run_table_model

    def before_experiment(self) -> None:
        """Perform any activity required before starting the experiment here
        Invoked only once during the lifetime of the program."""

        output.console_log("Config.before_experiment() called!")

        # Load the connection configuration
        with open('fabconfig.yml') as f:
            self.fabconfig = yaml.safe_load(f)

        host = self.fabconfig['hosts']['raspberrypi']

        # Replace the following parameters with your own Raspberry Pi's IP address, username and password
        # For start_run() and stop_run()
        self.c = Connection(host['hostname'], user=host['user'], connect_kwargs={'password': host['password']})
        # For start_measurement() and stop_measurement()
        self.t = Connection(host['hostname'], user=host['user'], connect_kwargs={'password': host['password']})

    def before_run(self) -> None:
        """Perform any activity required before starting a run.
        No context is available here as the run is not yet active (BEFORE RUN)"""

        output.console_log("Config.before_run() called!")

    def start_run(self, context: RunnerContext) -> None:
        """Perform any activity required for starting the run here.
        For example, starting the target system to measure.
        Activities after starting the run should also be performed here."""

        output.console_log("Config.start_run() called!")

        algo = context.run_variation['Algorithm']
        lang = context.run_variation['Language']
        gpt = context.run_variation['GPT']

        if gpt:
            print(f"Running {algo} in {lang} with GPT generated code")
        else:
            print(f"Running {algo} in {lang} with handwritten code")
            if lang == 'py':
                if algo == 'fasta':
                    #TODO: change input size
                    def run_thread():
                        if not self.stop_run_thread:
                            self.c.run(f'python -OO {self.fabconfig["hosts"]["codepath"]}handwritten/{algo}.py 1000', hide=True)

                    self.c_thread = threading.Thread(target=run_thread)
                    self.c_thread.start()

                if algo == 'helloworld':
                    def run_thread():
                        if not self.stop_run_thread:
                            self.c.run(f'nohup python -OO {self.fabconfig["hosts"]["codepath"]}handwritten/helloworld.py', hide=True)

                    self.c_thread = threading.Thread(target=run_thread)
                    self.c_thread.start()

    def start_measurement(self, context: RunnerContext) -> None:
        """Perform any activity required for starting measurements."""
        output.console_log("Config.start_measurement() called!")     
        
        profiler_cmd = "top -b -n1 | grep 'Cpu(s)' | awk '{print $2 + $4}'"

        def profiler_thread():
            while not self.stop_measurement_thread:
                result = self.t.run(profiler_cmd, hide=True)
                self.cpu_usage = float(result.stdout.strip())
                print(f'CPU Usage: {self.cpu_usage}%')
                time.sleep(1)

        self.t_thread = threading.Thread(target=profiler_thread)
        self.t_thread.start()


    def interact(self, context: RunnerContext) -> None:
        """Perform any interaction with the running target system here, or block here until the target finishes."""

        output.console_log("Config.interact() called!")

    def stop_measurement(self, context: RunnerContext) -> None:
        """Perform any activity here required for stopping measurements."""

        output.console_log("Config.stop_measurement called!")
        self.stop_measurement_thread = True
        self.t_thread.join()
        self.t.close()
        self.cpu_usage = None

    def stop_run(self, context: RunnerContext) -> None:
        """Perform any activity here required for stopping the run.
        Activities after stopping the run should also be performed here."""

        output.console_log("Config.stop_run() called!")

        # Stop the thread that gets the CPU usage
        self.stop_run_thread = True
        self.c_thread.join()

        # Close the fabric connection
        self.c.close()

    def populate_run_data(self, context: RunnerContext) -> Optional[Dict[str, Any]]:
        """Parse and process any measurement data here.
        You can also store the raw measurement data under `context.run_dir`
        Returns a dictionary with keys `self.run_table_model.data_columns` and their values populated"""

        output.console_log("Config.populate_run_data() called!")

        # Close the connection
        self.c.close()
        return None

    def after_experiment(self) -> None:
        """Perform any activity required after stopping the experiment here
        Invoked only once during the lifetime of the program."""

        output.console_log("Config.after_experiment() called!")

    # ================================ DO NOT ALTER BELOW THIS LINE ================================
    experiment_path:            Path             = None
