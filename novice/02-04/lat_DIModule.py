#dependency Module

class AppModule:

    @singleton
    @provider
    def provide_business_logic(self, api: Api) -> BusinessLogic:
        return BusinessLogic(api=api)

    @singleton
    @provider
    def provide_api(self) -> Api:

        configuration

        return Api()

if __name__ == '__main__':
    injector = Injector(AppModule())

    logic = injector.get(BusinessLogic)
    logic.do_stuff()