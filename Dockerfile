FROM python:3.8-slim

# Create app directory
WORKDIR /m-a-activity

# Install pipeline dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Bundle app source
COPY src /m-a-activity/src
COPY input_data /m-a-activity/input_data
CMD [ "python3", "src/m_a_pipeline.py" ]