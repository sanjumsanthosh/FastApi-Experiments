FROM python:3.9
WORKDIR /app
COPY requirements.txt /app/requirement.txt
COPY final_model.sav /app/final_model.sav
COPY train_processed.csv /train_processed.csv
COPY valid_processed.csv /vaild_processed.csv
RUN pip install -r /app/requirement.txt
COPY . /app
RUN rm /app/config.yaml && mv /app/config.prod.yaml /app/config.yaml
EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]