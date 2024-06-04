import click
from hello_world import greet_user

@click.command()
@click.argument('user_input', type=str)
def greet(user_input):
    """Respond with a greeting based on user input."""
    response = greet_user(user_input)
    click.echo(response)

if __name__ == '__main__':
    greet()

