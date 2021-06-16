from app import app


if __name__ == "__main__":
    # start the web server
    print("* Starting web service...")

    app.run(host='0.0.0.0', port=5000, debug=True)
