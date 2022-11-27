from app import app
from entrada import entrada

app.register_blueprint(entrada)

# starting the app
print("hola")
if __name__ == "__main__":
    app.run(port=3000, debug=True)