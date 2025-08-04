import click
from .timer import countdown
from .notifier import notify

@click.command()
@click.option('--focus', default=25, help='Focus duration in minutes')
@click.option('--short-break', default=5, help='Short break duration in minutes')
@click.option('--long-break', default=15, help='Long break duration in minutes')
@click.option('--cycles', default=4, help='Number of Pomodoro cycles before a long break')
def main(focus, short_break, long_break, cycles):
    for i in range(1, cycles + 1):
        countdown(focus, "Focus Time")
        notify("Focus Complete", f"Take a {'long' if i == cycles else 'short'} break!")

        if i == cycles:
            countdown(long_break, "Long Break")
        else:
            countdown(short_break, "Short Break")

if __name__ == '__main__':
    main()
