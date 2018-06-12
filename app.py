from fundz.make_app import make_app, make_config


config = make_config()
app = make_app(config)

if __name__ == "__main__":
    app.run(port=config['PORT'])
