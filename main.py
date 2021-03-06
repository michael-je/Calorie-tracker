"""
Entry point of the script.
Contains most of the interface logic.
"""

import datetime
import sqlite3
import logging

import db
import cli
import cfg

ORM = db.CalorieCounterORM(cfg.DB_PATH)


def main():
    """
    Main function of the program
    """
    args = cli.parser.parse_args()

    if args.subparser_name == "food":
        logging.info("food subparser used")

        new_data = db.QueryData(
            food_name=args.food,
            portion_type=args.type,
            calories=args.calories
        )
        ORM.add_row_to_table('food', new_data)

    elif args.subparser_name == "entry":
        logging.info("entry subparser used")

        new_data = db.QueryData(
            food_name=args.food,
            portion_type=args.type,
            servings=args.servings,
            date=args.date
        )
        ORM.add_row_to_table('record', new_data)

    else:
        logging.info("No subparser used")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format=(
            "%(asctime)s - %(levelname)-7s - " +
            "%(lineno)4s:%(funcName)-25s - %(message)s"
        ),
    )
    logging.info("Starting script")
    main()
