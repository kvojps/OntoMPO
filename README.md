# OntoMPO

# Desenvolvimento

## Configuração do ambiente

1. Criação do ambiente virtual python:
   ```bash
   python -m venv .venv
   ```
2. Ativação do ambiente virtual:

   ```bash
   # Linux
   source .venv/bin/activate

   # Windows
   .\.venv\Scripts\activate
   ```

3. Se necessário, atualize o PIP:
   ```bash
   python.exe -m pip install --upgrade pip
   ```
4. Instalação das dependências de desenvolvimento:
   ```bash
   pip install -r requirements-dev.txt
   ```
5. Instalação das dependências do projeto:
   ```bash
   pip install -r requirements.txt
   ```
   <br/>

## Configuração de extensões para desenvolvimento (VsCode)

- Instalação da extensão **MyPy Type Checker** para ser possível a verificação de tipagem no código durante o desenvolvimento do projeto;
  - **ID da extensão**: ms-python.mypy-type-checker;
- Instalação da extensão **isort** para organização dos imports nos arquivos;
  - **ID da extensão**: ms-python.isort;
- Instalação da extensão **Black Formatter** para formatação adequada do código python;
  - **ID da extensão**: ms-python.black-formatter;

**Observação:** Todas as extensões acima são disponibilizadas pela Microsoft.
<br/>

# Execução do projeto

## Local

Na raiz do projeto, execute o seguinte comando para iniciar a API FastAPI localmente via HTTP:

```bash
uvicorn api.app:app --reload
```

Para acessar a documentação dos endpoints, acesse: [http://localhost:8000](http://localhost:8000).
