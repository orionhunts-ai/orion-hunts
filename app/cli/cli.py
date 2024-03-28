import click
import subprocess

ORION_ASCII = """
      *
  *       *
*   *   *   *   *
  *       *
      *
"""

@click.command()
@click.argument('website_url', type=str)
def evaluate(website_url):
    """Evaluates a website for adversarial AI model signatures."""
    click.echo(ORION_ASCII)
    click.echo(f"Evaluating {ip_range} for adversarial AI model signatures...")
    
    # Replace './main' with the actual path to your compiled Go binary @TODO Alex to work this out.
    result = subprocess.run(['./main', website_url], capture_output=True, text=True)
    if result.stdout:
        click.echo(result.stdout)
    if result.stderr:
        click.echo(f"Error: {result.stderr}", err=True)

if __name__ == '__main__':
    evaluate()
