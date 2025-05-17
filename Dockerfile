FROM python:3.10

#muhut ozgaruvchilari
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONNUNBUFFERED=1

#loyhani joylash uchun yengi fayl
WORKDIR /app
#KUTUBHONALARNI O"RNATISH
COPY requirements.txt .
RUN pip install -r requirements.txt
#Django ni loyhani klonlimz 
COPY . .
# PORT Ochih uchun
RUN python manage.py migrate
EXPOSE 8000
#serverni ishga tushurish
CMD ["python","manage.py","runserver","127.0.0.1:8000"]

