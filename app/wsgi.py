from application import create_app
from application.model import model


model.preload_model()
app = create_app()


if __name__ == "__main__":
	# Model is nearly 120mb. It must be loaded prior to launching the Flask app.
	app.run(host='0.0.0.0', port=5001, threaded=True)
