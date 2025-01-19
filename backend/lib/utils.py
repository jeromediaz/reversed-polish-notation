import csv
import io
from typing import Iterable, TYPE_CHECKING

from fastapi.responses import StreamingResponse

if TYPE_CHECKING:
    from lib.persistence import Calculation

def calculations_as_csv_response(calculations: Iterable["Calculation"]) -> StreamingResponse:
    """
    Function to convert a list of persisted calculations into a CSV response.

    Args:
        calculations (Iterable[Calculation): Reverse Polish notation expression.

    Returns:
        StreamingResponse: response object to be returned by a FastAPI endpoint.

    """

    stream = io.StringIO()

    csv_writer = csv.writer(stream, delimiter=';')

    csv_writer.writerow(["id", "expression", "created_date", "result"])

    for calculation in calculations:
        csv_writer.writerow([calculation.id, calculation.expression, calculation.created_date, calculation.result])

    response = StreamingResponse(iter([stream.getvalue()]),
                                 media_type="text/csv"
                                )

    response.headers["Content-Disposition"] = "attachment; filename=export.csv"

    return response
