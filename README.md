# Flask URL Shortener

Flask URL shortener is a tool that takes any URL and generates a shorter, more readable version like bit.ly.

`.env` file contents:

```
SECRET_KEY=verysecretkey
DATABASE_URL=sqlite:///shorty.db
APP_SETTINGS=config.DevelopmentConfig
FLASK_APP=core
```

While deploying the app, make sure you change the `APP_SETTINGS` to `config.ProductionConfig`.

