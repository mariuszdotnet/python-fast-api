# Python FastAPI on Azure Web Apps (Linux)

Live Demo API [running on Azure](https://python-fast-api-mk.azurewebsites.net/).

## To run the application locally:

1. Go to the application folder:

    ```Console
    cd python-fast-api
    ```

2. Create a virtual environment for the app:

    ```Console
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Install the dependencies as per the [documentation](https://fastapi.tiangolo.com/tutorial/):
    ```Console
    pip install fastapi
    pip install uvicorn[standard]
    ```

4. Generate the requirements.txt file for Azure deployment.
    ```Console
    pip freeze > requirements.txt
    ```

5. Test install the dependencies with the requirements.txt file. (OPTIONAL)
    ```Console
    pip install -r requirements.txt
    ```

6. Run the app:
    ```Console
    uvicorn main:app --reload
    ```

## To run the application on Azure App Service:

1. In the Azure Web App under `Settings` -> `Configuration` -> `Application settings` make sure the application setting `SCM_DO_BUILD_DURING_DEPLOYMENT` is defined and set to `1`.  This instructs the build of the webapp container to install the `requirements.txt` dependencies for your application.

2. In the Azure Web App under `Settings` -> `Configuration` -> `Application settings` -> `Startup Command` orovide an optional startup command that will be run as part of container startup. [learn more](https://learn.microsoft.com/en-us/troubleshoot/azure/app-service/faqs-app-service-linux#built-in-images)
    ```Console
    gunicorn -k uvicorn.workers.UvicornWorker main:app
    ```

### Note:
`uvicorn.workers.UvicornWorker` is an ASGI worker class for Gunicorn that wraps the uvicorn server. It is used to run ASGI applications with Gunicorn. The Azure App Serice image for Linux with Python runtime runs Gunicorn by default.

You can build your own custom image to run Fast API on `Azure Web Apps` as described [here](https://learn.microsoft.com/en-us/azure/developer/python/tutorial-containerize-simple-web-app-for-app-service?tabs=web-app-fastapi).

You can build your own custom image to run FastAPI on `Azure Container Apps`as described [here](https://learn.microsoft.com/en-us/azure/developer/python/tutorial-containerize-simple-web-app?tabs=web-app-flask).

## References:
- [FastAPI](https://fastapi.tiangolo.com/)
- [Configure a Linux Python app for Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/configure-language-python)
- [Deploy FastAPI and uvicorn on Azure app service](https://stackoverflow.com/questions/66251679/deploy-fastapi-and-uvicorn-on-azure-app-service)
- [Running Gunicorn](https://docs.gunicorn.org/en/latest/run.html)
- [Gunicorn Worker Class Docs](https://docs.gunicorn.org/en/latest/settings.html#worker-class)
- [Gunicorn WSGI](https://www.uvicorn.org/)
- [Uvicorn ASGI](https://gunicorn.org/)
- [Difference between WSGI and ASGI ?](https://medium.com/analytics-vidhya/difference-between-wsgi-and-asgi-807158ed1d4c)