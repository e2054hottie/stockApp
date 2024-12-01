from databaseMappingFlamework.databaseMapping import select


class UserDao:
    @select("User",True)
    def user_select(self,id):
        pass

    @select("User")
    def sel(self,user):
        pass
    @select("User",True)
    def user_select_by_email(self,email):
        pass

    @select("User")
    def user_insert(self,name,email,password):
        pass

    @select("User")
    def user_select_all(self):
        pass