from answerkiller import app


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True,
            static_files={'/': '/home/kexi/projects/flaskapp/answerkiller/answerkiller/templates/admin'})
