## Project setup

### Start server
```
pip3 install -r requirements.txt
python3 manage.py runserver
```

### Start frontend
```
npm install
npm run serve
```

#### Default config in frontend/.env file
```
VUE_APP_API_URL=http://127.0.0.1:8000/api/
VUE_APP_HOST=localhost
VUE_APP_PORT=8080
```

#### Go to http://127.0.0.1:8000/admin/ (u: admin p: admin) to see django admin panel
#### Go to http://localhost:8080/ to see frontend application

Project is using sqlite3 database as a storage (default django storage).