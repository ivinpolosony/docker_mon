FROM django:onbuild
RUN pip install --upgrade pip
RUN pip install twython
RUN pip install python-social-auth
EXPOSE 8000
CMD ["python", "dockermon/manage.py", "runserver", "8000"]
ADD . /usr/src/app/
