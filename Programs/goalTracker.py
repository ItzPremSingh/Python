from datetime import datetime, timedelta
from argparse import ArgumentParser


def main() -> None:
    parser = ArgumentParser(
        description="Calculate the days remaining for a redemption goal"
    )

    parser.add_argument(
        "-now",
        "-n",
        type=int,
        help="Total coins at present (required)",
        required=True,
    )
    parser.add_argument(
        "-daily",
        "-d",
        type=int,
        help="Total coins obtained daily (default 82)",
        default=60,
    )
    parser.add_argument(
        "-target",
        "-t",
        type=int,
        help="Redemption target (default 8150)",
        default=8150,
    )

    args = parser.parse_args()

    today = datetime.now().date()

    leftTokens = (args.target - args.now) % args.daily

    daysLeft = (args.target - args.now + args.daily - 1) // args.daily
    completeDate = today + timedelta(days=daysLeft)

    totalCompleted = int(args.now / args.target * 100)

    print(f"\nDays left: {daysLeft} ({totalCompleted}% completed)")
    print(f"Left tokens: {leftTokens}")
    print(f"Redemption date: {completeDate.strftime('%A, %B %d, %Y')}")


if __name__ == "__main__":
    main()
