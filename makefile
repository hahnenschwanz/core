frontend:
	@echo "Building frontend..."
	cd frontend && yarn install && yarn build
	@rm -rf src/web/static
	@mkdir -p src/web/static
	@cp -r frontend/build/* src/web/static/
	@echo "Done building frontend"

backend:
	@echo "Getting backend dependencies..."
	pip install -r requirements.txt
	@echo "Done building backend"

run:
	@echo "Running backend..."
	python3 src/app.py