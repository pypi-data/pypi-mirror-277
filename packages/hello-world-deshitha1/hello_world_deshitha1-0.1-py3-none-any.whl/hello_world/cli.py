import click
from hello_world import greet_user

@click.command()
@click.argument('user_input', nargs=-1, type=str)
def greet(user_input):
    # Join all arguments into a single string
    input_str = ' '.join(user_input)
    response = greet_user(input_str)
    click.echo(response)

if __name__ == '__main__':
    greet()
