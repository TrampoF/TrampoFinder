import psycopg2

class Connection:
    def __init__(self, database='trampof'):
        self._host="localhost"  # Endereço do banco de dados
        self._user="postgres"  # Usuário do banco de dados
        self._password="100703"  # Senha do banco de dados
        self.database=database  # Nome do banco de dados
        self._connection=None
        self.cursor=None
    

    def set_host(self, host):
        self._host=host
    def set_user(self, user):
        self._user=user
    def set_password(self, password):
        self._password=password


    def get_cursor(self):
        if self.cursor: return self.cursor

        else:
            try:
                self._connection = psycopg2.connect(
                    host=self._host,
                    user=self._user,
                    password=self._password,
                    database=self.database
                )

                self.cursor = self._connection.cursor()

                return self.cursor
            
            except Exception as error:
                print(f"Erro ao conectar ao Banco de Dados: {error}")


    def close_cursor(self):
        if self.cursor:
            try:
                self.cursor.close()
            
            except Exception as error:
                print(f"Erro ao conectar ao encerrar o Cursor: {error}")
        
        else:
            print("Nenhum Cursor Aberto")


    def close_connection(self):
        if self._connection:
            try:
                if self.cursor: self.close_cursor()

                self._connection.commit()
                self._connection.close()

            except Exception as error:
                print(f"Erro ao encerrar a conexão com o Banco de Dados: {error}")

        else:
            print("Nenhuma Conexão Aberta")

    
    def force_commit(self):
        if self._connection: self._connection.commit()
        else: print("Nenhuma Conexão Aberta")


        

    





