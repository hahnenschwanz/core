frontend:
	@echo "Building frontend..."
	cd frontend && yarn install --ignore-engines && yarn build 
	@rm -rf src/web/static
	@mkdir -p src/web/static
	@cp -r frontend/build/* src/web/static/
	@echo "Done building frontend"

backend:
	@echo "Getting backend dependencies..."
	pip install -r requirements.txt
	@echo "Done building backend"

database:
	@echo "Removing old database..."
	@rm -f database.db
	@echo "Creating new database..."
	@python3 src/add_cocktails.py
	@echo "Done updating database"

run:
	@echo "Running backend..."
	python3 src/app.py
