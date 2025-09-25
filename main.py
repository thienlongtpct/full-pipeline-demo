from datetime import datetime

import pytz
from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI()


# Define the API endpoint
@app.get("/current_datetime")
def get_current_datetime():
    # Define the timezone GMT+7
    timezone = pytz.timezone("Asia/Bangkok")

    # Get the current datetime in GMT+7 timezone
    current_datetime = datetime.now(timezone)

    # Return the current datetime in ISO format
    return {"current_datetime": current_datetime.isoformat()}
    return {"current_datetime": current_datetime.isoformat()}
    return {"current_datetime": current_datetime.isoformat()}
