import io
from typing import Iterable
import csv
from lib.persistence import Calculation
from fastapi.responses import StreamingResponse

def calculations_as_csv_response(calculations: Iterable[Calculation]) -> StreamingResponse:
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
