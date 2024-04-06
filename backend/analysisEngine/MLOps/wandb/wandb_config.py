"""
Configuration Class  for WandB.

"""
import wandb

class WandBHelper:
    """
    A helper class for managing Weights & Biases experiments.
    """
    def __init__(self, project: str, entity: str):
        self.project = project
        self.entity = entity
        wandb.login()

    def start_run(self, run_name: str = None, config: dict = None) -> None:
        """Starts a W&B run with the given configuration."""
        wandb.init(project=self.project, entity=self.entity, name=run_name, config=config)

    def log(self, data: dict) -> None:
        """Logs the given data to the current W&B run."""
        wandb.log(data)

    def finish_run(self) -> None:
        """Finishes the current W&B run."""
        wandb.finish()
