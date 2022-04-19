import uvicorn
import logging
from APISetup import APISetup


def main():
    """
    Runs the web service
    """
    web_service = APISetup()
    uvicorn.run(web_service.app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
