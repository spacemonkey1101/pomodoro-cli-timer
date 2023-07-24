import click


# command group
@click.group()
def myCommands():
    pass


@click.command()
@click.option("--name", prompt="Enter your name", help="this would be a username")
def hello(name):
    click.echo(f"Hello {name}, Welcome to pomodoro timer!!")


@click.command()
@click.option("-n", "--name", prompt="Enter the task name", help="Name of the new task",required=False,default="Task")
@click.option(
    "-t",
    "--time",
    type=int,
    prompt="Enter the overall time you want to spend",
    help="This will calculate the work time and rest time",
    required=False,
    default=30
)
@click.option(
    "-d",
    "--description",
    prompt="Enter the task description",
    help="Description of the new task",
    required=False,
    default="non-urgent task"
)
def add_task(name,time=30, description="Standard Task"):
    click.echo(f"{name} added for {time//60} hours {time%60} minutes")


# add defined commands to the click group
myCommands.add_command(hello)
myCommands.add_command(add_task)


if __name__ == "__main__":
    myCommands()
