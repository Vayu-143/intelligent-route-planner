from datetime import datetime


def generate_text_report(
        result,
        filepath
):

    with open(
        filepath,
        "w"
    ) as file:

        file.write(
            "INTELLIGENT ROUTE PLANNER\n"
        )

        file.write(
            "=" * 50
        )

        file.write("\n\n")

        file.write(
            f"Generated : "
            f"{datetime.now()}\n\n"
        )

        file.write(
            f"Algorithm : "
            f"{result.algorithm}\n"
        )

        file.write(
            f"Source : "
            f"{result.source}\n"
        )

        file.write(
            f"Destination : "
            f"{result.destination}\n"
        )

        file.write(
            f"Distance : "
            f"{result.distance} km\n"
        )

        file.write(
            f"Visited Nodes : "
            f"{result.visited_nodes}\n\n"
        )

        file.write(
            "Route:\n"
        )

        file.write(
            " -> ".join(
                result.path
            )
        )