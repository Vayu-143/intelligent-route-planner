from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_pdf_report(
        result,
        filepath
):

    pdf = SimpleDocTemplate(
        filepath
    )

    styles = (
        getSampleStyleSheet()
    )

    content = []

    content.append(
        Paragraph(
            "Intelligent Route Planner",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            f"Algorithm: "
            f"{result.algorithm}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Source: "
            f"{result.source}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Destination: "
            f"{result.destination}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Distance: "
            f"{result.distance} km",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Visited Nodes: "
            f"{result.visited_nodes}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "Route:",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            " → ".join(
                result.path
            ),
            styles["Normal"]
        )
    )

    pdf.build(content)