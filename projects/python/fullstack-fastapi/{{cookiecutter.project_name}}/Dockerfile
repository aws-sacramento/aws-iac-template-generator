FROM public.ecr.aws/lambda/python:{{cookiecutter.runtime}}

COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

# Copy all relevant app files
COPY ./app/api ./app/api
# COPY ./app/api ${LAMBDA_TASK_ROOT}/app/api

# Expose port 8000 in Docker and forward to localhost:80
EXPOSE {{cookiecutter.port_internal}}:{{cookiecutter.port_external}}  

# Run the API when container starts
CMD ["app.api.main.handler"]

