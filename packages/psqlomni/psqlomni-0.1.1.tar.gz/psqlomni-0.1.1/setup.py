# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['psqlomni']

package_data = \
{'': ['*']}

install_requires = \
['halo>=0.0.31,<0.0.32',
 'langchain-community>=0.0.38,<0.0.39',
 'langchain-openai>=0.1.7,<0.2.0',
 'langchain>=0.1.20,<0.2.0',
 'prompt-toolkit>=3.0.43,<4.0.0',
 'psycopg2>=2.9.9,<3.0.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['psqlomni = psqlomni.__main__:main']}

setup_kwargs = {
    'name': 'psqlomni',
    'version': '0.1.1',
    'description': 'LLM-powered chat interface to your Postgres database - (psql powered with Natural Language)',
    'long_description': "# psqlomni  \n(psql powered with natural language)\n\nAn LLM-powered chat interface to your database. This tool understands Postgres syntax and can easily translate English queries into proper SQL queries. Uses Langchain and [Open AI](https://openai.com) model.\n\nThis provides the quickest way to enable LLM chat with your data - no preparation is needed.\n\n\nHere's a quick demo showing natural language queries:\n\nhttps://github.com/emmakodes/psqlomni/assets/34986076/0c58f4fd-c359-47c2-8e3c-4b068545e522\n\n## Installation\n\nYou will need:\n\n1. credentials for your database\n2. an OpenAI [API Key](https://platform.openai.com/account/api-keys) from your OpenAI account.\n\nthen\n\n```\npip install psqlomni\n```\n\nor download the source. \n\nRun the CLI with:\n\n    psqlomni\n\nor use `python -m psqlomni` to run from source.\n\n## What can it do?\n\nThe Open AI model understands most Postgres syntax, so it can generate both generic SQL commands as well as very Postgres-specific ones like querying system settings. It can answer questions based on the databases' schema as well as on the databases' content (like describing a specific table).\n\nThe LLM is also good at analyzing tables, understanding what they are likely used for, and inferring relationships between tables. It is good at writing JOINs between tables without explicit instruction.\n\nIt can write queries to group and summarize results.\n\nIt can recover from errors by running a generated query, catching the traceback and regenerating it correctly.\n\nIt will save tokens by only retrieving the schema from relevant tables.\n\nIt also maintains a history of the chat, so you can easily ask follow up questions.\n\n### Configuration\n\nYou can configure the database connection either using `psql` style command line arguments\nor the env vars `DBHOST`, `DBNAME`, `DBUSER`, `DBPASSWORD`, `DBPORT`.\n\nElse when you first run the program it will prompt you for the connection credentials as\nwell as your OpenAI API key.\n\nAfter first setup all the configuration information is stored in `~/.psqlomni`. Delete that\nfile if you want to start over.\n\nYou can specify the number of sample rows that will be appended to each table description. This can increase performance as demonstrated in the paper Rajkumar et al, 2022 (https://arxiv.org/abs/2204.00498). Follows best practices as specified in: Rajkumar et al, 2022 (https://arxiv.org/abs/2204.00498)\n\n## How it works\n\n`psqlomni` uses Langchain and the OpenAI model to create an agent to work with your database.\n\nWhen requested the LLM automatically generates the right SQL, ask if to execute the query, if yes(or y), it executes the query. The query results are then returned. If an error is returned, it rewrites the query, check the query, ask for confirmation to execute query and then try again.\n\n### Command Reference\n\nThere are a few system commands supported for meta operations: \n\n`help` - show system commands\n\n`connection` - show the current db connection details, and the active LLM model\n\n`exit` or ctrl-c to exit\n\n",
    'author': 'emmakodes',
    'author_email': 'emmamichael65@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
