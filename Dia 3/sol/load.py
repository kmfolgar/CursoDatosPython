BaseDeDatos = pd.read_excel(Direccion_De_Base_De_Datos)
BaseDeDatos.index = BaseDeDatos["núm_corre"]
BaseDeDatos.drop("núm_corre", axis=1, inplace=True)
BaseDeDatos.head()