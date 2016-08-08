# Tabela CFOP em SQL
Script que gera a tabela de CFOPs em SQL para implementação em banco de dados

## Esse repositório contém um script em python que gera um SQL com os registros de CFOP (número e descrição) para inserir em BD.

### Instruções:
- Alterar a linha 8 com os dados da tabela usada no BD
- Alterar a linha 17 caso deseja que a descrição não esteja em caixa alta
```
sql += "('%s', '%s'), " % (cfop, descricao.upper())
```
para
```
sql += "('%s', '%s'), " % (cfop, descricao)
```
- Executar o script com Python 3
