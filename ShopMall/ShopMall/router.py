class Router():
    def db_for_read(self, models, **hints):
        # print(models)
        return 'read'

    def db_for_write(self, models, **hints):
        return 'default'
