"""
Script que lê o CSV com todos os cfop e gera um sql para inserir no BD
"""

# abre o arquivo csv
with open('tabela-cfop', 'r') as cfop_file:
    # esqueleto do sql
    sql = "INSERT INTO cfop (cfop, descricao) values "

    # lê as linhas
    for linha in cfop_file.readlines():
        cfop, descricao = linha.split(';')
        descricao = descricao.replace('"', '', 2)
        descricao = descricao.replace('\n', '')

        # adiciona no sql
        sql += "('%s', '%s'), " % (cfop, descricao.upper())

# retira a vírgula do final
sql = sql[0:-2] + ';'

# salva o sql em um arquivo separado
with open('cfop.sql', 'w') as sql_file:
    sql_file.write(sql)
