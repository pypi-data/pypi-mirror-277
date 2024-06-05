import click

from hello_world import subtract


@click.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def main(a, b):
    """Simple program that subtracts two numbers."""
    result = subtract(a, b)
    click.echo(f"The result of {a} - {b} is {result}")


if __name__ == "__main__":
    main()
