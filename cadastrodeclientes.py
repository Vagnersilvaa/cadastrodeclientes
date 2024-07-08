import tkinter as tk
import sqlite3

# JA PODE BUSCAR UM PSICOLOGO PROFESSOR

# So consegui acessar o banco de dados pelo DB Browser, coloquei ele no arquivo caso  voce queira ver.
# Para ver Clica em "Abrir Banco de Dados" e entra no arquivo TDE 4 Algoritmo e clica em "Cliente"  e dps vai em Navegar Dados.

def criar_tabela():
    
    # Conecta ao banco de dados
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()

    # Cria a tabela se ela não existir
    c.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            telefone TEXT,
            cpf TEXT,
            endereco TEXT
        )
    ''')


    # Salva as mudanças
    conexao.commit()

    # Fecha a conexão com o banco de dados
    conexao.close()


def cadastrar_cliente():
    # Conecta ao banco de dados
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()

    # Insere dados na tabela
    c.execute("INSERT INTO clientes (nome, telefone, cpf, endereco) VALUES (?, ?, ?, ?)",
              (nome_entry.get(), telefone_entry.get(), cpf_entry.get(), endereco_entry.get()))

    # Salva as mudanças
    conexao.commit()

    # Fecha a conexão com o banco de dados
    conexao.close()


def buscar_cliente():
    # Conecta ao banco de dados
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()

    # Busca dados do CPF
    cpf = cpf_entry.get()
    c.execute("SELECT * FROM clientes WHERE cpf=?", (cpf,))
    resultado = c.fetchone()

    if resultado:
        nome_entry.delete(0, tk.END)
        telefone_entry.delete(0, tk.END)
        endereco_entry.delete(0, tk.END)

        nome_entry.insert(0, resultado[1])
        telefone_entry.insert(0, resultado[2])
        endereco_entry.insert(0, resultado[4])
    else:
        tk.messagebox.showinfo("Cliente não encontrado", "CPF não encontrado na base de dados.")

    # Fecha a conexão com o banco de dados
    conexao.close()


def excluir_cliente():
    # Conecta ao banco de dados
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()

    # Exclui dados do CPF
    cpf = cpf_entry.get()
    c.execute("DELETE FROM clientes WHERE cpf=?", (cpf,))

    # Salva as mudanças
    conexao.commit()

    # Fecha a conexão com o banco de dados
    conexao.close()


# Cria a tabela (chamada apenas uma vez)
criar_tabela()

janela = tk.Tk()
janela.title('Cadastro de Clientes')
janela.geometry("330x350")


# Campos de entrada
nome_label = tk.Label(janela, text="Nome:")
nome_entry = tk.Entry(janela)

telefone_label = tk.Label(janela, text="Telefone:")
telefone_entry = tk.Entry(janela)

cpf_label = tk.Label(janela, text="CPF:")
cpf_entry = tk.Entry(janela)

endereco_label = tk.Label(janela, text="Endereço:")
endereco_entry = tk.Entry(janela)


# Botões Cadatrar, Buscar, Excluir
cadastrar_button = tk.Button(janela, text="Cadastrar", command=cadastrar_cliente)
buscar_button = tk.Button(janela, text="Buscar", command=buscar_cliente)
excluir_button = tk.Button(janela, text="Excluir", command=excluir_cliente)


# Posicionamento dos widgets
nome_label.pack()
nome_entry.pack()

telefone_label.pack()
telefone_entry.pack()

cpf_label.pack()
cpf_entry.pack()

endereco_label.pack()
endereco_entry.pack()

cadastrar_button.pack()
buscar_button.pack()
excluir_button.pack()

janela.mainloop()


