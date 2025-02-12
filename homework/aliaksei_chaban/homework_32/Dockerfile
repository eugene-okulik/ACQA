FROM python
COPY homework/aliaksei_chaban/homework_32/to_run_via_docker.py .
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "to_run_via_docker.py"]
