
FROM node:14 as frontend_base

WORKDIR /app/frontend

COPY frontend /app/frontend
COPY src /app/backend

FROM frontend_base as frontend
RUN yarn install
RUN yarn build

FROM backend_base as backend
COPY requirements.txt /app/backend
RUN pip install -r requirements.txt

# Final image combining frontend and backend
FROM backend_base as final
COPY --from=frontend /app/frontend/build /app/backend/src/web/static
COPY --from=backend /usr/local /usr/local

# Expose the port your backend is running on
EXPOSE 8000

# Command to run the application
CMD ["python3", "/app/backend/src/app.py"]
